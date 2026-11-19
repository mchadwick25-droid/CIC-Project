# Card check: Martin Luther

**Verdict: FIX.** A new card (Decision-Log, "Batch 5 hearts", 2026-11-18, item 9), so there is no starting card to diff against. Every field was checked against its evidence in `Card_Edits.md`, and against the entry's existing fields in `cic-website/data/world-census.json`. Keys: all are `CARD_KEYS` and `QUOTATION_ORIGINAL_KEYS`, and there is no `briefLength`. All 22 cited files exist under `cic/texts/`, and every file a `quotationOriginals` entry or a quotation in the card's prose cites is in `sources`. The spelling is American, except "endeavour", which is Currie's printed wording. No audit, review or ruling is named.

## Quoted spans (7 in the brief, 7 entries)

Each `modern` matches the brief word for word. Each `printed` was re-read at its file and lines:

1. Thesis 37, KD 2576-2578. This span stands only after a scan reading (see Fix 1). The scan's "mortuus^" folds away.
2. The Worms answer, KD 5945-5950. It stands, with the hyphens joined ("testi-moniis", "pos-sum"), and "évidente" folds to "evidente". See Fix 4.
3. "Gott helff mir. Amen.", KD 5952. It stands.
4. The words "Ich kann nicht änderst, hie stehe ich" at RTA 36651. They stand. See Fix 5.
5. W4 11958-11961. It stands, and the sheet's range correction to 11961 is right.
6. W4 13558-13559. It stands, all on line 13558.
7. W1 285-286. It stands.

Originals: the outline's held Latin (Q1, Q2) and German (the Worms ending, Here I stand) are carried. For Q5 and Q7 the German is not held, so the English printing is correct there.

## Fix 1. The Thesis 37 scan fault: tools/quote_scan_readings.json (not edited)

The fault is on **line 2578, not 2577**. KD 2576 is "37. Quilibet verus Christianus...", 2577 is "habet participationem...", and 2578 is "etiam sine Uteris veniarum, a Deo sibi datam." `withReadings` looks for the scan text only inside the lines given. An entry with `"lines": "2577"` would itself fail ("no longer read \"Uteris\""), and the card's "literis" would still not be found. The entry to add to `readings`:

```json
{
  "file": "cic/texts/kidd_documents-illustrative-of-the-continental-reformation-lat-deu-fra-eng_1911.txt",
  "lines": "2578",
  "scan": "Uteris",
  "reads": "literis",
  "kind": "OCR misread"
}
```

Line 2578 holds "Uteris" once, and no reading for this file exists yet. The card's `printed` ("literis") stays as it is. The "Line corrections" in `Card_Edits.md` should read KD 2578.

## Fix 2. uncertain[11], the late writings against the Jews

The 1543 treatises are stated plainly as not held. The card does not say what they contain. The banishment sentence is quoted verbatim, and the rest of the paragraph is given faithfully (CUR 26647-26651). The jocular headnote is credited to Currie (CUR 26626). This all meets the ruling.

One sentence moves off the record, though. The letter says he grew weak near Eisleben "but it was my own fault". It also says she *would have said* that the Jews or their God were behind it, and then "perhaps they blew upon me" (CUR 26636-26645). The card drops "my own fault". It gives the Jews-or-their-God line as Luther's own claim, and it adds a "chill that weakened him", which the letter does not say.

- old: `After saying that the Jews, or their God, were perhaps behind the chill that weakened him near Eisleben, because they might have blown on him as his carriage passed a village where many Jews lived, he writes:`
- new: `He writes that he grew very weak near Eisleben, and that it was his own fault. But she would have said, he writes, that the Jews or their God were behind it. His carriage had passed a village near Eisleben where many Jews lived, and perhaps they blew on him. Then he writes:`

## Fix 3. uncertain[1], Here I stand (Contested in the source sheet, D1)

Wrede says that "im wesentlichen" (in the main) church historians keep the longer form, and that secular historians accept only the short cry (RTA 36646-36648). That is his report of the scholarship in 1896. The card states it as a present, universal fact, and it never says the question is open.

- old: `Church historians keep the longer form; secular historians accept only the short cry.`
- new: `Wrede reported in 1896 that it was mainly church historians who kept the longer form, and secular historians who accepted only the short cry. Which ending he spoke is not settled.`

## Fix 4. quotationOriginals[1], the Worms answer: add an `uncertain`

