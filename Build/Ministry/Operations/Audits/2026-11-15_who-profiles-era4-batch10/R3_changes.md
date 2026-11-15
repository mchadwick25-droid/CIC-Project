# Round 3 changes: era 4 Who batch 10

Applied as worded under Mark's cap ruling of 2026-11-15, his pick "Fix + one check (Recommended)": the one blocking point (Part C R3-B1, Harasiewicz's 1031 election and 1063 successor on Ilarion's card, records and README) and all 26 minor points, by three fresh Opus agents. Where an old string had already changed under a parallel edit, the replacement was applied to the current text with the least change, as each part notes. One targeted check of only these strings follows (R4_cap-check.md).

---

## R3 changes, Part A

All seven minor points applied as worded. No old string had drifted; each matched exactly once. Batch folder = Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch10/.

## R3-M1: applied as worded
- README.md l.32 (Theophanes, "Who the sources are"): "whose author and date are open." → "whose author and date are disputed."

## R3-M2: applied as worded
- stephen-the-younger.brief.txt para 5, and audio/stephen-the-younger.audio.txt same sentence: "Stephen was held in the Praetorium prison." → "Stephen was jailed for trial in the Praetorium."
- stephen-the-younger.brief.txt para 1, and audio/stephen-the-younger.audio.txt same sentence: "Certainly, said those standing by." → "Certainly, said the bystanders."
- Result: 333 words, FK 7.258, Flesch 66.537. Audio equals brief plus "[calmly] " / "[warmly] " (checked by diff).

## R3-M3: applied as worded
- README.md l.23: "The story "Stephen the Younger Dragged Through the Mese" (marked "primary text not yet read") differs too." → same + " Its `when` and text give 28 November 765, the text as the Life's account."
- Open-Gaps.md entry 272, first sub-bullet: "Stephen: Iconophile Byzantine Monasticism's `why`, `longDescription` and `voices[1]` say he was killed in 765, the first two "his Life says"." → "Stephen: Iconophile Byzantine Monasticism's `why`, `longDescription` and `voices[1]`, and the `when` and text of its story "Stephen the Younger Dragged Through the Mese", say he was killed in 765; `why`, `longDescription` and the story's text give it to the Life."
- Open-Gaps.md same sub-bullet: "the crowd (l.96917-96955) and the coin," → "the crowd (l.96917-96955), the Life's date (its caveat's "c. 809", where Fabricius gives 808, PG100 l.88570) and the coin,"

## R3-M4: applied as worded
- theophanes-the-confessor.card.json `dates`: "Born about 751 or 752 by Jacques Goar's reckoning from the winter of the ice, which Goar says Theophanes's own figures would put about 744." → "Born about 751 or 752 by Jacques Goar's reckoning from the winter of the ice; about 744, Goar says, by Theophanes's own figures."

## R3-M5: applied as worded
- records.json, nikephoros-of-constantinople, claim "Theophanes the priest is another and younger man than Theophanes the Confessor (Bollandists)", `witness`: "PG100 l.1629-1648" → "PG100 l.1629-1648, l.1656 (the scan carries the clause into the next column)". (Load-modify-write, 1-space indent; git diff shows only this line.)

## R3-M6: applied as worded
- README.md l.54: "The brief says "Patriarch Nikephoros" first" → "The brief says "Patriarch Nikephoros of Constantinople" first"
- Decision-Log.md batch entry, "Names and ids" bullet (l.3560): "The brief names "Patriarch Nikephoros" apart from the emperor Nikephoros I" → "The brief names "Patriarch Nikephoros of Constantinople" apart from the emperor Nikephoros I"

## R3-M7: applied as worded
- README.md l.13: "By the census's own Who rows, Greek East & Orthodoxy era 4 holds eight majors after batch 9; counted by era 4 card traditions, it holds nine." → "By the census's own Who rows, Greek East & Orthodoxy era 4 holds five majors in release 44 (Maximus, Martin I, Photius, Athanasios, Symeon), and batch 9's three make eight; counted by era 4 card traditions, it holds nine, with Humbert."

Part A had no blocking point (R3-B1 is in another part).

---

## Round 3 changes, Part B (Nicholas Mystikos, Peter of Sicily, Michael Keroularios)

