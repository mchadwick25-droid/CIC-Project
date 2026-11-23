# Card check, what it was about pass: Rufinus of Aquileia (`rufinus-of-aquileia`)

Checked `rufinus-of-aquileia.card.json` against `Card.pass2.json` (starting card), the section **Third pass: what it was about (2026-11-23)** of `Card_Edits.md`, and `rufinus-of-aquileia.brief.txt` as it now stands. Every cited line was opened. N202, N203, N206 as in `Card_Edits.md`.

## Verdict: FIX (two changes)

### FIX 1. `briefReferences[14]` (Epiphanius, Letter 51): wrong work named for the sides

The line on the sides is at N203 46255-46260. It sits in Fremantle's introduction to the Apology to Apronianus (div `vi.xi.i`, "Preface", at 46230-46263), not in his Prolegomena (div `vi.ii`, 44003 on). The Prolegomena (44177-44187) makes Rufinus John's adviser, but it does not say Jerome sided with Epiphanius.

- Old: `Fremantle, Prolegomena: in the disputes over Origen Jerome sided with Epiphanius and Rufinus with John of Jerusalem.`
- New: `Fremantle, introduction to the Apology to Apronianus: in the disputes over Origen Jerome sided with Epiphanius and Rufinus with John of Jerusalem.`

### FIX 2. `uncertain[18]` (the note on Letter 124): the charge is misstated

N206 24659-24660: "It begins by saying that Christ was made God's son not born". "Origen made the Son not born" can be heard as a different claim. The fewest words that put it right:

- Old: `that Origen made the Son not born, is not borne out`
- New: `that Origen said Christ was made God's Son, not born, is not borne out`

## Checks that passed

1. **Edits justified.**
   - Socrates IV.24 matches N202 13725-13742.
   - Epiphanius's three charges and his prayer match N206 10813-10818, 10876-10879, 10899-10901 and 10976-10979.
   - Letter 124's heading dates it 409 or 410 (N206 24628-24629). Its ranking of the Son and the Spirit is at 24684-24693, and its unsigned note at 24660-24663.
   - The Apology to Anastasius on the flesh and the devil matches N203 45988-45993 and 46008-46012.
   - Anastasius on the faith of the apostles and the emperors' decree matches N203 46162-46166 and 46204-46207.
   - Rufinus's claim of falsification is at N203 45763-45765.
   - `uncertain[17]` credits each side and tags the dispute as disputed.
2. **Nothing else moved.** A diff of the two cards shows only edits 1 to 12 of the list.
3. **Removed references.** The removed references (the ascetic society, the baptism line, Melania, "the comparison of the Latin with the Greek", Alaric) are all things the brief no longer tells. No remaining `briefReferences` entry names a cut event. `[2]` (six years and two more) grounds the brief's "eight years".
4. **Census rules.**
   - There are three quoted spans in the brief and three `quotationOriginals`. Each `modern` stands verbatim in the brief, and the printed and original entries are unchanged.
   - `briefReferences` has no quotation marks.
   - Letter 124's file (N206) is in `sources`.
   - No audit file is named, and the new text uses American spelling.
   - Validator, `--skip-quotes`, run on a scratch copy of the census with this card: 0 errors, 4 warnings (none for this entry).
5. **"Checked at card".** No quotation is under six words, so none applies.
6. **Not found or left in.** The skipped items are sound. Nothing clearly wrong is left in, apart from the two items above.
7. **Census entry.** None for this pass.

## Note (not a card change)

The header line of the third-pass section in `Card_Edits.md` reverses the direction. It says the card was written to `Card.pass2.json` from `rufinus-of-aquileia.card.json`, but the reverse is true.
