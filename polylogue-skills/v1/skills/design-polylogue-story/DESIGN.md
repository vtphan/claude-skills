---
name: design-polylogue-story
description: Co-design a complete graphic-novel-CYOA story package with a human author through a 9-round process. Produces a JSON story package conforming to schema.json — a Y-shaped story with chapter-end 3-MC decisions, exactly one perspective-taking fork, and divergent endings. Uses three internal sub-agents (Creative Writer, Instructional Designer, Reviewer/Editor). Use this skill when an author asks to design, write, or build a polylogue story for the student-facing app. Do NOT use for general story-writing without the polylogue/CYOA structure.
---

# design-polylogue-story

Co-design a complete graphic-novel-CYOA story package with a human author through a 9-round process. The output is a `story.json` file conforming to `schema.json` (bundled), consumed by a student-facing graphic-novel app. The skill orchestrates three internal sub-agents — Creative Writer, Instructional Designer, Reviewer/Editor — and brings polished drafts to the human author for review at every round.

This skill is structurally analogous to `concept-brief-brainstorm`: rounds, durable Markdown artifacts, human-driven decisions, LLM-suggested options. The difference is the output (structured JSON for downstream rendering) and the substantial creative writing the LLM does (story plot, dialogue, decisions, image prompts).

## Operating Principle

Always bring an artifact to the table before asking. Questions are useful only when they materially change the next artifact.

Prefer:
- Drafting a provisional version from incomplete input.
- Marking assumptions and uncertainties explicitly.
- Asking 1–3 high-leverage questions at a time.
- Advancing the artifacts after each author response.
- Moving toward a complete, schema-valid story package.

Avoid:
- Long questionnaires.
- Repeated question-only rounds.
- Blocking progress until the author fills every field.
- Treating silence as rejection.

**Default-and-confirm over ask.** When a reasonable proposal can be made from existing signal, propose it as a default the author can confirm or correct. Reserve real questions for cases where no defensible default exists *and* the answer would materially change the next artifact.

**The author always sees polished output.** Each round that produces creative content runs through the three-sub-agent pipeline (Creative Writer → Instructional Designer → Reviewer/Editor) before reaching the author. The Reviewer edits minor issues silently and flags structural ones. The author can revert silent edits via git diff on the chapter file.

**Counts are emergent, not parametric.** Chapter count and pages-per-chapter are NOT predefined. They emerge from the story arc and chapter beats, disciplined only by the runtime budget. Maintain a running runtime estimate through Rounds 3–4 and warn the author if the budget is tight or exceeded.

**Read author reactions for taste.** What they accept, reject, hesitate over, or rewrite reveals implicit criteria. Surface those criteria back when they would change a recommendation.

## Author's Job

The author's required engagement is small and well-defined:

1. Provide a seed in Round 0: story line idea, target thinking skill(s), target minutes (default 15), reading level (5/6/7).
2. React to artifacts: yes / no / mostly / not quite / change X.
3. Make or correct decisions when surfaced.
4. Approve the final package before Round 8 export.

The author is not required to fill template fields, answer questions in series, or read round files. `polylogue.md` is the master artifact; chapter files are the natural review unit.

The author can edit any Markdown file directly between rounds. The skill picks up edits on the next round.

## Loopback

When new signal damages prior work, choose loopback proportional to the damage:

- **Revise in place**: a single page, decision, or character description is wrong but the larger arc is intact — fix it directly.
- **Re-narrow** (Round 4–5): chapter outline is fine but page drafting or decisions need a new approach for one or more chapters.
- **Re-diverge** (Round 3): outline is exhausted but the concept is right — generate a fresh outline.
- **Re-frame** (Round 1–2): concept itself is wrong — return to brainstorming concepts.

Loopback can be invoked at any point.

## Artifacts

```
{slug}/
|-- polylogue.md                 # master living artifact: concept, character bible, locked art style,
|                                #   chapter list, runtime estimate, status, pointers to chapter files
|-- story.json                   # final export (Round 8 only)
|-- chapters/
|   |-- chapter-NN.md            # lazy: one per chapter, drafted in Round 4
|   `-- ...
`-- rounds/                      # lazy
    `-- round-NN-*.md            # only when material exceeds polylogue.md's scope
