---
description: Recovery/debug command to manually run verification for a slice using the same verifier rules as /build.
---

Manual fallback only. Normal verification is invoked by `/build` through the `slice-verifier`
subagent.

Read and obey `.claude/protocol.md`.

Use the `slice-verifier` subagent to verify the requested slice or the slice most recently
worked on by `/build`. The verifier can also re-confirm an already-verified slice whose
territory was mechanically touched by another slice; when doing that, tell it the triggering
current slice name so it records `Mode: affected-slice`.

Rules:

- Do not edit source code.
- Do not edit contracts, design, boundaries, acceptance files, or status.
- Verifier writes only `.project/slices/<slice>/verify.md`.
- Report the verdict to the user.
- If a state transition is needed, instruct the user to resume `/build`; do not perform build
  orchestration here unless explicitly asked.

$ARGUMENTS
