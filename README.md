CURRENT STATE: Runnable scalar prototype
========================================

4GINE is a runnable research prototype for the SPINALTAP modular game-engine
direction. Its standard-library Python package validates contracts and stages
synchronous scalar-state updates. It currently has no renderer, interactive
3D application, asset pipeline or general physics system [DOC], [RQ01].

Set up the selected Windows x64 environment, then run the two-worker
demonstration from the repository root:

```powershell
.\Bootstrap.cmd
.\.venv\Scripts\python.exe -m spinaltap
.\.venv\Scripts\python.exe -m spinaltap --json
```

The [setup guide](docs/getting_started.md) explains pinned local tools,
verification, failure recovery and intentional updates. First setup downloads
the selected tools; later checks use Verify.cmd.

The default scripted sequence accepts 14 fixed updates and finishes at
x = 0.672, y = -0.336, with about 0.008 seconds remaining. It checks oversized
delta and overlapping-write refusals. These are internal scalar specimens,
not evidence of an interactive engine or cross-platform replay [EV01].

PLANNED COMPLETED STATE: A usable SPINALTAP 3D engine
-----------------------------------------------------

The long-term direction is a usable 3D engine with bounded nervous-system
families, local vertebra solvers and spinal-column routing/reconciliation.
Smaller algorithmic stems pass bounded results to their parents. The
[global plan](docs/global_plan.md) separates reproducible prototype development,
trustworthy runtime claims, one scoped 3D demonstrator, and a qualified
application [GL01].

The first interactive scenario, target hardware, presentation backend,
production language boundary and distribution scope still require decisions.
The current Python prototype does not silently choose those answers.
The eight theories and fifteen style categories remain a preserved research
catalogue rather than a promise to deliver every proposed mode.

STILL TODO: Follow the phased development queue
-----------------------------------------------

Start with the [current queue](TODO.md) and its canonical task card.
The queue is the sole current next-task pointer. The
[workflow](docs/development_workflow.md) explains how to keep every change tied
to its phase, requirements and acceptance evidence.

- Maintain reproducible setup and automate the accepted checks.
- Resolve proof-state semantics and the governor minimum-versus-mean policy.
- Add the scoped timing, authority and whole-candidate evidence gates.
- Replace string-only style descriptions with typed, measurable limits.
- Define and qualify one interactive 3D application before wider engine work.

Individual statuses and dependencies live only in
[docs/todos](docs/README.md). Optional concurrency, durability, broader physics,
editor, audio and networking work needs an accepted use case; these are not
automatic prerequisites of the first demonstrator [RQ02].

Source and contract map
-----------------------

> Goal: [GL02] - EXPLAIN_THE_ACTUAL_SOURCE_BOUNDARIES
> Dependency: [DP01] - REVIEWED_CODE_AND_CONTRACTS
> Requirement: [RQ01] - CURRENT_CLAIMS_MATCH_IMPLEMENTATION

The package uses six design contracts and corresponding gates. Their technical
authority is [requirements.md](docs/requirements.md) and
[design.md](docs/design.md).

| Contract / gate | Current source role |
| --- | --- |
| DC01 / VG01 | Source scores, influence, risk and governor decision |
| DC02 / VG02 | Fixed packet size/count, remainder, interpolation and overflow |
| DC03 / VG03 | Ordered signals, owner/channel labels, envelope and hook |
| DC04 / VG04 | Local state, one fixed step, constraints and proposed delta |
| DC05 / VG05 | Ten nonblank strings describing style limits |
| DC06 / VG06 | Claim, contract, plan, failure path and promotion state |

[contract_kernel.py](spinaltap/contract_kernel.py) defines frozen record fields,
contract/gate identifiers, refusals and the proof-shape hook.
[contract_validation.py](spinaltap/contract_validation.py) validates complete
external mappings and revalidates matching dataclasses. Missing/unknown fields,
wrong types, booleans used as numbers, nonfinite values and invalid nested
records receive field-path refusals. Mapping snapshots are shallow. Frozen
records do not make arbitrary nested values immutable; direct constructors
remain trusted internal APIs.

[context_weight.py](spinaltap/context_weight.py) blocks missing attribution and
originality below 0.20, otherwise allowing a clamped arithmetic mean of four
caller-supplied scores. DOWN_WEIGHT exists but is unreachable. Historical FR05
specifies their minimum instead. ST-007 resolves that divergence; neither
formula or threshold has empirical calibration, and a nonblank reference does
not verify provenance.

[time_packet.py](spinaltap/time_packet.py) validates finite nonnegative elapsed
time/remainder, a positive fixed size and an integer budget of 1..4096 packets.
Excess time remains as backlog. Canonical solver steps contain one fixed update
and no frame remainder. Raw time and unexpanded frame packets are refused.
Floating-point boundary correction preserves intended step counts; it does
not prove packet origin, replay determinism or scheduler deadlines.

[vertebra_delta.py](spinaltap/vertebra_delta.py) validates a caller-proposed
delta against locally declared keys and exactly one finite, nonnegative
max_delta bound per scalar component. Proposed keys must exist in the local
slice. Any violation refuses the whole proposal without clamping. It is not
a general physical solver or persistent authorization registry.

[signal_spine.py](spinaltap/signal_spine.py) applies mandatory structure, time,
ownership and scalar-envelope checks before invoking a named synchronous hook.
The built-in VG03 hook passes after mandatory checks. Unknown hooks,
exceptions, invalid returns and malformed refusals fail closed. Hooks remain
trusted code, without timeout or side-effect isolation. The spine owns no
durable global state.

