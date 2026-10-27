# lpc story tellings (round 1) and public face (round 2): independent review

- **Part A verdict: Revise.** One P1 (the death of Cyprian, the sentence) and three P2s. The other tellings hold to their records and sources.
- **Part B verdict: Approved to proceed.** P1-1, P1-3 and P2-1 to P2-9 are applied correctly. Leaving P1-2's `horizon` paragraph for the project lead is acceptable for now. Two small P2 fixes need no further round.

- Change set, Part A: the seven `telling` fields in `records/lpc/story/*.md`. They were uncommitted when the brief was written and are now in commit c24e4bdc ("story tellings ... pending review"); that commit's content was reviewed. Author's claims: `Review-Artifacts/Story_Tellings_Authoring_Notes_2026-10-27.md`.
- Change set, Part B: commit 76875af9 against 734de2d4 (`records/worlds/lpc.yaml`, world_core, `wb_lpc_s21.py`, the traditions page).
- Reviewer model: Opus 5.5 (`claude-opus-5-5`). Part A round 1; Part B round 2, a targeted recheck.
- No repo file was modified other than this one. No model call, no spend, no generator, no git write. `canon/sealed_probes/plaintext/` was not read.

## Part A: checks

1. **Speech against the quote records.** Every quoted line was compared with its quote record's `modern_rendering`. All are verbatim, or a verbatim clause of it.
   - Checked: election (`chosen-while-still-a-neophyte`, `ancient-venom-against-my-episcopate`); Celerinus (`grieve-with-me-for-my-sister` from "Grieve", `shut-up-in-two-cells` last sentence, `the-case-set-before-the-bishop` last sentence, `because-i-am-already-weary`); Numidicus (`numidicus-remained-unwillingly`, five pieces); captives (`grief-and-not-without-tears`, `christ-redeemed-in-our-captive-brethren`, `a-hundred-thousand-sesterces`); plague (`a-dreadful-plague-broke-out`, `it-becomes-us-to-answer-to-our-birth`); death (`the-people-kept-watch-at-the-door`, `thanks-be-to-god`, `let-us-too-be-beheaded-with-him`); psalms (`the-psalms-hung-upon-the-wall`, four sentences, and `he-slept-with-his-fathers`).
   - Attributions hold. Galatians is given to Paul, the Scripture phrase to Scripture, and "Thanks be to God" and the cry to the Acta only. Nothing is given to the sister, Numeria, Candida, the wife or the daughter. PASS.
2. **The author's own rendering, "So I know she has not sacrificed." (Ep. XX §3).** Hartel (`cyprian_epistulae-lat_hartel1871-csel3-tei.txt` 3168-3170): *hanc ergo non sacrificasse ego scio*. ANF (30628-30629): "I know, therefore, that she has not sacrificed." Clause by clause: *ergo* is "So"; *ego scio* is "I know"; *hanc ... non sacrificasse* is "she has not sacrificed". Nothing is added. Only the stress on *ego* is lost, and that is harmless. PASS.
3. **The two variant readings.**
   - **Numidicus, *inuitus* / *inuictus*.** In Hartel's apparatus (5679-5690), against line 6 of p. 586, is "inaictus *Bv*" (OCR for *inuictus*). That is the siglum of one manuscript (B) plus *v*, the older printed editions. Hartel's text reads *remansit inuitus*. "One manuscript and the older printed editions read 'unconquered'" is exact. The telling tells the story by Hartel's reading and names the variant without settling it, which keeps the quote record's not_for. PASS.
   - **Plague, "not only to His own".** Hartel's text (`cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` 40837-40838): *exhibens cuncta ista non suis tantum :*. Apparatus (40869): "sed etiam alienis add. v". **The author's claim is right.** "Strangers as well as His own" rests only on the older editions that Hartel cites as *v*, and Hartel's text does not print it. The telling's "not only to His own people" follows Hartel and keeps the quote record's not_for. PASS.
