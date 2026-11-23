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

## Third pass: what it was about (2026-11-23)

Starting card: `Card.pass2.json` (unchanged copy). Everything not listed here is word for word. `quotationOriginals` untouched: the brief still quotes the same four spans (Q1, "substance", "alone unbegotten", "subject and obedient in all things"), with unchanged rendering. NP2 = `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml`; AUX, PHI as before.

### briefReferences (edited entries)

1. [0] Auxentius sections 55-63. "the persecution by a godless judge of the Goths and the martyrs" → "the persecution of the Goths and the martyrs" (the brief no longer tells the judge: "persecution drove him out, after many men and women had died as martyrs"). "the forty years, the order to Constantinople, his sudden illness" → "the emperor's order to Constantinople for a debate, to stop his opponents teaching in his churches, his sudden illness" (brief: "Later the emperor ordered Ulfila to Constantinople for a debate, to stop his opponents teaching in his churches"; AUX 15283-15286, ne Cristi eclesias ... docerent et infestarent).
2. [4] Philostorgius. "forebears who were Christian captives from Cappadocia carried off by Gothic raiders, who won many Goths to the faith; made bishop on a Gothic embassy to the emperor's court, by Eusebius and the other bishops with him;" → "made bishop at the emperor's court, by Eusebius and other bishops;" (brief: "says it was at the emperor's court, by Eusebius and other bishops"; PHI 120). Forebears and embassy no longer told.
3. [7] Socrates. After "banning the word substance for God" added "because, it says, the holy Scriptures nowhere mention the substance of the Father and the Son" (brief: "saying Scripture never uses it"; NP2 9564-9573). After "put down to the emperor Valens" added ", whose troops helped the chief Fritigernes in a Gothic civil war, and Fritigernes embraced the emperor's religion in gratitude" (brief: "whose help in a Gothic civil war won a chief over to his faith"; NP2 14428-14449). "Athanaric, who punished" → "Athanaric, who saw a violation of the privileges of his ancestors' religion and punished" (brief: "took this as an attack on his ancestors' religion"; NP2 14460-14465).
4. [8] Sozomen. "among about fifty bishops at Constantinople" → "among the bishops at Constantinople" (brief: "joined the bishops"; NP2 34561-34567); the fifty moved to `uncertain`. "on the Goths' embassy, under pressure" → "on the Goths' embassy, which asked for land for them, after the leaders of the Arian party promised, it is said, to forward the request if he conformed, under pressure" (brief: "an embassy seeking land for the Goths. The other side's leaders, he heard, promised help if he joined them"; NP2 40141-40146, 40163-40171, "it is said").

### briefReferences (new entry, appended)

