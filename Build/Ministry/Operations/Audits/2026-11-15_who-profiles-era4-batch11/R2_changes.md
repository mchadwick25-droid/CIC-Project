# Era 4 Who batch 11: round 2 changes

Three fresh Opus fixers, run one at a time, applied the round 2 findings. Part A: 9 findings, 6 applied as worded, 3 with change. Part B: 6 findings, 2 as worded, 4 with change. Part C: 8 findings, 6 as worded, 2 with change. None was refused.

## Era 4 Who batch 11, round 2, Part A: changes

Every source line below was reopened with `sed -n` before the fix. Audio files were updated with their briefs and still equal the brief plus "[calmly] " and "[warmly] ". `records.json` was dumped with the file's existing `indent=1` (ensure_ascii=False, final newline), not indent=2: the file at HEAD is indent=1, and indent=2 would rewrite all 2,048 lines, other parts' entries included. The diff on records.json is 4 lines. The worker may want to settle which indent the brief means.

## stepanos-of-taron

- R2-AB1: applied with change. The source holds: CHAB l.38282-38284 ends "(J. M,)"; the title gives Chabot as J.-B. Chabot (l.1, l.50); he credits "M. J. Marquart" for notes in this block (l.38314-38315). The reviewer's wording kept "his account" right after "Michael the Syrian's Chronicle", so "his" would point to Michael aloud. New card `legacy/traces[2]` second sentence: "A note in Jean-Baptiste Chabot's French edition of Michael the Syrian's Chronicle points to Stepanos's account of the synod of Manazkert." I do not name J. M. as Marquart on the card, since the note does not spell out the initials. Records `claims[28]`: claim now opens "A note signed (J. M.) in Chabot's edition, on Manazkert: \"Sur ce concile, cf. le récit d'Etienne Asolik, trad. Dulaurier, p. 131\""; witness "l.38282-38284". Independent re-confirmation still needed (blocking).
- R2-AM1: applied. Brief and audio: "In his youth, Stepanos writes, he saw some great teachers in their old age." Note: the source line is at MAC l.4346 ("Dans notre jeunesse"), not l.4302-4304 as the review says. Records `claims[7]` already cites l.4346-4348, so it needs no change.
- R2-AM2: applied. Brief and audio: "Marie-Félicité Brosset, who put an Armenian chronicle into French, wrote in 1876 that no one knows when Stepanos died." (ZAK l.26019-26020.)
- R2-AM3: applied. Card `uncertain[3]`: "Emin, from a letter of Gregory Magistros, had him alive between 1041 and 1045 and dying at about 117 or 129. Malkhasiants found that age wholly unlikely. Macler answers that Gregory wrote for years after, so one could as well say Stepanos was still alive at that later date." (MAC l.740-756.) The item's closing "Brosset, in 1876, said no one knows when he died." now follows a sentence whose subject is Stepanos, so "he" resolves. Records: no change.
- R2-AM4: applied with change. With the reviewer's wording, "says he was thought to be a cantor" came straight after "Stephen of Taron the historian two men", so "he" could mean either of the two men. I also put the two Alishan points in the source's order: the cantor line comes first, then the list (MAC l.788-793). New text in card `uncertain[5]`: "Alishan says Stepanos was thought to be a cantor from Taron; one word in the scan of that line is garbled. Alishan also cites a list that makes Asolik the vardapet and Stephen of Taron the historian two men. Macler doubts the list." Records: no change.
- R2-AM5: applied. Records `claims[25]` witness: "l.975-976, l.15210-15214". The quote "qui régnérent à Ani" is at MAC l.976, and the line opening that sentence is l.975.
- R2-AM6: applied. Card `uncertain[6]`: "F. C. Conybeare, in his Rituale Armenorum (1905), placed the writing between 991 and 1019, as Macler reports (the scan of Conybeare's page reads 19190)." The book's date of 1905 holds against CONY l.6 ("Clarendon Press, 1905"), and Macler's paraphrase is at MAC l.799-801. Records: no change.

## eulogius-of-cordoba

- R2-AM7: applied. Brief and audio: "Eulogius was a priest of the church of St Zoilus in the 800s, when Muslim emirs ruled Cordoba." "Cordube civitatis" is at EUL l.56819; the review says l.56818, one line off. Records: no change.

## paulus-alvarus

