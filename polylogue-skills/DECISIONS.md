# Polylogue Skills — Design Decisions

**Status:** `design-polylogue-story` v3 milestone snapshotted 2026-05-10. `.claude/skills/design-polylogue-story/` and `v3/skills/design-polylogue-story/` are identical at the snapshot point; `.claude/` is the live working directory for any next iteration, `v3/` is the read-only milestone archive. `v1/` and `v2/` are earlier archives (v1 milestone state and pre-v3 snapshot, respectively). **`revise-polylogue-story` is OUT OF DATE** — it's still on v1-era conventions (single-tier chapter end, six-category taxonomy, no skills-reference, no staging-pedagogy, no comp-check coin schedule, etc.) and references the old `agents/` folder name. It was included in the v3 snapshot in its current outdated state. It will be updated in a later milestone, after design-polylogue-story stabilizes. Do not invoke it for new stories until updated.

## V3 development goal (set 2026-05-09; committed 2026-05-10)

**Reduce process complexity without reducing artifact quality** (storyline, image quality, instruction). v1 produced an acceptable first story but the architecture accumulated structural overhead — number of rounds, role-switching ceremony, stress-test-finding rules, pedagogy-textbook content in skills-reference. v3 compressed each of these while preserving the load-bearing pieces (renderer-facing rules, two-tier chapter end, Y-shape with one fork, position distribution, misconception specificity, medium-specific staging pedagogy).

Concrete simplifications committed in v3:

1. **Rounds 2 and 3 merged** (cast + art style + outline as one round). The cast and the arc inform each other; the author no longer waits between them.
2. **Parallel "Creative Writer with Reviewer's visual eye" framing dropped.** Art style is an author taste decision — the model proposes defaults, the author confirms; renderer-facing verbatim verification is downstream when image prompts compose.
3. **Rounds 4 + 5 acknowledged as one round** (chapter authoring: pages + chapter-end challenges per chapter). They were already de facto merged; v3 calls it one round.
4. **Round 6 (image-prompt review) demoted out of the numbered flow** to an optional pass when renders exist.
5. **Three-agents-as-distinct-stages ceremony reduced.** SKILL.md describes round outputs directly; the lens specs (formerly `agents/`, now `lenses/`) describe what each concern attends to, not pipeline stages to formally enter and exit.
6. **Stress-test findings folded into the registry**, not duplicated as rules across SKILL.md and the lens specs. Position-distribution, staging-pedagogy, and selection warnings live as per-skill or shared notes in `skills-reference.md` rather than as rule stacks elsewhere.
7. **`agents/` folder renamed to `lenses/`** to match the v3 concern-lens framing. Lens files no longer carry agent-style `name:` frontmatter; they're documentation, not invokable subagents.
8. **`skills-reference.md` reformulated as a strategic registry** (Section 7), not a per-skill pedagogy textbook. See Section 7 for the new format. This removes pedagogy content the LLM already brings (definitions, mastery rubrics, lecture-style authoring notes) and keeps only what coordination and medium specificity require (misconception name registry, staging pedagogy, selection warnings).
9. **Sub-principle added to Section 2.2 — Decisions, not verification.** The author's role in the iterative dialog is *decisive* (taste, scope, classroom context), not *verificative* (QA on LLM output). The LLM resolves competence calls silently; flags surface bounded decisions where the author's privileged context determines the right answer. Round-end communication adopts a three-section format: *what changed*, *what I judged silently*, *decisions for you*.

Schema elaboration (the second structural tension flagged in the v3 plan): not addressed in v3. Schema still distinguishes `comp_check` / `decision`, `challenge_type`, `deliberation_prompt`. Per the original framing, schema unification only earns its place if elaboration gets in the way of authoring — it didn't, in v3.

**Last updated:** 2026-05-10
**Primary goal right now:** deliver **acceptable v1 stories**. Avoid over-engineering. Add complexity only when it demonstrably improves output on a real story.

