# Sample revision session — *Three Versions of Tuesday*

A fully-worked Phase 1 brainstorm illustrating what good opportunity-surfacing and one loop iteration look like for a real library story. This document is bundled with the skill as a few-shot reference for the Instructional Designer's diagnostic mode and the Reviewer/Editor's example-polishing. It is not loaded by the runtime as a working session; it is illustrative only.

The story under revision is `polylogue-stories/middle-school-friendship/`, exported as `story.json` v1.0.0, currently calibrated at grade 5, visibility *as authored*.

---

## Operator request (Round 0 of the session)

> Hey — I'm working with a 6th-grade ELA teacher (Ms. Rivera, third period, 24 students). She wants to use *Three Versions of Tuesday* next month but says it's pitched a year young for her kids on the language, and she's also worried they'll cruise past the lesson because the chapters are subtle — her class has been doing perspective-taking work all semester and she wants the thinking moves to land harder. So: grade 6, more visible. Walk the story and bring me opportunities I can take to her.

---

## Diagnostic pass

The skill loads `polylogue.md`, `story.json`, every `chapters/chapter-NN.md`, and `thinking-skills.md`. It builds the internal model:

- 5 spine chapters + 3 endings; one perspective fork at chapter 5 (3-correct, no failure mode); skill ladder is *Recognizing point of view* → *Reading between the lines* → *Considering multiple viewpoints*.
- Currently grade 5; reading-level coefficient 35 s/page; estimated runtime 23:32 median, 23:55 worst case (ending C path); 24-min budget.
- Two `metadata.author_overrides` already recorded (bible-sync compression, ending-node addressing).
- Existing evaluation report at `polylogue-stories/middle-school-friendship/evaluation-report.md` flags decision-label length and debrief vocabulary as the two highest-leverage grade-band issues.

The Instructional Designer runs the diagnostic on both axes.

### Reading level (target: grade 6)

| Location | Finding |
|---|---|
| ch02 correct (b), ch04 correct (a), ch04 wrongs (b) (c) | Decision labels run 35–47 words. At grade 6 a student scanning three options is reading 100+ words before answering — this is the highest-load surface in the story. |
| ch05 fork debriefs and overall `perspective_contrast` | Adult-register vocabulary: *covenant*, *transactional*, *forecloses*, *vulnerability*, *spontaneity*. The 6th-grade band can carry *promise / agreement*, *pact*, *like a contract*, *closes off*, *openness* — the substance survives. |
| ch04 page 2 narration (88 words) | Pushes the cognitive-load ceiling for one comic page. Splittable across two narration beats without restaging. |
| ch01–ch03 in-chapter narration | Already grade-6-comfortable; sentence length averages 8–11 words; vocabulary mostly tier-1/2. **No-op territory** — flag as already calibrated. |
| Hint text (all 4 gates) | Already at grade-6 reading level; no shifts needed for reading level alone. |

### Skill visibility (direction: more visible)

| Location | Finding |
|---|---|
| Per-chapter debrief lenses (all 5 chapters, all 12 choices) | Lenses are story-grounded ("Names what each person is doing in the present moment"). The named cognitive operation — *recognizing point of view*, *reading between the lines*, *considering multiple viewpoints* — appears nowhere in the lens text. **High headroom for naming**. |
| Hints (ch01, ch02, ch03, ch04) | All four hints reframe-style. None lead with or contain the named cognitive operation. Visibility-up could prepend a one-line operation name. |
| ch05 fork debrief (3 branches) | The capstone naming moment. The fork is the story's primary perspective-taking decision and is currently the most pedagogically-implicit decision in the spine — the lenses describe philosophies in story terms ("a covenant against any single person rewriting the past") without invoking *considering multiple viewpoints* by name. **Highest-headroom location in the story for visibility-up.** |
| ch01 wrong (a) and ch04 wrong (b) | Misconception pulls already at strong intensity (collapsing in-the-moment behavior into character traits — sharp, plausible). **No-op for visibility-up** — they cannot get sharper without becoming caricatures. |
| ch02 wrong (c), ch03 wrong (c) | Pulls already at strong intensity; ch03 wrong (c) (jealousy/sabotage) is borderline cartoonish at the upper end. **No-op for visibility-up.** |
| `metadata.perspective_taking_topic` | Currently a one-liner. Visibility-up could thicken — but this is a metadata field the student never sees, so out-of-scope unless the operator surfaces a specific reason. |

The diagnostic concludes: meaningful headroom on both axes, with the 5 fork debriefs as the single highest-leverage location and the per-chapter lens text as the broadest. Reading-level work concentrates in decision labels and debrief vocabulary; in-chapter narration is mostly already at the new band.

