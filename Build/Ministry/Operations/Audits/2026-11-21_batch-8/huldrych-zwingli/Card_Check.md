# Card check: Huldrych Zwingli

Batch 8, 2026-11-21. Independent checker; I wrote neither the brief nor the card. New card (no census entry, no starting card), so every field was checked against its evidence in `Card_Edits.md`. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (2 changes and 1 scan reading, below).

## The drowning letter: CONFIRMED

The brief says: "But, he went on, it pleases God to guard in this way against evils to come." This is reported speech, with no quotation marks. So it needs no `quotationOriginals` entry. The question is only whether the Latin bears it.

Kidd prints the letter to Watt, 7 March 1526 (KD 25407-25412): "Nollem crepundia renascentis Christianismi huiusmodi exemplis inaugurari; sed Deus non sumus cui sic placet futuris malis prospicere, ut olim quum Petro mentientem Ananiam subita atrocique morte trucidavit, quo nobis fallendi audaciam omnem, qui tamen nullius rei aeque gnari sumus, amputaret. . . ."

- **"non sumus" is not a fault.** "sed Deus non sumus" means "but we are not God". The relative "cui" takes Deus as its antecedent: "God, whom it pleases in this way (sic) to provide against evils to come (futuris malis prospicere)". The Ananias clause then gives the example.
- **The clause is clean in the scan.** The words that carry the claim, "Deus ... cui sic placet futuris malis prospicere" (KD 25409-25410), need no reading. The faults nearby ("NoUem", "honiinum", "turn") lie outside them.
- **The rule on one scan does not apply.** The batch 6 rule requires a second print only to confirm a reading of a scan fault. No reading is made here, so one clean print is enough evidence for a paraphrase.
- **Lines 25411-25412 are not "cut and run together".** They read continuously as Latin: "to cut off from us, who yet are skilled in nothing so much, all daring to deceive". Kidd's ellipsis ends his extract after "amputaret".
- **What the paraphrase drops is not distorted.** It leaves out "we are not God" and the Ananias example. Both hand the outcome to God's will, which the brief's "it pleases God" keeps.

`uncertain[6]` leaves this question open and misdescribes the last lines (FIX 2).

## 1. Each field justified

Spot-read against the files: Kidd on the election and admission (KD 21197-21198), the drowning mandate (KD 25384-25388), the war letter (KD 26134-26140), the minster record (EG 48400-48411). All hold as the card states them, except `uncertain[1]`, which credits Kidd to "the chapter's records". Kidd cites Zwingli's Opera (KD 21197-21198), and `Card_Edits.md` (Conflicts, item 6) itself found this. Fixed in FIX 1.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Checked against the brief and `huldrych-zwingli.brief.v1.txt`. The revision cut Myconius on the burning of the body and the 1524 images line. No reference names either. All nine entries tell what the brief tells, and none has quotation marks. No change.

## 4. Census rules

- Keys: all allowed. No `briefLength`.
- Four quoted spans, four entries, each `modern` exactly the brief's. [0], [1] and [2] carry no `secondReading`. [3] is under six words and carries "checked at card".
- Every cited file is in `sources`. No audit, review or ruling is named. American spelling throughout the card prose.
- Prints at their lines: [1] KD 26134-26139 is clean Latin, verbatim. [2] WA 12535-12544 is clean, and the long s folds to s. [3] EG 48407 stands verbatim. [0] JACK 2185-2216 stands only with the drop reading below: a footnote (2189-2210) and the running head "THE FIRST ZURICH DISPUTATION. 57" (2213) fall inside the sentence. Both are stray marks under the batch 6 rule.

## 5. Originals

