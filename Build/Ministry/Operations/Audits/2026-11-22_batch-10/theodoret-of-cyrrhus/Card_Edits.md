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
