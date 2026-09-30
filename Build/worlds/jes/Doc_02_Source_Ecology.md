# Doc_02 — Source Ecology: The Society of Jesus

**Status:** Draft. Not reviewed. Not approved to proceed. Not frozen.
**Companion document:** `Source_Registry.md` (the per-source ledger; "row N" below means a Registry row). Gaps and requests are in `Open_Gaps_Tracking.md`.
**Governed by:** Construction Framework V7.4 Part II and Step 2. Constitution V2.3, Article 17 (the five confidence levels), Article 20 (source asymmetry and marginalized voices) and Article 26 (Author Gravity). `Source_Registry_Template.md` V1.0. Forces Framework Step 2.
**Forces Framework integration:** Step 2. The forces lens is applied in §6.
**Grounded in:** `Doc_01_World_Identification_Boundaries_Orientation.md` (1540–1650; strand-singular as a recommendation pending the project lead). This document does not reopen Doc_01.

Confidence terms follow Article 17. Quotations are matched to the vendored files. Whitespace and line-break hyphens are normalised, and long s is read as s. No other letter is corrected. Every Latin quotation is checked against the scan text only. No page image was available.

---

## 1. Primary Sources

Nineteen works are vendored and assigned to this world (`cic/corpus-map/the-society-of-jesus.yaml`). They come to about 23.17 million characters in all. Every figure in this document is counted in a UTF-8 locale (`LC_ALL=C.UTF-8`). There two counts agree: the sum of the decoded length of each file, and `cat` of the nineteen files piped to `wc -m`, both give 23,171,710. A count of words by whitespace gives 3,397,128 by both methods. In the C locale the same commands give 23,333,736, which is the byte count, and 3,370,893 words. The word count is lower there because `wc -w` in that locale does not count a token made only of non-ASCII characters, and the files hold 26,235 such tokens. Step 0 gives 3,370,675 words for the same files. That figure is a C-locale count made before the seven Latin file headers were rewritten. The C-locale count of the files as they stood before that rewrite is 3,370,743, which is 68 words above Step 0's figure. Those 68 words are not traced.

- **By role in the corpus map.** Fifteen works are `tradition` role, about 18.08 million characters, or 78.0 per cent. Four are `context` role: Boero's life of Faber, the Trent decrees, Polanco's chronicle for 1555, and Ribadeneira's life of Ignatius. They come to about 5.10 million characters, or 22.0 per cent.
- **By language.** Eleven works are Latin, about 16.94 million characters, or 73.1 per cent. Eight are English, about 6.23 million, or 26.9 per cent.
- **By scan quality.** Three works are second witnesses under the Library's ruling of 25 September 2026 (point 5). They are the 1606 Constitutions, Nadal's 1595 *Adnotationes* and Ribadeneira's 1572 life. They come to about 3.73 million characters, or 16.1 per cent. Without them, the Latin that can be quoted as primary is about 13.21 million characters, or 57.0 per cent. A Latin original counts as primary evidence when its scan is clean, and this world's Latin volumes are counted on that rule. The header of each of the seven Latin scans named in Open_Gaps states this rule.
- **By who made the edition.** About 12.50 million characters, or 53.9 per cent, are volumes of the *Monumenta Historica Societatis Jesu* or Bouix's edition of Faber. The editors and compilers named on the title pages are Jesuits (§2).

**Who speaks, and for which years.** The years are the years the text covers. The rows are Registry rows.

| Voice | What is on the shelf | Years covered | Rows |
|---|---|---|---|
| Ignatius, own letters. | Latin, Spanish, Italian and Portuguese letters, with the O'Leary English selection. | 1524 to 28 February 1548, with one undated letter of February or March 1548. | 9–16. |
| Ignatius, *Exercises*. | Mullan's English of the autograph. | undated text; the Latin version was copied in 1541 and approved in 1548. | 1–4. |
| Ignatius, *Autobiography*. | dictated 1553–55, in English. | narrates 1491 to about 1538. | 5–8, 70. |
| Faber. | *Memoriale*, Latin, and Boero's English. | mostly 1542–43, with later notes to 1546. | 17–20. |
| Xavier. | Coleridge's compilation, with two English catechetical documents. | 1541 to 1552. | 21–24. |
| Lainez. | editors' life; letters. | own letters to 1556; register copies to Salmeron 1557–65: two as vicar, then fifteen as General from November 1558. | 25–26, 67. |
| Nadal. | editors' life; commentary on the Constitutions. | letters 1546–62 (prefatory matter read only); undated commentary. | 27–28. |
| Polanco. | chronicle; letters to Salmeron written on the Generals' commission. | chronicle for 1555; letters from December 1556 to 1570, and two as vicar in 1572. | 30, 73. |
| Salmeron. | own letters and letters to him. | 1536–85. | 32–33, 67–69, 73. |
| The Generals to Salmeron. | register copies, Italian and Spanish. | Borgia 1565 to March 1571 (7 as vicar general, 42 as General), Mercurian 1573–80 (about 88), Aquaviva 1581–84 (18 to 19). | 69. |
| Canisius. | English catechism of 1622, from a Latin text of Canisius. | the file does not date the Latin; English of 1622. | 34. |
| Constitutions. | 1606 print. | second witness. | 36. |
| Nadal, *Adnotationes*. | 1595 print. | second witness. | 29. |

