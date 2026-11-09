# ST-005 contract identity review and merge record [DOC]

Date: 2026-11-09. Phase P2; requirements REQ03-REQ09. This records the
authorized CI-branch merge and the accepted contract identity specification.
The policy is documentation; version-aware runtime ingress remains ST-006.

> Goal: [GL01] - CLOSE_POLICY_WITH_REVIEWABLE_SOURCE_CONTEXT
> Dependency: [DP01] - MERGED_BASELINE_AND_CONTRACT_AUDIT
> Requirement: [RQ01] - DISTINGUISH_SPECIFIED_AND_EXECUTED_BEHAVIOR

## GitHub merge and checkout identity

The authorized branch codex/st-003-accepted-checks was three commits ahead of
main, with no divergence. Its exact head had a successful hosted check.
Main was fast-forwarded from 8519d3c13aa6e6e574cd241aed0a79187a704905 to
d7c789bc8090f4290163534317939a752aafaeab with an expected-head guard and
without force. The branch was retained. No PR or branch protection change was
needed for this fast-forward merge.

The [main-branch run](https://github.com/deadcoast/4GINE/actions/runs/42592497332)
passed at that merged head. This establishes actual main-branch automation;
the ST-003 report's unmerged statements remain accurate historical observations
from 2026-11-08.

Before aligning local Git state, all 97 working files were compared with the
clean qualified checkout and matched. The old index was backed up locally,
origin/main was fetched and checked against the exact target, and a mixed
reset aligned HEAD/index without rewriting working files. Source hashes stayed
equal and the checkout became clean before ST-005 edits began.

## Source review and decisions

Reviewed contract_kernel.py, contract_validation.py, soft_proof.py, their
contract-validation specimens, the design/requirements, and downstream contract
and proof cards. Source identity is the merged commit above. No runtime, test,
verification-script or toolchain change is part of ST-005.

The [decision](../docs/decisions/contract_identity.md) now specifies:

- A separate strict envelope API using exact contract/schema_revision identity,
  initial revision 1 for DC01-DC06 and pinned nested dependencies.
- All required fields, nullable rules, type/range checks and helper refusal
  fields; explicit shallow-snapshot and trusted-constructor limits.
- A preserved legacy/internal parser and an explicit, attributed legacy
  migration with validation before and after conversion and a receipt.
- Missing, unknown and mismatched identity refusals with nested paths and
  owning contract/gate attribution; no inferred latest version or fallback.
- Frozen revision meaning and separate proof-record, subject and dependency
  identities for later evidence records; no inferred execution or promotion.
- Deferred JSON Schema export until a concrete external value profile exists.
  No new runtime dependency or general serializer is selected.

The [example corpus](../docs/examples/contract_identity.json) contains six
revision 1 envelopes, one explicit legacy migration example and 18 refusal
examples. It includes boolean/float/string/unknown revisions, omitted nullable
fields, extra keys, wrong contracts and nested unversioned/unknown identities.
These are specified outcomes for ST-006, not tests of a new parser.

## Executed observations and verification scope

[Source observations](evidence/st-005/source-review.json) preserve the reviewed
source hashes, corpus hash and 15 current-runtime observations:

1. All six existing complete legacy bodies decode to their matching records.
2. All six proposed versioned envelopes are refused by the current legacy API.
3. Omitting nullable overflow_risk still fails at DC02.overflow_risk.
4. A trusted constructor can create a boolean packet count, but revalidation
   rejects it at DC02.packet_count.
5. Top-level snapshot writes fail, while an original nested mutable list stays
   shared. No deep immutability claim follows from frozen records.

The review used the selected .venv Python and the existing payload specimens.
Every corpus field list was compared with contract_fields for its contract.
No versioned decoder, migration adapter or schema exporter was executed.

The final verification command is:

```powershell
.\Verify.cmd
```

This passed the existing 87 runtime and 31 tooling tests, JSON demo, pinned tool
and lock checks, Pyright, planning/link/citation validation, Markdown lint and
whitespace. Planning and Markdown covered 33 files with zero issues; planning
also covered 34 cards, five phases and 15 requirements. The detailed latest
result is .tools/verification/latest.json. Git comparison against the merged
commit confirmed no runtime, tests, scripts, historical controls or unrelated
VERIFICATION.md changes. The task closure and next pointer receive the same
final gates after updating their canonical records.

## Handoff and remaining scope

ST-006 owns the proposed strict decoder, exact revision registry, explicit
legacy adapter/receipt and executed positive/refusal fixtures. Its card now
links this decision and the corpus. ST-023/ST-024 own the later evidence state
and record implementation; their acceptance references the identity policy.
The README, requirements, design and global plan separate this specification
from today's unversioned runtime. P2 remains open.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST005_POLICY_AND_MERGE_REVIEW
  "Dated merge verification, contract policy review and bounded source evidence."

[GL01]: CLOSE_POLICY_WITH_REVIEWABLE_SOURCE_CONTEXT
  "Complete the contract identity decision using the actual merged baseline."

[DP01]: MERGED_BASELINE_AND_CONTRACT_AUDIT
  "Qualified main revision, record/decoder sources and current validation tests."

[RQ01]: DISTINGUISH_SPECIFIED_AND_EXECUTED_BEHAVIOR
  "Policy examples do not imply that the future versioned parser exists."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every active local marker."
