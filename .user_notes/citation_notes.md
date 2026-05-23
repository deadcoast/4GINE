# ROUGH NOTES

## SHORT MARKDOWN CITATION FORMAT ONBOARDING

```md
[ID]: CATEGORY "Full contextual definition"
```

Then the rest of the document can reference that ID inline:

```md
The engine is supported by the SPINALTAP_ALGORITHM [SA].
```

So `[SA]` is not just a footnote; it is a contextual knowledge pointer back to the fuller definition in `(Z)`. Same for `[TP]`, `[SP]`, `[CW]`, `[DN]`, `[AS]`, and the goal/workflow/requirement/dependency markers.

I also understand the blockquote declarations at the top of sections:

```md
> [GL02]: LARGE_BATCH "..."
> [DP00]: TODO ""
> [RQ00]: TODO ""
```

These operate like local section-level metadata: goal, dependency, requirement, workflow step, ignore rule, or constraint. The bottom `(Z)` area then provides the global definitions, source-of-truth meanings, and reusable context.

---

## EDITS TO CITATION FORMAT

Completed and normalized the document against your uploaded draft.

[New Edited File](4GINE_v01.md)

CHANGES:

* Treated `[DP00]`, `[RQ00]`, and added `[RS00]` as **reserved draft slots**, not broken IDs.
* Replaced completed section placeholders with real numbered IDs: `[DP01]`, `[RQ01]`, etc.
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
* Added only one major structural enhancement: a pseudo-citation lint section `[LN]`, because it directly strengthens the format and catches the exact class of problems your draft is designed to tolerate during development.
* Added a research-source template `[RS]` / `[RS00]` without fabricating external paper citations.
* Added formal style IDs `[SY01]` through `[SY15]` so the style examples now participate in the pseudo-citation system instead of sitting as unlinked prose.
* Linted the completed file so every active pseudo-citation marker used in the document resolves to a definition in `(Z) Context-Citations`.