**Ignatius and the first companions.**

- Ignatius has four kinds of text on the shelf. The *Exercises* are his manual for a retreat (rows 1–4). The *Autobiography* is a life he dictated in his last years (rows 5–8, 70). His letters run from 1524 to 28 February 1548 in the Latin volume. One undated letter of February or March 1548 follows. The English selection stops in 1547 (rows 9–16). The Latin volume also prints the ambassador's letter of March 1540 about sending men to India (row 15).
- Faber is a private diary in Latin, with an English rendering in Boero's Part the Second (rows 17–20).
- Xavier is on the shelf through Coleridge's compilation of his life and letters (rows 21–24). Coleridge also prints, in his notes, catechetical documents he attributes to Xavier (row 22).
- Lainez, Nadal and Salmeron are in Jesuit editions of their letters. Nadal's commentary on the Constitutions is a separate work (row 28). Salmeron's two volumes also print the letters of others to him. Those include about 150 letters by Polanco, written on the Generals' commission. They include letters under the Generals' own names, and one report on the Ireland mission of 1542 (rows 67–69, 73).
- Polanco's chronicle for 1555 gives one year of the order's life in detail (row 30). His letters to Salmeron, written on the Generals' commission, run from December 1556 and are the largest body of Roman letters on the shelf for 1556–65 (row 73).
- Canisius appears through a 1622 English catechism (row 34).

**What is not on the shelf.** The Formula of the Institute (row 38) and the Constitutions in a clean text (rows 36, 40). Ignatius's letters after February or March 1548 (row 49). Any letter or book of the Generals beyond the register copies to Salmeron (rows 47, 48). The *Jesuit Relations* (row 42), the *Ratio Studiorum* (row 45), and any text by Ricci or de Nobili (rows 51, 52).

## 2. Author Gravity Assessment

Five dimensions: Visibility, Representativeness, Influence, Limitations, Transmission History.

**Ignatius of Loyola (1491–1556).**
- *Visibility:* The most visible voice. He is the founder, and four kinds of his writing are on the shelf. Everything the Society says of itself in its first years is measured against him.
- *Representativeness:* The *Exercises* speak for a formation that every Jesuit passed through. Letters X and XX speak for the Society's early ministry (rows 10, 12). The *Autobiography* speaks for one man's account of his own conversion. Nothing on the shelf shows what an ordinary Jesuit in a school or a mission made of the *Exercises* in daily practice.
- *Influence:* Central. Nadal's commentary, Faber's diary and Xavier's letters all assume the *Exercises* and the Constitutions (rows 27, 28, 18, 23).
- *Limitations:* Two of his four kinds of text look back. The *Autobiography* was dictated in 1553–55 about events of 1521–38 (rows 5–7). The Writer says he adhered so closely to Ignatius's words that afterwards he could not explain the meaning of some of them. The *Exercises* are a manual, and Rule 13 is a rule for the exercitant. It tells us how Ignatius wanted men to hold to the Church. It does not tell us how the Society held to it under pressure from Popes (row 1, Doc_01 §2).
- *Transmission History:* The *Exercises* reach us through Mullan's English of the Spanish autograph (1914). Mullan says the Latin version was "formally approved by the Holy See in 1548" (row 4). The *Autobiography* has four stages. Ignatius spoke. Gonçalves da Câmara took notes, and part of them he dictated in Latin at Genoa in December 1555. Codretto made a Latin translation. O'Conor's English appeared in 1900 (rows 70, 71). The Editor does not say from which text the English was made. The letters reach us in the MHSI edition of 1903, from the order's own archive, and in O'Leary's English selection of 1914 (rows 9, 14–16). The Regesta from 1547 are the secretary's copies (row 16). The editors' own list says that Polanco and other secretaries wrote some letters at his order (row 14). No page image was seen.

