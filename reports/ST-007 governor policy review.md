# ST-007 governor policy review and evidence [DOC]

Date: 2026-11-09. Phase P2; REQ01, REQ04 and REQ10. This review selects the
[governor policy](../docs/decisions/governor_policy.md) and specifies ST-008's
implementation acceptance. The working tree is based on
d7c789bc8090f4290163534317939a752aafaeab with the prior ST-005/ST-006 work
preserved. Runtime, runtime tests, tool scripts and dependency files are
unchanged by ST-007. No new hosted CI run or implemented minimum governor is
claimed.

> Goal: [GL01] - RESOLVE_GOVERNOR_POLICY_WITH_SOURCE_EVIDENCE
> Dependency: [DP01] - FR05_DC01_AND_CURRENT_RUNTIME
> Requirement: [RQ01] - SEPARATE_OBSERVED_BEHAVIOR_FROM_SELECTED_RULES

## Reviewed context and selected rule

Reviewed the actual governor, both dedicated specimens, DC01 ingress and its
governor integration specimen, the ST-005 identity policy, ST-006 compatibility
tests, requirements/design, FR05 and the preserved realignment findings.
The current implementation uses a clamped arithmetic mean after missing-source
and originality gates; DOWN_WEIGHT is defined but never returned. FR05 uses a
minimum without a complete decision partition.

Select the minimum so strong factors cannot offset absent fit, authority or
validation reach. Retain the 0.20 originality floor as an explicitly
uncalibrated project constraint and missing attribution as an earlier block.
After those gates, zero support blocks, positive support below 1 down-weights,
and full support allows. Exact risk strings and evaluation priority are defined
in the decision. There is no new arbitrary allow threshold or compounding
penalty. All scores remain caller-declared rubric values.

The policy also requires complete input revalidation before scoring. Stored
outputs are recomputed, not trusted. DC01 revision 1 remains a structural
record; historical allow/0.75 results still decode and migrate literally.
Fresh evaluation is identified separately as governor-minimum-v1 plus the
implementation source identity. A later provenance field or stricter ingress
acceptance would require its own schema revision decision.

## Executed current-source observations

[source-review.json](evidence/st-007/source-review.json) retains the environment,
source/corpus/observer hashes and 52 input observations: 20 complete valid
claims and 32 invalid-score mutations. Each observation runs the existing
legacy ingress and the current governor. Direct governor calls deliberately
bypass ingress to inspect the trusted-constructor weakness; they are not
recommended application usage.

- All 20 complete outcome examples pass existing DC01 structural ingress.
- (1, 0, 1, 1) currently returns allow with weight 0.75. Its minimum is 0;
  the selected policy requires block with zero_support.
- Exactly 0.20 originality with other scores 1 currently returns allow/0.8;
  the selected policy requires down_weight/0.20. The immediate lower float
  remains blocked by the retained originality gate.
- The immediate predecessor of 1 as claim fit currently rounds to mean 1.0
  and allow. The minimum preserves its value below 1, requiring down_weight.
- Re-evaluating scores (0.9, 0.8, 0.7, 0.6) with earlier allow/0.75 metadata
  currently returns allow/0.75. The selected result is down_weight/0.6.
- All 32 invalid-score inputs are refused by existing ingress at the expected
  score field with DC01/VG01, invalid_payload and blocked promotion.
- Directly constructed malformed claims produce 26 allow results, two block
  results and four TypeError exceptions. This exposes the missing governor
  revalidation step; it does not mean validated external ingress accepts them.

The observer computes raw mean/minimum arithmetic for comparison. It does not
implement or execute the selected policy. Fields named
selected_policy_outcome_not_executed are copied specification expectations.
They must not be cited as successful ST-008 evidence.

Reproduce observations into a new local file after any source change:

```powershell
.\.venv\Scripts\python.exe reports/evidence/st-007/observe_governor.py `
  --output .tools/st007-new-observations.json
```

The checked-in [observer](evidence/st-007/observe_governor.py) uses only the
standard library and current repository modules. Nonfinite fixture values use
explicit JSON descriptors; they are reconstructed only for the Python probe.
Historical observation files are retained, not refreshed in place later.

## Specification and implementation handoff

The [policy corpus](../docs/examples/governor_policy.json) contains 20 complete
outcomes and 32 invalid-score cases for ST-008. It covers all three selected
decisions, divergent factors, ties, zero support, missing attribution,
threshold equality and adjacent floats, prior output overwrite and unresolved
references. Invalid scores cover booleans, numeric strings, null, negative and
above-one values, NaN and both infinities in each of the four fields.

The ST-008 card additionally requires precedence, invalid derived fields,
input preservation and idempotent rescoring. Its source-level policy identifier
must accompany evidence; it does not itself prove execution. Existing DC01
parsing/migration compatibility and both current governor block specimens
remain required. ST-009 retains registry/provenance resolution ownership.

README, requirements, design, contract-identity notes, the global plan and
catalogue link the accepted policy while clearly describing the unchanged
runtime. A dated supersession notice links from the historical research without
replacing its formula, sources or observations.

## Verification and limits

Verify.cmd passed 117 runtime tests, 31 tooling tests, the JSON demonstration,
Pyright with zero errors/warnings, planning/link/citation validation and
Markdown lint across 36 documents, lock/version checks and whitespace.
Planning covers 34 cards, five phases and 15 requirements. These tests verify
the existing source; they do not establish the selected governor behavior.

The [retained verification record](evidence/st-007/verification.json) includes
the exact commands/results, tool versions and unchanged runtime/test/tool
source hashes. The environment is CPython 3.13.18, uv 0.13.7, Node 24.22.2,
npm 11.19.1, Pyright 1.1.414 and markdownlint-cli2 0.23.1 / core 0.41.1.
The full latest verification also lives at .tools/verification/latest.json.
Task closure and the queue pointer receive final documentation checks.

No empirical calibration, originality detection, verified attribution, legal
assessment, engine resource enforcement or application acceptance follows from
this policy. P2 remains open. The next work is
[ST-008](../docs/todos/governance.md#st-008-implement-and-test-the-selected-governor-outcomes),
implementing and testing the selected outcomes against these specifications.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST007_POLICY_REVIEW_EVIDENCE
  "Dated review, selected governor policy and current-source observations."

[GL01]: RESOLVE_GOVERNOR_POLICY_WITH_SOURCE_EVIDENCE
  "Settle aggregation and outcome semantics before changing the governor."

[DP01]: FR05_DC01_AND_CURRENT_RUNTIME
  "Historical minimum, structural contract policy and the actual mean-based source."

[RQ01]: SEPARATE_OBSERVED_BEHAVIOR_FROM_SELECTED_RULES
  "Specification cases and arithmetic are not execution evidence for ST-008."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."
