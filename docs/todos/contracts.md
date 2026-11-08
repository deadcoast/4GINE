# Contract kernel and schema evolution [DOC]

The six ingress schemas are implemented. Future changes need explicit version
and migration policy while preserving structured refusals.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Kernel](../../spinaltap/contract_kernel.py)
- [Ingress](../../spinaltap/contract_validation.py)
- [Kernel tests](../../tests/test_contract_kernel.py)
- [Ingress tests](../../tests/test_contract_validation.py)

## Individual TODOs

### ST-005: Specify contract identity and schema evolution

- Status: ready
- Phase: P2
- Requirements: REQ03, REQ04, REQ05, REQ06, REQ07, REQ08, REQ09
- Depends on: ST-001
- Owner: contracts
- Legacy: Extends TODO.md::TK04
- Scope: Define version identity and compatibility boundaries for DC01 through
  DC06 before adding evidence, authority or typed style fields.
- Acceptance: Document required fields, trusted constructors, shallow snapshot
  limits and migration/refusal rules. Define how claim evidence identifies a
  contract revision. Include old/current/unknown-version examples and a
  decision on schema export; avoid promising deep immutability for
  unconstrained nested values.
- Evidence: pending

### ST-006: Implement version-aware ingress and migration fixtures

- Status: planned
- Phase: P2
- Requirements: REQ03, REQ04, REQ05, REQ06, REQ07, REQ08, REQ09
- Depends on: ST-002, ST-005
- Owner: contracts
- Legacy: Extends TODO.md::TK04
- Scope: Apply the accepted compatibility policy to the bounded prototype and
  preserve field-path refusals.
- Acceptance: Known payloads decode through the declared version path.
  Missing/unknown versions and incompatible fields fail as specified; nullable
  required fields, nonfinite values, booleans-as-numbers and nested errors
  remain covered. Attach migration fixtures and exact test results; document
  compatibility changes.
- Evidence: pending

### ST-033: Reconcile the full prototype requirement evidence matrix

- Status: planned
- Phase: P2
- Requirements: REQ01, REQ02, REQ03, REQ04, REQ05, REQ06, REQ07, REQ08, REQ09,
  REQ10, REQ11, REQ12, REQ13, REQ14, REQ15
- Depends on: ST-006, ST-008, ST-009, ST-011, ST-012, ST-014, ST-018, ST-024
- Owner: contracts
- Legacy: Continues TODO.md::TK12 as a behavioral audit
- Scope: Review every prototype requirement after the policy and authority
  slices; style implementation remains explicitly scheduled in P3.
- Acceptance: Link each requirement to source, acceptance/refusal specimens,
  evidence and remaining limits. Run the full runtime suite and integration
  CLI. Record REQ08/REQ14 as not yet satisfied beyond the current string
  schema until ST-021/ST-022 evidence exists. No requirement is marked
  complete solely because a planning document or file exists.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Contract kernel and schema evolution; authoritative individual task status and acceptance live here."

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
