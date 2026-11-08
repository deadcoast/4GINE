# CHANGELOG

---
01:

[New Edited File](../../.user_notes/depreciated_files/4GINE_v01.md)

CHANGES:

* Treated `[DP00]`, `[RQ00]`, and added `[RS00]` as **reserved draft slots**,
  not broken IDs.
* Replaced completed section placeholders with real numbered IDs: `[DP01]`,
  `[RQ01]`, etc.
* Normalized naming artifacts:

  * `THEORIZE_BRAINSTOM` → `THEORIZE_BRAINSTORM`
  * `MULTI-MODDULATED` → `MULTI-MODULATED`
  * `SPINAL_TAP` → `SPINALTAP_ALGORITHM`
  * `[PW01]` retained only as a deprecated alias of `[WL01]`
* Completed the workflow chain:

  * `[WL01]` theorize brainstorm
  * `[WL02]` research
  * `[WL03]` proposal
  * `[WL04]` development docspec
  * `[WL05]` development sourcecode
* Added only one major structural enhancement: a pseudo-citation lint section
  `[LN]`, because it directly strengthens the format and catches the exact
  class of problems your draft is designed to tolerate during development.
* Added a research-source template `[RS]` / `[RS00]` without fabricating
  external paper citations.
* Added formal style IDs `[SY01]` through `[SY15]` so the style examples now
  participate in the pseudo-citation system instead of sitting as unlinked
  prose.
* Linted the completed file so every active pseudo-citation marker used in the
  document resolves to a definition in `(Z) Context-Citations`.

---
02:

* Removed all bracketed `[00]` placeholder IDs from the completed document.
* Stopped using `[ID]: ...` syntax above `(Z)`.
* Converted upper-document metadata into reference/invocation form:

```md
> Goal: [GL01] — FORMAT_ONBOARDING
> Dependency: [DP01] — CONTEXT_CITATION_REGISTRY
> Requirement: [RQ01] — FORMAT_INTEGRITY
```

* Reserved true Markdown reference-definition syntax for `(Z)` only:

```md
[GL01]: FORMAT_ONBOARDING
  "Full source-of-truth definition."
```

* Added a non-authoritative **LINK-COMPLETE USAGE INDEX** `[LI]` so every
  active registry definition is referenced at least once without redefining
  it.
* Added/expanded stable namespaces:

  * `[NS]` namespace model
  * `[CE]` citation entry model
  * `[EV]` evidence ladder
  * `[DS]` design objects
  * `[MO]` module objects
  * `[LN01]` through `[LN12]` lint rules
* Expanded goals, dependencies, requirements, workflow tags, theory
  candidates, style tags, evidence tags, design tags, and module tags.
* Preserved `[PW01]` only as a deprecated alias of `[WL01]`.

The core MD053 issue is this: Markdown sees any line shaped like `[label]:
destination "title"` as a real link reference definition. Your draft used that
shape both in blockquote metadata and again in `(Z)`, for example with
`[GL01]`, `[DP00]`, `[RQ00]`, and later registry entries. That creates
duplicate or unused reference-definition states depending on where the marker
is also referenced.

`MD053` flags two cases: a reference definition exists but is not used, or the
same normalized label is defined more than once. Markdownlint counts full,
collapsed, and shortcut references as valid usages, so `[GL01]`, `[GL01][]`,
and `[text][GL01]` can all satisfy the definition if `[GL01]: ...` exists.
([GitHub][1])

That is why the reliable drop-in pattern is:

```md
# Above (Z): reference only
> Goal: [GL01] — FORMAT_ONBOARDING

# In (Z): define once
[GL01]: FORMAT_ONBOARDING
  "Definition text."
```

---
03:

> LINTER CONFLICT

It trips “sometimes but not others” because the parser only treats the line as
a definition when it matches Markdown reference-definition shape. The
GFM/CommonMark shape is a label, followed by a colon, optional whitespace, a
destination, and optional title; reference definitions can appear before or
after their uses. Shortcut references like `[foo]` can then bind to `[foo]:
/url "title"`. ([github.github.com][2])

One more important detail: reference labels are normalized. Case differences
like `[GL01]` vs `[gl01]` are not separate labels; Markdown treats matching
labels by normalized form, and if multiple definitions match, the first one
wins. ([CommonMark Spec][3])