4. **Facts against `text`, the limits and the sources.** Traced line by line. Notes:
   - Election. Stepping back for older men and the crowd at the doors: Pontius §5 (ANF 27826-27840). The limits are kept: Pontius alone on "neophyte", writing in praise, and no account of how the favour was shown (the quote guard). One wording problem: P2-1.
   - Celerinus. Lucian still in prison: Ep. XX §3, "You have desired to be sent into prison ... which now has come to pass". Works for "our banished colleagues": Ep. XX §2. Grant "in the name of" Paulus and the other martyrs: Ep. XXI §2. The condition is kept. "Both letters call what the women did a great sin": Ep. XX §3 "such a great sin" and Ep. XXI §1 "so great a crime committed". The sister is unnamed and none of the three women speaks. "Had been imprisoned" is not in Ep. XX or XXI, but it is documented in Ep. XXXIII (ANF 31984: "For nineteen days, shut up in the close guard of a dungeon"). So it is true but cited to the wrong letters; see problem 4 below. One omission: P2-2.
   - Numidicus. The place of the search is unknown, nobody's words survive, and there is no name for the wife or the daughter. The "completion" sentence is from `modern_contrast`. PASS.
   - Captives. The eight names are in the letter's salutation (ANF 36007-36009). "In Numidia" is not in the letter's body or in Hartel's manuscript title (*Ad Ianuarium et ceteros de captiuis redimendis*). It is the ANF heading's, and the `use_note.means` and the quote record already carry it. The sees are the standard identification, so this is not a finding. There is no conversion and no outcome. PASS.
   - Plague. The publican and the heathen, love of enemies, prayer for persecutors, the labour of the poor (*multi qui paupertatis beneficio sumptus exhibere non poterant ... proprio labore*) and Tobias: Pontius §9-10, with the Latin at 40832-40867. The telling avoids the record `text`'s "bodies left where they fell" and "strangers". The single witness, his praise and the persecutors limit are all kept. PASS.
   - Death. The date: Acta VI, *die octaua decima kalendarum Octobrium* (Knopf 4955). The field of Sextus, the cloak, kneeling and the twenty-five gold pieces: Acta 5.2-5.4 (Knopf 4917-4922). The difference over the cloths is stated and left unresolved, and the strengthening from above is Pontius's. One error: P1-1.
   - Psalms. Forty years: Possidius epilogue (5057-5060). Third month and fever: ch. 29 (4146-4147). No will, "a poor man of God", the library: ch. 31 (4983-4986). Single witness: kept. PASS.
5. **Readability (`engine.m1.gates.grade_text`).** The author's figures are confirmed: FK 5.2 to 6.3, FRE 73.9 to 80.6, longest sentence 19 to 24 words, mean 12.2 to 14.6.
   - **Plain and fine, not flattened.** The low FK comes from short sentences and from the quoted renderings, not from lost words or lost images. The world's own images all survive: the Tria Fata, "the brightness itself", "burned ... preserved", "fruitful fields in which to sow the seeds of our hope", "no longer bodies but the corpses of many", Zacchaeus in the branches, the sheets on the wall. That fits the earlier ruling that FK about 6 on surface records is not flattening when the images survive. FK 8 is a report-only floor; nothing needs merging.
   - **Length.** The 288 words of the death telling is not a defect. It is the only telling with two witnesses to keep apart, and it is within about 15% of the others. After P1-1 it grows by about a dozen words.
   - **The omitted point** (the two texts are not independent witnesses on the sentence) is a defect, because of how the telling words that sentence. It is folded into P1-1.
6. **AI tells and register.** There is no hedging filler, no disclaimer used as a crutch and no assistant cadence. The closing limit lines ("Only Pontius says ...", "Possidius is the only witness ...") are the world's own way of naming its witnesses. The Numidicus line on manuscripts is outside knowledge, but it is short, plain and needed. The captives line "not about charity but about who the captives were" is a "not X but Y" turn, but it comes from the record's own `text`. Not findings.
7. **Voice.** "We / our / us" matches each record's `text`. The psalms telling turns Possidius's "we stood by" into "Possidius and the others stood by". That is clearer for a page reader, and consistent. PASS.

## Part A: findings

P1 means wrong, unsupported or misleading. P2 means a plainly correct small fix.

- **P1-1 (`lpc.story.the-death-of-cyprian`, `telling`, paragraph 3): the sentence attributes Pontius's wording to the Acta and presents the two as agreeing witnesses.**
  - Text: `In both texts the sentence calls Cyprian a standard-bearer of the sect and an enemy of the gods. With his blood, it says, discipline would be made firm.`
  - Fails against:
    - The Acta's sentence (Knopf 4902-4909) calls him *nequissimorum criminum auctor et signifer*, "author and standard-bearer of most wicked crimes", and *inimicum ... diis Romanis*, an enemy of the Roman gods. "Of the sect" is Pontius's (§17, ANF 28235). The Acta's only *sectam* is the emperors' own rites (*ad sectam caeremoniarum suarum*).
    - The record's `text` says the Acta gives the sentence "in nearly the same words", and that "On the sentence the two texts are not independent witnesses."
    - The quote record `a-standard-bearer-of-the-sect` not_for: "a claim that Pontius and the Acta are independent witnesses to the wording of the sentence".
  - "In both texts ... calls" drops "nearly" and states the wording as shared. Without the non-independence clause, a reader takes the agreement as two witnesses confirming each other.
  - **Replacement** (FK 5.0 / FRE 76.8; sentences 17, 12, 10, 10, 9 words): `Pontius says the sentence called Cyprian a standard-bearer of the sect and an enemy of the gods. With his blood, it said, discipline would begin to be made firm. The Acta gives the sentence in nearly the same words. On the sentence, the two texts are not independent witnesses. Only the Acta gives his answer: "Thanks be to God."` This replaces the paragraph that runs from `In both texts` through `"Thanks be to God."`.

