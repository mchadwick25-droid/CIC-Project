# Card edits: Ulfila

Card: `ulfila.card.json`, from `Card.existing.json`. Every existing field is word for word; edits are appends only. No `briefLength` (the census rules bar it). AUX = `cic/texts/auxentius-durostorum_epistula-de-fide-vita-obitu-wulfilae_kauffmann1899.txt`; STR = `cic/texts/wulfila_gothic-bible-v1-got_streitberg1908.txt`; NP2 = `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml`.

Validator (`tools/validate-census.mjs --skip-quotes`, on a scratch copy of the census with this card and the brief in `ulfila`): the only two errors are the missing `secondReading` on the Q1 and "subject and obedient in all things" entries, left out on purpose (six words or more; release sets it). The full run was killed for memory here, so the Library quote check was not run; the new card prose carries no quotation marks.

## New: quotationOriginals (one per quoted span in the brief; four spans)

1. Exodus quote (Q1). Old: none. New: modern as in the brief; printed is the Latin, AUX 15273-15277 (checked line by line: "sicuti deus per Moysem ... sibi seruire"), as the file has it, including its scan slip "poptäum". No English print of Auxentius is held, and Streitberg's second print (STR 836-842, "populum" at 839) confirms the reading, so the Latin is printed and the fault is named in `uncertain`. Also noted there: the last clause takes "fecit" from the one before (AUX 15276-15277); STR 657 says Streitberg follows Kauffmann's text, so the prints are not independent (Source_Sheet E7). No `secondReading` (long).
2. "substance". New: printed is Sozomen IV.24's English, NP2 34565-34568 ("the terms “substance ” and “hypostasis” should never again be used in reference to God."). `secondReading` "checked at card" (one word). Note says the same clause bans hypostasis and that Socrates words it "substance" or "subsistence" (NP2 9606-9608). Brief: "banned the word "substance" for God".
3. "alone unbegotten". New: printed "solum ingenitum", AUX 15310 (read again; STR 886 agrees). "checked at card" (three words).
4. "subject and obedient in all things". New: printed "et filium subditum et oboedientem suo in omnibus deo patri", AUX 15324 (STR 902 agrees, with the scan slip "oboedieniem"). No `secondReading` (six words). Note: the brief closes the quote at "all things" and gives "to his God the Father" outside it, as the outline's Do not say requires.

## New: briefReferences

Whole list new (the existing card had none). Ten entries, each drawn from what the brief tells: Auxentius sections 55-63 (the section numbers stand in the margins of AUX 15108-15324; 58-59 are OCR-damaged "5^" and "*^^" and follow from the run 57, 60), sections 42-48 (AUX 15114-15176), section 63 (AUX 15301-15324); Kauffmann's years (AUX 3735, 3752-3755); Philostorgius 2.5 (PHI 120); Duchesne (DUC 20991-20995); Streitberg (STR 603-607); Socrates 2.41 (NP2 9606-9612) and 4.33 (NP2 14444-14465); Sozomen 4.24 (NP2 34561-34567) and 6.37 (NP2 40141-40181), with "360 is the usual date, Sozomen gives the reign, not the year" (outline, beat 4; NP2 40158-40163 "during the reign of Constantius"); Theodoret 4.33 (`cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` 15300-15323). No quotation marks in any entry. No entry to the census or to other entries (connections left out).

## New: what the outline sends to the card (appended to the end of each list)

