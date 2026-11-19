# Card edits: Patrick (`patrick-of-ireland`), new card

Everything is new; there was no card. Evidence is cited as Source_Sheet item (S, E, I, D) with its file and lines, or the brief's sentence. PE = White 1920 English (`cic/texts/patrick_writings-and-life-with-muirchu-eng_white1920.txt`); PE-ed = White's own introduction and notes in it. All lines re-read in the files.

## Fields

| Field | Evidence |
|---|---|
| otherNames: Patricius, Saint Patrick | Patricius: Patrick's own name for himself, PE 1678-1680 (Ego Patricius, Latin, ST 5944). Saint Patrick: census informal name (entry field `informalName`) |
| knownFor | Brief: "Almost all we know of him comes from two short Latin writings of his own"; E1, E3, E5, E7, E13; I1 (PE-ed 234-238) |
| datesNote | S3 (PE-ed 251-253, 645-646); D2 (AU 362-363, 1473-1475, 1649, 2632-2633, 2638-2640). Patrick gives no year (S3) |
| placeNote | S1 (PE 1682-1685; PE-ed 403-406: Banavem Taberniae not placed); E2/D6 (no place for slavery); E5 (Wood of Foclut, PE 2079-2104; White's Mayo, PE-ed 545-546); E7 |
| role | E7 (PE 2842-2844: bishop in Ireland) |
| keyWorks: Confession | E11 (PE 1778-1781), E15 (PE 2765-2771), PE-ed 1617-1625 (title not penitential), brief sentence on the Confession |
| keyWorks: Letter | E12 (PE 2855-2957), D7 (outcome not known) |
| legacy.traces 1 | I1: PE-ed 1532-1536, 1549-1550, 1657-1659 |
| legacy.traces 2 | I2: BAN 5011, 5053-5055; BAN file header (manuscript c. 680-691); hymn date Contested (Witness kinds; PE-ed 1277-1282). Brief: "More than two centuries on, a hymn copied by monks called him the teacher of the Irish" |
| legacy.traces 3 | I3: PE-ed 1402-1406; brief: "Armagh, a church in the north of Ireland that claimed him as founder" |
| legacy.remembered | I4: MU 5208-5210, 5228, PE 3593-3595 (before 699); NEN 1210-1211, 1225, 1300; LIS 16281-16282 |
| uncertain 1 | S4, D4: PROS 54222-54223; Sheet "No independent fifth-century witness names Patrick" |
| uncertain 2 | D2; Sheet Witness kinds (which text came first not known) |
| uncertain 3 | E8 (PE 1914-1915, 2329-2331) |
| uncertain 4 | E7, D3: PE-ed 995-1005; NEN 1224-1227 |
| uncertain 5 | E10, D5: PE 2129-2163, 2219-2232 |
| uncertain 6 | D6: PE-ed 528-531, 582-587 |
| uncertain 7 | E12: PE-ed 2803-2812; ST 7462-7463 (Stokes: a Briton) |
| sources | Files named in the Source_Sheet "Files and short names"; each exists under `cic/texts/` |
| briefReferences | One line per brief paragraph; chapter numbers checked against the numbered chapters in PE (Confession 1-62, Letter 1-21). No quotation marks, none being verbatim in the brief |
| quotationOriginals | Below |

## Quoted spans: all awaiting second reading

1. "I am Patrick, a sinner. I am utterly unlearned, and the least of all believers. Very many people look down on me." Printed: PE 1678-1680. Original: ST 5944-5946 (PL 195-196 is clean Latin but carries a stray footnote mark, "sum l apud", so it does not stand verbatim). Awaiting second reading.
2. "We beg you, holy boy, come and walk among us once more." Printed: PE 2099-2101. Original: PL 669-670. Awaiting second reading.
3. "By birth I was a free man, and my father was a town councillor. I sold my noble rank ... slave in Christ to a foreign people." Printed: PE 2989-3009, written as the sheet reads it (E13). Awaiting second reading. No `original`: the Latin is held only as ST 7370-7374 (scan faults: decoriorie, mcain, peni- tet, perennis uitoe) and PL is garbled, so no Latin stands verbatim.

No `secondReading` is set on any entry, as ordered. Note for the second-reading step and the engineering owner: the validator requires `secondReading` on every entry, so the card fails until it is filled.

## Scan faults the validator will see

Quote 3's printed English (PE 2989-3009) does not stand verbatim in the file: it crosses a page break with footnotes and running heads (PE 2991-3006), prints "jny" for "my" (PE 2990), and "^f" for "of" (PE 3009). The validator passes this only through `tools/quote_scan_readings.json`, which I was told not to edit. Those readings need adding there (file, lines, scan, reads, and a `drop` for the page-break lines) before the card can pass.

## Conflicts with the entry's existing fields

None found. Notes:
- `dates` "c. 432-461" and the teaser's "c. 432 to 461": 432 is the annals' date for his coming and 461 is White's death date; the card's datesNote says both are reckonings and that his death is recorded under 457, 461, 491 and 492 (D2, Contested). Not a contradiction, but the entry presents the pair without that qualification.
- `legacy` (the census) names the swineherd for seven years against his own six; the card keeps the same split (D1).
- `voices` names Muirchu as active about 697; the card says only "before 699" (PE 3593-3595).

## Claims not found / left out

- Nothing in the card lacks a cited line. Left out on purpose: the date of the Confession beyond White's "probably not earlier than 454" (a reckoning); Bury's summary of his achievement (I5, left for a later pass); connections to other entries.
