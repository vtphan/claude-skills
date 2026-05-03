# Architecture Doc Schema

The architecture artifact in **VADER** is a single markdown file that describes *how* the system is built. It includes an embedded Decision Log section that records the consequential structural choices (ADRs) by ID, with rationale and consequences. Separate ADR files (`docs/adr/ADR-NNN-*.md`) are *optional* — adopted only when the project earns the separation.

This schema is the contract for the `architect` skill, which has two modes:

- `architect draft` — produces the initial architecture doc and seeds the Decision Log from the vision.
- `architect ratify` — flips Proposed Decision Log entries to Accepted after human review.

Mid-cycle architectural changes are not handled by `architect`. They are detected by the review subagent inside `wave-update` and applied by `wave-update` itself. The `architect` skill is essentially a one-shot upfront tool, plus a short follow-up to ratify the initial draft.

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Architecture doc structure](#3-architecture-doc-structure)
4. [Decision Log entry format](#4-decision-log-entry-format)
5. [Lifecycle and ratification](#5-lifecycle-and-ratification)
6. [Promoting to separate ADR files](#6-promoting-to-separate-adr-files)
7. [Invariants](#7-invariants)
8. [Worked mini-example](#8-worked-mini-example)

---

## 1. Philosophy

Most projects let architectural decisions stay implicit in the code. That works until a year in, when no one remembers why the auth model is what it is. VADER makes architecture explicit through one artifact: a thin, *current* picture of the system, with a Decision Log section that records the choices and their reasons.

For small projects, embedded Decision Log entries are usually enough — they live next to the architecture they govern, and a reader doesn't need to chase across files. When the project grows (more decisions, more supersession, more cross-references), entries can be promoted to separate `docs/adr/ADR-NNN-*.md` files without changing their IDs. The promotion is opt-in and lazy.

Three operating principles thread through the schema:

**Architecture and decisions live together.** The architecture doc cites Decision Log IDs in module descriptions and key interfaces. A reader who wants to understand "why does the auth module work this way" finds the answer in the same file.

**Decisions are append-only.** A Decision Log entry can be added or marked Superseded, but the body of an Accepted entry is never edited. If the decision changes, a new entry supersedes the old one with a new ID. The old entry stays, with its `Status` updated to `Superseded`.

**Architecture is revisable but not casually so.** The propose-then-ratify pattern applies to all Decision Log entries. New entries (whether seeded by `architect` or proposed by `wave-update`'s review) start as `Proposed` and become `Accepted` only when ratified — by the human re-running `architect ratify` for initial seeds, or by `wave-update` itself for mid-cycle proposals.

## 2. File format and location

One file per project, under `docs/`:

- `<project-slug>-architecture.md` — the architecture doc, including the embedded Decision Log.

Optional, when the project earns it:

- `<project-slug>-adr/ADR-NNN-<slug>.md` — promoted ADR files. See [Section 6](#6-promoting-to-separate-adr-files).

The architecture doc carries YAML frontmatter:

```yaml
---
architecture_version: 4                  # Incremented on material architecture or Decision Log changes
created: 2026-05-02                      # ISO date, never changes
last_updated: 2026-06-15                 # ISO date, updated on any architecture doc edit
status: active                           # active | pivoted
adr_promoted_log: false                  # true once any entry has been promoted to a separate file
---
```

`status: pivoted` is set when a vision pivot has cascaded into architectural changes; cleared by the next `wave-update` cycle that reconciles the architecture to the new vision.

## 3. Architecture doc structure

The architecture doc has eight numbered sections, always in this order:

```markdown
# <Project> — Architecture

## 1. System overview
## 2. Modules and boundaries
## 3. Data and state
## 4. External dependencies
## 5. Deployment and operations
## 6. Quality guardrails
## 7. Open technical questions
## 8. Decision Log
```

The `architect` skill decides how much detail each section warrants. A simple project may need only stack, module boundaries, data ownership, dependencies, deployment shape, and testing strategy. A riskier project may need deeper interface, security, data model, or operational detail.

### 1. System overview

Two or three short paragraphs. What runs where, what the request lifecycle looks like end to end. A reader unfamiliar with the project should be able to learn the shape of the system from this section alone.

### 2. Modules and boundaries

A table or structured list of modules (responsibilities, not files). For each: name, responsibility (one sentence), W1 activation status, and the Decision Log entry IDs that govern it.

```markdown
| Module      | Responsibility                                  | W1            | Governed by |
|-------------|-------------------------------------------------|---------------|-------------|
| `auth`      | Magic-link issuance, session validation         | required      | ADR-002     |
| `clubs`     | Club state, membership, ownership transitions   | required      | ADR-005     |
| `notes`     | Lightweight meeting notes capture               | deferred (W3) | ADR-009     |
```

The `W1` column tells `wave-plan` which modules must be exercised by the W1 walking skeleton.

- `required` — must be touched by at least one W1 task. Default for any module that's part of the system's value-hypothesis-delivering vertical slice.
- `deferred (W<N>)` — the module's responsibility is real but the capability it provides is not part of W1's slice. The architect names the wave it's expected to come online in. `wave-plan`'s walking-skeleton check skips deferred modules.

Default to `required`. Use `deferred` only when the architect can name *why* a module isn't needed for W1's slice and *which* wave brings it online. If you can't name both, the module is `required`.

### 3. Data and state

Persistence shape: tables, collections, schemas, primary keys, ownership boundaries. Cite Decision Log IDs.

### 4. External dependencies

External services, APIs, libraries the system depends on. Each citation references the Decision Log entry that introduced or constrains it.

### 5. Deployment and operations

How the system runs in production: hosts, processes, environments, build artifacts. Even "single-binary CLI; no operational surface" is itself a section.

### 6. Quality guardrails

Testing strategy, performance budgets, security posture, accessibility. The cross-cutting properties the architecture commits to maintain.

When project-specific commands are not obvious from manifest files (`package.json` scripts, `Makefile` targets, `Cargo.toml`, etc.), include a lightweight **Project Commands** subsection so `wave-execute`'s Verification matrix has a single source of truth and doesn't rediscover commands per wave:

```markdown
**Project Commands**
- Install: `<command>`
- Run locally: `<command>`
- Test (unit): `<command>`
- Test (integration): `<command>` (or "n/a — none yet")
- Typecheck: `<command>` (or "n/a — dynamic language, no static check")
- Build: `<command>`
- Lint / format: `<command>`
```

Skip the subsection entirely when commands are derivable from a standard manifest the executor will read anyway (`npm test`, `cargo test`, `make test` — universal enough that documenting them is duplication). Add the subsection when commands are non-standard, multi-step, or wave-relevant in a way the executor would otherwise have to guess. Keep it command-only — the *strategy* (when to run integration vs unit, performance budgets, etc.) belongs in the prose above, not in the cheat-sheet.

### 7. Open technical questions

Things the architect hasn't yet decided. Mirrors the vision's Open Questions section but at the technical layer. Each is a candidate for a future Decision Log entry.

### 8. Decision Log

The append-only list of Decision Log entries (ADRs). Format defined in [Section 4](#4-decision-log-entry-format) below. Entries are ordered by ID (ADR-001, ADR-002, ...). Once added, an entry is never edited except to update its `Status` (e.g., from Proposed to Accepted, or from Accepted to Superseded with a pointer).

## 4. Decision Log entry format

Each entry is a structured block within Section 8 of the architecture doc:

```markdown
**ADR-007 — Voting data model: row-per-rank**
Status: Accepted (2026-06-12). Established by W2 wave-update.
Context: W2 audit revealed the flat per-member voting columns from the W1 sketch can't represent ranked voting without a schema migration. Depends on assumption A6 (ranked-choice preferred).
Decision: One row per (member, nomination), with an integer `rank` column. Position-1 ranks store rank=1; lower preferences store higher integers; unranked nominations store no row.
Consequences:
- Easier: supports both single-choice (rank=1 only) and ranked (rank 1..N) without schema change.
- Harder: query for "winners" now requires aggregation rather than direct read.
- Negative: storage cost grows linearly with member count per nomination.
Supersedes: ADR-004 (flat per-member columns).
Superseded by: <none yet>
```

ADR IDs are sequential (ADR-001, ADR-002, ...). They are never reused. A retired or superseded entry keeps its number forever.

`Consequences` must include at least one negative consequence. An entry without a downside hasn't been thought through.

## 5. Lifecycle and ratification

`Status` values:

- `Proposed (date). Drafted by <skill>.` — entry is drafted but not yet binding. Used in two situations: (a) `architect draft` produces seed entries that the human has not yet ratified, and (b) `wave-update`'s review subagent proposes a mid-cycle entry that wave-update has not yet ratified inside the same invocation.
- `Accepted (date). Established by <skill or wave>.` — current decision; modules and waves cite it.
- `Superseded (date) by ADR-N.` — a later entry replaces this one. The old entry's body is *never edited*; only its `Status` line is updated to point to the successor.

Ratification flow:

- **Seed entries from `architect draft`** start `Proposed`. Ratified by the human re-running `architect ratify` (which flips all Proposed seed entries to Accepted in one go), or by manually editing each `Status` field.
- **Mid-cycle entries from `wave-update`'s review** start `Proposed` within the same wave-update invocation. The human approves them as part of wave-update's interactive flow, after which wave-update flips them to Accepted before saving.

`wave-plan` and `wave-execute` refuse to run while any cited entry is `Proposed`. So ratification is the gate that unblocks downstream work.

## 6. Promoting to separate ADR files

**Default: do not promote.** For solo projects on the scale VADER targets, the embedded Decision Log section is sufficient indefinitely. Embedded entries live next to the architecture they govern, and a reader doesn't need to chase across files. The promotion path exists for projects that genuinely outgrow embedded entries — but most don't, and reaching for it prematurely adds file-management overhead without benefit.

Promote *only* when one of these conditions clearly fires (not "might fire" or "could fire"):

- The Decision Log section exceeds ~7 entries *and* you find yourself scrolling past entries when looking for one (the section is genuinely hard to navigate as one block).
- An entry needs to be superseded for the second time (history is now growing materially; a separate file gives the supersession chain room to breathe).
- Decision Log entries are being cited by callers outside the architecture doc (many wave-plan tasks reference an entry; the file becomes a navigation hub that benefits from being its own page).

If you're unsure whether a condition fires, do not promote. Wait until it's obvious. Promotion is reversible (entries can be re-embedded if they get small again), but the round-trip is friction.

When promoting:

1. Set frontmatter `adr_promoted_log: true`.
2. For each entry being promoted, create `<project-slug>-adr/ADR-NNN-<slug>.md` with the entry's full body. Add any deeper context the entry has accumulated.
3. Replace the entry in the architecture doc's Decision Log section with a one-line pointer: `**ADR-NNN** — <title>. *Status: <status>. See `adr/ADR-NNN-<slug>.md`.*`
4. Subsequent new entries can be created as separate files from the start (or continue as embedded entries — the choice is per-project).

Promotion preserves all IDs and references. Modules, waves, and tasks continue to cite `ADR-NNN`; the only change is where the body lives.

## 7. Invariants

1. **No material architecture body change without a Decision Log entry.** The current state of the system (sections 1-7) is justified by the entries in section 8. If a body section changes in a way that affects how the system is built — modules, interfaces, data ownership, dependencies, deployment shape, quality guardrails — a Decision Log entry explains why. Non-material edits (typos, wording clarifications, stale references, formatting, link fixes) bump `last_updated` but do not require a new entry. When unsure whether a change is material, treat it as material; an unnecessary entry is cheaper than a silent structural drift.
2. **Decision Log entries are append-only.** A new entry can be added; an existing entry's `Status` line can be updated retroactively (Proposed→Accepted, or Accepted→Superseded). Nothing else about an entry is ever edited.
3. **Decision Log IDs are never reused.** Retired or superseded entries keep their numbers forever.
4. **Every entry has at least one negative consequence.** A decision with no downsides has not been thought through.
5. **Every architectural change traces back to a wave or to the initial draft.** Mid-cycle entries are established by `wave-update`'s review of a specific wave; seed entries are established by `architect draft`. No "drive-by" entries.
6. **`architect` is the only skill that authors initial seed entries.** Mid-cycle entries are authored by `wave-update`'s review subagent and ratified by `wave-update`. No other skill writes to the architecture doc or Decision Log.
7. **Pivoted status mirrors the vision.** When the vision pivots in a way that affects architectural choices, the architecture doc is bumped to `pivoted` until the next `wave-update` cycle reconciles the Decision Log to the new vision.

## 8. Worked mini-example

A truncated example of an architecture doc with embedded Decision Log:

```markdown
---
architecture_version: 1
created: 2026-05-02
last_updated: 2026-05-02
status: active
adr_promoted_log: false
---

# bookclub — Architecture

## 1. System overview
A single-binary Go CLI invoked locally. Members interact via a small embedded
web UI on localhost. State persists to SQLite. No remote services other than
optional email for magic-link auth.

## 2. Modules and boundaries
| Module      | Responsibility                                  | W1            | Governed by |
|-------------|-------------------------------------------------|---------------|-------------|
| `auth`      | Magic-link issuance, session validation         | required      | ADR-002     |
| `clubs`     | Club state, membership                          | required      | ADR-005     |
| `polls`     | Nomination, voting, tally                       | deferred (W2) | (TBD W2)    |

## 3. Data and state
SQLite database at `~/.bookclub/bookclub.db`. Per ADR-001.

[... sections 4-7 ...]

## 8. Decision Log

**ADR-001 — Persistence: SQLite local file**
Status: Accepted (2026-05-02). Established by architect draft, ratified 2026-05-03.
Context: Solo/small-group scale. Vision §7 constraint: budget under $50/mo, no ops.
Decision: SQLite single file at `~/.bookclub/bookclub.db`.
Consequences:
- Easier: zero-ops, embedded in binary, fast for target scale.
- Negative: no concurrent multi-process access; manual backups required.

**ADR-002 — Magic-link auth, no passwords**
Status: Accepted (2026-05-02). Established by architect draft, ratified 2026-05-03.
Context: Members are invited by an organizer who already has their email. Password UX would dominate first-use experience.
Decision: Single-use, time-bounded magic-link via email. 30-day session cookie. No password recovery flow.
Consequences:
- Easier: one input field; no password storage; no recovery code.
- Negative: email deliverability becomes a hard dependency; account loss if email is lost.

**ADR-005 — Club state model: organizer-owned**
Status: Accepted (2026-05-02). Established by architect draft, ratified 2026-05-03.
Context: Vision §2 says Organizer is responsible for club state. Members participate but don't own.
Decision: Club row has a single `owner_id` (organizer). Membership is a separate join table. Ownership transferable via explicit handoff.
Consequences:
- Easier: clear authority boundary; simple permission checks.
- Negative: bus factor of 1 per club; handoff UX must exist eventually.
```

A subsequent wave-update cycle that adds `ADR-007` (row-per-rank voting, superseding the W2-sketched ADR-004) would append the new entry and update ADR-004's `Status:` line to `Superseded (2026-06-12) by ADR-007.` The body of ADR-004 stays untouched.

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
