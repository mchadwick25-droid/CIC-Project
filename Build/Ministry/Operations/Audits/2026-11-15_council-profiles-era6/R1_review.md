# Round 1 review: era 6 council profiles (2026-11-15)

A full review by two fresh Opus agents, one per council, neither of whom had seen the drafting, at full effort. Part A: the Council of Constance. Part B: the Council of Basel–Ferrara–Florence. Totals: 5 blocking, 12 substantial, 13 minor.

---

## Council profiles, era 6: review round 1, Part A — Council of Constance 1414

**Council.** `council-of-constance-1414`
**Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-constance-1414.brief.txt`, `audio/council-of-constance-1414.audio.txt`, `council-of-constance-1414.entry.json`, `records.json` key `council-of-constance-1414`, `README.md` (the Pisa and Basel join lines).
**Brief.** 399 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.23, Flesch 69.92. Longest sentence 23 words ("We commit your soul to the devil," ...). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Reviewer.** Independent Opus, full effort, first sight of these drafts. No profile file edited. No model calls, no network, no paid services. `git diff origin/main -- cic/texts/` is empty, so every line number below is good on main.

Abbreviations under `cic/texts/`: FIN2 / FIN3 = `council-of-constance_acta-concilii-constanciensis-bd2-lat_finke1923.txt` / `-bd3-lat_finke1926.txt`; MANSI27 = `mansi_sacrorum-conciliorum-collectio-tomus-27-1409-1418-lat_welter-facsimile1902.txt`; RICH = `richental_chronik-des-constanzer-concils-gmh_buck1882.txt`; MIRBT = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`; DENZ = `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt`; PALDOC = `palacky_documenta-mag-joannis-hus-lat-ces_1869.txt`; PALUB = `palacky_urkundliche-beitraege-hussitenkrieg-v1-deu-lat_1873.txt`; HUSLET = `hus_letters_workman-pope1904.txt`; HUSKOR = `hus_korespondence-a-dokumenty-lat-ces_novotny1920.txt`; LUTH2 / LUTH3 = `luther_works-v2-selected_jacobs-spaeth1916.txt` / `luther_works-v3-selected_various1930.txt`; LUTZ = `lutzow_life-and-times-of-hus_1909.txt`; HEF1 = `hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt`; GERSON = `gerson_opera-omnia-tomus-2-pars-1-tractatus-ad-schisma-lat_dupin1706.txt`; RAYN28 = `raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt`; HARAS = `harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt`; WALS = `walsingham_historia-anglicana-v2-lat_riley1863.txt`; GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt`; BUSCH = `busch_chronicon-windeshemense-lat_grube1886.txt`.

**Verdict: REVISE.** Every quotation in the brief and entry is verbatim or a faithful rendering, and the brief's facts sit with their right witnesses. The brief is clear, vivid and free of AI tells. But the records carry three false absences, each of which also misleads the entry: Benedict XIII's own reply to the council is printed in Mansi, the very acts file the entry leans on (and more of his side's texts are in Finke's third volume); a held historian, Hefele, argues what Martin V's "conciliariter ... et non aliter" meant; and a held Ruthenian annalist gives the archbishop Gregory's surname. Six substantial findings follow. The brief tells the safe-conduct dispute from the Hussite and Luther side only, and it uses "their editor" for Palacký. The Who click marks six people NOT SCORED whom the era 6 supplement scan has scored, and leaves out Richental, a scored WHO. The entry gives "Lords, go in peace" to Martin V, but the acts give it to a cardinal deacon. Two more absences are misdescribed: Martin V's order to burn Wyclif's bones is held, and Luther's own 1521 words on Hus's condemned articles are held. Seven minor findings close the list.

A scratch copy of the brief with every brief fix applied is at `/tmp/claude-0/-home-user-CIC-Project/1796b1ed-67d8-5bb9-8f37-94a4cc60df92/scratchpad/R1A_const/constance.fixed.txt`: 400 words, FK 7.03, Flesch 69.73, longest sentence 23 words.

---

## Blocking

**A-B1. Blocking (false absence: Benedict XIII's own reply is held, in the acts file the entry already cites).** Records `absent_details`: "Benedict XIII's own written reply. Known here only through Fillastre's summary; Finke's third volume, which may hold Benedict-side texts, was not read beyond its header." The entry follows it. `outcome[1]` reads "Fillastre summarizes his written reply". The `traditions` note for the Latin Papal Church reads "Benedict XIII's side refused, calling it no general council (Fillastre)". `sources.fromTheCouncil` lists FIN3, but no claim cites it and the records say it was not read.
- Evidence, Mansi. MANSI27 prints the notarial instrument of Benedict's reply, made at Peñíscola on 21 January 1417 (l.110726-110760). The text itself follows, headed "Sanctissimus & beatissimus dominus noster Papa Benedictus XIII. cuidam praetensae citationi sibi in castro Paniscolae ... presentata, respondet per modum qui sequitur" (l.111237-111246). In it Benedict says (l.111387-111391): "praedicti congregati in Constantia non sunt generalis Synodus, nec universalem Ecclesiam repraesentant; cum sint excommunicati, ac omnibus Ecclesiasticis dignitatibus, gradibus, auctoritate, & jurisdictione privati". Finke's own footnote in FIN2 points to this text: "Hardt IV, 1162-74; Mansi XXVII, 1041-46" (l.4846-4847, under Fillastre's "Tenor dicte responsionis sequitur", l.4836).
- Evidence, Finke III. FIN3 holds Benedict's side in its own voice. No. 244 (l.29733-29740): the reply of Benedict's cardinals to King Alfonso, Peñíscola, 3 May 1416, ending "quod ad congregacionem Constancie ire non possumus nee debemus" (l.29988-29989). No. 256 (l.30710-30738): Benedict's own declaration to the notaries of 8 March 1417. No. 258 (l.31527-31553): Benedict's excommunication, dated Peñíscola, Maundy Thursday 1417, of all "apud Constanciam congregatos" (l.31535-31536) and of the coming election, "que melius damnata intrusio dici debet" (l.31549).
- Why it matters. The refusing party's position can be told in its own words, which C3 and pattern rule 3 ask for. It now reaches the reader only through Fillastre, its judge, who wrote and read Benedict's sentence.
- Fix, entry:
  - `outcome[1]`: "Benedict XIII did not accept it. In his own reply of January 1417, he said those gathered at Constance were 'not a general synod' and did not represent the universal church, being excommunicate (the acts, in Mansi). In April 1417 he excommunicated all those gathered there (Finke)."
  - `traditions[0].note`, second sentence: "Benedict XIII refused it, saying those gathered there were no general synod (his reply, in Mansi)."
  - `record`: add `{"witness": "Benedict XIII, reply to the council's citation, January 1417 (Mansi, volume 27), and his and his cardinals' letters (Finke, volume 3)", "kind": "participant", "note": "The refusing pope's own voice; hostile to the council."}`. Move FIN3 in `sources` to `fromThoseThere`, titled "Acta concilii Constanciensis III: Benedict XIII's replies, his cardinals' letters, the excommunication of 1417", since what is cited from it is the three popes' side and not the council's acts.
- Fix, records: delete the `absent_details` item. Add claims: "Benedict XIII replied in writing to the citation, served at Peñíscola on 21 January 1417: those gathered at Constance are not a general synod and do not represent the universal church, being excommunicate" (MANSI27 l.110726-110760, 111237-111246, 111387-111391; participant; Documented); "Benedict's cardinals told King Alfonso in May 1416 that they could not and must not go to Constance" (FIN3 l.29733-29740, 29988-29989; participant; Documented); "Benedict XIII excommunicated those gathered at Constance, Maundy Thursday 1417" (FIN3 l.31527-31553; participant; Documented).

**A-B2. Blocking (false absence: a held historian argues what "conciliariter ... et non aliter" meant).** Records `absent_details`: "A held writer arguing what Martin V's 'conciliariter ... et non aliter' meant. None found". The contested claim "The binding force of Haec sancta" says the same: "is held, but no held writer argues it either way". Entry `uncertain[4]` ends: "Martin V's promise to keep what was done 'conciliarly, and not otherwise' is a text each side could read its own way." That last sentence has no witness, and it is a summing-up line.
- Evidence, Hefele. HEF1 l.3393-3400: "Martin v. sanctioned only those decrees of the Council of Constance which had been made in materiis fidei conciliariter et non aliter, nec alio modo. Now the decrees in question, respecting the superiority of the general council to the Pope, have nothing to do with the faith, and were given at Constance rather tumultuariter than conciliariter." Further, HEF1 l.3938-3941: the decrees of the earlier sessions "which concern the faith ... were given conciliariter as they were approved by Pope Martin v." The Gallican reading is the other side and is already in the entry (the 1682 Articles, DENZ l.23505-23516).
- Corroboration, a witness of the time. In a tract written after Martin's election (its date not checked here), GERSON l.27283-27294 lists, among the absurd results of the appeal he is answering, that Martin V "noluit ea quae conciliariter facta sunt per sacrum Constantiense Concilium inviolabiliter observare; cujus tamen oppositum idem Dominus noster pluries palam dixit". Gerson thus says Martin said several times, in public, that he would keep what was done "conciliariter".
- Fix, entry `uncertain[4]`, last sentence: "Martin V promised to keep what the council decided in matters of faith 'conciliarly, and not otherwise' (the acts). Hefele, a nineteenth-century historian of the councils, says this left out the decrees on the council's power, which did not concern the faith. The French clergy in 1682 read the council the other way." Add HEF1 to `sources.writtenLater` (title "A History of the Councils of the Church I, introduction", author "Karl Joseph von Hefele, tr. W. R. Clark", English) and add Hefele to the `modern reconstruction` witness row.
- Fix, records: delete the `absent_details` item. In the contested claim, replace "no held writer argues it either way" with "Hefele reads it as excluding the decrees on the council's power over the pope (HEF1 l.3393-3400, 3938-3941). Gerson says Martin publicly promised to keep what was done conciliariter (GERSON l.27289-27293)." Add a claim for Hefele's reading (modern reconstruction, Documented as his reading).

**A-B3. Blocking (false absence: the Ruthenian archbishop's surname is held).** Records `absent_details`: "The surname of Gregory, the Ruthenian archbishop. Fillastre's text gives an ellipsis after 'archiepiscopus'; searched all of cic/texts for Tsamblak, Camblak, Zamblak and Samblak with no hit."
- Evidence. HARAS l.4822-4825: "Anno 1418 perhibetur Metropolita Kijoviensis Gregorius Semivlach suscepisse iter ad synodum Constantiensem fine renovandae unionis." Harasiewicz is a Lviv annalist of 1862, so this is a modern reconstruction, and his "perhibetur" (it is said) marks it as report. The four spellings searched miss this one. A modern editor also names the see, Kiev, which matches Richental's "ertzbischoff von Kifionenß" (RICH l.2735) and "Kyfionensis" (RICH l.7167-7171, records).
- Fix, entry `people`: "Gregory, metropolitan of Kiev (Gregorius Semivlach, in Harasiewicz)". The part stays as written. Fix, `uncertain[13]`: add "Harasiewicz, a nineteenth-century Ruthenian annalist, names him Gregorius Semivlach, metropolitan of Kiev, and says he is reported to have come in 1418."
- Fix, records: delete the absent detail. Add the claim (HARAS l.4822-4825, modern reconstruction, Documented as Harasiewicz's statement). Add HARAS to `sources.writtenLater`.

## Substantial

**A-S1. Substantial (a contested point given from one side in the brief).** The brief carries the safe-conduct charge twice: from Hus ("Hus said he came under the king's safe-conduct") and, as its close, from Luther ("Those who burned him, he said, had broken a Christian safe-conduct"). The council's own ruling is not in it. The records hold it as a contested claim ("The safe-conduct", formation_confidence Contested), and the acts are held: MIRBT l.13959-13978, session XIX, 23 September 1415, says no safe-conduct to heretics bars a competent church judge, "etiamsi de salvo conductu confisi ad locum venerint iudicii". Pattern: "Contested gives both sides by name", and "What the acts say is told plainly". Fix, brief paragraph 6, after "The secular court burned him that day.": add "In September the council ruled that no safe-conduct shields a heretic from a church court." (15 words). The scratch copy makes room with five cuts, each keeping its claim and witness: "a Constance citizen and chronicler"; "speaks in his letters"; "deposed two and chose a third, but neither yielded, leaving three"; "pressed John to call a council"; "Richental counts 145 bishops and names envoys from Constantinople" (see A-M2). It also drops one "he" and joins A-M8's change to the Fillastre line.

**A-S2. Substantial (Who item 5: a role stands in for a named witness, in the brief).** Brief paragraph 8: "eight letters under 452 seals, by their editor's count." The count is Palacký's: his heading reads "sigillis 452 additis" (PALDOC l.30063-30065), and his note gives the eight letters' seals as 35, 100, 102, 84, 24, 26, 27 and 54 (l.30270-30273). Recounted, these make 452, and the letters were sent "concilio" (l.30270). Fix: "by František Palacký's count" (same length).

**A-S3. Substantial (C7: the Who click misstates verdicts the scans have made, and misses a scored WHO).** The pattern: "A person in the record whom no Who scan has scored shows as NOT SCORED." The era 6 supplement scan (`Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`, Approved to proceed 2026-11-12) has scored six people the entry marks NOT SCORED:
- John XXIII, STORY (l.247);
- Gregory XII, STORY (l.248);
- Benedict XIII, STORY (l.249);
- Sigismund, STORY (l.245);
- Guillaume Fillastre, WHO (l.234);
- Pierre d'Ailly, WHO, thin, judgment call (l.241).

The era 6 scan scores Ulrich Richental WHO as a recorder (`2026-11-12_who-scan-era6/Who_Scan_Era6.md` l.110, with l.49 and l.69). He saw the council as a citizen and is its most-used witness here, but `people` leaves him out. Fix: set those six verdicts as the scans give them. Add `{"name": "Ulrich Richental", "verdict": "WHO", "part": "Citizen of Constance; saw the council and wrote its chronicle"}` (no id until a profile exists).

**A-S4. Substantial (a quoted line given to the wrong speaker, in the entry).** `decided[12]`: "He then sent them home with 'Lords, go in peace' (Mansi)", with "He" meaning Martin V. The acts give the words to a cardinal deacon, speaking at the pope's command. The first printed account, MANSI27 l.129227-129233: "reverendissimus pater dominus * [Macello] diaconus cardinalis, de mandato ipsius domini nostri totiusque sacri Concilii, prout asseruit, alta & intelligibili voce pronunciavit haec verba ... Domini, ite in pace." The second account, l.129317-129322: "dominus Ynibaldus miseratione divina sancti Viti in Macello S.R.E. diaconus cardinalis, de mandato domini nostri Papae, totiusque sacri concilii ... pronunciavit; haec videlicet: Domini, ite in pace." Martin V's own act is the decree read before it, which dissolves the council and gives leave to go home: "ipsum Concilium absolvimus, omnibusque & singulis in eo existentibus ad propria remeandi ... licentiam impartimur" (l.129368-129370). Fix: "Martin V then dissolved the council by decree and gave all leave to go home. At his command a cardinal deacon said, 'Lords, go in peace' (Mansi)." Records: add the speaker to the claim "The last session, XLV ... closed with 'Domini, ite in pace'".

**A-S5. Substantial (an absence misdescribed, and a contested claim missing a witness).** Records `absent_details`: "The burning of Wyclif's bones. The council ordered them dug up in 1415 (Mansi); the burning is held only in Foxe, under the heading A.D. 1425."
- Evidence. RAYN28 l.7971-8027 prints Martin V's letter to the bishop of Lincoln, dated at Rome "V id. Decembris, anno xi". It orders Wyclif's body and bones dug up, "et igne publice concremari", and his ashes disposed of so that no trace remains (l.8013-8019). It also says Martin had confirmed the council's sentence "per alias nostras litteras" (l.8008-8009). Raynaldus adds that Martin wrote to Henry's council asking royal support (l.8020-8025). So the order to burn is held outside Foxe. The burning as done is still held only in Foxe.
- Why it matters. The contested claim "When Wyclif was condemned" sets the acts (4 May) against Fillastre, who says the 4 May sentence "non transivit in rem iudicatam" (FIN2 l.1868-1869). Martin V's letter is a further witness that the definitive sentence ordering the exhumation stood and was confirmed. It belongs on the acts' side.
- Fix, records: rewrite the absent detail: "The bones' burning as carried out. Martin V's order of December, his eleventh year, to burn them is held (RAYN28 l.7971-8027). The burning itself is held only in Foxe, under the heading A.D. 1425." Add a claim for the letter (later narrative for Raynaldus's frame; the letter text is a papal act). Add to the 4 May side of the contested claim: "Martin V's letter says the council's definitive sentence decreed the exhumation and that he confirmed it (RAYN28 l.7996-8009)." Entry `uncertain[5]`: add "Martin V later wrote that the council's sentence had ordered the exhumation and that he had confirmed it (Raynaldus)." Add RAYN28 to `sources.writtenLater`.

**A-S6. Substantial (an absence misdescribed: Luther's own words on Hus's articles are held).** Records `absent_details`: "Luther at Leipzig in 1519 in his own words. Not held; only a 1930 editor's introduction and Exsurge Domine, article 30."
- Evidence. LUTH3 holds Luther's "Argument in Defense of All the Articles" (the Grund und Ursach; contents l.9, title l.85). On the thirtieth article, l.5221-5237: "In truth, I have greatly erred on this point ... I now say, Not only certain articles, but all the articles of John Hus condemned at Constance are altogether Christian; and I confess that the pope and his followers acted in this matter like a very Antichrist". The editors' note to the article reads "From the Leipzig Disputation of 1519 (Weimar Ed., II, 279)" (l.5245-5248). So the volume holds Luther's own later words on the very claim Exsurge Domine condemned, beyond an introduction.
- Fix, records: rewrite the absent detail: "Luther's words at Leipzig in 1519 are not printed in full; LUTH3 gives the article as he put it there (editors' note, l.5245-5248) and his own 1521 defense of it (l.5221-5237)." Add a claim (LUTH3 l.5221-5237, later narrative, Documented). Entry `outcome[8]`: add after the bull sentence: "In his reply Luther wrote that 'all the articles of John Hus condemned at Constance are altogether Christian.'" Add LUTH3 to `sources.writtenLater`.

## Minor

**A-M1. Minor (translated quote: a sense added).** Brief and records: "And I commit it to the most merciful Lord Jesus Christ." The Latin is "Et ego eam committo piissimo domino Jesu Christo" (PALDOC l.17288-17289). "Piissimus" is most loving or most gracious, and mercy is "misericordissimus". The held English, Lützow, has "the most sacred Lord Jesus Christ" (LUTZ l.12287-12288). Fix: "the most gracious Lord Jesus Christ" (scratch copy).

**A-M2. Minor (an ambiguous sentence).** Brief paragraph 4: "Richental counts 145 bishops and envoys of the emperor at Constantinople." It reads as though he counts the envoys, perhaps as 145. He counts the bishops ("Bischoff hundert und xxxxv", RICH l.11633-11634) and names two dukes "in bottschaft des kaysers von Constantinopel" (l.2722-2724). Fix: "Richental counts 145 bishops and names envoys from Constantinople." (scratch copy; 9 words for 11).

**A-M3. Minor (the Library header cited as the editor; "lost original" not Buck's word).** Records: "Buck dates the Aulendorf codex ... a copy of a lost original of the 1420s", witness "richental ... l.9". Line 9 is the Library thread's header. Buck's preface is at RICH l.406-412: "eine um die mitte des fünfzehnten jahrhunderts gefertigte abschrift einer aus den zwanziger jahren stammenden vorlage". Buck says "vorlage", an exemplar, and adds that a fuller Latin diary lay behind it (l.414-429). The entry's `record` note for Richental and the era 6 Who scan's "lost original" carry the same wording. Fix, records witness: "RICH l.406-412". Fix, entry note: "Buck judges his copy a mid-1400s copy of an exemplar from the 1420s."

**A-M4. Minor (translation weakens the charge).** Entry `outcome[4]`: "It said he let Hus and Jerome burn 'under his safe-conduct, or rather his bald-conduct'." Prague writes that he "jussit condemnari et exuri", ordered them condemned and burned (PALUB l.2328-2332). Fix: "It said he had Hus and Jerome condemned and burned 'under his safe-conduct, or rather his bald-conduct'."

**A-M5. Minor (scope of a paraphrase).** Entry `issue[3]`: "While the union matter lay silent, Fillastre writes, the council acted against Hus." Fillastre's "Et ita siluit illa materia" (FIN2 l.975) refers to the Italian proposal to open by confirming Pisa, which d'Ailly's counter-schedule blocked (l.966-974). Fix: "While the proposal to confirm Pisa lay silent, Fillastre writes, the council acted against Hus."

**A-M6. Minor (an identification without its witness).** Entry `people`: "Ludwig, Count Palatine". Mladoňovice names him "duci Lodwico, filio quondam Clem de Bavaria" (PALDOC l.17304-17305), and no held line in the record calls him Count Palatine. Fix: "Duke Ludwig, son of Clem of Bavaria (Mladoňovice)".

**A-M7. Minor (an item cut short).** Entry `uncertain[12]`: "Her Who card gives Cumming's view that she had been canonized in 1391 and confirmed by John XXIII in 1414." The card's line (`Who-Profiles/era6/batch2/bridget-of-sweden.card.json` l.48) reads "confirmed by John XXIII in 1414 and Martin V in 1419". Fix: add "and by Martin V in 1419".

(A-M8, small, folded into A-S1's word budget: "Fillastre gave thanks" renders "Laudetur et benedicatur altissimus" (FIN2 l.8162), which is praise. The scratch copy has "Fillastre praised God that the church stood under one head." Optional.)

## Census (for Open-Gaps, not profile defects)

- All seven `traditions` ids exist in the live census with the names given and cover 1414-1418.
- `the-hussite-and-bohemian-brethren-movement`, documentedStories "The Sixth of July at Constance": "the council met in the cathedral with the emperor Sigismund presiding". That is Mladoňovice's side told as settled, and it says "emperor" for a man not yet crowned emperor. The entry's contested claim (the acts name Jean de Brogny presiding, MANSI27 l.77804-77816) is the real difference. Flag for Open-Gaps.
- `latin-papal-church-avignon-to-lateran-v`, `why` and `longDescription`: "The council deposed the rivals". Gregory XII resigned (FIN2 l.2412-2418), as the entry says. Flag.
- The same tradition's `legacy` says "In 1870 the First Vatican Council turned the claim down once more". The entry's absent detail (DENZ's Pastor aeternus does not name Constance) stands against this as told. Flag.
- Parties at the council with no census tradition at the date: the metropolis of Kiev under Lithuania (Gregory; `muscovite-monastic-christianity` is Moscow's, and no Ruthenian or Lithuanian Orthodox row covers 1418); the Dominicans (Giovanni Dominici, John of Podiomitis; `the-dominican-order` ends in 1300); the Bridgettines (the Scandinavian request, RICH l.3027-3058). Flag for Open-Gaps.

## Verified

- Every quote, against file and line, in context (who speaks, which council, which year):
  - "Ich lig hie in dem namen des tüfels" and "Sic capiuntur wulpes ... Also werdent die fuchs gefangen", on the road to Constance, at the Arlberg (RICH l.1503-1522);
  - "quendam hereticum Boemum" (FIN2 l.975-976);
  - "potestatem a Christo immediate habet", "etiamsi papalis existat", "in capite et in membris" (MIRBT l.13922-13926);
  - "quasi coactus fecit" (FIN2 l.8623);
  - Fillastre's "Laudetur ... sub uno capite constitui" (FIN2 l.8162-8163);
  - "Committimus animam tuam diabolo" and Hus's reply, spoken by the degrading bishops before the paper crown went on (PALDOC l.17287-17289);
  - "volens meam innocentiam ostendere" (l.17201-17203);
  - Workman's "I should have to give up many truths" (HUSLET l.11690-11693, mid-June 1415);
  - "vir utique bonus, justus et catholicus" and "usque effusionem sanguinis" (PALDOC l.30155-30156, 30255-30258, 2 September 1415);
  - "illam impiam crucem Antichristi ... fecit suo legato ... erigere" and "salvo aut potius calvo conductu" (PALUB l.2312-2316, 2329, 10 July 1420);
  - "autor, patronus et rector" (PALUB l.2291-2292);
  - Luther's "I have not yet found any errors in his writings" and "violated a Christian safe-conduct" (LUTH2 l.4319-4323, 1520);
  - "quod licuit et quod decuit" (MIRBT l.13997-13998);
  - "Unica est sancta universalis Ecclesia, quae est praedestinatorum universitas" (DENZ l.16016-16017);
  - Schaff's "the totality of the predestinate" (`hus_de-ecclesia-the-church_schaff1915.txt` l.2648-2649);
  - Wyclif's exhumation clause, "si ab aliis fidelibus corporibus discerni possint" (MANSI27 l.65561-65563);
  - Bannwart's "impiam et scandalosam" note and Eugene IV's 1446 words (DENZ l.16207-16222);
  - Gallican article 2 (l.23505-23516) and the 1682 and 1690 dates (l.23466, 23484, 23529-23531);
  - Exsurge Domine article 30, "christianissimi, verissimi et evangelici" (l.17662-17664);
  - Lützow's "very entertaining, though very mendacious chronicler" (LUTZ l.9291-9293);
  - the Gregory speech, "per congregacionem concilii" (FIN2 l.8478-8495);
  - Poggio's "ut alterum Catonem dixisses" and his date "III Kal. Junii" (PALDOC l.32704-32705, 32752);
  - the Gerson proposition, "etiam Papalis existat, eam audire ac eidem obedire teneatur" (GERSON l.18262-18265).
- Facts in the brief. All are true as told and sit with their witnesses:
  - the thirty years (FIN2 l.801);
  - Pisa: two deposed, a third chosen, the obediences held (l.824-833; MANSI27 l.13330 for 1409);
  - Sigismund's request and the cardinals' pressure (l.852-858), supported for "pressed" by Březová's "at Sigismund's wish" (records);
  - the November 1414 opening (l.870, 913-929);
  - the flight in March (l.1385-1398);
  - 6 April and the full reading (l.1566-1572);
  - John deposed on 29 May (l.2159-2168), Gregory resigned on 4 July (l.2412-2418), Benedict deposed on 26 July 1417 (l.6645-6681);
  - Hus's arrival on 3 November and arrest "ad tres hebdomadas cum media" later (PALDOC l.13497, 13600-13624), which supports "within four weeks";
  - the secular court burning him that day (FIN2 l.2575-2577);
  - the election on 11 November 1417 (l.17337-17345);
  - the eight letters and 452 seals (recounted).
- Entry facts:
  - the datesNote days (FIN2 l.900-929; Cerretanus l.8689-8693, 9307-9324; RICH l.1720-1722; MANSI27 l.129215-129220);
  - the length, three years, five months and twenty-two days (FIN2 l.8636-8637);
  - Richental's recapitulation counts and the later-hand 72,460 (RICH l.11629-11686);
  - two hundred fathers, "vel circa" (MANSI27 l.60334-60337);
  - the French nation's four hundred (FIN2 l.1333-1335);
  - the English delegation and the bishop of London (WALS l.26581-26586, 28073-28078);
  - the 53 electors (FIN2 l.7814-7819; GLASS l.18874-18880);
  - Zabarella and Andrew of Poznań (FIN2 l.1530-1572; MANSI27 l.60746-60750);
  - the 4 May objection and the 266 and 260 articles (FIN2 l.1861-1871, 2565-2571);
  - the communion decree (DENZ l.15955-16006);
  - the six bishops and Brogny presiding (MANSI27 l.78650-78666, 77804-77816);
  - Mladoňovice's seven bishops and hay-wagon denial (PALDOC l.17245-17246, 13600-13619);
  - the safe-conduct dated Speyer, 18 October 1414 (l.13104-13106);
  - Hus's "venimus sine salvo conductu" and Novotný's 5 November (HUSKOR l.14826-14827, 14871);
  - Frequens's five, seven and ten years "perpetuo" (MIRBT l.13940-13951);
  - Jerome's recantation, retraction and 30 May 1416 death (FIN2 l.3226-3297);
  - the Observant vicar general (GLASS l.18441-18556);
  - Inter cunctas, question 5 (DENZ l.16193-16198);
  - Busch's prior and Sigismund's Latin speech (BUSCH l.20478-20500);
  - Hus on the cup (HUSLET l.11866-11882) and Jakoubek in 1414 (Březová l.35605-35614);
  - Luther's editors on Jerome's safe-conduct (LUTH2 l.6102-6106);
  - Piccolomini's "quasi ad epulas invitati" (`piccolomini_historia-bohemica-lat_1592.txt` l.4055-4057);
  - Foxe's A.D. 1425 heading and "burnt his bones, and drowned his ashes" (l.7920-7922, 8042);
  - the 12 May barons' letter, "pro kriwé narčenie" (PALDOC l.28588-28625);
  - Finke on Fillastre's authorship, with only "a leise zweifelnden Äußerung" from Funk (FIN2 l.257-268).
- C1 to C8: kinds and sides set on every `record` row. Acts held and cited first. Issue, decided and outcome are kept apart. No creed. The tradition-page form with the "Major council" label. The brief is within the cap and opens on a scene. C3 passes in the brief through Hus's own words; for Benedict, see A-B1. Who items 1-4, 6-9, 11 and 13 pass, apart from A-S2 (item 5) and A-M1. No AI tells, empty contrasts, beat lines or filler in the brief, teaser or knownFor. The one summing-up line is in `uncertain[4]` (A-B2).
- The README's Pisa line agrees with the councils scan ("Council of Pisa (1409): folded into Constance", Councils_Scan l.88). `rivers` matches the scan's row (l.85).

## Searches run (absences)

All of `cic/texts/` unless named. Case-insensitive, with long-s and OCR variants.
- Benedict's reply: `responsi|Perpinian|Paniscol|Peniscol` and `congrega[ct]io.. +Constan|conventicul|pretens` in FIN3; `Sanct[iy]f?f?imus +(&|et) +beatif?f?imus +dominus +nof?ter` and `refponf` in MANSI27. These found A-B1.
- `conciliariter|conciliarly`: nine files, including HEF1, GERSON and FIN2, which found A-B2.
- `c?z?amblak|tsamblak|camblac|zamblak|samblak|semivlach|cemblak|tzamblak|semywlach`: found HARAS, A-B3.
- Wyclif's bones: `lutterworth` (21 files); `ossa.{0,40}(Wycl|Wicl)` and the reverse, which found RAYN28, A-S5. `bones` in LUTZ: no hit on Wyclif.
- Luther and Leipzig: `leipzig|lipsi` and `\bHuss?\b|Constance|Costnitz` in all twelve Luther files. These found LUTH3, A-S6, and Table Talk's Worms recollection (`luther_table-talk_bell1886.txt` l.3590), which is not on Leipzig.
- A signed voters' list: `subscripsi` with long-s variants in MANSI27 after l.38000. 25 hits, all notaries' or Benedict's and Balthasar's own subscriptions, none a voters' list. The absence stands.
- Vatican I naming Constance: `CONSTANTI` in DENZ after l.26000. Hits are all the word "constanti"; the absence stands.
- English renderings of the 6 July words: `commit (thy|your|his) soul`, `devil` in LUTZ, Foxe and HUSLET. Found LUTZ l.12287-12288, used in A-M1.

## Counts

Blocking 3 (A-B1 to A-B3). Substantial 6 (A-S1 to A-S6). Minor 7 (A-M1 to A-M7), plus one optional wording note folded into A-S1. Census flags for Open-Gaps: 4.


---

## Council profiles, era 6: review round 1, Part B — Council of Basel–Ferrara–Florence 1431

**Council.** `council-of-basel-ferrara-florence-1431` (Councils scan, `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/Councils_Scan.md` l.86, one joined row).
**Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-basel-ferrara-florence-1431.brief.txt`, `audio/council-of-basel-ferrara-florence-1431.audio.txt`, `council-of-basel-ferrara-florence-1431.entry.json`, `records.json` key `council-of-basel-ferrara-florence-1431` (114 claims, 20 contested claims, 12 absent details), `README.md`. Branch `claude/cft-councils-era6` at d583e23e.
**Brief.** 399 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.96, Flesch 69.24. Longest sentence 20 words ("The acts print a note, found after his death, accepting all that the church of elder Rome holds and teaches."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked with `diff`.
**Reviewer.** Independent Opus, at full effort, seeing these drafts for the first time. No repo file was edited. No model calls, no network calls, no paid services.

Abbreviations for files under `cic/texts/`: M31 / M32 / M35 = `mansi_sacrorum-conciliorum-collectio-tomus-31-concilium-florentinum-lat_welter-facsimile1906.txt` / `-tomus-32-1438-1549-..._1901.txt` / `-tomus-35-1414-1724-..._1902.txt`; RAY = `raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt`; SYR = `syropoulos_vera-historia-unionis-non-verae-grc-lat_creyghton1660.txt`; DOUK = `doukas_historia-byzantina-grc-lat_bekker1834.txt`; SPHR = `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt`; PG159 = `chalcocondyles_historiarum-libri-x-with-isidore-leonard-plusiadenos-pg159-grc-lat_migne1866.txt`; PG160 = `gennadius-scholarius_opera-omnia-pg160-grc-lat_migne1866.txt`; PO15 = `patrologia-orientalis-tomus15_petit-...1927.txt`; PO17 = `john-ephesus_lives-eastern-saints-po17_brooks1923.txt`; GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt`; HOF2 = `hofler_geschichtschreiber-husitischen-bewegung-v2-lat_1865.txt`; HPC = `historia-politica-et-patriarchica-constantinopoleos_grc-lat_bekker1849.txt`; DZ = `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt`; MIRBT = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`; ZY = `zara-yaqob_chroniques-zara-yaeqob-baeda-maryam-gez-fra_perruchon1893.txt`; LUD = `ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt`; MOUR = `mouravieff_history-of-the-church-of-russia_blackmore1842.txt`. Supplement = `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`.

**Verdict: REVISE.** Every quote in the brief is verbatim or a faithful rendering of its line, each sits with the right witness, and the scene, the signing, the reading and the close all check out. But there are two blocking points. The brief says Basel's acts are held only in later writers' quotations, while Mansi's tomus 31, already a main file of this entry, prints Basel's own letters, its Compacts with the Bohemians, John of Ragusa's report to it and the bulls of Felix V. And the brief tells the transfer to Ferrara in the papal party's frame, as settled, although the entry itself lists it as contested and the Basel party's own words are held. There are six substantial findings in the entry and records: Doukas's side is reversed; one Mansi note is given to Raynaldus; two people the supplement scan has scored are shown NOT SCORED; Glassberger's first-session date is tagged Widely Accepted against his own editors; the Sphrantzes passage is cut before Manuel II's warning; and the Ethiopian sender dispute leaves out held witnesses.

A scratch copy of the brief with every brief fix applied is at `/tmp/claude-0/-home-user-CIC-Project/1796b1ed-67d8-5bb9-8f37-94a4cc60df92/scratchpad/R1B/florence.fixed.txt`: 400 words, FK 6.53, Flesch 70.83, longest sentence 20 words.

---

## Blocking

**B-B1. Blocking (false absence: Basel's own documents are held).** Brief paragraph 2: "The acts of the Basel years are not among our sources, save where later writers quote them." The entry says the same at `uncertain[0]` ("The acts of the Basel years are not among our sources, save where Raynaldus, Glassberger and others quote them"). So do the records: claim 10, "Basel is held through quotation in Raynaldus, Glassberger, Mirbt and Mansi's appendices", and `absent_details[0]`, "Basel reaches us only in quotation (... Mansi 31 appendices ...)".
- Evidence. M31's own header, l.10: "The volume also holds the later acts of the Council of Basel and the Council of Bourges." Its index, l.205-600, lists "Littere conc. Basil ad episcopum Segobricensem", "Littera Concilii Basiliensis", "Bulla Felicis quinti", "Relatio D. Joannis de Ragusio" and "Compactata Pragensia". The texts are printed in full, from manuscripts:
  - The council's own letters. M31 l.3352-3361: "LITERE CONCILII BASILEENSIS ad episcopum Segobricensem electum ... [Sacrosancta] generalis Synodus Basilien. in Spiritu Sancto legitime congregata, universalem Ecclesiam repraesentans". The running heads "BASILEENSE G. CONCILIUM" run from l.1527 to about l.25900.
  - The Compacts with the Bohemians. M31 l.28590-28614. Mansi's note: "compactata cum Bohemis, ab ipsis primum concilii legatis ejus nomine in Praga & alibi concordata, ac dein ab ipso demum concilio confirmata". The text follows: "per gratiam sancti Spiritus concordata sunt inter legatos sancti concilii Basiliensis".
  - John of Ragusa's report to the council. M31 l.26095-26101: "RELATIO D. JOANNIS DE RAGUSIO ... Oratoris Sacri Concilii Basiliensis plurimis annis apud Graecos in Civitate Constantinopolitana". He is the same John of Ragusa whom the entry's `people` list has opening Basel. Raynaldus's editor says this report was read to the council (RAY l.31582-31584: "ex narratione rerum a se in Graecia gestarum quam ipse Joannes dein pro Concilio legit").
  - Bulls of Felix V, Basel's pope. M31 l.25913 onward, for example l.26080-26090, dated at Lausanne on 27 May 1440.
- What is true. The session minutes of Basel (Mansi tomi 29 and 30) are not held, and the era 6 Who scan says so (`Who_Scan_Era6.md` l.256). What reaches us is some of Basel's own documents, plus later quotations (RAY; GLASS; MIRBT l.15134-15138; M32 l.1611, Basel's decree on concubinage quoted by a diocesan synod).
- Fix, brief paragraph 2: replace the sentence with "For Basel we hold some of its letters, but its session records reach us only in quotation." (17 words for 17.)
- Fix, entry:
  - `uncertain[0]`, first sentence: "Basel's session records are not among our sources, save where Raynaldus, Glassberger and others quote them. Mansi's tomus 31 prints some of Basel's own letters, its Compacts with the Bohemians, John of Ragusa's report to it, and bulls of Felix V."
  - `record`: add `{"witness": "Letters of the council of Basel, the Compacts of Prague and bulls of Felix V (Mansi, tomus 31, appendices)", "kind": "acts", "note": "Basel's own documents, printed by Mansi from manuscripts. For the Basel party."}` and `{"witness": "John of Ragusa, report to the council of Basel on his embassy to Constantinople (Mansi, tomus 31)", "kind": "participant", "note": "Basel's envoy to the Greeks; for Basel."}`.
- Fix, records: rewrite claim 10 as "Basel's session acts (Mansi tomi 29-30) are not held. Mansi 31 prints some of Basel's own documents; the rest is quotation in Raynaldus, Glassberger, Mirbt and Mansi 32" (witness M31 l.10, 3352-3361, 25913, 26095-26101, 28590-28614; modern reconstruction; Documented). Rewrite `absent_details[0]` to the same effect. Add one claim each for the Compacts (M31 l.28590-28614, acts) and for John of Ragusa's Relatio (M31 l.26095-26101, participant).

**B-B2. Blocking (a contested point told as settled; C3, the Basel party's view not given).** Brief paragraph 3: "In 1437 Eugenius moved it to Ferrara to meet the Greeks, and in 1439 to Florence. Those who stayed at Basel deposed him and chose a pope of their own." This tells the transfer in the papal party's frame. The council "moved", and the men at Basel are only "those who stayed". The entry's own `uncertain` (last item) and the contested claim "Whether Basel remained a council after the transfer" say this is told by party. The Basel side's position is held in its own words, and the brief does not give it.
- Evidence. GLASS l.20990-20994: "Patres autem concilii Basileensis dicebant, quod ... concilium universale legitime congregatum potestatem immediate a Christo haberet et maius esse Papa; et quod idcirco Papa illud sine eius consensu nec transferre nec dissolvere posset." M32 l.6990-6996 (the Lausanne decree, 1449): "sancta haec Lausanensis synodus, dum Basileae in Spiritu sancto legitime congregata perseveraret, ne assentiret tunc Eugenio papae IV. Ferrariae congregationem sub nomine concilii generalis erigenti". The majority at Basel was against the papal choice of place (RAY l.31300-31310; Mansi's note, RAY l.31505-31506: "Concilii enim pars maxima ... cui tamen cardinalis Arelatensis praeerat").
- Fix, brief paragraph 3: replace "Those who stayed at Basel deposed him and chose a pope of their own." with "Those who stayed at Basel denied he could move it, deposed him and chose their own pope." (17 words.) No entry change is needed: the records already hold both witnesses, and the contested claim stands.

## Substantial

**B-S1. Substantial (a reversed side: Doukas favored the union).** Entry `record`, Doukas: "Greek historian of the fall of Constantinople; hostile to the union." `outcome[2]`: "Doukas, a hostile witness, also says some bishops would not sign until they were paid." Records contested claim "Whether money bought the Greek signatures": "Doukas, hostile".
- Evidence. Doukas's editor, DOUK l.489-494 (the preface): "Christianae pietatis tenacissimum et Catholicae ecclesiae communionis studiosissimum se ubique approbat. Graecis levitatem malamque fidem obiicit, qui ficte ac simulate cum Romana ecclesia concordiam inierant". Doukas's own words on the anti-unionists of 1452, DOUK l.14324-14328: "plebs fera, bonis infensa, arrogantiae germen et radix ... faex nationis Graecae ... qui ergo henoticorum partes secuti cum schismaticis colloquebantur". The era 6 Who scan calls him "partisan" (`Who_Scan_Era6.md` l.28), and his side is the union's. His story of the bishops' regret comes from a writer on the union's side, which is worth telling.
- Fix, entry `record` note: "Greek historian of the fall of Constantinople; on the union's side, and scornful of those who rejected it at home (his editor's preface). The notes correct him from the acts."
- Fix, `outcome[2]`: "Doukas, who favored the union, also says some bishops would not sign until they were paid. Syropoulos says the opposite: no money was asked or promised at the signing."
- Fix, records contested claim on money: "Doukas, on the union's side". Add a claim for the editor's judgment (DOUK l.489-494; modern reconstruction; Documented).
- Fix, brief paragraph 7 (Who checklist item 6, a partisan witness marked): "Doukas, a Greek historian on the union's side, says the returning bishops were asked, "Did we win?"" (in the scratch copy, within 400 words).

**B-S2. Substantial (a claim given to the wrong witness).** `datesNote`: "On 7 May 1437 the fathers split over where to meet the Greeks. Two rival decrees were read in the same session, Raynaldus says."
- Evidence. Raynaldus's own text, RAY l.31300-31310, gives only the majority's session of the nones of May and its choice of Basel, Avignon or Savoy. The two rival decrees come from Mansi's note at the foot of the page, RAY l.31490 and 31504-31505: "bina decreta inter se opposita eadem die eademque in sessione prodierunt". The records give this correctly to "Mansi's note" (claim at RAY l.31498-31510, modern reconstruction), and so does `issue[2]`.
- Fix, `datesNote`: "On 7 May 1437 the fathers split over where to meet the Greeks. Mansi's note says two rival decrees were read in the same session."

**B-S3. Substantial (C7: verdicts already made by a scan shown as NOT SCORED).** Entry `people`: "Eugenius IV", verdict "NOT SCORED"; "Aeneas Silvius Piccolomini", verdict "NOT SCORED".
- Evidence. Supplement (approved to proceed, 2026-11-12) l.250: "Eugenius IV (Gabriele Condulmer) | ... | STORY | Official texts"; l.44: "Popes and rulers are STORY on official texts: ... Eugenius IV". Supplement l.233: "Aeneas Sylvius Piccolomini (Pope Pius II) | ... | WHO (hostile inside writer; flag)"; l.46. The pattern shows NOT SCORED only for "a person in the record whom no Who scan has scored".
- Fix: Eugenius IV, verdict "STORY", part unchanged. Aeneas Silvius Piccolomini, verdict "WHO", part unchanged ("At Basel; eyewitness of the session that deposed Eugenius, as Raynaldus quotes him"). For the coordinator: the Constance entry's Gregory XII (supplement l.248, STORY) and Sigismund (l.245, STORY) show the same slip, which is outside this part.

**B-S4. Substantial ("Widely Accepted" where a held editor disagrees).** `datesNote`: "Glassberger dates its first session to Friday 7 December 1431." Records claim "Glassberger dates Basel's first session to Friday 7 December 1431", tagged `formation_confidence` "Widely Accepted".
- Evidence. GLASS l.20474-20475: "die veneris, VII. mensis Decembris ... celebrata est prima sessio concilii Basileensis". His Quaracchi editors' footnote 6 to that "VII", GLASS l.20494: "Secundum Card. Hergenröther, l. c. t. II. p. 96, et Dr. H. Bruck, l. c. p. 428: 14 Dec."
- Fix, `datesNote`: "Glassberger dates its first session to Friday 7 December 1431; his Quaracchi editors give 14 December, after Hergenröther and Brück."
- Fix, records: tag the claim "Contested". Add a claim for the editors' 14 December (GLASS l.20494, modern reconstruction). Add a contested claim, "The day of Basel's first session", with sides "7 December: Glassberger (GLASS l.20474-20475). 14 December: his Quaracchi editors, after Hergenröther and Brück (GLASS l.20494)."

**B-S5. Substantial (a source cut so that it reads one way).** `issue[3]`: "The chronicle printed under Sphrantzes's name has Manuel II tell his son that the Turks feared a union of Greeks and Latins above all." Records: "has Manuel II tell his son the Turks feared a union of Greeks and western Christians" (SPHR l.10236-10242).
- Evidence. The speech goes on, SPHR l.10242-10252: "ceterum cogita de synodo et rem curae habe, praesertim, quum impii tibi timendi sunt; cogere autem eam ne iam aggrediare, quoniam nostrates ... [ad unionem non idoneos] ... τοῦτο δὲ ἀδύνατον ὄντως· σχεδὸν γὰρ φοβοῦμαι μὴ καὶ χεῖρον σχίσμα γένηται". So Manuel tells his son to keep the council in mind as a threat, but not to try to hold it: the union is impossible and could make a worse schism. John rose and left without accepting this (l.10253-10254). Cut at l.10242, the passage reads as advice for union. Read whole, it is advice against holding the council.
- Fix, `issue[3]`, second sentence: "The chronicle printed under Sphrantzes's name has Manuel II tell his son that the Turks feared a union of Greeks and Latins. But he warned him not to hold the council, fearing a worse schism; John left without a word."
- Fix, records: extend the claim's lines to SPHR l.10236-10254 and add the warning to its text. In the contested claim "Why the Greeks came", the Manuel side should read "Manuel II's advice: use the council as a threat to the Turks, but do not hold it (SPHR l.10236-10254)".

**B-S6. Substantial (a contested claim missing held witnesses; an absence left open that the files answer).** `traditions` Ethiopian note: "Who sent them is disputed: Eugenius names the emperor, Dillmann the abbot of the Ethiopians in Jerusalem." `uncertain`: "Who sent the Ethiopians: Eugenius's letter and Patrizi name the emperor, Zara Yaqob. Dillmann, as Perruchon reports, says Nicodemus ...". Records `absent_details`: "Ludolf's works mention Florence but were not read in context."
- Evidence:
  - Perruchon himself, in his own text, takes the emperor's side. ZY l.672-674: "la députation envoyée par le roi Zar'a Yâ'eqôb au concile de Florence"; also l.551-552, "une délégation envoyée par le roi Zar'a Yâ'eqôb". Dillmann's view is in his footnote, l.578-582.
  - Ludolf denies that Zara Yaqob joined at all. LUD l.52432-52434: "Nihil autem tale in Concilio Florentino actum, sed potius Zera-Jacobum ab Ecclesia Romana alienum fuisse, testantur ipsi Patres Societatis".
  - The Catholic exhortation to the Ethiopians that Ludolf prints says the envoys came from the emperor and the metropolitan and took Eugenius's letters back to Zara Yaqob. It adds that the emperor David attested the letters in his letter to Clement VII. LUD l.57422-57425: "Venerunt ab Imperatore & metropolita vestro Oratores ad concilium Florentinum, unde ab Eugenio IV. ad Imperatorem Zara-Jacobum literas reportarunt; quas adhuc apud se extare testatus est Imperator David ... in epistola quam scripsit ad Clementem VII."
- Fix, `uncertain`: "Who sent the Ethiopians: Eugenius's letter, Patrizi and Perruchon name the emperor, Zara Yaqob, and a later Catholic letter printed by Ludolf says the emperor David attested Eugenius's reply. Dillmann, as Perruchon reports, says Nicodemus of the Ethiopian convent in Jerusalem sent them, without the king's knowledge. Ludolf says nothing was done at Florence in Zara Yaqob's name."
- Fix, Ethiopian `traditions` note: "Who sent them is disputed: Eugenius and Perruchon name the emperor, Dillmann the abbot of the Ethiopians in Jerusalem."
- Fix, `sources.writtenLater`: add LUD ("Ad suam Historiam Aethiopicam Commentarius", Hiob Ludolf, Latin, 1691).
- Fix, records: add Perruchon (ZY l.551-552, 672-674) and the exhortation (LUD l.57422-57425) to the emperor's side of "Who sent the Ethiopian envoys", and Ludolf (LUD l.52432-52434) as a third side. Delete the Ludolf `absent_details` line.

## Minor

**B-M1. Minor (an order of events the listener will mishear).** Brief paragraph 5 opens "On 6 July the decree was read in Latin and Greek", and then tells the signing and Eugenius's words. The listener hears the signing as after the reading. The Greeks and the pope signed on Sunday 5 July. SYR l.47626 has "Eiusdem Dominici hora secunda post meridiem"; at l.47971 the pope says "Cras solennem Liturgiam celebrabimus" after signing. The notes to Doukas, DOUK l.32662-32663, give "decreto vero non subsignaverunt Graeci nisi Iulii sequentis die 5". Fix, as in the scratch copy: "The Greeks signed on 5 July. "With tears and sighs most of us signed," Syropoulos writes. Mark of Ephesus refused. Hearing it, Eugenius said, "Then we have achieved nothing." Next day the decree was read in Latin and Greek." The two decree quotes and the bread-and-primacy sentence follow unchanged.

**B-M2. Minor (a loose quantifier; item 4).** Brief paragraph 4: "bishops from about twenty sees, by Syropoulos's list". The list has exactly twenty, SYR l.11452-11457 (Ephesus, Trebizond, Heraclea, Cyzicus, Sardis, Nicomedia, Nicaea, Tornobus, Monembasia, Lacedaemon, Amastris, Mitylene, Stauropolis, Moldo-Wallachia, Rhodes, Melenikon, Drama, Ganos, Distra, Anchialus). Fix: "from twenty sees".

**B-M3. Minor (one term for one thing; item 9).** The brief names Mark as "Mark, metropolitan of Ephesus" (paragraph 5) and then as "The bishop of Ephesus" (paragraph 8). In the entry, one text is "The anonymous Roman history printed before the Greek acts" (`issue[3]`, `issue[4]`, `attended[2]`) and also "The Roman editor of the acts" (`outcome`, last item, M31 l.46008-46015). That is a different label from "The Roman editor" of the signed list (`attended[5]`, the "OBSERVATIO EDITORIS ROMANI", M31 l.97258). Fix: in the brief, "Mark of Ephesus" both times (scratch copy). In the entry's last `outcome` item, "The Roman history printed before the acts says the Greeks never received this council ...".

**B-M4. Minor (an attribution the decree does not make).** `decided[3]`: "The Greek saying, "from the Father through the Son," was read in that sense." The decree speaks of the holy doctors and fathers, MIRBT l.14266: "id quod sancti doctores et patres dicunt ex patre per filium procedere spiritum sanctum". It is Doukas who calls it the Greeks' phrase (DOUK l.12039, "id quod Graeci dicunt"). Fix: "The fathers' phrase, "from the Father through the Son," was read in that sense."

**B-M5. Minor (a witness kind).** Records claim "Ferrara's first session was held on Wednesday 8 January 1438 ... Raynaldus counts five archbishops, eighteen bishops ...", tagged `witness_kind` "acts". The day is in the document Raynaldus quotes (RAY l.35133-35139). The count comes after the quotation closes, in Raynaldus's own words (l.35139-35142: "Interfuere illi, praeside legato Pontificio, quinque archiepiscopi ..."). Fix: split the claim. The date is acts. The count is later narrative, Documented as Raynaldus's statement.

**B-M6. Minor (for Open-Gaps: census gaps and live-tree differences).** The entry agrees with the held texts. The items below are for the coordinator to register, so that they do not go quiet.
- Parties at the council with no census tradition at the date: the Copts (Cantate Domino, RAY l.49118-49150, 51855-51936); the Syrian patriarch Ignatius's church (RAY l.59092-59112); the Georgians (SYR l.9398-9404, 44060-44072). Also the religious orders whose heads signed, apart from the Franciscans: the Camaldolese, the Augustinians and Vallombrosa (M31 l.97190-97197). The Dominicans, through John of Ragusa and Torquemada (PO15 l.322-323), also have no entry. The census has no era 6 entry for any of them.
- `byzantine-church-palaiologan`, `why`: "the Byzantine emperor and patriarch signed a union with Rome". The patriarch died before the signing: M31 l.94680-94684 (9 June) and SYR l.45231-45232 ("mortuus ante subscriptionem"). The signed list has no patriarch (M31 l.96984-97420).
- The same entry, `documentedStories[0]`: "leaving a note in favor of union that Syropoulos suspects was written for him". No held line of Syropoulos says this. His Latin at SYR l.45200-45244 tells the death and is silent on the note, as the entry's `absent_details` already says.
- The same `why`: "in exchange for military help" and "Mark of Ephesus alone ... refused". The entry rightly tells the first as a witness's view, and the second as contested (Isaias of Stauropolis, SYR l.47677-47681).

## Verified

- Brief paragraph 1. The arrival at the port of Ferrara on 7 March and the entry next morning are in M31 l.46705-46718. The bishops sent with the foot-kiss demand are at SYR l.17789. Joseph's question is at l.17873-17875 ("Num reliqui Apostoli ad S.Petri pedes osculandos in genua procubuere?"); the Greek at l.17811-17813 agrees. Embracing as brothers, or going back, is at l.17885-17890; "nunquam ex hac scapha in Terram descendere" is at l.17904-17905; the pope's yielding is at l.17918-17923 and 17963, and the reception "in Camera sua, adstante sola Cardinalium co[rona]" at l.17975-17976. The translation is faithful and adds nothing.
- Paragraph 2. Syropoulos signed: M31 l.97328-97329, "Magnus ecclesiarcha ... Silvester Syropulus subscr." The 1660 title is hostile. The Greek acts tell the patriarch kissing the standing pope's cheek with no quarrel, M31 l.46748-46758. They note only that the rite of reception was asked about overnight (l.46711-46714), so "leave out the quarrel" holds.
- Paragraph 3. The Bohemian hearing in 1433 is at HOF2 l.36062-36068. Glassberger on Basel's doctrine is at GLASS l.20990-20994. The transfer bull of 18 September 1437 is at RAY l.33176-33184, with Mansi's argument at l.31586-31596. The move to Florence on 10 January 1439 (dated 1438 by the Incarnation) is at RAY l.38405-38445. The deposition on 25 June 1439 is at RAY l.42619-42622 and GLASS l.21160-21162. Felix V is at GLASS l.21186-21189.
- Paragraph 4. Syropoulos's list of twenty sees is at SYR l.11452-11457. Purgatory first is in PO15 l.306-334; the Creed addition first in public is in PO17 l.37434-37441. The death, the written note and the date 9 June are at M31 l.94415-94461 and 94680-94684. "Omnia ... quae sentit, & quae dogmatizat catholica & apostolica ecclesia ... senioris Romae, ipse quoque sentio" supports "holds and teaches".
- Paragraph 5. The reading on Monday 6 July by Julian and Bessarion is at M31 l.96261-96270. "Laetentur coeli & exultet terra: sublatus est enim de medio paries, qui occidentalem orientalemque dividebat ecclesiam" is at M31 l.96338-96341, verbatim. The bread and the primacy are at MIRBT l.14280-14282 and 14294-14296. "cum lacrymis & suspiriis nostrorum plurimi subscripsimus" is at SYR l.47655-47656. "Ergo, inquit, nihil praestitimus" is at SYR l.47970, after "num Ephesius Definitioni subscripsisset" (l.47967-47968).
- Paragraph 6. The Armenians are at M31 l.99049-99098 and RAY l.52410-52416; the Copts at RAY l.51855-51936; the Syrians at RAY l.59092-59112; the Chaldeans and Maronites of Cyprus at RAY l.62412-62437.
- Paragraph 7. "vicimusne nos? ... fidem nostram vendidimus" is at DOUK l.12135-12137, the Latin of l.12125-12128. "μέσον ἀληθείας καὶ ψεύδους οὐδέν ἐστιν" is at PG160 l.99432-99433.
- Paragraph 8. "λεγομένης ὀγδόης συνόδου ... τέλος δὲ χρηστὸν οὐδέν, ὅλως τοῦ Ἐφέσου μὴ ὑπογράψαντος, ἀλλὰ καὶ λογομαχίας ... κινησάντων πολλῶν, ὅτε εἰς τὴν Κωνσταντίνου ἐπανῆλθον" is at HPC l.506-510, with the Latin at l.536-539.
- Entry quotes, each re-read in context:
  - "above all to root out the heresy of the Hussites" (GLASS l.20472-20473, "permaxime ad exstirpandam haeresim Hussitarum").
  - "We receive and approve" (M31 l.47688-47690).
  - "with the approval of the holy council" (RAY l.38425-38426, "sacro approbante Concilio").
  - "saving all their privileges and rights" (M31 l.96865).
  - "before three years have passed" (RAY l.51858, "nondum exacto triennio").
  - "little council, or rather a gathering" (MIRBT l.15138).
  - "from its beginning up to the transfer made by us" (DZ l.16219).
  - "Graeco-Latins" and the centaurs (PO17 l.38519-38522).
  - "What union is this, where no plain sign appears?" (PO17 l.38779-38780).
  - "by the Pope's gold" (PG160 l.99667-99668).
  - "if it was not feigned" (PG159 l.54516, "si non ficta fuit").
  - "Did we win? ... traded piety for impiety" (DOUK l.12135-12137).
- Entry dates and counts:
  - Basel opened on 23 July 1431 (RAY l.14188-14211). No bishops at the opening (RAY l.14457-14458).
  - Ferrara's first session on Wednesday 8 January 1438, with 5, 18 and 4 (RAY l.35130-35142).
  - "conventiculum" (RAY l.35532).
  - Seven bishops at the deposition, and Aeneas's words (RAY l.42112-42131, 42626-42628).
  - The Lausanne decree of 16 April 1449 and the French instrument of 4 April (M32 l.6988-6996, 7104-7108, 6855-6862, 6917).
  - Felix's abdication on 7 April 1449 and the first Lausanne session on 24 July 1448 (RAY l.71136-71140).
  - Cantate Domino dated 4 February 1442 by our reckoning (RAY l.49305-49311); 1441 in DZ l.16804.
  - Patrizi's April 1442 and Mansi's 1441 (RAY l.49284-49302).
  - Denzinger's 1438-1445 (DZ l.16425) and Mansi 35's 1438-1446 (M35 l.185-187).
  - Petit's 4 and 8 March and his "mardi saint, 9 avril" (PO15 l.297-304).
  - Bannwart's note of 4 September 1439 and 22 July 1446 (DZ l.16210-16221).
  - The Immaculate Conception note (GLASS l.21233-21236).
- The weekdays in the Julian calendar agree with the acts: 7 December 1431 a Friday, 8 January 1438 a Wednesday, 9 April 1438 a Wednesday, 5 July 1439 a Sunday, 6 July 1439 a Monday (computed).
- The signed list (M31 l.96860-97420): the pope first, then eight cardinals; then Basil of Jerusalem and Mark of Grado, Burgundy's envoys, bishops and the heads of orders; then the "Observatio editoris Romani" (l.97258-97262). On the Greek side the emperor signs first, then Antony of Heraclea for Alexandria, Gregory, Isidore for Antioch, Dositheus for Jerusalem, and the metropolitans, officials and monks.
- The 1443 synod is in M35 l.6060-6082 ("propendo, scriptum hoc esse plane commentitium, a Graeculo quodam schismaticarum partium studioso confictum").
- Mouravieff is at MOUR l.3834-3866, and Isidore at the Dormition is "the cathedral of the Assumption". Issaverdens's four vardapets are at l.7338-7353. Petit's Metrophanes in June and July 1440 is at PO17 l.17899-17901. Mark's "iam pridem ... corruptus" is at PO17 l.38164. Chalkokondyles on the Germans and the cardinals is at PG159 l.18127-18131 and 18233-18236. Leonard's "secundo idus Decembris" is at PG159 l.54516-54517. Doukas on Gennadios's door and on Hagia Sophia as a synagogue is at DOUK l.14222-14236 and 14729-14731.
- The census ids and names in `traditions` all exist and are alive at the dates. The Armenian entry ends in 1441, after the 1439 decree.
- README: the join is told (Basel 1431, Ferrara, Florence, Rome, and the rump at Lausanne to 1449). Each join has its witness in the entry: the transfer bull (Raynaldus; Mansi), the Florence decree (RAY l.38405-38445), the move to Rome (Patrizi; Mansi), the deposition (RAY; GLASS), and Lausanne (Mansi's note; M32). The README's field list could add `calledBy`, which also tells joins. That is not a finding.
- Audio and tags; C1, C4, C5, C6, C8; Who checklist items 1-3, 5, 7, 8, 11 and 13. Readability and sentence length pass.

## Searches run (absences)

- Basel's own acts. Searched M31, M32, M35, MIRBT, DZ, HOF1 and HOF2 for `ba[sf]il(e|i)en|ba[sf]ilea`, with the long s and OCR in mind. M31 gives about 140 hits in l.0-26000, with the index at l.205-600 and the running heads "BASILEENSE G. CONCILIUM". M32 hits l.236, 1544, 1611 and 2931-3019; M35 has none. Mansi tomi 29 and 30 are not in `cic/texts/`. Result: B-B1.
- Felix V's election day. Searched RAY for `Amede|Amad|antipap` in l.40000-48000, and read l.43160-43260 (Aeneas on the conclave, with no day). Searched M31 l.1-30000 for `nov(e|c)mbr|electus` and M32 for `Amede`. No second witness gives 17 November. The entry's absence holds.
- The Syropoulos note. Read SYR l.45170-45300 (Latin). He tells the death "inter coenandum", 10 June, before the signing, and is silent on the note. The entry's absence holds; the live tree's claim does not (B-M6).
- A Coptic-side witness. Searched Renaudot (`renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt`) for `flor[ea]nt|eugen|ferrari|unio(nem|ne) cum|1439-1442|Antonii abbas`. Only the dedication's Florentines and Medici appear (l.136-294). The entry's absence holds.
- An Ethiopian-side witness. Searched LUD and the English Ludolf for `flor[ea]nt|ferrar`. The Commentarius hits l.52406-52434 and 57421-57425, read in context (B-S6); the English New History has none. Read ZY l.565-592 and 660-680.
- Armenian envoys' names in the decree. Read M31 l.98025-98045, 98340-98400 and 99040-99150. None is named; the entry's absence holds.
- Chamich has one line (l.15230-15232). The entry is right.

## Counts

Blocking 2 (B-B1, B-B2). Substantial 6 (B-S1 to B-S6). Minor 6 (B-M1 to B-M6). The scratch brief with all brief fixes applied: 400 words, FK 6.53, Flesch 70.83, longest sentence 20 words.
