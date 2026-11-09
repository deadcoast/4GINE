# Contract identity and schema evolution [DOC]

Decision date: 2026-11-09. Owning task ST-005, phase P2; requirements
REQ03-REQ09. The reviewed baseline at
d7c789bc8090f4290163534317939a752aafaeab accepted unversioned mappings through
parse_contract. ST-006 implements this accepted policy in the working source;
the [implementation record](../../reports/ST-006%20versioned%20ingress.md)
separates its executed evidence from the historical ST-005 source review.
Task acceptance belongs to [ST-006](../todos/contracts.md); proof semantics to
[ST-023/ST-024](../todos/proof.md).

> Goal: [GL01] - IDENTIFY_CONTRACTS_WITHOUT_SILENT_REINTERPRETATION
> Dependency: [DP01] - REVIEWED_RECORDS_AND_INGRESS_RULES
> Requirement: [RQ01] - SPECIFY_COMPATIBILITY_BEFORE_IMPLEMENTATION

## Decision and alternatives

Use a mapping envelope with exactly three required fields: contract,
schema_revision and payload. A contract identity is the pair of an existing
DC01-DC06 identifier and a positive integer schema_revision. Initial supported
revisions are 1 for all six contracts. VG01-VG06 remain gate identities, not
schema versions; package versions, Git revisions and task IDs are separate.

This keeps transport metadata outside the existing dataclass field lists.
Adding version fields directly to every constructor would change all internal
callers and mingle transport with domain state. A single repository-wide
version would couple unrelated contract changes. Semantic-version ranges or
implicit latest-version selection would be misleading for closed records that
reject unknown fields. Select explicit per-contract revisions and exact decoder
dispatch instead. No revision compatibility is inferred from numeric order.

The envelope describes a Python mapping ingress protocol. JSON examples use
serializable values for clarity; they do not promise serialization of arbitrary
Python objects currently allowed inside opaque mapping fields.

## Revision 1 envelope and nested identity

> Goal: [GL02] - MAKE_INGRESS_IDENTITY_UNAMBIGUOUS
> Dependency: [DP02] - EXACT_REVISION_AND_NESTED_DEPENDENCY_REGISTRY
> Requirement: [RQ02] - REFUSE_MISSING_UNKNOWN_OR_MISMATCHED_IDENTITIES

The API is parse_contract_envelope(expected_contract, envelope).
The caller supplies a valid ContractRef as its trusted expected contract;
an invalid programmer argument is an API error, not a fabricated DC refusal.
The external envelope is untrusted and must pass these checks in order:

1. Require a mapping with nonblank string keys. Require contract,
   schema_revision and payload in that order, then reject extra keys.
2. Require contract to be the exact, case-sensitive expected DC identifier.
   Unknown or different identifiers fail; never dispatch to another contract
   merely because the payload asks for it.
3. Require schema_revision to be a positive Python integer, excluding bool.
   Reject strings, floats, null, zero and negatives without coercion. A positive
   but unregistered revision fails before payload decoding.
4. Require payload to be a complete mapping for that exact revision. Apply the
   closed field inventory and validation rules below. Recurse into every
   embedded contract envelope using the parent's declared dependency revision.

The result is an immutable DecodedContract with identity and record fields.
Identity is a ContractIdentity containing contract and schema_revision; record
is the corresponding existing domain dataclass. Do not erase identity at
external ingress. Internal domain calls can use record, but evidence and
serialization boundaries must retain identity. Neither wrapper proves source
authenticity, executed evidence or deep immutability.

| Parent revision | Embedded contract revisions |
| --- | --- |
| DC01 revision 1 | None |
| DC02 revision 1 | None |
| DC03 revision 1 | Each ordered_signal_bundle element is DC04 revision 1 |
| DC04 revision 1 | time_packet is DC02 revision 1 |
| DC05 revision 1 | None |
| DC06 revision 1 | None; contract_ref names the subject |

DC03 revision 1 therefore transitively pins DC02 revision 1. Empty signal lists
remain valid, while their declared item type still has that dependency.
Do not inherit an omitted nested revision from the parent, accept mixed
revisions, or unwrap an unversioned child automatically. A future child revision
requires a separately reviewed parent revision/dependency declaration before
that child can appear there. Ordered lists/tuples retain their order.

## Complete revision 1 body inventory

