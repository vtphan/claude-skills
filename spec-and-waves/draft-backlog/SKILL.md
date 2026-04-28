---
name: draft-backlog
description: >-
  Use this skill when the user has a finalized or mostly finalized Spec and
  Waves Starter Spec and wants a planning-ready Backlog drafted or revised. This
  skill translates the Starter Spec into concise user stories, features,
  priorities, guardrails, deferred items, decision points, and open questions.
  Use when the user says things like "draft the backlog", "turn this spec into
  backlog", "create stories and features from this starter spec", or provides
  docs/spec-and-waves/starter-spec.md and asks for the next step. Do NOT use for
  wave planning, wave sequencing, task breakdowns, detailed technical
  requirements, architecture, implementation plans, or code.
---

# Draft Backlog

Turn a finalized Starter Spec into a concise Backlog that is ready for rolling-wave planning. The Backlog is a translation layer: it organizes human intent into stories and features, but does not decide wave order or implementation detail.

Read `../templates/backlog.template.md` before producing a full backlog. If it is unavailable, use the section order in this skill.

Default artifact path: `docs/spec-and-waves/backlog.md`.

## Output Contract

Return three sections:

1. **Draft Backlog** — the full proposed backlog, using this structure:
   - `Decision Points`
   - `Goal for This Plan`
   - `Guardrails`
   - `Stories`
   - `Features`
   - `Deferred`
   - `Open Questions`
2. **Trace Notes** — concise notes mapping important backlog choices back to the Starter Spec.
3. **Leader Decisions** — at most 5 decisions the human should make before wave planning. Omit if none.

If revising an existing Backlog, preserve stable IDs unless there is a strong reason to change them.

## What Belongs In The Backlog

Include:

- A plan-level goal derived from the Starter Spec.
- Guardrails for this plan: in scope and out of scope.
- User stories with stable IDs.
- Short story context, especially from Key Journeys.
- Acceptance sketches: 2-4 user-facing checks per story.
- Features that support one or more stories.
- Priority: `must`, `should`, or `could`.
- Deferred items with reasons.
- Open questions that affect planning or implementation.

## What Does Not Belong

Do not add:

- Wave ordering.
- Task lists.
- Architecture.
- Database schemas, APIs, file paths, components, or implementation steps.
- Detailed technical requirements.
- Performance targets unless the Starter Spec commits to them.
- Long journey maps or persona narratives.

If technical detail seems necessary, put a short item in `Open Questions` or `Notes`; do not resolve it here.

## Drafting Rules

Use the Starter Spec as the source of truth:

- Preserve the human's scope boundaries.
- Treat LLM-suggested Key Journeys as proposed context, not validation.
- Convert rough user stories into consistent story form.
- Add missing stories only when strongly implied by Idea, Users, Features, Scope, or Key Journeys.
- Do not silently expand scope. Put attractive but uncommitted ideas in `Deferred` or `Open Questions`.
- Prefer fewer, stronger stories over exhaustive coverage.

## Traceability Rules

Every story and feature should be traceable to the Starter Spec.

For each important story or feature, make its origin clear through `Context`, `Notes`, or `Trace Notes`:

- `Idea`: the central problem or opportunity it serves.
- `Users`: the role it serves or affects.
- `User Stories`: the rough story it normalizes.
- `Features`: the capability it supports.
- `Key Journeys`: the pain point or hidden friction it addresses.
- `Scope`: why it is in or out.
- `Open Questions`: what uncertainty it depends on.

If you cannot trace a story or feature to the Starter Spec, do not quietly include it. Put it in `Deferred` or `Open Questions`.

## Risk Inputs For Wave Planning

The Backlog should not sequence waves, but it should preserve planning-relevant uncertainty.

Use `Open Questions`, `Notes`, or `Decision Points` to flag:

- high-uncertainty stories
- stories implied by unvalidated Key Journeys
- features likely to expand scope
- trust, approval, recovery, integration, or adoption risks
- priority decisions the human lead must settle before `draft-wave-plan`

## Story Guidance

Stories should be durable user-value units:

```markdown
### US-<ROLE>-<N>: <Title>

As a <role>, I want <capability>, so that <benefit>.

Context: <user moment, pain point, or key journey link>
Priority: must | should | could
Source: observed | assumed | validated

Acceptance sketch:
- Given ..., when ..., then ...
- Given ..., when ..., then ...

Notes:
- Optional ambiguity, constraint, or edge case.
```

Acceptance sketches are not full requirements. They should describe externally visible success, not internal implementation.

## Feature Guidance

Features are supporting capabilities:

```markdown
### F-<N>: <Title>

Description: One or two sentences.
Supports: US-...
Priority: must | should | could
Notes: Optional.
```

Every feature should support at least one story. If a feature supports no story, defer it or add an open question.

## Priority Guidance

- `must`: required for the plan goal to be credible.
- `should`: important, but the first plan can still succeed without it.
- `could`: useful but clearly optional.

If most stories are `must`, scope is probably too broad. Flag that in `Leader Decisions`.

## Decision Points

Use Decision Points to focus human review. Good decision points include:

- Priority boundaries.
- Scope cuts.
- Stories inferred from Key Journeys.
- Features that might be out of scope.
- Open questions that block wave planning.

Keep them concise and concrete.

## Quality Bar

A good Backlog is:

- Traceable to the Starter Spec.
- Small enough to plan in waves.
- Specific enough that `draft-wave-plan` can assign stories/features to waves.
- Free of implementation detail that will change downstream.

## Commit

When the Backlog is accepted or written to disk, commit only the relevant backlog file. Use concise messages that reference story or feature IDs when possible.

Examples:

- `Backlog: draft US-ADMIN-1..US-USER-3`
- `Backlog: defer F-4 and F-5`
