# Era 4 Who batch 11: round 2 review (targeted recheck)

Three parts, each by a fresh Opus agent at full effort that had not seen the drafting, against R1_review.md and R1_changes.md and the diff since 3e085559. Totals: 4 blocking, 23 minor (Part A 1 and 9, Part B 2 and 4, Part C 1 and 10).

## Era 4 Who batch 11, round 2 review: PART A

**Scope.** A targeted recheck of the round 1 changes to `stepanos-of-taron`, `eulogius-of-cordoba` and `paulus-alvarus`: brief, card, the `records.json` entry and the audio file for each, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`. I also checked the README bullets for these three. Untouched text was not re-reviewed, except where a fix changed what a nearby pronoun or referent points to.

**Method.** I read CLAUDE.md, `Who_Profile_Pattern.md` with its checklist, `lessons.md`, R1_review.md Part A with its README section, and R1_changes.md Part A with the README log. I worked from `git diff --word-diff 3e085559 HEAD` over the batch folder. I reopened every source line that a changed string rests on with `sed -n`:
- MAC l.430-446, 680-960, 973-980, 1014-1031, 3966-4001, 6274-6277, 15206-15215;
- ZAK l.26005-26025 and its header;
- KART l.12036-12041, 13889-13908;
- CHAB l.38270-38326 and its header;
- CHAM l.5198-5205 and its header;
- CONY l.2576-2582;
- EUL l.56696-56713, 58338-58348, 58860-58912, 58955-59000, 59168-59190, 63240-63262, 68574-68584, 75575-75578;
- PL83 l.123284-123290;
- ALV l.30924-30952, 31010-31076, 31540-31552, 31606-31660, 31672-31720, 40466-40472.

I checked the census paths that the README changed in release 44 (`movements[116]`, `movements[72]/voices[0]`). I also ran score.py and compared each audio file with its brief.

**Quotations.** No brief of the three uses quotation marks. On the cards, the only quoted strings are Stepanos's `"of Taron"` (a gloss, unchanged) and Neumann's "the learned Asolnik" (unchanged, verbatim at EGH l.798-799). The round 1 fix removed the French "Asolik" from quotation marks. Every changed Latin or French quotation in `records.json` for the three people is verbatim, whitespace- and OCR-tolerant, inside its cited range. I checked these:
- Tamayo's elogium and notes (ALV l.31683-31691);
- "non carnis nexu, sed contubernii vinculo" (l.31703-31705);
- "Codicem alium Toletanae Ecclesiae Thomas Tamaius laudat" (l.31019-31020) and "regio chronographo" (l.31061-31062);
- "litteris gothicis exarato" (l.31074);
- "Falso" / "False tribuuntur hi versus Virgilio" (l.31057, l.40470);
- note (c) on Bede, Defensor and Cassiodorus, and the Escorial gloss (l.31611-31655);
- Morales on Usuard and Charlemagne (EUL l.58865-58874) and note b "Labitur Morales ..." (l.58905-58911);
- the chronicle "Septembrio mense ... anni 883" and "Postea Dulcidius ..." (l.58985-58998);
- the Oviedo lessons (l.58961-58964);
- "omnes, tam clerici quam laici" (l.59176-59177);
- "iterum adversus eos hoc opere insurgit" and "Erat autem misere corruptum exemplar" (l.68574-68584);
- "quod ex ejusdem libro tertio constat ... Mahomad nominat" (l.56706-56710);
- "Divus Eulogius Cordubensis" (l.75577) and the Toledo list (PL83 l.123287-123289);
- Emin, Malkhasiants and Macler on the death (MAC l.740-764);
- Zarbhanalean (l.768-776);
- Alishan's "chantre et marie du Tarôn" (l.788-791);
- Brosset's two interpolations and "on ne sait pas qüand mourut l'auteur" (ZAK l.26016-26020);
- Brosset on "Asolic" (KART l.12038-12040, l.13891, l.13906-13907);
- Chamich (CHAM l.5200-5203);
- Conybeare (CONY l.2580, and MAC l.799-801);
- "le récit d'Etienne Asolik" (CHAB l.38282). This line is verbatim, but its witness is misnamed; see R2-AB1.

All are verified.

**Audio.** All three audio files equal their brief, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. Final newlines are present.

**Scores.** (score.py, 162.5 wpm)

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| stepanos-of-taron | 336 | 2:04 | 6.6 | 70.1 |
| eulogius-of-cordoba | 337 | 2:04 | 6.8 | 69.8 |
| paulus-alvarus | 336 | 2:04 | 7.9 | 63.3 |

All three are under about 2:05 (338 words), so none needs a README exception. All three pass FK ≤ 10 and Flesch ≥ 60. The README's restated range, 333 to 338, matches the files. All three cards are valid JSON with a final newline.

**Round 1 findings.**
- R1-AB1: confirmed, applied with change. The Brosset role, "who put an Armenian chronicle into French", holds: the ZAK volume is his French of Armenian chronicles, and the note is at l.26016-26020. The year 1876 is right. The new sentence's pronoun is a problem (R2-AM2).
- R1-AB2: confirmed, applied with change. "Macler answers ... one could as well say Stepanos was alive then" is a closer rendering of MAC l.754-756 than the reviewer's "fixes nothing". The `uncertain[3]` sentence is long and its "then" has no clear time (R2-AM3).
- R1-AB3: confirmed, applied. The parenthesis points to a word the card does not show (R2-AM4).
- R1-AB4: applied, but with a misattribution (R2-AB1). The Brosset half is right: KART cites "Asolic" 25 times, for dates and events. The Michael the Syrian note is signed "(J. M.)" and is not Chabot's own.
- R1-AB5: confirmed, applied. Every new claim exists. One range does not hold its quote (R2-AM5).
- R1-AM1: confirmed ("In his youth", which covers Macler's "jeunesse" and Gelzer's "Kindheit").
- R1-AM2: confirmed.
- R1-AM3: confirmed, applied with change. The para 4 split now leaves an unclear "he" after the new Emin sentence (R2-AM1).
- R1-AM4: confirmed.
- R1-AM5: confirmed, applied with change. "An Armenian scholar" for Alishan is fair from MAC l.788 and l.870-875 (his Armenian works). Dropping "Mekhitarist" from the brief is right, since MAC l.883-884 makes the library Mekhitarist, not Alishan.
- R1-AM6: confirmed, applied with change. Giving no year is right, since the scan gives Emin's range two ways (l.712 and l.752).
- R1-AM7: confirmed, applied with change (`knownFor` and `keyWorks[0]`).
- R1-AM8: confirmed. Conybeare has no role at first mention (R2-AM6).
- R1-AM9: confirmed (MAC l.439-441).
- R1-AM10: confirmed, applied with change. `place` rests on MAC l.975-977 and l.15210-15214. The records range is wrong (R2-AM5).
- R1-AM11: confirmed, applied with change ("district", MAC l.6276).
- R1-AB6: confirmed, applied with change. Both sides hold against ALV l.31683-31716, and the contested claim is in place.
- R1-AB7: confirmed, applied with change. The Morales premise (EUL l.58865-58874) and note b (l.58905-58911) are both held, and the contested claim is in place.
- R1-AB8: confirmed, applied with change. The chronicle (l.58985-58996), the note's "Postea Dulcidius" (l.58996-58998) and the separate Oviedo lessons (l.58961-58964) are each correctly placed. "Written in November 883" rests on "Novembrio discurrente ... qui hoc scribebat mense anni 883".
- R1-AB9: confirmed. All eight claims are retagged Documented and marked as a single witness.
- R1-AM12: confirmed. The move leaves para 2's "the city" with only a distant referent (R2-AM7).
- R1-AM13: confirmed, applied with change ("nearly all their fellow Christians" holds against l.59176-59187).
- R1-AM14: confirmed.
- R1-AM15: confirmed.
- R1-AM16: confirmed.
- R1-AM17: confirmed.
- R1-AB10: confirmed (brief, card and records).
- R1-AB11: confirmed. Note (c) is correctly separated from Antonio's main text (l.31544-31551).
- R1-AB12: confirmed. The two cards agree.
- R1-AB13: confirmed (Burial is Documented, Authorship is Contested).
- R1-AM18: confirmed, applied with change. "Preceptoris nostri Alvari" is at EUL l.63244-63245, in Memorial Book II, so "Memorial of the Saints" holds.
- R1-AM19: confirmed, applied with change. The Barberini clause slightly misplaces the gift (R2-AM8).
- R1-AM20: confirmed.
- R1-AM21: confirmed.
- R1-AM22: confirmed.
- R1-AM-R1: confirmed. No "(C<n>)" label remains.
- R1-AM-R2: confirmed.
- R1-AM-R3: confirmed, applied with change. MAC l.885-886 supports "whose age Alishan does not give".
- R1-AM-R4: confirmed. `movements[116]` is hesychasm-and-the-palamite-synthesis, "recorded by the physician Taronites".
- R1-AM-R5: confirmed. `movements[72]/voices[0]` reads "executed in 859".

## stepanos-of-taron

**Verdict:** revise (1 blocking, 6 minor).

**R2-AB1 (card `legacy/traces[2]`, "Jean-Baptiste Chabot, the editor of Michael the Syrian's Chronicle, points to his account of the synod of Manazkert."; records claim "Chabot, on Manazkert"): misattribution.** The note that cites Asolik on the synod is signed by someone else: "Sur ce concile, cf. le récit d'Etienne Asolik, trad. Dulaurier, p. 131. ... Hist. de la Siounie, eh. lxix, trad. Brosset, p. 252. La note de Brosset, p. 75, est inexacte. (J. M,)" (michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt l.38282-38284). Chabot's initials are J.-B. C. (l.1, l.50). In the same block of notes he says he relied on "M. J. Marquart, qui a bien voulu me communiquer les notes" (l.38314-38315). The note is in Chabot's edition, but it is not Chabot speaking.
Fix: card `legacy/traces[2]`: "Jean-Baptiste Chabot, the editor of Michael the Syrian's Chronicle, points to his account of the synod of Manazkert." → "A note in Jean-Baptiste Chabot's French edition of Michael the Syrian's Chronicle points to his account of the synod of Manazkert."
Records:
- claim "Chabot, on Manazkert: …" → "A note signed (J. M.) in Chabot's edition, on Manazkert: \"Sur ce concile, cf. le récit d'Etienne Asolik, trad. Dulaurier, p. 131\"";
- witness "l.38282-38283" → "l.38282-38284".
The `sources.about` entry stays, since the file is used.

**R2-AM1 (brief, para 4, "In his youth, he writes, he saw some great teachers in their old age."): the pronoun is unclear aloud.** The paragraph before now ends on the new R1-AM11 sentence, whose subject is "J.-B. Emin, his Russian translator". Heard aloud, "he writes" goes to Emin. The source line is Stepanos's own: "Dans notre jeunesse, nous avons vu nous-même quelques-uns de ces [Pères]" (MAC l.4302-4304).
Fix, brief and audio: "In his youth, he writes, he saw" → "In his youth, Stepanos writes, he saw". The words stay at 336. The later "Stepanos tasted" can stay.

**R2-AM2 (brief, para 5, "Marie-Félicité Brosset, who put an Armenian chronicle into French, wrote in 1876 that no one knows when he died."): the pronoun is unclear aloud.** The nearest "he" is Brosset himself. The source is "Du reste on ne sait pas qüand mourut l'auteur" (zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt l.26019-26020).
Fix, brief and audio: "that no one knows when he died." → "that no one knows when Stepanos died."

**R2-AM3 (card `uncertain[3]`, the R1-AB2 sentence): about 46 words in one sentence, "until 1041 to 1045", and a "then" with no clear time.** Emin has him alive "entre 1041 et 1045" (MAC l.742-743). Macler's "alive then" means at the date Gregory went on to write to: "le même Grégoire a écrit jusqu' en 1097 [scan], et l'on [pourrait] aussi bien dire qu'Étienne de Tarôn était encore vivant à cette date" (l.754-756).
Fix: "Emin, from a letter of Gregory Magistros, had him alive until 1041 to 1045 and dying at about 117 or 129; Malkhasiants found that age wholly unlikely, and Macler answers that Gregory wrote for years after, so one could as well say Stepanos was alive then." → "Emin, from a letter of Gregory Magistros, had him alive between 1041 and 1045 and dying at about 117 or 129. Malkhasiants found that age wholly unlikely. Macler answers that Gregory wrote for years after, so one could as well say Stepanos was still alive at that later date."
Records: no change.

**R2-AM4 (card `uncertain[5]`, "a cantor from Taron (the scan is garbled at this word)"): the parenthesis points to a word the reader is not shown.** The scan reads "on croit nil était chantre et marie du Tarôn" (MAC l.791). The garbled word "marie" is left out of the card, so "this word" has nothing to point to.
Fix: "says he was thought to be a cantor from Taron (the scan is garbled at this word); Macler doubts the list." → "says he was thought to be a cantor from Taron; one word in the scan of that line is garbled. Macler doubts the list."
Records: no change. The claim already notes "scan garbled at \"marie\"".

**R2-AM5 (records claim "Ani: the Bagratids \"régnèrent à Ani\" …", witness "l.444-445, l.15210-15214"): the range does not hold the quote.** MAC l.444-445 reads "les annales arméniennes. / Le récit commence à la fondation de la dynastie arménienne". The quoted words are at l.975-976: "Asolik est lhistoriographe des rois arméniens de la initie / Bagratouni (Bagratide) qui régnérent à Ani".
Fix, witness: "l.444-445, l.15210-15214" → "l.975-976, l.15210-15214".

**R2-AM6 (card `uncertain[6]`, "F. C. Conybeare placed the writing between 991 and 1019, as Macler quotes him"): no role or time at first mention, and "quotes" goes past the source.** Macler paraphrases: "M. Conybeare (Rituale Armenorum, p.xxxm) estime qu'Étienne Asolik dut écrire son histoire entre 991 et 1019" (MAC l.799-801). Conybeare's own line is "The historian Stephanos Asolik, who wrote between A.D. 991 and 19190" (rituale-armenorum-lectionary_conybeare1905.txt l.2580). The card's source entry dates the book 1905.
Fix: "F. C. Conybeare placed the writing between 991 and 1019, as Macler quotes him (the scan of Conybeare's page reads 19190)." → "F. C. Conybeare, in his Rituale Armenorum (1905), placed the writing between 991 and 1019, as Macler reports (the scan of Conybeare's page reads 19190)."
Records: no change.

## eulogius-of-cordoba

**Verdict:** pass after one minor fix (0 blocking, 1 minor). Every round 1 fix holds against its source.

**R2-AM7 (brief, para 2, "when Muslim emirs ruled the city"): the referent is now distant.** The R1-AM12 fix moved "of Cordoba" into para 1, where it is only a name tag. Para 2 no longer names the city, so a listener hears "the city" with no place in mind. The source is "Cordube civitatis ... natus" (EUL l.56818). The Alvarus brief has the same sentence with "Cordoba" in it.
Fix, brief and audio: "when Muslim emirs ruled the city." → "when Muslim emirs ruled Cordoba." The words stay at 337.

## paulus-alvarus

**Verdict:** pass after one minor fix (0 blocking, 1 minor). Every round 1 fix holds against its source.

**R2-AM8 (card `legacy/traces[0]`, "Antonio's own copy came from one that Tamayo de Vargas gave to Cardinal Barberini's library in Rome."): the gift is misplaced.** Antonio's text: "transcriptum ex altero nobis communicato ex amplissima Francisci S. R. E. cardinalis Barberini Romana bibliotheca, in qua asservatur: olim eidem, ... Matriti, dum ... a latere venisset legatus, ab eodem Thoma Tamaio de Vargas, regio chronographo, ... scriptum et oblatum" (paulus-alvarus_confessio-epistolae-indiculus-luminosus-pl121-lat_migne1852.txt l.31029-31036, l.31058-31063). Tamayo de Vargas gave the copy to the cardinal himself, at Madrid, while he was there as legate. It is now kept in the cardinal's library at Rome.
Fix: "Antonio's own copy came from one that Tamayo de Vargas gave to Cardinal Barberini's library in Rome." → "Antonio's own copy came from one that Tamayo de Vargas gave to Cardinal Barberini at Madrid, now in the cardinal's library at Rome."
Records: the claim already quotes l.31029-31036 and l.31058-31075. Add "Matriti, dum ... legatus" to the quoted words, with l.31058-31061 already in the range.

## README

**R2-AM-R1 (README "Other profiles", Paulus Alvarus, "The Alvarus who was Eulogius's brother (EUL l.68012-68030) appears in no other profile; no profile confuses the two."; "Corrections to the re-score", Alvarus, "l.68018 is about Eulogius's blood brother, also named Alvarus, another man."; "Names and ids", "Eulogius's blood brother, also named Alvarus, is another man."): Antonio's side is told as settled.** These lines were left untouched, but round 1 made the identity a contested claim on both cards. Tamayo's notes "hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre" and "non carnis nexu, sed contubernii vinculo"; Antonio holds "fratrem vere germanum Eulogii alterum Alvarum" (ALV l.31687-31691, l.31703-31708). The README's own Eulogius bullet now gives both sides, so these three lines contradict it.
Fix:
- "Other profiles": "appears in no other profile; no profile confuses the two." → "appears in no other profile. The two batch 11 cards give both Tamayo's view that he was Paulus Alvarus and Antonio's that he was another man."
- "Corrections": "l.68018 is about Eulogius's blood brother, also named Alvarus, another man." → "l.68018 is about Eulogius's brother Alvarus, whom Antonio holds to be another man and Tamayo took for Paulus Alvarus (ALV l.31683-31716)."
- "Names and ids": "Eulogius's blood brother, also named Alvarus, is another man." → "Eulogius's brother, also named Alvarus, is another man by Antonio's account; Tamayo took the two for one (ALV l.31683-31716)."

Every other changed README bullet for the three people checks out:
- the Stepanos "Who the sources are" sentence (MAC l.751-756, l.885-886, l.905-908; ZAK l.26019-26020);
- the `movements[116]` namesake;
- the `voices[0]` wording;
- the Eulogius and Alvarus brothers line (ALV l.31683-31716);
- the word range, 333 to 338.

**Verdict.** Blocking 1 (Stepanos 1). Minor 9: Stepanos 6, Eulogius 1, Alvarus 1, README 1. Eulogius and Paulus Alvarus pass once their single minor fix is made. Stepanos needs the Chabot attribution fixed (R2-AB1), and that fix needs independent re-confirmation.

## Era 4 Who batch 11, round 2 review: PART B

**Scope.** `theodore-abu-qurrah`, `stephen-of-mar-saba`, `ishoyahb-iii`: every round 1 change to brief, card, audio and `batch11/records.json` (`git diff 3e085559 HEAD`), and the README bullets for the three. I also ruled on R1-CM8 (the four "used here" places on the Stephen card) after a search of all of cic/texts. I checked the coordinator's standing rulings for Stephen. I edited no repo file.

**Method.** I read CLAUDE.md, the Pattern and its checklist, lessons.md, R1_review Part B and the README sections, R1_changes Part B and the README log, the diff, and the README. I reopened each changed string's source range with `sed -n`:
- GRAF: l.836-877, 900-912, 14075-14116, 16944-16960, 632-660.
- PG97: l.122118-122152. PG94: l.116604-116616.
- AASS: l.2725-2756, 9259, 9486-9496, 50365-50548, 53470-53482.
- AMR: l.6375-6410, 13280-13288. MARI: l.13479-13482.
- DUV: l.104-112, 228-233. ASS31: l.78620-78627. LABOURT: l.17232-17236.
- TOM: l.5684-5692, 5730-5753.

The Stephen absence search ran across all 1,771 files in cic/texts with rg. It covered:
- Stephan/Stephanus/Stephen/Stefan/Stefanos/Étienne/Στέφαν/اسطفان/ستيفان within six words of Saba/Sabas/Sabba/Mar Saba/Σαβ/σάβ/سابا.
- Sabaita/Sabaite/Sabaïte/Σαββαΐτ, and "Stephen the Sabaite/Poet/Melode", "Stephanus Poeta" and Stephan… within three words of poeta/ποιητ/melod/μελῳδ/hymnograph.
- Thaumaturg/θαυματουργ/Wonderworker next to Stephen.
- "Mar Saba", Sabaskloster, laure de Saint-Sabas, "twenty/XX/viginti/εἴκοσι … martyrs/monks … Sab", and martyr… Sabait….
- OCR splits: Ste-/Stepha-/Στε- at a line end, and Saba-/Sabai- at a line end.
- Nikodemos vols. 1 and 2, every Στέφανος and Σαββα hit.

I ran score.py. It left `git status` clean, so every audio file already equalled its rebuilt form.

**Quotations.** No brief or card quotation in Part B changed. I re-verified the changed and added records strings verbatim inside their cited ranges:
- Theodore: "Bischof war letzterer jedenfalls" (GRAF l.14112-14113), "der Lügner und Irrlehrer Nestorius" (l.876), "Quare assentior Turriano" (PG97 l.122148), "ut a sententia nos Turriani retrahant" (l.122125) and "perpe[r]am Turriano accipitur" (PG94 l.116609-116610, scan "perpeamy"). Verified.
- Stephen: the prologue's "quam scribendis temere se sermonibus ingerant, quos in ecclesia sacrisque conventibus necesse sit recitari" (AASS l.50512-50514), "Equidem horum omnium me insimulandum cognoscens" (l.50524-50525), the margin "S. Stephanus Poeta statim post rem gestam, scilicet post Pascha anni 797" (l.50373-50387) and Graf's "durch Beduinen" (GRAF l.646). Verified.
- Ishoyahb: "quae ei prae Amro propria sunt uncinis inclusa" (AMR l.6398-6400), "Jesujdbiis hazzensis" (l.13282), "Jesujabus hazzensis" (MARI l.13481), "nono foculo iueun- te" (ASS31 l.78624-78625), "quem regina Persarum Boran" (DUV l.110) and "écrit entre 832 et 850" (LABOURT l.17234). Verified.

**Audio.** All three audio files equal the brief, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph; score.py's rebuild changed nothing. All three cards and records.json parse and end with a newline.

**Scores.**

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| theodore-abu-qurrah | 338 | 2:04 | 8.2 | 62.0 |
| stephen-of-mar-saba | 337 | 2:04 | 6.2 | 75.5 |
| ishoyahb-iii | 338 | 2:04 | 7.1 | 66.0 |

All three are inside about 2:05, so no README reason is needed. The README's "333 to 338" holds. None of my fixes adds a word to a brief.

**Round 1 findings.**
- R1-BB1 (Theodore, Janah): confirmed applied. "He wrote it for Janah, whom Graf takes to be a bishop" matches GRAF l.14097-14114.
- R1-BM1: confirmed. The label now sits with Abu Ra'ita.
- R1-BM2: confirmed.
- R1-BM3: applied, but the new "his" is unclear aloud (R2-BM1).
- R1-BM4: confirmed.
- R1-BM5: applied with change, confirmed. The added l.122148-122150 is right: it is where the notice says it follows Turrianus.
- R1-BM6 (Stephen, the margin's 797): applied with change. The margin wording is right, but the fix kept "796 in their text" as the Bollandists' year. The volume itself contradicts that (R2-BB1).
- R1-BM7: confirmed. The clause begins at l.50512, and l.50524-50525 apply it to Stephen.
- R1-BM8: confirmed (GRAF l.645-647).
- R1-BM9: applied with change, confirmed. Gismondi does call the bracketed lines "a Sliba addita" (AMR l.6391), so "additions" is his word.
- R1-BM10: applied with change. "it" can still be heard as the eagle story (R2-BM3).
- R1-BM11, R1-BM12, R1-BM13, R1-BM14, R1-BM15: confirmed.
- R1-BM16, R1-BM17 (README): confirmed.
- R1-BM18 (README): applied, but it rests on the same 796 reading (R2-BB2).
- R1-CM8, Stephen part (not applied in round 1): ruled below as R2-BM2. Every "No source" claim holds for all of cic/texts, and one "only" claim does not.

## theodore-abu-qurrah

**Verdict:** pass, one minor.

**R2-BM1 (brief para 6: a pronoun from the R1-BM3 fix).** "Michael the Syrian, a Jacobite chronicler who died in 1199, tells of Theodore in Armenia. Graf gives his account in German." Aloud, "his" follows "Theodore", so it can be heard as Theodore's account. The account is Michael's: "der folgendes zu erzählen weiß" (GRAF l.906). Graf's own note cites Chabot for it (l.908).
- Brief and audio: "Graf gives his account in German." → "Graf gives Michael's account in German." (Same word count, 338.)
- Records: no change.

Checked and sound: the Abu Ra'ita sentence (GRAF l.843-844, l.857-858 "den Philosophen", l.870-877); the card `dates` absence, which the records' `absent_details` back with an all-texts search; the Turrianus third side (PG97 l.122124-122125, l.122148-122150; PG94 l.116609-116611).

## stephen-of-mar-saba

**Verdict:** one blocking here and its README counterpart (R2-BB2), two minor (R2-BM2, R2-BM4). The coordinator's standing rulings hold:
- He is a Who under the recorders rule. His thin life is flagged on the card, and R2-BM2 keeps that flag without the false "only".
- The card name is "Stephen of Mar Saba".
- "Mansur" is dropped. My search finds no held line giving him the name.
- The Wonderworker is named apart in the brief (para 3) and on the card (`otherNames[1]`, "Which Stephen").
- "Every held date placing given" fails until R2-BB1 is applied.

**R2-BB1 (brief para 4, card `dates`, card `uncertain` "The year", records: the Bollandists' year is 797, and 796 is one scan figure).** The R1-BM6 fix tells the Bollandists as making the raid 796 "by their own count", with 797 only in their margin. The same volume gives their year as 797 in two more places:
- **Their essay on Theophanes's chronology.** It opens the volume (AASS l.667, "Observationes ... ad S. Theophanis Chronographiam") and is the essay the commentary cites ("juxta ea quae ad Theophanis Chronologiam notavimus", l.50454-50455). It treats these very martyrs: "vide xx Martii probatum in Martyribus Sabaitis, quorum coaevus scriptor ... non potuisset scribere eos mortem oppetiisse anno ab orbe condito [6288], a Christi Incarnatione [788], Indictione v : cum quinta Indictio annum nostrum pccxcvir signet" (AASS l.2739-2750; scan "pccxcvir" for DCCXCVII). Migne's reprint, headed "GOD. HENSCHENII DISSERTATIO", reads "cum quinta indictio annum nostrum 797 signet" (PG108 l.104846-104858, l.104766).
- **The volume's chronological index.** "INDEX CHRONOLOGICUS TOMI III MARTII" (l.9259) has ". 797 Martyres xx mon: chi Laurg S. Sabze" (l.9493, scan).
- **The commentary's own figure.** It reads "annum nobis pccxcvi signant" (l.50455). Its own reason follows: one year must be added to the Alexandrian count, "itaque ad Indictionem indicatam pervenitur" (l.50455-50460). The fifth indiction is the year the essay calls 797. The scan figure is the outlier.

The "only their margin" reading, and the card's inference that the Christopher note "also points to 796", rest on that one scan figure. As drafted, the profile says the Bollandists hold 796 while the volume they edited says 797 twice more. That leaves out held placings and misstates the editors' side.

Fixes (each checked against the lines above; no "X, not Y", no sentence past 25 words):
- Brief and audio, para 4: "The Bollandists, by their own count of the years, make it 796." → "The Bollandists, by their own count of the years, make it 797." (337 words, unchanged.)
- Card `dates`: "The Bollandists, the seventeenth-century editors of the Acta Sanctorum, make it 796 in their text." → "The Bollandists, the seventeenth-century editors of the Acta Sanctorum, make it 797, the year the fifth indiction marks (one figure in the scan of their commentary reads 796)." The rest of `dates` follows R2-BM2.
- Card `uncertain` "The year": "The Bollandists, by their own chronology, make it 796 in their text, while their margin has him writing soon after the raid, just after Easter of 797. Their note on the martyr Christopher, a convert from Persia whom Stephen names, puts his death in 789 (the scan reads 189), seven years before the twenty, which also points to 796." → "The Bollandists, by their own chronology, make it 797, the year the fifth indiction marks. One figure in the scan of their commentary reads 796. Their margin has him writing soon after the raid, just after Easter of 797. Their note on the martyr Christopher, a convert from Persia whom Stephen names, puts his death in 789 (the scan reads 189), seven years before the twenty." The Graf sentence stays as it is.
- Records `claims`, "Bollandists' text": change the gloss "(scan: DCCXCVI = 796)" to "(scan: DCCXCVI = 796; the commentary goes on to add one year to the Alexandrian count to reach the fifth indiction, which the volume's essay on Theophanes makes 797)". Witness → "l.50454-50460".
- Records `claims`, add: `{"claim": "Essay on Theophanes's chronology, opening the volume (\"OBSERVATIONES PERQUAM UTILES AD 5. THEOPHANIS CHRONOGRAPHIAM\" (scan)): \"vide xx Martii probatum in Martyribus Sabaitis\"; \"cum quinta Indictio annum nostrum pccxcvir signet\" (scan: DCCXCVII = 797)", "witness": "AASS (acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt), l.667, l.2739-2750", "formation_confidence": "Contested"}`
- Records `claims`, add: `{"claim": "Chronological index: \"INDEX CHRONOLOGICUS TOMI III MARTII\"; \". 797 Martyres xx mon: chi Laurg S. Sabze\" (scan)", "witness": "AASS (acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt), l.9259, l.9493", "formation_confidence": "Contested"}`
- Records `contested_claims` "The year of the raid": replace sides 2 and 3 with one side: "The Bollandists: 797, the year of the fifth indiction, in the volume's essay on Theophanes (AASS l.2739-2750), its chronological index (l.9493) and their margin, which has Stephen writing just after Easter of 797 (l.50373-50387); one figure in their commentary reads DCCXCVI, 796, in the scan (l.50454-50455); their note e puts Christopher's death seven years before (l.53478-53480)". The Acts and Graf sides stay.

**R2-BM2 (R1-CM8 ruling: "used here" in `dates`, `place`, `uncertain` "His name" and "Which Stephen").** "Used here" is drafting language on reader-facing text and goes. Before accepting any "No source", I searched all of cic/texts (Method). The only Stephens tied to Mar Saba are these:
- **The Wonderworker**, John of Damascus's nephew: Le Quien, "in Vita Stephani Sabaitae, qui filius fuit fratris S. Joannis Damasceni" (PG94 l.5332-5335, also l.35211); PG99 l.72016, l.72454; the Analecta Bollandiana note (l.7994); Papadopoulos-Kerameus t.4 l.12941-12962; Nikodemos vol. 2 index, "Στέφανος ΣαββαΙττις Ίουλ." (l.58027).
- **A Stephen the Sabaite on 28 October.** Le Quien calls him "μαθητοῦ τοῦ ἁγίου Σάββα", a disciple of Saint Sabas (PG94 l.8858-8860). PO 15 has "Etienne, disciple du saint Sabas" (l.41678).
- **Nikodemos's 28 October Stephen the Sabaite** (vol. 1 l.23272-23316). He became a monk young, "ἤκμαζεν ἐν ἔτει ψϞ' (790)", was made a bishop, worked wonders and "ἐν εἰρήνῃ πρὸς Κ[ύριον] ἐξεδήμησεν". Nikodemos does not tie him to the Passion or to its hymns (see R2-BM4).

No held line gives the Passion's author a birth, a death, a birthplace or kinship with John of Damascus. So "No source gives…" is true of the Library in `dates`, `place` and "Which Stephen". One sentence is not true: "Of his own life, only what he says himself is known". The same card reports what others say of him: the Life's "glory and ornament", the Typikon's feast and the Bollandists' canons. The sentence is also a colon reveal.

Exact replacements:
- `dates`: "No source used here gives his birth or death" → "No source gives his birth or death".
- `place`: "No source used here gives his birthplace" → "No source gives his birthplace".
- `uncertain` "His name": "which take it from a Life of Stephen the Wonderworker that is not among the sources used here. Of his own life, only what he says himself is known: he was a monk of Mar Saba, he was there in the raid, he wrote at Abbot Basil's order, and he wrote hymns for the martyrs." → "which take it from a Life of Stephen the Wonderworker that the Library does not hold. For his own life, his account is the main witness. It says he was a monk of Mar Saba who saw the raid and wrote at Abbot Basil's order. It ends with him singing hymns to the martyrs." "the Library does not hold" is the form other live cards use. Sources: l.50539-50542, l.50524-50536, l.53326-53328 ("accinentis hymnos").
- `uncertain` "Which Stephen": "No source used here makes the writer a relative of John of Damascus." → "No source makes the writer a relative of John of Damascus."
- Records `absent_details`, "Birth, family, age, office, death, burial": replace the note with "Searched all of cic/texts for Stephan/Stephanus/Stefanos/Στέφαν/Étienne/اسطفان with Saba/Sabas/Sabaita/Σαββαΐτ/Mar Saba, with Poeta/ποιητ/melod/hymnograph and with Thaumaturg, including OCR line splits: nothing for the author. Namesakes: the Wonderworker (PG94 l.5332-5335, l.35211; PG99 l.72016, l.72454; Papadopoulos-Kerameus t.4 l.12941-12962); a 28 October Stephen the Sabaite, a disciple of Saint Sabas by Le Quien (PG94 l.8858-8860), and a bishop flourishing in 790 by Nikodemos, vol. 1 l.23272-23316, who does not tie him to the account."

**R2-BM4 (card `uncertain` "Which Stephen": a held namesake close to the Poet's feast).** The Bollandists report the Poet's feast in the Typikon on 27 October (AASS l.50435-50438). Nikodemos keeps a Stephen the Sabaite on 28 October, a bishop who flourished in 790 (vol. 1 l.23272-23296). A listener reading "Which Stephen" should know he exists, and that no source makes him the writer.
- Card: add at the end of "Which Stephen": "Nikodemos the Hagiorite keeps a Stephen the Sabaite on 28 October, a bishop and wonderworker who flourished in 790. He does not tie him to the account."
- Card `sources.about`: add `{"title": "Synaxaristes, volume 1 (September to February), 28 October", "author": "Nikodemos the Hagiorite", "date": "1900", "language": "Greek", "file": "cic/texts/nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt"}`.
- Records `claims`, add: `{"claim": "Nikodemos, 28 October: \"ΣΤΕΦΑΝΟΥ τοϋ Σαΰΰαίτου, τοΰ χαϊ 'Κταοχύιχου γενομέγον\" (scan, for Σαββαΐτου ... Ἐπισκόπου); \"ήκμαζεν έν ετει ψ/ (790)\"; \"ήξιώθη καί τοϋ χαρίσματος της άρχιερωσύνης\"; \"χάριν παραδόξων θαυμάτων\" (scan); no link to the Passion", "witness": "NIK1 (nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt), l.23272-23299", "formation_confidence": "Documented"}`.

## ishoyahb-iii

**Verdict:** pass, one minor.

**R2-BM3 (brief para 2: "it" after the R1-BM10 fix).** "Thomas of Marga tells the story in his history of the house ... Thomas says parts of it came down by the monastery's tradition." Aloud, "it" can be heard as the eagle story. Thomas ties tradition to the casket at Antioch (TOM l.5687-5690) and to the Apamea sorcerer (l.5750-5751), and never to the vision. The card says "parts of it" of the book, where the referent is clear.
- Brief and audio: "Thomas says parts of it came down by the monastery's tradition." → "Parts of the history, Thomas says, came down by the monastery's tradition." (Same word count, 338.)
- Records: no change.

Checked and sound: "Beth 'Abhe" throughout, Budge's form (57 hits in TOM); `otherNames[3]` with Gismondi's bracket rule and the unbracketed "Jesujdbiis hazzensis" (AMR l.13282, l.6398-6400; MARI l.13481); the `knownFor` letters (DUV l.230-232); Duval on the Boran side (DUV l.108-111); `uncertain[0]` with the three placings of Thomas (TOM l.94; LABOURT l.17234; ASS31 l.78624-78626); "In it, Ishoyahb blamed Simeon" (DUV l.8715-8747).

## README

**R2-BB2 (Live census mentions, Stephen, and Corrections to the re-score, Stephen l.160: the 796/797 reading, which R2-BB1 changes).** The census bullet says "the Bollandists' text 796 (l.50452-50455); only their margin, which has him writing straight after the raid, just after Easter of 797". The essay (AASS l.2739-2750) and the index (l.9493) make the "only" false. The census's "20 March 797" then agrees with the Bollandists.
- Census bullet: "\"March 797\": the Acts give AM 6288, 788 (l.50556-50557); the Bollandists' text 796 (l.50452-50455); only their margin, which has him writing straight after the raid, just after Easter of 797 (l.50373-50387). The profile gives all three." → "\"March 797\" agrees with the Bollandists, who make it 797 in the volume's essay on Theophanes (l.2739-2750), its chronological index (l.9259, l.9493) and their margin (l.50373-50387); one figure in the scan of their commentary reads 796 (l.50454-50455). The Acts give AM 6288, 788 (l.50556-50557), and Graf gives 796 or 797 (GRAF l.645-646). The profile gives each placing."
- Corrections, Stephen (l.160): "The 796 has company: the Bollandists' margin has him writing straight after the raid, just after Easter of 797 (l.50373-50387), which, read so, puts the raid in 797; Graf gives \"796 or 797\"." → "The re-score's \"Bollandists reckon 796\" rests on one figure in the scan of their commentary (l.50455). The volume's essay on Theophanes (l.2739-2750) and its chronological index (l.9493) give 797, the year of the fifth indiction, and their margin has him writing just after Easter of 797 (l.50373-50387). Graf gives \"796 or 797\"."

**Note, not a finding (Names and ids, Stephen; Who the sources are, Stephen).** No change is needed for "Stephen the Poet". It stays a note for Mark, as ruled (README l.67), and its cites (l.50431-50433, l.50436-50438) are right. The sources bullet's "a Life of Stephen the Wonderworker that is not held" is true across the Library. This is recorded only so the next round does not reopen it. It is not a finding, and I do not count it.

Checked and sound: the Theodore and Ishoyahb census and Other-profiles bullets after R1-BM16 and R1-BM17; the Beth Abe/Beth 'Abhe note; the 333 to 338 range.

**Verdict.** 2 blocking: R2-BB1 (Stephen: the Bollandists' year is 797, with held placings missing) and R2-BB2 (README, the same). 4 minor: R2-BM1 (Theodore pronoun), R2-BM2 (the R1-CM8 ruling, with exact replacements), R2-BM3 (Ishoyahb "it") and R2-BM4 (Nikodemos's 28 October Stephen). Theodore and Ishoyahb pass. Stephen passes once R2-BB1 and R2-BM2 are applied.

## Era 4 Who batch 11, round 2 review: PART C

**Scope.** A targeted recheck of round 1's changes to `al-tabari` and `ibn-ishaq` (brief, card, `records.json` entry, audio), and of the README as a whole: opening, Majors and lengths, River and tradition counts, census bullets, Other profiles, Who the sources are, Corrections to the re-score, Card traditions, Language and quotations, and every item in R1_changes.md's "README: round 1 changes" log (Parts A, B and C, and "Found while applying"). Untouched text was not re-reviewed, except where I tripped over a plain error.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md (with its checklist), lessons.md, R1_review.md (Part C and the README sections of Parts A and B) and R1_changes.md (Part C and the README log). I read `git diff 3e085559 HEAD` for both people's files, records and the README. Every changed string was reopened in context with sed in cic/texts: T4, T5, HITTI, WEIL, MOBERG, QUATREMERE, Michael the Syrian (Chabot), ELIAS, EVETTS, GINZEL. For the README log I reopened MAC (l.749-757, 877-918, 15152-15200), ZAK (l.26010-26021), ALV (l.31683-31716), ASS31 (l.78620-78627), LABOURT (l.17232-17236) and AASS (l.50373-50388, 50429-50439). I walked census.json (release 44) by script for the era 4 major counts by `laneLabel`, the outside-witness lanes and `toldWithin`, every census path the README log added, and the Beth Abe / Beth 'Abhe, Taronites and "executed in 859" paths. I grepped Who-Profiles and Council-Profiles for Tabari / Jarir / Abu Ja'far and for Ibn Ishaq / Ibn Hisham outside batch 11. A script counted sentences past 25 words in both briefs and every card field. score.py was run; the audio files were compared with the briefs by script before it rebuilt them.

**Quotations.** Every changed or added quotation is verbatim within its cited range:
- al-Tabari card `uncertain[1]`: Hitti "what has been once well said need not be told again" (HITTI l.615-616). Verified.
- al-Tabari card `keyWorks[1]`: "Daniel and his men" (MOBERG l.2824). Verified, unchanged.
- al-Tabari records: Quatremère/al-Maqrizi "plus de vingt exemplaires de cette chronique, du nombre desquels il y en avoit un écrit de la main de l'auteur" (l.14050-14053; the "il j en" scan is marked). Verified. Michael "Alors, Yezdegerd, dernier roi des Perses" (l.32600). Verified. Prym "Narratori duas inter se diversas relationes confusas esse perspicuum est" (T5 l.23986-23987). Verified. Moberg "even the Muhammadan interpreters do not agree, at least not unanimously" (l.2817-2818). Verified.
- Ibn Ishaq brief: Moberg "anything that suggests an independent Muhammadan tradition of historical value." (MOBERG l.2694-2695). Verified, unchanged.
- Ibn Ishaq records: the new Weil, Hitti/al-Baladhuri, nisba, Waraqa and revolt quotations hold (WEIL l.140-148, 300-301, 3285, 24250, 4532-4533, 5365-5369, 6686-6705, 8883-8884, 9565-9597; HITTI l.15759-15791, 15805-15806). Two ranges miss their lines (Ibn Ishaq M2).
- A note on a round 1 claim: R1_changes says the card's old "Almuttalebij" "is not in Weil". It is, hyphenated across a line: "Mohammed Ibn Ishak Almutta- / lebij" (WEIL l.257-258). The new "Almuttalabij" (l.301) is also held, so the card is right either way. Nothing to fix.

**Audio.** All eight audio files equaled their briefs, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph, before score.py rebuilt them. All files end in a newline, and all JSON parses.

**Scores.** (words; minutes at 162.5 wpm; FK; Flesch)
- al-tabari: 333; 2:02; 6.7; 68.7
- ibn-ishaq: 338; 2:04; 6.7; 69.5
- eulogius-of-cordoba: 337; 2:04; 6.8; 69.8
- ishoyahb-iii: 338; 2:04; 7.1; 66.0
- paulus-alvarus: 336; 2:04; 7.9; 63.3
- stepanos-of-taron: 336; 2:04; 6.6; 70.1
- stephen-of-mar-saba: 337; 2:04; 6.2; 75.5
- theodore-abu-qurrah: 338; 2:04; 8.2; 62.0

All pass FK ≤ 10 and Flesch ≥ 60. None is past 338 words, so none needs a README length reason. Every sentence in both of my briefs is 24 words or fewer. Ibn Ishaq sits at the 338 ceiling, so the Ibn Ishaq fixes below are word-neutral. The al-Tabari fix adds three words (336).

**Round 1 findings.**
- R1-CB1 (Quatremère is al-Maqrizi's account): applied correctly. "Egyptian historian" was rightly dropped, since QUATREMERE does not say it. The new wording has a gap in time and referent (al-Tabari M2).
- R1-CB2 (single-witness tags): applied. Ginzel's claim is now Dominant Modern Reconstruction and Quatremère/al-Maqrizi is Documented. Hitti l.911-914 keeps Widely Accepted on his two named Arab lives, following the batch 8 precedent. Confirmed.
- R1-CM1 (Aelia): applied. Confirmed.
- R1-CM2 (pronouns, castles): applied with change. The new wording renders T4 l.1495 fairly, but "the killing" now has no antecedent (al-Tabari M1).
- R1-CM3 ("last"): applied, first option. MICHAEL l.32600 verified, with a records claim and a `sources.about` entry. Confirmed.
- R1-CM4 (Moberg's majority): applied with change ("Muslim", from "Muhammadan interpreters", l.2816-2819). Confirmed.
- R1-CM5 (Hitti's rule): applied with change, as held English. Verified. Confirmed.
- R1-CM6 ("in most years"): applied. ELIAS l.7329-7668 has 21 Tabari citations. Confirmed. The sentence runs 29 words (al-Tabari M4).
- R1-CM7 (the chain): applied with change. Confirmed against T4 l.673-674, 697-727, 1502, 1533, 5549 and 6769. The contested claim's second side now carries the chain. On the coordinator pointer in R1_changes ("both garbled"), my ruling is that the card stands. At l.6769, "سلمة" and "بن اسحاق" are legible and only the first name is garbled. At l.5549, "عن ابن اسحاق" is legible after a garbled name. The records tag the identification at l.673-674 Inferential-Thin, and the card says plainly that the name is unreadable. No change needed.
- R1-CM8 (ranges): applied. T5 l.910-912 and l.5838 verified. Confirmed.
- R1-CM9 (scan marks): applied. Confirmed.
- R1-CM10 (Prym's note): applied with change. The text is tied to the page and not to one telling, which is the honest reading of T5 l.23955-23987. Confirmed. The new first mention of Prym causes a small doubling (al-Tabari M3).
- R1-CB3 and R1-CM1 (two audiences; Ja'far son of Abu Talib): applied with change. WEIL l.9374-9379 and l.9438-9459 verified. "Next day" matches "Am andern Morgen" (l.9438). Confirmed.
- R1-CB4 (`place`): applied. HITTI l.646-648 verified. Confirmed.
- R1-CB5 (Yasar): applied with change. HITTI l.15759-15791 verified. The fixer was right to leave out a causal link between Yasar's patron and the nisba. Confirmed. The new `otherNames[1]` adds al-Baladhuri's death year without records support (Ibn Ishaq M3).
- R1-CB6 (a reputation Weil reports): applied. WEIL l.140-146 verified on brief and card. Confirmed.
- R1-CB7 (tags): applied. Confirmed.
- R1-CM2 (Evetts's role): applied with change. EVETTS l.5637-5640 verified. The note has no "(A. J. B.)" mark, so it is Evetts's. Confirmed.
- R1-CM3 ("some", not "much"): applied in brief, card and contested side. Confirmed.
- R1-CM4 (long sentences): applied. Confirmed.
- R1-CM5 (Moberg's why): folded in. The tightened wording widens Moberg's scope (Ibn Ishaq M1).
- R1-CM6 (Hitti source title): applied, "introduction and text". Confirmed.
- R1-CM7 (Waraqa): applied with change. WEIL l.6686-6705 shows Waraqa meeting Muhammad at the Kaaba, so the fixer's range is right. Confirmed.
- R1-CM8 ("used here" on the Ibn Ishaq card): applied. Confirmed.
- R1-CM9 (Faymiyun ranges): applied with change, but the range still misses two quoted lines (Ibn Ishaq M2).
- R1-CM10 ("a wife of Muhammad"): applied. Confirmed.
- R1-CM11 (the Negus's later turn): applied with change. The new text misreports the event (Ibn Ishaq B1).
- R1-CM12 (scan marks): applied. Confirmed.
- README R1-CB8 (two counting rules): applied with change. It is verified by census walk: era 4 `major` rows by `laneLabel` are LW 10, GE 5, SEA 4, Caucasus 1, Africa 1. It agrees with the batch 9 README l.11, the batch 10 README l.13 and Open-Gaps 269. The citation is in subject-and-date form. Confirmed.
- README R1-CB9 (outside witnesses' lanes): applied with change. The fixer was right that both cards read "Outside the church". The census puts al-Baladhuri on Syriac East & Asia with `toldWithin` null, Josephus and Tacitus on Origin, Ammianus on Latin West, and Procopius and Agathias on Greek East. Confirmed.
- README R1-CM1 ("(C<n>)" labels, "draft"): applied. The only "draft" left is in "Opus drafted" and the section title. Confirmed.
- README R1-CM2 (al-Tabari requote): applied with change. The comparison is with the al-Baladhuri card's "scarcely judges what he reports" (batch8 card l.35). Confirmed.
- README R1-CM3 (census passages missed): applied. Paths verified: `movements[53]` `relationsSummary`, `voices[0]` and `voices[3]`; `[609]/card/uncertain[4]`; `[569]/card/uncertain[0]`. Not adding "Ja'far son of Abu Talib" to the patterns is right, because "Ja'far" already covers it. Confirmed. One sentence there overstates (README M1).
- README R1-CM4 (Open-Gaps entry): applied, "to be logged at approval". Open-Gaps ends at 272. Confirmed.
- README R1-CM5 (re-score caveats): applied with change. Rescore l.156, l.157 and l.160 verified, and Stephen's "Mark may prefer LISTED" was rightly added. Confirmed.
- README R1-CM6 ("evi"): applied under the "if it stays" branch. The card still has it, and the README lists it (DUV l.222). Confirmed.
- README R1-CM7 (Ibn Ishaq sources): applied. Confirmed.
- README R1-CM8 ("used here" on the Stephen card): not applied, since it is a profile edit. It is still open (README M2).
- README log, Part A: R1-AM-R1 to R5 are applied and true. ALV l.31683-31716 gives Tamayo and Antonio. MAC l.879-882 confirms that Alishan gives no notice of the manuscript's age, l.751-756 Emin from Gregory Magistros, and l.905-908 the Mush tombs. ZAK l.26020 has Brosset's "on ne sait pas quand mourut l'auteur". The `movements[116]` and `movements[72]/voices[0]` paths are verified. "The colophon's Armenian year 453, which Macler reckons as 1004 to 1005" is verified (MAC l.15156, l.15199-15200).
- README log, Part B: R1-BM14 is applied and true: every Beth Abe and Beth 'Abhe path is verified in census.json, and batch 11 writes Beth 'Abhe throughout. R1-BM16 and R1-BM17 are applied: ASS31 l.78623-78625 ("nono saeculo ineunte") and LABOURT l.17233 ("entre 832 et 850") are verified. R1-BM18 is applied: AASS l.50373-50387 margin "statim post rem gestam, scilicet post Pascha anni 797" is verified. The Stephen the Poet option is applied: AASS l.50431-50433 and l.50437-50438 are verified.

## al-tabari

**Verdict:** pass after minor fixes (0 blocking, 4 minor).

**R2-CM1 (brief para 3: "the killing" has no antecedent).** The round 1 fix reads "Priests and monks shouted to the men in the castles, blaming them alone for the killing." The sentence before it says only that Khalid's men "broke into houses and monasteries", so a listener has not heard of any killing. The source has it: "[...] الدور والديرات و واكثروا القاتل فنادى / القسيسون والرعبان يا اعل القصور ما يقتلنا غيركم" (T4 l.1493-1495, scan; "the houses and monasteries, and killed much; the priests and monks cried: people of the castles, none but you is getting us killed"). Fix, brief: "At Hira in Iraq, the commander Khalid ibn al-Walid's men broke into houses and monasteries." → "At Hira in Iraq, the commander Khalid ibn al-Walid's men broke into houses and monasteries and killed many." The sentence is 17 words, and the brief goes to 336 words, about 2:04. Records: none needed, because the Hira claim already carries "واكثروا القاتل ... (scan; the houses and monasteries, and killed much ...)". Restate the README word range afterwards.

**R2-CM2 (card `legacy.traces[2]`: al-Maqrizi has no time, and "the chronicle" has no referent).** "The historian al-Maqrizi, quoted in Étienne Quatremère's French of 1811, tells of the library of the caliph Aziz. Aziz had more than twenty copies of the chronicle, one written in the author's own hand." Without a time, a reader can take al-Maqrizi for a witness of Aziz's court. He wrote four centuries later. A held line dates him: "THE KHITAT OF AL-MAKRIZi (died A. H. 845 = A. D. 1441)" (EVETTS l.15213). "The chronicle" also points to nothing in this item; the card calls the work "Annals", and Quatremère's text says "l'histoire de Tabary ... cette chronique" (QUATREMERE l.14048-14051). Fix: `traces[2]` → "The historian al-Maqrizi (died 1441, by Evetts) is quoted in Étienne Quatremère's French of 1811 on the caliph Aziz's library. Aziz had more than twenty copies of al-Tabari's history, one written in the author's own hand." The first sentence is 21 words. Records: on the Quatremère claim, add "; al-Maqrizi's death: \"AL-MAKRIZi (died A. H. 845 = A. D. 1441)\" (scan), EVETTS l.15213" and add "EVETTS (abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt), l.15213" to the witness. EVETTS is already in `sources.about`.

**R2-CM3 (card `uncertain[3]` and `[4]`: Prym introduced twice, and "the volume" unclear at first mention).** The fix put Prym's first mention in `uncertain[3]` ("E. Prym, the volume's editor"), where "the volume" has no referent. `uncertain[4]` then introduces him again ("E. Prym, who edited the volume in 1893"). Held: vol. V "RECENSUIT E. PRYM", 1893 (records claim 1, T5 l.65-95). Fix: `uncertain[3]`: "On the same page, E. Prym, the volume's editor, notes" → "On the same page, E. Prym, who edited this volume of the Annals in 1893, notes"; `uncertain[4]`: "E. Prym, who edited the volume in 1893, filled part of the text" → "Prym filled part of the text". Records: none.

**R2-CM4 (card `legacy.traces[0]`: a fixed sentence of 29 words).** "The Christian chronicler Elias of Nisibis names al-Tabari's Annals among his Arabic sources, his editors say, and cites him in most years from 275 to 302 of the hijra." Fix: → "The Christian chronicler Elias of Nisibis names al-Tabari's Annals among his Arabic sources, his editors say. Elias cites him in most years from 275 to 302 of the hijra." (ELIAS l.126-128, 7329-7668.) Records: none.

Checked and sound in the new text: Aelia "as Jerusalem was then called" (T5 l.6621-6622; census `edges[49]`). Michael's "last". The Tafsir sentence (MOBERG l.2816-2825). Hitti's rule, verbatim, and "al-Tabari's preface voices it" ("gives expression to that principle", HITTI l.616-617). The Salama chain item (T4 l.669-727; the 90,000 at l.725). Prym's note, tied to the page. The new `sources.about` entry matches the Chabot file header (1901). The new card text has no "X, not Y" contrast, colon reveal, tail or unintroduced name, apart from M2.

## ibn-ishaq

**Verdict:** revise (1 blocking, 4 minor).

**R2-CB1 (card `uncertain[6]`: the Negus's answer to the revolt is misreported).** The round 1 addition reads: "In another report, Ibn Ishaq tells that the Abyssinians rose against the Negus for leaving their faith. In answer, the Negus wrote out the Muslim confession of faith." Read in context, the report says something else. The Negus wrote on a paper, "ich bekenne, dass es keinen Gott gibt ausser Gott, dass Mohammed sein Diener ist und sein Gesandter, dass Jesus sein Diener ist und sein Gesandter und sein Geist und sein Wort" (WEIL l.9573-9576). He hid it: "Er steckte dann diese Schrift in die rechte Seite seines Oberkleids, und zog den Abissyniern entgegen" (l.9577-9578). He laid his hand on his breast and said "ich bekenne, dass Isa, der Sohn Mariams nichts Anderes als diess war, er meinte damit, als in der Schrift, auf welche er seine Hand gelegt, ausgesprochen war" (l.9591-9594). Then "Die Abissynier gaben sich aber zufrieden" (l.9594-9595). The card's "In answer ... wrote out the Muslim confession" turns a concealed paper and a double-edged oath into an open profession made to the rebels. It also drops how the revolt ended. The phrase "for leaving their faith" also tells the Abyssinians' charge ("Du hast Dich von unserm Glauben losgesagt", l.9569) as fact. Fix, `uncertain[6]`, from "In another report" to the end: "In another report, Ibn Ishaq tells that the Abyssinians rose against the Negus for leaving their faith. In answer, the Negus wrote out the Muslim confession of faith." → "In another report, Ibn Ishaq tells that the Abyssinians rose against the Negus, saying he had left their faith. He wrote on a paper that there is no god but God, and that Muhammad and Jesus are each God's servant and messenger. He hid it in his robe and went out to meet the Abyssinians. Laying his hand on his breast, he told them that Jesus, son of Mary, was nothing other than this. By this, Ibn Ishaq explains, the Negus meant what was written on the paper. The Abyssinians were satisfied." (Sentences of 20, 23, 12, 19, 14 and 4 words. "Them" follows "the Abyssinians". The second "he" stays with the Negus.) Records, the revolt claim: after "dass Jesus sein Diener ist ...\"" add "(l.9573-9576); he put the paper in \"die rechte Seite seines Oberkleids\" (l.9577-9578), laid \"seine Hand auf die Brust\" and said \"ich bekenne, dass Isa, der Sohn Mariams nichts Anderes als diess war, er meinte damit, als in der Schrift, auf welche er seine Hand gelegt, ausgesprochen war\" (l.9591-9594); \"Die Abissynier gaben sich aber zufrieden\" (l.9594-9595)". The witness l.9565-9597 already covers these lines.

**R2-CM1 (brief para 5: the tightening widened Moberg's judgment).** "Axel Moberg, who edited a Syriac book on the martyrs in 1924, traces most of the Arabic stories to an older Christian account. In those stories he could not see ..." The round 1 text said "the Arabic stories of the persecution"; the fix dropped "of the persecution". Heard aloud, "the Arabic stories" can now cover the whole book, the Negus scene included. Moberg's judgment covers only "the oldest Arabic tradition on the persecution in Yaman and the first Abyssinian occupation of that land" (MOBERG l.2637-2638) and "These Arabic narratives" (l.2692). The fixer used "most" because the sea death points to the Book of the Himyarites (l.2708-2710). That book is also an older Christian account, so the plural covers it without "most". Fix (word-neutral, the brief stays at 338): "traces most of the Arabic stories to an older Christian account" → "traces the Arabic stories of the persecution to older Christian accounts". Records, the Moberg claim: "their facts owed to the Acta, save the king's death in the sea" → "their facts owed to the Acta, save the king's death in the sea, which suggests the Book of the Himyarites (l.2708-2710)".

**R2-CM2 (records, Faymiyun claim: the range misses two quoted lines).** The claim quotes "ein Zimmermann und Maurer" and "later sold as a slave in Najran". "Maurer" is at WEIL l.1001 ("und Maurer. Den Sonntag ..."), and "in Nadjran verkauft" is at l.1067 ("fallen und aufgegriffen und in Nadjran verkauft"). l.1060-1061 is a page break ("16"). Fix, witness: "l.994-1000, l.1060-1061, l.1091-1093" → "l.993-1001, l.1066-1067, l.1092-1093".

**R2-CM3 (card `otherNames[1]`: a new fact with no record).** The fix adds "al-Baladhuri, a Muslim historian who died in 892", which `legacy.traces[3]` also says. No Ibn Ishaq claim carries the year. Held: "The year 279/892 saw his death" (HITTI l.742). Fix, records: add a claim "Hitti on al-Baladhuri: \"The year 279/892 saw his death\" (card otherNames[1], legacy/traces[3])", witness "HITTI (baladhuri_origins-of-the-islamic-state-v1_hitti1916.txt), l.742", tag Documented. Card: none.

**R2-CM4 (card `knownFor`: a rewritten sentence of 39 words).** Split it, as the al-Baladhuri card's knownFor does: "A Muslim collector of traditions whose life of Muhammad, known only through Ibn Hisham's reworking, tells of Christians who met Muhammad and his first followers: the Negus of Abyssinia, the Christians of Najran, and Waraqa ibn Naufal of Mecca." → "A Muslim collector of traditions whose life of Muhammad is known only through Ibn Hisham's reworking. It tells of Christians who met Muhammad and his first followers: the Negus of Abyssinia, the Christians of Najran, and Waraqa ibn Naufal of Mecca." The colon introduces a list, not a reveal. Records: none.

Checked and sound in the new text: Brief para 1 (WEIL l.9374-9379, 9438-9459). Para 2: "an exile" and Umm Salama (l.9301-9304); Weil's placing (l.140-141); Hitti (l.665-667); Evetts (l.5637-5640). Para 3 keeps both sides of the wording question (Weil l.151-153; Ibn Hisham l.284-296). Para 4: Najran "der erste Ort" (l.985-986) and "Gott weiss welche die Richtige ist" (l.1183). "Like all Christians, Ibn Ishaq says" is the narrator's own "wie alle Christen" (l.16966), not the delegates'. Para 5 keeps Weil's report and his own view apart (l.141-148). `place`, `dates`, the new `uncertain[1]` (HITTI l.15759-15791), `uncertain[0]` and `sources.about[1]`. No "X, not Y" contrast, colon reveal, tail, aphorism or unintroduced name in the new text. Khalid has "the commander Khalid ibn al-Walid", and Ja'far has "son of Abu Talib".

## README

**R2-CM-R1 (Live census mentions, Ibn Ishaq: "These census claims rest on Simeon, the Book of the Himyarites and Procopius").** The sentence follows the `relationsSummary`, `voices[0]` and `voices[3]` items, but only `documentedStories[1]` lists those three sources (census `movements[53]/documentedStories[1]/sources[0-2]`). `relationsSummary` and `voices` cite nothing, and the entry's own `sources` are the Ezana inscriptions, the Garima Gospels, Cosmas, Munro-Hay and Phillipson. Fix: "These census claims rest on Simeon, the Book of the Himyarites and Procopius, not on him." → "The story's sources are Simeon, the Book of the Himyarites and Procopius, not him; `relationsSummary` and `voices` cite none."

**R2-CM-R2 (cross-batch, R1-CM8 still open: "used here" on the Stephen card).** The stephen-of-mar-saba card still reads "No source used here gives his birth or death" (`dates`), "No source used here gives his birthplace" (`place`), "a Life of Stephen the Wonderworker that is not among the sources used here" (`uncertain` "His name") and "No source used here makes the writer a relative of John of Damascus" (`uncertain` "Which Stephen"). lessons.md lists "used here" as drafting language not allowed in participant text, and the Ibn Ishaq card now reads "No source gives". The batch is therefore inconsistent. The batch 8 al-Baladhuri and batch 10 Ilarion cards still use the older form, which is a cross-batch matter for the coordinator, not this batch. Fix (Part B's file, or the coordinator): "No source used here gives" → "No source gives" (twice); "that is not among the sources used here" → "that is not held"; "No source used here makes" → "No source makes". Each now-universal absence must rest on a search of all cic/texts, recorded in the Stephen `absent_details`. If that search has not been run, run it before the edit. No README text changes.

Checked and true: the opening; Majors and lengths (333 to 338 words; Rescore l.156, 157 and 160 quoted in the Rescore's own terms); both river counts and the card-tradition counts, verified against census.json and against the batch 9, batch 10 and Open-Gaps 269 wording; the by-river and by-tradition lists; the lane sentence on outside witnesses; every census path the round 1 log added; Other profiles for both people (grep finds no Tabari, Ibn Ishaq or Ibn Hisham outside batch 11; `claims[5]` is the Medina claim); Who the sources are for both; the Corrections for l.156 and l.157; Card traditions; Language and quotations ("evi" listed; the card's new Hitti quotation is held English and needs no entry). The Part A, Part B and "found while applying" README items listed above are applied and true. If round 2's fixes change any brief, restate the word range in Majors and lengths: al-Tabari becomes 336 after R2-CM1, and Ibn Ishaq stays at 338.

**Verdict.** al-tabari passes after minors. ibn-ishaq needs one more fix (R2-CB1). README passes after minors. Blocking: 1 (ibn-ishaq 1). Minor: 10 (al-tabari 4, ibn-ishaq 4, README 2).

