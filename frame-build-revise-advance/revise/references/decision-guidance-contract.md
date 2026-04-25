# FBRA Decision Guidance Contract

Use this contract whenever a skill asks the human driver to decide something that affects product scope, user-visible workflow, tech stack, architecture, data model, persistence, auth/security, external services, billing, deployment, or verification expectations.

The goal is to reduce human decision load without hiding judgment. Give a short, informed recommendation based on the project context and on implementation by a smart LLM such as Claude Code or Codex.

## Decision Prompt

```markdown
Decision: <short name>

Context:
- <why this decision is needed now>
- Affects: <wave / must-have IDs / product or technical surfaces>

Options:
1. <option>
   - Pros: <1-3 bullets>
   - Cons: <1-3 bullets>
   - LLM-buildability: <why a smart coding agent can/cannot implement it reliably>
   - Reversibility: <reversible / costly / shipped-once>
   - Verification impact: <how this can be tested or demonstrated>

2. <option>
   - Pros: ...
   - Cons: ...
   - LLM-buildability: ...
   - Reversibility: ...
   - Verification impact: ...

Recommendation:
- Choose <option> because <reason>.

Assumptions:
- <what must be true for the recommendation to hold>

If deferred:
- Safe to proceed: <what can continue>
- Blocked: <what should wait>
```

Use 2-3 options. Do not ask open-ended questions when credible options can be framed.

## Evaluation Criteria

For important decisions, especially stack, architecture, persistence, auth/security, deployment, and integrations, evaluate:

- Convention density: strong defaults, common patterns, low ambiguity.
- LLM-buildability: likely to be implemented correctly by Claude Code or Codex with limited human correction.
- Local testability: cheap automated tests, scripted checks, or demos.
- Reversibility: whether removal later requires migration, rewrite, or user-visible breakage.
- Dependency risk: packages, services, credentials, billing, deployment complexity.
- Security blast radius: auth, permissions, secrets, file handling, code execution, payments.
- Operational burden: setup, debugging, monitoring, migrations, support.
- Fit to active wave: helps current must-haves without pulling in future-wave scope.

## Recording Approved Decisions

When the human approves a decision, record a compact entry in the wave doc's Decisions section:

```markdown
- YYYY-MM-DD - <Decision>: <chosen option>. Rationale: <one sentence>. Alternatives considered: <brief list>.
```

Do not record every local implementation choice. Record decisions future waves should honor.
