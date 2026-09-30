# Doc_02 — Source Ecology: The Society of Jesus

**Status:** Draft. Not reviewed. Not approved to proceed. Not frozen.
**Companion document:** `Source_Registry.md` (the per-source ledger; "row N" below means a Registry row). Gaps and requests are in `Open_Gaps_Tracking.md`.
**Governed by:** Construction Framework V7.4 Part II and Step 2. Constitution V2.3, Article 17 (the five confidence levels), Article 20 (source asymmetry and marginalized voices) and Article 26 (Author Gravity). `Source_Registry_Template.md` V1.0. Forces Framework Step 2.
**Forces Framework integration:** Step 2. The forces lens is applied in §6.
**Grounded in:** `Doc_01_World_Identification_Boundaries_Orientation.md` (1540–1650; strand-singular as a recommendation pending the project lead). This document does not reopen Doc_01.

Confidence terms follow Article 17. Quotations are matched to the vendored files. Whitespace and line-break hyphens are normalised, and long s is read as s. No other letter is corrected. Every Latin quotation is checked against the scan text only. No page image was available.

---

## 1. Primary Sources

Eighty-seven works are vendored and assigned to this world (`cic/corpus-map/the-society-of-jesus.yaml`). They come to about 106.10 million characters in all. Every figure in this document is counted in a UTF-8 locale (`LC_ALL=C.UTF-8`). There two counts agree: the sum of the decoded length of each file, and `cat` of the 87 files piped to `wc -m`, both give 106,104,896. A count of words by whitespace gives 15,791,624 by both methods. In the C locale the same commands give 106,884,350, which is the byte count, and 15,674,468 words. The word count is lower there because `wc -w` in that locale does not count a token made only of non-ASCII characters, and the files hold 117,156 such tokens. Step 0 describes the first nineteen of these works. They come to 23,171,710 characters and 3,397,128 words in the UTF-8 locale, and to 3,370,893 words in the C locale. Step 0 gives 3,370,675 words for them. That figure is a C-locale count made before the seven Latin file headers were rewritten. The C-locale count of those nineteen files as they stood before that rewrite is 3,370,743, which is 68 words above Step 0's figure. Those 68 words are not traced.

- **By role in the corpus map.** Eighty-two works are `tradition` role, about 98.76 million characters, or 93.1 per cent. Five are `context` role: Boero's life of Faber, the Trent decrees, Polanco's chronicle for 1555 (one copy), Ribadeneira's life of Ignatius and the second volume of the *Monumenta Xaveriana*. They come to about 7.35 million characters, or 6.9 per cent.
- **By language.** Forty-four works are Latin, many with Spanish, Italian and Portuguese documents in the languages they were written in. They come to about 82.70 million characters, or 77.9 per cent. Thirty-five are volumes of the *Jesuit Relations*, in French with Thwaites's English on the facing pages, about 17.17 million characters, or 16.2 per cent. Eight are English, about 6.23 million, or 5.9 per cent.
- **By scan quality.** Six works are second witnesses under the Library's scan-quality rule. They are the 1606 Constitutions, Nadal's 1595 *Adnotationes*, Ribadeneira's 1572 life, Trigault's 1615 Latin and Canisius's Latin of 1565 and 1573. They come to about 6.00 million characters, or 5.7 per cent. Without them, the Latin that can be quoted as primary is about 76.70 million characters, or 72.3 per cent. A Latin original counts as primary evidence when its scan is clean, and this world's Latin volumes are counted on that rule. The Library's headers state the rule.
- **By who made the edition.** About 67.93 million characters, or 64.0 per cent, are volumes of the *Monumenta Historica Societatis Jesu* or Bouix's edition of Faber. The editors and compilers named on their title pages are Jesuits (§2). The *Institutum Societatis Iesu* is the order's own collection, printed at Florence (rows 74–76). The *Jesuit Relations* are edited by Thwaites, the secretary of the State Historical Society of Wisconsin, from the missionaries' own reports (rows 90–92).

**Who speaks, and for which years.** The years are the years the text covers. The rows are Registry rows.

| Voice | What is on the shelf | Years covered | Rows |
|---|---|---|---|
| Ignatius, own letters. | Latin, Spanish, Italian and Portuguese letters, with the O'Leary English selection. | 1524 to 28 February 1548 in Tomus I, with one undated letter of February or March 1548. Then March 1548 to 29 March 1550, April 1550 to November 1551, April to November 1553 and December 1553 to 15 May 1554. Nothing from December 1551 to March 1553, or after 15 May 1554. | 9–16, 78. |
| Ignatius, *Exercises*. | Mullan's English of the autograph, and the Spanish text with the early Latin versions. | undated text; the Latin version was copied in 1541 and approved in 1548. | 1–4, 79. |
| Ignatius, *Autobiography*. | dictated 1553–55, in English, and in the original Spanish. | narrates 1491 to about 1538. | 5–8, 70, 80. |
| Faber. | *Memoriale*, Latin, and Boero's English. | mostly 1542–43, with later notes to 1546. | 17–20. |
| Xavier. | Coleridge's compilation, with two English catechetical documents, and the letters in their original languages. | 1541 to 1552. | 21–24, 85. |
| Lainez. | editors' life; letters and acts. | own letters to 1556; then 2 January 1557 to 19 January 1565, as vicar and as General from 2 July 1558. Also register copies to Salmeron: two as vicar, then fifteen as General from November 1558. | 25–26, 67, 81. |
| Borgia. | letters and documents. | 1540 to 1572; as General from 2 July 1565 to October 1572. Also 49 letters to Salmeron. | 82, 69. |
| Nadal. | editors' life; letters; commentary on the Constitutions. | letters 1546–62 (prefatory matter read only), 1562–65 and 1566–77 (title pages only); undated commentary. | 27–28, 83. |
| Polanco. | chronicle; letters to Salmeron written on the Generals' commission. | chronicle for 1550–52 and 1554–56; letters from December 1556 to 1570, and two as vicar in 1572. | 30, 73, 84. |
| Salmeron. | own letters and letters to him. | 1536–85. | 32–33, 67–69, 73. |
| Mercurian and Aquaviva. | register copies to Salmeron, Italian and Spanish. | Mercurian 1573–80 (about 88), Aquaviva 1581–84 (18 to 19). | 69. |
| The Society as a body. | the *Institutum*: bulls, the Formula, the Constitutions, the decrees of the first eight general congregations, the *Ratio Studiorum*. | 1540 to April 1646. | 74–77. |
| Broët, Le Jay, Codure, Rodrigues. | letters, and the papal papers of the Irish mission. | 1541 and after. | 87. |
| Canisius. | English catechism of 1622, from a Latin text of Canisius; the Latin of 1565 and 1573. | English of 1622; second witnesses for the Latin. | 34, 88. |
| Constitutions. | 1606 print (second witness), and the clean Latin of the *Institutum*. | 1540 to 1606. | 36, 75. |
| Nadal, *Adnotationes*. | 1595 print. | second witness. | 29. |
| Ricci. | Trigault's Latin reworking, 1615 (second witness). | the China mission; the years were not read. | 89. |
| The missionaries of New France. | the *Jesuit Relations*, volumes 1 to 35. | 1610 to 1650. | 90–92. |

