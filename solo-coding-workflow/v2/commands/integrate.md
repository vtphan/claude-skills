---
description: Wire verified slices into a working system, check seams and obsolescence, run full checks, and stop for gate 3 approval.
---

Read and obey `.claude/protocol.md`.

Preconditions:

- `.project/spec.md`, `.project/design.md`, contracts, and slice files exist.
- All required slices are `verified`, or the user explicitly names a smaller integration
  target.
- Git working tree is clean.

## Procedure

### 1. Sync state and as-built scope

Read:

- `.project/spec.md`
- `.project/design.md`
- `.project/contracts/*`
- `.project/decisions.md` — the as-built scope can diverge from the original plan because of
  gate-2 changes and recorded crossings
- each verified slice's `boundary.md` and `acceptance.md`

Confirm required slices are `verified` and the tree is clean.

### 2. Obsolescence pass

For each verified slice, confirm its behavior is actually reached by the integrated system.
A slice can become obsolete because:

- a gate-2 decision superseded it;
- another slice absorbed its responsibility via a recorded crossing;
- the original plan over-decomposed and integration uses a thinner subset.

For each obsolete slice, stop and present to the human lead: which slices appear unused,
why, and the options (delete, keep as dead code, keep for a documented future use). Do not
silently drop slices.

### 3. Seam conformance pass

For each pair of slices that meet at integration:

- consumer uses producer only through the contract declared in `.project/contracts/` or in
  the producer's `boundary.md` (no reaching past the seam);
- request/response shapes, error shapes, auth, and pagination match between consumer and
  producer;
- any seam not covered by a contract is recorded as a gap — either add the contract now (as
  a gate-2 change) or record it in `decisions.md` as a known omission.

Report seam-conformance findings before applying integration changes.

### 4. Apply integration changes

Wire slices together: top-level entry points, routing, dependency injection, configuration,
infrastructure glue, and any system-level setup not owned by an individual slice.

### 5. Verified-slice-territory rule

If integration must touch a verified slice's territory, classify whether this is
integration-only wiring or substantive enough to require rebuild. If rebuild is required,
mark the affected slice back to `todo`, record the reason in `decisions.md`, and re-verify
before gate 3.

### 6. Run full checks

Run the full test suite and every end-to-end flow named in `spec.md`. List each flow's
verdict.

### 7. System-level verification

Invoke the `integration-reviewer` subagent for system-level review when the integration is
non-trivial. Pass it the spec, design, decisions, contracts, verified slice files, check
output, and the integration diff.

Handle the reviewer verdict before gate 3:

- `PASS`: proceed to the gate 3 report.
- `FAIL`: address the findings, rerun relevant checks, and rerun system-level verification
  before presenting gate 3.
- `BLOCKED`: stop with the decision required, evidence, options, default recommendation, and
  affected files/slices.

### 8. Gate 3

Present:

- changes applied;
- seam-conformance findings;
- obsolescence findings;
- test and end-to-end flow results;
- risks;
- decision required.

Stop for human approval.

## After approval

- append gate 3 approval to `.project/decisions.md`;
- commit integration changes with `integrate: <short outcome>` if changes are not already
  committed.

Follow the gate approval rule in `.claude/protocol.md`.

$ARGUMENTS
