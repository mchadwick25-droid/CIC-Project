# Card check: Tertullian (`tertullian-s-voice`)

Batch 7, 2026-11-20. Card checker; I wrote neither the card nor the brief. New card: every field was checked against its evidence in `Card_Edits.md` and against the entry's own fields. I re-opened each cited line in its file. The validator was not run.

**Verdict: FIX** (7 changes below, one with two companion readings for `tools/quote_scan_readings.json`).

## 1. Each field against its evidence

Confirmed at the cited lines: `otherNames` (JERL 55610, AUG 2827, LACT 22707, Fotheringham 43480-43481); `knownFor`; `datesNote` (EUS-ed 10241-10250 and 10294-10303, ANF3-ed 1443-1446, MON 17071-17076, 17147-17163, 17245-17249, 17460-17469, JER 40514-40516); `placeNote` (JER 40496, EUS 10279-10280); `role`; `keyWorks`; `legacy` (JERL 55618-55626, BEN 2385-2390 and 40588-40593, JER 40895-40897, HARN 22546-22548, NPNF9-ed 427-430, AUG 2827-2835, LACT 22707-22710, LACT-E 4569, VIN 13555-13580, JER 40497); `uncertain` items 1-14 (MON 15478-15500 and 15568-15590, ANF4 17040-17042 and 17128-17141, ANF2-ed 8993-8997, VIN-ed 13538-13550 and 13575-13576, MANSI8 17218-17252, ANF3 59448-59450). No field contradicts the entry's `sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`, `dates` or `placeLabel`; the conflicts listed in `Card_Edits.md` are real and are handled under `uncertain`, not repeated.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

One part of one entry names something the brief does not tell (FIX 6). Remaining, all told in the brief: Apology 1 (hidden road, condemned unknown, about 197); Eusebius on Roman law, Jerome on Carthage, Vincent on first place among the Latins (after FIX 6); Augustine, On Heresies 86 (Tertullianists, named a heretic); Apology 40 and 50; Prescription 15, 19, 21, 36, 37; Against Praxeas 1, On Monogamy, On Fasting, Monceaux on Flight, Jerome and Augustine on the turn; Against Praxeas 1, 2, 12 and the three words; On Modesty and Monceaux's dating; Jerome Lives 70 with Harnack, Lives 53 on Cyprian, Lactantius V.4; Augustine on the basilica, Jerome on old age, McGiffert on the sources; the tradition.

## 4. Census rules

Keys allowed; no `briefLength`; no `secondReading` (left to that step). Nine spans in the brief, nine entries, none for a span the brief no longer quotes. Every `printed` and `original` stands verbatim at its lines (checked by hand and by the fold rule), and every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. American spelling throughout. One sentence of process narration (FIX 5).

## 5. Originals, ruled under the batch 6 rule

| # | Span | Ruling |
|---|---|---|
| 0 | hidden road of silent writing | **Leave out** (as the card does). OEH1 11256-11257 prints "liceat yeritati yel oc- / cnlta yia"; no held print confirms. But the `uncertain` prints the corrected Latin anyway, which supplies the text from knowledge: FIX 1. |
| 1 | not to be condemned unknown | **Leave out** (as the card does). OEH1 11261 "damneUir"; no confirming print. |
| 2 | the blood of Christians is seed | **Keep as it stands.** OEH1 30954-30955 "semen est sanguis / Christianorum" is clean. |
| 3 | Marcion ... springs | **Leave out** (as the card does). OEH2 2284-2285: "Mardon", "iMtes meoB Iransyertb"; no confirming print. |
| 4 | This property is mine | **Leave out** (as the card does). OEH2 2288-2289: "*prisr poBBideo". |
| 5 | I am the heir of the apostles | **Keep; the card left it out.** OEH2 2289 prints "Ego  sum  haeres  apostolorum." cleanly. The outline renders this span from that Latin (Outline 76). The card's note gives it as "heres", which is not what the page prints: FIX 2. |
| 6 | Against Praxeas 12 | **Keep, with one reading and one stray mark; the card left it out.** KRO 12558-12561: "alium autem quomodo accipere debeas, iam professus sum, personae, non substantiae nomine, ad distmccionem, non ad diuisionem. ceterum, (etsi) ubique 20 teneo unam substantiam in tribus cohaerentibus". "distmccionem" reads distinctionem: Oehler prints "ad distin- / ctionem" (OEH2 43866-43867). The "20" is Kroymann's margin line number. Oehler's other difference (teneam, no etsi) is a different reading between editions, already recorded in the entry's `uncertain`, not a scan fault. The card's reason for leaving it out (no entry in the scan-readings file) is not a reason under the rule; batch 6 added such entries (Kroymann 9633-9652). The outline renders this span from Kroymann (Outline 77): FIX 3. |
| 7 | not the church which consists of a number of bishops | **Keep as it stands.** CSEL20 15313-15314 clean. |
| 8 | Give me the master | **Keep as it stands.** JERL 55625 "Da magistrum" clean. |

