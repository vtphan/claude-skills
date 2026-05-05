---
name: concept-brief-brainstorm
description: Collaborate with the user to develop a rough idea into a decision-ready concept brief through recorded brainstorming rounds. Use this skill when the user asks to brainstorm, shape, formulate, or pressure-test an idea and wants both interactive collaboration and durable Markdown artifacts. The skill helps co-create a compact brief first, then reflects the working frame, generates directions, synthesizes choices, stress-tests the result, and produces `concept-brief.md`.
---

# Concept Brief Brainstorm

Develop a rough idea into a decision-ready `concept-brief.md` through interactive collaboration and durable Markdown files. The human lead owns context, goals, constraints, taste, and final judgment. Help formulate what is missing, infer a provisional brief, generate options, challenge assumptions, synthesize choices, and prepare next steps.

The goal is not endless ideation or a transcript. The product is a concept brief the human lead can use to decide, explain, validate, or begin execution.

## Operating Principle

Always bring an artifact to the table before asking for more. Questions are useful only when they materially improve the brief, change the frame, or affect the next move.

Prefer:

- Drafting a provisional brief from incomplete input.
- Marking assumptions and uncertainties explicitly.
- Asking 1-3 high-leverage questions at a time.
- Advancing the artifact after each user response.
- Moving toward a decision-ready concept brief.

Avoid:

- Long questionnaires.
- Repeated question-only rounds.
- Blocking progress until the human fully articulates the idea.
- Treating silence as rejection.
- Generating ideas before the basic problem frame is intelligible.

Templates are scaffolds, not quotas. Omit a section, mark it `TBD`, or note "no signal yet" rather than padding to fill structure.

Advance to the next round when the current artifact has enough signal to support the next phase. Rounds are not a per-turn cadence - multiple turns can live in the same round.

Read the human lead's reactions for taste, not just decisions. What they accept, reject, hesitate over, or rewrite reveals implicit criteria. Surface those criteria back when they would change a recommendation.

Invite the human lead to challenge assistant priors or recurring patterns. If you keep proposing the same shape of direction, that may be a pattern in your generation rather than a recommendation about their problem.

## Human Lead's Job

The human lead's required engagement is small and well-defined:

1. Provide a rough seed and any context they have.
2. React to artifacts: yes / no / mostly / not quite / change X.
3. Make or correct decisions when surfaced.

The human is *not* required to fill template fields, answer questions in series, or read round files. `brainstorm.md` is the only document they are expected to track; `concept-brief.md` is the deliverable. Round files are LLM-side process bookkeeping - history, not interface.

**Default-and-confirm over ask.** When a reasonable proposal can be made from existing signal, propose it as a default the human can confirm or correct. Reserve real questions for cases where no defensible default exists *and* the answer would materially change the next artifact. The 3-question cap is a ceiling; the target is zero.

**Decisions consolidate in one queue.** Surface decision points in `## Decisions Needed` in `brainstorm.md`, not scattered across rounds. The human should be able to scan that one block to know what needs their input.

**Reaction granularity is coarse.** When presenting directions, syntheses, or analyses, support reaction at the highest useful level (yes/no/hesitate on a whole direction). The fine-grained per-attribute reasoning is for your own work; the human's reaction can be coarse.

**Exit at any point.** If the human signals satisfaction or asks for the brief, generate `concept-brief.md` from current state. Mark undeveloped sections explicitly. Process completion is not required.

## Loopback

When new signal damages prior work, choose loopback proportional to the damage rather than always restarting. This applies at any round, not only after stress-test:

- **Revise in place**: a single assumption is wrong but the direction still holds - fix the recommendation, do not loop back.
- **Re-narrow** (Round 4): the synthesis combined the wrong elements - return to the shortlist with sharper criteria.
- **Re-diverge** (Round 3): the directions are exhausted but the frame is still right - generate fresh ones with new generative moves.
- **Re-frame** (Round 2): the problem space itself is wrong - go back and reflect a corrected frame.

## Artifacts

Use a folder for the brainstorm when possible. If the user provides a path, use it. Otherwise create a short slug from the idea title.

```
{brainstorm-slug}/
|-- brainstorm.md              # the only required living artifact
|-- concept-brief.md           # rendered from brainstorm.md when ready
`-- rounds/                    # optional; lazy
    `-- round-NN-*.md          # only when a round produces non-redundant material
```

`brainstorm.md` is the only living artifact. Keep it concise and current; every round updates it.

`concept-brief.md` is a render of `brainstorm.md`, not a parallel state. Generate it when the recommendation is decision-ready or when the human asks for the brief; regenerate on demand. Do not maintain it in parallel with `brainstorm.md`.

