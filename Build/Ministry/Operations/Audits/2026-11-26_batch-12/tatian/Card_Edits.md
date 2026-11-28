# Card edits: Tatian (`tatian.card.json`)

A full new card, built under the role's "A new card". The starting card (`Card.existing.json`, the same as the census `card` now) was a pointer only. Evidence is given as Source_Sheet rows (S, E, I, D), the outline at its lines, or the brief's sentence. Files are under `cic/texts/`; short names as in `Source_Sheet.md` (AG, AG-G, IR, HI, HI-G, EU, EP, JE, JC, TH, TH-M, DI, AD, SE, TE), plus MS `michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` and VC `liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt`. Every cited line was re-read in its file for this card. Keys follow the `polycarp-of-smyrna` card.

## Fields kept word for word from the starting card

| Field | Kept text | Evidence |
|---|---|---|
| `knownFor` | "A hearer of Justin Martyr who attacked Greek learning in his Address to the Greeks and wove the four Gospels into one, the Diatessaron." | E3 (IR 33664; HI 13005-13006); E5; E10; brief paragraph 2. |
| `keyWorks[0]` title, and `about` from "his conversion" to the end | as before | E1, E2, E5g; brief paragraphs 3-4. |
| `legacy.remembered[2]`, first sentence | "Eusebius of Caesarea and Jerome of Strido name him the founder of the Encratites." | E8 (EU 26424-26425; JE 40092-40093). |
| `sources.ownWords` (all three) | as before | AG, AG-G, DI. |
| `sources.about`: Epiphanius (Holl) and Theodoret (Maran) entries | as before | EP, TH-M. |

## Fields changed or new

