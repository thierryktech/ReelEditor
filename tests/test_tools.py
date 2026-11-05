import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.claude/skills/balena-video'

def load(name):
    spec = importlib.util.spec_from_file_location(name, SKILL / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class ExportChecks(unittest.TestCase):
    def setUp(self):
        self.module = load('check_video')
        self.data = {'streams': [{'codec_type':'video','codec_name':'h264',
                     'pix_fmt':'yuv420p','width':1080,'height':1920,
                     'avg_frame_rate':'30/1'}],
                     'format':{'duration':'16.000','format_name':'mov,mp4,m4a,3gp,3g2,mj2'}}
    def test_expected_export(self):
        result = self.module.inspect(self.data, silent=True)
        self.assertTrue(result['pass'])
        self.assertEqual(result['visual_review'], 'not-run')
    def test_unwanted_audio(self):
        self.data['streams'].append({'codec_type':'audio'})
        self.assertFalse(self.module.inspect(self.data, silent=True)['pass'])
    def test_wrong_resolution_and_duration(self):
        self.data['streams'][0]['width'] = 1920
        self.data['format']['duration'] = '8'
        result = self.module.inspect(self.data)
        self.assertEqual([c['check'] for c in result['checks'] if not c['pass']],
                         ['resolution', 'duration'])
    def test_invalid_probe_values(self):
        self.data['streams'][0]['avg_frame_rate'] = '0/0'
        self.data['format']['duration'] = 'N/A'
        result = self.module.inspect(self.data)
        self.assertFalse(result['pass'])
        json.dumps(result, allow_nan=False)
    def test_missing_streams(self):
        self.assertFalse(self.module.inspect({})['pass'])

class AssetChecks(unittest.TestCase):
    def test_hash_and_skip_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'original.png').write_bytes(b'original-image')
            (root/'skip.txt').write_text('not an asset')
            (root/'linked.png').symlink_to(root/'original.png')
            result = load('inventory_assets').inventory(root)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['sha256'], hashlib.sha256(b'original-image').hexdigest())
            self.assertEqual((root/'original.png').read_bytes(), b'original-image')
    def test_missing_directory(self):
        with self.assertRaises(ValueError):
            load('inventory_assets').inventory('/path-that-does-not-exist/balena')

class PackageChecks(unittest.TestCase):
    def test_reference_files_exist(self):
        import re
        body = (SKILL/'SKILL.md').read_text()
        for target in re.findall(r'\]\((references/[^)]+)\)', body):
            self.assertTrue((SKILL/target).is_file(), target)
    def test_brief_and_manifest(self):
        brief = json.loads((SKILL/'assets/brief.example.json').read_text())
        self.assertEqual(sum(brief['parts_seconds']), brief['duration_seconds'])
        self.assertEqual(brief['audio_policy'], 'silent')
        self.assertEqual(len(json.loads((SKILL/'assets/source-assets.json').read_text())), 9)

if __name__ == '__main__':
    unittest.main()
