# alx term gloss audit, 2026-10-03

**Reviewer note.** The audit below was run by a subagent and every quoted line was matched to the vendored files by script. I re-read eight of the cited lines (prayer, mysterion, pistis, pneuma-hagion, homoiosis, salvation x2, sophia); all eight are word for word. Two verdicts are weaker than the audit states:

- **sophia.** "wisdom is the knowledge of things divine and human" is Clement quoting Philo (anf02 lines 27948-27958), a definition Clement then builds on. It bears on the gloss "Not knowledge held in the mind", but less directly than the audit says.
- **pneuma-hagion.** Origen's "a share in the Holy Spirit we find possessed only by the saints" (anf04 lines 23759-23760) answers who has the Spirit. The gloss "Not an occasional visitor" is a different question, so "source contrary" is not established. Treat it as unverified.

Read the 13 "source bolder" verdicts as a first pass for a human to confirm. Logged as OG-13 in `Build/worlds/alx/Open_Gaps_Tracking.md`.

---

# ALX term gloss audit (24 terms)

Read-only audit. Nothing in the repo was changed.

## How to read this

- Source files (all under `cic/texts/`). Line numbers are the file's own XML line numbers. Tags are stripped only to read.
  - `anf02` = anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml (Clement: Protrepticus, Paedagogus, Stromateis)
  - `anf04` = anf04_tertullian4-minucius-felix-commodian-origen1-2.xml (Origen: De Principiis, Contra Celsum)
  - `anf09` = anf09_gospel-of-peter-diatessaron-origen-commentaries.xml (Origen: Commentary on John)
  - `npnf204` = npnf204_athanasius-select-works-letters.xml (Athanasius)
  - `npnf214` = npnf214_seven-ecumenical-councils.xml (Nicene Creed)
- Each quote is one line, copied verbatim from the line named. A quote may cut off at the line end.
- Headings added by the editors or translators are marked EDITOR HEADING. They are not the author's words.
- Primary verdict = the verdict on the "Not ..." gloss in `plain_meaning` / `quick_meaning`, the one the voice repeats. Other glosses get their own verdict in the detail.
- Verdicts: TRACED, SOURCE-BOLDER, MODERN-CONTRAST, UNVERIFIED as defined in the task.
- One extra label, SOURCE-CONTRARY: used once (pneuma-hagion). The gloss is bolder than the source, the opposite of SOURCE-BOLDER. Flagged so you can reclassify.
- SOURCE-BOLDER is also used where the source states plainly what the gloss denies (for example Clement defines prayer as "converse with God"; the gloss says "Not mainly speaking to God").
- Where no cited locus supports a claim, "searched" says what was searched.

## (a) Summary table

| term | the gloss (short quote) | primary verdict | recommendation |
|---|---|---|---|
| agape | "Not a feeling, but the fruit of real formation" | SOURCE-BOLDER | REWORD FROM SOURCE |
| arete | "Not a habit built by effort" | SOURCE-BOLDER | REWORD FROM SOURCE |
| baptism | "Not a ceremony announcing a choice already made" | MODERN-CONTRAST | REWORD FROM SOURCE |
| christ | "Not a surname added to Jesus" (priest, king, prophet in one) | MODERN-CONTRAST | REWORD FROM SOURCE |
| ekklesia | "Not a building or a members list" | TRACED (building); MODERN-CONTRAST (members list) | KEEP "not a building"; DROP "members list" |
| elpis | "Not optimism, but the soul's staying oriented" | SOURCE-BOLDER | REWORD FROM SOURCE |
| episkopos | "Not a church manager" | MODERN-CONTRAST | REWORD FROM SOURCE |
| fasting | "Not giving up food for health or credit" | MODERN-CONTRAST | REWORD FROM SOURCE |
| homoiosis | "not moral imitation, copying divine conduct" | SOURCE-BOLDER | REWORD FROM SOURCE |
| interpretation | "Not analysis applied to a text" | SOURCE-BOLDER | REWORD FROM SOURCE |
| metanoia | "Not feeling sorry... a change of nous" | TRACED | KEEP (tighten) |
| methexis | "Not by becoming God" | SOURCE-BOLDER | REWORD FROM SOURCE |
| mysterion | "Not a puzzle... not a secret teaching" | SOURCE-BOLDER | REWORD FROM SOURCE |
| oikos | "Not the private family" | MODERN-CONTRAST | REWORD FROM SOURCE |
| pistis | "Not agreeing with a list of claims" | SOURCE-BOLDER | REWORD FROM SOURCE |
| pneuma-hagion | "Not an occasional visitor" | SOURCE-CONTRARY (extra label) | REWORD FROM SOURCE |
| prayer | "Not mainly speaking to God" | SOURCE-BOLDER | REWORD FROM SOURCE |
| psyche | "Not a ghost living inside a body" | SOURCE-BOLDER | REWORD FROM SOURCE |
| salvation | "Not a not-guilty verdict, but healing" | SOURCE-BOLDER | REWORD FROM SOURCE |
| son-of-god | "Not an honor for being close to God" | TRACED | KEEP (drop the Origen line) |
| sophia | "Not knowledge held in the mind" | SOURCE-BOLDER | REWORD FROM SOURCE |
| theosis | "Not becoming a god" | SOURCE-BOLDER | REWORD FROM SOURCE |
| transformation | "Not self-improvement. Not better behavior..." | TRACED | KEEP |
| word-of-god | "Not first a name for the Bible" | TRACED (the Word is a person); MODERN-CONTRAST (not the Bible) | KEEP (tighten) |

## (c) Counts per primary verdict

- TRACED: 5 (ekklesia, metanoia, son-of-god, transformation, word-of-god)
- SOURCE-BOLDER: 13 (agape, arete, elpis, homoiosis, interpretation, methexis, mysterion, pistis, prayer, psyche, salvation, sophia, theosis)
- MODERN-CONTRAST: 5 (baptism, christ, episkopos, fasting, oikos)
- UNVERIFIED: 0 as a primary verdict. Several secondary claims are UNVERIFIED (listed in each detail).
- SOURCE-CONTRARY (extra label): 1 (pneuma-hagion)
- Total: 24

Recommendation counts: KEEP 5 (ekklesia partial, metanoia, son-of-god, transformation, word-of-god), REWORD FROM SOURCE 19, DROP 0 whole terms (one DROP of a single false friend: ekklesia "members list").

Terms where I was unsure: ekklesia, episkopos, fasting, metanoia, pneuma-hagion, word-of-god (see "Unsure" at the end).

## (b) Per-term detail

### agape (alx.term.agape)

Record wording:
- plain_meaning: "Not a feeling, but the fruit of real formation - what a changed soul freely gives."
- quick_meaning: "Not a feeling - the fruit of a soul truly formed."
- false_friend: "warm feelings or affection toward someone"; "a discipline of willpower, forcing loving acts".
- informational: "not a performance of the will"; personal: "the other is performing it."
- Sources cited: clement-stromateis IV, VI, VII; athanasius-de-incarnatione (whole). No relations. No alx quote records.

