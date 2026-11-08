# 4GINE implementation and evidence review [DOC]

Reviewed on 2026-11-07 against source at `9afd1cf`. This review covers all
12 Python package files and all 12 test files, plus the requirements, design,
source plan, README, and source TODO. Findings describe the bounded prototype;
they do not certify a complete engine [EV01]. The source and test links below
are the primary evidence; current execution logs belong to the coordinator's
verification record.

## What is implemented, and what does the code actually guarantee?

> Goal: [GL01] - DISTINGUISH_IMPLEMENTATION_FROM_INTENT
> Dependency: [DP01] - REVIEWED_SOURCE_AND_CONTRACTS
> Requirement: [RQ01] - PRESERVE_EVIDENCE_BOUNDARIES

### Takeaway 1

The executable core is a synchronous scalar-state proposal validator and
reconciliation specimen. It has strict contract ingress, fixed-step timing,
bounded deltas, ordered signal checks, and all-or-nothing candidate return.
It does not calculate general physical behavior, authorize identities, own a
world store, or render a scene. See the [reconciler](../../spinaltap/reconciliation.py),
[worker](../../spinaltap/vertebra_delta.py), and
[demonstration](../../spinaltap/demo.py).

### Cited findings: complete source inventory

| Source | Implemented responsibility | Important boundary |
| --- | --- | --- |
| [contract_kernel.py](../../spinaltap/contract_kernel.py) | Six contract enums, six gates, field registries, frozen records, refusals, specimen hooks | Frozen fields do not make arbitrary nested mappings immutable; proof hook checks text presence |
| [contract_validation.py](../../spinaltap/contract_validation.py) | Complete DC01-DC06 decoding, required/unknown fields, finite numbers, enums, nested records and field paths | Mapping snapshots are shallow; domain schemas and provenance remain separate |
| [context_weight.py](../../spinaltap/context_weight.py) | Blocks missing sources and originality below 0.20; otherwise clamps arithmetic mean to 0..1 | Scores are supplied by caller; no source registry, calibration or reachable down-weight outcome |
| [time_packet.py](../../spinaltap/time_packet.py) | Fixed packet conversion, bounded work, retained backlog, canonical solver steps | Validates supplied values; does not authenticate origin or maintain scheduler/checkpoint state |
| [vertebra_delta.py](../../spinaltap/vertebra_delta.py) | Declared-key ownership and finite per-component scalar max_delta checks | Validates caller-proposed changes rather than computing a general local solver result |
| [signal_spine.py](../../spinaltap/signal_spine.py) | Mandatory bundle checks followed by a registered synchronous hook | Registration identifies a callable, not an authorized worker/channel; no side-effect isolation |
| [reconciliation.py](../../spinaltap/reconciliation.py) | Shared scalar snapshot, ordered jobs, write-conflict preflight, complete candidate or refusal | No global candidate validator, persistent authority, versioned publication or durable commit |
| [style_surface.py](../../spinaltap/style_surface.py) | Rejects missing/blank fields and invalid mapping structure | Ten nonblank strings are accepted without parsing numeric or categorical limits |
| [soft_proof.py](../../spinaltap/soft_proof.py) | Builds a proof record, applies structural checks and matches contract to gate | Does not run specimens or validate evidence tier against observed evidence |
| [demo.py](../../spinaltap/demo.py) | Two scalar workers, velocity-times-step proposals, position hook, accepted-candidate adoption | Scripted elapsed-time samples; refused steps consume time; no real-time application loop |
| [__main__.py](../../spinaltap/__main__.py) | Text/JSON report and guard-dependent exit status | Demonstration CLI only; no project loading, assets or interactive runtime |
| [__init__.py](../../spinaltap/__init__.py) | Package identity docstring | No public facade or version declaration |

Specific implementation boundaries matter for later designs:

- `parse_contract` revalidates matching dataclasses as well as mappings.
  Every declared field, including nullable ones, is required. Unknown fields,
  booleans posing as numbers, nonfinite values and malformed refusal metadata
  are rejected. Direct constructors remain trusted internal entry points.
  See [decoder, lines 62-161](../../spinaltap/contract_validation.py).
- `TimePacketPump` accepts a positive fixed size and an integer packet budget
  in 1..4096. It keeps excess elapsed time as backlog, rather than bounding
  backlog itself. A four-ULP boundary correction is capped at one billionth of
  the fixed size. Solver packets are canonical one-step records with zero
  remainder/interpolation and no overflow flag. See
  [pump, lines 43-143](../../spinaltap/time_packet.py).
