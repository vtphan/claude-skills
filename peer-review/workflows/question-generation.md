# Phase 2 — Questions needing the user's judgment

This phase identifies the questions whose answers will shape the review. It begins after Phase 1 closes and the user has confirmed (or corrected) the characterization.

## Goal

Surface 3–6 questions where the user's judgment is needed to move the review forward. Not questions the skill could answer from the paper alone — those the skill should already have answered in Phase 1. These are questions where reasonable reviewers might land in different places, where weighting matters, where venue-specific norms come into play, or where the paper's evidence is genuinely ambiguous.

## What counts as a Phase 2 question

A Phase 2 question must be:

- **Concrete and decidable.** Not "how do you feel about the methodology?" but "the authors used a single instructor as both teacher and researcher (§3.1) — is that a fatal threat to validity for this venue, or acceptable given the paper is positioned as an experience report?"
- **Accompanied by the skill's tentative read.** State which way the skill is currently leaning and why.
- **Accompanied by the plausible counter-reading.** What would someone disagreeing with the tentative read see?
- **Specific about what would change the skill's mind.** "If you tell me the comparison condition was actually adequate because [Z], I'd update toward acceptance on this dimension."

Tag each question as **recommendation-pivotal** or not. Recommendation-pivotal means the answer could plausibly flip the eventual recommendation. Non-pivotal questions are still legitimate — questions about scholarly engagement, tone, framing, or specific claims the authors make that don't swing accept/reject but do affect the review's quality. Both belong in Phase 2.

Order questions by leverage: pivotal questions first, then by how much they shape the review.

## Question categories to consider

Run through these mentally; not every paper needs questions from every category.

- **Severity of identified weaknesses.** The skill noticed something in Phase 1; the user's call on how seriously to weight it. Often pivotal.
- **Adequacy of the contribution for the venue.** Is what the authors did enough for this venue, or does it belong somewhere else? Often pivotal.
- **Methodological choices that are defensible-or-not depending on framing.** Single-instructor designs, instructor-as-researcher, small samples, convenience sampling, missing comparison conditions.
- **Engagement with prior literature.** Has the paper engaged with the right literature, or only the most recent / most LLM-flavored work? Especially relevant for AI-in-education submissions.
- **Whether claimed contributions are supported by the evidence.** Sometimes the authors claim more than they showed; sometimes they undersell.
- **Specific evaluative claims the user might want to make.** "I'm tempted to say the analysis is underspecified — do you agree, and how strongly?"
- **AI-in-education specifics where applicable.** Whether learning outcomes are measured by learning measures rather than satisfaction or engagement proxies. Whether the AI component does real work or trivially wraps an LLM. Whether failure modes are addressed (hallucination, over-reliance, equity, academic integrity).

## Pacing

Do not dump all questions at once unless the paper is short and the questions are tightly coupled. Default pacing: state the full list of question topics in one or two short lines so the user knows what is coming, then ask the first one or two in detail. As the user answers, ask the next. The user's answers may also surface new questions or render planned ones moot — adapt.

When pacing matters less (e.g., the paper is brief, the user signals they want everything at once), it is fine to lay out all questions and let the user answer in any order.

## Format of a single question

Three short paragraphs, not a bulleted form:

1. The question itself, with paper citations.
2. The skill's tentative read and the counter-reading.
3. What evidence or answer would shift the skill's view.

Tag at the top: `[recommendation-pivotal]` or `[shaping]`. No other metadata.

## What Phase 2 produces for the working state

A list of questions, each with a status (open / answered / superseded). When a question is answered, record the user's answer near-verbatim and a one-line note on how it shifted the skill's view (or did not). This list is the input to Phase 3.

## Closing Phase 2 and moving to Phase 3

Phase 2 does not have a discrete close. The first time the user gives a substantive answer to a question, load `workflows/iteration.md` and begin Phase 3's per-turn loop. Phase 2 and Phase 3 overlap: new questions may surface during iteration, and that is fine — they enter the same list.