What the sources say:
- Clement defines love with the word "affection", the very word the false friend rules out.
- [anf02:47087] "divinity of love. For love is not desire on the part of him who loves;"
- [anf02:47088] "but is a relation of affection, restoring the Gnostic to the unity of the"
- [anf02:32833] "intensity of friendship and of affection, with right reason, in the"
- The contrast "done from fear or reward" versus "done from love" is in Clement.
- [anf02:39568] "The same work, then, presents a difference,"
- [anf02:39569] "according as it is done by fear, or accomplished by love, and is"
- [anf02:40000] "the doing of good out of love, and for the sake of its own excellence,"
- Love as a gift of grace:
- [anf02:39544] "day are gone. But they who have been perfected in love, through the"
- [anf02:39545] "grace of God, hold the place of the godly, who shall be manifested at"
- Athanasius, De Incarnatione: searched "love" in the De Incarnatione range (lines 15145-18899). Only "loving-kindness" of God appears (for example line 16434). Nothing on human love. Cited locus "(whole)" supports nothing here.

Verdicts:
- "Not a feeling / not warm feelings or affection": SOURCE-BOLDER. Clement says love is "a relation of affection" (VI.9, anf02:47088).
- "Not a discipline of willpower / performance": TRACED in substance (fear or reward versus love, Strom. IV.18 and IV.22 above).
- "fruit of formation": TRACED in spirit ("perfected in love, through the grace of God").

Recommendation: REWORD FROM SOURCE. Drop "Not a feeling". Say: love is "a relation of affection", not desire, and not good done "by fear" or for reward (Strom. IV.18, VI.9).

### arete (alx.term.arete)

Record wording:
- plain_meaning: "Not a habit built by effort, but the visible fruit of a soul truly changed."
- quick_meaning: "Not a habit built by effort - the fruit of a soul truly changed."
- false_friend: "excellence built through repeated practice, as in Aristotle"; "correct moral decisions made through good reasoning".
- informational: "Here virtue is something a soul receives rather than builds"; translational: "not a skill the soul builds".
- Sources: clement-stromateis II, IV, VI, VII; athanasius-vita-antonii (whole).

