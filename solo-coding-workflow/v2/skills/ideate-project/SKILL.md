---
name: ideate-project
description: Turn a rough software idea into an approved project spec and scaffold .project. Use for /ideate or when no spec exists.
---

# Ideate Project

Run ideation until `.project/spec.md` is strong enough for planning.

## Role

Act as a thinking partner. Push on weak problem statements, oversized scope, vague users,
unowned risks, and features that do not trace to the problem.

Ask one question at a time.

## Checklist

Maintain the checklist during the conversation. If filesystem access exists, persist it at
`.project/ideation.md`.

States:

- `open`
- `settled`
- `deferred`

Core items:

- specific users
- painful current workaround
- consequence if unsolved
- thinnest useful version
- explicit out-of-scope list
- core nouns/resources
- key user flows
- state ownership at structural level
- risks and dispositions: `confront`, `defer`, or `spike`
- trace-back: every in-scope item supports the problem

Do not write the final spec while core items remain `open`. The user may explicitly defer
items, but record the deferral.

If a central unknown requires code to understand, mark it `spike` and do not write a confident
implementation spec.

## Spec Output

Write `.project/spec.md`:

```markdown
# <Project name>

## Problem
<users, workaround, consequence>

## Thinnest useful version
<smallest useful version>

## In scope
- ...

## Explicitly out of scope
- ...

## Shape
<core nouns/resources, key flows, where state lives; structural only>

## Risks and dispositions
- <risk> - confront | defer | spike

## Open / deferred items
- ...
```

Spec rules:

- firm on what and why;
- loose on implementation details;
- no endpoints, schemas, file layouts, or slice decomposition;
- no planning content.

## Gate 0

Stop for human spec approval.

After approval, scaffold:

```text
.project/
  spec.md
  design.md
  decisions.md
  contracts/
  slices/
```

Stub contents:

- `.project/design.md`: `# Design\n\n_Pending /plan._`
- `.project/decisions.md`: append gate 0 approval entry.

Decision entry:

```markdown
## <ISO timestamp> - Gate 0 spec approval

- Decision: Spec approved.
- Reason: <one-sentence summary>
- Affected slices: none
```

Commit the approved spec and scaffold:

```text
project: approve spec
```

End by telling the user to run `/plan`.

Follow the gate approval rule in `.claude/protocol.md`.
