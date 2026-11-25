# Second Readings (B11M)

Piece: montanism-the-new-prophecy. Blind readings: `Second_Readings_Blind_A.md`. Key: `Second_Reading_Key.md`.

## Method

1. For each id, our wording in the key was checked word for word against `montanism-the-new-prophecy.brief.txt` and against the card entry's `modern` in `montanism-the-new-prophecy.card.json` (`quotationOriginals`). All three match exactly in all three cases.
2. Each was set beside the blind rendering. Where they differ, the cited lines in `cic/texts/` and the card's `printed` field were opened and read.
3. B11M-03, last Greek word: checked by hand. The Holl scan, lines 18762-18763, prints "χατιέ-" / "νγαις«". With the scan's usual χ for κ, the word is κατιέ-ναι, and "γαις" is scan noise. Two other places confirm κατιέναι: Oehler's print of the same passage, line 3287 of `epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt`, prints "κατιέναι" cleanly, and its Latin, lines 3357-3358, reads "in eumque sanctam Hierusalem delabi", a present infinitive. Holl line 18513 uses the same verb for the same belief, "κατιέναι τὴν ἄνωθεν Ἱερουσαλήμ". κατιέναι is the present infinitive of κάτειμι. It can carry a future sense, but "comes down" is a fair reading and matches the brief's earlier report of what the believers said. The card's `uncertain` note already reads it as κατιέναι, and its claims about Oehler (τύπον for τόπον; "hunc locum sanctum esse", split across lines 3357-3358) hold.

## Verdicts

| id | brief = card `modern` | verdict | reason |
|---|---|---|---|
| B11M-01 | yes | SAME | The only difference is the commas in "word, and spirit, and power". The words match the NPNF English at lines 29849-29852, with the endnote marker set aside. |
| B11M-02 | yes | MINOR | We have "divide" and the blind reader has "undo" for *soluant*. ANF's "disjoin (from God)" supports ours, and both mean denying Christ. "God" against "god", and "teach fasting" against "teach people to fast", come to the same thing. |
| B11M-03 | yes | MINOR | We have "showed" and "shining", the blind reader "revealed" and "bright", for ἀπεκάλυψε and λαμπρᾷ. The blind reader keeps the speech tag φησί, which our brief leaves out because it frames the quote itself. The last word, κατιέναι, is confirmed by hand (above), and "comes down" stands. |

## Counts

- SAME: 1
- MINOR: 2
- MEANING: 0

## Card changes needed

- `quotationOriginals[0]`: `secondReading`: "same".
- `quotationOriginals[1]`: `secondReading`: "minor".
- `quotationOriginals[2]`: `secondReading`: "minor".
- No `original` (`printed`) needs correcting. `quotationOriginals[2].printed` keeps the scan's own spelling, "χατιένγαις", as the card's convention requires, and its `uncertain` note already gives κατιέναι. It could add that Oehler line 3287 prints κατιέναι cleanly. That is optional, not a correction.

No brief wording changes.
