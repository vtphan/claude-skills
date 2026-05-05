---
name: concept-brief-brainstorm
description: Collaborate with the user to develop a rough idea into a decision-ready concept brief through recorded brainstorming rounds. Use this skill when the user asks to brainstorm, shape, formulate, or pressure-test an idea and wants both interactive collaboration and durable Markdown artifacts. The skill helps co-create a compact brief first, then reflects the working frame, generates directions, synthesizes choices, stress-tests the result, and produces `concept-brief.md`.
---

# Concept Brief Brainstorm

Develop a rough idea into a decision-ready `concept-brief.md` through interactive collaboration and durable Markdown files. The human lead owns context, goals, constraints, taste, and final judgment. Codex helps formulate what is missing, infer a provisional brief, generate options, challenge assumptions, synthesize choices, and prepare next steps.

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

## Artifacts

Use a folder for the brainstorm when possible. If the user provides a path, use it. Otherwise create a short slug from the idea title.

```
{brainstorm-slug}/
|-- brainstorm.md
|-- concept-brief.md
`-- rounds/
    |-- round-00-seed.md
    |-- round-01-brief.md
    |-- round-02-frame.md
    |-- round-03-directions.md
    |-- round-04-synthesis.md
    `-- round-05-next-steps.md
```

`brainstorm.md` is the living current synthesis. Keep it concise and current.

`rounds/*.md` preserve process history. They may be more exploratory and should record what changed, what was considered, what was rejected, and why.

`concept-brief.md` is the final or near-final decision-ready artifact. Generate it after Round 5, or update it when the brainstorm has converged enough that the recommendation is usable.

For lightweight sessions, it is acceptable to maintain only `brainstorm.md` and `concept-brief.md`. Do not force round files if the user wants a quick pass.

## Invocation

- `/concept-brief-brainstorm {rough idea}` - start from an inline seed.
- `/concept-brief-brainstorm path/to/idea.md` - start from an existing file.
- `/concept-brief-brainstorm` - continue from the current brainstorm artifacts if they exist; otherwise ask for a rough description.

If the user invokes a different command but clearly asks for this workflow, use the skill.

## Round Flow

### Round 0: Seed

Capture the user's rough idea with low friction. The seed can be messy, partial, contradictory, or solution-biased.

Create `rounds/round-00-seed.md` with:

```markdown
# Round 00: Seed

## Raw Seed
{preserve the user's original input or summarize the referenced file}

## Initial Interpretation
{what Codex thinks the idea is about}

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

## Working Frame

## Promising Directions

## Current Recommendation

## Risks and Assumptions

## Open Questions

## Decisions

## Next Steps
```

Create `rounds/round-01-brief.md` with:

```markdown
# Round 01: Brief Formation

## Draft Compact Brief
- Goal:
- Audience/User:
- Problem or Opportunity:
- Desired Change:
- Context:
- Constraints:
- Success Criteria:

## Assumptions

## Missing Dimensions

## High-Leverage Questions
```

Ask at most 3 questions. Group each question by purpose, such as `[audience]`, `[constraint]`, `[success]`, `[scope]`, `[failure mode]`, or `[decision]`.

### Round 2: Reflect the Working Frame

Reflect the problem space back to the human lead so they can correct Codex's model before ideation.

Create `rounds/round-02-frame.md` with:

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

Create `rounds/round-03-directions.md` with:

```markdown
# Round 03: Directions

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
```

Prefer 4-8 directions when the idea space is broad and 2-4 when the scope is tight. Include at least one conservative, one ambitious, and one high-variance direction when useful.

### Round 4: React, Narrow, Combine

Use the human lead's reactions to reject, combine, sharpen, or reframe directions. Do not restart questioning.

Create `rounds/round-04-synthesis.md` with:

```markdown
# Round 04: Synthesis

## Signals from the Human Lead

## Selected Elements

## Rejected or Set-Aside Elements

## Combined Direction

## Rationale

## Remaining Tensions
```

Update `brainstorm.md` with the strongest current recommendation and decisions.

### Round 5: Stress-Test and Make Next Steps

Pressure-test the synthesized direction and translate it into action.

Create `rounds/round-05-next-steps.md` with:

```markdown
# Round 05: Stress Test and Next Steps

## Risks

## Load-Bearing Assumptions

## Failure Modes

## Validation Plan

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

## Validation Plan

## Open Decisions

## Next Steps
```

The concept brief should distill the process, not reproduce it. Pull from `brainstorm.md`, `round-04-synthesis.md`, and `round-05-next-steps.md`.

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
