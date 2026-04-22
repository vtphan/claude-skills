# Bookclub Companion — Requirements

## 1. Context

Bookclub Companion is a lightweight mobile-first app for small, in-person book clubs (up to ~20 members, invite-only). It helps a club pick the next book, schedule the next meeting, capture shared notes during the meeting, and archive discussion notes and ratings afterward. The product deliberately avoids the social-network shape of existing "readers'" apps — there is no public discovery, no social feed, no retailer integration, no audio/video conferencing, and no in-book reading tracking.

The system is used by three roles. A **club organizer** sets up the club, invites members, and holds tie-breaking authority on votes and scheduling. A **club member** nominates books, votes, RSVPs, and contributes notes during and after the meeting. A **guest** is a one-time visitor invited to a single meeting who can view the current book and meeting details but cannot vote; guests use magic-link access and do not need an account.

Success means members keep showing up: the target is 70% of invited members attending at least one meeting in their first two months, and clubs averaging at least four consecutive monthly meetings. The UX must therefore reduce friction around the recurring monthly cycle (pick → schedule → meet → archive) rather than optimize for time-in-app.

## 2. User roles

| Role | Prefix | What they're trying to accomplish |
|------|--------|-----------------------------------|
| Club organizer | ORG | Stand up and run a small club: invite the right people, keep the monthly cycle moving, resolve deadlocks. |
| Club member | MEM | Participate meaningfully in choosing books, showing up to meetings, and remembering what was said. |
| Guest | GST | Attend a single meeting they've been invited to without signing up for an account. |

## 3. User stories

### Club organizer (ORG)

**US-ORG-1: Create a private club**
As a club organizer,
I want to create a new private club with a name and short description,
so that I have a dedicated space for my group to coordinate.

Acceptance criteria:
- Given I am signed in with no clubs, when I create a club with a name, then the club is created with me as organizer and no other members.
- Given I create a club, when creation completes, then I am taken to the club's home view with empty states for "current book" and "next meeting".

Priority: Must-have

**US-ORG-2: Invite members to the club**
As a club organizer,
I want to invite people by email (or shareable link) up to the ~20-member cap,
so that the right group can participate without the club being publicly discoverable.

Acceptance criteria:
- Given I enter an email address, when I send an invite, then the invitee receives a link to join and appears as "invited" in my member list.
- Given the club has 20 active members, when I try to send another invite, then I see a clear message that the cap is reached.

Priority: Must-have

**US-ORG-3: Break a tie on book selection or scheduling**
As a club organizer,
I want to cast a tie-breaking decision when a vote or scheduling poll is tied,
so that the club can move forward without stalling.

Acceptance criteria:
- Given a book vote closes with a tie, when I open the results, then I am prompted to pick one of the tied options as the winner.
- Given a scheduling poll closes with a tie, when I open the results, then I can select the final date/time from the tied options.
- Given I have not yet broken the tie, when any member opens the club, then they see a "waiting on organizer" indicator.

Priority: Must-have

**US-ORG-4: Invite a guest to a single meeting**
As a club organizer,
I want to invite a guest to one specific meeting via magic link,
so that friends or prospective members can attend without creating an account.

Acceptance criteria:
- Given an upcoming meeting, when I add a guest's email, then the guest receives a magic link that grants view-only access to that meeting's current book and details.
- Given a guest's magic link, when the meeting has ended, then the link no longer grants access.

Priority: Should-have

**US-ORG-5: Remove or replace an inactive member**
As a club organizer,
I want to remove a member who is no longer participating,
so that membership reflects who is actually in the club and the member cap isn't wasted.

Acceptance criteria:
- Given a member I select, when I remove them, then they lose access to the club but their past contributions (votes, notes) are preserved with their name.
- Given a removed member, when they try to open the club, then they see a clear "no longer a member" message.

Priority: Should-have

### Club member (MEM)

**US-MEM-1: Nominate a book for the next read**
As a club member,
I want to nominate a book (title, author, optional note on why),
so that it appears on the ballot for the next selection vote.

Acceptance criteria:
- Given nominations are open, when I submit a nomination, then it appears in the nomination list visible to all members.
- Given nominations are closed, when I try to nominate, then I see that nominations are closed and when the next window opens.

Priority: Must-have

**US-MEM-2: Vote on the next book**
As a club member,
I want to vote on the list of nominated books,
so that my preference counts toward the selection.

Acceptance criteria:
- Given a vote is open, when I submit my vote, then my choice is recorded and I can change it until the vote closes.
- Given the vote closes, when I open the club, then I see the winning book prominently.

Priority: Must-have