No Greek on this card.

## 6. Not-found claims

All upheld: "sacramentum" not shown in the held sources; "never made a saint" and "never quite belonged anywhere" have no held source; no source gives 220 or his death; no year of conversion in his own words. One thing left in that should not be: the outline says that if the card gives Vincent, it gives his "trial" as well as his praise (Outline 155); the card gives his praise and "more eloquent than faithful" but drops the "trial" (VIN 13580): FIX 7.

## FIXes

**FIX 1.** `quotationOriginals[0].uncertain`
- Old: `The Latin, liceat veritati vel occulta via tacitarum litterarum ad aures vestras pervenire, is held only in a damaged scan, so the English stands alone. The modern wording follows the Latin: silent writing is tacitarum litterarum, where Thelwall has a noiseless book.`
- New: `The Latin is held only in a damaged scan, so the English stands alone. The modern wording follows the Latin: silent writing is tacitarum litterarum, where Thelwall has a noiseless book.`

**FIX 2.** `quotationOriginals[5]`: add three keys and remove `uncertain`.
- Add: `"original": "Ego sum haeres apostolorum"`, `"originalFile": "cic/texts/tertullian_quae-supersunt-t2-polemica-lat_oehler1853.txt"`, `"originalLines": "2289"` (the file is already in `sources.ownWords`).
- Remove `uncertain`, old: `The Latin, Ego sum heres apostolorum, is held only in a damaged scan, so the English stands alone.`

**FIX 3.** `quotationOriginals[6]`: add three keys and change `uncertain`.
- Add: `"original": "alium autem quomodo accipere debeas, iam professus sum, personae, non substantiae nomine, ad distinctionem, non ad diuisionem. ceterum, (etsi) ubique teneo unam substantiam in tribus cohaerentibus"`, `"originalFile": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt"`, `"originalLines": "12558-12561"`.
- `uncertain` old: `the modern wording follows Kroymann. The card prints the English alone because Kroymann's scan misreads one word inside the span. The brief stops`
- `uncertain` new: `the modern wording and the Latin given here follow Kroymann. Kroymann's scan misreads distinctionem, which Oehler's print confirms. The brief stops`
- Companion entries for `tools/quote_scan_readings.json` (outside the card; the coordinator adds them):
  - `{"file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt", "lines": "12560", "scan": "distmccionem", "reads": "distinctionem", "kind": "OCR misread; Oehler prints distin-ctionem (tertullian_quae-supersunt-t2-polemica-lat_oehler1853.txt, lines 43866-43867)"}`
  - `{"file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt", "lines": "12560", "scan": "ubique  20", "reads": "ubique", "kind": "line number run into the line"}`

**FIX 4.** `uncertain[14]`
- Old: `no other held print confirms them, so these quotations are printed in English alone. For Against Praxeas`
- New: `no other held print confirms them, so these quotations are printed in English alone, except two short lines the scan prints cleanly, the blood of Christians is seed and I am the heir of the apostles, which carry the Latin. For Against Praxeas`

**FIX 5.** `uncertain[5]`
- Old: `which would make it older. For this reason the card says foremost, not first.`
- New: `which would make it older.`

**FIX 6.** `briefReferences[1]`
- Old: `Jerome, Lives of Illustrious Men 53: Carthage, and chief of the Latin writers after Victor and Apollonius.`
- New: `Jerome, Lives of Illustrious Men 53: Carthage. Vincent of Lérins, Commonitory 18: the first place among the Latins.`
- Why: the brief does not tell Jerome's order after Victor and Apollonius; its "foremost" rests on Vincent (VIN 13555-13557), per `Card_Edits.md`.

**FIX 7.** `legacy.remembered[2]`
- Old: `then calls him more eloquent than faithful, and quotes Hilary that by his subsequent error he detracted from the authority of his approved writings.`
- New: `then calls him more eloquent than faithful, quotes Hilary that by his subsequent error he detracted from the authority of his approved writings, and says he was a great trial in the Church.`
