# (A) 4GINE: SPINALTAP MULTI-MODULAR ALGORITHMIC ENGINE

- A novel, research-guided 3D game-engine design intended to be mathematically organized through the SPINALTAP_ALGORITHM [SA] and its multi-modular ALGORITHMIC_STEM structure [AS].
- The upper document operates as a contextual knowledge map. It uses compact pseudo-citation markers to connect local claims, goals, requirements, dependencies, workflow steps, style constraints, and theory objects to the larger definitions in the [Z] Context-Citations registry.
- The [Z] Context-Citations registry is the source-of-truth area. Each active marker used in the document must resolve to one complete definition in [Z].

---

## (1.A) DOCUMENT FORMAT ONBOARDING: [FM]

> [GL01]: FORMAT_ONBOARDING "Define how the note uses compact contextual pseudo-citations, section metadata, and a bottom registry so the document can grow without losing traceability."
> [DP01]: CONTEXT_CITATION_REGISTRY "The [Z] registry must contain the full description for every active reusable marker used in the document."
> [RQ01]: FORMAT_INTEGRITY "Every active inline marker must either resolve to one complete [Z] definition or be explicitly marked as a reserved draft slot."

---

### (1.A.1) Pseudo-Citation Grammar

The document uses one grammar in two locations:

```md
[ID]: CATEGORY "Full contextual definition"
```

Section-level metadata uses the same syntax inside blockquotes:

```md
> [GL01]: FORMAT_ONBOARDING "Goal for this section."
> [DP01]: CONTEXT_CITATION_REGISTRY "Dependency required by this section."
> [RQ01]: FORMAT_INTEGRITY "Requirement enforced by this section."
```

Inline references use the compact marker only:

```md
The engine model is organized through SPINALTAP_ALGORITHM [SA] and ALGORITHMIC_STEM [AS].
```

The marker points downward into [Z], where the complete definition lives. The body stays compact. The registry carries the contextual weight.

### (1.A.2) Reserved Draft Slots

[DP00] and [RQ00] are reserved draft-only placeholders. They are not failures, missing IDs, or final definitions. They mean: this section needs a dependency or requirement, but that object has not been created yet. Once the section is completed, [DP00] and [RQ00] should be replaced with a real numbered ID such as [DP05] or [RQ06].

---

## (2.A) GUARDRAILS: [GR]

> [GL02]: GUARDRAIL_ALIGNMENT "Keep the document novel, mathematically creative, research-aware, and internally traceable without letting source material overwrite the original SPINALTAP_ALGORITHM design."
> [DP02]: NOVELTY_CONTROL "The document depends on CONTEXT_WEIGHT [CW] and DO_NOT [DN] rules to prevent research material from becoming accidental replication."
> [RQ02]: NON_REPLICATION_REQUIREMENT "Research must inform the theory without recreating, lightly renaming, or over-weighting existing theories."
> [RQ03]: EVIDENCE_STANDARD "Critical theory claims must be promoted from TECHNICALLY_PLAUSIBLE [TP] toward SOFT_PROVEN [SP] through research, comparison, adjustment, and documented reasoning."

---

> [IG01]: STYLE "pixel_art"

```json
{
  "ignore": [
    "[IG01]: pixel_art"
  ],
  "reserved_draft_slots": [
    "[DP00]",
    "[RQ00]"
  ],
  "normalization": {
    "SPINAL_TAP": "SPINALTAP_ALGORITHM",
    "THEORIZE_BRAINSTOM": "THEORIZE_BRAINSTORM",
    "MULTI-MODDULATED": "MULTI-MODULATED",
    "PW01": "deprecated alias of WL01"
  }
}
```

Pixel art is excluded as an engine or core-design style target through [IG01]. This does not prevent future asset-level experiments, but it prevents the engine concept from drifting into a traditional 2D pixel-art framing when the active target is 3D style language [SY].

---

## (B) MULTI-MODULATED ALGORITHMIC MATHEMATICAL 3D ENGINE MODEL

### (1.B) CORE_THEORY: [CT]

