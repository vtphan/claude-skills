---
name: wave-plan
description: Use this skill when a vision doc and a ratified architecture doc exist, and the user wants the initial wave plan drafted. Triggers include phrases like "draft the wave plan from the vision and architecture", "produce the initial wave plan for this project", "what's W1 for this project", "break this into waves with W1 as a walking skeleton", or whenever the upstream vision and architecture artifacts are ready and the next step is committing them into a rolling-wave plan. Do NOT use when no architecture doc exists yet (run `architect draft` first). Do NOT use to revise an existing wave plan — that's `wave-update`. Do NOT use to write code; this skill produces a planning document only.
---

# Wave Plan

Produce the first version of the unified wave plan from the vision and architecture. The wave plan unifies requirements (stories, journeys, features) and plan (waves, tasks) into a single rolling document. W1 defaults to a **walking skeleton** — a thin vertical slice that exercises every architecture module marked `W1: required` with minimal functional content.

This is a one-time skill at project start. Subsequent edits to the wave plan are made by `wave-update`.

Before doing anything else, read `references/wave-schema.md` and `references/architecture-schema.md` in full.

## Inputs and output

**Inputs:**
- The vision doc (`<project-slug>-vision.md`). Source of goal, non-goals, roles, in-scope capabilities, success metrics, and (if present) core journeys.
- The architecture doc (`<project-slug>-architecture.md`). Source of modules, key interfaces, and the embedded Decision Log.
- All cited Decision Log entries must have `Status: Accepted` (the architecture doc has been ratified). If any are still `Proposed`, refuse to run.

**Output:** `<project-slug>-wave-plan.md` written to `docs/`. Frontmatter has `wave_plan_version: 1`, `current_wave: W1`, `status: in_progress`, with paths to the source vision and architecture.

## Workflow

### 0. Consult process notes (if present)

If `docs/<project-slug>-process-notes.md` exists, read your section (`## wave-plan`). Apply **Do** items at the appropriate steps in the workflow below; apply **Don't** items by skipping or simplifying the named standard step. Each note carries a one-sentence justification — if a note is unjustified, flag it to the user before proceeding.

If a note appears to:
- Eliminate an invariant from the "things to never do" list,
- Redefine artifact shapes (new fields, new sections, structural changes), or
- Replace the cycle (e.g., "skip wave-plan entirely"),

refuse to apply it and surface to the user — that's a bail case, schema change, or category mismatch, not a notes case. See `references/process-notes-schema.md` for the cap on notes' scope.

If the file is absent, run Full VADER's wave-plan workflow as written.

### 1. Read the vision and architecture thoroughly

Extract:
- **From the vision:** goal, non-goals, roles, in-scope capabilities, success metrics, open questions, core journeys (if present).
- **From the architecture:** the module list (Section 2), key interfaces (Section 3), and the Decision Log entries.

If either input is missing or inconsistent — e.g., the architecture doesn't have a module needed to support an in-scope capability — stop and ask the user.

### 2. Refuse to run if Decision Log has Proposed entries

Walk the architecture doc's Decision Log section. If any entry has `Status: Proposed`, stop. Tell the user: "Decision Log entries ADR-NNN, ADR-NNN are still Proposed; ratify them via `architect ratify` (or by manually flipping each `Status`) before drafting waves."

### 3. Decide the wave ladder

Aim for 3-6 waves. Four principles, in priority order:

**Walking skeleton first.** W1 is a vertical slice that exercises every architecture module marked `W1: required`, with minimal functional content. Modules marked `deferred (W<N>)` are preserved in the architecture but are not forced into W1. The point is to surface active integration risk in W1, when the plan is still flexible. Horizontal-foundation W1s ("set up auth first") are allowed only with explicit justification in the Goal section.

**Risk-first ordering.** Among candidate post-W1 waves, order them so the scariest unknowns are tackled earliest. Scariness = technical uncertainty + requirements uncertainty + how many later waves depend on the answer.

**Value-first as tiebreaker.** When two candidate waves have similar risk profiles, pick the one that delivers more user value.

**Size for learning, not tidiness.** Each wave should be small enough to plan comprehensively without guessing, large enough to produce something observable. Awkward sizes are fine.

### 4. Fully plan W1

