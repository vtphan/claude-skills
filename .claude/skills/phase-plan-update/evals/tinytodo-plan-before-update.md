---
plan_version: 1
created: 2026-04-22
last_updated: 2026-04-22
source_requirements: tinytodo-requirements.md
current_phase: P1
status: in_progress
---

# tinytodo — Implementation Plan

## 1. Goal and guardrails
A small local CLI for managing a personal todo list, stored in a single JSON file in the user's home directory. The point is zero friction: `tinytodo add "buy milk"` and done. Non-goals: sync, collaboration, GUI, mobile, integrations with any external system. Success: a user can manage a list of ~100 todos with no noticeable latency and no data loss on interrupted writes.

## 2. Requirements coverage
| Requirement | Delivered by | Notes |
|-------------|--------------|-------|
| US-USR-1 (add a todo) | P1 | |
| US-USR-2 (list todos) | P1 | |
| US-USR-3 (mark done) | P1 | |
| US-USR-4 (edit a todo) | P2 | |
| US-USR-5 (set priority) | P2 | |
| US-USR-6 (tag todos) | P3 | |
| F-1 (JSON storage)    | P1 | |
| F-2 (CLI interface)   | P1 | |

## 3. Phases overview
| Phase | Name                       | Status      | One-line goal |
|-------|----------------------------|-------------|---------------|
| P1    | Core add/list/done         | in_progress | A user can add, list, and complete todos. |
| P2    | Editing and priority       | future      | Todos can be edited and ordered by priority. |
| P3    | Tags and filtering         | future      | Todos carry tags; list can filter by tag. |

## 4. Phases (detailed)

### P1 — Core add/list/done
Status: in_progress
Started: 2026-04-22
Goal: A user can add, list, and mark-done todos from the command line, with state persisted in a JSON file.
Covers: US-USR-1, US-USR-2, US-USR-3, F-1, F-2
Depends on: none
Entry criteria: none (greenfield project).
Exit criteria:
- `python -m tinytodo add "buy milk"` adds a todo and prints a short confirmation.
- `python -m tinytodo list` prints all todos with their IDs and status (open/done).
- `python -m tinytodo done <id>` marks the todo with that ID as done.
- All state persists across invocations in a JSON file at `~/.tinytodo.json` (or `$TINYTODO_FILE` if set, for testing).
- Writes are atomic — interrupting a write does not corrupt the file.
- End-to-end test script exercises add → list → done → list and verifies the expected output.
Assumptions: A1
Risks: R1

#### Tasks
- [x] T1.1 — Project scaffold and CLI argument parsing.
      Acceptance: `python -m tinytodo --help` prints usage listing at least `add`, `list`, `done` subcommands and exits 0. `python -m tinytodo` with no args prints help and exits non-zero.
      Touches: `tinytodo/__init__.py`, `tinytodo/__main__.py`, `tinytodo/cli.py`, `pyproject.toml`.
- [x] T1.2 — JSON storage layer with atomic writes.
      Acceptance: A `Store` abstraction reads/writes a JSON file. Writes go through a temp file + `os.replace` so a crash mid-write cannot produce a partial file. A unit test simulates reading after an interrupted write (temp file exists, real file is old) and verifies the old file is still valid.
      Touches: `tinytodo/store.py`, `tests/test_store.py`.
- [x] T1.3 — Add and list commands.
      Acceptance: `add "X"` appends a todo with a new integer ID and status "open", printing "Added #<id>: X". `list` prints one line per todo in the format `[<status>] #<id> <text>` (status is `x` for done, ` ` for open). Ordering is by ID ascending.
      Touches: `tinytodo/cli.py`, `tests/test_cli.py`.
- [x] T1.4 — Done command + end-to-end test.
      Acceptance: `done <id>` sets the matching todo's status to done, prints "Done #<id>". Unknown IDs produce a clear error message and exit non-zero. An end-to-end test script (`tests/test_e2e.py`) uses a temporary `$TINYTODO_FILE`, adds two todos, lists them (both open), marks the second done, lists again (first open, second done), and asserts all output matches expectation.
      Touches: `tinytodo/cli.py`, `tests/test_e2e.py`.

### P2 — Editing and priority
Status: future
Goal: Users can edit a todo's text and assign a priority; list displays high-priority items first.
Covers: US-USR-4, US-USR-5
Depends on: P1
Entry criteria: P1 closed out; JSON schema stable.
Exit criteria:
- `edit <id> <new text>` updates a todo's text.
- `priority <id> <high|med|low>` sets a priority.
- `list` sorts by priority desc, then by ID asc.
Assumptions: A2
Sketch: Add `priority` field to the JSON schema with default "med"; migrate existing todos on read. Add two subcommands; update list ordering.

### P3 — Tags and filtering
Status: future
Goal: Users can attach tags to todos and filter the list by tag.
Covers: US-USR-6
Depends on: P2
Entry criteria: P2 closed out.
Exit criteria:
- `tag <id> <tag>` attaches a tag; tags are comma-joined strings.
- `list --tag <tag>` filters output.
Assumptions: A3
Sketch: Add a `tags` list field to each todo. Add `tag` subcommand and a `--tag` filter on list.

## 5. Assumptions register
- **A1** — A single JSON file is sufficient for typical list sizes (~100 todos). *Phase: P1. Status: untested.*
- **A2** — Three priority levels (high/med/low) are enough; users won't need custom ordering. *Phase: P2. Status: open.*
- **A3** — Tags are flat strings, not hierarchical. *Phase: P3. Status: open.*

## 6. Risks register
- **R1** — Concurrent writes from two terminal sessions could race. *Phase: P1. Likelihood: low. Impact: low.* *Mitigation: document as a known limitation; no locking in MVP.*

## 7. Change log

### 2026-04-22 — Plan created
Type: initial-draft
- Drafted for greenfield tinytodo CLI project.
- Three phases, P1 fully planned, P2–P3 sketched.
- 3 assumptions and 1 risk seeded.
