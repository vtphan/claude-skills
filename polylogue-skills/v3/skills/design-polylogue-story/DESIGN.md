# design-polylogue-story — architectural notes

This file is a brief architectural orientation for contributors working on the skill itself. It is **not** a reference for running the skill — for that, read `SKILL.md`. For load-bearing design decisions and their rationale, read `../../../DECISIONS.md` (canonical record).

## Where things live

- **`SKILL.md`** — the operational spec (audience, operating principles, round flow, runtime estimator, bundled assets). The single document a model running this skill needs to read first.
- **`schema.json`** — JSON Schema for the exported `story.json`. Cross-cutting invariants not enforceable by JSON Schema are listed in the schema's `description` field and re-checked at the Round 4 quality review.
- **`thinking-skills.md`** — canonical catalogue of skill names with slot tags. Used to validate author-named skills at Round 0 and to assign skills to slots at Round 2.
- **`skills-reference.md`** — per-skill **registry**: stable misconception names (used as `misconception_targeted` for cross-story consistency), per-skill staging pedagogy (medium-specific), per-skill selection warnings (system-specific). **Not a pedagogy textbook** — definitions, mastery rubrics, and authoring craft are LLM competence and aren't written there. Includes a gap-handling protocol for skills in the catalogue without a registry entry.
- **`lenses/`** — three concern-lens specs (story craft, pedagogy, polish-and-renderer). They describe what each concern asks of the work; they are *not* a three-stage pipeline the model must formally step through every round.

## Architectural shape (v3)

- **Six rounds, not nine.** R0 seed → R1 concept → R2 cast/art/outline → R3 chapter authoring (pages + chapter-end challenges per chapter, with image-prompt review as an optional pass when renders exist) → R4 quality review → R5 export. The collapses (R2+R3, R4+R5, R6 demoted) are documented in `../../../DECISIONS.md` §"V3 development goal."
- **Three concerns, not three stages.** The lens files in `lenses/` are concern lenses, not pipeline stages. SKILL.md describes what each round produces; the lens specs describe what to attend to when that concern is active. The Round 4 quality review is the one place where polish/renderer is genuinely sequential against a checklist.
- **Decisions, not verification.** The author's role in the iterative dialog is *decisive* (taste, scope, classroom context, theme, sensitivities), not *verificative*. The LLM resolves competence calls (schema, mechanics, prose, misconception specificity given the registry, elimination check, position distribution, bible sync, renderer-facing rules) silently and surfaces bounded decisions where the author's context determines the answer. After each round, the author sees *what changed*, *what was judged silently*, and *1-3 decisions for them* — not a review queue. See SKILL.md's "Iterative dialog with the author" section.
- **Y-shape with one perspective fork**, two-tier chapter end (formative comprehension check + narrative-routing decision), three skill categories (Foundational / Thinking / SEL with SEL split into content and process). All preserved from v2 — the v3 work was process simplification, not artifact change.
- **Cold-start design.** No bundled `sample-story.json`. Per DECISIONS §2.2, the iteration mechanism is what compensates for cold start; the first real story produced through the skill becomes the sample for v4+. `skills-reference.md` deliberately does not include worked micro-examples — author reactions during iteration encode calibration into the artifact.

## What this skill is not

- Not a general story-writing skill — the polylogue/CYOA structure, two-tier chapter end, and per-skill challenge authoring are load-bearing.
- Not a recipe to be followed step-by-step. It's a briefing for a capable LLM working in iterative dialog with a human author. See DECISIONS.md §2 for the operating principles (briefing-not-recipe, iterative dialog with decisions-not-verification, acceptable artifacts before architectural elegance).

## Companion skill

`revise-polylogue-story` (sibling folder) currently lags behind on v1-era conventions. It will be updated in a later milestone, after design-polylogue-story finalizes in v3. Don't invoke it for new stories until updated. See DECISIONS.md §13 for the file-by-file change list that will be echoed there.
