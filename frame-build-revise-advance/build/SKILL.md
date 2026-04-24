---
name: build
description: Use this skill when an FBRA wave doc exists and the user wants the active wave implemented. It reads the active wave, builds the must-have requirements, uses implementation freedom for local reversible choices, asks before crossing the decision boundary, updates task checkboxes, and reports verification. Trigger on "build the active wave", "implement W<N>", "run build phase", "do the current wave", or "proceed". Do not use to create the initial plan; use frame.
---

# Build

Implement the active wave. Before building, read `references/fbra-schema.md` and the wave doc.

## Purpose

Build turns the active wave into working software while preserving human control over important product and architecture decisions.

## Inputs

- The FBRA wave doc.
- The project repo.
- Any user clarifications since the wave was framed.

## Output

- Code changes.
- The wave doc with completed task checkboxes updated.
- A concise handoff message listing what changed, what was verified, what was not verified, and any decisions needed.

## Workflow

1. Identify the single `Status: active` wave. If there is none or more than one, stop and ask the human to frame or advance the doc into a valid state.
2. Read its must-have requirements, implementation notes, decision boundary, tasks, and verification section.
3. Inspect the codebase enough to follow existing patterns.
4. Build the must-have requirements. Nice-to-haves are optional and should only be done if cheap and low-risk.
5. Adjust tasks if needed while keeping must-have requirements stable. Keep edits to the wave doc minimal.
6. Ask the human before crossing the decision boundary.
7. Verify each must-have requirement with the cheapest credible test, scripted check, or manual demo.
8. Run relevant existing tests. Add focused tests for changed logic, persistence, APIs, permissions, migrations, parsers, data transformations, and bug fixes.
9. Update task checkboxes only for work that is actually done.
10. Handoff with verification results and unresolved questions.

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

## Decision Boundary

The LLM may choose local, reversible implementation details consistent with existing patterns.

Ask before changing:

- Product scope.
- Data model or persistence technology.
- Architecture or major dependencies.
- External services.
- Auth/security behavior.
- Pricing/billing behavior.
- User-visible workflow assumptions.

## Do Not

- Do not build inactive-wave scope unless the human explicitly pulls it in.
- Do not call the wave done while must-have requirements are unmet.
- Do not claim verification that was not performed.
- Do not let nice-to-haves delay or reshape the must-have work.
