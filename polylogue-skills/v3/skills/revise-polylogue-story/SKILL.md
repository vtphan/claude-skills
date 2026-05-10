---
name: revise-polylogue-story
description: Collaboratively revise an existing polylogue story for a specific classroom by adjusting reading level (grade 5/6/7) and the visibility of the lesson's thinking moves (more visible, as authored, less visible). The skill brainstorms opportunities with the teacher using concrete before/after examples from the story, then applies the agreed revisions while preserving the story's pedagogical structure. Use when a teacher wants to adapt a polylogue library story for their students. Do NOT use for creating new stories from scratch — use `design-polylogue-story` for that.
---

# revise-polylogue-story

Help a teacher calibrate an existing polylogue story for a specific classroom. The story already exists — produced by `design-polylogue-story` and stored as a library asset. The teacher's job is to judge what would land best for their students; the skill's job is to do the analytical and generative work that makes good judgment cheap.

The skill operates on two axes:

- **Reading level** — grade 5, 6, or 7
- **Skill visibility** — *more visible* (sharper misconception pulls, named cognitive moves), *as authored*, *less visible* (subtler cues, more demanding reading)

These are calibrations, not authoring moves. The story's structure — chapters, characters, art style, perspective fork, targeted skills, divergent endings — is preserved. What changes is the surface language and the pedagogical signal-to-noise.

## Operating Principle

Bring the analytical and creative work to the table before asking the teacher to commit. The teacher's reactions reveal taste, criteria, and classroom context the skill cannot infer from the story file alone — so generate concrete options, surface them, and refine based on signal.

Prefer:
- Surfacing 3–5 opportunity themes with concrete before/after examples in the first turn.
- Default-and-confirm over open-ended questions.
- Calibrating skill output through teacher reactions (yes / no / lighter / sharper / not quite).
- Accumulating teacher signal across loop iterations rather than starting over.
- Moving toward a revision plan the teacher can approve in plain language.

Avoid:
- Asking the teacher what they want before showing them what's possible.
- Surfacing abstract operations ("I'll make it more visible") without concrete examples.
- Open-ended menus longer than 5 themes.
- Looping more than 3 iterations without checking whether the conversation is converging.
- Manufacturing opportunities. If a story is already well-calibrated, say so.

**Brainstorm-style outside, authoring-quality inside.** The teacher sees a short, focused conversation about concrete moves on their story. Underneath, the skill orchestrates the same pipeline stages and quality checks that produced the story in the first place.

## Teacher's Job

The teacher's required engagement is small and well-defined:

1. Invoke the skill on a library story.
2. React to the opportunity themes the skill surfaces. Reactions can be coarse: yes, no, mostly, lighter, sharper, not quite, show me chapter X, I want something different.
3. Approve a revision plan when ready.

The teacher is *not* required to formulate revision intent from a blank page, read the story file, or know what "amplification" or "elimination check" mean. The skill does the diagnostic and generative work; the teacher judges.

**Default-and-confirm over ask.** Reserve real questions for cases where the teacher's intent is genuinely ambiguous *and* a default would be wrong in a way the skill cannot recover from. The 3-question cap is a ceiling; the target is zero.

**Exit at any point.** If the teacher signals readiness or asks for the revised story, generate outputs from the current approved plan. If parts of the plan are partial, mark them and produce what's ready.

## Loopback

When teacher signal damages prior brainstorming work, choose loopback proportional to the damage:

- **Revise-in-place**: a single example was off, but the theme it illustrates is right. Show a different example.
- **Re-narrow**: the opportunity set is too broad. Drop themes the teacher rejected; sharpen the rest.
- **Re-diverge**: the opportunity set is exhausted but the calibration axis is still right. Re-scan the story with adjusted criteria for fresh themes.
- **Re-frame**: the calibration axis itself is wrong. The teacher asked for visibility but really wants reading-level work, or vice versa. Switch axes and re-scan.

