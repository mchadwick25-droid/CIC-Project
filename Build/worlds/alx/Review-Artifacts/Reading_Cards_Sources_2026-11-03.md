# Reading cards for alx: source-check table (V7, Spec V4b)

Review artifact for the Opus reviewer of the 35 alx reading cards (26 quotes, 9 stories). For each card, each line maps to the exact source and locus, or the construction-document section, that the line was drafted from. File line numbers refer to the vendored files in `cic/texts/`: anf02 = `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, anf04 = `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, anf06 = `anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml`, anf09 = `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`, npnf201 = `npnf201_eusebius-church-history-life-of-constantine.xml`, npnf203 = `npnf203_theodoret-jerome-gennadius-rufinus.xml`, npnf204 = `npnf204_athanasius-select-works-letters.xml`, npnf214 = `npnf214_seven-ecumenical-councils.xml`; Philocalia = `origen_philocalia_lewis1911.txt`; Palladius = `palladius_lausiac-history_clarke1918.txt`. Construction documents are under `Build/worlds/alx/`.

Written blind: the author did not open the V7 Set, any graded-run answers or reviews. Cards were written for every alx quote and story.

## Notes for the reviewer

- **Lines omitted for lack of a source:** one. `alx.quote.the-grades-here-in-the-church` has no `open` line; the only qualification available (the passage says nothing about how the offices worked) is already carried by `whose_view`, and no contested-claim, honest-limit or divergence note bears on the passage. No `complicated_by` is given where no record genuinely qualifies the passage (17 cards).
- **`reads_differently_today` on stories** rewrites the record's `modern_contrast`: story records carry no `modern_lens_note`, and `modern_contrast` is their modern-lens field.
- **`historians_conclude` sources.** Where the construction documents give a confidence level for the point, the card uses it. Four lines rest on the vendored editions' own scholarly apparatus instead (McGiffert's NPNF2 vol. 1 notes; Robertson's NPNF2 vol. 4 notes and prolegomena), named in the line. Judgement calls to check: `dionysius-too-high-for-me-to-grasp` tags McGiffert's motive argument *Inferential-Thin* (one 1890 editor inferring motive; no construction document rates it); `clement-possessions` tags Doc_05 §5's "care as ministry" *Widely Accepted* (Doc_05 gives Widely Accepted to the school-tradition formation channels in that section's construction note, not to care-as-ministry by name); `demetrius-accused-him-bitterly` tags *Contested* following Doc_05 §4's rating of the Origen-Demetrius particulars, while `alx.story.origen-demetrius` tags *Widely Accepted* because its line is about the structural conflict (Doc_08 3B-1).
- **Findings against existing record fields, outside this card's licence (not edited; spec V4b allows the `reading_card` field only):**
  1. `alx.quote.dionysius-too-high-for-me-to-grasp` `use_note.not_for` says the stylistic authorship argument "precedes this passage"; in the vendored text it follows it (HE VII.25.6-8, npnf201 lines 41431-41460). Its `modern_lens_note` ("a critical result he has just proved") has the same order problem. The card states the order as the text has it.
  2. `alx.quote.no-festal-letter-was-written` `modern_lens_note` says the Festal Letter "went out every year. This year it did not". The edition prints fragments of a Letter XXIX for 357 with the note "If these fragments are authentic, the statement in the Index, that this year no letter could be sent, is an error" (npnf204 line 68615). The card's `open` line carries it.
  3. `alx.story.leonides-martyrdom` `modern_contrast` says the record presents the boy's zeal "as PREVENTED, not admired"; Eusebius both credits Providence for preventing it and praises the letter as "the first evidence of Origen's youthful wisdom" (HE VI.2.4-6, npnf201 lines 32540-32565). The card's `open` line carries both.
  4. `alx.quote.athanasius-death-trampled-down` and `alx.quote.athanasius-made-god` come from On the Incarnation, which `alx.source.athanasius-de-incarnatione` dates in or shortly before 318, before Nicaea. The cards do not attach the post-Nicene reconfiguration (Doc_05 §7) to these passages.
  5. `alx.quote.dionysius-plague` and `alx.story.plague-nursing` call the letter a festal letter of c. 260; McGiffert dates it shortly before Easter 263 and says it "does not seem to have been a regular festal epistle so-called" (npnf201 lines 41020-41030). The cards' `open` lines carry the edition's dating.
  6. `alx.story.potamiaena`: Palladius, Lausiac History III (Palladius file lines 205-207), tells a different Potamiaena account (a slave handed over by her master, under 'Maximianus'), noted in McGiffert's headnote to HE VI.5. The card's `open` line carries it.