**Peter Faber (1506–46).**
- *Visibility:* One private voice, on the shelf in Latin and, in part, in English.
- *Representativeness:* He speaks for a devout, solitary and travelling first companion. The Bouix preface says that Ignatius judged no other companion better able to absorb and pass on the spirit of the *Exercises* (row 17). He does not speak for the order's governing or its schools.
- *Influence:* The editors present him as a model of the *Exercises* lived (row 17). Ignatius's view is reported at second hand, in the editor's preface.
- *Limitations:* The diary is short: mostly a year from June 1542, with later notes (row 17). It mixes Latin and Spanish. It is a private record and does not show the Society's public work.
- *Transmission History:* The autograph is lost. Bouix says "ubi terrarum hodie lateat in incerto est", that it is unknown where on earth it now lies (row 17). The Latin was printed from lithographed copies of an earlier transcript (row 17). Boero's Italian is shorter than the Latin, and Coleridge's English is condensed in many places to match it (row 20). The Bouix Preface says that Pius IX had recently allowed Faber to be called Blessed and to be honoured with the rite of the Blessed. The title page prints 1872, and the Preface is dated 8 December 1873 (row 17, lines 349–355). Boero wrote his life after the Sacred Congregation of Rites had sanctioned the veneration of Faber (row 19).

**Francis Xavier (1506–52).**
- *Visibility:* The main missionary voice on the shelf. It is the only one, outside a few pages of Polanco and one report on the Ireland visit (rows 21–24, 30, 68).
- *Representativeness:* He speaks for the first missions to India and Japan. He does not speak for Ricci's China, de Nobili's India, or the later missions.
- *Influence:* His letters helped draw recruits. The editors' account of Nadal says one of them moved him to enter the Society (row 27).
- *Limitations:* The letters were written for circulation, with a missionary's hopes. The census adds its own caveat: his account of Japan is a first impression, taken through an interpreter of limited education. That caveat is the census's, and it is not tested here.
- *Transmission History:* Coleridge (a Jesuit, 1872) compiled the volumes from printed and manuscript sources. His postscript to Volume II tells of a manuscript collection of letters. It was brought from the archives of the Goa college in the last century "at the time of the suppression". Philippucci had already examined and translated it (row 23, postscript at lines 163–177). Xavier's catechetical documents in Volume I reach us by way of Philippucci's Latin, the editions of Menchaca and Poussines, and Coleridge's English (rows 22, 62). Coleridge gives no source for the "Explanation of the Creed". The attribution to Xavier himself is Inferential/Thin.

**Diego Lainez (1512–65).**
- *Visibility:* Present in three ways. His own letters to 1556 are in the Lainez volume. As General he is in register copies to Salmeron. The editors' life of him is a compact history of the order (rows 25, 26, 67).
- *Representativeness:* He speaks for the early governing centre of the order, first as one of Ignatius's chief helpers, then as vicar and General. The editors themselves say that letters of his generalate were mostly written in his name by secretaries (row 26).
- *Influence:* The editors report Ignatius's own judgment that no man had done more for the Society than Lainez. In that judgment Ignatius counted the great apostle of the Indies too (row 25, lines 200–204, in Latin).
- *Limitations:* The Lainez volume ends in 1556. The Preface says the registers of 1556–58 were lost. Almost no letters to Spain and Portugal survive for those years (row 26).
- *Transmission History:* The letters come from autographs and from the registers. The editors say they chose among the letters ("Delectus proinde adhibendus fuit") and did not print all (row 26).

**Jerónimo Nadal (1507–80).**
- *Visibility:* Strong, through his editors and his commentary. His own letters were not read beyond the Preface.
- *Representativeness:* He is the order's interpreter of the Constitutions and its travelling visitor. He speaks for the order's governors. He does not speak for the men in the field.
- *Influence:* Ignatius sent him through Spain, Portugal and much of Europe to explain the Constitutions. The Second General Congregation took his scholia for direction only and without any obligation, on the editor's report (rows 27, 28).
- *Limitations:* The commentary is a private work. Its editor says the congregations later settled points that Nadal left open (row 28). His Gospel commentary of 1595 is a second witness for scan quality (row 29).
- *Transmission History:* The letters are in the MHSI volume of 1898. The scholia were printed at Prato in 1883, from manuscript notes kept in the Society's houses (row 28). The *Adnotationes* came out in 1595, fifteen years after his death (rows 27, 29). The editors' Protestatio says that all reports of miracles and revelations rest on human faith only (row 27).

**Alfonso Salmeron (1515–85).**
- *Visibility:* A single correspondent, but a large one. His two volumes hold most of what the shelf has after 1562 (rows 32, 33).
- *Representativeness:* He speaks for a theologian at Trent and, from 1558, a leader of the Naples province. The letters sent to him give the view from Rome to one province (rows 69, 73).
- *Influence:* He and Lainez spoke first at Trent as the Pope's theologians (row 32). He also went to Ingolstadt in 1549 with Le Jay and Canisius (row 32).
- *Limitations:* The volumes' contents are the business of one man. The editors omit the passages in Polanco's letters about wine, provisions and payment. They also omit most of the letters that Salmeron himself wrote in Lainez's name. He wrote them at Rome as acting vicar general, from September 1561 to May 1562 (row 32, lines 1033–1035 and 1054–1057).
- *Transmission History:* The editors say that they print everything, including the faults and errors of the order's men. They say that Boero's earlier versions of Salmeron's letters were corrected, altered and almost always cut (row 32). Both statements are the editors' own claims and were not tested. Salmeron's own commentaries came out after his death, in 1597–1602 (row 63).

