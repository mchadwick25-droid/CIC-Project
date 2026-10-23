# Review A: Atlas fleet consistency and quality check (alx, cappadocian, hal, syr)

Read-only review, 2026-10-17. Records: `.claude/worktrees/review-main/records/` at 14ea7326a. Vendored sources: `cic/texts/` in the same worktree. Pleiades checked live (JSON API) for every place URL.

Severity: **BLOCKING** means wrong, unsupported or misleading. **SHOULD-FIX** means craft, readability or a tell.

## Fleet-level measurements (all four pages)

| Check | alx | cappadocian | hal | syr |
|---|---|---|---|---|
| Main story words (600–700) | 622 | 700 | 690 | 640 |
| Main story average sentence length | 12.2 | 12.5 | 13.0 | 11.6 |
| Main story sentences over 25 words | 0 | 0 | 0 | 0 |
| Tile average sentence length | 16.3 | **9.5** | **8.7** | 16.3 |
| Tile sentences over 25 words | **1 (31 words)** | 0 | 0 | 0 |
| Card tellings outside 120–250 | **100, 102** | 0 | 0 | 0 |
| Card sentences over 25 words | 0 (the two the mech check flagged at 33 and 36 words are each two sentences split at a closing quote) | 0 | 0 | 0 |
| Teaser length (words) | 25–31 | 23–39 | 25–35 | **41–52** |
| Cards in date order (by the site's `when` field) | yes | yes | yes | yes |
| Highlight notes over 25 words | 9 | 6 | 5 | 4 |
| Build jargon in participant text | tile | tile x2 | tile | none |

Verified verbatim against `cic/texts/` (no problems found): Leonides' letter line (npnf201 l.32562); the eunuch verse (npnf201 l.33197); Dionysius on Nepos (npnf201 l.41317); "open hands" (npnf201 l.41113); the Clement bee paraphrase (anf02 l.27493); the Edessa flood lines (chronicle-of-edessa_cowper.txt l.53, and the telling uses the record's modern rendering); the first Pearl hymn line (npnf213 l.21794, record rendering); Theodoret's gnats (npnf203 l.11174, record rendering); Ephrem's "Then trust me" (palladius_lausiac-history_clarke1918.txt l.471, record rendering); Sozomen's opening on Persia (npnf202 l.28874, record rendering); Jerome Ep. 45 "all Rome resounded" and "infamous turncoat" (npnf206 l.8636, l.8605); Ep. 138 "leave my pleasant home" (npnf206 l.28530); Ep. 139 "spiritual riches" (npnf206 l.28600). The Doctrine of Addai details also check out: the seventy-two, Taratha, the broken legs, and Serapion from Zephyrinus (addai_doctrine-of-addai.txt l.29, 49, 87, 89).

### Fleet-level finding F1: scholarly hedges inside the tradition's own voice (SHOULD-FIX)

The card tellings speak in the tradition's voice ("our church", "our bishop"). CLAUDE.md says a Representative's hedge must be emic, not the etic "historians disagree". Five cards break this:

- alx `origen-daring-deed`: "Some later scholars thought the story came from misreading Origen's own figures of speech. Eusebius's English translator saw no reason to doubt it." A 19th-century English translator is an anachronism in a third-century voice.
- alx `gregory-formation`: "though some scholars have questioned who gave it, and when"
- syr `edessa-flood-201`: "Scholars still dispute whether the line is original or was added later by another hand."
- syr `basil-legend`: "Modern scholars judge the Syrian to be another man, Eusebius of Emesa, and so judge the meeting a legend."
- syr `abgar-addai-legend` teaser: "Scholars judge the tale a later legend about how the church began."

The records' divergence notes do require these doubts to be stated, so the doubt has to stay. Only who voices it has to change. This holds across the fleet, so Mark should rule once on it instead of each page being patched. Possible emic forms: "Some have doubted that it happened at all" (alx); "Whether that line is original, or was added later by another hand, is not settled" (syr flood). The main stories are told by a narrator, so "Scholars disagree" there (alx [4], cappadocian [8], hal [1], syr [1], [7]) is acceptable.

