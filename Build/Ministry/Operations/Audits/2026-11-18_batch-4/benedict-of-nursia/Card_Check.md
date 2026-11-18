# Card check: Benedict of Nursia

Checker, 2026-11-18. Starting card: the census `card` for `benedict-of-nursia` in `cic-website/data/world-census.json`.

**Verdict: FIX** (one `briefReferences` part; one stale `uncertain` item).

## 1. Edits justified

New 1–2 and Clearly wrong 1–7 confirmed. Q3 re-read: GRG 5571-5572 ("for the holy man could not otherwise teach, than himself lived."), AS 80438-80440 ("quia sanctus vir nullo modo potuit aliter docere quam vixit."). Q1 and Q2 re-read at RBE 768-770, RBL 1240-1245, RBE 3960-3961, RBL 9527-9528; their census `secondReading` "same" correctly kept. The Paul the Deacon entry is rightly removed: the brief paraphrases it.

## 2. Nothing else moved

Diff against the census card: only `briefReferences` and `quotationOriginals` changed, each change listed. The apparent shifts are insertions; no existing entry was reordered.

## 3. References that remain

1. II.36: the pointer to the Rule. 2. II prologue: Rome, loose living, the four disciples, "Book II is the only early Life" (**FIX below**), miracles. 3. II.1: Subiaco, the cave. 4. II.3: abbot, poison, glass, twelve houses. 5. II.8: Cassino, Apollo. 6. II.15: Totila. 7. II.37: his death. 8. Rule, Prologue. 9. Rule ch. 48, 64. 10. Rule ch. 53, 58, 73. 11. II.17: the Lombards. 12. Paul the Deacon IV.17. 13. Carloman, 742. 14. Aachen, 802. 15. World census, his tradition (the census's standing placement reference; kept).

## 4. Census rules

Allowed keys only; no `briefLength`. Three quoted spans in the brief, three entries; each `printed` and `original` stands at its lines. All cited files in `sources`. No quotation marks remain in `briefReferences` (the ch. 48 marks rightly removed). No audit named in the card. American spelling ("honor", "labor").

## 5. Not found / left in

No "not found" claims. Left in and clearly wrong: the last `uncertain` item. It explains "the modern English of Benedict's words to Totila" and a modern rendering of Gregory's praise that leaves out "also". Neither the brief nor the card now gives either rendering: the brief paraphrases Totila and does not quote the praise, and `legacy.traces` quotes the 1608 with "also". The note describes text that does not exist, so it contradicts the finished brief. (Open-Gaps, "What release 50 leaves", 2026-11-17, put the question to Mark; this check rules it clearly wrong. Mark may overrule.) The Acta Sanctorum source stays: Q3 now uses it.

## FIX

1. `briefReferences[1]`. The brief nowhere says Book II is the only early Life.
   - Old: `... his four disciples as Gregory's sources. Book II is the only early Life of Benedict, and Gregory tells it to show the miracles of a holy man.`
   - New: `... his four disciples as Gregory's sources. Gregory tells Book II to show the miracles of a holy man.`
2. `uncertain[5]`. Remove the item.
   - Old: `The modern English of Benedict's words to Totila follows Gregory's Latin, "Multa mala facis, multa mala fecisti" (Acta Sanctorum, March, vol. 3), which has no word for "daily"; the 1608 English adds it. Gregory's praise of the Rule likewise leaves out the 1608 "also", which the Latin lacks.`
   - New: (removed)