- R2-AM8: applied with change. The reviewer's "..., now in the cardinal's library at Rome" leaves "now in" hanging on "Madrid". I split it into two sentences, which ALV l.31029-31036 and l.31058-31063 support. New card `legacy/traces[0]` close: "Antonio's own copy came from one in Cardinal Barberini's library at Rome. Tamayo de Vargas had given it to the cardinal at Madrid." Records `claims[27]`: "given to Barberini at Madrid \"ab eodem ..." → "given to Barberini at Madrid, \"Matriti, dum ... legatus\", \"ab eodem ...". "Matriti, dum" is at l.31036 and "legatus" at l.31059, both inside the cited ranges l.31019-31036 and l.31058-31075.

## Final word counts and scores (score.py)

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| stepanos-of-taron | 336 | 2:04 | 6.7 | 69.1 |
| eulogius-of-cordoba | 336 | 2:04 | 6.9 | 69.5 |
| paulus-alvarus | 336 | 2:04 | 7.9 | 63.3 |

No further tightening was made. Each fix was word-neutral or saved a word, and all three briefs stay inside 320-338 with no side or story cut. The batch range is now 333 to 338, as the README already says.

## README (for the worker)

R2-AM-R1: apply as the reviewer worded it. I checked it against ALV l.31683-31708 (Tamayo "hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre"; his note "non carnis nexu, sed contubernii vinculo"; Antonio "fratrem vere germanum Eulogii alterum Alvarum") and EUL l.68018 ("fratres meos Alvarum et Isidorum").
- "Other profiles", Paulus Alvarus bullet: "appears in no other profile; no profile confuses the two." → "appears in no other profile. The two batch 11 cards give both Tamayo's view that he was Paulus Alvarus and Antonio's that he was another man."
- "Corrections to the re-score", "Alvarus (l.134)": "l.68018 is about Eulogius's blood brother, also named Alvarus, another man." → "l.68018 is about Eulogius's brother Alvarus, whom Antonio holds to be another man and Tamayo took for Paulus Alvarus (ALV l.31683-31716)."
- "Names and ids", Eulogius of Cordoba and Paulus Alvarus: "Eulogius's blood brother, also named Alvarus, is another man." → "Eulogius's brother, also named Alvarus, is another man by Antonio's account; Tamayo took the two for one (ALV l.31683-31716)."

The word-range sentence ("333 to 338") still holds and needs no change.

## Era 4 Who batch 11, round 2, Part B: changes

I edited only the three people's brief, audio, card and records.json entries. Sources reopened with `sed -n`: GRAF l.640-650, l.900-910; TOM l.5684-5692, l.5745-5752; AASS l.665-669, l.1112-1120, l.2725-2756, l.9257-9261, l.9488-9496, l.50365-50392, l.50430-50470, l.50552-50560, l.53418-53425, l.53470-53482; NIK1 l.23268-23326; PG94 l.5331-5336, l.8856-8861, l.35209-35213; PG99 l.72015-72017, l.72453-72455; Papadopoulos-Kerameus t.4 l.12941-12946.

## theodore-abu-qurrah

R2-BM1: applied. Brief and audio, para 6: "Graf gives Michael's account in German." The account is Michael's ("der folgendes zu erzählen weiß", GRAF l.906). Records: no change.

## stephen-of-mar-saba

R2-BB1: applied with change. Every held placing stays on the card: the Acts' AM 6288 / 788 in the fifth indiction; the essay's 797 and the index's 797; the margin's Easter of 797; the commentary's scan figure 796 with its own reasoning; the Christopher note as worded; Graf's 796 or 797. What I checked:
- The essay (AASS l.2736-2750) says the Sabaite writer counted by the Alexandrian era and "annum unum ex more omisisset computare". It also says "cum quinta Indictio annum nostrum pccxcvir signet". The reviewer's l.2739 start leaves out "Alexandrina ZEra utenti-" (l.2736), so I cite l.2736-2750.
- The essay names Theophanes as "Magni-agri in Sigriana Hegumeni Confessorisque" (l.1116-1118). That holds "Theophanes the Confessor".
- The commentary (l.50454-50460) reads "pccxcvi" in the scan. It then says "adjiciendus est annus unus ... itaque ad Indictionem indicatam pervenitur". I give that reasoning as the commentary's own. I make no claim that the figure is a misprint.
- Note e on Christopher (l.53478-53480) gives 789 (scan 189) and "septennio ante horum Patrum passionem". It names no year for the twenty. The card gives the arithmetic plainly and draws no inference from it.
- The reviewer's `dates` sentence ran to 29 words with a parenthesis. I split it in two.
- The reviewer's `uncertain` text left out the essay, the index and the commentary's reasoning. I added them.

