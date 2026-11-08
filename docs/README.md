# 4GINE documentation and development catalogue [DOC]

Start with the [global plan](global_plan.md), select work through the
[root queue](../TODO.md), then use the
[development workflow](development_workflow.md). Individual status lives in
the task cards below. This catalogue preserves navigation and meaning across
the research, prototype and future application horizons [GL01].

## Document authority and reading order

> Goal: [GL01] - PRESERVE_THE_CATALOGUE_WITH_CLEAR_AUTHORITY
> Dependency: [DP01] - EXISTING_RECORDS_AND_CURRENT_PLAN
> Requirement: [RQ01] - QUALIFY_HISTORY_SCOPE_AND_IDENTIFIERS

| Document | Role | Authority boundary |
| --- | --- | --- |
| [Root README](../README.md) | Current behavior, destination and entry commands | Summary; detailed status belongs to task cards |
| [Global plan](global_plan.md) | Whole-project horizons, phases and exit gates | Current delivery authority |
| [Root TODO](../TODO.md) | Next-task pointer and historical source ledger | Queue only; historical TK states are dated |
| [Development workflow](development_workflow.md) | Per-change procedure and validation | Complements existing agent onboarding |
| [Setup guide](getting_started.md) | Bootstrap, verification and failure recovery | Selected Windows x64 development environment |
| [Automated checks](continuous_integration.md) | CI job, artifacts and failure diagnosis | Windows runner; evidence remains dated |
| [Bootstrap qualification](../reports/ST-002%20bootstrap%20qualification.md) | Cold/repeat setup, refusal cases and raw evidence | Observed Windows environment; CI remains separate |
| [Research plan](research_plan.md) | Method, guardrails, theories, lanes and styles | Preserved research vocabulary |
| [Live research](live_research.md) | Original sources and theory dispositions | Dated 2026-05-26 research snapshot |
| [Proposal](proposal.md) | Initial bounded prototype scope and module rationale | Original proposal, not the current work queue |
| [Requirements](requirements.md) | REQ01-REQ15 and prototype acceptance | Technical requirement authority; not a full product spec |
| [Design](design.md) | MG modules, DC contracts, VG gates and runtime boundaries | Current technical design |
| [Docspec tasklist](tasklist.md) | TK01-TK18 planning completion | Historical docspec work, not engine completion |
| [Initial source plan](sourcecode_plan.md) | Eight original slices and later scalar boundaries | Implementation history and traceability |
| [Changelog](logs/CHANGELOG.md) | Historical documentation changes | Append history; never treat old checks as current |
| [Realignment report][S01] | Findings, rationale and dated verification | Snapshot evidence, not a second roadmap |
| [Source review][S02] | Every source/test module and requirement boundary | Reviewed baseline 9afd1cf |
| [Planning review][S03] | Preserved catalogue, drift and migration reasoning | Input to this realignment |
| [Technical research][S04] | Primary sources, access results and influence limits | Support for constraints, not proof of the engine |
| [Initial catalogue inventory][S05] | Original paths, context definitions and reference locations | Frozen pre-realignment audit snapshot |

The inventory JSON is intentionally not a live planning manifest. Its line
numbers and findings describe the initial snapshot. Current consistency is
checked by [check_planning.py](../scripts/check_planning.py).

The [prototype tooling decision](decisions/prototype_toolchain.md) owns
selected development versions, required checks and ST-002's fresh-environment
qualification plan. It records the 2026-11-08 recovery of planning files that
were missing from the relocated checkout.

[Bootstrap.cmd](../Bootstrap.cmd) installs the selected local environment;
[Verify.cmd](../Verify.cmd) runs the required gates. Their implementation is
[bootstrap.ps1](../scripts/bootstrap.ps1) and [verify.py](../scripts/verify.py).
[Qualification](../scripts/qualify_bootstrap.py) uses disposable checkouts and
records cold setup, repeat setup and refusal specimens.

[VERIFICATION.md](../VERIFICATION.md) is an unclassified imported record about
a Rust media-deduplication tool. Its commands and tests are absent here. It is
preserved unchanged and is not evidence for 4GINE phases or required checks.

## Individual TODO catalogue

