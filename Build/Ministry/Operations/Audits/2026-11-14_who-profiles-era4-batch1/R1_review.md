# R1 review: era 4 batch 1

Round 1 ran in four parts, each by a fresh Opus agent that had not seen the drafting. The parts follow, unchanged.

## R1 review, part A: Bede, Hild of Whitby (era 4 Who batch 1)

Reviewer: independent Opus, first sight of these drafts. I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the era 3 batch 8 R1 review for format; the Decision-Log entries for era 3 batches 6 to 8 and their cap rulings. Following those rulings, missing common-name identifiers are minor and false absences are blocking, wherever they sit. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, the scratch records and the drafter's notes. I opened every cited line in its vendored file and read it in context, folding OCR noise, double spaces and hyphen breaks.

Files: Giles/Jane 1903 (`bede_ecclesiastical-history-english-people_giles1903.txt`, "GILES"), Plummer 1896 (`bede_opera-historica-v1-historia-abbatum-lat_plummer1896.txt`, "PLUMMER"), Raine 1879 (`byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt`, "RAINE"), Alcuin PL 100-101, Annales Cambriae, the Bute Breviary, the England Missal, the Lollard Apology, AASS June 5 and March 3, the York Prymer, and Arnold's Wyclif Select English Works v3 (`wyclif_select-english-works-v3_arnold1871.txt`, "ARNOLD3").

