# C9 coverage map: violence, empire, persecution, martyrs, power used badly

Read-only pass, 26 October 2026; nothing in the repo was edited. Claims were checked against `records/<code>/` front matter and `cic/texts/`; file paths, line numbers and verification results are in `search/C9/C9-coverage.json`.

## The sub-questions

| id | sub-question | question ids |
|---|---|---|
| C9.S1 | How dangerous was it; how many died; local or empire-wide; catacombs; accusations; arrests | C9-01, 02, 07, 11, 15, 20, 26 |
| C9.S2 | Seeking martyrdom; the lapsed who returned; informers; honouring endurance under a killing king | C9-06, 08, 16, 17, 21 |
| C9.S3 | Constantine and the empire; instrument or beast; taxes and office; praying for the persecutor | C9-03, 12, 19, 22 |
| C9.S4 | Soldiers, war, judges, the death penalty, "render unto Caesar" | C9-09, 14, 23 |
| C9.S5 | Power against dissenters: heretics, books, temples, forced conversion, Hypatia, the torturer's side | C9-04, 05, 10, 13, 18, 24, 25 |
| C9.S6 | The church taking political sides; injustice in Christian history | R-15, R-30 |

## Layer table

R = RENDERED (a record speaks to it), R* = partial, guard-only or draft-only, L = LOADED (vendored, mapped, read in context, no record), "-" = nothing. No IDENTIFIED-only or NOTHING cell turned up: every world has at least a loaded library.

| world | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| alx | R* | R | R | R* | R* | R |
| cappadocian | R | R* | R | L | R* | R |
| desert | R* | R | L | L | R* | R* |
| don | R | R | R | L | R | R |
| gallic | R* | R* | R | R | R | R |
| hal | R* | R* | R | L | R* | R |
| ijc | R* | R* | R | R* | R | R |
| lpc | R* | R | R | R* | R | R* |
| pahc | R | R | R* | L | R* | R* |
| rzg | R* | R* | L | L | R | R* |
| syr | R | R* | R | L | R* | R |
| witt | R | R | R | R* | R* | R |

All 330 `lpc` records are `status: draft`, so every lpc cell is draft-only. Hal, ijc and gallic S1/S2 are honest guards ("our window begins after the persecutions"), not evidence on the question.

Canon-cell demonstrations (per world; parsed from `canon_cells`, status `ready` unless noted):

| cell | alx | cap | des | don | gal | hal | ijc | lpc | pahc | rzg | syr | witt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F3-I | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| F3-E | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F3-P | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 draft | 0 | 0 | 0 | 0 |
| F6-E | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

The nine F3-I/F3-E/F3-P/F6-E demos are thinner than they look. The three F3-I demos answer leadership (f3-i-01, f3-i-05), not C9-01's question (f3-i-03, "dangerous to be a Christian"), so no world has a danger demo, a catacombs demo (f3-e-01) or a temples demo (f3-p-03). The `lpc` F3-P demo carries `canon_question_id` f3-p-02 but its participant line is the hypocrites question. The three `rzg` demos have empty `canon_cells`.

## Verification

38 quote records are cited as RENDERED; all 38 MATCH their vendored file. Four matched only after an editorial artifact: a spacing break (Milan edict, Constantine's vision, Symeon, the Aphrahat Jewish-sage quote). Four were resolved by hand: the Donatus line (Latin at `optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt:3357`, English at `optatus_against-the-donatists.txt:1904`; `don.quote.donatus-quid-est-imperatori` is still draft), Ammianus on Damasus (an OCR footnote digit), Pliny on the two women (it sits inside an editor's note, `npnf201` line 19504) and Ephrem's "blasphemy of madmen" (an editor's page marker).

## World by world

**Alexandria.** Can say, verified: Clement IV.4 on those "in haste to give themselves up" (`alx.quote.clement-rash-martyrdom`, anf02:37819); four persecutions and Origen tortured (`alx.force.persecution`); the empire as both protector and interferer, with Athanasius exiled five times. Thin: no catacombs, counts or accusations answer, though Origen's "easily numbered" (Against Celsus III.8, anf04:42965) and the Thyestean charge (npnf201:27024) are vendored. Nothing on the Serapeum (Socrates V.16, npnf202:15667) or Hypatia (VII.15, :19548); Origen's "we fight on his behalf" (VIII.73, anf04:63038) is the only soldier answer and is unquoted. Add: a Hypatia/Serapeum honest_limit.

**Cappadocians.** Strongest on danger and martyr memory: no catacombs, Eupsychius killed under Julian, the Forty, an honest "stranger weather" under Valens (`cappadocian.dw.a-stranger-weather`, `.story.valens-caesarea`). `dw.power-and-its-discipline` owns the 381 law. Gap: soldiers. Basil Letter 188, canon 13, "Homicide in war is not reckoned ... as homicide" (npnf208:35312) is vendored and unquoted, and the Forty were serving soldiers. The Basil and Nyssa martyr homilies and the 381 law are registered, unvendored.

