# Governor aggregation and down-weight policy [DOC]

Decision date: 2026-11-09. ST-007, phase P2; REQ01, REQ04 and REQ10.
Policy identifier: governor-minimum-v1. This is the accepted specification for
[ST-008](../todos/governance.md#st-008-implement-and-test-the-selected-governor-outcomes).
ST-008 now implements this policy; the
[implementation record](../../reports/ST-008%20governor%20implementation.md)
contains executed acceptance evidence. The earlier
[ST-007 observations](../../reports/ST-007%20governor%20policy%20review.md)
preserve the former mean-based behavior and are not rewritten as current results.

> Goal: [GL01] - BOUND_INFLUENCE_BY_EVERY_REQUIRED_FACTOR
> Dependency: [DP01] - HISTORICAL_FORMULATION_AND_REVIEWED_GOVERNOR
> Requirement: [RQ01] - MAKE_ALL_OUTCOMES_EXPLICIT_AND_TESTABLE

## Selection and rationale

For a structurally valid, attributed claim whose originality score is at least
0.20, use the minimum of source_authority, claim_fit, originality_distance
and validation_reach. These four caller-declared scores remain finite numbers
in the inclusive range 0..1. Higher scores permit more influence. They are a
project review rubric, not calibrated probabilities or measured originality.

The weight is the permitted fraction of the project's full influence budget
for this claim. It is bounded by every supplied factor: a strong authority
score cannot compensate for no fit, no reach or a low originality score.
Increasing a factor cannot decrease the minimum; reducing the limiting factor
cannot increase it. No sum normalization, clamping, rounding, averaging with
earlier results or additional multiplier applies to valid inputs.

| Alternative | Example (1, 0, 1, 1) | Decision |
| --- | ---: | --- |
| Arithmetic mean | 0.75 | Reject; strong factors compensate for absent fit |
| Minimum | 0 | Select; every factor limits permitted influence |
| Product | 0 | Reject; compounds scores without a reviewed model |
| Weighted mean | Depends on weights | Reject; ungrounded coefficients |

For balanced factors (0.5, 0.5, 0.5, 0.5), the minimum is 0.5 while the product
is 0.0625. The selected rule expresses a limit, not compounded evidence or
statistical independence. No external source or experiment establishes that
these scores predict novelty, quality, ownership or legal permission.

## Ordered evaluation and exact outcomes

ST-008 retains ContextWeightGovernor.evaluate(claim: SourceClaim) and its
SourceClaim return type for valid inputs. Evaluate the following rules in order:

1. Revalidate the complete claim through the existing DC01 legacy/internal
   validator, including matching dataclass inputs and any prior output fields.
   Invalid fields raise ContractValidationError with DC01/VG01, invalid_payload
   and blocked promotion. They do not produce a scored SourceClaim. Reject
   booleans, strings, nonfinite numbers and out-of-range scores; never coerce or
   clamp them into valid scores. An invalid field takes precedence over a
   business-rule block, even when source attribution is missing.
2. If source_ref is null, empty or whitespace-only, return block with weight
   0.0 and risk_flag hidden_influence. Attribution is required before influence.
3. If originality_distance is strictly less than 0.20, return block with weight
   0.0 and risk_flag low_originality. This takes precedence over zero support
   in another factor. Keep 0.20 as the existing conservative project floor;
   neither its value nor the supplied score is empirically calibrated.
4. Compute w = min(source_authority, claim_fit, originality_distance,
   validation_reach), then apply the table below.

| Condition after prior gates | Decision | Weight | risk_flag |
| --- | --- | --- | --- |
| w == 0 | block | 0.0 | zero_support |
| 0 < w < 1 | down_weight | w | limited_support |
| w == 1 | allow | 1.0 | none |

All three outcomes are retained and reachable. down_weight means a positive
influence allowance below the full budget of 1, not a reduction from a
caller-supplied previous weight. allow means the full budget under this rubric;
it does not grant authority outside the governor. block means no influence.
The none flag means no restriction was triggered by this rubric, not that
all source risks are absent. The single limited_support flag avoids inventing
a ranking or attribution of blame when several factors tie for the minimum.

The originality floor is inclusive on the permitted side: exactly 0.20 can
receive down_weight if every other factor is positive. It is not a threshold
on authority, fit or reach. A positive fit of 0.05 therefore permits at most
0.05 when the originality gate passes. There is no additional allow cutoff
at 0.5, 0.8 or a configurable threshold; all scores must be 1 for allow.

Comparisons use the validated Python float values directly, without epsilon
or display rounding. The predecessor of 0.20 blocks, 0.20 and its successor
can down-weight, and the predecessor of 1 remains down-weighted. The smallest
positive representable fit remains positive influence; signed zero has zero
support. This is a scalar reference policy, not cross-platform replay evidence.

Recompute influence_weight, risk_flag and governor_decision from the validated
source fields on every call. Preserve the source reference, claim text and
scores; do not mutate the input. Existing structurally valid output fields are
overwritten, not trusted or multiplied into the result. Invalid existing output
fields still fail whole-record validation. Identical validated inputs produce
the same result; evaluating that result again must not compound down-weighting.

The typed API remains a domain operation. External versioned data first uses
parse_contract_envelope(ContractRef.DC01, envelope), then passes its record to
the governor while retaining identity separately. No automatic source lookup,
resource allocation or downstream engine mutation is added by this policy.

## Examples and acceptance handoff

Factor order below is authority, fit, originality, reach. Except where shown,
the reference is a nonblank string and every other field is structurally valid.

| Factors / condition | Pre-ST-008 outcome | Selected policy outcome |
| --- | --- | --- |
| (1, 0, 1, 1) | allow, 0.75, none | block, 0, zero_support |
| (1, 1, 1, 1) | allow, 1, none | allow, 1, none |
| (0.5, 0.5, 0.5, 0.5) | allow, 0.5, none | down_weight, 0.5, limited_support |
| (1, 1, 0.20, 1) | allow, 0.8, none | down_weight, 0.20, limited_support |
| (1, 1, 0.19, 1) | block, 0, low_originality | block, 0, low_originality |
| (0, 1, 0.1, 1) | block, 0, low_originality | block, 0, low_originality |
| Missing ref | block, 0, hidden_influence | block, 0, hidden_influence |
| (0.9,0.8,0.7,0.6) | allow, 0.75, none | down_weight, 0.6, limited_support |

The machine-readable [policy examples](../examples/governor_policy.json)
specify 20 complete outcome cases and 32 invalid-score mutations. Boundary
neighbors use math.nextafter values rather than rounded approximations.
The special_float objects in invalid fixtures encode nonfinite Python test
values; they are fixture instructions, not a new DC01 wire format.

ST-008 must execute these target outcomes, test all four score fields,
attribution and threshold precedence, ties/zero/full support and repeated
evaluation without input mutation. Add malformed trusted dataclass tests,
including invalid derived fields and invalid data combined with missing
attribution. Preserve the two existing missing-source/low-originality tests;
any changed expectations need the semantic explanation in this decision.
All runtime, demo and accepted checks remain required for implementation.

## Compatibility, provenance and historical supersession

The 2026-05-26 [FR05 formulation](../live_research.md#55-context-weight-governor-fr05)
selected a minimum but did not define the complete outcome partition, input
validation, equality behavior or risk strings. This decision retains that
formula and supersedes its incomplete operational policy with the ordered
rules above. It also explicitly supersedes the former runtime's unrecorded
mean/allow-only scoring policy through the ST-008 implementation. Preserve
the historical formula, code observations and old test evidence as dated facts.

DC01 revision 1 remains a structural record, not a certificate that a particular
governor policy ran. Its accepted field types, ranges, nullable fields, decision
vocabulary and parsing/migration behavior do not change. In particular, a
historical record with allow and weight 0.75 must still decode and migrate
literally; it must not be relabeled as a governor-minimum-v1 result.
The [identity decision](contract_identity.md) deliberately left aggregation to
the governor's separate domain policy. The new outcome conditions govern fresh
evaluation, not reinterpretation of every previously stored decision value.

Consequently ST-008 does not add a transport revision or change DC01 decoders,
legacy fixtures or automatic migration. It introduces the named policy in
the governor, with a source-level GOVERNOR_POLICY_ID constant set to
governor-minimum-v1 for evidence callers. Evidence must name that policy ID,
the exact implementation revision/hash and input identity separately. The
constant is attribution, not proof of execution; DC01 alone cannot identify
which policy produced an output. Adding policy provenance fields or requiring
output consistency at ingress would change the contract and requires a new
reviewed schema revision under the existing evolution rules.

A nonblank source_ref remains caller attribution, even if it names an unknown
reference. ST-009 owns source-registry resolution and inspectable review basis.
Allowing a fully scored claim with an unresolved reference does not verify its
provenance. No automatic originality measurement, plagiarism detection,
empirical calibration or legal conclusion is part of this policy. Future
changes to score interpretation, formula, thresholds or flag/decision rules
need a new policy decision and identity; contract changes additionally follow
the schema evolution rule.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST007_GOVERNOR_POLICY
  "Selected minimum aggregation, ordered gates and explicit outcome semantics."

[GL01]: BOUND_INFLUENCE_BY_EVERY_REQUIRED_FACTOR
  "Prevent one strong caller-declared score from compensating for a weak factor."

[DP01]: HISTORICAL_FORMULATION_AND_REVIEWED_GOVERNOR
  "FR05, the current mean-based implementation, DC01 revision 1 and source observations."

[RQ01]: MAKE_ALL_OUTCOMES_EXPLICIT_AND_TESTABLE
  "Define reachable decisions, exact boundaries and a bounded ST-008 handoff."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."
