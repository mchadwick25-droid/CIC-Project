# Round 2 changes: era 6 council profiles (2026-11-15)

Applied by two fresh Opus fixers, one per council, each re-reading every cited line before writing. Fixes applied in corrected form are marked in each part.

## Round 2 changes, Part A — Council of Constance 1414

Files changed, all in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/`: `council-of-constance-1414.entry.json`, `council-of-constance-1414.brief.txt`, `audio/council-of-constance-1414.audio.txt`, and `records.json`, key `council-of-constance-1414` only.

How records.json was written: one Python script loaded the file and checked that `json.dumps(indent=2, ensure_ascii=False)` plus a newline reproduced it byte for byte. It then replaced the three fields in my key and wrote the file back at once. A key-by-key comparison with HEAD shows only `council-of-constance-1414` changed. `git diff` shows three hunks (l.149-150, l.653-654, l.893).

Both JSON files pass `python -m json.tool`. A script split every entry string into sentences: none runs past 25 words.

The audio file was rebuilt with mkaudio.py's own logic, run for Constance only. I did not run the script itself, because it also rewrites the Basel audio from the Basel brief, which the other fixer is editing. A `diff` of the audio, with the two tags stripped, against the brief is empty. The only tags are `[calmly]` and `[warmly]`. Nothing was committed.

Before each fix I re-read its source lines with `sed -n`.

### Substantial

**A2-S1 (the order of the last session).** Confirmed.
- MANSI27 (`mansi_sacrorum-conciliorum-collectio-tomus-27-1409-1418-lat_welter-facsimile1902.txt`), single column:
  - l.129215-129232: "SESSIO XLV. ET ULTIMA ... die Veneris, vigesimasecunda mensis ... Aprilis ... Missam de Spiritu sancto devotissime celebravit."
  - l.129232-129237: "Qua finita, & litaniis ... finitis & peractis, reverendissimus pater dominus * macello diaconus cardinalis, de mandato ipsius domini nostri totiusque sacri Concilii ... pronunciavit haec verba".
  - l.129243-129245: "Domini, ite in pace. Et responsum fuit per adstantes: Amen. Quo facto ... Joannes de Podiomitis episcopus Catanensis".
- The left column then goes on:
  - "ambonem ascendit. Antequam ... ambassiatores ... Uladislai Poloniae regis ... petierunt ... libellum ... fratris Joannis Falkemberg ... damnari" (l.129290-129305);
  - "sanctissimus dominus noster Papa dixit ... conciliariter, tenere & inviolabiliter observare volebat ... & non aliter" (l.129307-129314);
  - "dominus episcopus Catanensis fecit collationem solemnem" (l.129319-129320);
  - Cardinal de Chalant "de mandato ipsius domini nostri Papae & voluntate concilii ... quaedam decreta publice legit ... Martinus episcopus" (l.129332-129341);
  - "ipsum Concilium absolvimus ... ad propria remeandi ... licentiam impartimur" (l.129362-129370).
- The right column gives the second account. After the Mass comes "dominus Ynibaldus ... sancti Viti in Macello S.R.E. diaconus cardinalis, de mandato domini nostri Papae, totiusque sacri concilii, & consensu ... Domini, ite in pace" (l.129313-129328). The Podiomitis passage and the Polish request follow it (l.129350-129370).
- In both accounts the dismissal comes straight after the Mass. In both, the command is the pope's and the whole council's.

Entry `decided[12]` (l.57), applied in slightly different wording:

> "At the last session, the acts say, the words 'Lords, go in peace' came just after the Mass. A cardinal deacon spoke them at the command of the pope and the whole council. The Polish envoys then asked to have a book by John Falkenberg condemned. Martin V answered that he would keep what the council had decided in matters of faith 'conciliarly, and not otherwise'. After a sermon, a decree in his name dissolved the council and gave all leave to go home (Mansi)."

- Why the wording differs: the review's "the acts say, a cardinal deacon said" put "say" and "said" side by side. Putting the words first and the speaker in the next sentence reads cleanly. The facts are unchanged.
- The sentences run 17, 16, 13, 19 and 19 words.

Records claim 24 (l.149-150), applied as proposed:

> "The last session, XLV, met on Friday 22 April 1418, Martin V presiding. After the Mass the cardinal deacon of St Vitus in Macello said 'Domini, ite in pace', at the command of the pope and the whole council. The Polish request on Falkenberg, Martin V's answer, a sermon by the bishop of Catania and the reading of the dissolution decree followed"

Its witness is now `... l.129215-129246, 129280-129370`. Claim 25 (the decree) is unchanged.

**A2-S2 (Wyclif's bones).** Confirmed.
- LUTH2 l.1761-1763: "the body of Wycliff was exhumed and cremated and the ashes cast into the water (1427)." This is note [22] of the 1916 editors.
- BRAGHT l.45484-45486: "forty-one years after his death, his bones, by order of the pope, were exhumed, burnt, and the ashes thrown into the water." It is part of a quotation that opens at l.45476-45477, "writes Jacob Mehrning and others", and is cited "J. Mehrn., B. Hist., pp. 737, 738".
- FOXE l.7920-7922: the heading "... TO BE BURNED FORTY-ONE YEARS AFTER HE WAS BURIED ... A. D. 1425." FOXE l.8042: "burnt his bones, and drowned his ashes".
- RAYN28 l.8015: "igne publice concremari".

Records absent detail "The burning of Wyclif's bones as carried out" (l.893), note applied as proposed:

> "The council ordered them dug up in 1415 (Mansi), and Martin V's letter of his eleventh year orders them burned (raynaldus l.7977-8019). That the burning was done is held only in later writers: Foxe, under the heading A.D. 1425 (foxe l.7920-7922, 8042); the 1916 editors of Luther's works, who date it 1427 (luther_works-v2 l.1761-1763); and van Braght's Martyrs Mirror, quoting Mehrning, 'forty-one years after his death' (van-braght l.45484-45486). No witness of the time is held."

### Minor

**A2-M1 (Benedict's reply; the cardinals' witness).** Confirmed.
- MANSI27 l.111388-111390: "Respondet idem dominus Papa, quod praedicti congregati in Constantia non sunt generalis Synodus". The words are Benedict's.
- FIN3 l.29733-29738 (no. 244, "Antwort der Kardinäle ... Peñíscola 1416 Mai 3") and l.29988-29989 ("ad congregacionem Constancie ire non possumus nee debemus").

Entry `outcome[1]` (l.61), applied in corrected form:
- "(the acts, in Mansi)" is now "(Mansi)". The review proposed "(his reply, in Mansi)", but the sentence already opens "His written reply said". The label would repeat "reply" within one sentence. "(Mansi)" names the witness without calling it the acts, and it matches the label used in `decided[12]`.
- " (Finke)" is added to the cardinals' sentence, as proposed.

The text now reads: "... His written reply said those gathered at Constance were 'not a general synod' (Mansi). Being excommunicate, he said, they did not represent the universal church. His cardinals had told King Alfonso in May 1416 that they could not and must not go there (Finke). On Maundy Thursday 1417 Benedict excommunicated all those gathered at Constance (Finke)."

**A2-M2 (the safe-conduct and Jerome).** Confirmed.
- PALUB l.2328-2332: "virum M. Joh. Hus ... sub suo salvo aut potius calvo conductu. similiter Jeronymum ... eadem crudelitatis nece jussit condemnari et exuri." The phrase belongs to Hus. Jerome is added with "similiter".

Entry `outcome[4]` (l.64), applied as proposed: "It said he had Hus condemned and burned 'under his safe-conduct, or rather his bald-conduct', and Jerome in the same way." The sentence is 20 words. "In the same way" renders "similiter ... eadem ... nece".

**A2-M3 ("his text").** Confirmed.
- RICH l.408-412: "als ob der Aulendorfer codex zwar die älteste conception unter den vorhandenen texten, aber auch ... eine um die mitte des fünfzehnten jahrhunderts gefertigte abschrift einer aus den zwanziger jahren stammenden vorlage sei."
- l.904: "Der zu gründe gelegte codex aulendorfensis (A)". This confirms that the Aulendorf codex is the text Buck prints.

Entry `record`, Richental row note (l.99), applied as proposed: "Buck judges the Aulendorf codex he prints a mid-1400s copy of an exemplar from the 1420s."

**A2-M4 (Gerson's tract date; "pluries").** Confirmed.
- GERSON l.26993-26999 has the heading "Quomodo, & an liceat in causis Fidei a Summo Pontifice appellare". It stands under the Paris chancellor's name, which is garbled in the OCR at l.26985-26987.
- l.27012-27015, the Monitum: "Scriptus est iste Tractatus Anno 1418. sub finem Concilii Constantiensis occasione appellationis Oratorum Polonorum ad futurum Concilium circa negotium Libri seditiosi Joannis Falkemberg."
- The Monitum is the editor's note. The file header names the editor: "edited by Louis Ellies Du Pin", 1706.
- l.27293: "idem Dominus noster pluries palam dixit", which is "several times in public".
- The appeal itself appears in MANSI27 l.129306-129307: "protestabantur de gravamine & de appellando ad futurum Concilium".

Records claim 108 (l.653-654), applied in slightly different wording:

> "Gerson, in a tract his editor Du Pin dates to 1418, at the end of the council, on the Polish envoys' appeal over Falkenberg's book, says Martin said several times in public that he would keep inviolably what was done 'conciliariter' at Constance"

- Its witness is now `... l.26985-27015, 27283-27294`.
- Why the wording differs: the review's line references inside the claim text are moved to the witness field, which is where every other claim keeps them. "His editor" is added so the date stays with Du Pin.

Entry `uncertain[4]` (l.381), applied in corrected form:

> "Gerson wrote a tract on the Polish envoys' appeal over Falkenberg's book. His 1706 editor, Du Pin, dates it to 1418. In it Gerson says Martin said several times in public that he would keep what was done conciliarly."

- Why the wording differs: the review's "Gerson, writing in 1418" told the date as Gerson's own, but it is Du Pin's. "The Polish appeal" also had nothing in the item to explain it.
- The sentences run 13, 9 and 20 words.

**A2-M5 (Palacký as editor, in the brief).** Confirmed.
- PALDOC l.30063-30069 is Palacký's own heading, no. 85, "Literae baronum ... sigillis 452 additis, quibus Constantiensi concilio exprobrant". It is his edition of 1869.

I diffed the scratch copy against the brief. It differs only at the three A2-M5 places. The brief now reads:
- p.8: "eight letters under 452 seals, by their editor František Palacký's count." Applied as proposed (+2 words).
- p.5: "John fled in March 1415. On 6 April the council declared that its power came directly from Christ." Applied as proposed (−1).
- p.3: "A council at Pisa in 1409 deposed two and chose a third. Neither yielded, leaving three." Applied in different form (−1).
  - The review proposed "chose a third; neither yielded". That is word-neutral too, but aloud a semicolon gives no clear stop, and the voice runs the two clauses together.
  - A full stop costs the same one word. The voice then drops its pitch on "third" and starts the next sentence fresh. It also matches the p.5 change.
  - The facts are unchanged.
- The audio file carries the same three edits.

On "their editor František Palacký's count": I read it aloud and kept it. "Their" can only mean the letters' editor, since lords do not have editors. Any clearer phrasing ("by the count of their editor, František Palacký") costs four words, not two.

### Brief after round 2

400 words. `grade_text`: FK 6.72, Flesch 70.25. Longest sentence 23 words ("We commit your soul to the devil," they said, and Hus answered, "And I commit it to the most gracious Lord Jesus Christ."). No sentence is over 25 words.

FK is below the grade 8 floor that CLAUDE.md names, as it already was before round 2 (7.03). The two sentence splits in A2-M5 lowered it further. CLAUDE.md treats grade 8 as a floor worth staying above, not a hard rule. I have not restructured the brief to raise the score, because that is outside these findings.


## Round 2 changes, Part B — Council of Basel–Ferrara–Florence 1431

Files changed: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-basel-ferrara-florence-1431.entry.json` and `records.json`, but only the key `council-of-basel-ferrara-florence-1431`. The brief, the audio and README.md were not touched.