New wording:
- Brief and audio, para 4: "The Bollandists, by their own count of the years, make it 797." (337 words.) The brief names whose year this is, and the card carries the rest.
- Card `dates`: "The raid came in the year of the world 6288, AD 788, in the fifth indiction, by his own account. The Bollandists, the seventeenth-century editors of the Acta Sanctorum, make it 797, the year the fifth indiction marks. One figure in the scan of their commentary reads 796. Georg Graf, in 1910, gives March 796 or 797. The Bollandists think Stephen wrote straight after the raiders left, and their margin puts that just after Easter of 797. No source gives his birth or death"
- Card `uncertain` "The year": "The year. His account gives the year of the world 6288, AD 788, in the fifth indiction, when Elias was patriarch of Jerusalem and Basil was abbot. The Bollandists make it 797, the year the fifth indiction marks. They do so in their essay on the chronicle of Theophanes the Confessor and in the volume's index of dates. They say Stephen counted by the Alexandrian era, which runs eight years behind theirs, and left out one year. One figure in the scan of their commentary reads 796. That passage goes on to add the missing year, to reach the fifth indiction. Their margin has him writing soon after the raid, just after Easter of 797. Their note on the martyr Christopher, a convert from Persia whom Stephen names, puts his death in 789 (the scan reads 189), seven years before the twenty. The note names no year for the twenty, and seven years after 789 is 796. Georg Graf, in his 1910 German edition of the Arabic writings of Theodore Abu Qurrah, puts the massacre in March 796 or 797."
- Records `claims`, "Bollandists' text": I added to the gloss the scan quote "nam. Alecandrinz Fre annis octo ram communem subsequenti, adjiciendus est annus unus, Phocz, ob caussam ibi explicatam. detractus, itaque ad. Indictionem indicatam. pervenitur". The gloss now goes on: "the commentary goes on to add one year to the Alexandrian count to reach the fifth indiction, which the volume's essay on Theophanes makes 797". Witness: l.50454-50460.
- Records `claims`, added after the margin claim:
  - The essay claim as the reviewer gave it, plus "Magni-agri in Sigriana Hegumeni Confessorisque" and "et annum unum ex more omisisset computare". Witness: l.667, l.1116-1118, l.2736-2750. Contested.
  - The index claim as the reviewer gave it. Witness: l.9259, l.9493. Contested.
- Records `contested_claims` "The year of the raid": sides 2 and 3 are now one side: "The Bollandists: 797, the year of the fifth indiction, in the volume's essay on Theophanes (AASS l.2736-2750), its chronological index (l.9493) and their margin, which has Stephen writing just after Easter of 797 (l.50373-50387); one figure in their commentary reads DCCXCVI, 796, in the scan, and the passage goes on to add one year to reach the fifth indiction (l.50454-50460); their note e puts Christopher's death in 789 (scan 189), seven years before, and names no year for the twenty; seven years after 789 is 796 (l.53478-53480)". The Acts and Graf sides stay.

R2-BM2: applied with change. I checked each "No source" claim as worded against the reviewer's all-texts search and the namesake lines I reopened. None of the PG94, PG99, Papadopoulos-Kerameus or NIK1 lines ties a Stephen to the Passion or gives its writer a birth, death, birthplace or kinship with John.
- `dates`: "No source gives his birth or death".
- `place`: "No source gives his birthplace".
- `uncertain` "Which Stephen": "No source makes the writer a relative of John of Damascus."
- `uncertain` "His name": "...which take it from a Life of Stephen the Wonderworker that the Library does not hold. For the writer's own life, his account is the main witness. It says he was a monk of Mar Saba who saw the raid and wrote at Abbot Basil's order. It ends with him singing hymns to the martyrs." The change from the reviewer's text is "For the writer's own life" in place of "For his own life". Read aloud, "his" came straight after "Stephen the Wonderworker".
- Records `absent_details` "Birth, family, age, office, death, burial": the note is the reviewer's text, as given.

