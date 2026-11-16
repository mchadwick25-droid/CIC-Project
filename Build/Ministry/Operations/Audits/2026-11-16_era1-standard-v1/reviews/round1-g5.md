# Round 1 review, group g5

Briefs: `marcion-of-pontus` (batch1), `valentinus` (batch1), `hippolytus-of-rome` (batch2), `novatian` (batch2).

## Step 0: the blind pair (written before opening the pattern, the bar or the batch)

X (Constantinople, 380, the Anastasia) is the stronger Standard-v1 brief. Reasons:

1. Personal before impact. X gives the man himself early (the friendship with Basil, the refusal over Sasima, in his own words: "piglets and chickens"). Y has no personal beat at all; Novatian is known only by office and by what others say of him.
2. Every stance has what came of it. X: the Trinity preaching leads to Theodosius's order and the churches filled again; "what he did not take on he did not heal" leads to Agatho citing him three centuries later. Y: the On the Trinity stance ("crucified between two thieves") is followed only by Jerome's note that the book was taken for Cyprian's, which is a fact about the book, not a consequence of the stance.
3. Opening. X's first sentences put the reader in a city, a year, a crisis, with the person at its centre. Y's first two sentences are about Cornelius and the lapsed; Novatian enters in sentence three as the one who "refused".
4. Wandering. Y has sentences that do not move his story: "who had sided with Cornelius"; the long list in the last paragraph (Phrygia, Paphlagonia, Celestinus) reads as an appendix. X's sentences mostly each push the story.
5. Y's strength is honesty about the record ("most of what we have comes from his enemies"), which is good, and both are clear and readable. But Y reads as a report on a schism; X reads as a life.

Which was which (added after the full read): X is the bar brief `gregory-of-nazianzus`; Y is the batch brief `novatian`. The preference stands, and its reasons recur as findings on Novatian below (no moment, a stance with no consequence, the split told in two passes).

## Bar briefs compared against

Methodius of Olympus (thin, hostile-weighted record), Gregory of Tours and Benedict of Nursia (the Standard v1 opening, witnesses and impact), Origen and Ephrem the Syrian (flow, joined reasons), Gregory of Nyssa (an honest limit inside the story), John Chrysostom (AI-tell model), Athanasius (storytelling). All ten read in full from `Who-Profiles/bar/`.

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out, info) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Tool verdict |
|---|---|---|---|---|---|---|---|---|
| marcion-of-pontus | 325 | 9.6 | 7.9 | 76.9 | 21.7 | 0.6 | 13% | pass |
| valentinus | 314 | 9.5 | 8.3 | 68.1 | 18.5 | 1.0 | 12% | pass |
| hippolytus-of-rome | 314 | 8.8 | 6.8 | 78.9 | 18.5 | 0.6 | 18% | pass |
| novatian | 321 | 9.8 | 8.3 | 71.6 | 20.1 | 0.6 | 0% | pass |

All four are at or under 325 words, so no length judgment is owed. Hippolytus's names-out grade (6.8) and 18% short sentences say its prose is plain and choppy in places and its grade leans on names; see its sentence test. Novatian's 0% short sentences and Marcion's 21.7 words a sentence point to long sentences; each was read for ones the ear loses.

---

## marcion-of-pontus (batch1): BLOCKED, 2 blocking

### Blocking