| Field | Old | New | Evidence |
|---|---|---|---|
| `shortDescription` | none | written fresh, two sentences | Brief paragraphs 2-3 (born in the land of the Assyrians; a Christian in the middle of the second century; the Address; the Diatessaron read in worship). |
| `datesNote` | "Broke with the church about 172, by Eusebius's Chronicle" | four sentences: no birth or death year; Irenaeus's "after Justin's death"; the Chronicle's twelfth year of Marcus Aurelius, about 172; Jerome's reign | S4 (IR 33664-33666; JC 42910-42912, 43059-43060; JE 40098-40099); outline Setting and Cut first 16 ("in the reign of Marcus Aurelius", card). |
| `placeNote` | "Born in the land of the Assyrians; at Rome; later in Mesopotamia" | adds "he says", the great city, where he taught; Mesopotamia "by Epiphanius's report"; only Epiphanius names it among held old sources | S1 (AG 7460), S3 (AG 6550; EU 29214-29215), E9 (EP 15997-16002); outline beat 6 and Review B2 (the "only one" point to the card). Said of the held texts, not as Holl's judgment; Holl goes to `modernWorks`. |
| `role` | "Apologist and teacher" | "Teacher and writer" | "Apologist" is a label the card never explains (Kit, Explain it). Teacher: E6, IR 33667 ("being a teacher"). |
| `keyWorks[0].about` | begins "his conversion" | begins "a book written as a speech, telling of" | Outline Words to explain (*Address*, EU 26486-26487). |
| `keyWorks[1].about` | "one gospel woven from the four, long read in the Syriac-speaking churches" | adds the name's sense; "read in worship"; known now from later translations | E10 (EU 26433-26434; DI 10422-10424); I1 (AD 65); I3 (DI 10422-10435; VC). "Long read" dropped: the outline gives read in worship (Do not say, "read in worship"). |
| `keyWorks[2]` Problems | none | new | E6 (EU 29217-29223); outline Cut first 1, card. |
| `legacy.traces[0]` | Hogg's "very widely if not universally read" | the Doctrine of Addai's picture, narrated | I1 (AD 65). Hogg's summary is a modern judgment (sheet I1); Kit Rigor and Header "Modern works on the cards". No quote marks: the sibling's span is barred. |
| `legacy.traces[1]` | Ephrem wrote a commentary (inside traces[0]) | later writers of the Church of the East; Isho'dad and the Chronicle of Seert | I1 (DI-ed 1763-1768; SE 15906-15907); brief paragraph 9. |
| `legacy.traces[2]` | (was `remembered[2]`) "replaced more than two hundred copies ... in his diocese" | moved to traces; "held in honor in his churches", gathered, put away, the four Gospels brought in | I2 (TH 29735-29741; TH-M 14984-14987); outline Do not say ("Theodoret removed it from the Syriac churches"; "in his own churches", TH 29738). "Diocese" was not the source's word. |
| `legacy.traces[3]` | none | the Arabic translation, its first words and its last line | I3 (DI 2195-2196, 10422-10435); outline Cut first 13 (the Arabic ending), card. |
| `legacy.traces[4]` | none | Victor of Capua's preface | I3 (VC 23150-23158, 23203-23206; OCR rough, read for the sense only, no quotation). The Codex Fuldensis and its date are Hogg's (modern) and are left out. |
| `legacy.traces[5]` | none | the Address kept: Eusebius, Jerome, Clement | I4 (EU 26484-26486; JE 40096-40098; CL 29724-29727); outline Cut first 5, card. |
| `legacy.remembered[0]` | "...the first to deny that Adam was saved." | adds Irenaeus's answer in Book III | E7 (IR 33662-33664, 43907-43913). |
| `legacy.remembered[1]` | none | Hippolytus | E3, E7 (HI 13005-13013). |
| `legacy.remembered[2]` | first sentence | adds Jerome's chapter title, glossed | I5 (JE 40084). |
| `legacy.remembered[3]` | none | Theodoret: longed to head a sect | E7 later repeaters (TH 29632-29633). |
| `legacy.remembered[4]` | none | the writer against Artemon | I4 (EU 32129-32139); outline Leave out: card. |
| `uncertain` (all) | five items | eleven items | Rebuilt. The starting card's items rested on McGiffert, Zahn, Harnack, Hogg and Lightfoot, each a modern opinion that the Kit and the Header ("Modern works on the cards") keep off the card. Each new item stands on old texts: [0] who tells it (outline Who tells it); [1] D1 (AG 7460; EP 15995; TH 29630; DI 2111; SE 15907); [2] D2; [3] D3, outline Leave out ("card"); [4] D5, E4 (AG 6553-6554; EU 24073-24078), outline Leave out ("Eusebius's dropping 'and indeed on me' ... card"); [5] E6; [6] E7 (Irenaeus's motive his; Tatian's side not held); [7] D4, E8 (IR 33655-33664; EU 26185-26186, 26424-26425; JC 43059-43060; JE 40092-40093; EP 16007-16009; TH 29639-29642; EP 16066-16072), outline Cut first 4, card; [8] D6, E10, and Fresh_Read ("I know not how" in its plain sense, to the card); [9] D7 ('Abdisho, DI-ed 1904-1908, outline Leave out "card"; MS 14340-14354, sheet Library sweep "card"); [10] I2 (Rabbula, DI-ed 1914-1919), outline Leave out ("card"), with no claim that it aimed at the Diatessaron (Hogg's and Gwilliam's reading). |
| `sources.about` | Irenaeus, Hippolytus, Eusebius, Jerome, Epiphanius, Theodoret (Maran) | titles widened to the chapters used; added Wendland's Greek, Clement, Pseudo-Tertullian, the Chronicle (JC), Theodoret in PG 83 (TH), the Doctrine of Addai, the Chronicle of Seert, Michael the Syrian, Victor of Capua | Each file is cited by a card line or quotation. |
| `briefSources` | none | eleven old sources the brief draws on | The brief's credits and quotes: AG, AG-G, IR, HI, EU, JC, EP, TH, TH-M, Theodoret's letter (JE 33157-33166, "under Antioch"), SE (Ephrem). |
| `timeline` | none | nine periods, 44 lines, each with file and lines | All rows of the sheet the outline uses, in order; "Date unknown" or the record's own phrase where no date is held (Stage Two Kit 2.3). Cut first items 2, 3, 6, 10, 11, 12 (with "heretic" glossed), 14, 15, 17 and 18 are here, as the outline marks them. |
| `briefReferences` | sixteen lines | thirteen lines | Rebuilt for the brief as it stands. Dropped: Address 35 "the turn" and Address 42 "the closing stand" (no longer quoted); "Coxe and Ryland, the editors, take them to be the Hebrew Scriptures" (modern); McGiffert's "Justin's death about 165" (modern date; the brief gives none); Address 2, 32, 33 (no longer told); Theodoret's "two hundred books" as a quote; Hogg on the charge, on Rabbula and on the Codex Fuldensis (not told; modern); Hogg's "very widely" (modern). Added: Address 29, Rhodon, Valentinus and Marcion at Rome (IR 39969-39985), Hippolytus on Adam, Ephrem's role, Theodoret's Eranistes (TH 4230-4240) and letter. |
| `quotationOriginals[0]` | Address 35 | the brief's Quote 1 (Address 29) word for word; printed Ryland AG 6971-6978; `uncertain` on the Greek and Latin | Brief paragraph 3; outline Quote 1; E2. Otto's Greek and Latin (AG-G 10388-10394, 10458-10465) are held only in a damaged OCR scan, so by the role the English prints alone; no `original` is given. |
| `quotationOriginals[1]` | "the self-controlled" | the brief's Quote 2 (Irenaeus) word for word; printed IR 33664-33668; `uncertain` on the Greek | Brief paragraph 6; outline Quote 2; E7. The Greek (EP-ed 15968-15969, 16015-16016; HI-G 17441-17442) is in fragments in two damaged scans and lacks one clause, so no `original` span can be given. "the self-controlled" is no longer quoted in the brief (outline Do not say). |
| `quotationOriginals[2]` | Theodoret's two hundred books; Address 42 | removed; new entry "through four", printed Τὸ διὰ τεσσάρων (EP 16075-16076), `secondReading` "checked at card" | Brief paragraph 8; E10. Under six words. The other two dropped spans are no longer quoted. |

`secondReading` is left out of quotations 0 and 1 (each six words or more), so release sets it.

