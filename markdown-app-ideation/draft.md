# Viewer-First macOS Markdown App

## Idea

Build a macOS markdown app tailored for communicating with AI via markdown documents. Existing free macOS markdown apps don't fit. The dominant use pattern is reading docs written by AI, with occasional targeted edits — so the app should optimize for reading first, and make jumping into edit cheap when needed.

## Current Proposal

- **Viewer is the default; editor is contextual.** Two distinct modes, never side-by-side. Reading position is preserved across edit round-trips.
- **Workspace = a chosen folder.** All `.md`/`.yaml` files within are addressable. File-watch and `Cmd+P` fuzzy-find are scoped to the workspace.
- **Home screen is a typographic full-screen index** of recent docs from the workspace. Appears when no doc is open (launch with no restored state, or after closing the last doc). Click to open; close all docs to return.
- **Edit gesture: select-then-confirm.** After a text selection in viewer, a small contextual popover offers two actions: **highlight** (keep selection for native `Cmd+C`) or **edit** (enter edit mode at the selection start). The toolbar "edit" icon enters edit mode at the start of the file.
- **Editor opens the whole file** with cursor at the chosen position. iA Writer–style focused writing: minimal chrome, generous typography, no preview, no toolbar-driven markdown insertion. `Esc` saves and returns to viewer.
- **No visible tab bar.** Multi-doc switching via `Cmd+P` fuzzy-find. Merge All Windows still consolidates separate single-doc windows into one. A subtle, hideable bottom status bar shows: **open-tab count, word count, character count**.
- **Viewer navigation:** continuous scroll. `PgDn`/`PgUp` jump to next/previous heading. `Cmd+F` opens find scoped to the current doc, matching against rendered text.
- **Silent persistence + state restore.** Autosave on `Esc`, tab switch, and quit. No save dialog or unsaved indicator. On launch, restore open tabs and per-tab scroll positions. If a file changed on disk since close, reopen at top. If a file is missing, show a dismissable "missing" placeholder tab. File-watch auto-refreshes on external changes if no local edits; one-key reload prompt otherwise.
- **Content rendering.** Markdown flavor is **GFM**. Lang-aware syntax highlighting in code blocks (tokenizer choice deferred). Images render at natural size capped to content width, lazy-load below fold, click → macOS Quick Look.
- **Typography is a primary feature.** Tasteful, opinionated defaults — Steve Jobs aesthetic. Font and size controls minimal, not configurable.
- **No AI integration.** Content-source-agnostic.
- **YAML is a peer format** with the same viewer/editor split. Viewer affordances: tree-collapse on object/array nodes, subtle type hints.

## Rationale

- Reading and writing are different cognitive tasks; split-view is noise when only one is active.
- Workspace-as-folder simplifies file flow: no "where is my file" friction, file-watch is naturally scoped, fuzzy-find runs over a bounded set. Trade-off: opening files outside the workspace becomes a separate flow — see Q2.
- Home-screen-as-index treats "which doc to read" as a designed surface, not an afterthought — the user lands somewhere intentional.
- Select-then-confirm sidesteps the click-vs-edit gesture conflict: text selection is the canonical first move (familiar macOS gesture), and the popover lets the user choose what they actually want. Avoids forcing one default that breaks the other use.
- Edit mode opens the whole file with cursor at click — single rule, since positional click-to-source mapping is computationally cheap (markdown ASTs carry source byte offsets natively, O(1) per click).
- Writing affordance is contextual (click-to-edit), not GUI-driven. Keeps editor focused.
- `Cmd+P` fuzzy-find replaces the tab bar; bottom status bar earns its space by surfacing the small set of stats the user named.
- Continuous scroll with `PgDn`/`PgUp` heading-jump preserves natural reading flow and adds outline-aware skipping for AI docs.
- The differentiator vs. existing free apps is *taste*, not features — opinionated defaults over configurability (Steve Jobs aesthetic).
- File-watch scoped to the workspace folder directly serves the AI-writes-the-doc workflow.
- No AI integration keeps the surface small and durable.
- YAML kept as its own pipeline because rendering it as markdown would strip its structural affordances.
- Click-to-copy features intentionally omitted as overengineering. Native macOS text-select + `Cmd+C` remains the way to copy any rendered text.
- Assumes: the popover's "highlight" means "keep selection for native copy," not persistent annotations. Persistent highlights would be a new feature with their own state surface — see Q1.
- Assumes: opening files outside the workspace is rare; switching workspace suffices when needed. If users frequently want one-off external files, the flow needs a transient-open path — see Q2.
- Assumes: a single workspace at a time is enough. Multi-workspace via separate windows is plausible but not yet specified — see Q3.

## Clarifying Questions

1. **[highlight semantic]** In the select-then-confirm popover, what does "highlight" do? Read it conservatively: dismiss the popover, leave the selection intact, user can `Cmd+C` natively. The other reading is "save a persistent highlight" (annotation that lives on the doc across sessions), which would need a state surface. Which did you mean — (a) keep-selection-only or (b) persistent annotation?
2. **[opening files outside the workspace]** What happens when the user wants to open a file outside the current workspace folder? (a) only workspace files are addressable, "switch workspace to read elsewhere"; (b) `File → Open…` is still available for a transient one-off, opening as a tab without joining the workspace; (c) opening a file outside auto-switches the workspace to its containing folder. (a) is purest; (b) most flexible; (c) most automatic.
3. **[multi-workspace]** Single workspace at a time, with explicit switch action? Or multiple workspaces openable in separate windows (one per window)? Affects whether "switch workspace" is destructive or window-multiplying.