R2-BM4: applied with change. NIK1 l.23272-23319 says he became a monk young, entered the Laura of Sabas, flourished in 790 ("ψ/ (790)"), was made a bishop ("άρχιερωσύνης"), worked wonders and died in peace. He is not tied to the Passion. I left out the reviewer's "wonderworker" because it would blur him with Stephen the Wonderworker, who is a different entry. I added the date link to the Typikon's 27 October (AASS l.50435-50438).
- Card, end of "Which Stephen": "Nikodemos the Hagiorite keeps a Stephen the Sabaite on 28 October, the day after the Poet's feast in the Typikon. He was a monk of the laura who flourished in 790 and later became a bishop. Nikodemos does not tie him to the account."
- Card `sources.about`: added the vol. 1 Synaxaristes entry as given.
- Records `claims`: added the Nikodemos 28 October claim, inserted after the 20 March Nikodemos claim, and also quoting "εΐσελθών δηλαδή εις τήν Λαύραν τοϋ μεγάλου πατρός Σάββα" (scan) and the Typikon's 27 October. Witness: NIK1 l.23272-23299, l.23319. Documented.

Standing rulings kept: Who under the recorders rule, thin life flagged; card name "Stephen of Mar Saba"; "Mansur" dropped; the Wonderworker named apart; "Stephen the Poet" not adopted as a name.

## ishoyahb-iii

R2-BM3: applied with change. Brief and audio, para 2: "Parts of the history, Thomas says, came down by the monastery's tradition." The source lines are TOM l.5687-5690 and l.5750-5751. The new sentence brought the brief to 339 words, where the reviewer had counted 338, so I tightened para 3 by one word. "Its editor in 1903, Ignazio Guidi," became "Its 1903 editor, Ignazio Guidi,", with the meaning unchanged. Records: no change.

## Final counts and scores (score.py)

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| theodore-abu-qurrah | 338 | 2:04 | 8.2 | 61.7 |
| stephen-of-mar-saba | 337 | 2:04 | 6.2 | 75.5 |
| ishoyahb-iii | 338 | 2:04 | 7.2 | 65.5 |

The audio files equal their briefs, with the tags at the start of the first and last paragraphs. The card and records.json parse and end with a newline. Only these three entries changed in records.json.

## README (for the worker)

The word range at README l.11 ("333 to 338") still holds.

Live census mentions, Stephen (l.27). Replace:
"\"March 797\": the Acts give AM 6288, 788 (l.50556-50557); the Bollandists' text 796 (l.50452-50455); only their margin, which has him writing straight after the raid, just after Easter of 797 (l.50373-50387). The profile gives all three."
with:
"\"March 797\" agrees with the Bollandists, who make it 797 in the volume's essay on Theophanes (l.2736-2750), its chronological index (l.9259, l.9493) and their margin (l.50373-50387); one figure in the scan of their commentary reads 796, and the passage goes on to add one year to reach the fifth indiction (l.50454-50460). The Acts give AM 6288, 788 (l.50556-50557), and Graf gives 796 or 797 (GRAF l.645-646). The profile gives each placing."

Corrections to the re-score, Stephen (l.60, the "Stephen (l.160)" bullet). Replace:
"The 796 has company: the Bollandists' margin has him writing straight after the raid, just after Easter of 797 (l.50373-50387), which, read so, puts the raid in 797; Graf gives \"796 or 797\"."
with:
"The re-score's \"Bollandists reckon 796\" rests on one figure in the scan of their commentary (l.50455), and that passage goes on to add one year to reach the fifth indiction (l.50455-50460). The volume's essay on Theophanes (l.2736-2750) and its chronological index (l.9493) give 797, the year of the fifth indiction, and their margin has him writing just after Easter of 797 (l.50373-50387). Graf gives \"796 or 797\"."


## Era 4 Who batch 11, round 2, Part C: changes

Every cited range was reopened with sed before the edit: T4 l.1490-1496; EVETTS l.15210-15215; QUATREMERE l.14046-14054; ELIAS l.124-129; T5 l.60-96 (title page, "RECENSUIT E. PRYM", 1893); WEIL l.990-1002, 1058-1068, 1090-1094, 9563-9598; MOBERG l.2635-2639, 2690-2712; HITTI l.728-743.

## al-tabari

