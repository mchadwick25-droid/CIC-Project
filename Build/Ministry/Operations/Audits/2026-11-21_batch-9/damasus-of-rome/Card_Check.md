# Card check: Damasus of Rome (`damasus-of-rome`)

**Verdict: FIX** (four changes).

## Checks

1. Edits against evidence: the new traces, remembered lines and uncertain entries hold at AVE, AMM, CHR, RUF, SS, THD, LPD and BAS (AVE 5154-5202: clubs, axes, swords, fire, 160 dead, the fifth war, the ear-tickler).
2. Unlisted fields: the diff against `Card.existing.json` shows only the listed edits.
3. `briefReferences`: one entry names something the brief no longer tells (FIX 3).
4. Census rules: allowed keys; three `quotationOriginals`, one per quoted span. Each `printed` stands at its lines (validator on a scratch census). But the outline renders the Praetextatus line from Jerome's Latin, and the card does not carry that Latin (FIX 2). Mansi is cited and not in `sources` (FIX 2).
5. "checked at card": none.
6. Not found: none. Clearly wrong left in: `knownFor` (FIX 1).

## FIX

1. `knownFor`. The clubs and swords stand only in the Ursinian account (AVE 5107, 5159). The brief gives the weapons as that account's alone: "That is one side's charge." It also says "the accounts disagree". The outline's own guard reads: "'Damasus's men used clubs' as fact → the clubs are in the Ursinian account" (Outline.md line 94). Stating the clubs and swords as fact contradicts the brief. "Deadly violence" is what the brief says ("a fight that left many dead") and what Ammianus holds (AMM 23176-23189, 137 dead).
   - Old: "after an election fought with clubs and swords,"
   - New: "after an election fought with deadly violence,"
2. `quotationOriginals[0]` (Praetextatus). The damaged word is confirmed by another held print: Mansi, MAN3 42058-42060, has "Romane urbis". So the Latin goes on the card, as the outline renders from it (Outline.md line 59).
   - Add `"original": "Facite me Romanae urbis episcopum, et ero protinus Christianus"`, `"originalFile": "cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt"`, `"originalLines": "27958-27960"`.
   - Add two listings to `tools/quote_scan_readings.json` for that file. Lines "27958": scan "Facite me Πο-", reads "Facite me Ro-", kind "OCR misread (Latin letters read as Greek)". Lines "27959": scan "mans urbis", reads "manae urbis", kind "OCR misread". Tested on a scratch copy: the `original` then validates.
   - In its `uncertain`, old: "(lines 42056-42058 of its file)", new: "(lines 42058-42060 of its file)". Old: "The English print stands alone.", new: "The Latin is printed with Romanae as Mansi reads it."
   - Add to `sources.about`: `{"title": "Sacrorum conciliorum collectio, volume 3, note on Damasus", "author": "Giovanni Domenico Mansi", "date": null, "language": "Latin", "file": "cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-3-347-409-lat_welter-facsimile1901.txt"}`.
3. `briefReferences[6]`. The brief no longer tells "the judgment of the apostolic see". Old: "Rufinus, Church History 10, and Sozomen 6.25: Damasus and the bishop of Alexandria condemn Apollinaris in council at Rome. Damasus's letter in Theodoret: the judgment of the apostolic see." New: "Rufinus, Church History 10, and Sozomen 6.25: Damasus and the bishop of Alexandria condemn Apollinaris in council at Rome."
4. `uncertain[15]`. The same entry gives Duchesne's reason (the tradition had grown obscure, so the tombs had to be identified), and `legacy.remembered[3]` quotes Northcote and Brownlow's reason. "The sources give no reason" is too wide. It is the Liber Pontificalis (LPD 127133-127136, "requisivit") that gives none.
   - Old: "The sources give no reason for the searching out of the graves."
   - New: "The Liber Pontificalis gives no reason for the searching out of the graves."
