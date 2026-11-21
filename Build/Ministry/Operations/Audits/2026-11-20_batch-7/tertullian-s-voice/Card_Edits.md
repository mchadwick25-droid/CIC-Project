# Card edits: Tertullian (`tertullian-s-voice`)

Batch 7, 2026-11-20. New card: the census entry had none, so every field below is new. Written to `tertullian-s-voice.card.json`. Sheet items (S, E, T, I, D) and outline lines are in `Source_Sheet.md` and `Outline.md`. File short names as in the sheet (ANF3, ANF4, OEH1, OEH2, KRO, CSEL20, JER, JERL, EUS, EUS-ed, LACT-E, AUG, VIN, MON, HARN, BEN, MANSI8). Every cited line was re-read in its file. Keys used are only those `tools/validate-census.mjs` allows (not run). No `briefLength`, no connections, no `secondReading`.

## Fields

| Field | Evidence |
|---|---|
| `otherNames`: Tertullian of Carthage; Tertullianus; Septimius Tertullianus; Tertullianus Afer | "Tertullian of Carthage": the census `informalName` and the brief's first paragraph of the essence. "Tertullianus": JERL 55610; AUG 2827. "Septimius Tertullianus": LACT 22707; LACT-E (Fletcher's English, "Septimius Tertullianus also was skilled"). "Tertullianus Afer": Jerome's Chronicle, `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` 43480-43481 (S4). |
| `knownFor` | The brief's paragraph 2 and the outline's essence (Outline 5); "foremost" by Mark's ruling of 2026-11-20 (Outline "Do not say"), VIN 13555-13557, ANF4 17041. Apology: E1. Prescription: E4. Against Praxeas: E7, T4, T5. New Prophecy: E5. Augustine counts the Tertullianists among the heretics: AUG 2827-2835, 2868-2873. |
| `datesNote` | No death: E9. Jerome's reigns and old age: JER 40498-40499, 40514-40516 (S2, E9). Birth about 160 and death about 245: JER-ed 40493-40494. Birth about 160 common view, Nöldechen about 150 and about 230: EUS-ed 10241-10248. Apology 197 to 204, 197 practically established: EUS-ed 10294-10303; 198 and 204: ANF3-ed 1443-1446. Prescription about 200: MON 17156-17162. Turn 207 to 212: MON 17249. Break at the start of 213: MON 17071-17076. Against Praxeas after 213: MON 17462-17466 (ANF heading "not earlier than 208": ANF3-ed 51001). On Modesty 217 to 222, probably the last surviving: MON 17466-17469. |
| `placeNote` | Carthage in the province of Africa: JER 40496, JERL 55614 (S1). Tunisia: census `modernCountries`. "One of those especially distinguished in Rome": EUS 10279-10280 (S5). |
| `role` | Eusebius: well versed in the laws of the Romans (EUS 10241-10242, 10272-10280). Convert: S7. New Prophecy: E5. |
| `keyWorks` (three) | Apology: E1, E2, ANF3 3997-4003, 4653-4661. Prescription: E4; "demurrer, or formal objection": ANF3-ed 20037-20038 (S6). Against Praxeas: E7, T3, T4, T5; KRO 11738-11739, 12558-12562. On Modesty is left to `briefReferences` and `uncertain`, since the key works hold at most three. |
| `legacy.traces` | Cyprian: I3, JERL 55618-55626, JER 40500-40505; Benson: BEN 2385-2389, 40590-40592. Novatian: I2, JER 40895-40897, HARN 22546-22548. The words: T5, I1, NPNF9-ed 427-429 (Sanday). Followers: I5, AUG 2829-2835. |
| `legacy.remembered` | Lactantius: LACT 22707-22710, LACT-E 4569 (I4). Augustine: AUG 2827-2828. Vincent and Hilary: VIN 13555-13557, 13571-13580 (I6). Jerome's "keen and vigorous character": JER 40497. |
| `uncertain` (15 items) | 1 sources and gaps: S7, EUS-ed 10250, EUS-ed 10267-10268, S header. 2 law: S5, D3; EUS note 273 at 10273-10279; EUS-ed 10248-10249; NPNF9-ed 430; MON 15444-15497 (hypothesis at 15481-15484; relative at 15492-15494; "incontestable" 15498-15500). 3 why he turned: E6, D1; JER 40506-40509; AUG 2868-2873. 4 withdrawal: E5, D6; ANF3 51074-51076; ANF3-ed 51077-51081; MON 17071-17076. 5 office: EUS-ed 10257-10258; MON 15572-15589; EUS-ed 10252-10256. 6 first in Latin: D4; JERL 55610-55613; VIN 13555-13557; ANF4 17038-17042 (Coxe, a.d. 210, founder of Latin Christianity); ANF4 17128-17141 (date keenly disputed, perhaps about 166). 7 the words: T5, I1; ANF2-ed 8993-8997; ANF3-ed 51897-51899 (Kaye). 8 Praxeas and the edict: E7, E8; ANF3 51044 note; MON 17466-17469. 9 last book: E8, E9; EUS-ed 10260-10262 (a few works in Greek). 10 Cyprian's words: I3, D2; VIN-ed 13543-13548. 11 Novatian: I2. 12 father: S4; JER 40497; VIN-ed 13540. 13 Vincent and the decree: I6, D7; VIN-ed 13575-13576; MANSI8 17218-17222 and the note at 17236-17252. 14 Perpetua: ANF3 59448-59450. 15 the quoted Latin: Source Sheet "Language and text"; T4. |
| `sources.ownWords` / `about` | Files as listed in the sheet's "Files and short names", all re-checked to exist. `about` entries carry `date` (a string or null) as the validator requires; dates: JER 38785 (392 or 393 in the sheet), AUG 1098 note (about 428), VIN 434, LACT about 305 to 310, MON 1901, HARN 1904, BEN 1897; others null. |
| `briefReferences` (11) | One line for each part of the brief; no quotation marks. Chapters: Apology 1, 40, 50; Prescription 15, 19, 21, 36, 37; Against Praxeas 1, 2, 12; On Modesty 21; Jerome Lives 53 and 70 (the English edition's chapter numbering differs by two). The last line names the tradition, as the other cards do ("The Case Made in Latin", S3). |

## Quoted spans, from the brief's quotation marks

Every `secondReading` is left out: the second-reading step fills them. Each `modern` is the brief's wording exactly.

| # | Brief span | Printed wording (file and lines) | Original | Status |
|---|---|---|---|---|
| 0 | "Then let the truth reach your ears ... silent writing." | ANF3 1457-1459 (Thelwall) | none: Latin held only in Oehler's damaged scan (OEH1 11253-11261), no held print confirms its readings | awaiting second reading |
| 1 | "One thing only she asks for now: not to be condemned unknown." | ANF3 1463-1465 | none, same reason | awaiting second reading |
| 2 | "the blood of Christians is seed." | ANF3 4661 | OEH1 30954-30955, "semen est sanguis Christianorum" (the words are clean in the scan) | awaiting second reading |
| 3 | "By what right, Marcion, ... turn my springs aside?" | ANF3 21744-21746 (Holmes) | none: damaged scan (OEH2 2280-2290, which lost "quando et unde") | awaiting second reading |
| 4 | "This property is mine. I have held it long; I held it first." | ANF3 21748-21749 | none, same | awaiting second reading |
| 5 | "I am the heir of the apostles." | ANF3 21751 | none, same | awaiting second reading |
| 6 | "I have already said how you should take the word 'another' ... joined together." | ANF3 51894-51900 (Holmes) | left out: KRO 12558-12562 misreads "distinctionem" as "distmccionem" inside the span. OEH2 43865-43868 confirms the reading, but the checker only allows such a fix through `tools/quote_scan_readings.json`, which this brief does not touch, and Oehler's own page reads "teneam" with no "etsi", so it is not the same text as the modern wording (Kroymann's "ubique teneo" with "(etsi)"). Both readings are in the quotation's `uncertain`. | awaiting second reading |
| 7 | "not the church which consists of a number of bishops." | ANF4 9544-9545 (Thelwall) | CSEL20 15313-15314, "non ecclesia numerus episcoporum" (clean) | awaiting second reading |
| 8 | "Give me the master." | JER 40505 (Richardson) | JERL 55625, "Da magistrum" (clean) | awaiting second reading |

