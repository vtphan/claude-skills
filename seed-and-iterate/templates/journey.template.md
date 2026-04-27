---
id: journey-<short-slug>
title: <human-readable title>
seed_ref: seed
context_ref: context
goal_ref: goal-<slug>
persona_refs: [<persona-id-1>, <persona-id-2>]
status: draft
---

# Journey: <title>

> A specific user experience relevant to the current Goal. Captures the arc of what a persona is trying to accomplish, including emotions, friction, and cross-role handoffs. Stable stage IDs are essential because Stories will reference them.

## Decision points

1. <decision point 1>
2. <decision point 2>
3. <decision point 3>

## Scenario

*confidence: <high|medium|low>*

<One paragraph setting the context. Who, when, where, what state are they in, what triggered this journey, what's at stake?>

## Stages

> Ordered list of stages in the journey. Each has a stable ID for reference from Stories.

### stage-<short-slug>: <stage name>

*source: <observed|literature|assumed|validated>*  *confidence: <high|medium|low>*

- **User actions:** <what the user does at this stage>
- **User thoughts and feelings:** <internal state, motivations, anxieties>
- **Friction points:** <what gets in the way, where the user struggles or gives up>
- **System touchpoints:** <how the system is involved at this stage, if at all>

### stage-<short-slug>: <stage name>

*source: <observed|literature|assumed|validated>*  *confidence: <high|medium|low>*

- **User actions:**
- **User thoughts and feelings:**
- **Friction points:**
- **System touchpoints:**

### stage-<short-slug>: <stage name>

*source: <observed|literature|assumed|validated>*  *confidence: <high|medium|low>*

- **User actions:**
- **User thoughts and feelings:**
- **Friction points:**
- **System touchpoints:**

## Key insights

> Three to five takeaways that should drive design decisions. These are often where the highest-value insights live — emotional arcs, surprising behaviors, cross-role handoffs, gaps between stages.

- *source: <observed|literature|assumed|validated>* <insight 1>
- *source: <observed|literature|assumed|validated>* <insight 2>
- *source: <observed|literature|assumed|validated>* <insight 3>

## Cross-persona moments

> Optional. Moments where this journey touches another persona — handoffs, notifications, observations. These are often where Story-level work misses the most.

- <moment 1>
- <moment 2>

## Change log

- <YYYY-MM-DD>: Initial draft.
