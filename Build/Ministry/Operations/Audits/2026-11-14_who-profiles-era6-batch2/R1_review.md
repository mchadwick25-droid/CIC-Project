# R1 review: era 6 batch 2

Round 1, the full checklist review, by four fresh Opus agents that had not seen the drafting, at full effort. Part A covers Catherine of Siena, Bridget of Sweden and the README; Part B, Bernardino of Siena and Angelo Clareno; Part C, William of Ockham and Nicholas Cabasilas; Part D, Gregory Palamas and Gregory of Sinai. No repo file was edited by the reviewers; no web, paid or model call was made. Each part is given as written.

## Era 6 Who batch 2, round 1 review: PART A

**Scope.** `catherine-of-siena` and `bridget-of-sweden`: brief, card, audio and each one's `records.json` entry. Also the batch `README.md` as a whole, with every claim in it, for all eight people, checked against the batch files, the scan (`Who_Scan_Era6.md`) and the live census (`git show origin/main:cic-website/data/world-census.json`). The branch is `claude/cft-who-era6-batch2` at 7ba02188. I edited no repo file and made no web, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, the scan rulings (l.15-56), the scan rows for Catherine (l.96) and Bridget (l.97), the File key, lessons.md, the batch 1 house form (`julian-of-norwich.*`) and the first 300 lines of the batch 1 R1 Part A.
- I opened every line the two records cite, with 20 or more lines of context, and checked each brief sentence and card field against them.
- I checked every quotation by eye against its file.
- I searched all 1,771 files in `cic/texts/` with windowed, case-insensitive regexes (my script, `scratchpad/s/win2.py`) before accepting any absence or "only". The name forms were Catharin-/Caterin-/Katherin-/Catherin- with Senen-/Senenf-/Senis/Siena/Sienna/Sene, and Birgitt-/Brigitt-/Brigid-/Brigida. The terms were canoniz-/canonis-, Pius II and its variants, 1461, Minerva, sepult-/sepolt-, stigmat-/ftigmat-, 1347, Klemming, Uppenbarelser, Vita abbreviata, LIBER SEXTUS/SEPTIMUS/OCTAVUS, Gobelin-, razor/novacula and "entia non sunt multiplicanda".
- I scored the briefs and my proposed rewrites with `engine.m1.gates.grade_text`, compared each audio file with its brief by script, counted sentence lengths by script, and checked the card field order.
- For the README I recomputed the word and score ranges for all eight briefs. I checked each tradition name, voice and people-list claim against the census. I checked each "beyond the scan" list and "correction" against the scan rows and records, and spot-checked the source lines behind the corrections.

