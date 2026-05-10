# Skills reference

Per-skill **registry** for the polylogue pedagogy lens. Three pieces per skill: stable misconception names (used as `misconception_targeted` in `story.json` for cross-story consistency), medium-specific staging pedagogy (what the panel needs to show when this skill is at the chapter end), and a selection warning (when this skill is a poor fit for a chapter).

This file is **not a pedagogy textbook.** Definitions of what these skills are, mastery rubrics across grade levels, generic authoring craft — those are LLM competence and aren't written here. The file provides only what coordination and medium specificity require.

**Calibration on what specific wrong-choices work emerges from author reactions during iteration**, not from pre-baked worked examples. The principle is *decisions, not verification* — see SKILL.md. The author corrects the LLM's first wrong-choices, and those corrections encode taste into the artifact.

**Skills here are available, not required.** Author challenges only where the chapter's staged scene supports them. The story's dramatic shape decides which chapter ends carry challenges.

## Position-distribution authoring habit

Across the story's challenges, distribute the correct-answer position roughly evenly across A / B / C. Target ≥1 of each across the full story; in chapters with both a comp check and a gate, the two challenges should not share the same correct position.

The natural authoring habit gravitates toward (C) — *correct after the wrongs reads like a climax in prose*, and writing chronologically wrong-then-right pushes correct to the end. Resist this explicitly. With 3-MC + 2 attempts already conferring ~67% naive-guess success, a deterministic correct-position pattern collapses the gate further; students who play more than one story will pick up the pattern and bypass the skill check.

When in doubt: roll a die for the correct position, then check it doesn't repeat with the chapter's other challenge. Mechanical; resolve silently.

## Gap-handling protocol

When the author lands on a skill in `thinking-skills.md` that doesn't have a registry entry, draft one inline before authoring the challenge. Format:

1. **Misconceptions** — three named failure modes in `<adjective>-<concept>` form (e.g., `surface-of-the-word`, `picking-a-winner`). One-line description per failure mode, plus one example wrong-choice in MC voice.
2. **Staging pedagogy** — one or two lines on what the panel needs to show when this skill is at the chapter end (medium-specific).
3. **Selection** — one line on the shape of scene this skill needs.
4. **Hint shape** — one line on how the post-attempt-1 hint should redirect (text-anchored / discussion-prompting / framing-nudge).

Surface to the author **only** the part where their classroom context determines the answer — typically: *"do these failure modes match how your students actually miss this skill, or are there others to swap in?"* Don't ask for review of the whole draft. If the author confirms (or adjusts), the entry can be added permanently to this file.

---

## Foundational Reading

### Vocabulary in context · `[comprehension_check]` · individual

**Misconceptions** (use these names in `misconception_targeted`):

- `surface-of-the-word` — treats less-familiar word as similar to a more-familiar lookalike, ignoring context. *Wrong (e.g.):* "Jordan took money out for the project" (when "withdrew" was used).
- `ignoring-context` — picks a dictionary-correct meaning that doesn't fit the scene. *Wrong (e.g.):* "Jordan pulled out a notebook."
- `substituting-plot-for-meaning` — names what's happening in the story instead of what the word means. *Wrong (e.g.):* "Jordan is angry at Maya."

**Staging pedagogy.** Image is secondary; the cue lives in dialogue and surrounding text. Don't encode the word's meaning into the panel composition.

**Selection.** Works on words with morphological structure (prefixes, suffixes, recognizable roots) or with literal/figurative tension. Pure jargon and acronyms don't admit the failure modes — omit the comp check if no word of this shape stages naturally; don't force one.

**Hint shape.** Text-anchored — *"Look at the rest of the sentence — what's it telling us about [word]?"*

---

## Thinking

### Inferencing · `[gate]` · group

**Misconceptions:**

- `surface-reading-only` — answers what's literally on the page, treating the text as a transcript. *Wrong (e.g.):* "Maya isn't hungry today."
- `over-inferring` — leaps to a dramatic conclusion the text doesn't support, often importing an exciting genre script. *Wrong (e.g.):* "Maya is hiding a serious illness from her family."
- `wrong-direction-inference` — fixates on one weak detail and misses a stronger one. *Wrong (e.g.):* "Maya doesn't like the sandwich her mom made."