So the design rule I applied is:

```md
Only (Z) creates definitions.
Everything above (Z) invokes definitions.
The usage index makes every active definition needed.
No bracketed placeholder IDs survive link-complete mode.
```

That keeps the pseudo-citation design intact while making it acceptable to
markdownlint without silencing `MD053`.

[1]: https://github.com/DavidAnson/markdownlint/blob/main/doc/md053.md?utm_source=chatgpt.com "markdownlint/doc/md053.md at main"
[2]: https://github.github.com/gfm/?utm_source=chatgpt.com "GitHub Flavored Markdown Spec"
[3]: https://spec.commonmark.org/0.5/?utm_source=chatgpt.com "Version 0.5 (2014-10-25)"

---
04:

Created the agent-first onboarding document:

[Download
AGENT_ONBOARDING__PSEUDO_CITATION_FORMAT.md](../../.agents/ONBOARDING.md)

Validation completed:

* `markdownlint-cli2`: **0 errors**
* Custom link-completeness audit:

  * **81 definitions**
  * **81 unique active references**
  * **0 missing references**
  * **0 unused definitions**
* No active `[00]` placeholder IDs.
* No live bracket-colon definitions above `(Z) Context-Citations`.
* Includes explicit WHO / WHAT / WHERE / WHY / HOW onboarding.
* Includes CLI-agent editing protocol, shell scan patterns, MD053 repair
  logic, namespace model, completion rules, anti-patterns, corrective
  patterns, and a new-document template.
* The file itself is a working specimen of the current pseudo-citation format:
  body references, usage index, then single bottom registry.

I grounded the onboarding structure in the original draft’s compact
tag/reference model and bottom `(Z) Context-Citations` registry pattern.

---

05: 2026-11-07 development realignment

* Added the [global plan](../global_plan.md), five delivery phases and
  canonical workstream task cards; root TODO keeps the historical source ledger.
* Added the [catalogue](../README.md), qualified identifier crosswalks and
  [development workflow](../development_workflow.md).
* Preserved eight theory candidates, seven research lanes, fifteen style
  categories, eleven original sources and completed historical task records.
* Corrected current claims about proof readiness, numeric style, evidence tiers
  and the unresolved governor policy. No runtime behavior changed in this pass.
* Repaired README structure, historical navigation and the research-plan usage
  index; the source-plan usage index now includes its validation-family marker.
* Added a standard-library planning checker and separate regression specimens.
* The original downloaded-onboarding artifact name above is retained; its
  obsolete sandbox link now points to the repository's active onboarding.
* Exact current checks and exclusions are recorded in the
  [realignment report](../../reports/4GINE%20development%20realignment.md).

---

06: 2026-11-08 prototype tooling decision and checkout recovery

* Recovered completed planning documents and the prerequisite-completion
  checker fix from the prior workspace after finding them absent in the
  relocated checkout. Runtime, runtime tests and historical controls match.
* Recorded the [ST-001 tooling decision](../decisions/prototype_toolchain.md):
  exact target versions, lock ownership, required checks, optional Mypy and
  a clean-environment qualification plan. No new tool environment is claimed.
* Closed ST-001 with local verification evidence and advanced the canonical
  queue to ST-002 for implementation and fresh-environment qualification.
* Catalogued the unrelated Rust VERIFICATION.md as an unclassified imported
  record, preserved unchanged and excluded from 4GINE acceptance evidence.

---

07: 2026-11-08 prototype bootstrap and environment qualification

* Implemented pinned repository-local Python, uv, Node/npm and checker setup,
  versioned lockfiles, Bootstrap.cmd and Verify.cmd. Runtime dependencies
  remain empty; runtime code and specimens are unchanged.
* Added verifier regression tests and a disposable cold-checkout qualification
  harness covering repeat setup, unchanged inputs and eight expected refusals.
* Disabled managed Python executable shims and Windows registration; the final
  qualification confirms existing interpreter registrations remain unchanged.
* Added the [setup guide](../getting_started.md), updated entry commands and
  published the [qualification record](../../reports/ST-002%20bootstrap%20qualification.md)
  with raw command output, source identities and explicit simulation limits.
* Closed ST-002 and advanced the canonical queue to ST-003 for automated checks.