Base: d69359ea. Part B had no blocking point (0 blocking, 10 minor). Paths relative to Build/Ministry/Features/Church-Family-Tree/.

## R3-M1 — applied as worded
- Who-Profiles/era4/batch10/nicholas-mystikos.brief.txt, last paragraph, and audio/nicholas-mystikos.audio.txt (same sentence):
  "Once, on his knees, he had told Leo that a king is called an unwritten law, whose deeds should match the written law." → "Once, he writes, he had told Leo on his knees that a king is called an unwritten law, whose deeds should match the written law."

## R3-M2 — applied as worded
- Who-Profiles/era4/batch10/records.json, nicholas-mystikos.contested_claims["When the legates arrived"].sides[0]:
  "Nicholas: eight or nine months after the wedding, before his arrest (PG111 l.14277-14279)" → "Nicholas: eight or nine months after the wedding, before his arrest (PG111 l.14275-14277; the arrest follows at l.14390-14402)"
- Not changed (not named by the review): the claims record "Legates' arrival: ..." still cites "PG111, Letter 32, l.14277-14279" (records.json, nicholas-mystikos claims). Flag for the checker.

## R3-M3 — applied as worded
- peter-of-sicily.brief.txt, paragraph 5, and audio/peter-of-sicily.audio.txt:
  "Gieseler says Peter is wrong to call them Manichaeans." → "Gieseler says Peter is wrong to hold that they are really Manichaeans."

## R3-M4 — applied as worded
- michael-keroularios.brief.txt, paragraph 5, and audio/michael-keroularios.audio.txt:
  "They walked into the palace with a cross and staffs, he writes, and would not greet him or bow." → "They walked into the palace with a cross and staffs, Michael writes, and would not greet him or bow."

## R3-M5 — applied as worded
- Who-Profiles/era4/batch10/README.md, "Live census mentions", Nicholas bullet: inserted before "The rest agrees.":
  "It also has the dispensation come before the deposition. Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277); in the Life, as de Boor reads it, they had not yet come on the day of his exile, and de Boor prefers the Life (DEBOOR l.8546-8561, l.8599-8611)."

## R3-M6 — applied as worded
- README.md, "Live census mentions", Keroularios bullet:
  'A link note says he kept the post "until 1058"; Will gives 1059 (l.4053).' → 'A link note says he kept the post "until 1058", which is Blackmore's year (MOUR l.16005-16006); Will gives 1059 (l.4053).'

## R3-M7 — applied as worded
- README.md, "Corrections to the re-score", Nicholas bullet:
  "The row lists no disputed dates; the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all in dispute." → "The row gives the exile as 907, which is de Boor's; Krug and Muralt give 908, and Mai nine years after the election, or eleven by Leunclavius (DEBOOR l.5798-5800; PG111 l.662-664). It lists no other dates, though the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all in dispute."

## R3-M8 — applied as worded (two replacements)
- Decision-Log.md, "Who profiles, era 4 batch 10", "Contested points told in place":
  "Nicholas's fall is 907 for de Boor and 908 for Krug and Muralt, and whether eastern legates came is told with de Boor and his doubters." → "Nicholas's brief leaves the year of his fall untold; his card gives de Boor's 907, Krug and Muralt's 908, and Mai's nine years after the election, or eleven by Leunclavius. Whether eastern legates came is told with de Boor in the brief and with his doubters on the card."
  "Keroularios's death is told three ways" → "Keroularios's death is told two ways in his brief and three on his card"

## R3-M9 — applied as worded
- Decision-Log.md, same entry, round 2 list:
  'The tightening put back Nicholas's disputed year 907 with one placing. It also left "the same" with no referent in Peter's brief, on the profile's main contested point.' → 'Nicholas's brief still gave his disputed year 907 with one placing; round 1 had taken it off his card only. The tightening left "the same" with no referent in Peter's brief, on the profile's main contested point.'

## R3-M10 — Peter and re-score applied as worded; Nicholas applied with change
- Open-Gaps.md 272, Peter/Ilarion/Keroularios census bullet:
  'the link `paulicians--bogomils` has "around 870", and Gieseler dates the embassy to 868 (PETER l.154).' → 'the link `paulicians--bogomils` has "around 870", as Rader and Gifford give (PETER l.599; NPNF7 l.9962-9963), where Gieseler dates the embassy to 868 (PETER l.154).'