**Files opened (cic/texts/).**
- MIRBT = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`: l.13855-13900.
- CATHL = `catherine-of-siena_selected-letters_scudder1905.txt`: l.1-12, 160-225, 505-530, 588, 1190-1400, 2170-2190, 4658, 4726-4895, 5160-5240, 6700-6805, 12415-12430, 12720-12940.
- CATHD = `catherine-of-siena_dialogue_thorold1896.txt`: l.1-45, 3185-3205.
- CATHI = `catherine-of-siena_libro-della-divina-dottrina-ita_fiorilli1912.txt`: l.1, 89, 14315-14520, 14598-14645, 14995-15008, 15160-15172, 15250-15262, 15540-15550.
- BIRGL = `birgitta_revelationes-lat_duranti1628.txt`: l.1-12, 205-262, 1170-1205, 1495-1600, 3850-3935, 8150-8212, 11075-11150, 98270-98315, 98408-98422, 98548-98612, 98760-98810, 98940-99020, 99150-99172.
- BIRGE = `birgitta_revelations-enm_cumming1929.txt`: l.850-1130, 1176-1202, 1223-1224, 1684-1694, 1776-1786, 2110-2140, 9585-9625.
- ASJUN5 = `acta-sanctorum_junii-tomus-5-lat_palme1867.txt`: l.52495-52590.
- ASMAR3 = `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`: l.131880-131905, 132970-133010, 133250-133330.
- WILKENS = `jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt`: l.16050-16125, 16300-16315.
- MANSI26 = `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`: l.53340-53415.
- One block each: LEA3 l.29370-29412; COVEL l.1-8, 183, 51445-51470; GARDNER l.470-505; TERESA l.640-705; BANCHI1 l.150-165; TEB3 l.2165-2180, 9680-9693; RICH l.3022-3048; GLASS l.20955-20978; GERSON l.27968-27995, 28320-28332; OLAVUS l.17078-17098; TYNDALE l.11970-11992; `craft-of-dying_…comper1917.txt` l.765-780.
- For the README: `bullarium-franciscanum_nova-series-v1-lat_huntemann1929.txt` l.573-577, 1107-1111; `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` l.16240-16268; `ehrle-denifle_…bd2…1886.txt` l.5678-5690, 6140-6152, 7669-7680, 7730-7742; `mansi_…tomus-25…1903.txt` l.42484-42494, 42566-42580; `palamas_homiliae-41-grc_jerusalem1857.txt` l.3582-3586, 5883-5887, 10140-10144, 10567-10571; `palamas_opera-omnia-pg150-grc-lat_migne1865.txt` l.60948-60958, 69294-69302; `cantacuzenus_…v2/v3` (Cabasilas lines by grep); `Open-Gaps.md` l.2177-2190, 3469-3481.

**Quotations.** Every quotation in double quotes matches its file.
- Catherine brief: "But you, with your taxes and frivolities, are spoiling all that is sown." matches CATHL l.6795-6796.
- Catherine brief: "Come, come, come, and do not wait for time, since time does not wait for you." matches CATHL l.5220-5222. The file reads "I tell you, Come, come, come", so the capital C is the file's.
- Catherine brief: "I have made a Bridge of My Word, of My only-begotten Son, and this is the truth." matches CATHD l.3199-3201. The file opens with "WHEREFORE I have told thee that", and the quote begins after it.
- Catherine card: "her constant theme is the corruption of every rank in the hierarchy and the immediate necessity for reform." matches LEA3 l.29390-29392.
- Both cards: "the books of St. Gertrude, St. Catharine of Siena, or St. Bridget of Sweden" matches TERESA l.683-685.
- Catherine card: "perhaps" matches CATHL l.1313.
- Bridget brief and card: "a sleer of soules" matches BIRGE l.2133 ("thu arte verely a sleer of soules").

No quotation marks sit around the drafter's English of Latin, Italian, German, Middle High German or Swedish in either brief or card. I checked each modern-words telling against its original: Raymond's audience (MIRBT), Guidini and Maconi (CATHI), the Naples revelation, the Urban V revelation and the Rule (BIRGL), Duranti on the eight books and on the Fifteen O's (BIRGL), Wilkens (WILKENS), Torquemada's first call (BIRGL), Lea's line on Bridget (LEA3), Olavus Petri, Bale, Richental, Glassberger and the Gerson Declaratio. Three tellings drop or shift what the original says: A-B1, A-B4 and A-B5. The README puts the drafter's English of Wilkens's German in quotation marks (A-M28).

**Audio.** Both audio files are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, two tags and nothing else changed (checked by script). Pass.

**Scores now.** Catherine: 405 words, FK 6.61, Flesch 73.76. Bridget: 405 words, FK 7.12, Flesch 66.68. My proposed full rewrites, with every fix below applied, score Catherine at 406 words (FK 6.64, Flesch 72.63) and Bridget at 404 words (FK 6.58, Flesch 69.87). Neither brief reads as flattened or choppy. Catherine's opening paragraph is the lowest-graded, and it reads as a clear scene.

---

### catherine-of-siena

**Verdict: three blocking findings (A-B1 to A-B3) and eleven minor ones.**

**A-B1 (brief para 3: the pope's condition is dropped, and the sentence runs to 31 words).**
- Current text: "From Avignon, on 28 June 1376, she told the Eight of War, the magistrates Florence chose when it rebelled against the pope, that Gregory was ready to receive them as sons."
- Source: CATHL l.6788-6791: "at the end of our talk he said that if your case were as I presented it to him, he was ready to receive you as sons, and to do what seemed best to me."
- The pope's offer depends on a condition, and the brief drops it. Told without the condition, it reads as an open offer that Florence threw away. The sentence is also 31 words long.
- Replacement: "From Avignon, on 28 June 1376, she wrote to the Eight of War, the magistrates Florence chose when it rebelled against the pope. Gregory would receive them as sons, she said, if their case was as she had put it."
- This adds 9 words. The cuts that offset it are in A-M3 and A-M2.

**A-B2 (card `uncertain`, "The stigmata"; records claim and contested_claim "The stigmata"; README: a Bollandist note is misread as a witness against her stigmata).**
- Current card text: "A Bollandist commentary on Christina of Stommeln, in the Acta Sanctorum for June, reports a bull of Sixtus IV forbidding pictures that showed her with Christ's wounds."
- Current records side: "The Bollandist commentary: Sixtus IV forbade images of her with Christ's wounds (ASJUN5 l.52573-52576)".
- Current README: "the stigmata (Scudder against a Bollandist note on Sixtus IV)".
- What the source says, ASJUN5 l.52514-52590 in context:
  - Lucy of Narni testified "quod S.Catharina Senensis, precibus et orationibus obtinuit a D. N. Jesu Christo, ut stigmata ipsius Luciae … essent visibilia et palpabilia, in fidem et testimonium stigmatum ipsius S. Catharinae". That is, Catherine won from Christ that Lucy's own wounds be visible, as proof of Catherine's.
  - This happened while the Holy See was working "de reformanda seu mitiganda, (sicuti reformata et mitigata etiam fuit) non diu post, Bulla Sixti IV, prohibente imagines omnes". So the bull was reformed and softened not long after.
  - The commentator concludes that God arranged it "ut antiquiori in Senensi Catharina miraculo … fidem faceret indubitatam". The margin reads "ad certificanda stigmata S. Catharinae Senensis".
- The note is not "against" Scudder. It holds the stigmata as proven, and it says the bull was softened. The card tells half of the note and drops the half that runs the other way. The real record of doubt is the bull itself, a papal ban on showing the wounds.
- Card replacement: "The stigmata. Scudder's chronology says she received them at Pisa on 1 April 1375, invisible at her own request. A Bollandist commentary on Christina of Stommeln, in the Acta Sanctorum for June, reports a bull of Sixtus IV that forbade pictures showing her with Christ's wounds, and says it was later softened. The same commentary takes the visible wounds of Lucy of Narni as proof of hers."
- Records contested_claim, side 2: "A bull of Sixtus IV forbade images of her with Christ's wounds, and was soon reformed and softened (ASJUN5 l.52526-52527, 52580-52582). The Bollandist commentator himself takes Lucy of Narni's visible stigmata as proof of hers (ASJUN5 l.52514-52523, 52542-52546, 52587-52590)." Fix the records claim to match.
- README: "the stigmata (Scudder's chronology, and the bull of Sixtus IV against pictures of them, which the Bollandist note reports with its later softening)".

**A-B3 (card `uncertain`, "How far she caused the pope's return"; records contested_claim; README bullet: the recorded contest has no contrary side, and the held contrary witnesses are missed).**
- Current records sides:
  - Side 1: "Scudder: Gregory 'swayed by her representations' … Duranti: her letters handled the whole matter".
  - Side 2: "Bridget's revelations pressed the same demand … Scudder: Gregory perhaps regretted the return and became alienated from her".
- Neither item on side 2 denies or weakens her part in the return. Scudder's 1378 coolness comes after the return and does not touch its cause.
- Fiorilli, a further held witness, is on side 1: "avvenimento al quale santa Caterina aveva molto contribuito" (CATHI l.14342-14344).
- A held text does give other causes. MANSI26 l.53393-53410, the notice of Gregory XI printed in Mansi's councils, says "Hujus transmigrationis causam alii aliam referunt":
  - Platina tells of a bishop's retort ("cur ad propriam ecclesiam non redis?").
  - Gobelinus says the return came "instinctu & revelatione Dei, quae sanctae Brigittae tunc adhuc Romae degenti aliquoties obtigerat, perque Alphonsum quemdam eremitam illi secundo insinuata erat".
  - Neither names Catherine.
- The brief tells only side 1, by naming its witnesses. Under the pattern ("Contested gives both sides by name") a disputed point is told where it arises, with both sides.
- Brief replacement for para 4 (one sentence added): "Gregory reached Rome in January 1377. Scudder writes that he was swayed by Catherine. Consalvo Duranti, in his 1628 notes on Bridget of Sweden's Revelations, says her letters handled the whole matter of his return. A life of Gregory printed in Mansi's councils says one writer, Gobelinus, credited a revelation of Bridget."
- The added sentence is 17 words. The cuts that offset it are in A-M3 and A-M2. Mansi gives Gobelinus no role, so "one writer" claims no more than the line does.
- Card item replacement: "How far she caused the pope's return. Scudder writes that Gregory, swayed by her representations, returned, and Duranti says her letters handled the whole matter of the return. Matilde Fiorilli writes that she did much toward it. A notice of Gregory's life printed in Mansi's councils names other causes: Gobelinus credits Bridget of Sweden's revelations, and Platina a bishop's retort. Scudder also writes that Gregory, perhaps regretting his return, became alienated from her."
- Records, side 2: "Other causes: Gobelinus credits Bridget's revelations, delivered through Alphonso; Platina, a bishop's retort (MANSI26 l.53393-53410)". Add MANSI26 to the claims and Fiorilli to side 1. Bring the README bullet into line.

**A-M1 (brief para 5: "they" has no antecedent).**
- Current text: "Her secretary Cristofano Guidini wrote that she spoke it in a trance, every sense lost but her tongue, while they took turns writing."
- Source: CATHI l.14405-14407: "Ella diceva e uno scriveva: quando ser Barduccio, quando el detto donno Stefano, e quando Neri di Landoccio". Fiorilli's notes 5-7 call them disciples and secretaries (l.14432-14442).
- The only noun before "they" is Guidini, who is singular.
- Replacement: "…every sense lost but her tongue, while three disciples took turns writing." (+1 word)

**A-M2 (brief para 5: "kings and queens" overstates).**
- Current text: "…and wrote to kings and queens for him."
- Source: CATHL l.1379-1381: "She writes on his behalf to the Kings of France and Hungary, to Queen Giovanna of Naples, to the magistrates of Italian cities, to the Italian cardinals". That is one queen.
- Replacement: "…and wrote to rulers for him." (-2 words)

**A-M3 (brief para 6: Covel has no role, and the sentence repeats a fact the card shows).**
- Current text: "John Covel, writing in 1722, says Pope Pius II made her a saint about eighty years later."
- Source: COVEL l.51459-51461. The title page reads "D. D. and Master of CHRIST College in [Cambridge]" (COVEL l.183). He is arguing against prayer to her ("I protest I never well consider'd till now the wonderfull Power of the Pope", l.51462-51466).
- The pattern says facts the card already shows are not repeated as a list. The card's `dates` and `uncertain` carry the canonization with Covel named.
- Fix: cut the sentence from the brief (-17 words). If it is kept, it reads: "John Covel, Master of Christ's College, Cambridge, writing in 1722 against prayer to the saints, says…"

**A-M4 (brief closing: Thorold gets no time at first mention).**
- Current text: "In Algar Thorold's English of her Dialogue, God tells her:"
- Source: CATHD l.21-31 (1896).
- Replacement: "In Algar Thorold's English of 1896, God tells her:" (this adds 1 and cuts 3 words). "Her Dialogue" is named two paragraphs earlier.

With A-B1, A-B3 and A-M1 to A-M4 applied, the brief is 406 words, FK 6.64, Flesch 72.63. The full text is in `scratchpad/s/prop/cath.txt`. If 406 is too many, cut "As a young woman" (para 2).

**A-M5 (card `legacy.traces` 1: the Latin version comes loose from its witness).**
- Current text: "Stefano Maconi, one of her secretaries, says in testimony quoted by Matilde Fiorilli that he wrote down part of the Dialogue as she dictated it, and later put it into Latin."
- Source: the testimony (CATHI l.14444-14450) covers only the writing down. The Latin is in "alcune parole scritte di sua mano dietro ad un codice" of the Pavia Charterhouse: "sed ego latinizavi" (l.14452-14472).
- Replacement: "Stefano Maconi, one of her secretaries, said in the canonization process that he wrote down part of the Dialogue as she dictated it. A note in his own hand, which Matilde Fiorilli quotes, says he put it into Latin."

**A-M6 (card `legacy.traces` 4: a thesis line with no witness, and "led" overstates).**
- Current text: "Her disciples carried on her work. Fiorilli says Stefano Maconi became general of the Carthusians, and Tommaso Caffarini led the process for her canonization at Venice."
- Source: CATHI l.14436-14438 (Maconi "fu priore della certosa di Pavia e poi superiore generale dell'ordine") and l.14462-14465 (Caffarini "ebbe la parte maggiore nel processo della canonizzazione fatto a Venezia"). Fiorilli does not call Caffarini her disciple.
- Replacement: "Fiorilli says Stefano Maconi became prior of the Pavia Charterhouse and then general of the Carthusians, and that Tommaso Caffarini of Siena took the largest part in the process for her canonization held at Venice."

**A-M7 (card `legacy.traces` 3: Fiorilli's hedge is dropped).**
- Current text: "…the first in 1472."
- Source: CATHI l.14509-14510: "quella che è ritenuta edizione principe, 1472".
- Replacement: "…the first, as it is held, in 1472."

**A-M8 (card: scholars and witnesses get no role or time at first mention).**
- Current text: "Edmund Gardner writes…"; "Henry Charles Lea writes…"; "A note on Teresa of Ávila's manuscript, by Father Alvarez…".
- Sources:
  - GARDNER, the 1910 introduction to Seven Early English Mystical Treatises (file title).
  - LEA3, A History of the Inquisition of the Middle Ages, 1888.
  - TERESA l.644, 661-662, 695-696: "Father Rodrigo Alvarez, S. J."; "this, the 22nd day of February, 1582. P. Rodrigo Alvarez".
- Replacements:
  - "Edmund Gardner, introducing early English mystical texts in 1910, writes…"
  - "Henry Charles Lea, historian of the medieval Inquisition, writes in 1888…"
  - "A note of 1582 on Teresa of Ávila's manuscript, by the Jesuit Rodrigo Alvarez, names…"
- The same Alvarez fix applies on Bridget's card (A-M23).

**A-M9 (records: single-witness claims are tagged Widely Accepted).**
- Each of these rests on one witness:
  - The Avignon scene rests on Raymond alone. Scudder dates the stay but does not tell the scene.
  - The Mantellate (CATHL l.1279-1282).
  - "The peace failed" (CATHL l.1227).
  - The schism and Rome (CATHL l.1371-1385).
  - The places (CATHL l.1258-1261, 1320-1327, 1371-1375).
- The brief's rule: one witness is Inferential-Thin. The records already tag the birth day that way (CATHL l.1256-1262), so the tags are inconsistent.
- Fix: retag these Inferential-Thin, or add a held second witness where one exists. For "learned to write", add Fiorilli: "sapeva appena leggere e meno ancora scrivere", and her learning to write in October 1377 (CATHI l.14604-14607, 14631-14634).

**A-M10 (records contested_claim "When the Dialogue was finished": the Barberini line is the date of the book, not of its ending).**
- Current text: "1377: a Barberini copy (CATHI l.15169)".
- Source: CATHI l.15166-15169: "comincia lo libro … data da Dio a la sopradetta vergine … E questo fu nel 1377 (_sic_)". This is the date the codex gives for the book, at its opening, and Fiorilli marks it sic.
- Replacement: "1377 (Fiorilli's sic): a Barberini copy, at the book's opening (CATHI l.15166-15169)". The card's wording "a Barberini copy gives 1377" can stay.

**A-M11 (records `absent_details`, the canonization note: the second witness is under-described).**
- Current text: "Only Covel (COVEL l.51460-51461), with no year, and a 1517 edition title (CATHI l.15547-15550)."
- Source: CATHI l.15544-15550: "1517, Venetia … _Dialogo_ … con la sua uita: et canonizatione … (con poesie di papa Pio II e di altri in lode della santa)". This is a 1517 printing, held in Fiorilli's list, that joins her canonization to poems by Pius II.
- Replacement: "Only Covel (COVEL l.51460-51461), with no year, and Fiorilli's entry for the 1517 Venice Dialogue printed 'con la sua uita: et canonizatione' with poems of Pius II in her praise (CATHI l.15544-15550). No bull is held."

---

### bridget-of-sweden

**Verdict: two blocking findings (A-B4, A-B5) and sixteen minor ones.**

**A-B4 (brief para 3, card `uncertain` 1, records claim and contested_claim, README: witness swap; Vastovius is not the one who gives the eight books).**
- Current brief text: "Consalvo Duranti, a bishop annotating the Latin in 1628, quotes Johannes Vastovius, who gives all eight books to Peter Olafson."
- Current card text: "Duranti quotes Johannes Vastovius giving the translation of all eight books to Peter Olafsson, a Cistercian."
- Source: BIRGL l.11096-11123, in Duranti's own treatise on visions ("DE VISIONIBVS. CAP. II"):
  - Duranti names Matthias and Peter Olavus, "quorum vitam, & praeclare gesta scripsit Ioannes Vuasthonius Gothus, Canonicus Varmiensis, & Regis Poloniae Sigismundi Tertij Bibliothecarius".
  - He quotes Vastovius on Matthias only ("Matthias, inquit, floruit…").
  - Then he goes on in his own voice: "Alter S. Brigittae Confessor Petrus Olauus fuit Ordinis Cisterciensis, qui in linguam Latinam octo libros Reuelationum transtulit, cuius etiam vitam scripsit idem Ioannes Vuasthonius". The words "cuius etiam vitam scripsit idem" show that this is Duranti speaking about Vastovius, not quoting him.
- Duranti also gives a second account. At BIRGL l.8157-8181 he says three friends, "Petrus Olauus … Magister Matthias … Alphonsus", "redegerunt ea in libros".
- The "Peter Olafson" of the brief is Cumming's "first confessor of the Vadstena monastery" (BIRGE l.969-970). Duranti's "Petrus Olauus" is "Ordinis Cisterciensis". Torquemada's two men are "Fratris Petri Prioris Aluastri, & Domini Petri Olaui" (BIRGL l.1567-1568), and Alvastra is the Cistercian house. So the brief joins a name across two sources that may mean different men.
- Brief replacement: "Consalvo Duranti, a bishop annotating the Latin in 1628, gives all eight books to a Cistercian confessor he calls Peter Olavus." (+1 word)
- Card replacement for the Duranti sentence: "Consalvo Duranti gives all eight books to Peter Olavus, a Cistercian confessor, in one place, and in another names Peter Olavus, Master Matthias and Alphonso as the three who put her words into books."
- Records claim: "Duranti, in his treatise on visions: 'Alter S. Brigittae Confessor Petrus Olauus fuit Ordinis Cisterciensis, qui in linguam Latinam octo libros Reuelationum transtulit, cuius etiam vitam scripsit idem Ioannes Vuasthonius' (BIRGL l.11120-11124); also the three 'amici' (l.8157-8181)". Change the contested_claim side to the same owner.
- README: replace "Duranti quoting Vastovius" with "Duranti's two accounts".

**A-B5 (brief para 1: Christ's answer is told by its tail only, and its main claim is dropped).**
- Current text: "The answer, her Revelations say, was that whether she would see him come was not hers to know."
- Source: BIRGL l.98979-98980, 99007-99016:
  - Before her objection, Christ says "scias certissime, quod ipse veniet Roma" (l.98979-98980).
  - After it, he says "nihilominus tamen ego Dominus praevaleo eis, & ducam ipsum Papam ad Romam, non ad eorum consolationem. Sed vtrum tu videbis eum venire, an non, tibi non est licitum scire."
- The brief tells only the last clause as "the answer". The revelation's central claim is that the pope would come. Without it, the next two sentences ("She died in Rome that July. Gregory XI reached Rome in January 1377.") read as the narrator's irony against an answer the revelation did not give.
- Replacement: "Christ answered, her Revelations say, that he would lead the pope to Rome, but whether she would see it was not hers to know." (+6 words)

**A-M12 (brief para 1: first-person words in the narrator's voice, and a 34-word sentence).**
- Current text: "The Queen of Naples and many others tell me it is impossible for him to come to Rome, she said, because the King of France and the cardinals put many obstacles in his way."
- Source: BIRGL l.98980-98988: "O Domine Deus meus, Regina Neapolis, & multi alij dicunt mihi, quod impossibile est eum venire Romam, quia Rex Franciae, & Cardinales, & alij, quamplurima ponunt ei impedimenta".
- A listener hears "tell me" as the narrator's words before "she said" arrives.
- Replacement: "She told Christ that the Queen of Naples and many others called it impossible for him to come to Rome. The King of France and the cardinals, they said, put many obstacles in his way." (34 words in two sentences, ±0)

**A-M13 (brief para 4: the revelation's condition is dropped).**
- Current text: "When Urban V, who came in 1367, left again in 1370, a revelation she handed him warned that he would soon suffer a blow."
- Source: BIRGL l.98553-98556: "Si contigerit ipsum redire ad terras, vbi fuit electus Papa, ipse habebit in breui tempore vnam percussionem". The heading is "antequam rediret Auenionem … quam ipsa praesentauit ei in Monteflascone" (l.98413-98418).
- Replacement: "When Urban V, who came in 1367, left again in 1370, she handed him a revelation. If he went back, it warned, he would soon suffer a blow." (+4 words)
- For the card or records: Cumming says that "This revelation was delivered to him by Alphonso" (BIRGE l.993, 1022). This differs from the heading's "ipsa praesentauit". Note it in the records.

**A-M14 (brief para 5: "the English version" is undefined).**
- Current text: "In the English version, Christ tells…"
- Source: BIRGE title and l.1176-1180 (the fifteenth-century English version, Garrett MS).
- Replacement: "In a fifteenth-century English version, Christ tells…" (+1)

**A-M15 (brief: scholars get no role).**
- Current texts: "Henry Charles Lea, writing in 1888, judged…"; "C. A. Wilkens, writing in 1894, says…".
- Sources: LEA3 (the Inquisition history, 1888). WILKENS l.16058-16062 and 16310: Wilkens signs a review of Binder's and Flavigny's books in the Zeitschrift für Kirchengeschichte.
- Replacements: "The historian Henry Charles Lea judged in 1888 that…" (+1); "C. A. Wilkens, in an 1894 review, says…" (±0).
- Johannes Vastovius drops out of the brief with A-B4.

**A-M16 (brief closing: a colon-reveal, an "X, not Y" contrast and first-person words in the narrator's voice).**
- Current text: "She feared a trick of Satan, until Christ said: I am the maker of all, not a deceiver."
- Source: BIRGL l.1506-1524. She feared "illudi ab Angelo Sathanae" and went to Master Matthias. After fasts and a second vision, at the third she heard "Mulier audi me, Ego sum Deus tuus, qui tecum loqui volo, noli timere. Ego sum omnium conditor, non deceptor."
- The contrast is the source's. But told in the narrator's voice, after a colon and with no quotation marks, it is heard as the narrator's line.
- Replacement: "She feared a trick of Satan, until Christ told her that he was her God, the maker of all, and she need not fear." (+6 words)

**Cuts that offset A-B4, A-B5 and A-M12 to A-M16.**
- Cut para 6's "Cumming says the schism of rival popes brought the canonization into question, and later popes confirmed it." (-17). The card's `uncertain` carries it with its witnesses.
- Cut "for sisters and brothers" (-4). The card carries the order.
- Cut "rich" in "dimmed her rich images" (-1). Wilkens has "reiche Bildersprache", so either reading is faithful.
- With all of Bridget's fixes applied, the brief is 404 words, FK 6.58, Flesch 69.87. The full text is in `scratchpad/s/prop/brid.txt`.

**A-M17 (brief para 1 and records: "Early in 1373" is a reckoning, and the records do not show it).**
- Records claim: "Naples, early 1373, after Jerusalem". It cites the chapter heading, which gives no year: "in festo Sancti Policarpi, quando rediit de Hierusalem" (BIRGL l.98947-98953).
- The year follows from these lines:
  - She stopped at Naples "in February of 1372 on their way to Jerusalem" (BIRGE l.9590-9592).
  - The next revelation is "in mense Februario" (BIRGL l.99016-99018).
  - The fourth is dated "in mense Iulij, anno Domini M.CCC.LXXIII" (BIRGL l.99163-99165).
- Cumming also says "Birgitta returned to Rome the same year" (BIRGE l.1047-1048), meaning 1372.
- The brief's wording can stay. Fix the records claim: "Early 1373 by reckoning: the outbound stop at Naples in February 1372 (BIRGE l.9590-9592); the return on Polycarp's feast (BIRGL l.98947-98953); the February and July 1373 revelations that follow (BIRGL l.99016-99018, 99163-99165). Cumming's 'returned to Rome the same year' (BIRGE l.1047-1048) runs against it." Tag it Dominant Modern Reconstruction, owned by the drafter's reckoning, or Inferential-Thin.

**A-M18 ("Saviour" is British spelling outside quotation).**
- Current texts: brief para 4 "Order of St Saviour"; card knownFor, role and keyWorks.
- Cumming prints "Order of St. Saviour" (BIRGE l.1026-1027). The house rule is American spelling outside quotations.
- Replacement: "Order of St Savior" throughout. If the coordinator treats the order's English name as a title, it can be kept, but then it should be kept the same way across the batch.

**A-M19 (card `sources`: Scudder is missing).**
- The brief's "Gregory XI reached Rome in January 1377" rests on CATHL l.1227-1229 (records claim 3). Scudder is not in Bridget's `sources`.
- Fix: add `{"title": "Saint Catherine of Siena as seen in her Letters, chronology", "author": "Vida D. Scudder (trans. and ed.)", "date": "1905", "language": "English", "file": "cic/texts/catherine-of-siena_selected-letters_scudder1905.txt"}` to `about`.

**A-M20 (card `otherNames`: an inflected form).**
- Current text: "Brigittam de Suecia".
- Source: GERSON l.28327-28330, "Brigittam de Suecia", in the accusative after "conveniat".
- Replacement: "Brigitta de Suecia".

**A-M21 (card keyWorks 1: process narration).**
- Current text: "Books one to five are given here in the Latin printed at Rome in 1628".
- Replacement: "Books one to five survive in the Latin printed at Rome in 1628…". Alternatively: "The 1628 Roman printing of books one to five carries Juan de Torquemada's defense and Consalvo Duranti's notes."

**A-M22 (card keyWorks 3: the Rule's giver differs between the witnesses).**
- Current text: "which her revelations present as dictated by Christ."
- Sources: BIRGL l.98289-98312: "Filius Dei loquitur … Ego obtuli tibi Regulam … Ego dictaui eam". Against that, BIRGE l.1027-1030: "she had received and had written down the rules of the Order exactly as they were given to her by the Mother of God."
- Replacement: "which a revelation to Urban V presents as dictated by Christ. Cumming says she believed she had received it from the Mother of God, and that Urban V approved the order in 1370, after years of her entreaty."

**A-M23 (card `legacy`: witnesses get no role, and the Bale item misses Cumming's caveat).**
- Current texts: "Ulrich Richental writes…"; "Nicolaus Glassberger records…"; "A note … by Father Alvarez"; "John Bale, an English Protestant writer quoted by Cumming, calls them dark dreams."
- Sources:
  - RICH is the Chronicle of the Council of Constance (title).
  - Glassberger is "an Observant Franciscan writing about 1508", as the batch's own Bernardino card puts it.
  - TERESA l.644, 695-696 gives Rodrigo Alvarez, S.J., 1582.
  - BIRGE l.1223-1224: "John Bale, Scriptorum Illustrium maioris Brytanniae, Basileae, 1557 … Bale confuses St. Birgitta with St. Bridget of Ireland." No held line I found calls Bale a Protestant.
- Replacements:
  - "Ulrich Richental, chronicler of the Council of Constance, writes…"
  - "Nicolaus Glassberger, an Observant Franciscan chronicler, records…"
  - "A note of 1582 on Teresa of Ávila's manuscript, by the Jesuit Rodrigo Alvarez, names…"
  - "John Bale, writing in 1557 and quoted by Cumming, calls them dark dreams; Cumming notes that Bale confuses her with Brigid of Ireland."

**A-M24 (card `place` and `dates`: a reckoned year with no owner, and a held 23 July witness left out).**
- Current text: "Rome, where she lived from about 1349 and died."
- The year is a reckoning from Cumming's "two or three years" after 1346 (BIRGE l.928-929, 967). The Bollandists reckon "ab anno 1348" (ASMAR3 l.133269).
- Replacement: "Rome, where she lived from 1348 or 1349, by Cumming's reckoning, and died."
- In `dates` and `uncertain` ("Her death day…"), add the Bollandists' note to the 23 July side: "Anno 1373 die 23 Julii" (ASMAR3 l.133269). Replacement: "…Boniface IX's bulls set her feast on 23 July, and a Bollandist note on her daughter's Life gives the same day."

**A-M25 (missed held witness: Gobelinus credits her revelations for Gregory's return).**
- MANSI26 l.53403-53410 reports that Gregory returned "instinctu & revelatione Dei, quae sanctae Brigittae tunc adhuc Romae degenti aliquoties obtigerat, perque Alphonsum quemdam eremitam illi secundo insinuata erat". Neither the card nor the records use it, and the census voice line ("made the same demand") says less.
- Card `legacy.remembered`, new item: "A notice of Gregory XI's life printed in Mansi's councils reports that Gobelinus credited his return to Rome to her revelations, conveyed to him through Alphonso. Platina, it says, gave another cause." Add the claim to the records, with MANSI26 l.53393-53410.

**A-M26 (records contested_claim "Her birth year": a file header stands as a side).**
- Current text: side 2 is "File headers: about 1303 (not a witness)".
- A header is not a witness, so it cannot be a side. The real doubt is Cumming's: "The earliest authorities differ" (BIRGE l.889). His year line is also unclear in the OCR ("1302 or 1308?", l.857, with a footnote mark).
- Replacement sides: "Cumming's line as printed: 1302 or 1308 (BIRGE l.857); the second figure may be an OCR misreading" and "Cumming: the earliest authorities differ, citing S.R.S. iii (BIRGE l.889)". Move the header note to `absent_details`.

**A-M27 (records claim on the Naples revelation: the tag and the witness need a split).**
- Current text: "Documented" for a claim that joins the revelation's text with "Widow: her husband died in 1344 (BIRGE l.919)".
- The revelation's words are Documented. The year is a reckoning (A-M17).
- Fix: split the claim. Keep the revelation's text Documented and put the year under the A-M17 claim.

---

### README.md

The word, grade and Flesch ranges match my recount for all eight briefs: 402 to 406 words, FK 6.61 to 8.78, Flesch 61.60 to 73.76. Recompute them after the fixes. The tradition names match the census. These checks hold:
- Clareno is the Fraticelli entry's first voice and also a Franciscan Order voice.
- Palamas is also a Palaiologan voice.
- None of the eight has a census person entry.
- The Fraticelli `legacy` names Ockham among "The friars who fled the papal court" and does not list him as a voice.
- The tradition caps hold.
- The scan's Major column says "yes" for all eight.
- Latin West carries five majors from this batch, and batch 1's eight traditions are all in the Latin West river.

The scan corrections I checked against the files all hold:
- Bernardino: BULN l.575 and 1109 name only Capistrano; GLASS l.16242-16267 gives "adolescens XX annorum" and "annorum XXII" in 1402.
- Clareno: EHRLE II l.5678ff and 7669-7742 are the authorship case and the hearing.
- Ockham: MANSI25 l.42491-42493, "Willielmus de Okam, rector ecclesiae de Langleton, in theologia doctores", 1311.
- Palamas: PALH l.3584, 5885 and 10142 are headings; l.10569 follows Neilos's encomium heading.
- Gregory of Sinai: PG150 l.60950-60958 is the head of the Ascetica; l.69298 begins "CAPITA PER ACROSTICHIDEM".
- Cabasilas: CANT2 l.24909 ("ὁ σακελλίου Καβάσιλας"), l.32140-32169 (Nicholas and Pharmakes); CANT3 l.6396, 16601.
- Catherine: CATHL l.1394-1395 is the death; BIRGE l.980-993 never names Catherine.
- Bridget: BIRGE l.1049, 1184.

The "No held line has 'Ockham's razor'" claim holds. I searched "razor" and "novacula" within 600 characters of Ockham/Occam/Okam/Ocham/Occham, and "entia non sunt multiplicanda", "pluralitas non est ponenda" and "frustra fit per plura" across all files, and found nothing that ties any of them to Ockham.

The README also carries the errors in A-B2 (the stigmata), A-B3 (the return) and A-B4 (Vastovius). Those fixes include the README lines, so they are not counted again here.

**A-M28 (README, Bridget bullet: the drafter's English of German is in quotation marks).**
- Current text: "Wilkens's "rhetorical Latin"".
- Source: WILKENS l.16116: "in rhetorisierendes Latein".
- The README's own rule keeps quotation marks "only for lines held in English".
- Replacement: "Wilkens on her Latin as rhetorical".

**A-M29 (README, para 2: "only in their traditions' voices and people lists" is not true).**
- Current text: "the eight appear in the census only in their traditions' voices and people lists."
- Census:
  - Ockham is a Franciscan Order voice but is not in its `people` list.
  - Most of the eight also appear in tradition texts, for example Palamas in the Hesychasm `why`, `longDescription` and `legacy`, and Bernardino in Observant `why`, `legacy` and `documentedStories`.
  - The README itself says that the Fraticelli entry "names him in its text".
- Replacement: "none is a live census person entry; the eight appear in their traditions' voices, people lists and texts (Ockham is a Franciscan Order voice but not on its people list)."

**A-M30 (README, para 3: wrong Open-Gaps citation for who picks the river's five).**
- Current text: "Mark picks which five the river shows (Open-Gaps 217)".
- Source: Open-Gaps 217 (l.2177-2190) sets the caps and the major mark. It does not say who picks when the majors exceed the cap. That rule is in Open-Gaps 263 (l.3472), for eras 4 and 5 only: "Which five each river shows is proposed in `Rescore.md`. Owner: Mark, through the coordinator." No entry covers era 6 yet.
- Replacement: "Which five the river shows is Mark's pick, as for eras 4 and 5 (Open-Gaps 263); an era 6 entry is to be registered with this batch."

**A-M31 (README, Cabasilas bullet: "all tagged Contested" is wrong for one item).**
- Current text: "…whether the "Kabasilas of the sakellion" and Gregoras's old friend are he, and which anti-Latin writings are his are all tagged Contested."
- Records: the Gregoras friend claim is tagged "Dominant Modern Reconstruction" (Boivin's "Nicolaus scilicet", GREG2 l.47127-47128). The `contested_claims` list has no record for it. The card's `uncertain` does carry it.
- Fix: either add a contested_claim record (Gregoras names only "Καβάσιλας", GREG2 l.28603-28608; Boivin and Gass take him for Nicholas), or reword the README: "…are tagged Contested, and Gregoras's old friend is Boivin's and Gass's identification."

**A-M32 (README, "Held witnesses beyond those the scan cites": the lists read as full but leave out witnesses the cards use).**
- Catherine: Banchi (BANCHI1 l.158-160, card `remembered`) is not listed.
- Bridget: Lea (LEA3 l.29382-29386, brief para 5), Alvarez's note (TERESA l.683-685), Scudder's chronology (CATHL l.1227-1229, brief para 1) and, after A-M25, Mansi 26 are not listed.
- Fix: add these, or head the lists "among them".

### Census (for an Open-Gaps note; no census edit proposed)

The card tradition name for both, "The Latin Papal Church (Avignon to Fifth Lateran)", is the census name, and both are voices and on the people list.

The entry's documented story "'Be a Man, Father, Arise!'" tells as settled several things the held sources do not support or contradict:
1. "He died within the year": Scudder has Gregory reach Rome on 17 January 1377 and die in March 1378 (CATHL l.1228-1232).
2. The quoted "Be a man, Father, arise!" and "stinking flowers" are not Scudder's wording. Scudder has "deal manfully" (l.4658, 4820) and "the malodorous flowers" (l.5167), and no held file has the census wording.
3. "nearly four hundred survive" is in no held line I found.
4. "Gregory left Avignon in September 1376" is in no held line. Scudder dates only Catherine's departure, on 13 September (l.1345), and Mansi's notice gives no month.
5. The needle story rests on Raymond's full Life, which is not held (records `absent_details`).
6. The story's own caveat, "The weight of Catherine's influence on Gregory XI's decision is debated", matches A-B3.

### records.json (these profiles)

- **catherine-of-siena.** The claims cover every brief sentence and card field. Fix the stigmata claim and contested_claim (A-B2), add MANSI26 and Fiorilli to the return claim and contested_claim (A-B3), and add a records line for the Gobelinus sentence if it is adopted. Retag the single-witness claims (A-M9), and fix the Barberini side (A-M10) and the canonization absence note (A-M11). The burial absence holds: I searched Minerva, sepult-, sepolt- and "buried" near every name form and found no held place. The "Raymond's Life in full" absence holds: no Acta Sanctorum April file is held.
- **bridget-of-sweden.** Fix the Duranti claim and contested side (A-B4), the Naples year (A-M17, A-M27), the birth-year sides (A-M26), and add Gobelinus (A-M25) and Cumming's Alphonso note on the Urban revelation (A-M13). These absences hold:
  - "Her Swedish text": no Swedish text of the Revelations is held. Olavus Petri and later Swedish files only name them.
  - "Books six to eight": no LIBER SEXTUS, SEPTIMUS or OCTAVUS heading in BIRGL.
  - "The Life by her confessors and the Vita abbreviata": these appear only as citations, in Cumming (BIRGE l.871-879) and the Bollandists (ASMAR3 l.131890-131895).

### Checklist summary

| # | Item | catherine-of-siena | bridget-of-sweden |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Fail (A-B1, A-B2) | Fail (A-B4, A-B5) |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | Nothing invented | Pass | Pass |
| 4 | Reading aids, no AI tells | Fail (A-B1 length, A-M1, A-M2) | Fail (A-M12, A-M16, A-M14) |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass (Covel's polemic is unused; A-M3) | Pass |
| 7 | Contested claims show both sides by name | Fail (A-B3) | Fail (A-B4, wrong owner of one side) |
| 8 | Common names and scholars identified at first mention | Pass for places; roles missing (A-M4, A-M8) | Pass for places; roles missing (A-M15, A-M23) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene opening, disputes in place, length | Fail (the return dispute is told one-sided; A-B3) | Pass |
| 11 | `grade_text` (FK ≤ 10, Flesch ≥ 60) | Pass (6.61, 73.76) | Pass (7.12, 66.68) |
| 12 | Card order, missing fields absent, caveat repeated | Pass | Pass (sources gap A-M19) |
| 13 | Audio tags only in the audio script, placed right | Pass | Pass |
| 14 | Keeps list line; Who test | Pass (voice and people list) | Pass (voice and people list) |

### Count

- catherine-of-siena: 3 blocking (A-B1, A-B2, A-B3), 11 minor (A-M1 to A-M11).
- bridget-of-sweden: 2 blocking (A-B4, A-B5), 16 minor (A-M12 to A-M27).
- README.md: 0 blocking of its own (its errors are carried by A-B2, A-B3 and A-B4), 5 minor (A-M28 to A-M32).
- Part A total: 5 blocking, 32 minor.

---

## Era 6 Who batch 2, round 1 review: PART B

**Scope.** `bernardino-of-siena` and `angelo-clareno`: brief, card, audio script, their `records.json` entries, the README lines about them, their scan rows (Who_Scan_Era6.md l.98, l.99, with l.107-108, 156, 173, 254, 261), and the census entries for their traditions (`git show origin/main:cic-website/data/world-census.json`: `observant-reform-and-popular-preaching`, `fraticelli-spiritual-franciscan-rigorists`, `franciscan-order-era-6`). Branch `claude/cft-who-era6-batch2`. No repo file edited; no web, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, the batch README, the scan rulings (l.15-56) and file key, lessons.md, the Julian of Norwich profile of batch 1 and Part A of the batch 1 R1 review for the house form. I opened every line the two records entries cite, with 20 or more lines around each, and read the Latin, Italian and German myself. I checked every quotation by script (lowercase, letters and digits only, OCR "Chureh" read as "Church"), then by eye. For every "no witness", "only", "one" and absent_details note, I searched all of `cic/texts/` with name variants (Clarenus, Clareno, Clarin, Claren, Cingul, Cingol, Fossabrun, Forosempron; Bernardin* with Senis/Senensis/Siena, Albizz, Vegio/Vegius, Massa, Roma/Rome, fried/fritto/arostito, tavolett, tabell, segno), then read every hit near the subject's name. I scored the briefs with `engine.m1.gates.grade_text`, counted sentence lengths by script, rebuilt each audio script from its brief and compared it byte for byte, and scored my own replacement briefs the same way.

**Files opened (cic/texts/).** ORL = `bernardino-of-siena_sermons_orlandi-robins1920.txt` (l.1-12, 13-420, 2905-2956, 5780-5840, 6790-6880, 8730-8760); BANCHI1 = `bernardino-of-siena_prediche-volgari-1427-v1-ita_banchi1880.txt` (l.150-186, 250-262, 300-352, 405-470, 755-812, 809-1200 Vespasiano's Life whole, 1225-1275, 5325-5385, 6405-6415, 11625-11650); BANCHI2 = `…-v2-ita_banchi1884.txt` (l.1-5, 11035-11075, 11650-11680, 16095-16215); BANCHI3 = `…-v3-ita_banchi.txt` (l.1-5, searches); GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` (l.90-135, 16235-16300, 19740-19800, 20690-20715, 21075-21145, 21680-21790, 22950-22965); BULN = `bullarium-franciscanum_nova-series-v1-lat_huntemann1929.txt` (l.570-580, 1105-1112, 13100-13195, 43685-43700, 84488-84680, 108615-108630, 108940-108956, 109008-109020); RAYN = `raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt` (l.275-284, 2370-2450, 18235-18350, 60060-60115); LEA3 = `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt` (l.1-8, 2190-2203, 3328-3340, 3622-3634, 8220-8234); CLAR = `clareno_expositio-regulae-fratrum-minorum-lat_oliger1912.txt` (l.1-12, 92-149, 945-1060, 1125-1440, 1440-1590, 1625-1685, 2975-2995); EHRLE1 = `ehrle-denifle_archiv-…-bd1-deu-lat_1885.txt` (l.27536-27605, 27665-27705, 27755-27870, 28555-28570, 29150-29225); EHRLE2 = `…-bd2-deu-lat_1886.txt` (l.1-3, 5715-5770, 5815-5836, 5990-6020, 7655-7745); EHRLE3 = `…-bd3-deu-lat_1887.txt` (l.22698-22715); EHRLE4 = `…-bd4-deu-lat_1888.txt` (l.1-4, 555-660); BUL5 = `bullarium-franciscanum_v5-lat_eubel1898.txt` (l.23175-23190, 23350-23362, 84525-84640); DOELL = `doellinger_beitraege-zur-sektengeschichte-des-mittelalters-v2-lat-deu_1890.txt` (l.343-362); PG88 = `dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` (l.41436-41450, 43270-43310); SABAT = `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` (l.1-10, 46, 3795-3835, 4578-4592); ASMAR3 = `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` (l.1-3, 24700-24840); UNDERHILL = `underhill_jacopone-da-todi-poet-and-mystic_beck1919.txt` (l.8355-8420); ROBINSON = `francis-assisi_writings-of-saint-francis_robinson1906.txt` (l.2800-2812); LEMMENS = `leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt` (l.2810-2814); `acta-sanctorum_maii-tomus-6-lat_1739.txt` and `acta-sanctorum_junii-tomus-5-lat_palme1867.txt` (searched).

