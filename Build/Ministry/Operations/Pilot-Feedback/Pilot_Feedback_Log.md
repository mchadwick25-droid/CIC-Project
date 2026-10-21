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
- Decision (Mark, 2026-10-21): the admission gate is waived for promoting the item 29 conversation pages to live. Reason (Mark): this is a layout upgrade, not an engine change. Checked this session: `python -m engine.m3.admission_conform --enforce` fails for all 11 worlds (no live admission report for the current packages), and `live` is 340 commits behind `main`, so a promotion of `main` also ships the engine and record changes merged since the last one. Mark chose to waive with that stated. The step-by-step promotion (staging look, hand-set secrets, the promotion PR) is still his, through `CiC_Promotion_Runbook.md`. Nothing spent, nothing promoted. Not yet logged in the System Hub Decision Log.
- Status (2026-10-21): PR 1011 (CLAUDE.md 3.2 "Asking for any spend") merged into main at 2f0d54c5 after step 6 was restored to the approved wording. The branches `claude/claude-md-spend-step` and `claude/paid-run-gate` can be deleted; waiting on Mark's go-ahead.
