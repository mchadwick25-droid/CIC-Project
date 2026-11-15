# R4 cap check: era 4 batch 10

A fresh Opus agent did this check at full effort. It had not seen the drafting or the earlier rounds. This is the one targeted check under Mark's cap ruling of 2026-11-15, "Fix + one check (Recommended)", and it does not count toward the cap. It covers only the strings changed by round 3's fixes (R3-B1 and the 26 minor points) in the batch's briefs, audio scripts, cards, `records.json` and README, and in the Decision-Log batch entry and Open-Gaps 272. The diff read is d69359ea ("Era 4 batch 10: round 3 review (1 blocking, 26 minor)") to b09c5b90, limited to `Build/Ministry/Features/Church-Family-Tree/`. The Decision-Log's "**Round 3.**" placeholder and the batch entry's closing "Approved to proceed" line are left to the worker and not checked. No repo file was edited except this one. No paid calls were made.

**Verdict: NOT CLEAR. 0 blocking, 7 minor (R4-M1 to R4-M7).** Every round 3 fix is in the files as R3_review.md words it, or as R3_changes.md says it was adapted. No fix adds a wrong fact, a misquote or a writing failure to a brief. Two of the reviewers' own line ranges were wrong, and the fixes carried them into new strings (R4-M1, R4-M2). R3-B1 put Harasiewicz's 1031 on the card's `dates` and in the records as a contested year. Three places still tell 1051 with no witness named: the card's `knownFor`, Open-Gaps 272, and the Decision-Log's list of contested points (R4-M3 to R4-M5). The other two points are witness lines (R4-M6, R4-M7).

## What was checked

- **Harasiewicz, in context.** HARAS l.1671-1673: "erat celeberrimum illud Criptarum (Peezar) subterranearum / Kijoviae, cui initia dedit Hilarion, electus anno 1031 in / Metropolitam". L.1747-1749 head the series "Series Metropolitarum Kijoviensium hocce tempore est sequens" and read "3. Theopemptus (1023). 4. Hilarion (1031). 5. Georgius I (1063). 6. Joannes I (1072)." "Hilarion" occurs only at l.1672, l.1749 and l.12008 (a later archimandrite of Supraśl). The card's "as the scan reads twice", "the next metropolitan, George I, to 1063" and the records' quotation (l.1672-1673, l.1748-1749) are right. So are the source entry (header l.1-4: "Archpriest and Provost of the Ruthenian Metropolitan Chapter of Lviv", 1862) and the `absent_details` addition.
- **1051 beside it.** CROSS l.11741-11742 "6559 (1051). Yaroslav ... appointed Hilarion Metropolitan of Rus"; PSRL1 l.6896-6897, as the scan reads, "[6559 (1051)] Поетави Мрославъ Лариіѵна митрополитомъ . / Русина"; GORSKII l.181 and l.3995 give 6559 (1051). The card's `dates` names both witnesses, then Harasiewicz. `uncertain[6]` adds 1063 next to the foreword's 1079 (GORSKII l.824-827), Cross's 1072 (CROSS l.12488-12491) and Mouravieff's "early in the reign of Isyaslaff" (MOUR l.1691-1693). The brief needs no change, and none was made. It gives 1051 as the Chronicle's ("In 1051, the Chronicle says") and as his own signed date. The README's new sources sentence names Harasiewicz and both years.
- **Other source lines reopened.** THEOPH l.333 (744, 751 or 752); PG100 l.1647, l.1656 ("Aljus ergo hic noster Theo-" ... "phanes est et aliquanto junior"); PG100 l.81476, l.88568-88569, l.95739-95742, l.95723; PG108 l.78706-78707; PG111 l.662-664, l.14028-14029, l.14093-14097, l.14390-14402; DEBOOR l.5798-5800, l.8544-8561, l.8599-8612; PETER l.154, l.599, l.3878-3881; NPNF7 l.9961-9963; WILL l.17228-17232; MOUR l.16004-16006; Arkhiv I.7 l.16547-16552, l.32505-32511. The release 44 census: five Greek East & Orthodoxy era 4 rows marked major (Maximus, Martin I, Photius, Athanasios, Symeon), and the Mese story's `when` "28 November 765" and caveat "c. 809". All match, except as found below.
- **JSON.** All seven cards and `records.json` parse.
- **Audio.** For all seven, each script equals its brief with `[calmly] ` before the first paragraph and `[warmly] ` before the last.
- **Scores.** By `grade_text`: Stephen 333 words, FK 7.26, Flesch 66.54; Nicholas 330, FK 7.20, Flesch 68.74; Peter 333, FK 7.17, Flesch 65.38; Keroularios 329, FK 6.87, Flesch 68.95. No changed sentence runs past 25 words. Nicholas's new closing sentence is exactly 25, and its "he" is Nicholas.
- **Changes not listed in R3_changes.md, judged.** README l.11 and the Decision-Log "Length" bullet now say "329 to 333". That is right: Nicholas went from 328 to 330, so Ilarion and Keroularios, at 329, are now the shortest. Part C's R3-M1 text replaced Part A's R3-M7 text in README l.13. The result keeps the five rows R3-M7 named and adds Humbert and the era 5 note. That is right.

