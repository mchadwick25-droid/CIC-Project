# Opus review: Question-Coverage work (branch claude/question-coverage-2026-10-26)

Reviewer: Opus, independent. Date: 2026-10-26. Read-only. No model calls, no network, nothing in the repo edited. Checks were greps, line reads and one small quote-matching script, run in the scratchpad.

## Verdict

1. The work is useful and mostly accurate. Of 38 factual claims I checked, 26 held, 7 held only in part, and 5 failed. All 6 quotes I re-verified match.
2. The core finding stands: many good, mapped texts have no record. The Cappadocian silence on hell is the clearest case. It is real.
3. The headline number overstates that lever. "Loaded" counts opponent voices, outside historians and wrong authors in shared volumes. The tool ignores the corpus-map role, and the summary folds hostile "L-" cells into "loaded".
4. Two failures would put words in the wrong mouth. One is an Origen letter filed as Jerome's own renunciation. The other calls Fabiola's husband "violent", which the source does not say.
5. The acquisition and commentary scores are inflated. Out-of-window, out-of-place and opponent works earn full points. Unbuilt worlds count every cell as open.
6. Three findings are overstated: the privacy-page "mismatch", the "contradicted" Syriac and Reformed limits, and the Wittenberg free-will term.
7. Safety is handled with care in the prose. But 69 Facilitator-adjacent record rows invite build threads to write material for the turns right after a crisis. They should wait for a Facilitator-governance ruling.
8. One governance risk is real. The Library launch prompt asks for per-sub-question coverage in every Doc_02, yet says nothing in the remit changes. That is a method change. It needs a change order.
9. The Chrysostom mapping makes Antioch's sermons the voice of Rome, Milan and Constantinople. Mark should look at it again before it is applied.
10. Do this before any thread acts: correct the five failures, re-run "loaded" with a role filter, and get real visitor questions in.

## Accuracy spot-check

Result key: HOLD, PARTIAL (true but overstated or mis-cited), FAIL.

