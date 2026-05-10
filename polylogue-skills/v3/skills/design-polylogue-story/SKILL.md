---
name: design-polylogue-story
description: Co-design a graphic-novel choose-your-own-adventure story with a human author for grade 5–7 students. Produces a JSON story package (`story.json`) conforming to the bundled `schema.json`. Each chapter optionally ends with a foundational comprehension check and/or a thinking-skill decision; the story is Y-shaped with exactly one perspective-taking fork that diverges into different endings. Every challenge targets a named skill from the bundled `skills-reference.md` registry. Use when an author asks to design, write, build, or draft a polylogue story.
---

# design-polylogue-story

Co-design a graphic-novel CYOA story with a human author. The story has chapters → pages → optional chapter-end teaching moments (a foundational comprehension check, a thinking-skill decision, both, or neither — the chapter's dramatic shape decides). Exactly one perspective-taking fork diverges into different endings.

The skill carries three concern lenses (story craft, pedagogy, polish-and-renderer) — read whichever fits the work in front of you. The author sees a polished result; rough drafts stay internal.

## Audience and setting

- **Target audience:** grade 5, 6, or 7 students.
- **Reading mode:** each student reads the comic individually on their own laptop.
- **Group mode:** students can ask each other questions and discuss between/at decision points. The polylogue is partly the dialogue inside the comic, partly the *students* talking to each other when they hit a decision.
- **Practical realism:** "individual" challenges may receive peer help anyway. That's acceptable; the individual/group tag signals authoring intent and the elimination-check bar, not enforcement.

## Operating principles

Three principles shape how this skill operates.

### Briefing, not recipe

This skill is designed to be carried out by a capable LLM. It is a briefing for a capable colleague, not a recipe for a procedural worker.

What the file load-bears on (the model can't infer these): the audience and setting above; the catalogue in `thinking-skills.md` and the registry in `skills-reference.md`; the schema (`schema.json`); downstream renderer constraints (in `lenses/reviewer-editor.md`); the goals the work is trying to achieve.

What the file does *not* try to encode (the model already brings these): step-by-step procedures the model can sequence on its own; numerical micro-prescriptions of format; mechanical validation algorithms when an articulated *question* would do; pedagogy-textbook content like definitions and grade-level mastery rubrics.

Slot tags and other catalogue signals are *affordances*, not rules. A skill tagged `[gate]` *can* fit a gate slot; the model decides per-chapter whether the staged scene supports it.

### Iterative dialog with the author

The skill operates from cold start — no sample stories yet exist as few-shot ground truth. In compensation, the design process is structured as iterative dialog: the model brings concrete options the author can react to; the author holds context, scope, and taste-making standards (much of which is implicit). Iteration substitutes for examples — the author's reactions across multiple rounds encode taste into the artifact.

In practice:

- **Bring an artifact before asking.** Default-and-confirm over ask. Concrete options elicit implicit knowledge that abstract questions don't.
- **First-draft offness is the expected case**, not a failure. The author's correction is the signal the system is designed to elicit. Loopback is the natural rhythm of dialog, not a recovery mechanism.
- **Different authors will produce different stories from the same seed.** The dialog is the personalization mechanism.
- **Once a real story is produced through this skill, it becomes a sample for future runs** (when the author chooses to share it).

#### Decisions, not verification

The author's role in the dialog is **decisive**, not verificative. The author holds context the LLM doesn't — taste, scope, *these* students, *this* curriculum, sensitivities, theme alignment. The LLM holds craft and mechanical competence — schema validity, grade-level adaptation, prose polish, renderer-facing self-containment, misconception specificity given the registry, position distribution, elimination-check resolution, bible sync.

The line between silent resolution and explicit attention isn't *"does this change meaning?"* It's *"do I have privileged context to decide this?"*

- **Resolve silently** — craft and mechanical calls. Iterate to fix; don't ask the author to verify your work. The author's attention is the scarce resource; treat it that way.
- **Flag specifically** — bounded decisions where the author's context determines the right answer. Each flag names *what* is being decided and *why it's their call*. Not a review queue.

Examples of context-bound (flag-worthy): tone fit for the author's classroom, theme alignment, character/scene appropriateness, fork-branch legitimacy as the author judges it, misconception fit to *their* students' actual misreads, sensitivity calls.

Examples of competence (resolve silently): elimination-check failures, schema invariants, bible drift, renderer-facing rule violations, position-distribution shuffles, prose polish, grade-level adaptation.

If a borderline case is unclear, ask: *"would the author know something here I don't?"* If yes, flag. If no, resolve.

### Acceptable artifacts before architectural elegance

Aim for a useful, complete-enough story. Defer complexity that doesn't earn its place by improving the actual output.

## Author's job

1. Provide a seed in Round 0: story-line idea, target thinking skill(s), target minutes (default 15), reading level (5/6/7).
2. Make the decisions surfaced at each round-end — the bounded ones flagged for your context.
3. Approve the export.

The author can directly edit `polylogue.md` or any `chapters/chapter-NN.md` between rounds; you pick up edits on the next round.

## Artifacts

```
{slug}/
|-- polylogue.md            # master: concept, character bible, art style, chapter list, runtime estimate, debrief, endings
|-- story.json              # final export (Round 5 only)
|-- chapters/
|   |-- chapter-NN.md       # one per chapter; pages (with image prompts) + chapter-end challenges
|   `-- chapter-NNa.md, NNb.md, ...  # one per fork-branch ending (terminal chapters)
`-- rounds/                 # lazy round files (e.g., quality review reports)
```

`polylogue.md` is the single source of truth for the character bible, locked art style, chapter list, endings, and debrief. Chapter files are self-contained per chapter (pages + complete image prompts + comp check + decision + abrupt-end pages where applicable).

## Invocation

`design-polylogue-story <seed-text>` — start a new story. With no args, continue from current artifacts in the working directory.

## Concern lenses

Three spec files in `lenses/` capture what to attend to for each concern across the round flow:

- **`lenses/creative-writer.md`** — story craft. Plot, character, dialogue, scene staging, abrupt-end consequences.
- **`lenses/instructional-designer.md`** — pedagogy. Misconception registry from `skills-reference.md`, grade-level fit, chapter-end challenge authoring, the elimination check (with group bar), correct-answer position distribution, gap-handling for skills without a registry entry.
- **`lenses/reviewer-editor.md`** — polish and renderer. Prose polish, complete renderer-facing image prompts (verbatim character descriptions; staging-for-pedagogy attention by skill type), bible sync, the Round 4 quality review.

Read these as briefings on what each concern asks of the work, not as procedural stages to step through three times per round. Within a round, draw on whichever concerns are active. The Round 4 quality review is a distinct pass against a checklist — that one is genuinely sequential.

## Round flow

The flow is a collaborative dialog with the author, not a sequential checkpoint procedure. Loopback (revise-in-place / re-narrow / re-diverge / re-frame) is callable from any round and is the natural rhythm of authoring under cold start.

### Round 0 — Seed

Capture: (1) story-line idea, (2) target thinking skill(s), (3) target minutes (default 15), (4) reading level (5/6/7). Validate skill names against `thinking-skills.md`; if author names don't match, surface the closest canonical names and ask whether to map or extend. Initialize `polylogue.md`.

### Round 1 — Concept

Generate 3–5 distinct story concepts (logline, character sketches, arc shape with proposed fork location, tone, theme). For each concept, layer two pedagogical dimensions:

- **Skills targeted** — primary + secondary thinking skills the concept naturally implicates (drawing from `thinking-skills.md`; with depth from `skills-reference.md` for any with registry entries), with one-line reasoning each. Mention which slot(s) each would fill.
- **Teaching moments** — concrete sketches of the challenges each concept makes available: 2–4 example challenges per concept (mix of comp checks, gates, fork moment), grounded in scenes the concept produces.

These are first-class output, not afterthoughts. Without them, the author's concept selection is uninformed on the dimension that matters most for a teaching tool.

Polish before presenting. **Concept selection is the author's call** (taste, scope, audience fit) — the round-end output names this as a decision. The author picks one or composes by combining elements; the secondary-skill set is confirmed. Update `polylogue.md`.

### Round 2 — Cast, art style, and outline

Three things land together because they inform each other: who the cast is, what the world looks like, and what the chapter beats are.

**Cast.** Each recurring character: name, role, age, physical description, clothing, distinctive features, expression baseline. Visually distinct identifiers across the cast — different hair, different builds, different distinctive items — give the renderer a chance at consistency across pages.

**Art style.** Propose defaults (rendering style, palette, lighting, line treatment, aspect ratio — `2:3` unless the author has a reason otherwise). **Author's call to confirm or adjust.** Renderer-facing verbatim verification of the locked style happens downstream when image prompts are composed.

**Outline.** Y-shaped chapter outline: chapter beats from the arc (don't impose a chapter count), fork placement, divergent endings sketch.

Then, with the outline visible, decide which chapter ends carry challenges. A chapter end has 0, 1, or 2 challenges (comp check + decision, comp check only, decision only, or neither). Not every chapter needs a teaching moment — a chapter without a natural vocabulary moment shouldn't have a comp check forced; a chapter without a real decision shouldn't have a manufactured gate. Assign target skills to slots: foundational reading skills to `[comprehension_check]` slots, thinking skills to `[gate]` slots, perspective-taking thinking skills (or SEL-as-content perspective-shift skills) to the single `[fork]` slot. Per-skill slot tags are in `thinking-skills.md`; registry entries are in `skills-reference.md`.

Compute the runtime estimate; if it exceeds the budget by more than 10%, surface the gap with options (cut pages, drop a comp check, trim a chapter) — the author chooses which to take.

### Round 3 — Chapter authoring

Per chapter: pages and chapter-end challenges authored together. The order is natural — sometimes the chapter-end comes into focus first and shapes the staging; sometimes the pages reveal what the chapter end actually wants to ask.

**Pages.** Draft narration + dialogue at the natural length the chapter beats require. Pages are moments — one beat per page. Adapt language to the chosen grade level (read each line aloud mentally — would a real student at that grade say this?). Polish for grade-level voice and dialogue authenticity, then compose the complete renderer-facing image prompt per page (verbatim character descriptions inlined from the bible).

**Staging carries pedagogical weight, varying by skill type at the chapter end.** The image prompt is not independent of the chapter-end challenge: inferencing gates require the multiple pieces of evidence the inference combines to be visibly depictable; SEL-as-content gates require the social pattern (eye-contact, body angle, who-gets-interrupted) to be visible because dialogue can't replace what staging shows; perspective forks require all correct paths to be visually approachable; vocabulary-in-context places the cue in dialogue, not the panel. Per-skill staging notes are in `skills-reference.md`; the renderer-facing rules are in `lenses/reviewer-editor.md`.

**Chapter-end challenges.** For each chapter end, author the relevant challenge(s):

*Comprehension check* (when present): foundational skill, individual default, formative — does NOT route the story; failure does NOT trigger abrupt-end. 3-MC, 1 correct + 2 wrong (each wrong annotated with `misconception_targeted` from the per-skill registry in `skills-reference.md`). Hint after attempt 1 redirects to text or visible evidence. Coin schedule **1/0/0** (1 if correct on first attempt; 0 otherwise — the formative signal).

*Decision* (when present): thinking skill or SEL-as-content, group default, narrative routing.

- *Gate*: 3-MC, 1 correct + 2 wrong (each wrong annotated with `misconception_targeted`). Hint after attempt 1 redirects via group discussion. Coin schedule 3/1/0.
- *Perspective fork* (exactly one per story): 2 correct + 1 incorrect, OR 3 correct + 0 incorrect (per author preference). Each correct choice routes to a different post-fork chapter. For 3-correct/0-incorrect variant, use a `deliberation_prompt` (framing nudge presented when the choice lands) instead of `hint_after_attempt_1`.

Run the **mandatory elimination check** before handing back: could a student lacking the named skill arrive at the correct answer via process of elimination, narrative cues, or common sense? For *group* challenges, the bar is harder. **Resolve failures by sharpening wrong-choices, not by flagging.** This is competence, not author context.

**Track correct-answer position (A/B/C) across the story** and resolve drift toward (C) by re-shuffling. Mechanical; no flag.

When the chosen skill doesn't have a registry entry in `skills-reference.md`, draft one inline (three named misconceptions + example wrongs + one-line staging pedagogy + selection warning) and surface to the author *only* the part their context determines: does this set of misconceptions match how their students actually miss this skill? See the gap-handling protocol at the top of `skills-reference.md`.

Draft abrupt-end pages (1–2 short consequence pages, in-fiction) for any decision with at least one incorrect choice; compose their image prompts.

Write each chapter to `chapters/chapter-NN.md` with transcript, complete image prompts, and chapter-end challenges stored together. Update the runtime estimate in `polylogue.md` after each chapter.

**Optional pass: image-prompt review.** Once renders exist, present complete prompts chapter-by-chapter for the author to edit staging directly. If the author edits the bible in `polylogue.md`, run sync — regenerate inline character descriptions in all affected chapter files. Often deferrable until the renders show whether the prompts are doing what the author wanted; skipping is acceptable.

### Round 4 — Quality review

Run a full pass against the checklist in `lenses/reviewer-editor.md` and produce a pass/warn/fail report. The report has two audiences: yourself (resolve silently or by bouncing to the right lens) and the author (only on dimensions where their context determines the answer).

Cross-cutting checks at this round include elimination (every gate at group bar, every comp check), fork legitimacy, ending diff, runtime fit, bible sync, renderer-facing self-containment (mechanical scans), schema/DAG validity, position distribution, staging-pedagogy, and tone/theme/classroom-fit. The first nine resolve silently or via lens bounce-back; the last is the explicit author flag.

### Round 5 — Export

Read `polylogue.md` for metadata, art style, characters, debrief, endings. Read each `chapters/chapter-NN.md` for pages, comp checks, decisions, abrupt-ends. Run final bible sync. Validate against `schema.json`. Add `version` field (semver; v1 = "1.0.0"). Write `story.json` (or `story-vN.json` if a version exists). Print one-line summary.

## Runtime estimator

```
total_seconds =
  60                                      # setup
  + sum(pages_per_chapter × seconds_per_page)
  + sum(comp_checks × 30)                 # comp check time (read, deliberate, hint, retry, reveal)
  + sum(decisions × 90)                   # decision time (covers 2 attempts + group deliberation)
  + 120                                   # debrief
```

Default coefficients: grade 5 = 35 s/page; grade 6 = 30 s/page; grade 7 = 25 s/page; comp checks = 30 s; decisions (gates and forks) = 90 s. If `total_seconds / 60` exceeds `estimated_duration_minutes × 1.10`, surface the gap with cut options for the author to choose from.

## Bundled assets

- `schema.json` — JSON Schema for `story.json`. Used at Round 4 validation and Round 5 export.
- `thinking-skills.md` — canonical catalogue of skill names grouped by category, with slot tags. Used to validate author-named skills in Round 0 and to assign skills to slots in Round 2.
- `skills-reference.md` — per-skill **registry** (stable misconception names + medium-specific staging pedagogy + system-specific selection warnings). Not a pedagogy textbook — definitions and grade-level mastery rubrics are LLM competence and aren't written here. Includes the gap-handling protocol for skills in the catalogue without a registry entry.
- `lenses/` — concern-lens specs (see "Concern lenses" above).
- `sample-story.json` — fully-worked example. Not bundled in v1 by design (there are no existing stories at cold start; the first real story produced through the dialog becomes the sample for future versions).

## Communication style

After each round, respond to the author with three explicit sections — short, scannable, no padding:

**What changed.** One or two lines naming the artifact(s) updated and the most important shift.

**What I judged silently.** A brief list of competence calls made without asking — e.g., "shuffled correct-answer positions to A/B/A across Ch 1-3; sharpened the over-inferring wrong on Ch 2 gate after the elimination check failed first try; resolved bible drift on Ch 3 page 4." This isn't a justification; it's transparency. The author can revert any silent edit via git diff if they disagree.

**Decisions for you.** 1–3 bounded items where your context determines the right answer. Each one: what it is, why it's your call, the options. *Not a review queue.* Not "please verify my work." Specific decisions, surfaced one at a time, sized to be answered in a sentence.

Keep chat short. Durable work belongs in the files. The chapter file is the artifact you ship per chapter; `polylogue.md` is the master state.