**Juan Alfonso de Polanco (1517–76).**
- *Visibility:* Two bodies of writing on the shelf. One is the chronicle for the single year 1555. The other is about 150 letters to Salmeron, from December 1556 to 1570, printed in Salmeron's two volumes (rows 30, 73).
- *Representativeness:* The secretary of Ignatius, writing the order's history from its own papers (row 30). After Ignatius died he wrote to Salmeron on the commission of the vicar and of the Generals. He speaks for the centre, and in the letters he writes in the plural voice of the office (row 73).
- *Influence:* The Lainez editors call him the first and most diligent writer of the order's annals (row 25, in Latin).
- *Limitations:* Only Tomus V of the chronicle is vendored. It counts sixty-one places, and the editors' note counts sixty-five (row 30). The letters go to one correspondent, in Naples. The editors leave out the passages about wine, provisions and payment (row 73).
- *Transmission History:* The chronicle was printed in Madrid in 1897, from the manuscript volumes of his chronicle (row 30). For the letters, the Salmeron editors' footnotes cite the Society's register volumes, for example the fourth Regesta codex (row 73).

**Peter Canisius.** His catechism reaches us in an English translation of 1622, by an unnamed translator, from a Latin text (row 34). The scan is badly damaged. The census says his catechisms shaped Catholic teaching across German-speaking Europe. Nothing else of his is on the shelf.

**Pedro de Ribadeneira.** His Latin life of Ignatius (Naples, 1572) is held at second-witness status (row 31). The corpus map calls him someone who knew Ignatius personally. The life is not read here.

**The Jesuit editors and translators.** Mullan, O'Conor, Goodier, Coleridge, Boero, Bouix and the fathers of the *Monumenta Historica Societatis Jesu* are all members of the Society, on their title pages. The files do not say whether O'Leary, who translated the letters, was a Jesuit, and the Canisius translator is unnamed. Their editions are careful, and some of their prefaces state their policies openly (rows 26, 32). Every edition is also an act of self-presentation by the order. The Bouix preface, the Boero life and the Nadal Protestatio show a devotional and hagiographic frame (rows 17, 19, 27). Coleridge's Xavier volumes give a Jesuit's reading of Xavier for English Catholics (rows 21–24). No editor outside the Society is on the shelf for any of the Society's own texts. This document treats that as a structural fact about the shelf and not as a fault in any one editor.

## 3. Secondary Scholarship Assessment

All the secondary matter on the shelf is by Jesuits and was written between 1872 and 1914. It is the editors' prefaces, Coleridge's narrative and Boero's life. No modern specialist work is vendored. O'Malley (1993), Schurhammer (1973–82) and the *Cambridge History* chapters are named in the census and are not vendored (rows 54–56). Claims below rest on the editors' prefaces and are marked accordingly.

**1. Why was the Society founded? Contested.** Step 0 (§2 A3) places the order inside the Reformation crisis as a response to it. The shelf's own account is different. Coleridge, a Jesuit, reports an address of the companions in 1537. They could not go to Palestine as they had vowed. In Italy they found "how vast a field" for their apostolic labours (row 21). The Lainez editors say Lainez was freed from "voto Hierosolymas adeundi", the vow to go to Jerusalem (row 25, in Latin). The census's note on O'Malley says that book was written "to counter mythologized readings of the order's founding" (row 54). Both readings are carried. The vow to go to Jerusalem is Widely Accepted. The address itself is at three removes, and is Inferential/Thin.

**2. What was the bull's day? Not settled.** Coleridge's contents page reads "Sept 27, 1540", and his text reads "Sept. 17". The Lainez editors give "27 Septembris anni 1540" (rows 21, 25). The year is Documented, and the day is carried as 27 September on the editors' authority, with the difference noted. Coleridge's own sentence says the bull was signed "on the Feast of SS. Cosmas and Damian, Sept. 17, 1540" (row 21, lines 4822–4823). Nothing on this world's shelf gives the day of that feast, so the feast does not settle the question here. The Roman Breviary, which is assigned to another world (Open_Gaps, section E), prints the feast under 27 September in a calendar of 1908. This document does not use it.

**3. When was Ignatius elected General? Not settled.** Coleridge dates the ballots 4–5 April 1541 and Ignatius's entry on duty 19 April. The O'Leary table says 13 April (rows 9, 21). April is Documented and the day is carried open.

**4. How far did Nadal's commentary bind? Documented as the editor's statement.** The Second General Congregation took Nadal's scholia for direction only, with no obligation (row 28). Nadal's private view was not the Society's law.

**5. The Chinese and Malabar Rites. No secondary or primary source on the shelf.** Step 0 dates its events to 1623, 1627–28 and 1645. No source on the shelf confirms any of these dates, so each is Inferential/Thin. Their only basis is Step 0 §2 A3 and the source dossier, and neither names a source (rows 51–53).

