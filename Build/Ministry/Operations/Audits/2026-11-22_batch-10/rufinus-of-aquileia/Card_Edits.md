# Card edits: Rufinus of Aquileia (`rufinus-of-aquileia`)

Card written to `rufinus-of-aquileia.card.json` from `Card.existing.json`. Everything not listed here is unchanged, word for word and in order. No `briefLength`. Connections left out.

## Clearly wrong (1)

1. `legacy.traces[0]`: "are known only through his Latin" -> "are known chiefly through his Latin".
   Evidence: `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` 22122-22124 ("We possess it chiefly in a Latin translation by Rufinus"; the Greek has "for the most part" perished), 21996-22002 (a few Greek fragments are preserved); the brief: "survive chiefly in his Latin, his editors note." On First Principles is named in the sentence, and Greek fragments of it exist, so "only" is contradicted.

## New (appended; nothing existing reworded)

2. `legacy.traces`, new entry 5 (Gennadius): "opened to the Latin speaking church the greater part of the Greek literature". Evidence: N203 (`npnf203_theodoret-jerome-gennadius-rufinus.xml`) 42467-42470. Sent to the card by the outline's Cut first.
3. `legacy.traces`, new entry 6 (Frumentius, from Edesius). Evidence: `eusebius_werke-bd2-2-...mommsen1908.txt` 27383-27385; `npnf202_socrates-sozomen-ecclesiastical-histories.xml` 4372-4374. Sent by the fresh read (minor 3) and the outline's Cut first.
4. `legacy.traces`, new entry 7 (Socrates still used Rufinus): N202 5666-5668. Cut first item.
5. `legacy.traces`, new entry 8 (only small portions of Jerome's version survive): ANF4 22126-22128. Cut first item. Attributed to the Ante-Nicene Fathers introduction, not to a named editor.
6. `uncertain`, new entry 9 (his method is the quarrel): Rufinus's claim, N203 45750-45755, 45775-45780; Jerome's charge, N203 51287-51303; Fremantle's judgment, N203 45702-45706; ANF4 21996-22002. From the outline's Do not say and the review's blocking finding 1; the brief says "He said he followed that method."
7. `uncertain`, new entry 10 (dates): First Principles preface 397, N203 45693-45694; published early 398, N203 44222; Church History probably 401, N203 44550-44555. The outline says no year in the brief.
8. `sources.ownWords`, new entry: Rufinus's preface to First Principles as printed in Jerome's letters (Letter 80), N206 18367-18372 (second print behind Quote 2).
9. `sources.about`, new entries: Jerome Letter 3 (N206 3752-3942, Quote 1); Apology against Rufinus Book 1 in Latin, PL23 (Quote 3's original); Introductory Note to the Works of Origen, ANF4 (author null: the note is not signed in the file); McGiffert's Prolegomena to Eusebius, N201 5232-5233.
10. `briefReferences`: 15 entries, one for each source the brief draws on (lines in the entries above and in `Source_Sheet.md`). No quotation marks.
11. `quotationOriginals`: three entries, one for each quoted span in the brief.
    - Quote 1, "A friendship that can end was never real.": printed N206 3941-3942. Latin not held. No `secondReading` (eight words).
    - Quote 2, "Where I found anything ... again and again.": printed N203 45775-45780. Latin not held; the note records that the second English print (N206 18367-18372) has no "rule of faith" in its second half. No `secondReading`.
    - Quote 3, "In the books On First Principles ...": printed N203 51325-51331; original Latin PL23 31112-31115 ("simpliciter ... transtuleras"). The scan misprints the Greek title word (reads "Arlῶν"), so the Latin starts after it; the English print confirms the reading. No `secondReading`.

## Not carried, or not found

- Outline "to the card" items with no field on a card: Palladius's pilgrims at their own cost and "made a priest" (both in `briefReferences` item on Palladius), the three clergy (in `briefReferences`), Didymus (in `briefReferences`), "not a defender or a champion of Origen" (in `briefReferences`, no quotation marks), "friends asked him for Origen", "asked about him by the bishop of Jerusalem", the household that fled Italy with him (the last three not given a separate line; they are in sources cited in `briefReferences`).
- Church History date 402-403: stands only in the header of the Latin edition's library file, not in a held scholar's words; left out. Fremantle's 401 is carried.
- Optional items left out as optional: the Creed praise by Gennadius, Jerome's Letter to Rusticus, Augustine's lament (already on the card).
- Existing claims not found in a held source, left in place: none found. "Rufinus of Concordia" (otherNames) rests on Jerome and the editors naming Concordia his native town (N203 44045-44048), not on a held use of the name itself.

## Second pass (2026-11-23)

### Checker changes

FIX 1 to FIX 8 (`briefReferences[0]`, `[1]`, `[2]`, `[3]`, `[5]`, `[9]`, `[10]`, `[13]`): applied word for word. Each old text occurred once.

### Scan readings to add

None listed by the checker.

### Items added (N203 = `npnf203_theodoret-jerome-gennadius-rufinus.xml`)

1. `legacy.traces`: "Gennadius says Rufinus wrote on Jacob's blessing on the patriarchs in a threefold sense, \"the historical, moral and mystical\"." Evidence: N203 42484-42487. Outline Leave out (Benedictions of the Patriarchs, to the card).
2. `legacy.traces`: "W. H. Fremantle says Rufinus also wrote a History of the Monks of the East, partly from personal knowledge, partly from what he had heard or read of them." Evidence: N203 44396-44398. Same outline item (History of the Monks).
3. `legacy.traces`: "Palladius of Helenopolis says that Melania and Rufinus received at their own charges those who visited Jerusalem in pursuance of a vow, bishops and monks and virgins." Evidence: `palladius_lausiac-history_clarke1918.txt` line 501, [6]. Cut first 4; Palladius credited.
4. `uncertain`: three clergy of his baptism, Chromatius, Jovinus and Eusebius, "all now bishops"; one then presbyter, one archdeacon, one deacon, the third his teacher in the creed. Evidence: N203 46563-46575. Cut first 6. Worded as Rufinus's own account, in the order he gives.
5. `uncertain`: six years in Egypt and two more where Didymus lived; Fremantle calls him a pupil of Didymus. Evidence: N203 49434-49439 (Rufinus); N203 44084-44088 (Fremantle). Cut first 8.
6. `uncertain`: the tenth book of Eusebius left out for its praise of bishops and the history folded into the ninth; his own two books "partly from the traditions of the former generation, partly from facts within my own memory"; "like the two fishes to the loaves". Evidence: N203 58776-58787. Cut first 2 and 3.
7. `uncertain`: "I am not a defender or a champion of Origen" in the Apology to Anastasius. Evidence: N203 46070-46071. Cut first 12.
8. `uncertain`: Anastasius's letter answers John of Jerusalem, who had asked his advice about Rufinus. Evidence: N203 46149-46152; Fremantle at 44423-44425. Cut first 17.
9. `uncertain`: the brethren constantly adjuring him to translate On First Principles, and he yielded to Macarius; Fremantle says Urseius and Macarius asked him to translate various Greek books, among them that one. Evidence: N203 45741-45745; 44208-44211. Cut first 18.
10. `uncertain`: in the preface to Origen on Numbers he joined Pinianus and his company in their flight; Fremantle says the party left by way of Sicily and Africa and Rufinus joined their religious company. Evidence: N203 59013-59015; 44436-44441. Cut first 19.

The rest of the outline's "to the card" items were already on the card: Frumentius and Edesius, "from Constantine to the death of Theodosius" (keyWorks), the Pamphilus Defence, Jerome's fragments, Gennadius's "opened to the Latin speaking church", Socrates still using him, Augustine's lament, the priesthood (`role`), the Recognitions and Xystus, the birth year and Concordia, Epiphanius's prayer (`legacy.remembered`). The fresh read's Frumentius item is trace 6.

### Skipped

- Jerome's "Grunnius" satire (Letter to Rusticus, outline Leave out): worded "to the card if wanted", not held as a text (only Fremantle's mention at N203 44120); left out.
- Quote 1's first sentence (Cut first 15): the checker's FIX 1 keeps it out of `briefReferences`; the sentence is a printed line, N206 3936-3942, and no card field takes it.
- Gennadius's praise of the Creed: not marked for the card.
