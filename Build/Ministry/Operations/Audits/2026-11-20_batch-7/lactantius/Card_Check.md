# Card check: Lactantius (`lactantius`)

Batch 7, 2026-11-20. Card checker; I wrote neither the card nor the brief. New card: every field was checked against its evidence in `Card_Edits.md` and against the entry's own fields. I re-opened each cited line in its file. The validator was not run.

**Verdict: FIX** (7 changes below).

## 1. Each field against its evidence

Confirmed at the cited lines: `otherNames`; `knownFor`; `datesNote` (JE 41033-41054, MO 24954-24955, 25164-25169, 25872-25876, 25928-25930, 26030-26050, 25190-25191, 25228-25232, 25246-25249, AN-ed 476); `placeNote` (JE 41033-41041, MO 24813-24815, AN-ed 470-476); `role`; `keyWorks`; `legacy` (AU 35552-35555, EU-ed 50239-50242, MO 29258-29282 and 29870-29893, JL 14112-14114 and 19203-19211, TE 11241-11252 and 11465-11492); `uncertain` items 1-12. No field contradicts the entry's own fields beyond the conflicts listed in `Card_Edits.md` (the death year and the address to Constantine), which the card handles under `uncertain`.

Wrong as left in:
- **Jerome on the millennium** (`legacy.remembered[3]`). Jerome's words (JE 39880-39885): those "who say that after the resurrection the Lord will reign in the flesh with the saints", among them Lactantius. "A thousand years on earth" is not in the passage: FIX 1.
- **The lost word after deo** (`quotationOriginals[0].uncertain`). Brandt's apparatus (DI-L, the notes after 23212) reports that Cellarius and Bünemann thought a word such as duce fell out after deo ("post dco fort. duce ... excidisse putant Cellarius et Btienemanum"). The suspicion is theirs, reported by Brandt, not Brandt's own: FIX 2.
- **Fotheringham's lines** (`quotationOriginals[2].uncertain`). Jerome's own entry stands at 44984-44986, not 44985-44987 ("uit, uir omnium suo tempore eloquen-" is 44984; "CCLXXV olymp' plerumque" is 44986): FIX 3.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Four parts name something the brief does not tell: Diocletian and Galerius disputing whether to burn the church (ref 0); "a disciple of Arnobius" (ref 1); the presbyters led to execution "with their families" (ref 2); the thousand-year reign after the six thousand years (ref 4): FIX 4 to FIX 7. Remaining, all told in the brief: Persecutors 12 and Divine Institutes V.2 on the church's fall and his teaching in Bithynia; Jerome, Lives 80 and the Chronicle on Nicomedia, the Greek city, the writing and Crispus; Persecutors 13-15, Eusebius and Constantine on the edict, the fire and the killings; Divine Institutes V.1, V.2, V.4 on the two men, the task, Tertullian, Cyprian and the newcomer; the seven books and V.19-20; Persecutors 33-35, 42 and 48 on Galerius's edict and Milan; the opening and close of the Persecutors, with its dating and authorship; Jerome's Letters 58 and 84 and Augustine; McGiffert and Monceaux.

## 4. Census rules

Keys allowed; no `briefLength`; no `secondReading`. Three spans in the brief, three entries. Every `printed` and `original` stands verbatim at its lines, and every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. American spelling ("honors", "leveling"; "Pretorian" is Hailes's own form, AN 10161).

## 5. Originals, ruled under the batch 6 rule

All Latin; no Greek on this card.

| # | Span | Ruling |
|---|---|---|
| 0 | Spurred on by their proud ungodliness ... | **Keep as it stands.** Brandt 23207-23209 is clean: "et illorum superba inpietate / stimulatus et ueritatis ipsius conscientia et, ut ego arbitror, / deo, suscepi hoc munus". The suspected lost word is an editors' conjecture in the apparatus, not a fault in the print. |
| 1 | Religion must be defended ... | **Keep as it stands.** Brandt 26240-26242 clean. |
| 2 | the most eloquent man of his time ... | **Keep as it stands, as Prosper's copy.** Brandt's TE 11251-11252 (Prosper) is clean; the "20" after the span is a margin number. The card says plainly in `work` that it is Prosper's copy. Jerome's own entry is held twice with the same words: Fotheringham 44984-44986, where "CCLXXV olymp'" is a margin mark (a stray mark under the rule), and Brandt's TE 11241-11243, where the "m" before "tempore" is stray. Either could stand instead with one scan-readings entry; the card's choice is verbatim and honestly labeled, so it stands. Coordinator's option: cite Fotheringham 44984-44986 with a reading that drops "CCLXXV olymp' ". |

## 6. Not-found claims

All upheld: Calvin's "ancient doctor of the Church" letter (entry `legacy`) is on no held source the sheet names; Monceaux dates the Institutes to early 307 to early 311 (MO 25928-25930), not "303 to before 311"; Schanz on the Persecutors at SH 40249-40250 is unreadable, and the card uses SH 39060-39062 instead; the sheet's line corrections hold.

## FIXes

**FIX 1.** `legacy.remembered[3]`
- Old: `Jerome counts him among those who held that Christ would reign a thousand years on earth after the resurrection.`
- New: `Jerome counts him among those who held that after the resurrection the Lord would reign in the flesh with the saints.`

**FIX 2.** `quotationOriginals[0].uncertain`
- Old: `Brandt's apparatus suspects a word lost after deo; the printed text reads as quoted.`
- New: `Brandt's apparatus reports that earlier editors thought a word was lost after deo; the printed text reads as quoted.`

**FIX 3.** `quotationOriginals[2].uncertain`
- Old: `(lines 44985-44987 of that file)`
- New: `(lines 44984-44986 of that file)`

**FIX 4.** `briefReferences[0]`
- Old: `within view of the palace; Diocletian and Galerius disputing whether to burn it; Diocletian fearing the city would burn;`
- New: `within view of the palace; Diocletian fearing the city would burn;`

**FIX 5.** `briefReferences[1]`
- Old: `Jerome, Lives of Illustrious Men 80: a disciple of Arnobius, summoned to Nicomedia`
- New: `Jerome, Lives of Illustrious Men 80: summoned to Nicomedia`

**FIX 6.** `briefReferences[2]`
- Old: `the presbyters led to execution with their families, burned in crowds,`
- New: `the presbyters led to execution, people burned in crowds,`

**FIX 7.** `briefReferences[4]`
- Old: `true worship, and the six thousand years followed by a thousand-year reign.`
- New: `true worship, and the six thousand years.`
