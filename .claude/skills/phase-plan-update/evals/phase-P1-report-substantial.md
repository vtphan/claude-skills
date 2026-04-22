# P1 Core add/list/done — Implementation Report
Phase: P1
Completed: 2026-04-22
Plan version at start: 1

## What was built
A working CLI with `add`, `list`, and `done` subcommands backed by a single
JSON file. All four P1 tasks completed at the code level. Covers US-USR-1,
US-USR-2, US-USR-3, F-1, F-2.

During a pre-release dogfood with three users, we observed that two of the
three use tinytodo as their *primary* task tracker (not just a weekend-
project TODO list) and one has 1,800+ items accumulated from migration from
a previous tool. This reshapes what we thought tinytodo was.

## Task status
- [x] T1.1 — Done.
- [x] T1.2 — Done.
- [x] T1.3 — Done.
- [x] T1.4 — Done.

## Assumptions status
- **A1 (single JSON file sufficient for ~100 todos): broken.** Dogfood
  showed real-world list sizes of 500-2000 items. At 1800 items, `list`
  takes ~320ms to render on a modern laptop; `add` latency jumps to ~180ms
  because every write rewrites the entire file. Users noticed. Recommend
  replacing A1 with a new assumption: the data layer should support list
  sizes up to ~5000 items without degrading interactive latency below
  100ms p95, implying a move to SQLite or a partitioned-file approach.
- A2 (three priority levels enough): untested — P1 didn't exercise priority.
- A3 (flat string tags): untested — P1 didn't exercise tags.

## Discoveries
- **Real list sizes are 10-20x larger than the plan assumed.** This is the
  biggest discovery and it propagates into every future phase:
  - P2 (editing/priority): list ordering now a hot path, needs indexing.
  - P3 (tags/filtering): filter queries on 2000 items need to be fast;
    full-scan on every `list --tag` is not acceptable.
- **Data migration is now a first-class concern.** Users who have large
  existing lists in other tools want to import them. This wasn't in any
  phase; likely belongs in a new phase between current P1 and current P2.
- SQLite is probably the right storage. Python ships it; file-per-user
  model still works; indexed queries solve both the list-render and
  tag-filter performance problems.

## Proposed scope changes
- **Add**: a new data-migration capability — take a CSV or plaintext file
  and import as todos. Needed because of user demand observed in dogfood.
  Candidate placement: a new phase between P1 and current P2.
- **Add**: switch the storage layer from JSON-file to SQLite. Consequences
  propagate: P2's priority ordering becomes an indexed ORDER BY, P3's tag
  filtering becomes a JOIN. Candidate placement: front of the new phase.
- **Remove from P2**: the "migrate existing todos on read" part of the
  sketch; SQLite + migration change this mechanism entirely.
- **No change to the goal.** Tinytodo is still a zero-friction personal
  CLI; we just learned the real scale.

## Risks encountered
- R1 (concurrent writes racing) did not materialize in P1; dogfood didn't
  use concurrent sessions. Status unchanged.
- New risk: SQLite migration breaks existing JSON files. Mitigation: a
  one-shot converter that runs on first post-migration invocation.

## Readiness for next phase
Before proceeding to what is currently P2 (editing/priority), the storage
pivot should land. Suggest a new current phase for that work. Current P2
and P3 scopes should be revised to assume SQLite as the storage layer.
