# Era 4 on the live tree (data release 43): review round 2

Reviewer: fresh Opus agent, full effort, independent of the drafting and of round 1. Targeted recheck. Branch `claude/cft-era4-live` at `0e562369`, against `origin/main`. No paid calls.

**Verdict: not yet approved to proceed. 0 blocking, 2 substantial, 6 minor.** Both substantial findings are one-sentence wording fixes in `bagratid-armenian-christianity`. A round 3 recheck can be limited to those two fields and whichever minor fixes are taken.

`node tools/validate-census.mjs --base <origin/main census> --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` passes: `619 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four shortName length warnings carried from release 42). `python tools/check_spelling.py --base origin/main --enforce` passes: 0 British spellings, 0 in enforced trees.

How this was checked. Every R1 finding was rechecked against the census, the profile files and the held lines. Every leaf of the census that changed since `9bfa033c` (28 leaves in 17 entries, none from the merge) was compared old to new, read against its held lines, and scored with `engine.m1.gates.grade_text`. The Agathon scan reading, the brief and the records were read against the Evetts file at l.45959-45965 and 46143-46144. The Decision-Log entry and the Open-Gaps closures and item 264 were checked statement by statement against the branch.

---

## Round 1 findings

| R1 | Status |
|---|---|
| B1 Agathon | Fixed, and better than R1 asked. R1's proposed "The sinner Agathon" was wrong: the sentence starts on the page before, "And as for me," (Evetts l.45965), so the page reads "And as for me, the sinner Agathon, I was the son of the Father Benjamin" (l.46143). The census and brief now quote only "I was the son of the Father Benjamin," and "and knew much of his virtues through my intimacy with him.", both verbatim on l.46143-46144 without any reading. The records quote the full sentence correctly. See M4 for the reading left behind. |
| S1 Spelling | Fixed in the census, the six profile files and the six tree pages. No "travell", "metre" or "catalogue" is left in those pages. |
| S2 Bede teaser | Fixed: the teaser equals the card's knownFor, and it no longer gives 735 as settled. See M5 on its reading ease. |
| S3 Verden | Fixed. See "Checked and holding" for the index lines. M2 is a small leftover in the caveat. |
| S4 Dhuoda | Fixed: no oath, no false dispute. M1 is a small attribution point. |
| S5 Dionysius | Fixed: the closer now agrees with the caveat. M3 is a wording point. |
| S6 Release records | Fixed: the Decision-Log entry, the closures on 254 to 262 and 255, and item 264 are written. The changes file now lists all 18 profile files the branch changes against origin/main. M6 is one count. |
| M1 Harun | Fixed. |
| M2 Maximus | Fixed. "That evening" now follows the hearing, as "Eademque die ad vesperam" does (Relatio l.7497), and the order matches l.7497-7546. |
| M3 830s revolt | Fixed: both `when` lines read "c. 830–832". |
| M4 Symeon | Fixed: "under the patriarch Sergius". Combefis has Sergius still living when Symeon was restored ("Exstinctus brevi post restitutum Symeonem patriarcha Sergius", Calecas PG 152 l.20233-20234, OCR normalized). |
| M5 Cedd | Fixed: "Cedd died 664 or 659; Chad died 672". |
| M6 Reading level | Fixed: Bagratid why FRE 60.5, longDescription 60.2; Macedonian legacy 53.8 (above its 53.4 before this release); Martin FK 8.4; Dionysius FK 9.3. |
| M7 Ormanian's year | Fixed: "put into English in 1912" in all three fields. |
| M8 Narek closer | The stock phrase is gone, but the new phrase claims more than the held lines give. See S2. |
| M9 Moses bar Kepha | Fixed and recorded: the liturgy commentary is kept (Bar Hebraeus vol. 1 l.22907, "5. Commentarius in liturgiam", OCR normalized), and the card's legacy still carries Bar Hebraeus's notice of his commentaries. |

---

## SUBSTANTIAL

### S1. "Pray with it at home" is not in the held line (`bagratid-armenian-christianity`, why)

Current text: "He says Armenians pray with it at home and treat it as a strong charm against every kind of danger."

Held line: "For private prayers there is also used a book called Narek, composed by the monk St. Grigor of Narek (f 1003). This collection, which is written in a florid and sublime style, is regarded as a potent talisman against all kinds of dangers." (`ormanian_church-of-armenia_gregory1912.txt` l.7744-7748). Ormanian says private prayer. He does not say at home. The round 1 fix for reading ease added a place the source does not give. The changes file's own Held line for this field quotes "For private prayers".

Fix: "He says Armenians pray with it in private. They treat it as a strong charm against every kind of danger." This scores FK 7.7, FRE 61.5 for the whole field.

### S2. "For centuries" is not held (`bagratid-armenian-christianity`, documentedStories[1].text, last sentence)

Current text: "The book still carries the name of the house that raised him, and his church used it in its services and in private prayer for centuries."

The first clause holds: Chamich has Gregory "brought up from his infancy in the convent of Narek" (`chamich_history-of-armenia-v2_avdall1827.txt` l.4814-4815). The second does not. The held lines give two dates and no span. Serpos says the prayers "oggidì pure sono in uso nelle sagre funzioni", still in use today in the services, in 1786 (`serpos_compendio-storico-nazione-armena-t2-ita_1786.txt` l.1714-1715, OCR normalized). Ormanian gives private prayer in a book of 1910, put into English in 1912 (l.7744-7745; l.371). No held line says the book was used for centuries, and none says anything of private use before Ormanian. No other held file says it either: the Narek hits in `issaverdens_armenian-ritual-parts1-4_1876.txt` and the other vendored files say nothing of its use over time. R1's suggested wording for M8 caused this, and the branch took it as written.

Fix: "The book still carries the name of the house that raised him. His church still used it in its services in 1786, and in private prayer in 1912." That sentence restates what the text has already said. Ending on the first clause alone is also sound: "The book still carries the name of the house that raised him." The whole story scores FK 8.9, FRE 66.6 with the first version.

---

## MINOR

### M1. Dhuoda: William's death in 850 sits inside the Patrologia note's attribution (`carolingian-reform-christianity`, documentedStories[1].text)

Current text: "William rose to avenge his father, an older editor's note in the Patrologia Latina says, and was put to death as a rebel in 850."

The PL note gives only the rising: "Willelmus patris mortem ulturus, Pippini auxilio Tolosam intercepit" (`eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt` l.112842-112844). The death in 850 is Bondurand's: "Guillaume fut condamné à mort en 850 et exécuté comme rebelle" (`dhuoda_liber-manualis_bondurand1887.txt` l.1833-1834). The sentence makes the note the source of both. The younger Bernard's sentence holds ("ne songea qu'à venger son père et son frère", l.1837-1843).

Fix: "William rose to avenge his father, an older editor's note in the Patrologia Latina says. He was put to death as a rebel in 850." Optionally add the place: "and seized Toulouse".

### M2. Verden: the caveat names Mabillon, but the text no longer introduces him (`carolingian-reform-christianity`, documentedStories[0].caveat)

Current text: "Alcuin's letters on the tithe are known here only through Mabillon's report and the index to his works."

The rewrite took out "Jean Mabillon, who had them, says ...", so a reader meets "Mabillon's report" with no idea who he is or what he reported. Fix: "Alcuin's letters on the tithe are known here only through the index to his works and a note by the scholar Jean Mabillon, who had read them."

### M3. Dionysius: "in his own" can be read as Dionysius's, and the closer recaps the story (`syriac-orthodox-under-islam`, documentedStories[1].text)

Current text: "Bar Hebraeus keeps only a few passages in Dionysius's own words. The journey itself he tells in his own: a patriarch sent as the caliph's envoy, an army that undid his errand, and his return to tell the caliph so."

Just after "Dionysius's own words", "his own" is easily read as Dionysius's, which is the opposite of what the caveat says. The list after the colon then repeats three things the reader has just been told, a summing-up of the kind the writing standard avoids. Fix: "Bar Hebraeus keeps only a few passages in Dionysius's own words. The journey he tells in his own words, not the patriarch's."

### M4. The Agathon scan reading no longer covers any quotation, and the Decision-Log describes the page wrongly (`tools/quote_scan_readings.json`, the Evetts l.46143 reading; Decision-Log, "Era 4 on the live tree", Quotations)

The census and brief now quote only "I was the son of the Father Benjamin," and "and knew much of his virtues through my intimacy with him." Both stand on l.46143-46144 as the scan prints them. "The sinner Agathon" is now unquoted narration. The reading `"scan": "I he sinner Agatbon", "reads": "the sinner Agathon"` is accurate, but it no longer covers any quoted span. The file's own "about" says it is for "Scan faults inside quoted spans", and the validator does not catch an unused reading. Keeping it is harmless, but it is a stale entry, of the kind the project removes rather than keeps.

The Decision-Log says: "the Evetts file prints "the" as "I he", so Agathon's sentence begins "the sinner Agathon"." The sentence begins "And as for me," (l.45965), on the page before.

Fix: remove the reading. In the Decision-Log, write "... written down as 12 readings ... Review round 1 found that one reading, for Agathon's words, added a word: the Evetts file prints "the" as "I he", and the page reads "And as for me, the sinner Agathon". The brief now quotes only the words that follow, which need no reading, and the reading is removed." If the reading is kept instead, say why in the Decision-Log, and keep the count at 13.

### M5. Bede's teaser is just below the reading-ease floor (`bede-of-jarrow`, teaser and card.knownFor)

Current text (it is also the card's knownFor): "Monk and priest of Wearmouth and Jarrow who wrote the Ecclesiastical History of the English nation. He also wrote commentaries on many books of the Bible, drawn from the Fathers, and books on nature and the reckoning of time." Score: FK 9.9, FRE 59.1.

Fix, in `Who-Profiles/era4/batch1/bede-of-jarrow.card.json` and the census: "... He also wrote commentaries on many books of the Bible, drawn from the Fathers. He wrote books on nature and the reckoning of time as well." (FK 7.3, FRE 67.7). Record it with the other approved-profile wording changes.

### M6. The Decision-Log's count of older-text changes takes in one change to a new entry (Decision-Log, "Era 4 on the live tree", Fixes folded in)

Current text: "110 changes to older census text, each resting on a held line."

`Census_Text_Changes.md` has 110 Old/New items. 109 are older text, the count R1 checked. The 110th, "Review round 1, B1: `agathon-of-alexandria`, longDescription", is in an entry new in this release. Fix: "109 changes to older census text, and one to a new entry after review round 1 (Agathon), each resting on a held line."

---

## Checked and holding

- **Verden.** The four new sentences rest on the volume's index: s.v. Fides, "Voluntaria res est, ad quam nemo cogi potest, I, 42, 50" (l.118264-118265); s.v. Saxones, "Non erat decimarum exactione et rigore poenarum vexanda, 51" (l.121659-121660); s.v. Decimae, "Illarum exactio conversioni Saxonum impedimento fuisse censetur, 51, 104" (l.117543-117544). "Is judged to have hindered" renders "censetur" faithfully. The claim that the index "sums up what his letters say" holds. The index's own key says its numbers are Froben's tome and page ("numeri Romani I. II. significant primum vel secundum tomum (juxta divisionem editionis Frobenii), numeri Arabici paginam", l.115273-115274, OCR normalized). The two pages cited for the tithe, 51 and 104, fit the two letters Mabillon names in Froben's numbering, "epistolae 7 et 41 (nunc 33 et 65)" (l.114700-114703, OCR "05"). "The letters' own words are not in the Library's copy" is true: the file holds PL 101 only (title page l.218; Open-Gaps 254, carried in 264). "Saw it otherwise" refers back to the tithe law of the sentence before it, and the title and teaser's "doubts" sit fairly with "objection".
- **Dhuoda.** The rewrite says only what the two notes say, apart from M1.
- **Dionysius.** "Took his leave for Damascus" renders "accepta licentia, Damascum profectus est" (Bar Hebraeus l.21820-21822). The joined sentences hold to l.21798-21822 and l.21905-21923.
- **Maximus.** "For by its decrees it had cast out the four councils" is the Record's "quatuor concilia ejecerunt, per illa novem capitula ... et per ecthesim ... et per typum" (l.7538-7541).
- **Martin.** The joined sentences keep every fact R1 checked. Nothing is added.
- **Agathon.** Both quoted pieces are verbatim at l.46143-46144. The brief equals the census longDescription. Both records claims are corrected. The `audio/agathon-of-alexandria.audio.txt` copy keeps the old wording, and Open-Gaps 264 says so.
- **Narek and Bagratid fields, apart from S1 and S2.** "A former Armenian patriarch of Constantinople ... his book was put into English in 1912" and the legacy and longDescription splits hold to Ormanian l.371 and l.7744-7748, and to Serpos t2 l.1714-1715.
- **Card and brief equality.** Every era 4 brief equals its census longDescription. Every era 4 card's keyWorks, legacy, uncertain and knownFor equal the census. The sources differ only by the census's added `"date": null`. Every teaser equals its knownFor.
- **Reading levels of changed fields.** Every changed story text is between FK 7.8 and 9.3 and FRE 65.8 and 73.4. The Agathon longDescription is FK 7.6, FRE 63.6. The Bagratid why and longDescription are at FRE 60.5 and 60.2. The only field below the floor is Bede's teaser (M5). Fields where only one word was respelled (Beuno longDescription FK 4.3, Elias keyWorks about FRE 44.4) are older text, already counted under Open-Gaps 264.
- **AI tells.** Apart from the recap in M3, no changed line has filler, hedging, assistant cadence or a stock closer.
- **Decision-Log entry, apart from the two placeholders and M4 and M6.** 60 new entries plus Bede make 61 profiles and 64 people. The three pairs are right. Exactly ten voice rows became person links: Boniface, Leoba, Alcuin, Dhuoda, Maximus, Photius, Dionysius, Humbert, Braulio and Ildefonsus. John of Nikiu's name row is removed. Seventeen story texts are rebuilt and six titles changed, as the changes file has them. The profile-wording list matches the 18 profile files in the diff. Release 42 is PR #1653. The data page and the census credit show release 43, 14 November 2026.
- **Open-Gaps.** The closure lines on 254, 255 and 256 to 262 are each true to the census as built. Item 264 lists what is carried. That includes the audio copies that keep pre-release text (Agathon, al-Baladhuri, Beuno, Brigid: the four briefs the branch changes), the map years and the 404 check after deploy. The Alcuin letters stay wanted through 254's Library item, which 264 carries.
