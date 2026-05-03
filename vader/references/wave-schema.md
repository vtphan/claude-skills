# Wave Plan Schema

The wave plan is the central operating artifact of the **VADER** loop. It unifies requirements and plan into a single rolling document, organized wave by wave. The current wave is specified and planned in full; future waves are sketched as themes; past waves carry compact closeout summaries.

This schema is the contract for three skills:

- `wave-plan` — writes the first version of the wave plan from the vision and architecture.
- `wave-execute` — implements the current wave's tasks and produces an execution report.
- `wave-update` — closes the current wave, ratifies any architectural changes proposed by its review subagent, expands the next wave, and writes a change-log entry that captures both findings and decisions.

`wave-update` is the per-cycle hub. It runs an internal review subagent (fresh context, reads only artifacts) to produce findings, presents them interactively to the human for approval, applies any architectural changes, expands the next wave, and saves everything atomically. There is no separate review report — findings live in the change-log entry.

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Top-level structure](#3-top-level-structure)
4. [Per-wave structure](#4-per-wave-structure)
5. [Assumptions register](#5-assumptions-register)
6. [Risks register](#6-risks-register)
7. [Decision Log references](#7-decision-log-references)
8. [Change log](#8-change-log)
9. [Execution report template](#9-execution-report-template)
10. [Pivot handling](#10-pivot-handling)
11. [Invariants](#11-invariants)
12. [Worked mini-example](#12-worked-mini-example)

---

## 1. Philosophy

Rolling-wave development exists because later-wave certainty is an illusion. The further ahead we specify and plan, the more the document is speculation dressed up as detail. The discipline says: **specify and plan the current wave comprehensively, sketch future waves concisely, execute one wave at a time, and commit to learning between waves**.

VADER's simplified loop has two skills per cycle:

- `wave-execute` builds the current wave's tasks and produces an execution report.
- `wave-update` reviews what happened (via a fresh-context subagent), surfaces findings to the human for approval, applies any architectural changes, closes the current wave, expands the next wave's sketch into full detail.

Three operating principles thread through the schema:

**Current in detail, future in sketch.** Future waves carry only titles, themes, sketches, and sketched criteria. Anything beyond that is a schema violation.

**Every claim is traceable.** Stories cite features; features cite waves; tasks cite stories or features and the modules / Decision Log entries (ADRs) they touch. A reader walking backward from any statement can reach its origin in the vision, the architecture doc, or a previous wave's reports.

**Surprises are first-class.** Discoveries during execution and review are absorbed into the change log, not buried.

## 2. File format and location

One file per project, named `<project-slug>-wave-plan.md`. Lives in `docs/` alongside the vision and architecture docs. Execution reports archive under `<project-slug>-wave-plan.reports/`.

YAML frontmatter holds machine-parseable state:

```yaml
---
wave_plan_version: 3                          # Incremented by each wave-update pass
created: 2026-05-02                           # ISO date, never changes
last_updated: 2026-06-15                      # ISO date, updated each update pass
source_vision: bookclub-vision.md             # Path to the vision doc
source_architecture: bookclub-architecture.md # Path to the architecture doc
current_wave: W2                              # The wave currently being executed
status: in_progress                           # in_progress | complete | paused | pivoted
---
```

`status` values:
- `in_progress` — normal operating state.
- `complete` — all waves closed out.
- `paused` — deliberately halted; requires human input before resuming.
- `pivoted` — a wave-update pass followed a vision pivot or substantial replan; some wave IDs may have been retired. Cleared back to `in_progress` after the next successful execute → update cycle.

## 3. Top-level structure

Below the frontmatter, the wave plan contains nine numbered sections, always in this order:

```markdown
# <Project> — Wave Plan

## 1. Goal and non-goals
## 2. Roles
## 3. Waves overview
## 4. Waves (detailed)
## 5. Assumptions register
## 6. Risks register
## 7. Decision Log references
## 8. Change log
## 9. Themes not yet waved
```

### 1. Goal and non-goals

Two or three short paragraphs restating the project's goal, what success looks like, and explicit non-goals. **Drawn from the vision doc**, not invented. Drift between the wave plan's goal section and the vision is reported and reconciled, not papered over.

### 2. Roles

A compact table of user roles, mirroring the vision doc's Section 2.

### 3. Waves overview

A one-glance summary: the wave ladder. One row per wave with status and one-line goal.

### 4. Waves (detailed)

One subsection per wave, in order. Format depends on wave status — see [Section 4](#4-per-wave-structure).

### 5, 6. Registers

Assumptions and risks are flat lists, referenced by ID from waves, stories, features, and tasks.

### 7. Decision Log references

A pointer table from each Decision Log entry (ADR-NNN) to the waves that respect it, establish it, or supersede it. The architecture doc's Decision Log section is the source of truth; this table is a cross-reference for navigation.

### 8. Change log

Append-only. One entry per `wave-update` pass. Each entry combines findings (what the review subagent surfaced) and decisions (what was absorbed).

### 9. Themes not yet waved

Themes the project intends to address but hasn't yet assigned to a wave. Graduates to a future-wave sketch when wave-update decides to plan it.

## 4. Per-wave structure

Every wave uses the same skeleton. The **depth** of each field depends on the wave's status — this is how the schema makes rolling-wave discipline structural.

### Common fields (all waves)

```markdown
### W<N> — <Wave name>
Status: future | in_progress | complete | pivoted | deferred
Goal: One sentence — what capability this wave delivers to users.
Theme: One to three words — the product area this wave addresses.
Depends on: W<N-1>, W<N-2>, or "none"
```

### Future waves (sketches)

A future wave also carries, and only carries:

```markdown
Entry criteria (sketch): One or two sentences.
Exit criteria (sketch): 2-4 bullets of testable outcomes, as best they can be stated now.
Candidate stories: <titles only>
Anticipated features: <titles only>
Assumptions: A<N>, A<N>
Risks: R<N>
ADRs respected: ADR-NNN, ADR-NNN
Anticipated new ADRs: <one-line titles only>
Sketch: 2-4 sentences describing approach.
```

No task breakdowns. No per-story acceptance criteria. No feature definitions beyond titles. No repro path. **Any of those in a future-wave section is a schema violation.**

### Current wave (fully planned)

A current wave has the sketch fields in full detail, plus execution-ready fields.

```markdown
Started: 2026-05-08

Entry criteria: <precise, satisfied by prior waves' outputs>
Exit criteria: <testable; each bullet verifiable from the artifacts>
Expected touched modules: <module names from architecture Section 2>
Repro: Path to a script or command that exercises this wave end-to-end from a clean state.

#### Stories
- **US-<role>-<N>: <title>**
  As a <role>, I want to <goal>, so that <benefit>.
  Acceptance criteria:
  - Given <context>, when <action>, then <outcome>.
  Priority: must-have | should-have | nice-to-have

#### Features
- **F-<N>: <name>**
  Description: One or two sentences.
  Supports stories: US-..., US-...
  Priority: must-have | should-have | nice-to-have

#### Tasks
- [ ] T<N>.1 — <short task description>
      Acceptance: <one or two concrete testable conditions>
      Serves: <US or F IDs the task advances, or "plumbing" if implicit>
      Touches: <module names from architecture doc; ADRs respected>

Assumptions: A<N>, A<N>
Risks: R<N>
ADRs respected: ADR-NNN, ADR-NNN
New ADRs proposed: ADR-NNN (proposed)   # If any will be established by this wave
```

`Expected touched modules` is the wave-level declaration of blast radius — the union of the modules each task names in its `Touches` field, plus any cross-cutting plumbing the wave will modify (test infra, build config, scripts). The review subagent in `wave-update` checks the actual diff against this list and surfaces any module touched that wasn't declared. Module-level granularity, not file-level — file-level declarations create compliance theater under refactors.

Story, feature, and task guidelines:

- **Every current-wave story has acceptance criteria.** A story without acceptance can't be honestly closed.
- **INVEST filter for stories:** Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Every current-wave task has acceptance criteria.** No exceptions.
- **Tasks sized for one agent session.** A task larger than a few hours of focused work is split.
- **Tasks cite what they serve and touch.** Story or feature ID; module name(s); ADR ID(s).
- **Order matters.** Within a wave, the task that most reduces uncertainty comes first — usually the end-to-end integration task.

Checkbox state (`[ ]` / `[x]`) is the single source of truth for task status. The executor flips them as it finishes each task; no other skill touches them.

### Past waves (closeout)

When `wave-update` closes a wave, its detailed content is replaced by a compact closeout summary.

```markdown
### W<N> — <Wave name>
Status: complete | pivoted | deferred
Completed: 2026-06-12
Theme: <preserved>
Delivered: Short prose — what this wave actually produced. A reader should
  see the shape of what was built without opening any other file.
Assumptions resolved: A<N> validated | A<N> broken → A<N+1> opened
ADRs established: ADR-NNN, ADR-NNN
ADRs superseded: ADR-NNN → ADR-NNN
Stories closed: US-..., US-...
Features delivered: F-..., F-...
Execution report: <path>
```

## 5. Assumptions register

Flat list. Waves, stories, features, and tasks reference entries by ID.

```markdown
- **A1** — Club sizes stay under ~20 members. *Wave: W1. Status: untested.*
- **A2** — Voting is single-choice per member, not ranked. *Wave: W2. Status: broken (2026-06-12) — superseded by A6.*
- **A6** — Members prefer ranked-choice voting over single-choice. *Wave: W2. Status: open.* Replaces: A2.
```

Status values: `untested` | `open` | `validated` | `broken`.

Rules: never delete; broken assumptions are superseded with new IDs; status changes are dated; assumption bodies are never edited.

## 6. Risks register

Same flat-list shape as assumptions, with mitigation instead of status text. Risk status values: `open` | `retired (did not materialize)` | `triggered — mitigated` | `triggered — unresolved`.

## 7. Decision Log references

A pointer table, not the source of truth. The architecture doc's `## 8. Decision Log` section (or promoted ADR files) holds the actual entries.

```markdown
| ADR     | Title                              | Established | Status                             | Cited by               |
|---------|------------------------------------|-------------|------------------------------------|------------------------|
| ADR-001 | Persistence: SQLite local file     | architect   | Accepted                           | W1, W2                 |
| ADR-004 | Voting data model: flat columns    | W2 sketch   | Superseded (2026-06-12) by ADR-007 | (historical)           |
| ADR-007 | Voting data model: row-per-rank    | W2 update   | Accepted                           | W2, W3 (anticipated)   |
```

The "Cited by" column is denormalized from the wave-detail sections and updated by `wave-update` when entries are added or supersession changes the picture.

## 8. Change log

Append-only. One entry per `wave-update` pass. Each entry combines the review subagent's findings (with disposition) and the decisions absorbed. The findings list is the durable record of what the review surfaced — including findings the human rejected — so a reader can reconstruct both what was found and what was done. **Findings carry their own evidence**, not just labels: enough text that a future reader can understand the finding without reopening the (ephemeral) subagent conversation.

```markdown
### 2026-06-15 — Update after W2
Type: normal-update
Audit verdict: pass-with-findings

Review findings (from subagent):
- F1 (high, accepted): A2 (single-choice voting) is broken.
  Evidence: user-test simulation in W2 produced minority winners in 5 of 8 sampled
  scenarios; the W1 sketch's flat-column model can't represent ranked preferences
  without schema migration. Recommend opening A6 (members prefer ranked-choice).
- F2 (medium, accepted, ratified ADR-007): ADR-004 (flat vote columns) violated
  by T2.3.
  Evidence: T2.3's implementation (`db/migrations/004_votes.sql`) adds a `rank`
  column inconsistent with the flat-column shape ADR-004 mandated. Subagent
  proposed ADR-007 (row-per-rank); wave-update ratified it and embedded the
  accepted entry in `architecture.md` Section 8.
- F3 (low, accepted as plumbing): tests/perf/ added without a planned task.
  Evidence: 4 perf tests under tests/perf/voting/ — diff scope leakage but
  benign; treat as undeclared-but-aligned plumbing.
- F4 (medium, deferred to W3): T2.4 marked [x] but admits partial coverage.
  Evidence: report admits tie-break E2E missing; checkbox should have been [~].
  Coverage gap doesn't block W2 exit criteria but should be picked up in W3.

Decisions absorbed:
- Closed W2 with T2.4 partial; tie-break E2E carried to W3 scope (per F4).
- A2 marked broken; A6 (ranked-choice) opened (per F1).
- ADR-007 added to architecture.md Section 8 Decision Log (Accepted), supersedes ADR-004 (per F2). Context, decision, and consequences are recorded in the ADR-007 entry.
- Architecture doc Section 3 (Data and state) edited to reference row-per-rank schema; architecture v3 → v4.
- Expanded W3 from sketch.
- Re-sketched W4 to account for ranked-voting data shape.
```

The format is mandatory: every entry has `Type:`, `Audit verdict:`, a `Review findings` list, and a `Decisions absorbed` list. Each finding line has the shape `F<N> (<severity>, <disposition>[, <action>]): <one-line summary>` followed by an indented `Evidence:` block of one to three sentences naming the specific artifact, file, ADR, or test that grounds the finding. Disposition values: `accepted` | `rejected (user override: <reason>)` | `deferred to W<N+M>`. A reader six months later should be able to reconstruct what the review found and how the human handled it without opening any other file.

`Type` values:
- `initial-draft` — first write by `wave-plan`.
- `normal-update` — routine: one wave closed, next wave planned, minor register/Decision Log updates.
- `substantial-update` — multiple assumptions broken, multiple future waves materially changed. Plan still coherent.
- `vision-pivot-update` — the vision was pivoted; this update reconciles the wave plan to the new vision. Retired wave IDs and superseded ADRs are listed; new wave IDs may appear. Frontmatter `status` is set to `pivoted` until a subsequent execute → update cycle clears it.
- `blocked-update` — audit verdict `fail`. The wave is *not* closed and the next wave is *not* expanded. The change log records the failing findings (with evidence) and the human's chosen recovery path (loop back to `wave-execute`, renegotiate scope on the current wave's exit criteria, or pause the project).

`Audit verdict` values, captured per update pass: `pass` | `pass-with-findings` | `fail`.
- `pass` / `pass-with-findings` allow the update to close the wave and expand the next; Type is `normal-update`, `substantial-update`, or `vision-pivot-update`.
- `fail` blocks closeout. Type is `blocked-update`. Frontmatter behavior on a `blocked-update`: `wave_plan_version` still bumps (the change log was appended, which is itself a state change); `current_wave` is unchanged; `last_updated` is set to today; `status` stays `in_progress` unless the human chooses `paused`. The change-log entry's `Decisions absorbed` list records the recovery path explicitly (e.g., "Loop back to wave-execute for T2.3 with revised acceptance" or "Renegotiate W2 exit criteria E2 from p95 ≤ 5s to p95 ≤ 8s — see body edit"). Renegotiating exit criteria *is* allowed under a blocked-update, with explicit human approval and an explicit change-log bullet — that's the only place the wave plan's structural content can change without the wave being closed.

## 9. Execution report template

Produced by `wave-execute` at the end of each wave. Read by `wave-update` (via its review subagent and directly).

Location: `<project-slug>-wave-plan.reports/wave-W<N>-execution.md`.

```markdown
---
wave: W<N>
wave_start_ref: <git-sha-at-start>      # captured by wave-execute before work; empty only if project lacks git
wave_end_ref: <git-sha-at-end>          # captured by wave-execute after its commit; empty only if project lacks git
completed: 2026-06-12
wave_plan_version_at_start: 2
---

# W<N> <Wave name> — Execution Report

## What was built
Prose summary of actual outcome — what a user can now do that they couldn't
before. Reference completed task IDs and the stories/features they delivered.
Not a commit log; a capability summary.

## Task status
- [x] T2.1 — ...
- [~] T2.4 — Partial: <what's missing and why>

## Exit criteria status
- [x] <criterion>: <evidence>
- [~] <criterion>: <gap>

## Verification
| Check                    | Status         | Evidence                                  |
|--------------------------|----------------|-------------------------------------------|
| Unit tests               | pass           | `pytest tests/unit` — 87/87               |
| Integration tests        | pass           | `pytest tests/integration` — 12/12        |
| Typecheck                | pass           | `mypy src/` — clean                       |
| Build                    | pass           | `make build` — produced `dist/app`        |
| Repro                    | pass           | `scripts/demo-w2.sh` — 3/3 checks PASS    |
| Manual / browser check   | n/a            | (CLI only; no UI in this wave)            |

The matrix lists every check the executor considered for this wave, with `pass`, `fail`, `skipped (<reason>)`, or `n/a (<reason>)`. Don't omit rows; don't pad with `n/a` for checks that genuinely don't apply without naming why. Match verification depth to change risk: a docs-only change doesn't need an integration suite; a load-bearing logic change probably does. The matrix is the executor's accountability for what was actually run.

## Assumptions status
- A<N>: validated | broken — <evidence or recommended replacement>

## ADR adherence
For each ADR cited by this wave, did the implementation respect it?
- ADR-001: respected.
- ADR-004: violated — implementation required a row-per-rank shape; recommend supersede via wave-update.

## Discoveries
Things learned during execution that affect future waves or challenge plan assumptions.

If the executor accepted *technical debt* during the wave — visible compromises taken knowingly to stay in scope — list them as labeled bullets:

```
- D<N>: <description>. Accepted because: <reason>. Owner: <wave when this should be revisited, or "watch" if no firm owner yet>.
```

Examples: "D1: pickle for serialization — accepted because public API isn't W2's scope; revisit before W4 (when external clients integrate)." "D2: magic-string config in T2.3 — accepted because the value set isn't stable yet; watch."

`wave-update`'s review subagent surfaces these as a category-9 finding (code-quality lens, sub-lens "accepted debt") when applying that lens. If accepted debt accumulates across waves, the wave plan can grow an optional **Debt register** parallel to Assumptions/Risks (same flat-list shape: ID, description, reason accepted, owner wave or `watch`, status `open` | `paid (W<N>)` | `accepted-permanent`). Skip the register while debt count stays low; promote when the change-log starts repeatedly citing the same debt items.

## Proposed scope changes
Explicit, bulleted — each with one-line rationale.

## Risks encountered
- R<N>: did not materialize | materialized — <what happened>
- New risks: ...

## Readiness for next wave
Prerequisites the next wave needs that weren't originally planned.
```

A section may be omitted **only** if it would be empty.

## 10. Pivot handling

Pivots can originate at two layers, with different cascades.

**Wave-plan pivot (substantial-update or pivot type).** Vision unchanged; multiple wave-level decisions revised. Type in change log: `substantial-update` if waves are revised but the wave ladder shape persists; for genuine wave-ladder pivots (retiring wave IDs), use `vision-pivot-update` if vision changed alongside, or note the wave-only pivot in `substantial-update` with explicit retired-IDs list.

**Vision pivot.** The vision doc is revised by `vision pivot` mode, which sets vision frontmatter to `pivoted`. The next `wave-update` invocation must produce a `vision-pivot-update` change-log entry that:

1. Notes the source vision change (which sections were revised in vision-version N).
2. Reconciles the wave plan's Goal and Roles sections to match the new vision.
3. Retires any waves whose goal no longer fits. Retired wave IDs are listed; never reused.
4. Introduces new wave IDs as needed.
5. Triggers an architecture review (within the same wave-update invocation): if any ADRs are now invalid under the new vision, the review subagent surfaces them as supersession proposals and wave-update applies them.
6. Sets wave-plan frontmatter `status: pivoted` until the next successful execute → update cycle.

The `vision pivot` mode does *not* edit the wave plan directly. It only edits the vision and signals the wave-update cycle to reconcile.

## 11. Invariants

1. **The wave plan is the single source of truth for project state below the vision.** Skills do not maintain parallel state for waves, assumptions, risks, or Decision Log cross-references.
2. **The vision and architecture are upstream sources of truth.** The wave plan's Goal/Roles mirror the vision; the wave plan's Decision Log references mirror the architecture's Decision Log section. Drift is reported and fixed; not papered over.
3. **Future waves never get task-level detail, per-story acceptance, or feature definitions.** Only titles, themes, sketches, and sketched criteria.
4. **Every current-wave task has acceptance criteria.** No exceptions.
5. **Every current-wave story has acceptance criteria.**
6. **Every wave has exit criteria and a repro path.** A wave without them cannot be reviewed.
7. **Registers are append-only.** Assumptions, risks, and the Decision Log references table are never shrunk; broken or superseded entries are kept with new IDs replacing them.
8. **The change log is append-only.** Entries are never rewritten.
9. **Execution reports do not modify the wave plan.** Only `wave-update` modifies the plan.
10. **`wave-update`'s review subagent runs in fresh context.** It reads only committed artifacts (wave plan, execution report, architecture doc, code, repro). The subagent's output is presented to the human for approval before any plan or architecture edits are applied.
11. **Scope expansion requires an explicit change-log entry.** No silent absorption.
12. **Walking-skeleton default for W1.** Vertical slice exercising every architecture-module marked `W1: required`. Modules marked `deferred (W<N>)` in the architecture's Section 2 are skipped by the walking-skeleton check. Horizontal-foundation W1 (no vertical slice at all) requires explicit justification in the Goal section.
13. **One expansion per update.** Exactly one future wave is expanded per update cycle.
14. **Audit verdict gates closeout.** A `fail` verdict blocks the wave from being closed and the next wave from being expanded. The change-log entry uses Type `blocked-update`, captures the failing findings with evidence, and names the chosen recovery path (loop back to `wave-execute`, renegotiate the current wave's exit criteria, or pause). `current_wave` is unchanged on a blocked-update; `wave_plan_version` still bumps because the change log was appended.
15. **Pivots bump frontmatter status to `pivoted`.** Cleared back to `in_progress` only by the next successful full cycle.
16. **Retired wave IDs and superseded ADR IDs are never reused.**
17. **ADRs cited by the architecture doc must be ratified (`Status: Accepted`) before `wave-plan` and `wave-execute` run.** Seed ADRs from `architect draft` are ratified by `architect ratify` (or manual edit). Mid-cycle ADRs from `wave-update`'s review subagent are ratified by `wave-update` itself before saving.
18. **No skill auto-invokes the next.** Each step is invoked by the human lead.

## 12. Worked mini-example

A truncated wave plan for `filetagger` (a CLI that tags files by content), after W1 closeout and W2 in progress:

```markdown
---
wave_plan_version: 2
created: 2026-05-02
last_updated: 2026-05-26
source_vision: filetagger-vision.md
source_architecture: filetagger-architecture.md
current_wave: W2
status: in_progress
---

# filetagger — Wave Plan

## 1. Goal and non-goals
A local CLI that tags files in a directory by content (topic, sentiment,
language) and lets users find files by tag combinations. Non-goals: no
cloud sync, no GUI, no write-back into file contents.

## 2. Roles
| Role | What they're trying to do |
|------|---------------------------|
| User | Find files by what they're about, not just by name. |

## 3. Waves overview
| Wave | Name                        | Status       | One-line goal |
|------|-----------------------------|--------------|---------------|
| W1   | Scan and tag (skeleton)     | complete     | One file in, one tagged row out. |
| W2   | Query by tag                | in_progress  | User can find files by tag combinations. |
| W3   | Incremental re-scan         | future       | Re-scans only touch changed files. |

## 4. Waves (detailed)
[per-wave content omitted in this excerpt; structure follows Section 4 above]

## 5. Assumptions register
- **A1** — SQLite handles 10k-file indexes fast enough. *Wave: W1, W2. Status: validated (2026-05-15).*
- **A4** — Query latency is dominated by SQLite, not the LLM. *Wave: W2. Status: untested.*
- **A5** — mtime + size is a reliable change signal. *Wave: W3. Status: open.*

## 6. Risks register
- **R1** — Boolean parser may misinterpret ambiguous queries. *Wave: W2. Likelihood: medium. Impact: low. Status: open.* *Mitigation: echo parsed AST on `--explain`.*

## 7. Decision Log references
| ADR     | Title                          | Established | Status   | Cited by   |
|---------|--------------------------------|-------------|----------|------------|
| ADR-001 | Persistence: SQLite local file | architect   | Accepted | W1, W2, W3 |
| ADR-002 | Tagger: remote LLM API         | architect   | Accepted | W1, W2     |
| ADR-003 | Distribution: single-binary    | architect   | Accepted | W1, W2, W3 |
| ADR-004 | Tag namespace: string-prefixed | W1 update   | Accepted | W1, W2     |

## 8. Change log
### 2026-05-26 — Update after W1
Type: normal-update
Audit verdict: pass

Review findings (from subagent):
- F1 (medium, accepted): A2 (one tag set per file) is broken.
  Evidence: 3 of 5 W1 dogfooding sessions tagged the same file under conflicting
  meanings (work/personal). Single tag-set forces destructive overwrites.
- F2 (medium, accepted, ratified ADR-004): Tag namespace needs a structural
  decision.
  Evidence: T1.4 introduced ad-hoc string prefixes (`work:`, `personal:`) without
  a Decision Log entry; wave-update ratified ADR-004 (string-prefixed namespace)
  and embedded the accepted entry in `architecture.md` Section 8.

Decisions absorbed:
- Closed W1 (walking skeleton). All exit criteria met.
- A2 marked broken; A3 (string-prefixed namespace) opened and validated in same wave (per F1).
- ADR-004 added to architecture.md Section 8 Decision Log (Accepted), no supersession (per F2). Context, decision, and consequences are recorded in the ADR-004 entry.
- Expanded W2 sketch into full detail. current_wave advanced to W2.
- Re-sketched W3 briefly to confirm re-scan against the prefixed namespace.

### 2026-05-02 — Wave plan created
Type: initial-draft
- Drafted from filetagger-vision.md (v1) and filetagger-architecture.md (v1) with seed ADRs ADR-001, ADR-002, ADR-003.
- Three waves; W1 fully planned as walking skeleton; W2-W3 sketched.
- 5 assumptions, 2 risks seeded from vision Open Questions.

## 9. Themes not yet waved
- Watch mode (continuous retagging on file change).
- Multi-machine sync of indexes.
- GUI frontend.
```

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
