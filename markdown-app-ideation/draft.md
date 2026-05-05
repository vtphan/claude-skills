# Viewer-First macOS Markdown App

## Idea

Build a macOS markdown app tailored for communicating with AI via markdown documents. Existing free macOS markdown apps don't fit. The dominant use pattern is reading docs written by AI, with occasional targeted edits — so the app should optimize for reading first, and make jumping into edit cheap when needed.

## Current Proposal

- **Viewer is the default; editor is contextual.** Two distinct modes, never side-by-side. Reading position is preserved across edit round-trips.
- **No workspace concept.** Files are opened directly via `File -> Open...`, drag/drop, Finder, or recent files. The app does not ask the user to choose a folder and does not crawl a project directory.
- **Home screen is a typographic full-screen recent-files index.** Appears when no doc is open (launch with no restored state, or after closing the last doc). Click to open; close all docs to return.
- **Edit gesture: select-then-confirm.** After a text selection in viewer, a small contextual popover offers two actions: **highlight** (keep selection for native `Cmd+C`) or **edit** (enter edit mode at the selection start). The toolbar "edit" icon enters edit mode at the start of the file.
- **Editor opens the whole file** with cursor at the chosen position. iA Writer–style focused writing: minimal chrome, generous typography, no preview, no toolbar-driven markdown insertion. `Esc` saves and returns to viewer.
- **No visible tab bar.** Multi-doc switching via `Cmd+P` fuzzy-find over open and recent files. Merge All Windows still consolidates separate single-doc windows into one. A subtle, hideable bottom status bar shows: **open-tab count, word count, character count**.
- **Viewer navigation:** continuous scroll. `PgDn`/`PgUp` jump to next/previous heading. A transient outline palette jumps within the current doc. `Cmd+F` opens find scoped to the current doc, matching against rendered text.
- **Silent persistence + state restore.** Autosave on `Esc`, tab switch, and quit. No save dialog or unsaved indicator. On launch, restore open tabs and per-tab scroll positions. If a file changed on disk since close, reopen at top. If a file is missing, show a dismissable "missing" placeholder tab. File-watch auto-refreshes open files on external changes if no local edits; one-key reload prompt otherwise.
- **Content rendering.** Markdown flavor is **GFM**. Lang-aware syntax highlighting in code blocks (tokenizer choice deferred). Images render at natural size capped to content width, lazy-load below fold, click → macOS Quick Look.
- **Frontmatter is rendered as document metadata, not body prose.** Markdown frontmatter appears in a visually distinct treatment at the top of the rendered doc.
- **Typography is a primary feature.** Tasteful, opinionated defaults — Steve Jobs aesthetic. Font and size controls minimal, not configurable.
- **No AI integration.** Content-source-agnostic.
- **YAML is a sibling experience, not markdown stretched sideways.** YAML viewer is a polished structural tree with collapse and subtle type hints; YAML editor is raw text in v1.

## Rationale

- Reading and writing are different cognitive tasks; split-view is noise when only one is active.
- Removing workspace cuts product ceremony: no folder picker, no project boundary, no argument about files "inside" or "outside" the app. Trade-off: fuzzy-find becomes recent/open-file based, not a complete filesystem index.
- Home-screen-as-recent-index treats "what was I reading?" as the designed empty state, not a project dashboard.
- Select-then-confirm sidesteps the click-vs-edit gesture conflict: text selection is the canonical first move (familiar macOS gesture), and the popover lets the user choose what they actually want. Avoids forcing one default that breaks the other use.
- Edit mode opens the whole file with cursor at click — single rule, since positional click-to-source mapping is computationally cheap (markdown ASTs carry source byte offsets natively, O(1) per click).
- Writing affordance is contextual (click-to-edit), not GUI-driven. Keeps editor focused.
- `Cmd+P` fuzzy-find replaces the tab bar; limiting it to open and recent files keeps the no-workspace model simple.
- Continuous scroll with `PgDn`/`PgUp` heading-jump plus a transient outline palette preserves natural reading flow while making long AI docs navigable.
- The differentiator vs. existing free apps is *taste*, not features — opinionated defaults over configurability (Steve Jobs aesthetic).
- File-watch should attach to open files, not a folder tree; this preserves external-edit awareness without reintroducing workspace machinery.
- No AI integration keeps the surface small and durable.
- YAML kept as its own sibling pipeline because structural inspection is the value; v1 keeps YAML editing raw to avoid building a second full editor.
- Click-to-copy features intentionally omitted as overengineering. Native macOS text-select + `Cmd+C` remains the way to copy any rendered text.
- Assumes: the popover's "highlight" means "keep selection for native copy," not persistent annotations. Persistent highlights would be a new feature with their own state surface.
- Assumes: recent/open-file discovery is enough for a viewer-first app. If users need to browse hundreds of unopened docs, the no-workspace model will need a separate file-discovery surface.

