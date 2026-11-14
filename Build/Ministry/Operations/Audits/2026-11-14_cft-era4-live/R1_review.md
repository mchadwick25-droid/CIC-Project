# Era 4 on the live tree (data release 43): review round 1

Reviewer: fresh Opus agent, full effort, independent of the drafting. Branch `claude/cft-era4-live` at `f2f9cad5`, against `origin/main`.

**Verdict: not yet approved to proceed. 1 blocking, 6 substantial, 9 minor.**

`node tools/validate-census.mjs --base <origin/main census> --atlas cft-website/index.html --tree cft-website/tree cic-website/data/world-census.json` passes: `619 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four shortName length warnings carried from release 42). `python tools/check_spelling.py --base origin/main --enforce` **fails** (exit 1, 16 findings in enforced trees; see S1).

How this was checked. The older-text changes were reviewed from an independent leaf-by-leaf diff of the origin/main census against the branch census. It matches the 109 items in `Census_Text_Changes.md`, plus the people-list mechanics and peopleNote drops. Every rewritten story was read against the held lines the changes file names, and the claims below were checked in the vendored file at the line given. The 60 new person entries and Bede's merge were compared field by field with their profile files: every longDescription equals its brief, every card field equals its card file (datesNote and placeNote from `dates` and `place`), and every teaser equals knownFor, except Bede's (S2). Every toldWithin is the first tradition the card names; al-Baladhuri is told within none. Every new people row is in its home tradition's list, and every list is sorted by year. Every modernCountries row is copied from an existing census row of the same place name. Every new short dates line was read against its card's dates note. The 13 new scan readings were each opened at file and line.

---

## BLOCKING

### B1. Agathon's own words are misquoted, through a scan reading that inserts a word (`agathon-of-alexandria`, longDescription; `tools/quote_scan_readings.json`)

The census text: "Early in the account, its writer names himself: \"I the sinner Agathon, I was the son of the Father Benjamin, and knew much of his virtues through my intimacy with him.\""

The scan line is `I he sinner Agatbon, I was the son of the Father Benjamin, and knew much` (`severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt` l.46143). The new scan reading gives `"reads": "I the sinner Agathon"`. In this file the OCR prints the word "the" as "I he" throughout, lower case as well as capital:
- "in the guardianship of I he orthodox faith" (l.601)
- "I he shepherds of his flock" (l.605)
- "I he author ol this history, Scverus, son of Al-Mukalfa" (l.2002), which is "The author of this history"
- "in I he histories" (l.2558), "all I he doctors" (l.4909), "at I he time" (l.6041), "I he angel ol God" (l.6214), "I he sick" (l.6401), "in I he sanctuarv" (l.7111)

So the printed page reads "The sinner Agathon, I was the son of the Father Benjamin". The reading adds a word to the man's own words, the quote then passes the validator on that reading, and it stands on the live tree page `cft-website/tree/agathon-of-alexandria.html`.

Fix. Change the scan reading to `"reads": "The sinner Agathon"` (kind "OCR misread"). Change the quote in `Who-Profiles/era4/batch6/agathon-of-alexandria.brief.txt`, the census longDescription and `records.json` l.162 to "The sinner Agathon, I was the son of the Father Benjamin, and knew much of his virtues through my intimacy with him." Rebuild the tree page.

---

## SUBSTANTIAL

### S1. The spelling gate fails on 16 British spellings from the new entries (`cic-website/data/world-census.json`, `cft-website/tree/*.html`)

`check_spelling.py --base origin/main --enforce` exits 1. Both trees are enforced (`ENFORCED` holds `cic-website/` and `cft-website/`). The findings are all in narrator prose or `about` notes, not in quotations:
- `bede-of-jarrow` card legacy: "wrote on Scripture, on metre, on time and on history" (census l.82922).
- `beuno` longDescription: "Beuno was travelling near a ford on the river Severn" (census l.108111).
- `aidan-of-lindisfarne` card: "who travelled on foot to preach" (census l.109212).
- `severus-ibn-al-muqaffa` card: "Joseph Assemani's catalogue" twice (census l.114336, 114343).
- `elias-of-nisibis` card: "named in the catalogue of Ebedjesu of Soba" (census l.114804).
- The matching tree pages: `aidan-of-lindisfarne.html`, `bede-of-jarrow.html`, `beuno.html` (three), `elias-of-nisibis.html` (two), `severus-ibn-al-muqaffa.html` (two), `timothy-i-of-baghdad.html`.

Fix: "meter", "traveling", "traveled", "catalog" in the profile files and the census (Decision-Log 77), then regenerate the pages. CI fails until this is done.

### S2. Bede's teaser was not merged, and it gives his disputed death year as settled (`bede-of-jarrow`, teaser)

The census text: "Jarrow, c. 673 to 735 CE. A monk given to his monastery at seven, who wrote the book that is still the main record of the English church." It is the release 42 teaser, and the map in `cft-website/index.html` shows it. The brief's own rule is teaser = knownFor, and the new card's knownFor reads: "Monk and priest of Wearmouth and Jarrow who wrote the Ecclesiastical History of the English nation. ..." Every other new entry follows the rule.

The card's dates note says: "Plummer holds that he died on the eve of Ascension Day in 735; the Saxon Chronicle and several other chronicles give 734". The entry's own `dates` now reads "born 672 or 673; died 735 or 734". Open-Gaps 254 (batch 1, 2026-11-14) already named "735" as "a disputed year as settled".

Fix: set the teaser to the card's knownFor.

### S3. The Verden story says Alcuin's letters are not held and leaves his view unstated, though the held volume's index states it (`carolingian-reform-christianity`, documentedStories[0].text, teaser, caveat)

The text: "Alcuin of York, the reform's leading scholar, wrote about that tithe. His letters on it are not in the Library. Jean Mabillon, who had them, says they show what Alcuin thought of easing the tithes that Charlemagne wanted from the newly baptized Saxons. Both kinds of text are the reform's: the law it enforced, and the doubts its own scholar raised." The teaser: "His own leading scholar has doubts about the tithe the conquered must pay."

The held Mabillon line says only what the letters are about, not what Alcuin thought: "Quid de relaxandis decimis, quas a novitiis Christianis Saxonici populi eus volebat Carolus, senserit vir pius, probant epistolae 7 et 41" (`alcuin_opera-omnia-letters_migne-pl100-101_1863.txt` l.114700-114703). On that line alone, "doubts" in the teaser and in the closing sentence is the narrator's inference. The story's centre is now an empty clause: Mabillon "says they show what Alcuin thought", and the reader is never told what that was.

The same file's index does say what he thought, and the story does not use it:
- s.v. Saxones: "Non erat decimarum exactione et rigore poenarum vexanda, 51" (l.121659-121660): the Saxon people was not to be harassed by the exaction of tithes and the rigor of punishments.
- s.v. Decimae: "Decimarum jugum an rudibus populis in principio fidei imponendum, I, 58, 117. Illarum exactio conversioni Saxonum impedimento fuisse censetur, 51, 104" (l.117543-117544, OCR normalized).
- s.v. Fides: "Voluntaria res est, ad quam nemo cogi potest, I, 42, 50" (l.118264-118265).

The letters' own text is not in the OCR (no hit for the index's phrases in the body). So "His letters on it are not in the Library" is true of the text but misleads. The volume that holds the index is the Library's, and the file header says it includes his letters.

Fix. Replace the last four sentences of the text with one that rests on the held index. For example: "Alcuin of York, the reform's leading scholar, saw it otherwise. The index to his collected works, in J.-P. Migne's printing, sums up his letters: faith is a matter of the will, to which no one can be forced, and the Saxons were not to be harassed with tithes and harsh punishments. The letters' own words are not in the Library's copy. Both kinds of text are the reform's: the law it enforced, and the objection its own scholar raised." Keep the caveat's "known here only through" wording, naming the index beside Mabillon. The teaser can then keep "doubts".

### S4. Dhuoda: two compatible notes are set against each other as a dispute, and "swore" is in neither (`carolingian-reform-christianity`, documentedStories[1].text)

The text: "Who swore to avenge Bernard is told two ways. Édouard Bondurand, her editor, gives the wish for vengeance to the younger son; an older editor's note in the Patrologia Latina gives it to William."

The two held lines do not conflict. The Patrologia note has William "patris mortem ulturus" seize Toulouse, which was before his own death in 850 (`eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt` l.112842-112844). Bondurand has the younger Bernard, once grown, think only "à venger son père et son frère" (`dhuoda_liber-manualis_bondurand1887.txt` l.1838-1843). The brother he avenged is William. Neither source has an oath. Framing the two as rival accounts misleads, and it is a dispute the record does not hold.

Fix: "William rose to avenge his father, an older editor's note in the Patrologia Latina says, and was put to death as a rebel in 850. The younger son, Bernard, grew up, Édouard Bondurand writes, thinking only of avenging his father and his brother." Fold this into the sentence on 844 and 850.

### S5. The Dionysius story's closing claim no longer matches its own text or its caveat (`syriac-orthodox-under-islam`, documentedStories[1].text)

The closing sentence: "Few chronicles let the head of a church under Islam say, in his own voice, what cooperation with the caliphate cost and what it bought."

After the rewrite, the journey, Afshin's burning and the report to the caliph come from Bar Hebraeus's narration (`barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` l.21798-21822). The new caveat says Bar Hebraeus "tells the journey without marking it as Dionysius's own words". The passages in Dionysius's voice are on the Copts' learning and simony, and on the pyramids (l.21905-21923, 22128-22136). They say nothing of what cooperation with the caliph cost or bought. The garden ruling of 829 is also Bar Hebraeus's narration (l.21491-21496, 21700-21716). The sentence survives from the old text, which drew on material the branch has removed as not held.

Fix: end on what the held text shows. For example: "Bar Hebraeus keeps only a few pages in Dionysius's own words, but they show a patriarch who served the caliph as envoy, watched the army undo his errand, and went back to tell the caliph so." Or end the story on the pyramids sentence.

### S6. The release records are not on the branch, and the changes file misses four profile edits

- There is no Decision-Log entry for release 43 and no Open-Gaps entry carrying its items. Release 42's entry and Open-Gaps 255 set the pattern. Items that need a home:
  - al-Baladhuri told within none, in the Syriac East & Asia river (the brief's question for Mark).
  - The S3 index lines for Alcuin's letters (a Library item: the letter text is missing from the OCR).
  - Closing lines for Open-Gaps 254-262 and 255, with each item closed by name.
  - No audio for the 60 new entries.
  - The tree-page 404 check after deploy.
- `Census_Text_Changes.md` ("Profile files changed by this release") lists seven profile files. The diff changes eleven. These four are missing:
  - `era3/batch2/brigid-of-kildare.brief.txt`, the Basnage sentence.
  - `era4/batch6/agathon-of-alexandria.brief.txt`, the quote (B1).
  - `era4/batch2/timothy-i-of-baghdad.card.json`, "Why he is named for Baghdad".
  - `era4/batch5/moses-bar-kepha.card.json`, the fourth key work dropped (M9).

Fix: write the Decision-Log entry and the Open-Gaps carry, and add the four files to the changes file, before the pull request is marked ready.

---

## MINOR

### M1. Harun's question: "in few words" is moved from the answer to the question (`the-church-of-the-east-on-the-silk-road`, documentedStories[0].text)

The text: "Harun al-Rashid once asked him, in few words, which religion God approves." Amr has the caliph ask for a short answer: "respondc mihi breviter, o pater christianorum, de hoc quod te interrogo" (`amr-ibn-matta_de-patriarchis-nestorianorum-commentaria-pars-altera-ara-lat_gismondi1896-1897.txt` l.12943-12944, OCR normalized). Fix: "Harun al-Rashid once asked him to say in few words which religion God approves."

### M2. Maximus: the evening talk is placed after the communion exchange, which it precedes (`byzantine-imperial-church-heraclian-iconoclast`, documentedStories[0].text)

The text runs: the communion question, the four councils, the envoys, the three young men, then "That evening he told two officials that he had no teaching of his own". In the Record, the same evening visit by Troilus and Sergius Eucrates holds "Ego dogma proprium non habeo", and then the question "Non communicas throno Constantinopolitano?" and the four councils (`maximus-confessor_relatio-motionis-disputatio-bizyae-grc-lat_migne-pg90.txt` l.7497-7546). Fix: move the "no teaching of his own" sentence before "He was asked whether he would communicate". Let it open the evening scene: "That evening two officials came to him. He told them he had no teaching of his own, only the common teaching of the catholic church. Would he communicate with the throne of Constantinople, they asked? He would not ..."

### M3. The 830s revolt: the `when` lines leave out Makrizi's year (`coptic-christianity-under-early-islam` and `syriac-orthodox-under-islam`, documentedStories, when)

Both read "c. 830–831". Bar Hebraeus's "eodem anno" is the Greek year 1141, 829-830 (l.21719, 21798). Makrizi's Hijra year 216, which the Coptic story itself gives, runs from February 831 to February 832, and he has the revolt unsubdued until al-Ma'mun came (`renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt` l.17703-17708). Fix: "c. 830–832".

### M4. Symeon's exile is dated "about 1000", a date the held line gives for his life, not for the exile (`athonite-and-comnenian-byzantine-monasticism`, documentedStories[1].when)

The Philokalia compilers place Symeon "περίπου τὸ χιλιοστὸν ἀπὸ Χριστοῦ ἔτος" (`philokalia_ton-ieron-neptikon-v2-grc_tzelatis1893.txt` l.19937-19950). The caveat rightly says "No source used here gives the year of the exile". Fix: "early eleventh century?" or "under the patriarch Sergius". Sergius is named in the text (`calecas_opera-omnia-pg152-grc-lat_migne1866.txt` l.20084-20124).

### M5. Cedd's death year is given as settled where the card gives a second year (`cedd-and-chad`, dates)

The line: "Cedd died 664; Chad died 672". The card reads: "Charles Plummer and the Bollandists date his death to 664, though a heading in J. A. Giles's English gives 659." Bede gives no year for either brother. Fix: "Cedd died 664 (Plummer); Chad died 672 (Bollandists)", or "Cedd died 664 or 659; Chad died 672".

### M6. Reading level: three patched fields fall below the target, and two rewrites go below the floor

Scores from `engine.m1.gates.grade_text`, old to new:
- `bagratid-armenian-christianity` longDescription: FRE 63.4 to 58.3. why: FRE 61.3 to 59.7. Both were above 60 before the patch.
- `byzantine-imperial-church-macedonian` legacy: FRE 53.4 to 49.6.
- `byzantine-imperial-church-heraclian-iconoclast` documentedStories[1].text is FK 5.7. `syriac-orthodox-under-islam` documentedStories[1].text is FK 6.8. Both are below the grade 8 floor, from runs of very short sentences.

Every other rewritten story text lands at FK 7.6-9.5 and FRE 62-76, from release 42's FK 11-25. The `why` fields of the Coptic, Syriac and Macedonian entries stay far off target (FRE 4-29); that is older text, and only single sentences were patched here.

Fix: in the Bagratid fields, split the Ormanian sentences ("Malachia Ormanian was once Armenian patriarch of Constantinople. In 1912 he wrote that ..."). In the Macedonian legacy, split "Photius's Bibliotheca preserves ... 279 books, by his own count, a great many of which ..." into two sentences. In the Martin story, join a few of the shortest clauses (for example "Martin had been ill since the October before, and in his own letter he says he lay on his bed before the altar of the Lateran church").

### M7. Ormanian "wrote in 1912" (`bagratid-armenian-christianity`, documentedStories[1].text, legacy)

The held book is G. Marcar Gregory's English of 1912. Its own printed date line reads "London : Society for Promoting Christian Knowledge, 1910" (`ormanian_church-of-armenia_gregory1912.txt` l.371), and the header dates the translation's introduction to 1912. Fix: "Malachia Ormanian ... wrote, in a book put into English in 1912, that ...", or drop the year.

### M8. One stock closer (`bagratid-armenian-christianity`, documentedStories[1].text)

"The book carries the name of the house that made its writer, and his church kept it close." "Kept it close" is a soft, generic phrase with no fact behind it. The facts are in the text already: used in the services in 1786, and in private prayer and as a charm in 1912. Fix: "The book still carries the name of the house that raised him, and his church used it in its services and in private prayer for centuries."

### M9. Moses bar Kepha's card lost a reviewed key work with no record (`moses-bar-kepha`, card.keyWorks)

The branch drops `{"title": "Commentary on the liturgy", "about": "named in the list of his works given by Abbeloos and Lamy. It is not among the sources used here"}`. That entry was added by the batch 5 review's fix B-B2 and is held (`barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` l.22907, "5. Commentarius in liturgiam", OCR normalized). The drop meets the validator's three-work limit (`tools/validate-census.mjs` l.215), but no file records it or says why this work went rather than another. The tradition's longDescription still says "Moses bar Kepha explained the liturgy". Fix: record the drop and its reason in the changes file, or keep the liturgy commentary and drop the Old and New Testament commentaries instead. Bar Hebraeus's notice of those commentaries is already in the card's legacy traces.

---

## Checked and holding

- The Martin I story against Mansi 10 and Duchesne: the soldiers with lances, swords and bows, the candles like leaves in a winter wind (l.87327-87339), a year on Naxos (l.87518-87520), 17 September and ninety-three days (l.87653-87655, 87746-87752), Olympius (l.87821), the terrace and crowd, the cloak, the torn tunic and the chains (l.87872-87994), Cherson by 15 May (l.88440-88444), three or four modii for a coin (l.88462-88468), the church of Saint Peter and the prayer for its pastor (l.88472-88540), death on 16 September (l.88336).
- The Timothy story against Chabot (l.40254-40272; 7 May 780 from the index, l.49679), Mari (l.12984-12990), Amr (l.12941-12950, 13027-13029), Thomas of Marga (l.21495-21505, 21955-21986, 20155-20166, 20186) and Mingana (l.1685-1704). Every quotation is verbatim.
- The stele story against Malech's reprint of Wylie (l.13563-13567, 13680-13711, 13742-13763, 13997-13999, 14139-14154), Wells Williams (l.14211-14216) and Yule-Cordier (l.2994-3000). Every quotation is verbatim.
- The Coptic and Syriac 830s stories against Bar Hebraeus (l.20514-20541, 21488-21496, 21700-21716, 21796-21824, 21903-21924, 22128-22137), Eutychius in PG 111 (l.87139-87158) and Renaudot reporting Makrizi (l.17703-17711).
- Jacob of Edessa against Michael the Syrian (l.36349-36425).
- The two Makurian stories against the History of the Patriarchs in PO 5 (l.5839-5846, 7068-7142) and Abu Salih (l.13526-13556).
- Athanasios against Meyer (l.1225-1241, 1400-1450, 5462-5477). Symeon against Combefis (l.20084-20124, 20267-20290, 20431-20462).
- The Narek story and the Bagratid fields against Chamich (l.4813-4817, 4877-4888), Issaverdens (l.847-856), Ormanian (l.7742-7748) and Serpos (t2 l.1710-1718; t3 l.17992-17998). Every quotation is verbatim.
- Boniface against Kylie (l.975-1024) and the Royal Frankish Annals (l.1665-1670). Verden against the Annals (l.4675-4687, 4824-4831) and the Capitulatio (l.5299-5307, 5333-5338). Dhuoda's Nithard sentence (l.2296-2305).
- The other twelve scan readings: the Bede running head (l.220), the Boniface signature mark and running head (l.2457-2460; "so" is the page number 50), "abomi nable" (Rees l.13535-13536), "ihe", "1 have" (Evetts l.2137, 2375), and the seven Chronicle of Seert volume misreads (l.929, 1013, 1014, 1016, 1017, 8463, 10419). Each "reads" is what the printed page says.
- Short dates lines: the other 58 say nothing their card does not, and each disputed year carries "c.", "or", a range or a named source.
- Placings, lanes and people lists: no defect found beyond those above. Name rows for Adomnán (Insular Irish) and Humbert (Macedonian era) stay as name rows outside each man's home tradition, as Jerome's and Reccared's do in release 42. The John of Nikiu row's removal from the Miaphysite Egypt list is justified by its year and source (Open-Gaps 259).
- The generated pages: data, about and method show release 43 and 619 movements; the validator's atlas and tree checks pass.