---

## Themes presented to the operator (first iteration)

> **Three Versions of Tuesday** — currently grade 5, runs ~24 minutes, teaches *considering multiple viewpoints* with two scaffolding skills (recognizing point of view, reading between the lines).
>
> I read it through against grade 6 and "more visible." Five things stood out. I'm going to show one or two before/after examples per theme — react to the examples, not the abstractions, and tell me which of these matter for Ms. Rivera's class.

### Theme 1 — Decision labels run long for a grade-6 scan

The chapter-end labels are where the language load piles up. A 6th grader reading three options at chapter 4 is parsing 110 words before they can answer. Tightening them to ≤25 words each preserves the misconception pulls and recovers parseability.

> **ch02 correct (b)** — currently:
> > It tells you for sure that Priya was mid-sentence, that Oz did the impression, and that Priya stood up and left. It tells you about Priya that she felt cut off, read Tasha's laugh as siding-with, and walked out before checking. *(47 words)*
>
> Could become:
> > Priya's frame guarantees what happened — the joke, the laugh, the standing-up. It only tells you about Priya that she felt cut off and read Tasha's laugh as taking sides. *(30 words)*

> **ch04 correct (a)** — currently:
> > She noticed Oz's cowlick was more sprung than usual. That tells you he was tense before he sat down — so the joke was a tense person making a tense joke. It came out wrong because he was already wound up. *(42 words)*
>
> Could become:
> > She noticed the cowlick more sprung than usual. That tells you Oz arrived tense — the joke was a tense person making a tense joke, not a reaction to Priya. *(29 words)*

The misconception pulls in (a)/(c) on each gate stay sharp; only the parseable surface shrinks.

### Theme 2 — Adult vocabulary in the debrief language

The fork branch debriefs and the overall `perspective_contrast` block use words pitched at adults: *covenant*, *transactional*, *forecloses*, *vulnerability*, *spontaneity*. The substance is right — the words can come down without losing the trade-off shape.

> **ch05 fork (a) debrief lens** — currently:
> > This perspective puts shared, written truth above ongoing repair — a covenant against any single person rewriting the past. It buys clarity. It costs spontaneity.
>
> Could become:
> > This perspective puts shared written truth above quick repair — a promise against any one person rewriting what happened. It buys clarity. It costs the freedom to just be in the moment.

> **ch05 fork (c) debrief lens** — currently:
> > This perspective holds the perspectives themselves as the truth, and trades after-the-fact repair for in-the-moment vulnerability. It buys depth. It costs comfort.
>
> Could become:
> > This perspective treats all three versions as the truth, and trades fixing things later for being honest in the moment. It buys depth. It costs comfort.

The trade-off shape ("buys X, costs Y") is preserved on every branch.

### Theme 3 — Per-chapter debrief lenses don't name the cognitive move

The current lenses describe what the choice meant in story terms — "names what each person is *doing* in the present moment" — without invoking the named skill from `thinking-skills.md`. For Ms. Rivera's class, that's the largest visibility-up surface in the story: every gate can name the operation explicitly in the post-decision lens, so the cognitive move the chapter just exercised is on the page when groups deliberate.

> **ch01 correct (b) debrief lens** — currently:
> > Names what each person is *doing* in the present moment, separated from who they generally are.
>
> More-visible:
> > Names what each person is *doing* in the present moment, separated from who they generally are. That separation — present-tense action vs. character label — is what *recognizing point of view* is built on.

> **ch03 correct (b) debrief lens** — currently:
> > Names the inference: a hidden hurt, a deflection that protects Oz more than Tasha, and the word *rescue* doing concealment work.
>
> More-visible:
> > Names the inference: a hidden hurt, a deflection that protects Oz more than Tasha, and the word *rescue* doing concealment work. *Reading between the lines* is exactly this — letting the evidence the surface tries to hide do the work.

The operation gets named once, at the moment the group has just done it. Elimination check is unaffected — these are post-answer lenses, not choice labels.

### Theme 4 — Hints could lead with the named operation

The hint after attempt 1 currently reframes the question with concrete cues but doesn't invoke the named skill. Visibility-up could lead with the operation, then deliver the same cue.

> **ch03 hint** — currently:
> > Stay with the word *rescue.* Who in the scene actually needed rescuing — and who was the joke aimed at protecting? Then look at the pocket. The paper has been there since first period. He hasn't told anyone.
>
> More-visible:
> > Reading between the lines means letting the off-topic evidence count. Stay with the word *rescue.* Who actually needed rescuing — and who was the joke aimed at protecting? Then look at the pocket. The paper has been there since first period. He hasn't told anyone.