> [GL03]: CORE_THEORY_LARGE_BATCH "Generate a large batch of technically plausible mathematical theory candidates that can support or refine the SPINALTAP_ALGORITHM engine model."
> [DP03]: SPINALTAP_FRAMEWORK "The model depends on a three-layer algorithmic structure: nervous_system [SA01], vertebrae [SA02], and spinal_column [SA03]."
> [RQ04]: MODULAR_ALGORITHM_CHAIN "The core theory must remain expressible as [SA] = [SA01] -> [SA02] -> [SA03]."

---

4GINE is designed as a capable 3D game engine whose architecture is organized by SPINALTAP_ALGORITHM [SA]. The core metaphor is not decorative; it is the structural map for algorithm ownership, data movement, and modular responsibility.

The simplified algorithmic chain is:

```md
[SA] = [SA01] -> [SA02] -> [SA03]
```

- nervous_system [SA01] represents large but bounded algorithm families. These are broad engine domains with distinct responsibilities.
- vertebrae [SA02] represents smaller scoped formulas, local solvers, routing units, or transform rules that operate inside or between those broader domains.
- spinal_column [SA03] represents the aggregating layer that receives, orders, reconciles, and forwards the outputs of the vertebrae and nervous-system modules.

The ALGORITHMIC_STEM model [AS] keeps each local formula scoped. A stem can formulate, transform, score, route, or reconcile data, but it should not own the entire engine. Parent stems ingest child-stem outputs and produce a higher-order state. This allows the system to remain modular without collapsing into disconnected micro-systems.

Conceptual schema:

```md
SPINALTAP_ENGINE_STATE(t + 1)
  = spinal_column(
      nervous_system_batch(
        vertebrae_formulas(input, state(t), constraints, context_weight)
      )
    )
```

The schema is a design scaffold, not a final mathematical proof. It defines how theory candidates should be shaped before entering research and soft-proof validation [TP], [SP].

---

### (2.B) WORKFLOW: [WL]

> [GL04]: WORKFLOW_ROADMAP "Move from open theory generation to research-supported theory, then into proposal, docspec, and sourcecode development."
> [DP04]: WORKFLOW_SEQUENCE "Each workflow stage depends on the prior stage producing enough context to advance without destroying traceability."
> [RQ05]: ORDERED_WORKFLOW "The workflow must preserve the sequence [WL01] -> [WL02] -> [WL03] -> [WL04] -> [WL05]."

---

> [WL01]: THEORIZE_BRAINSTORM "First and loosest guardrail stage. Generate the largest useful batch of theories, then trim toward the exact theory framework that will support SPINALTAP_ALGORITHM [TP]."
> [WL02]: RESEARCH "Second stage. Apply stricter standards, compare against external research, extract strengths and failures, and promote only what survives SOFT_PROVEN review [SP]."
> [WL03]: PROPOSAL "Third stage. Convert the strongest research-adjusted theory into a specific engine proposal with scope, risks, modules, and acceptance criteria."
> [WL04]: DEVELOPMENT_DOCSPEC "Fourth stage. Create the development document specification: requirements.md, design.md, and tasklist.md."
> [WL05]: DEVELOPMENT_SOURCECODE "Fifth stage. Use the research, proposal, requirements, design, and tasklist to begin sourcecode development."

---

## (C) THEORIZE_BRAINSTORM: [WL01]

> [GL05]: THEORY_GENERATION_BATCH "Create broad but usable mathematical theory candidates that may support the SPINALTAP_ALGORITHM model."
> [DP05]: CREATIVE_MATHEMATICAL_SPACE "The brainstorm depends on technical imagination, loose early constraints, and strong anti-replication control [DN01]."
> [RQ06]: TECHNICAL_PLAUSIBILITY_FILTER "Every candidate must remain technically plausible enough to be researched, formalized, or rejected without becoming incoherent speculation [TP]."

---

The brainstorm stage deliberately starts wide. Its job is not to prove the final engine. Its job is to create a large enough theory surface that useful structures can be discovered, compared, cut, and refined.

### (C.1) Candidate Theory Batch

