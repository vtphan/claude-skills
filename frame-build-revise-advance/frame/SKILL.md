---
name: frame
description: Use this skill when the user wants to create or reshape a wave doc for a one-human, one-smart-LLM coding process. It turns a brief, brainstorm, product idea, existing notes, or messy current plan into a concise Frame-Build-Revise-Advance wave doc with inactive, active, and done waves. Trigger on requests like "frame this project", "create the wave doc", "plan the first wave", "turn this idea into waves", "set up FBRA", or "reframe the plan". Do not use for actually building code; use build for implementation.
---

# Frame

Create or reshape the project's wave doc. Before writing, read `references/fbra-schema.md`.

## Purpose

Frame gives a smart LLM enough direction to build with freedom while preserving human control over scope, architecture, and product decisions.

## Inputs

- A brief, brainstorm, product idea, existing requirements, or current codebase context.
- Optionally, an existing wave doc to reshape.

## Output

A single wave doc, usually `docs/<project-slug>-waves.md`. If the path is ambiguous, choose `docs/` when it exists; otherwise place it beside the source brief.

## Workflow

1. Extract the goal, intended users, non-goals, hard constraints, and obvious decision boundaries.
2. Choose the first active wave. Default W1 to a walking skeleton unless the user clearly needs a different first slice.
3. Write inactive waves as concise future direction: must-have stories, must-have features, and notes only.
4. Write the active wave with must-have requirements, optional nice-to-haves, implementation notes, tasks, decisions needed, and verification.
5. Seed a compact Decisions section only with durable choices already known.
6. Put deferred ideas and open questions in Notes.

## Judgment

Prefer fewer waves with clear intent over a long speculative roadmap. Three to five waves is usually enough.

Must-have requirements in the active wave should be testable and user-visible where possible. Avoid requirements that merely name components.

Give the LLM freedom on local implementation details. Make it ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.

Verification should be practical: relevant existing tests, focused new tests for important logic, and a demo path for the main user value.

## Do Not

- Do not create detailed tasks for inactive waves.
- Do not require formal acceptance criteria for every story.
- Do not create separate execution or audit reports.
- Do not overfill Decisions with guesses.
- Do not make the wave doc longer than the project can justify.
- Do not leave more than one active wave.