- **P2-1 (`lpc.story.election-of-cyprian`, `telling`, paragraph 1): "He passed over most of Cyprian's early years".**
  - Pontius §2 passes over only the years before conversion ("these things I pass over"). §2-4 then tell his early Christian years at length: continence, the sale of his estates, the presbyterate, Caecilius. What §5 says is "It would be tedious to go through individual circumstances ... this one thing is enough" (ANF 27707 and 27815-27818). The record's `text` has the same slip, but it is not voiced.
  - **Replacement for the second sentence:** `He said it would take too long to tell all that Cyprian did, and that one fact was proof enough of his good works.` (24 words, FK 6.6 / FRE 90.8.)

- **P2-2 (`lpc.story.celerinus-writes-to-lucian`, `telling`, paragraph 2): the sister is grieved, but the plea for her is left out.**
  - In Ep. XX §2 (ANF 30580-30588), Celerinus weeps "until ... affection manifested through you, or through those my lords who have been crowned, from whom you are about to ask it, shall come to the help of so terrible a shipwreck." The telling's "He also asked the martyrs' pardon for two women" can read as if he asked only for the two. The `tellable_as` ("to seek peace for his sister and two other women") and `use_note.means` both include her. The earlier review's P1-1 was about exactly this undercount in the voiced fields.
  - **Fix:** after `She was still alive in body.`, insert `He would weep, he said, until help came through Lucian or through the martyrs Lucian would ask.` (17 words.)

- **P2-3 (`lpc.story.the-death-of-cyprian`): the length is not a defect. Do not cut to make room for P1-1.** Recorded so the fix does not trade the cloths paragraph or the "only Pontius" paragraph for words.

## Part A: the author's six problems in the story records

None of them blocks a telling. Each telling either avoids the defect or rests on support that exists.

| # | Problem | Real? | Blocks the telling? |
|---|---|---|---|
| 1 | Plague `text`: "strangers as well as His own" | **Real.** Hartel's apparatus gives *sed etiam alienis* as *v* only (40869). The story `text` does not flag it, though the quote record does. | No. The telling says only "not only to His own people". |
| 1b | Plague `text`: "bodies left where they fell" | Real but small. Pontius says corpses lay over the whole city; "left where they fell" is a gloss, and `modern_contrast` repeats it. | No. The telling quotes the rendering. |
| 2 | Numidicus has no note of the variant | Real but small. The quote record's `divergence_note` and not_for carry it. | No. The telling names the variant. |
| 3a | Election `tellable_as` FRE 58.4 | Real (gate figure). | No. |
| 3b | Ep. XXXIX is used but not in `sources` | **Real.** Only Ep. LXVII is listed. The quote record `ancient-venom-against-my-episcopate` carries the locus. | No. Add the source row to the story. |
| 3c | "he says so himself" is unsupported | **Partly wrong.** It is not in §5, but Pontius §1 says he writes so the "honour of his deserts" is recorded and calls himself unequal to it (ANF 27680-27692). It needs a §1 locus, not a deletion. | No. |
| 4a | Celerinus "had been imprisoned" | Real as a citation gap only. Documented in Ep. XXXIII (ANF 31984), which is not in the story's `sources`. | No. Add Ep. XXXIII to `sources`. |
| 4b, 5 | Two `claim_guards` fail GUARD_MARKERS | Real (gate). | No. |
| 6 | Psalms "by the Vandals" | Real but small. Possidius ch. 28 names Vandals and Alans with some Goths (3982); "the Vandals" is the usual short form, and the doorway uses it too. | No. |

Items 1, 3b, 3c and 4a belong in `Open_Gaps_Tracking.md` as record fixes, separate from the tellings.

## Part B: targeted recheck of `Public_Face_Review_2026-10-27.md`

