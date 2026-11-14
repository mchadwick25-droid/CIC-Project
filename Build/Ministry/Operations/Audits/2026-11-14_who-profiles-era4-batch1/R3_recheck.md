# R3 recheck: era 4 batch 1

Round 3, the last, ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. The parts follow, unchanged.

## R3 recheck, part 1: Bede, Hild of Whitby, Aidan of Lindisfarne, Adomnán of Iona

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git writes and no web, paid or model calls, and used local scripts and read-only git only. Inputs: R1_review.md parts A and B, R1_changes.md parts A and B, R2_recheck.md part 1, R2_changes.md part 1, the current batch 1 files, `records.json`, the scratchpad records and the Bede notes, and the batch README. Changed text was found by comparing the current briefs and cards with the wording R1 and R2 quote. For every R1 and R2 finding, and for every changed sentence, I opened the cited lines again in the vendored file and read them in context, folding OCR noise, double spaces and hyphen breaks.

**Mechanical (all four), by script.**

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card order, no empty fields | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| bede-of-jarrow (major) | 405 | 2:30 | 6.5 | 71.8 | yes (1 calmly, 1 warmly) | yes | 24 |
| hild-of-whitby (major) | 404 | 2:30 | 5.6 | 78.1 | yes | yes | 24 |
| aidan-of-lindisfarne (major) | 405 | 2:30 | 6.3 | 77.7 | yes | yes | 25 (P1, at the limit) |
| adomnan-of-iona (major) | 404 | 2:30 | 7.3 | 71.1 | yes | yes | 24 |

No tag is in a brief or card. No card sentence outside `sources` runs past 25 words. Each card has at most three `keyWorks` (Hild and Aidan have none, rightly). Every `sources` file exists and holds the named work. Each `records.json` entry is identical to its scratchpad record, and every `formation_confidence` is one of the five levels. Each `contested_claims` entry gives two or more sides with witnesses.

---

### Bede

| Finding | Verdict | Evidence |
|---|---|---|
| A-B1 (false absence, "sell Christ") | RESOLVED | "Seynt Bede seij?, We sellen Crist whanne we forsaken treufe, and taken falsnesse and meyntene it" (ARNOLD3 l.17672-17674), after priests who say Mass "in pride, coveitise" (l.17665-17666). Card `legacy.traces` 6 tells it faithfully; the Arnold volume is in `sources.about`; the absent detail is gone. |
| A-M1 (speaker shifted) | RESOLVED | "Now it is finished" … "Well, thou hast spoken truth; it is finished" (PLUMMER l.5888-5890). |
| A-M2 ("other chronicles") | RESOLVED | "734 is the date of all MSS. of the Sax. Chron." (PLUMMER l.5479-5480). |
| A-M3 (heresy charge with no content) | RESOLVED | "Epistola ad Plegwinum apologetica de Sex Aetatibus Saeculi … Plegwin, a monk of Hexham" (l.10480-10484); six ages at l.2856-2858. Declining the Easter beat is right at the cap. |
| A-M4 (Nothelm's purpose; Jane sentence) | RESOLVED | "searched into the archives … found there some epistles of the blessed Pope Gregory" (GILES l.166-168). Jane "has … supplied the Biographical Notice" (l.15581-15584); "practically the only authority for the history of England from the Saxon invasion to the year 732" (l.15634-15637). 24 words. |
| A-M5 (mixed person) | RESOLVED | "the words of thy wisdom" and "come to thee, the fountain of all wisdom" (GILES l.15563-15566). |
| A-M6 (two books joined) | RESOLVED | "Bede himself calls the longer work De Temporibus Liber Maior" (PLUMMER l.2736-2738). |
| A-M7 (birth years; Mayor and Lumby) | RESOLVED | Ann. Lindisf. and S. D. for 677, "Stevenson places his birth in 674, but on very precarious grounds. Church Historians", Fl. Wig. 678 (l.540-561). |
| A-M8 (beat line "Rome honors him.") | RESOLVED | "Homily by the Venerable Bede" (BREVIARY l.30252); "From the Venerable Bede's History" (l.61583-61584). No count given. |
| A-M9 (two census differences withdrawn) | RESOLVED | "AD CAROLUM MAGNUM. (Anno 800.) Commendat … libros [vii] adversus Felicem" (ALCUIN l.9436-9442). |
| R2-1-M1 (card `dates`, "other chronicles") | RESOLVED | "734 is the date of all MSS. of the Sax. Chron., of the Ann. Ult., W. M. …" (PLUMMER l.5479-5481). The card now reads "the Saxon Chronicle and several other chronicles give 734", which matches `uncertain` 1. |
| R2-1-M2 (two census-side points) | RESOLVED | Notes items 5 and 6 added, each with its lines (GILES l.6988-6990; PLUMMER l.2736-2738). |

**Changed strings checked.** Card `dates` (R2-1-M1): PASS. Nothing else on the profile changed in round 2. I also re-read the whole brief against its lines and found no fault R1 and R2 missed: the deathbed (PLUMMER l.5884-5895), Bede's own life (GILES l.15414-15432), the plague (PLUMMER l.606-636, "can hardly be any other than Bede himself"), the heresy charge (l.10483-10486, "in connexion with the De Temporibus", Plummer's words, told through him), Nothelm and the "faithful testimony of innumerable witnesses" for the Northumbrians (GILES l.213-219), and the closing prayer (l.15562-15566). A fresh search of all `cic/texts/` for Plegwin, Pleguin, Pleguuin and "lascivientibus rusticis" finds only the Plummer file, so `uncertain` 6 ("known here only from Plummer") holds.