**Staging pedagogy.** Stage the multiple pieces of evidence the inference combines (body language, environment, action, what's said vs. what's done). Each evidence piece must be visibly depictable in a panel, not buried only in narration. Don't editorialize through composition — no dramatic backlighting that says "lonely," no isolation framing that says "burdened." Show behaviors; let the reader read them.

**Selection.** Scenes with at least two visible evidence pieces. Avoid scenes where the inference is the only possible reading — that becomes recall, not inferencing.

**Hint shape.** Discussion-prompting — redirect the group to evidence the staging plants without revealing the answer. *"What did the chapter show us before this moment? Talk it through with your group."*

### Considering multiple viewpoints · `[fork]` · group always

**Misconceptions:**

- `picking-a-winner` — names one view as "correct" and the other as a misunderstanding. *Wrong (e.g.):* "Jordan was just being defensive — Maya was right."
- `flattening-to-everyone-has-an-opinion` — treats both views as equally valid because held, without engaging with the reasons. *Wrong (e.g.):* "They both have feelings about it."
- `fake-compromise` — invents a position neither side actually holds. *Wrong (e.g.):* "They both wanted to do a good job and just got frustrated."

**Staging pedagogy.** All correct paths must be visually approachable on the page that lands the fork. No compositional tilt — comparable visual sizes across the perspective figures, comparable distances from the protagonist, even lighting. The camera must not have already chosen.

**Selection.** Each correct branch must represent a view a thoughtful person *who held that view* would defend. If one branch is clearly more virtuous, the fork is hollow — redesign. The incorrect choice (when present) typically fails by *avoiding* the perspective conflict (deferring to authority, opting out, picking-a-winner-via-shortcut) rather than by holding a different perspective.

**Hint shape.** *2-correct/1-incorrect:* discussion-prompting on what's at stake for each side. *3-correct/0-incorrect:* `deliberation_prompt` framing nudge inviting the group to weigh paths before voting.

---

## Social-Emotional (SEL-as-content)

### Recognizing when a peer is dismissed · `[gate]` · group always

**Misconceptions:**

- `charitable-misread` — names a benign explanation that ignores the visible cue. *Wrong (e.g.):* "Priya didn't hear Jordan."
- `personal-attribution` — locates the cause inside the dismissed person rather than in the social pattern. *Wrong (e.g.):* "Jordan is just shy."
- `mirror-symmetry` — treats a one-sided pattern as if both people were doing it equally. *Wrong (e.g.):* "They were both talking over each other."

**Staging pedagogy.** The panel composition is the *primary* evidence — dialogue and narration support but cannot replace what visible staging shows. Eye-contact direction, gaze tracking, body angles, and frame-positioning are load-bearing. Show cues across at least two panels (the dismissal moment + a contrast moment, e.g., the same idea accepted from a different speaker). A single panel makes the question recall.

**Selection.** Scenes that stage the social pattern *visibly* — through repeated cues, contrast (the same idea accepted from a different speaker), or behavioral consequence (the dismissed person going quiet). Avoid scenes where the dismissal is implied but not shown — that becomes inference, not social-awareness.

**Hint shape.** Discussion-prompting on the contrast — *"What did Priya do when Jordan started talking? And what happened when Oz said almost the same thing? Talk through the difference with your group."*

**Bar shifts G5→G7.** G5 names *what* (Priya cut off Jordan); G6 names *the pattern* (it happens to Jordan a lot in this group); G7 names *the consequence* (Jordan stopped offering ideas at all). Shape the prompt and choices so the bar matches the chosen grade level.

---

## Skills in the catalogue without a registry entry

Most of `thinking-skills.md` (sequencing, predicting, distinguishing fact from opinion, recognizing assumptions, the lumped fallacies, additional SEL-as-content skills, etc.) are usable in stories — the gap-handling protocol above produces an inline draft entry per author session. Once a session's drafted entry has been confirmed by an author, it's a candidate for permanent inclusion here.
