# Source Ecology: The Tridentine Church (Doc_02)

**Status:** Cleared review (Round 2, Revision 2). Approved to proceed is held until the project lead rules on the Borromeo placement. Not Frozen.
**World file-code:** none assigned yet (per Step 0 and Doc_01); this document lives at `Build/World-Builds/Tridentine-Church/` until one is.
**Companion document:** `Source_Registry.md` (the per-source ledger; "row N" below means a Registry row). Gaps and requests are in `Open_Gaps_Tracking.md`; each is cited below by subject and month.
**Governed by:** Construction Framework V7.4 Part II and Step 2. Constitution V2.3, Article 4 (the floor), Article 17 (the five confidence levels), Article 20 (the affirmative duty to name omitted voices), Article 26 (Author Gravity) and Articles 28 and 29 (historical world and living tradition). `Source_Registry_Template.md` V1.0. Forces Framework V1.1 §4, Step 2 entry.
**Forces Framework integration:** Step 2. The forces lens is applied in §6 and is carried in §3, §7 and §8.
**Grounded in:** `Doc_01_World_Identification_Boundaries_Orientation.md` (Revision 3, Approved to proceed; window 1517 to 1650; strand-singular for the corporate-magisterial material, with Bellarmine's devotional voice a live second candidate for Doc_04) and `Step0_Movement_Scope_Confirmation.md` (Revision 3, Approved to proceed). This document does not reopen either.

Confidence terms follow Article 17. Quotations are matched to the vendored files. Whitespace and line-break hyphens are normalised, and long s is read as s. No other letter is corrected. Where the scan prints f for s, the quotation keeps the f. Where the scan prints an inner double quotation mark inside a quotation, the quotation shows a single mark. Every Latin, Italian, Dutch and Danish quotation is checked against the scan text only; no page image was available. A quotation is cited by the file's own division where the edition has one, and otherwise by file line. The file names are in the Registry's file table.

---

## 1. Primary Sources

The corpus-map bucket `cic/corpus-map/the-tridentine-church.yaml` holds 64 rows over 59 distinct files. The files come to 75,948,214 characters and 11,527,898 words. Every figure is counted in a UTF-8 locale (`LC_ALL=C.UTF-8`) by two independent methods. The first sums the decoded length of each file and the whitespace-split word count of each file in Python, with each file decoded from raw bytes so that the CRLF line ends of the Jewel file are kept. The second runs `wc -m -w` on each file and again on all 59 files piped through `cat`. All three agree. In the C locale `wc` counts bytes, so the same pipe gives 77,073,634 "characters" and 11,415,735 words. The word count is lower there by 112,163, because `wc -w` in that locale does not count a token made only of non-ASCII characters.

- **By role in the corpus map.** The 64 rows are 21 `tradition` and 43 `context`; 32 are `assigned` and 32 `provisional`. By file, 16 files (26,026,659 characters, 34.3 per cent) are `tradition` only, 39 files (46,466,977 characters, 61.2 per cent) are `context` only, and 4 files (3,454,578 characters, 4.5 per cent) carry both roles. The `role` is a finding-aid placement made by the Library. The Registry's Boundary Status is a separate judgement, made here on Doc_01's boundary, and the two differ in places (§7 item 15; Open_Gaps: corpus-map change requests, October 2026).
- **By language.** By the language of most of each file: Latin 16 files, 32,947,269 characters (43.4 per cent); English 25 files, 22,447,415 characters (29.6 per cent); Italian 12 files, 14,121,700 characters (18.6 per cent); Latin with English 1 file, 1,495,851 characters (2.0 per cent); Czech 1 file, 1,289,472 characters (1.7 per cent); Spanish 1 file, 1,163,870 characters (1.5 per cent); German with Latin 1 file, 1,132,915 characters (1.5 per cent); Dutch 1 file, 1,062,963 characters (1.4 per cent); Danish 1 file, 286,759 characters (0.4 per cent). Files that mix languages (Schaff, Reusch, Barlow, the Jesuit letter volumes) are counted under one label.
- **By scan quality.** Nine files are second witnesses throughout, under the Library's scan-quality rule or on this document's reading: Pole, Bascapè, Pallavicino's 1664 third part, Jewel's Latin, the three Canisius printings, Valier and Reusch (the German introduction as well as the Latin index texts). A tenth, Schaff, is a second witness for its Latin only; its English is clean and quotable, as a cross-check to Waterworth for the canons and as the working English of the Profession. The ten files come to 8,306,934 characters, or 10.9 per cent of the shelf, counting Schaff whole, so the figure is an upper bound. The other Pallavicino texts (the 1846 tomo and the first two parts of 1664) are clean and stay quotable. A Latin or Italian original counts as primary evidence when its scan is clean, under the Library ruling of 25 September 2026. Each Latin and Italian quotation here keeps the scan's letters.
- **By who made the edition.** The English texts of the Council, the Catechism, the Breviary and the Missal were made by Catholic clergy in the nineteenth and early twentieth centuries (rows 1, 10, 24, 23). Schaff, Gibbings, Barlow and the Epistle Dedicatory of the Sarpi volume are Protestant hands (rows 6, 27, 21, 50). The Latin acts are printed by the Church's own presses or by Catholic editors (rows 12, 17, 28).

**Who speaks, and for which years.** The years are the years the text covers. The rows are Registry rows.

| Voice | What is on the shelf | Years covered | Rows |
|---|---|---|---|
| The Council | The canons and decrees of all 25 sessions in English, with an editor's history; the dogmatic decrees in Latin. | 1545 to 4 December 1563. | 1 to 6 |
| The papacy | Paul III's bull against Henry VIII (Latin); Pius IV's Profession and bull of confirmation; Pius V's letters, his bulls for Breviary and Missal and for the deposition of Elizabeth; Sixtus V's *Immensa*; Clement VIII's bull of 1595; Gregory XV's *Inscrutabili*. | The bull against Henry VIII (1535, from the builder's knowledge; the lines read give no date); the others 1564 to 1622. | 7, 12 to 16, 17, 21, 72 |
| The commissioned catechism | The Roman Catechism for parish priests, in English. | Issued under Pius V; the English is the second revised edition of McHugh and Callan (copyright 1934, sixth printing 1937; first published 1923). | 10, 11 |
| The liturgical books | The Roman Missal in English (a lay edition of 1843); one volume of four of the Roman Breviary in English (Autumn). | The rite of 1570 and 1568, as revised later. | 23, 24 |
| The Index and the Holy Office | The Tridentine Index and its sixteenth-century forerunners (German scholar's edition, noisy Latin); one Inquisition sentence of 1564. | 1559 to 1570; 1564. | 19, 27 |
| The bishop of Milan | Borromeo's Acta and Instructions (Latin print of 1599); his Lives by Giussano, Possevino, Valier, Bascapè and Peña; the Breviary's lessons for his feast. Borromeo's own Italian is held as context only, pending the project lead's ruling on which world owns his voice. | His years as archbishop, 1565 to 1584; the Lives 1586 to 1884. | 28, 34 to 40, 24 |
| Devotional voices | Bellarmine's two late works in four English versions; Granada's meditations in the English of 1582; the Oratory's Life of Philip Neri. | 1615 and 1616; 1582; Philip's life, 1515 to the 1590s. | 41 to 44, 47, 48 |
| Pole | One oration in a black-letter print of 1560, not legible. | Printed 1560. | 49 |
| Narrators and opponents | Sarpi (English, 1676) and Pallavicino (Italian, 1664 and 1846) on the Council; Jewel, Marnix and Barlow's commentary against Rome. | 1562 to 1681. | 50 to 58, 22 |
| The Council's reception elsewhere | A Carmelite reformer on Trent's decrees; a Jesuit household letter from Trent; a papal bull for the Ruthenians; a Roman cardinal's letter on an Eastern patriarch. | 1562 to 1595. | 59, 68, 72, 25 |

**The Council and the papal acts.**

- The decrees reach us in Waterworth's English. The Session III recital, the Session IV decree on the Scriptures and the traditions, and the four anathemas that Doc_01 §5 sets out are all on the shelf and read clean (rows 1, 2). The disciplinary decrees on benefices, seminaries and vernacular instruction are there too (row 3).
- The Council itself ordered the Index, the Catechism, the Breviary and the Missal. Session XXV says so in a decree headed "ON THE INDEX OF BOOKS ; ON THE CATECHISM, BREVIARY, AND MISSAL." (lines 23914–23916) (row 4). The papal acts that carried the order out are on the shelf: *Quod a nobis* (1568) for the Breviary and *Quo primum* (1570) for the Missal, both in the Bullarium (row 12).
- *Regnans in Excelsis* is on the shelf twice. The Bullarium prints the Latin (row 13). Barlow prints the English and Latin in parallel columns (row 21). The Source Readiness Dossier says the bull exists only through Barlow. That is out of date.
- The curia is represented by *Immensa aeterni Dei* (row 14) and the mission office by *Inscrutabili* and the Congregation's decrees of 1626 (row 17).

**Borromeo, the bishops and the parish.**

- The Acta and the Instructions are the world's one body of diocesan legislation (row 28). They set out, among much else, the confessional box with its measurements.
- The Lives of Borromeo are hagiography. Giussano states that the Pope entrusted the Council's acts to his nephew (row 34). The Breviary's lesson for his feast says that he wished to order his Church by the requirements of the Council (row 24).
- Borromeo's own Italian letters, counsels and sermons are held as context here and are `tradition` for Borromean Milan in the corpus map. They are Native in the Registry but not licensed for this world's Representative. Which world owns Borromeo's voice is for the project lead (rows 29 to 33; Open_Gaps: no record of the Borromean Milan placement, October 2026).

**Devotional and pastoral voices.** Bellarmine speaks in two works, each in two English versions (rows 41 to 44). Granada speaks through his English translator (row 47). Philip Neri speaks through Bacci's Life (row 48). The Missal and the Breviary give the prayer of the Church in English (rows 23, 24). Doc_01 §7 item 1 asked Doc_02 to cite these directly and not to describe a thin or absent pastoral voice. This document does so, and states in §6 what is still thin.

**What is not on the shelf.**

- The Council's own acts and diaries. Theiner's *Acta genuina* and the Görres edition of *Concilium Tridentinum* are on archive.org in Latin and are not vendored (rows 81, 82; Open_Gaps: the Council's acts in Latin, October 2026).
- The Latin of the Catechism, the Missal, the Breviary and the Ritual (rows 107, 108, 109, 110; Open_Gaps: the Latin Catechism, Missal, Breviary and Ritual, October 2026).
- Bellarmine's controversial writing, which the census calls the era's standard Catholic reply to Protestant theology (row 111; Open_Gaps: Bellarmine's controversial writing, October 2026).
- Any text by or about the Capuchins, the Ursulines or the Greek College beyond one 1626 decree (rows 17, 78, 112; Open_Gaps: voices the shelf lacks, October 2026).
- Any document from before 1545 except Paul III's bull against Henry VIII, and almost nothing for 1600 to 1650 beyond Bellarmine and the Collectanea (§6; Open_Gaps: the window is thin at both ends, October 2026).
- Pole's letters, the Carranza process, visitation records, and Borromeo in English (rows 83, 97, 84).

## 2. Author Gravity Assessment

Five dimensions: Visibility, Representativeness, Influence, Limitations, Transmission History. The life and reign dates in the headings come from three places. The Library's file headers give Bellarmine, Granada, Pole and Pius V's lifespan (Creator lines). The vendored texts give Borromeo's birth in 1538 and death in 1584 (Giussano) and Philip Neri's birth in 1515 (Bacci). Pius V's reign of 1566 to 1572 is the builder's knowledge, Widely Accepted, with no Registry row.

**The Council of Trent (1545 to 1563), as a corporate voice.**
- *Visibility:* The most visible voice. Its canons and decrees are the world's charter, and every other text on the shelf refers to them.
- *Representativeness:* It speaks for the bishops, theologians and legates present. The acts record the subscribers at the close: "they were in number CCLV." (line 24112) The legates, cardinals, patriarchs, archbishops, bishops, abbots, proctors and generals who signed add up to 255 (row 4). It does not speak for the laity, for women, or for the Protestants it condemns.
- *Influence:* Central. The Catechism, the Missal, the Breviary and the Index are ordered by Session XXV (row 4). Pius V's letters press the decrees on bishops (row 16).
- *Limitations:* The decrees are the settled text. They do not show the debate. The history that does is Waterworth's editor's, a Catholic apologetic of 1848 (row 5). The disputes the Council left open, such as whether residence is of divine right, appear only in that essay (Open_Gaps: the Council's debates are carried from one essay, October 2026).
- *Transmission History:* The English is Waterworth's, a priest's translation with a preface dated 1848, in a printing of about 1888 (row 1). The Latin dogmatic decrees reach us in Schaff, a Protestant editor of 1878, whose note says the reform decrees are left out (row 6). The Latin of the Council's own acts is not on the shelf. The Library's header calls the Waterworth text a later impression of the same translation.

**Pius V (pontificate 1566 to 1572).**
- *Visibility:* Strong across four kinds of text: the letters, the bull of 1570 against Elizabeth, the Breviary bull and the Missal bull.
- *Representativeness:* He speaks for the papal office. Nothing here shows what a parish priest made of his letters.
- *Influence:* He implemented the Council. The Missal bull recalls that the Council's decrees concerned the books: "Cumque inter alia facri Tridentini Concilii decreta,nobis flatuendum effet de facris libris, Catechifmo , Miffali , & Breviario » edendis atque emendandis" (lines 87976–87979) (row 12).
- *Limitations:* The letters are a collection first printed in 1640 ("Nunc primüm in lucem" (line 40)), with the editor's headings. The bulls are in the editors' Bullarium with their rubrics (rows 16, 12).
- *Transmission History:* The letters were printed at Antwerp by the Plantin press in 1640 (row 16). The bulls are in the Luxembourg reprint of the Bullarium (catalogue date 1727, imprint year garbled in the scan) and, for *Regnans*, also in Barlow's English printing of 1681. The file header of the letters says the Latin is a second witness; the Library's own ruling and corpus-map note say otherwise (Open_Gaps: two file headers say second witness, October 2026).

**Sixtus V, Clement VIII, Gregory XV and the Congregation.**
- *Visibility:* One act each. The *Immensa* of 1588 founds the fifteen Congregations. The bull of 1595 receives the Ruthenian bishops. *Inscrutabili* of 1622 founds Propaganda (rows 14, 72, 17).
- *Representativeness:* They speak for the machinery of government and the mission office.
- *Influence:* The Congregations lasted. The Collectanea shows the new office issuing decrees to orders within four years of its founding (row 17).
- *Limitations:* The Collectanea is a printed collection of 1907, not the archive. The *Immensa* text is column-interleaved in the scan.
- *Transmission History:* The Bullarium is a Luxembourg reprint. The Collectanea was printed at the Propaganda press in 1907. The bull of 1595 reaches us in Theiner's Vatican-archive edition of 1863, whose editor was an Oratorian and Prefect of the Archives (header of row 72).

**Charles Borromeo (1538 to 1584).**
- *Visibility:* High. He is named in the Breviary, in four Lives and a canonisation summary, in the Council's last period and in his own Acta.
- *Representativeness:* He speaks for one great archdiocese and, in the Catholic world's memory, for the model Tridentine bishop. The Lives and the Breviary make him exemplary.
- *Influence:* How widely other dioceses adopted the Acta is not tested on this shelf. Doc_01 §1 calls his role as the Pope's agent in Rome Widely Accepted. Giussano states it, and Pallavicino's footnotes cite the legates' letters to him (rows 34, 51). That is two witnesses of different kinds. Both are partisans.
- *Limitations:* The Lives are hagiography. His own Italian letters were printed in 1762 and 1763 by anti-Jesuit editors who chose them for what they show of his dealings with the Jesuits (rows 29, 31). The Acta are his legislation, not his practice.
- *Transmission History:* The Acta were collected and edited at Federico Borromeo's order (the title page has "I V S S V", line 72) and printed at Milan in 1599, with a dedication by the Oblates (row 28). Giussano's Life appeared in 1610 and reaches us in an English of 1884 by the Oblates of St Charles, Westminster, and in an Italian reprint of 1855 (rows 34, 36). The Instructions of 1577 also exist as a separate print (row 113). Voelker's English of 1976 is in copyright and access-restricted, on the dossier's word (row 84).

**Robert Bellarmine (1542 to 1621).**
- *Visibility:* Two late devotional works, each in two English versions: four files in all (rows 41 to 44). His controversial work is not on the shelf.
- *Representativeness:* One cardinal's contemplative practice. The 1925 Preface calls the *Ascent* "the fruit of one of the great man’s annual retreats" (line 207).
- *Influence:* The Preface calls him "the most famous of Papal controversialists" and says these works stand apart from the controversy. Whether they shaped others was not tested.
- *Limitations:* Two works by one man. A search of the four files for the Council's name finds nothing, which fits Doc_01 §4 Test 2 (the works were not written to teach or enforce a decision). The 1925 translator is "a Religious of the English Church", an Anglican. The tract filed under his name is an Anglican refutation of his *Notes of the Church* (row 46). The Foxton volume binds an essay by Addison (row 45).
- *Transmission History:* *De ascensione* (1615) reaches us in Hall's English of 1703 and in the English of 1925. *De aeterna felicitate* (1616) reaches us in Foxton's English of 1722 and in Dalton's, whose preface carries Bellarmine's own words linking the two works (row 43). Whether the second strand of Doc_01 §4 is real is for Doc_04.

**The Roman Catechism.**
- *Visibility:* One text, long and orderly.
- *Representativeness:* It speaks for the Council's commissioners and for the priests it was written for (row 10). It does not show what the people were taught in practice.
- *Influence:* Session XXIV orders a catechism in the vernacular for the people (row 3). Giussano says Borromeo made the observance of the decrees his principal care (row 35).
- *Limitations:* The English is a translation with an apologetic Introduction and footnotes by two Dominicans (row 11). The Latin original is not on the shelf.
- *Transmission History:* Issued under Pius V. English by McHugh and Callan. The title page reads "SECOND REVISED EDITION" (line 72) and "SIXTH PRINTING, SEPTEMBER, 1937" (line 73), and the imprint carries a copyright notice of 1934 (line 110). The imprimatur is dated "DIE 3 JANUARII, 1923" (line 107), earlier than the copyright notice, so it appears to be carried over from the first edition of 1923; the shelf does not say so. Whether the revision changed the text at the passages quoted cannot be told from the shelf. The file header's rights line describes a 1923 publication and not this printing (Open_Gaps: the Catechism edition and its rights basis, October 2026).

**The Missal and the Breviary.**
- *Visibility:* The prayer of the Church. The Missal is complete; the Breviary is one volume of four.
- *Representativeness:* They speak for the whole Latin Church's worship. Bute's Breviary is a revised book, so it speaks for the Church after Pius V as well (row 24).
- *Influence:* Pius V's bulls make them binding (row 12).
- *Limitations:* The Missal is a lay edition of 1843. The Breviary is one season. The file does not say when the lessons for Borromeo entered the book.
- *Transmission History:* The Missal is the English of the Right Rev. Dr. John England, with a copyright notice of 1843 entered in Pennsylvania (front matter, lines 174–177). The Breviary is Bute's of 1908, whose title says it was revised under Clement VIII, Urban VIII and Leo XIII.

**Luis de Granada (1504 to 1588).**
- *Visibility:* One manual, long.
- *Representativeness:* A Spanish Dominican's meditations on the mysteries, for the English Catholic laity of the Inns of Court (row 47).
- *Influence:* The Library calls it the most widely read Catholic devotional book of the later sixteenth century; that claim is the Library's and was not tested.
- *Limitations:* The voice is the translator's English, and the translator's name rests on a garbled dedication. The Spanish is not on the shelf.
- *Transmission History:* Spanish to English by Hopkins, printed at Paris in 1582 for the English recusant market (row 47).

**Philip Neri (born 1515).**
- *Visibility:* Through Bacci's Life only (row 48).
- *Representativeness:* The Oratory's account of its founder. Volume I stops at Chapter VI of Book III.
- *Influence:* Bacci shows Borromeo and Gregory XIII giving money for the Oratory's church.
- *Limitations:* Tier 3. The prospectus is Faber's. The Italian original is not on the shelf.
- *Transmission History:* Bacci, a priest of the Oratory, wrote in Italian; Faber's series gave the English in 1847.

**Reginald Pole (1500 to 1558).**
- *Visibility:* Waterworth's essay names him as the author of the exhortation read at Session II (row 5).
- *Representativeness:* A legate and cardinal.
- *Influence:* Presiding legate at the Council's opening.
- *Limitations:* His one oration on the shelf cannot be read (row 49).
- *Transmission History:* An English translation of 1560, printed in a hostile frame, in a garbled scan. His letters are in Latin and Italian only (row 83).

**Sarpi and Pallavicino.**
- *Visibility:* The two long narratives of the Council, one in English, one in Italian.
- *Representativeness:* Sarpi is a Servite friar writing against the Curia from inside the Church (Step 0 §4 item 2). Pallavicino is a Jesuit cardinal answering him.
- *Influence:* Each answers the other. Both agree on some facts of the close and disagree on their meaning (§3).
- *Limitations:* Neither was at the Council as a Father. Each writes long after it.
- *Transmission History:* Sarpi first appeared in London in 1619 under a pseudonym; the vendored English is the 1676 reprint with a Protestant dedication (row 50). Pallavicino is vendored in the 1664 print and the clean 1846 reprint (rows 51 to 54).

**The opponents: Jewel, Marnix and Barlow.**
- *Visibility:* Three Protestant voices, each aimed at Rome, none at the Church's own formation.
- *Representativeness:* A bishop of Salisbury (1562 to 1564), a Dutch Reformed satirist (1569) and an Anglican bishop (1681).
- *Influence:* They show how the Council looked from outside (rows 55, 57, 22).
- *Limitations:* All are polemics. Barlow's is after the window.
- *Transmission History:* Jewel in Lady Bacon's English of 1564 as edited in 1888; Marnix in a Dutch edition of 1858 and Gilpin's English; Barlow in 1681.

**The Jesuit, Carmelite and Eastern witnesses.** These voices belong to other worlds and are heard here at one point each. Lainez arrives at Trent on 13 August 1562 in a household letter (row 68). Teresa names the Council's decree on hermits (row 59). A cardinal writes of an Eastern patriarch's profession (row 25). A Ruthenian bishop swears the Tridentine Profession's closing words (row 72). None speaks for this world.

## 3. Secondary Scholarship Assessment

The secondary matter on the shelf is by editors and translators, all writing between 1847 and 1934. It comprises Waterworth's essays (1848), Faber's prospectus (1847), the Giussano preface by Cardinal Manning (1884), Schaff's notes (1878), Gibbings's notes (1853), Reusch's introduction (1886) and the McHugh and Callan Introduction (first published 1923, here in the revised edition of 1934). The editors are Catholic, or are described as Catholic by the Library, except Schaff and Gibbings. No modern specialist work is vendored. The works that a specialist would name are listed in the Registry and not vendored: Jedin (row 104), Hsia (row 105), Pastor (row 114), O'Malley (row 102) and de Boer on Borromeo (row 106). Claims below rest on the primary texts and on the editors, and are marked accordingly.

**1. Was Trent a reply to Luther or an internal reform? The Council states both aims. Documented for the stated aims.** Doc_01 §2 tags the existence of a pre-1517 reform current Widely Accepted and its own characterisation of it Inferential-Thin, pending this document. The Council's own words give both aims. Session III names "the extirpating of heresies, and the reforming of manners, for the sake of which chiefly it is assembled" (lines 12321–12323) (row 1). Pius IV's bull of confirmation gives the same two: "To extirpate very many and most pernicious heresies, to correct manners, and to restore ecclesiastical discipline" (lines 24208–24210) (row 4). That the Council stated both is Documented. How much of the reform current was independent of Luther is not tested on this shelf, because no pre-1517 reform text is vendored. The shelf holds no source that states a scholarly dispute on the point, so nothing here supports a Contested tag. Doc_01's tags stand: Widely Accepted for the existence of the current and Inferential-Thin for its characterisation.

**2. The Bishops' residence and the source of episcopal power. Documented as an unresolved dispute.** Waterworth's essay reports that "fifty-three supported the demand of the Archbishop of Granada" (lines 9378–9379), that Lainez's reasoning impressed the congregation most, and that the Legates were directed "to abstain from defining it to be of divine right, in opposition to the opinions of so many of the prelates" (lines 9846–9848) (row 5). The shelf holds one narrator of this debate, a Catholic editor. Sarpi and Pallavicino also treat it and were not read for it (rows 50, 52 to 54).

**3. How is *Regnans in Excelsis* attested? Documented, in two witnesses.** The Bullarium prints the Latin under the heading "Damnatio & excommunicatio Elifabeth Reginz" (line 85366) (row 13). Barlow prints English and Latin columns (row 21). Both give the claim that the Church was entrusted to Peter's successor "in poteftatis plenitudine". The year 1570 is in the page margin of the Bullarium. A margin note near the bull reads "Dar. P. A. c. die 25. Febr." (lines 85574–85575). The columns of the page interleave, so which constitution the note belongs to is not certain, and the day is not established from this file.

**4. The close of the Council. Documented for the facts; Contested for their meaning.** Four sources speak.
- Waterworth's decrees record the acclamations, with the speaker named as "The Cardinal of Lorraine. To the most blessed Pius, Pope, and our lord" (lines 24035–24036), the cry "Cardinal. Anathema to all heretics." (line 24103), the answer "Answer. Anathema, anathema." (line 24105) and the number of signatories (row 4). The Session was "terminated on the fourth day of December" (lines 21863–21864) (row 4).
- Waterworth's editor says the acclamations were led by the Cardinal of Lorraine, who also had composed them, and that the historians who were eye-witnesses "represent the Fathers as filled with joy at the conclusion of their labours" (lines 11136–11138). He quotes a diary for the tears, which were "per gran letitia", for great joy (row 5).
- Sarpi writes: "The Cardinal of Lorain took upon him to be the chief, not*only to compose the acclamations, but to thunder them out also" (lines 70194–70196). He adds that this was construed as a lightness and vanity not becoming a prelate, and that Rome feared the Pope's death during a Council (row 50).
- Pallavicino's Argomento for Book XXIV reports the Pope's illness and the Legates' haste: "Diligenze perciò de’ Legati a fin d’ accelerar la sessione" (lines 53240–53241) (row 51).
That the Cardinal of Lorraine led the acclamations is Documented in the decrees' own text. That he composed them is Documented as the editor's statement and as Sarpi's, from opposite sides. That the Pope was ill and the Legates hurried is Documented as Pallavicino's and Sarpi's statement. Whether the haste was a rush or a prudent closing is Contested between the two histories.

**5. The census story "The Last Day at Trent". The tears are attested, with a different source and a different cause.** The census says the secretary Massarelli's diary supplies the tears and the haste. The shelf has no Massarelli (row 82). The tears are in a footnote that quotes another diary, as tears of joy (row 5). The haste is in Pallavicino and Sarpi. The census's attribution to Massarelli is not supported on this shelf: no Massarelli text is vendored, and that is an absence and not a confidence level. The census marks the story "from reference summaries; primary text not yet read".

**6. The reformed books. Documented.** The Council's Session XXV orders the work on the Index, the Catechism, the Breviary and the Missal (row 4). Pius V issued the Breviary bull in 1568 and the Missal bull on the day before the Ides of July 1570, 14 July by the calendar (row 12). Doc_01 §4 Test 3 says both books follow the Council's mandate. That is now Documented from the bulls themselves.

**7. Jewel's charge of pluralism. Documented that the decree exists; Contested whether Rome kept it.** Jewel says that the Council ordered that one man should not hold two benefices at one time and that Rome gives a man several (row 55). Session VII, Chapter IV is headed "The retainer of several Benefices contrary to the Canons shall be deprived thereof" (lines 14355–14357) (row 3). The shelf has no evidence on practice.

**8. Was Borromeo the Pope's executor for the Council? Widely Accepted, now with two witnesses.** Doc_01 §1 says the Rome-based executor role is Widely Accepted and unchecked. Giussano says "The special superintendence of the acts of the Council was entrusted by the Sovereign Pontiff to his nephew Charles." (lines 3655–3657) (row 34). Pallavicino cites the legates' letters to Borromeo throughout his footnotes (row 51). Both are partisans.

**9. Bellarmine's retreat. Documented as the translator's statement.** The 1925 Preface says *De ascensione* is "the fruit of one of the great man’s annual retreats" (line 207). Bellarmine's own preface to the second work opens: "LAST year, for my own spiritual benefit especially, I composed a 'Gradual to ascend unto God from the Contemplation of created objects.'" (lines 94–97) (rows 41, 43).

**10. The Jesuits inside the Council. Documented.** Doc_01 §1 rests on Waterworth. Lainez's own household letter from Trent confirms that he arrived on 13 August 1562 (row 68).

**11. The Catholic dating of the "Protestant Rebellion". Carried.** The translators' Introduction dates it from 1520 in a footnote (row 11). Doc_01 dates the controversy from 1517. The two are not the same and the difference is a translators' remark, not a source.

**12. The cross-world relations that Doc_01 §7 item 6 names.** Step 0 of Lutheran Wittenberg (VI.1) describes the Tridentine Church as "the direct doctrinal target of, and respondent to, this movement" and expects Doc_02 of each world to cite the other as the primary named rival (`Build/worlds/witt/Step0_Movement_Scope_Confirmation.md`, §2 A3). Step 0 of the Reformed cities (VI.2) names the Tridentine Church twice in §3 B3 (`Build/worlds/rzg/Step0_Movement_Scope_Confirmation.md`). The first time is in its list of worlds with no figure overlap. The second time it says that the Tridentine Church's own decrees, once vendored, "will almost certainly need to be read directly against this candidate's own confessional documents, the same 'direct doctrinal rival' relationship Lutheran Wittenberg's own Step 0 names for its own relationship to Trent". The sources for the Lutheran and Reformed side are not on this world's shelf, and this world does not borrow them.

## 4. Formation Narrative Sources

Tier labels follow the Framework's four-tier scheme.

- **The Lives of Borromeo.** Giussano (rows 34 to 36), Possevino, Valier, Bascapè and Peña (rows 38, 39, 37, 40). Tier 3, attributed tradition, for the formation portrait. They were written by the saint's household and fellow bishops and by an official of his cause. Peña's work is a summary of the life and of the canonisation, and is counted with the Lives here. Giussano's Book VIII is a thematic treatment of Borromeo's virtues, and Book IX treats his miracles (row 35). Tier 3 also for the miracles and the canonisation procedure. The 1604 to 1610 process itself is not on the shelf.
- **The Breviary's lessons for 4 November.** The Church's own liturgical narrative of Borromeo (row 24). Tier 3 for the formation portrait. Tier 1 as the text the Church read aloud. The file does not give the date the lessons entered the book.
- **Bacci's Life of Philip Neri.** An Oratorian's Life (row 48). Tier 3 for the portrait, Tier 1 for dated events such as his ordination as priest on 23 May 1551 (lines 2024–2025). Faber's prospectus is a convert's apologetic of 1847.
- **Bellarmine's prefaces.** The two prefaces are Bellarmine's own statements about his own work (rows 41, 43). Tier 1 for what he says of himself.
- **Granada's translator's epistle.** The translator's account of why the book was made (row 47). Tier 1 for the translator's purpose.
- **The Council's own narrative of its close.** The acclamations and the signatories (row 4) are Tier 1 documents. The editors' account of the joy and tears is Tier 2, collected material.
- **Sarpi and Pallavicino.** Narrative histories (rows 50, 51). Tier 2 for the events both report; Contested for the attributions of motive.
- **The Inquisition sentence of 1564.** A Roman record (row 27). Tier 1 for the sentence; the editor's notes are an opponent's.
- **The stories the census names.** "The Last Day at Trent" can be told from the decrees, Sarpi and Pallavicino, with the difference in §3 item 5. "The Primate of Spain in the Inquisition's Prison" has no primary source on the shelf: the process, the Commentary and the studies are not vendored (rows 97, 98). Two narrators touch it. Pallavicino writes in Book XXI: "Stava carcerato già da molti anni nell’inquisizion di Spagna frate Bartolomeo Carranza domenicano arcivescovo di Toledo" (lines 34962–34965), and that "Ora i vescovi del concilio, avvisandosi che nella prigionia di quel gran mitriato sotto altro tribunale che del sommo pontefice, tutto l’ ordine loro rimanesse avvilito" (lines 34967–34971) (row 51; the passage repeats at lines 36812–36820). Sarpi says the Deputies for the Index, having given Carranza's work to divines to be censured, were told that nothing worth censure was in it, and that the Congregation approved it, in a passage the scan partly garbles (row 50, lines 65034–65046). He places the approval with the Index deputies and their Congregation, not with a session of the Council. The census states that Trent's approval of the Catechism is in the council's records; that is not on the shelf in a primary text. "Twenty-Eight Names in a Book at Brescia" has none: Merici's Rule is not found (row 93). Both stay at "from reference summaries; primary text not yet read".

## 5. Material Culture and Daily Life Sources

- **Vendored:** no archaeology, no building record, no object, no image. The census's "experience today" is the Museo Diocesano Tridentino in Trento. The shelf has nothing on it.
- **Prescribed objects in the texts.** The Acta prescribe a confessional for every parish church, two where the cure is over 400 souls, and give the height, the confessor's seat and the penitent's kneeler (row 28). The Instructions of 1577 cover churches, altars, fonts and vestments (the title: "ET SVPELLECTILIS ECCLESlASTlC AE ." (line 90273)). Session XXIII orders seminaries (row 3). The Missal and the Breviary prescribe the rites and the hours (rows 23, 24). These are instructions, not records of use.
- **Institutional action.** Bacci records that Borromeo gave the first money for the church of the Oratory at the Vallicella, and that Gregory XIII and cardinals followed (row 48). The Collectanea shows the Congregation ordering annual reports from mission prefects (row 17).
- **Punishment.** The sentence of 1564 records the Holy Office at work on a friar. The title page says he was to be walled up (row 27). The editor's notes say it is Protestant evidence against Rome.
- **Social background.** The reception of the decrees is told by Teresa for hermits and endowments (row 59), by Pius V's letters to bishops (row 16), and by the Jesuit household letter (row 68). All are clerical.
- **Lay use.** The lay Missal of 1843 and Granada's English of 1582 show books made for lay readers. Neither records a reader.
- **Social roles attested for a Representative.** A bishop (Borromeo, in his Acta and Lives); a parish priest (the Catechism's reader, the Acta's confessional rule); a cardinal-writer (Bellarmine); a founder of an Oratory (Philip Neri); a legate (Pole, the presiding legates); an inquisitor's notary (the 1564 sentence); a cardinal-historian (Pallavicino). No lay role speaks.
- **The gap is stated, not filled.** The daily life of a parish, a seminary, a confraternity, a school of Christian doctrine or a convent cannot be reconstructed from what is vendored. Visitation records and rosters are absent (Open_Gaps: voices the shelf lacks, October 2026).

## 6. Source Asymmetries and Missing Voices

Under Article 20 the primary duty is to name whose voices the sources structurally omit, and why.

**Overrepresented:** Rome and its curia; bishops and cardinals; Latin and Italian; the Council's own decrees; one saintly bishop (Borromeo has an Acta, four Lives, a canonisation summary and a Breviary feast); Catholic editors and translators of 1847 to 1934.

**Structurally missing, and why:**

- **The laity.** Parishioners, confraternity members and the children of the schools of Christian doctrine appear only as the objects of instruction. The shelf's genres (acts, bulls, rules, Lives, histories) are clerical. The nearest traces are Granada's English readers at the Inns of Court (row 47) and the lay Missal of 1843 (row 23), and neither records a reader.
- **Women.** The census names Angela Merici and the Ursulines as a voice. Her Rule is not found and no text of the Ursulines is on the shelf (rows 93, 79). Women appear on the shelf as hearers, objects, scribes and translators. A countess hears Philip Neri's jest about the Madonna (row 48, lines 4744–4750). Queens are subjects of negotiation in Pallavicino's Argomento for Book XXIV, which names "la reina di Francia" and "la reina di Scozia" (row 51, lines 53231–53232). Angelica Agata Sfondrati wrote down Borromeo's sermons (row 33). Lady Anne Bacon translated Jewel (row 55). Teresa is the one woman's voice, and she is held to her own world (rows 59 to 63).
- **The condemned.** Fra Tommaso de Fabianis is heard only through the sentence against him (row 27). The authors on the Index appear, if at all, as titles in a noisy scan (row 19).
- **Protestants in their own words.** No Lutheran or Reformed text is on this shelf. Jewel and Marnix speak against Rome, in one case in a translator's English (rows 55, 57). Barlow speaks in 1681, after the window (row 22). Sarpi speaks from inside the Church (row 50). The Lutheran and Reformed sources belong to Wittenberg (VI.1) and the Reformed cities (VI.2) and are not borrowed here.
- **The Eastern churches.** The Church of the East appears through one Roman cardinal's letter and a patriarch's profession that is held to another world (rows 25, 26). The Ruthenians appear through one papal bull and the closing words of one bishop's oath (row 72).
- **The peoples of the missions.** No convert, catechist or ruler speaks. The mission appears as instructions from Rome and a letter to the Archbishop of Goa (rows 17, 16).
- **The Spanish Church and its Inquisition.** Carranza, the Spanish Inquisition and Spanish Catholicism are present only through Pallavicino's and Sarpi's remarks (§4) and through Teresa's two passages. Granada reaches us through an English translator.
- **The orders beyond the Jesuits and the Oratory.** The Capuchins have one decree of 1626 (row 17). The Ursulines and the other new orders are absent, or are held to other worlds. The Oratory speaks through Bacci's Life of its founder (row 48).
- **The princes.** The Emperor, the French and Spanish kings and the Catholic princes speak only as the Council's text addresses them, and through the three narrators of the close (rows 4, 50, 51).
- **Dissent inside the Church.** Sarpi is present. Seripando, Carranza and the Spanish bishops who pressed residence as of divine right are present only in Waterworth's essay and in Pallavicino's footnotes.

**The gap in time and in voice, stated plainly.**

1. **1517 to 1545.** Doc_01 §2 flags 1600 to 1650 as the thin end of the window. The first third of the window is thinner. The only text on the shelf from these decades is Paul III's bull against Henry VIII, printed in Latin in Barlow's volume and not dated in the lines read (row 21). Bacci's Life of Philip Neri covers his life from his birth in 1515 (row 48). Waterworth's essay narrates the years before the Council at second hand (row 5). There is no Leo X, no Clement VII, no text from Luther's first decades, and no pre-1517 reform text. The Hussite and Lollard precedents that Doc_01 §2 names are in other worlds.
2. **1545 to 1563.** Dense. The decrees, the Profession, Pole's exhortation at second hand, the Jesuit letter from Trent, the Cardinal of Lorraine's acclamations, and two narrators of the whole Council.
3. **1563 to 1600.** Dense on the papal side. The Bullarium runs from Pius IV to Innocent IX (to 1591). Pius V's letters, the Catechism, the Breviary and Missal bulls, *Regnans in Excelsis*, *Immensa*, the Acta of Milan and the Lives of Borromeo, the Granada of 1582 and the Index of 1564 are all here.
4. **1600 to 1650.** Thin. Bellarmine's two works of 1615 and 1616, and the Collectanea's entries from 1622 to 1650, are the shelf. The Bullarium for these decades (Tomus Tertius), the Rituale of 1614 and the Capuchin annals of 1641 are on archive.org and not vendored (rows 77, 110, 112). No lay, episcopal or parish text from the first half of the seventeenth century is on the shelf. The institutional developments Step 0 names for this period are present only as follows: Propaganda by its founding bull and decrees of 1626 (row 17); the Index by sixteenth-century texts only; the Roman Inquisition by one sentence of 1564; the new orders by the Oratory's Life of its founder; and no Greek College.
5. **Personal and pastoral voice.** This is now substantially filled, as Step 0 and Doc_01 say, but with these limits. Borromeo's own voice in Latin is the Acta, a body of legislation, and not personal writing. His Italian letters, counsels and sermons are held as context pending the project lead's ruling. Bellarmine is one cardinal's retreat. Granada is a translator's English. Philip Neri is a hagiographer's report. Pole cannot be read. The Missal and Breviary are public prayer, not private. No priest at a parish speaks.
6. **What this means for the world.** A Representative built on this shelf would have a full doctrinal and institutional voice for 1545 to 1600, a papal voice to 1591, an episcopal voice in Borromeo's legislation, and a devotional voice in Bellarmine, Granada and Bacci. It would have no lay voice, no woman's voice of its own, almost nothing before 1545, and almost nothing after 1600 beyond Bellarmine and the Congregation's decrees. Doc_02 does not fill these gaps from the census or from memory.

**Forces lens (Forces Framework Step 2).** The forces are those of Doc_01 §5: the Reformation and the fracture of Western Christendom (Cell 1A); the internal-reform pressure that predates Luther (Cell 1B); confessional politics across the window (Cell 2A); the Council's three-session structure and its internal debates (Cell 2B); Cell 3A left open; and *Regnans in Excelsis* with its practical failure (Cell 3B, placement provisional for Doc_08, with Cell 2A the alternative).

*Which sources speak to external forces.*
- The Reformation (Cell 1A). The Council's four anathemas answer named claims (row 2). The Session XXV decree on receiving the decrees says the Synod condemned "the principal errors of the heretics of our time" (row 4). The Catechism's preface says that "false prophets have gone forth into the world" (lines 2832–2833) and that false catechisms were circulating (rows 10, 11). Jewel and Marnix answer from the other side (rows 55, 57). No Lutheran or Reformed text is in this world's own evidence.
- Confessional politics (Cell 2A). The Session XXV decree asks princes to protect the decrees from corruption by heretics (row 4). Pallavicino's Argomento for Book XXIV lists the Pope's instruction on the Council, the Queen of France's wish for a colloquy, the Queen of Scots' marriage and the alienation of church goods (row 51). Sarpi's Dedicatory charges the Roman bishops with a purpose "to weaken the lawful Rights of Kings and Princes" (lines 364–365) (row 50). Jewel complains that German divines were "quite shut out" (row 55).
- England (Cell 3B or 2A). *Regnans in Excelsis* in two witnesses, and Barlow's hostile frame (rows 13, 21, 22); Jewel's refusal to attend (rows 55, 56).
- The East. A Roman cardinal's letter on an Eastern patriarch, and a bull and oath for the Ruthenians (rows 25, 72).
- The missions. *Inscrutabili* and the decrees of 1626 (row 17); Pius V's letter to Goa (row 16).

*Which sources speak to internal forces.*
- Pluralities and residence (Cell 1B, Cell 2B). Session VII, Chapter IV (row 3); the essay on the residence dispute (row 5); Pius V's letters pressing the decrees (row 16); Jewel's charge (row 55).
- The orders and the new office. The Congregation's decree of 24 July 1626 complains that superiors of regulars obstructed missionaries (row 17).
- The Holy Office. The sentence of 1564 and the Council's bishops' complaint about the Spanish Inquisition's hold on Carranza (rows 27, 51).
- Jesuits and bishops. Borromeo's Italian letters on the Jesuits are held as context pending the project lead's ruling (rows 29, 31).

*What the silences show.*
- The two forces that made the world, Luther's challenge and the older reform current, are heard only through the Church's replies and its opponents' polemics. The shelf has no text from before 1517 and no Protestant text in the Protestants' own words.
- The Council's debates are heard through a Catholic editor, a hostile friar and a partisan cardinal. The acts themselves exist and are not vendored (rows 81, 82).
- The Index and the Holy Office appear as structure and as one sentence. How either worked in a diocese or a city is not on the shelf.
- No source has economic conditions as its subject. Pallavicino's Argomento lists the alienation of church goods as a topic (row 51). Whether any vendored book treats the funding of seminaries and missions beyond passing mention was not read.
- The Turkish threat appears in the 1640 editor's dedication to Pius V's letters, not in a text of the window (row 16).

*Survivorship patterns.*
- The Church printed its own acts. What survives is what the Church, its presses and its Catholic editors kept: the Council's decrees, the bulls, the Catechism, the Missal, Borromeo's Acta compiled in 1599, the Bullarium reprinted in the eighteenth century.
- The editors chose. Schaff leaves out the reform decrees (row 6). The Bullarium volume prints constitutions with the editors' scholia (row 15). Pius V's letters are a collection first printed in 1640 (row 16). On the file headers' account, the Italian letters of Borromeo were selected in 1762 by anti-Jesuit printers, and the printer says some letters were left out (rows 29, 31).
- Opponents preserved what they attacked. *Regnans* is in a hostile printing of 1681 as well as in the Bullarium (row 21). Pole's oration survives inside a hostile frame, garbled (row 49). Sarpi survives with a Protestant dedication (row 50).
- The pressure that shows most is therefore papal and doctrinal, because the Church's own archive and press kept the letters and bulls that carry it. This is an effect of what survives. It is not a finding that Rome or heresy was the most threatening force.

**Evidential visibility is not ecological visibility.** The world's most formative work was likely the sermon, the confessional, the catechism class, the seminary and the Mass said at a parish altar. The shelf's evidence is the Council's decrees, the popes' acts, one bishop's legislation, three devotional voices and some narrators. Reconstruction that reaches past the evidence is marked Inferential-Thin. A bounded reconstruction of any marginalised voice needs a specific textual trace and is not attempted here.

## 7. Required Disclosure

Doc_01 §7 carries eleven binding or disclosure items for Doc_02. Each is addressed in turn.

**1. The personal and pastoral voice (Doc_01 §7 item 1; Step 0 §4 item 1).** Cited directly in §1 and §2. Pole is vendored and cannot be read: the 1560 scan is garbled at every line sampled, so the item stays a second witness (row 49). Borromeo's Latin Acta count as his primary voice directly under the Library ruling of 25 September 2026 (row 28). The Breviary is one of four seasonal volumes, the Autumn volume (row 24).

**2. Sarpi's status (item 2; Step 0 §4 item 2).** Sarpi was a Servite friar and priest who stayed in the Church and wrote against the Curia. The vendored volume is the English of 1676 on Brent's translation, with a Protestant Epistle Dedicatory that is not Sarpi's. The hostile and contested register governs citation (row 50). The file does not give the date of Brent's translation.

**3. The liturgical books (item 3; Step 0 §4 item 3).** The Roman Missal is vendored whole, as a lay English edition of 1843, with the Latin beside the English (row 23). The Breviary is the Autumn volume of four, in a book revised after Pius V (row 24). Neither is a pure text of 1568 or 1570. This document does not say there is no pastoral or interior voice.

**4. The Trent and Society of Jesus split (item 4; Step 0 §4 item 4).** The corpus map holds Waterworth as `tradition` here and `context` for the Society of Jesus. This document applies that (rows 1 to 5). It also records that Jesuit voices inside the Council are on this shelf through Waterworth's essay and one Jesuit letter (rows 5, 68). The Society of Jesus Doc_02 holds Waterworth as `context` on its side of the split (`Build/worlds/jes/Doc_02_Source_Ecology.md`, §7 item 3), and notes that Sarpi's History names Lainez and Salmerón and counts the matches without reading them (the same document, §3 item 6).

**5. The Borromean Milan boundary (item 5; Step 0 §4 item 5).** The corpus map holds Borromeo's Acta here as `tradition` and as `tradition` for Borromean Milan. It holds his five Italian files here as `context` and for Borromean Milan as `tradition`, and the Lives here as `context`. This document does not decide which world owns Borromeo's voice. The Library decision log lists "which world owns Borromeo's voice (VI.12 or VI.22)" among the placements left for the project lead (entry "Era VII library pass: scope, corpus size, and placements left to Mark") and has no entry that answers it. The nearest records are two. The entry "Era VII rulings after the two library passes (Mark, six decisions)" sends the build-recommended worlds into Steps 0 to 2 and does not rule on Borromeo. The entry "A voice may belong to several worlds of the same era; Tatian is co-owned" records the words "it doesn't have to be just one" and is read by the Library as a ruling on Tatian and on figures that share Tatian's shape. The Tridentine dossier ends its reading "A ruling for Mark", and the Borromean Milan dossier passes the question on. The Registry therefore holds the Acta Native, as the map has it. It holds the five Italian files Native but as context and not licensed for this world's Representative, which keeps them dual-placed until the ruling. It holds the Lives Native as formation narrative, which departs from the map's `context` (item 15). The question is routed to the project lead (Open_Gaps: no record of the Borromean Milan placement, October 2026).

**6. Lutheran Wittenberg and the Reformed cities (item 6; Step 0 §4 item 6).** Cross-referenced in §3 item 12 and in the forces lens of §6. Step 0 of Lutheran Wittenberg (§2 A3) names the Tridentine Church as its direct doctrinal target and respondent. Step 0 of the Reformed cities (§3 B3) names it twice: once among the worlds with no figure overlap, and once as a direct doctrinal rival whose decrees will need to be read against its own confessional documents. This document cites both and borrows the sources of neither.

**7. The unattributed selection rationale and the window (item 7; Step 0 §4 item 7).** The batch-selection narrative has no findable record outside Step 0. This document does not use it as an argument. The window is Doc_01's 1517 to 1650, and §1 and §6 test the shelf against it.

**8. Dossier staleness (item 8).** Doc_01 §7 item 8 lists five stale points. The dossier has since been revised. Its October 2026 update corrects Pallavicino, Borromeo's voice and Pole, and its §1 now lists the Waterworth text as `tradition`. Its §6 now says the floor clears from Trent's Session III recital and notes the filioque. Three points remain stale:
- The dossier §1 still describes the merged bucket as twenty-one files. The bucket now has 64 rows over 59 files (Open_Gaps: corpus-map change requests, October 2026).
- Dossier §5 says *Regnans in Excelsis* "exists only through Barlow". The Bullarium prints it (row 13).
- Dossier §4 closes Theiner's *Acta genuina* because no English exists. The Latin is on archive.org and a Latin original can be primary evidence (row 81).

**9. The EEBO-wide rights re-check (item 9; Step 0 §3 B1).** Still outstanding. No document in the record reports it. Step 0 reports a positive item-specific check on Pole. Other files on the shelf that come from the Early English Books microfilm collection rest on public domain by date: Granada (1582), Sarpi (1676), Pole (1560), the Marnix English (1623), Canisius (1622) and the Anglican tract filed under Bellarmine (1688). Hall's English of 1703 and Foxton's of 1722 come from the sibling eighteenth-century series on archive.org (the same `bim_` microfilm family) and rest on the same basis, so the re-check covers them too. Each Registry row states the rights line of its file header and does not claim a wider check (Open_Gaps: the EEBO-wide rights re-check, October 2026). The Catechism file raises a separate rights question: its header says published 1923, and the title page is the revised edition with a copyright of 1934, which is public domain in the United States only if it was not renewed. Rows 10 and 11 are used pending the Library's check (Open_Gaps: the Catechism edition and its rights basis, October 2026).

**10. The *Notes of the Church* (item 10).** The file filed under Bellarmine's name is an Anglican refutation of his work, an opponent's voice. It is Excluded as a Named Comparandum (row 46). This document cites only the four genuine Bellarmine files (rows 41 to 44). A related point: Doc_01 §4 says the Foxton title page reads "Being, a Practical Discourse Concerning the Eternal Happiness of the Saints in Heaven". That wording is in the Library's header for the file. The scanned title page is illegible (row 44; Open_Gaps: quotations in Doc_01 that differ slightly from the scan, October 2026).

**11. Living Tradition Status (item 11).** PENDING the project lead's confirmation, as Doc_01 §1 states. It does not block Doc_02. This document does not self-confirm it. Under Articles 28 and 29 it notes one consequence of the status for sources: the Church's own voice on the shelf in English reaches us through Catholic clergy of the nineteenth and twentieth centuries (Waterworth, McHugh and Callan, Bute, England, Faber, the Oblates of St Charles). The census entry for VI.22 carries `living: False`; Doc_01 records the status as pending (Open_Gaps: Living Tradition Status is outstanding, October 2026). The living tradition's editors are therefore part of the transmission of the historical world.

**12. The 1659 Instruction is outside the window.** The famous Propaganda Instruction on accommodation is dated 1659. It is Excluded as Out-of-Boundary (row 18). It must not be cited as evidence of this world's practice.

**13. The Latin and Italian scans have not been checked against page images.** The Library's headers say wording must be checked against the page image before it is quoted. No page image was available. Every Latin, Italian and Dutch quotation here is verified against the scan text only, and keeps its f-for-s and its recognition errors.

**14. File headers that contradict the corpus map.** The headers of the Pius V letters (row 16) and the Acta (row 28) say the Latin is "a second witness, never primary evidence for a Representative". That contradicts the corpus-map notes and the Library ruling of 25 September 2026 that a clean Latin original is primary evidence. This document follows the corpus map. The Library is asked to correct the headers (Open_Gaps: two file headers say second witness, October 2026).

**15. Corpus-map placements this document does not follow.** Where a bucket row says `context` and the Registry says Native, or the reverse, the Registry's Boundary Status follows Doc_01's boundary and the file's own subject, and not the bucket's role. The differences are listed in Open_Gaps: corpus-map change requests, October 2026. They include the Lives of Borromeo (`context` in the map, Native here as formation narrative), the Teresa files, the Glostrup and Slavata files, and the profession of Abdisho IV. The five Italian Borromeo files match the map: `context` here.

**16. Statements in Doc_01 that this document overtakes, and quotations that differ from the scan.** Doc_01 is Approved to proceed and is not reopened. Four statements are now out of date on the evidence of the shelf. Each is a candidate for a change order and is recorded in Open_Gaps: statements in Doc_01 that Doc_02 overtakes, October 2026. First, Doc_01 §5 (Cell 3B) says *Regnans in Excelsis* survives "chiefly through" Barlow and tags its 1681 transmission Documented; the Bullarium prints the Latin (row 13). Second, Doc_01 §2 says the years 1600 to 1650 are evidenced "by devotional material only"; the Collectanea adds the Congregation's decrees of 1622 to 1650 (row 17). Third, Doc_01 §2 says Propaganda Fide, the developed Index and the Roman Inquisition "have no vendored source"; the shelf holds the Propaganda decrees (row 17), the Index texts of 1559 to 1570 (row 19) and one Inquisition sentence of 1564 (row 27), though none for the Index or the Inquisition in 1600 to 1650. Fourth, Doc_01 §2 names the Catechism as "McHugh & Callan, 1923 English translation"; the vendored printing is the second revised edition of 1934 (row 10). Where a quotation in Doc_01 differs from the scan in a comma, a footnote mark or a small word, the difference is recorded in Open_Gaps: quotations in Doc_01 that differ slightly from the scan, October 2026.

**17. Schaff's Latin.** The Latin of the dogmatic decrees and of the Profession is the only Latin of the Council's text on the shelf. Its scan is noisy and the file is a second witness for the Latin (rows 6, 7).

## 8. Confidence Map

**Article 4 check.** The five commitments are quoted from Step 0's header, where they are quoted verbatim from the Constitution. Each result is stated at its own strength, against the Council's Session III recital of the Creed (row 1) and the Profession of Faith in Schaff's English and the 1734 English (rows 7, 8). The floor test is belief, not submission to a council.

| # | Commitment (Article 4, as quoted in Step 0) | Result | Strength |
|---|---|---|---|
| 1 | "One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen." | Shown. The Council recites "I believe in one God the Father Almighty, maker of heaven and earth, of all things visible and invisible", and the Profession opens with the same Creed. | Documented for the recital (row 1). |
| 2 | "Jesus Christ as the only Son of God, eternally begotten of the Father, God from God, Light from Light, true God from true God, begotten not made, of one Being with the Father." | Shown in substance. The Council recites the Son as "the only begotten Son of God, and born of the Father before all ages; God of God, light of light, true God of true God; begotten, not made, consubstantial with the Father". | Documented for the recital. "Consubstantial" stands for "of one Being". |
| 3 | "Jesus Christ as truly human — incarnate of the Holy Spirit and the Virgin Mary, 'became truly human.'" | Shown. The Council recites that He "was incarnate by the Holy Ghost of the Virgin Mary, and was made man". | Documented for the recital. |
| 4 | "Christ's death under Pontius Pilate, burial, bodily resurrection on the third day, ascension, and his return in glory to judge the living and the dead." | Shown in substance. The Council recites that He was "crucified also for us under Pontius Pilate", "suffered and was buried", "rose again on the third day", "ascended into heaven", and "will come with glory to judge the living and the dead". | Documented for the recital. The word "bodily" is not in the recital and was not found at the loci read; the clause is silent, not denied. |
| 5 | "The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son." | Shown, with the filioque. The Council recites the Holy Ghost as "the Lord, and the giver of life, who proceedeth from the Father and the Son; who with the Father and the Son together is adored and glorified". | Documented for the recital. The filioque differs from the 381 wording, as Step 0 §2 A1 records; it is not a floor failure. |

The Session III recital is the Creed with the filioque. The floor clears in substance. The clause on "bodily" resurrection is silent in the recital and is not denied; the Catechism says Christ "so arose that He could die no more" (row 10). The Article 4 check was made against the Council's text of 1546 and the Profession of 1564. It was not made against the voices of 1600 to 1650.

| Claim | Confidence | Basis |
|---|---|---|
| The Council ended with Session XXV on 3 and 4 December 1563. | Documented. | The session heading and Pallavicino's Argomento (rows 4, 51). The year in Waterworth's heading is damaged in the scan ("MDLXHL"). |
| The Session III recital of the Creed includes the filioque. | Documented. | Row 1. |
| Session XXV ordered the work on the Index, Catechism, Breviary and Missal. | Documented. | Row 4. |
| Pius V issued the Breviary bull in 1568 and the Missal bull on 14 July 1570. | Documented for the year of the Breviary bull and for the Missal bull's dating clause; the day is computed from the clause. | Row 12. |
| *Regnans in Excelsis* was issued in 1570 and claims power to depose Elizabeth. | Documented, in two witnesses. | Rows 13, 21. The day is not established from the file: a margin note reads "Dar. P. A. c. die 25. Febr." and may belong to another constitution on the page (§3 item 3). |
| Gregory XV's *Inscrutabili* is dated 22 June 1622. | Documented. | Row 17. |
| Clement VIII's bull *Magnus Dominus et laudabilis* is of 1595. | Documented. | Row 72. |
| The Council's reform and doctrine both aimed at heresy and discipline. | Documented for the Council's stated aims. | Rows 1, 4. |
| A pre-1517 reform current existed inside the Church. | Widely Accepted, as Doc_01 §2 tags it. | No pre-1517 text is vendored (§3 item 1). |
| The pre-1517 reform current was independent of Luther. | Inferential-Thin, as Doc_01 §2 tags its characterisation. | No pre-1517 text is vendored, and the shelf holds no source that states a dispute (§3 item 1). |
| The Cardinal of Lorraine led the acclamations. | Documented. | Row 4, where the decrees name him as the speaker, and row 5. |
| The Cardinal of Lorraine composed the acclamations. | Documented as the editor's statement and as Sarpi's, from opposite sides. | Rows 5, 50. The decrees' own text does not say it. |
| The Pope's illness and the Legates' haste shaped the close. | Documented as Pallavicino's and Sarpi's statement; Contested in meaning. | Rows 51, 50. |
| The Fathers wept at the close. | Documented only as tears of joy in a footnote quoting a diary other than Massarelli's. | Row 5. |
| The census's attribution of the tears and the haste to Massarelli's diary. | Not supported on this shelf. No Massarelli text is vendored; this is an absence, not a confidence level. | Rows 82, 5. |
| Residence of bishops by divine right was left undefined. | Documented as Waterworth's editor's account. | Row 5. |
| Pole wrote the Session II exhortation. | Documented as the editor's statement. | Row 5. |
| Lainez arrived at Trent on 13 August 1562. | Documented. | Row 68. |
| Borromeo was the Pope's agent for the Council's last period. | Widely Accepted. | Rows 34, 51; both partisan. |
| Borromeo required a confessional in every parish church. | Documented as his legislation. | Row 28. |
| Borromeo's feast names Trent as the aim of his government. | Documented. | Row 24. |
| Plurality of benefices was forbidden by Session VII, Chapter IV. | Documented. | Row 3. |
| Rome did not keep the rule on pluralities. | Contested. | Jewel's charge only (row 55). |
| Bellarmine wrote *De ascensione* in a retreat. | Documented as the translator's statement. | Row 41. |
| The file `bellarmine_notes-of-the-church_1688.txt` is not Bellarmine's work. | Documented. | Row 46. |
| The strand is singular for the corporate-magisterial material. | Dominant Modern Reconstruction, as Doc_01 §4 states. | Unchanged by this document. |
| Whether Bellarmine's devotional works are a second strand. | Not tagged. An open Doc_04 test, as Doc_01 §4 states. | The controversial work is not on the shelf (row 111). |
| The shelf is thin before 1545. | Documented for the shelf. | §6. |
| The shelf is thin for 1600 to 1650 beyond Bellarmine and the Collectanea. | Documented for the shelf. | §6. |
| The Index was applied in practice as the Tridentine texts prescribe. | Not tested. | Only the texts, in a second-witness scan (row 19). |
| The Index deputies' Congregation approved Carranza's book. | Documented as Sarpi's statement, from one hostile witness, in a partly garbled passage (lines 65034–65038). Sarpi places the approval with the deputies for the Index and their Congregation, not with a session of the Council. The census gives it as Trent's approval, in the Council's records; that is not on the shelf. | Row 50. |

**Thin-evidence map.** Where the shelf is thin, any reconstruction is Inferential-Thin or is not attempted.

| Area | What the shelf holds | What is missing | Treatment |
|---|---|---|---|
| 1517 to 1545 | Paul III's bull against Henry VIII; Waterworth's essay at second hand (rows 21, 5) | Leo X, Clement VII, any pre-1517 reform text | Not reconstructed; Inferential-Thin if attempted |
| 1600 to 1650, institutions | The Collectanea, 1622 to 1650 (row 17) | The Bullarium for these decades, the Rituale of 1614, the Capuchin annals | Documented for the Congregation's decrees only |
| 1600 to 1650, voice | Bellarmine's two works (rows 41 to 44) | Any lay, episcopal or parish text | Documented for Bellarmine; the rest not attempted |
| Parish, seminary, confraternity | Prescriptions in the Acta, the decrees and the liturgical books | Visitation records, rosters, any record of use | Prescription is Documented; practice is Inferential-Thin |
| The Council's debates | One Catholic editor, Sarpi and Pallavicino (rows 5, 50, 51) | The Council's acts and diaries in Latin | Documented as each narrator's account; Contested in meaning |
| Index and Inquisition in practice | Index texts in a second-witness scan; one sentence of 1564 (rows 19, 27) | Any diocesan or city record | Structure is Documented; practice is not tested |
| The Protestant side | Jewel, Marnix, Barlow, in polemic (rows 55, 57, 22) | Any Lutheran or Reformed text in its own words | Held to the Wittenberg and Reformed worlds |
| Laity and women | Granada's English readers, the lay Missal, hearers in the Lives | Any lay or woman's voice of this world | Not reconstructed |
| Pole | One oration in a garbled scan (row 49) | A legible text; his letters | Not usable; an absence |

**Confidence propagation.** The world's doctrinal and institutional outline rests at Documented, often on one editor's translation. That outline is the Council's decrees, the papal acts of 1560 to 1591, the Catechism and the liturgical bulls. Its practice, its parishes and its laity rest at Inferential-Thin or on no evidence. The same holds for 1517 to 1545 and, apart from Bellarmine and the Congregation, for 1600 to 1650.

## 9. Search record, field-bibliography sweep, and saturation

**Search record (STARLITE headings).**

*Sampling strategy:* the 835 text files in `cic/texts/` (the `.txt` and `.xml` files of 842 directory entries) were searched in full text for the Council's name. The corpus-map bucket, the Source Readiness Dossier (all six sections), the census entry VI.22 and its three documented stories, Step 0, Doc_01 and its reviews, the Library decision log, and the Borromean Milan dossier were read.

*Terms:* one case-insensitive regular expression over each file with every run of whitespace collapsed to one space: `Council of Trent`, `Tridentine`, `Concilio di Trento`, `Concilii Tridentini`, `Concilio Tridentino`, `Tridentin`, `Konzil von Trient`, `Concile de Trente`. Archive.org queries are listed below.

*Type:* source discovery for a construction step.

*Approaches:* full-text search; corpus-map, dossier and census read; footnote and preface snowball in the vendored apparatus (the Waterworth essay, the Giussano preface, the Reusch contents, the Collectanea headings, the Bullarium index); archive.org catalogue queries.

*Instruments:* Python and `grep` over `cic/texts/`; archive.org's advanced-search service.

**Date:** 2026-10-23

*Results of the shelf search.* 223 of 835 files contain a match. The count is the same by two methods: a Python regular expression over the whitespace-collapsed text, and `grep -l -z -P` over the raw files. Forty-three of the 59 bucket files match. The 16 that do not are the four Bellarmine devotional files, Granada, Pole (garbled), Canisius's Latin of 1565, Gibbings, Glostrup, Slavata, the English Marnix, two Borromeo Italian files (the Aggiunta and the Ricordi) and three Teresa files (the Life in English and in Spanish, and the Interior Castle). Outside the bucket, the files with the most matches belong to other worlds: the Jesuit letters and chronicle (Nadal, Ignatius, Polanco, Borgia, Broët, Lainez volumes 1, 3 and 5), Hough's *History of Christianity in India*, Raulin and Geddes on the Synod of Diamper, the French Reformed synods, Crespin's martyrs, Beza, Calvin's letters, the Zurich Letters, Mansi, Pelesz and Harasiewicz on the Ruthenian union. None is rowed here, because none is assigned here. They are listed in Open_Gaps: files on other worlds' shelves, October 2026 as candidates on other worlds' shelves.

**Field-bibliography sweep: run against one instrument, archive.org's catalogue.** The 17 queries follow. "Hits" are the number the service reported.

| # | Query (archive.org advanced search, `mediatype:texts`) | Hits | Disposition |
|---|---|---|---|
| 1 | title "Concilium Tridentinum" | 47 | Rowed: Görres edition (row 82); printings of the decrees not rowed |
| 2 | title "acta genuina" | 2 | Rowed: Theiner 1874 (row 81) |
| 3 | creator Jedin, title Trent, Trient or Tridentin | 10 | Rowed: Jedin (row 104) |
| 4 | title "Disputationes de controversiis" | 1 | One item, with no author or year in the listing; see query 5 |
| 5 | creator Bellarmino or Bellarmine, title controversiis | 11 | Rowed (row 111) |
| 6 | title "Rituale Romanum", 1600 to 1700 | 4 | Rowed (row 110) |
| 7 | title "Catechismus ex decreto" | 29 | Rowed (row 107) |
| 8 | title Carranza with catechismo, catechismus or arzobispo | 8 | Rowed (rows 97, 98) |
| 9 | creator Pastor, title "History of the Popes" | 283 | Rowed as a class (row 114) |
| 10 | title "Missale Romanum", 1570 to 1650 | 24 | Rowed (row 108) |
| 11 | title "Breviarium Romanum", 1568 to 1650 | 2 | Rowed (row 109) |
| 12 | title Ursuline, Orsolina or Ursulinarum, 1535 to 1650 | 5 | Nothing relevant; unproductive |
| 13 | title Capuccini, Capuchin or Cappuccini, 1536 to 1650 | 26 | Rowed: Boverio's annals (row 112) |
| 14 | title "Collegium Graecorum", "Greek College" or "Collegio Greco" | 9 | Nothing in the window; the nearest is a history of the Greek rite in Italy dated 1763; unproductive |
| 15 | title Carranza, creator Tellechea | 0 | Unproductive |
| 16 | identifier `conciliumtrident00coun` | 1 | Confirms the Görres volume (row 82) |
| 17 | title "Instructiones fabricae" or "Instructionum fabricae" | 2 | Rowed (rows 113, 84) |

Instruments not reached: HathiTrust (the catalogue answers; the viewer does not), Google Books (blocked from this environment, per the Library decision log), WorldCat, national library catalogues, the bibliographies of Jedin and of the Cambridge History volumes, and any bibliography of Borromean, Jesuit or Capuchin studies.

**Saturation.** Not closed. The sweep found nine items that the dossiers had closed or never named: the Latin acts of the Council, the Latin Catechism, the 1570 Missal, the 1568 Breviary, the Rituale, Bellarmine's *Disputationes*, the Capuchin annals, the separate print of the Instructions of 1577, and Pastor. Each is a lead for acquisition. The last unproductive searches are queries 12, 14 and 15 and the dossier's closed searches for Merici's Rule, Ochino, the Capuchin Constitutions of 1536 and de Sales in 1613 English (rows 93, 92, 91, 94). A registry that has found nine new leads with one instrument has not reached saturation.

## 10. Open items carried forward

Gaps, requests to the Library thread, candidates on other worlds' shelves and questions for the project lead are in `Open_Gaps_Tracking.md`. The main items are these.
- The Council's own acts in Latin (Open_Gaps: the Council's acts in Latin, October 2026) and the Latin of the Catechism, Missal, Breviary and Ritual (Open_Gaps: the Latin Catechism, Missal, Breviary and Ritual, October 2026).
- Bellarmine's controversial writing for the Doc_04 question (Open_Gaps: Bellarmine's controversial writing, October 2026).
- The first and last thirds of the window (Open_Gaps: the window is thin at both ends, October 2026) and the missing voices: laity, women, Capuchins, Ursulines, Greek College (Open_Gaps: voices the shelf lacks, October 2026).
- The file headers of the Pius V letters and the Acta (Open_Gaps: two file headers say second witness, October 2026), and the missing record of the Borromean Milan placement (Open_Gaps: no record of the Borromean Milan placement, October 2026).
- The small differences between Doc_01's quotations and the scan (Open_Gaps: quotations in Doc_01 that differ slightly from the scan, October 2026).
- Corpus-map change requests (Open_Gaps: corpus-map change requests, October 2026) and the candidates on other worlds' shelves (Open_Gaps: files on other worlds' shelves, October 2026).

## 11. Disposition

Cleared review at Round 2 of two (Revision 2). Review files: `Review-Artifacts/Doc02_Round1_Review.md` (substantial revision required) and `Review-Artifacts/Doc02_Round2_Review.md` (Cleared). It is not Approved to proceed and it is not Frozen. One escalation category applies: a portfolio-level, cross-world question, the ownership of Borromeo's voice between Borromean Milan (VI.12) and this world (VI.22). It is routed to the project lead (Open_Gaps: no record of the Borromean Milan placement, October 2026), and this document does not decide it. Approved to proceed follows that ruling. This document does not change Doc_01. Four statements in Doc_01 are overtaken by the shelf and are listed as change-order candidates (Open_Gaps: statements in Doc_01 that Doc_02 overtakes, October 2026).

*End Doc_02.*