## Findings

### R4-M1 (Nicholas: the R3-M2 range is two lines early, and two later fixes copied it)

- Text, in three places:
  - `records.json`, `contested_claims` "When the legates arrived", Nicholas's side: "(PG111 l.14275-14277; the arrest follows at l.14390-14402)"
  - README "Live census mentions", Nicholas (from R3-M5): "Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277);"
  - Open-Gaps 272 (from R3-M10): "Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277), and the Life"
- Source: in the file, l.14275-14276 are blank, l.14277 reads "Octavo vel nono mense post initas illas nuptias", l.14278 reads "quæ universam Ecclesiam nostram mœrore aſſecer.,", and l.14279 reads "veteris Romæ legati advenerunt". The old witness, l.14277-14279, was right. The new range takes in two blank lines and drops "legati advenerunt". Under "no fix on a fix", the old range goes back in. The records claim "Legates' arrival", which R3_changes flagged, still cites l.14277-14279 and is right.
- Replacements:
  - records: "(PG111 l.14277-14279; the arrest follows at l.14390-14402)"
  - README: "Nicholas has Rome's legates arrive before his arrest (PG111 l.14277-14279);"
  - Open-Gaps 272: "Nicholas has Rome's legates arrive before his arrest (PG111 l.14277-14279), and the Life"

### R4-M2 (Stephen: the PG108 editors' 28 November 767 is not at l.131105-131109)

