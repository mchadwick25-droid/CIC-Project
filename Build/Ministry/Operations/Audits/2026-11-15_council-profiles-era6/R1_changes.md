# Round 1 changes: era 6 council profiles (2026-11-15)

The coordinator applied the brief fixes from each reviewer's scratch copy; Opus fixers applied the entry and records fixes, each re-checking the evidence in cic/texts/ before applying it.

---

## Council profiles, era 6, round 1: changes for Part A (Council of Constance 1414)

Files changed: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-constance-1414.entry.json` and `records.json`, key `council-of-constance-1414` only. I re-read records.json just before writing it and replaced only that key, so the Basel key the other agent is editing was left alone. I did not touch the brief, the audio file or README.md. Both JSON files pass `python -m json.tool`. No entry sentence runs past 25 words. The only one the script flagged is a false split inside a quotation in outcome[8], which is really two sentences of 9 and 15 words. Before each fix I re-opened its source lines with sed or grep.

### Blocking

**A-B1 (Benedict XIII's reply).** Confirmed. MANSI27 l.110726-110760 is the notarial instrument made at Peñíscola on 21 January 1417. l.111237-111246 gives the heading of the reply, and l.111387-111391 has "non sunt generalis Synodus ... excommunicati". In FIN3, no. 244 is the cardinals' answer to Alfonso of 3 May 1416, with "ire non possumus nee debemus" at l.29988-29989. No. 256 is the declaration of 8 March 1417. No. 258 is the excommunication dated Maundy Thursday, VI id. Apr. (Finke dates it 8 April 1417), l.31527-31553. Finke's footnote pointing to Mansi is at FIN2 l.4850.
- Entry `outcome[1]`: "Benedict XIII did not accept it. The council's summons was served on him at Peñíscola in January 1417. His written reply said those gathered at Constance were 'not a general synod' (the acts, in Mansi). Being excommunicate, he said, they did not represent the universal church. His cardinals had told King Alfonso in May 1416 that they could not and must not go there. On Maundy Thursday 1417 Benedict excommunicated all those gathered at Constance (Finke)."
  - Applied differently: the review's "In his own reply of January 1417" became "the summons was served ... in January 1417". The held line dates the serving of the summons, and the reply is recorded in the same instrument. The review's one long sentence is split in two, and I added the cardinals' letter.
- Entry `traditions[0].note`: "Benedict XIII refused it, saying those gathered there were no general synod (his reply, in Mansi)."
- Entry `record`: new participant row, "Benedict XIII, reply to the council's summons, January 1417 (Mansi, volume 27), and his and his cardinals' letters (Finke, volume 3)". Its note: "The refusing pope's own voice; hostile to the council."
- Entry `sources`: FIN3 moved from `fromTheCouncil` to `fromThoseThere`, retitled "Acta concilii Constanciensis III: Benedict XIII's replies, his cardinals' letters, the excommunication of 1417".
- Records: the absent detail is deleted. Three participant claims are added, all Documented:
  - the reply (MANSI27 l.110726-110760, 111237-111246, 111387-111391);
  - the cardinals' letter (FIN3 l.29733-29740, 29988-29989);
  - the excommunication, quoting "que melius damnata intrusio dici debet" (FIN3 l.31527-31553).
- Fillastre's summary (claim on FIN2 l.4826-4834) is kept as his account.

**A-B2 (conciliariter).** Confirmed. HEF1 l.3333-3337 shows Hefele speaking in his own voice ("In point of fact, however, these two Popes sanctioned only a part"). l.3393-3400 and l.3938-3941 say what the review says. GERSON l.27283-27294 also checks out.
- Entry `uncertain[4]`: the summing-up sentence is replaced with this: "Martin V promised to keep what the council decided in matters of faith 'conciliarly, and not otherwise' (the acts). Hefele, a nineteenth-century historian of the councils, says this left out the decrees on the council's power. Those decrees, he says, did not concern the faith. Gerson, writing after the election, says Martin said often and in public that he would keep what was done conciliarly."
  - Applied differently: I left out the review's "The French clergy in 1682 read the council the other way". The same item already gives the 1682 reading, so the line would repeat it. I added the Gerson sentence, since he is a witness of the time.
- Entry: HEF1 added to `sources.writtenLater`. Hefele added to the modern-reconstruction `record` row.
- Records: the absent detail is deleted. In the contested claim "The binding force of Haec sancta", "no held writer argues it either way" is replaced with Hefele's reading (l.3393-3400, 3938-3941) and Gerson's statement (l.27289-27293). Two claims are added:
  - Hefele's reading (l.3333-3400, 3938-3941; modern reconstruction; Documented);
  - Gerson's statement (l.27283-27294; participant; Documented, with "tract date not checked" in the claim).

**A-B3 (Gregory's surname).** Confirmed at HARAS l.4820-4823: "perhibetur Metropolita Kijoviensis Gregorius Semivlach suscepisse iter ad synodum Constantiensem". The header names him an archpriest of the Ruthenian chapter at Lviv, writing in 1862, and his church is the one in communion with Rome.
- Entry `people`: renamed "Gregory, metropolitan of Kiev (Gregorius Semivlach, in Harasiewicz)". The part is unchanged.
- Entry `uncertain[13]`: added "Harasiewicz, a Ruthenian Catholic church historian of Lviv writing in 1862, names him Gregorius Semivlach, metropolitan of Kiev. He says Gregory is reported to have set out for the council in 1418."
  - Applied differently: "came in 1418" became "set out for the council". That is what "suscepisse iter" says.
- Entry: HARAS added to `sources.writtenLater`. Harasiewicz added to the modern-reconstruction `record` row.
- Records: the absent detail is deleted. One claim is added (HARAS l.4820-4823; modern reconstruction; Documented).

### Substantial

**A-S1, A-S2: applied by the coordinator (brief).** Current brief wording:
- A-S1, paragraph 6: "In September the council ruled that no safe-conduct shields a heretic from a church court."
- A-S2, paragraph 8: "eight letters under 452 seals, by František Palacký's count."
- Records side: these were already in place, so nothing changed.
  - The session XIX ruling is claim "Session XIX (23 September 1415): no safe-conduct to heretics bars a church judge..." (MIRBT l.13959-13978, re-checked). It is also on the council's side of the contested claim "The safe-conduct".
  - Palacký's count is claim "Palacký's heading gives 452 seals..." (PALDOC l.30062-30065, 30270-30273, re-checked: 35+100+102+84+24+26+27+54 = 452).
  - In the entry, `outcome[2]` already names Palacký and `decided[6]` already carries the ruling.

**A-S3 (Who click).** Checked against `Who_Scan_Supplement.md`:
- l.234: Fillastre, WHO;
- l.241: d'Ailly, "WHO (thin; judgment call)";
- l.245: Sigismund, STORY;
- l.247-249: John XXIII, Gregory XII and Benedict XIII, all STORY.

`Who_Scan_Era6.md` l.110 scores Richental WHO (recorder). None of the remaining NOT SCORED people has a row in either scan. That covers Zabarella, Brogny, Andrew of Poznań, Malatesta, Dominici, Chlum, de Causis, the bishop of Lodi, Duke Ludwig, Frederick of Austria, Gregory of Kiev, Richard of London, Heusden, Wladimiri, Falkenberg and Petit. The verdicts already in the entry also match the era 6 scan: Hus, Jerome, Mladoňovice, Wyclif, Gerson and Bridget WHO; Martin V STORY; Páleč LISTED (paired row).
- Entry `people`: the six verdicts are set as the scans give them, with d'Ailly as plain "WHO". Added `{"name": "Ulrich Richental", "verdict": "WHO", "part": "Citizen of Constance; saw the council and wrote its chronicle"}`, with no id, since there is no profile.
- The list is re-sorted by verdict (WHO, STORY, LISTED, NOT SCORED) to keep the entry's existing grouping. Order within each group is unchanged.

**A-S4 ("Lords, go in peace").** Confirmed: MANSI27 l.129227-129233 and l.129317-129322 give the words to the cardinal deacon of St Vitus in Macello, speaking "de mandato" of the pope. The dissolution decree is at l.129362-129370, though the two-column OCR is interleaved there.
- Entry `decided[12]`: "His decree dissolved the council and gave all leave to go home. At his command a cardinal deacon said, 'Lords, go in peace' (Mansi)."
  - Applied differently: I dropped the review's "then". In the interleaved columns the order of the Falkenberg reply, the decree and the dismissal cannot be read safely.
- Records:
  - claim "The last session, XLV ..." now names the speaker and the pope's command, with witness l.129215-129243 and 129317-129322;
  - new claim "Martin V's decree at the last session dissolved the council and gave all present leave to go home" (l.129362-129370; acts; Documented).

**A-S5 (Wyclif's bones).** Confirmed at RAYN28:
- the heading is at l.7971;
- the letter to the bishop of Lincoln runs l.7977-8019, dated "V id. Decembris, anno xi";
- the definitive sentence and "per alias nostras litteras ... confirmavimus" are at l.7988-8001;
- "igne publice concremari" is at l.8015;
- the letter to the English king's council is at l.8019-8025;
- Raynaldus files all this under 1427 (year heading at l.7559).

Changes:
- Records, absent detail rewritten: "The burning of Wyclif's bones as carried out". Its note: "The council ordered them dug up in 1415 (Mansi), and Martin V's letter of his eleventh year orders them burned (raynaldus l.7977-8019). The burning itself is held only in Foxe, under the heading A.D. 1425."
- Records, two claims added:
  - the letter text (l.7977-8019; participant, because Martin V is writing in his own voice; Documented);
  - Raynaldus's frame, the year 1427 and the appeal to the king's council (l.7559, 7971-7976, 8019-8025; later narrative; Documented).
- Records, contested claim "When Wyclif was condemned": the acts' side now adds Martin V's letter (l.7988-8001), "without dating it".
  - Applied differently: the letter does not date the sentence, so the claim says so rather than placing it outright on the 4 May side.
- Entry `uncertain[5]`: added "Martin V later wrote that the council's sentence had ordered the exhumation, and that he had confirmed it (Raynaldus)."
- Entry: RAYN28 added to `sources.writtenLater`. New participant `record` row: "Martin V to the bishop of Lincoln, on Wyclif's bones, in his eleventh year (Raynaldus, Annales ecclesiastici, volume 28)". Its note: "The pope the council chose, writing years later; printed in Raynaldus's Annales, which file it under 1427."

**A-S6 (Luther 1521).** Confirmed at LUTH3 l.5221-5237, with the editors' note at l.5245-5248.
- Entry `outcome[8]`: added "In his 1521 reply Luther went further: 'all the articles of John Hus condemned at Constance are altogether Christian.'"
- Entry: the `record` later-narrative row now reads "Martin Luther, 1520 and 1521". LUTH3 added to `sources.writtenLater` as "An Argument in Defense of All the Articles, 1521".
- Records:
  - absent detail rewritten: "Luther's words at Leipzig in 1519, printed in full", noted as not held, but the volume gives the article (l.5245-5248) and his 1521 defense (l.5221-5237);
  - claim added (l.5221-5237, 5245-5248; later narrative; Documented).

### Minor

- **A-M1, applied by the coordinator (brief).** "And I commit it to the most gracious Lord Jesus Christ." PALDOC l.17288-17289 reads "piissimo", re-checked. Records and entry carry only the Latin (claim on l.17288-17304) and no English rendering, so nothing changed there.
- **A-M2, applied by the coordinator (brief).** "Richental counts 145 bishops and names envoys from Constantinople." The records already split the count (claim on l.11631-11665) from the envoys (claim on l.2722-2724).
- **A-M3 (Buck).** Confirmed at RICH l.406-412 ("als ob ... abschrift einer aus den zwanziger jahren stammenden vorlage"), and the fuller Latin diary at l.413-429.
  - Records claim: "Buck judges the Aulendorf codex of Richental a copy made about the mid-1400s from an exemplar ('vorlage') of the 1420s, behind which lay a fuller Latin diary", witness l.406-429.
  - Entry `record` note: "Buck judges his text a mid-1400s copy of an exemplar from the 1420s."
  - Not my file, flagged only: `Who_Scan_Era6.md` l.110 still says "lost original", cited to the RICH header.
- **A-M4.** Confirmed: "jussit condemnari et exuri" (PALUB l.2328-2332).
  - Entry `outcome[4]`: "It said he had Hus and Jerome condemned and burned 'under his safe-conduct, or rather his bald-conduct'."
  - The records claim on Prague 1420 is reworded the same way, quoting "jussit condemnari et exuri".
- **A-M5.** Confirmed at FIN2 l.966-975.
  - Entry `issue[3]`: "While the proposal to confirm Pisa lay silent, Fillastre writes, the council acted against Hus."
  - The records claim is reworded to the Italian proposal and d'Ailly's counter-schedule, witness l.966-977.
- **A-M6.** Confirmed at PALDOC l.17304-17305. Entry `people`: "Duke Ludwig, son of Clem of Bavaria (Mladoňovice)".
- **A-M7.** Confirmed at the Bridget card, l.48.
  - Entry `uncertain[12]`: "Her Who card gives Cumming's view that she had been canonized in 1391. He says John XXIII confirmed it in 1414, and Martin V in 1419." I split it to stay under 25 words.
  - The records contested claim on Bridget now adds "and Martin V in 1419".
- **A-M8, applied by the coordinator (brief).** "Fillastre praised God that the church stood under one head." The entry's `outcome[0]` already gives "Praised be the Most High ...". The records carry the Latin (FIN2 l.8162-8163). Nothing changed there.

### Census differences for Open-Gaps (from the review's Census section; not profile defects)

1. `the-hussite-and-bohemian-brethren-movement`, documentedStories, "The Sixth of July at Constance", says "the council met in the cathedral with the emperor Sigismund presiding".
   - This tells Mladoňovice's side as settled. The acts name Jean de Brogny presiding (MANSI27 l.77804-77816), which the entry treats as a contested claim.
   - It also calls Sigismund "emperor", though he was not yet crowned emperor.
2. `latin-papal-church-avignon-to-lateran-v`, `why` and `longDescription`: "The council deposed the rivals". Gregory XII resigned (FIN2 l.2412-2418).
3. The same tradition's `legacy` says "In 1870 the First Vatican Council turned the claim down once more". Pastor aeternus as held (Denzinger) does not name Constance, and that absence stands in the records.
4. Some parties at the council have no census tradition covering the date:
   - the metropolis of Kiev under Lithuania (Gregory). `muscovite-monastic-christianity` is Moscow's, and no Ruthenian or Lithuanian Orthodox row covers 1418;
   - the Dominicans (Giovanni Dominici, John of Podiomitis). `the-dominican-order` ends in 1300;
   - the Bridgettines (the Scandinavian request, RICH l.3027-3058).


---

## Round 1 changes, Part B — Council of Basel–Ferrara–Florence 1431

Files changed: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-basel-ferrara-florence-1431.entry.json` and `records.json`, but only the key `council-of-basel-ferrara-florence-1431`. records.json was re-read just before the write, and only this key was replaced (ensure_ascii=False, indent=2, trailing newline). After the write, the `council-of-constance-1414` key is byte-for-byte what it was before. The brief, the audio and README.md were not touched. The review asks for no README fix: `calledBy` is "not a finding".

