# AGENT_ONBOARDING: How to utilize the Documents Proprietary Citation Format [AO]

This file is an ingestion document for a fresh local CLI agent. It assumes no
prior knowledge of the user, repository, project, document history, or citation
format. It explains how to read, preserve, extend, lint, and repair the current
pseudo-citation system used by the 4GINE / SPINALTAP document family [PJ].

This file is not written for human narrative reading. It is written as an
operational protocol for agents such as Codex, Claude Code, or another local
shell-based editing system [CLI].

## (0) Agent mission [GL01]

Your mission is to preserve a link-complete Markdown pseudo-source system while
editing or extending project documents [FM]. Treat the document as two connected
layers:

1. The upper body is a compact contextual knowledge map [BD].
2. The bottom registry is the source-of-truth definition layer [Z].

Never treat bracketed markers as decorative tags. Each active marker is a
context pointer that must resolve to one registry definition and must be used in
the body or the usage index [UI].

## (1) Who, what, where, why, how [WH]

### Who [WH01]

The expected reader is a fresh CLI agent with repository access but no project
memory. The agent may be asked to complete tags, add sections, normalize IDs,
repair lint errors, create related documents, or convert unfinished drafts into
link-complete form [CLI].

The project owner is designing a compact pseudo-sourcing format that borrows
from Markdown reference-link mechanics but repurposes them as contextual source
maps [FM]. The user is not asking for generic footnotes, generic academic
citations, or a new project config.

### What [WH02]

The format is a structured Markdown pattern where compact markers such as goal,
dependency, requirement, workflow, theory, style, evidence, and module IDs are
referenced throughout the body and defined once in a bottom registry [NS].

A marker is a compact context handle:

```md
The theory must remain technically plausible [TP] and avoid source replication
[DN01].
```

The registry entry is the full definition:

```md
[TP]: TECHNICALLY_PLAUSIBLE
  "A creative theory standard that permits novelty while rejecting incoherent,
  unbounded, or non-actionable speculation."
```

### Where [WH03]

Markers appear anywhere above the registry as references: headings, paragraphs,
lists, local metadata, design notes, usage indexes, or workflow summaries [BD].

Definitions appear only in the bottom section named `(Z) Context-Citations`
[RG]. Do not create live reference-definition lines above that registry [LN01].

### Why [WH04]

The format compresses repeated context. It lets the upper document stay small
while the bottom registry carries the full contextual weight, intent, and
source-of-truth definitions [CW].

The design also keeps the document compatible with markdownlint without changing
project lint configuration [MD]. It intentionally uses Markdown reference-link
syntax, so the system must respect Markdown reference-definition rules [DP01].

### How [WH05]

The operating rule is simple:

```txt
reference above; define once below; index all active markers; lint clean
```

A correct body invocation:

```md
> Goal: [GL01] — FORMAT_ONBOARDING
> Dependency: [DP01] — CONTEXT_CITATION_REGISTRY
> Requirement: [RQ01] — FORMAT_INTEGRITY
```

A correct registry definition:

```md
[GL01]: FORMAT_ONBOARDING
  "Define how the note uses compact contextual pseudo-citations, local
  metadata, and the bottom registry without losing traceability."
```

An incorrect upper-document metadata definition:

```md
> [GL01]: TODO ""
```

That incorrect form creates a real Markdown reference definition inside the
body. It can collide with the registry definition and trigger MD053 or related
reference-definition lint errors [MD053].

## (2) Core model [FM]

### (2.1) Body layer [BD]

The body layer is the readable working document. It uses markers as compact
references. The body may contain plain explanatory prose, technical theory,
metadata blocks, lists, code blocks, style lists, and workflow sections.

The body must not create active definitions. It must not use the live pattern:

```md
[ID]: DESTINATION "title"
```

except inside fenced examples or inside the bottom registry [LN01].

### (2.2) Registry layer [RG]

The registry layer is the final authoritative source of marker definitions. It
is normally the final major section of the document:

```md
## (Z) Context-Citations
```

Each active marker has one definition. The preferred registry shape is:

