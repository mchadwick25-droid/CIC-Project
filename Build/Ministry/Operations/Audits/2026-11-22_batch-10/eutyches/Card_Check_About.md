# Eutyches: card check, third pass (what it was about)

Checked `eutyches.card.json` against `Card.pass2.json`, the section "Third pass: what it was about (2026-11-23)" of `Card_Edits.md`, and `eutyches.brief.txt` as it now stands. Every cited line opened.

**Verdict: FIX** (one change).

## What holds

- **Nothing else moved.** A field-by-field comparison with `Card.pass2.json` shows changes only in `briefReferences[0]`, `[1]`, `[2]`, `[3]`, `[4]`, `[6]`, `[8]` and the appended `quotationOriginals[3]`, each listed in the edit list. The key set is the same and allowed.
- **Edits 1-8 (briefReferences).** Each is supported by the brief and its lines:
  - `[0]`: Perry 23797-23809 has Flavian's notary's deposition, "He had not Flesh Con-substantial with us"; the brief says "his judges recorded that he denied it shared our nature".
  - `[2]`: Leo 4544-4560 has Eutyches citing Julius, Felix, Athanasius and Gregory, who "rejected the phrase “two natures,”"; this matches the brief's paragraph 7.
  - `[3]`: Leo 4740-4745 has "nor yet that the Lord's flesh was of the same substance with us"; this matches the brief's paragraph 7. The Valentinus and Apollinaris clause is correctly gone, because the brief cut "old heresies".
  - `[4]`: Leo 5301-5302 has "both natures retain their own proper character", and 5434-5435 has "God and man is one person"; this matches the brief's paragraph 9.
  - `[6]`: Perry 23861-23862 has Basil's recorded sentence ("you speak of mixture and of a con-fusing"). Perry 23931-23933 has "Whoever affirms Two Natures let him be Anathematized". Perry 24113-24118 and 24145-24148 have Flavian altering and subtracting from the faith. All of this matches the brief's paragraph 13. The brief's paragraph 13 also no longer names Theodoret.
  - `[1]` and `[8]`: the removals match the brief, which no longer has Eusebius as an advocate, Theodoret, or Nestorius deposed.
- **Rule 3.** No remaining `briefReferences` entry names something the brief no longer tells.
- **Rule 4.** The brief has four quoted spans and the card has four `quotationOriginals` entries. Q1 and Q2 are unchanged and carry no blind-reading field the role forbids. Q3 "This he certainly never did." matches Leo 5028 verbatim. Every cited file is in `sources`. No audit file is named. Spelling is American, and Perry's "grey" stays only inside the verbatim printed wording.
- **Rule 6.** Not-found items are unchanged (Chrysaphius as godson and the exile, both already under `uncertain`). Nothing clearly wrong is left in.

## FIX

The `printed` field of the new quotation carries words its rendering does not render. The brief quotes only the two words. In every other entry, here and on the model card, `printed` stands for the quoted span alone. Line 4560 holds the two words verbatim.

- Field: `quotationOriginals[3].printed`
- Old: `rejected the phrase “two natures,”`
- New: `two natures`

(`file` `cic/texts/npnf212_leo-great-gregory-great.xml` and `lines` `4560` stay as they are. `secondReading` "checked at card" is correct, because the quotation is two words. With this change, the rendering "two natures" matches the print.)