Absence searches across all of `cic/texts/`: Plegwin/Pleguin/Pleguuin; "sell(en) Crist/Christ"; Bede in every Wyclif and Lollard file; Bede in the Breviary; years for Alcuin's books against Felix; Hild/Hilda/Hilde/Hylde; Bede's chapters naming Hild; "accus-" in Bede's life of Wilfrid (V.19); a source that glosses Bede's "Scots".

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied all the suggested brief fixes to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/fixA/bede-of-jarrow.brief.txt` and `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/fixA/hild-of-whitby.brief.txt`.

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. Both cards follow Mark's order, have no null or empty fields, and every `sources` file exists and holds the named work. Bede has three `keyWorks`; Hild has none, rightly. The tradition on both cards, Anglo-Saxon Christianity (597 to 793), is a census tradition and fits the dates. The drafts carry no list lines, so the list-line half of item 14 was not checked.

---

### Bede (major; 404 words, about 2:30; FK 6.3, Flesch 71.7)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M1, A-M3, A-M4, A-M6, A-M7) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M2, A-M4, A-M5, A-M8) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Bede's own side on the Britons and Aidan is on the card) |
| 7 | Contested claims both sides | PASS (death year, the plague boy and the translation are each told as their witness's) |
| 8 | Common names | PASS (two Cuthberts kept apart on the card) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the brief's death-year caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-B1) |

**Sentences checked and found faithful.**
- P1: the deathbed is in Plummer's English of Cuthbert's letter: "Then the same boy, named Wilbert, said once more: 'There is still one sentence, dear master, which is not written down.' And he said, 'Well, then, write it.'" … "Take my head in thy hands, for it much delights me to sit opposite my holy place where I used to pray" … "upon the floor of his cell singing 'Glory be to the Father …'" (PLUMMER l.5884-5895). The evening is at l.5882-5883.
- P2: Cuthwin and Cuthbert are at l.5511-5512. "Fellow pupil" stands on "co-disciple" and "our master Bede" (l.5512, 5517), though Plummer reads "collector" as fellow-lector (l.5569-5580). Plummer's year is at l.5430-5432, and his Wednesday 25 May 735, "ecclesiastically … Ascension Day", is at l.5664-5672. The 734 witnesses are at l.5479-5483.
- P3: Bede's own account is at GILES l.15415-15437, quoted verbatim. Benedict Biscop is Jane's identification (l.15601-15604).
- P4: the anonymous History in Plummer's English is at l.610-628 (§14, l.646). Plague in 686 is at l.528-531. Plummer's "can hardly be any other than Bede himself" is at l.629-636.
- P5: the list of works is at GILES l.15434-15560. The heresy charge, "a lasciuientibus rusticis … per pocula", is at PLUMMER l.10483-10490, and 703 is at l.10505.
- P6: the preface is at GILES l.154-169 and l.225-230, quoted verbatim across the page break. Jane's "practically the only authority" is at l.15634-15637, and Jane as editor is at l.15581-15586. "J. A. Giles" is held as well as in the header (asser stevenson1904 l.1264; Wordsworth l.719).
- P7: the closing prayer is at GILES l.15562-15568.

**Card.** I checked these against their lines:
- `knownFor` and `keyWorks` 1 and 2 (GILES l.115, 15524-15531).
- `dates` (PLUMMER l.507-512; GILES l.15600).
- `place` (PLUMMER l.836-841; Plummer calls Wearmouth and Jarrow one monastery, l.517-523).
- Alcuin's York poem (PL100-101 l.67059-67087) and the two Felix citations (l.10320-10322, 13850-13852).
- Annales Cambriae l.2893 and l.1520-1539.
- Jane on Alfred and on 1643 (l.15644-15646).
- The Lollard miracles line (l.6031-6034).
- The Breviary (l.1935, 71002-71005) and the Missal (l.34692, 34723-34727).
- Plummer on "Venerable" (l.3466-3483, 3511-3537) and on Dante (l.2898-2908).
- `uncertain` 2, 4, 5, 6, 7 and 8. Plummer's St. Gallen text and his doubt are at l.5760-5766, 11307-11312, 11337 and 5806-5811. The Plummer-only claim for the heresy charge holds: Plegwin appears in no other file.

**Census entry (movements `bede-of-jarrow`): the drafter's six differences, checked.**
1. "Bede had just finished translating the Gospel of John." The difference is **confirmed**. Only Jane says "just completed" (GILES l.15616-15617). The St. Gallen text stops at John 6:9 (PLUMMER l.11307-11312). The ordinary text names the Gospel and does not say it was finished (l.11337). The census also puts Jane's claim next to "His pupil Cuthbert described the scene", which reads as Cuthbert's claim.
2. "He died on Ascension Day in 735, aged sixty-two." The difference is **confirmed in part**. The day is supported: Jane says Ascension Day, and Plummer says the death fell ecclesiastically on Ascension Day (l.5664-5672). What needs a witness is the year, which is contested (Plummer 735; the Saxon Chronicle 734; Mayor and Lumby 742), and the age, which is Jane's.
3. `sources.about` "unsigned editor", with null keys. The difference is **confirmed**. The editor is L. Cecil Jane (GILES l.15581-15586).
4. "Sell Christ." The difference is **wrong; withdraw it**. The line is held (A-B1).
5. The Breviary "lessons quote him". **No census error.** The quoted lessons are the Breviary's, for Theodore of Tarsus (l.70997-71005), and "Its lessons quote him" is true. A fuller census wording could name Theodore's office. The drafter's premise is false: the Breviary holds much more of Bede than a calendar line (A-M9).
6. "About the year 800" for the books against Felix. The difference is **wrong; withdraw it**. Migne heads Alcuin's letter to Charlemagne sending the books "(Anno 800.)" (PL100-101 l.9436-9442), and that letter is the census's own cited source (A-M9).

#### Findings

- **A-B1 BLOCKING (records `absent_details` 3; notes, "Differences" 4 and "Gaps"; a false absence that would drive a wrong census fix).** The records say the census's "sell Christ" line was not found "in the Apology and the vendored Wyclif English works". It is in Arnold's Select English Works vol. 3, in the tract "The Grete Sentence of Curs Expouned" (heading ARNOLD3 l.16381-16382). The line reads: "And Seynt Bede seiþ, We sellen Crist whanne we forsaken treuþe, and taken falsnesse and meyntene it" (l.17672-17674; OCR "seij?", "treufe"). Its context is priests who say Mass "in pride, coveitise" (l.17659-17668). This bears out the census `legacy` and `why` ("against clerical greed"). Fix: delete `absent_details` 3 and add a claim, Documented, with that quotation and witness. Strike difference 4 and the matching Gaps line from the notes. Tell the coordinator the census line stands. The census calls the text "A Wycliffite English tract", which is right.

- **A-M1 MINOR (brief P1; item 1; the speaker shifted).** "When it was written, Bede said it was finished." In the letter the boy says "Now it is finished", and Bede answers "Well, thou hast spoken truth; it is finished" (PLUMMER l.5888-5890). Fix: "When the boy said it was written, Bede agreed, "it is finished.""

- **A-M2 MINOR (brief P2; item 4; "other chronicles" makes Plummer a chronicle, and length).** "Plummer holds … 735, though other chronicles give 734." Plummer names the 734 witness first: "734 is the date of all MSS. of the Sax. Chron." (l.5479-5480). Fix: "Charles Plummer, who prints it, holds that Bede died on the eve of Ascension Day in 735, though the Saxon Chronicle gives 734." This merges the two sentences and drops "says Cuthbert later became abbot of Bede's monastery". The card keeps that point in `uncertain` 8, and dropping it frees the words that A-M3 needs.

- **A-M3 MINOR (brief P5; items 1 and 10; the charge has no content, and the position beat is thin).** The listener hears that Bede was charged with heresy but not what about. Plummer's held title for the reply is "Epistola ad Plegwinum apologetica de Sex Aetatibus Saeculi" (l.10480-10481). He says the two books on time are where Bede "lays down formally the doctrine … of the six ages of the world" (l.2856-2858). Fix: "He answered in a letter to Plegwin, a Hexham monk, on the six ages of the world." (Optional, for the drafter: the brief never tells Bede's Easter stance, which Plummer says filled his mind "out of all proportion" (l.2805-2806). The card's `uncertain` 7 carries it. There is no room for it at the cap.)

- **A-M4 MINOR (brief P6; items 1 and 4).**
  - (a) "searched the papal archives for letters of Gregory the Great" gives Nothelm a purpose the preface does not. The preface says he "searched into the archives … found there some epistles of the blessed Pope Gregory, and other popes" (GILES l.165-168). Fix: "searched the papal archives and found letters of Gregory the Great."
  - (b) The Jane sentence runs to 26 words, and "editor of J. A. Giles's translation in 1903" is hard to say aloud. Fix: "L. Cecil Jane, who edited the 1903 English edition, calls the History practically the only authority for England from the Saxon invasion to 732." This is 24 words; source l.15581-15586 and l.15634-15637.

- **A-M5 MINOR (brief P7; item 4; mixed person).** "who had been given the words of His wisdom" turns Bede's "thy" into a capitalized "His", next to a quoted "thee". Fix: "He asked that he, who had been given "the words of thy wisdom," might "come to thee, the fountain of all wisdom."" The words "the words of thy wisdom" are verbatim (l.15563-15564).

- **A-M6 MINOR (card `keyWorks` 3; item 1; two books joined without a source).** The card ties History III.17's "De Temporibus" (GILES l.6988-6990) to the 703 book Plummer dates. Plummer notes that "Bede himself calls the longer work De Temporibus Liber Maior" (l.2736-2738). III.17 does not say which book it means, and the held lines do not settle it. Fix, for `about`: "his book on reckoning time, which Plummer dates to 703. Plummer reports that a charge of heresy was later brought against Bede over it. In the History Bede says he proved in his book "De Temporibus" that Aidan of Lindisfarne kept Easter wrongly. Plummer notes that Bede also calls his larger book on time De Temporibus."

- **A-M7 MINOR (card `uncertain` 3 and 1; item 1; a modern author counted as a chronicler, and names with no context).**
  - (a) "later chroniclers who put it in 674, 677 or 678." The 674 is Stevenson's, in his Church Historians, and Plummer calls its grounds "very precarious" (l.557-559). The 677 comes from the Lindisfarne annals and Simeon of Durham (l.543-545), and the 678 from Florence of Worcester (l.560-561). Fix: "Plummer reckons his birth from Bede's own words as 672 or 673. He notes that the Lindisfarne annals and Simeon of Durham put it in 677, and Florence of Worcester in 678. Stevenson, in his Church Historians, puts it in 674, on grounds Plummer calls very precarious."
  - (b) "the case of Lumby and Mayor for 742" gives no word on who they are. Fix: "He sets aside the case for 742 made by Mayor and Lumby, from whose edition he prints Cuthbert's letter." Source: l.5530-5534 and l.5555-5556 ("as given by M. & L.").

- **A-M8 MINOR (card `legacy.remembered` 1; item 4; a beat line).** "Rome honors him." adds no fact. Fix: delete it, and start "The Roman Breviary keeps Bede the Venerable on 27 May…". With A-M9, add: "Its lessons also read his homilies and passages of his History."

- **A-M9 MINOR (notes, "Differences" 5 and 6; incomplete searches behind two flagged census differences, and a held trace left unused).**
  - (a) "the Breviary holds only a calendar line for Bede" is false. The same volume reads "Homily by the Venerable Bede" about nineteen times (e.g. l.30252, 40578, 44848). It also gives lessons "From the Venerable Bede's History" (l.61583-61584, 77302-77304).
  - (b) "no held line … dates the seven books to 800" is false. Migne heads Alcuin's covering letter "Epistola beati Alcuini ad Carolum Magnum. (Anno 800.)", and the letter "Commendat … libros [vii] adversus Felicem" (PL100-101 l.9436-9442).
  - Fix: withdraw both differences from the census list. Optionally, restore "about 800, when Alcuin sent them to Charlemagne, by Migne's heading" to `legacy.traces` 2. Add the Breviary homilies to the records and to the card, as in A-M8.

After the fixes (A-M1 to A-M5 in the brief): 405 words, about 2:30, FK 6.5, Flesch 71.8 (scratch copy scored).

---

### Hild of Whitby (major; 405 words, about 2:30; FK 5.4, Flesch 79.4)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B2, A-M10, A-M14, A-M15) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M11, A-M13) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Stephen is "Wilfrid's biographer") |
| 7 | Contested claims both sides | PASS (Stephen and Bede in place in P5; Thomas of Ely and Bede on the card) |
| 8 | Common names | FAIL (A-M12) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS (FK 5.4 is well under the grade 8 floor; see note) |
| 12 | Card order, fields, caveat repeated | FAIL (A-M16) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Sentences checked and found faithful.**
- P1: Caedmon, IV.24 (GILES l.11137-11203). "In huius monasterio abbatissae" ties him to Hild (PLUMMER l.25149).
- P2: Hereric, Edwin and the faith are at GILES l.10899-10904, and Edwin's baptism at York in 627 is at l.4994-5002. "Some fifty years" runs from 680 to 731 (l.10890, 15408).
- P3: thirty-three years, the East Angles and Cale are at l.10895-10923. Aidan's recall follows Bede's Latin, "ab Aidano episcopo patriam reuocata" (PLUMMER l.24865-24866), against Giles's garbled English (l.10925-10926). Heruteu and Aidan's teaching are at l.10931-10946. Jane's "Heruteu = Hartlepool" is a garbled note on p. 192 (l.15949).
- P4: "either to build or to arrange" is at l.10950-10952. Peace and charity, the first church, and kings and princes are at l.10954-10963. A house of men and women is at l.11515-11519. The five bishops and "Mother" are at l.10973-11016.
- P5: the synod of 664 is at l.7955-7968, 8236-8238 and 8215-8218. In Stephen, ch. 10, "in coenobio quod Streuneshalgh dicitur, presente sanctimoniale matre piissima Hilde" (RAINE l.5067-5081). Pope John's letter, ch. 54, says "qui a Theodoro … et Hylde religiosae memoriae abbatissae, ad eum accusandum huc prius advenerant" (l.9384-9425). I checked "Bede is silent on it": Bede's life of Wilfrid mentions his accusers but neither Theodore's men nor Hild's (GILES l.14029-14094).
- P6: the fever, the deathbed and the dream are at l.11021-11060, and "whose life was a bright example" is verbatim (l.11034-11035).

**Card.** I checked these against their lines:
- `knownFor`, `dates` (655 at l.7703; "two years after" at l.7770-7772, Latin "Quae post biennium", PLUMMER l.21154-21157), `place` (l.7769, 7958-7959, 15953, 16013), `role`.
- `legacy.traces` 1, 3 and 4. Bosa, Aetla and the rest are at PLUMMER l.24946-24956, and John's priest Wilfrid at GILES l.12539-12541.
- `legacy.remembered` 1, 3, 4 and 5 (PLUMMER l.5224-5228; Prymer l.11647; RAINE l.1611, "the cradle of our national poetry").
- `uncertain` 2, 3, 4 and 7. Thomas of Ely is at AASS Jun. 5 l.95476-95486 and l.93770, and the Bollandists' "ante finem seculi xii" at l.93125-93126.

**Absence searches.** The other held witnesses are the ones the records list. No source gives words of hers beyond the deathbed charge. The Bollandists' "colitur 15 Decemb." (AASS l.95275) is a feast day and does not conflict with Bede's death day.

**Readability note.** FK 5.4 is a pass. The sentences average 13.5 words, at the low end of the 12-to-20 band, and P4 runs on short ones ("Kings and princes asked her advice."). The fixes below join two sentences. A further pass for sentence variety would help, but I do not count it as a finding.

#### Findings

- **A-B2 BLOCKING (card `uncertain` 1; item 1; a count that is wrong).** "He tells her life in one chapter, with her place at Whitby and the story of Caedmon in two more." Bede names or places her in IV.23 (her life), III.24 (Heruteu and the founding of Whitby, GILES l.7768-7778), III.25 (the synod at her house, l.7958-7967), IV.24 (Caedmon, "this abbess's monastery") and the V.24 summary of years (l.15360-15363). That is three chapters besides her life, and one annal. The card's own `sources` lists III.24-25, IV.23-24 and V.24. Fix: "Most of what is known of her comes from Bede, writing about fifty years after her death. He tells her life in one chapter. Three more tell of her houses, the synod at Whitby and Caedmon, and his summary of years notes her death. Her dates come from his reckoning."

- **A-M10 MINOR (brief P1; item 1; Bede's comparison widened).** "Bede says no one in England could compare with him in religious song." Bede compares him with those who came after: "Others after him attempted, in the English nation, to compose religious poems, but none could ever compare with him" (l.11147-11150). Fix: "He was Caedmon. Bede says no later English poet of religious song could compare with him."

- **A-M11 MINOR (brief P5; item 4; an undefined term).** "the Scots" will be heard as people of Scotland. Bede says the Scots came into Britain "migrating from Ireland" (l.380-382). Fix, together with A-M12: "Hild and her followers held with Bishop Colman of Lindisfarne and the Scots, as Bede calls the Irish." The link to Aidan is dropped for length. "Of Lindisfarne" makes the link.

- **A-M12 MINOR (brief P5; item 8; common names).**
  - (a) "Bishop Colman" is a common Irish name with no place. Bede has him in "the same church of Lindisfarne" (l.8262-8269) and bishop after Finan (l.8239-8241). Fix: in A-M11.
  - (b) "Pope John" names one of many Johns. The letter is later than the events it reports: it looks back to "praedecessore nostro Agathone" and calls Hild "of religious memory" (RAINE l.9419-9425). The brief's "went to Rome" also leaves the time out. Fix: "He copies a later letter of Pope John. It says men sent by Theodore of Tarsus and by Hild had come to Rome under Pope Agatho to accuse Wilfrid." That is 8 and 22 words, and it also splits the 25-word sentence.
  - For length, P3's "She lived thirty-three years in the world. Then she went…" becomes "After thirty-three years in the world, she went…" (l.10896-10898).

- **A-M13 MINOR (card `legacy.remembered` 2; items 1 and 4; a tail that misframes Bede).** "He tells both as the nuns' visions." Bede tells the first as God's act: "it pleased Almighty God, by a manifest vision, to make known her death" (l.11064-11066). He gives the second as "It is also reported" (l.11111). Fix: replace the last two sentences with "Bede presents this as a manifest vision by which God made her death known. He adds, as a report, that a nun at Whitby saw the same that night."

- **A-M14 MINOR (card `uncertain` 5; item 1).**
  - (a) "Charles Plummer describes the Scots as the Irish monks of Iona." Plummer does not gloss Bede's word. He writes of "the Irish monks of Iona, by whom Northumbria was reconverted" (PLUMMER l.988-990).
  - (b) "Bede does not say how she answered the ruling." Bede says "all present, both great and small, gave their assent" (l.8215-8217).
  - Fix: "The synod. Bede says Hild and her followers held with the Scots, and that King Oswy ruled for the Roman Easter. Bede says the Scots came into Britain from Ireland. Charles Plummer writes of the Irish monks of Iona, by whom Northumbria was won back to the faith. Bede says all present assented to the ruling, and gives no word of hers. Stephen also places the meeting at her monastery and in her presence."

- **A-M15 MINOR (card `legacy.traces` 2; item 1).** "Tatfrid, chosen bishop there before him…" Bede has him chosen "before the aforesaid man of God, Bosel" (GILES l.11007-11010; Latin "ante praefatum uirum Dei Boselum", PLUMMER l.24986-24990). Bosel held the see before Oftfor. Fix: "Tatfrid, from her house too, had been chosen bishop there before Bosel, Oftfor's predecessor, and died before he could be ordained."

- **A-M16 MINOR (card `uncertain` 6 and `otherNames`; item 12).**
  - (a) `uncertain` 6 reports a fault in one translation's English, not something uncertain about Hild. Bede's Latin is clear (PLUMMER l.24865-24866). Fix: delete it from the card. Keep it in the records (claim 5 already holds it) and in the notes.
  - (b) `otherNames` repeats "Hild", which is already the card's name. Fix: remove "Hild" from `otherNames`.

After the fixes (A-M10 to A-M12 in the brief): 407 words, about 2:30, FK 5.4, Flesch 79.1 (scratch copy scored). The scratch copy is at the path given above.

#### Verdicts

- Bede: NOT CLEAR (1 blocking, 9 minor).
- Hild of Whitby: NOT CLEAR (1 blocking, 7 minor).

## R1 review, part B: Aidan of Lindisfarne, Adomnán of Iona (era 4 Who batch 1)

Reviewer: independent Opus, seeing these drafts for the first time. I edited no profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

The bar: `Who_Profile_Pattern.md` (checklist 1 to 14), `CLAUDE.md` ("Trust and source fidelity", "Accessible and rigorous"), the era 3 batch 8 R1 for format and for how it graded findings, the Decision-Log entries for era 3 batches 6 to 8, and the coordinator's rulings in the reviewer brief. For each id I read the brief, the card, the audio and the scratch records and notes. I opened every cited line in its vendored file and read it in context, allowing for OCR noise and line breaks. Before accepting any absence I searched all of `cic/texts/`: for `Aidan/Aedan/Aidanus/Edan*/Lindisfarn*` in the Annales Cambriae, Bede and Huyshe; for `Adamnanus/Adamanus/Adomnan*`; for `cain Ad*`, `lex innocent*`, `law of Ad*` and `Birr`; and for `captiv*`, `prisoner` and `hostage` near Adomnán. Brief paragraphs are P1, P2 and so on. Readability comes from `engine.m1.gates.grade_text`, run from the repo root. All the suggested brief fixes for each profile were applied together to scratch copies and scored again: `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/fixB/aidan.txt` (405 words, FK 6.2, Flesch 78.3) and `.../fixB/adomnan.txt` (405 words, FK 7.3, Flesch 71.3).

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or a card. Every brief fix below has to be carried into the audio. Both cards follow Mark's order and have no empty or null fields. Every `sources` file exists. No card sentence runs past 25 words. Both tradition pairs use census movement names. The drafts carry no list lines, so the list-line half of item 14 was not checked. I compared both profiles with the approved Columba (era 3 batch 5) and Ciaran of Clonmacnois (era 3 batch 7) profiles, and with this batch's Hild and Bede cards, and found no contradiction. Columba's card says Huyshe places the Life "between 679 and 704" (Huyshe's title-page span, HUY l.87). The Adomnán card says Huyshe reports the view that it was written between 692 and 697 (HUY l.1999-2000). The two agree, since the second range falls inside the first.

---

### Aidan of Lindisfarne (major; 405 words, 2:30; FK 6.6, Flesch 76.5)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B1, B-B2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M2, B-M3, B-M4) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Bede "who followed the Roman Easter", placed once) |
| 7 | Contested claims both sides | FAIL (B-B2) |
| 8 | Common names | FAIL (B-M1) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 opens with "Nearly all … from Bede") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (census Anglo-Saxon and Insular entries both name him among their voices) |

**Sentences checked and found faithful.** P1: "It is reported, that when King Oswald had asked a bishop of the Scots … there was first sent to him another man of more austere disposition … returned home … because they were uncivilized men, and of a stubborn and barbarous disposition". Then Aidan: "did not at first, conformably to the apostolic rule, give them the milk of more easy doctrine", and "presently concluded, that he deserved to be made a bishop … being ordained, they sent him" (GILES l.5965-5999). "Scots" as the Irish: GILES l.5757-5758. P2: "a monk of the island called Hii" (l.5794-5795). The tidal island is at l.5763-5768. "Not skilful in the English tongue … the king himself interpreting … for he had perfectly learned the language of the Scots during his long banishment" (l.5772-5782). The Breviary gives "could not speak English well" (BREV l.61596-61597). The 731 date is "the 731st year" (l.15189-15191), and "as near as I could be informed by those that knew him" is at l.7003-7004. The 630s follow from the annals' 651 (l.15317-15318) and the "seventeenth year" (l.6939); the Bollandists give 635 (AASS-Mar3 l.32776-32779). P3: "taught no otherwise than he and his followers had lived", "traverse both town and country on foot", "to alms and good works", "ransoming such as had been wrongfully sold for slaves … advanced them to the order of priesthood" (l.5919-5963). Eata: l.8258-8268. P4: Oswin's horse, the king's complaint, "Is that foal of a mare more dear to you than the Son of God ?", the king kneeling, the tears and "the king will not live long" (l.6761-6808). The death "twelve days after the king he loved, on the 31st of August" is at l.6812-6818, with the annals' 651. P5: "from the fourteenth to the twentieth moon" (l.5751-5752). "Very much detesting the same" (l.6985-6988). "On the Lord's day" (l.7026-7029). "Patiently tolerated by all men" (l.7903-7905). Plummer's "It is sad" (PLUM l.2806-2809). P6: the Anonymous Life, "animam sanctam, quasi in globo igneo ad coelum efferri … post paucas dies … eadem hora noctis" (AASS-Mar3 l.38813-38832; the heading "Auctore monacho Lindisfarnensi coaevo" is at l.38593-38596). P7: l.6994-7011.

**Card.** I checked each `legacy` and `uncertain` line against its source: III.3 (l.5781-5794), IV.27 (l.11650-11657), the Wednesday and Friday fast (l.5950-5954), Chad (l.8479-8487), Hild and Heiu (l.10924-10946, with PLUM l.24866-24868), III.25 and Honorius and Felix (l.7903-7914), Alcuin (ALC l.64991-64995, 65627-65657, 66242, 64738-64741), the Breviary (BREV l.2279, 61468-61475), the wonders (l.6827-6982), the sixteen and seventeen years (l.6925, 6939, 8240), Jane's note "' ' The royal city " — Bamborough" (l.15916; Jane is named as author at l.15582-15586), King Aedan (GILES l.3189-3190; HUY l.3070, 9172-9173), Rees's "Maidoc, qui et Aidanus" (REES l.6518), and the Annales Cambriae, which name only Aidan son of Gabran and Aidan son of Blegywryd (AC l.2572, 4241; no Lindisfarne hit). I checked the otherNames Aedan (PLUM l.18699), Aidanus (AASS-Mar3 l.34572) and Edanus (ALC l.66242). The tradition call fits: both census windows hold 635-651, and both entries name him.

#### Findings

- **B-B1 BLOCKING (brief P5 and audio; item 1; Plummer's words attached to the wrong statement).** "Yet he grants that Aidan always kept it on a Sunday, and that the difference was patiently borne while he lived. Charles Plummer calls it "sad" that Bede pauses to say so." Read aloud, "say so" points back to the sentence just before it, Bede's grant that the difference was borne patiently. Plummer finds something else sad: "It is sad that he should think it necessary to pause in the middle of his beautiful sketch of the sweet and saintly character of Aidan to say that he 'much detests' his mode of keeping Easter" (PLUM l.2806-2809). The "patiently tolerated" line is also in a different chapter, III.25 (GILES l.7903-7905), and has nothing to do with the pause in III.17. The listener is also told nothing about who Charles Plummer is (Pattern: "any name a general listener would not know"). Fix: "Bede, who followed the Roman Easter, says he detests this. Charles Plummer, who edited Bede in 1896, calls it "sad" that Bede breaks off his praise of Aidan to say so. Yet Bede grants that Aidan always kept it on a Sunday. While Aidan lived, he adds, all bore the difference patiently." (Plummer's edition: PLUM header l.2-4, "edited by Charles Plummer", 1896.) To stay within 405 words, take out P3's last sentence, "One of the twelve English boys he took to teach, Eata, later became bishop of Lindisfarne." Card `legacy.traces` 4 already carries it.

- **B-B2 BLOCKING (brief P6 and audio; items 1 and 7; a disputed detail told as narrator's fact, with its witness split off).** "In a saint's Life of Cuthbert of Lindisfarne, an unnamed Lindisfarne monk says the young shepherd Cuthbert saw a soul carried to heaven. Days later came news that Aidan had died that hour." The second sentence has no witness. It states as fact the one point on which the two held Lives disagree. The anonymous monk has "post paucas dies" (AASS-Mar3 l.38829-38832). Bede's prose Life has Cuthbert learn it "mane facto", the next morning (l.34343-34347). The records list this as a `contested_claim`, and card `uncertain` 5 gives both sides. The brief gives one side and leaves the other out. The sentence also opens awkwardly, with "Lindisfarne" twice in one line. Fix: "An unnamed Lindisfarne monk wrote a saint's Life of Cuthbert of Lindisfarne. He says the young shepherd Cuthbert saw a soul carried to heaven, and days later heard that Aidan had died that hour. Bede's Life of Cuthbert says he learned it the next morning." To pay for the words, change P7's first sentence to "Bede praises Aidan's love of peace and his care for the afflicted and the poor." Bede has "his tenderness in comforting the afflicted, and relieving or defending the poor" (GILES l.7000-7002). This also drops a three-part list the narrator picked from Bede's eight. And in P2, change "drawing on those who had known him" to "from those who had known him".

- **B-M1 MINOR (brief P1; item 8; the subject's own common name with no place at first mention).** P1 introduces "Aidan" with no identifier. The card's own `uncertain` 7 names two namesakes, King Aedan and Rees's Aidan, and the Pattern rule covers the subject's own name. Fix: P1 "Aidan, a monk of Iona, told him he had been too severe…". Bede says Aidan "was also present in the council" and was sent "from the aforesaid island, and college of monks" (GILES l.5914-5915, 5989-5990). Then begin P2 with "He came to the English from Iona, which Bede calls Hii, in the 630s." in place of "Aidan was a monk of Iona, which Bede calls Hii, and came to the English in the 630s."

- **B-M2 MINOR (brief P1; item 4; an awkward opening).** "Bede tells, from report, of a council…" is stiff to read aloud. Fix: "Bede passes on a report of a council among the elders of the Scots, as he calls the Irish." The source has "It is reported" (GILES l.5965).

- **B-M3 MINOR (brief P3 and card `knownFor`; items 1 and 4; "free people" reads two ways, and the card drops "wrongly").** In the brief, "Gifts from the rich went to the poor, or to free people wrongly sold as slaves" can be heard as gifts going to free people. In the card, "to free slaves" drops Bede's "wrongfully sold" (GILES l.5960-5961). Read that way, it turns ransom into a general freeing of slaves. The card sentence is also a three-verb list ("set … walked … gave"). Fix the brief: "…or to ransom people wrongly sold as slaves." Fix the card: "He set his see on Lindisfarne and gave what he was given to the poor and to ransom people wrongly sold as slaves."

- **B-M4 MINOR (brief P2 and card `knownFor`, `role`, `legacy.traces` 2; item 4; an undefined term).** "Gave him a see on Lindisfarne." Most listeners will not know "see". The fixed scratch copy keeps the word to stay inside the cap. If any words come free, use "Oswald gave him Lindisfarne, an island at high tide, as the seat of his bishopric." Bede has "appointed him his episcopal see in the isle of Lindisfarne" (GILES l.5763-5764). This is optional. Nothing here is false.

- **B-M5 MINOR (card `sources`; item 12).** (a) Plummer's Latin is titled "Book III", but the card's Hild line rests on his IV.23 (PLUM l.24866-24868). Make it "Books III and IV.23". (b) The Giles list leaves out I.34, where `uncertain` 7 relies on King Aedan (GILES l.3189-3190). (c) `uncertain` 7 also relies on Rees's Lives (REES l.6518), Adomnán's Life in Huyshe (HUY l.3070) and the Annales Cambriae, and none of these is listed. Add the three, or cut those two clauses. (d) In the same item, "David of Wales" is not the form the source uses. Rees uses Menevia (REES l.18000-18003), so write "David of Menevia".

- **B-M6 MINOR (records).** The claim "Bollandists date the anonymous Life … circa annum DCC" is tagged Documented, but the Bollandists give it as their own view ("Videtur", AASS-Mar3 l.32852-32853). Tag it Dominant Modern Reconstruction, naming the Bollandists. The same holds for the "635" in the "630s" claim (l.32776-32779).

---

### Adomnán of Iona (major; 402 words, 2:29; FK 7.2, Flesch 71.7)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M8, B-M9) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M7, B-M10) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | FAIL (B-M10: Ceolfrid) |
| 7 | Contested claims both sides | PASS (Bede and the preface against Jane, in place in P4) |
| 8 | Common names | PASS |
| 9 | One term for one thing | FAIL (B-M11) |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 carries the Huyshe and saint's-Life caveats) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Sentences checked and found faithful.** P1: Ceolfrid's question, "why do you imitate the tonsure of him whom St. Peter anathematised ?", and the answer, quoted verbatim, "though I have Simon's tonsure, according to the custom of my country, yet I utterly detest and abhor the Simoniacal wickedness" (GILES l.14883-14899). "Sent ambassador by his nation to King Alfrid, came to see our monastery" (l.14883-14886). Ceolfrid's abbey is at l.14333-14337, and the letter sits inside Bede's text at l.14355-14360. "Aldfrith" is Huyshe's spelling (HUY l.1989). P2: HUY l.1979-1994, and its "foster-son, or alumnus" is at l.1989-1990. P3: the three books (HUY l.2039-2048). The preface quotation is verbatim (l.2084-2087). Failbeus, "my predecessor", with Oswald's vision, is at l.2420-2424. The plague and "my friend, King Aldfrid" are at l.9123-9132. P4: Bede V.15 (GILES l.13594-13620). The preface is "mihi Adamnano … dictavit" (PL88 l.66266-66270). Jane's note is "It is doubtful if he really wrote the book De Situ Terrae Sanctae here quoted by Bede" (GILES l.16033-16035). P5: GILES l.13551-13592, and "a good and wise man, and remarkably learned in Holy Scripture" is verbatim (l.13566-13567). P6: White, "Acts of the Synod held at Birr, by Adamnan, A.D. 695-697" (WHITE l.3768-3770). Stokes, "Adamnan's rule, not to slay women" (STOKES-TRIP l.13852, 13863-13864; OCR "Adamiian's"). P7: "pro eodem sancto sacerdote Arculfo divinam precentur clementiam … pro me misello peccatore eorumdem craxatore" (PL88 l.68716-68732).

**Card.** I checked each line against its source: the canons and d'Achery (WASS l.6930-6968), the Annales Cambriae's "Dormitatio Adomnan" at 704 (AC l.2801-2802), Alcuin's altar verse "Adomnanus atque, Praeclari Patres, morum vitaeque magistri" (ALC l.60492-60496), Reeves and Cormack (HUY l.2016-2018, 2033-2034), Cummene (HUY l.9547-9552), Egbert, Dunchad, 716 and 715 (GILES l.14983-15031, 5877-5878), the Book of Leinster's "[693.] Adamnan brought the captives to Ireland" (STOKES-TRIP l.14840, 14912), Huyshe on women freed from fighting (HUY l.1586-1590), and the Coldingham Adamnan (GILES l.11316-11317). The absences hold. No held file has the text of Cáin Adomnáin, the acts of Birr, or whose captives these were.

#### Findings

- **B-M7 MINOR (brief P6 and audio, card `uncertain` 3 and `legacy.traces` 4–5; item 4; a late witness given no date, and names with no context).** "A note in the Lebar Brecc, printed by Whitley Stokes…" A listener does not know what the Lebar Brecc is. Nor would they guess that it is about seven hundred years later than Adomnán. Warren calls it "a collection of pieces in Irish and Latin, compiled from ancient sources about the end of the fourteenth century" (antiphonary-of-bangor-pt2 l.17719-17720). Huyshe calls it "the fifteenth-century manuscript" (HUY l.1684-1685). "Newport White" is likewise given with no context. Fix the brief: "Newport White, who edited Patrick's writings, says Adomnán held a synod at Birr in the late 690s. A note in the Lebar Brecc, an Irish manuscript of about 1400, counts Adomnán's rule among four rules of Ireland, "not to slay women"." (White's book: "St. Patrick, His Writings and Life", file header.) In card `uncertain` 3, add after the first sentence: "The Lebar Brecc is an Irish manuscript of about 1400." In card `legacy.traces` 4, write "Muirchu, who wrote a Life of Patrick," (WHITE, "Introduction to Muirchu's Life of St. Patrick", l.171, 3589).

- **B-M8 MINOR (brief P5 and audio; item 1; the sequence compressed so that he seems to die in Ireland).** "In Ireland he brought many to the canonical Easter, and he died before the next year came round." Bede has him return to Iona after the Irish Easter, try again and fail, and only then die: "Returning to his island, after having celebrated the canonical Easter in Ireland … he departed this life before the next year came round" (GILES l.13582-13587). Huyshe also has him die in Iona (HUY l.2001-2004). Fix: "In Ireland he brought many to the Roman Easter. He went home and died before the next year came round." For the term, see B-M11.

- **B-M9 MINOR (brief P4 and audio; item 1).** "A storm had driven Arculf onto Britain's west coast on his way home from Jerusalem." Bede has Arculf travel on from Jerusalem to "Damascus, Constantinople, Alexandria, and many islands" before he was "returning home by sea" (GILES l.13598-13602). Fix: "…on his way home." To stay within 405 words, also cut "Bede says he gave the book to Aldfrith." Card `keyWorks` 2 already carries it.

- **B-M10 MINOR (brief P1 and audio; items 4 and 6; a partisan witness not marked, and "tonsure" not explained).** Ceolfrid wrote the letter to argue for the Roman Easter and tonsure. Naitan asked him for "arguments, by the help of which he might the better confute those that presumed to keep Easter out of the due time; as also concerning the form and manner of tonsure" (GILES l.14338-14342). The brief tells his story with no marking of whose side he was on. "Tonsure" is also left unexplained for a listener. Fix: "Ceolfrid, abbot of Wearmouth and Jarrow, once asked a guest why his head was shaved like that of the man Saint Peter had cursed." And "Ceolfrid, who argued for the Roman tonsure, told the story in a letter that Bede copied into his History." Ceolfrid has "wear on your head a crown … imitate the tonsure of him whom St. Peter anathematised" (l.14889-14893). To stay within the cap: in P5, "He changed his mind, but could not win his monks of Iona." In P2, "the exiled Aldfrith".

- **B-M11 MINOR (brief P5 and card `knownFor`, `dates`, `legacy.traces` 1–2; item 9).** One Easter has four names: "canonical Easter" (brief, `dates`, traces 1), "Catholic Easter" (traces 2), "Roman Easter" (`knownFor`) and "Roman reckoning" (`uncertain` 5). The Aidan and Columba profiles use "the Roman Easter". Fix: use "the Roman Easter" in the brief's P5 and in `dates`, traces 1 and traces 2, and keep "Roman reckoning" only where it means the reckoning.

- **B-M12 MINOR (card `tradition`; for the coordinator).** The second tradition, "Insular / Irish Monastic Christianity" (c.450-664), fits him only through Huyshe's undated "became a monk under his kinsman, Seghine", Seghine being abbot until 652 by Huyshe's own note (HUY l.1985-1986, 2538-2539). Every dated act falls after 664. The census Insular entry lists him at 679, which is outside its own end year. The drafter's call, Medieval Irish first, is sound, and the card need not change. The census row's year is the one to log as an inconsistency.

- **B-M13 MINOR (card `sources`; item 12).** The Bede English title leaves out III.4, which gives the 715 in traces 2 (GILES l.5877-5878), and IV.25, the Coldingham namesake in `uncertain` 7 (l.11316-11317). Add both.

- **B-M14 MINOR (records).** The otherNames claim cites "Adamnanus" from Plummer's oblique cases ("instante Adamnano", "Adamnanum"). Plummer's only nominative "Adamnanus" (PLUM l.25354) belongs to the Coldingham namesake. Cite the nominative for this man from PL 88 l.66004 ("Adamnanus pre[s]byter et abbas") instead.

---

### Counts

- Aidan of Lindisfarne: 2 blocking (B-B1, B-B2), 6 minor (B-M1 to B-M6).
- Adomnán of Iona: 0 blocking, 8 minor (B-M7 to B-M14).

## R1 review, part C: Boniface of Mainz, Alcuin of York (era 4 Who batch 1)

Reviewer: independent Opus, first sight of these drafts. I did not edit any profile file, and made no git, web, paid or model calls. I used local scripts only. Scratch copies with the fixes below applied are in `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/rC/`.

### Method

- I read every brief sentence and every card field against its cited line in `cic/texts/`, in context. Files opened: `boniface_english-correspondence_kylie1911.txt`, `capitulatio-de-partibus-saxoniae_pertz1881.txt` (Boretius, Capitularia 1), `annales-regni-francorum_kurze1895.txt`, `bede_opera-historica-v1-historia-abbatum-lat_plummer1896.txt`, `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`, `alcuin_opera-omnia-letters_migne-pl100-101_1863.txt`, `roman-breviary_bute1908.txt`.
- I re-checked all quotations against the files: the Lioba letter (Kylie l.5878), "one blood and one bone" (l.7522), the watchdog (l.7047-7051), the Stephen letter (l.1550-1553), and Milret (l.7891-7892). All are verbatim, allowing for OCR noise.
- The brief also asked me to test the drafter's claim that the Alcuin file holds PL 101 only. **I confirm it.** The title page reads "PATROLOGIAE LATINAE TOMUS CI" (l.218), and the contents begin at "Operum pars tertia" (l.430-433). The only letters in the file are:
  - three letters ascribed to Angilbert, in an appendix (l.103470-103520);
  - a pointer to Charlemagne's letter to Elipandus in PL 98 (l.106099-106105);
  - letters quoted inside Mabillon's and Froben's essays.

  I searched for "voluntaria", "decimas", "Megenfr", "Higbald/Hygbald" and "fides res est" across the whole of `cic/texts/`, with whitespace-tolerant patterns. They hit only Migne's index (l.118264, 119766), unrelated passages, or Bede's Hygbald. The file header's "including his letters" and "extensive, genuine Alcuin correspondence with Arn" are wrong for this file. That is a Library-header fault for the Library thread, not a profile fault.
- Other false-absence tests:
  - Willibald's Life of Boniface. Searched Willibald/Willebald/Uuillibald across all files. Only the Bollandists' one-phrase quote (AS l.164194-164197) turned up, plus late references. The absence holds.
  - Geismar/Gaesmere/robur Jovis. Kylie only. Holds.
  - Alcuin's 796 Saxon letters. Not held anywhere. Holds.
- Census: I checked `anglo-saxon-christianity` and `carolingian-reform-christianity` in `cic-website/data/world-census.json`. Findings C-M9 and C-M17 below.
- Readability by `grade_text`, word counts by `wc -w`. I compared the audio with the brief after stripping the tags.

---

### Boniface of Mainz (major, cap ~405 words)

401 words (about 2:29). FK 7.4, Flesch 70.0. Audio equals the brief once `[calmly] ` and `[warmly] ` are removed. There are no tags in the brief or the card.

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-B1; C-M1, C-M5) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (C-M3, C-M4) |
| 5 | No role for a named witness | PASS |
| 6 | Partisan witness marked | PASS (none hostile; Kylie named as a modern account) |
| 7 | Contested claims both sides | PASS (754/755; archbishop 732/synod) |
| 8 | Common names, first mention | FAIL, minor (C-M7) |
| 9 | One term for one thing | FAIL, minor (C-M2) |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS (FK 7.4, Flesch 70.0) |
| 12 | Card order, no empty fields, caveat repeated | PASS (uncertain opens with the brief's "Kylie's modern account is the main witness") |
| 13 | Audio tags placement | PASS |
| 14 | List line kept; Who test | PASS (census people row unchanged) |

**C-B1 BLOCKING (brief, paragraph 5).** "Boniface told Pope Zacharias that Carloman had promised to set right the church's order." The Latin Boretius prints reads "promisit, se de aecclesiastica religione ... aliquid corrigere et emendare velle" (OCR "rclij:,ione", "conngerc ct"; capitulatio l.2203-2205). Carloman promised to correct and amend *something* concerning the church. The brief drops "aliquid" and turns a limited promise into a full one. That is a rendered Latin passage that drops its qualifier. Fix: "Boniface told Pope Zacharias that Carloman had promised to do something to set right the church's order."

**C-M1 MINOR (brief, opening sentence).** "In 754 Boniface ... sailed down the Rhine toward Frisia for the last time." Kylie gives no year for the departure (l.1749-1761). He dates only the death: "on June 5, 754" (l.1815). Fix: move the year to the death. Open with "Boniface, archbishop of Mainz, sailed down the Rhine toward Frisia for the last time." In the third sentence, write "On the fifth of June 754 at Dokkum, he writes, ...".

**C-M2 MINOR (brief paragraph 3; card keyWorks 1).** "Cynehild" is not in any held source. Kylie has "Cynehilda" (l.486, 5873, 8039) and "Chunihilt" (l.1200). The brief's "he wrote that he would 'beseech, nay all but command' them" also turns Boniface's present "I beseech" (l.5878) into a conditional. Fix for the brief: 'He wrote to Lioba, Tecla and Cynehilda, "I beseech, nay all but command you," and asked them to pray for him.' The card should read "Cynehilda" too.

A related point for the coordinator: the census person row names her "Leoba", and the profile uses Kylie's "Lioba". It is one person across the tree. Either keep Kylie's form, as the census quote's own work title does ("Lioba to Boniface", in the Leoba people row), or write "Lioba (Leoba)" at her first mention on the card. This is the coordinator's call; log it either way.

**C-M3 MINOR (brief, paragraph 4).** "The Saxons themselves, he reminded them, were wont to say." Kylie's line is a plea: "Have pity on them because even they themselves are wont to say" (l.7521-7522). "Reminded" misframes it. "Wont" is archaic in the narrator's own voice. Fix (same word count): 'Have pity on them, he wrote, for they themselves say, "We are of one blood and one bone."'

**C-M4 MINOR (brief, paragraph 5).** "In a letter Alfred Boretius prints with the decree, ..." gives a listener a name with no context. Boretius is the nineteenth-century editor, and the witness is Boniface, who is already named. The sentence also runs to 23 words. Fix: "In a letter printed with the decree, Boniface told Pope Zacharias ...". The card already names Boretius in its sources.

**C-M5 MINOR (brief, paragraph 6).** "After a synod in 747, he sent its decrees to Cuthbert." The year is Kylie's (l.1637-1638; letter heading "747+", l.6872). Boretius's headnote holds that synod's year only as a conjecture: "in alia quoque regni Francorum synodo anno 747 ut coniicere licet habita" (capitulatio l.2209-2210). Fix: "After a synod Kylie dates to 747, he sent its decrees to Cuthbert, archbishop of Canterbury."

**C-M6 MINOR (card, `role`).** "legate in Germany of the Roman church." Letter XLV reads "legate in Germany of the universal Church and servant of the Apostolic See" (Kylie l.7497-7499). Fix: "legate in Germany of the universal Church, as he called himself".

**C-M7 MINOR (card, `legacy.traces` 3).** "taught at Utrecht by Gregory, the disciple and successor of Boniface the martyr." Gregory the Great is named one item earlier in the same card, so this Gregory needs the pattern's name of place. Altfrid: "Gregorio, discipulo et successori S. Bonifacii Martyris ... in Trajecto monasterio" (AS l.164259-164264). Fix: "Liudger was taught by Gregory of Utrecht, the disciple and successor of Boniface the martyr."

**C-M8 MINOR (card, `dates`).** "Kylie gives the day as 5 June." The Bollandists also give it: "Contigit illud Nonis Junii in loco Dockinge dicto" (AS l.161072). Fix: "Kylie gives the day as 5 June, and the Bollandists give the Nones of June, the same day."

The Bollandists also quote Liudger's own Life of Gregory: "quem oculis meis ipse vidi candidum canitie et decrepitum senectute" (AS l.161055-161058), and "Dockingam villulam martyrii sui sanguine consecravit" (l.164199-164200). That is a held eyewitness of Boniface in old age, and of the place of his death. It is not a finding, but it is available if wanted.

**C-M9 MINOR (census, not the profile).** The `anglo-saxon-christianity` story "The Oak at Geismar" says Boniface "was killed in Frisia in 754 by robbers who wanted the chests his party carried". Every held witness says pagans killed him:
- the Royal Frankish Annals: "a paganis interfectus" (l.1668-1670);
- Kylie: "a heathen band" (l.1817).

The profile follows the held sources and is right. The census story is marked "primary text not yet read". Log the difference in Open-Gaps against that census story. No profile change.

Not findings:
- Kylie's "Crediton in Somersetshire" (l.690) is rightly left without the county.
- "Dokkum" is the Bollandists' "Dockum" (l.164202), and the card notes the spellings.
- The tradition placing (Anglo-Saxon Christianity) fits the census people row and the census dates.

After the fixes: 404 words. FK 7.5, Flesch 69.9 (scored on the scratch copy).

---

### Alcuin of York (major, cap ~405 words)

405 words (2:30). FK 7.9, Flesch 66.2. Audio equals the brief once the tags are removed. There are no tags in the brief or the card.

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-B2; C-M12, C-M15) |
| 2 | Quotes verbatim | PASS (no quotation marks in the brief; Latin renderings checked) |
| 3 | No invention | FAIL, minor (C-M10) |
| 4 | Reading aids, no AI tells | FAIL, minor (C-M11, C-M14) |
| 5 | No role for a named witness | PASS |
| 6 | Partisan witness marked | PASS (Elipandus's charge is marked as a charge; Felix's confession is "Alcuin says") |
| 7 | Contested claims both sides | PASS (death 804 / after 810; York poem Gale-Rivet / Oudin) |
| 8 | Common names, first mention | PASS |
| 9 | One term for one thing | FAIL, minor (C-M13) |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS (FK 7.9, Flesch 66.2) |
| 12 | Card order, no empty fields, caveat repeated | PASS (with C-M16) |
| 13 | Audio tags placement | PASS |
| 14 | List line kept; Who test | PASS |

**C-B2 BLOCKING (brief, paragraph 4).** "Alcuin wrote that he came at Charlemagne's call, and that his master had charged him to defend the Catholic faith wherever new sects arose." In the source, the "master" is Alcuin's own teacher, not Charlemagne. The line reads "etiam et ut vir venerabilis totusque Deo deditus meus mihi mandatum dederat magister" (PL 101 l.17303-17305, preface to Against Elipandus). Mabillon names him: "Magister iste Alcuini est Albertus, ex Vitae num. 11" (l.113548). Placed straight after "Charlemagne's call", "his master" will be heard as Charlemagne. That is a source line misread in the telling. Fix (same word count): "Alcuin wrote that he came at Charlemagne's call. His teacher, he says, had charged him to defend the Catholic faith wherever new sects arose." If wanted, the card can add Mabillon's identification of the teacher as Ælberht.

**C-M10 MINOR (brief, opening).** "Liudger, a young Frisian, once traveled to York." Altfrid gives no age. He calls Liudger a deacon: "Liudgerum Diaconem" (AS l.164332) and "studiosus Levita" (l.164404). Fix: "Liudger, a Frisian deacon, traveled to York to study under its master, Alcuin." (Dropping "once" also pays for C-M12.)

**C-M11 MINOR (brief, sentence 2).** "tells it in his saint's Life of Liudger." "Saint's Life" is a genre term, and here it reads as a slip. Fix: "Altfrid, a ninth-century bishop of Münster, tells it in his Life of Liudger." The source for that description is AS l.160459-160463 and l.160510-160530.

**C-M12 MINOR (brief, sentence 4).** "for he would rather die than see his dear son harmed." Altfrid's line is "potius se velle mori, quam ut filius suus dilectus illic quicquam pateretur lethalis mali" (AS l.164434-164436). The fear is of deadly harm. Fix: "for he would rather die than see his dear son suffer deadly harm."

**C-M13 MINOR (card, `legacy.remembered` 1).** "the most learned man anywhere." Einhard's "virum undecunque doctissimum" (l.113571-113572) means learned in every field. The brief renders it that way, so the card both misrenders it and differs from the brief. Fix: "Einhard, as Mabillon quotes him, calls Alcuin a deacon from Britain, of Saxon race, a man most learned in every field."

**C-M14 MINOR (card, `uncertain` 2, last sentence).** "The day itself reads xiv before the Kalends of June, that is 19 May, in two places in this scan, and xvi in one." "In this scan" is process narration in participant text, and the Latin date form is left unexplained. Mabillon himself fixes the day: "nimirum xiv Kal. Junii, ut constat ex Vita, Rabano, et Hariulfo monacho Centulensi" (l.114934-114936; l.115024 in the column). Fix: "Mabillon gives the day as 19 May, from the older Life, from Rabanus, and from Hariulf, a monk of Centula." Keep the OCR "xvi" at l.114740 in the record only.

**C-M15 MINOR (card, `legacy.traces` 1).** "Liudger studied under Alcuin at York for three years and six months." That is Liudger's second stay. On the first, Altfrid has him stay "anno uno" and join Alcuin then ("cui statim vir prudens Liudgerus sedulo jungebatur", AS l.164380-164383). The margin reads "init notitiam cum Alcuino ... ad hunc iterum redit, manetque 3 annos, 6 menses" (l.164341-164357). Fix: "Altfrid's Life of Liudger tells that Liudger studied under Alcuin at York for a year, and later went back for three years and six months. He came home with many books."

**C-M16 MINOR (card, `keyWorks` 3).** The York poem is listed as his key work with no word of the authorship dispute the card itself records under `uncertain`, which names Oudin, Rivet and Gale. Fix: begin the `about` text "ascribed to him, though not by all; a long poem on York's bishops and saints."

**C-M17 MINOR (census, not the profile).** There is no contradiction with `carolingian-reform-christianity`. The census person year 782 is the arrival in Francia, and the card's 780 is Mabillon's date for the Parma meeting and invitation (l.113480-113484). The two can stand together. The census story "Verden, and Alcuin's Letter About It" rests on the 796 letters. The card correctly says those letters are not among the sources used here. That story is "primary text not yet read", and the Library lacks PL 100. Log PL 100, or Dümmler's MGH Epistolae IV, as wanted. That entry is already in the drafter's gap list.

Not findings:
- Mabillon's death argument ("ad annum 81[3] aut certe annum 810 excessisse", l.114896-114898) is told as his, and the 804 side is named.
- The claim that Froben dates On the Faith of the Trinity to 802 checks: "existimo de anno 802" (l.616). The card attributes it to him.
- The Frankfurt c. 56 (capitulatio l.5940-5942) and Boretius's note (l.5948-5949) check.
- The honey-and-wine letter (l.113979-113986) checks clause by clause. The brief leaves out its purpose clause, "ut plurimos ... erudiam". That is not a dropped condition.

After the fixes: 405 words. FK 7.7, Flesch 66.4 (scored on the scratch copy).

---

### Counts

| Profile | Blocking | Minor |
|---|---|---|
| Boniface of Mainz | 1 (C-B1) | 9 (C-M1 to C-M9; C-M9 is census-side) |
| Alcuin of York | 1 (C-B2) | 8 (C-M10 to C-M17; C-M17 is census-side) |

Library-thread item, not a profile finding: the header of `alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` says it includes the letters and PL 100. The file holds PL 101 only.

## R1 review, part D: Dhuoda, Nennius (era 4 Who batch 1)

Reviewer: independent Opus, first sight of these drafts. I did not edit any profile file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `CLAUDE.md`, `Who_Profile_Pattern.md` (checklist 1 to 14), the era 3 batch 8 R1 review as the form model, the Decision-Log rulings from l.2732, and the coordinator rulings in the reviewer brief. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, the scratch records and the drafter's notes. I opened every cited line in its vendored file and read it in context. Every quoted string in both records files was matched by script against its file, folding OCR noise and hyphen breaks. All matched, and the line numbers I spot-checked by hand are right. Absence checks: I searched all of `cic/texts/` for Dhuoda / Dodana / Duodana / Dodane / Dhuodane (word-start, whitespace-tolerant), for Elbotus / Elvod / Elbod- / Elfod-, for Germanus with Auxerre, and for Stevenson near Nennius. Brief references are to paragraphs (P1, P2...). Readability comes from `engine.m1.gates.grade_text`, run from the repo root. All the brief fixes for each profile were applied together to scratch copies and scored again: `/tmp/claude-0/-home-user-CIC-Project/6b42ac6e-3c4b-56ec-af0b-237963ab96aa/scratchpad/rD/fix/`.

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or card. Neither card has a null or empty field. Each has at most three `keyWorks`, and every `sources` file exists and is the work named. Every brief fix below has to be carried into the audio. Both cards' `dates` field ends without a full stop (see D-M12).

---

### Dhuoda (major; 405 words, 2:30; FK 6.7, Flesch 76.9)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (D-B2, D-M3, D-M8, D-M9) |
| 2 | Quotes verbatim | PASS (no quotation marks; every rendering checked against the Latin) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (D-B1, D-M1, D-M2, D-M4, D-M6) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | FAIL (D-M6, Mabille) |
| 8 | Common names | FAIL (D-M5, D-M6) |
| 9 | One term for one thing | FAIL (D-M1, D-M3) |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 opens with the brief's caveat) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (census `people` row, year 841; WHO under the women's rule, Decision-Log l.2077) |

**Sentences checked and found faithful.** P1: subscription "II anno obitus Ludovici … II kalendas decembris, sancti Andreae missa" (DHU l.12534-12537) and Bondurand's reckoning "a donc été commencé le 30 novembre 841" (l.13229-13230); "écrit à Uzès" (l.216); "Cernens plurimos cum suis in saeculo gaudere proles, et me Dodanam, o fili Willelme, a te elongatam … hoc opusculum ex nomine meo scriptum … dirigo" (l.1893-1896). P2: preface year XI of Louis "in Aquisgrani palatio" (l.2220-2224) with Bondurand's "24 juin 824" (l.2238); Delisle's "Bernard, duc de Septimanie" (l.285-287); births of 29 November 826 and 22 March 841 "in Uzecia urbe" (l.2224-2234, notes); the baby sent "ante quam baptismatis accepisset gratiam" and her stay "sub jussione senioris mei" (l.2256-2262). P3: "Audivi enim quod genitor tuus B. in manus domini te commendavit Karoli regis" (l.2303-2304); Nithard III.2, "victoriam autem ut Karoli esse didicit, filium suum Willelmum ad illum direxit et, si honores quos idem in Burgundia habuit eidem donare vellet, ut se illi commendaret, praecepit" (NITH l.2296-2305). P4: table "De diligendo Deum", "De quaerendo Deum" (l.2318-2320); Bondurand on ch. XII to XV (l.1068-1075); ch. VII, "Fili, habebis doctores … sed non aequali conditione, animo ardentis in pectore, sicut ego genitrix tua" and the brother "cujus modo inscia sum nominis" (l.3168-3178). P5: ch. LXXI on debts "non solum de christianis, verum etiam de judaeis" for Bernard's service "in Marchis" (l.11756-11769), where "debitores" means her creditors in context, as the drafter says; ch. LXXIII, the grave verses (l.11966-12049) and the DHVODANE acrostic (l.465-466). P6: Annals of Saint-Bertin 844, "maiestatis reus Francorum iudicio, iussu Karoli … capitalem sententiam subiit" (BERT l.2051-2053), and 850 (l.2516-2520); Bondurand's "dut peu survivre" (l.1772, 1783-1784). P7: "Ad istum tamen semper recurre libellum. Vale et vige, nobilis puer, semper in Christo" (l.12483-12484).

**Card.** `otherNames` (l.12596-12602, 285-286), `place`, `role`, `keyWorks` 1 and 3, `legacy.traces` 2 and 3, `legacy.remembered` 1 and 2, and `uncertain` 1, 3, 4 and 6 match their lines. Mabillon and Baluze (l.293-298), the Histoire littéraire (l.348-352), "De tous les écrits dûs à des femmes nées sur le sol de la France" (l.1854-1856), McHugh and Callan (TRENT l.820-831), the 842/843 argument (l.1446-1474, 13244-13271) and the Charlemagne note (l.13160-13220) were all checked.

**Absence check.** "Outside her book, no source of her own time used here names her" holds. The search finds her besides Bondurand only in the Bollandists' note (ASM6 l.33161, which separates Dodana from an Aldana), in the 1923 Catechism, in index entries in Peeters (l.42968, 58428, 59884), and in an eighteenth-century note in Migne's PL 115 (l.112830-112845, see D-M13). None is of her time. The Cluny charters' "Dodane" (l.14986 and others) are other women.

**Census check** (`carolingian-reform-christianity`, 751 to 888, Francia). The tradition and the year 841 fit. The brief agrees with the census `why` and `voices`. It rightly does not follow the census story where the held text differs (see D-M13).

#### Findings

- **D-B1 BLOCKING (brief P4 and audio; item 4; a thesis-opening sentence that is classification narration).** "Dhuoda taught in writing, for her sons." The sentence carries no fact the next sentence does not give. Its odd comma reads as a label written to meet the women's rule ("WHO if she founded, taught or led", Decision-Log l.1890-1893; the drafter's notes say as much). The Pattern's checklist fails "a paragraph that opens on a thesis" and status-announcement register. Fix: delete the sentence. P4 then opens "Her book teaches William to love and seek God…", which shows the teaching itself.

- **D-B2 BLOCKING (brief P5 and audio; items 1, 4; a rendered Latin passage drops a condition).** "She told William to pray often that God would give his father peace with all, if it could be, and bring him to heaven." Ch. LVII has two conditions: "pacem et concordiam, si fieri potest, cum omnibus" and "cum fructu poenitentiae et elemosinarum largitate, ad regnum, si jubet, faciat pervenire supernum" (DHU l.10106-10112). Bondurand's French keeps both ("s'il est possible"; "grâce aux fruits de sa pénitence", l.10096-10101). The brief keeps the first and drops "si jubet", so a hope that rests on God's will is told as a plain request. Fix: "…peace with all, if it could be, and, if God willed, bring him to heaven." (+3 words; carried in the scratch copy.)

- **D-M1 MINOR (brief P1; items 4, 9; a vague "it" and two names for one passage).** "Édouard Bondurand, her editor in 1887, dates it from her closing lines." "It" could mean the day or the book. The card calls the same passage "her closing lines" in `dates` and "Its closing note" in `uncertain` 6. "Closing lines" also clashes with P7, where her last words are a different passage (l.12483-12484). Bondurand reckons the year from the subscription (l.13222-13230). Fix: "Édouard Bondurand, who edited the book in 1887, reckons the year from its closing note." In card `dates`, use "from its closing note" as well.

- **D-M2 MINOR (brief P2; item 4; a name a listener will not know).** "Léopold Delisle, quoted by Bondurand, names him as Bernard, duke of Septimania." Delisle is not placed, and "quoted by Bondurand" is a sourcing step the card already carries. Bondurand gives his post: "Administrateur général de la Bibliothèque Nationale" (l.247-250). Dhuoda herself writes only "B." (l.2223, 11757). Fix: "Léopold Delisle, of the national library in Paris, names him as Bernard, duke of Septimania."

- **D-M3 MINOR (brief P2; items 1, 9).** (a) "Bernard had him brought to Aquitaine by Elefant". The preface says "una cum Elefanto, praedictae civitatis episcopo, et cum caeteris fidelibus suis", that is, together with the bishop and Bernard's other men (l.2256-2259). "By" comes only from the Gallia Christiana note Bondurand prints ("Elephanti episcopi ministerio", l.2288-2293), while the sentence hangs on "Her preface says". (b) "her lord's orders" brings in a third name for Bernard after "William's father" and "Bernard". A listener may hear the lord as someone else. Fix: "…brought to Aquitaine with Elefant, bishop of Uzès, while Bernard's orders kept her at Uzès."

- **D-M4 MINOR (brief P6; item 4; an event with no place).** "In 850 William took two counts by a trick…". The listener is not told where, or that this is a revolt far from Charles's court. The annal gives the place: "in marca Hispanica Aledramnum et Isembardum comites dolo capit" (BERT l.2516-2517). Fix: "In 850 William took two counts by a trick in the Spanish March, was taken by a craftier one, and was killed at Barcelona."

- **D-M5 MINOR (card `keyWorks` 1; item 8; namesakes on one card).** "quotations from Prudentius and Donatus". The card's `sources` list "Prudentius of Troyes" as author of the Annals. The Prudentius of the Handbook is the poet: Bondurand found the lines "dans Prudence (Cathemerinon Liber, ix…)" (l.1168-1171). Fix: "quotations from the poet Prudentius and from Donatus".

- **D-M6 MINOR (card `uncertain` 5; items 4, 7, 8).** (a) It opens "A daughter of Charlemagne?". That is a question in participant text, where every other label is a plain phrase. (b) "the late emperor Louis" is not placed. Bondurand's note says Louis succeeded "son père Charlemagne" (l.2237). (c) The record's contested claim names Émile Mabille on the open side, but the card does not. Delisle: "elle n'a pas été absolument abandonnée par M. Mabille" (l.13199-13201). Fix: "Whether she was Charlemagne's daughter. The Paris copy has Dhuoda call the late emperor Louis, Charlemagne's son, her brother, and some writers made her Charlemagne's daughter. Baluze, Dom Vaissete and Dom Rivet rejected this. Léopold Delisle notes that Émile Mabille had not wholly given it up. The Nîmes fragment reads the late emperor Louis instead, and Delisle says the idea must be given up."

- **D-M7 MINOR (card `legacy.traces` 1; item 1).** "One is a Carolingian fragment". Bondurand describes fragments of a Carolingian manuscript, 32 leaves, which "ne représentent malheureusement qu'une faible partie du texte total" (l.208-213, 228-238). "Two manuscripts carry the book" overstates what the Nîmes leaves carry. Fix: "Two manuscripts survive, Bondurand says. One is thirty-two leaves of a Carolingian copy, a small part of the text, found in the papers of E. Germer-Durand, which the library of Nîmes bought in 1885."

- **D-M8 MINOR (card `keyWorks` 2; item 1; a witness detached in a split sentence).** "Léopold Delisle found that the first letters of the opening verses spell… The first letters of chapter 69 spell…". Delisle found the first acrostic (l.429-432). The chapter 69 acrostic is Bondurand's own reading from the Nîmes copy (l.434-438, 448-450), but the card leaves it under Delisle. Fix: "Édouard Bondurand found, from the Nîmes copy, that the first letters of chapter 69 spell, in Latin, verses to William her son."

- **D-M9 MINOR (card `uncertain` 7; items 1, 5).** "Bondurand gives a later chronicle's story". Bondurand names the source: "La vieille chronique d'Odon Héribert" (l.1804-1805). Fix: "Bondurand gives the story from the old chronicle of Odo Héribert that Charles stabbed him at Saint-Sernin in Toulouse. He says popular imagination surrounded the death with such details."

- **D-M10 MINOR (card `uncertain` 2; item 1).** "a Dodana who died before 813". Dadila's testament was written in 813 and leaves goods of his daughter "morte précédemment" (l.618-627). She may have died in 813. Fix: "a Dodana dead by 813".

- **D-M11 MINOR (card `legacy.remembered` 3; item 4).** "the introduction to their 1923 English Roman Catechism" is unclear. Fix: "the introduction to their 1923 English translation of the Roman Catechism".

- **D-M12 MINOR (card `dates`, both cards).** The last sentence lacks its full stop ("…birth or death" in both cards). Fix: add the full stop.

- **D-M13 MINOR (process; notes and Open-Gaps; a census difference stated too strongly).** The drafter's notes list the census story's "William rebelled to avenge him" as differing from the held text, since Bondurand gives the wish for vengeance to the younger Bernard (l.1840-1843). But a held note does give it to William. Migne's PL 115 prints, under 844, the editor's note "Willelmus patris mortem ulturus, Pippini auxilio Tolosam intercepit" (eulogius-cordoba…pl115 l.112838-112845, marked "Boug."). It is an eighteenth-century editor's note and not a source of her time, so the brief needs no change. The census correction, when it is logged, should read: the held texts differ on whose vengeance this was, and none is a source of the time. The other census differences the notes list (the dead "of both families", Gregory and Augustine, "hostage") stand. I checked l.571-574, 487-491 and 1225, and NITH l.2300-2305. These need an Open-Gaps entry against the census story, which is marked "from reference summaries; primary text not yet read".

**After the fixes** (D-B1, D-B2, D-M1 to D-M4 applied to the scratch copy): 410 words, about 2:32, FK 7.1, Flesch 75.9. That is a little over the cap, as batch 8's John Climacus was at 408. If the coordinator wants 405, drop "in the Spanish March" from D-M4 and keep the rest.

---

### Nennius (recorder, standard length; 333 words, 2:03; FK 6.5, Flesch 71.2)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (N-B2, N-M3) |
| 2 | Quotes verbatim | PASS (all eight quoted strings match Giles's text) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (N-B1, N-M2, N-M3, N-M5) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (none) |
| 7 | Contested claims both sides | PASS (authorship and date told with both sides, named) |
| 8 | Common names | FAIL (N-M4) |
| 9 | One term for one thing | FAIL (N-M3: Elbotus, Elvod, Elbodug) |
| 10 | Story, scene, disputes in place, length | PASS |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (N-B1, N-B3) |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | FAIL (N-M8: no list line in the census) |

**Sentences checked and found faithful.** P1: "Nennius, the lowly minister … disciple of St. Elbotus" (NEN l.42-43); the apology, "I, Nennius, disciple of St. Elbotus … all that I could find as well from the annals of the Romans as from the chronicles of the sacred fathers … and from the annals of the Scots and Saxons, and from our ancient traditions" and "like a chattering jay" (l.110-121). P2: "Here beginneth the history of the Britons, edited by Mark the anchorite, a holy bishop of that people" (l.170-171); Duchesne's "Marci anachoretae Historia Britonum (Pseudo-Nennius)" (LP1 l.52070-52071) and "l'Historia Britonum du pseudo-Nennius (ix e siècle)" (l.27343-27344); Raine, "as the pseudo-Nennius calls him" (RAINE l.1215-1216); Hugh Williams, "in some MSS. attributed to Gildas" (GILDAS l.965-968); Stevenson, "Nennius, the only other Welsh writer of this century known to us", meaning Asser's ninth century (ASSER l.4290-4291). P3: 858 and Mervin (NEN l.93-95); 976 (l.142-143); Giles's note (l.145-148); Williams ab Ithel's "The first edition of Nennius appeared in 674" and the younger compiler of the genealogies (ANN l.1207-1224). P4: Giles's note (NEN l.46-47). P5: Adam (l.150), Vortigern (l.629), Germanus (l.674), Patrick (l.1210), the genealogies (l.1321-1370), Arthur (l.1129-1145). P6: "I was indignant, that the name of my own people … should sink into oblivion … I had rather myself be the historian of the Britons than nobody" (l.66-69).

**Card.** `knownFor`, `dates`, `place`, `role`, `keyWorks`, `legacy` and `uncertain` 1, 2 and 5 match their lines. I checked the Harleian 3859 note (ANN l.377-383), the Badon borrowing (GILDAS l.3933-3937), Thanet (ASSER l.3479-3481, 15428-15430), Stokes's extracts (STOKES l.13471-13472), Geoffrey (GILDAS l.966-968), the 960 and 840 counts (ANN l.1101-1104, 1124-1130), the Oxford interpolation in Camden's text (ASSER l.749, 870-909), Ussher's eleven manuscripts (l.1736-1738), and the Jerusalem cross variant (NEN l.1172-1173).

**Census check** (`medieval-welsh-christianity`, c. 768 to 1282). The census names the book only in `sourcing`, "the Historia Brittonum (attributed to Nennius)", and its `people` list is empty. The prologue's 858 and Stevenson's ninth century fall inside the window. Giles's 755 for Elbotus and Williams ab Ithel's 674 fall before it, and both are told as their witnesses' readings, so the placing holds. See N-M8 for the missing list line.

**The card name, "Nennius (attributed)" against "Nennius".** My view is "Nennius", for four reasons from the Pattern.
1. Naming: the display name is the person's name, in English, with a place only where needed. "(attributed)" is not a form of anyone's name.
2. Confidence: the five levels "are not shown as labels on the card". "(attributed)" works as a confidence label (the records tag the authorship Contested) placed in the most visible field. It would also show on tree pages and Who lists.
3. Ids: an id is made "from the display name". The id is `nennius`, which matches "Nennius" and does not match "Nennius (attributed)".
4. The doubt is in the wrong place. The held texts do not doubt that the prologue's writer calls himself Nennius. What is disputed is whether that Nennius wrote or edited the Historia, against Mark the anchorite and the pseudo-Nennius label. "Nennius (attributed)" reads as if the name itself were attributed.

The batch has a precedent: era 3's `joshua-the-stylite`, whose name rests on one copyist's note and whose Chronicle Nau gives to a pseudo-Dionysius, is named "Joshua the Stylite", with the doubt in `knownFor` and `uncertain`. The card already says it plainly in both places ("Named in its own prologue and apology as the writer…"; "Its author is disputed."), and the brief says it in P2. That meets the coordinator's ruling that the attribution be tagged and said plainly. "(attributed)" should stay where it is accurate, as the `author` of the work in `sources.ownWords`.

The other options:
- Keep "Nennius (attributed)". This is the most cautious choice, but it breaks the id rule and puts a label in the name.
- Use "Nennius, disciple of Elbotus". This is the prologue's own self-description, but it is long, and it repeats `role`.

#### Findings

- **N-B1 BLOCKING (card `uncertain` 4; items 4, 12; process narration in participant text).** "Arthur. The brief tells only this book's account." A participant card must not talk about "the brief". Batch 8 A-B2 is the same fault (a card talking about a Library file header). Fix: delete "The brief tells only this book's account." The item then opens "Arthur. Giles's text gives nine hundred and forty killed by Arthur's hand at Badon."

- **N-B2 BLOCKING (card `uncertain` 6; item 1; a claim no held line makes, under a wrong label).** "His name. W. H. Stevenson, who edited Asser, is a different man from Joseph Stevenson, whose edition of Nennius Giles cites." Giles's note says only "according to Stevenson's new edition", with no first name (NEN l.145). The record's witness, ASSER l.1264-1268, names Joseph Stevenson as an Asser translator of 1854, not as an editor of Nennius. Hugh Williams names Joseph Stevenson as editor of Gildas in 1838 (GILDAS l.22549-22550). I searched every held file that names Stevenson within four lines of "Nenni-" and found no line that makes Joseph Stevenson the editor Giles means. The label "His name" is also wrong, since the item is not about Nennius's name. Joseph Stevenson appears nowhere else on the card, so the item disambiguates something the reader never sees. Fix: delete `uncertain` 6, and drop the Joseph Stevenson half of the last records claim.

- **N-B3 BLOCKING (card `otherNames`; items 12, 1; a scholars' label given as another name of the person).** `otherNames: ["pseudo-Nennius"]`. The Pattern allows the census `informalName` and original-language forms a vendored source spells (Naming, "Other forms on the card"). "Pseudo-Nennius" is neither. It is Duchesne's and Raine's name for a writer they take not to be Nennius (LP1 l.27344; RAINE l.1216). Listing it as one of Nennius's names says the opposite of what they mean. It already appears, correctly, in `dates`, `remembered` 1 and `uncertain` 1. Fix: remove `otherNames`. A missing field is absent.

- **N-M1 MINOR (card `name`; Naming).** Change "Nennius (attributed)" to "Nennius", for the reasons above. This is the coordinator's call, since the assignment gave the name. Leave `sources.ownWords[0].author` as "Nennius (attributed)".

- **N-M2 MINOR (brief P2 and audio; item 4; five scholars named without context, and an undefined term).** P2 names Duchesne, Raine, Hugh Williams, Stevenson and Gildas in four sentences. None is placed, and "pseudo-Nennius" is not explained. Each can be placed from his own title page: Duchesne edited the Liber pontificalis, the early lives of the popes; Hugh Williams edited Gildas; Stevenson edited Asser's Life of King Alfred. Gildas is the older writer: "The author of the book of Nennius, who lived at a later period" (ANN l.1101). Raine can stay on the card (`uncertain` 1, `remembered` 1) to keep the length. Fix (replace from "Louis Duchesne" to the end of P2): "Louis Duchesne, editor of the early lives of the popes, lists a Vatican copy that gives it to Mark. He calls the writer pseudo-Nennius, that is, someone who is not really Nennius. Hugh Williams, editor of Gildas, notes that some copies give the book to that older British writer. W. H. Stevenson, editor of Asser's Life of King Alfred, calls Nennius a Welsh writer of the ninth century." Stevenson still carries the side that holds for Nennius.

- **N-M3 MINOR (brief P4 and card `uncertain` 3; items 1, 4, 9; a statement with no stated point, three spellings, and an editor's year given as the annals').** P4 sets Giles's Elvod of 755 beside the annals' Elbodug of 768 and does not say how they relate. No held line says Giles's Elvod and the annals' Elbodug are one man: Giles cites no annal, and Williams ab Ithel's index links Elbodug only to Elbod of Gwynedd (ANN l.13654-13656). The annal also gives no year AD, only "CCCXXIV. Annus" (l.2984); 768 is the editor's margin (l.2962). Fix: in the brief, keep only Giles's sentence and say it plainly: "Giles makes Elbotus the Elvod who was bishop of Bangor in 755 and first brought a new way of fixing Easter into the Welsh church." In card `uncertain` 3, change "put the change of Easter among the Britons in 768" to "put the change of Easter among the Britons in the year their editor reckons as 768". The card already keeps the Elbodug and Elbodg entries side by side with their witnesses.

- **N-M4 MINOR (brief P5; card `knownFor`, `keyWorks`; item 8; a common name without its place).** "the bishop Germanus" appears at first mention in both texts. The name is shared by several bishops. A held source gives the place for this one: "Germanus (Garmon) of Auxerre" (GILDAS l.19277), the Gallic bishop who visited Britain with Lupus in 429 (l.1643-1646). Stokes's Patrick dossier also places Patrick's Germanus at Auxerre (STOKES l.9490-9512). Fix: "the bishop Germanus of Auxerre" at first mention in the brief and in `knownFor`. The later mentions on the card can stay "Germanus".

- **N-M5 MINOR (brief P5; item 4; a name with no context).** "through Vortigern". The book's own line places him: "Vortigern then reigned in Britain" (NEN l.629). Fix: "through the British king Vortigern, Saint Patrick and the bishop Germanus of Auxerre."

- **N-M6 MINOR (records; formation_confidence).** Williams ab Ithel's 674 is tagged Dominant Modern Reconstruction. It is one 1860 editor's reading of one Vatican line, and the records themselves list it as one side of the contested date. Fix: tag it Contested, so it matches the `contested_claims` entry.

- **N-M7 MINOR (card `sources.about`, Annales Cambriae).** `language: "Latin"`. The card's points from this file (674, Harleian 3859, 960 and 840) come from Williams ab Ithel's English preface. Fix: "Latin, with an English preface".

- **N-M8 MINOR (process; item 14; no list line to keep).** The census `medieval-welsh-christianity` has an empty `people` list, so Nennius has no list line, and the Pattern says a Who keeps one. Fix: the coordinator logs this in Open-Gaps. The census needs a `people` row for Nennius, written as a list line from the census and the held file ("attributed" belongs in that line).

**After the fixes** (N-M2, N-M3, N-M4, N-M5 applied to the scratch copy): 339 words, about 2:06, FK 6.8, Flesch 69.2.

---

**Totals for part D.** Dhuoda: 2 blocking, 13 minor. Nennius: 3 blocking, 8 minor.