- `legacy.traces` +4: Jordanes on the Lesser Goths in Moesia (JOR 3288-3296; outline Cut first 2, What came 4); Isidore of Seville on Gulfilas (STR 1292-1296; Cut first 4); Theodoret's Goths holding the Father greater than the Son (THD 15316-15323; Cut first 5); Walafrid Strabo (STR 1324-1338; "For the card, not the story").
- `uncertain` +7: Theodoret's eloquence and bribes, the bribe his charge (THD 15300-15323; the brief tells it); Sadagolthina and the Valerian and Gallienus raid (PHI 120; "For the card"); Sozomen's statue, tents and tent church, "it is said" and "I have heard" (NP2 40188-40199; the brief's Cut 7 and the Do not say on burnings); Auxentius's three languages with no Bible named, Socrates setting the letters under Valens (AUX 15211-15213, 15220-15222; NP2 14448-14459; Cut first 6 and 9); the Spirit in the creed, "neither God nor Lord" (AUX 15321-15323; Leave out); Christianople (AUX 15292-15301; Cut first 10); Socrates's Selenas, with Zenos's note (NP2 16697-16705; "For the card").
- `sources.about` +2, so each new line cites a held file the card lists: Theodoret IV.33 (`cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`) and Jordanes ch. 51 (`cic/texts/jordanes_origin-and-deeds-of-the-goths_mierow1908.txt`). Isidore and Walafrid stand in STR, already listed.

## Clearly wrong

None. Each existing claim was read against the files and the brief; none is contradicted. Checked: Auxentius "most holy man ... confessor of Christ ... teacher of piety" (AUX 15114, 15271); the two Photius quotes (PHI 120); Sozomen's "innumerable perils" (NP2 40178 area, "He had exposed himself to innumerable perils in defense of the faith"); Selinus (NP2 41606-41612); Socrates on Theophilus (NP2 9606-9612); Kauffmann on Eusebius of Nicomedia "damals bereits bischof von Constantinopel" at Antioch 341 (AUX 2750-2752); Kauffmann on the numbers and 348-349 (AUX 3740-3762); Codex Argenteus and the Bobbio palimpsests at Milan (STR 1348-1356, 1402-1414); Sozomen's embassy and the Huns (NP2 40125-40150).

## Claims not found

None.

## Scan readings to add

None. The card check lists no scan readings.

## Second pass (2026-11-23)

**The checker's change.**
- `keyWorks[0].about`: "written in silver and gold on purple parchment" becomes "written in the fifth or sixth century in silver and gold on purple parchment". Applied word for word. Evidence: Streitberg's file (STR) line 1352, "Geschrieben im 5./6. Jh. mit Silber- und Goldbuchstaben auf purpurgefärbtem Pergament"; Outline Cut first 11. This also covers the Cut first 11 item, so it is not added twice.

**Added from the outline.**
- Field `uncertain` (appended). Text: "Philostorgius says the emperor settled the Goths Ulfila brought over in different parts of Moesia, as he thought best, and held Ulfila in such honor that he often spoke of him as the Moses of his day." Outline Cut first 8 ("Beat 2", the settling in Moesia, with Philostorgius's credit). Evidence: `cic/texts/philostorgius_ecclesiastical-history_walford1855.txt` line 120, "This multitude of converts were located by the emperor in the different parts of Moesia, as he thought best, and he held Urphilas himself in such high honour, that he would often speak of him in conversation as the Moses of his day." The Moses saying was already on the card under `legacy.remembered`; the settling was not.

**Skipped, already held** (each re-read against the card): Cut first 1 (Sozomen's tribute, `legacy.remembered`); 2 (Jordanes, `legacy.traces` and `sources.about`); 3 (Selinus, `legacy.traces`); 4 (Isidore, `legacy.traces`); 5 (Theodoret, `legacy.traces`); 6 (three languages, `uncertain`); 7 (Philostorgius's "first bishop" against Theophilus, `uncertain`); 9 (Socrates on Valens, `uncertain`); 10 (Christianople, `uncertain`). Leave out and For the card: Sadagolthina, Kauffmann's country bishop, Waitz's doubt, Philostorgius's own views, the Holy Spirit in the creed, Walafrid Strabo and Selenas are all on the card (`uncertain` or `legacy.traces`). Cut first 12 is marked Leave out.

**Validator** (`--skip-quotes`, scratch copy of the census): two errors for this entry, the missing `secondReading` on `quotationOriginals[0]` and `[3]` (six words or more; release sets it).
