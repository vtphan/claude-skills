# Goal Drafter: Example Interaction

This file shows a Goal Drafter pass on the homework system, continuing from the Context Builder example. It exists to calibrate the skill — what good Goal scoping looks like, where the discipline matters, how to make cuts visible.

## Input: an accepted Context

The Context document produced by Context Builder, accepted by the user. (Summarized for brevity; in practice the skill reads the full file.)

Key elements:

- **Vision:** Homework environment for college-level algorithms courses where the act of doing the work generates evidence that improves the work.
- **Strategy:** Infrastructure first; single-course pilot as learning instrument; pedagogical and research utility weighted equally; instructor-led adoption.
- **Outcomes:** No-data-loss for students; instructor identifies struggling students earlier; 2-4 research papers in 3 years; system informs its own evolution; sustained operation by single maintainer.
- **Personas:** Maya (student), Devon (instructor), Priya (TA), Ana (learning scientist).

User input alongside the Context: "I want the first goal to be a real pilot in my algorithms course this semester. Keep it small."

## Output

### Part 1: The Goal document

```markdown
---
id: goal-first-pilot
title: First-pilot infrastructure for algorithms course
seed_ref: seed
context_ref: context
status: draft
time_horizon: 6-10 weeks
---

# Goal: First-pilot infrastructure for algorithms course

## Decision points

1. I cut TA queue, experiments, hint systems, and the instructor dashboard from this iteration. The dashboard especially is tempting — confirm it stays out, or is a minimal version worth including?
2. The done condition "8-15 students complete one assignment" assumes you'll deploy to your section this semester. If the deployment timing is uncertain, this needs to change.
3. I propose 6-10 weeks as time horizon. If your semester start dictates a shorter window, the scope needs to shrink further (probably by deferring the export pipeline).
4. The Goal serves three of the four strategic bets directly. "Research utility weighted equally with pedagogical utility" is served only by the export pipeline; full research-grade infrastructure is deferred. Confirm.
5. I included "Devon can identify at least one student who would benefit from intervention" as a done condition without a dashboard — meaning you'd identify them by querying logs directly. Reasonable for the pilot, or do you want a minimal dashboard included?

## Statement

Build the minimum end-to-end system that supports students completing one recursion-focused assignment in the algorithms course, with full behavioral logging, exportable data, and the instructor able to identify at least one struggling student during the assignment window.

## In scope

- Student authentication (institutional SSO if available, simple credentials otherwise).
- Problem viewer for one assignment's worth of recursion problems.
- Code editor with autosave (5-second cadence, robust to network drops).
- Test-case execution with pass/fail feedback per case.
- Full behavioral event logging: keystrokes (aggregated into typing bursts), code runs with results, focus changes, idle periods over 30 seconds.
- Append-only event store with versioned schema.
- Manual instructor query interface (SQL or notebook) for inspecting student progress during the assignment window.
- Deidentified data export pipeline producing a clean dataset for collaborator analysis.
- Deployment on existing institutional infrastructure with single-instructor monitoring.

## Out of scope

- Instructor dashboard with real-time visualizations.
- Stuck-score algorithm or any predictive analytics.
- Hint system, self-explanation prompts, or any pedagogical scaffolding.
- TA queue or human help routing.
- Experimental infrastructure for randomized conditions.
- Multi-assignment or multi-section support.
- Mobile clients.
- Researcher-facing tooling beyond raw export.
- Gradebook integration or LMS connectors.
- Content authoring UI (problems are authored as files for now).

## Definition of done

- 8 to 15 students in the algorithms course complete at least one recursion-focused assignment using the system.
- Behavioral events are captured with no greater than 0.5% data loss across the cohort, measured by reconciling client-side event sequences against server-side records.
- Devon can identify at least one student during the assignment window who would benefit from intervention, by inspecting event logs directly.
- A deidentified export of the cohort's events is produced and validated as queryable by Ana (or another collaborator) without requiring custom preprocessing.
- The system runs the assignment cycle without unrecoverable failures requiring instructor intervention beyond initial setup.

## Time horizon

6-10 weeks of focused development, plus the assignment cycle itself.

## Linked context

- **Vision served:** "the act of doing the work generates evidence" — the iteration produces the first real evidence-generation cycle.
- **Strategy bets served:**
  - "Infrastructure first, not features" — directly enacted; this iteration is almost entirely infrastructure.
  - "Single course pilot as learning instrument" — directly enacted; the pilot is the iteration.
  - "Instructor-led adoption" — directly enacted; students use the system because the course requires it.
  - "Research utility and pedagogical utility weighted equally" — partially served; the export pipeline supports research utility, but no specific pedagogical features are built.
- **Success outcomes contributed to:**
  - "No-data-loss for students" — the autosave and event capture targets this.
  - "Instructor identifies struggling students earlier" — partial; the iteration tests whether log inspection alone is sufficient.
  - "Sustained operation by single maintainer" — the iteration tests this directly.
- **Primary personas:** Maya (student) and Devon (instructor). Priya and Ana are secondary; the iteration produces data Ana can use but doesn't build researcher-facing tooling, and Priya's role is not addressed.

## Success signals

- Students complete assignments without reporting work loss or interface confusion.
- Event logs are clean enough that ad-hoc queries return sensible results without preprocessing.
- Devon spends less than four hours per week on system maintenance during the assignment cycle.
- Ana finds the exported data useful enough to want a second iteration.

## Open questions

- Is autosave at 5-second cadence sufficient for student trust, or does perceived autosave reliability require shorter cadence or visible indicators?
- Does inspection of raw event logs scale even at section size (8-15 students), or is even the minimal instructor view a usability problem?
- Is the event schema correct for downstream research, or does the first export cycle reveal gaps?
- Does the load on existing institutional infrastructure stay within tolerable bounds for the cohort size?

## Change log

- 2026-04-27: Initial draft from accepted Context. Cuts the dashboard, stuck-score, hints, TA queue, and experiments to keep scope honest.
```

