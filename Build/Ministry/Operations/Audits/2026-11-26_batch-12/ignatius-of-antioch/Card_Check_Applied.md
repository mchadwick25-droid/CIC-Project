# Card check applied: ignatius-of-antioch

Each old text was found exactly once in `ignatius-of-antioch.card.json` and replaced word for word. Nothing else changed.

| # | Field | Result |
|---|---|---|
| 1 | `timeline[3].lines[5].text`: last sentence now "It is the last stage of his road that his letters tell." | applied |
| 2 | `timeline[1].lines[4].text`: "... come to him at Smyrna, the first two with others of their churches." | applied |
| 3 | `timeline[2].lines[0].text`: elders glossed as "the council who led a church with its bishop" | applied |
| 4 | `timeline[4].lines[4].note`: "... speak the wheat line as he heard the lions roaring." | applied |
| 5 | `timeline[5].when`: "After his death" to "Later" | applied |
| 6 | `quotationOriginals[1].uncertain`: "some read the last question, and the clause after it, as statements ..." | applied |
| 7 | `uncertain[2]`: "writing much later" | applied |
| 8 | `uncertain[5]`: ends at "... argued among modern editors for centuries." | applied |

Entry fields: the check gives none, so `Card_Edits.md` is unchanged.

JSON check: `python -m json.tool ignatius-of-antioch.card.json > /dev/null` passed.

Readability: `python -m engine.m1.profile_readability` on a plain file of the card's running text (kept outside the repository): "1437 words, grade 8.0 (names out 6.8), reading ease names out 76.0, 16.7 words a sentence, 23% short sentences, longest sentence 51 words - pass". My extraction took fewer fields than the check's own run (which gave 1762 words), so the word count differs.
