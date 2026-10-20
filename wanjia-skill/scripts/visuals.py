"""Find packaged still images through observed descriptions and nearby transcript text."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys

HOME = Path(__file__).resolve().parents[1]


def local_path(value):
    if not isinstance(value, str) or '\\' in value or ':' in value:
        raise ValueError('Invalid image resource path')
    relative = Path(value)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('External image resource path')
    path = (HOME / relative).resolve()
    if not path.is_relative_to(HOME) or not path.is_file():
        raise ValueError('Missing packaged resource: ' + value)
    return path


def terms(text):
    text = text.lower()
    output = set(re.findall(r'[a-z0-9][a-z0-9_-]*', text))
    for span in re.findall(r'[\u3400-\u9fff]+', text):
        if len(span) == 1:
            output.add(span)
        else:
            output.update(span[i:i+2] for i in range(len(span)-1))
    return output


def load_index():
    doc = json.loads(local_path('references/visual-index.json').read_text('utf-8'))
    if doc.get('schema_version') != 1:
        raise ValueError('Unsupported visual index schema')
    return doc


def verify(row, checked):
    path = local_path(row['path'])
    if row['path'] not in checked:
        checked[row['path']] = hashlib.sha256(path.read_bytes()).hexdigest()
    if checked[row['path']] != row['sha256']:
        raise ValueError('Image hash mismatch: ' + row['path'])
    return str(path)


def lookup(doc, query=None, source_id=None, time_seconds=None, limit=5, max_distance=30):
    wanted = terms(query) if query else set()
    results = []
    for row in doc['images']:
        if source_id and row['source_id'] != source_id:
            continue
        distance = abs(row['time_seconds']-time_seconds) if time_seconds is not None else None
        if distance is not None and distance > max_distance:
            continue
        text = ' '.join([row.get('description', ''), ' '.join(row.get('keywords', [])),
                         row.get('source_title', ''), row.get('nearby_transcript', '')]).lower()
        matched = sorted(t for t in wanted if t in text)
        if wanted and not matched:
            continue
        score = len(matched)/len(wanted) if wanted else 0
        results.append({**row, 'matched_terms': matched, 'score': score,
                        'time_distance_seconds': round(distance, 6) if distance is not None else None})
    results.sort(key=lambda r: (-(r['score']), r['time_distance_seconds'] if time_seconds is not None else 0,
                                r['source_id'], r['time_seconds'], r['id']))
    checked = {}
    selected = results[:max(0, limit)]
    for row in selected:
        row['absolute_path'] = verify(row, checked)
        row['image_sha_verified'] = True
    return selected


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('query', nargs='?')
    p.add_argument('--source-id')
    p.add_argument('--time', type=float)
    p.add_argument('--sid')
    p.add_argument('--limit', type=int, default=5)
    p.add_argument('--max-distance', type=float, default=30)
    p.add_argument('--verify', action='store_true')
    a = p.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if a.time is not None and (not math.isfinite(a.time) or a.time < 0):
        p.error('--time must be finite and nonnegative')
    if not math.isfinite(a.max_distance) or a.max_distance < 0:
        p.error('--max-distance must be finite and nonnegative')
    if a.sid and (not a.source_id or a.time is not None):
        p.error('--sid requires --source-id and cannot be combined with --time')
    if not (a.query or a.source_id or a.verify):
        p.error('a query, --source-id, or --verify is required')
    doc = load_index()
    if a.verify:
        checked = {}
        for row in doc['images']:
            verify(row, checked)
        print(json.dumps({'status': 'PASS', 'entries': len(doc['images']), 'unique_image_files': len(checked),
                          'scope': 'Packaged image paths and SHA only; no semantic, OCR, or permission certification'}))
        return
    if a.sid:
        sources = json.loads(local_path('references/source-index.json').read_text('utf-8-sig'))['sources']
        source = next((s for s in sources if s['source_id'] == a.source_id), None)
        if not source or not source.get('transcript'):
            p.error('source has no video transcript')
        transcript = json.loads(local_path(source['transcript']).read_text('utf-8-sig'))
        segment = next((s for s in transcript['segments'] if s.get('sid', s.get('segment_id')) == a.sid), None)
        if segment is None:
            p.error('SID not found in this source')
        a.time = segment['start']
    out = {'mode': 'packaged_image_navigation', 'edition': doc['edition'],
           'query': a.query, 'source_id': a.source_id, 'time_seconds': a.time, 'sid': a.sid,
           'boundary': 'Descriptions are editorial observations; nearby_transcript is saved automatic text, not image OCR. Time proximity does not prove speaker identity or causality. Open the image before describing visual facts. Navigation thumbnails may not preserve small text. No personification or action permission is added.',
           'results': lookup(doc, a.query, a.source_id, a.time, a.limit, a.max_distance)}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
