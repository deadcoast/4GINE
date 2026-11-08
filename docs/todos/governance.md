# Source influence and provenance [DOC]

The current governor uses a clamped mean while historical FR05 specifies a
minimum. This work resolves policy explicitly; neither formula is a calibrated
originality detector.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Governor](../../spinaltap/context_weight.py)
- [Governor tests](../../tests/test_context_weight_governor.py)
- [Historical formulation](../live_research.md)

## Individual TODOs

### ST-007: Resolve governor aggregation and down-weight policy

- Status: ready
- Phase: P2
- Requirements: REQ01, REQ04, REQ10
- Depends on: none
- Owner: governance
- Legacy: TODO.md::TK05
- Scope: Compare historical FR05 minimum with the runtime mean, the 0.20
  originality boundary and the unreachable DOWN_WEIGHT enum.
- Acceptance: Record the selected rule and rationale using divergent examples
  including factors (1,0,1,1), boundary values and missing attribution. Decide
  retained outcomes and their meaning. Update requirement/design policy with
  an explicit historical supersession note. Clearly label scores as a project
  rubric unless empirical calibration evidence exists.
- Evidence: pending

### ST-008: Implement and test the selected governor outcomes

- Status: planned
- Phase: P2
- Requirements: REQ04, REQ10
- Depends on: ST-002, ST-007
- Owner: governance
- Legacy: TODO.md::TK05
- Scope: Align code, tests and current design with the accepted policy without
  rewriting historical source findings.
- Acceptance: Every retained allow/down-weight/block outcome is reachable.
  Tests cover the chosen aggregation examples, threshold equality and
  neighbors, invalid scores and missing sources. Refusals and risk text match
  the decision. Existing tests are revised only with documented semantic
  reasons.
- Evidence: pending

### ST-009: Resolve source references through a provenance record

- Status: planned
- Phase: P2
- Requirements: REQ01, REQ04, REQ10
- Depends on: ST-005, ST-008
- Owner: governance
- Legacy: Extends TODO.md::TK05
- Scope: Define a bounded source registry and claim linkage containing source
  identity, access/version, purpose, influence limit and review basis.
- Acceptance: Known references resolve to inspectable records; unknown, stale
  or conflicting references cannot silently claim verified provenance.
  Preserve historical source versions and distinguish availability from
  support. Show one positive and one refused claim, and record that registry
  resolution does not prove novelty or ownership.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Source influence and provenance; authoritative individual task status and acceptance live here."

[GL01]: DELIVER_BOUNDED_TRACEABLE_SLICES
  "Advance the owning global phase through individually scoped and verified
  development work."

[DP01]: GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
  "Global phase intent comes from global_plan.md; requirements and design own
  technical meaning; task dependencies name globally unique ST identifiers."

[RQ01]: ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION
  "Each task retains its phase, requirements, dependencies, acceptance and
  evidence. Planned or structural evidence cannot imply runtime completion."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative index invoking each active local context marker."
