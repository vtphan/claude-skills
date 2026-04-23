# Rolling-Wave Plan Schema

This file is the shared contract between the three planning skills:

- `phase-plan-draft` — writes the first version of the plan from a requirements document.
- `phase-plan-execute` — reads the plan and implements the current phase, producing a report.
- `phase-plan-update` — reads the plan + report and advances the plan to the next phase.

All three skills must read, write, and interpret the plan in exactly the way this document specifies. If a skill needs information that isn't in the schema, either the schema is wrong (update it here first) or the skill is overreaching (pull it back).

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Top-level structure](#3-top-level-structure)
4. [Per-phase structure](#4-per-phase-structure)
5. [Assumptions register](#5-assumptions-register)
6. [Risks register](#6-risks-register)
7. [Change log](#7-change-log)
8. [Implementation report template](#8-implementation-report-template)
9. [Invariants — rules all three skills must honor](#9-invariants)
10. [Worked mini-example](#10-worked-mini-example)

---

## 1. Philosophy

Rolling-wave planning exists because later-phase certainty is an illusion. The further ahead we plan, the more our plan is speculation dressed up as detail. The discipline says: **plan the near term comprehensively, sketch the far term concisely, and commit to learning between phases**.

This schema enforces that discipline through its structure. It is deliberately harder to over-plan a future phase than to sketch it, and deliberately harder to silently expand scope than to flag a discovery.

Three operating principles thread through the schema:

**One source of truth.** The plan file is the single place where project state lives. If a skill needs to know something, it reads the plan. If a skill learns something, it writes to the plan. No parallel docs.

**Every claim is traceable.** Phases cite the requirements they cover. Tasks cite the acceptance criteria they satisfy. Updates cite the assumptions they validated or broke. A reader should be able to walk backward from any statement to its origin.

**Surprises are first-class.** Discoveries during execution are the point, not a failure. The schema has a dedicated place to record them at every level — per-task, per-phase, per-plan — so they can't be buried.

## 2. File format and location

One markdown file per project, named `<project-slug>-plan.md`. The file sits alongside the requirements document it was drafted from, typically in the project's `docs/` directory.

YAML frontmatter holds machine-parseable state. The markdown body holds human-and-agent-readable detail. No other files, no splits, no sidecars.

```yaml
---
plan_version: 3                         # Incremented by each update pass
created: 2026-04-22                     # ISO date, never changes
last_updated: 2026-04-28                # ISO date, updated every pass
source_requirements: bookclub-requirements.md
current_phase: P2                       # The phase currently being executed
status: in_progress                     # in_progress | complete | paused | pivoted
---
```

`status` values:
- `in_progress` — normal operating state.
- `complete` — all phases closed out; no further work planned.
- `paused` — deliberately halted; requires human input before resuming.
- `pivoted` — an update pass rewrote the plan substantially; the old phase IDs may have been retired. The change log entry explains.

## 3. Top-level structure

Below the frontmatter, the plan contains seven numbered sections, always in this order:

```markdown
# <Project> — Implementation Plan

## 1. Goal and guardrails
## 2. Requirements coverage
## 3. Phases overview
## 4. Phases (detailed)
## 5. Assumptions register
## 6. Risks register
## 7. Change log
```

### 1. Goal and guardrails

Two or three short paragraphs restating why we're building this, what success looks like, and explicit non-goals. Drawn from the requirements doc's Context and Open Questions. This section is load-bearing: it's what the executor reads to sanity-check whether a proposed piece of work is in scope.

### 2. Requirements coverage

A compact table mapping requirements-doc IDs (stories and features) to the phases that deliver them, plus a "Deferred" row for requirements the plan explicitly chooses not to address.

```markdown
| Requirement | Delivered by | Notes |
|-------------|--------------|-------|
| US-ORG-1    | P1           |       |
| US-ORG-2    | P1, P2       | Split: basic in P1, polish in P2 |
| US-MEM-3    | Deferred     | Depends on F-7, out of MVP scope |
| F-1         | P1           |       |
```

If a story or feature isn't in this table at all, the plan has a coverage gap and the update skill should flag it.

### 3. Phases overview

A one-glance summary: the phase ladder.

```markdown
| Phase | Name                         | Status      | One-line goal |
|-------|------------------------------|-------------|---------------|
| P1    | Club setup and invites       | complete    | A club exists with members. |
| P2    | Nomination and voting flow   | in_progress | Members can pick the next book. |
| P3    | Scheduling and RSVPs         | future      | A meeting is on the calendar. |
| P4    | Shared notes and archive     | future      | Meetings produce durable artifacts. |
```

### 4. Phases (detailed)

One subsection per phase, in order. Format depends on whether the phase is `past`, `current`, or `future` — see [Section 4](#4-per-phase-structure).

### 5. Assumptions register

See [Section 5](#5-assumptions-register).

### 6. Risks register

See [Section 6](#6-risks-register).

### 7. Change log

See [Section 7](#7-change-log).

## 4. Per-phase structure

Every phase uses the same skeleton. The **depth** of each field depends on the phase's status. This is how the schema makes rolling-wave discipline structural rather than aspirational.

### Common fields (all phases)

```markdown
### P<N> — <Phase name>
Status: future | in_progress | complete | pivoted | deferred
Goal: One sentence — what capability this phase delivers.
Covers: US-..., F-...   (requirements-doc IDs from Section 2)
Depends on: P<N-1>, P<N-2>, or "none"
```

### Future phases (sketches)

A future phase also carries:

```markdown
Entry criteria: One or two sentences — what must be true before this phase starts.
Exit criteria: What "done" looks like, stated as testable outcomes. 2-5 bullets.
Assumptions: A<N>, A<N>   (references to entries in Section 5)
Risks: R<N>               (references to Section 6)
Sketch: 2-4 sentences describing approach at a high level.
```

No task breakdown. No acceptance criteria per task. No implementation detail. **Task-level detail for a future phase is speculative work and is forbidden by the schema.** If the update skill finds itself wanting to pre-plan tasks for a future phase, it's crossing the rolling-wave line.

### Current phase (fully planned)

A current phase has everything a future phase has, plus:

```markdown
Started: 2026-04-28   (ISO date, set when the phase becomes current)

#### Tasks
- [ ] T<N>.1 — <short task description>
      Acceptance: <one or two concrete conditions that prove the task is done>
      Touches: <files/modules/components, optional>
- [ ] T<N>.2 — ...
```

Guidelines for tasks:

- **Acceptance criteria are mandatory, not optional.** A task without acceptance criteria can't be closed out honestly. The draft and update skills must refuse to produce one.
- **Keep tasks small enough to close in one sitting.** If a task is larger than a day's work, split it. Large tasks are the loophole rolling-wave exists to prevent.
- **Tasks cite the stories/features they advance.** If a task doesn't serve a requirement, either it's implicit plumbing (fine, say so) or it's scope creep (flag it).

Checkbox state (`[ ]` / `[x]`) is the single source of truth for task status. The executor skill marks tasks complete as it finishes them.

### Past phases (closeout)

When a phase completes, its detailed plan is replaced by a compact closeout summary. The task list is removed (the report archives it); what remains is the learning.

```markdown
### P<N> — <Phase name>
Status: complete | pivoted | deferred
Completed: 2026-04-27
Covers: US-..., F-...
Delivered: Short prose — what this phase actually produced, independent
  of what was planned. A reader should be able to see the shape of what
  was built without opening any other file.
Assumptions resolved: A<N> validated | A<N> broken → A<N+1> opened
Report: <path to the report file>   (link to the archived report)
```

## 5. Assumptions register

A flat list, top of the plan as a stable reference. Phases and tasks reference these by ID.

```markdown
## 5. Assumptions register

- **A1** — Club sizes stay under ~20 members. *Phase: P1. Status: untested.*
- **A2** — Voting is single-choice per member, not ranked. *Phase: P2. Status: untested.*
- **A3** — Magic-link auth is acceptable for guest access. *Phase: P1. Status: validated (2026-04-25).*
- **A4** — Members are reachable via email; SMS is not required. *Phase: P2. Status: broken — superseded by A6.*
- **A6** — Members prefer ranked-choice voting over single-choice. *Phase: P2. Status: open.* Replaces: A2.
```

Status values: `untested` | `validated` | `broken` | `open` (a new assumption not yet exercised).

Rules:

- **Never delete an assumption.** If it's wrong, mark it broken and open a replacement with a new ID. The history matters — it explains why the plan looks the way it does.
- **Every assumption cites the phase it belongs to.** Assumptions floating free of phases are a yellow flag.
- **Status changes are dated.** When the executor or updater marks an assumption validated or broken, include the date.

## 6. Risks register

Same flat-list structure as assumptions, with mitigation instead of status.

```markdown
## 6. Risks register

- **R1** — Poll-open notifications may be delayed by email provider.
  *Phase: P2. Likelihood: medium. Impact: medium.*
  *Mitigation: in-app badge as primary signal, email as secondary.*
- **R2** — Guest magic-links may expire before a meeting ends.
  *Phase: P1. Likelihood: low. Impact: low.*
  *Mitigation: TTL of 24h past meeting end; allow organizer to reissue.*
```

Phases reference risks by ID in their `Risks:` field. When a risk materializes during execution, the executor reports it; the updater promotes it to the current state (e.g., updates the mitigation or marks the risk "triggered — resolved by R1-mitigation").

## 7. Change log

Append-only. One entry per plan update pass. The updater skill writes one entry per invocation — even if the update was minimal — so the history is complete.

```markdown
## 7. Change log

### 2026-04-28 — Update after P2 closeout
Type: normal-update
- Closed P2. All exit criteria met.
- A2 (single-choice voting) marked broken based on report observation;
  opened A6 (ranked-choice). Impacts P2 data model — see P2 closeout notes.
- Expanded P3 sketch into full plan. current_phase advanced to P3.
- Re-sketched P4 to account for ranked-voting data shape.

### 2026-04-25 — Update after P1 closeout
Type: normal-update
- Closed P1. All exit criteria met except "offline sync for guest links"
  — deferred to P4 (was out of scope anyway).
- A3 validated.
- current_phase advanced to P2.

### 2026-04-22 — Plan created
Type: initial-draft
- Drafted from bookclub-requirements.md (v2, human-revised).
- Four phases, P1 fully planned, P2-P4 sketched.
- 8 assumptions and 4 risks seeded from the requirements' Open Questions.
```

`Type` values:
- `initial-draft` — the first write of the plan by phase-plan-draft.
- `normal-update` — a routine update: one phase closed, next phase planned, minor register updates.
- `substantial-replan` — multiple assumptions broken, multiple future phases materially changed. Plan still coherent.
- `pivot` — the forward plan was rewritten. Retired phase IDs are listed; new phase IDs may appear. The plan's frontmatter `status` is set to `pivoted` until an execute/update cycle completes.

## 8. Implementation report template

The executor skill produces a report at the end of each phase. The updater skill reads it. The report lives alongside the plan as `<project-slug>-plan.reports/phase-P<N>-report.md`.

```markdown
# P<N> <Phase name> — Implementation Report
Phase: P<N>
Completed: 2026-04-28
Plan version at start: 2

## What was built
Prose summary of the actual outcome — what a user could now do that
they couldn't before. Reference completed task IDs. This is not a
changelog of commits; it's a summary of capability delivered.

## Task status
- [x] T2.1 — Schema for nominations and votes. Done.
- [x] T2.2 — Nomination UI. Done.
- [x] T2.3 — Voting UI with tie-break path. Done.
- [~] T2.4 — End-to-end test. Partial: covers nominate and vote but not
       tie-break. Tie-break E2E deferred to P3.

## Assumptions status
- A1: validated — 30-member synthetic club performs fine.
- A2: broken — user testing showed strong preference for ranked voting;
  single-choice felt arbitrary. Recommend replacing with A6 (ranked).

## Discoveries
Things learned during execution that weren't known at phase start.
Focus on anything that affects later phases or the plan's assumptions.
Be specific — not "voting is more complex than we thought" but
"ranked-choice voting requires per-member vote-order storage, which
will change the P3 schedule UI because scheduling inherits the voter
list from the current poll."

## Proposed scope changes
Explicit, bulleted — each with one-line rationale.
- Add to P3: migration from single-choice to ranked data model.
- Remove from P4: shared-notes emoji reactions — didn't come up once in
  testing, and the current scope is already large.
- Defer to later: dark mode for voting UI.

## Risks encountered
- R1 (poll notification delay) did not materialize.
- New risk: ranked-choice ties can produce multi-way deadlocks; needs
  a tie-break rule. Opening as R3 in the registry.

## Readiness for next phase
Prerequisites the next phase needs that weren't originally planned, or
that need to happen before the next phase can start cleanly.
```

A report section may be omitted **only** if it would be empty — e.g., "Assumptions status" can be omitted if the phase had no assumptions. Omitting a section with content is a schema violation.

## 9. Invariants

Rules every skill must honor. Violating one is a schema-level bug, not a judgment call.

1. **The plan file is the single source of truth.** Skills do not maintain parallel state.
2. **Future phases never get task-level detail.** Tasks live only in the current phase. This is the rolling-wave discipline — if a skill pre-plans tasks for a future phase, it has failed.
3. **Every task has acceptance criteria.** A task without acceptance can't be honestly closed out.
4. **Every phase has exit criteria.** A phase can't be closed out without them.
5. **Requirements coverage is complete or explicitly deferred.** Every story/feature in the requirements doc appears in Section 2 — either assigned to a phase or in the Deferred row with a reason.
6. **Assumptions are never deleted.** If wrong, mark broken and open a replacement. The history is the context.
7. **The change log is append-only.** Entries are never rewritten, even if superseded by later entries.
8. **Reports do not modify the plan.** Only the updater skill modifies the plan. The executor writes the report; the updater interprets it.
9. **Scope expansion requires an explicit change-log entry.** If an update adds work that wasn't in scope before, it's called out by name and rationale — never silently absorbed.
10. **Pivots bump frontmatter status to `pivoted`.** The next successful execute/update cycle clears it back to `in_progress`. This keeps pivots visible.

## 10. Worked mini-example

A tiny plan for a CLI tool that tags files by content. Shown here in full to make the schema concrete end-to-end.

```markdown
---
plan_version: 2
created: 2026-04-22
last_updated: 2026-04-26
source_requirements: filetagger-requirements.md
current_phase: P2
status: in_progress
---

# filetagger — Implementation Plan

## 1. Goal and guardrails
A local CLI that reads files in a directory and attaches content-derived
tags (topic, sentiment, language) as xattrs or a sidecar index. Non-goals:
no cloud sync, no GUI, no write-back into file contents.

Success: a user can run `filetagger scan ~/Documents` and then
`filetagger find topic:invoices` and get accurate results in under
two seconds for 10k files.

## 2. Requirements coverage
| Requirement | Delivered by | Notes |
|-------------|--------------|-------|
| US-USR-1 (scan directory) | P1 | |
| US-USR-2 (find by tag)    | P2 | |
| US-USR-3 (re-scan changes)| P3 | |
| F-1 (tagging engine)      | P1 | |
| F-2 (query engine)        | P2 | |
| F-3 (watch mode)          | Deferred | Out of MVP; low user demand in validation. |

## 3. Phases overview
| Phase | Name                    | Status       | One-line goal |
|-------|-------------------------|--------------|---------------|
| P1    | Scan and tag            | complete     | Files get tagged into a local index. |
| P2    | Query by tag            | in_progress  | User can find files by tag combinations. |
| P3    | Incremental re-scan     | future       | Re-scans only touch changed files. |

## 4. Phases (detailed)

### P1 — Scan and tag
Status: complete
Completed: 2026-04-25
Covers: US-USR-1, F-1
Delivered: `filetagger scan <dir>` walks a directory, extracts content,
  calls an LLM tagger, and writes results to a SQLite index at
  `~/.filetagger/index.db`. Tested on 5k mixed files; mean 120ms/file.
Assumptions resolved: A1 validated; A2 broken → A3 opened.
Report: filetagger-plan.reports/phase-P1-report.md

### P2 — Query by tag
Status: in_progress
Started: 2026-04-25
Goal: User can run `filetagger find <query>` and get matching paths.
Covers: US-USR-2, F-2
Depends on: P1
Entry criteria: P1 index format stable; index populated.
Exit criteria:
- `filetagger find topic:X` returns exact matches.
- Boolean queries (`topic:X AND lang:en`) parse and execute.
- Query on 10k-file index completes in under 2s on a laptop.
Assumptions: A3, A4
Risks: R1

#### Tasks
- [x] T2.1 — Query parser for tag:value and AND/OR/NOT.
      Acceptance: unit tests cover all operator combinations; syntax
      errors produce clear messages citing column position.
- [x] T2.2 — Query executor against SQLite index.
      Acceptance: returns correct matches for the parser's AST;
      benchmark on synthetic 10k-file index shows < 2s p95.
- [ ] T2.3 — CLI surface for `find` subcommand.
      Acceptance: `filetagger find` shows help; arg parsing errors exit
      non-zero; output is one path per line by default, JSON with --json.
- [ ] T2.4 — End-to-end test across tag + find.
      Acceptance: Playwright-style script tags a fixture directory and
      finds the same files; passes in CI.

### P3 — Incremental re-scan
Status: future
Goal: Only re-tag files that changed since last scan.
Covers: US-USR-3
Depends on: P1, P2
Entry criteria: Query engine stable enough that re-scan correctness can be verified by query.
Exit criteria:
- `filetagger scan --incremental <dir>` re-tags only changed/new files.
- A full re-scan after small edits completes 10x faster than a cold scan.
Assumptions: A5
Risks: R2
Sketch: Compare mtime + size + xattr-recorded hash to decide whether to re-tag. Falls back to full scan if index schema changed.

## 5. Assumptions register

- **A1** — SQLite is fast enough for 10k-file indexes on a laptop. *Phase: P1. Status: validated (2026-04-25).*
- **A2** — One tag set per file (flat). *Phase: P1. Status: broken (2026-04-23) — users want multi-set (personal + work).* Superseded by A3.
- **A3** — Tags live in a flat namespace; users differentiate via prefix (e.g. `work/topic:X`). *Phase: P1, P2. Status: validated (2026-04-25).*
- **A4** — Query latency is dominated by SQLite, not by LLM calls (queries don't call the tagger). *Phase: P2. Status: untested.*
- **A5** — File mtime + size is a reliable change signal (false negatives are rare enough to ignore). *Phase: P3. Status: open.*

## 6. Risks register

- **R1** — Boolean query parser may misinterpret user intent on ambiguous queries. *Phase: P2. Likelihood: medium. Impact: low.* *Mitigation: echo parsed AST on `--explain`; document precedence.*
- **R2** — Filesystems without mtime precision (some FUSE mounts) break incremental scan. *Phase: P3. Likelihood: low. Impact: medium.* *Mitigation: detect and fall back to full scan with a warning.*

## 7. Change log

### 2026-04-26 — Update after P1 closeout
Type: normal-update
- Closed P1. All exit criteria met.
- A2 broken during P1; A3 opened and validated in the same phase after
  refactoring tag namespace to be string-prefixed.
- Expanded P2 sketch into full plan. current_phase advanced to P2.
- Re-sketched P3 briefly to confirm the re-scan logic works against the
  new string-prefixed tag namespace.

### 2026-04-22 — Plan created
Type: initial-draft
- Drafted from filetagger-requirements.md.
- Three phases, P1 fully planned, P2-P3 sketched.
- 5 assumptions and 2 risks seeded from requirements Open Questions.
```
