# Round 1 review: era 5 council profiles (2026-11-15)

Three fresh Opus reviewers, one per council, none of whom had seen the drafting, at full effort. Part A: Council of Clermont (1095). Part B: Fourth Lateran Council (1215). Part C: Second Council of Lyon (1274).

---

## Council profiles, era 5: review round 1, Part A — Council of Clermont 1095

**Council.** `council-of-clermont-1095`
**Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/council-of-clermont-1095.brief.txt`, `audio/council-of-clermont-1095.audio.txt`, `council-of-clermont-1095.entry.json`, `records.json` key `council-of-clermont-1095`.
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.55, Flesch 68.34. Three sentences over 25 words (27, 33, 30).
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked by script.
**Reviewer.** Independent Opus, at full effort, seeing these drafts for the first time. No profile file was edited. No model calls, no network calls, no paid services.

Abbreviations for files under `cic/texts/` (the working tree matches origin/main for every file cited; `git diff origin/main -- cic/texts/` is empty): PL166 = `stephen-harding_charta-caritatis-and-exordium-in-pl166-lat_migne1894.txt` (Baldric, Albert, Walter); WT = `william-tyre_..._v1-lat-fra_rhc1844.txt`; MIRBT = `mirbt_quellen-...1911.txt`; CART = `le-couteulx_annales-ordinis-cartusiensis-v1-lat_1887.txt`; PL159 = `anselm-canterbury_opera-with-eadmer-historia-novorum-pl159-lat_migne1903.txt`; LP1 / LP2 = `liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt` / `-t2-..._duchesne1892.txt`; ANNA = `anna-komnene_alexias-grc_reifferscheid1884.txt`; MATT = `rhc-armeniens_documents-armeniens-t1-fra_academie1869.txt`; IBNA = `rhc-historiens-orientaux_t1-fra_academie1872.txt`; M21 = `mansi_sacrorum-conciliorum-collectio-tomus-21-lat_welter-facsimile1903.txt`; AASS = `acta-sanctorum_junii-tomus-5-lat_palme1867.txt`; PL152 = `bruno-cologne_opera-omnia-with-acta-pl152-lat_migne1879.txt`.

**Verdict: REVISE.** Every quotation is verbatim, and most facts check out against their lines. But there are two blocking false absences. A contemporary notice that we hold gives a count of bishops (310), a day the council sat (18 November) and a year (1096); the brief says "None of our sources gives a count", and the entry says no source gives a count or an opening day. A held Mansi volume prints several more canons of Clermont, among them the ban on kings and princes granting church offices; the brief and entry say two canons reach us. There are also four substantial findings: "the emperor's daughter" in the brief is heard as Henry IV's daughter; an English rendering of Anna Komnene is shown in quotation marks as her words; an editor's note on the Hours of the Virgin is read backwards; and the entry counts the Bollandists only on the 1096 side of the year when a line it cites gives 1095.

A scratch copy of the brief with every brief fix applied is at `/tmp/claude-0/-home-user-CIC-Project/ae522d88-ff95-54e2-81c3-aaef67a4f314/scratchpad/R1A/clermont.fixed.txt`: 400 words, FK 7.02, Flesch 69.26, longest sentence 23 words.

---

## Blocking

**A-B1. Blocking (false absence: a count, a day and a year are held).** Brief paragraph 3: "None of our sources gives a count." The same claim is made in the entry at `attended[1]` ("No count and no list of names is among our sources"), `uncertain[2]` ("no source among ours gives a number of bishops or abbots"), `datesNote` and `uncertain[3]` ("No source among ours gives the opening day or the day of Urban's speech"), and in the records' `absent_details` ("A count of those present ... No source among ours gives either"; "The opening day ... No source among ours gives them").
- Evidence. Duchesne, Liber Pontificalis tome 1, introduction, prints the notice of Urban II from the Liber Floridus of Lambert, canon of Saint-Omer. LP1 l.47693-47697: "Huius temporibus, anno dominice incarnationis mxcvi, indictione vi, xiiii kl. decembris, sedit concilium apud Clarum montem cccx episcoporum, présidente ipso papa Urbano, in quo tocius orbis populum christianum apostolica invitavit auctoritate sanctam bellico apparatu adiré Hierusalem, de manu Turcorum liberandam." Duchesne on the author and his date, LP1 l.47588-47590: "Lambert, fils d'Onulf, chanoine de Saint-Omer, ... composa, vers l'an 1120, une sorte d'encyclopédie portative". On these notices, l.47681-47682: the notices from Urban II to Calixtus II are "assez courtes, de main contemporaine".
- What it gives. 310 bishops; the council sitting on the 14th day before the Kalends of December, which is 18 November; and the year 1096, with indiction "vi" as printed. Lambert is a contemporary witness to the year as well, so the year dispute has another witness on the 1096 side. The records' contested claim "The year" leaves him out.
- Fix, brief paragraph 3: replace "None of our sources gives a count." with "Lambert, a canon of Saint-Omer, counts 310 bishops." (8 words for 7; the scratch copy stays within 400.)
- Fix, entry:
  - `attended[1]`: "Lambert, a canon of Saint-Omer, counts 310 bishops, with the pope presiding (his notice of Urban II, printed by Louis Duchesne). No list of names is among our sources."
  - `datesNote`: "November 1095, the month William of Tyre gives. Lambert of Saint-Omer has the council sit on 18 November, in a year he gives as 1096. The council was still sitting at the end of the month: a letter of Urban II for the church of Grenoble is dated at Clermont on 29 November, and the act of concord between Cluny and La Chaise-Dieu on 1 December 1095. No source among ours gives the day of Urban's speech"
  - `uncertain[2]`: "The count: Lambert of Saint-Omer gives 310 bishops. Baldric and William give no number, and no list of names is held."
  - `uncertain[3]`: "The day: Lambert of Saint-Omer has the council sit on 18 November. William of Tyre gives November, and documents are dated at Clermont on 29 November and 1 December. No source among ours gives the day of the speech."
  - `uncertain[4]`: add "Lambert of Saint-Omer, writing about 1120 by Duchesne's dating, also gives 1096." (A-S4 also changes this item.)
  - `record`: add `{"witness": "Lambert of Saint-Omer, Liber Floridus, notice of Urban II, printed by Louis Duchesne in Le Liber Pontificalis I", "kind": "later narrative", "note": "A canon of Saint-Omer, writing about 1120 by Duchesne's dating; the only count among our sources (310 bishops), with 18 November and the year 1096."}`.
  - `sources.writtenLater`: add LP1 with the title "Le Liber Pontificalis, tome 1: introduction, the Liber Floridus notices", author "ed. Louis Duchesne", language "Latin and French".
- Fix, records: add a claim for Lambert's count, day and year (LP1 l.47693-47697, later narrative, Documented as his statement). Add a claim for Duchesne's "vers l'an 1120" (l.47588-47590, modern reconstruction). Rewrite the two `absent_details` as "A list of names: no source among ours gives one" and "The day of Urban's speech: no source among ours gives it". Add Lambert (LP1 l.47694) to the 1096 side of the contested "The year".

**A-B2. Blocking (false absence: more canons of Clermont are held).** Brief paragraph 2: "Two canons reach us, printed by Carl Mirbt, a German editor." The entry says the same at `decided[0]` and `uncertain[0]`, and so does the `absent_details` item "The acts and the full list of canons ... two canons reach us only as Mirbt's extracts". The `sources.fromTheCouncil` group lists only Mirbt and the concord.
- Evidence. M21 prints the council of Beauvais held in 1114 by the legate Cono (l.11886-11887: "centesimo decimo quarto in civitate Belvacensi a Conone sedis apostolicae legato concilium celebratum"). Under it come "excerpta quaedam ex hoc concilio, quibus decreta in eo partim edita, partim recitata et confirmata continentur" (l.11936-11938) and "Ex gestis Bellovacensis concilii" (l.11944). Among the decrees recited there, several are headed as Clermont's:
  - l.12045-12049: "Ex Concilio Clavomontano [sic OCR]. Interdictum est, ne reges, vel aliqui principes, aliquam investituram de honoribus ecclesiasticis faciant." This is the ban on kings and princes granting investiture of church offices.
  - l.12064-12079: "Ex concilio Claromontano ab Urbano II. celebrato. cap. 11": no layman may seize another's inheritance ("Ne aliquis laicus alterius hereditates sibi usurpet"), and no priest may admit him to penance until he makes it good.
  - l.12071-12077: "Urbanus papa II. in concilio Claromontano ... cap. 12": "Ne ulli filii concubinarum, & clericorum, presbyterorum, diaconorum, subdiaconorum, ad ordinationes ... promoveantur, nisi monachi, vel regulares fiant."
  - l.12080-12083: "Urbanus II. in eodem concilio, cap. 14": "Nulli clerico liceat deinceps in duabus civitatibus duas praebendas obtinere".
  - Further items follow under "Item ejusdem", "Item ejusdem Urbani ... c. 9", "Idem, cap. 5" and "Item in eodem, cap. 6" (l.12084-12122: two offices in one church; clerics' concubines; gifts for consecrations; benefices bought as boys or as men). Their heading to Clermont has to be read line by line in this two-column OCR before any of them is counted.
- Corroboration that more canons are known. Baluze's notes to Lateran I, M21 l.27445-27452: "constitutio Urbani II. qui in concilio Claromontano statuerat ne monachi in parochialibus ecclesiis ... absque episcoporum consensu, presbyteros collocent". M21 l.45240 and 45261 cite Clermont canons by number. Denzinger's editors list Clermont among the decrees against simony and against clerical incontinence (`denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` l.12708-12709, 12719-12720). William of Tyre's own "canones ... ad morum aedificationem" (WT l.6120-6123) are already in the entry.
- Fix, brief paragraph 2: replace "Two canons reach us, printed by Carl Mirbt, a German editor." with "Some of the council's rulings, its canons, survive in later copies, among them the record of a council at Beauvais in 1114." This also explains "canon" before paragraph 5 uses it (A-M4). Paragraph 5 then says "one canon", "Another" and "a third"; see the scratch copy.
- Fix, brief paragraph 5 (new sentence, as in the scratch copy): "Another forbade kings and princes to invest anyone with a church office." Source: M21 l.12047-12049.
- Fix, entry:
  - `decided[0]`: "The acts are not among our sources. Canons reach us in later copies: two as extracts printed by Carl Mirbt, and others recited again at the council of Beauvais in 1114, printed by Mansi."
  - Add after canon 9: "From the Beauvais record: kings and princes were forbidden to grant investiture of church offices; no layman was to seize another's inheritance, and no priest was to admit him to penance until he made it good; sons of concubines and of clergy were not to be ordained unless they became monks or canons regular; no cleric was to hold prebends in two cities."
  - `uncertain[0]`: "The acts are not among our sources; canons reach us only in later copies, in Mirbt's sourcebook and the Beauvais record of 1114. The fullest account from inside the council is Baldric's, a partisan of the call, who wrote Urban's speech in his own Latin."
  - `record`: add `{"witness": "Canons of Clermont recited at the council of Beauvais, 1114 (Mansi, tomus 21)", "kind": "acts", "note": "Papal; a later council's excerpts that repeat earlier decrees, among them canons headed as Urban II's at Clermont."}`.
  - `sources.fromTheCouncil`: add M21 with the title "Sacrorum conciliorum collectio, tomus 21: the council of Beauvais (1114), canons of Clermont".
  - Mansi 21 already appears in `writtenLater` for Baluze's note; that entry stays where it is.
- Fix, records: rewrite `absent_details[0]` as "The acts and the full list of canons. Not held: Mansi tomus 20 is not among our sources. Canons reach us in Mirbt's extracts (MIRBT l.11220-11233) and in the Beauvais record of 1114 (M21 l.11936-12122)." Add one claim per canon kept, each with its M21 lines and witness_kind acts.

## Substantial

**A-S1. Substantial (misleading; common-name item 8).** Brief paragraph 7: "As the armies came east, Anna Komnene, the emperor's daughter, wrote that her father feared their greed and their broken promises." The only emperor the brief names is "the emperor Henry IV" (paragraph 3), and Alexios is never named, so a listener hears Anna as Henry's daughter. The sentence order also makes it sound as though Anna wrote while the armies came. Evidence: ANNA l.1068-1069, "εγώ Άννα, θυγάτηρ μεν των βασιλέων Αλεξίου και Ειρήνης"; ANNA l.15626-15632 (Alexios heard the report and feared). Fix: "Anna Komnene, daughter of the emperor Alexios, wrote that as the armies came east, her father feared their greed and broken promises." (21 words; scratch copy.)

**A-S2. Substantial (a modern rendering shown as the quote).** In entry `outcome[5]`, "like rivers flowing together from everywhere" sits in quotation marks. It is the drafter's English for Greek, ANNA l.15675-15676: "καθάπερ τινάς ποταμούς απανταχόθεν συρρέοντας". The Library holds no English Alexiad: the only Alexiad file is the Reifferscheid Greek, and no held file contains "rivers flowing". This breaks the pattern's quote rule and CLAUDE.md's rule on modern renderings. The brief tells the same image unquoted, which is correct. Fix: drop the quotation marks: "She tells of an unarmed crowd with crosses on their shoulders, women and children among them, like rivers flowing together from everywhere." Alternatively, quote the Greek verbatim and gloss it.

**A-S3. Substantial (an editor's note read backwards).** Entry `uncertain[8]`: "A later tradition that Clermont prescribed the Hours of the Virgin for clergy rests on late writers, and its own editor doubts parts of it." The records' contested claim says the same: "Late writers cited by the editor of Bruno's Acta (Labbe, Petreius, Dorland, Blomevenna), who himself doubts parts". The editor in PL152 accepts the Clermont prescription: "imo reipsa, ut apparet, in concilio Claromontano (adi Labbeum tom. X Conciliorum col. 517) fuerit injunctum" (l.26632-26636). He points to Labbe's printed councils, not only to late writers. What he doubts is the apparition of Peter to the Carthusians (l.26582-26604) and Petreius's claim that it came before Clermont ("nullo plane argumento probat", l.26653). Fix, `uncertain[8]` second sentence: "That Clermont prescribed the Hours of the Virgin for clergy rests on Ruinart, who reports it as hearsay, and on Labbe's printed councils, which the editor of Bruno's Acta cites and accepts. He doubts only the Carthusian vision told beside it. No witness of the time among ours says so." Fix, contested-claim sides to match: "Ruinart's Life of Urban II ('Ferunt'), and Labbe tom. X col. 517, cited and accepted by the editor of Bruno's Acta (PL152 l.26618-26636); the editor doubts the apparition and Petreius's order (l.26582-26604, 26645-26654)."

**A-S4. Substantial (editors' dates counted on one side only).** Entry `uncertain[4]`, "Migne's heading to the act and the Bollandists give 1096", and `record[12]`, "(1095 in Mirbt and Duchesne, 1096 in Migne's heading and the Bollandists)". The same Bollandist volume gives 1095 at the line the entry cites for Peter of Pamplona. AASS l.26403-26405: "non potest tamen falli nec fallere pro anno 109S [1095, OCR], quo Concilio Claromontano idem Petrus interfuit". Only l.148148-148149, "anno salutis mxcvi in Concilio Claromontano", gives 1096. Fix, `uncertain[4]`: "The year: the act of concord dates itself 1095, and William gives 1095. Lambert of Saint-Omer gives 1096. Migne's heading to the act gives 1096, and the Bollandists give 1095 in one note and 1096 in another. Baldric's printed text says the synod was held the year after a star-shower of April 1095, with '1096' set in brackets, likely an editor's addition." Fix, `record[12]` note: "(1095 in Mirbt, Duchesne and one Bollandist note; 1096 in Migne's heading and another)". In the records' contested "The year", add AASS l.26404 to the 1095 side.

## Minor

**A-M1. Minor (item 1; an inference told flat).** Brief paragraph 2: "Baldric wrote the pope's speech in his own Latin". Baldric gives his own warrant for this, which the brief does not use. PL166 l.77696-77697: "His vel hujuscemodi aliis a Domino apostolico ... intimatis", with these or other such words. Fix: "Baldric gives the pope's words, or words like them, in his own Latin, and he wanted the journey made."

**A-M2. Minor (item 4; sentences past about 25 words).** Paragraph 1, sentence 1 (27 words); paragraph 5, the canon 2 sentence (33); paragraph 8, sentence 1 (30). Fixes, as in the scratch copy:
- "At Clermont in November 1095, Pope Urban II sat in a pulpit. He spoke of Christians suffering in Jerusalem and the East, and called the knights to fight for Jerusalem."
- "Under one canon, whoever went to free the church of God at Jerusalem would have the journey counted in place of all penance. He had to go for devotion alone, and not to gain honor or money."
- "With the soldiers, she wrote, came an unarmed crowd more than the sand and the stars, with crosses on their shoulders. Women and children had left their homes to come too."
"Raised" is dropped from "raised pulpit" because Baldric has only "residens in pulpito" (PL166 l.77477-77478). The call to fight is Baldric's: "pro vestra Jerusalem decertetis" (l.77639-77640), and "Christi milites ... ad defendendam Orientalem Ecclesiam ... concurrite" (l.77629-77631).

**A-M3. Minor (item 4; a term used before the listener has it).** "Asked ... leave ... to go" (paragraph 1) and "he wanted the journey made" (paragraph 2) come before anything says where. Jerusalem as the goal arrives only in paragraph 5. Fix: the second sentence in A-M2 adds "and called the knights to fight for Jerusalem".

**A-M4. Minor (item 4; an undefined term).** "Canons" (paragraph 2) is never explained. Fix: covered by A-B2's "the council's rulings, its canons".

**A-M5. Minor (wording that can be misheard).** Paragraph 5: "Pilgrims to the holy places came first." It is heard as pilgrims arriving first. MIRBT l.11233: "ac primum peregrinis ad sacra loca tendentibus". If the truce detail is kept: "Above all, it covered pilgrims going to the holy places." The scratch copy shortens the truce sentence to fit A-B2 within the cap.

**A-M6. Minor (item 6; hostile polemic not marked).** Anna's "greed" and "broken promises" (paragraph 7) are her own charges against the Franks: "επί χρήμασι κεχηνότες ... τας σφών συνθήκας ευκόλως ανατρέποντες" (ANNA l.15631-15632). The entry's `record` marks her as "hostile to the Franks", but the brief does not. If the cap allows: "Anna Komnene, daughter of the emperor Alexios and no friend of the Franks, wrote ..."

**A-M7. Minor (item 5; a role standing in for a named witness).** Entry `outcome[7]`: "Mansi's editors, notes to the Lateran council of 1123". The notes are Étienne Baluze's: the heading "STEPHANI BALUZII" (M21 l.27334), and the first-person "Lemovices meos" (l.27397) and "nos ... in libro x. de vita rebusque virorum illustrium Lemovicensium" (l.27400-27402). Fix: "Étienne Baluze, in his notes to the Lateran council of 1123 printed by Mansi, says ...". Make the same change in `record[12]` and the records claim.

**A-M8. Minor (item 5 and item 1; record note for Albert).** `record[6]`: "Lotharingian; by Migne's notice he wrote from the reports of those who were there." The notice Migne reprints is Fabricius's ("(Fabric. Biblioth. med. et inf., Lat., tom. I)", PL166 l.27615). It calls Albert "Aquensis in Gallia Ecclesiae custos" (l.27619), and no held line says "Lotharingian". Fix: "By Fabricius's notice, which Migne reprints, custos of the church of Aix ('Aquensis in Gallia'), writing 'ex fide eorum qui praesentes interfuere'."

**A-M9. Minor (a misread citation in the record note).** `record[0]` note: "Mirbt prints canon 2 from Mansi's volume 20 ... and canon 9 from the Codex of Cencius." Mirbt gives one citation for the whole number, "Mansi XX 816. 902" (MIRBT l.11222). He marks only canon 9 "(Codex Cencii)" (l.11228). Nothing on the page says canon 9 is not from Mansi. Fix: "Papal; Mirbt cites Mansi's volume 20, columns 816 and 902, which is not among our sources, and marks canon 9 as from the Codex of Cencius." The records claim already words it correctly.

**A-M10. Minor (a dropped condition).** Entry `decided[7]`: clergy and laity were forbidden to obey the archbishop of Vienne "until the judgment was carried out". CART l.13313-13315 gives two ends: "donec aut judicium quod factum est exequatur, aut querela haec ante nos Canonico judicio ... certiorem finem accipiat". Fix: "... until the judgment was carried out or the case was settled before the pope."

**A-M11. Minor (a place no source gives).** Entry `outcome[3]`: "In Flanders, Walter of Thérouanne writes, Count Robert heard ...". Walter does not say where Robert heard it (PL166 l.65369-65380). Fix: "Walter of Thérouanne writes that Count Robert of Flanders, son of Robert the Frisian, heard the decree of the council of Clermont and left his wife and children for the journey." This also settles a namesake (item 8): l.65372 reads "superioris Roberti Frisonis filius". Make the same change to the people line "Robert of Flanders".

**A-M12. Minor (an inference told flat).** `calledBy`: "The Old French translation of William has it sit at all three places, a change made by the translator". The held text shows only that the two versions differ (WT l.6114-6115 "convocare disposuit" against l.6140-6142 "sist premierement à Verzelai, l'autre foiz au Pui ..."). Fix: "The Old French translation of William has it sit at all three places, where the Latin says only that he planned the first two."

**A-M13. Minor (a generalization from one line).** `traditions[2].note` and the census-edge claim: "Latin clergy later filled the new sees in the East". The held line is one case: Bernard of Valence, Adhémar's chaplain, made patriarch of Antioch (MATT l.15578-15581, Dulaurier). Daimbert at Jerusalem is the census edge's second case (l.15582-15584). Fix for the tradition note: "Princes who took the cross after the council went on to Jerusalem (William of Tyre). The crusaders made Bernard of Valence, who had come as Adhémar's chaplain, patriarch of Antioch (Dulaurier's note to Matthew of Edessa)."

**A-M14. Minor (OCR shown to participants).** Entry `decided[1]` quotes "pecmiiae" (MIRBT l.11226, OCR for "pecuniae"), and `calledBy` quotes "Arverniz" (CART l.13307, OCR for "Arverniae"). Both are verbatim to the file, but participants see the garble. Fix: keep the English and drop the Latin in both places. Or, if the Latin must stay, give the reading with the OCR noted in the record ("pecuniae", printed "pecmiiae" in the vendored OCR).

**A-M15. Minor (C7 form).** `modernCountries` gives only the country. The era 4 form carries a `place` even where no census row gives a place id (Whitby: `{"country": "United Kingdom", "countryId": "Q145", "place": "Whitby"}`). No census row has Clermont as a place (searched). Fix: `{"country": "France", "countryId": "Q142", "place": "Clermont"}`.

**A-M16. Minor (C7; people in the record).** The Who click leaves out the three witnesses whom the 2026-11-14 rescore makes WHO: Anna Komnene (Rescore.md l.50, 203), William of Tyre (l.197) and Ibn al-Athir (l.216). Era 4 lists witnesses in the record the same way (Nicaea 787 lists Theophanes the Confessor, WHO). Fix, if they are to be listed: `{"name": "Anna Komnene", "verdict": "WHO", "part": "Not present; at the Byzantine court, wrote of the armies' coming and traced it to Peter"}`, `{"name": "William of Tyre", "verdict": "WHO", "part": "Not present; wrote of the council about ninety years later, with another speech and Peter present"}`, and Ibn al-Athir likewise. None has a census id yet, so no id is given.

---

## Verified

Quotations, each verbatim in its file (OCR spellings as in the file):
- "Christiani nostri fratres": PL166 l.77485 ("Christiani nostri fratres nostri membra Christi").
- "nobis videntibus": PL166 l.77700.
- "nos unusquisque properantes redivimus ad propria": PL166 l.77737-77738 (hyphenated "prope-rantes").
- "qui praesens est": WT l.6318-6319 ("qui prae-sens est").
- "quod apud Clarummontem civitatem Arverniz celebravimus": CART l.13306-13307.
- "pro sola devotione, non pro honoris vel pecmiiae adeptione": MIRBT l.11226.
- "like rivers flowing together from everywhere": not a quote (A-S2).

Facts checked and found right:
- Baldric's scene: the pulpit and the speech (PL166 l.77477-77486). Weeping, trembling, arguing (l.77696-77699). Adhémar ("Neimarus"), glad face, kneeling, leave and blessing asked and won, the order to obey him, the army (l.77699-77709). The nobles assent and sew the cross on at once (l.77709-77711). Urban's instruction to fit the cross, to go more safely and as an example (l.77711-77719). Raymond's envoys (l.77721-77724). The fainthearted "heri" took heart "hodie" (l.77735-77736). The council dissolved, the preaching and shouting, the daily growth (l.77737-77742). The bishops told to preach in their churches (l.77670-77672).
- Baldric was abbot of Bourgueil and later archbishop of Dol (PL166 l.76177-76185, Gallia Christiana and Orderic). He was not on the crusade and reworked an anonymous history ("Non tamen huic beatae interesse promerui militiae ... nescio quis compilator", l.77311-77318). He was at Clermont by the Histoire littéraire (l.76398-76400). After Piacenza he came to Auvergne with many bishops and abbots of Gaul (l.77461-77464). "Viri potentes et honorati innumeri" (l.77475-77477). The star-shower of 4 April 1095 and "anno subsequente (1096)" (l.77749-77751, 77773-77774).
- William of Tyre: 1095, indiction 4, Henry IV reigning (WT l.6066-6068). Piacenza, the emperor's anger, the Alps, the kingdom of the Franks, the faith "perisse", the prince of darkness (l.6071-6072, 6106-6111). Vézelay and then Le Puy planned, Clermont "mense Novembre", bishops and abbots "ex universis transalpinarum partibus provinciarum", "nonnullis principibus" (l.6114-6119). Canons of morals, and peace "suggerente Petro Heremita" (l.6119-6123). The patriarch: no hope from the Greeks, more than half the empire lost (l.5750-5755). Peter brings the patriarch's letters to Urban (l.5870-5874). The speech's relaxation of penances, the protection, excommunication by the local bishop until restitution, suspension of bishops and priests (l.6320-6332). The bishops sent home to keep the truce (l.6332-6339). Adhémar first, William of Orange after (l.6433-6436). The cross by the pope's command, on clothes and shoulders (l.6450-6452). The list of princes (l.6500-6510). The Old French "sist premierement à Verzelai ..." (l.6140-6142). Writing "in hunc annum ... mclxxxiv" (l.3997).
- Albert: Peter, the patriarch's letters, Rome (PL166 l.27806-27826). The council decreed at Le Puy, then Clermont, with the bishops of all France, dukes, counts and princes (l.27895-27900). The Fabricius notice (l.27619).
- Walter of Thérouanne: Robert, hearing the decree of Clermont, leaves wife and children (PL166 l.65369-65380). The work is his Vita prior (l.64905, 64938).
- The Book of the Popes: Gregory preached the journey and was hindered by King Henry (LP2 l.71352-71356). The church would not let Urban go; with his blessing and absolution they fought "sub eo principe et beato P." (l.71362-71366). Duchesne's "synodes de Clermont (1095)" (l.71663).
- Mirbt no. 256: the heading, the citation, canon 2, canon 9 with the three years, Thursday to Sunday, clerics and monks, pilgrims (MIRBT l.11220-11233). Mansi tomus 20 is not in `cic/texts/` (file list checked).
- Urban to Guy of Vienne, Piacenza, "IIII Idus Martii" (CART l.13244-13266). Hugh's account of the Arvernian council (l.13289-13299). The letter to Count Guigo, the clergy and the people, dated "III Kalend. Decembris apud Clarummontem", which is 29 November (l.13303-13316). Le Couteulx's margin "ANNUS 1095" (l.13240-13241).
- The concord: its heading "(Anno 1096.)" from Baluze's Miscellanea (PL159 l.74874-74878). The parties and the archbishops of Lyon and Bourges (l.74882-74890). "Actum publice apud Clarum-montem ... anno ab Incarnatione Domini 1095. Kal. Decembris, indictione iv" (l.74961-74965).
- Anna: daughter of Alexios and Irene (ANNA l.1068-1069). Alexios's fear (l.15626-15632). Peter (Koukoupetros), his failed pilgrimage, the divine voice, the counts of Frankia (l.15648-15666). The unarmed crowd, sand and stars, crosses, women and children, rivers (l.15671-15676). No pope or council named (searched l.15560-16400 for πάπ-, σύνοδ-, Ούρβαν; the only Rome hit, l.15906, is the banner of St Peter sent to Hugh).
- Ibn al-Athir: Bardouyl and Roger (IBNA l.24668-24705), the caliphs of Egypt (l.24711-24717), the oath on Antioch at Constantinople and the year 490 (l.24720-24735). No pope or council named (searched).
- Matthew of Edessa: year 545, the prophecy of Nerses (MATT l.12668-12672). Italy, Spain, the farthest Franks, Jerusalem (l.12724-12731). No pope or council named (searched). Dulaurier on Bernard of Valence (l.15578-15581).
- Baluze on the Spanish indulgence: "eandemque peccatorum indulgentiam euntibus ... in Hispaniam concesserunt, quae Orientalis ecclesiae defensoribus concessa fuerat in concilio Claromontano" (M21 l.27403-27413).
- Peter of Pamplona at the council, by a Bollandist note (AASS l.26396-26405).
- The census: the four tradition ids exist in `movements` (latin-papal-church-gregorian 1049-1300, cluniac-reform-monasticism 909-1109, latin-church-of-outremer 1099-1291, byzantine-church-after-1054 1054-1300). Their names match. `gregory-vii` is kind person. Q142 France is copied from existing rows. The census's own text on the council, the edge `latin-papal-church-gregorian--latin-church-of-outremer`, agrees with the entry ("At Clermont in 1095 Pope Urban II decreed ..."). No census movement names the council otherwise.
- Coverage: every party at the council has a census tradition covering 1095. The Latin bishops and abbots fall under latin-papal-church-gregorian, Cluny under cluniac-reform-monasticism, and the Byzantine court under byzantine-church-after-1054. La Chaise-Dieu has no tradition of its own and falls under the Latin papal church. Henry IV's party was not at the council. No gap of the era 4 kind was found.
- People verdicts: Urban II, Adhémar, Peter the Hermit, Baldric and the rest are NOT SCORED, and no scan scores them (searched the era 5 scan, the supplement and the rescore). Hugh of Cluny is LISTED (Who_Scan_Era4 l.191, supplement l.420). Alexios I is LISTED (Who_Scan_Era5 l.117). Henry IV is WHO by Mark's answer (Who_Scan_Era5 l.212). Gregory VII is WHO with census id `gregory-vii` (l.32). All correct.
- Pattern: the field order and forms match era 4 (key order compared by script). `kind` and `kindLabel` are right. Rivers are "Latin West", as in the Councils_Scan table (l.75). The brief's caveat opens `uncertain`. Audio tags appear only in the audio script. Common names have their place at first mention in the brief.

## Searches run (absences)

- **A count, a day or a list of names.** Grep of all `cic/texts/` for Claromont, Clarum montem, Clermont, Clarimont and Arvern within 80 characters of 1095, 1096, Urban, concil or synod. Every hit file was opened at its hits. This found LP1 l.47693-47697 (A-B1). LP2 l.87787 is Innocent II's Clermont of 1130; PL152 l.4011-4568 and CART l.2135 are Hugh of Die's Clermont of 1077; Hitti's Usama l.530 is modern and gives no day. No list of names was found.
- **Canons beyond Mirbt's two.** `pro omni poenitentia reputetur` appears only in MIRBT. The Clermont grep over M21 found the Beauvais excerpts (l.11936-12122), Baluze (l.27445-27452) and the notes at l.45240 and 45261 (A-B2). It also found Denzinger l.12708-12720, PL159 l.42302-42305 (an editor citing a Clermont canon on priests' sons), and `lettres-edifiantes_memoires-du-levant-t3-fra_1780.txt` l.4036-4040 (Urban forbade intinction "dans le Concile de Clermont"). Mansi tomus 20: not in the file list.
- **Henry IV's party on Clermont.** The Vita Heinrici IV in `gratius_fasciculus-rerum-expetendarum-v1-lat_brown1690.txt` (l.11729-12700) was grepped for Hierosol/Hierufal/Ierofol, sepulc, cruce, peregrin, expedit, Arvern and Clarom. The hits (l.12430, 12584) are not about Clermont. The absence stands.
- **An appeal from Alexios at Piacenza.** "Placenti" near Graec/Grec/legat/imperator/Constantinop/Urban/1095, and Alexios near Urban/aid/help/auxili, across all files. No appeal was found; `muston_israel-of-the-alps-v1_montgomery1866.txt` l.1522 is modern and gives "1095 and 1096". Bernold is cited by editors only, and his chronicle is not held. The absence stands.
- **Fulcher, Robert the Monk, Guibert and the Gesta Francorum.** Fulcher-, Foucher, "Robertus Monachus", "Robert le Moine", Guibert/Novigent and "Gesta Francorum" across all files. The hits are other Fulchers, other Roberts, or editors' citations (MATT l.12882, 13090, 14433). None of the texts is held. The absence stands.
- **Peter the Hermit in Baldric.** "Petr", "heremit" and "eremit" in PL166 l.77300-77800. The only hit at the council is "beatus Petrus" of Antioch (l.77502), and Peter the Eremite appears later (l.77984). The absence stands.
- **The pope or the council in the Eastern witnesses.** ANNA l.15560-16400, MATT l.12660-12800 and IBNA l.24600-24760 for pope, council and Urban forms. None found. The absence stands.
- **The Hours of the Virgin.** PL152 l.26560-26745 read in full (A-S3).
- **An English Alexiad.** File list grep for anna/alexi/komn/comnen, and "rivers flowing" across all files. Only the Greek is held.

## Counts by severity

- Blocking: 2 (A-B1, A-B2)
- Substantial: 4 (A-S1 to A-S4)
- Minor: 16 (A-M1 to A-M16)

---

## R1 review, part B: Fourth Lateran Council (1215)

- **Council:** `fourth-lateran-council-1215`
- **Files:** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/fourth-lateran-council-1215.brief.txt`, `audio/fourth-lateran-council-1215.audio.txt`, `fourth-lateran-council-1215.entry.json`, and the `fourth-lateran-council-1215` key of `records.json` (branch `claude/cft-councils-era5`, head `e96e6250`).
- **Library:** all 19 cited `cic/texts/` files are present and byte-identical to `origin/main` (md5 checked file by file).
- **Brief:** 400 words, about 2:30 at 160 wpm, so it is at the cap. `grade_text`: **FK 8.84, Flesch 60.98**. That passes, with Flesch 1 point over the floor. Three sentences run past 25 words (28, 30 and 28).
- **Audio:** equals the brief, with `[calmly] ` at the start and `[warmly] ` before the last paragraph and no other tag (diff checked).

