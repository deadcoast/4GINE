"""Observe the current governor; never implement the selected ST-007 policy.

Run from the repository root with the selected Python and --output pointing
at a new evidence file. Do not overwrite a historical review after source edits.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from spinaltap.context_weight import ContextWeightGovernor
from spinaltap.contract_kernel import ContractRef, SourceClaim
from spinaltap.contract_validation import ContractValidationError, parse_contract


def observe(payload):
    try:
        parse_contract(ContractRef.DC01, payload)
        ingress = {"status": "decoded"}
    except ContractValidationError as error:
        ingress = {"status": "refused", "field": error.field,
                   "refusal": asdict(error.refusal)}
    # Deliberately bypass ingress to expose the current trusted-constructor
    # boundary. This is a source observation, not recommended application use.
    try:
        result = ContextWeightGovernor().evaluate(SourceClaim(**payload))
        direct = {"status": "returned", "outcome": {
            "governor_decision": result.governor_decision,
            "influence_weight": result.influence_weight,
            "risk_flag": result.risk_flag,
        }}
    except Exception as error:
        direct = {"status": "exception", "type": type(error).__name__,
                  "message": str(error)}
    return {"legacy_ingress": ingress, "direct_governor": direct}


def json_safe(value):
    if isinstance(value, float) and not math.isfinite(value):
        return {"special_float": str(value)}
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    corpus = json.loads((ROOT / "docs/examples/governor_policy.json").read_text())
    observations = []
    for case in corpus["cases"]:
        scores = [case["payload"][field] for field in corpus["score_order"]]
        observations.append({
            "id": case["id"], "arithmetic_mean": sum(scores) / len(scores),
            "raw_minimum": min(scores),
            "selected_policy_outcome_not_executed": case["selected_policy_outcome"],
            **observe(case["payload"]),
        })
    invalid_observations = []
    for case in corpus["invalid_inputs"]:
        value = case["value"]
        if isinstance(value, dict):
            value = float(value["special_float"])
        payload = {**corpus["invalid_input_base"], case["field"]: value}
        invalid_observations.append({"id": case["id"], **observe(payload)})
    sources = (
        "spinaltap/context_weight.py", "spinaltap/contract_kernel.py",
        "spinaltap/contract_validation.py", "tests/test_context_weight_governor.py",
        "tests/test_contract_validation.py", "docs/examples/governor_policy.json",
        "reports/evidence/st-007/observe_governor.py",
    )
    report = {
        "scope": "ST-007 current-source observations and arithmetic comparison; selected policy is not executed",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "base_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source_hashes": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in sources
        },
        "observations": observations, "invalid_input_observations": invalid_observations,
    }
    args.output.write_text(
        json.dumps(json_safe(report), indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    print(f"Recorded {len(observations)} outcomes and {len(invalid_observations)} invalid inputs")


if __name__ == "__main__":
    main()