**Ignatius and the first companions.**

- Ignatius has four kinds of text on the shelf. The *Exercises* are his manual for a retreat, in Mullan's English and in the Spanish original (rows 1–4, 79). The *Autobiography* is a life he dictated in his last years, in English and in the original Spanish (rows 5–8, 70, 80). His letters run from 1524 to 28 February 1548 in the first Latin volume. One undated letter of February or March 1548 follows. Four later volumes carry them to 15 May 1554, with a gap from December 1551 to March 1553. The English selection stops in 1547 (rows 9–16, 78). The first Latin volume also prints the ambassador's letter of March 1540 about sending men to India (row 15).
- Faber is a private diary in Latin, with an English rendering in Boero's Part the Second (rows 17–20).
- Xavier is on the shelf through Coleridge's compilation of his life and letters (rows 21–24), and in the original languages in the *Monumenta Xaveriana* (row 85). Coleridge also prints, in his notes, catechetical documents he attributes to Xavier (row 22).
- Lainez, Borgia, Nadal, Polanco and Salmeron are in Jesuit editions. Lainez has eight volumes of letters and acts, to 19 January 1565 (rows 25–26, 81). Borgia has three volumes, to 1572 (row 82). Nadal has four volumes of letters and writings, to 1577 (rows 27, 83). Nadal's commentary on the Constitutions is a separate work (row 28). Salmeron's two volumes also print the letters of others to him. Those include about 150 letters by Polanco, written on the Generals' commission. They include letters under the Generals' own names, and one report on the Ireland mission of 1542 (rows 67–69, 73).
- Polanco's chronicle covers 1550–52 and 1554–56 in detail (rows 30, 84). His letters to Salmeron, written on the Generals' commission, run from December 1556 and are the largest body of Roman letters on the shelf for 1556–65 (row 73).
- Broët, Le Jay, Codure and Rodrigues are in one volume, with the papal papers of the Irish mission (row 87).
- The Society speaks as a body in the *Institutum*: the bulls, the Formula, the Constitutions and the decrees of the first eight general congregations, to April 1646 (rows 74–77).
- The missions of New France speak in the *Jesuit Relations*, volumes 1 to 35, for 1610 to 1650 (rows 90–92). Ricci's China mission is on the shelf only in Trigault's reworking of 1615, a second witness (row 89).
- Canisius appears through a 1622 English catechism, and in Latin printings of 1565 and 1573 that are second witnesses (rows 34, 88).

**What is not on the shelf.** Ignatius's letters from December 1551 to March 1553 and after 15 May 1554 (row 49). Borgia's first two volumes (row 47), Polanco's chronicle for 1537–49 and 1553 (row 50), and any volume of the letters of Mercurian or Aquaviva (no row). The *Jesuit Relations* from volume 36 (row 42). Ricci's own text, and any text by de Nobili (rows 51, 52). The documents of the rites controversy (row 53). The *litterae annuae* as a series (row 44).

## 2. Author Gravity Assessment

Five dimensions: Visibility, Representativeness, Influence, Limitations, Transmission History.

**Ignatius of Loyola (1491–1556).**
- *Visibility:* The most visible voice. He is the founder, and four kinds of his writing are on the shelf. Everything the Society says of itself in its first years is measured against him.
- *Representativeness:* The *Exercises* speak for a formation that every Jesuit passed through. Letters X and XX speak for the Society's early ministry (rows 10, 12). The *Autobiography* speaks for one man's account of his own conversion. Nothing on the shelf shows what an ordinary Jesuit in a school or a mission made of the *Exercises* in daily practice.
- *Influence:* Central. Nadal's commentary, Faber's diary and Xavier's letters all assume the *Exercises* and the Constitutions (rows 27, 28, 18, 23).
- *Limitations:* Two of his four kinds of text look back. The *Autobiography* was dictated in 1553–55 about events of 1521–38 (rows 5–7). The Writer says he adhered so closely to Ignatius's words that afterwards he could not explain the meaning of some of them. The *Exercises* are a manual, and Rule 13 is a rule for the exercitant. It tells us how Ignatius wanted men to hold to the Church. It does not tell us how the Society held to it under pressure from Popes (row 1, Doc_01 §2).
- *Transmission History:* The *Exercises* reach us through Mullan's English of the Spanish autograph (1914). Mullan says the Latin version was "formally approved by the Holy See in 1548" (row 4). The *Autobiography* has four stages. Ignatius spoke. Gonçalves da Câmara took notes, and part of them he dictated in Latin at Genoa in December 1555. Codretto made a Latin translation. O'Conor's English appeared in 1900 (rows 70, 71). The Editor does not say from which text the English was made. The *Exercises* also reach us in the Spanish text and the early Latin versions of 1919 (row 79), and the earliest text of the *Autobiography* is in Spanish and Italian in a volume of 1904 (row 80). The letters reach us in the MHSI edition of 1903, from the order's own archive, and in O'Leary's English selection of 1914 (rows 9, 14–16). Four later MHSI volumes carry them to 1554, and most of their letters are summaries from the registers or were written by secretaries in his name (row 78). The Regesta from 1547 are the secretary's copies (row 16). The editors' own list says that Polanco and other secretaries wrote some letters at his order (row 14). No page image was seen.

