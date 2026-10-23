# Pilot Feedback Log

Append-only. Entries are numbered; a merged entry's number never changes. Status changes are added as new lines under the entry, never edits.

## Batch 1 — 2026-10-19
Source: one pilot tester (name not given), notes passed on by Mark.

| # | Part of product | What they said | Sort | Status |
|---|---|---|---|---|
| 1 | Participant app: main screen | Main screen does not fit the screen (photo attached; not yet seen). | Quick fix | Open |
| 2 | Participant app: waiting state | While the AI is thinking, animate something so it does not look stalled. | Quick fix | Open |
| 3 | Participant app: reading area | Wondered where the answer went. Reading space was very small. Zoom did not work. | Quick fix | Open |
| 4 | Participant app: text selection | Copy/paste is glitchy: can highlight backwards but not forwards. | Quick fix | Open |
| 5 | Public site: page order | The table app is the biggest element; highlight it at the top instead of the bottom. | Quick fix | Open |
| 6 | World content: table choices | Choices at the table are lesser known and lack Ignatius, Irenaeus, Tertullian, Athanasius, Augustine, Clement. Why? | Bigger issue | Open |
| 7 | World content: scope | Would it make sense to add Jewish rabbis? Josephus? | Bigger issue | Open |
| 8 | Voice and answer behaviour | Asked about Luke 9:27. None of the three had an answer (good: nothing invented), then they described what their group generally represents. Asks whether that is wanted or whether they should just answer. Dislikes 400 words where 4 suffice. | Bigger issue | Open |
| 9 | Funding and product direction | Loves the 300 free tokens. Assumes a paywall comes after. | Bigger issue | Open |
| 10 | Participant app: disclaimer | Loves the disclaimer before conversation. | Praise | No action |
| 11 | Overall | Loves it. Great tool to go right to the source. | Praise | No action |

## Status updates — 2026-10-19
- Mark approved quick fixes 2 to 5 as one batch (item 1 waits for the photo).
- Item 2: built. The waiting note now shows larger animated dots in the table room and the interview room.
- Item 3: built. The table room now brings the newest question to the top so the answer opens below it, as the interview room already did. The zoom fault was the app's height tracking: pinch-zoom shrank it. It now allows for the zoom level.
- Item 4: not fixed. Nothing in the code blocks forward selection; it needs a reproduction (device and browser).
- Item 5: built. The Build a Table card now sits first on the home page, above Church Family Tree.

## Status updates — 2026-10-19 (photos)
- Item 1: Mark sent six iPad photos of the table room and home page and confirmed the table room is the screen that does not fit. In the photo the page is cropped at both edges, which fits a zoomed page. The page that frames the table room sized itself to the zoomed viewport, the same fault as item 3. Fixed in talk.html; not yet confirmed on an iPad.

## Batch 2 — 2026-10-19 (Mark's own observations, divergent phase)
Source: Mark, from his iPad photos. Not sorted yet; Mark is collecting before any build starts.

