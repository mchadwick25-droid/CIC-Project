Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: Opus Round 1 reviewer, Anabaptists (independent subagent; wrote none of the text under review)
Drafter agent: a308a6756db757d95 (Sonnet)
Round: 1
Truncation check, method 1: structural count. `wc -l -c` gives Doc_02 389 lines / 70,986 bytes, Registry 168 / 107,000, gap ledger 154 / 15,289. Doc_02 has eleven `##` headings, §1 to §11 in order, the last "## 11. Disposition" with its closing sentence. The Registry has 99 table rows numbered 1 to 99 with no gap or duplicate, every row with exactly 16 pipes, followed by the files table and the saturation statement. The ledger runs OG-1 to OG-17.
Truncation check, method 2: tail read and byte check. Each of the three files ends on a complete sentence followed by a newline (`tail -c1 | od -c` gives `\n`): Doc_02 ends "...note the new floor evidence (OG-10).", the Registry ends "...none relevant, and was dropped.", the ledger ends "...Doc_03 must read what it uses." SHA-256 prefixes at review time: Doc_02 48446021a65126e1, Registry da2a5729082fafa6, ledger acae82f1862dfe7d.

# Review of Doc_02_Source_Ecology.md and Source_Registry.md (The Anabaptist Movements, VI.3)

**Date:** 2026-10-23. **Files reviewed:** `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md` in `Build/World-Builds/Anabaptist-Movements/`. **Read for context:** `Step0_Movement_Scope_Confirmation.md`, `Doc_01_World_Identification_Boundaries_Orientation.md` (both Approved to proceed), the Source Readiness Dossier, the corpus map, the Construction Framework V7.4 Step 2 text, the Source Registry Template, the Record-Native Build Process V2.0 §4, and the `jes` Doc_02 exemplar.

## Verdict

**Substantial revision required.** 8 BLOCKING, 10 COSMETIC.

The two documents are strong work. Quotation fidelity is very high. A script normalised whitespace, line-break hyphens and long s, and checked every quotation that carries a line locus against the 25 vendored files: 94 of 94 in Doc_02 and 131 of 134 in the Registry were found at the cited lines. The three misses are title labels (finding C5). I then read 41 passages by eye at their loci (listed under "Spot-checks" below). The corpus figures reproduce exactly. The Registry counts in its header reproduce exactly. The forces lens is substantive. The Article 4 check is careful and states each result at its own strength. The two claims the brief asked me to test both hold (see "The two claims tested").