**Verdict: NOT APPROVED TO PROCEED. 6 blocking, 6 substantial, 13 minor.**

The quotations and most citations hold, and the drafting is careful. Two things block it. First, there are three false absences: Francis at the council, the canons "held only" in two source books, and "no Cathar text". Second, there are two wrong-work or wrong-author citations: Joachim's Psalterium passage cited as the Tractatus, and Bartholomew of Trent's Life filed under Jordan. Also blocking is one unsupported statement in the record: that Vitry was "not at the council".

---

## Blocking

**B-B1. False absence: Francis at the council does not rest on Glassberger alone.**
- **Where:**
  - `attended[5]`: "No earlier source among ours puts Francis there."
  - `uncertain[4]`: "Whether Francis was there rests on Glassberger alone."
  - `people` (Francis): "by Glassberger's account only".
  - `record` (Glassberger): "the only source among ours that puts Francis at the council".
  - `records.json` `contested_claims[4]`: "Yes: Glassberger alone".
  - `claims[58]`: Inferential-Thin.
- **Evidence:** two held files carry Gerard de Frachet's *Vitae fratrum* (c. 1260, Dominican). In it, Dominic, in Rome to press for his order's confirmation, sees a vision. The next day he meets Francis in a church.
  - `gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt` l.1750-1753: "cum esset Rome beatus Dominicus et pro ordinis contirmacione apud Deum et apud dominum papam instaret quadam nocte orans".
  - Same file, l.1767-1770: "socium ... quem ante non noverat, in crastinum, cum eum in ecclesia reperisset".
  - Manuscript C's variant, l.1776-1777: "circa concilium Lateranense anno domini 1215 celebratum".
  - Reichert's note, l.1743: "Hanc visionem accidisse anno 1215 constat ex II^ red. huius operis".
  - Conway's English, `gerard-de-frachet_lives-of-the-brethren_conway1924.txt` l.1014-1017: "when St Dominic our Father was in Rome, during the sitting of the Lateran Council, pressing his suit before God and the Pope for the confirmation of his Order". The meeting with "the blessed Francis" follows at l.1044-1050.
  - Frachet names his chain of witnesses in Conway at l.996-997 and l.1010-1011: a friar minor, long Francis's companion, told the brethren, and one of them wrote it to Jordan.
