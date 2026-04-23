# Internal Knowledge Hub — Requirements

## 1. Context

The Internal Knowledge Hub is an internal product whose goal is to let anyone at the company find answers to "how do we do X" without having to ask in Slack. Today that institutional knowledge is trapped in chat threads, personal notes, and tribal memory; the hub is meant to make it discoverable, browseable, and — crucially — trustworthy enough that readers can act on what they find.

In scope: anyone can write an article, articles are searchable and browseable by topic, trusted reviewers can **endorse** articles to signal trustworthiness, and articles expire on a refresh cadence so stale content doesn't mislead readers. The system has four roles: **Reader** (everyone), **Author** (anyone writing), **Reviewer** (trusted endorser), and **Admin** (manages topics and reviewer permissions). A person will typically hold multiple roles — e.g., most people are Readers and occasional Authors.

Several design questions were open in the input spec (ownership/editability model, reviewer-selection criteria, and refresh cadence). Where this document had to assume a direction to make stories concrete, the assumption is named here and restated in Open Questions (§7):
- Articles are **single-owner** by default, but the author can grant co-edit rights to named collaborators. Anyone can propose edits via a suggestion mechanism.
- **Reviewers are appointed by Admins**; no automatic promotion based on activity.
- **Refresh cadence is quarterly (every 90 days)** by default, configurable per topic by Admin.

## 2. User roles

| Role | What they're trying to accomplish |
|------|------------------------------------|
| Reader | Find a trustworthy answer to a "how do we do X" question quickly, without asking in Slack. |
| Author | Capture what they know so others can reuse it, with minimal friction. |
| Reviewer | Vouch for articles in their domain so readers know what's trustworthy and current. |
| Admin | Keep the taxonomy coherent and ensure the right people have reviewer rights. |

## 3. User stories

### Reader (role prefix: RDR)

**US-RDR-1: Search for an answer**
As a Reader,
I want to search the hub by keyword and see ranked results,
so that I can find an answer faster than asking in Slack.

Acceptance criteria:
- Given I enter a search term, when I run the search, then I see a ranked list of articles with title, topic, last refresh date, and endorsement status.
- Given an article is endorsed and fresh, when it appears in results, then it is visually distinguished from unendorsed or stale articles.
- Given no articles match, when the search runs, then I see a "no results" state suggesting I browse by topic or author a new article.

Priority: Must-have

**US-RDR-2: Browse by topic**
As a Reader,
I want to browse articles grouped under topics,
so that I can discover what exists in an area even when I don't know the right search term.

Acceptance criteria:
- Given I open the topic index, when I select a topic, then I see all articles under it, sorted by most recently refreshed.
- Given a topic has sub-topics, when I open it, then sub-topics are visible as navigable sub-sections.

Priority: Must-have

**US-RDR-3: Judge whether an article is trustworthy**
As a Reader,
I want to see whether an article is endorsed and how recently it was refreshed,
so that I can decide whether to rely on it without reading the whole thing.

Acceptance criteria:
- Given I open an article, when the page loads, then the endorsement status, the endorsing reviewer(s), and the last-refreshed date are visible above the fold.
- Given an article is past its refresh date, when I open it, then I see a clear "this article may be out of date" banner.

Priority: Must-have

**US-RDR-4: Flag a problem with an article**
As a Reader,
I want to flag an article as wrong, outdated, or misleading,
so that the author and reviewers can fix it rather than readers being quietly misled.

Acceptance criteria:
- Given I am reading an article, when I click "flag", then I can select a reason and add an optional note, and the author plus any reviewers on the article receive a notification.
- Given I have flagged an article, when the author responds or changes the article, then I am notified.

Priority: Should-have

**US-RDR-5: Suggest an edit**
As a Reader,
I want to propose a specific edit to an article,
so that I can contribute a fix without needing write access.

Acceptance criteria:
- Given I am reading an article, when I select "suggest edit", then I can submit a proposed change with a reason.
- Given I submit a suggestion, when the author or a co-editor reviews it, then they can accept, reject with a note, or modify it before accepting.

