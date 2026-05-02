# Wave Doc Schema

The wave doc is the central operating artifact of the **VADER** loop. It unifies requirements and plan into a single rolling document, organized wave by wave. The current wave is specified and planned in full; future waves are sketched as themes; past waves carry compact closeout summaries.

This schema is the contract between four skills:

- `wave-draft` — writes the first version of the wave doc from the vision and architecture artifacts.
- `wave-execute` — reads the wave doc, implements the current wave, and produces an execution report.
- `wave-audit` — independently verifies the current wave against the wave doc, the architecture doc and ADRs, and the execution report. Produces an audit report.
- `wave-redraft` — reads the wave doc, both reports, and the architect-review report. Closes the current wave, expands the next wave's sketch into full detail, re-sketches remaining waves.

Two adjacent skills also bear on the wave doc:

- `architect-review` reads the wave doc and the wave's reports, and produces an architect-review report. It does not write to the wave doc.
- `vision-pivot` does not write to the wave doc, but a vision pivot triggers a reconciling redraft cycle that will edit the wave doc substantially.

All readers and writers must follow this schema. If a skill needs information not in the schema, either the schema is wrong (update it here first) or the skill is overreaching (pull it back).

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Top-level structure](#3-top-level-structure)
4. [Per-wave structure](#4-per-wave-structure)
5. [Assumptions register](#5-assumptions-register)
6. [Risks register](#6-risks-register)
7. [ADR references](#7-adr-references)
8. [Change log](#8-change-log)
9. [Execution report template](#9-execution-report-template)
10. [Audit report template](#10-audit-report-template)
11. [Architect-review report](#11-architect-review-report)
12. [Cycle order and gating](#12-cycle-order-and-gating)
13. [Pivot handling](#13-pivot-handling)
14. [Invariants](#14-invariants)
15. [Worked mini-example](#15-worked-mini-example)

---

## 1. Philosophy

Rolling-wave development exists because later-wave certainty is an illusion. The further ahead we specify and plan, the more the document is speculation dressed up as detail. The discipline says: **specify and plan the current wave comprehensively, sketch future waves concisely, execute one wave at a time, and commit to learning between waves**.

VADER inherits this from DEAR and adds two things:

**The vision and architecture artifacts are upstream of the wave doc.** Goal, non-goals, and roles come from the vision; structural decisions come from the architecture doc and the ADR log. The wave doc references both rather than duplicating them, so they can be edited (under their own discipline) without rewriting the wave doc.

**The cycle has two verification gates per wave.** `wave-audit` checks whether the wave's claimed outcomes hold up. `architect-review` checks whether the architecture's claimed adherence holds up. Both gates produce reports; the redrafter consumes both before advancing.

Three operating principles thread through the schema:

**Current in detail, future in sketch.** Future waves carry only titles, themes, sketches, and sketched criteria. Anything beyond that in a future-wave section is a schema violation.

**Every claim is traceable.** Stories cite features; features cite waves; tasks cite stories or features and the modules / ADRs they touch. A reader walking backward from any statement can reach its origin in the vision, the architecture doc, or a previous wave's reports.

**Surprises are first-class.** Discoveries during execution are the point, not a failure. The schema has dedicated places to record them — per-task, per-wave, per-doc — so they can't be buried.

## 2. File format and location

One markdown file per project, named `<project-slug>-wave-doc.md`. The file lives in the project's `docs/` directory alongside the vision doc and architecture doc.

YAML frontmatter holds machine-parseable state. Markdown body holds detail. Reports archive under `<project-slug>-wave-doc.reports/`.

```yaml
---
wave_doc_version: 3                           # Incremented by each redraft pass
created: 2026-05-02                           # ISO date, never changes
last_updated: 2026-06-15                      # ISO date, updated each redraft
source_vision: bookclub-vision.md             # Path to the vision doc
source_architecture: bookclub-architecture.md # Path to the architecture doc
adr_log: bookclub-adr/                        # Path to the ADR directory
current_wave: W2                              # The wave currently being executed
status: in_progress                           # in_progress | complete | paused | pivoted
---
```

`status` values:
- `in_progress` — normal operating state.
- `complete` — all waves closed out.
- `paused` — deliberately halted; requires human input before resuming.
- `pivoted` — a redraft followed a vision-pivot or substantial-replan; some wave IDs may have been retired. Cleared back to `in_progress` after the next successful execute/audit/architect-review/redraft cycle.

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
## 7. ADR references
## 8. Change log
## 9. Themes not yet waved
```

### 1. Goal and non-goals

Two or three short paragraphs restating the project's goal, what success looks like, and explicit non-goals. **Drawn from the vision doc**, not invented. If the wave doc's goal contradicts the vision doc's, the vision wins; raise the contradiction to the redrafter or trigger a vision-pivot. The wave doc's goal section is the executor and auditor's quick-reference for in-scope vs. out-of-scope decisions; it must not drift from the vision.

### 2. Roles

A compact table of user roles, mirroring the vision doc's Section 2.

```markdown
| Role | What they're trying to do |
|------|---------------------------|
| ...  | ...                       |
```

Roles span the whole project, not individual waves. New roles added later are a notable event and get a change-log entry — usually corresponding to a vision pivot.

### 3. Waves overview

A one-glance summary: the wave ladder.

```markdown
| Wave | Name                         | Status      | One-line goal |
|------|------------------------------|-------------|---------------|
| W1   | Walking skeleton             | complete    | End-to-end login + empty dashboard. |
| W2   | Nomination and voting flow   | in_progress | Members can pick the next book. |
| W3   | Scheduling and RSVPs         | future      | A meeting is on the calendar. |
```

### 4. Waves (detailed)

One subsection per wave, in order. Format depends on wave status — see [Section 4](#4-per-wave-structure).

### 5, 6. Registers

Assumptions and risks are flat lists, referenced by ID from waves, stories, features, and tasks. See [Section 5](#5-assumptions-register) and [Section 6](#6-risks-register).

### 7. ADR references

A pointer table from each ADR ID to the waves that respect it, establish it, or supersede it. The ADR file itself is the source of truth; this table is a cross-reference for navigation. See [Section 7](#7-adr-references).

### 8. Change log

Append-only. One entry per redraft pass.

### 9. Themes not yet waved

Themes the project intends to address but hasn't yet assigned to a wave. One bullet per theme. A theme graduates to a future-wave sketch the first time a redraft pass decides to plan it.

## 4. Per-wave structure

Every wave uses the same skeleton. The **depth** of each field depends on the wave's status. This makes rolling-wave discipline structural.

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
Candidate stories: <titles only, no acceptance criteria, no IDs yet>
  - ...
Anticipated features: <titles only, no detail>
  - ...
Assumptions: A<N>, A<N>
Risks: R<N>
ADRs respected: ADR-NNN, ADR-NNN
New ADRs anticipated: <one-line titles only>
Sketch: 2-4 sentences describing approach.
```

No task breakdowns. No per-story acceptance criteria. No feature definitions beyond titles. No repro path. **Any of those in a future-wave section is a schema violation.**

### Current wave (fully planned)

A current wave has the sketch fields in full detail, plus execution-ready fields.

```markdown
Started: 2026-05-08

Entry criteria: <precise, satisfied by prior waves' outputs>
Exit criteria: <testable; each bullet verifiable by an independent auditor>
Repro: Path to a script or command an auditor can run end-to-end.

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
  Notes: <if any>

#### Tasks
- [ ] T<N>.1 — <short task description>
      Acceptance: <one or two concrete testable conditions>
      Serves: <US or F IDs the task advances, or "plumbing" if implicit>
      Touches: <module names from architecture doc; ADRs respected>
- [ ] T<N>.2 — ...

Assumptions: A<N>, A<N>
Risks: R<N>
ADRs respected: ADR-NNN, ADR-NNN
New ADRs proposed: ADR-NNN (proposed)   # If any will be established by this wave
```

Story, feature, and task guidelines are unchanged from DEAR — same INVEST filter for stories, same one-session sizing for tasks, same mandatory acceptance criteria for both.

Checkbox state (`[ ]` / `[x]`) is the single source of truth for task status. The executor flips them as it finishes each task; no other skill touches them.

### Past waves (closeout)

When a wave completes, its detailed content is replaced by a compact closeout summary. The story list, feature list, and task list are removed (the reports archive them); what remains is the learning.

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
Audit report: <path>
Architect-review report: <path>
```

## 5. Assumptions register

Flat list. Waves, stories, features, and tasks reference entries by ID.

```markdown
- **A1** — Club sizes stay under ~20 members. *Wave: W1. Status: untested.*
- **A2** — Voting is single-choice per member, not ranked. *Wave: W2. Status: broken (2026-06-12) — superseded by A6.*
- **A3** — Magic-link auth is acceptable for guest access. *Wave: W1. Status: validated (2026-05-15).*
- **A6** — Members prefer ranked-choice voting over single-choice. *Wave: W2. Status: open.* Replaces: A2.
```

Status values: `untested` | `open` | `validated` | `broken`.

Rules (unchanged from DEAR): never delete; broken assumptions are superseded with new IDs; status changes are dated; assumption bodies are never edited.

## 6. Risks register

Same flat-list shape as assumptions, with mitigation instead of status text. Risks have their own status: `open` | `retired (did not materialize)` | `triggered — mitigated` | `triggered — unresolved`.

## 7. ADR references

A pointer table, not the source of truth. The architecture doc's `<project>-adr/` directory holds the actual ADR files.

```markdown
| ADR     | Title                              | Established | Status                           | Cited by                   |
|---------|------------------------------------|-------------|----------------------------------|----------------------------|
| ADR-001 | Persistence: SQLite local file     | W1          | Accepted                         | W1, W2                     |
| ADR-002 | Magic-link auth, no passwords      | W1          | Accepted                         | W1                         |
| ADR-004 | Voting data model: flat columns    | W2 sketch   | Superseded (2026-06-12) by ADR-007 | (historical)             |
| ADR-007 | Voting data model: row-per-rank    | W2          | Accepted                         | W2, W3 (anticipated)       |
```

The "Cited by" column is denormalized from the wave-detail sections and updated by the redrafter.

A new ADR enters this table when `architect-review` proposes it. It enters with `Status: Proposed` and is moved to `Accepted` only when the redrafter expands the next wave that ratifies it.

## 8. Change log

Append-only. One entry per redraft pass, even if the redraft was minimal — so the history is complete.

```markdown
### 2026-06-15 — Redraft after W2 closeout
Type: normal-redraft
- Closed W2. All exit criteria met.
- A2 (single-choice voting) marked broken; A6 (ranked-choice) opened.
- ADR-004 (flat vote columns) superseded by ADR-007 (row-per-rank),
  per architect-review report.
- Architecture doc bumped to v4 (Section 4 Data model edited per ADR-007).
- Expanded W3 sketch into full detail. current_wave advanced to W3.
- Re-sketched W4 to account for ranked-voting data shape.

### 2026-05-08 — Wave doc created
Type: initial-draft
- Drafted from bookclub-vision.md (v1) and bookclub-architecture.md (v1)
  with seed ADRs ADR-001 through ADR-005.
- Four waves; W1 fully planned as walking skeleton; W2-W4 sketched.
- Assumptions A1-A5 and risks R1-R2 seeded from vision Open Questions.
```

`Type` values:
- `initial-draft` — first write by `wave-draft`.
- `normal-redraft` — routine: one wave closed, next wave planned, minor register updates.
- `substantial-redraft` — multiple assumptions broken, multiple future waves materially changed. Doc still coherent.
- `vision-pivot-redraft` — the vision was pivoted; this redraft reconciles the wave doc to the new vision. Retired wave IDs and superseded ADRs are listed; new wave IDs may appear. Frontmatter `status` is set to `pivoted` until a subsequent execute/audit/architect-review/redraft cycle clears it.

## 9. Execution report template

Produced by `wave-execute` at the end of each wave. Read by `wave-audit` (to verify) and (later) `wave-redraft`.

Location: `<project-slug>-wave-doc.reports/wave-W<N>-execution.md`.

```markdown
---
wave: W<N>
wave_start_ref: <git-sha-at-start>      # captured by wave-execute at start of work; empty if no git
wave_end_ref: <git-sha-at-end>          # captured by wave-execute at end; empty if no git
completed: 2026-06-12
wave_doc_version_at_start: 2
---

# W<N> <Wave name> — Execution Report

## What was built
Prose summary of actual outcome — what a user can now do that they
couldn't before. Reference completed task IDs and the stories/features
they delivered. Not a commit log; a capability summary.

## Task status
- [x] T2.1 — ...
- [~] T2.4 — Partial: <what's missing and why>

## Exit criteria status
- [x] <criterion>: <evidence>
- [~] <criterion>: <gap>

## Assumptions status
- A<N>: validated | broken — <evidence or recommended replacement>

## ADR adherence
For each ADR cited by this wave, did the implementation respect it?
- ADR-001: respected.
- ADR-004: violated — implementation required a row-per-rank shape;
  recommend supersede via architect-review.

## Spec-level discoveries
Things learned about users, stories, or features that change future waves.

## Plan-level discoveries
Things learned about implementation that change future waves.

## Proposed scope changes
Explicit, bulleted — each with one-line rationale.

## Risks encountered
- R<N>: did not materialize | materialized — <what happened>
- New risks: ...

## Readiness for next wave
Prerequisites the next wave needs that weren't originally planned.
```

A section may be omitted **only** if it would be empty.

## 10. Audit report template

Produced by `wave-audit` after `wave-execute`. Verifies the execution report against the wave doc and the artifacts.

Location: `<project-slug>-wave-doc.reports/wave-W<N>-audit.md`.

```markdown
---
wave: W<N>
verdict: pass-with-findings              # pass | pass-with-findings | fail
audited: 2026-06-12
wave_doc_version_at_audit: 2
execution_report: wave-W<N>-execution.md
diff_baseline: <git-sha>                 # copied from execution report's wave_start_ref
diff_head: <git-sha>                     # commit at the time of audit
---

# W<N> <Wave name> — Audit Report

## Verdict
pass | pass-with-findings | fail

One-paragraph summary justifying the verdict.

## Exit criteria verification
For each exit criterion: pass / fail / unverifiable, with reproduction step.
- [x] <criterion> — verified by <evidence>
- [~] <criterion> — finding F<N>

## Task verification
Cross-reference the report's claimed task status against the wave doc's
checkboxes and the repo diff. Flag discrepancies.

## Assumption verification
For each assumption the report claims to have resolved, check the evidence.

## ADR adherence
For each ADR cited by this wave, confirm adherence independently.
Disagreement with the execution report's ADR-adherence section goes
under Findings.

## Scope findings
Changes in the diff that don't map to planned tasks or declared
discoveries. None is ideal; any means investigate.

## Entry-criteria check for next wave
Per the wave doc's W<N+1> entry criteria (sketch), check whether this
wave's outputs satisfy them. If not, flag what's missing.

## Findings
- **F1** — <description>. Severity: low | medium | high.
  Recommendation: <one or two sentences>.

## Recommendations to architect-review and redrafter
Brief — name the issues that need a decision, not prescriptions for
how to decide them.
```

Verdict guidance:
- `pass` — all exit criteria met, all claims verified, no scope leakage, no ADR violations.
- `pass-with-findings` — substantive issues but none block closeout. Architect-review and redraft proceed, addressing findings explicitly.
- `fail` — exit criteria not met, ADR violated without a supersede proposal, or next-wave entry criteria unsatisfied. Architect-review and redraft cannot close this wave.

## 11. Architect-review report

Produced by `architect-review` after `wave-audit`. Format defined in `architecture-schema.md` Section 6. Lives at `<project-slug>-wave-doc.reports/wave-W<N>-architect-review.md`.

The architect-review report is required for wave closeout in normal cycles. It can be skipped only if the audit verdict is `fail` (in which case the cycle loops back to execute or to scope renegotiation, neither of which involves architecture review).

## 12. Cycle order and gating

The per-wave loop is strictly ordered:

```
wave-execute → wave-audit → architect-review → wave-redraft
```

Gating rules:

- `wave-audit` runs only after `wave-execute` produces an execution report.
- `architect-review` runs only after `wave-audit` produces an audit report whose verdict is `pass` or `pass-with-findings`. A `fail` verdict blocks architect-review.
- `wave-redraft` runs only after both audit and architect-review reports exist (in the normal-cycle case). On a `fail` audit, the user decides whether to loop back to `wave-execute` or to renegotiate scope explicitly via `wave-redraft`; in either case the architect-review is skipped, and the eventual redraft change-log entry says so.

Each step is invoked by the user. No skill auto-invokes the next.

## 13. Pivot handling

Pivots can originate at two layers, with different cascades.

**Wave-doc pivot (substantial-redraft or pivot type).** The vision is unchanged, but multiple wave-level decisions are revised. Type in change log: `substantial-redraft` if waves are revised but the wave ladder shape persists, or a wave-doc-level `pivot` if wave IDs are retired. Frontmatter `status` becomes `pivoted` for a wave-doc-level pivot.

**Vision pivot.** The vision doc is revised by `vision-pivot`, which sets vision frontmatter to `pivoted`. The next `wave-redraft` invocation must produce a `vision-pivot-redraft` change-log entry that:

1. Notes the source vision change (which sections were revised in vision-version N).
2. Reconciles the wave doc's Goal and Roles sections to match the new vision.
3. Retires any waves whose goal no longer fits the new vision. Retired wave IDs are listed; never reused.
4. Introduces new wave IDs as needed (W7, W8, ... — never reusing retired numbers).
5. Triggers an architecture review check: if any ADRs are now invalid under the new vision, mark them for supersession in the next architect-review pass.
6. Sets wave-doc frontmatter `status: pivoted` until the next successful execute/audit/architect-review/redraft cycle.

The vision pivot does *not* edit the wave doc directly. `vision-pivot` only edits the vision and signals the wave-redraft cycle to reconcile.

## 14. Invariants

Rules every skill must honor.

1. **The wave doc is the single source of truth for project state below the vision.** Skills do not maintain parallel state for waves, assumptions, risks, or ADR cross-references.
2. **The vision and architecture are upstream sources of truth.** The wave doc's Goal/Roles mirror the vision; the wave doc's ADR references mirror the ADR log. Drift is reported and fixed; not papered over.
3. **Future waves never get task-level detail, per-story acceptance, or feature definitions.** Only titles, themes, sketches, and sketched criteria.
4. **Every current-wave task has acceptance criteria.** No exceptions.
5. **Every current-wave story has acceptance criteria.**
6. **Every wave has exit criteria and a repro path.** A wave without them cannot be audited independently.
7. **Registers are append-only.** Assumptions, risks, and the ADR-references table are never shrunk; broken or superseded entries are kept with new IDs replacing them.
8. **The change log is append-only.** Entries are never rewritten.
9. **Execution and audit reports do not modify the wave doc.** Only `wave-redraft` modifies the doc.
10. **Architect-review does not modify the wave doc.** It only modifies the architecture doc and ADR log; its findings are absorbed into the wave doc by `wave-redraft`.
11. **Scope expansion requires an explicit change-log entry.** No silent absorption.
12. **Walking-skeleton default for W1.** Vertical slice exercising the full architecture; horizontal-foundation W1 requires explicit justification in the Goal section.
13. **One expansion per redraft.** Exactly one future wave is expanded per redraft cycle.
14. **Audit verdict gates architect-review and redraft.** A `fail` verdict blocks both until addressed.
15. **Architect-review verdict (proposed ADRs / supersessions) gates redraft.** Redraft cannot ratify or expand without architect-review's input on the cycle.
16. **Pivots bump frontmatter status to `pivoted`.** Cleared back to `in_progress` only by the next successful full cycle.
17. **Retired wave IDs and superseded ADR IDs are never reused.**
18. **ADRs cited by the architecture doc must be ratified (`Status: Accepted`) before `wave-draft` runs.** Seed ADRs from `architect-draft` start as `Proposed` and are ratified by the human (manual edit or `architect-draft --ratify`). Mid-cycle ADRs from `architect-review` start as `Proposed` and are ratified by `wave-redraft`. `wave-draft` and `wave-execute` refuse to run against un-ratified seed ADRs.
19. **No skill auto-invokes the next.** Each step is invoked by the human lead. The optional `vader-next` helper dispatches the next skill *only* on explicit user confirmation per invocation; it is not an exception to this rule.

## 15. Worked mini-example

A truncated wave doc for `filetagger`, a CLI that tags files by content, after W1 closeout and W2 in progress:

```markdown
---
wave_doc_version: 2
created: 2026-05-02
last_updated: 2026-05-26
source_vision: filetagger-vision.md
source_architecture: filetagger-architecture.md
adr_log: filetagger-adr/
current_wave: W2
status: in_progress
---

# filetagger — Wave Doc

## 1. Goal and non-goals
A local CLI that tags files in a directory by content (topic, sentiment,
language) and lets users find files by tag combinations. Non-goals: no
cloud sync, no GUI, no write-back into file contents.

(Drawn from filetagger-vision.md §1, §4, §5.)

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
- **A2** — One tag set per file (flat). *Wave: W1. Status: broken — superseded by A3.*
- **A3** — Tag namespace is flat with string prefixes. *Wave: W1, W2. Status: validated (2026-05-15).*
- **A4** — Query latency is dominated by SQLite, not the LLM. *Wave: W2. Status: untested.*
- **A5** — mtime + size is a reliable change signal. *Wave: W3. Status: open.*

## 6. Risks register
- **R1** — Boolean parser may misinterpret ambiguous queries. *Wave: W2. Likelihood: medium. Impact: low. Status: open.* *Mitigation: echo parsed AST on `--explain`.*
- **R2** — Filesystems without mtime precision break incremental scan. *Wave: W3. Likelihood: low. Impact: medium. Status: open.* *Mitigation: detect and fall back to full scan with warning.*

## 7. ADR references
| ADR     | Title                          | Established | Status   | Cited by   |
|---------|--------------------------------|-------------|----------|------------|
| ADR-001 | Persistence: SQLite local file | W1          | Accepted | W1, W2, W3 |
| ADR-002 | Tagger: remote LLM API         | W1          | Accepted | W1, W2     |
| ADR-003 | Distribution: single-binary    | W1          | Accepted | W1, W2, W3 |
| ADR-004 | Tag namespace: string-prefixed | W1          | Accepted | W1, W2     |

## 8. Change log
### 2026-05-26 — Redraft after W1 closeout
Type: normal-redraft
- Closed W1 (walking skeleton). Exit criteria met.
- A2 broken during W1; A3 opened and validated.
- ADR-004 established (string-prefixed tag namespace).
- Expanded W2 sketch into full detail. current_wave advanced to W2.
- Re-sketched W3 briefly to confirm re-scan against the prefixed namespace.

### 2026-05-02 — Wave doc created
Type: initial-draft
- Drafted from filetagger-vision.md (v1) and filetagger-architecture.md (v1)
  with seed ADRs ADR-001, ADR-002, ADR-003.
- Three waves; W1 fully planned as walking skeleton; W2-W3 sketched.
- 5 assumptions, 2 risks seeded from vision Open Questions.

## 9. Themes not yet waved
- Watch mode (continuous retagging on file change).
- Multi-machine sync of indexes.
- GUI frontend.
```

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
