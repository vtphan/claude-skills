# Story Generator: Example Interaction

This file shows a Story Generator pass on the homework system, using the Goal (first-pilot-infrastructure) and the Journey (completing a homework assignment) from previous examples. It exists to calibrate the skill — what good story decomposition looks like, how aggressive pruning should be, what well-formed requirements look like.

## Input

Accepted Seed, Context, Goal (first-pilot-infrastructure scoped to one assignment, ten items in out-of-scope), and one Journey (completing a homework assignment, with seven stages and five key insights).

## Output (abbreviated)

### Part 1: Story set summary

Generated 28 candidate stories from journey moments and key insights. Pruned to 11 stories that fit the Goal's scope. Priority distribution: 7 `must`, 3 `should`, 1 `could`. Journey coverage: every stage of the journey except `stage-stuck` is addressed by at least one Story; `stage-stuck` is intentionally not directly addressed (the Goal explicitly cuts pedagogical scaffolding), but the event capture stories will record stuck behavior for future iterations.

One tension worth flagging: the autosave Story (`must`) and the event-pipeline Story (`must`) compete for the same client-side resources. Requirements have been written to be compatible, but real implementation may require trade-offs that surface during build.

### Part 2: Pruned candidates

```markdown
## Pruned candidates

Out of scope for this Goal:
- **story-stuck-detection-algorithm** — Goal cuts predictive analytics.
- **story-instructor-dashboard** — Goal cuts the dashboard.
- **story-hint-system** — Goal cuts pedagogical scaffolding.
- **story-self-explanation-prompts** — Goal cuts pedagogical scaffolding.
- **story-ta-queue** — Goal cuts human help routing.
- **story-experiment-runner** — Goal cuts experimental infrastructure.
- **story-mobile-editor** — Goal cuts mobile clients.
- **story-content-authoring-ui** — Goal cuts content authoring.
- **story-multi-section-support** — Goal cuts multi-section.
- **story-gradebook-integration** — Goal cuts gradebook integration.
- **story-cohort-comparison-view** — Goal cuts dashboard and stuck-score.

Folded into other stories:
- **story-network-resilience-on-save** — Folded into `story-autosave-progress` as a requirement.
- **story-test-result-display** — Folded into `story-run-tests`.
- **story-event-batching** — Folded into `story-event-pipeline`.

Not grounded in current Journey or Seed:
- **story-classmate-help-button** — Not in Journey; would require Seed update for peer interaction.
- **story-progress-indicator-on-assignment-list** — Aspirational; not addressed by Journey or Goal.

Too small to be a Story:
- **story-confirm-submission-dialog** — Folded into `story-submit-assignment` as acceptance criterion.

Duplicate:
- **story-resume-editing-on-reopen** — Subsumed by `story-autosave-progress`.
```

### Part 3: Story documents (showing two representative ones)

#### Story 1: Autosave progress

