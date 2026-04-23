---
name: phase-plan-draft
description: Use this skill whenever the user has a requirements document (stories, journeys, features — typically the output of requirements-expander, possibly hand-edited) and wants an initial rolling-wave implementation plan drafted from it. Triggers include phrases like "draft an implementation plan from these requirements", "create a rolling-wave plan for this spec", "break this down into phases", "plan how to build this", "what's the first phase for this project", or whenever a requirements markdown file is provided and the next step is deciding how to build it. Also trigger when the user shares a PRD, product brief, or feature list and asks for a phased build plan, MVP sequencing, or a roadmap. Do NOT use when the user wants a project timeline with dates and owners (that's Gantt/PM tooling), when the user wants code written directly without intermediate planning, or when a plan already exists and the user wants to update it (use phase-plan-update for that).
---

# Phase Plan Draft

Produce the first version of a rolling-wave implementation plan from a reviewed requirements document. The plan is a single markdown file that follows the schema in `references/plan-schema.md` — read that file fully before doing any planning work. This SKILL.md covers the judgment calls that shape *good* plans; the schema file covers *format*.

## Inputs and output

**Input:** a requirements document — typically the output of `requirements-expander`, often hand-edited by the user. Don't assume the document matches the expander's template exactly. Read it for the facts it carries (goal, scope, roles, stories, journeys, features, open questions), not for a specific layout.

**Output:** a single file named `<project-slug>-plan.md`, written alongside the requirements doc unless the user specifies a different name or location. Confirm the file path before writing.

## Workflow

### 1. Read the requirements document thoroughly

Extract the following, even if the document structures them differently than you expect:

- **Goal and non-goals** — what the system is, and what it explicitly is not.
- **User stories and features with their IDs** — you'll reference these by ID throughout the plan.
- **User journeys** — critical paths through the system; these strongly inform phase ordering.
- **Open questions** — these become the initial seeds of the plan's assumptions register. Pay particular attention; these are the doc's honest statement of what it doesn't yet know.
- **Success metrics** if present — these shape what "done enough to ship" means.
- **Constraints** — tech stack, platform, timeline, user environment.

If any of these are genuinely missing — not just differently named — and a plan can't be drafted without them, stop and ask the user one focused question. Don't interrogate them.

### 2. Decide on phases (the hard part)

This is where most of the skill's value lives. Good plans and bad plans diverge at phase selection, not at formatting. Follow the principles in [Phase selection principles](#phase-selection-principles) below. Aim for 3-6 phases. Fewer than 3 is probably too coarse; more than 6 suggests you're over-planning work that rolling-wave is designed to defer.

### 3. Fully plan the current phase (P1)

Expand P1 into tasks with acceptance criteria. Every task must have acceptance. Tasks should be sized so a developer agent can complete each in one sitting — if a task stretches beyond that, split it. See [Task sizing and acceptance](#task-sizing-and-acceptance) below.

### 4. Sketch future phases

Future phases get the phase skeleton (goal, covers, entry/exit criteria, assumptions, risks, 2-4 sentence sketch). **No task breakdowns.** If you find yourself drafting tasks for P3, stop — that's future work whose shape you don't yet know, and pre-planning it defeats the point of rolling-wave.

### 5. Seed the assumptions and risks registers

Walk the requirements doc's Open Questions and lift each one into either the assumptions register (things we're assuming in order to proceed) or the risks register (things that could go wrong and how we'd mitigate). Some open questions become both. Assign each one to the phase where it first matters.

### 6. Fill in traceability and change log

Write the requirements-coverage table. Every story and feature from the requirements doc must appear either assigned to a phase or in the Deferred row with a one-line reason. Add the initial-draft entry to the change log.

### 7. Write the file and verify

Write the plan file. Then do a final read-through checking the invariants in `references/plan-schema.md` section 9 — especially: no task detail in future phases, every task has acceptance, every requirement is accounted for.

## Phase selection principles

Phase boundaries are the most consequential decisions in the plan. Get them right and the plan runs itself; get them wrong and every update pass will be fighting the structure. Four principles, in priority order when they conflict.

### Principle 1: Vertical slices beat horizontal layers

A good P1 is a **thin end-to-end slice** that exercises the whole stack shallowly — one story, implemented from data layer up to whatever interface the user actually uses — rather than a foundational horizontal layer ("all the data models first", "all the auth infrastructure first").

Vertical slicing wins because:

- **Integration risk surfaces early.** The dangerous bugs in a system are almost never in individual layers — they're in the handoffs between them. A vertical slice forces those handoffs to happen in P1, when the plan is still flexible. A horizontal approach hides them until late phases, when the plan is too committed to absorb the cost of fixing them.
- **Each phase delivers observable outcome.** A user (or stakeholder) can see progress after each phase, because each phase ends with the system being able to do something new end-to-end. Horizontal phases end with the system still not being able to do anything users care about.
- **Rolling-wave replanning has real information to work with.** When P1 ends, you've seen the whole stack work once. Future-phase sketches can be refined based on that reality. Horizontal phases end with only partial knowledge, and replanning is still partly speculative.

The exception: if a required technical foundation is genuinely hard and genuinely shared across everything (e.g., "this whole system only works if we have a custom search engine that doesn't exist yet"), that foundation can be P1. But default hard to vertical slicing — the bar for a horizontal P1 should be high, and the plan should explain in the Goal section why the default was overridden.

### Principle 2: Risk-first ordering

Among candidate phases, order them so the scariest unknowns are tackled earliest. Scariness is a function of:

- **Technical uncertainty** — "we don't know if the tagging engine will be accurate enough" is scarier than "we need a settings page."
- **Requirements uncertainty** — "we don't know if users will actually accept magic-link auth" is scarier than "we know we need CRUD on clubs."
- **Dependency weight** — things many future phases depend on are scarier than leaf features.

The reason: rolling-wave's whole purpose is to learn between phases. Learning is maximized when you front-load the things you're least sure about. If P1 tackles something safe, P1 was wasted relative to what the rolling-wave discipline could have given you.

### Principle 3: Value-first as tiebreaker

When two candidate first phases have similar risk profiles, pick the one that delivers more user value. This keeps stakeholders' confidence up and ensures that if the project stops after any phase, the built system is still useful.

### Principle 4: Size for learning, not for tidiness

Each phase should be **small enough that you can plan it comprehensively without guessing**, and **large enough to produce something observable** (deployable, demo-able, or testable end-to-end). If you're tempted to add a fifth small phase because things look uneven, resist — uneven phase sizes are fine. Awkward-sized phases usually mean you're optimizing for the wrong thing (making the plan look clean) instead of for the thing that matters (learning fast).

A phase sized for one developer-agent to complete in somewhere between a half-day session and a week of sessions is usually about right. If you're aiming for several weeks of work in one phase, the phase is too big.

## Task sizing and acceptance

Within the current phase (P1), break the work down into tasks with these properties.

**Size**: each task should be completable by a developer agent in roughly one session — a few hours of focused work. If a task description starts mentioning "and then" or "followed by", split it.

**Acceptance**: every task has at least one testable acceptance criterion. Good acceptance criteria are specific:

Bad: "The scan command works."
Good: "`filetagger scan <dir>` exits 0 on a directory of mixed files, writes at least one row per file to `~/.filetagger/index.db`, and produces stderr only on actual errors."

Acceptance criteria answer "how will we know this is done?" — not "what does this task do?" If they read like a duplicate of the task description, they aren't useful.

**Citation**: each task advances at least one story or feature, OR it's implicit plumbing (e.g., "T1.1 — Project scaffolding"). In the latter case, say so explicitly — don't let silent scope drift sneak in as plumbing.

**Order**: tasks within a phase should be orderable (T1.1 before T1.2 in general), though the schema allows parallel work. Put the task that most reduces uncertainty first — that's usually the one that proves the end-to-end integration works.

## Filling each section of the plan

See `references/plan-schema.md` for the format. A few per-section notes that the schema doesn't say explicitly:

**Goal and guardrails**: rewrite the goal in your own words — don't just quote the requirements doc. The plan is a fresh document and the goal should read as if it was written for this document, not cut-and-pasted.

**Requirements coverage**: when a story spans multiple phases (e.g., "basic in P1, polish in P2"), say so in the Notes column. This prevents confusion later when the same story ID appears in multiple phases.

**Phases overview**: keep the one-line goal sharp. If you can't describe the phase's goal in ten words, the phase is probably fuzzy. Sharpen the phase, not the description.

**Assumptions register**: read the requirements doc's Open Questions carefully. Every open question is a candidate. Distinguish **assumptions** (things we're choosing to assume in order to proceed — e.g., "we're assuming single-choice voting until we validate") from **risks** (things that could go wrong even if our assumptions hold — e.g., "email delivery might be delayed"). Assumptions close out via validation; risks close out via occurrence or mitigation.

**Risks register**: only include risks where you can say something useful about mitigation. A risk with no mitigation path is either trivially true ("the database could fail") or really an assumption in disguise. Don't pad.

## When the requirements doc is imperfect

The requirements doc has probably been human-edited. It may have renamed sections, inconsistent IDs after a restructuring, or partial trimming. The skill should tolerate this and work from the substance, not the layout.

Specifically:

- If IDs are inconsistent (some US-OWN-*, some US-O-*, some just US-1), use whatever the current doc uses and don't try to "fix" it — the plan should reference things by the IDs the user will actually see in their doc.
- If a section seems missing (e.g., no Journeys section), check whether its content has been folded into another section. Don't assume it's truly absent until you've looked.
- If the doc has added new sections that aren't in the expander's template (e.g., "Prior art", "Design constraints"), read them — they often contain the juiciest input for phase selection.

If after an honest read the doc is genuinely missing something critical, ask one focused question rather than guessing.

## Invariants — things to never do

From the schema, but worth repeating because these are the most common failure modes:

1. **No task-level detail in future phases.** Even if a P3 task is "obvious," don't write it down. You don't yet know what you'll learn in P1 and P2.
2. **Every task has acceptance criteria.** No exceptions. A task without acceptance is a task that can't be honestly closed out.
3. **Don't silently drop requirements.** If a story or feature from the requirements doc isn't in any phase, it goes in the Deferred row with a reason. Silent omissions will cause pain two update passes from now.
4. **Don't over-plan.** The comfort of a detailed plan is seductive. Resist. If you're filling in risks for a phase that you sketched in two sentences, you're probably overreaching.

## Handoff to the next skill

The plan's current phase is now ready for execution. The next step in the user's workflow is `phase-plan-execute`, which reads this plan and implements the current phase. When writing the plan, imagine an executor agent opening this file and trying to start work — would they know exactly what to do? If yes, you're done. If no, the P1 section needs more concreteness (usually in acceptance criteria, not in more text).

## Worked example

Given a requirements doc for `filetagger` (a CLI that tags files by content), a reasonable first-draft plan would have:

- **P1 — Scan and tag.** Vertical slice: point it at a directory, see tags land in an index. Proves end-to-end feasibility of the tagger pipeline, which is the single biggest risk. Fully planned, ~4 tasks.
- **P2 — Query by tag.** Sketched. Entry criterion: P1 index format stable.
- **P3 — Incremental re-scan.** Sketched, with an assumption about mtime reliability (A5) that will be tested when P3 becomes current.
- **Deferred:** watch mode, GUI, multi-machine sync.

Note what this plan *doesn't* do: no "P1 — Scaffolding and setup" (rolled into P1 as plumbing tasks), no "P0 — Architecture decisions" (those belong in the requirements doc or get decided inline during P1), no breakdown of P2 tasks even though they might look straightforward.

A full example of this plan is shown in `references/plan-schema.md` Section 10.
