# Rendering Review: syr quote records, batch 2 (17 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 17 `syr.quote` records.

## Method

Each record's `text` is compared with the vendored edition in `cic/texts/` at its locus. Where a record gives no file, the passage is found by grepping a distinctive phrase in the file that carries the work. For the XML files, `<note>` elements and tags are stripped. Line-end hyphens are rejoined, and whitespace (including U+00A0) is folded before the exact-substring test. The line span runs from the line holding the quote's first word to the line holding its last word. Edition apparatus that the record's `divergence_note` says is not reproduced (Mitchell's page marker, Hallock's footnote marker `~1~`) is treated as apparatus, not as text.

Each rendering is read clause by clause against the edition text and the surrounding lines. It is also checked against `confidence.divergence_note` and `use_note.not_for`. Sentence lengths are counted by script: split at `.`, `!` or `?`, then count word tokens, with dashes not counted as words. Translators' bracketed or parenthetical supplements are checked under the bracket rule. A supplement that adds meaning must stay bracketed or be left out; a purely grammatical one may be rendered plainly. Reported speech is checked to stay inside its frame.

Sources read: `npnf213_gregory-great-ephraim-syrus-aphrahat.xml`, `npnf202_socrates-sozomen-ecclesiastical-histories.xml`, `npnf203_theodoret-jerome-gennadius-rufinus.xml`, `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, `palladius_lausiac-history_clarke1918.txt`, `ephraim_prose-refutations_mitchell1912-1921.txt`, `chronicle-of-edessa_cowper.txt`, `aphrahat_demonstrations-2-7_hallock1932.txt`.

## Results

**17 records: 11 PASS, 6 FAIL (1 P1, 5 P2).**

| Record id (syr.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| ephrem-resurrection-pledge | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 22311-22314 | pass | all clauses; "would" keeps both clauses inside the pledge; "bring them to" supplies the verb the edition implies; longest 13 | PASS |
| nativity-this-is-the-day | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 17530-17533 | pass (small-caps "This" is markup only) | all clauses; "fulfilled ... performed" becomes "came true - all of them"; longest 14 | PASS |
| nisibene-death-trembled | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 15642-15644 | pass | all clauses; the elliptical "and Satan" kept as "Satan, too"; longest 8 | PASS |
| on-a-certain-day-a-pearl | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 21794-21801 | pass | all clauses, but sentence 2 joins the "saw" and "fountain" thoughts in 27 words | FAIL P2 |
| palladius-hospitaller | cic/texts/palladius_lausiac-history_clarke1918.txt, line 471 | pass | "on your behalf I appoint myself" kept; "hospitaller" glossed by its function, which the next sentence of the chapter describes; no office implied; longest 15 | PASS |
| pearl-mysteries | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 21794-21797 | pass | all clauses; "semblances and types" as "pictures and signs"; longest 15 | PASS |
| permitted-to-erect-churches | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 19172-19176 | pass | all clauses; "decimated" rendered in its exact sense (one in ten put to death); the king's grant kept; longest 23 | PASS |
| sozomen-melodies | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 32088-32090 | pass | "exact copies of Harmonius's versions" adds a sense the edition lacks | FAIL P2 |
| symeon-and-usthazanes | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 28873-28877 | pass | all clauses; the Magi relative clause split cleanly; visible organisation stays the provocation; longest 15 | PASS |
| tatian-barbaric-writings | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 6970-6978 | pass (the edition has lower-case "retiring" after a dash mid-sentence; the record capitalises the first word of the excerpt; footnote 498 stripped) | sentence 2 runs to 36 words; "Retiring" misleads in its modern sense | FAIL P2 |
| tatian-born-assyrian | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 7457-7464 | pass | all clauses; "barbarian philosophy" kept as Tatian's own self-description; longest 15 | PASS |
| the-blasphemy-of-madmen | cic/texts/ephraim_prose-refutations_mitchell1912-1921.txt, line 358 | pass (the page marker "[Ov. p. 53, l. 2.]" falls inside the run; it is apparatus and the divergence note declares it) | the final sentence runs to 30 words | FAIL P2 |
| the-scribes-and-the-prefects-over-the-archives | cic/texts/chronicle-of-edessa_cowper.txt, line 59 | pass | Cowper's gloss "(i.e., archivists.)" is voiced as the Chronicle's own words ("that is, as archivists") | FAIL P2 |
| the-temple-of-the-church-of-the-christians | cic/texts/chronicle-of-edessa_cowper.txt, line 53 | pass | all clauses; "more than two thousand" kept exactly; "lamentation" as "mourning"; longest 17 | PASS |
| the-wedding-feast-continues-for-but-seven-days | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 25940-25947 | pass | all clauses; "(virgins)" is a referential supplement that names who "these" are, as the context already shows, so rendering it plainly adds no meaning; each antithesis is one thought; longest 24 | PASS |
| theodoret-gnats | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 11174-11175 | pass | all clauses; "on them" only restates the "darts of his curse" at the barbarians in the line before; length 18 | PASS |
| warned-before-baptism | cic/texts/aphrahat_demonstrations-2-7_hallock1932.txt, line 57 | pass (Hallock's footnote marker "~1~" between "God" and "before" is apparatus and the divergence note declares it) | Hallock's meaning-adding supplements "(wishing to. become)" and "(i.e.~in matrimony)" are voiced as Aphrahat's own; the preachers' quoted warning loses its quotation frame; one sentence runs to 27 words | FAIL P1 |

## Failed renderings: corrected text

### on-a-certain-day-a-pearl

Sentence 2 ("In it I saw mysteries ... mysteries of the Son.") joins two thoughts with a semicolon and runs to 27 words. Splitting it at the semicolon fixes both problems; nothing else needs to change.

Corrected rendering:

> One day, my brothers, I picked up a pearl. In it I saw mysteries of the Kingdom, images and symbols of the Majesty. It became a fountain, and from it I drank mysteries of the Son. I set it, my brothers, on the palm of my hand so I could examine it. I went to look at it from one side, and it showed faces on every side. I discovered that the Son cannot be fully grasped, since he is wholly Light.

### sozomen-melodies

The edition says the Syrians sing "not the precise copies by Harmonius" (his own compositions) "but the same melodies." "Exact copies of Harmonius's versions" adds a layer the edition lacks: it suggests that Harmonius made versions of something else.

Corrected rendering:

> Even now the Syrians often sing, not the exact pieces Harmonius wrote, but the same melodies.

### tatian-barbaric-writings

Sentence 2 runs to 36 words. "Retiring by myself" reads to a modern reader as leaving work; the edition means withdrawing into solitude.

Corrected rendering:

> Withdrawing by myself, I tried to find out how I might discover the truth. I was giving the matter my most earnest attention. Then I happened to come across certain non-Greek writings. They were too old to be compared with the opinions of the Greeks, and too divine to be compared with their errors. Several things led me to put faith in these writings. The language was plain and unpretending. The writers were artless. They showed foreknowledge of future events. Their precepts were excellent. And they declared that the government of the universe is centred in one Being.

### the-blasphemy-of-madmen

The last sentence ("You cannot bring a man back ... into the wild.") runs to 30 words. Split it, and keep the edition's condition ("unless one goes a little from the way after him").

Corrected rendering:

> We are not daring to blaspheme the Good One. We say this so that the blasphemy of madmen may perhaps be refuted by what sounds like blasphemy, though it is not. For you cannot bring a man back to the road while he walks off it. To do that, you must go a little off the road after him, into the wilderness.

### the-scribes-and-the-prefects-over-the-archives

"(i.e., archivists.)" is Cowper's gloss on the Syriac phrase "trusted of the city". The rendering voices it as the Chronicle's own ("that is, as archivists"), and adds "officers". The gloss largely repeats "prefects over the archives", so little meaning changes. Even so, the bracket rule requires the gloss to stay marked as the translator's.

Corrected rendering:

> Mar Yahab Bar Shemesh and Kajuma Bar Magartat were the scribes of Edessa. They recorded this event, and the command of king Abgar. Bar Din and Bulid were the prefects over the archives of Edessa. They received the record and placed it in the archives, as the trusted men of the city [that is, archivists].

### warned-before-baptism

Hallock's supplements "(wishing to. become)" and "(i.e.~in matrimony)" add meaning: the first says these people are not yet holy, and the second names the "natural state of fellowship". The rendering voices both as Aphrahat's own and drops "natural state of fellowship". The preachers' warning is quoted speech in the edition. Rendered without quotation marks and recast as "you", it reads as Aphrahat's own direct address. "Turn back now" adds "now". The 27-word sentence ("And if you are afraid ... along with your own.") is over length.

Corrected rendering:

> For this reason the preachers of the Church, who sound the trumpets, should warn everyone in God's covenant before baptism. They should also warn those who choose virginity and holiness for themselves: young men, virgins, and those [wishing to become] holy. The preachers are to warn them and say: "Whoever has set his heart on the natural state of fellowship [that is, marriage] should marry before baptism. Otherwise, perhaps, he may fall in the fight and be killed. Whoever is afraid of this part of the struggle should turn back. Otherwise, perhaps, he may break his brothers' hearts as well as his own. Whoever loves possessions should turn back from the army. Otherwise, perhaps, when the battle goes against him, he may remember his possessions and turn back to them. For there is disgrace for the one who turns back from the fight."
