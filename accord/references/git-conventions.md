# ACCORD Git Conventions

Git is part of ACCORD's process state. Commits and lightweight tags mark approved phase boundaries and make cross-conversation handoff precise.

If git is unavailable, save artifacts normally and warn that later review has a weaker baseline.

## Commit Prefixes

- `intent:`
- `design:`
- `plan:`
- `exec:`
- `review:`

## Tags

Use lightweight tags:

- `accord-intent-v<N>`
- `accord-design-v<N>`
- `accord-plan-v<N>`
- `accord-exec-<unit-id>`
- `accord-review-<unit-id>`

Increment version tags when canonical `intent.md`, `design.md`, or `plan.md` is promoted again.

## Commit Rules

- Commit only after human approval.
- Commit explicit paths only.
- Never sweep unrelated user work into a phase commit.
- If the working tree has unrelated dirty files, stop and ask how to proceed.
- Include enough commit body detail to name the approved artifact, source draft if applicable, decisions, scope, and evidence.
- Do not create or move tags silently if a target tag already exists.

## Suggested Messages

```text
intent: approve project intent

Promotes docs/accord/intent/draft_02.md to docs/accord/intent/intent.md.
Updates docs/accord/accord-state.md.
Tag: accord-intent-v1
```

```text
design: approve architecture and decisions

Promotes docs/accord/design/draft_04.md to docs/accord/design/design.md.
Key decisions: D-001 persistence, D-002 deployment.
Tag: accord-design-v1
```

```text
exec: implement auth-login

Implements approved unit auth-login.
Report: docs/accord/reports/exec-auth-login.md.
Tag: accord-exec-auth-login
```
