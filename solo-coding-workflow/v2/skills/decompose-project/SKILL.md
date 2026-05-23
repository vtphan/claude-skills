---
name: decompose-project
description: Convert an approved spec into slice files, contracts, boundaries, and acceptance checks. Use for /plan and gate-2 replanning.
---

# Decompose Project

Read and obey `.claude/protocol.md`.

## Preconditions

Require:

- `.project/spec.md` exists;
- gate 0 approval is recorded or the user explicitly confirms approval.

If missing, stop.

## Planning Rules

Plan is a hypothesis, not a contract.

Specify:

- interface seams;
- slice responsibilities;
- dependencies and phase order;
- contracts;
- acceptance checks;
- operational boundaries.

Do not over-specify:

- internal file structure beyond useful boundary ownership;
- implementation details build can determine safely;
- test internals unless needed for acceptance.

Prefer vertical slices by feature/resource. Do not split by technical layer unless the layer is
a real shared foundation.

Carve shared foundations first when multiple slices depend on the same resource.

## Required Outputs

### `.project/design.md`

Include:

- slice list;
- one-sentence responsibility per slice;
- phase per slice;
- dependencies;
- provided contracts;
- dependency graph;
- phase order;
- integration notes.

### `.project/contracts/api.yaml`

Create `.project/contracts/api.yaml` only when the project exposes or consumes an API.
For non-API projects, create the smallest contract files that capture real seams, or leave
`contracts/` empty and state in `design.md` that no external contract is needed yet.

For API projects, use real OpenAPI YAML. Every endpoint must specify:

- method;
- path;
- auth;
- request body/params;
- response body by status code;
- shared error shape;
- pagination for unbounded lists.

Add other contract files only when needed.

### Per-Slice Files

For each slice create:

```text
.project/slices/<slice>/
  status.json
  boundary.md
  acceptance.md
  build.md
  verify.md
```

`status.json`:

```json
{
  "slice": "<slice>",
  "state": "todo",
  "phase": 1,
  "depends_on": []
}
```

State values: `todo`, `verified`, `blocked`.

`boundary.md`:

```markdown
# Boundary: <slice>

## Owns
- <files/modules/resources this slice may change>

## May use
- <contracts/resources it may depend on but not redefine>

## Off limits
- <specific dangerous or forbidden areas>

## Crossing notes
- None yet.
```

`acceptance.md`:

```markdown
# Acceptance: <slice>

## Criteria
- ...

## Checks
- `<command>` - <what it proves>
```

Use concrete check commands when known. If not known, write observable acceptance criteria.

`build.md` and `verify.md` start empty.

Optional `.project/boundaries.md` may summarize all boundaries, but per-slice `boundary.md`
is authoritative.

## Gate 1

Stop after producing artifacts.

Present:

- slices and dependency graph;
- foundation slices;
- key contract decisions;
- deliberate looseness;
- risks and assumptions;
- recommendation for approval or edits.

Do not build.

After human approval:

- append gate 1 approval to `.project/decisions.md`;
- commit the approved plan artifacts with `project: approve plan`;
- tell the user to run `/build`.

Follow the gate approval rule in `.claude/protocol.md`.

## Gate 2 Replanning

The canonical gate-2 procedure lives in `commands/contract-change.md`. This skill is invoked
from within that procedure (step 4) when the approved change is structural enough to require
replanning — for example: introducing or merging slices, restructuring dependencies, or
adding new contracts.

When invoked for replanning:

1. Read the blocking slice files, relevant contracts, and the recorded decision.
2. Apply the minimal planning changes: update `design.md`, contracts, and the affected
   slices' `boundary.md` / `acceptance.md` / `status.json` (creating or removing slice
   directories as needed).
3. Return control to `/contract-change`, which handles `decisions.md` append, commit, and
   user report.

Do not duplicate the gate-2 stop, the human-decision step, or the commit — those belong to
`/contract-change`.