- Worker input keys must be within its locally declared `local_keys`, and
  proposed writes must already exist in the supplied slice. The only supported
  constraint is exactly `max_delta`; it applies separately to each scalar
  component, not a vector norm. Invalid proposals are refused in full, without
  clamping. See [worker, lines 24-138](../../spinaltap/vertebra_delta.py).
- The spine checks record structure, fixed-step time, delta ownership and
  worker/envelope scalar limits before a hook. Unknown hooks, exceptions,
  non-refusal return values and malformed refusal records fail closed. Its
  built-in `VG03` hook is a pass-through after mandatory checks. See
  [spine, lines 104-161](../../spinaltap/signal_spine.py).
- `reconcile_step` prepares all local views before any hook runs. Every worker
  reads the original snapshot; even zero or equal writes to one key conflict.
  A late refusal discards candidate state and all previously accepted bundles.
  Finite scalar addition is checked. Empty ordered batches return a snapshot
  no-op. See [reconciler, lines 51-158 and 248-285](../../spinaltap/reconciliation.py).
- Atomicity is limited to the returned state and bundle set. Trusted callback
  side effects, concurrent commits, storage durability and rollback are
  outside the guarantee. Scalar normalization converts integers to floats,
  so it should not be reused as an exact-integer store. See
  [reconciler, lines 58-62 and 236-245](../../spinaltap/reconciliation.py).
- Demo order is lateral/y then motion/x, with fixed size 0.016, budget four,
  scalar delta limit 0.25 and per-coordinate position limit -1..1. Refusals
  consume the scheduled time but publish neither coordinate. See
  [demo, lines 70-176](../../spinaltap/demo.py).

### Inferences 1

The prototype provides a useful executable contract baseline. The next
architecture work should strengthen policy and acceptance evidence before
adding renderer or physics breadth. Do not infer production determinism from
repeatability of the scripted scalar demo, or access-control guarantees from
caller-supplied ownership labels. These conclusions follow from the boundaries
in the [design](../../docs/design.md) and source inventory above.

### Gaps 1

No tracked manifest, lockfile, CI workflow, renderer, scene loader, asset
pipeline, input system, audio system or distributable application exists in the
reviewed tree. Python is the current specimen language; a final engine language
and backend have not been established by these sources. The initial scope
explicitly excludes a complete renderer or physics engine in
[requirements REQ02](../../docs/requirements.md) and
[source plan](../../docs/sourcecode_plan.md).

## What do the specimens prove, and where do claims outrun evidence?

> Goal: [GL01] - DISTINGUISH_IMPLEMENTATION_FROM_INTENT
> Dependency: [DP01] - REVIEWED_SOURCE_AND_CONTRACTS
> Requirement: [RQ01] - PRESERVE_EVIDENCE_BOUNDARIES

### Takeaway 2

Static enumeration finds 87 test methods. Coverage is strongest around mapping
boundaries, scalar timing, local constraints, hook failures and batch refusal.
The tests currently preserve the weak proof-promotion and style-string
behaviors; a passing suite does not close those semantic gaps [EV01].

### Cited findings: complete test inventory

| Test file | Methods | Behavioral evidence |
| --- | ---: | --- |
| [test_contract_kernel.py](../../tests/test_contract_kernel.py) | 4 | Field definitions, refusal state and missing proof plan |
| [test_context_weight_governor.py](../../tests/test_context_weight_governor.py) | 2 | Low originality and missing attribution block |
| [test_time_packet_pump.py](../../tests/test_time_packet_pump.py) | 2 | Frame expansion and overflow marker |
| [test_vertebra_delta_worker.py](../../tests/test_vertebra_delta_worker.py) | 2 | In-slice acceptance and outside-slice refusal |
| [test_signal_constraint_spine.py](../../tests/test_signal_constraint_spine.py) | 3 | Ordered routing, missing hook and direct mutation refusal |
| [test_style_constraint_surface.py](../../tests/test_style_constraint_surface.py) | 2 | Complete string profile accepted; missing fields refused |
| [test_soft_proof_lab.py](../../tests/test_soft_proof_lab.py) | 2 | Text-complete claim promoted; absent plan refused |
| [test_spinal_reconciliation.py](../../tests/test_spinal_reconciliation.py) | 2 | Single-worker routing and worker-refusal propagation |
| [test_contract_validation.py](../../tests/test_contract_validation.py) | 23 | All schemas, unknown/missing fields, bad numbers/enums, nested paths, top-level snapshot isolation and gate mismatch |
| [test_runtime_gates.py](../../tests/test_runtime_gates.py) | 22 | Raw-time refusal, packet budget, decimal/subnormal timing, 1000-frame accumulation, scalar constraints and hook failure |
| [test_demo.py](../../tests/test_demo.py) | 5 | Scripted final state, coupled refusal, position limits and JSON subprocess |
| [test_multi_worker_reconciliation.py](../../tests/test_multi_worker_reconciliation.py) | 18 | Ordering, shared snapshot, duplicate writes/owners, late failures, mutation/substitution attempts and no partial candidates |