> Goal: [GL02] - CONNECT_EACH_WORKSTREAM_TO_DELIVERY
> Dependency: [DP02] - CANONICAL_TASKS_AND_PHASE_GATES
> Requirement: [RQ02] - ONE_MUTABLE_TASK_STATUS

| Workstream | Canonical cards | Main phase relationship |
| --- | --- | --- |
| [Tooling and workflow](todos/tooling.md) | ST-001-ST-004, ST-034 | P1 reproducibility and planning |
| [Contract kernel](todos/contracts.md) | ST-005, ST-006, ST-033 | P2 compatibility and evidence matrix |
| [Source governance](todos/governance.md) | ST-007-ST-009 | P2 policy and provenance |
| [Time](todos/time.md) | ST-010-ST-012 | P2 identity, replay and workload |
| [Workers](todos/workers.md) | ST-013-ST-016 | P2 scalar authority, P3 scoped richer state |
| [Signals and reconciliation](todos/signals.md) | ST-017-ST-019 | P2 candidate adoption; optional P5 discovery |
| [Style](todos/style.md) | ST-020-ST-022 | P3 typed limits, P4 rendered enforcement |
| [Proof](todos/proof.md) | ST-023-ST-024 | P2 executed-evidence semantics |
| [Application](todos/application.md) | ST-025-ST-032 | P3 scenario, P4 demonstration, P5 qualification |

Read the card for its current status, dependencies, acceptance and evidence.
This index intentionally carries no copied task statuses. New tasks receive a
unique ST identifier and an owning global phase; new workstream files must be
linked here and covered by the consistency checks.

## Requirement and contract crosswalk

> Goal: [GL02] - CONNECT_EACH_WORKSTREAM_TO_DELIVERY
> Dependency: [DP02] - CANONICAL_TASKS_AND_PHASE_GATES
> Requirement: [RQ02] - ONE_MUTABLE_TASK_STATUS

REQ identifiers below mean only definitions in
[requirements.md](requirements.md). DC/VG/MG meanings refer to
[design.md](design.md). A coverage link is not evidence that a requirement is
satisfied.

| Requirement | Meaning | Contract/gate | Current work |
| --- | --- | --- | --- |
| REQ01 | SPINALTAP identity and scope ownership | Architectural review | [Governance](todos/governance.md), [application](todos/application.md) |
| REQ02 | Bounded prototype before wider engine | Scope admission | [Global plan](global_plan.md), [application](todos/application.md) |
| REQ03 | Validated design and task trace before source | Change workflow | [Tooling](todos/tooling.md), [contracts](todos/contracts.md) |
| REQ04 | Govern source influence and risk | DC01 / VG01 | [Governance](todos/governance.md) |
| REQ05 | Convert elapsed time to fixed packets | DC02 / VG02 | [Time](todos/time.md) |
| REQ06 | Route ordered signals | DC03 / VG03 | [Signals](todos/signals.md) |
| REQ07 | Local bounded deltas | DC04 / VG04 | [Workers](todos/workers.md) |
| REQ08 | Measurable rendering/asset style limits | DC05 / VG05 | [Style](todos/style.md) |
| REQ09 | Specimen, failure path and promotion state | DC06 / VG06 | [Proof](todos/proof.md) |
| REQ10 | High-influence source gate | DC01 / VG01 | [Governance](todos/governance.md) |
| REQ11 | Fixed-time solver boundary | DC02 / VG02 | [Time](todos/time.md) |
| REQ12 | Validated mutation route | DC03 / VG03 | [Signals](todos/signals.md) |
| REQ13 | Explicit local ownership | DC04 / VG04 | [Workers](todos/workers.md), [signals](todos/signals.md) |
| REQ14 | Measurable-style gate | DC05 / VG05 | [Style](todos/style.md) |
| REQ15 | Runnable proof and failure advancement | DC06 / VG06 | [Proof](todos/proof.md), [contracts](todos/contracts.md) |

Application expansion must add actual requirements and design extensions
through ST-025 before P4 source work. Existing scope requirements trace that
decision; they do not silently specify a renderer or complete product.

## Source and specimen catalogue

