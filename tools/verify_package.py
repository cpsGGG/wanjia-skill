"""Verify a complete local 玩家.skill distribution using only the standard library."""
from __future__ import annotations
import collections
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(home, value):
    target = (home / value).resolve()
    if not target.is_relative_to(home.resolve()) or not target.is_file():
        raise ValueError('missing/nonlocal resource: ' + str(value))
    return target


DISTRIBUTION_METADATA_BINDINGS = {'SKILL.md': {'before': {'sha256': '5b55871e3d5403e339cc0ccfbbef571177bf2588af9881ea6d75a66bdff1f82e', 'bytes': 19139}, 'after': {'sha256': '5b55871e3d5403e339cc0ccfbbef571177bf2588af9881ea6d75a66bdff1f82e', 'bytes': 19139}}, 'agents/openai.yaml': {'before': {'sha256': '828ce157c141d39a8906da6028b69832229b85453ef62fa5472ed6046bb155dd', 'bytes': 290}, 'after': {'sha256': '828ce157c141d39a8906da6028b69832229b85453ef62fa5472ed6046bb155dd', 'bytes': 290}}, 'LICENSE': {'before': {'sha256': '14331e3bc55644cd605bd3fac7e36a6789eaadc084521f7b7c1bcb38935156ef', 'bytes': 1473}, 'after': {'sha256': '14331e3bc55644cd605bd3fac7e36a6789eaadc084521f7b7c1bcb38935156ef', 'bytes': 1473}}, 'THIRD_PARTY_NOTICES.md': {'before': {'sha256': '3084f2ccdc240a4d704fcf4b3bf263e97aadf16e7b2c0e200930093fa756cc95', 'bytes': 1997}, 'after': {'sha256': '3084f2ccdc240a4d704fcf4b3bf263e97aadf16e7b2c0e200930093fa756cc95', 'bytes': 1997}}}

def runtime_content_measurement(measurement):
    # The build environment is recorded; only this environment field may differ.
    return {key: value for key, value in measurement.items() if key != 'python_version'}


