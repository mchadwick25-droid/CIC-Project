# Card edits: Marcionism (`marcion-marcionism`, tradition)

Card: `marcion-marcionism.card.json`, from `Card.existing.json`. A tradition has no `card` key, so the card file holds the census entry's card fields in the same order, as the batch's other tradition cards do. `why`, `relationsSummary` and `teaser` are left word for word in the card file; their changes are under **Entry fields**. Every field not listed below is word for word. New keys follow at the end: `uncertain`, `sources` (the `cyril-and-methodius` form, `about` only: no work by a Marcionite is held as a text), `briefReferences`, `quotationOriginals`, `modernWorks`. File abbreviations as in `Source_Sheet.md`.

**Checks run.** A scratch census copy outside the repository, with these fields at the top of the entry, the brief as `longDescription` and the Entry-field changes below, gives 0 errors and the same 4 warnings as the live census (`node tools/validate-census.mjs --skip-quotes <copy>`; the validator checks a tradition's quotations nowhere, so the full quote pass was not run). With a scratch script using the validator's fold rule: each `modern` matches its span in the brief; each `printed` and `englishPrinted` stands at its file and lines, and each file is in `sources`; every quoted span in the card's prose, double or single, stands in a cited file. Quotation marks balance. No audit, review or ruling is named.

## Clearly wrong (card fields)

1. `legacy`, sentence 1.
   - Old: "Marcionite churches faded in the West by roughly the fourth century and lingered considerably longer in Syria and the East, but nothing descends from them."
   - New: "Epiphanius still found Marcionite churches in Rome and Italy late in the fourth century, and they lingered considerably longer in Syria and the East, but nothing descends from them."
   - Evidence: Epiphanius, Panarion 42.1, Epi 7470-7474: the sect is found "even now" (ἔτι καὶ νῦν) in Rome and Italy (Source Sheet S2). Outline Do not say: no source tells their end.
2. `legacy`, the canon sentences (Part 1: a judgment only modern work makes stays off the card; the brief never made it).
   - Old: "Congregations that had never needed to specify which books counted as Scripture discovered that they now had to, and the confession of one God, ..."
   - New: "The confession of one God, ..."
   - Old: " How far he actually caused the New Testament canon rather than accelerated a process already under way is still debated by historians."
   - New: (removed)
   - Evidence: no held old line says it; it is a modern reconstruction and a modern debate stated as content. The outline's What came of it holds no canon claim.
3. `documentedStories[0].text`, Metrodorus.
   - Old: "he records that a presbyter named Metrodorus, ‘who appeared to be a member of the sect of Marcion’, was burned alive in the same city with the presbyter Pionius, in the Decian persecution."
   - New: "he records that Metrodorus, ‘who appears to have been a proselyte of the Marcionitic sect’, was burned alive in the same city with the presbyter Pionius. Eusebius sets this in Polycarp’s time; the Acts of Pionius date it under Decius and call Metrodorus a presbyter of the Marcionites."
   - Evidence: E-en 23677-23681 ("about the same period of time with Polycarp's martyrdom. Among them also Metrodorus, who appears to have been a proselyte of the Marcionitic sect, suffered death by fire"). Eusebius neither says "presbyter" nor "Decian"; the Acts do (Pion 5601-5602, 5655-5658). The old quoted words are not in the print. Source Sheet E4 and section 5.
4. `documentedStories[0].text`, the woman.
   - Old: "and adds: ‘a woman also, who is said to have belonged to the sect of Marcion, is reported to have suffered the same contest.’"
   - New: "and adds: ‘They relate that besides these, in the same persecution and the same city, a certain woman endured a similar conflict. But it is reported that she belonged to the sect of Marcion.’"
   - Evidence: E-en 40472-40474, word for word; the old quoted words are not in the print.
5. `documentedStories[0].text`, the anonymous writer.
   - Old: "was aware that the Marcionites had ‘a great many martyrs of Christ’"
   - New: "was aware that the Marcionites claimed ‘a multitude of martyrs for Christ’"
   - Evidence: E-en 29926-29929: "those called Marcionites ... say that they have a multitude of martyrs for Christ" ("a great many martyrs" is said of "some of the heresies"). Outline beat 2 ("claimed").
6. `documentedStories[0].caveat`.
   - Old: "drawn from lost martyr acts; the qualifier ‘who appeared to be’ and ‘is said to have belonged’ is Eusebius’ own hedge. Nothing further is known of Metrodorus or the woman at Caesarea."
   - New: "drawn from martyr acts, of which the Acts of Pionius survive; the qualifiers ‘appears to have been’ and ‘it is reported’ are Eusebius’ own hedge. The Acts add that Metrodorus was set on the left of Pionius, and that both faced east; nothing further is known of the woman at Caesarea."
   - Evidence: the Acts are held (Pion 5584-5662); the hedges as printed (E-en 23680, 40473); right, left and east, Pion 5602-5604 (outline Leave out: "Card").
7. `documentedStories[0].sources`: the Lieu line removed to `documentedStories[0].modernWorks` (see Entry fields 5); one line added after the first: `{"work": "Martyrdom of Pionius 21", "type": "primary", "note": "Metrodorus, a presbyter of the sect of the Marcionites, on the stake beside Pionius."}` (follows from 3 and 6; Pion 5584, 5601-5602).

## New (card fields)

8. `legacy`: a new last paragraph, from outline What came of it 2 ("Card") and Leave out (Cyprian, "Card"): "Their baptism became a question for other churches. A letter Cyprian of Carthage answered held that those who came from Marcion did not need to be baptized, since they seemed already baptized in the name of Jesus Christ. Cyprian answered that Marcion did not hold the same Father, the Creator, and so his baptism could not give remission of sins." Evidence: ANF5 38505-38552; CypLat 14584-14586.
9. `uncertain` (new), thirteen items, each in its witness's voice:
   - a. The year of the break: outline Do not say ("Any year ... no held old source fixes it"); ANF3 21338-21342 (expelled more than once; the two hundred sesterces).
   - b. Apelles a Marcionite or not, and Philumene: Do not say and Leave out ("Card"); E-en 28967-29068, 29111; ANF3 21358-21369.
   - c. The three opinions and Rhodon's exchange: Cut first 3, Cut first 8 ("old man"), Leave out ("Card"); E-en 29066-29105, 29160-29199.
   - d. Their rites: Leave out, Tertullian I.14 and Epiphanius ("Card", "in his voice"); heart, "a Sabbath fast ... card"; ANF3 23412-23419, Kr 15351-15355; Epi 7687, 7742-7753, 7893-7897.
   - e. The marriage rule, their side: beat 2 ("as Clement reports it ... card"); ANF2 35341-35342 (Stromata III, Latin, "nolentes implere mundum, qui factus est a Creatore, volunt abstinere a nuptiis"); Hippolytus X, ANF5 15388-15392.
   - f. Their prayer: Cut first 1; Ephr 1585.
   - g. Martyrs: Cut first 2 and 5; E-en 29924-29930, 40459-40474; E-gr 9658-9664.
   - h. Metrodorus: Do not say ("Eusebius's hedge goes to the card"), Leave out (right and left, "On a March day": "Card"); Pion 5598-5604, 5646, 5655-5659; E-en 23677-23681.
   - i. Asclepius and Peter: Cut first 10; E-en 47044-47058.
   - j. After the edict: Cut first 4; E-en 66161-66164.
   - k. Chrysostom's charge: Leave out ("Card"); Chrys 24419-24429.
   - l. Theodoret's counts and Cyrrhus's churches: Leave out ("Card"), Cut first 6 and 7; Thdt 31511-31512, 33162-33166, 35164-35166.
   - m. Prepon: Leave out ("Card"); ANF5 12054-12060.
   - Not carried: the Lebaba inscription (Source Sheet S4 and outline Leave out: held only in a modern work's damaged print, off the card's claims). Cut first 9 (the five books) is already on the card in `voices[1]`.
10. `sources` (new): sixteen old works under `about`, each with its file: Gebhardt's Pionius; ANF1; ANF3; Kroymann; Oehler; NPNF 2.1 (E-en); Schwartz (E-gr); Heikel (VC-gr); ANF5; Hartel (CypLat); ANF2 (Clement); Holl (Epi); NPNF 2.7 (Cyr); Mitchell (Ephr); NPNF 1.12 (Chrys); NPNF 2.3 (Thdt). Titles, editors and dates from the file headers and the source sheet's table.
11. `briefReferences` (new): eight lines, one for each paragraph of the brief, each with the lines it draws on. Each was re-read at its lines.
12. `quotationOriginals` (new): one entry for each of the brief's four quoted spans; each `modern` copied from the brief.
    - Rhodon on Apelles: `printed` McGiffert, E-en 29119-29123 (the Greek of Book V is not held; the endnote's λόγον, 29120-29121, named in `uncertain`).
    - Tertullian, Q1: `printed` Kroymann's Latin, Kr 16287-16289, as the scan reads ("statira"); `uncertain` names Oehler's "statim", Oe 4956-4958, which confirms the reading, so the original is printed. `englishPrinted` ANF3 24452-24457 (the editor's note between "redoubled" and "emphasis" set aside). I checked the rendering by hand: *quid non et in persecutionibus* "why, in times of persecution, do you not", *statim* "at once", *oblata acerra* "when the incense box is held out", *animam negatione lucraris* "save your life by denying", *absit, inquis, absit* "'Never,' you say, 'never!'". It leaves out *et* ("also"), as the outline check allows.
    - "one Holy Catholic Church": `printed` Gifford, Cyr 20356-20357 ("And in one Holy Catholic Church"). Four words, so `secondReading` "checked at card". Note: the outline cites Cyr 20348-20359; in the file the passage runs 20349-20362.
    - Theodoret, Q3: `printed` Jackson, Thdt 31511-31512 (the Greek is not held).
    - No `secondReading` is set for the three spans of six words or more.

## Entry fields (for release)

1. `why`.
   - Old: "The Roman church expelled him and gave back his money, by tradition in 144."
   - New: "The Roman church expelled him and gave back his money."
   - Evidence: outline Do not say, "Any year for Marcion's break with Rome (144 or another) → no held old source fixes it"; the brief says "in the middle of the second century" and no longer makes the claim (the approved brief did). The rest of `why` is held: Sinope (Epi 7476-7477), the shipmaster and the money that went with him (ANF3 21331-21342), the two Gods and the cut Luke and ten letters (ANF1 33577-33591).
2. `teaser`.
   - Old: "c. 140 into the 300s CE"
   - New: "the mid-second century into the fifth"
   - Evidence: the brief, "in the middle of the second century", "For about three hundred years", and Theodoret's villages "In the fifth century" (Thdt 31501, 31511; Setting, Widely Accepted). No held source gives 140.
3. `relationsSummary`.
   - Old: "Second-century rival the proto-orthodox defined themselves against"
   - New: "Rival church, from the second century to the fifth, that the mainstream church drew its line against"
   - Evidence: the brief carries the rivalry to Theodoret; outline What came of it 1 ("The mainstream church drew its line against them"). "Proto-orthodox" is a modern label (Part 1).
4. `dates`: "c. 140-300s" → "2nd-5th c." (the census form for century spans). Evidence as 2. **`start` 140 and `end` 300: not changed, flagged for Mark.** No held source gives either year; 300 is contradicted by Cyril, Ephrem and Theodoret. The axis needs a year.
5. `modernWorks` (new on the entry), from outline Who tells it, Modern ("clarify"): McGiffert's notes (1890); Holl (1922, J. C. Hinrichs, Leipzig); Kroymann (1906, F. Tempsky, Vienna); Oehler (1853, T. O. Weigel, Leipzig); Gebhardt (1902, Alexander Duncker, Berlin); Gifford (1894); Jackson (1892); Mitchell, Bevan and Burkitt (1912-1921, Williams and Norgate). Each note says what the work covers. All are prints before 1931, held in `cic/texts/`. On `documentedStories[0].modernWorks`: the Lieu line moved from that story's `sources`, `{"title": "Marcion and the Making of a Heretic", "author": "Judith Lieu", "year": "2015", "publisher": "Cambridge", "note": "On Marcionite communities and martyrs."}`. Title, author, year and publisher are from the old line; its note dropped "The standard modern study;", a judgment Part 1 keeps off a note. Not held; listed only as further reading.

## Flagged, not changed

- `documentedStories[0].verification` still reads "from reference summaries; primary text not yet read", though its three Eusebius notices are now read and corrected above. Left for release.
- `teaser`: "across the empire", while Epiphanius's list reaches Persia (Epi 7472-7473). Not clearly wrong.

## Not found (left in place)

- `voices[0]`: "with its own bishops" (outline Do not say: the only held Marcionite bishop is Asclepius, "supposed to be" one; Tertullian's "has its churches", ANF3 29323-29330, names no bishops).
- `why`: "wealthy"; "stripped of what he judged to be Jewish corruption" (not re-read; its source in Against Marcion IV.4 is a barred quote).
- `legacy`: "lingered considerably longer in Syria and the East" (held for Syria and Edessa only: Thdt 31511, Ephr 1585); "hammered into its sharpest early form in argument against him" (a judgment).
- `documentedStories[0].text`: three men "executed ... for provoking the judge by their confession" (E-en 40459-40472: they "went before the judge and met the end"); "women who confessed before a governor"; "the two sides refused each other communion to the end" (V.16.22 says it of the Montanists' martyrs); the closing sentence on the historians' credit (a judgment).
