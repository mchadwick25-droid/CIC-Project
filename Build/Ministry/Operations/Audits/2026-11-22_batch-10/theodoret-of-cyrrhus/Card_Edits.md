# Card edits: Theodoret of Cyrrhus

Card: `theodoret-of-cyrrhus.card.json`, from `Card.existing.json`. Everything not listed here is word for word as it was. Checked with `tools/validate-census.mjs --skip-quotes` on a temporary copy of the census with this card and the brief in the entry (the full run is killed for memory in this environment). The only errors on the entry are the missing `secondReading` on the three quotations of six words or more, which release sets. No `briefLength`, no connections.

## Correction (1)

- `uncertain[1]`. Old: "which the Library does not hold." New: "which the Library holds in Greek." Evidence: `cic/texts/theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt` is held (Simeon at lines 113735-113738); the brief draws on it.

## New: `uncertain` (7 entries appended)

1. Letter to Nestorius kept only in Latin; date Inferential-Thin. Evidence: NP3 37972-37974 (Greek copies perished, three Latin versions), 37982-37986 (follows one version; date "not long after" the Chapters), 37999-38003 (he has accepted the Egyptian writings).
2. No charge and no accuser is his own complaint; the acts show Pelagius's libel; no year for the order. Evidence: NP3 31456-31458; P449 13316-13323; NP3 2911-2916. Brief: "with no charge and no accuser, he wrote."
3. Date of the deposition. Evidence: P449 header (session of 22 August 449); NP3 2956-2957 (8 August); NP3 33034-33036 (11 August).
4. Chalcedon session eighth or ninth. Evidence: NP3 3304; EVW 5242.
5. Return to Cyrrhus doubtful. Evidence: NP3 3350-3353.
6. The bribe is the Syriac chronicle's charge only. Evidence: ZACH 2219-2221. Brief: "says he won Leo over with a bribe."
7. Church History dated 438-439 or a little later; Religious History undated and held only in Greek. Evidence: NP3 17855-17864.

## New: `sources`

- `ownWords`: Religious History (Greek, Migne PG 82), file `theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt`. Needed for Quote 3.
- `about`: Evagrius, Ecclesiastical History, tr. Walford (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt`); the Syriac chronicle under the name of Zachariah of Mitylene, tr. Hamilton and Brooks (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt`); the Latin letter to Nestorius in the Synodicon, Mansi V (`mansi_sacrorum-conciliorum-collectio-tomus-5-431-441-lat_welter-facsimile1901.txt`, lines 88759-88763).

## New: `briefReferences` (14 entries, no quotation marks)

Each traces to the brief's sentence and the lines in `Source_Sheet.md`; lines re-read in the files (NP3 38007-38010, 31496-31516, 36088-36090, 4724-4734, 37939-37947, 5219-5224, 3305-3338, 33201-33205, 43772-43776; RH 113735-113738; P449 15581-15603, 15641-15645; EVW 1109-1110, 5242-5249; ZACH 932-937, 2219-2221; NP14 23656-23661).

## New: `quotationOriginals` (7, one per quoted span in the brief)

1. "I will never agree ..." printed from Jackson's English, NP3 38007-38010. The Latin (M5 88759-88763) is a damaged scan, so it is not printed; the Latin reads injuste et inique and anime imbecillitatem, which the rendering follows ("wickedly", "weak soul") where Jackson has "illegally" and "my infirmity". Said in the entry's `uncertain`. No `secondReading`.
2. "The form of God ..." NP3 4724-4726. No `secondReading`. Greek not held.
3. "unwillingly" NP3 31499. "checked at card".
4. "First he ordered it cut ..." Greek, RH 113735-113738, printed exactly as the scan has it (chi for kappa, delta for beta, a stray mark before the genitive of "the earthly"; "ἐξ" where the numeral six is meant). Read by hand: six, twelve, twenty-two, thirty-six; fly up to heaven; be freed from this earthly way of life. Only one print, and no English print of this chapter exists, so the damaged Greek is the only printed wording that can stand in the lines; the faults are named in the entry's `uncertain`. No `secondReading`.
5. "Anathema to Nestorius" NP3 3335. "checked at card".
6. "a most excellent record" EVW 1110. "checked at card". Evagrius's Greek (EVG) is not printed: damaged accent lines.
7. "not a tomb" NP3 33203. "checked at card".

## Not found / not changed