**6. Jesuits in other worlds' files.** Sarpi's history of Trent names Lainez and Salmeron, and the Roman Breviary names Xavier and Borgia. Both are assigned to the Tridentine Church. The matches were counted and not read. Neither file is used here (Open_Gaps, section E).

## 4. Formation Narrative Sources

- **The *Autobiography*.** A first-person life, given by Ignatius to a scribe over two years, in his last years (rows 5–8, 70). It gives the story of a conversion and a formation. Tier 1 in the Framework's four-tier scheme, for what Ignatius reported of himself. That means Documented to Widely Accepted at the narrative level, with the mediation named in §2. The scribe's or editor's plural voice at line 484 is Tier 3 (attributed tradition). It is a hagiographic comment on Ignatius's chastity. The visions in Chapter III are Tier 3 for their content and Tier 1 as what Ignatius said he saw.
- **Faber's *Memoriale*.** A private diary of an interior life (rows 17, 18). Tier 1 for what Faber wrote of himself. Boero's frame is Tier 3.
- **Ribadeneira's life of Ignatius.** A close disciple's life (row 31). Not read. Held at second-witness status. Tier 3 by genre, if used.
- **Coleridge's *Life and Letters of St. Francis Xavier*.** A compiler's narrative with the letters set in it (rows 21–24). Tier 1 where the letters speak. Tier 3 in Coleridge's account of visions and miracles, which this document does not use.
- **Boero's life of Faber.** A beatification-era life (row 19). Tier 3. It quotes the circular letter of 7 August 1546 on Faber's death. That letter is Tier 1 for the fact of the death (row 19).
- **Polanco's chronicle.** A secretary's history from the order's papers (row 30). Tier 1 for the year 1555, with the editors' corrections.
- **The stories the census names.** The census's Tier 1 story "Xavier Writes from Kagoshima" says of itself: "from reference summaries; primary text not yet read". The shelf has the letter in Coleridge's English (row 23), and this document has read it. The census's quoted wording is not in Coleridge's translation (row 43). The story's tier waits on the Costelloe translation or the original.

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

**Overrepresented:** Ignatius and the first generation; the order's Roman centre; Iberian and Italian Jesuits; Jesuit editors of the years 1872–1914.

**Structurally missing, and why:**

- **Ordinary Jesuits.** The brothers and coadjutors appear rarely and as helpers, for example Brother Christopher López, Ribadeneira's companion and librarian (row 32). Residences appear in lists (rows 8, 30). No brother, novice or teacher speaks of daily life.
- **Women.** Ignatius writes to women (rows 13, 37). The Lainez editors say Margaret of Austria had been Lainez's penitent at Rome (row 25). The Salmeron editors name two noblewomen among the correspondents of that volume, Portia Carafa, countess of Ruvo, and Maria Sanseverino, countess of Nola. The editors list them among the authors of letters written to Ignatius, Lainez, Borgia or Salmeron, so they wrote (row 33, lines 238–262). Women appear as patrons and correspondents. None speaks as a member of the order.
- **The laity.** The confraternity at Azpeitia, the poor in the hospitals and the children in catechism appear only as objects of the Society's work (rows 10, 12, 22).
- **The peoples of the missions.** No Japanese, Indian, Chinese, Ethiopian, Brazilian or Irish voice is on the shelf. The Japanese appear through Xavier (row 23). The Irish appear through the missionaries' report on their visit (row 68). The Ethiopians appear through Polanco's note on the consistory and the patriarchate (row 30). The census names Ricci for China and de Nobili for India, and neither is on the shelf (rows 51, 52).
- **The opponents.** No Protestant, Dominican, inquisitor or colonial official speaks in his own words. They appear as the Society's editors describe them (rows 7, 24, 25, 27).
- **The Society's own critics inside the order.** The editors say that quarrels ambitious men stirred up in 1556–58 were the worst of the order's troubles (row 25). No voice of those men is on the shelf.

**The Jesuit voice gap, stated plainly.**

