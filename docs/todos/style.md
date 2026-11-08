# Measurable style profiles [DOC]

DC05 currently validates ten nonblank strings. The fifteen historical style
categories remain research vocabulary; start with one measured profile
selected for an explicit demonstrator.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Style surface](../../spinaltap/style_surface.py)
- [Style tests](../../tests/test_style_constraint_surface.py)
- [Style catalogue](../research_plan.md)

## Individual TODOs

### ST-020: Define one typed and measurable style profile

- Status: planned
- Phase: P3
- Requirements: REQ08, REQ14
- Depends on: ST-025
- Owner: style
- Legacy: TODO.md::TK09
- Scope: Select one profile from the preserved style vocabulary and specify
  its numeric units, ranges, allowed categories and cross-field relationships.
- Acceptance: Give concrete geometry, lighting, texture, color, fog, alpha,
  depth, camera, cadence and artifact rules tied to a fixture. Refuse vague
  labels, unsupported units and impossible combinations in the design.
  Separate an intentional aesthetic from historically accurate hardware
  emulation. Record why chosen budgets fit the demonstrator.
- Evidence: pending

### ST-021: Implement typed profile decoding and budget checks

- Status: planned
- Phase: P3
- Requirements: REQ08, REQ14
- Depends on: ST-006, ST-020, ST-024
- Owner: style
- Legacy: TODO.md::TK09
- Scope: Replace the string-only DC05 specimen through the agreed
  schema/migration path.
- Acceptance: One real profile decodes to explicit values. All-vague strings,
  nonfinite/negative values, unsupported categories, invalid units and
  conflicting limits fail with useful field paths. Fixtures cover every field
  and legal boundaries. Tests establish schema/budget behavior, not rendered
  visual correctness.
- Evidence: pending

### ST-022: Measure profile enforcement in rendered output

- Status: planned
- Phase: P4
- Requirements: REQ08, REQ14, REQ15
- Depends on: ST-021, ST-027
- Owner: style
- Legacy: New rendering evidence
- Scope: Map the selected profile to actual presentation behavior and
  instrument the controlled scene.
- Acceptance: Capture repeatable camera/asset/settings data, output images and
  applicable counts/timings on named hardware. Demonstrate an in-budget scene
  and a deliberate violation. Record subjective visual review separately from
  numeric limits. Unimplemented profile fields cannot be reported as enforced.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Measurable style profiles; authoritative individual task status and acceptance live here."

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