> Goal: [GL03] - PRESERVE_REQUIRED_FIELDS_AND_EXISTING_BOUNDARIES
> Dependency: [DP01] - REVIEWED_RECORDS_AND_INGRESS_RULES
> Requirement: [RQ03] - NO_IMPLICIT_DEFAULTS_OR_DEEP_FREEZE_CLAIMS

All fields listed below are required even when their value may be null.
Unknown fields fail. Strings are preserved rather than trimmed; a nonblank
requirement checks whitespace without rewriting the value. Numeric fields
accept int/float and produce finite floats, excluding bool, numeric strings,
overflow and values outside their specified bounds. Packet counts and revision
identities are integer fields and do not accept float representations.

### DC01: SourceClaim

- source_ref: string or null; blank strings are representable so the governor
  can issue its existing missing-source refusal.
- claim_text: nonblank string.
- source_authority, claim_fit, originality_distance and validation_reach:
  finite numbers in 0..1 inclusive.
- influence_weight: null or a finite number in 0..1 inclusive.
- risk_flag: null or a nonblank string.
- governor_decision: null, allow, down_weight or block.

These fields do not verify source provenance or empirically calibrate scores.
The [governor policy](governor_policy.md) selects minimum aggregation,
implemented under ST-008. Versioned ingress remains structural and does not
assert which governor policy produced stored output fields. Fresh evaluation
and its policy identity are separate from literal decoding/migration of
historical records.
No DC01 revision 1 field, range, vocabulary or acceptance rule changes here.

### DC02: TimePacket

- elapsed_time: finite nonnegative number.
- fixed_packet_size: finite positive number.
- packet_count: nonnegative integer, excluding bool.
- accumulator_remainder: finite nonnegative number.
- interpolation_state: finite number in 0..1 inclusive.
- overflow_risk: null or a nonblank string.

Zero counts and backlog larger than one fixed packet remain valid ingress
states. Solver-step rules, pump budgets and timing consistency are separate
domain checks. Revision 1 does not certify packet origin or replay identity.

### DC03: SignalBundle

- owner, channel and validation_hook: nonblank strings unless residual_risk
  is a valid refusal; in that case blank strings remain representable.
- ordered_signal_bundle: list/tuple of DC04 revision 1 envelopes; decode into
  an ordered tuple of DeltaPacket records. Empty is permitted.
- constraint_envelope: mapping with nonblank string keys and opaque values.
- residual_risk: null or the refusal helper defined below.

### DC04: DeltaPacket

- local_state_slice, constraint_set and bounded_delta: mappings with nonblank
  string keys and opaque values.
- time_packet: a DC02 revision 1 envelope.
- residual_risk: null or the refusal helper defined below.

The worker/spine retain their scalar ownership, finite-value and max_delta
checks. Ingress does not grant authority, validate all opaque values or make a
candidate durable. Field names and body meanings otherwise match the reviewed
legacy records; embedded contract envelopes are the transport change.

### DC05: StyleLimits

Each of geometry_limit, lighting_limit, texture_limit, color_limit, fog_limit,
alpha_limit, depth_limit, camera_limit, animation_cadence and artifact_limits
is a required nonblank string. Revision 1 preserves the current string-only
boundary; measurable typed limits require the ST-020/ST-021 decision and a new
DC05 revision. Text such as vague still meets this structural rule.

### DC06: ProofRecord

- claim_ref: nonblank string.
- contract_ref: a known DC01-DC06 value naming the subject contract.
- specimen_plan and failure_path: strings; blank values remain representable
  for the proof hook's specific missing-plan/failure refusals.
- promotion_state: candidate, blocked or implementation_ready.
- evidence_tier: nonblank string; a controlled vocabulary is ST-023 work.

The DC06 envelope identifies the proof record's own schema, not the subject's
revision. Revision 1 keeps the old planning record shape. It cannot on its own
identify a tested subject revision or demonstrate execution. Do not infer
either from its existing promotion_state label.

### Refusal helper and opaque mappings

The helper has exactly contract, gate, code, reason and promotion_state.
Contract and gate must be known and correspond; code must be a known
RefusalCode, reason nonblank, and promotion_state blocked. Matching
RefusalState instances may be supplied but must be revalidated, as today.
It is not a seventh top-level contract: its shape belongs to the containing
DC03/DC04 revision. Its contract/gate identify the failing domain, not a
new subject revision. Adding a helper field or accepted code requires affected
parent revisions; existing identities cannot silently change their code set.

