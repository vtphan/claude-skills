# Journey Mapper: Example Interaction

This file shows a Journey Mapper pass on the homework system, drafting the "completing a homework assignment" journey for the student persona Maya. It exists to calibrate the skill — what good stage construction looks like, where friction lives, how insights earn their place.

## Input

Accepted Seed, Context (with Maya as a `medium`-confidence student persona), and Goal (first-pilot-infrastructure scoped to one assignment with full event capture).

User invokes Journey Mapper for the anchor journey "Completing a homework assignment."

## Output

### Part 1: The Journey document

```markdown
---
id: journey-completing-assignment
title: Completing a homework assignment
seed_ref: seed
context_ref: context
goal_ref: goal-first-pilot
persona_refs: [persona-maya]
status: draft
---

# Journey: Completing a homework assignment

## Decision points

1. I drafted seven stages. The "abandons-and-switches" stage is the most consequential for design and is `assumed` — does this pattern match what you've observed in your section?
2. The insight "students often switch problems and return with fresh eyes" is load-bearing for the multi-problem layout decision. Confirm or push back.
3. I tagged the emotional content as `assumed` throughout, even where the behavior is `observed`. Adjust if your observation extends to internal states.
4. The cross-persona moment with the instructor is conditional on stuck-detection existing — which it doesn't in the current Goal. The Journey describes the future experience; flag if you'd rather scope it to current Goal only.
5. I omitted "asks classmate for help" as a stage because the Seed and Context don't address peer interaction. If this is a real and important part of the experience, the Seed may need updating.

## Scenario

Maya is a first-year student in the algorithms course. It's Tuesday evening, two days before a homework assignment is due. She has three recursion problems to solve. She's done some of the prior assignments comfortably and struggled on others. She's working alone in her dorm, on her laptop, with about 90 minutes available before she wants to sleep. The assignment matters for her grade, but she's not yet panicked about it.

## Stages

### stage-orienting: Orienting

*source: observed*  *confidence: medium*

- **User actions:** Opens the homework system, sees three problems on the assignment, reads each one briefly, picks the one that looks most tractable.
- **User thoughts and feelings:** Mild anxiety about scope. Looking for a foothold. Wants to start with something that gives a quick win.
- **Friction:** Hard to tell which problem is actually easiest from the prompt alone. May misjudge which to start with.
- **System touchpoints:** Assignment list view; problem prompts.

### stage-first-attempt: First attempt

*source: observed*  *confidence: medium*

- **User actions:** Reads the chosen problem more carefully. Thinks for a few minutes about the approach. Writes a first version of the code. Runs it against the test cases.
- **User thoughts and feelings:** Active engagement; the kind of focus that comes from confident effort. Often in flow.
- **Friction:** Initial approach may have a flaw the test cases catch. Test failure messages may be unhelpful.
- **System touchpoints:** Code editor; test runner; test results.

### stage-iterating: Iterating

*source: observed*  *confidence: medium*

- **User actions:** Edits the code, runs again, looks at which tests fail. Tries variations. Adds print statements. Runs again.
- **User thoughts and feelings:** Engagement narrows. If progress is happening, focus deepens. If progress isn't happening, frustration begins to leak in.
- **Friction:** Several attempts may fail in similar ways without revealing why. Print-statement debugging is slow. Hard to know whether to keep trying or change approach.
- **System touchpoints:** Editor; test runner; output.

### stage-stuck: Stuck

*source: observed*  *confidence: medium*

- **User actions:** Stops actively typing. Stares at the screen. Re-reads the problem. May open a browser tab and consider searching, then close it. May text a classmate, then not send.
- **User thoughts and feelings:** Frustration crystallizing into self-doubt. "Is everyone else finding this easy?" Reluctance to ask for help — social cost feels real even when no one's watching. Uncertainty about whether to push harder or change strategy.
- **Friction:** No external signal about whether her struggle is normal. No low-cost way to externalize her thinking. Help options (asking classmate, asking instructor, searching online) all carry costs she'd rather not pay this late at night.
- **System touchpoints:** None — the stuck stage is largely invisible to the system unless the system specifically observes idle time and lack of progress.

### stage-abandons-and-switches: Abandons and switches

*source: assumed*  *confidence: medium*

- **User actions:** Closes the current problem (mentally or by switching tabs/files). Picks up one of the other two problems. Starts on it.
- **User thoughts and feelings:** Relief at the change. Maybe a little guilty about giving up. Sometimes a feeling that progress on a different problem will give her a path back.
- **Friction:** State on the abandoned problem must be preserved (autosave); switching context is cognitively expensive; she may forget what she was thinking when she returns.
- **System touchpoints:** Autosave; the multi-problem assignment layout; problem-switching mechanics.

### stage-returning-with-fresh-eyes: Returning with fresh eyes

*source: assumed*  *confidence: medium*

- **User actions:** After progress on the second problem (or after a break), returns to the first problem. Re-reads it. Often spots the bug or the misunderstanding within minutes.
- **User thoughts and feelings:** Relief and a small surge of confidence. The "aha" moment. Sometimes embarrassment at how obvious the fix was.
- **Friction:** Returning to a half-finished mental state requires reconstructing context. Lost or unclear autosave state would be devastating here.
- **System touchpoints:** The recovered editor state; the test runner.

### stage-completing-and-submitting: Completing and submitting

*source: observed*  *confidence: medium*

- **User actions:** Fixes the code, runs the tests, sees them pass, submits.
- **User thoughts and feelings:** Satisfaction. Closure. Brief pride. Then onward to the next problem.
- **Friction:** Anxiety between hitting submit and seeing confirmation; ambiguity about whether the submission registered.
- **System touchpoints:** Submission confirmation; assignment status update.

## Key insights

- *source: assumed* **Switching between problems is part of the work, not a failure of focus.** Many students productively use the multi-problem structure to escape stuck moments and return with fresh eyes. Design that assumes deep linear focus on one problem at a time would miss this. The system should make switching cheap and returning cheaper still.
- *source: assumed* **The stuck stage is the most pedagogically important and the least visible to the system.** When Maya is stuck, the system sees idle time at most. The richness of her cognitive state — re-reading, considering help, opting against — is invisible. Designing instrumentation to capture some of this signal is high-leverage.
- *source: observed* **Help-seeking has a social cost even when no one is watching.** The reluctance to ask a classmate or instructor is real even in private. This shapes what kind of support is most likely to be used: the lowest-friction option, ideally the one that doesn't feel like asking for help.
- *source: observed* **Autosave reliability is load-bearing for the productive-switching pattern.** If switching problems risks losing work, the productive-switch pattern collapses into "students avoid switching." This is a small system-design decision with outsized pedagogical consequences.
- *source: assumed* **The submission moment is anxious despite seeming routine.** The brief gap between submitting and seeing confirmation is when Maya has the least information and the most stake. Confirmation latency and clarity matter more than the surface area of the feature suggests.

## Cross-persona moments

- **Stuck-detection signal to instructor:** The stuck stage is invisible to Maya's instructor unless the system specifically detects it and surfaces it. This is a cross-persona moment that the current Goal does not address (no dashboard, no stuck-score), but the Journey records that the moment exists for future iterations.
- **Behavioral signal to researcher:** The full event sequence — including the stuck stage's idle and tab-switching behavior — is captured for later analysis by Ana. This is a cross-persona moment present in the current Goal: the export pipeline exists.

## Change log

- 2026-04-27: Initial draft.
```

