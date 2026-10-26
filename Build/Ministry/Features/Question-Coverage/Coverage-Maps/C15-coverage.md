# C15 coverage map: "What would you say about today?"

Read-only pass, 26 October 2026; nothing in the repo was edited. All twenty questions are flagged NF (never faced). Record ids, files, lines and guard text are in `search/C15/C15-coverage.json`. The earlier agent's eight search runs were complete (all error files empty) and were reused; I regrouped them to the ids in `07-subquestions.yaml`.

## Sub-questions

| id | sub-question | question ids |
|---|---|---|
| S1 | Gay marriage | C15-01 |
| S2 | Evolution, science, climate | 02, 09 |
| S3 | AI and talking to a machine | 03 |
| S4 | Which church; Catholic church and pope now; megachurches and bands; Reformation and East-West split | 04, 05, 06, 10 |
| S5 | Christians in politics and voting; "religion causes wars" | 07, 15 |
| S6 | Women pastors today | 08 |
| S7 | Abortion laws; an ageing church; a burnt-out pastor; the Bible on a phone | 11, 12, 13, 14 |
| S8 | Are we what you hoped for; Christians and Jews together; Sunday; the world now; would you still believe | 16-20 |

## Layer table

NR = NEAREST-RENDERED, NL = NEAREST-LOADED, LO = LIMIT-ONLY. A cell shows the best and worst of its wordings (best/worst). NOTHING is not used: a limit can always be written.

Rules I applied. NR needs a record with the nearest material and a guard that names the modern frame (an honest_limit, a not_for, or a plain in-voice refusal). A record with no such guard counts as NL and is listed in the JSON with empty guards. LO means the right answer is silence plus a limit; the JSON says whether one is built.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | NL | NR/LO | LO | NR/LO | NL | NR | NL/LO | NR/LO |
| cappadocian | NL | NL | LO | NR/LO | NL | NR | NR/LO | NL/LO |
| desert | LO | LO | LO | NL/LO | LO | NR | NR/LO | NR/LO |
| don | LO | LO | LO | NR/LO | NR | NR | LO | NL/LO |
| gallic | NL | LO | LO | NR/LO | NR/NL | LO | NR/LO | NR/LO |
| hal | NL | LO | LO | NR/LO | NL | NR | NL/LO | NR/LO |
| ijc | NL | NL/LO | LO | NR/NL | NR | NL | NR/LO | NL/LO |
| lpc | NL | NL/LO | LO | NL/LO | NL | NL | NL/LO | NL/LO |
| pahc | NL | NR/LO | LO | NR/LO | NL/LO | NR | NR/LO | NR/LO |
| rzg | NL | NL | LO | NR/LO | NL | NR | LO | LO |
| syr | NL | NR/LO | LO | NR/LO | NL | NR | NL/LO | NR/LO |
| witt | NL | NR/LO | LO | NR/NL | NR | NL | NL/LO | NR/LO |

Totals over 240 cells: NR 57, NL 72, LO 111. S3 is LO everywhere; S1 has no NR anywhere.

Verification: 34 quote records are cited. 31 match their vendored file verbatim (two only after spacing is normalised). Three needed a hand check. `pahc.quote.two-female-slaves-who-were-called-deaconesses` is verbatim at npnf201 lines 19502-19506, but inside the NPNF editor's endnote; the record names a Pliny source that is not vendored. `cappadocian.quote.macrina-refuses-remarriage` matches once the editor's page marker "|25" is dropped (line 128). `don.quote.donatus-quid-est-imperatori` is partial: the English gloss is at line 1904 of the Optatus translation, but the Latin appears only in the critical edition's index (line 23707).

## World by world

**Alexandria.** Strong on S2 (Origen, days without a sun, fenced against "modern science"), S4 (`alx.dw.one-church`) and S6 (in-voice "no woman in office, will not invent one"). S8 doubt is fenced three ways. Nothing on S1 guards, S3, abortion or Jews.

**Cappadocians.** S4 is fenced, including worship ("a modern preference about worship style", `cappadocian.term.psalmodia`). Burnout has Gregory of Nazianzus resigning, with his reasons unsettled. S2 and S9 have Basil's Hexaemeron and no guard. S1's loaded text is Basil's Canon VII, a penance rule.

**Desert.** Good on S6 (Sarah, fenced against gender-identity readings) and burnout (the noonday demon, "not a diagnosis of burnout"). Genesis limit built. No church-identity or politics guard.

**Donatists.** Best for S5: church-state fences and the Bagai limit. S4 fenced (no present-day descendant). S2 limit sits inside a not_for. Quote caveat above.

**Gallic monastics.** Best burnout fence in the fleet (`gallic.term.accidie`, `lukewarmness`). S4 fenced, including "Pope" as a title. S5 fenced by `government-of-god`. S1's nearest is Salvian on Africa, unframed.

**Jerome's circle.** S4 and S6 fenced (Marcella is "not an ordained role"). `hal.dw.church-failure` fences against modern abuse parallels. Nothing on S2, S3.

**Imperial-juridical.** Best fenced for S5 and the East-West split (`primatus`, `primacy-reception`). `ijc.limit.reading-alone` serves the Bible-on-a-phone question. It already has the fleet's one "later age" limit (`ijc.limit.later-questions`).

**Latin pastoral (building).** Rich vendored library, but all 330 records are draft with no use_note, so no guards exist. Every lpc cell is NL or LO until that changes.

**Post-apostolic.** The model for S2: "that fight had not been invented yet." Also fenced on S4, S6 (`ministrae`) and S7 (most could not read). Abortion appears only as one line of the Two Ways story and Barnabas 19.

