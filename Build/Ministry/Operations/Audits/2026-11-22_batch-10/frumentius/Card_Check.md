# Card check: Frumentius (`frumentius`)

Read: `CLAUDE.md` (Trust and source fidelity), the card role, `frumentius.brief.txt`, `frumentius.card.json`, `Card_Edits.md`, `Card.existing.json`, `Outline.md`, `Source_Sheet.md`, `Review.md`, `Fresh_Read.md`, and the cited lines in `cic/texts/`. No census entry (the person has one already).

## Verdict: FIX

## What holds

- **Nothing else moved.** Every existing field is word for word: `otherNames`, `knownFor`, `datesNote`, `placeNote`, `role`, `legacy.traces[0]`, `legacy.remembered[0-1]`, `uncertain[0-3]`, `sources.about[0-4]` (compared by script). All other content is additions, at the end of each list.
- **Additions checked at their lines:** LUD 18719-18724 (ninety-five metropolitans, Frumentius to Simeon); SYN 43570-43612 (Revealer of the Light, Alameda, the work of war, the children brought up, Abreha and Asbeha, the peace of Christ); N202 29927-29928 ("revered as no less than an apostle"); NIKO 23209, 35441-35442 (30 November, ἰσαπόστολος); BRV 83690, 83714-83726 (27 October, first bishop, a captive); NIK 4674-4677 (Afrudit); MIN 1152-1155; N204 7299 (Apology 356-7), 10403-10408 (end of 346), 5676-5684, 1519; N203 7719-7723, 7739-7742; PHI 160; LIT 483, 567-569, 1500-1501; N203 44550 ("probably 401"). Each holds.
- **Quotations:** four quoted spans in the brief, four entries, none dropped. Each `modern` matches the brief exactly. Each `printed` stands verbatim at its lines (RUF 27383-27385, RUF 27376-27377 with "sieut", N204 36144-36145, N204 36150-36151). All six words or more, so no `secondReading` and no "checked at card" entry.
- **Keys:** all allowed by `tools/validate-census.mjs`; no `briefLength`. No audit, review or ruling named. American spelling throughout. `briefReferences` carries no quotation marks, and every item names something the brief still tells.
- **Not found:** `legacy.traces[0]` "and the king's household" is rightly listed as not found and left in place: RUF 27326-27330 names only the Roman traders, but no held source contradicts it. Nothing clearly wrong is left in the existing card.

## Changes

1. **`quotationOriginals[2]`: carry the Greek.** The outline renders this quote from the held Greek (PG25 92806-92807), and gives that damaged print as confirmed by the 1892 English (N204). That matches the kit's "a damaged one another held print confirms". The census already carries Greek originals from this same PG25 file, with its scan faults listed in `tools/quote_scan_readings.json` (the `athanasius-of-alexandria` Defence of his Flight entry). So the original goes on the card.
   - Add after `"lines": "36144-36145",`:
     `"original": "Οὐκοῦν Φρουμέντιον τὸν ἐπίσκοπον ἐκπέμπετε τὴν ταχίστην εἰς Αἴγυπτον", "originalFile": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "originalLines": "92806-92807",`
   - `uncertain`, old: "The Greek of the letter is held only in a damaged scan (Migne, PG 25), so the 1892 English stands alone as the print. The modern words follow the Greek, which says to send Frumentius the bishop to Egypt most speedily, and that Athanasius put him in this rank, being guilty of countless evils."
     new: "Migne's Greek is a damaged scan, read by hand and confirmed by the 1892 English. The modern words follow the Greek, which says to send Frumentius the bishop to Egypt most speedily."
   - For release, the scan readings this original needs in `tools/quote_scan_readings.json` (PG25 file): line 92806 "Οὐχοῦν" reads "Οὐκοῦν" (OCR misread, χ for κ); line 92806 "Φρουμέντιον (36)" reads "Φρουμέντιον" (footnote marker run into the line); line 92807 "ἐπίσχοπον" reads "ἐπίσκοπον" and "ἐχπέμπετε" reads "ἐκπέμπετε" (χ for κ).