records.json was re-read just before each write, and only this key was changed (ensure_ascii=False, indent=2, trailing newline; a round-trip of the untouched file reproduces it byte for byte). The `council-of-constance-1414` key was being edited by another thread at the same time. Its uncommitted edits were already on disk when I wrote. After my write, that key compares equal to what was on disk before. The coordinator should check that the Constance thread's next write does not overwrite this key with an older copy.

Both files pass `python -m json.tool`. Sentence check over every entry string (file paths excluded): the longest sentence is 25 words, and none is over 25. The longest sentence in the new `uncertain` item has 20 words.

Counts in records: claims 123 → 129, contested claims 21 (unchanged), absent details 12 (unchanged).

Every cited line was re-opened with sed, awk or grep in a numbered range before its fix went in. Where the review's line numbers or wording were off, the correction is given below. ALM = Almeida, Historia Aethiopiae V-VIII; MEND = Mendez, Expeditio Aethiopica I-II; both are edited by Beccari. Quotations keep the OCR spelling where the OCR differs.

### Substantial

**B2-S1 (Ethiopian sender: held witnesses; "nothing of the kind" with no antecedent).** Confirmed, with five corrections.

What was read:
- ALM l.28117-28121: chapter heading "CAPITULO XXII. Obediencia que o Emperador e todos os grandes de Etiopia derfto [derão] publicamente ao muito sancto papa Urbano oitavo nas maios [mãos] do patriarca dom Affonso Mendez". The date is at l.28124-28125: "huma quarta feira, dia undecimo de fevereiro do anno de 1626".
- **That the passage is Mendez's oration, not Almeida's own narrative.** Confirmed. At l.28174-28182 Almeida says the patriarch began "huma larga pratica, ou pregação", and that he will write "ao menos a substancia della". The heading at l.28184 is "Pratica do Patriarca no acto do juramento". From there each line of the speech carries the « mark, through l.28464-28468. At l.28514 Almeida resumes: "Em se acabando a pratica do patriarcha". So Almeida gives the substance of the oration, not a verbatim text.
- **"Patriarcha".** Confirmed, at l.28464-28465: "ao concilio Florentino forão mandados embaixadores pelo Emperador e Patriarcha, e trouxerão cartas do papa Eugenio quarto ao emperador Zara Jacob". At l.28466-28468: "o emperador David no anno 24 do seculo passado, escrevendo ao papa Clemente VII, dizia ter a dita carta em seu poder".
- LUD l.57418-57421: "Venerunt ab Imperatore & metropolita vestro Oratores ad concilium Florentinum". LUD l.56875-56877 says the text comes from Mendez's letter to the Jesuit General of 1 June 1626, printed in Italian at Rome. So "Ludolf's Latin" is a Latin version made from an Italian print.
- ALM l.7658-7697 (Almeida's own narrative): "como refere o cardeal Baronio, e dizem muitos authores gravissimos, no fim do tal concilio chegarão ali com os Armenios alguns Ethiopes ou Abexins". They made "profissão da sancta fee catholica", and "aceitarão e levarão com sigo as letras da união". He then mentions "breves do papa Eugenio", named by David in two letters of 1524. The passage ends: "nem o emperador Zara Jacob, em cujo tempo chegarão a Ethiopia as bullas do papa Eugenio, nem seus successores se mudarão, nem melhorarão do schisma". No sender is named. Beccari's Latin margin summary (ALM l.30012-30013) is a summary of Almeida, so it is not cited as Beccari's own view.
- **Innocent X's brief: the date's line number was off.** MEND l.1414-1420 is Beccari's introduction: "missae sunt novae litterae summi pontificis Innocentii X ad imperatorem Fasiladas ... (4)". Footnote (4), l.1432-1440: "Compertum vero speciatim est Aethiopiae regem Zerah oratores ad Eugenium IV ... in concilio Florentino, qui tum Ferrariae agebatur, legasse ut Aethiopicam Ecclesiam cum Romana coniungeret". The date is not inside l.1432-1440. It is at l.1450-1451: "Datum Romae apud S. Mariam Maiorem, die xxx octobris mdcxxxxv, pontificatus nostri anno secundo". The date is confirmed as 30 October 1645. The witness is now l.1414-1420, l.1432-1440 and l.1450-1451.
- **Beccari's "commentitia est": the range started late.** It is Beccari's own introduction: the running heads "INTRODUCTIO XXXI" are at l.1407 and "XXXII INTRODUCTIO" at l.1456, and the file header gives "Beccari's Latin introduction". The sentence begins at l.1420 ("Mirari, ut mitius loquar, iure"), not at l.1458. It runs on after the footnote, l.1458-1465: "merito quis posset in hoc brevi mentionem nullam fieri laborum ... eiusque loco commemorari obedientiam praestitam a Zara Iacob in concilio Florentino, quae, ut historicis notum, commentitia est." The witness is now l.1420 and l.1456-1465.
- MEND l.6748-6750 (Mendez's own text): "Cum enim ex Marci Pauli veneti peregrinatione et monachorum ad Florentinam synodum confluentium relatione agnovissent, in Oriente christianum quemdam Regem, dictum Presbyterum Ioannem". The subject is "piissimorum Lusitaniae Regum" (l.6747-6748), so the wording is "Portugal's kings", not "the Portuguese". The review gives l.6749-6750; l.6748 holds "Cum enim", so the range is l.6748-6750.
- **What "Nihil autem tale" answers.** LUD l.52403-52408 has "N° XCVII. De Legationibus Aethiopum ad Pontificem Romanum. Doctores Ecclesiae Romanae communiter scribunt; Legatos Regis Aethiopiae ... Florentiam ad Eugenium IV ... venisse". Below that, Miraeus "Zera-Iacobo attribuit" (l.52412; the OCR is poor). Ludolf then turns aside to Tzaga-Zaab's falsifications (l.52428-52432). He comes back at l.52432-52435: "Nihil autem tale in Concilio Florentino actum, sed potius Zera-Jacobum ab Ecclesia Romana alienum fuisse, testantur ipsi Patres Societatis". The Portuguese words of Susenyos follow at l.52437-52440 ("O mal aya el Rey Zera-Jacob ..."), then l.52442: "Ita Susneus Zera-Jacobum manifeste schismatis autorem facit". So "tale" answers the Catholic writers, as the review says.
- **One correction to the review's wording.** The review's proposed sentence "Ludolf denies it" (that the envoys came) goes beyond the Latin. Ludolf denies that anything of that kind was done at the council. A few lines on (l.52444) he writes "Post illa tempora nulla Aethiopica legatio Romam venit", "after those times", which reads as if he grants that an embassy came. The entry and records therefore keep his own words, "nothing of the kind was done at the council", now with a clear antecedent. Two other parts of the review's wording were not kept. Its Prester John sentence was cut to the point that bears on the sender: the monks. "The patriarch" was clarified, because Mendez himself is a patriarch.
- Zerah: "Zerah" is the brief's own name for the king. The entry says "also names the king, as Zerah", which keeps the name and makes the identification plain.

Text now in the entry:
- `uncertain`, replacing the old item: "Who sent the Ethiopians: Eugenius's letter, Patrizi and Perruchon name the emperor, Zara Yaqob. Pope Innocent X's brief of 1645, printed by Beccari, also names the king, as Zerah. Alphonsus Mendez, the Catholic patriarch sent to Ethiopia, gave an oration there in 1626. In Almeida's Portuguese of it, the emperor and the patriarch sent them. Ludolf's Latin of the same oration has "your metropolitan" instead. The oration adds that the emperor David later said he still had Eugenius's letter. Dillmann, as Perruchon reports, says Nicodemus of the Ethiopian convent in Jerusalem sent them, without the king's knowledge. Mendez's own history speaks of monks who came to the Florentine synod. Almeida's history says only that some Ethiopians came with the Armenians as the council ended. Catholic writers, Ludolf says, hold that the king's envoys came to Eugenius at Florence. Ludolf answers that nothing of the kind was done at the council. The Jesuits themselves, he says, show that Zara Yaqob stood apart from the Roman church. Beccari, the modern editor of Mendez and Almeida, says historians know Zara Yaqob's obedience at Florence to be a fiction." That is thirteen sentences of 10 to 20 words, each one claim with its witness named.
- `record`, Ludolf item: witness "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691), with a Latin version of the oration of the Portuguese patriarch Alphonsus Mendez". Note "Ludolf says Zara Yaqob stood apart from the Roman church. The oration, in his Latin, says the emperor and the metropolitan sent the envoys."
- `record`, two items added after it:
  - {"witness": "Manuel de Almeida, Historia Aethiopiae, books V-VIII (ed. Beccari), with Mendez's oration of 1626 in Portuguese", "kind": "later narrative", "note": "Jesuit history of the mission, for the Roman side. Its text of the oration says the emperor and the patriarch sent the envoys."} The review's note "For Rome." was made a little fuller, to match the Ludolf note.
  - {"witness": "Alphonsus Mendez, Expeditio Aethiopica, books I-II (ed. Beccari), with Innocent X's brief of 1645", "kind": "later narrative", "note": "The patriarch's own history. Beccari's introduction calls Zara Yaqob's obedience at Florence a fiction."}
- `sources.writtenLater`, two items appended in the existing shape:
  - {"title": "Historia Aethiopiae, liber V-VIII", "author": "Manuel de Almeida, ed. Camillo Beccari", "language": "Portuguese and Latin", "file": "cic/texts/almeida_historia-aethiopiae-liber-5-8-por_beccari1907.txt"}
  - {"title": "Expeditionis Aethiopicae liber I et II", "author": "Alphonsus Mendez, ed. Camillo Beccari", "language": "Latin", "file": "cic/texts/mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt"}
  The "ed. Camillo Beccari" follows the shape of "Odoric Raynaldus, ed. Augustin Theiner".

Text now in records (file names in full in the file):
- Mendez claim: "The oration of the patriarch Alphonsus Mendez (1626) says envoys came to Florence from the emperor and the patriarch, in Almeida's Portuguese; Ludolf's Latin has the metropolitan. They took Eugenius's letters back to Zara Yaqob, and the emperor David later said he still had them". Witness LUD l.57416-57425; LUD l.56873-56877; ALM l.28117-28125; ALM l.28184; ALM l.28464-28468. Later narrative, Contested. The review's ALM l.28117-28120 was widened to l.28125 to take in the date, and l.28184 was added for the heading that names the speech as the patriarch's.
- Ludolf claim: "Ludolf answers the Catholic writers who say the Ethiopian king's envoys came to Eugenius at Florence: nothing of the kind was done at the council, he says. The Jesuit fathers themselves, he says, show Zara Yaqob stood apart from the Roman church". Witness LUD l.52403-52408; LUD l.52431-52442. Later narrative, Contested. The review's single range, l.52405-52434, was split to skip the Tzaga-Zaab digression, and it was extended to l.52442 for Susenyos's words.
- Four claims added after it, each Contested:
  - "Pope Innocent X's brief of 30 October 1645, as Beccari prints it, says King Zerah of Ethiopia sent envoys to Eugenius IV at the council of Florence, then held at Ferrara, to join the Ethiopian church to the Roman". Witness MEND l.1414-1420; l.1432-1440; l.1450-1451. Acts, following the shape of the Lateran V and Lausanne claims, where a document's own text is tagged acts.
  - "Mendez's history says Portugal's kings learned of Prester John from Marco Polo's travels and from the report of monks who came to the Florentine synod". Witness MEND l.6748-6750. Later narrative.
  - "Almeida says, after Baronius and other authors, that some Ethiopians came with the Armenians at the end of the council, professed the Catholic faith and took back the letters of union. He says Eugenius's bulls reached Ethiopia in Zara Yaqob's time, but neither Zara Yaqob nor his successors changed or came out of the schism". Witness ALM l.7658-7697. Later narrative.
  - "Beccari, the modern editor of Mendez and Almeida, says historians know Zara Yaqob's obedience at Florence to be a fiction". Witness MEND l.1420; MEND l.1456-1465. Modern reconstruction.
- Contested claim "Who sent the Ethiopian envoys", sides now: "The emperor, called Constantine: Eugenius's letter (RAY l.49240-49247). Zara Yaqob: Patrizi, as Mansi reports (RAY l.49290-49296; l.51822-51826). Perruchon, in his own text (ZY l.552-553; l.673-674). King Zerah: Innocent X's brief of 1645 (MEND l.1432-1440; l.1450-1451). The emperor and the patriarch (Almeida's Portuguese, ALM l.28464-28468), or the metropolitan (Ludolf's Latin, LUD l.57416-57425), and the emperor David later still had Eugenius's letters: the oration of Alphonsus Mendez. Nicodemus, head of the Ethiopian convent in Jerusalem, without the king's knowledge: Dillmann, as Perruchon reports (ZY l.578-582). Consistent with it, monks who came to the synod: Mendez's history (MEND l.6748-6750). Some Ethiopians came with the Armenians at the council's end, no sender named: Almeida (ALM l.7658-7697). Nothing of the kind was done at Florence, and Zara Yaqob stood apart from Rome: Ludolf (LUD l.52403-52408; l.52431-52442). Zara Yaqob's obedience at Florence is a fiction: Beccari (MEND l.1420; l.1456-1465)." The Almeida side was added because his account names no sender, and it was read in context. Innocent X is given as his own "King Zerah" line on the emperor's side.
- `absent_details`, "An Ethiopian-side witness", second sentence now: "Ludolf (1691), Almeida and Mendez, with Beccari's introduction and Innocent X's brief, were read in context; none is an Ethiopian text of the time." The review has "Beccari's notes"; the passage read is his introduction, so the note names that.

### Minor

**B2-M1 (Glassberger range one line short).** Confirmed. GLASS l.20474-20475: "Anno igitur praedicto 1431, indictione IX, die veneris, VII. mensis Decembris, pontificatus domini Eugenii Papae IV. anno I, hora nona ...". l.20476: "celebrata est prima sessio concilii Basileensis". The records claim "Glassberger dates Basel's first session to Friday 7 December 1431" now cites `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt l.20474-20476`. The contested claim "The day of Basel's first session" now reads "Friday 7 December 1431: Glassberger (glassberger_chronica-analecta-franciscana-v2-lat_1887.txt l.20474-20476). ...", and the rest is unchanged.

**B2-M2 (weak witness line for Albergati).** Confirmed. RAY l.31494 is Mansi's note on "Nicolai tit. S. Crucis ... cardinalis Albergati discessus a Concilio" in an earlier year. RAY l.382, in the year summary at the head of the volume: "MCDXXXVIII. 1. Coepta Synodus Ferrariae, praeside Nicolao Albergato." The claim "Raynaldus says the legate Nicholas (Albergati) presided at Ferrara's first session ..." now cites RAY l.35130-35145; RAY l.382. Its text is unchanged.

**B2-M3 (Compacts: one claim, two witness kinds).** Confirmed, with a line correction. M31 l.28590-28593 holds only the head ("COMPACTATA PRAGENSIA. IN SEQUENTES TABULAS ADMONITIO P. MANSI"). Mansi's words are at l.28597-28599: "compactata cum Bohemis, ab ipsis primum concilii legatis ejus nomine in Praga & alibi concordata, ac dein ab ipso demum concilio confirmata". The Compacts' own text, l.28617-28623: "concordata sunt inter legatos sancti concilii Basiliensis, & generalem congregationem inclyti Regni Bohemiae & Marchionatus Moraviae, in civitate Pragensi". The old claim was replaced by two:
- "The Compacts with the Bohemians, as Mansi prints them, were agreed between the legates of the council of Basel and the general assembly of Bohemia and Moravia at Prague". Witness M31 l.28617-28623. Acts, Documented.
- "Mansi's note says the Compacts were agreed by the council's legates in its name, at Prague and elsewhere, and then confirmed by the council itself". Witness M31 l.28594-28599, not the review's l.28590-28593. Modern reconstruction, Documented. The review's text, "the council itself then confirmed them", was widened to carry all of Mansi's sentence, since the first claim no longer holds "in its name ... and elsewhere".

**B2-M4 (procession: one claim, two witness kinds).** Confirmed. DOUK l.12004-12007 (Greek): "ἐκ πατρὺς καὶ υἱοῦ ὡς ἐκ μιᾶς ἀρχῆς καὶ μοναδικῆς προβολῆς, τὸ ὅπερ λέγουσιν οἱ Γραικοὶ ἐκ πατρὸς δι' υἱοῦ" (OCR as printed: "Γραικοὲ", "πατρὺς"). DOUK l.12038-12040 (Latin): "tanquam ex uno principio et unica processione, id quod Graeci dicunt ex patre per filium".
- Decree claim now: "The decree teaches that the Spirit proceeds from the Father and the Son as from one principle and one spiration. It reads the holy doctors' and fathers' 'through the Son' in that sense. It says the Filioque was added lawfully and with good reason". Witness mirbt l.14262-14274; denzinger l.16432-16444. Acts, Documented.
- Claim added after it: "Doukas calls 'from the Father through the Son' the phrase the Greeks use". Witness DOUK l.12004-12007; DOUK l.12037-12040. Later narrative, Documented.

### Not changed

- Entry `people` (Zara Yaqob) and the Ethiopian `traditions` note still name the emperor's side as "Eugenius's letter, Patrizi and Perruchon". Both statements stay true, and the full list is in `uncertain`, so they were left as they are.
- Records claim 9 ("Basel's session acts ... are not held") still cites M31 l.28590-28614 as one range for the Compacts and the admonition. That range is correct for a claim that only lists what tomus 31 prints.