**Zurich and Geneva.** S6 has `rzg.limit.dentiere-and-womens-voice`. S2 has no record, yet Calvin on Genesis 1:16 ("Moses wrote in a popular style") is vendored and unquoted. Its marriage limit says the record has no marriage teaching while Calvin's commentary is vendored: reconcile. The Reformation is its own, so C15-10 is in-window.

**Syriac.** The only explicit "today" fence on the Jewish question (`syr.term.anti-jewish-polemic`). S2, S4, S6 fenced. Nothing on S5 guards or S7.

**Wittenberg.** Fenced on S2, S4 (no church "existing today or after 1580"), S5 (modern political theology, religiously sanctioned violence). The East-West split meets the vendored Jeremias II correspondence (1576-81, Latin). The 1543 text on the Jews is named, not vendored.

## Existing conventions to follow

**Horizon scan** (`engine/m1/horizon.py`). Flags 29 gazetteer events (303 to 1648), fleet `modern_term` display terms, explicit years and later centuries. The fleet has one modern_term (Trinity). Tested: evolution, internet, AI, podcast, gay marriage and the bare word "Reformation" are not flagged; "Great Schism", "Protestant", "Council of Trent" and "twentieth century" are.

**Output check** (`engine/m4/output_check.py:397-415`). `check_horizon` reports one finding per sentence on finished text; it never edits. It needs each world's window end (alx 400 ... rzg 1650, witt 1580; list in the JSON).

**Routing** (`engine/m5/routing.py:177-190`). A `later_age` question on the first ask goes to the voice ("in-world answer"); only a second ask reaches `etic_turn`. So the honest_limit does all the work on the first ask. "What do you think about AI?" does not match the system_nature shape, so no Facilitator turn fires.

**Etic and bridge turns** (`engine/m4/facilitator_turns.py:139-148, 194, 433`). The etic text for later_age is fixed and code-owned: "That question reaches past where this Christian tradition's own witnesses stop ... a real period this tradition simply never reached." The bridge turn needs a `modern_term` record; none exists for any C15 term.

**Honest_limit phrasing.** Greps: "your tongue" 1 record (`alx.demo.marriage-ending`); "no occasion" 0 limits; "later question" 0. The working patterns are: `ijc.limit.later-questions` ("That framing comes from a later age's battles ... we will not invent an answer they did not give"); `don.limit.questions-we-never-argued` ("The nearest we can bring you is small ... Anything more would be us making it up"); `pahc.witness.scripture-and-testimony` ("that fight had not been invented yet. We cannot answer it the way you're asking it"); `syr.dw.reading`; `witt.dw.one-holy-church-forever`; and the women-in-office demos. `gallic` and `witt` voice_craft files carry a "later-names" rule: one sentence naming that the label is not in the record, then answer in the world's own words. Schema: statement, why_sources_cannot_answer, nearest_material, use_note.not_for.

## Proposed honest_limit shapes (a proposal for Mark, not a Representative answer)

Frame for all: (1) name the frame as not ours, in the world's own word; (2) say what we did hold, nearest first, with its confidence; (3) say what the sources cannot give; (4) not_for: a verdict on any person or on today.

- **S1.** {World} never put {modern term} to itself. What it held about {marriage | the body}: {record}, {confidence}. Nothing on {the modern case}. Not for: a verdict on any couple; no penance canon or Rom 1 passage offered as the answer.
- **S2.** {Fight} had not been invented in {window}. We read {creation text} for {purpose}: {record}. Not for: a side in evolution or the age of the earth.
- **S3.** One sentence of silence; no likeness to {idol | oracle}; no nearest. System questions stay with the Facilitator.
- **S4.** {Catholic} meant {sense}, not {later denomination}. Which church to join is not ours to answer; our rivals were {named}. What we looked for: {mark}. Not for: any present-day church as heir.
- **S5.** We never stood where you stand: {acclamation | emperor | magistrate}. Nearest: {record}. Where our side used force: {admission}. Not for: a view on a party or state.
- **S6.** In named office we cannot show you a woman, and we will not invent one. Authority also ran through {household | school | covenant}: {named woman, source}. Not for: ordination today.
- **S7.** Four slots. Tired pastor: {term}, not a diagnosis. Old church: limit only. Abortion: {penance rule | Two Ways line}, never law; no view on yours. Bible on a phone: most could not read; scripture came by {ear}.
- **S8.** We feared {our named failure}; we cannot see you. Sunday: {our gathering}; where to find us now is not ours to say. Jews: {one-sided frame}; no verdict today. Doubt: {record}, not weighed against modern knowledge.

## Three findings

1. No record in any world says "we never met that question" for a C15 wording. Fences are by-products of canon cells: F2-T gives four explicit science non-answers, F3-T gives nine worlds a "not a later denomination" fence. S1, S3, ageing churches and "the world now" have none.
2. The engine cannot see these questions: the horizon scan misses every modern topic here, the first-ask path has no Facilitator text, and no modern_term exists.
3. For S1, S3 and abortion the nearest vendored text is condemnatory or penal. Offered as "nearest" it answers by implication; whether to name it is Mark's call.

## Not checked

- Non-English vendored texts were counted, not read (witt Jeremias II letters, Luther Latin, Calvin Opera).
- Whole-file scans hit shared volumes (Cyril in npnf207, Athenagoras in anf02); each NL line was traced to a mapped work, not every one to its exact chapter.
- Cells marked LO were judged from the searches and the not_for survey, not from reading every mapped work; Calvin's Exodus 21:22 comment and Luther on the Jews are not vendored.
- `canon/sealed_probes/` was not read. Nothing was run against a model. lpc draft records were not checked against the compiled package.