1. **Signal-Routing Spine** [TH01] — A spinal-column routing model where independent module outputs are converted into typed state signals before being aggregated by [SA03].
2. **Vertebrae Local Solvers** [TH02] — A local-formula model where small scoped solvers [SA02] handle specific transformations, collisions, style constraints, animation transitions, or state corrections.
3. **Context-Weight Governor** [TH03] — A research-weighting model that controls how much outside theory can influence the internal theory before it becomes derivative [CW], [DN01].
4. **Style-Constraint Layer** [TH04] — A style-facing model that treats visual style as a bounded constraint surface rather than a loose aesthetic afterthought [SY].
5. **Soft-Proof Pipeline** [TH05] — A promotion model that moves a candidate from imagination to technical plausibility [TP], then to research-supported plausibility [SP].

### (C.2) Brainstorm Acceptance Filter

A brainstormed theory remains active only if it can satisfy all of the following:

- It can be expressed through the SPINALTAP_ALGORITHM structure [SA].
- It can be decomposed into bounded ALGORITHMIC_STEM units [AS].
- It can eventually become a requirement, dependency, or task without losing its meaning [RQ], [DP].
- It avoids excessive replication of established theories [DN01].
- It can be researched without requiring immediate live engine testing [SP].

---

## (D) RESEARCH: [WL02]

> [GL06]: RESEARCH_SUPPORT "Use external research to challenge, strengthen, narrow, and correct the best brainstormed theory candidates."
> [DP06]: RESEARCH_COLLECTION "Research requires source gathering, comparison, extraction of useful constraints, and explicit context-weight assignment [CW]."
> [RQ07]: SOFT_PROVEN_STANDARD "A theory can be marked SOFT_PROVEN only when its logic is technically plausible, research-adjusted, internally consistent, and ready for proposal without claiming final empirical proof [SP]."

---

Research is not used as a copy source. It is used as pressure. The task is to find what existing work proves, where it fails, why it fails, and what constraints should be inherited or avoided.

### (D.1) Research Procedure

1. Identify the exact theory claim being tested, such as routing, aggregation, local solver stability, visual style constraint, or engine-state composition.
2. Collect relevant papers, books, documentation, talks, or implementation notes and assign them research-source records [RS].
3. Extract strengths, shortcomings, assumptions, and failure modes.
4. Assign CONTEXT_WEIGHT [CW] to each source before using it in the theory.
5. Rewrite the internal theory in SPINALTAP_ALGORITHM terms [SA] instead of reproducing source terminology or structure [DN01].
6. Promote only the adjusted portion that survives TECHNICALLY_PLAUSIBLE [TP] and SOFT_PROVEN [SP] standards.

### (D.2) Research Source Record Template

```md
[RS##]: RESEARCH_SOURCE "TITLE: ... | SOURCE: ... | YEAR: ... | LINK_OR_DOI: ... | USED_FOR: ... | CONTEXT_WEIGHT: LOW/MEDIUM/HIGH | LINKED_CONTEXT: [SA], [AS], [TH##], [RQ##]"
```

[RS00] is reserved as an open source slot. It should only be used while a real source entry is being created. Once the source is known, it should be promoted to a real numbered source ID.

### (D.3) STYLE EXAMPLES: [SY]

> [GL07]: STYLE_TAXONOMY "Use formal style language for 3D game aesthetics from approximately 1995-2005 without drifting into ignored pixel-art framing [IG01]."
> [DP07]: FORMAL_STYLE_LANGUAGE "The style section depends on named 3D rendering and presentation categories that can be used as constraints during research, proposal, and implementation."
> [RQ08]: STYLE_EXCLUSION_REQUIREMENT "Traditional pixel_art must remain excluded as an engine or core-design solution unless the ignore rule [IG01] is explicitly revised."

---