Priority: Should-have

### Author (role prefix: AUT)

**US-AUT-1: Write a new article**
As an Author,
I want to draft and publish a new article under a topic,
so that what I know becomes searchable for everyone else.

Acceptance criteria:
- Given I start a new article, when I save, then it is stored as a draft visible only to me.
- Given I have a draft and select a topic and publish, then the article is visible to all Readers in search and topic browse.
- Given I try to publish without a topic, then publish is blocked with a clear message.

Priority: Must-have

**US-AUT-2: Revise my article**
As an Author,
I want to edit my article after publication,
so that I can fix mistakes or keep it current without creating a duplicate.

Acceptance criteria:
- Given I own an article, when I open it, then I see an "edit" action.
- Given I publish a revision, when it goes live, then the last-refreshed date updates and any prior endorsement is marked "pending re-endorsement" until a reviewer re-endorses.

Priority: Must-have

**US-AUT-3: Request endorsement**
As an Author,
I want to request endorsement from a reviewer,
so that my article is marked trustworthy for readers.

Acceptance criteria:
- Given my article is published, when I click "request endorsement", then I can pick a reviewer associated with the article's topic and send the request.
- Given the reviewer acts on the request, when they endorse or decline, then I am notified with any comments.

Priority: Must-have

**US-AUT-4: Refresh an article when it expires**
As an Author,
I want to be reminded when my article is approaching expiry and confirm it's still accurate (or update it),
so that my content doesn't quietly go stale.

Acceptance criteria:
- Given my article's refresh date is within 14 days, when that threshold is crossed, then I receive a reminder notification.
- Given I confirm the article is still accurate, when I click "confirm fresh", then the refresh date is reset without requiring a content change.
- Given I miss the expiry, when the date passes, then the article is flagged stale for readers but remains visible.

Priority: Must-have

**US-AUT-5: Triage suggestions and flags**
As an Author,
I want one place to see flags and edit suggestions on my articles,
so that I can respond without hunting through notifications.

Acceptance criteria:
- Given I have open flags or suggestions, when I open my author dashboard, then I see a list with article title, type (flag vs. suggestion), submitter, and age.
- Given I act on an item, when I resolve or respond, then the submitter is notified.

Priority: Should-have

**US-AUT-6: Grant co-editor rights**
As an Author,
I want to invite named collaborators to edit my article,
so that a team can maintain a shared article without one person being a bottleneck.

Acceptance criteria:
- Given I own an article, when I add a named co-editor, then they can edit the article and receive refresh reminders alongside me.
- Given a co-editor edits the article, when changes are saved, then the revision history attributes the change to them.

Priority: Should-have

### Reviewer (role prefix: REV)

**US-REV-1: See pending endorsement requests**
As a Reviewer,
I want a queue of articles awaiting my endorsement in my topics,
so that I can work through them efficiently.

Acceptance criteria:
- Given I have reviewer rights for a topic, when I open my reviewer dashboard, then I see all pending endorsement requests and re-endorsement-needed articles in my topics.
- Given an item has been pending for over 7 days, when I view the queue, then it is visually flagged as aging.

Priority: Must-have

**US-REV-2: Endorse or decline an article**
As a Reviewer,
I want to endorse an article (or decline with a reason),
so that readers have a clear signal of trustworthiness.

Acceptance criteria:
- Given I'm reviewing an article, when I endorse it, then the article is marked endorsed with my name and the endorsement date; readers see this.
- Given I decline, when I submit the decline with a reason, then the author is notified and the article remains unendorsed.

Priority: Must-have

**US-REV-3: Revoke an endorsement**
As a Reviewer,
I want to revoke an endorsement I previously gave,
so that I can correct the record when an article has become wrong or stale.

Acceptance criteria:
- Given I previously endorsed an article, when I revoke, then the article loses endorsed status, the author is notified, and readers see the unendorsed state.
- Given an article is edited after I endorsed it, when I open the article, then I see a clear diff of changes since my endorsement.