| # | Part of product | What was observed | Sort | Status |
|---|---|---|---|---|
| 12 | Participant app: under the question box | Five small controls stack below the box (Leave for now, free tokens and Go deeper, This helped, Report a problem, Delete this conversation). Mark finds the visuals struggling and overwhelming. | Not sorted | Collecting |
| 13 | Participant app: visual load | Mark's view: the visuals are overwhelming overall. Conceptual items to follow from Mark. | Not sorted | Collecting |
| 14 | Selection and descriptions: scholarly voices | Mark's view: users want connection with the scholarly voices of each tradition, but those voices appear only late in a description. They should come first in every description, especially at selection (for example, "Alexandria was the first school; its voices of origin were ..."). Overlaps items 6 and 7. | Not sorted | Collecting |
| 15 | Representatives: who they stand for | Mark's view: keep Representative voices, but users do not know who a Representative is or has context for them. The Representative knows the real historical voices. It must be much clearer who the Representative is representing, not only which world. Overlaps item 14 and the safety/no-invention rules (no invented personal history). | Not sorted | Collecting |
| 16 | Product direction: what users come for | Mark's view: a Representative cannot be given an invented personal history, but users want the wisdom of the tradition's own voices, not a general account of a movement. Clarifies items 14 and 15; also bears on item 8 (answers that describe the group instead of answering). | Not sorted | Collecting |
| 17 | Church Family Tree to Table | Mark's view: users want to reach the multi-voice Table from the Church Family Tree. Today clicking a tradition on the tree opens a single conversation. An earlier attempt failed because choosing one tradition jumped straight to table selection; users want to click all three traditions on the tree first. | Not sorted | Collecting |
| 18 | Church Family Tree: audio | Mark's view: the Family Tree audios are too technical. Idea: voice the short intro at the top of the page as the opening voice, then let users continue to the deeper story. Any new audio is a paid bulk run, so the sample-first rule in CLAUDE.md applies. | Not sorted | Collecting |

## Clarification — 2026-10-19
- Item 18: Mark says the audio problem applies only to the 11 built worlds, because their stories are much longer and more complex.
| 19 | First engagement | Mark's view: what exists is strong but too complex and hard to enter for people with short attention spans. Wants a simpler, easier start that layers down into depth. Most people are less deep and less interested than Mark, so first engagements should be simple draws. Asks what other programs with this rigor do. Overlaps items 8, 12 and 13. | Not sorted | Collecting |
| 20 | Table conversation: rambling | Mark's view, reinforcing item 8: table voices ramble. When there is no direct answer they fall back to general, irrelevant statements out of a need to say something. Touches voice and answer behaviour; the no-invention and honest-limit rules must hold. | Not sorted | Collecting |
| 21 | Public site: landing page | Mark's view: the landing page needs to be much cleaner. Overlaps items 5, 13 and 19. | Not sorted | Collecting |
| 22 | Product direction: design principles | Mark's view: accessibility and polish matter. Engagement should come in layers, from simple (short, social-post style) down to deep research with access to the sources, with rigor, accessibility and cost held in balance. The feel: simple, discovery, layers of going deeper. Conversations easy to read, never dropping off the page, and no manual scrolling to start. Frames items 13, 19, 21; the scrolling point links to item 3. | Not sorted | Collecting |
| 23 | Product direction: start from the familiar | Mark's view: people want to see and engage with what they already know, and learn new things from there. Overlaps items 6, 7 (well-known figures at the table), 14 and 19. | Not sorted | Collecting |
| 24 | Design model: timed layers | Mark's idea, from speaker training: prepare each message at 1, 3, 5 and 10 to 15 minutes, built from modules and stories that are themed together. A possible model for the layers of engagement in items 19 and 22, and a link to the story repository (Doc_09). | Not sorted | Collecting |
| 25 | Audio: scope and cost | Mark's view: everything should be available as audio, but not through generated, paid-API audio for now. If funding comes, generated audio follows. Text is never given up. The three-level transparency stays. Exact reading to be confirmed with Mark (see item 18, which notes the paid bulk-run rule). | Not sorted | Collecting |

## Clarification — 2026-10-19
- Item 25: Mark says ElevenLabs is the fixed voice for all audio quality. Any generation still follows the paid bulk-run rule in CLAUDE.md (sample first, Mark approves by ear, settings passed explicitly and printed).
- Item 25 (further): Mark says funding exists for ElevenLabs audio of fixed text (stable content such as stories, descriptions and intros), and does not exist for audio of generated conversations. Audio of live conversation replies waits for funding; text always stays.