- Open-Gaps.md 272, Stephen/Nicholas census bullet (with change): another part had already added, before "Owner: the coordinator", the sentence 'Its "accepting Constantine VII's legitimacy" is not in the account before the Tomus of Union, in the lines read.' That covers the review's first inserted sentence, so I kept it and did not add a duplicate. Inserted after it, before "Owner: the coordinator", only the second half as worded:
  "The story puts the dispensation before the deposition; Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277), and the Life, as de Boor reads it, after his exile (DEBOOR l.8546-8561)."
- Open-Gaps.md 272, re-score corrections bullet, Nicholas:
  "the row lists no disputed dates, but the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all disputed." → "the row's exile of 907 is de Boor's, against Krug and Muralt's 908 and Mai's nine years after the election (DEBOOR l.5798-5800; PG111 l.662-664); the election (895 or 901), the return (911 or 912) and the death (924 or 925) are also disputed."

## Checks
- Audio equals brief with "[calmly] " first and "[warmly] " before the last paragraph: true for all three.
- Words / grade_text: Nicholas 330, FK 7.20, FRE 68.74; Peter 333, FK 7.17, FRE 65.38; Keroularios 329, FK 6.87, FRE 68.95. README's "328 to 333" holds.
- records.json valid JSON, 1-space indent, final newline; only the one Nicholas string changed. Cards untouched. I committed nothing; the coordinator's commits ff654de8 and 48d19886 already carry these edits.

---

## R3 changes, Part C (ilarion-of-kyiv, README, close-out records)

Paths relative to Build/Ministry/Features/Church-Family-Tree/. B = Who-Profiles/era4/batch10/. Brief and audio of Ilarion not changed (review: no change needed).
Note: a parallel agent's commit ff654de8 ("round 3 fixes in progress") picked up my card and records edits mid-run; they are in HEAD, the README/Decision-Log/Open-Gaps edits below are in the working tree.

## R3-B1 — applied as worded
Source lines rechecked: HARAS l.1-4, l.1671-1673, l.1748-1749; CROSS l.11741-11742; PSRL1 l.6896-6897; GORSKII l.181, l.3995. All match.
1. B/ilarion-of-kyiv.card.json `dates`: after "...by the Russian Primary Chronicle and his own confession of faith." inserted " Michael Harasiewicz's Annales Ecclesiae Ruthenae (1862) gives 1031 for the election, as the scan reads twice, and dates the next metropolitan, George I, to 1063."
2. Card `uncertain[6]`: after "...Mouravieff says George was sent early in the reign of Izyaslav, Yaroslav's son." inserted " Michael Harasiewicz's list of the Kyiv metropolitans (1862) puts George I in 1063."
3. Card `sources.about`: appended {"title": "Annales Ecclesiae Ruthenae", "author": "Michael Harasiewicz, archpriest of the Ruthenian metropolitan chapter of Lviv", "date": "1862", "language": "Latin", "file": "cic/texts/harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt"} (last item).
4. B/records.json, ilarion-of-kyiv `claims`: appended the reviewer's HARAS claim verbatim (last item; formation_confidence "Contested").
5. records `contested_claims`: appended "The year he was made metropolitan" with the reviewer's three sides verbatim (last item).
6. records `absent_details`, "Year of his death or end of office", note: "Searched all cic/texts for Hilarion, Ilarion, Иларион, Ларион, Ларіон and OCR variants." → same + " Harasiewicz (1862) gives no end for him and lists George I under 1063 (HARAS l.1749)."
7. B/README.md, "Who the sources are", Ilarion: "l.4485-4489). Nothing held gives his birth" → "l.4485-4489). Michael Harasiewicz's Annales Ecclesiae Ruthenae (1862) gives 1031 for the election and 1063 for George I (l.1672, l.1749). Nothing held gives his birth"

