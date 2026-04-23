# Wave Doc Schema

This file is the shared contract between the four skills in the **DEAR** loop:

- `wave-draft` — writes the first version of the unified wave doc from a brief or short spec.
- `wave-execute` — reads the wave doc, implements the current wave, and produces an execution report.
- `wave-audit` — independently verifies the current wave against the plan and the report, and produces an audit report.
- `wave-redraft` — reads the wave doc plus both reports, closes the current wave, expands the next wave's sketch into full detail, and re-sketches remaining waves.

All four skills must read, write, and interpret the wave doc in exactly the way this document specifies. If a skill needs information that isn't in the schema, either the schema is wrong (update it here first) or the skill is overreaching (pull it back).

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Top-level structure](#3-top-level-structure)
4. [Per-wave structure](#4-per-wave-structure)
5. [Assumptions register](#5-assumptions-register)
6. [Risks register](#6-risks-register)
7. [Architectural commitments register](#7-architectural-commitments-register)
8. [Change log](#8-change-log)
9. [Execution report template](#9-execution-report-template)
10. [Audit report template](#10-audit-report-template)
11. [Invariants](#11-invariants)
12. [Worked mini-example](#12-worked-mini-example)

---

## 1. Philosophy

Rolling-wave development exists because later-wave certainty is an illusion. The further ahead we specify and plan, the more the document is speculation dressed up as detail. The discipline says: **specify and plan the current wave comprehensively, sketch future waves concisely, execute one wave at a time, and commit to learning between waves**.

This schema enforces that discipline structurally. It is deliberately harder to over-specify a future wave than to sketch it, and deliberately harder to silently expand scope than to flag a discovery.

Four operating principles thread through the schema:

**One document, one source of truth.** Requirements and plan live in the same document, organized by wave. Every wave holds its own stories, features, and plan tasks together — not in parallel files. If a skill needs to know something, it reads the wave doc. If a skill learns something, it writes to the wave doc.

**Current in detail, future in sketch.** The wave doc physically distinguishes the current wave (full stories, features, tasks with acceptance, exit criteria, repro path) from future waves (themes, candidate story titles, approach sketch, sketched entry/exit criteria). The structure makes over-specification of future work hard to do by accident.

**Every claim is traceable.** Stories cite features; features cite waves; tasks cite stories or features; updates cite the assumptions they validated or broke. A reader walking backward from any statement can reach its origin.

**Surprises are first-class.** Discoveries during execution are the point, not a failure. The schema has a dedicated place to record them at every level — per-task, per-wave, per-doc — so they can't be buried. The audit step is a separate skill so that verification stays independent of interpretation.

## 2. File format and location

One markdown file per project, named `<project-slug>-wave-doc.md`. The file sits in the project's `docs/` directory (or equivalent).

YAML frontmatter holds machine-parseable state. The markdown body holds human-and-agent-readable detail. No other files, no splits, no sidecars except the reports archived under `<project-slug>-wave-doc.reports/`.

```yaml
---
wave_doc_version: 3                      # Incremented by each redraft pass
created: 2026-04-22                      # ISO date, never changes
last_updated: 2026-04-28                 # ISO date, updated every redraft
source_spec: bookclub-brief.md           # The input the doc was drafted from
current_wave: W2                         # The wave currently being executed
status: in_progress                      # in_progress | complete | paused | pivoted
---
```

`status` values:
- `in_progress` — normal operating state.
- `complete` — all waves closed out; no further work planned.
- `paused` — deliberately halted; requires human input before resuming.
- `pivoted` — a redraft rewrote the doc substantially; some wave IDs may have been retired. The change log entry explains.

## 3. Top-level structure

Below the frontmatter, the wave doc contains nine numbered sections, always in this order:

```markdown
# <Project> — Wave Doc

## 1. Goal and non-goals
## 2. Roles
## 3. Waves overview
## 4. Waves (detailed)
## 5. Assumptions register
## 6. Risks register
## 7. Architectural commitments register
## 8. Change log
## 9. Themes not yet waved
```

### 1. Goal and non-goals

Two or three short paragraphs restating why we're building this, what success looks like, and explicit non-goals. Drawn from the input spec. This section is load-bearing: it's what the executor and auditor read to sanity-check whether a proposed piece of work is in scope.

### 2. Roles

A compact table of user roles with a one-line description of what each role is trying to accomplish in the system. A role is defined by what the person is trying to do, not their job title.

```markdown
| Role      | What they're trying to do                                    |
|-----------|--------------------------------------------------------------|
| Organizer | Set up and run a book club on behalf of a group.             |
| Member    | Participate in nominations, voting, and meetings.            |
| Admin     | Keep the system healthy and unblock users.                   |
```

Roles span the whole project, not individual waves. New roles added later are a notable event and get a change-log entry.

### 3. Waves overview

A one-glance summary: the wave ladder.

```markdown
| Wave | Name                         | Status      | One-line goal |
|------|------------------------------|-------------|---------------|
| W1   | Walking skeleton             | complete    | End-to-end login + empty dashboard. |
| W2   | Nomination and voting flow   | in_progress | Members can pick the next book. |
| W3   | Scheduling and RSVPs         | future      | A meeting is on the calendar. |
| W4   | Shared notes and archive     | future      | Meetings produce durable artifacts. |
```

### 4. Waves (detailed)

One subsection per wave, in order. Format depends on whether the wave is `past`, `current`, or `future` — see [Section 4](#4-per-wave-structure).

### 5, 6, 7. Registers

The three registers — assumptions, risks, architectural commitments — are flat lists referenced by ID from waves, tasks, stories, and features. See their dedicated sections below.

### 8. Change log

Append-only. One entry per redraft pass. See [Section 8](#8-change-log).

### 9. Themes not yet waved

A short list of themes that belong to the product vision but haven't been assigned to a wave yet. One bullet per theme, no further detail. This section exists so scope conversation has a place to live without bleeding into the future-wave sketches (which are committed directions; themes here are not yet committed). A theme graduates to a future-wave sketch the first time a redraft pass decides to plan it.

## 4. Per-wave structure

Every wave uses the same skeleton. The **depth** of each field depends on the wave's status. This is how the schema makes rolling-wave discipline structural rather than aspirational.

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
Entry criteria (sketch): One or two sentences — what must be true before this wave starts.
Exit criteria (sketch): 2-4 bullets of testable outcomes, as best they can be stated now.
Candidate stories: <titles only, no acceptance criteria, no IDs yet>
  - Member can nominate a book.
  - Member can vote on nominations.
  - Organizer can close a vote.
Anticipated features: <titles only, no detail>
  - Nomination form
  - Voting UI
  - Vote tallying
Assumptions: A<N>, A<N>   (references to entries in Section 5)
Risks: R<N>               (references to Section 6)
Commitments respected: AC<N>, AC<N>   (entries in Section 7 that constrain this wave)
Anticipated new commitments: <titles only; new commitments this wave may need to add>
Sketch: 2-4 sentences describing approach at a high level.
```

No task breakdowns. No per-story acceptance criteria. No feature definitions beyond titles. No repro path. **Any of those in a future-wave section is a schema violation** — the rolling-wave invariant catches them in the audit pass.

### Current wave (fully planned)

A current wave has the sketch fields in full detail (not as a sketch), plus the execution-ready fields.

```markdown
Started: 2026-04-28   (ISO date, set when the wave becomes current)

Entry criteria: <precise, satisfied by prior waves' outputs>
Exit criteria: <testable; each bullet verifiable by an independent auditor>
Repro: Path to a script or command an auditor can run to exercise this wave end-to-end.

#### Stories
- **US-<role>-<N>: <title>**
  As a <role>, I want to <goal>, so that <benefit>.
  Acceptance criteria:
  - Given <context>, when <action>, then <outcome>.
  Priority: must-have | should-have | nice-to-have

#### Features
- **F-<N>: <name>**
  Description: One or two sentences describing the capability.
  Supports stories: US-..., US-...
  Priority: must-have | should-have | nice-to-have
  Notes: <dependencies, constraints — if any>

#### Tasks
- [ ] T<N>.1 — <short task description>
      Acceptance: <one or two concrete testable conditions>
      Serves: <US or F IDs the task advances, or "plumbing" if implicit>
      Touches: <files/modules, optional>
- [ ] T<N>.2 — ...

Assumptions: A<N>, A<N>
Risks: R<N>
Commitments respected: AC<N>, AC<N>
New commitments proposed: AC<N>, AC<N>   (commitments this wave will establish)
```

Guidelines for stories in the current wave:

- **Every story has acceptance criteria.** A story without acceptance is a story that can't be honestly closed.
- **INVEST filter applies.** Independent, Negotiable, Valuable, Estimable, Small, Testable. If a story is bloated, split it. If it reads like a UI spec, rewrite it.
- **Stories here serve this wave.** A story that doesn't serve the current wave is a theme (goes in Section 9) or a future-wave candidate — not a current-wave story.

Guidelines for features in the current wave:

- **Features support stories.** Every feature traces to at least one story. If a feature doesn't, it's either implicit plumbing (label it) or scope creep.
- **Features are capabilities, not components.** "Sitter search" is a feature; "SQLAlchemy ORM" is a component.

Guidelines for tasks in the current wave:

- **Acceptance criteria are mandatory.** A task without acceptance can't be closed out honestly. Drafting and redrafting skills must refuse to produce one.
- **Tasks sized for one agent session.** A task larger than a few hours of focused work is split. Large tasks are the loophole rolling-wave exists to prevent.
- **Tasks cite what they serve.** Story/feature ID, or "plumbing" for implicit scaffolding.
- **Order matters.** Within a wave, the task that most reduces uncertainty comes first — usually the end-to-end integration task.

Checkbox state (`[ ]` / `[x]`) is the single source of truth for task status. The executor flips them as it finishes each task; no other skill touches them.

### Past waves (closeout)

When a wave completes, its detailed content is replaced by a compact closeout summary. The story list, feature list, and task list are removed (the reports archive them); what remains is the learning.

```markdown
### W<N> — <Wave name>
Status: complete | pivoted | deferred
Completed: 2026-04-27
Theme: <preserved>
Delivered: Short prose — what this wave actually produced, independent
  of what was planned. A reader should see the shape of what was built
  without opening any other file.
Assumptions resolved: A<N> validated | A<N> broken → A<N+1> opened
Commitments established: AC<N>, AC<N>
Stories closed: US-..., US-...
Features delivered: F-..., F-...
Execution report: <path>
Audit report: <path>
```

## 5. Assumptions register

Flat list. Waves, stories, features, and tasks reference entries by ID.

```markdown
## 5. Assumptions register

- **A1** — Club sizes stay under ~20 members. *Wave: W1. Status: untested.*
- **A2** — Voting is single-choice per member, not ranked. *Wave: W2. Status: untested.*
- **A3** — Magic-link auth is acceptable for guest access. *Wave: W1. Status: validated (2026-04-25).*
- **A4** — Members are reachable via email; SMS is not required. *Wave: W2. Status: broken — superseded by A6.*
- **A6** — Members prefer ranked-choice voting over single-choice. *Wave: W2. Status: open.* Replaces: A2.
```

Status values: `untested` | `open` | `validated` | `broken`.

Rules:

- **Never delete an assumption.** If it's wrong, mark it broken and open a replacement with a new ID. The history explains why the doc looks the way it does.
- **Every assumption cites the wave it belongs to.** Floating assumptions are a yellow flag.
- **Status changes are dated.** When execute or redraft marks an assumption validated or broken, include the date.
- **Never edit an existing assumption's body.** Open a replacement instead.

## 6. Risks register

Same flat-list structure as assumptions, with mitigation instead of status text.

```markdown
## 6. Risks register

- **R1** — Poll-open notifications may be delayed by email provider.
  *Wave: W2. Likelihood: medium. Impact: medium.*
  *Mitigation: in-app badge as primary signal, email as secondary.*
- **R2** — Guest magic-links may expire before a meeting ends.
  *Wave: W1. Likelihood: low. Impact: low.*
  *Mitigation: TTL of 24h past meeting end; allow organizer to reissue.*
```

Waves reference risks by ID in their `Risks:` field. When a risk materializes during execution, the executor reports it; redraft updates the entry accordingly.

Risk status values (used during redraft): `open` | `retired (did not materialize)` | `triggered — mitigated` | `triggered — unresolved`.

## 7. Architectural commitments register

First-class list of decisions made about *how* the system is built. Distinct from assumptions (which are beliefs about the world) and risks (which are things that could go wrong). Commitments are choices whose revision has real cost.

```markdown
## 7. Architectural commitments register

- **AC1** — Persistence: SQLite with a single local file at `~/.bookclub/bookclub.db`.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: solo/small-group scale; zero-ops; embedded in the CLI binary.*
- **AC2** — Auth: magic-link via email; no passwords.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: lowest friction for book club context; avoids password reset UX.*
- **AC3** — Deployment: single-binary Go executable.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: users run locally; no server to operate.*
- **AC4** — Voting data model: one vote row per (member, nomination), ordered integer rank.
  *Established: W2 (2026-04-28). Status: active.*
  *Rationale: supports both single-choice (rank=1 only) and ranked (rank 1..N) without schema change.*
- **AC5** — Old voting model (flat: one column per member pick). *Established: W2 sketch. Status: superseded (2026-04-28) by AC4.*
```

Status values: `active` | `superseded (<date>) by AC<N>` | `retired (<date>)`.

Rules:

- **Every commitment has a rationale.** A commitment without a reason is a preference dressed as architecture. Require the rationale line.
- **Every commitment cites the wave that established it.** Walking-skeleton waves typically establish many commitments; later waves rarely add more than one or two.
- **Commitments are referenced by waves that respect them and by waves that add new ones.** The redrafter uses these references to check that later waves don't silently violate earlier choices.
- **Never edit an existing commitment's body.** If it needs to change, supersede it with a new ID. History matters.

## 8. Change log

Append-only. One entry per redraft pass, even if the redraft was minimal — so the history is complete.

```markdown
## 8. Change log

### 2026-04-28 — Redraft after W2 closeout
Type: normal-redraft
- Closed W2. All exit criteria met.
- A2 (single-choice voting) marked broken based on execution report and audit;
  opened A6 (ranked-choice). Impacts W2 data model — see W2 closeout notes.
- AC5 (flat vote columns) superseded by AC4 (rank-ordered row model).
- Expanded W3 sketch into full detail. current_wave advanced to W3.
- Re-sketched W4 to account for ranked-voting data shape.

### 2026-04-25 — Redraft after W1 closeout
Type: normal-redraft
- Closed W1 (walking skeleton). All exit criteria met.
- AC1, AC2, AC3 established.
- A3 validated.
- current_wave advanced to W2.

### 2026-04-22 — Wave doc created
Type: initial-draft
- Drafted from bookclub-brief.md.
- Four waves, W1 fully planned as walking skeleton, W2-W4 sketched.
- 5 assumptions, 2 risks, 3 anticipated commitments seeded from the brief.
```

`Type` values:
- `initial-draft` — first write by wave-draft.
- `normal-redraft` — routine: one wave closed, next wave planned, minor register updates.
- `substantial-redraft` — multiple assumptions broken, multiple future waves materially changed. Doc still coherent.
- `pivot` — forward direction was rewritten. Retired wave IDs listed; new wave IDs may appear. Frontmatter `status` is set to `pivoted` until a subsequent execute/redraft cycle completes.

## 9. Execution report template

Produced by `wave-execute` at the end of each wave. Read by `wave-audit` (to verify) and `wave-redraft` (to interpret).

Location: `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`.

```markdown
# W<N> <Wave name> — Execution Report
Wave: W<N>
Completed: 2026-04-28
Wave doc version at start: 2

## What was built
Prose summary of actual outcome — what a user can now do that they
couldn't before. Reference completed task IDs and the stories/features
they delivered. Not a commit log; a capability summary.

## Task status
- [x] T2.1 — Schema for nominations and votes. Done.
- [x] T2.2 — Nomination UI. Done.
- [x] T2.3 — Voting UI with tie-break path. Done.
- [~] T2.4 — End-to-end test. Partial: covers nominate and vote but not
       tie-break. Tie-break E2E deferred to W3.

## Exit criteria status
- [x] Members can submit nominations through the nomination UI.
- [x] Poll closes automatically at deadline and records a winner.
- [~] 10-member synthetic test completes in under 5s — measured 7s p95.

## Assumptions status
- A1: validated — 30-member synthetic club performs fine.
- A2: broken — user testing showed strong preference for ranked voting;
  single-choice felt arbitrary. Recommend replacing with A6 (ranked).

## Commitments status
- AC1, AC2, AC3: respected.
- AC5 (anticipated from W2 sketch): the flat vote-columns design is
  inadequate once ranked voting enters scope. Recommend supersede with
  a row-per-rank design (proposed AC6 if redrafter agrees).

## Spec-level discoveries
Things learned about users, stories, or features that change future waves.
- US-MEM-3 (change own vote before close) turned out to be two stories:
  editing an unranked vote vs. re-ranking. Recommend split in W3 scope.

## Plan-level discoveries
Things learned about implementation that change future waves.
- Email delivery from local binary requires SMTP config; users running
  in restricted networks hit timeouts. W3 scheduling will have the same
  issue; may need a shared queue abstraction.

## Proposed scope changes
Explicit, bulleted — each with one-line rationale.
- Add to W3: migration from single-choice to ranked data model.
- Remove from W4: shared-notes emoji reactions — didn't come up once in
  testing, and current scope is already large.
- Defer to later: dark mode for voting UI.

## Risks encountered
- R1 (poll notification delay) did not materialize.
- New risk: ranked-choice ties can produce multi-way deadlocks; needs
  a tie-break rule. Opening as R3 in the registry.

## Readiness for next wave
Prerequisites the next wave needs that weren't originally planned, or
that need to happen before the next wave can start cleanly.
```

A section may be omitted **only** if it would be empty (e.g., "Risks encountered" when none surfaced). Omitting a section with content is a schema violation.

## 10. Audit report template

Produced by `wave-audit` after `wave-execute` and before `wave-redraft`. Verifies the execution report against the wave doc and the artifacts.

Location: `<project-slug>-wave-doc.reports/wave-W<N>-audit.md`.

```markdown
# W<N> <Wave name> — Audit Report
Wave: W<N>
Audit date: 2026-04-28
Wave doc version at audit: 2
Execution report reviewed: wave-W<N>-execution.md

## Verdict
pass | pass-with-findings | fail

One-paragraph summary justifying the verdict.

## Exit criteria verification
For each exit criterion, independent pass/fail with evidence:
- [x] Members can submit nominations — verified by running repro script
      `scripts/demo-w2.sh` which exercises the flow end-to-end.
- [x] Poll closes at deadline — verified by scripted time advance in test
      harness `tests/e2e/test_poll_close.py::test_closes_at_deadline`.
- [~] 10-member synthetic test under 5s — report admits 7s p95; exit
      criterion is technically not met. Finding F1 below.

## Task verification
Cross-reference report's claimed task status against the wave doc's
checkbox state and the repo diff. Flag discrepancies.

## Assumption verification
For each assumption the report claims to have resolved, check the
evidence:
- A2 marked broken — evidence is user-test transcript in
  `research/w2-voting.md`, confirmed.
- A1 marked validated — evidence is benchmark output; cross-checked.

## Commitment verification
For each commitment referenced by this wave, confirm adherence:
- AC1 (SQLite) — respected; no other persistence layer introduced.
- AC2 (magic-link auth) — respected.
- AC3 (single-binary) — potentially violated: new SMTP dependency pulls
  in a network runtime. Finding F2 below.

## Scope findings
Changes in the diff that don't map to planned tasks or declared
discoveries. None is ideal; any means investigate.

## Entry-criteria check for next wave
Per the wave doc's W<N+1> entry criteria (sketch), check whether this
wave's outputs satisfy them. If not, flag what's missing.

## Findings
- **F1** — W2 exit criterion "10-member test under 5s" not met (7s p95).
  Severity: medium. The report acknowledges this but marks the wave
  complete. Recommend either extending W2 to close the gap or
  explicitly renegotiating the criterion in redraft.
- **F2** — AC3 (single-binary) at risk due to new SMTP code path.
  Severity: medium. Recommend resolving in redraft: either supersede
  AC3 with a more permissive commitment, or refactor SMTP into a
  vendor-able dependency.

## Recommendations to redrafter
One or two sentences per recommendation, not a full rewrite of the
plan. The redrafter makes the decisions; the auditor surfaces what
needs a decision.
```

Audit verdict guidance:

- `pass` — all exit criteria met, all assumption claims verified, no scope leakage, no commitment violations, entry criteria for next wave satisfied. Redraft proceeds normally.
- `pass-with-findings` — substantive issues exist but none block closeout. Redraft proceeds, addressing findings explicitly in the change log and possibly in the next wave's plan.
- `fail` — one or more exit criteria not met in fact (not just admitted), a commitment violated without a supersede proposal, or entry criteria for the next wave unsatisfied. Redraft cannot close this wave. Either loop back to execute or explicitly renegotiate via scope change, both of which surface to the user.

## 11. Invariants

Rules every skill must honor. Violating one is a schema-level bug, not a judgment call.

1. **The wave doc is the single source of truth.** Skills do not maintain parallel state.
2. **Future waves never get task-level detail, per-story acceptance, or feature definitions.** Only titles, themes, sketches, and sketched criteria. Anything beyond that in a future-wave section is a schema violation.
3. **Every current-wave task has acceptance criteria.** A task without acceptance cannot be honestly closed.
4. **Every current-wave story has acceptance criteria.** Story-level acceptance drives task-level acceptance and audit checks.
5. **Every wave has exit criteria and a repro path.** A wave without them cannot be audited independently.
6. **Every story and feature that falls in-scope is traced to a wave.** Items that belong to the product vision but aren't yet waved live in Section 9 (Themes not yet waved), not as loose bullets.
7. **Registers are append-only.** Assumptions, risks, and commitments are never deleted. Wrong ones are marked broken/superseded and replaced with a new ID. The history is the context.
8. **The change log is append-only.** Entries are never rewritten.
9. **Execution and audit reports do not modify the wave doc.** Only `wave-redraft` modifies the doc. Execute writes the execution report; audit writes the audit report; redraft interprets both.
10. **Scope expansion requires an explicit change-log entry.** If a redraft adds work that wasn't in scope before, it's called out by name and rationale — never silently absorbed.
11. **Walking-skeleton default.** W1 is a vertical slice that exercises the full architecture with minimal functional content — unless the Goal section explicitly justifies a horizontal foundation as W1. The draft skill must carry that justification forward where applicable.
12. **One expansion per redraft.** Exactly one future wave — the new current wave — is expanded per redraft cycle. Other future waves stay as sketches.
13. **Pivots bump frontmatter status to `pivoted`.** Cleared back to `in_progress` by the next successful execute/audit/redraft cycle.
14. **Audit verdict gates redraft closeout.** A `fail` verdict blocks closeout until addressed.
15. **Retired wave IDs are never reused.** After a pivot, W3 stays retired; introduce W5, W6, etc.

## 12. Worked mini-example

A tiny wave doc for a CLI tool that tags files by content. Shown here to make the schema concrete end-to-end.

```markdown
---
wave_doc_version: 2
created: 2026-04-22
last_updated: 2026-04-26
source_spec: filetagger-brief.md
current_wave: W2
status: in_progress
---

# filetagger — Wave Doc

## 1. Goal and non-goals
A local CLI that reads files in a directory and attaches content-derived
tags (topic, sentiment, language) as xattrs or a sidecar index. Non-goals:
no cloud sync, no GUI, no write-back into file contents.

Success: a user can run `filetagger scan ~/Documents` and then
`filetagger find topic:invoices` and get accurate results in under
two seconds for 10k files.

## 2. Roles
| Role | What they're trying to do |
|------|---------------------------|
| User | Find files by what they're about, not just their name. |

## 3. Waves overview
| Wave | Name                        | Status       | One-line goal |
|------|-----------------------------|--------------|---------------|
| W1   | Scan and tag (skeleton)     | complete     | One file in, one tagged row out, end-to-end. |
| W2   | Query by tag                | in_progress  | User can find files by tag combinations. |
| W3   | Incremental re-scan         | future       | Re-scans only touch changed files. |

## 4. Waves (detailed)

### W1 — Scan and tag (walking skeleton)
Status: complete
Completed: 2026-04-25
Theme: ingest
Delivered: `filetagger scan <file>` reads a single file, calls the LLM
  tagger once, writes one row to a SQLite index at `~/.filetagger/index.db`.
  Walking skeleton: the whole pipeline works; only one file is processed.
Assumptions resolved: A1 validated.
Commitments established: AC1, AC2, AC3.
Stories closed: US-USR-1a (minimal scan).
Features delivered: F-1a (minimal tagger).
Execution report: filetagger-wave-doc.reports/wave-W1-execution.md
Audit report: filetagger-wave-doc.reports/wave-W1-audit.md

### W2 — Query by tag
Status: in_progress
Started: 2026-04-25
Theme: query
Goal: User can run `filetagger find <query>` and get matching paths.
Depends on: W1

Entry criteria:
- Index schema from W1 is stable (confirmed by audit).
- At least one scanned file exists in the index (repro uses a fixture).
Exit criteria:
- `filetagger find topic:X` returns exact matches.
- Boolean queries (`topic:X AND lang:en`) parse and execute.
- Query on 10k-file fixture index completes in under 2s p95.
Repro: scripts/demo-w2.sh — seeds a 10k-file fixture index and runs the
  three exit-criteria checks, printing PASS/FAIL per check.

Assumptions: A3, A4
Risks: R1
Commitments respected: AC1, AC2, AC3

#### Stories
- **US-USR-2: Find files by tag**
  As a user, I want to query the index by tag expressions, so that I can
  locate files by what they're about.
  Acceptance:
  - Given a populated index, when I run `filetagger find topic:invoices`,
    then I see all paths tagged `topic:invoices`, one per line.
  - Given a boolean query `topic:invoices AND lang:en`, when I run it,
    then results match both clauses.
  Priority: must-have

#### Features
- **F-2: Query parser and executor**
  Description: Parses tag-expression syntax and executes against the SQLite
  index.
  Supports stories: US-USR-2
  Priority: must-have

- **F-3: `find` CLI surface**
  Description: Exposes the query engine via `filetagger find` with
  argument parsing and output formatting.
  Supports stories: US-USR-2
  Priority: must-have

#### Tasks
- [x] T2.1 — Query parser for tag:value and AND/OR/NOT.
      Acceptance: unit tests cover all operator combinations; syntax
      errors produce clear messages citing column position.
      Serves: F-2
- [x] T2.2 — Query executor against SQLite index.
      Acceptance: returns correct matches for the parser's AST;
      benchmark on synthetic 10k-file index shows < 2s p95.
      Serves: F-2
- [ ] T2.3 — CLI surface for `find` subcommand.
      Acceptance: `filetagger find --help` shows help; arg parsing
      errors exit non-zero; default output is one path per line; JSON
      via `--json`.
      Serves: F-3, US-USR-2
- [ ] T2.4 — End-to-end demo and repro.
      Acceptance: `scripts/demo-w2.sh` exists, is executable, seeds a
      fixture index, runs all three exit criteria, and prints PASS/FAIL
      per check. Passes in CI.
      Serves: plumbing (repro path)

### W3 — Incremental re-scan
Status: future
Theme: efficiency
Goal: Re-tag only files that changed since last scan.
Depends on: W1, W2

Entry criteria (sketch): query engine from W2 stable enough that re-scan
  correctness can be verified by query.
Exit criteria (sketch):
- `filetagger scan --incremental <dir>` re-tags only changed/new files.
- A full re-scan after small edits completes 10x faster than cold scan.
Candidate stories:
  - Re-scan only changed files.
  - Fall back to full scan if signals are unreliable.
Anticipated features:
  - Change detection (mtime + size + content hash).
  - Fallback logic for unreliable filesystems.
Assumptions: A5
Risks: R2
Commitments respected: AC1, AC2, AC3
Sketch: Compare mtime + size + stored content hash to decide whether to
  re-tag. Fall back to full scan if index schema changed.

## 5. Assumptions register

- **A1** — SQLite handles 10k-file indexes fast enough for interactive
  queries. *Wave: W1, W2. Status: validated (2026-04-25).*
- **A2** — One tag set per file (flat namespace). *Wave: W1. Status: broken
  (2026-04-23) — users want multi-set.* Superseded by A3.
- **A3** — Tag namespace is flat with string prefixes (e.g., `work/topic:X`).
  *Wave: W1, W2. Status: validated (2026-04-25).*
- **A4** — Query latency is dominated by SQLite, not the LLM (queries
  never call the tagger). *Wave: W2. Status: untested.*
- **A5** — mtime + size is a reliable change signal on target
  filesystems. *Wave: W3. Status: open.*

## 6. Risks register

- **R1** — Boolean query parser may misinterpret ambiguous queries.
  *Wave: W2. Likelihood: medium. Impact: low. Status: open.*
  *Mitigation: echo parsed AST on `--explain`; document precedence.*
- **R2** — Filesystems without mtime precision break incremental scan.
  *Wave: W3. Likelihood: low. Impact: medium. Status: open.*
  *Mitigation: detect and fall back to full scan with a warning.*

## 7. Architectural commitments register

- **AC1** — Persistence: SQLite at `~/.filetagger/index.db`.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: zero-ops, embedded, fast enough for target scale.*
- **AC2** — Tagger: remote LLM API, configurable provider.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: tag quality is the product; local models not yet competitive.*
- **AC3** — Distribution: single-binary CLI via PyInstaller.
  *Established: W1 (2026-04-25). Status: active.*
  *Rationale: users install one file; no runtime dependency hell.*

## 8. Change log

### 2026-04-26 — Redraft after W1 closeout
Type: normal-redraft
- Closed W1 (walking skeleton). Exit criteria met.
- A2 broken during W1 scan design; A3 opened and validated in the same
  wave after refactoring tag namespace to string prefixes.
- AC1, AC2, AC3 established.
- Expanded W2 sketch into full detail. current_wave advanced to W2.
- Re-sketched W3 briefly to confirm re-scan works against the string-
  prefixed tag namespace.

### 2026-04-22 — Wave doc created
Type: initial-draft
- Drafted from filetagger-brief.md.
- Three waves; W1 fully planned as walking skeleton, W2-W3 sketched.
- 5 assumptions, 2 risks, 3 anticipated commitments seeded from the brief.

## 9. Themes not yet waved
- Watch mode (inotify-driven continuous retagging).
- Multi-machine sync of indexes.
- GUI frontend.
```

---

This schema is the contract. If a skill needs to deviate, the schema changes first (and the change is a change-log entry in this file's own git history, not in any wave doc).