```md
[ID]: CATEGORY_LABEL
  "Complete contextual definition."
```

`ID` is the bracket marker, `CATEGORY_LABEL` is the compact destination, and
the quoted text is the source-of-truth explanation [CE].

### (2.3) Usage index [UI]

The usage index is a non-authoritative bridge section placed before the
registry. It references every active marker at least once. This keeps reference
definitions from being treated as unused by markdownlint [LN04].

The usage index is not the source of truth. It must not redefine markers. It
only invokes them.

### (2.4) Link-complete state [LC]

A file is link-complete when all of these are true:

- Every active marker used in the body resolves to exactly one registry entry.
- Every active registry entry is referenced at least once.
- The registry is the only live definition location.
- No zero-number placeholder IDs remain in active text.
- Deprecated draft tags are either removed or declared as explicit aliases.
- The file passes markdownlint under the existing project configuration.

## (3) Required syntax [SYX]

### (3.1) Marker reference syntax [MR]

Use marker references in the body:

```md
[GL01]
[DP04]
[RQ07]
[SA]
[SA01]
[TH03]
[SY14]
```

Shortcut references are acceptable because the registry supplies the matching
reference definitions [DP01].

### (3.2) Local metadata syntax [LM]

Use readable local metadata. Do not use bracket-colon syntax in metadata.

Correct:

```md
> Goal: [GL05] — THEORY_GENERATION_BATCH
> Dependency: [DP05] — CREATIVE_MATHEMATICAL_SPACE
> Requirement: [RQ06] — TECHNICAL_PLAUSIBILITY_FILTER
```

Incorrect:

```md
> [GL05]: TODO ""
> [DP00]: TODO ""
> [RQ00]: TODO ""
```

The correct form references existing definitions. The incorrect form creates
new reference definitions and may duplicate later registry entries [MD053].

### (3.3) Registry syntax [RSX]

Only the registry uses active reference-definition syntax:

```md
[DP05]: CREATIVE_MATHEMATICAL_SPACE
  "The brainstorm depends on technical imagination, loose early constraints,
  and strong anti-replication control."
```

Keep the category label short, stable, and mostly uppercase snake case [LN07].
Use the quoted definition for the full description.

### (3.4) Code examples [EX]

Code examples may show invalid or draft syntax only inside fenced code blocks.
Fenced blocks prevent markdownlint from interpreting those lines as live
reference definitions [LN08].

## (4) Namespace model [NS]

Use namespaces to keep marker families stable. Do not invent a new namespace
when an existing one already represents the concept.

| Namespace | Meaning                   | Typical use                             |
|-----------|---------------------------|-----------------------------------------|
| `[Z]`     | Context-citation registry | Bottom source-of-truth section          |
| `[FM]`    | Format model              | Rules for this pseudo-source system     |
| `[GL]`    | Goal                      | Desired outcome of a section or task    |
| `[DP]`    | Dependency                | Prerequisite or support object          |
| `[RQ]`    | Requirement               | Required condition or acceptance rule   |
| `[WL]`    | Workflow                  | Ordered project phase                   |
| `[TH]`    | Theory candidate          | Brainstormed or refined engine theory   |
| `[SA]`    | SPINALTAP algorithm       | Core engine organization model          |
| `[AS]`    | Algorithmic stem          | Modular formula ownership model         |
| `[CW]`    | Context weight            | Allowed influence of source material    |
| `[DN]`    | Do-not rule               | Negative contextual constraint          |
| `[SY]`    | Style                     | Formal visual/rendering style marker    |
| `[IG]`    | Ignore rule               | Excluded design direction or input      |
| `[RS]`    | Research source           | External source record pattern          |
| `[EV]`    | Evidence level            | Support strength for a claim            |
| `[DS]`    | Design object             | Proposal or docspec architecture object |
| `[MO]`    | Module object             | Sourcecode-facing module marker         |
| `[LN]`    | Lint rule                 | Pseudo-citation validation rule         |
| `[LI]`    | Link index                | Non-authoritative usage anchor          |

Numbered IDs extend the family. For example, `[GL]` defines the goal family,
while `[GL01]`, `[GL02]`, and `[GL03]` define individual goals [ID].