**B1. The Polycarp exchange will not be followed by ear (item 11; item 4, "statements with no context or meaning").**
Sentence: "Irenaeus of Lyon tells that when Polycarp, the old bishop of Smyrna, met him, Marcion asked, "Do you recognize us?" Polycarp answered, "I recognize, I recognize the first-born of Satan.""
The quotations themselves match `comparison.md` E24 and E25 exactly, and E24/E25 are grounded in held originals (Gebhardt 1054-1056; Hadrian I, MGH Ep. 5, 17230-17231; npnf201 22977-22982), so fidelity passes. The ear does not. A listener hears one man ask "Do you recognize us?" and will take it literally ("do you know who I am?"). The point, which the card note for E24 states and Irenaeus's next sentence carries ("Such was the horror which the apostles and their disciples had against holding even verbal communication with any corrupters of the truth", `anf01` 39884-39886), is that Marcion asked to be owned as a fellow Christian and Polycarp refused. Nothing in the brief tells the listener that, and "us" from one speaker is left unexplained. The doubled "I recognize, I recognize" without "you" will also sound like a stumble when spoken unless the narrator has set it up.
Fix I would accept: one frame clause from Irenaeus's own context before the quotation, so the reply lands as a refusal. For example: "...met him, Marcion asked to be owned as a brother: "Do you recognize us?" Polycarp answered, "I recognize, I recognize the first-born of Satan."" (or without the colon: "Marcion, asking to be owned as one of the faithful, said ..."). Keep the comparison's final readings unchanged.

**B2. The opening gives no "what was going on" (item 16).**
Sentences 1-2 give "Around 150", Rome, Pontus on the Black Sea coast of Asia Minor, and the tradition, but nothing of the moment in Rome. Every bar brief has it (Methodius: "Origen had been dead some fifty years, and his books still had critics and defenders"; Benedict: "Italy was ruled by Gothic kings"). A held line supplies it: Irenaeus III.4.3 (`anf01` 39968-39984) puts Valentinus, Cerdo and then Marcion at Rome under the same run of bishops, Hyginus to Anicetus, and III.3.4 (`anf01` 39870-39875) has Polycarp come to Rome under Anicetus and turn many back from Valentinus and Marcion. The second also gives the Polycarp scene its setting and a consequence the writer left out for length.
Fix I would accept: one clause of setting from those lines (for example that several rival teachers had come to Rome in those years, Irenaeus naming Valentinus and Cerdo), paid for by a cut elsewhere (see the sentence test).

### Rigor: what was checked and holds