1. **1556 to 1562.** The order's central voice is partial. It comes through one correspondent's mail. Ignatius's own letters end on 28 February 1548, with one undated letter of February or March (row 16). Lainez's own volume ends in 1556, and the registers of 1556–58 are lost (row 26). Polanco's chronicle covers only 1555 (row 30). Nadal's letters run to 1562, and this pass read only their Preface (row 27). Against that, Salmeron's first volume prints about 150 letters from Polanco to Salmeron, written on the commission of the vicar and of the Generals. Of the 146 read in full, 112 fall in 1556–61 (row 73). It also prints 2 letters from Lainez as vicar and 15 from Lainez as General (row 67). So the centre does speak for these years, but only to the Naples province, in the plural voice of the office, and mostly in Italian and Spanish. Salmeron writes throughout.
2. **1558 to 1585.** The Generals speak only as senders of register copies to one correspondent, Salmeron, in Naples. Counted from the scan's headings, Salmeron's first volume has 17 letters headed Lainez: 2 as vicar and 15 as General, from November 1558 to January 1565. It also has about 150 headed Polanco on the commission of the Generals (rows 67, 73). The second volume has 49 headed Borgia: 7 as vicar general in 1565 and 42 as General, to March 1571. It has about 88 headed Mercurian, from 1573 to 1580, and 18 to 19 headed Aquaviva, from 1581 to 1584. It has 12 more headed Polanco on commission, to 1570 (rows 69, 73). Most were written by secretaries in the General's name. Nothing vendored is a volume of any General's own correspondence. Step 0 §4 item 5 states the same count.
3. **After 1562.** Salmeron's two volumes are the one continuous thread to February 1585 (rows 32, 33).
4. **After February 1585.** Nothing composed after this date is vendored. The window runs to 1650, so 65 of its 110 years, or 59 per cent, have no Jesuit voice of their own. The three later works on the shelf are later printings of earlier texts: the *Adnotationes* (1595), the Constitutions (1606) and Canisius in English (1622) (rows 29, 34, 36). The first two are second witnesses.
5. **The missions.** The missionary voice is Xavier's, to his death in 1552, with one report on the Ireland visit (1542) and one year of Polanco (rows 21–24, 30, 68). The *Jesuit Relations* are not vendored (row 42). No text of Ricci or de Nobili is on the shelf (rows 51, 52). The census names the Relations as a core primary source for the global dimension, and it has not been checked.
6. **What this means for the world.** A Representative built on this shelf would have a full voice for 1540–1556, a partial voice for 1556–1562, and a thin voice for 1562–1585. It would have no voice at all for 1585–1650, unless the Library supplies the volumes listed in Open_Gaps, section B. Doc_02 does not fill the gap from the census or from memory.

**Forces lens (Forces Framework Step 2).** The forces are those in Doc_01 §6. Externally they are the Reformation and the Council of Trent, papal control of the order, suspicion and inquiry, colonial officials, and the controversy over the rites. Internally they are the quarrels of 1556–58 and, later, the dispute over accommodation inside the order.

*Which sources speak to external forces.*
- The Council: Ignatius's instruction for the road to Trent (row 12); Lainez's and Salmeron's roles there, in the editors' lives (rows 25, 32); the Trent decrees themselves (row 35).
- Papal control of the order. Paul IV's imposed choir and term, and Lainez's work to remove them, are in the Lainez preface (row 25). Pius V's decree on ordination, and Salmeron's advice, are in the Salmeron preface (row 33). Nadal's plea to Gregory XIII is in the Nadal preface (row 27). Polanco's letters to Salmeron run through the years of the Pauline decrees and of the quarrels of 1556–58 (row 73). They were counted and not read for this question, so they are named here as a source for Doc_08.
- Suspicion and inquiry: the *Autobiography* on Alcalá, Salamanca and Rome (row 7); the attack on the *Exercises* in 1554 (row 27).
- Colonial officials: Xavier and Don Alvaro (row 24), the ambassador's letter of 1540 (row 15).
- The rites: no source (row 53).

*What the silences show.* Nothing on the shelf is a papal document in the original. There is no bull and no brief, and the Formula of the Institute is absent (row 38). No Protestant, Dominican or inquisitorial text is on the shelf, so the pressure appears only through the Society's own account of it. The forces that shaped the order most, the Reformation and the Roman curia, are heard only from inside the order. No source has economic conditions as its subject. Whether the vendored books treat the funding of colleges beyond passing mentions was not read in this pass.

*Survivorship patterns.*
- The order kept its own archive, and its own Jesuit fathers edited it in the years around 1900 (rows 14, 16, 25). What survives is what the archive kept. Register volumes for 1556–58 are lost (row 26), and the sixth of the Ignatian registers, for Spain, Portugal and India in 1556, seems lost (row 16).
- The editors chose. The Lainez editors say they selected among letters (row 26). The Salmeron editors omit the passages in Polanco's letters about wine, provisions and payment. They also omit most of the letters Salmeron wrote in Lainez's name as his deputy at Rome. They say they omit nothing that would stain the order's history (row 32). That statement is a claim of the editors and was not tested.
- Faber's autograph is lost (row 17). A collection of Xavier's manuscript letters was brought out of the archives of the Goa college at the suppression (row 23).
- The pressure that shows most is therefore papal and internal, because the order's archive kept the letters about it. This is an effect of what survives. It is not a finding that Rome was the most threatening force.

**Evidential visibility is not ecological visibility.** The world's most formative work was likely the *Exercises* given one to one, the classroom, the confessional and the mission station. The shelf's evidence is the founder's writing, the Generals' business letters and one missionary's correspondence. Reconstruction that reaches past the evidence is marked Inferential/Thin. A bounded reconstruction of any marginalised voice needs a specific textual trace and is not attempted here.