- **What is wrong:** a 13th-century source among ours puts the meeting of Dominic and Francis at Rome during the council: explicitly in one manuscript and in Conway's English, and by its editor's dating. Glassberger (late 15th century) is not alone, and is not the earliest.
- **Fix:**
  - `attended[5]`: "Whether Francis of Assisi was there: Gerard de Frachet's Lives of the Brethren, a Dominican collection of about 1260, tells of Dominic meeting Francis in a church at Rome while he pressed the pope to confirm his order. One manuscript and Placid Conway's English put this during the Lateran council, and its editor Reichert dates it to 1215. The Observant Franciscan chronicler Nicolaus Glassberger says Francis met Dominic at the council. Neither says Francis sat in the sessions"
  - `uncertain[4]`: "Whether Francis was at Rome during the council rests on Gerard de Frachet, in one manuscript, in Conway's English and by Reichert's dating, and on Glassberger; neither puts him in the sessions."
  - `people` (Francis) `part`: "Met Dominic at Rome during the council, by Gerard de Frachet's and Glassberger's accounts".
  - `record`: add `{"witness": "Gerard de Frachet, Lives of the Brethren (Reichert's Latin; Conway's English)", "kind": "later narrative", "note": "Dominican, about 1260; tells of Dominic meeting Francis at Rome, during the council in one manuscript and in Conway's English, by a friar minor's report."}`. Change Glassberger's note to "Observant Franciscan; says Francis met Dominic at the council."
  - `contested_claims[4]` sides: "Yes, or at Rome around it: Gerard de Frachet (gerard-de-frachet_vitae-fratrum-lat_reichert1896.txt l.1750-1770, variant l.1776-1777, editor's note l.1743; gerard-de-frachet_lives-of-the-brethren_conway1924.txt l.1014-1050) and Glassberger (l.2110-2112). Against: no early Franciscan source among ours names the council." Add a claim row for Frachet as a later narrative.
  - Add both Frachet files to `sources.writtenLater`.