1. **Low-poly 3D** [SY01] — broad reduced-polygon modeling style.
2. **Texture-mapped low-poly 3D** [SY02] — low-poly geometry with image textures as the primary surface-detail method.
3. **Affine-textured 3D** [SY03] — perspective-imperfect texture mapping associated with warped retro 3D texture behavior.
4. **Dithered 3D** [SY04] — limited-color or noise-patterned visual treatment used to imply gradients, shading, or transitional color.
5. **Vertex-lit 3D** [SY05] — lighting calculated at vertices and interpolated across faces.
6. **Gouraud-shaded 3D** [SY06] — smooth-shaded polygonal lighting using interpolated vertex colors or lighting values.
7. **Flat-shaded 3D** [SY07] — visible hard polygon facets, often with minimal or no texture detail.
8. **Billboarded 3D** [SY08] — 2D planes or sprites oriented within a 3D scene.
9. **Pre-rendered 3D** [SY09] — offline-rendered backgrounds, sprites, or assets placed inside a real-time presentation.
10. **Fixed-function 3D** [SY10] — pre-modern-shader rendering language associated with limited programmable graphics behavior.
11. **Cel-shaded / toon-shaded 3D** [SY11] — cartoon-like rendering through simplified lighting, outlines, ramps, or stylized shading.
12. **Arcade 3D** [SY12] — clean, bright, high-readability 3D presentation associated with arcade-era real-time 3D aesthetics.
13. **Early real-time CGI** [SY13] — glossy, toy-like, early-2000s presentation that imitates offline CGI within real-time limits.
14. **Sixth-generation 3D** [SY14] — PS2/GameCube/Dreamcast/Xbox-era 3D presentation language.
15. **Retro 3D** [SY15] — umbrella term for modern recreation, remixing, or controlled imitation of older real-time 3D styles.

---

## (E) PROPOSAL: [WL03]

> [GL08]: PROPOSAL_FORMATION "Convert research-adjusted theory into a specific engine proposal that can be turned into requirements, design, and tasks."
> [DP08]: PROPOSAL_INPUTS "The proposal depends on active theory candidates [TH], research-source records [RS], context weighting [CW], and guardrails [GR]."
> [RQ09]: PROPOSAL_READINESS "A proposal must identify selected theories, rejected theories, dependencies, requirements, risks, source influence, and implementation boundaries."

---

The proposal is the first stage where the document stops expanding theory and begins selecting a buildable direction.

A proposal entry should include:

- selected SPINALTAP_ALGORITHM interpretation [SA];
- active theory candidates [TH];
- accepted and rejected research influences [RS], [CW];
- engine modules implied by the ALGORITHMIC_STEM model [AS];
- requirements and dependencies [RQ], [DP];
- style target and exclusions [SY], [IG];
- risks created by novelty, scope, implementation difficulty, or weak evidence [DN].

A theory is ready for proposal only when it is narrow enough to build, broad enough to matter, and documented enough to explain.

---

## (F) DEVELOPMENT_DOCSPEC: [WL04]

> [GL09]: DEVELOPMENT_DOCSPEC "Create the document package that turns the proposal into implementation-ready development artifacts."
> [DP09]: DOCUMENTATION_PACKAGE "The docspec depends on the proposal output, numbered requirements, numbered dependencies, and traceable design claims."
> [RQ10]: DOCSPEC_TRACEABILITY "requirements.md, design.md, and tasklist.md must preserve traceability back to [Z] definitions and active workflow IDs."

---

### (F.1) requirements.md

requirements.md should contain the numbered build requirements. Each requirement must connect to:

- one or more goals [GL];
- one or more dependencies [DP];
- one or more workflow stages [WL];
- one source-of-truth definition in [Z].

### (F.2) design.md

design.md should explain how the system works. It should map:

- SPINALTAP_ALGORITHM [SA];
- nervous_system modules [SA01];
- vertebrae local solvers [SA02];
- spinal_column aggregation [SA03];
- ALGORITHMIC_STEM routing and ownership [AS];
- style constraints [SY];
- research-adjusted decisions [RS], [CW].

### (F.3) tasklist.md

tasklist.md should convert requirements and design sections into implementation tasks. No task should exist without a parent requirement [RQ]. No requirement should exist without a dependency [DP] or an explicit explanation for why it is dependency-free.

---

## (G) DEVELOPMENT_SOURCECODE: [WL05]

> [GL10]: DEVELOPMENT_SOURCECODE "Begin sourcecode development only after the conceptual theory, research pass, proposal, and docspec have created enough traceable structure."
> [DP10]: CODE_ARCHITECTURE_SCAFFOLD "Sourcecode depends on the docspec and should mirror the SPINALTAP_ALGORITHM structure rather than becoming a generic engine layout."
> [RQ11]: SOURCE_TRACEABILITY "Every major source module should trace back to an active requirement, dependency, workflow stage, and source-of-truth context entry."

---

Sourcecode should begin as a traceable scaffold, not a detached implementation.

Suggested initial structure:

```txt
/engine
  /spinal_column
    aggregator.*
    router.*
    reconciler.*
  /nervous_system
    rendering.*
    simulation.*
    scene_state.*
    style_constraints.*
  /vertebrae
    local_solver.*
    transform_unit.*
    collision_unit.*
    signal_unit.*
  /docs
    requirements.md
    design.md
    tasklist.md
```

The source tree should preserve the conceptual chain [SA01] -> [SA02] -> [SA03]. Implementation can later replace these placeholder module names, but the first scaffold should make the architecture legible.

---

## (H) PSEUDO-CITATION LINT RULES: [LN]

> [GL11]: LINT_VALIDATION "Keep the pseudo-citation system internally consistent as the document grows."
> [DP11]: CITATION_LINTER "The document depends on a repeatable lint pattern that catches unresolved IDs, duplicate IDs, broken aliases, placeholder leakage, and unsafe syntax."
> [RQ12]: LINT_COMPLIANCE "Before a section is treated as complete, it must satisfy the active lint rules [LN]."

---

Applied normalization rules:

1. [LN01] Every active marker should have exactly one source-of-truth definition in [Z].
2. [LN02] Blockquote metadata should use the same syntax as registry entries.
3. [LN03] [DP00], [RQ00], and [RS00] are reserved draft slots, not final objects.
4. [LN04] Deprecated or renamed IDs must be declared as aliases rather than silently reused.
5. [LN05] Definitions should avoid unescaped nested double quotes; use apostrophes inside the definition string when needed.
6. [LN06] External factual or research claims should be linked through research-source records [RS].
7. [LN07] Category labels should use stable uppercase snake-case names.
8. [LN08] No workflow stage should advance unless its goal, dependency, and requirement metadata are present.
9. [PW01] is retained only as a deprecated alias for [WL01], because the original draft used both naming schemes for the same workflow concept.

---

## (Z) Context-Citations

[Z]: CONTEXT_CITATIONS "The bottom registry that houses the complete source-of-truth definitions for all active pseudo-citation markers used in the document."

[FM]: FORMAT_MODEL "The document-format model that defines how compact inline markers, section metadata, and source-of-truth registry entries work together."
[GR]: GUARDRAILS "The safety, novelty, research, and formatting constraints that prevent the document from drifting away from its intended design."
[LN]: LINT_RULES "The validation rules used to keep the pseudo-citation system consistent, traceable, and readable."

[GL]: GOAL "The intended outcome of a correlated section, subsection, task, request, or theory object."
[GL01]: FORMAT_ONBOARDING "Define how the note uses compact contextual pseudo-citations, section metadata, and a bottom registry so the document can grow without losing traceability."
[GL02]: GUARDRAIL_ALIGNMENT "Keep the document novel, mathematically creative, research-aware, and internally traceable without letting source material overwrite the original SPINALTAP_ALGORITHM design."
[GL03]: CORE_THEORY_LARGE_BATCH "Generate a large batch of technically plausible mathematical theory candidates that can support or refine the SPINALTAP_ALGORITHM engine model."
[GL04]: WORKFLOW_ROADMAP "Move from open theory generation to research-supported theory, then into proposal, docspec, and sourcecode development."
[GL05]: THEORY_GENERATION_BATCH "Create broad but usable mathematical theory candidates that may support the SPINALTAP_ALGORITHM model."
[GL06]: RESEARCH_SUPPORT "Use external research to challenge, strengthen, narrow, and correct the best brainstormed theory candidates."
[GL07]: STYLE_TAXONOMY "Use formal style language for 3D game aesthetics from approximately 1995-2005 without drifting into ignored pixel-art framing [IG01]."
[GL08]: PROPOSAL_FORMATION "Convert research-adjusted theory into a specific engine proposal that can be turned into requirements, design, and tasks."
[GL09]: DEVELOPMENT_DOCSPEC "Create the document package that turns the proposal into implementation-ready development artifacts."
[GL10]: DEVELOPMENT_SOURCECODE "Begin sourcecode development only after the conceptual theory, research pass, proposal, and docspec have created enough traceable structure."
[GL11]: LINT_VALIDATION "Keep the pseudo-citation system internally consistent as the document grows."