## (5) Project context the agent must know [PJ]

The current project family is 4GINE: SPINALTAP multi-modular algorithmic engine
[SA]. It is a novel three-dimensional game-engine theory and development path.
The core model uses a nervous-system-inspired algorithm chain:

```txt
[SA] = [SA01] -> [SA02] -> [SA03]
```

The conceptual meanings are:

- `[SA01]` nervous_system: broad but bounded algorithm families.
- `[SA02]` vertebrae: local solvers, transform units, and scoped formulas.
- `[SA03]` spinal_column: aggregation, routing, and reconciliation layer.

The biological terms are not decorative. They describe scope, ownership, data
routing, solver boundaries, and aggregation responsibility [SA].

The algorithmic stem model [AS] means smaller algorithmic stems solve bounded
jobs and pass results into parent stems. The project is intentionally novel, but
novelty must remain technically plausible [TP] and research-adjustable [SP].

## (6) Editing protocol for CLI agents [CLI]

### (6.1) Before editing [ED01]

1. Locate the bottom registry heading.
2. Build a registry map of every definition label.
3. Build a body-reference map of every marker reference outside fenced code.
4. Identify unresolved references, unused definitions, duplicates, aliases, and
   zero-number placeholders.
5. Do not start broad rewrites until the map is understood.

Useful shell scan patterns:

```sh
# Live reference definitions.
grep -nE '^\[[A-Za-z0-9]+\]:' file.md

# Illegal blockquote definitions above the registry.
grep -nE '^>\s*\[[A-Za-z0-9]+\]:' file.md

# Draft zero-number IDs.
grep -nE '\[[A-Z]{1,6}00\]' file.md

# Markdownlint validation.
markdownlint-cli2 file.md
```

### (6.2) When adding a new section [ED02]

Every substantial workflow or design section should have a goal, dependency,
and requirement metadata block [LN09]. Use existing IDs when the section is
already covered. Create new IDs only when the section introduces genuinely new
context.

Correct pattern:

```md
## (E) PROPOSAL: [WL03]

> Goal: [GL08] — PROPOSAL_FORMATION
> Dependency: [DP08] — PROPOSAL_INPUTS
> Requirement: [RQ09] — PROPOSAL_READINESS
```

Then define any new IDs once in the registry and add them to the usage index.

### (6.3) When resolving placeholders [ED03]

Do not preserve bracketed zero IDs in a link-complete pass [LN05]. Resolve them
by doing one of the following:

1. Infer the real concept and assign the next available numbered ID.
2. Reuse an existing ID if the existing definition already covers the concept.
3. Delete the placeholder if the metadata is not needed.
4. Convert unresolved intent into plain prose without brackets until it is real.

Do not write active placeholders such as:

```md
[DP00]
[RQ00]
[RS00]
[GL00]
```

A numbered ID is allowed only when the definition exists or is created in the
same pass [RQ03].

### (6.4) When renaming or correcting tags [ED04]

If a draft tag was misspelled or renamed, prefer the corrected active tag. Keep
the old tag only when historical continuity matters [LN06]. Old tags must be
explicit aliases, not silent duplicates.

Correct alias pattern:

```md
[PW01]: DEPRECATED_ALIAS
  "Former artifact tag for THEORIZE_BRAINSTORM; preserve only as historical
  draft context and use WL01 as the active workflow ID."
```

Do not keep two active IDs with the same meaning unless one is clearly marked
as deprecated or legacy.

### (6.5) When adding external research [ED05]

Do not fabricate research-source IDs. Create a numbered research-source entry
only after an actual source exists [RS]. Until then, describe the research need
in prose or task form without a bracketed source marker.

Research sources should carry context weight [CW]. External source influence
must not overpower the internal SPINALTAP structure [DN01].

Recommended source-record shape:

```md
[RSnn]: RESEARCH_SOURCE
  "TITLE: ...
  SOURCE: ...
  YEAR: ...
  LINK_OR_DOI: ...
  USED_FOR: ...
  CONTEXT_WEIGHT: LOW | MEDIUM | HIGH
  LINKED_CONTEXT: [SA], [THnn], [RQnn], [DPnn]"
```