| # | Claim (where) | Result | Evidence |
|---|---|---|---|
| 1 | `desert.limit.tithe` is contradicted by Cassian Conf. XXI (summary 5) | HOLD | npnf211 Conf. XXI ch. III "Of the offering of tithes and firstfruits" (~44592). The Conferences are mapped to desert as `tradition` (desert-monasticism.yaml row 120). The limit only searched the Vita and Palladius. |
| 2 | `desert.limit.f2-scripture-detail` is contradicted by Conf. X (summary 5) | HOLD | Conf. X begins at npnf211 35878. The Sarapion anthropomorphite story is a reading of Genesis 1:26. |
| 3 | `rzg.limit.no-teaching-on-wealth-or-marriage` is "true of the records, not the library" (summary 5) | PARTIAL | The statement already says "Our teachers did write on both, but we cannot yet give you that teaching here." Only `why_sources_cannot_answer` ("none is available to draw on now") is wrong. It is a fix, not a contradiction. |
| 4 | `syr.limit.marriage` says no text speaks to Christian marriage (summary 5) | PARTIAL | The limit says no in-window text describes it "in any detail". It already cites Bardaisan. anf08 68980-68984 gives one sentence on Edessene Christians who "withdraw" from an unchaste wife. That defeats the limit's "not a description of Christian practice" clause. It does not defeat the limit. |
| 5 | `witt.term.free-will` is wrong; Formula of Concord XI at Book of Concord line 25390 (C4, summary 5) | PARTIAL | FC is vendored. But line 25390 is a table-of-contents heading; the article text is near 27593 and 34493. FC (1577) lies past the term's own `years: 1520-1545`. The world core says later years "reach us only through the later book". Whether FC speaks in this voice is a world decision, not drift. |
| 6 | `witt.source.book-of-concord` is marked unvendored while Jacobs 1911 is vendored and mapped | HOLD | Source record says "NOT VENDORED"; corpus map row 55 maps Jacobs 1911 as `tradition`. |
| 7 | No cappadocian record mentions hell or judgment (C3) | HOLD | Grep for hell, gehenna, eternal punishment, last judgment, apokatastasis over non-source records: zero. |
| 8 | Nazianzen Or. 40.23 "neither glorified nor punished" at npnf207 ~38494 | HOLD | Lines 38492-38494. |
| 9 | Nyssa Cat. Or. 26 at npnf205 44408-44422 | HOLD | "restoration of those who are now lying in Sin ... purgation". |
| 10 | On Infants' Early Deaths at npnf205 32849 | HOLD | Heading at 32849. |
| 11 | Basil's Rules on eternal punishment at 7722, vendored and mapped | HOLD | "to eternal punishment ... the fire is not quenched"; file mapped in cappadocian yaml. |
| 12 | Circumcellions "throw themselves over precipices" at npnf104 16889 | HOLD | Line 16888-16890, framed as "friends of the devil ... learned to kill themselves". |
| 13 | City of God I.17 on suicide at npnf102 2426 | HOLD | Chapter 17 heading at 2426. |
| 14 | Cyprian's reunion passage at anf05 47279 | HOLD | "a dense crowd of parents, brothers, children". |
| 15 | Justin Dial. 5 "the soul is not in its own nature immortal" at anf01 17704 | HOLD | Chapter heading 17704-17707. |
| 16 | Jerome Ep. 39 "mourn ... only for him whom Gehenna receives" at npnf206 7903 | HOLD | Lines 7903-7905. |
| 17 | Jerome Ep. 42 on the sin against the Holy Ghost at npnf206 8389 | HOLD | Lines 8386-8390. |
| 18 | "The Apology against Rufinus renunciation ('the devil will be saved; a thing which no man ... could say', npnf203 53776)" as Jerome's own words for hal (C3; records-by-world hal row "C3 must add") | FAIL | The sentence is Origen's letter to friends, which Jerome quotes and compares with Rufinus's version (53740-53779: "the later words of Origen which I have translated"). The "I" is Origen. A hal quote record built on this row would misattribute. |
| 19 | `hal.quote.she-put-on-sackcloth`: "a woman who left a violent husband" (C14 line 78; summary 6 and 9; records-by-world hal fix row) | FAIL | Ep. 77.3 (npnf206 17395-17430) names faults "not even a prostitute or a common slave could have put up with" and an "incontinent husband". No violence. The record quotes sec. 4 on penance. C8 had it right ("vices a whole neighbourhood knew"); C14 and the summary drifted. This sits on Facilitator ground. |
| 20 | lpc: "330 records", all draft, no use_note, nothing on hell; package inclusion "not checked" | PARTIAL | 360 records (210 source, 150 other). All draft, none with use_note, no hell or judgment record: HOLD. And `packages/` has no lpc folder, so no lpc record reaches a participant. That was one `ls` away. |
| 21 | The Library holds no Jewish voice (no Josephus, Philo, rabbinic text) | HOLD | No such file in `cic/texts/` (the Trypho text is Justin's). |
| 22 | `hal.story.oea-gourd`: "whether from ignorance or spite" (Ep. 71.5, line 32546) and "guard fails" | PARTIAL | Text and line hold (npnf101 32540-32550). But the `telling` adds "as Augustine reports it" and `absent_detail` names the hearsay layers. A not_for line is still worth adding. "Fails" is too strong. |
| 23 | `witt.term.the-turk` world_word files Jews with the Turk as the devil's instruments; not_for covers only the political reading | HOLD | Line 52 and not_for lines 72-75. |
| 24 | alx: no devil, demon, miracle, angel or saint record in 179 | HOLD | 179 files; hits are incidental. One quote (`alx.quote.the-grades-here-in-the-church`) reads church order as an angelic copy, which is close but not about angels. |
| 25 | `desert.story.antony-tomb-combat` reads the beast-demons as a "chosen register for interior struggle" | HOLD | absent_detail line 55. |
| 26 | `cappadocian.term.martys-martyrion` not_for says the world "denied" worship of martyrs | HOLD | not_for line 75. |
| 27 | Zwingli vol. 3 line 1523 "unbaptized infants are not under condemnation" is the editor's paraphrase | HOLD | Lines 1519-1526 are the editor's summary. |
| 28 | Only one of nine "what are you" questions matches `_SYSTEM_NATURE_SHAPE` | HOLD | I ran the regex from `engine/m5/routing.py` 56-62 on all nine. Only C16-12 matches. "Are you real" and "Are you an AI" match. |
| 29 | `SYSTEM_NATURE` text at `engine/m4/facilitator_turns.py` 64-76 | HOLD | Text as quoted. |
| 30 | Privacy page has "two back-to-back cookie paragraphs" (summary 8, C16) | FAIL | The two-jobs paragraph is `hidden`. `cic-website/assets/privacy-go-deeper.js` swaps them when Go Deeper is on. It is a feature flag, not a defect. |
| 31 | Privacy page says the review copy is deleted while the code keeps its scores; handoff says the page "overstates deletion" | PARTIAL | `qc_store.py` clears question and answer text at 90 days and keeps marks, scores, routing and flags under a keyed hash. The page says the copy "of questions and replies" is deleted, which is true. Not saying that scores stay is a disclosure gap, not an overstatement. |
| 32 | `SourceList.tsx` never prints `edition`; edition is None when a source has a `citation` | HOLD | `edition` appears only in `types/conversation.ts`; `citation_cards.py` ~167 sets `"edition": None`. |
| 33 | rzg has no record on justification by faith | HOLD | "justif" occurs only as `narrative_tier_justification` and in a craft note. |
| 34 | Servetus is named in rzg only in a parenthesis | HOLD (fact) | `rzg.force.counter-reformation-sustained-pressure` line 24 says Servetus is "scoped to a different registered world and not treated here". The worklist asks for a Servetus record without naming that scoping. It is a cross-world decision. |
| 35 | Didascalia Apostolorum is the top acquisition at 11 cells (alx, pahc, syr) | FAIL | The Didascalia is Syrian, c. 230. pahc's window ends at 200 (five cells). alx is Egypt (one cell). Only syr's five cells fit. |
| 36 | Erasmus's Paraphrases rank first for Eras 7-10 at 143 (hus 53, jes 53, rzg 28, witt 9) | FAIL | The survey's own caveat says hus ends in 1517, before the Paraphrases. Erasmus is not a Reformed, Lutheran or Jesuit own voice. The score counts cells his text cannot fill in those worlds' voices. |
| 37 | `pahc.quote.appointed-to-be-read` quotes Athanasius's 367 letter in a 70-200 world | HOLD | True, though the record discloses it itself (line 16). |
| 38 | `gallic.term.predestination` "can be read as universalism" and is unguarded | PARTIAL | The term itself quotes "Those then who perish, perish against His will." The risk is small. |

Quotes I re-verified against the vendored file (verbatim, allowing only line-end hyphens and editorial markup):

| Quote record | Result |
|---|---|
| `hal.quote.she-put-on-sackcloth` (npnf206 ~17449) | MATCH |
| `desert.quote.moses-sins-run-out` (Budge v2 line 1160) | MATCH |
| `gallic.quote.salvian-free-men-in-seeming-captivity` (Sanford 1930 lines 6457-6459, split "seem- ing") | MATCH. This closes the summary's open "lead, not a verification". |
| `pahc.quote.two-female-slaves-who-were-called-deaconesses` (npnf201 19502-19506) | MATCH, but inside an NPNF editor's endnote quoting Pliny, as the report says |
| `cappadocian.quote.ousia-and-hypostasis` (npnf208) | MATCH |
| `alx.quote.dionysius-too-high-for-me-to-grasp` (npnf201) | MATCH at clause level |

Totals: 38 claims (26 HOLD, 7 PARTIAL, 5 FAIL) plus 6 quotes (6 MATCH). Four of the five failures are in reports finished on Sonnet or in the worklists built from them.

## Method

**The layering is sound in shape.** RENDERED, LOADED, IDENTIFIED, OTHER and NOTHING are the right questions in the right order. They separate "the voice can say it" from "the Library could let it say it" from "we must acquire".

**LOADED is not role-aware.** The corpus map gives every work a role: `tradition` (own voice), `context` (outside view or contemporary opponent), `antecedent`, `transmission` (custody, not voice). `Tools/coverage_search.py` reads `source_file` and ignores `role`. It also scans whole files, so shared volumes count for the wrong author. The reports catch some of this by hand. C4 marks L- for "hostile or outsider" cells. C3 warns that npnf207 holds Cyril, not only Nazianzen. But the summary then counts "L, L-, L-T" together as "loaded only". So the 299 cells (21.5 percent) mix three different things:
- own-voice text with no record (the real, cheap gap);
- an opponent's or outsider's voice (Augustine and Optatus for don; Rilliet for rzg; Ammianus for ijc), which can feed a contested_claim but never the world's "we";
- the wrong author in a shared volume. Failure 18 shows where that leads: an Origen letter offered as Jerome's.

The don figures show the scale. Its map has 24 tradition rows, 25 context and 8 antecedent. So don's "loaded" cells lean hard on its opponents.

**Existing tools were not used.** The build process already has `python -m engine.m9.cli holdings <code>` and `shelf`, which report per world whether a file is in scope, named, drawn on or "in scope, unread", and they carry the role. CLAUDE.md also names the CORPUS-USE.md tier method. A new search tool was built beside them instead. Re-running "loaded" through the shelf and holdings would split it by role at once.

**Sub-question groupings hide real differences.** Some groupings join questions with different answers and different safety weight. C3.S7 puts "outsiders" with "unbaptised infants" and "suicide". C3.S5 puts "purgatory" with "ghosts" and "reincarnation". C2.S2 puts "father or judge" with "the same God as Jews and Muslims" and "anger at God". A cell marked R for one facet reads as covered for all. R* is used for at least four different states ("limit", "partial", "guard only", "draft only"), so the 316 limit-or-partial cells cannot be read as one thing. C15 counts 240 wordings while the others count cells, and the summary adds them into one total of 1,632.

**Tradition versus context, and window.** The method assumes a mapped text is the world's to speak. It does not test window and place per passage. Examples: Didascalia for pahc, Formula of Concord for a 1520-45 term, Jerome's Ep. XV written before hal's window (the worklist notes this one), Erasmus for hus and jes. The voice rule needs a per-row test: own voice, in window, in place. Otherwise the row is context, and it goes to a contested_claim or a Facilitator note.

**Evidence trail.** The JSON files use a different schema per cluster. They cite `search/<C>/` paths that are not in the repo. The summary names `*-4cluster.*` files that are not saved. So the counts cannot be re-derived from the folder, though the tool can be re-run.

## Fit with CLAUDE.md

**Never invent.** The prose is careful and says plainly what was not read. The risk sits in the worklists, which a build thread will treat as instructions:
- Failure 18 would create a misattributed quote.
- Failure 19 puts an invented detail ("violent") on a record cleared for warmth after a crisis redirect.
- Several "must add" rows rest on lines read through a grep window, not in context.

**Contradicted limits.** Two hold (desert tithe, desert Genesis). Three are overstated (rzg, syr, witt). Calling them "contradicted" pushes a world from honest silence to a claim it may not own. That is the overstatement the project guards against. The fix for each is to narrow the wording, and the reports partly say so. But "contradicted" will travel further than "narrow".

**Safety and the Facilitator.** The prose keeps the boundary: FAC questions list "what a voice can say truthfully after the template-anchored redirect", and the battered-wife material is "history, never counsel". Three concerns:
- The FAC flag joins distress and system-nature. These are different routes. System-nature is not a safety event.
- The records worklist marks 69 rows FAC and proposes records (infant death, suicide, despair, a husband's violence). Building records meant for the turn after a crisis is a Facilitator-governance question under `CiC_L3D_Facilitator_Governance_V3.6`. It is not a world-build task. The rows should be held until Mark rules.
- The Circumcellion text (npnf104 16889) is a real hazard for a suicide-bereaved visitor. That was found and is the right priority.

**Generic voice.** C15 proposes one honest-limit frame for all worlds, with slots such as "{Fight} had not been invented in {window}". Filled the same way in twelve worlds, that produces the uniform voice CLAUDE.md names as a fabrication risk. The hedge must be emic: each world's own way of naming its silence. The ready list of `records-by-world` honest_limits (197 `no_text` rows, many of them "faith alone", "indulgences" or "Muslims out of window" for each patristic world) multiplies that risk. It also invites the voice to raise anachronistic frames nobody asked about.

**Quiet governance change.** README and Decision-Log say no method change is proposed. But the Library launch prompt tells the Library thread to build every world's Doc_02 so that "for each sub-question ... the registry should say what the world's vendored and identified sources can and cannot support". The Doc_02 spec in `CiC_Record_Native_World_Build_Process_V2.0.md` (line 417) holds no such duty. The prompt also says "Nothing in your remit changes with this task". That is the quiet change Mark told the thread not to make. It needs a change order with old and new text.

**Ownership conflict.** The launch prompt says the Library does "not touch ... world records". Then its item 2 says to fix registry drift such as `witt.source.book-of-concord`, which is a world record under `records/witt/source/`. The corpus-map half is the Library's. The source-record half is the world thread's.

**Placement.** Everything is under `Build/Ministry/Features/Question-Coverage/`; `git diff origin/main...HEAD` touches nothing else. That is correct for notes and worklists. Small issues: `Repository/00-frame.yaml` still says "Draft in scratchpad; not a repo file". Three scripts (`coverage_search.py`, `render.py`, `build_worklists.py`) live in a notes folder. CLAUDE.md's pattern puts code in `Sandbox/` and support material in `Build/Ministry/Features/`, not the reverse. Neither is a live-surface breach.

**The Chrysostom proposal.** See the recommendations table. The thread itself flagged the role problem, which is to its credit.

**Cost.** The handoff says about half the week's allowance went to this design work. CLAUDE.md says at least half goes to building. The worklists, if run as written, imply hundreds of Opus-rendered quote records. Each needs a verbatim check, an Opus rendering, an independent Opus check and review rounds. Non-English sources need an Opus translation from the original (build process line 836). The worklists do not price this.

## Recommendations assessed

| Recommendation (where) | Justified? | Priority right? | Cost proportionate? | What I would do instead |
|---|---|---|---|---|
| (a) Closing LOADED-to-RENDERED is the main lever; "costs quote records and renderings, not source research" (summary 1) | Partly. True for own-voice, in-window rows. Not for opponent, context or wrong-author rows inside the 299. | Right lever, wrong size. | No. Each quote costs Opus rendering, an Opus check and review. 343 rows is weeks of build. | Re-run with a role, window and author filter. Then rank by real visitor frequency and harm. Start with the few high-stakes cells: the Cappadocian afterlife texts, the lpc afterlife texts (when lpc builds), Perpetua's Dinocrates, and the guards. |
| Canon does not force demonstrations per world (summary 2) | Yes as a finding. | Medium. | It implies a method change. | Send it to Mark as an observation. Any fix is a change order. |
| Fleet-wide holes by sub-question (summary 3) | Mostly, subject to the grouping caveats. | OK. | n/a | Treat it as a map, not a to-do list. |
| Four worst worlds: rzg, ijc, lpc, don (summary 4) | rzg yes. lpc is unpackaged and in build, so it is not participant-facing. don's "loaded" is mostly opponent text. | rzg first is right. | Medium. | rzg: justification, Trinity, Institutes on the afterlife, from its own voice. don: contested_claims and limits, not witnesses. |
| Narrow five contradicted limits (summary 5) | Two yes, three overstated. | High for the two. | Small. | Fix desert tithe and desert Genesis now. For rzg, change only the `why_sources` line. For syr, fix the "not Christian practice" clause. For witt, the world thread decides whether FC speaks in its voice. |
| Jewish-visitor guards (summary 6) | Yes. witt.term.the-turk is the clearest. | High. | Small. | Add not_for lines in witt and alx. Treat oea-gourd as a light touch. The Library gap (no Jewish voice) is real; Josephus (Whiston, PD) is the cheapest fix. |
| Suicide text unframed in don and lpc (summary 6) | Yes. | Highest among content items. | Small. | A guard on the don records that could retrieve it, plus a Facilitator-side check. No new Representative content. |
| (d) Eight of nine "what are you" questions fall through (summary 8, C16) | The regex result is correct. Not every fall-through is a defect: "Are you making this up?" can be answered well in voice. C16-20 (who is behind this) and C16-26 (is this private) are true gaps. | Medium-high for privacy. | Small engineering, but it is a Facilitator-governance change. | Mark rules on two new shapes (privacy, who is behind this) through the Facilitator governance doc. Leave in-voice the questions that the records can answer honestly. |
| (d) Privacy page mismatches (summary 8) | One of three fails (cookie). One is overstated (scores). One holds (nothing in the app links to the policy). | Medium. | Small. | Add one line to the page saying scores and flags are kept without text. Add a privacy link inside the conversation app. Drop the cookie finding. |
| "Show me the page": edition never shown (C16) | Yes. | Medium. Students and pastors will ask. | Small engineering. | Show `edition` on the source card. |
| Facilitator-adjacent material by world (summary 9) | Accurate as inventory, except the Fabiola error. | Should not be a build priority. | n/a | Hold the 69 FAC rows until Mark rules under the governance doc. |
| (b) Acquisition list scored by cells unlocked (acquire.md) | The scoring ignores window, place and role, and unbuilt worlds count as all open. The Didascalia (#1) is inflated. | Several top rows are mis-ranked. Unbuilt worlds are under-counted in acquire.md (they were mapped only for C3) and over-counted in the commentary survey. | Downloads are cheap. Rights checks and Opus translation are not. | Score only own-voice, in-window cells. Score unbuilt worlds against their time window, not as "all open". Add a cost column: PD English, or original language needing Opus translation. Verify every rights claim before download. |
| Commentaries for every era, Origen on Romans first (commentaries-eras-*) | It serves pastors, as Mark asked. But Origen's Romans survives in Rufinus's abridged and adapted Latin, so it is weak as Origen's own voice. It also needs Opus translation. | The survey's own "biggest cheap win" (Chrysostom, already vendored) is a better first step. So are Calvin's vendored Genesis and Tyndale's prologues. | Large. | Do the vendored-and-unused commentaries first. Put Origen on Romans after them, and label it "Rufinus's Latin". Fix the Erasmus row. |
| (c) Chrysostom mapping: ijc `tradition`; hal, gallic, cappadocian `context` | Mark decided it. But most of these homilies (Matthew, John, 1 Corinthians, Ephesians and others) were preached at Antioch c. 386-397, before Constantinople. ijc's place is "Rome, Constantinople, Milan". There is an unbuilt Antiochene world named for Chrysostom. `context` is defined as the outside view, and the thread says Chrysostom is not that for the other three. | Before it is applied. | Small to apply, larger to undo. | Map to ijc as `tradition` only the series preached at Constantinople (for example Acts, Hebrews, Colossians, the Thessalonian letters), or map all of it as `context` for ijc. Add no context rows for hal, gallic and cappadocian. A pastor-facing passage index can reach Chrysostom without making him any world's "we". Mark re-decides by change order. |
| (e) Library builds Doc_02 around sub-question coverage (launch prompt) | The idea is good. Done as written, it is an unannounced method change. | Not first. | Medium per world. | Mark decides by change order. If yes, it should be a short appendix produced by the holdings tool, not a new registry duty. |
| Registry drift fixes (launch prompt item 2) | Yes, for the drift that holds (Book of Concord, Cassian De Incarnatione, Genevan Psalter and the others). | High and cheap. | Small. | Library fixes the corpus map. Each world thread fixes its own source records. Fix the prompt's contradiction. |
| (f) Sonnet finishing cluster reports from an earlier agent's saved runs | Mark asked for it to save allowance. The output shows the cost: four of my five failures come from that stage. C16's background runs were cut off. C13's runs had to be re-run. | n/a | Cheap then, costly if acted on unchecked. | A targeted Opus recheck of every "must add" quote row whose line sits in a shared volume, and of every FAC row. Not a full re-review. |
| Per-world gaps go to each Open_Gaps_Tracking.md through that world's thread (Decision-Log Open) | Yes, and required by CLAUDE.md. | After the corrections above. | Small. | Enter only rows that pass the role and window filter. |

## Gaps and risks

1. **Real questions.** About 15-18 real dashboard questions exist (Decision-Log, 25 October), and none were used. The repository's 465 wordings are predicted, or drawn from US and Protestant research. Everything is weighted to questions nobody has yet asked. A hostile critic would say the project measured its worlds against its own guesses.
2. **Opponent as witness.** A scholar would object first that "loaded" treats Augustine on the Donatists, or Rilliet on Servetus, as the Donatists' or Geneva's own ground. The method says so in places, but the totals do not.
3. **Shared volumes.** NPNF and ANF volumes hold several authors. A line number in a grep window is not an attribution. Failure 18 shows it happening.
4. **Facilitator ground.** A pastor would object to records written to be spoken right after a disclosure of abuse, suicide or infant death, whatever their accuracy. The texts the work found mostly counsel endurance (Monica, Basil, Chrysostom). The work says this. The worklist still lists them as rows.
5. **Overstatement through "contradicted".** The most likely way this work leads a build thread to overstate is a "contradicted limit" or a "must add" row taken at face value. The Wittenberg term would then claim a predestination doctrine from a 1577 text. The Syriac voice would describe Christian marriage from one Bardaisanite sentence.
6. **Invention through templates.** The most likely way it leads to invention is the C15 honest-limit template filled across twelve worlds. The result is generic hedges in a uniform voice, which are fabrications of a world's voice.
7. **Not checked by the work, and cheap to check:** lpc packaging (none exists); window per passage; role per file; cross-world scoping notes (Servetus).
8. **Research review.** The Opus research review depends on press coverage for several figures, and dates two sources to 2025-26. I could not check them. The handoff flags this correctly.
9. **Cost.** No row in any worklist carries a build-cost estimate.

## Top ten next steps

| # | Step | Owner | Cost | What it unlocks |
|---|---|---|---|---|
| 1 | Correct the five failures in the folder: Origen and Jerome (C3, hal worklist row); Fabiola "violent" (C14, summary, hal fix row); cookie paragraph (C16, summary, handoff); Didascalia and Erasmus scores. Mark the rzg, syr and witt "contradicted" items as "narrow", not "contradicted". | Design thread (Sonnet edit, Opus check of the changed lines) | Small; no download; no metered call | Stops threads from acting on wrong rows. |
| 2 | Put the real dashboard questions into the repository as REAL. Re-weight the clusters by what people actually asked. | Mark pastes; design thread enters | Small | The true priority order. |
| 3 | Rule on the Library launch prompt: strike or change-order the Doc_02 sub-question duty, and fix the world-records contradiction. Send the Library session the correction. | Mark | Small | Keeps the method change visible and owned. |
| 4 | Re-decide the Chrysostom mapping before it is applied: ijc `tradition` only for the Constantinople series, or `context`; no context rows for hal, gallic, cappadocian. | Mark, then Library | Small; no download | A clean voice rule, and the Antiochene world kept intact. |
| 5 | Re-run "loaded" with role, window and author filters, using `engine/m9` shelf and holdings. Split LOADED into own-voice and outside-voice. | Design or Library thread, script (Haiku/Sonnet) | Medium; no download; no metered call | An honest size for the lever; a usable records worklist. |
| 6 | Safety-adjacent guards now: don records near the Circumcellion charge, `witt.term.the-turk`, `alx.quote.clement-schoolmaster`. Hold the 69 FAC rows until Mark rules under Facilitator Governance V3.6. | World threads; Mark for the FAC hold | Small | Removes the most harmful failure paths first. |
| 7 | Narrow the two limits that are truly contradicted (`desert.limit.tithe`, `desert.limit.f2-scripture-detail`) and the single wrong clauses in rzg and syr. Log each in that world's `Open_Gaps_Tracking.md`. | desert, rzg, syr threads | Small | The voice stops denying what its own library holds. |
| 8 | Registry drift: Library fixes the corpus-map side; world threads fix the source records (Book of Concord, Cassian De Incarnatione, Genevan Psalter, Acta Saturnini, Basil liturgy). | Library and world threads (Haiku for mechanical edits) | Small; no download | Correct "vendored" flags. Some rows move from IDENTIFIED to LOADED. |
| 9 | Product: show `edition` on source cards; add one privacy line about kept scores and a privacy link in the app; Mark rules on two new system-nature shapes (privacy, who is behind this) through the Facilitator governance doc. | Engineering; Mark for the routing rule | Small engineering | Honest answers to "show me the page" and "is this private". |
| 10 | Re-score acquisitions and commentaries on own-voice, in-window cells, with a translation-cost column. Do the vendored-and-unused commentaries first (Chrysostom by passage, Calvin's Genesis, Tyndale's prologues), then Josephus (Whiston), then Origen on Romans labelled as Rufinus. Verify rights before any download. | Library | Medium; downloads; non-English texts later need Opus rendering, which counts against allowance, not metered spend | An acquisition list that serves the voice rule and the budget. |

## What I could not check

- The web sources in the research review (Pew, PRRI, Barna and others): no network.
- Rights and hosts in the acquisition and commentary lists: no network. I did not test any licence claim.
- The reader classifier: not run, by rule. Fall-through is judged from the regex, as the work did.
- `canon/sealed_probes/`: not opened, by rule.
- Non-English vendored texts: not read.
- The count tables (1,392 cells and so on): not re-derived. The raw `search/` runs are not in the repo.
- Readability of any spoken field: not graded.
- Clusters C1, C2, C5, C6, C7, C9, C10 and C12 were read only where a claim led to them.