The hint still doesn't give the answer; it just opens with the named move so a struggling group hears it before the cue.

### Theme 5 — The fork debrief is the highest-headroom visibility moment

The chapter-5 fork is the story's capstone *considering multiple viewpoints* decision and is currently the most pedagogically-implicit moment in the spine. The lenses describe each branch's philosophy in story terms but never name the cognitive operation the student group just performed. For a class deliberately working on perspective-taking, this is the moment to make the move visible.

This theme is partly already covered by Theme 2's wording shifts on the same lenses — but the *structural* visibility move (naming the operation) is separate from the vocabulary shift, and the operator can take one without the other.

> **ch05 fork (a) debrief lens** — combined Theme 2 + Theme 5:
> > *Considering multiple viewpoints* doesn't always mean blending them. Priya's path lets all three viewpoints exist on paper as separate columns — a promise against any one person rewriting what happened. It buys clarity. It costs the freedom to just be in the moment.

> **ch05 fork (c) debrief lens** — combined:
> > *Considering multiple viewpoints* sometimes means letting them stay different. Tasha's path treats all three versions as the truth, and trades fixing things later for being honest in the moment. It buys depth. It costs comfort.

The named operation lands once per branch, on the lens for that branch — so whichever ending the student group plays, they see the move named.

---

> **Five themes. Which of these matter for Ms. Rivera's class? Take any combination, ask for variations, tell me what I'm missing, redirect if I'm pointing at the wrong things.**

---

## Operator reaction (the loop signal)

> Okay. Theme 1 is exactly right — Ms. Rivera flagged the long choices specifically. Apply it.
>
> Theme 2 — you're right that those words are too adult, but I think you're going further than she'd want. She likes "trade-off shape" language; she just wants the worst offenders down-leveled. Stick to the words you flagged (*covenant*, *transactional*, *forecloses*, *vulnerability*, *spontaneity*) and leave the rest of each lens alone.
>
> Theme 3 — yes, this is the kind of thing she's asking for. Apply across all gates.
>
> Theme 4 — actually no. She's pretty firm that hints shouldn't lead with the named move. Her view: when a group hits the hint they should still be doing the work — naming the operation right there does some of the thinking for them. Drop it.
>
> Theme 5 — yes, capstone. But she'd want both branches she sees in the lesson to have the named move on them, not just one. Make sure all three branches are named.

This reaction exercises the loop in three different shapes:

- *Approval* on themes 1, 3, 5 — locked into the plan.
- *Calibration* on theme 2 — direction right, intensity too high. Re-narrow the scope.
- *Redirection* on theme 4 — drop. The teacher's pedagogical reasoning ("hints shouldn't do the work") is now part of the criteria the skill carries forward.

The skill updates `revision-session.md` with three things:

1. **Refined opportunity set.**
    - Theme 1 — *teacher-approved* (apply as shown).
    - Theme 2 — *under refinement* (narrowed: only the five flagged tier-3 words; preserve rest of lens text verbatim).
    - Theme 3 — *teacher-approved* (apply across all four gates).
    - Theme 4 — *teacher-rejected* (do not name the operation in hints; carry as a criterion: hints lead with cues, not with the named skill).
    - Theme 5 — *teacher-approved* (apply across all three fork branches).

