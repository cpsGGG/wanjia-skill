"""Exercise representative retrieval and usage boundaries; print no source text."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'wanjia-skill'

def run(script, args, expected=0):
    process = subprocess.run([sys.executable, '-B', str(SKILL / 'scripts' / script), *args],
        capture_output=True, encoding='utf-8', cwd=ROOT,
        env={**os.environ, 'PYTHONIOENCODING':'utf-8'}, timeout=90)
    if process.returncode != expected:
        raise ValueError('Unexpected exit code: ' + script)
    return json.loads(process.stdout)

def main():
    checks = []
    result = run('read_context.py', ['--source-id','9zRpsnsPGxU','--sid','S02543','--before','1','--after','1'])
    segment = next(x for x in result['segments'] if x['sid'] == 'S02543')
    checks.append(segment['correction_review_required'] is True
        and segment['text_must_not_be_used_as_definite_reading'] is True
        and segment['independent_local_audio_review'] == 'not_done')
    overlay = json.loads((SKILL / 'references/audio-corrections.json').read_text('utf-8'))
    stored = next(x for x in overlay['corrections'] if x['segment_id'] == 'S02543')
    checks.append(segment['audio_correction']['review_record'] == stored)
    action = run('action.py',['--id','action-pilot-visible-photo-selection'])
    checks.append(action['allowed'] is True)
    closed = run('action.py',['--id','mikey-sijiao-001-K0001'])
    checks.append(closed['allowed'] is False)
    rejected = run('read_context.py',['--source-id','mikey-sijiao-001','--sid','S00001',
        '--knowledge-id','v2-action-001-k0001','--before','0','--after','0'],2)
    checks.append(rejected['permission_decision']['allowed'] is False)
    print(json.dumps({'status':'PASS' if all(checks) else 'FAIL','checks':len(checks),
        'passed':sum(checks),'scope':'Representative correction and approved/closed usage routes only'},ensure_ascii=False))
    return 0 if all(checks) else 1

if __name__ == '__main__':
    raise SystemExit(main())
