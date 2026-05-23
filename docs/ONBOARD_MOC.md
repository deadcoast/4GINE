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
