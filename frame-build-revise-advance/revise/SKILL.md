---
name: revise
description: Use this skill after or during Build when the user wants to review results, reconcile surprises, adjust the active wave, or decide what to do about incomplete work. It compares the active wave's must-have requirements to the actual implementation and verification results, preserves stable requirement IDs while updating the active wave or recording decisions, and commits material plan corrections when commits are permitted. Trigger on "revise the wave", "review what changed", "update the active wave", "handle these build findings", "the plan changed", or "what remains before done". Do not use to close a wave and activate the next one; use advance.
---

# Revise

Review the active wave against reality and update the plan while the wave remains active. Before revising, read `references/fbra-schema.md`, `references/decision-guidance-contract.md`, and the wave doc. If commits are permitted or material wave-doc history is involved, also read `references/commit-message-contract.md`.

## Purpose

Revise keeps the active wave honest when Build surfaces surprises, incomplete verification, changed scope, or human feedback.

## Inputs

- The FBRA wave doc.
- Current repo state.
- Build handoff, test results, user feedback, or observed gaps.

## Output

- Updated active-wave section if needed.
- Updated Decisions or Notes if durable learning surfaced.
- Docs or fix commits for material revisions when commits are permitted.
- Concise summary of what changed in the plan and what remains, using the same handoff slots as build (Changes, Verified, Not verified, Assumptions, Needs decision, Approved decisions) so the human reads the same shape across phases.

## Workflow

1. Read the active wave's stable must-have IDs, requirements, and verification section.
2. Compare each must-have requirement against actual implementation and verification.
3. Classify gaps:
   - Still required: keep or add a task.
   - No longer required: remove or move to Notes with a short rationale.
   - Needs human decision: add to Decisions needed using informed options and a recommendation.
   - Nice-to-have: move out of must-have scope.
4. Update implementation notes if the codebase taught the LLM something future work should respect.
5. Add durable choices to Decisions.
6. Add deferred ideas or unresolved questions to Notes.
7. Preserve existing requirement IDs. If a requirement is split, dropped, deferred, or superseded, make that explicit instead of silently deleting or renumbering it.
8. Leave the wave `active` unless the user explicitly asks to advance and it is ready.
9. When commits are permitted, commit material wave-doc revisions and related code fixes using the commit-message contract. If commit permission is unclear, ask before the first commit.

## What To Preserve

Keep must-have requirements stable unless the human changes scope or the build shows they are wrong. If a requirement changes, make the reason visible in a short note.

Keep the doc concise. Revise is not an audit report; it is a plan correction.

Requirement IDs are audit handles. Preserve them even when the text changes, and create new IDs for split-out requirements. Do not renumber IDs for neatness.

Commit requirement-doc revisions separately from code corrections when practical. A `fix` commit should reference the original must-have ID and the verification failure or human feedback that caused the revision.

## Decision Guidance

When build findings reveal a decision, use the decision guidance contract. Explain why the original plan no longer fits, which must-have IDs or verification gaps are affected, what can proceed if the decision is deferred, and which option best fits implementation by a smart LLM in the current codebase.

## Readiness Check

A wave is ready for Advance when:

- All must-have requirements are implemented or explicitly dropped by the human.
- Verification has passed, or gaps are clearly accepted.
- Important decisions are recorded.
- Remaining work is either out of scope, deferred, or assigned to a future inactive wave.

## Do Not

- Do not close the wave; Advance does that.
- Do not rewrite inactive waves in detail.
- Do not create a separate report unless the user asks.
- Do not bury an unmet must-have as a follow-up without human agreement.
- Do not delete, reuse, or renumber requirement IDs to hide scope churn.
- Do not turn a failed or ambiguous requirement into an open-ended human question without options and a recommendation.