```markdown
---
id: story-autosave-progress
title: Autosave student work to prevent loss
seed_ref: seed
context_ref: context
goal_ref: goal-first-pilot
journey_moment_refs:
  - journey-completing-assignment#stage-iterating
  - journey-completing-assignment#stage-abandons-and-switches
  - journey-completing-assignment#stage-returning-with-fresh-eyes
priority: must
status: draft
---

# Story: Autosave student work to prevent loss

## Story

**As a** student,
**I want** my work to be saved automatically without my having to think about it,
**so that** I don't lose progress when I switch problems, close my laptop, or experience a network drop.

## Journey moments served

- [journey-completing-assignment#stage-iterating] — Students iterate quickly with multiple edits and runs; loss of work mid-iteration is high-cost.
- [journey-completing-assignment#stage-abandons-and-switches] — The productive-switching pattern depends on safe abandonment; lost state collapses this pattern.
- [journey-completing-assignment#stage-returning-with-fresh-eyes] — Returning depends on accurate restoration of prior state, including in-progress edits.

## Acceptance criteria

- After typing in the editor, a student can close the browser, reopen it within 24 hours on the same device or another, and see their most recent edits intact.
- A student switching between problems within an assignment can return to a prior problem and see its state as they left it, including unfinished code.
- A student experiencing a network drop while editing does not lose work; their edits resume saving when connectivity returns.
- A student is never shown stale work after a successful save (within reasonable time bounds).

## Requirements

### req-autosave-cadence: Save cadence

- **Type:** non-functional
- **Specification:** Editor edits are persisted to the server within 5 seconds of the most recent edit when changes are present. On tab blur, page close, or visibility change to hidden, an immediate save is triggered.
- **Verification:** Automated test simulating typing patterns and measuring server-side write timestamps.

### req-autosave-latency: Save latency under load

- **Type:** non-functional
- **Specification:** Save round-trip latency (edit confirmed by server) is no more than 500ms at p95 under expected pilot load (up to 15 concurrent students).
- **Verification:** Load test against pilot infrastructure with synthetic traffic at expected concurrency.

### req-network-resilience: Network failure handling

- **Type:** edge-case
- **Specification:** On save failure, retry with exponential backoff (initial 1s, max 30s, max 5 attempts within a 2-minute window). After all retries fail, queue edits client-side and surface a non-modal indicator that work is unsaved. Resume saving when connectivity is detected.
- **Verification:** Manual test with simulated network disconnect during editing; confirm queued edits survive and re-save on reconnection.

### req-restore-on-reopen: State restoration

- **Type:** functional
- **Specification:** On reopening the editor for a problem, the most recent saved state is restored within 500ms of authentication. Restoration is per-problem; switching between problems restores the corresponding problem's state.
- **Verification:** Automated test: write code, close, reopen, assert content matches.

### req-version-history: Edit history retention

- **Type:** data
- **Specification:** A minimum of one edit snapshot per minute of active editing is retained for the duration of the course plus one year. Snapshots are queryable for research and recovery purposes.
- **Verification:** Inspection of stored snapshots after a sample editing session.

### req-conflict-resolution: Multi-tab conflict

- **Type:** edge-case
- **Specification:** If a student opens the same problem in two tabs simultaneously, the most recent save wins (last-write-wins) and a visible warning indicates that edits from another tab were superseded.
- **Verification:** Manual test with two tabs; confirm warning appears and content is not silently lost.

## Notes

The autosave Story is load-bearing for the Goal's "no greater than 0.5% data loss" done condition and for the Journey's productive-switching pattern. Trade-offs with the event pipeline (which also writes to the server frequently) need to be managed at implementation time; both are `must`.

## Change log

- 2026-04-27: Initial draft.
```

#### Story 2: Behavioral event capture

```markdown
---
id: story-event-pipeline
title: Capture and persist behavioral events
seed_ref: seed
context_ref: context
goal_ref: goal-first-pilot
journey_moment_refs:
  - journey-completing-assignment#stage-orienting
  - journey-completing-assignment#stage-first-attempt
  - journey-completing-assignment#stage-iterating
  - journey-completing-assignment#stage-stuck
  - journey-completing-assignment#stage-abandons-and-switches
  - journey-completing-assignment#stage-returning-with-fresh-eyes
  - journey-completing-assignment#stage-completing-and-submitting
priority: must
status: draft
---

# Story: Capture and persist behavioral events

## Story

**As a** instructor (and downstream researcher),
**I want** the system to capture a complete record of student behavior during homework sessions,
**so that** I can identify struggling students and analyze how learning happens.

## Journey moments served

This Story serves all stages of the journey, because event capture is continuous throughout the homework session, not tied to specific moments. Particularly important for the `stage-stuck` stage, which is otherwise invisible.

## Acceptance criteria

- After a complete student session, an event log exists that records: assignment open/close, problem switches, code edits (as typing bursts), code runs (with results), focus changes, and idle periods over 30 seconds.
- The event log is queryable by the instructor during the assignment window using a manual query interface.
- The event log is exportable to a deidentified dataset usable by the research collaborator without preprocessing.
- Event log capture does not noticeably degrade the student-facing editor experience.

## Requirements

### req-event-types: Event type coverage

- **Type:** functional
- **Specification:** Events captured include, at minimum: `session_open`, `session_close`, `problem_view`, `code_edit_burst` (start time, end time, characters added, characters deleted, final cursor position), `code_run` (timestamp, code hash, test cases attempted, pass/fail per case, runtime, error messages), `focus_change` (visible/hidden), `idle` (start time, duration). Each event includes student pseudonymous ID, assignment ID, problem ID, and timestamp.
- **Verification:** Inspection of event log after a sample session, confirming each event type appears as expected.

### req-event-loss: Event loss rate

- **Type:** non-functional
- **Specification:** Across a complete assignment cycle, no more than 0.5% of client-side emitted events are missing from the server-side store, measured by reconciling client-side sequence numbers with server-side records.
- **Verification:** Reconciliation script run after the pilot assignment cycle.

### req-event-batching: Client-side batching

- **Type:** non-functional
- **Specification:** Events are batched client-side and posted to the server every 10 seconds or when the batch exceeds 50 KB, whichever is first. On tab close, an immediate flush is attempted via sendBeacon.
- **Verification:** Network inspection during a sample session.

### req-event-schema-versioning: Schema version

- **Type:** data
- **Specification:** Each event record includes a `schema_version` field. Schema changes are versioned semantically. Historical events remain queryable after schema changes; migration or annotation strategies are documented for any field changes.
- **Verification:** Inspection of stored events; documentation review.

### req-event-storage: Storage and retention

- **Type:** data
- **Specification:** Events are stored in an append-only event store partitioned by course and date. Retention is course duration plus three years for FERPA compliance; longer retention requires IRB-covered research basis.
- **Verification:** Inspection of storage configuration and retention policies.

### req-pseudonymous-ids: Identity separation

- **Type:** data
- **Specification:** Each event references the student via pseudonymous ID. The mapping from pseudonymous ID to identifying information is stored separately, accessible only by the instructor and only for operational purposes (e.g., identifying a struggling student for intervention). Research exports use only pseudonymous IDs.
- **Verification:** Inspection of data model; manual verification that exports do not include identifying fields.

### req-query-latency: Query latency for instructor view

- **Type:** non-functional
- **Specification:** Events emitted are queryable by the instructor within 5 minutes of capture. Query response time for typical instructor queries (per-student status during assignment) is no more than 5 seconds at p95.
- **Verification:** Latency measurement during pilot assignment cycle.

## Notes

This Story is the central infrastructure of the project — the data layer everything else depends on. Schema decisions made here will be very expensive to retrofit, so requirements are deliberately specific even at MVP scale. Several requirements (especially schema versioning and pseudonymous IDs) feel heavy for a single-section pilot but are load-bearing for the research bet.

## Change log

- 2026-04-27: Initial draft.
```