Priority: Must-have

**US-REV-4: Track articles I've endorsed**
As a Reviewer,
I want a list of articles I currently endorse,
so that I can see what I'm vouching for and re-check them over time.

Acceptance criteria:
- Given I have endorsed articles, when I open "my endorsements", then I see them sorted by refresh date with status (fresh / expiring soon / stale).

Priority: Should-have

### Admin (role prefix: ADM)

**US-ADM-1: Manage the topic taxonomy**
As an Admin,
I want to create, rename, merge, and retire topics,
so that the taxonomy stays coherent as the company evolves.

Acceptance criteria:
- Given I create a new topic, when I save, then Authors can assign articles to it.
- Given I merge topic A into topic B, when I confirm, then all articles under A move to B and old links to topic A redirect.
- Given I retire a topic with articles still under it, when I attempt retirement, then I am blocked until articles are reassigned or archived.

Priority: Must-have

**US-ADM-2: Appoint and remove reviewers**
As an Admin,
I want to grant or revoke reviewer rights for specific topics,
so that endorsements are issued by people who actually know the area.

Acceptance criteria:
- Given I grant someone reviewer rights for a topic, when I save, then they can endorse articles in that topic and appear in endorsement-request pickers.
- Given I revoke reviewer rights, when I save, then they can no longer endorse new articles; their existing endorsements remain visible but are tagged "former reviewer".

Priority: Must-have

**US-ADM-3: Configure refresh cadence**
As an Admin,
I want to set the default and per-topic refresh cadence,
so that fast-moving topics aren't allowed to stagnate and slow-moving topics don't generate noise.

Acceptance criteria:
- Given I set a default cadence, when new articles are created, then their refresh date is computed from that cadence.
- Given I override cadence for a topic, when existing articles in that topic recompute, then their refresh dates shift to the new cadence.

Priority: Should-have

**US-ADM-4: Monitor hub health**
As an Admin,
I want a dashboard of hub health metrics (coverage by topic, stale ratio, unendorsed ratio, unresolved flags),
so that I can spot gaps and intervene before the hub loses reader trust.

Acceptance criteria:
- Given the dashboard loads, when I view it, then I see counts and trend lines for articles per topic, percent stale, percent endorsed, and open flags.
- Given a topic has zero articles or >50% stale articles, when I view the dashboard, then the topic is highlighted.

Priority: Should-have

## 4. User journeys

**UJ-RDR-1: Reader looks up how to do something**
Role: Reader
Trigger: Reader hits a "how do we do X" question in the course of their work (e.g., "how do we request a vendor security review?").
Outcome: Reader either has a trustworthy answer or knows definitively that one doesn't yet exist.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Trigger | Needs an answer; would have asked Slack | — | Slightly annoyed; doesn't want to interrupt anyone |
| 2. Search | Types the question into hub search | Returns ranked results with endorsement + freshness signals | Skeptical — will this actually be useful? |
| 3. Evaluate | Scans top result; checks endorsement + last refresh | Displays endorsement, endorsing reviewer, refresh date above the fold | Relieved if endorsed + fresh; wary if stale |
| 4. Act / fallback | Uses the answer, or flags the article, or falls back to Slack | Captures flag; notifies author | Frustrated if content is wrong; grateful if clean |
| 5. Contribute (optional) | Submits an edit suggestion or proposes a new article | Routes suggestion to author / opens draft | Mild ownership — "I'm making this better for next time" |

Supporting stories: US-RDR-1, US-RDR-2, US-RDR-3, US-RDR-4, US-RDR-5