- Existing `keyWorks[0].about`, "to the death of Theodore of Mopsuestia": Theodoret's own words are "the death of the admirable Theodorus and Theodotus" (NP3 18272-18274), with Jackson's note tying Theodotus to 429 and Theodore of Mopsuestia. Not contradicted outright, so left; flagged.
- Every existing quotation on the card (legacy) was re-read against NP3 3234-3235, 43772-43776, P449 15594-15595 and NP14 23656-23661, and holds.

## Second pass (2026-11-23)

### Checker changes
1. `quotationOriginals[3].uncertain`, the scan-fault wording: applied word for word.
2. `briefReferences[1]`, "the porticoes, " removed: applied word for word.
3. `briefReferences[3]`, "his birth at Antioch from the Religious History; " removed: applied word for word.

### Scan readings to add
None listed in the card check.

### Items added from the outline (all in `theodoret-of-cyrrhus.card.json`)
Evidence file short names: NP3 = `npnf203_theodoret-jerome-gennadius-rufinus.xml`; EVW = Walford's Evagrius; P449 = Perry's Syriac acts; ZACH = Hamilton and Brooks's chronicle; RH = Migne's Greek; NP2 = `npnf202_socrates-sozomen-ecclesiastical-histories.xml`; ANF9 = `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`.

- `legacy.traces` (Outline 164 and 16, Review 13): the first-session cries at Chalcedon: "Cast out the teacher of Nestorius", "Do not call him a bishop! ... Cast out the Jew!", the blank-paper cry, and the officials' "The vulgar cries are not worthy of bishops". Evidence: NP3 3231-3242, 3270-3272, 3290-3291.
- `legacy.traces` (Outline 173.2): Theodosius's death in July 450, the conceded council, Marcian's summons, the decree rescinded; credited to Jackson. NP3 3186-3205 (note 79 at 3195-3199).
- `legacy.traces` (Outline 13/Cut 13): Evagrius on the council of 449 revoking Eutyches's deposition and deposing Theodoret. EVW 1773-1787.
- `legacy.traces` (Outline 5): Zenos on the Tripartite History in twelve books. NP2 1695-1699. Cassiodorus's own Latin (CASS 83303-83307) not used: too damaged to quote.
- `legacy.remembered` (Outline 163): Juvenal on salt. P449 15695-15709.
- `legacy.remembered` (Outline 169): Dioscorus on the pavement, credited to the chronicle; council left unnamed as the sentence leaves it. ZACH 2429-2436.
- `uncertain` (Outline 8): parents' promise, own letter to Nomus. NP3 31496-31498.
- `uncertain` (Review 12, Outline 14): "condemned without a trial" and the second request to Leo. NP3 33171-33172, 33189-33193.
- `uncertain` (Outline 3): the request to go West or live in his monastery; Jackson says the second was granted. NP3 33476-33485, 3064-3069.
- `uncertain` (Outline 9): the Prologue's reason for the History. NP3 5208-5213.
- `uncertain` (Outline 7): "long ago stamped out", Apollinarius, Letter 150. NP3 36107-36109.
- `uncertain` (Outline 6): Ephesus 431, the deputies stopped at Chalcedon, credited to Jackson. NP3 2826-2838.
- `uncertain` (Outline 167): Compendium of Heretical Fables (Jackson, Photius): NP3 3630-3634, 3666-3667. Not a `keyWorks` entry: the validator allows three.
- `uncertain` (Outline 167): the Methodius fragment in Eranistes Dialogue I. NP3 20518-20520.
- `uncertain` (Outline 167): the Diatessaron passage and the two hundred copies, credited to Hogg. ANF9 1788-1794, 1922-1923.
- `uncertain` (Outline 11): leather clothes and the pillar. RH 113729-113734.
- `uncertain` (Outline 12): the Ishmaelites. RH 113926-113940.
- `sources.about`: NP2 (Zenos) and ANF9 (Hogg), the two new files cited above.

### Skipped
- Birth-year and death-year debate (157), ten books (166), Jackson's 553 verdict (Cut 4), officials' word that Leo restored the see (Cut 16): the card already holds them.
- Cut 8's wonder of birth, Cut 10 and Cut 15 (marked Leave out), and the Latin survival of the letter (Review 1): not marked for the card, or already held.
- Cassiodorus's own Latin: damaged scan.

