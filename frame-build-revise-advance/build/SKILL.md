---
name: build
description: Use this skill when an FBRA wave doc exists and the user wants the active wave implemented. It reads the active wave, builds the must-have requirements, uses implementation freedom for local reversible choices, asks before crossing the decision boundary, creates explainable commits when commits are permitted, updates task checkboxes, and reports verification. Trigger on "build the active wave", "implement W<N>", "run build phase", "do the current wave", or "proceed". Do not use to create the initial plan; use frame.
---

# Build

Implement the active wave. Before building, read `references/fbra-schema.md`, `references/commit-message-contract.md`, and the wave doc.

## Purpose

Build turns the active wave into working software while preserving human control over important product and architecture decisions.

## Inputs

- The FBRA wave doc.
- The project repo.
- Any user clarifications since the wave was framed.

## Output

- Code changes.
- The wave doc with completed task checkboxes updated.
- Coherent implementation and wave-doc commits when commits are permitted.
- A handoff message (see Handoff section).

## Workflow

1. Identify the single `Status: active` wave. If there is none or more than one, stop and ask the human to frame or advance the doc into a valid state.
2. Read its stable must-have IDs, requirements, implementation notes, decision boundary, tasks, and verification section.
3. Inspect the codebase enough to follow existing patterns.
4. If active-wave must-haves do not have stable IDs, add minimal IDs before building when the meaning is obvious; otherwise ask whether to normalize the wave doc first.
5. Build the must-have requirements. Nice-to-haves are optional and should only be done if cheap and low-risk.
6. Adjust tasks if needed while keeping must-have requirements stable. Keep edits to the wave doc minimal.
7. Ask the human before crossing the decision boundary.
8. Verify each must-have requirement with the cheapest credible test, scripted check, or manual demo.
9. Run relevant existing tests. Add focused tests for changed logic, persistence, APIs, permissions, migrations, parsers, data transformations, and bug fixes.
10. Update task checkboxes only for work that is actually done.
11. When commits are permitted, create commits at coherent implementation, verification, and wave-doc boundaries using the commit-message contract. If commit permission is unclear, ask before the first commit.
12. Handoff with verification results, relevant commits, and unresolved questions.

## Handoff

After build, send a single handoff message with these slots:

- **Changes**: files touched, wave-doc sections updated (one line each).
- **Committed**: commit hash, subject, and must-have IDs referenced, or `Not committed` with the reason.
- **Verified**: per must-have requirement, include the receipt — command run or action taken, and what was observed.
- **Not verified**: what and why.
- **Assumptions**: silent choices that could have gone another way, each tagged (reversible / costly / shipped-once).
- **Needs decision**: each framed as 2–3 options with tradeoffs and a recommendation.
- **Approved decisions**: add each to the wave doc's Decisions section with a one-line rationale; reference them by date in the handoff.

Be terse when things went as expected. Make surprises, skipped verifications, and crossed boundaries visually stand out (bold, or a leading `!`).

## Testing Bar

Always run relevant existing tests when feasible.

Add or update tests when the wave changes important behavior, especially:

- Business/domain logic.
- Data transformations.
- Persistence and migrations.
- API contracts.
- Auth, permissions, billing, or security-sensitive paths.
- Parsers and import/export formats.
- Bugs fixed during the wave.

Manual or browser-based demo is acceptable for UI feel, layout, copy, animations, and exploratory interaction quality. Still report exactly what was exercised.

If tests cannot be run, or a requirement cannot be verified, say `Not verified` and explain why.

When claiming verified, include a receipt — the command run or action taken, and what was observed. "Verified" without a receipt should read `Not verified`.

## Explainable Commits

Plan commits around natural feature or risk boundaries, such as auth, data model/migrations, permissions, APIs, user-visible workflows, verification fixes, and wave-doc state updates.

Every behavior-changing commit should reference the relevant must-have IDs. Wave-doc changes are material implementation history: commit them when commits are permitted, or ask the human whether to commit them. Prefer separate `docs` commits for scope, decision, verification, and wave-state changes. A small checkbox update may travel with an implementation commit only when it describes exactly the same completed and verified work.

Before committing, inspect the worktree and avoid staging unrelated user changes.

## Decision Boundary

The LLM may choose local, reversible implementation details consistent with existing patterns.

Stop and request human approval before crossing. Do not proceed without explicit approval:

- Product scope.
- Tech stack, data model, or persistence technology.
- Architecture or major dependencies.
- External services.
- Auth/security behavior.
- Pricing/billing behavior.
- User-visible workflow assumptions.

Rule of thumb: if removing the choice later would require a migration, a schema change, or a user-visible break, it is not local.

When asking, present 2–3 options with tradeoffs and a recommendation. Do not pose open questions.

Existing precedent in the codebase or a prior entry in Decisions counts as approval — do not re-ask. If precedent is ambiguous (two patterns in use, or the codebase is empty), treat it as no precedent and ask.

When approval is granted, record it in Decisions: what was decided, alternatives considered, a one-line rationale, and the date. Future waves must honor recorded Decisions unless the human supersedes them.

## Do Not

- Do not build inactive-wave scope unless the human explicitly pulls it in.
- Do not call the wave done while must-have requirements are unmet.
- Do not claim verification that was not performed.
- Do not let nice-to-haves delay or reshape the must-have work.
- Do not create vague commits such as "implement wave" when smaller explainable boundaries are available.
