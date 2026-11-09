# (A) 4GINE SOURCE TODO: RUNNABLE CONTRACT PROTOTYPE [DOC]

Current work is governed by the [global plan](docs/global_plan.md) and
[canonical workstream cards](docs/README.md). This file is the next-task
pointer plus the preserved source/diagnostic history. The historical checkboxes
below are snapshots, not a second mutable backlog.

## (0) Current development queue

> Goal: [GL04] - PRESERVE_FORWARD_WORK_FOR_NEXT_AGENT
> Dependency: [DP04] - CURRENT_SLICE_LIMITS
> Requirement: [RQ04] - KEEP_PENDING_INTEGRATION_VISIBLE

Next task: ST-008

Start with
[ST-008: Implement and test the selected governor outcomes](docs/todos/governance.md#st-008-implement-and-test-the-selected-governor-outcomes).
Its card owns status, scope, dependencies, acceptance and evidence.
Follow the [development workflow](docs/development_workflow.md), updating this
pointer when the selected task finishes.

| Workstream | Current task authority |
| --- | --- |
| Tooling and alignment | [Tooling TODO](docs/todos/tooling.md) |
| Contracts and schemas | [Contract TODO](docs/todos/contracts.md) |
| Source influence | [Governance TODO](docs/todos/governance.md) |
| Time and replay | [Time TODO](docs/todos/time.md) |
| Local workers | [Worker TODO](docs/todos/workers.md) |
| Signals and reconciliation | [Signal TODO](docs/todos/signals.md) |
| Measurable style | [Style TODO](docs/todos/style.md) |
| Proof and evidence | [Proof TODO](docs/todos/proof.md) |
| Interactive application | [Application TODO](docs/todos/application.md) |

### Legacy task migration

The qualified identifiers below refer only to this root TODO's old TK records.
Same-numbered TK entries in docs/tasklist.md are separate completed docspec
tasks. Completed slices keep their original evidence; their successors are new
work, not a retroactive change to the old checked state.

| Historical source task | Canonical continuation |
| --- | --- |
| TODO.md::TK01 | [ST-001/ST-002](docs/todos/tooling.md): tooling decision and bootstrap |
| TODO.md::TK02 | [ST-001/ST-002](docs/todos/tooling.md): select required type gates and configure them |
| TODO.md::TK03 | [ST-004](docs/todos/tooling.md): optional IDE snapshot refresh/retirement |
| TODO.md::TK04 | Preserve ingress slice; [ST-005/ST-006](docs/todos/contracts.md) handle evolution |
| TODO.md::TK05 | [ST-007/ST-008/ST-009](docs/todos/governance.md): policy, outcomes and provenance |
| TODO.md::TK06 | Preserve fixed-step slice; [ST-010/ST-011/ST-012](docs/todos/time.md) extend evidence |
| TODO.md::TK07 | Preserve scalar constraints; [ST-013-ST-016](docs/todos/workers.md) extend scoped workers |
| TODO.md::TK08 | Preserve hooks; [ST-017/ST-018](docs/todos/signals.md) extend authority/adoption |
| TODO.md::TK09 | [ST-020/ST-021/ST-022](docs/todos/style.md): numeric schema and rendered evidence |
| TODO.md::TK10 | [ST-023/ST-024](docs/todos/proof.md): proof semantics and evidence ledger |
| TODO.md::TK11 | Preserve scalar candidate atomicity; [ST-017/ST-018](docs/todos/signals.md) extend it |
| TODO.md::TK12 | Preserve recorded alignment pass; [ST-034](docs/todos/tooling.md) and ongoing workflow |

### Historical snapshot boundary

Sections (1)-(6), their context definitions and recorded checkboxes below
preserve the earlier source continuation and IDE intake. Their original
remaining-work language does not make every listed extension a current release
requirement. In particular, durable commits, additive merges, concurrency and
hook isolation now require a scoped use case under ST-019.

The old MO06 measurable-limit status label describes text-field validation;
numeric style enforcement is still pending. The current proof specimen checks
planning text and does not validate an executed artifact. See the
[current README](README.md) and [dated review](reports/4GINE%20development%20realignment.md)
for the corrected current interpretation. Older tool paths/results remain
historical; fresh evidence is recorded separately.

Historical introduction follows:

This TODO is the agent-facing status ledger for the current SPINALTAP source
slice. It preserves the `linter_error_output.json` intake [IN01], [LS] and
records the 2026-11-05 mapping validation, fixed-step runtime, and multi-worker
reconciliation continuation [TK04], [TK06], [TK07], [TK08], [TK11]. It tracks
diagnostic disposition, module status, verification evidence, and remaining
source work without treating the prototype as an engine-ready system [RQ03],
[ST].

## (1) Intake ledger [IN]

> Goal: [GL01] - TRIAGE_IDE_PROBLEMS_SNAPSHOT
> Dependency: [DP01] - LINTER_EXPORT_IS_INPUT_EVIDENCE
> Requirement: [RQ01] - CLASSIFY_BEFORE_EDITING

- [x] [IN01] Input snapshot: `linter_error_output.json`.
- [x] [IN02] Snapshot total: `37` IDE diagnostics.
- [x] [IN03] Source split: `Mypy=8`, `Pylance=29`.
- [x] [IN04] Root pattern: broad `object` contract fields prevented static
  analyzers from seeing numeric fields, tuple fields, optional refusals, and
  style/proof record shapes.
- [x] [IN05] Missing project-module result: no missing `spinaltap.*` imports
  were present in the snapshot.
- [ ] [IN06] Refresh need: rerun VS Code Problems after this pass; the JSON
  file remains the original snapshot until the IDE exports a new one.

## (2) Source status ledger [MS]

> Goal: [GL02] - RECORD_MODULE_STATUS_WITHOUT_ENGINE_READY_CLAIMS
> Dependency: [DP02] - SOURCECODE_PLAN_MODULE_ORDER
> Requirement: [RQ02] - DISTINGUISH_SLICE_STATUS_FROM_REMAINING_WORK

- [MO01] `spinaltap/contract_kernel.py`
  - Status: `RUNTIME_MAPPING_INGRESS_VALIDATED`.
  - Applied: typed `SourceClaim`, `TimePacket`, `SignalBundle`,
    `DeltaPacket`, `StyleLimits`, and `ProofRecord` fields; companion
    `spinaltap/contract_validation.py` validates all six payload schemas and
    nested records with structured field-path refusals.
  - Still required: module-specific value schemas, schema export, package
    metadata, and cross-module contract versioning. Direct record constructors
    remain trusted internal APIs.
- [MO02] `spinaltap/context_weight.py`
  - Status: `LINTER_ROOT_FIX_APPLIED_THROUGH_CONTRACT_TYPES`.
  - Applied: numeric source-influence fields are statically visible; mapping
    ingress enforces finite scores in `0..1`, and blank source attribution
    remains blocked by the governor.
  - Still required: calibrated down-weight branch, source registry linkage,
    originality scoring policy, and claim provenance ledger.
- [MO03] `spinaltap/time_packet.py`
  - Status: `FIXED_STEP_SOLVER_BOUNDARY_IMPLEMENTED`.
  - Applied: finite inputs, bounded packet budgets, overflow backlog, decimal
    boundary correction, and `solver_steps` expansion. Workers refuse raw time
    and unexpanded frame records. Accumulator stress and demo integration pass.
  - Still required: packet provenance, checkpoint policy, and scheduler-level
    timing qualification.
- [MO04] `spinaltap/vertebra_delta.py`
  - Status: `SCALAR_DELTA_CONSTRAINTS_IMPLEMENTED`.
  - Applied: full local-slice ownership and per-component `max_delta` checks;
    one invalid component refuses the whole proposal. Invalid constraint
    schemas and nonfinite or nonnumeric deltas are refused.
  - Still required: vector and per-key budget schemas, persistent worker
    registry, and conflict policies beyond refusing shared writes.
- [MO05] `spinaltap/signal_spine.py`
  - Status: `VALIDATION_HOOK_EXECUTION_IMPLEMENTED`.
  - Applied: mandatory shape, time, ownership, and envelope checks precede
    named synchronous hooks. Unknown hooks, exceptions, invalid returns, and
    worker refusals stop bundle acceptance.
  - Still required: channel registry, general state publication policy, hook
    isolation, and conflict policies beyond the scalar step boundary.
- [MO06] `spinaltap/style_surface.py`
  - Status: `MEASURABLE_LIMIT_SPECIMEN_PRESENT`.
  - Applied: untrusted style profiles pass through mapping validation; unknown
    fields and non-text values are refused, while missing or blank limits
    retain the vague-style refusal.
  - Still required: numeric/range schema, renderer-facing translation, style
    preset ledger, and artifact budget validation.
- [MO07] `spinaltap/soft_proof.py`
  - Status: `PROOF_RECORD_SPECIMEN_PRESENT`.
  - Applied: proof mappings validate field types and enums; whitespace-only
    plans or failure paths remain blocked. A gate belonging to another
    reviewed contract cannot advance the claim.
  - Still required: evidence-tier policy, proof review ledger, source
    attachment model, and promotion audit output.
- [MO08] `spinaltap/reconciliation.py`
  - Status: `ATOMIC_MULTI_WORKER_SCALAR_STEPS_PRESENT`.
  - Applied: `WorkerUpdate` records run in declared order against one shared
    snapshot. Repeated write keys are refused. `StepResult` exposes a candidate
    only if every worker and hook accepts; failures expose no partial bundles.
    The CLI demo now adopts complete two-worker state updates.
  - Still required: persistent worker/channel authority, global cross-worker
    constraints, additive merges, concurrent publication, durable commits, and
    full engine-loop boundary tests.

## (3) Linter disposition ledger [LD]

> Goal: [GL03] - MAP_EACH_DIAGNOSTIC_BUCKET_TO_ACTION
> Dependency: [DP03] - DIAGNOSTIC_BUCKETS_FROM_JSON
> Requirement: [RQ03] - NO_FALSE_ENGINE_READY_STATUS

- [x] [LD01] `context_weight.py`: `10` diagnostics.
  - Codes: `Mypy arg-type`, `Pylance reportArgumentType`.
  - Disposition: `APPLIED_ROOT_TYPE_FIX`.
  - Fix surface: `SourceClaim` numeric fields.
- [x] [LD02] `time_packet.py`: `5` diagnostics.
  - Codes: `Mypy arg-type`, `Mypy call-overload`, `Mypy no-code`,
    `Pylance reportArgumentType`.
  - Disposition: `APPLIED_ROOT_TYPE_FIX`.
  - Fix surface: `TimePacket.fixed_packet_size` and `TimePacket.packet_count`.
- [x] [LD03] `tests/test_contract_kernel.py`: `1` diagnostic.
  - Code: `Pylance reportOptionalMemberAccess`.
  - Disposition: `TEST_NARROWING_APPLIED`.
  - Fix surface: local `refusal` variable plus Python assertion.
- [x] [LD04] `tests/test_signal_constraint_spine.py`: `4` diagnostics.
  - Code: `Pylance reportAttributeAccessIssue`.
  - Disposition: `TEST_NARROWING_APPLIED`.
  - Fix surface: local `risk` variable plus `RefusalState` assertion.
- [x] [LD05] `tests/test_soft_proof_lab.py`: `2` diagnostics.
  - Code: `Pylance reportOptionalMemberAccess`.
  - Disposition: `TEST_NARROWING_APPLIED`.
  - Fix surface: local `refusal` variable plus `RefusalState` assertion.
- [x] [LD06] `tests/test_spinal_reconciliation.py`: `4` diagnostics.
  - Codes: `Pylance reportArgumentType`, `reportIndexIssue`,
    `reportAttributeAccessIssue`.
  - Disposition: `APPLIED_CONTRACT_TYPE_FIX_AND_TEST_NARROWING`.
  - Fix surface: `SignalBundle.ordered_signal_bundle` tuple typing and local
    residual-risk narrowing.
- [x] [LD07] `tests/test_style_constraint_surface.py`: `5` diagnostics.
  - Code: `Pylance reportOptionalMemberAccess`.
  - Disposition: `TEST_NARROWING_APPLIED`.
  - Fix surface: local `limits` and `refusal` variables plus assertions.
- [x] [LD08] `tests/test_time_packet_pump.py`: `4` diagnostics.
  - Codes: `Pylance reportCallIssue`, `reportArgumentType`.
  - Disposition: `APPLIED_CONTRACT_TYPE_FIX`.
  - Fix surface: `TimePacket` float fields.
- [x] [LD09] `tests/test_vertebra_delta_worker.py`: `2` diagnostics.
  - Code: `Pylance reportAttributeAccessIssue`.
  - Disposition: `TEST_NARROWING_APPLIED`.
  - Fix surface: local `risk` variable plus `RefusalState` assertion.

## (4) Required next tasks [TK]

> Goal: [GL04] - PRESERVE_FORWARD_WORK_FOR_NEXT_AGENT
> Dependency: [DP04] - CURRENT_SLICE_LIMITS
> Requirement: [RQ04] - KEEP_PENDING_INTEGRATION_VISIBLE

- [ ] [TK01] Add repo tooling manifest only after deciding whether this stays
  stdlib-only or adopts project-managed type tooling.
- [ ] [TK02] If mypy is required as a local gate, add the dependency and config
  through the chosen manifest instead of relying on global Python.
- [ ] [TK03] Re-export VS Code Problems after the IDE refreshes; compare new
  diagnostics against [LD01] through [LD09].
- [x] [TK04] Add runtime validation for untrusted mappings entering all six
  contract records. `parse_contract` validates complete payloads and nested
  records; style and specimen mapping inputs use it. Trace: requirements
  `REQ04` through `REQ09`, contracts `DC01` through `DC06`, and
  [design ingress rules](docs/design.md#41-runtime-mapping-ingress-dc).
- [ ] [TK05] Define the `DOWN_WEIGHT` governor path or remove the enum branch
  if the next design pass rejects it.
- [x] [TK06] Add fixed-step `TimePacket` worker entry with raw-dt refusals,
  checked frame expansion, and accumulator stress tests. Trace: `REQ05`,
  `REQ11`, `DC02`, `VG02`; design section 4.2.
- [x] [TK07] Enforce scalar per-component delta limits and reject the entire
  proposal on any violation. Trace: `REQ07`, `REQ13`, `DC04`, `VG04`; design
  section 4.3.
- [x] [TK08] Execute named signal validation hooks after mandatory checks and
  before bundle acceptance. Trace: `REQ06`, `REQ12`, `DC03`, `VG03`; design
  section 4.4. General state publication remains pending.
- [ ] [TK09] Convert style limits from strings into validated range/budget
  records after the style schema is specified.
- [ ] [TK10] Add proof ledger persistence or structured in-memory records after
  evidence-tier rules are specified.
- [x] [TK11] Expand reconciliation to ordered multi-worker steps, shared input
  snapshots, explicit write-conflict refusal, and all-or-nothing scalar state
  candidates. Trace: `REQ06`, `REQ07`, `REQ12`, `REQ13`, `DC03`, `DC04`,
  `VG03`, `VG04`; design section 4.5.
- [x] [TK12] Run docspec alignment checks for this source slice; preserve the
  requirement to rerun them on each later source or TODO change.

## (5) Verification ledger [VF]

> Goal: [GL05] - RECORD_FRESH_VERIFICATION_EVIDENCE
> Dependency: [DP05] - LOCAL_COMMAND_OUTPUT
> Requirement: [RQ05] - STATUS_REQUIRES_COMMAND_EVIDENCE

- [x] [VF01] `py -3.13 -m unittest discover -s tests`
  - Result: `87` tests ran, `OK`; this continuation began with `68` tests.
- [x] [VF02] Pyright CLI, `spinaltap tests`
  - Result: `0 errors`, `0 warnings`, `0 informations`. Invoked the existing
    cached Node CLI directly because `npx` package retrieval was unavailable.
- [ ] [VF03] `py -3.13 -m mypy spinaltap tests`
  - Result: blocked by environment; Python 3.13 reports `No module named
    mypy`.
- [ ] [VF04] `.venv\Scripts\python.exe -m mypy spinaltap tests`
  - Result: not run; this checkout has no repo-local virtualenv interpreter.
    Tooling setup remains tracked by [TK01] and [TK02].
- [x] [VF05] Markdownlint CLI for `TODO.md`, requirements, design, tasklist,
  and sourcecode plan, using the existing cached Node CLI.
  - Result: `5` Markdown files linted, `0` issues; lint configuration unchanged.
- [x] [VF06] Pseudo-citation audit for the same five documents
  - Result: `383` definitions and `383` unique references summed across files;
    `0` missing, unused, duplicate, misplaced, or zero-placeholder markers.
    The root TODO contains `75` definitions and `75` unique references.
- [x] [VF07] `py -3.13 -m spinaltap` and JSON subprocess smoke test
  - Result: `14` accepted two-worker steps, final `x = 0.672`, `y = -0.336`,
    remainder `0.008`, and oversized-delta plus write-conflict guard refusals.
    The CLI exited successfully.

## (6) Notes for the next source agent [NT]

> Goal: [GL06] - HAND_OFF_WITH_BOUNDARIES
> Dependency: [DP06] - PARTIAL_SOURCE_SLICE
> Requirement: [RQ06] - DOCUMENT_STATUS_AND_REMAINING_WORK

- [NT01] Treat `linter_error_output.json` as an input snapshot, not live IDE
  state after edits.
- [NT02] No source modules were created for missing imports because the export
  contained no missing-import diagnostics.
- [NT03] `.mypy_cache/` is ignored because local type-checker state is
  generated output.
- [NT04] Current source includes a runnable scalar demo and synchronous
  multi-worker reconciliation; broader engine systems remain pending work. Run
  `py -3.13 -m spinaltap` from the repository root.

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes active markers so the registry
below remains link-complete [LC], [LN].

- Document and sections: [DOC], [IN], [LS], [MS], [LD], [TK], [VF], [NT],
  [ST], [LC], [LN]
- Intake markers: [IN01], [IN02], [IN03], [IN04], [IN05], [IN06]
- Module markers: [MO01], [MO02], [MO03], [MO04], [MO05], [MO06], [MO07],
  [MO08]
- Linter markers: [LD01], [LD02], [LD03], [LD04], [LD05], [LD06], [LD07],
  [LD08], [LD09]
- Task markers: [TK01], [TK02], [TK03], [TK04], [TK05], [TK06], [TK07],
  [TK08], [TK09], [TK10], [TK11], [TK12]
- Verification markers: [VF01], [VF02], [VF03], [VF04], [VF05], [VF06], [VF07]
- Note markers: [NT01], [NT02], [NT03], [NT04]
- Metadata markers: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [DP01],
  [DP02], [DP03], [DP04], [DP05], [DP06], [RQ01], [RQ02], [RQ03], [RQ04],
  [RQ05], [RQ06]

## (Z) Context-Citations

[DOC]: SOURCE_TODO_LEDGER
  "The root TODO ledger for linter triage, module status, and remaining source
  work."

[IN]: INTAKE_LEDGER
  "The section that records the IDE Problems snapshot and diagnostic shape."

[LS]: LINTER_SNAPSHOT
  "The exported VS Code Problems JSON used as input evidence for this pass."

[MS]: MODULE_STATUS_LEDGER
  "The section that records current source-slice status per module."

[LD]: LINTER_DISPOSITION_LEDGER
  "The section mapping diagnostic buckets to applied or remaining action."

[TK]: TASK_LEDGER
  "The section preserving remaining source and tooling tasks for the next
  agent."

[VF]: VERIFICATION_LEDGER
  "The section recording fresh command evidence and blocked verification
  checks."

[NT]: NEXT_AGENT_NOTES
  "The section recording handoff boundaries and non-obvious status notes."

[ST]: STATUS_BOUNDARY
  "A marker that separates current specimen status from broader engine
  readiness."

[LC]: LINK_COMPLETE_STATE
  "A pseudo-citation document state where active markers are defined once and
  referenced."

[LN]: LINT_RULE
  "The rule that live marker definitions belong in the bottom registry."

[GL01]: TRIAGE_IDE_PROBLEMS_SNAPSHOT
  "Classify the IDE Problems export before editing source."

[GL02]: RECORD_MODULE_STATUS_WITHOUT_ENGINE_READY_CLAIMS
  "Record module status while avoiding broader engine readiness language."

[GL03]: MAP_EACH_DIAGNOSTIC_BUCKET_TO_ACTION
  "Map every linter diagnostic bucket to an applied fix or remaining status."

[GL04]: PRESERVE_FORWARD_WORK_FOR_NEXT_AGENT
  "Keep required next work visible for subsequent implementation passes."

[GL05]: RECORD_FRESH_VERIFICATION_EVIDENCE
  "Record current command evidence for tests, type checks, and document checks."

[GL06]: HAND_OFF_WITH_BOUNDARIES
  "Hand off source status with explicit scope and remaining work boundaries."

[DP01]: LINTER_EXPORT_IS_INPUT_EVIDENCE
  "The pass depends on the exported VS Code Problems JSON as input evidence."

[DP02]: SOURCECODE_PLAN_MODULE_ORDER
  "Module status depends on the existing sourcecode plan order."

[DP03]: DIAGNOSTIC_BUCKETS_FROM_JSON
  "Linter disposition depends on counts and file buckets from the JSON export."

[DP04]: CURRENT_SLICE_LIMITS
  "Next tasks depend on the known limits of the current specimen source slice."

[DP05]: LOCAL_COMMAND_OUTPUT
  "Verification status depends on fresh local command output."

[DP06]: PARTIAL_SOURCE_SLICE
  "The handoff depends on recognizing the current source as a bounded prototype
  slice."

[RQ01]: CLASSIFY_BEFORE_EDITING
  "Diagnostics should be grouped and understood before source edits are made."

[RQ02]: DISTINGUISH_SLICE_STATUS_FROM_REMAINING_WORK
  "Module status must separate applied slice work from remaining integration."

[RQ03]: NO_FALSE_ENGINE_READY_STATUS
  "The TODO must not imply broader engine readiness from linter cleanup."

[RQ04]: KEEP_PENDING_INTEGRATION_VISIBLE
  "Remaining integration tasks must stay visible and actionable."

[RQ05]: STATUS_REQUIRES_COMMAND_EVIDENCE
  "Reported status must be tied to command output or marked as blocked."

[RQ06]: DOCUMENT_STATUS_AND_REMAINING_WORK
  "The TODO must record what changed, what remains, and how to verify it."

[IN01]: LINTER_JSON_INPUT
  "The linter_error_output.json file supplied by the IDE Problems export."

[IN02]: SNAPSHOT_TOTAL_COUNT
  "The export contained thirty-seven diagnostics."

[IN03]: SNAPSHOT_SOURCE_SPLIT
  "The export split into eight mypy diagnostics and twenty-nine Pylance
  diagnostics."

[IN04]: ROOT_TYPE_PATTERN
  "Broad object-typed contracts caused static analyzers to lose field shape."

[IN05]: NO_MISSING_PROJECT_MODULES
  "The export did not report missing spinaltap module imports."

[IN06]: IDE_REFRESH_REQUIRED
  "The IDE Problems tab must be refreshed before treating the snapshot as live
  state."

[MO01]: CONTRACT_KERNEL_MODULE
  "The contract kernel and companion mapping validation module owning records,
  refusal states, payload shape checks, and proof hook primitives."

[MO02]: CONTEXT_WEIGHT_MODULE
  "The source module owning source-influence scoring behavior."

[MO03]: TIME_PACKET_MODULE
  "The source module owning fixed packet conversion behavior."

[MO04]: VERTEBRA_DELTA_MODULE
  "The source module owning local-state delta specimens."

[MO05]: SIGNAL_SPINE_MODULE
  "The source module owning ordered signal bundle routing."

[MO06]: STYLE_SURFACE_MODULE
  "The source module owning measurable style-limit translation."

[MO07]: SOFT_PROOF_MODULE
  "The source module owning proof record review behavior."

[MO08]: RECONCILIATION_MODULE
  "The source module owning single-worker routing and all-or-nothing
  multi-worker scalar step candidates."

[LD01]: CONTEXT_WEIGHT_DIAGNOSTICS
  "The context_weight.py diagnostic bucket from the IDE export."

[LD02]: TIME_PACKET_DIAGNOSTICS
  "The time_packet.py diagnostic bucket from the IDE export."

[LD03]: CONTRACT_KERNEL_TEST_DIAGNOSTIC
  "The test_contract_kernel.py optional-member diagnostic."

[LD04]: SIGNAL_SPINE_TEST_DIAGNOSTICS
  "The test_signal_constraint_spine.py residual-risk diagnostics."

[LD05]: SOFT_PROOF_TEST_DIAGNOSTICS
  "The test_soft_proof_lab.py optional-refusal diagnostics."

[LD06]: RECONCILIATION_TEST_DIAGNOSTICS
  "The test_spinal_reconciliation.py tuple and residual-risk diagnostics."

[LD07]: STYLE_SURFACE_TEST_DIAGNOSTICS
  "The test_style_constraint_surface.py optional-limits diagnostics."

[LD08]: TIME_PACKET_TEST_DIAGNOSTICS
  "The test_time_packet_pump.py assertAlmostEqual diagnostics."

[LD09]: VERTEBRA_TEST_DIAGNOSTICS
  "The test_vertebra_delta_worker.py residual-risk diagnostics."

[TK01]: TOOLING_MANIFEST_DECISION_TASK
  "Decide whether source tooling should be managed by a repo manifest."

[TK02]: MYPY_DEPENDENCY_TASK
  "Add mypy only through the chosen project tooling path if it becomes a gate."

[TK03]: IDE_REFRESH_TASK
  "Refresh and re-export VS Code Problems after source edits."

[TK04]: RUNTIME_CONTRACT_VALIDATION_TASK
  "Validate untrusted mappings before they become contract records."

[TK05]: GOVERNOR_DOWN_WEIGHT_TASK
  "Define or remove the currently unused down-weight decision path."

[TK06]: SOLVER_API_TIME_GATE_TASK
  "Add solver-facing APIs that accept fixed packets and reject raw dt."

[TK07]: VERTEBRA_CONSTRAINT_TASK
  "Implement measurable constraint enforcement for vertebra deltas."

[TK08]: SIGNAL_HOOK_TASK
  "Execute validation hooks before signal publication."

[TK09]: STYLE_SCHEMA_TASK
  "Turn string style limits into validated range or budget records."

[TK10]: PROOF_LEDGER_TASK
  "Add structured proof review records after evidence rules are specified."

[TK11]: RECONCILIATION_EXPANSION_TASK
  "Expand reconciliation to ordered workers, shared snapshots, conflict
  refusals, and complete scalar state candidates."

[TK12]: DOCSPEC_ALIGNMENT_TASK
  "Rerun document alignment checks when TODO or source status changes."

[VF01]: UNITTEST_VERIFICATION
  "Fresh unittest command evidence for the Python specimen tests."

[VF02]: PYRIGHT_VERIFICATION
  "Fresh Pyright command evidence for Pylance-class static diagnostics."

[VF03]: SYSTEM_MYPY_BLOCKED
  "Python 3.13 could not run mypy because the module is not installed."

[VF04]: VENV_MYPY_BLOCKED
  "Repo-local mypy was not run because this checkout has no virtualenv
  interpreter."

[VF05]: MARKDOWNLINT_VERIFICATION
  "Markdownlint verification for TODO and docspec documents."

[VF06]: PSEUDO_CITATION_AUDIT
  "Custom audit for missing, unused, duplicate, or misplaced marker
  definitions."

[VF07]: RUNNABLE_DEMO_VERIFICATION
  "Direct CLI and JSON subprocess evidence for the multi-worker scalar demo,
  including overflow backlog, oversized-delta refusal, and write conflicts."

[NT01]: SNAPSHOT_NOT_LIVE_STATE
  "The JSON export should not be treated as refreshed IDE state after edits."

[NT02]: NO_MISSING_IMPORT_MODULES_NOTE
  "No missing source modules were created because no missing-import diagnostics
  were present."

[NT03]: MYPY_CACHE_NOTE
  "The generated mypy cache directory is ignored by git."

[NT04]: SOURCE_SCOPE_NOTE
  "The current source includes contract specimens and a synchronous scalar
  multi-worker prototype; broader engine systems remain pending."