**New findings.** None.

**Verdict: CLEAR** (0 blocking, 0 minor).

---

### Hild of Whitby

| Finding | Verdict | Evidence |
|---|---|---|
| A-B2 (chapter count) | RESOLVED | Her life (IV.23), three more chapters (III.24, GILES l.7768-7778; III.25, l.7958-7967; IV.24) and the V.24 annal. |
| A-M10 (comparison widened) | RESOLVED | "Others after him attempted … but none could ever compare with him" (GILES l.11147-11150). |
| A-M11 ("the Scots") | RESOLVED | "the Scots, who, migrating from Ireland" (GILES l.381-382). |
| A-M12 (Colman; Pope John) | RESOLVED | Colman of "the church of Lindisfarne" (GILES l.8260-8269); "praedecessore nostro Agathone" and "Hylde religiose memorie" (RAINE l.9419-9425). |
| A-M13 (tail misframes Bede) | RESOLVED | "it pleased Almighty God, by a manifest vision, to make known her death" (GILES l.11063-11065); "It is also reported" (l.11111), in "the same monastery" where she died. |
| A-M14 (Plummer gloss; assent) | RESOLVED | "all present, both great and small, gave their assent" (GILES l.8214-8216); "the Irish monks of Iona, by whom Northumbria was reconverted" (PLUMMER l.988-990). |
| A-M15 (Tatfrid "before him") | RESOLVED | "Before the aforesaid man of God, Bosel, Tatfrid … had been chosen bishop there, from the same abbess's monastery" (GILES l.11008-11012). |
| A-M16 (translation fault; "Hild" repeated) | RESOLVED | Both done. |
| R2-1-M3 ("later" with no anchor) | RESOLVED | P2 now reads "writing about fifty years after her death": 731 (GILES l.15408) less 680 (l.15362-15363). The word paid for it: "verses praising God", from "began to sing verses to the praise of God" (l.11178-11179). Faithful. |
| R2-1-M4 (oblique Latin forms as names) | RESOLVED | `otherNames` is `["Hilda"]` (GILES l.10891; AASS June 5 l.95275). The records claim marks "Hilde" and "Hylde" as Latin case forms (RAINE l.5083, 9425). |

**Changed strings checked.** Brief P1 last clause and P2 second sentence: PASS. Card `otherNames`: PASS. Audio carries both. I re-read the whole brief against its lines: Caedmon (GILES l.11137-11203), Hereric and Edwin (l.10899-10904), Cale and the recall (l.10923-10926; PLUMMER l.24865-24866), Whitby "of men and women" (GILES l.11517-11519), peace and charity, "no person was there rich, and none poor", kings and princes, five bishops and "Mother" (l.10954-11016), the synod ("The kings, both father and son, came thither", l.7962-7963), Stephen and Pope John (RAINE l.5067-5081, 9395-9428), the fever, the charge to keep peace, and the dream (GILES l.11021-11060; "whose life was a bright example" verbatim at l.11033-11034). No new fault.

**New findings.** None.

