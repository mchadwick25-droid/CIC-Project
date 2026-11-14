# R2 recheck: eight Who profiles, era 3 batch 7

A targeted recheck by three fresh Opus agents that had not seen the drafting or round 1, at full effort, in the same three parts as round 1. Each checked every R1 finding against its source, every changed line, each brief read whole, lengths, readability and the audio scripts. Totals: of the 7 R1 blocking points, 7 resolved; of the 49 R1 minors, 44 resolved, 4 partly resolved and 1 left for the coordinator (A-M5, Boethius's card tradition); new findings 0 blocking and 15 minor (part A 5, part B 6, part C 4).

## Part A


Scope: Boethius (major), Philoxenus of Mabbug (major) and John of Beth Aphthonia (recorder), with their cards, audio scripts and `records.json` entries, and the README lines on these three. I am a fresh reviewer. I did not draft or fix these files and had not seen round 1 before this recheck. I read the changes as a diff from `081a8d6b` (the drafts R1 reviewed) to HEAD (`1d5aa724`), limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch7/`, and compared the three `records.json` entries key by key. I then read each brief whole for flow. I opened every new or changed sentence, quotation and records entry at its line in the vendored file and checked who speaks there. Coordinator rulings applied: Boethius and Philoxenus are major; John of Beth Aphthonia is one Who as the Life's author, with his identity told as a contested claim and bar Aphthonia's facts kept apart. I edited no repo file, and made no git writes, model calls or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5 and so on.

Mechanical checks, all three:
- Each audio script equals its brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph (checked by script). No tag appears in a brief or card.
- `grade_text` passes for all three. Boethius sits on the floor (Flesch 60.5), so any wording change there must be re-scored. My Boethius fix below was re-scored.
- No narrator sentence runs past 25 words. The longest is Boethius l.5, "Hodgkin answered them from a fragment drawn from a lost work of Cassiodorus, which names a book on the Holy Trinity and one against Nestorius." (25), which is unchanged.
- `briefLength` matches on all three. All three cards and `records.json` parse.
- Unchanged brief quotes re-run with `vq.py` all pass: "it is the most unhappy kind of misfortune to have been happy" (l.8959-8960), "Faith is the foundation and the architect" (l.12638), "truly a stranger to God" (Walford l.6799). The card's new Aquinas quote passes ("Persona est rationalis naturae individua substantia", l.59310-59311).

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Boethius (MAJOR) | 401 | 2:29 | 8.1 | 60.5 | within 405 |
| Philoxenus of Mabbug (MAJOR) | 402 | 2:29 | 7.2 | 68.6 | within 405 |
| John of Beth Aphthonia | 321 | 1:59 | 6.0 | 72.7 | within 325 |

### 1. The 4 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| A-B1 (Boethius: a catalog of saints not in the Roman Martyrology told as the Roman Martyrology) | RESOLVED | Brief l.11: "The Bollandists, in their Acta Sanctorum of saints' days, list him as a martyr at Pavia." The day list under "DIES VIGESIMA SEPTIMA MAJI" (`acta-sanctorum_maii-tomus-6-lat_1739.txt` l.8030) gives "S. JOANNES Primus, Pontifex Roma- nus Martyr. Additur ex occaiione. S. Severinus Boetius, Exconlul. Ro- manos, Mattyi Xidni apud Inlu- bres" (l.8150-8155), which reads "Martyr Ticini apud Insubres". Card `legacy.remembered` 3, `uncertain` 5, the records claims and contested claim 3 no longer call the entry the Roman Martyrology's. The catalog entry at l.16492-16497 reads, through the OCR swaps, "in altero Catalogo eorum qui non sunt in Martyrologio Romano". R1's own fix wording calls this "an Italian catalog", which merges Ferrarius's two catalogs (R2-A-M1). |
| A-B2 (Philoxenus: Michael's "première interprétation" told as the first Syriac New Testament) | RESOLVED | Brief l.7: "Michael the Syrian says a Syriac version of the New Testament was made at Mabbug through his care." Michael: Thomas of Harkel revised the New Testament "après la première interpréta- tion qui avait été faite à Mabboug par les soins et du temps de l'évêque Philoxenus" (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.29482-29486). Card `keyWorks` 2 now reads "the earlier version made at Mabbug through Philoxenus's care". The records note cites Budge on the Peshitta: "all the quotations are taken from the Peshitta" (`philoxenus-of-mabbug_discourses_budge1894.txt` l.2807-2809), which holds. |
| A-B3 (John: Greek-era years 849 and 850 with no era) | RESOLVED | Card `dates`: "8 February of the year 849 of the Greeks, which E. W. Brooks gives as 538; Elias of Nisibis puts bar Aphthonia's death in the next year of that count." The extract: "Saint Mar Severe… sortit de ce monde en l'an 849, le 8 fevrier… et Mar Jean Bar Aphthonia mourut le 4 novembre" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.19884-19886). Brooks: "On Feb. 8, 538 Severus died in Egypt" (`severus-of-antioch_select-letters-book6-part1_brooks1903.txt` l.240-241). Elias: "Annus 849. Eo Severus patriarcha Iacobitarum mortuus est die 8° sabat… [Annus 850]. Eo Iohannes filius Aphthoniae doctor Iacobitarum mortuus est" (`elias-of-nisibis_opus-chronologicum-lat_brooks-chabot-csco1910.txt` l.5366-5373). The new records claim on the count holds: the extract's "En l'an 823" for Sidon (l.19739) matches Hamilton and Brooks, "THE EIGHT HUNDRED AND TWENTY-THIRD YEAR OF THE GREEKS", with their note "512" (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.8853-8854, 8888). Card `uncertain` 3 and contested claim 1 match. |
| A-B4 (John: Crum's catalog heading told as the sherd's text) | RESOLVED | Card `legacy.traces` 1 now says the fragment "holds a passage from a Life of Apa Severus, which W. E. Crum identifies as John of Beth-Aphthonia's." Crum's heading: "From the Biography of Severus of Antioch, by John of Beth-Aphthonia" (`monastery-of-epiphanius-thebes-pt2-coptic-ostraca_crum1926.txt` l.19898-19900). The sherd in his English: "From: the Life of the ….- Apa Severus" (l.19903). His note, read across the interleaved columns: "Ryl. 99, another extract from this work, shows that it was familiar in Egypt. Of this ms. (probably) there is a further fragt. in the Munich Library" (l.19912-19914). The records claim now separates the heading, the sherd and the note. |

### 2. R1 minor findings

**Boethius**
- A-M1: RESOLVED. "in the year Mommsen dates to 524". The margin "a. 524" stands beside "Iustino et Opihone" (`chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt` l.21303), and the header names Mommsen as editor. The records claim says so.
- A-M2: RESOLVED. The two paragraphs are joined, and the letter gives "Ptolemy the astronomer" (`cassiodorus_variae-letters-hodgkin1886.txt` l.7640-7641). The paragraph reads well. The join leaves Theodoric's identifier at his second mention (R2-A-M2).
- A-M3: RESOLVED. Card `uncertain` 1: "The Bollandists report one writer's doubt of the account of the Anonymus Valesianus, since others say the sword, and answer that the sword is not in Procopius." The passage reads "Suspectam hanc habet narrationem C… sibi ex MS. exhibitam prius quam vulgaretur; suspectam autem tali argumento, quod gladio ipsum interemptum alii dixerint. Sed hoc non legitur apud Procopium, vel apud Auctorem Catalogi Pontificum…" (l.16338-16343, heavy OCR). "Hoc" is the sword, so the card reads the answer rightly. The records mark the reading as reconstructed.
- A-M4: RESOLVED. "Thomas Aquinas, in the Summa of Theology, opens his article on the definition of a person by testing the one Boethius gives". The article opens "Videtur quod incompetens sit definitio personae quam Boetius assignat" (l.59306-59308).
- A-M5: OPEN, for the coordinator. The card's tradition is unchanged and the README keeps its reason. This is a census call and is not counted here.
- A-M6: RESOLVED. "the Paraenesis of Ennodius, bishop of Pavia". Hodgkin's index: "Ennodius, Magnus Felix, Bishop of Ticinum (died 516)" (l.23579), and Ticinum is Pavia (l.577).

**Philoxenus of Mabbug**
- A-M7: RESOLVED. "The chronicle under Zachariah's name, from his own side, says his zeal urged on the monks." The partisan witness is now placed once on each side, and the paragraph flows.
- A-M8: RESOLVED. The border clause is cut. The sentence is 21 words.
- A-M9: RESOLVED on both cards. "which Budge quotes from J. S. Assemani's Bibliotheca Orientalis"; "J. S. Assemani, in his Bibliotheca Orientalis, names two Johns".

**John of Beth Aphthonia**
- A-M10: RESOLVED. "Asking him was like hiring a worker in lead to make a royal crown." Kugener's "plombier" carries note 2, "morußdoupyös", that is μολυβδουργός (l.13188, 13196).
- A-M11: RESOLVED. "J.-B. Chabot and Rubens Duval write of the Life as John bar Aphthonia's, and E. W. Brooks names him its author." The full name "Rubens Duval" stands in a held note of Nau's (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt` l.10524). Brooks: "the later life by John archimandrite of Kenneshre" (Select Letters I l.191).
- A-M12: RESOLVED as a claim. "Zachariah Rhetor wrote another Life of Severus" is true: Hamilton and Brooks, "between 511 and 518 wrote a Life of Severus" (l.365); Kugener, "VIE DE SEVERE, PAR ZACHARIE LE SCHOLASTIQUE" (l.76). The Ethiopic Life by Athanasius is held (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.663-665), so dropping "two" is right. In place, though, the sentence floats (R2-A-M3).
- A-M13: PARTLY. The added purpose is gone: Michael says Jacob "alla au monastère d'Aphtonia et y prit l'habit monastique. Il y étudia soigneusement les Psaumes en langue grecque" (l.36363-36366). R1's second point was that the close leaves the listener to take this house for the writer's, which the card gives as disputed. R1's fix wording did not address that, and the brief still does not (R2-A-M4).
- A-M14: RESOLVED. "John bar Aphthonia's house at Kenneshre became a place of Greek learning."
- A-M15: RESOLVED. Kugener's French form is dropped from `otherNames`.

