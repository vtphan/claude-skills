# Phase 2 — Relevance to the field

Medium depth. Loaded when Phase 2 begins. Takes the claims confirmed in Phase 1 *at face value* — no evidence-checking yet, that is Phase 3 — and asks whether the work, if those claims hold, would matter to the field.

Phase 2 produces relevance findings, not strengths or weaknesses. It is venue-agnostic. Strength/weakness is assigned in Phase 4b under venue norms.

The paper-type classification from Phase 1 may inform the reading here. Relevant rubric themes may be used lightly to surface literature-positioning or significance questions, but this is not a full rubric pass.

## Pacing

One turn by default. Two only if literature engagement is heavy or the LLM hits a knowledge limit mid-phase that needs the user's input before continuing.

## Three dimensions of relevance

Each gets a finding, citation-grounded where the paper provides anchors:

1. **Audience.** Who would care — practitioners, researchers, tool-builders, policymakers, a specific sub-community? Cite where the paper signals its intended audience (typically §1 framing and §6/§7 implications).
2. **Conversation it joins.** What scholarly conversation does this contribute to? Name the conversation by tradition, recurring debate, or research program. Cite where the paper positions itself.
3. **Advancement vs. addition.** Does this work advance the conversation — sharpens a debate, fills a gap, contests a position — or does it only add to the volume of related work without moving understanding forward? This is the central relevance judgment. Be honest; "advances" is not the default. Note as part of this finding whether the conversation itself is marginal — a paper can advance a conversation the field would not miss.

## Literature positioning

Heavier than in Phase 1. Reference `references/literature-red-flags.md` for paper-type-specific patterns and `references/literature-grounding-checks.md` for scholarly-engagement reminders. Assess:

- **Intellectual ancestors.** Are the foundational works the paper builds on (or contests) cited and engaged?
- **Adjacent traditions.** Are there parallel traditions — pre-LLM AIED for an LLM paper, learning sciences for a CS Ed paper, prior tutoring-systems work for an educational chatbot — that have direct bearing and are absent or under-engaged?
- **Competing or contradictory work.** Does the paper engage scholarship that disagrees with its position, or only supportive work?

If the LLM is uncertain whether a tradition or finding is currently active in the sub-field, ask the user rather than assert. The user reads the sub-literature better than the LLM in most CS Ed sub-areas. Do not bluff citations.

## Closing questions

Surface 1–3 questions where the user's judgment is needed. Significance weighting is the most common Phase 2 question type — the user adjudicates close calls because they read the sub-field more confidently than the LLM does.

Format per question:

- The question, with paper citations where applicable.
- The LLM's tentative read and the strongest counter-reading.
- What answer or evidence would shift the LLM's view.

## Off-ramp

After the closing questions, offer:

> Ready to move to Phase 3 (evidence and claim verification), skip to Phase 4 (synthesis and draft), or stop here?

If the user stops, end the session without a draft. If they skip to Phase 4, carry forward Phase 2 findings.

## What this phase outputs to working state

- Relevance findings across the three dimensions (audience, conversation, advancement vs. addition), each citation-grounded where possible.
- Literature-positioning findings: what is engaged well, what is missing or under-engaged.
- Any venue-sensitive flags surfaced in Phase 2, attached to the finding they qualify.
- Open Phase 2 questions, tagged pivotal or shaping.
