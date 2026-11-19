# Card check: Augustine of Hippo (new card)

Checker, 2026-11-18. I did not write this card. Read against `augustine-of-hippo.brief.txt` (and `.v1`), `Card_Edits.md`, `Outline.md`, `Source_Sheet.md`, the census entry's own fields and the cited lines in `cic/texts/`.

## Verdict: FIX (one scan reading, one spelling)

### FIX 1: a line number inside the Retractations span (`tools/quote_scan_readings.json`)

`quotationOriginals[1].printed` does not stand at RET 9059-9066 as the file reads. Knoll's edition line number "10" sits inside the span, at the end of line **9063**, not 9065 as `Card_Edits.md` says:

```
9063: quis enim te discernit? quid autem habes, quod non 10
9064: accepisti? si autem accepisti, quid gloriaris, quasi
```

The card's wording is right; the fault is the scan's. The card stays as it is. The validator needs this reading added to `readings` in `tools/quote_scan_readings.json`. It follows the existing entry for the Confessions file at line 13470 ("euangelica 20"). I have not edited that file.

```json
{
 "file": "cic/texts/augustine_retractationes-lat_knoll-csel36.txt",
 "lines": "9063",
 "scan": "quod non 10",
 "reads": "quod non",
 "kind": "line number run into the line"
}
```

I applied this reading in memory, joined the line-end hyphens ("solu-/tione", "per-/ueniri") as the validator does, and folded the text. With that done, the printed wording stands at 9059-9066. The other "5" at line 9058 is outside the span. No other fault lies in either span. In the Confessions span (AUGL 13463-13465), the line number "15" on line 13465 comes after the span's last word, so no reading is needed there.

### FIX 2: American spelling

Field `sources.about[4].title`. The title is our English for Facundus's Latin *Pro defensione trium capitulorum*, not printed English wording.

- Old: `"In Defence of the Three Chapters"`
- New: `"In Defense of the Three Chapters"`

## 1. Each field against its evidence

Re-read at the cited lines; each holds:
- datesNote: seventy-six years and almost forty as priest or bishop, POS 4919-4921; born 13 November 354, POS 133-134, with the note at 149-153 (De beata vita); Prosper's death entry, PRC 54206-54211 (the OCR year aside); 391 for the priesthood, POS 5227; "in 391 consecrated him as coadjutor", and the succession in 396-397, POS 5309-5311. The card reports the note faithfully and marks 395-396 as the dominant modern reconstruction.
- legacy.traces: Maassen on canons IX and XI-XXV and the rest, MGHC 4124-4127; Boniface II, 4157-4159. Luther to Emser, LUE 18056-18063. Calvin, CAL 25351-25354 and 25389-25391. Jansen, NEA 886-890 (Urban VIII, 6 March 1642, book and theses) and 1097-1104 (31 May 1653, the Five Propositions).
- uncertain: Possidius's friendship of "almost forty years", POS 5057-5060; the apparatus "diuina S: uicina BCGHMOPQVW edd., uicino F", AUGL 13486.

Nothing on the card contradicts the brief. No field names an audit, review or ruling.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. Brief references

Each of the 11 entries names something the brief tells. None is removed. They remain as written: Possidius (Tagaste, the teaching posts, Ambrose, Easter baptism, the seizure for the priesthood, the councils and Honorius's laws, the Vandals, seventy-six years, the library, the poet's lines); Confessions IV.2.2; VI.6.9; VIII.12.28-30; Retractations II.1 and Predestination 8 (Simplicianus); Letter 93; Retractations II.43 and City of God XIV.28; On the Spirit and the Letter 5; Orange (Maassen, Warfield); Luther, Calvin, Neale on Jansen; the census entries. The details there that the brief does not repeat (Alaric, Prosper's Sentences) are names for events the brief does tell, not things it no longer tells.

## 4. Census rules

- Keys: all allowed; no `briefLength`.
- Quotations: the brief has 2 quoted spans (the inner single quotes sit inside them); the card has 2 entries, one each, none extra. Each `modern` is the brief's wording exactly.
- `printed`: AUGL 13463-13465 stands. RET 9059-9066 stands once FIX 1's reading is listed. Both files are in `sources`.
- No quotation marks in `briefReferences`.
- `secondReading` is absent from both entries, as the new-card prompt directs; the second-reading step must fill it before the card can pass the validator.

## 5. Originals

The outline renders both quotations from the held Latin, and the card carries the Latin as `printed` from Knoll's editions. That meets the rule. The card notes the diuina/uicina variant, and the rendering follows uicina. An `englishPrinted` from Pilkington's Confessions is allowed but not required.

## 6. "Not found" claims and conflicts

- The Pelagian years (Possidius's "almost ten", the census's "twenty") are left unresolved, and the brief gives no number. That is right.
- The authorship of the Isidore verses is left off. That is right.
- The Confessions date of 397-400 comes from `cic/corpus-map/WORKS.yaml`, which the card names only as "the Library's works list". That is accurate, so it is not a FIX.
- The writer's flag points to RET line 9065; the numeral is at 9063 (FIX 1).
- No conflict with the entry's own fields. `voices` says "thirty-five years" as bishop, which fits the 395-396 reconstruction. The 1642 bull adds to `legacy`'s 1653 condemnation and does not contradict it.