## (7) Lint behavior and MD053 [MD]

Markdown treats this shape as a reference definition:

```md
[label]: destination "optional title"
```

The pseudo-citation format intentionally uses that mechanism in the registry.
Because of that, the system must obey Markdown reference-definition rules
[DP01].

MD053 can appear when a reference definition is unused, duplicated, or parsed in
an unintended location [MD053]. The most common cause in this format is writing
metadata as a definition above the registry:

```md
> [GL01]: TODO ""
```

That line is not harmless metadata. It is a reference definition inside a
blockquote. If the registry later defines `[GL01]` again, the linter may report
a duplicate definition. If the marker is not referenced, the linter may report
an unused definition. If casing differs, the labels can still collide because
Markdown reference labels are case-normalized [LN03].

Do not silence the linter. Repair the format.

## (8) Completion rules [VAL]

A completion pass must satisfy these rules:

1. Definitions live only in `(Z) Context-Citations` [LN01].
2. Body metadata references IDs but does not define IDs [LN02].
3. Marker labels are unique after case folding [LN03].
4. Every active registry entry is referenced at least once [LN04].
5. No active zero-number placeholder IDs remain [LN05].
6. Deprecated tags are explicit aliases [LN06].
7. Category labels remain stable and readable [LN07].
8. Invalid examples are fenced in code blocks [LN08].
9. Workflow sections carry goal, dependency, and requirement metadata [LN09].
10. External factual claims route through research-source records when they
    become design support [LN10].
11. Nested double quotes inside definition titles are avoided or rewritten
    [LN11].
12. `markdownlint-cli2` passes without changing project configuration [LN12].

## (9) Agent decision table [DT]

- Marker used in body but missing from registry: add a real registry entry
  or replace the marker with a valid existing one.
- Registry entry unused: reference it in the body, add it to the usage index,
  or remove it.
- Zero-number placeholder found: resolve it to a real numbered ID or remove
  the bracketed marker.
- Duplicate definition found: keep one source-of-truth entry and convert extras
  into references.
- Misspelled old tag found: replace it with the corrected tag or define the old
  tag as a deprecated alias.
- New research needed but no source exists: write a plain prose task note; do
  not create a numbered source ID.
- New concept introduced: choose an existing namespace or create a justified new
  namespace entry.
- MD053 appears: search for duplicate or unused reference definitions before
  editing config.
- User asks for format completion: complete IDs, definitions, usages, aliases,
  and the usage index first.
- User asks for project theory expansion: preserve [SA], [AS], [CW], [DN01],
  [TP], and [SP] semantics.

## (10) Anti-patterns [FAIL]

Do not do these:

```md
> [GL01]: TODO ""
> [DP00]: TODO ""
> [RQ00]: TODO ""
```

```md
[AS]: ALGORITHMIC_STEM "Uses smaller batch algorithm "stems" ..."
```

```md
[gl01]: SOME_OTHER_GOAL
  "Case changed to avoid duplicate."
```

```md
[RS00]: RESEARCH_SOURCE
  "TODO find paper later."
```

The first block creates illegal body definitions. The second block risks
breaking the quoted title with nested double quotes. The third block is still a
duplicate after case normalization. The fourth block creates a fake numbered
source before a source exists [FAIL].

## (11) Corrective patterns [FIX]

### Convert body definitions to references [FIX01]

Draft:

```md
> [GL04]: TODO ""
> [DP00]: TODO ""
> [RQ00]: TODO ""
```

Link-complete form:

```md
> Goal: [GL05] — THEORY_GENERATION_BATCH
> Dependency: [DP05] — CREATIVE_MATHEMATICAL_SPACE
> Requirement: [RQ06] — TECHNICAL_PLAUSIBILITY_FILTER
```

### Convert TODO IDs to real IDs [FIX02]

Draft:

```md
[DP01]: DEPENDENCY_ONE "[TODO]"
```

Link-complete form:

```md
[DP01]: CONTEXT_CITATION_REGISTRY
  "The registry must contain the full description for every active reusable
  marker used in the document."
```

