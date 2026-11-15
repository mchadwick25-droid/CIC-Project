# Round 1 changes: era 4 Who batch 11

Each part was applied by a fresh Opus agent who reopened every cited source line. README findings were applied afterwards in one pass (below).

---

## Era 4 Who batch 11, round 1, Part A: changes

All cited ranges were reopened with sed -n before each fix. Every card fix has a matching records fix in scratchpad/rec/<id>.json. Audio was rebuilt by score.py.

## stepanos-of-taron

- R1-AB1: applied with change. The brief now says "Marie-Félicité Brosset, who put an Armenian chronicle into French, wrote in 1876 that no one knows when he died." The reviewer's "a French scholar of Armenia" is not in any held line. ZAK is his French translation of Zakaria of Agulis (ZAK l.26019-26020). The sentence now opens para 5. "No early source gives his own death" is gone.
- R1-AB2: applied with change. `dates` adds: "J.-B. Emin, his Russian translator, had him die between 1041 and 1045, from a letter of Gregory Magistros; Malkhasiants found the age this gives him wholly unlikely." Brosset there is now "Marie-Félicité Brosset, a French translator of Armenian and Georgian chronicles". The Kartlis file is now in `sources`, which supports "Georgian". `uncertain[3]` adds: "Emin, from a letter of Gregory Magistros, had him alive until 1041 to 1045 and dying at about 117 or 129; Malkhasiants found that age wholly unlikely, and Macler answers that Gregory wrote for years after, so one could as well say Stepanos was alive then." The reviewer had "so the letter fixes nothing". I changed it because Macler's actual point (MAC l.754-756) is "l'on [pourrait] aussi bien dire qu'Étienne de Tarôn était encore vivant à cette date". Records: a new Contested claim cites MAC l.740-745, l.752-756 and l.759-764. Emin is added as a side of "His death".
- R1-AB3: applied. "...and says he was thought to be a cantor from Taron (the scan is garbled at this word)". Records: a new claim quotes MAC l.788-791 with "(scan garbled)". The reviewer's l.789 is off by one: the Alishan sentence starts at l.788. The Family note was added to `absent_details`.
- R1-AB4: applied. `traces[2]` now reads: "Marie-Félicité Brosset, in his French History of Georgia (1849), cites him again and again for dates and events. Jean-Baptiste Chabot, the editor of Michael the Syrian's Chronicle, points to his account of the synod of Manazkert." Both files are added to `sources.about`. New records claims: KART l.12038-12040, l.13891, l.13906-13907; CHAB l.38282-38283.
- R1-AB5: applied. New claims cover the following:
  - the nine manuscripts and the 1859 and 1885 editions (MAC l.222-234, l.370-378);
  - the translations (l.383-398, l.404-407);
  - the tomb tradition, reported by Indjidjian (l.905-913);
  - Zarbhanalean (l.768-776) and Alishan (l.788-791);
  - Brosset's interpolations (ZAK l.26017-26018);
  - Derjan in Upper Armenia (l.3971-3972, note l.3999-4000; I added this to the existing Derjan claim);
  - Ani and Sargis's see (l.444-445, l.15210-15214);
  - Book III from the start of the Bagratid dynasty, with its dates (l.437-441, l.1028-1030);
  - Taron as a district (l.6276).
- R1-AM1: applied. The wording "in his youth" is now carried by the R1-AM3 split.
- R1-AM2: applied. "In Lent they drank water only on Saturday and Sunday."
- R1-AM3: applied with change.
  - Para 4: "In his youth, he writes, he saw some great teachers in their old age. Among them was Anania of Narek. Stepanos tasted the sweet food of their words." I named Stepanos so that "he" is not heard as Anania.
  - Para 6: "Stepanos ends his History by asking readers to remember him in their prayers. Then he too might be found worthy to sing the Trinity's praise."
  - Para 5: "Ghevond Alishan, an Armenian scholar, reported a manuscript at Venice. It says the father of the monastery, Stephen, also Asoghik, died when the Persians took Kars." See R1-AM5 for why.
- R1-AM4: applied. "...than to fill the gaps with bold guesses."
- R1-AM5: applied with change.
  - Brief: Alishan is introduced as "an Armenian scholar". Macler cites him from his Armenian works (MAC l.788, l.875). His being a Mekhitarist comes only from a file header, and lessons say a header is not the scan. "Mekhitarist" was also an undefined term. The card keeps the Mekhitarist library (MAC l.883-884). The card's `uncertain[3]` now opens "Ghevond Alishan, an Armenian scholar, reported...".
  - Card `uncertain[5]`: "Garegin Zarbhanalean, in a history of Armenian literature (1897), says he studied at Ani and was ordained a priest; Macler says that does little to settle the question."
  - `dates`: Brosset is introduced as in R1-AB2.
