"""Standard-library-only frozen-tree metrics and runtime permission measurement."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import os
import subprocess
import sys

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def local(home, value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('Expected a nonempty forward-slash local file path')
    relative = Path(value)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('External resource path: ' + value)
    result = (Path(home) / relative).resolve()
    if not result.is_relative_to(Path(home).resolve()) or not result.is_file():
        raise ValueError('Missing/nonlocal resource: ' + value)
    return result

def files(home):
    home = Path(home).resolve()
    output = []
    for p in sorted(home.rglob('*')):
        if '__pycache__' in p.parts or p.suffix == '.pyc':
            continue
        if p.is_symlink() or getattr(p, 'is_junction', lambda: False)():
            raise ValueError('Links/junctions cannot enter a frozen distribution: ' + str(p))
        if p.is_file():
            if not p.resolve().is_relative_to(home):
                raise ValueError('File escapes frozen tree')
            output.append(p)
    return output

def snapshot(home):
    home = Path(home).resolve()
    return {p.relative_to(home).as_posix(): {'sha256': digest(p.read_bytes()), 'bytes': p.stat().st_size}
            for p in files(home)}

def rows(home):
    return [json.loads(line) for line in local(home, 'references/knowledge.jsonl').read_text('utf-8-sig').splitlines() if line.strip()]

def collect_metrics(home):
    home = Path(home).resolve()
    knowledge = rows(home)
    index = read_json(local(home, 'references/source-index.json'))
    sources = index['sources']
    by_id = {r['id']: r for r in knowledge}
    if len(by_id) != len(knowledge) or len({s['source_id'] for s in sources}) != len(sources):
        raise ValueError('Duplicate knowledge or source IDs')
    atom_authority = read_json(local(home, 'references/atom-authority.json'))
    method_authority = read_json(local(home, 'references/method-authority.json'))
    registered = set(atom_authority['atom_payload_sha256'])
    method_ids = set(method_authority)
    if not method_ids <= registered or not registered <= set(by_id):
        raise ValueError('Atom/method authority has missing or inconsistent IDs')
    concept_ids = registered - method_ids
    for kid in registered:
        expected_kind = 'isolated_action_method' if kid in method_ids else 'isolated_concept_atom'
        if by_id[kid].get('status', {}).get('payload_kind') != expected_kind:
            raise ValueError('Registered payload kind mismatch: ' + kid)
        if digest(canonical(by_id[kid])) != atom_authority['atom_payload_sha256'][kid]:
            raise ValueError('Atom-authority object hash mismatch: ' + kid)
    unregistered = {r['id'] for r in knowledge if r.get('status', {}).get('payload_kind') in
                    {'isolated_action_method', 'isolated_concept_atom'}} - registered
    if unregistered:
        raise ValueError('Unregistered isolated payloads: ' + ', '.join(sorted(unregistered)))
    source_ids = {s['source_id'] for s in sources}
    knowledge_counts = Counter(r['source_id'] for r in knowledge)
    if not set(knowledge_counts) <= source_ids:
        raise ValueError('Unknown knowledge source')
    source_types = Counter()
    per_source = {}
    video_segments = community_segments = 0
    for source in sources:
        sid = source['source_id']
        if source['knowledge_count'] != knowledge_counts[sid]:
            raise ValueError('Index knowledge_count mismatch: ' + sid)
        kind = source.get('source_kind', 'youtube_local_video')
        source_types[kind] += 1
        key = 'fulltext' if kind == 'youtube_community_post' else 'transcript'
        doc = read_json(local(home, source[key]))
        count = len(doc['segments'])
        if key == 'fulltext':
            community_segments += count
        else:
            video_segments += count
        for field in ('source_analysis', 'untrimmed_transcript', 'excluded_segments_ledger', 'audio_correction_overlay'):
            if source.get(field):
                local(home, source[field])
        selected = [r for r in knowledge if r['source_id'] == sid]
        per_source[sid] = {'knowledge': len(selected),
                          'source_original_knowledge': sum(r['id'] not in registered for r in selected),
                          'isolated_concept_atoms': sum(r['id'] in concept_ids for r in selected),
                          'isolated_action_methods': sum(r['id'] in method_ids for r in selected),
                          'segments': count, 'source_kind': kind, 'text_path': source[key]}
    levels = {'direct', 'context_only', 'hold', 'do_not_generalize'}
    incomplete = sum(not (isinstance(r.get('status'), dict)
                     and r['status'].get('cross_use_level') in levels
                     and type(r['status'].get('first_person_allowed')) is bool
                     and type(r['status'].get('action_advice_allowed')) is bool) for r in knowledge)
    counts = {'sources': len(sources),
              'video_sources': sum(n for k, n in source_types.items() if k != 'youtube_community_post'),
              'community_sources': source_types['youtube_community_post'],
              'knowledge': len(knowledge), 'source_original_knowledge': len(knowledge) - len(registered),
              'isolated_concept_atoms': len(concept_ids), 'isolated_action_methods': len(method_ids),
              'video_segments': video_segments, 'community_segments': community_segments,
              'packaged_images': sum(p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.gif'} for p in files(home)),
              'incomplete_permission_schema_rows': incomplete}
    return {'counts': counts, 'source_types': dict(sorted(source_types.items())),
            'per_source': per_source, 'concept_atom_ids': sorted(concept_ids), 'method_ids': sorted(method_ids)}

def runtime_probe(home):
    home = Path(home).resolve()
    code = """import json,sys,hashlib,platform
from pathlib import Path
sys.dont_write_bytecode=True
home=Path(sys.argv[1]);sys.path.insert(0,str(home/'scripts'))
import runtime_policy as p
rows=p.STORE.rows()
person=p.permission_decisions(rows)
action=p.permission_decisions(rows,'action_advice')
print(json.dumps({'personification_allowed_ids':sorted(d['knowledge_id'] for d in person if d['allowed']),
'action_advice_allowed_ids':sorted(d['knowledge_id'] for d in action if d['allowed']),
'personification_allowed':sum(d['allowed'] for d in person),
'action_advice_allowed':sum(d['allowed'] for d in action),
'python_version':platform.python_version(),
'authority_and_runtime_hashes':{f:hashlib.sha256((home/f).read_bytes()).hexdigest() for f in
['references/atom-authority.json','references/method-authority.json','scripts/runtime_policy.py','scripts/search.py','scripts/read_context.py','scripts/action.py','scripts/resource_utils.py']}},ensure_ascii=False))
"""
    command = [sys.executable, '-B', '-c', code, str(home)]
    result = subprocess.run(command, cwd=home, capture_output=True, encoding='utf-8', timeout=120,
                            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
    if result.returncode:
        raise ValueError('Runtime measurement failed: ' + result.stderr[:1000])
    return json.loads(result.stdout)