### Convert old artifact names to aliases [FIX03]

Draft artifact:

```md
[PW01]: THEORIZE_BRAINSTORM
  "Old brainstorm marker."
```

Link-complete alias:

```md
[PW01]: DEPRECATED_ALIAS
  "Former artifact tag for THEORIZE_BRAINSTORM; preserve only as historical
  draft context and use WL01 as the active workflow ID."
```

### Preserve examples without creating definitions [FIX04]

Invalid syntax demonstrations must be fenced:

````md
```md
> [GL01]: TODO ""
```
````

Outside a fenced code block, the same line becomes active syntax and may trip
lint [EX].

## (12) New-document template [TPL]

Use this shape when creating a new project document that uses the format:

```md
# TITLE: DOCUMENT_NAME [DOC]

Intro text with compact references [FM], [PJ].

## (A) SECTION_NAME: [WL01]

> Goal: [GL01] — GOAL_NAME
> Dependency: [DP01] — DEPENDENCY_NAME
> Requirement: [RQ01] — REQUIREMENT_NAME

Body text using references [SA], [AS], [TP].

## (Y) LINK-COMPLETE USAGE INDEX: [LI]

- Core markers: [DOC], [FM], [PJ], [LI]
- Goal markers: [GL], [GL01]
- Dependency markers: [DP], [DP01]
- Requirement markers: [RQ], [RQ01]

## (Z) Context-Citations

[DOC]: DOCUMENT_NAME
  "Definition."

[FM]: FORMAT_MODEL
  "Definition."

[GL]: GOAL
  "Definition."

[GL01]: GOAL_NAME
  "Definition."
```

The template is illustrative. Do not copy the example IDs blindly into a real
file if those IDs already exist with different meanings [ID].

## (13) Validation workflow [VW]

Run validation in this order:

```sh
# 1. Check for illegal body definitions.
grep -nE '^>\s*\[[A-Za-z0-9]+\]:' file.md

# 2. Check for zero placeholders.
grep -nE '\[[A-Z]{1,6}00\]' file.md

# 3. Check all reference definitions.
grep -nE '^\[[A-Za-z0-9]+\]:' file.md

# 4. Run markdownlint without disabling rules.
markdownlint-cli2 file.md
```

If lint fails, fix the document, not the config [RQ04].

## (14) Agent output expectations [OUT]

When returning work to the user:

- Provide the completed or edited Markdown file.
- State whether markdownlint passed.
- State major repairs made, especially placeholder removal, alias creation,
  registry completion, and usage-index updates.
- Do not claim external factual support unless source records were actually
  added.
- Do not ask the user to confirm obvious placeholder completions when the
  document context gives enough information to infer a real ID [VAL].

## (15) Link-complete usage index [LI]

This section is intentionally non-authoritative. It references every active
onboarding marker so the registry definitions below are needed by the Markdown
reference system.

- Onboarding and context markers: [AO], [PJ], [CLI], [WH], [WH01], [WH02],
  [WH03], [WH04], [WH05]
- Format markers: [FM], [BD], [RG], [Z], [UI], [LI], [LC], [CE], [MR],
  [LM], [RSX], [EX], [SYX], [NS], [ID]
- Goal, dependency, and requirement markers: [GL], [GL01], [DP], [DP01],
  [RQ], [RQ03], [RQ04]
- Project markers: [SA], [SA01], [SA02], [SA03], [AS], [CW], [DN], [DN01],
  [TP], [SP], [WL], [TH], [RS], [EV], [SY], [IG], [IG01], [DS], [MO]
- Editing markers: [ED01], [ED02], [ED03], [ED04], [ED05], [VAL], [DT],
  [FAIL], [FIX], [FIX01], [FIX02], [FIX03], [FIX04], [TPL], [VW], [OUT]
- Lint markers: [MD], [MD053], [LN], [LN01], [LN02], [LN03], [LN04],
  [LN05], [LN06], [LN07], [LN08], [LN09], [LN10], [LN11], [LN12]

## (Z) Context-Citations

