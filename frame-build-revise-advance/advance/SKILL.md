---
name: advance
description: Use this skill when the active FBRA wave is ready to close and the user wants to move the project forward. It converts the active wave into a done summary, records shipped stories/features and durable decisions, chooses or creates the next active wave, and keeps remaining waves inactive and concise. Trigger on "advance the wave", "close W<N>", "mark this wave done", "move to the next wave", "activate W<N+1>", or "run advance". Do not use while must-have requirements are still unresolved unless the user explicitly accepts the gap.
---

# Advance

Close the active wave and activate the next one. Before advancing, read `references/fbra-schema.md` and the wave doc.

## Purpose

Advance turns completed work into compact project memory and prepares the next active build scope.

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

## Workflow

1. Confirm there is exactly one active wave and that it is ready:
   - Must-have requirements are implemented or explicitly dropped.
   - Verification passed or gaps are accepted by the human.
   - Important decisions are recorded.
2. Convert the active wave to `done`:
   - Summarize delivered capability.
   - List stories completed.
   - List features completed.
   - Record decisions established.
   - Record follow-up notes.
   - Remove task-level detail unless it matters later.
3. Choose the next wave:
   - Prefer the next inactive wave if it still matches the goal.
   - Reorder only if learning made another wave more important.
   - Create a new wave only if needed.
4. Expand exactly one next wave to `active`:
   - Add must-have requirements.
   - Add nice-to-haves if useful.
   - Add implementation notes.
   - Add tasks.
   - Add decisions needed.
   - Add verification.
   - If the new wave implies a boundary-crossing decision that has not been approved (e.g., a new service, dependency, or auth change), list it under Decisions needed. Do not encode unapproved choices as must-have requirements.
5. Keep other waves inactive and concise. Update their stories/features only if learning materially changed future direction.
6. Increment `wave_doc_version`, update `last_updated`, and set `current_wave`.

## Selecting The Next Wave

Pick the wave that most improves the product while reducing the most uncertainty. User value breaks ties.

Do not activate a broad cleanup wave unless cleanup is blocking product progress or verification.

## Handling Gaps

If a must-have requirement is not done, do not silently close the wave. Either:

- Keep the wave active.
- Move the requirement into the next active wave with human agreement.
- Drop it from scope with human agreement and record why.

If verification did not run, record the gap and ask before advancing unless the user already accepted it.

## Handoff

After advance, send a short message with these slots:

- **Closed**: W<N> delivered capability plus must-haves actually shipped.
- **Deferred or dropped**: with a one-line reason each.
- **Activated**: W<N+1> goal plus the first concrete next step.

Be terse when things went as expected. Flag any unresolved must-have the human accepted as a gap.

## Do Not

- Do not activate more than one wave.
- Do not add detailed tasks to inactive waves.
- Do not preserve noisy task history in done waves.
- Do not hide unfinished must-have requirements in follow-up notes.
