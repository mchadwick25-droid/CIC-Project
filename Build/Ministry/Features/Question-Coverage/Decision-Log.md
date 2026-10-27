# Question-Coverage — Decision Log

Newest last. Decisions are Mark's unless marked as a finding.

## 2026-10-25 — Worked example first
Mark chose hell and salvation after death as the worked example before a wider sample of real visitor questions. Finding: the Question Canon holds one hell question (F6-T, "are people like me going to hell?") and nothing on whether hell ends, restoration, annihilation or the state after death.

## 2026-10-25 — Build the question repository first, from the visitor's side
Mark: stop, identify all the questions first, then search; the repository is for different kinds of users and the kinds of questions they would likely ask, from the point of view of those who use the system. The real visitor sample is thin (about 15 to 18 dashboard questions); the repository says so and is built to take real questions as they arrive.

## 2026-10-25 — Twelve visitor kinds accepted as the working frame
Alternatives offered: merge to the curriculum's four plus the grieving; reframe by the visitor's denomination. Mark accepted the twelve.

## 2026-10-25 — Opus research review, all additions accepted
Mark asked for an Opus review of the repository against what major research groups report people struggle with, without stereotyping. Accepted: 40 sourced additions tagged RESEARCH with the study named, the voice-note corrections for the leaver, skeptic, churchgoer, other-faith, pastor and grieving kinds, and the Hindu-visitor rewording. Known limits written into the repository: mostly US, Protestant and ministry-commissioned; nothing found on students, history lovers or Orthodox and Global South visitors. One widely cited UK study (Bible Society, The Quiet Revival, 2025) was withdrawn in March 2026 and is not used.

## 2026-10-25 — System challenges split out of the content clusters
Mark: remove questions that try to pull the Representative out of character and put them under challenging the system. New cluster C17. Eleven items moved with their birth ids kept; sixteen added (existing boundary probes plus predicted).

## 2026-10-25 — Variants kept as wordings, not counted as questions
Three levels: sub-question (the coverage unit), canonical question, wordings. 465 items folded into 129 sub-questions.

## 2026-10-25 — Search every cluster; map before closing gaps
Mark chose to map the remaining twelve clusters before starting to close gaps. Finding (all sixteen): loaded-not-rendered is the dominant gap; see `Coverage-Maps/00-summary-all.md`.

## 2026-10-25 — Usage
Mark asked to move the thread to Sonnet once the research was done. Cluster reports from C2 onward were completed by Sonnet from the earlier agents' saved runs.

## 2026-10-26 — No quiet change to the build; priority is answering from sources
Asked how the work should enter the build, Mark's answer: the priority is being able to answer the questions well from sources; expand access to resources and the accuracy of the context and answers. No method change is proposed or applied. If one is needed it comes to Mark as a change order with old and new text.

## 2026-10-26 — Commentaries wanted, every era
Mark: collect every Bible commentary that can be found; this will help pastors. Surveys cover Eras 1 to 10. Origen's Commentary on Romans is first on the list. Many editions, hosts and licences are from memory and marked unverified.

## 2026-10-26 — Chrysostom homilies mapped to built worlds
Decision: imperial-juridical-christianity as tradition; hieronymian-ascetic-literary, gallic-monastic-ascetic-christianity and cappadocian-nicene-pastoral-monastic-tradition as context; no download. Written as a change list (`Worklists/chrysostom-mapping-change-list.md`), not applied, because the `_staging` files belong to the Library thread. Open point: `context` means the outside view and Chrysostom is a neighbour for those three worlds.

## 2026-10-26 — Saved; Library thread launched
Mark: save it and launch a new library thread to support this work. Saved to this folder on branch `claude/question-coverage-2026-10-26`. Library thread launched with `Library-Thread-Launch-Prompt.md`.

## 2026-10-26 — Opus review of the work; corrections
Mark asked for an Opus review of the work and the recommendations (`Review/opus-work-review.md`). Result: 38 claims checked, 26 held, 7 in part, 5 failed; 6 of 6 quotes matched. Corrections applied in place and marked "corrected after Opus review": the hal Origen-versus-Jerome row (withdrawn), Fabiola's husband (not "violent"), the privacy cookie item (withdrawn), and "contradicted" limits narrowed. Two of my own earlier actions were wrong and are reversed: (1) the Library launch prompt added a Doc_02 per-sub-question duty while saying the remit was unchanged, which is a method change, so it is struck and the Library thread was told; (2) the Chrysostom mapping is held for re-decision, because most of those homilies were preached at Antioch before Constantinople and `context` means the outside view. Held for Mark: the 69 Facilitator-adjacent rows (Facilitator Governance V3.6), the "loaded" sizing (re-run with role, window and author filters), the acquisition re-scoring.