The coordinator owns fresh execution results. The reviewed
[existing verification ledger](../../TODO.md) records a prior 87-test pass,
Pyright pass and five-document Markdown/citation checks; those entries are
historical evidence, not a fresh result for every document in the repository.

### Cited findings: three reproduced semantic gaps

Read-only probes on 2026-11-07 produced the following outputs. They were run
with Python 3.13 against the reviewed source, without changing runtime files.

- Proof probe: matching DC03/VG03, plan `not executed`, failure path
  `not observed`, and evidence tier `docs-only` returned
  `implementation_ready` with no refusal.
- Style probe: all ten fields set to `vague` were accepted with no refusal.
- Governor probe: authority=1, fit=0, originality=1 and reach=1 returned
  `allow` with influence 0.75; the research minimum formula produces 0.0.

The proof result follows from
[contract_kernel.py, lines 269-296](../../spinaltap/contract_kernel.py) and
[soft_proof.py, lines 30-76](../../spinaltap/soft_proof.py). `evidence_tier` is
only a nonblank string in
[contract_validation.py, lines 264-272](../../spinaltap/contract_validation.py).
The test named `test_complete_claim_produces_implementation_ready_proof_record`
asserts this promotion using text inputs alone in
[test_soft_proof_lab.py, lines 15-35](../../tests/test_soft_proof_lab.py).

The style result follows from
[contract_validation.py, lines 260-261](../../spinaltap/contract_validation.py)
and [style_surface.py, lines 28-54](../../spinaltap/style_surface.py). Even the
mapping fixture uses identical `specified_limit` strings for every field in
[test_contract_validation.py, line 85](../../tests/test_contract_validation.py).
Calling this a measurable-limit specimen, as the
[source plan step 6](../../docs/sourcecode_plan.md) does, overstates it.

The governor formula differs from the documented FR05 working relation.
[Live research, lines 265-275](../../docs/live_research.md) specifies the minimum
of four factors, while
[context_weight.py, lines 43-50](../../spinaltap/context_weight.py) implements
their arithmetic mean. No superseding decision is recorded in the reviewed
requirements, design or source plan. Neither formula is established as
calibrated truth. `DOWN_WEIGHT` is declared but never returned by the
[governor, lines 11-40](../../spinaltap/context_weight.py).

### Inferences 2

The proof wording has two levels that must be separated: a claim can be ready
for implementation planning after a specimen is specified; it cannot thereby
be treated as a verified implementation. The requirements demand a plan and
failure path, while the design also says to prevent proof by prose. This
ambiguity needs an explicit lifecycle decision before changing the API or
calling the current behavior a completed proof system. See
[requirements REQ09/REQ15 and DC06](../../docs/requirements.md) and
[design Soft-Proof Lab and validation design](../../docs/design.md).

### Gaps 2

There are no tests of evidence artifact identity, stale evidence, failed
specimen rejection, numeric style interpretation, source registry resolution,
reachable down-weight policy, scheduler deadlines, replay identity,
cross-worker aggregate invariants, persistent commits or actual rendered
output in the [test inventory](../../tests). Internal tests should not be
relabeled as external validation or human visual acceptance [EV01].

## How should global outcomes map to the next implementation tasks?

> Goal: [GL01] - DISTINGUISH_IMPLEMENTATION_FROM_INTENT
> Dependency: [DP01] - REVIEWED_SOURCE_AND_CONTRACTS
> Requirement: [RQ01] - PRESERVE_EVIDENCE_BOUNDARIES

