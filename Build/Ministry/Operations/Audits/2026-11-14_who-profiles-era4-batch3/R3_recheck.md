# R3 recheck: era 4 batch 3

Round 3, the last, is a targeted recheck by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. It covers all eight profiles and the README.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git write and no web, paid or model call, and used local scripts and read-only git only. Inputs: the review brief, `R1_review.md`, `R1_changes.md`, `R2_recheck.md`, `R2_changes.md`, era 4 batch 1's `R3_recheck.md` for form, and `git diff 4f7aa7ad bc1bad6f` over `Who-Profiles/era4/batch3/` (word diff for briefs and cards, line diff for `records.json`). The merge commit 89e69fb1 changes nothing in this folder, so the working tree matches bc1bad6f.

For every R2 finding and every string changed in bc1bad6f, I opened the cited lines again in the vendored file under `cic/texts/` and read them in context, folding OCR noise, double spaces, hyphen breaks and Migne's interleaved columns. I then read each brief and card whole, as a participant would, and checked its sentences against their lines, including sentences earlier rounds passed. Short names as in R2: GILES (Giles/Jane 1903), RAINE (Raine 1879), ALC (Alcuin PL 100-101), KYLIE, WHITE (White 1920), STOKES (Stokes 1887), PL72, AASS3 (Acta Sanctorum March 3), LP1 (Duchesne, Liber pontificalis I).

---

## 1. R2 findings