Round files are lazy. Create one only when a round produces material that does not belong in `brainstorm.md` - rejected directions worth preserving, alternative frames you considered, scratchpad fragments, loopback breadcrumbs, or detailed reasoning the brainstorm summary would lose. Rounds 0, 1, and 2 rarely earn a file. Round 3 often does (the full direction set with attributes). Rounds 4 and 5, when produced in the same session, combine into a single `round-04-synthesis-and-stress-test.md`. If a round produces nothing non-redundant, skip the file.

## Invocation

- `/concept-brief-brainstorm {rough idea}` - start from an inline seed.
- `/concept-brief-brainstorm path/to/idea.md` - start from an existing file.
- `/concept-brief-brainstorm` - continue from the current brainstorm artifacts if they exist; otherwise ask for a rough description.

If the user invokes a different command but clearly asks for this workflow, use the skill.

## Round Flow

### Round 0: Seed

Capture the user's rough idea with low friction. The seed can be messy, partial, contradictory, or solution-biased.

Fold the seed into `brainstorm.md` directly. Create a separate `rounds/round-00-seed.md` only when the raw input is substantial enough to warrant archiving (long pasted document, external file you're summarizing, multiple variants). When created, use:

```markdown
# Round 00: Seed

## Raw Seed
{preserve the user's original input or summarize the referenced file}

## Initial Interpretation
{what you think the idea is about}

## Early Unknowns
{short bullets; mark only important gaps}

## Suggested Round 1 Focus
{what the brief-formation round should resolve first}
```

Initialize `brainstorm.md` from the same material.

### Round 1: Co-create the Compact Brief

Help the human lead formulate a compact brief; do not require them to provide one upfront.

Update `brainstorm.md` with:

```markdown
# {Working Title}

## Compact Brief
- Goal:
- Audience/User:
- Problem or Opportunity:
- Desired Change:
- Context:
- Constraints:
- Success Criteria:

## Working Frame

## Promising Directions

## Current Recommendation

## Risks and Assumptions

## Confidence Notes

## Decisions Needed

## Decisions Made

## Next Steps
```

Create `rounds/round-01-brief.md` only when assumptions, missing dimensions, or alternative briefs you weighed are substantial enough to preserve. The Compact Brief itself lives in `brainstorm.md`; the round file (if created) captures only what doesn't fit there:

```markdown
# Round 01: Brief Formation

## Assumptions

## Missing Dimensions

## High-Leverage Questions
```

`Missing Dimensions` should include not just structurally empty fields but what category knowledge suggests usually matters for this kind of problem - regulatory constraints, distribution, baseline metrics, common failure modes, key stakeholders - that the human has not yet mentioned.

Ask at most 3 questions. Group each question by purpose, such as `[audience]`, `[constraint]`, `[success]`, `[scope]`, `[failure mode]`, or `[decision]`.

### Round 2: Reflect the Working Frame

Reflect the problem space back to the human lead so they can correct your model before ideation.

Create `rounds/round-02-frame.md` only when alternative frames you weighed, significant tensions, or correction history are worth preserving. When created, use:

```markdown
# Round 02: Working Frame

## Problem Space

## Context and Constraints

## Opportunity Areas

## Decision Criteria

## Tensions

## Corrections Needed
```

Update `brainstorm.md` so the compact brief and working frame represent the current best understanding.

### Round 3: Generate Directions

Generate distinct directions only after the working frame is coherent enough to make ideas meaningful.

These named moves expand the search beyond free-form ideation. Apply whichever fit the problem - not all of them every round:

- **Analogies**: what other problem (in a different domain) has this same shape?
- **Prior art**: how have people solved this or its neighbors before? what patterns recur?
- **Inversion**: what would guarantee failure? what would the opposite design look like?
- **Constraint flipping**: 10x the budget, 0.1x the budget, no time pressure, hostile users.
- **Adjacent-domain transfer**: what does another field (medicine, games, ops, governance) do here?
- **Knowledge-gap flag**: if you don't have enough domain knowledge to generate well, say so and ask for a reference rather than producing weak options confidently.

When you pull examples or patterns from memory (prior art, analogies, adjacent-domain transfers), mark them as remembered/unverified unless they are sourced from provided materials or explicit research. Confidently inventing prior art is worse than naming an uncertain reference.

Use a scratchpad when raw probes help you find directions; skip it when directions come directly. Scratchpad content is disposable - prune it before locking the round unless specific fragments are worth preserving as history.

Create `rounds/round-03-directions.md` with:

```markdown
# Round 03: Directions

## Scratchpad
{optional - rough probes, analogies, fragments; omit if you didn't need it, or prune before locking}

## Direction 1: {Name}
- Shape:
- Why it might work:
- Tradeoffs:
- Effort:
- Novelty:
- Fit:

## Direction 2: {Name}

## Direction 3: {Name}

## Comparison

## Recommended Shortlist

## Knowledge Gaps
{topics where you lack enough domain knowledge to generate confidently - name them rather than bluffing}
```

Prefer 4-8 directions when the idea space is broad and 2-4 when the scope is tight. Include at least one conservative, one ambitious, and one high-variance direction when useful.

After the first batch, name the unexplored quadrant of the design space - what shape of direction is missing? Generate one or two more directions targeting that gap before locking the round.

### Round 4: React, Narrow, Combine

Use the human lead's reactions to reject, combine, sharpen, or reframe directions. Do not restart questioning.

Infer taste from reactions: what implicit criteria would explain their acceptances, rejections, hesitations, and edits? Name those criteria - they often matter more than the directions themselves and should reshape the shortlist.

Beyond criteria, name the underlying principle emerging across the directions and reactions. Sometimes the real idea is the pattern beneath them, not any single direction - the combined direction should express that principle, not just blend mechanics. If the principle suggests a direction nobody generated, that is a signal to re-diverge rather than synthesize from what you have.

Combine *fragments* of accepted directions, not just whole directions. The strongest concept often comes from grafting one direction's mechanism onto another's framing.

If reactions cluster around "none of these feel right," the frame is probably wrong. Drop back to Round 2 or Round 3 rather than forcing a synthesis.

Create `rounds/round-04-synthesis.md` (or, if Round 5 will happen in the same session, `rounds/round-04-synthesis-and-stress-test.md` to hold both) with:

```markdown
# Round 04: Synthesis

## Signals from the Human Lead

## Inferred Criteria
{what reactions reveal about implicit values, taste, and decision criteria}

## Emerging Principle
{the deeper pattern or concept implied by the directions and reactions - the "real idea" beneath the surface options}

## Selected Elements

## Rejected or Set-Aside Elements

## Combined Direction

## Rationale

## Remaining Tensions
```

Update `brainstorm.md` with the strongest current recommendation and decisions.

### Round 5: Stress-Test and Make Next Steps

Pressure-test the synthesized direction and translate it into action.

Infer the load-bearing private belief from prior signal: what would have to be true for the human to abandon this? Propose it as a default for them to correct or confirm - "Likely belief that, if false, kills this concept: X." Only ask the literal question when no defensible inference is available.

If the stress test reveals weakness, apply the Loopback ladder (revise in place / re-narrow / re-diverge / re-frame). Stress-test is the most common invocation site, but loopback is available at any round.

Append to the combined `rounds/round-04-synthesis-and-stress-test.md` if you opened one for Round 4 in the same session; otherwise create `rounds/round-05-next-steps.md` with:

```markdown
# Round 05: Stress Test and Next Steps

## Risks

## Load-Bearing Assumptions

## What Would Change the Human Lead's Mind
{disconfirming evidence the human lead names - the belief that, if false, kills the concept}

## Failure Modes

## Validation Plan

## Loopback Decision
{none / revise in place / re-narrow / re-diverge / re-frame - with reason}

## Open Decisions

## Next Actions
```

Then generate or update `concept-brief.md`.

## Concept Brief Format

`concept-brief.md` should be clean enough to share and concrete enough to act on.

```markdown
# {Concept Name}

## Summary

## Problem or Opportunity

## Target Audience

## Context and Constraints

## Core Insight

## Recommended Direction

## Why This Direction

## Alternatives Considered

## Risks and Assumptions

## Confidence Notes
{remembered/unverified claims, speculative assumptions, and knowledge gaps the decision-maker should see; carry forward markings from round files}

## Validation Plan

## Open Decisions

## Next Steps
```

The concept brief is rendered from `brainstorm.md`, not maintained in parallel. Pull primarily from `brainstorm.md`; pull from any round files that exist for additional detail (rejected alternatives, reasoning traces). Regenerate on demand from current state.

## Iteration Rules

On every continuation:

1. Read `brainstorm.md`, `concept-brief.md` if present, and the latest relevant round file.
2. Identify new human signal from chat or file edits.
3. Update the current artifact before asking questions.
4. Ask at most 3 questions, and only if the answers would materially change the next artifact.
5. Preserve important rejected ideas in round history or `Alternatives Considered`.
6. Keep `brainstorm.md` current and concise.
7. Move to `concept-brief.md` when the recommendation is decision-ready enough.

## Communication Style

After writing or updating files, respond in chat with:

- What artifact changed.
- The most important current shift.
- The 1-3 items the human lead should review or answer next.

Keep chat short. The durable work belongs in the files.
