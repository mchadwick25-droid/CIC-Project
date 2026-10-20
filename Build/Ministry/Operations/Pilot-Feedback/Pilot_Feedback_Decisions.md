# Pilot Feedback Decisions

Append-only. One entry per decision Mark converged on. Nothing here is built until Mark asks.

## Theme D: the front door and layers — 2026-10-19

Status: converged (Mark). Nothing built.

Covers feedback items 5, 12, 13, 19, 21, 22, 23, 24, 26 and the Q5 change in PR 976.

Decisions
- Visitor: the curious Christian, someone who knows names like Augustine and Luther, has a little time, and wants to learn more.
- First invitation: hear a short story. A one-minute story in text and audio, then "go deeper" or "talk to someone who was there". Fixed text, so there is no per-visit model cost.
- Story choice: three or four short teasers to pick from. One tap, then the story.
- Layers: by time (1, 3, 5, then 10 to 15 minutes), built from themed modules and stories. Sources sit inside each layer, using the three transparency levels already in the app.
- Free tokens: one short line on the landing page near the doors. In the conversation, a small count in the header, off the stack under the question box.
- Header: logo, the three doors (Church Family Tree, Conversation with One, Build a Table), and Menu. "Tell us what you think" moves into the Menu.
- Page shape: a clean landing page with a short headline, the story teasers, then the three doors as one line each. Sources one click away at every layer.

What must hold
- Honest limits and no invention. The disclaimer stays.
- Reading level at the BBC News or National Geographic target.
- Sources one click away at every layer.
- No overlays, no stacked small controls.
- Audio of fixed text only, in the fixed ElevenLabs voice; any generation follows the paid bulk-run rule (sample first, approved by ear).

Evidence used
- Mark's synthesis of user discussions (items 12 to 26) and the single pilot tester's notes.
- Research round 1 (web search, 2026-10-19): progressive disclosure practice, Google Arts and Culture's 2025 daily-feed homepage, Duolingo's value-before-signup. The sources were mostly vendor blogs and commentary. No measured results were found, and nothing on Khan Academy or museum sites.

Open and not decided here
- Which stories lead, and the order of the teasers.
- Whether to add one or two opening questions ("What do you already know?") to choose the teasers. Mark did not add it.
- How the Church Family Tree collects up to three picks (theme E).
- Which layer gets audio first (theme F).
- Q5 in PR 976 places the Build a Table card first on the current page; this decision may move it.

### Correction to Theme D evidence — 2026-10-19
- Research round 1 was a quick scan of four web searches, read for what supported the draft. It did not test the draft, look for counter-examples, open the products, or record what was not found beyond a short gap note. It is not research evidence and does not support the Theme D decision. The Theme D decision stands only as Mark's judgment until proper research is done.
- Proper research, to be agreed with Mark: questions written first, systems chosen by stated criteria, each one actually opened and recorded in a comparison grid, evidence against the draft sought as hard as evidence for it, and a list of what could not be found.

### Amendment to Theme D, pending the research — 2026-10-19
Source: Mark's own look at two of the ten sites. These are his preferences, not research findings.
- Google Arts and Culture: he likes the simplicity and the scrolling.
- BibleProject: he likes the simple selection.
- His idea: not everything has to be on the first page. Show a rotating few, something new each time, very clean.
- Effect on the draft: the story teasers become a rotating few drawn from a larger set, not a fixed three or four. How the rotation works is open. The research grid still has to be filled and the six claims tested.
- Rotation (Mark): a new random few each visit, skipping stories that visitor has already seen. The browser remembers what was seen; no account. Needs a larger set of one-minute stories than the three or four first drafted.

## Theme D, the chooser — 2026-10-19

Status: converged (Mark: "Converged, write the build plan"). Nothing built.

Covers how a visitor chooses a conversation on the landing page and the Build a Table page. Full record: `Build/Ministry/Features/Conversation-Chooser/` (decision log, research plan, comparison grid, prototype, build plan).

