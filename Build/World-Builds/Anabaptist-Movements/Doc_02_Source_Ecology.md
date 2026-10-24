# Doc_02: Source Ecology: The Anabaptist Movements

**Status:** Approved to proceed (Revision 2; Round 1 substantial revision, Round 2 Cleared; review files `Review-Artifacts/Doc02_Round1_Review.md` and `Review-Artifacts/Doc02_Round2_Review.md`; no escalation category applies; items waiting on the project lead are OG-5, 8, 9, 10, 12, 18, 19 and 20; not Frozen; does not change Doc_01).
**Round:** 2
**Companion documents:** `Source_Registry.md` ("row N" below means a Registry row) and `Open_Gaps_Tracking.md` ("OG-n" means an entry there).
**Governed by:** Construction Framework V7.4, Part II and Step 2. Constitution V2.3, Articles 4 (the floor check), 16, 17 (the five confidence levels), 20 (source asymmetry and marginalized voices) and 26 (Author Gravity). `Source_Registry_Template.md` V1.0. The Library rulings in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`.
**Forces Framework integration:** Step 2 (Forces Framework V1.1, Section 4). The forces lens is applied in §6.
**Grounded in:** `Doc_01_World_Identification_Boundaries_Orientation.md` (Revision 3, Approved to proceed: 1525 to 1650; the Swiss lands, Moravia and the Netherlands; two Article 21 strands, a Congregational strand across the Swiss and Dutch wings and a Communal-Property strand in Moravia) and `Step0_Movement_Scope_Confirmation.md`. This document does not reopen either.

Confidence terms follow Article 17: Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential/Thin. "Not attested" names an absence, not a level. Quotations are matched to the vendored files. Whitespace, line-break hyphens and the long s are normalised, and no other letter is changed, so the scans' OCR errors stay in the quotations. No page image was available. Every German quotation is therefore checked against the scan text only.

---

## 1. Primary Sources

Twenty-five files are vendored and assigned to this world (`cic/corpus-map/the-anabaptist-movements.yaml`, 26 rows; McGlothlin 1911 has two). They come to 35,213,045 characters and 5,591,950 words. Every figure is counted in the UTF-8 locale (`LC_ALL=C.UTF-8`) by two methods that agree: the sum of each file's decoded length, and `cat` of the 25 files piped to `wc -m -w`. In the C locale `wc -w` gives 5,573,280 words, because it does not count tokens made only of non-ASCII letters, and `wc -m` there counts bytes (35,507,084). The counts are of whole files. McGlothlin's file is a compendium of Baptist confessions, and only its Anabaptist and Mennonite parts concern this world (rows 21 and 22).

- **By role in the corpus map.** Eighteen files have the `tradition` role: 28,554,821 characters, or 81.1 per cent. Seven have the `context` role: 6,658,224 characters, or 18.9 per cent. The context files are the Augsburg Confession, the Book of Concord, the Second Helvetic Confession, two volumes of Calvin, Zwingli's selected works and Vedder's life of Hubmaier. Vedder is marked `context`, but his Appendix and pp. 130 to 134 print Hubmaier's own words (rows 34 and 35).
- **By language.** Thirteen files are German: 16,351,859 characters, or 46.4 per cent. Twelve are English: 18,861,186 characters, or 53.6 per cent. No Dutch text is on the shelf. The Dutch wing speaks to us in English only (Funk, Kolb, Sohm, the Elkhart manual). The first three say they were made from the Dutch. None can be checked against it.
- **By scan quality.** Eight files are second witnesses under the Library's scan-quality rule: 4,722,827 characters, or 13.4 per cent. They are the Wolkan microfilm, the Ausbund of 1846, Riedemann, Böhmer's Fraktur articles and the four Hubmaier prints. The other 17 files, 30,490,218 characters or 86.6 per cent, can be quoted. Twelve of those are English and verbatim-ready (18,861,186 characters). Five are German with a clean scan, and still need a page-image check (11,629,032 characters, or 33.0 per cent): Bossert, Egli, Beck, Wolkan's clean scan and the Ausbund of 1856. The two-method measure of scan quality is in §9.
- **By who made the edition.** The English editions of the Dutch wing's own books were made by Mennonite publishers for Mennonite readers. Funk's Publishers write that their readers are "those professing the same faith with Menno" (lines 228–229), the Elkhart manual is from the Mennonite Publishing Company, and the 1886 publisher's preface to the *Mirror* calls its matter "especially precious to us, as Mennonites" (lines 78–79). The Hutterite *Geschicht-Buch* of 1923 was published by the Brethren themselves (row 27). Beck, Bossert, Egli and Böhmer are academic editors of the nineteenth and twentieth centuries. The hostile frame comes from Zwingli, Calvin and the Lutheran and Reformed confessions.

**Who speaks, and for which years.** The years are the years the text covers or was made. The rows are Registry rows.

| Voice | What is on the shelf | Years | Rows |
|---|---|---|---|
| Menno Simons, own words | The tracts of Funk's two parts (about 531,000 words), in English from the Dutch | Dated tracts run from 1544 to January 1559; the *Renunciation* is dated in the OCR to 1554 | 1 to 8 |
| Dirk Philips, own words | The *Enchiridion*, four books and more | Undated in the file | 9, 10 |
| The Dutch churches, corporate | The Dordrecht Confession (1632) in two English editions; the Waterlander confession (about 1580) in English from Latin; the confessions of 1627 and 1630 inside the *Mirror* | 1580 to 1632 | 12, 20, 21 |
| The martyrs and the compiler | The *Martyrs' Mirror*, with trial records, letters, testaments and dialogues | Entries from 1524 to 1660; compiled 1660 | 11 to 19 |
| The Swiss Brethren, corporate | The Schleitheim articles: two English texts from Zwingli's Latin, a shortened German text in Beck, a garbled German text in Böhmer | 24 February 1527 | 22, 40, 24, 23 |
| The Swiss Brethren, hymns | The Ausbund, two scans | Undated hymns; Lancaster printings of 1846 and 1856 | 29, 30 |
| Zurich's authorities and the first believers | The Zurich council's mandates, interrogations and sentences | 1525 to 1533 | 31 |
| Württemberg's authorities and the believers | Ducal mandates, visitations, interrogations | 1527 to 1641 (the Library's description of the volume) | 32 |
| The Hutterite Brethren | The communal chronicle in two scans and in Beck's older-spelled print; the 1545 *Rechenschaft* to the Moravian lords; Riedemann's confession | Chronicle entries from 1527 to 1665 (Wolkan) and 1519 to 1722 (Beck) | 27, 100, 26, 25, 33 |
| Balthasar Hubmaier | *On the Sword* and the Twelve Articles in English; four microfilm reels of 1526 and 1527 prints in German, holding seven of his titles | 1525 to 1527 | 34, 35, 36 to 39 |
| The opponents | Zwingli's *Refutation*; Calvin's *Institutes*; the Augsburg Confession; the Formula of Concord; the Second Helvetic Confession | 1527 to 1577, and 1566 | 40 to 45 |

**The Dutch wing.**

- Menno speaks at length and in his own voice, about his leaving Rome, baptism, the ban, the Incarnation and the magistrates (rows 1 to 8). Dirk Philips speaks in his handbook, and in particular on the Incarnation (rows 9 and 10).
- The churches speak in the Dordrecht Confession and the Waterlander confession. The Elkhart edition of Dordrecht gives the churches' own forms of service as well (row 20).
- Ordinary believers speak in the *Mirror*: Anna of Rotterdam in her testament (row 15), Herman Vleckwijk in his disputation (row 17) and the court's copy of Dirk Willems's sentence (row 16).

**The Swiss wing.**

- The Swiss Brethren have no book of their own on the shelf. Their voice reaches us in four ways. Schleitheim is one: it exists in four texts of one document, none of them clean German (rows 22, 40, 24, 23). Sattler's trial and his letter to Horb are the second (row 13). The hymnal is the third (row 29). The Zurich council's file is the fourth. It records what the first believers said when they were questioned (row 31).
- Conrad Grebel's name occurs 215 times on the shelf, 185 of them in Egli, and never in the *Mirror*. Egli's Nr. 646 prints a letter to the Zurich council from a Täufer whom Egli queries as Blaurock (lines 18484 onward). Felix Mantz speaks in his own words only in the admonition the *Mirror* attributes to him (row 14). The council's sentence reports what he taught (row 31).

**The Moravian wing.**

- The Hutterite Brethren speak in their chronicle (rows 27 and 26) and, to the Moravian lords, in the *Rechenschaft* of 1545 (row 25). Riedemann's confession is on the shelf only as a second witness (row 33), but his letters are printed in the Chronicle (row 100).
- Vedder's life of Hubmaier is the one English account of the Nikolsburg split (row 34).

**Hubmaier.** Hubmaier speaks in English in *On the Sword* (row 35) and in the Twelve Articles that Vedder prints in full (row 34). His German prints are second witnesses. The four reels hold seven of the 26 writings in Vedder's Bibliography (rows 36 to 39).

**What is not on the shelf.** Any Dutch text of Menno, Dirk or the *Mirror* (row 55). Any writing of Marpeck (rows 69 and 87) or of Denck (row 66). Any letter of Grebel (row 70). Hubmaier's writings of 1524 to 1525 and 1526 to 1527 in the two reels not vendored (rows 51 and 52). Sattler's own tracts (Böhmer says German printings of the trial account and the Horb letter exist, row 23). The later Täuferakten volumes (row 63). Hutterite epistles other than those the chronicle prints. The Hutterite community ordinances (row 84). No English translation of any German file exists in the public domain.

## 2. Author Gravity Assessment

Five dimensions: Visibility, Representativeness, Influence, Limitations, Transmission History. The Transmission History entries are drawn from the editors' own prefaces and notes on the shelf.

**Menno Simons (1496 to 1561, or 1559).**
- *Visibility:* The most visible single voice. About 531,000 words of his tracts are on the shelf (rows 1 to 8).
- *Representativeness:* He speaks for the Dutch wing's leader and, through his name, for the churches that bear it. McGlothlin says of the churches "Because of his great services in rehabilitating the Anabaptist cause in the Netherlands and North Germany, they came to be called Mennonites" (lines 1420–1422) (row 21). He does not speak for the Swiss or the Moravian wing. He did not write the Dordrecht Confession, which is dated 1632, 71 to 73 years after the two dates the shelf gives for his death.
- *Influence:* Central to the Dutch wing, and his name became theirs. McGlothlin says the Dutch churches divided "questions of discipline and the proper view of the person of Christ" (lines 1439–1440) (row 21). Outside the churches, the *Mirror* has a friar charging him with the sieve-and-spout image and a martyr denying that he wrote it (row 17).
- *Limitations:* Much of what he wrote answers named opponents (A'Lasco, Gellius Faber, Martin Micron). Several tracts are revised versions of earlier ones. Menno's note "To the Reader" after the title block at line 1121 says he revised and corrected the *Foundation* and changed its form, not its doctrine. The English leaves out the works Menno rejected (Publishers' Preface, row 3).
- *Transmission History:* Menno wrote in Dutch. Funk's Publishers followed the Dutch edition of Johannes van Veen (Amsterdam, 1681), and Part I follows, in part, the English of I. Daniel Rupp (1863), which was made from a German translation. They compared it all with the Dutch and corrected it (row 3). The translators are not named. The date of Menno's death is disputed between the *Mirror* (13 January 1559) and Funk's Note 1 (1561). Funk's reason is a tract dated in the volume to 23 January 1559 (row 3). The Dutch of 1681 is a lead (row 55).

**Dirk Philips.**
- *Visibility:* One large book, the *Enchiridion*, in at least four books (rows 9 and 10).
- *Representativeness:* Kolb calls him "contemporary of and co-worker with Menno Simons" (lines 1298–1299). He speaks for the Dutch wing and, above all, for its teaching on the Incarnation.
- *Influence:* Kolb's preface says that the English edition is "for the first time presented to the public in the English language" (lines 1306–1307). The preface adds that the book had "numerous editions in the Dutch" (line 1308) and later appeared in German and French.
- *Limitations:* The parts read are argument from Scripture. The book is not a report of church life. Its front matter is OCR noise.
- *Transmission History:* Kolb (1910) translated it. He does not name the Dutch edition he used, and no Dutch is on the shelf (row 9).

**Peter Riedemann.** *Visibility:* named 95 times in five files, under four spellings ("Rideman", "Ridemann", "Riedeman" and "Riedemann"; Beck's single "Riedmann" is not counted): 58 in the clean Chronicle scan, 27 in Beck, 6 in McGlothlin, 2 in Bossert and 2 in the 1902 reprint of his book. His book is unreadable (row 33), but the Chronicle prints his letters, including the letter to Hans Amon (lines 12636 and following; row 100). *Representativeness:* the Moravian wing's fullest doctrinal statement, per the corpus map, and, in the letters, a leader writing to named congregations from prison. *Influence:* not tested. *Limitations:* the book exists only as a garbled reprint of 1902. The letters reach us through the Chronicle's modernised spelling and its margin-note layout, and they are provisional until the page images are read. *Transmission History:* Beck's note says that after his imprisonment at Nuremberg the community sent him to Hesse: "Aus Nürnberg kaum zurückgekehrt, wurde er von der Gemain nach Hessen entsendet" (lines 4793–4794). The 1902 publishers call the book an unaltered reprint of a sixteenth-century printing. The English translations are in copyright (row 64).

**Balthasar Hubmaier.**
- *Visibility:* Seven titles in Vedder's Bibliography are on the shelf in some form (rows 36 to 39), and one treatise and the Twelve Articles are in readable English (rows 35 and 34).
- *Representativeness:* He speaks for a learned preacher who moved from Waldshut through Zurich to Nikolsburg. Vedder reports that his sword position was held by one party at Nikolsburg, the Schwertler (row 34). Doc_01 §4 has already decided that this party is not a third strand. Beck's Vorrede calls him "der eigentliche Gründer der mährischen Gemeinde" (lines 329–330). That is Beck's claim. Vedder and Doc_01 place the communal tradition with Hubmaier's opponents, the Stäbler.
- *Influence:* Not tested here beyond the Nikolsburg dispute.
- *Limitations:* The readable part is a prayer-creed and one treatise, so the voice is narrow. His wider baptismal and Supper writing exists only in unreadable German. Doc_01 §7 item 2 asked that the world's argument not rest on more named voices than the shelf can source. The shelf holds Hubmaier on the sword, the Twelve Articles and (unreadably) six other titles.
- *Transmission History:* Vedder's Preface says some of the booklets were translated long ago by Osgood and others by himself, and the file does not say which of the two made the English of *On the Sword* or of the Twelve Articles (row 34). Vedder worked from the Rochester Theological Seminary collection of the originals. The German prints on the shelf are microfilm photographs of sixteenth-century prints, assembled in 1938 (Library headers). Vedder says Hubmaier wrote the Twelve Articles in prison at Zurich and printed them at Nikolsburg a year later. The German print of them is not on the shelf.

**The Swiss Brethren at Schleitheim, and Michael Sattler.**
- *Visibility:* One short, key text, in four versions (rows 22, 40, 24, 23).
- *Representativeness:* A statement of agreement among the brothers: its title in the English is "The Articles, which we have drawn up and in which we agree" (lines 515–516). Böhmer says that Sattler was the leader of the assembly and that he sent the articles on to the congregations. His words are "von dem leiter derselben, Michael Sattler" (lines 1716–1717). The census calls Sattler the principal author. The shelf supports "leader and sender" (Documented) and does not say who wrote the words.
- *Influence:* Böhmer: "Sie fanden handschriftlich sofort eine außerordentliche Verbreitung" (lines 1717–1718). Zwingli says almost every Anabaptist had a copy (row 40). Calvin knew them in 1544 through a French printing that is now lost (row 23).
- *Limitations:* The articles speak for agreement on seven points. They are silent on the Trinity and Christology (Step 0 §2 A1). Whatever the Swiss did after 1527 is not in them.
- *Transmission History:* Böhmer's introduction gives the chain. The articles were adopted at Schlatt on 24 February 1527. Two German printings carried them with Sattler's letter (recension A). A Bernese copy reached Zwingli in April 1527 (recension B). Zwingli put it into Latin and printed it with his reply in August 1527. McGlothlin and Jackson each translated that Latin into English. A French printing is lost. A later Moravian copy is the one Beck prints in shortened form. McGlothlin's statement that the German was never printed is wrong on Böhmer's evidence (rows 23, 22). The two English texts differ in wording, as in the Fourth Article (row 40). The clause on "diabolical arms of violence" is in the English, identifiable in Böhmer's garbled German, and not in Beck's shortened German (row 24).

**Conrad Grebel, Felix Mantz and Georg Blaurock.**
- *Visibility:* Present only through others. The Zurich council's file names Grebel 185 times (row 31). The Hutterite Chronicle tells their story (row 27). Mantz has the admonition the *Mirror* attributes to him (row 14).
- *Representativeness:* The three founders, in the opponents' file and in the later communal memory. No letter of Grebel's is on the shelf (row 70).
- *Influence:* Beck's Vorrede names Grebel, Mantz and Blaurock as the men who took the lead at Zurich, and says the Brethren's chronicle puts the movement's cradle on the Limmat (row 26).
- *Limitations:* Their own voice is almost absent. What survives in the Zurich file is what the council wrote down, and Egli's regesta cannot always be told from the sixteenth-century text in the OCR.
- *Transmission History:* Egli's source notes cite the council's books and an archive file headed "A. Wiedertäufer" (for example after Nr. 936). The council's sentence on Mantz is of 5 January 1527 (row 31), where the *Mirror* heads his entry 1526 (row 14).

**The Hutterite chroniclers.**
- *Visibility:* The chronicle is the largest German text on the shelf, in three witnesses (rows 27, 28, 26).
- *Representativeness:* A communal self-record. Wolkan's foreword says the writing was begun by the community's leader Kaspar Braitmichel (the scan reads "Brattmichel"), who kept it to 1542, and continued by Hanns Kräl and the community's scribe Haupprecht Zapff. The name is spelled so in the foreword (lines 117 to 118); the text has "Haupprecht Zapf" at line 2952, and this document uses the foreword's form. He wrote to 1593, then four further hands, the last to the end (lines 126 to 130). It speaks for the Communal-Property strand.
- *Influence:* The community kept the book. Wolkan says it is still in the Brethren's hands in America, whither they came from Russia in 1874, and that Beck in 1883 wrongly thought it lost (lines 88 to 96).
- *Limitations:* A self-vindicating genre. The Brethren's Vorrede says the writer gathered his account from reliable people and from his own experience (row 27). The first-baptism story and the Sattler entry are told at a distance of decades.
- *Transmission History:* Three stages. The sixteenth-century manuscript was copied. Beck printed extracts from the manuscripts in 1883 with the older spelling (row 26). Wolkan printed the whole in 1923 from a careful copy, and he modernised the spelling and followed the words, not the letters (row 27). A quotation from Wolkan therefore cannot be used to settle a point of spelling.

**The Ausbund's hymn writers.**
- *Visibility:* A hymnal with a Register of first lines (line 38321 of the 1856 file).
- *Representativeness:* The Swiss Brethren's community singing. The Vorrede says the book gathers poems of people of different religions and leaves each unmocked (row 29).
- *Influence:* Still in Amish use, per the census and the corpus map (Doc_01 §6).
- *Limitations:* Not read hymn by hymn. The OCR reads round s as f.
- *Transmission History:* The scans are Lancaster printings of 1846 and 1856, the 1856 one being the seventh American printing. The census dates the first printing to 1564, and no vendored text gives that date. The hymns' own dates are not on the shelf.

**Thieleman J. van Braght (the compiler of the *Mirror*).** Treated as a narrative source with all five dimensions (Framework, Expanded Author Gravity). *Visibility:* the whole of the Dutch wing's martyr record passes through him. *Representativeness:* a Dutch Mennonite compiling in 1660. The census calls the *Mirror* "a 1660 Dutch Mennonite compilation, not a contemporaneous archive". *Influence:* still printed and read in Amish and Mennonite homes (Doc_01 §6). *Limitations:* a hagiographic frame. His title claims "Compiled from Various Authentic Chronicles, Memorials, and Testimonies" (lines 46–47). He says himself that the rescue of the thief-catcher at Asperen is told by "trustworthy persons" and the seventy cries by "trustworthy memoirs" (row 16). He dates Mantz's death 1526 against the council's 1527 and Menno's death 1559 against Funk's 1561. *Transmission History:* Sohm's English of 1886 is from the edition of 1660 in Dutch. The Dutch is not on the shelf (row 11).

**Ordinary believers in the records.** The Zollikon baptisms of January and February 1525 are told by the believers in Egli's Nr. 636 (row 31). Anna of Rotterdam's testament, Herman's disputation and Dirk Willems's sentence are in the *Mirror*. Their transmission is the compiler's (above). The Zurich words are given under interrogation (§6).

**The editors and translators.** Funk's translators are unnamed Mennonite publishers. Kolb's patron is named in his preface and the Dutch edition is not. Sohm, the *Mirror*'s translator, appears on the title page only. Vedder wrote for a series on the leaders of the Protestant Reformation (Preface to the series), and he leaves unmarked which of his translations are Osgood's. McGlothlin published through the American Baptist Publication Society, and his Mennonite pages are there for a Baptist reason. Of the Waterlander confession he writes "It has special interest for Baptists" (line 1446) (row 21). Beck, Bossert, Egli and Böhmer edit the archives of the opponents and the Brethren's manuscripts. Each edition is a choice. This document treats the editors' view as a structural fact about the shelf.

**Marpeck and Denck.** Neither is on the shelf in his own words (rows 69, 66). Doc_02 does not fill the gap. A Bossert footnote points to the one text of Marpeck named in the apparatus (row 87).

**The opponents.** Zwingli, Calvin, the Augsburg Confession, the Formula of Concord and the Second Helvetic Confession are in print on the shelf (rows 40 to 45). They are the opponent's voice. The Mirror's friar is another. The authorities speak in Egli's and Bossert's mandates and sentences. Their words describe the believers and do not come from them.

## 3. Secondary Scholarship Assessment

The secondary matter on the shelf is by editors and biographers of 1871 to 1930. It is Vedder's life of Hubmaier (1905), McGlothlin's introductions (1911), Funk's notes (1871), Kolb's preface (1910), Beck's Vorrede (1883), Wolkan's foreword (1923), Bossert's Einleitung (1930), Egli's summaries (1879) and Böhmer's notes (1910). No work published after 1930 is vendored. Roth and Stayer (2007), the *Cambridge History* chapter and Gregory (1999) are named in the census and are not on the shelf (rows 76, 77, 78). Claims below rest on the editors' own words and are marked accordingly. The modern scholarly view on these questions was not consulted, so the rulings in this section are the shelf's and not the field's (OG-21).

**1. Where and when did the movement begin? Widely Accepted: Zurich, January 1525.** The census and Doc_01 give January 1525. The vendored dated evidence is consistent with it and does not date the first adult baptism itself. On 18 January 1525 the Zurich council ordered that every unbaptised child be baptised within eight days: "alle noch ungetauften Kinder innert acht Tagen" (lines 17690–17691) (Egli Nr. 621). On 21 January it ordered "besonders Konrad Grebel und (Felix) Manz sollen von ihrem « disputieren und fürnemen » abstehen" (lines 17846–17847) (Nr. 624). Jackson notes a first disputation on 17 January 1525 (row 40, line 5559). The first believers' own account of the Zollikon baptisms is in Egli's Nr. 636, with the judgment dated 7 February 1525. The Chronicle's account of the first baptism carries no date in the passage read (row 27).

**2. Who baptised whom? The Brethren's account, as the Brethren's account.** The Chronicle says Grebel, Mantz and Zwingli met; that Zwingli drew back; that Georg, called Blaurock, asked Grebel for baptism; and that "hat der Konrad ihn getauft, weil dazumal sonst kein verordneter Diener, solches Werk zu handlen, war" (lines 5517–5519). That is *Documented* as what the Brethren wrote down, long after the event. It is the only account of that sequence on the shelf. For Zollikon, Egli's Nr. 636 has a heading, "Marx Bosshard erzählt von Blaurocks Taufe" (lines 18091–18092), for the telling of the baptism by Blaurock, and the believer Jörg Schad saying that Mantz baptised him (row 31). So Blaurock and Mantz baptising is attested in the Zurich file for the Zollikon group. Grebel baptising Blaurock first is the Chronicle's alone. Nothing on the shelf contests the sequence, and the Zurich file is consistent with it. It is *Documented* as the Chronicle's account and rests on that one witness on this shelf. Doc_01 §2 rates the sequence *Documented* on the strength of the Reformed Cities world's Doc_01. The shelf here neither confirms nor overturns that rating, and the single-witness basis is routed to the project lead (OG-18).

**3. Was the German Schleitheim text ever printed? Documented: yes.** McGlothlin writes "So far as known, they were never printed" (lines 490–491). Böhmer's introduction names two German printings of the articles, one in the Munich State Library in two copies and one in Berlin and with a Leipzig dealer, both without year or place (row 23). The Library's file header for McGlothlin repeats the claim, and the corpus-map note says the German survives only in archival manuscript. The Library's dossier already corrects it (dossier §1).

**4. Who wrote Schleitheim? Documented for Sattler as leader and sender; the authorship of the words is not attested on the shelf.** Böhmer's section on the seven articles says that they were adopted on 24 February 1527 at a meeting of Upper German Anabaptists, and that Sattler, the leader of the meeting, sent them on to the congregations. His words are "wurden am 24 Februar 1527 in einer Versammlung oberdeutscher täufer" (lines 1713–1714) and "von dem leiter derselben, Michael Sattler" (lines 1716–1717). The census calls Sattler the principal author, and Doc_01 repeats it. The *Mirror*'s trial record does not mention Schleitheim (no match in the file). The title of the Pressburg manuscript, as Beck and McGlothlin give it, names only the place and the date (row 24). The census wording is *Widely Accepted* outside the shelf and is carried here as that. Doc_01 §2 states Sattler's authorship as *Documented*, which the shelf does not support for the words of the articles. Doc_01 is not reopened here. The difference is routed to the project lead (OG-19).

**5. Which articles carry the refusal of the sword? Documented, for the texts.** In the English from Zwingli's Latin the Fourth Article ends with the renunciation of "the diabolical arms of violence" and the Sixth is headed by the sword (rows 22 and 40). In Beck's shortened German the sword is in the Sixth only: "Das schwert ist ein gottes Ordnung ausserhalb der volkomenhait Christi" (lines 4896–4897). Böhmer's garbled German has the clause in the Fourth (lines 2005 to 2007). So the refusal stands in the Sixth Article of every text that has the Sixth's opening, and in the Fourth Article of the English and of Böhmer's German but not of Beck's shortened German. Doc_01 §4 cites the Fourth. That citation holds for the English, and it does not hold for Beck's text.

**6. When was Felix Mantz sentenced? Documented: 5 January 1527.** Egli's Nr. 1109 is the council's sentence, dated "1109. Jan. 5 (Samstag v. h. Dreikönigen)" (line 33679) under the heading for 1527. It names Mantz and orders him bound and thrown into the water (row 31). The *Mirror* heads his entry 1526 and writes "This occurred in the year of our Lord 1526" (lines 58475–58476) (row 14). Doc_01 §2 already discloses the *Mirror*'s date. The council's own text is the stronger witness. The drowning follows the sentence by its own terms. The execution is not recorded in the entry (*Widely Accepted*).

**7. When did Menno Simons die? Contested between two editors on the shelf.** The *Mirror* gives 13 January 1559 (row 19). Funk's Note 1 argues for 1561 from a tract dated 23 January 1559 in his own volume, and Note 2 sets his birth in 1496 (row 3). The year is carried open.

**8. Did Menno teach that Christ's flesh came from heaven? Contested within the Dutch record; the words themselves are Documented.** Menno writes "the whole Christ Jesus, God and man, man and God, is from heaven and not of earth" (lines 48892–48894) and "the Word came down from heaven, became flesh in Mary" (lines 48906–48907) (row 2). Dirk's chapter title denies that Christ's flesh came from Mary (row 9). Dordrecht Article IV declines to say how the body was prepared (row 12). The charge that Menno taught passage "as water through a sieve" appears only in the friar's mouth, and Herman denies it (row 17). §7 item 1 gives the full handling.

**9. Why do the two Dordrecht texts differ at Article IV? Not resolvable on the shelf.** The *Mirror* reads "conceived in the virgin Mary" and the Elkhart edition reads "conceived by the Virgin Mary" (rows 12 and 20). The Dutch of 1632 is not on the shelf. Dirk Philips himself writes that Christ "became man in Mary" (line 6406) while denying that Mary gave the flesh. So the preposition does not decide the question in either English, and it should not carry weight (OG-5).

**10. Who founded the Moravian communal tradition? Documented for the split; Contested between two editors for the word "founder".** Vedder reports from the chronicle that the party of Widemann, the Stäbler, "went their way to Austerlitz" (line 9003), and that for them community of goods became "a standing or falling Church" (line 8983) (row 34). Beck's Vorrede calls Hubmaier "der eigentliche Gründer der mährischen Gemeinde" (lines 329–330) (row 26). The two can be read together if Beck means the Nikolsburg congregation and Vedder the communal order. Doc_01 §2 and §4 follow Vedder. Neither editor's word is a Hutterite source.

**11. Was the movement one origin or many? Contested, between the Brethren's own account and the polygenesis the census names.** The Brethren's chronicle, as Beck reports it, says their ship was built "an den Gestaden der Limmat, und nicht in Wittenberg oder Zwickau gezimmert" (lines 177–178) (row 26). Roth and Stayer's polygenesis, which Doc_01 §4 uses as context only, is not on the shelf and could not be read for this question (row 76).

**12. Did the movement disown Münster? Documented, in the movement's own words.** Menno: "Never in my life have I seen Munster" (line 370) (row 1). Menno and Dirk (rows 6 and 10). The Moravian Brethren in 1545 write of Münster "die wir derselbigen weiss auffs allerhöchst hassen" (lines 11285–11286) (row 25). The Münster exclusion remains a scope decision (Doc_01 §5).

## 4. Formation Narrative Sources

Tiers are those of the Framework's four-tier story classification.

- **Menno's *Renunciation*.** A first-person account of his break with Rome and his doubts about infant baptism, dated 1554 in the title block (the OCR of the date is garbled) and telling of 1536 and earlier (row 1). It is Tier 1 for what Menno reports of himself, with the retrospect named. It is not a report of the Münster years, which he disowns.
- **The Chronicle's first-baptism story.** Told in the Brethren's introduction from "reliable people" and from the writer's own experience (row 27). It is Tier 2: collected community memory with an identifiable collection history. The detail of who baptised whom is single-sourced on this shelf (§3 item 2).
- **Sattler's trial in the *Mirror*, and the Chronicle's version.** The *Mirror* prints the charges, his answers and the sentence (row 13). The Chronicle has eight charges where the *Mirror* has nine (row 27). Böhmer says a German printing of the trial account was made (row 23). Tier 1 for the sentence. The date of the execution is given plainly by Böhmer alone: "Sattlers märtyrertod, 21 Mai 1527" (line 1733). The *Mirror* closes the account of the burning with "21st day of May, A. D. 1527" (line 58958), which is consistent with Böhmer. The Chronicle's entry begins "Anno 1527, am 21. Tag des Maien, ward B. Michael Sattler" (line 5816), and on the grammar of that sentence the date belongs to his arrest (*gefangen*) and not to his death. Tier 3 for the compiler's remarks around the sentence.
- **Anna of Rotterdam's testament.** A document, in the compiler's frame (row 15). Tier 1 for the testament as a text, with the compiler's attribution. The census names her "Anneken Jans". The *Mirror* names her Anna of Rotterdam. Doc_01 §2 already notes the difference. No text on the shelf joins the names (OG-8).
- **Dirk Willems.** The census places the story at Tier 2. The sentence of the court of Asperen is a copy of the town record, certified and collated in 1606 (row 16), and is Tier 1. The rescue on the ice rests on the compiler's report "trustworthy persons, that when he fled" (line 104653) and is Tier 2. The seventy cries at the stake come from "trustworthy memoirs" (line 104674) in a later Note and are Tier 3, *Inferential/Thin* in the detail. The court record says Dirk confessed without torture.
- **Herman's disputation.** Tier 2 at best. The compiler says of the two prisoners "two disputations are extant" (lines 109290–109291), and does not say who recorded them (row 17).
- **Leonhard Schoener's admonition (1528) and Hans van Overdam's confession and letter (1550).** Own-voice texts inside the *Mirror* (row 19). Tier 1 for the texts as the compiler prints them.
- **Hubmaier in Vedder.** A biography, so a secondary narrative source with its own Author Gravity entry (§2). Vedder's Twelve Articles are Tier 1 for what Hubmaier said of his faith.
- **The Zollikon testimonies in Egli's Nr. 636.** Ordinary believers answering a court. Tier 1 as recorded speech, with the coercion named in §6.
- **The Ausbund.** Hymns as the community's memory, Tier 2. The prison origin the title page claims for the hymns is the title page's claim (row 29).
- **The census story "The Kingdom at Münster".** Outside the scope (Doc_01 §1). Its sources are Excluded or not on the shelf (rows 79, 80, 59).

## 5. Material Culture and Daily Life Sources

- **Vendored:** no archaeology, no building record, no object. The census names two places a visitor can go: the Täuferhöhle near Bäretswil and the Menno Simons monument at Witmarsum (rows 85 and 86). The shelf says nothing about the cave.
- **Where believers met.** The Zurich file has them in houses. In Nr. 636 a witness says that Grebel and Mantz went to several houses morning and evening: "Konrad Grebel und Felix Manz alle Morgen und Abend in etliche Häuser laufen" (lines 18268–18270) (Egli's summary). The *Mirror* has two accounts of meeting out of doors. Leonhard Schoener (1528) writes "Our chambers are in caves and cliffs, and snares are laid for us as for the birds of the air. We go about in forests, and are hunted with dogs" (lines 59864–59866), and Hans van Overdam (1550) writes of a Sunday meeting "Early in the morning, Hansken went with me to the woods where we were to assemble" (lines 68846–68847). The 1886 publisher's preface says the believers were "compelled to dwell in caves and mountains, and other secluded places" (lines 84–85), which is the publisher's later summary and not a source (rows 11 and 19).
- **The Supper and baptism as practised.** Sattler's charges include "placing the bread and wine on a plate, and eating and drinking the same" (lines 58705–58706) (row 13). At Zollikon the believer Jörg Schad says of the table that "si habind ein brot (ge)brochen und in dem namen (Gotts) geessen" (lines 18134–18135) (row 31). These are accounts of practice by participants or by the Zurich court.
- **Social background.** The Zollikon list in Nr. 636 names men and their sons and several servants of named masters, for example "Heini Giglis Knecht" (line 18110). Bossert's and Egli's registers hold names and places (rows 32 and 31). A social profile of the believers was not made. The Hutterite communal order is described in the chronicle (rows 27 and 26), but the ordinances are not on the shelf (row 84).
- **Surrounding religious environment.** The Catholic, Lutheran and Reformed churches appear as persecutors and as hostile writers (rows 40 to 45, 31, 32). The Moravian lords appear in the Brethren's address to them (row 25). No non-Christian religious voice is on the shelf.
- **The gap is stated, not filled.** The daily life of a Swiss household, a Dutch congregation and a Moravian communal household cannot be reconstructed from what is vendored beyond the points above.

## 6. Source Asymmetries and Missing Voices

Under Article 20 the first duty is to name whose voices the sources structurally omit, and why.

**Overrepresented.**
- The believers who were caught and killed. The *Mirror* is a book of martyrs. Egli and Bossert are the files of courts.
- The Dutch wing in English, which has the widest English coverage on the shelf (Menno, Dirk, the *Mirror*, Dordrecht).
- The Hutterite Brethren's institutional memory, the largest German text.
- Male leaders and ministers, and the compiler's and editors' frames (Mennonite publishers, academic editors).
- The opponents in print: Zwingli and Calvin are on the shelf in clean English.

**Structurally missing, and why.**
- **The believers never arrested.** The two main genres, the court record and the martyr book, record only people who were taken. A believer who was never questioned and never killed has no entry. This is a feature of the genres.
- **Women.** They appear as martyrs (Anna of Rotterdam, row 15), as names in the Zurich lists, and as the "sisters" Sattler addresses ("beloved of God, brethren and sisters" (lines 58967–58968), row 13). Egli's Nr. 934 says "Auf dieselbe Weise sollen Frauen und Töchter behandelt" (lines 28331–28332) and Nr. 936 names "männer, frowen noch dochteren" (lines 28370–28371) among those who would be drowned. Only Anna writes. No woman speaks in the Swiss or the Moravian wing.
- **Children and the very poor.** They do not speak. Anna writes to her son (row 15). The Zollikon list names servants (row 31) who answer as part of a group.
- **The Swiss wing after 1527.** The shelf has Schleitheim, Sattler's answers, the undated Ausbund, and the *Mirror*'s summaries for 1614 to 1645. The Swiss tracts of the century between are not on the shelf. The Swiss voice is almost wholly the voice of the Zurich court.
- **Marpeck, Denck, Grebel, and Hubmaier's earlier writings.** Not on the shelf (rows 69, 66, 70, 51).
- **The magistrates and lords who tolerated them.** The *Mirror* prints three acts of the House of Orange for the Anabaptists of Middelburg (row 19). William I granted a letter of privilege (from line 147918), dated at Middelburg on "the 26th of January, A. D., 1577" (lines 148004–148005). It answers a complaint that the magistrate had closed the believers' shops because they would not render the customary oath. A second charge to the magistrate (from line 148155) is dated at Antwerp on 16 July 1578 and orders that they be left in peace. The compiler's Remark says the toleration lapsed: "after the decease of that good prince they began again" (lines 148235–148236). It says that this renewed oppression "was terminated by a third prohibition, by his son" (lines 148238–148239). The son is Maurice. His letter to the Middelburg magistrates, dated "Gravenhage, on the 4th of March, 1593" (line 152809), asks them to let the believers keep the liberties granted in the time of his father. So the son restored the toleration and did not end it. The Moravian lords do not speak. The Brethren's address to them is on the shelf, and their answer is not (row 25).
- **The persecutors beyond their texts.** The Habsburg and Reich side speaks in mandates (Ferdinand's order of 26 January 1528 and the legal texts in Bossert's Einleitung, row 32). Catholic, Lutheran and Reformed lay opinion is absent.
- **The daily life of a congregation.** No source records a Swiss household, a Dutch congregation or a Moravian communal household as an ordinary week (§5).

**Coerced testimony.** The court files are not plain inside voice. The Zollikon believers of Nr. 636 answer as prisoners. Bossert's volume uses "peinlich" on 51 lines, for example an order to question two men "peinlich zu befragen" (lines 3053–3054) with the executioner, and "gütlich" (mild) on 19 lines. So the file holds interrogations under torture and under milder terms. The *Mirror* prints a sentence in which the court says Dirk Willems confessed "without torture and iron bonds (or otherwise) before the bailiff and us judges" (lines 104714–104716) (row 16). That is the court's statement. Neither file marks which of its answers were given under torture. This document does not soften the caveat. It also does not treat every court answer as coerced in the same way.

**Evidential visibility is not ecological visibility.** The shelf is heaviest where a community kept its own books (Dutch, Hutterite) or where an archive of the persecutors survived (Zurich, Württemberg). The most formative things for a believer were probably the examination of a candidate before baptism, the ban and the household in which a congregation met. The shelf shows the ban's controversy (Menno, Dordrecht, Schleitheim) and the Zollikon baptisms. It does not show an ordinary examination or an ordinary household. Where a reconstruction goes beyond the evidence it is marked *Inferential/Thin*. A bounded reconstruction of any missing voice needs a specific textual trace and is not attempted here.

**Forces lens (Forces Framework V1.1, Section 4, Step 2).** The forces are those of Doc_01 §5, in its six cells (Layer 1 only).

*Which sources speak to external forces.*
- **Cell 1A, Zwingli's slow and state-bound reform.** The Zurich council's decisions of 18 and 21 January 1525 (Egli Nr. 621 and 624, row 31). Zwingli's reply, in which he quotes the articles (row 40). The Chronicle's account, in which Zwingli, "welchem vor Christi Kreuz, Schmach und Verfolgung grauset" (lines 5460–5461), will not go on and says an uproar would follow (row 27). Hubmaier's dialogue against Zwingli's baptism booklet, as a second witness (row 36).
- **Cell 2A, criminalisation by every confession.** The council's mandate of 7 March 1526 and its sentence on Mantz (row 31). Ferdinand's order of 26 January 1528 and the Reich texts in Bossert's volume (row 32): of the Frankfurt standstill of 1539 Bossert prints "Dieselbigen sollen auch von keinem teil geduldet werden" (lines 1296–1297), that is, neither party was to tolerate them, and of the treaty of Kadan of 1534 that rebaptisers were "und in ihren landen nit geduldet noch gelitten werden" (lines 1286–1287). Sattler's sentence (row 13). Menno on the law of Theodosius (row 6). The hostile confessions (rows 43, 44, 45, 42).
- **Cell 2A, the exceptions.** The acts of William I in 1577 and 1578 and of Maurice in 1593 (above). The Moravian nobles' protection, which Vedder describes: the nobles, he says, answered the king's edicts of persecution with a refusal until Lichtenstein died in 1572, when Nikolsburg changed (row 34, lines 9529 to 9545). The Brethren's own address to the lords, which asks them to hear the Brethren (row 25).
- **Cell 2A, Münster.** The movement's repudiations (rows 1, 6, 10, 25). No Münsterite text is counted.
- **Cell 3A, the endings.** Vedder on the royal decree of 1623: "In 1623 a new royal decree for the persecution of Anabaptists was issued through Cardinal Dietrichstein" (lines 9627–9629) (row 34). The Swiss entries of 1614 to 1645 and the Amsterdam supplication of 1642 (row 18).
- **Internal forces, Cells 1B, 2B and 3B.** The gathered church as a conviction: Menno's account, the Chronicle's origin story, Hubmaier's creed (rows 1, 27, 34). The ban and shunning: Schleitheim's Second Article, Dordrecht XVI and XVII, Menno's *Excommunication* (rows 22, 20, 5). Community of goods: Vedder on the Stäbler, the Brethren's 1545 address ("Der Gemainschafft halber" (line 11289)), the Chronicle (rows 34, 25, 27). The sword: Hubmaier's treatise (row 35). The consolidation at Dort in 1632: Dordrecht itself, signed by ministers of the united churches at a peace convention (rows 12, 21).

*What the silences show.*
- The authorities speak through mandates and sentences. Their deliberations are not on the shelf. The Reich texts in Bossert are printed from seventeenth- and eighteenth-century collections (Goldast, 1712 and 1713), so the legal frame reaches us at second hand.
- The Swiss own voice falls silent after 1527 on the shelf, while the persecution of the Swiss was still active in the 1640s (row 18). The silence is a silence of the record and does not mean the Swiss ceased to write.
- No source has the economy as its subject. The Brethren's address to the lords touches tax and community of goods (row 25). Confiscation of property appears in the sentence on Mantz: "Sein Gut ist meinen Herren verfallen" (line 33753).

*Survivorship patterns.*
- What survives is what a community kept or an archive filed. The Hutterite manuscript stayed with the Brethren. Wolkan says it is in America and that Beck thought it lost in 1883 (row 27). The Ausbund went on being sung. The *Mirror* was compiled in 1660 from earlier martyr books (row 11).
- The persecutors' archives survived and were published: Zurich in 1879, Württemberg in 1930. The shelf therefore sees Zurich and Württemberg through the courts and does not see, for example, the Swiss valleys through the believers.
- Schleitheim survives in many copies and in Zwingli's hostile translation (row 23). A text that the opponent chose to refute survived better than a tract nobody refuted.
- These patterns are consistent with legal persecution as the force that shaped what was kept. That is an effect of what survives. It is not a finding that persecution was the most threatening force.

## 7. Required Disclosure

**1. The celestial-flesh Christology (Step 0 §4 item 1; Doc_01 §7 item 1, binding).**
- *What the shelf holds.* Menno's words (row 2). Dirk's chapter title and text (row 9). The friar's charge and Herman's answer (row 17). Dordrecht Article IV and its refusal to fix the mode (row 12). The Waterlander Article VIII (row 21).
- *Result, at its own strength.* *Contested* within the Dutch wing's own record, as Doc_01 §7 item 1 requires. The words are *Documented*. Menno: "the whole Christ Jesus, God and man, man and God, is from heaven and not of earth" (lines 48892–48894). Dirk's title says Christ's flesh is "not of Mary". The Waterlander text keeps the incarnation inside the virgin's body: "who in the body of the virgin Mary was made flesh or man" (lines 1702–1703). Dordrecht says that the Word became flesh and, on how this was done, "we content ourselves with the statement pertaining to this matter which the worthy evangelists have left us in their accounts" (lines 5657–5660). The resolution toward "the Dutch wing denied Christ's full humanity" is not supported, and the resolution toward "there is no real tension" is not supported.
- *The sieve-and-spout image.* It appears in the friar's mouth only (row 17). It does not occur in Menno's volume (row 2). Any later document must keep the positive wording of Menno and Dirk and not the caricature.
- *Dutch-wing only.* Hubmaier's creed says "thou wast conceived by the Holy Spirit, without any human seed, born from Mary, the pure and ever chaste virgin" (lines 5136–5138) (row 34). The Moravian Brethren in 1545 say Christ was "In Maria der Jungfrau vermenscht" (line 11240) (row 25), which uses the same preposition as Dordrecht and says nothing on the mode. Nothing in the Swiss or Moravian record on the shelf teaches that Christ's flesh was not Mary's. Later documents should not extend the complication to those regions.
- *The in/by check Doc_01 asked for.* The 1632 Dutch is not on the shelf, so the check against it cannot be made. The English texts disagree (Sohm "in", Elkhart "by"). Dirk uses "in Mary" while denying Mary's flesh. Dordrecht declines to say how. The Moravian paragraph of 1545 also says "In Maria". The preposition therefore proves nothing on the point and stays corroborating only (OG-5).

**2. Marpeck unsourced, Hubmaier partly recovered (Step 0 §4 item 2; Doc_01 §7 item 2, binding).**
- Marpeck has no text on the shelf. Four files name him and a Bossert footnote points to a 1929 edition that was not found (rows 69 and 87).
- Hubmaier is now heard in three ways. *On the Sword* is complete in English (row 35). The Twelve Articles are printed in full in English (row 34). Six other titles are on the shelf as second witnesses (rows 36 to 39). His 1524 to 1525 writings and two further reels are not on the shelf (rows 51 and 52). Davidson's English of 1939 is closed (row 67).
- The named voices that speak in readable words on the shelf are Menno, Dirk Philips, Hubmaier (two texts), Peter Riedemann (the letters the Chronicle prints, in modernised German), Anna of Rotterdam, Herman, Leonhard Schoener, Hans van Overdam, Mantz (one admonition at second hand) and, collectively, the Hutterite Brethren, the Swiss Brethren at Schleitheim and the churches of Dort. Marpeck, Denck and Grebel have no readable words of their own. Riedemann's book has none, and his letters are the only text of his that the shelf can quote. The world's argument must not rest on more named voices than these.

**3. The Schleitheim Confession's once-removed provenance (Step 0 §4 item 3; Doc_01 §7 item 3, binding).**
- Wherever the Confession is cited, the English is a translation of Zwingli's Latin, which Zwingli made from a Bernese copy of the German (rows 22, 40, 23). Two English renderings of that Latin exist and they differ in wording.
- The German is on the shelf twice. Beck's text is readable and shortened, and its Fourth Article lacks the clause on weapons (row 24). Böhmer's is complete and garbled (row 23).
- McGlothlin's file lacks printed pages 6 and 7. It breaks off in the Fifth Article and resumes with the last paragraph of the Sixth, which ends "that the body may remain whole and united" (lines 651–652). It has the Sixth Article's closing lines (lines 647–654), but not its heading or its statement on the sword. The same closing argument is in Jackson's English: "Since therefore Christ is as he is described, the members must necessarily be such" (lines 8281–8282). The Sixth is read in full in Jackson's English and in Beck's German.
- McGlothlin's claim that the German was never printed is wrong on Böhmer's evidence. The Library's file header repeats it in other words: "the original German articles were never printed" (lines 18–19). The corpus-map note says only that the German "survives only in archival manuscript". The once-removed caveat on the English stands.
- Doc_01's quotations of the Second and Fourth Articles are in the McGlothlin English and are correct there. They are not quotations of the German.

**4. Swiss, Moravian and Dutch coherence (Step 0 §4 item 4; Doc_01 §4, §7 item 4).**
- Dutch: Dordrecht, Menno, Dirk in English (affirmative evidence on the five commitments, and the evidence for non-resistance, the oath and the ban in the corporate voice).
- Swiss: Schleitheim at two removes, Sattler's trial answers, the Ausbund, and the Zurich file (coerced).
- Moravian: the Chronicle, Vedder's account of the Stäbler, and a new source that Step 0 and Doc_01 did not use: the Brethren's own address of 1545. In it they state an affirmative creed paragraph (§7, Article 4 check below). They state that obedience to rulers has a limit, "daz man Gott mer, dann den menschen gehorsamen soll" (lines 11256–11257). They refuse a war tax and the hangman's money: "Wo man aber Etwas, das von Gott nit geordnet" (lines 11268–11269) is asked of them, "als Steuer in krieg vnd henkhergelt oder andere sachen, die einen Christen nit gebüren" (lines 11270–11271), they cannot agree. They say that those who came with goods "freiwillig von inen gegeben zur vnderhaltung der Witwen vnd Waysen oder Notturfftigen" (lines 11312–11314) (row 25). The refusal of a war tax and the free giving are consistent with Doc_01 §4's reading that non-resistance did not divide the strands, and they come from the Moravian wing's own voice.
- Boundary note. Doc_01 names three regions. The Registry also rows files about neighbouring places (Württemberg in Bossert; Tyrol, Austria and South Germany in the chronicle). They are Native by tradition and subject. The lead is asked to confirm (OG-9).

**5. The Münster exclusion and the Donatist comparison (Step 0 §4 item 5; Doc_01 §7 item 5).**
- The exclusion is a scope decision and not a confidence-rated claim (Doc_01 §5). The movement's own repudiations are on the shelf in four places (§3 item 12).
- Menno reports that he met a Münsterite leader twice: "I conferred twice with one of" (line 545) their leaders (row 1). That is consistent, from his side, with Doc_01's statement that Menno's milieu and Münster's were close. It does not test Doc_01's claim about the Melchiorite milieu.
- The Donatist rejection is in Menno and Dirk (rows 6 and 10). The dossier's note that Ribbeck and von Soden compare the Donatists with the Anabaptists is not borne out: Ribbeck has two passing sixteenth-century remarks, a contrast with Münster and a likeness between Rothmann and Novatian, among ten uses of "Wiedertäufer" that otherwise name the Donatists. Von Soden uses the word only for third-century rebaptisers (rows 49 and 50).
- No Münsterite or eyewitness text is counted. Rothmann is rowed as a Named Comparandum (row 80).

**6. The Täuferakten and Harder (Step 0 §4 item 6; Doc_01 §7 item 6, binding).**
- The Täuferakten volume for Württemberg and the Zurich acts are on the shelf (rows 32 and 31). The later volumes of the series and Harder's English edition are in copyright and not reachable (rows 63 and 62). They are named and closed for acquisition.
- Doc_01 said that these records would show ordinary believers' words only as transcribed by their persecutors. That is confirmed for Nr. 636 (§6).

**7. Author Gravity and the Article 20 duty (Doc_01 §7 item 7, binding).** The richest sourcing is confessional and martyrological. The court testimony is coerced evidence, and the caveat is carried in §6 without softening.

**8. Living Tradition status (Article 29).** Pending the project lead's own act. Every English edition of the Dutch wing's own books was made by Mennonite publishers, and the Hutterite chronicle by the Hutterian Brethren. What this world says of the movement is mediated by the heirs' own editions, as it is by the opponents' archives (§1).

**9. No page images.** The German scans were not checked against page images. The file headers require that check before any passage is used. German quotations in this document carry weight. They form the Moravian column of the Article 4 check, and they support §3 items 1, 5, 6 and 11 and the forces lens. Each stays provisional until its page image is read (OG-3).

**10. Wolkan modernised the spelling.** The 1923 text is not the sixteenth-century spelling (row 27).

**11. Editors' summaries are not marked apart.** In Egli and Bossert the OCR does not keep italics, so a document's own words and the editor's summary cannot be told apart in the file (rows 31 and 32).

**12. The census and the shelf disagree in five places.** The census names Anneken Jans where the *Mirror* heads Anna of Rotterdam (OG-8). It calls Sattler the principal author where Böhmer calls him the leader who sent the articles on. It dates the first printing of the Ausbund to 1564, which no vendored text states. It names the Verduin and Wenger edition of Menno, which is in copyright, where the shelf has Funk (row 71). The census also says the Hutterite Chronicle holds "the only account of the first believers' baptism". The Zurich file holds another, for Zollikon (row 31).

**13. The corpus-map row for McGlothlin names the Dordrecht Confession.** The volume introduces the Confession and does not print it (row 21). The dossier's count of three English copies is two (row 74).

**Article 4 check.** The five commitments, as Step 0 quotes them:
(1) "One God, the Father, the Almighty, maker of heaven and earth, of all that is, seen and unseen."
(2) "Jesus Christ as the only Son of God, eternally begotten of the Father, God from God, Light from Light, true God from true God, begotten not made, of one Being with the Father."
(3) "Jesus Christ as truly human — incarnate of the Holy Spirit and the Virgin Mary, 'became truly human.'"
(4) "Christ's death under Pontius Pilate, burial, bodily resurrection on the third day, ascension, and his return in glory to judge the living and the dead."
(5) "The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son."

Each wing is tested on its own words. A clause not found is silent, not denied.

| | Dutch wing | Moravian wing (1545) | Swiss wing | Hubmaier |
|---|---|---|---|---|
| (1) | *Shown.* Dordrecht I: "we confess with the mouth, and believe with the heart, with all the pious, according to the holy Scriptures, in one eternal, almighty, and incomprehensible God, the Father, Son and Holy Ghost" (lines 5499–5502) and "we believe and confess that He is the Creator of all things visible and invisible" (lines 5511–5512) (row 12). Dirk: "The Father, Son and Holy Ghost, then, is the only true and living God and Lord" (lines 20544–20545). | *Shown in substance.* "daz Wir glauben an den Ainigen, Ewigen lebendigen Gott" (lines 11234–11235), "der himel vnd erd vnd was darin ist erschaffen hat vnd erhaltet" (lines 11235–11236) (row 25). "Father" and "almighty" are not found in the first sentence. | *Not found* in the Swiss voice on the shelf. | *Shown.* "I believe in God, Father Almighty, maker of heaven and earth" (lines 5104–5105) (row 34). |
| (2) | *Shown in part.* "who is God's only, first and own Son" (lines 5643–5644) and "whose goings forth have been from of old, from everlasting" (lines 5637–5638). The Waterlander text: the Father "begat his Son from eternity" (line 1534), "before all creatures" (row 21). "Light from Light", "begotten not made" and "of one Being" are not found in the passages read. | *Shown in part.* Christ is "der mit Gott dem Vater ains im wesen" (line 11239), of one being with God the Father. | *Not found.* | *Shown in part.* "I believe also in Jesus Christ, thine only begotten Son, our Lord" (lines 5124–5125) and "I believe he is Christ, true God and man" (lines 5131–5132). |
| (3) | *Shown, with the Contested complication* (§7 item 1). Sohm: "was conceived in the virgin Mary" (lines 5621–5622). Elkhart: "conceived by the Virgin Mary" (line 337). Waterlander VIII: "through the admirable power of God and the incomprehensible operation of his Holy Spirit" (lines 1703–1705). | *Shown in part.* "In Maria der Jungfrau vermenscht" (line 11240). The Holy Spirit's part is not found in the paragraph. | *Not found.* | *Shown.* "thou wast conceived by the Holy Spirit, without any human seed, born from Mary, the pure and ever chaste virgin" (lines 5136–5138). |
| (4) | *Shown, except "in glory".* Dordrecht IV: "suffered under the judge, Pontius Pilate" (lines 5672–5673), "was crucified, dead, was buried, and, on the third day, rose from the dead, and ascended to heaven" (lines 5673–5675), "whence He will come again to judge the quick and the dead" (lines 5676–5677). | *Shown in part.* Ascension only: "nach seinen todt wider geen himel aufgestigen ist" (lines 11241–11242). Burial, the third day and the return are not found. | *Shown in part*, in Sattler's answer: "Christ ascended into heaven and, sitteth on the right hand of His heavenly Father" (lines 58747–58749) and "whence He shall come to judge the quick and the dead" (lines 58749–58750) (row 13). | *Shown.* "wast crucified, dead and buried" (line 5155), "didst rise again from the dead for our sakes" (lines 5180–5181), "thou wilt come to judge the quick and the dead on the day of the last judgment" (lines 5208–5210) and "in his great glory and majesty coming in the clouds of heaven" (lines 5212–5213). |
| (5) | *Shown in part.* The one God is "Father, Son and Holy Ghost" (Dordrecht I). Waterlander III: the Spirit is "proceeding from the Father" (line 1539). "Lord and giver of life" is not found. | *Shown in part.* "welcher Geist von dem vater vnd son ausgangen vnd mit dem son vnd vater in der krafft vnd wesen ain Gott" (lines 11244–11245). | *Not found* in the Swiss voice. The *Ausbund*'s Confessio of Thomas von Imbroich names the Father, the Son and the Holy Spirit in the baptismal formula (lines 38814 to 38830, garbled; not quoted). | *Shown.* "I believe also in the Holy Spirit, who proceedeth from the Father and the Son, and yet with them is the only and true God, who sanctifieth all things" (lines 5241–5243). |

*Result.* The floor evidence is affirmative for the Dutch wing, for Hubmaier (all five commitments, in English) and in part for the Moravian Brethren's own paragraph of 1545. For the Swiss wing only commitment (4) is shown, in part, in Sattler's answers. This adds to Step 0 §2 A1, which found no affirmative parallel for the Swiss or Moravian wings, and which noted that Hubmaier's material in Vedder might bear on the question once read in full. It does. Step 0 is not reopened. The addition is reported for the lead (OG-10). Schleitheim itself touches none of the five (Step 0 §2 A1).

## 8. Confidence Map

| Claim | Confidence | Basis |
|---|---|---|
| The first adult baptisms were performed at Zurich in January 1525. | *Widely Accepted* | The census and Doc_01. The Zurich council's decisions of 18 and 21 January 1525 and the Zollikon trial of 7 February 1525 are consistent with it; no vendored text dates the act (Egli Nr. 621, 624, 636, row 31). |
| Fourteen Zollikon believers answered a Zurich court in early 1525 and told of their baptism. | *Documented* | Egli Nr. 636 (row 31). |
| Grebel baptised Blaurock and Blaurock then baptised the others. | *Documented* as the Chronicle's account; one witness on this shelf | The Chronicle (row 27). Nothing on the shelf contests it. For Zollikon, Egli has Blaurock and Mantz baptising (row 31). Doc_01 §2 rates it *Documented* (OG-18). |
| The Schleitheim articles were adopted at Schlatt on 24 February 1527. | *Documented* | Böhmer, Beck's heading and McGlothlin's manuscript title (rows 23, 24, 22). |
| Sattler led the meeting and sent the articles on. | *Documented* as Böhmer's statement | Row 23. |
| Sattler wrote the articles. | Not attested on the shelf; *Widely Accepted* in the census | Rows 23, 13. |
| The German Schleitheim text was printed in the sixteenth century. | *Documented* | Böhmer (row 23), against McGlothlin (row 22). |
| The refusal of the sword is in the Sixth Article of every text that has the Sixth's opening (McGlothlin's file has only its closing paragraph), and in the Fourth of the English and of Böhmer's German but not of Beck's. | *Documented* for the texts | Rows 40, 24, 23, 22. |
| Sattler was executed on 21 May 1527. | *Documented* | Böhmer states it (row 23). The *Mirror*'s closing date line is consistent (row 13). The Chronicle gives 21 May for the arrest (row 27). |
| The Zurich council ordered drowning for repeat rebaptism (7 March 1526). | *Documented* | Egli Nr. 936 and 937 (row 31). |
| The Zurich council sentenced Felix Mantz to drowning on 5 January 1527. | *Documented* | Egli Nr. 1109 (row 31). The *Mirror*'s 1526 stands alone against it (row 14). |
| Mantz was drowned on that day. | *Widely Accepted* | The sentence orders it; the execution is not recorded in the entry. |
| The Reich estates agreed in 1534 and 1539 not to tolerate Anabaptists. | *Documented* as Bossert's printed texts | Row 32, printed from collections of 1712 and 1713. The texts themselves were not checked against the originals. |
| Menno left the Church of Rome, doubted infant baptism and never took part in Münster. | *Documented* as his own account | Row 1. |
| Menno died in 1559. | *Contested* | The *Mirror* against Funk's Note 1 (row 3). |
| Menno and Dirk taught that Christ's flesh did not come from Mary. | *Contested* as a characterisation; the words are *Documented* | Rows 2, 9, 17. |
| Menno taught that Christ passed through Mary "as water through a sieve". | Not supported | The friar says it and Herman denies it; Menno's text has no such image (rows 17, 2). |
| Dordrecht Article IV says the Word became flesh and declines to fix the mode. | *Documented* | Row 12. |
| The Dordrecht Confession was adopted at Dort on 21 April 1632. | *Documented* | The *Mirror*'s heading (row 12). |
| The Waterlander confession dates from about 1580. | *Documented* as McGlothlin's dating | Row 21. |
| The Stäbler left Nikolsburg for Austerlitz in the summer of 1528. | *Documented* as Vedder's account from the chronicle | Row 34. |
| The Moravian nobles protected the Brethren until 1572 and later; a royal decree of 1623 ended it. | *Documented* as Vedder's account | Row 34. |
| William I granted the Anabaptists of Middelburg a letter of privilege (26 January 1577) and charged the magistrate to leave them in peace (16 July 1578). The toleration lapsed after his death, and his son Maurice restored it by a letter of 4 March 1593. | *Documented* | The three acts and the compiler's Remark, as printed in the *Mirror* (row 19). |
| Felix Landis died of hunger in prison at Zurich in 1642. | *Documented* as the *Mirror*'s statement | Row 18. |
| The Twelve Articles are Hubmaier's own and contain all five Article 4 commitments. | *Documented* in Vedder's English | Row 34. The German print is not on the shelf and the translator is not named. |
| The Moravian Brethren in 1545 stated an affirmative creed paragraph. | *Documented* in Beck's shortened print | Row 25. |
| The Hutterite Chronicle was begun by Braitmichel, carried on by Kräl and Zapff, and survives in the Brethren's hands. | *Documented* as Wolkan's statement | Row 27. |
| The Ausbund hymns were written in the prison at Passau. | *Inferential/Thin* on the shelf; *Widely Accepted* outside it | The title page's claim only (row 29). |
| The Ausbund was first printed in 1564. | Not attested on the shelf; *Widely Accepted* in the census | Row 29. |
| "Anna of Rotterdam" is "Anneken Jans". | *Inferential/Thin* | The names are joined only by the census (row 15). |
| Dirk Willems turned back on the ice. | *Widely Accepted* as the tradition's story, Tier 2 | The compiler's "trustworthy persons" (line 104653, row 16). The court's sentence of 16 May 1569 is *Documented* from the town record. The seventy cries are *Inferential/Thin*. |
| A letter to the Zurich council is Blaurock's. | *Contested* | Egli's own question mark (Nr. 646, row 31). |
| The Swiss and Moravian wings affirm the five commitments. | See the Article 4 check in §7 | Moravian in part (1545); Swiss only commitment (4), in part; Hubmaier all five. |

**Confidence propagation.** The world's outline rests at *Documented*, usually on one editor or compiler: the Zurich file for the early years, the *Mirror* for the martyrs, Vedder for Moravia, and the Brethren's own chronicle. The positive teaching of the Dutch wing rests on English translations that cannot be tested against the Dutch. The Swiss wing's own voice rests on a text at two removes. Daily practice, the Swiss after 1527 and the Moravian household rest at *Inferential/Thin* or on no evidence at all. The Hubmaier and Moravian floor evidence is *Documented* but narrow.

## 9. Search record, field-bibliography sweep, and saturation

**Search record (STARLITE headings).**

*Sampling strategy:* the 842 entries of `cic/texts/` (797 `.txt` files, 38 `.xml` files and 7 others) were searched by full text. The corpus map (26 rows), the Source Readiness Dossier (sections 1 to 6), the census entry VI.3, the Library decision log, Step 0 and Doc_01 were read.

*Terms:* one case-insensitive regular expression, `anabapt|catabapt|wiedert[aä]ufer|wiedertoeuf|\bt[aä]ufer|menno\b|mennonit|hutterit|hutterisch|hubmaier|ausbund|\bamish`, applied to every file. Surname counts, with the spelling variants found in the files: Marpeck and Marbeck; Denck; Grebel; Blaurock and Blabrock; Riedemann, Ridemann, Riedeman and Rideman.

*Type:* source discovery for a construction step.

*Approaches:* full-text search; corpus-map and dossier read; census fields; footnote and preface snowball in the vendored apparatus (Vedder's Bibliography, Böhmer's introduction, Beck's Vorrede, Funk's Publishers' Preface, McGlothlin's notes, Bossert's footnotes); title and creator queries on `archive.org`.

*Instruments:* Python 3 regular-expression scan; `grep -l` and `grep -c` in `C.UTF-8`; the `archive.org` advanced-search and metadata interfaces.

**Date:** 23 October 2026.

*Results.* The pattern matches 167 files by two methods. Twenty-five are this world's files (all 25 match). The 142 others include files that matter to this world and are assigned only to other worlds: Crespin's martyrology, Brandt's history of the Low Countries, Voetius, Foxe, Beza, the Index of prohibited books (Reusch), the Schwenckfeld volume and Zwingli's Latin works. They are listed in `Open_Gaps_Tracking.md` and licensed for nothing. Name counts over every `.txt` file of the shelf, with the spelling variants named, by two methods (a regular-expression scan and `grep -o`): "Marpeck" or "Marbeck", 5 files and 9 occurrences; "Denck" as a string, 11 files and 27 occurrences (six of Beck's seven are the word "Denckbüchel", the memorial book, and none is a text of Denck's); "Grebel" or "Gräbel", 7 files and 215; "Blaurock", "Blabrock" or "Blaurok", 6 files and 81; "Riedemann", "Ridemann", "Riedeman" or "Rideman" (Beck's single "Riedmann" is not counted), 5 files and 95. The Chronicle spells Riedemann "Rideman" and Blaurock "Blabrock", so a search on the modern spelling alone undercounts both.

**Scan quality, by two methods.** The Library measures the share of word tokens that read as words. A second measure, the share of letter-run tokens that are one of 46 common German function words (*und, der, die, das, nicht, ist, sie, er, es, in, zu, den, von, mit, auf, für, ein, eine, dem, des, im, auch, wir, ich, so, wie, als, aber, dass, daß, wird, sich, bey, nach, oder, da, wer, ihr, sein, sind, hat, haben, wenn, dann, also*), counts independently of any dictionary. Clean German prose of this period gives about 0.27 to 0.33. The sixteenth-century print spells "vnd", so the Hubmaier reels read lower than their quality alone would give.

| File | Library measure | Function-word share (tokens) |
|---|---|---|
| Wolkan 1923, clean scan | 0.93 | 0.329 (343,350) |
| Wolkan 1923, microfilm | 0.57 | 0.071 (394,697) |
| Ausbund 1856 | 0.90 | 0.276 (134,834) |
| Ausbund 1846 | 0.53 | 0.063 (143,476) |
| Beck 1883 | readable, sampled at five points | 0.274 (238,397) |
| Bossert 1930 | clean, sampled at five points | 0.289 (454,694) |
| Egli 1879 | clean, sampled at five points | 0.266 (426,066) |
| Riedemann 1902 | garbled throughout | 0.057 (84,815) |
| Böhmer 1910 (whole file) | Antiqua clean, Fraktur garbled | 0.095 (17,311) |
| Hubmaier 1526, Gesprech | about 0.6 word-like | 0.113 (21,039) |
| Hubmaier 1527, Grund und Ursach | about 0.73 of windows readable | 0.110 (22,528) |
| Hubmaier 1527, Nachtmal, Bann, Freiheit | about 0.84 of windows readable | 0.138 (17,936) |
| Hubmaier 1527, Freiwilligkeit, Schwert | about 0.86 of windows readable | 0.135 (21,856) |

The two measures agree on which files are clean and which are not. The second measure cannot grade the Hubmaier reels finely, and the Library's own reading of them stands.

**Sweep of the apparatus and of `archive.org`.** Thirty-eight title and creator queries were run on `archive.org`: 27 first runs, four repeats in simpler form after a connection error, and seven for the works named in the recall test below. The metadata of 12 of the dossier's section 3 identifiers were fetched again, and each title and year matches the dossier (rows 51 to 61). The productive queries returned the *Bibliotheca Reformatoria Neerlandica*, Kessler's *Sabbata*, Burrage, Cornelius, Strickler, Bullinger's *Reformationsgeschichte*, Zwingli's *Werke*, Rothmann, Gresbeck and the German Mennonite histories (rows 88 to 97, 80). The unproductive ones are named in the Registry's saturation statement.

**Field-bibliography sweep: run in part.** The vendored bibliographies were swept (Vedder's list of 26 Hubmaier writings and his list of other sources). The `archive.org` interface was swept for the works they name. Instruments not reached are coverage limits: the Global Anabaptist Mennonite Encyclopedia Online (HTTP 403 from this environment); Hillerbrand's *Anabaptist Bibliography 1520 to 1630* (found on `archive.org`, not opened, row 102); the bibliographies of Roth and Stayer and of the *Cambridge History* chapter; Google Books; library catalogues.

**Recall test and PRESS question.** The independent instrument is the reference lists of the English Wikipedia article "Anabaptism", read on 23 October 2026. Ten works that a specialist would expect were taken from it. Five were already in the Registry: Vedder's *Balthasar Hübmaier* (row 34), the *Martyrs Mirror* (rows 11 to 19), the 1987 English *Chronicle of the Hutterian Brethren* (row 72), Marpeck's *Writings* (row 69) and Cornelius on the Münster uprising (row 91). Five were not, and each is now a row as a consultation lead: Williams, *The Radical Reformation* (row 101); Hillerbrand's bibliography (row 102); Stayer, *Anabaptists and the Sword* (row 103); Packull, *Hutterite Beginnings* (row 104); and *The Mennonite Encyclopedia* in print (row 105). Recall before these rows was 5 of 10. The PRESS question was "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly." The answer was Hillerbrand, Stayer, and Newman's *History of Anti-Pedobaptism*. The first two are rowed above, and Newman is rowed as a rights-check lead (row 106). Estep's *The Anabaptist Story* (row 107) and Ruth's *Conrad Grebel, Son of Zurich* (row 108) are rowed too. All of these are secondary scholarship, mostly in copyright. They are acquisition and consultation leads, and no claim in this document rests on them (`Open_Gaps_Tracking.md`).

The saturation statement in the Registry is not closed.

## 10. Open items carried forward

Gaps, requests to the Library thread, candidates on other worlds' shelves and questions for the project lead are in `Open_Gaps_Tracking.md`. In short:

- OG-1: Marpeck unsourced; the Loserth lead. OG-2: Hubmaier's second-witness reels, the leads, the translator of Vedder's English.
- OG-3: no page images for any German scan. OG-4: Schleitheim (the missing pages, the German witnesses, the header note).
- OG-5: the Dordrecht Dutch of 1632 and the corpus-map row for McGlothlin. OG-6: Menno's Dutch and the year of his death.
- OG-7: the Chronicle's editions. OG-8: five places where the census and the shelf disagree. OG-9: the boundary reading for Württemberg, Tyrol and South Germany.
- OG-10: the new floor evidence for the Moravian wing and Hubmaier. OG-11: how court records are to be used. OG-12: the holdings report.
- OG-13: candidates on other worlds' shelves. OG-14: rights and placement rulings. OG-15: older scans' staging notes and the Waterlander author slug.
- OG-16: sweep leads and coverage limits. OG-17: bodies not read.
- OG-18: the sequence of the first baptisms (a Doc_01 rating). OG-19: Sattler's authorship (a Doc_01 rating). OG-20: Riedemann's letters in the Chronicle and Doc_01 §7 item 2. OG-21: secondary scholarship not consulted, and acquisition leads.

**Library-stage outputs in one place.** The corpus map holds 26 rows for this world, each with a Library-issued `row_id`; Doc_02 changes none of them. Proposed corrections to the Library: retitle the McGlothlin row that names the Dordrecht Confession (OG-5); state in the staging notes that Böhmer prints the Schleitheim German (OG-4); settle the Waterlander author slug and the old scans' staging notes (OG-15); decide the weight of the Egli double placement (OG-14). The Vedder volume is rowed twice: as an English biography of Hubmaier that prints the Twelve Articles (row 34), and for *On the Sword* (row 35). Its use as a witness is stated in §1. `cic/corpus-map/PAIRS.yaml` holds only the fixture pair and no ruling for this world, so the sibling relations are the dossier's and not a Library ruling. The dossier names three siblings: the Reformed Cities (the persecutor and the shared Zurich archive), Lutheran Wittenberg (the Augsburg condemnations) and the anti-Trinitarian current, which the floor note keeps separate. Whether any of these becomes a mutual-awareness pair is for the Library and the project lead. The cross-world candidates are in OG-13.

## 11. Disposition

Approved to proceed (Revision 2; Round 1 substantial revision, Round 2 Cleared; review files `Review-Artifacts/Doc02_Round1_Review.md` and `Review-Artifacts/Doc02_Round2_Review.md`; no escalation category applies; items waiting on the project lead are OG-5, 8, 9, 10, 12, 18, 19 and 20; not Frozen; does not change Doc_01).
