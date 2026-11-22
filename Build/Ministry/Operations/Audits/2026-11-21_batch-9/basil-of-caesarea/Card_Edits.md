# Card edits: Basil of Caesarea (`basil-of-caesarea`)

New card, no existing card. Written to `basil-of-caesarea.card.json`. Checked with `tools/validate-census.mjs` on a scratch copy of the census with the card and the brief set in. The only errors are the ones the release step clears: no `secondReading` on the three quotations (six words or more, left out as instructed), and the brief's three modern quotations not yet listed in `tools/quote_renderings.json`. Every cited wording stands in its lines.

## Fields and evidence (files under `cic/texts/`; `npnf207` = `npnf207_cyril-jerusalem-gregory-nazianzen.xml`, `npnf208` = `npnf208_basil-letters-select-works.xml`)

- **otherNames:** census `informalName` "Basil the Great"; Jerome's note and Theodoret 4.16 (`npnf203...xml` 41555, 14087); "Basilius" in Rufinus HE 11.9 (`eusebius_werke...txt` 29991).
- **knownFor:** the brief's essence; Letter 94 (`npnf208` 30011-30023); Oration 43.63 "a little way from the city" (`npnf207` 42734-42742); Nicaea II canon 20 (`npnf214...xml` 41052-41062).
- **datesNote:** `npnf208` 556-557, 685-689, 776-777; Clarke, Life of Macrina 52; Gwynn `npnf213...xml` 11423-11424; Gregory of Nyssa, Life of Macrina 178-180.
- **placeNote:** Jerome `npnf203...xml` 41555-41556; Oration 43.34 (inland, `npnf207` 41972-41976); 43.15 (Athens, 41365-41369); 43.29 (Pontus, 41819-41821); `npnf208` 600-605 (the Iris); census `modernCountries`.
- **role, keyWorks:** Longer Rule 7 (Clarke 13174-13215); Oration 43.34 (41962-41964); On the Holy Spirit 1.3, 10.24, 29.71-72 (`npnf208` 8793-8823, 10553-10558, 14349-14406); Letters 94, 159, 223 (`npnf208` 29984-30023, 33450-33453, 39057-39062).
- **legacy.traces:** Gennadius and Fremantle (`npnf203` 42466-42471, 44607-44609); Benedict ch. 73 (Gasquet 4289-4292; Latin 10409-10412); Nicaea II canon 20 (41052-41062); Sozomen 6.34 (`npnf202...xml` 39955-39961); census `first-council-of-constantinople-381`; Theodoret (`npnf203` 14086-14087, 20714); Photius (`photius...txt` 1959-1971); Jerome (`npnf203` 41556-41557) and Jackson's chronology (`npnf208` 650-652); Palladius 457; census tradition `legacy`.
- **legacy.remembered:** Oration 43.15, 43.25, 43.28-29, 43.34-35, 43.37, 43.48-50, 43.58-59, 43.62-63, 43.78-80 (`npnf207` 41365-41369, 41700-41701, 41774-41821, 42005-42022, 42046-42056, 42305-42367, 42569-42621, 42725-42789, 43228-43275); Letter 223.2 (`npnf208` 39143-39153); Rufinus HE 11.9 (`eusebius_werke...txt` 30043-30050); Socrates (`npnf202` 13929-13931); Sozomen 6.16 (38325-38339). These are the items the outline and the review sent to the card.
- **uncertain:** the outline's Source Sheet section 5 (D1-D7) and Do not say; Review M3 and Recheck_Story's list for the card; E3 (Rufinus; `npnf208` 1241); R8 (Morison 370-382; Clarke 13154); D3 (Sozomen `npnf202` 31861-31863); H5 and H6 (`npnf203` 14166-14168; `npnf208` 710-711, 30050-30052); Sp8 (Hefele 17825-17832); Hefele 17893-17895; Sp3 and Letter 159 date (`npnf208` 742-743, 33450-33453); the English-only quotations (Outline, Quotes).
- **sources:** every file cited above. The about entries carry `date` only where the file's header gives one (Hefele 1876, Morison 1912) or the text is dated (787).
- **briefReferences:** one line for each beat, quotation or impact item in the brief, with its source lines above. No quotation marks.
- **quotationOriginals:** three, one for each quoted span. 1: `npnf208` 39133-39135. 2: Greek `basil_opera-omnia-pg31-grc-lat_migne1857.txt` 72547-72549, printed as the Greek it is rendered from, with Clarke's English beside it (13460-13464); Greek checked by hand against the line, including the spaced semicolons and `καθ᾽ ἑαυτὸν`. 3: `npnf208` 33483-33485. The outline marks 1 and 3 as rendered from English because the Greek of the Letters is not held.
- **Left out:** `label` (not an outside witness), `briefLength`, `secondReading`, and any connection to another entry.

## Conflicts with the census entry (listed, card follows the held sources and the brief)

1. `dates` "c. 329-379", `longDescription` "Basil died on 1 January 379": the card and brief say 378 or 379; the held editors differ (Jackson and Clarke 1 January 379, Gwynn end of 378).
2. `longDescription` dates On the Holy Spirit "not long after 373": the card gives Jackson's 374 and the tree's "about 375" and notes that Letter 159 (about 373) is not the reply to the attackers.
3. `longDescription` names "Eusebius of Caesarea" as the bishop who died in 370: the card keeps him by role, as the outline's Do not say asks (the name is an editor's insertion in `npnf207` 41776 and 42048).
4. `longDescription` says the friend "took it ill" and `why` says "about 370": no contradiction. The census `voices` and `sourcing` (Letter 38 disputed) are not contradicted.

## Claims not found

- Outline Sp8 and R8 rest on modern editors; held as written and placed under uncertain.
- The outline's claim that Clarke's edition "treats the Rules as Basil's" was not found at a line, so the card says only that Clarke's edition prints them under Basil's name (the title of the file).
