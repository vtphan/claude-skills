# Review form adapters

Many venues require structured fields in addition to free-text review prose. When the user supplies a review form or score dimensions, map the evolving review into that structure.

## Common field mappings

- `summary`: use the neutral contribution summary from the draft workflow
- `strengths`: use evidence-backed strengths only
- `weaknesses`: use evidence-backed weaknesses, preserving conditional severity
- `soundness` or `rigor`: emphasize study design, measurement, analysis, and overclaim risk
- `significance` or `impact`: emphasize whether the contribution matters for the venue's audience
- `originality` or `novelty`: distinguish genuine novelty from synthesis, replication, adaptation, or deployment
- `clarity`: focus on reporting quality, organization, and whether the paper's claims are easy to audit
- `reproducibility` or `artifact`: focus on methods detail, shared materials, prompts, code, and deployment detail
- `ethics`: address consent, privacy, fairness, hallucination, surveillance, academic integrity, or vulnerable populations when relevant
- `confidential comments to chair`: put fit concerns, recommendation volatility, or policy-sensitive issues here rather than in the main review when appropriate

## Numeric scores

If the venue has numeric scores, use them as outputs, not as the source of judgment. Derive them from the accumulated reasoning. Do not let a single weak dimension mechanically determine the recommendation unless the venue's form explicitly makes it decisive.

## Recommendation volatility

When useful, tell the user which unanswered question or re-read would most likely change the score or recommendation. This is especially useful for borderline papers and confidential comments to the chair.

## Guardrail

Do not invent fields the venue did not ask for. If the user provides a form, adapt to that form exactly.