### 3. New findings

No new blocking points in part A.

- **R2-A-M1 MINOR (Boethius card `legacy.remembered` 3 and `uncertain` 5; `records.json` contested claim "Whether he died a Christian, and whether he is a martyr"; items 1 and 5; carried by R1's own A-B1 fix wording).**
  - The card says: "They also quote an Italian catalog of saints who are not in the Roman Martyrology, which names him a martyr at Pavia under Theodoric."
  - The passage names two catalogs by Ferrarius. One is of the saints of Italy and the other is of saints not in the Roman Martyrology. Read through the OCR: "Ferrarius, in Catalogo Sanctorum Italiae agit de S. Severino Boetio Martyre Ticini… & in altero Catalogo eorum qui non sunt in Martyrologio Romano, Ticini S. Severini Boetii Martyris, sub Theodorico Gothorum Rege" (l.16492-16497). The OCR has "is Car 4/d^*54Jr^«* ram Italia agit dt S. Severino Boctio Martyrc Ticini" and "in altera Cata- lagaearamqainanfantia Alartpralogia Ramana".
  - "An Italian catalog of saints who are not in the Roman Martyrology" merges the two. The card also leaves the compiler unnamed, though the records claim names him.
  - Fix, card `legacy.remembered` 3, second sentence: "They also cite two catalogs of saints by Ferrarius, one of the saints of Italy and one of saints who are not in the Roman Martyrology. Both name him a martyr at Pavia, the second under Theodoric."
  - Fix, card `uncertain` 5, last clause: "the title comes from the Bollandists and the later catalogs they cite."
  - Fix, records contested claim: "and cite Ferrarius's two catalogs, of the saints of Italy and of saints 'qui non sunt in Martyrologio Romano', both naming him a martyr at Pavia, the second under Theodoric (l.16492-16497; reading reconstructed from heavy OCR)". Make the same change to the absent-detail note's "the catalog of saints not in the Roman Martyrology that they quote".

- **R2-A-M2 MINOR (Boethius brief l.1 and l.3; item 8).**
  - l.1 names "King Theodoric" with no identifier. The identifier comes only at the second mention, in the paragraph A-M2 joined: "Theodoric, the Ostrogothic king of Italy". Theodoric is a name a listener can take for more than one king.
  - Fix, l.1: "Boethius stood before Theodoric, the Ostrogothic king of Italy, to defend a fellow senator, Albinus, accused of writing to the emperor Justin against the king."
  - Fix, l.3, first sentence: "Boethius was a Roman senator under Theodoric and was consul in 510."
  - Re-scored with both: 400 words, FK 8.1, Flesch 60.4. That passes, but sits on the floor.
  - The audio script follows.

- **R2-A-M3 MINOR (John brief l.3; item 4, a line with no context).**
  - Paragraph 2 now reads: "The heading names the writer as John, superior of the monastery of Beith Aphthonia. He calls himself small and not learned in letters. Zachariah Rhetor wrote another Life of Severus."
  - The last sentence links to nothing on either side. Coming after the writer's self-abasement, it reads as an implied contrast that no source makes. It is also the third short sentence in a row, so the paragraph reads as a list.
  - The fact is not needed for John's story, and the card does not depend on it.
  - Fix: drop "Zachariah Rhetor wrote another Life of Severus." The records claim can stay as support for the card's sources. This also buys the words R2-A-M4 needs.

- **R2-A-M4 MINOR (John brief l.11; items 1 and 7; the open half of A-M13; the coordinator's ruling that bar Aphthonia's facts are kept apart).**
  - The close, "Michael the Syrian says Jacob of Edessa later became a monk at the monastery of Aphthonia and studied the Psalms there in Greek", follows a brief in which "the monastery of Beith Aphthonia" is the writer's house. A listener takes Jacob's monastery for the writer's.
  - The card gives that identification as disputed (`uncertain` 2: John of Ephesus names a monastery of Aphthonia at Charrhae). Bar Hebraeus names Jacob's house as Kenneshre: "in monasterio Aphtonii seu Kenserinensi graecam linguam… didicit" (`barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` l.17306-17309). The brief has already told Kenneshre as bar Aphthonia's house (l.7).
  - Fix, l.11, add a second sentence: "Bar Hebraeus calls it the Kenneshre monastery."
  - With R2-A-M3: 321 words (1:59), FK 5.8, Flesch 74.0.
  - The audio script follows. `[warmly] ` stays at the start of l.11.

- **R2-A-M5 MINOR (README, the John of Beth Aphthonia year in the order paragraph; internal text; part C owns the README, so this is flagged for it).**
  - The README says: "John of Beth Aphthonia (538, the Library header's year for the archimandrite John bar Aphthonia, whom he may or may not be)".
  - The header gives the year to the writer, not the archimandrite: "John of Beth Aphthonia (d. 538)" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.6-7). No held line gives 538 for either man. Brooks's 538 is Severus's year. The extract and Elias give the archimandrite the years 849 and 850 of the Greeks.
  - Fix: "John of Beth Aphthonia (538, by the Library header, which gives the year to the writer; the held sources date only the archimandrite John bar Aphthonia, whom he may or may not be, to 849 or 850 of the Greeks)".

