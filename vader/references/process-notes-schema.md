# Process Notes Schema

Process notes are an optional project-local file that adjusts VADER's standard wave-skill behavior — *when*, *how*, *with what rigor* the skills operate. They do not change *what* gets built or *what shape* artifacts take. Notes are produced by `architect ratify` when the process-fit verdict is "VADER with notes," and read by `wave-plan`, `wave-execute`, and `wave-update` on every invocation.

The notes file is one of three shapes the architect's process-fit verdict can recommend:

- **Full VADER** — wave cycle as shipped; no notes file produced.
- **VADER with notes** — wave cycle with project-specific simplifications and additions captured in this file.
- **Bail** — VADER's envelope doesn't fit; vision and architecture remain as inputs to a different process.

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [What process notes can and cannot do](#3-what-process-notes-can-and-cannot-do)
4. [Per-skill structure](#4-per-skill-structure)
5. [Authoring lifecycle](#5-authoring-lifecycle)
6. [Invariants](#6-invariants)
7. [Worked mini-example](#7-worked-mini-example)

---

## 1. Philosophy

VADER ships with a default rolling-wave discipline calibrated for solo human + LLM, small-to-medium projects, moderate-to-high uncertainty. Real projects sit on a gradient — some need less discipline, some need more. Process notes are the lightweight mechanism for tuning the cycle without forking VADER per project.

Three operating principles thread through the schema:

**Process, not features.** A note adjusts how a wave skill operates (depth, order, granularity, rigor). It does *not* introduce project-specific tooling (lint commands, screenshots, design tokens) — those belong in the architecture's Quality guardrails or as ADRs. It does *not* introduce new artifact fields or sections — those are schema changes, not notes.

**Capped scope.** Notes can subtract overhead, add project-specific process steps, modulate operating principles. They cannot eliminate invariants, redefine artifact shapes, or replace the cycle. The cap is what keeps notes from forking VADER per project.

**Authored once, read many times.** Drafted by `architect ratify`; user-reviewed before commit; modified by the user as process needs evolve. Each wave skill consults the file at the start of its workflow.

## 2. File format and location

One markdown file per project, named `<project-slug>-process-notes.md`, lives in `docs/` alongside the vision, architecture, and wave plan. Optional — its absence means Full VADER.

```yaml
---
created: 2026-05-03                  # ISO date, set on first creation
last_updated: 2026-05-03             # ISO date, updated on each modification
applies_to: <project-slug>           # Matches the project's other artifacts
---
```

No version field. Notes represent the project's *current* process state, not history. Modifications overwrite. If a note becomes wrong, edit or remove it.

## 3. What process notes can and cannot do

**Can:**

- **Subtract** — skip or simplify a standard step, relax a default trigger, omit a sub-step that doesn't pay off on this project.
- **Add** — introduce a project-specific process step or check, tighten a default rigor, require an explicit sign-off cycle.
- **Modulate** — change the priority or depth of a standard operating principle (e.g., "prioritize speed over verification depth on routine waves").

**Cannot:**

- **Eliminate an invariant** from any wave skill's "things to never do" list. Invariants are structural; if a project genuinely needs to violate one, that's a bail case, not a notes case.
- **Redefine artifact shapes.** New fields, new sections, different structures — those are schema-level changes, not project-local notes. Schema changes go through schema revision.
- **Replace the cycle.** "No wave-update needed at all" is bail-down. "Different audit mechanism" is bail-up. Notes don't substitute for the cycle.
- **Conflict with standard steps.** A note that says "always commit dirty trees" contradicts the dirty-state preflight (which is invariant-shaped). Refuse and surface to the user.

If a note appears to do any of the "Cannot" items, the wave skill consuming it refuses to apply it and asks the user to reclassify (as a bail, a schema change, or a quality requirement).

### Category-mismatch examples (NOT process notes)

| Apparent note | Actual category | Where it belongs |
|---|---|---|
| "Run `npm run lint:fix` before commit" | Tooling preference | Architecture §6 Project Commands |
| "All UI components must have Storybook stories" | Quality requirement | Architecture §6 Quality guardrails |
| "Use design tokens; no hardcoded colors" | Architectural decision | Decision Log entry (ADR) |
| "Add a Reversibility field to ADRs" | Schema change | Schema revision (architecture-schema.md) |
| "Execution report includes a Customer impact section" | Schema change | Schema revision (wave-schema.md) |

The architect rejects category-mismatch notes when drafting and points the user to the right home.

## 4. Per-skill structure

The notes file is organized per-skill with explicit Do/Don't sub-lists. Each skill reads only its own section.

```markdown
# Process notes for <project>

## wave-plan

**Do:**
- <process-shaped item the skill should add or tighten>
  Justification: <one sentence grounded in the project>

**Don't:**
- <process-shaped item the skill should skip or simplify>
  Justification: <one sentence grounded in the project>

## wave-execute

**Do:**
- ...
  Justification: ...

**Don't:**
- ...
  Justification: ...

## wave-update

**Do:**
- ...
  Justification: ...

**Don't:**
- ...
  Justification: ...
```

A note without justification is a draft, not a commitment. Skills consuming an unjustified note flag it to the user.

If a section is empty (`## wave-plan` has no notes), the section may be omitted from the file entirely. An absent section means Full VADER for that skill.

## 5. Authoring lifecycle

- **Created by `architect ratify`** when the process-fit verdict is "VADER with notes." The architect drafts the notes from project context (vision, architecture, signals about uncertainty and convention); user reviews/approves; file is written alongside the architecture commit.
- **Modified by the user** at any time via direct edit. No skill rewrites the notes file — preventing it from accidentally drifting from user intent.
- **Read by** `wave-plan`, `wave-execute`, and `wave-update` on every invocation.
- **Versioning**: free-form. Each modification updates `last_updated`; no version field.

When the user edits the notes mid-project, the change applies to subsequent skill invocations only — past wave-update entries are not retroactively re-evaluated.

## 6. Invariants

1. **Notes are process-shaped, not feature/tooling/architectural/schema-shaped.** Wrong-category notes are rejected by the consuming skill with a pointer to the right home.
2. **Notes cannot eliminate invariants** in any wave skill's "things to never do" list.
3. **Notes cannot redefine artifact shapes.** Schema-level changes go through schema revisions, not project-local notes.
4. **Notes cannot replace the cycle.** A project that doesn't fit the cycle is a bail case.
5. **Each note carries a one-sentence justification grounded in the project.** Unjustified notes are drafts.
6. **Each wave skill reads only its own section.** wave-execute does not parse wave-update's notes.
7. **The notes file is optional.** Its absence means Full VADER.

## 7. Worked mini-example

A truncated notes file showing both lighter and heavier directions for one skill:

```markdown
---
created: 2026-05-03
last_updated: 2026-05-03
applies_to: bookclub
---

# Process notes for bookclub

## wave-plan

**Don't:**
- Wave count may be 2 (not 3-6).
  Justification: project is small enough that two waves capture rolling-wave value without padding.
- Skip the Features layer in current-wave detail; tasks cite Stories directly.
  Justification: Features add a layer this project's stories don't need.

## wave-execute

**Do:**
- Run the repro twice in step 5: once on a checkout of `wave_start_ref` (regression baseline), then on the wave's commit (wave behavior).
  Justification: false-positive repro passes have happened on this codebase.

**Don't:**
- Skip the per-task ADR re-read in step 4.2; trust the wave plan's `ADRs respected` list.
  Justification: ADRs are short and well-known.
- Verification matrix: only the Repro row is mandatory; other rows optional based on risk calibration.
  Justification: this project's tests are integrated under the repro.

## wave-update

**Don't:**
- Skip the code-quality lens default-trigger.
  Justification: this project's logic is conventional CRUD; lens findings would be low-signal.
- Audit findings: compress Evidence to a single sentence unless the finding is consequential (high severity, supersession, or scope change); consequential findings keep the full Evidence block.
  Justification: solo project; routine findings don't need multi-sentence evidence, but consequential ones still anchor the audit trail.
```

A reader can see at a glance how this project's process differs from Full VADER: lighter on wave-plan structure, slightly tighter on wave-execute regression discipline, lighter on wave-update audit depth. The cycle's spine — propose-then-ratify, walking-skeleton, audit independence — remains intact.

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
