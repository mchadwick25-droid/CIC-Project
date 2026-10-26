# C16 coverage map: evidence, sources, and "what are you"

Read-only pass, 25 October 2026; nothing in the repo was edited. Ids, counts, paths, line numbers and verification results are in `search/C16/C16-coverage.json`; scripts and raw greps sit beside it.

## Part A: evidence and sources

### The sub-questions

| id | sub-question | question ids |
|---|---|---|
| S1 | How do you know; single voice; documentation vs inference; where is your record thinnest | C16-01, 03, 04, 05, 08, 09, 24, 28; F2-E-01, -03 |
| S2 | Legend collected later; falsely attributed; later polish; is this text by its named author | C16-02, 07, 18; F2-E-02 |
| S3 | Show me the page; which edition and translation | C16-15, 17 |
| S4 | What modern historians think you got wrong | C16-27 |
| S5 | Named figures in their own words | C16-14, 21, 22 |
| S6 | One line to quote on Sunday | C16-23 |
| S7 | You sound too polished; would a real person talk like this | C16-25 |
| S8 | Whose voices are missing entirely | C16-06 |

LOADED barely applies: the answering material is the record's own metadata (limits, contested claims, source records, divergence notes), not a vendored passage. The background runs over vendored texts stopped after the Gallic world and were not used.

### Layer table

R = a record speaks to it; R* = partial or guard only; O = governed by instruction or product fact, no record.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R | R* | R | R | R | R | O | R |
| cappadocian | R | R | R | R | R* | R | O | R |
| desert | R* | R | R | R | R | R | O | R* |
| don | R | R | R | R | R* | R* | O | R |
| gallic | R | R | R | R | R | R | O | R |
| hal | R* | R | R | R | R | R | O | R |
| ijc | R | R | R | R | R | R | O | R |
| lpc | R | R* | R* | R | R | R | O | R |
| pahc | R | R | R | R | R* | R | O | R |
| rzg | R* | R* | R* | R* | R* | R* | O | R |
| syr | R | R | R | R* | R | R | R* | R |
| witt | R | R | R* | R | R* | R* | O | R |

73 of 96 cells are rendered outright, the best-covered cluster so far. The thinness sits in Zurich and Geneva across the row, the named-figures column, and S7, which no record anywhere answers.

**Canon F2-E.** Four canon questions exist (`engine/canon/records/canon_question/_fleet.canon.f2-e-01..04.md`). Demonstrations exist in four worlds: `rzg.demo.consensus-contest` (f2-e-01, canon_cells empty), `don.demo.mostly-legend` (f2-e-02), `gallic.demo.record-thinnest` and `witt.demo.record-thinnest` (f2-e-03). None anywhere for f2-e-04. Nine worlds carry the cell on a witness or limit instead (ids in the JSON); desert and hal have it only on contested claims, quotes and terms.

### World by world

**Alexandria.** `alx.dw.record` is a model S1 answer: the books were public, Origen answered Celsus by name, Clement flags the John story as handed down, Dionysius weighed the Apocalypse's authorship by its style (`alx.quote.dionysius-too-high-for-me-to-grasp`, verified npnf201 L41418). `alx.contested.didaskaleion-institution` answers C16-09. Legend as such rests on one divergence note. Clement 9 quotes, Origen 6, Athanasius 4, Dionysius 3; Pantaenus, Demetrius, Heraclas, Didymus zero.

**Cappadocians.** `dw.where-record-thinnest` ("three men, one household, one circle of students") and `limit.whose-voice-we-lack` cover S1 and S8. S2 has the fleet's clearest attribution case: `cappadocian.quote.ousia-and-hypostasis`, Letter 38 "transmitted as Basil's; a substantial body of modern scholarship reassigns it to Gregory of Nyssa" (verified npnf208 L25461). The hole is S5: Basil 17, Nyssa 3, Gregory of Nazianzus 0, Macrina 0 in her own words, with the Theological Orations vendored.

