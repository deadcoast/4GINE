"""Run the bounded SPINALTAP prototype: python -m spinaltap [--json]."""

import argparse
from dataclasses import asdict
import json

from spinaltap.demo import run_demo


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the SPINALTAP multi-worker fixed-step prototype."
    )
    parser.add_argument(
        "--json", action="store_true", help="print the structured demonstration report"
    )
    args = parser.parse_args()
    report = run_demo()
    if args.json:
        print(json.dumps(asdict(report), indent=2, allow_nan=False))
    else:
        print("SPINALTAP multi-worker fixed-step prototype")
        print(f"Worker order: {' -> '.join(report.worker_order)}")
        print("Frame  Elapsed   Steps  Accepted  Refused  Remainder  Overflow")
        for frame in report.frames:
            print(
                f"{frame.index + 1:5d}  {frame.elapsed_time:7.3f}  {frame.fixed_steps:5d}"
                f"  {frame.accepted_steps:8d}  {frame.refused_steps:7d}  {frame.remainder:9.3f}"
                f"  {'yes' if frame.overflow else 'no'}"
            )
        print(
            f"Final demo position: x = {report.final_state['x']:.3f}, y = {report.final_state['y']:.3f}"
        )
        status = "PASS" if report.oversized_delta_refused else "FAIL"
        print(f"Oversized delta guard: {status} ({report.guard_refusal_code})")
        conflict_status = "PASS" if report.conflicting_writes_refused else "FAIL"
        print(
            f"Conflicting writes guard: {conflict_status} ({report.conflict_refusal_code})"
        )
    passed = (
        report.oversized_delta_refused
        and report.conflicting_writes_refused
        and all(frame.refused_steps == 0 for frame in report.frames)
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