- R1-AM6: applied with change. `remembered[1]` now reads: "Gregory Magistros, an Armenian scholar, asks in a letter for a commentary on Jeremiah by Asolik, whom he calls a very old man (Macler's French)." I added no year. The scan gives Emin's range two ways, "entre 1041 et 1 057" (l.712) and "entre 1041 et 1045" (l.752). A year there would have to pick one. Emin's placing stays in `dates` and `uncertain[3]`. Records: the Gregory claim now cites l.711-712, l.751-752 and l.951-958, and notes both readings. "Wrote until 1058 (scan 1097)" is removed.
- R1-AM7: applied with change. `knownFor` now reads: "...down to his own day. Its closing note gives the Armenian year 453, which Frédéric Macler reckons as 1004 to 1005." On the same grounds, `keyWorks[0]` "to 1004 or 1005" became "to his own day".
- R1-AM8: applied. Appended to `uncertain[6]`: "Michael Chamich's History of Armenia, in Johannes Avdall's English of 1827, has it run to the year 1000. F. C. Conybeare placed the writing between 991 and 1019, as Macler quotes him (the scan of Conybeare's page reads 19190)." Both files are added to `sources.about`. Claims: CHAM l.5200-5204, and CONY l.2580 with MAC l.799-801. Both are added as sides of "Where the History ends".
- R1-AM9: applied. "Book III runs from the start of the Bagratid dynasty in about 887, Macler says, with dates for almost every event."
- R1-AM10: applied with change. The whole `place` field now reads: "Taron, the district his name comes from, as J.-B. Emin reads it; the monastery of Khladsor in Derjan, a district of Upper Armenia, where he spent a Lent; Ani, where the Bagratid kings ruled and where the catholicos Sargis moved his see in 992, Macler notes".
- R1-AM11: applied with change. "J.-B. Emin, his Russian translator, took the name Taronetsi to mean he came from the district of Taron." This rests on MAC l.698-700, with "canton de Tarôn" at l.6276. "A district of Armenia" was not on any held line.

## eulogius-of-cordoba

- R1-AB6: applied with change. "Juan Tamayo, author of a Spanish Martyrology, took this Alvarus to be his friend Paulus Alvarus, and said the brothers were bound by a shared life rather than by blood. Nicolás Antonio, in his notice on Paulus Alvarus, holds that they were blood brothers and that this Alvarus was another man." The role "Spanish martyrologist" became "author of a Spanish Martyrology" (ALV l.31676). Records:
  - the "Brothers" claim now quotes Tamayo's elogium and notes (ALV l.31675-31716);
  - a new contested claim, "Was Eulogius's brother Alvarus the same man as Paulus Alvarus", has the sides "Tamayo: one man (ALV l.31683-31691)" and "Antonio: two men (ALV l.31706-31716)". The Tamayo range starts at l.31683, where "Oscitantiam Joannem Tamaii" begins.
- R1-AB7: applied with change. After "...took the Cordoban martyrs from Eulogius's books." the card now adds: "Morales held that Usuard wrote for Charlemagne and could hardly have outlived Eulogius. A note in Lorenzana's edition says Morales was wrong about Usuard, who dedicated his martyrology to Charles the Bald in about 875, sixteen years after Eulogius died." I added the first sentence so the dissent has its premise (EUL l.58865-58874). Records:
  - the Morales claim now quotes his Charlemagne premise;
  - a new claim cites note b, l.58905-58911;
  - a new contested claim is "Did Usuard himself enter the Cordoban martyrs".
- R1-AB8: applied with change. "A note in Lorenzana's edition quotes a chronicle written in November 883. It says a priest had been sent that September with letters to the ruler of Cordoba, and had not yet come back. The note adds that this envoy, Dulcidius, brought the bodies of Eulogius and Leocritia to Oviedo on 9 January 884." The chronicle as scanned (l.58985-58996) does not name either the sender or Dulcidius: the text before "urbis presbyterum" is garbled. The name and the date come from the note's own "Postea". The reviewer's "King Alfonso sent Dulcidius as his envoy" belongs to the Oviedo lessons (l.58960-58964), which are a separate witness. Records: the claim is split into the chronicle (l.58985-58996), the note (l.58996-58998) and the Oviedo lessons (l.58958-58975).
- R1-AB9: applied. Eight claims are retagged "Documented", each marked "[Alvarus's own account; single witness]": the palace, the birth and orders, Reccafred, the release, Leocritia, the answer to the judge, the burial and the election. The claim "For most of his life Alvarus is the only witness" is kept.
- R1-AM12: applied. Para 1 has "a counselor who knew Eulogius of Cordoba well", and para 2 has "Eulogius was a priest".
- R1-AM13: applied with change. Brief: "When Christians began to die as martyrs, Eulogius writes, nearly all their fellow Christians turned against them for fear of the emir." The reviewer's version ran to 26 words, so I cut "clergy and laity". The records quote "omnes, tam clerici quam laici". Card: "when most of the city's Christians turned against the martyrs".
- R1-AM14: applied. "Eulogius Cordubensis, the Latin form in later notes and in the list of Toledo's early bishops". Records cite l.75577 and PL83 l.123287, l.123289.
- R1-AM15: applied. "The editors note that in it he argues again against Christians who still spoke against the martyrs." and "The editors' copy was badly corrupted".
- R1-AM16: applied. "...so he fixed the era and the year by astronomical reckoning, and corrected the ruler to Muhammad from Eulogius's own third book and from Alvarus." Records quote l.56706-56711.
- R1-AM17: applied. "citing Enrique Flórez's España Sagrada". Tamayo and Dulcidius are covered by R1-AB6 and R1-AB8.

## paulus-alvarus

