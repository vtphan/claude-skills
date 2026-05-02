# Vision Doc Schema

The vision doc is the upstream artifact in the **VADER** loop. It is the answer to "why are we building this, for whom, and what would success look like" — written before requirements are expanded, before architecture is committed, and before any wave is planned.

This schema is the contract between two skills:

- `vision-shaper` — produces the initial vision doc through a sounding-board conversation.
- `vision-pivot` — revises the vision doc when learning from later waves invalidates a core part of it.

Other VADER skills *read* the vision doc but do not write to it.

## Contents

1. [Philosophy](#1-philosophy)
2. [File format and location](#2-file-format-and-location)
3. [Required sections](#3-required-sections)
4. [Pivot semantics](#4-pivot-semantics)
5. [Change log](#5-change-log)
6. [Invariants](#6-invariants)
7. [Worked mini-example](#7-worked-mini-example)

---

## 1. Philosophy

The vision doc captures **intent**, not specification. It is short on purpose. A vision doc longer than two pages is almost always over-reaching into requirements territory; the right place for that detail is the wave doc.

Three things make a vision doc useful downstream:

**It is opinionated about scope.** The doc names what is in scope and, with equal weight, what is deliberately out. The wave doc's "themes not yet waved" section depends on this: a theme is in scope but not yet waved; an out-of-scope idea is rejected on principle. Without a clear vision, that distinction collapses.

**It is opinionated about the user.** A role here is a person trying to do a thing, not a job title. Get the roles right and downstream artifacts inherit clarity. Get them wrong and every wave's stories will smell off.

**It is honest about what we don't know.** The vision doc has an Open questions section, and that section is meant to be substantial in a freshly drafted vision. It is the seed for the assumptions register in the wave doc.

The vision doc is normally stable. It is revised only by `vision-pivot`, only when a later-wave learning invalidates a core part of it, and only with an explicit change-log entry. Body edits without a change-log entry are forbidden.

## 2. File format and location

One markdown file per project, named `<project-slug>-vision.md`. The file lives in the project's `docs/` directory alongside the architecture doc and the wave doc.

YAML frontmatter holds machine-parseable state. Markdown body holds the doc.

```yaml
---
vision_version: 1                       # Incremented by each vision-pivot pass
created: 2026-05-02                     # ISO date, never changes
last_updated: 2026-05-02                # ISO date, updated by vision-pivot
status: active                          # active | pivoted
---
```

`status` values:
- `active` — the vision is the current statement of intent.
- `pivoted` — the most recent change was a pivot (set by `vision-pivot`); cleared back to `active` only when a subsequent wave-redraft cycle has fully reconciled downstream artifacts to the new vision.

## 3. Required sections

Below the frontmatter, the vision doc contains exactly nine numbered sections, always in this order. Sections are short by design.

```markdown
# <Project> — Vision

## 1. Problem
## 2. Target users
## 3. Value hypothesis
## 4. In scope
## 5. Non-goals
## 6. Success metrics
## 7. Constraints
## 8. Prior art and alternatives considered
## 9. Open questions
## 10. Core journeys (optional)
```

Section 10 is **optional**. Include it for product-heavy systems where the architecture's modules and key interfaces depend on user flows; skip it for tech/infra projects where data flow drives architecture more than user flow. When in doubt, include it lightly — one or two short journeys is fine.

### 1. Problem

One or two paragraphs. What problem are we solving, in whose life, and what does the status quo look like today. If you can't name a specific person who has this problem, the problem statement is too abstract.

### 2. Target users

A compact table of roles. A role is what someone is trying to accomplish, not their job title. One row per role.

```markdown
| Role | What they're trying to do | Why this product helps them |
|------|---------------------------|------------------------------|
| ...  | ...                       | ...                          |
```

If you have more than four or five roles in a vision doc, the project is probably too broad — split it or sharpen the focus. Roles can always be added later via `vision-pivot`.

### 3. Value hypothesis

One paragraph in the form: "If we build X for Y, they will Z, because of W." This is the testable claim the project rests on. The vision is right or wrong as a function of this claim being right or wrong.

The value hypothesis is referenced by the wave doc's success metrics and by the audit's verdict criteria. A vague value hypothesis will produce vague success metrics, which will produce un-auditable waves. Tighten this section until the claim is falsifiable.

### 4. In scope

A bulleted list of capabilities the system must provide to deliver value. Capabilities, not features — the wave doc breaks capabilities down into features per wave. Aim for 5-12 bullets at this level.

### 5. Non-goals

A bulleted list of things the system deliberately does *not* do, paired with one-line reasons. Non-goals are load-bearing: every wave-redraft cycle uses them to reject scope creep. Without explicit non-goals, the audit step has nothing to compare proposed scope changes against.

### 6. Success metrics

Two to five measurable outcomes that, if achieved, would mean the value hypothesis is confirmed. Each metric specifies the measurement method, not just the target.

Bad: "Users like the product."
Good: "After 30 days, ≥ 60% of users return at least once a week, measured by weekly active users / total users in the first cohort."

### 7. Constraints

Hard constraints the project must respect: regulatory, technical, organizational, budgetary, timeline. One bullet per constraint. Soft preferences belong elsewhere or in the architecture doc; this section is for what must be true regardless of design choices.

### 8. Prior art and alternatives considered

Two or three paragraphs naming what already exists in this space, what's been tried, and why this project is a meaningfully different bet. This section keeps the value hypothesis honest: if the alternatives column is empty, the author probably hasn't looked.

### 9. Open questions

A bulleted list of things the vision can't yet answer. Each open question is a candidate for the wave doc's assumptions register and gets revisited by every redraft cycle. Be specific — not "monetization unclear" but "do we charge per-user or per-team, and at what point in the funnel does pricing surface?"

A freshly drafted vision usually has 5-15 open questions. A vision with zero open questions is suspicious — either the author is overconfident or the doc has been over-edited and the honest gaps have been laundered out.

### 10. Core journeys (optional)

For product-heavy projects where users navigate flows that span multiple modules, include 1-3 *core journeys* — short end-to-end walkthroughs that name what a role actually does to get value. The journeys inform `architect-draft`'s module decomposition and key interfaces, and they inform `wave-draft`'s choice of W1 walking-skeleton path.

For each journey, use this lightweight format:

```markdown
**CJ-<N>: <journey name>**
Role: <which role from §2>
Trigger: <what starts this journey>
Steps:
1. <user action> → <system response>
2. <user action> → <system response>
3. ...
Outcome: <what "done" looks like for this role>
Friction now: <what makes this hard or impossible today>
```

Three guidelines:

- **Keep journeys short.** 4-7 steps. If a journey is sprawling, it's actually two journeys; split.
- **Name friction.** The "Friction now" line is load-bearing — it is what tells the architect *why* a particular module or interface matters. A journey with no friction line is decoration, not signal.
- **Don't enumerate every variant.** The journeys here are *core* — the 1-3 paths that, if the system supports them well, demonstrate the value hypothesis. Edge cases and minor flows belong in the wave doc as stories.

Skip this section when:
- The product is primarily an infra/tech tool (CLI, build tool, library) where users don't navigate a flow.
- The vision is genuinely too thin to commit to journeys yet — list candidate journeys in Open Questions instead and revisit at the next vision-pivot.

## 4. Pivot semantics

A pivot is a revision of the vision doc that changes the value hypothesis, the in-scope set, the non-goals, the target users, or the success metrics in a way that invalidates downstream artifacts. Adding a new open question is not a pivot. Tightening a success metric numerically is usually not a pivot. Realizing the wrong roles were named is a pivot.

`vision-pivot` is the only skill allowed to edit the vision body. When it does:

1. Edit the affected sections in place.
2. Frontmatter `vision_version` is incremented; `last_updated` is set to today; `status` is set to `pivoted`.
3. A change-log entry is appended (Section 5 of the doc) describing what changed and why.
4. Out-of-band: `vision-pivot` triggers a cascading reconciliation in the wave doc and architecture doc — but it does not edit those artifacts itself. Reconciliation is the next `wave-redraft` cycle's job.

Status returns to `active` only after a wave-redraft cycle has produced a reconciled wave doc that is consistent with the new vision. This is the only mechanism for clearing pivoted status.

## 5. Change log

A vision doc with `vision_version: 1` has no change log. Versions 2+ carry a change-log section appended at the end.

```markdown
## Change log

### 2026-06-15 — Pivot v3
Type: pivot
- Section 2 (Target users): role "Solo organizer" replaced with "Group of co-organizers". The W3 audit revealed the single-organizer model is rejected by every observed real club.
- Section 3 (Value hypothesis): rewritten around shared organizing as the central value, not solo convenience.
- Section 4 (In scope): added "co-ownership and handoff of clubs"; removed "single-organizer onboarding wizard".
- Section 5 (Non-goals): added "We do not support nested sub-clubs" to forestall a recurring scope-creep request.
- Section 6 (Success metrics): metric M2 ("weekly active users") replaced with M4 ("weekly active clubs with ≥ 2 active organizers"); old text preserved as M2 (retired).
- Triggers downstream reconciliation. Vision status: pivoted until next wave-redraft.
```

The change log is append-only. Old metric names, old role names, and old non-goals are preserved as superseded entries with new IDs (e.g., M2-retired, M4-new). The doc carries its own history of what was once true.

## 6. Invariants

Rules every reader and writer must honor.

1. **The vision doc is short by design.** Pressure to grow it past two pages of body content is a symptom; the symptom is usually that someone is trying to specify in the vision rather than in the wave doc. Push back.
2. **The vision doc captures intent, not implementation.** Architecture commitments belong in the architecture doc, not here. Wave plans belong in the wave doc, not here.
3. **Only `vision-pivot` writes to the body.** `vision-shaper` writes the initial draft; nothing else writes after that.
4. **Every body change carries a change-log entry.** Silent edits violate the contract.
5. **Pivoted status is cleared only by a successful wave-redraft cycle.** This guarantees the downstream artifacts catch up before the project is treated as stable again.
6. **Open questions are first-class.** They never become invisible; they get migrated to the wave doc's assumptions register or addressed by a subsequent vision-pivot.
7. **Non-goals are sticky.** Removing a non-goal is itself a pivot — it broadens the project. The change-log entry must say so explicitly.

## 7. Worked mini-example

A short vision doc for a hypothetical project, shown to make the schema concrete.

```markdown
---
vision_version: 1
created: 2026-05-02
last_updated: 2026-05-02
status: active
---

# bookclub — Vision

## 1. Problem
Casual reading groups (4-12 people) struggle to coordinate which book to read next, when to meet, and what they discussed last time. Group chats lose state; spreadsheets feel heavy; no one wants to be the permanent organizer. Existing tools optimize for large public communities, not small private clubs.

## 2. Target users
| Role      | What they're trying to do                            | Why this product helps |
|-----------|------------------------------------------------------|------------------------|
| Organizer | Run a club without permanently being "the one"      | Club state lives in the system, not in their head |
| Member    | Vote, RSVP, see what's next, see what was discussed | Less group-chat noise; one place to look |

## 3. Value hypothesis
If we give small private book clubs a lightweight tool that owns the *state* of the club (next book, next meeting, last discussion), members will return weekly to interact with that state, because the alternative — re-deriving state from a noisy group chat — is the bottleneck that kills most clubs by month four.

## 4. In scope
- Create a private club with members.
- Nominate and vote on the next book.
- Schedule and RSVP to meetings.
- Capture lightweight notes / takeaways from each meeting.
- Browse archive of past meetings.

## 5. Non-goals
- Public clubs or discoverability — this is private-only.
- Real-time chat — clubs already have group chats.
- E-commerce / book purchases — out of scope, defer to bookstores.
- AI summarization of meetings — interesting but not differentiated.

## 6. Success metrics
- M1: ≥ 60% of clubs created in cohort A are still active 90 days later (active = ≥ 1 vote or RSVP in the prior 30 days).
- M2: median ≥ 4 of 6 members vote in any active poll.
- M3: ≥ 70% of meetings have at least one captured note within 72h of meeting time.

## 7. Constraints
- Solo dev, 6-month build window for v1.
- Hosting budget under $50/month.
- No location-data collection (privacy-by-design).

## 8. Prior art and alternatives considered
- Bookclubs.com: optimized for public discovery; heavy onboarding for what should be a 5-minute setup.
- Goodreads groups: discussion threads, but no scheduling or voting flow.
- Group chat + shared spreadsheet: the status quo; works until it doesn't, around month four when state-loss compounds.

## 9. Open questions
- OQ1: Are members willing to install an app, or does this need to be web-only / link-only?
- OQ2: Single-choice voting or ranked-choice for picking the next book?
- OQ3: Do clubs want a single permanent organizer or rotating organizing duties? (Affects role model.)
- OQ4: How important is asynchronous discussion (comments on past meetings) vs. just notes?
- OQ5: Do members want a way to see *other* people's clubs they're part of in one place?
```

A freshly drafted vision should look approximately like this — short, opinionated, with a real list of open questions seeded for the wave doc to inherit.

---

This schema is the contract. If a skill needs to deviate, the schema changes first.