## Attribution correction — 2026-10-19
- Items 12 to 25 were logged as "Mark's view". Mark says many of them came from other users and he stated them as his own. Which items, and from how many users, is to be confirmed with Mark. Until then they are attributed "Mark, relaying users (to confirm)".
- Attribution (settled): items 12 to 25 are Mark's synthesis. They come out of discussions with users, with Mark's reading of what people were saying shaped into concrete ideas. They are recorded as "Mark, synthesis of user discussions". The raw user wording was not captured; when it is, it is added under the item.
| 26 | Product direction: overall experience | Mark's view: improve the experience overall. Simpler, connected to what people are looking for, and very professional: no amateur layouts, no overlays, nothing hard to make work. Frames items 12, 13, 19, 21, 22, 23. | Not sorted | Collecting |

## Decision — 2026-10-19
- Theme D (items 5, 12, 13, 19, 21, 22, 23, 24, 26): Mark converged. Record: Pilot_Feedback_Decisions.md. Nothing built.
- Correction (Mark, 2026-10-19): research round 1 for Theme D was a quick scan read as support for the draft, which is not how research is done here. Corrected in Pilot_Feedback_Decisions.md. Proper research is pending.
- Mark's first look (2026-10-19): likes the simplicity and scrolling of Google Arts and Culture and the simple selection of BibleProject. Idea: a rotating few on the first page, new each time, very clean. Recorded as an amendment to Theme D in Pilot_Feedback_Decisions.md; not research evidence.
- Coordination (Mark, 2026-10-19): the chooser thread owns the cards and landing order; this thread supplies inputs and stops editing index.html. See Pilot_Feedback_Decisions.md.
- Decision (2026-10-19): Theme B (items 8, 16, 20) converged by Mark. Record: Pilot_Feedback_Decisions.md. Nothing built or tested.
- Decision (2026-10-19): Theme C (items 6, 7, 14, 15, 16, 23) converged by Mark. Record: Pilot_Feedback_Decisions.md. Nothing built.
- Decision (2026-10-20): Theme E (item 17) converged by Mark. Change order: reverses the earlier ruling that kept tables off the tree. Record: Pilot_Feedback_Decisions.md. Nothing built.
- Thread ownership (Mark, 2026-10-20): working set is four threads; triage thread settles the 7 shared commits; Theme B engine work on hold. See Pilot_Feedback_Decisions.md.
- Decision (2026-10-20): Theme F (items 18, 25) converged by Mark. Record: Pilot_Feedback_Decisions.md. Nothing written, generated or spent.
- Decision (2026-10-20): Theme G (item 9, and the funding half of item 25) converged by Mark. Landing line: "Free to start. Add more any time." Record: Pilot_Feedback_Decisions.md. Nothing built.
- Change order (Mark, 2026-10-20): story teasers dropped from the landing page in favour of the chooser's spacing and card descriptions; "Tell us what you think" stays in the masthead. See Pilot_Feedback_Decisions.md.
- Clarification (Mark, 2026-10-20): the cards scroll and click to pull forward. Recorded under Theme E in Pilot_Feedback_Decisions.md.
- Status (2026-10-20): PR 987 merged into main (51cbfb4c). Landing page, names line, seating and scroll built. Open: free-tokens line, card text size, tree seat button, device checks. See Pilot_Feedback_Decisions.md.
- Item 27: Mark asks for a vertical scroll for people without a mouse wheel, on the landing page hand of cards.
- Item 28: Mark requires the landing page and cards to work on phones, iPads, laptops and desktop computers, with no exceptions.
- Decision (2026-10-20): Items 27 and 28 converged by Mark. Item 27 is a visible control that switches the hand to a plain top-to-bottom list on any device. Owner: the new landing page thread, with the step 4 device checks. Nothing built.
- Decision (2026-10-20): Mark rules that the landing page thread (session_01GSkmJBxTD77vXWGm6syanq, draft PR 1004) owns edits to the chooser code from now on: chooser.js, chooser.css and index.html. The Conversation chooser research thread builds nothing until Mark says. Reason: the landing thread's branch already changes those files.
- Correction (2026-10-20): the entry above that says the landing thread owns chooser code edits is withdrawn as a standing rule. Mark's role for the pilot-feedback thread is to track conflicts between build threads and answer ideas and questions, not to assign build ownership. Which thread builds what is Mark's call with those threads.