- **Word counts** use the gate's own counter (`engine/m1/gates.py` `reading_card_texts`, `_WORD`); every card is at or under 120.

## Per-card source table

### `alx.quote.a-doctrine-they-would-not-have-taught`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-contra-celsum, record body (written in Caesarea, c. 248); Contra Celsum II.55-56, anf04 lines 41560-41593 |
| `source_says` | alx.source.origen-contra-celsum, Contra Celsum II.56, anf04 lines 41560-41600 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §7 (Ongoing external forces); Doc_05_Ecological_Reconstruction.md §5 (Forces) |
| `contributes` | alx.term.anastasis; Doc_05_Ecological_Reconstruction.md §5 (Forces) |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.1 (Origen: systemic author-gravity risk; later work in Caesarea) |
| `open` | alx.quote.a-doctrine-they-would-not-have-taught, use_note.not_for |
| `reads_differently_today` | alx.quote.a-doctrine-they-would-not-have-taught, modern_lens_note |

### `alx.quote.appointed-by-the-fathers-to-be-read`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.athanasius-festal-letters; Letter XXXIX heading (For 367), npnf204 lines 68711-68716 |
| `source_says` | alx.source.athanasius-festal-letters, Letter XXXIX §§2-7, npnf204 lines 68745-68830 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.3 (Athanasius: must not characterize the pre-Nicene period); Doc_05_Ecological_Reconstruction.md §7 construction note |
| `contributes` | alx.gravity.scripture-formative (manifestation: Letter 39's canon list); alx.term.katechesis |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.3 (perspective episcopal, not the community describing itself); alx.force.post-nicene-authority-shift |
| `open` | Letter XXXIX §2, npnf204 lines 68745-68755; alx.source.athanasius-festal-letters, work field (an extract, not the whole letter) |
| `reads_differently_today` | alx.quote.appointed-by-the-fathers-to-be-read, modern_lens_note |
| `complicated_by` | alx.quote.dionysius-too-high-for-me-to-grasp (record ids; resolve under the gate) |

### `alx.quote.athanasius-death-trampled-down`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.athanasius-de-incarnatione, work field (composed in or shortly before 318, per the NPNF editor) |
| `source_says` | alx.source.athanasius-de-incarnatione, On the Incarnation §§28-29, npnf204 lines 17405-17460 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Lexicon-Chunks/alexlex019_resurrection.md, Key Sources note |
| `contributes` | alx.term.anastasis; alx.term.thanatos |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.3; Doc_05_Ecological_Reconstruction.md §7 construction note |
| `open` | alx.quote.athanasius-death-trampled-down, use_note.not_for |
| `reads_differently_today` | alx.quote.athanasius-death-trampled-down, modern_lens_note |

### `alx.quote.athanasius-fountains`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.athanasius-festal-letters; Letter XXXIX heading (For 367), npnf204 lines 68711-68716 |
| `source_says` | alx.source.athanasius-festal-letters, Letter XXXIX §§4-6, npnf204 lines 68780-68815 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.3; Doc_05_Ecological_Reconstruction.md §7 construction note |
| `contributes` | alx.gravity.scripture-formative; alx.force.scripture-ongoing |
| `whose_view` | alx.force.post-nicene-authority-shift; alx.quote.athanasius-fountains, use_note.not_for |
| `open` | alx.source.athanasius-festal-letters, Letter XXXIX §7, npnf204 lines 68816-68822 |
| `reads_differently_today` | alx.quote.athanasius-fountains, modern_lens_note |
| `complicated_by` | alx.quote.appointed-by-the-fathers-to-be-read, alx.quote.dionysius-too-high-for-me-to-grasp (record ids; resolve under the gate) |

### `alx.quote.athanasius-made-god`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.athanasius-de-incarnatione, work field; On the Incarnation §54, npnf204 line 18725 |
| `source_says` | alx.source.athanasius-de-incarnatione, On the Incarnation §54, npnf204 lines 18725-18760 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §2 (D-B Theosis as Horizon) and §4 table; Robertson's endnote 347, npnf204 line 18744 |
| `contributes` | alx.gravity.soul-transformation; alx.term.theosis |
| `whose_view` | Build/worlds/alx/Doc_04_Gravity_Discovery.md §2 (D-B: attested in Clement, Origen, Athanasius) |
| `open` | alx.contested.ecology-wide-primacy |
| `reads_differently_today` | alx.quote.athanasius-made-god, modern_lens_note |

### `alx.quote.clement-bee`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-stromateis, Stromateis I.1, anf02 lines 27476-27483 |
| `source_says` | alx.source.clement-stromateis, Stromateis I.1, anf02 lines 27483-27500 |
| `historians_conclude` [confidence: Contested] | anf02 editor's note at line 27489 ('Most likely Pantaenus'); alx.contested.didaskaleion-institution; Build/worlds/alx/Doc_01_World_Identification_Boundaries_Orientation.md §1.2 |
| `contributes` | alx.term.didaskalos; alx.gravity.learning-formation |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 (Clement: representativeness partial) |
| `open` | alx.contested.didaskaleion-institution, held_against |
| `reads_differently_today` | alx.quote.clement-bee, modern_lens_note |
| `complicated_by` | alx.contested.didaskaleion-institution (record ids; resolve under the gate) |

### `alx.quote.clement-instructor`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-paidagogos; Build/worlds/alx/Doc_02_Source_Ecology.md §2 Stream 2 (Paedagogus explicitly catechetical) |
| `source_says` | alx.source.clement-paidagogos, Paedagogus I.2, anf02 lines 18768-18795 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C3 Divine Pedagogy: core Widely Accepted); alx.gravity.divine-pedagogy body (Origen's systematic form DMR) |
| `contributes` | alx.gravity.divine-pedagogy; alx.term.paideia |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 |
| `open` | alx.contested.ecology-wide-primacy |
| `reads_differently_today` | alx.quote.clement-instructor, modern_lens_note |

### `alx.quote.clement-new-song`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-protrepticus, work field (Exhortation to the Heathen) |
| `source_says` | alx.source.clement-protrepticus, Protrepticus I, anf02 lines 15168-15220 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C4: function Widely Accepted; cosmology DMR); alx.gravity.logos-unity body |
| `contributes` | alx.gravity.logos-unity; alx.term.logos |
| `whose_view` | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C4: literate-attested) |
| `open` | Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §6.4 (Boundary Ecology) |
| `reads_differently_today` | alx.quote.clement-new-song, modern_lens_note |

