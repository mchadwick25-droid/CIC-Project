# Card check: Council of Ephesus (431)

Card: `council-of-ephesus-431.card.json`, against `Card.existing.json`, the brief, `Card_Edits.md`, `Outline.md` and `Source_Sheet.md`.

## Verdict: FIX

## What holds

- Nothing moved that `Card_Edits.md` does not list. A field-by-field diff shows `rivers`, `knownFor`, `datesNote`, `issue`, `calledBy` and `traditions` are word for word. The list fields changed only by appending, and in the two Wigram corrections.
- The two Wigram corrections are justified. WIG 9272-9274 reads "had certainly not accepted Ephesus — nor had they formally rejected it — nor had they ever been asked to do either". The brief and the outline's Do not say line agree.
- Spot-checked additions all stand at their cited lines: Candidian's four days (BH 7804-7813), Hefele's ignored demand (HEF 2997-3002), the 126 and 34 (HEF 3054-3068), Philip and Arcadius (ACTS 17615-17625, 17657-17659), Canon VIII (ACTS 18395ff), the Messalians (ACTS 18769ff), the edict (HEF 6189-6196), the eight delegates (BH 1178-1185), John's letter and the condition (HEF 7463-7477, 7222-7226), the twelve anathemas left unmentioned (BH 1323-1325), Zeugma (BH 1326-1343), "Let the heavens rejoice" (ACTS 19428-19430), the late arrival (ACTS 18574-18599, HEF 2933-2941, 2992-2997, EV 1303-1307), Candidian (ACTS 17826-17834), Letter CLII (npnf203 36836-36880), Barhadbeshabba (BB 34044-34056), Badger and Sleewa (BAD1 7676-7681, BAD2 5921-5935), and the Chalcedon letters (ACTS 19395-19415, 20256-20262).
- `quotationOriginals` has one entry for each of the brief's four quoted spans. Each `printed` and `englishPrinted` stands verbatim at its file and lines: BH 8645-8647; BH 7767-7768 and 7821-7822; HEF 4977-4978; PUS 5217-5222. Every cited file is in `sources`. Only allowed keys are used. No `secondReading` is given for a quotation of six words or more. No audit file is named. Spelling is American outside verbatim print.
- Quote 1: Nau's French (NAU 7137-7139) has no word for "And" before the accuser, as stated. The Syriac is not held.
- Quote 2: Mansi, tomus 5, 76917-76919 agrees with Lupus's Latin, damaged scan aside.
- Quote 3 ("checked at card"): the rendering "by persuasion and force" matches Hefele's print, and it matches both Latin versions (below).

## Fixes

### 1. Quote 4 (the confession of 433): carry the Greek

The outline renders this quote from the Greek. It marks it "an original in a damaged print that another held print confirms" (Outline, Quotes 3), so the Kit's exception applies and the card carries the original. The reason in `Card_Edits.md` item 6 is that the clean Greek failed the validator. That is not a ground to drop it. The validator reads past listed scan faults through `tools/quote_scan_readings.json`.

I checked the Greek by hand. HEF 7243-7245 and PUS 3519-3525 agree word for word on these clauses once each print's misreads are set aside. Both prints have Κύριον against Hefele's πύριον, and ἀσυγχύτου ἑνώσεως against Hefele's ἀσυγχύτευ ἱνώσεως. Pusey has θεοτόκον against Hefele's διοτόκον. The second article must be τὴν, feminine, with παρθένον: Hefele's scan reads τὸν and Pusey's reads THY. I applied the four readings below to a copy of HEF 7243-7245 and ran the validator's `fold` match: it passes.

- `quotationOriginals[3]`: add
  - `"original": "δύο γὰρ φύσεων ἕνωσις γέγονε· διὸ ἕνα Χριστὸν, ἕνα Υἱὸν, ἕνα Κύριον ὁμολογοῦμεν. κατὰ ταύτην τὴν τῆς ἀσυγχύτου ἑνώσεως ἔννοιαν ὁμολογοῦμεν τὴν ἁγίαν παρθένον θεοτόκον"`
  - `"originalFile": "cic/texts/hefele_history-of-the-councils-v3-431-451_clark1883.txt"`
  - `"originalLines": "7243-7245"`
