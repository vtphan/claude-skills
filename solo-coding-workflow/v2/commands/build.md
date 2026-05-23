---
description: Build eligible slices using the workflow protocol, invoking the slice-verifier subagent after each slice and committing each verified slice.
---

Use the `orchestrate-build` skill.

Read and obey `.claude/protocol.md`.

Assumptions:

- only one `/build` orchestrator runs at a time;
- Git is available;
- the working tree must be clean before starting each slice;
- the verifier subagent is available as `slice-verifier`;
- one verified slice should become one Git commit.

Main loop:

1. Sync `.project/` state.
2. Ensure the Git tree is clean before selecting a slice.
3. Select the next eligible slice.
4. Preflight boundary, dependencies, contracts, and previous verifier findings.
5. Implement or fix the slice.
6. Append `build.md`.
7. Invoke the `slice-verifier` subagent.
8. If verified-slice territory was mechanically touched, invoke `slice-verifier` for each
   affected verified slice too.
9. Read verifier results from `verify.md`.
10. If all required verifier invocations PASS, mark the current slice `verified`, commit the
    verified slice, and continue.
11. If FAIL with implementation defects, fix and reverify.
12. If FAIL the orchestrator cannot resolve, or BLOCKED, mark `blocked`, append `decisions.md` if appropriate, and stop for the human lead.

Stop only for protocol stop conditions in `.claude/protocol.md`.

Do not ask the human to approve individual slices.

$ARGUMENTS
