# C6 coverage map: authority, who was in charge, popes, councils, tradition

Read-only pass, 26 October 2026; nothing in the repo was edited. Every claim was checked against `records/<code>/` front matter and `cic/texts/`; paths, line numbers and verification results are in `search/C6/C6-coverage.json`.

## The sub-questions

The 26 C6 questions plus R-16, R-17, R-39 and R-40 group into eight:

| id | sub-question | question ids |
|---|---|---|
| C6.S1 | Who led, how chosen, titles, bishops or not, could a congregation remove one | C6-01, 02, 06, 08, 15, 20, 21, 23 |
| C6.S2 | The pope and Rome; Peter and "on this rock" | C6-09, 10, 25 |
| C6.S3 | Councils and creeds; who decided; did ordinary believers have a say | C6-03, 18, 19, 26 |
| C6.S4 | Tradition and scripture; apostolic succession; only true church; a church today | C6-04, 05, 13, 14, 24 |
| C6.S5 | Heresy: who decided, what happened to heretics | C6-12 |
| C6.S6 | Married clergy; deacons and deaconesses | C6-11, 22 |
| C6.S7 | The emperor's say in belief | C6-17 |
| C6.S8 | Leaders who failed or abused; distrust; lonely leaders; divided congregations | C6-07, 16; R-16, 17, 39, 40 |

## Layer table

R = RENDERED, `*` = partial or guard only, L = LOADED (vendored, mapped, read in context, no record). No cell fell to I, O or NOTHING; IDENTIFIED and OTHER items sit inside cells in the JSON.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R* | L | R | R | R | R* | R | R |
| cappadocian | R | L | R | R | R | R* | R | R |
| desert | R | L | R | R* | R | L | L | R |
| don | R | R* | R | R | R | L | R | R |
| gallic | R | R | R | R | R | L | R | R |
| hal | R* | R* | R | R | R | L | R* | R |
| ijc | R* | R | R | R | R | L | R | R |
| lpc | R | R* | R | R | R | L | R | R |
| pahc | R | R | R* | R | R | R* | R* | R |
| rzg | R | R* | R | R* | R | L | R | R* |
| syr | R | L | R | R | R | R* | R | R* |
| witt | R | R | R | R | R | R | R | R |

Totals: 66 R, 18 R*, 12 L. Weakest columns: S6 (one full answer) and S2 (four full). `lpc` is wholly draft with no package yet.

**Canon demonstrations.** F3-I has 5 questions, F1-E 2, F3-T 2 (9 per world). Demonstrations exist for F3-I only: `gallic.demo.who-chose-bishops` (f3-i-05), `syr.demo.authority` and `witt.demo.who-held-authority` (f3-i-01): 3 demos, 3 of 12 worlds. F1-E: 0 of 12 worlds. F3-T: 0 of 12. The cells are not empty of records (171, 35 and 49 records carry F3-I, F1-E and F3-T tags), so what is missing is the worked exchange, not the ground.

Verification: 68 quote records are cited as RENDERED; 67 match their vendored file verbatim (file and line in the JSON). Seven matched only after an editorial artifact: section numbers (Demetrius, the Didache prophet), spacing (Basil's doxology, Symeon), a line-end hyphen (Augustine's ordination), an italic tag (Pliny), a printed page break (the hyena quote). None is a wording change. `don.quote.donatus-quid-est-imperatori` is partial: the English line matches Vassall-Phillips line 1904, but the Latin is found only in Ziwsa's word index, and the record is draft.

## World by world

**Alexandria (alx).** Can say: the council answer (teachers, then bishop, then council; no vote), tradition as the rule of faith, the Demetrius-Origen break, the emperor's double effect; all quotes verified. Thin: how a bishop was chosen (nothing rendered; Athanasius's election is in `npnf204` line 4429; Jerome Ep. 146 says Alexandrian presbyters named their bishop, but it sits in hal's map), Rome (no record), deacons beyond Clement's ranks. Add: a quote on choosing a bishop, a Rome note.