**Peter Faber (1506–46).**
- *Visibility:* One private voice, on the shelf in Latin and, in part, in English.
- *Representativeness:* He speaks for a devout, solitary and travelling first companion. The Bouix preface says that Ignatius judged no other companion better able to absorb and pass on the spirit of the *Exercises* (row 17). He does not speak for the order's governing or its schools.
- *Influence:* The editors present him as a model of the *Exercises* lived (row 17). Ignatius's view is reported at second hand, in the editor's preface.
- *Limitations:* The diary is short: mostly a year from June 1542, with later notes (row 17). It mixes Latin and Spanish. It is a private record and does not show the Society's public work.
- *Transmission History:* The autograph is lost. Bouix says "ubi terrarum hodie lateat in incerto est", that it is unknown where on earth it now lies (row 17). The Latin was printed from lithographed copies of an earlier transcript (row 17). Boero's Italian is shorter than the Latin, and Coleridge's English is condensed in many places to match it (row 20). The Bouix Preface says that Pius IX had recently allowed Faber to be called Blessed and to be honoured with the rite of the Blessed. The title page prints 1872, and the Preface is dated 8 December 1873 (row 17, lines 349–355). Boero wrote his life after the Sacred Congregation of Rites had sanctioned the veneration of Faber (row 19).

**Francis Xavier (1506–52).**
- *Visibility:* The main missionary voice on the shelf for 1541–52. Outside him there are a few pages of Polanco and one report on the Ireland visit (rows 21–24, 30, 68). After 1552 the missionary voices are those of New France and Trigault's Ricci (rows 89–92).
- *Representativeness:* He speaks for the first missions to India and Japan. He does not speak for Ricci's China, de Nobili's India, or the later missions.
- *Influence:* His letters helped draw recruits. The editors' account of Nadal says one of them moved him to enter the Society (row 27).
- *Limitations:* The letters were written for circulation, with a missionary's hopes. The census adds its own caveat: his account of Japan is a first impression, taken through an interpreter of limited education. That caveat is the census's, and it is not tested here.
- *Transmission History:* Coleridge (a Jesuit, 1872) compiled the volumes from printed and manuscript sources. His postscript to Volume II tells of a manuscript collection of letters. It was brought from the archives of the Goa college in the last century "at the time of the suppression". Philippucci had already examined and translated it (row 23, postscript at lines 163–177). Xavier's catechetical documents in Volume I reach us by way of Philippucci's Latin, the editions of Menchaca and Poussines, and Coleridge's English (rows 22, 62). Coleridge gives no source for the "Explanation of the Creed". The attribution to Xavier himself is Inferential/Thin. The *Monumenta Xaveriana* print his letters in the original Spanish, Portuguese, Italian and Latin (row 85). The census's quotation from the letter written at Kagoshima is Costelloe's English of a Spanish sentence in that volume (row 85, lines 29495–29496).

**Diego Lainez (1512–65).**
- *Visibility:* Present in four ways. His own letters to 1556 are in the first Lainez volume. His letters and acts as vicar and General, from 2 January 1557 to 19 January 1565, are in seven more volumes. He is also in register copies to Salmeron. The editors' life of him is a compact history of the order (rows 25, 26, 67, 81).
- *Representativeness:* He speaks for the early governing centre of the order, first as one of Ignatius's chief helpers, then as vicar and General. The editors themselves say that letters of his generalate were mostly written in his name by secretaries (row 26).
- *Influence:* The editors report Ignatius's own judgment that no man had done more for the Society than Lainez. In that judgment Ignatius counted the great apostle of the Indies too (row 25, lines 200–204, in Latin).
- *Limitations:* The first Lainez volume ends in 1556. Its Preface says the registers of 1556–58 were lost. Almost no letters to Spain and Portugal survive for those years (row 26). The later volumes print what survives, chiefly as register copies. Only the last volume was read at the loci named (row 81).
- *Transmission History:* The letters come from autographs and from the registers. The editors say they chose among the letters ("Delectus proinde adhibendus fuit") and did not print all (row 26). The eight volumes appeared in Madrid from 1912 to 1917 (rows 26, 81).

**Jerónimo Nadal (1507–80).**
- *Visibility:* Strong, through his editors and his commentary. His own letters were read only at the Preface of the first volume. The three later volumes were checked by title page (rows 27, 83).
- *Representativeness:* He is the order's interpreter of the Constitutions and its travelling visitor. He speaks for the order's governors. He does not speak for the men in the field.
- *Influence:* Ignatius sent him through Spain, Portugal and much of Europe to explain the Constitutions. The Second General Congregation took his scholia "pro directione tantum et sine ulla obligatione", in its own decree 42 (row 75). The editor of the scholia reports the same (rows 27, 28).
- *Limitations:* The commentary is a private work. Its editor says the congregations later settled points that Nadal left open (row 28). His Gospel commentary of 1595 is a second witness for scan quality (row 29).
- *Transmission History:* The letters are in the MHSI volumes of 1898 to 1905, and the fourth volume prints his chief writings (row 83). The scholia were printed at Prato in 1883, from manuscript notes kept in the Society's houses (row 28). The *Adnotationes* came out in 1595, fifteen years after his death (rows 27, 29). The editors' Protestatio says that all reports of miracles and revelations rest on human faith only (row 27).

**Alfonso Salmeron (1515–85).**
- *Visibility:* A single correspondent, but a large one. His two volumes hold most of the centre's letters that the shelf has for 1573–85 (rows 32, 33).
- *Representativeness:* He speaks for a theologian at Trent and, from 1558, a leader of the Naples province. The letters sent to him give the view from Rome to one province (rows 69, 73).
- *Influence:* He and Lainez spoke first at Trent as the Pope's theologians (row 32). He also went to Ingolstadt in 1549 with Le Jay and Canisius (row 32).
- *Limitations:* The volumes' contents are the business of one man. The editors omit the passages in Polanco's letters about wine, provisions and payment. They also omit most of the letters that Salmeron himself wrote in Lainez's name. He wrote them at Rome as acting vicar general, from September 1561 to May 1562 (row 32, lines 1033–1035 and 1054–1057).
- *Transmission History:* The editors say that they print everything, including the faults and errors of the order's men. They say that Boero's earlier versions of Salmeron's letters were corrected, altered and almost always cut (row 32). Both statements are the editors' own claims and were not tested. Salmeron's own commentaries came out after his death, in 1597–1602 (row 63).