## 2026-10-26 — Loaded re-run; Augustine counted as outside voice
Sizing redone with role, window and author (`Worklists/loaded-rerun-2026-10-26/`). Of 299 loaded-only cells: A 219, B 23, C 36, D 1, X 20; 161 of the 219 A cells are located passages. Mark ruled: Augustine's anti-Donatist (don) and anti-Pelagian (gallic) works count as outside voice for sizing, though the map labels them `tradition`. The don and gallic threads are asked how they treat him. Under the map's labels the A total would be 227.

## 2026-10-26 — Real visitor questions folded in
Mark pasted the dashboard list for 20 to 26 October: 11 questions, about four visits, four worlds (pahc, syr, alx, desert). Nine entered as REAL (C3-31, C4-27, C4-28, C5-31, C6-27 to C6-30, C7-29); the repeated "who is jesus" is already C1-01. Visitor kinds are my reading (K1, some K9), not known. The recurring-questions rollup was not supplied. The sample shows what has appeared, not what is typical. Mark ruled: "how did you come to believe in Jesus" and "how did you start this tradition" form a new sub-question, C6.S9, with a new flag NI (no invented personal history).

## 2026-10-26 — Facilitator fall-through: rulings
Findings: Governance V3.6 section 12 already names "Are you an AI?", "Who made this?" and "Why do you keep saying 'we'?" as frame-breakers never routed to the Representative; today's code (`engine/m5/routing.py`) catches only the AI, bot, real and built shapes. The doc is silent on privacy and has no rule for adding a shape. Mark ruled:
- Who is behind this and what are you: a small family of fixed Facilitator templates (are you real, who made this, why we), all code-owned (option B1).
- Is this private: one new fixed Facilitator template, filled from the facts file, pointing to the privacy page and the in-app delete control (option A1).
- Facts live in one code-owned facts file in `engine/`, with a test that checks each line against `privacy.html` and `about.html` (option C1).
- The 69 held Facilitator-adjacent rows release in two groups (R1): the 18 system and product rows after the shapes are built; the 51 pastoral rows only where the distress path is confirmed.
Not done: no Facilitator wording written, no engine change, no change order filed. The new shapes and any new text come back to Mark by change order. The reader classes need a model call to retest, which needs a named, capped live test from Mark. Facts still to be supplied by Mark: whether the project team who review conversations may be named and what reviewers see; whether any person may be named; whether the Facilitator may name Anthropic's Claude and a model version; any funding or church affiliation; counsel's review of the privacy text; whether the privacy page should say scores and flags are kept without text.

