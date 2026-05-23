# Solo LLM-Coding Workflow

A one-person-led Claude Code workflow for taking small software projects from a rough idea
to an integrated, verified build. You are the lead: you reason and approve at the gates;
the agents ideate-with-you, plan, build, verify, and integrate in between.

The whole system rests on one principle — **durable files in `.project/` and Git are the
source of truth, not any conversation.** If you remember one thing, remember that the files
are the system; the conversations are just workers that read and write them.

This workflow is intentionally optimized for small projects where each phase fits in one
conversation. If a phase does not fit, split the project or re-plan into smaller phases
instead of turning it into a cross-session protocol.

## The shape of it

```text
  /ideate        →   /plan          →   /build              →   /integrate
  (1 convo)          (1 convo)          (1 convo)               (1 convo)
  produces           produces           builds slices,          wires slices,
  spec.md +          design.md +        invokes verifier        runs checks,
  scaffolds          contracts +        per slice, commits      stops for
  .project/          per-slice files    each verified one       gate 3

   ▲ gate 0           ▲ gate 1           ▲ gate 2 (mid-flight)    ▲ gate 3
   approve spec       approve plan       only contract /          approve
                                         architecture changes     integration
                                         stop for you
```

`/build` invokes the `slice-verifier` subagent synchronously after each slice. No separate
verify terminal, no baton between conversations. `/verify` exists as a manual recovery
command only.

`/contract-change` handles gate-2 decisions when build stops mid-flight.

## YOUR RESPONSIBILITIES (read this part)

The agents do the work; you do three things and only three things. Everything else flows
without you.

### 1. Approve at the four gates

| Gate | What you're approving | Why it's yours |
|------|----------------------|----------------|
| **0 — spec** | `spec.md` is right before planning starts | A wrong spec poisons everything downstream |
| **1 — plan** | slices, boundaries, contracts before any code | this is where slice independence is decided — highest leverage |
| **2 — contract change** | any change that alters a contract or core architecture | it ripples to other slices, so it can't be autonomous |
| **3 — integration** | seam conformance, obsolescence findings, and the end-to-end run | the last irreversible step |

Between gates, do **not** approve individual slices — that defeats the design.

### 2. Respond when build stops for a decision

The orchestrator runs slices to completion and only stops when it actually needs you. When
it does, it presents:

- the issue;
- evidence;
- options;
- a default recommendation;
- the exact files and slices affected.

Your job: pick. Usually that means running `/contract-change` to apply the gate-2 decision,
which records it in `decisions.md` and rolls affected slices back to `todo` for rebuild.

If build stops for repeated verification failure it cannot resolve, the call is yours:
fix the slice manually, replan, or accept the failure as a documented limitation.

### 3. Keep the scope honest

Watch for slice drift. Build is *allowed* to reach into not-yet-started slices or to touch
verified-slice territory for mechanical changes, but every crossing must show up in
`decisions.md`. If you see those crossings piling up, the clean decomposition is eroding —
pull it back to gate 2 and replan.

**That's the whole job.** If you find yourself approving every slice, hand-relaying file
contents, or resolving things the files already record, the system is being used against
its grain.

## What the agents handle (not you)

- Slice selection, boundary preflight, verifier invocation, fix/reverify cycles.
- Per-slice commits and `.project/` state updates.
- Routine implementation defects (verifier flags them, build fixes them).
- Process hygiene: clean tree before each slice, `build.md` handoffs, `verify.md` records.

If you catch yourself doing any of these, stop and ask why the agent isn't.

## Core assumptions

- One `/build` orchestrator runs at a time.
- `/build` invokes a verifier subagent instead of using a second terminal.
- Git tracks code changes and recovery.
- `.project/` tracks intent, state, boundaries, contracts, and decisions.
- One verified slice should become one Git commit.
- Agents manage process hygiene.
- The human lead makes only product and architecture decisions.
- The orchestration agent is capable — it classifies crossings, drives the verify-fix loop,
  and passes minimal context to subagents without supervision.
- Each phase (`/ideate`, `/plan`, `/build`, `/integrate`) fits in one conversation — no
  cross-session resumption is required.
- Contract files are proportional to the project. API projects should have real OpenAPI
  contracts; non-API projects should record only the seams that actually need contracts.

## Files

Installed workflow files live under `.claude/`:

```text
.claude/
  protocol.md
  commands/
    ideate.md
    plan.md
    build.md
    verify.md
    integrate.md
    contract-change.md
  skills/
    ideate-project/SKILL.md
    decompose-project/SKILL.md
    orchestrate-build/SKILL.md
  agents/
    slice-verifier.md
    integration-reviewer.md
```

`.claude/protocol.md` is normative. Commands, skills, and agents must obey it.

Project artifacts live under `.project/`.

## Operational project layout

The workflow creates:

```text
.project/
  spec.md
  design.md
  decisions.md
  contracts/
    <contract files as needed>
  slices/
    <slice>/
      status.json
      boundary.md
      acceptance.md
      build.md
      verify.md
```

Per-slice files are the operational source of truth. Project-level summary files may exist,
but should not replace per-slice state, boundary, or acceptance files.
