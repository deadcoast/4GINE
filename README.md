CURRENT STATE:

4GINE is a research prototype for the SPINALTAP modular game-engine architecture. The repository contains a standard-library Python package that exercises contract validation and a deterministic scalar-state simulation. It is runnable software and a set of implementation specimens; it is not yet a 3D game engine.

Run the two-worker demonstration from the repository root with Python 3.13:

```powershell
py -3.13 -m spinaltap
```

Use `py -3.13 -m spinaltap --json` for the same report as JSON. The demo converts elapsed frame time into fixed updates, drains a capped backlog over later frames, runs a lateral worker before a motion worker, and adopts state only after the whole step succeeds. Its default sequence processes 14 fixed updates and finishes at `x = 0.672`, `y = -0.336`, with `0.008` seconds remaining. It also checks that an oversized update and overlapping writes are refused. A failing guard makes the command exit unsuccessfully.

The implementation uses only the Python standard library. `py -3.13 -m unittest discover -s tests` runs the current test suite. Pyright and markdownlint have been run from locally cached command-line tools; Mypy is not installed in this checkout, and the IDE diagnostic JSON is an older snapshot rather than a refreshed report.

The package is organized around six design contracts (`DC01`–`DC06`) and six validation gates (`VG01`–`VG06`):

| Contract | Current source role |
| --- | --- |
| `DC01` | Source claim scores, provenance fields, influence weight, risk, and governor decision. |
| `DC02` | Frame timing, fixed packet size/count, remainder, interpolation, and overflow information. |
| `DC03` | Ordered signal bundles, owner/channel metadata, constraint envelope, hook name, and residual refusal. |
| `DC04` | Worker-local state, constraints, one fixed time step, proposed delta, and residual refusal. |
| `DC05` | Ten nonblank string limits describing visual and asset constraints. |
| `DC06` | Claim, contract, specimen plan, failure path, promotion state, and evidence tier. |

`spinaltap/contract_kernel.py` defines immutable record shapes, contract and gate identifiers, refusal codes, promotion states, and the basic proof specimen hook. `spinaltap/contract_validation.py` parses complete external mappings: missing or unknown fields, wrong types, booleans masquerading as numbers, nonfinite values, and out-of-range scores are rejected with a field path and a blocked refusal. Nested signal bundles and time packets are checked too. Mapping fields get shallow read-only snapshots, so nested values remain the responsibility of their owning modules. Direct dataclass construction is treated as a trusted internal operation; callers accepting untrusted input should use `parse_contract`.

`spinaltap/context_weight.py` blocks unattributed claims and claims whose originality distance is below `0.20`; otherwise it allows influence using the bounded mean of authority, fit, originality, and validation-reach scores. The `DOWN_WEIGHT` enum exists, but there is no down-weight outcome yet. The threshold and averaging rule are prototype policy, not calibrated research results.

`spinaltap/time_packet.py` validates finite, nonnegative frame time and remainder, uses a positive fixed step, and caps each frame's work budget at 4096 packets. Excess time stays in the accumulator as backlog and is marked as overflow. `solver_steps` expands a frame packet into individual fixed-step records. Workers reject raw elapsed time and unexpanded frame packets. Small floating-point boundary corrections avoid losing an update to representation error. These records validate supplied values; they do not prove packet provenance or scheduler timing.

`spinaltap/vertebra_delta.py` accepts only a worker's registered keys and a state slice within that ownership. Its current constraint schema is exactly one finite, nonnegative `max_delta`; every proposed value must be a finite scalar with absolute magnitude at or below that limit for one step. An invalid component refuses the whole proposal. There are no vector norms, per-key budgets, nested state schemas, or clamping.

`spinaltap/signal_spine.py` checks bundle shape, worker refusals, fixed-step time, local ownership, and both worker and bundle scalar limits before invoking a named synchronous validation hook. `VG03` is a built-in pass-through hook after those checks. Unknown hooks, exceptions, invalid returns, or malformed refusals fail closed. Hooks are trusted code and have no timeout or side-effect isolation. An accepted bundle is eligible for caller-managed state publication; the spine itself does not own global state.

`spinaltap/reconciliation.py` exposes both a single-worker routing method and `reconcile_step` for ordered worker batches. Each worker reads a read-only view of the same initial scalar state snapshot. Repeated proposed write keys are rejected before any hook runs, including equal or zero writes. Workers are not combined or resolved by priority. The returned `StepResult` contains a read-only candidate state and ordered bundles only if every worker accepts; a failure returns no candidate and no partial bundle list. The method does not mutate the caller's state. Atomicity covers this returned candidate, not external side effects from trusted worker or hook code, concurrent publication, or durable commits.

`spinaltap/demo.py` connects the pump, workers, hooks, and reconciler, and applies only complete accepted steps to demo-owned state. `spinaltap/__main__.py` provides the text and JSON command-line output. `style_surface.py` and `soft_proof.py` provide current style-record and proof-promotion specimens, but style values are still strings and proof evidence is not persisted or audited in a ledger.

PLANNED COMPLETED STATE:

The intended destination is a usable 3D game engine organized around the SPINALTAP model: broad algorithm families own bounded local solvers, and a spinal-column layer coordinates validated state and publishes higher-level results. The Python prototype is a contract and workflow foundation, not evidence that renderer, physics, or game-loop systems are complete.

The project documents define requirements, module ownership, data contracts, failure behavior, and validation gates before promoting implementation claims. The planned engine would extend the current specimens with renderer and asset systems, richer simulation/state models, measurable visual constraints, controlled worker and channel ownership, and verifiable engine-facing state publication. New behavior should keep its input and output boundaries explicit and include a runnable failure specimen before it is described as implementation-ready.

STILL TODO:

- **Project setup and diagnostics:** decide how project tooling should be managed, install/configure Mypy if it is a required gate, and refresh the IDE Problems export. The checked-in `linter_error_output.json` records 37 older diagnostics (8 Mypy and 29 Pylance) and is not current status.
- **Source influence:** define and validate a real `DOWN_WEIGHT` path or remove the unused outcome; calibrate scoring and originality policy; connect source references to a provenance registry.
- **Time and workers:** define packet provenance and checkpoint policy; qualify scheduler behavior; extend scalar `max_delta` into justified per-key or vector schemas; add persistent worker registration and authority.
- **Signals and state:** define channel authorization and cross-worker constraints; choose whether conflicts remain refusals or gain explicit merge rules; isolate hook side effects; design general state publication and durable commits.
- **Style and proof:** replace string-only style descriptions with validated numeric ranges and budgets; translate them for a renderer; specify evidence tiers, proof records, persistence, source attachment, and promotion audits.
- **Engine systems:** implement rendering, asset handling, richer simulation, and an engine loop. The repository currently contains no renderer or production game engine.
- **Acceptance evidence:** extend validation beyond scalar unit specimens to integration and runtime behavior for the actual engine systems as they are built.

The tracked task and verification state is in [TODO.md](TODO.md). Architecture and contracts are in [docs/design.md](docs/design.md) and [docs/requirements.md](docs/requirements.md); the ordered source plan is in [docs/sourcecode_plan.md](docs/sourcecode_plan.md). The initial docspec planning record is [docs/tasklist.md](docs/tasklist.md).

