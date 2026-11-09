# ST-008 governor implementation and evidence [DOC]

Date: 2026-11-09. Phase P2; REQ04 and REQ10. This implements the accepted
[governor-minimum-v1 policy](../docs/decisions/governor_policy.md) in the local
working tree based on d7c789bc8090f4290163534317939a752aafaeab. Prior
ST-005/ST-006/ST-007 work and historical observations are preserved. No new
commit, push or hosted CI result is claimed for this implementation.

> Goal: [GL01] - EXECUTE_THE_ACCEPTED_GOVERNOR_POLICY
> Dependency: [DP01] - ST007_POLICY_CORPUS_AND_DC01_INGRESS
> Requirement: [RQ01] - VALIDATE_BEFORE_SCORING_AND_PRESERVE_COMPATIBILITY

## Behavior and compatibility

[context_weight.py](../spinaltap/context_weight.py) now exports
GOVERNOR_POLICY_ID = governor-minimum-v1 and revalidates the entire SourceClaim
through the existing DC01 parser before evaluating any business rule. Invalid
scores, source/claim text or derived fields raise structured DC01/VG01
invalid_payload refusals with blocked promotion and precise field paths.
Malformed direct dataclass calls no longer bypass input validation.

For valid inputs, missing attribution blocks with hidden_influence, then
originality below 0.20 blocks with low_originality. Otherwise the minimum of
all four scores controls influence: zero blocks with zero_support, positive
values below 1 down-weight with limited_support, and 1 allows with none.
There is no mean, clamping, epsilon comparison or compounding of past weights.
Signed zero produces positive zero influence. Existing output fields are
validated and recomputed; source fields and the input record are preserved.

The semantic changes from the earlier runtime are explicit: (1, 0, 1, 1)
now blocks at 0 instead of allowing 0.75, and exactly 0.20 originality with
other factors 1 now down-weights to 0.20 instead of allowing 0.8. All three
decisions are reachable. The two existing missing-source and low-originality
test methods keep their original bodies and expectations.

DC01 revision 1 remains structurally unchanged. Its decoder, envelope registry,
migration implementation, fixtures and accepted fields are preserved. A legacy
allow/0.75 record still decodes and migrates literally. Only explicit governor
evaluation recalculates it as down_weight/0.6 for scores (0.9, 0.8, 0.7, 0.6).
The original decoded/migrated record remains unchanged. Policy and source
identity are recorded separately from input contract identity.

## Executed specimens

[Governor tests](../tests/test_context_weight_governor.py) now contain 15
methods: two preserved specimens and 13 additions. They execute the unchanged
[ST-007 corpus](../docs/examples/governor_policy.json): all 20 complete
outcome cases and all 32 malformed-score cases match their specified results.
Invalid scores are supplied through trusted constructors deliberately, so the
governor itself must perform revalidation.

Additional cases cover invalid text/derived fields, invalid-data priority over
attribution and originality blocks, every factor limiting influence over a
256-combination grid, unchanged inputs, idempotent rescoring and replacement of
earlier decisions/weights. Exact neighboring floats around 0.20 and 1, the
smallest positive fit, signed zero, ties and zero support retain the specified
boundaries. Versioned-ingress and legacy-migration specimens verify that
decoding alone does not execute this policy.

The earlier [ST-007 source review](ST-007%20governor%20policy%20review.md)
remains historical evidence of the old mean-based governor, including its
invalid-direct-call behavior. Neither that record nor its observer output is
rewritten as a successful run of the new policy.

## Verification and source identity

Commands run from the repository root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests `
  -p test_context_weight_governor.py -v
.\Verify.cmd
```

The dedicated suite passes all 15 methods. Verify.cmd passes 130 runtime
methods (117 existing plus 13 new), 31 tooling methods, the JSON demo,
Pyright with zero errors/warnings, planning/link/citation validation and
Markdown lint across 37 documents, lock/version checks and whitespace.
Planning covers 34 cards, five phases and 15 requirements. The demonstration
retains 14 accepted and zero refused scheduled updates, both refusal guards,
final x = 0.672, y = -0.336 and about 0.008 seconds remainder.

The environment remains CPython 3.13.18, uv 0.13.7, Node 24.22.2, npm 11.19.1,
Pyright 1.1.414 and markdownlint-cli2 0.23.1 / core 0.41.1. Runtime dependencies
stay empty. The [retained verification record](evidence/st-008/verification.json)
contains exact commands/results, environment, policy/input identity and source
hashes. The only changed runtime/test files in this task are the governor and
its dedicated test module. The preservation audit covers the existing contract
code, fixtures, other tests, tool scripts, dependency inputs and older evidence.

The full latest checkout verification is also available at
.tools/verification/latest.json. Task closure and the queue update receive
final documentation checks after the implementation checks pass.

## Limits and next work

Scores and the 0.20 originality floor remain uncalibrated project rules. A
nonblank source reference does not prove provenance; a policy constant or
stored output does not prove execution. This is local contract/governor and
scalar integration evidence, not rendered-engine or human acceptance.

P2 remains open. The next card is
[ST-009](../docs/todos/governance.md#st-009-resolve-source-references-through-a-provenance-record),
which owns a bounded source registry and inspectable claim linkage. Its work
must preserve historical source versions and distinguish reference resolution
from evidence that a source supports a claim. Proof-state semantics, timing,
authority, typed styles and the later application retain their own gates.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST008_GOVERNOR_IMPLEMENTATION_EVIDENCE
  "Local implementation, executed policy corpus and compatibility verification."

[GL01]: EXECUTE_THE_ACCEPTED_GOVERNOR_POLICY
  "Make minimum aggregation and all retained outcomes executable and reviewable."

[DP01]: ST007_POLICY_CORPUS_AND_DC01_INGRESS
  "The accepted policy and its examples plus the existing structural validator."

[RQ01]: VALIDATE_BEFORE_SCORING_AND_PRESERVE_COMPATIBILITY
  "Reject malformed complete records while leaving decoding and migration literal."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."
