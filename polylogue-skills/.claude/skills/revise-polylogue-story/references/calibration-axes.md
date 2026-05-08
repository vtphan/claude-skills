# The Two Calibration Axes — Detail

This file is the deep-dive reference for the two axes the skill operates on: reading level and skill visibility. SKILL.md describes the operational mechanics in Phase 2; load this file when an unusual case requires the deeper rationale (especially for shifts that hit asymmetric constraints).

## Reading-level shift

**What changes:** narration prose, dialogue word choice, decision prompt language, hint text, debrief lens prose.

**What stays:** characters, locked art style, perspective fork, chapter structure, targeted skills, misconception annotations, decision *meanings* (a wrong choice still targets the same misconception; only its language adjusts).

**Mechanics:** the Instructional Designer sub-agent runs at the new grade level on every page. The runtime estimator recomputes with the new coefficient (35/30/25 s/page for grades 5/6/7). The bible and art style are not affected.

**Asymmetric notes:** shifting *up* (e.g., grade 5 → grade 7) is generally safer than shifting *down*. Shifting down may require simplifying perspective tradeoffs themselves — not just words — and at sufficient distance becomes re-authoring. The skill should refuse a grade-7 → grade-5 shift if the targeted skill's complexity would not survive the simplification, and surface this to the teacher: "This story's perspective tradeoffs are calibrated to grade 7. Shifting to grade 5 would require simplifying the perspectives themselves, which is closer to re-authoring than calibration. Want me to shift to grade 6 instead, or do you want me to flag this and try anyway?"

## Skill visibility shift

**What changes:** misconception-targeted wrong choice language, hint specificity, per-chapter debrief lens phrasing, fork debrief lens phrasing, narrative cues for skill-relevant moments.

**What stays:** the targeted skill at every gate, the fork's structure and skill-target, the elimination check passing on every decision (hard floor), the fork legitimacy on every fork branch, the misconception annotations themselves (the names; the language realizing them shifts).

**Hint-naming tension.** Making a hint name the cognitive operation explicitly ("*Reading between the lines* means letting the off-topic evidence count…") increases pedagogical clarity but risks doing the work students should be doing for themselves at the moment of attempt-2. When the diagnostic proposes hint-naming as a visibility-up move, surface the tradeoff in the example presentation so the operator (and through them the teacher) decides — do not default the skill toward naming.

**Asymmetric constraints:**

- *More visible* has a soft ceiling: heavy-handedness. The skill should self-flag when amplification crosses into stories that narrate their own pedagogy at students. Pull back if so.
- *Less visible* has a hard floor: the elimination check. If softening a wrong choice makes the decision guessable, the skill must not commit the change for that chapter. Partial application is acceptable; chapter-by-chapter floor enforcement is mandatory.

**Mechanics:** the Instructional Designer adjusts decision-related language; the Reviewer/Editor runs the elimination check on every adjusted decision before commit; the fork uses the fork-legitimacy check instead.
