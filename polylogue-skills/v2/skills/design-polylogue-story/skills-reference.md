# Skills reference

Per-skill working reference for the polylogue Instructional Designer. For each skill: a definition, where it can sit in a chapter end, what mastery looks like at grades 5/6/7, the named ways students go wrong with it (each with an example wrong-choice in MC voice), and a worked micro-example.

**At cold start, these worked examples are doing the work a sample story would otherwise do.** They are the only concrete pedagogical ground-truth available to the LLM. Read the entry for any skill before authoring a challenge that targets it.

**Skills here are available, not required.** Author challenges only where the chapter's staged scene supports them naturally. A chapter that doesn't stage a vocabulary-in-context moment shouldn't have a comprehension check forced onto it; a chapter without a real decision shouldn't have a manufactured gate. Per DECISIONS.md Section 4, chapter ends carry 0, 1, or 2 challenges — the story's dramatic shape decides.

The four entries below are the v1 starter set, chosen to validate the template across all three skill categories and all three challenge slots:

- `vocabulary in context` — Foundational, `[comprehension_check]`, individual default
- `inferencing` — Thinking, `[gate]`, group default
- `considering multiple viewpoints` — Thinking, `[fork]`, group always
- `recognizing when a peer is dismissed` — SEL-as-content, `[gate]`, group always

Additional skills in the taxonomy (sequencing, predicting, distinguishing fact from opinion, recognizing assumptions, etc.) are not yet in this reference; add them as the dialog with authors surfaces specific needs.

---

## Vocabulary in context

**Category:** Foundational Reading
**Slot:** `[comprehension_check]`
**Default challenge type:** individual

**Definition.** Figuring out what a word means by using the surrounding text — other words in the sentence, the situation in the story, what's happened so far — instead of needing a dictionary or a teacher.

**Mastery signs.**

- *Grade 5:* For a moderately unfamiliar word, points to a specific clue in the same sentence or paragraph. ("It says 'devour' and Maya hadn't eaten in hours, so devour means eat fast.") Concrete, one-step.
- *Grade 6:* Combines a clue from the sentence with knowledge from earlier in the chapter. ("'Withdrawn' — earlier she was bouncing around, now she's quiet at her desk; withdrawn must mean pulled-back, quiet.") Beginning to handle abstract words anchored by concrete context.
- *Grade 7:* Distinguishes between two reasonable meanings using subtler cues — tone, irony, figurative use. ("She said it 'sarcastically' so 'great' here is the opposite of the usual meaning.")

**Common failure modes.**

*Surface-of-the-word.* Treats a less-familiar word as similar to a more-familiar word it sounds or looks like, ignoring the surrounding text.
Example wrong-choice (scene: "Jordan withdrew from the project"): *"Jordan took money out for the project."*

*Ignoring context.* Picks a dictionary-correct meaning that doesn't fit the scene.
Example wrong-choice: *"Jordan pulled out a notebook."*

*Substituting plot for word meaning.* Names what's happening in the story instead of what the word means.
Example wrong-choice: *"Jordan is angry at Maya."*

**Worked micro-example.**

Scene: After the argument, Jordan stopped showing up to the lab table. By Friday, Jordan had moved to a different group entirely. Maya wrote in her notebook: *"Jordan withdrew from the project."*

What does "withdrew" mean in this scene?

- *Mastery (G6):* "Jordan stopped working on the project — pulled out of it." (Notices: stopped showing up, moved groups; connects to "withdraw" = pull-back, leave.)
- *Surface-of-the-word failure:* "Jordan took money out for the project."
- *Ignoring-context failure:* "Jordan pulled out a notebook."
- *Substituting-plot failure:* "Jordan is angry at Maya."

**Authoring notes.**

