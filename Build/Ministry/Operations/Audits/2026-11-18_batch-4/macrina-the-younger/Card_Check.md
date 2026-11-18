# Card check: Macrina the Younger (batch 4)

**Verdict: FIX** (six changes below).

## 1. Edits justified

All eleven listed edits hold against the brief and the files.

- The Petit source is real, and lines 2304-2306, 8681-8688, 10731-10734 and 10758-10760 say what the Ferrara reference claims.
- Clarke lines 132, 158, 160, 232, 234, 274, 276 and 412 support the new references.
- The Lampadia quote and reference, the dating reference (lines 64, 108, 402) and the line-84 reference are rightly gone. The brief tells none of them.

## 2. Nothing else moved

I diffed the card against the census `card` for `macrina-the-younger`. Only `briefReferences`, `quotationOriginals` and the new `sources.about[4]` differ, as listed. Every other field is word for word.

## 3. References that remain

Twelve entries hold in full: the census setting, line 132, lines 138/158, line 158, lines 164/264/356, line 160, lines 274/276, line 230, line 196 with the dialogue, and Ferrara. Five parts name things the brief does not tell:

- `[0]` "on the floor". The brief has only "a sack spread over a board".
- `[2]` "betrothed at twelve". The brief gives no age.
- `[9]` "Basil's death". The brief gives only "In 379, as scholars date it, she lay dying".
- `[11]` "and by moving her hands". The brief has only "she finished it in her heart".
- `[13]` "and burial", with lines running to 346. The brief tells no burial. Her death is at line 234.

## 4. Census rules

- Keys are allowed and there is no `briefLength`.
- The brief's two spans, "You, Lord," and "have set us free from the fear of death.", are one sentence broken by "she said". One entry for them is right.
- All cited files are in `sources`.
- There are no quotation marks in `briefReferences`, and the spelling is American.
- **`printed` is not verbatim.** PG 46 at line 71690 prints `φόθον`, but the card prints `φόβον`. The entry's own note gives the OCR form, so `printed` should carry it. The garbled Latin run that is left out is already noted in the entry.

## 5. Not found / clearly wrong

The writer reported nothing not found. Beyond the points above, nothing in the card contradicts the brief or a held source.

## FIXes

1. `briefReferences[0]`. Old: `she lies on the floor on a sack spread over a board`. New: `she lies on a sack spread over a board`.
2. `briefReferences[2]`. Old: `betrothed at twelve; the young man died;`. New: `the match her father planned; the young man died;` (LIFE 128: "her father's schemes", "the plan formed for her").
3. `briefReferences[9]`. Old: `Clarke's introduction (line 52): Basil's death and Gregory's visit in 379.`. New: `Clarke's introduction (line 52): Gregory's visit in 379.`
4. `briefReferences[11]`. Old: `she finished the evening thanksgiving in her heart and by moving her hands, and closed`. New: `she finished the evening thanksgiving in her heart, and closed`.
5. `briefReferences[13]`. Old: `Life (Clarke, lines 184-346): Gregory's own account of her last days, death and burial,`. New: `Life (Clarke, lines 184-234): Gregory's own account of her last days and death,`.
6. `quotationOriginals[0].printed`. Old: `«Σὺ,» φησὶν, «ἔλυσας ἡμῖν, Κύριε, τοῦ θανάτου τὸν φόβον.`. New: `«Σὺ,» φησὶν, «ἔλυσας ἡμῖν, Κύριε, τοῦ θανάτου τὸν φόθον.`
