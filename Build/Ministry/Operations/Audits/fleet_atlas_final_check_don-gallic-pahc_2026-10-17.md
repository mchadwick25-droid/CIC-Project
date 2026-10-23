# Review B: fleet consistency and quality check, Atlas pages for don, gallic and pahc

Reviewer: Opus 5.5, independent and read-only. Date: 2026-10-17.

**Inputs**
- `live_don.md`, `live_gallic.md` and `live_pahc.md` in this folder.
- The records under `.claude/worktrees/review-main/records/<code>/`.
- The vendored texts in `cic/texts/`.
- The Pleiades JSON for every cited place, fetched 2026-10-17.

**Excluded, so not re-reported**
- The record defects in OG-42 (don, gallic) and OG-33 (pahc).
- Everything closed in the don and gallic round 1 to 3 reviews.

**Method**
- Sentence lengths come from a script. It splits on terminal punctuation and counts whitespace tokens, including sentences inside quotations.
- Every claim below was checked against the record named, and quotes were checked against the vendored line.

**Fleet-wide results for checks 1, 2 and 4**
- No participant text contains dash asides, parentheses, "this world", "the world's own" or "grounded".
- Every section's average sentence length is between 9 and 19 words.
- Only two sentences run over 25 words: pahc story unit 2 and the don Passio Marculi teaser. Both are listed below.

**Key**
- B = BLOCKING: wrong, unsupported or misleading.
- S = SHOULD-FIX: craft, readability or an AI tell.

---

## 1. Donatism (don)

**Counts:** B 0, S 7.

The spot-checks pass:
- the 279 to 286 count, held open as "about 280 ... slightly larger";
- the Felix inquiry under threat of torture;
- 310 bishops at Bagai in 394;
- the "Sit down, all" and "Thanks be to God" exchange (`optatus_against-the-donatists.txt` l.183, Appendix l.7324-7328);
- "He was a betrayer" (`don.story.gesta-apud-zenophilum` text);
- Donatus's "what has the emperor to do with the church" (`don.quote.donatus-quid-est-imperatori`, modern_rendering);
- Gregory's 590s letters naming rebaptism in Numidia (`don.core.donatism` horizon);
- the three appeals to the state in 313, 361 and the 390s (`don.gravity.principled-refusal-vs-pragmatic-recourse` l.51-53);
- "In Numidia it far outnumbered the other church" (`don.core.donatism` l.60).

One point needs no change: "sworn" in the Gesta teaser is not in the record, but the vendored Appendix supports it (l.5946, "brought in and sworn").

### D-1 (S). The main story is 714 words, over its 700-word cap. Proposed cut: −18 words, giving 696, with no fact lost.
- **Current (unit 3):** "The doctrine had one public consequence, repeated for a century. Anyone who crossed over from the rival church was washed again. The Donatists did not count it as a second baptism. A hand from a broken line had given nothing the first time. So the Donatist font gave a convert his first real baptism. Imperial edicts named the practice as an offense."
- **Evidence:**
  - "So the Donatist font gave a convert his first real baptism" says again what the sentence before it already says.
  - "The doctrine had one public consequence" is a setup followed by a reveal, which is an AI tell. Its only content, "for a century", is kept in the replacement.
  - `don.term.rebaptism` l.67 and `don.gravity.rebaptism-boundary-marking` l.73 and l.97 support the edict sentence, which is kept.
- **Proposed:** "For a century, anyone who crossed over from the rival church was washed again. The Donatists did not count it as a second baptism. A hand from a broken line had given nothing the first time. Imperial edicts named the practice as an offense." (44 words, replacing 62.)

### D-2 (S). Story unit 1 uses a rhetorical question that sets up a reveal
- **Current:** "They split over one question. Could a bishop's conduct under persecution void what his hand later gave? One side said yes."
- **Evidence:** The pattern is a short setup, then a question, then a three-word reveal. That is assistant cadence. `don.core.donatism` supports the content.
- **Proposed:** "They split over whether a bishop's conduct under persecution could void what his hand later gave. One side said it could." (21 words, so the count does not change.)