- R2-CM1: applied. Brief para 3: "At Hira in Iraq, the commander Khalid ibn al-Walid's men broke into houses and monasteries and killed many." (17 words.) T4 l.1494 "الدور والديرات و واكثروا القاتل" holds it. Records: none; the Hira claim (claims[13]) already carries the line. Audio rebuilt by score.py.
- R2-CM2: applied. Card `legacy.traces[2]`: "The historian al-Maqrizi (died 1441, by Evetts) is quoted in Étienne Quatremère's French of 1811 on the caliph Aziz's library. Aziz had more than twenty copies of al-Tabari's history, one written in the author's own hand." EVETTS l.15213 reads "AL-MAKRIZi (died A. H. 845 = A. D. 1441)"; QUATREMERE l.14048-14049 "l'histoire de Tabary". Evetts is introduced in `traces[1]`. Records, Quatremère claim (claims[24]): claim now ends `; al-Maqrizi's death: "AL-MAKRIZi (died A. H. 845 = A. D. 1441)" (scan), EVETTS l.15213`; witness now ends `; EVETTS (abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt), l.15213`.
- R2-CM3: applied. Card `uncertain[3]`: "On the same page, E. Prym, who edited this volume of the Annals in 1893, notes that the teller has plainly mixed two different accounts." `uncertain[4]`: "Prym filled part of the text from two later writers, Mujir al-Din and al-Suyuti." T5 title page verified. Records: none.
- R2-CM4: applied. Card `legacy.traces[0]`: "The Christian chronicler Elias of Nisibis names al-Tabari's Annals among his Arabic sources, his editors say. Elias cites him in most years from 275 to 302 of the hijra." (ELIAS l.126-128 verified.) Records: none.

## ibn-ishaq

- R2-CB1: applied with change. Card `uncertain[6]`, from "In another report" to the end, now reads: "In another report, Ibn Ishaq tells that the Abyssinians rose against the Negus, saying he had left their faith. He wrote on a paper that there is no god but God, and that Muhammad is God's servant and messenger. The paper added that Jesus is God's servant and messenger, his spirit and his word. The Negus hid it in his robe and went out to meet the Abyssinians. They said he had called Jesus a servant, and that they held Jesus to be God's son. Laying his hand on his breast, the Negus said that Jesus, son of Mary, was nothing more than this. The report explains that he meant what was written on the paper. The Abyssinians were satisfied and dispersed." (Sentences of 19, 20, 15, 13, 17, 19, 12 and 6 words.) Changes from the reviewer's wording, and why: (1) the paper's "sein Geist und sein Wort" for Jesus is kept (l.9575-9576); (2) the Abyssinians' charge and creed are added ("Du hast unsern Glauben verlassen und Jesus einen Diener genannt", "Wir sagen, er ist Gottes Sohn", l.9589-9591), because without them "this" in the oath has nothing to play against and the double edge is lost; (3) "Ibn Ishaq explains" → "The report explains": the gloss "er meinte damit ..." sits inside a report Ibn Ishaq has from Djafar ibn Muhammad after his father (l.9567), so its voice is the report's and cannot be pinned on Ibn Ishaq; (4) "The Negus hid it", so the pronoun does not land on Jesus; (5) "and dispersed" for "giengen auseinander" (l.9595). Records, the revolt claim (claims[21]): the Negus's quotation now runs to `... sein Geist und sein Wort" (l.9573-9576); he put the paper in "die rechte Seite seines Oberkleids" (l.9577-9578); the Abyssinians: "Du hast unsern Glauben verlassen und Jesus einen Diener genannt" (scan "onsem"), "Wir sagen, er ist Gottes Sohn" (l.9589-9591); he laid "seine Hand auf die Brust" and said "ich bekenne, dass Isa, der Sohn Mariams nichts Anderes als diess war, er meinte damit, als in der Schrift, auf welche er seine Hand gelegt, ausgesprochen war" (l.9591-9594); "Die Abissynier gaben sich aber zufrieden, und giengen auseinander" (l.9594-9595)`. The witness l.9565-9597 already covers these lines.
- R2-CM1: applied. Brief para 5: "Axel Moberg, who edited a Syriac book on the martyrs in 1924, traces the Arabic stories of the persecution to older Christian accounts." Word-neutral; MOBERG l.2637-2638, 2692-2710 verified. Records, Moberg claim (claims[14]): "... their facts owed to the Acta, save the king's death in the sea, which suggests the Book of the Himyarites (l.2708-2710)".
- R2-CM2: applied. Faymiyun claim (claims[10]) witness: "l.993-1001, l.1066-1067, l.1092-1093". Checked by grep -n: l.993 Mughira, l.996 "Ein frommer, eifriger Christ", l.1001 "und Maurer", l.1067 "in Nadjran verkauft", l.1092-1093 "Diess ist die Tradition des Wahb ... Nadjran".
- R2-CM3: applied. New records claim (appended): "Hitti on al-Baladhuri: \"The year 279/892 saw his death\" (card otherNames[1], legacy/traces[3])", witness "HITTI (baladhuri_origins-of-the-islamic-state-v1_hitti1916.txt), l.742", Documented. HITTI l.734-742 confirms the subject is al-Baladhuri. Card: none.
- R2-CM4: applied with change. Card `knownFor`: "A Muslim collector of traditions whose life of Muhammad is known only through Ibn Hisham's reworking. The book tells of Christians who met Muhammad and his first followers: the Negus of Abyssinia, the Christians of Najran, and Waraqa ibn Naufal of Mecca." "The book" for the reviewer's "It", since "It" would land on "reworking". Records: none.