> Goal: [GL03] - MAP_THE_EXECUTABLE_BASELINE
> Dependency: [DP03] - REVIEWED_SOURCE_AND_TEST_FILES
> Requirement: [RQ03] - KEEP_CODE_PRESENCE_SEPARATE_FROM_ACCEPTANCE

The MO identifiers in this table mean the original root TODO's concrete
module meanings. They differ from the research plan's conceptual MO taxonomy.

| Source file | Root TODO module | Design contract/gate | Responsibility |
| --- | --- | --- | --- |
| [contract_kernel.py](../spinaltap/contract_kernel.py) | MO01 | DC01-DC06 / VG01-VG06 | Records, refusal types, field registry, proof-shape hook |
| [contract_validation.py](../spinaltap/contract_validation.py) | MO01 | DC01-DC06 / VG01-VG06 | Strict mapping/dataclass ingress |
| [context_weight.py](../spinaltap/context_weight.py) | MO02 / MG01 | DC01 / VG01 | Source-score policy specimen |
| [time_packet.py](../spinaltap/time_packet.py) | MO03 / MG02 | DC02 / VG02 | Fixed packets and canonical solver steps |
| [vertebra_delta.py](../spinaltap/vertebra_delta.py) | MO04 / MG04 | DC04 / VG04 | Local scalar proposal validation |
| [signal_spine.py](../spinaltap/signal_spine.py) | MO05 / MG03 | DC03 / VG03 | Mandatory checks and synchronous hooks |
| [style_surface.py](../spinaltap/style_surface.py) | MO06 / MG05 | DC05 / VG05 | Current nonblank string-profile validation |
| [soft_proof.py](../spinaltap/soft_proof.py) | MO07 / MG06 | DC06 / VG06 | Current proof-record planning readiness |
| [reconciliation.py](../spinaltap/reconciliation.py) | MO08 / MG03, MG04 | DC03, DC04 / VG03, VG04 | Ordered scalar candidate staging |
| [demo.py](../spinaltap/demo.py) | Supporting harness | DC02-DC04 | Two-worker elapsed-time fixture |
| [__main__.py](../spinaltap/__main__.py) | Supporting CLI | Harness output | Text/JSON command and guard-dependent status |
| [__init__.py](../spinaltap/__init__.py) | Package identity | Not a separate design module | Package docstring |

| Test module | Reviewed methods | Evidence focus |
| --- | ---: | --- |
| [test_contract_kernel.py](../tests/test_contract_kernel.py) | 4 | Field registry and proof-shape refusal |
| [test_contract_validation.py](../tests/test_contract_validation.py) | 23 | Six ingress schemas and malformed inputs |
| [test_context_weight_governor.py](../tests/test_context_weight_governor.py) | 2 | Missing source and low originality blocks |
| [test_time_packet_pump.py](../tests/test_time_packet_pump.py) | 2 | Expansion and overflow |
| [test_vertebra_delta_worker.py](../tests/test_vertebra_delta_worker.py) | 2 | Local slice and outside-slice refusal |
| [test_signal_constraint_spine.py](../tests/test_signal_constraint_spine.py) | 3 | Ordered routing and mutation refusal |
| [test_style_constraint_surface.py](../tests/test_style_constraint_surface.py) | 2 | Complete strings and missing-field refusal |
| [test_soft_proof_lab.py](../tests/test_soft_proof_lab.py) | 2 | Text-complete readiness and absent plan |
| [test_spinal_reconciliation.py](../tests/test_spinal_reconciliation.py) | 2 | Single-worker route and refusal |
| [test_runtime_gates.py](../tests/test_runtime_gates.py) | 22 | Time, finite scalar bounds and hooks |
| [test_demo.py](../tests/test_demo.py) | 5 | Scripted final state, coupled refusal and CLI |
| [test_multi_worker_reconciliation.py](../tests/test_multi_worker_reconciliation.py) | 18 | Snapshot, ordering, conflicts and all-or-nothing return |

The 87 methods are a dated baseline count, not a permanent target.
[Planning-checker tests](../scripts/tests/test_check_planning.py) exercise the
documentation workflow separately. [Verifier tests](../scripts/tests/test_verify.py)
exercise failure propagation, lock drift, discovery and demo validation. See
the [source review][S02] for exact runtime guarantees and absent evidence.

