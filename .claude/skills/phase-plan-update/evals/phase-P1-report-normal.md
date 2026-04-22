# P1 Core add/list/done — Implementation Report
Phase: P1
Completed: 2026-04-22
Plan version at start: 1

## What was built
A user can now manage a personal todo list from the command line with three
subcommands: `python -m tinytodo add "<text>"`, `python -m tinytodo list`,
and `python -m tinytodo done <id>`. State is persisted in a JSON file at
`~/.tinytodo.json`, or at the path in `$TINYTODO_FILE` when set (used by the
tests). Writes go through a same-directory temp file and `os.replace`, so an
interrupted write cannot leave the real file truncated or partial. The CLI
covers the phase's three user stories — US-USR-1 (add), US-USR-2 (list),
US-USR-3 (mark done) — and the two feature slices F-1 (JSON storage) and
F-2 (CLI interface). All four P1 tasks (T1.1–T1.4) are complete.

## Task status
- [x] T1.1 — Project scaffold and CLI argument parsing. Done. `python -m
      tinytodo --help` lists `add`, `list`, `done` and exits 0; running with
      no args prints help and exits with code 2 (non-zero).
- [x] T1.2 — JSON storage layer with atomic writes. Done. `tinytodo/store.py`
      implements `Store` with a temp-file + `os.replace` write path and
      `fsync` before rename. `tests/test_store.py` has 8 tests, including
      one that monkey-patches `os.replace` to raise mid-write and verifies
      the on-disk file is byte-identical to its pre-crash contents, and one
      that plants a garbage orphan temp file next to the real file and
      verifies reads still see the valid old file.
- [x] T1.3 — Add and list commands. Done. `add "X"` appends with a new
      integer ID and status `open`, prints `Added #<id>: X`. `list` prints
      one line per todo in the exact format `[<status>] #<id> <text>`
      (status is `x` for done, single space for open) ordered by ID
      ascending. Covered by 5 tests in `tests/test_cli.py`.
- [x] T1.4 — Done command + end-to-end test. Done. `done <id>` flips the
      matching todo's status and prints `Done #<id>`; unknown IDs print
      `Error: no todo with ID <id>` to stderr and exit 1. `tests/test_e2e.py`
      launches the CLI via subprocess against a temporary `$TINYTODO_FILE`
      and walks through add → list → done → list, asserting exact output.

## Assumptions status
- A1 (a single JSON file is sufficient for ~100 todos): **untested at scale**
  in this phase. The code is correct at the sizes used by tests (≤ 3 todos),
  but no benchmark against ~100 todos was run — P1's exit criteria didn't
  require one. Status stays `untested`; a small timing test would cheaply
  validate it before P2 closes if desired.

## Discoveries
- Atomic-write testing shape: simulating "crash mid-write" is cleanest by
  monkey-patching `os.replace` to raise *after* the temp file has been
  written. This reliably reproduces the "real file is old, orphan temp
  file exists" state the acceptance criterion describes, without needing
  `os.kill` gymnastics. Worth reusing if future phases add more write
  paths (e.g., P2's `edit`).
- The on-disk JSON shape chosen is `{"next_id": <int>, "todos": [...]}`
  rather than a bare list. This keeps ID allocation monotonic even after
  todos are deleted (none deleted in P1, but P2/P3 may need it), and means
  `list` output ordering doesn't depend on insertion order in the array.
  Not a scope change — within T1.3's remit — but the updater should know
  the schema key names so P2's `priority` migration can be specified
  precisely: "add a `priority` field to each item in `todos`, default
  `med`; read-path fills it in if missing."
- `argparse` in Python 3.9+ changed how missing-subcommand failures are
  reported vs. 3.7. The scaffold currently uses the explicit `dest="command"`
  + `if args.command is None: print_help(); return 2` pattern so the
  acceptance criterion "no-args prints help and exits non-zero" behaves
  identically across versions — worth preserving through P2's CLI edits.

## Proposed scope changes
None. All P1 tasks met their acceptance criteria without needing to touch
future-phase work.

## Risks encountered
- R1 (concurrent writes from two terminals could race) did not materialize
  and was not exercised. The MVP keeps it as a known limitation per the
  plan's mitigation. The atomic-write path means a race cannot corrupt the
  file, but it can still lose an update (last writer wins). No action
  proposed for P2.

## Readiness for next phase
- P2 will add an `edit` subcommand and a `priority` field. The store's
  read path already tolerates missing keys (see `_load` defensive
  defaults), so adding `priority` with a default of `med` on read should
  be a one-line change — no explicit migration step needed. Worth noting
  explicitly in P2's sketch if the updater expands it.
- The current CLI dispatch in `tinytodo/cli.py` uses a simple
  `if args.command == "..."` ladder. Adding two subcommands is fine at
  this size; if P3 adds filtering flags to `list`, a small refactor to a
  command-handler dict may be worth it. Not required now.
- Test layout (`tests/test_store.py`, `tests/test_cli.py`, `tests/test_e2e.py`)
  is set up so `python -m unittest discover tests` runs everything. P2 can
  add `tests/test_priority.py` and similar without changing the runner.
