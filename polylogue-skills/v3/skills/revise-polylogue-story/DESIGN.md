---
name: revise-polylogue-story
description: Design rationale for the revise-polylogue-story skill. Verbose, development-time only — not loaded at runtime. Captures why the skill operates on two calibration axes, why the conversation is brainstorm-shaped on the outside and authoring-shaped on the inside, why opportunity examples are the load-bearing artifact, why the asymmetric constraints (elimination floor for less-visible, heavy-handedness ceiling for more-visible) are non-negotiable, why the MVP is operator-mediated rather than direct-to-teacher, and what stays touchable vs. locked in scope.
---

# revise-polylogue-story — Design Document

This is the verbose design rationale for the `revise-polylogue-story` skill. It is a development reference. It is not loaded at runtime. The runtime contract is in `SKILL.md`; the few-shot reference is in `sample-revision-session.md`.

This skill exists because `design-polylogue-story` produces *one* version of a story, but classrooms are not one classroom. A grade-7 perspective-taking story drafted in the authoring tool may need a grade-5 reading shift before it reaches a classroom of grade-5 students; a story whose thinking moves are sharp and visible may need to be softened for a class that has already been taught the named skill and is ready to do the work without scaffolding. The library exists to amortize authoring cost across many classrooms — but only if classrooms can adapt the library asset to their actual students. This skill is the adaptation layer.

The skill is structurally analogous to `design-polylogue-story` in that it orchestrates the same three sub-agents (Creative Writer, Instructional Designer, Reviewer/Editor) and produces deliverables that conform to the same `schema.json`. It differs in two ways. First, the work is calibration, not authoring — chapter structure, characters, art style, fork shape, and target skills are preserved. Second, the conversational shape is brainstorm-style with a teacher (or in MVP, an operator advocating for a teacher) rather than round-by-round with an author. The teacher does not drive a 9-round process; they react to a single brainstorm pass and approve a plan.

## The two calibration axes

Two axes, and only two.

- **Reading level** — grade 5, 6, or 7. The same canonical levels as the authoring tool. Reading level adjusts narration prose, dialogue word choice, decision-prompt language, hint text, and debrief prose. It does not adjust *what the chapters teach*.
- **Skill visibility** — *more visible*, *as authored*, *less visible*. Adjusts how strongly the chapter's thinking move is foregrounded — how sharp the misconception pulls land, how specifically hints name the cognitive operation, whether the per-chapter debrief explicitly calls out the targeted skill or describes it in story terms.

Why these two and only these two.