[DP]: DEPENDENCY "A component, task, prerequisite, input, or contextual support object that must exist before a requirement can be satisfied."
[DP00]: OPEN_DEPENDENCY_SLOT "Reserved draft-only dependency placeholder. Use when a section clearly needs a dependency but the actual dependency has not been created yet. Replace with a real numbered dependency before finalizing the section."
[DP01]: CONTEXT_CITATION_REGISTRY "The [Z] registry must contain the full description for every active reusable marker used in the document."
[DP02]: NOVELTY_CONTROL "The document depends on CONTEXT_WEIGHT [CW] and DO_NOT [DN] rules to prevent research material from becoming accidental replication."
[DP03]: SPINALTAP_FRAMEWORK "The model depends on a three-layer algorithmic structure: nervous_system [SA01], vertebrae [SA02], and spinal_column [SA03]."
[DP04]: WORKFLOW_SEQUENCE "Each workflow stage depends on the prior stage producing enough context to advance without destroying traceability."
[DP05]: CREATIVE_MATHEMATICAL_SPACE "The brainstorm depends on technical imagination, loose early constraints, and strong anti-replication control [DN01]."
[DP06]: RESEARCH_COLLECTION "Research requires source gathering, comparison, extraction of useful constraints, and explicit context-weight assignment [CW]."
[DP07]: FORMAL_STYLE_LANGUAGE "The style section depends on named 3D rendering and presentation categories that can be used as constraints during research, proposal, and implementation."
[DP08]: PROPOSAL_INPUTS "The proposal depends on active theory candidates [TH], research-source records [RS], context weighting [CW], and guardrails [GR]."
[DP09]: DOCUMENTATION_PACKAGE "The docspec depends on the proposal output, numbered requirements, numbered dependencies, and traceable design claims."
[DP10]: CODE_ARCHITECTURE_SCAFFOLD "Sourcecode depends on the docspec and should mirror the SPINALTAP_ALGORITHM structure rather than becoming a generic engine layout."
[DP11]: CITATION_LINTER "The document depends on a repeatable lint pattern that catches unresolved IDs, duplicate IDs, broken aliases, placeholder leakage, and unsafe syntax."

[RQ]: REQUIREMENT "A necessary condition, object, rule, output, or acceptance criterion required to achieve or build the correlated goal."
[RQ00]: OPEN_REQUIREMENT_SLOT "Reserved draft-only requirement placeholder. Use when a section clearly needs a requirement but the actual requirement has not been created yet. Replace with a real numbered requirement before finalizing the section."
[RQ01]: FORMAT_INTEGRITY "Every active inline marker must either resolve to one complete [Z] definition or be explicitly marked as a reserved draft slot."
[RQ02]: NON_REPLICATION_REQUIREMENT "Research must inform the theory without recreating, lightly renaming, or over-weighting existing theories."
[RQ03]: EVIDENCE_STANDARD "Critical theory claims must be promoted from TECHNICALLY_PLAUSIBLE [TP] toward SOFT_PROVEN [SP] through research, comparison, adjustment, and documented reasoning."
[RQ04]: MODULAR_ALGORITHM_CHAIN "The core theory must remain expressible as [SA] = [SA01] -> [SA02] -> [SA03]."
[RQ05]: ORDERED_WORKFLOW "The workflow must preserve the sequence [WL01] -> [WL02] -> [WL03] -> [WL04] -> [WL05]."
[RQ06]: TECHNICAL_PLAUSIBILITY_FILTER "Every candidate must remain technically plausible enough to be researched, formalized, or rejected without becoming incoherent speculation [TP]."
[RQ07]: SOFT_PROVEN_STANDARD "A theory can be marked SOFT_PROVEN only when its logic is technically plausible, research-adjusted, internally consistent, and ready for proposal without claiming final empirical proof [SP]."
[RQ08]: STYLE_EXCLUSION_REQUIREMENT "Traditional pixel_art must remain excluded as an engine or core-design solution unless the ignore rule [IG01] is explicitly revised."
[RQ09]: PROPOSAL_READINESS "A proposal must identify selected theories, rejected theories, dependencies, requirements, risks, source influence, and implementation boundaries."
[RQ10]: DOCSPEC_TRACEABILITY "requirements.md, design.md, and tasklist.md must preserve traceability back to [Z] definitions and active workflow IDs."
[RQ11]: SOURCE_TRACEABILITY "Every major source module should trace back to an active requirement, dependency, workflow stage, and source-of-truth context entry."
[RQ12]: LINT_COMPLIANCE "Before a section is treated as complete, it must satisfy the active lint rules [LN]."