### Decision points

```markdown
## Decision points

1. I generated 28 candidates and pruned to 11. The cuts are listed; argue with any of them — particularly "story-classmate-help-button" since peer interaction may matter more than the Seed currently captures.
2. The autosave latency target is 500ms at p95. This is reasonable for institutional infrastructure but may be tight for some deployments. Adjust?
3. The event loss rate target is 0.5%. This is the threshold the Goal cites for the "0.5% data loss" done condition. Confirm this is what you intend (sometimes "0.5% data loss" can be interpreted differently).
4. I wrote `story-event-pipeline` as serving all journey stages because event capture is continuous. Some teams prefer to write separate Stories per event type — happy to split if you'd prefer that granularity.
5. The `req-event-schema-versioning` requirement feels heavy for a single-section pilot. It's load-bearing for the research bet (you cannot retrofit schema versioning), but if you'd rather defer it, I'd flag this as a major risk for downstream research utility.
```

---

## What this example illustrates

A few things to notice:

**Pruning is the most important work.** The candidate set was 28; the surviving set is 11. The cuts list is prominently shown so the user can object to any.

**Out-of-scope cuts dominate the pruning.** Most cuts trace back to explicit Goal scope decisions — the dashboard, hints, stuck-score, etc. This is what makes the Goal earn its keep at this stage.

**Requirements are quantified.** "500ms at p95," "0.5% loss rate," "5-second cadence," "5 seconds at p95 query latency." Each requirement is testable.

**Verification methods are concrete.** Each requirement has a verification method that's actually verifiable — not "tested" but "automated test simulating typing patterns" or "reconciliation script run after the pilot."

**Acceptance criteria are user-facing, requirements are technical.** The autosave Story's acceptance criteria describe what the student experiences; the requirements describe what the system does. Both layers are present.

**Cross-Story tensions are surfaced.** The autosave-vs-event-pipeline tension is flagged in the summary so the user knows to expect implementation-time tradeoffs.

**Notes carry rationale.** The event-pipeline Story's note explains why heavyweight requirements (schema versioning, pseudonymous IDs) appear at MVP scale. This rationale will be useful to a future reader (or a future iteration of the same skill) trying to understand why those requirements are there.

## Counter-example: under-pruned set

> A Story set with 35 stories, including three different versions of "instructor dashboard," one for "self-explanation prompts," one for "TA queue prioritization," and one for "mobile editor."

Why this is wrong: most of these are out of Goal scope. The skill's job is to enforce the Goal's boundaries, not to surface every possible Story. An under-pruned set delegates the cutting work to the user, which is exactly what the skill should be doing.

## Counter-example: vague requirements

> ### req-autosave: Autosave should work
>
> - **Type:** functional
> - **Specification:** The system saves the student's work automatically.
> - **Verification:** Manual test that work is saved.

Why this is wrong: not quantified, not testable, not specific. "Work is saved" doesn't say when, how often, with what latency, with what failure handling. A requirement at this level of vagueness is a wish, not a requirement.

The fix: every requirement has numbers and thresholds where applicable, and a verification method that someone could actually execute.
