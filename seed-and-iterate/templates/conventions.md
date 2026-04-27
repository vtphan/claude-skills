# Conventions

Shared rules across all schemas in the seed-and-iterate process. Read this before using any template.

## File format

All schemas are markdown files with optional YAML frontmatter for structured fields. The frontmatter holds machine-readable metadata; the markdown body holds human-readable content.

A typical document looks like:

```markdown
---
id: journey-completing-assignment
title: Completing a homework assignment
persona_refs: [persona-struggling-student]
status: accepted
---

# Completing a homework assignment

[markdown body follows]
```

The frontmatter is delimited by `---` lines at the top. Everything after the second `---` is the body.

## File naming

One artifact per file. Files are named `<type>-<short-slug>.md`. Examples:

- `seed.md` (one per project, no slug needed)
- `context.md` (one per project)
- `goal-first-pilot.md`
- `journey-completing-assignment.md`
- `journey-getting-unstuck.md`
- `story-autosave-progress.md`

Slugs are lowercase, hyphenated, and short. They become part of the stable ID, so renaming a file means renaming references to it elsewhere — change them rarely.

## Stable IDs

Every artifact has a stable ID in its frontmatter. The ID is the filename without the `.md` extension. Examples: `seed`, `context`, `goal-first-pilot`, `journey-completing-assignment`, `story-autosave-progress`.

Within Journey documents, each stage has its own ID nested under the journey ID:

```
journey-completing-assignment#stage-start-problem
journey-completing-assignment#stage-first-attempt
```

Stage IDs are referenced from Story documents to record which journey moment the story serves.

## Cross-references

Cross-references between documents are written as the target's stable ID. They appear in frontmatter fields like:

```yaml
journey_moment_refs: [journey-completing-assignment#stage-first-attempt]
persona_refs: [persona-struggling-student, persona-instructor]
```

In the markdown body, cross-references are written inline as `[journey-completing-assignment#stage-first-attempt]` without backticks, so they remain readable while staying parseable.

## Confidence tags

Sections in AI-drafted documents are tagged with confidence:

- `high` — strong basis from memory, prior work, or domain knowledge.
- `medium` — reasonable inference from available context.
- `low` — guess, please verify.

Tags appear inline at section boundaries, like:

```markdown
### Strategy
*confidence: medium*

[content]
```

Confidence tags are AI-produced. Humans don't need to add them when editing.

## Source tags

Personas, journey stages, and journey insights are tagged with the source of the information:

- `observed` — directly observed by the human (teaching, prior work, etc.).
- `literature` — from published research or reference materials.
- `assumed` — inferred without direct evidence; treat as a working hypothesis.
- `validated` — was previously assumed, now confirmed through validation conversation or pilot data.

Tags appear inline:

```markdown
- *source: observed* Students often switch between problems when stuck.
- *source: assumed* Students prefer hints over peer help when working alone late at night.
```

## Status

Each artifact has a `status` field in frontmatter:

- `draft` — being worked on, not yet committed.
- `accepted` — human has reviewed and committed to current version.
- `superseded` — replaced by a newer version (kept for history but not authoritative).

Downstream skills only read `accepted` artifacts.

## Decision points

AI-drafted documents include a "Decision points" section near the top of the body, listing three to seven specific things the human should react to. Format:

```markdown
## Decision points

1. I drafted three personas; the third is a non-collaborator researcher. Keep or remove?
2. I tagged five assumptions; which can you validate quickly?
3. The strategy says "infrastructure-first" but the journey list includes a content authoring journey — is that a contradiction?
```

The human reads decision points first; the rest of the document can be skimmed.

## Change log

The Seed has a Change log section at the bottom. Other documents can have one too if they evolve enough to warrant it. Format:

```markdown
## Change log

- 2026-04-27: Added "single-section deployment" as constraint after Seed Reader proposed it.
- 2026-04-25: Reframed bet from "rich features" to "infrastructure-first" after reviewing Goal draft.
- 2026-04-23: Initial draft.
```

Most recent entry first. One line per change. Date in ISO format.

## Priority and severity vocabularies

Where priority is used (Stories), values are: `must`, `should`, `could`, `won't`.

Where severity is used (Reviewer findings), values are: `critical`, `major`, `minor`, `nit`.

Stick to these vocabularies; don't introduce new levels without good reason.

## What goes in frontmatter vs. body

Rule of thumb: structural metadata (IDs, refs, status, tags applied to the whole document) goes in frontmatter. Content (prose, bullet lists, sections, inline tags) goes in the body.

If a field is queryable across many documents — "show me all stories with priority `must`" — it should be in frontmatter. If it's only meaningful within one document, it can stay in the body.