### `alx.quote.clement-possessions`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-quis-dives, work field; Quis Dives Salvetur 14-16, anf02 lines 56500-56520 |
| `source_says` | alx.source.clement-quis-dives, Quis Dives Salvetur 14-15, anf02 lines 56500-56535 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §5 (Care as ministry) and its construction note |
| `contributes` | alx.gravity.soul-transformation; alx.term.agape |
| `whose_view` | alx.quote.clement-possessions, use_note.not_for; Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 |
| `open` | alx.limit.faith-alone-later-frame, statement and sources (Quis Dives 27-29) |
| `reads_differently_today` | alx.quote.clement-possessions, modern_lens_note |
| `complicated_by` | alx.limit.faith-alone-later-frame, alx.quote.couches-and-trenchers-and-bowls (record ids; resolve under the gate) |

### `alx.quote.clement-rash-martyrdom`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-stromateis, Stromateis IV.4, anf02 lines 37795-37805 |
| `source_says` | alx.source.clement-stromateis, Stromateis IV.4, anf02 lines 37812-37827 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (T4); Doc_05_Ecological_Reconstruction.md §5 (Martyrdom as formation) |
| `contributes` | alx.term.martys; alx.gravity.martyrdom-contemplative-tension |
| `whose_view` | alx.gravity.martyrdom-contemplative-tension, description; Build/worlds/alx/Doc_09_Story_Inventory.md §3 (the martyr's own interior) |
| `open` | alx.quote.clement-rash-martyrdom, use_note.not_for |
| `reads_differently_today` | alx.quote.clement-rash-martyrdom, modern_lens_note |
| `complicated_by` | alx.story.leonides-martyrdom (record ids; resolve under the gate) |

### `alx.quote.clement-schoolmaster`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-stromateis, Stromateis I.5 chapter heading, anf02 line 27876 |
| `source_says` | alx.source.clement-stromateis, Stromateis I.5, anf02 lines 27877-27895 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 (Influence), §3.5 and §4 (van den Hoek 1988) |
| `contributes` | alx.force.philonic-inheritance; alx.force.platonic-environment |
| `whose_view` | alx.limit.faith-alone-later-frame, why_sources_cannot_answer (Stromateis I.9); Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 (Limitations) |
| `open` | anf02 editor's note at line 27873 |
| `reads_differently_today` | alx.quote.clement-schoolmaster, modern_lens_note |

### `alx.quote.couches-and-trenchers-and-bowls`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-paidagogos, Paedagogus II.3 heading, anf02 line 22104 |
| `source_says` | alx.source.clement-paidagogos, Paedagogus II.3, anf02 lines 22105-22150 |
| `historians_conclude` [confidence: Documented] | alx.limit.material-remains, why_sources_cannot_answer; Build/worlds/alx/Doc_02_Source_Ecology.md §8 |
| `contributes` | alx.gravity.soul-transformation; alx.term.oikos |
| `whose_view` | alx.quote.couches-and-trenchers-and-bowls, use_note.not_for; Build/worlds/alx/Doc_02_Source_Ecology.md §3.2 |
| `open` | alx.quote.couches-and-trenchers-and-bowls, use_note.not_for |
| `reads_differently_today` | alx.quote.couches-and-trenchers-and-bowls, modern_lens_note |
| `complicated_by` | alx.limit.material-remains (record ids; resolve under the gate) |

### `alx.quote.demetrius-accused-him-bitterly`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica; Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Eusebius: writes decades after Origen) |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VI.8.3-5, npnf201 lines 33210-33233 |
| `historians_conclude` [confidence: Contested] | McGiffert, NPNF2 vol. 1, Note 16 'Origen and Demetrius', npnf201 lines 51969-52090; Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §4 construction note |
| `contributes` | alx.gravity.teacher-bishop-tension; alx.force.origen-demetrius-conflict |
| `whose_view` | alx.story.origen-demetrius, absent_detail; Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 |
| `open` | alx.story.origen-demetrius, absent_detail; alx.quote.demetrius-accused-him-bitterly, use_note.not_for |
| `reads_differently_today` | alx.quote.demetrius-accused-him-bitterly, modern_lens_note |
| `complicated_by` | alx.story.origen-demetrius (record ids; resolve under the gate) |

### `alx.quote.dionysius-nepos`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.1-3, npnf201 lines 41285-41300 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.1-5, npnf201 lines 41285-41330 |
| `historians_conclude` [confidence: Contested] | alx.contested.allegory-from-within, concedes; Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §6.4 construction note |
| `contributes` | alx.term.allegoria; alx.gravity.scripture-formative |
| `whose_view` | npnf201 editor's note at line ~41297 ('This work of Nepos has entirely perished'); alx.story.arsinoite-conference, absent_detail |
| `open` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Dionysius: doubly mediated); npnf201 endnote at line 41310 |
| `reads_differently_today` | alx.quote.dionysius-nepos, modern_lens_note |
| `complicated_by` | alx.contested.allegory-from-within (record ids; resolve under the gate) |