**Quotations.** All five quotations in double quotes match their files.
- Bernardino brief: "Chew, and chew, it would not go down!" matches ORL l.6860, the "!" included.
- Bernardino brief: "and we shall see what I have said that is wrong. I am one of those who wish to hold to that which Holy Church doth hold." matches ORL l.5832-5834, with the OCR allowance "Chureh". Robins leaves out a saying of Gregory that stands between the two sentences in the Italian (BANCHI2 l.11672-11675); the quote is Robins's English as printed, so it passes.
- Bernardino card: "who counts as the formal founder of the Observantines" matches LEA3 l.8229-8231. The file goes on with a full stop, so the stop outside the marks is right.
- Clareno card: "a man of the firmest and gentlest spirit" matches LEA3 l.3336-3337. The file runs on with a comma; the stop outside the marks is right.
- No quotation marks stand around the drafter's English of Latin, Italian or German. Each modern-words telling was checked against its lines. The Clareno letter of defense (EHRLE1 l.27862-27869), the hearing (EHRLE2 l.7693-7697), Simon's lament (CLAR l.1477), Sigonius (RAYN l.2392-2425), Glassberger (GLASS l.19790-19794) and Eugenius IV (BULN l.13124-13178) are told fairly. Two tellings add to their source (B-B1, B-B8) and one drops a hedge (B-B10).

**Audio.** Both audio scripts are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Pass for both.

**Scores as drafted.** Bernardino: 405 words, FK 7.50, Flesch 67.6. Clareno: 402 words, FK 7.79, Flesch 64.0. Both pass `grade_text`. Sentences over 25 words: Bernardino four (28, 26, 26, 25); Clareno one (31).

---

### bernardino-of-siena

**Verdict: five blocking findings (B-B1 to B-B5) and thirteen minor.**

**B-B1 (brief para 1: added detail, "bought" the chamois).**
- Current text: "He bought a Bible, and chamois skin to keep it dry."
- Source: he bought the Bible and went to buy the leather. ORL l.6840-6842: "And I bought the Bible, and I went to buy a piece of leather, of chamois skin, that water might not soak in at the sides of the book". The Italian is the same: "E comparai la Bibbia, e andai per comparare uno quoio di camoza" (BANCHI2 l.16150-16152). Neither says he got it.
- Fix: "He bought a Bible, and went to buy chamois skin to keep it dry."

**B-B2 (brief para 2: a Library file header used as a witness).**
- Current text: "For about forty-four years, writes Nazareno Orlandi, editing his sermons in 1920, he preached more often in town squares than in churches."
- Source: the year rests on the host record only. ORL l.6: "no year is legible in the OCR; the item's date field reads 1920 … Rights rest on the host date only." The records claim says the same ("The year 1920 is the host date only"). The preface is signed "N. O." (ORL l.324) and gives no year.
- Fix: "For about forty-four years, writes Nazareno Orlandi, editing his sermons, he preached more often in town squares than in churches." The card's `sources` date "1920" is a catalogue field and can stay.