Not findings:
- **Boethius brief, whole.** The order runs from the scene to the senator, the tractates, the fall, the four death accounts, the faith dispute and his own words. It reads as one story. The joined paragraph 2 is smooth.
- **"Acta Sanctorum of saints' days".** This is a fair gloss for a listener.
- **Philoxenus brief, whole.** The A-M7 marker sits naturally, and the Flavian paragraph now places a witness on each side. The l.7 Michael sentence ends the teaching paragraph on a fact about his work and does not read as a tail.
- **John card `dates`.** It gives the archimandrite's 4 November inside the entry for the year 849 without converting that year, and it states no year of its own. `uncertain` 3 adds that the Life puts his death before Severus's. That is consistent with the extract, since in that entry November precedes February.
- **README Boethius sentence.** "Mommsen's year for the consuls under whom Marius of Avenches puts his death" matches l.21303-21310.
- **README Kugener sentence.** "the later of the two Lives of Severus that M.-A. Kugener edits" matches Brooks's "the later life" and the volume's title (l.1-3).

Totals for part A: of the 4 R1 blocking points, 4 are resolved. Of the 15 R1 minors, 13 are resolved, 1 is partly resolved (A-M13, carried by R2-A-M4) and 1 is open for the coordinator (A-M5). There are 0 new blocking points and 5 new minor points (R2-A-M1 to R2-A-M5).

## Part B


Scope: Fulgentius of Ruspe (major), Primasius of Hadrumetum and Avitus of Vienne, with their cards, audio scripts and `records.json` entries, and the README's Avitus sentence (C-M16). I am a fresh reviewer; I did not draft or fix these files. I read the changes from `081a8d6b` (the drafts R1 reviewed) to HEAD (`1d5aa724`), limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch7/`, as a word diff for the cards and README and entry by entry for `records.json`. I then read each brief whole for flow. I opened every new or changed sentence, quotation and records entry at its line in the vendored file, and checked who speaks there: the ancient writer, a document he copies, an editor's text or an editor's index. I edited no repo file, and made no git writes, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5 and so on. Card fields are named by key and 0-based list position.

Mechanical checks, all three:
- Each audio script equals its brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph (checked by script). No tag appears in a brief or card.
- `grade_text` passes for all three. Primasius (Flesch 60.7) sits nearest the floor.
- No narrator sentence runs past 25 words. The longest is Fulgentius l.1, "When the Arian bishop of the district offered to punish the priest…" (24).
- `briefLength` matches on all three. All three cards and `records.json` parse.
- No new or changed quotation in the briefs. Changed quotations in records were run through `vq.py` or read at the line where OCR defeats it.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Fulgentius of Ruspe (MAJOR) | 404 | 2:30 | 7.4 | 68.6 | within 405 |
| Primasius of Hadrumetum | 321 | 1:59 | 8.4 | 60.7 | within 325 |
| Avitus of Vienne | 325 | 2:00 | 6.6 | 68.6 | 325, at the cap |

### 1. The R1 blocking finding