### Validator
`--skip-quotes` on a scratch census: no errors outside the quotation checks. The 23 quotation errors (brief spans not matching the census's old long description) are from the census holding the old text.

## Third pass: what it was about (2026-11-23)

Starting card: `theodoret-of-cyrrhus.card.json` as it stood, copied to `Card.pass2.json`. Evidence short names as in the second pass. Brief: `theodoret-of-cyrrhus.brief.txt` against `.brief.v3.txt`. Fresh_Read_About_Applied.md asks for no card correction.

### Edits (all in `Card.pass2.json`)

1. `briefReferences[1]` (Nomus letter). Old: "...unwillingly; two bridges and the conduit; the eight villages..." New: "...unwillingly; the eight villages...". Evidence: the brief no longer tells the bridges and water channel (cut 1).
2. `briefReferences[1]`. Old: "no indictment published and no prosecutor." New: "no indictment published and no prosecutor, and no cause for the decree but his convening a synod of bishops." Evidence: brief, "with no charge and no accuser, he wrote, only for calling bishops together"; NP3 31453-31458.
3. `briefReferences`, new entry after the Letter 150 entry: Cyril's first anathema (falls on anyone who refuses to confess the Virgin Mother of God) and Theodoret's counter-statements to the second and eleventh anathemas (a mixture of flesh and Godhead destroys what each nature is). Evidence: brief, "The first fell on anyone who would not call Mary Mother of God. Theodoret charged that they mixed God and man."; NP3 4616-4619, 4764-4771, 5145-5148.
4. `briefReferences`, new entry: Letter to Eusebius of Ancyra, his accusers called him a heretic and charged him with dividing one Lord Jesus Christ into two sons. Evidence: brief, "his accusers, who said he split Christ into two sons"; NP3 31544-31549 (Letter 82).
5. `briefReferences`, Jackson's Prolegomena entry. Old: "Ephesus in 431 on John's side; the peace of 433, his refusal to accept the deposition of Nestorius, and his finding a meaning for the anathemas on Nestorianism, not on Nestorius;" New: "Ephesus in 431, where Cyril's party opened the council without John of Antioch and his party and passed the condemnation of Nestorius, and Theodoret stood on John's side; the peace of 433 and his refusal to accept the deposition of Nestorius;". Evidence: brief's Ephesus clause; NP3 2826-2835. The later-acceptance clause is cut from the brief (cut 4).
6. `briefReferences`, Chalcedon acts entry. Old: "the offer to condemn Nestorius and Eutyches, the cry that he was a heretic, and the curse." New: "his answer that he anathematizes Nestorius and asks to set out his faith first, the cry that he was a heretic, and the curse on Nestorius and on whoever divides the only begotten Son into two Sons." Evidence: brief, "He said he condemned him, but asked to explain his faith first ... a curse on his friend and on all who split the one Son into two"; NP3 3316-3337.
7. `briefReferences`, new entry before the census entry: Chalcedon's definition (one Son in two natures, unconfusedly, immutably, indivisibly, inseparably) and the chronicle's Dioscorus not confessing two natures after the union. Evidence: brief, "Chalcedon's teaching of two natures, God and man"; NP14 20288-20296; ZACH 2316-2320. The file is already in `sources`.
8. `uncertain`, new (cut 1): his own claim of two large bridges and a conduit, Nomus letter. NP3 31507-31511.
9. `uncertain`, new (cut 2): the Prologue, Eusebius's history to Constantine, and where his begins. NP3 5219-5224.
10. `uncertain`, new (cut 4, item 12): Jackson's summary of the later acceptance of the anathemas on Nestorianism, not on Nestorius, credited as the translator's. NP3 2862-2870.
11. `uncertain`, new (cut 5, item 13): his Chalcedon answer naming Nestorius and Eutyches, with the shouts; Eutyches's two natures before the union, one after, credited to Evagrius. NP3 3316-3331; EVW 1728-1730.

### Quotations
All seven spans are unchanged in the brief; `quotationOriginals` unchanged (no changed rendering, no dropped span). Lines re-read: NP3 38007-38010, 4724-4726, 31499, 3335, 33203; RH 113735-113738; EVW 1110.

### Skipped
- Item 5 (Apollinarius) and the "long ago stamped out" line: already in `uncertain`; its content is marked leave out.
- Item 8's Nomus as procurer, cut 3 (", Simeon among them"), items 9-11, 14-16, 18-20: already told in the brief and held, or not marked for the card.
- Cuts 6-10 (wording only): no card change.
- No Pelagius clause files exist for this entry.

### Validator
`--skip-quotes` on a scratch census with this card and the brief in the entry: 0 errors, none for this entry.