## Preserved research catalogue

> Goal: [GL01] - PRESERVE_THE_CATALOGUE_WITH_CLEAR_AUTHORITY
> Dependency: [DP01] - EXISTING_RECORDS_AND_CURRENT_PLAN
> Requirement: [RQ01] - QUALIFY_HISTORY_SCOPE_AND_IDENTIFIERS

### Eight theory candidates

These TH identifiers belong to [research_plan.md](research_plan.md); their
recorded dispositions and FR formulations belong to
[live_research.md](live_research.md). Accepted here means retained for the
proposal, not implementation proof.

| Candidate | Recorded disposition | Current design relationship |
| --- | --- | --- |
| TH01 Signal-Routing Spine | Revise | FR01/MG03/DC03/VG03 |
| TH02 Vertebrae Local Solvers | Revise | FR02/MG04/DC04/VG04 |
| TH03 Context-Weight Governor | Core candidate | FR05/MG01/DC01/VG01 |
| TH04 Style-Constraint Layer | Revise | FR04/MG05/DC05/VG05 |
| TH05 Soft-Proof Pipeline | Revise | FR06/MG06/DC06/VG06 |
| TH06 Temporal Coherence Controller | Core candidate | FR03/MG02/DC02/VG02 |
| TH07 Visual Metric Translator | Revise | FR04/MG05/DC05/VG05 |
| TH08 Scope Boundary Allocator | Revise | FR01; ownership |

### Seven research lanes

[Research-plan](research_plan.md) RL01-RL07 retain their original questions:

1. RL01: engine-state routing.
2. RL02: local solver behavior.
3. RL03: temporal coherence.
4. RL04: context weight and originality.
5. RL05: style constraint mathematics.
6. RL06: soft-proof and validation.
7. RL07: module boundary mapping.

### Fifteen style categories

[Research-plan](research_plan.md) SY01-SY15 remain a research vocabulary:

| ID | Category | ID | Category | ID | Category |
| --- | --- | --- | --- | --- | --- |
| SY01 | Low-poly 3D | SY06 | Gouraud-shaded | SY11 | Cel/toon-shaded |
| SY02 | Texture-mapped low-poly | SY07 | Flat-shaded | SY12 | Arcade |
| SY03 | Affine-textured | SY08 | Billboarded | SY13 | Early real-time CGI |
| SY04 | Dithered | SY09 | Pre-rendered | SY14 | Sixth-generation |
| SY05 | Vertex-lit | SY10 | Fixed-function | SY15 | Retro 3D |

These categories are not fifteen committed modes or numeric hardware profiles.
ST-020 selects one bounded profile and gives it measurable meaning.

### Eleven original research sources

The records in [live_research.md](live_research.md) retain their original
2026-05-26 access context. The [technical review][S04] separately records
2026-11-07 checks and unavailable sources without rewriting those dates.

| Local ID | Original source family | Permitted role |
| --- | --- | --- |
| RS01 | Bevy ECS | Scope/order precedent, not selected architecture |
| RS02 | Godot nodes/scenes and SceneTree | Composition/activation precedent |
| RS03 | Box2D simulation and samples | Stepping and testbeds |
| RS04 | Position Based Dynamics | Bounded position-correction research |
| RS05 | Fix Your Timestep | Accumulation, interpolation and overload |
| RS06 | ACM plagiarism policy | Historical; refresh unavailable |
| RS07 | Khronos OpenGL Registry | Locate historical specifications |
| RS08 | Khronos Fixed Function Pipeline | Refresh unavailable |
| RS09 | Microsoft Direct3D 9 Architecture | Rendering constraint vocabulary |
| RS10 | Godot Unit Testing | Test/assertion precedent |
| RS11 | Bevy Creating Examples | Focused examples and testbeds |

The technical review contains sixteen local source records, including the
language/tooling evidence needed for this realignment. Those local RS numbers
do not replace the eleven older source identifiers. No external record proves
SPINALTAP's novelty, performance or governor calibration.

## Identifier boundaries and historical material

> Goal: [GL01] - PRESERVE_THE_CATALOGUE_WITH_CLEAR_AUTHORITY
> Dependency: [DP01] - EXISTING_RECORDS_AND_CURRENT_PLAN
> Requirement: [RQ01] - QUALIFY_HISTORY_SCOPE_AND_IDENTIFIERS