- `tools/quote_scan_readings.json`: add four readings for that file, each with `"kind": "OCR misread"`. On line 7244: `πύριον` reads `κύριον`; `ἀσυγχύτευ ἱνώσεως` reads `ἀσυγχύτου ἑνώσεως`; `ὁμολογοῦμεν τὸν` reads `ὁμολογοῦμεν τὴν`. On line 7245: `διοτόκον` reads `θεοτόκον`.
- `quotationOriginals[3].uncertain`. Old: "The Greek is held in two damaged prints, Pusey's (lines 3519-3525) and Hefele's (lines 7243-7245), which agree on these clauses, so the English stands alone here." New: "The Greek is given from Hefele's print (lines 7243-7245), a damaged scan, confirmed by Pusey's Greek (lines 3519-3525), also damaged. Where Hefele's scan reads πύριον, ἀσυγχύτευ ἱνώσεως and διοτόκον, Pusey's has Κύριον, ἀσυγχύτου ἑνώσεως and θεοτόκον, and the grammar needs τὴν before παρθένον." The rest of the note is unchanged.

### 2. Quote 3 ("by persuasion and force"): its note is clearly wrong

The note says the report is held "only in Hefele's English of it ... not in the original". Two held prints contradict this. Mansi, tomus 4, line 123610, at Hefele's cited p. 1397, reads "Vix igitutr potui periuafione & vi" (that is, persuasione et vi). Mansi, tomus 5, lines 77791-77792, reads "vix przvalui perfuafione ac violentia, fi oportet verius dicere" (persuasione ac violentia). Both are damaged scans, and they word it differently, so neither confirms the other and the English stays alone.

- `quotationOriginals[2].uncertain`. Old: "English only: the report is held only in Hefele's English of it (he cites Mansi, tomus 4, p. 1397), not in the original." New: "English only: the report is held in Latin in two damaged scans that word it differently, Mansi, tomus 4 (line 123610, persuasione et vi), which Hefele cites, and Mansi, tomus 5 (lines 77791-77792, persuasione ac violentia). Both say by persuasion and force." The last sentence is unchanged.

### 3. `briefReferences`: two clauses name what the brief no longer tells

- Entry 4. Old: "the sixteen days past Pentecost, the message from two of John's metropolitans, the three summonses". New: "the sixteen days past Pentecost, the three summonses".
- Entry 14. Old: "Cyril's letter to Nestorius and his letter of peace to John of Antioch read and received, and the order of Ephesus kept." New: "Cyril's letter to Nestorius and his letter of peace to John of Antioch read and received."

### 4. Items the outline sends to the card are missing

Append each item at the end of the field named.

- `attended`, new item (Cut first 1; ACTS 18586-18592): "After the sixteen days, two of John's metropolitans, Alexander of Apamea and Alexander of Hierapolis, arrived first. They said John had told them to announce that if anything delayed him, the council should not be put off but should do what was right (the council's letter to Celestine)."
- `attended`, new item (Cut first 8; HEF 2986-2988): "Nestorius, by Hefele's account, sent word that he would appear as soon as all the bishops were assembled."
- `attended`, new item (Leave out, "for the card"; ACTS 17531-17536, 17627-17640): "When Celestine's letter was read at the second session, the bishops cried out, \"To Cœlestine, a new Paul! To Cyril a new Paul!\" and \"One Cœlestine! One Cyril!\" At the third session the legate Philip said that Peter, head of the Apostles, lives and judges in his successors, and that Celestine holds his place (acts, Sessions II and III)."
- `attended`, new item (Cut first 10; ACTS 17838-17846): "At John's assembly, Candidian told how Cyril's side had met five days before, in spite of all warnings, and declared that Nestorius had been condemned unheard (Hefele, in the editor's excursus to the English acts)."
- `decided`, new item (Cut first 9; ACTS 17276-17277): "The decree says the bishops came, \"with many tears, to this sorrowful sentence\" (the decree against Nestorius)."
- `calledBy` (Cut first 5; HEF 2838-2848). Append after "(the emperor's edict, as Hefele summarizes it)": ". By the same edict, he was to take no part in the debates on the faith, and was to keep order by removing from the city the monks and laymen who came out of curiosity".

`Card_Edits.md` should then list fixes 1 to 4, and item 6's reason should be withdrawn.

## Not found, and nothing else clearly wrong

The writer lists no claim as not found. I found nothing else clearly wrong in the starting card or the additions. There is no new census entry to check.