Decisions
- A hand of five cards, dealt from a deck the visitor can narrow by era or by a place or a name they know. The count is always written. The Church Family Tree is one step away as the full map.
- It replaces the chair strips and the multi-voice table launch (Mark's words). One world list feeds both.
- Card front: portrait, Representative's name and title, the world's name and era. The intro line and the two actions are on the back.
- A seated card keeps a mark and a ring; the tray counts to three; "Go to the table" turns on at two.
- Era colour is a tint with the era name always written. Three tones proposed, to be measured before they enter the census.
- Reduced motion and phones get a list of the same cards.
- Every path lands on the existing talk page. The room's welcome, disclosure and safety handling are unchanged.

What must hold
- The eleven intro lines stay drafts under their own review. Donatism stays provisional.
- The "What the record holds" line on each card is derived from the world's own thinness statement and passes the readability check before it ships.

Evidence used
- The research plan, the fourteen-system comparison grid (each row labelled by how it was seen) and the three-direction prototype, all in the feature folder. Seven systems stayed indexed only because the session's network blocked them; the harness is ready to re-run when the hosts open.

Open
- Where the story teasers sit relative to the hand on the landing page.
- A name search must say why a world matched (Augustine matches Donatism as an opponent).

### Theme D, page order — 2026-10-19
- Mark: "Put the story teasers above the hand." Landing page order: headline, story teasers, the hand of cards with its deck controls, then the three doors. This resolves the open item under "Theme D, the chooser" above. The story pool itself is still unwritten.

## Coordination with the chooser thread — 2026-10-19
Decision (Mark): the "Conversation chooser research and design" thread owns the cards and the landing page order. The feedback thread's Theme D decisions and the C3, C4, C5 and C6 needs go to it as inputs, and the feedback thread makes no further edits to cic-website/index.html. The chooser decisions above are that thread's record.

## Theme B: answer the question, honestly, briefly — 2026-10-19

Status: converged (Mark: "Converged, auto mode"). Nothing built or tested.

Covers feedback items 8, 16 and 20 (the Luke 9:27 case, answers that describe the group instead of answering, rambling at the table, and the wish for the tradition's own wisdom).

Decisions
- No direct answer: the voice says so in one line and offers the nearest real source, cited. The nearest source must be real and close, never a stretch. If nothing is close, the honest line stands alone.
- Length: layers on the answer. One line first, then a short answer, then the full answer on request. This applies the 1, 3, 5 minute layers (Theme D) to a reply.
- Enforcement: approved text for the honest limit, written per world, so it cannot invent; plus a check after the answer for length and filler, with a redo when the check fails. The redo costs a second model call only when needed.
- At the table: a voice with nothing direct to add stays silent, with a one-line note or a small "nothing to add" mark. Only voices with something real speak at length.

What must hold
- No invention. Honest limits stay. Each world keeps its own voice, and an over-short reply that flattens the voice is a failure too.
- Contested claims keep their confidence tag; brevity must not drop it.
- The tester liked that nothing was made up. That is not to be broken.

Evidence used
- One tester's case, Mark's reading of user discussions, and another thread's measurement of past runs: 1,848 answers, median 264 words, mean 288, longest 1,425 words in the 19 October gallic sample. The feedback thread did not re-measure and did not read the voice's current instructions. No research round was run for this theme.

Open and not decided here
- Wording of the approved honest-limit line for each of the eleven worlds, who drafts it and how it is reviewed. The line is participant-facing voice text and is held to the accessibility, distinct-voice and no-invention rules.
- The thresholds for the length and filler check.
- How often voices have no direct answer, and whether layered replies fit every question type. Measuring this needs a named, capped live test approved by Mark; none has been run.
- How the silent "nothing to add" mark looks at the table, which belongs with the chooser and room design.
- This changes the engine and the voice text. It is a governance and methodology change, so it needs Mark's go-ahead before any build.

## Theme C: who am I talking to — 2026-10-19

Status: converged (Mark: "Converged, auto mode"). Nothing built.

Covers feedback items 6, 7, 14, 15, 16 and 23 (the missing well-known names, rabbis and Josephus, scholarly voices first, who a Representative stands for, the tradition's own wisdom, starting from what people know).

Decisions
- Real voices at selection: each card carries one line naming the writers the voice is built from. A person chooses the names per world and checks them against the records. Figure records are not listed automatically, since some are a church, a network or a group, not a person.
- Name search: a visitor who types a name sees the worlds that hold it, with a plain note on why each matched (a source, or an opponent as Augustine is in Donatism).
- Representative on the card: no "not a person" or AI statement. That disclosure already sits in the room's welcome and the site's AI note. The card says who the voice speaks for through the one line above.
- People with no world: if someone is genuinely a source in a world, include them there. If they have no world, the name search says plainly that while they were influential across the Christian traditions, there is no single tradition they are clearly part of.
- Representative names are not changed here. Naming and image remain a packaged decision of their own.
- The deeper "who is behind this voice" panel (names, dates, sources, using the room's figure mark) is a later layer, not part of the card.

What must hold
- No invented family, age or personal history for a Representative.
- Real voices named only as the records support them, with confidence tags kept.
- Card text meets the reading-level target and each world's own voice.
- Contested or uncertain claims never shown as settled.

Evidence used
- A check of the world records, by file name and by counting files that mention a name; the records were not read. Findings: Ignatius is a figure in the House Church world; Athanasius and Clement in Alexandria; Augustine in Donatism and Hieronymian and in a Latin pastoral record set not among the live tradition pages. Irenaeus has no figure record but runs through the House Church world as sources, quotes, stories and doctrinal witnesses. Tertullian is a source in several worlds. Josephus appears in none.
- One tester's complaint and Mark's reading of user discussions. No research round was run for this theme.

Open and not decided here
- Which writers each world's line names, and the review of those lines.
- The wording of the no-world statement, including for Josephus, who is a source for the early church and not a teacher the traditions followed.
- Whether Irenaeus should get a figure record in the House Church world (a records task with review).
- Which worlds to build next, whether around well-known names, and whether Jewish or rabbinic voices belong in the Library. Not decided; belongs to the world-building plan.
- Where the names line sits on the chooser's card, which belongs to the chooser thread.

## Theme E: the Church Family Tree to the table — 2026-10-20

Status: converged (Mark: "Converged, auto mode"). Nothing built.

Covers feedback item 17 (users want to reach the multi-voice Table from the Church Family Tree and pick all three traditions first).

Change order
- This reverses an earlier ruling, recorded in a comment in `cic-website/atlas-v3.html`, that launching a multi-voice Table from the tree is confusing without more context-setting. Reason: the chooser's seating tray now supplies that context. The comment is not edited here.

Decisions
- One seating behaviour everywhere. A card chosen for the table raises, like a card pulled from a hand, and stays raised and counted in the tray. The visitor can click up to two more cards, which raise too. When the table launches, it seats the two or three raised cards. "Go to the table" turns on at two.
- Searching again: the visitor can choose a card from the hand, then search, narrow by era or shuffle for another world for the table, and again. Seated cards stay held and are never dropped by a new deal.
- The tree feeds the chooser's hand. A "Seat at the table" button in each built tradition's panel raises that tradition's card into the same hand, held in the browser. Seats chosen on the tree and in the chooser are one table. The table launches from the chooser or from the tray on the tree.
- The first click never jumps to table selection. Only built worlds can be seated.
- The map itself is not changed: no new mode and no marks on the dots.

What must hold
- The tree stays calm. No overlays and no mode a visitor has to leave.
- The room's welcome, disclosure and safety handling are unchanged.
- The chooser thread owns the cards and the tray. Any change to the tree goes through it.

Evidence used
- A code comment in atlas-v3.html recording the earlier ruling, the chooser thread's build plan (which leaves the tree unchanged and records the tree as one launch source), and Mark's description. The tree was not run and no phone screen was checked. No research round was run for this theme.

Open and not decided here
- How the tray looks on the tree and on a phone.
- How long a held seat is remembered in the browser.
- How a visitor on the tree tells which traditions can be seated. Mark chose the card behaviour above and did not pick a map mark or a note on other panels.

## Thread ownership — 2026-10-20
Decision (Mark): the working set is four threads: Paused workstreams triage, Conversation chooser, Landing page and card selection, and Pilot feedback. The landing page thread finished (its four PRs merged) and the chooser thread built on its work.
- Chooser thread: cards, hand, tray, landing order, raised-card seating, the names line. This thread sends inputs and makes no product edits.
- Paused workstreams triage thread: settles 7 commits (1012af273, 111a5f906, 226da0aeb, 28d6642a5, 8ebb3fd78, c09c77288, c5fee0752) carried by 34 remote branches, including three dormant Library branches. By hash and a message search for "sentence-enforcement", they are in neither origin/main nor origin/live. Contents not read. One of them, c5fee0752, removes the sentence-enforcement retry in engine reply handling.
- Theme B engine work is on hold until the triage thread reports, because that retry change may interact with the planned check-and-redo.
- Theme F audio and the Theme D story pool have no owner thread yet.
- Pull requests from this thread go to main, not live (CLAUDE.md 4.1). PR 976 targeted live before that rule was in place; it is merged.

### Correction to the thread ownership entry — 2026-10-20
The Paused workstreams triage thread reported on the seven commits. By hash none is an ancestor of origin/main, but by content main already has them: PR 869 was merged on 2026-10-13 (head 226da0aeb), the sentence-enforcement code is gone from the engine code on main, the added lines are mostly present, and all 40 records/syr/source records carry a citation line. It did not merge anything and recommends that the Library branches be rebased or merged onto current main so the seven drop out as duplicates. It checked line matches, not every file: engine/m4/turn.py has 35 of 52 added lines present and engine/m9/enforce.py 2 of 12, and it did not read turn.py to confirm the fallback to the world's answer record is intact.
- The earlier statement here that the seven are "in neither origin/main nor origin/live" was true by hash only. The duplication risk is smaller than stated: the content is on main.
- Theme B stays on hold, for a different reason. The removed retry is part of PR 869, "quotes by code, no rewrite". The title suggests a deliberate choice not to rewrite replies after generation. Theme B plans a check after the answer with a redo, which may contradict it. Nobody has read PR 869's reasoning against Theme B. That has to happen before Theme B is built.

## Theme F: audio for the fixed text — 2026-10-20

Status: converged (Mark: "Converged, auto mode"). Nothing written, generated or spent.

Covers feedback items 18 and 25 and the audio parts of 24 (the Church Family Tree audio is too technical; audio for everything fixed, not for generated conversation; ElevenLabs as the voice).

Decisions
- What to voice first: new short hooks for the 11 built tree worlds. Each is a 30 to 60 second plain-language hook at the top of that world's tree page, in text and in audio, followed by the long story and its existing audio. The one-minute story pool from Theme D is voiced after it is written.
- Whose voice: each built world's own voice, keeping Mark's 2026-09-27 ruling that gave the 11 built worlds distinct voices for tree narration. The script is documentary and sourced, never in character, so it cannot read as invented speech from a Representative.
- Delivery: a play button beside the hook. The hook text is always shown, and audio plays only when pressed. The line "Read by a synthesized voice, not a recording" stays.
- Scope: audio only for fixed, reviewed text. None for generated conversation replies, until funding exists for it.

What must hold
- Text is always kept. Audio never replaces it.
- A paid bulk run starts with a small sample that Mark approves by ear. The voice and every setting are passed on the command and printed with item and character counts (CLAUDE.md 3.2). Nothing is generated before then.
- Hook text meets the reading-level target and each world's record, with no invented speech.

Evidence used
- A count of the audio files in cic-website/audio: 990 files, 644 MB (516 documented stories, 282 tree narrations, 62 stories, 11 to 12 per built world, 7 site files). The 2026-09-27 and 2026-09-28 entries in the front-end decision log; the site audio manifest, which records one ElevenLabs voice id, the model eleven_v4 and fixed settings. No audio was played. The cost estimate of $50 to $100 per million characters comes from the System Hub log and was not rechecked. No research round was run for this theme.

Open and not decided here
- The 11 voice picks. Checked 2026-10-20: all 11 per-world voice overrides in Build/tools/tree-narration-voices.mjs are empty, so every tree narration uses the single default narrator until Mark picks voices. Which voice id the default narrator uses for the tree is not checked.
- Who writes and reviews the 11 hooks, and how each is checked against its world's record.
- Whether the repo or object storage holds the new files. The storage question in the 2026-09-27 log entry was not checked for a ruling.
- No thread owns this work yet. A site audio thread is proposed.
- The story pool for Theme D has no owner and is not written.

## Theme G: after the free tokens — 2026-10-20

Status: converged (Mark: "Converged, auto mode"). Nothing built.

Covers feedback item 9 (the tester loves the 300 free tokens and asks whether it goes to a paywall after) and the funding half of item 25.

Decisions
- The landing page line, near the doors (placement from Theme D): "Free to start. Add more any time." No price on it. Mark chose this over "Free to start. Gifts keep it open.", which I had recommended.
- The room keeps its small token count, off the stack under the question box (Theme D). The existing limit wording stays: "To carry on in this conversation, add tokens or enter a code." and "Your tokens have run out. Add more to carry on."
- The answer to the tester: it is not a wall. After the free allowance a visitor can add tokens, enter a sponsor's code, or wait. Free conversations are kept open by gifts.
- Funding strategy, the bridge funding and the legal structure are not decided here. They belong to the funding workstream.

What must hold
- No price in the app; Stripe shows the amount.
- A number shown to visitors is read from the operations file, so the page and the allowance cannot drift.
- The line meets the reading-level target.

Evidence used
- The Go Deeper decision log (Build/Ministry/Features/Go-Deeper/Decision-Log.md) and engine/deeper/ops/go-deeper.yaml, read on 2026-10-20: a free allowance of 550 tokens in a 30-day window per visitor and 3 rounds per free conversation; packs of $7, $15 and $30; a weekly gift-funded ceiling with stages; sponsor and tester codes. The yaml was last changed three days earlier in a commit titled "Open the pilot to the general audience". No research round was run for this theme.

Open and not decided here
- Whether the buy button is live and a Stripe Payment Link is set. An earlier log entry says it stays hidden until one is set; not checked.
- What the tester's "300 free tokens left" was counted from. It fits a 550 allowance partly used, which is not confirmed.
- Who builds the landing line. It sits with the chooser thread's landing page work.

## Change orders to Theme D — 2026-10-20

Source: Mark, after seeing the built landing page (PR 987).

1. **Story teasers are dropped from the landing page.** Mark: he chose the spacing and the card descriptions rather than the story teaser, and wants the cards on the landing screen. This supersedes three earlier entries: the Theme D decision that the first invitation is a short story, the amendment for a rotating few story teasers, and the chooser thread's "Put the story teasers above the hand" page order. Reason: Mark's choice once he saw the built page.
   - Still standing: layers by time as the model for depth, and sources one click away at every layer.
   - The "rotating few" idea now describes the hand's deal of five cards. Whether the deal skips cards the visitor has already seen is for the chooser thread to confirm; this thread has not checked.
   - The one-minute story pool is no longer needed for the landing page. Whether it is still wanted for the tree or the Theme F hooks is open.
2. **"Tell us what you think" stays in the masthead, as a button to the left of the Menu, not inside it** (Mark, 2026-10-20). PR 987's description records a later change order by Mark: one masthead row with the wordmark, the three feature links, "Tell us what you think" and Menu. This supersedes the Theme D header decision that moved it into the Menu. Source: the PR description; the chooser decision log was not read here.
3. **Where Theme G's landing line goes is open.** It was to sit near the doors. The doors are now plain text links in the masthead and the line "Free to start. Add more any time." is not on the page. Mark has not said where it goes.

### Clarification to Theme E, card behaviour — 2026-10-20
Mark: "the cards scroll and click to pull forward." The hand scrolls through the cards, and clicking a card pulls it forward. This describes how a visitor moves through and brings a card to the front, and sits beside the Theme E seating rule (a card chosen for the table stays raised and counted). Checked by the chooser build thread against cic-website/assets/chooser.js on the PR 987 branch (reported to this thread; not read here): a click on a side card pulls it forward; a click on the active card flips it to the back; the hand also moves with the Previous and Next buttons and the arrow keys. It found no mouse-wheel or swipe handler, so "the cards scroll" is not built for the hand; the only horizontal scroll is the "See all" mini-card row. Seating is separate: the "Seat at the table" button on the card back toggles the seat tray, and the click that pulls a card forward never seats it. Card body text is 1.1em on a card font of 4% of card width: about 9 px at a 210 px card and about 17 px at the 380 px maximum. Open: whether Mark wants scroll and swipe added to the hand.
- Decision (Mark, 2026-10-20): scroll and swipe are added to the hand, besides the Previous and Next buttons and the arrow keys. A wheel or trackpad scroll must act only while the pointer is over the hand, so it cannot trap a visitor scrolling the page. Passed to the design thread, which now holds PR 987, as a request. Nothing built here.

### Status after PR 987 merged — 2026-10-20
PR 987 is on origin/main at 51cbfb4c (checked on main: a wheel handler is in cic-website/assets/chooser.js). Reported by the chooser design thread and not all read here: cards on the landing screen with no teasers; "Tell us what you think" as a button left of the Menu on every page with the masthead; scroll and swipe on the hand (the wheel rolls one card per notch over the hand and leaves page scroll alone elsewhere; swipe was already there). Not done: the "Free to start. Add more any time." line (no home chosen), the card body text size (no ruling), the tree's "Seat at the table" button, and the iPad, phone and screen-reader pass. Decisions are in Build/Ministry/Features/Conversation-Chooser/Decision-Log.md.