[CT]: CORE_THEORY "The fundamental idea or framework describing how the theory operates, what problem it solves, and how the algorithmic engine model is organized."
[TP]: TECHNICALLY_PLAUSIBLE "A creative theory standard that permits novelty and exploratory mathematical structure while rejecting incoherent, unbounded, or non-actionable speculation."
[SP]: SOFT_PROVEN "A research-supported plausibility standard. A theory is soft-proven when it has coherent mathematics, explicit assumptions, research comparison, critical adjustment, and enough internal consistency to proceed without live engine test data."

[WL]: WORKFLOW "The ordered roadmap of the project from theory generation to research, proposal, docspec, and sourcecode development."
[WL01]: THEORIZE_BRAINSTORM "First and loosest guardrail stage. Generate the largest useful batch of theories, then trim toward the exact theory framework that will support SPINALTAP_ALGORITHM [TP]."
[WL02]: RESEARCH "Second stage. Apply stricter standards, compare against external research, extract strengths and failures, and promote only what survives SOFT_PROVEN review [SP]."
[WL03]: PROPOSAL "Third stage. Convert the strongest research-adjusted theory into a specific engine proposal with scope, risks, modules, and acceptance criteria."
[WL04]: DEVELOPMENT_DOCSPEC "Fourth stage. Create the development document specification: requirements.md, design.md, and tasklist.md."
[WL05]: DEVELOPMENT_SOURCECODE "Fifth stage. Use the research, proposal, requirements, design, and tasklist to begin sourcecode development."
[PW01]: DEPRECATED_ALIAS "Former artifact tag for THEORIZE_BRAINSTORM. Use [WL01] as the active workflow ID unless preserving historical draft context."

[TH]: THEORY_CANDIDATE "A brainstormed or research-adjusted theoretical object that may become part of the SPINALTAP_ALGORITHM engine model."
[TH01]: SIGNAL_ROUTING_SPINE "A candidate theory where independent module outputs are converted into typed state signals before being aggregated through spinal_column [SA03]."
[TH02]: VERTEBRAE_LOCAL_SOLVERS "A candidate theory where small scoped solver units [SA02] perform specific transformations, collisions, corrections, style constraints, or state changes."
[TH03]: CONTEXT_WEIGHT_GOVERNOR "A candidate theory for measuring, limiting, and documenting how strongly outside research can influence the internal theory [CW], [DN01]."
[TH04]: STYLE_CONSTRAINT_LAYER "A candidate theory where visual style is treated as a formal constraint surface that can shape rendering, asset rules, and engine presentation [SY]."
[TH05]: SOFT_PROOF_PIPELINE "A candidate theory for moving an idea from raw brainstorm to TECHNICALLY_PLAUSIBLE [TP], then toward SOFT_PROVEN [SP]."

[SA]: SPINALTAP_ALGORITHM "A series of modular algorithms organized through a nervous-system-inspired framework for a mathematical 3D engine. The simplified structure is nervous_system [SA01] -> vertebrae [SA02] -> spinal_column [SA03]."
[SA01]: nervous_system "A broad but bounded algorithm family. Each nervous_system domain contains multiple scoped formulations and contributes to the overall engine ecosystem without owning the entire system."
[SA02]: vertebrae "A smaller modular algorithm, local solver, transform unit, or scoped formulation that operates on a defined data target, module boundary, or delivery point."
[SA03]: spinal_column "The aggregation, routing, and reconciliation layer that ingests outputs from vertebrae and nervous_system modules, orders their relationships, and produces higher-order engine state."

[AS]: ALGORITHMIC_STEM "A modular theory of operation where smaller scoped algorithmic stems formulate their assigned jobs and feed bounded results into larger parent stems that ingest, reconcile, and continue the formulation chain."
[CW]: CONTEXT_WEIGHT "The amount of influence discovered data, source material, research, or prior theory is allowed to have on the current output. High context weight requires stronger anti-replication discipline."
[DN]: DO_NOT "A negative constraint used to remove, ignore, limit, or release an item from contextual relevance."
[DN01]: DATA_REPLICATION "Do not over-weight established theories so heavily that the result becomes a lightly modified replica of the original. Extract constraints, failures, and useful principles without recreating the source."