Loopback can be invoked at any point in the brainstorm phase.

## Artifacts

The skill writes to a sibling folder beside the source library asset. Source files are never modified.

```
{source-slug}/                       # READ ONLY — the library asset
|-- polylogue.md
|-- story.json
`-- chapters/

{source-slug}-revised-vN/             # written by the skill
|-- revision-session.md              # single living artifact: state of the brainstorm
|-- revised-polylogue.md             # produced when the teacher approves a plan
|-- revised-story.json               # produced when the teacher approves a plan
|-- teacher-prep.md                  # produced alongside the revised story
`-- chapters/                        # mirror of source chapters with revisions applied
    `-- chapter-NN.md
```

`revision-session.md` is the only living artifact maintained across the conversation. It holds the current opportunity set, teacher signal history, the skill's current interpretation of teacher criteria, and approved plan items. It is session-internal — the teacher does not read it.

`revised-polylogue.md`, `revised-story.json`, `teacher-prep.md`, and the revised chapter files are the deliverables. They are generated from the approved plan when the teacher signals readiness; they are not maintained in parallel with `revision-session.md`.

Versioning: if `{source-slug}-revised-v1/` already exists when the skill is invoked, write to `{source-slug}-revised-v2/`, and so on. Teachers can revise their revisions; each session produces a new versioned folder.

No rounds folder. The brainstorm phase fits in `revision-session.md`; the apply phase is one-shot; the verify phase produces the deliverables. There is nothing the skill needs to preserve across sessions that does not fit in the session artifact.

## Invocation

- `revise-polylogue-story <path-to-source-story-folder>` — start a new revision session for the named story.
- `revise-polylogue-story` with no args — continue from the most recent revision session in the working directory if one exists; otherwise ask which story to revise.

If the teacher invokes a different command but clearly asks for this workflow ("help me adjust this story for my class"), use the skill.

## The three pipeline stages

The skill orchestrates three pipeline stages that mirror those in `design-polylogue-story`. Each stage has a prompt spec bundled in `agents/`. When phase steps below name a stage, read the corresponding spec and apply its instructions in your current context — these are not registered subagents in the standalone skill, just specs you load on demand.

- **Creative Writer** (`agents/creative-writer.md`) — drafts replacement language at full creative quality. Used in Phase 1 to produce before/after examples; not run in Phase 2 (calibration-only).
- **Instructional Designer** (`agents/instructional-designer.md`) — runs the diagnostic scan, adapts to grade level, runs the elimination check on every adjusted decision.
- **Reviewer/Editor** (`agents/reviewer-editor.md`) — polishes for grade-level voice, runs sync-checks across chapter files, runs the Phase 3 quality-review pass.

## Phase Flow

The conversation has three phases. The first is a loop; the second and third are one-shot.

```
Brainstorm (loop)  →  Apply  →  Verify and Deliver
```

The teacher does not see phase names. They see a focused conversation with examples and reactions, followed by a revised story and a teacher-prep summary.

### Phase 1: Brainstorm (loop)

The skill carries the analytical and generative weight here. Each loop iteration produces a refined opportunity set; the teacher's reactions calibrate what gets refined.

#### First iteration

**Step 1 — Read everything.** Load `polylogue.md`, `story.json`, every `chapters/chapter-NN.md`, and the bundled `thinking-skills.md`. Build an internal model of the story: chapter list with targeted skills, character bible, locked art style, current reading level, runtime estimate, decision-by-decision misconception annotations, fork debrief lenses.

**Step 2 — Run the diagnostic pass on both axes.**

For *reading level*, identify:
- Pages with vocabulary or syntax above the authored grade level
- Decision prompts whose language is dense relative to the rest of the chapter
- Hints that rely on idioms or abstractions students at the level may miss
- Pages already calibrated well (so the skill can say "this is fine as-is" rather than manufacture work)

For *skill visibility*, identify:
- Decisions whose misconception-targeted wrongs have headroom for sharpening (the pull toward the misconception is weaker than it could be) or softening (the wrong choice is stronger than the elimination-check floor requires)
- Hints that are generic where they could specifically name a cognitive move (or vice versa)
- Per-chapter debrief lenses that don't (or do) name the targeted cognitive operation
- The fork's debrief — almost always a high-headroom moment because it's the capstone
- Decisions already pedagogically tight (no headroom; mention as a no-op)

The Instructional Designer does this scan. Dispatch with the full story context and the named axis; receive an opportunity list with chapter-level locations and brief rationales.

The diagnostic produces both opportunities and explicit *no-ops* at chapter-level granularity. A no-op is a chapter, decision, or surface where the story is already at the requested calibration — a misconception pull already at strong intensity, a passage already comfortable at the new reading band, a debrief lens already naming the cognitive move. Surface no-ops in the structured output alongside opportunities; do not bury or omit them. Honest no-ops prevent the operator from assuming revision is wholesale, make the work visibly targeted, and tell the operator where the story is already strong (which is also useful information for the teacher's run).

**Step 3 — Cluster opportunities into themes.** A teacher does not want a list of fifteen micro-opportunities. They want to see the *shape* of opportunity. Cluster the diagnostic findings into 3–5 themes:

- Examples of visibility-up themes: "Misconception pulls in chapters X, Y, Z could land harder," "Hints across the story are generic — each could name a specific thinking move," "The fork's debrief lenses don't name the cognitive operation."
- Examples of visibility-down themes: "Misconception language reads as obviously wrong-coded — could be made more plausible-on-the-surface," "Debrief explicitly names the move — could trust readers to notice for themselves."
- Examples of reading-level themes: "Chapter 4 has dense vocabulary at grade 5," "Decision prompts in chapters 2 and 5 are syntactically complex."

Honesty matters. If the diagnostic returned little — the story is already well-calibrated for the teacher's likely target — present that finding directly. "I scanned the story and didn't find significant opportunities for revision at this reading level. Did you have something specific in mind?"

**Step 4 — Generate concrete before/after examples for each theme.** For each theme, produce one or two example revisions: actual current language from the story paired with the proposed revised language. The Creative Writer drafts the revised text; the Instructional Designer ensures it preserves pedagogical integrity (the elimination check passes, the misconception annotation still applies, the targeted skill is unchanged); the Reviewer/Editor polishes for grade-level voice.

These examples are *production-quality drafts*, not sketches. A weak example will make the teacher reject the entire theme. The polish discipline applied here is the same as Round 4 of the authoring skill.

**Step 5 — Present opportunities and examples to the teacher.** Structured output, brainstorming tone. Lead with what the skill noticed; group by theme; show before/after pairs for each theme; close with an open prompt that supports coarse reaction.

Sample shape:

> **{Story Title}** — currently {grade level}, runs {N} minutes, teaches {primary skill}.
>
> I read through it looking for places where revision could matter for your classroom. Here's what I noticed:
>
> **{Theme 1}.** {One-sentence rationale.} For example, in chapter X the {element} now reads:
> > {current text}
>
> It could become:
> > {proposed text}
>
> {Theme 2}. … {Theme 3}. …
>
> Which of these matter for your classroom? Pick any combination, ask for variations, tell me what I'm missing, or redirect if I'm pointing at the wrong things.

Three to five themes. One to two examples per theme. Each example genuinely informative, not filler.

#### Subsequent iterations

The teacher's reaction drives what changes:

- **"Yes, those are right — apply them"** → exit the loop, move to Apply.
- **"Yes to themes 1 and 3, no to 2"** → narrow the plan; ask if anything is missing.
- **"Theme 2 is the right idea but lighter than that"** → revise-in-place; show one or two examples at lighter intensity.
- **"None of these — I was hoping for X"** → re-frame; switch axes or re-scan with the teacher's framing.
- **"You missed chapter 5 — that's what I'm worried about"** → re-diverge; scan chapter 5 specifically and propose themes for it.
- **"Show me a third example for theme 1"** → revise-in-place; produce another example, ideally from a different chapter than the first two.
- **"Something feels off but I can't say what"** → offer alternatives at different intensities, surface the dimensions of variation explicitly, or ask one direct clarifying question. Do not loop on weak signal.

Each loop iteration produces three things in `revision-session.md`:
1. The refined opportunity set, with each item tagged *proposed* / *teacher-approved* / *teacher-rejected* / *under refinement*.
2. A summary of what changed since the previous iteration ("narrowed to themes 1 and 3, dropped theme 2 based on heaviness concern, added theme 6 for chapter 5").
3. The current next-prompt for the teacher.

#### Loop guardrails

- **Accumulate signal, never reset.** Approved themes stay approved across iterations. Rejected themes do not return unless the teacher reverses themselves. The skill's interpretation of teacher criteria sharpens with each iteration.
- **Soft mention at 3 iterations.** When the loop reaches a third iteration, the skill mentions it as an observation, not a stop: "We've been refining for a few rounds. Want to apply what's here, or keep exploring?"
- **Re-frame escape at 6 iterations.** If refinement is genuinely not converging, surface this explicitly: "We've gone through six rounds and aren't quite landing. It might be faster if you describe what you're looking for in your own words and let me start over."
- **Detect circular signal.** If the same kind of refinement request repeats without convergence, surface the pattern. "I've adjusted twice toward 'lighter.' Want to see the lightest version that still passes the elimination check, so you can see the floor?"

#### What the brainstorm phase never does

- It does not ask the teacher to formulate intent before showing them anything.
- It does not present operations abstractly without concrete before/after examples.
- It does not propose changes that violate the customization policy (see below).
- It does not loop endlessly. Six iterations is a hard ceiling; after that, re-frame is mandatory.

### Phase 2: Apply

When the teacher approves a plan, the skill executes it. This phase is one-shot — no loop, no further teacher input until the verify step.

**Step 1 — Build the working directory.** Determine the next available `{source-slug}-revised-vN/` folder. Copy the source `chapters/` contents into the new folder's `chapters/` directory. Copy `polylogue.md` to `revised-polylogue.md`.

**Step 2 — Coupling pass.** Before the chapter walk begins, identify every surface (a chapter's debrief lens, a decision's choice labels, a hint, a fork branch debrief) that is touched by two or more approved themes, and sequence the operations on those surfaces deterministically. The order is: language-level changes first (reading-level adaptation, vocabulary swaps), then structural changes (lens additions, debrief naming, hint specificity adjustments). Reversing this order produces awkward results. Example: a fork branch debrief lens approved for both a vocabulary down-level (e.g., *covenant → promise*) and a named-operation prepend (*"Considering multiple viewpoints doesn't always mean blending them. …"*) — applying the prepend first leaves the named-operation sentence sitting above un-down-leveled body text, and the second pass has to re-read the lens with both changes in scope; applying the down-level first means the prepend lands cleanly on grade-band prose. The coupling pass commits the order before applying; the deliverable surfaces it implicitly through the final text. For surfaces touched by only one theme, no coupling decision is needed.

**Step 3 — Walk the story, applying approved themes chapter by chapter.** For each chapter file, in order:

For *reading-level shifts*:
- The Instructional Designer rewrites narration and dialogue at the new grade level
- Decision prompts and hints are adjusted to grade-level-appropriate language
- The targeted skill at the chapter gate is unchanged
- Image prompts may need staging-line adjustments only if narration changes alter what's depicted; usually they do not

For *visibility shifts (more visible)*:
- The Instructional Designer sharpens misconception-targeted wrong choices — the pull toward each misconception becomes stronger and more tempting
- Hints become more specific to the cognitive move the chapter targets
- Per-chapter debrief lenses explicitly name the targeted cognitive operation if not already
- Page narration is conservatively adjusted to foreground skill-relevant cues; this is the area at most risk of heavy-handedness, so apply minimally
- Run the elimination check after every decision change — visibility-up almost always strengthens the check, but verify

For *visibility shifts (less visible)*:
- The Instructional Designer softens misconception-targeted wrong choices — they remain misconception-targeted but read as more plausible-on-the-surface
- Hints become more general and less prescriptive
- Per-chapter debrief lenses describe what the choice meant in story terms rather than naming the cognitive operation
- **Run the elimination check after every decision change.** This is the asymmetric constraint: visibility-down can break the check. If a chapter's decision fails the elimination check after softening, do not commit the change for that chapter. Flag it for the teacher in the verify phase: "Chapter X could not be softened further without making the question guessable. Held at the previous level."

**Step 4 — Apply visibility shifts to the perspective fork.** Same operations as for gate decisions, but validated by the fork-legitimacy check rather than the elimination check. The fork's *structure* is locked (one fork, three correct branches representing distinct perspectives, divergent endings); only the *visibility* of those perspectives shifts.

**Step 5 — Update the master.** Adjust `revised-polylogue.md`'s reading-level field if changed; recompute the runtime estimate with appropriate coefficients (35 s/page for grade 5, 30 s/page for grade 6, 25 s/page for grade 7); update the per-chapter debrief lens summaries if visibility shifted. Character bible and locked art style are not modified by either calibration axis.

**Step 6 — Run bible-sync.** Even though the bible itself did not change, every chapter's inline character descriptions in image prompts must remain consistent with the bible. The Reviewer/Editor runs a sync-check across all chapters and flags any drift.

The Creative Writer is *not* run in Phase 2 of the MVP. Creative drafting at revision time is out of scope; Phase 2 only edits existing creative content.

### Phase 3: Verify and Deliver

**Step 1 — Run the quality-review pass.** The Reviewer/Editor runs the same checks the authoring skill runs at Round 7, adjusted for the revision context:

- *Elimination check* — every gate decision still passes, including chapters where visibility was softened
- *Fork legitimacy* — the perspective fork's branches still represent genuinely distinct, defensible perspectives
- *Ending diff* — the divergent endings are still drastically different in fate, mood, and lesson
- *Runtime fit* — recomputed runtime is within the original budget (or report the change to the teacher)
- *Bible sync* — inline character descriptions match the bible across all chapters
- *Schema validity* — `revised-story.json` validates against the bundled schema
- *Cross-cutting invariants* — exactly one perspective fork, ending count matches fork branches, all `next_chapter_id` references resolve

**Step 2 — Surface any failures or warnings.** For visibility-down requests that hit the elimination-check floor, report the partial application clearly: "I softened chapters 1, 2, and 5. Chapters 3 and 4 could not be softened further without making the questions guessable, so they're at the original level. Want to leave it as-is or pull back the partial revision?"

For other warnings, follow the warn-and-allow pattern: report the issue, propose a fix, allow the teacher to override if they choose. Record any overrides in `metadata.author_overrides` with a one-line justification.

**Step 3 — Generate `teacher-prep.md`.** A substantive one-to-two-page document for the teacher, containing:

- *What changed* — concise bullet list of the calibration axes applied and the chapters affected
- *What stayed the same* — characters, art style, perspective fork structure, targeted skills (this matters because teachers familiar with the original need to know what's unchanged)
- *Updated runtime* — if it changed
- *Image-pipeline cost* — for the MVP's two axes, this should be "none — text only" unless something unusual happened; surface explicitly so teachers know whether to commission a re-render
- *What to listen for in group discussion* — for each chapter-end decision in the revised story, name the cognitive operation the decision is targeting and one or two student moves that suggest engagement vs. avoidance of the skill. Specific to this story; not generic facilitation advice.
- *Common student misreadings the revised decisions target* — pulled from the misconception annotations, written in plain teacher-facing language
- *Suggested teacher prompts during chapter-end discussion* — one or two per chapter, in the form of questions the teacher can ask groups to surface the targeted thinking move

This is the substantive teacher-prep deliverable. It is not boilerplate; it is specific to the revised story and grounded in the misconception structure of its decisions.

**Step 4 — Write outputs.** Save `revised-polylogue.md`, `revised-story.json`, `teacher-prep.md`, and the revised chapter files to `{source-slug}-revised-vN/`. Source files are not touched.

**Step 5 — Report to the teacher.** Brief summary in chat:
> Done. {Story title} revised at {grade level}, visibility {level}. Runtime: {N} minutes. {Any flags from the verify step.} Files in `{source-slug}-revised-vN/`. The teacher-prep document has facilitation notes for each chapter.

## The Two Calibration Axes — Detail

Phase 2 above describes the operational mechanics of each axis inline with the chapter walk. For the deeper rationale — what changes vs. what stays per axis, the asymmetric constraints (less-visible's hard elimination floor; more-visible's soft heavy-handedness ceiling), and the hint-naming tension — read `references/calibration-axes.md`.

## Customization Policy

The MVP allows revisions only along the two calibration axes. The full table of editable vs. locked fields is in `references/customization-policy.md` — read it when the teacher requests something near the edge of scope. When the request falls outside the policy, refuse warmly and offer alternatives within scope.

## Refusal Patterns

When refusing, follow the pattern: **acknowledge → explain briefly → offer alternative**. Worked examples for the four most common out-of-scope requests (more-obvious answer, re-target a chapter's skill, add a chapter, give the fork a "best" answer) are in `references/refusal-patterns.md`.

## Bundled Assets

The skill loads:

- `schema.json` — JSON Schema for `story.json`. Used by the Reviewer/Editor in the verify phase and by the Apply phase for re-validation.
- `thinking-skills.md` — canonical list of skill names. Used to resolve any skill-related vocabulary the teacher uses to canonical names.
- `sample-revision-session.md` — a fully-worked example session showing what good Phase 1 output looks like. Provided as a few-shot reference for the Instructional Designer's diagnostic mode and the Reviewer/Editor's example-polishing.
- `agents/` — prompt specs for the three pipeline stages (Creative Writer, Instructional Designer, Reviewer/Editor). Read on demand when phase steps name a stage.
- `references/` — progressive-disclosure docs (customization-policy, refusal-patterns, calibration-axes). Read on demand when the relevant section above links to them.

The skill loads nothing from outside its own folder and the source story folder.

## Iteration Rules

On every continuation:

1. Read the most recent `revision-session.md` in the working directory if one exists; otherwise read the source story.
2. Identify new teacher signal from chat or file edits.
3. Update the session artifact before asking questions.
4. Ask at most 3 questions, only if the answers would materially change the next opportunity set.
5. Move to Apply when the teacher approves a plan, regardless of whether every theme has been refined.

## Communication Style

After each turn, respond to the teacher with:

- What's on the table now (current opportunity set, refined examples, or proposed plan).
- The 1–3 things the teacher should react to or decide.

Keep chat short. The opportunity examples are where the substance lives. Avoid meta-commentary about the skill's process; the teacher does not need to know about phase boundaries, pipeline stages, or quality checks unless something fails and the teacher needs to decide how to handle it.

When the teacher's reaction is rich (specific, multi-faceted), respond with a refined plan and the next examples. When the reaction is thin ("not quite," "I don't know"), offer alternatives at different intensities or ask one direct clarifying question — do not loop on weak signal indefinitely.

When the teacher signals readiness, exit the loop and apply. Do not ask for further confirmation once a plan is approved; the verify step is where additional confirmation happens, if any is needed.