**B-B2. Wrong-work citation: Joachim's "three branches on one root" is from his *Psalterium decem chordarum*, quoted in a note by Buonaiuti, not from the *Tractatus*.**
- **Where:**
  - `records.json` `claims[32]`: "In his Tractatus, Joachim warns against thinking of the three as three branches fixed in one root ...".
  - `record` witness: "Joachim of Fiore, letter of submission (1200) and Tractatus super quatuor Evangelia".
  - `sources.writtenLater`: "Tractatus super quatuor Evangelia".
  - The brief's "In another work" is literally true, but its sourcing is wrong.
- **Evidence:** `joachim-fiore_tractatus-super-quatuor-evangelia-lat_buonaiuti1930.txt`.
  - The passage sits in Buonaiuti's footnote "(1)" (l.17741), which strings together quotations.
  - Its first part: "« Nobis autem, ut senioritus evo, ... in mundum ». (P., 239d)" (l.17741-17746).
  - The cited words run from l.17746 to l.17856 and end "habes ergo in uno sole mysterium Trinitatis » (P., fol. 229b-c)".
  - The siglum list, l.3009: "P=Psalterium decem chordarum."
  - The cited words: "neque ut tres ramos uni radici infixos, ut substantiam, radicem et tres ramos, hypostases, arbitreris, iuxta aliquorum perfidiam ([l'allusione è a Pier Lombardo]), quod est inducere quaternitatem" (l.17812-17817).
- **Fix:**
  - `claims[32]`: "In his Psalterium decem chordarum (fol. 229), as Ernesto Buonaiuti quotes it in a note to his edition of the Tractatus, Joachim warns against thinking of the three as three branches fixed in one root, the substance as root and the hypostases as branches, which is to bring in a quaternity; Buonaiuti's bracket says the allusion is to Peter Lombard". The witness stays l.17741-17856.
  - `record` witness: "Joachim of Fiore, letter of submission (1200), and his Psalterium decem chordarum as Buonaiuti quotes it".
  - `sources` row: title "Psalterium decem chordarum, quoted in Ernesto Buonaiuti's notes", author "Joachim of Fiore, in Buonaiuti's edition of the Tractatus super quatuor Evangelia", same file.
  - The brief can stay as it is.

**B-B3. Wrong author: the second Life of Dominic is by Bartholomew of Trent, not Jordan of Saxony.**
- **Where:** `sources.writtenLater[0]`: title "Libellus de principiis ordinis Praedicatorum, and the second Life of Dominic", author "Jordan of Saxony, in Acta Sanctorum, August I". `outcome[0]` cites it only as "(the second Life of Dominic)".
- **Evidence:** `acta-sanctorum_augusti-tomus-1-lat_1750.txt` l.94619-94624: "VITA ALTERA, Quam F. Bartholomaeus Tridentinus ex Ordine Praedicatorum ante medium seculi XIII breviter conscripsit". The cited line, l.94737-94738, is in that Life: "Honorius itaque Papa Ordinem confirmavit".
- **Fix:**
  - Split the source row in two. First: title "Libellus de principiis ordinis Praedicatorum", author "Jordan of Saxony, in Acta Sanctorum, August I". Second: title "Vita altera of Dominic", author "Bartholomew of Trent, in Acta Sanctorum, August I", same file.
  - `outcome[0]`: "Honorius III confirmed the order (Bartholomew of Trent's Life of Dominic)."
  - Add a `record` row: "Bartholomew of Trent, Life of Dominic", kind later narrative, note "Dominican, before the middle of the thirteenth century, by the Bollandists".

**B-B4. False "only": the canons are not held only in Mirbt's and Denzinger's extracts.**
- **Where:**
  - Brief, paragraph 2: "Among our sources, its canons are held only in extracts printed by two modern editors, Carl Mirbt and Heinrich Denzinger."
  - `record` (Bollandists): "Held only as this eighteenth-century quotation."
  - `uncertain[0]` and `absent_details[0]` name the Bollandists' quotation but no other.
- **Evidence:**
  - The entry's own `decided[7]` and `sources.fromTheCouncil[2]` hold canon 13 from the Bollandists (`acta-sanctorum_augusti-tomus-1-lat_1750.txt` l.74820-74827). That contradicts the brief's "only".
  - Canon 13 is held a second time. Glassberger's editors quote Salimbene's Latin quoting it: `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` l.7318-7323, "volens implere decretalem Innocentii III, quam fecit in concilio generali (Lateranensi 1215), quae sic dicit: Ne nimis Religionum diversitas gravem in Ecclesia Dei confusionem inducat, firmiter prohibemus, ne quis de cetero novam Religionem inveniat, sed quicumque ad Religionem converti voluerit, unam de approbatis assumat".
  - Phrases of canon 1 are quoted in the Leonine Aquinas (`thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt` l.30508-30510, 33675-33677).
- **Fix:**
  - Brief: "Most canons we hold come in extracts printed by two modern editors, Carl Mirbt and Heinrich Denzinger." This also drops the doubled "among our sources" (see the full text below).
  - `record` (Bollandists) note: "Also quoted, from Salimbene, in the notes of Glassberger's editors (1887)."
  - `uncertain[0]`: "... and in the quotations of canon 13 by the Bollandists and, from Salimbene, by Glassberger's editors."
  - `absent_details[0]`: the same.
  - Add Glassberger's editors' note as a `fromTheCouncil` source row ("Canon 13, as Salimbene quotes it, in the notes to Glassberger's Chronica").

**B-B5. Unsupported: "not at the council" for Jacques de Vitry.**
- **Where:** `record` (Vitry) note: "Latin crusade preacher; not at the council."
- **Evidence:** no held line says where Vitry was in November 1215. I grepped the Röhricht letters for concil/lateran/Konzil and Vitry's *Historia* for Lateran: only the two Maronite lines (l.10033, l.10744) came up, with nothing on his own presence. His letter I opens with him as "Acconensis ecclesie minister humilis" (l.5860-5861) and tells of his coming to Perugia in 1216 (l.5934-5935).
- **Fix:** "Latin crusade preacher, later bishop of Acre; no source among ours puts him at the council."

**B-B6. False absence: "No Cathar text is held."**
- **Where:** `records.json` `absent_details[10]`: "No Cathar text is held, and no Waldensian account of the council."
- **Evidence:** `doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt` l.4096-4112 prints the dualist apocryphon "Joannis et Apostoli et Evangelistae Interrogatio in coena sancta regni coelorum". Döllinger notes, l.132-140, that another text of it stands in the Carcassonne inquisition records printed in Benoist's *Histoire des Albigeois*. The same volume carries the "Errores haereticorum Catharorum" and other inquisitors' documents (contents l.231-240).
- **Fix:** `absent_details[10]`: "A Cathar or Waldensian voice on the council. Neither is held. The Library holds the Interrogatio Iohannis, a dualist scripture the Cathars used (Döllinger II), and Waldensian poems (the Nobla Leiczon), but no Cathar or Waldensian text that speaks of the council."

---

## Substantial

**B-S1. Dropped condition: canon 21's exception for Easter communion.**
- **Where:** brief, paragraph 4: "...and to receive communion at Easter."
- **Evidence:** `mirbt...1911.txt` l.12401-12403: "suscipiens reverenter ad minus in Pascha eucharistiae sacramentum, nisi forte de consilio proprii sacerdotis ob aliquam rationabilem causam ad tempus ab eius perceptione duxerit abstinendum". The brief drops both "at least" and the priest's exception. `decided[5]` has both right.
- **Fix:** split the 30-word sentence: "Another canon bound every believer past the age of discretion to confess all their sins at least once a year to their own priest. They were to take communion at least at Easter, unless that priest advised a pause." This is in the full brief text below, inside the cap.

**B-S2. Dropped condition: canon 3's visitation of parishes where heretics are reported.**
- **Where:** `decided[2]`: "Bishops were to visit their parishes once or twice a year and put men on oath to name heretics".
- **Evidence:** `mirbt...1911.txt` l.12366-12370: "bis aut saltem semel in anno propriam paroehiam, in qua fama fuerit haereticos habitare, circumeat et ibi tres vel plures boni testimonii viros ... iurare compellat". As written, the entry reads as a general visitation, when the canon sets an inquest where heresy is reported. `claims[22]` has it right.
- **Fix:** "Bishops were to go, twice or at least once a year, through any parish where heretics were said to live, and put three or more men of good name on oath to name them".

**B-S3. A manufactured contest: what canon 13 forbade.**
- **Where:** `uncertain[5]`: "the Bollandists' quotation forbids any new religious order; Salimbene reads it as a ban on new orders of mendicants". Also `contested_claims[5]`.
- **Evidence:** Salimbene himself, as Glassberger's editors quote his Latin (p. 262 of the Parma edition), gives the canon's general wording: "ne quis de cetero novam Religionem inveniat" (`glassberger...1887.txt` l.7318-7323). He applies it to the new mendicant groups that Gregory X suppressed at Lyon. Coulton's passage (`salimbene...coulton1907.txt` l.13490-13493) is Salimbene's summary elsewhere. One writer's summary and the same writer's quotation are not two sides.
- **Fix:** `uncertain[5]`: "What canon 13 forbade: the Bollandists and Salimbene, as Glassberger's editors quote him, give its wording, that no one is to found a new religious order. In another passage, in Coulton's English, Salimbene summarizes it as a ban on new orders of mendicants." Recast `contested_claims[5]` to match, or move it to `claims`.

**B-S4. Witness kind: Joachim is not a "participant".**
- **Where:** `record` (Joachim) kind "participant"; `claims[32]` and `claims[34]` `witness_kind` "participant".
- **Evidence:** the pattern defines participant as "a letter or account by someone who was there or who called it". Joachim died in 1202 (`ehrle-denifle...bd1...1885.txt` l.3351, per the rescore). His letter is dated 1200 (`acta-sanctorum_maii-tomus-6-lat_1739.txt`, "anno Dominicae Incarnationis millesimo ducentesimo", the right column after l.80685).
  - Era 4 met the same case. Columbanus's letters, sixty years before Whitby, were filed as a later narrative with a note, and the pattern gap is registered: Open-Gaps 266, "Pattern gap: no witness kind fits a writer earlier than the meeting" (2026-11-14).
  - The `sources` already file Joachim under `writtenLater`, so the record contradicts its own sources list.
- **Fix:** kind "later narrative". Note: "The condemned party's own voice, written before the council; not a witness to it. The letter is the one canon 2 cites." Set `witness_kind` to "later narrative" in `claims[32]` and `claims[34]`. Cite the era 4 pattern-gap entry in the era 5 Open-Gaps entry.