## Clarifying Questions

1. **[file discovery]** Without a workspace, what should `Cmd+P` search: only currently open tabs, open + recent files, or open + recent + files from standard macOS recent-document APIs? This is now the main discovery boundary.
>Remove Cmd+P.  Cmd+F is searching for things in the current file.
>
2. **[recent index]** How should the home screen decide which recent files to show: last opened by this app only, Finder/system recents, or pinned + recent? The choice determines whether the home screen feels private and app-specific or more ambient.

3. **[YAML structure]** In the YAML viewer, are arrays/objects enough, or should scalar values also get light type treatment such as string/number/bool/null badges? This is the thin line between tasteful structural view and noisy inspector.

## Incremental Improvements

1. **Open-flow polish** — Make drag/drop, Finder "Open With", and `File -> Open...` first-class routes that all land in the same viewer state. Removing workspaces raises the bar for ordinary file opening to feel excellent.
2. **Recent-file pinning** — Add a small pin affordance on the home index so repeatedly used AI/codesign docs do not churn out of view. This preserves a light organizing primitive without becoming a workspace.
3. **Frontmatter treatment** — Render frontmatter as a compact metadata band with a disclosure control: key names visible, values hidden until expanded. This honors "format differently" without turning metadata into body content.

## Transformative Improvements

1. **Document set as manual collection** — Instead of workspaces, let users create named lightweight collections of file aliases. A collection is not a folder crawl; it is a curated reading set. This tests whether organization is needed, but only after rejecting implicit workspace complexity.
2. **Single-document purist mode** — Drop hidden tabs entirely: one window equals one document, recent files handle return, and `Cmd+P` becomes "open recent." This tests whether even hidden multi-doc state is unnecessary for a viewer-first app.
3. **Zero-library app** — Drop the home index entirely. Launch restores prior docs if any; otherwise it shows a native open panel. This tests whether even recent-file curation is more app surface than the viewer-first premise needs.

## Decisions

**Taken:**
- No AI integration; the app is content-source-agnostic.
- **No workspace concept.** Files open directly; the no-doc home screen shows recent files instead of asking for or indexing a folder.
- **Home screen is a typographic full-screen index** of recent files; appears when no doc is open.
- Edit mode opens the whole file with cursor at the click/selection point (single rule).
- **Edit gesture is select-then-confirm:** after a text selection in viewer, a popover offers **highlight** (keep selection for native `Cmd+C`) or **edit** (enter edit mode at selection start). Toolbar "edit" icon enters at the start of the file. (Replaces the earlier "double-click or click-then-`⏎`" formulation.)
- Editor mode is iA Writer–style focused writing; `Esc` saves and returns to viewer.
- No toolbar-driven markdown insertion; writing affordance is contextual (click-to-edit).
- No visible tab bar; multi-doc switching via `Cmd+P` fuzzy-find. Merge All Windows consolidates separate windows. **Bottom status bar shows: open-tab count, word count, character count.**
- Viewer navigation: continuous scroll; `PgDn`/`PgUp` jump to next/previous heading; `Cmd+F` find scoped to current doc, matching rendered text.
- Add a transient document outline palette for jumping within long markdown docs.
- Reading typography is a primary feature; font/size controls minimal but tasteful (Steve Jobs aesthetic — opinionated defaults, not configurability).
- Reading place is preserved across edit round-trips.
- Autosave on `Esc`, tab switch, and quit; no save dialog or unsaved indicator.
- State restore on launch: open tabs and scroll positions. If a file changed on disk, reopen at top. If a file is missing, show a dismissable "missing" placeholder tab.
- File-watch open files: auto-refresh on external changes if no local edits; one-key reload prompt otherwise.
- **Markdown flavor: GFM.** Lang-aware code-block syntax highlighting (tokenizer deferred). Images render at natural size capped to content width, lazy-load below fold, click → macOS Quick Look.
- YAML is a sibling experience with the same viewer/editor split; viewer affordances include tree-collapse and subtle type hints.
- YAML v1 scope is a polished structural viewer plus raw text editor, not YAML-aware editing.
- Treat markdown frontmatter as visually distinct metadata at the top of the rendered doc.
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
- **Workspace as organizing concept** — unnecessary complexity; recent files are enough when no file is open.
- **Workspace-scoped fuzzy-find and file-watch** — removed with the workspace concept; discovery shifts to open/recent files and file-watch shifts to open files.
- **First-launch workspace picker** — deferred because workspace itself is removed from the core model.
- **Folder browser as permanent primary surface** — rejected.
- **Inbox-to-library workflow** — rejected.

## Notes

>Additional idea: do you think this app should target both Markdown and Yaml documents?  I think these two formats are popular for AI/LLM to communicate with human codesigners.
