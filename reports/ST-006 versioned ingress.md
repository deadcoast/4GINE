# ST-006 versioned ingress and migration evidence [DOC]

Date: 2026-11-09. Phase P2; requirements REQ03-REQ09. This implements the
[accepted identity policy](../docs/decisions/contract_identity.md) in the local
working tree based on d7c789bc8090f4290163534317939a752aafaeab. Pre-existing
ST-005 documentation is retained. No new commit, push or hosted CI result is
claimed for this implementation.

> Goal: [GL01] - EXECUTE_EXPLICIT_CONTRACT_COMPATIBILITY
> Dependency: [DP01] - ACCEPTED_IDENTITY_POLICY_AND_PINNED_ENVIRONMENT
> Requirement: [RQ01] - PRESERVE_REFUSALS_AND_ATTRIBUTE_MIGRATION

## Implemented boundary

[contract_validation.py](../spinaltap/contract_validation.py) adds
parse_contract_envelope, immutable identity/results, a read-only exact-revision
registry and migrate_legacy_contract. All six contracts support revision 1.
DC03 pins DC04 revision 1, which pins DC02 revision 1. Descriptor field lists
and enum vocabularies are fixed independently of future kernel additions.
Each descriptor records its direct dependencies and policy document.

Strict ingress requires complete mappings at every envelope and payload
boundary, including required nullable fields. Unknown fields/revisions,
booleans as numbers/revisions, nonfinite values, unversioned children and
mismatched identities fail with structured blocked refusals. Nested errors
preserve the full wire path and the failing child's contract/gate.

The original parse_contract API, return types and legacy field paths remain.
Existing modules continue revalidating their internal dataclasses. Neither API
detects the other format or silently migrates it. The shared body validators
preserve the reviewed semantics; incompatible future rules require separate
decoders and registry entries.

The deliberate adapter accepts only the exact d7c789b baseline and nonblank
caller attribution. It validates before conversion and again through strict
ingress. MigratedContract contains decoded and receipt fields. The immutable
receipt records source reference/revision, the contract's legacy-0 identity,
target identity and legacy-d7c789b-to-r1 adapter. Invalid attribution has its
own field path; invalid legacy bodies retain their original paths.

## Executed compatibility and migration cases

[Versioning tests](../tests/test_contract_versioning.py) add 30 test methods,
including parameterized cases. They execute the existing ST-005 specification
corpus unchanged: all six accepted envelopes and all 18 specified refusals
match their expected paths, owners, invalid_payload code and blocked state.
The corpus's original specification-only scope remains historical provenance.

[Eight migration fixtures](../tests/fixtures/legacy_contract_migrations.json)
contain complete input bodies and expected envelopes. They cover DC01-DC06,
an ordered two-signal refusal bundle and a previously implementation_ready
proof record. Each is exercised as a mapping and as a matching dataclass.
Receipts, record values/order/refusals and unchanged inputs are checked.

Additional cases exercise every required body/header field, wrong key types,
closed fields, exact header validation order, numeric boundaries, unknown
identities, bare nested dataclasses, helper refusal validation and empty/tuple
signals. A synthetic registered revision 2 proves that a parent pin still
refuses it; this test does not register production support for revision 2.

Migration refuses omitted nullable fields, malformed nested dataclasses,
unregistered baselines, invalid attribution and already versioned input.
An opaque object that raises on deepcopy survives migration by identity.
Snapshot tests show top-level isolation alongside shared nested mutable values.
Proof promotion and free evidence-tier text remain unchanged, without invented
subject revisions or execution timestamps.

The versioned DC02 frame decodes but cannot directly enter a solver. Expansion
through TimePacketPump yields a legal step; the worker then accepts a bounded
local delta and refuses oversized/outside-slice proposals. Existing integration
and CLI specimens remain part of the full runtime suite.

## Verification and retained evidence

Commands run from the repository root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests `
  -p test_contract_versioning.py -v
.\Verify.cmd
```

The dedicated suite passes 30 methods. The complete accepted checks pass
117 runtime methods (87 existing plus 30 new), 31 tooling methods, the JSON
demo, Pyright with zero errors/warnings, planning/link/citation validation and
Markdown lint across 34 documents, lock/version checks and whitespace.
Planning covers 34 cards, five phases and 15 requirements. The demo retains
14 accepted and zero refused scheduled steps, both refusal guards, final
x = 0.672 and y = -0.336, and about 0.008 seconds remainder.

The first full attempt caught two Pyright argument errors in the negative
metadata test helper. Explicit casts at that intentional invalid-input test
boundary resolved them; no type checks were disabled. Planning also caught a
historical heading link after a rename; restoring the stable anchor fixed it.
The final run uses
CPython 3.13.18, uv 0.13.7, Node 24.22.2, npm 11.19.1, Pyright 1.1.414 and
markdownlint-cli2 0.23.1 / core 0.41.1. Runtime dependencies remain empty.

The [retained verification record](evidence/st-006/verification.json) contains
command outputs, tool versions and source hashes for the implemented boundary,
tests, fixtures and policy. The full latest checkout verification is also
available locally at .tools/verification/latest.json, including the working
tree description and before/after input hashes. Task closure and the next-task
pointer receive a final accepted-check run after their updates.

## Limits and next work

This is local Python contract and scalar integration evidence. Constructors
remain trusted, snapshots remain shallow, receipts do not verify provenance,
and ingress never promotes proof or grants runtime authority. No serializer,
JSON Schema export, future migration chain, installed application, rendered
engine or human acceptance is demonstrated. Original artifacts must be kept
separately from migration receipts.

P2 remains open. The next queue entry is the ready governor policy decision,
[ST-007](../docs/todos/governance.md#st-007-resolve-governor-aggregation-and-down-weight-policy).
Proof-state semantics remain with ST-023/ST-024; authority, timing, typed style
and later application work retain their own cards and acceptance gates.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST006_VERSIONED_INGRESS_EVIDENCE
  "Local implementation and verification of exact contract revisions and migration."

[GL01]: EXECUTE_EXPLICIT_CONTRACT_COMPATIBILITY
  "Make the accepted six-contract policy executable without implicit migration."

[DP01]: ACCEPTED_IDENTITY_POLICY_AND_PINNED_ENVIRONMENT
  "ST-005 policy, d7c789b baseline and the selected repository-local toolchain."

[RQ01]: PRESERVE_REFUSALS_AND_ATTRIBUTE_MIGRATION
  "Retain field paths, shallow values and proof states while recording deliberate migration."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."
