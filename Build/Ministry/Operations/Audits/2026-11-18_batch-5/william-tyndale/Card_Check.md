# Card check: William Tyndale (new card)

Checker, 2026-11-18. I did not write this card. Read against `william-tyndale.brief.txt`, `Card_Edits.md`, `Outline.md`, `Source_Sheet.md`, the census entry's own fields and the cited lines in `cic/texts/`.

## Verdict: FIX (one word)

### FIX 1: American spelling

Field `legacy.traces[2]`. The word is card prose, not quoted printed wording (Cranmer's printed "licence", CM 32950, is not quoted here).

- Old: `"In 1537 Thomas Cranmer, archbishop of Canterbury, sent the king's minister an English Bible, saying he liked it better than any translation made before, and asked a licence for it to be sold and read; ...`
- New: `"In 1537 Thomas Cranmer, archbishop of Canterbury, sent the king's minister an English Bible, saying he liked it better than any translation made before, and asked a license for it to be sold and read; ...`

(Only `licence` becomes `license`. The rest of the string stays word for word.)

## 1. Each field against its evidence

Re-read at the cited lines; each holds:
- otherNames: DT 438-440 (Hychins), 828-829 (Hotchens).
- datesNote: 1484 as the editor's probability, DT 377-378; 1524 for leaving, DT 906-909; Cologne 1525 (Cochlaeus), Worms 1526, Marburg 1530 (DT 1665-1677, colophon "MDXXX"); death at Vilvoorde 1536, "[of October 6th]" with the note "Foxe gives this date in his calendar", DT 3328-3331, 3364.
- keyWorks: the 1535 title, DT 3245-3247; the 1534 comparison with the Greek, DT 30039-30042.
- legacy.traces: Henry VIII's "untrue translations to be burned", DT 1221-1252; Cranmer's two letters, CM 32932-32960 and 33055-33060, with Thomas Matthew at the note; Matthew's Bible content, DT 3284-3297; the king's printer before the end of 1536, DT 3338-3344.
- legacy.remembered: "worthily called an apostle of England", DT 3407-3409.
- uncertain: Elyot's letter of 14 March 1532, DT 2189-2199, backs the order to seize him.

Nothing on the card contradicts the brief. No field names an audit, review or ruling.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. Brief references

Each of the 12 entries names something the brief tells. None is removed. They remain as written:
1. Cochlaeus: Cologne, 1525, the press stopped, the flight up the Rhine.
2. Welsh border, Oxford, Cambridge; priest; his reason; no place in all England.
3. Leaving in 1524; the Greek, not the Latin (the 1534 preface's "weeded out faults" is the source's wording of the comparison the brief tells).
4. Worms, merchants, the bishop's thirty days, Luther's sect, the untrue translations.
5. The Obedience; the Practice of Prelates through Vaughan; Foxe's story of the king's praise; the five books from the Hebrew; hypocrites.
6. Vaughan's letters, the minister's verdict and mercy line, the offer (one quotation broken by an ellipsis), no answer held, the order to seize him (DT 2189-2199).
7. The 1534 Testament and its preface.
8. Phillips, Antwerp, Vilvoorde, the emperor's law, the stake, the last cry.
9. Foxe's readers; Maundrel; heresy.
10. Cranmer, 1537; most of it Tyndale's.
11. The 1533 letter to Frith.
12. World census, the English Reformation and Elizabethan Settlement.

## 4. Census rules

- Keys: all allowed; no `briefLength`.
- Quotations: the brief has 5 quoted spans; the card has 5 entries, one each, none extra. Each `modern` is the brief's wording exactly.
- Each `printed` stands at its file and lines (folded as the validator folds; checked in memory, no file written): DT 25837-25838, F4 51045, DT 1250, DT 2091-2101, DT 3332-3333. Every cited file is in `sources`. No scan fault inside any span, so no `tools/quote_scan_readings.json` entry is needed.
- No quotation marks in `briefReferences`.
- `secondReading` is absent from all five, as the new-card prompt directs; the second-reading step must fill it before the card can pass the validator.

## 5. Originals

The brief's quotations come from English printed wording (Walter's modernized text, Foxe, Henry VIII, Tonstal). The outline renders no quotation from a held Latin, Greek, French or German original. Nothing to add.

## 6. "Not found" claims and conflicts

- The `sourcing` conflict is real: it says the Library holds "two volumes of his own writing", and only DT is his. It also implies Foxe's own account is held; it is held only as Walter quotes it. The card says the right thing (one volume; Foxe through Walter, `uncertain[7]`). The `sourcing` field is not the card's to change; it is flagged for whoever owns the census entry.
- Outline items left off (Packington, the Index, Joye and the rest): rightly left off; none is told in the brief.
- Nothing clearly wrong was left in.

## Applied (card fixer)
- FIX 1 (`legacy.traces[2]`, "licence" -> "license"): applied word for word.
- Not applied: none.
