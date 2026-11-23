# Pelagius: card check, modern pass

Checked `pelagius.card.json` against `Card.pass3.json`, the section "Fourth pass: no modern opinion (2026-11-23)" of `Card_Edits.md`, and `pelagius.brief.txt` as it now stands. Role: `Brief-Kit/roles/card.md`, check pass.

**Verdict: FIX (one change, two fields).**

## What holds

- Nothing moved outside the edit list. A JSON diff of the pass-3 card and this card shows only the four new `uncertain` entries and the four `briefReferences` changes listed.
- Lines re-read: NPNF105 880 (Warfield: Alaric, "landed together in Africa (A.D. 411)", "departed for Palestine"); NPNF105 10286-10287 (Augustine: arrival, the glimpse while "preparing for the conference ... with the heretical Donatists", "hastened away across the sea"); PL33 62249-62250 (damaged, "417, aut ... 418"); CSEL57 4484-4515 (no date in the letter); NPNF105 10615-10621 (endnote dates the two books to 418; Augustine's text says "After ... first Innocent, and then Zosimus"); NPNF105 11255 ("when I was in the East, to ... Demetrias"); NPNF211 15434 (the editor's "A.D. 430"). Each matches its entry.
- The Maurist, Retractations-editor and Cassian-editor entries each credit the view by name to its modern source and mark it as modern.
- `briefReferences`: the Diospolis entry no longer names December 415. No entry names wording the brief no longer has. The brief's cut "Pelagius was then in the East" is not on the card. The two new entries match brief lines 1 and 15.
- `quotationOriginals`: the brief's three quoted spans are unchanged; no entry added or dropped.
- The year 417 (Zosimus). The card never calls it only an editor's date. The `uncertain` entry and the `sources` title give "21 September 417" as plain fact, which AVELL 11204-11211 supports (the preceding letter dated "Honorio Aug. XI. et Fl. Constantio ... conss.", with the September letter at 11493-11497). `datesNote` ends "(B. B. Warfield's dates)". That credits Warfield for the dates he gives. It does not say no old source holds them, so it stands.

## The fix: the 411 bound

The new Warfield entry in `uncertain` calls the 411 landing "his judgment". It also says Augustine "says only that Pelagius reached Africa and hurried away across the sea". That treats 411 as only Warfield's, and it is wrong against the held text. Augustine ties his glimpse of Pelagius in Africa to the preparations for the conference with the Donatists (NPNF105 10286-10287). The conference's own record is dated "Post consulatum Varanis V. C. calendis juniis Carthagine", that is 1 June 411 (PL43 54339; OCR reads "Pott consulatum Yaranis"). The outline's Do not say line sends this bound to the card ("Held only through Augustine's tie to the Donatist conference ... itself dated 1 June 411 by its record (PL43 54339) ... Card.", Outline.md 114). It also contradicts the card's own earlier `uncertain` entry, which already tells the Donatist tie.

1. Field `uncertain`, the entry beginning "B. B. Warfield, a modern editor":
   - Old: `B. B. Warfield, a modern editor, says that Pelagius and Caelestius fled Alaric's second raid on Rome and landed together in Africa in 411, and that Pelagius soon afterwards departed for Palestine. This is his judgment. Augustine, whom he draws on, says only that Pelagius reached Africa and hurried away across the sea.`
   - New: `B. B. Warfield, a modern editor, says that Pelagius and Caelestius fled Alaric's second raid on Rome and landed together in Africa in 411, and that Pelagius soon afterwards departed for Palestine. The flight, the landing together and the voyage to Palestine are his judgment. Augustine, whom he draws on, says he glimpsed Pelagius in Africa while preparing for the conference with the Donatists, and that Pelagius hurried away across the sea. The conference's own record dates it to 1 June 411.`

2. Field `sources.about`, add one entry at the end (the file is now cited):
   - Old: (none)
   - New: `{"title": "Acts of the Conference of Carthage with the Donatists (Gesta Collationis Carthaginiensis), opening date line, in Migne, Patrologia Latina 43", "author": "The conference of Carthage, 411", "date": null, "language": "Latin", "file": "cic/texts/augustine_scripta-contra-donatistas-opera-omnia-t9-lat_migne-pl43.txt"}`

No other change. After the fix, run `node tools/validate-census.mjs --skip-quotes` on a scratch census again.