**US-MEM-3: RSVP to the next meeting**
As a club member,
I want to RSVP yes / no / maybe to the next meeting,
so that the organizer and other members know who is coming.

Acceptance criteria:
- Given a scheduled meeting, when I set my RSVP, then my status is visible to other members and updates live.
- Given I change my RSVP, when I save, then the new status replaces the old.

Priority: Must-have

**US-MEM-4: Contribute notes during the meeting**
As a club member,
I want to add to a shared scratchpad during the meeting,
so that the group captures interesting points as they come up.

Acceptance criteria:
- Given a meeting is in progress, when I add a note, then it appears in the shared scratchpad for other attendees within a few seconds.
- Given I add a note, when the scratchpad is saved, then my name (or initials) is attached to my contribution.

Priority: Must-have

**US-MEM-5: Rate and reflect on the book after the meeting**
As a club member,
I want to leave a rating and a short reflection after the meeting,
so that the book's archive entry captures how the group felt about it.

Acceptance criteria:
- Given a meeting has ended, when I submit a rating (e.g., 1–5) and optional reflection, then both are saved to that book's archive entry.
- Given I've already rated, when I open the archive entry, then I can update my rating and reflection.

Priority: Should-have

**US-MEM-6: Browse the club's past books and notes**
As a club member,
I want to browse previous books with their notes and ratings,
so that I can recall what we read and what we said.

Acceptance criteria:
- Given the club has past meetings, when I open the archive, then I see a chronological list of past books with aggregated ratings.
- Given a past book, when I open it, then I see the meeting date, the shared notes from that meeting, and member reflections.

Priority: Must-have

### Guest (GST)

**US-GST-1: Access a single meeting via magic link**
As a guest,
I want to open the meeting I was invited to using a magic link,
so that I can see the book and meeting details without creating an account.

Acceptance criteria:
- Given a valid magic link for an upcoming meeting, when I open it, then I see the current book, the meeting date/time, and the location.
- Given the meeting has ended, when I open the link, then I see a message that access has expired.

Priority: Must-have

**US-GST-2: See what's being read without voting**
As a guest,
I want to view the current book's title, author, and description,
so that I can prepare for the discussion I'm attending.

Acceptance criteria:
- Given I am on the meeting page as a guest, when I view the current book, then I see its title, author, and any description the club entered.
- Given I am a guest, when I try to nominate or vote, then those controls are not visible to me.

Priority: Must-have

## 4. User journeys

**UJ-ORG-1: Standing up a new club**
Role: Club organizer
Trigger: Has a group of friends who want to read together, decides to use the app
Outcome: Club is created, members have joined, and the first monthly cycle is in motion

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Create | Signs up, creates a club, names it | Creates the club, sets them as organizer, shows empty-state home | Slight anxiety about whether friends will actually show up |
| 2. Invite | Adds 8 email addresses, shares a link in group chat | Sends invites, lists them as "invited" | Worries about nagging people, wonders if emails land in spam |
| 3. Seed | Opens nominations for the first book, adds one nomination themselves | Opens the nomination window, shows the nominations list | Wants to model participation without dominating |
| 4. Schedule | Starts a poll for the first meeting date | Creates poll visible to members as they join | Mild overwhelm — too many features at once? |
| 5. Close loop | After vote and schedule close, confirms winners, breaks any tie | Locks in book and meeting, sends confirmations | Relief — the club feels real now |

Supporting stories: US-ORG-1, US-ORG-2, US-ORG-3, US-MEM-1, US-MEM-2, US-MEM-3

**UJ-ORG-2: Running the monthly cycle**
Role: Club organizer
Trigger: Current meeting just ended, or a set point in the month (e.g., 3 weeks before next meeting)
Outcome: Next book chosen, next meeting scheduled, members RSVP'd

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Open cycle | Opens nominations and scheduling poll | Notifies members both are open | Worries nobody will nominate |
| 2. Monitor | Checks participation, nudges quiet members | Shows who has / hasn't nominated or voted | Doesn't want to feel like a project manager |
| 3. Close | Closes nominations, then vote, then schedule | Closes windows, tallies, flags ties | Tense if there's a tie |
| 4. Resolve | Breaks any tie, confirms final book + date | Locks in selections, notifies club | Satisfaction — decision made |
| 5. Hand off | Shares meeting details, optionally invites a guest | Generates guest magic links | Hopeful — meeting is set |

Supporting stories: US-ORG-3, US-ORG-4, US-MEM-1, US-MEM-2, US-MEM-3