**UJ-AUT-1: Author captures and publishes knowledge**
Role: Author
Trigger: Author realizes they've been answering the same question multiple times in Slack, or is asked by a teammate to "write that down."
Outcome: A published, topic-tagged, endorsed article that others can find.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Decide | Opens hub, starts a new article | Creates empty draft owned by author | Motivated but dreads the friction |
| 2. Draft | Writes content, picks a topic | Autosaves; validates topic selection | Mild anxiety — "is this good enough?" |
| 3. Publish | Clicks publish | Article becomes visible; refresh date set | Small relief |
| 4. Endorse | Requests endorsement from a reviewer in that topic | Routes request; notifies reviewer | Waiting / uncertain |
| 5. Maintain | Receives refresh reminder at 14 days before expiry; confirms or edits | Resets refresh date; re-endorsement pending if edited | Minor chore; wants it to be quick |

Supporting stories: US-AUT-1, US-AUT-2, US-AUT-3, US-AUT-4, US-AUT-6

**UJ-AUT-2: Author responds to reader feedback**
Role: Author
Trigger: A Reader flags an article or suggests an edit.
Outcome: The article is corrected (or a rejection is recorded with a reason), and the submitter is informed.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Notify | Receives flag/suggestion notification | Shows item in author dashboard | Defensive first, curious second |
| 2. Triage | Opens dashboard; reviews item | Presents flag reason / diff for suggestion | Wants to resolve quickly |
| 3. Decide | Accepts edit, rejects with note, or makes their own change | Applies change; notifies submitter | Ownership |
| 4. Re-endorse | If endorsed and materially changed, article moves to pending re-endorsement | Notifies reviewer | Mildly annoyed by extra loop |

Supporting stories: US-AUT-2, US-AUT-5, US-RDR-4, US-RDR-5

**UJ-REV-1: Reviewer works through the endorsement queue**
Role: Reviewer
Trigger: Weekly reminder, or ad-hoc visit when prompted by an author.
Outcome: Queue drained; each item either endorsed, declined, or revoked.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Open queue | Opens reviewer dashboard | Shows pending + aging items for reviewer's topics | Slight dread if queue is long |
| 2. Evaluate | Reads article; compares to own expertise | Shows diff since last endorsement (for re-endorsements) | Careful — their name is on this |
| 3. Decide | Endorses, or declines with reason | Updates article status; notifies author | Sense of responsibility |
| 4. Maintain | Periodically revisits "my endorsements" | Shows endorsed articles with freshness | Wants to avoid vouching for stale content |

Supporting stories: US-REV-1, US-REV-2, US-REV-3, US-REV-4

**UJ-ADM-1: Admin maintains taxonomy and reviewer roster**
Role: Admin
Trigger: A topic split is proposed, a new domain emerges, or a reviewer leaves the team.
Outcome: Taxonomy reflects reality; reviewer permissions match who actually owns each area.

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Spot | Reviews hub health dashboard; sees stale topic or coverage gap | Highlights problem topics | Ownership of hub quality |
| 2. Plan | Decides to merge / split / retire a topic, or rotate reviewers | — | Cautious — doesn't want to break links |
| 3. Change | Executes topic change or reviewer grant/revoke | Applies migration; redirects old links; notifies affected users | Wants confidence that nothing is lost |
| 4. Verify | Re-checks dashboard | Shows updated state | Satisfied / iterative |

Supporting stories: US-ADM-1, US-ADM-2, US-ADM-3, US-ADM-4

## 5. Features

### Core workflow

**F-1: Article authoring and versioning**
Description: Create, edit, and publish articles with autosave, drafts, revision history, and co-editor support.
Supports stories: US-AUT-1, US-AUT-2, US-AUT-6
Supports journeys: UJ-AUT-1, UJ-AUT-2
Priority: Must-have
Notes: Revision history must preserve author attribution for co-edited articles.

**F-2: Topic taxonomy**
Description: Hierarchical topics that articles are assigned to; supports create, rename, merge, retire, and redirect of old URLs.
Supports stories: US-AUT-1, US-RDR-2, US-ADM-1
Supports journeys: UJ-AUT-1, UJ-RDR-1, UJ-ADM-1
Priority: Must-have
Notes: Merge/retire must never orphan articles or break inbound links.

