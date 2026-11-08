"""Download, verify, and extract the complete public WTS training split."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import urllib.request


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'TRAINING_DOWNLOADS.json').read_text(encoding='utf-8'))
    cache = root / '.downloads'
    cache.mkdir(exist_ok=True)
    for record in manifest['files']:
        archive = cache / record['name']
        if not archive.exists() or hashlib.sha256(archive.read_bytes()).hexdigest() != record['sha256']:
            request = urllib.request.Request(record['url'], headers={'User-Agent': 'WTS-training-download'})
            with urllib.request.urlopen(request, timeout=90) as response, archive.open('wb') as stream:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    stream.write(chunk)
        if hashlib.sha256(archive.read_bytes()).hexdigest() != record['sha256']:
            raise RuntimeError('Archive checksum mismatch: ' + record['name'])
        with ZipFile(archive) as bundle:
            for name in bundle.namelist():
                target = (root / name).resolve()
                if root.resolve() not in target.parents:
                    raise RuntimeError('Invalid archive member: ' + name)
            bundle.extractall(root)
        print('Verified and extracted ' + record['name'])
    import csv
    with (root / 'training_manifest.csv').open(encoding='utf-8', newline='') as stream:
        for record in csv.DictReader(stream):
            path = root / record['path']
            if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
                raise RuntimeError('Extracted file checksum mismatch: ' + record['path'])
    for folder in ['img', 'label_1D', 'label_3D']:
        count = sum(p.is_file() for p in (root / 'train' / folder).iterdir())
        if count != 871:
            raise RuntimeError('Unexpected training file count: ' + folder)
    print('Complete WTS training split verified: 871 images and matching masks.')


if __name__ == '__main__':
    main()
