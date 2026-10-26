# C12 coverage map: daily life (food, homes, work, clothes, sickness, death)

Read-only pass, 25 October 2026; nothing in the repo was edited. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; file paths, line numbers and verification results are in `search/C12/C12-coverage.json`.

## The sub-questions

The 25 C12 questions plus R-03 group into eight:

| id | sub-question | canon / question ids |
|---|---|---|
| S1 | An ordinary day; food and drink; fun, baths, games; rest | C12-01, 02, 08, 11, 15, 18 |
| S2 | Houses, clothes, language at home and in prayer | C12-12, 13, 19 |
| S3 | Work, school, community size, travel, letters, telling time | C12-14, 17, 20, 22, 23, 24 |
| S4 | Sickness, plague, lifespan, child death | C12-03, 10, 16 |
| S5 | Burial, grief, mourning customs | C12-09, 21 |
| S6 | What belonging cost; distance from loved ones | C12-06, 07 |
| S7 | "Were you happy"; "what's the point of life" | C12-25, R-03 |
| S8 | What archaeology would find; how historians know | C12-04, 05 |

The 13 canon F5 questions feed S1, S3, S4, S6 and S8; S2, S5 and S7 have no canon cell (predicted or research-added only).

## Layer table

R = RENDERED (a record speaks to it), R\* = partial or guard only (honest_limit, not_for, one slice of the question), L = LOADED (vendored and mapped, read in context, no record), "-" = nothing found. IDENTIFIED and OTHER sources are listed per cell in the JSON.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R\* | R\* | R\* | R | R\* | R | R\* | R |
| cappadocian | R | L | R | R | R | R | R\* | R |
| desert | R | R\* | R | L | R\* | R | R | R\* |
| don | R\* | L | R | R\* | R\* | R | - | R |
| gallic | R | R | R | R\* | R | R | R | R |
| hal | R | R | R | R | R | R | - | R |
| ijc | R\* | L | L | R\* | R\* | R | R\* | R\* |
| lpc | R\* | R\* | R | R | R\* | R | R | R\* |
| pahc | R | L | R | R\* | R\* | R | - | R |
| rzg | R\* | R\* | R | L | L | R | L | R |
| syr | R | L | R | R | R\* | R | R\* | R |
| witt | R | R\* | R\* | R\* | R | R\* | R\* | R |

Totals over 96 cells: 50 R, 33 R\*, 10 L, 3 "-" (S7 for don, hal and pahc). Worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) were not mapped. lpc is all `draft`.

Verification: 47 quote records are cited as RENDERED; all 47 MATCH their vendored file. Forty-two are exact, two match after spacing or ligatures, and three needed editorial artifacts removed: OCR footnote marks in the two Salvian quotes (`gallic.quote.salvian-on-the-unburied-dead`, `...-demand-for-circuses`) and a marginal letter in Basil on work and prayer. None is a wording change.

## Three findings across the cluster

**1. The ambient record type holds no daily life.** Nine ambient records exist: `don` 3, `lpc` 3, `rzg` 3 (plus one fixture, `fix.ambient.daily-bread`). All nine state a scale or an object, never a day: 310 bishops at Bagai, 87 at Carthage, 600 in the Zurich Town Hall, four Deo laudes stones, an organ gone silent. All carry `canon_cells: []`, `tier: 3`, `retrieve_when: []` and `formation_claim_barred: true`. Nothing routes to them: `engine/m1/gates.py` (line 1547) says ambient records are parked, System Hub Decision Log line 6044 parks them untouched, and `engine/m4/evidence.py` gives tier 3 zero priority. Nine worlds have none. `rzg.ambient.emptied-worship-space` is Inferential-Thin.

**2. F5 demonstrations are six, and mostly one.** Of 13 F5 canon questions, three have a demonstration: f5-i-03 (women in their own words; alx, gallic, hal, witt), f5-i-01 (ijc, as an honest limit) and f5-e-01 (pahc, material remains). Ten have none anywhere: food, children, the enslaved, sickness and dying, work, cost of belonging, distance, marriage, money, how historians know. Cappadocian, desert, don, lpc, rzg and syr have no F5 demonstration.

**3. Doc_05 holds more daily life than the records do, in two worlds.** `gallic` Doc_05 sec 1.2 (dress, food, sleep, cell, labour, climate) and `witt` Doc_05 sec 1.2 (rising, table, bed, fasting, burial) are the richest daily-life text in the fleet; each became only a handful of records. The other ten Doc_05s are thin on purpose or name the gap.

## World by world

**Alexandria (alx).** Can say: the plague of 260 and the nursing church (verified), the costly furniture of the rich, who may eat and who fasts, Origen's mother hiding his clothes. Thin: no ordinary day, burial, or household; Clement's *Paedagogus* II (drinking, laughter, clothes, L22382, L23729) and Anatolius's Paschal Canon (anf06 L14759) are mapped and unquoted. Doc_05 sec 6.2-6.3: the day, week and year rhythm and the martyrs' era never became records. F5 demos: 1. Ambient: 0. Add: a Clement quote on food and clothes, with the not_for already used.

**Cappadocians (cappadocian).** Among the strongest daily-life worlds. Ordinary day, famine, poorhouse, deathbed, grief and costly friendship are all covered; the day and poorhouse stories are Inferential-Thin by tag. Gaps: houses, clothes and speech (S2), and child death, though Nyssa's *On Infants' Early Deaths* (npnf205 L443) is vendored. Doc_05 sec 1: cold plateau, indigenous speech beside church Greek, charms, slave-exporting region; none recorded. F5 demos: 0. Ambient: 0. Unvendored: poorhouse, Annisa shrine, Nazianzen's will.