Vocabulary-in-context is the prototypical comprehension check — individual (each student is checking their own understanding), formative (a wrong answer doesn't risk the story), unambiguous (the word means what it means in this scene). Stage the word in a sentence with at least one clear contextual clue, and let the surrounding chapter add a second. Wrong choices ride real student moves: confusing similar-sounding words, picking the most common dictionary meaning when the scene doesn't support it, and substituting "what's happening" for "what the word means." Avoid words defined only by external knowledge with no in-scene support — that's vocabulary recall, not vocabulary-in-context.

**Word selection matters.** This skill works best on words with morphological structure (prefixes, suffixes, recognizable roots) or with literal/figurative tension (a word that has both a concrete and a figurative meaning, where the scene calls for the figurative). Pure jargon and acronyms don't admit the failure modes well — the student has nothing adjacent to misread from. If the chapter's staged scene doesn't naturally include a word of this shape, the comprehension check should be omitted on this chapter, not forced.

---

## Inferencing

**Category:** Thinking
**Slot:** `[gate]`
**Default challenge type:** group

**Definition.** Drawing a conclusion the text implies but doesn't state outright, using textual evidence plus prior knowledge.

**Mastery signs.**

- *Grade 5:* Names a specific text detail and a one-step conclusion. ("She said she 'didn't care anyway' — she's hurt.") Inferences are usually about feelings, motivations, simple cause-and-effect.
- *Grade 6:* Combines two or more details across paragraphs. ("She said she didn't care, but she'd been practicing for an hour — she's hurt and trying to hide it.") Begins handling dramatic irony.
- *Grade 7:* Holds competing inferences and weighs which is best supported. Recognizes when the text is deliberately ambiguous.

**Common failure modes.**

*Surface-reading-only.* Answers what's literally on the page, treating the text as a transcript.
Example wrong-choice (scene: Maya leaves a full lunch tray after an argument): *"Maya isn't hungry today."*

*Over-inferring.* Leaps to a dramatic conclusion the text doesn't support, usually by importing an exciting genre script.
Example wrong-choice: *"Maya is hiding a serious illness from her family."*

*Wrong-direction inference.* Inferring, but fixating on one weak detail and missing a stronger one.
Example wrong-choice (earlier in the chapter, Maya was excited about her mom's packed lunch): *"Maya doesn't like the sandwich her mom made."*

**Worked micro-example.**

Scene: After the lab-partner argument, Maya sits alone in the cafeteria. Her tray is full. She unzips her bag, sees the sandwich her mom packed — her favorite — and zips it back up.

What's going on with Maya?

- *Mastery (G6):* "Maya is too upset to eat — even her favorite sandwich isn't tempting her." (Notices the full tray, the favorite food, the bag zipped back up; connects to the earlier argument.)
- *Surface-reading failure:* "Maya isn't hungry."
- *Over-inferring failure:* "Maya is going to confront her partner after lunch."
- *Wrong-direction failure:* "Maya doesn't like the sandwich her mom made."

*Hint after attempt 1 (group, discussion-prompting):* "What did the chapter show us before lunch? Talk it through — what could explain why even her favorite sandwich isn't tempting her?"

**Authoring notes.**

Stage at least two pieces of evidence the correct inference accounts for and the wrong choices don't. Surface-reading wrongs miss the second piece; over-inferring wrongs aren't supported by *any* of them. Avoid scenes where the inference is the only possible reading — that turns the gate into recall.

Under the group challenge bar (Section 8 of DECISIONS.md), wrong choices need to be tempting enough that a discussion of three students wouldn't trivially eliminate them. Discussion narrows the field, so plausible-but-wrong is the standard.

---

## Considering multiple viewpoints

**Category:** Thinking (perspective-taking subcategory)
**Slot:** `[fork]`
**Default challenge type:** group always

**Definition.** Holding two or more reasonable views of a situation in mind at once, recognizing each as supported by real reasons even when they conflict — without immediately deciding one is right.

**Mastery signs.**

- *Grade 5:* Names a second character's view in their own words. ("Maya thinks her partner abandoned her, but Jordan thinks Maya talked over them.") Two views, simply stated.
- *Grade 6:* Identifies a specific reason behind each view, not just the position. ("Maya feels betrayed because they'd promised to share the work; Jordan feels dismissed because Maya kept overriding their suggestions.") Reasons, not just stances.
- *Grade 7:* Recognizes that two views can both be partly right, or that holding both creates a more complete picture than either alone. Begins to see how identity, history, or stake shapes which view a person holds.

**Common failure modes.**

*Picking a winner.* Names one view as "correct" and the other as a misunderstanding.
Example wrong-choice: *"Jordan was just being defensive — Maya was right that they didn't do their share."*

*Flattening to "everyone has an opinion."* Treats both views as equally valid because they're held, without engaging with the reasons.
Example wrong-choice: *"They both have feelings about it."*

*Fake compromise.* Smooths the conflict by inventing a position neither side actually holds.
Example wrong-choice: *"They both wanted to do a good job and just got frustrated."*

**Worked micro-example (fork scenario).**

Maya and Jordan have argued. The protagonist, Tasha, has heard both sides separately and is now asked: which perspective should the lab group lead with at tomorrow's class meeting?

Two correct fork branches (each routes to a different post-fork chapter):

- *Lead with Maya's perspective: the project requires reliable participation, and absences hurt the group.* Values structure and accountability.
- *Lead with Jordan's perspective: collaboration requires real listening, and if voices get overridden the group has already broken.* Values voice and inclusion.

One incorrect choice (with misconception):

- *"Tell the teacher to assign new partners — neither is wrong, but they can't work together."* (Picking a winner via avoidance — sidesteps the actual perspective conflict.)

Mastery (G7) reasoning: "Both views have a real reason. Maya's is about structure; Jordan's is about voice. Either could lead, and which one leads first changes how the conversation goes."

*Hint after attempt 1 (group, discussion-prompting):* "What's at stake for each of them? Try saying out loud, in your group, the strongest reason for each side before you decide which to lead with."

**Authoring notes.**

The perspective fork is the one place where multiple choices are correct — the legitimacy bar is high. Each correct branch must represent a view a thoughtful person *who held that view* would defend; if one branch is clearly more virtuous, the fork is hollow and should be redesigned. The incorrect choice (when present) typically fails by *avoiding* the perspective conflict (picking-a-winner-via-shortcut, opting out, deferring to authority) rather than by holding a different perspective.

Stage the chapter so both correct views have real evidence in the story and real cost. This is the moment the CYOA structure (Section 3 of DECISIONS.md) does its load-bearing perspective-taking work.

---

## Recognizing when a peer is dismissed

**Category:** Social-Emotional (SEL-as-content)
**Slot:** `[gate]`
**Default challenge type:** group always

**Definition.** Noticing the social pattern in which one person's contribution to a conversation is treated as if it didn't happen — through interruption, talking-over, ignoring, or repeating someone else's earlier point as if it were new.

**Mastery signs.**

- *Grade 5:* Identifies the *what*: "Jordan was talking and Priya cut them off." Names the visible behavior.
- *Grade 6:* Identifies the *pattern*: "It happens to Jordan a lot in this group — they start, someone talks over, they stop trying." Notices repetition across a scene.
- *Grade 7:* Identifies the *consequence*: "After Priya kept doing this, Jordan stopped offering ideas at all — even ones the group needed." Connects the pattern to its social cost.

**Common failure modes.**

*Charitable misread.* Names a benign explanation that ignores the visible cue.
Example wrong-choice (scene below): *"Priya didn't hear Jordan."*

*Personal-attribution.* Locates the cause inside the dismissed person rather than in the social pattern.
Example wrong-choice: *"Jordan is just shy."*

*Mirror-symmetry misread.* Treats a one-sided pattern as if both people were doing it equally.
Example wrong-choice: *"They were both talking over each other."*

**Worked micro-example.**

Scene: At the lab table, Jordan looks up. *"What if we used the data from week two—"* Priya, mid-sentence about something else, raises her voice slightly, looks at Oz, and continues her own point. Jordan's mouth closes. Jordan looks down at the notebook. Two minutes later Oz suggests something close to what Jordan was about to say. Priya: *"Yes! That's exactly what we should do."*

What just happened in the lab group?

- *Mastery (G6):* "Priya talked over Jordan, then accepted the same idea when Oz said it. Jordan got dismissed."
- *Charitable-misread failure:* "Priya didn't hear Jordan."
- *Personal-attribution failure:* "Jordan is just shy."
- *Mirror-symmetry failure:* "They were both talking over each other."

*Hint after attempt 1 (group, discussion-prompting):* "What did Priya do when Jordan started talking? And what happened a few minutes later when Oz said almost the same thing? Talk through the difference with your group."

**Authoring notes.**

This skill works at a gate when the chapter scene stages the social pattern *visibly* — through repeated cues, contrast (the same idea accepted from a different speaker), or a clear behavioral consequence (the dismissed person going quiet). Avoid scenes where the dismissal is implied but not shown — that becomes inference, not social-awareness.

Under the group challenge bar, wrong choices should be moves real students at this age make. Charitable misreads are the most important to author well — middle schoolers default to "they didn't mean to" framings, and a wrong choice that just says "she didn't notice" is exactly the move the skill is meant to defeat.

The correct answer should require *naming the pattern*, not just describing what happened — which is why the mastery signs distinguish G5 (the what), G6 (the pattern), and G7 (the consequence). A G5-level chapter should accept "Priya cut off Jordan" as correct; a G7-level chapter should require the mastery answer to name the consequence.
