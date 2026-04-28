# Spec and Waves

Spec and Waves is a lightweight process for AI-assisted software development. It is designed for a human lead working with LLM agents on small to medium projects where some structure is useful, but heavyweight product discovery would slow the work down.

The core pattern is:

```text
Human lead reviews and decides.
LLM drafts, proposes, executes, and reports.
```

## Flow

```text
Starter Spec
-> Backlog
-> Wave Plan
-> Execute Wave
-> Wave Report
-> Update Wave Plan
-> next wave
```

## Artifacts

By default, project artifacts live together in the project repo:

```text
docs/spec-and-waves/
  starter-spec.md
  backlog.md
  wave-plan.md
  reports/
    wave-W1-report.md
```

**Starter Spec**

A concise, human-readable spec that captures stable project intent:

- idea
- users
- rough user stories
- features
- key journeys
- scope
- open questions
- notes

The Starter Spec should stay short. It is not an implementation plan.

**Backlog**

A planning-ready translation of the Starter Spec:

- decision points
- plan goal and guardrails
- normalized user stories
- features
- deferred items
- open questions

The Backlog adds enough structure for planning, but avoids technical requirements and task breakdowns.

**Wave Plan**

A rolling implementation plan:

- maps every Backlog item to `W1`, `W2`, `Future Wave`, or `Deferred`
- fully details only the current wave
- keeps future waves as sketches
- tracks assumptions, risks, and change history

**Wave Report**

The execution handoff after a wave:

- what was built
- task status
- acceptance evidence
- assumptions and risks
- discoveries
- proposed changes
- next-wave readiness

Reports do not update the Wave Plan. They provide evidence for `update-wave-plan`.

## Commit Discipline

Each skill commits durable changes at handoff:

- `codesign-spec`: Starter Spec changes
- `draft-backlog`: Backlog changes
- `draft-wave-plan`: Wave Plan creation
- `execute-wave`: completed implementation slices, task checkbox updates, and Wave Reports
- `update-wave-plan`: Wave Plan reconciliation

Commit messages should be concise and traceable, using artifact sections and stable IDs where possible:

```text
Spec: clarify users and scope
Backlog: draft US-ADMIN-1..US-USER-3
Wave plan: map backlog to W1/W2/deferred
Wave W1: complete T1.1 import validation
Wave plan: close W1 and expand W2
```

Skills should not commit unrelated working-tree changes.

## Skills

**codesign-spec**

Co-designs the Starter Spec with the human lead. It fills missing stable project-level elements, proposes non-obvious Key Journeys, and avoids low-level implementation detail.

**draft-backlog**

Turns the approved Starter Spec into a concise Backlog with stories, features, priorities, guardrails, deferred items, and open questions.

**draft-wave-plan**

Turns the approved Backlog into a Wave Plan. It maps every story and feature to a wave or deferral, fully plans `W1`, and sketches later waves.

**execute-wave**

Implements only the current wave. It verifies task acceptance checks, updates task checkboxes, and writes a Wave Report.

**update-wave-plan**

Reconciles the Wave Plan with a Wave Report. It closes or keeps open the current wave, updates assumptions and risks, expands the next wave if appropriate, and writes the change log.

## Templates

Templates live in `templates/`:

- `starter-spec.template.md`
- `backlog.template.md`
- `wave-plan.template.md`
- `wave-report.template.md`

## Invariants

- The Starter Spec is the home for durable project commitments.
- The Backlog is the home for story and feature intent.
- The Wave Plan is the home for execution state.
- Reports are evidence and handoff, not plan edits.
- Future waves never contain task lists.
- Current-wave tasks always have acceptance checks.
- Every story and feature is covered or explicitly deferred.
- Scope changes must be explicit.

## When To Use

Use Spec and Waves for:

- new features or small systems with meaningful ambiguity
- multi-wave AI-assisted implementation
- projects where scope drift is likely
- work where each wave should teach the next

Use something lighter for one-sitting fixes, routine refactors, clear bug fixes, or throwaway prototypes.
