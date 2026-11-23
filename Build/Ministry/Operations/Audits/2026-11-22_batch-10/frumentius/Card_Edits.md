# Card edits: Frumentius (`frumentius`)

Existing words: every one kept as it was. No existing sentence was changed, reordered or cut. All edits below are additions (old words: none).

## Corrections

None. No held source or the brief contradicts any existing statement.

## Not found (left in place)

- `legacy.traces[0]`: "among the Roman merchants and the king's household". Rufinus (RUF 27326-27330) and Socrates (N202 4343-4349) give the Roman traders only; no held text names the king's household as where the church began.

## Additions

Files: RUF = eusebius_werke-bd2-2 (Rufinus); N204 = npnf204; PG25 = athanasius_opera-omnia-pg25; others by their `cic/texts/` names.

1. `legacy.traces`, new item: Ludolf's count of ninety-five metropolitans. Evidence: LUD 18719-18724 (informant, file header line 8); brief paragraph 11.
2. `legacy.remembered`, new item: Ethiopian book of saints, 26 Hamle, Abba Salama, the Revealer of the Light, peace of Christ, fifteenth-century Ge'ez. Evidence: SYN 43570-43612; SYN1 1089-1094 (dating, not cited in card); brief last paragraph.
3. `legacy.remembered`, new item: Sozomen's praise, Greek calendar 30 November, Roman Martyrology 27 October. Evidence: N202 29925-29928; NIKO 23208-23209, 35442-35443; BRV 83690-83726.
4. `legacy.remembered`, new item: John of Nikiu (file header: late 7th century; NIK 4672-4677) and Mingana on the Syriac chroniclers (MIN 1150-1155).
5. `uncertain`, new item: no answer to the letter known; letter about 356 by Robertson's dating (N204 7299); end of 346 earliest possible (N204 10403-10408). Brief paragraphs 9 and 10.
6. `uncertain`, new item: Theodoret's drowned-and-captured crew (N203 7719-7724); Jackson on "Roman way" (N203 7739-7742).
7. `uncertain`, new item: Philostorgius's Theophilus at Aksum, no Frumentius (PHI 160).
8. `uncertain`, new item: the late book's differences (SYN 43570-43612: Alameda, Abreha and Asbeha, "the work of war", the children brought up); Rufinus has none (RUF 27316-27330).
9. `uncertain`, new item: the royal stone (LIT 483, 567-569) and Nöldeke's match to Sazanas (LIT 1500-1501), marked a modern reconstruction.
10. `sources.about`, nine new entries: PG25 (Greek letter), LUD, SYN, PHI, NIK, NIKO, BRV, LIT, MIN. Each file exists under `cic/texts/`.
11. `briefReferences`, new (seven items): Rufinus, the three Greek retellings with Valesius (N202 4287-4288), the letter, Robertson (N204 1519, 5676-5684, 10405-10408), Ludolf, the Synaxarium, the census tradition entry. No quotation marks.
12. `quotationOriginals`, new (four entries, one per quoted span in the brief; no `secondReading`, all six words or more):
   - Edesius: printed Latin RUF 27383-27385, verbatim.
   - Athanasius as Rufinus reports him: printed Latin RUF 27376-27377, verbatim (print reads "sieut", noted).
   - "So send Frumentius ...": printed English N204 36144-36145 only. The Greek (PG25 92806-92807, checked by hand: Frumentius the bishop, send out most speedily, into Egypt) is held only in a damaged scan, so no `original` is given.
   - "This Frumentius was set ...": printed English N204 36150-36151; Greek PG25 92812-92814 checked by hand (set in this rank, Athanasius, liable to countless evils), not printed, same reason.

## Left out

- `briefLength`: the validator's allowed keys do not include it.
- Connections to other entries.

## Validator

Run on a one-entry copy of the census (the full run was killed for memory by other sessions), with the new brief as the entry's text. Remaining errors are only the expected ones: `secondReading` missing on the four quotations and the four modern renderings not yet listed in `tools/quote_renderings.json` (both set at release), plus faults of the one-entry copy itself. No key, file, line or wording error.

## Scan readings to add

For `tools/quote_scan_readings.json`, file `cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt`:
- Line 92806 "Οὐχοῦν" reads "Οὐκοῦν" (OCR misread, χ for κ); line 92806 "Φρουμέντιον (36)" reads "Φρουμέντιον" (footnote marker run into the line); line 92807 "ἐπίσχοπον" reads "ἐπίσκοπον" and "ἐχπέμπετε" reads "ἐκπέμπετε" (χ for κ).
- Lines 92813-92814 "βίον χατ- \nἔστησεν" reads "βίου κατέστησεν" (OCR misread, ν for υ and χ for κ, across the line-end hyphen); line 92814 "χαχοῖς" reads "κακοῖς" (χ for κ).

## Second pass (2026-11-23)

**Checker changes (all applied word for word)**
1. `quotationOriginals[2]`: Greek original added (`originalFile` the Migne PG 25 file, `originalLines` 92806-92807); its `uncertain` replaced as given. Applied word for word.
2. `quotationOriginals[3]`: Greek original added (92812-92814); its `uncertain` replaced as given. Applied word for word. (The old `uncertain` sentence stood once in each of the two entries, so each was changed in its own entry.)
3. `uncertain[7]`: "names the king Alameda," became "calls him Fremenatos, names the king Alameda,". Applied word for word.
4. `uncertain`: new last item on Rufinus's opening. Applied word for word.
5. `sources.about`: new last entry, Budge's volume 1 introduction. Applied word for word.
6. `briefReferences[6]`: census entry line changed as given. Applied word for word.

**Items added from the outline:** none. Every "to the card" item is already held or was worded by the checker:
- Theodoret's drowned and captive crew (Outline l.32; N203 7719-7723): held, `uncertain[5]`.
- Rival Aizanas stone (Outline l.38; LIT 483, 567-569, 1500-1501): held, `uncertain[8]`.
- Philostorgius's envoy (l.101; PHI 160): held, `uncertain[6]`.
- Rufinus's opening (l.104): checker change 4.
- Ethiopian book's Fremenatos, Alameda, Abreha and Asbeha, the work of war (l.105, 110): held in `uncertain[7]`; Fremenatos by checker change 3.
- Greek calendar and Roman Martyrology (l.111): held, `legacy.remembered[3]`.
- John of Nikiu (l.112): held, `legacy.remembered[4]`.
- Syriac chroniclers (l.113): held, `legacy.remembered[4]`.
- Sozomen's "no less than an apostle" (l.114): held, `legacy.remembered[3]`.
- "In the Roman way" (l.115; N203 7739-7742): held, `uncertain[5]`.

**Skipped:** none beyond the above.

**Validator** (`--skip-quotes`, scratch census): 14 errors for this entry, all expected before release: secondReading missing on the four quotations; brief-quote mismatches because the scratch entry still holds the old brief; the two new Greek originals not standing until the scan readings above are added.
