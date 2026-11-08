"""Prevent the CI negative test from accepting a success or unrelated crash."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ci_refusal_probe import require_refusal


class RefusalProbeTests(unittest.TestCase):
    def test_success_with_error_text_is_not_a_refusal(self):
        with self.assertRaises(RuntimeError):
            require_refusal(0, 'MD025', 'MD025')

    def test_unrelated_failure_is_not_the_expected_refusal(self):
        with self.assertRaises(RuntimeError):
            require_refusal(1, 'Cannot find checker', 'ST-999999')

    def test_nonzero_with_expected_diagnostic_is_accepted(self):
        require_refusal(1, 'ERROR: unknown ST-999999', 'ST-999999')


if __name__ == '__main__':
    unittest.main()