**Juan Alfonso de Polanco (1517–76).**
- *Visibility:* Two bodies of writing on the shelf. One is the chronicle for 1550–52 and 1554–56. The other is about 150 letters to Salmeron, from December 1556 to 1570, printed in Salmeron's two volumes (rows 30, 73, 84).
- *Representativeness:* The secretary of Ignatius, writing the order's history from its own papers (row 30). After Ignatius died he wrote to Salmeron on the commission of the vicar and of the Generals. He speaks for the centre, and in the letters he writes in the plural voice of the office (row 73).
- *Influence:* The Lainez editors call him the first and most diligent writer of the order's annals (row 25, in Latin).
- *Limitations:* Four of the six volumes of the chronicle are vendored: Tomi 2, 4, 5 and 6. Tomus 5 is on the shelf twice. It counts sixty-one places, and the editors' note counts sixty-five (row 30). The letters go to one correspondent, in Naples. The editors leave out the passages about wine, provisions and payment (row 73).
- *Transmission History:* The chronicle was printed in Madrid from 1894 to 1898, from the manuscript volumes of his chronicle (rows 30, 84). For the letters, the Salmeron editors' footnotes cite the Society's register volumes, for example the fourth Regesta codex (row 73).

**Francis Borgia (1510–72).**
- *Visibility:* Three volumes of his letters and of documents about him, to 1572, and 49 letters to Salmeron (rows 82, 69).
- *Representativeness:* The third General. After Lainez died, the professed fathers at Rome elected him vicar general, and the congregation elected him General on 2 July 1565 (rows 33, 75). He speaks for the centre from 1565 to 1572.
- *Influence:* The volumes' title pages call him Duke of Gandia and third General (row 82). His letters to Salmeron show him settling the business of one province (row 69).
- *Limitations:* Only headings were read. The volumes print letters to him as well as by him. His letter to Salmeron of 4 March 1565 is written in the third person about the vicar, so at least some letters in his name are by secretaries (row 69).
- *Transmission History:* The three volumes were printed in Madrid from 1908 to 1911 (row 82).

**The Society as a body: the *Institutum* and the general congregations.**
- *Visibility:* Three volumes: the bulls and briefs, the Constitutions with the decrees of the first eight general congregations, and the rules with the *Ratio Studiorum* (rows 74–76). The decrees run from 1558 to 1646.
- *Representativeness:* The order's corporate voice, as its governors made it: the professed fathers in congregation, and the Generals in ordinances and instructions. It does not speak for the men in the field.
- *Influence:* The decrees bound the order. The Second Congregation's decree 42 fixed the standing of Nadal's scholia (row 75).
- *Limitations:* The text prescribes. It does not show how a house or a college lived. The headings are the editors', and the Generals' ordinances are printed together across the centuries. Only the loci named in the Registry were read.
- *Transmission History:* Printed at Florence in 1892–93 (rows 74–76).

**The missionaries of New France (the *Jesuit Relations*).**
- *Visibility:* Thirty-five volumes for 1610 to 1650. They are the only sustained mission voice on the shelf after Xavier (rows 90–92).
- *Representativeness:* They speak for Acadia, Quebec and the Huron mission. They do not speak for India, Japan, China, Brazil or Ethiopia.
- *Influence:* The census calls the Relations a core primary source (row 42). Whether they shaped the order's policy was not tested.
- *Limitations:* The census says they were written for an edifying purpose and shaped by their audience (row 42). The English is Thwaites's. The peoples of Canada appear only through the missionaries. Only a few loci were read.
- *Transmission History:* Thwaites edited the volumes at Cleveland from 1896 to 1901. He printed the French, Latin and Italian texts with his English on the facing pages (rows 90–92).

**Matteo Ricci, through Trigault.** Trigault compiled five books on the China mission from Ricci's Italian commentaries and reworked them (row 89). Ricci's own text is not on the shelf, and the scan of Trigault's Latin is a second witness. This document does not quote it.

**Broët, Le Jay, Codure and Rodrigues.** Their letters, with the papal briefs for the Irish mission, are in one volume of 1903 (row 87). Only the brief to Broët and Salmeron was read.

**Peter Canisius.** His catechism reaches us in an English translation of 1622, by an unnamed translator, from a Latin text (row 34). The scan is badly damaged. The census says his catechisms shaped Catholic teaching across German-speaking Europe. His Latin *Summa* of 1565 and 1573 is on the shelf as second witnesses (row 88).

**Pedro de Ribadeneira.** His Latin life of Ignatius (Naples, 1572) is held at second-witness status (row 31). The corpus map calls him someone who knew Ignatius personally. The life is not read here.

**The Jesuit editors and translators.** Mullan, O'Conor, Goodier, Coleridge, Boero, Bouix and the fathers of the *Monumenta Historica Societatis Jesu* are all members of the Society, on their title pages. The files do not say whether O'Leary, who translated the letters, was a Jesuit, and the Canisius translator is unnamed. Their editions are careful, and some of their prefaces state their policies openly (rows 26, 32). Every edition is also an act of self-presentation by the order. The Bouix preface, the Boero life and the Nadal Protestatio show a devotional and hagiographic frame (rows 17, 19, 27). Coleridge's Xavier volumes give a Jesuit's reading of Xavier for English Catholics (rows 21–24). No editor outside the Society is on the shelf for any of the Society's own texts. This document treats that as a structural fact about the shelf and not as a fault in any one editor.

## 3. Secondary Scholarship Assessment

The secondary matter on the shelf is by Jesuits, except Thwaites's introductions to the *Jesuit Relations*. It was written between 1872 and 1917. It is the editors' prefaces, Coleridge's narrative and Boero's life. No modern specialist work is vendored. O'Malley (1993), Schurhammer (1973–82) and the *Cambridge History* chapters are named in the census and are not vendored (rows 54–56). Claims below rest on the editors' prefaces and are marked accordingly.

**1. Why was the Society founded? Contested.** Step 0 (§2 A3) places the order inside the Reformation crisis as a response to it. The shelf's own account is different. Coleridge, a Jesuit, reports an address of the companions in 1537. They could not go to Palestine as they had vowed. In Italy they found "how vast a field" for their apostolic labours (row 21). The Lainez editors say Lainez was freed from "voto Hierosolymas adeundi", the vow to go to Jerusalem (row 25, in Latin). The census's note on O'Malley says that book was written "to counter mythologized readings of the order's founding" (row 54). Both readings are carried. The vow to go to Jerusalem is Widely Accepted. The address itself is at three removes, and is Inferential/Thin.

**2. What was the bull's day? Documented as 27 September.** The bull's own dating clause reads "quinto kal. Octobris", the fifth day before the Kalends of October, and the *Institutum*'s index gives "27 Sept. 1540" (row 74). The Lainez editors give "27 Septembris anni 1540", and Coleridge's contents page reads "Sept 27, 1540" (rows 21, 25). Only Coleridge's text reads "Sept. 17", in the sentence that also names "the Feast of SS. Cosmas and Damian" (row 21, lines 4822–4823). Nothing on this world's shelf gives the day of that feast. The bull's day and year are both Documented, and Coleridge's "Sept. 17" is the one reading that differs.

