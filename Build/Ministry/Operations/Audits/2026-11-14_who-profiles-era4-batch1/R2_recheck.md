# R2 recheck: era 4 batch 1

Round 2 ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or round 1, at full effort. The parts follow, unchanged.

## R2 recheck, part 1: Bede, Hild of Whitby, Aidan of Lindisfarne, Adomnán of Iona

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git, web, paid or model calls, and used local scripts only. Inputs: R1_review.md parts A and B, R1_changes.md parts A and B, the current batch 1 files, `records.json`, the scratchpad records and the Bede notes. Changed text was found by comparing the current briefs and cards with the wording R1 quotes. I opened each cited line again in its vendored file, folding OCR noise, double spaces and hyphen breaks.

**Mechanical checks (all four).** I checked by script that each audio file equals its brief plus `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. All four match, with one tag of each kind, and no tag is in a brief or card. Each card is in Mark's order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks where held, legacy, uncertain, sources), with no empty or null fields and at most three keyWorks. Every `sources` file exists. Each `records.json` entry is identical to its scratchpad record.

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence |
|---|---|---|---|---|---|
| bede-of-jarrow (major, cap about 405) | 405 | 2:30 | 6.5 | 71.8 | 23 |
| hild-of-whitby (major) | 404 | 2:30 | 5.6 | 78.3 | 24 |
| aidan-of-lindisfarne (major) | 405 | 2:30 | 6.2 | 78.3 | 25 (P1) |
| adomnan-of-iona (major) | 404 | 2:30 | 7.3 | 71.1 | 24 |

One card sentence runs past 25 words: Adomnán `legacy.traces` 4, at 28 (R2-1-M5).

---

### Bede

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B1 (false absence of "sell Christ") | RESOLVED | ARNOLD3 l.16380-16382 is the heading "THE CRETE SENTENCE OF CURS EXPOUNED". At l.17672-17674 it reads "Seynt Bede seij?, We sellen Crist whanne we forsaken treufe, and taken falsnesse and meyntene it", after priests who say Mass "in pride, coveitise" (l.17665-17666). The new `legacy.traces` 6 is faithful, and the Arnold volume is in `sources.about`. The absent detail is gone from the records. |
| A-M1 (speaker shifted) | RESOLVED | The boy says "Now it is finished", and Bede answers "Well, thou hast spoken truth ; it is finished" (PLUMMER l.5888-5890). |
| A-M2 ("other chronicles") | RESOLVED in the brief | "734 is the date of all MSS. of the Sax. Chron." (PLUMMER l.5479-5480). The card's `dates` keeps the same fault (R2-1-M1). |
| A-M3 (heresy charge empty) | RESOLVED | "Epistola ad Plegwinum apologetica de Sex Aetatibus Saeculi", to "Plegwin, a monk of Hexham" (l.10480-10484). The six ages doctrine is at l.2856-2858. Declining the optional Easter beat is right at the cap. |
| A-M4 (Nothelm's purpose; Jane sentence) | RESOLVED | "searched into the archives … found there some epistles of the blessed Pope Gregory" (GILES l.166-168). Jane edited the 1903 edition (l.15581-15586), and "practically the only authority … to the year 732" is at l.15634-15637. The sentence is 24 words. |
| A-M5 (mixed person) | RESOLVED | "the words of thy wisdom" and "come to thee, the fountain of all wisdom" are verbatim (GILES l.15563-15566). |
| A-M6 (two books joined) | RESOLVED | "Bede himself calls the longer work De Temporibus Liber Maior" (PLUMMER l.2736-2738). The card now leaves III.17's reference open. |
| A-M7 (birth years; Mayor and Lumby) | RESOLVED | Lindisfarne annals and Simeon of Durham for 677, Stevenson's 674 "on very precarious grounds" in "Church Historians", and Florence of Worcester for 678 (l.540-561). "as given by M. & L." is at l.5555-5556. |
| A-M8 (beat line) | RESOLVED | "Rome honors him." is gone. "Homily by the Venerable Bede" (BREVIARY l.30252, 40578, 44848) and "From the Venerable Bede's History" (l.61583, 77302) back the new sentence. No count is given, which is right. |
| A-M9 (two withdrawn census differences) | RESOLVED | The Alcuin heading reads "AD CAROLUM MAGNUM. (Anno 800.) Commendat … libros [vii] adversus Felicem" (ALCUIN l.9436-9442). Both differences are withdrawn in the notes, and the year is back in `legacy.traces` 2. |

**Census-difference list (live entry `movements` id `bede-of-jarrow`, against `notes/bede-of-jarrow.md`).** I read the live entry in full and checked each item against its line.

1. "Bede had just finished translating the Gospel of John." **Right.** The words are Jane's (GILES l.15616-15617). The St. Gallen text stops at John 6:9 (PLUMMER l.11307-11312), and Plummer doubts even that (l.5806-5811). The census puts the claim after "His pupil Cuthbert described the scene", so it reads as Cuthbert's.
2. "He died on Ascension Day in 735, aged sixty-two." **Right as the notes word it.** The day can stand, because Plummer makes the death ecclesiastically Ascension Day (l.5664-5672). The year is contested (735 Plummer; 734 the Saxon Chronicle; 742 Mayor and Lumby), and the age is Jane's alone.
3. "unsigned editor", with `date: null` and `author: null` keys. **Right.** Jane "supplied the Biographical Notice" (GILES l.15583-15588).
4. "Sell Christ." **Right as now worded.** The line stands. The one difference is that the live `sources.about` lists only the Lollard Apology, while the line is in Arnold's volume 3.
5. Two withdrawals (the Theodore lesson; "About the year 800"). **Right to withdraw** (BREVIARY l.71002-71005; ALCUIN l.9436-9442).
6. The "agrees" list holds where I checked it. "Ceolwulph" is Giles's spelling (GILES l.115). "Spending all the remaining time of my life in that monastery" backs the census's rest-of-his-life line (l.15424-15425). The census `uncertain` 1 wording about Aidan's Easter matches GILES l.7024-7029.

The list is complete for facts. Two census-side points are not on it (R2-1-M2).

**Changed sentences checked and found faithful.** Brief P1 (A-M1), P2 (A-M2), P5 (A-M3), P6 (A-M4), P7 (A-M5). Card `keyWorks` 3, `legacy.traces` 2 and 6, `legacy.remembered` 1, `uncertain` 1 and 3. The common names keep their identifiers in both texts: "Cuthbert, Bede's pupil" at its first card mention, "Aidan of Lindisfarne", and "Theodore of Tarsus". No new contrast, tail or colon-reveal.

#### New findings

- **R2-1-M1 MINOR (card `dates`; item 4; the A-M2 fault left on the card).** "Plummer holds that he died on the eve of Ascension Day in 735; other chronicles give 734." As in the brief before A-M2, "other chronicles" counts Plummer as a chronicle. Plummer names the witnesses: "734 is the date of all MSS. of the Sax. Chron., of the Ann. Ult. …" (PLUMMER l.5479-5481). Fix: "Plummer holds that he died on the eve of Ascension Day in 735; the Saxon Chronicle and several other chronicles give 734" (the card's `uncertain` 1 already says "of several other chronicles").

- **R2-1-M2 MINOR (notes, census differences; for the coordinator).** Two points are not on the list.
  - (a) The census card's `keyWorks` 3 says On the Times is the book "where, he says, he proved Aidan's way of keeping Easter wrong". That joins the 703 book to the "De Temporibus" of III.17 as settled. Plummer notes that Bede also calls the longer work De Temporibus (PLUMMER l.2736-2738), and A-M6 qualified the profile for this reason.
  - (b) The census card still opens `remembered` with "Rome honors him.", the beat line A-M8 removed from the profile. This is a writing point and not a fact.
  - Fix: add both to the census-difference list, so the census card can be brought into line with the profile.

---

### Hild of Whitby

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B2 (chapter count) | RESOLVED | Plummer's own index has Hild at "iii. 24 … iii. 25 … iv. 23 … iv. 24 … v. 24" (PLUMMER l.36311-36316). That is her life, three more chapters and the annal (GILES l.15362-15363), as the card now says. IV.26 mentions her monastery but not her (GILES l.11517-11519), so the count holds. |
| A-M10 (comparison widened) | RESOLVED | "Others after him attempted, in the English nation … but none could ever compare with him" (GILES l.11147-11150). "No later English poet of religious song matched him" keeps "after him". |
| A-M11 ("the Scots") | RESOLVED | "the Scots, who, migrating from Ireland" (GILES l.381-382). |
| A-M12 (Colman; Pope John) | RESOLVED | Colman of "the church of Lindisfarne" (GILES l.8239-8269). The letter looks back to "sub … praedecessore nostro Agathone pontifice" and to "Hylde religiose memorie abbatisse" (RAINE l.9416-9425). "Had come to Rome under Pope Agatho" fits "huc prius advenerant" in that clause. |
| A-M13 (tail misframes Bede) | RESOLVED | "it pleased Almighty God, by a manifest vision, to make known her death" (GILES l.11064-11066). "It is also reported" (l.11111). |
| A-M14 (Plummer gloss; assent) | RESOLVED | "all present, both great and small, gave their assent" (GILES l.8215-8217). Plummer's "the Irish monks of Iona, by whom Northumbria was reconverted" (PLUMMER l.988-990) is told as his. |
| A-M15 (Tatfrid "before him") | RESOLVED | "Before the aforesaid man of God, Bosel, Tatfrid … had been chosen bishop there" (GILES l.11008-11011). |
| A-M16 (translation fault; "Hild" repeated) | RESOLVED | (a) and (b) both done. One further fault in `otherNames` remains (R2-1-M4). |

**Changed sentences checked and found faithful.** Brief P1 last sentence, P3 opening, P5 (A-M11, A-M12). Card `legacy.traces` 2, `legacy.remembered` 2, `uncertain` 1, 3 and 5. The Thomas of Ely split in `uncertain` 3 reads cleanly.

#### New findings

- **R2-1-M3 MINOR (brief P2 and audio; items 1 and 4; "later" has no anchor).** "Most of what is known of her comes from Bede, writing about fifty years later." R1 changed "some fifty years after her death" to "about fifty years later" to save words. Now the time is counted from nothing. The sentence before it names Hild and her place, and the scene before that, Caedmon's call, has no year (records, absent detail "Caedmon's date"). Bede finished in 731 (GILES l.15408), and she died in 680 (l.15362-15363). Fix: "Most of what is known of her comes from Bede, writing about fifty years after her death." That makes 406 words, which sits inside "about 405", as R1's own 407-word scratch copy did.

- **R2-1-M4 MINOR (card `otherNames`; items 1 and 12; inflected Latin forms given as names).** "Hilde" and "Hylde" are not forms of her name. They are case endings in Stephen's Latin: "presente … matre piissima Hilde" (RAINE l.5067-5081) and "et Hylde religiose memorie abbatisse" (l.9424), and the rubric "uita Sce. Hilde" (PLUMMER l.33990) is the same. This is the fault B-M14 corrected for Adomnán. The nominatives held are "Hild" (PLUMMER l.24823) and "Hilda" (GILES l.10891; AASS June 5 l.95275, "S. Hilda, Abbatissa"). Fix: `otherNames` becomes `["Hilda"]`, and the records' otherNames claim drops the two oblique forms or marks them as cases.

---

### Aidan of Lindisfarne

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B1 (Plummer's "sad" on the wrong sentence) | RESOLVED | "It is sad that he should think it necessary to pause in the middle of his beautiful sketch … to say that he 'much detests' his mode of keeping Easter" (PLUM l.2806-2809). "Very much detesting the same" (GILES l.6987-6988) now comes first, and "breaks off his praise of Aidan to say so" points to it. Plummer is placed as Bede's 1896 editor (PLUM l.60, MDCCCXCVI). The patient tolerance is now a separate grant. |
| B-B2 (Cuthbert's timing one-sided) | RESOLVED | "post paucas dies" (AASS Mar. 3 l.38829-38832) and "mane facto" (l.34343-34347) are both told in place, each with its Life named. P7's "his love of peace … his tenderness in comforting the afflicted, and relieving or defending the poor" holds (GILES l.6995-7002). |
| B-M1 (no identifier) | RESOLVED | "Aidan, a monk of Iona" (GILES l.5914-5915, 5989-5990). |
| B-M2 (stiff opening) | RESOLVED | "It is reported" (GILES l.5965). |
| B-M3 ("free people"; "wrongly") | RESOLVED | "ransoming such as had been wrongfully sold for slaves" (GILES l.5960-5961), in both brief and card. |
| B-M4 ("see" undefined) | DECLINED-WRONG (minor) | The decline rests on the cap. But a fix with the same number of words exists, and read aloud "a see on Lindisfarne, an island at high tide" is heard as "a sea". See R2-1-M6. |
| B-M5 (card sources) | RESOLVED | "Books III and IV.23"; I.34 for King Aedan (GILES l.3189-3190); Huyshe, Rees and the Annales Cambriae are listed. "Vetus Menevia" and "the Monastery he had founded in Menevia" (REES l.17998-18003) back "David of Menevia". The Annales Cambriae name only Aidan son of Gabran and Aidan son of Blegywryd (AC l.2572, 4241; index l.12204-12209), so "do not name him" holds. |
| B-M6 (records tag) | RESOLVED | The c.700 claim is now Dominant Modern Reconstruction and quotes "Videtur" (AASS Mar. 3 l.32846-32854). The 630s claim names the 635 as the Bollandists'. |

**Changed sentences checked and found faithful.** Brief P1, P2 opening, P3 ransom sentence, P5, P6, P7 opening. Card `knownFor`, `uncertain` 5 and 7, `sources`. P1's third sentence is 25 words, at the limit and not over it.

#### New findings

- **R2-1-M6 MINOR (brief P2 and audio; item 4; an undefined term heard as another word).** "Oswald gave him a see on Lindisfarne, an island at high tide." A listener does not know "see", and in audio it sounds like "sea", which the island clause seems to confirm. Bede has "appointed him his episcopal see in the isle of Lindisfarne" (GILES l.5763-5764). Fix, at the same word count: "Oswald made Lindisfarne, an island at high tide, the seat of his bishopric." That is 13 words against 12, and R2-1-M7 frees the word. The card may keep "see", since a reader sees the spelling.

- **R2-1-M7 MINOR (brief P2 and audio; items 1 and 4; "later" counts from the wrong event, and "writing … from those" is awkward).** "Nearly all we know of Aidan comes from Bede, writing some eighty years later, from those who had known him." The sentence before it is about his coming in the 630s. A listener counts eighty years from there and lands in the 710s, but Bede wrote in 731 (GILES l.15189-15191), eighty years after the death in 651 (l.15317-15318). The card's `uncertain` 1 rightly says "some eighty years after Aidan's death". "Writing … from those who had known him" also reads as if Bede wrote from among them. Bede's words are "as near as I could be informed by those that knew him" (l.7003-7004). Fix: "Nearly all we know of Aidan comes from Bede, who wrote some eighty years after his death and learned from those who had known him." That is 23 words, three more than now. With R2-1-M6 the brief reaches 409. To hold the cap, P2's opening can drop ", which Bede calls Hii,": "He came to the English from Iona in the 630s." The card's `place` keeps "Iona, which Bede calls Hii". That saves four words and brings the brief to 405.

---

### Adomnán of Iona

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-M7 (Lebar Brecc and White without context) | RESOLVED in the brief, PARTLY in the card | White's title page reads "St. Patrick: His Writings and Life", with "NEWPORT J D WHITE" (OCR, WHITE l.112-119), so "who translated Patrick's writings" holds. The held witnesses differ on the Lebar Brecc's date: Huyshe has "the fifteenth-century manuscript, the Leabhar Breac" (HUY l.1684-1685), and the Antiphonary of Bangor has "compiled from ancient sources about the end of the fourteenth century" (antiphonary-of-bangor-pt2 l.17717-17719). The brief's "a late medieval Irish manuscript" covers both. The card gives only Huyshe's date, and its first mention of the Lebar Brecc (`legacy.traces` 5) has no context. See R2-1-M5 and R2-1-M8. |
| B-M8 (seems to die in Ireland) | RESOLVED | "Returning to his island, after having celebrated the canonical Easter in Ireland … he departed this life before the next year came round" (GILES l.13582-13587). Huyshe: "returned to his monastery in Iona, and there, soon after, he died" (HUY l.2001-2003). |
| B-M9 (Arculf "from Jerusalem") | RESOLVED | "returning home by sea" (GILES l.13598-13602). |
| B-M10 (Ceolfrid unmarked; "tonsure") | RESOLVED | Naitan asked for arguments "concerning the form and manner of tonsure" (GILES l.14338-14342). Ceolfrid's question is at l.14889-14893. "Why his head was shaved like that of the man Saint Peter had cursed" explains the tonsure before the quoted answer names Simon. |
| B-M11 (four names for one Easter) | RESOLVED | "The Roman Easter" in brief P5, `knownFor`, `dates` and `legacy.traces` 1-2. "Roman reckoning" stays only in `uncertain` 5, where it means the reckoning. |
| B-M12 (second tradition; census year) | DECLINED-OK | This is for the coordinator, and the census Insular row's 679 is logged in the notes. |
| B-M13 (Bede title) | RESOLVED | III.4 (GILES l.5877-5878) and IV.25 (l.11316-11317) are in the title. |
| B-M14 (namesake's nominative) | RESOLVED | "Adamnanus pre[s]byter et abbas monachorum qui erant in insula Hii" (PL88 l.66004-66005). "Adomnanus captiuos duxit ad Hiberniam" (STOKES-TRIP l.14840) and Alcuin's "Adomnanus" are nominatives too. |

**Changed sentences checked and found faithful.** Brief P1, P2 last sentence, P4, P5, P6. Card `dates`, `knownFor`, `keyWorks` 2, `legacy.traces` 1-2, `uncertain` 3. No new contrast or tail.

#### New findings

- **R2-1-M5 MINOR (card `legacy.traces` 4; item 4; a sentence past 25 words, and a name with no context).** The B-M7 addition made it 28 words: "Newport White says Muirchu, who wrote a Life of Patrick, and Aedh of Sletty signed the acts of the synod Adomnán held at Birr, between 695 and 697." This is also the card's first mention of Newport White, and the card gives him no context. White: "Both Aedh and Muirchu subscribed the Acts of the Synod held at Birr, by Adamnan, a.d. 695-697", with Aedh "bishop of Sleibte (Sletty)" (WHITE l.3764-3770). Fix: "Newport White, who translated Patrick's writings, says Muirchu and Aedh of Sletty signed the acts of Adomnán's synod at Birr. Muirchu wrote a Life of Patrick, and White dates the synod 695 to 697." (21 and 16 words.)

- **R2-1-M8 MINOR (card `legacy.traces` 5 and `uncertain` 3; items 1 and 7; one of two held dates given, and the first mention without context).** `uncertain` 3 says "Wentworth Huyshe calls the Lebar Brecc a fifteenth-century manuscript". It leaves out the other held date, which the records carry ("about the end of the fourteenth century", antiphonary-of-bangor-pt2 l.17717-17719). `legacy.traces` 5 comes first on the card and gives the manuscript no context. The drafter's reason for not naming Warren holds: his name is not readable on the held title page. So name the book, which is the witness. Fixes:
  - `legacy.traces` 5: "A note in the Lebar Brecc, a late medieval Irish manuscript printed by Whitley Stokes, counts Adomnán's rule, not to slay women, among four rules of Ireland."
  - `uncertain` 3, in place of the Huyshe sentence: "Wentworth Huyshe calls the Lebar Brecc a fifteenth-century manuscript. The held edition of the Antiphonary of Bangor says it was compiled about the end of the fourteenth century."

---

### Counts

| Profile | R1 findings | Resolved | Partly | Declined | New blocking | New minor |
|---|---|---|---|---|---|---|
| Bede | 10 (A-B1, A-M1 to A-M9) | 10 | 0 | 0 | 0 | 2 (R2-1-M1, R2-1-M2) |
| Hild of Whitby | 8 (A-B2, A-M10 to A-M16) | 8 | 0 | 0 | 0 | 2 (R2-1-M3, R2-1-M4) |
| Aidan of Lindisfarne | 8 (B-B1, B-B2, B-M1 to B-M6) | 7 | 0 | 1 wrong (B-M4) | 0 | 2 (R2-1-M6, R2-1-M7) |
| Adomnán of Iona | 8 (B-M7 to B-M14) | 6 | 1 (B-M7, card) | 1 OK (B-M12) | 0 | 2 (R2-1-M5, R2-1-M8) |

Every R1 blocking finding (A-B1, A-B2, B-B1, B-B2) is resolved. None of the four profiles has a new blocking finding. The census-difference list for Bede is right, with two census-side additions (R2-1-M2).

## R2 recheck, part 2: Boniface of Mainz, Alcuin of York, Dhuoda, Nennius

Reviewer: independent Opus, first sight of these files. I edited no profile file and made no git writes, web, paid or model calls. I used local scripts only. Inputs: R1_review.md parts C and D, R1_changes.md parts C and D, the current batch 1 files, `records.json`, and the drafter's notes in the scratchpad. Changed text was found with `git diff --word-diff` against the first-draft commit 09ff83c9 (the version R1 quotes) for the briefs, and field by field for the cards. I opened every cited line again in its vendored file in `cic/texts/` and read it in context. A scored copy of the one brief fix below is in `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/r2part2/`.

**Mechanical checks (all four).** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are removed. All four match, with one tag of each kind, and no tag in any brief or card. Each card is in Mark's order (name, otherNames where held, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources). None has a null or empty field. Nennius now has no `otherNames`, which is right after N-B3. Each card has at most three keyWorks, and every `sources` file exists. Each `records.json` entry is identical to its scratchpad record. Every quotation in the Boniface and Nennius briefs matches its file by script, with OCR noise folded. Dhuoda and Alcuin use no quotation marks. No narrator sentence in any brief passes 24 words. The one 27-word sentence, in Boniface's last paragraph, is Kylie's verbatim quotation of the Stephen letter (Kylie l.1550-1553). No changed card sentence passes 25 words.

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| boniface-of-mainz (major, cap about 405) | 403 | 2:29 | 7.5 | 69.8 |
| alcuin-of-york (major, cap about 405) | 404 | 2:30 | 7.7 | 66.3 |
| dhuoda (major, cap about 405) | 402 | 2:29 | 6.8 | 76.0 |
| nennius (recorder, about 2:00) | 340 | 2:06 | 6.6 | 70.0 |

---

### Boniface of Mainz

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B1 ("aliquid" dropped) | RESOLVED | "had promised to put right something of the church's order" keeps "aliquid corrigere et emendare" (capitulatio l.2204-2205, OCR "conngerc ct"). The reworded form is plainer than the review's and loses nothing. |
| C-M1 (754 on the departure) | RESOLVED | The year now sits on the death: "on June 5, 754" (Kylie l.1815). The departure, "for the last time took boat on the Rhine" (l.1750-1751), carries no year. |
| C-M2 (Cynehild; tense) | RESOLVED | "Cynehilda" (l.5871, 5875) in the brief and in `keyWorks` 1. "I beseech, nay all but command you" is verbatim (l.5878). |
| C-M3 ("reminded"; "wont") | RESOLVED | "Have pity on them because even they themselves are wont to say" (l.7521-7522). The brief tells the plea in modern words and quotes only the Saxons' saying. |
| C-M4 (Boretius unplaced) | RESOLVED | "In a letter printed with the decree". Boretius stays in the card's sources. |
| C-M5 (747 as Boretius's conjecture) | RESOLVED | "After a synod Kylie dates to 747" (Kylie l.1637-1638, heading "747+" at l.6872). Boretius's "ut coniicere licet" (l.2209) is in the records. |
| C-M6 (role) | RESOLVED | "legate in Germany of the universal Church" (l.7499), "as he called himself". |
| C-M7 (second Gregory) | RESOLVED | "Gregory of Utrecht": Altfrid has him teaching Liudger "in Trajecto monasterio" (AS l.164260-164265). |
| C-M8 (Bollandists' day) | RESOLVED | "Contigit illud Nonis Junii in loco Dockinge dicto, sive ut habet MS. Vita S. Willehadi …" (AS l.161072-161073). The sentence follows the end of the Einhard quotation and goes on with the Bollandists' own variant from the Life of Willehad, so it is theirs. Giving it to the Bollandists is right. |
| C-M9 (census "robbers") | DECLINED-OK | Census-side. Logged in the Boniface notes for Open-Gaps against "The Oak at Geismar". No Open-Gaps entry exists yet, so the coordinator must still write it. |
| Lioba / Leoba (coordinator's call) | DECLINED-OK | Kept as Kylie's "Lioba". Logged in the notes as the coordinator's call. |

**Changed sentences checked and found faithful.** These are the opening sentence and the death sentence, the Lioba sentence, the Saxon plea, the Carloman sentence and the 747 sentence. In the card they are `dates`, `role`, `keyWorks` 1 and `legacy.traces` 3. Each matches its line. No new contrast, tail or AI tell.

**New findings.** None.

---

### Alcuin of York

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B2 ("his master" heard as Charlemagne) | RESOLVED | "Alcuin wrote that he came at Charlemagne's call. His teacher, he says, had charged him …". The two claims are now split. "Meus mihi mandatum dederat magister" (PL101 l.17306-17307) is his teacher, whom Mabillon identifies: "Magister iste Alcuini est Albertus" (l.113553). The brief drops "et apostolicis contrariis doctrinis". That is a description of the sects and not a condition, so the rendering holds. |
| C-M10 ("young") | RESOLVED | "a Frisian deacon": "Liudgerum Diaconem" (AS l.164336) and "studiosus Levita" (l.164412). |
| C-M11 ("saint's Life") | DECLINED-OK | Reworded to "his Life of Saint Liudger". The slip is gone, and the hagiography stays marked. |
| C-M12 ("harmed") | RESOLVED | "suffer deadly harm" for "quicquam pateretur lethalis mali" (AS l.164435-164436). |
| C-M13 (card: "most learned man anywhere") | RESOLVED | "a man most learned in every field" for "virum undecunque doctissimum" (l.113572-113573). Card and brief now agree. |
| C-M14 ("in this scan") | RESOLVED | "Mabillon gives the day as 19 May, from the older Life, from Rabanus, and from Hariulf, a monk of Centula" ("xiv Kal. Junii, ut constat ex Vita, Rabano, et Hariulfo monacho Centulensi", l.115022-115025). |
| C-M15 (two stays) | RESOLVED | "for a year, and later went back for three years and six months". The first stay is "anno uno" (AS l.164393). The second is "annis tribus et mensibus sex" (l.164420), with the master "Eboraicae civitatis" (l.164415). |
| C-M16 (York poem ascription) | RESOLVED | "ascribed to him, though not by all". The dispute stays in `uncertain` 5. |
| C-M17 (census) | DECLINED-OK | Census-side, and logged in the Alcuin notes with PL 100 or Dümmler as wanted. |

**Changed sentences checked and found faithful.** These are the opening three sentences, Mabillon's "essay" sentence and the C-B2 pair. In the card they are `keyWorks` 3, `legacy.traces` 1, `legacy.remembered` 1 and `uncertain` 2. Each matches its line.

**New findings.** None.

---

### Dhuoda

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B1 (thesis label) | RESOLVED | The sentence is deleted, and P4 opens on what the book teaches. |
| D-B2 ("si jubet" dropped) | PARTLY | Both conditions are back, but the split detaches the second from the prayer. See R2-D-B1. |
| D-M1 (vague "it"; three names for one passage) | RESOLVED in the brief | "reckons the year from its closing note": "its" follows "a book in her name", and Bondurand reckons the year from the subscription (l.13224-13229). The card's matching edit leaves "its" with no antecedent. See R2-D-M1. |
| D-M2 (Delisle unplaced) | RESOLVED | "head of France's national library" for "Administrateur général de la Bibliothèque Nationale" (l.247-248). |
| D-M3 ("by Elefant"; "her lord's orders") | RESOLVED | "una cum Elefanto, praedictae civitatis episcopo, et cum caeteris fidelibus suis" (l.2256-2257); "sub jussione senioris mei" (l.2259-2260). |
| D-M4 (850 with no place) | RESOLVED | "in marca Hispanica" (BERT l.2515-2516). The sentence is 24 words, and the brief holds 402 words. |
| D-M5 (two Prudentiuses) | RESOLVED | "the poet Prudentius" (l.1168-1171). |
| D-M6 (`uncertain` 5) | RESOLVED | It now opens on a plain label. Louis is "Charlemagne's son" (Bondurand's note, l.2236-2237). Mabille is named: "elle n'a pas été absolument abandonnée par M. Mabille" (l.13198-13199). His first name, Émile, is in the same file (l.2346, 11787). The Nîmes reading "Ludovici condam imperatori" (l.13207-13208) and "Il faut donc renoncer" (l.13219) check. |
| D-M7 (traces 1: fragments) | RESOLVED | 32 leaves, "une faible partie du texte total" (l.228-237). |
| D-M8 (chapter 69 acrostic) | RESOLVED | Bondurand: "Les autres pièces de poésie, révélées par le ms. de Nimes … Le chap. lxix … VERSI AD VVILLELMVM F(ilium)" (l.440-462). |
| D-M9 (unnamed chronicle) | RESOLVED | "La vieille chronique d'Odon Héribert" (l.1804); "L'imagination populaire entoura cette vengeance … de circonstances romanesques" (l.1802-1803). |
| D-M10 ("died before 813") | RESOLVED in the card | "a Dodana dead by 813" (l.620-627). The notes still carry the old wording. See R2-D-M2. |
| D-M11 (Catechism) | RESOLVED | "their 1923 English translation of the Roman Catechism". |
| D-M12 (full stop) | RESOLVED | Present. |
| D-M13 (census vengeance) | RESOLVED | The notes now say the held texts differ, and that neither is a source of her time. |

**Changed sentences checked.** P1's last sentence, P2's Delisle and Elefant sentences, P3's "granted" and P6's 850 sentence are faithful. In the card, `keyWorks` 1 and 2, `legacy.traces` 1, `legacy.remembered` 3 and `uncertain` 2, 5 and 7 are faithful. There are two faults, below.

#### New findings

- **R2-D-B1 BLOCKING (brief P5 and audio; items 1 and 4; a rendered Latin passage split away from its frame).** The R1 fix now reads: "She told William to pray often for his father's peace with all, if it could be. If God willed, Bernard would come to heaven." In ch. LVII both clauses are what William is to pray for. The text runs "ut det illi Deus … pacem et concordiam, si fieri potest, cum omnibus … ad regnum, si jubet, faciat pervenire supernum" (DHU l.10106-10112). The second sentence stands alone in the narrator's voice. It reads as a statement about Bernard's fate, and it no longer says this is part of the prayer Dhuoda asks for. The R1 fault was a dropped condition. The repair moved the condition back in but cut it off from its witness and its frame. Fix (24 words, the same count as now, so the brief stays at 402): "She told William to pray often that God would give his father peace with all, if it could be, and heaven, if God willed." Scored on the scratch copy: FK 7.1, Flesch 75.5. Rebuild the audio and the records claim to match.

- **R2-D-M1 MINOR (card `dates`; items 4 and 9; "its" with no antecedent).** "Édouard Bondurand reckons from its closing note that she began the book on 30 November 841." In the card field the only earlier sentence is "Married in 824, in Léopold Delisle's date", so "its" points forward to "the book". Fix: "Édouard Bondurand reckons from the book's closing note that she began it on 30 November 841." (l.13224-13229.)

- **R2-D-M2 MINOR (process; drafter's notes, `notes/dhuoda.md` l.15).** The notes still say "a Dodana dead before 813", the wording D-M10 corrected. The notes feed Open-Gaps. Fix: "a Dodana dead by 813" (l.620-627).

---

### Nennius

| R1 finding | Verdict | Evidence |
|---|---|---|
| N-B1 ("The brief tells …") | RESOLVED | Deleted. `uncertain` 4 opens "Arthur. Giles's text gives …". |
| N-B2 (Joseph Stevenson item) | RESOLVED | `uncertain` 6 is deleted. The records claim no longer has the namesake half, and the notes withdraw it. |
| N-B3 ("pseudo-Nennius" as another name) | RESOLVED | `otherNames` is removed, and the field is absent. |
| N-M1 (card name) | RESOLVED | "Nennius", on the coordinator's ruling. `sources.ownWords[0].author` stays "Nennius (attributed)", and the id is `nennius`. |
| N-M2 (scholars unplaced; pseudo-Nennius undefined) | RESOLVED (wording DECLINED-OK) | Duchesne edited the lives of the popes (LP1 header). Hugh Williams edited Gildas (GILDAS l.70-79). Stevenson edited Asser (ASSER l.75-81). "That older British writer" holds: Williams ab Ithel calls Gildas and Taliesin "two contemporaries" of Badon, and the author of Nennius "lived at a later period" (ANN l.1084-1101). "A false Nennius" is a plain gloss of Duchesne's "Pseudo-Nennius" (LP1 l.52070-52071). Both sides of the authorship dispute stay named in the brief: the prologue and Stevenson for Nennius, Mark's heading, Duchesne and Williams's copies against. |
| N-M3 (Elvod and Elbodug; editor's year) | RESOLVED in the brief, PARTLY in the card | The brief keeps only Giles's note: "Or Elvod, bishop of Bangor, A.D. 755, who first adopted in the Cambrian church the new cycle for regulating Easter" (NEN l.46-47). In `uncertain` 3, 768 is now "the year their editor reckons as 768". The next sentence's 809 has the same fault. See R2-N-M1. |
| N-M4 (Germanus of Auxerre) | RESOLVED | In the brief and in `knownFor`. "Germanus (Garmon) of Auxerre" (GILDAS l.19277). |
| N-M5 (Vortigern) | RESOLVED | "Vortigern then reigned in Britain" (NEN l.629). |
| N-M6 (674 tag) | RESOLVED | The records tag is now Contested. |
| N-M7 (source language) | RESOLVED | "Latin, with an English preface". |
| N-M8 (no census list line) | DECLINED-OK | Census-side, and logged in the Nennius notes. No Open-Gaps entry exists yet. |

**Changed sentences checked and found faithful.** These are P1's split apology sentences (NEN l.112-117), P2's placements, P4's Giles sentence and P5's Vortigern and Germanus sentence. In the card they are `knownFor`, `dates`, `sources.about[1].language` and `uncertain` 3 and 4. In P4, "first brought a new way of fixing Easter into the Welsh church" is a fair modern telling of "first adopted in the Cambrian church the new cycle for regulating Easter".

#### New findings

- **R2-N-M1 MINOR (card `uncertain` 3; records contested claim "Elbotus's see and dates"; item 1; the same fault as N-M3, left in the next sentence).** "They put the death of Elbodg, archbishop of Gwynedd, in 809." The annal gives only "CCCLXV. Annus. Elbodg archiepiscopus Guenedote regione migravit ad Dominum" (ANN l.3102-3103). The 809 is the editor's margin (l.3114), as 768 is (l.2962). Fix: "Under the year their editor reckons as 809, they put the death of Elbodg, archbishop of Gwynedd." In the records' contested claim, change "Easter changed under Elbodug in 768; Elbodg … died 809" to "in the editor's 768 … in the editor's 809".

- **R2-N-M2 MINOR (card `legacy.remembered` 2; item 4; a statement with no context, in text changed after R1).** "John Williams ab Ithel writes of the author of the book of Nennius as living at a later period." The listener is not told later than what. Williams ab Ithel means later than Gildas and Taliesin, whom he has just called "two contemporaries" of Badon (ANN l.1084-1086, 1100-1101). The new phrasing "writes of … as living" is also stiff. Fix: "John Williams ab Ithel says the author of the book of Nennius lived later than Gildas and Taliesin. He notes that this author made Badon the twelfth of Arthur's battles."

- **R2-N-M3 MINOR (process; drafter's notes, `notes/nennius.md` l.5).** The notes still call Elbodug "the man Giles takes for Nennius's teacher". N-M3 found that no held line makes Giles's Elvod the annals' Elbodug, and the brief no longer says so. The notes feed Open-Gaps. Fix: "the 768 Easter change (the editor's year) that the Annales Cambriae credit to Elbodug". Drop the link to Giles.

---

### Counts

| Profile | R1 findings resolved | New blocking | New minor |
|---|---|---|---|
| Boniface of Mainz | 10 of 10 resolved or declined-OK (C-B1, C-M1 to C-M9) | 0 | 0 |
| Alcuin of York | 9 of 9 resolved or declined-OK (C-B2, C-M10 to C-M17) | 0 | 0 |
| Dhuoda | 14 of 15 resolved; D-B2 partly | 1 (R2-D-B1) | 2 (R2-D-M1, R2-D-M2, process) |
| Nennius | 10 of 11 resolved or declined-OK; N-M3 partly | 0 | 3 (R2-N-M1, R2-N-M2, R2-N-M3, process) |

For the coordinator: the census-side items C-M9 (Geismar "robbers"), C-M17 (PL 100 wanted), D-M13 (whose vengeance) and N-M8 (no Nennius list line), and the Lioba/Leoba call, are in the drafter's notes only. None has an Open-Gaps entry yet.
