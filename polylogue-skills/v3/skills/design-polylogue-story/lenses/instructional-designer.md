---
description: Pedagogy concern lens for the design-polylogue-story skill. Use when sketching teaching moments per concept (Round 1), assigning skills to chapter-end slots (Round 2), adapting the draft to grade level (Round 3), authoring chapter-end challenges (Round 3), running the elimination check, and tracking correct-answer position distribution. Per-skill misconception registries, staging pedagogy, and selection warnings live in `skills-reference.md` — read the relevant entry before authoring a challenge that targets that skill, or draft one inline if the entry is missing. Read this file in the design-polylogue-story round flow when pedagogy is the active concern.
---

# Pedagogy lens

This file captures what to attend to when the work is pedagogical: per-concept teaching-moment sketches, slot assignments, grade-level adaptation, chapter-end challenge authoring, the elimination check, position distribution. It's a briefing on a concern, not a stage to formally enter and exit.

The story-craft lens (`creative-writer.md`) provides the draft and the staged scenes you author against. The polish/renderer lens (`reviewer-editor.md`) polishes your output, composes the final image prompts, and runs the Round 4 quality review.

## What this lens brings

`skills-reference.md` is a *registry* — stable misconception names (used in `misconception_targeted` for cross-story consistency), per-skill staging pedagogy (medium-specific), and selection warnings (system-specific). It is **not** a pedagogy textbook — definitions, mastery rubrics, and authoring craft are LLM competence and aren't written there. Read the relevant entry before authoring a challenge that targets a skill.

Misconception specificity is the load-bearing work — vague wrong choices kill the pedagogy. Generic labels ("surface reading") used across every story produce gates that don't discriminate. Use the registry's exact misconception names; ground each wrong-choice in what the chapter actually staged.

## Inputs

- The draft from the story-craft lens (concept options, outline, pages, characters — depending on round).
- The story's `grade_level` (5, 6, or 7), `primary_skill`, and `secondary_skills`.
- `skills-reference.md` — per-skill registry (misconceptions + staging pedagogy + selection warnings) plus the gap-handling protocol.
- `thinking-skills.md` — taxonomy of skill names with slot tags (`[comprehension_check]`, `[gate]`, `[fork]`).
- The story's running state from `polylogue.md` (chapters drafted so far, challenges already authored — for cross-chapter awareness and position-distribution tracking).

## Three responsibilities

1. **Round 1 — teaching-moment sketches per concept.**
2. **Round 2 — slot assignments per chapter.**
3. **Round 3 — grade-level adaptation and chapter-end challenge authoring.**

### 1. Round 1 — teaching-moment sketches per concept

When the story-craft lens has produced 3–5 concept candidates, layer two pedagogical dimensions onto each. These are first-class output, not afterthoughts — without them, the author chooses between concepts on narrative grounds alone, missing the dimension that matters most for a teaching tool.

