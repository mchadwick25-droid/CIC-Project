# Full-system review: scholarly rigor and content quality, 2026-10-23

One of four parallel reviews Mark asked for on 2026-10-23. This one covers scholarly rigor and content quality. Engineering, safety and operations; participant experience; and market readiness are reviewed separately. Read-only: no product file was changed, no model was called, and no paid service was used.

Status: reviewer findings by Opus. Any finding marked blocking needs independent re-confirmation before it is acted on as settled (CLAUDE.md, "Governance vocabulary and closure").

## 1. Scope and method

**Commits reviewed.** `origin/main` = `e64646393` (merge of PR #1083). `origin/live` = `469d072cf` (merge of PR #1081, 2026-10-23). The world registry (`records/worlds/*.yaml`) gives the same state and the same package pin on both branches for all 20 worlds. Production therefore serves the same eleven packages reviewed here.

**What I read myself.** `CLAUDE.md`; `README.md`; all 20 registry files; the quote, source, voice_craft and world_core records of the eleven admitted worlds; `engine/m1/gates.py` (readability thresholds, `grade_text`); `cic-poc/frontend/src/components/Arrival.tsx` and `engine/api/wiring.py` (which text reaches participants); `cic-website/data/worlds/*.json` (tradition pages and narration text); `Build/Ministry/Operations/Audits/2026-10-19_live-reply-claim-check_eleven-worlds.md`; the 2026-10-21 change order and decision 36 text in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`; `engine/m3/reports/admission-2026-10-09/`; selected `Open_Gaps_Tracking.md` entries; the vendored source files named below.

**Delegated reading.** Four read-only subagents surveyed: build documents and review counts per world; the Library's provenance and rights; the Family Tree census and narration; and validation evidence. Their reports were leads. Every claim below from that reading was either re-checked by me against the file, or is marked "(survey count, not re-checked)".

**Commands and checks I ran.**
- Quote verification, all quotes, not a sample: a script resolved each quote record in the eleven admitted worlds to its vendored file through `sources[].source_id` → the source record's `cic/texts/` path. It normalized whitespace, quote marks, dashes, case and XML tags, split on ellipses, and tested each segment as a substring. Unmatched quotes were re-tested ignoring punctuation, then ignoring digits and short bracketed apparatus. Every quote still unmatched was opened and read by hand against the source line.
- Readability: `engine.m1.gates.grade_text` (the project's own scorer) on each admitted world's `doorway_description`, `card.summary` and `card.intro`, and on all 366 `modern_rendering` values. Sentence length (over 25 words) by a simple sentence split, with three results read by hand.
- `python3 tools/check_live_commentary.py --surface records`.
- Spot re-checks of the 19 October claim-check findings against current records and vendored texts.

**Not checked.** Live replies (any check needs a model call; CLAUDE.md forbids it here). Audio against text word by word (only character counts were compared, by the survey). Doctrinal-witness, story and term records line by line against sources, beyond the spot checks named. Doc_01–Doc_10 content quality (only presence, status lines and review counts). Rights of the 929 texts one by one (survey counts only). Representative images.

## 2. Done, with evidence

Built from the registry and the files, not from memory. "Docs" counts construction documents found under `Build/worlds/<code>/` (survey count, not re-checked). Quotes, contested claims and honest limits are counts of files in `records/<code>/`. "Quotes found" is my verification result.

| Code | Tradition | State | Representative | Package pin | Docs | Quotes found / total | Contested | Honest limit |
|---|---|---|---|---|---|---|---|---|
| alx | Alexandria | admitted | Theon | 2026-10-20 | D01–D09 | 26/26 | 5 | 3 |
| cappadocian | Cappadocia | admitted | Chilo | 2026-10-20 | D01–D09 | 21/21 | 4 | 2 |
| desert | Desert monks | admitted | Papnoute | 2026-10-21 | D01–D10 | 61/61 | 3 | 6 |
| don | Donatism | admitted | Fidelis | 2026-10-21 | D01–D09 | 5/5 | 12 | 7 |
| gallic | Gaul | admitted | Renatus | 2026-10-21 | D01–D09 | 110/110 | 5 | 2 |
| hal | Bethlehem circle | admitted | Albina | 2026-10-20 | D01–D09 | 32/32 | 7 | 4 |
| ijc | Church and Empire | admitted | Marius | 2026-10-20 | D01–D09 | 39/39 | 7 | 7 |
| pahc | Household churches | admitted | Chloe | 2026-10-20 | D01–D09 | 25/25 | 9 | 4 |
| rzg | Zurich and Geneva | admitted | Theophilus | 2026-10-20 | D01–D09 | 6/6 | 3 | 9 |
| syr | Syriac | admitted | Mar Yausep | 2026-10-20 | D01–D09 | 34/34 | 8 | 4 |
| witt | Wittenberg | admitted | Nikolaus | 2026-10-20 | D01–D10 | 7/7 | 5 | 2 |
| fix | fixture | built | Vera | 2026-10-20 | none (synthetic) | not checked | 1 | 4 |
| lpc | Latin pastoral | building | none | none | D01–D09 | not checked | 4 | 9 |
| rcg | Roman Gregorian | building | none | none | D01–D02 (D02 not cleared) | — | — | — |
| aec, hus, jes, meth, obel, wsyr | six candidates | candidate | none | none | D01–D02 (aec, meth "not approved to proceed") | — | — | — |

Also: `grkap` and `latap` have only a Step 0 document and no registry code; the four `Build/World-Builds/` worlds have only Doc_01.

**Proven by a file or a check:**
- **Every quote in the live worlds is in its vendored source.** 366 of 366 quote records were found. 312 matched exactly after normal clean-up. 25 matched once punctuation was ignored. The other 29 were read by hand: 24 differed only by scan noise in the source file (verse and page numbers, footnote marks, line-end hyphens, OCR misreads such as "Tor" for "For", "1 do" for "I do", "onr" for "our"). Five used ellipses or Latin with a gloss and are correct at every segment. **Mismatches in wording: none.**
- **Confidence tags use only the five-level vocabulary.** No non-standard `formation_confidence` value is in any record (survey grep, not re-checked line by line). Contested and Inferential-Thin tags are in active use: for example pahc has 48 Contested and 15 Inferential-Thin tags.
- **Every Representative is defined as a composite voice, with no invented life.** I read the `identity:` field of all eleven voice_craft records. Each says the voice is a role or a whole community, not a person ("Fidelis is not a biography"; "No invented memory" in alx). None gives an age, a family or a personal history.
- **The site census matches the registry.** For all eleven, dates, Representative name, card summary and card intro match (survey check). Only the short place labels differ.
- **Known gaps are tracked.** Each of the eleven admitted worlds has an `Open_Gaps_Tracking.md`, and each logs the 19 October claim check as an open entry (for example `Build/worlds/hal/Open_Gaps_Tracking.md` OG-29, "Status: OPEN").

## 3. In process

- **The 19 October claim-check fixes.** That audit found 4 to 10 unsupported or contradicted claims per world in the records behind live replies. Of eleven findings I re-checked, seven are still in the current records (section 6, R1).
- **lpc** is at "building", with D01–D09 approved to proceed and no Representative in the registry. **rcg** is held at Doc_02, which is not cleared and is logged as an unresolved tension.
- **Six candidates** (aec, hus, jes, meth, obel, wsyr) are at Doc_01–Doc_02. aec and meth carry "Not approved to proceed" after three rounds. That is the cap, so each is an escalation to Mark (survey reading of status lines, not re-checked).
- **Source acquisition.** `WANTS-REGISTER.md` lists 154 wanted sources across 11 worlds, 113 of them not yet classified. Cappadocia has the most (56), then Wittenberg (42) (survey count).

## 4. Still needed for the full system to be live

1. **Fix the record errors found on 19 October and re-confirm them independently.** These are claims the voice repeats as fact.
2. **Evidence that each Representative holds under pushback, on the package it actually runs.** Today there is none on file for any current package (R2).
3. **Bring participant-facing text to the readability bar and the tradition vocabulary.** That covers the arrival-screen paragraphs (R3) and the recorded narration (R4).
4. **Re-record Donatism's two drifted narration pieces** and add a fingerprint check for world audio (R5).
5. **External scholarly review.** None has happened. The only file in `Build/Ministry/Scholarly-Review/` is an unsent draft letter, deferred to "Year 2" (survey reading; I confirmed the folder holds one file).
6. **For the full portfolio:** nine worlds not yet built past Doc_02, and the Phase Five plus full-system closure gate, which nothing has passed.

## 5. Quality: strengths with examples

- **Quote fidelity is genuinely high.** No wording error in 366 quotes is unusual for a corpus this size. Records keep the qualifier inside the sentence instead of trimming it. Example: `alx.quote.a-doctrine-they-would-not-have-taught` keeps Origen's "I hold to be", and its `not_for` list forbids using it as eyewitness proof.
- **Uncertainty is modeled, not hidden.** `use_note.not_for` lists, `divergence_note`, contested_claim and honest_limit records are everywhere. Example: `witt.contested.1543-treatise-later-effect` tags itself Contested and says plainly that both scholarly positions reach the library only through a tertiary source.
- **Absence is named.** The alx world core lists what does not survive: no child's own story, no ordinary deathbed account, no woman's own words.
- **Thinness is told to participants.** Every card carries a `record_holds` line, for example "Rich in teaching and argument. Thin on ordinary believers and rural Egypt."
- **Modern renderings mostly meet the bar.** Of 366, only 5 fail the FK and FRE gate. Most read cleanly and keep every clause.
- **Provenance is traceable.** Each source record names edition, translator, vendored file and rights basis. Example: `alx.source.origen-contra-celsum` reads rights from the file's own DC.Rights header and notes the better copyrighted translation it could not use.

## 6. Risks, ranked

### Blocking

**R1. Live records still state things their own sources contradict.**
- *Evidence.* The 19 October audit found 4 to 10 class-D (unsupported or contradicted) claims per world. I re-checked eleven of them against current records. Seven are still present: hal, pahc memoirs, pahc Quintus, witt "the how", ijc "settled who Christ is", cappadocian epektasis, alx "closes the era". Four were no longer found. Two I confirmed against the vendored text myself:
  - `records/hal/doctrinal_witness/hal.dw.suffering.md:48` says grief was "never condemned as unbelief". Jerome, Letter 39, to Paula on Blaesilla's death (`cic/texts/npnf206_jerome-principal-works.xml:8125-8127`), says: "Yours are detestable tears, sacrilegious tears, unbelieving tears."
  - `records/pahc/quote/pahc.quote.the-memoirs-of-the-apostles-are-read.md:32` says of the memoirs that Justin "does not call them that" (the Gospels). Justin, 1 Apology 66 (`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml:16477-16478`), says: "in the memoirs composed by them, which are called Gospels".
- *Failure scenario.* A participant asks the Bethlehem circle how it treated grief. The voice, grounded in `hal.dw.suffering`, says grief was never called unbelief. The best-known letter of that circle says the opposite. A participant who knows Jerome stops trusting every answer.
- *Why blocking.* These are fabrications at the record level, the failure CLAUDE.md ranks most serious. Quote gates cannot catch them: the quotes are right, and the prose around them is wrong.
- *Smallest fix.* Work the 19 October list world by world. Correct each record against the cited locus, then have a second Opus pass re-confirm it. Closing an entry needs that independent check.

### High

**R2. No evidence on file that any live Representative holds under pushback on the package it runs.**
- *Evidence.*
  - The latest admission results are `engine/m3/reports/admission-2026-10-09/` (28/28 for all eleven). They test single-turn source boundedness and register only. There are no pushback, fabrication-bait or out-of-window probes. They also ran on 9 October packages, and all eleven pins are now from 20 or 21 October. I confirmed the alx report's details and the pins.
  - The boundary-test transcripts are simulated or design-time, and older than the current packages (survey list).
  - Decision 36 ("an admitted or open world has a live admission report on its pinned package") still stands per the 2026-10-21 change order. The change order says it "is no longer checked at promotion". So all eleven "admitted" states currently lack the evidence that decision requires.
- *Failure scenario.* A participant pushes: "Surely Calvin agreed with Luther on the Supper?" The voice caves or invents a compromise. Nothing on file says whether the current package resists that.
- *Smallest fix.* This is Mark's call, since it costs money. Run one capped, named pushback set on the current pins, saving the transcripts. Or record in the registry that "admitted" no longer implies a current admission report, and amend decision 36 to say so.

**R3. The arrival-screen paragraph fails the readability bar in 9 of 11 worlds, badly in three.**
- *Evidence.* `doorway_description` is shown on the Arrival screen (`cic-poc/frontend/src/components/Arrival.tsx:31-33`, served by `engine/api/wiring.py:321`). By the project's own `grade_text` (bar: FK ≤ 10 and FRE ≥ 60):

  | World | FK | FRE |
  |---|---|---|
  | rzg | 19.8 | 17.7 |
  | don | 19.4 | 24.4 |
  | cappadocian | 15.5 | 36.6 |
  | desert, gallic, syr, witt | 8.6–9.3 | 53–59.9 |

- *Card intros.* Seven of eleven `card.intro` texts also fail, for example hal at FK 11.7 and FRE 32.5.
- *Example.* Donatism's paragraph includes "not a doctrinal heresy - its confession is standard North African Latin Trinitarian and Christological orthodoxy".
- *Not gated.* I found no gate on `doorway_description` or `card.*` (searched `engine/m1/gates.py`, `engine/m10/`, `tools/`).
- *Failure scenario.* A non-native speaker picks Zurich. The first paragraph they read is graduate-level, and they leave before the conversation starts.
- *Smallest fix.* Rewrite the three worst paragraphs to the house standard. Then add these registry fields to the readability gate, so the fault is fixed at its source.

**R4. The public narration and tradition pages say "this world" to participants about 176 times, mostly as "this world's own".**
- *Evidence.* Counts of "this world" in `cic-website/data/worlds/*.json` (survey method; I re-ran the counts):

  | Tradition | Count |
  |---|---|
  | ijc | 28 |
  | rzg | 22 |
  | alx | 20 |
  | desert, pahc, syr | 18 each |
  | hal, witt | 17 each |
  | cappadocian | 15 |
  | gallic | 3 |
  | don | 0 |

- *Narrated aloud.* The `orientation.legacy` text is read aloud (`Build/tools/generate_world_narration.mjs`, per survey). For example: "This world's own eight named categories of tempting thought…" (desert) and "This world's own final council did not close in agreement" (ijc).
- *Inconsistent with other text.* Elsewhere participants are told "Christian tradition" (alx `doorway_description`).
- *A generated tic.* The doubled "own" ("this world's own record", "its own span") is the kind of generated cadence CLAUDE.md 1.2 calls an AI tell.
- *Failure scenario.* A visitor hears "this world" and takes the tradition for a fiction or a game world. The repeated "own" makes the narrator sound machine-made.
- *Smallest fix.* Fix the upstream world-front records the pages are generated from, regenerate, and re-record the affected pieces. Donatism already shows the target wording.

### Medium

**R5. Donatism's recorded audio no longer matches its text.**
- *Evidence.* The `story` piece and the Carthage 411 telling changed length after recording (3985 → 3965 and 1321 → 1287 characters; survey measurement, not re-checked).
- *No check.* `generate_world_narration.mjs` stores no fingerprint, so a changed text is never re-recorded unless forced. A same-length edit in any world would also go unseen.
- *Smallest fix.* Re-record the two pieces as a gated paid run (sample first). Add the fingerprint check the docstory and site generators already have.

**R6. Wittenberg's account of Luther's 1543 treatise rests on Wikipedia.**
- *Evidence.* `witt.contested.1543-treatise-later-effect` cites `witt.source.wikipedia-on-the-jews-and-their-lies` as "the tertiary intermediary through which both poles reach this library". Luther's text itself is `kind: unvendored`.
- *Honest, but thin.* This is disclosed honestly and tagged Contested. Still, it is the most sensitive subject in that tradition, and the voice cannot quote or check Luther's own words.
- *Also.* The same record marks Kaufmann (2017) and Wallmann (1987) `license: public-domain`, which is wrong for modern scholarship.
- *Smallest fix.* Vendor the public-domain German original (Weimar edition) and correct the license fields. Whether a public-domain English translation exists was not checked.

**R7. About one in six modern renderings has a sentence over 25 words.**
- *Evidence.* 60 of 366 by my split. Some are inflated by quoted Scripture inside the sentence.
- *Hand-confirmed.* `cappadocian.quote.basil-on-antiphonal-psalmody`'s last long sentence is 34 words and has lost its subject ("…all together, as with one voice and one heart, raise the psalm…"). Cappadocia is worst: 9 of 21.
- *No gate.* I found no gate on the 25-word rule; FK is gated, sentence length is not.
- *Smallest fix.* Opus re-renders the flagged items (the rendering rule). Add a sentence-length check to the existing rendering gate.

**R8. Canonical records carry build commentary.**
- *Evidence.* `tools/check_live_commentary.py --surface records` reports 896 hits: 40 REWRITE and 5 ROUTE.
- *Example.* The body of `alx.quote.a-doctrine-they-would-not-have-taught` narrates why the record was made ("could not show it: C-E was served by that witness alone").
- *Why it matters here.* This breaks CLAUDE.md's clean-surfaces rule. Where body text is retrievable, build reasoning can leak into what the voice says.
- *Smallest fix.* Clear the 45 REWRITE/ROUTE lines in the next records PR, as CLAUDE.md requires.

### Low

- **R9. Census place labels drift in three worlds** (survey, not re-checked):
  - cappadocian says "Anatolia", which is not in the registry.
  - desert drops Palestine.
  - syr drops Adiabene.
- **R10. A better Latin witness exists for one quote.**
  - `don.quote.emeritus-magno-argumento` says "No clean vendored transcription exists to repoint to".
  - `cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-4-410-431-lat_welter-facsimile1901.txt:19491-19494` carries the same passage with far better OCR. Repointing would allow `verified-direct`.
- **R11. Some quote `text` fields mix the original with a translation.** Example: `don.quote.donatus-quid-est-imperatori` puts the Latin and an English gloss in one field. Verbatim checks then have to treat the gloss as source text.
- **R12. Card summaries often fall below FK 8.** Ten of eleven are between 5.0 and 7.7. CLAUDE.md calls grade 8 "a floor worth staying above". This is a watch item, not a defect, unless the text reads flat.

## 7. Best parts

1. Quote fidelity: 366 of 366 quotes found in their vendored source, with no wording errors.
2. A five-level confidence vocabulary that is actually used, with Contested and Inferential-Thin tags in quantity rather than everything marked Documented.
3. Composite Representatives with no invented lives, stated in each voice's own identity line.
4. Honest thinness, told to participants on every card and modeled as honest_limit and absence records.
5. A traceable, rights-checked Library: 929 vendored texts with a registry and per-file rights headers. The 35 that are not public domain are marked as such (survey count).

## 8. Gaps

- No current-package evidence for pushback, fabrication bait or out-of-window behaviour (R2).
- Record-level contradictions still open from 19 October (R1).
- No external scholar has reviewed anything. Every review on file is an AI review.
- No readability gate on registry display fields (R3), and no sentence-length gate on renderings (R7).
- No audio-to-text fingerprint for world narration (R5).
- Primary text missing for Wittenberg's most sensitive subject (R6). Cappadocia rests on 59 unvendored sources, more than any other world (my count of `kind: unvendored`).

## 9. Cross-lens notes

- Engineering: the 19 October audit says sentences marked `verdict: withhold` in grounding reached the final reply in alx and Cappadocia. That is an engine question, not yet investigated.
- Engineering: the README generator leaves the rights column blank for nine XML volumes (anf05, anf06, anf09, npnf101, npnf102, npnf104, npnf106–108). The files themselves say Public Domain (survey).
- Engineering: `CORPUS-USE.md` says 835 vendored files; there are 929 (survey).
- Participant experience: the tradition pages' `representative` speaker label and the site's "Representative" wording.
- Safety: the admission battery has no distress probe (survey). Safety classification itself is outside this lens.
- Market: the absence of external scholarly review is the first thing a due-diligence reader with a theology background would ask about.

## 10. Five questions for Mark

1. Should "admitted" still mean "has a live admission report on its pinned package" (decision 36)? Or should the registry and decision 36 be changed to match the 21 October change order?
2. Will you approve one small, capped pushback test on the current packages, with transcripts saved, so there is at least one current piece of evidence per world?
3. Which comes first: fixing the 19 October record errors (R1), or rewriting the participant-facing paragraphs and narration (R3, R4)?
4. On the public site and in narration, should participants hear "tradition" everywhere and never "world"?
5. Is external scholarly review still a "Year 2" item, or should one reviewer read one world before more worlds go live?