## 7. Required Disclosure

**1. The Constitutions and Nadal's *Adnotationes* are not primary-quotable (Step 0 §4 item 1, binding).** Both are vendored and both are second witnesses for scan quality. Doc_02 does not quote either. It cites the Constitutions only for the structure of the front matter (row 36) and the *Adnotationes* only for its genre (row 29). Ribadeneira's life (row 31) is held the same way. No public-domain English exists for the Constitutions (row 39).

**2. Faber's *Memoriale* is a primary voice (Step 0 §4 item 2).** It is cited as Faber's own words in the Latin (rows 17, 18). Boero's Part the Second is an English rendering of the same diary, from a Latin lithograph, condensed in places (row 20). That answers the corpus-map note's question about how much of the *Memoriale* the Boero volume contains. The map holds Boero's whole volume as context, provisional. Its Part II is not Boero's narrative, and the Library may want to hold Part II separately (Open_Gaps).

**3. The Trent split is settled at the corpus-map level (Step 0 §4 item 3).** The Waterworth text is `tradition` for the Tridentine Church and `context` for this world (row 35). It is used here only for the Article 4 context.

**4. The Chinese and Malabar Rites are in the window, and no source is vendored (Step 0 §4 item 4).** Doc_01 carries their events as Step 0 gives them, each date at Inferential/Thin. No source on the shelf tests them (row 53).

**5. The gap after Xavier's death and after 1562 (Step 0 §4 item 5).** §6 states it. The Jesuit Relations are not vendored and not checked (row 42).

**6. The unattributed selection rationale (Step 0 §4 item 6, disclosure only).** Neither the desert-monastic echo nor the "Catholic-renewal voice" framing has a findable record of the project lead's own reasoning. This document does not use either as an argument.

**7. The Latin scans have not been checked against page images.** The files' headers say that wording must be checked against the page image before it is quoted. No page image was available to this pass. Every Latin quotation here is verified only against the scan text. The OCR errors seen in the Latin quotations, such as "Mercarían us", "Juiii" and "3l" for 31, are left as printed or paraphrased.

**8. Canisius's 1622 scan.** Long s is printed as f, marginal Scripture references are interleaved, and letters are misread. No continuous passage can be quoted. Whether it is garbled under the Library's own rule is the Library's call (row 34, Open_Gaps). This document does not decide it.

**9. Living tradition.** Every vendored edition and every translation is by a Jesuit. What this world says of the Society is mediated by the Society's own account of itself (Doc_01 §1).

**10. Xavier's catechetical documents.** They are English of 1872, taken through a Latin version, and attributed to Xavier by Coleridge (row 22). They are used for the Article 4 check, and are not treated as Xavier's own words.

**11. The census and the shelf disagree in one place.** The census's Xavier story quotes "the best who have as yet been discovered". That wording is from the Costelloe translation, and it is not in Coleridge's (row 23, row 43).

## 8. Confidence Map

