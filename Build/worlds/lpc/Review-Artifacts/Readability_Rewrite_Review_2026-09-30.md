Simulated review — informational only, not an Article 31 substitute.

# lpc readability rewrite: independent review of the 43 rewritten fields

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** separate readability-rewrite review pass (fresh context, high effort; read none of the drafting session's reasoning; read the rewrite map, the committed records, the source records, Doc_02, Doc_04 and the consumers)
- **Drafter agent:** readability rewrite session (commits 3c51238f5 and 87f68b4f3)
- **Round:** 1 (the independent Opus check of a readability rewrite; not a document revision round)
- **Truncation check, method 1:** line count and closing marker: `grep -cE '^\| [0-9]+ \| lpc\.' ` on this file returns 43 field rows, and `tail -n 1` returns "End of review.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the record/field pairs in the per-field table equal, as a set, the 43 `###` headings of Readability_Rewrite_Map_2026-09-30.md; none is missing on either side. Each finding id in the verdict list also appears as a `###` finding heading.
- **Scope:** the 43 fields in 39 records named in `Build/worlds/lpc/Review-Artifacts/Readability_Rewrite_Map_2026-09-30.md`; the generator edits in `wb_lpc_s22.py`, `s24.py`, `s26.py`, `s28.py`. Records only; nothing was edited.
- **Standards read:** CLAUDE.md "Source fidelity" and "Accessible and rigorous"; `Build/reference/method/CiC_Register_Bar_2026-08-29.md`; the decision that a readability rewrite changes how a field reads and may not change what it says; Doc_02 section 7; Doc_04 section 3 and the section 6 interaction matrix.
- **Verdict:** 28 fields clear, 15 need a fix. 2 blocking (one field states a Doc_04 relation backwards; one honest-limit sentence now reads as a claim about an unread transcript), 11 substantial, 2 optional. Every proposed wording below was graded with `engine.m1.gates.grade_text` against the whole field and passes FK 10 / FRE 60. Several fields sit within one FRE point of the floor, so some fixes carry a small offsetting split. Each one is named.

## Gates and tools run directly

| Check | Result |
|---|---|
| Record fields against the map (own script: YAML front matter parsed at HEAD~2 and in the working tree, each named field compared after whitespace normalisation) | All 43 "Old" blocks equal the HEAD~2 field. All 43 "New" blocks equal the working-tree field |
| Only the named field changed (same script, every key compared) | True for all 39 records. Bodies unchanged. In the five `positions` lists only the named index differs |
| `python -m engine.m10.cli records lpc` | PASS |
| `python -m engine.m10.cli regate lpc` | PASS (175 new or edited fields; one pre-existing FRE finding on `lpc.demo.road-back-examined`, not a regression) |
| `python -m engine.m10.cli claims lpc` | PASS (110 derived, 110 registered). No claim sentence was reworded; the registered sentence in `gravity.penitential-discipline` is verbatim |
| Numbers, dates, section marks and Roman numerals, old against new (own script) | Identical in all 43 fields |
| Consumers read | `bridge_line`: `engine/m2/builders.py` `build_figures_json` then `engine/m4/name_bridge.py`, shown as its own paragraph in `cic-poc/frontend/src/components/FigureBridgeMark.tsx`. `tellable_as`: the story citation-card label (`engine/m4/citation_cards.py`), the story chunk head (`engine/m2/builders.py`), `engine/m2/site_compiler.py` `_resolve_story` |

## Per-field verdicts

| # | Field | Verdict | Severity | Finding |
|---|---|---|---|---|
| 1 | lpc.ambient.council-assembly-scale / detail | clear | — | — |
| 2 | lpc.ambient.two-cities-scale / detail | clear | — | — |
| 3 | lpc.contested.compel-coercion-development / claim | clear | — | — |
| 4 | lpc.contested.cyprian-death-genre / claim | fix | substantial | S1 |
| 5 | lpc.contested.de-unitate-recensions / claim | fix | substantial | S2 |
| 6 | lpc.contested.grace-pelagius-characterization / claim | fix | substantial | S3 |
| 7 | lpc.witness.answerability-as-ground / positions[1] | clear | — | — |
| 8 | lpc.witness.baptism-traced-to-the-apostles / positions[0] | clear | — | — |
| 9 | lpc.witness.communion-over-separation / positions[0] | clear | — | — |
| 10 | lpc.witness.communion-over-separation / positions[1] | clear | — | — |
| 11 | lpc.witness.communion-over-separation / text | clear | — | — |
| 12 | lpc.witness.confessor-claim-vs-regulated-peace / positions[1] | clear | — | — |
| 13 | lpc.witness.confessor-claim-vs-regulated-peace / text | fix | optional | O1 |
| 14 | lpc.witness.constantine-did-not-corrupt / text | clear | — | — |
| 15 | lpc.witness.marriage-a-threefold-good / positions[0] | clear | — | — |
| 16 | lpc.witness.tradition-tested-by-apostolic-warrant / text | clear | — | — |
| 17 | lpc.limit.411-gesta-unread / statement | fix | blocking | B2 |
| 18 | lpc.story.election-of-cyprian / tellable_as | clear | — | — |
| 19 | lpc.story.the-death-of-cyprian / tellable_as | fix | substantial | S10 |
| 20 | lpc.term.grace / plain_meaning | clear | — | — |
| 21 | lpc.term.preaching / quick_meaning | clear | — | N3 |
| 22 | lpc.figure.augustine / bridge_line | clear | — | — |
| 23 | lpc.figure.celerinus / bridge_line | clear | — | — |
| 24 | lpc.figure.cyprian / bridge_line | clear | — | — |
| 25 | lpc.figure.lucian / bridge_line | clear | — | — |
| 26 | lpc.figure.numidicus / bridge_line | clear | — | — |
| 27 | lpc.figure.pontius / bridge_line | clear | — | — |
| 28 | lpc.force.congregational-acclamation-overriding-preference / description | clear | — | N4 |
| 29 | lpc.force.decian-persecution-libelli-system / description | fix | substantial | S4 |
| 30 | lpc.force.donatist-schism / description | clear | — | — |
| 31 | lpc.force.inherited-latin-theological-vocabulary / description | clear | — | — |
| 32 | lpc.force.organized-carthaginian-church / description | clear | — | N2 |
| 33 | lpc.force.recurring-contest-failed-member / description | fix | substantial | S5 |
| 34 | lpc.force.standing-legal-condition-unlicensed-religion / description | clear | — | — |
| 35 | lpc.force.valerianic-persecution / description | clear | — | — |
| 36 | lpc.gravity.collegial-communion-preserved / description | fix | substantial | S6 |
| 37 | lpc.gravity.confessor-authority-vs-episcopal-peace / description | fix | substantial | S6 |
| 38 | lpc.gravity.pastoral-office-flock-keeping / description | fix | substantial | S6 |
| 39 | lpc.gravity.penitential-discipline / description | fix | substantial | S6, S9 |
| 40 | lpc.gravity.preaching-and-catechesis / description | fix | substantial | S6 |
| 41 | lpc.gravity.sacramental-ordination-validity / description | fix | blocking | B1, S6, S7, S8 |
| 42 | lpc.core.latin-pastoral-congregational-christianity / formation_logic | clear | — | N1, P1 |
| 43 | lpc.core.latin-pastoral-congregational-christianity / horizon | fix | optional | O2, N1 |

## Blocking findings

### B1. `gravity.sacramental-ordination-validity`: a Doc_04 relation now reads backwards

Old: "But penitential discipline relates to grace and human incapacity differently: it is reshaped by that concern, not continued in it." New: "That concern reshapes it, and does not continue in it." In the new sentence the subject of "does not continue" is grace. So it now says grace does not continue in penitential discipline. Doc_04 (Candidate 2, Interaction) says the reverse: penitential discipline is reshaped by grace and is not continued in it. This is a changed relation, not a changed reading.

Proposed wording (whole-field fix set with S6, S7, S8 and one offset; field then grades FK 7.25, FRE 60.41):

- "That concern reshapes it, and does not continue in it." becomes "It is reshaped by that concern, not continued in it."
- "It supports pastoral office, penitential discipline, collegial communion, and conciliar authority." becomes "It strengthens pastoral office, penitential discipline, collegial communion, and conciliar authority." (S6)
- "Penitential discipline supports this concern in the first phase." becomes "Penitential discipline strengthens this concern in the first phase." (S6)
- "The confessor tension asks a close question." becomes "The confessor tension asks a question close to this one." (S7; the next sentence, "Who may grant standing within the community?", stays)
- "That resemblance runs the other way, toward grace and human incapacity." becomes "That resemblance runs toward grace and human incapacity." (S8)
- Offset: "Both positions are solidly attested." becomes "Both positions are firmly attested." This also matches the other five gravity records, which the rewrite already moved to "firmly".

### B2. `limit.411-gesta-unread`: the honest limit now states what the unread transcript would show

Old: "What it would show about how our own bishops, beyond Cyprian and Augustine themselves, actually argued authority among themselves is not something we can tell you yet." New: "We cannot yet tell you what it would show. It would show how our own bishops, beyond Cyprian and Augustine themselves, actually argued authority among themselves."

The second new sentence is a flat claim about the contents of a transcript the record says has not been validly read. It follows a sentence that says we cannot tell. The honest limit's scope is what the record does not know. A readability rewrite may not turn the unknown part into a stated finding.

Proposed wording (field grades FK 8.72, FRE 61.35): replace the two sentences with "We cannot yet tell you what it would show about how our own bishops, beyond Cyprian and Augustine themselves, actually argued authority among themselves."

## Substantial findings

### S1. `contested.cyprian-death-genre`: "evidence" weakened to "proof"

Old: "rather than evidence the account itself cannot be trusted as testimony". New: "Neither is proof that we cannot trust the account as a witness's word." "Not proof" is a weaker claim than "not evidence". It leaves room for the framing to count as evidence against the account, which the claim denies. The claim's stance is the thing the record exists to state against its `held_against` entries, so its strength has to stay.

Proposed wording (field grades FK 6.48, FRE 61.22):

- "Neither is proof that we cannot trust the account as a witness's word." becomes "Neither is evidence that we cannot trust the account as a witness's word."
- Offset, which also brings the two scholarly labels in after their plain meaning as the Register Bar asks: "The account also casts events as echoes of Scripture (typology). It sees God's plan in them (providential framing)." becomes "The account also casts events as echoes of Scripture. This is called typology. It sees God's plan in them. This is called providential framing."

### S2. `contested.de-unitate-recensions`: "evidence" weakened to "proof"

Old: "not evidence of anything Cyprian himself wrote or revised". New: "It is no proof of what Cyprian himself wrote or revised." The same weakening as S1. The interpolation thesis this record states says the Primacy Text is not evidence at all.

Proposed wording (field grades FK 6.95, FRE 62.13):

- "It is no proof of what Cyprian himself wrote or revised." becomes "It is not evidence of anything Cyprian himself wrote or revised."
- Offset: "A later hand added it to Cyprian's own original words." becomes "A later hand added it to the words Cyprian first wrote." Same meaning; "original" survives as "first wrote".

Optional in the same field, no wording proposed: "reads more kindly toward Roman primacy" is an odd verb for a text's leaning. "More favourably" is the precise word, but it pushes this field under FRE 60 with the fix above. Leave it unless a later pass has room.

### S3. `contested.grace-pelagius-characterization`: "modern" narrowed to "again today"

Old: "the later Reformation-era and modern Catholic/Protestant use". New: "They did so in the Reformation era and again today." "Today" narrows "modern" to the present. "Again" adds a gap between two separate episodes, which the old text did not say.

The attribution itself is accurate. The old "Catholic/Protestant use" names the same two parties, and the record's own `held_against` speaks of "Reformation-era and later Catholic/Protestant appropriations". So "later Catholics and Protestants" is faithful.

Proposed wording (field grades FK 7.39, FRE 60.66): "They did so in the Reformation era and again today." becomes "They did so in the Reformation era and in modern times."

Optional in the same field, no wording proposed: "show what Pelagius himself held. They show it as it was." carries "accurately represents" faithfully, but the doubled sentence reads as filler. Every single-sentence form tried ("give an accurate account of", "show truly", "are true to") drops the field under FRE 60. It needs a wider pass on the field, not a word swap.

### S4. `force.decian-persecution-libelli-system`: "demanded" softened to "asked for"

Old: "It demanded a documented act of compliance." New: "It asked for a documented act of compliance." An imperial edict enforced on pain of death did not ask. This softens the force's central fact and flattens the world's sense of it ("a table emptied one certificate at a time").

Proposed wording (field grades FK 7.67, FRE 60.46):

- "It asked for a documented act of compliance." becomes "It demanded a documented act of compliance."
- Offset: "It worked through certificates recording that the holder had sacrificed." becomes "It worked through certificates. Each one recorded that the holder had sacrificed."

### S5. `force.recurring-contest-failed-member`: "ordinary sin" became "everyday sin"

Old: "over ordinary sin after baptism". New: "over everyday sin after baptism". In Augustine "everyday sin" names a specific class: the daily, lighter sins forgiven through the Lord's Prayer and almsgiving, distinct from grave sins that needed public penance. The old text, and its source (Doc_04 Candidate 2 quoting Doc_01 section 6, "ordinary sin and schism"), mean post-baptismal sin in general. The penitential-discipline gravity still says "the ordinary sin of catechized believers", so the two records now also disagree.

Proposed wording (field grades FK 7.70, FRE 61.47, unchanged): "everyday sin after baptism" becomes "ordinary sin after baptism".

### S6. Six gravity records: the Doc_04 relation "reinforces" became "supports"

"Reinforces" is the relation Doc_04 records in each candidate's Interaction test and in its section 6 matrix ("Reinforcing", "Competes", "Reshapes", "No demonstrated relationship"). "Supports" breaks that link. It also collides with the class name "Supporting" (Primary / Supporting / Tensional), which the same world uses. The core record's formation_logic says "Three more concerns support these" to mean the Supporting class. So "Conciliar authority supports it weakly" (conciliar authority is a Supporting gravity) and "Penitential discipline supports this concern" (a Primary gravity) can now be read as class statements. The untouched `gravity.grace-and-human-incapacity` still says "It reinforces preaching and catechesis", so the fleet of eight now uses two verbs for one relation.

"Reinforces" itself pushes three of the six fields under FRE 60 at their current margins. "Strengthens" keeps Doc_04's sense, does not collide with the class name, and passes in all six. The grace record may keep "reinforces"; the two verbs mean the same relation.

Proposed wording (each field graded whole):

- `gravity.collegial-communion-preserved` (FK 7.39, FRE 60.79): "It supports pastoral office, penitential discipline, conciliar authority, and sacramental validity." becomes "It strengthens pastoral office, penitential discipline, conciliar authority, and sacramental validity."
- `gravity.confessor-authority-vs-episcopal-peace` (FK 7.43, FRE 60.16): "It competes with penitential discipline and supports the pastoral office." becomes "It competes with penitential discipline and strengthens the pastoral office."
- `gravity.pastoral-office-flock-keeping` (FK 7.89, FRE 60.54): "It supports penitential discipline and collegial communion. It supports preaching and catechesis, sacramental validity, and the confessor tension. Conciliar authority supports it weakly." becomes "It strengthens penitential discipline and collegial communion. It strengthens preaching and catechesis, sacramental validity, and the confessor tension. Conciliar authority strengthens it weakly."
- `gravity.penitential-discipline` (with S9; FK 7.55, FRE 60.22): "It supports pastoral office, collegial communion, preaching and catechesis, and sacramental validity." becomes "It strengthens pastoral office, collegial communion, preaching and catechesis, and sacramental validity."
- `gravity.preaching-and-catechesis` (FK 7.85, FRE 60.18): "It supports pastoral office, penitential discipline, and grace and human incapacity." becomes "It strengthens pastoral office, penitential discipline, and grace and human incapacity."
- `gravity.sacramental-ordination-validity`: the two sentences are in B1's fix set.

### S7. `gravity.sacramental-ordination-validity`: "a closely related question" became "a close question"

Old: "The confessor tension is a closely related question about who may grant standing within the community." New: "The confessor tension asks a close question." In ordinary English "a close question" means a question that is hard to call. The meaning "closely related" is lost. Fix in B1's set: "The confessor tension asks a question close to this one."

### S8. `gravity.sacramental-ordination-validity`: "instead" became "the other way"

Old: "the second-phase family resemblance, which runs toward grace and human incapacity instead." New: "That resemblance runs the other way, toward grace and human incapacity." The same paragraph opens "That last link runs one way only". Right after it, "runs the other way" reads as the reverse direction of that link, which is not what the old text said. Fix in B1's set: "That resemblance runs toward grace and human incapacity." The previous sentence ("It does not depend on the second-phase family resemblance") already carries the contrast that "instead" gave.

### S9. `gravity.penitential-discipline`: "directly" dropped

Old: "Whether it continues into Augustine's phase was checked directly, not assumed. It holds directly for Cyprian's phase." New: "It holds in Cyprian's phase itself." "Directly" marks the first-phase hold as direct, against the qualified second-phase continuity the paragraph goes on to describe. It is a strength marker, and the rewrite had to keep every one.

Proposed wording (with S6; field grades FK 7.55, FRE 60.22): "It holds in Cyprian's phase itself." becomes "It holds directly for Cyprian's phase."

### S10. `story.the-death-of-cyprian`: the "remembered as" frame dropped

Old: "How our tradition remembered our first great bishop's death as a life fully given, completed". New: "How our tradition remembered the death of our first great bishop. It was a life fully given, completed."

The old line put the "life fully given, completed" reading inside the tradition's remembering. The new second sentence says it in the voice's own mouth, as fact. That matters here more than anywhere. The "death as completion of a formed life" is one of CF V7.4's own named markers of hagiographic narrative. `lpc.contested.cyprian-death-genre` exists because this story's tier is unresolved, and Doc_09 builds its tier judgement on naming Pontius's mediation rather than passing it off as plain narration. The story's own `text` opens the same way: "We offer it as that portrait, not as a report of what a bystander would have seen." The new label no longer keeps the frame its own story sets. The line is also the story's citation-card label, so it is the most visible form of the story.

Proposed wording (FK 7.19, FRE 61.33): "How our tradition remembered the death of our first great bishop. We remember it as a life fully given, completed."

## Optional findings

### O1. `witness.confessor-claim-vs-regulated-peace` / text: an unclear "he"

"That person had failed the test he himself had passed." Once the sentence is split off, "he himself" can be read as "that person", which contradicts the sentence. Proposed (FK 7.78, FRE 69.59): "That person had failed the test the survivor himself had passed."

### O2. `core` / horizon: two small ambiguities

"No one continuous institutional story across the century between them bounds it." "No one" first reads as "nobody". And "whether a rival consecration counted as a valid sacrament" adds "counted" (recognition by someone) where the old "sacramentally valid" spoke of validity itself. Proposed (both together, FK 7.82, FRE 60.24): "No single continuous institutional story across the century between them bounds it." and "whether a rival consecration was valid as a sacrament".

## Notes (fields marked clear; no fix required)

### N1. The "of Augustine" and "by Augustine" constructions have a tool cause

Eight places now read "On Baptism by Augustine argues", "the long, respectful argument of Augustine", "the sermon collection of Augustine", "Letters XXXI and CCXIII by Augustine himself", "the Sermons and Tractates on John by Augustine", "all of On Baptism by Augustine", "the death of Augustine", "The church of Augustine". Each is stiffer than the possessive it replaced. The cause is in `engine/m1/fk.py` `_count_syllables`: the silent-e rule skips words ending in "e's", so "Augustine" counts 3 syllables and "Augustine's" counts 4. Rewriting the possessive into a "by" phrase also adds a one-syllable word, which lowers syllables per word. The prose was written around a counting defect. The root fix is in the counter, not in these records. Once it is fixed, the possessives can come back with no FRE cost. This is registered here for the gate owner. It is not a finding against the rewrite, which met the gate as it stands.

### N2. `force.organized-carthaginian-church`, and the same phrase in the penitential and confessor gravities: "run by rule"

"A process of penance run by rule" keeps the meaning of "regulated process of penance". It reads a little stiff, and it loses the echo of the world's own phrase "the bishop's regulated peace", which the confessor gravity keeps two paragraphs later ("show the regulated answer"). Restoring "regulated" pushes each field under FRE 60 at its current margin, so no wording is proposed now.

### N3. `term.preaching` and `gravity.pastoral-office-flock-keeping`: "all else"

"Nearly all else we hold" and "the concern all else in this world turns on" lean slightly old-fashioned, which the Register Bar warns against. "Everything else" fails FRE 60 in both fields. No change proposed.

### N4. `force.congregational-acclamation-overriding-preference`: "were glad"

Possidius (Weiskotten 1919, Vita ch. VIII, lines 2136-2137 of the vendored file) reads "all who heard rejoiced and clamored". "Were glad" is a fair paraphrase in an etic description, but "rejoiced" is closer to the source. Restoring it takes the field to FRE 59.67. No change proposed. "Under compulsion and constraint" is kept verbatim, as the record's own source locus requires.

## The listed wording choices, one by one

| Choice | Finding |
|---|---|
| "reinforces" to "supports" (six gravity fields) | Not faithful. See S6 |
| "regulated process of penance" to "process of penance run by rule" | Meaning kept; stiff. N2 |
| "institution" to "the church as a whole" (sacramental gravity) | Faithful. The old sentence set the institution against "individual converts", and "the church as a whole" against "single converts" keeps that contrast. The donatist-schism force still says "the institution"; the two readings agree |
| "independent" to "each on his own" (sacramental gravity) | Faithful. In context "independent" means two separate authors each treating the question at length, not sources unaware of each other (Augustine argues directly with Cyprian). "Each on his own" says the same |
| "alternative recension" to "the other form" | Faithful. The contest is between two versions of chapters 4-5, and the record's `held_against` uses "recension" for exactly that |
| "directly quoted" to "quoted word for word" | Faithful. The project sense is a verbatim, re-verified quote record, which "word for word" names plainly |
| "solidly attested" to "firmly attested" (five places) | Faithful. Neither is a term in the five-level confidence vocabulary. The sacramental gravity alone kept "solidly"; B1's offset aligns it |
| "solicitation" to "request" (compel-coercion) | Faithful. The record's `concedes` still reads "narrow, unsuccessful solicitation of legal protection"; the two say the same thing |
| "later Catholics and Protestants" (grace-pelagius) | The attribution is accurate to the old claim ("Catholic/Protestant use") and to the record's own `held_against`. The time phrase is not: S3 |
| "corpus" to "writings"; "unaided" to "with no help" | Faithful. "Unaided" in this dispute means without grace, and "with no help" keeps that. "Unaided" is plain enough to have stayed |
| "genus clause" quotation (cyprian-death-genre) | Verbatim and unchanged |
| core swaps ("fiercely", "gives us", "will not let", "stance", "knows itself as", "tidy end") | Faithful. The core is emic, so "gives us" is the world's own "us". "Fiercely" keeps the heat of "ferociously" |

## Distinctiveness

The world's own images all survive: the table emptied one certificate at a time, the church with no door or no Master, the shepherd wounded in the flock, crisis turned into teaching, the bond it will not break, the road back walked before the people who watched you fall. The witness records still speak from inside, in the first person. No assistant cadence was added. Two places read as filler (S3's doubled "They show it as it was", noted as optional) or as rewriting around a counter (N1). In the gravities and forces, the many new short "It ..." sentences in a row read choppy in places (for example "It supports ... It supports ... Conciliar authority supports it weakly"). This is within the bar but at its edge.