### D-3 (S). The Passio Marculi teaser is 27 words
- **Current:** "In his church's own account, a bishop who gave up worldly advancement is flogged, shown a cup, a crown and a palm, and thrown from a cliff."
- **Evidence:** It is the only don sentence over 25 words. `don.story.passio-marculi` tellable_as supports the shorter form.
- **Proposed:** "In his church's own account, a bishop is flogged, shown a cup, a crown and a palm, and thrown from a cliff." (21 words.)

### D-4 (S). The Maximianists highlight says "a larger meeting" with nothing for it to be larger than
- **Current:** "People who followed Maximian, a deacon made rival head of the church in 393. A larger meeting of bishops at Bagai condemned them in 394."
- **Evidence:**
  - The note never mentions the 393 meeting at Cebarsussi, so "larger" compares to nothing.
  - `don.term.concilium` use_note: "Cebarsussi elected a rival primate in 393, and Bagai condemned him in 394."
- **Proposed:** "People who followed Maximian, a deacon made rival primate at Cebarsussi in 393. A larger council of 310 bishops at Bagai condemned them in 394." (25 words.)

### D-5 (S). The Cebarsussi highlight places the town in Byzacena, which none of its cited records says
- **Current:** "A town in the Roman province of Byzacena, where Maximian was made rival head of the church in 393. Its exact site is unknown."
- **Evidence:**
  - Neither `don.term.concilium` nor `don.force.maximianist-fracture` names a province for Cebarsussi. No don record does: `grep -ri byzacen records/don` finds only the general lists of provinces in `don.core.donatism` l.57 and `don.gravity.parallel-hierarchy`.
  - The claim exists only in the build history (Doc_01 Round 2 and 3 reviews: "Cebarsussi convened in Byzacena").
  - Pleiades 329199 lists it as "BAtlas 33 unlocated Cebarsussi" and gives no province.
  - It is probably correct, but the note's own grounding does not support it.
- **Proposed:** Either add a record that carries Byzacena to `grounded_in`, or use "The town where Maximian was made rival primate in 393. Its site is unknown." The second "unlocated" matches Pleiades.

### D-6 (S). Twelve highlights run over 25 words
The trims below use only wording from the note itself or its records.

| Note | Words | Proposed (≤25 words) |
|---|---|---|
| traditores | 31 | "Latin for those who handed over the scriptures in the persecution. Donatists held that such a man could no longer baptize or ordain." (23) |
| the same faith | 29 | "The faith in the Trinity and in Christ, which both churches confessed in the same Latin words. They split over which bishops were valid." (24) |
| persecution of 303 to 305 | 27 | "Diocletian and his fellow emperors hunted Christians in these years. They ordered clergy to hand over the scriptures and church vessels to be destroyed." (25) |
| Vandal | 29 | "The Vandals invaded Roman North Africa in 429 and took Carthage in 439. That removed the Roman power that had judged and coerced the Donatists." (25) |
| hearing at Rome | 28 | "A hearing at Rome in 313. Constantine sent the Donatists' case there. It ruled against them, and they rejected it." (19) |
| Donatus | 28 | "Primate at Carthage from about 313. Exiled about 347, he died in exile. The movement bears his name. Not one page of his survives." (24) |
| Petilian | 27 | "Donatist bishop of Constantina, the renamed Cirta, and a speaker for his church in 411. His letters survive only inside Augustine's replies." (22). This also fixes the problem that "Constantina" is not linked to the Cirta note ("now the city of Constantine"); see `don.figure.petilian` l.38, "Constantina, the renamed Cirta". |
| Tyconius | 29 | "A Donatist writer of the 370s and 380s. His Book of Rules gives seven rules for reading scripture. A council reportedly condemned him around 380." (25) |
| Optatus | 29 | "Catholic bishop of Milevis. In the 360s he wrote seven books against the Donatists, later revised. Most of their early history comes through him." (24) |
| Flavius Marcellinus | 28 | "The imperial officer who judged the hearing of 411, a cleric of neither church. He was put to death in 413 on another charge." (24) |
| Cirta | 26 | "An ancient city of Numidia, now Constantine in Algeria. Bishops met there in a council of disputed date, 305, 307 or later." (22) |
| Novapetra | 30 | "The cliff where, by his church's account, Marculus was held four days and thrown down. It is probably Henchir Encedda, in today's Algeria." (23). "Probably" stays, because Pleiades 334604 is titled "Nova Petra?" and rates the name "less-certain". |

