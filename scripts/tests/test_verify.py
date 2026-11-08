"""Refusal cases for the verification boundary, independent of installed tools."""
from dataclasses import asdict
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from verify import (Runner, VerificationError, require_npm_lock, require_test_count,
                    require_version, validate_demo)
from spinaltap.demo import run_demo


class VerificationTests(unittest.TestCase):
    def test_stale_npm_manifest_is_rejected_without_resolution(self):
        package = {'name': 'fixture', 'devDependencies': {'checker': '1.0.0'}}
        lock = {'lockfileVersion': 3, 'packages': {'': dict(package)}}
        require_npm_lock(package, lock)
        package['devDependencies'] = {'checker': '2.0.0'}
        with self.assertRaisesRegex(VerificationError, 'Stale package-lock.json'):
            require_npm_lock(package, lock)

    def test_actual_demo_is_accepted(self):
        validate_demo(asdict(run_demo()))

    def test_failed_guard_cannot_be_reported_as_pass(self):
        value = asdict(run_demo())
        value['oversized_delta_refused'] = False
        with self.assertRaises(VerificationError):
            validate_demo(value)

    def test_nonfinite_or_wrong_state_is_rejected(self):
        for value in (float('nan'), float('inf'), True, 0.0):
            report = asdict(run_demo())
            report['final_state']['x'] = value
            with self.assertRaises(VerificationError):
                validate_demo(report)

    def test_malformed_json_shape_is_rejected(self):
        for value in ({}, [], {'frames': []}):
            with self.assertRaises(VerificationError):
                validate_demo(value)

    def test_zero_or_absent_test_summary_is_rejected(self):
        for output in ('Ran 0 tests in 0.001s\nOK', 'OK'):
            with self.assertRaises(VerificationError):
                require_test_count(output)
        self.assertEqual(require_test_count('Ran 1 test in 0.001s\nOK'), 1)

    def test_substituted_tool_version_is_rejected(self):
        with self.assertRaises(VerificationError):
            require_version('1.2.4', '1.2.3', 'fixture')

    def test_child_failure_remains_failure_with_success_text(self):
        with tempfile.TemporaryDirectory() as directory:
            runner = Runner(Path(directory), {})
            with self.assertRaisesRegex(VerificationError, 'exit 7'):
                runner.run('fixture', [sys.executable, '-c', "print('PASS'); raise SystemExit(7)"])
            self.assertEqual(runner.stages[-1]['exit_code'], 7)

    def test_missing_child_executable_is_actionable(self):
        with tempfile.TemporaryDirectory() as directory:
            runner = Runner(Path(directory), {})
            with self.assertRaisesRegex(VerificationError, 'cannot run command'):
                runner.run('fixture', [str(Path(directory) / 'absent.exe')])


if __name__ == '__main__':
    unittest.main()