The brief's quotation runs straight from "clear reason" to "I cannot and will not take back anything". Without any mark, it leaves out the parenthesis on popes and councils and the clause "victus sum Scripturis... in verbis Dei" (KD 5947-5950). The card should say so.

- add: `"uncertain": "The brief leaves out, without marking it, the words between: the aside that he trusts neither pope nor councils alone, since they have often erred, and the clause that he is bound by the Scriptures he has cited and his conscience is captive to the words of God."`

This is also a point for the brief's own owner: it is a silent cut inside quotation marks. It is flagged here, and the brief was not edited.

## Fix 5. quotationOriginals[3], Here I stand: add an `uncertain`

The prints read "Ich kann nicht änderst, hie stehe ich", which is "I cannot otherwise, here I stand". The brief has the clauses the other way round, which is Kidd's order (KD 5951-5952).

- add: `"uncertain": "The two prints give the clauses the other way round: I cannot otherwise, here I stand. Kidd prints them in the brief's order, Hie stehe ich. Ich kan nicht anders."`

## Fix 6. briefReferences: remove parts the brief does not tell

- [0] old: `C. M. Jacobs, the editor, says the indulgence of 1515 was to pay for the new church in Rome, with Albrecht as its commissioner.` new: `C. M. Jacobs, the editor, says the indulgence was to pay for the new church in Rome.` (The brief names neither 1515 nor the commissioner.)
- [1] old: `The Freedom of a Christian, 1520: a Christian is a free lord of all and a dutiful servant of all, justified by faith alone and not by works.` new: `The Freedom of a Christian, 1520: a Christian is justified by faith alone and not by works.` (The brief does not tell the lord and servant pairing.)
- [3] old: `The Acta of Worms printed by his side in May 1521, in Wrede's edition: the hearing of 17 April and the crowd, and the answer of 18 April in Kidd's Latin.` new: `The Acta of Worms printed by his side in May 1521, in Wrede's edition, and the answer of 18 April in Kidd's Latin.` (The brief tells neither the first hearing nor the crowd.)
- [5] old: `The preface to the Wittenberg hymnbook of 1524, and Bacon's count of its eight hymns, four of them Luther's.` new: `Bacon's count of the eight hymns in the Wittenberg hymnbook of 1524, four of them Luther's.` (The brief does not tell the preface.)

The remaining entries are each tied to a sentence of the brief: [2] decree and burning; [4] edict, hiding, New Testament; [5] Formula Missae, hymnbook count, Bacon, Halle 1730; [6] 1525 writings, Rühel, the Hutterite chronicle; [7] the marriage letters; [8] the Small Catechism and the 1539 preface; [9] the census. None of them has quotation marks.

## Fix 7. datesNote, the last sentence

`A letter of 1 February 1546 is held` names no letter. On a read-through, it looks cut off, and nothing else in the note tells the reader what the letter is. Two checks agree: the string itself, and `Card_Edits.md`, which cites it as the letter of CUR 26624-26636.

- old: `A letter of 1 February 1546 is held`
- new: `A letter of 1 February 1546 to his wife is held`

## Rulings on "not found" and on the entry's fields

- **Death date: accepted.** No held source used here gives the day (Currie's index has only "1483-1546"). The card gives none, which does not contradict `longDescription` ("died on 18 February 1546").
- **Froben's "his writings": accepted.** KD 4104-4110 and 4134 concern his collected works.
- **Doltzig: accepted.** CUR 9806-9813. "Another letter" in `uncertain`, and "to a friend" in the references, both follow the brief.
- **Bach and "learned by heart at home": accepted as not found.** The card does not repeat either claim, and does not contradict them.
- **"A miner's son from Eisleben" (`why`) is found.** TT 97 has "his father, a poor miner". `Card_Edits.md` says the card "keeps it", but the card never mentions it. No change is needed.
- **The sheet's line corrections are right.** The banishment sentence is at CUR 26647-26648, and Q3 is at W4 11958-11961.
- **Spot-checked and right:** Rühel and Jacobs (W4 12296-12304), Aleander (KD 5781-5786), the archbishop of Mainz (KD 6152-6160), Contarini (KD 6148-6150), the Hutterite chronicle (HUT 5345-5349), Charles V (RTA 39105-39125), Spangenberg (HY 556-562), the Formula of Concord (BC 25517-25520), the marriage date (CUR 9752-9753).
- **Nothing contradicts the entry's existing fields.**