### D-7 (S). Petilian highlight: "Constantina" is not explained
This is covered by the D-6 replacement. It is listed so it is not lost if D-6 is applied only in part.

---

## 2. Gallic monasticism (gallic)

**Counts:** B 1, S 6.

The spot-checks pass:
- He was enrolled at 15 and baptized at 20 (npnf211 l.726 and l.807).
- "Numbers of these afterwards made bishops" (l.1155).
- The discharge before Julian, with "the tyrant" (l.843).
- Nesteros on exorcists (Conf. XV.7, l.39895ff).
- Discretion as "the mother of all virtues" (`gallic.term.discretion` l.86).
- "Cannot be fully grasped by the mind and reason of man" (l.38624).
- Fifty or sixty psalms, then twelve, and two readings added (Inst. II.5-6, l.17191, l.17230).
- "Almost to the number of two thousand" (l.2493).
- Pleiades checks on all 11 places.

### G-1 (B). Four teasers state a miracle or vision as fact. The tellings attribute them, and so do the don and pahc teasers.
- **Current:**
  - Cloak: "That night he sees Christ wearing the half he gave away."
  - Catechumen: "Two hours later the man opens his eyes."
  - Angel and psalms: "The hour for prayer arrives, and one father sings twelve and vanishes."
  - Honoratus: "The snakes give way."
- **Evidence:**
  - The raising of the catechumen is rated Contested. Its `use_note.not_for` reads "evidence that the miracle really happened, which the record does not assess".
  - The cloak is also Contested, with not_for "evidence that the vision really happened".
  - In Honoratus, Hilary "counts this among his master's miracles" (the story text).
  - Every one of these tellings attributes the event: "Sulpitius tells us", "As Sulpitius tells it", "they believed", "Hilary says".
  - Fleet standard: don's teaser reads "In his church's own account, a bishop ... is ... shown a cup", and pahc's reads "The account says the fire arched around him".
  - The teaser is the first sentence a participant sees, and it presents a resurrection as fact.
- **Proposed:**
  - Cloak: "A soldier cuts his cloak in two for a naked beggar at the city gate. That night, Sulpitius says, he sees Christ in his sleep, wearing the half he gave away."
  - Catechumen: "Martin returns to find a new believer dead before baptism. He bolts the door and stretches himself over the body. Sulpitius says that two hours later the man opens his eyes."
  - Angel and psalms: "Egyptian fathers cannot agree how many psalms to sing each evening. At the hour of prayer, Cassian reports, one father sings twelve and vanishes. They take twelve as the number."
  - Honoratus, which also fixes G-5: "A founder walks unafraid onto an island shunned for its filth and snakes, a psalm on his lips. His disciple Hilary says the snakes gave way." (26 words, replacing 43.)

### G-2 (S). The Trier telling ends on "sixteen more years" as a plain fact, but it is Gallus's own figure
- **Current:** "He lived sixteen more years and never went to a synod again."
- **Evidence:**
  - `gallic.story.trier-and-the-ithacian-communion` divergence_note: "Gallus says only that Martin 'lived sixteen years after this.'" Its tellable notes say: "Gallus's figure, carried as given, not converted to a year."
  - `gallic.figure.martin` reads "by Gallus's own reckoning" and fixes Martin's death at 397.
  - Maximus's court at Trier cannot be sixteen years before 397, so the bare figure gives a participant a number the records themselves only report.
  - The vendored text is npnf211 l.5217: "He lived sixteen years after this".
- **Proposed:** "Gallus says he lived sixteen more years, and he never went to a synod again."

### G-3 (S). The Trier teaser overclaims an inner state
- **Current:** "He never fully forgives himself."
- **Evidence:** The source gives two concrete things.
  - His healing came more slowly, and "with tears" he blamed the communion (npnf211 l.5212-5216).
  - He never attended a synod again (l.5217-5218).
  - "Never fully forgives himself" is an inference about his mind that no record states.
- **Proposed:** "He never goes to a synod again."

### G-4 (S). Story unit 5 alters Vincent's formula
- **Current:** "On Lérins, Vincent wrote that the true faith is what has been believed everywhere, always, by everyone."
- **Evidence:**
  - The verbatim text and the modern_rendering of `gallic.quote.believed-everywhere-always-by-all` both read "everywhere, always, by all" (npnf211 l.12186-12187).
  - This is the most famous phrase on the page, and it is cited as Vincent's words.
