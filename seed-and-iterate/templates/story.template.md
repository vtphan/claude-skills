---
id: story-<short-slug>
title: <human-readable title>
seed_ref: seed
context_ref: context
goal_ref: goal-<slug>
journey_moment_refs: [<journey-id>#stage-<slug>]
priority: <must|should|could|won't>
status: draft
---

# Story: <title>

> A deliverable unit of work tied to one or more journey moments. Includes the user-facing story, acceptance criteria, and concrete technical requirements.

## Story

**As a** <role>,
**I want** <capability>,
**so that** <benefit>.

## Journey moments served

> Which journey stages this story addresses. Every story should trace to at least one journey moment. If it doesn't, it's suspect — the story may not be serving real user value.

- [<journey-id>#stage-<slug>] — <brief note on how this story addresses that moment>

## Acceptance criteria

> What "done" looks like from the user's perspective. Should be observable and testable.

- <criterion 1>
- <criterion 2>
- <criterion 3>

## Requirements

> Concrete technical specifications. Every requirement has a type, a specification with concrete numbers and thresholds where applicable, and a verification method. Vague requirements ("the system should be performant") are not acceptable — every requirement must be testable.

### req-<short-slug>: <requirement title>

- **Type:** <functional|non-functional|data|edge-case>
- **Specification:** <what must be true, with concrete numbers and thresholds>
- **Verification:** <how to confirm this is met — automated test, manual test, observation, etc.>

### req-<short-slug>: <requirement title>

- **Type:** <functional|non-functional|data|edge-case>
- **Specification:**
- **Verification:**

### req-<short-slug>: <requirement title>

- **Type:** <functional|non-functional|data|edge-case>
- **Specification:**
- **Verification:**

## Notes

> Optional. Context, rationale, alternatives considered, related stories. Anything that helps a future reader understand why this story is the way it is.

<notes>

## Change log

- <YYYY-MM-DD>: Initial draft.