## Status update — 2026-10-20 (items 9 and 17, list control)
- Item 9 (Theme G): the landing line "Free to start. Add more any time." is built, under the hand.
- Item 17 (Theme E): only the button's wording is decided ("Add to the table"). The tree button, shared seat store and tree tray are not built; the tray's look and how long a seat is remembered are still open.
- A control that switches the hand to a top-to-bottom list on any device is built (Mark's item 27 as relayed; the log above stops at item 26). Record: `Build/Ministry/Features/Conversation-Chooser/Decision-Log.md`, 2026-10-20.
- Item 29 (Mark, 2026-10-20): the conversation pages are too chaotic and confusing. Mark wants a simpler layout showing only needed information, with the rest optional under "go deeper", plus the token and pay-as-you-go options. A new thread is to take this. Overlaps items 1, 2, 4, 9 and 12. Not sorted. Nothing built.
- Item 29, update 2026-10-21: the design was worked out in sketches with Mark, who converged, and it is built in cic-poc/frontend (one card or three above one conversation area, a token ribbon, a ⋯ menu, a book while the voice thinks, a smooth reveal and scroll). Record, change orders and open points: `Build/Ministry/Operations/Pilot-Feedback/Pilot_Feedback_Decisions.md`, "Item 29". Not yet on live.
- Status (2026-10-21): PR 1011 (CLAUDE.md 3.2 "Asking for any spend") merged into main at 2f0d54c5 after step 6 was restored to the approved wording. The branches `claude/claude-md-spend-step` and `claude/paid-run-gate` can be deleted; waiting on Mark's go-ahead.

## Records catch-up — 2026-10-21 (system and pilot feedback management thread)
Source: the 2026-10-21 handoff and what was read on main (bc2cde4d) in this session. Rulings marked "reported" came second-hand from the other pilot feedback manager and were not read at their source.
- Item 27 and the hand's scroll: the mouse wheel was removed from the hand on 2026-10-20 (checked: no wheel handler in `cic-website/assets/chooser.js` on main). This corrects the status entry that says a wheel handler is on main. The list control (item 27) is the way to scroll without a wheel.
- The open list of 2026-10-20 still carries the "Free to start. Add more any time." line and the card text size as not built or undecided. The line was built under the hand (entry of 2026-10-20, items 9 and 17). The card text size still has no ruling.
- Tree button wording (item 17): "Add to the table". Reported, not read at source.
- Reported rulings (Mark): one build thread at a time. Theme B's length and filler check only logs and never triggers a paid redo. The in-room AI note is one small light line at the foot (PR 1013, merged into main).
- CLAUDE.md: PR 1011 added the 3.2 "Asking for any spend" steps. Commit 1c29a6e6 later restored the 2026-10-17 version "at Mark's direction", so main's CLAUDE.md no longer has that section. The earlier entry that calls PR 1011 merged is true of the merge, not of the file today.
- Production (2026-10-21): the live app failed on every voice after promotion PR 1018 (Bedrock rejected API version 2026-10-21, sent by anthropic 2.0.0). The SDK is capped below 2 (PR 1020) and promoted (PR 1021). Whether voices work on the capped build was not tested by this thread. Open: the phone still showed the old version (cause not found); daily-limit counts to clear by restarting `cic-engine`; unpinned `boto3`, `fastapi`, `uvicorn`, `pydantic`, `httpx` and `pyyaml` can break a rebuild the same way.
- New work Mark has asked for, no design yet, nothing built: coupons and exceptions for particular people; pay as you go.

## Item 30 — conversation page text feels small — 2026-10-22
Mark: the text on the conversation intro and on the "Get more conversations" ribbon feels small. Sizes read in `cic-poc/frontend/src/app.css` on main (16 px base assumed; not checked on a device or at phone widths): intro `.turn--welcome` 0.95rem (about 15 px, muted grey); ribbon count and button 0.875rem (about 14 px, gold); body text 1.0625rem (about 17 px). Passed to the conversation pages thread (session_01RnnjAQrYFWSzjZiPnWuYke, branch claude/magical-goodall-ucv6e2) as Mark's request on 2026-10-22. No sizes chosen by Mark; a fix floated (intro at body size in the normal text colour, ribbon about 16 px) is not decided. Not sorted. Nothing built here.
- Also 2026-10-22: PR 1025 merged (coupon decisions). Mark's environment network access set to Full; blocked research hosts then reachable (checked from this session). Mark is waiting to see whether PR and merge blocks recur; a `.claude/settings.json` allow-list addition was prepared as text, not applied (a session may not edit its own permissions).
- The accounts and presence project (account system with memory, tokens and coupons) is to be its own thread; a launch prompt was drafted in chat, not saved to the repo.

## Daily visitor limits removed — 2026-10-22 (daily-limits thread)
Built from the 2026-10-22 ruling in `Pilot_Feedback_Decisions.md` ("No daily reset on visitor limits"). Branch `claude/remove-daily-visitor-limits-2026-10-22`; draft PR, merged into main when green. Not promoted to live.
- Removed: the 5-conversation and 150-message daily counts, the daily Facilitator-only sitting, and the paid sitting that existed only for them (`engine/api/anon_cap.py`, `deeper_admission.py`, `engine/m4/grants.py`, `turn.py`, `round.py`, `app.py`, `config.py`). The Render variables `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` are no longer read; they can be deleted in the dashboard.
- Kept: the visitor cookie and `CIC_API_ANON_CAP_ENABLED`, `group_daily_ceiling`, the door and `daily_share`, admin and tester caps, the per-minute burst limits, the 3-round free cap, the paid round cap of 40, and the per-message safety check.
- A conversation no longer counts when created, so a failed first voice reply costs nothing (new test).
- Go Deeper page sentence "each day has a free allowance": not found on `cic-website/go-deeper.html` on main; it already says the allowance is monthly.
- Open, Mark's words: `cic-website/privacy.html` still says "5 new conversations and 150 messages per visitor each day". Draft shown as an Artifact; not applied. Promote the page change with the engine change.
- Open, noted for Mark: dropping the cookie now gives a fresh free allowance, held back only by the per-minute burst limits and the door's weekly ceiling. The old daily count bounded that rate. Not a regression of the requirement, but a change in what limits a repeat visitor.
- Scope change from Mark (2026-10-22, via the system and pilot feedback thread): this thread did Job 1 only. Accounts research and design belong to session_01MVjZWWg11yP99Xqsna8nQ3.

## Status — 2026-10-22 (afternoon)
Sources: the PR pages on GitHub (read 2026-10-22) and reports from other threads, which are marked as reported.
- Item 30 (conversation text feels small): resolved on main by PR 1031 (https://github.com/mchadwick25-droid/CIC-Project/pull/1031), merged. Mark chose "Intro 17, ribbon 16" in the conversation pages thread. Welcome line 17 px in the normal text colour; ribbon count and "Get more conversations" 16 px. Reported by that thread: ribbon stays one row at 320, 360, 390 and 820 px; not checked on a real phone or iPad. Not yet on live.
- No daily reset on visitor limits: built and merged into main by PR 1032 (https://github.com/mchadwick25-droid/CIC-Project/pull/1032), by the thread session_014kMdzhac3pg4njANzhBJ2m. Reported in the PR: daily counts and the daily Facilitator-only sitting removed; a conversation no longer counts if its first voice reply fails; cookie, group ceiling, door, operator caps, per-minute limits and per-conversation caps kept; engine suites pass (1,982 with Go Deeper off, 842 with it on). Not in the PR: `cic-website/privacy.html` still describes the daily limit and waits on Mark's words; the two Render variables `CIC_API_ANON_DAILY_SESSION_LIMIT` and `CIC_API_ANON_DAILY_TURN_LIMIT` are no longer read and Mark can delete them in the dashboard. Not yet on live.
- Accounts: design merged earlier (PR 1027). PR 1033 (https://github.com/mchadwick25-droid/CIC-Project/pull/1033), draft, adds slice A1a (account store, typed-code sign-in, sessions, recovery, deletion) behind `CIC_ACCOUNTS_ENABLED`; cannot be switched on in production, no mail provider chosen; Opus attack-surface review and a security review still to do. Coupon button: Mark answered in the accounts thread that the design decisions were made and he wants it seamless, no copy and paste and no emails from him; recorded there as ruling 24 (reported). See the correction in Pilot_Feedback_Decisions.md.
- Promotion PR 1034 (https://github.com/mchadwick25-droid/CIC-Project/pull/1034) from main to live is open and waits on Mark. The PR says three runbook gates are not done: staging check (Mark reports the staging service does not load), the admission gate (11 failures, one per world, possibly a sandbox artefact, no approved run), and five hand-set secrets in Render not confirmed (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `CIC_API_ANON_VISITOR_SECRET`, `CIC_DEEPER_FREE_KEY`, `CIC_DEEPER_WEBHOOK_SECRET`). Mark also reads the `render.yaml` and `engine/api` diffs before merging. This thread has not read the diffs.
- The $12 weekly door: the base is already $12 and enforcing on live (`engine/deeper/ops/go-deeper.yaml` on `origin/live`, read 2026-10-22). The earlier status that it awaited promotion was out of date.
- Environment: Mark set Network access to Full; blocked research hosts then loaded from this session.
- Other threads (their own reports, not checked): Church Family Tree navigation, option A not merged; conversation chooser research, branch reset with no new PR; Library Eras VII and VIII, branches pushed, paused.
- Still open: a decision on the admission gate; whether voices work on the capped build; the phone showing the old version; Render Auto-Deploy and the `cic-engine` restart; deleting `claude/paid-run-gate` and `claude/claude-md-spend-step` on GitHub; unpinned `boto3`, `fastapi`, `uvicorn`, `pydantic`, `httpx` and `pyyaml`; the `.claude/settings.json` allow-list addition (prepared as text, not applied).

## Participant-experience design thread — 2026-10-23
Source: the design thread itself (session_012jjhAokk8iJ5PiFZ3Tn15r), commissioned 2026-10-22. Design only; nothing built, no site or engine file changed.
- Three design canvases, each worked through with Mark one decision at a time, every new participant-facing line approved by him as written: the room without an account (https://claude.ai/artifact/3DjRnJLekCqDXNs8ej7iyf), the buy page (https://claude.ai/artifact/4Qf4Ms81C147gChMerfdnQ), the optional account (https://claude.ai/artifact/PXwNUfLjJsWxeZ53zWgMcq).
- Mark's choices in the thread: the stop as ruled (Facilitator line, panel from the bottom on a phone, beside on desktop); the buy page opens in the same tab everywhere and returns to the same conversation; packs first on the Go Deeper page; the 18-or-over line as a sentence under the packs; sign-in invited in the panel's account section and one ⋯ menu line only; counts described in tokens, in his words "550 free tokens every 30 days. 50 to launch a new conversation, 20 to 25 for each question".
- The 2026-10-22 change order removing the free 3-round rule reached the thread mid-design and was applied: no screen or line says three rounds.
- Opus 5.5 review: 26 findings in round one, two new blocking in round two from the fixes, round three clear. Open for Mark (six items) in the handoff: Build/Ministry/Operations/Handoffs/2026-10-23_participant-experience-design.md.
- Not done: the second pass (13-to-17 and groups) waits on Mark's approval of the first; Google, Apple and passkey screens out of scope; a list of built-word states not drawn is in the handoff.