Reading level is the single biggest classroom-mismatch factor — teachers commonly say "this is great but my kids are a year ahead/behind" and the language is the issue, not the content. It is also the axis where the existing authoring pipeline already has machinery (the Instructional Designer's grade-level adaptation work in Round 4 of `design-polylogue-story`); the revision skill can dispatch the same agent for the same job at revision time.

Skill visibility is the second-biggest classroom-mismatch factor, and unlike reading level it does not have a knob in the authoring tool. A teacher whose class has been taught "perspective-taking" all year wants the thinking moves to be subtle so the kids do the work; a teacher whose class is meeting the skill for the first time wants the moves named and amplified. The authored story sits at one point on this axis. Without a calibration tool, the teacher has only "use it as is" or "don't use it" — there's no middle ground.

We considered other axes — runtime, character voice, ending count, fork branching, skill substitution — and rejected them for the MVP. Runtime drifts naturally from reading-level shifts (the runtime estimator recomputes), so it doesn't need a separate axis. Character voice belongs to the authoring tool: a teacher who wants different characters needs a different story, not a revised one. Ending count and fork branching are structural — changing them is re-authoring, not revision. Skill substitution is the most tempting future axis but is also re-authoring: a chapter targeting "reading between the lines" was *built* around that skill at the page level, and substituting "comparing and contrasting" would require redrafting nearly every page. We left it as a Phase-2 candidate but explicitly out of MVP scope.

The two-axis constraint is deliberate. A larger axis space gives the teacher more knobs and gives the skill more rope to hang itself. With two axes, every diagnostic finding clusters cleanly into one of two themes; every refusal pattern points at the same small set of locked fields; every quality check applies in the same shape regardless of which axis was touched. The simplicity of the axis space is a feature.

## Brainstorm-style outside, authoring-quality inside

The conversation a teacher has with the skill is brainstorm-shaped. The skill walks in with concrete opportunities, the teacher reacts coarsely, the skill refines, and a plan emerges. The teacher does not see rounds, sub-agents, elimination checks, or quality gates. They see "here are 3-5 things I noticed; here are examples of how each could go; what matters for your class?"

Underneath, the skill is doing authoring-grade work. The Creative Writer drafts replacement language at full creative quality. The Instructional Designer adapts to grade level and runs the elimination check on every adjusted decision. The Reviewer/Editor polishes for grade-level voice, composes/syncs image prompts when needed, and runs the Round-7-equivalent quality pass before any deliverable is written. These are the same agents and the same machinery that produced the story in the first place — that is non-negotiable, because revision can break what authoring carefully constructed (the elimination check in particular).

The asymmetry between conversation and machinery is the design. A teacher does not have time or context to follow a 9-round authoring conversation. They have the time and context to look at a few before/after examples and say "yes, no, lighter, sharper, missed chapter X." The skill absorbs the complexity so the teacher doesn't have to.

This is also the reason the conversation is not reducible to a form. A form ("pick a grade level, pick a visibility level, click apply") would skip the brainstorm phase, but the brainstorm phase is where the teacher's classroom context enters the loop. The skill cannot infer from the story file alone whether the chapter-3 inference work is too hard or too easy for the teacher's specific kids; only the teacher knows. The brainstorm exposes the dimensions of variation through examples and lets the teacher's reactions reveal their criteria.

## Examples-first, with a brainstorm loop

The skill's load-bearing artifact in Phase 1 is the set of concrete before/after examples for each opportunity theme. A teacher cannot react to "I'll make chapter 3 more visible" — that's an abstract operation with no surface for judgment. They can react to "in chapter 3, the wrong choice (a) currently reads *'He's making a joke to be funny, and the joke just happened to land badly.'* It could become *'He's just goofing off — Oz is always doing voices and this one missed.'*" Now they can say "yes, that's stronger" or "no, the original was better" or "the new one is too obvious — try something between those two."

Examples work because they convert an axis-level decision into a sentence-level decision. They make the cost of each move visible. They reveal the dimensions of variation the teacher cares about, which the skill then accumulates into a sharper interpretation of the teacher's criteria for subsequent iterations.

The loop that wraps the examples is structured around four kinds of teacher signal:

- *Approval* — the example is right, apply the theme. Move to Apply phase if the rest of the plan is approved.
- *Calibration* — the theme is right but the intensity is off. Show one or two examples at the corrected intensity. The skill's interpretation of "what the teacher wants" sharpens.
- *Redirection* — the theme is wrong, but a different theme is right. Drop this theme; possibly add a new one based on the teacher's framing.
- *Re-frame* — the calibration axis itself is wrong. Switch axes and re-scan.

The four loopback flavors mirror the authoring skill's loopback (revise-in-place / re-narrow / re-diverge / re-frame), with the same proportionality discipline: the loopback should be the smallest one that absorbs the new signal.

We chose three to five themes per first iteration, with one or two examples per theme, after considering shorter (one big theme at a time) and longer (a comprehensive opportunity menu) shapes. One-theme-at-a-time turns the conversation into a long sequence of tiny decisions and prevents the teacher from seeing the *shape* of opportunity. A comprehensive menu of every micro-opportunity in the story is overwhelming and pushes the teacher into spreadsheet mode rather than judgment mode. Three to five themes is the size of opportunity space a person can hold in working memory without feeling either rushed or dumped on.

The iteration cap is six, with a soft mention at three and a re-frame escape at six. We want the loop to terminate. If it isn't converging by iteration six, the calibration axis itself is probably wrong, and the skill should surface that rather than keep refining at a finer grain. The cap also protects the operator's time budget — this is a calibration tool, not an authoring tool, and a calibration session that turns into a six-round iteration probably should have been an authoring session.

## Asymmetric constraints

The two visibility directions are not symmetric. *More visible* and *less visible* have fundamentally different failure modes, and the skill handles them differently.

### Less visible has a hard floor: the elimination check

Softening misconception-targeted wrong choices makes them more plausible-on-the-surface. That is the entire point of the move. But the floor — the bright-line constraint the authoring skill enforces with the elimination check — is that a student who does not use the named thinking skill should not be able to arrive at the correct answer via process of elimination, narrative cues, or common sense. With three multiple-choice options and two attempts, naive guessing wins ~67% of the time, so weak wrong choices effectively bypass the skill check.

When the skill softens a wrong choice, the elimination check on that decision can break. The Instructional Designer runs the check after every softening, and if the check fails for a chapter, the skill *does not commit the change for that chapter*. Partial application is acceptable; chapter-by-chapter floor enforcement is mandatory.

This floor is non-negotiable because the alternative — softening past the floor anyway — produces a story whose pedagogical structure has been destroyed without the teacher noticing. The story would still look like a polylogue story; its decisions would still have three choices; but the choices would no longer require the named thinking skill to navigate. The teacher's "less visible" request would have collapsed into "less effective." The skill must refuse this collapse, and must do so on a per-chapter basis (not a per-story basis), because some chapters will have headroom for softening and others will not.

The verify phase reports the partial application in plain language: "I softened chapters 1, 2, and 5. Chapters 3 and 4 could not be softened further without making the questions guessable, so they're at the original level. Want to leave it as-is or pull back the partial revision?"

### More visible has a soft ceiling: heavy-handedness

Sharpening misconception pulls and naming cognitive moves explicitly is the *more visible* move. The pull cannot be sharpened past a hard floor analogous to less-visible's elimination check, because there is no equivalent bright line — making the pull sharper can always pull harder. The risk on this side is qualitative: the story slides into pedagogical heavy-handedness and starts narrating its own lesson at students.

A polylogue story whose chapters say "this is a perspective-taking moment" or whose hints say "use the inferencing skill to figure out what Oz is hiding" is less a story than a worksheet with character names. Students notice; they read it as condescension; engagement drops; and the skill the story was meant to teach gets harder to teach because students are now defending against being taught.

The ceiling is enforced by the Instructional Designer's judgment, not by a numerical check. The skill must self-flag when a sharpened decision starts to read as didactic, and pull back. The discipline is: foreground the cognitive cues the skill is meant to surface (more concrete language at evidence points, sharper misconception pulls, named lenses in the debrief) without narrating the cognitive move itself ("notice how she's reading between the lines here"). That distinction is sometimes subtle, which is why a soft ceiling enforced by judgment is appropriate — a hard rule would either be too loose (allowing some narration-of-pedagogy) or too tight (refusing legitimate amplification).

In practice, the most common heavy-handedness failure is in the per-chapter debrief lens: "this choice helps students practice perspective-taking" reads as a curriculum sticker rather than as a story-grounded reflection. The fix is to keep the lens story-grounded ("this choice trusts the friendship to hold without paperwork") and let the *targeted skill* annotation in the schema do the curricular labeling.

### Reading level is mostly safe — except going down

Reading-level shifts are nearly symmetric. Going up (e.g., grade 5 → grade 7) is generally safe — vocabulary widens, sentence structure can carry more clauses, abstraction is more available. Going down (grade 7 → grade 5) is asymmetrically risky: at sufficient distance, simplification is no longer just lexical but structural. A grade-7 perspective-taking story whose tradeoffs require holding three competing frames simultaneously may not survive simplification to grade 5 — not because grade-5 readers can't read the words, but because the cognitive scaffolding for the lesson was built at grade 7.

The skill should surface this rather than silently re-author. If the requested down-shift is more than one level (grade 7 → grade 5) and the diagnostic finds that the story's perspective tradeoffs depend on grade-7-level abstraction, the skill flags it: "This story's perspective tradeoffs are calibrated to grade 7. Shifting to grade 5 would require simplifying the perspectives themselves, which is closer to re-authoring than calibration. Want me to shift to grade 6 instead, or do you want me to flag this and try anyway?"

The default is to refuse the silent re-authoring. The teacher can override.

## Operator-mediated, not direct-to-teacher (in the MVP)

The skill is designed for teachers, but the MVP runs under an operator. A teacher does not invoke the skill directly; the operator invokes the skill on the teacher's behalf, presents the brainstorm output to the teacher (in whatever form the operator chooses — a meeting, a doc, an email), receives the teacher's reaction, and feeds it back to the skill.

This is a deliberate MVP constraint, not a limitation we forgot to relax.

The reason is that the brainstorm phase, when done well, is short and easy for a teacher; when done poorly, it is overwhelming. We do not yet have enough usage data to know how often the diagnostic surfaces the right opportunities, how often the example before/afters land for teachers, and how often the loop converges within the iteration cap. Putting an operator in the loop gives us a human-shaped buffer between the skill and the teacher: if the skill's first-iteration output is wrong-shaped for a particular classroom, the operator can rephrase, re-prompt, or escalate to authoring rather than dumping the wrong-shaped output on the teacher and burning trust.

Concretely, the operator's job is:

- Read the source story enough to judge whether the skill's diagnostic captures the chapters the teacher is actually concerned about.
- Translate the teacher's classroom-context language ("my kids are sharper than this," "they freeze at long questions," "this would be a great fit if it pulled less hard at chapter 3") into the calibration axes the skill operates on.
- Filter the skill's output before it reaches the teacher. The brainstorm is meant to be readable, but if a particular iteration is awkward — five themes when the teacher only cares about one, or a heavy-handedness ceiling pull-back the teacher doesn't need to see — the operator trims.
- Decide when to call it done versus when to keep iterating. A teacher who has approved the plan but hasn't said the word "approved" should not be looped on; a teacher who has said "fine I guess" probably needs another iteration.

The operator role is expected to retire when the skill's first-iteration output is good enough often enough that direct teacher use is not a trust risk. That milestone is empirical, not architectural — the skill itself does not need to change to support direct teacher use, only the deployment surface around it.

## Customization policy

The MVP allows revision only along the two calibration axes. The boundaries of "calibration" are codified in `SKILL.md`'s policy table. The rationale, axis by axis:

- **Page narration prose**, **dialogue text**, **decision prompt language**, **hint text**, **per-chapter debrief lens**: editable on both axes. These are the surface text of the story; both axes naturally adjust them.
- **Decision choice labels**: editable on visibility (the language can shift the pull strength) but the *correctness flags* (`is_correct`, `misconception_targeted`) are locked. Allowing visibility shifts to flip correctness or rename misconceptions would silently change what the chapter teaches.
- **Fork debrief lenses**: editable on visibility only. The *structural roles* of the fork branches (which branch represents which philosophy) are locked. The visibility axis can sharpen or soften how those philosophies are described, not what they are.
- **Image-prompt staging**: adjusted only when narration changes alter what the page depicts. In practice the calibration axes rarely change staging — language shifts and pull-strength shifts don't change who is in the panel or where they're looking. When narration does change visibly, the Reviewer/Editor adjusts staging; when it doesn't, staging is left alone to preserve image consistency across renders.
- **Locked art style** and **character bible**: not modified by either axis. These are the canonical visual lock; revision must not drift them.
- **Schema structure**: chapter count, fork existence, ending count are locked. These are structural, not textual.
- **Targeted skill at gate** and **targeted skill at fork**: locked. Re-targeting a chapter's skill is a re-authoring operation; the chapter content was built to teach that specific skill at the page level. Phase-2 of the skill's roadmap may relax targeted-skill-at-gate (with significant care); targeted-skill-at-fork is permanently locked because the fork is the story's primary perspective-taking moment.

When the teacher requests something outside this policy, the skill refuses warmly with the *acknowledge → explain briefly → offer alternative* pattern. The refusals are not scolding; they are pointing at what the skill *can* do. The four refusal examples in `SKILL.md` cover the most common out-of-scope requests: "make the right answer more obvious" (collapses the elimination floor), "change the targeted skill of chapter 3" (re-authoring), "add a chapter" (structural), and "make the perspective fork have a 'best' answer" (collapses the fork legitimacy bar).

## Artifacts and versioning

The skill writes to a sibling folder beside the source library asset. Source files are never modified. The folder pattern is `{source-slug}-revised-vN/`, with `vN` incrementing per session — teachers can revise their revisions, and each session produces a new versioned folder.

The session-internal artifact is `revision-session.md`, a single living document that holds the current opportunity set, teacher signal history, and approved plan items. It is the only file maintained across the brainstorm loop; the deliverables (`revised-polylogue.md`, `revised-story.json`, `teacher-prep.md`, the revised chapter files) are produced one-shot when the teacher approves a plan.

There is no rounds folder. The brainstorm phase fits in `revision-session.md`; the apply phase is one-shot; the verify phase produces the deliverables. There is nothing the skill needs to preserve across sessions that does not fit in the session artifact.

The teacher does not read `revision-session.md`. The operator reads it (and may share excerpts with the teacher when useful), but the document's primary purpose is to give the skill a stable place to record its current state across iterations. We considered having the brainstorm output live entirely in chat, but chat history can be lost across sessions and is harder to inspect when a teacher reaction arrives in a separate channel (email, meeting). A file-based session artifact is durable, inspectable, and grep-able.

The deliverables follow the same structure as the source library asset. `revised-polylogue.md` is the calibrated master; `revised-story.json` is the calibrated export; `teacher-prep.md` is the substantive teacher-facing facilitation document; the `chapters/` mirror holds the revised chapter files. These are produced from the source files plus the approved plan; they are not maintained in parallel with the brainstorm.

## Teacher-prep document

The single most under-specified part of the original SKILL.md draft was the `teacher-prep.md` deliverable. It is a non-trivial document, and we want it to be substantive rather than boilerplate.

The teacher-prep document is not a release note. It is a one-to-two-page facilitation aid that answers: *what should I, the teacher, do with this story when I run it with my class?* The MVP includes a structured set of sections in `SKILL.md`:

- *What changed* and *what stayed the same* — orient teachers familiar with the original story.
- *Updated runtime* — if it changed, so the teacher can plan the lesson period.
- *Image-pipeline cost* — explicit "none" call-out so teachers know whether to commission a re-render. (For the MVP's two axes, this is almost always "none — text only.")
- *What to listen for in group discussion* — per chapter-end decision, the cognitive operation the decision is targeting and one or two student moves that suggest engagement vs. avoidance. Specific to *this* story; not generic facilitation advice.
- *Common student misreadings the revised decisions target* — pulled from the misconception annotations, written in plain teacher-facing language.
- *Suggested teacher prompts during chapter-end discussion* — one or two per chapter, in the form of questions the teacher can ask groups to surface the targeted thinking move.

The substance of these sections is not generic. They are grounded in the specific decisions and misconception annotations of *this* revised story, and they shift when the visibility axis shifts (a more-visible revision foregrounds the cognitive move, and the teacher-prep should reflect that). The Reviewer/Editor sub-agent authors this document in Phase 3, after the verify pass, because verify-pass output (especially partial-application flags) feeds the teacher-prep.

This document is the part of the deliverable that compensates teachers for the reading they would otherwise have to do to use the story well. A teacher who runs the revised story without having read it benefits more from a good teacher-prep than from a perfectly calibrated revision.

## Quality gates

The verify phase runs the same checks the authoring skill runs at Round 7, adapted for revision context:

- *Elimination check* — every gate decision still passes. This is the most consequential check for visibility-down requests; chapters that hit the floor are reported as partial application.
- *Fork legitimacy* — the perspective fork's branches still represent genuinely distinct, defensible perspectives. Visibility shifts to fork debrief language must not collapse one branch into "the obvious right answer."
- *Ending diff* — the divergent endings are still drastically different in fate, mood, and lesson. Reading-level shifts are not expected to flatten ending diff, but worth verifying.
- *Runtime fit* — recomputed runtime is within the original budget (or the change is reported to the teacher).
- *Bible sync* — inline character descriptions match the bible across all chapters. Bible should not have changed in the revision, but the sync-check is cheap insurance.
- *Schema validity* — `revised-story.json` validates against the bundled schema. Cross-cutting invariants: exactly one perspective fork, ending count matches fork branches, all `next_chapter_id` references resolve.

The warn-and-allow pattern from the authoring skill is preserved: report the issue, propose a fix, allow the teacher to override. Overrides are recorded in `metadata.author_overrides` (we preserve the field name even though the entity overriding is a teacher, not the original author — the schema field is descriptive, and revising the schema would be out of scope).

## Why operate at all? Why not point the teacher at the authoring tool?

The temptation, when first sketching this skill, was to say: a teacher who needs revisions deeper than language adjustment should run the authoring skill from scratch with their classroom in mind. That preserves authoring tool fidelity at the cost of teacher time.

We rejected this for two reasons.

First, the authoring skill produces *one* story per nine-round session. Teachers who want a perspective-taking lesson for grade 6 do not need the eight stories that exist in the library to all be authored at grade 6; they need the *one* story they want to use to be available at grade 6. Calibration is the right scope of work for that need.

Second, the authoring skill's machinery (Creative Writer + Instructional Designer + Reviewer/Editor) is expensive in ways that calibration does not need to pay. Re-running concept brainstorming, character bible authoring, and outline drafting for a teacher who just wants the existing story at a different reading level is wasted authoring effort, and the result will not be the same story — concept brainstorming is non-deterministic and produces variation. A calibration tool that preserves the story's identity is what teachers actually want.

The line between calibration and re-authoring is the customization policy table. Anything inside the policy is calibration; anything outside is authoring. The skill is rigorous about this line because crossing it silently is the failure mode that loses teacher trust.