## Bridge lines on the six figure records

The consumer shows `bridge_line` as its own paragraph in the name-bridge popover (`FigureBridgeMark.tsx`, Level 2 and Level 3). Nothing splices the line into a sentence after the name, so a lowercase lead phrase followed by a full sentence renders as written. The fleet already has both shapes: lowercase phrases in `alx` (for example `alx.figure.origen`) and capitalised full sentences in `cappadocian` (for example `cappadocian.figure.gregory-of-nyssa`). The six new lines read naturally there, and no fact moved. Clear.

## Silence scope and claim sentences (Doc_02 section 7)

The horizon's century-gap paragraph keeps its substance: a real silence in this world's own record, not a general lack of evidence, the century richly attested but almost entirely through Donatism's own sources. That matches Doc_02 section 7. No registered claim sentence changed (the claims gate derives 110, registers 110). The one silence-scope sentence whose substance did change is the 411 limit: B2.

## The generator strings

The four strings in `wb_lpc_s28.py` that carried older wording (two-cities "a century and a third apart"; communion-over-separation, positions[0] and text, "a century and a third later"; the 411 limit "other than our two anchor figures") now carry the records' wording. The map calls these "three" strings; there are four, in three records. The records are right and the old generator text was wrong: OG "A century and a third vs. a century and a half" (Open_Gaps_Tracking, the round that corrected nine instances) fixed 256 to c. 401 at about 145 years. The generator text for every field the map says a generator emits was confirmed present, and the fields the map says no generator emits (four witness records, the forces, gravities and core) were confirmed absent.

## Outside this rewrite's scope (for the world's gap log)

### P1. `core` / formation_logic still says "A century and a third later" for the 256 to c. 400 gap

"A century and a third later, Augustine argues at book length that Cyprian's ruling was wrong." This is the same interval that `witness.communion-over-separation` gives as "a century and a half later" for the same event. The earlier correction round named nine instances and missed this one. The readability rewrite rightly left it alone, since it may not change what a field says. It needs its own fact fix ("a century and a half later") and an Open_Gaps_Tracking entry. `gravity.sacramental-ordination-validity`'s "decades apart" is already logged (Open_Gaps_Tracking, the permanent-prompt interval entry of the B-7 review, 2026-09-30).

End of review.