- **[0] the Disputation: no original held.** The German record is not held, so McLouth's English stands as `printed`. The rendering follows it clause by clause.
- **[1] the war letter: KEEP.** The rendering follows the Latin. "oligarchiae nervi" is rendered as the rule of the few, and `uncertain` says so.
- **[2] Marburg, article 15: KEEP.** The German matches the rendering in every clause.
- **[3] "M. Uorichs seligen": KEEP as printed, checked at card.**
  - The entry prints the scan's letters and makes no reading, so no confirming print is needed.
  - `uncertain` records the book's other spelling, Uolrichs, as Mark's guidance asks.
  - The rendering does not hang on the letter. "Seligen" here is "the late", which "of blessed memory" renders fairly. Egli's own bracket "(Zwingli)" at 48403 fixes whom the record means.

## 6. "Not found" claims and anything left wrong

- **"Records of the chapter" not found: correct.** But `uncertain[1]` still says it (FIX 1).
- **"Central" Switzerland: correct to leave to the brief.** Kidd has "Five Forest Cantons" (KD 26088).
- **The tree's three conflicts:** each is credited in `uncertain[0]` and `[1]`, not told as fact; the card's knownFor and legacy say "one of their founders", as Jackson does.
- **Foxe's "forty-four":** kept in `uncertain[12]` and not used. Correct.
- Nothing else found wrong.

## Fixes

**FIX 1.** `uncertain[1]`, opening words
- Old: `When the preaching through Matthew began. Kidd, from the chapter's records, gives his admission as people's priest as 1 January 1519`
- New: `When the preaching through Matthew began. Kidd gives his admission as people's priest as 1 January 1519`

**FIX 2.** `uncertain[6]`, the passage from "The next clause" to "Kidd's remark"
- Old: `The next clause in Kidd's print reads "Deus non sumus cui sic placet futuris malis prospicere", and goes on to Ananias struck down for lying. The print has "non sumus" and no second held print of the letter confirms or corrects it, so whether the clause says that it pleases God to guard in this way against evils to come, or something else, is read from this one print. The print's last lines, 25411-25412, are cut and run together. Kidd's remark`
- New: `The next clause in Kidd's print reads "Deus non sumus cui sic placet futuris malis prospicere": but we are not God, whom it pleases to guard in this way against evils to come. It goes on to Ananias struck down for lying. The clause is clean in the print; no second print of the letter is held, and Kidd's extract ends there. Kidd's remark`

## Scan reading to add (for entry [0])

```json
{"file": "cic/texts/zwingli_selected-works_jackson1901.txt", "lines": "2188-2214", "scan": "THE FIRST ZURICH DISPUTATION. 57", "drop": true, "kind": "footnote and running head with page number", "lines_held": ["* [Hager in \"Gyrenrupfen \" presents the dispute about the council thus:", "\"After this Mr. Fritz, the majordomo, very cleverly presented the com-", "mand of his master, saying that his master had been surely informed,", "that in a year there would be a council. Concerning this Zwingli did", "not wish to speak. Thereupon you immediately began to speak, and rose", "and said the same as Mr. Fritz had just said, and in a nice way referred", "to the future council and showed yourself a little more, just as if the matter", "had not also been commended to you. Thereupon Zwingli arose, and said we", "should not be led astray by the council; he also had had a letter in which he", "was informed how the German princes had demanded from the pope that he", "have a council within a year, but that the pope had formally assented had not", "yet happened, nor is it possible (he said) that within the space of a year a", "general council could be gathered together; furthermore the three mightiest", "lords, King of France, Emperor, and King of England, were at war with each", "other, who could not easily be conciliated; also that the fixing of the council", "would be left to the Germans. Hence one could see that the promise of a", "council was only a postponement, not a definite resolve; but it mattered little", "whether they had a council or not, for he believed that no man would live to", "see a council in which the word of God would be allowed to rule. Therefore,", "even if a council should be held at once, one would not care either, for we", "would depend upon and preach the word of God; may the councils determine", "herein what they please.\" After this he from Neftenbach arose and spoke.]", "THE FIRST ZURICH DISPUTATION. 57"]}
```