```

`polylogue.md` is the master artifact. It holds the concept, **the canonical character bible** (physical descriptions used by every image prompt), the locked art style, the chapter list (with one-line summaries and IDs), the running runtime estimate, and any author overrides recorded against quality gates.

**Each `chapter-NN.md` is a complete, self-contained authoring artifact** for that chapter. It contains:
- Chapter purpose + skill targeted at the chapter end.
- All pages of the chapter — full narration, full dialogues, **complete image prompt** (style + character descriptions inlined + staging).
- The full chapter-end decision — prompt, all 3 choices (with correct/wrong markers and misconception annotations), hint after attempt 1, abrupt-end pages (with their own complete image prompts), perspective-fork branches if applicable, debrief lens.

The character bible in `polylogue.md` is the single source of truth. Inline character descriptions in chapter-file image prompts are *snapshots* of the bible and must stay in sync.

Round files are lazy. Create one only when a round produces material that doesn't belong in `polylogue.md` (e.g., rejected concept variants worth preserving, alternative outline structures, scratchpad fragments).

## Invocation

- `design-polylogue-story {seed text or path to seed file}` — start a new story.
- `design-polylogue-story` — continue from current artifacts in the working directory if they exist; otherwise ask for a seed.

If the user invokes a different command but clearly asks for this workflow (e.g., "help me write a polylogue story"), use the skill.

## Round Flow

### Round 0 — Seed

Capture the author's four required inputs with low friction:

1. **Story line idea** — anywhere from a logline to a paragraph.
2. **Target thinking skill(s)** — primary skill and optionally secondary skills, from `thinking-skills.md`. If the author lists skills not in `thinking-skills.md`, surface that and ask whether to map to existing skills or extend the reference.
3. **Target minutes** — default 15 if not specified.
4. **Reading level** — 5, 6, or 7. If unclear, ask once.

Initialize `polylogue.md` with these and a `Status: Round 0 complete` marker.

If the seed is rich (multiple paragraphs, references), preserve the raw input in `rounds/round-00-seed.md`. Otherwise fold directly into `polylogue.md`.

### Round 1 — Concept

The Creative Writer agent generates 3–5 distinct story concepts grounded in the seed. Each concept includes:
- Logline.
- Main characters (sketch).
- Arc shape with a proposed location for the perspective fork.
- Tone and theme.

The Instructional Designer agent then **suggests secondary thinking skills** that the story naturally implicates, in addition to the primary skill(s) the author already named in Round 0. The goal is to surface the natural pedagogical opportunities the story shape opens up — not to enumerate every possible skill. For each suggested secondary skill, name a one-line reason ("this story has multiple characters arguing → counter-arguing fits naturally"). The author confirms, drops, or adds.

Run the full three-agent pipeline (Creative Writer → Instructional Designer → Reviewer/Editor) on the concepts and skill suggestions before presenting to the author.

The author picks one concept (or composes by combining elements) and confirms the secondary-skill set. Update `polylogue.md` with the chosen concept and the locked primary + secondary skill list.

### Round 2 — Character Bible & Locked Art Style

The Creative Writer drafts the recurring cast: each character with full physical description, role, age, clothing, distinctive features, expression baseline. The Reviewer/Editor checks that descriptions are visually unambiguous (e.g., not just "tall" but "tall, lanky, with a knot of red hair").

In parallel, the Creative Writer (with input from the Reviewer's visual eye) drafts the locked art style: rendering style, palette, lighting, line treatment.

Both are written to `polylogue.md`. The character bible becomes the single source of truth for image-prompt composition.

### Round 3 — Outline

The Creative Writer drafts a Y-shaped story arc:
- Identify chapter beats based on the arc, not a count.
- Place the perspective fork (where in the story it lands).
- Each chapter has a one-line purpose and a target thinking skill at its chapter-end decision.
- Post-fork branches diverge to different endings.

The Instructional Designer maps each gate to a target skill from `thinking-skills.md` and ensures progression makes pedagogical sense.

The Reviewer/Editor estimates runtime: pages_per_chapter × seconds_per_page (by grade level) + decisions × seconds_per_decision. Defaults: grade 5 = 35s/page, grade 6 = 30s/page, grade 7 = 25s/page, 90s per decision, plus 1 min setup + 2 min debrief. Flag if total exceeds the target minutes by more than 10%.

The chapter list (with IDs, purposes, skills targeted) is written to `polylogue.md`.

### Round 4 — Page Drafting

For each chapter (in order, but author can request any order):
- The Creative Writer drafts pages (narration + dialogue) at the natural length the chapter beats require.
- The Instructional Designer adapts language to the grade level.
- The Reviewer/Editor polishes for grade-level voice, dialogue authenticity, and narrative flow.

For each page, the Reviewer also composes the **complete image prompt** by pulling from the character bible: locked style header + verbatim character descriptions for everyone on the page + staging (pose/action/environment/mood/camera). The page is written to `chapters/chapter-NN.md` with transcript and complete image prompt stored together.

After each chapter is drafted, present it to the author for review. Update the runtime estimate in `polylogue.md`. Warn if the running total now exceeds budget.

### Round 5 — Decision Authoring

For each chapter (typically interleaved with Round 4 — chapter pages and chapter decision authored together):
- The Instructional Designer drafts the chapter-end decision: prompt, 3 choices.
  - For gates: 1 correct + 2 incorrect choices, each incorrect explicitly tied to a `misconception_targeted` from the skill's failure-mode list in `thinking-skills.md`.
  - For the perspective fork: 2 correct + 1 incorrect (default) or 3 correct (no failure mode), per author preference. Each correct choice routes to a different post-fork chapter.
- The Instructional Designer drafts the hint shown after attempt 1 wrong (must not give away the answer; should reframe or surface the relevant skill).
- The Creative Writer drafts the abrupt-end pages (1–2 short consequence pages, in-fiction) for any decision with at least one incorrect choice. The Reviewer composes their complete image prompts.
- The Instructional Designer drafts the skill-debrief panel for the abrupt-end.

**Elimination check (mandatory).** Before presenting to the author, the Reviewer/Editor runs an explicit elimination check on every decision: "Could a student who does NOT use the named thinking skill arrive at the correct choice via process of elimination, narrative cues, or common sense?" If yes, flag the decision back to the Instructional Designer for revision (typically by sharpening the misconception-targeted wrong choices). If the issue persists after revision, surface it to the author with a recommendation.

For the perspective fork specifically, also run the **fork-legitimacy check**: "Would a thoughtful person who held perspective X choose this answer?" Each correct choice must clear this bar.

### Round 6 — Image-Prompt Review

Present the complete image prompts (already composed during Round 4–5) chapter-by-chapter for author review. The author can request edits to any prompt's staging (pose, action, environment, mood, camera). Character descriptions are not edited here — they're edited via the bible.

If the author edits the bible during this round, run `/sync-prompts`: the Reviewer regenerates the inline character descriptions in all affected chapter files.

### Round 7 — Quality Review

Run the full quality-review pass and present a pass/fail report:

- **Elimination check** — per gate decision, can it be solved without the skill? (Already run in Round 5; re-run here as a final pass.)
- **Fork legitimacy** — does each correct choice at the perspective fork represent a genuinely distinct, defensible perspective?
- **Ending diff** — produce a "diff sheet" comparing the 2 (or 3) endings: are the fates, moods, and lessons drastically different? If endings feel like reskins, flag for the author.
- **Runtime fit** — does the total estimated runtime fit `metadata.estimated_duration_minutes`?
- **Image consistency** — verify every chapter file's inline character descriptions match the current bible (run sync-check).
- **Schema validity** — does the structure match `schema.json`? Are cross-cutting invariants satisfied (exactly one perspective_fork, endings count matches fork branches, all next_chapter_id references resolve)?

For each failed check, propose a fix. If the author chooses to override rather than fix, record a `metadata.author_overrides` entry with a one-line justification (warn-and-allow enforcement; never block export).

### Round 8 — Export

Compile `story.json`:
1. Read `polylogue.md` for metadata, art_style, characters, debrief.
2. Read each `chapters/chapter-NN.md` for pages, decisions, abrupt-ends.
3. Run a final sync-check (inline character descriptions match bible).
4. Validate against `schema.json`.
5. Add `version` field (semver-style; v1 = "1.0.0").
6. Run `metadata.author_overrides` validation if any are recorded.
7. Write `story.json` (or `story-vN.json` if a version exists; bump filename version stamp).
8. Write a one-line summary to the author: "Exported story-v1.json — N chapters, M pages, K decisions, Q author overrides recorded. Skill complete."

## The Three Sub-Agents

The skill invokes three registered subagents via the Agent tool. They are deployed to `.claude/agents/` (separate from this skill's folder) and named with the `polylogue-` prefix to avoid collision:

- `polylogue-creative-writer`
- `polylogue-instructional-designer`
- `polylogue-reviewer-editor`

The skill orchestrates the pipeline:

```
Creative Writer  →  Instructional Designer  →  Reviewer/Editor  →  Human Author
```

### Creative Writer (`polylogue-creative-writer`)
- **Job:** drafts story plot, character arcs, dialogue spirit, scene staging, abrupt-end consequences. Free creative latitude — not constrained by grade level (the Instructional Designer handles that downstream).
- **Inputs per invocation:** the chapter or content unit being drafted, the seed, the locked concept (after Round 1), the character bible and arc (after Rounds 2–3).
- **Outputs:** raw creative drafts in Markdown.

### Instructional Designer (`polylogue-instructional-designer`)
- **Job:** adapts language and vocabulary to the specified grade level (5/6/7); validates dialogues read naturally for that grade level; authors the 3-MC decisions (correct + 2 misconception-bearing wrongs, or fork branches); authors the hint after attempt 1; runs the elimination check on every decision.
- **Inputs per invocation:** the Creative Writer's draft + the enriched `thinking-skills.md` (bundled with this skill) + grade level.
- **Outputs:** grade-leveled draft + decision structures with misconception-targeted wrongs.

### Reviewer/Editor (`polylogue-reviewer-editor`)
- **Job:** final pre-author polish. Reads everything for grade-level fit, dialogue authenticity, decision quality (re-checks elimination), consistency with the character bible / locked art style. Composes complete image prompts. Edits minor issues silently; flags structural issues for the author. Runs sync-checks when the bible changes.
- **Inputs per invocation:** the Instructional Designer's output + the character bible + locked art style + `schema.json`.
- **Outputs:** polished chapter Markdown ready to present to the author + a list of any flagged structural issues.

The author sees only the Reviewer's output and can request a regeneration with specific feedback, which re-enters the pipeline at the appropriate role's stage.

**Deployment note:** the three subagent files live alongside this skill in the development bundle but deploy to `.claude/agents/`, not inside the skill folder. They must be registered there for the Agent tool to dispatch to them.

## Runtime Estimator

Used during Rounds 3–4 to track the running total against `metadata.estimated_duration_minutes`.

```
total_seconds =
  60                                              # setup
  + sum(page_count_per_chapter × seconds_per_page)
  + decision_count × seconds_per_decision
  + 120                                           # debrief