**B-S5. Pattern order: what was at stake comes after the record and the attendance.**
- **Where:** brief. The stake, Hethum's "to tear Jerusalem from the hands of unbelievers", is paragraph 3 and sentence 10. Before it come the record (no account, the canons, Mirbt's dates) and the attendance (Hethum's count, the Maronites).
- **Evidence:** pattern, "The brief": "What was at stake follows within the first few sentences". The order is: "The scene. What was at stake and who called the meeting. Whose account we have ... Who came, from where."
- **Fix:** move the stake to paragraph 2 and put the record, then who came, after it. See the full text below.

**B-S6. Census differences, to register in the era 5 Open-Gaps entry.**
- `latin-papal-church-gregorian` `documentedStories[1].text`: "attended by more than four hundred bishops and eight hundred abbots, legislated in seventy-one constitutions". No held line gives 800 abbots or 70 or 71 constitutions. My grep over every Lateran-bearing file found none. The held counts are Hethum's 422 bishops and 72 archbishops and al-Duwayhi's 411 bishops. The records name the census in `contested_claims[0]` and `absent_details[1]`, but nothing yet carries it to Open-Gaps.
- `maronite-christianity` (`why`, `documentedStories[0]`) says the patriarch "traveled to Rome ... to settle its terms", "received the pallium from Innocent III, and returned with the bull Quia divinae sapientiae". "To settle its terms" rests on no held line. The pallium rests on al-Duwayhi alone, read as a second witness (`duwayhi...1890.txt` l.9494-9496). The bull is not held (grep "Quia divinae sapientiae": no hit).
- Parties with no census tradition at that date:
  - **The Irish bishops.** The Four Masters, l.16099-16108, and the Annals of Ulster, l.16505-16513: `medieval-irish-christianity` ends in 1169, and no era 5 Irish entry exists.
  - **Dominic's preachers.** They are "Gathered" in 1215, under `the-dominican-order`, whose census start is 1216.
  - Covel (`covel...1722.txt` l.4915-4918) also says two Latin patriarchs, of Constantinople and Jerusalem, sat at the synod. There is no census row for the Latin church of Constantinople; `latin-church-of-outremer` covers Jerusalem but is not in `traditions`.
- **Fix:** carry these four items into the era 5 councils Open-Gaps entry, owner the coordinator (census text and map build), as era 4's entry 266 did.

---

## Minor

**B-M1. Brief shape: long sentences, crowded paragraphs, a doubled phrase.** Three sentences run past 25 words:
- "In the sacrament of the altar ..." (28 words)
- "Another canon bound ..." (30 words)
- "The council spared his monastery ..." (28 words)

Paragraph 2 (five sentences) holds the record, the dating, the count and the Maronites. Paragraph 4 (five sentences) holds canons 1, 21 and 3. "No account from inside the sessions is among our sources. Among our sources, its canons are ..." repeats the phrase back to back. Fix: see the full text below.

**B-M2. Item 8, first mentions.**
- "Dominic" (brief para 1; also `teaser`-free) has no place or role. The Mansi notice gives "sanctus Dominicus, Hispanus" (`innocent-iii...pl214...txt` l.1049-1050). Use "Dominic, a Spanish preacher".
- "Joachim of Fiore" has no role. The canon says "Abbas Joachim" (`denzinger...` l.13945). Use "the abbot Joachim of Fiore".
- `people` "Almaric": the notice places him at Paris ("Almaricus de viginti erroribus convictus, cum sectariis pluribus Parisiis post obitum exhumatus, combustus est", l.1056-1058). Name him "Almaric of Paris" with part "Dead; his teaching condemned in canon 2; exhumed and burned at Paris, by the notice in Mansi".
- Optional: "Augustine's" could be "Augustine of Hippo's". Jordan says only "beati Augustini, praedicatoris egregii" (`acta-sanctorum_augusti...` l.93073-93074), so leave it unless the cap allows.

**B-M3. Brief: "Joachim had submitted all his writings to Rome".** The canon says he ordered them handed over: "omnia scripta sua nobis assignari mandaverit, Apostolicae Sedis iudicio approbanda seu etiam corrigenda, dictans epistolam, quam propria manu subscripsit" (`denzinger...` l.14044-14047). His letter asks his abbots to present them after his death (`acta-sanctorum_maii...` right column, l.80654-80672). Fix: "The council spared his monastery for its sound rule, and above all because Joachim had ordered his writings judged by Rome. He asked this in a letter he signed himself."

**B-M4. Brief: rulers' oath loses "from their lands".** The canon has "quod de terris suae iurisdictioni subiectis universos haereticos ab ecclesia denotatos ... exterminare studebunt" (`mirbt...` l.12314-12316). Fix: "Rulers were to swear to drive from their lands the heretics the church named."

**B-M5. Modern editors' dates told without their names (C4).**
- `outcome[1]`: "(Vitry's letter of October 1216)". Röhricht's heading reads "I. Octob. 1216" (l.5856).
- `outcome[6]`: "By the end of March 1217". Röhricht's heading reads "Sub finem Martii 1217" (l.6112).
- `outcome[3]`: "in 1255 the commission at Anagni". 1255 is Denifle's dating (`ehrle-denifle...bd1` l.5151).
- `outcome[1]` puts "July 1216" with no witness, next to Vitry, who gives no month.
- Fix: "In a letter Röhricht dates to October 1216, Jacques de Vitry ..."; "In a letter Röhricht dates to the end of March 1217 ..."; "in 1255, by Denifle's dating, ..."; "Innocent died at Perugia in July 1216 (the notice in Mansi, after the Ursberg chronicler; Glassberger; the Assisi catalogue)."

**B-M6. "Heinrich Denzinger's headings of 1911".** `issue[4]` and the `record` note say this. Denzinger died in 1883. The held file is "editio undecima quam paravit Clemens Bannwart" (header l.1-2), and from one edition we cannot tell whose the headings are. Fix: "the headings in Denzinger's Enchiridion, in Clemens Bannwart's edition of 1911". Optionally, in the brief: "two modern source books, Carl Mirbt's and Heinrich Denzinger's" (same word count as "two modern editors, Carl Mirbt and Heinrich Denzinger").

**B-M7. The Pedalion as "modern reconstruction".** The pattern keeps that kind for an editor or historian "who supplies a date, a count or a sequence that no ancient witness gives". The Pedalion is a later canonical commentary that judges the council's standing. Fix: kind "later narrative" in `record` and in `claims[27]` and `claims[28]`.

**B-M8. `teaser` and `knownFor` are long single sentences (33 and 31 words).**
- `teaser`: "Rome, 1215. Pope Innocent III held a general council at the Lateran. Its canons set out the faith and the change of bread and wine in substance. They bound every believer to yearly confession, moved against heretics and rebuked the Greeks."
- `knownFor`: "The council of Innocent III that defined the change of bread and wine in substance and bound every believer to yearly confession and Easter communion" (25 words). Joachim is in the teaser's "heretics" only by implication; keep him in `knownFor` if preferred, at about 31 words.

**B-M9. C1 coverage: witnesses used but not in `record`.** The following are used in `attended`, `datesNote`, `calledBy` or `uncertain`, but have no `record` row with kind and side:
- the Assisi papal catalogue printed by Ehrle, which its printer identifies as Richard of Poitiers's catalogue (l.26363-26366);
- Alishan;
- Covel, who is hostile and Anglican;
- the Pulkava variant;
- Denifle's article and the Anagni protocol, which also lack a `sources` row (the file is listed only as the catalogue).

Fix: add the rows. Covel's note: "Anglican, 1722; hostile; calls it a pretended general council and says two Latin titular patriarchs sat for Constantinople and Jerusalem."

**B-M10. Close (optional).** The close is about Innocent's death and Vitry's moral, not "where it stands in later memory or what it left in place". Era 4 accepted sourced moral closes (R1 era 4, item 4 note), so this is a choice, not a fault. The held line that shows what the council left in place is Trent's eighth canon on penance: "iuxta magni concilii Lateranensis Constitutionem semel in anno" (`mirbt...` l.18263-18264). If Mark wants a council-memory close, a sentence on Trent could follow or replace the Vitry close, within the cap.

**B-M11. `issue[2]` drops the half of Lombard's sentence that carries Joachim's objection.** The canon quotes "Quoniam quaedam summa res est Pater, et Filius, et Spiritus Sanctus, et illa non est generans, neque genita, neque procedens" (`denzinger...` l.13947-13949). Fix: "...that there is one supreme reality which is Father, Son and Holy Spirit, and which neither begets nor is begotten nor proceeds."

**B-M12. `attended[4]`: "Irish bishops came."** The Four Masters say Dionysius O'Lonargan "died at Rome" (l.16103), not that he attended. Only O'Heney is tied to the council ("died on his return from the fourth General Council of Lateran", l.16104-16108), and Mac Gilluir is tied to it by the Annals of Ulster. Fix: "Irish bishops came. The Annals of the Four Masters, in O'Donovan's English, say Conar O'Heney, bishop of Killaloe, died on his way home from the council, and enter the death at Rome of Dionysius O'Lonargan, archbishop of Cashel, in the same year. ..."

**B-M13. Brief sentence 1 joins a time clause to a different event.** In Jordan, "Ingruente autem tempore, quo ad Lateranense Romam episcopi adire coeperunt" introduces two men of Toulouse giving themselves to Dominic (l.93023-93026). "Adjunctus autem eidem episcopo F. Dominicus, ut simul adirent concilium" comes a paragraph later (l.93047-93048). Both fall in the same weeks, so this is not misleading as told, and the cap leaves no room. Note it for the records: `claims[0]` cites both.

---

## Proposed brief (all brief fixes above, 400 words, FK 8.13, Flesch 62.84, longest sentence 24 words)

Checked with `grade_text` and `wc -w`. Audio: `[calmly] ` at the start and `[warmly] ` before the last paragraph, as now.

> When the bishops began to leave for Rome and the Lateran council, Dominic, a Spanish preacher, went with Fulk, bishop of Toulouse. They meant to ask Pope Innocent III to confirm an order of Preachers. Jordan of Saxony, Dominic's successor, tells it so.
>
> Innocent held the council, says Hethum of Korykos, an Armenian chronicler, to tear Jerusalem from the hands of unbelievers.
>
> No account from inside the sessions is among our sources. Most canons we hold come in extracts printed by two modern editors, Carl Mirbt and Heinrich Denzinger. Mirbt dates the council from 11 to 30 November 1215.
>
> Hethum counts 422 bishops and 72 archbishops. The Maronites kept Latin customs as a sign of obedience, Jacques de Vitry writes, and so their patriarch came.
>
> The first canon set out the faith: one universal church, outside which no one at all is saved. Christ's body and blood are truly present under the forms of bread and wine, the bread changed in substance into the body.
>
> Another canon bound every believer past the age of discretion to confess all their sins at least once a year to their own priest. They were to take communion at least at Easter, unless that priest advised a pause. Rulers were to swear to drive from their lands the heretics the church named. Preachers without leave from pope or bishop were excommunicated.
>
> The fourth canon rebuked the Greeks. They washed altars where Latin priests had said Mass, it said, and baptized again those the Latins had baptized. Nearly six centuries later, the Greek canon book called the Pedalion named this council a local synod.
>
> The second canon condemned a tract by the abbot Joachim of Fiore, who had called the theologian Peter Lombard a heretic and a madman. In another work, Joachim warns against picturing the three persons as branches on one root, which brings in a fourth. The council spared his monastery for its sound rule, and above all because Joachim had ordered his writings judged by Rome. He asked this in a letter he signed himself.
>
> Innocent told Dominic to choose a rule already approved. After the council, the brothers took Augustine's.
>
> Innocent died at Perugia the next summer. Jacques de Vitry found his body, stripped of its robes at night and left almost naked in the church. He saw, he wrote, how short and empty is the deceiving glory of this world.

---

## Verified (right as written)

Line numbers are in `cic/texts/` files, read in context.

**Brief**
- Dominic and Fulk going together to ask Innocent to confirm an order "qui Praedicatorum diceretur": `acta-sanctorum_augusti-tomus-1-lat_1750.txt` l.93047-93052.
- Innocent urging him to choose an approved rule, and "celebrato concilio" the rule of Augustine: l.93055-93074.
- Jordan as "secundo ejusdem Ordinis Magistro generali": l.92240-92242.
- "Nearly ten years": l.93020-93022.
- Mirbt's "Das vierte Laterankonzil (11.—30. Nov. 1215)": `mirbt...1911.txt` l.12278. Mirbt's canon 1 extract: l.12285-12292.
- Canon 3 in Mirbt: l.12300-12384, with no group named.
- Canon 21: l.12399-12423. Canons 23 to 26: l.12427 ff. Canon 62: l.12534-12538.
- The crusade decree (twentieth for three years, religious and crusaders excepted, the pope and cardinals a full tenth): l.12544-12550 and l.12553-12554.
- Trent, penance canon 8: l.18263-18264.
- Hethum, "Le pape Innocent [III] tint un concile général pour arracher Jérusalem des mains des infidèles; quatre cent vingt-deux évêques et soixante et douze archevêques y assistèrent", under 664 (27 janvier 1215 — 26 janvier 1216): `rhc-armeniens...1869.txt` l.54605-54612. The entry sits inside the "TABLE CHRONOLOGIQUE DE HÉTHOUM, COMTE DE GOR'IGOS" running heads. The editors' "composée en 1296": l.53306-53307.
- Vitry, Maronites "in signum obedientiae consuetudines & ritus observant Latinorum. Unde & eorum Patriarcha interfuit generali concilio Lateranensi": `jacques-de-vitry_historia...1597.txt` l.10738-10743, duplicated at l.10031-10035.
- Denzinger:
  - heading "Oecumenicum XII (contra Albigenses, Ioachim, Waldenses etc)" and "[Definitio contra Albigenses aliosque haereticos.]": l.13855-13862;
  - canon 1, church and body and blood: l.13916-13923;
  - baptism, penance, married people: l.13924-13941;
  - canon 2, the tract, "haereticum et insanum", the quaternity, the collective unity: l.13943-13962;
  - "sacro approbante Concilio, credimus et confitemur cum Petro Lombardo": l.13990-13991;
  - the defender refuted as a heretic: l.14038-14040;
  - Fiore spared, "propria manu subscripsit": l.14041-14049;
  - Almaric "non tam haeretica censenda sit, quam insana": l.14050-14053;
  - canon 3 "[Waldensibus]" paragraph: l.14058-14070;
  - canon 4: l.14074-14097, "unum ovile et unus pastor" verbatim;
  - canon 5, the patriarchal order and "mater universorum Christi fidelium et magistra": l.14105-14115.
- The Pedalion, "ἡ ἐν Λατεράνῳ τῆς Ῥώμης τοπικὴ σύνοδος, γενομένη κατὰ τὸ ασιε΄ ἔτος", canon 4 cited, "κατὰ τὴν μαρτυρίαν τῶν ἰδίων ἐχθρῶν": `nikodemos-hagiorite_pedalion...1886.txt` l.7151-7160 (left column). First printed in 1800: header Creator line.
- Vitry at Perugia, "papam Innocentium inveni mortuum, sed necdum sepultum ... Corpus autem eius fere nudum et fetidum in ecclesia reliquerunt ... quam brevis sit et vana huius seculi fallax gloria", and "Sequente autem die elegerunt cardinales Honorium": `jacques-de-vitry_briefe...1894.txt` l.5934-5941.

**Entry and records**
- The Maronite submission, "Patriarcha vero Maronitarum cum archiepiscopis et episcopis suis et populo ... catholice et obedientie sancte Romane ecclesie se subdidit": l.6802-6805.
- The notice in Mansi:
  - "ad depravatos mores populi corrigendos, ad haereticos damnandos, et principes populumque ad terram sanctam recuperandam, Lateranensem synodum oecumenicam xii indixit, eique inter cpxn [unreadable] episcopos praesedit": `innocent-iii...pl214...txt` l.1033-1038;
  - the death "ut ait Urspergensis, decimo sexto Kalendas Augusti, anno Domini 1216": l.1066-1070;
  - the notice heading "NOTITIA EX CONCILIIS (Mansi, XXII, 687.)": l.958-960.
- The Assisi catalogue, "Anno vero XVIII pontificatus sui in basilica Lateranensi celebravit concilium generale, ubi pene corpus totius universalis ecclesie convenit; et post decimo kal. augusti apud Perusinum defunctus": `ehrle-denifle...bd1...1885.txt` l.26431-26434.
- Denifle on the Decretals: l.4430-4433. The Anagni protocol, "videtur adhuc astruere heresim dampnatam in concilio Lateranensi": l.7739-7740.
- Honorius III:
  - to Lucca, "Datum Romae apud Sanctum Petrum, quarto Nonas Decembris, Pontificatus nostri anno primo" (2 December 1216): `acta-sanctorum_maii-tomus-6-lat_1739.txt` left column, l.80602-80634;
  - "per totam Calabriam faciatis publice enuntiari, quia eum fuisse virum Catholicum reputamus ... Datum Laterani, sexto Kalendas Januarii, Pontificatus nostri anno quinto" (27 December 1220): right column, l.80581-80596;
  - the address to Cosenza and Bisignano: l.80639. The interleaving caveat in `contested_claims[7]` is honest and right.
- Joachim's letter, "Hoc scriptum feci ego Joachim Abbas, & propria manu roboravi anno Dominicae Incarnationis millesimo ducentesimo": after l.80685.
- Lea, 1220 bull "expressly declaring that he was a good Catholic": `lea...v3_1888.txt` l.1008-1013. Lea on Lyon 1274, the Carmelites and Augustinians "allowed to exist on sufferance": l.1846-1858. Innocent's sermon "to the assembled fathers": l.991-992.
- Salimbene, "the Pope ordained that there should be henceforth no [new] Order of religious Mendicants: but this constitution was not kept, through the negligence of the prelates": `salimbene...coulton1907.txt` l.13489-13492.
- Glassberger, "Anno Domini 1215 concilium generale Lateranense ... ubi sanctus Franciscus sanctum Dominicum, qui cum Fulcone ... advenerat, reperit": `glassberger...1887.txt` l.2109-2112; "XVI. kalendas Augusti": l.2118-2129.
- The Bollandists' canon 13 "Ne nimia Religionum diversitas ... unam de approbatis assumat", with the link to Innocent's answer: `acta-sanctorum_augusti...` l.74814-74827.
- The Four Masters, 1215, O'Lonargan and O'Heney: l.16099-16108. The Annals of Ulster, 1216, "post generale Consilium Lateranense Rome feliciter obdormiuit": l.16505-16513. Kilronan, 1216: l.16632-16637.
- The Pulkava variant, "Anno Domini MCCXIII epistola a domino papa per orbem mittuntur de concilio convocando, que incipit: Vineam Domini Sabaoth": `laurentius-de-brezova...1893.txt` l.14998-15000; Pulkava running heads at l.13987-14751.
- Alishan, "Ce concile fut tenu le 11 Nov. 1215", called "quatrième Concile tenu à Lyon": `alishan...1888.txt` l.12465-12469.
- Covel, "the Decree of a pretended general Council": `covel...1722.txt` l.4909, in the Lateran context at l.4914-4918.
- Al-Duwayhi, 411 bishops "من الشرق والغرب" and Jeremiah, damaged OCR: `duwayhi...1890.txt` l.9488-9496. The second-witness treatment is right.
- Census:
  - all nine `traditions` ids exist in `movements`, with names matching;
  - `innocent-iii` exists with kind `person`;
  - `modernCountries` is copied exactly from `latin-papal-church-gregorian`;
  - `rivers` matches the major-councils table (`Councils_Scan.md` l.76: Latin West, Syriac East).
- People verdicts against the Who scan and rescore:
  - Innocent III: STORY (Rescore l.51, l.171).
  - Dominic: WHO (Rescore l.188).
  - Francis: WHO (Who_Scan_Era5 l.30).
  - Joachim: WHO (Rescore l.193).
  - Jeremiah: LISTED (Who_Scan_Era5 l.115).
  - Fulk, Almaric, Honorius III and the Irish bishops: no row in either file, so NOT SCORED is right.
  - Ids are given only where a census entry exists, which is right.
- Form: field order and the bare-string style (no closing period) match era 4. The empty `fromThoseThere` group is left out, as in the Quinisext entry.

## Searches run (absence claims)

- **Canon text beyond Mirbt and Denzinger.** Grep over all `cic/texts/` for "utriusque sexus", "Firmiter credimus", "nimia religionum", "religionum diversitas", "Damnamus ergo", "Antiqua patriarchalium", "Licet Graecos", "Excommunicamus et anathematizamus", "In nonnullis provinciis". Found: canon 13 in the Bollandists and in Glassberger's editors' note (B-B4); canon 1 phrases in the Leonine Aquinas. The other hits are later bulls citing the incipits.
- **Canons 67-70.** Grep for "qualitate habitus", "Quanto amplius christiana", "Cum sit nimis absurdum", "Quidam qui ad baptismi", and Lateran with Jews/Juifs/Juden/Iudae on one line: none. `absent_details[1]` holds.
- **Mansi 22 and Hefele V.** Mansi tomus 21 is the nearest held; Hefele is held only to vol. 3 (English) and vol. 1 (German); Hefele-Leclercq only tome 1-1 and 2-1. Holds.
- **Inside accounts.** No file for Wendover, Matthew Paris before 1240 (only vol. IV, 1240-1247, is held), Richard of San Germano, Burchard of Ursberg, Peter of Vaux-de-Cernay, William of Puylaurens or the Canso. The name hits are citations. The Ursberg chronicler reaches us only through the Mansi notice. `absent_details[2]` holds.
- **Lateran IV in 13th-century Dominican and other texts.** Found Gerard de Frachet, Latin and English, which led to B-B1. Stephen of Bourbon l.13451 and Bernard Gui l.4901 concern an earlier Roman council on the Waldenses.
- **800 abbots or 71 constitutions.** Grep for octingent-/800/eight hundred/huit cents with abbots, and seventy-one/71 with canons or constitutions, over every Lateran-bearing file: none. `absent_details[5]` holds.
- **"Vineam Domini Sabaoth" (1213).** Only the Pulkava variant and unrelated later uses (Clement XI, 1705). Holds.
- **"Quia divinae sapientiae".** No hit. Holds.
- **"Desiderio desideravi hoc pascha"** (Innocent's opening sermon). Hits are other works, none Innocent's. `absent_details[7]` holds.
- **Joachim's tract "de unitate seu essentia Trinitatis".** Found only Denzinger's canon and the Acta Sanctorum quotation, no text of the tract. Holds.
- **Cathar texts.** Found the Interrogatio Iohannis and the Errores Catharorum in Döllinger II (B-B6).
- **Raymond VI and Simon de Montfort at the council.** Perrin, van Braght and Lea mention them, but not at the Lateran council in 1215. Holds.
- **A Greek writer of the time.** Grep "Λατερ" in Greek files: only the Pedalion and an unrelated Chalcocondyles line. Holds.
- **Vitry's presence.** Grep concil/lateran/Konzil in the Röhricht letters: nothing on 1215. Grep Lateran in the *Historia*: only the Maronite lines (B-B5).

## Counts

- Blocking: 6 (B-B1 to B-B6)
- Substantial: 6 (B-S1 to B-S6)
- Minor: 13 (B-M1 to B-M13)

---

## Council profiles, era 5: review round 1, Part C

**Council.** `second-council-of-lyon-1274` (Second Council of Lyon, 1274).

**Files reviewed.** In `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/`: `second-council-of-lyon-1274.brief.txt`, `audio/second-council-of-lyon-1274.audio.txt`, `second-council-of-lyon-1274.entry.json`, and the `second-council-of-lyon-1274` key of `records.json`. Branch `claude/cft-councils-era5`. `cic/texts/` has no diff from origin/main. No repo file was edited.

**Brief as drafted.** 396 words (about 2:28 at 160 wpm). FK 8.04, Flesch 65.25 (`engine.m1.gates.grade_text`). Longest sentence 37 words (the close). Audio script equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag: checked by script.

**Brief with the fixes below.** Scratch copy: `/tmp/claude-0/-home-user-CIC-Project/ae522d88-ff95-54e2-81c3-aaef67a4f314/scratchpad/R1C/second-council-of-lyon-1274.fixed.txt`. 392 words, FK 8.02, Flesch 64.06, longest sentence 26 words.

**Standard.** `Council_Profile_Pattern.md` C1 to C8, with `Who_Profile_Pattern.md` items 1 to 9, 11 and 13. Form compared with the era 4 entries (field order matches `lateran-council-649.entry.json`).

**Verdict.** NOT YET: two blocking findings (a wrong date range for the Greek witnesses, told in the brief, and a false absence on Michael's motive in the records and entry), four substantial, nine minor. Every quotation is verbatim. Readability and audio pass.

---

## Blocking

**C-B1. The Greek witnesses are dated "1400s and later"; a held Greek witness was written about 1300, and another is dated by its held editor to the 1300s.** (Items 1 and 7; also a near-false absence.)

- Where: brief, paragraph 2: "No Greek account from the time is among our sources. The Greek side reaches us from writers of the 1400s and later." Entry `uncertain[0]`: "the Greek side, both for and against the union, reaches us from writers of the 1400s and later." `records.json`, `absent_details`, "A Greek account from the time": "the Greek witnesses held date from the 1400s on."
- Evidence 1, the patriarch list that the profile itself uses for Joseph and Bekkos. It is Nikephoros Kallistos's catalogue of the patriarchs ("Anselmi Bandurii ad Nicephori Callisti Catalogum observationes", `nicephorus-callistus_historia-ecclesiastica-with-hesychast-tracts-pg147-grc-lat_migne1865.txt` l.283-284; heading "NICEPHORI CALLISTI ENARRATIO DE EPISCOPIS BYZANT.", l.21339). It ends with John XII and the return of Athanasios under Andronikos II (Latin l.21320-21328; Greek l.21391-21402), and closes its count "anno 6800 [Christi 1292]" in Migne's Latin (l.21330-21336). It calls Andronikos "τοῦ εὐσεβεστάτου βασιλέως ᾿Ανδρονίκου" (OCR "εὗσεδεστάτου ... ᾿Ανδρηνίχου", l.21376-21377), as a living ruler. The profile names it only as "the patriarch list printed in PG 147", without its author or date, and then counts it among writers of the 1400s.
- Evidence 2, Kalekas. His held editor, Fabricius in Harles, says "vixit non tempore concilii Lugdunensis a. 1274, sed post errores a Palama disseminatos ... adeoque circa ann. 1560 [OCR; after Palamas, so the 1300s]" (`calecas_opera-omnia-pg152-grc-lat_migne1866.txt` l.367-369). The codex note gives his death in 1410 (l.388). Only his death falls in the 1400s.
- Evidence 3: Gregory Palamas's answers to Bekkos's pro-Latin florilegium, the "ἀντεπιγραφαὶ" to "τὰς παρὰ τοῦ Βέκκου ὑπὲρ Λατίνων ... χρήσεσιν" (`palamas_opera-omnia-pg150-grc-lat_migne1865.txt` l.52640-52649), are a held Greek text of the 1300s against the union's doctrine.
- "From the time" can stand: none of these is of 1274-1282. "1400s and later" cannot.
- Fix, brief paragraph 2: delete "No Greek account from the time is among our sources." and replace "The Greek side reaches us from writers of the 1400s and later." with "The Greek side reaches us from later writers, from about 1300 on." (Net -10 words; the deleted sentence is carried by the new one.)
- Fix, `uncertain[0]`: "...No Greek account from the time is among our sources; the Greek side, both for and against the union, reaches us from later writers, the earliest the patriarch list of Nikephoros Kallistos from about 1300."
- Fix, `absent_details` note: "None among our sources; Pachymeres, Akropolites and Gregoras's first volume are not held. The earliest held Greek witness is Nikephoros Kallistos's patriarch list, from about 1300; Kalekas dates from the later 1300s (died 1410); Gennadios, Doukas and the Sphrantzes chronicle are later."
- Fix, `record` and `sources`: name the list's author. `record` witness: "Nikephoros Kallistos's list of the patriarchs (PG 147)", note "Greek, against the union; written about 1300, under Andronikos II; Migne's Latin mistranslates Joseph's line, so the Greek is followed." `sources` entry: title "The patriarchs of Constantinople", author "Nikephoros Kallistos, in Migne, PG 147". Elsewhere the entry may keep "the patriarch list" as the short form once the author is given.

**C-B2. False absence: "no held witness says" Michael sought help from the West. The Recueil editors, cited by this profile for the next sentence, say so.** (Brief rule 4, a false absence; C5; census check.)

- Where: `records.json`, `contested_claims`, "Michael VIII's motive": "The census tradition entry byzantine-church-after-1054 says he needed help from the West; no held witness says so." Entry `uncertain[6]`: "the later witnesses say he wished to ward off a Western attack; none of them says he sought help from the West."
- Evidence: `rhc-armeniens_documents-armeniens-t2-latins-et-francais-fra_academie1906.txt` l.54168-54172: "Les Grecs, espérant se concilier la faveur et l'appui des princes d'Occident, se rendirent au concile de Lyon en 1274, abjurèrent le schisme et reconnurent la suprématie du Pape." The profile cites l.54172-54180 of the same note for the 1277 signature and the 1281 excommunication, two lines below.
- The entry's sentence is true only of the medieval witnesses, and it says nothing to show that a held modern editor takes the census's side. The records' sentence is false as written.
- Fix, records `sides`: add "To win the favor and support of the Western princes: the Recueil editors, modern (rhc-armeniens_documents-armeniens-t2-latins-et-francais-fra_academie1906.txt l.54168-54172). The census entry byzantine-church-after-1054 ('needed help from the West') follows this modern view; no held medieval witness says it." Raise the claim's `formation_confidence` to Contested.
- Fix, `uncertain[6]`: "Michael's motive: Gennadios, the Sphrantzes chronicle and the Directorium say he wished to ward off the Latins' revenge or Charles of Anjou's attack. The Recueil editors, modern, say the Greeks hoped to win the Western princes' favor and support."

## Substantial

**C-S1. The mendicant-orders decree is told from a chronicler of 1508 and a pope of 1773. A contemporary held witness, Salimbene, is left out, and the witnesses disagree without a flag.** (C5, item 7, rule 2 "acts versus later narratives".)

- Where: entry `decided[3]`; `traditions` (the Carmelites); `absent_details` note, "the mendicant decree is known through Glassberger, Clement XIV and Lea".
- Evidence, Salimbene, a Franciscan who lived through it. Coulton's English: "Pope Gregory X in full Council at Lyons [a.d. 1274] had forbidden their further multiplication" (of Segarelli's Apostles, `salimbene_from-st-francis-to-dante_coulton1907.txt` l.16092-16094). Coulton reports that Salimbene held Gregory "divinely inspired in abolishing the Order" of the Sack (l.15763-15766). Salimbene also says of Gregory, "In 1274 he celebrated a General Council at Lyons, wherein he appeared truly holy, for there he ordained many good constitutions" (l.13617-13619). Glassberger's own editors quote Salimbene's Latin: "Gregorius X. cassavit in concilio Lugdunensi Religiones mendicantes, quae noviter apparuerant, ut Saccatorum et istorum ribaldorum, qui se appellabant Apostolos" (`glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` l.7323-7325). Eubel's note says the Sack friars were "in concilio Lugdunen. secundo suppressis" (`bullarium-franciscanum_v5-lat_eubel1898.txt` l.14488-14489).
- The disagreement. Glassberger: only two mendicant orders, "aliis omnibus cassatis, donec aliud de ipsis ordinaretur" (l.7301-7305). Clement XIV: only those founded after Lateran IV "qui nullam confirmationem sedis apostolicae meruerunt" were banned (`mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` l.23010-23015). Lea: the Carmelites and Augustinians "were allowed to exist on sufferance until further order", and confirmed orders "were permitted to continue" (`lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt` l.1856-1862). The entry sets Glassberger and Clement XIV side by side and does not say that they differ.
- Fix, `decided[3]`: "On the mendicant orders, the text of the decree is not among our sources. Salimbene, a Franciscan of the time, says in Coulton's English that Gregory forbade new orders such as the Sack friars and the Apostles. Glassberger says only the Friars Minor and the Preachers were kept, the others dissolved until something else was ordered. Clement XIV in 1773 says Gregory banned for ever the mendicant orders founded after the Fourth Lateran Council without the apostolic see's confirmation, and Lea says the Carmelites and Augustinians were left on sufferance (see uncertain)."
- Fix: add to `uncertain`: "What the mendicant decree did: Glassberger says all orders but the Minors and Preachers were dissolved; Clement XIV and Lea say it struck only unconfirmed orders, and Lea that the Carmelites and Augustinians were left on sufferance." Add a matching `contested_claim`. Add Salimbene to `record` (later narrative; Franciscan, of the time, in Coulton's English), to `sources.writtenLater` (`cic/texts/salimbene_from-st-francis-to-dante_coulton1907.txt`, English), and to the `absent_details` note: "known through Salimbene (in Coulton's English and in Glassberger's editors' Latin), Glassberger, Eubel, Clement XIV and Lea."

**C-S2. Pattern breach: Tocco's Life and the canonization depositions are filed under `fromThoseThere`.** (Pattern, the entry's `sources` field: "`fromThoseThere` (participants' own accounts)"; C1.)

- Thomas never reached the council: he fell ill at Maenza and died at Fossanova (`acta-sanctorum_martii-tomus-1-lat_1735.txt` l.112359-112366 and l.114090-114111). Neither Tocco nor the deponents of 1319 was at Lyon. The profile's own `record` gives both the kind "later narrative".
- Fix: move the entry to `sources.writtenLater` and leave `fromThoseThere` out, as the pattern says for a field with no content ("A missing field is absent, never filled").

**C-S3. Census differences on this council are not flagged for Open-Gaps.** (Brief step 5.)

`cic-website/data/world-census.json`, `byzantine-church-after-1054`, differs from the profile in four places. `Open-Gaps.md` has no Lyon entry, and the one records note on the first point is itself wrong (C-B2).
- `why` and `longDescription`: "In 1274 Emperor Michael VIII needed help from the West". This is a held modern editor's view, not a medieval witness's (C-B2).
- `sourcing`: "Rich: ... Lyons 1274 acta". The acts are not held, only three texts in modern extracts (`absent_details`, "The full acts (Mansi tomus 24)").
- `documentedStories`, "Michael VIII Punishes the Anti-Unionists": it rests wholly on Pachymeres and Michael's autobiography, neither held, marked "from reference summaries; primary text not yet read". It says "the Byzantine church refused the emperor a Christian burial". The held witnesses differ among themselves: Boulliau says he was denied funeral pomp and the usual honors (`doukas_historia-byzantina-grc-lat_bekker1834.txt` l.32499-32501); Creyghton says he was cast out unburied, with earth heaped on him (`syropoulos_vera-historia-unionis-non-verae-grc-lat_creyghton1660.txt` l.3090-3094); Guillaume Adam says the monks made Andronikos swear never to let him be buried (`rhc-armeniens...` l.63744-63748). None of them says the church refused it.
- The same story's "with the exception of a compliant patriarch" sits beside the profile's Recueil note that Bekkos at first resisted and was imprisoned (`rhc-armeniens...` l.63805-63812).
- Fix: add one Open-Gaps entry, "Census: byzantine-church-after-1054 and the Second Council of Lyon (2026-11-15)", listing the four points with these lines. In `records.json` keep the motive point with C-B2's wording.

**C-S4. The brief names roles in place of witnesses.** (Item 5: "No role standing in for a named witness ('his editor', ...)"; item 6.)

- Brief paragraph 4: "...in 1267, Denzinger's editor notes." The editor is Clemens Bannwart (`denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` l.1-2), and the entry names him.
- Brief paragraph 7: "A later Greek chronicle says..." The entry names it "the chronicle printed under Sphrantzes's name". This is the witness for the floggings, and it is hostile to Michael (`record`), so the listener needs its name.
- Fix, paragraph 4: "Michael VIII, emperor at Constantinople, sent a profession of faith. Clemens Bannwart, Denzinger's editor, notes that Pope Clement IV had first put it to him in 1267." (This also gives Michael his place at first mention; see C-M5.)
- Fix, paragraph 7: "The chronicle printed under Sphrantzes's name says Michael flogged, ill-treated and exiled many who resisted." (See C-M1 for "ill-treated".)

## Minor

**C-M1. "Maimed" follows the Latin version, not the Greek.** Brief paragraph 7 and entry `outcome[1]`. The Greek has "τῶν μὴ πειθομένων πολλοὺς ἐμαστίγωσε καὶ ἐκάκωσε καὶ ἐξώρισε" (OCR "ἐκάχωσε", "ἔξώρισε"; `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt` l.1259-1260). ἐκάκωσε is "ill-treated, harmed", and the Latin's "multos flagellavit vel mutilavit vel eiecit" (l.1290) narrows it. Fix: "flogged, ill-treated and exiled", in the brief and in `outcome[1]`, and in the records claim (l.1255-1260).

**C-M2. Creyghton's "non ita nuper" is reversed.** Entry `attended[1]`: "Germanos, not long before patriarch". Creyghton: "Germanum non ita nuper Patriarcham; qui medius inter Arsenium, & Josephum primum intercedens" (`syropoulos_vera-historia-unionis-non-verae-grc-lat_creyghton1660.txt` l.3061-3063). "Non ita nuper" means "not so recently". Fix: "and Germanos, who had been patriarch some years before, between Arsenios and Joseph."

**C-M3. Doukas is cited for "a union on Latin terms", which his line does not say.** Entry `uncertain[8]` and the records contested claim "What Lyon decided, in later Greek memory". Doukas (`doukas_historia-byzantina-grc-lat_bekker1834.txt` l.14310-14316) sets "ἡ ἐν τῷ Λουγδούνῳ γενομένη σύνοδος" beside Florence, as unions sworn with oaths and anathemas. He says nothing of their terms. Fix, `uncertain[8]`: "Gennadios remembers it as a union on Latin terms, and Doukas sets it beside Florence as a union sworn under oaths; a unionist dialogue has an opponent claim it condemned the Latins and that the acts were corrupted."

**C-M4. The close runs to 37 words and uses "Lyons" outside the quotation marks.** Brief, last paragraph. Elsewhere the brief and entry say "Lyon" (item 9). Fix: 'In 1870 the First Vatican Council looked back to Lyon. With that council's approval, it said, "the Greeks professed that the holy Roman Church enjoys supreme and full primacy and pre-eminence over the whole Catholic Church."' This keeps "with the approval" ("Approbante vero Lugdunensi concilio secundo", Mirbt l.26478) and the full quote. 10 + 26 words.

**C-M5. Names at first mention without their place.** (Item 8.) "The emperor Michael VIII" (paragraph 4) and "Patriarch Joseph" (paragraph 7). Fix: "Michael VIII, emperor at Constantinople" (in C-S4's fix) and "Patriarch Joseph of Constantinople refused it and lost his throne." With C-B1's cut and the drop of "solemn" before "Mass" (paragraph 1; Glassberger's "Missarum solemnia" needs no gloss), the fixed brief is 392 words.

**C-M6. Paragraph 3 holds four ideas.** The opening day, the dream, Kalekas's count and Thomas's journey are in one paragraph. Fix: start a new paragraph at "Manuel Kalekas, a Greek who sided with the Latins...". This keeps the order of the pattern: who called it, then who came.

**C-M7. "Set out in Lent" goes further than the deponent.** Entry `attended[5]` and the records claim at `acta-sanctorum...` l.116095-116100. The witness is asked when the herring at Maenza happened, and answers that it was while Gregory "erat Lugduni, et convocabat Concilium, ad quod Concilium dictus Frater Thomas vocatus ibat ... fuit tempore Quadragesimali". Lent dates the stay at Maenza on the road, not the departure. Fix: "Thomas Aquinas was summoned and was on the road in Lent, by a witness at his canonization, when he fell ill at Maenza (Tocco's Life; the deposition of Nicholas, abbot of Fossanova)."

**C-M8. Small precision in `decided[1]` and `outcome[7]`.**
- `decided[1]`, "the eucharist made from unleavened bread": the profession says the Roman church makes it so, "Sacramentum Eucharistiae ex azymo conficit eadem Romana Ecclesia" (Denzinger l.14610-14611). Fix: "...seven sacraments, that the Roman church makes the eucharist from unleavened bread, and the supreme and full primacy...".
- `outcome[7]`: "The house of the Sack friars at Oxford was left at the apostolic see's disposal". Clement V's bull says the house "a dictis fratribus sit in brevi ut creditur relinquendus, in dispositione sedis apostolicae ... remansurus", and grants it to the Franciscans (`bullarium-franciscanum_v5-lat_eubel1898.txt` l.14399-14409). Fix: "In 1309 Clement V gave the Oxford Franciscans the Sack friars' house, which was expected soon to fall to the apostolic see under Gregory's constitution."

**C-M9. Records hygiene and labels.**
- The records contested claim "Whether Manuel Kalekas was at Lyon" carries "per the dossier ... not rechecked". Both lines are now rechecked and hold: Creyghton, "Manuel Callecas in Lugdunensi secunda acerrimus Latini dogmatis propugnator" (`syropoulos...` l.2288-2289), and Stewart's note, "si Caleca concilio Lugdunensi interfuit, ut scribit Galesinius" (`calecas...` l.17894-17895). Fix: delete "per the dossier," and ", not rechecked".
- `traditions`, the Dominican Order as "Gathered": its one member in the record never arrived. Glassberger also has the pope charge "praecipue Fratribus Minoribus et Praedicatoribus" with preaching the cross (l.7291-7293). Fix: part "Affected", note "Thomas Aquinas was summoned with his book against the Greeks and fell ill on the way (Tocco's Life); the pope charged the Preachers, with the Minors, to preach the cross (Glassberger)."
- `informalName`: "The general council of Lyon" is the plain name, not another name in use (compare era 4 LAT-6). Fix: leave the field out.

---

## Verified (found right)

Quotations, verbatim:
- Brief close: "the Greeks professed that the holy Roman Church enjoys supreme and full primacy and pre-eminence over the whole Catholic Church" (`schaff_creeds-of-christendom-v2-greek-latin-creeds_1878.txt` l.23523-23528; "su-/preme", "pre-/eminence" joined at line breaks). The Latin is at Mirbt l.26478-26480.
- The entry has no other direct quotation. Its paraphrases were checked as facts below.

Brief facts:
- The envoys' arrival before the end, the prelates half a league out, the kiss and tears, the Creed sung three times with the article on the procession, and John of Balastri as the friar-interpreter who taught them: Glassberger l.7245-7255.
- Glassberger writing in 1508: l.106 ("Occupatus erat in scribendis his Chronicis an. 1508, ut scribit pluries") and l.3988.
- The opening on the feast of Philip and James and the dream: l.7157-7163. The editors' "1 Maii": l.7205. The Order's chronicle, "mense Maio": l.7154-7155.
- Kalekas, "quadringenti ferme episcopi", and the envoys standing in for Constantinople: `calecas...` l.15002-15006. Died 1410: l.388. A Dominican: l.367-368.
- Thomas and the book written at Urban's order against the Greeks: Acta Sanctorum l.112359-112366. Ill at Maenza, a month at Fossanova: l.114090-114111.
- The constitution, "non tanquam ex duobus principiis, sed tanquam ex uno principio", and its condemnation "sacro approbante Concilio": Denzinger l.14482-14502.
- Bannwart's note on 1267 and Clement IV: l.14515-14517.
- Ubi periculum: ten days, one closed conclave, three days and then five days of one dish, then bread, wine and water: Mirbt l.13355-13387. The brief's "eight days" is 3 + 5, from the acts.
- Bonaventure's death during the council, and the Greeks and Latins following the bier "amaris ... lacrymis": Glassberger l.7281-7289.
- Gennadios on the deceit by oikonomia, the envoys bringing "Λατινισμὸν προφανῆ", the fear of the Latins' revenge for the city, safety for himself and his children, and the "μεγάλης καὶ λαμπρᾶς συνόδου" that overturned "ἡ ἐν Λουγδούνῳ πρᾶξις": PG 160 l.67359-67379.
- Joseph's refusal and loss of his throne: Synaxaristes l.24169-24174 ("παραίτησε τὸν θρόνον"); PG 147 l.21368-21371 ("διὰ τὴν ἕνωσιν τῶν Λατίνων ἐκβάλλεται παρὰ τοῦ βασιλέως Μιχαήλ"). Migne's Latin, "quod cum Latinis junctus esset", is a mistranslation, as the records say (l.21296-21297). The brief's order, the refusal told after the envoys' return, holds: Ducange gives the first withdrawal as 11 January 1274, and Possinus puts sixteen months between it and Bekkos's creation (`gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt` l.38329-38342).

Entry and records facts:
- Jerome of Ascoli's mission to the Greeks and Tatars: Glassberger l.7095-7099. Elected minister general at the Lyon chapter while still away: l.7166-7169.
- The three Franciscan presidents, "ex iussione domini Papae praesidebant": l.7173-7177. Eubel on Paul of Tripoli and Eudes: `bullarium...` l.91098-91107. Bonaventure's death on 15 July 1274, "cum concilio Lugdunen. praesideret": l.91358-91360.
- The Tatar envoys and the baptism: Glassberger l.7272-7275. The crusade charge, "Si mentes fidelium": l.7291-7293. Boniface VIII and the Augustinians and Carmelites: l.7330-7332. The Greeks' recognition of the primacy and relapse: l.7254-7255. Bonaventure's sermon on Baruch 5: l.7255-7275.
- The canonization witness on Gregory convoking the council: Acta Sanctorum l.116095-116100.
- Michael's profession: purgatory, the seven sacraments, azymes, primacy and its judgment on questions of faith (Denzinger l.14506-14634).
- The Sphrantzes chronicle on the three heads, oikonomia not innovation, and Pope Alexander and Baldwin and Charles: l.1205-1260.
- The Directorium in Miélot's French on Charles and Peter of Aragon: `rhc-armeniens...` l.54214-54225. The 1332 date: l.13391. The Recueil editors on 1277 and on 18 November 1281: l.54172-54180.
- Guillaume Adam on the patriarch sent to Lyon: l.63721-63722, dated 1317 by its editors (l.17238). The burial oath: l.63744-63748. Bekkos as the envoy: index l.94775-94780 and intro l.17950-17952. The note on Bekkos's resistance: l.63805-63812.
- The Athonite martyrs: Synaxaristes l.10268-10271 and l.47818-47828. Meyer's doubt and the Catalan suggestion: `athos-monasteries...` l.2917-2939.
- Boulliau on the funeral: Doukas l.32497-32501. Creyghton on 7 May, the envoys, "proximo mense" and the unburied body: l.3059-3094.
- Joseph of Methone's dialogue ("Synodus illa haereticos esse Latinos statuit", "Acta adulterarunt"): PG 159 l.56894-56920.
- Ravenna 1311, "per constitutionem Gregorianam, Ubi periculum": Mansi 25 l.43552-43556 and l.43732-43746. Clement V's Oxford bull, 27 May 1309: Bullarium V l.14391-14409.
- Clement XIV: Mirbt l.23008-23015. Lea on the orders and on the military orders: l.1851-1862 and l.11518-11522.

Census:
- Every `traditions` id exists in `movements` and covers 1274: `latin-papal-church-gregorian` 1049-1300, `the-franciscan-movement` 1209-1300, `the-dominican-order` 1216-1300, `byzantine-church-after-1054` 1054-1300, `athonite-and-comnenian-byzantine-monasticism` 963-1300, `the-carmelites` 1206-1300, `military-religious-orders-templars-hospitallers` 1120-1291. Names match.
- `bonaventure` exists with kind `person`. No other people id is given, and none is owed: there is no census person or Who profile for Thomas, Gregory X or Michael VIII.
- `modernCountries` France Q142 and Lyon Q456 are copied from `the-waldensians`, `irenaeus-of-lyon` and `constantius-of-lyon`.
- The census `bonaventure` text agrees: he went with the pope to Lyon and died there during the council.
- Coverage: the Greek and Latin parties both have a tradition at 1274. The Augustinian Hermits, the Sack friars and the Apostles, all struck at or by the mendicant decree, have no census tradition. This is a note, not a fix to this profile.

People verdicts, against `Who_Scan_Era5.md` and `Rescore.md`:
- Bonaventure WHO (scan row 31). Thomas Aquinas WHO (Rescore row "Thomas Aquinas | Era5:73 | WANTED | WHO"). Michael VIII STORY (scan row 47).
- Gregory X and John Bekkos are not scored (scan, councils table, l.185). All other names are NOT SCORED, with no id. No verdict is made by the profile.

C1 to C8:
- C1 passes: every witness in `record` has a kind, and the partisan ones a side.
- C2 passes: the brief's paragraph 2 says it, once and early, and names Glassberger.
- C3 passes: the Greek opponents speak through Gennadios, the patriarch list and the Synaxaristes.
- C4 passes: Kalekas's count is his, and the 1 May is the editors'.
- C5 passes apart from C-S1. C6 passes (the constitution and the profession are told as acts of the meeting). C7 passes apart from C-S2. C8 passes.

## Searches run (absence claims)

- Greek mentions of Lyon (Λουγδ-, Λούγδ-) in all of `cic/texts/`: hits only in Routh, Bessarion PG 161 (l.91315, not Lyon II), PG 159, Gennadios PG 160, Chrysostom PG 52, the Pedalion (Irenaeus), Palamas's homilies (a 1617 imprint), PO 15 (Irenaeus), and Socrates. No Greek narrative of 1274-1282 is held. "From the time" stands.
- Bekkos (Βέκκ-, Beccus, Veccus): the Greek-relevant hits are Gregoras v2 (Ducange and Boivin notes, index), Palamas PG 150 (Antepigraphai, l.52640-52649), PG 151 (Combefis note), PG 147 (catalogue, Banduri's notes), Gedeon's patriarchal acts (a reference only, l.808), Papadopoulos-Kerameus (index). These led to C-B1.
- Pachymeres, Akropolites, Gregoras v1: no file (`ls cic/texts | grep -iE "pachym|akropol|acropol"`; only Gregoras v2 and v3). Pachymeres is quoted at second hand in Banduri's note (PG 147 l.23045-23058, on Gregory of Cyprus) and in Ducange (Gregoras v2 l.38329-38342). The absence stands.
- The acts: "Lugdun"/"Lyon" with "concil"/"1274" across all files (60 files ranked). Mirbt holds nos. 304-306 under Lyon 1274: the envoys' letter and Gregory's reply to Rudolf (l.13300-13346) and Ubi periculum. Only no. 306 is a council act. Denzinger holds the constitution and the profession only. Ehrle IV cites Mansi XXIV for the opening's three heads (l.23606-23610) and for the opinions of Bruno of Olomouc and Humbert of Romans (l.23934-23940), but holds no text of them. "Only three texts" stands.
- Decree texts ("Religionum diversitatem", "Zelus fidei", "Usurarum voraginem", "Dudum super generalis"): no text of any is held, only stray phrases ("zelus fidei" in other contexts). The letter of summons and the decrees are not held; the absence stands.
- Closing day ("17 Juli/iul/July 1274", "XVI kal. aug"): no hit for 1274. The absence stands.
- A count of bishops other than Kalekas's ("quingent", "quadringent", 400/500 bishops, πεντακόσι-, τετρακόσι-) in Glassberger, Creyghton, Salimbene, Bullarium V, the Recueil, Lea, Ehrle IV, Mansi 25, PG 159, 160 and 152: no Lyon II count (Creyghton's 412 at l.2955 is Lateran IV). "Kalekas alone" stands.
- The mendicant decree in contemporary witnesses: Salimbene (Coulton) l.13617, l.15763-15766, l.16092-16094, and the Glassberger editors' note l.7323-7328. These led to C-S1.
- Michael "seeking help from the West": the Recueil editors l.54168-54172. This led to C-B2. No medieval held witness says it (Gennadios, the Sphrantzes chronicle, the Directorium and Guillaume Adam were read).
- Dominicans at the council (Peter of Tarentaise and others): Glassberger l.7404 names Peter in a later context only. This led to C-M9's relabel.

## Notes for the coordinator (no fix to this profile)

- `Councils_Scan.md` l.77 lists `the-waldensians` among the traditions Lyon 1274 touched. No held line ties the Waldensians to Lyon II. The entry rightly leaves them out, but the table should be corrected or the omission noted.
- Paul, bishop of Tripoli, one of the three presidents by the Franciscan account, was a Latin bishop of Outremer. `latin-church-of-outremer` (1099-1291) could be listed as Gathered if wanted. This is an option, not a defect.
- The census story "Michael VIII Punishes the Anti-Unionists" rests on Pachymeres, who is not held. If the Library acquires Pachymeres (Failler-Laurent is not public domain; Bekker's Bonn edition of 1835 is), the profile's "From the time" absence would change.

## Counts

| Severity | Count | Findings |
|---|---|---|
| Blocking | 2 | C-B1, C-B2 |
| Substantial | 4 | C-S1, C-S2, C-S3, C-S4 |
| Minor | 9 | C-M1 to C-M9 |