### Fleet-level finding F2: tiles carry most of the tells

All four main stories are clean on length and nearly clean on tells. Three of the four tiles hold the page's build jargon, its colon-reveals and its triads. The tiles look like they were written in a different pass from the main stories and missed the final tell sweep. Details are under each tradition below.

---

## Alexandria (alx)

### A1. BLOCKING: tile states the contested act as fact (and runs 31 words)
- **Current:** "When a young Origen took a hard verse from Matthew too literally and acted on it, his bishop first praised his zeal, then turned the same act against him years later."
- **Evidence:** `alx.story.origen-daring-deed` is graded `Contested`. Its `use_note.not_for` says: "stating the act as established fact when only Eusebius reports it and its history is disputed". The card on the same page hedges it ("Eusebius alone tells…"). The tile drops the attribution. At 31 words it is also the only participant sentence on the four pages over 25.
- **Proposed:** "Eusebius reports that a young Origen took a hard verse from Matthew literally and acted on it. His bishop first admired his daring, then later turned the act against him."

### A2. SHOULD-FIX: build jargon in tile
- **Current:** "This world's own record was kept almost entirely by literate men."
- **Proposed:** "What survives was written almost entirely by literate men."

### A3. SHOULD-FIX: tells in tile (colon-reveal; "X, not Y")
- **Current:** "Teachers led seekers through Scripture, layer by layer: the plain story first, then a deeper meaning underneath it, opening onto Christ himself."
- **Proposed:** "Teachers led seekers through Scripture layer by layer. The plain story came first, then a deeper meaning that opened onto Christ himself."
- **Current:** "Clement and Origen were confident that Greek learning could serve Christ, not threaten him. Two real authorities never merged here: the teacher's, earned by demonstrated wisdom, and the bishop's, handed down by office."
- **Proposed:** "Clement and Origen were confident that Greek learning could serve Christ. A teacher and a bishop each held real authority, and the two never became one. The teacher's came from the wisdom people saw in him. The bishop's was an office handed down." (This is the main story's own wording, [5].)

### A4. SHOULD-FIX: Leonides card contradicts itself and the source on Origen's age
- **Current:** "His son Origen was sixteen." … "At seventeen, Origen was left the eldest of seven children, and his mother was a widow."
- **Evidence:** Eusebius HE VI.2.12: "he was left with his mother and six younger brothers when he was not quite seventeen years old" (npnf201 l.32608–9). The record `alx.story.leonides-martyrdom` `text` says "at seventeen", so the record itself rounds up. Within 100 words the card says sixteen and then seventeen for the same moment.
- **Proposed:** "Not yet seventeen, Origen was left the eldest of seven children, and his mother was a widow."

### A5. SHOULD-FIX: two tellings under 120 words
- `alx.story.origen-demetrius`: 100 words. `alx.story.didymus-meeting`: 102 words.
- **Proposed additions, from the records' own fields:**
  - origen-demetrius, after "He never taught in the city again.", add "The letters and rulings from the break are lost." (`absent_detail`: "The synodal documents are lost.")
  - didymus-meeting, after "Palladius calls him the blind author.", add "Jerome, who studied with him briefly, says that in 392 he had already passed his eighty-third year." (`alx.figure.didymus` `dates.born`, Jerome De Viris 109)
- The Leonides telling also averages 9.8 words a sentence, the choppiest card on the page. Joining "One line of that letter survives. 'Take heed…'" into one sentence would help.

### A6. SHOULD-FIX: "formation" is build vocabulary
- **Current (main [8]):** "Among those who could read, the long bond between teacher and student was no longer the main way formation worked."
- **Proposed:** "Among those who could read, the long bond between teacher and student was no longer the main way faith was formed."

### A7. SHOULD-FIX: etic hedges in two cards (see F1)
- `origen-daring-deed`: "Some later scholars thought the story came from misreading Origen's own figures of speech. Eusebius's English translator saw no reason to doubt it."
- **Proposed (keeps the divergence the record requires):** "Some have doubted that it happened at all, and thought the report grew from Origen's own figures of speech. Others see no reason to doubt it."

### A8. SHOULD-FIX: place note missing "probably" where Pleiades marks the name as uncertain
- **Current:** "Arsinoe was the capital of this district, called a nome. The city's site is Medinet el-Fayum, in today's Egypt. The villages that followed Nepos were here." (26 words)
- **Evidence:** Pleiades 736948 (Krokodilopolis/Ptolemais Euergetis) lists the name "Arsinoe" with `associationCertainty: less-certain`. The location itself is certain.
- **Proposed:** "The capital of this district, probably the city called Arsinoe, stood at Medinet el-Fayum, in today's Egypt. The villages that followed Nepos were here." (24)

### A9. SHOULD-FIX: highlight notes over 25 words (proposed trims keep only record content)
| Note | Words | Proposed |
|---|---|---|
| Alexandria | 29 | "A port city in Egypt's Nile Delta, founded by Alexander the Great in 332 or 331 BCE. Its modern name is Iskandariya." |
| Origen | 32 | "Origen lived from about 185 to about 253. He taught in Alexandria until he broke with his bishop, then in Caesarea." |
| Athanasius | 30 | "Born about 296, he was bishop of Alexandria from 328 to 373. He was exiled five times." |
| Didymus | 35 | "Didymus the Blind, about 309 or 313 to about 398. Later tradition says he headed the school. Palladius, Jerome and Socrates do not say so." |
| Eusebius | 41 | "Eusebius of Caesarea, about 260 to 339. His Church History is the main source here. He is more reliable when he quotes documents." |
| Gregory | 27 | "About 213 to about 270. He studied under Origen at Caesarea from about 233 to 238. His farewell speech's date and author are questioned." |
| homoousios | 26 | "Greek for of one substance. The council at Nicaea used it to say the Son is fully God. Critics said it is not in Scripture." |
| Ephesus | 28 | "A great city of Ionia. Its ruins lie by Selçuk, in today's Turkey. Clement's story of John is set in a city near it." |
| Arsinoite district | 26 | see A8 |

Rigor spot-check, all supported: the 202 date and Leonides' letter (HE VI.2); Origen heading the catechetical teaching "in his eighteenth year" (npnf201 l.32732); the move to Caesarea in Alexander's tenth year and Demetrius's 43 years (l.36331); Dionysius's three days and Coracion (HE VII.24, record `arsinoite-conference`); Didymus blind from four and dead at 85 (`alx.figure.didymus`, Palladius). The Athanasius line "fenced what the churches had received" rests on `alx.term.homoousios` (translational) and `alx.dw.was-jesus-god`.

---

## Cappadocian (cappadocian)

### C1. BLOCKING: Gregory was not at Basil's funeral
- **Current (athens-friendship):** "Standing at his friend's funeral, Gregory chose to remember Athens first."
- **Current (valens-caesarea):** "As Gregory of Nazianzus told it at Basil's funeral, Modestus threatened…"
- **Evidence:** the NPNF introduction to Oration 43: "A serious illness, in addition to other causes, prevented S. Gregory from being present at his funeral (Epist. 79)… Tillemont places the date of this Oration soon after his return to Nazianzus" (after June 381) (npnf207_cyril-jerusalem-gregory-nazianzen.xml l.40926–40948). The athens card contradicts itself: two sentences earlier it says the speech was given "years afterward". The records carry the slip too: `cappadocian.story.valens-caesarea` `absent_detail`, "delivered at Basil's funeral", and the divergence_note "Gregory's public telling at Basil's funeral". Those records need the same correction.
- **Proposed (athens):** "When he rose to praise his dead friend, Gregory chose to remember Athens first." (record `text`: "standing to eulogize his friend")
- **Proposed (valens):** "As Gregory of Nazianzus told it in his funeral speech for Basil, Modestus threatened…" (record `text`: "Gregory of Nazianzus's funeral speech says")

### C2. BLOCKING: the Forty did not die in an empire-wide persecution
- **Current (forty-sebaste):** "It was around the year 320, in one of the last persecutions across the whole empire."
- **Evidence:** Sozomen IX.2 places the Forty "under Licinius at Sebaste in Armenia" (npnf202 l.44612). Licinius ruled only the East in 320. The record `cappadocian.story.forty-sebaste` `text` says "under one of the last empire-wide persecutions", which is a record error, and its sources are `verification_state: unverified`.
- **Proposed:** "It was around the year 320, in one of the last persecutions." (and correct the record's `text`)

### C3. BLOCKING: tile overstates the famine preaching
- **Current:** "Basil named hoarding landowners from the pulpit."
- **Evidence:** `cappadocian.story.famine-open-barns`: "Basil, then a priest, preached against them". No record says he named individuals, and the homilies are `unverified`.
- **Proposed:** "Basil, then a priest, preached against landowners who hoarded grain."

### C4. SHOULD-FIX: build jargon in tile (2)
- **Current:** "This world's own bishops were threatened and exiled." → **Proposed:** "Their bishops were threatened and exiled."
- **Current:** "The same exactness reordered how this world treated the poor." → **Proposed:** "The same exactness reordered how these churches treated the poor."

### C5. SHOULD-FIX: tile tells (colon-reveal, rhetorical questions, aphorism ending, choppy rhythm)
- The tile averages 9.5 words a sentence and runs in short bursts ("A famine came.").
- **Current:** "They defended one claim: the Son and the Spirit are fully what the Father is." → **Proposed:** "They held that the Son and the Spirit are fully what the Father is."
- **Current:** "How far can worship's own words go in naming who the Holy Spirit really is?" → **Proposed:** "The other contest was interior. It asked how far the words of worship could go in naming the Holy Spirit."
- **Current (ending):** "Did the three teachers ever agree on one settled scheme? That is itself an open question today." → **Proposed:** "Whether the three teachers ever agreed on one settled scheme is still debated." (It could also be cut, so the tile ends on "No woman's own words survive on their own." That line itself would read better as "No woman's own words survive.")

### C6. SHOULD-FIX: empty tail
- **Current (athens-friendship, last line):** "When their studies ended, both men went home to Cappadocia to begin the ascetic and church careers that would define them."
- **Proposed:** "When their studies ended, both men went home to Cappadocia."

### C7. SHOULD-FIX: undefined technical term "Homoian"
- **Current (nyssa-exile):** "Hostile Homoian bishops had arranged them…"; **(gregory-constantinople):** "because the Homoian party, long favored by the emperors, still held the city's great churches."
- The main story deliberately avoids the term ("a rival creed. It held the Son to be merely like the Father").
- **Proposed:** nyssa: "Hostile bishops of the court's party, who held the Son merely like the Father, had arranged them…"; gregory-constantinople: "because a rival party, long favored by the emperors, still held the city's great churches." (main [9] wording)

### C8. SHOULD-FIX: summary lines (tells)
- **Current (doxology-stand):** "The prayer held. Years later, when the bishops gathered again…" → **Proposed:** "Years later, when the bishops gathered again…" (drop "The prayer held.")
- **Current (main [6]):** "The words looked small. Yet to glorify the Spirit together with the Father and the Son placed the Spirit on the Creator's side of the line." → **Proposed:** "To glorify the Spirit together with the Father and the Son placed the Spirit on the Creator's side of the line."

### C9. SHOULD-FIX: highlight notes over 25 words
| Note | Words | Proposed |
|---|---|---|
| Pontus | 30 | "A province in what is now Turkey, renamed for Helena, Constantine's mother, after she died. Basil's family had a home at Annisa, in Pontus." |
| Nicaea | 30 | "A Greek city of northwestern Anatolia, now İznik in Turkey. A council of bishops met here in 325." |
| Council of Constantinople | 31 | "Bishops met in Constantinople in 381 and upheld the Nicene faith. Gregory of Nazianzus presided for a short time, then resigned." |
| Gregory of Nazianzus | 27 | "Born about 329 or 330, died about 390. Basil's friend from student days, he was briefly bishop of Constantinople." |
| Modestus | 26 | "Prefect of the East under Valens, from about 369 or 370 to 377. Valens sent him to bring Basil into line." |
| Hypostasis | 33 | "Greek for who God is. Father, Son and Holy Spirit are each a real someone." |

Rigor spot-check, supported apart from C1 and C2: Basil a bishop from 370 (`cappadocian.figure.basil`); Valens dividing Cappadocia in 372 (`cappadocian.figure.valens`); the doxology's two forms and the charge of "novel and… contradictory terms" (npnf208, De Spiritu Sancto I.3; the record allows no quotation marks, and the page uses none); Macrina's death in 379 at Annisa (`cappadocian.story.macrina-deathbed`); the poorhouse as "the new city", not "Basileias" (`cappadocian.term.basileias`). The card says Modestus came "in 371 and 372" and the main story says "in 371 or 372". Both follow records, so this is not flagged.

---

## Hieronymian (hal)

### H1. BLOCKING: tile contradicts the main story on church office
- **Current (tile):** "No one here held church office. Authority ran on learning and money instead."
- **Evidence:** main [4] on the same page: "Jerome was only a presbyter, under the bishop of Jerusalem." The quote record `hal.quote.no-one-preferred-to-the-seventy` calls him "the presbyter Jerome". `hal.core.hieronymian` says authority ran "never through episcopal office or territorial jurisdiction". The office the circle lacked was a bishop's.
- **Proposed:** "No one here held a bishop's office. Authority ran on learning and money instead."

### H2. BLOCKING: tile states Marcella's contested standing as flat fact and inflates it
- **Current (tile):** "Clergy still brought her their hardest questions about scripture."
- **Evidence:** `hal.story.marcella-standing` is graded `Contested`. Its `use_note.not_for`: "presenting the extent of her authority as documented fact". Its `text`: "Many men put hard questions to her, he adds, priests sometimes among them." The main story and card both attribute this to Jerome and say "sometimes".
- **Proposed:** "Jerome says priests were sometimes among those who brought her hard questions about scripture."

### H3. BLOCKING: tile overstates the source base and contradicts the page
- **Current (tile):** "Everything we know of them comes through Jerome's own pen."
- **Evidence:** main [8] on the same page reports the women through Pope Innocent's letter. `hal.limit.f5-women-own-words` says Innocent's reply attests their report. `hal.core.hieronymian` cautions: "Nearly the whole record is in Jerome's hand."
- **Proposed:** "Nearly everything we know of them comes through Jerome's pen."

### H4. SHOULD-FIX: build jargon in tile
- **Current:** "Fierce arguments tested this world." → **Proposed:** "Fierce arguments tested the circle."

### H5. SHOULD-FIX: tile triads and choppy rhythm (average 8.7 words a sentence, the lowest on the four pages)
- The tile holds three stacked groups of three: "on scripture, on giving things up, and on the written word"; "money, conviction, and their own hard questions"; "One was… One was… One was…".
- **Proposed (merging the short sentences and breaking one triad):** "Jerome came to Rome in 382 and joined a household of ascetic women that the widow Marcella had already gathered." "There the widow Paula and her daughter Eustochium built monasteries and a guesthouse for travelers." For the arguments: "Jerome broke with an old friend over a condemned teacher, and quarreled with a fellow scholar over one changed word. In 416, armed men burned the Bethlehem monasteries." This replaces the three parallel "One was" sentences with two plain ones and a date.

### H6. SHOULD-FIX: highlight notes over 25 words
| Note | Words | Proposed |
|---|---|---|
| Oea | 27 | "Oea began as a Phoenician town. Its site is now Tripoli, in Libya. The uproar over Jonah took place here." |
| Jerome | 27 | "A Christian scholar who lived in Rome, then Bethlehem, and died in 420. His letters carry nearly everything we know of this circle." |
| Marcella | 34 | "A widow of Rome who died in 410. Her Aventine house was already a place of fasting and scripture study when Jerome arrived." |
| Eustochium | 27 | "Paula's daughter, vowed to a virgin's life from her youth. She led the Bethlehem women after her mother died." |
| Augustine | 27 | "Bishop of Hippo, 354 to 430. He wrote to Jerome for about twenty-five years, arguing against giving up the old Greek text." |

Rigor spot-check, all supported: the crowd's "detestable monks… Tiber" (`hal.quote.detestable-monks`, Ep. 39.6); "all Rome resounded… infamous" (Ep. 45, npnf206 l.8605, 8636); the Oea tumult and the Jewish residents (`hal.quote.oea-tumult`, Augustine Ep. 71); Innocent on "ravages, murders, fires" and the unnamed agent (`hal.quote.innocent-ravages`, Ep. 137); "spiritual riches" (Ep. 139, npnf206 l.28600) and "leave my pleasant home" (npnf206 l.28530); Augustine's "no one should be preferred" (City of God XVIII.43). "Courteous" letters (main [6]) is the record's own word (`hal.story.oea-gourd`). The empty tails are clean: every telling ends on an event.

---

## Syriac (syr)

No BLOCKING findings. The rigor spot-check found every date and quote supported. The page's problems are consistency and craft.

### S1. SHOULD-FIX: teasers run roughly twice the fleet length
- Syr teasers run 41–52 words in 3–4 sentences. The other three pages run 23–39 words in 2–3 sentences. Trims using the teasers' own words:
  - edessa-flood-201 (47): "The Chronicle of Edessa, compiled about 340 years later, says a river flood killed more than two thousand people. It says the waters destroyed a church building, a line scholars dispute." (F1 also applies to "scholars dispute".)
  - ephrem-roll-and-vine (51): "In one dream, angels choose Ephrem to be trusted with a written roll. In another, a vine grows from his tongue. Both dreams appear only in the Syriac Paradise."
  - qyama-morning (47): "Before dawn at Nisibis, men and women of the covenant gather for the vigil. The daughters of the covenant sing a teaching hymn, and the Gospel is read as one story."
  - ephrem-famine-death (52): "Palladius and Sozomen tell that in Edessa's famine, Ephrem takes money from the rich and sets up some three hundred beds. He nurses the starving, and he dies within a month."
  - basil-legend (46): "A later Life of Ephrem says a vision sends him to meet Basil, who ordains him a deacon. The praise of a Syrian in Basil's writings is about another man."
  - choirs-tradition (42): "A later tradition says Ephrem founded the choirs of the daughters of the covenant. In his own time, we know only that these women sang his hymns."
  - jacob-deliverance (41) and simeon-martyrdom (41): see S3 for jacob-deliverance. For simeon-martyrdom: "The tradition tells that Simeon, bishop of Seleucia-Ctesiphon, is brought in chains before King Shapur. He will not worship the sun, and he is put to death with his clergy."

### S2. SHOULD-FIX: vision and miracle told without the source's voice
- **Current (ephrem-roll-and-vine, paragraphs 2–4):** "One of the holy fathers saw a dream in which the holy angels came down from heaven at God's command." … "Then the old man knew within himself that the words coming from Ephrem's lips were of the Holy Spirit." The attribution comes only in the first paragraph. For three paragraphs the vision is narrated flat. Compare Potamiaena (alx) and the Forty (cappadocian), which keep "the tradition says" audible all the way through.
- **Proposed:** "The Paradise tells that one of the holy fathers saw a dream…" and "Then, it says, the old man knew within himself…"
- **Current (abgar-addai-legend):** "He healed the king and preached to the city…" → **Proposed:** "The story says he healed the king and preached to the city…"

### S3. SHOULD-FIX: teaser states a contested miracle as fact
- **Current (jacob-deliverance):** "…Ephrem begs the old bishop Jacob to climb a tower and curse them. Jacob calls down only gnats and mosquitoes, and the Persians flee."
- **Evidence:** the record is graded `Contested`. The telling attributes the miracle ("Then, Theodoret writes"), but the teaser's last sentence does not.
- **Proposed:** "Theodoret, writing about a century later, says Jacob of Nisibis cursed the Persian besiegers with only gnats and mosquitoes. In his telling, the Persians flee."

### S4. SHOULD-FIX: etic hedges in emic cards (see F1)
- edessa-flood-201: "Scholars still dispute whether the line is original or was added later by another hand." → "Whether the line is original, or was added later by another hand, is not settled."
- basil-legend: "Modern scholars judge the Syrian to be another man, Eusebius of Emesa, and so judge the meeting a legend." This needs Mark's fleet ruling under F1, because the identification itself is etic knowledge.

### S5. SHOULD-FIX: highlight note is cryptic
- **Current (Syriac):** "The language of these churches. Ephrem wrote hymns in it, and most of Aphrahat's letters follow its alphabet."
- **Evidence:** `syr.term.tahwyata`: "the first twenty-two follow the twenty-two-letter Syriac alphabetic acrostic… one letter per piece".
- **Proposed:** "The language of these churches. Ephrem wrote hymns in it. Aphrahat's first twenty-two letters each begin with the next letter of its alphabet."

### S6. SHOULD-FIX: highlight notes over 25 words
| Note | Words | Proposed |
|---|---|---|
| Nisibis | 27 | "A fortress city, Roman from 298 until 363, when it was ceded to Persia. Its site is Nusaybin, on today's Turkey–Syria border." |
| Bardaisan | 30 | "A philosopher at the court of Abgar VIII of Edessa, 154 to 222. His words survive only through a student's dialogue and Ephrem's refutations." |
| Papa | 26 | "Papa bar Aggai was a bishop around 300. Later writers called him Catholicos, a title no one used in his time." |
| Theodoret | 26 | "A church historian, about 393 to about 460. He told of Jacob and the gnats about a century after the sieges." |

Rigor spot-check, all supported: the year-513 flood and both quoted lines (Cowper l.53; record `syr.quote.the-temple-of-the-church-of-the-christians`); the chronicle compiled about 540 (`syr.source.chronicle-of-edessa`); Edessa "taken over by Rome in 214" (`syr.force.frontier-plural-milieu`); the twenty-year vacancy after Barba'shmin (`syr.force.shapur-persecution`); Papa contested c. 315 (`syr.contested.papa-primacy`); the synod of 410 under Isaac (`syr.force.synod-410`); Palladius's "Then trust me" and the "some 300 beds" (Clarke l.471); Theodoret on Ephrem begging Jacob (npnf203 l.11170–11178). Place notes: all syr places are `certain` in Pleiades. The Seleucia-Ctesiphon URL points to Ctesiphon alone (893976), and the note correctly describes Ctesiphon's position "35 km south of modern Baghdad".

---

## Not flagged (checked and acceptable)
- Card order: every page follows the site's `when` field. The hal dream (c. 374) comes first, and the undated syr dreams sit inside Ephrem's lifetime.
- Main-story endings: alx's legacy close ("people loved it and argued over it") reports reception, not a moral. The other three end on events or quotes.
- Pleiades certainty: every place except the Arsinoe name (A8) is `certain`. Neo-Caesarea's locations carry 10 km accuracy, but they are still rated `certain`.
- "Later tradition called him the seer" (alx Didymus): this follows the record's deliberate choice not to attribute the name to Jerome's De Viris 109.