### Part 2: Summary

- Drafted seven stages reflecting the emotional and cognitive arc of an evening homework session, not just functional steps. The "stuck" and "abandons-and-switches" stages do the most design-relevant work.
- Five key insights, three of which are load-bearing: switching as productive behavior, the invisibility of stuck moments, and autosave reliability as pedagogically consequential. These should drive design decisions in this and future iterations.
- Two cross-persona moments noted: stuck-detection (not addressed in current Goal but visible in the Journey for future iterations), and behavioral export to researcher (addressed in current Goal).
- Source tags lean `assumed` for emotional content even where behavior is `observed`. The user's teaching observation grounds the stages but not necessarily the internal states; flagged in decision points for the user to upgrade where appropriate.
- One thing I held back from including: a "asks classmate for help" stage. The Seed and Context don't address peer interaction, and adding it speculatively would expand scope. Flagged in decision points so the user can decide whether the Seed should be updated.

---

## What this example illustrates

A few things worth noticing:

**Stages are emotional, not just functional.** "Stuck" and "abandons-and-switches" capture cognitive transitions, not task transitions. This is what makes the Journey useful for design rather than just descriptive.

**Friction is surfaced everywhere.** Every stage has friction content. Even the "completing and submitting" stage names the brief anxiety between submit and confirmation — a small thing that's nonetheless real.

**The stuck stage gets special attention.** It's the longest, most detailed stage, with the most friction and the most insight to mine. This reflects the fact that stuck moments are pedagogically the most important in homework.

**Insights are specific and actionable.** Each one drives at least one design decision: multi-problem layout matters, capturing stuck-stage signal is high-leverage, autosave reliability is non-negotiable, confirmation latency matters more than expected.

**Cross-persona moments are flagged even when not in current Goal.** The instructor stuck-detection moment is real for the journey even though the current Goal doesn't address it. The Journey records future-relevant moments alongside currently-addressed ones.

**Source tags are honest.** The behavioral content is `observed` (the instructor has seen students do this); the emotional content is `assumed` (he hasn't observed their internal states directly). Don't conflate observation of action with observation of feeling.

## Counter-example: textbook journey

For contrast, here's what an under-calibrated Journey looks like:

> ### stage-1: Read problem
>
> - **Actions:** Reads the problem.
> - **Thoughts:** Thinks about the problem.
> - **Friction:** May not understand.
>
> ### stage-2: Write code
>
> - **Actions:** Writes code.
> - **Thoughts:** Thinks about the code.
> - **Friction:** Code may not work.

This is descriptive but not insightful. It captures functional steps without the emotional or cognitive content that makes Journey work valuable. There's no design that follows from it.

The fix: ask "what's specific to this persona in this scenario?" at every stage. If the answer is "nothing — anyone reading a problem reads a problem," the stage is too abstract to do work.

## Counter-example: prescriptive journey

> ### stage-stuck: Stuck
>
> - **Actions:** Click the "I'm stuck" button.
> - **Thoughts:** Wants help.
> - **Friction:** Hint system needs to be available.

This is wrong because it describes the system's response, not the user's experience. The Journey should be agnostic to what the system does — it captures what the user experiences, and Stories downstream decide how the system responds.

The fix: write Journeys as if the system might not exist. What does the user do, think, and feel? The system shows up in "system touchpoints" but doesn't drive the narrative.
