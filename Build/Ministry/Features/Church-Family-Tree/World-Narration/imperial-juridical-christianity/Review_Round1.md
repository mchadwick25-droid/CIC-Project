# Review Round 1: imperial-juridical-christianity

| Piece | Verdict | Grade | Ease | Findings |
|---|---|---|---|---|
| story | REVISE | 8.4 | 70.1 | 1 PRE-EXISTING ("The emperor stopped hunting the church"), 1 MINOR (31-word opening join) |
| legacy | REVISE | 7.8 | 66.1 | 1 BLOCKING ("The record used here"), 2 MINOR ("The record opens..."; "these churches") |
| altar-of-victory | PASS | 6.8 | 75.8 | none |
| callinicum-synagogue | PASS | 9.1 | 66.6 | 1 MINOR (card: the account rests on Ambrose alone) |
| dream-before-battle | PASS | 8.7 | 75.5 | 1 MINOR (record: "by that mark, Lactantius says") |
| emperor-builds-another-basilica | PASS | 8.5 | 75.1 | none |
| emperor-penance | PASS | 8.3 | 70.5 | none |
| eutropius-at-the-altar | PASS | 7.8 | 72.3 | 1 MINOR (record: source of "first eunuch") |
| letter-that-outranked-a-council | PASS | 8.7 | 71.2 | none |
| tome-that-would-not-bend | PASS | 8.5 | 68.7 | 1 MINOR ("No apostle had taught there") |
| vigil-in-basilica | PASS | 7.0 | 78.1 | 1 MINOR (record should cite the locus for "like the Father") |
| vision-and-alliance | REVISE | 6.6 | 81.3 | 1 PRE-EXISTING ("Constantine stopped hunting the church") |

The scores come from `python -m engine.m1.profile_readability` and are names-out ease. All 12 pieces pass the hard limits. Five pieces score under grade 8: altar-of-victory, eutropius-at-the-altar, vigil-in-basilica, vision-and-alliance and legacy. I read each one as a listener and judge them adult and not flat.

## Grounding the rewriter's flags

Each detail the rewriter flagged is held by its story record's `text` and is confirmed in the vendored sources:
- **Altar of Victory sequence:** `npnf210` 40399-40400 and 40477-40479.
- **Callinicum details:** `npnf210` Ep. XL 43163-43166 and Ep. XLI 43563-43570, 43981-43990.
- **Basilica account:** Optatus, Appendix X, `optatus_against-the-donatists.txt` from 7193.
- **Eutropius account:** `npnf109` 17441, 17520-17573, 17593-17599, 17703-17741, 17808.
- **"Under oath":** `npnf201` 61201.
- **"Julius had not attended their council":** the record's own text. Julius's letter answers the Eusebians' objections at `npnf204` 23101-23122.

None is unsupported.

## Quotes

| Piece | Span | Record | File and line | Result |
|---|---|---|---|---|
| emperor-penance | "I, I say, have no reason to charge you with defiance, but I have reason to fear," | ijc.quote.ambrose-dare-not-offer | npnf210_ambrose-select-works-letters.xml 44181-44183 | supported |
| emperor-penance, story | "I dare not offer the sacrifice if you intend to be present." | ijc.quote.ambrose-dare-not-offer | npnf210_ambrose-select-works-letters.xml 44183 | verbatim |
| letter-that-outranked-a-council | "Are you unaware that the custom has been to write to us first, and then for a just decision to be passed from this place?" | ijc.quote.julius-custom | npnf204_athanasius-select-works-letters.xml 23549-23551 | supported |
| tome-that-would-not-bend | "This is the faith of the fathers," | ijc.quote.peter-has-spoken | npnf214_seven-ecumenical-councils.xml 19997 | verbatim |
| tome-that-would-not-bend | "Peter has spoken thus through Leo." | ijc.quote.peter-has-spoken | npnf214_seven-ecumenical-councils.xml 20000 | verbatim to source (the rendering has "so") |
| tome-that-would-not-bend | "things secular stand on a different basis from things divine." | ijc.quote.leo-things-secular | npnf212_leo-great-gregory-great.xml 9079-9081 | verbatim |
| vigil-in-basilica | "like the Father" | none | npnf202_socrates-sozomen-ecclesiastical-histories.xml 8557 ("like to the Father who begat him"), via ijc.term.homoios | supported; the story record should cite it |
| vigil-in-basilica, story | "I cannot give up the basilica, but I must not fight." | ijc.quote.ambrose-cannot-surrender | npnf210_ambrose-select-works-letters.xml 41754-41755 | supported |
| vigil-in-basilica | "the Emperor is within the Church, not above it." | ijc.quote.ambrose-emperor-in-church | npnf210_ambrose-select-works-letters.xml 42662-42663 | verbatim |
| vision-and-alliance, story | "Conquer by this." | ijc.quote.vc-conquer-by-this | npnf201_eusebius-church-history-life-of-constantine.xml 61206 | verbatim |

There is no BLOCKING-QUOTE.

## BLOCKING

- **legacy**: "The record used here ends just as that fracture opens, and it says nothing of how the fracture would end." This is build vocabulary and a report about the record, and the listener cannot place "used here". Replace with: "The story of this period ends just as that fracture opens, and its documents say nothing of how the fracture would end."

## PRE-EXISTING (tree text to correct; tell the record owner)

- **vision-and-alliance**: "Constantine stopped hunting the church..." In the narrator's voice this says Constantine had persecuted the church. Lactantius, *De Mortibus* 24 (`anf07` line 10337), has him restoring Christian worship from his accession, and `ijc.force.constantine-alliance` dates persecution's legal end from Galerius in 311. Replace with: "The empire stopped hunting the church, and within a year toleration was law."
- **story**: "The emperor stopped hunting the church..." Same fault. Replace with the same sentence.

## Pattern

The rewrite is light, as the ruling asks. Most pieces needed only a join or two, and the originals were already in the third person. The two faults that remain are where the church's own view slipped into the narrator's voice:
- the world's emic "an emperor ... stopped hunting the church", carried into the story and the vision story;
- "this world's own record" carried into the legacy as "the record used here".

The MINOR items are for record owners and the card, not the audio.
