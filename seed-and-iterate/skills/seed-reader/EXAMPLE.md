# Seed Reader: Example Interaction

This file shows a complete Seed Reader cycle on a realistic sparse seed. It exists to calibrate the skill's behavior — what good output looks like, how much to propose, what tone to take.

## Input: a sparse first-draft seed

```markdown
---
id: seed
project_name: homework system for algorithms course
status: draft
---

# Seed

## Project description

A homework system for my algorithms course that captures behavioral data for instructor intervention and learning research.

## Non-obvious bets

- Infrastructure first, not features
- Single course pilot before generalizing

## Out of scope

-

## Constraints

-

## Anchor personas

-

## Anchor journeys

-

## Open questions

- How much experimental infrastructure should be in phase one?

## Change log

- 2026-04-27: Initial draft.
```

## Output

### Part 1: The revised seed

```markdown
---
id: seed
project_name: homework system for algorithms course
status: draft
---

# Seed

## Project description

A homework system for my algorithms course that captures fine-grained behavioral data, supports instructor intervention during assignment windows, and provides exportable data for learning research.

## Non-obvious bets

- **Infrastructure first, not features.** Build event logging, editor with autosave, and exportable data layer before any feature breadth.
- **Single course pilot before generalizing.** Algorithms course at one institution for the first iteration; multi-section and multi-course support deferred.
- **Research utility and pedagogical utility weighted equally.** Design decisions that serve only one are weaker than those that serve both.
- **Instructor-led adoption.** Students use the system because the course requires it, not because they choose it standalone.

## Out of scope

- Gradebook or LMS integration.
- Multi-institution deployment.
- Mobile clients.
- Content authoring UI for instructors (problems are authored as files for now).
- Human help routing or TA queue (deferred to later iteration).

## Constraints

- FERPA compliance for any student data captured.
- IRB approval required before any data is used for research; needs to fit existing IRB framework.
- Single instructor maintaining the system; cannot rely on dedicated ops staff.
- Must run on existing infrastructure available to the instructor.

## Anchor personas

- Student in the algorithms course.
- Instructor (the project owner).
- Teaching assistant for the course.
- Learning scientist collaborator.

## Anchor journeys

- Completing a homework assignment.
- Getting unstuck on a problem.

## Open questions

- How much experimental infrastructure should be in phase one? Specifically, is randomized assignment to conditions in scope for the first iteration, or only observational data capture?
- Does the first iteration need any researcher-facing tooling, or is exporting raw event data sufficient until later?

## Change log

- 2026-04-27: Seed Reader pass — added bets, populated constraints, personas, journeys, out-of-scope; sharpened project description; expanded one open question.
- 2026-04-27: Initial draft.
```

### Part 2: Changes proposed

- **Added** two bets (research-and-pedagogy weighting, instructor-led adoption). Both follow naturally from the project description and the existing infrastructure-first bet, but were implicit rather than committed.
- **Populated** out-of-scope with five items inferred from the bets and project description. The most important is gradebook integration, which is the most likely "while we're at it" addition that would derail the infrastructure focus.
- **Populated** constraints with FERPA, IRB, single-maintainer, and existing-infrastructure items. These follow from the institutional context but weren't written down.
- **Populated** anchor personas with four roles. The four are the minimum needed to make sense of the bets — student and instructor are core; TA is needed for the "getting unstuck" journey; learning scientist is needed for the research bet.
- **Populated** anchor journeys with the two we discussed. These cover the most design-critical experiences without being exhaustive.
- **Sharpened** the project description to specify what kind of behavioral data, what kind of intervention, and what kind of research output. The original was too vague to constrain design.
- **Expanded** the open question about experimental infrastructure into a more specific form, and added a related question about researcher-facing tooling.

### Part 3: Questions

1. I treated "learning scientist collaborator" as a single persona, but if you're also designing for researchers who are not your direct collaborators (e.g., other faculty who might use exported data later), that's a distinct persona. Should I split this?
2. The IRB constraint says "fit existing IRB framework" — does this mean the system must work within your current Polylogue 2.0 or related approval, or are you anticipating a new IRB application for this system specifically? The answer affects what experimental infrastructure is feasible in iteration one.

---

## What this example illustrates

A few things to notice about this example, since they show what calibrated Seed Reader output looks like:

**Substantial proposals when the seed is sparse.** The input had three populated sections; the output added five sections worth of content. This is appropriate when the user has clearly signaled they want help filling things in.

**Every proposal is grounded in something the user wrote or implied.** The bets weren't invented — they follow from the project description and the existing bets. The constraints come from institutional context the user mentioned. Nothing was added speculatively.

**Sharpening preserves intent.** The project description was sharpened, not rewritten. The original "captures behavioral data" became "captures fine-grained behavioral data" — same intent, more specific.

**Out-of-scope is treated as load-bearing.** Five out-of-scope items, each of which is the kind of thing that would be tempting to include later. The list does real work in constraining the project.

**Questions are about decisions only the user can make.** Both questions identify ambiguities where there's no defensible default — they require the user's judgment about institutional context (IRB) or research collaboration (persona scope).

**Change log entries are specific.** "Seed Reader pass — added bets, populated constraints, personas, journeys, out-of-scope; sharpened project description; expanded one open question" tells a future reader exactly what changed without requiring them to diff the document.

## Counter-example: when to propose less

For contrast, here's what good Seed Reader output looks like when the seed is already polished. Input: a complete seed with no contradictions and concrete language throughout. Output:

> The seed is in good shape. I have no substantive proposals.
>
> One small observation: the open question about "TA queue scope" appears resolved by the out-of-scope item ("human help routing deferred to later iteration"). Consider closing this open question with a brief note in the change log, or leaving it open if you want to revisit before the next iteration.

That's the entire output. No revised seed (since nothing substantive changed), one observation, no questions. Resist the urge to find changes for their own sake.