| Qualified family | Meaning | Handling |
| --- | --- | --- |
| research_plan.md::MO01-MO05 | Conceptual owners | Research taxonomy |
| TODO.md::MO01-MO08 | Concrete source modules | Historical source taxonomy |
| docs/tasklist.md::TK01-TK18 | Docspec tasks | Keep completion history |
| TODO.md::TK01-TK12 | Source/diagnostic tasks | Snapshot plus successors |
| docs/requirements.md::REQ01-REQ15 | Prototype needs | Technical authority |
| docs/design.md::DC01-DC06, VG01-VG06 | Contracts/gates | Technical |
| docs/todos/*.md::ST-nnn | Current work | Canonical task status |
| docs/global_plan.md::P1-P5 | Delivery phases | Outcomes and exits |

Two theory drafts are tracked despite the ignored parent directory:
[4GINE_v01](../.user_notes/depreciated_files/4GINE_v01.md) and
[4GINEv02](../.user_notes/depreciated_files/4GINEv02.md). Preserve their older
syntax and content as history; do not make ignored local notes a required
dependency of current development.

The required agent guide is
[ONBOARDING.md](../.agents/ONBOARDING.md), with the
[actual template](../.agents/template/TEMPLATE_ONBOARDING.md) and
[REFRESHER.md](../.agents/REFRESHER.md). Some internal links in those read-only
control files still target nonexistent template paths or ignored historical
copies. Use the working links here. The current project checks explicitly
exclude control files and historical drafts from format repair; this is a
scope declaration, not a claim those old paths pass validation.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [LI], [GL01], [GL02], [GL03]
- Dependencies: [DP01], [DP02], [DP03]
- Requirements: [RQ01], [RQ02], [RQ03]
- Review records: [S01], [S02], [S03], [S04], [S05]

## (Z) Context-Citations

[DOC]: DOCUMENTATION_AND_DEVELOPMENT_CATALOGUE
  "Navigation and authority map for preserved research, current contracts,
  canonical work items and dated evidence."

[GL01]: PRESERVE_THE_CATALOGUE_WITH_CLEAR_AUTHORITY
  "Retain theory, research, styles and history while identifying each record's
  role."

[GL02]: CONNECT_EACH_WORKSTREAM_TO_DELIVERY
  "Join individual work to global phases and technical requirements."

[GL03]: MAP_THE_EXECUTABLE_BASELINE
  "Make every reviewed package and test file reachable with evidence limits."

[DP01]: EXISTING_RECORDS_AND_CURRENT_PLAN
  "The original document chain, historical drafts and current delivery plan."

[DP02]: CANONICAL_TASKS_AND_PHASE_GATES
  "Task cards own status and acceptance; the plan owns global exit conditions."

[DP03]: REVIEWED_SOURCE_AND_TEST_FILES
  "Twelve package files and twelve runtime test files at baseline 9afd1cf."

[RQ01]: QUALIFY_HISTORY_SCOPE_AND_IDENTIFIERS
  "Same-spelled context IDs in different files must not be merged silently."

[RQ02]: ONE_MUTABLE_TASK_STATUS
  "Current task status is recorded only in its owning workstream card."

[RQ03]: KEEP_CODE_PRESENCE_SEPARATE_FROM_ACCEPTANCE
  "Source or test presence does not establish unexecuted engine-level claims."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for this file's context definitions."

[S01]: ../reports/4GINE%20development%20realignment.md
  "Dated synthesis of findings and realignment verification."

[S02]: ../research_notes/4GINE%20development%20realignment/source_review.md
  "Full source/test review and reproduced semantic gaps."

[S03]: ../research_notes/4GINE%20development%20realignment/planning_review.md
  "Planning catalogue, authority drift and migration analysis."

[S04]: ../research_notes/4GINE%20development%20realignment/technical_research.md
  "Primary-source verification ledger, context weights and limitations."

[S05]: ../research_notes/4GINE%20development%20realignment/catalogue_inventory.json
  "Frozen pre-realignment paths and context-reference audit; not a live
  manifest."