What the sources say:
- Clement says we are made for acquiring virtue.
- [anf02:47620] "Above all, this ought to be known, that by nature"
- [anf02:47621] "we are adapted for virtue; not so as to be possessed of it from our birth,"
- [anf02:47622] "but so as to be adapted for acquiring it."
- Clement says knowledge (gnosis) is acquired and becomes habit through practice. The sentence just before names virtues as habits.
- [anf02:47174] "Further, also, the philosophers regard the virtues as habits,"
- [anf02:47179] "and the acquiring of it in its elements demands application, and training,"
- [anf02:47180] "and progress; and then from incessant practice it passes into a habit;"
- Clement also holds that virtue is not built by everyday practice and is God-given (the gloss's side).
- [anf02:50139] "is the friend of God. For neither are we born by nature possessing virtue,"
- [anf02:50140] "nor after we are born does it grow naturally, as certain parts of the" (Strom. VII.3)
- [anf02:50142] "virtue, like speech, perfected by the practice that results from everyday"
- [anf02:43028] "it results that virtue is neither by nature, nor is it taught, but is" (Plato's Meno as quoted by Clement, Strom. V.13)
- Athanasius, Life of Antony: effort language is heavy.
- [npnf204:31288] "keep all his desire and energy for perfecting his discipline. He"
- [npnf204:31747] ".” Wherefore virtue hath need at our hands of willingness alone,"
- [npnf204:31434] "world for the sake of it, ought not to be measured by time, but by"
- [npnf204:31435] "desire and fixity of purpose.’ He at least gave no thought to the"

Verdicts:
- "Not a habit built by effort": SOURCE-BOLDER. Clement says virtue is acquired and practice becomes habit. Antony's Life is built on "discipline". The sources hold both sides (gift and effort). The gloss keeps only the gift side.
- "Aristotle": MODERN-CONTRAST in part. Aristotle is not discussed on this point in the cited loci. Clement does note that "the philosophers regard the virtues as habits" (VI.9).

Recommendation: REWORD FROM SOURCE. Say virtue is for acquiring ("adapted for acquiring it") and that it is "neither by nature, nor... taught" but comes with God's help; Antony says it "hath need at our hands of willingness".

### baptism (alx.term.baptism)

Record wording:
- plain_meaning: "Not a ceremony announcing a choice already made. A real crossing - the body sharing in Christ's death and rising."
- quick_meaning: "Not a ceremony marking a choice. A real crossing, in the body, into Christ's death and rising."
- false_friend: "a public statement of a private decision already made"; "an empty ritual that only symbolizes something".
- informational: "not a picture of it". Body "goes under the water and the breath stops".
- Sources: clement-paidagogos I.6-7. No relations.

What the sources say:
- Clement, Paed. I.6 (cited locus) lists effects. It has no line on death and rising and none on breath or immersion.
- [anf02:19292] "became. Being baptized, we are illuminated; illuminated, we become sons;"
- [anf02:19297] "and perfection, and washing: washing, by which"
- [anf02:19299] "transgressions are remitted; and illumination, by which that holy light"
- [anf02:19397] "faith, and faith with baptism is trained by the Holy Spirit. For that"
- Death and rising in baptism appears in Origen (quoting Paul), not Clement:
- [anf04:42097] "Him; as is declared by Paul, “For we were buried with Him by"
- [anf04:42098] "baptism, and have also risen with Him.” Cf. Rom. vi. 4.  These matters, however, which relate"
- Searched Clement, Origen, Athanasius for baptism as "sign" or "picture". No vendored line makes baptism a mere sign. One line calls pagan purification a sign: [anf02:40104] "and purification are practiced for a sign. Now purity is to think holy".
- Searched for any line on a choice "already made" or "a public statement". None.

Verdicts:
- "Not a ceremony announcing a choice already made": MODERN-CONTRAST. It answers the later debate over baptism as a public sign of personal faith. No source discusses it.
- "real effect, not a picture": TRACED in spirit (Clement: remission, illumination, sonship).
- "body goes under the water and the breath stops": UNVERIFIED (nothing in the vendored texts).

Recommendation: REWORD FROM SOURCE. Use Clement's chain: "Being baptized, we are illuminated; illuminated, we become sons". Drop the believer's-baptism jab and the breath detail.

### christ (alx.term.christ)

Record wording:
- plain_meaning: "Not a surname added to Jesus, but a confession - the Anointed One, sent to be priest, king, and prophet all in one person."
- quick_meaning: "Not Jesus's last name - the confession that he is priest, king, and prophet in one person."
- false_friend: "Christ used as Jesus's last name"; "a vague title of general holiness".
- informational: "commissioned as all three at once... and not as an honor added afterward".
- Sources: clement-stromateis I.5; origen-comm-john I; athanasius-de-incarnatione 1-3, 54. Relations: son-of-god, word-of-god.

What the sources say:
- Clement names the three anointed offices, but of Israel, not as one office of Christ.
- [anf02:40413] "of God. Wherefore, of all the circumcised tribes, those anointed to be"
- [anf02:40414] "high priests, and kings, and prophets, were reckoned more holy. Whence He"
- Clement on the name Christ:
- [anf02:15278] "but inasmuch as He has now assumed the name Christ, consecrated of old,"
- Origen links anointing to kingship and sometimes priesthood only, and says it was not from the start. (The title line "Christ as Anointed (Christ) and as King" at anf09:21721 is an EDITOR HEADING.)
- [anf09:21727] "fellows.”  His loving righteousness and hating iniquity were"
- [anf09:21728] "thus added claims in Him; His anointing was not contemporary with His"
- [anf09:21729] "being nor inherited by Him from the first.  Anointing is a symbol"
- [anf09:21730] "of entering on the kingship, and sometimes also on the priesthood; and"
- Athanasius says he was anointed for our sake, not to become God or King.
- [npnf204:44132] "And therefore He is here ‘anointed,’ not that He may become"
- [npnf204:44133] "God, for He was so even before; nor that He may become King, for He had"
- Searched Clement, Origen, Athanasius for a "priest, king, and prophet" formula applied to Christ. Not found in the vendored texts.

Verdicts:
- "Not a surname": MODERN-CONTRAST. No source discusses "last name".
- "priest, king and prophet in one person": UNVERIFIED as a formula for Christ (the three appear only in Clement's list of Israel's anointed).
- "not an honor added afterward": contradicted in part by Origen ("His anointing was not contemporary with His being"). Athanasius says the opposite ("not that He may become... King"). The sources disagree with each other here.

Recommendation: REWORD FROM SOURCE. Say "Christ" means "anointed" (Clement: "the name Christ, consecrated of old"). Drop the three-offices formula, or present it as Israel's anointed (Clement), not Christ's single office.

### ekklesia (alx.term.ekklesia)

Record wording:
- plain_meaning: "Not a building or a members list, but the assembly gathered around the Logos who calls it."
- quick_meaning: "Not a building or a list of members. It is the assembly gathered around the Logos."
- false_friend: "a building where Christians meet"; "an organization with a membership roll".
- personal: baptized person who never shares "belongs only in name"; a catechumen "is... more fully inside the church."
- Sources: clement-stromateis VII.5; athanasius-festal-letters. Relation: episkopos.

What the sources say:
- [anf02:50446] "of God fashioned into a temple? For it is not now the place,"
- [anf02:50447] "but the assemblage of the elect, Montacutius suggests ἐκκλήτων,"
- [anf02:50450] "[Notes 3 and 5, p. 290, supra.] that I call the"
- (The sentence reads: "For it is not now the place, but the assemblage of the elect... that I call the Church." An editor's note is spliced in between.)
- Clement also treats the Church as having orders:
- [anf02:47891] "bishops, presbyters, deacons, are imitations of the angelic glory,"
- Searched "catechumen" in Clement, Origen, Athanasius. No line says a catechumen is more fully in the church than an absent baptized person.
- Searched for a "roll" or "membership". Nothing.

Verdicts:
- "Not a building": TRACED (Strom. VII.5).
- "Not a list of members / membership roll": MODERN-CONTRAST. No source discusses it. Clement's own "grades... bishops, presbyters, deacons" is an ordered body.
- "catechumen more fully inside than a baptized non-sharer": UNVERIFIED.

Recommendation: KEEP "not a building" with Clement's wording. DROP "members list" and the catechumen line unless a source is found.

### elpis (alx.term.elpis)

Record wording:
- plain_meaning: "Not optimism, but the soul's staying oriented toward a life not yet fully reached."
- quick_meaning: "Not optimism. It is staying turned toward a life not yet fully reached."
- false_friend: "optimism, expecting things to turn out well"; "a mood that rises and falls with circumstances".
- translational: "grounded hope in something already accomplished, not a feeling about the future".
- Sources: clement-stromateis II.12, VII; athanasius-de-incarnatione 20-32. Relation: metanoia.

What the sources say:
- Clement defines hope as expectation of good, and even says "sanguine".
- [anf02:32826] "and hope. Now hope is the expectation of good things, or an expectation"
- [anf02:32827] "sanguine of absent"
- [anf02:32511] "being present. And hope is the expectation of the possession of"
- [anf02:32512] "good. Necessarily, then, is expectation founded on faith. Now he is"
- Athanasius ties hope to resurrection.
- [npnf204:16537] "for us, by the hope of resurrection which He has given us. For since"
- Searched for hope as "a mood". Nothing.

Verdicts:
- "Not optimism / not expecting things to turn out well": SOURCE-BOLDER. Clement's definition is "expectation of good things" and "an expectation sanguine of absent good".
- "grounded in accomplished resurrection": TRACED in spirit (Athanasius).
- "a mood that rises and falls": UNVERIFIED.

Recommendation: REWORD FROM SOURCE. Use "hope is the expectation of the possession of good", "founded on faith" (Strom. II.6, II.9) and Athanasius's "hope of resurrection". Drop "Not optimism".

### episkopos (alx.term.episkopos)

Record wording:
- plain_meaning: "Not a church manager. The bishop governs how the community is formed and guards what it received."
- quick_meaning: "Not an administrator. The bishop governs formation, not budgets."
- false_friend: "a diocesan executive who manages clergy and finances"; "the teacher's organizational superior".
- personal: "the office does not confer the standing on its own; the person's own righteousness is what the office recognizes."
- Sources: athanasius-festal-letters; athanasius-de-decretis 19-20; clement-stromateis VI.13. Relations: quote the-grades-here-in-the-church; didaskalos (tension); ekklesia.

What the sources say:
- Clement, VI.13, is about the true presbyter and deacon. The word "bishop" is not in this passage.
- [anf02:47856] "the chosen body of the apostles. Such an one is in reality a"
- [anf02:47858] "will of God, if he do and teach what is the Lord’s; not as"
- [anf02:47865] "is used in Tit. i. 5. by men, nor regarded righteous"
- [anf02:47866] "because a presbyter, but enrolled in the presbyterate Presbytery"
- Same chapter, Clement treats the three grades as real and as images of heaven:
- [anf02:47891] "bishops, presbyters, deacons, are imitations of the angelic glory,"
- Athanasius's own text shows a bishop doing administration (grain for widows):
- [npnf204:22754] "corn was given by the father of the Emperors for the support of certain"
- [npnf204:22756] "received it up to this time, Athanasius getting nothing therefrom, but"
- [npnf204:22757] "the trouble of assisting them. But now, although the recipients"
- (This is a letter quoted inside Apologia contra Arianos, §18, which calls him "our fellow-minister Athanasius", line 22751. Treat it as evidence for what bishops did, not as Athanasius's own definition.)
- Searched De Decretis 19-20 range (De Decretis begins at npnf204:26384) for the bishop's office. It argues the Nicene confession, not the bishop's role.

Verdicts:
- "Not a church manager / not budgets": MODERN-CONTRAST. It answers a modern executive image. The vendored text shows a bishop overseeing relief. No source says the bishop is not an administrator.
- "office does not confer the standing": the quoted Clement line fits "not as being ordained by men". But it is about the "true" presbyter, and Clement keeps the grades. The record's reading is stronger than the text. Partly TRACED, partly UNVERIFIED.
- "Clement treats the bishop as a human participant in divine governance": UNVERIFIED.

Recommendation: REWORD FROM SOURCE. Keep the Clement quote as it stands ("not... regarded righteous because a presbyter, but enrolled in the presbyterate because righteous"). Say "overseer". Drop "not budgets" and "not an administrator".

### fasting (alx.term.fasting)

Record wording:
- plain_meaning: "Not giving up food for health or credit. Training the soul's wanting, through the body's hunger."
- quick_meaning: "Not a diet - training the soul's own wanting, practiced through the body's hunger."
- false_friend: "dieting or food restriction for health"; "earning merit through hardship".
- Sources: clement-paidagogos II.1; athanasius-festal-letters (Paschal fast). Relation: prayer.

What the sources say:
- Clement, Paed. II.1 (starts anf02:21201): "On Eating". It argues moderation. Searched that chapter for "fast", "fasting": none. The cited locus does not discuss fasting.
- Clement, Strom. VI.12 and VII.12: fasting is abstinence from evil.
- [anf02:47770] "Now fastings signify abstinence from all"
- [anf02:47771] "evils whatsoever, both in action and in word, and in thought"
- [anf02:51903] "Aphrodite. He fasts in his life, in respect of covetousness and"
- Athanasius, the Festal Letter headed "Of Fasting, and Trumpets" (heading at npnf204:64550):
- [npnf204:64674] "neighbours, thereby causing great mischief. For the boast of fasting"
- [npnf204:64675] "did no good to the Pharisee, although he fasted twice in the week Luke xviii."
- [npnf204:64696] "and in what manner the law commands us to fast. It is required that not"
- [npnf204:64697] "only with the body should we fast, but with the soul. Now the soul is"
- [npnf204:64717] "acknowledgment of God. For not only does such a fast as this obtain"
- [npnf204:64718] "pardon for souls, but being kept holy, it prepares the saints, and"
- Searched for fasting "for health" or as "diet". Nothing.

Verdicts:
- "Not a diet / not for health": MODERN-CONTRAST. No source discusses dieting.
- "Not for credit": TRACED (the "boast of fasting did no good to the Pharisee").
- "Not earning merit": SOURCE-BOLDER in part. Athanasius says such a fast "obtain[s] pardon for souls" and "prepares the saints".
- "training the soul's wanting": partly TRACED (fasting of the soul, from evils, covetousness). "not crushing the hunger" is UNVERIFIED.

Recommendation: REWORD FROM SOURCE. Use Athanasius: "not only with the body should we fast, but with the soul". Use Clement: "fastings signify abstinence from all evils". Drop "Not a diet" and the Paed. II.1 citation.

### homoiosis (alx.term.homoiosis)

Record wording:
- plain_meaning: "Not a second gift - the same image, restored and grown..."
- false_friend: "becoming like God as moral imitation, copying divine conduct from outside"; "a quality already possessed that only needs noticing".
- personal: "Only the second is the likeness; the first is imitation."
- Sources: clement-stromateis II.19, 22; VII.1-3; athanasius-de-incarnatione 3-8; origen-de-principiis III.6. Relation: eikon.

What the sources say:
- The record quotes Origen III.6 itself. The line says the likeness is acquired by imitation of God.
- [anf04:31513] "at his first creation; but that the perfection of his likeness has been"
- [anf04:31514] "reserved for the consummation,—namely, that he might acquire it"
- [anf04:31515] "for himself by the exercise of his own diligence in the imitation of"
- [anf04:34790] "which are innate in the essence of God, and which may enter into man by"
- [anf04:34791] "diligence and imitation of God; as the Lord also intimates in the"
- Clement says the same:
- [anf02:33985] "likeness of God, who imitates God as far as possible, deficient in none"
- [anf02:33991] "imitating God in conferring like benefits. For God’s gifts"
- [anf02:40660] "For the gnostic must, as far as is possible, imitate God. And the poets"
- [anf02:47819] "assimilation to God the Saviour arises to the Gnostic, as far as"
- The image/likeness split (the record's informational sense) is traced to Origen:
- [anf04:31509] "expression, “In the image Imago. of God created"
- Clement II.19's title "The True Gnostic is an Imitator of God" (anf02:33982) is an EDITOR HEADING.

Verdicts:
- "Not moral imitation": SOURCE-BOLDER. Origen and Clement both say the likeness comes through "imitation of God".
- "image given, likeness grown": TRACED (Origen III.6).
- "a quality already possessed": UNVERIFIED (no source targets it).

Recommendation: REWORD FROM SOURCE. Use Origen: the likeness is "reserved for the consummation... acquire it for himself by the exercise of his own diligence in the imitation of God". Drop "the first is imitation".

### interpretation (alx.term.interpretation)

Record wording:
- plain_meaning: "Not analysis applied to a text. It is a practice of formation: meeting the Logos who speaks through Scripture."
- quick_meaning: "Not textual analysis - meeting the Logos who speaks through Scripture."
- false_friend: "expert method applied to a text to settle its meaning"; "a determination, once made, that closes the question".
- Sources: origen-de-principiis IV; clement-stromateis I, V, VI. Relation: quote no-sun-no-moon-no-sky.

What the sources say:
- Clement requires learning to read Scripture.
- [anf02:28313] "Some, who think themselves naturally gifted, do not" (Strom. I.9; the chapter title at 28311 is an EDITOR HEADING)
- [anf02:28330] "geometry, and music, and grammar, and"
- [anf02:28331] "philosophy itself, culling what is useful, he guards the faith against"
- [anf02:42348] "real philosophy and the true theology. They also wish us to require an"
- [anf02:42349] "interpreter and guide. For so they considered, that, receiving truth at"
- Origen gives methods and a rule.
- [anf04:33371] "Christ, and that they have come down to us, we must point out the ways"
- [anf04:33372] "(of interpreting them) which appear (correct) to us, who cling to the"
- [anf04:32390] "then, ought to describe in his own mind, in a threefold manner, the"
- Depth follows progress (the record's sense is TRACED here):
- [anf04:32393] "very body of Scripture; for such we term that common and historical"
- [anf04:32395] "prog­ress, and are able to see something more (than that),"
- [anf04:32396] "they may be edified by the very soul of Scripture.  Those,"

Verdicts:
- "Not analysis / not expert method": SOURCE-BOLDER. Clement and Origen both prescribe learned method and an "interpreter and guide".
- "depth received as formation allows": TRACED (Origen's body, soul, spirit).
- "closes the question": UNVERIFIED (no source targets it).

Recommendation: REWORD FROM SOURCE. Say interpretation uses learning and a guide, and reads deeper "by progress" (Origen). Drop "Not analysis".

### metanoia (alx.term.metanoia)

Record wording:
- plain_meaning: "Not feeling sorry. Metanoia - a change of nous - the soul truly turned back toward God."
- quick_meaning: "Not just feeling sorry. Metanoia is the soul truly turning back to God."
- false_friend: "feeling sorry or regretful about wrong acts"; "resolving to behave better while wanting the same things".
- Sources: clement-paidagogos I.8-9; origen-de-principiis III.1. Relation: elpis.

What the sources say:
- Clement defines repentance as knowledge or intelligence, and as ceasing to act as before.
- [anf02:32501] "“afterwards knew.” For repentance is a tardy knowledge,"
- [anf02:33165] "repentance is high intelligence. For he that repents of what he did, no"
- [anf02:33166] "longer does or says as he did. But by torturing himself for his sins,"
- [anf02:33167] "he benefits his soul. Forgiveness of sins is therefore different from"
- An editor's footnote on Hermas also glosses the Greek verb as a change of mind:
- [anf02:1323] "is thus used for a change of mind, either from evil to good, or good to" (EDITOR NOTE, not the author)
- Athanasius says repentance alone does not reach the root:
- [npnf204:16377] "repentance call men back from what is their nature—it merely"
- [npnf204:16378] "stays them from acts of sin. 4. Now, if there were merely a"

Verdicts:
- "Not just feeling sorry; a change of mind": TRACED (Clement: "tardy knowledge", "high intelligence", "no longer does... as he did"). Clement does not forbid sorrow; he praises "torturing himself for his sins".
- "a change of nous, redirecting the soul": the Greek sense is supported by the editor's note and by "afterwards knew". The word nous is not used in these lines. Athanasius says repentance "merely stays them from acts of sin", which sits against the gloss that metanoia redirects the soul's deepest direction.

Recommendation: KEEP, with Clement's words in place of "Not feeling sorry": "repentance is a tardy knowledge... high intelligence; he that repents... no longer does or says as he did".

### methexis (alx.term.methexis)

Record wording:
- plain_meaning: "Real sharing in God's own life. Not by becoming God - by becoming fully what a creature was made to be, because the Logos entered human nature."
- quick_meaning: "Real sharing in God's own life, not mere nearness to it."
- false_friend: "mere nearness to or approach toward God"; "dissolving into the divine, losing the creature's own nature".
- evidential: quotes "For He was made man that we might be made God" (De Inc. 54).
- Sources: athanasius-de-incarnatione 1-10, 54; clement-stromateis VII; athanasius-contra-arianos I.37-38.

What the sources say:
- Athanasius says "made God" (the record itself quotes it, which contradicts "Not by becoming God").
- [npnf204:18743] "been known, and its Giver and Artificer the very Word of God. 3. For He"
- [npnf204:18744] "was made man that we might be made God θεοποιηθῶμεν. See Orat. ii. 70, note 1, and many other passages"
- (The Greek and the note after "made God" are the editor's. The body sentence is "For He was made man that we might be made God".)
- [npnf204:43645] "has made us sons of the Father, and deified men by becoming Himself"
- [npnf204:43649] "God, but He was God, and then became man, and that to deify us [De Incar. 54, and note.]. Since, if when He became man, only then He"
- [npnf204:43674] "gods, whether in earth or in heaven, were adopted and deified through"
- The safeguard is "by nature" versus "by adoption/grace", not "not becoming God":
- [npnf204:43678] "157, note 6., and He alone is very God from the"
- [npnf204:43680] "nor being another beside them, but being all these by nature and"
- [npnf204:49175] "creature and work; but if we become sons by adoption and grace, then"
- [anf02:33596] "is impossible for that, which is by adoption, to be equal in substance"
- Against "mere nearness":
- [npnf204:49730] "been deified if joined to a creature, or unless the Son were very God;"
- Against "dissolving": 
- [npnf204:27512] "But as we, by receiving the Spirit, do not lose our own proper" (De Decretis, ch. III body)

Verdicts:
- "Not by becoming God": SOURCE-BOLDER. Athanasius: "made God", "deified men".
- "not mere nearness": TRACED (Athanasius: "man had not been deified if joined to a creature").
- "not dissolving, losing the creature's nature": TRACED (De Decretis: "we... do not lose our own proper" substance).

Recommendation: REWORD FROM SOURCE. Drop "Not by becoming God". Say: "made God... by adoption and grace", while the Son is God "by nature" (Contra Arianos I.39, npnf204:43680; Discourse II, npnf204:49175).

### mysterion (alx.term.mysterion)

Record wording:
- plain_meaning: "Not a puzzle waiting to be solved, but a depth known only from inside."
- quick_meaning: "Not a puzzle to solve - a depth known only from inside."
- false_friend: "an unsolved puzzle that explanation will eventually dissolve"; "a secret teaching reserved for an inner circle".
- Sources: clement-stromateis I, V; origen-de-principiis IV.

What the sources say:
- Clement says the wisdom must be hidden and not told to all.
- [anf02:28610] "for him who perceives the magnificence of the word; it is requisite,"
- [anf02:28611] "therefore, to hide in a mystery the wisdom spoken, which the Son of"
- [anf02:28636] "but not enjoining us to communicate to all"
- [anf02:42361] "it is not wished that all things should be exposed indiscriminately to all"
- [anf02:42349] "interpreter and guide. For so they considered, that, receiving truth at"
- (Chapter titles "The Mysteries of the Faith Not to Be Divulged to All" at anf02:28607 and "Reasons for Veiling the Truth in Symbols" at anf02:42338 are EDITOR HEADINGS; the body lines above are Clement's.)
- Origen rejects the charge of a "secret system", yet allows doctrines held back from the crowd:
- [anf04:36274] "unbelievers.  In these circumstances, to speak of the Christian"
- [anf04:36275] "doctrine as a secret system, is altogether absurd.  But"
- [anf04:36276] "that there should be certain doctrines, not made known to the"
- [anf04:36277] "multitude, which are (revealed) after the exoteric ones have been"
- (Contra Celsum I.7.)
- Clement on veiled meanings (closest thing to a "puzzle" in the sources; it is solved by the formed reader, not dissolved):
- [anf02:42360] "ignorant and unlearned man fails. But the Gnostior apprehends. Now, then,"
- Searched for "puzzle" or "riddle" language as a charge or a contrast. None.

Verdicts:
- "Not a secret teaching reserved for an inner circle": SOURCE-BOLDER. Clement says to "hide in a mystery" and not "communicate to all". Origen denies a "secret system" but keeps unrevealed doctrines for those taught later.
- "Not a puzzle waiting to be solved": MODERN-CONTRAST. No source uses the puzzle image either way.

Recommendation: REWORD FROM SOURCE. Say the mystery is veiled and given to those ready ("not... exposed indiscriminately to all and sundry"; Origen: some doctrines "not made known to the multitude"). Drop "not a secret teaching".

### oikos (alx.term.oikos)

Record wording:
- plain_meaning: "Not the private family. The oikos is the whole household, where most people were formed."
- quick_meaning: "Not a private family. The household where most formation happened."
- false_friend: "the modern nuclear family in a private home"; "a sphere kept separate from the community's formation life".
- informational: "sometimes fifteen to forty people"; formation happened there "far more than the school or even the weekly Eucharist".
- Sources: clement-paidagogos II-III. No relations.

What the sources say:
- Clement addresses masters and servants together.
- [anf02:26793] "good-will from the soul doing service. ye masters, treat your servants"
- [anf02:25285] "therefore, they ought to regard with modesty parents and domestics; in"
- [anf02:24736] "and very opulent; and so with three hundred and eighteen servants of"
- Searched Clement, Origen, Athanasius for household size ("fifteen", "forty"), for the household as the main place of formation, and for a comparison with the school or Eucharist. Not found.

Verdicts:
- "Not the modern nuclear family": MODERN-CONTRAST. It answers a modern idea.
- "household includes servants and dependents": TRACED in spirit (Paed. III).
- "fifteen to forty people" and "where most formation happened, more than school or Eucharist": UNVERIFIED (scholars' reconstruction, not in the vendored texts).

Recommendation: REWORD FROM SOURCE. Say Clement speaks to "masters" and "servants" and to "domestics" in the same home. Drop the numbers and the comparison.

### pistis (alx.term.pistis)

Record wording:
- plain_meaning: "Not agreeing with a list of claims, but the soul's first real turn toward God."
- quick_meaning: "Not agreeing with claims - the soul's first real turn toward God."
- false_friend: "intellectual assent to a list of doctrines"; "certainty with no unresolved questions".
- Sources: clement-stromateis II.2-6; origen-contra-celsum I.9-13.

What the sources say:
- Clement defines faith as assent.
- [anf02:32062] "But faith, which the Greeks disparage, deeming it futile and"
- [anf02:32063] "barbarous, is a voluntary preconception, Or anticipation, πρόληψις."
- [anf02:32064] "the assent of piety—“the subject of things hoped for,"
- [anf02:32069] "2, 6. Others have defined faith to be a uniting assent to an"
- [anf02:32059] "“Except ye believe, neither shall ye understand.” Isa. vii. 9."
- Origen defends believing without full reasons:
- [anf04:36367] "wallowed, whether it were better for them to believe without a reason,"
- [anf04:36368] "and (so) to have become reformed and improved in their habits, through"
- (Chapter title "Faith the Foundation of All Knowledge", anf02:32146, is an EDITOR HEADING.)
- Searched for faith with "no unresolved questions". Nothing.

Verdicts:
- "Not agreeing with claims / not intellectual assent": SOURCE-BOLDER. Clement: faith is "the assent of piety", "a uniting assent". Origen: believing "without a reason" reforms the many.
- "foundation that gnosis builds on": TRACED in spirit ("Except ye believe, neither shall ye understand").
- "certainty with no unresolved questions": UNVERIFIED.

Recommendation: REWORD FROM SOURCE. Use Clement's "the assent of piety". Drop "Not agreeing with claims".

### pneuma-hagion (alx.term.pneuma-hagion)

Record wording:
- plain_meaning: "Not an occasional visitor, but the one always at work in Scripture, prayer, and the soul's own change."
- quick_meaning: "Not an occasional visitor - always at work in the soul's own change."
- false_friend: "a presence that visits only in extraordinary moments"; "a vague feeling of inspiration or community energy".
- informational: "The Spirit does not arrive for special occasions and then leave."
- Sources: clement-stromateis IV, VI, VII; origen-de-principiis I.3.

What the sources say:
- Origen limits the Spirit's share to saints and says it can leave.
- [anf04:23759] "distinction to every creature; but a share in the Holy Spirit we find"
- [anf04:23760] "possessed only by the saints.  And therefore it is said, “No"
- [anf04:23761] "man can say that Jesus is Lord, but by the Holy Ghost.” 1 Cor. xii. 3.  And on one occasion, scarcely even the"
- [anf04:23762] "apostles themselves are deemed worthy to hear the words, “Ye"
- [anf04:23732] "“My Spirit shall not abide with those men for ever, because they"
- [anf04:22560] "spiritual meaning which the law conveys is not known to all, but to"
- [anf04:22561] "those only on whom the grace of the Holy Spirit is bestowed in the word"
- [anf04:34552] "by participation in the Holy Spirit is a man rendered holy and"
- Searched Clement (IV, VI, VII) for the Spirit as "continuous" or "ordinary" agent. No such claim.

Verdicts:
- "Not an occasional visitor, always at work": SOURCE-CONTRARY. Origen: "a share in the Holy Spirit we find possessed only by the saints"; the Spirit "shall not abide with those men for ever". The gloss is bolder than the source.
- "a vague feeling of inspiration or community energy": MODERN-CONTRAST (no source discusses it).

Recommendation: REWORD FROM SOURCE. Use Origen: the Spirit's share is "possessed only by the saints"; by it "a man [is] rendered holy and spiritual". Drop "Not an occasional visitor".

### prayer (alx.term.prayer)

Record wording:
- plain_meaning: "Not mainly speaking to God. The soul turning to attend to what God is already saying."
- quick_meaning: "Not mainly speaking to God - the soul turning to attend to what God is already saying."
- false_friend: "verbal speech aimed at a divine listener, as the whole of what prayer is"; "clearing the mind into a blank, contentless openness".
- informational: "Prayer is not opening a channel that was otherwise silent".
- Sources: clement-stromateis VII.7, 12. Relation: fasting.

What the sources say:
- Clement's own definition is speech to God, even when silent.
- [anf02:50824] "Prayer is, then, to speak more boldly, converse"
- [anf02:50825] "with God. Though whispering, consequently, and not opening the lips,"
- [anf02:50826] "we speak in silence, yet we cry inwardly. [1 Sam. i. 13. See this same"
- [anf02:50827] "chapter, infra, p. 535.] For God hears continually"
- [anf02:51819] "His whole life is prayer and converse with God."
- Searched Clement, Origen, Athanasius for "God is already addressing the soul" as the meaning of prayer. Not found.
- Searched for prayer as clearing the mind into blank openness. Not found.

Verdicts:
- "Not mainly speaking to God": SOURCE-BOLDER. Clement: "Prayer is... converse with God" and "we speak in silence".
- "attending to what God is already saying": UNVERIFIED.
- "blank openness": MODERN-CONTRAST (no source discusses it).

Recommendation: REWORD FROM SOURCE. Use Clement: "Prayer is... converse with God", also "in silence", and "His whole life is prayer and converse with God". Drop "Not mainly speaking".

### psyche (alx.term.psyche)

Record wording:
- plain_meaning: "Not a ghost living inside a body. The whole human person, made for God - alive through the body, not caged in it..."
- quick_meaning: "...not a spirit trapped inside it."
- false_friend: "an inner spirit lodged in flesh, waiting to be freed from a material prison"; "a poetic word for mind or character with no real referent".
- translational: "this world refused that picture directly. The soul is not caged in the body".
- Sources: clement-paidagogos I; athanasius-de-incarnatione 3-8. Relations: eikon, nous.

What the sources say:
- Clement speaks of the flesh as a chain and of being fettered in it.
- [anf02:50833] "intellectual essence; and endeavouring to abstract the body from the"
- [anf02:50834] "earth, along with the discourse, raising the soul aloft, winged with"
- [anf02:50836] "holiness, magnanimously despising the chain of the flesh. For we know"
- [anf02:33509] "fettered in the flesh were able to listen, so the prophets spake to us;"
- Searched Paed. I and De Incarnatione 3-8 for a line on the soul acting "through the body" as its instrument. Not found. The Genesis 2:7 "breath of life" claim is not in De Incarnatione 3-8 (searched "breath of life", "breathed"): UNVERIFIED.

Verdicts:
- "Not caged in the body / not a spirit trapped inside": SOURCE-BOLDER. Clement: "despising the chain of the flesh"; "we who are fettered in the flesh". (Clement elsewhere honors the body; but the gloss denies his own image.)
- "poetic word with no referent": UNVERIFIED (no source targets it).

Recommendation: REWORD FROM SOURCE. Drop "not caged". If kept, give both: Clement's "chain of the flesh" and his care for body and soul together.

### salvation (alx.term.salvation)

Record wording:
- plain_meaning: "Not a not-guilty verdict, but healing - the soul's own direction turned back toward God."
- quick_meaning: "Not a verdict of not-guilty - the soul's direction healed and turned back to God."
- false_friend: "acquittal, a not-guilty verdict from a judge"; "a legal record wiped clean".
- evidential: "Athanasius describes the Logos entering human nature to reverse it from within, not to settle a legal claim".
- Sources: athanasius-de-incarnatione (whole); clement-paidagogos I.

What the sources say:
- Athanasius states the legal claim and the debt in plain words.
- [npnf204:16309] "above, gained from that time forth a legal Gen. ii. 15. hold"
- [npnf204:16310] "over us, and it was impossible to evade the law, since it had been laid"
- [npnf204:16374] "repentance would, firstly, fail to guard the just claim See"
- [npnf204:16469] "satisfied the debt by His death. And thus He, the incorruptible Son of"
- [npnf204:16995] "Life, none teach, but the Word. And He, to pay our debt of death, must"
- He also describes corruption of nature, which fits "healing":
- [npnf204:16377] "repentance call men back from what is their nature—it merely"
- Clement's physician image (the healing side):
- [anf02:18797] "creature; the all-sufficient Physician of humanity, the Saviour, heals"
- (The §7 summary at npnf204:16349-16356 is the EDITOR'S summary; it is not quoted above.)

Verdicts:
- "not to settle a legal claim / not a verdict": SOURCE-BOLDER. Athanasius names a "legal hold", "the just claim of God", "the debt", and says Christ "satisfied the debt by His death". The gloss denies what he says.
- "healing": TRACED (Clement's Physician; Athanasius on corruption). Athanasius holds both the debt and the corruption.

Recommendation: REWORD FROM SOURCE. Keep both parts in Athanasius's words: the debt is paid ("satisfied the debt by His death") and nature is renewed. Drop "not to settle a legal claim" and "Not a not-guilty verdict".

### son-of-god (alx.term.son-of-god)

Record wording:
- plain_meaning: "Not an honor for being close to God. Nicaea's own claim - the Son is genuinely God, not the highest thing God made."
- quick_meaning: "Not an honor for closeness to God - Nicaea's claim that the Son is genuinely God."
- false_friend: "an honorific for someone unusually holy or favored"; "the highest creature God made, closer to God than any other".
- evidential: "Origen's earlier language about the Son as Image of the Father was itself one of the questions Nicaea later settled."
- Sources: athanasius-contra-arianos I-III; de-incarnatione 1-10; origen-de-principiis I.2; nicene-creed-325 line 2412.

What the sources say:
- Creed:
- [npnf214:2412] "not made, being of one substance (ὁμοούσιον,"
- [npnf214:2424] "Father] or that he is a creature, or subject to change or"
- The Arian formula, in Athanasius's own report:
- [npnf204:46731] "heresy was in course of formation. They wrote thus: ‘He is a"
- [npnf204:46732] "creature, but not as one of the creatures; a work, but not as one of"
- Athanasius against "honor":
- [npnf204:43680] "nor being another beside them, but being all these by nature and"
- [npnf204:43650] "was called Son and God, but before He became man, God called the"
- Origen:
- [anf04:23147] "breath of life that He is made a Son, by"
- [anf04:23148] "any outward act, but by His own nature."
- Searched for any vendored line saying Nicaea settled Origen's "Image" language. Not found (a later scholars' view).

Verdicts:
- "Not an honor for closeness to God": TRACED (Athanasius: others were "called sons" and "gods"; the Son is "by nature").
- "not the highest creature": TRACED (the Arian "creature, but not as one of the creatures"; the creed anathema on "creature").
- "Origen's language was a question Nicaea settled": UNVERIFIED. Origen himself says "by His own nature".

Recommendation: KEEP the main gloss. Drop the Origen sentence in `evidential`.

### sophia (alx.term.sophia)

Record wording:
- plain_meaning: "What a lifetime of formation grows in a soul. Not knowledge held in the mind - a change seen in how a person perceives, loves, and lives."
- quick_meaning: "What formation grows in a soul, seen in how it loves and lives."
- false_friend: "accumulated practical experience or age"; "theoretical mastery of ultimate questions".
- informational: "Wisdom cannot be acquired, only grown".
- Sources: clement-stromateis VI-VII; clement-protrepticus (whole).

What the sources say:
- Clement defines wisdom as knowledge and speaks of acquiring it.
- [anf02:27952] "mistress; so also philosophy itself co-operates for the acquisition of"
- [anf02:27953] "wisdom. For philosophy is the study of wisdom, and wisdom is the knowledge"
- [anf02:27954] "of things divine and human; and their causes.” Wisdom is therefore"
- [anf02:48572] "For perfect wisdom, which is knowledge of things divine and human,"
- [anf02:40521] "and logically occupies himself with God. For wisdom is the knowledge of"
- [anf02:48342] "said that practical wisdom is divine knowledge, and exists in those who"
- [anf02:48343] "are deified; but that self-control is mortal, and subsists in those who"
- Clement also says wisdom is God-given:
- [anf02:43030] "whom it is found.” Wisdom which is God-given, as being the power"

Verdicts:
- "Not knowledge held in the mind": SOURCE-BOLDER. Clement's definition, three times, is "knowledge of things divine and human".
- "cannot be acquired, only grown": contradicted in part ("acquisition of wisdom"), supported in part ("Wisdom which is God-given").
- "accumulated practical experience or age": UNVERIFIED.

Recommendation: REWORD FROM SOURCE. Use "wisdom is the knowledge of things divine and human; and their causes". Add that it is "God-given". Drop "Not knowledge held in the mind".

### theosis (alx.term.theosis)

Record wording:
- plain_meaning: "Becoming like God: sharing in God's own life, as far as a creature can. Not becoming a god."
- false_friend: "becoming a god (polytheism)"; "losing your self in God".
- Sources: athanasius-de-incarnatione 54. Relations: gravity soul-transformation; quote athanasius-made-god.
- Also (outside the term file): demonstration alx.demo.who-was-jesus: "Not that we become gods - but that his own life is opened to us and shared."

What the sources say:
- Athanasius, De Incarnatione 54 (the record's own cited line):
- [npnf204:18743] "been known, and its Giver and Artificer the very Word of God. 3. For He"
- [npnf204:18744] "was made man that we might be made God θεοποιηθῶμεν. See Orat. ii. 70, note 1, and many other passages"
- Athanasius, Against the Arians:
- [npnf204:43645] "has made us sons of the Father, and deified men by becoming Himself"
- [npnf204:43674] "gods, whether in earth or in heaven, were adopted and deified through"
- [npnf204:49175] "creature and work; but if we become sons by adoption and grace, then"
- [npnf204:49736] "deified, unless the Word who became flesh had been by nature from the"
- Clement:
- [anf02:15351] "that thou mayest learn from man how man may become God. Is it not then"
- [anf02:18339] "great, divine, and inalienable inheritance of the Father, deifying man"
- [anf02:19294] "immortal. “I,” says He, “have said that ye are gods, and"
- [anf02:19295] "all sons of the Highest.”"
- [anf02:21070] "life according to which we have been deified, let us anoint ourselves"
- [anf02:40661] "call the elect in their pages godlike and gods, and equal to the gods," (said of the poets' phrase; Clement ties it to "image and likeness")
- The only safeguard in the sources is "by nature" versus "by adoption":
- [anf02:33595] "vi. 40. not in essence (for it"
- [anf02:33596] "is impossible for that, which is by adoption, to be equal in substance"
- (Strom. II.17. The chapter title "On the Various Kinds of Knowledge" is an EDITOR HEADING.)
- [npnf204:43680] "nor being another beside them, but being all these by nature and"
- Not used as evidence: any editor note or chapter summary (for example the editor's "Word 'deifies' Human Nature" notes). Only body sentences are quoted.

Verdicts:
- "Not becoming a god": SOURCE-BOLDER. Clement: "how man may become God"; "ye are gods"; "we have been deified". Athanasius: "made God", "deified". The only limit in the sources is nature versus adoption and grace.
- "losing your self in God": MODERN-CONTRAST (no source discusses it).
- "(polytheism)": MODERN-CONTRAST. Athanasius's own Contra Gentes attacks polytheism, but never as an objection to being made God.

Recommendation: REWORD FROM SOURCE. Use "made man that we might be made God" and "become sons by adoption and grace"; Clement: "how man may become God". Say the Son is God "by nature" and we by grace.

### transformation (alx.term.transformation)

Record wording:
- plain_meaning: "The soul reoriented by contact with God, down at the level of what it wants. Not self-improvement. Not better behavior with the same old direction."
- quick_meaning: "The soul reordered by contact with God, not self-improvement."
- false_friend: "self-help or personal development"; "better behavior without a changed direction".
- Sources: clement-stromateis I, IV, VII; athanasius-de-incarnatione 14-20.

What the sources say:
- Athanasius: renewal is God's work, not repentance or effort:
- [npnf204:16377] "repentance call men back from what is their nature—it merely"
- [npnf204:16378] "stays them from acts of sin. 4. Now, if there were merely a"
- [npnf204:16384] "recall, but the Word of God, which had also at the beginning made"
- Clement: same act, different kind, by fear or by love:
- [anf02:39568] "The same work, then, presents a difference,"
- [anf02:39569] "according as it is done by fear, or accomplished by love, and is"
- Clement: God-given, yet it rouses free will:
- [anf02:43030] "whom it is found.” Wisdom which is God-given, as being the power"
- [anf02:43031] "of the Father, rouses indeed our free-will, and admits faith, and repays"
- Antony:
- [npnf204:31747] ".” Wherefore virtue hath need at our hands of willingness alone,"

Verdicts:
- "Not self-improvement": TRACED in substance (source of change is God; the soul's will is roused, not replaced).
- "Not better behavior with the same old direction": TRACED (Clement IV.18, "the same work... by fear... or by love").
- "self-help or personal development": MODERN-CONTRAST (names a modern genre).

Recommendation: KEEP. Optionally add that the will is "roused" (Clement) and that Antony says virtue needs "willingness".

### word-of-god (alx.term.word-of-god)

Record wording:
- plain_meaning: "Not first a name for the Bible. The eternal Word who speaks - who made everything, and now speaks to the soul through Scripture too."
- quick_meaning: "Not a name for the Bible - the eternal Word who speaks, including through Scripture."
- false_friend: "a synonym for the Bible"; "an ancient document with religious authority".
- Sources: clement-protrepticus I, VI; origen-comm-john I-II; athanasius-de-incarnatione 1-5. Relations: christ, son-of-god.

What the sources say:
- Clement, Protrepticus I:
- [anf02:15350] "to thee, shaming thy unbelief; yea, I say, the Word of God became man,"
- [anf02:15351] "that thou mayest learn from man how man may become God. Is it not then"
- Origen, Commentary on John I (the heading at anf09:21316-21318, "The Word of God is Not a Mere Attribute of God, But a Separate Person", is an EDITOR HEADING):
- [anf09:21470] "being a separate entity from the Father, and accordingly as it, having"
- [anf09:21472] "the Word is a separate being and has an essence of His own.  We"
- Athanasius:
- [npnf204:18743] "been known, and its Giver and Artificer the very Word of God. 3. For He"
- Searched for any vendored line that says "the Word of God" is not the Bible, or that the "person, not the page" gives Scripture its power. Not found.

Verdicts:
- "the eternal Word who speaks, a person": TRACED (Clement, Origen, Athanasius).
- "Not a name for the Bible / not an ancient document with authority": MODERN-CONTRAST. It answers a modern equation of Word and Bible. No source argues it.
- "the person, not the page, gives Scripture its power": UNVERIFIED.

Recommendation: KEEP the person-of-the-Word core in the sources' words ("the Word of God became man"; "a separate being and has an essence of His own"). Drop "Not a name for the Bible".

## Unsure (for the caller)

- ekklesia: the "catechumen is more fully inside" line has no source either way. I rated it UNVERIFIED, not contradicted.
- episkopos: the Clement line about the "true presbyter" is not about bishops. I could not tell whether the record reads it too strongly. The Athanasius grain letter is a third-party letter inside the Apologia, not his own definition.
- fasting: the cited Paed. II.1 has no fasting text. Athanasius's "obtain pardon for souls" may or may not count as "earning merit".
- metanoia: Clement fits the gloss, but Athanasius (De Inc. 7) says repentance "merely stays them from acts of sin". These point different ways on how deep repentance goes.
- pneuma-hagion: I used an extra label, SOURCE-CONTRARY. The gloss is bolder than Origen. Clement IV/VI/VII were searched only by keyword.
- word-of-god: the Origen line is an argument against a mere "attribute" reading. Whether it also supports the "not the Bible" gloss is not shown.
