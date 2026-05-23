---
description: Turn the approved spec into a build plan: slices, contracts, and per-slice operational files.
---

Use the `decompose-project` skill.

Read:

- `.claude/protocol.md`
- `.project/spec.md`

If `.project/spec.md` is missing or unapproved, stop and ask for gate 0 approval.

Produce:

- `.project/design.md`
- `.project/contracts/<contract files as needed>`
- `.project/slices/<slice>/status.json`
- `.project/slices/<slice>/boundary.md`
- `.project/slices/<slice>/acceptance.md`
- `.project/slices/<slice>/build.md`
- `.project/slices/<slice>/verify.md`
- optional `.project/boundaries.md`

Use per-slice files as the operational source of truth.

Stop for gate 1 approval. Do not build.

After approval:

- append the approval to `.project/decisions.md`;
- commit the approved plan artifacts with `project: approve plan`;
- tell the user the next step is `/build`.

Follow the gate approval rule in `.claude/protocol.md`.

$ARGUMENTS