Both files pass `python -m json.tool`. Sentence check over every entry string (file paths excluded): the longest sentence is 25 words, and none is over 25.

Counts in records: claims 114 → 123, contested claims 20 → 21, absent details 12 (unchanged).

Every cited line was re-opened with sed or grep before its fix went in. Where the review's line numbers or wording were off, the corrected version is noted below.

### Brief fixes (applied by the coordinator from the reviewer's scratch copy)

The current brief was read. It matches the scratch copy, and the entry was made consistent with it.
- B-B1, para 2: "For Basel we hold some of its letters, but its session records reach us only in quotation."
- B-B2, para 3: "Those who stayed at Basel denied he could move it, deposed him and chose their own pope."
- B-S1, para 7: "Doukas, a Greek historian on the union's side, says the returning bishops were asked, "Did we win?""
- B-M1, para 5: "The Greeks signed on 5 July. "With tears and sighs most of us signed," Syropoulos writes. Mark of Ephesus refused. Hearing it, Eugenius said, "Then we have achieved nothing." Next day the decree was read in Latin and Greek."
- B-M2, para 4: "bishops from twenty sees, by Syropoulos's list"
- B-M3, paras 5 and 8: "Mark of Ephesus" both times.

### Blocking

**B-B1 (Basel's own documents are held).** Confirmed in M31. "LITERE CONCILII BASILEENSIS" is at l.3352. "FELICIS V. BULLA" is at l.25913, with a bull dated at Lausanne on 27 May 1440 at l.26080-26090. "RELATIO D. JOANNIS DE RAGUSIO ... Oratoris Sacri Concilii Basiliensis plurimis annis apud Graecos" is at l.26095-26101. The Compacts and Mansi's admonition are at l.28590-28614. RAY l.31583 has "quam ipse Joannes dein pro Concilio legit". One correction: the review's "M31's own header, l.10" is the Library's prepended content note, not Mansi's own text. So it is not cited as a witness; the documents themselves are cited.
- Entry `uncertain[0]`: "Basel's session records are not among our sources, save where Raynaldus, Glassberger and others quote them. Mansi's tomus 31 prints some of Basel's own documents: letters, the Compacts with the Bohemians, John of Ragusa's report and bulls of Felix V." The review's 25-word second sentence was tightened to 24 words.
- Entry `record`: two items added, as the review words them. The first is "Letters of the council of Basel, the Compacts with the Bohemians and bulls of Felix V (Mansi, tomus 31, appendices)", kind acts, note "Basel's own documents, printed by Mansi from manuscripts. For the Basel party." "Compacts of Prague" became "the Compacts with the Bohemians", Mansi's own phrase. The second is "John of Ragusa, report to the council of Basel on his embassy to Constantinople (Mansi, tomus 31)", kind participant, note "Basel's envoy to the Greeks; for Basel."
- Entry, consequential edits: `people` John of Ragusa now ends "...; later Basel's envoy to Constantinople; his report to Basel is in Mansi". In `sources.fromTheCouncil[0]`, "and Basel matter" became "and documents of Basel".
- Records claim "The main acts of Basel's sessions..." was rewritten. The new text: "Basel's session acts (Mansi tomi 29 and 30) are not held. Mansi's tomus 31 prints some of Basel's own documents: its letters, the Compacts with the Bohemians, John of Ragusa's report and bulls of Felix V. The rest is quotation in Raynaldus, Glassberger, Mirbt and Mansi's tomus 32." Witnesses: M31 l.3352-3361, 25913-26090, 26095-26101, 28590-28614; RAY l.14188-14212; GLASS l.20455-20477; MIRBT l.15134-15138; M32 l.1611. Tagged modern reconstruction, Documented.
- Records: two claims added. One is for the Compacts (M31 l.28590-28614, acts, Documented). The other is for John of Ragusa's report (M31 l.26095-26101 and RAY l.31578-31584, participant, Documented). The second says "Mansi's note says he read it before the council".
- Records `absent_details[0]` note was rewritten to say the same: tomus 31 prints some of Basel's documents, and the rest reaches us in quotation.

**B-B2 (the transfer told in the papal frame).** Confirmed. GLASS l.20990-20994 has "nec transferre nec dissolvere posset". M32 l.6990-6996 has the Lausanne "ne assentiret tunc Eugenio". The brief fix is above. As the review says, the entry and records need no change: claims at GLASS l.20990-20994 and M32 l.6988-6996 and the contested claim "Whether Basel remained a council after the transfer" already hold both sides. One note for the coordinator: README.md l.5 still uses the old frame ("Those who stayed at Basel deposed him..."). It is a Ministry support file and the review did not flag it, so it was left as it is.

### Substantial

**B-S1 (Doukas favored the union).** Confirmed: DOUK l.490-495 has "Catholicae ecclesiae communionis studiosissimum", and l.14324-14327 has "plebs fera ... faex nationis Graecae ... acta omnia pro infectis reputabat". There is one correction. The preface the review calls "his editor's preface" is Boulliau's (BULLIALDI PRAEFATIO, from l.355), not Bekker's. The wording below names Boulliau, his first editor.
- Entry `record`, Doukas note: "Greek historian of the fall of Constantinople. His first editor, Boulliau, says he held to communion with the Catholic church. He scorns those at home who rejected the union. The notes correct him from the acts." It is split so each claim sits with its own witness: the preface for Boulliau's sentence, and Doukas's own text for the scorn.
- Entry `outcome[2]`: "Doukas, who favored the union, also says some bishops would not sign until they were paid. Syropoulos says the opposite: no money was asked or promised at the signing."
- Records contested claim on money: "Doukas, hostile" became "Doukas, on the union's side".
- Records, two claims added. The first is Boulliau's judgment (DOUK l.489-495, modern reconstruction, Documented): "Boulliau, Doukas's first editor, says Doukas held firmly to communion with the Catholic church. He blamed the Greeks who made the union insincerely, to win western help against the Turks." The second is Doukas's own scorn (DOUK l.14324-14327, later narrative, Documented): "Doukas calls the common people who treated the union as undone the dregs of the Greek nation."

**B-S2 (the rival decrees are Mansi's note).** Confirmed. RAY l.31300-31310 gives only the majority's session. "bina decreta inter se opposita eadem die eademque in sessione prodierunt" is Mansi's note, at RAY l.31504-31505.
- Entry `datesNote`: "Mansi's note says two rival decrees came out of the same session." The review has "were read". The verb was changed to "came out of", because "prodierunt" means "were issued", not "were read".

**B-S3 (verdicts already scored).** Confirmed. The supplement has Eugenius IV as STORY at l.250 and l.44, and Aeneas Sylvius Piccolomini as "WHO (hostile inside writer; flag)" at l.233 and l.46.
- Entry `people`: Eugenius IV is now "STORY" and Aeneas Silvius Piccolomini is now "WHO". Their parts are unchanged.
- I also checked every other `people` verdict against `Who_Scan_Era6.md` and the supplement. The NOT SCORED names have no row in either scan: John VIII, Joseph II, Cesarini, Albergati, Aleman, Felix V, John of Ragusa, Antony of Heraclea, Dorotheos, Metrophanes, Isaias, the Georgians, Constantine, Sargis and Joachim, Andrew, John the Coptic patriarch, Nicodemus, Abdallah, Timothy, Isaac, Traversari and Basil II. The scored names match: Mark, Bessarion and Scholarios are WHO; Syropoulos is WHO; Mammas, Plethon and Jonah are LISTED; Zara Yaqob is WANTED; Nicholas V is STORY.
- For the coordinator: Isidore of Kiev is STORY in the era 6 main table (l.226). But the same scan's event rows (l.268, l.271) say "Isidore LISTED", and supplement answer 9 logs "Isidore of Kyiv (era 6 LISTED ...)" as a change order. The entry keeps STORY, from the main table. That inconsistency between the scans is outside this entry and may want an Open-Gaps note. The review also flags that Gregory XII and Sigismund in the Constance entry show the same slip (outside Part B).

**B-S4 (Glassberger's date and his editors' 14 December).** Confirmed. GLASS l.20474 has "die veneris, VII.", with the footnote marker 6 attached to the "VII". Footnote 6, at l.20494, reads "Secundum Card. Hergenröther ... et Dr. H. Bruck ...: 14 Dec."
- Entry `datesNote`: "Glassberger dates its first session to Friday 7 December 1431; his Quaracchi editors give 14 December, after Hergenröther and Brück."
- Entry `uncertain`: new item, placed before Felix V's day. "The day of Basel's first session: Glassberger says Friday 7 December 1431. His Quaracchi editors give 14 December, after Hergenröther and Brück." This was added so the contested point also appears in the entry's list of uncertainties.
- Records: the Glassberger claim is now tagged Contested, with its witness narrowed to l.20474-20475. A claim was added for the editors' 14 December (GLASS l.20494, modern reconstruction, Contested). A contested claim was added, "The day of Basel's first session", with sides "Friday 7 December 1431: Glassberger (l.20474-20475). 14 December: his Quaracchi editors, after Hergenröther and Brück (l.20494)."

**B-S5 (the Sphrantzes passage was cut short).** Confirmed: SPHR l.10236-10254. The words are "ceterum cogita de synodo et rem curae habe, praesertim, quum impii tibi timendi sunt; cogere autem eam ne iam aggrediare", then "τοῦτο δὲ ἀδύνατον ὄντως· σχεδὸν γὰρ φοβοῦμαι μὴ καὶ χεῖρον σχίσμα γένηται", then "μηδὲν εἰπὼν ἀναστὰς ἀπῆλϑε". The review's gloss, "use the council as a threat to the Turks", goes a little beyond the Latin we hold. That Latin says to keep the council in mind and in hand, "especially when the impious are to be feared". So the wording was corrected:
- Entry `issue[3]`: "The chronicle printed under Sphrantzes's name has Manuel II tell his son that the Turks feared a union of Greeks and Latins. He told him to keep the council in mind while the Turks were a danger, but not to hold it. He feared a worse schism. John rose and left without a word." "Above all" was dropped, because it is not in the Latin.
- Records claim: the witness is now l.10236-10254, and the text adds "He told him to keep the council in mind while the Turks were a danger, but not to hold it, fearing a worse schism. John rose and left without a word."
- Records contested claim "Why the Greeks came": the Manuel side now reads "Manuel II's advice: the Turks feared a union, so keep the council in mind, but do not hold it, for fear of a worse schism. The chronicle under Sphrantzes's name (l.10236-10254)."

**B-S6 (Ethiopian sender: held witnesses left out).** Confirmed. In ZY, Perruchon's own words are at l.552-553 ("délégation envoyée par le roi Zar'a Yâ'eqôb") and l.673-674. The review cites l.551-552 and 672-674, which are off by one; the corrected numbers are used. Dillmann is in the footnote at l.578-582. LUD l.52432-52434 has "Nihil autem tale in Concilio Florentino actum, sed potius Zera-Jacobum ab Ecclesia Romana alienum fuisse, testantur ipsi Patres Societatis". LUD l.57416-57425 has "Venerunt ab Imperatore & metropolita vestro Oratores ad concilium Florentinum ... quas adhuc apud se extare testatus est Imperator David ... ad Clementem VII".

There is one correction. The review's "later Catholic exhortation/letter" is the oration of the Portuguese patriarch Alphonsus Mendez, by the running head "Oratio Alph. Mendezii Patriarchae Lusitan." at LUD l.56873, and Ludolf's introduction at l.56875. The wording names it that way. The review's single `uncertain` sentence ran past 25 words, so it was split, each sentence keeping its own witness. Ludolf's "nothing of the kind" was kept as he words it, rather than "nothing was done in Zara Yaqob's name", because "tale" refers back to a claim and does not name the emperor.
- Entry `uncertain`: "Who sent the Ethiopians: Eugenius's letter, Patrizi and Perruchon name the emperor, Zara Yaqob. An oration of the Portuguese patriarch Alphonsus Mendez, printed by Ludolf, says the emperor and the metropolitan sent them. It adds that the emperor David later said he still had Eugenius's reply. Dillmann, as Perruchon reports, says Nicodemus of the Ethiopian convent in Jerusalem sent them, without the king's knowledge. Ludolf says Zara Yaqob stood apart from the Roman church, and that nothing of the kind was done at Florence."
- Entry Ethiopian `traditions` note: "Who sent them is disputed: Eugenius and Perruchon name the emperor, Dillmann the abbot of the Ethiopians in Jerusalem."
- Entry `people`, Zara Yaqob: "...named as sender of the envoys by Eugenius's letter, Patrizi and Perruchon, but not by Dillmann".
- Entry `sources.writtenLater`: Ludolf added, "Ad suam Historiam Aethiopicam Commentarius", Hiob Ludolf, Latin, file `cic/texts/ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt`. Entry `record`: a Ludolf item was added so the record list matches the sources: "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691), with the oration of the Portuguese patriarch Alphonsus Mendez", later narrative.
- Records: three claims added, each Contested. Perruchon's own text (ZY l.552-553, 673-674, modern reconstruction). The Mendez oration (LUD l.57416-57425 and 56873-56877, later narrative). Ludolf's denial (LUD l.52424-52434, later narrative). The contested claim "Who sent the Ethiopian envoys" now adds Perruchon to the emperor's side, adds the Mendez oration as its own side, and adds Ludolf as a further side.
- Records `absent_details`, "An Ethiopian-side witness": the review says to delete the Ludolf line. Only the Ludolf sentence was deleted, not the whole item, because the absence still holds: neither Ludolf nor Mendez is an Ethiopian text of the time. The sentence was replaced with "Ludolf (1691) and the Mendez oration he prints were read in context; neither is an Ethiopian text of the time."

### Minor

**B-M1 (order of signing and reading).** Confirmed: SYR l.47625 has "Ejusdem Dominici"; l.47968-47971 has "nihil praestitimus ... Cras solennem Liturgiam"; DOUK l.32663-32664 has "Iulii sequentis die 5". The fix is in the brief (above). The entry's `datesNote` already reads "signed on 5 July 1439 and read on 6 July", and the records' claim "signed on the Sunday" stands. No entry or records change.

**B-M2 (twenty sees).** Confirmed: SYR l.11452-11457 lists twenty. The fix is in the brief. The entry's `attended[2]` and the records already say twenty.

**B-M3 (one term for one thing).** The brief fix is above.
- Entry, last `outcome` item: "The Roman history printed before the acts says the Greeks never received this council, apart from those who sat in it. The Greeks call it the eighth, it adds." It was split to stay at or under 25 words; both sentences rest on M31 l.46008-46015. In the same item, "because the bishop of Ephesus refused" became "because Mark of Ephesus refused", to match the brief. The Greek reads τοῦ Ἐφέσου.
- Records claim: "The Roman editor's history says" became "The Roman history printed before the acts says". The "Roman editor" of the signed list (Observatio editoris Romani) is a different label, and it was left as it is.

**B-M4 (the fathers' phrase, not the Greeks').** Confirmed: MIRBT l.14266 has "id quod sancti doctores et patres dicunt"; DOUK l.12039 has "id quod Graeci dicunt".
- Entry `decided[3]`: "The fathers' phrase, "from the Father through the Son," was read in that sense."
- Records claim: now "It reads the holy doctors' and fathers' 'through the Son' in that sense. Doukas calls the phrase the Greeks'." DOUK l.12037-12040 was added as a witness.

**B-M5 (witness kind).** Confirmed. The date sits in the quoted document, at RAY l.35133-35139 ("dic vero Mercurii, octava mensis Januarii"). "Interfuere illi, praeside legato Pontificio, quinque archiepiscopi..." at l.35139-35142 is Raynaldus's own sentence.
- Records: the claim was split. The first part reads "Ferrara's first session was held on Wednesday 8 January 1438, by the record Raynaldus quotes" (l.35133-35139, acts, Documented). The second reads "Raynaldus says the legate Nicholas (Albergati) presided at Ferrara's first session. He counts five archbishops, eighteen bishops, four bishops-elect and many heads of orders" (l.35130-35145, later narrative, Documented). The legate is "Nicolaus" in l.35130-35132. His surname comes from Mansi's note at RAY l.31494 ("Nicolai tit. S. Crucis ... cardinalis Albergati"), which is added as a witness.

**B-M6 (census gaps; for Open-Gaps).** Nothing was changed in the entry. These items are to be registered by the coordinator:
- Parties at the council with no era 6 census tradition:
  - the Copts (Cantate Domino, RAY l.49118-49150 and 51855-51936);
  - the church of the Syrian patriarch Ignatius (RAY l.59092-59112);
  - the Georgians (SYR l.9398-9404 and 44060-44072);
  - the Camaldolese, Augustinian and Vallombrosan orders, whose heads signed (M31 l.97190-97197);
  - the Dominicans, through John of Ragusa and Torquemada (PO15 l.322-323).
- The live tree's `byzantine-church-palaiologan`, field `why`, says "the Byzantine emperor and patriarch signed a union with Rome". The patriarch died before the signing (M31 l.94680-94684; SYR l.45231-45232, "mortuus ante subscriptionem"). The signed list has no patriarch (M31 l.96984-97420).
- The same entry, `documentedStories[0]`, says "leaving a note in favor of union that Syropoulos suspects was written for him". No held line of Syropoulos says this. SYR l.45200-45244 is silent on the note, as this entry's `absent_details` records.
- The same `why` has "in exchange for military help" and "Mark of Ephesus alone ... refused". This entry tells the first as a witness's view, and the second as contested (Isaias of Stauropolis, SYR l.47677-47681).
- Also for the coordinator, not a census item: the Isidore of Kiev verdict is inconsistent between the era 6 main table (STORY), its event rows (LISTED) and supplement answer 9 (see B-S3).