- R1-AB10: applied. Brief: "In another, Alvarus quotes lines on the fearless Getae, which he wrongly gives to Virgil." Card: "In another letter Alvarus quotes lines on the fearless Getae, which he gives to Virgil; a note in the edition says they are not Virgil's. Antonio reads the lines as a claim to be a Goth, perhaps in jest." Records add "Virgilium audi" and the two notes (l.31057, l.40470).
- R1-AB11: applied. `uncertain[4]`: "A note to Antonio's notice reports other manuscripts that give it to Bede, to Defensor or to Cassiodorus." `remembered[2]`: "A note to Antonio's notice reports it and thinks it may come from him." Records name note (c) for both: l.31611-31615, l.31638-31655. The Sahagún codex stays with Antonio's main text, l.31544-31551.
- R1-AB12: applied. `uncertain[7]`: "Eulogius writes of his brothers Alvarus and Isidore, exiled in the lands of Louis, king of Bavaria. Juan Tamayo, author of a Spanish Martyrology, took this Alvarus to be Paulus Alvarus, and called the brothers bound by a shared life rather than by blood. Nicolás Antonio holds that this Alvarus was another man, Eulogius's brother by birth, and that Paulus's bond with Eulogius was friendship." Records carry the same contested claim as Eulogius, with the same ranges. The two cards agree.
- R1-AB13: applied. "Burial" is now Documented (single witness), and "Authorship" is now Contested.
- R1-AM18: applied with change. "Eulogius of Cordoba once went to the house of Paulus Alvarus, whom he calls his teacher. There Eulogius found a Christian named Aurelius, asking how to seek martyrdom." Naming Eulogius again keeps the pronoun clear. "Eulogius, his closest friend, tells this" became "Eulogius tells this in his Memorial of the Saints." The old wording had an ambiguous "his", and it saved words. The friendship is still told in para 2.
- R1-AM19: applied with change. "A codex of the church of Cordoba, in Gothic script, kept his works, and Morales saw it. Thomas Tamayo de Vargas, the royal chronicler, praised another at Toledo. Antonio's own copy came from one that Tamayo de Vargas gave to Cardinal Barberini's library in Rome." I added the role "the royal chronicler" (l.31061-31062 "regio chronographo") and the full surname to keep him apart from Juan Tamayo. "In Gothic script" rests on the title of Tamayo's copy, "litteris gothicis exarato" (l.31074-31075). Records: l.31019-31036, l.31058-31075.
- R1-AM20: applied. "The sources say no more of who he was."
- R1-AM21: applied. `dates`: "cites Enrique Flórez, author of the España Sagrada, for about 861 (the scan reads $61)". `uncertain[5]`: "about 861 (the scan reads $61)".
- R1-AM22: applied, through R1-AM21.

Briefs also tightened to stay in range:
- Stepanos: "spent a Lent with them". The Macler "first writer whose dates can be trusted" sentence was merged into para 2. "Mekhitarist library" moved to the card.
- Alvarus: "Alvarus was a Christian layman"; "In 854 an unsigned book, the Luminous Index, defended..."; "Antonio gives it to Alvarus from its style and date."; "Hardly one in a thousand"; "The city's Christians, he writes,"; "Closing the Life, he turns to his dead friend".

