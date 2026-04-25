---
name: advance
description: Use this skill when the active FBRA wave is ready to close and the user wants to move the project forward. It converts the active wave into a done summary that preserves stable must-have IDs, records shipped stories/features and durable decisions, recommends next-wave activation or material closeout choices when direction is not mechanical, then activates exactly one next wave. It commits wave-state changes when commits are permitted. Trigger on "advance the wave", "close W<N>", "mark this wave done", "move to the next wave", "activate W<N+1>", or "run advance". Do not use while must-have requirements are still unresolved unless the user explicitly accepts the gap.
---

# Advance

Close the active wave and activate the next one, recommending material closeout or next-wave choices before applying them when direction is not mechanical. Before advancing, read `references/fbra-schema.md`, `references/decision-guidance-contract.md`, and the wave doc. If commits are permitted or the wave doc will be committed, also read `references/commit-message-contract.md`.

## Purpose

Advance turns completed work into compact project memory and prepares the next active build scope. It should be mechanical when the wave is clearly done and the next wave is already agreed, but recommendation-backed when closeout reveals gaps, changed priority, new dependencies, or unresolved decisions.

## Inputs

- The FBRA wave doc.
- Current repo state.
- Build or Revise handoff.
- Human confirmation when there are unmet requirements or verification gaps.

## Output

- Updated wave doc:
  - Previous active wave becomes `done`.
  - One inactive wave becomes `active`, or a new active wave is created.
  - Remaining future waves stay `inactive`.
  - Decisions and Notes are updated.
  - The final doc has exactly one active wave unless the project is complete or deliberately paused.
- A docs commit for the wave-state transition when commits are permitted, or a prompt asking whether to commit it.

## Workflow

1. Confirm there is exactly one active wave and that it is ready:
   - Must-have requirements are implemented or explicitly dropped.
   - Verification passed or gaps are accepted by the human.
   - Important decisions are recorded.
2. Convert the active wave to `done`:
   - Summarize delivered capability.
   - List must-have IDs actually delivered.
   - List stories completed.
   - List features completed.
   - Include implementation commit references when useful and available.
   - Record decisions established.
   - Record follow-up notes.
   - Remove task-level detail unless it matters later.
3. Choose the next wave:
   - Prefer the next inactive wave if it still matches the goal.
   - Reorder only if learning made another wave more important.
   - Create a new wave only if needed.
4. Before applying material closeout or next-wave changes, present informed recommendations and get human approval when Advance would:
   - Reorder waves based on new learning.
   - Create a new active wave.
   - Move unfinished must-haves into the next wave.
   - Drop, defer, split, or supersede unmet must-haves.
   - Activate scope that introduces architecture, data model, auth/security, integration, deployment, billing, or user-visible workflow decisions.
   - Expand broad inactive-wave ideas into concrete active-wave requirements when multiple valid slices exist.
5. Expand exactly one next wave to `active`:
   - Add stable must-have IDs and requirements.
   - Add nice-to-haves if useful.
   - Add implementation notes.
   - Add tasks.
   - Add decisions needed.
   - Add verification.
   - If the new wave implies a boundary-crossing decision that has not been approved (e.g., a new service, dependency, or auth change), list it under Decisions needed using informed options and a recommendation. Do not encode unapproved choices as must-have requirements.
6. Keep other waves inactive and concise. Update their stories/features only if learning materially changed future direction.
7. Increment `wave_doc_version`, update `last_updated`, and set `current_wave`.
8. When commits are permitted, commit the wave-doc transition using the commit-message contract. If commit permission is unclear, ask before committing.

## Selecting The Next Wave

Pick the wave that most improves the product while reducing the most uncertainty. User value breaks ties.

Do not activate a broad cleanup wave unless cleanup is blocking product progress or verification.

If the next-wave choice is not obvious, recommend one path with tradeoffs rather than asking an open-ended question. Explain what can proceed if the decision is deferred and what should remain blocked.

## Handling Gaps

If a must-have requirement is not done, do not silently close the wave. Either:

- Keep the wave active.
- Move the requirement into the next active wave with human agreement.
- Drop it from scope with human agreement and record why.

If verification did not run, record the gap and ask before advancing unless the user already accepted it.

## Requirement Trace

Done-wave summaries should preserve the audit chain. List delivered must-have IDs, note deferred/dropped/superseded IDs, and include implementation commit references when they help future auditors understand how the wave was built.

## Decision Guidance

When activating the next wave exposes unresolved choices, use the decision guidance contract. Recommend the path that best preserves momentum, implementation reliability by a smart LLM, reversibility, and verification clarity. If the decision can be deferred, say exactly what can proceed and what should remain blocked.

Human approval is required before applying material direction changes during Advance. Routine closeout of completed, verified, already-agreed scope can proceed without a decision prompt.

## Handoff

After advance, send a short message with these slots:

- **Closed**: W<N> delivered capability plus must-haves actually shipped.
- **Deferred or dropped**: with a one-line reason each.
- **Activated**: W<N+1> goal plus the first concrete next step.
- **Committed**: wave-doc transition commit hash and subject, or `Not committed` with the reason.

Be terse when things went as expected. Flag any unresolved must-have the human accepted as a gap.

## Do Not

- Do not activate more than one wave.
- Do not add detailed tasks to inactive waves.
- Do not preserve noisy task history in done waves.
- Do not hide unfinished must-have requirements in follow-up notes.
- Do not renumber requirement IDs during closeout or next-wave activation.
- Do not activate a wave with an unframed boundary-crossing decision.