The initial code set is invalid_payload, constraint_violation,
validation_failed, write_conflict, hidden_influence, raw_dt,
direct_global_mutation, outside_local_slice, vague_style, missing_specimen and
missing_failure_path.

Mappings get shallow read-only snapshots. Top-level caller mutations do not
alter them, but a mutable list/object stored as a value can remain shared.
Freeze only the validated structure; do not deep-copy, serialize or normalize
opaque values as an incidental migration. JSON safety, cycles and value schemas
need explicit future decisions. A frozen dataclass does not validate its
constructor arguments or recursively freeze values.

## Compatibility, migration and refusal paths

> Goal: [GL04] - MAKE_COMPATIBILITY_EXPLICIT_AND_AUDITABLE
> Dependency: [DP02] - EXACT_REVISION_AND_NESTED_DEPENDENCY_REGISTRY
> Requirement: [RQ04] - NEVER_GUESS_OR_SILENTLY_UPGRADE_INPUT

Retain parse_contract(contract, payload) as the explicit legacy/internal
compatibility path, with its existing return types, revalidation and error
paths. It does not assign a schema revision. Existing constructors, module
calls and baseline tests may continue using it. New external callers needing
version guarantees must call parse_contract_envelope; neither function should
auto-detect or silently fall back to the other format.

Bare contract dataclasses are not versioned envelopes or versioned embedded
children. Revalidate matching dataclasses at the legacy/internal boundary.
Simply constructing ContractIdentity or DecodedContract is also trusted code,
not proof that external validation ran.

The pre-version baseline is called legacy-0 only in migration/evidence records.
Zero is never an accepted envelope revision. Initially register one explicit
migration source: d7c789bc8090f4290163534317939a752aafaeab, covering all six
reviewed legacy record shapes. Do not claim compatibility with an arbitrary
historical commit just because its fields happen to fit.

Provide migrate_legacy_contract(expected_contract, payload, source_revision,
source_ref) as a deliberate adapter. source_revision must identify
that registered baseline and source_ref must be nonblank. This context is
caller attribution, not automatic provenance verification. The adapter must:

1. Validate the complete legacy input, including matching dataclasses, nested
   records, nullable fields and refused cases. Do not fill absent fields.
2. Wrap the validated root and embedded contracts as revision 1 envelopes,
   preserving values, ordering and residual refusals without mutating input.
3. Validate through the strict versioned path and return decoded identity and
   record plus a migration receipt. The receipt names source_ref,
   source_revision, source identity legacy-0, target identity and adapter ID
   legacy-d7c789b-to-r1. Keep the original source artifact independently.
4. Preserve proof promotion text as historical data; never create evidence,
   subject revisions, timestamps of execution or new trust during migration.

No generic future migration, automatic chain or downgrade is approved. A new
supported edge needs reviewed input/output identities, loss policy and positive
and refused fixtures. If a conversion needs invented units, authority, defaults
or proof semantics, refuse it until the owning policy provides that meaning.

Strict envelope errors use ContractValidationError with invalid_payload,
blocked promotion and the existing contract/gate attribution model. Use actual
envelope paths, for example DC02.schema_revision or
DC03.payload.ordered_signal_bundle[1].payload.time_packet.schema_revision.
That nested example belongs to DC02/VG02. Unknown/mismatched identities are
attributed to the caller's expected contract at that position. Legacy error
paths remain unchanged; do not promise exact human reason wording as an API.
Recognized payload domain refusals remain domain refusals; structural decoding
alone does not authorize a solver step or promote a claim.

### Implemented Python API and migration receipt

The APIs and immutable identity/result/receipt types live in
[contract_validation.py](../../spinaltap/contract_validation.py). For example,
load the checked-in corpus from the repository root:

```python
import json
from pathlib import Path

from spinaltap.contract_kernel import ContractRef
from spinaltap.contract_validation import (
    LEGACY_BASELINE_REVISION,
    migrate_legacy_contract,
    parse_contract_envelope,
)

examples = json.loads(Path("docs/examples/contract_identity.json").read_text())
decoded = parse_contract_envelope(
    ContractRef.DC02, examples["accepted_envelopes"]["DC02"]
)
identity, packet = decoded.identity, decoded.record

legacy_body = examples["accepted_envelopes"]["DC02"]["payload"]
migrated = migrate_legacy_contract(
    ContractRef.DC02, legacy_body,
    source_revision=LEGACY_BASELINE_REVISION,
    source_ref="example:legacy-time-packet",
)
assert migrated.decoded == decoded
assert migrated.receipt.target_identity == identity
```