| Finding | Status | Evidence |
|---|---|---|
| B-B1 (Primasius: Kihn's "Adrumetinus" misread as a monastery of Hadrumetum) | RESOLVED | Card `uncertain` 1 now reads: "The manuscripts of Victor read aquimetensis, and Migne prints Aquimetensis. Theodor Mommsen corrects it to Acoemetensi… Heinrich Kihn quotes the line with Adrumetinus, naming Primasius by his city, and names no monastery. He places the sending after Primasius's refusal to attend the council in May 553, though Victor tells it under 552." Mommsen's text has "Primasius quoque Acoemetensi monasterio relegatur" (l.19115) and the apparatus "aquimetensis libri" (l.19164). Migne prints "Piimasius quoque Aquime-/tensis monaslerio relegatus" (PL 68 l.74708-74709). Kihn: "Primasius quoque Adrumetinus (Migne: Aquimetensis) monasterio relegatus" (OK by `vq.py`, l.12674-12675), and in his own telling only "wurde er in ein Kloster relegiert" (OK, l.12690). The placing holds too: Kihn's footnote 1 is keyed to the council's ruling after the 8 May refusal, "De Primasio quidem… quae oportet disponantur" (l.12645-12646), and the note reads "Hierher fällt nach meinem Erachten die Relegation" (OK, l.12673-12674). Records claim 15 and contested claim 1 ("Kihn names no monastery (l.12675, l.12690)") match. |

### 2. R1 minor findings

**Fulgentius of Ruspe**
- B-M1: RESOLVED. Brief l.5 "reading Augustine of Hippo on Psalm 36"; l.7 "Theodoric, the Ostrogothic king"; card `knownFor` "a follower of Augustine of Hippo". Records claim 11 cites Fulgentius's own "Augustinum Hipponensem" (PL 65 l.42467, read). Records claim 15 cites Dalton's "Theodoric the Great, king of the Ostrogoths" (l.23889-23890, read). "In Africa" was cut from l.5; l.1 already sets the scene "near Sicca in North Africa".
- B-M2: RESOLVED. Brief l.3: "The Life of Fulgentius, by a Catholic monk who lived with him, tells this from what Fulgentius told him." The Life: "omnia quae memoriter nobis audientibus ipse referebat" (l.8003-8004) and "sicut ipse nobis postea referebat" (l.8501). Records claim 5 ties the wording to both.
- B-M3: RESOLVED. Card `legacy.traces` 0 now has Facundus apart: "and Facundus of Hermiane says Faustus was exposed and refuted by Fulgentius of holy memory". Facundus: "a sanctae memoriae Fulgentio Ruspensi detectus atque convictus est" (PL 67 l.66179-66183). Records claim 34 and the `absent_details` note on the lost books now say Facundus names no books.

**Primasius of Hadrumetum**
- B-M4: RESOLVED. Brief l.7 opens "The rest is told only by Victor of Tunnuna, who defended the Three Chapters and tells it as betrayal." "Only Victor" still holds: the PL 67 note, the PL 68 note to Liberatus, Kihn and Mesnage all rest on Victor. "The rest" no longer dates the sending after the signature, and the card's `uncertain` 1 gives both placings.
- B-M5: RESOLVED in the brief. "Primasius agreed to condemn the Three Chapters so that he might take his place." Victor: "memoratae damnationi protinus assensit" (l.19116); the condemnation is the Three Chapters', named just before in Firmus's entry, "damnationi eorumdem Capitulorum assensum praebuit" (PL 68 l.74705-74707). Records claim 11 glosses it. The card's `uncertain` 0 still has the vague "gave way" (R2-B-M1).
- B-M6: RESOLVED. "In the same way, wherever truth shines, it should be won back for the Catholic Church." Prologue: "ita undecunque veritas clareat, catholicae defendenda est unitati. Huic enim soli competit quidquid veritas foris etiam personarit … cum verae matri fuerit redditum" (PL 68 l.62678-62685). The sentence is framed by "he wrote" in the sentence before. It is Primasius's claim told in modern words, not a narrator's saying.
- B-M7: RESOLVED. Brief l.9 "Augustine of Hippo"; card `knownFor` "Augustine of Hippo and the Donatist Tyconius". Records claim 25 notes the placing through Isidore's notice.
- B-M8: RESOLVED. "Victor of Tunnuna says the emperor summoned him there with other African bishops. Victor's editor, Theodor Mommsen, gives the year as 551." Victor l.19057-19062, under Mommsen's 551.
- B-M9: RESOLVED. `keyWorks` 1 `about` now ends: "The notice from Cave that Migne prints calls it long lost; it reports an old manuscript that gives the surviving Praedestinatus to Primasius, and doubts it." Notice: "Interiit jam dudum opus istud" (l.34982-34983); "Longe potiori jure tribuendi videntur Primasio nostro, idque fide vetusti codicis… in bibliotheca Augiensi vidit cl. Mabillonius" (l.35020-35023); "Opus sancti Primasii, discipuli Augustini, de Haeresibus numero XC" (l.35027-35028); "quisquis hanc notulam codici Augiensi apposuit, forsan hallucinatus" (l.35030-35031), with the reason that whoever wrote it knew from Isidore of three books and put the name on three anonymous ones (l.35038-35040). The card's "and doubts it" is the notice's last word on the point. Records claim 32 is now Contested, but no contested-claim record stands behind it (R2-B-M3).
- B-M10: RESOLVED in substance. `dates`: "Vigilius's ruling, which he signed, is dated the day before the Ides of May…" (Avellana l.24223-24225; Günther l.18303) and "He tells of his fall and death under 552, an entry that runs past that year, since Primasius signed in May 553." The facts are right. The new "He" now follows "Theodor Mommsen" (R2-B-M2).
- B-M11: RESOLVED. `knownFor` "a commentary on the Apocalypse of John".
- B-M12: RESOLVED. Both tail sentences are gone. Removing the second left "grey" ending a changed line (R2-B-M5).
- B-M13: RESOLVED. Records claim 7 cites Kihn, "am 5. Mai 553 … vom Kaiser eröffneten" (l.12603-12604) and the sixteen signers (l.12652-12657). Claim 8 cites Kihn on Theodore's writings, Theodoret's writings against Cyril and the letter of Ibas (l.12648-12652). The council profile is kept as a cross-reference.

**Avitus of Vienne**
- B-M14: RESOLVED. Brief l.9: "His Life says he died under the emperor Anastasius, and gives no year. Peiper corrects the emperor to Justin." Life "Moritur Anastasio adhuc principe" (l.18342); Peiper "immo Iustino" (l.18385; index l.30143). The card keeps the wider absence.
- B-M15: RESOLVED. "Once Gundobad was lost in his unbelief, Agobard says, Avitus turned his son and heir Sigismund to the Catholic faith." Agobard "ipso Gundobado in sua perfidia perdito" (l.5548). Brief and card now agree. Records claim 20 notes that the words do not settle whether Gundobad had died.
- B-M16: RESOLVED. "Peiper tentatively dates…" The table line is l.43290 as the drafter corrected ("intra a. 513 — 510?", OCR for 516?).
- B-M17: RESOLVED. Card `dates` "his Life puts this in the time of the emperor Zeno, and no source used here gives a year"; `uncertain` 0 "No source used here gives the year he became bishop; his Life puts it in the time of the emperor Zeno." Life "Tempore Zenonis imperatoris" (l.18084). Records claim 8 notes it.

**C-M16 (Avitus card and records; README)**
- RESOLVED on the card and in records; PARTLY in the README (R2-B-M6).
- Card `dates`: "Peiper's index places it before 533, when Julian signs as bishop of Vienne at the council of Orléans. It places it after a homily at Geneva that Binding dates to the end of 525 or the start of 526."
- Card `uncertain` 0 adds: "That homily's date is Binding's, and Peiper's preface puts all the Geneva letters and homilies between 513 and 516."
- Peiper's index: "incertum quo anno, sed post a. 525 ex. vel 526 in. quo tempore homiliam in dedicatione basilicae Genevensis dixit, ante a. 533, nam in concilio Aurelianensi Iulianus episcopus Viennensis subscripsit" (l.30143-30149).
- The prooemium: "non ante 525 ex. vel 526 in. putat Bindingius" (l.3377-3378), and "Omnes autem et epistulas et homilias, quae pertinent ad Genevam urbem, intra annos 513 et 516 scripsisse puto Avitum" (l.3380-3381, OCR "antem", "quac").
- The homily is the one on the Geneva church of Bishop Maximus (l.3358-3363), so "a homily at Geneva" is right. The Orléans 533 list has "Iulianus episcopus" with the note "Viennensis" (Maassen l.5637 and l.5652).
- Records claim 32, contested claim 2 (third side) and `absent_details` 0 match and cite the lines. They also keep the earlier search result apart from the index read directly. That is honest about how the window was missed.

### 3. New findings

No new blocking point.

- **R2-B-M1 MINOR (Primasius card `uncertain` 0; items 1 and 4; B-M5 fixed in the brief only).** "Victor says he was sent to a monastery, gave way so that he might succeed Boethius as head bishop of Byzacena…" The card is its own text, and it still never says what he gave way on. The brief now says it. Fix: "Victor says he was sent to a monastery, agreed to condemn the Three Chapters so that he might succeed Boethius as head bishop of Byzacena, persecuted his former side at home, was condemned by his own province's bishops and died an unhappy death."
- **R2-B-M2 MINOR (Primasius card `dates`; item 4; carried by R1's B-M10 wording).** "Victor of Tunnuna tells of his summons to Constantinople under the year Theodor Mommsen gives as 551. He tells of his fall and death under 552…" The nearest man before "He" is Mommsen. The 552 entry is Victor's and not Mommsen's. Fix: "Victor tells of the fall and death under 552, an entry that runs past that year, since Primasius signed in May 553."
- **R2-B-M3 MINOR (Primasius `records.json`; item 7, the Confidence rule).** Claim 32 was raised to Contested under B-M9, but `contested_claims` has no record for it. The pattern says a Contested claim "has a `contested_claim` record behind it". Fix, add to `contested_claims`: `{"claim": "Whether his work on heresies is lost, or survives as the Praedestinatus", "sides": "Lost: the notice from Cave that Migne prints, 'Interiit jam dudum opus istud' (liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866 l.34982-34983), which ends by doubting the Reichenau title: 'quisquis hanc notulam codici Augiensi apposuit, forsan hallucinatus' (l.35030-35031). His: the title in the old Reichenau manuscript Mabillon saw, 'Opus sancti Primasii, discipuli Augustini, de Haeresibus numero XC' (l.35027-35028), toward which the same notice first leans: 'Longe potiori jure tribuendi videntur Primasio nostro' (l.35020-35021). Other authors the notice reports for the Praedestinatus: Sirmond's Arnobius the Younger and Piccinardus's Vincentius (l.35002-35017)."}`
- **R2-B-M4 MINOR (Avitus card `uncertain` 4; item 9; a spelling clash created by C-M16).** The C-M16 text writes "the council of Orléans" in `dates` and `uncertain` 0. `uncertain` 4 still has "the abbot Avitus of Micy near Orleans". One place now has two spellings on one card. The README and records use "Orléans". Fix, `uncertain` 4: "…the abbot Avitus of Micy near Orléans, whom Gregory of Tours shows pleading with King Chlodomer for Sigismund's life."
- **R2-B-M5 MINOR (Primasius card `uncertain` 7; British spelling in own prose; a line B-M12 changed).** "for his venerable grey hair." No other Who card uses "grey". Fix: "His age. Andrea Gallandi wonders whether Junillus calls him Father for his venerable gray hair." The same word in records claim text can follow.
- **R2-B-M6 MINOR (README Avitus sentence; C-M16 as worded by R1).** The README reads: "Peiper puts his death under Justin and before 533, when Julian signs as bishop of Vienne at Orléans; the Library header's 518 is the earliest year that allows". Peiper's index also sets a lower bound, after late 525 or early 526 (l.30143-30145). Taken at its word, that bound would put Avitus after Philoxenus (523) and Boethius (524) in the batch order. The bound rests on Binding's date for the Geneva homily, which Peiper's own preface doubts (l.3380-3381). So the order can stand, but the README should say why. Fix: "Avitus of Vienne (no held source gives a year; Peiper puts his death under Justin and before 533, when Julian signs as bishop of Vienne at Orléans; his index's later bound, after a Geneva homily that Binding dates to 525 or 526, is one his own preface doubts, so the order uses 518, the first year of Justin, as the Library header does)". The README is part C's file; I give the fix here because C-M16 sent the Avitus side to this part.

### 4. Each brief read whole

- **Fulgentius.** The brief reads as a story from the beating at Sicca to the return to Carthage. The B-M1 and B-M2 changes fit without seams. Cutting "in Africa" from l.5 loses nothing, since l.1 has "North Africa". In l.3, "tells this from what Fulgentius told him" repeats "tell". That is a matter of polish and not a fault.
- **Primasius.** The order is clear: the scene with Junillus, who he was and why he came, the signature, Victor's story with its witness marked, then the commentary. Splitting the Mommsen sentence (B-M8) keeps l.3 easy to follow. "The rest is told only by Victor" makes a clean turn. The close is his own image, told in modern words.
- **Avitus.** The new two-sentence death paragraph (l.9) names the Life's silence and Peiper's correction plainly and no longer opens on an absence. The brief stays at 325 words, at the cap. It does not need the 533 window, which the card carries.

### Not findings

- **"Heinrich Kihn quotes the line with Adrumetinus" (Primasius card `uncertain` 1).** Kihn sets his reading against Migne's ("Migne: Aquimetensis"), so it is his emendation and not a manuscript reading. The card says what he prints and that he names no monastery. Nothing in it is wrong, and the sentence before gives the manuscripts' reading.
- **"Peiper corrects the emperor to Justin" (Avitus l.9).** This follows "the emperor Anastasius", so the context marks the emperor. It needs no further place or number.
- **Victor placed twice (Primasius l.7).** Victor is marked once as partisan ("who defended the Three Chapters"). Kihn's warning is a second, named witness to that judgment, not a repeat.

### Totals for part B

B-B1 resolved. Of the 17 R1 minors, all 17 are resolved. C-M16 is resolved on the Avitus card and records, and partly resolved in the README (R2-B-M6). New: 0 blocking and 6 minor (Primasius 4: R2-B-M1, M2, M3, M5; Avitus 1: R2-B-M4; README 1: R2-B-M6). None of the minor fixes touches a brief, so length, readability and audio stay as measured.

## Part C


Scope: `eugippius` (recorder) and `ciaran-of-clonmacnois` (founder known through a late Life), with their cards, audio scripts and `records.json` entries, and the batch `README.md`. I am a fresh reviewer; I did not draft, review in round 1, or fix these files. I read the changes as a word diff from `081a8d6b` to HEAD, limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch7/`, and compared the two `records.json` entries object by object against the `081a8d6b` copy. I then read each brief whole for flow. Every new or changed sentence, quotation and records entry was opened at its line in the vendored file, and I checked who speaks there: the ancient writer, a document he copies, the translator, an editor's note, or an index. Quotations were checked with the scratchpad `vq.py`, and OCR passages were read by line. I edited no repo file. I made no git writes, model calls or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5, 7, 9 and 11.

Mechanical checks, both profiles:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes for both. No narrator sentence runs past 25 words. The longest are Eugippius l.5, "He gathered a memoir…" (23, most of it quoted), and Ciaran l.1, the stake line (23, mostly quoted).
- Every quotation in both briefs, and every new quotation on the cards, is verbatim. Robinson: "are more easily depicted by their pupils" (l.4259-4260), "Even in the lifetime of Saint Severinus" (l.477), "a fragrance of such sweetness…" (l.3962-3963), "The deeds of the good cannot perish with time" (l.4231). Lismore: the stake line (l.22700-22701), "Awful is this way above" (l.22820). Tripartite: "a year before Ciaran's obit" (l.16366-16368). Huyshe: "the Clonoensian monastery of St. Ceran" (l.2735-2736).
- `briefLength` reads "about 2 minutes" on both. Both cards and `records.json` parse.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Eugippius (recorder) | 324 | 2:00 | 6.9 | 69.0 | within 325 |
| Ciaran of Clonmacnois | 323 | 2:00 | 6.5 | 73.5 | within 325 |

### 1. The 2 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| C-B1 (Ciaran: the Life misreported on his teachers and first house) | RESOLVED | Brief l.7: "The Life then takes him to Enda of Aran. Before Clonmacnois he led a house on the island of Inis Angin for three years." Lismore: "Ciarán went to Aran to commune with Enna" (l.22541); on Inis Angin the priest "gave the island up to him" (l.22640-22641); Enna Mac-Hui-Laigsi "became abbot after Ciarán" (l.22650); "Three years, then, and three months dwelt Ciarán in Inis Angin" (l.22667-22668). "Other teachers" is gone. Card `uncertain` 6 has the R1 text. Findian "his tutor" (l.22512); "suo magistro" (AS March III l.76789) and "sui Abbatis Endei" (l.76802-76803) are both Enda; the threshing years are "septem annis… trituratoris officium" on Aran (l.76780-76786). The Bollandists' "priusquam in S. Sennani disciplinam concederet, sub hoc S. Endeo monastica vitae potuisset tyrocinia" (l.75805-75807) is rightly given as "may have". Magraidin "ex duabus vetustioribus tam exiguo judicio consarcinavit" (l.75742-75747) supports "patched it together from two older Lives with very little judgment". Records claim 18 and contested claim 2 match. |
| C-B2 (Ciaran: false absence, "no earlier source") | RESOLVED | Card `uncertain` 1: "Apart from his baptism by the deacon Justus, which Tirechan also tells, its stories… are told in no earlier source used here". Lismore: "He was baptized by deacon Justus" (l.22098-22100); "his tutor, deacon Justus" (l.22145). Tirechan: "babtitzatus est Ceranus ex libro Patricii, a diacono Iusto" (Tripartite l.3476-3477, OCR "lusto"). The changes file's line correction is right. Records claim 8 is new and matches. See the Comlach note under Not findings. |

### 2. R1 minor findings

**Eugippius**
- C-M1: RESOLVED. Brief l.1: "When Count Pierius forced the Romans out of Noricum's Danube towns…". Onoulf "ordered all the Romans to migrate to Italy" (l.3927-3928). The provincials "abandoned the towns on the banks of the Danube" (l.3976-3977). Robinson's note on Jung is at l.3979-3986. The split keeps both sentences short. Records claim 1 carries all three passages, at the right lines.
- C-M2: PARTLY. Card `uncertain` 1 and records claim 25 are right ("are more easily depicted by their pupils", l.4259-4260). The brief's paraphrase overstates the comparative and frames Paschasius as answering the doubt (R2-C-M1).
- C-M3: RESOLVED. "the Roman deacon Paschasius" in brief l.5 and card `dates`. Robinson's index: "Paschasius, Roman deacon, 126." (l.5838).
- C-M4: RESOLVED. "Augustine of Hippo" in brief l.9, card `knownFor` (the card's first mention; the drafter rightly moved the identifier there) and `keyWorks` 2. Sigebert, as Gallandi quotes him: "libros Augustini episcopi fIip- pouensis" (PL 67 l.68093-68094).
- C-M5: RESOLVED. Card `uncertain` 1: "…he heard no more of the saint's homeland than he tells." Robinson l.477-479, with what he had related at l.446-448 ("a man of purest Latin stock", "some desert place of the East"). The records' corrected lines (446-448, 477-479) are right, and R1's l.440-447 and 474-476 were off.
- C-M6: RESOLVED. Card `uncertain` 2: "he read the layman's letter 'About two years ago, in the consulship of Importunus'" (l.278-281).
- C-M7: RESOLVED. Card `uncertain` 3. Gallandi: "commentum de duobus Eugippiis, quorum alter italus, Africanus alter fuerit, Miraeo, Bollando, Caveo aliisque probatum" (PL 67 l.68087-68090); Sigebert "Fuit tempore Pelagii II et imperatoris Tiberii Constantini" and "bifariam errat Sigebertus" (l.68096-68098); "Sigeb. Gembl." (l.67956). Records claim 29 says Gallandi does not name Fabricius.
- C-M8: RESOLVED. Card `legacy.remembered` 3: "the words of Teuffel's History of Roman Literature". Robinson: "Teuffel and Schwabe's History of Roman Literature" (l.179-180); "the work which Teuffel terms 'the incom- parable biography of Saint Severinus'" (l.117-118).

**Ciaran of Clonmacnois**
- C-M9: RESOLVED. Brief l.3: "It is a saint's Life, the house's own telling of its founder, written down long after him." Records claim 5 matches.
- C-M10: RESOLVED. The Stokes sentence is split. The two sentences now both turn on "says"; see Not findings.
- C-M11: RESOLVED. `knownFor`: "…an Irish Life that Whitley Stokes says was composed at Clonmacnois, kept in a book of the 1400s." Stokes: "compiled… in the latter half of the fifteenth century" (l.218-219); footnote (l.22789). Records claim 3 tags the footnote Dominant Modern Reconstruction and names Stokes.
- C-M12: RESOLVED. `legacy.remembered` 1: "Columba, Colum Cille in Irish". The Lismore passage is l.21978-21981 ("as Colombcille said, — Lucerna hujus insulce"); Stokes's note is "Lucerna huius insulae" (l.28776).
- C-M13: PARTLY. The date is now given, but without the note's "probably" (R2-C-M3).
- C-M14: RESOLVED. `uncertain` 3: "in their commentary on the Life of Enda"; the 544 is "circa extremum Thuatalii Regis annum, Christi DXLIV" in the commentary's §7 (AS March III l.75798-75812). `uncertain` 7: "The index to Stokes's Tripartite Life"; "Ciaran, son of Darerca, eps., 550." (Tripartite l.22152).
- C-M15: RESOLVED. Records claim 3 pins the footnote to "this city" (l.22755-22756); the footnote is l.22789.

**README**
- C-M16: PARTLY. The README's Avitus clause now names Peiper and the 533 end. But it leaves out the lower bound that the same index line gives. It also calls 518 "the earliest year that allows", which the index does not allow (R2-C-M4). The Avitus card does give that lower bound.
- C-M17: RESOLVED. "Boethius (524, Mommsen's year for the consuls under whom Marius of Avenches puts his death)": Marius under "Iustino et Opilione", Mommsen's margin "a. 524" (records, Boethius; Chronica Minora 2 l.21303-21310). "John of Beth Aphthonia (538, the Library header's year for the archimandrite John bar Aphthonia, whom he may or may not be)": the header gives "John of Beth Aphthonia (d. 538)" (Kugener PO 2 l.6-7), which the records call a cataloguer's merging. The year fits the archimandrite, since Elias puts John son of Aphthonia's death the year after Severus's (records, Elias claim). The Kugener wording ("the later of the two Lives… that M.-A. Kugener edits"; Chabot and Duval "write of the Life as his") matches the John profile's records.

### 3. New findings

- **R2-C-M1 MINOR (`eugippius.brief.txt` l.7; items 1 and 7; a paraphrase stronger than its source).**
  - The brief says: "Paschasius answers that teachers are best portrayed by their pupils."
  - Paschasius writes that the virtues of teachers "are more easily depicted by their pupils" (l.4259-4260). He says this to explain why he adds nothing: "it is one thing to relate what we have been told, quite another thing, to draw from the stores of our own experience" (l.4255-4257).
  - "Best" turns his comparison into a superlative. "Answers" makes him reply to the doubt the narrator has just raised, when he is replying to the memoir. The card (`uncertain` 1) gets both right.
  - Fix: "Paschasius replies that teachers are more easily portrayed by their pupils." (+1 word; see the length note below.)

- **R2-C-M2 MINOR (`eugippius.brief.txt` l.9, card `keyWorks` 2; items 4 and 8; a name with no context).**
  - "Cassiodorus says he saw him." gives the listener nothing to place Cassiodorus by. The pattern's common-name standard covers "any name a general listener would not know". All the brief's other witnesses carry a place or a role: Isidore of Seville, Andrea Gallandi, G. W. Robinson, Count Pierius and the priest Lucillus. Round 1 did not raise this.
  - Hodgkin's introduction places him: "the statesman who, after spending thirty years at the Court of Theodoric and his daughter, spent thirty-three years more in the monastery which he had himself erected at Squillace" (`cassiodorus_variae-letters-hodgkin1886.txt` l.1119-1121). The file header gives "Magnus Aurelius Cassiodorus Senator" and describes the letters as "The chancery letters of Theoderic and his successors" (l.1-2, 16-17). The card already cites Hodgkin.
  - Fix, brief l.9, replacing the first two sentences: "Cassiodorus, a statesman of Gothic Italy, says he saw him, and calls him not deeply trained in worldly learning but full of the Scriptures." This keeps Cassiodorus's own contrast attributed to him ("non usque adeo saecularibus litteris eruditum, sed divinarum Scripturarum lectione plenissimum"). It also removes the "He… Cassiodorus writes" pronoun turn, where a listener can briefly hear "He" as Cassiodorus.
  - Card `keyWorks` 2, `about`, at the card's first mention: "…for Proba, a consecrated virgin, in the account of Cassiodorus, a statesman of Gothic Italy; …".
  - To hold the length, also change l.5 "a holy man of the borderlands of the Danube" to "a holy man of the Danube borderlands", and "Then he began to tell the clergy" to "He began to tell the clergy".
  - With R2-C-M1 and R2-C-M2 applied together to a scratch copy: 326 words (2:01), FK 7.2, Flesch 67.8. No narrator sentence runs past 24 words. That is one word over the about-325 line, within "about".

- **R2-C-M3 MINOR (card `ciaran-of-clonmacnois` `uncertain` 4; records claim 26; items 1 and 7; an editor's "probably" told as settled, carried by R1's own C-M13 wording).**
  - The card says: "Gilla Coemain's chronological poem, which a note in Stokes's edition dates to 1072, puts it…".
  - The note reads: "The meaning probably is (as O'Conor says) that the new moon fell in 1071 on the 25th Dec., and that therefore there were seven days thence to Jan. 1, 1072, the year in which these verses were made." (Tripartite l.15790-15797.) The 1072 depends on a reading the note calls probable, and the reading is O'Conor's.
  - Fix: "King Tuathal Maelgarb's death. The Lismore Life puts it on the night Ciaran planted the first stake, seven months before his own death. Gilla Coemain's chronological poem puts it 'a year before Ciaran's obit', in Stokes's English. A note in Stokes's edition, following O'Conor, says the verses were probably made in 1072."
  - Records claim 26 already quotes "probably" through "as O'Conor says". Its prose should say "probably dates the verses to 1072" so it matches.

- **R2-C-M4 MINOR (`README.md` l.5; a witness's window cut in half, carried by R1's own C-M16 wording).**
  - The README says: "Avitus of Vienne (no held source gives a year; Peiper puts his death under Justin and before 533, when Julian signs as bishop of Vienne at Orléans; the Library header's 518 is the earliest year that allows)".
  - Peiper's index, in the same parenthesis that gives 533, also gives a lower bound: "incertum quo anno, sed post a. 525 ex. vel 526 in. quo tempore homiliam in dedicatione basilicae Genevensis dixit, ante a. 533" (`avitus-vienne_opera-mgh-aa-6-2-lat_peiper1883.txt` l.30146-30149). By the index, then, 518 is not allowed.
  - 518 survives only on Peiper's prooemium. There Peiper credits the late homily date to Binding ("non ante 525 ex. vel 526 in. putat Bindingius", l.3377-3378), and himself puts the Geneva letters and homilies "intra annos 513 et 516" (l.3381). Without the homily, only "Anastasio (immo Iustino) adhuc principe" (l.30143) is left, and that means 518 or later.
  - The Avitus card already gives both bounds (`dates`; `uncertain` 0). So the README now disagrees with the profile it describes.
  - Fix: "Avitus of Vienne (no held source gives a year. Peiper's index puts his death after late 525 or early 526, by Binding's date for a homily at Geneva, and before 533, when Julian signs as bishop of Vienne at Orléans. Peiper's preface dates the Geneva pieces to 513 to 516, which leaves only his 'under Justin', from 518. The batch orders him by that 518, the Library header's year)".
  - The batch order can stand on the earliest year any held reading allows. The README should still say which reading that is. By the index's window, Avitus would sort after Boethius.

### 4. Each brief read whole

- **Eugippius.** The brief reads as one connected account: the grave scene, the house at the tomb, the book and how it began, the question of how well he knew Severinus, then Cassiodorus and Isidore, and Paschasius's close. The R1 fixes left no seams. The split opening reads better than the old run-on. "Paschasius answers…" is the one sentence that sits awkwardly, because "answers" appears to reply to the narrator (R2-C-M1). The removed honest limit is still on the card (`dates`, `uncertain` 2). There is no tail, no empty contrast and no process word. The prose has no British spellings.
- **Ciaran of Clonmacnois.** The brief opens on the stake and Tuathal's death. It places the Life and marks it as a saint's Life. It sets the two early witnesses against it, tells the childhood and the road to Clonmacnois, then the death and its two years, and closes on the namesake and the hymn. The new l.7 close keeps to the Life and ends on a fact, not a beat. The cut "and the brethren running out to meet him" costs nothing. The card's `uncertain` 1 still has the full Adomnán scene ("a canopy of poles"). There are no British spellings: "wright", "sovranty" and "Clonoensian" are inside quotes or are the source's own terms.

### Not findings

- **Ciaran l.3, "says… He says".** The split leaves two short sentences in a row that each report Stokes. The rhythm is a little flat but nothing is wrong. If wanted, "Whitley Stokes, its editor and translator, says the book was put together in the late 1400s, and the Life composed at Clonmacnois itself." gives 23 words, FK 6.8, Flesch 72.4. Optional.
- **"the deacon Justus" without a place (Ciaran brief l.5, card `uncertain` 1).** Justus is a common name; Justus of Rochester is in this era. But the two witnesses place him differently. The Lismore Life has "deacon Justus at Fidarta" (l.22141), which Stokes's Lismore index makes Fuerty (l.32776). Tirechan has "tenuit Fidard" (Tripartite l.3468), which Stokes's Tripartite index lists separately as "Fidard, 318; Fethard, in co. Tipperary, O'D." (l.25973). Adding either place would put one witness's place in the other's mouth. In both texts, "the deacon" together with Tirechan's Patrick context and the Irish setting identifies him. Leave as is.
- **The Comlach legend.** The Lismore Life names "the relics of Paul and Peter which Benian and Comlach left in the hollow tree here" (l.22866-22867). Stokes's Tripartite appendix prints from Rawl. B. 512 a tale that "Patrick foretold him (Ciaran) three score years before his birth" through Comlach (Tripartite l.17928, 17984-17998). The "three wrong stories" note is printed there too (l.17980-17982). No held file dates that manuscript against the Book of Lismore. So the card's "no earlier source used here", now limited to the Justus baptism, still holds, and so does records claim 8's "earlier held source".
- **"visit" for Aran and Inis Cathaig (Ciaran card `uncertain` 6).** The Life has him on Aran long enough to dry corn in the kiln (l.22552-22553). "Visit" is the R1 wording and is fair to "to commune with Enna" (l.22541) and "to bid farewell to Senán" (l.22563-22564). It makes no false claim.
- **"the island of Inis Angin" (Ciaran brief l.7).** "Inis" means island, but a listener needs the gloss. Not a doublet.
- **John of Beth Aphthonia's 538 in the README.** The header attaches the year to "John of Beth Aphthonia" as the author of the Life. Calling it "the header's year for the archimandrite" reads the header as the records do (a merging of the two men), and the year fits the archimandrite's death. Fair.

Totals for part C: both R1 blocking points (C-B1, C-B2) resolved. Of the 17 R1 minors, 14 resolved and 3 partly (C-M2, C-M13, C-M16, carried by R2-C-M1, R2-C-M3 and R2-C-M4). New: 0 blocking and 4 minor (R2-C-M1 to R2-C-M4: Eugippius 2, Ciaran 1, README 1).

