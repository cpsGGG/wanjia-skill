"""Build an exclusive deterministic ZIP from the reviewed public manifest."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MEDIA = {'.mp4','.mkv','.webm','.mov','.mp3','.wav','.m4a','.opus','.flac','.zip','.7z'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or output.with_suffix(output.suffix+'.sha256').exists():
        raise ValueError('Refusing an existing output')
    if output.suffix != '.zip':
        raise ValueError('Output must be a ZIP')
    manifest = json.loads((ROOT/'package-manifest.json').read_text('utf-8'))
    members = sorted([*manifest['files'],'package-manifest.json'])
    contents = {}
    for name in members:
        relative = PurePosixPath(name)
        if relative.is_absolute() or '..' in relative.parts or '\\' in name or ':' in name:
            raise ValueError('Unsafe manifest member')
        if any(x in {'.git','__pycache__','dist'} or x.startswith('.env') for x in relative.parts):
            raise ValueError('Private or generated manifest member')
        path = ROOT.joinpath(*relative.parts)
        if path.is_symlink() or path.suffix.lower() in MEDIA or not path.resolve().is_relative_to(ROOT):
            raise ValueError('Unsafe source file')
        data = path.read_bytes()
        if name != 'package-manifest.json':
            pin = manifest['files'][name]
            if len(data) != pin['bytes'] or hashlib.sha256(data).hexdigest() != pin['sha256']:
                raise ValueError('Reviewed content changed: '+name)
        contents[name] = data
    subprocess.run([sys.executable,'-B',str(ROOT/'tools/verify_package.py')],cwd=ROOT,check=True)
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for name,data in contents.items():
            info = zipfile.ZipInfo('玩家.skill/'+name,date_time=(1980,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info,data,compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or len(archive.infolist()) != len(contents):
            raise ValueError('ZIP CRC or member count mismatch')
        for name,data in contents.items():
            if archive.read('玩家.skill/'+name) != data:
                raise ValueError('ZIP content mismatch')
    sha = hashlib.sha256(output.read_bytes()).hexdigest()
    with output.with_suffix(output.suffix+'.sha256').open('x',encoding='utf-8') as file:
        file.write(sha+'  '+output.name+'\n')
    print(json.dumps({'status':'PASS_PUBLIC_PACKAGE_BUILD','version':manifest['version'],
        'members':len(contents),'bytes':output.stat().st_size,'zip_sha256':sha},ensure_ascii=False))

if __name__ == '__main__':
    main()