## Entry fields (for release, after the checker)

- `teaser`: no change. It says no more than `knownFor` and the brief.
- `modernWorks` (new; editions and translations the outline used to clarify a text, all printed before 1931):
  - {"title": "Tatiani Oratio ad Graecos (Corpus Apologetarum Christianorum saeculi secundi 6)", "author": "J. C. T. Otto (ed.)", "year": "1851", "note": "The Greek of the Address with a Latin translation and notes, including the clause on the making of all things that the English leaves out."}
  - {"title": "Fathers of the Second Century (Ante-Nicene Fathers, volume 2)", "author": "Alexander Roberts and James Donaldson (ed.), J. E. Ryland (tr. of Tatian)", "year": "1885", "note": "English translation of the Address to the Greeks and of Clement's Stromata."}
  - {"title": "The Church History of Eusebius (Nicene and Post-Nicene Fathers, second series, volume 1)", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes that quote the Chronicle's entry for Tatian."}
  - {"title": "Epiphanius, zweiter Band: Panarion haer. 34-64 (Die griechischen christlichen Schriftsteller 31)", "author": "Karl Holl (ed.)", "year": "1922", "note": "The Greek text of Panarion 46, with notes that give the Greek of Irenaeus and Eusebius on Tatian and mark which details only Epiphanius reports."}
  - {"title": "Hippolytus Werke, dritter Band: Refutatio omnium haeresium (Die griechischen christlichen Schriftsteller 26)", "author": "Paul Wendland (ed.)", "year": "1916", "note": "The Greek text of the Refutation, with notes that print the Greek of Irenaeus on Tatian's break."}
  - {"title": "The Diatessaron of Tatian (Ante-Nicene Fathers, volume 9)", "author": "Hope W. Hogg (tr.)", "year": "1896", "note": "English translation of the Arabic Diatessaron, with an introduction that quotes the later Syriac writers on the book."}
  - {"title": "Corpus Apologetarum Christianorum saeculi secundi 9", "author": "J. C. T. Otto (ed.), with the prolegomena of Prudentius Maran", "year": "1872", "note": "Prints Theodoret's Greek and Latin on the Diatessaron and its copies."}
  - {"title": "Eusebii Pamphili Chronici canones latine vertit, adauxit, ad sua tempora produxit S. Eusebius Hieronymus", "author": "J. K. Fotheringham (ed.)", "year": "1923", "note": "Jerome's Latin of Eusebius's Chronicle, with the entry for Tatian under the twelfth year of Marcus Aurelius."}
  - The starting card's `sources` held no modern work, so none moves. Not listed: Coxe's and Ryland's judgments, McGiffert's and Harnack's dates, and Hogg's claims on language and use (each a claim of its own; sheet D8, E5, E10).
- No `why`, `relationsSummary`, `legacy` or `voices` on the entry; nothing to change.

## Conflicts and not found

- Entry `region` "Rome, Edessa", `placeLabel` "Rome · Edessa" and the Edessa row in `modernCountries` place Tatian at Edessa. No held source does (S5; outline Do not say, "Tatian went to Edessa"). The card does not repeat it. For release to judge; not changed here.
- Entry `regions` "Asia Minor": no held line puts him there (S1, S3, E9). Not changed; the map build slice owns the field.
- The brief's three quoted spans (Quote 1, Quote 2, "through four") are renderings, not verbatim in a cited file, and are not yet in `tools/quote_renderings.json`; the three old Tatian listings there are for spans the brief no longer quotes. Release lists the new ones and removes the old.
- Left out, not carried: Aphrahat and the Diatessaron (editor's inference, Inferential-Thin, sheet I1; the Kit keeps it off the card); Hogg's verse counts and the Codex Fuldensis's manuscript details (modern); Epiphanius's twelfth year of Antoninus, his blind man and "According to the Hebrews" (outline Leave out, not card).
- Nothing from the starting card is listed as not found; what was dropped was dropped as modern opinion or as no longer in the brief.

Scorer (`python -m engine.m1.profile_readability`, card running text, outside the repository): `2197 words, grade 7.6 (names out 5.8), reading ease names out 78.6, 14.2 words a sentence, 0.1 joining words per 100, 26% short sentences, longest sentence 30 words - pass (note: grade 7.6 is under 8: the listener read checks it is not flat)`

Validator (`tools/validate-census.mjs --skip-quotes` on a census copy outside the repository, with this card and the brief as `longDescription`): the only errors are the two missing `secondReading` values, which release sets. Each `printed` stands at its lines. The two quoted spans in the card's own prose ("I know not how", "In the beginning was the Word") were checked by a script against the cited files and found.

## Entry fields (card check)

- `modernWorks`, the entry titled `Corpus Apologetarum Christianorum saeculi secundi 9`: change its `note`.
  - Old: `Prints Theodoret's Greek and Latin on the Diatessaron and its copies.`
  - New: `Prudentius Maran's prolegomena on Tatian, which quote the Greek of the Address, chapter 29, and of Irenaeus on the break, and Theodoret's Greek and Latin on the Diatessaron and its copies.`