**3. When was Ignatius elected General? Not settled.** Coleridge dates the ballots 4–5 April 1541 and Ignatius's entry on duty 19 April. The O'Leary table says 13 April (rows 9, 21). April is Documented and the day is carried open.

**4. How far did Nadal's commentary bind? Documented.** The Second General Congregation took Nadal's scholia "pro directione tantum et sine ulla obligatione", in its own decree 42 (row 75). The editor of the scholia reports the same (row 28). Nadal's private view was not the Society's law.

**5. The Chinese and Malabar Rites. No document of the controversy is on the shelf.** Step 0 dates its events to 1623, 1627–28 and 1645. No source on the shelf confirms any of these dates, so each is Inferential/Thin. Their only basis is Step 0 §2 A3 and the source dossier, and neither names a source (rows 51–53). Trigault's account of Ricci's mission (row 89) may bear on Ricci's method. It is a second witness and was not read for that question.

**6. Jesuits in other worlds' files.** Sarpi's history of Trent names Lainez and Salmeron, and the Roman Breviary names Xavier and Borgia. Both are assigned to the Tridentine Church. The matches were counted and not read. Neither file is used here (Open_Gaps, section E).

## 4. Formation Narrative Sources

- **The *Autobiography*.** A first-person life, given by Ignatius to a scribe over two years, in his last years (rows 5–8, 70). It gives the story of a conversion and a formation. Tier 1 in the Framework's four-tier scheme, for what Ignatius reported of himself. That means Documented to Widely Accepted at the narrative level, with the mediation named in §2. The scribe's or editor's plural voice at line 484 is Tier 3 (attributed tradition). It is a hagiographic comment on Ignatius's chastity. The visions in Chapter III are Tier 3 for their content and Tier 1 as what Ignatius said he saw.
- **Faber's *Memoriale*.** A private diary of an interior life (rows 17, 18). Tier 1 for what Faber wrote of himself. Boero's frame is Tier 3.
- **Ribadeneira's life of Ignatius.** A close disciple's life (row 31). Not read. Held at second-witness status. Tier 3 by genre, if used.
- **Coleridge's *Life and Letters of St. Francis Xavier*.** A compiler's narrative with the letters set in it (rows 21–24). Tier 1 where the letters speak. Tier 3 in Coleridge's account of visions and miracles, which this document does not use.
- **Boero's life of Faber.** A beatification-era life (row 19). Tier 3. It quotes the circular letter of 7 August 1546 on Faber's death. That letter is Tier 1 for the fact of the death (row 19).
- **Polanco's chronicle.** A secretary's history from the order's papers (rows 30, 84). Tier 1 for the years 1555 and 1556, and for the other years it holds, with the editors' corrections.
- **The *Jesuit Relations*.** The missionaries' annual reports from New France, printed for readers in France (rows 90–92). Tier 1 for what the missionary reports of his own work and of his instructions, such as the instruction of 1637 for the fathers sent to the Hurons. Tier 3 for accounts of the deaths and visions of others, which this document does not use.
- **The stories the census names.** The census's Tier 1 story "Xavier Writes from Kagoshima" says of itself: "from reference summaries; primary text not yet read". The shelf has the letter in Coleridge's English (row 23) and in the original Spanish (row 85), and this document has read both at the loci named. The census's quoted wording is not in Coleridge's translation (row 43). It is Costelloe's English of the Spanish at row 85, lines 29495–29496, so the story can be told from the Spanish.

## 5. Material Culture and Daily Life Sources

- **Vendored:** no archaeology, no building record, no object. The census's "experience today" is the Church of the Gesù in Rome. The shelf has nothing on it.
- **Prescribed practice in the texts.** The *Exercises* fix the posture of the retreatant: "now on my knees, now prostrate on the earth, now lying face upwards, now seated, now standing" (row 2). Ignatius's letter to Magdalena de Loyola sends her "twelve beads, with many blessings attached to them" (row 13). These are instructions and gifts, not records of use.
- **Institutional lists.** The editors' note to Polanco lists sixty-five residences of the Society at the start of 1555 (row 30). The Autobiography's appendix lists early colleges (row 8). They give scale and are not material evidence.
- **Social background** comes through Xavier's letter on the Japanese: their honour, poverty and reading (row 23), and through the Autobiography's hospitals and prisons (rows 5, 7). All of it is a Jesuit's view.
- **The 1595 book.** Nadal's *Adnotationes* is a printed book. This pass did not test whether the printed book carried engravings, and the scan is text only (row 29).
- **Surrounding religious environment.** Protestants appear as opponents and as the audience Ignatius told his men not to argue with (row 12). Non-Christian religions appear only in Xavier's letter on Japan and in Coleridge's summaries (rows 22, 23). No Buddhist, Hindu, Confucian or Jewish voice is on the shelf.
- **The gap is stated, not filled.** The daily life of a college, a mission station, a lay confraternity or a Jesuit house cannot be reconstructed from what is vendored.

## 6. Source Asymmetries and Missing Voices

Under Article 20 the primary duty is to name whose voices the sources structurally omit, and why.

**Overrepresented:** Ignatius and the first generation; the order's Roman centre; Iberian and Italian Jesuits; Jesuit editors of the years 1872–1917.

**Structurally missing, and why:**

- **Ordinary Jesuits.** The brothers and coadjutors appear rarely and as helpers, for example Brother Christopher López, Ribadeneira's companion and librarian (row 32). Residences appear in lists (rows 8, 30). No brother, novice or teacher speaks of daily life.
- **Women.** Ignatius writes to women (rows 13, 37). The Lainez editors say Margaret of Austria had been Lainez's penitent at Rome (row 25). The Salmeron editors name two noblewomen among the correspondents of that volume, Portia Carafa, countess of Ruvo, and Maria Sanseverino, countess of Nola. The editors list them among the authors of letters written to Ignatius, Lainez, Borgia or Salmeron, so they wrote (row 33, lines 238–262). Women appear as patrons and correspondents. None speaks as a member of the order.
- **The laity.** The confraternity at Azpeitia, the poor in the hospitals and the children in catechism appear only as objects of the Society's work (rows 10, 12, 22).
- **The peoples of the missions.** No Japanese, Indian, Chinese, Ethiopian, Brazilian, Irish, Huron or Algonquin voice is on the shelf. The Japanese appear through Xavier (rows 23, 85). The Irish appear through the missionaries' report on their visit (row 68). The Ethiopians appear through Polanco's note on the consistory and the patriarchate (row 30). The peoples of New France appear only through the missionaries (rows 90–92). The census names Ricci for China and de Nobili for India. Ricci is on the shelf only in Trigault's second witness (row 89), and de Nobili is not on it (row 52).
- **The opponents.** No Protestant, Dominican, inquisitor or colonial official speaks in his own words. They appear as the Society's editors describe them (rows 7, 24, 25, 27).
- **The Society's own critics inside the order.** The editors say that quarrels ambitious men stirred up in 1556–58 were the worst of the order's troubles (row 25). No voice of those men is on the shelf.

