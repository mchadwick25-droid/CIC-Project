# C5 coverage map: the Bible, which books, how to read it, one verse at a time

Read-only pass, 26 October 2026; nothing in the repo was edited, no model calls. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; paths, line numbers and verification results are in `search/C5/C5-coverage.json`.

## The sub-questions

| id | sub-question | canonical / question ids |
|---|---|---|
| S1 | Which books, the Apocrypha, who decided, Bible as only authority | C5-02, 04, 07, 16, 27, 30 |
| S2 | How they read: literal or more senses, the OT about Jesus or against Jews, what a modern reader misses | C5-01, 05, 11, 12, 25, 26, 28, 29 |
| S3 | Reliability, errors, authorship, "science disproves it" | C5-13, 17, 24, R-27, R-28 |
| S4 | Genesis and the six days | C5-08, 20 |
| S5 | Revelation and the end | C5-14 |
| S6 | Who could read or own a Bible; language; translation | C5-03, 15 |
| S7 | The violence in the texts; the cursing psalms | C5-06, 21 |
| S8 | One passage at a time (VERSE) | C5-09, 10, 18, 19, 22, 23, R-33 |

## Layer table

R = RENDERED, R* = honest_limit or guard only, or answers part, L = LOADED (vendored, read in context, no record), - = nothing found. IDENTIFIED and OTHER entries are in the JSON.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R | R | R | R | R | R* | L | R* |
| cappadocian | R* | R | - | R* | L | R | R* | R* |
| desert | R | R | R* | R* | R* | R* | R* | L |
| don | R | R | R* | R* | R* | R | R* | L |
| gallic | R* | L | - | L | R | L | - | L |
| hal | R | R | R | L | R* | R | L | L |
| ijc | R* | R | L | L | L | R* | L | L |
| lpc (draft) | R* | R | R* | R | L | R* | R | R* |
| pahc | R | R | R* | R | R* | R | R* | R* |
| rzg | R* | R* | R* | L | L | R* | R* | L |
| syr | R* | R | R* | R | R | R | L | R* |
| witt | R* | R | R* | R* | R | R* | L | L |

Totals: 31 R, 39 R*, 23 L, 3 empty. The saved tool runs are named off by one at the end (`S7-ot-jesus-jews` feeds S2, `S8-violence` feeds S7); S8 has no tool run.

Verification: 32 quote records are cited as RENDERED; all 32 MATCH their vendored file verbatim. Three needed an editorial artifact allowed for (a section number in Dionysius; spacing in Jerome's Hebrew sentence and Ephrem's poison image). No wording changed.

## S8: one passage at a time

File codes: nNNN = `npnfNNN`, aNN = `anfNN`; line numbers in the named file. "Treats" means a homily, commentary or chapter on the passage; shared-volume authors who are not the world's voice are marked (shared). The saved counts in `passages.json` are citation counts and overstate treatment (572 hits on Matt 5-7 in anf09 are Tatian's gospel text).

| passage | treated | cited only or none |
|---|---|---|
| Luke 9:27 | alx Origen on Matt 16:28 (a09:34066); lpc Augustine, Harmony II.56 (n106:6460), Sermon 28 (n106:13729); ijc Leo Sermon 51 (n212:17800) | desert, pahc, syr only via Origen (shared); six worlds none |
| John 1:1-14 | alx Origen Comm. John I.22, II (a09:21212, 22440); lpc Tractates 1-2 (n107:498, 673); pahc Irenaeus III.11 (a01:40845); syr Diatessaron opens here (a09:2195) | don, hal, ijc: Conf. VII.9 (n101:10780) |
| Matt 7:21-23 | lpc Sermon on the Mount II.25 (n106:3117); don Cyprian, Unity (a05:42621); pahc 2 Clement 4 (a09:17831); desert Life of Antony (n204:32179), Cassian XV (n211:39605); gallic Cassian XV; cappadocian Basil, Rules (basil_ascetic:28802) | alx, ijc, rzg, witt cite it |
| Sermon on the Mount | lpc Augustine (n106:729, 1967); pahc Tertullian, Marcion IV (a03:30694); witt Luther, Temporal Authority (luther v3:12060); rzg Zwingli (zwingli:7856); don, cappadocian Cyprian on the Lord's Prayer (a05:44621) | alx, hal, ijc none |
| Genesis 1 | alx Origen (a04:33527); cappadocian Basil Hexaemeron (n208:15203), Nyssa (n205:33984); lpc Augustine (n102:20373, n101:16834); pahc Theophilus II (a02:8692); rzg Calvin (calvin Gen vol1:3162); syr Ephrem (ephraim:887); desert Cassian X (n211:35878) | gallic Sulpitius (n211:6931); witt none |
| Psalm 137 | lpc Augustine on Ps 137 (n108:27073) | hal, desert: Jerome Ep. 22.6 reads "dash the little ones" as crushing evil thoughts (n206:5607) |
| Song of Songs | alx Origen fragments (origen_philocalia:126, 446); lpc Augustine CoG XVII.20 (n102:29636); ijc Ambrose (n210:37062); rzg Calvin on Castellio (calvin letters v1:18297) | Origen's and Nyssa's Song texts are not vendored |
| Luke 15 | ijc Ambrose (n210:35106), Chrysostom to Theodore (n109:7320); alx, desert, hal Tertullian, On Modesty (a04:7827, shared) | witt Arndt (arndt:11483) |
| Isa 41:10, Jer 29:11 | none | witt Arndt only (arndt:16999, 7021) |
| Phil 4:6 | none | Cassian IX (n211:35154); Augustine (n108:7911); Arndt (arndt:16012) |

