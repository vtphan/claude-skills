# Spec and Waves: A Lean Process for AI-Assisted Software Development

## Overview

Spec and Waves is a lightweight process for designing and building small to medium software projects with AI assistance. It is a new process that arose from Seed-and-Iterate and Waves, but it has its own artifact and skill contracts.

It keeps the useful inheritance:

- A short Starter Spec captures the durable intent humans must commit to.
- A compact Backlog turns that intent into buildable stories and features.
- A Wave Plan drives implementation one wave at a time.
- Wave Reports capture what changed, what was learned, and what should happen next.

The process is calibrated for projects that take days to a few weeks, not months of product discovery. It is meant for one person or a small team working with AI agents, where the goal is enough structure to prevent drift without creating a documentation project.

## Principles

**One durable source of truth.** The Starter Spec holds project-level commitments. If a decision should still matter two waves from now, it belongs in the Starter Spec.

**One execution source of truth.** The Wave Plan holds current execution state: wave order, task status, assumptions, risks, and change history.

**Backlog before Wave Plan, not full specification.** The Backlog names what should be built and why. It does not try to specify every threshold, field, or edge case up front.

**Plan near work in detail, later work in sketches.** The current wave gets tasks with acceptance criteria. Future waves get goals, coverage, exit criteria, assumptions, risks, and a short sketch.

**Reports preserve learning.** Reports do not update the Wave Plan. They capture execution results and give the updater evidence to interpret.

**Escalate only when the project earns it.** Journeys, full requirement specs, privacy reviews, and methodologist reviews are optional tools, not default stages.

## Artifacts

The default process uses four artifacts:

```text
docs/spec-and-waves/
  starter-spec.md
  backlog.md
  wave-plan.md
  reports/
    wave-W<N>-report.md
```

If a project already has a documentation convention, use the nearest equivalent directory, but keep the Spec and Waves artifacts together.

The default process uses four artifact types:

1. `starter-spec.md`
2. `backlog.md`
3. `wave-plan.md`
4. `reports/wave-W<N>-report.md`

Templates live in `templates/` and are intentionally minimal. Skills should preserve their structure unless the process doc changes first.

Optional artifacts are allowed, but they must justify themselves. If an artifact will not change build decisions, do not create it.

### Starter Spec

The Starter Spec is the smallest project-level specification the human is willing to stand behind. It should be quick for a human leader to draft, even if it is incomplete. The LLM's job is to turn this rough intent into a sharper Backlog and Wave Plan.

Use this schema:

```markdown
# <Project> Starter Spec

## Idea
What are we trying to build, for whom, and why now?

## Users
- Who will use this, operate it, approve it, or be affected by it?

## User Stories
- As a <user>, I want <capability>, so that <benefit>.
- Rough/incomplete stories are fine.

## Features
- Capability or behavior the system probably needs.

## Technical Stack
- Committed stack choices, if any.
- Options the LLM should compare, with concise pros/cons for the human lead.
- Unknowns that affect stack choice.

## Key Journeys
- Optional. Non-obvious journey where a user is trying to <goal>, but <specific pain point, risk, or hidden friction> may shape what should be built.
- LLM-suggested journeys are prompts for human assessment, not settled facts.

## Scope
In:
- Thing that should be included.

Out:
- Thing the AI might otherwise add, but should not.

## Open Questions
- What are we unsure about?
- What should the LLM make a reasonable proposal for?

## Notes
- Anything else the LLM should know before drafting a backlog or plan.
```

Guidelines:

- Write fast. Fragments are fine.
- Keep decisions project-level. Iteration goals, detailed requirements, and wave tasks belong downstream.
- Prefer bullets over prose unless a paragraph is faster.
- If the Starter Spec grows beyond one page, move detail into the Backlog or Wave Plan.
- Do not force source tags, metrics, or a change log into the first draft. Add them only if they clarify a real decision.

### Backlog

The Backlog is the build contract. It is drafted from the Starter Spec and revised by human reaction. It replaces the heavier Context, Goal, Journey, and Story-and-Requirements stack from Seed-and-Iterate.

Use this schema:

```markdown
# <Project> Backlog

## Decision Points
1. The few choices the human should react to before planning.

## Goal for This Plan
One paragraph: what the next plan should deliver.

## Guardrails
In:
- Iteration-level scope.

Out:
- Iteration-level cuts.

## Stories

### US-<ROLE>-<N>: <Title>
As a <role>, I want <capability>, so that <benefit>.

Context: The user moment, friction, or need this story addresses.
Priority: must | should | could
Source: observed | assumed | validated

Acceptance sketch:
- Given ..., when ..., then ...
- Given ..., when ..., then ...

Notes:
- Optional constraints, ambiguity, or known edge cases.

## Features

### F-<N>: <Title>
Description: One or two sentences.
Supports: US-...
Priority: must | should | could
Notes: Optional.

## Deferred
- Story or feature considered but intentionally left out, with reason.

## Open Questions
- Questions that affect planning or implementation.
```

Guidelines:

