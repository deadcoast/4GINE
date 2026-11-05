"""Run the bounded SPINALTAP prototype: python -m spinaltap [--json]."""

import argparse
from dataclasses import asdict
import json

from spinaltap.demo import run_demo


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the SPINALTAP fixed-step prototype."
    )
    parser.add_argument(
        "--json", action="store_true", help="print the structured demonstration report"
    )
    args = parser.parse_args()
    report = run_demo()
    if args.json:
        print(json.dumps(asdict(report), indent=2, allow_nan=False))
    else:
        print("SPINALTAP fixed-step prototype")
        print("Frame  Elapsed   Steps  Accepted  Refused  Remainder  Overflow")
        for frame in report.frames:
            print(
                f"{frame.index + 1:5d}  {frame.elapsed_time:7.3f}  {frame.fixed_steps:5d}"
                f"  {frame.accepted_steps:8d}  {frame.refused_steps:7d}  {frame.remainder:9.3f}"
                f"  {'yes' if frame.overflow else 'no'}"
            )
        print(f"Final demo position: x = {report.final_position:.3f}")
        status = "PASS" if report.oversized_delta_refused else "FAIL"
        print(f"Oversized delta guard: {status} ({report.guard_refusal_code})")
    return 0 if report.oversized_delta_refused else 1


if __name__ == "__main__":
    raise SystemExit(main())