| Item | Result | Evidence |
|---|---|---|
| P1-1 `safety_adjacent` | PASS | `safety_adjacent: true` is restored after `thinness_statement`. |
| P1-2 `living_traditions` / `horizon` | Left open, acceptable for now (P2-B2) | `living_traditions` matches s21 `LIVING_TRADITIONS` exactly. `horizon` is unchanged in the record and in s21 (lines 4088-4090). No ruling is logged. |
| P1-3 `Catholics` alias | PASS on content; length P2-B1 | The gloss is right and `kind: own` is kept. "Latin Pastoral Congregations" is gone. |
| P2-1 Church splits | PASS | Applied word for word. |
| P2-2 doorway | PASS | Applied in `doorway_description`. The page's `<p class="tile">` equals it exactly after unescaping. |
| P2-3 Money | PASS | Applied word for word. |
| P2-4 Caring for the sick | PASS | Applied word for word. |
| P2-5 Martyrs | PASS | Applied word for word. |
| P2-6 scholarly alias | PASS | Dropped. |
| P2-7 thinness | PASS | Applied word for word. |
| P2-8 notes | PASS | Sin, Bible and Emperor are word for word. Marriage reads "in three ways, for children, faithfulness and its sacrament", which keeps the meaning of the review's colon list. |
| P2-9 `living_traditions` sentence 8 | PASS | The "likeness ... not as a warrant" sentence is deleted from the record and from s21. |

- **Page.** The first `<img>` is `../assets/portraits/datus.jpg`. Wittenberg, Nikolaus and Luther: 0 matches. The talk and table links carry `worlds=latin-pastoral-congregational-christianity`, which equals `census_id`. `../tree/latin-pastoral-congregational-christianity.html` exists. The page does not yet show the tellings; "Read the full account" sits over `tellable_as`, so the tellings reach the page only on a later regeneration.
- **Gates.** `python -m engine.m1.cross_world`: 0 new defects, 6 accepted-open, 223 observations, none for lpc. `python -m engine.m6.cli check`: `"pass": true`, `"changes": []`.
- **New notes.** All 15 topic notes are 12 to 14 words. Together they score FK 7.5 / FRE 61.4, which passes. Each new note matches the record the round-1 review traced. The alias note is 16 words (P2-B1).

## Part B: findings

- **P2-B1 (`records/worlds/lpc.yaml`, `card.aliases[0].note`): 16 words, over the 14-word note length.**
  - Every other world's alias note is 14 or fewer (alx 13, cappadocian 14, don 13, pahc 14, syr 14). The round-1 replacement was itself 15 words, though that review called it 14.
  - Current: `Their own word for the church in communion across the world, not today's Roman Catholic Church.`
  - **Replacement (13 words, FK 7.6 / FRE 63.5):** `Their word for the church in communion worldwide, not today's Roman Catholic Church.` `kind: own` already says it is their own word.
- **P2-B2 (`Open_Gaps_Tracking.md` OG-92): the open item describes a state that has since changed.**
  - OG-92 asks "whether the confirmed Living Tradition Status ... moves into `world_core.living_traditions`". Commit 734de2d4 has since filled that field, and the voice reads it beside the unchanged `horizon` paragraph.
  - Leaving `horizon` as it is, pending the project lead, is acceptable for now. Both statements name no heir, judge no later dispute and speak for no church, and the risk against caution 16 is a duplicate rather than a false claim.
  - It is acceptable only if the record says so. **Fix:** append to OG-92, dated, that `living_traditions` is now filled with the adopted wording (P2-9 applied), that `horizon` still carries the older paragraph, and that the project lead's ruling covers both: keep, move or remove. Promotion stays his call through the runbook in any case.

## Verdict

- **Part A: Revise.** Apply P1-1 (the sentence paragraph of the death telling), P2-1 and P2-2. Round 2 is a targeted recheck of those three paragraphs only. The other four tellings (Numidicus, captives, plague, psalms) are approved to proceed. Log the record-side items 1, 3b, 3c and 4a in `Open_Gaps_Tracking.md`.
- **Part B: Approved to proceed.** Apply P2-B1 and P2-B2. Neither needs another review round. Rebuild and re-pin after the tellings and the world_core edits, under the default action for a `records/` edit.

## Round 2: targeted recheck (2026-10-27)

**Verdict: Approved to proceed.** No new findings.

| Item | Result | Evidence |
|---|---|---|
| P1-1 death telling, paragraph 3 | PASS | The replacement is applied word for word. "In both texts" is gone. "Nearly the same words" and the non-independence sentence are present. |
| P2-1 election telling, paragraph 1 | PASS | The second sentence is replaced word for word. |
| P2-2 Celerinus telling, paragraph 2 | PASS | The sentence is inserted word for word after `She was still alive in body.` |
| P2-B1 `card.aliases[0].note` | PASS | Replaced word for word: 13 words, FK 7.6 / FRE 63.5. `kind: own` is kept. |

- **Scope.** `git diff HEAD` touches only these four lines. Each file parses. Against HEAD, only `telling` changed in each story record, and only the alias note in `lpc.yaml`. Speech, `text`, `absent_detail`, limits and guards are unchanged.
- **Readability** (`engine.m1.gates.grade_text`, whole telling). Death: FK 6.1 / FRE 74.4, longest sentence 22 words. Election: FK 6.2 / FRE 75.2, longest 24. Celerinus: FK 5.2 / FRE 80.4, longest 22. All pass.
