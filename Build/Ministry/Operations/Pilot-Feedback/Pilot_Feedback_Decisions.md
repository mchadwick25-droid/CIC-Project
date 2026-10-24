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

## Item 29: the conversation pages — 2026-10-21

Status: converged (Mark chose "Converged: build to main" in the option box on 2026-10-21, after working through sketches in a design thread). Built in cic-poc/frontend on branch claude/magical-goodall-ucv6e2. Not yet promoted to live; promotion is Mark's call through the runbook.

Decisions (Mark, from the sketches)
- One conversation area. A card on top for one voice, three small cards side by side for the Table. Same landing-card look: gold frame, era band, portrait fading into a plate, gold serif name. No greyed or stretched portraits.
- The page, top to bottom: a slim bar with a ⋯ menu, a flat token ribbon, the cards, the conversation, the box under it.
- ⋯ menu: About, Tell us what you think, Report a problem, Leave for now, and Delete this conversation in red.
- The welcome line is the engine's door turn. It shows under the card until the first question, then closes.
- Thinking: a small book with leafing pages beside "{name} is considering"; at the Table, "The table is considering". No other text beside it.
- The reply rolls out word by word at a steady pace, in order, and never pops in. The conversation grows down the page from the card; once the box is reached it scrolls, with space left under the newest line.
- Scrolling back: a gold scroll bar for a mouse or trackpad; a finger scrolls on a touch screen with no bar; a "Latest ↓" button brings the reader back.
- Token ribbon: "{n} tokens left" in gold at the left, "Get more conversations" in gold at the right, no underline, and a gold line along the bottom that slides when the count changes. Under 100 tokens the count turns white; the link stays gold. The count shows after the first reply (Go Deeper log, 2026-10-05).
- Table: five or six replies in an uneven order. Each card lifts and glows only while its voice speaks, then hands over. While the table is still thinking no card glows (option B). After the last reply every card rests.
- Smoothness: new blocks open from nothing and the page follows them, so nothing jumps.