**The Jesuit voice gap, stated plainly.**

1. **Ignatius, to 1554.** His own letters run to 28 February 1548 in the first Latin volume, with one undated letter of February or March (row 16). Four later volumes carry them from March 1548 to 15 May 1554, chiefly as summaries from the registers or as secretaries wrote them. They leave a gap from December 1551 to March 1553 (row 78). Nothing under his name is on the shelf after 15 May 1554, and he died on 31 July 1556 (row 75).
2. **1556 to 1565.** The order's centre speaks through its registers. Lainez's letters and acts run in eight volumes to 19 January 1565. The editors say that those of his vicariate and generalate were mostly written in his name by secretaries (rows 26, 81). Polanco's chronicle covers 1556 (row 84). Salmeron's first volume prints about 150 letters from Polanco to Salmeron, written on the commission of the vicar and of the Generals. Of the 146 read in full, 112 fall in 1556–61 (row 73). It also prints 2 letters from Lainez as vicar and 15 from Lainez as General (row 67). Nadal's letters run through the period (rows 27, 83). The decrees of the first two general congregations speak for the professed fathers (row 75). Salmeron writes throughout.
3. **1565 to 1585.** Borgia's letters as General run to 1572 (row 82). Nadal's letters run to 1577 (row 83). Mercurian and Aquaviva speak only as senders of register copies to one correspondent, Salmeron, in Naples: about 88 letters headed Mercurian, from 1573 to 1580, and 18 to 19 headed Aquaviva, from 1581 to 1584 (row 69). The decrees of the third and fourth congregations, and Aquaviva's instruction to superiors, whose date this pass did not read, speak for the order as a body (rows 75, 76). Salmeron's second volume also has 49 letters headed Borgia, 7 as vicar general in 1565 and 42 as General, to March 1571, and 12 more headed Polanco on commission, to 1570 (rows 69, 73). Nothing vendored is a volume of Mercurian's or Aquaviva's own correspondence. Salmeron's two volumes run to February 1585 (rows 32, 33). Step 0 §4 item 5 states the same count.
4. **After 1585.** Apart from the Generals' ordinances and instructions in the *Institutum*, whose dates this pass did not read (row 76), no letter, chronicle or life of the order's centre composed after February 1585 is vendored. The window runs to 1650, so 65 of its 110 years fall after that date. Three kinds of text cover them. The decrees of the fifth to eighth general congregations (1593–94, 1608, 1615–16 and 1645–46) and the *Ratio Studiorum* speak for the order as a body (rows 75, 76). Trigault's reworking of Ricci appeared in 1615, and it is a second witness (row 89). The *Jesuit Relations* give New France from 1610 to 1650 (rows 90–92). The later printings of earlier texts are the *Adnotationes* (1595), the Constitutions (1606) and Canisius in English (1622) (rows 29, 34, 36). The first two are second witnesses.
5. **The missions.** For 1541–52 the missionary voice is Xavier's, in English and in the original languages, with one report on the Ireland visit (1542), the papal briefs for it, and a few pages of Polanco (rows 21–24, 30, 68, 84, 85, 87). After 1552 the only sustained missionary voice is New France, from 1610 to 1650 (rows 90–92). This pass read the *Jesuit Relations* only at the loci named in the Registry. It found no missionary's own voice from India, Japan, Brazil or Ethiopia after Xavier's death, other than Polanco's notes for 1554–56 (rows 30, 84). No text of de Nobili is on the shelf, and Ricci is there only as Trigault's second witness (rows 52, 89). The documents of the rites controversy were not found (row 53).
6. **What this means for the world.** A Representative built on this shelf would have a full voice for 1540–1565 and the order's decrees to 1646. For the letters of the centre it would have a thinner voice for 1565–1585 and none after 1585. For the missions it would have Xavier to 1552 and New France from 1610 to 1650. For India, Japan and China it would have Xavier and Trigault's second witness only. Doc_02 does not fill the gap from the census or from memory.

**Forces lens (Forces Framework Step 2).** The forces are those in Doc_01 §6. Externally they are the Reformation and the Council of Trent, papal control of the order, suspicion and inquiry, colonial officials, and the controversy over the rites. Internally they are the quarrels of 1556–58 and, later, the dispute over accommodation inside the order.

*Which sources speak to external forces.*
- The Council: Ignatius's instruction for the road to Trent (row 12); Lainez's and Salmeron's roles there, in the editors' lives (rows 25, 32); the Trent decrees themselves (row 35).
- Papal control of the order. Paul IV's imposed choir and term, and Lainez's work to remove them, are in the Lainez preface (row 25). Pius V's decree on ordination, and Salmeron's advice, are in the Salmeron preface (row 33). Nadal's plea to Gregory XIII is in the Nadal preface (row 27). Polanco's letters to Salmeron run through the years of the Pauline decrees and of the quarrels of 1556–58 (row 73). They were counted and not read for this question, so they are named here as a source for Doc_08.
- Suspicion and inquiry: the *Autobiography* on Alcalá, Salamanca and Rome (row 7); the attack on the *Exercises* in 1554 (row 27).
- Colonial officials: Xavier and Don Alvaro (row 24), the ambassador's letter of 1540 (row 15).
- The rites: no source (row 53).

*What the silences show.* The papal documents on the shelf are the bulls and briefs of the *Institutum*, with the Formula of the Institute (row 74), and Paul III's briefs for the Irish mission (row 87). The index of the *Institutum* lists no bull of Paul IV, so his decrees on choir and term, which the Lainez preface reports (row 25), are not printed there. No Protestant, Dominican or inquisitorial text is on the shelf, so the pressure appears only through the Society's own account of it. The forces that shaped the order most, the Reformation and the Roman curia, are heard only from inside the order. No source has economic conditions as its subject. Whether the vendored books treat the funding of colleges beyond passing mentions was not read in this pass.

