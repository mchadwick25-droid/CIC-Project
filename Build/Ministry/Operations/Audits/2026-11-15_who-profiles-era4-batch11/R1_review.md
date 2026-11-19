# Round 1 review: era 4 Who batch 11

Three fresh Opus agents that had not seen the drafting reviewed the batch at full effort on 2026-11-15, in three parts: Part A (Stepanos of Taron, Eulogius of Cordoba, Paulus Alvarus), Part B (Theodore Abu Qurrah, Stephen of Mar Saba, Ishoyahb III) and Part C (al-Tabari, Ibn Ishaq, and the README's general sections). Part A found 13 blocking and 27 minor points, Part B 1 and 18, Part C 9 and 30.

---

## Era 4 Who batch 11, round 1 review: PART A

**Scope.** `stepanos-of-taron`, `eulogius-of-cordoba`, `paulus-alvarus`: brief, card, `records.json` entry and `audio/<id>.audio.txt` for each, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`. I also cross-checked the Eulogius and Alvarus profiles against each other on every fact they share, and checked the README bullets for these three people, census release 44 included.

**Method.** I read CLAUDE.md, `Who_Profile_Pattern.md` (with the 14-item checklist), `lessons_review.md`, the batch 11 README, the batch 10 `peter-of-sicily` house form and Rescore rows l.133, l.134 and l.158. I reopened every cited range with `sed -n`. For the absence and "only" checks I searched all of `cic/texts` for name variants: asol[i1]k, asoghik, asolnik, acogh/Açogh'ig, Asolic, Taronetsi, Stephannos, Stepanos, eulog/evlog with cord/toled/alvar/leocrit/zoil, and alvar/albar. That turned up held Stepanos material the profile does not use: Chamich (Avdall 1827), Conybeare's Rituale (1905), Ormanian (1912), Brosset's Kartlis Tskhovreba (1849) and Chabot's Michael the Syrian (1901). I walked `census.json` for every spelling.

**Quotations.** None of the three briefs uses quotation marks. On the cards, Neumann's "the learned Asolnik" is verbatim (eghishe…neumann1830.txt l.798-799), and Stepanos's "of Taron" is a gloss. "Asolik" is a name form taken from Macler's French and placed in quotation marks (see R1-AM6). Every Latin and French record quote I spot-checked matches its file as the scan reads, inside its range. Records quote Macler, PL115, PL121, Mansi 14 and PL83 correctly.

**Audio.** All three audio files equal the brief, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. Final newlines are present.

**Scores.**

| id | words | minutes (162 wpm) | FK | Flesch |
|---|---|---|---|---|
| stepanos-of-taron | 325 | 2.01 (2:00) | 7.34 | 68.57 |
| eulogius-of-cordoba | 336 | 2.07 (2:04) | 6.83 | 69.77 |
| paulus-alvarus | 336 | 2.07 (2:04) | 7.82 | 63.78 |

All three are within the README's stated 324-338 range. None claims an exception. All pass `grade_text`.

## stepanos-of-taron

**Verdict:** revise (5 blocking, 11 minor).

**R1-AB1 (brief, para 5, "No early source gives his own death."): unsupported absence claim.** The sentence implies that Alishan's manuscript, told next, is late. Macler stresses that its age is unknown: Alishan "ne donne aucune notice sur ce manuscrit, sur son contenu, sur son âge probable" (stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt l.885-886). The held witnesses who say the death is unknown are Malkhasiants ("les dates de la naissance et de la mort d'Etienne de Tarôn sont inconnues", MAC l.764-765) and Brosset ("on ne sait pas qüand mourut l'auteur", zakaria…brosset1876.txt l.26019-26020).
Fix, brief and audio: "No early source gives his own death." → "Marie-Félicité Brosset, a French scholar of Armenia writing in 1876, says no one knows when he died." The README "Who the sources are" line has the same error (R1-AM-R3).

**R1-AB2 (card `dates` and `uncertain[3]` "His death"): a held placing of his death is missing.** Emin dates the death to between 1041 and 1045, at about 117 or 129: "Emin, se basant sur un passage de Grégoire Majistros, fait mourir Asohik entre 1041 et 1045" (MAC l.753-754). See also l.740-745: "on devra reconnaitre qu'il mourut âgé d'environ 1 17 où 129 ans". Malkhasiants rejects the longevity as "tout à fait invraisemblable" (l.762-764).
Fix: append to `dates`: "; J.-B. Emin, his Russian translator, had him die between 1041 and 1045, from a letter of Gregory Magistros, which Malkhasiants rejects as an impossible age". In `uncertain[3]`, before "Brosset, in 1876, …", add: "Emin, from a letter of Gregory Magistros, had him alive until 1041 to 1045 and dying at about 117 or 129; Malkhasiants found that age wholly unlikely, and Macler notes that Gregory wrote for years after, so the letter fixes nothing."
Records: add a claim for MAC l.740-745 and l.753-756 (Emin; Macler's answer), and add an Emin side, "between 1041 and 1045 (MAC l.753-754)", to the contested claim "His death".

**R1-AB3 (card `uncertain[5]` "His office", "says he was thought to be a married cantor"): a detail the scan does not establish.** The scan reads: "on croit nil était chantre et marie du Tarôn" (MAC l.791). "marie du Tarôn" is garbled. It does not parse as "married" ("marié du Tarôn" is not French), and "natif du Tarôn" reads more naturally. A married state is a family detail and must not rest on a garbled OCR word.
Fix: "and says he was thought to be a married cantor" → "and says he was thought to be a cantor from Taron (the scan is garbled at this word)". Records: add a claim quoting MAC l.789-791 with "(scan)", and note the reading in `absent_details` ("Family").

**R1-AB4 (card `legacy/traces[2]` "Later writers on Armenia and Georgia cite him again and again for dates, among them Brosset and the editor of Michael the Syrian's Chronicle."): partly unsupported, and its sources are not on the card.** Brosset does cite "Asolic" again and again in kartlis-tskhovreba_histoire-de-la-georgie-pt1-histoire-ancienne-fra_brosset1849.txt (for example l.12038-12040, l.13891, l.13907). Neither that file nor Chabot's is in `sources`. Chabot cites him twice, on the synod of Manazkert and a place name, not for dates: "Sur ce concile, cf. le récit d'Etienne Asolik" (michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt l.38282; l.38325). The trace also has no records claim.
Fix: "Later writers on Armenia and Georgia cite him again and again for dates, among them Brosset and the editor of Michael the Syrian's Chronicle." → "Marie-Félicité Brosset, in his French History of Georgia (1849), cites him again and again for dates and events. Jean-Baptiste Chabot, the editor of Michael the Syrian's Chronicle, points to his account of the synod of Manazkert." Add both files to `sources.about`, and add records claims for Kartlis l.12038-12040 and l.13891, and for Chabot l.38282.

**R1-AB5 (records `stepanos-of-taron`): card facts with no claim.** These have no claim: `legacy/traces[0]` (the nine manuscripts, MAC l.222-234; the editions of 1859 and 1885, l.370-378), `traces[1]` (the translations, l.383-398), `uncertain[4]` (the tomb at Mush, l.906-913, which is only an `absent_details` note), `uncertain[5]` (Zarbhanalean, l.768-776; Alishan, l.786-791), `uncertain[6]` (Brosset's insertions, ZAK l.26017-26018) and `place` (Derjan in Upper Armenia, MAC l.3971-3972 and note l.4000).
Fix: add one claim per item, quoting the lines given.

**R1-AM1 (brief, para 4, "as a young man"; card `uncertain[2]`): the second translation is left out.** Macler has "Dans notre jeunesse" (MAC l.4302), and Gelzer has "in unserer Kindheit" (stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt l.6486-6487), which means childhood. The record notes this and the brief does not.
Fix, brief and audio: "He writes that as a young man he saw" → "He writes that in his youth he saw". That covers both translations.

**R1-AM2 (brief, para 1, "In Lent they drank cold water only on Saturday and Sunday."): the adjective goes past both translations.** Macler has "l'usage de l'eau fraîche … que le samedi et le dimanche" (MAC l.3992-3994), and Gelzer has "nur mit einem Trunke Wasser" (GEL l.6362-6363). Fix: "drank cold water" → "drank water".

**R1-AM3 (brief: four sentences past about 25 words).** Splits:
- Para 4: "He writes that as a young man he saw … tasted the sweet food of their words." (31 words) → "He writes that in his youth he saw some of the great teachers in their old age. Among them was Anania of Narek, and he tasted the sweet food of their words."
- Para 6: "At the end of the History, Stepanos asks … to sing the Trinity's praise." (29 words) → "At the end of the History, Stepanos asks his readers to remember him in their prayers. Then he too might be found worthy to sing the Trinity's praise."
- Para 5: "A manuscript in the Mekhitarist library … died when the Persians took Kars." (26 words) → "Ghevond Alishan, a Mekhitarist scholar, reported a manuscript in his order's library at Venice. It says the father of the monastery, Stephen, also Asoghik, died when the Persians took Kars." (This also meets R1-AM5.)
- Para 1 (25 words) can stay.

**R1-AM4 (brief, para 3, "than to fill it with bold guesses"): "it" has no clear referent when heard aloud.** Macler: "rester dans cette quasi ignorance, plutôt que de chercher à y remédier par des hypothèses aventureuses" (MAC l.687-690). Fix: "to fill it with bold guesses" → "to fill the gaps with bold guesses", which matches the card.

**R1-AM5 (brief and card: witnesses not introduced).** In the brief, "reported by Alishan" gives no role. Alishan's own file names him "Father Ghewond (Léon) M. Alishan, of the Mekhitarist Congregation of San Lazzaro, Venice" (alishan_leon-le-magnifique…1888.txt l.2). On the card, `uncertain[5]` has "a modern notice" where Pattern item 5 wants the real witness named. Macler names him as "Garegin Zarbhanalean, dans son Histoire de la littérature arménienne ancienne (Venise, 1897)" (MAC l.768-776).
Fix: the brief as in R1-AM3. In the card, "That he studied at Ani and was ordained a priest is a modern notice, which Macler says" → "Garegin Zarbhanalean, in a history of Armenian literature (1897), says he studied at Ani and was ordained a priest; Macler says that". In `dates`, "Marie-Félicité Brosset said" → "the French scholar Marie-Félicité Brosset said".

**R1-AM6 (card `legacy/remembered[1]`): a corrected year with no scan note, and a French word in quotation marks.** The card has "who wrote until 1058, Macler says". The scan reads "le même Grégoire a écrit jusqu' en 1097" (MAC l.754-755), and the records note "(scan 1097)". Choosing 1058 is a correction the file does not show. Separately, "Asolik" is quoted from a French source.
Fix: "Gregory Magistros, an Armenian scholar who wrote until 1058, Macler says, asks in a letter for a commentary on Jeremiah by \"Asolik\", whom he calls a very old man (Macler's French)." → "Gregory Magistros, an Armenian scholar whose letter Emin placed between 1041 and 1057, asks for a commentary on Jeremiah by Asolik, whom he calls a very old man (Macler's French)." This rests on MAC l.711-712. Records: cite l.711-712 for it.

**R1-AM7 (card `knownFor`, "finished in 1004 or 1005"): one side of a dating the card itself treats as uncertain.** `uncertain[6]` gives a reading that runs to 1023-1024 (MAC l.844-848). Fix: "finished in 1004 or 1005" → "whose closing note dates it to 1004 or 1005".

**R1-AM8 (card `uncertain[6]` "When the History ends"): two held placings are missing.** Chamich (Avdall's English) has "who by order of the pontiff wrote a history of Armenia from its origin to the year of our Lord 1000" (chamich_history-of-armenia-v2_avdall1827.txt l.5200-5203). Conybeare has "who wrote between A.D. 991 and 19190 [scan]" (rituale-armenorum-lectionary_conybeare1905.txt l.2580), which Macler quotes as 991 to 1019 (MAC l.799-801).
Fix: append "Michael Chamich's History of Armenia, in Avdall's English of 1827, has it run to the year 1000. F. C. Conybeare placed the writing between 991 and 1019." Add both files to `sources.about`, with records claims.

**R1-AM9 (card `keyWorks[0].about`, "from its restoration in about 887"): "restoration" is not in the source.** Macler: "du début de la dynastie bagratide" (MAC l.439-441). Fix: "from its restoration in about 887" → "from the start of the Bagratid dynasty in about 887".

**R1-AM10 (card `place`, "His church served the Bagratid kings at Ani"): a statement with no clear meaning or source.** The held line is Macler's note that Sargis "transféra le siège catholical à Ani en la même année" (MAC l.15212-15214). Fix: "His church served the Bagratid kings at Ani" → "Ani, the Bagratid capital, where the catholicos Sargis moved his see in 992, Macler notes".

**R1-AM11 (brief, para 3, "The name Taronetsi says he came from Taron."): an inference with no named owner.** It is Emin's reading as Macler reports it: "surnommé Tarônetsi, parce qu'il était originaire du Tarôn" (MAC l.698-700). Fix: → "Emin, his Russian translator, took the name Taronetsi to mean he came from Taron, a district of Armenia."

## eulogius-of-cordoba

**Verdict:** revise (4 blocking, 6 minor).

**R1-AB6 (card `uncertain[5]` "His brothers"): a disputed identity told as settled.** The card says "This Alvarus is a different man from his friend Paulus Alvarus", and then that Tamayo "confused" the two. "Confused" is Antonio's verdict. Tamayo held the other side: in his elogium he called Alvarus, "ut quidam credunt, sancti Eulogii fratrem", and in his notes "hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre" (paulus-alvarus…pl121…txt l.31687-31691). He also held "non carnis nexu, sed contubernii vinculo" (l.31703-31706). The card also carries an "X, not Y" sentence.
Fix: replace "This Alvarus is a different man from his friend Paulus Alvarus. Juan Tamayo said the two brothers were brothers in a shared life, not by blood, and confused this Alvarus with Paulus Alvarus. Nicolás Antonio, in the notice on Paulus Alvarus, argues they were blood brothers." with "Juan Tamayo, a Spanish martyrologist, took this Alvarus to be his friend Paulus Alvarus and said the brothers were bound by a shared life rather than by blood. Nicolás Antonio, in his notice on Paulus Alvarus, holds that they were blood brothers and that this Alvarus was another man."
Records: add a contested claim "Was Eulogius's brother Alvarus the same man as Paulus Alvarus", with the sides "Tamayo: one man (ALV l.31687-31691)" and "Antonio: two men (ALV l.31706-31716)". The same fix applies to the Alvarus card (R1-AB12).

**R1-AB7 (card `legacy/traces[2]`): a held editor's dissent is missing.** The card tells Morales's view that "whoever added these martyrs to Usuard's martyrology" drew on Eulogius. Morales's premise is that Usuard wrote for Charlemagne and could hardly have outlived Eulogius (eulogius-cordoba…pl115…txt l.58870-58873). The edition's note answers him: "Labitur Morales … eum vixisse sub Carolo cognomento Calvo, atque huic opus suum nuncupavisse circa annum 875, proindeque sexdecim annis post obitum Eulogii" (l.58905-58911).
Fix: after "took the Cordoban martyrs from Eulogius's books." add "A note in Lorenzana's edition says Morales was wrong about Usuard, who dedicated his martyrology to Charles the Bald in about 875, sixteen years after Eulogius died." Records: add a claim for l.58905-58911, and a contested claim on whether Usuard himself entered the martyrs.

**R1-AB8 (card `legacy/traces[1]`): a date misattributed to its witness.** The card has "A note in Lorenzana's edition, citing a chronicle written in 883, says Dulcidius brought the bodies … on 9 January 884." The chronicle, written in November 883, says only that Dulcidius was sent in September and had not come back: "unde adhucusque non est reversus Novembrio discurrente. Sic auctor, qui hoc scribebat mense anni 883." The entry into Oviedo comes from the note's own "Postea": "Postea Dulcidius … Ovetum cum eis intravit die nona Januarii anni 884" (l.58993-58998). The Oviedo lessons are a separate witness (l.58967-58975).
Fix: → "A chronicle written in 883 says King Alfonso sent Dulcidius as his envoy to Cordoba that September. A note in Lorenzana's edition adds that Dulcidius brought the bodies of Eulogius and Leocritia to Oviedo on 9 January 884." Records: split the Oviedo claim so the chronicle and the note each have their own line.

**R1-AB9 (records: confidence tags).** Seven claims that rest on Alvarus's Life alone are tagged "Widely Accepted": the palace scene (l.57655-57703), birth and orders (l.56818-56822, l.56896-56900), Reccafred's jailing (l.56979-56985), the release (l.56996-57001), Leocritia (l.57422-57545), the answer to the judge (l.57596-57603), the burial (l.57689-57722) and the election (l.57314-57326). One friend's hagiography is a single witness, not Widely Accepted. The dossier itself says "Widely Accepted (one friend's witness)".
Fix: retag each as "Documented" (Alvarus's own account), keeping the claim "For most of his life Alvarus is the only witness".

**R1-AM12 (brief, para 1: the first mention has no identifier).** The brief opens on "Eulogius", and "Eulogius of Cordoba" first appears in para 2. Eulogius of Alexandria is a namesake in the census (`movements[552]`). Fix: "a counselor who knew Eulogius well" → "a counselor who knew Eulogius of Cordoba well". In para 2, "Eulogius of Cordoba was a priest" → "Eulogius was a priest". Mirror in audio.

**R1-AM13 (brief, para 3, and card `keyWorks[0]`): "the city" turning against the martyrs hides who turned.** Eulogius means the Christians themselves, who first honored the martyrs: "cepere omnes, tam clerici quam laici … extollere" … then "omnes exterriti … sententias mutant, detrahunt, maledicunt; … paucis admodum … sequestratis" (l.59172-59187). Heard aloud, "the whole city" includes the Muslims.
Fix, brief and audio: "nearly the whole city turned against them for fear of the emir" → "nearly all the city's Christians, clergy and laity, turned against them for fear of the emir". Card: "when most of the city turned against the martyrs" → "when most of the city's Christians turned against the martyrs".

**R1-AM14 (card `otherNames[0]`, "the Latin form in his friend Paulus Alvarus's Life"): not in the Life.** In the Life range (l.56723-57900) "Cordubensis" is Alvarus's own name ("AUCTORE ALVARO CORDUBENSI", l.56738). "Eulogius Cordubensis" appears in later notes (l.75577) and the Toledo list (isidore-seville…pl83…txt l.123287, l.123289). Fix: → "Eulogius Cordubensis, the Latin form in later notes and in the list of Toledo's early bishops".

**R1-AM15 (card `keyWorks[2].about`): two misreadings.**
- "The editors note that he wrote it again against Christians" misreads "iterum adversus eos hoc opere insurgit, tanquam non satis haberet in primo libro contra hos valide pugnasse" (l.68577-68580). He argues again; he did not write the book again. Fix: → "The editors note that in it he argues again against Christians who still spoke against the martyrs."
- "It survives in one badly corrupted copy" goes past "Erat autem misere corruptum exemplar" (l.68582), the editors' exemplar. Fix: → "The editors' copy was badly corrupted."

**R1-AM16 (card `uncertain[1]`, "so he fixed both himself by astronomical reckoning"): the method is stretched to cover the ruler's name.** Morales fixed the era and the year by reckoning ("utrumque recte signavimus", l.56699-56706). He corrected the ruler from Eulogius's Book III and Alvarus: "quod ex ejusdem libro tertio constat … et Alvarus etiam ipsum regem Mahomad nominat" (l.56706-56711).
Fix: → "so he fixed the era and the year by astronomical reckoning, and corrected the ruler to Muhammad from Eulogius's own third book and from Alvarus."

**R1-AM17 (card: witnesses not introduced).** "Juan Tamayo" is covered by R1-AB6. In `uncertain[3]`, "citing Enrique Flórez" → "citing Enrique Flórez's España Sagrada", which rests on "Hisp. Sacr." at l.58342 and l.58347. "Dulcidius" is covered by R1-AB8.

## paulus-alvarus

**Verdict:** revise (4 blocking, 5 minor).

**R1-AB10 (brief, para 3, and card `uncertain[1]`, "Alvarus quotes Virgil on the fearless Getae"): contradicted by a held note.** Alvarus writes "Virgilium audi" (paulus-alvarus…pl121…txt l.30933). The edition's note says "Falso tribuuntur hi versus Virgilio" (l.31057), and the note at the letter itself says "False tribuuntur hi versus Virgilio" (l.40470).
Fix, brief and audio: "In another, Alvarus quotes Virgil on the fearless Getae." → "In another, Alvarus quotes lines on the fearless Getae, which he wrongly gives to Virgil." Card: "In another letter Alvarus quotes Virgil on the fearless Getae" → "In another letter Alvarus quotes lines on the fearless Getae, which he gives to Virgil; a note in the edition says they are not Virgil's". Records: add the note to the Goth claim (l.31057, l.40470).

**R1-AB11 (card `uncertain[4]` and `legacy/remembered[2]`): words given to Antonio that belong to a later note.** The other attributions of the Book of Sparks (to Bede, Defensor and Cassiodorus) and the Escorial marginal "ALVARUS" with "quae forsan ex Alvaro nostro descendit" sit in note (c) to the notice (l.31631-31656). That note cites "Florezium tom. XI. pag. 47" (l.31615), which is later than Antonio's own text. Antonio's main text gives only the Sahagún codex (l.31544-31550).
Fix: `uncertain[4]`, "Other manuscripts give it to Bede, to Defensor or to Cassiodorus, Antonio reports." → "A note to Antonio's notice reports other manuscripts that give it to Bede, to Defensor or to Cassiodorus." `remembered[2]`, "Antonio reports it and thinks it may come from him." → "A note to Antonio's notice reports it and thinks it may come from him." Records: name the note as witness in both claims.

**R1-AB12 (card `uncertain[7]` "Eulogius's brother"): a disputed identity told as settled.** This is the same issue as R1-AB6. "This Alvarus is another man. Juan Tamayo confused him with Paulus Alvarus" gives Antonio's verdict as fact (ALV l.31687-31716).
Fix: → "Eulogius writes of his brothers Alvarus and Isidore, exiled in the lands of Louis, king of Bavaria. Juan Tamayo took this Alvarus to be Paulus Alvarus, and called the brothers bound by a shared life rather than by blood. Nicolás Antonio holds that this Alvarus was another man, Eulogius's brother by birth, and that Paulus's bond with Eulogius was friendship." Records: the same added contested claim.

**R1-AB13 (records: confidence tags).** "Burial" rests on Alvarus alone and is tagged "Widely Accepted"; it should be "Documented". The "Authorship" claim (Morales first against, then for, with Antonio for, and Higuera's chronicles for Bonitus or Wistremir, ALV l.31102-31130) is tagged "Widely Accepted", while the profile's own contested claim "Author of the Indiculus luminosus" sets out three sides. Fix: retag it "Contested".

**R1-AM18 (brief, para 1, "the house of his teacher Alvarus"): no identifier at first mention, and a courtesy title stated as fact.** Eulogius's brother Alvarus is a namesake. Morales calls the title "teacher" humility, since the two were fellow students: "Quod idem praeceptorem suum etiam vocat, humilitatis est prorsus: cum fuerint … condiscipuli" (eulogius…pl115…txt l.56714-56716).
Fix, brief and audio: → "Eulogius of Cordoba once went to the house of Paulus Alvarus, whom he calls his teacher."

**R1-AM19 (card `legacy/traces[0]`): "One codex" and "lies behind the printed text" go past the source.** Antonio also names a second codex: "Codicem alium Toletanae Ecclesiae Thomas Tamaius laudat" (ALV l.31019-31020). What came from Tamayo's copy, by way of the Barberini library, is Antonio's own transcript, "Nos inde … habemus exemplum" (l.31029-31036), and nothing about a printed text.
Fix: → "A codex of the church of Cordoba, in Gothic script, kept his works, and Morales saw it; Thomas Tamayo de Vargas praised another at Toledo. Antonio's own copy came from one Tamayo gave to Cardinal Barberini's library in Rome."

**R1-AM20 (card `uncertain[6]`, "No source here says more of who he was."): drafting-process language on reader-facing text.** Fix: → "The sources say no more of who he was."

**R1-AM21 (card `dates` and `uncertain[5]`, "about 861"): a scan reading given without a mark.** The scan reads "ad annum Christ $61" (ALV l.31661-31662). Fix: "cites Enrique Flórez for about 861" → "cites Enrique Flórez, author of the España Sagrada, for about 861 (the scan reads $61)". In `uncertain[5]`, after "about 861", add "(the scan reads $61)".

**R1-AM22 (card `dates`, first mention of "Enrique Flórez" with no role).** Covered by the R1-AM21 fix.

**Eulogius and Alvarus: shared facts.** They agree on every shared fact:
- the death: Saturday, 11 March, 859 by Morales's reckoning;
- the friendship from boyhood under Speraindeo;
- the Life written for the yearly feast;
- the burial by the Christians at St Zoilus, and that Alvarus does not say he buried Eulogius;
- the election to Toledo, with Alvarus as the one witness;
- the hymn and epitaph in Antonio's list;
- Morales's edition and Schott's reprint;
- Morales's "Serenity" argument for noble birth, against Antonio's answer;
- the brothers Alvarus and Isidore.

The two cards agree with each other on the brothers. Both tell Antonio's side as settled (R1-AB6, R1-AB12). The README's statement that they disagree is stale (R1-AM-R2).

## README

**R1-AM-R1 (README l.35, l.39, l.40, and the Ishoyahb census bullet: dangling cross-references).** "(C1)", "(C4)", "(C6)" and "(C7)" point to no section in the README. Fix: replace each with a plain pointer to the entry it means, or remove it.

**R1-AM-R2 (README l.35, "The two batch 11 cards, Eulogius and Alvarus, disagree on the brothers; see (C4)."): stale.** The cards now carry the same account (see above). Fix: → "The two batch 11 cards, Eulogius and Alvarus, agree on the brothers."

**R1-AM-R3 (README "Who the sources are", Stepanos, "Death and burial rest on a late manuscript notice and a tradition."): "late" is unsupported.** Macler says the manuscript's age is unknown (MAC l.885-886). Fix: "a late manuscript notice" → "a manuscript notice of unknown age".

**R1-AM-R4 (README census, Stepanos: an unlisted namesake hit).** The pattern "taron" also hits `movements[116]/documentedStories[0]/sources[0]/work`, "recorded by the physician Taronites", which is another man. The bullet ends "No other passage." Fix: add "`movements[116]` (the physician Taronites) is a namesake, set aside."

**R1-AM-R5 (README census, Eulogius, "`voices[0]` agrees"): inconsistent with the bullet's own standard.** `movements[72]/voices[0]` reads "executed in 859". That is the same flat statement of Morales's year that the bullet flags in `why` and `longDescription`. Fix: "`voices[0]` agrees" → "`voices[0]`, 'executed in 859', states Morales's year flat, as `why` does".

Every other census claim for these three checks against census.json, release 44: every "eulog", "alvar", "asog", "asol", "taron", "stepan", "Stephen of T" and "Étienne" hit is listed or is a namesake, Euloge, Eulogia or eulogy, Francisco Alvares, or Calvary. The "agrees" and "differs" verdicts I spot-checked against MAC l.4639-4650 and l.4657-4658 and EUL l.56979-57001 hold. The Rescore corrections for l.133, l.134 and l.158 are right.

**Verdict.** Blocking 13: Stepanos 5, Eulogius 4, Alvarus 4. Minor 27: Stepanos 11, Eulogius 6, Alvarus 5, README 5. All three profiles need a revision round.

---

## Era 4 Who batch 11, round 1 review: PART B

**Scope.** `theodore-abu-qurrah`, `stephen-of-mar-saba`, `ishoyahb-iii`: brief, card, `batch11/records.json` entry, `audio/<id>.audio.txt`, and the README bullets for the three. Also: the coordinator's call to drop "Mansur" and name him Stephen of Mar Saba, and Ishoyahb III checked against `era4/batch5/thomas-of-marga.*`. No repo file was edited.

**Method.** I read CLAUDE.md, the Pattern and its checklist, the lessons file, the batch11 README, and the house form (batch10 peter-of-sicily). I reopened every cited range with `sed -n` in cic/texts: Graf 1910, PG97, PG94, Peeters, AASS Martii III (Acts, commentary, margins, index, Greek appendix), Nikodemos, Papadopoulos-Kerameus t.4, Thomas of Marga (Budge), Duval, Mingana, Amr/Sliba (Gismondi), Mari, Elias, Bar Hebraeus/Lamy, Seert II, Guidi, Assemani III.1 and III.2, Sachau, Labourt, Jugie. Absence checks run across all of cic/texts:
- Abucara, Abu Qurra, Abukar and Pygl/Puggal: new hits only in index lines (Bessarion, Calecas and Cotelier indexes, Cabasilas), none of which conflicts.
- Mansur, Μανσ and Stephan... Mansur: no hit for this man.
- Stephanus Sabaita and its variants: AASS only. Papadopoulos-Kerameus t.4 l.12941 is a namesake Stephen, John of Damascus's nephew, in a Life of Kosmas.

I walked census.json for every spelling (qurr, Abucara, Harran; Mar Saba, Sabait, Mansur, 796 and 797, Twenty; Isho'yahb variants, Jesujab, Sahdona, Kuphlana, Beth Abe and Beth 'Abhe, Rev-Ardashir, Maremmeh).

**Quotations.** Briefs: Ishoyahb only. "having many eaglets upon his back" is verbatim at TOM l.6757-6758, inside l.6755-6761. "this country has since sat in darkness" is verbatim at MING l.1566, inside l.1553-1567. Theodore and Stephen quote nothing; all their Latin and German is told in modern words, correctly. Cards: Ishoyahb's "the blessed in everything" is verbatim (TOM l.10245). One card quotation is not held English: "of Hazza" (R1-BM9). The records strings I checked match their files at the cited lines. The Newman quotation (NPNF l.42151-42152) is verbatim.

**Audio.** All three audio files equal the brief with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. All files end with a newline, and the JSON parses.

**Scores.**

| id | words | minutes (~162 wpm) | FK | Flesch |
|---|---|---|---|---|
| theodore-abu-qurrah | 332 | 2:03 | 8.07 | 62.4 |
| stephen-of-mar-saba | 324 | 2:00 | 6.21 | 75.4 |
| ishoyahb-iii | 338 | 2:05 | 7.16 | 65.5 |

All three are within the 2:00 rule, and no exception is claimed. FK is at or above the grade 8 floor only for Theodore. Stephen and Ishoyahb sit lower on a story-led text, which is not a breach.

**Card structure.** All three cards keep the Pattern's field order and omit absent fields. Each `uncertain` opens with the brief's caveat. Every source named is listed and every listed source is used. All files exist.

## theodore-abu-qurrah

**Verdict:** one blocking, five minor.

**R1-BB1 (brief para 7: an inference told as fact).** "He wrote it for a bishop, Janah." The text gives only "Anba Janah" (GRAF l.14079-14080), and Graf says the "anbā" is probably a copyist's (GRAF l.14097-14104). The bishop is Graf's inference from the praise: "Bischof war letzterer jedenfalls, da Abu Qurra ihn lobt wegen seiner großen Fürsorge für die Christen und die Rechtgläubigkeit" (GRAF l.14112-14114). Graf also leaves open whether Janah is the bishop of Tela: "Ob dieser Mann der Adressat des vorliegenden Schreibens ist, bleibt eine offene Frage" (l.14111-14112). The card already hedges ("whom Graf takes to be a bishop"), so the brief and card disagree.
- Brief and audio: "He wrote it for a bishop, Janah." → "He wrote it for Janah, whom Graf takes to be a bishop."
- Records: no change. The claim at l.14061-14130 already carries "Graf: 'Bischof war letzterer jedenfalls'".
- Length after the fix: 336 words, inside the README's stated 324 to 338.

**R1-BM1 (brief para 4: a hostile witness's label in the narrator's voice, and a pronoun).** "He calls Theodore the philosopher, and a secret follower of the false teacher Nestorius." Aloud, "He" follows "the deacon Elian", so it can be heard as Elian. "the false teacher" can be heard as the narrator's own label, but it is Abu Ra'ita's: "der Lügner und Irrlehrer Nestorius" (GRAF l.876).
- Fix: → "Abu Ra'ita calls Theodore the philosopher, and a secret follower of Nestorius, whom he calls a false teacher."
- Audio: the same fix. Records: no change.

**R1-BM2 (brief para 6: pronoun).** "Michael says the young archdeacon Nonnus of Nisibis beat him in debate." "him" sits closest to Michael.
- Fix: → "beat Theodore in debate".
- Audio: the same fix.

**R1-BM3 (brief para 6: a loose "only").** "We have his account only in Graf's German." This states a general limit. Michael's Book XII survives, and Graf cites Chabot's edition for it: "Vgl. J. B. Chabot. Tome III. fasc. 1. p. 495" (GRAF l.908). What is true is that the Library lacks it; the card already says so ("Michael's own text of it is not among the sources").
- Fix: → "Graf gives his account in German."
- Audio: the same fix.

**R1-BM4 (card `dates`: a loose "no").** "No source gives a date for his birth, his consecration or his death" contradicts the same field. Peeters gives "ante annum 820 videtur obiisse" (scan 520, PEETERS l.867-868), and Graf has "ungefähr ... 740 und 820" (GRAF l.1157-1158).
- Fix: → "No source gives an exact year for his birth or his death, or any year for his consecration".
- Records `absent_details` already say this.

**R1-BM5 (records `contested_claims` "Same man as Theodore of Caria": a held witness on the other side).** The "No" side lists Turrianus. Le Quien reports the opposite: "Hic porro Theodorus perperam Turriano accipitur pro Theodoro illo Cari in Thracia, vel Asia minori, episcopo" (PG94 l.116610-116611). The Mai notice instead holds to Turrianus against Gretser: "ut a sententia nos Turriani retrahant" (PG97 l.122125).
- Records fix: remove "Turrianus" from the "No" side and add a third side: "Turrianus, reported both ways: Le Quien says he took the two for one man (PG94 l.116610-116611); the Mai notice follows him in keeping them apart (PG97 l.122124-122125)".
- Card: no change. `uncertain[2]` does not name Turrianus.

Checked and sound:
- The David scene and its heading (GRAF l.12025-12061).
- "Most" Arabic headings Harran ("mit Ausnahme von III und X", l.666-668).
- Graf a parish priest (l.86) and "soweit bis jetzt bekannt" (l.743-745).
- Edessa as "Vaterstadt" (l.505-511) and Mar Saba (l.737-743).
- Abu Ra'ita's captivity, Elian and the threefold reading (l.799-844).
- The Greek heading of opusc. IV as Graf renders it (l.607-617) and 811 to 813 (l.660-664).
- Michael "gest. 1199", partisan, and the defeat rejected (l.904-909, l.991-997, l.1055-1063).
- The mirror prayer (l.16946-16958).
- Peeters, Fabricius, Gallandi and the Migne 770 (PEETERS l.867-868; PG97 l.121459, l.121548-121554).
- Fabricius's two notices on John's death (PG97 l.121547-121548; PG94 l.617).
- Grotius 1617 (GROTIUS l.1, l.364, l.12316). Euthymius of Tyre and Sidon, 1720 (GRAF l.4103-4115; "as-Saifä" in the scan, l.439).

## stephen-of-mar-saba

**Verdict:** pass, three minor. The name call is right (below).

**Name check (the coordinator's call).** Dropping "Mansur" is right.
- No line in cic/texts gives this man the name. AASS has only "mansurus/mansura". Every other "Mansur" in the Library is John of Damascus's family name, another man or a place. The census's "Stephen Mansur" rests on no held line.
- The relative of John of Damascus whom the census merges with him is, by the Bollandists, a different man who died before the raid. They write "alterius similiter Sabaitae Stephani, quem Thaumaturgum et S. Joannis Damasceni Nepotem dictum videbimus" and "prius ille e vivis excesserat, quam haec tempestas in Lauram incurreret" (AASS l.50429-50444). Their index keeps two entries (l.241961-241965).
- "Stephen of Mar Saba" renders the Bollandists' own heading, "Auctore Stephano Monacho Sabaita" (l.50496), so it is the record's form.
- One caution, not a finding: the Wonderworker is equally "a Sabaite" ("similiter Sabaitae"). What sets this man apart in the record is the Typikon's "Poetae titulo" (l.50438). The card carries "Stephen the Poet" and the brief names the Wonderworker apart, so listeners can tell them apart. If Mark wants the display name itself to tell them apart, "Stephen the Poet, of Mar Saba" is the held option.

**R1-BM6 (brief para 4, card `dates`, `uncertain` "The year", records: which event the margin's 797 belongs to).** "a note in their margin says 797". The margin reads "Poeta statim post rem gestam, scilicet post Pascha anni 797" (AASS l.50376-50387). It sits beside §5's "Statim autem scripsisse opinamur post barbarorum discessum" (l.50438-50441), so it dates the writing. It puts the raid in 797 only by implication, as Holy Week just before that Easter. The card's own "When he wrote" item reads it that way, so the year item and the brief disagree with it.
- Brief and audio: "and a note in their margin says 797." → "and a note in their margin has him writing just after Easter of 797."
- Card `dates`: "make it 796 in their text and 797 in their margin." → "make it 796 in their text, while their margin has him writing just after Easter of 797."
- Card `uncertain` "The year": "make it 796 in their text and 797 in their margin." → "make it 796 in their text, while their margin has him writing just after Easter of 797, which puts the raid that spring."
- Records: the claim "Bollandists' margin" → add "(the margin dates the writing; it implies the raid in 797)". In `contested_claims` "The year of the raid", side 3 → "The Bollandists' margin: Stephen wrote just after Easter of 797, which puts the raid in 797 (AASS l.50376-50387)".

**R1-BM7 (brief para 4: hagiography not marked).** The brief never says the account was written for the church's worship. The prologue says such writings are made "quos in ecclesia sacrisque conventibus necesse sit recitari" (AASS l.50513-50514). The Bollandists add the canons Stephen wrote for the feast (l.50414-50417).
- Brief and audio: "Stephen wrote at the order of his abbot, Basil, so that the courage of these men would not fade with time." → "Stephen wrote at the order of his abbot, Basil, for reading in church, so that the courage of these men would not fade with time." (+3 words, 327.)
- Records: add the claim "Written for reading in church: 'quos in ecclesia sacrisque conventibus necesse sit recitari'", witness "AASS l.50513-50514", Documented.

**R1-BM8 (card `uncertain` "Who the raiders were": a held placing missing).** Graf, already on the card, calls the killers Bedouin: "Dem im März 796 oder 797 durch Beduinen angerichteten Blutbad" (GRAF l.645-646).
- Card: add at the end of the item: "Georg Graf calls them Bedouin."
- Records: add to `contested_claims` "Who the killers were", side 2: "Graf: Bedouin (GRAF l.645-646)".

Checked and sound:
- The opening scene: money demanded, no bread, quivers emptied, about thirty wounded, doors smashed, arrows drawn, "nihilo levius ... transfixa ... pectora" (AASS l.51229-51257).
- Eyewitness (l.50539-50542). The abbot's order and its purpose (l.50524-50545).
- No name in the Acts: a grep of l.50496-53500 and the Greek l.229100-231600 finds "Stephan" only in the Bollandists' heading and notes.
- AM 6288 and AD 788, indiction 5, Elias and Basil (l.50556-50624). The 796 by the Bollandists' count (l.50452-50455).
- Sergius's flight, capture, beheading and hearsay (l.51696-51757). Patricius and the seven (l.51893-51907).
- Eighteen in the smoke (l.52205-52215). The nineteenth, Sergius (l.52338-52345). The twentieth, the hand (l.52740-52753).
- The Sinai and Raithou comparison (l.52683-52690). The closing prayer (l.53326-53328). The Christopher note, 789 (l.53418-53480).
- Nikodemos (NIK l.5248-5274).

## ishoyahb-iii

**Verdict:** pass, seven minor.

**R1-BM9 (card `otherNames[3]`: own English in quotation marks, and a misattribution).** "Jesujabus hazzensis, \"of Hazza\", the region Amr ibn Matta says is now called Arbela, in the Latin of Amr and of Mari ibn Sulayman". There are two problems.
- "of Hazza" is not held English, so it cannot carry quotation marks.
- "nunc notae nomine Arbela" is in square brackets (AMR l.13284). Gismondi says he printed Sliba's text with "quae ei prae Amro propria sunt uncinis inclusa" (AMR l.6398-6400), so the gloss is Sliba ibn Yuhanna's, not Amr's.

Fixes:
- Card: → "Jesujabus hazzensis, that is, of Hazza, in the Latin of Amr ibn Matta and of Mari ibn Sulayman; Sliba ibn Yuhanna's text adds that Hazza is now called Arbela".
- Records: in the "Places" claim, add "Gismondi: bracketed words are Sliba's own (AMR l.6398-6400)".

**R1-BM10 (brief para 2: pronoun).** "Parts, he says, came down by the monastery's own tradition." The nearest man is "E. A. Wallis Budge". The words are Thomas's (TOM l.5688-5690, l.5750-5751).
- Fix: → "Parts of it, Thomas says, came down by the monastery's own tradition."
- Audio: the same fix.

**R1-BM11 (brief para 7: pronoun).** "He blamed Simeon of Rev-Ardashir". The paragraph never names Ishoyahb, and "He" follows "the new Arab rulers".
- Fix: → "In it, Ishoyahb blamed Simeon of Rev-Ardashir". The same letter carries both passages (DUV l.8715-8719, l.8740-8747; MING l.1553-1567).
- Audio: the same fix.

**R1-BM12 (card `uncertain` "Who sent the mission": a held witness on the Boran side missing).** Duval, on the card, also names Boran: "quem regina Persarum Boran, ad Heraclium imperatorem, legatum de pace componenda mittebat" (DUV l.108-111).
- Card: "Budge, who translated Thomas in 1893, and Addai Scher, who translated Seert in 1919, both side with Boran." → "Budge, who translated Thomas in 1893, Rubens Duval and Addai Scher, who translated Seert in 1919, all side with Boran."
- Records: in `contested_claims` "Who sent the mission", side 2, add "Duval (DUV l.108-111)".

**R1-BM13 (card `uncertain[0]`: the dates of Thomas's book, against the Thomas of Marga profile).** The card gives Budge "about 840" and Labourt "between 832 and 850" (LABOURT l.17234-17235). The batch5 Thomas profile also gives Assemani's placing, "nono saeculo ineunte claruit" (ASSEMANI3-1 l.78622-78626).
- Card: "...or between 832 and 850 by Jérôme Labourt, about two centuries after him," → "...or between 832 and 850 by Jérôme Labourt, while J. S. Assemani has him flourish early in the ninth century, about two centuries after Ishoyahb,". This also clears "him", which in that sentence could mean Thomas.
- Records: add "Assemani: Thomas 'nono saeculo ineunte claruit' (ASS31 l.78622-78626)" to the Thomas date claim.

**R1-BM14 (brief and card: one place, two spellings across profiles).** Ishoyahb writes "Beth Abe" throughout. The batch5 Thomas of Marga profile, the live census Thomas entry (`movements[604]`) and the Timothy I card (`[599]`) write Budge's "Beth 'Abhe"; the Babai card (`[543]`) writes "Beth Abe". Within this profile the term is consistent. Across the two linked profiles a listener meets one house under two names.
- No text change is required in this round. Log it to the batch's Open-Gaps entry so the census fix picks one form, or align this profile to "Beth 'Abhe" to match its companion profile.

**R1-BM15 (card `knownFor`: parse).** "His surviving letters fight the teaching of his friend Sahdona and the bishops of Fars and Qatar who broke from him." This can be heard as fighting the bishops' teaching. Duval lists letters "adversus Sahdonam, et adversus Simeonem ... episcoposque Qataraeos" (DUV l.230-232).
- Fix: → "Among his surviving letters are attacks on the teaching of his friend Sahdona, and letters against the bishops of Fars and Qatar who broke from him."

**Against the Thomas of Marga profile (batch5).**
- No fact conflicts. The brief's "dated 840 by its translator, E. A. Wallis Budge" matches the Thomas brief's "Budge's title dates the book to 840" (TOM l.94 is Budge's title page).
- Thomas's use of the monastery's tradition (TOM l.5688-5690, l.5733-5752) matches the Thomas brief's sources passage.
- Neither profile has Ishoyahb in Thomas's lifetime, and both cards sit in The Church of the East on the Silk Road.
- The remaining differences are R1-BM13 and R1-BM14.

Checked and sound:
- The vision, the sacristan, seventy men and Jacob's body, the recall and Kuphlana (TOM l.6600-6620, l.6745-6795).
- "Of Adiabene" (TOM l.5782-5783; SEERT2 l.34489; ELI l.3627).
- Nineveh, then the Arbela and Mosul metropolitanate (AMR l.13286-13287; DUV l.106-107).
- The embassy: Thomas against the anonymous chronicle. Guidi's 670 to 680 and Nöldeke (GUIDI l.1589-1597, l.2341-2344).
- Sahdona: Thomas against Seert, and Scher's note (TOM l.5779-5784; SEERT2 l.34462-34494).
- Amr's election story, unbracketed and so common to Amr and Sliba (AMR l.13286-13295).
- "Virum infirmum" (DUV l.7625-7626). The 647 to 650 and 657 to 660 placings, each held at its cited line, including Lamy's "ante annum 660" (BH3 l.7536-7540).
- Bar Hebraeus's bribery charge and Lamy's note (BH3 l.7414-7417, l.7434-7435).
- The Arab rulers passage and the India passage (DUV l.8715-8719, l.8740-8747; MING l.1553-1567). Budge's footnote "he was a married man" (TOM l.5517) and Guidi l.2302 concern Ishoyahb II, not him.

## README

**R1-BM16 (Other profiles, Ishoyahb bullet, and Live census mentions (3): stale against the current draft).**
- The Other profiles bullet says "The draft's 'his 840 history' (brief) and 'in 840' (card `uncertain[0]`) differ in dropping the attribution". The census bullet (3) says the Babai card is "more careful than the draft (C1)".
- The draft now reads "dated 840 by its translator, E. A. Wallis Budge" (brief para 2) and "about 840 by Budge's date, or between 832 and 850 by Jérôme Labourt" (card `uncertain[0]`).
- Fix: Other profiles → "The draft dates the book 840 by Budge's title (brief) and adds Labourt's 832 to 850 (card), as the Thomas profile does; after R1-BM13, Assemani's early ninth century as well." Census (3) → "agrees with the draft".

**R1-BM17 (Who the sources are, Ishoyahb: a date stated flat).** "Thomas of Marga's Book of Governors (840, Budge's English)" → "Thomas of Marga's Book of Governors (840 by Budge's title; Labourt, 832 to 850; Budge's English)".

**R1-BM18 (Corrections to the re-score, Stephen l.160, and Live census mentions, Stephen: the margin's 797).** "the Bollandists' margin gives 797 (l.50387)" → "the Bollandists' margin has him writing just after Easter of 797 (l.50376-50387), which implies the raid in 797". This matches R1-BM6. The census bullet's "only their margin 797, after Easter (l.50384-50387)" is close; give the range as l.50376-50387.

Checked and sound:
- The census bullets for all three are complete for every spelling I walked, and their agree/differ verdicts hold.
- The Theodore census bullet: `movements[65]` `statusDescription`, `sourcing`, `why`, `longDescription`, `voices[1]`, `sources[1]`, `people[1]` and `documentedStories[1]`. There are no other qurr, Abucara or Harran-Theodore hits.
- The Stephen census bullet: the one passage, `movements[65]/documentedStories[0]`. Every other Mansur, Mar Saba or 797 hit is another matter.
- The Ishoyahb census bullet, with its namesakes.
- The card traditions, including the Silk Road entry's c. 635 to 845 (`movements[63]`), and the Rescore rows at l.159, l.160 and l.165.
- If R1-BB1 and R1-BM7 are applied, Theodore runs 336 and Stephen 327 words, still inside the stated 324 to 338. Restate the range only if other fixes move it.

**Verdict.** 1 blocking (R1-BB1, Theodore). 18 minor: Theodore 5, Stephen 3, Ishoyahb 7, README 3. Stephen and Ishoyahb pass. Theodore passes once R1-BB1 is applied. The "Stephen of Mar Saba" name and the dropping of "Mansur" are confirmed.

---

## Era 4 Who batch 11, round 1 review: PART C

**Scope.** `al-tabari` and `ibn-ishaq` (brief, card, `records.json` entry, audio), both outside witnesses. The README's general sections: opening, Majors and lengths, River and tradition counts, Card traditions, Language and quotations, the file table, and the README bullets for these two people. Cross-batch consistency of all eight (form, field conventions, terms).

**Method.** I read CLAUDE.md, the Pattern (including "The outside witness" and the 14-item checklist), lessons_review.md, the batch 11 README and the batch 8 al-Baladhuri profile as precedent, and the Rescore rows (l.102, l.156-157). Every brief sentence and card field for the two profiles was reopened with sed in T4, T5, GINZEL, HITTI, WEIL, WUE, MOBERG, EVETTS, ELIAS and QUATREMERE. I ran case-sensitive and variant searches over all of cic/texts for Tabari (Tabari/Tabary/Ṭabarī/Thabari, Jarir, Abu Ja'far, Yazdegerd + "last") and for Ibn Ishaq (Ibn Is(h)aq/Ishak/Ishâk, Hisham/Hischam) to test every absence claim. I walked census.json (release 44) with a regex walker over movements, edges, retired lists and eras for every spelling the README lists, plus Yazdegerd, Merv, Aelia, jizya, Khalid, Hira, Kaleb, 523 and 615. Counts were checked against the census `major` flags and `laneLabel`, the batch 9 and batch 10 READMEs, and Open-Gaps 269. The al-Tabari profile was checked against batch8 al-baladhuri on shared facts. I wrote two scripts. One finds every quoted string in all eight briefs and cards and searches it in the card's source files and the records' witness files, whitespace- and hyphen-tolerant. The other checks the non-Arabic quotes in the two records entries against their cited line ranges. Audio, JSON validity and final newlines were checked by script. Scores come from `engine.m1.gates.grade_text`.

**Quotations.** Briefs: all four brief quotations are verbatim in their files: Hitti "We only transmit to others what has been transmitted to us." (HITTI l.618-619), Moberg "anything that suggests an independent Muhammadan tradition of historical value." (MOBERG l.2693-2694), and Part B's two Ishoyahb quotations (TOM, MING). Cards: every quoted string is found verbatim except al-Tabari's "the testimony of the history of At-Tabari". That one crosses the folio mark "Fol.lllb" (EVETTS l.15053-15054), as the README says, and it is verbatim apart from that mark. Ishoyahb's card puts the Latin scan string "evi" in quotation marks (README M6). Records: the non-Arabic quotes in the two entries hold within tolerance. A few silent scan cleanups and three off ranges are listed below (Tabari M8, Ibn Ishaq M9).

**Audio.** All eight audio files equal the brief with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. All files end in a newline, and all JSON parses.

**Scores.** (words; minutes at 162 wpm; FK; Flesch)
- al-tabari: 333; 2.06; 6.62; 68.9
- ibn-ishaq: 335; 2.07; 6.65; 70.8
- eulogius-of-cordoba: 336; 2.07; 6.83; 69.8
- ishoyahb-iii: 338; 2.09; 7.16; 65.5
- paulus-alvarus: 336; 2.07; 7.82; 63.8
- stepanos-of-taron: 325; 2.01; 7.34; 68.6
- stephen-of-mar-saba: 324; 2.00; 6.21; 75.4
- theodore-abu-qurrah: 332; 2.05; 8.07; 62.4

All pass. All run about 2:00 to 2:05, which matches the README's 324-338. Seven of the eight sit below FK 8. That is not a finding by itself (never pad), but it is worth a read for choppy rhythm.

## al-tabari

**Verdict:** revise (2 blocking, 10 minor). The brief is accurate, sourced and well shaped as an outside-witness profile. It agrees with al-Baladhuri's profile on every shared fact: Hitti as translator in 1916, his judgment that Arab historians rarely weigh reports (batch8 "scarcely judges"), and al-Baladhuri's death in 892 against "after al-Baladhuri".

**R1-CB1 (card `legacy.traces[2]` and records Quatremère claim: misattribution).** The account of the caliph Aziz's library is al-Maqrizi's, quoted by Quatremère. It is not Quatremère's own telling. QUATREMERE l.14025: "« La bibliothèque deskhalifes (2), dit Macrizy," and the quote runs through l.14040-14053 ("plus de vingt exemplaires de cette chronique, du nombre desquels il j en avoit un écrit de la main de l'auteur"). Fix: `traces[2]`: "Étienne Quatremère, in 1811, tells that the caliph Aziz kept more than twenty copies of the chronicle in his library, one written in the author's own hand." → "The Egyptian historian al-Maqrizi, in Étienne Quatremère's French of 1811, tells that the caliph Aziz kept more than twenty copies of the chronicle in his library, one written in the author's own hand." The records claim becomes: "Quatremère quoting al-Maqrizi ('dit Macrizy', l.14025): the caliph 'Aziz' ...", witness l.14025-14053, tag Documented. If "Egyptian historian" is not held in QUATREMERE, use "The historian al-Maqrizi".

**R1-CB2 (records: confidence tags on single witnesses).** (a) Ginzel's "(224 — 310 d. Hedschra) gilt als der verlässlichste aller mohamedanischen Annalisten" (GINZEL l.15786-15789) is tagged Widely Accepted. It is one modern witness who names no source, as the card itself says ("Ginzel names no source"). (b) Quatremère/al-Maqrizi on Aziz's copies (l.14040-14053) is tagged Widely Accepted, also on one witness. Fix: both `formation_confidence` "Widely Accepted" → "Dominant Modern Reconstruction" for (a), and → "Documented" for (b), as the record of what al-Maqrizi says, after B1. Hitti's life at l.911-914 can keep Widely Accepted, following the batch8 precedent, because Hitti names two Arab lives (al-Fihrist and Ibn Khallikan).

**R1-CM1 (brief para 4: "For Aelia, his name for Jerusalem").** Aelia is the name the terms themselves use: "هذا ما اعطى عبد الله عبر امير ... ايلياء من الأمان" (T5 l.6621-6622). The census's own note reads "Aelia, as Jerusalem was then called" (edges[49]). Fix: "For Aelia, his name for Jerusalem, he gives" → "For Aelia, as Jerusalem was then called, he gives".

**R1-CM2 (brief para 3: pronouns aloud).** In "Priests and monks shouted to the men in the castles that they alone were getting them killed", "they" and "them" are hard to sort out when heard. Source: "فنادى القسيسون والرعبان يا اعل القصور ما يقتلنا غيركم" (T4 l.1495). Fix: "Priests and monks shouted to the men holding the castles that their fighting alone was getting the priests and monks killed." Or shorter: "Priests and monks shouted to the men in the castles that they, the castle men, alone were getting the clergy killed."

**R1-CM3 (brief para 1 and card `knownFor`: "The last Persian king").** "Last" appears in none of the card's sources (T5 and its argumentum l.906-912 give only Jazdadjird and Merw). It is held elsewhere: Michael the Syrian, "Yezdegerd, dernier roi des Perses" (michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt l.32600). Fix: add a records claim citing that file and line and add the file to `sources.about`. Otherwise "The last Persian king, Yazdegerd," → "The Persian king Yazdegerd" in the brief, and "the last Persian king" → "the Persian king Yazdegerd" in `knownFor`.

**R1-CM4 (card `keyWorks[1].about`: Moberg's claim told flat).** "Most interpreters refer the Quran's verses on the pit to the Najran martyrs" is Moberg's judgment: "This, no doubt, is the interpretation preferred by the majority" (MOBERG l.2819-2820). Fix: "Most interpreters refer the Quran's verses on the pit to the Najran martyrs. Moberg says the commentary also gives" → "Moberg says most interpreters refer the Quran's verses on the pit to the Najran martyrs, and that the commentary also gives".

**R1-CM5 (card `uncertain[1]`: "states the principle", no referent).** Hitti's principle is "what has been once well said need not be told again" (HITTI l.614-615). Fix: "and that al-Tabari's preface states the principle." → "and that al-Tabari's preface states their rule, that what has been well said once need not be told again."

**R1-CM6 (card `legacy.traces[0]`: "year by year").** Elias cites Tabari under 275-286, 288, 290-297, 300 and 302. The years 287, 289, 298, 299 and 301 have no citation (ELIAS l.7330-7668). Fix: "cites him year by year from 275 to 302 of the hijra" → "cites him in most years from 275 to 302 of the hijra".

**R1-CM7 (card `uncertain[2]`: chain overstated).** "The Hira and Najran reports reach him through a chain of tellers, al-Sari from Shu'ayb from Sayf ibn Umar" covers only the 190,000 Hira report (T4 l.1502). The 90,000 report of the next item follows a chain through Salama from "ابن [Ishaq]" (scan "سلمة عن ابن hos enl", T4 l.673-674). That is Tabari's usual chain to Ibn Ishaq, which is a link to the batch's other profile. Fix: "The Hira and Najran reports reach him" → "The Hira report of 190,000 dirhams and the Najran report reach him". The drafter should also check l.673-697 against the edition's Latin and add the chain of the 90,000 report to the contested-claim side if it holds.

**R1-CM8 (records: ranges).** "Mors Jazdadjirdi apud Merw ... Variae de ejus exitu traditiones" is at T5 l.910-912, not l.906-908. "lAthir" (scan) is at T5 l.5838, not l.5839. Fix the two witness strings: "l.898, 906-908, 23978-24030" → "l.898, 910-912, 23978-24030", and "l.6590-6609, 5839" → "l.6590-6609, 5838".

**R1-CM9 (records: unmarked scan cleanups).** "Elias von Nisibis setzt" (scan "Nisibis®", GINZEL l.15890), "14. Schauwäl 280" (scan "ı4.", l.15897) and "ibn-al-Athir and abu-l-Fida" (scan "abu- 1-Fida", HITTI l.718-719) are cleaned without the "(scan)" mark the README promises. Fix: add "(scan ...)" after each.

**R1-CM10 (card `uncertain[3]`: an editor's held note on the second telling).** At the Merv page, Prym notes "Narratori duas inter se diversas relationes confusas esse perspicuum est" (T5 l.23986-23987). It seems to annotate the second telling (the body on the branch, the bishop's vault). The OCR does not show which word it marks, so the drafter should confirm against the argumentum. Fix, once confirmed: add to `uncertain[3]` after "where he used to sit.": "E. Prym, the volume's editor, thinks this telling joins two different accounts." Add a records claim at T5 l.23986-23987.

## ibn-ishaq

**Verdict:** revise (5 blocking, 12 minor).

**R1-CB3 (brief para 1: two audiences merged into one scene).** The bishops with their books are at the first audience (WEIL l.9374-9376: "Als sie vor den Nadjaschi kamen, der auch seine Bischöfe mit ihren Büchern um sich versammelt batte, fragte er sie: 'was ist das für eine Religion ...'"). The question about Jesus, Ja'far's answer and the twig come on the next day, after Amr's complaint (l.9438-9457: "Am andern Morgen begab sich Amr wieder zum Nadjaschi ... Der Nadjaschi schickte nach ihnen"), and there the murmurers are "Die Patrizier" (l.9454-9455). Fix: "The Muslims who had fled Mecca stood before the Negus, the Christian king of Abyssinia, with his bishops and their books around him. Asked about Jesus, their spokesman Ja'far said" → "The Muslims who had fled Mecca stood before the Negus, the Christian king of Abyssinia, with his bishops and their books around him. The next day he called them back to ask about Jesus. Their spokesman, Ja'far son of Abu Talib, said". Records claim 1: add "second audience, next morning, l.9438-9459" to the witness.

**R1-CB4 (card `place`: unsupported).** "Medina, by Philip Hitti, who sets him at the head of the tradition of Medina" is not in Hitti. Hitti classifies traditions by region and does not place the man: "that of al-Madinah as represented by Muhammad ibn-Ishak and al-Wakidi" (HITTI l.647-648). "At the head" is added. No held line gives where he lived. Fix: `place` → "No source gives where he was born, lived or died. Philip Hitti counts him, with al-Waqidi, as representing the tradition of Medina". Records: none needed beyond claim 6, which stays.

**R1-CB5 (records `absent_details[0]` and card: a false absence).** "Birth, birthplace, family ... No held source gives them" is wrong about family. Al-Baladhuri, in Hitti's English, lists among the captives Khalid took at 'Ain at-Tamr, "certain persons in a church": "(4) Yasar, a grandfather of Muhammad ibn-Ishak — the author of as-Sirah — and a freedman of Kais ibn-Makhramah ibn-al-Muttalib" (HITTI l.15766-15791; footnote l.15805-15806 "The biography of the Prophet from which ibn-Hisham's was abridged"). This also explains the nisba al-Muttalibi on the card. Fix: add a records claim, witness HITTI l.15766-15791, 15805-15806, tag Documented (al-Baladhuri's report). Change `absent_details[0]`.detail to "Birth, birthplace, parents, teachers, travels, place of death, burial" and add to its note: "His grandfather Yasar is named by al-Baladhuri (HITTI l.15789-15791)". Card: add to `uncertain`, after item 0 or as a new last item: "His family. Al-Baladhuri, in Hitti's English, says his grandfather Yasar was among the captives Khalid took from a church at 'Ain at-Tamr, and was a freedman of Qays ibn Makhrama ibn al-Muttalib." Also change `otherNames[1]` to "al-Muttalibi, the name he bears in Ibn Hisham's chain of transmission (Weil: Almuttalebij), after the clan his grandfather served, by al-Baladhuri". Once the absence is corrected, add "al-Baladhuri" to the README's "Who the sources are".

**R1-CB6 (brief para 5 and card `uncertain[0]`: Weil reports a reputation and is made to hold it).** WEIL l.141-144: "galt bei seinen Zeitgenossen sowohl als bei nachfolgenden Gelehrten als ein ausgezeichneter und zuverlässiger Traditionssammler, wenn auch Neid und Sektenhass ihn zu verdächtigen suchte." Weil's own judgment is the next sentence, "den treuen Ausdruck der zu seiner Zeit ... cursirenden Ueberlieferung" (l.144-146). The card's `legacy.remembered[0]` has it right. Fix, brief: "Weil calls him an excellent and reliable collector, whom envy and sectarian hatred tried to discredit." → "Weil says his own age and later scholars held him an excellent and reliable collector, though envy and sectarian hatred tried to discredit him." Fix, card `uncertain[0]`: "Weil calls him reliable, and the faithful voice of the traditions of his day," → "Weil says his own age and later scholars held him reliable. Weil himself calls him the faithful voice of the traditions of his day,". The contested claim's first side ("Weil: a faithful expression ...") already matches.

**R1-CB7 (records: confidence tags against the card's own words).** The card says the al-Mansur commission "rests on one sentence of Hitti's, who names no early source for it" (`uncertain[4]`). Records claim 4 (HITTI l.665-669, "written for al-Mansur ... (d. 151/767)") is tagged Widely Accepted, and claim 6 (Hitti's judgment on Medina, l.646-652) is also tagged Widely Accepted. Each is one modern witness. Fix: claim 4 "Widely Accepted" → "Dominant Modern Reconstruction". Claim 6 "Widely Accepted" → "Dominant Modern Reconstruction".

**R1-CM1 (brief para 1: common name).** "Ja'far" is a common name, and the same book has a Ja'far son of Muhammad at l.9567. WEIL l.9378-9379: "Djafar, der Sohn Abu Talibs". The fix is folded into B3: "Ja'far son of Abu Talib".

**R1-CM2 (brief para 2: witness role).** "A note by B. T. A. Evetts, in 1895, gives 768." does not say who Evetts is. Fix: "B. T. A. Evetts, in a note to the book on Egypt's churches he edited in 1895, gives 768." (EVETTS header and l.5637-5640).

**R1-CM3 (brief para 5: "much").** Weil's "Manches" is "some things", and he adds that it is not to be held against Ibn Ishaq (l.146-148). Fix: "Weil adds that much he tells as fact belongs to legend." → "Weil adds that some of what he tells as fact belongs to legend, which Weil does not count against him."

**R1-CM4 (brief: two sentences past 25 words).** "When Christians from Najran came to debate at Medina, he says they held, like all Christians, that Jesus is God, a son of God and the third of three." (29 words). Fix: "Christians from Najran later came to Medina to debate. He says they held, like all Christians, that Jesus is God, a son of God and the third of three." The closing Moberg sentence has 33 words. Fix: "Axel Moberg edited a Syriac account of the Najran martyrs in 1924. In the Arabic stories of the persecution, he could not see "anything that suggests an independent Muhammadan tradition of historical value.""

**R1-CM5 (brief close: the doubt without its why).** The Pattern says "Each doubt names who raises it and why." Moberg's reason is that the facts "are owed ... to a relation already well known — that of the Acta" (MOBERG l.2704-2708). If words allow, add after the Moberg sentence: "He traces their facts to the older Christian Acts of the martyrs." The card's `uncertain[1]` already carries this.

**R1-CM6 (card `sources.about[1]`: title and author).** "The Origins of the Islamic State, part 1, introduction", with author "al-Baladhuri; Philip Khuri Hitti (tr.)". The introduction is Hitti's, and the file is volume I (header l.1-4; "PART I— ARABIA" at l.213 is after the introduction). The al-Tabari card has it right. Fix: title → "The Origins of the Islamic State, volume 1, introduction"; author → "Philip Khuri Hitti". After B5, the line on Yasar is al-Baladhuri's own text, so add a second entry, or retitle this one "introduction and text" with author "Philip Khuri Hitti; al-Baladhuri".

**R1-CM7 (card `knownFor`: Waraqa has no record, and the frame is loose).** Waraqa is held (WEIL l.4532 "Waraka I. Naufal ... dieser war Christ geworden"; l.5366-5368 "Waraka, der ein gelehrter Christ war"), but no claim in records supports him. He met Khadija and Muhammad, not "Muhammad's first followers" as a group. Fix: add a records claim (WEIL l.4532-4533, 5366-5369). Then "tells of the Christians Muhammad's first followers met:" → "tells of Christians who met Muhammad and his first followers:".

**R1-CM8 (card `dates`, `place`: drafting language).** "No source used here gives his birth". The brief asks for no "used here" on reader-facing text, and the Tabari card says "No source gives". Fix: "No source used here gives his birth" → "No source gives his birth". The `place` text is replaced in B4. The same applies to stephen-of-mar-saba (README M8).

**R1-CM9 (records: ranges).** The Faymiyun claim cites l.1003-1010 and l.1066-1067. "Ein frommer, eifriger Christ, Feimijun genannt" is at l.996, "ein Zimmermann und Maurer" at l.1000, and the sale "in Nadjran verkauft" at l.1061. Fix: witness → "l.996-1000, l.1060-1061, l.1091-1093".

**R1-CM10 (card `uncertain[5]`: "later").** "one of the exiles and later Muhammad's wife": Weil gives only "Gattin Mohammed's" (l.9303-9304). Fix: "and later Muhammad's wife" → "and a wife of Muhammad". The brief's "one of the exiles" is fine.

**R1-CM11 (card: the Negus's later turn, held in his own book).** The card's `knownFor` counts the Negus among the Christians. Ibn Ishaq goes on to say the Abyssinians rose against him ("Du hast Dich von unserm Glauben losgesagt") and that he wrote out the Muslim confession (WEIL l.9567-9597, a range the README itself cites). Fix: add to `uncertain[1]` after its first sentence: "Ibn Ishaq also tells that the Abyssinians rose against the Negus for leaving their faith, and that he wrote out the Muslim confession of faith." Add a records claim at l.9567-9597.

**R1-CM12 (records: unmarked scan cleanups).** "wie alle Christen" (scan "\rie alle", WEIL l.16966) and "lebte in der ersten Hälfte" (scan "lebte in i.' der ersten", l.140-141) are cleaned without "(scan)". Fix: add the marks.

## README

**R1-CB8 (River and tradition counts: the era 4 standing counts mix two rules).** The README says that by the census's own Who rows the majors "stand at Latin West & Catholicism 10, Greek East & Orthodoxy 5", and then that by card traditions "Greek East stands at nine, as the batch 9 and batch 10 READMEs set out". The 10 and 5 are the release 44 flags alone (verified: census era 4 person rows with `major` true are Latin West 10, Greek East 5, Syriac East & Asia 4, Caucasus 1, Africa 1). The nine includes batch 9's three Greek East majors. Batch 9's README l.11, batch 10's README l.13 and Open-Gaps 269 all count the census rule with batch 9's majors: Greek East eight and Latin West eleven, with Anskar. By card traditions they count nine and ten. Fix: "By the census's own era 4 Who rows (release 44's major flag), the majors stand at Latin West & Catholicism 10, Greek East & Orthodoxy 5, Syriac East & Asia 4, Caucasus 1 and Africa 1. Counted by era 4 card traditions, Greek East stands at nine, as the batch 9 and batch 10 READMEs set out." → "Release 44's major flags give era 4 Latin West & Catholicism 10, Greek East & Orthodoxy 5, Syriac East & Asia 4, Caucasus 1 and Africa 1. With batch 9's majors (John of Damascus, Theodore, and Cyril and Methodius in the Greek East; Anskar in the Latin West), the census rule gives Greek East eight and Latin West eleven. Counted by era 4 card traditions, Greek East stands at nine and Latin West at ten, as the batch 9 and batch 10 READMEs and Open-Gaps 269 set out."

**R1-CB9 (River and tradition counts: "two outside the church ..., which have no river").** In the census, outside witnesses do sit on a river lane. al-baladhuri (era 4) has `laneLabel` "Syriac East & Asia" with `toldWithin` null. Ammianus Marcellinus sits on the Latin West, Procopius and Agathias on the Greek East, and Josephus, Suetonius, Tacitus and Pliny on the Origin lane. Saying these two "have no river" contradicts the precedent their own card follows. Fix: "and two outside the church (al-Tabari, Ibn Ishaq), which have no river." → "and two outside the church (al-Tabari, Ibn Ishaq). Their cards carry no tradition, but the census places each outside witness on a lane: al-Baladhuri, of Baghdad, sits on Syriac East & Asia. Which lane these two take is for the map build slice (Open-Gaps, "Map Who build slice: caps, major mark, placement", 2026-11-11)." Then log it in the batch's Open-Gaps entry.

**R1-CM1 (Live census mentions and Other profiles: dangling labels and drafting language).** "(C1)", "(C4)", "(C6)" and "(C7)" refer to a crosscheck list that is not in the README (it lives in the scratchpad's crosscheck.md). "The draft", "the draft card" and "the draft attributes" will be stale once the profiles are approved. Fix: replace each "(C<n>)" with the finding itself, or with "see the batch's Open-Gaps entry". Replace "the draft" with "the profile", "the draft card" with "the card", and so on.

**R1-CM2 (Other profiles, al-Tabari: stale brief text).** It quotes "Hitti says Arab historians did little to weigh or test their reports". The brief now reads "Arab historians did little to test their reports". Fix: requote, and drop "see (C7)".

**R1-CM3 (Live census mentions: passages missed).** For Ibn Ishaq the bullet lists `movements[53]` `why`, `longDescription`, `statusDescription` and `documentedStories[1]`. It misses `relationsSummary` ("The Najran martyrs of 523 and King Kaleb's campaign in Himyar around 525"), `voices[0]` (Kaleb "around 525 in response to the killing of the Christians of Najran") and `voices[3]` (the martyrs "killed in Himyar in 523"), which differ from his version on the same points as `documentedStories[1]`. It also misses `movements[609]/card/uncertain[4]` ("his works rest on the tradition of Medina"), which is Hitti's passage naming him (agrees). For al-Tabari the bullet misses `movements[569]/card/uncertain[0]` (Theophanes's account of Umar at Jerusalem; neither confirmed nor contradicted). Fix: add these, each with agree or differ.

**R1-CM4 (Live census mentions: an Open-Gaps entry that does not exist yet).** "Open-Gaps, 'Era 4 Who batch 11' (2026-11-15)" is not in Open-Gaps.md (the last era 4 entry is 272, batch 10). Fix: create it at approval, as batch 10 did, before the README is merged, or cite it as "to be logged".

**R1-CM5 (opening or Majors and lengths: the re-score's caveats not carried).** Rescore l.156 says of al-Tabari "Mark may judge it too thin". l.157 calls Ibn Ishaq a "judgment call", since the held text is Ibn Hisham's recension. Fix: after "al-Tabari's and Ibn Ishaq's lives are thin as well, as the outside-witness rule allows." add: "The re-score leaves both to Mark: al-Tabari's life may be judged too thin, and Ibn Ishaq's held text is Ibn Hisham's recension (Rescore l.156-157)."

**R1-CM6 (Language and quotations: a Latin scan string in quotation marks).** The README rule is "Quotation marks are kept for held English". The Ishoyahb card's `keyWorks[0].about` reads "106 letters (the scan reads \"evi\")", from DUV l.222 "Epistulae supersunt hodie evi" (cvi). Fix, in Part B's file: "106 letters (the scan reads \"evi\") in three parts" → "106 letters in three parts", and keep the scan reading in records. If it stays, list it in this section.

**R1-CM7 (Who the sources are: Ibn Ishaq).** After CB5, "His life rests on Weil, Hitti and a note by B. T. A. Evetts (1895)." → "His life rests on Weil, Hitti, a line of al-Baladhuri's in Hitti's English on his grandfather, and a note by B. T. A. Evetts (1895)."

**R1-CM8 (cross-batch: one form for honest limits on cards).** ibn-ishaq (`dates`, `place`) and stephen-of-mar-saba (four places) say "No source used here gives". The other six say "No source gives". "Used here" is drafting-process language on reader-facing text. Fix: "No source used here" → "No source" in both cards. Also stephen-of-mar-saba's "...used here. Of his own life" and "No source used here makes the writer a relative": drop "used here".

**Cross-batch checks that pass.**
- All eight cards follow the Pattern's field order, with `label` only on the two outside witnesses, as on al-Baladhuri's card.
- Tradition lines match the census names and dates: Mozarabic Christianity 711-1031, Melkite Arabic Christianity c. 700-1009, The Church of the East on the Silk Road c. 635-845, and Bagratid Armenian Christianity c. 884-1045. St Thomas Christians begins in 849, so the README's reason for moving Ishoyahb holds.
- `briefLength` reads "about 2 minutes" throughout.
- `dates` and `place` end without a period, as in the batch 8 and batch 10 house form.
- American spelling holds outside titles (the one "Defence" is Grotius's title).
- The file table matches the files.
- "None of the eight has a census person row" and the Major column "no" for all eight hold (Rescore l.133-165).

A pointer for Parts A and B: by a script count, stepanos-of-taron has three sentences past 25 words (31, 26 and 29) and theodore-abu-qurrah has one (26).

**Verdict.** Revise. Blocking: 9 (al-tabari 2, ibn-ishaq 5, README 2). Minor: 30 (al-tabari 10, ibn-ishaq 12, README 8).
