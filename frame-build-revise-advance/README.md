# Frame-Build-Revise-Advance

Four Claude skills for a one-human, one-smart-LLM coding process.

The process uses one evolving wave doc as the shared steering surface. The human provides direction and decisions. The LLM plans enough to move, builds with local implementation freedom, asks before crossing important boundaries, and records what matters for future work.

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

### build

Use `build` to implement the active wave.

The LLM should:

- Build the active wave's must-have requirements.
- Use existing codebase patterns.
- Make local, reversible implementation choices independently.
- Ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.
- Verify the must-have requirements with the cheapest credible tests, scripted checks, or manual demo.
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

### advance

Use `advance` when the active wave is ready to close.

`advance`:

- Converts the active wave to `done`.
- Summarizes delivered stories and features.
- Records durable decisions and follow-up notes.
- Chooses the next inactive wave.
- Expands exactly one next wave into `active`.

This is where closeout and next-wave activation happen.

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
|   `-- references/fbra-schema.md
|-- build/
|   |-- SKILL.md
|   `-- references/fbra-schema.md
|-- revise/
|   |-- SKILL.md
|   `-- references/fbra-schema.md
|-- advance/
|   |-- SKILL.md
|   `-- references/fbra-schema.md
`-- references/
    `-- fbra-schema.md
```

The canonical schema is `references/fbra-schema.md`. Each skill also has a mirrored copy so it can load its local reference directly.