**UJ-MEM-1: Participating in a monthly cycle**
Role: Club member
Trigger: Notification that a new cycle is open, or organizer nudge
Outcome: Has read (or tried to read) the chosen book, attended the meeting, and left reflections

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Nominate | Adds a book they've been meaning to read | Adds it to the ballot | Low-stakes fun |
| 2. Vote | Scans other nominations, votes | Records vote, shows live tallies (if allowed) | Curious about what others picked |
| 3. Schedule | Picks dates that work, RSVPs yes | Records RSVP, updates the members list | Mild calendar Tetris |
| 4. Meet | Attends meeting, adds notes on the scratchpad | Syncs notes across attendees | Worried about typing on phone during a real conversation |
| 5. Reflect | After meeting, rates and writes a short reflection | Saves to book archive | Satisfaction at closing the loop |
| 6. Revisit | Months later, browses archive | Shows past books with notes | Nostalgia, "I forgot we read that" |

Supporting stories: US-MEM-1, US-MEM-2, US-MEM-3, US-MEM-4, US-MEM-5, US-MEM-6

**UJ-GST-1: Attending one meeting as a guest**
Role: Guest
Trigger: Friend (an organizer or member) invites them to a specific meeting
Outcome: Shows up informed, without having signed up for anything

| Phase | User action | System response | Pain points / emotions |
|-------|-------------|-----------------|------------------------|
| 1. Receive | Gets email with magic link | Link lands in inbox | Mild suspicion — is this legit? |
| 2. Open | Taps the link on their phone | Opens meeting view: book, date, location | Relief — no signup wall |
| 3. Prepare | Reads book description, notes the venue | Shows current book and venue | Wants to not look unprepared |
| 4. Attend | Goes to the meeting | Link still valid day-of | Focus on meeting, not app |
| 5. Expire | Opens the link a week later out of curiosity | Shows "access expired" | Expected — not frustrating if messaged well |

Supporting stories: US-GST-1, US-GST-2, US-ORG-4

## 5. Features

### Core workflow

**F-1: Private club setup and membership**
Description: Create a private club, invite members by email or shareable link up to a ~20-member cap, remove members, and keep membership history.
Supports stories: US-ORG-1, US-ORG-2, US-ORG-5
Supports journeys: UJ-ORG-1
Priority: Must-have
Notes: Must enforce the member cap. Decide whether shareable links should expire or be revocable (open question).

**F-2: Book nominations**
Description: A per-cycle window where members can nominate books (title, author, optional note); nominations appear in a list visible to all members.
Supports stories: US-MEM-1
Supports journeys: UJ-ORG-1, UJ-ORG-2, UJ-MEM-1
Priority: Must-have
Notes: Requires a concept of a "cycle" with open/closed states for nominations.

**F-3: Book selection vote**
Description: Ranked or single-choice vote on the nominated ballot, with changeable votes until the vote closes, and a declared winner at close.
Supports stories: US-MEM-2, US-ORG-3
Supports journeys: UJ-ORG-2, UJ-MEM-1
Priority: Must-have
Notes: Voting method (approval, single-choice, ranked) is not specified — open question.

**F-4: Meeting scheduling and RSVPs**
Description: Create a meeting with date/time and location/venue (optionally via a poll over candidate dates), members RSVP yes/no/maybe, organizer breaks ties on date polls.
Supports stories: US-MEM-3, US-ORG-3
Supports journeys: UJ-ORG-1, UJ-ORG-2, UJ-MEM-1
Priority: Must-have
Notes: Location is free-text unless a maps integration is desired (open question).

**F-5: Tie-breaking by organizer**
Description: When a vote or scheduling poll closes in a tie, the organizer is prompted to pick a winner; members see a "waiting on organizer" state until resolved.
Supports stories: US-ORG-3
Supports journeys: UJ-ORG-2
Priority: Must-have
Notes: Applies to both book votes (F-3) and scheduling polls (F-4).

**F-6: Shared in-meeting scratchpad**
Description: A live, collaboratively editable notes area for the current meeting, with attribution of contributions, usable on phones.
Supports stories: US-MEM-4
Supports journeys: UJ-MEM-1
Priority: Must-have
Notes: Real-time sync requirement; offline behavior not specified (open question). Mobile ergonomics are critical.

**F-7: Post-meeting ratings and reflections**
Description: After a meeting ends, members can submit a rating and short reflection tied to that book's archive entry, editable later.
Supports stories: US-MEM-5
Supports journeys: UJ-MEM-1
Priority: Should-have
Notes: Rating scale not specified — assume 1–5 unless clarified (open question).

**F-8: Club book archive**
Description: A chronological archive of past books for the club, showing meeting date, shared scratchpad contents, member reflections, and aggregated rating.
Supports stories: US-MEM-6
Supports journeys: UJ-MEM-1
Priority: Must-have
Notes: Depends on F-6 (scratchpad) and F-7 (ratings).

