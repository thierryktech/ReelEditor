#!/usr/bin/env python3
"""Inventory originals without modifying image bytes. No external dependencies."""
import argparse
import hashlib
import json
from pathlib import Path

EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4', '.mov', '.wav', '.mp3'}

def inventory(directory):
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise ValueError(f'Asset directory does not exist: {directory}')
    result = []
    for path in sorted(directory.rglob('*')):
        if path.is_symlink() or not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(block)
        result.append({'path': path.relative_to(directory).as_posix(),
                       'size_bytes': path.stat().st_size, 'sha256': digest.hexdigest(),
                       'visual_review': 'not-run'})
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        data = json.dumps(inventory(args.directory), ensure_ascii=False, indent=2) + '\n'
        if args.output:
            # Refuse to overwrite the original input asset tree.
            source = args.directory.resolve()
            target = args.output.resolve()
            if target == source or source in target.parents:
                parser.error('Write the inventory outside the source asset directory.')
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(data, encoding='utf-8')
        else:
            print(data, end='')
    except (OSError, ValueError) as exc:
        parser.exit(2, f'{exc}\n')

if __name__ == '__main__':
    main()
