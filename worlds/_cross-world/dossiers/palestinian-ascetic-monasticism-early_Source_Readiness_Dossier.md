# Source Readiness Dossier — Early Palestinian Ascetic Monasticism

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** I.34
**Corpus-map slug:** `palestinian-ascetic-monasticism-early`
**Time window:** c. 330–450 CE
**Region(s):** Gaza, the Judean desert, Sinai road
**Dossier author / date:** source-acquisition research thread, 2026-09-21
**Corpus-map / `cic/texts/` state as of:** `main` @ commit `009caaf`, plus
one new cross-link assignment made during this dossier pass (§2 below).

Unlike `greek-apologists-second-century` and `latin-apologists`, this
candidate has no Step 0 Movement-Scope Confirmation on file — it has never
been individually researched, only registered on the census in 2026 after
the corpus-assignment run found material with nowhere accurate to go. This
dossier is therefore closer to first-pass research than the other two, and
correspondingly more likely to have moved the needle.

## 1. Already assigned

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Life of S. Hilarion | jerome | tradition | assigned | ~11,619 words | `npnf206_jerome-principal-works.xml` |
| The Life of Malchus, the Captive Monk | jerome | tradition | assigned | ~3,513 words | `npnf206_jerome-principal-works.xml` |
| Lausiac History — Ch. XLVIII–LIV (Elpidius, Sisinnius, Gaddanas, Elias, Sabas, Abramius, the Elder Melania) — **added this pass, see §2** | palladius | tradition | provisional | ~7 chapters of a ~1,000-page work (not separately word-counted this pass) | `palladius_lausiac-history_clarke1918.txt` |

## 2. Cross-link opportunities

**Checked using `CORPUS-USE.md`'s tier method against the full `cic/texts/`
directory listing.**

- **A real, verified addition made this pass, not merely named — following
  the Ambrosian-Milan/Theodoret precedent for a dossier-found cross-link.**
  Palladius' *Lausiac History* was assigned only to `desert-monasticism`
  (Egypt). Checked directly against the vendored text (not assumed from a
  chapter-title search): seven consecutive chapters — XLVIII (Elpidius, "in
  the caves of the Amorites round about Jericho," Palladius himself an
  eyewitness resident "I too lived with him" for twenty-five years), XLIX
  (Sisinnius, Elpidius' own disciple), L (Gaddanas, "an old Palestinian...
  in the region round the Jordan... region round the Dead Sea"), LI (Elias,
  "in the same parts"), LII (Sabas, "a native of Jericho... the ascetics of
  the Jordan"), LIII (Abramius, same unbroken block), and LIV (the Elder
  Melania, who "came to Jerusalem" and founded "a monastery" there) — sit
  squarely inside this candidate's own region and window. Added to
  `cic/corpus-map/_staging/palladius_lausiac-history.yaml` and re-merged
  (scoped `corpus_map_merge.py --write-only`); `role: tradition` on the
  same footing as this candidate's existing Jerome entries,
  `confidence: provisional` because whether an Egypt-centered author's
  testimony about neighboring Judean-desert monks counts as this
  movement's own voice, at the same weight as Jerome's participant-observer
  Hilarion and Malchus, is a Doc_02 gravity-informed judgement this dossier
  pass is not positioned to make alone.
- **Sozomen's *Ecclesiastical History* — named, not verified, real enough to
  flag rather than drop.** Already assigned to `desert-monasticism` (context),
  whose own note reads "I.12-14, III.14 and VI.28-34 are extended accounts of
  Egyptian (and Palestinian/Syrian) monasticism naming Antony, Pachomius and
  the Nitrian fathers." The volume (`npnf202_socrates-sozomen-ecclesiastical-
  histories.xml`) contains 93 occurrences of "Palestine" fleetwide, but this
  pass did not isolate which, if any, fall inside those specific chapter
  spans and describe this candidate's own region rather than Egypt — the
  named authors in the existing note are all Egyptian. A future pass should
  read I.12–14, III.14, and VI.28–34 directly before adding or declining a
  cross-link here; not done this pass for time.
- **Chrysostom's ascetic material — checked and confirmed not a gap.** The
  census's own `why` field names "Chrysostom's ascetic treatises" as one of
  two piles that originally landed on `desert-monasticism` for lack of a
  home. Checked directly: Chrysostom's own ascetic works in
  `npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml` are already
  correctly assigned to `antiochene-exegetical-christianity-chrysostom-ce`
  (his own entry), not to `desert-monasticism` or this candidate — the
  census's own summary describes a state this corpus map has since moved
  past, not a live gap. No action needed.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Pilgrimage of Etheria | Egeria (Etheria) | M. L. McClure and C. L. Feltoe | 1919 | https://archive.org/details/pilgrimageofethe00mccliala | pd-us-by-date | Direct `WebFetch` against the archive.org details page, 2026-09-21 — page states `NOT_IN_COPYRIGHT`; corroborated by a separate archive.org item, a 2018 LibriVox recording of the same translation, independently carrying a Public Domain Mark 1.0 license. Already named once before — `records/hal/search_record/hal.search.egeria-pilgrimage.md` (2026-08-21) — but scoped there to Bethlehem context only for a different world; this pass re-verified it directly rather than trusting that prior citation, and the fit here is closer: Egeria's own 380s journey runs "the Sinai road" — this candidate's own `region` field, verbatim — through the Judean desert, describing monks and hermits she met along it. Added to `worlds/_cross-world/download-queue-seed.yaml`; not yet vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Cyril of Scythopolis, *Lives of the Monks of Palestine* (Euthymius, Sabas, Chariton, and others) | The single most direct primary-source author for exactly this movement — a Judean-desert monk writing lives of its own founders, c. 555 | Checked against `archive.org` (title search, 2026-09-21): no public-domain English translation exists. What surfaces is unrelated (a 1993 archaeological study of Euthymius' monastery, still in copyright; a Greek-novelist Chariton, a different ancient author entirely). The standard modern English translation (R.M. Price, Cistercian Publications, 1991) is in copyright; no 19th- or early-20th-century translation was ever made, unlike Palladius or Jerome. A real and durable gap, not a research gap. |

## 5. Open cross-world questions

- **The census's own `why` field states the live classification question
  directly, and this dossier does not attempt to answer it:** "whether the
  century before [c. 450] is a world of its own or the prehistory of the
  one already on the map" — `chalcedonian-monasticism-judean-desert-and-gaza`,
  which begins where this candidate's own window ends. Both this candidate's
  Jerome entries and the newly-added Palladius chapters are equally
  consistent with either reading; nothing found this pass bears on it either
  way.
- **The `role: tradition` vs. `role: context` judgment on the new Palladius
  entry (§2)** is named there as `provisional` and carried here as the same
  open item — an Egypt-centered author's own testimony about neighboring
  monks, on the model of Jerome's participant-observer status or on a
  lighter, more external footing. A Doc_02 gravity pass, not this dossier,
  is positioned to weigh it.
- **The duplicate census entry noted in `NEEDS-RULING.md`**
  (`cyrilline-miaphysite-egyptian-tradition` vs.
  `cyrilline-miaphysite-egyptian-christianity`) does not touch this
  candidate's own roster and is not repeated here beyond this pointer.
