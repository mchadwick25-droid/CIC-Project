# Card check: Dhuoda

**Verdict: FIX** (three references).

Base: the census card for `dhuoda`. Diffed field by field: only `briefReferences` and `quotationOriginals` differ, as `Card_Edits.md` lists.

## 1. Edits justified

Every listed edit checks against its evidence. Re-read:
- DH 1893-1894, 3163-3178, 11364-11370, 11964-11968, 11999-12002.
- The table of chapters, per sheet A2.
- AB 2415-2417.

The quotation marks dropped from the references match the brief, which quotes none of those words.

## 2. Nothing else moved

Confirmed. Every other field is word for word.

## 3. References

The flagged four are ruled under rule 3.
- **Removed:** the opening verses, Aachen 824, the board game, and the Histoire littéraire's praise.
- **Kept:** "William born 826". It grounds the brief's "William had just turned fifteen" (sheet E2, A4).
- **Kept:** the closing note's "the year missing". It grounds "more than a year" (sheet E11, D1).

FIX 1. `briefReferences[1]`. Remove the entry. The brief does not tell the opening verses, the discord or the acrostic.
- Old: "Liber manualis, opening verses: the kingdom and homeland in discord; the acrostic to William, read by Delisle."
- New: (entry removed)

FIX 2. `briefReferences[2]`
- Old: "Liber manualis, preface: married at Aachen, 824; William born 826; Louis's death; the second son born at Uzès in 841 and brought to Bernard in Aquitaine with Elefantus, bishop of Uzès, before baptism; she stays at Uzès sub jussione senioris mei; she dictated the book and had it written out and sent; a mirror and a board game."
- New: "Liber manualis, preface: William born 826; Louis's death; the second son born at Uzès in 841 and brought to Bernard in Aquitaine with Elefantus, bishop of Uzès, before baptism; she stays at Uzès sub jussione senioris mei; she dictated the book and had it written out and sent; a mirror."

FIX 3. `briefReferences[11]`. The "oldest writing" claim is Bondurand's own (DH 1854-1855). The copies agreeing comes from DH 402-410, and Delisle is quoted for the printings.
- Old: "Bondurand's introduction, quoting Delisle and the Histoire littéraire: the Nîmes and Paris copies agree; un monument respectable de literature et de piété; the oldest writing by a woman born in France."
- New: "Bondurand's introduction, quoting Delisle: the Nîmes and Paris copies agree; the oldest writing by a woman born in France."

All other references name what the brief tells.

## 4. Census rules

Pass.
- Only allowed keys, and no `briefLength`.
- There are three quoted spans and three entries, and none is left over.
- The three removed entries ("in discord", "at my lord's command", "the manual of Dhuoda") are no longer quoted in the brief.
- Each `printed` stands at its lines: DH 1893-1894, 3165-3167 and 3169-3171.
- The cited file is in `sources`.
- There are no quotation marks in the references.
- No audit is named.
- The spelling is American.

Two entries have no `secondReading` yet. That is expected at step 7.

## 5. Not found, and left in

The edit list has no "not found" claims. Nothing clearly wrong is on the card.

Note, outside the card: the brief says she asks for the epitaph to be "carved". Her word is "transcribere", to write it on the tomb (DH 11968). The card's "written on her tomb" is the closer reading.