### `alx.quote.dionysius-plague`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VII.22.1, npnf201 lines 41017-41030 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VII.22.6-10, npnf201 lines 41058-41110 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Eusebius: lower risk for verbatim quotation of documents); alx.source.eusebius-historia-ecclesiastica, work field |
| `contributes` | alx.term.martys; alx.term.agape |
| `whose_view` | alx.quote.dionysius-plague, use_note.not_for; alx.story.plague-nursing, absent_detail |
| `open` | McGiffert's note to HE VII.22.1, npnf201 lines 41020-41030; alx.story.plague-nursing, absent_detail |
| `reads_differently_today` | alx.quote.dionysius-plague, modern_lens_note |

### `alx.quote.dionysius-too-high-for-me-to-grasp`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.3 and VII.25.1, npnf201 lines 41300-41305, 41386-41390 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VII.25.1-5, npnf201 lines 41388-41430 |
| `historians_conclude` [confidence: Inferential-Thin] | McGiffert's note to HE III.24.18, npnf201 lines 17713-17745 |
| `contributes` | alx.gravity.scripture-formative; alx.force.scripture-ongoing |
| `whose_view` | alx.source.eusebius-historia-ecclesiastica, HE VII.25.1-4, npnf201 lines 41390-41420 |
| `open` | alx.source.eusebius-historia-ecclesiastica, HE VII.25.6-8, npnf201 lines 41431-41460; alx.quote.dionysius-too-high-for-me-to-grasp, use_note.not_for (treatise lost) |
| `reads_differently_today` | alx.quote.dionysius-too-high-for-me-to-grasp, modern_lens_note |
| `complicated_by` | alx.quote.athanasius-fountains (record ids; resolve under the gate) |

