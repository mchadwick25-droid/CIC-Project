# Card check: Martin of Tours

Checker, 2026-11-18. Starting card: the census `card` object for `martin-of-tours` in `cic-website/data/world-census.json`.

**Verdict: FIX** (one change, `knownFor`).

## 1. Edits justified

- N1 (Life 6): NP11 942-953 holds "publicly scourged", "compelled to leave the city", "a monastery for himself at Milan", "violently expelled him". Justified.
- N2 (Life 13-15): NP11 1244-1248, 1296-1298 ("wherever he destroyed heathen temples, there he used immediately to build either churches or monasteries"), 1319-1323 (Leprosum, "driven back not without bodily injury"), 1365-1369 ("they themselves overthrew their own temples"). Justified.
- N3 (Life 10): NP11 1119-1125 ("the same homeliness in his garments"), 1139-1140 ("all things were possessed in common"), 1155-1158 ("what city or church ... would not desire to have its priests from among those in the monastery of Martin?"). Justified.
- N4 (Epistle III): NP11 2380-2390 (clerics "at variance", "wishing to restore peace", "he well knew that the end of his own days was at hand"). Justified.
- N5 (Gregory): GT 1470-1477 ("at Candes, a village of his diocese"); GT 11933-11936 ("became a model for saints' lives"). Justified.
- N6: capital letter only, matching the brief. `secondReading` "minor" copied. Justified.
- W1-W5: each removed or replaced part names what the brief no longer tells, or quoted words not in it (W2: NP11 855-856 is not in the brief). Justified.

## 2. Nothing else moved

Diffed against the census card. Only `briefReferences` and `quotationOriginals[1].modern` differ, as listed. Every other field is word for word; order kept.

## 3. References that remain

Life 2; Life 3 (cloak, dream); Life 3 (baptism); Life 4; Life 5 and 7; Life 6; Life 9; Life 10; Life 13-15; Life 25; Chronicle II.50; Dialogue III.11-13; Epistle III; Gregory (Perpetuus's church, Clovis's edict, Candes, Brehaut's note); World census. Each names only what the brief tells. Place names attached to told events (Leprosum, the Loire) are identification, not new matter.

## 4. Census rules

- Keys: the census card's keys only; no `briefLength`.
- The brief quotes two spans; two `quotationOriginals` entries.
- Printed wording verbatim: NP11 841-842 ("I am the soldier of / Christ: it is not lawful for me to fight."); NP11 11657-11660 (the printed words stand on 11658-11660, inside the range). Latin: Halm 6335-6337 and 5905-5907 hold the cited words (OCR as noted). Both files are in `sources`.
- No quotation marks in `briefReferences`. No audit, review or ruling named. American spelling ("quarreling", "honored").

## 5. Rulings

- "Not found": none claimed. None found.
- **`knownFor`, "not for an emperor to judge": clearly wrong.** Sulpicius's Latin reads "ut causam ecclesiae iudex saeculi iudicaret" (Halm 5905-5907): a judge of this world, not an emperor. Roberts's English agrees: "a secular ruler should be judge in an ecclesiastical cause" (NP11 11658-11660). The brief gives the plea as "for a judge of this world to try a case of the church". And the case was in fact tried by the prefect Evodius, not the emperor (NP11 11665-11667). The card puts a word in Martin's mouth that no held text gives him.

### FIX

Field `knownFor`.

- Old: `A Roman soldier who became a monk and then bishop of Tours, and who pleaded at Trier that Priscillian's case was not for an emperor to judge.`
- New: `A Roman soldier who became a monk and then bishop of Tours, and who pleaded at Trier that Priscillian's case was not for a judge of this world.`

(The words "an emperor to judge" become "a judge of this world".)
