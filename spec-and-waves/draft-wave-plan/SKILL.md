---
name: draft-wave-plan
description: Use this skill when the user has an approved Spec and Waves Backlog and wants a rolling Wave Plan drafted or revised. This skill maps every backlog story and feature to W1, W2, Future Wave, or Deferred; proposes wave sequencing based on value, risk, dependencies, and learning; fully details only the current wave; and keeps future waves as concise sketches. Use when the user says things like "draft the wave plan", "plan this in waves", "turn this backlog into a wave plan", "create the implementation waves", or provides a <project>-backlog.md and asks for planning. Do NOT use for code implementation, executing tasks, post-wave updates, or detailed requirements beyond current-wave task acceptance.
---

# Draft Wave Plan

Turn an approved Backlog into a rolling Wave Plan. The LLM proposes sequencing; the human lead reviews value, risk, scope, and first-wave detail.

Read `../templates/wave-plan.template.md` before producing a full plan. If it is unavailable, use the section order in this skill.

## Output Contract

Return three sections:

1. **Draft Wave Plan** — the full proposed plan, using this structure:
   - `Goal and Guardrails`
   - `Backlog Coverage`
   - `Waves Overview`
   - `Waves`
   - `Assumptions`
   - `Risks`
   - `Change Log`
2. **Planning Rationale** — concise bullets explaining wave sequence, W1 choice, major deferrals, and risk-first decisions.
3. **Leader Decisions** — at most 5 decisions the human should make before execution. Omit if none.

## Core Rule

Fully plan only the current wave. Future waves are sketches.

The current wave gets tasks with acceptance checks. Future waves get goal, coverage, entry criteria, exit criteria, assumptions, risks, and a short sketch. No future-wave task lists.

## Backlog Coverage

Map every `US-*` and `F-*` from the Backlog to one of:

- `W1`
- `W2`
- `Future Wave`
- `Deferred`

Use a rationale column. This is a scope-control mechanism: nothing from the approved Backlog is silently dropped, and every early/late/deferred choice is reviewable by the human lead.

## Wave Selection Principles

Choose waves in this order of priority:

1. **Learning and risk first.** Pull the most consequential uncertainty early.
2. **Thin usable slice.** Prefer a first wave that demonstrates value end-to-end.
3. **Dependency honesty.** Do prerequisite work early only when it truly unlocks user-visible work.
4. **Scope discipline.** Defer attractive but nonessential work explicitly.
5. **Human reviewability.** Make the sequencing rationale easy to challenge.

Avoid setup-only W1 unless the Backlog makes a technical foundation unavoidable. If W1 is mostly setup, explain why.

## Current Wave Detail

For W1, include:

- Goal.
- Covers: story and feature IDs.
- Depends on.
- Entry criteria.
- Exit criteria.
- Assumptions.
- Risks.
- Tasks with acceptance checks.

Tasks should be small enough for an implementation agent to complete in one sitting. Every task needs a concrete acceptance check. Tasks may mention likely files/modules only if useful; do not over-specify implementation.

## Future Wave Sketches

For W2 and later, include only:

- Goal.
- Covers.
- Depends on.
- Entry criteria.
- Exit criteria.
- Assumptions.
- Risks.
- Sketch: 2-4 sentences.

No task lists. No low-level design. No detailed requirements.

## Assumptions and Risks

Add only assumptions and risks that materially affect sequencing or execution.

Good assumptions:

- A user behavior belief that affects W1 vs W2.
- A technical feasibility belief that the first wave should test.
- A dependency or data availability belief.

Good risks:

- Scope likely to expand.
- Integration uncertainty.
- Trust, approval, adoption, or recovery-path risk.
- A future wave depending on an unvalidated W1 result.

Do not pad these registers.

## What Does Not Belong

Do not add:

- Tasks for future waves.
- Architecture documents.
- Database schemas or APIs.
- Detailed technical requirements.
- Code-level implementation steps.
- Dates, owners, or Gantt-style schedules unless the user asks.

## Quality Bar

A good Wave Plan:

- Covers or defers every Backlog item.
- Makes W1 executable.
- Keeps W2 and later lightweight.
- Explains sequencing tradeoffs.
- Helps the human lead challenge hidden scope, risk, and priority.