*Survivorship patterns.*
- The order kept its own archive, and its own Jesuit fathers edited it in the years around 1900 (rows 14, 16, 25). What survives is what the archive kept. Register volumes for 1556–58 are lost (row 26), and the sixth of the Ignatian registers, for Spain, Portugal and India in 1556, seems lost (row 16).
- The editors chose. The Lainez editors say they selected among letters (row 26). The Salmeron editors omit the passages in Polanco's letters about wine, provisions and payment. They also omit most of the letters Salmeron wrote in Lainez's name as his deputy at Rome. They say they omit nothing that would stain the order's history (row 32). That statement is a claim of the editors and was not tested.
- Faber's autograph is lost (row 17). A collection of Xavier's manuscript letters was brought out of the archives of the Goa college at the suppression (row 23).
- The pressure that shows most is therefore papal and internal, because the order's archive kept the letters about it. This is an effect of what survives. It is not a finding that Rome was the most threatening force.

**Evidential visibility is not ecological visibility.** The world's most formative work was likely the *Exercises* given one to one, the classroom, the confessional and the mission station. The shelf's evidence is the founder's writing, the Generals' registers and decrees, Xavier's letters and the missionaries' printed reports from New France. Reconstruction that reaches past the evidence is marked Inferential/Thin. A bounded reconstruction of any marginalised voice needs a specific textual trace and is not attempted here.

## 7. Required Disclosure

**1. The Constitutions and Nadal's *Adnotationes* are not primary-quotable (Step 0 §4 item 1, binding).** Both are vendored and both are second witnesses for scan quality. Doc_02 does not quote either. It cites the Constitutions only for the structure of the front matter (row 36) and the *Adnotationes* only for its genre (row 29). Ribadeneira's life (row 31), Trigault's Latin (row 89) and Canisius's Latin (row 88) are held the same way. The *Institutum* prints the Constitutions in a clean Latin text (row 75). This disclosure binds the 1606 and 1595 files and the other second witnesses, and it does not bind that text. No public-domain English exists for the Constitutions (row 39).

**2. Faber's *Memoriale* is a primary voice (Step 0 §4 item 2).** It is cited as Faber's own words in the Latin (rows 17, 18). Boero's Part the Second is an English rendering of the same diary, from a Latin lithograph, condensed in places (row 20). That answers the corpus-map note's question about how much of the *Memoriale* the Boero volume contains. The map holds Boero's whole volume as context, provisional. Its Part II is not Boero's narrative, and the Library may want to hold Part II separately (Open_Gaps).

**3. The Trent split is settled at the corpus-map level (Step 0 §4 item 3).** The Waterworth text is `tradition` for the Tridentine Church and `context` for this world (row 35). It is used here only for the Article 4 context.

**4. The Chinese and Malabar Rites are in the window, and no document of them is vendored (Step 0 §4 item 4).** Doc_01 carries their events as Step 0 gives them, each date at Inferential/Thin. No source on the shelf tests them (row 53).

**5. The gap after Xavier's death and after 1562 (Step 0 §4 item 5).** §6 states the gap as it stands. Volumes 1 to 35 of the *Jesuit Relations* are vendored and were read only at the loci named in rows 90–92. Volumes 36 to 73 are not vendored (row 42).

**6. The unattributed selection rationale (Step 0 §4 item 6, disclosure only).** Neither the desert-monastic echo nor the "Catholic-renewal voice" framing has a findable record of the project lead's own reasoning. This document does not use either as an argument.

**7. The Latin scans have not been checked against page images.** The files' headers say that wording must be checked against the page image before it is quoted. No page image was available to this pass. Every Latin quotation here is verified only against the scan text. The OCR errors seen in the Latin quotations, such as "Mercarían us", "Juiii" and "3l" for 31, are left as printed or paraphrased.

**8. Canisius's 1622 scan.** Long s is printed as f, marginal Scripture references are interleaved, and letters are misread. No continuous passage can be quoted. Whether it is garbled under the Library's own rule is the Library's call (row 34, Open_Gaps). This document does not decide it.

**9. Living tradition.** Every vendored edition and every translation of the Society's own texts is by a Jesuit or by the Society, except Thwaites's edition of the *Relations* (rows 90–92). What this world says of the Society is mediated by the Society's own account of itself (Doc_01 §1).

**10. Xavier's catechetical documents.** They are English of 1872, taken through a Latin version, and attributed to Xavier by Coleridge (row 22). They are used for the Article 4 check, and are not treated as Xavier's own words.

**11. The census and the shelf disagree in one place.** The census's Xavier story quotes "the best who have as yet been discovered". That wording is Costelloe's English of a Spanish sentence in the *Monumenta Xaveriana*, and it is not in Coleridge's (rows 23, 43, 85).

**12. Two columns.** The *Institutum* and several other volumes are printed in two columns, and the scan interleaves the columns line by line. Quotations from them are taken only where a phrase runs unbroken along its own line, and the Registry names the lines (rows 74–76).

## 8. Confidence Map

