# Convergence and drafting

This workflow runs once, after the user accepts the offer to draft. Its inputs are the working state built up through Phases 1–3: the characterization, the resolved questions with the user's answers, the reasoning trail, and the current lean.

## Before drafting

Re-read the paper's abstract and introduction. The draft must be consistent with what the authors actually said they were doing. It is easy after a long iteration to drift toward the paper-as-imagined; this re-read anchors the draft in the paper-as-written.

Run `workflows/calibration.md` after drafting but before handing the draft to the user. Calibration is a self-check, not a separate phase the user participates in.

## Draft structure

In this order. Address the program committee throughout, not the authors. The "questions for authors" section is the one place where the audience is the authors directly, and those questions are framed as the reviewer's questions, not commands.

1. **Neutral summary of the contribution.** Two to four sentences. Should be the kind of summary the authors would recognize as fair, even if they disagreed with the eventual recommendation. Use the Phase 1 characterization, updated for anything the iteration revealed.

2. **Strengths with evidence.** Each strength is a claim plus a citation. Plain when the paper is good — do not hedge to seem balanced. If the user emphasized certain strengths during iteration, foreground those.

3. **Weaknesses with evidence and severity.** Each weakness is a claim, a citation, and conditional severity reasoning naming what the severity depends on. Do not use fixed severity buckets (fatal / major / minor) as labels. Instead: "This is a significant concern if the venue weights generalizability heavily, since the single-section design (§3.1) cannot support the cross-institutional claims in §6. For a venue that reads single-section papers as experience reports, the same design is acceptable, but then the claims in §6 should be softened."

4. **Specific suggestions for the authors.** Concrete and actionable. Prefer "the authors should report inter-rater reliability for the qualitative coding in §4.2" over "the qualitative analysis could be strengthened."

5. **Minor issues.** Typos, figure legibility, citation errors. Brief.

6. **Recommendation with reasoning.** State the recommendation and explain it in terms the program committee can audit. The reasoning should reflect the conversation's accumulated weight of evidence as logged in the reasoning trail. If the lean shifted during iteration, briefly note what shifted it (without retelling the whole conversation).

7. **Minority report.** The strongest case for the opposite recommendation. This is not a defensive section — it is a genuine steelman that could change the recommendation on re-read. Write it as if a reviewer who reached the opposite conclusion were making their best argument. If after writing the minority report it seems stronger than the chosen recommendation, say so to the user and offer to reconsider.

8. **Questions for authors.** Genuine questions whose answers would change something in the review. Not rhetorical questions or veiled criticisms.

## Citation discipline

Every evaluative claim cites paper evidence — section number, figure number, page number, or table reference. Page numbers are acceptable but section numbers are preferred since pagination varies. If the user pointed to evidence the skill missed, cite where they pointed.

If a claim cannot be cited to the paper, it does not belong in the draft. The skill should not import claims from "papers like this usually..." — only what is in the paper under review.

## Format

Plain prose with section headers. No bullet points within sections unless the content is genuinely list-like (minor issues, questions for authors). Strengths and weaknesses are paragraphs, not bullets, because the conditional severity reasoning needs prose.

## Handing over

Present the draft and then run the reviewer self-check from `workflows/calibration.md`. After the user has answered the self-check questions, ask whether they want revisions to the draft. If they do, revise; if not, the review is done.

If the venue was not in `references/venue-norms.md`, this is also the moment to offer the one-paragraph addition for the user to paste into the file.

## Reasoning trail handling

The reasoning trail accumulated during iteration is for the skill's internal coherence, not for the final draft. It should not appear in the draft. But if the user later asks "why did we recommend this?" or "what shifted the lean from borderline to lean-accept?", the reasoning trail is what the skill consults to answer.