- A story should be small enough to place in a wave, not necessarily small enough to implement in one task.
- Acceptance sketches are user-facing checks, not full technical requirements.
- Features are supporting capabilities, not separate product epics.
- Every must-have story should support the plan goal.
- If a story needs research-grade journey evidence, create a Journey artifact for that story's role. Otherwise keep journey context inline.

### Wave Plan

The Wave Plan inherits the rolling-wave shape from Waves. It is the single execution state file for Spec and Waves.

Use this structure:

```markdown
---
plan_version: 1
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
source_starter_spec: docs/spec-and-waves/starter-spec.md
source_backlog: docs/spec-and-waves/backlog.md
current_wave: W1
status: in_progress
---

# <Project> Wave Plan

## 1. Goal and Guardrails
## 2. Backlog Coverage
## 3. Waves Overview
## 4. Waves
## 5. Assumptions
## 6. Risks
## 7. Change Log
```

Wave Plan rules:

- Backlog Coverage maps every `US-*` and `F-*` from the Backlog to `W1`, `W2`, `Future Wave`, or `Deferred`, with rationale.
- The current wave has tasks with acceptance criteria.
- Future waves have no tasks.
- Assumptions are never deleted. Broken assumptions are marked broken and replaced with new IDs.
- The change log is append-only.
- The Wave Plan may summarize learnings from past waves, but the full evidence lives in Reports.

### Wave Report

Reports are archival handoff documents written after execution of a wave. They should be short unless something surprising happened.

Use this schema:

```markdown
# W<N> <Wave Name> — Report

Wave: W<N>
Completed: YYYY-MM-DD
Wave plan version at start: <N>

## What was built
What a user or maintainer can now do.

## Task status
- [x] T<N>.1 — Done.
- [~] T<N>.2 — Partial, with reason.

## Acceptance evidence
- Tests, commands, screenshots, review notes, or manual checks used.

## Assumptions and risks
- A<N>: validated | broken | untested, with evidence.
- R<N>: materialized | did not materialize | changed.

## Discoveries
- Things learned that affect later waves, scope, or the Starter Spec.

## Proposed changes
- Add, remove, defer, or revise scope, with rationale.

## Next-wave readiness
- Anything the next wave needs before it starts.
```

Guidelines:

- Omit empty sections only when they truly have no content.
- Be specific with task IDs, story IDs, assumption IDs, and risk IDs.
- Reports do not edit the Wave Plan.

## Commit Discipline

Each skill commits durable changes before handoff. Commits are part of the traceability system, not just version control hygiene.

Default commit responsibilities:

- `codesign-spec`: commits `docs/spec-and-waves/starter-spec.md`.
- `draft-backlog`: commits `docs/spec-and-waves/backlog.md`.
- `draft-wave-plan`: commits `docs/spec-and-waves/wave-plan.md`.
- `execute-wave`: commits completed implementation slices, current-wave task checkbox updates, and `reports/wave-W<N>-report.md`.
- `update-wave-plan`: commits `docs/spec-and-waves/wave-plan.md` updates.

Commit rules:

- Commit only files touched for the current skill handoff.
- Do not include unrelated working-tree changes.
- Use concise messages that reference artifact sections or stable IDs.
- Prefer IDs over prose when possible: `US-*`, `F-*`, `W*`, `T*`, `A*`, `R*`.
- During execution, commit coherent completed task groups rather than waiting for a large wave-end commit if the wave is substantial.

Examples:

```text
Spec: clarify users and scope
Backlog: draft US-ADMIN-1..US-USER-3
Wave plan: map backlog to W1/W2/deferred
Wave W1: complete T1.1 import validation
Wave report: record W1 acceptance evidence
Wave plan: close W1 and expand W2
```

## Optional Artifacts

### Journey

Create a Journey only when the project has novel UX, multiple roles with handoffs, or user behavior uncertainty that will materially change the build.

Keep it to one page:

```markdown
# Journey: <Title>

Persona: <role>
Scenario: One paragraph.

| Stage | User action | Friction | System touchpoint | Source |
|-------|-------------|----------|-------------------|--------|

## Insights
- Design-relevant takeaways.

## Story links
- US-...
```

### Requirement Detail

Create per-story requirement detail only when acceptance sketches are too weak to implement safely. This is an escalation, not a default stage.

Use it for security, data migration, performance, privacy, protocol, billing, or other high-risk work:

```markdown
## Requirement Detail: US-<ROLE>-<N>

Functional:
- Requirement. Verification.

Non-functional:
- Requirement. Verification.

Data:
- Requirement. Verification.

Edge cases:
- Requirement. Verification.
```

Requirement detail can live inside the Wave Plan's current-wave notes or in the Wave Report if it was discovered during execution. Do not produce requirement detail for future waves.

## Skill Set

Spec and Waves should define its own skills rather than reusing the predecessor skills unchanged. The predecessor skills are reference material, not the contract.

The process needs five default skills and two optional skills.

**codesign-spec** co-designs `docs/spec-and-waves/starter-spec.md` with the human leader. It fills missing stable project-level elements, proposes concise additions, and avoids implementation detail that belongs downstream.