```

Defaults (tunable; ship with these for v1):
- `seconds_per_page` by grade level: grade 5 = 35, grade 6 = 30, grade 7 = 25.
- `seconds_per_decision` = 90 (covers 2 attempts + group deliberation).

Warn the author if `total_seconds / 60` exceeds `estimated_duration_minutes × 1.10`.

## Bundled Assets (loaded by the skill)

These files live inside the skill folder (`.claude/skills/design-polylogue-story/`) at deployment:

- `thinking-skills.md` — canonical list of available thinking-skill names, grouped by category (Comprehension/Analysis, Questioning, Evaluating Information, Reasoning & Argument, Perspective-Taking). Used by the author to pick `primary_skill` and `secondary_skills` in Round 0, and by the Instructional Designer to keep skill names consistent with the schema. Definitions, grade-level signs, and misconception patterns are NOT in this file — the LLM derives those from its own pedagogical knowledge of each named skill at the target grade level.
- `schema.json` — the JSON Schema for `story.json`. Loaded by the Reviewer/Editor (Round 7) and the export step (Round 8).
- `sample-story.json` — one fully-worked example story. Loaded by sub-agents as a few-shot reference for style and structure.

The three subagents (`polylogue-creative-writer`, `polylogue-instructional-designer`, `polylogue-reviewer-editor`) live separately at `.claude/agents/` and are dispatched via the Agent tool; the skill folder itself does not contain them.

The skill loads nothing from outside `.claude/skills/design-polylogue-story/` and `.claude/agents/`.

## Iteration Rules

On every continuation:

1. Read `polylogue.md` and any existing chapter files.
2. Identify new author signal (chat or file edits).
3. Update the current artifact before asking questions.
4. Ask at most 3 questions, only if answers would materially change the next artifact.
5. Preserve important rejected concepts/outlines/drafts in round history.
6. Keep `polylogue.md` current and concise.
7. Run sync-checks if the bible has changed.
8. Move to Round 8 export when the author signals readiness, regardless of warnings (warn-and-allow).

## Communication Style

After writing or updating files, respond to the author with:
- What artifact changed.
- The most important current shift.
- The 1–3 items the author should review or answer next.

Keep chat short. The durable work belongs in the files.