Change orders (Mark's words in the thread; reasons are his)
1. **The in-room disclosure is removed from the conversation page.** Dropped: the "system exists to reveal Jesus" paragraph, the "name is ours" line, the ✲ line, "What this voice knows well — and doesn't", and the "AI voice" note. Mark: "this idea is in the about page, doesnt need to be on every conversation", "the statement of the ai voice is on the main page, we don't need it on the conversation also, i want this as clean as possible and not this ai transparency focus, we don't need to tell everyone everything". This supersedes the Theme D line "The disclaimer stays" and the Theme C line that the AI disclosure "already sits in the room's welcome and the site's AI note". The About panel keeps the voice, its place and the living-tradition line. **Not checked:** whether any law or platform rule (Apple's guidance on AI features, for one) calls for an AI disclosure inside the conversation. Mark should confirm before promotion.
2. **The small token count moves from under the box to a ribbon under the top bar** (supersedes the Theme D placement "off the stack under the question box").
3. **"Go deeper" is freed for depth.** The token panel's name and its button in the room are now "Get more conversations". "Go deeper" is kept for going further into the conversation or the world, which is not built. Mark: "go deeper in this context would assume going deeper in the conversation or world, pay as you go, get more time needs to be the kind of message".

Chosen while building, not by Mark (flag, change if wrong)
- The gold line's full length is the most tokens this browser has seen (stored in localStorage as cic_balance_peak). Mark asked which scale to use (550 free, or the last top-up) and did not answer.
- The suggested-question chips and the page-level "This helped" like are gone; the sketches never showed them and Mark never asked for them. The per-reply "This helped" and "Answer was not clear or accurate" links under each finished reply stay as they were.
- The card band's era comes from the world's time window (eras copied from cic-website/data/world-census.json). The landing page uses the census's own era per world, so a world whose window opens before its census era may show a different band.
- The panel's wording inside "Get more conversations" is unchanged ("Tokens pay for each new conversation and each round…"). Mark saw only the ribbon.
- "Latest ↓" shows on touch screens too; Mark did not answer whether it should.

Checks
- Frontend tests, type check and a run of the real app in Chromium with a mocked API at a phone and a laptop width. Not checked: a real phone or tablet, a screen reader, or the live streaming path (the mock returns whole replies).


## Records catch-up — 2026-10-21
Entries below correct or add to earlier ones. Nothing earlier is edited.
- **Theme E, scroll and swipe:** the 2026-10-20 decision added wheel and swipe to the hand. The wheel was removed on 2026-10-20 (no wheel handler in `cic-website/assets/chooser.js` on main, checked 2026-10-21). The "Status after PR 987 merged" entry that says a wheel handler is on main is out of date. The visible list control stands in for scrolling without a wheel.
- **Rulings reported by the other pilot feedback manager (Mark), not read at their source:** (1) one build thread at a time; (2) Theme B's length and filler check only logs and never triggers a paid redo, which also settles the earlier worry that a check-and-redo could contradict PR 869; (3) the in-room AI note is one small light line at the foot (PR 1013). Item 29 change order 1 removed the long in-room disclosure; this is the small line that remains. The unchecked question there (whether a law or platform rule calls for a disclosure in the conversation) is still open for Mark.
- **Theme G:** "Free to start. Add more any time." is built under the hand (log, 2026-10-20). The Theme D change order saying it has no home on the page is out of date.
- **Access and payment, new work:** coupons and exceptions for particular people, and pay as you go. Mark has not given the design. Mechanics that exist: free allowance, packs, sponsor codes, tester codes (`engine/deeper/ops/go-deeper.yaml`). A tester code passes the daily cap (`engine/api/anon_cap.py`, checked on main 2026-10-21). Asked first, nothing built.
- **Daily cap, flagged and not asked:** a conversation counts toward the 5 a day when it is created, even if the first voice reply then fails.
- **Admission gate:** `python -m engine.m3.admission_conform --enforce` failed for all 11 worlds on 2026-10-21. Mark has not ruled on running, waiving or holding it for the whole fleet. A log entry says it was waived for the conversation pages.

## Coupons for named people — 2026-10-22
Decision (Mark, 2026-10-22): a coupon is a sponsor code made for a named person. The name is kept outside the system. Mark mints a code with the existing routes and keeps his own list of who received which code. Nothing is built.
- Existing routes, read in `Build/Ministry/Features/Go-Deeper/Decision-Log.md` (entries of 2026-10-04 and 2026-10-15) and not run: `POST /api/admin/deeper/mint` (a pack and a count, as separate codes or one code; a gift, not a sale) and `POST /api/admin/deeper/tester` (more tokens and a last day; $0 toward the door).
- Why outside: the design stores no name, email or note with a code, so the meter and the conversations share no key with a person. A label on the code would be a change order on that ruling and on the privacy page.
- Pay as you go: already designed and built as Go Deeper. Open items are in the Go Deeper decision log (Stripe stored-value answer, legal and tax questions, refund and expiry wording, AWS budget ceiling). Nothing new decided here.

### Coupon delivery: one button, inside the system — 2026-10-22
Decision (Mark, 2026-10-22), superseding "Mark keeps his own list, nothing is built" above for the long run: Mark wants to grant a coupon with one button, approved by him, with no emailing and nothing sent by hand. The coupon is delivered inside the system. Mark chose to wait for accounts rather than build an interim link. Nothing is built.
- Requirement for the accounts build thread: an admin control to pick an account and grant tokens to it with one tap. It must respect the 2026-10-05 accounts change order (decision 53): no name stored, the account store holds only a scrambled address value. How the admin finds an account without storing a name is for that thread to design and bring to Mark.
- Until accounts exist, coupons are codes Mark mints (mint or tester route) and passes on himself.
- State checked 2026-10-22: no accounts module in `engine/`; accounts were designed to ship dark behind `CIC_ACCOUNTS_ENABLED`, after the door's observe week. Whether any accounts branch exists was not checked. The engine has no email sending.

## No daily reset on visitor limits — 2026-10-22
Decision (Mark, 2026-10-22): the free allowance is monthly with no daily reset. More tokens come through the pilot or a purchase. Mark asked for recommendations on which limits to remove and approved them as written below. Nothing is built from this thread; a build thread does the code change.

Checked 2026-10-22 on `origin/live` (same as main for `engine/deeper` and `engine/api`):
- Already as ruled: the free allowance is 550 tokens in a rolling 30-day window kept in the meter file (`engine/deeper/free.py`, `go-deeper.yaml` `tokens.free`). Solo cost is 50 to open, 20 a round for rounds 1 to 3, 25 from round 4 (`engine/deeper/tokens.py`, `LATER_ROUNDS_FROM = 4`). The pilot join gives one $7-pack code (1,100 tokens) per address; on live the general audience is open, capped at 100, to 2026-12-31.
- The fault: `engine/api/deeper_admission.py`, `Admission.provider`, sets `limited = daily_cap_reached or …`, so the daily conversation count (`engine/api/anon_cap.py`: 5 new conversations and 150 messages per visitor per UTC day) closes the free path even when the visitor has free tokens left.

Requirement for the build thread:
1. Remove the daily visitor counts (5 conversations, 150 messages) and the daily Facilitator-only sitting that exists only because of them. The per-message safety check stays.
2. Keep the visitor cookie. The free allowance is keyed on it, and the engine refuses to start with the free allowance on and the visitor cap off (`CIC_API_ANON_CAP_ENABLED` stays on); change the counts, not the flag.
3. Keep: the group code daily ceiling (`group_daily_ceiling` 6,000), the door including `daily_share`, the admin and tester operator caps, the per-minute burst limits (`engine/api/ratelimit.py`), the 3-round free cap and the paid round cap of 40.
4. Related: a conversation counts when created even if its first voice reply fails; fix with the same change. The Go Deeper page sentence "each day has a free allowance" is untrue since 2026-10-04 (log, S2b); check and correct it with Mark's words.
5. Not a fix: setting `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` very high in Render would work today but is a workaround.
- AWS cap: Mark says one is set. Not confirmed from the repo; `CiC_Alerting_Runbook.md` describes an AWS Budgets alert and says Mark picks the figure. Whether it blocks spending or only alerts was not checked.

## Correction to the coupon decisions — 2026-10-22
The entries "Coupons for named people" and "Coupon delivery: one button, inside the system" above are not edited. This entry corrects them.
- Mark first chose to keep the name outside the system and keep his own list. He then asked for a one-tap grant inside the system with no emailing and nothing sent by hand. The accounts thread's ruling 3 does this: the operator types the person's address once at one button, only its keyed hash is kept, and the coupon attaches at the person's next sign-in. The system never receives a name.
- At this thread's request the accounts thread put the question to Mark. Reported answer (not read at its source): the design decisions were made; he wants it seamless, no copy and paste and no emails from him. Ruling 3 stands. Recorded in the accounts thread as ruling 24 in the Go Deeper Decision-Log (PR 1033, in review at the time).
- So "the name is kept outside the system" now means the system never receives a name. It does see an address once. Nothing is built for the grant button; accounts slice A1a is a draft (PR 1033).
- The statement above that coupons are "a code Mark mints and passes on himself" holds only until accounts are switched on.

## Daily limits and conversation text — built — 2026-10-22
- The no-daily-reset requirement above is built and merged by PR 1032 (see the log). A build thread handled it; the accounts thread declined it as a change to the live visitor path. Remaining: `cic-website/privacy.html` words (Mark's), the two Render variables (Mark, optional), promotion to live (Mark, through PR 1034).
- Item 30 text sizes were chosen by Mark in the conversation pages thread: intro 17 px, ribbon 16 px. PR 1031 merged.

## Independent review of pay as you go and accounts — 2026-10-22
Mark asked for a review of the whole pay-as-you-go and accounts system. An Opus 5.5 subagent in the system and pilot feedback management thread read the code and logs on origin/main (read-only, no model calls, no spend) and reported twelve findings. This thread spot-checked five of them in the code (ratelimit.py limits, deeper_routes.py add_funds for pilot and admin grants, anon_cap.py cookie issue, door.py gift sum, accounts service.py date-of-birth step); the dollar figures are the reviewer's estimates and were not re-derived. The reviewer could not run the safety-at-every-limit seam tests (the built world packages were absent in its checkout), so did not see them pass.
- F1 (blocking): with the daily visitor counts gone, the only per-visitor bound is 40 messages a minute per address; each message still costs a safety check (the log estimates about $0.003), so one script can close free voice for everyone in about 23 minutes at the live door settings, and keep spending after. IPv6 is counted by /64, so a home user can look like 256 networks.
- F2 (serious): each pilot join and admin grant adds its pack price as a gift to the door's weekly ceiling ($5.60 of ceiling per $7 pack), although no money arrives; tester codes and coupons count $0. Open for Mark.
- F3 (serious): the free allowance is keyed to a cookie the server issues to anyone without one, so a cookie-dropping script gets a fresh 550 tokens each time; it also defeats the accounts rule that a new account starts with what is left of the browser's free window.
- F4 (serious): `cic-website/privacy.html` still states the removed daily limits. Words are Mark's.
- F5 (serious, blocks the accounts launch): anyone who knows an address can lock its owner out of sign-in for the day and send that inbox ten codes.
- F6 to F12 (minor): six-digit code guessing odds; refill day clamps to 28 where the ruling says the month's last day; A1a still asks for a date of birth (A1d replaces it); the pilot page has no age line; the door's switch to enforcing and the $75 then $12 base have no decision-record entry; a flat 25 tokens a round to round 40 may under-price late rounds; small refund and dispute gaps.
- The reviewer reads AWS's documentation as saying an AWS Budget is a once-a-day alert unless a Budget Action is configured. Whether Mark's budget has an action is not known.

Decision (Mark, 2026-10-22), on the first open question (what bounds a visitor and a network now): Mark does not want to choose a mechanism. The goal is that the most a single troublemaker or script can cost in safety checks is about $1 a month per visitor, and a few dollars per shared network, without blocking real people. Passed to the thread that built PR 1032 (session_014kMdzhac3pg4njANzhBJ2m) to re-check F1 and F3, propose the smallest correct design with its worst-case dollar cost, and show Mark before building. Nothing built. Mark's suggestion to end a conversation after 5 idle minutes or two empty turns was heard; it tidies idle sessions but does not bound a fast script, so it is not the bound.
- Still open for Mark: pilot and admin grants counting $0 toward the door (F2); whether safety-check spend at a closed door should count toward closing the door; the AWS budget (alert only, or an action that stops spending, and the figure); the pilot join count; whether the 2026-10-17 switch of the door to enforcing and the $12 base were meant; replacement words for `privacy.html`.

## Visitor bound and door rulings after the review — 2026-10-22
Mark answered the review's open questions one at a time. The proposal they refer to is the build thread's Artifact "Safety check budget" (https://claude.ai/artifact/PdzGxMjy3KEdX6BXNeKZ57), which this thread read; its F1 and F3 re-check was done by that thread (session_014kMdzhac3pg4njANzhBJ2m) and reported, not read here. Dollar figures use the Go Deeper log's estimate of $0.003 per safety check and an assumed, unmeasured $0.06 per voiced round. Nothing is built. Mark has not said "converged, auto mode"; the build is not started.

1. Past a visitor's monthly count, a message gets a fixed Facilitator line with the crisis resources added by code and no model call. This is a safety-protocol change decided by Mark (a governance and methodology decision). Chosen over keeping the full AI check on every message.
2. Counts of messages that got a safety check and no voice reply, rolling 30 days, kept as scrambled values in the meter file: **100 per visitor and 200 per network** (IPv4 address or IPv6 /56). Worst case about $0.30 and $0.60. Mark chose these over the proposal's 300 and 900. Noted risk: a class of about 25 on one network could reach 200 together; a group code is the usual route and groups are not built. The build thread shows Mark the numbers as they run.
3. Per-network free-voice window: **5 allowances (2,750 tokens, about 75 voiced rounds, about $4.50 worst case)** over 30 days. A network's worst case is about $5.10 in all. Noted: the door allows about $2.81 of free-voice spend a day, so one network can use its whole pool in a burst and close free voice for a day, once per 30 days; a pool of 3 ($2.70) would sit just under that line. Mark's choice stands; he can reconsider.
4. Pilot and admin grants count **$0** toward the door, as tester codes and coupons already do (call sites `engine/api/deeper_routes.py` lines 539 and 579 at review time). The $12 weekly base is then a real cap. Noted consequence: in a busy pilot week the door may pause free and pilot voice until the week turns; Mark can raise the base later once real weekly spend is known.
5. Safety-check spend keeps counting toward the door's ratio. Chosen over leaving it out or capping its share.
6. AWS cap: Mark will check his AWS Budget (the figure, and whether it has a Budget Action that stops spending or is alert only) and report. Nothing recorded as fact. The reviewer read AWS's documentation as saying a Budget is a once-a-day alert unless an action is configured; that was not verified by this thread.
7. Privacy page cookie section (`cic-website/privacy.html`, `#visitor-cookie`), wording approved by Mark: heading "One cookie, to keep the free allowance fair"; paragraph `cookie-one-job`: "The cookie does one job. It lets us count unique visitors."; paragraph `cookie-two-jobs`: "The cookie does two jobs. It keeps track of your free allowance, described in the next section. It also lets us count unique visitors." The sentence about the new monthly counts (a scrambled count for the visitor ID and one for the network, deleted 30 days after the first message counted) waits until the counts are built and returns to Mark; the 30-day deletion must be confirmed by the build. The page ships with the promotion that carries PR 1032.
- Still open for Mark: the pilot join count; whether the 2026-10-17 switch of the door to enforcing and the $12 base were meant (no decision-record entry); the AWS report; and whether the build may start (answered in the next entry if so).

## Change order: the free 3-round rule is removed — 2026-10-22
Decision (Mark, 2026-10-22): the only thing that should limit the free allowance is the token count. Chosen option A: drop the free 3-round rule and leave the engine's own caps in place. Nothing is built; the change is passed to the thread that built PR 1032 (session_014kMdzhac3pg4njANzhBJ2m) to build after Mark's go-ahead there.
- Supersedes: the 2026-10-03 token table row "Free: a conversation stops after 3 rounds; a code lifts the cap" and the 2026-10-04 S2b wording "five solo conversations of three rounds" (Go Deeper Decision-Log). Source of the rule in code: `engine/deeper/ops/go-deeper.yaml` `tokens.free.rounds_per_conversation: 3`, applied to free visitors in `engine/api/deeper_admission.py`.
- Stays: the engine caps `SESSION_TURN_CAP = 10` voiced rounds for a solo conversation (`engine/m4/turn.py`) and `TABLE_SESSION_ROUND_CAP = 3` for a Table (`engine/m4/round.py`). Free length is then the smaller of the tokens and these caps. A 10-round free solo conversation costs 285 of the 550 tokens (50 to open, 20 a round for rounds 1 to 3, 25 from round 4).
- Why the rule existed: a conversation's per-round cost grows with its history (the comment on `SESSION_TURN_CAP`); the flat 25-token price from round 4 may under-price late rounds (review finding F11, not measured). Option B (lift the engine caps for free visitors and price later rounds to real cost) was offered and not chosen; it needs the cost measured first.
- Words now untrue and awaiting Mark's approval of replacements: the Go Deeper page line "A free conversation lasts three rounds, and you get a free allowance each month." and any copy in `cic-poc/frontend/src/lib/deeperCopy.ts`, the privacy page or the pilot page that says three rounds. Passed also to the participant-experience design thread (session_012jjhAokk8iJ5PiFZ3Tn15r) so its screens do not repeat it.
- Commissioned the same day: a Fable design thread for the participant experience of tokens, buying and optional accounts (session_012jjhAokk8iJ5PiFZ3Tn15r). Design only, Artifacts for Mark's review, backend rulings closed.
- Earlier record line corrected: PR 1040 says Mark had not yet said "converged, auto mode" on the visitor bound; that was true when written. Mark then said it to this thread. The build thread asked Mark itself in its own thread, as it should; his answer there governs.

## Parked threads and one big project at a time — 2026-10-23
Decision (Mark, 2026-10-23): the Library era builds and the Church Family Tree navigation work restart when the current big project (pay as you go, tokens and accounts, with the participant-experience design) is finished. Reason, in Mark's words: "we just keep getting into trouble when we do too many things at once." This confirms the earlier reported ruling of one build thread at a time. Nothing is deleted; each thread's work stays where it is.
- Parked, restart after the big project (statuses are the threads' own last reports, 2026-10-23, not re-checked here): Library Era III (session_81YLgpE5…, branch `library/era-iii-2026-10`, batch 1 pushed), Era VI (awaiting a Franciscan checkpoint call), Era VII (`library/era-vii-2026-10`), Era VIII (`library/era-viii-2026-10`); Church Family Tree navigation (input remap and the pinch-and-glide input in `cic-website/atlas-v3.html`, option A not merged).
- Not decided: the Conversation chooser research thread (branch reset to main@30b9463, no new PR) was not named by Mark; it stays idle until he says.
- Archived the same day, finished work, reversible: account system research, integrity issues, pilot launch recruitment, conversation layout redesign.
- The big project's active threads: the participant-experience design (Fable), accounts from A1d onward, and the daily-limits thread finishing PR 1050.

## Finish line for the big project — 2026-10-23
Decision (Mark, 2026-10-23): the tokens and accounts project is done, and LPC can start, when buying works end to end and the visitor experience is approved. Buying works means Stripe is live and a real smallest-pack purchase and refund are proven. Accounts continue after that as one quiet tail thread until the mail provider and the lawyer's answers arrive. Chosen over "everything including accounts switched on" and over "stop now with buying dark."
- What that finish line needs (from the 2026-10-23 status; each item is open): three Stripe Payment Links and the webhook with the matching Render settings; the buy page changed from one link to three; Stripe's written answer on stored value; the lawyer's answers on expiry and refund wording; one real smallest-pack purchase and refund; dropping `noindex`, linking the Go Deeper page and adding the age line to the pilot page; the participant-experience design approved by Mark; the next promotion (accounts A3 and the cost report) and Mark's reading of the cost report.
- Accounts tail, not part of the finish line: the mail provider choice, the words-and-screens and backup-and-deletion slices, the sign-in findings F5 to F7, and the coupon grant button.
- Handoff for this thread: `Build/Ministry/Operations/Handoffs/2026-10-23_system-and-pilot-feedback-management.md`.

## Promotion, Theon card, LPC next — 2026-10-23
- Decision (Mark, 2026-10-23): hold accounts A3 out of the promotion, and merge the replacement promotion PR 1056 at once. Done; see the log entry "Promotion to live — 2026-10-23".
- Item 31, Theon's card (Alexandria): the portrait looks zoomed in. Two causes found by this thread and confirmed by the chooser thread's render: the picture takes the height left after the card text (`.pic{flex:1 1 0}`), and Theon's text is the second longest of the eleven cards (237 characters against 162 to 271), so his picture window is short (223 px on desktop and 147 px on a phone, against 223 to 260 and 127 to 209 across cards); and `alexandria.png` is a tighter close-up than the other portraits. Mark asked to zoom out further. The fix is CSS only: a picture height that does not depend on the text, and a further zoom-out for his portrait. A wider portrait would be a paid image step needing a small sample Mark approves first. Open: Mark is looking at the chooser thread's before and after; one small PR follows his agreement.
- LPC (the Latin pastoral world, `Build/worlds/lpc/`, with Augustine's sermons rendered): Mark chose to start it next, after the tokens and accounts project, not in parallel. Meanwhile this thread's scoping brief stands: about 2.14 million Latin words in the four vendored sermon files (about 1,340 sermon headers, approximate) plus about 1.0 million in the Enarrationes in Psalmos; the world sits at V2.0 rebaseline phase L0 with its open checks listed in `lpc_Rebaseline_Declaration.md`; every modern rendering is written by Opus 5.5 under CLAUDE.md; rendering cost not priced (a small approved sample sizes it); whether a full modern English edition exists in the public domain was not verified. Open questions for Mark when it starts: what "make available" means, which sermons first, and whether the Representative stays Datus.
- Cost report request: Mark chose a read-only admin report to measure the real cost per voiced round, cache warm or cold, and per safety check. Built (PR 1055, on `main`, not on live). After the next promotion Mark opens it once and sends the numbers; the daily-limits thread then answers whether the flat 25 tokens from round 4 under-prices real rounds (review finding F11).

## Buying, no test purchase, LPC now, and a promotion conflict — 2026-10-23
- Buy page naming (Mark): the visitor-facing name is "More conversations: N tokens" at $7.00, $15.00 and $30.00, not "Go deeper". File names and addresses stay (`go-deeper.html`, `go-deeper-return.html`). Mark set the three live Stripe Payment Links, the Stripe event destination and the `CIC_DEEPER_PRODUCTS` list in Render himself, from this thread's walkthrough. Not confirmed by Mark: each link's redirect, fixed quantity of 1, and amounts at checkout.
- No test purchase (Mark): "i dont want to spend money." The finish line named a real smallest-pack purchase and refund. Mark chose to prove the buying path at $0 instead (admin-minted code and tester code) and leave real payment untested until a real buyer. Mark later had the payment links merged (PR 1067, https://github.com/mchadwick25-droid/CIC-Project/pull/1067), as the visitor-limits thread reports; this thread did not see that instruction. Result: the unlisted buy page can take payment; no payment has been made or proven.
- Open conflict, not decided: the privacy first line approved for PR 1083 (https://github.com/mchadwick25-droid/CIC-Project/pull/1083) says nothing is for sale and no payment is taken, while the buy page can. Options put to Mark: hold the line and draft a payment paragraph, merge as approved, or switch the buy buttons off. Mark has not answered. This thread asked the visitor-limits thread to hold that one line until he does.
- LPC starts now (Mark, 2026-10-23, overriding "after this project"): a new thread, scope per Mark: all Augustine's sermons rendered and categorized like other worlds (quotes, stories, lexicon, general reference), able to answer broad and deep Augustine questions including the Reformation questions from people pairing LPC with the Swiss cities; Datus stays; the representative role has been removed for all representatives (ruling not located by this thread). Scope records: PR 1068, https://github.com/mchadwick25-droid/CIC-Project/pull/1068.
- Promotions at Mark's direct word: PR 1076 (https://github.com/mchadwick25-droid/CIC-Project/pull/1076, merged, live at b2733002, health confirmed) and PR 1081 (https://github.com/mchadwick25-droid/CIC-Project/pull/1081, open). This thread opened both because Mark asked. The CLAUDE.md that loaded today says a session never opens a PR into `live` itself; the conflict was named to Mark and is his to settle.
- Flip cue and card spacing (Mark): the word "Flip" at the lower right of each chooser card as a plain cue (PR 1066, https://github.com/mchadwick25-droid/CIC-Project/pull/1066, merged); then the empty band under it removed (PR 1075, https://github.com/mchadwick25-droid/CIC-Project/pull/1075, merged).
- Weekly allowance (Mark): he is deliberately spending the end of the week's allowance before the Friday 2:00 pm reset; the four Library era threads and LPC are running for that reason, not by drift.

## Full-system review rulings and LPC first — 2026-10-24
Four Opus review threads reported on 2026-10-23 (main e64646393, live 469d072c): engineering and safety (draft PR 1091, https://github.com/mchadwick25-droid/CIC-Project/pull/1091), scholarly content (draft PR 1089, https://github.com/mchadwick25-droid/CIC-Project/pull/1089), participant experience (draft PR 1090, https://github.com/mchadwick25-droid/CIC-Project/pull/1090), and market view (a summary page, no PR). The findings are the reviewers'; this thread did not re-verify them, except that the public privacy page now carries the payment paragraph (checked 2026-10-24). Mark ruled one question at a time:
- Safety check fails (Mark): when the safety check itself cannot run, show the fixed Facilitator line and template-anchored crisis resources already used past the monthly limit, not a clarifying question or "the voice couldn't be reached". No model call. A safety-method change: it needs an independent Opus review against the old text before anyone reports what changed (CLAUDE.md 4.4). Governing doc: `CiC_L3D_Facilitator_Governance_V3.6`.
- First public accuracy message (Mark): quotes only for now. The evidence supports "every quote is placed from the original text and checked word for word". Not "everything it says is sourced": the 19 October claim check found 69 of 483 claims (about 14%) unsupported or contradicted and 44 (about 9%) in the wrong voice. Published rate and any wider claim wait for the records fixes and a re-run of the claim check. Exact public words are not yet written or approved.
- Records errors still live (Mark): seven of eleven record errors from the 19 October check were still in the records (reviewer's count; two confirmed against the texts by the reviewer). The close-out thread fixes them; a separate Opus thread then re-checks every fix against the vendored sources. The close-out thread is not to clear the finding itself. The recheck has not started.
- Pushback proof (Mark): a small named live test, capped, on two or three worlds, for pushback and fabrication-bait. Not authorized to run: Mark has not given a test name or a dollar cap, and CLAUDE.md 3.2 requires both and the explanation steps first. The last admission run was 9 October on older packages with no pushback tests.
- Front-end fixes (Mark): crisis styling and keyboard, no word changes: make the crisis message stand out on a phone and keep the "this is the Facilitator speaking" line in view; label the message box; return focus to it after each send. The arrival-text readability rewrite (grade 19.8 for Zurich, 19.4 for Donatism against 8 to 10) was offered and not chosen.
- Unmatched-payment alert (Mark): when Stripe reports a payment whose payment link is not in `CIC_DEEPER_PRODUCTS`, record it and show a red tile on the admin dashboard so the buyer can be fixed by hand. The products list stays in Render, not in the repo.
- Builder (Mark): the buying thread builds the safety reply, the front-end fixes and the payment alert as one batch in one draft PR. The close-out thread keeps the records fixes.
- AWS budget (Mark): the weekly door is gone, so the AWS budget is the only spending backstop and no record shows it stops spending rather than only emailing. Mark was given click-by-click steps to check the amount, alerts and any Actions on the budget and the Bedrock service quotas. Open: Mark has not reported what he saw. A budget action that blocks Bedrock at the limit would be a decision for Mark first.
- LPC first, Library paused (Mark, 2026-10-23): after the Friday 2:00 pm reset the first share of the new week's allowance goes to the LPC world build. The Library era threads finish what is in flight, write a handoff and stop; Mark restarts Library work later. Era VI landed (PR 1072, https://github.com/mchadwick25-droid/CIC-Project/pull/1072) and its thread is archived.
- Archived at Mark's word (reversible): Library Era VI and the four Opus review threads.
