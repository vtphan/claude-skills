# Architecture Doc and ADR Schema

The architecture artifact in **VADER** is two coupled things: a single architecture doc that describes *how* the system is built, and an append-only log of Architecture Decision Records (ADRs) that capture *why* each structural choice was made.

This schema is the contract between two skills:

- `architect-draft` — produces the initial architecture doc and seeds the first ADRs from the vision and (optionally) a draft wave doc.
- `architect-review` — runs after each wave's audit, before the redraft. Reads the wave's execution and audit reports and proposes new ADRs, supersession of existing ADRs, or (rarely) edits to the architecture body. It produces an architecture-review report that the redrafter consumes.

Other VADER skills *read* the architecture doc and *cite* ADRs by ID but do not write to either.

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Architecture doc structure](#3-architecture-doc-structure)
4. [ADR file structure](#4-adr-file-structure)
5. [Supersession and lifecycle](#5-supersession-and-lifecycle)
6. [Architecture-review report](#6-architecture-review-report)
7. [Relationship to the wave doc](#7-relationship-to-the-wave-doc)
8. [Invariants](#8-invariants)
9. [Worked mini-example](#9-worked-mini-example)

---

## 1. Philosophy

Most projects let architectural decisions stay implicit in the code. That works until it doesn't — a year in, no one remembers why the auth model is what it is, every refactor re-litigates settled questions, and silent drift accumulates between what was decided and what is.

VADER makes architecture explicit through a deliberate split:

**The architecture doc is the *current* picture of the system.** It is revised in place when the picture changes, but only via the ADR mechanism. A reader who wants to know "how is this system structured today?" reads exactly this doc.

**ADRs are the *history* of structural decisions.** Each ADR is a single decision: context, the choice, consequences. Once accepted, an ADR is never edited; it can only be *superseded* by a later ADR. A reader who wants to know "why is this system structured this way?" walks the ADR log.

Three operating principles thread through the schema:

**No architecture body change without an ADR.** The architecture doc is a thin, current view; the ADR log is the durable record of choice. If the body changes without an ADR explaining why, history is lost and audit becomes impossible.

**Architecture is revisable but not casually so.** `architect-review` runs every cycle and is allowed to propose changes — that's the whole point of including it. But every change is an ADR, and every supersession preserves the prior ADR. Revision is encouraged; amnesia is not.

**ADRs and assumptions are different.** Assumptions are claims about the world that may be wrong ("users tolerate magic-link auth"). ADRs are choices we made given those assumptions ("we chose magic-link auth because..."). Both registers are append-only; both supersede rather than overwrite. They are kept separate because their lifecycles differ — assumptions resolve via validation, ADRs resolve via supersession.

## 2. File format and location

Two artifacts per project, both under `docs/`:

- `<project-slug>-architecture.md` — the architecture doc.
- `<project-slug>-adr/ADR-NNN-<slug>.md` — one file per ADR. Numbered sequentially, never reused.

The architecture doc carries its own frontmatter:

```yaml
---
architecture_version: 4                  # Incremented on body edit
created: 2026-05-02                      # ISO date, never changes
last_updated: 2026-06-15                 # ISO date, updated on body edit
status: active                           # active | pivoted
adr_log: docs/<project-slug>-adr/        # Path to the ADR directory
---
```

`status` values mirror the vision doc. `pivoted` is set when a vision pivot has cascaded into architectural changes; cleared when those changes have been absorbed into a redrafted wave doc.

ADR files do not carry frontmatter; their metadata lives in the file body (Section 4 below).

## 3. Architecture doc structure

The architecture doc has exactly seven numbered sections.

```markdown
# <Project> — Architecture

## 1. System overview
## 2. Module decomposition
## 3. Key interfaces
## 4. Data model
## 5. Auth and identity
## 6. Deployment and operations
## 7. Non-functional considerations
```

### 1. System overview

Two or three short paragraphs and (optionally) a single block diagram in ASCII. A reader unfamiliar with the project should be able to learn the shape of the system from this section alone — what runs where, what the major components are, what the request lifecycle looks like end to end.

The system overview is the part most likely to drift; `architect-review` should treat it as the canary for whether the architecture body needs an edit.

### 2. Module decomposition

A table or structured list of modules / packages / services. For each: name, responsibility (one sentence), the ADR(s) that govern it. Modules are the units the wave doc's tasks reference (e.g., "T2.1 — Touches: module `auth`").

```markdown
| Module      | Responsibility                                  | Governed by |
|-------------|-------------------------------------------------|-------------|
| `auth`      | Magic-link issuance, session validation         | ADR-002     |
| `clubs`     | Club state, membership, ownership transitions   | ADR-005     |
| `polls`     | Nomination, voting, tally                       | ADR-007     |
| ...         | ...                                             | ...         |
```

### 3. Key interfaces

The contracts between modules — function signatures, message formats, API endpoints, schema contracts — at the coarsest level that's still useful. Not exhaustive; just the interfaces that matter for module-to-module reasoning. Each contract cites the ADR that established it.

### 4. Data model

The persistence model: tables, collections, schemas, primary keys, important indexes. Flag fields whose presence is itself a decision (citing the ADR). This is the section auditors check most often when looking for silent ADR violations.

### 5. Auth and identity

The identity model: who can be authenticated, what tokens or sessions look like, what authorization boundaries exist. Cite the relevant ADRs.

### 6. Deployment and operations

How the system runs in production: hosts, processes, environments, build artifacts, observability surface, on-call surface. Even for solo or local-only systems, this section says so explicitly — "this is a single-binary CLI with no operational surface" is itself a decision, and should cite the ADR that made it so.

### 7. Non-functional considerations

Performance budgets, security posture, accessibility, internationalization, privacy, anything that crosses module boundaries. One bullet per consideration, each citing the ADR (if any) that constrains the choice.

## 4. ADR file structure

Each ADR is a single markdown file. Five sections, always in this order, no others.

```markdown
# ADR-007 — Voting data model: row-per-rank

## Status
Accepted (2026-06-12). Established by W2 architect-review.

## Context
What is the situation that forced this decision? What constraints,
assumptions, and prior choices are relevant? Reference the wave that
surfaced the need (e.g., "W2 audit revealed that the flat per-member
voting columns from the W1 sketch can't represent ranked voting
without a schema migration").

Reference the assumptions in play (e.g., "Depends on assumption A6:
members prefer ranked-choice voting"). If a prior ADR is being
superseded, name it and quote the relevant decision.

## Decision
The choice in one paragraph. Specific enough that an engineer reading
it knows what to build. "We will store one row per (member, nomination)
pair, with an integer `rank` column. A vote where the member ranked
the nomination in position 1 stores rank=1; lower ranks store higher
integers; unranked nominations store no row."

## Consequences
What does this decision make easier? Harder? What new things can we
do? What old things become more expensive? What are we committing
ourselves to (versus things we'd preserve flexibility on)?

This section is honest — list at least one negative consequence. An
ADR with no downsides is an ADR that hasn't been thought through.

## Supersedes / superseded by
- Supersedes: ADR-004 (flat per-member vote columns).
- Superseded by: <none yet> (this field is updated retroactively when
  a later ADR supersedes this one).
```

ADR IDs are sequential (ADR-001, ADR-002, ...). They are never reused. A retired or superseded ADR keeps its number forever.

## 5. Supersession and lifecycle

ADR `Status` values:

- `Proposed` — the ADR is drafted but not yet accepted. Used in two situations: (a) `architect-draft` produces seed ADRs that the human has not yet ratified, and (b) `architect-review` proposes a mid-cycle ADR that `wave-redraft` has not yet ratified.
- `Accepted` — the ADR is the current decision; modules and waves cite it.
- `Superseded` — a later ADR replaces this one. The superseded ADR is kept for history; its body is *never edited* (only its `Superseded by` line is updated to point to the new ADR).
- `Retired` — rare. The decision is no longer relevant because the area it governed has been removed from scope. Retirement requires a change-log entry in the wave doc.

ADRs follow a propose-then-ratify pattern uniformly:

- **Seed ADRs from `architect-draft`** start as `Proposed (date). Drafted by architect-draft.` They are ratified by the human (either by re-invoking `architect-draft` in ratify mode, or by manually flipping each ADR's `Status` field to `Accepted`). `wave-draft` refuses to run while any cited seed ADR is still `Proposed`.
- **Mid-cycle ADRs from `architect-review`** start as `Proposed (date). Drafted by architect-review.` They are ratified by `wave-redraft` when it expands the next wave (status moves to `Accepted (date). Established by W<N> redraft.`).

Until ratification, a proposed ADR is real (the file exists) but not yet binding on wave plans or implementation.

Supersession rules:

- A superseding ADR has its own ID and is its own file.
- Its `Supersedes:` field names the prior ADR ID.
- The superseded ADR's `Superseded by:` field is updated to point to the new ADR. **This is the only kind of edit allowed to an existing ADR.**
- Modules in the architecture doc that cited the old ADR are updated to cite the new one — this is a body edit, and is recorded by incrementing `architecture_version` and noting the supersession in the wave doc's change log.

## 6. Architecture-review report

`architect-review` produces one report per wave cycle, after `wave-audit` and before `wave-redraft`. The report lives at `<project-slug>-wave-doc.reports/wave-W<N>-architect-review.md`.

```markdown
---
wave: W<N>
summary: new-adrs-proposed              # no-changes | new-adrs-proposed | supersessions-proposed | body-edits-required
review_date: 2026-06-12
architecture_version_at_review: 3
reports_reviewed:
  - wave-W<N>-execution.md
  - wave-W<N>-audit.md
---

# W<N> Architect Review

## Summary
One paragraph: did the wave's outcome require any architectural
revision, and if so, what shape? The frontmatter `summary` field
carries the machine-readable verdict; this section is the
human-readable justification.

## Adherence check
For each ADR cited by W<N>'s tasks, confirm whether the implementation
adheres. Cross-reference against the audit report's ADR-adherence
section.
- ADR-002 (magic-link auth) — adhered.
- ADR-005 (club state model) — adhered.
- ADR-004 (flat vote columns) — violated by T2.3 implementation, which
  required a row-per-rank shape. See proposed ADR-007.

## Proposed ADRs
For each new ADR proposed, include the full ADR body inline (or as a
linked draft). The redrafter will create the file and set status to
Accepted as part of redraft.
- ADR-007 (proposed): voting data model — row-per-rank.
  Replaces: ADR-004.
  Rationale: <abbreviated; full body in the inline draft below>.

## Body edit recommendations
Specific edits to the architecture doc body that the redrafter should
make to keep the doc consistent with accepted ADRs. State each edit
as a quoted before/after.
- Section 4 (Data model): replace the `votes` table description with the
  row-per-rank schema. (Required only if ADR-007 is accepted.)

## Open architectural questions
Things the review surfaced that aren't yet decisions but might become
ADRs in a future cycle. Mirrors the vision doc's Open Questions
section but at the architecture layer.
```

The architect-review report is the *only* mechanism by which the architecture doc and ADR log change. Drift caught by other skills (the auditor, the redrafter) is reported back through this channel; it is not patched directly.

## 7. Relationship to the wave doc

The wave doc references architectural state by ID, not by inlining it. Specifically:

- The wave doc no longer carries an "architectural commitments register" of its own. Its old `Commitments respected:` field becomes `ADRs respected:`, and its `New commitments proposed:` field becomes `New ADRs anticipated:`.
- Wave-doc tasks that touch a particular module cite that module's name (from the architecture doc's Section 2) and may cite the relevant ADR.
- The wave doc's change log records ADR supersessions and architecture-version bumps as bullet entries — those are summary pointers, not the source of truth. The source of truth is the ADR file and the architecture doc.

## 8. Invariants

1. **No architecture body edit without an ADR.** Period. If you cannot point to an ADR that justifies an edit, the edit doesn't happen.
2. **ADRs are append-only.** A new ADR can be created; the `Superseded by:` line of an existing ADR can be updated retroactively when a successor exists; nothing else about an ADR is ever edited.
3. **ADR IDs are never reused.** Retired or superseded ADRs keep their numbers forever.
4. **Every ADR has a `Consequences` section with at least one negative consequence.** A decision with no downsides has not been thought through.
5. **Every architectural change traces back to a wave.** ADRs are established or superseded as a result of architect-review's analysis of a specific wave's outcome. No "drive-by" ADRs.
6. **`architect-review` is the only authorial writer; `wave-redraft` is the only ratifying writer.** `vision-shaper`, `vision-pivot`, `architect-draft` (after the initial draft), `wave-draft`, `wave-execute`, and `wave-audit` read the architecture doc and ADR log but never write to them. `architect-review` authors all *proposed* changes (new ADRs, supersessions, body edits) but writes them only as proposals (ADR status `Proposed`; body edits as quoted recommendations in its report). `wave-redraft` is the only skill that ratifies — moving proposed ADRs to `Accepted`, updating superseded ADRs' `Superseded by:` lines, and applying architect-review's body-edit recommendations. No skill authors original architectural content outside this propose-then-ratify split.
7. **Pivoted status mirrors the vision.** When the vision pivots in a way that affects architectural choices, the architecture doc is bumped to `pivoted` until the next architect-review cycle reconciles the ADR log to the new vision.

## 9. Worked mini-example

A truncated example of a single ADR file, to make the format concrete.

```markdown
# ADR-002 — Magic-link auth, no passwords

## Status
Accepted (2026-05-08). Established by W1 architect-draft.

## Context
The bookclub project (see vision §2 Target users) is a private,
small-group product. Members are typically invited by an organizer
who already has their email. The friction of password creation,
recovery, and reset would dominate the first-use experience and
disproportionately affect members who use the product infrequently
(every 2-4 weeks per club).

Assumption A3 in the wave doc states that magic-link auth is
acceptable for the target users. This ADR depends on A3.

## Decision
Authentication is via magic-link only. When a user enters their
email, the system issues a single-use, time-bounded link via email.
Clicking the link establishes a session cookie valid for 30 days.
There are no passwords. There is no recovery flow because there is
nothing to recover.

## Consequences
Easier:
- First-use UX is one input field.
- No password storage or hashing infrastructure.
- No password-reset flow to build or maintain.

Harder:
- Email deliverability becomes a hard dependency. If a user's mail
  provider delays or blocks the magic-link, the user cannot log in.
- Sessions tied to email mean account-recovery if email is lost
  requires manual intervention. Acceptable for the target user but
  a real limitation.

Negative consequences (always required):
- Reliance on email provider availability is a single point of failure.
- Power users who prefer password managers may find this awkward.

## Supersedes / superseded by
- Supersedes: <none>.
- Superseded by: <none>.
```

A second ADR superseding ADR-002 would, when written, also update ADR-002's `Superseded by:` line to point to the new ID. The original body of ADR-002 stays untouched.

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
