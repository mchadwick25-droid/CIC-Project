# Card edits: Epiphanius of Salamis (`epiphanius-of-salamis`)

Starting card: `Card.existing.json`. New card: `epiphanius-of-salamis.card.json`. Every field not listed here is word for word as it was. No `briefLength` (the validator does not allow it). `secondReading` is left off both quotation entries (each is six words or more); release sets it.

File keys: HOLL1 = `cic/texts/epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`; J6 = `npnf206_jerome-principal-works.xml`; J3 = `npnf203_theodoret-jerome-gennadius-rufinus.xml`; SS = `npnf202_socrates-sozomen-ecclesiastical-histories.xml`; SOZG = `sozomen_historia-ecclesiastica-tomus2-libri-5-9-grc-lat_hussey1860.txt`; PALL = `palladius_dialogue-life-of-chrysostom_moore1921.txt`; AUG = `augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt`; MEN = `mendham_seventh-general-council-second-of-nicaea_1850.txt`; PHOT = `photius_library-v1_freese1920.txt`.

## Clearly wrong (three edits, fewest words)

The Library holds the Panarion in Greek from heresy 1 (HOLL1, "Ancoratus und Panarion haer. 1-33", Holl 1915) and the Ancoratus (HOLL1 from line 1576, "Ancoratus 1, 1-2, 5"; Ancoratus 10-13 at lines 2509 and 2629).

1. `keyWorks[0].about`. Old: "...heresies 34 to 80 are held in Greek". New: "...heresies 1 to 80 are held in Greek". Evidence: HOLL1 (1 to 33), HOLL2 (34 to 64), PG 42 (65 to 80).
2. `keyWorks[1].about`. Old: "...; not held in the Library". New: "...; held in Greek". Evidence: HOLL1 1576, 2509, 2629. Sozomen's report of Ammonius naming The Anchored is SS 43614.
3. `uncertain[5]`. Old: "The Library holds the Panarion only from heresy 34 on, in Greek, and the Ancoratus not at all." New: "The Library holds the Panarion in Greek from heresy 1 on, and the Ancoratus in Greek." Evidence: as above.

Also added to `sources.ownWords`: HOLL1 (the file those corrections rest on).

## New: legacy.traces (appended)

- Augustine followed his order, took fifty-seven heresies, and says the Greeks counted him among the great: AUG 2411-2426 (the Latin: "ordinem sum secutus", "quinquaginta septem ex Epiphanii ipsius opere in meum transtuli", "apud Grecos inter magnos habitus"), editors' date AUG 1098 ("circiter annum 428"). Outline "For the card", Augustine's extras.
- Photius: PHOT 11676-11684. Outline "For the card", Photius.
- Hilarion's praises: J6 30110-30112. Outline "For the card", Hilarion.

## New: legacy.remembered (appended)

- Taught from youth by ascetics, most of his time in Egypt: SS 39795-39797 (Sozomen). Outline "For the card".
- His giving: SS 42340-42345. Outline "For the card".
- Monks came to Cyprus for love of him: J6 21024-21027 (Jerome, Letter 108). Outline "For the card".
- Thirty-six years: PALL 8919-8921. Outline "For the card".
- A bright star among bishops (the quotation stands verbatim in J6 22472-22474, Letter 113): outline "For the card", Theophilus's change of view; the existing card already holds the Dialogue's half of it.

## New: uncertain (appended after the old six, in this order)

