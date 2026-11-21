# Card check: Thomas Cranmer

Batch 8, 2026-11-21. Independent checker; I wrote neither the brief nor the card. New card (no census entry, no starting card), so every field was checked against its evidence in `Card_Edits.md`. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (2 changes and 2 scan readings, below).

## 1. Each field justified

Spot-read against the files:
- Cox's print of the 1549 preface (COX 48899-48901).
- The rebels' eighth article (COX 17555).
- Foxe on the speech and the fire (FOXE8 7398-7404, 7518-7527).
- Perkins's copy of the speech (PERK 44207-44211).

All hold as the card states them. Both of the card's year conflicts are handled honestly: the scan's 1550 at COX 747 against the register's 1556, and the unreadable "153^" for the second marriage.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Checked against the brief and `thomas-cranmer.brief.v1.txt`. Two entries name the Tower, which neither brief tells (FIX 1, FIX 2).

"St. Mary's church", "Latimer and Ridley" and "Stephen" name places and people the brief still tells, by role: "the university church", "the other two bishops", "the first martyr". So they stand.

None has quotation marks.

## 4. Census rules

- Keys: all allowed. No `briefLength`.
- Five quoted spans, five entries, each `modern` exactly the brief's, including the comma in "like a Christmas game,".
- [1], [3] and [4] are under six words and carry "checked at card". [0] and [2] carry no `secondReading`.
- Every cited file is in `sources`. No audit, review or ruling is named. American spelling throughout the card prose.

## 5. Originals

All five are English prints, and no other original is held.

- **[0] the preface (COX 48899-48901): verbatim.** The rendering keeps every clause. "Edified" becomes "built up", which `uncertain` notes.
- **[1] "like a Christmas game" (COX 17555): verbatim.** Checked at card: the rebels' own words, as Cranmer prints them.
- **[3] "unworthy right hand" (FOXE8 7524): verbatim.** Checked at card. Foxe prints "his unworthy right hand", and the brief drops "his" without changing the sense. The margin "fire." stands before the quotation, outside the span.
- **[4] "Lord Jesus, receive my spirit" (FOXE8 7526): verbatim.** Checked at card. The margin "Cranmer" stands outside the span.
- **[2] the hand speech (FOXE8 7403-7404): KEEP, with two readings.**
  - "oflended" reads offended. A held print confirms it: Perkins prints "offended" cleanly (PERK 44210).
  - "pimished" reads punished. Foxe's scan holds the "p" and "-ished", and Perkins's damaged "unifhed" (PERK 44211) holds "-unished". Each print resolves the other, as the Palamas chapter 107 prints do.
  - Perkins copies Foxe, but he is a separate held print of the same sentence, which is what the rule asks.
  - The margin "pope, as" at the head of 7404 falls inside the span. It is a stray mark. The margin "seth the" at 7403 stands before "forasmuch", outside the span.
  - The rendering keeps Foxe's sense: "may I come to the fire" is read as "If I come to the fire".

## 6. "Not found" claims and anything left wrong

- **Foxe's unnamed informant, the 1563 edition and the marriage year: correct to leave off the card.**
- **The four conflicts with the tree's entry:** each is credited in `uncertain`, not told as fact. "Watched Ridley and Latimer burn from the roof" is rightly left off, since Foxe says otherwise (FOXE7 45576-45581).
- Nothing else found wrong.

## Fixes

**FIX 1.** `briefReferences[1]`
- Old: `Cox, Biographical Notice, on the Tower, Oxford, the condemnation of 1554 and the burning; the bishop of London's printed book of the submissions; Foxe, Acts and Monuments, vol. 8, on the hand in the fire; Clay on the book of 1559.`
- New: `Cox, Biographical Notice, on Oxford, the condemnation of 1554 and the burning; the bishop of London's printed book of the submissions; Foxe, Acts and Monuments, vol. 8, on the hand in the fire; Clay on the book of 1559.`

**FIX 2.** `briefReferences[4]`
- Old: `Cox on Mary's accession, the Tower, Oxford, the condemnation of 20 April 1554, the two bishops burned in 1555 and the stripping of rank on 14 February 1556; Foxe on the choice put to him, on why he signed, and on the bishop of London's six printed papers, with Cox's appendix.`
- New: `Cox on Mary's accession, Oxford, the condemnation of 20 April 1554, the two bishops burned in 1555 and the stripping of rank on 14 February 1556; Foxe on the choice put to him, on why he signed, and on the bishop of London's six printed papers, with Cox's appendix.`

## Scan readings to add (for entry [2])

```json
{"file": "cic/texts/foxe_acts-and-monuments-v8_cattley-townsend1837.txt", "lines": "7403", "scan": "oflended", "reads": "offended", "kind": "OCR misread"},
{"file": "cic/texts/foxe_acts-and-monuments-v8_cattley-townsend1837.txt", "lines": "7404", "scan": "pope,  as    first  be  pimished", "reads": "first  be  punished", "kind": "margin note run into the line, with an OCR misread"}
```