### Guest access

**F-9: Guest magic-link access**
Description: Organizer invites a guest to one specific meeting; guest receives a magic link granting view-only access to the current book and meeting details, with access expiring after the meeting.
Supports stories: US-ORG-4, US-GST-1, US-GST-2
Supports journeys: UJ-ORG-2, UJ-GST-1
Priority: Should-have
Notes: "Expires after the meeting" needs a concrete rule (end of meeting day? 24h after?) — open question.

### Platform

**F-10: Mobile-first client**
Description: The entire experience is designed for phones first, with touch-friendly interactions and reasonable performance on mobile networks.
Supports stories: (all — cross-cutting)
Supports journeys: UJ-MEM-1 (especially phase 4, in-meeting typing), UJ-GST-1
Priority: Must-have
Notes: Cross-cutting constraint from the input spec.

**F-11: Notifications and nudges**
Description: Notify members of cycle events (nominations open, vote open, schedule open, meeting reminders) and let organizers nudge quiet participants.
Supports stories: US-MEM-1, US-MEM-2, US-MEM-3, US-ORG-2
Supports journeys: UJ-ORG-2, UJ-MEM-1
Priority: Should-have
Notes: Channel (push, email, both) not specified — open question. Strongly tied to the 70%-attendance and 4-consecutive-meeting success metrics.

## 6. Traceability matrix

| Story | Features | Journeys |
|-------|----------|----------|
| US-ORG-1 | F-1 | UJ-ORG-1 |
| US-ORG-2 | F-1, F-11 | UJ-ORG-1 |
| US-ORG-3 | F-3, F-4, F-5 | UJ-ORG-1, UJ-ORG-2 |
| US-ORG-4 | F-9 | UJ-ORG-2, UJ-GST-1 |
| US-ORG-5 | F-1 | — (membership maintenance, not part of a primary journey) |
| US-MEM-1 | F-2, F-11 | UJ-ORG-1, UJ-ORG-2, UJ-MEM-1 |
| US-MEM-2 | F-3, F-11 | UJ-ORG-2, UJ-MEM-1 |
| US-MEM-3 | F-4, F-11 | UJ-ORG-1, UJ-ORG-2, UJ-MEM-1 |
| US-MEM-4 | F-6 | UJ-MEM-1 |
| US-MEM-5 | F-7, F-8 | UJ-MEM-1 |
| US-MEM-6 | F-8 | UJ-MEM-1 |
| US-GST-1 | F-9, F-10 | UJ-GST-1 |
| US-GST-2 | F-9, F-10 | UJ-GST-1 |

Coverage check: every story maps to at least one feature; every journey is supported by at least three stories. US-ORG-5 (remove member) does not appear in a primary journey — this is expected, as membership maintenance is an occasional administrative action rather than part of the monthly cycle.

## 7. Open questions

1. **Voting method for book selection.** The spec says members "vote on the next book" but not whether it's single-choice, approval, or ranked. This materially changes F-3 and how ties are defined for F-5.
2. **Rating scale.** The spec mentions "ratings" in the per-book archive but doesn't specify the scale (thumbs up/down? 1–5? 1–10?). Assumed 1–5 for now.
3. **Scheduling mechanism.** Is the meeting scheduled by the organizer outright, or via a poll of candidate dates that members vote on? The organizer's "tie-breaking authority on scheduling" implies a poll, but this should be confirmed.
4. **Guest magic-link expiry rule.** "Access expires after the meeting" — does that mean at the meeting's scheduled end time, end of meeting day, or 24 hours after? Also: should guests see the shared scratchpad during the meeting, or only the book and logistics?
5. **Shareable invite links.** Should invite links (as distinct from per-email invites) exist at all, and if so should they be single-use, time-limited, or revocable by the organizer?
6. **Offline behavior for the in-meeting scratchpad.** In-person meetings can happen in places with poor connectivity (restaurants, basements). Should the scratchpad work offline and sync later, or require connectivity?
7. **Notification channels.** Push only, email only, or both? Matters for F-11 and for hitting the attendance success metric.
8. **Nomination cap per member.** Is there a limit on how many books one member can nominate in a cycle? Affects ballot size and F-2.
9. **Archive visibility for removed members and guests.** Once a member is removed (US-ORG-5), do their past notes and ratings remain attributed to them by name? Can past guests still see the specific meeting they attended?
10. **Multi-club membership.** Can one person be a member of multiple clubs, and if so does the organizer role scope per club (assumed yes, but not stated)?