[reconciliation.py](spinaltap/reconciliation.py) supports single-worker routing
and ordered multi-worker steps. Every worker reads the same initial scalar
snapshot. Repeated proposed write keys, including equal or zero writes, fail
before hooks run. A StepResult exposes a read-only candidate and ordered bundles
only when all workers accept; failure exposes neither partial state nor partial
bundles. The caller adopts the result. This guarantees candidate-return
atomicity, not rollback of callback side effects, concurrent publication or
durable storage. Whole-candidate invariants remain future work.

[style_surface.py](spinaltap/style_surface.py) validates field presence and
nonblank text, not numeric units or budgets. A profile containing only the word
vague in all ten fields currently passes. ST-020/ST-021 define and implement
measurable semantics; ST-022 requires actual rendered enforcement evidence.

[soft_proof.py](spinaltap/soft_proof.py) checks proof-record shape, nonblank
specimen/failure text and contract/gate agreement. It can return
implementation_ready for an unexecuted docs-only plan. That current label
means structural planning readiness; the code does not execute a specimen or
verify a result artifact. ST-023/ST-024 establish explicit evidence semantics.

[demo.py](spinaltap/demo.py) calculates simple velocity-times-step proposals,
runs lateral/y before motion/x, applies complete candidates and consumes
scheduled time even when a step is refused.
[__main__.py](spinaltap/__main__.py) supplies text/JSON output and a failing
exit
status when its guards or expected default steps fail.
[__init__.py](spinaltap/__init__.py) identifies the package.

The [catalogue](docs/README.md) maps every source/test file, all fifteen
requirements, module identities and contracts. The [source review][S01]
records detailed boundaries and the three reproduced semantic gaps.

Verification and how to continue
-------------------------------

> Goal: [GL03] - PRESERVE_HONEST_REPRODUCIBLE_EVIDENCE
> Dependency: [DP02] - DATED_CHECKS_AND_CANONICAL_WORKFLOW
> Requirement: [RQ03] - DISTINGUISH_BASELINE_FROM_PRODUCT_ACCEPTANCE

```powershell
.\Verify.cmd
```

The 2026-11-07 runtime baseline at 9afd1cf passed 87 tests under Python 3.13.12
and Pyright 1.1.414. Those tests exercise ingress, scalar timing, constraints,
hooks and reconciliation; some intentionally preserve the current proof/style
semantics that the roadmap will strengthen. Planning-checker tests are
separate. Exact final documentation results belong to the
[realignment report][S02].

The earlier audit used cached static/Markdown tools; Mypy was unavailable.
The checked-in linter_error_output.json remains an older 37-diagnostic IDE
snapshot, separate from current command checks.

The [accepted tooling decision](docs/decisions/prototype_toolchain.md) records
the pinned environment and required checks. Bootstrap.cmd installs CPython
3.13.18, uv 0.13.7, Node 24.22.2, npm 11.19.1 and locked development tools
inside the checkout. Verify.cmd checks versions, locks, both test suites,
demo results, Pyright, planning, Markdown and unchanged inputs. Pyright is the
required type checker; Mypy is optional. Results and full command output are
saved in .tools/verification/latest.json.

The [bootstrap qualification](reports/ST-002%20bootstrap%20qualification.md)
records successful cold/repeat Windows setup, 87 runtime and 28 tooling tests,
all required gates and eight expected refusals. The
[automated-checks guide](docs/continuous_integration.md) describes the Windows
CI job and retained artifacts; the canonical card owns its acceptance status.

No renderer/GPU, installed application, performance budget or human acceptance
claim follows from these checks.

Read the [global plan](docs/global_plan.md), [catalogue](docs/README.md), and
[workflow](docs/development_workflow.md) before continuing. The
[initial source plan](docs/sourcecode_plan.md) and
[docspec tasklist](docs/tasklist.md) preserve completed earlier slices within
their original scope; they are not competing current backlogs.

(Y) Link-complete usage index
----------------------------

- Context: [DOC], [GL01], [GL02], [GL03], [DP01], [DP02]
- Requirements and evidence: [RQ01], [RQ02], [RQ03], [EV01], [S01], [S02]

(Z) Context-Citations
--------------------

[DOC]: CURRENT_PROJECT_ENTRY_POINT
  "Current source behavior, planned delivery horizons and navigation for 4GINE."

[GL01]: CONNECT_PROTOTYPE_TO_ENGINE_DIRECTION
  "Advance from a bounded scalar specimen to a scoped, qualified application."

[GL02]: EXPLAIN_THE_ACTUAL_SOURCE_BOUNDARIES
  "Describe implementation and its limitations rather than inferred maturity."

[GL03]: PRESERVE_HONEST_REPRODUCIBLE_EVIDENCE
  "Tie each completion claim to appropriate dated checks and artifacts."

[DP01]: REVIEWED_CODE_AND_CONTRACTS
  "The twelve source files, technical documents and current source review."

[DP02]: DATED_CHECKS_AND_CANONICAL_WORKFLOW
  "Recorded baseline checks and the maintained task/phase workflow."

[RQ01]: CURRENT_CLAIMS_MATCH_IMPLEMENTATION
  "Do not overstate frozen records, provenance, authority, proof or style
  checks."

[RQ02]: INDIVIDUAL_TASKS_FOLLOW_GLOBAL_SCOPE
  "Canonical task cards own status and carry phase, requirement and evidence
  links."

[RQ03]: DISTINGUISH_BASELINE_FROM_PRODUCT_ACCEPTANCE
  "Scalar checks do not establish a renderer, production performance or
  release."

[EV01]: INTERNAL_SCALAR_SPECIMEN_EVIDENCE
  "Current tests and CLI outputs support only the reviewed scalar prototype."

[S01]: research_notes/4GINE%20development%20realignment/source_review.md
  "Complete source and test review at baseline 9afd1cf."

[S02]: reports/4GINE%20development%20realignment.md
  "Dated realignment findings and verification record."
