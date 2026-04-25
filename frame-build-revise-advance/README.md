# Frame-Build-Revise-Advance

Four Claude skills for a one-human, one-smart-LLM coding process.

The process uses one evolving wave doc as the shared steering surface. The human provides direction and decisions. The LLM plans enough to move, builds with local implementation freedom, asks before crossing important boundaries, and records what matters for future work.

When commits are permitted, the process also uses Git history as an explainable implementation record. Stable must-have IDs in the wave doc connect intent to commits, verification receipts, and done-wave summaries.

When the LLM needs a human decision, it should provide informed options and a recommendation. Important choices should be evaluated for implementation by a smart coding agent, not only for abstract technical merit.

## The Loop

```text
Frame -> Build -> Revise as needed -> Advance -> Build -> Revise as needed -> Advance ...
```

## The Four Skills

### frame

Use `frame` to discover and finalize the project brief, then create or reshape the wave doc.

Typical uses:

- Start a project from a broad goal, partial stories, brainstorm, or product idea.
- Iteratively consult with the human to complete a working brief.
- Map concise must-haves to the waves that will address them.
- Finalize the brief and translate it into a wave doc.
- Expand the first wave into a full active wave.

`frame` is for shaping the plan, not implementing code.

When `frame` asks about stack, architecture, persistence, auth/security, integrations, deployment, or W1 scope, it should present the top options with tradeoffs and recommend the option most likely to be implemented reliably by Claude Code or Codex.

### build

Use `build` to implement the active wave.

The LLM should:

- Build the active wave's must-have requirements.
- Reference stable must-have IDs in implementation work and handoffs.
- Use existing codebase patterns.
- Make local, reversible implementation choices independently.
- Ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.
- Verify the must-have requirements with the cheapest credible tests, scripted checks, or manual demo.
- Create coherent implementation and wave-doc commits when commits are permitted.
- Report what was verified and what was not verified.

### revise

Use `revise` when the active wave needs adjustment before it can close.

Typical uses:

- Build revealed a requirement was wrong or ambiguous.
- Verification failed.
- Tasks need to be reshaped.
- A must-have should be dropped, deferred, or clarified.
- Lessons learned need to be recorded.
- Human decisions are needed.

`revise` keeps the current wave active. It does not close the wave or activate the next one.

When requirements change, `revise` preserves stable IDs, records superseded/deferred/dropped scope explicitly, and commits material wave-doc changes when commits are permitted.

When `revise` surfaces a decision, it should explain the failed assumption or verification gap, identify affected must-have IDs, and recommend a path forward.

### advance

Use `advance` when the active wave is ready to close.

`advance`:

- Converts the active wave to `done`.
- Summarizes delivered stories and features.
- Records durable decisions and follow-up notes.
- Chooses the next inactive wave.
- Expands exactly one next wave into `active`.

This is where closeout and next-wave activation happen.

When commits are permitted, `advance` commits the wave-state transition so the project history shows when one wave closed and the next became active.

When `advance` activates a wave with unresolved choices, it should frame those choices with options, tradeoffs, and a recommendation before encoding them as requirements.

## Informed Decisions

Decision prompts should be recommendation-backed. For stack, architecture, data model, persistence, auth/security, deployment, integrations, and other boundary-crossing choices, evaluate:

- Convention density.
- LLM-buildability by Claude Code or Codex.
- Local testability.
- Reversibility.
- Dependency risk.
- Security blast radius.
- Operational burden.
- Fit to active-wave scope.

See `references/decision-guidance-contract.md` for the decision prompt contract.

## Explainable Implementation History

The intended audit chain is:

```text
Must-have ID -> task(s) -> commit(s) -> verification receipt -> done-wave summary
```

Active-wave must-have requirements use stable IDs such as `W1-MH1`. Commit messages should reference those IDs, describe affected behavior and important surfaces, and include verification receipts. Git already records changed files, so commit messages should focus on intent and impact rather than repeating file lists.

See `references/commit-message-contract.md` for the commit message contract.

## Wave States

Each wave has exactly one state. During normal Build/Revise/Advance work, the wave doc should have exactly one active wave. Zero active waves is only a transitional state: before the first wave is framed, after the project is complete, while the human is reorganizing the doc, or during a deliberate pause. Never have more than one active wave.

### inactive

Future direction only. Keep inactive waves concise.

They should include:

- Goal.
- Must-have stories.
- Must-have features.
- Notes, constraints, or open questions.

They should not include detailed tasks, implementation plans, or formal acceptance criteria.

### active

Current build scope.

An active wave should include:

- Goal.
- Must-have requirements.
- Nice-to-have items.
- Implementation notes.
- Tasks.
- Decisions needed.
- Verification.

Must-have requirements are binding. If they are not implemented or explicitly dropped by the human, the wave is not done.

### done

Completed project memory.

A done wave should include:

- Delivered capability.
- Stories completed.
- Features completed.
- Decisions established.
- Follow-up notes.

Remove noisy task-level detail unless it matters later.

## Typical Project Flow

1. Start with `frame`.
2. Iterate with the human on inactive waves until the direction feels right.
3. Use `frame` to expand the first inactive wave into an active wave.
4. Use `build` to implement the active wave.
5. Use `revise` if build results, verification, or human feedback require changing the active wave.
6. Use `advance` once the active wave is ready to close.
7. Repeat from `build` on the newly active wave.

## Skill Layout

```text
frame-build-revise-advance/
|-- frame/
|   |-- SKILL.md
|   `-- references/
|       |-- fbra-schema.md
|       |-- commit-message-contract.md
|       `-- decision-guidance-contract.md
|-- build/
|   |-- SKILL.md
|   `-- references/
|       |-- fbra-schema.md
|       |-- commit-message-contract.md
|       `-- decision-guidance-contract.md
|-- revise/
|   |-- SKILL.md
|   `-- references/
|       |-- fbra-schema.md
|       |-- commit-message-contract.md
|       `-- decision-guidance-contract.md
|-- advance/
|   |-- SKILL.md
|   `-- references/
|       |-- fbra-schema.md
|       |-- commit-message-contract.md
|       `-- decision-guidance-contract.md
`-- references/
    |-- fbra-schema.md
    |-- commit-message-contract.md
    `-- decision-guidance-contract.md
```

The canonical schema is `references/fbra-schema.md`. The canonical commit contract is `references/commit-message-contract.md`. The canonical decision contract is `references/decision-guidance-contract.md`. Each skill also has mirrored copies so it can load its local references directly.
