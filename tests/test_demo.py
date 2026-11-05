import json
from pathlib import Path
import subprocess
import sys
import unittest

from spinaltap.demo import run_demo


class DemoTests(unittest.TestCase):
    def test_guard_specimens_remain_isolated_at_a_position_boundary(self):
        report = run_demo([0.016] * 50, velocity=0)
        self.assertAlmostEqual(report.final_state["y"], -0.984)
        self.assertTrue(report.oversized_delta_refused)
        self.assertTrue(report.conflicting_writes_refused)

    def test_demo_drains_backlog_and_applies_only_fixed_step_updates(self):
        report = run_demo()
        self.assertEqual(
            [frame.fixed_steps for frame in report.frames], [0, 2, 4, 4, 4, 0]
        )
        self.assertEqual(sum(frame.accepted_steps for frame in report.frames), 14)
        self.assertEqual(sum(frame.refused_steps for frame in report.frames), 0)
        self.assertAlmostEqual(report.final_position, 0.672)
        self.assertAlmostEqual(report.final_state["y"], -0.336)
        self.assertEqual(
            report.worker_order, ("vertebra:demo-lateral", "vertebra:demo-motion")
        )
        self.assertAlmostEqual(report.frames[-1].remainder, 0.008)
        self.assertTrue(report.oversized_delta_refused)
        self.assertEqual(report.guard_refusal_code, "constraint_violation")
        self.assertTrue(report.conflicting_writes_refused)
        self.assertEqual(report.conflict_refusal_code, "write_conflict")

    def test_worker_refusals_leave_demo_state_unchanged(self):
        report = run_demo(velocity=100.0)
        self.assertEqual(report.final_position, 0)
        self.assertEqual(report.final_state, {"x": 0, "y": 0})
        self.assertEqual(sum(frame.refused_steps for frame in report.frames), 14)

    def test_custom_hook_limits_position_after_worker_acceptance(self):
        report = run_demo([0.016] * 30)
        self.assertAlmostEqual(report.final_position, 0.96)
        self.assertAlmostEqual(report.final_state["y"], -0.48)
        self.assertEqual(sum(frame.accepted_steps for frame in report.frames), 20)
        self.assertEqual(sum(frame.refused_steps for frame in report.frames), 10)

    def test_module_command_emits_a_parseable_report(self):
        result = subprocess.run(
            [sys.executable, "-m", "spinaltap", "--json"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        report = json.loads(result.stdout)
        self.assertTrue(report["oversized_delta_refused"])
        self.assertAlmostEqual(report["final_position"], 0.672)
        self.assertAlmostEqual(report["final_state"]["y"], -0.336)
        self.assertTrue(report["conflicting_writes_refused"])
        self.assertEqual(len(report["frames"]), 6)


if __name__ == "__main__":
    unittest.main()