No record answers any of these except John 1 (alx) and Genesis 1 (alx, cappadocian, lpc, pahc, syr). The pilot's Luke 9:27 gap stands in all twelve worlds. Chrysostom's verse-by-verse homilies on Matthew, John and Philippians are vendored but mapped only to the Antiochene world.

**Is a full per-world passage index feasible?** In two tiers, not one. The 32 ThML volumes (about 27% of the mapped bytes) carry 76,551 `scripRef` tags with book.chapter.verse, and 9 carry 626 `scripCom` tags naming the passage a homily treats: Augustine's Sermon on the Mount, John and Psalms volumes (lpc), Chrysostom on Acts and Romans (ijc), Victorinus on the Apocalypse. That can be built by script, and `cic/texts/STRUCTURE.md` already lists section titles. The other 281 plain-text files (77 Latin, 39 Greek, 29 French, 21 German by filename) have no tags: references appear in prose as "Matt. v. 39", "Matt. 7:23", "Matth. 7, 22", and Vulgate numbering moves Psalm 137 to 136. Counts also cannot tell citing from treating. So script the first tier and hand-curate the second for a fixed passage list, as above.

## World by world

**Alexandria (alx).** Can say, verified: Athanasius's 367 tiers with the Apocrypha read to newcomers; Origen's senses of Scripture; Nepos against allegory; days before the sun not literal; Dionysius doubting Revelation's author yet not rejecting it. Thin: troubling texts, access, the OT as Jews read it. Add: Eusebius HE III.25 (n201:17817) and Serapion on the Gospel of Peter for suppressed gospels; Origen on Matt 16:28.

**Cappadocians (cappadocian).** Can say: unwritten custom beside Scripture; psalms as the unlettered believer's schooling; Basil's close reading. Thin: the six days (Hexaemeron I-III and Making of Man are registered, vendored, unquoted), reliability (nothing), Revelation. The canon list in n207:8395 is Cyril of Jerusalem's, not theirs. Add: a Hexaemeron quote on days, and an honest_limit on the end.

**Desert (desert).** Can say: "the same Scriptures", a verse at a time, honest gaps. Check: `desert.limit.f2-scripture-detail` says no source records a desert voice on Genesis, yet Cassian Conference X (n211:35878), which its own Sarapion story uses, is that debate. Add: Vita Antonii 3 (n204:31296) for access.

**Donatists (don).** Can say: Scripture as books a magistrate could demand, not the only authority, honest limits on canon, Genesis and violence. Gap: Tyconius's Rules (tyconius:247) are vendored and unread; they are the world's only interpreter.

**Gallic (gallic).** Strong only on the end (two verified Antichrist quotes). Nothing on how they read, Genesis or access. Add: Cassian XIV's four senses (n211:38874); honest_limits for reliability and violence.

**Jerome's circle (hal).** Strong on canon, translation and reliability (Helmeted Preface, Augustine on the Septuagint, Jerome's partial Hebrew). Thin: reading method, violence. Add: Ep. 22.6, the ready answer to Psalm 137.

**Imperial-juridical (ijc).** Honest on juridical reading and creed beside Scripture. Everything else is loaded and unrecorded. Add: honest_limits; Leo on Luke 9:27. Ulfila's Gothic Bible is registered, unvendored.

**Latin pastoral (lpc, all draft).** Richest vendored verse-by-verse set and the only substantive violence and Genesis witnesses, none in a package. Add: canon and Apocrypha (Augustine, De Doctrina Christiana II, in n102) and quotes for Tractate 1, Psalm 137 and Sermon on the Mount II.25.

**House church (pahc).** Strong on a fluid canon and public reading; Genesis is not a science question. Thin: Revelation; Irenaeus III.11, 2 Clement 4 and Tertullian on the Sermon unrecorded.

**Zurich and Geneva (rzg).** Sola scriptura answered; nothing on canon, translation or Genesis. Calvin's accommodation passages are at calvin Gen vol1:4104 and 4428.

**Syriac (syr).** Strong on typology, the Diatessaron and Peshitta, Genesis as type. Thin: canon list, violence (Ephrem against Marcion, ephraim:1854).

**Wittenberg (witt).** Two voices on Scripture alone; plain sense is spiritual sense. Thin: canon and Apocrypha, Revelation. Luther's German Testament and prefaces are registered, unvendored (`witt.source.luther-das-newe-testament-deutzsch`).

## Other sources (outside the repo; from working knowledge, not fetched)

Origen's Homilies on Genesis, Joshua and Commentary on the Song (Rufinus, GCS 6-8); Nyssa's Song and Beatitudes homilies; Ephrem on Genesis and the Diatessaron (CSCO); Calvin on the Psalms, Isaiah, Jeremiah and the Harmony (Calvin Translation Society, public domain); Luther's prefaces (Philadelphia Works vol. 6) and Genesis lectures (WA 42-44); Tyconius on Revelation (Beatus recension); Ambrose, Hexameron; Ulfila's Gothic Bible (Streitberg 1908).

## Not checked

- Tool hits are noisy (Marcion, "canonical" as canon law). Cells rest on the records and hand checks, not on counts.
- Shared volumes give hits for the wrong author (Cyril in n207, Origen in anf09, Hippolytus in anf05); flagged in the JSON, not every line traced.
- Latin, Greek, French and German files were counted, not read. Nazianzen's canon poem (PG37) was not located.
- Passage "treats" entries were judged from headings and a few lines around each hit, not whole works.
- `canon/sealed_probes/` was not read. The Pachomian Rule's letters requirement was not checked. The seven record-less worlds are not covered.