- "Around 150 ... teaching in Rome": Justin, First Apology 26, "even at this day alive, and teaching" (`anf01` 14943-14944); Apology 46, "one hundred and fifty years ago" (15680); Irenaeus III.4.3, flourished under Anicetus (39983-39984); Tertullian, Prescription 30, "in the reign of Antoninus" (`anf03` 21334). Holds as an approximate year.
- Teaching two: Justin (`anf01` 14943-14946), Irenaeus I.27.1-2 (33567-33594), Tertullian (`anf03` 22609-22612, 23735-23736). Tertullian had the Antitheses and Marcion's Gospel before him (28903-28917, 29246-29249), so his witness is independent of Irenaeus on the teaching. Passes "teaching two".
- Life one: "Tertullian, but neither earlier witness, tells that Marcion first belonged to the church at Rome, which put him out": Prescription 30 (`anf03` 21335-21345), Against Marcion IV.4 (29237-29240). Justin 26 and 58 and Irenaeus III.4.3 do not say it (in III.4.3 it is Cerdo who is excommunicated, 39977-39983). Marked as one witness. Passes.
- Cut down Luke and Paul "to fit this teaching": Irenaeus I.27.2 (33581-33594, removing what calls the Maker His Father) carries the purpose; Tertullian IV.2 and V.1 (29097-29103, 36484-36488). Holds.
- "many of every nation" (14946), churches of their own (29322-29330), four Gospels "more ... or fewer ... For Marcion" (41044-41046, 41141-41146), five books with the fourth testing his Gospel (28913-28917). Hold.
- Epiphanius's place list (`epiphanius_panarion-haer-34-64` 7462-7472) and Theodoret's eight villages (`npnf203` 31511-31512). Hold.
- "We have none of Marcion's own books" (writer's flag). It is a statement about the record, an honest limit of the `absence` kind, and it is true of what survives; no held file contains a work of his. It may stand. It is also what makes the next clause ("so nearly all we know of him comes from men who thought as Polycarp did") a sound inference. The writer's alternative opening is acceptable but not needed.
- "Two centuries after Marcion" and "In the century after that" (writer's flag). Panarion about 375 is roughly 225 years after 150; Theodoret's Letter 81 to the consul Nomus is about a century later again. Both rest on widely accepted dates of the two writers, not on a modern scholar's private reckoning, and both are approximate in the right direction. They may stand.

### Non-blocking

- "The cut-down Scriptures drew an answer. Irenaeus argued that the church has four Gospels ...". Irenaeus's four-Gospel case (III.11.7-9) answers several groups at once (those who use only Matthew, only Mark, only John), not Marcion alone. "named Marcion as one who made them fewer" is honest; "drew an answer" slightly overstates the cause for Irenaeus. Tertullian's books are squarely an answer to Marcion. Consider "drew answers" with Tertullian first, or keep as is.
- "Tertullian, but neither earlier witness, tells that Marcion first belonged to the church at Rome, which put him out, but his own churches spread all the same." Two "but"s in one 30-word sentence; the ear loses which "but" turns against what. Split at "out" or join the spread to the next sentence.

### Craft (item 10), beside the bar

1. Good storytelling. Line: a teacher from Pontus set another God above the Creator and cut the Scriptures to fit; his churches spread in his lifetime, drew the church's answer on its Gospels, and lasted three centuries. Weakest: "The cut-down Scriptures drew an answer." Beside Gregory of Tours, "and a king put that faith to the test." A plainer hinge, but it carries a cause. Reaches the level.
2. Flow. Weakest link: the double-"but" sentence above, against Origen, "In his eighteenth year Origen took charge of teaching the faith in Alexandria, because everyone else had fled." Close to the level; the non-blocking recast brings it there.
3. No AI tells. Weakest: "his own churches spread all the same." Beside John Chrysostom's opening paragraph. A light connective, no device. Reaches the level.
4. No hanging sentences. The Polycarp exchange ends paragraph 1 on a quotation, and "men who thought as Polycarp did" picks it up at once; sound. The close, Theodoret's eight villages, ends where the record ends, like Ephrem's "a month later, Palladius says, he died there." Reaches the level (but see B1 on the exchange itself).
5. Everything relevant. The idea of why he mattered is there: the God of the law and the prophets was not the Father of Jesus, and his chief work was to separate the law from the gospel. Beside Athanasius, "If the Son were only a creature ...". Reaches the level.

### Sentence test: 1 marked of 15

- Marked: "In the century after that, Theodoret of Cyrrhus, a bishop in Syria, wrote that he had led eight villages of Marcionites over to his own faith." A second example of the same consequence (the churches lasted) where Epiphanius already carries it. It does finish the story by showing the churches being drawn back, so it may stay; if B2's setting clause needs room, this is the sentence to fold into the Epiphanius sentence ("... and Theodoret of Cyrrhus, a century later, led eight villages of them over to his faith").

---

## valentinus (batch1): BLOCKED, 3 blocking

### Blocking

**B1. "Irenaeus and Clement wrote independently" is unsupported and contradicted by a held source (items 1, 6; writer's flag).**
Sentence: "Irenaeus and Clement wrote independently, and on his teaching they agree on two points."
The writer marks it as our judgment with no ancient line behind it. A held line goes against it: Eusebius, Church History VI.13, says Clement, in his book On the Passover, "mentions Melito and Irenæus, and certain others, and gives extracts from their writings" (`npnf201` 34263-34266). Clement read Irenaeus. The two-witness rule is still met, but for a different reason the record does carry: Clement quotes Valentinus's own letters and homily (`anf02` 34289-34301, 39090-39108), which Irenaeus does not, so on the teaching Clement stands on Valentinus's words, not on Irenaeus. The sentence is also the paragraph's thesis-opening source announcement (item 4, status register), so the fix is a rewrite of the passage, not a word swap.
Fix I would accept: drop "wrote independently" and let Clement's access carry the second witness, joined to the teaching itself, e.g. "Clement had Valentinus's own letters before him, and on two points he and Irenaeus agree: Valentinus placed the Maker of this world below a higher, unseen God, and his school held ..." (no colon-reveal if the writer prefers; a plain "and" join works).

**B2. "Valentinus's own words survive only in a few passages that Clement of Alexandria quotes" is false against a held file (item 1; item 4, loose quantifier "only").**
The Refutation, in the held `anf05`, quotes a psalm of Valentinus word for word: "And Valentinus has elucidated this ... in a psalm ... expressing himself thus: 'I behold all things suspended in air by spirit ...'" (`anf05` 9787-9802), and tells his vision of a newborn child who said he was the Word (10053-10057). Clement holds most of what survives, not all.
Fix I would accept: "Valentinus's own words survive only in a few passages his opponents quote, most of them in Clement of Alexandria, who quotes them in order to answer them." Or name Clement as the chief keeper without "only".

**B3. The opening gives no "what was going on" (item 16).**
"Around 140, a teacher named Valentinus came to Rome." The next sentences give his arrival and stay by bishops and the tradition, but nothing of the moment, against every bar opening. The same held line as Marcion's B2 supplies it: Irenaeus III.4.3 (`anf01` 39968-39983) has Cerdo arrive at Rome in the same years and Marcion follow him. One clause is enough; the region for Rome (Italy) can go in the same clause.
Fix I would accept: a single clause of setting from III.4.3, paid for by folding "Tertullian of Carthage, another opponent, tells how the break came" into the next sentence (see the sentence test).

### Rigor: what was checked and holds

- "Around 140": Irenaeus III.4.3, "came to Rome in the time of Hyginus, flourished under Pius, and remained until Anicetus" (`anf01` 39968-39970); Eusebius IV.10, Hyginus bishop in the first year of Antoninus (`npnf201` 22120-22126). Approximate and held. May stand.
- The break, its reason and the confessor: Tertullian, Against the Valentinians 4 (`anf03` 43109-43116); "ambition ... revenge" (43113-43115). "Tertullian alone tells this": not in Irenaeus I.11 or III.4.3, nor Clement. Holds. Life one, marked.
- The heart as inn, and the quotation: `anf02` 34296-34302; matches E28 final, unchanged. Holds.
- Maker below a higher God: Irenaeus I.11.1 (`anf01` 31535-31543); Clement IV.13, the Creator as "Painter" whose image is "to the glory of the invisible One" (`anf02` 39103-39110). Saved by nature: Clement II.3 (32106-32109), IV.13 (39095-39096); Irenaeus I.6.2 (`anf01` 30754-30763). Teaching two holds.
- Paired powers and the fall: Irenaeus I.11.1 (31522-31531). "Irenaeus alone sets out the fuller system" is true of the witnesses the brief uses (Clement does not confirm it). Strictly, Tertullian's Against the Valentinians and the Refutation also set out a system; neither is in the brief, and the card can say why. Acceptable; see non-blocking.
- Ptolemy and Heracleon (29872-29873; `anf02` 38778-38780); Irenaeus read their books, met some, feared believers would be carried off (29844-29854); earlier writers failed and to overthrow them is to overthrow every heresy (44326-44338). Hold. "So he wrote his five books" slightly widens the preface's purpose (it introduces Book I's exposition), but IV preface 2 says the whole work turns on the Valentinians; acceptable.

### Non-blocking

- "Irenaeus alone sets out the fuller system": consider "Irenaeus sets out a fuller system, which Clement does not confirm", which is exact against all held files.
- "theirs was one of the Gnostic Christianities, which claimed a knowledge higher than faith": "Gnostic Christianities" is a plural few listeners know; it reads close to a label. "one of the Gnostic schools" would be plainer, if the tradition name stays recognizable.

### Craft (item 10), beside the bar

1. Good storytelling. Line: a gifted teacher came to Rome, broke with the church when he was passed over for bishop, taught a higher God and an elect saved by nature, and his school drove Irenaeus to write his five books. Weakest: "Irenaeus and Clement wrote independently, and on his teaching they agree on two points." Beside Methodius, "Both men admired Origen, so neither is a neutral witness." Methodius's source sentence follows the witnesses' content and weighs it; this one announces before the content. Does not reach the level here (folded into B1's rewrite).
2. Flow. Weakest link: "...driven by ambition and revenge." to "Valentinus's own words survive only in a few passages ...". Beside Benedict, "The Rule is Benedict's own words." Benedict's turn is a single clean pivot; this one is close to it. Reaches the level once B2 is fixed.
3. No AI tells. Weakest: "tells how the break came." Beside John Chrysostom's opening. A plain announcing phrase, no device. Reaches the level.
4. No hanging sentences. The close: "Earlier writers had failed to refute the Valentinians, he says, because they did not know their system, and whoever overthrew them overthrew every heresy." Beside Gregory of Tours's close, "his is the only account we have." It is Irenaeus's own claim, attributed, and finishes the story of the reply. Reaches the level.
5. Everything relevant. Why he mattered, as an idea: a higher, unseen God above the world's Maker, and a people saved by nature above believers who need faith. Beside Origen's body, soul and spirit. Reaches the level.

### Sentence test: 1 marked of 17 (plus the B1 sentence)

- Marked: "Tertullian of Carthage, another opponent, tells how the break came." A transition that only connects; the witness and his leaning can go into the next sentence ("Tertullian of Carthage, another opponent, says Valentinus expected to be made bishop ..."). This frees the room B3 needs.

---

## hippolytus-of-rome (batch2): BLOCKED, 1 blocking

### Blocking

**B1. His rank is told as settled, and the brief contradicts itself on it (items 1, 7).**
Sentence: "Hippolytus was a presbyter and writer there, in the Roman church of the third century." Close: "Theodoret of Cyrrhus quoted Hippolytus as a bishop and martyr".
The list of 354 calls him "Yppolitus presbiter" (`chronica-minora` 13078). Eusebius says he "presided over another church" (`npnf201` 35447-35449); Jerome calls him "bishop of some church (the name of the city I have not been able to learn)" (`npnf203` 40690-40692); Theodoret, "Hippolytus and Methodius, bishops and martyrs" (20261-20262). And the Refutation's own author, whom the brief takes to be Hippolytus, writes as one holding high office (the refs record, (a), `anf05` 1129-1135). The writer moved this to the card as "a dispute over his rank that the brief cannot settle", but the opening does settle it, for the presbyter side, and the close then calls him a bishop without comment. A listener will notice. This is a contested point told as settled.
Fix I would accept: do not give a rank in the opening ("Hippolytus was a teacher and writer there"); let the list of 354 call him presbyter where it already does ("the bishop Pontianus and the presbyter Hippolytus"), and either let Theodoret's "bishop and martyr" stand as Theodoret's, or add four words where the list is cited ("though later writers call him a bishop"). Do not add a paragraph.

### The writer's flag: "a book now read as his"

The attribution of the Refutation rests on modern judgment only: the held `anf05` introduction says the work came down under other names and that "the majority of modern scholars have decided" for Hippolytus (`anf05` 760-900). No held ancient witness names this book as his; Jerome's list has an "Against all heresies" (`npnf203` 40701), but whether that is this book is itself the modern question. Under Standard v1 a modern attribution is never told flat and no modern scholar is named. "A book now read as his" does neither: it says, without naming anyone, that the attribution is today's, and the sentence also says "it is an enemy's account". The later sentences ("it says", "he charges", "Hippolytus claims", "by his own account") stand inside that frame. My decision: the honest wording may stand. If the coordinator wants it plainer to the ear, "a book first counted as his in modern times" says the same thing on the same basis (the `anf05` introduction) and avoids "read", which a listener could hear as "read aloud". The card must carry the detail under What is uncertain, as the refs record's (d) already asks. The same basis question touches "In his own book against that teaching" (Against Noetus, attributed by the held file's title only; no held ancient list names it); acceptable as the work's title, and the card should say so.

### Rigor: what was checked and holds

- "Around 220", Callistus bishop: list of 354 (`chronica-minora` 13066-13069; the years 218-222 are the edition's bracketed consular reckoning, so "around 220" is right).
- Callistus's teaching, "one and the same", under two names (`anf05` 13842-13846); Hippolytus's side opposed and was called "worshippers of two gods" / "Ye are Ditheists" (13630-13640, 13837-13839). Holds.
- Against Noetus: Noetus "alleged that Christ was the Father Himself" (23142-23144); "another beside Himself ... I do not mean that there are two Gods" (23614-23620). Quotation matches E32 final, unchanged.
- Sabellius cut off "from apprehension of me" (13816-13819); Sabellius "says that Christ is the Father" (Novatian, `anf05` 61487-61488). Holds.
- Offenders "by us forcibly ejected" (13884-13887); Callistus forgave, the ark of clean and unclean (13873-13878, 13907-13911); crowds (13915-13919); "attempt to call themselves a Catholic Church", "whose school continues" (13950-13960). Hold.
- "The sources we have do not show how the quarrel ended." Searched the Refutation IX-X, Eusebius VI.20-22, Jerome Lives 61, the list of 354 and Theodoret's citations: none says. I believe it.
- Exile with Pontianus to Sardinia under the consuls Severus and Quintianus (13078, 13107; "235" is the consular year, documented); burials "Ypoliti in Tiburtina ... et Pontiani in Calisti" in one entry of the calendar of martyrs (12911-12913). Hold.
- Easter table "gave the cue to Eusebius" (`npnf203` 40692-40695). Holds. Theodoret: 20261-20262. Holds.

### Non-blocking

- "By his own account Hippolytus lost this fight, for crowds went over to Callistus ...". The author never concedes a loss; he reports the crowds and calls Callistus's following a school. "lost this fight" is our reading. Safer: "By his own account, crowds went over to Callistus, whose following still stood ...".
- "A calendar of martyrs in the same book records their burials at Rome in one entry." The listener is not told what "in one entry" shows. Say it: both were remembered as martyrs and buried at Rome, side by side in the same entry.

### Craft (item 10), beside the bar

1. Good storytelling. Line: a Roman teacher fought his bishop over how Father and Son are one God and over forgiving grave sins, lost the crowd by his own telling, was exiled beside a bishop of the other side, and was kept by later teachers as a witness to the faith. Weakest: the calendar sentence above. Beside Athanasius, "In 366 he came back to his church for good, and died in 373." The source gives no more; with the non-blocking recast it reaches the level. Reaches the level.
2. Flow. Weakest link: "...out of fear of him." to "The second quarrel was over grave sins." Beside Gregory of Tours, "He held the same ground against the Arians of Spain." Gregory of Tours's turn carries a claim; this one only announces. Close to the level; "He fought Callistus over grave sins too" would carry it.
3. No AI tells. Weakest: "His books outlived the quarrel." Beside Origen, "His great work was on Scripture." Comparable tidy hinge. Reaches the level.
4. No hanging sentences. "The sources we have do not show how the quarrel ended." is tied to the exile that follows, as in Gregory of Nyssa. The close, Theodoret, finishes the story as Methodius's does. Reaches the level.
5. Everything relevant. The idea: the Word is "another beside" the Father, yet "I do not mean that there are two Gods". Beside Athanasius. Reaches the level.

### Sentence test: 3 marked of 17

- "The second quarrel was over grave sins." A transition that only connects; fold into the next sentence.
- "A calendar of martyrs in the same book records their burials at Rome in one entry." As written it carries a record detail, not a point (see non-blocking).
- "His books outlived the quarrel." A transition; the two sentences after it carry the content, and "His books" can open the Jerome sentence.

---

## novatian (batch2): BLOCKED, 2 blocking

### Blocking

**B1. The story is told in two passes with the Trinity book between them, and there is no moment (items 10 storytelling and flow, 15, 16; writer's flag on the opening).**
Paragraph 1 tells the split and its outcome ("So began Novatianism"). Paragraph 2 turns to On the Trinity. Paragraph 3 goes back: "For the split itself, most of what we have comes from his enemies." That is a transition that only returns to a thread already left, and it is the weakest link in the brief. Beside Gregory of Nyssa ("Macrina had turned him around once before ... But it was his sister who persuaded him") or Athanasius, which runs from the severed hand to the exiles in one line, this is two reports, not one story. The opening also has no sourced moment: the setting is sound (251, Rome, Decius, the lapsed, the tradition named), but Novatian enters as the one who "refused", and the brief has no personal beat. The held sources give two moments the brief already half-tells: the rival consecration, told both ways (Cornelius's drunk country bishops, `npnf201` 38518-38532, against Socrates's "such bishops as entertained similar sentiments", `npnf202` 14083-14084), and Novatian's letter to all the churches (14083-14091). The writer kept the Cornelius charge out of the opening to avoid letting polemic crowd the stance; that is right, but the moment can be the consecration told with both witnesses at once.
Fix I would accept: a rewrite of the order, not a patch. Setting; then the split as one run: the refusal, the consecration told with both witnesses and the hostile one marked, the letter to the churches (his case), the synod, the provinces taking sides, Nicaea, Socrates's own day. Place the Trinity stance either before the split, as who he was (Cornelius himself mocks him as "this dogmatist, this defender of the doctrine of the Church", `npnf201` 38514-38515; quote it only after its rendering check), or after it, with its consequence (B2). Either way "For the split itself" goes.

**B2. The Trinity stance has no consequence, and its one follow-on sentence hangs (items 10 hanging sentences, 15; Mark's rule "Each stance is followed by what came of it").**
Sentence: "Jerome says many later took the book for the work of Cyprian of Carthage, who had sided with Cornelius."
The stance (Christ "crucified between two thieves" between those who call him the Father and those who call him only a man, `anf05` 63444-63459) is real and well told. What follows is a fact about the book's name, with an irony ("who had sided with Cornelius") the brief does not draw. Jerome's line is "a great volume On the Trinity ... which many mistakenly ascribe to Cyprian" (`npnf203` 40895-40897). What it does show, read plainly, is that the book was read as sound teaching in Jerome's day, under the name of the bishop who opposed its author. That is a consequence and can be said in those words, with Jerome as witness. If the writer judges that too much to draw from one line, the brief must say plainly that the sources we have do not show what came of the book in his own day, as Gregory of Nyssa does.
Fix I would accept: recast the Jerome sentence to state what it shows ("In Jerome's day many still read it, though under the name of Cyprian of Carthage, who had sided with Cornelius"), or replace it with the plain honest limit. Part of the B1 rewrite.

### The writer's flags

- No opening scene: see B1. The setting itself passes item 16.
- "Two centuries after the split": Socrates writes after 439 (Celestinus, from 422, is past for him, `npnf202` 19284-19290); 251 to about 440 is under two centuries. "Nearly two centuries after the split" is exact. Non-blocking.
- His case on the lapsed rests on Socrates alone: it does not. Socrates gives his letter (14083-14091), and Socrates's leaning is marked ("who had a friend among the Novatians", 3855-3858). But two hostile held witnesses describe the same rule: Cyprian, Epistle 51.28, mocking those who "exhort to the repentance of atonement, and ... take away the healing" so that the penitent "die without the pale of the Church" (`anf05` 34102-34108), and Jerome, "refusing to receive penitent apostates" (`npnf203` 40887-40890). Eusebius VI.43.1 says the same in hostile words (`npnf201` 38265-38268). So friend and enemies agree on what he taught; only the gentler framing ("their pardon should be left to God") is Socrates's. The brief would gain by one clause saying so, e.g. "and Cyprian, his opponent, describes the same rule in mockery". Non-blocking, but it is the "teaching two" logic applied where it helps.

### Rigor: what was checked and holds

- 251, Cornelius: list of 354, consular year (`chronica-minora` 13121). Decius and the lapsed received: Socrates IV.28 (`npnf202` 14066-14071); "medicines of repentance" (`npnf201` 38292-38294). Hold.
- Made bishop by like-minded bishops (14083-14084). Cornelius's charges: long desired the office (38383-38386), three rustic bishops made drunk and forced (38521-38532), kept by Eusebius (38376-38381). Hold.
- Synod of sixty, "strangers" (38286-38292); "the brethren leave him every day" (38776-38777). Hold.
- Provinces took sides (14090-14096). "many welcomed the stricter rule": Socrates says "others received the rule as just"; "many" is ours. Non-blocking: "others" or "some".
- Nicaea canon 8 on the Cathari: keep rank on a written promise to communicate with the twice married and with the lapsed under penance (`npnf214` 3768-3778); Cathari = Novatian's party (`npnf201` 38268-38270; `npnf203` 40889). The brief drops the twice married, which is a fair narrowing. Holds.
- Phrygia and Paphlagonia "even to the present day" (14057-14059); Rome, many churches until Celestinus (19289-19293). Hold.
- Quotation matches E33 final, unchanged.

### Non-blocking

- "many welcomed the stricter rule" to "others welcomed"; "Two centuries" to "Nearly two centuries"; Cyprian's corroboration, above.

### Craft (item 10), beside the bar

1. Good storytelling. Line: a Roman presbyter refused to take back those who had sacrificed, was made a rival bishop and cut off by a synod, and his strict churches stood for two centuries. The line can be said, but the brief does not run along it (B1). Beside Athanasius, from the severed hand to the exiles. Does not reach the level.
2. Flow. Weakest link: paragraph 2's end to "For the split itself, most of what we have comes from his enemies." Beside Origen, "because everyone else had fled." Does not reach the level (B1).
3. No AI tells. Weakest: "So began Novatianism, the strict churches that took his name." Beside Constantine's "with him begins Imperial and Juridical Christianity, the church of the emperors", which it follows. No device. Reaches the level.
4. No hanging sentences. The Jerome sentence (B2) hangs. The close, Socrates on Phrygia, Paphlagonia and Celestinus, finishes the story of the churches and is sound, though long (41 words with "and at Rome ..."); consider ending the sentence at "strict rule" and giving Rome its own. Does not reach the level until B2 is fixed.
5. Everything relevant. The idea of why he mattered: those who sacrificed should be urged to repent but kept from communion, their pardon left to God; and Christ crucified between two errors. Beside Athanasius. Reaches the level.

### Sentence test: 1 marked of 16 (plus the B1 transition)

- Marked: "Jerome says many later took the book for the work of Cyprian of Carthage, who had sided with Cornelius." As written it does not move his story (B2).
- The B1 transition "For the split itself, most of what we have comes from his enemies." carries the hostile-witness marking, which must stay, but as a transition it goes in the rewrite; the marking moves into the sentence that gives Cornelius's charge.

---

## Summary for the coordinator

| Brief | Verdict | Blocking |
|---|---|---|
| marcion-of-pontus | BLOCKED | B1 Polycarp exchange not followed by ear; B2 opening lacks what was going on |
| valentinus | BLOCKED | B1 "wrote independently" contradicted by Eusebius VI.13; B2 "only in Clement" false (Refutation quotes his psalm); B3 opening lacks what was going on |
| hippolytus-of-rome | BLOCKED | B1 rank told as settled, contradicts the close |
| novatian | BLOCKED | B1 story in two passes, no moment; B2 Trinity stance without consequence, Jerome line hangs |

All fixes are local rewrites of one passage each, except Novatian B1, which is a reordering of the whole brief. None needs new sources: every fix uses a held line cited above. "A book now read as his" (Hippolytus) may stand. "We have none of Marcion's own books", "Around 150", "Around 140", "Around 220", and the "two centuries" phrases in Marcion may stand.