No story or side was cut. The contested points keep their sides: Stepanos's death (Brosset against Alishan and Macler), Alvarus's ancestry (Hebrew against Goth), the Luminous Index (Antonio, named), and the year 859 (Morales's reckoning).

**Final scores (score.py)**

| id | words | time | FK | FRE |
|---|---|---|---|---|
| stepanos-of-taron | 336 | 2:04 | 6.6 | 70.1 |
| eulogius-of-cordoba | 337 | 2:04 | 6.8 | 69.8 |
| paulus-alvarus | 336 | 2:04 | 7.9 | 63.3 |

All three are inside the README's 324-338 range. All three cards are valid JSON with a final newline. The audio files are regenerated.

## README (for the worker)

- R1-AM-R1: in l.35, l.39, l.40 and the Ishoyahb census bullet, delete each "(C1)", "(C4)", "(C6)" and "(C7)", or replace it with a plain pointer naming the entry it means, for example "see the Eulogius and Alvarus bullet above". Do not point to a section that does not exist.
- R1-AM-R2: l.35. Replace "The two batch 11 cards, Eulogius and Alvarus, disagree on the brothers; see (C4)." with "The two batch 11 cards, Eulogius and Alvarus, agree on the brothers: each gives Tamayo's view that Eulogius's brother Alvarus was Paulus Alvarus, and Antonio's that he was another man."
- R1-AM-R3: the "Who the sources are" Stepanos bullet. Replace "Death and burial rest on a late manuscript notice and a tradition." with "Death and burial rest on a manuscript notice of unknown age, Emin's reading of a letter of Gregory Magistros, and a tradition." This adds the Emin placing now on the card. Also replace "the old teachers he saw as a young man" with "the old teachers he saw in his youth".
- R1-AM-R4: the census Stepanos bullet. Before "No other passage.", add "`movements[116]` (the physician Taronites) is a namesake, set aside."
- R1-AM-R5: the census Eulogius bullet. Replace "`voices[0]` agrees" with "`voices[0]`, 'executed in 859', states Morales's year flat, as `why` does".
- The word range line: unchanged at 324-338. The Part A counts are 336, 337 and 336.

---

## Era 4 Who batch 11, round 1, Part B: changes

Every cited range was reopened with sed -n in cic/texts before each fix. Files edited: the three briefs and cards in batch11/, and scratchpad/rec/<id>.json for each. README.md and batch11/records.json were not touched. Audio rebuilt by score.py.

## theodore-abu-qurrah

- R1-BB1: applied. Brief para 7: "He wrote it for Janah, whom Graf takes to be a bishop." (GRAF l.14079-14080, l.14097-14114 checked: "Anba" a copyist's, the bishop Graf's inference, Tela left open.) Records unchanged.
- R1-BM1: applied. Brief para 4: "Abu Ra'ita calls Theodore the philosopher, and a secret follower of Nestorius, whom he calls a false teacher." (GRAF l.870-877: "der Lügner und Irrlehrer Nestorius" sits inside Abu Ra'ita's quoted words.)
- R1-BM2: applied. Brief para 6: "...Nonnus of Nisibis beat Theodore in debate."
- R1-BM3: applied. Brief para 6: "Graf gives his account in German." (GRAF l.908 cites Chabot's edition.)
- R1-BM4: applied. Card `dates`: "No source gives an exact year for his birth or his death, or any year for his consecration". (PEETERS l.867-868, GRAF l.1157-1158 checked.)
- R1-BM5: applied with change. Records `contested_claims` "Same man as Theodore of Caria of the council of 869": "No" side now "No: Fabricius, the Mai notice, Le Quien, Graf (PG97 l.121554-121558, 122148-122150; PG94 l.116610-116614; GRAF l.340-343)"; new third side "Turrianus, reported both ways: Le Quien says he took the two for one man (PG94 l.116610-116611); the Mai notice follows him in keeping them apart (PG97 l.122124-122125, 122148-122150)". The change: I added l.122148-122150 ("Quare assentior Turriano") to the Mai notice citation, since that is where the notice states it follows Turrianus. Card unchanged.
- Tightening to hold length: brief para 3 "so Graf holds that Theodore lived there" → "so Graf holds Theodore lived there" (meaning unchanged, GRAF l.737-743).

## stephen-of-mar-saba

Name kept as "Stephen of Mar Saba" (see README section for Mark's option).

- R1-BM6: applied with change. I reread the margin (AASS l.50373-50387: "S. Stephanus Poeta statim post rem gestam, scilicet post Pascha anni 797"). It dates the writing "immediately after the event", so I kept "statim" in each fix, so the 796 text and 797 margin are not heard as a year's gap. I did not use the reviewer's "which puts the raid that spring" on the card, which is an inference past the margin's words. The range starts at l.50373, where the margin begins "S. Stephanus", not l.50376.
  - Brief para 4 (split to stay under 25 words): "The Bollandists, by their own count of the years, make it 796. A note in their margin has him writing soon after the raid, just after Easter of 797."
  - Card `dates`: "...make it 796 in their text. Georg Graf, in 1910, gives March 796 or 797. The Bollandists think Stephen wrote straight after the raiders left, and their margin puts that just after Easter of 797. No source used here gives his birth or death"
  - Card `uncertain` "The year": "...make it 796 in their text, while their margin has him writing soon after the raid, just after Easter of 797."
  - Records claim "Bollandists' margin": adds 'beside "S. Stephanus Poeta" (the margin dates the writing, soon after the raid; read so, it puts the raid in 797)'; witness l.50373-50387. `contested_claims` "The year of the raid", side 3: "The Bollandists' margin: Stephen wrote soon after the raid, just after Easter of 797, which puts the raid in 797 (AASS l.50373-50387)".
- R1-BM7: applied. Brief para 4: "Stephen wrote at the order of his abbot, Basil, for reading in church, so that the courage of these men would not fade with time." (25 words.) Records: new claim 'Written for reading in church: "quam scribendis temere se sermonibus ingerant, quos in ecclesia sacrisque conventibus necesse sit recitari"; Stephen counts himself among such writers: "Equidem horum omnium me insimulandum cognoscens" (scan)', witness AASS l.50512-50514, l.50524-50525, Documented. (The reviewer cited l.50513-50514; the clause begins at l.50512. I added l.50524-50525 because the prologue's line is general, and it is Stephen's own "horum omnium me insimulandum" that applies it to his text.)
- R1-BM8: applied. Card `uncertain` "Who the raiders were" ends: "Georg Graf calls them Bedouin." Records "Who the killers were", side 2 adds "; Graf: Bedouin (GRAF l.645-646)". (GRAF l.645-646 checked: "durch Beduinen angerichteten Blutbad".)

## ishoyahb-iii

- R1-BM9: applied with change. Card `otherNames[3]`: "Jesujabus hazzensis, that is, of Hazza, in the Latin of Amr ibn Matta and of Mari ibn Sulayman; in Enrico Gismondi's edition, Sliba ibn Yuhanna's additions to Amr say Hazza is now called Arbela". (AMR l.13282 "Jesujdbiis hazzensis", unbracketed; l.13284 "[nunc notae nomine Arbela"; l.6398-6400 Gismondi's bracket rule; MARI l.13481 "Jesujabus hazzensis".) The change: Gismondi named as the editor so the bracket attribution has its owner. Records "Places" claim adds 'Gismondi: bracketed words are Sliba's own, "quae ei prae Amro propria sunt uncinis inclusa"; Amr "Jesujdbiis hazzensis" (scan); Mari "Jesujabus hazzensis"', witness now AMR l.13282-13295, l.6398-6400; MARI l.13481.
- R1-BM10: applied with change. Brief para 2: "Thomas says parts of it came down by the monastery's tradition." Same fix in a shorter order, and "own" dropped to hold length (TOM l.5688-5690, l.5750-5751).
- R1-BM11: applied. Brief para 7: "In it, Ishoyahb blamed Simeon of Rev-Ardashir, in Fars, ..." (Both passages are in letter XIV, "Ad Simeonem episcopum urbis Rewardashir", DUV l.8570 onward, l.8715-8719, l.8740-8747.)
- R1-BM12: applied with change. Card `uncertain` "Who sent the mission": "Budge, who translated Thomas in 1893, sides with Boran, as do Duval and Addai Scher, who translated Seert in 1919." Reordered so the "who translated" clauses do not nest (DUV l.108-111 checked). Records side 2: "...Budge, Duval and Scher agree (TOM l.5557-5558; DUV l.108-111; SEERT2 l.30814)".
- R1-BM13: applied with change. Card `uncertain[0]`: "Thomas of Marga wrote the history of Beth 'Abhe, his own monastery, about two centuries after Ishoyahb. Budge dates the book about 840, and Jérôme Labourt between 832 and 850, while J. S. Assemani has Thomas flourish early in the ninth century. Thomas says parts of it came down to him by the monastery's own tradition." Split into three sentences to stay under 25 words. (ASSEMANI3-1 l.78622-78626 "nono saeculo ineunte claruit", scan "nono foculo iueunte"; LABOURT l.17234.) Records Thomas date claim adds 'Assemani: Thomas "nono saeculo ineunte claruit" (scan: "nono foculo iueun- te")', witness ASS31 l.78622-78626.
- R1-BM14: applied. Per instruction, aligned to the Thomas of Marga profile and live census form: "Beth Abe" → "Beth 'Abhe" in the brief (para 1) and every card occurrence (`place`, `legacy.traces[0-1]`, `uncertain[0]`, `uncertain` "His burial" twice). Records label "Beth Abe in the Mosul district" → "Beth 'Abhe in the Mosul district". Quoted source strings (Scher's "Beith 'Abe", Mari's "Ba'abae") unchanged. No reason against found; the Babai card's "Beth Abe" (census `[543]`) is now the odd one out (README section).
- R1-BM15: applied with change. Card `knownFor`: "His surviving letters include attacks on the teaching of his friend Sahdona, and others against the bishops of Fars and Qatar who broke from him." Avoids "letters ... letters" (DUV l.230-232).
- Tightening to hold length: brief para 1 "They would not have a school in their monastery." → "They would not have a school there."; para 3 "names three other bishops instead." → "names three other bishops."

## Final counts and scores (score.py)

| id | words | minutes | FK | FRE |
|---|---|---|---|---|
| theodore-abu-qurrah | 338 | 2:04 | 8.2 | 62.0 |
| stephen-of-mar-saba | 337 | 2:04 | 6.2 | 75.5 |
| ishoyahb-iii | 338 | 2:04 | 7.1 | 66.0 |

All JSON parses with a final newline. Audio rebuilt.

Tally: 18 findings in Part B, counting README. Profiles: 15 (1 blocking, 14 minor): 8 applied, 7 applied with change (BM5, BM6, BM9, BM10, BM12, BM13, BM15), 0 not applied. README: 3, given below for the worker.

## README (for the worker)

- R1-BM16, Other profiles, Ishoyahb bullet: replace the sentence on "his 840 history" / "in 840" with: "The draft dates the book 840 by Budge's title (brief) and adds Labourt's 832 to 850 and Assemani's early ninth century (card `uncertain[0]`); the Thomas profile gives the same three placings." Live census mentions (3), Babai card: "more careful than the draft (C1)" → "agrees with the draft".
- R1-BM17, Who the sources are, Ishoyahb: "Thomas of Marga's Book of Governors (840, Budge's English)" → "Thomas of Marga's Book of Governors (840 by Budge's title; Labourt, 832 to 850; Assemani, early ninth century; Budge's English)".
- R1-BM18, Corrections to the re-score, Stephen l.160: "the Bollandists' margin gives 797 (l.50387)" → "the Bollandists' margin has him writing soon after the raid, just after Easter of 797 (l.50373-50387), which implies the raid in 797". Live census mentions, Stephen: give the margin range as l.50373-50387 (the margin begins "S. Stephanus Poeta" at l.50373).
- R1-BM14, spelling: add to the Other profiles / census notes: "Ishoyahb now writes Beth 'Abhe, matching the Thomas of Marga profile (batch5), the census Thomas entry (`movements[604]`) and the Timothy I card (`[599]`). The Babai card (`[543]`) still writes Beth Abe; the census fix should align it." Log in the batch's Open-Gaps entry if one exists; cite only an existing entry.
- Word range: restate as 337 to 338 for these three (Theodore 338, Stephen 337, Ishoyahb 338). Combine with Part A's counts for the batch range.
- For Mark (not applied): the reviewer notes that "Stephen of Mar Saba" alone does not tell this man from Stephen the Wonderworker, who is also "a Sabaite" (AASS l.50429-50431, "similiter Sabaitae"). What marks this Stephen in the record is the Typikon's "Poetae titulo" (l.50438). If Mark wants the display name itself to tell them apart, "Stephen the Poet, of Mar Saba" is the held option. The name stays "Stephen of Mar Saba" for now; the card already carries "Stephen the Poet" and the brief names the Wonderworker apart.

---

## Era 4 Who batch 11, round 1, Part C: changes

Every cited line was reopened with sed in cic/texts before a fix was applied. Records edited at scratchpad/rec/<id>.json only.

## al-tabari

- R1-CB1: applied with change. QUATREMERE l.14025 ("dit Macrizy") confirms the account is al-Maqrizi's, quoted by Quatremère. "Egyptian historian" is not held for al-Maqrizi in the file (grep found no such line), so "The historian" is used. The sentence is split to stay under 25 words. `legacy.traces[2]`: "The historian al-Maqrizi, quoted in Étienne Quatremère's French of 1811, tells of the library of the caliph Aziz. Aziz had more than twenty copies of the chronicle, one written in the author's own hand." Records: the claim now reads "Quatremère quoting al-Maqrizi ("« La bibliothèque deskhalifes (2), dit Macrizy" (scan), l.14025; source note "Ms, Arab. 678 C", l.14033): the caliph "Aziz"; ...", witness l.14025-14053, tag Documented.
- R1-CB2: applied. Ginzel's "gilt als der verlässlichste" claim: Widely Accepted → Dominant Modern Reconstruction. Quatremère/al-Maqrizi: → Documented (with CB1). Hitti l.911-914 keeps Widely Accepted.
- R1-CM1: applied. Brief: "For Aelia, as Jerusalem was then called, he gives the caliph Umar's terms."
- R1-CM2: applied with change. Neither of the reviewer's wordings was used, because both were long or clumsy aloud. Brief: "Priests and monks shouted to the men in the castles, blaming them alone for the killing." This follows T4 l.1494-1495 (يا اعل القصور ما يقتلنا غيركم, "people of the castles, none but you is getting us killed"). "them" points to the men in the castles, the nearest noun.
- R1-CM3: applied (first option). Michael the Syrian, "Alors, Yezdegerd, dernier roi des Perses" (michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt l.32600), was confirmed. "Last" stays in the brief and in `knownFor`. Added to `sources.about`: {"title": "Chronique, tome 2", "author": "Michael the Syrian; J.-B. Chabot (tr.)", "date": "1901", "language": "French translation", "file": "cic/texts/michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt"}. New records claim: MICHAEL l.32600, Documented.
- R1-CM4: applied with change. Moberg says "Muhammadan interpreters" (MOBERG l.2817-2820), so the fix says "Muslim". The sentence is split to stay under 25 words. `keyWorks[1].about`: "which Axel Moberg, in 1924, calls his great commentary on the Koran. Moberg says most Muslim interpreters refer the Quran's verses on the pit to the Najran martyrs. He says the commentary also gives traditions that refer them to an incident among the Parsees, or to \"Daniel and his men\". Not held". Records: the Tafsir claim adds "even the Muhammadan interpreters do not agree, at least not unanimously".
- R1-CM5: applied with change. The rule is quoted as Hitti's held English (HITTI l.614-616) and split into its own sentence. `uncertain[1]` now ends: "Hitti says Arab historians did little to analyze, compare or test their reports. Their rule, in his words, was \"what has been once well said need not be told again\", and al-Tabari's preface voices it." New records claim: HITTI l.614-616, Documented.
- R1-CM6: applied. ELIAS l.7329-7668 shows 21 Tabari citations across the 28 years 275-302 (year headings for 287, 289, 298, 299 and 301 carry none; the 280-281 headings are not legible in the scan). `traces[0]`: "...and cites him in most years from 275 to 302 of the hijra."
- R1-CM7: applied with change. The chain at T4 l.673-674 reads "حدتنا ابن auum قل سآ سلمة عن ابن / hos enl صا بن كيسان". The name after Salama is illegible, and the "Ibn Humayd" before Salama is illegible too, so it is not named. No new chain stands before l.727. Elsewhere in T4, Salama's chain reaches Ibn Ishaq legibly: "عن ابن اسحاق" (l.5549) and "سلمة عن حيد بن اسحاق" (l.6769). `uncertain[2]`: "His sources for the conquests. The Hira report of 190,000 and the Najran report reach him through a chain of tellers, al-Sari from Shu'ayb from Sayf ibn Umar. The Hira report of 90,000 comes by another chain, through Salama. The name after Salama is unreadable in the scan, but elsewhere in the volume Salama's chain reaches Ibn Ishaq, the biographer of Muhammad. A later summary printed in the Leiden edition says he had the Jerusalem story from Sayf too." ("dirhams" is left off the 190,000 because the records note it as implied.) New records claim at T4 l.673-674, 697-727, 5549 and 6769, tagged Inferential-Thin. The contested "Hira's tribute" second side now gives this chain.
- R1-CM8: applied. "l.898, 906-908, 23978-24030" → "l.898, 910-912, 23978-24030". In-claim "l.906-908" → "l.910-912". "l.6590-6609, 5839" → "l.6590-6609, 5838", and in-claim "IAthir", T5 l.5839 → "lAthir" (scan), T5 l.5838.
- R1-CM9: applied. "Elias von Nisibis (scan "Nisibis®") setzt", "jene vom 14. Schauwäl 280" (scan "ı4."), "ibn-al-Athir and abu-l-Fida" (scan "abu- 1-Fida").
- R1-CM10: applied with change. T5 l.23986-23987, "Narratori duas inter se diversas relationes confusas esse perspicuum est", is the first note (a) of the page. That page holds the end of the second telling (branch, vault) and the opening of the third (l.23967-23974). The OCR does not show which word the note marks, and the Latin argumentum (l.910-912) says only "Variae de ejus exitu traditiones". The added text is therefore tied to the page, not to one telling. `uncertain[3]`, after "where he used to sit.": "On the same page, E. Prym, the volume's editor, notes that the teller has plainly mixed two different accounts." New records claim at T5 l.23967-23974 and 23986-23987, Documented.

## ibn-ishaq

- R1-CB3 and R1-CM1: applied with change (tightened for length). WEIL l.9374-9379 (first audience: bishops and books, "Djafar, der Sohn Abu Talibs") and l.9438-9459 (next morning, the question about Isa, the twig) were confirmed. Brief para 1: "Muslims who had fled Mecca stood before the Negus, the Christian king of Abyssinia, his bishops and their books around him. Next day the king asked them about Jesus. Their spokesman, Ja'far son of Abu Talib, said Jesus was God's servant and messenger, his spirit and his word, given to the virgin Mary. The king picked up a twig. Jesus, he said, is not one twig more than that. He told the exiles they were safe." ("said Jesus was" replaces "said he was", where "he" could be heard as Ja'far.) Records claim 1: first and second audiences marked, witness "l.9374-9379 (first audience), l.9438-9459 (second audience, next morning)".
- R1-CB4: applied. `place`: "No source gives where he was born, lived or died. Philip Hitti counts him, with al-Waqidi, as representing the tradition of Medina". Records claim 6 adds that Hitti groups the tradition by region and does not say where Ibn Ishaq lived.
- R1-CB5: applied with change. HITTI l.15759-15791 and 15805-15806 were confirmed ("found certain persons in a church whom he took captives"; "(4) Yasar, a grandfather of Muhammad ibn- Ishak ... a freedman of Kais ibn-Makhramah ibn-al-Muttalib"). The reviewer's otherNames wording "after the clan his grandfather served" was not used. No held line says the nisba comes from that clan, so the two facts are set side by side without a link. A separate finding: the card's "Almuttalebij" is not in Weil. Weil's form is "Almuttalabij" (WEIL l.301), and that form is now used. New text:
  - `otherNames[1]`: "al-Muttalibi, the name he bears in Ibn Hisham's chain of transmission, as Weil gives it (Almuttalabij). His grandfather Yasar was a freedman of Qays ibn Makhrama ibn al-Muttalib, by al-Baladhuri, a Muslim historian who died in 892"
  - new `uncertain[1]`: "His family. Al-Baladhuri, in Hitti's English, names his grandfather Yasar among the captives that the commander Khalid ibn al-Walid took from a church at 'Ain at-Tamr. Al-Baladhuri says Yasar was a freedman of Qays ibn Makhrama ibn al-Muttalib."
  - records `absent_details[0]`: detail "Birth, birthplace, parents, teachers, travels, place of death, burial"; note adds "His grandfather Yasar is named by al-Baladhuri, in Hitti's English (HITTI l.15789-15791)."
  - new records claims: the Yasar claim (HITTI l.15759-15791, 15805-15806, Documented) and the nisba claim (WEIL l.300-301, 3285, 24250, Documented).
- R1-CB6: applied with change (tightened). Brief para 5: "Weil says Ibn Ishaq's contemporaries and later scholars held him an excellent, reliable collector, though envy and sectarian hatred tried to discredit him." `uncertain[0]`: "How far he can be trusted. Weil says Ibn Ishaq's contemporaries and later scholars held him reliable. Weil himself calls him the faithful voice of the traditions of his day. Some of what he reports as fact, Weil says, belongs to legend, which Weil does not hold against him. ..." The records Weil claim now quotes l.140-148 in full: the reputation Weil reports, then Weil's own "treuen Ausdruck" and "nicht ihm anrechnen".
- R1-CB7: applied. Claim 4 (al-Mansur) and claim 6 (Medina): Widely Accepted → Dominant Modern Reconstruction.
- R1-CM2: applied with change (shorter). "B. T. A. Evetts, editing a book on Egypt's churches in 1895, gives 768 in a note." (EVETTS header and l.5637-5640.)
- R1-CM3: applied with change (shorter). "Weil adds, without blaming him, that some of what he tells as fact is legend." (WEIL l.146-148, "Manches", "dürfen es nicht ihm anrechnen".) The card's `uncertain[0]` and the contested-claim side now say "some" too.
- R1-CM4: applied with change. Najran: "Later, Christians of Najran debated at Medina. Like all Christians, Ibn Ishaq says, they held that Jesus is God, a son of God and the third of three." Moberg: "Axel Moberg, who edited a Syriac book on the martyrs in 1924, traces most of the Arabic stories to an older Christian account. In those stories he could not see "anything that suggests an independent Muhammadan tradition of historical value."" Every sentence in the brief is now 24 words or fewer.
- R1-CM5: applied with change. It is folded into the Moberg sentence above ("traces most of the Arabic stories to an older Christian account"). "Most" is there because Moberg gives the king's death in the sea to the Book of the Himyarites (MOBERG l.2697-2706).
- R1-CM6: applied (the "introduction and text" option). `sources.about[1]`: title "The Origins of the Islamic State, volume 1, introduction and text", author "Philip Khuri Hitti; al-Baladhuri".
- R1-CM7: applied with change. The reviewer's lines show Waraqa as Christian, but not meeting Muhammad. l.4532 is told by Waraqa's sister, not by Khadija. The records claim therefore cites WEIL l.6686-6705 (Khadija goes to Waraqa; Waraqa meets Muhammad at the Kaaba and kisses his forehead) and l.8883-8884 (Waraqa and Bilal under torture), as well as l.4532-4533 and 5365-5369. `knownFor`: "...tells of Christians who met Muhammad and his first followers: the Negus of Abyssinia, the Christians of Najran, and Waraqa ibn Naufal of Mecca."
- R1-CM8: applied. `dates`: "No source gives his birth". `place` was replaced under CB4.
- R1-CM9: applied with change. "Ein frommer, eifriger Christ" is at l.996 and "Zimmermann / und Maurer" at l.999-1000. The chain opens at l.994, so the witness is "l.994-1000, l.1060-1061, l.1091-1093".
- R1-CM10: applied. `uncertain[6]` (formerly [5]): "one of the exiles and a wife of Muhammad,". Records: the Umm Salama claim notes that Weil gives no time for the marriage.
- R1-CM11: applied with change. It goes on the Negus-scene item (`uncertain[6]`), not on the Moberg item, because Moberg's judgment covers the Najran persecution only. Added: "In another report, Ibn Ishaq tells that the Abyssinians rose against the Negus for leaving their faith. In answer, the Negus wrote out the Muslim confession of faith." New records claim: WEIL l.9565-9597, Documented.
- R1-CM12: applied. "wie alle Christen [scan "\rie alle"]"; "lebte in der ersten Hälfte ..." (scan "lebte in i.' der ersten").

## Final counts and scores (score.py)

- al-tabari: 333 words, 2:02, FK 6.7, FRE 68.7
- ibn-ishaq: 338 words, 2:04, FK 6.7, FRE 69.5

Audio rebuilt by score.py. JSON parses, with a final newline.

## README (for the worker)

- R1-CB8 (River and tradition counts, para "The river counts do not change"): replace "By the census's own era 4 Who rows (release 44's major flag), the majors stand at Latin West & Catholicism 10, Greek East & Orthodoxy 5, Syriac East & Asia 4, Caucasus 1 and Africa 1. Counted by era 4 card traditions, Greek East stands at nine, as the batch 9 and batch 10 READMEs set out." with "Release 44's major flags give era 4 Latin West & Catholicism 10, Greek East & Orthodoxy 5, Syriac East & Asia 4, Caucasus 1 and Africa 1. With batch 9's majors (John of Damascus, Theodore, and Cyril and Methodius in the Greek East; Anskar in the Latin West), the census rule gives Greek East eight and Latin West eleven. Counted by era 4 card traditions, Greek East stands at nine and Latin West at ten, as the batch 9 and batch 10 READMEs and Open-Gaps 269 set out." (Not re-verified by Part C against the census; the worker should check the reviewer's counts before applying.)
- R1-CB9 (by-river sentence): replace "and two outside the church (al-Tabari, Ibn Ishaq), which have no river." with "and two outside the church (al-Tabari, Ibn Ishaq). Their cards carry no tradition, but the census places each outside witness on a lane: al-Baladhuri, of Baghdad, sits on Syriac East & Asia. Which lane these two take is for the map build slice (Open-Gaps, \"Map Who build slice: caps, major mark, placement\", 2026-11-11)." Log it in the batch's Open-Gaps entry.
- R1-CM1 (Live census mentions and Other profiles): replace each "(C1)", "(C4)", "(C6)", "(C7)" with the finding itself or "see the batch's Open-Gaps entry". Replace "the draft" → "the profile", "the draft card" → "the card", "the draft attributes" → "the profile attributes", "the draft's record 5" → "the Ibn Ishaq records' Medina claim", "the draft records" → "the records". In the al-Tabari Other-profiles bullet: "appear only in the Tabari draft" → "appear only in the Tabari profile".
- R1-CM2 (Other profiles, al-Tabari): replace "The Tabari brief's \"Hitti says Arab historians did little to weigh or test their reports\" draws on HITTI l.612-619, which opens \"Aside from the use of judgment in the choice of isnad\"; see (C7)." with "The Tabari brief's \"Beyond choosing their chains of reporters, Hitti says, Arab historians did little to test their reports\" draws on HITTI l.612-619, which opens \"Aside from the use of judgment in the choice of isnad\"; the two cards agree."
- New, from Part C's changes (Other profiles, Ibn Ishaq): "No other profile names him or Ibn Hisham." is no longer true. Replace it with "Of the other profiles, only this batch's al-Tabari card names him: its `uncertain[2]` says Salama's chain in the Leiden volume reaches Ibn Ishaq (T4 l.5549, 6769), and that the chain of the 90,000 Hira report runs through Salama, with the next name unreadable (T4 l.673-674). The two cards agree."
- R1-CM3 (Live census mentions): to the Ibn Ishaq bullet, add "`movements[53]` `relationsSummary` (\"The Najran martyrs of 523 and King Kaleb's campaign in Himyar around 525\"), `voices[0]` (Kaleb \"around 525 in response to the killing of the Christians of Najran\") and `voices[3]` (the martyrs \"killed in Himyar in 523\") differ from his version on the same points as `documentedStories[1]` (no year, no Kaleb). `movements[609]/card/uncertain[4]`, \"his works rest on the tradition of Medina\", is Hitti's passage naming him (HITTI l.646-652); agrees." To the al-Tabari bullet, add "`movements[569]/card/uncertain[0]` (Theophanes's account of Umar at Jerusalem): Tabari's Aelia terms neither confirm nor contradict it." (Not re-walked by Part C; the worker should confirm the paths in census.json.) Also add "Ja'far son of Abu Talib" to the Ibn Ishaq patterns, since the brief now names him so.
- R1-CM4: replace "Open-Gaps, \"Era 4 Who batch 11\" (2026-11-15)" with "Open-Gaps, \"Era 4 Who batch 11\" (2026-11-15, to be logged at approval)", or create the entry before merge.
- R1-CM5 (Majors and lengths): after "al-Tabari's and Ibn Ishaq's lives are thin as well, as the outside-witness rule allows." add "The re-score leaves both to Mark: al-Tabari's life may be judged too thin, and Ibn Ishaq's held text is Ibn Hisham's recension (Rescore l.156-157)." Restate the word range once Parts A and B are final. Part C's two are 333 and 338.
- R1-CM6 (Ishoyahb's card, Part B's file): "106 letters (the scan reads \"evi\") in three parts" → "106 letters in three parts", with the scan reading kept in records. If it stays, list it under Language and quotations.
- R1-CM7 (Who the sources are, Ibn Ishaq): "His life rests on Weil, Hitti and a note by B. T. A. Evetts (1895)." → "His life rests on Weil, Hitti, a line of al-Baladhuri's in Hitti's English on his grandfather Yasar, and a note by B. T. A. Evetts (1895)."
- New, from Part C's changes (Who the sources are, al-Tabari): after "His life rests on F. K. Ginzel (1887) and Philip Hitti (1916)." add "His card also cites al-Maqrizi in Étienne Quatremère's French (1811) on the copies in the caliph Aziz's library, and Michael the Syrian in J.-B. Chabot's French (1901) for Yazdegerd as the last Persian king."
- R1-CM8 (cross-batch): stephen-of-mar-saba (Part B or A's file): "No source used here" → "No source" in every place. "...used here. Of his own life" → drop "used here". "No source used here makes the writer a relative" → "No source makes the writer a relative". Done for ibn-ishaq by Part C.
- Language and quotations: unchanged for Part C. The brief quotations stay Hitti's "We only transmit to others what has been transmitted to us." and Moberg's "anything that suggests an independent Muhammadan tradition of historical value." The al-Tabari card adds one held-English quotation, Hitti's "what has been once well said need not be told again" (HITTI l.614-616), if the section lists card quotations.