2. **Change summary.** Narrowed Theme 2 to a five-word vocabulary swap; dropped Theme 4 with reason (teacher's hint principle); confirmed Theme 5 spans all three branches; locked Themes 1 and 3.

3. **Next prompt.** One iteration to confirm Theme 2's narrowed scope with one concrete example.

---

## Loop iteration 2

> Quick confirmation on Theme 2. Narrowed it to a vocabulary swap on the five words you flagged, leaving the rest of each lens alone. Here's what that looks like for fork (a):
>
> Currently:
> > This perspective puts shared, written truth above ongoing repair — a **covenant** against any single person rewriting the past. It buys clarity. It costs **spontaneity**.
>
> Narrowed Theme 2 (just the word swap):
> > This perspective puts shared, written truth above ongoing repair — a **promise** against any single person rewriting the past. It buys clarity. It costs **the moment**.
>
> Then Theme 5 (capstone naming) on top of that:
> > *Considering multiple viewpoints* doesn't always mean blending them. This perspective puts shared, written truth above ongoing repair — a promise against any single person rewriting the past. It buys clarity. It costs the moment.
>
> Same shape for the other two branches; same shape for `perspective_contrast` in the overall debrief. Other lens text untouched. Good?

### Operator reaction (iteration 2)

> Yes. Apply it.

Loop terminates at iteration 2. The skill writes the final entry to `revision-session.md`:

---

## Approved plan (locked)

| Theme | Status | Scope of application |
|---|---|---|
| 1. Decision-label tightening (≤25 words per choice) | Approved | All chapter-end choice labels in ch02 and ch04 (ch01, ch03, ch05 already within band on a re-scan); preserve `is_correct` and `misconception_targeted` annotations verbatim. |
| 2. Vocabulary swap (narrowed) | Approved | Replace *covenant → promise*, *transactional → like a contract*, *forecloses → closes off*, *vulnerability → openness*, *spontaneity → the moment* in all per-chapter and fork debrief lens text and in `metadata.perspective_contrast`. Do not touch other words in the lenses. |
| 3. Per-chapter debrief lenses name the cognitive operation | Approved | Append a one-sentence naming line to the *correct-choice* debrief lens at every gate (ch01, ch02, ch03, ch04). Wrong-choice lenses unchanged (already do their work). |
| 4. Hint operation-naming | Rejected | Carry forward as a criterion: hints lead with cues, not with named operations. |
| 5. Fork debrief naming | Approved | Append a one-sentence naming line to all three fork branch debrief lenses (ch05). Apply on top of Theme 2's vocabulary swap. |

### What the apply phase will do, in order

1. Build `middle-school-friendship-revised-v1/`, copy chapter files and master.
2. Walk the four spine chapter gates: tighten ch02 and ch04 choice labels (Theme 1); append cognitive-operation naming lines to correct-choice lenses (Theme 3); leave wrong-choice annotations and misconception names unchanged.
3. Run the elimination check on every adjusted gate. (Theme 1 cannot break the check by construction — only labels were tightened, pulls were preserved — but the check is still mandatory.)
4. Walk chapter 5 fork: apply vocabulary swap (Theme 2 narrowed) to all three branch lenses, then append cognitive-operation naming line to each (Theme 5).
5. Apply vocabulary swap (Theme 2 narrowed) to `metadata.perspective_contrast` and any per-chapter debrief lens prose carrying the flagged words.
6. Recompute runtime with the grade-6 coefficient (30 s/page) — expected ~21:30 median (down from ~23:32 at grade-5 coefficient), inside the 24-min budget with comfortable headroom.
7. Verify phase: elimination check across all gates; fork legitimacy on the three fork branches (none should be affected, but check); ending diff (no expected change); bible sync (no bible changes, but cheap to verify); schema validity; partial-application report (none expected — no visibility-down operations were requested).
8. Author `teacher-prep.md`: name the cognitive operations now visible in each lens; list the five tier-3 → grade-6 swaps; identify the three highest-leverage discussion prompts per chapter, grounded in the misconception annotations the *wrong* choices retain.
9. Write deliverables to `middle-school-friendship-revised-v1/`. Source files untouched.

### What stays the same (operator reminder for Ms. Rivera)

- All five chapter structures, the perspective fork shape, three endings.
- Every character, the locked art style, every image prompt.
- The targeted skill at every gate and at the fork.
- Every misconception annotation on every wrong choice.
- Every hint (the operator's redirection on Theme 4 preserved them all verbatim).

### Estimated runtime after apply

- Median path: ~21:30 (grade-6 coefficient, no page-count change).
- Worst case (ending C, 23 pages): ~21:55.
- Inside the original 24-min budget. The spare ~2:00 absorbs the additional decision-deliberation time the more-visible debrief lenses may invite.

---

## Notes on this session for the few-shot reader

Three things worth noticing about the shape of this session:

**The diagnostic surfaced more no-ops than ops.** Five of nine misconception pulls are flagged as "already at strong intensity — leave alone." Most in-chapter narration is flagged as already grade-6-comfortable. Honest no-ops are part of the brainstorm output; they tell the operator (and through them the teacher) that the story has already done some of the calibration work and the revision is targeted, not wholesale.

**The teacher's redirection on Theme 4 became a durable criterion.** Once the operator surfaced "hints shouldn't lead with the named move," the skill carried it forward as a guardrail for any future iteration — not just for this story but for any subsequent revision pass for Ms. Rivera. The skill's interpretation of teacher criteria sharpens with each loop iteration; it does not reset.

**Theme 2 and Theme 5 stack on the same surface.** The fork debrief lenses are touched by both themes — Theme 2 narrows the vocabulary, Theme 5 prepends the named operation. The skill applied them in the right order (vocabulary first, naming second) so the named-operation line lands cleanly on top of grade-6-band prose. When two themes touch the same surface, order matters.
