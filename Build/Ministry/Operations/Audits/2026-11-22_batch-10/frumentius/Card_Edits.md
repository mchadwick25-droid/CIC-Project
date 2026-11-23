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

## Third pass: what it was about (2026-11-23)

Written to `Card.pass2.json`, copied from `frumentius.card.json`; every other field word for word.

**Edits**
1. `briefReferences`, new entry after the Robertson entry, for the two new explanations (the teaching, the charges).
   - Old: none. New: "Athanasius, Apology to Constantius 29 to 31, Robertson's prolegomena, Theodoret I.4 (the letter of Arius) and the Nicene creed as Athanasius gives it: the teaching of Arius and of Athanasius, the name Arians as Athanasius used it, and the charges the emperor's side made against Athanasius, which he denied."
   - Evidence: the brief's sentences on Arians, Arius and the Son, and on the charges. Lines re-read: N204 35938-35940 ("the professors of Arianism"); N203 6043-6047 (Arius: "the Son has a beginning, but that God is without beginning"); N204 19675-19680 (creed: "from the essence of the Father", "One in essence with the Father"); N204 34917-34924 and 35099-35104 (the two charges); N204 5741-5744 and 5748-5752 (Robertson). No new file: all three held files are already in `sources.about`.
2. `uncertain`, new item: "The name Arians for the emperor's bishops of 356 is Athanasius's. Robertson says the East generally rejected the Nicene wording without being Arian." Evidence: Outline, What it was about 1 (Contested note); N204 5741-5744.
3. `uncertain`, new item: "The charges the emperor's side made against Athanasius, that he turned Constans against Constantius and wrote to Magnentius, are held only with his denial in the Apology to Constantius and the emperor's assertion in the letter. Whether they were true is not settled by any held source." Evidence: Outline, What it was about 2 (Contested note); N204 34917-34924, 35099-35104, 36151-36153.
4. `briefReferences[1]`: the brief no longer says the editor's "almost word for word".
   - Old: "...: the three Greek retellings, with Valesius's note that Socrates translated Rufinus almost word for word."
   - New: "...: the three Greek retellings."
   - Evidence: the brief's "Three Greek church historians retold the story in the century after Rufinus." The Valesius point stays in `uncertain[0]`.
5. `briefReferences`, Ludolf entry removed ("Hiob Ludolf, A New History of Ethiopia: the ninety-five metropolitans counted from Frumentius."). Evidence: the brief no longer tells the 1681 count. Ludolf stays in `legacy.traces` and `sources.about`.

**Quotations:** none changed. The four quoted spans in the brief are the four `quotationOriginals` entries, wording identical. The one changed sentence ("The letter ordered:") keeps its quote as before. `secondReading` entries left as the starting card has them.

**Skipped**
- Outline item 8 (Philostorgius's envoy, "to the card"): already held in `uncertain[6]`.
- Cuts 1 and 2 ("to the card"): Ludolf's count is already in `legacy.traces`; Valesius's "almost word for word" is already in `uncertain[0]`.
- Cuts 3 to 7 (recency of the letter, sites for buildings, wife and small son as heirs, "calls Frumentius its bishop", "sharp and wise"): the outline does not send them to the card; the first is already held in `uncertain[1]`.
- Items 3 to 7 of What it was about: already explained in the brief, no new source.

**Validator** (`--skip-quotes`, scratch census copy with this card in the frumentius entry): 0 errors for this entry (0 errors overall, 4 warnings for other entries).

## Fourth pass: no modern opinion (2026-11-23)

Starting card kept unchanged as `Card.pass3.json`; edits made in `frumentius.card.json`. Every other field word for word. Lines re-read.

**Edits**
1. `uncertain[1]` (the consecration date), appended: " These are modern editors' judgments; no old source gives another date."
   - Evidence: the brief now says only "Rufinus gives no year, but sets it just after Athanasius became bishop, which was in 328." Robertson N204 5674-5684, 10405-10408; Valesius N202 4294-4296; Rufinus 27374-27375.
2. `uncertain`, new item after the consecration item. Old: none. New: "Fremantle, in his introduction to Rufinus in the Nicene and Post-Nicene Fathers, dates Rufinus's history probably 401. This is a modern judgment."
   - Evidence: N203 44550-44552 ("The date is probably 401"). The brief says "around 400", now resting on Rufinus's preface (RUF 26046-26047) and Prosper (53486-53488).
3. `uncertain`, new last item. Old: none. New: "The tree's own listing places the kingdom in what is now Ethiopia and Eritrea. That extent comes from the listing, not from any held old source."
   - Evidence: the brief now says only "in what is now Ethiopia" (SYN 43584-43585, 43597-43611); the region's extent went to the card.
4. `briefReferences[0]`: old "The editors' date for Rufinus is about 401." New "Rufinus's preface, written when Alaric's Goths broke into Italy, with Prosper's chronicle under the year 400: the date of Rufinus's writing, around 400." Evidence: RUF 26046-26047; Prosper 53486-53488.
5. `sources.about`, added Prosper's Chronicle (`cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`). Evidence: lines 53486-53488 ("Stilichone et Aureliano. a. 400"; "Gothi Italiam Alarico et Radagaiso ducibus ingressi").
6. `briefReferences[3]`: removed "Robertson's prolegomena, ". Evidence: the brief's Arians and charges rest on Athanasius (N204 35938-35940, 34915-34921, 35101-35104), not Robertson's note.
7. `briefReferences[4]`: old "Archibald Robertson's prolegomena and chronology to Athanasius: Athanasius made bishop in 328, the letter about 356, and the consecration no earlier than the end of 346." New "Athanasius, Easter letters, the Alexandrian index (Select Works): Athanasius made bishop in the consulship of Januarius and Justus, which is 328, and driven from Alexandria on the night of 13 to 14 Mechir in 356." Evidence: N204 64076-64081, 64351-64362; the brief's "After Athanasius was driven from his city in 356" and "which was in 328". Robertson's views stay in `uncertain`.
8. `briefReferences[5]`: old "The Ethiopian Synaxarium, 26 Hamle: Abba Salama, the peace of Christ, and his death in peace." New adds " ... and its lives of Cosmas and Gabriel", "and later bishops of Alexandria making the bishop of Ethiopia, which shows the book was written centuries later." Evidence: SYN 18812-18830, 25056-25069; the brief's "Centuries later ... later bishops of Alexandria still make the bishop of Ethiopia."
9. `briefReferences[6]` (world census entry) removed. Evidence: the brief no longer tells "the church of Aksum kept taking its bishops from Alexandria" or "Ethiopia and Eritrea".

**Quotations:** none changed. The four quoted spans stand word for word, and the four `quotationOriginals` entries are unchanged.

**Already held, left in place:** Littmann's fifteenth-century date (`legacy.remembered`, credited "by its editors' dating"); Ludolf's ninety-five metropolitans (`legacy.traces`); Robertson's 356 to 357 and 346 (`uncertain`); the stone of Aizanas (`uncertain`).

**Validator** (`--skip-quotes`, scratch census copy with this card and brief in the frumentius entry): 0 errors for this entry (0 errors overall, 4 warnings for other entries).