### Takeaway 3

Preserve the original requirements and historical completed task records, but
add a single current work order with explicit acceptance conditions. Source
presence, docspec completeness, behavioral verification and engine acceptance
must be separate statuses. The current source ledger and initial source plan
already distinguish a bounded prototype from a full engine:
[TODO](../../TODO.md), [source plan](../../docs/sourcecode_plan.md).

### Cited findings: requirement-to-source map

| Requirement | Current source/evidence | Status for planning |
| --- | --- | --- |
| REQ01 SPINALTAP identity | [design stance](../../docs/design.md) | Manual architecture constraint; tests do not certify originality |
| REQ02 bounded prototype | [CLI/demo](../../spinaltap/demo.py) | Implemented scope boundary; full engine deferred |
| REQ03 docspec before source | [initial source gate](../../docs/sourcecode_plan.md) | Historical entry gate; future contract changes still need review |
| REQ04 governor output | [governor](../../spinaltap/context_weight.py) | Partial; unrecorded min/mean policy divergence |
| REQ05 time conversion | [pump](../../spinaltap/time_packet.py) | Implemented for supplied finite timing samples |
| REQ06 ordered signals | [spine](../../spinaltap/signal_spine.py) | Implemented routing specimen; authority/publication partial |
| REQ07 local bounded deltas | [worker](../../spinaltap/vertebra_delta.py) | Implemented scalar proposal validation |
| REQ08 measurable style | [style surface](../../spinaltap/style_surface.py) | Partial; strings do not constitute validated limits |
| REQ09 proof prerequisites | [proof lab](../../spinaltap/soft_proof.py) | Structural planning gate only |
| REQ10 high-influence source gate | [governor](../../spinaltap/context_weight.py) | Partial; supplied scores and unresolved policy |
| REQ11 fixed solver time | [canonical step check](../../spinaltap/time_packet.py) | Implemented shape; origin not certified |
| REQ12 routed mutations | [reconciler](../../spinaltap/reconciliation.py) | Implemented synchronous candidate boundary |
| REQ13 ownership | [worker](../../spinaltap/vertebra_delta.py) | Locally declared keys; persistent authorization absent |
| REQ14 measurable style gate | [style schema](../../spinaltap/contract_validation.py) | Unfulfilled beyond field/type completeness |
| REQ15 proof advancement | [proof hook](../../spinaltap/contract_kernel.py) | Ambiguous readiness semantics; no executed-evidence check |

Requirement meanings come from
[requirements.md](../../docs/requirements.md). Module naming must be qualified:
requirements/design use MG01-MG06, while root TODO uses MO01-MO08 and the
research plan has different MO meanings. Likewise, source TODO TK numbers are
not the same as docspec tasklist TK numbers. Every migration needs a document
path plus local ID, not an unqualified numeric label. See
[research plan](../../docs/research_plan.md), [TODO](../../TODO.md),
[tasklist](../../docs/tasklist.md), and
[source plan traceability table](../../docs/sourcecode_plan.md).

### Inferences: ordered task recommendations and acceptance

These are proposed work items for the global-plan author, not claims that work
is completed or that full engine systems have been approved.

1. __Establish a repeatable development baseline.__ Retain a standard-library
   runtime unless a dependency has a demonstrated need. Declare supported
   Python and developer tools, decide the required type checker(s), and provide
   one documented verification command. Acceptance: a fresh checkout can run
   the demo, tests and documentation checks with declared prerequisites;
   missing tools fail explicitly; fresh logs identify revision, interpreter,
   command, result and limitations. Preserve the old IDE snapshot as historical
   evidence. Existing scope: [source TODO TK01-TK03](../../TODO.md).
2. __Separate planned proof from executed evidence.__ Decide whether current
   `implementation_ready` means permission to implement or verified behavior;
   introduce unambiguous states and an evidence-tier vocabulary. Link each
   executed result to its claim, contract/schema revision, specimen, failure
   path and artifact. Acceptance: text-only claims never acquire an executed
   evidence state; known passing and failing specimens are distinguishable;
   unknown tiers, missing artifacts, mismatched revisions and stale results
   cannot silently advance a claim. Preserve migration semantics for old
   records. No arbitrary shell-command execution should be inferred from a
   plan string. Existing scope: [DC06/VG06](../../docs/design.md),
   [source TODO TK10](../../TODO.md).
