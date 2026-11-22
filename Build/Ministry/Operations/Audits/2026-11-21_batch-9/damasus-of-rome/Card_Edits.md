# Card edits: Damasus of Rome (`damasus-of-rome`)

Starting card: `Card.existing.json`. New card: `damasus-of-rome.card.json`. Every field not listed here is word for word as it was. No `briefLength` (the validator does not allow it). `secondReading` is left off the three quotation entries (each is six words or more); release sets it.

File keys: AMM = `ammianus-marcellinus_roman-history_yonge1862.txt`; AVE = `collectio-avellana_epistulae-imperatorum-pontificum-pars1-lat_guenther1895-csel35.txt`; CHR = Jerome's Chronicle (Fotheringham); RUF = Rufinus X (Schwartz-Mommsen); SS = `npnf202_socrates-sozomen-ecclesiastical-histories.xml`; THD = `npnf203_theodoret-jerome-gennadius-rufinus.xml`; JER = `npnf206_jerome-principal-works.xml`; PL23 = Migne's Jerome; CTH = `theodosianus-16_mommsen-meyer1905.txt`; CTL = `codex-theodosianus_latinlibrary.txt`; LPD = Duchesne's Liber Pontificalis, `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt`; BAS = `npnf208_basil-letters-select-works.xml`; MAN3 = Mansi vol. 3.

## Clearly wrong

None found.

## Flagged, left in place

- `knownFor`, "an election fought with clubs and swords", is stated as fact. The clubs and swords are held only in the Ursinian account (AVE 5107 "fustibus"; AVE 5159 "securibus gladiis et fustibus"); Ammianus says only that the partisans carried their violence to actual battle (AMM 23176-23182). No held source contradicts the sentence, and the brief does not use it, so it is not changed. A new `uncertain` entry names the account that holds it.

## New: legacy.traces (appended)

1. Jerome expects to be called a forger; Fremantle dates the preface 383: JER 46631-46646, JER 46629.
2. His verse on Peter and Paul: LPD 27770-27779 (OCR "Borna ... nierait" read Roma ... meruit; the first lines are confirmed in part by Turner, `turner_ecclesiae-occidentalis-monumenta-iuris-antiquissima-tom1-fasc1-lat_1899.txt` 35321-35322).
3. Vigilius's inscription: LPD 127955-127960 (sixth century, per the source sheet).
4. Sozomen retells the law: SS 40612-40617.
5. Theodoret at Antioch, Sapor, Flavian: THD 15484-15506.
6. About 449 Theodoret quotes the anathema: THD 34897-34903 (the date is the editor's, THD 34776-34778).
7. The Eastern bishops' letter: THD 37891-37895 (quotation verbatim).
8. The Breviary of 1908: `cic/texts/roman-breviary_bute1908.txt` 2622-2625.

## New: legacy.remembered (appended)

- Burial on the Via Ardeatina beside his mother and sister: LPD 127456-127459 (late).

## New: uncertain (appended after the old five, in this order)

1. Juventius withdrawing; Praetextatus appeasing the tumult: AMM 23176-23182, 23972-23986.
2. Jerome's Chronicle, Rufinus, Socrates on the election: CHR 46055-46058, 46085-46088; RUF 30176-30181, 30222-30226; SS 14200-14216.
3. The Ursinian account's further charges, the clubs and swords credited to it alone, and the two names for the besieged church: AVE 5147-5153, 5157-5168, 5196, 5201-5202, 5223-5241.
4. The Liber Pontificalis's interpolated election lines, and Jackson's nominee note: LPD 127130-127133, 127699-127732; THD 10205-10208.
5. The order opening the Sicininum church, Günther's dates: AVE 7933-7951, 7965.
6. The council at Rome, Rimini annulled, 369 as Hartranft's note, Latin differing from Greek: SS 38808-38820; THD 10203-10204.
7. Rufinus's account of Apollinaris's teaching; the year of the council: RUF 30635-30646; SS 39030-39039.
8. Basil: BAS 28593-28625, 41012-41035; BAS 8112-8115.
9. The rescript to Aquilinus and Günther's dates; the council's letter and Duchesne's 380: AVE 8256-8262, 8444-8449, 8460-8466; LPD 127972-128007.
10. The council's letter on Isaac and the Liber Pontificalis's charge: LPD 127980-127994 (the same lines, read in Duchesne's clean reprint rather than Mansi's scan, MAN3 62301-62316).
11. Duchesne on the tombs: LPD 127928-127937. Outline "For the card".

## New: sources

- `ownWords`: LPD (his verses and epitaph, for the new quotation and trace).
- Existing Socrates and Sozomen title, old: "...; Book 6, chapter 23 (Sozomen)". New: "...; Book 6, chapters 23 and 25, and Book 7, chapter 4 (Sozomen)". Evidence: SS 39030, SS 40612.
- Existing Jerome Letters title, old: "Letters 15 and 123; Preface to the Four Gospels". New: the same, then "; Against John of Jerusalem, chapter 8" (JER 40869-40872).
- Added files: THD (Church History 4.19, 5.2, 5.3 and letters), AVE (petition, order, rescript), CHR, RUF, PL23, CTH, CTL, LPD, BAS, the 1908 Breviary.

## New: briefReferences (fifteen entries)

Each names only what the brief tells, with lines as above: AMM 23176-23189, 23972-23986; AVE 5097-5168, 6673-6684, 7933-7951, 8444-8449; CHR 46055; RUF 30176, 30635-30652; SS 14200, 38799-38820, 39030-39039; THD 14599-14605, 15395-15423, 16117-16120; CTL 6883; LPD 127133-127136, 128201-128214; JER 46631, 2929; THD 41382-41385.

## New: quotationOriginals (three, one for each quoted span)

1. Praetextatus's joke: printed in Fremantle's English, JER 40871-40872. The Latin in PL23 27958-27960 is damaged at the name of the city (scan: "Πο- mans"); Mansi's print (MAN3 42056-42058) reads "Romane urbis" but is itself a scan with long s read as f ("Chrifianus"). No Latin print is whole, so the card prints the English alone and says so; the modern "of the city of Rome" follows the Latin "Romanae urbis". If the card checker wants the Latin printed, `tools/quote_scan_readings.json` needs a listing for PL23 lines 27958-27959.
2. The law of 380: printed in Latin from CTL 6883 (the Latin Library; edition not stated, so the card notes that Mommsen and Meyer's critical text, CTH 83597-83601, reads the same, apart from scan slips such as "Cuncios"). The file is lower-case throughout; the card prints it as it stands. The outline's "also CTL 6883" is this line.
3. The epitaph: printed Latin at LPD 128214 (the only print held; lines 128206 and 128210 are damaged, this line is clean). No English print exists, so the Latin is the printed wording.

## Not found (left in place)

None. Every statement on the existing card checks against the sheet rows listed in `Source_Sheet.md` (S1-S8, E1-E13, E43, E45, E52, E53).

## Conflicts with the census entry

None. The census `dates` and `teaser` agree with the card.
