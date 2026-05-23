---
description: Produce an approved project spec and scaffold .project.
---

Use the `ideate-project` skill.

Requirements:

- Produce `.project/spec.md`.
- Do not produce design, slice, boundary, or contract content.
- Stop for gate 0 spec approval.
- After approval, scaffold the `.project/` structure with stubs:
  - `.project/design.md`
  - `.project/decisions.md`
  - `.project/contracts/`
  - `.project/slices/`
- Append the gate 0 approval to `.project/decisions.md`.
- Commit the approved spec and scaffold with `project: approve spec`.
- Tell the user the next step is `/plan`.

Follow the gate approval rule in `.claude/protocol.md`.

$ARGUMENTS