**F-3: Search**
Description: Keyword search over article titles and bodies with ranking that incorporates endorsement and freshness signals.
Supports stories: US-RDR-1
Supports journeys: UJ-RDR-1
Priority: Must-have
Notes: Results must visibly distinguish endorsed vs. unendorsed and fresh vs. stale.

**F-4: Browse by topic**
Description: Topic index with drill-down into sub-topics and article lists sorted by freshness.
Supports stories: US-RDR-2
Supports journeys: UJ-RDR-1
Priority: Must-have

**F-5: Endorsement system**
Description: Lets Authors request endorsement; lets Reviewers endorse, decline, or revoke; displays endorsement status and endorsing reviewers to Readers.
Supports stories: US-AUT-3, US-REV-1, US-REV-2, US-REV-3, US-REV-4, US-RDR-3
Supports journeys: UJ-AUT-1, UJ-REV-1, UJ-RDR-1
Priority: Must-have
Notes: Endorsement must auto-become "pending re-endorsement" when the underlying article changes materially (threshold TBD — see Open Questions).

**F-6: Article freshness and refresh cadence**
Description: Tracks refresh dates per article, surfaces stale banners to Readers, reminds Authors before expiry, and supports "confirm fresh" without content change. Cadence is configurable per topic by Admins.
Supports stories: US-AUT-4, US-RDR-3, US-ADM-3
Supports journeys: UJ-AUT-1, UJ-RDR-1
Priority: Must-have

### Feedback loops

**F-7: Flagging**
Description: Readers can flag articles as wrong/outdated/misleading; flags route to the author and any topic reviewers; flaggers are notified on resolution.
Supports stories: US-RDR-4, US-AUT-5
Supports journeys: UJ-RDR-1, UJ-AUT-2
Priority: Should-have

**F-8: Edit suggestions**
Description: Readers can propose specific edits that the author or a co-editor can accept, reject, or modify before accepting.
Supports stories: US-RDR-5, US-AUT-5
Supports journeys: UJ-RDR-1, UJ-AUT-2
Priority: Should-have

**F-9: Author dashboard**
Description: Single view of an Author's articles with pending flags, suggestions, and upcoming expiry reminders.
Supports stories: US-AUT-4, US-AUT-5
Supports journeys: UJ-AUT-1, UJ-AUT-2
Priority: Should-have

**F-10: Reviewer dashboard**
Description: Single view of pending endorsement requests and re-endorsement-needed articles scoped to the Reviewer's topics, with aging indicators and a "my endorsements" list.
Supports stories: US-REV-1, US-REV-4
Supports journeys: UJ-REV-1
Priority: Must-have

### Administration

**F-11: Reviewer permissions**
Description: Admins can grant and revoke reviewer rights scoped to specific topics; former reviewers' past endorsements are preserved but labeled.
Supports stories: US-ADM-2, US-REV-2
Supports journeys: UJ-ADM-1
Priority: Must-have

**F-12: Hub health dashboard**
Description: Admin-facing metrics including coverage per topic, stale ratio, endorsed ratio, and open-flag count, with thresholds that highlight problem topics.
Supports stories: US-ADM-4
Supports journeys: UJ-ADM-1
Priority: Should-have

### Cross-cutting

**F-13: Notifications**
Description: In-app and email notifications for endorsement requests, endorsement outcomes, flags, suggestions, refresh reminders, and topic changes affecting an article.
Supports stories: US-AUT-3, US-AUT-4, US-AUT-5, US-REV-1, US-REV-2, US-RDR-4
Supports journeys: UJ-AUT-1, UJ-AUT-2, UJ-REV-1, UJ-RDR-1
Priority: Must-have
Notes: Users need preference controls to avoid notification fatigue — detail TBD.

**F-14: Identity and role assignment**
Description: Every person is authenticated as a company employee (Reader by default). Reviewer and Admin rights are additive. Author is implicit — anyone can write.
Supports stories: US-ADM-2, US-AUT-1, US-AUT-6
Supports journeys: UJ-ADM-1, UJ-AUT-1
Priority: Must-have
Notes: Assumes integration with existing company SSO; details out of scope for this document.