**draft-backlog** drafts or revises `docs/spec-and-waves/backlog.md` from the Starter Spec. It normalizes rough user stories and feature notes into a planning-ready Backlog. It does not produce full technical requirements by default.

**draft-wave-plan** drafts `docs/spec-and-waves/wave-plan.md` from the Starter Spec and Backlog. It maps every Backlog item to a wave or deferral, fully plans W1, and sketches later waves.

**execute-wave** executes the current wave only. It updates task checkboxes and writes the wave Report. If a story needs requirement detail before implementation, it drafts just enough detail for that current story and records it in the Report or current-wave notes.

**update-wave-plan** reads the Wave Plan and Report, closes or keeps open the current wave, updates assumptions and risks, expands the next wave if appropriate, and writes the change-log entry.

**Journey Mapper** is optional. Use it only when inline story context is not enough.

**Reviewer** is optional but recommended at gates. Default modes for this process are `traceability-check`, `skeptical-engineer`, and `pruning-pass`. Use privacy or methodologist modes only when the project actually has those risks.

## Process

### Stage 0: Starter Spec

The human writes or sketches the Starter Spec. `codesign-spec` proposes a tightened version. The human accepts or edits it.

Time: 15-30 minutes.

Gate:

- The Starter Spec gives enough idea, users, rough stories, feature notes, technical stack context, key journeys, scope, and questions for the LLM to draft a plausible Backlog.

### Stage 1: Backlog

`draft-backlog` creates a clean Backlog from the Starter Spec. The human reviews decision points, scope cuts, priorities, and acceptance sketches.

Optional: create a Journey only if the Backlog has weak user-context assumptions that would change story shape.

Time: 20-45 minutes.

Gate:

- Must-have stories support the plan goal.
- Every story has an acceptance sketch.
- Every feature supports at least one story.
- Deferred items are explicit.

### Stage 2: Wave Plan

`draft-wave-plan` creates the rolling Wave Plan from the Starter Spec and Backlog.

Time: 20-40 minutes.

Gate:

- Every story and feature is mapped to `W1`, `W2`, `Future Wave`, or `Deferred`, with rationale.
- W1 has tasks with acceptance criteria.
- Future waves are sketches only.
- Assumptions and risks are present but not padded.

### Stage 3: Wave Loop

For each wave:

1. `execute-wave` implements the current wave only.
2. The executor writes a Report.
3. The human or AI checks whether discoveries affect the Starter Spec or Backlog.
4. If project-level commitments changed, update the Starter Spec. If unbuilt story scope changed, update the Backlog.
5. `update-wave-plan` reconciles the Report into the Wave Plan and advances or replans.

Gate to next wave:

- Report exists.
- Acceptance evidence is recorded.
- Wave Plan registers and change log are updated.
- Starter Spec or Backlog changes, if needed, are made before expanding the next wave.

## Invariants

1. The Starter Spec is the only home for durable project commitments.
2. The Backlog is the only home for story and feature intent.
3. The Wave Plan is the only home for execution state.
4. Reports are evidence and handoff, not Wave Plan edits.
5. Future waves never contain task lists.
6. Current-wave tasks always have acceptance criteria.
7. Every story and feature is covered or explicitly deferred.
8. Assumptions and change-log entries are append-only.
9. Scope changes are explicit in the Wave Plan change log.
10. Optional artifacts are created only when they change decisions.

## Human Time Budget

For a typical small/medium project:

- Starter Spec: 15-30 minutes.
- Backlog: 20-45 minutes.
- Wave Plan: 20-40 minutes.
- Per wave: 10-20 minutes reviewing report/update, plus any review of risky requirement detail.

Most projects should start implementation after 1-2 hours of artifact work. If the process takes longer than that before code starts, either the project is larger than expected or the artifacts are too heavy.

## When to Use

Use this process for:

- New features or small systems with meaningful ambiguity.
- Multi-wave AI-assisted implementation.
- Projects where scope drift is likely without a written anchor.
- Work where later waves should learn from earlier waves.

Use something lighter for:

- One-sitting fixes.
- Routine refactors.
- Bug fixes with clear reproduction.
- Throwaway prototypes.

Use something heavier only when:

- Multiple stakeholders must approve artifacts.
- User research is a core deliverable.
- Compliance, privacy, data quality, or research methodology materially shape the build.

## Maintenance

After each project, ask:

- Which artifact changed a build decision?
- Which artifact was ignored?
- Which gate caught a real issue?
- Which skill produced too much detail?
- Which optional artifact should become default for this project type, if any?

Then tighten the schemas and skills. The process should stay smaller than the work it supports.

## Summary

Default to four artifacts: Starter Spec, Backlog, Wave Plan, and Reports. Keep the Starter Spec short, the Backlog build-oriented, the Wave Plan rolling-wave, and Reports evidence-focused. Add Journeys or full requirement detail only when the project has enough UX, compliance, data, or technical risk to justify the extra weight.
