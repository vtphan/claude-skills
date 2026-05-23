---
description: Handle gate 2 contract/product/architecture changes and return affected slices to todo for rebuild.
---

Read and obey `.claude/protocol.md`.

Use this only when build or verifier stops for a decision-required contract, product, boundary,
or architecture issue.

This command is the canonical gate-2 procedure. If the change is structural enough to require
replanning (new slices, restructured boundaries, new contracts), use the `decompose-project`
skill to apply the planning portion within step 4 below, then continue.

Procedure:

1. Read the blocking slice's `build.md`, `verify.md`, boundary, acceptance, and relevant
   contracts.
2. Present the human lead with:
   - issue;
   - evidence;
   - options;
   - default recommendation;
   - affected contracts/slices.
3. Wait for the human decision.
4. Apply the minimal approved change. For structural replanning, invoke `decompose-project`.
5. Append the decision to `.project/decisions.md`.
6. Mark affected verified slices back to `todo` so `/build` rebuilds and re-verifies them.
   Record what changed for each in `decisions.md`.
7. Mark blocked slices `todo` if the decision unblocks them.
8. Commit the approved change with `project: approve contract change`.
9. Report the delta and next `/build` action.

Follow the gate approval rule in `.claude/protocol.md`: if the user gives gate 2 approval in this
same conversation, record and commit the approved change before ending; otherwise stop
without recording or committing gate 2 approval.

Do not proceed to implementation after the contract change unless the user explicitly asks to
continue.

$ARGUMENTS