## R3-M1 — applied with change (old string already altered by a parallel edit)
8. B/README.md l.13: the current text read "This batch adds no majors, so the counts in the batch 9 README stand. By the census's own Who rows, Greek East & Orthodoxy era 4 holds five majors in release 44 (Maximus, Martin I, Photius, Athanasios, Symeon), and batch 9's three make eight; counted by era 4 card traditions, it holds nine, with Humbert." (not the reviewer's old string). Replaced that whole span with the reviewer's text as worded: "This batch adds no majors. Release 44's flags mark the same five Greek East & Orthodoxy era 4 Who rows that batch 9 counted: Martin I, Maximus, Photius, Athanasios and Symeon. With batch 9's three, the census's own Who rows give eight. Counted by era 4 card traditions, Humbert's Macedonian-era card makes nine; Antony and Theodosius sit in era 5, as batch 9 sets out."
9. Decision-Log.md, batch entry "No majors" bullet: "The river counts in the batch 9 README stand." → "Release 44 flags the same five Greek East era 4 rows that batch 9 counted, so the river counts in the batch 9 README stand: eight by the census's Who rows, nine by era 4 card traditions."

## R3-M2 — applied as worded
10. README l.20: "Each difference below will be logged in Open-Gaps, in an entry "Era 4 Who batch 10", for the census fix." → "Each difference below is logged in Open-Gaps, "Era 4 Who batch 10" (2026-11-15), for the census fix."

## R3-M3 — applied as worded
11. README Stephen bullet: "and the PG108 editors 767." → "and the PG108 editors 28 November 767 (THEO l.131105-131109)."

## R3-M4 — applied as worded, optional README part taken
12. Card `uncertain[3]`: "from the patriarch Michael Cerularius" → "from the patriarch Michael Keroularios"
13. Card `uncertain[3]`: "from Michael Cerularius, whom he calls the leader of the schism" → "from Michael Keroularios, whom he calls the leader of the schism"
14. README Ilarion sources line: "consecration from Michael Cerularius (SUSZA1666" → "consecration from Michael Keroularios (SUSZA1666"
(records.json contested_claims still says "Michael Cerularius" in Mouravieff's and Smotrytsky's sides; those are witness summaries in the sources' own form and the review did not name them, so left.)

## R3-M5 — applied as worded, optional Open-Gaps part taken
15. records `absent_details`: appended {"detail": "A Polish pamphlet on the consecration", "note": "Arkhiv Iugo-Zapadnoi Rossii I.7 (1887), p. 384, gives the war with the Greeks as the reason, citing the Caves Paterik and Zonaras; its scan prints the Polish in Cyrillic letters (l.16547-16552), so it is not used. The index points to it (l.32507-32511)."} (lines rechecked).
16. Open-Gaps.md 272, Library line: "the Life of Antony that Simon of Vladimir cites;" → "the Life of Antony that Simon of Vladimir cites; a readable scan of the Polish pamphlets in Arkhiv Iugo-Zapadnoi Rossii I.7 (p. 384, on Ilarion's consecration);"

## R3-M6 — applied as worded (the Stephen sub-bullet had been edited elsewhere by a parallel part; the old sentence was still intact)
17. Open-Gaps 272, Stephen: "Fabricius 766 (PG100 l.88570-88571), and Theophanes 20 November under Goar's 757 (PG108 l.78706-78707)." → "Fabricius 766 (PG100 l.88570-88571), the Short History's marker 766 (PG100 l.81476), Theophanes 20 November under Goar's 757 (PG108 l.78706-78707), and the PG108 editors 28 November 767 (PG108 l.131105-131109)."

## R3-M7 — applied as worded
18. Open-Gaps 272, Nicholas: after "and 921 in de Boor (DEBOOR l.4693-4694)." added " Its "accepting Constantine VII's legitimacy" is not in the account before the Tomus of Union, in the lines read."

## R3-M8 — applied as worded
19. Open-Gaps: one empty line inserted before "272." (after 271's last sub-bullet).

## R3-M9 — applied as worded (first part); second part left to the worker per instructions
20. Decision-Log batch entry: "This batch's pull request waits for data release 44 (PR #1669)." → "This batch's pull request waited for data release 44 (PR #1669), which is now merged into this branch."
"**Round 3.**" placeholder and "Approved to proceed" line not touched; the worker should name Mark's cap ruling in the Round 3 line.

## Noticed, not changed
- Card `dates` ends "...in its entry for 1072" with no final period (pre-existing).