| Claim | Confidence | Basis |
|---|---|---|
| The Society was confirmed by bull in September 1540. | Documented for the year. | Lainez editors, Coleridge's contents, Nadal's count of sixteen years to 1556 (rows 21, 25, 27). The day is 27 September on the editors' authority; Coleridge's text reads 17. |
| The Society had a spoken approval on 3 September 1539. | Documented for the year; the day rests on Coleridge alone. | Rows 9, 21. |
| Ignatius was elected General in April 1541. | Documented for the month. | Rows 9, 21. The day is not settled. |
| Ignatius died on 31 July 1556. | Documented. | O'Leary table and Nadal's own note through the editors (rows 9, 27) |
| Lainez was elected General on 2 July 1558 and died on 19 January 1565. | Documented. | The Salmeron preface gives 2 July, and the Lainez preface's scan reads "2 Juiii" for the same day (rows 25, 32). The Lainez preface gives the death (row 25) |
| Borgia was elected on 2 July 1565 and died on 1 October 1572. | Documented as the editors' statement. | One preface (row 33) |
| Mercurian was elected on 29 April 1573 and died on 1 August 1580. | Documented as the editors' statement. | One preface (row 33) |
| Nadal died on 3 April 1580. | Documented as the editors' statement. | One preface (row 27) |
| Faber died on 1 August 1546. | Documented as a circular letter's statement. | Boero quotes it (row 19) |
| The Society had eight provinces at the start of 1555. | Documented. | Polanco and the editors' table agree (row 30) |
| The number of places of residence in 1555. | Contested between two counts. | Sixty-one (Polanco) and sixty-five (the editors) (row 30) |
| The companions vowed to go to Jerusalem and were freed from the vow. | Widely Accepted. | Lainez editors and Coleridge (rows 21, 25) |
| The Society was founded as a response to the Reformation. | Contested. | Step 0 §2 A3 against the shelf's own account and the census's note on O'Malley (rows 21, 25, 54) |
| Paul IV imposed choir and a three-year term, and Lainez had them removed. | Documented as the editors' statement. | One preface (row 25) |
| Pius V restricted ordination to men with solemn vows. | Documented as the editors' statement. | One preface (row 33) |
| Xavier landed in Japan in 1549. | Documented. | His own letter of 5 November 1549, in Coleridge's English (row 23) |
| Xavier died on 2 December 1552. | Widely Accepted for 1552. Documented as Coleridge's statement for the day, Friday 2 December. | Coleridge is the single witness on the shelf (row 24, lines 30589–30590) |
| The "Explanation of the Creed" is Xavier's work. | Inferential/Thin. | Coleridge names no source (row 22) |
| The catechist's form, in a Latin and English chain, reflects Xavier's method. | Inferential/Thin. | Rows 22, 62. |
| The Article 4 commitments are affirmed in substance in the founders' generation. | Commitment 4 is largely shown, and "in glory" is not found. Commitments 1, 2, 3 and 5 are shown in substance. The clauses not found are silent, not denied. | Doc_01 §8. Some clauses rest on Coleridge's rendering of material attributed to Xavier, which is Inferential/Thin for the attribution. |
| The Article 4 floor holds for the mission's later voice and for 1585–1650. | Not checked. The evidence is not on the shelf. | Doc_01 §8. |
| The Second General Congregation took Nadal's scholia for direction only. | Documented as the editor's statement. | Row 28. |
| Ignatius's *Exercises* were approved by the Holy See in 1548. | Documented. | Mullan and the brief's date (row 4) |
| The Generals' letters to Salmeron are register copies, often by secretaries. | Documented as the editors' statement. | Rows 26, 33, 69. |
| Polanco's letters to Salmeron were written on the Generals' commission, about 150 of them for 1556–65. | The commission is Documented as the editors' statement. The count is from OCR headings and is approximate. | Salmeron Tomus I, lines 1709–1710 (rows 32, 73). |
| The Autobiography reports Ignatius's words closely. | Documented as the Writer's statement; the Writer also says he could not explain some words. | Row 70. |
| The order's central voice is partial for 1556–62, thin after 1562 and absent after 1585. | Documented for the shelf. | §6. |
| The Chinese and Malabar Rites events fall in the window: Ricci from the 1580s, de Nobili from 1606, the ruling of 1623, the Jiading conference of 1627–28 and the decree of 1645. | Inferential/Thin. | Step 0 §2 A3 and the source dossier, which name no source. No vendored source confirms any of the dates (row 53) |

**Confidence propagation.** The world's outline rests at Documented, often on one editors' preface. The outline is the founding, the Generals' dates, the provinces of 1555 and the presence at Trent. Its practice, its daily work and its missions after 1552 rest at Inferential/Thin or on no evidence at all.

## 9. Search record, field-bibliography sweep, and saturation

**Search record (STARLITE headings).**

*Sampling strategy:* the 315 text files in `cic/texts/` (277 `.txt` and 38 `.xml`) were searched by full text. The directory holds 322 entries. The other seven are metadata files, the index database and the intake folder.

*Terms:* the search words were `Jesuit`, `Society of Jesus`, `Societatis Iesu` or `Jesu`, `Compañía de Jesús` and `Company of Jesus`. The names searched were Loyola, Xavier, Canisius, Ricci, the *Ratio Studiorum*, Acosta, Bellarmine, Lainez, Salmeron, Ribadeneira, Borgia and Nadal. The corpus map, the texts registry, the source dossier, the census entry VI.11 and Step 0 were read.

*Type:* source discovery for a construction step.

*Approaches:* full-text search; corpus-map and registry read; census fields; footnote and preface snowball in the vendored apparatus.

*Instruments:* Python and `grep` over `cic/texts/`.

**Date:** 2026-09-30

*Results:* 66 files match the Jesuit words. Eighteen of the nineteen assigned files match. The nineteenth, Canisius, does not match because its scan is garbled. The rest are other worlds' files with incidental mentions or false matches. The *Ratio Studiorum* matches five files, four of them assigned to this world, and every hit is a mention in the editors' apparatus (row 45). No Jesuit voice composed after February 1585 was found.

**Field-bibliography sweep: not run.** No external bibliographic instrument was consulted. Instruments not reached are named in the Registry's saturation statement. The saturation statement there is not closed, and the Step 2 completion standard's saturation requirement is not met until a sweep has been run and dispositioned.

## 10. Open items carried forward

Gaps, requests to the Library thread, candidates on other worlds' shelves, and questions for the project lead are in `Open_Gaps_Tracking.md`.

## 11. Disposition

Draft. It is not approved to proceed, and it is not frozen.