### `alx.quote.ecclesiastical-and-apostolical-tradition`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-de-principiis, work field (English of Rufinus's Latin) |
| `source_says` | alx.source.origen-de-principiis, De Principiis preface 2-3, anf04 lines 22419-22453 |
| `historians_conclude` [confidence: Contested] | alx.contested.origen-positions, held_against; Build/worlds/alx/Doc_02_Source_Ecology.md §4 (named live debate) |
| `contributes` | alx.term.kanon-pisteos; alx.gravity.speculative-doctrinal-tension |
| `whose_view` | Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §4 (inheritance and unease) |
| `open` | alx.source.origen-de-principiis, work field and body (transmission caveat) |
| `reads_differently_today` | alx.quote.ecclesiastical-and-apostolical-tradition, modern_lens_note |
| `complicated_by` | alx.contested.origen-positions (record ids; resolve under the gate) |

### `alx.quote.gregory-spark`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.gregory-address-to-origen, work field; anf06 editor's introduction, lines 631-632 |
| `source_says` | alx.source.gregory-address-to-origen, Address VI, anf06 lines 2985-3025 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Gregory) and §5 item 1 |
| `contributes` | alx.gravity.learning-formation; alx.term.didaskalos |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (one gifted pupil); alx.quote.gregory-spark, use_note.not_for |
| `open` | alx.source.gregory-address-to-origen, confidence.divergence_note; alx.gravity.learning-formation, description |
| `reads_differently_today` | alx.quote.gregory-spark, modern_lens_note |

### `alx.quote.no-festal-letter-was-written`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.athanasius-festal-letters; Festal Index XXIX, npnf204 lines 64360-64370 |
| `source_says` | alx.source.athanasius-festal-letters, Festal Index XXIX-XXX, npnf204 lines 64362-64376 |
| `historians_conclude` [confidence: Widely Accepted] | Robertson, NPNF2 vol. 4 Prolegomena, npnf204 lines 6028-6036 |
| `contributes` | alx.term.episkopos; alx.force.post-nicene-authority-shift; alx.force.arian-controversy |
| `whose_view` | alx.quote.no-festal-letter-was-written, use_note.not_for |
| `open` | Editor's note to Letter XXIX, npnf204 line 68615 |
| `reads_differently_today` | alx.quote.no-festal-letter-was-written, modern_lens_note |

### `alx.quote.no-sun-no-moon-no-sky`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-de-principiis, De Principiis IV.1, anf04 |
| `source_says` | alx.source.origen-de-principiis, De Principiis IV.1.15-16, anf04 lines 33683-33740 |
| `historians_conclude` [confidence: Dominant Modern Reconstruction] | alx.gravity.scripture-formative, body (systematized method Origen-concentrated, caps at DMR); Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C1) |
| `contributes` | alx.term.allegoria; alx.term.interpretation |
| `whose_view` | alx.quote.no-sun-no-moon-no-sky, use_note.not_for; alx.contested.allegory-from-within, held_against |
| `open` | alx.source.origen-de-principiis, De Principiis IV.1.19, anf04 line 33869; work field (Rufinus) |
| `reads_differently_today` | alx.quote.no-sun-no-moon-no-sky, modern_lens_note |
| `complicated_by` | alx.contested.allegory-from-within, alx.story.arsinoite-conference (record ids; resolve under the gate) |

