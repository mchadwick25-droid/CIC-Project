# Card check, modern pass: Council of Ephesus (431)

Read: `CLAUDE.md` ("Trust and source fidelity"), `roles/card.md`, `council-of-ephesus-431.brief.txt`, `council-of-ephesus-431.card.json`, `Card.pass3.json`, `Card_Edits.md` (section "Fourth pass: no modern opinion (2026-11-23)"), `Outline.md` (Modern pass, Do not say), `Modern_Pass.md`, `Fresh_Read_Modern.md`. Compared the card with `Card.pass3.json` by `diff` on normalized JSON.

## What holds

- **Nothing else moved.** The diff shows only `uncertain` 16-20 (new), `briefReferences` 12-14 (rewritten), Wigram and Badger removed from `briefReferences`, and the new Barhadbeshabba entry. Each one is listed in `Card_Edits.md`.
- **The five new `uncertain` entries, re-read at their lines:**
  - The commissioner's month: HEF 4932-4935 ("as is universally admitted, arrived there at the beginning of August"). BH 1125-1141 (Count John's arrival under August). M4 123607-123661: the report gives no month. "augustarum literarum" means the imperial letters, not August.
  - The dissolution: BH 262-263 ("dissolved in September"). HEF 6205-6207 ("October 30, 431"). M5 80115-80129 ("synodus Ephesina solvatur"), undated.
  - The year of the peace: HEF 7584-7590, verbatim for "probably of the year 433", Tillemont and "no great importance". BH 1250, 1338-1341 (433).
  - The condition: HEF 7224-7225 ("conditio sine qua non"). M5 35298-35303 ("depositioni illius consentirent") and 35345-35355 ("Nestorii dogmata ... anathematizasset, seque illum pro deposito habere confessus esset").
  - Who refused: BH 1269-1273 and 1340-1344. npnf203 37983-38012, the letter and the endnote's dating.
- **`briefReferences` 13, 14 and 16:** each matches the brief as it now stands. The Wigram and Badger removals are correct, since the brief no longer tells either one.
- **`quotationOriginals`:** four spans in the brief and four entries on the card, unchanged. "by persuasion and force" (checked at card): HEF 4977-4978 is verbatim. It renders M4 123610 "persuasione & vi". Held.
- **Census rules:** the keys are allowed, there is no `briefLength`, no audit file is named, the spelling is American, and every cited file is in `sources`.

## Verdict: FIX

Some modern views on the card still go uncredited, or are credited to an unnamed editor. One `briefReferences` entry still names a modern source the brief no longer draws on.

1. **`knownFor`** (uncredited modern year. Outline Do not say: "Not 'in 433' or 'two years later' for the peace", HEF 7582-7589, BH 1250, 1340; `uncertain` 18.)
   Old: `and was healed only by their peace two years later.`
   New: `and was healed only by their later peace.`

2. **`datesNote`** (uncredited modern dating. The edict is undated, M5 80117-80128. The date comes from BH 262-263 and HEF 6205-6207; `uncertain` 17.)
   Old: `The council was dissolved later that year`
   New: `The council was dissolved later that year, by the reckoning of Hefele and of Driver and Hodgson`

3. **`traditions[1].note`** (uncredited year. The same form as `outcome[2]`.)
   Old: `in 433 John and Cyril made peace.`
   New: `in 433, by Hefele's dating, John and Cyril made peace.`

4. **`traditions[3].note`** (two modern writers, named but not marked as modern. Badger is not in `record`. The years follow `uncertain[5]`.)
   Old: `W. A. Wigram, its English historian, says the church took no corporate action on Ephesus at the time. George Percy Badger says the Eastern bishops were cut off by its decree.`
   New: `W. A. Wigram, its English historian, in 1910, says the church took no corporate action on Ephesus at the time. George Percy Badger, in 1852, says the Eastern bishops were cut off by its decree.`

5. **`issue[4]`** (a modern writer, not marked. npnf214 18992-18996 calls him "the famous Bossuet ... his somewhat isolated position as a Gallican", in Percival's edition of 1900.)
   Old: `(Bossuet's account, printed in the English edition of the canons; Hefele)`
   New: `(the account of Bossuet, a modern Gallican writer, printed in the English edition of the canons; Hefele)`

6. **`uncertain[10]`** (two modern editors, not named. Percival is the editor of npnf214, lines 410 and 583; the excursus is at 17830-17834. Blomfield Jackson translated and annotated Theodoret's letters, npnf203 680-686; the note is at 36862-36865.)
   Old: `The editor of the English acts, giving Hefele, says`
   New: `The editor of the English acts, Henry R. Percival, giving Hefele, says`
   Old: `The editor's note to John's assembly's report, in the volume of Theodoret's letters, says`
   New: `Blomfield Jackson's note to John's assembly's report, in his English of Theodoret's letters, says`

7. **`uncertain[12]`** (uncredited modern date. It is Nau's, BB 31577. Outline Do not say: "Not 'around 600' or any date for Barhadbeshabba: Nau's dating"; `record[5]` and `traditions[4]` already credit it.)
   Old: `Barhadbeshabba, near the end of the sixth century, says`
   New: `Barhadbeshabba, near the end of the sixth century by François Nau's dating, says`

8. **`uncertain[19]`** (new this pass; the modern editor is not named. npnf203 37983-37985 is Jackson's endnote; see 680-686.)
   Old: `and the editor says it dates not long after Theodoret received Cyril's chapters`
   New: `and the editor, Blomfield Jackson, says it dates not long after Theodoret received Cyril's chapters`

9. **`briefReferences[12]`** (the brief no longer draws on the editors' chronology here. Outline line 107: "their chronology (dates, the arrests, who refused the peace) is not used in the story". The arrests now rest on M4 123609-123647.)
   Old: `Count John's own report to the emperor, in Latin (Mansi, tomus 4), and Hefele's English of it, with Driver and Hodgson's chronology: the emperor's letter`
   New: `Count John's own report to the emperor, in Latin (Mansi, tomus 4), and Hefele's English of it: the emperor's letter`

No other defect was found. No claim on the card is listed as not found, and nothing on it is clearly wrong.