| Finding | Verdict | Evidence |
|---|---|---|
| R2-B1 (Cuthbert `uncertain` 7, false absence) | RESOLVED on the card | The false absence is gone. "Abbas Eata cum Cuthberto et ceteris, quos secum adduxerat, Fratribus domum repulsus est" (AASS3 l.34679-34684); the founding, "tollens idem Abbas quosdam e Fratibus secum, in quibus et Cuthbertum" (l.34606-34612); the History's "would rather quit the place than adopt the catholic Easter" (GILES l.13996-14001); the Bollandists' "SS. Eata, Cuthbertus aliique propter Pascha Catholicum ceterosque ritus reliquerunt Riponense monasterium" (AASS3 l.33599-33601). V.19 is now in the History's source title (GILES l.13848, 13990-14001). `place` keeps the bare "Ripon", as R2 allowed. The new records note brings a new false absence (R3-M2), and the card's "sent home" softens "repulsus" (R3-M1). |
| R2-M1 (Theodore `keyWorks` 1) | RESOLVED | "Among them are Easter, …" Bede's ten chapters are at GILES l.9311-9356. Six are named, and "Among them" no longer claims all. |
| R2-M2 (Wilfrid "Bede is briefer.") | RESOLVED | "Bede tells it more briefly." "It" is the Life of the sentence before. Brief and audio match. |
| R2-M3 (Wilfrid return; Alfrid apposition) | RESOLVED | "Returning to England, he was admitted to the friendship of King Alfrid … the monastery, of thirty families, at the place called Ripon" (GILES l.13990-13996). This Alfrid is Oswy's son: "King Oswy and his son Alfrid" (l.7727, 7924-7925). "son of King Oswy of the Northumbrians" now makes Oswy the king. |
| R2-M4 (Muirchu nested sentence) | RESOLVED | "There is evidence that Aedh visited Armagh, and made a formal submission to the primatial claims of its bishop; and it is probable that Muirchu's Life … was inspired by a desire to offer a literary tribute from Leinster to Armagh" (WHITE l.3772-3778). "White says" carries the witness, and "probably" keeps White's hedge. 13 and 13 words. |
| R2-M5 (double stop) | RESOLVED | One full stop. |
| R2-M6 (Loiguire believed) | RESOLVED | "King Loiguire said to them, It is better for me to believe than to die. And after taking counsel, he believed on that day, by the advice of his friends" (WHITE l.4739-4742). "the elders and all his senate" (l.4738) backs "his elders". |
| R2-M7 (Muirchu stock opener) | RESOLVED | `uncertain` 1 opens "Muirchu says almost nothing about himself.", the brief P3 caveat word for word. |
| R2-M8 (Tirechan stock opener) | RESOLVED | "Tirechan tells little of himself." matches the brief P3 caveat. |
| R2-M9 (Tirechan "latest") | RESOLVED | "post mortalitates nouissimas" (STOKES l.3188-3189); "the latest plagues" in `dates`, `uncertain` 2 and 6. |
| R2-M10 (verbless sentence) | RESOLVED | "This note is not part of the work of Tirechan; but was probably due to the scribe of A, Ferdomnach" (WHITE l.7417-7418). The verb is in. |
| R2-M11 (Clonmacnois witness) | RESOLVED | WHITE l.8554: "St. Ciaran of Clonmacnois. By R. A. S. Macalister." in the series list. The claim now names Macalister's title. |
| R2-M12 (Kildare walls) | RESOLVED for the source | "decorata pictis tabulatis"; "in quo unus paries decoratus, et imaginibus depictus" (PL72 l.59429-59432). The new "it" has no clear antecedent (R3-M3). |
| R2-M13 (Cogitosus "writer … wrote") | RESOLVED | "The writer was Cogitosus. His Latin Life of Brigid of Kildare is a saint's Life, mostly miracles." The card's `uncertain` 1 still matches. |
| R2-M14 (Stokes's reasoning) | RESOLVED | Both index entries point to p.269: "Cogitosus (A.I). 800-835), 269." (STOKES l.21226) and "Coguitosus, 269." (l.22198). The held file starts partway into the Life, at "NOTES BY MUIRCHU" p.2 of the text (l.222), so p.269 is not in it. No other vendored file holds a Stokes note on Cogitosus (a search of all `cic/texts/` for "cogitos" finds only PL72, WHITE, STOKES and stray Latin forms of *cogitare*). |
| A-M22 (README call; Decision-Log) | PARTLY, coordinator step | `R1_changes.md` l.34 now reads "is to be logged". `Decision-Log.md` still has no era 4 batch 3 entry. `R2_changes.md` says it is written at merge. Nothing more is due in the profile files. |
| B-M6 (Muirchu `keyWorks` double stop) | RESOLVED | Done with R2-M5. |
| B-M29 (Cuthbert, Ripon not used) | RESOLVED | The item is on the card, V.19 is in the source title, and `place` keeps "Ripon" with the reason in `uncertain` 7. |

---

## 2. New findings

### Blocking

None.

### Minor

- **R3-M1 MINOR (Cuthbert card `uncertain` 7; items 1 and 9; participant text).** Two small faults in the R2-B1 wording.
  - "both were later sent home" softens the Life's "domum repulsus est" (AASS3 l.34681-34682), which is "driven back home". The item exists to set the Life's expulsion beside the History's Easter reason, so the force of the verb matters.
  - "His History" comes straight after a sentence whose last-named men are Eata and Cuthbert, so "His" can be heard as Cuthbert's. Cuthbert wrote no History.
  - Fix: "Ripon. Bede's prose Life says Eata took Cuthbert to found a monastery at Ripon, and that both were later sent home. His History says the founders left rather than take the Roman Easter. The Bollandists join the two accounts." -> "Ripon. Bede's prose Life says Eata took Cuthbert to found a monastery at Ripon, and that both were later driven home. Bede's History says the founders left rather than take the Roman Easter. The Bollandists join the two accounts." (20, 12 and 6 words.)

- **R3-M2 MINOR (Cuthbert `records.json`, claim "Ripon in Bede's prose Life"; item 1; a false absence in the records, not in participant text).** The R2 fix added "the Bollandists alone join this to the History's Easter reason". James Raine joins them too. His note to Stephen's chapter 8 reads: "Ripon, where Alchfrid had founded a monastery, which he had given in the first instance to Eata, abbot of Melrose. When the Scottish party refused to give up their anti-catholic views, Alchfrid removed them, and gave Ripon to Wilfrid. See Beda's Life of Cuthbert, capp. vii." (RAINE l.4986-4995.) Raine does not name Cuthbert, but he cites the Life of Cuthbert for it. The card's "The Bollandists join the two accounts" says no "only" and stands.
  - Fix, records: "the Bollandists alone join this to the History's Easter reason" -> "the Bollandists join this to the History's Easter reason; so does James Raine's note to Stephen's chapter 8, citing Bede's Life of Cuthbert: \"When the Scottish party refused to give up their anti-catholic views, Alchfrid removed them\"", and add "RAINE (byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt) l.4986-4995" to the witness. Keep Inferential-Thin.

- **R3-M3 MINOR (Cogitosus brief P1 and audio; item 4; participant text).** "Painted boards adorned it, and one wall bore pictures." The R2-M12 fix put "it" two sentences away from "the great church". The nearest singular nouns are "the altar" and "the other" tomb, so a listener can hear the boards as on the altar or the tomb. Cogitosus has the church itself "decorata pictis tabulatis" (PL72 l.59429). Fix: "Painted boards adorned it, and one wall bore pictures." -> "Painted boards adorned the church, and one wall bore pictures." (+1 word.) Carry it into `audio/cogitosus.audio.txt`.

- **R3-M4 MINOR (README; internal, but every statement must be true).** "All eight run 327 to 341 words, about 2:00 to 2:06." The R2 fixes made Wilfrid 346 words (2:08) and Cogitosus 326 (2:01). Fix, with R3-M3 applied (Cogitosus 327): "All eight run 327 to 341 words, about 2:00 to 2:06." -> "All eight run 327 to 346 words, about 2:01 to 2:08." Without R3-M3: "… 326 to 346 words, about 2:01 to 2:08."

Considered, and not a finding:
- Willibrord brief P6, "the patron saints of many cities, from Rome to Paris". Alcuin's list goes on past Paris to Reims and Champagne (ALC l.56116-56122). "From Rome to Paris" is a span, it names no picked list, and R2 accepted it under A-M8. Changing it would be a wording preference.
- Muirchu brief P5 drops White's "There is evidence that" before Aedh's submission. "White says" names the witness, and the card's `uncertain` 5 gives his fuller wording. Not misleading.
- Cogitosus brief P6, "asking the brothers to pray". Cogitosus asks pardon of "fratribus et lectoribus" and then "Orate pro me" (PL72 l.59494-59502). The brothers are among those he asks. True.

---

## Changed strings checked

Every string changed in bc1bad6f, against its lines:

| File, field | Result |
|---|---|
| theodore card `keyWorks` 1 | PASS (GILES l.9311-9356) |
| wilfrid brief P2 last sentence, and audio | PASS |
| wilfrid brief P3 last sentence, and audio | PASS (GILES l.7727, 13990-13996) |
| muirchu brief P5, and audio | PASS (WHITE l.3772-3778) |
| muirchu card `keyWorks` 1 | PASS |
| muirchu card `uncertain` 1 | PASS (matches brief P3) |
| muirchu card `uncertain` 7 | PASS (WHITE l.4738-4742) |
| tirechan card `uncertain` 1, 2, 4 | PASS (STOKES l.3188-3189; WHITE l.7417-7418) |
| tirechan records, Clonmacnois claim | PASS (WHITE l.8554) |
| cogitosus brief P1, and audio | PASS for the source; antecedent fault (R3-M3) |
| cogitosus brief P2, and audio | PASS |
| cogitosus card `uncertain` 5 | PASS (STOKES l.21226, 22198, 222) |
| cuthbert card `uncertain` 7 | PASS for the false absence; R3-M1 |
| cuthbert card `sources.about` 1 title | PASS (GILES V.19 at l.13848) |
| cuthbert records, Ripon claim | Quotation PASS (AASS3 l.34679-34684); "alone" fails (R3-M2) |

In the changed strings: every witness is attached; White's "probably" and "probable" hedges are kept; pronouns resolve except the one in R3-M3 and the "His" in R3-M1; the one changed quotation (records) is verbatim; there is no new AI tell, contrast frame, beat line or colon reveal. "The Bollandists join the two accounts" closes an item but carries a fact. No changed sentence runs past 25 words (longest: 20).

---

## Mechanical checks

By script, on the files as they stand.

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card order, no empty or null field | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| theodore-of-tarsus | 329 | 2:02 | 6.1 | 72.2 | yes (1 calmly, 1 warmly) | yes | 22 |
| willibrord | 332 | 2:03 | 6.4 | 74.4 | yes | yes | 25 |
| leoba | 337 | 2:05 | 6.8 | 71.4 | yes | yes | 25 |
| wilfrid-of-ripon | 346 | 2:08 | 5.8 | 77.8 | yes | yes | 23 |
| muirchu | 338 | 2:05 | 6.1 | 75.2 | yes | yes | 21 |
| tirechan | 336 | 2:04 | 7.5 | 67.9 | yes | yes | 25 |
| cogitosus | 326 | 2:01 | 7.9 | 64.8 | yes | yes | 21 |
| cuthbert-of-lindisfarne | 335 | 2:04 | 5.8 | 79.1 | yes | yes | 21 |

- All eight pass `grade_text` (FK 10 or below, Flesch 60 or above). Cogitosus with R3-M3 applied, scored on a scratch copy: 327 words, FK 7.9, Flesch 64.9.
- Each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, one of each. No tag is in a brief or card.
- Every card parses as JSON and its keys run in Mark's order (`name`, `otherNames` where held, `knownFor`, `dates`, `place`, `tradition`, `role`, `briefLength`, `keyWorks` where held, `legacy`, `uncertain`, `sources`). Tirechan and Cogitosus have no `otherNames`, and Cuthbert has no `keyWorks`. Those fields are absent, as they should be, never empty.
- No card sentence outside `sources` runs past 25 words.
- Every quotation in the eight briefs and cards matches its listed source file once whitespace, case, punctuation and hyphen breaks are folded. Two need a closer look, and both pass: "row-boat", which the file breaks at the hyphen (WHITE l.3801-3802), and "nepote culpabili", where the OCR reads "culpabiH" (PL72 l.59502).
- In `records.json` every `formation_confidence` is one of the five levels. Every `contested_claim` gives at least two sides.

---

## Each brief read whole

I read each brief as a participant would, top to bottom, and then each card, against checklist items 1-14.

- **Theodore of Tarsus.** It opens on Pope Vitalian's search (GILES l.8733-8768), with "venerable for age, being sixty-six years old" and "according to the custom of the Greeks" verbatim. I checked the arrival and tour (l.8834-8846), Hertford (l.9280-9356), 678 (l.9865-9897, 15352-15353), the death at eighty-eight and the "than ever they had done before" line (l.12685-12705). No new fault.
- **Willibrord.** It opens on the calendar note, "quamvis indignus", with 690 and 695 (LP1 l.173618-173629). I checked Duchesne on Bede's figures (l.173613-173636), Fosite's island, the cattle and the silent spring, and the three baptized (ALC l.55163-55260). I also checked the sermon (l.56070-56134). No new fault.
- **Leoba.** I checked the letter (KYLIE l.4510-4567): Dynne "more than eight years since", Aebbe, the only-daughter line, the gift, the homely style, the verses and Eadburga. Kylie's own account is marked as his (l.1184-1205, 1749-1778), and the Torhthat and Tecla letters match (l.4576-4592, 5868-5906). No new fault.
- **Wilfrid of Ripon.** I checked the Roman hearing, "who that Bishop Wilfrid was?" and "near forty years" (GILES l.14105-14124), and the second expulsion "five years after" (l.14073-14081). The South Saxons and "the enmity of the aforesaid king" are at l.9913-9918. The death verse "Emitte spiritum tuum, et creabuntur, et renovabis faciem terre" is in Stephen (RAINE l.10578-10580). Bede's "Undalum" is Oundle in Plummer's index (PLUMMER l.36545). No new fault.
- **Muirchu.** I checked the preface quotations (WHITE l.3790-3812), "the most ancient Life of the Saint now extant" (l.3592-3593), the great plain and the fire (l.4341-4407), Loiguire (l.4738-4742) and 17 March (l.5417-5419). No new fault.
- **Tirechan.** I checked the paruchia passage (STOKES l.2974-3015), White's datings and his purpose for Tirechan (WHITE l.1386-1442), Mount Egli (l.595-597), the daughters of Loiguire (l.7096-7112) and the magician's stone (l.6826-6828). No new fault.
- **Cogitosus.** I checked the church and its two doors (PL72 l.59400-59464), Basnage's note (l.58440-58478), the prologue (l.58482-58500), "caput pene omnium Hiberniensium Ecclesiarum" and the hermit bishop (l.58505-58528), the miracles in the monastery (l.59334-59337) and the signature (l.59494-59502). One fault: R3-M3.
- **Cuthbert of Lindisfarne.** I checked the vision on the hills (AASS3 l.34320-34352), Boisil at the door, "hoc unum dixit adstantibus: Ecce servus Dei", and his being "Praepositus" (l.34440-34447, 34540-34545), and the Tweed (GILES l.11577). The rest of the brief is unchanged since R2 and matches its lines. On the card: R3-M1. In the records: R3-M2.

Each brief still opens on a scene, names its witness at each disputed point, and keeps the source's hedges. None tells a dispute as settled.

---

## 3. Verdicts

| Profile | R2 findings and R1 partlies | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Theodore of Tarsus | R2-M1 resolved | 0 | 0 | CLEAR |
| Willibrord | none | 0 | 0 | CLEAR |
| Leoba | none | 0 | 0 | CLEAR |
| Wilfrid of Ripon | R2-M2, R2-M3 resolved | 0 | 0 | CLEAR |
| Muirchu maccu Machtheni | R2-M4 to R2-M7 and B-M6 resolved | 0 | 0 | CLEAR |
| Tirechan | R2-M8 to R2-M11 resolved | 0 | 0 | CLEAR |
| Cogitosus | R2-M12 to R2-M14 resolved | 0 | 1 (R3-M3) | CLEAR |
| Cuthbert of Lindisfarne | R2-B1 and B-M29 resolved | 0 | 2 (R3-M1; R3-M2, records) | CLEAR |
| README.md | A-M22 partly (Decision-Log entry, coordinator step at merge) | 0 | 1 (R3-M4) | CLEAR for its text once R3-M4 is applied |

**Totals.** Round 2 had 15 findings plus 3 R1 partlies, 18 items in all. Of these, 17 are resolved: R2-B1, R2-M1 to R2-M14, B-M6 and B-M29. A-M22 stays partly, because the Decision-Log entry is still to be written; that is a coordinator step. Round 3 found 0 new blocking findings and 4 new minor ones (R3-M1 to R3-M4). All eight profiles are CLEAR.

**Cap note.** This is round 3, the last of the three review rounds the cap allows on each profile. No blocking finding is open, so nothing has to escalate. R3-M1 (Cuthbert card) and R3-M3 (Cogitosus brief and audio) are participant text. Under the cap, changing them after this round needs a cap ruling from Mark, so they go to him as optional one-line fixes. Each is given above in final wording, checked against its line. R3-M2 (records) and R3-M4 (README) are not participant text. A-M22's Decision-Log entry is the coordinator's step at merge.
