# FBRA Wave Doc Schema

This schema supports a one-human, one-smart-LLM workflow:

- `frame` creates or reshapes the wave doc.
- `build` implements the active wave.
- `revise` reviews what changed and updates the active wave if needed.
- `advance` closes a done wave and activates the next one.

The wave doc is a steering surface, not a compliance artifact. Keep it short enough that the human will actually read it.

## File

Use one markdown file per project, usually `docs/<project-slug>-waves.md`.

```yaml
---
wave_doc_version: 1
created: 2026-04-24
last_updated: 2026-04-24
current_wave: W1
status: active
---
```

## Required Sections

```markdown
# <Project> - Waves

## Goal
## Operating Rules
## Waves
## Decisions
## Notes
```

## Goal

One to three paragraphs describing the product goal, intended users, and explicit non-goals.

## Operating Rules

Short project-wide rules for the LLM:

- Implementation freedom: what the LLM may decide independently.
- Decision boundary: when the LLM must ask the human.
- Verification bar: what must be tested or demonstrated before work is called done.

Default decision boundary:

> The LLM may choose implementation details that are local, reversible, and consistent with existing patterns. Ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.

Default verification bar:

> Verify every active-wave must-have requirement with the cheapest credible automated test, scripted check, or manual demo. Run relevant existing tests. Report anything not verified.

## Waves

Each wave has exactly one state:

- `inactive` - future direction, concise.
- `active` - current build scope, detailed enough for execution.
- `done` - completed summary.

Normal state: exactly one wave is `active`. Transitional states may briefly have zero active waves before the first wave is framed, after the project is complete, while the human is reorganizing the doc, or during a deliberate pause. Never have more than one active wave.

### Inactive Wave

```markdown
### W<N> - <Name>
Status: inactive
Goal: One sentence.

Must-have stories:
- ...

Must-have features:
- ...

Notes:
- Optional constraints, dependencies, or known questions.
```

Inactive waves do not have tasks, detailed implementation plans, formal acceptance criteria, or verification commands.

### Active Wave

```markdown
### W<N> - <Name>
Status: active
Goal: One sentence.

Must-have requirements:
- ...

Nice-to-have:
- ...

Implementation notes:
- Existing patterns, constraints, or guidance the LLM should respect.

Tasks:
- [ ] ...

Decisions needed:
- None currently.

Verification:
- Automated: ...
- Manual/demo: ...
- Commands: ...
```

Rules for active waves:

- Must-have requirements are binding. If unmet, the wave is not done.
- Nice-to-have items are optional and must not distort the wave.
- Tasks may be adjusted by the LLM while building if the requirements stay stable.
- The LLM must ask before crossing the decision boundary.
- Verification must be credible, not necessarily exhaustive.

### Done Wave

```markdown
### W<N> - <Name>
Status: done
Completed: 2026-04-24

Delivered:
- ...

Stories completed:
- ...

Features completed:
- ...

Decisions established:
- ...

Follow-up notes:
- ...
```

Done waves keep only durable project memory. Remove task-level detail unless it matters later.

## Decisions

Use this as a compact decision log. Add only decisions that future work should respect.

```markdown
- 2026-04-24 - Use SQLite for local persistence because deployment is single-user and local-first.
```

Do not turn this into a full architecture decision record system unless the project needs it.

## Notes

Use for open questions, deferred ideas, and things that belong to the product vision but are not yet waved.

## Invariants

1. Keep exactly one active wave during normal Build/Revise/Advance work. Zero active waves is only a transitional state. Never have more than one active wave.
2. Inactive waves stay concise.
3. Active waves include must-have requirements and verification.
4. Done waves summarize shipped capability and durable decisions.
5. The LLM asks before crossing the decision boundary.
6. If verification was not run or did not pass, say so plainly.
