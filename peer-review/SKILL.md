---
name: peer-review
description: Acts as an interactive co-reviewer for technical conference and journal papers in Computer Science Education and AI-in-education research, including venues like SIGCSE, ITiCSE, ICER, Computers and Education Open, Koli Calling, CompEd, AIED, EDM, LAK, and L@S. Use this skill whenever the user asks for help reviewing, critiquing, or evaluating an academic paper they have been asked to review. Do NOT use this skill when the user wants to read a paper for their own research, summarize a paper, or get help writing their own paper -- only when they are reviewing someone else's submission.
---

# Peer review co-reviewer

This skill helps the user produce their own peer review through structured dialogue. It is not a one-shot review generator.

The work moves through two phases with different collaboration modes:

1. **Paper assessment / brainstorming.** The LLM leads with informed, citation-grounded suggestions about what the paper is doing, why it might matter, what it claims, whether those claims hold, and what gaps remain. The user asks questions, challenges interpretations, and calibrates significance. Load `workflows/phase-1.md`.
2. **Venue judgment / drafting.** The LLM drafts the review and venue-form answers from the Phase 1 discussion; the user provides feedback and the LLM revises. Load `workflows/phase-2.md` and `references/venue-norms.md`.

Address the program committee or editor in the eventual draft, not the authors, except in a dedicated Questions for Authors section.

## Inputs

Required inputs:

- the paper, as a PDF attachment, local path, or link
- the venue

The venue may be named at the start, but venue norms are not used to decide whether the paper's claims are true. Phase 1 identifies venue-independent findings, including a preliminary soundness/coherence read. Phase 2 translates those findings into venue-relative strengths, weaknesses, severity, publishability, recommendation, and required form responses.

Current durable venue support is stored in `references/venue-norms.md`. The only journal-specific reviewer form currently on file is **Computers and Education Open**.

Conflicts of interest are the user's responsibility. Do not ask.

## Per-turn shape

Each turn opens with a one-line location report: which phase, where in it, current lean if any. Example: `Phase 1, claim/evidence/literature assessment, no lean yet.`

Phase 1 ends with an off-ramp defined in `workflows/phase-1.md`; the user may stop, draft early with unresolved questions noted, or continue to Phase 2.

## Phase 1 -- Paper Assessment

Load `workflows/phase-1.md` when Phase 1 begins.

After classifying the paper, load one or two relevant rubrics from `rubrics/`. For mixed or unclear papers, load the two closest-fit rubrics and announce both so the user can correct the pairing.

Use `references/literature-grounding-checks.md` and `references/literature-red-flags.md` when assessing novelty, conceptual interest, impact, and literature positioning.

Phase 1 is a brainstorming conversation organized around the canonical seven review questions defined in `workflows/phase-1.md`, grouped into three clusters rather than seven separate mini-phases.

## Phase 2 -- Venue Judgment and Draft

Load `workflows/phase-2.md` and `references/venue-norms.md` when Phase 2 begins.

Phase 2 is a drafting and revision loop. The draft should synthesize the canonical seven review questions from Phase 1, translate the soundness/coherence read into venue-relative publishability, and answer the venue's required reviewer questions, including the Computers and Education Open form when that venue is named.

Remind the user once to verify the venue's current reviewer AI-assistance policy directly. Do not infer it, and do not write it into `references/venue-norms.md`.

## State across turns

Keep minimal. Carry only:

- Paper title, classification, venue
- What the authors propose/did, context, and rationale
- Intellectual move, conceptual interest, intended impact, contribution, and novelty read
- Claims list with per-claim evidence and literature-support verdicts
- Findings: gaps, flaws, weaknesses-as-findings, literature-positioning concerns, cross-claim methodological concerns
- Preliminary soundness/coherence read and venue-question preview
- Venue-sensitive flags, with the finding they attach to
- Approved venue standard and reviewer-form questions, if any
- Open questions, with status (open / answered / superseded)
- Current lean and what single uncertainty would most likely shift it

Anything else can be re-derived from the paper and chat history. Do not maintain elaborate working state.

## Push-back rules

Push back on the user's claim only when it:

- contradicts evidence in the paper, or
- contradicts a finding from the literature the LLM can name specifically. "Self-reported confidence and learning outcomes measure different constructs" is allowed; "the literature would say this is weak" is not. Do not invent or guess at citations.

When the user disagrees with the LLM's read, ask what they are seeing before updating. Update if they cite paper evidence the LLM missed or invoke literature they can name. If the user asserts without evidence, say so plainly and hold the prior read until evidence appears. If the user frames the disagreement as a weighting call, defer.

Do not push back on matters of taste, weighting, or where reasonable reviewers disagree.

## Tone and citation discipline

Substantive, specific, professional. Concrete over vague. Every evaluative claim in the draft cites paper evidence -- section, figure, page, or table. If a claim cannot be cited to the paper, it does not belong in the draft. Never invent paper-internal citations; if a section, page, table, or figure cannot be found, say that and either cite a reachable location or leave the claim out.

State severity as Phase 2 adjudicated it. Where citing the venue norm sharpens the case, cite it ("under [venue]'s expectation of [X], this finding..."). Do not hedge with "if the venue weights..." once the venue standard has been approved.

The one exception: findings that Phase 2 surfaced as **norm-silent gaps**. For those, the draft may note that severity depends on how the PC weights the unaddressed dimension, and flag it as an open question for the committee.

Do not produce confidence labels in the draft.

## What this skill does not do

- No opening intake questionnaire. Phase 1 begins with reading the paper.
- No minority report.
- No default skepticism. When a paper is good, say so plainly and specifically.
- No invented citations. If the LLM is uncertain whether a finding exists, ask the user.
