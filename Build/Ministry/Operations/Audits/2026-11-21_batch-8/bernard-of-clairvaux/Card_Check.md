# Card check: Bernard of Clairvaux

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. Read: `bernard-of-clairvaux.brief.txt` (and `brief.v1.txt`, to see what the final brief dropped), `bernard-of-clairvaux.card.json`, `Card_Edits.md`, `Outline.md`, `Review.md`, and each quoted line in its file. There is no starting card: Bernard has no census entry yet.

**Verdict: FIX** (changes below; FIX 1 is the coordinator's call).

## 1. Each field is justified

Every field was checked against the evidence `Card_Edits.md` gives. Spot re-reads at the cited lines:
- placeNote and datesNote: Mabillon's 1091 entry puts his birth "in the castle called Fontaines, near Dijon, in Burgundy" (E1-ed 4360-4363). It stands.
- legacy.traces[2] and briefReferences[8], Hus: Hus quotes On Consideration IV, 1 and says "Pope Eugenius ought to be a vicar in poverty and humility ... following Peter. For that man is a true vicar of him whose place he fills and from whom he has lawfully received the procuratorial power" (HUS 6161-6165). Schaff's note calls it "The most famous book ever written on the papal office" (HUS 6137). Both stand.
- uncertain[10], the Rhine: Letter 365 says only that Ralph "boasts that he is a monk and a hermit" (E2 24272), and the editor's note, from Otto of Freising, says Bernard "brought him at length, by virtue of his vow of obedience, to retire to his" monastery (E2-ed 24259). The card is right that the held texts do not make him a monk of Bernard's own order. The brief says "a monk of his own order"; the review kept that wording as widely held and asked the card to say what the held letter says (Review M4). The card does so. No card change.
- uncertain[9], the crusade's start: one sentence misreads Mabillon. See FIX 5.

## 2. Nothing else moved

Not applicable: new card, no starting card, no existing entry. The tradition-entry differences `Card_Edits.md` lists are the tradition entry's, not this card's.

## 3. References

The final brief dropped "the Valley of Wormwood" and the sermon's number; other references carry source details the brief never told.

**FIX 3.** `briefReferences[0]`
- Old: "William of Saint-Thierry, Life I: Bernard's father Tescelin, a knight; the brothers won one by one; Guy and the boy Nivard in the street. Entry in 1113, the fifteenth year from the founding of Cîteaux. Mabillon's chronology: born at Fontaines in Burgundy."
- New: "William of Saint-Thierry, Life I: Bernard's father Tescelin, a knight; Guy and the boy Nivard in the street. Entry in 1113. Mabillon's chronology: born in Burgundy."
- Why: the brief does not tell the brothers won one by one, the fifteenth year, or Fontaines.

**FIX 4.** `briefReferences[1]`, `[2]`, `[6]` and `[7]`
- [1] Old: "William, Life I: Bernard entered Cîteaux in 1113 with more than thirty companions, under abbot Stephen; the small house..."
- [1] New: "William, Life I: Bernard entered Cîteaux in 1113 with more than thirty companions; the small house..."
- [2] Old: "William, Life I: Clairvaux, an old den of robbers, in the territory of Langres; the abbot sent..."
- [2] New: "William, Life I: Clairvaux, an old den of robbers; the abbot sent..."
- [6] Old: "Bernard, Letters 363 and 365: the Jews must not be persecuted, killed or driven out;"
- [6] New: "Bernard, Letters 363 and 365: the Jews must not be killed or driven out;"
- [7] Old: "William of Tyre: the kings turned back from Damascus in 1148 with nothing done, his rival rumours and his words that he has not found out who was guilty."
- [7] New: "William of Tyre: the kings turned back from Damascus in 1148 with nothing done, his rumors of treachery and his words that he has not found out who was guilty."
- Why: the brief does not name Stephen at Cîteaux, Langres, or persecution, and tells the treachery, not rival rumors. [7] also had British spelling.

References kept as they stand: [3] (Sermon 83 is the quote's source; Calvin, Hus and the tradition entry support "read for centuries"), [4], [5], [8], [9].

## 4. Census rules

Only allowed keys; no `briefLength`. The brief has three quoted spans (paragraphs 1, 7 and 15); the card has three entries, each `modern` word for word as the brief has it. Each `printed` stands at its lines: VP 34743, E4 32161-32164, PL182 75607-75608. Every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. All three spans are six words or more and carry no `secondReading` yet, as the new-card prompt asks.

**FIX 6. American spelling** (none of these is inside printed wording):
- `legacy.traces[3]`: "the wounds of the Saviour" becomes "the wounds of the Savior".
- `uncertain[7]`: "their books burnt wherever found" becomes "their books burned wherever found".
- `uncertain[11]`: "that quarrelling was poured out on the princes" becomes "that quarreling was poured out on the princes"; "gives rival rumours of treachery" becomes "gives rival rumors of treachery".
- `briefReferences[7]`: covered by FIX 4.

## 5. Originals

**FIX 1 (coordinator's call). `quotationOriginals[0]`, Nivard.** The `printed` wording, Alan's "ut vos coelum habeatis, ego terram" (VP 34743), is a different speech. Alan's Nivard says "Cum maledictione ... fiat haec distributio" (VP 34742-34743), "let this division be cursed". The brief's "This is not a fair division" is William's "Non ex aequo divisio haec facta est", and Alan has nothing like it. So the printed words do not stand behind the rendering. William's Latin (VP 16246-16250) reads "rxltiui,ct" for caelum, et, "a:qiio" for aequo and "! xc" for haec. Alan's "coelum" could confirm the first, but no held print confirms "aequo", so William's Latin cannot be printed under the batch 6 ruling, and no English of either Life is held. The census needs a printed wording behind every quoted span. Two choices:
- (a) Take the quotation marks off Nivard's words in the brief (say, Nivard answered that heaven was for them and earth for him, and the division was not fair), and delete `quotationOriginals[0]`. Recommended: it is the only choice that leaves no printed wording standing behind words it does not hold.
- (b) Keep the quotation, and keep Alan's fragment as the nearest held print, with its `uncertain` note as it stands. This leaves "This is not a fair division" with no printed wording behind it.

**FIX 2. `quotationOriginals[2]`, the shield.** The card prints only the first clause, though the rendering covers the whole passage. The passage can be printed in full from PL182 75606-75611. Each of its faults is read from Geoffrey's quotation of the same passage (VP 20932-20937), a parallel held print, as the batch 6 ruling allows:

| PL182 line | Scan | Reads | Confirmed by |
|---|---|---|---|
| 75607 | `feri` | `fieri` | VP 20932, "fieri" |
| 75609 | `mr me` | `tur me` (with "digne-" at 75608: dignetur) | VP 20934, "dignetur" |
| 75610 | `nent'mm linguas maledieas, el` | `hentium linguas maledicas, et` (with "detra-" at 75609: detrahentium) | VP 20935-20936, "detrahentium linguas maledicas, et" |
| 75611 | `blaspüemorum` | `blasphemorum` | VP 20936 "blasphemurum" has the h; PL182 has the o. Each print confirms the letter the other lacks. |

"ut." at 75611 is a stray point; "Libens" after a comma is a matter of case. The coordinator may judge that the last row does not meet the ruling, because no single print shows "blasphemorum" clean. If so, leave this entry as it stands.
- `printed` old: "malo in nos murmur hominum, quam in Deum esse"
- `printed` new: "Etsi necesse sit unum fieri e duobus, malo in nos murmur hominum, quam in Deum esse. Bonum mihi, si dignetur me uti pro clypeo, Libens excipio in me: detrahentium linguas maledicas, et venenata spicula blasphemorum, ut non ad ipsum perveniant."
- `work` old: "Bernard, On Consideration II, 1, first clause of the passage, Latin of PL182"
- `work` new: "Bernard, On Consideration II, 1, Latin of PL182"
- `lines` old: "75607-75608"; new: "75606-75611"
- `uncertain` old: "Only the first clause is printed, because the rest of the passage (PL182 75606-75611, and Geoffrey's quotation of it at VP 20932-20937) stands in two scans that each carry small faults, and no English of On Consideration is held. The rendering follows the Latin for the whole passage; where both scans can be read they agree, except that PL182 begins Etsi necesse sit and Geoffrey begins Si necesse sit."
- `uncertain` new: "The scan of PL182 has small faults in the passage; each is read from Geoffrey's quotation of the same passage (VP 20932-20937), which prints those words cleanly, and blasphemorum, faulty in both scans in different letters, from the two together. The two agree, except that PL182 begins Etsi necesse sit and Geoffrey begins Si necesse sit. No English of On Consideration is held."
- The four readings go to `tools/quote_scan_readings.json` for `cic/texts/bernard-clairvaux_opera-t1-pl182-lat_migne1879.txt`, kind "OCR misread".

**Sermon 83: no change.** The outline renders from PL183's Latin (PL183 105304-105306). "prster" (105304) is a fault for praeter, and no held print confirms it, so the card prints Eales's English (E4 32161-32164) alone. That is right under the ruling.

## 6. Not found, and anything clearly wrong left in

**FIX 5.** `uncertain[9]`
- Old: "Mabillon's chronology tells of a new expedition prepared in 1149 and 1150 from which the Cistercians dissuaded the king."
- New: "Mabillon's chronology says that after his return in 1149 the king was making preparations for a new expedition and the Cistercians dissuaded him, as Abbot Robert's chronicle reports under 1150."
- Why: Mabillon, under 1149, says "When making preparations for a new expedition he was dissuaded by the Cistercians, as Abbot Robert reports in his Chronicle, under A.D. 1150" (E1-ed 5149-5154). He does not say it was prepared in 1150.

Not found, as `Card_Edits.md` lists them. The tradition entry's present-day line is not carried, and that is right: it is not in `cic/texts/`. The year of the canonization is stated in the card as not held, and that is right. William's Latin of Nivard's speech is not printable clean (FIX 1). No other claim in the card is clearly wrong.
