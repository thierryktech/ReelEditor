#!/usr/bin/env python3
"""Check export properties with ffprobe. Does not assess visual fidelity."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import subprocess

def inspect(data, seconds=16.0, width=1080, height=1920, fps=30.0, silent=False):
    checks = []
    def add(name, ok, actual):
        checks.append({'check': name, 'pass': bool(ok), 'actual': actual})
    streams = data.get('streams', [])
    videos = [s for s in streams if s.get('codec_type') == 'video']
    audio = [s for s in streams if s.get('codec_type') == 'audio']
    add('one_video_stream', len(videos) == 1, len(videos))
    if videos:
        video = videos[0]
        add('resolution', (video.get('width'), video.get('height')) == (width, height),
            [video.get('width'), video.get('height')])
        add('h264', video.get('codec_name') == 'h264', video.get('codec_name'))
        add('yuv420p', video.get('pix_fmt') == 'yuv420p', video.get('pix_fmt'))
        try:
            actual_fps = float(Fraction(video.get('avg_frame_rate', '0/1')))
        except (ValueError, ZeroDivisionError):
            actual_fps = 0
        add('fps', abs(actual_fps - fps) < 0.001, actual_fps)
    try:
        duration = float(data.get('format', {}).get('duration', 'nan'))
    except (ValueError, TypeError):
        duration = float('nan')
    add('duration', abs(duration - seconds) <= 1 / fps + 0.001,
        duration if duration == duration else None)
    formats = data.get('format', {}).get('format_name', '').split(',')
    add('mp4_container', 'mp4' in formats, formats)
    if silent:
        add('no_audio_stream', not audio, len(audio))
    return {'pass': all(c['pass'] for c in checks), 'checks': checks,
            'visual_review': 'not-run', 'faststart_check': 'not-run'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--seconds', type=float, default=16)
    parser.add_argument('--width', type=int, default=1080)
    parser.add_argument('--height', type=int, default=1920)
    parser.add_argument('--fps', type=float, default=30)
    parser.add_argument('--silent', action='store_true')
    args = parser.parse_args()
    if min(args.seconds, args.width, args.height, args.fps) <= 0:
        parser.error('Duration, dimensions and fps must be positive.')
    if not args.video.is_file():
        parser.error('Video file does not exist.')
    try:
        run = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format',
                              '-of', 'json', str(args.video.resolve())],
                             capture_output=True, text=True, check=True, timeout=60)
        result = inspect(json.loads(run.stdout), args.seconds, args.width,
                         args.height, args.fps, args.silent)
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        parser.exit(2, f'Unable to inspect video: {exc}\n')
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result['pass'] else 1)

if __name__ == '__main__':
    main()
