---
name: revise
description: Use this skill after or during Build when the user wants to review results, reconcile surprises, adjust the active wave, or decide what to do about incomplete work. It compares the active wave's must-have requirements to the actual implementation and verification results, then updates the active wave or records decisions without closing the wave. Trigger on "revise the wave", "review what changed", "update the active wave", "handle these build findings", "the plan changed", or "what remains before done". Do not use to close a wave and activate the next one; use advance.
---

# Revise

Review the active wave against reality and update the plan while the wave remains active. Before revising, read `references/fbra-schema.md` and the wave doc.

## Purpose

Revise keeps the active wave honest when Build surfaces surprises, incomplete verification, changed scope, or human feedback.

## Inputs

- The FBRA wave doc.
- Current repo state.
- Build handoff, test results, user feedback, or observed gaps.

## Output

- Updated active-wave section if needed.
- Updated Decisions or Notes if durable learning surfaced.
- Concise summary of what changed in the plan and what remains.

## Workflow

1. Read the active wave's must-have requirements and verification section.
2. Compare each must-have requirement against actual implementation and verification.
3. Classify gaps:
   - Still required: keep or add a task.
   - No longer required: remove or move to Notes with a short rationale.
   - Needs human decision: add to Decisions needed.
   - Nice-to-have: move out of must-have scope.
4. Update implementation notes if the codebase taught the LLM something future work should respect.
5. Add durable choices to Decisions.
6. Add deferred ideas or unresolved questions to Notes.
7. Leave the wave `active` unless the user explicitly asks to advance and it is ready.

## What To Preserve

Keep must-have requirements stable unless the human changes scope or the build shows they are wrong. If a requirement changes, make the reason visible in a short note.

Keep the doc concise. Revise is not an audit report; it is a plan correction.

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