[AO]: AGENT_ONBOARDING
  "A machine-oriented onboarding document for local CLI agents first seeing
  the current pseudo-citation format."

[PJ]: PROJECT_CONTEXT
  "The 4GINE / SPINALTAP project family: a novel three-dimensional game engine
  theory organized through the SPINALTAP_ALGORITHM and related modular
  mathematical design patterns."

[CLI]: LOCAL_CLI_AGENT
  "A local coding or document-editing agent such as Codex, Claude Code, or a
  shell-based assistant operating on repository files."

[WH]: WHO_WHAT_WHERE_WHY_HOW
  "The contextual bootstrap needed by an agent with no prior project memory."

[WH01]: WHO_CONTEXT
  "The agent audience, user role, and expectation that no hidden project
  context is assumed."

[WH02]: WHAT_CONTEXT
  "The definition of the pseudo-citation format as compact marker references
  connected to complete bottom-registry entries."

[WH03]: WHERE_CONTEXT
  "The placement rule: references live throughout the body, while definitions
  live in the bottom Context-Citations registry."

[WH04]: WHY_CONTEXT
  "The purpose of the format: compact traceability, reusable context, and
  lint-compatible pseudo-sourcing without project config changes."

[WH05]: HOW_CONTEXT
  "The operating method: reference above, define once below, index active
  markers, and keep markdownlint clean."

[FM]: FORMAT_MODEL
  "The document-format model that joins compact inline markers, local metadata,
  usage indexes, and bottom-registry entries into a traceable pseudo-source
  system."

[BD]: BODY_LAYER
  "The upper document layer that acts as a contextual knowledge map and uses
  pseudo-citation markers without defining them."

[RG]: REGISTRY_LAYER
  "The bottom source-of-truth layer where each active marker is defined exactly
  once."

[Z]: CONTEXT_CITATIONS
  "The bottom registry that houses the complete source-of-truth definitions for
  all active pseudo-citation markers used in the document."

[UI]: USAGE_INDEX
  "A non-authoritative section that invokes every active marker at least once
  so registry entries remain needed under markdownlint."

[LI]: LINK_INDEX
  "A marker family for usage-index sections that anchor active definitions
  without becoming source-of-truth definitions themselves."

[LC]: LINK_COMPLETE_STATE
  "A completed state where every active marker is defined once, referenced at
  least once, free from zero placeholders, and lint-clean."

[CE]: CITATION_ENTRY
  "A single pseudo-citation object consisting of a marker label, compact
  category destination, and complete quoted context definition."

[MR]: MARKER_REFERENCE
  "A body-level invocation of a pseudo-citation marker, usually written as a
  shortcut reference such as [GL01] or [SA]."

[LM]: LOCAL_METADATA
  "Section-level metadata that references goal, dependency, requirement, or
  workflow markers without using bracket-colon definition syntax."

[RSX]: REGISTRY_SYNTAX
  "The live reference-definition syntax reserved for Context-Citations entries
  in the bottom registry."

[EX]: FENCED_EXAMPLE
  "A fenced code block used to show draft, invalid, or illustrative syntax
  without causing Markdown to parse it as live references or definitions."

[SYX]: REQUIRED_SYNTAX
  "The required syntax model for marker references, local metadata, registry
  definitions, and code examples."

[NS]: NAMESPACE_MODEL
  "The rule set for assigning stable marker families such as goals,
  dependencies, requirements, theories, styles, and modules."

[ID]: NUMBERED_IDENTIFIER
  "A stable marker label in a namespace family, where the family marker defines
  the class and numbered IDs define individual concepts."

[GL]: GOAL
  "The intended outcome of a correlated section, subsection, task, request,
  theory object, or validation pass."

[GL01]: ONBOARD_FRESH_AGENT
  "Give a fresh local CLI agent enough context to preserve and extend the
  pseudo-citation system without prior project memory."

[DP]: DEPENDENCY
  "A component, task, prerequisite, input, or contextual support object that
  must exist before a requirement can be satisfied."

[DP01]: MARKDOWN_REFERENCE_PARSER
  "The format depends on Markdown reference-link parsing, so reference labels,
  definitions, duplicates, and unused entries must be handled deliberately."