### `alx.quote.origen-gospel-firstfruits`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-comm-john; Commentary on John I.4, anf09 lines 20455-20464; editor's note, anf09 line 24426 |
| `source_says` | alx.source.origen-comm-john, Commentary on John I.6, anf09 lines 20560-20582 |
| `historians_conclude` [confidence: Widely Accepted] | alx.gravity.logos-unity, manifestations; Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C4) |
| `contributes` | alx.force.johannine-logos; alx.gravity.logos-unity |
| `whose_view` | alx.quote.origen-gospel-firstfruits, use_note.not_for |
| `open` | alx.source.origen-comm-john, work field |
| `reads_differently_today` | alx.quote.origen-gospel-firstfruits, modern_lens_note |

### `alx.quote.origen-punishment-heals`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-philocalia, author field; Philocalia XXVII heading, file line 432 |
| `source_says` | alx.source.origen-philocalia, Philocalia XXVII.2-7, file lines 433-436 |
| `historians_conclude` [confidence: Contested] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (Restoration: restorative conviction WA, separable from Apokatastasis); alx.term.apokatastasis, plain_meaning |
| `contributes` | alx.gravity.divine-pedagogy; alx.term.restoration |
| `whose_view` | alx.quote.origen-punishment-heals, use_note.not_for; alx.source.origen-philocalia, body (compiled c. 358-378) |
| `open` | alx.contested.origen-positions; alx.term.apokatastasis |
| `reads_differently_today` | alx.quote.origen-punishment-heals, modern_lens_note |
| `complicated_by` | alx.contested.origen-positions (record ids; resolve under the gate) |

### `alx.quote.origen-scripture-senses`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.origen-philocalia, work field; Philocalia I, file line 76 |
| `source_says` | alx.source.origen-philocalia, Philocalia I.11-13, file lines 76-78 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (C1); alx.contested.ecology-wide-primacy |
| `contributes` | alx.gravity.scripture-formative; alx.term.interpretation |
| `whose_view` | alx.gravity.scripture-formative, body (systematized method Origen-concentrated); Build/worlds/alx/Doc_02_Source_Ecology.md §3.1 |
| `open` | alx.contested.allegory-from-within; Philocalia I.8-9, file lines 73-74 |
| `reads_differently_today` | alx.quote.origen-scripture-senses, modern_lens_note |
| `complicated_by` | alx.contested.allegory-from-within (record ids; resolve under the gate) |

### `alx.quote.the-grades-here-in-the-church`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-stromateis, Stromateis VI.13, anf02 lines 47860-47895 |
| `source_says` | alx.source.clement-stromateis, Stromateis VI.13, anf02 lines 47866-47900 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_04_Gravity_Discovery.md §4 table (T1: Widely Accepted structural); Doc_05_Ecological_Reconstruction.md §4 |
| `contributes` | alx.term.episkopos |
| `whose_view` | alx.quote.the-grades-here-in-the-church, use_note.not_for; Stromateis VI.13, anf02 line 47889 |
| `reads_differently_today` | alx.quote.the-grades-here-in-the-church, modern_lens_note |

### `alx.quote.timothy-ordinary-questions`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.alexandrian-canonical-answers, author field; Canonical Answers heading, npnf214 lines 44104-44109 |
| `source_says` | alx.source.alexandrian-canonical-answers, Timothy, Questions I, VIII, X, XI, npnf214 from line 44104 |
| `historians_conclude` [confidence: Dominant Modern Reconstruction] | Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §2 construction note |
| `contributes` | alx.gravity.learning-community-tension; alx.term.photismos; alx.term.fasting |
| `whose_view` | alx.quote.timothy-ordinary-questions, use_note.not_for; alx.source.alexandrian-canonical-answers, body |
| `open` | alx.source.alexandrian-canonical-answers, body (what it is not); alx.limit.f5-women-own-words |
| `reads_differently_today` | alx.quote.timothy-ordinary-questions, modern_lens_note |
| `complicated_by` | alx.limit.f5-women-own-words (record ids; resolve under the gate) |

