# House Churches force records: adversarial review, round 2, 2026-10-24

- **Reviewed:** the fixes to the round-1 findings (`2026-10-24_pahc-force-records_Review_Round1.md`, B1 to B6 and N1 to N4) in the uncommitted edits under `records/pahc/force/`: transmission-network, roman-mediterranean-world, systematic-theological-mode-elsewhere, monepiscopacy-consolidation, authority-consolidation, boundary-drawing, martyrdom-meaning.
- **Method:** targeted recheck. Only the sentences and source entries named in round 1, plus anything the fixes introduced in those same places. Each fixed sentence read against the vendored text at the cited lines. Not a full re-review. Path keys as in round 1: A1 = `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`; A2 = `cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`; E = `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`. Line numbers are raw lines.
- **Gates:** `python -m engine.m10.cli regate pahc --base origin/main`: PASS (no force record in this set raises a finding; the only force note is the pre-existing, unchanged alexandria-emergence). `python -m pytest engine/m1/tests/test_embedded_quotations.py -q -p no:cacheprovider`: 16 passed.
- **Date:** 2026-10-24
- **Reviewer:** independent Opus context. Read only. No model or API calls. No record edited.

## Verdict: PASS

All six blocking findings are resolved with the round-1 wording, and the text now matches the source. N1 to N4 are applied correctly. The new Irenaeus source entry points at Against Heresies 3.3.3. One new non-blocking point (R2-N1) is noted below; it does not hold the records back.

## B1 to B6

| # | Record | Resolved? | Evidence |
|---|---|---|---|
| B1 | transmission-network: description, divergence_note, shepherd-hermas locus | Resolved | All three now say Hermas writes two copies of his book and Clement sends it "to foreign countries". A2:1010-1013: "You will write therefore two books, and you will send the one to Clemens and the other to Grapte. ... And Clemens will send his to foreign countries, for permission has been granted to him to do so." The quoted 'for permission has been granted to him' is verbatim (A2:1012-1013). |
| B2 | transmission-network: description | Resolved | "The other was a dispute" is gone. The quarrel is now tied to 1 Clement's own occasion, and Dionysius is cited for lasting use. E:25113-25118: "showing that it had been the custom from the beginning to read it in the church ... we have read your epistle. From it, whenever we read it, we shall always be able to draw advice, as also from the former epistle, which was written to us through Clement." The paraphrase ("They will always draw advice from it, as from the earlier letter written to them through Clement"; "reading Clement's letter in church was an old custom") is faithful and stays under the 8-word quotation threshold. |
| B3 | roman-mediterranean-world: description | Resolved | Now: "they and Ignatius both wrote to him. They asked that anyone traveling on to Syria carry the Philippians' letter." A1:3607-3610: "Both you and Ignatius wrote to me, that if any one went [from this] into Syria, he should carry your letter with him". |
| B4 | systematic-theological-mode-elsewhere: description | Resolved | Now: "Irenaeus argues from apostolic succession as a structure already secured." Tertullian's Apology is no longer said to argue from succession; the remaining Tertullian sentence ("It opens a body of confident Latin defense") makes no succession claim. |
| B5 | monepiscopacy-consolidation: divergence_note, description, sources | Resolved | Both fields now say Irenaeus names Victor's predecessors one at a time and lists the same men in the episcopate, so the passage does not settle one bishop versus a college. E:31527-31530: "the presbyters before Soter, who presided over the church which thou now rulest. We mean Anicetus, and Pius, and Hyginus, and Telesphorus, and Xystus." A1:39846-39851: "then, sixth from the apostles, Sixtus was appointed; after him, Telesphorus ... then Hyginus; after him, Pius; then after him, Anicetus. Soter having succeeded Anicetus, Eleutherius does now, in the twelfth place from the apostles, hold the inheritance of the episcopate." New source entry: see below. |
| B6 | authority-consolidation: description | Resolved | Now: "Hermas, 1 Clement and Polycarp's letter name no single bishop over a church." This no longer conflicts with Hermas naming Clement and Grapte (A2:1010-1013). |

**New source entry, monepiscopacy-consolidation.** `pahc.source.irenaeus-adversus-haereses`, locus "3.3.3 (the Roman succession from Linus to Eleutherius, 'the inheritance of the episcopate')". Correct. A1:39762 opens Book III, "Chapter III.—A refutation of the heretics, from the fact that, in the various Churches, a perpetual succession of bishops was kept up." Paragraph 3 begins at A1:39824 ("3. ... committed into the hands of Linus the office of the episcopate", A1:39825-39826) and ends with Eleutherius (A1:39849). "the inheritance of the episcopate" is verbatim (A1:39849-39850). The source record `records/pahc/source/pahc.source.irenaeus-adversus-haereses.md` exists, and regate accepts the entry.

## N1 to N4

| # | Applied correctly? | Evidence |
|---|---|---|
| N1 | Yes, in both authority-consolidation and boundary-drawing | Both read "He calls a eucharist sound when the bishop, or someone he entrusts, leads it (Smyrnaeans 8)." A1:8279-8283: "Eucharist, which is [administered] either by the bishop, or by one to whom he has entrusted it." |
| N2 | Yes | The "English texts we hold" sentence is gone, replaced by the round-1 wording. The ignatius-letters locus now carries "Ephesians 2, Magnesians 2, Trallians 1 (delegates met at Smyrna)": A1:4746 Burrhus, A1:5675 Damas, A1:6279 "Polybius your bishop ... who has come to Smyrna". See R2-N1. |
| N3 | Yes | "One side is a council of leaders against one bishop. The other is apostolic witness against a closed canon." |
| N4 | Yes | The manifestation reads "planning to keep the anniversary of his martyrdom (Martyrdom of Polycarp 18)", consistent with the description and the source locus. |

## New findings

| # | Record / field | Severity | Problem | Replacement |
|---|---|---|---|---|
| R2-N1 | roman-mediterranean-world: description (N2 sentence) | Non-blocking | "These letters were written in Greek, even those sent to and from Rome." In this description "these letters" are the Ignatius and Polycarp letters it names. One of them was sent to Rome, but none was sent from Rome. The claim is true of the world's letters at large (1 Clement was sent from Rome), so nothing is false. The words "from Rome" just have no referent in the paragraph. | Optional: replace with "These letters were written in Greek, even the one sent to Rome." Or keep as is. |

No new blocking defect. The fixed sentences add no invented detail, and each quotation they carry is verbatim.
