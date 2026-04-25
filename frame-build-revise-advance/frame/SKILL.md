---
name: frame
description: Use this skill when the user wants to discover, frame, or reshape a project for a one-human, one-smart-LLM coding process. It starts from a broad goal, partial stories, notes, an existing brief, or a messy plan; iteratively consults with the human to complete a working brief; then translates the finalized brief into a concise Frame-Build-Revise-Advance wave doc with stable must-have IDs, one expanded active first wave, and concise inactive future waves. Trigger on requests like "frame this project", "discover the requirements", "create the working brief", "create the wave doc", "plan the first wave", "turn this idea into waves", "set up FBRA", or "reframe the plan". Do not use for actually building code; use build for implementation.
---

# Frame

Discover and frame the project with the human, then create or reshape the project's wave doc. Before writing the wave doc, read `references/fbra-schema.md` and `references/decision-guidance-contract.md`. If commits are permitted or the human asks for committed history, also read `references/commit-message-contract.md`.

## Purpose

Frame helps the human driver discover and finalize the project brief, then gives a smart LLM enough direction to build with freedom while preserving human control over scope, architecture, and product decisions.

## Inputs

- A broad goal, partial user stories, brainstorm, product idea, existing requirements, existing brief, existing wave doc, or current codebase context.
- Human answers during discovery.

## Output

- A working brief, usually `docs/<project-slug>-brief.md`.
- After human finalization, a wave doc, usually `docs/<project-slug>-waves.md`.
- If paths are ambiguous, choose `docs/` when it exists; otherwise place the files beside the source brief.
- If commits are permitted, a docs commit for material wave-doc creation or reshaping; otherwise ask whether the human wants the wave-doc change committed.

## Workflow

1. Start with discovery. Derive an initial framing hypothesis from the user's input, but do not write the final wave doc yet.
2. Create or update the working brief as discovery proceeds. Treat the brief as the current shared understanding, not as a private scratchpad.
3. Ask focused questions in small rounds. Prefer 3-5 high-leverage questions that affect scope, architecture, implementation, verification, or the first wave. For boundary-crossing decisions, provide informed options and a recommendation.
4. Consult the human on all material dimensions: intended users, user stories, must-have features, must-have requirements, non-goals, technical stack, data and persistence, auth and security, integrations, deployment and operations, UX workflow expectations, verification expectations, risks, and dependencies.
5. Maintain a concise must-have map in the working brief. Each must-have should map to one or more candidate waves, or be marked deferred/open.
6. Keep discovery centered on W1. The first wave must be buildable without guessing hard constraints; later waves need only enough detail to show where must-haves belong.
7. Ask for explicit human approval before finalizing the brief and translating it into the wave doc.
8. After approval, write the wave doc from the finalized brief. Choose the first active wave, defaulting W1 to a walking skeleton unless the human clearly needs a different first slice.
9. Write inactive waves as concise future direction: must-have stories, must-have features, and notes only.
10. Write the active wave with stable must-have IDs (`W<N>-MH<K>`), optional nice-to-have IDs when useful (`W<N>-NH<K>`), implementation notes, tasks, decisions needed, and verification.
11. Seed a compact Decisions section only with durable choices approved by the human or already established by the codebase.
12. Put deferred ideas and open questions in Notes.
13. If commits are permitted, commit material brief or wave-doc changes using the commit-message contract. If commit permission is unclear, ask before the first commit.

## Working Brief

The working brief should stay concise and reviewable. Include:

- Goal and intended users.
- User stories.
- Must-have features and must-have requirements.
- Must-have map: must-have, why it matters, addressed in, and notes.
- Non-goals.
- Technical stack and architectural constraints.
- Data, persistence, auth, security, integrations, deployment, and operations assumptions.
- UX and workflow expectations.
- Verification expectations.
- Risks, dependencies, open questions, and deferred ideas.

Do not force every section to be complete before moving forward. If an unknown does not block W1, record it under open questions, deferred ideas, Notes, or Decisions needed.

## Finalization Gate

The brief is ready to finalize when:

- The goal, intended users, and core user stories are clear.
- The concise must-have map exists and each must-have has a wave, deferred status, or open decision.
- W1 can be built without guessing hard constraints.
- Product scope, user-visible workflow assumptions, technical stack, persistence, auth/security, external services, deployment, and verification expectations are either approved or explicitly listed as decisions needed.
- The human has approved translating the brief into a wave doc.

## Judgment

Prefer fewer waves with clear intent over a long speculative roadmap. Three to five waves is usually enough.

The must-have map is the system vision layer. Keep it concise, but make it complete enough that the human and LLM can see what the system is becoming and which wave addresses each must-have.

Must-have requirements in the active wave should be testable and user-visible where possible. Avoid requirements that merely name components.

Assign stable IDs only when requirements are concrete enough to execute or audit. Active-wave must-haves must have IDs. Future inactive waves may stay as unnumbered stories/features until they become active.

Give the LLM freedom on local implementation details. Make it ask before changing product scope, data model, architecture, external services, auth/security behavior, pricing/billing behavior, or user-visible workflow assumptions.

Verification should be practical: relevant existing tests, focused new tests for important logic, and a demo path for the main user value.

Do not commit to a tech stack, persistence technology, or architectural approach in the brief or wave doc without the human's approval. If discovery does not settle them, list them under Decisions needed on the first active wave; do not quietly assert a choice.

## Decision Guidance

When asking about product scope, user-visible workflow, tech stack, architecture, data model, persistence, auth/security, integrations, deployment, or verification expectations, use the decision guidance contract.

For key technical choices, recommend the option most likely to be implemented reliably by a smart LLM in this repo. Favor convention density, local testability, reversibility, low dependency risk, clear security boundaries, manageable operations, and fit to W1 scope. Make assumptions explicit and say what becomes blocked if the decision is deferred.

## Do Not

- Do not create detailed tasks for inactive waves.
- Do not require formal acceptance criteria for every story.
- Do not create separate execution or audit reports.
- Do not skip the working brief and jump straight to the wave doc unless the user explicitly provides a finalized brief and asks for translation.
- Do not overfill Decisions with guesses.
- Do not make the wave doc longer than the project can justify.
- Do not leave more than one active wave.
- Do not renumber existing requirement IDs.
- Do not ask open-ended questions when credible options and a recommendation can be framed.