**Desert (desert).** Day, hand-labour, village trade, exile and the "point" (Evagrius, Contested) are covered. No record on sickness: the Pachomian Rules (L194) hold the prior serving the sick. Burial is only Antony's. S8 has no honest_limit: `desert.term.kellion` names the dig while the 1,500-structure Kellia excavation is unvendored. Doc_05 sec 4-5: Nitria-Kellia is one day's walk (19 km) and the weekly synaxis ends in a shared meal; unrecorded. F5 demos: 0. Ambient: 0.

**Donatists (don).** Best-guarded: `don.limit.no-ordinary-day-survives` and `...the-room-we-cannot-show-you` refuse to invent a day or a room. Size comes as bishops (310, 279), not people. Unrecorded and vendored: Punic as the common language at Fussala (npnf104 L10597) and epitaphs with ages at death (CIL VIII Suppl., L420). S7 nothing found. F5 demos: 0. Ambient: 3 (all physical facts, none retrievable).

**Gallic monastics (gallic).** Funeral, dress, lentils, weekly service and the goal of life are all quoted and verified. Missing from records: sleep, fasting days, labour as copying, climate (Doc_05 sec 1.2); and sickness beyond fevers (the "plague" at Sulpicius L4932 is hail). Caution: Cassian's dress and food rules describe Egypt, not Gaul. F5 demos: 1. Ambient: 0.

**Jerome's circle (hal).** Hospital, hostel, epitaph, trilingual psalms at a burial, a child's boxwood letters: verified. The day at Bethlehem is Inferential-Thin. Unrecorded and vendored: Letter 39 on Blesilla (npnf206 L7763), Letter 60 (consolation on Nepotian's death), Letter 22 on wine. S7 nothing found. F5 demos: 1. Ambient: 0.

**Imperial-juridical (ijc).** The honest limit and a worked demo refuse an ordinary day, correctly. Everything else is L or R\*: Chrysostom on the theatre, the Codex Theodosianus on tomb violation (CTh 9.17, L3332), Ambrose's grief for Satyrus (npnf210 L651). `ijc.quote.happy-christian-emperors` is about rulers; do not use it for "were you happy". F5 demos: 1. Ambient: 0.

**Latin pastoral (lpc, draft).** Plague, last illness, ransom, bishops' assemblies and "formed us for Thyself" are covered. Unrecorded: Augustine, *On Care to Be Had for the Dead* (npnf103 L43495), Monica's death (npnf101 L13842), Cyprian on virgins and mixed baths (Latin), Perpetua's nursing infant (Latin), and the Carthage excavation reports in French (Audollent). F5 demos: 0. Ambient: 3 (council size, two cities, administrative objects).

**Post-apostolic (pahc).** Sunday gathering, letters, imprisonment and the material-remains limit with its demo. Unrecorded and vendored: Diognetus ("common table, but not a common bed", anf01 L2735), Aristides on burying a poor man (L2853), Tertullian on funeral incense (anf03 L4148). S7 nothing found. F5 demos: 1. Ambient: 0.

**Zurich and Geneva (rzg).** Thin: honest limit on the day, worship-space limit, a crowd of 600, Calvin's journey, Zwingli's death. Sickness, burial and the "point" are L only: Calvin's letters on plague (L217), the Ordonnances' visitation of the sick, and the Geneva Catechism's first question (L229). F5 demos: 0. Ambient: 3, one Inferential-Thin.

**Syriac (syr).** Best sickness ground: Dem. 6, Palladius, Ephrem and the famine, with the Physician. Best S8: a baptistery has been found, and a verified quote shows how the record survived. Missing: houses, clothes, speech (Bardaisan's *Laws of Countries*, anf08 L67888, is mapped). Nisibis cathedral report unvendored. F5 demos: 0. Ambient: 0.

**Wittenberg (witt).** Household, daily prayer, fasting, burial as sleep and hymns at the grave are Documented terms. Unrecorded: the morning and evening blessings (SC 543-607), the calamity list with pestilence, the churchyard as resting place. Saxon visitation protocols are unvendored, so the ordinary parish stays prescription. F5 demos: 1. Ambient: 0.

## Other sources (outside the repo; from working knowledge, not fetched)

Egyptian papyri for daily life (Oxyrhynchus, Karanis; alx, desert); Kellia and Nitria excavation reports (desert); Luther, *Whether one may flee from a deadly plague* (1527; witt); Sehling's Kirchenordnungen (witt); Calvin's 1541 Ordinances in English (rzg); Nazianzen's funeral orations 7 and 8 (cappadocian); Brock and Harvey on Syrian holy women (syr).

## Not checked

- `canon/sealed_probes/` was not read.
- S8 had no tool run; it is judged from records, Doc_05 and the source registry.
- The tool scans whole mapped files, so generic terms flood the counts; LOADED loci were chosen by hand and read in context, not traced work by work in shared volumes.
- Non-English vendored texts were counted, not read. The four Doc_05s for ijc, pahc, rzg and syr were skimmed by heading and keyword.
- Readability of spoken fields was not graded. Which lpc draft records are in the compiled package was not checked.