[RQ]: REQUIREMENT
  "A necessary condition, object, rule, output, or acceptance criterion
  required to achieve or build the correlated goal."

[RQ03]: NO_PLACEHOLDER_IDS
  "Completed passes must not leave active bracketed zero-number placeholder IDs
  such as GL00, DP00, RQ00, or RS00."

[RQ04]: LINT_CLEAN_WITHOUT_CONFIG_CHANGES
  "The document must pass markdownlint by repairing syntax rather than changing
  or silencing project lint configuration."

[SA]: SPINALTAP_ALGORITHM
  "A modular algorithm family organized through a nervous-system-inspired
  framework for a mathematical three-dimensional game engine."

[SA01]: nervous_system
  "Broad but bounded algorithm families that each own a scoped area of the
  engine ecosystem."

[SA02]: vertebrae
  "Smaller local solvers, transform units, or scoped formulations operating on
  defined data targets."

[SA03]: spinal_column
  "The aggregation, routing, and reconciliation layer that orders module
  relationships and produces higher-order engine state."

[AS]: ALGORITHMIC_STEM
  "A modular operation model where scoped algorithmic stems solve assigned jobs
  and pass bounded results to parent stems."

[CW]: CONTEXT_WEIGHT
  "The allowed influence weight of discovered data, source material, research,
  or prior theory on the current output."

[DN]: DO_NOT
  "A negative constraint used to remove, ignore, limit, or release an item from
  contextual relevance."

[DN01]: DATA_REPLICATION
  "Do not over-weight established theories so heavily that the result becomes a
  lightly modified replica of the original."

[TP]: TECHNICALLY_PLAUSIBLE
  "A creative theory standard that permits novelty while rejecting incoherent,
  unbounded, or non-actionable speculation."

[SP]: SOFT_PROVEN
  "A research-supported plausibility standard based on coherent mathematics,
  explicit assumptions, comparison, and critical adjustment."

[WL]: WORKFLOW
  "Ordered roadmap from theory generation to research, proposal, docspec, and
  sourcecode development."

[TH]: THEORY_CANDIDATE
  "A brainstormed or research-adjusted theoretical object that may become part
  of the SPINALTAP_ALGORITHM engine model."

[RS]: RESEARCH_SOURCE
  "External source entry such as a paper, book, documentation page, talk, or
  implementation note with context-weight metadata."

[EV]: EVIDENCE_LEVEL
  "Evidence-strength label used to show how much support a claim has before it
  is promoted in the workflow."

[SY]: STYLE
  "Formal video-game design or rendering style marker framed around platform
  capability, rendering behavior, or presentation constraint."

[IG]: IGNORE
  "Contextual ignore marker used to remove a style, concept, source, or
  direction from active design relevance."

[IG01]: STYLE_EXCLUSION_PIXEL_ART
  "Ignore traditional pixel_art as an engine-level or core-design solution for
  this document family unless the ignore rule is explicitly revised."

[DS]: DESIGN_OBJECT
  "Design-level object used by the proposal and docspec to turn theory into
  scoped architecture and acceptance criteria."

[MO]: MODULE_OBJECT
  "Implementation-facing module marker that maps the conceptual algorithm model
  onto sourcecode and documentation structure."

[ED01]: PRE_EDIT_SCAN
  "Before editing, locate the registry, build maps of definitions and marker
  references, identify duplicates, and inspect unresolved placeholders."

[ED02]: ADD_SECTION_PROTOCOL
  "When adding a substantial section, include goal, dependency, and requirement
  metadata that references existing or newly defined IDs."

[ED03]: PLACEHOLDER_RESOLUTION_PROTOCOL
  "When resolving draft placeholders, replace them with real IDs, reuse valid
  existing IDs, remove them, or convert unresolved intent to plain prose."

[ED04]: TAG_RENAME_PROTOCOL
  "When correcting renamed or misspelled tags, use the active corrected tag and
  preserve old tags only as explicit deprecated aliases when needed."