### Part 2: Summary

- Cut hard. The out-of-scope list has ten items, several of which would be tempting to include. The dashboard cut is the most consequential — instructors will want one — but a manual query interface is sufficient to test the load-bearing assumption that log inspection can identify struggling students.
- Done conditions are observable and trailing. "8-15 students complete at least one assignment" is a yes/no condition at the end. "0.5% data loss" is a measurable threshold. "Devon can identify one student" is a check the instructor performs.
- Time horizon is 6-10 weeks. Honest range, not a deadline. If the semester start forces a shorter window, the export pipeline is the most natural cut.
- The Goal serves three strategic bets directly and one partially. The "research utility" bet is partially served by the export pipeline but not by researcher-facing tooling. This is a deliberate compromise for iteration one; flagged in decision points.
- Two things I held back from including: a minimal dashboard (would be useful but breaks the infrastructure-first discipline), and a stuck-score algorithm (premature without baseline data). Both surface in decision points so the user can override.

---

## What this example illustrates

A few things to notice:

**The out-of-scope list is the most important section.** Ten items, each of which is a reasonable "while we're at it" addition. Naming them explicitly is what protects the iteration from creeping into a six-month version-one trying to ship everything.

**Done conditions are observable.** Each one can be answered yes or no after the iteration. None requires interpretation or judgment about whether something is "good enough."

**The Goal serves the Context, not the project as a whole.** It doesn't claim to advance every strategic bet equally. The "research utility weighted equally" bet is partially served by the export pipeline; full research-grade infrastructure is explicitly deferred. This honesty is what makes the Goal accountable.

**Time horizon is a range, not a date.** 6-10 weeks acknowledges uncertainty. A specific date would be false precision.

**Open questions are about what the iteration will teach.** Each question, when answered by completing the Goal, advances the project's understanding. They're different from Seed-level open questions (which are about strategy) — these are about iteration-level learning.

**Decision points front the most consequential cuts.** The dashboard cut and the time horizon are the two most likely points of disagreement. They're surfaced explicitly so the user can react.

## Counter-example: scoping too large

For contrast, here's what an over-scoped Goal might look like — and why it's wrong:

> **Statement:** Build a complete first version of the homework system with editor, dashboard, stuck detection, hints, and exportable data.
>
> **In scope:** [twelve items including all of the above plus admin tooling and content authoring]
>
> **Out of scope:** [two items: mobile and gradebook]
>
> **Definition of done:** "The system is usable by students and instructors and produces research-quality data."

Why this is wrong:

- The scope is the whole project, not an iteration.
- Done conditions are vague ("usable," "research-quality") and not observable.
- The out-of-scope list does no work — the items are obvious non-features.
- The time horizon would be six months minimum, which isn't an iteration; it's a release.

When you see a Goal like this, the right move is to send it back for tighter scoping, not to accept it.

## Counter-example: scoping too small

> **Statement:** Set up the deployment pipeline.
>
> **In scope:** Configure server, set up CI, set up monitoring.
>
> **Out of scope:** Everything else.
>
> **Definition of done:** "Deployment pipeline works."

Why this is wrong:

- No user-facing surface; nothing observable to a student or instructor.
- Doesn't test any strategic bet.
- Completing it teaches nothing about the project.
- Could be a task within a larger Goal, but isn't a Goal on its own.

A Goal should be small enough to ship and large enough to teach. This one is small enough but not large enough.