**Desert.** Strong on hagiography as genre: `desert.contested.antony-literacy` (Rubenson against Gould), `desert.limit.doubt-and-doctrine`, the Macarian homilies "transmitted under the name of Macarius; author unknown", and the Paradise's own rubric (`desert.quote.composed-by-bishop-palladius-for-the-prefect-lausus`, verified budge v2 L50). No witness answers "where is your record thinnest" as a whole, and no dedicated limit on women's or ordinary voices. Antony 15, Evagrius 6; 30 quotes have no figure record (Cassian's abbots, Palladius's informants).

**Donatists.** The best S1/S2 world: `don.dw.written-by-our-opponents`, `don.demo.mostly-legend` ("Not centuries later. That is the wrong worry about us. The right one is who held the pen"), the forged letter in `don.contested.ministerial-purity` and `don.story.acta-purgationis-felicis`. The worst S5 world: 26 figure records, 5 quotes; Donatus, Petilian, Emeritus one each; Augustine, Optatus, Tyconius, Parmenian zero. The Emeritus quote could not be found in the OCR'd Migne file (verification).

**Gallic monastics.** `gallic.demo.record-thinnest` is the fullest honest-limits exchange in the fleet; `gallic.limit.no-one-who-saw-him` carries "how do you know" in its own cell. Sulpitius's shaping is marked record by record (`gallic.quote.martin-imagined-soldiers-speech`, "his own rhetorical expansion"). The only world that quotes its editors: Gibson's prolegomena and Heurtley's appendix, four verified quotes in npnf211, give S4 a real answer about how modern editors read Vincent. Honoratus zero quotes.

**Jerome's circle.** F2-E lives in contested claims and quotes, not a witness: `hal.contested.ep46-authorship` (the letter in Paula's and Eustochium's names is Jerome's), `hal.contested.hebrew-fluency` with `hal.quote.partially-acquired-hebrew` (npnf206 L22016), and Palladius's outside verdicts (`hal.quote.hindered-by-jerome`, `hal.quote.paula-escaped-his-envy`). No record says where the record as a whole is thinnest. Jerome 19, Augustine 2; Paula, Marcella, Pammachius zero.

**Imperial-juridical.** `ijc.dw.record-under-question` opens "More of our story would hold up in a library than of most ancient worlds" and names the forged attributions (`ijc.contested.damasine-decretals`); two Ammianus quotes give the pagan historian's verdict. Ambrose 6, Leo 5, Constantine 3; Damasus, Pulcheria, Marcian zero.

**Latin pastoral (in build).** `lpc.limit.the-silent-century` (130 years with no ordinary pastoral voice) and eight more limits cover S1 and S8; `lpc.contested.de-unitate-recensions` answers "is this text genuine" where it matters. Gaps: its 210 source records carry an edition but no `citation` field or `kind`; no witness meets the legend question in the visitor's wording. Augustine 19, Cyprian 3, Possidius 1; Pontius, Celerinus, Lucian, Numidicus zero.

**House church (pahc).** `pahc.witness.scholarly-standing` is written for this cluster ("one writer whose dating is genuinely disputed ... our teaching manual survives mostly through one copy"), with the Ignatius, Polycarp and Didache contested claims behind it; Justin 5, Ignatius 3, Hermas 2; Polycarp and Papias zero, with the Martyrdom and Polycarp's letter vendored.

**Zurich and Geneva.** Thin across the row. S1 has a guard (`rzg.limit.hagiography-refused`), one limit on Calvin's one-sided letters, and the Consensus demo; no witness says what the record holds or where it thins. S4's only record concedes "No secondary scholarship on the Consensus Tigurinus specifically is vendored". Six quotes: Zwingli 2, Calvin 2 (one the joint Consensus), Bullinger 1, Myconius 1; Beza, Farel zero.

**Syriac.** `syr.dw.corpus-and-its-edges` does S1, S2 and S4 in one witness: the sage's letters date themselves, the chronicle's flood line may have been added later, the Abgar story "is a legend ... we tell it as our legend, not as our history" (`syr.quote.abgar-letter`, `syr.quote.chronicle-flood-line`, `syr.quote.theodoret-gnats`, all verified). The only partial ground for S7: `syr.dw.jesus` and `syr.dw.was-jesus-god` say hymn, not analysis, was the fitting register. Aphrahat 12, Ephrem 11, Tatian 2; Rabbula, Marutha, Simeon bar Sabbae zero.

