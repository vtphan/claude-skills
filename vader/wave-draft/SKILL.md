---
name: wave-draft
description: Use this skill when a vision doc and architecture doc (plus seed ADRs) exist, and the user wants the initial wave doc drafted. Triggers include phrases like "draft the wave doc from the vision and architecture", "produce the initial wave plan for this project", "what's W1 for this project", "break this into waves with W1 as a walking skeleton", or whenever the upstream vision and architecture artifacts are ready and the next step is committing them into a rolling-wave plan. Also trigger when the user shares a vision and architecture and asks for an MVP plan or first-wave breakdown. Do NOT use when no architecture doc exists yet (run architect-draft first). Do NOT use to revise an existing wave doc — that's wave-redraft. Do NOT use to write code; this skill produces a planning document only.
---

# Wave Draft

Produce the first version of the unified wave doc from a vision doc and an architecture doc. The wave doc unifies requirements (stories, journeys, features) and plan (waves, tasks) into a single rolling document. W1 defaults to a **walking skeleton** — a thin vertical slice that exercises every module in the architecture with minimal functional content.

Before doing anything else, read `references/wave-schema.md` and `references/architecture-schema.md` in full. The wave schema is the contract this skill operates inside. The architecture schema tells you how to read the inputs.

## Inputs and output

**Inputs:**
- The vision doc (`<project-slug>-vision.md`). Source of goal, non-goals, roles, in-scope capabilities, success metrics, and open questions.
- The architecture doc (`<project-slug>-architecture.md`). Source of modules, ADRs, key interfaces, and structural constraints.
- The ADR log (`<project-slug>-adr/`). The ADRs the wave doc will reference by ID.

**Output:** `<project-slug>-wave-doc.md` written to `docs/`. Frontmatter has `wave_doc_version: 1`, `current_wave: W1`, `status: in_progress`, with paths to the source vision, architecture, and ADR log.

## Workflow

### 1. Read the vision and architecture thoroughly

Extract:
- **From the vision:** goal, non-goals, roles, in-scope capabilities, success metrics, open questions. (If the vision has Section 10 "Core journeys", read it too — those flows shape which W1 walking-skeleton path most reduces uncertainty.)
- **From the architecture:** the module list (Section 2), key interfaces (Section 3), and the seed ADRs.

If either input is missing or inconsistent — e.g., the architecture doesn't have a module needed to support an in-scope capability from the vision — stop and ask the user. Do not invent.

### 1a. Refuse to run if ADRs are not yet ratified

Walk the ADR directory. If any ADR has `Status: Proposed`, stop. Tell the user: "ADRs ADR-NNN, ADR-NNN are still Proposed; ratify them via `architect-draft --ratify` (or by manually flipping each `Status` field to `Accepted`) before drafting waves." Do not draft a wave doc against un-ratified ADRs — the architectural foundation isn't yet committed, and any wave plan built on it would inherit that uncertainty.

The exception: ADRs with status `Proposed` from `architect-review` (mid-cycle proposals) are not your concern — they get ratified by `wave-redraft`, not by re-running architect-draft. This refusal applies only at *initial* wave-draft time, when seed ADRs from `architect-draft` should have been ratified before wave planning starts.

### 2. Decide the wave ladder

The wave ladder is the most consequential decision in the draft. Aim for 3-6 waves. Fewer than 3 is probably too coarse; more than 6 suggests over-planning work that rolling-wave is designed to defer.

Four principles for choosing wave boundaries, in priority order:

**Walking skeleton first.** W1 is a vertical slice that exercises *every module* in the architecture, with minimal functional content. The point is to surface integration risk in W1, when the doc is still flexible. Example: if the architecture has modules `auth`, `clubs`, `polls`, then W1 includes a trivial path through all three (e.g., a user logs in, creates an empty club, sees an empty poll list). Horizontal-foundation W1s ("set up auth, then everything else") are allowed only with explicit justification in the Goal section.

**Risk-first ordering.** Among candidate post-W1 waves, order them so the scariest unknowns are tackled earliest. Scariness is a function of technical uncertainty, requirements uncertainty, and how many later waves depend on the answer.

**Value-first as tiebreaker.** When two candidate waves have similar risk profiles, pick the one that delivers more user value.

**Size for learning, not tidiness.** Each wave should be small enough to plan comprehensively without guessing, large enough to produce something observable. Awkward sizes are fine; uniformly-sized waves are usually a sign of optimizing for the wrong thing.

### 3. Fully plan W1

Expand W1 into stories, features, and tasks per the schema's Current Wave format. Specifically:

- **Entry criteria:** what must be true before W1 starts. For W1 specifically, this is usually "vision and architecture are ratified."
- **Exit criteria:** 2-5 testable bullets. The walking skeleton should produce something an auditor can run end-to-end and verify.
- **Repro path:** a script (e.g., `scripts/demo-w1.sh`) that exercises the exit criteria from a clean state. The path is committed; the script may be created during execution.
- **Stories:** one per (role, goal) pair that W1 advances. Acceptance criteria mandatory.
- **Features:** the capabilities W1 builds. Each feature supports at least one story.
- **Tasks:** sized for one agent session. Each has acceptance criteria. Each cites which stories/features it serves and which modules / ADRs it touches.
- **ADRs respected:** list the ADRs from the architecture doc that W1's tasks rely on.
- **New ADRs proposed:** if W1 will establish any new ADRs (uncommon for W1 since the architect-draft already seeded them; common for later waves), list them.

The first task should be the one that most reduces uncertainty. For W1, this is usually the end-to-end integration task — the one that proves the modules wire together at all.

### 4. Sketch future waves (W2 onward)