**Verdict: CLEAR** (0 blocking, 0 minor).

---

### Aidan of Lindisfarne

| Finding | Verdict | Evidence |
|---|---|---|
| B-B1 (Plummer's "sad" on the wrong sentence) | RESOLVED | "It is sad that he should think it necessary to pause … to say that he 'much detests' his mode of keeping Easter" (PLUM l.2806-2809). "very much detesting the same" (GILES l.6987-6988) now comes first; the patient tolerance (l.7903-7905) is a separate grant. |
| B-B2 (Cuthbert's timing one-sided) | RESOLVED | "etenim post paucas dies … eadem hora noctis … audierunt" (AASS Mar. 3 l.38829-38832); "agnovitque mane facto Antistitem Lindisfarnensis Ecclesiae Aidanum … per id temporis, quo viderat" (l.34345-34350). Both Lives in place. |
| B-M1 (no identifier) | RESOLVED | "Then said Aidan, who was also present in the council" (GILES l.5978-5982); sent "from the aforesaid island" (l.5989-5990). |
| B-M2 (stiff opening) | RESOLVED | "It is reported" (GILES l.5965). |
| B-M3 ("free people"; "wrongly") | RESOLVED | "ransoming such as had been wrongfully sold for slaves" (GILES l.5960-5961), in brief and card. |
| B-M4 ("see" undefined) | RESOLVED (through R2-1-M6) | R2 judged the decline wrong; the R2 fix now carries it. |
| B-M5 (card sources) | RESOLVED | I.34, Huyshe, Rees and the Annales Cambriae listed; "Maidoc, qui et Aidanus" (REES l.6518); "Vetus Menevia … the Monastery he had founded in Menevia" (l.17998-18003). |
| B-M6 (records tag) | RESOLVED | The c.700 claim is Dominant Modern Reconstruction, with "Videtur". |
| R2-1-M6 ("see" heard as "sea") | RESOLVED | "Oswald made Lindisfarne, an island at high tide, the seat of Aidan's bishopric." Bede: "the king appointed him his episcopal see in the isle of Lindisfarne … enclosed by the waves of the sea like an island" (GILES l.5763-5767). "Aidan's" removes the doubt over whose bishopric. |
| R2-1-M7 ("later" counted from the 630s) | RESOLVED | "…from Bede, who wrote some eighty years after his death, learning from those who knew him." Bede wrote of 731 (GILES l.15189-15191); Aidan died in 651 (l.15317-15318); "as near as I could be informed by those that knew him" (l.7003-7004). 23 words. |

**Changed strings checked.** Brief P2, second and fourth sentences: PASS. Audio carries both. I re-read the rest of the brief against its lines: the council (GILES l.5965-5999, "a great council", "the milk of more easy doctrine" verbatim), the interpreting king (l.5772-5782), the walking mission, alms and ransom (l.5919-5963), Oswin's horse and Aidan's tears (l.6761-6818), the Easter custom "according to the custom of his country … from the fourteenth to the twentieth moon" (l.5749-5752), and the closing quotation "These things I much love and admire in the aforesaid bishop" (l.7009-7010). No new fault.

**New findings.** None.

**Verdict: CLEAR** (0 blocking, 0 minor).

---

### Adomnán of Iona

| Finding | Verdict | Evidence |
|---|---|---|
| B-M7 (Lebar Brecc and White without context) | RESOLVED | Brief: "Newport White, who translated Patrick's writings" (WHITE title page l.103-119); "a late medieval Irish manuscript" covers both held dates. The card now carries both, through R2-1-M5 and R2-1-M8. |
| B-M8 (seems to die in Ireland) | RESOLVED | "Returning to his island, after having celebrated the canonical Easter in Ireland … he departed this life before the next year came round" (GILES l.13582-13587). |
| B-M9 (Arculf "from Jerusalem") | RESOLVED | "returning home by sea" (GILES l.13598-13602). |
| B-M10 (Ceolfrid unmarked; "tonsure") | RESOLVED | Naitan asked "concerning the form and manner of tonsure" (GILES l.14338-14342); "why do you imitate the tonsure of him whom St. Peter anathematised?" (l.14893-14895). |
| B-M11 (four names for one Easter) | RESOLVED | "the Roman Easter" in brief P5, `knownFor`, `dates`, traces 1-2; "Roman reckoning" only in `uncertain` 5. |
| B-M12 (second tradition; census year) | DECLINED-OK | Census Insular movement: c.450-664; Medieval Irish: c.664-1169 (world-census.json). The Insular entry names "Adomnán — abbot of Iona" among its voices. The census 679 is logged in the notes for the coordinator. |
| B-M13 (Bede title) | RESOLVED | III.4 (GILES l.5877-5878) and IV.25 (l.11316-11317) are in the title. |
| B-M14 (namesake's nominative) | RESOLVED | "Adamnanus pre[s]byter et abbas monachorum qui erant in insula Hii" (PL88 l.66004-66005). |
| R2-1-M5 (traces 4: 28 words; White without context) | RESOLVED | "Both Aedh and Muirchu subscribed the Acts of the Synod held at Birr, by Adamnan, a.d. 695-697", with Aedh "bishop of Sleibte (Sletty)" (WHITE l.3763-3768). The two sentences are 21 and 16 words. |
| R2-1-M8 (traces 5 and `uncertain` 3: one held date, no context) | RESOLVED | Traces 5: "a late medieval Irish manuscript … Whitley Stokes prints it", which keeps Stokes as printer of the note only (STOKES-TRIP l.13852, 13859-13866). `uncertain` 3 gives both dates: "the fifteenth-century manuscript, the Leabhar Breac" (HUY l.1683-1685) and "compiled from ancient sources about the end of the fourteenth century" (antiphonary-of-bangor-pt2 l.17716-17719). |

**Changed strings checked.** Card `legacy.traces` 4 and 5, `uncertain` 3: PASS. I re-read the whole brief against its lines: Ceolfrid's letter (GILES l.14883-14903, the answer verbatim), Huyshe's life (HUY l.1979-2004, "came as a refugee" behind "the exiled Aldfrith"), the preface (l.2084-2087, verbatim), Failbeus and Oswald, the plague visit (l.9120-9132, "my friend, King Aldfrid" verbatim), Bede V.15 (GILES l.13551-13592; "a good and wise man, and remarkably learned in Holy Scripture" verbatim), White and the Lebar Brecc note, and the closing prayer ("Obsecro itaque eos quicunque breves legerint libellos, ut pro eodem sancto sacerdote Arculfo divinam precentur clementiam", PL88 l.68715-68718). No new fault in the brief.

#### New findings

- **R3-1-M1 MINOR (card `uncertain` 5; items 1 and 5; a witness dropped across a split; unchanged text that R1 and R2 did not flag).** "Bede says God so ordered it that he died before Easter came round again. So this lover of peace did not have to quarrel more seriously with those who would not follow him." The second sentence stands as the narrator's own statement, but it is Bede's providential reading of the death: "the Divine goodness so ordaining it, that as he was a great lover of peace and unity, he should be taken away to everlasting life before he should be obliged, on the return of the time of Easter, to quarrel still more seriously with those that would not follow him in the truth" (GILES l.13587-13592). This is the fault batch 8 fixed in R3-A-M2. Fix, second sentence only: "So, Bede adds, this lover of peace did not have to quarrel more seriously with those who would not follow him." (19 words; "adds" keeps it from echoing "Bede says" in the sentence before.)

**Verdict: CLEAR** (0 blocking, 1 minor).

---

### The batch README (opening paragraphs and the lines on these four)

Checked against the era 4 scan, `world-census.json`, the Decision-Log and the files.

- True: none of the eight was written before (no other Who-Profiles folder holds these ids). Bede's id is the live census id, `bede-of-jarrow` (`movements`, `toldWithin` anglo-saxon-christianity). Seven briefs run 402 to 405 words and Nennius 340, about 2:06. The scan's Major column proposes "yes" for all eight (Who_Scan_Era4.md l.27-31, 39-41). The Palladius, John of Ephesus and Gregory of Tours rulings are in the Decision-Log (l.2540, 2659, 2677). Bede's held life, list of works and Cuthbert's letter are all held (GILES l.15414-15560; PLUMMER l.5511-5960, 11212-11425).
- Traditions: the three calls are sound. Aidan: both census movements name him ("Aidan — Irish monk from Iona who founded Lindisfarne"; "Aidan — the monk sent from Iona in 635"), and 635 to 651 falls in both windows (597-793; c.450-664). Adomnán: 679 to 704 falls in Medieval Irish Christianity (c.664-1169), which does not name him; the Insular movement names him and covers Iona, as the README says. The spelling "Adomnán of Iona" matches the census voices line and the era 3 Columba card.
- Prose: plain, no tells, no sentence past 25 words.

#### New finding

- **R3-1-M2 MINOR (README, first paragraph; a claim that is not true as worded).** "These are the first era 4 WHO rows of `…/Who_Scan_Era4.md`". The scan's WHO rows run Bede, Boniface, Aidan, Hild, Adomnán (l.27-31), then Theodore of Tarsus, Willibrord, Leoba, Muirchu, Tirechan, Cogitosus and Jonas of Bobbio (l.32-38), before Nennius, Alcuin and Dhuoda (l.39-41). The batch is the first eight WHO rows whose Major column proposes "yes"; the seven skipped rows propose "judgment call" or "no". Fix: "These are the first eight era 4 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md` whose Major column proposes yes, the first batch under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full."

#### Note for the coordinator (not a finding)

The README twice says points are "logged in Open-Gaps" (the Bede census differences, and the three tradition calls). Open-Gaps has no era 4 batch 1 entry yet. That follows the batch 8 practice, where the entry was written at close. The close entry should carry the Bede census-difference list (notes items 1 to 6), the three tradition calls, the census Insular row's 679 for Adomnán (B-M12), and the wanted items in the notes.

---

### Counts

| Profile | R1 findings | R2 findings | Resolved | Declined | New blocking | New minor |
|---|---|---|---|---|---|---|
| Bede | 10 | 2 | 12 | 0 | 0 | 0 |
| Hild of Whitby | 8 | 2 | 10 | 0 | 0 | 0 |
| Aidan of Lindisfarne | 8 | 2 | 10 (B-M4 through R2-1-M6) | 0 | 0 | 0 |
| Adomnán of Iona | 8 | 2 | 9 | 1 OK (B-M12) | 0 | 1 (R3-1-M1) |
| README | | | | | 0 | 1 (R3-1-M2) |

### Verdicts

- Bede: CLEAR
- Hild of Whitby: CLEAR
- Aidan of Lindisfarne: CLEAR
- Adomnán of Iona: CLEAR (one minor card fix, R3-1-M1, in final wording above)

## R3 recheck, part 2: Boniface of Mainz, Alcuin of York, Dhuoda, Nennius

Reviewer: independent Opus, first sight of these files. I edited no profile file and made no git writes, web, paid or model calls. I used local scripts and read-only git only. Inputs: R1_review.md parts C and D, R1_changes.md parts C and D, R2_recheck.md part 2, R2_changes.md part 2, the batch README, the current batch 1 files, `records.json`, the scratchpad records and the drafter's notes. Changed text since round 2 was found with `git diff --word-diff a62c9e9b 1070cfcb` on the four profiles. Only Dhuoda's brief P5 and card `dates`, and Nennius's card `uncertain` 3 and `legacy.remembered` 2, changed, as R2_changes says. Boniface and Alcuin are unchanged since round 1's fixes. I opened the cited lines again in `cic/texts/` for every R2 finding and for the R1 fixes I spot-checked.

**Mechanical (all four), by script.**

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card order, no empty fields |
|---|---|---|---|---|---|---|
| boniface-of-mainz (major) | 403 | 2:29 | 7.5 | 69.8 | yes (1 calmly at start, 1 warmly on last paragraph) | yes |
| alcuin-of-york (major) | 404 | 2:30 | 7.7 | 66.3 | yes | yes |
| dhuoda (major) | 402 | 2:29 | 7.1 | 75.5 | yes | yes |
| nennius (major mark, standard length) | 340 | 2:06 | 6.6 | 70.0 | yes | yes (no `otherNames`, correctly absent) |

No tag appears in any brief or card. Each card has at most three `keyWorks`, and every `sources` file exists. Each `records.json` entry equals its scratchpad record. No narrator sentence in any brief passes 25 words. The longest are Nennius P4 at 25 and Boniface's closing quotation of the Stephen letter at 27, which is Kylie's verbatim sentence (l.1550-1553). Card sentences past 25 words: Boniface `place` (50) and `role` (28) and Alcuin `place` (32) are semicolon lists, as the fleet's cards are. One prose sentence passes, in Boniface `keyWorks` 1 (R3-C-M1).

---

### Boniface of Mainz

| Earlier finding | Verdict | Evidence |
|---|---|---|
| C-B1 ("aliquid" dropped) | RESOLVED | "promisit, se de aecclesiastica religione ... aliquid corrigere et emendare velle" (OCR "rclij:,ione", "conngerc ct", CAP l.2202-2204). "had promised to put right something of the church's order" keeps it. "calcata et dissipata ... per sexaginta vel septuaginta annos" carries the next sentence. |
| C-M1 (754 on the departure) | RESOLVED | "for the last time took boat on the Rhine" (Kylie l.1749-1750) has no year; "At Docking ... on June 5, 754" (l.1814-1815). The winding-sheet: "he bade Lul put a winding-sheet for his body in the chest with his books" (l.1751-1753). |
| C-M2 (Cynehilda; tense) | RESOLVED | As R2 found. |
| C-M3 ("reminded"; "wont") | RESOLVED | "Have pity on them because even they themselves are wont to say 'We are of one blood and one bone'" (l.7524-7525). |
| C-M4 to C-M8 | RESOLVED | As R2 found. |
| C-M9 (census "robbers") | DECLINED-OK | Census-side, in the notes. |
| Lioba / Leoba | DECLINED-OK | Coordinator's call, in the notes. |
| Round 2 | none raised | |

**New findings.**

- **R3-C-M1 MINOR (card `keyWorks` 1 `about`; item 4; a nested sentence of 28 words; unchanged since the draft, missed by rounds 1 and 2).** "He asks them to pray that God would turn the hearts of the pagan Saxons, who themselves say, he writes, "We are of one blood and one bone."" Kylie: "may turn to the Catholic faith the hearts of the pagan Saxons ... Have pity on them because even they themselves are wont to say 'We are of one blood and one bone'" (l.7518-7525). Fix, split at the joint: 'He asks them to pray that God would turn the hearts of the pagan Saxons. The Saxons themselves say, he writes, "We are of one blood and one bone."' (14 and 13 words. The quote is verbatim.)

Not findings: "In 742 Carloman ... called a synod" matches Carloman's own "concilium et synodum ... congregavi" (CAP l.2227-2229). "archiepiscopus Mogontiacensis in Frisia verbum Dei praedicans a paganis interfectus" (RFA l.1668-1670) carries P1's last sentence and the card's see. The card's `dates` and `place` end without a full stop, as six of the eight cards here and 75 of the 76 era 3 cards do.

---

### Alcuin of York

| Earlier finding | Verdict | Evidence |
|---|---|---|
| C-B2 ("his master" heard as Charlemagne) | RESOLVED | As R2 found. The two claims are separate sentences, and "His teacher" names whose charge it was. |
| C-M10 to C-M16 | RESOLVED (C-M11 DECLINED-OK) | As R2 found. Spot-checked: "anno 780 cum mortuo Ælberto Eboracensi episcopo pro Eanbaldi successoris obtinendo pallio Romam missus inde rediret, Parma occurrit Carolo Magno, qui ipsum in Franciam invitavit" (PL101 l.113483-113487) carries P3's first two sentences. Frankfurt c. 56, the last chapter, asks the synod to receive "Alquinum" into its fellowship and prayers (CAP l.5939-5942). P4's "end with" holds. |
| C-M17 (census) | DECLINED-OK | Census-side, in the notes. |
| Round 2 | none raised | |

**New findings.** None.

---

### Dhuoda

| Earlier finding | Verdict | Evidence |
|---|---|---|
| D-B1, D-M1 to D-M11, D-M13 | RESOLVED | As R2 found. |
| D-B2 ("si jubet") with R2-D-B1 (the split) | RESOLVED | "She told William to pray often that God would give his father peace with all, if it could be, and heaven, if God willed." Ch. LVII: "ut pro eo frequens et assidue orator sis ... ut det illi Deus ... pacem et concordiam, si fieri potest, cum omnibus ... ad regnum, si jubet, faciat pervenire supernum" (DHU l.10104-10112). Both conditions sit inside the prayer, and "pray often" renders "frequens et assidue". The dropped "tempore dum vivet", "post expletum vitae praesentis" and "cum fructu poenitentiae" are a time and a means, not conditions. The sentence is 24 words. Audio and records match. |
| D-M12 (full stop on `dates`) | RESOLVED as asked | Coordinator's note, not a finding: the fleet's cards end `dates` without a stop (75 of 76 in era 3, and the other six cards here). The two cards D-M12 changed are now the exceptions. |
| R2-D-M1 (card `dates`: "its") | RESOLVED | "Édouard Bondurand reckons from the book's closing note that she began it on 30 November 841." Bondurand: "Le manuel de Dhuoda a donc été commencé le 30 novembre 841" (l.13224-13229). |
| R2-D-M2 (notes: "dead before 813") | RESOLVED | `notes/dhuoda.md` l.15 reads "a Dodana dead by 813". |

**New findings.** None. Also checked: P3's Nithard sentence ("victoriam autem ut Karoli esse didicit, filium suum Willelmum ad illum", NITH l.2302-2305, after "praedicti proelii", the Fontenoy battle). P4's teachers sentence ("habebis doctores qui te plura et ampliora utilitatis doceant documenta, sed non aequali conditione, animo ardentis in pectore, sicut ego genitrix tua", DHU l.3166-3169). P4's unnamed brother ("cujus modo inscia sum nominis", l.3171). The interlinear "Carolus" that follows it is set aside by Bondurand's own note, "Dhuoda ignore le nom de son second fils. Elle ne peut donc le nommer Charles" (l.3202-3204). So the brief's "whose name she did not yet know" holds.

---

### Nennius

| Earlier finding | Verdict | Evidence |
|---|---|---|
| N-B1, N-B2, N-B3, N-M1, N-M2, N-M4 to N-M7 | RESOLVED | As R2 found. |
| N-M3 with R2-N-M1 (editor's years) | RESOLVED | `uncertain` 3: "in the year their editor reckons as 768" and "Under the year their editor reckons as 809". The annal reads only "CCCXXIV. Annus. Pasca commutatur apud Brittones ... emendante Elbodugo" (ANN l.2984-2988) and "CCCLXV. Annus. Elbodg archiepiscopus Guenedote regione migravit ad Dominum" (l.3102-3103). The 768 and 809 are the margin (l.2962, 3114). "One of their manuscripts calls him bishop of Gwynedd" holds: "Elbodu episcopus Wenedotiae obiit, B." (l.3176-3177). The records' contested side now says "the editor's 768 ... the editor's 809". |
| R2-N-M2 (`remembered` 2) | RESOLVED | "lived later than Gildas and Taliesin": Badon "is noticed by two contemporaries, Gildas and Taliesin ... The author of the book of Nennius, who lived at a later period, represents the battle of Mount Badon as the twelfth which Arthur fought" (ANN l.1086-1104). |
| R2-N-M3 (notes: Elbodug linked to Giles) | PARTLY | `notes/nennius.md` l.5 is fixed. l.17 still heads the item "Elbotus/Elfoddw" and gives "in 768" and "dying in 809" as the annals' years. See R3-N-M2. |
| N-M8 (no census list line) | DECLINED-OK | Census-side, in the notes. |

**New findings.**

- **R3-N-M1 MINOR (card `dates`; item 4; an undefined term at its first mention on the card; unchanged since the draft).** "Louis Duchesne places the pseudo-Nennius in the ninth century." This is the card's first use of the term. Here it reads as a second man set beside Nennius, and the card does not say what it means until `uncertain` 1. The brief glosses it (N-M2). Duchesne: "l'Historia Britonum du pseudo-Nennius (ix e siècle)" (LP1 l.27343-27344). Fix: "Louis Duchesne, who calls the writer pseudo-Nennius, places him in the ninth century." (15 words.)

- **R3-N-M2 MINOR (process; `notes/nennius.md` l.17; the R2-N-M1 and R2-N-M3 faults left in a second line of the notes).** "Elbotus/Elfoddw: Giles's note makes him bishop of Bangor in 755 (NEN l.46); the Annales Cambriae have the Easter change under Elbodug in 768 and Elbodg, archbishop of Gwynedd, dying in 809". The heading joins Giles's Elbotus to a Welsh form, "Elfoddw", that no held file spells, and so to the annals' man. No held line makes them one man (N-M3). The years are the editor's. The notes feed Open-Gaps. Fix: "Elbotus: Giles's note makes him Elvod, bishop of Bangor in 755 (NEN l.46). The Annales Cambriae have the Easter change under Elbodug in the editor's 768, and Elbodg, archbishop of Gwynedd, dying in the editor's 809, with a variant "episcopus" (ANN l.2962, 2984-2988, 3102-3103, 3114, 3176). No held line makes Giles's Elvod the annals' man. Both are kept on the card."

---

### The batch README: the lines on these four

Checked true: the ids and names; "The Royal Frankish Annals call him archbishop of Mainz" ("Bonifatius archiepiscopus Mogontiacensis", RFA l.1668). "Popes of the name are in the census" is true: Boniface VIII is in `world-census.json`. "Seven run 402 to 405 words" is true: 403, 404, 402, 405, 404, 405 and 404 by `wc -w`. Nennius's 340 words make about 2:06. The attribution is said in the brief (P2), in `uncertain` 1 and in the author line, as the README says. The Nennius name call is sound for the four reasons R1 gave, with the `joshua-the-stylite` precedent. Two lines are wrong.

- **R3-R-M1 MINOR (README, Boniface tradition; a reason that is not true).** "His mission and synods fall before 751, when Carolingian Reform Christianity begins." His last mission does not. The Royal Frankish Annals put his death in Frisia "verbum Dei praedicans" under 754 (RFA l.1660-1670), and his anointing of Pippin, under the annal DCCL with the edition's margin "751" (l.1355-1357), falls in 751 itself. The call itself is sound. The census `anglo-saxon-christianity` row (597 to 793) lists "Boniface" among its people (year 716), and its window covers his whole life. The `carolingian-reform-christianity` row (751 to 888) does not list him. Fix: "Boniface of Mainz reads "Anglo-Saxon Christianity". The census lists him among its people, and its years, 597 to 793, cover his whole life. His synods fall before 751, when Carolingian Reform Christianity begins, and that movement does not list him."

- **R3-R-M2 MINOR (README, Nennius length; a precedent cited for what it did not rule).** "Nennius is a recorder with a thin held life, so he keeps the major mark and runs at standard length, about 2:06, by the rulings for Palladius, John of Ephesus and Gregory of Tours." Those rulings made each recorder not major and kept him at standard length (Decision-Log l.2540, 2659, 2677). They give no basis for keeping a major mark, and "so" makes the mark follow from the thin life. The major mark is the coordinator's ruling (reviewer brief: "all eight are 'major'"). Also, 2:06 is a little past the standard 2:00. Fix: "Nennius keeps the major mark, as the coordinator ruled. He is a recorder with a thin held life, so his brief is held near standard length, about 2:06. The recorders Palladius, John of Ephesus and Gregory of Tours were kept at standard length too, though they were not marked major (the coordinator's call, 2026-11-14)."

Considered and not a finding: the README's "The doubt is over who wrote the Historia Brittonum, not over his name" uses an "X, not Y" shape. It is internal, and the contrast carries the reason for the ruling (R1's reason 4). It is not an empty contrast.

---

### Counts

| Profile | Earlier findings resolved | New blocking | New minor |
|---|---|---|---|
| Boniface of Mainz | 11 of 11 (C-B1, C-M1 to C-M9, Lioba), resolved or declined-OK; no R2 findings | 0 | 1 (R3-C-M1) |
| Alcuin of York | 9 of 9 (C-B2, C-M10 to C-M17), resolved or declined-OK; no R2 findings | 0 | 0 |
| Dhuoda | 15 of 15 R1 and 3 of 3 R2 resolved (D-B2 through R2-D-B1) | 0 | 0 |
| Nennius | 11 of 11 R1 resolved or declined-OK; R2: 2 of 3 resolved, R2-N-M3 partly | 0 | 2 (R3-N-M1; R3-N-M2, process) |
| README (these four) | n/a | 0 | 2 (R3-R-M1, R3-R-M2) |

R3-C-M1 and R3-N-M1 are participant text. Under the brief's rule, changing them after this round needs a cap ruling from Mark. Each fix above is given in final wording, checked against its line. R3-N-M2 and the two README points are not participant text.

### Verdicts
- Boniface of Mainz: CLEAR (0 blocking, 1 minor).
- Alcuin of York: CLEAR (0 blocking, 0 minor).
- Dhuoda: CLEAR (0 blocking, 0 minor).
- Nennius: CLEAR (0 blocking, 2 minor, one of them process).