5. Arius, a presbyter, as Socrates reports him and as Theodoret gives his own letter to Eusebius of Nicomedia; Socrates 4.33 and Sozomen 6.37 name the faith after him. Evidence: brief ("after Arius, a priest who taught that the Son had a beginning"); NP2 2064-2099 (Socrates 1.5); `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` 6002, 6044-6046 (Theodoret 1.4, Arius's letter); NP2 14446-14449, 40180-40181.

### uncertain (three appended)

6. Sozomen's about fifty bishops at Constantinople, the formulary of Ariminum, the banned terms, reign not year, 360 the usual date (outline sends "about fifty" to the card; NP2 34559-34568; the "usual date" wording was in the removed reference clause).
7. Philostorgius: the captives carried off from Cappadocia, Ulfila's forebears among them, brought many Goths to the faith (outline, cut 2, to the card; PHI 120, "Of the number of these captives were the ancestors of Urphilas").
8. Auxentius: sent to Constantinople once forty years were complete, seven among the Goths and thirty-three on Roman soil (outline, cut 6, count to the card; AUX 15270, 15279-15283).

### sources.about (titles widened so each newly cited chapter is listed)

- Socrates/Sozomen entry: "Church History, Book 2, chapter 41;" → "Church History, Book 1, chapter 5; Book 2, chapter 41;" (Arius, NP2 2064-2099).
- Theodoret entry: "Church History, Book 4, chapter 33" → "Church History, Book 1, chapter 4; Book 4, chapter 33" (Arius's letter, line 6002).

### Skipped

- Items 1, 2, 3, 4, 7, 8, 9, 10, 12, 15, 18: already explained, no new card content; the brief's references already carry them.
- Item 6 (the Gothic embassy at the consecration): left out of the brief; the card's `uncertain` already tells Philostorgius's embassy.
- Item 14's motive (Sozomen's "or, possibly") and item 17's opponents' name (damaged, editor-restored, STR 866-868): the outline marks neither for the card; the reference carries the first as Sozomen's, and the second is left unstated for want of a verified restoration reading.
- Cut 4 (godless judge) and cut 7 (the other bishops with him): reference trimmed only; the outline sends neither to the card.
- Applied Fresh_Read changes (Socrates "only in 360", "Two church historians", "he heard"): wording only; the card's claims were not affected. Nothing else clearly wrong; no claim not found.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch copy of the census with this card and the brief in `ulfila`: 0 errors (4 warnings, none for this entry).

## Fourth pass: no modern opinion (2026-11-23)

Starting card: `Card.pass3.json`, unchanged. Brief changes: the consecrator's identity, the Gothic Bible's translator, the council's year and the year of death are no longer told (`Modern_Pass.md`, `Outline.md` "Modern pass"). Every line re-read in `cic/texts/`.

### uncertain (modern views marked as modern judgments, credited by name)

1. Duchesne, entry on the consecration. "Louis Duchesne, in his history of the early church (1907), names him Eusebius of Nicomedia." → "... names him Eusebius of Nicomedia, a modern judgment." Evidence: DUC 20991-20995 ("Eusèbe de Nicomédie le vit ... le consacra évoque pour sa nation"); PHI 120 names only "Eusebius and the other prelates".
2. Streitberg, entry on the fragments. "Streitberg sees no doubt that they are the remains of Ulfila's translation." → "... translation, a modern judgment." Evidence: STR 603-607.
3. Council year, first entry. "says he held the Nicene creed until he signed the creed of the council at Constantinople in 360" → "... at Constantinople under Constantius". Evidence: Socrates gives no year (NP2 9480-9482, 9606-9612; "τότε πρῶτον", SOC-G1 27461-27466); 360 stays in the Sozomen entry as the modern date.
4. Council year, Sozomen entry. "360 is the usual date." → "360 is the usual modern date, a modern judgment that no held old source gives." Evidence: Sozomen gives the reign only (NP2 40160-40162); the note "360 a.d." at NP2 9738-9739 dates the consecration of St Sophia, not the council. No held modern writer is named for the council's year.

### datesNote

5. "(Kauffmann's dates, worked from Auxentius's numbers)" → "(Kauffmann's dates, a modern judgment worked from Auxentius's numbers)". Evidence: AUX 3684, 3735 ("im Juni 383 zu Constantinopel verstorben"); AUX 15283-15292 gives no year.

### briefReferences (wording the brief no longer has)

6. Removed: the Kauffmann entry ("the years ... with the death at Constantinople about 383"); the brief tells no year.
7. Removed: the Duchesne entry (Eusebius of Nicomedia as the consecrator); the brief no longer tells it.
8. Removed: the Streitberg entry (no doubt the fragments are Ulfila's); the brief no longer tells it.
9. Sozomen entry: "; 360 is the usual date, and Sozomen gives the reign, not the year" → "; Sozomen gives the reign, not the year". The brief says "Under the emperor Constantius" (NP2 40160-40162).

No new old source and no new `sources` file: the brief's new words rest on Sozomen and Socrates, already referenced and listed. The Duchesne and Streitberg files stay in `sources.about` and `ownWords` for the `uncertain` entries.

### quotationOriginals

Unchanged: the brief still quotes four spans (the Exodus passage, "substance", "alone unbegotten", "subject and obedient in all things"), each with its entry word for word. None dropped, none added.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch copy of the census with this card and this brief in `ulfila`: 0 errors, 4 warnings (none for this entry).

### Not found

None.