The blocking findings are not about invented material. They are misreadings of a source (William of Orange's son), one missed body of own-voice text (Riedemann's letters in the Chronicle), one overstated witness count (Sattler's date), a wrong locus, a confidence level that no witness supports, two false verification notes, one wrong description of a vendored witness, and the reviewer-side recall and PRESS results, which the Registry must now disposition.

## The two claims tested

**1. McGlothlin's file does not print the Dordrecht Confession. Confirmed.** `mcglothlin_baptist-confessions-of-faith_1911.txt` lines 2628 to 2644 describe the confession of Dort, 21 April 1632 ("drawn up in eighteen articles at a peace convention held in Dort"), say it "is found in Van Braght's 'Martyrs' Mirror,' pp. 36-42", and close: "These later Mennonite Confessions had no direct influence on Baptist Confessions and, therefore, are not reproduced." "Dort" occurs on one line only (2630). Phrases from the Confession ("worthy evangelists", "Pontius", "shunning", "eighteen articles" outside 2629) do not occur. Registry row 21, row 74, Doc_02 §7 item 13 and OG-5 are right, and the dossier's "three times" is two.

**2. Böhmer shows that Schleitheim was printed. Confirmed.** `boehmer_urkunden-bauernkrieg-wiedertaeufer-deu_1910.txt` lines 1760 to 1770: "Inzwischen war A samt einem sendbriefe Sattlers an die gemeinde Gottes zu Horb am Neckar und einem berichte über Sattlers martyrium ... in deutscher spräche im drucke erschienen. Zwei dieser drucke sind auf uns gekommen: A 1, vorlianden in zwei exemplaren in München Staatsbibliothek ... ohne Jahreszahl und druckort; A 2, vorhanden in Berlin kgl. Bibl. und bei antiquar Haupt in Leipzig". A French printing is reported lost (line 1747). McGlothlin's "So far as known, they were never printed" (lines 490–491) is therefore wrong on Böhmer's evidence. One nuance the drafter may add: Böhmer reports that in July 1527 Zwingli believed the Täufer had not let the articles be printed (lines 1727–1729, "da die täufer selbst ... sie nicht drucken ließen"), which is likely the root of McGlothlin's statement. The Wolkan Chronicle's footnote to the Sattler entry names a further 1527 German print of the Sattler account in Berlin ("Ayn newes wunderbarlichs geschicht von Michel Sattler", lines 5850–5852). This is advisory, not a finding.

## Findings

### BLOCKING

**B1. William of Orange's son restored the toleration. He did not end it.** Doc_02 §6 ("The magistrates and lords who tolerated them"), §8 (row "William of Orange ordered the magistrate of Middelburg ... and his son ended that toleration", rated *Documented*), and the Registry row 19 use.
- *Locus checked:* `van-braght_martyrs-mirror_sohm1886.txt` lines 148227–148240, the Remark. It reads: "the true fruit did still not follow, notwithstanding it was obeyed for a few years immediately afterwards; for after the decease of that good prince they began again; however, to the salvation of the defenseless church of God, it was terminated by a third prohibition, by his son". What "was terminated" is the renewed oppression, "to the salvation of the ... church". Lines 152743–152760 confirm it: "Maurice, the oldest son of the aforesaid prince ... following the footsteps of his father, issued, for the third time, a prohibition concerning the oppressing of the aforesaid people, to the end that they might now certainly obtain liberty of conscience", and Maurice's act follows.
- *Also wrong:* "William of Orange speaks once". The *Mirror* prints a first act, "LETTER OF PRIVILEGE GRANTED BY WILLIAM I, TO THE ANABAPTISTS AT MIDDELBORGH" (from line 147918, dated at Middelburg on 26 January [1577], line 148004), as well as the 1578 charge.
- *Consistency:* Doc_01 §2 and §5 say the Middelburg toleration was "restored after a lapse by his son". Doc_02 contradicts Doc_01 without saying so, and Doc_01 is the one that is right.
- *Fix:* correct §6, the §8 row and the forces-lens bullet for Cell 2A. Name both of William's acts (1577, 1578) and Maurice's act, with loci. Add Maurice's act to row 19's loci or give it a row of its own.

**B2. Riedemann's own letters are on the shelf, in the clean Chronicle scan.** Doc_02 §2 (Peter Riedemann: "named 37 times in five files ... his own book is unreadable"), §7 item 2 ("Riedemann, Marpeck, Denck and Grebel have no readable words. The world's argument must not rest on more named voices than these"), §9 name counts, Registry row 33, OG-17.
- *Locus checked:* `hutterite-brethren_geschicht-buch-deu_wolkan1923.txt`. The Chronicle spells him "Rideman" or "Ridemann" (52 + 5 occurrences). Its table of contents lists "Peter Ridemans Schreiben an die im Land ob der Enns" (line 534), "Peter Ridemans Brief an die Philippischen" (563), "Peter Ridemans Schreiben an Hanns Amon" (569) and "Peter Ridemans Brief der Gemein ... aus seiner Gefängnis" (595). The text prints them, for example line 12461, under the margin note "Peter Ridemans anderer Brief an die Philippischen Brüder" ("Will Euch mit kurzen Worten das Urteil dieses Spahns ..."), and line 12636, the letter to Hans Amon ("Peter, Dein Bruder und Vertrauter im Herren, meinem lieben Bruder im Herren Hans Amon. Ich wünsch Dir viel Barmherzigkeit ..."). Further Riedemann sections follow at 13665, 13789, 13915 and 14039, and his last hymn is noted at 20409.
- *The count:* the figure "37 in five files, 22 in Beck" is reproduced only by counting "Riedemann" plus "Ridemann" (Beck 15 + 7, Wolkan 5, McGlothlin 6, Bossert 2, the Riedemann file 2). The search left out the Chronicle's own spelling, "Rideman". The stated term "Riedemann" alone gives 25 in 4 files.
- *Effect:* this changes a binding disclosure (Doc_01 §7 item 2, which is carried into Doc_02 §7 item 2). It also changes the Author Gravity Visibility entry and the "Moravian wing" summary in §1. These letters carry the Library's "verbatim-ready after page-image check" flag and Wolkan's modernised spelling (OG-3, OG-7), like every other Chronicle passage.
- *Fix:* add Riedemann's letters, as the Chronicle prints them, to the named voices that have readable words. Give them a Registry row with loci, or extend row 27. Restate the visibility count with the spelling variants named. Re-run the other surname counts with variants: Blaurock is "Blabrock" in Wolkan (for example lines 311, 2222 and 5467), and Hubmaier and Grebel have variant spellings too.

**B3. Sattler's date is not given by "three witnesses" as an execution date.** Doc_02 §4 (Sattler bullet: "Tier 1 for the sentence and the date, 21 May 1527, which three witnesses give: the *Mirror*, the Chronicle and Böhmer"), §8 ("Sattler was executed on 21 May 1527 | Documented | The *Mirror*, the Chronicle and Böhmer"), Registry row 13 ("The sentence ends 'Done the 21st day of May, A. D. 1527.'").
- *Loci checked:* Wolkan line 5816 to 5821. The Chronicle's sentence is "Anno 1527, am 21. Tag des Maien, ward B. Michael Sattler von Staufen ... mit samt etlichen Personen zu Rottenburg am Necker gefangen, um etlicher Artikel willen". Read on its own grammar, the date governs "gefangen" (taken prisoner), not the execution. *Mirror* lines 58936–58959: the court's sentence is the quoted passage ending "...he shall be pinched five times in the same manner." The words "Done the 21st day of May, A. D. 1527" come after the account of the burning, the brothers' beheading and the wife's drowning "a few days afterwards". They are the compiler's closing date line, not the end of the sentence. Böhmer line 1733 is explicit: "Sattlers märtyrertod, 21 Mai 1527".
- *Effect:* *Documented* can stand on Böhmer, with the *Mirror* consistent. But the basis as written overstates the evidence, and row 13 assigns the date line to the court's voice.
- *Fix:* restate the basis: Böhmer explicit; the *Mirror*'s closing date consistent; the Chronicle attaching 21 May to the arrest. Correct row 13's description of the date line.

**B4. Dirk Willems's "trustworthy persons" is cited to another martyr's entry.** Registry row 16 ("The rescue is reported on others' word: 'trustworthy persons' (line 86506)"). Doc_02 §2, §4 and §8 rest on it.
- *Locus checked:* *Mirror* line 86506 reads "Until quite recently trustworthy persons were still living, who ... saw him in his leather clothes, lying dead in his blood". It is in an entry about 18,000 lines before Dirk Willems, about a man "secretly murdered by night". The Dirk Willems use is at line 104653: "Concerning his apprehension, it is stated by trustworthy persons, that when he fled he was hotly pursued by a thief-catcher". The script passed this quotation only because the phrase occurs in the file six times.
- *Effect:* the claim stands, but at the wrong locus. Under the quotation rule this is a blocking locus error.
- *Fix:* change the locus to line 104653. Check the other short phrases with more than one hit in the *Mirror* ("two disputations are extant", "trustworthy memoirs") by eye. I checked both, and both are right.

**B5. "Contested" for who baptised whom has no contesting witness, and it downgrades Doc_01 without routing.** Doc_02 §3 item 2 and §8 ("Grebel baptised Blaurock and Blaurock then baptised the others | Contested").
- *Loci checked:* Wolkan lines 5449–5519 (the Chronicle's sequence). Egli Nr. 636 (lines 18080–18135), in which Marx Bosshard tells of Blaurock baptising and Jörg Schad says "syg Felix Manz töifer gesin". The Zurich file shows Blaurock and Mantz baptising at Zollikon. That is consistent with the Chronicle's sequence, which has Blaurock baptised first and then baptising others. Nothing on the shelf contests it.
- *The rating:* Article 17's *Contested* means credible witnesses or scholars disagree. A single late communal source with no rival is *Documented* as the Chronicle's account, or *Inferential/Thin* for the event itself.
- *Consistency:* Doc_01 §2 rates the sequence *Documented* (timeline bullet, citing `rzg`). Doc_02 says "*Widely Accepted* for the outline (Doc_01 §2)", which mis-cites Doc_01's rating for the sequence, and no OG entry routes the change to the lead.
- *The same applies to Sattler's authorship.* Doc_01 §2 states it as *Documented* ("Michael Sattler, principal author of Schleitheim"). Doc_02 §3 item 4 finds it not attested on the shelf. OG-8 frames this only as census wording.
- *Fix:* re-rate the sequence (Documented as the Chronicle's account; the event single-sourced). Route both Doc_01 departures to the lead as change-order candidates in the ledger.

**B6. Two Registry verification notes state shelf counts that are false.** Registry rows 49 and 50. Doc_02 §7 item 5 rests on them.
- *Row 49 (Ribbeck):* the row says "two uses of the word 'Wiedertäufer', both passing contrasts with the Münster movement (lines 1705 and 2117)". `grep -c -i wiedertäufer` gives 10 lines (for example 10892, 10947, 11202, 14794, 17314, 18394, 20411, 20421). The other eight use "Wiedertäufer" for the ancient rebaptisers (Donatists, Petilian), which is the dossier's point seen from the other side. The conclusion (no comparison of Donatists with the sixteenth-century movement beyond the two Münster contrasts) stands. The count does not. Line 2117 also likens Rothmann's fall to Novatian's, which is a comparison and not only a contrast.
- *Row 50 (von Soden):* the row says "None of the four files contains 'Anabapt' or 'Wiedertäufer' (checked by two methods)". `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt` and `vonsoden_streit-rom-karthago-ketzertaufe-deu_1909.txt` both have "die orientalischen Wiedertäufer" (line 332) and "die wiedertäuferische Praxis" (line 1564), in the third-century sense.
- *Effect:* the Excluded status is right. But a note that claims a two-method check whose result is wrong is the kind of claim the project treats as most serious.
- *Fix:* correct both counts, and say in what sense the word is used.

**B7. McGlothlin's file does hold part of the Sixth Article.** Registry row 22 ("The Sixth Article (the sword) is therefore not in this file"), Doc_02 §7 item 3 ("McGlothlin's file lacks printed pages 6 and 7, so it has no Sixth Article"), OG-4.
- *Locus checked:* McGlothlin lines 647–654, "be disposed toward him in all things, lest there be any disagreement in the body by which it could perish. For every kingdom divided against itself perishes. Since, therefore, Christ is such as is written concerning him, necessarily the members ought also to be such, that the body may remain whole and united". This is the closing paragraph of the Sixth Article, as Jackson's text shows at lines 8274–8283 ("that there be no strife in the body to destroy it. For every kingdom divided against itself perishes ...").
- *What is missing:* the heading and the sword sentences of the Sixth, and the end of the Fifth.
- *Effect:* the sourcing description of a binding witness is inexact, and row 22 quotes lines 647–648 without saying what they are.
- *Fix:* say that the file holds the last paragraph of the Sixth Article, without its heading or its statement on the sword. Adjust "every text that has a Sixth" in §3 item 5 and in the §8 row accordingly.

**B8. Reviewer-side coverage checks: recall 5/10, and the PRESS answer, to be dispositioned.** These are required by the Framework's Step 2 review rule, and Doc_02 §9 and OG-16 hand them to this round.
- *Instrument:* the References and Further reading of the English Wikipedia article "Anabaptism", fetched 2026-10-23. This is independent of the build. The build swept `archive.org` and the vendored apparatus.
- *Ten works a specialist would expect, chosen from that list:*
  1. Vedder, *Balthasar Hübmaier* (1905): found, row 34.
  2. van Braght, *Martyrs Mirror*: found, rows 11 to 19.
  3. *The Chronicle of the Hutterian Brethren* (1987): found, row 72.
  4. Marpeck, *Writings* (Klassen and Klaassen, 1978): found, row 69.
  5. Cornelius, *Geschichte des Münsterischen Aufruhrs* (1855): found, row 91.
  6. George H. Williams, *The Radical Reformation*: not found. Row 81 is Williams and Mergal, a different work.
  7. Hans J. Hillerbrand, *Anabaptist Bibliography 1520–1630* (1991): not found.
  8. James M. Stayer, *Anabaptists and the Sword* (1972; 1976): not found.
  9. Werner O. Packull, *Hutterite Beginnings* (1995): not found.
  10. Bender et al., *The Mennonite Encyclopedia* (print): not found as a row. GAMEO is named only as an instrument not reached.

  **Recall = 5/10.**
- *PRESS question, asked verbatim:* "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly." Answer:
  1. Hillerbrand, *Anabaptist Bibliography 1520–1630*. It is itself the field's standard bibliographic instrument, and the §9 sweep should name it as reached or as a coverage limit.
  2. Stayer, *Anabaptists and the Sword*. It is the standard study of the Schwertler and Stäbler question that Doc_01 §4 and Doc_02 §3 item 10 rest on Vedder for.
  3. Albert H. Newman, *A History of Anti-Pedobaptism* (1896/1897). It is public domain by date, and the instrument cites it. It is a possible acquisition lead for English secondary matter.
- *Fix:* row each of the eight works named above that is not held (items 6 to 10, Newman, and, if the drafter agrees, Estep's *The Anabaptist Story* and Ruth's *Conrad Grebel, Son of Zurich* from the same list). Most go at C, consultation only and in copyright. Mark Newman as a rights-check lead. Record the recall result and the PRESS answer in §9 and the saturation statement, and name Hillerbrand among the instruments. With five secondary misses, §3's reliance on 1871–1930 editors should also say plainly that the modern scholarly view on these questions was not consulted. The document half-says this now.

### COSMETIC

**C1. Doubled loci from a mechanical pass.** Doc_02 line 77 "(lines 4793–4794) (lines 4793 to 4794)", line 130 "(lines 5517–5519) (lines 5517 to 5519)", line 198 "(lines 3053–3054) with the executioner (lines 3053 to 3054)", line 210 "("Der Gemainschafft halber" (line 11289), line 11289)". Registry row 3 "(line 64677) (line 64677)", row 21 "(lines 2643–2644) (lines 2643 to 2644)", row 27 "(line 5449) (line 5449)" and "(line 2863) (line 2863)". Keep one locus each.

**C2. Sentences broken where quotations were spliced in.** Doc_02 §2 Sattler: "Böhmer says Sattler was "von dem leiter derselben, Michael Sattler" ... (the leader of the assembly) who sent them". §2 Dirk: "Kolb says the book "although it had passed through numerous editions in the Dutch" ... and later in German and French" (no main verb). §3 item 2: "Marx Bosshard telling of "Marx Bosshard erzählt von Blaurocks Taufe"". §3 item 4: "the articles were adopted "wurden am 24 Februar 1527 in einer Versammlung oberdeutscher täufer"". Registry row 13: "Sattler "Having conferred with them ...""; row 23: "at Schlatt am Randen adopted" and "They "Sie fanden ..."". Row 25: "they hate its way "die wir derselbigen weiss ..."". The quotations are all verbatim, but the sentences around them are not English. This fails the writing bar.

**C3. Row 27's supporting quotation does not say what it is cited for.** The row says the Vorrede's writer gathered his account "from reliable people and from his own experience" and quotes "Weil aber solches bisher nicht ist beschehen" (line 2863), which means "because this has not yet been done". The statement itself is at Wolkan lines 2888–2892: "solches alles hab ich bei glaubhaften Menschen ... erkundigen; auch was ich selbst in guter und gewisser Erfahrung hab". Doc_02 §2 and §4 also rest on it. Swap the locus and the quotation.

**C4. Query count disagrees.** Doc_02 §9: "Thirty-three title and creator queries were run (four of them failed ...)". Registry saturation statement: "31 queries; four were repeated". Reconcile.

**C5. Title labels in quotation marks that are not the file's wording.** Registry row 4: "The Education of Children" (the title block at lines 30255–30266 reads "...HOW ALL PIOUS PARENTS ... ARE REQUIRED TO GOVERN, CORRECT AND EDUCATE THEIR CHILDREN...") and "The Spiritual Resurrection" (lines 26170–26180 read "Plain Instruction ... CONCERNING THE SPIRITUAL RESURRECTION, AND NEW OR HEAVENLY BIRTH"). Use the printed title in quotation marks, or an unquoted descriptive label. Row 20's "The Shunning of those who are Expelled" differs only in capitals (line 938, all capitals), which is acceptable. These are labels, not evidential quotations, so the finding is rated cosmetic.

**C6. OG-4 misquotes its source.** It says the file header and the corpus-map note say the German "was never printed". The McGlothlin file header (lines 18–19) reads "were never printed". The corpus-map note does not use the phrase: it says "which survives only in archival manuscript". Quote each correctly. Doc_02 §3 item 3's "McGlothlin's header note in the corpus map repeats his claim" should name the file header and the corpus-map note separately in the same way.

**C7. The scribe's name.** Doc_02 §2 has "Hauprecht Zapf. Zapff wrote to 1593". The scan reads "Haupprecht Zapff" in the foreword (Wolkan lines 117–118) and "Haupprecht Zapf" at line 2952. Use one form, and say which.

**C8. Library-stage outputs not gathered in one place.** Process V2.0 §4 lists "cross-world overlaps and pairs (`cic/corpus-map/PAIRS.yaml`)" and "corpus-map rows with a Library-issued `row_id`, corrected `role` and `voice_of`". The pieces are scattered: the Vedder role note (§1), the McGlothlin retitle (OG-5), the Egli double placement (OG-14) and the OG-13 candidates. The siblings the dossier §6 names (Reformed Cities, Wittenberg, anti-Trinitarians) and the PAIRS question are not stated. The approved `jes` exemplar does not have this either, so this is a polish item: one short paragraph would close it.

**C9. Disclosure §7 item 9 understates how German is used.** It says "This document quotes German only to name and locate passages." In fact German quotations carry evidence in the Article 4 check (the Moravian column), in §3 items 1, 5, 6 and 11, and in the forces lens. The provisional status is stated elsewhere (the opening note, OG-3). Reword item 9 to say that these German quotations carry weight and stay provisional until the page images are read.

**C10. Process narration inside the document.** Doc_02 §9 ("The reviewer-side recall test ... and the PRESS question are for Round 1") and OG-16 ("The Round 1 review adds ...") narrate the review process. In the revision, replace them with the recorded results (B8).

## Checks that passed

- **Corpus figures (item 7).** I reproduced them by two methods. `cat` of the 25 files piped to `wc -m -w` under `LC_ALL=C.UTF-8` gives 35,213,045 characters and 5,591,950 words. A Python sum of decoded lengths gives 35,213,045. Under `LC_ALL=C` the result is 5,573,280 words and 35,507,084 bytes. Tradition role: 18 files, 28,554,821 characters (81.1 per cent). German: 13 files, 16,351,859 characters (46.4 per cent). The Registry's header counts (99 rows; 28 A, 22 B, 44 C, 5 D; 80 P, 17 S, 2 M; 91 Native, 7 Out-of-Boundary, 1 Named Comparandum) reproduce exactly. Bossert's "peinlich" on 51 lines and "gütlich" on 19 reproduce.
- **Boundary and Step 0 / Doc_01 consistency (item 2).** The window, regions and strands are carried unchanged. The Münster exclusion is kept as a scope decision. The Mantz date, the in/by check, the Schleitheim provenance and Marpeck are handled as Doc_01 §7 binds them. The exceptions are B1 and B5. OG-9 (Württemberg, Tyrol) and OG-10 (new floor evidence) are correctly routed to the lead and not decided.
- **Attribution discipline (item 3).** Every source Doc_02 names for a claim has a Registry row. Every row has a Boundary Status, and Excluded rows have a reason. Rothmann is correctly a Named Comparandum with a Comparandum Note. Second-witness rows license nothing verbatim, and Doc_02 quotes none of them. Nothing is attributed to the project lead without a record: the Library rulings cite `LIBRARY-DECISION-LOG.md`. Confidence A is defensible on the rows checked. Rows 26 and 34 license slightly more (the cross-check role; "the good time of the church in Moravia") than their notes show read. The drafter may narrow those, and I do not count it as a finding.
- **Step 2's job (item 4).** All of Part II §1 to §9 is present, with the STARLITE record, the saturation statement (honestly marked "Not closed"), a quotability flag per file, voice flags on mixed works, edition and language per work, holdings dispositions, and every dossier §1–§5 item accounted for. The bar matches the `jes` exemplar.
- **Forces integration (item 5).** This is substantive, not lip service. It names the sources for each Layer 1 cell, says what the silences show (deliberations absent; the legal frame at second hand through Goldast 1712 and 1713; the Swiss silence after 1527), and gives survivorship patterns. It states the limit plainly ("an effect of what survives ... not a finding that persecution was the most threatening force"). Transmission History is a named dimension in every Author Gravity entry.
- **Writing bar (item 6).** The text is generally B2 with short sentences. The only em-dashes are inside verbatim quotations (the Step 0 commitment text, Doc_02 line 277; Bossert's heading, Registry row 32), which is correct. "Not attested" is used only as an absence. Uncertainty is stated plainly. There are no AI tells beyond the spliced sentences in C2.

## Spot-checks read by eye at the locus (41)

- McGlothlin 481–516, 600–655, 1439–1440, 1460–1461, 1702–1705, 2620–2644.
- Böhmer 1711–1800 (eight quotations).
- Beck 296–303, 329–330, 4770–4776, 4895–4897, 11182–11186, 11234–11245, 11256–11271, 11285–11289, 11312–11314.
- Wolkan 86–130, 2855–2892, 5449, 5517–5519, 5814–5880, 12455–12650.
- Egli 17671, 17843–17847, 18080–18135, 18483–18486, 28360–28383, 33679–33681, 33751–33757.
- Bossert 1278–1297, 3050–3054.
- *Mirror* 5621–5622, 58466–58479, 58680–58750, 58900–58959, 86500–86510, 104627–104745, 147915–148004, 148150–148240, 152735–152800.
- Vedder 5088–5100, 9527–9546.
- Kolb 1289–1310.
- Jackson 5555–5560, 7244–7245, 8270–8283.
- Funk 26165–26180, 30255–30276.
- Elkhart 934–942.
- Ribbeck (ten lines); von Soden 332 and 1564.

## Escalation-category check

- **Representative identity or title:** none arises.
- **Portfolio or cross-world:** OG-13 (placing other worlds' files) and OG-14 (Egli double placement) are already routed to the Library and the lead. Nothing new.
- **Governance or methodology:** none. OG-10's Step 0 change-order question and B5's two Doc_01 change-order candidates go to the lead through the ledger. They are not methodology changes.
- **Unresolved tension the pipeline cannot close:** none. Every finding above has a concrete fix within the documents. This is Round 1 of three.

The scope rulings OG-9 (regional boundary reading) and OG-8 (census wording) remain the lead's, as Doc_02 §11 asks.

Disposition: (left for the drafter)