## 2026-10-27 — Safety guards: gaps logged, alx and witt guards applied, don held
Gaps logged: don OG-49, witt OG-82, alx OG-37. Correction to the hand-off: the Augustine precipice text is lines 16889 to 16891 and speaks of Donatist "confessors", not the Circumcellions (only para. 110 links them to precipices). Mark approved the alx and witt guards: applied, with follow-up entries alx OG-38 and witt OG-83, and both worlds pass `records` and `regate`. The don guard was first held; Mark ordered an Opus review of it: not fit as drafted, with five blocking findings (the claim that only para. 110 links the Circumcellions to precipices is false, since paras. 46 and 204 do; the four cited passages are a selective sample; a Donatist-voiced account exists in the Passio Marculi; the `claim` field carried Augustine's verdict on the card; `use_note.years` was missing). Review verdict on the waiver: no bump and no analytic voice; mark the record ready after fixes and an independent recheck. A separate honest limit is also needed for the question a bereaved visitor asks. Review text: `Review/opus-don-guard-review.md`. Mark then ordered the record written with the review's corrections: `don.contested.augustine-precipice-charge` (ready, `use_note.status` provisional) and two `not_for` edits, gaps OG-49 and OG-50; the honest limit for a bereaved visitor's question is still to be written.

## 2026-10-27 — Retrieval for visitor wording: canon change order approved
The first week of real questions showed that retrieval, not only missing records, keeps good records from being reached: six of ten questions reached no cell or the wrong one. Mark approved, as a named change order, five `[measured]` questions added to existing canon cells in the visitors' words, "as written" (`Build/Ministry/Operations/Audits/2026-10-27_canon-visitor-wording_ChangeOrder.md`). No new cells, no record hints, no matcher change. Offline bench rerun: ground records 1,226 to 1,258, cells reached 159 to 162, quotes 205 to 210; two small losses (gallic, rzg) left visible. The alias layer in the matcher is held. Found on the way: the canon seed script has drifted from eight hand-edited records and must not be re-run over them.

## 2026-10-27 — No world threads; first record batch written here
Mark: there are no active world threads, so the record work from the real questions is done in this thread. Mark chose a first batch of honest limits and guard fixes (not quote records yet). Written on Sonnet, gates run per world, Opus review of the changed lines to follow: the don limit on the fate of those who end their own lives; 'faith alone' limits for alx and pahc; 'what must one do' for syr; assurance and the dead for pahc; origins for desert; a use note on `pahc.quote.appointed-to-be-read`; the dangling `pahc.contested.table-diversity` reference removed. Gaps: don OG-51, alx OG-39, pahc OG-42, desert OG-41 (syr has no gaps file). Mark ordered an Opus review of the batch (`Review/opus-honest-limits-review.md`): two records not fit as written (the alx limit misread Clement's Stromateis I.9 and left out Paedagogus I.6; the pahc assurance limit left out 1 Clement 50 and Polycarp 9 and so slanted against the faithful dead being with the Lord), a false absence claim in the don limit (Augustine's Contra Gaudentium quotes a Donatist bishop on chosen death and was not read), and a misstatement of Jerome in the desert limit. All fourteen findings were applied or answered on the same branch. The 367 Athanasius quote is now `voice: analytic`, not voiced with a false `years` range. `desert.dw.apostolic` conflicts with Cassian Conference XVIII.5 and is flagged, not edited. `use_note.status` stays provisional on every new record until someone other than the author rechecks the corrected text. The shortlist's item on `retrieve_when` for empty witnesses is dropped: the retrieval rules call a hint written from a failing question overfitting, and the canon change order took the right route.

## 2026-10-27 — Facilitator change order parked; honest limits rechecked
Mark asked how the Facilitator change order relates to questions design. Finding: it answers a gap the study found (system questions fall to the Representative, which has no facts), but the evidence for it is the research and predictions, not the real questions; none of the ten real questions this week were about the system. Mark agreed: the Facilitator change order (B1, A1, C1, R1 above) is parked. The rulings stand as recorded; nothing is built and no wording is written, and it resumes when Mark asks and has supplied the facts.

Mark then had the corrected honest limits rechecked by a fresh Opus reader (`Review/opus-honest-limits-recheck.md`). Verdicts: ready to mark reviewed for `pahc.limit.faith-alone-later-frame`, `syr.limit.what-must-one-do` and `desert.limit.origins-no-single-founder` (now `use_note.status: reviewed`, with the reader's wording nits applied); named changes for the don limit (it told the visitor about unread letters on a death chosen under pressure and named a method), the alx limit (an overclaim in the opening, and Quis Dives 27 universalised) and the pahc assurance limit (Justin was said to have met people he only warned Trypho about; an unsearched assurance claim; "the Lord's day"). Those corrections are applied with the reviewer's wording. The don, alx and pahc assurance limits stay `provisional` until the corrected text is read by someone other than the person who wrote it.

## 2026-10-27 — Cap ruling on the honest limits; third round applied
The third reader (`Review/opus-honest-limits-final-read.md`) passed the alx limit (one overstatement fixed) and found two blocking safety defects: the don limit named a method ("perished by the rope") and set "the traitor" beside a suicide question; the pahc assurance limit's Justin sentence read as saying a bereaved visitor's belief that the dead go to heaven is not Christian. Under the three-round cap these came to Mark. Mark ruled: apply the reader's exact corrections and order one more read by a different reader (`Review/opus-honest-limits-read-4.md`, named in a Cap ruling entry in the System Hub Decision Log). Applied: the don statement now keeps only the martyrs-quarrel line and cites Optatus; the pahc assurance statement drops Justin (his view stays in `not_for`) and restores "by God's grace"; the alx closing is reworded. Also corrected: the don record's account of the Monumenta file (it holds the Passio Marculi, a Donatist text that has Marculus pushed from the cliff and places martyrs in heaven), the Petilian locus (II.8.17), and a stray line break inside the pahc spoken text. Nothing moves to reviewed until the fourth read passes.

## Findings passed to other threads (information, not instructions)
- Latin pastoral thread: Augustine's commentaries are vendored and mapped to it; its 330 records are all draft with no use notes; nothing on hell, the dead, infants or suicide. Sent 2026-10-26.
- System and pilot-feedback thread: asked to route the Chrysostom mapping to the corpus-map owner. Sent 2026-10-26.

## Open
- Whether and how the question-coverage pass joins the build cycle (change order, if any).
- Passage index design for commentaries.
- Real visitor questions: first week entered 2026-10-26; the recurring-questions rollup and later weeks still to come.
- Per-world gaps from `Worklists/records-by-world.*` go to each world's `Open_Gaps_Tracking.md` through that world's thread.