**Cappadocians (cappadocian).** The best tradition answer (unwritten customs, "no signed receipt"), a clean council answer, and the fleet's best lonely-leader material (Sasima, Nyssa's exile, Gregory resigning). Thin: Rome (Basil's appeals to Damasus, `npnf208` 8159), deaconesses (Lampadia in the Life of Macrina, line 278; unrendered). The 381 communion law is named, not vendored. Add: a Rome contested_claim, a deaconess term.

**Desert (desert).** Honest and unusual: earned elders against the Pachomian office, never settled; monks sat in no council. Thin: tradition, succession and a church today (R*); Rome, married clergy and the emperor (Paphnutius of the Thebaid at Nicaea, `npnf202` 3763; Constantine's letter to Antony, Vita 81). Add: absence records for S4, S6 and S7. The hyena quote is verified across a page break; the communal-wrong limit is draft.

**Donatists (don).** Excellent on S1, S3, S5 and S7: made by people and bishops, 279 against 286 at Carthage, three imperial recourses owned. The Rome answer is a guard (the primate was no pope). Optatus on Peter's keys and chair (`optatus_against-the-donatists.txt` 145, 153) is unrendered. The founding emperor quote is draft and half verified. Add: finish that quote; one Rome note.

**Gallic monastics (gallic).** The fleet's richest set on how bishops were made (demo, story, contested capture claim, four verified quotes), on Rome as honour not supremacy, and on tradition (Vincent's test). Thin: deacons and married clergy; the Synod of Orange 441, canon 26 ("Deaconesses shall no longer be ordained", `hefele` v3 line 8855) is in ijc's map only.

**Jerome's circle (hal).** Thin on office: authority is patronage and learning. Rome is where news arrives. Jerome's "I communicate with none but your blessedness, that is with the chair of Peter" (`npnf206` 5050) and his Ep. 146 on presbyters choosing bishops are vendored and unquoted. The emperor answer is about corruption, not belief. Add: two quotes.

**Imperial-juridical (ijc).** The model for S2 and S7: Julius, Leo, Canon 28, "Peter has spoken", Ambrose's "within the Church". Thin: no term for presbyter or deacon; Chrysostom on a deaconess and Orange 441 are unrendered. Add: a deaconess term.

**Latin pastoral (lpc, building).** Every authority record is draft: election of Cyprian, the people's cry for Augustine, Cyprian's "bishop of bishops", the only apostolic-succession witness and an "origin undefended" limit. Eight quotes verified. Nothing is packaged. Thin: Rome as such, clergy marriage.

**Post-apostolic house church (pahc).** Best titles answer (episkopos, presbyteros, diakonos) and the honest "bishops or not"; Polycrates against Victor; Corinth removing its elders. No council or creed record (R*). Deaconesses via Pliny's verified "ministrae", with the warning that the title is Pliny's. Irenaeus III.3 succession lists are vendored and unrendered.

**Zurich and Geneva (rzg).** Good on who governed (council, consistory, elders) but Rome appears only as the foil for sola scriptura. Calvin IV.6 on "Thou art Peter" (`calvin vol3` 4943), Zwingli on Matt. 16 and Zwingli's petition for married priests (`zwingli_selected-works` 968) are unrendered. The 1576 council revision of the Ordinances is vendored in French; the 1541 text is named only. Servetus appears in no record. Add: quotes for Calvin on the papacy and on deacons; a Servetus contested_claim.

**Syriac (syr).** Authority never ranked (bishops, covenant, teachers); Papa's primacy Contested; the one worked demo on F3-I-01. The Doctrine of Addai gives an ordination chain from Cephas through Rome and Antioch to Palut (`addai_doctrine-of-addai.txt` 89): the fleet's only Syriac Rome text, unrendered. The Nicene creed in Marutha's Syriac texts is vendored. Add: a quote on that chain; a Didascalia source.

**Wittenberg (witt).** The only full column. Office as task, pope and Antichrist as two voices, married pastors argued. But authority has two quotes only. Unquoted though vendored: the Treatise on the Power and Primacy of the Pope (`book-of-concord ... jacobs1911` 17482), AC XXVIII (line 1271), AC XXIII on priests' marriage (line 707) and Apology XXIII. No deacons. Add: three quotes.

## Other sources (outside the repo; from working knowledge, not fetched)

Didascalia Apostolorum (Syria, 3rd c.): bishops, deaconesses, penance; Gibson 1903 is public domain (syr S1, S5, S6; also helps pahc). Hippolytus, Apostolic Tradition: the bishop "chosen by all the people" (Easton 1934; rights unchecked). Both are in the JSON with editions and licences.

## Not checked

- `canon/sealed_probes/` was not read.
- Not every LOADED line was traced to its author in a shared volume; the cited ones were read in context.
- Non-English vendored texts were counted, not read.
- The seven record-less worlds (aec, hus, jes, meth, obel, rcg, wsyr) were not graded.
- Readability of spoken fields was not graded.