### `alx.quote.to-believe-or-disbelieve`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-stromateis, Stromateis IV.24 heading, anf02 line 40326 |
| `source_says` | alx.source.clement-stromateis, Stromateis IV.24, anf02 lines 40327-40340 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Lexicon-Chunks/alexlex013_freedom-autexousia.md, Quick Meaning; alx.term.autexousia, confidence |
| `contributes` | alx.term.autexousia; alx.term.pistis |
| `whose_view` | alx.source.clement-stromateis, Stromateis IV.24, anf02 lines 40336-40340 |
| `open` | alx.quote.to-believe-or-disbelieve, use_note.not_for |
| `reads_differently_today` | alx.quote.to-believe-or-disbelieve, modern_lens_note |

### `alx.story.arsinoite-conference`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.3, 6, npnf201 lines 41300-41345 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.6-9, npnf201 lines 41335-41382 |
| `historians_conclude` [confidence: Contested] | alx.contested.allegory-from-within, concedes; Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §6.4 construction note |
| `contributes` | alx.term.allegoria (evidential sense); alx.gravity.scripture-formative |
| `whose_view` | alx.story.arsinoite-conference, absent_detail |
| `open` | alx.source.eusebius-historia-ecclesiastica, HE VII.24.6, npnf201 lines 41336-41345 |
| `reads_differently_today` | alx.story.arsinoite-conference, modern_contrast |
| `complicated_by` | alx.contested.allegory-from-within (record ids; resolve under the gate) |

### `alx.story.didymus-meeting`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.palladius-lausiac-history, author field; Lausiac History IV, file line 211 |
| `source_says` | alx.source.palladius-lausiac-history, Lausiac History IV.1-2, file line 211 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.4 (Representativeness / social location) |
| `contributes` | alx.term.didaskalos; alx.gravity.teacher-bishop-tension |
| `whose_view` | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Palladius) and §5 item 3 |
| `open` | alx.story.didymus-meeting, absent_detail |
| `reads_differently_today` | alx.story.didymus-meeting, modern_contrast |

### `alx.story.gregory-formation`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.gregory-address-to-origen; anf06 editor's introduction, lines 631-632; alx.story.gregory-formation body (five years, Pontus) |
| `source_says` | alx.source.gregory-address-to-origen, Address VI-IX, XIII, anf06 from line 2288; alx.gravity.learning-formation, sources |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_09_Story_Inventory.md §2 (alexstory001); Doc_02_Source_Ecology.md §3.6 |
| `contributes` | alx.gravity.learning-formation; alx.term.didaskalos |
| `whose_view` | alx.story.gregory-formation, absent_detail; Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 |
| `open` | alx.source.gregory-address-to-origen, confidence.divergence_note; alx.story.gregory-formation, absent_detail |
| `reads_differently_today` | alx.story.gregory-formation, modern_contrast |

### `alx.story.john-young-robber`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.clement-quis-dives, Quis Dives Salvetur 42, anf02 lines 57244-57247 |
| `source_says` | alx.source.clement-quis-dives, Quis Dives Salvetur 41-42, anf02 lines 57225-57247 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_09_Story_Inventory.md §1 (tier cross-walk) and §2 (Tier 2 definition) |
| `contributes` | alx.term.lapsi; alx.term.metanoia |
| `whose_view` | alx.story.john-young-robber, narrative_tier_justification |
| `open` | alx.story.john-young-robber, absent_detail; anf02 footnote at line 57257 |
| `reads_differently_today` | alx.story.john-young-robber, modern_contrast |

### `alx.story.leonides-martyrdom`