## 6. Traceability matrix

| Story | Feature(s) | Journey(s) |
|-------|------------|------------|
| US-RDR-1 | F-3 | UJ-RDR-1 |
| US-RDR-2 | F-2, F-4 | UJ-RDR-1 |
| US-RDR-3 | F-5, F-6 | UJ-RDR-1 |
| US-RDR-4 | F-7, F-13 | UJ-RDR-1, UJ-AUT-2 |
| US-RDR-5 | F-8 | UJ-RDR-1, UJ-AUT-2 |
| US-AUT-1 | F-1, F-2, F-14 | UJ-AUT-1 |
| US-AUT-2 | F-1 | UJ-AUT-1, UJ-AUT-2 |
| US-AUT-3 | F-5, F-13 | UJ-AUT-1 |
| US-AUT-4 | F-6, F-13 | UJ-AUT-1 |
| US-AUT-5 | F-7, F-8, F-9, F-13 | UJ-AUT-2 |
| US-AUT-6 | F-1, F-14 | UJ-AUT-1 |
| US-REV-1 | F-5, F-10 | UJ-REV-1 |
| US-REV-2 | F-5, F-11, F-13 | UJ-REV-1 |
| US-REV-3 | F-5 | UJ-REV-1 |
| US-REV-4 | F-5, F-10 | UJ-REV-1 |
| US-ADM-1 | F-2 | UJ-ADM-1 |
| US-ADM-2 | F-11, F-14 | UJ-ADM-1 |
| US-ADM-3 | F-6 | UJ-ADM-1 |
| US-ADM-4 | F-12 | UJ-ADM-1 |

Every story maps to at least one feature and one journey; every feature supports at least one story.

## 7. Open questions

1. **Article ownership model.** The input spec flagged this as undecided. This document assumes **single-owner with explicit co-editors and reader-submitted edit suggestions**. The alternative — wiki-style, anyone-can-edit — would significantly simplify F-8 (edit suggestions become direct edits) but would require a different endorsement model (what exactly is a reviewer vouching for if anyone can change it after?). Needs product decision before F-1, F-5, and F-8 can be finalized.
2. **Reviewer selection criteria.** The spec flagged "trusted reviewer criteria are TBD." This document assumes **Admin-appointed**. Alternatives considered: (a) automatic promotion after N authored-and-endorsed articles in a topic, (b) peer nomination with Admin approval. Recommend deciding before F-11 is built, because the UI for reviewer-management differs.
3. **Refresh cadence.** Spec says "probably quarterly but unconfirmed." This document assumes **90-day default, Admin-configurable per topic**. Needs confirmation and a decision on whether cadence can also be set per article (e.g., for evergreen policy docs that should refresh annually).
4. **What counts as a "material" edit for endorsement invalidation?** F-5 says endorsement flips to "pending re-endorsement" on material changes. Character-level diff? Any save? Author-declared? Needs decision.
5. **Are drafts fully private, or visible to the author's manager / co-editors before publication?** US-AUT-1 currently assumes fully private. Confirm.
6. **Notification preferences.** F-13 assumes users can tune notification frequency, but the spec is silent. Minimum viable preference set needs to be scoped.
7. **Archival vs. deletion.** Neither the spec nor this document defines what happens to articles whose topics are retired, whose authors leave the company, or that a Reviewer wants permanently removed. Likely needs an "archive" state distinct from "stale."
8. **Analytics for Authors.** Should Authors see view counts or search hits on their articles? Useful for motivation but not in the input spec. Flag for potential follow-up.
9. **Access control.** The spec assumes "everyone at the company" is a Reader; it does not address whether some articles should be visible only to certain groups (e.g., HR-sensitive material). Currently out of scope, but worth confirming before launch.
10. **Mobile/offline.** Not mentioned in spec. Assumed desktop-web-only for now.