A check of my own, using the validator's fold rule on the card file: every `printed` and `original` stands in its cited lines, and every `modern` is a quoted span of the brief. The validator itself was not run.

## Conflicts with the entry's other fields, and claims not found

- `why` and `voices` call him "the first major Christian author to write in Latin" and "probably a trained rhetorician". The card says foremost, not first (Mark's ruling; D4: Jerome says first among the Latins after Victor and Apollonius, the Octavius may be older), and says trained in Roman law is Eusebius's word with practice contested (S5). Listed under `uncertain` items 2 and 6.
- `why`: "invented them - trinitas, persona, substantia, sacramentum". The held sources show the first three in his text (T5) and Sanday says he coined terms; "sacramentum" is not found in the held sources used here, and the Greek triad is older (ANF2-ed 8993-8997). The card says "put to work" and lists the point under `uncertain` item 7.
- `legacy`: "never made a saint" and "he never quite belonged anywhere": not found in any held source (I6; Mark, 2026-11-20). The card does not repeat it.
- `why`: "trained as an advocate" is Contested (S5, D3); the card does not say "advocate".
- `dates` "c. 197-220": the end year 220 has no held source. The card gives Monceaux's 217 to 222 for the last surviving book and says no source gives his death (E8, E9). Not a contradiction.
- `voices`: "Jerome reports that Cyprian read Tertullian every day": it is Jerome's hearsay through Paul and Cyprian's secretary, and the English translation of Jerome garbles the chain (I3, D2). The card tells the chain in `uncertain` item 10.
- `legacy`: "Cyprian and Jerome read him closely, and Augustine called his many works eloquent". Augustine: AUG 2827-2828, in `legacy.remembered`. Jerome's own reading of him: not found in the held sources here beyond his life of him.
- Not found: any year for his conversion in his own words (S7; McGiffert's 180 to 190 is an editor's guess), and any source for his death (E9).
- Not used, kept for the card in the outline but left out here to stay in scope: the Apology's Greek translation (I7), the jurist of the Digest beyond the hypothesis, Hilary's own text (not held), the decree's details beyond one clause.