Expand W1 per the schema's Current Wave format:
- **Entry criteria:** for W1 specifically, "vision and architecture are ratified."
- **Exit criteria:** 2-5 testable bullets. The walking skeleton should produce something an external reader can run end-to-end and verify.
- **Expected touched modules:** the union of modules each W1 task names in its `Touches` field, plus any cross-cutting plumbing (test infra, build config, scripts) the wave will modify. Module-level granularity, drawn from architecture Section 2. The review subagent uses this to detect scope drift.
- **Repro path:** a script (e.g., `scripts/demo-w1.sh`) that exercises the exit criteria from a clean state.
- **Stories:** one per (role, goal) pair W1 advances. Acceptance criteria mandatory. INVEST filter applies.
- **Features:** the capabilities W1 builds. Each supports at least one story.
- **Tasks:** sized for one agent session. Each has acceptance criteria. Each cites stories/features it serves and modules / Decision Log entries it touches.
- **ADRs respected:** list the entries from the Decision Log that W1's tasks rely on.

The first task should be the one that most reduces uncertainty — usually the end-to-end integration task that proves the modules wire together.

### 5. Sketch future waves (W2 onward)

Each future wave gets the schema's Future Wave format and *only* that. No task breakdowns. No per-story acceptance criteria. No feature definitions beyond titles.

For each: Goal, Theme, Depends-on, sketched Entry/Exit criteria, Candidate stories (titles only), Anticipated features (titles only), Assumptions/Risks/ADRs respected, Anticipated new ADRs, and a 2-4 sentence Sketch.

If you find yourself drafting tasks for W3, stop. That's future work whose shape you don't yet know.

### 6. Seed the registers

**Assumptions register:** walk the vision's Open Questions. Each becomes a candidate assumption (phrased as a belief, not a question). Cite the wave where it first matters; status `untested` (or `open`).

**Risks register:** distinct from assumptions. Risks are things that could go wrong even if assumptions hold. Each has a one-line mitigation. Don't pad — only include risks where you can name a real mitigation.

**Decision Log references table (Section 7):** populate from the architecture's Decision Log. Each entry's "Cited by" column reflects which waves cite it.

### 7. Walking-skeleton completeness check

Before finalizing, verify that every module in the architecture's Section 2 marked `W1: required` is touched by at least one W1 task. Modules marked `W1: deferred (W<N>)` are skipped — they're expected to come online in a later wave.

If a `required` module is not touched by any W1 task, either:
- the module shouldn't have been marked required (raise with the user; may want to flip to deferred and re-run this check), or
- W1 isn't actually a walking skeleton (add a task that exercises the missing module).

If the architecture pre-dates the `W1` column (no activation status on modules), default to "all modules are required" and apply the original check.

### 8. Fill the change log and save

Write the initial-draft entry. Be specific about what was drafted from (vision version, architecture version, seed ADR IDs).

Re-read the file checking the schema's invariants — especially: no task detail in future waves, every current-wave task has acceptance, every story and feature traces to a wave, every wave has exit criteria and a repro path.

## Invariants — things to never do

1. **No task-level detail in future waves.**
2. **Every current-wave task has acceptance criteria.** No exceptions.
3. **Every wave has exit criteria and a repro path.**
4. **Don't silently drop scope.** If an in-scope capability isn't covered by any wave, it goes in Section 9 (Themes not yet waved) with a one-line reason.
5. **Don't over-plan.** The comfort of detail is seductive. Resist.
6. **Don't violate the architecture.** If you find yourself wanting to plan something that contradicts a Decision Log entry, stop — either the entry is wrong (rare; flag for architect re-run) or the wave is wrong (replan).

## Worked example

Given a vision and architecture for `filetagger` with modules `walker`, `tagger`, `index`, `cli` and entries ADR-001 (SQLite), ADR-002 (remote LLM tagger), ADR-003 (single-binary):

- **W1 — Scan and tag (walking skeleton).** Tasks exercise all four modules end-to-end. One story: `filetagger scan <one-file>` produces one tagged row. Repro: `scripts/demo-w1.sh`. ADRs respected: 001, 002, 003.
- **W2 — Query by tag.** Sketched. Theme: query. Anticipated new ADR: query DSL syntax.
- **W3 — Incremental re-scan.** Sketched. Theme: efficiency. Anticipated assumption: mtime+size as change signal.
- **Themes not yet waved:** watch mode, multi-machine sync, GUI.

## Handoff

After the wave plan is saved, tell the user the next step is `wave-execute` to build W1.

**Git.** Check whether git is in use (`git rev-parse --is-inside-work-tree`). If yes, after the user approves the wave plan, commit yourself: `git commit -m "wave: initial wave plan, W1 <name>, W2+ sketched" -m "..." -m "Co-authored-by: Claude <noreply@anthropic.com>"`. Then tag both `wave-plan-v1` and `W1-start` on the same commit — it's the baseline for `wave-execute`'s diff scoping.

Tell the user about the commit (sha, tags). Override with `git reset --soft HEAD~1` if amending is needed. If git is not in use, save normally and note no commit was made; warn that without git, `wave-update`'s review subagent will have a fuzzier diff baseline. See `../references/git-conventions.md`.
