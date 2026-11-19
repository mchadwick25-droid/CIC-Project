# R4 cap check: era 6 batch 2

The one targeted check ordered by Mark's cap ruling of 2026-11-15 for era 6 Who batch 2 ("Fix + one check"). This check does not count toward the three-round cap. It was done at full effort by a fresh Opus reviewer who had not seen the drafting or any review round.

## Scope

Only the strings changed after round 3, as `R3_changes.md` lists them under "Strings for the cap check", plus its last line on the records claim "Gass: unter den Anhängern des Palamas genannt…". The records entries that `R3_changes.md` says were changed with those findings are checked too. The diff is `git diff 7179f165..da177cd9 -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch2/` on branch `claude/cft-who-era6-batch2`; the working tree matches da177cd9. The findings answered are D3-B1, B3-B1, B3-M1 to B3-M3, C3-B1, C3-B2, C3-M1, A3-B1, A3-M1 to A3-M3 and D3-M1 (`R3_review.md`). No repo file other than this one was edited. No web, paid or model call was made.

## Method

1. Read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md`, `R3_changes.md` and the R3 findings listed above.
2. Took the word diff of the briefs, cards and README, and the full diff of `records.json`, for 7179f165..da177cd9.
3. For each changed string, opened every cited line in `cic/texts/` with 20 or more lines of context (grep -n, sed -n). I asked who speaks, what document a note annotates, whether a hedge or condition dropped, and whether a claim moved to another witness.
4. For the Cabasilas see, checked that each claim sits with its own witness: Fabricius (PG150), Gass (GASS), Jugie (PO19), Kantakouzenos (CANT3) and Symeon. I also checked that the see is told as contested in the brief, card, README and records.
5. Read each changed string as a listener would hear it: what each pronoun points to, identifiers at first mention, AI tells, and sentence length (counted by script).
6. Parsed all nine JSON files. Rebuilt every audio script from its brief by script (`[calmly] ` at the start, `[warmly] ` at the start of the last paragraph) and compared for equality, and also compared the tag-stripped audio with the brief. Counted words with `wc -w`. Scored all eight briefs with `engine.m1.gates.grade_text`, and scored the proposed Cabasilas replacement on a scratch copy.

## Files opened (cic/texts/), with context

- PO19 `john-ephesus_lives-eastern-saints-po19-mixed-issue_brooks1926.txt`: l.1-15, 18195-18262, 39860-39925.
- PG150 `palamas_opera-omnia-pg150-grc-lat_migne1865.txt`: l.338-350, 26055-26080.
- GASS `cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt`: l.995-1012, 1195-1240, 1360-1395, 1765-1800, 1870-1940.
- CANT3 `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt`: l.6330-6450, 16599-16602.
- MANSI26 `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`: l.10505-10526, 12058-12072, 12185-12192, 19568-19600, 53375-53420, 111540-111565.
- BIRGL `birgitta_revelationes-lat_duranti1628.txt`: l.98770-98805.
- BIRGE `birgitta_revelations-enm_cumming1929.txt`: l.953-962.
- EHRLE1 `ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd1-deu-lat_1885.txt`: l.27780-27800.
- EHRLE2 `ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd2-deu-lat_1886.txt`: l.5810-5860.
- PG88 `dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt`: l.43290-43312.
- PAISZ `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt`: l.3984-4000, 14193-14226.
- MEYER `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt`: l.30-50.
- PO15 `patrologia-orientalis-tomus15_petit-documents-concile-de-florence-purgatoire-grc-fra_graffin-nau1927.txt`: l.1-10, 95 (Petit's name, for the records note on Jugie's footnote).

## Strings

| # | Finding | String | Verdict |
|---|---|---|---|
| 1 | A3-M1 | Catherine brief para 4: "A life of Gregory in Mansi's collection of church councils says Gobelinus of Paderborn credited his return to Bridget's revelations." | PASS. MANSI26 l.53396-53409, "Gobelinus cap. 73. sextae aetatis, instinctu & revelatione Dei, quae sanctae Brigittae … obtigerat … accidisse quod Avenione Romam redierit"; running head "VITA GREG. PAP XI." (l.53417); "Gobelinus Paderbonensis officialis" (l.111555-111556). "His return" carries Gregory from the paragraph's first sentence. |
| 2 | A3-M1 | Catherine card `uncertain` 1: "A notice of Gregory's life … names other causes. Gobelinus of Paderborn credits Bridget's revelations. Platina, in his life of Gregory, tells of a bishop's retort that hastened the return." | PASS. "Hujus transmigrationis causam alii aliam referunt. Platina scribit, quod quidam episcopus … responderit … eaque responsione motum pontificem reditum maturasse" (MANSI26 l.53396-53403); "Platina in vita ipsius Gregorii" (BIRGL l.98786-98787, 98793-98794). The colon-reveal is gone. |
| 3 | A3-M2 | Bridget card `legacy.remembered` 4: "… says Gobelinus of Paderborn credited his return to Rome to her revelations. They reached him through Alphonso. Platina, in his life of Gregory, gave another cause." | FAIL (R4-M3). The source holds: "perque Alphonsum quemdam eremitam illi secundo insinuata erat" (MANSI26 l.53407-53408), where "illi" is the pope. The split leaves "him" open to Gobelinus. |
| 4 | B3-B1 | Clareno card `dates`: "The year is Ehrle's reckoning, from a note dated to the Friday after Pentecost, which was also the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had found the years in which that Friday fell on 13 June." | PASS. "feria VI infra octavam pentecostes scil. festo s. Antonii" and "wie schon Papebroch berechnete, diese fer. VI … nur in den J. 1317, 1337 und 1348 auf den 13. Juni, das Fest des hl. Antonius" (EHRLE1 l.27791-27795, OCR "octaram", "18. Jani"). The dropped condition is restored. 24 and 16 words. |
| 5 | B3-M1 | Clareno card `legacy.traces`: "Rader grants that Ambrose does not give his name, and says the description makes plain who is meant." | FAIL (R4-M4). Source holds: "et quamvis Angeli nomen non exprimat, ita tamen describit et depingit illum, ut res oculis tangi possit" (PG88 l.43306-43307). The idiom is fixed, but "his name" now reads as Ambrose's own. |
| 6 | B3-M2 | Clareno card `uncertain`, authorship: "… and Ehrle reports doubts from Richard, writing in 1884, and from Professor Felice Tocco." | FAIL (R4-M5). The source holds: "Richard 1) schliesst sich blindlings den erwähnten Zweifeln Affós an" (EHRLE2 l.5822-5823), note "Bibl. de l'école des Chartes 1884, XLV, 528s." (l.5856). The sentence is now 27 words. |
| 7 | B3-B1 | Clareno card `uncertain` "When he died", first two sentences. | FAIL (R4-M5). The source holds, as in row 4 (EHRLE1 l.27789-27795; "In dem Verzeichniss seiner Wunder … am Ende dieses Verzeichnisses", l.27789-27790). The two sentences run 29 and 30 words. |
| 8 | D3-B1 | Palamas card `uncertain`: "François Combefis, a Dominican, annotates the tome of 1351 in Mansi and calls it heretical." | PASS. The 1347 tome "recitatur inter acta synodi Palamiticae anni 1350, rectius an. 1351, a Combefisio vulgata" (MANSI26 l.10511-10524). The 1351 tome: "regnantibus … Cantacuzeno & Palaeologo" (l.12063-12070). The notes "NOT. PSEUDO-SYNOD. CONSTANTINOPOLIT." (l.19574) say "haeretico plane spiritu conscripta" and "Gregoras, qui ipse in hac Synodo … damnatur" (l.19591-19597). Gregoras was condemned in 1351, so the note is on the 1351 tome. |
| 9 | C3 merged fix, cut | Cabasilas brief para 3: "In 1349 Cabasilas and Demetrios Kydones joined the emperor's plan to leave the world." | FAIL (R4-M1). CANT3 l.6346, "μοναχῶν ἑλέσθαι βίον"; l.6371, "monachorumque instituta sectari"; l.6395, "τὴν ἐκ τοῦ βίου ἀναχώρησιν"; l.6420-6427, the monasteries of St Mamas and then the Mangana. The cut drops the one word that says what kind of plan this was. |
| 10 | C3 merged fix, cut | Cabasilas brief para 3: "Gass finds him named among the followers of Gregory Palamas." | PASS. "unter den Anhängern des Palamas genannt und für sie in die Schranken tretend" (GASS l.1233-1235). Dropping "standing up for them" leaves a true and weaker sentence, and the records keep the full quotation. No false sense. |
| 11 | C3-B1, C3-B2, A3-B1 | Cabasilas brief para 5 (whole paragraph). | FAIL (R4-M2), on the pronoun only. The sources hold. Fabricius: "Nili Cabasilae Thessalonicensis ex fratre nepos, ejusdemque, defuncti vita, in munere successor fuit" (PG150 l.26071-26072). Gass: "verwaltete dasselbe Amt zehn Jahr nachher (nach 1350), so dass zwischen Beide nur die bischöfliche Regierung des Gregorius Palamas … fällt" (GASS l.1374-1377). Jugie: "On a fait de lui, sans aucune preuve serieuse, le successeur de son oncle … qui a du lui venir de ce qu'on l'a confondu souvent avec Nil" (PO19 l.39892-39895, 39914). Each claim sits with its own witness, "also" does not make Gass agree to a direct succession, and the see is told as contested. |
| 12 | C3-B2, A3-B1 | Cabasilas card `role`: "… archbishop of Thessalonica, by Fabricius and Gass, though Martin Jugie doubts it" | PASS. Sources as in row 11. The Thessalonica record is no longer counted as a witness that names him. 25 words. |
| 13 | C3-B1, C3-B2, C3-M1, A3-B1 | Cabasilas card `uncertain` 1 (whole item). | FAIL (R4-M2), on pronouns only. Each witness holds. Fabricius and Migne: PG150 l.26071-26072, 343-346 ("NICOLAUS CABASILA, THESSALONICENSIS METROPOLITA"). Gass on Palamas between them: GASS l.1374-1377. Gass on "nach einigen Jahren", "nicht vor 1354": l.1782-1785. The Synodikon's "Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης" and Gass's "dass er nämlich … gekämpft habe": l.1917, 1884-1888. Kantakouzenos's "ὄντα ἔτι ἰδιώτην": CANT3 l.16601-16602. Jugie, "ni Jean Cantacuzene, ni les suscriptions des manuscrits, ni le Synodicon de l'Eglise de Thessalonique ne soufflent mot de ce titre": PO19 l.39893-39895. Every sentence is 23 words or fewer. |
| 14 | A3-B1 | Cabasilas card `sources.about`, Jugie entry. | PASS. "HOMELIES MARIALES BYZANTINES … MARTIN JUGIE … II … XI. NICOLAS CABASILAS" (PO19 l.18203-18218); "NICOLAS CABASILAS … INTRODUCTION" (l.39869-39879), in French; tome XIX, 1926 (l.3-9; imprimatur 30 December 1925, l.18248). |
| 15 | A3-M3 | README para 3: "405 to 407 words … grade 6.8 to 8.6 and Flesch Reading Ease 61.4 to 71.5." | PASS. `wc -w` 405-407; `grade_text` FK 6.79 to 8.59, Flesch 61.37 to 71.51. |
| 16 | B3-M3 | README Clareno: "… using Papebroch's list of the years in which the Friday after Pentecost fell on 13 June …" | PASS (EHRLE1 l.27791-27795). |
| 17 | A3-B1, C3-B2 | README Cabasilas bullet. | FAIL (R4-M2), on the pronoun only. The claims match the card and records, and the see is tagged Contested (records claim "Archbishop…", `contested_claims`). |
| 18 | A3-M1 | Records, "Scudder on the return…": the added Gobelinus and Platina lines. | PASS (MANSI26 l.111555-111556; BIRGL l.98786-98787). |
| 19 | A3-M2 | Records, "Gobelinus, in Mansi's notice…", and the Rome claim, BIRGE l.956-961. | PASS. BIRGE l.955 is blank, and l.956-961 hold the Extravagantes, "xv annis, antequam veniret Papa". |
| 20 | B3-B1 | Records, "Ehrle's reckoning of the year": "this Friday after Pentecost ('diese fer. VI')". | PASS (EHRLE1 l.27792-27795). |
| 21 | D3-B1 | Records, "Combefis's note": the 1351 tome, its witness lines. | PASS (MANSI26 l.10511-10524, 12063-12070, 12189, 19574, 19583, 19592-19597). |
| 22 | D3-M1 | Records, "Paisius on the copies…", the Basil claim, "Meyer 1894…". | PASS. "Отца Паісія, настоятеля Нямецкаго Вознесенскаго Монастыря" (PAISZ l.3993-3994, OCR "Патсія"); "старецъ схимонахъ Василій въ своемъ скиту, именуемомъ Поляномерульскимъ" (l.3988-3990); "Старца Поляномерульской обители Василія" (l.14215, OCR "Ноляномерульской"); "DIE HAUPTURKUNDEN … VON PH. MEYER" (MEYER l.32-48). |
| 23 | C3-B1, C3-B2, A3-B1 | Records, "Archbishop: …" (text, witness, retag to Contested). | FAIL (R4-M6), on witness lines only. Jugie's quotation is verbatim to PO19 l.39892-39895, 39914, with the OCR forms noted. "Mgr Petit" (l.39907) is the same "Mgr Louis Petit" as PO15 l.1, 95. The witness range GASS l.1919-1938 misses l.1917-1918, which carry the quoted "Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης". |
| 24 | C3-M1, A3-B1 | Records `contested_claims`, "Whether and when he became archbishop of Thessalonica" (three sides). | FAIL (R4-M6), on the Gass side's lines only. The three sides each hold. The Gass side cites GASS l.1919-1938 for the Synodikon's Nicholas, which is at l.1917. |
| 25 | follows from A3-B1 | Records `absent_details`, "The date he took the see…". | PASS (PO19 l.39892-39895; GASS l.1785 gives only a bound). |
| 26 | R3_changes last line | Records, "Gass: 'unter den Anhängern des Palamas genannt…' … the Thessalonica Synodikon praises a Nicholas, whom Gass takes for him, against …". | FAIL (R4-M6). The text is right (GASS l.1884-1888, 1935). The witness has no line for Gass's identification, and its "GASS l.1932-1934" is Gass's own text on the manuscripts. The quoted "τοῦ Βαρλαὰμ καὶ Ἀκινδύνου … μανίαν" is at l.1935. |
| 27 | audio | `catherine-of-siena`, `nicholas-cabasilas`, and the other six. | PASS. Each script equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and holds two tags and nothing else. |
| 28 | JSON | All nine JSON files. | PASS (all parse). |

## Findings

No blocking finding. Every changed string is supported by its cited source. Each claim is given to its own witness, and the Cabasilas see is told as contested in every place.

**R4-M1 (Cabasilas brief para 3: the cut "for a monastery" leaves an idiom a listener can mishear).**
- Current text: "In 1349 Cabasilas and Demetrios Kydones joined the emperor's plan to leave the world."
- Source: the emperor and Irene resolve "μοναχῶν ἑλέσθαι βίον" (CANT3 l.6346), "nuntium rebus humanis mittere monachorumque instituta sectari" (l.6371-6372). Cabasilas and Kydones "συνείποντο δὲ αὐτῷ πρὸς τὴν ἐκ τοῦ βίου ἀναχώρησιν" (l.6395-6396, OCR "αυνείποντο"), "Addebant se ad hanc secessionem socios Nicolaus Cabasilas et Demetrius Cydones" (l.6420-6421).
- Fault: in plain modern English, and to a B2 listener, "leave the world" can be heard as "die". The next sentences ("chose a chaste life", "The plan was dropped") do not say it was a monastic plan. The cut removed the one word that told the listener what the plan was.
- Replacement (±0 words): "In 1349 Cabasilas and Demetrios Kydones joined the emperor's plan to become a monk."
- Audio: the same change in `audio/nicholas-cabasilas.audio.txt`.

**R4-M2 (Cabasilas brief para 5, card `uncertain` 1, README: "editing his sermons" binds to Jugie).**
- Current brief text: "Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof and thinks the title came from confusing him with Nilus."
- Current card text: "Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof that he succeeded Nilus. He says neither Kantakouzenos, nor the titles in the manuscripts, nor the record of the church of Thessalonica gives him that title. He thinks it came from confusion with Nilus."
- Current README text: "Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof."
- Source: Jugie edits Cabasilas's three homilies on the Nativity, Annunciation and Dormition (PO19 l.18203-18218, 39869-39879, 39921, "Les trois homelies mariales que nous publions").
- Fault: Jugie is new to the listener. After "Martin Jugie," the default reading of "his sermons" is Jugie's own. In the card, "He says" comes straight after "he succeeded Nilus", where "he" was Cabasilas. The brief wording is the ruling's draft. The fix changes one word in it and no claim.
- Replacement, brief (±0 words): "Martin Jugie, editing Cabasilas's sermons on Mary in 1926, finds no serious proof and thinks the title came from confusing him with Nilus."
- Replacement, card: "Martin Jugie, editing Cabasilas's sermons on Mary in 1926, finds no serious proof that he succeeded Nilus. Jugie says neither Kantakouzenos, nor the titles in the manuscripts, nor the record of the church of Thessalonica gives him that title. He thinks it came from confusion with Nilus."
- Replacement, README: "Martin Jugie, editing Cabasilas's sermons on Mary in 1926, finds no serious proof."
- Audio: the same brief change in `audio/nicholas-cabasilas.audio.txt`.
- Grade of the brief with R4-M1 and R4-M2 both applied (scratch copy): 405 words, FK 8.11, Flesch 60.52, which passes. R4-M2 must go with "become a monk" in R4-M1: "enter a monastery" with "Cabasilas's" scores Flesch 59.88 and fails. With both applied, the README Flesch range becomes 60.5 to 71.5.

**R4-M3 (Bridget card `legacy.remembered` 4: "him" can be heard as Gobelinus).**
- Current text: "They reached him through Alphonso."
- Source: "instinctu & revelatione Dei, quae sanctae Brigittae … aliquoties obtigerat, perque Alphonsum quemdam eremitam illi secundo insinuata erat" (MANSI26 l.53404-53408). "Illi" is the pope.
- Fault: the split puts Gobelinus last before "him", so a reader can take it that the revelations reached the chronicler.
- Replacement: "They reached Gregory through Alphonso."

**R4-M4 (Clareno card `legacy.traces` 1: "his name" binds to Ambrose).**
- Current text: "Rader grants that Ambrose does not give his name, and says the description makes plain who is meant."
- Source: "et quamvis Angeli nomen non exprimat, ita tamen describit et depingit illum, ut res oculis tangi possit" (PG88 l.43306-43307).
- Fault: "Ambrose does not give his name" reads as Ambrose's own name. Angelo was last named two sentences back.
- Replacement: "Rader grants that Ambrose does not give Angelo's name, and says the description makes plain who is meant."

**R4-M5 (Clareno card `uncertain`: three sentences over about 25 words after the R3 fixes).**
- Current text, authorship item (27 words): "Affò, an eighteenth-century writer, asked on what ground Wadding gave it to Angelo, and Ehrle reports doubts from Richard, writing in 1884, and from Professor Felice Tocco."
- Replacement: "Affò, an eighteenth-century writer, asked on what ground Wadding gave it to Angelo. Ehrle reports doubts from Richard, writing in 1884, and from Professor Felice Tocco."
- Current text, "When he died" (29 and 30 words): "Ehrle fixed 1337 from a note at the end of the list of his miracles, dated to the Friday after Pentecost and the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had already found that in the first half of the fourteenth century the Friday after Pentecost fell on 13 June only in 1317, 1337 and 1348."
- Replacement (14, 17 and 23 words): "Ehrle fixed 1337 from a note at the end of the list of his miracles. The note is dated to the Friday after Pentecost, which was the feast of Saint Anthony, 13 June. Papebroch had already found that in the first half of the fourteenth century this Friday fell on 13 June only in 1317, 1337 and 1348."
- Source: EHRLE1 l.27789-27795: "am Ende dieses Verzeichnisses … feria VI infra octavam pentecostes scil. festo s. Antonii … wie schon Papebroch berechnete, diese fer. VI in der … ersten Hälfte des 14. Jahrhunderts nur in den J. 1317, 1337 und 1348 auf den 13. Juni". "Scil." makes the feast the same day as the Friday, so "which was" is the closer reading. "Daniel Papebroch, a Bollandist" is already given at his first card mention, in `dates`. The rest of the item is unchanged.

**R4-M6 (records: GASS witness lines for the Thessalonica Synodikon).**
- Source: GASS l.1917, "e) NixoXdov tov dyuutdtov fAtjtgofJtoXltov 0saaaXovUij9 tov" (OCR for "Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης τοῦ"), continued at l.1918. The footnote resumes at l.1935, "t^v rov Bagkadfi mal *u4xivSvvov msvo/iavlav", and runs to "alojvla fivi^iirj, Le Quien" at l.1937 and "Synodicon" at l.1938. Gass's identification is at l.1884-1888. Lines 1919-1934 are blank lines, a page number and Gass's main text on the manuscripts.
- Claim "Archbishop: …", current witness fragment: "GASS (cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt) l.1373-1377, 1773-1786, 1884-1888, 1919-1938". Replacement: "GASS (cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt) l.1373-1377, 1773-1786, 1884-1888, 1917-1918, 1935-1938".
- `contested_claims`, Gass side, current fragment: "(GASS l.1884-1888, 1919-1938)". Replacement: "(GASS l.1884-1888, 1917-1918, 1935-1938)".
- Claim "Gass: 'unter den Anhängern des Palamas genannt…'", current witness fragment: "GASS l.1932-1934". Replacement: "GASS l.1884-1888, 1917-1918, 1935-1937".

## Count

- Blocking: 0.
- Minor: 6 (R4-M1 to R4-M6).
- Rows checked: 28. 17 PASS, counting the audio and JSON rows. 11 FAIL on a minor point, and in each of those the source supports the claim.
- The fixes for all five R3 blocking points (D3-B1, B3-B1, C3-B1, C3-B2, A3-B1) are correct against their sources.

Verdict: NOT CLEAR (0 blocking, 6 minor)