MigratedContract has decoded and receipt fields. MigrationReceipt has exactly
source_ref, source_revision, source_identity, target_identity and adapter_id.
The source identity is LegacyContractIdentity(contract, "legacy-0"), an audit
label rather than an envelope version. The target is ContractIdentity(contract,
1). Metadata is validated before the legacy body; invalid attribution uses
paths such as DC02.source_revision and DC02.source_ref. Invalid bodies retain
their legacy field paths. Receipts and result wrappers are frozen, but their
constructors are trusted and do not certify validation or provenance.

CONTRACT_SCHEMAS is a read-only exact-identity mapping. Each frozen descriptor
declares its body fields, direct nested identities, document reference, decoder
and frozen enum vocabularies. Shared legacy/revision 1 body validators preserve
the reviewed meaning; future incompatible rules need separate decoders and
registry entries. Migration is fixed to the reviewed baseline and revision 1;
future legacy changes must preserve that adapter's original interpretation.

## Revision changes and claim evidence

> Goal: [GL05] - BIND_EVIDENCE_TO_THE_MEANING_TESTED
> Dependency: [DP03] - FROZEN_CONTRACT_MEANING_AND_SOURCE_IDENTITY
> Requirement: [RQ05] - DO_NOT_TRANSFER_ACCEPTANCE_ACROSS_REVISIONS

A revision freezes fields, accepted types, nullability, ranges, enum meanings,
refusal rules and nested revision pins. A changed normative interpretation or
acceptance rule also needs a new revision, even if field names stay identical.
This includes additive fields in these closed records, changed units or score
semantics, and typed replacements for style strings. Register revisions
monotonically per contract, never reuse retired identities, and keep every
supported decoder's meaning fixed. An editorial correction or a bug fix that
restores the already-approved rule need not increment schema_revision; its
source commit and fresh verification still matter.

ST-006 implements a registry keyed by exact ContractIdentity, including nested
pins and the document reference describing each supported revision. An unknown
positive revision fails; a future supported older revision may decode only
through its registered decoder. No >=, latest, or inferred compatibility range.

Claim evidence must distinguish these identities, illustrated as a fragment:

```json
{
  "claim_ref": "claim:bounded-step",
  "record_identity": {"contract": "DC06", "schema_revision": 1},
  "subject_identity": {"contract": "DC04", "schema_revision": 1},
  "dependency_identities": [{"contract": "DC02", "schema_revision": 1}]
}
```

This fragment is not an executed-evidence record. ST-023/ST-024 must add actual
specimen/result, exact source revision, relevant configuration/environment,
artifact locator/digest and review decision. Record the subject's transitive
declared dependency identities as a deduplicated set in stable contract/revision
order. Its contract must match the proof body's contract_ref. Unknown/missing
subject revision or a mismatch cannot support acceptance. Legacy evidence keeps
its historical source identity and unresolved revision; do not relabel it as
revision 1 evidence. A later revision needs fresh review and verification,
not a copied accepted status.

## Old, current and unknown examples

> Goal: [GL02] - MAKE_INGRESS_IDENTITY_UNAMBIGUOUS
> Dependency: [DP02] - EXACT_REVISION_AND_NESTED_DEPENDENCY_REGISTRY
> Requirement: [RQ02] - REFUSE_MISSING_UNKNOWN_OR_MISMATCHED_IDENTITIES

Legacy DC02 body, accepted by today's parse_contract only:

```json
{
  "elapsed_time": 0.04,
  "fixed_packet_size": 0.016,
  "packet_count": 2,
  "accumulator_remainder": 0.008,
  "interpolation_state": 0.5,
  "overflow_risk": null
}
```

Revision 1 form, decoded by the strict API:

```json
{
  "contract": "DC02",
  "schema_revision": 1,
  "payload": {
    "elapsed_time": 0.04,
    "fixed_packet_size": 0.016,
    "packet_count": 2,
    "accumulator_remainder": 0.008,
    "interpolation_state": 0.5,
    "overflow_risk": null
  }
}
```

Replacing schema_revision with 999 must refuse at DC02.schema_revision before
decoding the body. Removing that property, using true, 1.0 or "1", or supplying
revision 0 must also refuse. A missing overflow_risk must refuse despite its
nullable type. ST-006 executes these specified outcomes in its test suite.