This document is the canonical record of design choices that emerged from extended design discussion. It exists so future conversations can pick up the architecture without re-deriving it. Decisions here are committed but not yet reflected in skill files.

---

## 1. Audience and setting

- **Target audience:** grade 5, 6, or 7 students.
- **Reading mode:** each student reads on their own laptop (individual reading of the comic).
- **Group mode:** students can ask each other questions and discuss between/at decision points. The polylogue is partly the dialogue inside the comic and partly the *students themselves* talking to each other when they hit a decision.
- **Practical realism:** "individual" challenges may receive peer help anyway. That's acceptable. The individual/group tag signals authoring intent and framing, not enforcement.

## 2. Operating principles

Two principles shape how the skill operates, distinct from the architectural decisions in later sections.

### 2.1 Briefing, not recipe

The polylogue skills are designed to be carried out by a **capable LLM** (Opus 4.7-class). They are **briefings for a capable colleague, not recipes for a procedural worker.**

This shapes what belongs in the skill files and what doesn't.

**Skill files load-bear on what only the skill file can provide:**

- Audience and setting (who this is for, how it's consumed).
- The taxonomy with worked examples — canonical skill names plus mastery signs and failure modes the model otherwise can't access consistently across stories.
- The schema (output format constrained by downstream consumption).
- Downstream-system constraints (the renderer's mechanical rules, the reader app's dialog-column rendering).
- The goals the work is trying to achieve (engagement via CYOA, foundational-reader support, perspective-taking).

**Skill files should not try to encode what the model already brings:**

- Step-by-step procedures for tasks the model can sequence on its own.
- Micro-prescriptions of format (average sentence-length targets, exact page lengths, prescribed concept counts as rigid rules).
- Mechanical validation algorithms when an articulated *question* would do — e.g., the elimination check is better stated as the question to ask ("could a student without the skill still elimination-guess this?") than as a procedure to execute.
- Anything that flattens craft judgment.

**Slot tags and other taxonomy signals are affordances, not rules.** A skill tagged `[gate]` *can* fit a gate slot; the model decides per-chapter whether the staged scene supports it. The taxonomy widens the model's options; it doesn't restrict its judgment.

### 2.2 Iterative dialog with the author (the cold-start compensator)

The skill operates from a **cold start** — there are no existing sample stories the LLM can use as few-shot ground truth. In compensation, the design process is **structured as iterative dialog between LLM and human author**, with distinct roles:

- **LLM**: creative, generative — brings concrete options the author can react to.
- **Human author**: decisive — holds context, scope, and taste-making standards, much of which is implicit and never written into any document.
- **Iteration substitutes for examples** — the author's reactions across multiple rounds *encode taste into the artifact*, even when those standards are never articulated explicitly.

This principle is load-bearing because the cold start is real. The skill must work without a worked sample story; the dialog is what closes the loop.

**What this means in practice:**

- **The round flow is the engine of the collaboration**, not paperwork. Each round = one cycle of propose / react / revise. (v3 collapsed nine rounds to six; the propose/react/revise rhythm is unchanged.)
- **"Default-and-confirm over ask" is right** precisely because abstract questions don't elicit implicit knowledge well; concrete artifacts do.
- **First-draft offness is expected, not a failure mode.** The author's correction is the *signal the system is designed to elicit*. Loopback (revise-in-place / re-narrow / re-diverge / re-frame) is the natural rhythm of dialog, not a recovery mechanism.
- **The polish/renderer lens's role** is to bring clean drafts for the author to react to, not to pre-judge whether the draft is "right" for this story — that's the author's call.
- **Different authors produce different stories from the same seed.** This is the personalization mechanism, not noise.
- **Cold-start cost is concentrated in the first story.** Once the author has produced one story through this dialog, that story becomes a sample for future runs (when the author chooses to share it).

#### Sub-principle: Decisions, not verification (set 2026-05-10)

The author's role is **decisive**, not **verificative**. The author holds context the LLM doesn't — taste, scope, *these* students, *this* curriculum, sensitivities, theme alignment. The LLM holds craft and mechanical competence — schema validity, grade-level adaptation, prose polish, renderer-facing self-containment, misconception specificity given the registry, position distribution, elimination-check resolution, bible sync.

The line between silent resolution and explicit attention is **"do I have privileged context to decide this?"** — *not* "does this change meaning?"

- **Resolve silently:** craft and mechanical calls. Iterate to fix; don't ask the author to verify your work. Examples: elimination-check failures (sharpen wrongs), schema invariants, bible drift, renderer-facing rule violations, position-distribution shuffles, prose polish, grade-level adaptation.
- **Flag specifically:** bounded decisions where the author's context determines the right answer. Each flag names *what* is being decided and *why it's their call*. Examples: tone fit for the author's classroom, theme alignment with their curriculum, character/scene appropriateness, fork-branch legitimacy as the author judges it, misconception fit to *their* students' actual misreads, sensitivity calls.

If a borderline case is unclear: ask *"would the author know something here I don't?"* If yes, flag. If no, resolve.

**Why this is load-bearing.** The author's attention is the scarce resource. A "review my work" posture trains the author to disengage (nothing requires their judgment) or burn time on QA (which the LLM is competent at). A "decisions, not verification" posture concentrates attention on the dimensions where authoring actually depends on the author. This sharpens the iterative-dialog mechanism: corrections happen on the dimensions that need them, and the LLM's competent calls don't get bogged down in verification.

**Consequence for round-end communication.** Each round ends with three sections: *what changed* (artifact summary), *what I judged silently* (transparency on competence calls — author can revert via git diff), *decisions for you* (1–3 bounded items, sized to be answered in a sentence).

**Consequence for the per-skill registry (Section 7):** the registry replaces a per-skill pedagogy chapter with a tight registry of stable misconception names + medium-specific staging pedagogy + system-specific selection warnings. Calibration on what specific wrong-choices work in the wild emerges from author reactions during iteration, not from pre-baked worked examples. The cold-start argument for worked examples (v1's framing) was overcautious — under decisions-not-verification, iteration *is* calibration.

### Relationship to the simplicity preference (Section 10)

The two principles above and the simplicity preference all pull toward restraint, in different dimensions:

- **Simplicity** restrains *us* — don't build elaborate architecture.
- **Briefing-not-recipe** restrains the *skill text* — don't over-specify the model's thinking.
- **Iterative dialog** acknowledges that *understanding emerges through collaboration* — don't expect first drafts to be right or all standards to be articulable upfront.

When revising existing skill files, look for procedural lists and numerical micro-prescriptions to replace with orientation that conveys intent. Look for places where the round flow can be described as collaborative dialog rather than as sequential checkpoints. Trust the author to bring what isn't in the documents.

## 3. CYOA structure (preserved from current skill)

- The graphic-novel CYOA format is load-bearing. It is hypothesized to (a) attract students — practical engagement requirement — and (b) afford perspective-taking through branching consequence.
- The story remains **Y-shaped**: linear (with optional gates) up to one perspective fork, then divergent branches to multiple endings.
- **Exactly one perspective fork per story.** This invariant is preserved.

## 4. Two-tier chapter end

A chapter end has 0, 1, or 2 challenges:

- **Comprehension check** — foundational reading skill, **individual** challenge by default, **formative**. Does NOT route the story; failure does NOT trigger abrupt-end. Wrong on attempt 1 → hint → try again. Wrong on attempt 2 → reveal answer with brief explanation, no coins for the check, story continues.
- **Decision** — thinking skill (or SEL-as-content skill), **group** challenge by default, **narrative routing**. Either a gate (1 correct → continue, 2 wrong → abrupt-end) or, exactly once per story, a perspective fork (multi-correct → divergent paths).

A chapter can have either, both, or (rarely) neither. The story's dramatic shape dictates which:

- Early chapters often comprehension-only as the world builds.
- Middle chapters add gates as conflict escalates.
- The fork sits at the dramatic pivot.
- Branches play out consequences, often a mix.

**Why two-tier:** focus-group input from teachers — many grade 5–7 students still need foundational reading support. A pure thinking-skills intervention creates friction for them. The comprehension check is a foothold and a diagnostic; it tells the room *which* skill a struggling student is stuck on without punishing them narratively.

**Why comprehension checks don't route:** punishing a student narratively for missing a vocabulary word in context defeats the support we're trying to give. Comprehension checks teach; they don't gate the story.

## 5. Three skill categories (replaces current six-category `thinking-skills.md`)

### Foundational Reading Skills

Vocabulary in context, identifying main idea/gist, summarizing, sequencing, identifying explicit cause-and-effect, tracking character/setting, recognizing problem-solution structure. (Pruned from the current "Basic Reading Comprehension" entries; junk like reading fluency, decoding, and "thinking for themselves" is dropped.)

- Slot tag: `[comprehension_check]`
- Default challenge type: **individual**

### Thinking Skills

Inferencing, distinguishing fact from opinion, recognizing assumptions, counter-arguing, spotting bias, evaluating sources, considering multiple viewpoints, identifying author's purpose, recognizing point of view, separating emotion from analysis, distinguishing claim/evidence/reasoning, predicting from textual evidence, synthesizing across chapters or scenes. Lumped fallacies split into three: overgeneralization, either/or thinking, circular reasoning.

- Slot tag: `[gate]` for most; `[fork]` for the perspective-taking subcategory (considering multiple viewpoints, identifying point of view, separating emotion from analysis, etc.)
- Default challenge type: **group**

### Social-Emotional Skills

SEL splits into two kinds with different roles in the polylogue:

**SEL-as-content** — when a chapter scene depicts a social moment (someone interrupting, dismissing, changing their mind, building on another's idea), the chapter end can ask the group to identify or evaluate what just happened socially. These are first-class taxonomy entries with standard slot tags. Examples: *recognizing when a peer is dismissed*, *acknowledging when one has changed one's mind*, *recognizing when emotion is overriding reasoning*, *building on someone else's idea*.

- Slot tag: `[gate]` or `[comprehension_check]` (when the social moment is observable in the staged scene), or `[fork]` (mind-change moments, willingness to revise).
- Always group when in a challenge slot.

**SEL-as-process** — skills that are *performed* during discussion rather than *selected* on a 3-MC: active listening, disagreeing respectfully, taking turns, voicing dissent. These don't admit gates by their nature. They are NOT formal taxonomy entries. Instead they live as universal authoring guidance: the hint after attempt 1 on any group challenge can invite SEL behaviors ("Have you heard from everyone in your group?"; "Try arguing the other side before you re-vote"). This guidance lives in the Instructional Designer's spec, not in the skill taxonomy.

### Removed

**Dispositional skills** (intellectual curiosity, persistence, "thinking for yourself") are removed from the taxonomy. They don't admit 3-MC gates and they emerge from doing the work. They show up implicitly via character behavior and can be acknowledged in the debrief, but are not formal taxonomy entries.

The earlier `[modeled]` slot tag is also removed. It was a category for "things teachers care about that don't fit our system," which conflated two different things — SEL-as-content (which does fit, as standard slot tags) and SEL-as-process (which lives as authoring guidance, not a skill entry).

## 6. Slot-to-skill mapping

| Slot | Skills that can fill it | Routing | Challenge type | Cardinality per story |
|---|---|---|---|---|
| `[comprehension_check]` | Foundational; occasional SEL-as-content (when scene observable) | None (formative) | Individual default | 0–N (most chapters have one) |
| `[gate]` | Thinking (non-perspective); SEL-as-content | Binary (continue or abrupt-end) | Group default | 0–N |
| `[fork]` | Thinking (perspective-taking); SEL-as-content (mind-change) | Multi-branch | Group always | Exactly 1 |

Slot tags are *affordances* — they signal which slots a skill can naturally fill, not where it must go. The Instructional Designer reads the staged chapter scene and decides whether the chapter end calls for a challenge in any slot, and which skill from the available pool best fits that slot given what the scene actually depicts.

## 7. Per-skill registry — `skills-reference.md` (revised 2026-05-10)

`thinking-skills.md` is the **catalogue** — name + slot tag, used to validate author-named skills at Round 0 and to assign skills to slots at Round 2. By itself it's insufficient: telling the LLM to "derive misconceptions from your own pedagogical knowledge" produces inconsistent, generic wrong choices across stories. The cross-story `misconception_targeted` field needs stable names; the medium has specific staging-pedagogy that isn't generic LLM knowledge.

`skills-reference.md` is a tight **registry** providing what the LLM cannot derive on its own:

1. **Slot tag and default challenge type** (echoed from the catalogue for self-contained reading).
2. **Misconception name registry** — three named failure modes per skill in `<adjective>-<concept>` form, used as the canonical values for `misconception_targeted` in `story.json`. One-line description per name + one example wrong-choice in MC voice.
3. **Staging pedagogy** — one-paragraph guidance on what the panel needs to show when this skill is at the chapter end. Medium-specific (the graphic-novel CYOA panel is doing pedagogical work).
4. **Selection warning** — one-line guidance on the shape of scene this skill needs. Prevents the recurring mistake of forcing a slot a chapter doesn't naturally support.
5. **Hint shape** — one-line note on how the post-attempt-1 hint should redirect (text-anchored / discussion-prompting / framing-nudge).

What the registry **does not** include:

- Definitions (the LLM knows what vocabulary-in-context, inferencing, considering multiple viewpoints are).
- Mastery rubrics across grade levels (broad strokes are derivable; one-line bar-shift notes appear only when the bar shifts in a non-obvious way for that skill).
- Standalone worked micro-examples with mastery response and per-failure-mode response. Under decisions-not-verification, calibration emerges from author reactions during iteration; pre-baked worked examples create over-anchoring risk and duplicate the iteration mechanism.
- Authoring-notes lectures on general pedagogy.

**Gap-handling protocol.** When an author lands on a skill in the catalogue without a registry entry, the pedagogy lens drafts one inline (~5 lines) and surfaces only the part where the author's context determines the answer (typically: *"do these failure modes match how your students miss this skill?"*). The author confirms or adjusts; the entry can be added permanently to `skills-reference.md` if they want.

**Coverage.** v1 ships 4 entries (vocabulary-in-context, inferencing, considering multiple viewpoints, recognizing when a peer is dismissed) chosen to validate the template across all three categories and all three slot types. The remaining ~26 skills in the catalogue are usable via the gap-handling protocol; expanding the registry is incremental as real stories surface needs.

## 8. Individual vs. group challenge tag

Each challenge carries `challenge_type: individual | group`.

Defaults at slot level:
- Comprehension check → individual
- Decision (gate) → group
- Decision (perspective_fork) → group always

Author can override per-challenge.

Affects three things:

- **Prompt phrasing** — "What do you think?" vs. "What does your group think?"
- **Hint phrasing after attempt 1** — text-anchored ("Reread the moment when…") vs. discussion-prompting ("Has anyone in your group noticed something different?")
- **Elimination check bar** — individual: could one student lacking the skill reach the correct answer? Group (the harder bar): could a *group* of students lacking the skill collectively reach the correct answer through discussion? Discussion narrows down options, so group challenges need sharper wrongs.

## 9. Schema changes (sketch)

```
chapter:
  id, purpose, pages
  comprehension_check (optional):
    skill, challenge_type ("individual" default), prompt, choices, hint_after_attempt_1, ...
  decision (optional):
    skill, challenge_type ("group" default), kind ("gate" | "perspective_fork"),
    prompt, choices, hint_after_attempt_1, abrupt_end (if gate), ...
  next_chapter_id (required unless this chapter has perspective_fork or is terminal)
```

Cross-cutting invariants preserved: exactly one `perspective_fork`, `endings.length` equals number of correct choices in the fork, every `next_chapter_id` resolves.

New invariants:
- Every `comprehension_check.skill` is a Foundational skill (or occasional SEL-as-content with `[comprehension_check]` tag).
- Every `decision.skill` is a Thinking skill or SEL-as-content skill.
- `comprehension_check` has no `abrupt_end` and does not route.

**Additional schema fields surfaced by the v1 run-through (see Section 12 step 4 finding):**
- `deliberation_prompt` (optional on `decision`) — framing nudge surfaced *before* the choice; required for 3-correct/0-incorrect forks, optional elsewhere.
- Runtime coefficient: `comprehension_check` = ~30s; preserve `decision` = 90s and per-grade page weights.
- `attempts_allowed` semantics: stay locked at 2; for all-correct forks, second attempt functions as "change your mind" rather than retry-after-wrong.

## 10. What's deferred for v1 (avoid over-engineering)

These are real future improvements but not load-bearing for shipping acceptable stories:

- **Multi-tagging skills** that work in multiple slots. v1: each skill carries one primary slot tag.
- **Comprehensive SEL skill set** in the reference. v1 ships a small starter set of 2–3 SEL-as-content skills (e.g., recognizing when a peer is dismissed, acknowledging when one has changed one's mind) with standard slot tags. The full SEL coverage is deferred until v1 produces a real story and we see which SEL skills the medium most naturally invites.
- **Anti-pattern section** per skill in the reference. Useful but skip for v1.
- **Multi-skill chapter-end** (a chapter that exercises several thinking skills at once). Stay one-skill-per-challenge.
- **Adaptive runtime** tuned per group's reading speed.
- **Author-tunable coin schedule.** Stay with locked 3/1/0 for decisions; comprehension checks use **1/0/0** (1 coin if correct on first attempt; 0 if correct on second attempt; 0 if failed). The zero on second attempt is the formative signal — the hint helped you reach the answer, you don't get the reward, but the story continues unchanged. Adjust during first real story if needed.
- **Component-moves section** in the per-skill reference. Useful for sophisticated reasoning but not required for v1; can be deferred or compressed into the definition + mastery signs.
- **Detailed individual-vs-group authoring guidance** beyond defaults. v1 can use the slot defaults uniformly.

## 11. What stays unchanged

- The three-stage pipeline (Creative Writer → Instructional Designer → Reviewer/Editor).
- Y-shape topology with one perspective fork.
- 3-MC + 2 attempts on every challenge.
- Locked 3/1/0 coin schedule on decisions.
- Renderer-facing image-prompt rules (these come from outside the model — keep them strict).
- Round flow (R0 seed → R8 export), with a small update at R5 to author both comprehension-check and decision per chapter end.
- Loopback machinery (revise-in-place / re-narrow / re-diverge / re-frame).
- Warn-and-allow Round 7 enforcement.

## 12. Recommended v1 implementation order

When we commit to making changes, the smallest set that closes the load-bearing gaps:

1. **Restructure `thinking-skills.md`** into the three-category taxonomy with slot tags. Add the missing high-value entries (sequencing, predicting, synthesizing across scenes, split fallacies, the starter SEL-as-content skills). Drop the junk.
2. **Draft four stress-test per-skill reference entries** to validate the template across all three skill categories and all slot types:
   - `vocabulary in context` (Foundational, comprehension_check, individual default)
   - `inferencing` (Thinking, gate, group default)
   - `considering multiple viewpoints` (Thinking, fork, group always)
   - `recognizing when a peer is dismissed` (SEL-as-content, gate, group always)

   **These reference entries are load-bearing at cold start (Section 2.2).** With no sample stories available as few-shot, the worked micro-examples and failure-mode example wrong-choices in each entry are the only concrete pedagogical ground-truth the LLM has. Treat them with extra care — they're doing the work a sample story would otherwise do, scoped to the skill rather than the story.
3. **Update the schema** to support optional `comprehension_check`, optional `decision`, chapter-level `next_chapter_id`, and `challenge_type` tagging.
4. **Update SKILL.md and agent specs** to reference the new taxonomy and reference, the two-tier chapter end, and the group-bar elimination check. **In the same pass, apply both operating principles (Section 2):**
    - *Briefing-not-recipe (2.1):* replace procedural step-lists with orientation that conveys intent; replace numerical micro-prescriptions (avg sentence-length targets, prescribed concept counts, mechanical validation checks) with the questions and goals they were standing in for. Keep the schema, taxonomy, and renderer-facing rules — those are constraints from outside the model.
    - *Iterative dialog (2.2):* describe the round flow as collaborative dialog rather than as sequential checkpoints. Frame loopback as the natural rhythm of dialog, not a recovery mechanism. Treat first-draft offness as the expected case; the author's correction is the signal the system is designed to elicit.
    - *Round 1 output (v1 stress-test finding, 2026-05-09):* concept proposals must include per-concept *skills-targeted* analysis and concrete *teaching-moment* sketches (handful of challenges per concept — comp checks, gates, fork) alongside logline/cast/arc/tone/theme. The author's selection is pedagogical, not just narrative; without this analysis, choosing between concepts is uninformed on the dimension that matters most for a teaching tool.
    - *Image staging and chapter-end challenge correlation (v1 stress-test finding, 2026-05-09):* page staging and chapter-end challenges are not independent — the panel carries pedagogical weight that varies by skill type. **Inferencing gates:** staging must depict the evidence the correct inference combines (body language, environment, action) without editorializing through composition (no "this character is sad" framing — the camera shouldn't make the inference for the reader). **SEL-as-content gates:** the panel is the primary evidence — dialogue and narration cannot replace what visible staging shows about who looks at whom, whose body turns away, whose moment gets interrupted. **Perspective forks:** staging must keep all correct paths visually approachable (no compositional tilt toward one path). **Vocabulary-in-context:** image is secondary; the cue lives in the dialogue and surrounding text. When the Reviewer/Editor spec is updated, add a staging-for-pedagogy section alongside renderer-facing rules; when the per-skill reference is extended, add per-skill staging notes alongside authoring notes.
    - *Correct-answer position randomization (v1 stress-test finding, 2026-05-09):* across the first three chapters drafted, the correct answer landed at position (C) every time — purely by authoring habit (correct-after-wrongs reads as a natural climax in prose, and authors writing in chronological wrong-then-right order will gravitate to (C) without noticing). With 3-MC + 2 attempts already conferring ~67% naive-guess success, a deterministic correct-position pattern collapses the gate further: students who play more than one story will pick up the pattern and bypass the skill check. Going forward: distribute the correct answer's position roughly evenly across A/B/C within a story (target ≥1 of each across the story's challenges); within a chapter that has both a comp check and a gate, the two should not share the same correct position. The Instructional Designer is responsible for tracking this across the story; the Reviewer/Editor's Round 7 quality review should add a "position distribution" check.
    - *Renderer-facing mechanical checks (v1 stress-test finding, 2026-05-09):* during the first end-to-end story run (Round 7 review of `stories/three-athletes`), four kinds of renderer-facing violations occurred during enthusiastic drafting — (1) cross-page references ("same description as Page 1"); (2) cross-chapter comparatives ("more relaxed than at the start of Chapter 4"); (3) negative-form instructions referencing alternatives the renderer doesn't know ("no dramatic lighting on Minh — no rescue framing"); (4) bold-printed editorial inside `[Page staging]` directed at a future reviewer rather than the image generator ("Critical: this panel must give all three approachable paths roughly equal visual weight"). When the Reviewer/Editor spec is updated, the self-containment check should explicitly include grep-style scans for these patterns: phrases like "same as Page X", "as in Chapter Y"; comparative-to-baseline phrasings ("more X than usual", "X-er than at"); negative-instruction lists ("no X, no Y, no Z" addressed to the renderer); and bold-printed editorial inside `[Page staging]` blocks. These are mechanical and can be caught deterministically by text inspection — the existing renderer-facing rules in the Reviewer/Editor spec describe the principle, but adding the mechanical scans as part of the check converts principle into practice.
    - *Schema additions from first run-through (v1 stress-test finding, 2026-05-09):* the schema sketch in Section 9 needs three additions surfaced during `stories/three-athletes`. These should land in Section 12 step 3 (schema update) when it's taken on:
      **(a) Comprehension check runtime coefficient.** Comp checks add ~30 seconds to a chapter's runtime (covers reading the question, group deliberation, hint after attempt 1, retry, answer reveal). Update the runtime estimator: `total_seconds = 60 (setup) + sum(pages × seconds_per_page_by_grade) + sum(comp_checks × 30) + sum(decisions × 90) + 120 (debrief)`. The existing estimator only counted pages and decisions.
      **(b) `deliberation_prompt` field on `decision`.** Distinct from `hint_after_attempt_1`, surfaced *before* the choice lands rather than after a wrong attempt. Required for the 3-correct/0-incorrect perspective-fork variant (where there is no wrong attempt to hint after) — gives the group a framing nudge to deliberate before voting. Optional for gates and 2-correct/1-incorrect forks (where it can complement the post-wrong hint).
      **(c) `attempts_allowed` semantics for all-correct forks.** Schema locks `attempts_allowed` at 2 across all decisions. For the 3-correct/0-incorrect fork variant, the second attempt is structurally a "change-your-mind" opportunity rather than a retry-after-wrong. Recommendation: keep locked at 2 (consistent UX, allows re-vote after group deliberation) but document the variant semantics in the field description.
5. **Mirror changes in `revise-polylogue-story`** so revision matches design.

**No `sample-story.json` is built up-front.** A pre-built synthetic example would hard-code the LLM's first guess as canonical, which defeats the dialog principle (Section 2.2). Instead: the first real story produced by the skill — through one full pass of the iterative dialog with a real author — becomes the sample. Subsequent runs of the skill can use it as a few-shot.

After v1 produces its first real story end-to-end, evaluate which deferred items (full SEL section, multi-tagging, anti-patterns, component moves) earn their place based on observed failure modes — and consider including the first story as a bundled sample for v2.

## 13. Files affected when implementing

All changes land in `.claude/skills/` (the working folder). `v1/` and `v2/` are read-only archives — do not touch. When v1 is ready to ship, snapshot `.claude/` to `v3/` as the next archive.

- `thinking-skills.md` → restructured into three-category taxonomy with slot tags
- `skills-reference.md` (new) → per-skill reference, replaces name-only file
- `schema.json` → comprehension_check, decision optional, challenge_type, chapter-level next_chapter_id
- `SKILL.md` → Round 5 update; reference to skills-reference.md; briefing-not-recipe pass
- `lenses/instructional-designer.md` (was `agents/instructional-designer.md` in v2; renamed in v3 to match the concern-lens framing) → per-skill registry usage, group-bar elimination check, comprehension-check authoring, SEL-as-process hint guidance, gap-handling protocol, briefing-not-recipe + decisions-not-verification pass
- `lenses/creative-writer.md` (renamed in v3) → minor update for comprehension-only chapter framing, briefing-not-recipe pass
- `lenses/reviewer-editor.md` (renamed in v3) → group-bar elimination check, comprehension-check schema validation, silent-edit/flag line redrawn around competence-vs-context, briefing-not-recipe + decisions-not-verification pass
- **`.claude/skills/revise-polylogue-story/` — currently OUT OF DATE.** Still on v1-era conventions. The same set of changes will be echoed there in a later milestone, after `design-polylogue-story` finalizes in v3. Until then, it should not be used for new stories.

`sample-story.json` is intentionally NOT built up-front (see Section 12). The first real story produced by the v1 skill becomes the sample asset for v2.
