# Second cap-ruling check: six strings on five story cards (2026-11-15)

Strings checked: 6. BLOCKING: 0. MINOR: 2. Verdict: CLEAR.

Method: one fresh Opus reviewer at full effort, who had not seen the drafting, the rounds or the first check's work. CLAUDE.md read in full first. Read only. Each `relationsSummary` was parsed from `DATA.stories` in cft-website/index.html at HEAD (628ee067). Each string was matched exactly against the shipped field. Each fact was checked against the card's own `text`, `teaser`, `caveat` and `sources`, and against each named census movement in cic-website/data/world-census.json, one at a time. The pre-cleanup lines (a9302d0b) were read to see which claims came from the old line. Cap_ruling_check.md was read for what was ruled. Readability was scored with `engine/m1/gates.grade_text`, as shipped and with proper names masked.

Exact match: all six strings are shipped exactly as given. String 1 is the whole Abercius field. Strings 2 to 6 each occur once in their card's field.

Sentence lengths (words): 13 and 23; 14; 5 and 13; 10 and 16; 23; 11 and 15. None passes 25.

Readability, whole lines: raw FK 8.4 to 11.7, Flesch 47 to 57. With proper names masked: FK 6.0 to 8.5, Flesch 70 to 75. The raw spread comes from tradition and place names the lines must carry, as in the first check. No line fails the bar on readability.

### 1. abercius-epitaph
PASS.
- "Phrygia was the home of the New Prophecy, which began there around 165." Census Montanism: region "Phrygia, spreading"; `why` "In a Phrygian village around 165"; the movement expected the New Jerusalem at Pepuza "in Phrygia". The card places Hierapolis in Phrygia, so the link reads without help.
- "Nisibis, the far end of Abercius's journey". Card `text`: sent to Rome, "traveled through Syria and crossed the Euphrates to Nisibis".
- "belongs to Syriac Edessa, a tradition that begins around 200". Census: name "Syriac Christianity (Edessa/Nisibis)", region "Edessa & Nisibis", dates 200–410, first hard evidence the flood of 201.
- "the same time as the epitaph". Card: "around the end of the second century"; caveat: "'c. 200' is a compromise". The line claims no more than that.
- Nothing from the cut sentence survives. No Montanist reading of the stone is claimed. Abercius is now named, so "journey" has its owner. Census facts and card facts only, as ruled.
- Writing: sentence 2 carries two appositives at 23 words. It stays clear because each appositive is short and concrete. Not counted.

### 2. john-the-almsgiver ("John stands for the minority church ...")
PASS.
- "the minority church there". Card `text`: "in a city where most Christians followed the rival Coptic patriarch". "There" resolves to Alexandria in the preceding sentence.
- "in the decades before the Arab conquest". Card: patriarch from 610, fled in 619. Census Church of Alexandria: "Arab armies took Egypt between 640 and 642"; census Coptic Egypt: Alexandria taken "in 641-42". The new wording no longer implies John was in office at the conquest. Fixed as ruled, with "John" in place of "He".

### 3. john-the-almsgiver ("He was appointed by Heraclius. ...")
- Facts hold. "Appointed by Heraclius": card `text` "made Chalcedonian patriarch of Alexandria in 610 at the emperor Heraclius' wish". The teaser's "elected against his will" does not clash with it; the old line said the same ("the emperor who appointed him"). Census Byzantine Church II: dates 622-843; its `why` opens with Heraclius, and its `longDescription` opens "Heraclius recovered the True Cross from Persia in 630". Heraclius's reign ran through 622 (card 610 accession; census 630). "Next era" is gone, so the "next after what?" question no longer arises.
- MINOR (writing): "opens in his reign". The sentence before has John as its subject ("He was appointed by Heraclius"), so a reader may first take "his" to mean John. "Reign" points to the emperor, and most readers will get there, but only after a second look. Proposed: "He was appointed by Heraclius, whose reign opens the Byzantine imperial church's story from 622 to 843." (15 words; one sentence, the referent fixed.)

### 4. salzburg-emigrants
PASS.
- "Halle's Francke Foundations organized relief and publicity for the emigrants." Old-line claim (a9302d0b). Not counted, per the brief; the convention is with Mark.
- "The Georgia settlement was a Halle project through Urlsperger". Card `text`: "recruited by the Augsburg pastor Samuel Urlsperger with Halle's backing"; `sources`: the Georgia diaries edited by Urlsperger and published at Halle, 1735–52. "Halle project" is the old line's wording and slightly firmer than "with Halle's backing", but the card's Halle-published reports support it.
- "so the link to Pietism is direct". Census Pietism: its center "became Halle, where August Hermann Francke built an orphanage that grew into ... a printing house". The line names the Francke Foundations first, so the reader has the Halle–Pietism tie. "Link" speaks to the card's "How it connects" heading, not about the data. No slug.
- The split cures the 25-word sentence and the loose tag. The whole line reads in order. (Herrnhut sentence: old-line, not counted.)

### 5. nickel-mines-forgiveness
- Facts hold. Census Anabaptists: "In January 1525, a small group in Zurich baptized one another as adults"; dates 1525-1650. "Long after": the 1690s are 170 years on. "The 1690s": old line, not counted, per the brief. The map-label date range is gone, as ruled.
- MINOR (could mislead by implication): "the first adult baptisms at Zurich in 1525". Specialists read this as the movement's first believers' baptisms, and that is standard usage. A general reader may take it to mean adults were never baptized before 1525. Adult converts were baptized from the church's beginning. The census avoids the problem by saying who baptized whom. Proposed (two sentences, census wording): "The Amish began in the 1690s, in a split within the Anabaptist family. That family began at Zurich in 1525, when a small group baptized one another as adults." (13 and 16 words.)
- Whole line, not counted (outside the six strings): sentence 2, "among the heirs of the Anabaptists who became settled churches after 1650", lets "who" attach to "the Anabaptists" rather than "the heirs". The census `why` puts it plainly: "After 1650 the heirs of the Anabaptists became settled churches." Also the `relatedIds` gap from the first check stands: the Mennonites are named but not linked.

### 6. walatta-petros
PASS.
- "helped lead the resistance to Emperor Susenyos's Catholic policy". Card `text`: after Susenyos "publicly professed Roman Catholicism in 1622 and ordered his subjects rebaptized", she preached against it, refused to recant before him, and "founded and led seven successive religious communities ... sheltering clergy and lay people who would not convert". Teaser: "gathered a community of hundreds ... who refused the new faith". "Helped lead" fits that record.
- "The revolt against it grew so fierce that he gave up the throne in 1632." Census Ethiopia's Ordeal: "provoking a revolt so fierce that he abdicated in 1632". Card: "Susenyos abdicated in 1632 after a civil war".
- The split does what the first check asked. She now leads the resistance, and the revolt is told as its own event, so she is no longer made a leader of the civil war. "It" resolves to the policy and "he" to Susenyos. The rest of the line follows on cleanly.