| Line | Source / locus used |
|---|---|
| `setting` | alx.story.leonides-martyrdom, narrative_tier_justification; Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VI.2.2-6, npnf201 lines 32520-32565 |
| `historians_conclude` [confidence: Contested] | Build/worlds/alx/Doc_09_Story_Inventory.md §2 (alexstory003); Doc_08_Forces_Document.md 2A-3 |
| `contributes` | alx.force.persecution; alx.gravity.martyrdom-contemplative-tension |
| `whose_view` | alx.source.eusebius-historia-ecclesiastica, HE VI.2.1, npnf201 lines 32514-32518 |
| `open` | alx.source.eusebius-historia-ecclesiastica, HE VI.2.4-6 and McGiffert's note, npnf201 lines 32545-32565; alx.story.leonides-martyrdom, absent_detail |
| `reads_differently_today` | alx.story.leonides-martyrdom, modern_contrast |
| `complicated_by` | alx.quote.clement-rash-martyrdom, alx.limit.f5-women-own-words (record ids; resolve under the gate) |

### `alx.story.origen-daring-deed`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VI.8.1, npnf201 lines 33135-33142 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VI.8.1-5, npnf201 lines 33195-33233 |
| `historians_conclude` [confidence: Contested] | McGiffert's note to HE VI.8.1, npnf201 lines 33142-33150; alx.story.origen-daring-deed, confidence.divergence_note |
| `contributes` | alx.gravity.teacher-bishop-tension; alx.force.origen-demetrius-conflict |
| `whose_view` | alx.story.origen-daring-deed, absent_detail; HE VI.8.1, npnf201 lines 33139-33142 |
| `open` | alx.story.origen-daring-deed, absent_detail; McGiffert's note, npnf201 lines 33180-33190 |
| `reads_differently_today` | alx.story.origen-daring-deed, modern_contrast |

### `alx.story.origen-demetrius`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VI.8, VI.23, VI.26 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VI.8.4 and VI.26, npnf201 lines 33218-33224, 36325-36335 |
| `historians_conclude` [confidence: Widely Accepted] | Build/worlds/alx/Doc_08_Forces_Document.md 3B-1; McGiffert, Note 16 'Origen and Demetrius', npnf201 lines 52014-52060 |
| `contributes` | alx.gravity.teacher-bishop-tension; alx.gravity.learning-formation; alx.force.origen-demetrius-conflict |
| `whose_view` | alx.story.origen-demetrius, absent_detail |
| `open` | alx.story.origen-demetrius, absent_detail; Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §4 construction note |
| `reads_differently_today` | alx.story.origen-demetrius, modern_contrast |
| `complicated_by` | alx.quote.demetrius-accused-him-bitterly (record ids; resolve under the gate) |

### `alx.story.plague-nursing`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VII.22.1, npnf201 lines 41017-41030 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VII.22.4-10, npnf201 lines 41047-41110 |
| `historians_conclude` [confidence: Documented] | Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Eusebius: lower risk for verbatim quotation of documents) |
| `contributes` | alx.term.martys; alx.term.agape |
| `whose_view` | alx.story.plague-nursing, absent_detail |
| `open` | McGiffert's note to HE VII.22.1, npnf201 lines 41020-41030; alx.story.plague-nursing, absent_detail |
| `reads_differently_today` | alx.story.plague-nursing, modern_contrast |

### `alx.story.potamiaena`

| Line | Source / locus used |
|---|---|
| `setting` | alx.source.eusebius-historia-ecclesiastica, HE VI.5.1, npnf201 lines 32950-32958 |
| `source_says` | alx.source.eusebius-historia-ecclesiastica, HE VI.5.1-6, npnf201 lines 32950-32990 |
| `historians_conclude` [confidence: Dominant Modern Reconstruction] | Build/worlds/alx/Doc_05_Ecological_Reconstruction.md §6.5 construction note; Doc_09_Story_Inventory.md §1 (Tier 3 cross-walk) |
| `contributes` | alx.term.martys; alx.gravity.martyrdom-contemplative-tension |
| `whose_view` | alx.limit.f5-women-own-words, why_sources_cannot_answer; alx.story.potamiaena, absent_detail |
| `open` | alx.source.palladius-lausiac-history, Lausiac History III, file lines 205-207; McGiffert's note to HE VI.5, npnf201 lines 32925-32945 |
| `reads_differently_today` | alx.story.potamiaena, modern_contrast |
| `complicated_by` | alx.limit.f5-women-own-words (record ids; resolve under the gate) |