**Desert.** Death-wish is answered twice, both hedged: `desert.dw.death-wish` is Inferential-Thin, the Antony quote Contested. No empire answer (Vita Antonii 81, emperors write to Antony, npnf204:33185, unrendered); nothing on soldiers. `desert.limit.communal-wrong-unrepaired` is still draft.

**Donatists.** The fullest power answer: `don.dw.what-we-did-with-the-power-we-had`, the Bagai decree quote, a ready F3-P demo; empire as "our whole case". The Bagai violence limit is draft. Hazard: Circumcellion martyr-seeking rests on hostile portraits and the world cannot answer; Augustine Letter 133 on sparing them and City of God XIX.6 on the torturing judge (npnf101:45893, npnf102:38301) are mapped and unframed. Tilley's Donatist martyr stories and the Abitinian acts are registered, unvendored.

**Gallic monastics.** Only world with a verified soldier answer: Martin's discharge ("I am the soldier of Christ: it is not lawful for me to fight", npnf211:827-842) and the Trier/Ithacian story, where Martin refused to defend church power and lost his gift for yielding once. S1/S2 are guards (no persecution in the span).

**Jerome's circle.** Honest guards: `hal.limit.martyrdom`, `hal.dw.empire` (no catacombs), `hal.dw.church-failure` ("we dealt some and took some"). The only violence is the 416 attack by Christians (`hal.story.attack-416`). Nothing on soldiers or the death penalty.

**Imperial-juridical.** Richest on empire and force: Milan edict, Constantine's vision, Augustine on compelling the Donatists, Callinicum, the Altar of Victory, Thessalonica and penance, Damasus's riot. Gap: soldiers and the death penalty; Hypatia (L). `ijc.limit.earlier-windows` declines martyrdom and torture questions.

**Latin pastoral (draft).** Decian libelli, the lapsed's missing voice, the Numidicus story and Augustine's three-phase coercion are all written, none ready. Unrendered and mapped: Letter 133 (npnf101:45893) and City of God XIX.6, which answer the death penalty and the torturer's side. The demo mismatch is above.

**Post-apostolic house church.** Best danger answer: Pliny, Tacitus, "not constant terror", no catacomb evidence; Quintus recanting, Polycarp betrayed from his own household. Gaps: soldiers (Justin on swords into ploughshares, anf01:15403, unrendered) and taxes (Justin, anf01:14581).

**Zurich and Geneva.** `rzg.witness.defending-the-anabaptist-suppression` is the honest answer. But Servetus is named only in a parenthesis, while Tweedie's *Calvin and Servetus* (550 hits), Calvin's Opera vol. 8 and Letters vol. 2 are vendored and mapped; the Second Helvetic Confession XXX ("punish ... incorrigible heretics"; wars "only in self-defense", schaff:1568) and Institutes IV.20 are unquoted. The Anabaptist side (Hubmaier, Menno, Martyrs Mirror) is vendored but mapped to another movement.

**Syriac.** Persian persecution is covered (Simeon, Usthazanes, the double tax). Starter C9-08, "does honouring endurance teach people to accept a killing king?", has no answer; Aphrahat's Demonstration V, Of Wars (npnf213:24534), is mapped and unrendered. The Persian martyr acts (Braun 1915, Hoffmann 1880) are vendored but mapped to the Church of the East movements, not syr.

**Wittenberg.** Honest on the sword and the Brussels martyrs; the 1525 Peasants' War and the 1543 tract are named as existing and not quoted (the 1525 tracts are registered, unvendored). Gap: AC XVI ("sit as judges ... engage in just wars, serve as soldiers", melanchthon_augsburg-confession_anon-pg275:414) is vendored and unrendered.

## Biggest findings

1. C9.S4 is nearly bare: only gallic has a ready soldier answer. Seven worlds are LOADED-only, each with a verified, unquoted passage above.
2. Demonstrations: none for C9-01, C9-02 or C9-05 in any world; don alone covers three of four cells; lpc's is draft and mismatched.
3. Servetus (rzg), Hypatia and the Serapeum (all worlds), and informers (C9-21) have no record, though sources sit in the library.

## Other sources (outside the repo; from working knowledge, not fetched)

Knipfing, "The Libelli of the Decian Persecution" (HTR 1923) for the lapsed (alx, lpc); the Acts of Maximilian and Marcellus (Ruinart) for soldiers; Synesius's letters and Damascius for Hypatia; Hippolytus's Apostolic Tradition 16 on soldiers and magistrates; Libanius, Oration 30, for temples.

## Not checked

- `canon/sealed_probes/` was not read. The seven record-less worlds were not read. Spoken-field readability was not graded.
- The anchor scan counts whole mapped files, so shared volumes can credit a world with a neighbour's author; only cited lines were read in context.
- Non-English texts (Latin, German) were counted, not read. Tertullian's Apology (anf03) is mapped to pahc only; lpc and don were not checked for it.
- Which `lpc` drafts reach the compiled package was not checked.