[SY]: STYLE "A formal video-game design or rendering style marker, usually framed around computational platform capability, rendering behavior, or visual presentation constraints."
[SY01]: LOW_POLY_3D "A reduced-polygon 3D modeling style where simplified geometry is an intentional visual and computational feature."
[SY02]: TEXTURE_MAPPED_LOW_POLY_3D "A low-poly 3D style where image textures provide most surface detail over simplified geometry."
[SY03]: AFFINE_TEXTURED_3D "A retro 3D texture-mapping style associated with perspective-imperfect or visibly warped texture behavior."
[SY04]: DITHERED_3D "A visual style using dithering, color limitation, or noise-pattern transitions to create retro shading and color behavior."
[SY05]: VERTEX_LIT_3D "A lighting style where illumination is calculated at vertices and interpolated across polygon faces."
[SY06]: GOURAUD_SHADED_3D "A smooth polygonal shading style based on interpolated vertex color or lighting values."
[SY07]: FLAT_SHADED_3D "A hard-faceted 3D style where individual polygon planes remain visually distinct."
[SY08]: BILLBOARDED_3D "A 3D presentation technique where 2D planes or sprites are placed and oriented within a 3D scene."
[SY09]: PRE_RENDERED_3D "A presentation style using offline-rendered 3D backgrounds, sprites, or assets inside a real-time or interactive context."
[SY10]: FIXED_FUNCTION_3D "A 3D rendering style associated with pre-modern-shader hardware behavior and limited programmable graphics control."
[SY11]: CEL_SHADED_TOON_SHADED_3D "A stylized 3D rendering approach using simplified lighting, color ramps, outlines, or cartoon-like presentation."
[SY12]: ARCADE_3D "A clean, bright, readable real-time 3D aesthetic associated with arcade 3D presentation."
[SY13]: EARLY_REAL_TIME_CGI "A glossy or toy-like 3D presentation style that imitates early offline CGI while remaining real-time."
[SY14]: SIXTH_GENERATION_3D "A 3D style language associated with Dreamcast, PlayStation 2, GameCube, and original Xbox-era presentation."
[SY15]: RETRO_3D "A broad modern umbrella style for recreating, remixing, or constraining older real-time 3D aesthetics."

[IG]: IGNORE "A contextual ignore marker used to remove a style, concept, source, or direction from active design relevance."
[IG01]: STYLE "Ignore traditional pixel_art as an engine-level or core-design solution for this document."

[RS]: RESEARCH_SOURCE "A real external source entry such as a paper, book, article, documentation page, talk, or implementation note. A complete source record should include title, source, year, link or DOI when available, usage context, context weight, and linked pseudo-citation markers."
[RS00]: OPEN_RESEARCH_SOURCE_SLOT "Reserved draft-only research-source placeholder. Use while a source is being identified, then replace with a complete numbered source record."

[LN01]: UNIQUE_SOURCE_OF_TRUTH "Every active marker should have exactly one source-of-truth definition in [Z]."
[LN02]: SHARED_METADATA_SYNTAX "Blockquote metadata should use the same marker, category, and quoted-definition syntax as registry entries."
[LN03]: RESERVED_DRAFT_SLOTS "[DP00], [RQ00], and [RS00] are reserved draft slots and should not appear in completed sections except when intentionally marking open work."
[LN04]: EXPLICIT_ALIAS_RULE "Deprecated or renamed IDs must be declared as aliases rather than silently reused."
[LN05]: SAFE_QUOTATION_RULE "Definitions should avoid unescaped nested double quotes; use apostrophes inside definition strings when needed."
[LN06]: EXTERNAL_CLAIM_LINKAGE "External factual or research claims should be connected to a research-source record [RS]."
[LN07]: STABLE_CATEGORY_LABELS "Category labels should use stable uppercase snake-case names to reduce renaming artifacts."
[LN08]: WORKFLOW_METADATA_COMPLETENESS "No workflow stage should advance unless its goal, dependency, and requirement metadata are present."

---
