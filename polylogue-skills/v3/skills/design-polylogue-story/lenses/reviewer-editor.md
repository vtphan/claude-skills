---
description: Polish-and-renderer concern lens for the design-polylogue-story skill. Use when polishing the draft for prose and grade-level voice; composing complete renderer-facing image prompts (verbatim character descriptions inlined, staging-pedagogy attention by skill type); running sync when the bible changes; running the Round 4 quality review (elimination check, fork legitimacy, ending diff, runtime fit, schema validity, position distribution, renderer-facing mechanical scans, staging-pedagogy). Per-skill staging pedagogy lives in `skills-reference.md`. Read this file in the design-polylogue-story round flow when polish, image-prompt composition, or quality review is the active concern.
---

# Polish and renderer lens

This file captures what to attend to when the work is final polish, renderer-facing composition, or quality review. It's a briefing on a concern, not a stage to formally enter and exit.

The story-craft lens (`creative-writer.md`) provided the draft. The pedagogy lens (`instructional-designer.md`) authored the chapter-end challenges and ran the elimination check. This lens makes the result publishable.

## What this lens brings

The renderer-facing rules below and the Round 4 quality-review checklist are mechanical *because the renderer and the schema are mechanical*; those constraints are external. Everywhere else, exercise judgment.

A chapter file that's been through this lens should be readable, complete, schema-valid, bible-synced, renderer-self-contained, and pedagogically aligned (staging supports the chapter-end challenge). The author should be able to trust the artifact and engage where you've explicitly invited their attention — not be put in the position of QA'ing your work.

## Inputs

- Pages with grade-leveled narration and dialogue from the pedagogy lens; chapter-end challenges (comp check + decision per chapter, when present); abrupt-end pages where applicable.
- The character bible and locked art style from `polylogue.md`.
- `schema.json` — JSON Schema for `story.json`.
- `skills-reference.md` — per-skill registry (misconceptions + staging pedagogy + selection warnings) for re-running checks and validating staging-pedagogy.
- `thinking-skills.md` — taxonomy for slot-tag validation.
- The current state of all chapter files in `chapters/`.

## Decisions vs competence — the line

The author's role is *decisive* (taste, scope, classroom context, theme alignment, sensitivities), not *verificative*. The line for what to fix silently vs flag is **not** "does this change meaning?" It's **"do I have privileged context to decide this?"**

**Resolve silently** — these are LLM competence, not author context. Iterate to resolve; don't flag:

- Wordsmithing, grade-level drift, prose flow, dialogue authenticity within established voice.
- Bible-sync drift (image prompts out of sync with the bible's verbatim descriptions).
- Renderer-facing rule violations (the four mechanical scans below). The renderer is mechanical; rewrite to the rules.
- Schema invariants — `next_chapter_id` resolution, coin schedules, attempts allowed, `misconception_targeted` annotations present, `endings.length` matches fork branches, exactly one `perspective_fork`. Fix silently if fixable; if not, the issue is upstream (pedagogy lens) and bounces back there, not to the author.
- Position-distribution miss (correct-answer position skewed). Re-shuffle.
- Staging that doesn't support the chapter-end challenge. Iterate the staging.
- Elimination-check failure on a wrong-choice. Bounce back to the pedagogy lens with a sharpening note; the pedagogy lens iterates until it passes.
- Fork-legitimacy borderline cases where the fix is craft (rephrase a branch description, adjust a staged emphasis).

**Flag for the author** — bounded, specific, with a one-line *why-it's-their-call*:

- **Tone fit.** "The protagonist's voice landed sardonic in this draft — does that fit the room you're teaching?"
- **Theme alignment.** "This chapter leans on a competition theme — does that resonate with your broader curriculum, or should it pull back?"
- **Character / scene appropriateness.** "The cafeteria scene depicts an exclusion dynamic — flagging because you know the social dynamics in your room better than I do. Keep, soften, or change?"
- **Fork branch legitimacy as the author would judge it.** "I drafted three correct branches; one (B) feels marginal to me — does it represent a perspective you want to expose your students to?"
- **Concept selection.** Always the author's call. (Round 1.)
- **Locked art style.** Always the author's confirmation. (Round 2.)
- **Misconception fit to *their* students.** "I used the registry's three vocabulary-in-context misconceptions; do they match what your students actually do, or is there a fourth I should swap in?"
- **Sensitivities specific to the author's setting** — names, depicted situations, family compositions, identity references. Surface explicitly when there's a real choice.

Flag shape:

```
**[FLAG: <category>]** <one-line headline>
- Where: <chapter id, page number, challenge>
- Your call because: <one phrase — "your students" / "your curriculum" / "your taste" / "scope">
- Options: <one or two>
```

If a borderline issue is unclear which side of the line it falls on, ask: *"would the author know something here I don't?"* If yes, flag. If no, resolve.

## Compose complete renderer-facing image prompts

For every page (regular AND abrupt-end), compose the complete `image_prompt`. Image prompts are read by an LLM image generator with **no access** to the story, the bible, or any other page. Each prompt is a self-contained brief.

#### Composition template

```
Aspect ratio: <art_style.aspect_ratio>.

[Style]
<rendering_style>. <palette>. <lighting>. <line_treatment>.

[Characters present]
<for each character on the page, write the verbatim physical_description + clothing + distinctive_features from the bible, prefixed with name and age.>

[Page staging]
<absolute visual instructions: pose, action, environment, mood, camera, framing.>
```

The aspect-ratio line is **always the first line** — verbatim from `art_style.aspect_ratio`.

#### Renderer-facing rules

These are mechanical. The renderer cannot reason about them — translate to the *do*-form before concatenating.

1. **Self-contained.** No cross-page or cross-chapter references — the renderer has no "before" or "later" or "as in Chapter N."
   - *Don't:* "same description as Page 1." / "not the sharp Priya from Ch 2."
   - *Do:* repeat the full character description verbatim. / "Priya's mouth softened, eyes settled, hands relaxed on the open notebook."

2. **Absolute visual states, never comparatives-to-baseline.** The renderer has no baseline.
   - *Don't:* "more relaxed than at the start of Chapter 4." / "cowlick more sprung than usual."
   - *Do:* "shoulders dropped and back nearly straight, head lifted." / "cowlick standing straight up at the crown."

3. **No meta-instructions to the pipeline.** The renderer has no bible, no Round number, no "future reviewer."
   - *Don't:* "skin tones must match the bible exactly."
   - *Do:* "Render skin tones, hair texture, body type, and accessories exactly as described in the [Characters present] section above."

4. **No story-internal nicknames or shorthand.** Translate to a visual state.
   - *Don't:* "the leader-pose softened." / "the article-talk Priya gone quiet."
   - *Do:* "Priya leaning slightly forward, both hands flat on the notebook, chin up — but shoulders relaxed." / "Priya's mouth slightly open then closing, gaze on her lap."

5. **No meta-commentary on composition.** State what the panel shows; don't explain its purpose.
   - *Don't:* "Tasha sees both of them at once — that's the whole point of the composition." / "**Critical: this panel must give all three approachable paths roughly equal visual weight.**"
   - *Do:* "Tasha foregrounded right, gaze tracking from frame-left (Priya) to frame-right (Oz)." / "Three figures composed at comparable visual size, warm natural daylight falls evenly on all three."

6. **No negative-form instructions referencing alternatives the renderer doesn't know.** Rewrite as positive specifications.
   - *Don't:* "no isolating composition on Reuben (no team-up framing); no centering effect."
   - *Do:* "Reuben at frame-left at comparable size to other figures, warm natural daylight falls evenly across the panel."

7. **No on-image text and no speech-balloon planning.** Dialog renders in a separate column on the reader app.
   - *Don't:* "speech balloon over Priya's head." / "a sign reading 'CAFETERIA.'"
   - *Do:* omit text entirely; describe only the visual scene.

8. **Drop aspirational specs the renderer cannot honor.** Percentage-precise art direction, exact ink-skip counts, production-grade asks. Drop from `image_prompt`; those belong to human retouch.

#### Token budget

Target ~250–400 tokens per prompt. Compress the style block by removing meta and aspirational specs. Let `[Characters present]` and `[Page staging]` carry the weight. Flag any prompt over 600 tokens.

#### Bible verbatim

When inlining a character, use the bible's `physical_description` + `clothing` + `distinctive_features` verbatim. **Do not paraphrase** — repetition is what gives downstream image generation a chance at face/outfit consistency. If the bible itself contains pipeline meta or comparatives, translate to renderer-facing language before concatenating.

## Apply staging-pedagogy

Page staging is not independent of the chapter-end challenge. The panel carries pedagogical weight that varies by skill type. When composing the image prompt, ask: *what evidence does the chapter-end challenge ask students to read, and is that evidence visibly present without the camera doing the inference for them?*

Per-skill staging pedagogy (the specifics of what counts as evidence under each skill type) lives in `skills-reference.md`. The orientation:

- **Inferencing gates** — stage the multiple pieces of evidence the inference combines; let the reader read it. Avoid composing the panel to telegraph the answer.
- **SEL-as-content gates** — the panel is the *primary* evidence (eye-contact, body angles, frame-positioning). Dialogue can't replace what staging shows.
- **Perspective forks** — all correct paths visually approachable on the page that lands the fork. No compositional tilt.
- **Vocabulary-in-context** — image is secondary; the cue lives in dialogue. Staging should support the contextual situation.
- **Chapters with no challenge** — staging serves the story without pedagogical constraint.

When staging fails the pedagogy, **iterate to fix**, not flag. Rewrite the staging to put the evidence where the gate's pedagogy needs it. Flag only if the chapter beat fundamentally cannot stage what the chapter-end skill requires (in which case the chapter-end skill assignment is what's wrong, and the issue belongs back in the pedagogy lens).

## Run quality-review checks

After polishing a chapter, run the **local checks**:

- **Schema sanity per chapter.**
  - Comp check (when present): `skill_type=foundational` (or SEL-as-content with `[comprehension_check]`), `challenge_type` set, `coin_schedule = {1, 0, 0}`, `attempts_allowed = 2`, no `abrupt_end`, does not route.
  - Decision (when present): `choices.length = 3`, `attempts_allowed = 2`, `coin_schedule = {3, 1, 0}`, `abrupt_end` present iff any choice has `is_correct=false`. For gates: 1 correct + 2 incorrect, `next_chapter_id` set on the correct choice. For perspective_fork: 2-correct/1-incorrect or 3-correct/0-incorrect; each correct choice has a distinct `next_chapter_id`. For 3-correct variant, `deliberation_prompt` present in place of `hint_after_attempt_1`.
  - Linear chapter: `next_chapter_id` set at chapter level (terminal chapters excepted).
- **Bible sync.** Inline character descriptions match the current bible verbatim.
- **Misconception coverage.** Each incorrect choice has a non-empty `misconception_targeted` annotation pattern-matched to a registered name in `skills-reference.md`.

Fix silently. If the fix is upstream (pedagogy or story-craft), bounce back to that lens, not to the author.

At **Round 4** (the dedicated quality-review round), run the cross-cutting checks and produce a pass/warn/fail report. The report's audience is *you* (for resolve-by-iteration) and the *author* (only on the dimensions where they have privileged context).

| Check | What it asks | Resolution |
|---|---|---|
| Elimination — every gate | Could a group of students lacking the named skill arrive at the correct answer? | Resolve via pedagogy lens (sharpen wrongs). Author flagged only if their students' actual misreads aren't captured. |
| Elimination — every comp check | Could a student lacking the foundational skill still pick the correct answer? | Resolve via pedagogy lens. |
| Fork legitimacy | Each correct branch genuinely distinct, defensible? | Borderline cases flagged for the author with the specific branch named ("(B) feels marginal — does it represent a perspective you want exposed?"). |
| Ending diff | Branches drastically different in fate, mood, lesson? | Reskin pattern flagged for the author (it's a structural taste call). |
| Runtime fit | `total_seconds / 60 ≤ estimated_duration_minutes × 1.10`? | Resolve mechanically (cut pages, trim challenges). If cut requires content judgment, flag with specific options. |
| Bible sync | Inline character descriptions match the current bible verbatim. | Resolve silently. |
| Renderer-facing self-containment | Mechanical scans pass. | Resolve silently — rewrite to the rules. |
| Schema / DAG validity | Cross-cutting invariants hold. | Resolve silently or bounce to pedagogy lens. |
| Position distribution | A/B/C distributed across challenges. | Resolve silently. |
| Staging-pedagogy | Staging supports the chapter-end skill's evidence requirement. | Iterate; flag only if the chapter beat can't support the assigned skill (then the slot assignment is the issue, not the staging). |
| Tone, theme, classroom fit | Does this story land for *these* students? | **Author's call.** Flag specifically. |

#### Renderer-facing self-containment — mechanical scans

Run these as text-pattern scans across every `image_prompt`. They catch the four most common drafting violations:

1. **Cross-chapter / cross-page references.** Scan for: `same as Page`, `same description as`, `as in Chapter`, `as in Page`, `like in Page`, `like Chapter`. Each match: replace with verbatim repeat or absolute description.
2. **Comparatives-to-baseline.** Scan for: `more X than`, `X-er than`, `than usual`, `than at`, `than before`. Each match: rewrite as absolute visual state.
3. **Negative-form instructions referencing alternatives.** Scan for `no X (no Y)`, `without X`, lists of `no A, no B, no C` inside `[Page staging]`. Each match: rewrite as positive specifications.
4. **Editorial bold-print inside `[Page staging]`.** Scan for `**` markers inside the `[Page staging]` block. Each match: remove or move outside the prompt body.

Each match is a FAIL until rewritten. Resolve silently.

## Run sync (when bible changes)

When the human author edits the character bible in `polylogue.md`, inline character descriptions in chapter image prompts may drift. Sync re-pulls every affected page's image prompt from the new bible and rewrites the chapter file. Invoked explicitly (e.g., `/sync-prompts`) or as part of Round 4's bible-sync check. Resolve silently.

## What other lenses handle

- New plot or dialogue → story-craft lens.
- Authoring or restructuring multiple-choice challenges (which choice is correct, what misconception a wrong encodes) → pedagogy lens.
- Concept-level teaching-moment sketches → pedagogy lens.

## Principles

- **The author's attention is the budget.** Don't fill it with verification asks. Resolve where competent; flag where context-bound.
- **Composition is mechanical, not creative.** Bible verbatim. Repetition is the point.
- **Renderer-facing rules are mechanical because the renderer is mechanical.** They feel rigid because the constraint is real, not because the model needs micromanagement.
- **Staging-pedagogy is judgment, not algorithm.** Skill-type guidance frames the question; the model decides whether the panel passes.
- **Trust upstream lenses on their domains.** If story-craft wrote a strange-but-deliberate scene, don't second-guess. Wordsmith without altering intent.
- **Iterate to resolve, flag to invite.** The author's role is decisive on context-bound calls, not verificative on competence calls.
- **Never block export.** Even if checks fail, present a clear report. Warn-and-allow.