2. **`quotationOriginals[3]`: carry the Greek**, for the same reason (PG25 92812-92814, checked by hand).
   - Add after `"lines": "36150-36151",`:
     `"original": "τὸν Φρουμέντιον τοῦτον εἰς ταύτην τὴν τάξιν τοῦ βίου κατέστησεν Ἀθανάσιος, μυρίοις ἔνοχος ὢν κακοῖς", "originalFile": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "originalLines": "92812-92814",`
   - `uncertain`, old: the same sentence as in change 1.
     new: "Migne's Greek is a damaged scan, read by hand and confirmed by the 1892 English. The modern words follow the Greek, which says Athanasius put him in this rank, being guilty of countless evils."
   - Scan readings for release: lines 92813-92814 "βίον χατ- \nἔστησεν" reads "βίου κατέστησεν" (OCR misread, ν for υ and χ for κ, across the line-end hyphen); line 92814 "χαχοῖς" reads "κακοῖς" (χ for κ).

3. **`uncertain[7]`: the name the outline sends to the card.** Outline, Cut first 1, sends "it calls him Fremenatos" to the card (SYN 43575-43576, 43585); the card dropped it.
   old: "The Ethiopian book of saints, a late compilation, names the king Alameda,"
   new: "The Ethiopian book of saints, a late compilation, calls him Fremenatos, names the king Alameda,"

4. **`uncertain`: Rufinus's frame, which the outline's Leave out sends to the card** (RUF 27266-27269, 27302-27303; Source_Sheet line 35). Add a new last item:
   "Rufinus opens by saying that no apostle's preaching had reached this further India, and that it first received the seeds of faith in the times of Constantine."

5. **`sources.about`: the file behind the fifteenth-century dating.** `legacy.remembered[2]` dates the book "put into Ge'ez in the fifteenth century by its editors' dating", which rests on Budge's introduction in volume 1 (lines 1086-1095), not on the cited volume. Add a new last entry:
   `{"title": "The Book of the Saints of the Ethiopian Church, vol. 1, introduction (the date of the Ethiopic translation)", "author": "E. A. Wallis Budge", "date": null, "language": "English", "file": "cic/texts/ethiopian-synaxarium_book-of-saints-ethiopian-church-v1-maskaram-khedar_budge1928.txt"}`

6. **`briefReferences[6]`: the right census entry for the bishops line.** The `aksumite-christianity-conversion-era` entry says only that its first bishop came from Alexandria. "Kept taking its bishops from Alexandria" comes from `post-aksumite-ethiopian-christianity` (`why`, `relationsSummary`), as the outline cites it.
   old: "World census, Aksumite Christianity (conversion era): the setting"
   new: "World census, Aksumite Christianity (conversion era) and Post-Aksumite Ethiopian Christianity: the setting"

## Noted, not a card change

The census `why` of `aksumite-christianity-conversion-era` still says "shipwrecked", "tutor the royal household" and "around 330", against RUF 27310-27325 and the brief. The outline flagged this. It is a census change for Mark, not for this card.

## Second pass check (2026-11-23)

Compared the card at commit 265332d5 (before the second pass) with the card now, field by field (script).

1. **Changes went in as worded.** All six changes above stand exactly as given: the two Greek originals with their file and lines, the two new `uncertain` notes, "calls him Fremenatos," in `uncertain[7]`, the new last `uncertain` item on Rufinus's opening, the Budge volume 1 entry as `sources.about[14]`, and `briefReferences[6]`. Nothing else in any field moved.
2. **Second-pass additions.** None were made, so there is nothing to check at its lines.
3. **Outline "to the card" items.** Twelve, all held: Theodoret's crew (l.32) and Jackson on "in the Roman way" (l.115) in `uncertain[5]`; the Aizanas stone (l.38) in `uncertain[8]`; Philostorgius (l.101) in `uncertain[6]`; Rufinus's opening (l.104, RUF 27266-27269, 27302-27303) in `uncertain[9]`; the Ethiopian book's details (l.105, l.110) in `uncertain[7]`; the calendars and Sozomen (l.111, l.114) in `legacy.remembered[3]`; John of Nikiu and the Syriac chroniclers (l.112-113) in `legacy.remembered[4]`. None skipped.
4. **Scan readings.** Identical to the ones given above, and each scan form stands at its line (92806 "Οὐχοῦν", "Φρουμέντιον (36) "; 92807 "ἐπίσχοπον", "ἐχπέμπετε"; 92813-92814 "βίον χατ- \nἔστησεν"; 92814 "χαχοῖς"). With them, the 92812-92813 hyphen "Φρου-/μέντιον" is joined by the validator. The scan's "ὧν" and "᾿Α" fold the same as the card's "ὢν" and "Ἀ", and the card's forms are the right Greek, so they need no readings.
5. **Rules.** Allowed keys only, no `briefLength`, no audit named, American spelling throughout.

**Verdict: PASS.**
