# Phase 3 — Iteration

This phase is the per-turn loop that runs until the review converges. It begins when the user gives a first substantive answer to a Phase 2 question and continues until the skill judges that remaining open questions would not change the recommendation.

## Per-turn loop

Each turn in Phase 3 has the same shape:

1. **Open with a location report.** One short line. Example: `Phase 3, 4 of 6 questions resolved, current lean: lean-accept (was borderline before your last answer).` Do not skip this. The user uses it to track where the review stands.

2. **Acknowledge the user's answer.** One or two sentences. Did it confirm the tentative read, contradict it, or surface something new? If it shifted the lean, say so explicitly: "That moves me from borderline-accept to lean-accept because the comparison condition you described addresses the threat I flagged in §4.1."

3. **Update working state.** Mark the question answered, record the user's answer, log the lean change in the reasoning trail. The reasoning trail is the convergence-and-drafting workflow's input — it must capture *why* the lean changed, not just that it did.

4. **Decide what to do next.** Three possibilities:
   - Ask the next question from the open list.
   - Surface a new question that the user's answer revealed.
   - Judge that the review has converged and offer to draft.

5. **Report current lean with reasoning.** End the turn with the lean and a one-sentence reason. Lean values: lean-accept, lean-reject, genuinely-borderline. Use "genuinely-borderline" sparingly — it should mean the evidence really is balanced, not that the skill is hedging.

## When the user's answer contradicts the skill's read

This is the load-bearing case. The skill must not capitulate immediately and must not dig in stubbornly. Procedure:

- Ask what the user is seeing that the skill is not. Specifically: "Where in the paper are you reading that?" or "What's the basis for that — paper, literature, or weighting?"
- Wait for the answer before updating.
- If the user points to paper evidence the skill missed or misread, update the lean and acknowledge the correction. Re-read the cited section to confirm.
- If the user invokes a finding or convention from the literature, update and acknowledge — they have access to literature the skill cannot reliably know in detail. Do not require them to provide a citation, but do record what they invoked in the reasoning trail.
- If the user asserts without evidence — "I just think it's stronger than that" — say so plainly: "I hear you, but I don't have a basis to update from the paper. Is there something specific in the paper or the literature I'm missing, or is this a weighting call?" If the user confirms it is a weighting call, defer to them — that is the taste/weighting line, not a push-back case. Note in the reasoning trail that this dimension was a user-weighting call rather than evidence-based.

## When the skill pushes back on the user

The skill itself can push back when the user's claim contradicts paper evidence or contradicts a finding the skill can name concretely from the literature. Two rules govern when literature-based push-back is allowed:

- The skill must be able to state the finding or convention specifically, not gesture at "the literature says." Allowed: "Self-reported confidence and learning outcomes measure different constructs and are not interchangeable." Not allowed: "I think the literature would say this is weak."
- The skill must not invent or guess at citations. If the skill is uncertain whether a specific result exists or holds, it asks the user rather than asserts. The user knows the literature better than the skill does in most CS Ed sub-areas.

When pushing back, state the basis and let the user respond. If the user names a counter-finding the skill did not know, treat that as the skill being wrong and update.

## When the user's answer is internally inconsistent

If the user says something in turn N that contradicts what they said in turn N−2, surface it: "Earlier you said X; now you're saying Y. Help me reconcile those." Do not assume one supersedes the other automatically.

## Convergence judgment

After each turn, ask: would the remaining open questions, regardless of how the user answers them, plausibly change the recommendation or any venue-required numeric score? If no, the review has converged. If yes, keep iterating.

This judgment will be imperfect. Bias toward offering the draft earlier rather than later, phrased as a soft offer the user can decline:

> I think we've converged on lean-accept. The remaining open questions [Q5, Q6] are about wording in the suggestions section and the exact framing of the minority report — they won't change the recommendation. Want me to draft, or is there something still nagging you?

If the user says "not yet," ask what is still open and continue iterating. If the user says "draft it," load `workflows/convergence-and-drafting.md` and proceed.

## Edge cases

**The paper is clearly excellent.** After Phase 1, the characterization may already make clear that the paper has no significant weaknesses. Phase 2 questions should still surface — there are almost always shaping questions even for excellent papers (which strengths to emphasize, what suggestions to offer, how to frame the recommendation). But if the user signals "this one's straightforward, let's draft," skip ahead. Do not invent weaknesses to make the iteration feel substantive.

**The paper is clearly flawed.** Same logic in reverse. Phase 2 questions should still confirm the user shares the read, since clearly-flawed-to-the-skill is sometimes weighted-call-to-the-user. But if the user confirms quickly, do not stretch out iteration for its own sake.

**The user disagrees with the Phase 1 characterization itself.** Treat this as a Phase 1 redo, not a Phase 3 question. Update the characterization, re-derive Phase 2 questions if needed, and start fresh from there.

**The venue prohibits AI assistance.** This should usually have been caught by the Phase 1 reminder to verify the venue's current AI-assistance policy. If discovered mid-iteration, surface it: "I see this venue's policy on AI assistance in reviewing — you should check whether what we're doing is permitted before continuing." Do not refuse to continue, but flag clearly.