def main():
    manifest = json.loads((ROOT / 'package-manifest.json').read_text(encoding='utf-8'))
    errors = []
    checks = 0

    def check(ok, description):
        nonlocal checks
        checks += 1
        if not ok:
            errors.append(description)

    expected = manifest['files']
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts and p.suffix != '.pyc'
              and '.git' not in p.relative_to(ROOT).parts
              and 'dist' not in p.relative_to(ROOT).parts
              and p != ROOT / 'package-manifest.json'}
    check(actual == set(expected), 'package file set mismatch')
    for value, pin in expected.items():
        try:
            path = local(ROOT, value)
            check(digest(path) == pin['sha256'] and path.stat().st_size == pin['bytes'],
                  'file mismatch: ' + value)
        except (OSError, ValueError) as exc:
            check(False, str(exc))
    skill = ROOT / manifest['skill_directory']
    index = json.loads((skill / 'references/source-index.json').read_text(encoding='utf-8-sig'))
    rows = [json.loads(line) for line in (skill / 'references/knowledge.jsonl').read_text(
        encoding='utf-8-sig').splitlines() if line.strip()]
    sources = index['sources']
    counts = collections.Counter(row['source_id'] for row in rows)
    summary = manifest['counts']
    check(len(sources) == len({s['source_id'] for s in sources}) == summary['sources'],
          'source count or uniqueness mismatch')
    check(len(rows) == len({r['id'] for r in rows}) == summary['knowledge'],
          'knowledge count or uniqueness mismatch')
    check(set(counts) <= {s['source_id'] for s in sources}, 'unknown knowledge source')
    video_segments = community_segments = 0
    for source in sources:
        check(source['knowledge_count'] == counts[source['source_id']],
              'per-source knowledge count: ' + source['source_id'])
        key = 'fulltext' if source.get('source_kind') == 'youtube_community_post' else 'transcript'
        try:
            document = json.loads(local(skill, source[key]).read_text(encoding='utf-8-sig'))
            length = len(document['segments'])
            if key == 'fulltext':
                community_segments += length
            else:
                video_segments += length
            for field in ('source_analysis', 'untrimmed_transcript', 'excluded_segments_ledger',
                          'audio_correction_overlay'):
                if source.get(field):
                    local(skill, source[field])
            check(True, 'registered local resource: ' + source['source_id'])
        except (KeyError, OSError, ValueError) as exc:
            check(False, source['source_id'] + ': ' + str(exc))
    check(video_segments == summary['video_segments'], 'video segment count mismatch')
    check(community_segments == summary['community_segments'], 'community segment count mismatch')
    mapping = json.loads((skill / 'references/baseline-resource-map.json').read_text(encoding='utf-8'))
    check(mapping['baseline_root'] == '.' and mapping['mode'] == 'local_materialized_only_no_external_fallback',
          'resource map uses external fallback')
    metadata_names = {'SKILL.md', 'agents/openai.yaml', 'LICENSE', 'THIRD_PARTY_NOTICES.md'}
    check(set(manifest['modified_guide_files']) <= metadata_names, 'nonmetadata guide change is not allowed')
    for value, pin in mapping['resources'].items():
        try:
            if value in metadata_names and value in manifest['modified_guide_files']:
                check(pin['sha256'] == manifest['guide_snapshot'][value]['sha256'], 'resource map original metadata pin mismatch: ' + value)
            else:
                check(digest(local(skill, value)) == pin['sha256'], 'resource map mismatch: ' + value)
        except (KeyError, OSError, ValueError) as exc:
            check(False, str(exc))
    expected_modified = set()
    for value, binding in DISTRIBUTION_METADATA_BINDINGS.items():
        try:
            check(manifest['guide_snapshot'].get(value) == binding['before'], 'metadata original snapshot mismatch: ' + value)
            path = local(skill, value)
            actual_metadata = {'sha256': digest(path), 'bytes': path.stat().st_size}
            check(actual_metadata == binding['after'] == manifest['files'][manifest['skill_directory'] + '/' + value], 'exact generated naming/document metadata mismatch: ' + value)
            if binding['before'] and binding['before']['sha256'] != binding['after']['sha256']:
                expected_modified.add(value)
        except (KeyError, OSError, ValueError) as exc:
            check(False, str(exc))
    check(expected_modified == set(manifest['modified_guide_files']), 'modified guide metadata list differs from exact naming bindings')
    for value, pin in manifest['guide_baseline_files'].items():
        if value not in manifest['modified_guide_files']:
            check(digest(local(skill, value)) == pin, 'frozen guide baseline mismatch: ' + value)
    from v2_package_support import collect_metrics, runtime_probe
    actual_policy = None
    try:
        frozen = ROOT / 'FREEZE_INPUT.json'
        ready = json.loads(frozen.read_text(encoding='utf-8-sig'))
        release = json.loads((ROOT / 'release.json').read_text(encoding='utf-8-sig'))
        check(digest(frozen) == manifest['ready_input_sha256'] == release['ready_input_sha256'], 'final ready original-byte pin mismatch')
        check(ready['guide_files'] == manifest['guide_snapshot'], 'ready and manifest full guide snapshot differ')
        check(ready['counts'] == summary == release['counts'], 'ready, manifest and release counts differ')
        check(ready['runtime_permission_measurement'] == manifest['runtime_permission_measurement'] == release['runtime_permission_measurement'], 'ready, manifest and release runtime measurements differ')
        computed = collect_metrics(skill)
        check(computed['counts'] == summary, 'dynamic V2 counts/atoms/schema mismatch')
        check(computed['source_types'] == manifest['source_types'], 'dynamic source types mismatch')
        actual_policy = runtime_probe(skill)
        check(runtime_content_measurement(actual_policy) == runtime_content_measurement(manifest['runtime_permission_measurement']), 'actual runtime permission or authority mismatch')
    except (KeyError, OSError, ValueError) as exc:
        check(False, 'V2 actual measurement: ' + str(exc))
    entry = (skill / 'SKILL.md').read_text(encoding='utf-8-sig')
    check('name: wanjia-skill' in entry and 'version: "0.2.1"' in entry, 'V2 entry metadata mismatch')
    result = {'status': 'PASS' if not errors else 'FAIL', 'checks': checks,
              'errors': errors, 'counts': summary,
              'scope': 'package integrity and local resource structure; not semantic or outcome certification'}
    result['runtime_verification_environment'] = {
        'python_version': actual_policy.get('python_version') if actual_policy else None,
        'build_python_version': manifest['runtime_permission_measurement'].get('python_version'),
        'python_version_is_content_failure_condition': False}
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