- **Proposed:** "...what has been believed everywhere, always, by all."

### G-5 (S). The Honoratus teaser is 43 words, against a fleet range of about 23 to 37
- **Current:** "A founder walks unafraid onto an island shunned for its filth and snakes, a psalm on his lips. The snakes give way. Then, as far as his disciple's sermon can be read, the priesthood he had run from catches up with him there."
- **Evidence:** It is the longest teaser in the three pages. The third sentence repeats a hedge that the telling already carries.
- **Proposed:** See G-1. The priesthood point stays in the telling and in story unit 3.

### G-6 (S). The Julian highlight reads like an editor's note
- **Current:** "The text calls this commander only Julian Caesar. One editor of the English edition names him Julian the Apostate. The text never says so."
- **Evidence:**
  - "The text" and "the English edition" are build language, and the closing sentence restates the first. That is the AI tell of a summary ending.
  - The vendored npnf211 note 12 (l.830) reads "Commonly known as Julian the Apostate."
- **Proposed:** "Sulpitius calls this commander only Julian Caesar. A modern editor names him Julian the Apostate, which Sulpitius never does." (19 words.)

### G-7 (S). Ten highlights run over 25 words

| Note | Words | Proposed (≤25 words) |
|---|---|---|
| Sulpitius | 33 | "The Aquitanian who wrote the Life of Martin. He says he learned it partly from Martin and partly from those who lived with him." (25) |
| Chaeremon | 29 | "An old man whose cell stood near Panephysis in Egypt. Years later, in Gaul, Cassian set down his teaching in his own words." (23) |
| synod | 28 | "A meeting of bishops. After Trier, Martin stayed away from them. Vincent of Lérins trusted an ancient general council's decrees to guard the faith." (23) |
| communion | 29 | "Fellowship in the church, and the sacrament within it. Withholding it was the church's sharpest penalty. Martin felt one forced communion lessened his power." (24) |
| discretion | 34 | "The Egyptian fathers' word, passed on by Cassian, for the judgment that keeps each virtue from going wrong. A monk gained it through humility." (25) |
| purity of heart | 31 | "The monk's nearest goal, short of heaven itself. Cassian's Egyptian fathers ranked fasting and night prayer as aids to it, never the point." (23) |
| grace | 28 | "God's help, without which no effort reaches its goal. Scholars still disagree on whether Cassian held that grace or the will begins the good." (25) |
| heretics | 27 | "People judged to have left the ancient, universal church. Martin held that bishops might expel them, but an emperor's sword had no place." (23) |
| Marseilles | 28 | "Greek Massalia, founded around 600 BCE, now Marseille in France. Cassian is said to have founded two houses here, one for men, one for women." (25) |
| Andethanna | 28 | "A village near Trier where Martin sat grieving in the woods. It is probably Niederanven in Luxembourg, though an editor calls the text corrupt." (24) |

---

## 3. House Churches (pahc)

**Counts:** B 1, S 11.

