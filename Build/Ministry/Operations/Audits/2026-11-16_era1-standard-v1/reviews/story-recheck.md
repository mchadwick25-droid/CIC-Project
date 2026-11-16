# Era 1, Standard v1: story recheck (checklist items 19 and 20)

Independent Opus reviewer, 2026-11-16. Targeted recheck ordered by Mark, outside the three-round cap. Range d5590b4f..b438d4de, the briefs under `Who-Profiles/era1/` and `Council-Profiles/era1/` and their cards. Only changed sentences were checked: against the references record's two ruling sections, the held lines in `cic/texts/`, and `renderings/comparison.md` FINAL. No model calls; no other file changed.

Readability: `python3 -m engine.m1.profile_readability --report` on all 21 briefs: 21 graded, 0 failing. No brief grew; every changed brief is shorter or the same length (word counts at d5590b4f against b438d4de).

| Brief | Result |
|---|---|
| anatolius-of-alexandria-and-laodicea | CLEARS |
| bardaisan-of-edessa | CLEARS |
| clement-of-alexandria | Finding C1 (a sentence that does not read clearly) |
| councils-of-rome-and-carthage-251 | CLEARS |
| dionysius-of-alexandria | CLEARS |
| eusebius-of-caesarea | CLEARS |
| hermas | Finding H1 (a hostile witness's claim now reads as fact) |
| hippolytus-of-rome | CLEARS |
| ignatius-of-antioch | CLEARS |
| josephus | Finding J1 (the card needs the Jerome caveat) |
| justin-martyr | CLEARS |
| marcion-of-pontus | CLEARS |
| novatian | CLEARS |
| peter-of-alexandria | CLEARS (unchanged in range) |
| pliny-the-younger | CLEARS |
| polycrates-of-ephesus | CLEARS |
| pontius-the-deacon | CLEARS |
| suetonius | CLEARS (unchanged in range) |
| tacitus | CLEARS |
| tatian | CLEARS (wording note N2) |
| valentinus | CLEARS |

## Checks that passed across the set

- **Joined quotations.** Eusebius ("Since I am the first ... untrodden road."), Polycrates ("We keep the day ... taking nothing away."), Clement, Valentinus and Ignatius (Smyrnaeans) each now carry one span. Each one equals its FINAL string (E37, E19, E30, E28, E16) word for word once the FINAL's "he wrote" is left out.
- **Kept quotations.** Every other kept quotation equals its FINAL, apart from the two joined forms the renderings README already sanctions (E15 Ignatius, E34 Pontius).
- **Dropped quotations.** Each card's `quotationOriginals` lost exactly the quotations that the brief now tells plainly: Clement E29; Ignatius E14 and E17; Josephus E1, E4 and E5; Justin E21; Marcion E26 and E27; Pliny E12 and E13. The halves still on the cards for the five joined spans join up to exactly the brief's span (see N1).
- **Quotation limit.** No brief keeps more than two quotations.
- **Narration from former quotations.** I opened the held lines. None of the narrated versions says more or less than its source:
  - Clement, Stromata I.1: anf02 27489-27492.
  - Ignatius, Romans 5 and Smyrnaeans 8: anf01 7087 and 8277-8278.
  - Josephus, Antiquities XX.9.1; Origen; Jerome: Whiston 91005-91009, anf09 30628, npnf203 39729.
  - Justin: Martyrdom 2, anf01 29312-29313; Irenaeus IV.6.2, anf01 28894-28895, where "the Creator" stands for "the Fashioner and Maker [of the world]".
  - Marcion, First Apology 26: anf01 14944-14946.
  - Pliny: Trajan's reply, npnf201 19526-19527; Tertullian, Apology 2, anf03 1585-1586, where "a contradiction" matches "a self-contradiction".
  - Tatian: Clement, A2 29724-29727, "discussed with accuracy"; Eusebius, npnf201 26185-26186, "It is said that Tatian was the author".
  - Clement: Alexander's letter, npnf201 33612-33617.
- **Partisan witnesses placed once.** The cut tags in these briefs all follow a witness who is already named, with his leaning, earlier in the same run:
  - Novatian: Cornelius "tells it as an enemy".
  - Hippolytus: the Refutation is "an enemy's account".
  - Pontius: "He writes as an admirer".
  - Tacitus: the chapter "treats them as criminals".
  - Council: "reaches us from Cyprian, who called the meeting and defended it afterward".
  - Bardaisan: Epiphanius named in the sentence before.
  - Pliny: "comes from them".

  This is the "named once" form that item 19 allows.

## Findings

### C1. clement-of-alexandria: one sentence uses "him" for two different men

File `Who-Profiles/era1/batch1/clement-of-alexandria.brief.txt`, line 9:

> From prison he sent a letter to Antioch by Clement's hand, praising him for having strengthened and built up the church while Clement was with him.

The first "him" is Clement and the second is Alexander, so a listener cannot tell who praised whom. The claim itself traces correctly: npnf201 33612-33617 ("by Clement, the blessed presbyter, a man virtuous and approved ... Being here ... he has strengthened and built up the Church of the Lord"). This fails item 3, because the closing sentence does not read clearly.

Accepted fix, exact wording:

> From prison he sent a letter to Antioch by Clement's hand. In it he praised Clement for strengthening and building up the church during his stay.

Checked on a scratch copy: 292 words, grade 9.0 (names out 7.3), reading ease names out 71.9, pass.

### H1. hermas: Tertullian's claim about the councils now reads as the narrator's

File `Who-Profiles/era1/batch1/hermas.brief.txt`, line 7:

> Tertullian of Carthage, attacking a bishop who forgave adulterers, called it the one writing that favored them, a book the councils of the churches had judged false.

The claim that councils of the churches judged the Shepherd false rests on Tertullian alone: anf04 8141-8144, "if it had not been habitually judged by every council of Churches (even of your own) among apocryphal and false (writings)". Tertullian is also a hostile witness, writing a polemic. When the claim follows "called it" as an appositive, the listener hears the narrator stating it as fact. The cut tag "and said" carried trust: the claim rests on one source, and that source is hostile. Restoring it is not a synonym swap.

Accepted fix, exact wording:

> Tertullian of Carthage, attacking a bishop who forgave adulterers, called it the one writing that favored them, and said the councils of the churches had judged it false.

Checked on a scratch copy: 355 words, which is still below the 360 at d5590b4f; grade 8.5, pass. The refs record's "Mark's ruling: tell the story" section should then list "and said" under Kept, as a claim resting on one hostile witness.

### J1. josephus: the card still needs the caveat that Jerome's Latin is not held

The brief now tells Jerome's version plainly: "but in his version Jesus was believed to be the Christ." It then concludes: "So neither Origen nor Jerome read that line as our copies give it." For Jerome, that conclusion rests on one word ("believed") in E. C. Richardson's English, npnf203 39729, and Jerome's Latin is not held.

Dropping the quotation removed the `quotationOriginals` object that carried this caveat. The claim stayed, and so did the reason for the caveat. The card's legacy line says "in E. C. Richardson's English", but nothing on the card says the original is unchecked. The Origen caveat ("our Jesus") survives in the What is uncertain list. The Jerome caveat should sit there too.

Accepted fix: in `Who-Profiles/era1/batch1/josephus.card.json`, line 35, the first `uncertain` entry, insert this sentence after "So at least that line was not read as our copies give it.":

> Jerome's Latin is not held, so his version of the line rests on E. C. Richardson's English alone.

## Non-blocking notes

- **N1. Split halves on the cards.** The cards for Clement, Eusebius, Ignatius (Smyrnaeans), Valentinus and Polycrates still hold the quotation the brief now joins as two `quotationOriginals` objects. The two halves join up to exactly the brief's span. For Polycrates the split also carries something real: one clause's Greek is held and the other's is not. That makes it acceptable as it stands. If the card view shows each object as a separate quotation, merge each pair into one object.
- **N2. tatian, line 9.** "Irenaeus traced it to earlier teachers, but for Eusebius, Tatian was said to have founded it." The meaning holds (npnf201 26185-26186). However, "for Eusebius" can be heard as "on Eusebius's behalf". Accepted wording, which keeps a tag that carries trust on a disputed point: "Irenaeus traced it to earlier teachers, but Eusebius passes on a report that Tatian founded it."
- **Tags and quotation counts.** I found no kept tag that carries no trust. Each kept tag marks one of these:
  - the person's own words;
  - a partisan or hostile witness;
  - a single source;
  - a wonder;
  - a dispute.

  No brief keeps a quotation beyond what the ruling allows. Clement's "whose books were drawn from the heart of philosophy" is Jerome's mild praise, inside a sentence of which he is the subject (npnf206 16636). It can stand.

## Fixes applied (coordinator thread, 2026-11-16)

Each finding is applied in the accepted wording above: Clement (the pronoun), Hermas (Tertullian's claim marked as his again), Josephus's card (the caveat on Jerome's Latin restored), and the non-blocking Tatian wording ("Eusebius passes on a report that Tatian founded it."). Readability rerun on the three briefs: all pass.