## Incremental Improvements

1. **YAML frontmatter handling in markdown viewer.** Many .md files start with `---\n…\n---` frontmatter. Decide a default: render as a subtle metadata strip above the doc (collapsed by default), hide entirely, or show as a code block. AI-generated docs often include frontmatter; getting this wrong looks unpolished.
2. **First-launch workspace picker.** First launch needs a designed welcome flow: invite the user to choose a folder, suggest a sensible default (e.g., `~/Documents/Markdown`), offer to create it if missing. Without this, the very first session is "where do I even start?"
3. **Theme model.** Three modes: light, dark (auto-follow macOS appearance by default), plus an optional sepia for long reads. No per-knob configuration. Aligns with the no-config Steve Jobs principle while still supporting the modes long-form readers actually want.

## Transformative Improvements

1. **Workspace = git repo (or git-friendly).** Reframe the workspace as a git-aware folder. Auto-stage and commit doc changes (or surface git status if the user is doing it themselves); offer "view history" on a doc to see how it evolved. Pulls in the "what's new since last read" benefit (which you rejected as a feature) via a known mechanism — diffing commits — rather than an app-specific state surface. Tests whether the workspace concept has more shape than just "a folder."
2. **Drop YAML peer support; markdown only for v1.** Re-question YAML as peer-class. YAML viewing/editing as a separate pipeline is real scope (separate viewer, separate editor, separate affordances). If AI communication is mostly markdown — which most chat UIs emit — YAML could ship in v2 or be delegated to other tools. Tests whether YAML earns its way into v1, or whether scope-cutting it would let the markdown experience get more attention.
3. **No tabs — browser-style history navigation.** Replace the open-tabs concept entirely with a doc-visit history: `Cmd+P` jumps to a doc, `Cmd+[` / `Cmd+]` go back/forward through visit history, no "currently open set." Tests whether multi-tab is actually load-bearing — you read one doc at a time, and `Cmd+P` already gets you anywhere. Tabs may be cargo-culted from web browsers.

## Decisions

**Taken:**
- No AI integration; the app is content-source-agnostic.
- **Workspace = a chosen folder.** All `.md`/`.yaml` files within are addressable; `Cmd+P` fuzzy-find and file-watch are scoped to the workspace.
- **Home screen is a typographic full-screen index** of recent workspace docs; appears when no doc is open.
- Edit mode opens the whole file with cursor at the click/selection point (single rule).
- **Edit gesture is select-then-confirm:** after a text selection in viewer, a popover offers **highlight** (keep selection for native `Cmd+C`) or **edit** (enter edit mode at selection start). Toolbar "edit" icon enters at the start of the file. (Replaces the earlier "double-click or click-then-`⏎`" formulation.)
- Editor mode is iA Writer–style focused writing; `Esc` saves and returns to viewer.
- No toolbar-driven markdown insertion; writing affordance is contextual (click-to-edit).
- No visible tab bar; multi-doc switching via `Cmd+P` fuzzy-find. Merge All Windows consolidates separate windows. **Bottom status bar shows: open-tab count, word count, character count.**
- Viewer navigation: continuous scroll; `PgDn`/`PgUp` jump to next/previous heading; `Cmd+F` find scoped to current doc, matching rendered text.
- Reading typography is a primary feature; font/size controls minimal but tasteful (Steve Jobs aesthetic — opinionated defaults, not configurability).
- Reading place is preserved across edit round-trips.
- Autosave on `Esc`, tab switch, and quit; no save dialog or unsaved indicator.
- State restore on launch: open tabs and scroll positions. If a file changed on disk, reopen at top. If a file is missing, show a dismissable "missing" placeholder tab.
- File-watch over the workspace folder: auto-refresh on external changes if no local edits; one-key reload prompt otherwise.
- **Markdown flavor: GFM.** Lang-aware code-block syntax highlighting (tokenizer deferred). Images render at natural size capped to content width, lazy-load below fold, click → macOS Quick Look.
- YAML is a peer format with the same viewer/editor split; viewer affordances include tree-collapse and subtle type hints.
- Click-to-copy as a feature class is dropped; native macOS text-select + `Cmd+C` is the way to copy.

**Set aside:**
- **Drop-the-editor / external editor handoff** — editor stays in-app.
- **Tabs-as-projects** — adds a "project" concept without clear payoff.
- **Render YAML through the markdown engine** — would strip YAML's structural affordances.
- **Renderer as standalone library / app as thin shell** — out of MVP scope.
- **Click-to-copy as a feature class** (heading anchors, code blocks, tables, links, YAML key-paths) — overengineering for a viewer-first app.
- **Doc as a revision stream / "what's new since last read"** — rejected.
- **No app-side state** (state in markdown HTML comments) — rejected.
- **One-mode live preview** — user prefers a refined, dedicated viewer mode over always-rendered editing.

## Notes

>Additional idea: do you think this app should target both Markdown and Yaml documents?  I think these two formats are popular for AI/LLM to communicate with human codesigners.