**B-B3 (brief para 5: one late, partisan witness, and his outcome told as the narrator's fact).**
- Current text: "Nicolaus Glassberger, an Observant Franciscan who wrote a chronicle about 1508, says Dominican preachers accused him before Pope Martin V of leading people toward a kind of idolatry. The pope heard him, found nothing wrong, and let him preach everywhere."
- Source: the hearing and its outcome are Glassberger's alone: "Dominus autem Papa, audito beato Bernardino, nihil iniuste actum seu indiscretum praedicatum asserebat … licentiam ei praedicandi universaliter concessit" (GLASS l.19792-19794). The records tag it Inferential-Thin ("One late, partisan witness"). The witness comes loose at the full stop. In the first sentence, "him" can also be heard as Glassberger (B-M2).
- Fix: "He says Dominican preachers accused Bernardino before Pope Martin V of leading people toward a kind of idolatry. The pope heard him, Glassberger goes on, found nothing wrong, and let him preach everywhere." The sentence that introduces Glassberger is in B-M4.

**B-B4 (card `uncertain`, "When the Bologna story happened", and the records contested claim: a misread note).**
- Current text: "Raynaldus files the burning of the games and the painter of cards under 1424, after Sigonius. Mansi, in a note to the annals, says the annalist misdated the cardinal legate's term at Bologna, which began in August 1423."
- Source: Mansi's note (1) is attached to Raynaldus's sentence on Condulmer taking the Bologna legation, "Acccpta porro Bononiensi praefectura" (RAYN l.2371-2372). It is not attached to the Bernardino passage (l.2386-2426). The note says the legation "superiori anno mcdxxiii, die xvi Augusti coepisse, desiisse vero hoc anno die vii vel ix Junii" (l.2432-2435), so it ran from August 1423 to June 1424. Sigonius places the bonfire "post IV nonas Maii" (l.2412-2413), soon after the legate came ("Sub eos inde dies S. Bernadinus … in urbem venit", l.2397-2398). May 1424 falls inside the legation as Mansi dates it. No held line disputes the year of the Bologna story.
- Fix: delete this `uncertain` item. In `records.json`, delete the contested claim "Year of the Bologna story" and the claim "Card uncertain: Mansi's note in Raynaldus on Condulmer's legation …". The card's `place` line on Bologna can stay.

**B-B5 (records, card `uncertain` "Who accused him, and when", and brief para 5: a false "one witness", and a held own-voice account missed).**
- Current text: the records claim calls the Martin V accusation "Undated … One late, partisan witness". The card says Glassberger "gives no year", and the brief tells it from Glassberger alone.
- Source: Bernardino speaks of the Rome affair himself, in the 1427 Siena cycle: "Di quello che s'è fatto a Roma non dico nulla; che quando io v'andai, chi mi voleva fritto e chi arostito; e poi che ebbero udite le predicazioni che io lo' feci, chi avesse detto una parola contra a me, mal per lui" (BANCHI1 l.5337-5341, Predica quarta). Banchi's note on it: "San Bernardino s'era recato a Roma non molto prima, costrettovi dalle male lingue, che ne accusavano di poca ortodossia le dottrine e gl'insegnamenti" (l.5373-5375). His introduction says Bernardino "era stato chiamato a difendere dall'accusa di poca ortodossia i suoi insegnamenti", and that the pope then named him bishop of Siena (l.318-322). The note at l.6410-6412 gives that appointment by Martin V as 4 June 1427. So the Rome hearing has a second witness and a date before the Siena cycle. Banchi does not name the Dominicans or Manfred, so whether this is Glassberger's hearing remains an inference.
- Fix (brief para 5, after the B-B3 sentences): "Bernardino himself said at Siena in 1427 that at Rome some had wanted him fried, and some roasted. Banchi says he was called there to defend his teaching." (The offsetting cuts are in B-M4.)
- Fix (card `uncertain`): "Who accused him, and when. Glassberger, an Observant Franciscan writing about 1508, places an accusation before Pope Martin V by Dominican preachers with Manfred of Vercelli, and gives no year. Bernardino said at Siena in 1427 that at Rome some had wanted him fried and some roasted, and Banchi says he had been called there to defend his teaching. Eugenius IV's letter of 7 January 1432 names a different accuser, Michael, a priest of St Adalbert in Prague, who had charged him with heresy over the new sign of the name of Jesus. No witness says whether these were one case."
- Fix (records): change the claim's note "One late, partisan witness" to "Glassberger alone names the accusers and the outcome; Bernardino's own words (BANCHI1 l.5337-5341) and Banchi (l.318-322, 5373-5375, 6410-6412) witness a Roman hearing on his teaching before June 1427." Add a claim for the Rome sentence with those witnesses, Widely Accepted.

**B-M1 (brief para 1: "one" with no clear antecedent; Massa with no place).**
- Current text: "He went looking for one near Massa, could not choose a hill, and came home."
- Source: he was looking for a place to settle ("where I might lodge", ORL l.6843-6844; "dove io mi potesse appollaiare", BANCHI2 l.16154-16155). After the Bible and the chamois, "one" reads as a third purchase. Banchi's note on this Massa reads "La città … che fu patria del Santo" (BANCHI2 l.16176), and Banchi places his birth "in Massa Marittima" (BANCHI1 l.158-159).
- Fix: "He went looking for a place near Massa Marittima, could not choose a hill, and came home."

**B-M2 (brief para 5: "him" captures Glassberger).** Covered by the B-B3 fix ("accused Bernardino").

**B-M3 (brief para 4: "He drew a sun" can be heard as the painter).**
- Current text: "Bernardino told him to paint this instead. He drew a sun, and inside it the name of Jesus in a new form of letters."
- Source: the drawer is Bernardino: "S. Bernardinus respondit … ac circulo facto, solem in eo formavit" (RAYN l.2420-2424).
- Fix: "Bernardino told him to paint this instead, and drew a sun, with the name of Jesus inside it in a new form of letters."

**B-M4 (brief paras 5-6: "Observant" used a paragraph before it is defined; offsetting cuts).**
- Current text: para 5 calls Glassberger "an Observant Franciscan", and para 6 defines the term: "the Observants of Italy, the friars who kept the rule strictly".
- Fix (para 5 opening): "Nicolaus Glassberger, a friar of the Observance, the stricter Franciscan branch, wrote a chronicle about 1508." Its witness is GLASS l.96-104.
- Offsetting cuts for B-B5: delete "In 1439, Glassberger writes, Bernardino was made vicar general over all the Observants of Italy, the friars who kept the rule strictly." The card's `role` carries it. Also delete "Pope Nicholas V made him a saint at Pentecost 1450." The card's `dates` and `remembered` carry it. Also delete the opener "Bernardino preached devotion to the name of Jesus." Para 4 still shows the devotion through Sigonius's story.

**B-M5 (brief para 5: "another charge" settles what the card leaves open).**
- Current text: "Pope Eugenius IV quashed another charge, brought by Michael …"
- Source: the card says "No witness says whether the two were one case." "Another" tells it as a separate case.
- Fix: "In January 1432, Pope Eugenius IV quashed a charge brought by Michael, a Prague priest, and called Bernardino a fierce rooter-out of heresy." This also brings the sentence from 26 words to 23.

**B-M6 (brief para 6: the opening sentence takes Vespasiano's side before the dispute is told).**
- Current text: "In May 1444, on his way to preach at L'Aquila, he fell ill and died. His friend Vespasiano … says he died before reaching the town; Glassberger places his death in its friary."
- Source: "on his way" is Vespasiano's ("Innanzi che giugnesse all'Aquila, si ammalò … si morì", BANCHI1 l.1150-1157 in the Life). Glassberger has him die "in civitate Aquila in conventu sancti Francisci" (GLASS l.21739-21741). Surius has him die in his cell (RAYN l.60099).
- Fix: "In May 1444 he was sent to preach at L'Aquila, and he fell ill and died. His friend Vespasiano da Bisticci, a Florentine bookseller who wrote his Life, says he died before reaching the town. Glassberger places his death in its friary." The split also ends the 26-word sentence.

**B-M7 (brief para 7: first-person words outside the marks, and a close with no context).**
- Current text: "Say it to my face, he told his hearers, or write it to me, "and we shall see …""
- Source: ORL l.5829-5834. Without marks, "my face" and "to me" are heard in the narrator's voice. Read aloud, the line also floats free of what he was defending.
- Fix: "He dared his critics to say it to his face, or write it to him, "and we shall see what I have said that is wrong. I am one of those who wish to hold to that which Holy Church doth hold.""

**B-M8 (brief para 4 and card `place`: a name form the sources do not use; scholars with no time).**
- Current text: "The historian Carlo Sigonius, quoted in the church annals of Odoricus Raynaldus". The card's `place` also reads "Carlo Sigonius".
- Source: Raynaldus writes "Carolus Sigonius" (RAYN l.2393). "Carlo Sigonius" mixes the Italian and Latin forms. No held line gives Sigonius's or Raynaldus's time.
- Fix: "The historian Carolus Sigonius, quoted in the church annals of Odoricus Raynaldus, …" Make the same change in the card. Log the missing times in Open-Gaps under the common-name standard.

**B-M9 (brief para 3: "the Campo" undefined).**
- Current text: "stood in the Campo with wax tablets".
- Source: "in su la Piazza di Siena, detta il Campo" (BANCHI1 l.1257).
- Fix: "stood in the square called the Campo with wax tablets".

**B-M10 (card `place`: Vespasiano does not say Marittima).**
- Current text: "Massa Marittima, where Banchi and Vespasiano place his birth."
- Source: Vespasiano: "Santo Bernardino nacque a Massa" (BANCHI1, the first line of the Life, l.819). Banchi: "in Massa Marittima" (l.158-159). Orlandi's note: "Massa Marittima was his birthplace" (ORL l.2955).
- Fix: "Massa Marittima, where Banchi and Orlandi place his birth; Vespasiano says Massa."

**B-M11 (card `legacy.traces`: Glassberger does not place the exchange at Basel).**
- Current text: "Glassberger tells that at the Council of Basel Bernardino told John of Capistrano not to oppose the Observant friars beyond the Alps."
- Source: Glassberger tells of the minister general's attempt at Basel to break the Constance decree. Many Italian Observants agreed with him, Capistrano above all. "Unde hoc attendens beatus Bernardinus arguebat fratrem Iohannem" (GLASS l.20690-20708). He says nothing of where Bernardino said it.
- Fix: "Glassberger tells that when the minister general tried at the Council of Basel to undo the Observants' decree, Bernardino told John of Capistrano not to oppose the Observant friars beyond the Alps."

**B-M12 (card `otherNames`: a form no held line spells).**
- Current text: "Bernardino Albizzeschi".
- Source: ORL l.186-187: "Friar Bernardine Al-bizzeschi". The Italian has only "dell'Albizzeschi" (BANCHI1 l.532, 798). A search of all `cic/texts` found no "Bernardino Albizzeschi".
- Fix: "Bernardine Albizzeschi".

**B-M13 (card `sources`: the second volume is relied on and not listed).**
- Current text: one `ownWords` entry, "volumes 1 to 3", pointing to the v1 file only.
- Source: the sow-thistle story (BANCHI2 l.16120-16207) and the birthday sermon (BANCHI2 l.11051-11055, 11070) are in the separately vendored second volume.
- Fix: add an entry: title "Le prediche volgari … Volume secondo", author "Bernardino of Siena, as reported by Benedetto di maestro Bartolomeo; Luciano Banchi (ed.)", date "1884", language "Italian", file `cic/texts/bernardino-of-siena_prediche-volgari-1427-v2-ita_banchi1884.txt`. Narrow the first entry's title to volume 1 and its date to 1880.

**The Bernardino brief with every fix above:** 405 words, FK 7.21, Flesch 69.9 (`grade_text`). Its longest sentence is the closing line, 26 words to the first full stop inside the quotation. The text is in `/tmp/claude-0/-home-user-CIC-Project/3ea19bcb-cc32-5eac-a148-2940f6505916/scratchpad/r1b/bern.txt`. It uses the Glassberger opener "a friar of the strict Observant branch"; with B-M4's longer wording it is 407.

---

### angelo-clareno

**Verdict: seven blocking findings (B-B6 to B-B12) and thirteen minor.**

**B-B6 (card `dates`, card `uncertain` "When he was born", records `absent_details` "Birth year": a false absence).**
- Current text: "No witness gives his birth year." The absent_details note says all of `cic/texts` was searched.
- Source: SABAT l.4586: "2° Angelo Clareno da Cingoli (circa 1245-1337)". That is Paul Sabatier's apparatus to the Speculum perfectionis ("Nunc primum edidit Paul Sabatier", l.46). At l.3828 he writes, after Ehrle, that Angelo "prit l'habit franciscain peu après 1260". The file header's "c. 1255" (CLAR l.2) is rightly not used.
- Fix (`dates`, first sentence): "Paul Sabatier, editing the Mirror of Perfection, gives his life as about 1245 to 1337."
- Fix (`uncertain`): "When he was born, and where. Paul Sabatier gives about 1245, and no other witness gives a year. Oliger names Cingoli and Fossombrone, and thinks Fossombrone is more commonly and perhaps more rightly held."
- Fix (records): replace the absent_details entry with a claim, "Sabatier: 'Angelo Clareno da Cingoli (circa 1245-1337)'" (SABAT l.4586), Inferential-Thin. Add SABAT to the card's `sources.about`.

**B-B7 (brief para 5, card `dates`, card `uncertain` "When he died", records contested "Year of death": an unsupported "older writers" and a contested death day told as settled).**
- Current text: brief, "died there on 15 June 1337". Card `dates`: "Older writers had said 1348." Card `uncertain`: "Older writers gave 1348." Records: "1348, older writers (EHRLE1 l.28565-28567)".
- Source: EHRLE1 l.28565-28567 reads "dass Angelo am 15. Juni 1337, nicht erst 1348 starb". At l.27792-27797 Ehrle says only that the weekday also fits 1348, and rules it out because Simon died on 2 February 1348. Neither line says any writer gave 1348. The older writers the Library does hold are in the Bollandists' note in ASMAR3 l.24804-24817. Possevinus "mortuum putet 1294", and Arturus "mortuum ait an. 12340" (OCR, probably 1340) and put the day at 26 April. The Bollandists themselves, from the miracles that "coaevus D. Robertus de Mileto … paullo post sancti viri obitum scripsit", give "obiisse 14 Junii" (l.24815-24817). They add that Arturus lists him "inter Beatos ad 15 Junii" (l.24828-24829). Against this, Ehrle says the list of miracles names 15 June expressly (EHRLE1 l.27789-27790). So the day is contested between witnesses, and the 1348 side has no holder.
- Fix (brief): "He died there in June 1337, Ehrle reckons." (This is in the replacement brief below, with B-B8.)
- Fix (card `dates`): replace "Older writers had said 1348." with "The Bollandists, from a contemporary record of his miracles, give 14 June."
- Fix (card `uncertain`, "When he died"): "When he died. Ehrle fixed 1337 from a note dated by weekday at the end of the list of his miracles, as Daniel Papebroch, a Bollandist, had first reckoned it. In the first half of the fourteenth century that weekday fell on 13 June only in 1317, 1337 and 1348. Ehrle ruled out 1348 because Simon Fidati died early that year. Ehrle reads the list as naming 15 June. The Bollandists, from the same contemporary miracles by Robert of Mileto, give 14 June. Older writers they cite gave 1294 and a year the text prints as 12340."
- Fix (records): contested "Year of death": replace the second side with "Possevinus 1294; Arturus a Monasterio, as the Bollandists report him (ASMAR3 l.24804-24816)". Add a contested claim "Day of death", with sides "15 June: Ehrle from the list of miracles (EHRLE1 l.27789-27790); Oliger (CLAR l.1398-1399)" and "14 June: the Bollandists from Robert of Mileto's miracles (ASMAR3 l.24815-24817)". Add ASMAR3 to the card's sources.

**B-B8 (brief para 5: "fled" is added, and Oliger's hedge is dropped).**
- Current text: "Angelo fled to a hermitage in the Basilicata, in the south, and died there on 15 June 1337."
- Source: Oliger: "Sed Angelus eo tempore recessisse videtur in Italiam meridionalem, et quidem in Basilicatam, verosimiliter in eremitorium S. Michaelis de Basilicata … Mortuus est in eremitorio S. Mariae de Aspro" (CLAR l.1395-1399). That is "seems to have withdrawn", "probably" to one hermitage, and death at another. Ehrle: "nicht sehr lange vor seinem Tode begab er sich trotz seines hohen Alters in das Eremitorium in loco S. Marie de Aspro … wo er am 15. Juni 1337 starb" (EHRLE1 l.27770-27774). Neither says he fled. Placed straight after the 1334 arrest order, "fled" also gives him a motive no held line gives. No records claim carries "fled".
- Fix: "Not long before his death, the old man went to a hermitage in the Basilicata, in the south. He died there in June 1337, Ehrle reckons." Witness: EHRLE1 l.27770-27774, added to the records' death claim.

**B-B9 (brief para 2: a partial list read as the full list, and Ehrle's date told as fact).**
- Current text: "In a letter of 1317 Angelo lists the prisons he had known: Ancona, Forano, Rome, Viterbo and Assisi."
- Source: the letter runs on: "in carceribus plurimis Ancone, Forani, Rome, Viterbii, Asisii, in omnibus locis fratrum, que sunt a Roma usque ad Anconam" (EHRLE1 l.29195-29197). It goes on to further prisons at Ancona again and at Terra Nova (l.29221-29224). Oliger calls it "longa serie carcerum", in which these places come "primo" (CLAR l.1218). The year is Ehrle's dating: "Geschrieben im Sommer 1317, sei es nun …" (EHRLE1 l.29200), and the records claim says so.
- Fix: "In a letter Ehrle dates to 1317, Angelo names prisons he had known, first Ancona, Forano, Rome, Viterbo and Assisi."

**B-B10 (card `legacy.traces`, Rader: a hedge dropped).**
- Current text: "Matthaeus Rader, introducing his own Latin John Climacus, calls Angelo the first of all Climacus's translators. He reports that Ambrose of Camaldoli found that version obscure, word for word."
- Source: "Primus omnium interpres Climaci, quod sciam, fuit Angelus de Cingulo" (PG88 l.43283), that is, "as far as I know". The title notice says only that it "Latine primum reddita fuisse dicitur an. 1295" (l.41447). Rader also says Ambrose "Angeli nomen non exprimat", but describes him so that "res oculis tangi possit" (l.43306-43307).
- Fix: "Matthaeus Rader, a Jesuit, introducing his own Latin John Climacus, calls Angelo the first of Climacus's translators, as far as he knows. Ambrose of Camaldoli, Rader adds, found that version obscure, word for word, though Ambrose does not name him."

**B-B11 (card `uncertain` "When he died": a false "only").**
- Current text: "That weekday fell on 13 June only in 1317, 1337 and 1348."
- Source: Ehrle limits it to the first half of the century: "in der hier allein in Betracht kommenden, ersten Hälfte des 14. Jahrhunderts nur in den J. 1317, 1337 und 1348" (EHRLE1 l.27793-27795). Without the limit, the "only" is false. He also credits the reckoning to Papebroch: "wie schon Papebroch berechnete" (l.27792).
- Fix: carried in the B-B7 replacement for this item.

**B-B12 (README, "Names and ids": a contested identity told as settled).**
- Current text: "Angelo Tancredi and the Angelo of the Spoleto valley are different men."
- Source: Oliger, on John XXII's bull of 23 November 1331 against friars "sub ducatu Angeli de Valle Spoletana": "non liquet … edilorque Bullarii Franc. P. Eubel dubitat. Ad eam vero assumendam propensus videtur Raynaldus … et eam sustinet F. Tocco … aliique" (CLAR l.1418-1424). Raynaldus and Tocco hold that he is Clareno, and Eubel doubts it.
- Fix (README): "Angelo Tancredi is a different man. Whether the "Angelo of the Spoleto valley" of the 1331 bull is Clareno is open: Raynaldus and Tocco think so, Eubel doubts it, and Oliger leaves it unsettled." Fix (card `uncertain`, a new item after the 1334 item): "Whether a bull of 1331 was aimed at him. John XXII's bull of 23 November 1331 names a leader, Angelo of the Spoleto valley. Raynaldus and Francesco Tocco take him for Clareno, Eubel doubts it, and Oliger says it is not clear." Note: "F. Tocco" is Oliger's form, and EHRLE3 l.22702 has "Prof. F. Tocco". Use "Professor F. Tocco" if no held line spells "Francesco".

**B-M14 (brief para 5 and card: the weekday reckoning credited to Ehrle alone).**
- Current text: brief, "Ehrle worked out the year from the weekday given in a note on his miracles." Card `dates`: "Ehrle reckoned the year from a weekday in a note on his miracles."
- Source: "wie schon Papebroch berechnete" (EHRLE1 l.27792). Ehrle adds the exclusion of 1348 (l.27795-27797, 28562-28567). Ehrle names him "der Bollandist Papebroch" (l.27540) and "Daniel Papebrochius" (l.27601).
- Fix (brief): the sentence is replaced by "He died there in June 1337, Ehrle reckons." (B-B8). Fix (card `dates`): "The year is Ehrle's reckoning, from a weekday first worked out by Daniel Papebroch, a Bollandist."

**B-M15 (brief para 1: first-person words heard as the narrator's).**
- Current text: "I did not leave them, the friar answered; ask them why they threw me out."
- Source: EHRLE2 l.7695-7696, Latin; the drafter's English is rightly unquoted. Unquoted, though, "I" and "me" open the sentence in the narrator's voice.
- Fix: "He had not left them, the friar answered; they should be asked why they threw him out."

**B-M16 (brief para 4: a 31-word sentence).**
- Current text: "In his letter of defense, Angelo wrote that he and his brothers were no heretics, unless it was heresy to believe and practice, humbly, what Francis believed about keeping his rule. That heresy, he wrote, he had always held and held still."
- Source: EHRLE1 l.27862-27869.
- Fix: "In his letter of defense, Angelo wrote that he and his brothers were no heretics. If it was heresy to believe and practice humbly what Francis believed of his rule, he wrote, he had always held that heresy and held it still."

**B-M17 (brief paras 1, 4, 5: one group, two names; and "led the Spirituals" says more than Oliger).**
- Current text: para 1 has "a chronicle of the Franciscan rigorists", para 4 has "Angelo led the Spirituals, the friars who wanted Francis's rule kept to the letter", and para 5 has "the Fraticelli, the condemned rigorist friars".
- Source: "rigorists" is used both for the Spirituals and for the Fraticelli (checklist 9). Oliger: "Ei successit in regimine fratrum Spiritualium" (CLAR l.1294-1295). That is Liberatus's group; Ubertino and the Provençal Spirituals stood apart (EHRLE2 l.7670-7690).
- Fix: para 1, "a chronicle of the Spirituals, the friars who wanted Francis's rule kept to the letter". Para 4, "After Liberatus died in 1307, Angelo led his band of Spirituals." Para 5 keeps "the condemned rigorist friars" for the Fraticelli.

**B-M18 (brief para 3 and card `role`: a namesake with no place).**
- Current text: brief, "he and his leader Liberatus". Card: "leader of the Spirituals after Liberatus".
- Source: "Fr. Liberatus a Macerata" (CLAR l.1208, 1288). Liberatus is a common name (Liberatus of Carthage).
- Fix: brief, "he and his leader, Liberatus of Macerata,". Card, "leader of the Spirituals after Liberatus of Macerata".

**B-M19 (brief para 3: "Armenia" misleads a modern listener).**
- Current text: "he went as a missionary to Armenia."
- Source: "Hoc vero nomine non intelligenda est antiqua Armenia, sed regnum Armeniae in Cilicia" (CLAR l.1191-1192). The card already says "Cilician Armenia".
- Fix: "he went as a missionary to the Armenian kingdom in Cilicia."

**B-M20 (brief para 5: a scholar with no role; Subiaco with no place).**
- Current text: "The pope soon let him go, Henry Charles Lea writes … Back in Italy, he lived mostly at Subiaco."
- Source: LEA3, the Inquisition history (title page l.54, "1888"). Oliger: "suosque rexit in regione Urbis, morans ut plurimum Sublaci" (CLAR l.1344-1345).
- Fix: "The pope soon let him go, writes the historian Henry Charles Lea, and allowed him the Celestine habit and rule. Back in Italy, he lived mostly at Subiaco, near Rome."

**B-M21 (brief para 6: a late single witness told as fact; Simon's own words held).**
- Current text: "Simon Fidati of Cascia, who had first studied under him as a boy, mourned him in a lament."
- Source: "as a boy" rests on a cult decree of 17 August 1833, quoted by Oliger (CLAR l.1434-1437), and is tagged Widely Accepted. Simon's own lament says "Predicabam catheticatus ab ipso" (CLAR l.1490, 1507) and calls him "doctor discipulo" (l.1485). Oliger: "quem patrem spiritualem et magistrum coluerat" (l.1405), and Simon is "O. S. A." (l.1404).
- Fix: "Simon Fidati of Cascia, an Augustinian preacher whom Angelo had taught, mourned him in a lament." Records: add CLAR l.1485-1490 to the claim. Tag the 1833 decree's "a teneris annis" Inferential-Thin if it is kept anywhere.

**B-M22 (card `uncertain` "Whether the 1334 arrest order was aimed at him", and records: a Contested tag with no other side; a held witness missed).**
- Current text: "The bull does not name the heretic … Eubel adds Angelo's name in brackets." The records tag it Contested.
- Source: no held line says the bull meant someone else. An inquisition record of 28 February 1334, a week after the bull, from the same inquisitor Simon of Spoleto to whom its second copy is addressed (BUL5 l.84637-84639), has a friar say their general "est frater Angelus Clarani de Fossabruno, qui alias fuit vocatus frater Petrus de Fossabruno" (EHRLE4 l.594, 648-650). Eubel's note cites this volume ("Denifle-Ehrle l. c. IV, 16", BUL5 l.84605). Oliger states it plainly: "Iohannes XXII edidit bullam contra Angelum" (CLAR l.1394). The record is an inquisitor's, of a questioned man.
- Fix (card): "Whether the 1334 arrest order was aimed at him. The bull does not name the heretic who called himself head of the Fraticelli, and Eubel adds Angelo's name in brackets. A week later, a friar questioned by the inquisitor Simon of Spoleto named Angelo Clareno as the Fraticelli's general." Records: tag Dominant Modern Reconstruction (Eubel, Oliger), add EHRLE4 l.648-650, and add EHRLE4 to the card's sources.

**B-M23 (card `knownFor`: "exiled" is not in the sources).**
- Current text: "He was jailed in Italy, exiled to Greece and questioned at Avignon".
- Source: "ut Italiam relinquere et in Graeciam confugere statuerint zelantes" (CLAR l.1245). They chose to flee; no one exiled them.
- Fix: "He was jailed in Italy, fled with his brothers to Greece and was questioned at Avignon".

**B-M24 (card `place`: Ehrle's identification told as a name).**
- Current text: "first on an island Ehrle names as Trixonia."
- Source: "in parva quadam insula, cuius nomen et situs ignorantur, a P. Ehrle vero argumentis non spernendis ut Trixonia … determinatur" (CLAR l.1249-1251).
- Fix: "first on a small island whose name is lost, which Ehrle identifies as Trixonia."

**B-M25 (card: scholars with no role or time at first mention).**
- Current text: "Luke Wadding writes …" (`remembered`), "Ehrle reports doubts from Richard and from Tocco" and "Annibali da Latera, after Wadding" (`uncertain`).
- Source: Ehrle gives "Wadding (1625), der als der erste die historia ausgiebig für seine Annalen verwerthete" (EHRLE2 l.5716-5717). For Tocco: "Prof. F. Tocco" (EHRLE3 l.22702). Annibali's Supplement is cited by page (EHRLE1 l.27824). No held line gives Richard's time.
- Fix: "Luke Wadding, the Franciscan annalist of the 1620s, writes …"; "Ehrle reports doubts from Richard and from Professor F. Tocco"; "Annibali da Latera, in his Supplement to the Franciscan Bullarium, after Wadding". Log Richard's missing identifier in Open-Gaps.

**B-M26 (card `role`: "by his own words" rests on the Historia).**
- Current text: "never a priest by his own words".
- Source: the words are his reply as the History of the Seven Tribulations reports it (EHRLE2 l.7709-7711), a work whose authorship the card itself marks as uncertain.
- Fix: "never a priest, by his answer to the pope in the History of the Seven Tribulations".

**The Clareno brief with every fix above:** 406 words, FK 7.93, Flesch 63.3 (`grade_text`); the longest sentence is 27 words (the heresy sentence of B-M16). It keeps "the Fraticelli, the condemned rigorist friars". If a cut is wanted, "head of the condemned Fraticelli" brings it to 403 (FK 7.87, Flesch 63.5), at the cost of the definition. Both texts are in `/tmp/claude-0/-home-user-CIC-Project/3ea19bcb-cc32-5eac-a148-2940f6505916/scratchpad/r1b/` (`ang407.txt`, 406 words; `ang.txt`, 403 words).

---

### records.json (these profiles)

- **bernardino-of-siena.** Every claim's witness lines were opened, and the lines say what the claims quote. There are three faults. The Bologna contested claim and the Mansi claim rest on a misread note (B-B4). The Martin V claim is called "one late, partisan witness" although Bernardino's own words and Banchi are held (B-B5). The death claim should add Surius's "Vixit in terris annis sex et sexaginta … quadraginta … praedicavit" (RAYN l.60109-60111) to the preaching-years contested claim, since Surius gives forty years too. The absent_details on his Latin works says only the file list was searched. A content search for "Vangelo eterno", "De evangelio aeterno" and "Sermones" near his name found nothing more, so the note stands, but it should say a content search was run.
- **angelo-clareno.** The birth-year absent_details is false (B-B6). The "Year of death" contested claim's second side has no holder (B-B7). A day-of-death contested claim is missing (B-B7). The 1334 claim's Contested tag has no other side (B-M22). The Rader claim drops "quod sciam" (B-B10). The death claim needs EHRLE1 l.27770-27774 for "went … not long before his death", and nothing supports "fled" (B-B8). Simon's claim leans on the 1833 decree (B-M21). The absent_details on his Climacus, Macarius and Basil versions stands: no held file holds them, and the hits are notices only (PG88; EHRLE1 l.27670-27673). The absent_details on a full Historia stands (CLAR l.1645).

### Census (origin/main)

- Both card traditions are census names: "Observant Reform & Popular Preaching" (`observant-reform-and-popular-preaching`) and "Fraticelli (Spiritual Franciscan rigorists)" (`fraticelli-spiritual-franciscan-rigorists`). Bernardino is a voice of the first. Clareno is the first voice of the second and also a voice of `franciscan-order-era-6`.
- For Open-Gaps (no census edit proposed):
  1. The Fraticelli `voices` line ("author of their own history of the order's persecutions"), the Franciscan Order `voices` line ("wrote their own history of the order's persecutions"), and the Fraticelli `sources` entry titled "Angelo Clareno, A Chronicle or History of the Seven Tribulations" all tell the authorship as settled. The held sources contest it: Affò (EHRLE2 l.5756-5763), Richard and Tocco as Ehrle reports them (EHRLE2 l.5822-5835; EHRLE3 l.22700-22712), and Ehrle's own "muthmassliche Verfasser".
  2. The Observant entry's `legacy` ("the radiant IHS monogram that Bernardino held up at the end of his sermons") and its story ("the name of Jesus painted on a tablet he held up") tell a held-up tablet that no held line shows (records absent_details, searched again here). This is unsupported rather than contested.
  3. The same story says Benedetto "had taught himself a shorthand" and went "every morning before dawn". The held lines speak only of wax tablets and a stylus (BANCHI1 l.1263-1266; ORL l.248-252). This is also unsupported, not contested.

### README (lines about these two)

- True: the opening lines for both; "said plainly to be Benedetto's report"; "told as two records"; "His place and age at death differ by witness"; the held-witness and correction lists for both (checked: BULN l.575 and 1109 name only Capistrano; GLASS l.16242-16268; EHRLE2 l.5678-6150 and 7669-7740; the 1334 bracket); the tradition placings; the word and score ranges (405 and 402 words; FK 7.50 and 7.79; Flesch 67.6 and 64.0, inside the stated 402-406, 6.6-8.8 and 61.6-73.8).
- Not true as written: "Angelo Tancredi and the Angelo of the Spoleto valley are different men" (B-B12). "His death year is Ehrle's reckoning" is incomplete, because the weekday reckoning is Papebroch's first (B-M14). "Peter of Fossombrone was his earlier name, and the card gives it": the card gives the Latin "Petrus de Forosempronio" only.
- Not verified: "the Carmelite Bernardinus de Senis". A file that could hold him is held (`carmelite-general-chapters_acta-capitulorum-generalium-v1-1318-1593-lat_wessels1912.txt` matches the name), but I did not open it.

### Checklist summary

| # | Item | bernardino-of-siena | angelo-clareno |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Fail (B-B2, B-B3, B-B4, B-B5) | Fail (B-B6, B-B7, B-B9, B-B11) |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | No invented detail | Fail (B-B1) | Fail (B-B8, B-M23) |
| 4 | Reading aids, no AI tells | Fail (B-M1, B-M3, B-M4, B-M7, B-M9) | Fail (B-M15, B-M16, B-M19, B-M20) |
| 5 | No role for a named witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass (Glassberger placed as an Observant; Paulinus not used) | Pass (Paulinus marked hostile) |
| 7 | Contested claims shown both sides | Fail (B-B4 invents a dispute; B-M6 leans) | Fail (B-B7, B-B10, B-B12) |
| 8 | Common names have a place | Fail (B-M1 Massa, B-M8) | Fail (B-M18) |
| 9 | One term for one thing | Fail (B-M4) | Fail (B-M17) |
| 10 | Story, scene first, disputes in place, length | Pass | Pass |
| 11 | `grade_text` | Pass (FK 7.50, Flesch 67.6) | Pass (FK 7.79, Flesch 64.0) |
| 12 | Card order, missing fields, caveat repeated | Pass (sources incomplete, B-M13) | Pass |
| 13 | Audio tags | Pass | Pass |
| 14 | List line kept; Who test | Pass | Pass |

### Count

- **bernardino-of-siena:** 5 blocking (B-B1 to B-B5), 13 minor (B-M1 to B-M13).
- **angelo-clareno:** 7 blocking (B-B6 to B-B12, B-B12 being in the README), 13 minor (B-M14 to B-M26).

---

## Era 6 Who batch 2, round 1 review: PART C

**Scope.** `william-of-ockham` and `nicholas-cabasilas`: brief, card, audio script and `records.json` entry for each, the README lines about them, and the census text for their two traditions. Branch `claude/cft-who-era6-batch2` at a5ce67a7. No repo file edited; no web, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, lessons.md, the batch README, the scan rulings (Who_Scan_Era6.md l.15-56), the scan rows (l.101 Ockham, l.117 Cabasilas) and the File key, and Part A of the batch 1 R1 review for layout. For every brief sentence and card field I opened the cited lines with 20 or more lines of context. Quotations were checked by eye against the file, allowing for whitespace, case, hyphen breaks and OCR. Modern-words tellings of Latin, Greek, Italian and German were checked against the original lines. False-absence checks used a windowed regex script over all 1,771 files in `cic/texts/` (headers skipped, hyphen breaks joined). Name forms: Occam, Ockham, Okam, Ockam, Ocham, Okkam, Occham, Hokham; Cabasil-, Kabasil-, Καβάσιλ-, Καβασίλ-, Καδάσ-, Кавасил-. Context words: born, natus, geboren, Surrey, Merton, Oxford, inceptor, provincial, obiit, mortuus, died, ἐτελεύτ-, Thessalon-, archiep-, metropol-, μητροπολ-, ἀρχιερ-, Erzbisch-; razor, "entia non sunt multiplicanda", "frustra fit per plura". `grade_text` was run on the current briefs and on each proposed revision.

**Files opened (cic/texts/).**
- CARL = `carlini_fra-michelino-e-la-sua-eresia-ita-lat_1912.txt`, l.1-12, 4690-4705, 5320-5352, 6250-6295, 8630-8705, 9510-9540, 10695-10720, 12815-12825, 13140-13200.
- BUL5 = `bullarium-franciscanum_v5-lat_eubel1898.txt`, l.2200-2207, 3445-3460, 42395-42520, 54315-54332, 54375-54410, 54690-54705, 58500-58515, 59012-59075, 59245-59255, 63278-63290, 65190-65202, 72695-72745, 86110-86128, 86255-86263, 93684.
- LEA3 = `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt`, l.6470-6520, 6790-6870, 7095-7115, 7430-7495.
- GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt`, l.1-12, 100-125, 11135-11160, 11512-11524, 12540-12557, 13520-13562.
- SCHOLZ = `scholz_unbekannte-kirchenpolitische-streitschriften-v2-lat_1914.txt`, l.1-14, 155-175, 20025-20042, 21020-21042, 22600-22700, 22755-22770, 22805-22840, 25805-25875.
- FZ = `fasciculi-zizaniorum_shirley1858.txt`, l.1-10, 203, 3070-3090, 3355-3372.
- GERSON = `gerson_opera-omnia-tomus-2-pars-1-tractatus-ad-schisma-lat_dupin1706.txt`, l.27008-27030, 27180-27214.
- LUTHER4 = `luther_works-v4-selected_various1931.txt`, l.15634-15652, 16772-16782.
- REUSCH = `reusch_indices-librorum-prohibitorum-sechzehnten-jahrhunderts-deu-lat_1886.txt`, l.15708-15716, 16972-16982.
- CATHAY = `cathay-and-the-way-thither_vol3-...yule-cordier1914.txt`, l.10485-10496.
- VAUGHAN = `wyclif_tracts-and-treatises_vaughan1845.txt`, l.738-758, 22058-22066.
- HILTON = `hilton_scale-or-ladder-of-perfection_dalgairns1908.txt`, l.1-14, 112-125, 205-222, 2426-2436.
- MATTHEW = `wyclif_english-works-hitherto-unprinted_matthew1880.txt`, l.498-508.
- MANSI25 = `mansi_sacrorum-conciliorum-collectio-tomus-25-1300-1344-lat_welter-facsimile1903.txt`, l.42486-42496, 42563-42572.
- BALUZE = `baluze_vitae-paparum-avenionensium-v1-lat_mollat1921.txt` (searched; no Ockham or Cesena line).
- CANT2 = `cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt`, l.24900-24940, 32120-32175, 34020-34032.
- CANT3 = `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt`, l.6380-6450, 6475-6520, 16348-16378, 16520-16640.
- PG150 = `palamas_opera-omnia-pg150-grc-lat_migne1865.txt`, l.1-12, 161, 340-348, 26050-26200, 26405-26500, 35852-35866, 36555-36600, 44340-44395, 49308-49320.
- GASS = `cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt`, l.1-10, 1225-1240, 1365-1420, 1448-1492, 1770-1850, 1872-1942.
- ACTA = `acta-et-diplomata-graeca_acta-patriarchatus-constantinopolitani-1315-1402-v1-grc-lat_miklosich-mueller1860.txt`, l.13950-13962, 14055-14072.
- PHRAN = `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt`, l.1-12, 7950-7996.
- PG155 = `symeon-thessalonica_opera-omnia-pg155-grc-lat_migne1866.txt`, l.1-12, 350-360, 796-808, 9215-9240.
- GREG2 = `gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt`, l.28590-28612, 47120-47140.
- PALL = `pallavicino_istoria-del-concilio-di-trento-tomo3-libri17-24-ita_classici-sacri1846.txt`, l.7630-7655.
- PO15 = `patrologia-orientalis-tomus15_petit-documents-concile-de-florence-purgatoire-grc-fra_graffin-nau1927.txt`, l.1-10, 470-660.
- COVEL, MANSI46 and PG161 (Bessarion): search hits only.
- Census: `git show origin/main:cic-website/data/world-census.json`, movements 116 (Hesychasm), 124 (Fraticelli), 131 (Franciscan Order, era 6).

**Quotations.** Every passage in double quotes in these two profiles:
- Ockham brief: "There was nothing sure but Scripture." The words match LEA3 l.6822 ("There  was  nothing  sure  but  Scripture ;"). The file has a semicolon where the brief puts a full stop inside the marks (C-M2).
- Ockham brief and card: "the glory and the reproach of his order". This matches FZ l.3081-3082.
- Ockham card: "Occam, my dear master". This matches LUTHER4 l.16777. It is the 1931 English translation, held in English, and the comma sits rightly outside the marks.
- Ockham card: "more than doubtful". This matches LEA3 l.6838.
- Cabasilas: no double quotes in the brief or the card. The Greek of Kantakouzenos and Cabasilas, the Latin of Fabricius and Hervet, and the German of Gass are all told in modern words, with no marks.

Checks of the modern-words tellings: the Ockham tract (SCHOLZ l.25859-25868) drops a qualifier (C-M3). The 1323 letter (BUL5 l.42407-42452) drops a condition (C-B1). The Dialogus line is Ambrose's, quoted inside the master's argument (C-M8). In Cabasilas, the Petit side is reversed (C-B3). The Life in Christ tellings are close to PG150 l.35858-35860, 36560-36592 and 44358-44389; they have writing faults but no fidelity fault (C-M20). The 1353, 1346 and 1349 tellings match CANT3 l.16595-16634, CANT2 l.32137-32169 and CANT3 l.6394-6427. The tellings of Hervet (PG150 l.26426-26494), the 1350 synod record (ACTA l.14063-14068) and the windows line (PG150 l.36590-36592) also match.

**Audio.** Both scripts are the brief exactly (checked by diff after the tags were stripped). Each has `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and nothing else. Pass for both.

---

### william-of-ockham

**Verdict: one blocking finding (C-B1); otherwise passes with minor fixes.** 404 words; `grade_text` FK 8.08, Flesch 62.2. With every fix below applied, it runs 407 words, FK 8.22, Flesch 62.3.

**C-B1 (brief para 3; records "The 1323 summons": a dropped condition, so a report is told as fact).**
- Current text: "He also ordered the bishops of Bologna and Ferrara to summon an English friar named William, who had preached the friars' view."
- Source: the letter says only that a report had reached the pope ("ad nostri apostolatus auditum infesta produxit relatio, quod Guillelmus dictus Anglicus ... praesumpsit"). The bishops were to find out first, and to cite him only "si ea repereritis veritate fulciri" (BUL5 l.42413-42444). Lea, the witness named in the sentence before, says the same: "to investigate the truth of the report, and if it was correct to cite Ockham" (LEA3 l.6499-6501).
- Why it matters: this is the friar whose identity is in doubt in the very next sentence. The brief tells as settled that he preached it, and both witnesses hedge.
- Fix (two sentences, +9 words): "He also told the bishops of Bologna and Ferrara to summon an English friar named William. They were to do so if they found he had preached the friars' view at Bologna."
- Records: add to the claim "If the report is true: 'si veritas suffragetur relatibus', 'si ea repereritis veritate fulciri' (BUL5 l.42437-42444)".

**C-M1 (brief para 4: the witness came loose from "Benedict XII").**
- Current text: "For some twenty years, Lea writes, William wrote against John XXII and Benedict XII."
- Source: Lea has "for twenty years he poured forth a series of controversial works in defence of the cause" and "merciless were his assaults on the errors ... of John XXII" (LEA3 l.6815-6817, 6835-6836). Lea never names Benedict XII as William's target. That name comes from Scholz's titles (SCHOLZ l.165-167), and the card already has it.
- Fix (−2): "For twenty years, Lea writes, William poured out works in their defense."

**C-M2 (brief para 4: a quoted sentence heard as the narrator's, with the wrong stop).**
- Current text: "In Lea's summary, William argued that a pope can fall into heresy, and so can a council. "There was nothing sure but Scripture.""
- Problem: in the audio the marks vanish, so the second sentence is heard as the narrator's own claim. The file also reads "Scripture ;" (LEA3 l.6822).
- Fix (+2): "In Lea's summary, William argued that a pope can fall into heresy, and so can a council, and that "there was nothing sure but Scripture"."

**C-M3 (brief para 5: a qualifier dropped from his own words).**
- Current text: "He went into persecution knowingly, he says, and did not mean to flee it."
- Source: "Persecutioni igitur scienter me ingerens et eam fugere non intendens, quamvis forte si esset necesse vel aliquando mihi videretur expediens ... uterer licentia Christi dicentis ...: Cum vos persequentur in civitate illa, fugite in aliam" (SCHOLZ l.25852-25858). He keeps Christ's leave to flee from one city to another. In a brief built on his flight, the shortened line reads as a contradiction he did not make.
- Fix (−6): "He brought persecution on himself knowingly, he says."
- Alternative, if the beat is wanted (+11; it then needs its own cut): "He went into persecution knowingly, he says, and did not mean to flee it, though Christ allowed flight from one city to another."

**C-M4 (brief para 3: a thesis opener that ties the heresy case to poverty).**
- Current text: "The quarrel was over poverty."
- Problem: the line opens the paragraph on a thesis. Coming straight after the paragraph on the case against William, it also tells the listener that the case was about poverty. The 1328 and 1330 letters speak only of "multarum opinionum erronearum et haereticarum, quas ipse scripserat" (BUL5 l.54697-54700, 72733-72739). Carlini says he was already under suspicion "per altre dottrine" (CARL l.5336-5337).
- Fix (−5): delete the sentence. The paragraph then opens "Michael's friars held that Christ and the apostles owned nothing."

**C-M5 (brief para 2: "lords in ... England").**
- Current text: "Letters ordering his arrest went to bishops and lords in Germany and England."
- Source: German bishops (BUL5 l.58508-58512), the margrave of Baden and other German lords (l.3451, 59017-59072), the English bishops, and the King of England, asked to help (l.3455, 59248-59253). No English lords are named.
- Fix (−4): "Letters ordering his arrest went to Germany and England."

**C-M6 (brief para 1: an unclear "it", and Carlini without a role).**
- Current text: "Armando Carlini, writing in 1912, dates it to the night of 26 May."
- Problem: "it" has no noun before it (the sentence before is about the boat and galley), and Carlini has no role. The file is his 1912 study (CARL l.1-12, 6268-6278).
- Fix (+1): "Armando Carlini, in a 1912 study, dates the flight to the night of 26 May."

**C-M7 (brief: witnesses at first mention without a time or role).**
- Lea has a role but no time. Fix (+2): "In 1323, writes Henry Charles Lea in his 1888 history of the Inquisition, the pope declared that view heretical."
- Wadding has a role but no time. "saeculo septimo decimo" is at BUL5 l.86114-86116. Fix (+1): "Luke Wadding, a seventeenth-century Franciscan annalist, ..."
- Glassberger has neither. The Quaracchi preface says "Occupatus erat in scribendis his Chronicis an. 1508" (GLASS l.106), and the title page calls him "Ordinis Minorum Observantium" (GLASS l.1). Fix (+3): "...to Munich, writes Nicolaus Glassberger, an Observant chronicler of about 1508."
- Offsetting cuts: "several" and "already" in para 2 (−2): "In 1330 the pope added that doctors examining William's writings had found many articles heretical." Para 6 (−1): "Walter Shirley, editor in 1858 of a Carmelite collection against Wyclif, called him "the glory and the reproach of his order"."

**C-M8 (card keyWorks, Dialogus: the line is Ambrose's, inside the master's argument).**
- Current text: "There William writes that the Christian religion takes no one's right from him."
- Source: the words are a quotation. "Ait enim Ambrosius super epistolam ad Titum: ... quia christiana religio neminem privat iure suo" (SCHOLZ l.22690-22696). The master of the dialogue uses them in an argument he says "multipliciter videtur posse probari" (l.22683-22686: "Nam religio christiana et per consequens Christus neminem, eciam secularem et infidelem, privavit iure suo").
- Fix: "There the master of the dialogue argues, with Ambrose, that the Christian religion takes no one's right from him, even an unbeliever's."
- Records: cite SCHOLZ l.22682-22696 and say that the line is Ambrose's, quoted.

**C-M9 (card legacy traces, Gerson: an argument with no context).**
- Current text: "...that William built an argument in his Dialogus."
- Source: "Hanc autem materiam latissime & studiosissime prosecutus est, & fundavit Ockam in Dialogo suo" (GERSON l.27205-27206). The tract was written on the occasion of the Polish envoys' appeal to a future council (l.27012-27016).
- Fix: "Jean Gerson wrote in 1418, near the close of the Council of Constance, in a tract on an appeal from the pope to a council, that William had argued the matter at length in his Dialogus."

**C-M10 (card legacy traces, Luther: the words cut off from what they introduce).**
- Current text: "Martin Luther calls him "Occam, my dear master", in his Exhortation to the Clergy at Augsburg of 1530."
- Source: the phrase opens a charge in a list of the schoolmen's faults: "Occam, my dear master, writes that it cannot be proved from the Scriptures that man needs the grace of God in order to do a good work. These are the best of them" (LUTHER4 l.16776-16780). Cut off there, it reads as plain praise.
- Fix: "Martin Luther, in his Exhortation to the Clergy at Augsburg of 1530, calls him "Occam, my dear master", and says he wrote that Scripture cannot prove that man needs God's grace to do a good work."

**C-M11 (card uncertain, "His birth and early life": Dalgairns misdated).**
- Current text: "...and J. B. Dalgairns in 1908 connect him with Merton College at Oxford."
- Source: Dalgairns's essay first appeared with the 1870 edition and is "also reprinted in this volume" (HILTON l.212-217). The Library header gives his dates as 1818-1876. Dalgairns also puts the Merton link in "some writers'" mouths: "Some writers have connected him with Ockham, because Merton College had the honour of producing both" (l.2431-2433).
- Fix: "...and J. B. Dalgairns, in an essay of 1870 reprinted in 1908, connect him with Merton College at Oxford."

**C-M12 (card otherNames: a form not held).**
- Current text: "Wilhelmus de Occam".
- Source: no file has it. The held form is "Wilhelmus Occam" (SCHOLZ l.21026, Clement VI in Konrad of Megenberg).
- Fix: replace it with "Wilhelmus Occam".

**C-M13 (card sources ownWords: the Carlini appendix is Michael's words, not William's).**
- Current text: an ownWords entry "Michael of Cesena's protest of 1338 at Munich, with William's signature".
- Source: Carlini prints Michael's protest. For William he gives only "Ego, predictus frater Guillermus de Ocham .... (segue come per H. de Thalem: mancan solo le parole: et judico)" (CARL l.13195-13196), which is not William's text.
- Fix: remove the entry from ownWords. Fold "the 1338 protest at Munich, with William named as a witness" into the existing Carlini entry under "about".

**C-M14 (card: names at first mention without a role or time).**
- knownFor, "Henry Charles Lea": fix "In the summary of Henry Charles Lea, writing a history of the Inquisition in 1888, ...".
- dates, "Armando Carlini, writing in 1912": fix "Armando Carlini, in a 1912 study of Michael of Cesena, ...".
- dates, "Nicolaus Minorita", "Riezler and Müller": these are named with no role. Carlini's note gives only their works: "Il Riezler: Literar. Widersacher (Leipzig, 1874)", "il Müller, o. c." and "Nicolaus Minorita" (CARL l.6281-6283). Lea cites "Nicholaus Minorita (Bal. et Mansi III. 238-40)" (LEA3 l.7105). No held line read here gives his time. Fix: "after Nicolaus Minorita, whom Lea also cites; he notes that Riezler, writing in 1874, and Müller give the 25th." Log Nicolaus Minorita's missing time as a gap.

**C-M15 (card uncertain, "Whether his writings were heretical": Wyclif's line widened, and "inceptor" left undefined).**
- Current text: "Wyclif, as Shirley quotes him, says that whoever calls the venerable inceptor a heretic cannot prove it."
- Source: "Assumit quod venerabilis inceptor Hokham fuit haereticus, quod nescit probare" (FZ l.3362-3364). One opponent "assumes" it; there is no "whoever".
- Fix: "Wyclif, as Shirley quotes him, says that an opponent who takes him for a heretic cannot prove it, and calls him the venerable inceptor, a title for a beginning master."
- If "a title for a beginning master" cannot be shown from a held line, cut it and the term: "...cannot prove it."

**C-M16 (card place: "his tombstone").**
- Current text: "England, which the papal letters and his tombstone give as his country."
- Source: Carlini says that after the 1802 demolition only "una lastra di macigno quadrato fu risparmiata: trovavasi nella chiesa vicino all' altar maggiore e portava un nome" (CARL l.8690-8698). That is a stone slab near the high altar, bearing his name. Carlini does not call it his grave.
- Fix: "England, which the papal letters give as his country, as does a stone from the Munich church that Carlini reports."

**C-M17 (README, Quotations line: incomplete).** The README says marks are kept only for Scudder, Thorold, Cumming, Robins, Lea and Shirley. The Ockham card also quotes Luther in the 1931 English (LUTHER4 l.16777), which is correct under the rule. Fix: add "the 1931 English Luther" to that list.

**Not counted (an observation for records).** Carlini says Ockham signed the Perugia decision of 1322: "Fu la sentenza perugina firmata da Michelino, da Guglielmo Ockam" (CARL l.4698-4700; again at l.5326-5329). Eubel says the English William who signed at Perugia was William of Alnwick (BUL5 l.42504-42507), and the Yule-Cordier note puts Ockham at "a council held at Assisi in 1322" (CATHAY l.10492-10494). These are held witnesses on his life before 1323, and they are not in records. They could go under the 1323-identity contested claim. The card's "No witness of his time gives his birth year, his entry to the order or his studies" stays true.

**Absences checked.** Birth year, birthplace, entry and studies: no held line before Vaughan 1845 gives any of them, apart from the bracketed "[born in Surrey]" in CATHAY l.10492. The records note holds. "Ockham's razor": no held line ties razor, "entia non sunt multiplicanda" or "frustra fit per plura" to him; the one "frustra fit per plura" hit is a Jacobean text (gerard-john_condition-of-catholics... l.15339). The README line holds. The doctors and articles of 1330: no list was found, and the Luttrell hits are namesakes. The note holds. "No witness gives his birth year" (card dates) holds.

---

### nicholas-cabasilas

**Verdict: two blocking findings (C-B2, C-B3); otherwise passes with minor fixes.** 404 words; `grade_text` FK 8.19, Flesch 61.6. With every brief fix below applied, it runs 406 words, FK about 8.1, Flesch about 61.4. Flesch is close to the floor, so recheck it after any further edit.

**C-B2 (brief para 5, card uncertain item 1, card role, records: the archbishop question is framed as a dispute it is not, Gass is misread, and a held witness is missed).**
- Current brief text: "Whether he later became archbishop of Thessalonica is disputed. Fabricius says he succeeded his uncle. Gass finds him named archbishop no earlier than 1354. Symeon of Thessalonica, writing in the next century, calls him blessed and gives him no see."
- Gass is on the "yes" side. "Er war Schwestersohn des Nilus und verwaltete dasselbe Amt zehn Jahr nachher (nach 1350)" (GASS l.1373-1375). "Muthmasslich wird also Cabasilas erst nach einigen Jahren das Erzbisthum angetreten haben ... Jedenfalls wird er nicht vor 1354 als Erzbischof genannt" (l.1781-1785). Gass also calls Symeon "Einer seiner Nachfolger" (l.1881). The brief gives only his lower date, so a listener cannot tell which side he is on.
- A held witness is missed. Gass quotes the Synodikon of the church of Thessalonica: "Nicht minder ehrenvoll lautet ein Zeugniss aus dem Synodicon der Kirche von Thessalonich" (l.1884-1888). His note (e) begins "Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης" and ends "αἰωνία ἡ μνήμη, Le Quien, Oriens Christ. tom. II, p. 40" (l.1919-1938). This is the church's own record, and it names him its most holy metropolitan.
- No held witness says he did not take the see. Kantakouzenos's "still a layman" is dated 1353 (CANT3 l.16601-16602). Symeon's "τοῦ μακαρίτου ἐκείνου Καβάσιλα ... Νικολάου κατὰ τὴν κλῆσιν" (PG155 l.9228-9231) names no see, and that is silence. Allatius, quoted in PG155 l.355-357, gives Nilus and Isidore their see and Nicholas none, which is also silence. Migne heads him "THESSALONICENSIS METROPOLITA" (PG150 l.343-345), and so does the PG161 index.
- So "disputed", with Symeon's silence set as one side, makes a dispute out of an absence, and the fullest witness is left out.
- Fix, brief para 5 (40 words, the same as now): "Fabricius says he later succeeded his uncle as archbishop of Thessalonica. Gass presumes so too, and finds him named archbishop no earlier than 1354. A record of the church of Thessalonica, which Gass quotes, calls him its most holy archbishop."
- The doubt is still told in place. Para 1 says he was a layman in 1353, para 2 says the two Cabasilases are often confused, and the card gives Symeon. Symeon's praise stays on the card under "remembered".
- Fix, card uncertain item 1: "When he became archbishop of Thessalonica, and whether he did. Fabricius says he succeeded his uncle Nilus in that office, and Migne heads him as metropolitan of Thessalonica. A record of the church of Thessalonica, quoted by Gass, calls him its most holy metropolitan. Gass presumes he took the see some years after 1353 and finds him named archbishop no earlier than 1354. Kantakouzenos calls him still a layman in 1353. Symeon of Thessalonica praises him and names no see. No held line gives the date or tells how he took office."
- Fix, card role: "Layman of the imperial household, by Kantakouzenos's account; envoy; theologian of the sacraments; archbishop of Thessalonica, by Fabricius and the Thessalonica record".
- Records: on the "yes" side add "GASS l.1373-1375, 1781-1785; the Thessalonica Synodikon via Le Quien, GASS l.1884-1888, 1919-1938". On the other side, keep Kantakouzenos 1353 as a date only and Symeon as silence. Add an absent_details note: "No held line gives the date he took the see or says he never held it; searched all cic/texts for the name forms with Thessalon-, archiep-, metropol-, μητροπολ-, ἀρχιερ-, Erzbisch-." Whether the claim stays Contested is the coordinator's call. Fabricius, Migne and Gass come late; the Synodikon is one church witness, quoted second-hand.

**C-B3 (card uncertain item 5, records contested claim "Whether he wrote against the Latins": Petit's view reversed).**
- Current text: "Louis Petit gives a tract on purgatory to Barlaam of Calabria." Records: "Petit: the purgatory tract is Barlaam's (PO15 l.513-516)".
- Source: at l.513-517 Petit reports the attributions: "Les uns ont attribue l'ouvrage a Nil Cabasilas, les autres a Nicolas Cabasilas, neveu du precedent, les autres enfin a Barlaam, sans qu'il soit d'ailleurs possible de citer un seul manuscrit". He says Barlaam "won out" after Arcudius claimed it for him. He then rejects that reading: "cette malencontreuse attribution a Barlaam d'une oeuvre qui n'a absolument rien a voir avec le moine calabrais" (l.540-544). His own view is that the tract is the Greeks' joint answer at Ferrara, much of it taken word for word from Mark of Ephesus, with the rest Bessarion's: "la majeure partie de cet opuscule est empruntee, mot pour mot, a Marc d'Ephese" (l.584-587), and "tous les passages de la Reponse non identiques ... au premier discours de Marc, appartiennent en propre a Bessarion" (l.630-640).
- Fix, card item 5, last sentence: "Louis Petit, editing the Florence documents on purgatory in 1920, notes that a tract on purgatory has been given to Nilus, to Nicholas and to Barlaam of Calabria. He finds it the Greeks' joint answer at Ferrara, written by Mark of Ephesus and Bessarion."
- Records: replace the side with "Petit: the purgatory tract, once given to Nilus, Nicholas or Barlaam, is the Greeks' joint answer at Ferrara, by Mark of Ephesus and Bessarion (PO15 l.513-517, 540-544, 584-587, 630-640)".

**C-M18 (brief para 1: "prayed for a new patriarch").**
- Current text: "In 1353 the bishops at Constantinople prayed for a new patriarch and put forward three names."
- Source: "ἐπευξάμενοι ἀγαθῶν πολλῶν ἐσμὸν, ἔπειτα τὴν θείαν χάριν ἐπικαλεσάμενοι τοῦ πνεύματος, ἐπελέξαντο τρεῖς" (CANT3 l.16596-16598). They wished the emperor many blessings, called on the grace of the Spirit, and chose three.
- Fix (+2): "In 1353 the bishops at Constantinople called on the Holy Spirit and put forward three names for patriarch."

**C-M19 (brief para 1: who-line thin, and Philotheos without a place).**
- Problem: the only thing said of Cabasilas before para 2 is "still a layman", so the listener does not learn why he matters. "Philotheos" is a common name with no place at first mention. The place is held: "Φιλόθεόν τε τὸν τῆς Ἡρακλείας ἀρχιερέα" (CANT3 l.16598).
- Fix (+5, +2): "...was Nicholas Cabasilas, a writer on the sacraments who was still a layman. Kantakouzenos, the emperor, chose Philotheos, bishop of Heraclea."

**C-M20 (brief para 4: an unclear "this life", "we/us" heard as the narrator's, and a closing list cut off from its point).**
- Current text: "...he wrote that this life grows and begins here, and is made complete in the life to come. Baptism gives us our being in Christ. The anointing with chrism puts in us the working that fits this life ... We did not go up to God, he wrote; he came down to us. No one needs to go to far places, change his clothes or ruin his health for this life. The general leads his army, the farmer farms and the craftsman runs his work."
- Problems: "this life" can be heard as the present life, against "the life to come". "us" and "we" come in the narrator's voice. The last sentence states a bare fact and loses the source's point. The source says that while meditating on these things "στρατηγήσει μὲν ὁ στρατηγὸς ... καὶ οὐ δεήσεταί γε οὐδενὶ τῶν γιγνομένων" — the general will still command and will give up none of his work. The Latin is "licet domi ... manentem" (PG150 l.44358-44389). The Greek of the opening is "Ἡ ἐν Χριστῷ ζωὴ φύεται ἐν τῷδε τῷ βίῳ ... τελειοῦται δὲ ἐπὶ τοῦ μέλλοντος" (l.35858-35860), and "τελειοῖ τὸν γεγεννημένον" (l.36564) supports "the newborn".
- Fix (+2): "The life in Christ begins and grows here, he wrote in his book of that name, and is made complete in the world to come. Baptism gives being in Christ. The anointing with chrism puts in the newborn the working that fits that life, and the Eucharist keeps it whole. People did not go up to God; God came down to them. No one need go to far places, change clothes or ruin his health for it. A general can still lead his army, a farmer farm and a craftsman run his work."

**C-M21 (brief para 2: Migne and Fabricius without a role, and a 26-word sentence).**
- Current text: "A notice that Migne took from the Bibliotheca Graeca of Fabricius calls Cabasilas a thoroughly learned man and a nephew of Nilus Cabasilas, archbishop of Thessalonica."
- Source: "ACCURANTE J.-P. MIGNE" and "APUD J.-P. MIGNE, EDITOREM" (PG150 l.161, 195). The notice heading is "Fabric. Harl. Bibliotheca Graeca, t. X, p. 159" (l.26062).
- Fix (+5): "In 1865 the editor J.-P. Migne printed a notice from the Bibliotheca Graeca of Fabricius. It calls Cabasilas a thoroughly learned man and a nephew of Nilus Cabasilas, archbishop of Thessalonica."
- Offsetting cut in the same paragraph (−2): "Wilhelm Gass, who printed the Greek of his Life in Christ in 1849, follows the chronicler George Phrantzes in making him a sister's son."

**C-M22 (brief para 3: an opener that names the source and says nothing).**
- Current text: "Kantakouzenos names him in his history several times. In 1346 Thessalonica chose..."
- Problem: the first sentence is process narration that opens the paragraph. The paragraph also runs to six sentences.
- Fix (−6): "In 1346, Kantakouzenos writes, Thessalonica chose Nicholas Cabasilas and a man named Pharmakes as envoys..."

**C-M23 (card uncertain item 2: Phrantzes does name the archbishop).**
- Current text: "Phrantzes names Nicholas's mother as the sister of an archbishop of Thessalonica, without naming him."
- Source: "διὰ τὸ ἐκεῖσε εἶναι τὸν ἀδελφὸν αὐτῆς Καβάσιλαν ἀρχιερέα" (PHRAN l.7961-7962, 7987-7988). Phrantzes also calls her "τῇ ἀδελφῇ τῶν τριῶν ἀρχιερέων" (l.7957-7958), the sister of three archbishops.
- Fix: "Phrantzes calls Nicholas's mother the sister of three archbishops, and says her brother Kabasilas was archbishop at Thessalonica, without a first name."

**C-M24 (card otherNames: a form not held).**
- Current text: "Νικόλαος ὁ Καβάσιλας".
- Source: no file has this form. Held forms are "Καβάσιλας Νικόλαος" (CANT3 l.6395), "Νικόλαον τὸν Καβάσιλαν" (l.16599; accusative) and "Nicolaus Cabasilas" (l.6420).
- Fix: replace it with "Καβάσιλας Νικόλαος".

**C-M25 (card sources: Kantakouzenos volume 2 has no file).**
- Current text: the entry "Historiarum libri IV, volumes 2 and 3" gives only `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt`. The 1343, 1346 and 1347 lines are in volume 2.
- Fix: split it into two entries. Add volume 2 (Ludwig Schopen, ed., 1831, `cic/texts/cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt`).

**C-M26 (card: names and terms at first mention with no context).**
- dates, "John Kantakouzenos": fix "John Kantakouzenos, the emperor, in his history, names him...".
- dates, "The notice from Fabricius in Migne": fix "The notice from Fabricius that J.-P. Migne printed in 1865...".
- legacy: "Sforza Pallavicino" should be "Sforza Pallavicino, in his history of the council". "Mark of Ephesus" should be "Mark of Ephesus, the Greek spokesman at Florence", as PO15 l.584-640 has him. "Papebroch's commentary" should be "the commentary of the Bollandist Daniel Papebroch" (PG150 l.49318: "DANIELIS PAPEBROCHII COMMENTARIUS"). "Casaubon" is held only by surname, so write "the scholar Casaubon".
- knownFor: "the civil war" needs context: "an envoy in the civil war of the 1340s". The 1343 to 1347 embassies are in CANT2.
- keyWorks and knownFor: "chrismation" is undefined. Fix "chrismation, the anointing with chrism".
- uncertain item 4: "His editor Boivin" should be "Boivin, who edited Gregoras's history". The note is in GREG2's Annotationes (l.47127-47130).

**C-M27 (records and README: Gregoras's old friend has no contested record, though the README says it is tagged Contested).**
- Records tag the claim "Dominant Modern Reconstruction" with no `contested_claims` entry. The README says "whether the 'Kabasilas of the sakellion' and Gregoras's old friend are he ... are all tagged Contested".
- Source: Gregoras names only "ὁ καλὸς ... Καβάσιλας, τῶν φίλων ὁ βέλτιστος", one of the friends who turned against him at the 1351 synod, "πρός τε τὸ βαθὺ γῆρας ἀποβλέπων" (GREG2 l.28603-28606). Boivin's note says "Nicolaus scilicet" (l.47127), and Gass follows him (GASS l.1786-1787). There is one reconstruction, with a second editor following it, and no held contrary voice.
- Fix: keep the DMR tag, owned by Boivin and followed by Gass. Correct the README to "...and whether the 'Kabasilas of the sakellion' is he ... are tagged Contested; Gregoras's old friend is Boivin's identification, followed by Gass."

**C-M28 (records: Symeon's "next century" rests on the Library header; one-witness Palamite tie).**
- Symeon: the records claim cites PG155 l.1-3, the header ("Saeculum XV, annus 1430"). A held line in the volume says it: "Sim. Thessal. claruisse a. 1410 et obiisse a. 1429" (PG155 l.796-806, Harles after Wharton). Fix: change the witness to PG155 l.796-806.
- Palamas: "Gass finds him named among the followers of Gregory Palamas" is tagged Widely Accepted on Gass alone (GASS l.1231-1235). Two held witnesses back it. Symeon counts Cabasilas's writings among those against "τοῦ Βαρλαάμ τε καὶ Ἀκινδύνου αἱρέσεως" (PG155 l.9225-9236), and the Thessalonica Synodikon in Gass praises him against "τοῦ Βαρλαὰμ καὶ Ἀκινδύνου ... μανίαν" (GASS l.1932-1934). Fix: add both as witnesses. If only Gass is kept, tag it Inferential-Thin.

**Absences checked.** Birth, death, burial: none found, in a windowed search with obiit, mortuus, died, ἐτελεύτ- and the other forms above. The hits are Constantine Cabasilas, a deacon Kabasilas of the Thessalonica metropolis (ACTA), Michael Cabasilas (ACTA index) and Symeon's own death. The absent_details note holds. Monastic profession: no line says he took the habit. Gass notes a monastic surname "Χαμαετός" (GASS l.1392-1393) and a leaning toward monastic life (l.1450-1455), which is not profession. The note holds. Not counted: COVEL (l.15389-15652) and MANSI46 (the Melkite synods on "Cabasilae sententiam" on the form of consecration) are held later witnesses on the epiclesis question that the card does not use.

---

### records.json (these profiles)

- **william-of-ockham.**
  - The 1323 summons claim needs the letter's condition (C-B1).
  - The Dialogus claim needs its witness moved to l.22682-22696, with Ambrose named (C-M8).
  - The Dalgairns date in the birth claim should be 1870 (C-M11).
  - Optional: the Perugia 1322 lines (CARL l.4698-4700, 5326-5329; BUL5 l.42504-42507; CATHAY l.10492-10494) could go under the 1323-identity contested claim.
  - The "Twenty years" claim is tagged DMR, and its owner is Lea. That is right.
  - The flight's date is tagged Widely Accepted, with a contested record for 25 against 26 May. That is consistent.
  - Every brief and card fact has a records witness, apart from the Gerson tract topic (C-M9), whose witness is GERSON l.27012-27016.
- **nicholas-cabasilas.**
  - The archbishop contested record needs the Synodikon and the Gass lines, with silence kept as silence (C-B2).
  - The "Whether he wrote against the Latins" side needs Petit's view restated (C-B3).
  - Gregoras's old friend stays DMR, and the README is corrected (C-M27).
  - Symeon's date witness is a Library header (C-M28).
  - The Palamite tie rests on one witness unless Symeon and the Synodikon are added (C-M28).
  - The 1353 claim calls Kantakouzenos "partisan witness", but the brief does not say so. On this point he names his own friend: "ἐν τοῖς πρώτοις μάλιστα τῶν φίλων" (CANT3 l.6398-6399). If the tag stays, the brief or card should say once that the account is the emperor's own, as para 1 already half does with "Kantakouzenos, the emperor". Not counted.

**Census notes, for an Open-Gaps entry (no census edit proposed).**
- Movement 131, documentedStories[0], tells as settled that the galley was "provided by the emperor Louis of Bavaria". Its caveat reads "The date of the flight and the galley are securely documented." Lea writes "A galley, furnished, according to John, by the Emperor Louis, but according to other and more trustworthy accounts, by Genoese refugees" (LEA3 l.7103-7106). Carlini says "Chi inviasse la galea non è sicuro" and gives John of Winterthur's French king and Andrea Dei's Genoese exiles (CARL l.6285-6292). Carlini also records Riezler and Müller's 25 May (l.6281-6282).
- The same story says Ockham "had been at Avignon for four years answering charges about his own philosophy" and "spent the rest of his life at the imperial court in Munich". No held line gives four years or the subject of the charges; CARL l.5336-5337 says only "altre dottrine". Wadding's reading of the 1349 letter (GLASS l.13552-13558) contests the second phrase.
- Movement 116 tells Cabasilas as "the layman Nicholas Cabasilas" ("why"), and its voices line says "a layman of Thessalonica". Fabricius, Migne's heading and the Thessalonica Synodikon in Gass make him archbishop of Thessalonica (C-B2).
- Card traditions: "The Franciscan Order — Spirituals Crisis to the Great Division" and "Hesychasm & the Palamite Synthesis" are exact census names. Ockham is a voice of movement 131 (voices[3]), and Cabasilas of movement 116 (voices[2], people[4]). Both keep their list lines.

**README lines about these two.** True, apart from the Gregoras "tagged Contested" phrase (C-M27) and the incomplete list of English quotations (C-M17). Checked and true: the Ockham opening line; the death witnesses; "No held line has 'Ockham's razor'"; the Mansi 25 rector of Langton, a namesake, in 1311 (MANSI25 l.42491-42492, 42563); the "also Fraticelli" note (movement 124 voices are Clareno, Olivi and John XXII); the Cabasilas corrections (1343 sakellion embassy; 1346 Berroia; the Greek of the Life in Christ in PG150); and the grade ranges, which hold for these two (8.08/62.2 and 8.19/61.6).

### Checklist summary

| # | Item | william-of-ockham | nicholas-cabasilas |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Fail (C-B1, C-M1, C-M8, C-M10, C-M11) | Fail (C-B2, C-B3, C-M18, C-M23) |
| 2 | Quotes verbatim | Fail, minor (C-M2: the stop) | Pass (no quotes) |
| 3 | No invented detail | Pass | Pass |
| 4 | Reading aids, no AI tells | Fail, minor (C-M2, C-M4, C-M6) | Fail, minor (C-M20, C-M21, C-M22, C-M26) |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass (John XXII and Clement VI told as theirs) | Pass (see the records note on Kantakouzenos) |
| 7 | Contested claims both sides, not settled | Pass | Fail (C-B2, C-B3) |
| 8 | Common names and scholars at first mention | Fail, minor (C-M7, C-M14) | Fail, minor (C-M19, C-M21, C-M26) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene, disputes in place, length | Pass | Fail, minor (C-M19: who-line thin) |
| 11 | Readability | Pass (8.08 / 62.2) | Pass (8.19 / 61.6; near the floor) |
| 12 | Card order, missing fields absent, caveat repeated | Fail, minor (C-M12, C-M13) | Fail, minor (C-M24, C-M25) |
| 13 | Audio tags only in the script, at start and close | Pass | Pass |
| 14 | Keeps the list line; Who test | Pass | Pass |

### Count

- william-of-ockham: 1 blocking (C-B1), 17 minor (C-M1 to C-M17).
- nicholas-cabasilas: 2 blocking (C-B2, C-B3), 11 minor (C-M18 to C-M28).

---

## Era 6 Who batch 2, round 1 review: PART D

**Scope.** `gregory-palamas` and `gregory-of-sinai`: brief, card, audio, and each one's `records.json` entry; the README lines about them; the census entries for their tradition. Branch `claude/cft-who-era6-batch2`. No repo file edited; no web, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, lessons.md, the batch README, the scan's rulings (l.15-56), its rows for both men (l.113, l.114) and the File key, and the house form in batch 1 (`julian-of-norwich.*`; `R1_review.md` Part A). For every sentence of both briefs and every card field I opened the cited lines with 20 or more lines around them, and I read the Greek, Latin, Church Slavonic, Croatian and German myself. I searched all 1,771 files in `cic/texts/` for name variants (Palam-/Палам-; Σιναΐτ-/Σιναίτ-/Sinait-/Синаит-; Calec-/Kalek-; Γρηγορ- near Σινα-) before accepting any absence, and for death years near Palamas's name in PG150, PG151, PALH, CANT3, GREG3, Mansi 26 and the Acta Sanctorum. I scored the briefs and my proposed rewrites with `engine.m1.gates.grade_text`, counted words and sentence lengths by script, and diffed each audio file against its brief after removing the two tags. I read the census from `git show origin/main:cic-website/data/world-census.json`.

A note on spelling. The review brief's item 5 lists "American spelling outside quotations" as a fault, while lessons.md lists "British spelling outside quotations". Both cards use American spelling ("favor", "Defenses", "practice"), which is the lessons.md rule. I did not count it.

**Files opened (cic/texts/).**
- CANT1 = `cantacuzenus_historiarum-libri-iv-v1-grc-lat_schopen1828.txt` (l.32560-32760)
- CANT2 = `cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt` (l.34225-34345)
- CANT3 = `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt` (l.6195-6330, 11040-11145; Palamas hits to l.36503)
- GREG2 = `gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt` (l.11900-11912, 18630-18648)
- GREG3 = `gregoras_byzantina-historia-v3-grc-lat_bekker1855.txt` (l.13045-13200)
- PALH = `palamas_homiliae-41-grc_jerusalem1857.txt` (l.1-200, 440-640, 1270-1480, 2100-2150, 2430-2470, 2540-2652, 2870-2900, 4250-4332, 5080-5135, 5935-5965, 7275-7436, 8230-8300, 29450-29463)
- PG150 = `palamas_opera-omnia-pg150-grc-lat_migne1865.txt` (l.195-205, 495-560, 49990-50070, 60940-60980, 66790-66808, 69098-69225, 71600-71665, 71940-71975, 72480-72498, 72555-72610; headings 69298-72561)
- PG151 = `palamas_opera-omnia-pg151-grc-lat_migne1865.txt` (l.1-12, 14760-14770, 26505-26518)
- ACTA = `acta-et-diplomata-graeca_acta-patriarchatus-constantinopolitani-1315-1402-v1-grc-lat_miklosich-mueller1860.txt` (l.9655-9720, 10295-10310, 11270-11470, 11500-11610, 18898-18998)
- MANSI26 = `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt` (l.10180-10235, 19570-19598)
- PHIL1 = `philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` (l.1-200)
- PHIL2 = `philokalia_ton-ieron-neptikon-v2-grc_tzelatis1893.txt` (l.33585-33670, 41600-41690, 42140-42180, 72420-72462, 72668-72684)
- PAISZ = `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` (l.1-12, 3995-4015, 4505-4535, 4640-4660, 8225-8250, 8440-8455, 9255-9290, 10515-10545, 10985-11035, 14195-14240)
- PAISK = `paisius-velichkovsky_vostorgnutye-klasy-chu_optina1849.txt` (l.1-10, 9825-9845)
- MEYER = `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` (l.1-40, 3985-4015)
- RACKI = `racki_bogomili-i-patareni-rad-viii-hrv_jazu1869.txt` (l.3530-3548, 3650-3700)
- NIL = `nil-sorsky_predanie-i-ustav-chu_borovkova-maikova1912.txt` (l.2418-2436)
- PG160 = `gennadius-scholarius_opera-omnia-pg160-grc-lat_migne1866.txt` (l.57940-57948)
- ASAUG1 = `acta-sanctorum_augusti-tomus-1-lat_1750.txt` (l.151935-151972)
- COVEL = `covel_some-account-of-the-present-greek-church_1722.txt` (l.29748-29758)
- PAISII-H = `paisii-hilendarski_istoriia-slavianobolgarskaia-bul_ivanov1914.txt` (l.1-12, 7115-7160)

**Quotations.** Neither brief nor either card holds a line in double quotation marks. Every line held only in Greek, Latin, Slavonic, Croatian or German is told in modern words with no marks, as the README's rule requires. I checked each modern-words telling against its original:
- Palamas: Kantakouzenos on the release (CANT2 l.34246-34251, 34328-34333): one misreading (D-B1) and one dropped phrase (D-M4). Barlaam's charges (CANT1 l.32690-32694): faithful. Palamas on the navel-soul charge (PHIL2 l.42166-42170): faithful. The 1341 tome (ACTA l.9703-9708): faithful. Chapter 75 (PG150 l.66797-66804): faithful. Philotheos on four years under guard (PALH l.5949-5950), the capture (l.7320-7323) and the year (l.7408): faithful. Gregoras on many gods (GREG3 l.13057): faithful. Gregoras on God's justice (GREG3 l.13186-13189): hedge dropped (D-M1). The editor and Philotheos on sainthood (PALH l.510-514, 523-555): narrowed (D-M3). The closing line on the body (PHIL2 l.41676-41679): faithful.
- Gregory of Sinai: the notice (PG150 l.69111-69144; PHIL2 l.33605-33640): faithful. The prayer whole and half (PG150 l.72588-72601): one misassignment and one unclear verb (D-M15). How to sit (PG150 l.72564-72583): one condition dropped (D-M16). Baptism's gift (PG150 l.72489-72493): one condition dropped (D-M17). Paisius on the copies (PAISZ l.10530-10541): faithful. Basil (PAISZ l.4651-4653): faithful in wording, wrong work (D-B2). Meyer (MEYER l.4000-4006): faithful, with "first" added (D-M12). Rački (RACKI l.3664-3690): faithful. "There" is unclear (D-M14).

**Audio.** Both `audio/<id>.audio.txt` files are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and no other tag. Pass for both.

**Census.** Both cards read "Hesychasm & the Palamite Synthesis", the census `name` of `hesychasm-and-the-palamite-synthesis`. Pass. Census text that tells as settled what held sources contest is listed under records.json, for an Open-Gaps note.

---

### gregory-palamas

**Verdict: one blocking finding (D-B1). Otherwise passes with minor fixes.**

`grade_text`: FK 7.61, Flesch 64.29. 404 words. Audio pass. With every fix below applied, my scratch copy is 409 words, FK 7.71, Flesch 63.83; the offsetting cut in D-B1 brings it to 406.

**D-B1 (brief para 1: Anna's wish for peace is the reverse of what Kantakouzenos says).**
- Current text: "The empress Anna wanted peace. She had him brought out and sent him as an envoy to her rival, the emperor John Kantakouzenos."
- Source: Kantakouzenos says the empress was running from any settlement and would rather die than make one: "eam a pacificatione refugientem mori ipsosque secum perdere malle viderunt" (CANT2 l.34226-34227). The palace guards then planned to hand the palace over. Her son John, "tum quindecim natus annos", ran to her and begged her to send to Kantakouzenos at once (l.34233-34240). Only then was she persuaded: "lico persuasa mater Andronicum Asanem … et Gregorium Palamam illic carcere detentos ad se adduci iussit: quibuscum de pace locuta, eos ad imperatorem legat" (l.34275-34277; Greek "αὐτίκα τε ἐπείθετο ἡ μήτηρ", l.34246). "Wanted peace" is a motive the source denies her.
- Fix: "Her young son urged the empress Anna to make peace. She had Palamas brought out and sent him as an envoy to her rival, the emperor John Kantakouzenos." ("him" becomes "Palamas", because the new sentence puts the son in front of it.)
- Offset (+5 words): "Kantakouzenos, who tells this in his history, took Palamas's side." becomes "Kantakouzenos, his ally, tells this." (−5). His side-taking stays marked. The next paragraphs still say "Kantakouzenos says", and the card names his history.
- Records: the claim on the release should add CANT2 l.34225-34240 and the son's part.

**D-M1 (brief para 5, card `uncertain` "How he was captured": Gregoras's hedge is dropped).**
- Current text: brief "Gregoras calls the capture God's justice."; card "…and tells it as God's justice."
- Source: Gregoras offers two causes and does not choose: "nescio, utrum tale quid ad Christianos captos illudendos facere soleant, an tribuendum sit divinae supremaeque iustitiae, qui virum illum … barbarorum manibus tradidit" (GREG3 l.13187-13189; Greek "εἶτ᾽ εἰωθὸς σφίσι ποιεῖν … εἶτ᾽ ἐνδεδωκυίας τῆς θείας ἄνωθεν δίκης", l.13160-13163).
- Fix, brief: "Gregoras wonders if it was God's justice." Card: "…and asks whether it was God's justice." Records: the claim on the capture should say Gregoras offers it as one of two causes.

**D-M2 (brief para 2 and card `dates`: "Philotheos" at first mention has no place).**
- Current text: brief "Philotheos, a patriarch who wrote a speech in his praise, says…"; card `dates` "Philotheos, his panegyrist, says…".
- Evidence: the name is shared within this batch's own sources. Philotheos of Sinai has a preface in PAISZ (TOC l.14206-14207), and the brief on Gregory of Sinai names the Athos monastery of Philotheou. The pattern's rule on common names applies (checklist item 8). The encomium's title gives the see: "ΝΕΑΣ ΡΩΜΗΣ ΚΑΙ ΟΙΚΟΥΜΕΝΙΚΟΥ ΠΑΤΡΙΑΡΧΟΥ ΦΙΛΟΘΕΟΥ" (PALH l.1286, OCR), and the title page has "ΠΑΤΡΙΑΡΧΩΝ ΚΩΝΣΤΑΝΤΙΝΟΥΠΟΛΕΩΣ" (l.102, OCR).
- Fix, brief: "Philotheos, a patriarch of Constantinople who wrote a speech in his praise, says…" (+2). Card: "Philotheos, patriarch of Constantinople and his panegyrist, says…".

**D-M3 (brief para 6: the reason for sainthood is narrowed).**
- Current text: "He quotes Philotheos, who counted him a saint for the healings at his tomb."
- Source: Philotheos holds him a saint for his life, for his struggles against the passions and the demons, and for his defense of the Church. Then he adds "μάλιστα δὲ ἀκριβῶς πεπληροφόρημαι τοῦτο … ὡς ΑΓΙΟΝ ἀπὸ τῶν θαυμάτων αὐτοῦ … ἰαμάτων πηγὴν τὸν ἴδιον ἀναδείξας τάφον" (PALH l.523-555).
- Fix: "Philotheos, he notes, counted him a saint above all for the healings at his tomb." (+1)

**D-M4 (brief para 1: "for him" is dropped, and "mean" is the wrong word).**
- Current text: "Through all he had suffered, he writes, Palamas never said or did anything mean."
- Source: "ὅτι πολλὴν ὑπὲρ αὐτοῦ δικαίου καὶ τῆς ἀληθείας κάκωσιν ὑπενεγκών, οὐδὲν ἀγεννὲς οὔτε ἔπραξεν οὔτε ἐφθέγξατο ἄχρι τέλους" (CANT2 l.34328-34333, OCR; Latin "pro iustitia veritateque gravissime afflictus, usque ad extremum nihil abiectum aut fecerit, aut dixerit"). He suffered for Kantakouzenos's cause, and that is what makes the praise partisan. A listener can hear "mean" as stingy. The Greek and Latin mean base or abject.
- Fix: "Through all he had suffered for him, he writes, Palamas never said or did anything base." (+2)

**D-M5 (card `dates`: a partial list of synods reads as the full list).**
- Current text: "The synods that judged the dispute met in 1341, 1347 and 1351."
- Source: Migne's notice lists four synods, including "secunda ann. 1345, adversus Palamam" (PG150 l.50063-50065, OCR "1245"). Kalekas's letter of November 1344 reports synodal action against Palamas (ACTA l.11286-11300, 11425-11440).
- Fix: "The synods that upheld him met in 1341, 1347 and 1351."

**D-M6 (card `uncertain` "Whether the 1341 synod judged the teaching": Combefis is not marked hostile, and has no role).**
- Current text: "François Combefis, in a note printed by Mansi, writes after Gregoras that no doctrine was debated at that synod."
- Source: the note is headed "Francisci Combefisii Ord. Praed. Notae" (MANSI26 l.19583, OCR). It calls the tome "heretico plane spiritu conscripta, & mendaciis conferta" (l.19592-19593). Mansi's own heading calls the 1347 synod "Pseudo-synodus" (l.10180). The pattern requires a hostile witness to be marked.
- Fix: "François Combefis, a Dominican hostile to the tome, writes in a note printed by Mansi, after Gregoras, that no doctrine was debated at that synod."

**D-M7 (card `uncertain` "How he was captured": who threw the books).**
- Current text: "Gregoras, his enemy, says the pirates found gold and silver on him, threw his books into the sea and flogged him…"
- Source: barbarians in pirate boats took the ship (GREG3 l.13070-13071; Latin l.13092). The money was found on him (l.13102-13104). Then "the barbarian", the elder son of the satrap "Hyrcanus", asked whose each book was and ordered Palamas's own books thrown into the sea, and ordered him flogged (l.13072 and 13093 for the satrap's son; l.13115 and 13140 for the books; l.13127 and 13148 for the flogging).
- Fix: "Gregoras, his enemy, says his captors found gold and silver on him, and that a satrap's son had his books thrown into the sea and had him flogged. Gregoras asks whether it was God's justice." (This takes in D-M1.)

**D-M8 (card `uncertain`: a held disagreement on his age when he left for Athos is missing).**
- Evidence: Philotheos says he left when already past boyhood, "τὸν ἔφηβον ὑπερβεβηκὼς ἤδη" (PALH l.2125). Kantakouzenos says he and his two brothers left "ἐπὶ πάνυ παιδικῇ τῇ ἡλικίᾳ", "aetate admodum puerili" (CANT1 l.32726, 32751-32752). The brief's "As a young man" follows Philotheos and may stand.
- Fix: add an item: "How old he was when he left for Athos. Philotheos says he was past his boyhood. Kantakouzenos says he and his two brothers were still boys." Records: add the two lines to the claim on the brothers.

**D-M9 (card `sources` and records: works the card relies on are missing, and some files are wrong).**
- The brief rests on CANT2 (para 1) and CANT3 (para 5), and on GREG3 (paras 4 and 5). The card's "about" list gives only the CANT1 file for Kantakouzenos, and only the GREG2 file under "Byzantina historia, volumes 2 and 3".
- The card's legacy and remembered lines also rest on files not listed: PG160 (Gennadios, l.57945); ASAUG1 (l.151940-151968); COVEL (l.29751-29756); PHIL1 l.147-153 (Nikodemos with "the holy Macarius of Corinth" published the Philokalia); and PAISK, whose title and contents (l.1, 9835) carry "Paisius Velichkovsky put him on prayer into Slavonic".
- Records has no claim for the Philokalia's compilers or for Paisius's Slavonic.
- Fix: give each Kantakouzenos and Gregoras volume its own entry with its own file, add the five files above to "about", and add two records claims: compilers (PHIL1 l.147-153, Documented) and Paisius's Slavonic (PAISK l.1, 9835, Documented).

**D-M10 (records: a file header used as a side of a contested claim; a reported line cited as Gregoras's own).**
- contested_claim "Year of death", side 2: "Library file headers: 1359 (not a witness)". A header is not a witness, so it cannot be a side. Fix: drop the claim. Move the note to absent_details "Birth year and death year in a source text", which already says it. The card item "When he was born and when he died" stays, since it rests on Philotheos and the editor.
- Claim "Akindynos and Gregoras against him" cites GREG2 l.18641 "Palamae, Deos multos statuentis". That line is what interpreters of an omen said ("apparet, inquiebant", l.18639-18641), as Gregoras reports it. Gregoras's own words are GREG3 l.13057 ("τῇ πρὶν ἐκείνῃ πολυθεΐᾳ τἀνδρός"). Fix: say so in the claim, and lead with GREG3.

---

### gregory-of-sinai

**Verdict: three blocking findings (D-B2, D-B3, D-B4). Fix and recheck.**

`grade_text`: FK 8.78, Flesch 63.25. 406 words. Audio pass. With every fix below applied, my scratch copy is 403 words, FK 8.64, Flesch 62.87. It is given in full after D-M17.

**D-B2 (brief para 3, records: Basil's line is from the wrong preface, and Basil has no context).**
- Current text: "Basil of Poiana Marului, in a preface to Gregory's book, says the most learned fathers of Athos at first opposed him."
- Source: the line "И самому сему Григорію Синаиту сопротивишася испрва саміи словеснѣйшіи отцы Аѳонскія горы, егда началъ бѣ о семъ ихъ учити" is at PAISZ l.4651-4653, on printed page 87. Basil's preface to Gregory's book begins at l.3999 (page 72-73). His next preface, "ПРЕДИСЛОВІЕ НА ГЛАВИЗНЫ БЛАЖЕННАГО [Филоѳея Синайскаго]", begins at l.4523. The contents list puts it at page 85, and the Hesychius preface at page 97 (l.14206-14208). So the line is in Basil's preface to the chapters of Philotheos of Sinai.
- A listener also meets Basil with no context. The contents list calls him "Старца Схимонаха Василія, спостника и друга блаженнаго Отца Паѵсія" (l.14198-14199) and "Старца Поляномерульской обители Василія" (l.14215).
- Fix: "Basil, elder of the Poiana Marului monastery and a friend of Paisius, writes that the most learned fathers of Athos at first opposed him." (+4). Card `uncertain` "Whether the Athos fathers opposed him": "Basil of Poiana Marului, in his preface to the chapters of Philotheos of Sinai, says…". Records: replace the witness "TOC 14201-14204" with "PAISZ l.4523-4526, 4651-4653; TOC l.14206-14207".

**D-B3 (brief para 1, card, records: a held side is missing; Paisius, citing the Life, says Gregory found no one at all).**
- Current text: "At the skete of Magoula, opposite the monastery of Philotheou, he met only three who gave a little time to contemplation: Isaiah, Cornelius and Macarius." The card says only "The notice says only that the monks did not know the terms."
- Source: Paisius says "якоже является отъ житія Святаго Григорія Синаита, иже всю Святую гору обшедъ, и прилѣжно дѣлателей сея молитвы поискавъ, отнюдь никогоже обрѣте въ ней, ниже малое вѣдѣніе о молитвѣ сей имущаго" (PAISZ l.11025-11029, OCR "ионе"). He then draws from it that no one in so holy a place knew the prayer (l.11029-11031). This retells the Life the notice names. It disagrees with the notice's three monks at Magoula (PG150 l.69125-69131), so the count is contested and has to be told in place.
- Fix, brief para 2, after the Kallistos sentence: "Paisius Velichkovsky, archimandrite of Neamț in Moldavia, says a Greek copy that reached his community lacked the account of Gregory's death. Citing the Life, he also says Gregory found no one on Athos who knew the prayer." (This takes in D-M11. See D-M12 for the offset.)
- Card `uncertain`: add "Whether anyone on Athos knew the prayer. The notice names three monks at Magoula who gave a little time to contemplation. Paisius Velichkovsky, citing Kallistos's Life, says Gregory found no one with even a little knowledge of it. Meyer makes the three Gregory's pupils."
- Records: add a claim (PAISZ l.11025-11031, Inferential-Thin) and a contested_claim, "Whether he found anyone on Athos who knew the prayer": side 1 the notice (PG150 l.69125-69131; PHIL2 l.33615-33620); side 2 Paisius (PAISZ l.11025-11031); Meyer's pupils (MEYER l.4006-4007) as a note.

**D-B4 (card `uncertain`, item 1: a false "one", and an unsupported claim that the notice draws on the Life).**
- Current text: "His life rests on one short notice. The Philokalia's editors wrote it, drawing on the Life by his disciple Kallistos."
- Source: the notice says only that Kallistos "κατὰ πλάτος συνέγραψεν" his Life (PG150 l.69142-69144). It does not say the notice draws on it. And the life does not rest on the notice alone. The card's own items use Meyer for Crete and the thirteenth century (MEYER l.4000-4009), Rački for Paroria and the Theodosius story (RACKI l.3664-3690), and Basil for opposition. Paisius adds the copy history and the "no one" line (PAISZ l.10530-10541, 11025-11031).
- The brief's own caveat is "The story comes from a short notice by the editors of the Philokalia". The item should open with that.
- Fix: "Most of the story comes from a short notice by the editors of the Philokalia, which Migne reprinted in 1865. The notice names a longer Life by his disciple, the patriarch Kallistos. Meyer and Paisius Velichkovsky cite that Life, and Paisius says the Greek copy which reached his community was incomplete and lacked the account of Gregory's death."

**D-M11 (brief para 2, card: Paisius Velichkovsky has no context at first mention).**
- Current text: "Paisius Velichkovsky, whose community copied it, says…". A listener does not know who he is.
- Source: "Писанія Старца Паѵсія, Архимандрита Молдовлахійскія Нямецкія обители" (PAISZ l.14222-14223).
- Fix: as in D-B3: "Paisius Velichkovsky, archimandrite of Neamț in Moldavia, says…". The card's first mention (`uncertain` item 1) gets the same words.

**D-M12 (brief para 2: Meyer's role is inferred, "first" is added, and the sentence is 26 words).**
- Current text: "Citing the Life in 1894, the German scholar Philipp Meyer says Gregory first learned the prayer of the mind on Crete, from a hermit named Arsenios."
- Source: Meyer gives the story "einer glaubhaften Ueberlieferung nach … Er lernte die Sache aber auf Creta von einem Eremiten Arsenios kennen" (MEYER l.4002-4004). "First" is not in it. His role is in his title: the main documents of the Athos monasteries, "herausgegeben … von Ph. Meyer" (l.1). "German scholar" rests on the language and imprint only.
- Fix: cut the sentence from the brief (−26). It pays for D-B3, D-B2 and D-M11. The card keeps Crete, the thirteenth century and Iviron with Meyer's name. If the drafter keeps it instead: "Philipp Meyer, who edited the main Athos documents in 1894, says from the Life that Gregory learned the prayer of the mind on Crete, from a hermit named Arsenios." Then another cut is needed elsewhere.

**D-M13 (brief para 5, card `place` and `knownFor`: Paroria is told as a place before the dispute, and "Migne's Latin" is undefined).**
- Current text: "He built three large lauras, communities of monks, at Paroria, near the borders of Macedonia. Migne's Latin takes Paroria to mean the borders, but the 1893 Philokalia prints it as a place name."
- Source: "κατὰ τὰ παρόρια τῆς Μακεδονίας τρεῖς λαύρας μεγίστας οἰκοδομήσας" (PG150 l.69134-69136). Lecomte's Latin reads "in finibus Macedoniae" (l.69175). PHIL2 prints "Παρόρια" with a capital (l.33628). Rački has "na planini Paraoriji … kod jedrene" (RACKI l.3667). The first sentence takes both readings at once, then reports the dispute in editors' terms a listener cannot place.
- Fix, brief: "The notice says he built three large lauras, communities of monks, in what it calls the paroria, the borderlands, of Macedonia." And later: "Theodosius comes to him on the mountain Paroria, near Adrianople. Gregory sends him to Tsar Alexander of Bulgaria to seek protection from the Turks." The Latin and Greek readings stay on the card.
- Card `place`: "The paroria, the borderlands, of Macedonia, where the notice says he built three lauras; Rački names a mountain Paroria near Adrianople." Card `knownFor`: "…built monastic houses in the paroria, the borderlands, of Macedonia."

**D-M14 (brief para 5: "There" can be heard as Paroria).**
- Current text: "There, monks of Greek and Slavic birth gather round Gregory."
- Source: in Rački the disciples gather while Gregory is on Athos, at "Magali, i u drugih mjestih" (RACKI l.3668-3685). They do not gather at Paroria.
- Fix: "In it, monks of Greek and Slavic birth gather round Gregory."

**D-M15 (brief para 4, card `keyWorks` 2: the prayer's two forms are misassigned, and "set down both" is unclear).**
- Current text: brief "The Fathers said the prayer whole, Gregory wrote: … Others said half…" and "…he added; he set down both." Card: "…and that he sets down both the mouth and the mind."
- Source: "Οὕτως εἶπον οἱ Πατέρες· ὁ μέν· … τὸ ὅλον· ὁ δέ, τὸ ἥμισυ" (PG150 l.72589-72591): among the Fathers, one says it whole and another half. "Οἱ μὲν διὰ στόματος, οἱ δὲ διὰ νοῦ διδάσκουσι λέγειν αὐτήν. Ἐγὼ δὲ ἀμφότερα τίθημι" (l.72599-72601). He holds to both. A listener can hear "set down" as dropped.
- Fix, brief: "Some Fathers said the prayer whole, Gregory wrote: … Others said half…" and "Some say it with the mouth and some with the mind, he added, and he taught both." Card: "…and that some teach it with the mouth and some with the mind, and he teaches both."

**D-M16 (brief para 4: a condition is dropped, and the sentence is 22 words of commands).**
- Current text: "Sit on a stool, he told the monk, bend low, gather your mind into your heart and call on the Lord Jesus."
- Source: "κύπτων κάτωθεν, καὶ τὸν νοῦν ἐν τῇ καρδίᾳ συνάγων, εἴπερ διήνοικται, ἐπικαλοῦ τὸν Κύριον Ἰησοῦν εἰς βοήθειαν" (PG150 l.72578-72579). "If it has been opened" is the teacher's condition.
- Fix: "Sit on a stool, he told the monk, and bend low. Gather your mind into your heart, if it has opened, and call on the Lord Jesus."

**D-M17 (brief, closing line: the cause of the burying is dropped).**
- Current text: "It lies buried under the passions and waits for our repentance."
- Source: "ἢ [ἣ] διὰ τῆς τῶν ἐντολῶν ἀμελείας τοῖς πάθεσι συγχωσθεῖσα, καὶ τὴν μετάνοιαν ἡμῶν ἀναμένουσα" (PG150 l.72491-72493). It is buried through neglect of the commandments. As written, the brief makes the burying universal.
- Fix: "Through neglect of the commandments it lies buried under the passions, and waits for our repentance."

The brief with D-B2, D-B3, D-M11 to D-M17 applied (403 words, FK 8.64, Flesch 62.87):

> Gregory of Sinai came to Mount Athos and went round its monasteries and hermitages. He found many wise and serious monks who did not know guarding of the mind, stillness or contemplation even by name. At the skete of Magoula, opposite the monastery of Philotheou, he met only three who gave a little time to contemplation: Isaiah, Cornelius and Macarius.
>
> The story comes from a short notice by the editors of the Philokalia, a Greek collection on prayer first printed in 1782. They say he became a monk on Mount Sinai, and so was called the Sinaite. They place him about 1330, under an emperor Andronikos. His disciple Kallistos, later patriarch of Constantinople, wrote his Life at length. Paisius Velichkovsky, archimandrite of Neamț in Moldavia, says a Greek copy that reached his community lacked the account of Gregory's death. Citing the Life, he also says Gregory found no one on Athos who knew the prayer.
>
> On Athos, the notice says, he taught hermits and the monks in communities alike about watchfulness, guarding the mind and prayer of the mind. Basil, elder of the Poiana Marului monastery and a friend of Paisius, writes that the most learned fathers of Athos at first opposed him.
>
> Some Fathers said the prayer whole, Gregory wrote: Lord Jesus Christ, Son of God, have mercy on me. Others said half, Jesus, Son of God, have mercy on me, which is easier for a weak mind. Some say it with the mouth and some with the mind, he added, and he taught both. Sit on a stool, he told the monk, and bend low. Gather your mind into your heart, if it has opened, and call on the Lord Jesus. When your shoulders hurt and your head aches, hold on, seeking the Lord in your heart.
>
> The notice says he built three large lauras, communities of monks, in what it calls the paroria, the borderlands, of Macedonia. Franjo Rački, a Croatian historian, retold in 1869 a Life of Theodosius of Trnovo written by Kallistos. In it, monks of Greek and Slavic birth gather round Gregory. Theodosius comes to him on the mountain Paroria, near Adrianople. Gregory sends him to Tsar Alexander of Bulgaria to seek protection from the Turks.
>
> The working of the Holy Spirit, Gregory wrote, is given in baptism to every believer. Through neglect of the commandments it lies buried under the passions, and waits for our repentance.

**D-M18 (card `knownFor`: "a monk who became a monk", and "brought" takes Meyer's side).**
- Current text: "A monk who became a monk on Mount Sinai, brought the prayer of the mind to the monks of Mount Athos…"
- Source: the notice says he taught it ("ἐδίδασκεν", PG150 l.69134) and found three monks already giving it a little time. "Brought", that is introduced ("eingeführt"), is Meyer's (MEYER l.4003).
- Fix: "A monk, tonsured on Mount Sinai, who taught the prayer of the mind to the monks of Mount Athos and built monastic houses in the paroria, the borderlands, of Macedonia." (This takes in D-M13.)

**D-M19 (card `dates`: "Kallistos" at first mention in the card, a name the scan lists as a namesake trap).**
- Current text: "…after a tradition he takes from Kallistos's Life."
- Evidence: the scan lists "the five Kallistoi" as namesake traps (Who_Scan_Era6.md l.232, 305). The card's later "his disciple Kallistos" comes after this first mention.
- Fix: "…after a tradition he takes from the Life by the patriarch Kallistos."

**D-M20 (card `keyWorks` 2: the sitting advice is a separate short piece).**
- Current text: under "On stillness and the two ways of prayer": "with his advice on how the hesychast, the monk of stillness, should sit at prayer…"
- Source: the fifteen chapters "DE QUIETUDINE ET DUOBUS ORATIONIS MODIS" begin at PG150 l.71961-71971. The sitting advice is a separate piece by him, "EJUSDEM QUOMODO OPORTEAT SEDERE HESYCHASTAM AD ORATIONEM" (l.72555-72561), followed by "Περὶ τοῦ πῶς δεῖ λέγειν τὴν εὐχήν" (l.72588).
- Fix: "…on the two ways into prayer of the mind. Printed after it are his short pieces on how the hesychast, the monk of stillness, should sit at prayer (on a stool, bent low, gathering the mind into the heart) and how to say the prayer."

---

### records.json (these profiles)

- **gregory-palamas.** Claims: add CANT2 l.34225-34240 and the son's part (D-B1); mark Gregoras's two causes (D-M1); add Kantakouzenos's "still boys" (D-M8); add the compilers' and Paisius's Slavonic claims (D-M9). Lead the many-gods claim with GREG3 l.13057 (D-M10). contested_claims: drop "Year of death", whose second side is a file header (D-M10). absent_details: I searched the four entries again with variants and accept them. The captivity letter is named in Philotheos (PALH l.7330-7333) with its text left out ("γράφων οὕτω· …"), which agrees with the note.
- **gregory-of-sinai.** Fix Basil's witness (D-B2). Add the Paisius "no one" claim and contested_claim (D-B3). absent_details: accepted after my search. Paisii of Hilendar (PAISII-H l.7135-7137, 1762) names a Bulgarian saint as Gregory's pupil under Tsar John son of Asen, with no birth or death detail. It does not break any absence.
- **Census text that tells as settled what held sources contest (for an Open-Gaps note; no census edit proposed).**
  1. `hesychasm-and-the-palamite-synthesis` `longDescription`: "Councils at Constantinople in 1341, 1347 and 1351 settled it in Palamas's favor". The `byzantine-church-palaiologan` entry: "Synods at Constantinople in 1341, 1347 and 1351 ruled for the hesychast monks. They made Gregory Palamas's theology the standard of Orthodoxy." Against this, Mansi's heading calls 1347 a "Pseudo-synodus" (MANSI26 l.10180). Combefis, after Gregoras, says no doctrine was debated in 1341 (l.19594-19597). The condemned side's case is in GREG2 and GREG3. The census's own sources note says the tomoi are the winning side's records.
  2. `hesychasm-and-the-palamite-synthesis` `documentedStories` "Palamas Among the Turks": "A storm drove the ship ashore near Gallipoli". Gregoras says a dead calm held the ship at anchor off the Hellespont for two days, and on the third barbarians in pirate boats took it, off the Scamander and Simoeis (GREG3 l.13063-13071, 13088-13092). The entry is marked "from reference summaries; primary text not yet read". The letter it rests on is not held (Palamas records, absent_details).

### Checklist summary

| # | Item | gregory-palamas | gregory-of-sinai |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Fail (D-B1) | Fail (D-B2, D-B4) |
| 2 | Quotes verbatim | Pass (no quotations in marks) | Pass (no quotations in marks) |
| 3 | No invented family, feeling, thought, anecdote, speech | Pass (D-B1 is a misreading, counted under 1) | Pass |
| 4 | Reading aids, no AI tells | Fail, minor (D-M4) | Fail, minor (D-M12, D-M14, D-M15, D-M18) |
| 5 | No role for a named witness | Pass (the 1857 editor is unnamed in the held file; the edition is named) | Pass (the notice is unsigned; the compilers are named in PHIL1, but tying the notice to them would be an inference) |
| 6 | Partisan or hostile witness named and marked | Fail, minor (D-M6) | Pass |
| 7 | Contested claim shows both sides | Pass | Fail (D-B3) |
| 8 | Common names with place at first mention, each text | Fail, minor (D-M2) | Fail, minor (D-M19) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene opening, disputes in place, length | Pass | Pass (with D-B3 told in place) |
| 11 | Readability (FK ≤10, Flesch ≥60) | Pass (7.61 / 64.29) | Pass (8.78 / 63.25) |
| 12 | Card order, missing fields absent, caveat in What is uncertain | Pass | Fail (D-B4) |
| 13 | Audio tags only in audio, at start and before last line | Pass | Pass |
| 14 | Keeps list line; a Who with body of work or following | Pass | Pass |

README lines on both men: true as written. I checked "No held source text gives his birth or death year" by search, and found only file headers. The Gregory of Sinai line does not touch Basil's preface, so D-B2 needs no README change. The README's "Paroria as a place … on the card" stays true under D-M13.

### Count

- **gregory-palamas:** 1 blocking (D-B1), 10 minor (D-M1 to D-M10).
- **gregory-of-sinai:** 3 blocking (D-B2, D-B3, D-B4), 10 minor (D-M11 to D-M20).
- **Part D total:** 4 blocking, 20 minor.

---