| Claim | Confidence | Basis |
|---|---|---|
| The Society was confirmed by bull on 27 September 1540. | Documented for the year and the day. | The bull's own dating clause and the *Institutum*'s index (row 74), the Lainez editors and Coleridge's contents page (rows 21, 25) give 27 September. Nadal's count of sixteen years to 1556 gives the year (row 27). Only Coleridge's text reads 17 (row 21). |
| The Society had a spoken approval on 3 September 1539. | Documented for the year; the day rests on Coleridge alone. | Rows 9, 21. |
| Ignatius was elected General in April 1541. | Documented for the month. | Rows 9, 21. The day is not settled. |
| Ignatius died on 31 July 1556. | Documented. | The first general congregation's own heading, the O'Leary table and Nadal's own note through the editors (rows 75, 9, 27) |
| Lainez was elected General on 2 July 1558 and died on 19 January 1565. | Documented. | The first and second congregations' headings give both dates (row 75). The Salmeron preface gives 2 July, and the Lainez preface's scan reads "2 Juiii" for the same day (rows 25, 32). The last Lainez letter is of 19 January 1565 (row 81) |
| Borgia was elected on 2 July 1565 and died on 1 October 1572. | Documented. | The second and third congregations' headings (row 75), and one preface (row 33) |
| Mercurian was elected in April 1573 and died on 1 August 1580. | Documented for the month and for the death. The day of the election is Contested between two editors. | The third congregation's heading has 23 April (row 75). The Salmeron preface has 29 April (row 33). The death is in both, and in the fourth congregation's heading (rows 75, 33) |
| Aquaviva was elected on 19 February 1581 and died at the end of January 1615. Vitelleschi was elected on 15 November 1615 and died on 9 February 1645. Carafa was elected on 7 January 1646. | Documented as the Society's own record. | The headings of the fourth, seventh and eighth congregations (row 75) |
| Nadal died on 3 April 1580. | Documented as the editors' statement. | One preface (row 27) |
| Faber died on 1 August 1546. | Documented as a circular letter's statement. | Boero quotes it (row 19) |
| The Society had eight provinces at the start of 1555. | Documented. | Polanco and the editors' table agree (row 30) |
| The number of places of residence in 1555. | Contested between two counts. | Sixty-one (Polanco) and sixty-five (the editors) (row 30) |
| The companions vowed to go to Jerusalem and were freed from the vow. | Widely Accepted. | Lainez editors and Coleridge (rows 21, 25) |
| The Society was founded as a response to the Reformation. | Contested. | Step 0 §2 A3 against the shelf's own account and the census's note on O'Malley (rows 21, 25, 54) |
| Paul IV imposed choir and a three-year term, and Lainez had them removed. | Documented as the editors' statement. | One preface (row 25) |
| Pius V restricted ordination to men with solemn vows. | Documented as the editors' statement. | One preface (row 33) |
| Xavier landed in Japan in 1549. | Documented. | His own letter of 5 November 1549, in Coleridge's English and in the original Spanish (rows 23, 85) |
| Xavier died on 2 December 1552. | Widely Accepted for 1552. Documented as Coleridge's statement for the day, Friday 2 December. | Coleridge is the single witness on the shelf (row 24, lines 30589–30590) |
| The "Explanation of the Creed" is Xavier's work. | Inferential/Thin. | Coleridge names no source (row 22) |
| The catechist's form, in a Latin and English chain, reflects Xavier's method. | Inferential/Thin. | Rows 22, 62. |
| The Article 4 commitments are affirmed in substance in the founders' generation. | Commitment 4 is largely shown, and "in glory" is not found. Commitments 1, 2, 3 and 5 are shown in substance. The clauses not found are silent, not denied. | Doc_01 §8. Some clauses rest on Coleridge's rendering of material attributed to Xavier, which is Inferential/Thin for the attribution. |
| The Article 4 floor holds for the mission's later voice and for 1585–1650. | Not checked. The *Relations*, the decrees and Trigault are on the shelf and were not read for it. | Doc_01 §8. |
| The Second General Congregation took Nadal's scholia for direction only. | Documented. | Its decree 42 (row 75) and the editor's statement (row 28). |
| Ignatius's *Exercises* were approved by the Holy See in 1548. | Documented. | Mullan and the brief's date (row 4), and the *Institutum*'s index (row 74) |
| The Generals' letters to Salmeron are register copies, often by secretaries. | Documented as the editors' statement. | Rows 26, 33, 69. |
| Polanco's letters to Salmeron were written on the Generals' commission, about 150 of them for 1556–65. | The commission is Documented as the editors' statement. The count is from OCR headings and is approximate. | Salmeron Tomus I, lines 1709–1710 (rows 32, 73). |
| The Autobiography reports Ignatius's words closely. | Documented as the Writer's statement; the Writer also says he could not explain some words. | Row 70. |
| The order's central voice is fullest to 1565, thinner for 1565–85, and after 1585 only the decrees and ordinances of the *Institutum*. | Documented for the shelf. | §6. |
| The only sustained mission voice on the shelf after Xavier is that of New France, 1610–1650. | Documented for the shelf. | Rows 90–92; §6. |
| The Chinese and Malabar Rites events fall in the window: Ricci from the 1580s, de Nobili from 1606, the ruling of 1623, the Jiading conference of 1627–28 and the decree of 1645. | Inferential/Thin. | Step 0 §2 A3 and the source dossier, which name no source. No vendored source confirms any of the dates (row 53) |

**Confidence propagation.** The world's outline rests at Documented, often on one editors' preface. The outline is the founding, the Generals' dates, the provinces of 1555 and the presence at Trent. Its practice, its daily work and its missions after 1552 rest at Inferential/Thin or on no evidence at all. The exception is New France, whose reports were read only at a few loci.

## 9. Search record, field-bibliography sweep, and saturation

**Search record (STARLITE headings).**

*Sampling strategy:* the 396 text files in `cic/texts/` (358 `.txt` and 38 `.xml`) were searched by full text. The directory holds 403 entries. The other seven are metadata files, the index database and the intake folder.

*Terms:* the search was one case-insensitive regular expression, `Jesuit|Society of Jesus|Societatis [IJ]esu|Compañía de Jesús|Company of Jesus`, applied to each file with every run of whitespace collapsed to one space. The names searched were Loyola, Xavier, Canisius, Ricci, the *Ratio Studiorum*, Acosta, Bellarmine, Lainez, Salmeron, Ribadeneira, Borgia and Nadal. The corpus map, the texts registry, the source dossier, the census entry VI.11 and Step 0 were read.

*Type:* source discovery for a construction step.

*Approaches:* full-text search; corpus-map and registry read; census fields; footnote and preface snowball in the vendored apparatus.

*Instruments:* Python and `grep` over `cic/texts/`.

**Date:** 2026-09-30

*Results:* 144 files match the Jesuit words. Eighty-five of the 87 assigned files match. The two that do not are Canisius's English of 1622, whose scan is garbled, and Trigault's Latin of 1615, whose scan has lost its word spaces. The other 59 matches are other worlds' files with incidental mentions or false matches. The *Ratio Studiorum* matches thirteen files, twelve of them assigned to this world (rows 45, 76). Jesuit voices composed after February 1585 are the decrees and ordinances of the *Institutum*, Trigault's Latin and the *Jesuit Relations* (rows 75, 76, 89–92).

**Field-bibliography sweep: not run.** No external bibliographic instrument was consulted. Instruments not reached are named in the Registry's saturation statement. The saturation statement there is not closed, and the Step 2 completion standard's saturation requirement is not met until a sweep has been run and dispositioned.

## 10. Open items carried forward

Gaps, requests to the Library thread, candidates on other worlds' shelves, and questions for the project lead are in `Open_Gaps_Tracking.md`.

## 11. Disposition

Draft. It is not approved to proceed, and it is not frozen.