1. The count of the Panarion's books: HOLL1 12394 ("διὰ βιβλίων τριῶν"), PHOT 11650-11652 (three volumes, seven books), AUG 2424-2425 ("sex libros"). Source sheet, I1.
2. His reasons for the ordination and the curtain: J6 10651-10660, 10702-10706 (no priest to celebrate; fear of estrangement), J6 10653-10654, 10713-10714 (not under Jerusalem's jurisdiction), J6 11105-11108 (image of a man in Christ's church). Review M2, sent to the card by the recheck. The letter's English only, from Jerome's Latin of his Greek (J6 10627-10628, 13202-13212).
3. Jerome's translation charge, Rufinus named, the six thousand books: J6 13190-13225 (Letter 57 §1-2), J6 10977-10978, J3 53880-53902. Outline "Leave out": the jibe and the translation quarrel go to the card.
4. John Chrysostom driven out a short time after: SS 18225-18230. Review, "John's being driven from his see ... is for the card".
5. The farewell at the shore, Sozomen's report: SS 43620-43626; SOZG 30108-30116 (Greek read by hand: Ἀφίημι ὑμῖν τὴν πόλιν καὶ τὰ βασίλεια, καὶ τὴν ὑπόκρισιν· ἐγὼ δὲ ἄπειμι· σπεύδω γάρ, πάνυ σπεύδω, "I leave you the city and the palace and the acting; but I am going away; for I am in haste, in great haste"); Moore's note PALL 4740. Outline's dropped Q3.
6. The writings against images: MEN 26231-26239, 26273-26281, 26282-26316, 26327-26331. Outline, What came 3 and source sheet I3 (Contested).
7. Paula's ten days and Olympias's gifts: J6 21019-21026; PALL 9584-9588. Outline "Leave out", "card".
8. Late feast days: ETH 29512-29521 (17 Genbot, "On this day died the great Saint Epiphanius"); ACTA 16081 (12 May). Outline "Leave out", "card"; marked late legend.

## New: sources.about

- Existing npnf206 entry title, old: "Letter 57, to Pammachius; Letter 66, to Pammachius". New: the same, then "; Letter 108, to Eustochium; Letter 113, from Theophilus to Jerome; Against John of Jerusalem, chapter 11; Life of Hilarion" (J6 21019, 22446, 40982, 30110).
- Existing npnf203 Jerome entry title, old: "Lives of Illustrious Men, chapter 114, with Richardson's note". New: the same, then "; Apology against Rufinus" (J3 53880-53902).
- Added files: AUG, PHOT, MEN, SOZG, the Ethiopic Synaxarium (`cic/texts/ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt`), the Acta Sanctorum (`cic/texts/acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt`).

## New: briefReferences (eleven entries)

Each names only what the brief tells: the Proems (HOLL1 12381-12399, 13363-13364, 13424-13434, with Holl's note at 13447), Panarion 33 (HOLL1 34006-34011, 34016-34746), Panarion 77 (PG42 48853-48857), Sozomen 6.32 (SS 39793-39798), Against John 11 (J6 40982-41015), Letter 51 (J6 10813-10818, 10899-10922, 10676-10700, 11096-11120), Socrates and Sozomen on Theophilus, Constantinople and the death (SS 17868-17899, 18078-18230, 43502-43631), Augustine (AUG 2411-2426), Nicaea II and the Caroline Books (MEN 26273-26316), and the tradition.

## New: quotationOriginals (two, one for each quoted span)

1. The Panarion preface, "We are going to show you ... fall into it.": printed Greek at HOLL1 12387-12391. Holl's print is the only one held, and its scan has three slips inside the span (line 12388 "TE" for τε; line 12390 "zal" for καί; line 12391 "προχαταληπτικὰ" for προκαταληπτικὰ). The card prints the Greek as read by hand and says so in `uncertain`. No printed English is held, so the card cannot print an English alone from a file. **The validator needs these three listings added to `readings` in `tools/quote_scan_readings.json` before this entry validates** (I did not edit that shared file; exact, copied from the lines):
   - file `cic/texts/epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`, lines "12388", scan "τάς TE παρ᾽", reads "τάς τε παρ᾽", kind "OCR misread".
   - the same file, lines "12390", scan "δεδηγμένων zal", reads "δεδηγμένων καὶ", kind "OCR misread".
   - the same file, lines "12391", scan "προχαταληπτικὰ", reads "προκαταληπτικὰ", kind "OCR misread".
   With those three listed, the validator (run on a scratch copy with the entry in place) raises no error on the entry; the only errors left are the two renderings that `tools/quote_renderings.json` gets at release.
   Greek checked by hand: "For since we are about to show you the names of the heresies and uncover their unholy deeds, being like venoms and poisons, and together with them to fit antidotes, remedies for the bitten and preventives for those about to fall into this."
2. The Euphrates: printed at J6 10920-10922 (Fremantle's English); Greek and Jerome's Latin not held. English stands alone.

## Not found (left in place)

None. Every other statement on the existing card is held: the birth, the dates, the Zenos note, the Dialogue's change of view, Sozomen's and Jerome's lines.

## Conflicts with the census entry

None. `dates` and `teaser` in the census agree with the card.