[Complete examples](../examples/contract_identity.json) include all six current
envelopes, old/current/unknown cases, mismatched identities and nested failure
paths. Accepted means structurally decoded; the DC02 frame above still needs
expansion before a solver can consume it. The corpus retains its ST-005
specification provenance; the separate ST-006 report records its execution
alongside nonfinite-number, constructor, shallow-sharing and domain-gate tests.

## Schema export decision and handoff

Defer JSON Schema export and any export CLI in ST-006. Keep runtime dependencies
empty. This decision and the exact decoder registry define the protocol;
the example JSON is an acceptance corpus, not a JSON Schema or validator.
The opaque mapping values have no complete JSON serialization contract yet.

If a concrete external consumer later needs export, first choose its JSON value
profile and dialect, then add generated schemas and parity tests against the
runtime. JSON Schema's properties keyword alone neither requires properties
nor rejects extra ones; an export would need explicit required and closed-field
rules [RS01]. Null and absence are distinct [RS02]. Even that structural schema
cannot replace the project's worker, ownership or proof-evidence gates.

ST-006 must cover all six identities, strict header checks, nested pins,
explicit migration receipts and legacy API compatibility. Keep source and
normalization side effects out of decoding. Proof-state redesign, authoritative
ownership, typed style, persistence and generalized serialization remain with
their owning cards. The implementation report records these tests and their
limits without closing those later workstreams.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [LI], [RS01], [RS02]
- Goals: [GL01], [GL02], [GL03], [GL04], [GL05]
- Dependencies: [DP01], [DP02], [DP03]
- Requirements: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05]

## (Z) Context-Citations

[DOC]: CONTRACT_IDENTITY_DECISION
  "Accepted ST-005 revision, compatibility and migration policy for ST-006."

[GL01]: IDENTIFY_CONTRACTS_WITHOUT_SILENT_REINTERPRETATION
  "Use explicit contract identities and preserve the historical source meaning."

[GL02]: MAKE_INGRESS_IDENTITY_UNAMBIGUOUS
  "Require exact outer and nested contract/revision identities."

[GL03]: PRESERVE_REQUIRED_FIELDS_AND_EXISTING_BOUNDARIES
  "Inventory all six record shapes without inventing domain validation."

[GL04]: MAKE_COMPATIBILITY_EXPLICIT_AND_AUDITABLE
  "Separate strict ingress, legacy compatibility and deliberate migrations."

[GL05]: BIND_EVIDENCE_TO_THE_MEANING_TESTED
  "Keep record, subject, dependency and implementation identities distinct."

[DP01]: REVIEWED_RECORDS_AND_INGRESS_RULES
  "contract_kernel.py, contract_validation.py and their specimens at d7c789b."

[DP02]: EXACT_REVISION_AND_NESTED_DEPENDENCY_REGISTRY
  "Per-contract supported revisions and frozen embedded-contract dependencies."

[DP03]: FROZEN_CONTRACT_MEANING_AND_SOURCE_IDENTITY
  "Normative rules, actual implementation revision and traceable evidence."

[RQ01]: SPECIFY_COMPATIBILITY_BEFORE_IMPLEMENTATION
  "Resolve ST-005 policy before ST-006 changes runtime ingress."

[RQ02]: REFUSE_MISSING_UNKNOWN_OR_MISMATCHED_IDENTITIES
  "No inference, coercion, fallback or acceptance of unregistered revisions."

[RQ03]: NO_IMPLICIT_DEFAULTS_OR_DEEP_FREEZE_CLAIMS
  "Nullable fields remain required and opaque nested values remain shallow."

[RQ04]: NEVER_GUESS_OR_SILENTLY_UPGRADE_INPUT
  "Migration requires an explicit registered source and recorded adapter."

[RQ05]: DO_NOT_TRANSFER_ACCEPTANCE_ACROSS_REVISIONS
  "A matching name or promotion label does not carry evidence to a new meaning."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."

[RS01]: https://json-schema.org/understanding-json-schema/reference/object
  "Official JSON Schema object reference; required and additional-property
  behavior consulted 2026-11-09. Export is deliberately deferred."

[RS02]: https://json-schema.org/understanding-json-schema/reference/null
  "Official JSON Schema null reference distinguishes null from absent values;
  consulted 2026-11-09."