## Final word counts and scores (score.py, after the edits; audio rebuilt)

- al-tabari: 336 words; 2:04; FK 6.7; Flesch 68.4
- ibn-ishaq: 338 words; 2:04; FK 6.8; Flesch 68.8
- eulogius-of-cordoba: 336; 2:04; FK 6.9; Flesch 69.5
- ishoyahb-iii: 338; 2:04; FK 7.2; Flesch 65.5
- paulus-alvarus: 336; 2:04; FK 7.9; Flesch 63.3
- stepanos-of-taron: 336; 2:04; FK 6.7; Flesch 69.1
- stephen-of-mar-saba: 337; 2:04; FK 6.2; Flesch 75.5
- theodore-abu-qurrah: 338; 2:04; FK 8.2; Flesch 61.7

All pass FK ≤ 10 and Flesch ≥ 60; none past 338.

## README (for the worker)

- Majors and lengths: restate the word range as "336 to 338 words" (all eight briefs now fall in 336-338; al-tabari is 336 after R2-CM1, ibn-ishaq stays 338). If the README gives per-person counts, al-tabari 336.
- R2-CM-R1 (Live census mentions, Ibn Ishaq): replace "These census claims rest on Simeon, the Book of the Himyarites and Procopius, not on him." with "The story's sources are Simeon, the Book of the Himyarites and Procopius, not him; `relationsSummary` and `voices` cite none." (Not re-walked by me in census.json; taken from the reviewer's walk of `movements[53]/documentedStories[1]/sources[0-2]`.)
- R2-CM-R2 / R1-CM8 ("used here" on the Stephen card): Part B has now applied it on the stephen-of-mar-saba card. If the README logs open items, mark it applied by Part B in round 2. No other README text changes. The cross-batch use of "used here" on the batch 8 al-Baladhuri and batch 10 Ilarion cards stays a coordinator matter outside this batch.

## README log (worker)

Applied as the fixers worded them, each matched once in README.md:
- Length line: "After round 1 the eight run 333 to 338 words, about 2:00 to 2:05," → "After round 2 the eight run 336 to 338 words, about 2:04,".
- R2-AM-R1 (three lines: "Other profiles", Paulus Alvarus; "Corrections to the re-score", Alvarus; "Names and ids"): Antonio's side of the brothers question now given as his, with Tamayo's.
- R2-BB2 (Live census mentions, Stephen; Corrections to the re-score, Stephen): the Bollandists' 797 by essay, index and margin, the commentary's scan figure 796 and its own reasoning, the Acts' 788, Graf's 796 or 797.
- R2-CM-R1 (Live census mentions, Ibn Ishaq): "The story's sources are Simeon, the Book of the Himyarites and Procopius, not him; `relationsSummary` and `voices` cite none."
- R1-CM8: applied on the Stephen card by Part B (R2-BM2). No "used here" remains on any batch 11 card or records entry. The README's quotation of the batch 5 Alopen card ("No source used here says") is a quotation of another batch's card, a cross-batch matter for the coordinator.
- quotes.py: bad 2, the two known hits (the folio-marked Evetts quote the README names, and a regex artifact on the Ishoyahb card).