- Text, in three places:
  - README "Live census mentions", Stephen (from Part C's R3-M3): "and the PG108 editors 28 November 767 (THEO l.131105-131109)."
  - Open-Gaps 272 (from R3-M6): "and the PG108 editors 28 November 767 (PG108 l.131105-131109)."
  - `records.json`, Stephen, `contested_claims` "The date of his death", the range both fixes copied: "Patrologia Graeca editors of Theophanes: 28 November 767 (THEO l.131105-131109)"
- Source: l.131105-131109 hold only "etus, mox in Proconnes um exsul mi" and "sub finem, idem sanetus ab exsilio redux;" with blank lines and a colon. The date is at l.131112-131114: "torii. Anno demum 767, tatis sus iin (non vero / post annos Lx in clausura exactos, ut seribit Theo- / phanes), die xxvi1r Novembris, martyrii palmam". The sibling side in the same record (THEO l.131106-131115) covers it.
- Replacements:
  - README: "and the PG108 editors 28 November 767 (THEO l.131112-131114)."
  - Open-Gaps 272: "and the PG108 editors 28 November 767 (PG108 l.131112-131114)."
  - records: "Patrologia Graeca editors of Theophanes: 28 November 767 (THEO l.131112-131114)"

### R4-M3 (Ilarion card `knownFor`: 1051 told as the narrator's fact, beside a contested year)

- Text: "In 1051 Prince Yaroslav of Kyiv gathered the bishops and made him metropolitan of Rus."
- After R3-B1, the records hold "The year he was made metropolitan" as a contested claim, and the card's `dates` gives Harasiewicz's 1031. `knownFor` is the card's headline, and it names no witness. The brief tells the same sentence as the Chronicle's. The evidence runs heavily to 1051: the Chronicle (CROSS l.11741-11742; PSRL1 l.6896-6897) and his own signed confession (GORSKII l.2610, l.3995). Harasiewicz's list is loose elsewhere. So this is minor, but the rule (Who_Profile_Pattern checklist 7) is that a contested claim is never told as settled.
- Replacement: "In 1051, the Russian Primary Chronicle says, Prince Yaroslav of Kyiv gathered the bishops and made him metropolitan of Rus."

### R4-M4 (Open-Gaps 272, Ilarion: the same 1051 is told flat in the bullet round 3 edited)

- Text: "He was made metropolitan in 1051 (CROSS l.11741-11742; GORSKII l.3995)."
- The census fixer reads this line against the census's "c. 1049". The README's census bullet (l.27) already says "the Chronicle and his confession make him metropolitan in 1051". The Open-Gaps entry should say the same and name the held dissent.
- Replacement: "The Chronicle and his confession make him metropolitan in 1051 (CROSS l.11741-11742; GORSKII l.3995); Harasiewicz gives 1031 (HARAS l.1672, l.1749)."

### R4-M5 (Decision-Log batch entry, "Contested points told in place": the new contested year is missing)

- Text: "Who made Ilarion a monk, and why he was consecrated in Kyiv, are given to each witness."
- R3-B1 added "The year he was made metropolitan" to the records as a contested claim and gave it on the card. Round 3 rewrote this bullet (R3-M8) but did not add it.
- Replacement: "Who made Ilarion a monk, and why he was consecrated in Kyiv, are given to each witness. His brief gives 1051 as the Chronicle's, and his card adds Harasiewicz's 1031."

### R4-M6 (Ilarion records, the new contested side: "His confession" cites the foreword and the translation, not the confession)

- Text: "His confession: 6559 (1051) (GORSKII l.181, l.3995)"
- Source: l.181 is the 1844 foreword quoting the confession (the scan reads "си в5 лъто «фи (1051)"). L.3995 is the Russian translation ("Было же се въ лёто 6559 (1051)"). The confession's own Slavonic line is l.2610, "телю. Быша же си въ лёто язфню, Владычествующу", where the scan garbles the year. The side should name the confession's own line.
- Replacement: "His confession: 6559 (1051) (GORSKII l.2610, where the scan garbles the year; the foreword's quotation, l.181; the translation, l.3995)"

### R4-M7 (Keroularios: Blackmore's "sat till 1058" is at MOUR l.16005, and Open-Gaps 272 cites l.16006)

- Text: Open-Gaps 272, in the bullet R3-M10 edited: "A link note has him in office "until 1058", which is Blackmore's year (MOUR l.16006);". README l.74, "Language and quotations", has the same line for the quotation: "Blackmore's "sat till 1058" (MOUR l.16006)".
- Source: MOUR l.16005, "in 1043. His successor was Michael Cerularius, who sat till 1058, and in". L.16006 begins "whose time the schism". R3-M6's new README string cites l.16005-16006 for the same words, so the three citations now disagree. Both old citations predate round 3, but they sit beside text that round 3 changed.
- Replacements:
  - Open-Gaps 272: "which is Blackmore's year (MOUR l.16005);"
  - README l.74: "Blackmore's "sat till 1058" (MOUR l.16005)"

## Noticed, not raised

- README l.67, "His active year for the release worker is 1051, when he was made metropolitan". This is unchanged by round 3. As an active-year rule it is right under either year's evidence. The worker may add "by the Chronicle and his confession" if R4-M3 and R4-M4 are taken.
- Card `dates` ends "...in its entry for 1072" with no final period (R3_changes already notes it; pre-existing).

**Counts: 0 blocking, 7 minor (R4-M1 to R4-M7).**