3. __Resolve governor policy drift, then implement it.__ Record why the
   selected rule is minimum, mean or another justified policy; specify the
   0.20 boundary and whether down-weight remains a real outcome. Acceptance:
   divergent fixtures such as (1,0,1,1) match the chosen rule; boundary values
   around the originality threshold are covered; all retained decisions are
   reachable; missing or unresolved source references cannot claim verified
   provenance. Distinguish policy examples from empirical calibration.
   Existing scope: [FR05](../../docs/live_research.md),
   [source TODO TK05](../../TODO.md).
4. __Make style limits typed and measurable.__ Define units, numeric bounds,
   legal categorical values, cross-field relationships and preset identity
   before changing DC05. Acceptance: a concrete profile decodes to explicit
   budgets; nonfinite/negative or unit-mismatched numbers, unsupported enums,
   contradictory combinations and all-vague strings are refused. Translation
   does not count as renderer enforcement until measured render output exists.
   Existing scope: [REQ08/REQ14](../../docs/requirements.md),
   [source TODO TK09](../../TODO.md).
5. __Define temporal identity and replay before a real scheduler.__ Specify
   step identity, input sequencing, checkpoint contents, backlog policy and
   the current choice to consume refused steps. Acceptance: equivalent runs
   from a checkpoint reproduce state within a declared numeric model; stale,
   duplicate or out-of-order steps follow explicit refusal rules; sustained
   overload is measured and remains bounded by a chosen policy. Keep current
   fixed-step math tests. Existing scope:
   [pump and demo](../../docs/sourcecode_plan.md).
6. __Add authoritative state integration in a bounded slice.__ Define worker
   and channel ownership, typed state, schema/version handling, a whole-step
   invariant check and an adoption policy. Keep shared-write refusal as the
   default until a specific merge requirement exists. Acceptance: unknown or
   revoked identities fail; disjoint individually valid deltas that violate a
   combined invariant are refused together; a stale state version cannot be
   published; no failure exposes partial publication. Clearly document the
   trusted-hook boundary. Add durability or concurrency only when selected by
   a concrete application requirement. Existing scope:
   [reconciliation gaps](../../docs/design.md).
7. __Choose a first visible 3D vertical slice.__ Record the target platform,
   renderer/backend, language boundary, input and asset requirements, sample
   scene and frame/visual budgets. Acceptance: a directly runnable sample
   consumes only reconciled state, exercises interaction and refusals, and
   produces measured rendering evidence on named hardware. Treat physics,
   audio, editor tooling, networking and distribution as separately scoped
   capabilities, not automatic completion implied by a visible triangle.
   Existing boundary: [proposal scope](../../docs/proposal.md) and
   [REQ02](../../docs/requirements.md).

### Gaps and decision ownership

The source does not determine the target audience, release platform, renderer,
final implementation language or minimum useful engine experience. Those need
explicit product/architecture decisions before time estimates or broad engine
acceptance claims. Work can still proceed on the policy, reproducibility and
contract gaps above without pretending those larger decisions are settled.

## (Y) Link-complete usage index [LI]

This index references the active local markers without defining them.

- Document and evidence: [DOC], [EV01], [LI]
- Metadata: [GL01], [DP01], [RQ01]

## (Z) Context-Citations

[DOC]: IMPLEMENTATION_RESEARCH_NOTES
  "Source and test review of the 4GINE prototype at revision 9afd1cf on
  2026-11-07; a research input to the development realignment report."

[GL01]: DISTINGUISH_IMPLEMENTATION_FROM_INTENT
  "Explain actual behavior, evidence limits and the next decisions without
  treating code presence or text-complete plans as engine completion."

[DP01]: REVIEWED_SOURCE_AND_CONTRACTS
  "The spinaltap package, its twelve test modules, requirements, design,
  source plan and active or historical task ledgers provide primary evidence."

[RQ01]: PRESERVE_EVIDENCE_BOUNDARIES
  "Separate observed source behavior, reproduced probes, historical checks,
  proposed work and unverified engine-level capabilities."

[EV01]: INTERNAL_SPECIMEN_SCOPE
  "Internal scalar prototype evidence supports only the reviewed contract and
  runtime behaviors; it does not certify rendering, production performance,
  external originality review or human acceptance."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "A non-authoritative index of every active pseudo-citation in this file."
