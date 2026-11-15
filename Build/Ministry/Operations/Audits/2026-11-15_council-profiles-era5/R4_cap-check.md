# Era 5 council profiles: targeted check of the cap-ruling fixes

- **Date.** 2026-11-15.
- **Scope.** Under Mark's cap ruling of 2026-11-15 on the era 5 major councils, this checks only the 16 strings changed for ten R3_recheck.md findings: A3-M1, A3-M2, B3-S1, B3-M1 to B3-M5, C3-B1 and C3-S1. It does not count toward the review cap (Mark's cap ruling, 2026-11-15).
- **Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/council-of-clermont-1095.entry.json`, `fourth-lateran-council-1215.entry.json`, `second-council-of-lyon-1274.entry.json`, `records.json`; `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` entry 267 (l.3503). Branch `claude/cft-councils-era5`, commit `1905a305` against `c05725b9`.
- **Reviewer.** A fresh Opus reviewer at full effort, who did not see the drafting or the earlier rounds.
- **Method.** `git diff` was compared with the fix log line by line. Each string was read in its file and against the vendored source lines in `cic/texts/` (grep and small `sed -n` ranges). Sentence lengths were counted by script. No model calls, no network, no paid services. Nothing was edited except this report.

## Summary

| # | Finding | File and field | Verdict |
|---|---|---|---|
| 1 | A3-M1 | Clermont entry, `issue[1]`, `issue[3]`, `issue[4]`, `outcome[7]` | CLEAR |
| 2 | A3-M2 | records.json, Clermont, contested claim "The year", `sides` | CLEAR, with one minor (R4-M1) |
| 3 | B3-S1 | Lateran IV entry, `outcome[7]` | CLEAR |
| 4 | B3-M1 | Lateran IV entry, `uncertain[5]` | CLEAR |
| 5 | B3-M2 | Lateran IV entry, `outcome[5]` | CLEAR |
| 6 | B3-M3 | Lateran IV entry, `attended[5]` | CLEAR |
| 7 | B3-M4 | Lateran IV entry, `calledBy` | CLEAR |
| 8 | B3-M5 | Open-Gaps 267, l.3503 | CLEAR |
| 9 | C3-B1 | Lyon entry, `outcome[7]` | CLEAR |
| 10 | C3-S1 | Lyon entry, `attended[2]` and `people`; records.json, new Lyon claim; Open-Gaps 267 | CLEAR |

**Mechanics.** All 16 strings are in the files exactly as logged. `git diff --stat c05725b9 1905a305` shows the five files (three entries, `records.json` and `Open-Gaps.md`; 20 insertions, 14 deletions) plus the change log `R3_changes.md` in this folder. No other line changed in the five files. All four JSON files parse. Every reader-facing sentence runs 25 words or fewer and ends with a period. The longest is `uncertain[5]` at 25. There is no British spelling in the added lines. "Parastron" and "Bène" no longer occur in any era 5 file or in Open-Gaps.

## 1. A3-M1: CLEAR

- **Text.** `issue[1]`: "Then, William says, fleeing the anger ..." (24 words). `issue[3]`: "The Book of the Popes says Urban had heard of his predecessor's plan. In that telling, Gregory VII had preached ...". `issue[4]`: "In her telling, he proclaimed ..." (24 words). `outcome[7]`: "In his account, it had been granted at Clermont ...".
- **Resolves.** Each second sentence now carries its writer. This matters most for Gregory VII's plan, which is one side of a dispute.
- **Sources.**
  - William of Tyre v1 l.6107: "apud Placentiam celebraverat, imperatoris praedicti indignationem fugiens". The records claim (l.6066-6068, 6106-6108) matches.
  - LP2 l.71356-71360: "Audierat ... praedecessorem suum Gregorium papam praedicasse ... Iherosolimam pro defensione christianae fidei pergere ... quod facere minime potuit quia persecutio Heinrici regis". "His predecessor's plan" is a fair plain word for a journey he preached and could not carry out.
  - Anna: the records claim, l.15648-15666, matches the second sentence.
  - Mansi 21 l.27408-27414 (Baluze; long s written as s): "eandemque peccatorum indulgentiam euntibus ... in Hispaniam concesserunt, quae Orientalis ecclesiae defensoribus concessa fuerat in concilio Claromontano".
- **Writing.** It is plain and has no tells. The added tags ("In her telling", "In his account") do not repeat within one item.

## 2. A3-M2: CLEAR, with one minor (R4-M1)

- **Text.** "... 1096: Lambert of Saint-Omer, a contemporary hand by Duchesne (LP1 l.47694), though the same notice puts Urban's death in 1096 (LP1 l.47699), against 1099 in Duchesne (LP2 l.71346); Migne's heading to the act (PL159 l.74878); another Bollandist note (AASS-JUN5 l.148148-148149); and Baldric's printed ...".
- **Resolves.** The semicolons now close the death clause. Migne, the second Bollandist note and Baldric read as witnesses for a council in 1096, not for a death in 1099.
- **Sources, every citation in the string.**
  - WT l.6066-6067: "millesimo nonagesimo quinto".
  - PL159 l.74964: "ab Incarnatione Domini 1095".
  - CART l.13240-13241 ("ANNUS 1095") and l.13316 ("Data III Kalend. Decembris apud Clarummontem").
  - MIRBT l.11220: "Synode zu Clermont (1095)".
  - LP2 l.71663: "synodes de Clermont (1095)".
  - AASS-JUN5 l.26404: "109S, quo Concilio Claromontano idem Petrus interfuit".
  - LP1 l.47694: "anno dominice incarnationis mxcvi". LP1 l.47699: "Et anno Domini mxcvi obiit". LP2 l.71346: "URBANUS II (1088-1099)".
  - PL159 l.74878: "(Anno 1096.)".
  - PL166 l.77749-77751: "(An. D. 1095) ... pridie Nonarum Aprilium". PL166 l.77773: "anno subsequente 1096) et synodus Arvernis habita est".
  - AASS-JUN5: see R4-M1.
- **R4-M1. Minor (a citation range one line short).** The second Bollandist note is cited at AASS-JUN5 l.148148-148149. Those lines open the sentence ("Gemebat sub duro Saracenorum jugo Palaestina ..."). The year comes on l.148150: "Urbanus II, anno salutis mxcvi in Concilio Claromontano, pro ejusdem liberatione bellum sacrum indixit". The claim is right, but the cited lines do not hold the year. The R3 recheck repeated the short range. It came in with the records file (commit e96e6250), not with this fix.
  - **Fix.** Change "AASS-JUN5 l.148148-148149" to "AASS-JUN5 l.148148-148150" in this `sides` string. No other text changes.

## 3. B3-S1: CLEAR

- **Text.** "Nearly six centuries after the council, it called the meeting a local synod held in the Lateran of Rome in 1215." (21 words.)
- **Resolves.** "After the council" anchors the span to 1215, not to the 1800 printing.
- **Sources.** Pedalion l.7149-7150 (a line break in the OCR joined): "ἡ ἐν Λατεράνῳ τῆς Ῥώμης τοπικὴ σύνοδος. γενομένη κατὰ τὸ ασιε΄. ἔτος ἀπὸ Χριστοῦ" (ασιε΄ = 1215). The editors' address, l.236: "Ἔξεδόθη τὸ πρῶτον ἐν Λειψίᾳ τῆς Σαξωνίας, κατὰ τὸ 1800". From 1215 to 1800 is 585 years, so "nearly six centuries" holds.
- **Writing.** "The council ... the meeting ... in 1215" names the event three ways in one sentence. That is clear and avoids a repeated word. No finding.

## 4. B3-M1: CLEAR

- **Text.** "... give its wording: no one is to found a new religious order." (25 words.)
- **Resolves.** The colon marks the canon's wording as reported, not as a bare command. The facts are unchanged from the round 2 verified text.

## 5. B3-M2: CLEAR

- **Text.** "At Trent, the eighth canon on penance, as Mirbt prints it, names the constitution of the great Lateran council." (19 words.)
- **Resolves.** The witness now covers the first sentence, and the trailing "(Mirbt)" is gone.
- **Source.** Mirbt l.18260 opens canon 8: "8. Si quis dixerit". At l.18263-18264: "aut ad eam non teneri omnes et singulos utriusque sexus Christi fideles iuxta magni concilii Lateranensis Constitutionem semel in anno".

## 6. B3-M3: CLEAR

- **Text.** "One manuscript and Placid Conway's English put this during the Lateran council. The collection's editor, Reichert, dates it to 1215."
- **Resolves.** "The collection's editor" has a clear antecedent.
- **Source.** Vitae Fratrum (Reichert 1896) l.1743, note a: "Hanc visionem accidisse anno 1215 constat ex II red. huius operis". Variant at l.1776-1777: "circa concilium Lateranense anno domini 1215". Reichert edited the Vitae Fratrum.

## 7. B3-M4: CLEAR

- **Text.** "One manuscript of Pulkava's Bohemian chronicle adds a passage, printed in its editor's note." (15 words.)
- **Resolves.** It no longer says a manuscript is printed in a note.
- **Source.** Goll's note, `laurentius-de-brezova_historia-hussitica-lat-ces_goll1893.txt` l.14998-15000: "K tomuto roku klade rk. 3 následující zprávu: Anno Domini MCCXIII epistola a domino papa per orbem mittuntur de concilio convocando, que incipit: Vineam Domini Sabaoth". "Its editor" refers to the chronicle, which is named just before. That is clear.

## 8. B3-M5: CLEAR

- **Text.** Open-Gaps 267, l.3503: "Lateran IV: Almaric, Fulk of Toulouse, ...".
- **Resolves.** It matches the entry's `people` row "Almaric" (NOT SCORED). The line sits inside entry 267, whose own unmerged wording may be corrected before merge.

## 9. C3-B1: CLEAR

- **Text.** "In 1309 Clement V gave the Oxford Franciscans the Sack friars' house (his letter, in the Franciscan bullarium). It was expected soon to fall to the apostolic see under Gregory's constitution. Boniface VIII later set the Augustinian Hermits and the Carmelites on a firm footing, as before the council (Glassberger)."
- **Resolves.** The 1309 grant is credited to Clement V's own letter, not to Glassberger. "(Glassberger)" now covers only the Boniface VIII sentence.
- **Sources.**
  - Bullarium Franciscanum V l.14389-14392: "131. Fratribus Min. Oxonen. concedit locum fratrum de Poenitentia I. C. eis contiguum ... 1309, maii 27, Avinione".
  - l.14403-14410: "locus fratrum de Poenitentia Iesu Christi ... de Oxone eidem loco vestro contiguus a dictis fratribus sit in brevi ut creditur relinquendus, in dispositione sedis apostolicae iuxta tenorem constitutionis a Gregorio pp. X ... in generali concilio Lugdunen. editae remansurus".
  - l.14420-14421: "vobis de speciali gratia concedimus et donamus ... Datum Avenione, VI kalendas iunii" (27 May).
  - The editor's index, l.705, calls it "locum olim fratrum de Sacco", so "the Sack friars" is right.
  - "Gave" plus "expected soon to fall" matches the grant, which takes effect once the friars leave.
  - Glassberger l.7330-7332: "Bonifacius Papa VIII. Ordines Eremitarum sancti Augustini et Carmelitarum statuit lore [esse, OCR] in statu solido, sicut fuerant ante concilium Lugdunense". This matches the records claim at that range.
- **Writing.** Six sentences of 10 to 19 words. The parenthetical names the witness plainly.

## 10. C3-S1: CLEAR

- **Text.** `attended[2]`: "Glassberger names their interpreter as John of Balastri, a Franciscan of Constantinople who knew Greek and Latin. At Lyon he interpreted for the emperor and the Greek prelates." `people` name: "John of Balastri". New records claim at Glassberger l.7359-7362, later narrative, Widely Accepted. Open-Gaps 267: "John of Balastri".
- **Resolves.** Glassberger no longer "names" him Parastron, a form found only in Ducange's note on Gregoras. The second sentence now has a records claim. The name agrees across the entry, the records and Open-Gaps.
- **Sources.**
  - Glassberger l.7251-7253: "per eorum interpretem, fratrem Iohannem de Balastri 4 de Constantinopoli de Ordine Fratrum Minorum, sufficienter in utroque lingua, videlicet graeca et latina, eruditum". So "names", "Balastri", "of Constantinople", "Franciscan" and "Greek and Latin" all hold.
  - The editors' note 4, l.7265: "Alias Palastro". It does not give "Parastron", and the entry no longer claims it does.
  - l.7359-7362: "frater Iohannes de Balaslri Ordinis nostri, tam graeca quam latina lingua sufficienter peritus, pridem in concilio Lugdunensi interpres Imperatoris Graecorum et Praelatorum Graeciae, remissus ab eodem concilio cum Graecis ad Graeciam, Constantinopoli feliciter migravit ad Dominum". The new claim renders every clause and adds nothing. It leaves out the miracles that follow, which is right. Its witness kind and confidence match the other Glassberger narrative claims for Lyon.
- **Noted, no finding.** "Interpreted for the emperor" renders "interpres Imperatoris Graecorum". The emperor acted at Lyon through envoys, and `attended[0]`-`[1]` say so just before this item. So the item does not suggest he was present.

## Result

All ten findings are resolved: A3-M1, A3-M2, B3-S1, B3-M1 to B3-M5, C3-B1 and C3-S1 are CLEAR. There are no blocking or substantial findings. One minor remains, R4-M1: in the `sides` string changed for A3-M2, the second Bollandist note is cited at AASS-JUN5 l.148148-148149, but the year "mxcvi" is on l.148150. The fix is to cite l.148148-148150. This check does not count toward the review cap (Mark's cap ruling, 2026-11-15).