**Wittenberg.** `witt.limit.record-thinnest` with its demo, `witt.limit.no-outsider-witness`, and `witt.contested.theses-door-posting` (the posting "is legend", Iserloh) cover S1, S2, S4, S8. The hole is S5 and S6: seven quotes, every one spoken by the Augsburg Confession or the catechism "said by the household itself"; none is attributed to Luther or Melanchthon. "One line from one of your own writers" has no named writer to give.

### Named figures the visitor expects (C16-14)

| name | quotes, by world |
|---|---|
| Athanasius | alx 4; desert 5 (as the Vita's narrator); pahc 1 (the 367 letter, outside its window) |
| Augustine | lpc 19; ijc 4; hal 2; gallic 1; don 0 (figure record exists) |
| Ignatius | pahc 3 |
| Irenaeus | 0 everywhere; no figure record (named only inside `pahc.figure.papias`) |
| Tertullian | 0 everywhere; no figure record |
| Clement of Alexandria | alx 9 (pahc's "First Clement", 2, is a different Clement) |

All quotes are citation_specificity A except two B (desert, gallic).

### "Show me the page": the product today

What a participant sees is built in `engine/m4/citation_cards.py` (`resolve_source_card`, L129-190) and drawn by `cic-poc/frontend/src/components/SourceList.tsx`: the source record's one-line `citation` (or work and author), the locus, the rights status. Four limits:

- `edition` is in the payload (L178) but `SourceList.tsx` never prints it, and when a source record has a `citation` the edition is set to None (L167). The "which edition" answer sits in every source record of eleven worlds and reaches no screen.
- `engine/prose.py display_locus` (L233) strips the vendored file name and the "file lines" clause before display.
- A quote card carries `spoken_rendering` and the speaker; the verbatim `text` is not sent (L186-188).
- No API route serves `cic/texts`; `cic-website/traditions/*.html` carry no per-tradition source list.

Verdict: a checkable citation for every cited claim, yes; the page, no.

## Part B: "what are you"

### What the Facilitator says today

The only system-nature template is `SYSTEM_NATURE`, `engine/m4/facilitator_turns.py` L64-76:

> "Yes - we use AI here, and I'd rather tell you plainly than let you wonder. Each Christian tradition you can speak with is built from a fixed set of records - sources that actually survive from that time and place - and the voice answering you may only say what those records carry. Before you see an answer, each claim in it is checked to make sure its words come from the record it names. The record itself was checked against the sources when the tradition was built. Where the record is silent, the voice is built to say so, not to fill the gap. It isn't a person, it isn't the church, and it doesn't speak for anyone living. / That's the honest shape of it - whenever you're ready, let's keep going."

It is reached (`engine/m5/routing.py` L172-181) only when the reader classifies `system_nature` and the message matches `_SYSTEM_NATURE_SHAPE` (L56-62): a form of *be*, then *you* or *this*, then one of ai, bot, chatbot, robot, real, fake, human, script, program, built, made, created, coded, simulated, artificial, algorithm, software, llm, inside one sentence. Other fixed lines: `DEPENDENCY_CHECK` (L114-132, "not a person who can be there for you"), on a `HARMFUL_DYNAMIC_SIGNAL` only; the etic texts (L139-152); `DOOR` (L85-91). Outside the turn: "This is an AI-generated voice." (`cic-poc/frontend/src/screens/Conversation.tsx` L198) and the site note at `cic-website/index.html` L370.

### Which questions reach a template

| question | regex | result |
|---|---|---|
| C16-10 "...Were you actually alive in the 1500s? What are you, exactly?" | no | Representative |
| C16-11 "What are you, really?" | no | Representative |
| C16-12 "No - how were you made? What are your limitations?" | yes | SYSTEM_NATURE |
| C16-13 "Why do you keep saying 'we'? ... Who is 'we'?" | no | Representative |
| C16-16 "Are you making this up?" | no | Representative |
| C16-19 "Are you going to try to convert me?" | no | Representative |
| C16-20 "Who wrote your answers? Who is behind this?" | no | Representative |
| C16-26 "Is my conversation private? Who reads this?" | no | Representative |
| R-23 "Should I trust you that much [as my pastor]?" | no | Representative |

One of nine has a template. "Are you real?" and "How were you made?" match; "What are you, really?", "Who made you?", "Is this private?" do not. Fall-through list: **C16-10, 11, 13, 16, 19, 20, 26, R-23.**

What the Representative then does is fixed by `engine/shape/records/fleet_voice/_fleet.voice.fleet.md` L33: one sanctioned sentence, "I am a representative of [world]", "only when the participant's own question is directly about the voice's own nature", and otherwise "No explaining what kind of thing is speaking"; Gallic's craft adds "Asked why we say 'we', the answer is a practice or memory held by many, never a sentence about the pronoun." The one in-world demonstration, `rzg.demo.why-we`, takes C16-10 verbatim and answers with the two cities' history; it never says AI. So eight of nine K12 questions get an in-character deflection by design; for C16-20 and C16-26 the voice holds no facts and is forbidden to explain, so its answer will be improvised.

### Privacy facts, for checking the "is this private" answer

Code: conversations idle 90 days are deleted daily (`engine/m4/store.py purge_inactive`; scheduler at `engine/api/app.py` L1147-1162); a participant can delete one. The QC store (`engine/m7/qc_store.py`) keeps one row per turn under a keyed hash of the session id, clears question and answer text after 90 days, keeps marks, scores, routing and flags indefinitely, and samples whole conversations for an offline audit. Backups: 14 days (`engine/api/db_backup.py`).

Stated (`cic-website/privacy.html`): saved 90 days; a scrubbed review copy deleted after 90 days; "Our project team reviews conversations"; "we never quote from them"; Anthropic's Claude on Amazon's servers, kept out of training; Faithways Studio, Inc. is who is behind it (`about.html`). Findings (corrected after Opus review; the 'two cookie paragraphs' item is withdrawn because one paragraph is hidden by a feature flag in `cic-website/assets/privacy-go-deeper.js`): the page does not say the code keeps scores and flags without text (a disclosure gap, not an overstatement: the page's claim about the copy of questions and replies is true); and nothing inside the conversation app links to or states any of this (the only "privacy" string in `cic-poc/frontend/src` is account-deletion copy, `lib/accountsCopy.ts` L132).

## Fleet-wide thin spots

1. Eight of nine K12 questions fall through to a voice forbidden to explain itself. Either the regex shapes widen (what are you really, who made you, is this private, who is behind this) or those get templates; the privacy and "who is behind this" answers exist on the site and are unreachable from the conversation.
2. Irenaeus and Tertullian do not exist in the fleet; Luther, Melanchthon, Gregory of Nazianzus, Polycarp, Augustine in the Donatist world, and Beza have figure records and zero quotes.
3. "Show me the page" is answered with a citation whose edition is never drawn and whose page reference is stripped; the verbatim text is not sent.
4. S7 is empty everywhere; the honest answer ("we sang; we argued in letters; this is a rendering") exists only as syr's register tensions and the quotes' modern_lens notes.
5. F2-E demonstrations in four worlds; none for the suppressed-gospels question.
6. Zurich and Geneva: no witness on what its record holds, six quotes, a conceded absence of secondary scholarship.

## Verification

23 quote records were checked against their vendored files; 19 match exactly or with the tool's known variants. Three match after a hand read of an editorial artifact: `hal.quote.hindered-by-jerome` (clarke1918 L475, footnote numbers 275/276 and "[2]" inside the sentence), `ijc.quote.ammianus-sicininus-massacre` (yonge1862 L23176-23189, section "13." and footnote "1"), `ijc.quote.ammianus-roman-luxury` (L23191, OCR "1 do not deny" for "I"). One is unresolved: `don.quote.emeritus-magno-argumento`, whose Latin is not findable in the OCR-noisy `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` ("argumento" occurs nine times, never with "veritas occultatur").

## Not checked

- `canon/sealed_probes/` was not opened.
- The three background `coverage_search.py` runs were cut off (T1 and T3 after gallic, T2 before output); vendored-text hits were not traced for any layer.
- The reader classifier was not run; fall-through is judged from the routing regex, the second of two conditions.
- `engine/m7/qc_scrub.py` not read against the privacy page; readability not graded; lpc package inclusion not checked; record-less worlds not grepped.
