---
name: orchestrate-build
description: Run the build orchestrator: build eligible slices sequentially, invoke slice-verifier, fix/reverify defects, update state, and commit each verified slice.
---

# Orchestrate Build

Read and obey `.claude/protocol.md`.

## Preconditions

Require:

- `.project/spec.md`
- `.project/design.md`
- `.project/contracts/`
- `.project/slices/*/status.json`
- gate 1 approval recorded or explicitly confirmed
- Git repository available

If plan artifacts are missing or stubs, stop and tell the user to run `/plan`.

Only one build orchestrator may run at a time.

## Write Permissions

Build may write:

- source code;
- tests;
- current slice `status.json` (to mark `verified` or `blocked`);
- current slice `build.md`;
- future slice `boundary.md` or `acceptance.md` only for recorded necessary crossings;
- `.project/decisions.md`;
- Git commits.

Build must not write:

- current slice `verify.md`;
- contracts without gate 2 approval;
- arbitrary boundaries outside the crossing rules.

Verifier subagent writes only `verify.md`.

## Build Loop

Repeat until no eligible slice remains or a stop condition occurs.

### 1. Sync

Read:

- all slice `status.json`
- relevant `boundary.md` and `acceptance.md` for candidate slices
- `Owns` sections for the current slice and any slice whose territory may be touched

### 2. Ensure Clean Git Tree

Run:

```text
git status --short
```

If dirty before selecting a slice:

- if dirty files are only safe `.project/` cache/status updates from this command, reconcile
  and continue;
- otherwise stop and report dirty files.

Do not start a slice with unrelated uncommitted changes.

### 3. Select Slice

Eligible:

- state is `todo`;
- all dependencies are `verified`;
- no pending human decision.

Pick lowest phase first.

If none eligible:

- all slices `verified`: recommend `/integrate`;
- otherwise report blocked/todo slices and why they cannot proceed.

### 4. Preflight

For selected slice, read:

- `status.json`
- `boundary.md`
- `acceptance.md`
- relevant contracts
- latest `verify.md` if a prior verification attempt failed
- other slice `boundary.md` `Owns` sections needed to determine ownership for every expected touch

Classify expected touches:

- current slice: proceed;
- future slice: proceed only if necessary; update that slice's boundary/acceptance and log to `decisions.md`;
- verified slice: stop for gate 2 unless the change is mechanical and every affected verified
  slice can be re-confirmed by the verifier in the same build cycle; log to `decisions.md`
  either way;
- contract: stop for gate 2.

### 5. Build

Implement or fix the slice.

Run local checks useful before verifier.

Append to `build.md`:

```markdown
## Build: <slice> - <ISO timestamp>

**Intent:** <new build | fix after verification>

**Summary:**
- ...

**Commands run:**
- `<command>` - PASS | FAIL | not run (<reason>)

**Boundary/crossing notes:**
- ...

**Ready for verifier:** yes
```

### 6. Verify

Invoke the `slice-verifier` subagent with:

```text
Verify slice <slice>.
Use .project artifacts and the current Git diff as authority.
Do not rely on my informal summary.
Do not edit source, status, contracts, design, boundaries, acceptance, or build logs.
Write only .project/slices/<slice>/verify.md.
```

Read the latest verifier entry.

If the current slice mechanically touched verified-slice territory, invoke `slice-verifier`
again for each affected verified slice before committing. Tell the verifier it is checking an
affected already-verified slice against the current uncommitted diff. All affected-slice
verifications must PASS before the current slice can be committed.

### 7. Handle Verdict

PASS:

- set state `verified`;
- append any required decision entries;
- ensure any affected verified slices also have fresh PASS verifier entries when their
  territory was mechanically touched;
- commit source plus `.project/` updates:
  - `slice(<slice>): <short outcome>`
- confirm Git tree is clean;
- continue loop.

FAIL:

- if failures are implementation defects the orchestrator can resolve, fix and re-verify;
- if the orchestrator cannot resolve after reasonable attempts, set state `blocked`, append a decision entry, and stop with evidence and recommendation.

BLOCKED:

- set state `blocked`;
- append decision entry if the issue is known;
- stop with issue, evidence, options, default recommendation, and affected files/slices.

## Stop Conditions

Stop for:

- missing or unapproved plan;
- dirty Git tree before slice start;
- contract change;
- product ambiguity;
- architecture/boundary decision;
- stale state/protocol corruption;
- repeated verification failure the orchestrator cannot resolve;
- no eligible slices;
- integration ready.

When stopping for a decision, include:

- issue;
- evidence;
- options;
- default recommendation;
- exact files/slices affected.

Do not ask the human to approve individual slices.
