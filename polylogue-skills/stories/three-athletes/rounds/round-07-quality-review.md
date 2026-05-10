# Round 7 — Quality Review

**Date:** 2026-05-09.
**Story:** *The Saturday Field* (slug: `three-athletes`).
**Reviewer:** acting as Reviewer/Editor against DECISIONS.md and `skills-reference.md`.

## Summary

| Check | Status |
|---|---|
| Elimination — Ch1 comp ("scoping out") | WARN |
| Elimination — Ch2 gate (single-detail inferencing) | PASS |
| Elimination — Ch3 comp ("select team") | PASS |
| Elimination — Ch3 gate (multi-detail inferencing) | PASS |
| Fork legitimacy (Ch4) | PASS |
| Ending diff (5a / 5b / 5c) | PASS |
| Runtime fit | WARN (15.5 min vs 15 target — within 10% tolerance) |
| Bible sync | WARN (some inline character descriptions abbreviated) |
| **Renderer-facing self-containment** | **FAIL** (4 violations) |
| Schema validity / DAG | PASS |
| Position distribution (A/B/C across challenges) | PASS (1/2/1; Ch3 comp+gate at different positions) |
| Staging-pedagogy | PASS |

## Renderer-facing FAIL — specific violations

1. **Chapter 4 Page 3**: cross-page reference. "Coach Reyna, mid-30s: same description as Page 1." The renderer has no Page 1; descriptions must repeat verbatim.

2. **Chapter 4 Page 3**: meta-commentary inside `[Page staging]`. The bold-printed line *"Critical: this panel must give all three approachable paths roughly equal visual weight (per staging-pedagogy finding for forks)"* is instruction to a future reviewer, not to the renderer.

3. **Chapter 4 Page 3**: negative-form instructions. *"No dramatic lighting on Minh (no rescue framing); no isolating composition on Reuben (no team-up framing); no centering effect that says 'Ines should stay still.'"* The renderer can't render the absence of things relative to alternatives it doesn't know. Must be rewritten as positive specifications.

4. **Chapter 5c Page 1**: cross-chapter comparative. *"His shoulders visibly more relaxed than at the start of Chapter 4."* The renderer has no "start of Chapter 4" baseline; absolute visual state required.

**All four fixes applied in this pass** (see "Fixes applied" below).

## WARN-class items (not blocking)

**Runtime fit (15.5 min vs 15 target).** Within the 10% tolerance window. Could trim by dropping a page (most likely candidate: Chapter 1 Page 1, the arrival beat — folding its dialogue into Page 2). Not blocking for v1.

**Bible sync.** Some chapter prompts have slightly abbreviated physical descriptions (e.g., dropping the eyebrow scar in some Minh references, condensing Coach Reyna's description). The renderer rules say repetition of the bible verbatim is what gives image generation a chance at face/outfit consistency. A pass through to restore verbatim bible text everywhere character descriptions appear would tighten this. Not blocking; image consistency matters most when renders exist.

**Elimination check, Ch1 comp ("scoping out").** Wrong (A) "telescope" is dramatic and unlikely; wrong (C) "examining each kid carefully up close" is plausible-but-narrow. A student who didn't use the skill might still elimination-guess (B) by recognizing (A) as too dramatic. Comp checks are formative and lower stakes, so this is a soft warning. Could sharpen the wrongs in a v2 pass.

## PASS-class checks — brief notes

**Elimination check, Ch2 gate.** Wrongs encode real misconceptions: surface-reading takes Minh's spoken word ("just tired") at face value; wrong-direction reads the social distance as conflict with the coach. The correct answer requires using the staged evidence (phone moment + missed connection + body language that doesn't read as exhaustion). Group bar holds.

**Elimination check, Ch3 gate.** Multi-detail inference combining Chapters 2 and 3 evidence. Wrong (A) reads only Chapter 3; wrong (C) imports a non-soccer frame. The correct answer uniquely combines orange jersey + select-team / tryout overheard + Chapter 2 phone-and-deflection.

**Fork legitimacy.** Each of (A) team approach, (B) direct ask, (C) patient presence is a defensible perspective with real cost and real gift. None is more virtuous than the others. A thoughtful person valuing each corresponding perspective would defend their choice.

**Ending diff.** Distinct fates (changed / quieter / more bonded), moods (tense honest / patient settled / warm collective), and lessons (truth has cost / presence is its own answer / you don't have to carry hard things alone). Not reskins.

**Schema / DAG.** Exactly one perspective_fork (Ch4). `endings.length` = 3 = number of correct choices in fork. All `next_chapter_id` references resolve (A→05c, B→05a, C→05b).

**Position distribution.** Across the four challenges with correct positions: B, A, C, B. A=1, B=2, C=1. Each position used at least once. Within Chapter 3 (the only chapter with both comp check and gate), the comp check is at C and the gate is at B — different positions.

**Staging-pedagogy.** Each gate's evidence is visibly staged in panels (Ch2 phone-check on Page 2; Ch3 orange jersey on Page 1, fence overhearing on Page 2); the fork's three paths are spatially balanced in Ch4 Page 3 (after fix). No camera editorializing on Minh's emotional state in Ch2.

## Operational findings worth recording

Two observations from running this review for the first time, worth folding into DECISIONS.md as v1 stress-test findings:

**1. Renderer-facing violations are easy to commit during enthusiastic drafting.** Phrases like *"more relaxed than at the start of Chapter 4"* feel natural in prose but break the renderer's self-containment. When the Reviewer/Editor agent spec is updated, the renderer-facing-self-containment check should explicitly include grep-style scans for cross-chapter/cross-page/comparative-to-baseline phrasings.

**2. Meta-commentary creep inside `[Page staging]`.** Even authoring with the staging-pedagogy finding actively in mind, I wrote *"Critical: this panel must give all three approachable paths roughly equal visual weight"* directly inside the prompt — instruction to a future reviewer, not to the image generator. The check should specifically scan for bold-printed editorial inside `[Page staging]`.

These are concrete, mechanical checks the Reviewer/Editor can apply.

## Fixes applied (this pass)

- **Ch4 Page 3 character descriptions**: Coach Reyna line replaced with full description verbatim from bible.
- **Ch4 Page 3 [Page staging]**: removed bold meta-commentary; rewrote negative instructions as positive specifications (explicit "daylight-ordinary throughout, three figures composed at comparable visual weight").
- **Ch5c Page 1 [Page staging]**: replaced comparative-to-baseline with absolute visual state ("shoulders dropped and back nearly straight").

## Recommendations going forward

- Apply the bible-sync pass when image renders are about to be generated (closer to actual production).
- Trim Ch1 Page 1 if runtime needs to come down further; not necessary for v1 unless time budget is being enforced strictly.
- Capture the two operational findings above in DECISIONS.md as v1 stress-test findings (Reviewer/Editor mechanical checks).
- Story is otherwise ready for Round 8 export — pending schema update per the v1 implementation order in DECISIONS.md Section 12.