[ED05]: RESEARCH_ENTRY_PROTOCOL
  "When adding external research, create numbered source entries only after real
  sources exist and assign explicit context weight."

[VAL]: COMPLETION_RULES
  "The validation rules that determine whether a document has been completed in
  the pseudo-citation format."

[DT]: AGENT_DECISION_TABLE
  "A compact mapping from common document states to the required agent repair
  action."

[FAIL]: ANTI_PATTERNS
  "Common malformed patterns that break the pseudo-citation system or trigger
  markdownlint errors."

[FIX]: CORRECTIVE_PATTERNS
  "Preferred repairs for body definitions, TODO IDs, deprecated aliases, and
  fenced examples."

[FIX01]: BODY_DEFINITION_TO_REFERENCE
  "The repair that converts illegal body bracket-colon definitions into local
  metadata references."

[FIX02]: TODO_ID_TO_REAL_ID
  "The repair that replaces placeholder or TODO registry entries with real
  category labels and contextual definitions."

[FIX03]: OLD_TAG_TO_ALIAS
  "The repair that converts a renamed draft marker into an explicit deprecated
  alias instead of a silent duplicate."

[FIX04]: FENCE_INVALID_EXAMPLES
  "The repair that places invalid or illustrative syntax inside fenced code
  blocks so it is not parsed as live Markdown syntax."

[TPL]: NEW_DOCUMENT_TEMPLATE
  "A starter shape for creating a new Markdown file that follows the current
  pseudo-citation format."

[VW]: VALIDATION_WORKFLOW
  "The shell-oriented scan and markdownlint sequence used to confirm the file
  is link-complete."

[OUT]: AGENT_OUTPUT_EXPECTATIONS
  "The expected final response behavior after a CLI agent edits or creates a
  pseudo-citation document."

[MD]: MARKDOWNLINT_COMPATIBILITY
  "The requirement that the pseudo-citation system work with standard
  markdownlint behavior instead of depending on disabled rules."

[MD053]: MD053_REFERENCE_DEFINITION_FAILURE
  "A markdownlint reference-definition failure commonly caused by duplicate,
  unused, or accidentally parsed reference definitions."

[LN]: LINT_RULE
  "A pseudo-citation validation rule used to keep marker definitions,
  references, aliases, and lint behavior consistent."

[LN01]: REGISTRY_ONLY_DEFINITIONS
  "Only the bottom Context-Citations registry should use live bracket-colon
  reference-definition syntax for active markers."

[LN02]: BODY_REFERENCES_ONLY
  "The upper document may reference markers, but it must not define those
  markers."

[LN03]: CASE_NORMALIZED_UNIQUENESS
  "Marker labels must be unique after case folding because Markdown reference
  labels are matched by normalized form."

[LN04]: USAGE_INDEX_REQUIRED_WHEN_NEEDED
  "Use a non-authoritative usage index when active registry definitions need a
  visible reference to remain lint-clean."

[LN05]: ZERO_PLACEHOLDER_BAN
  "Do not leave active zero-number placeholder IDs in completed document
  passes."

[LN06]: EXPLICIT_DEPRECATED_ALIAS
  "Deprecated or renamed IDs must be declared as aliases instead of silently
  reusing the old meaning."

[LN07]: STABLE_CATEGORY_LABELS
  "Category destination labels should remain short, stable, readable, and
  mostly uppercase snake case."

[LN08]: FENCE_INVALID_SYNTAX
  "Invalid syntax demonstrations must be fenced so Markdown does not parse them
  as real references or definitions."

[LN09]: WORKFLOW_METADATA_COMPLETENESS
  "Substantial workflow sections should include goal, dependency, and
  requirement metadata."

[LN10]: EXTERNAL_CLAIM_LINKAGE
  "External factual or research claims should connect to a research-source
  record before they become design support."

[LN11]: SAFE_QUOTATION_RULE
  "Registry definitions should avoid unsafe nested double quotes and prefer
  apostrophes or rewrites inside title text."

[LN12]: MARKDOWNLINT_PASS_REQUIRED
  "The final file should pass markdownlint without suppressing MD053 or
  changing project configuration."