**Skills targeted (per concept).** Primary + secondary thinking skills the concept naturally implicates. Draw from `thinking-skills.md` (catalogue) and `skills-reference.md` (those with registry entries — others are usable, you'll just draft an entry inline). One-line reason each ("this story has multiple characters reasoning aloud → counter-arguing fits"); name the slot(s) each skill would fill.

**Teaching moments (per concept).** Sketch 2–4 concrete challenges the concept makes available — a mix of comp checks, gates, fork moment. Ground each sketch in a scene the concept naturally produces. One-line per challenge ("Inferencing gate: Maya's behavior at lunch — surface reads as 'tired,' correct read combines phone-check + missed connection.").

The author picks a concept partly on what teaching surface it offers; your sketches are what makes that judgment possible.

### 2. Round 2 — slot assignments per chapter

When the outline lands alongside the cast and art style, decide which chapter ends carry challenges and which skills fill which slots.

A chapter end has 0, 1, or 2 challenges:

- **No challenge.** The chapter is a transition or breath; nothing pedagogical to extract without forcing.
- **Comp check only.** A natural vocabulary moment exists; the chapter doesn't carry a real decision moment.
- **Decision only.** A real decision moment exists; the chapter doesn't naturally stage a vocabulary or main-idea moment.
- **Both.** Comp check first as warmup; decision as the gate or fork.

Don't force a slot the chapter doesn't support. Manufactured comp checks where no natural vocab moment exists become recall, not vocabulary-in-context. Manufactured gates where no real decision exists become contrived.

Assign skills to slots: foundational reading skills to `[comprehension_check]` slots; thinking skills to `[gate]` slots; perspective-taking thinking skills (or SEL-as-content perspective-shift skills) to the single `[fork]` slot. Slot tags in `thinking-skills.md` are affordances — a skill tagged `[gate]` *can* fit when the chapter naturally stages it; you decide per-chapter.

### 3. Round 3 — grade-level adaptation and challenge authoring

#### Grade-level adaptation

Adapt the draft to the chosen reading level.

- **Grade 5** readers want short, concrete sentences with vocabulary in their everyday range. Avoid abstract metaphor; new words should be supportable from context.
- **Grade 6** readers can handle moderate length and abstraction; some metaphor when grounded.
- **Grade 7** readers welcome longer sentences, wider vocabulary, metaphor, inference-rich language.

Across all levels: dialogue must sound like middle schoolers — or like adults in a way middle schoolers find natural. Read each line aloud mentally; would a real student at that grade say this?

Rewrite phrases or sentences for grade-level fit. Don't change plot, character motivations, or scene structure — those are story-craft. If grade-leveling forces a content change, flag it back rather than silently changing the story.

#### Chapter-end challenge authoring

For each chapter end, author the relevant challenge(s) according to the slot assignment from Round 2.

**Comprehension check** (when present): foundational skill, individual default, formative — does NOT route the story; failure does NOT trigger abrupt-end.

- 3-MC, 1 correct + 2 wrong; each wrong annotated with `misconception_targeted` from the registry in `skills-reference.md` for the named skill.
- Hint after attempt 1: text-anchored. Redirect to evidence in the chapter; don't reveal the answer.
- Coin schedule: locked at **1/0/0** (1 if correct on first attempt; 0 otherwise — the formative signal).
- Attempts allowed: 2.

**Decision (gate)**: thinking skill or SEL-as-content, group default, narrative routing.

- 3-MC, 1 correct + 2 wrong; each wrong annotated with `misconception_targeted` from the registry. Each wrong should ride a real grade-band misconception, not a red herring. The chapter's staged scene must invite each wrong-choice misread.
- Hint after attempt 1: discussion-prompting. Redirect to evidence the staging plants; can also invite SEL-as-process behaviors. Reframe; don't reveal.
- Coin schedule: 3/1/0. Attempts: 2.

**Decision (perspective fork)**: perspective-taking thinking skill (`[fork]`-tagged) or SEL-as-content perspective-shift skill. Group always. Exactly one per story.

- Variant: 2 correct + 1 incorrect, OR 3 correct + 0 incorrect (author preference).
- Each correct choice represents a genuinely distinct, defensible perspective. Run the legitimacy check: would a thoughtful person who held perspective X choose this? If one branch is clearly more virtuous, it's not a real fork — flag back.
- Each correct choice routes to a different `next_chapter_id`.
- For 2-correct/1-incorrect: incorrect choice annotated with `misconception_targeted`; abrupt-end on attempt-2 failure. `hint_after_attempt_1` applies.
- For 3-correct/0-incorrect: no failure mode. Use `deliberation_prompt` (framing nudge presented when the choice lands) instead of `hint_after_attempt_1`.

#### Output format per challenge

```
**Slot:** comprehension_check | gate | perspective_fork
**Skill:** <name from thinking-skills.md>
**Challenge type:** individual | group
**Prompt:** <one sentence or short scenario, framed in-fiction>

- (A) <label>  [correct | incorrect: misconception=<name>]  → next_chapter_id: <id> (if correct routing)
- (B) <label>  [correct | incorrect: misconception=<name>]
- (C) <label>  [correct | incorrect: misconception=<name>]

**Hint after attempt 1:** <one sentence>          (gate / 2-correct fork / comp check)
**Deliberation prompt:** <one sentence>           (3-correct fork only)

**Debrief lens (per choice):**
- (A): <how this choice plays in the debrief>
- (B): ...
- (C): ...
```

## Mandatory elimination check

For every challenge, ask explicitly:

> Could a student lacking the named skill arrive at the correct answer via elimination, narrative cues, or common sense?

For **group challenges**, the bar is harder:

> Could a *group* of students lacking the skill collectively arrive at the correct answer through discussion?

Group discussion narrows the field. A wrong choice that fools one student often gets surfaced and rejected when three argue about it — so group-targeted wrong-choices need to be sharper.

If a wrong choice sounds clearly off when read out of context, sharpen it. If it doesn't pattern-match a named misconception in the registry, sharpen it. If a quick group-deliberation simulation eliminates two wrongs trivially, the wrongs are too weak.

**Resolve elimination-check failures by sharpening, not by flagging.** This is LLM competence, not author context. Iterate the wrong-choices until the check passes. The author shouldn't be asked to verify wrong-choice quality — that's your call. The exception is when the author has classroom-specific knowledge the registry doesn't ("my students don't actually make that misread; they make this other one") — in that case, flag the specific misconception for confirmation, not the whole challenge.

## Position distribution (track across the story)

Distribute the correct-answer position roughly evenly across A / B / C. Target ≥1 of each across the story; in any chapter with both a comp check and a gate, the two challenges should not share the same correct position. The natural authoring habit gravitates toward (C) — resist it explicitly. With 3-MC + 2 attempts already giving ~67% naive-guess success, deterministic position patterns collapse the gate further.

This is mechanical. Track it as you author and resolve it yourself; the polish/renderer lens re-checks at Round 4.

## Gap-handling: skills without a registry entry

When the chosen skill is in `thinking-skills.md` but doesn't have a `skills-reference.md` registry entry, draft one inline before authoring the challenge:

1. Three failure modes the LLM is confident about, named in registry style (e.g., `<adjective>-<concept>` — `surface-of-the-word`, `picking-a-winner`).
2. One-line description per failure mode + an example wrong-choice in MC voice.
3. One-line staging pedagogy note (what the panel needs to show — medium-specific).
4. One-line selection warning (what shape of scene this skill needs).

Surface to the author *only* the part where their classroom context determines the answer — typically: "do these three failure modes match how your students miss this skill, or are there others to add?" Don't ask for review of the whole draft. Once the author confirms (or adjusts), the draft entry can be added permanently to `skills-reference.md` if they want.

## SEL-as-process: hint guidance for group challenges

Skills like *active listening*, *disagreeing respectfully*, *taking turns*, *voicing dissent* aren't gate-able by 3-MC — they're *performed* during group discussion rather than *selected* on a question. They're not in the taxonomy as challenge skills, but they live in the **hint after attempt 1** for group challenges.

When authoring a hint for a group challenge, consider whether the hint can also invite SEL-as-process:

- *"Has every member of your group shared what they noticed before you re-vote?"*
- *"If you disagreed about the answer, try arguing the *other* side for a moment before you vote again."*
- *"What's another angle? Has anyone in your group noticed something different from the rest of you?"*

Don't shoehorn — only when the prompt naturally supports it. The first job of the hint is still pedagogical (redirect to the missed evidence). SEL is the bonus when both fit.

## Decisions vs competence

Pedagogy work is largely LLM competence: misconception specificity (given the registry), elimination-check resolution, hint phrasing, position distribution, grade-level adaptation. Make those calls confidently. Resolve issues by iterating, not by flagging.

What surfaces to the author as a decision: where the author's *classroom-specific* knowledge changes the answer — do these wrong-choices match how *your* students miss this skill; does this perspective fork's branch set match the perspectives *you* want exposed; is there a misconception in your students' actual repertoire that the registry doesn't cover. These are bounded, specific decisions, surfaced one at a time, not "please review my work."

## What other lenses handle

- Plot, characters, scene staging, abrupt-end pages → story-craft lens.
- Final renderer-facing image prompts and quality review → polish/renderer lens.
- Bible sync and renderer-facing mechanical scans → polish/renderer lens.

## Principles

- **Misconception specificity is the load-bearing work.** Grounded, scene-specific, real-student misconceptions are the work.
- **Slot tags are affordances, not rules.** A skill tagged `[gate]` *can* fit when the chapter naturally stages it.
- **The chapter's shape decides.** Don't force a comp check on a chapter without a vocab moment. Don't force a gate on a chapter without a real decision.
- **Grade-level fit is non-negotiable but should not flatten voice.** A grade-6 story can still have a sharp, funny, distinctive narrator — just within reach of a 6th-grade reader.
- **Hints teach, they don't solve.** A great hint redirects attention to evidence or reframes a misread. A weak hint just tells the kid the answer.
- **The fork's correct branches must be peers.** No "best answer" wearing a perspective costume.
- **Position distribution is yours, not the reviewer's.** Track it as you author.
- **Iterate to resolve, flag to invite.** Sharpen wrong-choices yourself; flag only when the author's classroom context determines the answer.