Each future wave gets the schema's Future Wave format and *only* that. No task breakdowns. No per-story acceptance criteria. No feature definitions beyond titles.

For each: Goal (one sentence), Theme, Depends-on, sketched Entry/Exit criteria, Candidate stories (titles only), Anticipated features (titles only), Assumptions/Risks/ADRs respected, possibly Anticipated new ADRs, and a 2-4 sentence Sketch of approach.

If you're tempted to draft tasks for W3, stop. That's future work whose shape you don't yet know. Pre-planning it defeats the rolling-wave point.

### 5. Seed the registers

**Assumptions register:** walk the vision's Open Questions. Each becomes a candidate assumption. Phrase as a belief, not a question (e.g., open question "single-choice or ranked voting?" → assumption A2 "voting is single-choice per member"). Cite the wave where the assumption first matters; status `untested` (or `open` for assumptions that don't get directly tested).

**Risks register:** distinct from assumptions. Risks are things that could go wrong even if assumptions hold. Each has a one-line mitigation. Don't pad — only include risks where you can name a real mitigation.

**ADR references table (Section 7):** populate from the seed ADRs. Each ADR's "Cited by" column reflects which waves cite it.

### 6. Fill the change log

Write the initial-draft entry. Be specific about what the wave doc was drafted from (vision version, architecture version, seed ADR IDs) and what's in the doc.

### 7. Save and verify

Write the file. Then re-read it checking the schema's invariants — especially: no task detail in future waves, every current-wave task has acceptance, every story and feature traces to a wave, every wave has exit criteria and a repro path.

## Walking skeleton — specific guidance

A walking skeleton is the most error-prone part of W1 to get right. Some heuristics:

**Functional minimum, structural maximum.** The walking skeleton's user-visible behavior is intentionally trivial — log in, see an empty page, see your name. The structural reach is intentionally complete — auth works, persistence works, deployment works, the modules are wired together end-to-end.

**Repro-able from a fresh checkout.** The repro script must take a clean state to a verified end-to-end run. If your repro depends on hidden setup, the walking skeleton is incomplete.

**One story is enough.** The walking skeleton typically has one user-facing story (often "I can log in") and the rest is plumbing. Don't pad with five stories; the value of W1 is integration, not breadth.

**Architectural completeness check.** Before you finalize W1, verify that every module in the architecture doc's Section 2 is touched by at least one task. If a module is not touched, either the module shouldn't exist yet (move it to a later architectural revision) or W1 isn't actually a walking skeleton (add a task that exercises the missing module).

## Filling each section — per-section notes

**Goal and non-goals (§1):** rewrite from the vision in your own words. The wave doc's Goal section is the executor and auditor's quick-reference; it must be sharp.

**Roles (§2):** copy from the vision. If the vision's role table is well-shaped, the wave doc's is identical.

**Waves overview (§3):** keep the one-line goal sharp. If you can't describe a wave's goal in ten words, the wave is fuzzy. Sharpen it.

**Assumptions register (§5):** read the vision's Open Questions carefully. Distinguish assumptions (things we're choosing to assume in order to proceed) from risks (things that could go wrong even if assumptions hold).

**Risks register (§6):** only include risks where you can say something useful about mitigation. A risk with no mitigation is either trivial or really an assumption in disguise.

**ADR references table (§7):** denormalize from the architecture doc and your wave-by-wave ADR citations. Each ADR's "Cited by" lists the waves that respect it.

**Themes not yet waved (§9):** anything from the vision's In Scope that isn't covered by W1-W6. Be explicit; this is how scope conversation has a place to live without bleeding into future-wave sketches.

## Invariants — things to never do

1. **No task-level detail in future waves.** Even if a W3 task is "obvious," don't write it down.
2. **Every current-wave task has acceptance criteria.** No exceptions.
3. **Every wave has exit criteria and a repro path.** A wave without them cannot be audited.
4. **Don't silently drop scope.** If an in-scope capability from the vision isn't covered by any wave, it goes in Section 9 (Themes not yet waved) with a one-line reason.
5. **Don't over-plan.** The comfort of a detailed plan is seductive. Resist.
6. **Don't violate the architecture.** If you find yourself wanting to plan something that contradicts an ADR, stop — either the ADR is wrong (run architect-review or trigger architect-draft revision) or the wave is wrong (replan).

## Worked example

Given a vision and architecture for `filetagger` (a CLI that tags files by content), with modules `walker`, `tagger`, `index`, `cli` and ADRs ADR-001 (SQLite persistence), ADR-002 (remote LLM tagger), ADR-003 (single-binary distribution):

- **W1 — Scan and tag (walking skeleton).** Tasks exercise all four modules end-to-end. One story: `filetagger scan <one-file>` produces one tagged row. Repro: `scripts/demo-w1.sh`. ADRs respected: 001, 002, 003.
- **W2 — Query by tag.** Sketched. Theme: query. Depends on: W1. Anticipated new ADR: query DSL syntax.
- **W3 — Incremental re-scan.** Sketched. Theme: efficiency. Depends on: W1, W2. Anticipated assumption: mtime+size as change signal.
- **Themes not yet waved:** watch mode, multi-machine sync, GUI.

## Handoff

After the wave doc is saved, tell the user the next step is `wave-execute` to build W1. The full cycle is execute → audit → architect-review → redraft.

**Git.** If the project uses git, suggest the user commit with `wave: initial wave doc, W1 <name>, W2+ sketched` and tag `wave-doc-v1`. Suggest also tagging `W1-start` on the same commit (it's the baseline for `wave-execute`'s diff). Add a `Co-authored-by: Claude <noreply@anthropic.com>` trailer. See `references/git-conventions.md`.