The spot-checks pass:
- "Ground by the teeth of the wild beasts ... pure bread of Christ" (anf01 l.7040-7042).
- "Eighty and six years" (l.3990).
- The Pliny modern_rendering (`pahc.quote.two-female-slaves-who-were-called-deaconesses`).
- The Didache cup prayer (`pahc.quote.first-concerning-the-cup` modern_rendering).
- Lampe and Victor in 189-199, kept as contested (`pahc.contested.rome-monepiscopacy-dating`).
- "Nine thousand ... thirty-nine" (npnf201 l.16899-16906).
- 1 Clement dated "as late as 140" (Welborn's range in the divergence_note).
- Pleiades checks on all 5 places, with one wording issue (P-10).

This page had no independent round-robin before this one. Its round 1 was the author's own review.

### P-1 (B). The Quintus teaser gets the letter's order wrong
- **Current:** "Before praising Polycarp, the letter from Smyrna names Quintus."
- **Evidence:**
  - The Martyrdom of Polycarp opens by praising Polycarp, in ch. I (anf01 l.3760-3772: "and especially to the blessed Polycarp ... set a seal upon it by his martyrdom"). Quintus first appears in ch. IV (l.3839-3850).
  - OG-33 logs this same error in the record's `tellable_as`, and the telling was corrected ("Before Polycarp's own flight and arrest ..."). The teaser on the live page still carries the error.
- **Proposed:** "The letter from Smyrna that honors Polycarp also names Quintus. He came forward for trial and lost his nerve at the sight of the beasts. The letter says the gospel does not teach people to give themselves up."

### P-2 (S). Story unit 2 has a 26-word sentence
- **Current:** "Ignatius, a bishop of Antioch, tells the churches he writes to that they should be subject to the bishop as the apostles were subject to Christ."
- **Evidence:** It is the only sentence on the page over 25 words.
- **Proposed:** "Ignatius, a bishop of Antioch, writes to several churches. He tells them to be subject to the bishop, as the apostles were subject to Christ." (8 and 15 words.)

### P-3 (S). Story unit 3 opens with a rhetorical question that sets up a reveal
- **Current:** "Who should lead, once the apostles were gone? The surviving letters show two different answers."
- **Evidence:** A question followed by a short reveal is assistant cadence. Don's D-2 has the same pattern.
- **Proposed:** "The surviving letters give two different answers to who should lead once the apostles were gone."

### P-4 (S). The main story ends on an aphorism
- **Current (unit 8, last sentence):** "These churches had still been building that line, letter by letter."
- **Evidence:**
  - This is a summary closer under Mark's "remove all the add on tails that dont say anything".
  - The sentence before it ("...argued from an apostolic line they treated as already secure.") is the last real claim, and it is supported by `pahc.force.systematic-theological-mode-elsewhere`.
- **Proposed:** Delete the sentence. The story drops from 642 to 631 words, still within the 600-700 range.

### P-5 (S). The Nero teaser has an unclear "He" and drops the attribution
- **Current:** "The Roman historian Tacitus reports that Nero blamed a group the crowd called Christians. He had them put to death with cruelty."
- **Evidence:**
  - The subject of the sentence before is Tacitus, so "He" first reads as Tacitus.
  - The second sentence also states the executions with no source, although the record's divergence_note holds the event itself contested (Shaw and Jones).
- **Proposed:** "The Roman historian Tacitus reports that Nero blamed a group the crowd called Christians, and had them put to death with cruelty."

### P-6 (S). Two tellings use etic hedges ("scholars") inside the community's own "we" and "our" voice
- **Current:**
  - Nero: "Tacitus wrote from outside our communities ... Some scholars doubt that Christians, as a group known by that name, were punished after the fire. They think a more general memory from later years may have been attached to it."
  - Pliny: "...which they said was harmless. Scholars still debate what that meal was." The same telling says "we have only what Pliny chose to record".
- **Evidence:**
  - CLAUDE.md: "A Representative's hedge language is emic, not etic."
  - Don and gallic tellings hedge in the tradition's own voice ("It is reported, Augustine says"; "as far as Hilary's sermon can be read").
  - Records: `pahc.story.nero-scapegoating` divergence_note ("a later, more general memory retrojected onto the fire") and `pahc.story.pliny-interrogation` divergence_note ("Contested is what the 'common yet harmless' meal actually was").
- **Proposed:**
  - Nero: "We cannot be sure that Christians, as a group known by that name, were punished after the fire. A more general memory from later years may have been attached to it."
  - Pliny: "What that meal was, we cannot say for certain."
- **Consistency note:** the pahc tellings switch between a "we" voice (Nero, Pliny, Martyrdom) and a neutral narrator ("Some scholars argue ..." in Ignatius, Polycarp and 1 Clement). Don and gallic hold one voice throughout. The project lead should decide which voice pahc tellings use. These lines are not rewritten here.

### P-7 (S). The Polycarp-forwards telling understates who called Polycarp a bishop
- **Current:** "He never calls himself bishop, though later tradition remembers him as Smyrna's bishop."
- **Evidence:**
  - The same page says "Ignatius addresses Polycarp ... as a bishop" (story unit 3).
  - The Ignatius telling reads "He asked Polycarp, bishop of Smyrna".
  - The Martyrdom telling calls him "its aged bishop", following Smyrna's own letter.
  - "Later tradition" therefore misplaces the earliest witnesses, Ignatius and Smyrna's letter, which date from his lifetime or his death.
- **Proposed:** "He never calls himself bishop, though Ignatius writes to him as one, and Smyrna's letter on his death calls him its bishop."

### P-8 (S). The Domitian telling uses "plethra" and "denaria", which a participant cannot read
- **Current:** "...they had only nine thousand denaria between them, and not in coin. That was the value of a piece of land of only thirty-nine plethra."
- **Evidence:**
  - Both terms are used without introduction, against the CLAUDE.md rule that a term is introduced before it is used.
  - The vendored translation reads "nine thousand denarii ... a piece of land which contained only thirty-nine acres" (npnf201 l.16899-16906).
  - OG-33 covers the record's dropped "only", not this.
- **Proposed:** "...they had only nine thousand denarii between them, and not in coin. That was the value of a piece of land of only thirty-nine acres."

### P-9 (S). Two tile sentences are clumsy or vague
- **Current:**
  - "After the apostles died, these churches did not settle in these years who should lead."
  - "Following this way could at times bring real danger."
- **Evidence:**
  - The first sentence repeats "these" and puts "in these years" in an awkward place.
  - In the second, "this way" has nothing for it to refer to.
  - Records: `pahc.gravity.authority-consolidation` and `pahc.gravity.state-pressure`.
- **Proposed:** "After the apostles died, these churches had not yet settled who should lead." and "Being a Christian could at times bring real danger."

### P-10 (S). The Philippi highlight gives an ancient name as the modern site
- **Current:** "Its ruins, at Krenides, lie in today's Greece."
- **Evidence:**
  - Pleiades 501482 describes the city as founded "on the site of the Thasian colony of Krinides" and lists Krenides as an ancient name.
  - The page's other place notes give a modern place in that slot ("at Ksar Baghai", "at Archaia Korinthos").
- **Proposed:** "Its ruins lie in today's Greece." See P-12 for the whole note.

### P-11 (S). The card order puts Quintus after Polycarp's death, but his story comes first
- **Current order:** martyrdom-of-polycarp, then quintus-recantation. Both have use_note years 155-156.
- **Evidence:** The Quintus telling begins "Before Polycarp's own flight and arrest". In the letter, Quintus (ch. IV) comes before Polycarp's flight (ch. V) and death (ch. XV-XVI).
- **Proposed:** Swap the two cards.

### P-12 (S). Six highlights run over 25 words

| Note | Words | Proposed (≤25 words) |
|---|---|---|
| Corinth | 28 | "An ancient Greek city in the Peloponnese, whose church removed some elders and drew Rome's letter. Its site is Archaia Korinthos, in Greece." (23) |
| Philippi | 26 | "An ancient city founded by Philip II of Macedon. Its church asked Polycarp for the letters of Ignatius. Its ruins lie in today's Greece." (25) |
| elders | 28 | "Leaders who shared in governing a community. They acted as a council in some churches, and beside one overseer in others." (21) |
| Didache | 29 | "A short teaching manual, likely from one community. It survives almost whole in one copy of 1056. Scholars date it about 50 to 150." (24) |
| Ignatius | 29 | "Bishop of Antioch. Seven letters in his name say he was marched under guard toward death in Rome. Their author and date are disputed." (24) |
| Nero | 26 | "Roman emperor at the Great Fire of Rome in 64. Tacitus says rumor blamed him, and he turned the blame on Christians." (22) |

---

## 4. Consistency across the three pages (check 6)

| Check | don | gallic | pahc |
|---|---|---|---|
| Story 600-700 words | 714. **Over the cap; see D-1** | 699 | 642 (631 after P-4) |
| Cards in date order | Yes | Grouped by Martin's life and then by Egypt. This is a settled choice (gallic OG-42) and is not re-litigated | Yes, except Quintus and Martyrdom (P-11) |
| Telling length 120-250 | 170-238 | 169-249 | 121-250 |
| Teaser length | 27-33 | 23-43 (G-5) | 24-37 |
| Miracles told as testimony | Yes | Tellings yes, **teasers no (G-1)** | Yes |
| Emic hedges in the tradition's voice | Yes | Yes | **Mixed (P-6)** |
| Notes over 25 words | 12 | 10 | 6 |

## Totals
- don: B 0, S 7.
- gallic: B 1, S 6.
- pahc: B 1, S 11.
