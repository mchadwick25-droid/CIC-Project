# Source-fidelity review, lpc, scope C (60 participant-facing fields)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), independent pass, 2026-10-24.
Scope file: `spoken_C.txt`. No repo file was modified.

Method. For each field, every sentence was read against the record's own `sources[].locus`. Most force and gravity loci say only "see this record's own body text", so those were checked against the construction documents they restate (`Doc_01`, `Doc_02`, `Doc_04`, `Doc_07`, `Doc_08`) and then against the vendored text itself. Every quotation was matched word for word in `cic/texts/`. Line numbers below are file lines.

Short file names used below:
- ANF05 = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`
- NPNF101 = `cic/texts/npnf101_augustine-confessions-letters.xml`
- NPNF104 = `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`
- NPNF105 = `cic/texts/npnf105_augustine-anti-pelagian-writings.xml`
- SENT = `cic/texts/cyprian_sententiae-episcoporum-lat_hartel1868-csel3-tei.txt`
- CTH = `cic/texts/codex-theodosianus_latinlibrary.txt`

Severity: **P1** = invented or unsupported detail, claim wider than its source, misattribution, contested point stated as settled, quotation not word for word, or a governing rule that contradicts the sources. **P2** = loose paraphrase that is not wrong, a missing locus, or a stale statement about the build.

---

## ambient

### lpc.ambient.council-assembly-scale — `detail`

**C-1 · P1 · claim wider than source; invented detail**
- Sentences: "eighty-seven bishops gathered in one place to give their own sentence ... one after another, each in his own words." / "That many men, in one room, on one day, each expected to speak for himself rather than be spoken for."
- Problem: Not all of them gathered, and not all spoke for themselves. Natalis of Oea speaks for himself and for two absent bishops, Pompeius of Sabrata and Dioga of Leptis Magna, "corpore quidem absentes, spiritu praesentes". So "each expected to speak for himself rather than be spoken for" is contradicted by the text it cites. "In one room" is not in the source, which says only "in unum Cartaginem conuenissent". The source does say that presbyters, deacons and most of the people were also there.
- Evidence: SENT:107-110 (preface, "kalendis Septembribus", presbyters, deacons, "plebis maxima parte"); SENT:138-141 ("singuli quid sentiamus proferamus neminem iudicantes"); SENT:1473-1478 (Natalis speaking for the two absent bishops).
- Proposed text: "In September of 256, bishops from three provinces met at Carthage on the rebaptism question. Their record holds eighty-seven sentences, given one after another. Each bishop said what he judged. Two who could not come sent their vote with a colleague. Presbyters, deacons and most of the people were there to hear it."

### lpc.ambient.two-cities-scale — `detail`

**C-2 · P2 · locus does not carry the claim; loose wording**
- Sentence: "the largest Latin Christian city outside the empire's own capital in the west."
- Problem: The first cited locus is the 256 council. That text says nothing about the size of the city. The claim restates `Doc_01` line 34 ("the most populous and consequential Latin Christian city outside Rome itself"), which gives no primary locus. "The empire's own capital in the west" is also unclear for 391–430, when the western court sat at Milan and Ravenna. `Doc_01` and world_core `horizon` both say "Rome".
- Evidence: `Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md:34`; SENT:107-110.
- Proposed text: "The first is a great port city, the largest Latin Christian city outside Rome." Also correct the locus so it cites `Doc_01` §2 rather than the council.

### lpc.ambient.church-administrative-objects — `detail`

**C-3 · P2 · loose subject**
- Sentence: "One church we know entrusted the care of its own building and property to the more capable of its own clergy, in turn."
- Problem: In Possidius it is the bishop who does this: "he assigned and entrusted in turn to the more capable clergy." The rest of the field follows the text closely.
- Evidence: `cic/texts/possidius_vita-augustini_weiskotten1919.txt:3459-3466`.
- Proposed text: "In one church we know, the bishop handed the care of its building and property to the more capable of his clergy, in turn."

---

## world_core — lpc.core.latin-pastoral-congregational-christianity

### `cautions`

**C-4 · P1 · governing rule forbids Documented material; contested point not labelled (confirms OG-57 N10, and N9)**
- Sentences: "The century gap (258-391) is Donatism's territory, not this world's. Never describe what happened in those years from this world's own collection. Its few texts from those years, such as Optatus's polemic, the council canons and imperial law, record events but are not this world's own pastoral voice, so far as assessed."
- Problem: Read literally, the rule bars the *Confessions* on 386–391. That covers Augustine's conversion, his baptism at Milan in 387 and his seizure into the presbyterate in 391, all Documented. The same record cites the *Confessions* as a source, and `lpc.limit.ordinary-interior-life` quotes it on the 387 baptism. "Few texts" that "record events" leaves out Augustine's own writings of 386–391, which `Doc_02` §7 lists: the *Soliloquies* (row 25) and *On the Morals* (row 22). The sentence also does not call the silence Contested, and it runs past 25 words.
- Evidence: `Build/worlds/lpc/Open_Gaps_Tracking.md:1792-1793` (N9, N10); `Doc_02_Source_Ecology.md:122` (§7: the silence means "no surviving voice continuous with Cyprian's ordinary-pastoral mode"; the list "is not exhaustive"); NPNF101:13731-13732 (Confessions IX.vi.14).
- Proposed text: "2) From Cyprian's death in 258 to Augustine's ordination in 391, this world's own pastoral voice is silent, so far as this build has assessed (Contested; nine tractatus in Morin 1917 are not yet assessed). Never fill those years from the Donatist world's record. Augustine's own account of his life from 386 to 391 is this world's own, and may be told. Other texts from those years, such as Optatus's polemic, council canons and imperial law, are not this world's pastoral voice. The Donatist schism is one of the historical pressures on this world. How to speak of Donatism as an opponent is governed by a separate rule. It is never this world's own voice to borrow."

**C-5 · P1 · factual errors in a governing caution**
- Sentences: "These are three different years under different emperors, easily collapsed into one another. The graded schedule of silver fines aimed at Donatists in XVI.5.52 belongs to the Donatist world, not this one."
- Problem: (a) XVI.5.52's graded schedule is in **gold**: *auri pondo* 50, 40, 30, 20 and 5 by rank. Only the Circumcellions are fined in silver, *argenti pondo decem*. (b) The three items are not under three different emperors. XVI.5.52 (412) is issued under Honorius and Theodosius II. Honorius was emperor in 401 and is already a co-issuer of XVI.5.21 (392). The 401 item is a council, not an imperial act. (c) Only NPNF's editorial endnote dates that council to 401. Letter 185 itself gives no date, and `Doc_01` line 162 says so.
- Evidence: CTH:7095-7096 (XVI.5.21, "denis libris auri", 392 iun. 15); CTH:7185-7195 (XVI.5.52, "auri pondo ... circumcelliones argenti pondo decem", "ravennae honorio viiii et theodosio v aa. conss.", 412 ian. 30); NPNF104:19628-19632 (endnote "Carthage ... 401").
- Proposed text: "5) Two imperial laws are easily confused. The fine at Codex Theodosianus XVI.5.21 (392) is not the same provision as XVI.5.52 (412). Between them falls the council that Letter 185, section 25, records. An editor's note dates it to 401. Keep the three apart. The graded schedule of fines aimed at Donatists in XVI.5.52, in gold by rank, belongs to the Donatist world, not this one."

### `horizon`

**C-6 · P2 · silence not scoped to the finding it restates**
- Sentences: "The century between the two bishops (258-391) is a silence in this world's own record." / "That century is richly attested, but almost entirely through sources that belong to Donatism, not to this world's own surviving voice."
- Problem: The field does qualify the silence ("what this build has read so far", "open to doubt"), but it never names the Contested level. "A silence in this world's own record" is also wider than the `Doc_02` §7 finding, which is the absence of a *pastoral* voice. The world's own record does cover 386–391. "Sources that belong to Donatism" reads as Donatist authorship, but Optatus, the main source, is Catholic. `Doc_02` says "Donatism's territory".
- Evidence: `Doc_02_Source_Ecology.md:122, 128`.
- Proposed text: "The century between the two bishops (258-391) is a silence in this world's own pastoral voice. That holds for what this build has read so far, and the claim is Contested. [Morin sentences unchanged.] It is not a general lack of evidence about the period. That century is richly attested, but mostly through sources this build places in the Donatist world, not in this world's own surviving voice."

### `formation_logic`

**C-7 · P2 · loose interval**
- Sentence: "A century and a third later, Augustine argues at book length that Cyprian's ruling was wrong."
- Problem: The council was in 256 and *On Baptism* is c. 400, about 144 years later. "A century and a third" (133) is the separate 258–391 span, so the phrase blurs two different numbers.
- Evidence: NPNF104:10756ff (On Baptism); SENT:107.
- Proposed text: "Nearly a century and a half later, Augustine argues at book length that Cyprian's ruling was wrong."

### `thinness`

**C-8 · P2 · stale statement about the build**
- Sentence: "We have not yet read the rites themselves as evidence in their own right."
- Problem: The rites were read as liturgical evidence in September 2026. `Doc_05` and `Doc_07` simply do not draw on those readings.
- Evidence: `Doc_05_Ecological_Reconstruction.md:377`; `Doc_07_Integrated_Ecology_Analysis.md:252`.
- Proposed text: "The rites have been read once as evidence in their own right, but this account does not yet draw on that reading."

(The thinness field's own silence sentence is correctly marked Contested.)

---

## voice_craft — lpc.craft.datus-voice

### `characteristic_concerns[1]`

**C-9 · P1 · governing rule contradicts the source**
- Sentence: "It is never withheld forever either."
- Problem: Cyprian and his council decided that people who did not repent, and asked for peace only when sickness and danger came, "are to be absolutely restrained from the hope of communion and peace." As written, this rule would have Datus deny a Documented refusal.
- Evidence: ANF05:33961-33969 (Ep. LI §23).
- Proposed text: "whether a road back is real. It must be examined and walked in the open. It is never granted on request. It is never withheld forever from one who truly walks it."

### `flavor_notes[reasoning-opening].note`

**C-10 · P2 · loose**
- Sentence: "He argues against someone who actually disagrees, inside a bond neither will break."
- Problem: This is true of Augustine and Cyprian's memory. It is not true of the Donatists, who stood outside communion, or of Pelagius's party, which the African councils condemned. As a standing voice note it could lead Datus to describe every opponent as a colleague still in communion.
- Evidence: NPNF104:19623-19632; `npnf214_seven-ecumenical-councils.xml:36430-36445` (African Code canon CIX, 418, anathemas).
- Proposed text: "He argues against someone who actually disagrees. Where the other is a colleague, he argues inside a bond neither will break."

---

## demonstration

### lpc.demo.compel-three-phase — `exchange[representative].text`

**C-11 · P1 · misattribution; contested point stated as settled**
- Sentences: "At first he held that no one should ever be forced into the church -- only argument, never compulsion." / "Later he asked a magistrate for a narrow measure against a rival clergy ..." / "What moved between his first stand and his last was real -- we do not pretend it was nothing."
- Problem: (a) In Letter 185 §25, "certain of the brethren, of whom I was one" carried the point in council. The measure was to be sought "from the emperors", and envoys went "to the court". Augustine did not ask a magistrate. (b) The first stage is known only from Augustine's later account in Letter XCIII §17. The record's own divergence_note, `lpc.contested.compel-coercion-development` and `lpc.term.compel-them-to-come-in` all leave open whether the sequence was a genuine change of mind or a later self-presentation. "At first he held", stated flatly, together with "was real", settles that question.
- Evidence: NPNF104:19623-19632 (Letter 185 §25-26); NPNF101:38245-38256 (Letter XCIII §17).
- Proposed text: "Not exactly the shape of it. In our later years, one of our own voices moved across a hard question in three stages, and we report all three. By his own later account, he first held that no one should be forced into the church. Argument only, never compulsion. Later, he and his colleagues in council asked the emperors for a narrow measure. It would fine rival clergy only where our own people had suffered violence. It was not even granted. Later still, he defended a fuller compulsion at length. He tells it as a change of mind. We report it as he tells it."

### lpc.demo.compel-three-phase — `exchange[representative].text#2`

**C-12 · P1 · claim wider than source**
- Sentences: "What changed his mind was not one argument answering another. It was watching whole towns cross over to us under the weight of the law ..."
- Problem: Augustine says he "yielded to the evidence afforded by these instances which my colleagues have laid before me." He saw one case himself, his own town. The others "were mentioned to me by name". He was persuaded by instances his colleagues pointed to, not mainly by watching towns change.
- Evidence: NPNF101:38245-38262.
- Proposed text: "We do not say it was self-evidently right, and we do not disown it either. What changed his mind, he says, was not his opponents' words. It was cases his colleagues set before him. The first was his own town. It had once stood wholly with the other side. Fear of the emperors' laws brought it back to the one communion, and it stayed. Many other towns were named to him. That is what persuaded him, by his own account. We hold that position honestly, as his own, argued at real length. We are not ashamed to name it, and we do not ask you simply to accept it from us."

### lpc.demo.font-twice-answered — `exchange[representative].text`

**C-13 · P2 · loose; puts the opponent's framing in Cyprian's mouth**
- Sentence: "One of us held that nothing valid is given outside at all, so we bring the person to the water again."
- Problem: Cyprian rejected the word "again". In his view those who come from heretics "are not rebaptized among us, but are baptized", because what they received outside was no baptism.
- Evidence: ANF05:38184 (Ep. LXX, to Quintus: "not re-baptized among us, but are baptized"); SENT:115-119.
- Proposed text: "One of us held that nothing valid is given outside at all. So the person comes to the water in the church, and is baptized for the first time."

### lpc.demo.road-back-examined — `exchange[representative].text`

**C-14 · P1 · invented purpose**
- Sentence: "Their name is set down. Not hidden, not quietly forgotten -- set down, so the congregation knows exactly who is walking this road and why."
- Problem: The cited locus, Epistle X, asks the confessors to name each person in their certificates. The reason is to stop vague requests like "Let such a one be received to communion along with his friends", and to name only those "whose penitence you see to be very near to full satisfaction". Nothing there says the name was set down so that the congregation would know. That purpose is invented.
- Evidence: ANF05:29935-29954 (Ep. X §4).
- Proposed text: "Their name is set down. Not a vague 'this man and his friends', but one person, by name, whose change someone has actually seen."

---

## force

### lpc.force.augustine-engagement-cyprian-conciliar-acts — `description`

**C-15 · P1 · contested claim stated as settled**
- Sentence: "No other force carries as much of the world's formation logic across its 133-year silence between the two phases."
- Problem: The silence is stated as fact, with no Contested label and no "so far as assessed".
- Evidence: `Doc_02_Source_Ecology.md:122, 128`; `Open_Gaps_Tracking.md:1763-1765` (OG-54).
- Proposed text: "No other force carries as much of the world's formation logic across the 133 years between the two phases, which this build has assessed as a silence in the world's pastoral voice (Contested)."

**C-16 · P2 · loose**
- Sentence: "Augustine read, argued with, and overturned the ruling on rebaptism made by Cyprian's council of 256."
- Problem: Augustine argues that Cyprian's ruling was wrong. But he attributes its correction to a later plenary council of the whole church ("the earlier are often corrected by those which follow them"), not to himself.
- Evidence: NPNF104:11303.
- Proposed text: "Augustine read the ruling on rebaptism made by Cyprian's council of 256, and argued at length that it was wrong."

### lpc.force.corpus-outliving-the-world — `description`

**C-17 · P1 · claim wider than source**
- Sentence: "At the end, Augustine went back through everything he had written and corrected it, in the Retractationes"
- Problem: The *Retractationes* review his books "praeter epistulas et sermones", that is, not his letters and sermons. He meant to go on to those, but did not.
- Evidence: `cic/texts/augustine_retractationes-lat_knoll-csel36.txt:89-92` (Knoll, Praefatio); 13731 ("antequam epistulas et sermones").
- Proposed text: "At the end, Augustine went back through his books one by one and corrected them, in the Retractationes. He did not reach his letters and sermons. Our own corpus holds no English translation of that work."

**C-18 · P2 · loose**
- Sentence: "Cyprian gathered and forwarded his own letters as a body of work."
- Problem: What he sent to Rome was thirteen letters, to give an account of what he had done in the crisis. It was a dossier, not a collected body of work.
- Evidence: ANF05:30188-30190 (Ep. XIV §2).
- Proposed text: "Cyprian gathered thirteen of his own letters and sent them to Rome, to give account of what he had done."

### lpc.force.decian-persecution-libelli-system — `description`

**C-19 · P2 · missing locus**
- Sentence: "Tertullian, in On Modesty, already tells of sinners who ask imprisoned martyrs for peace."
- Problem: The sentence is supported, but neither `sources[]` nor the body cites it. This matters because world_core Caution 3 treats Tertullian as a named comparandum.
- Evidence: `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml` (De Pudicitia ch. 22, around 9570-9602).
- Proposed fix: add a locus for De Pudicitia 22 as comparandum evidence. No text change.

### lpc.force.donatist-schism — `description`

**C-20 · P2 · could mislead**
- Sentence: "It tested, at its hardest edge, whether communion could hold despite disagreement, and communion held."
- Problem: The sentence restates `Doc_08` line 135 ("G3 holds"). But a participant will read "communion held" as communion with the Donatists, which was broken by the schism itself.
- Evidence: `Doc_08_Forces_Document.md:135`.
- Proposed text: "It tested, at its hardest edge, whether disagreement had to become separation. Augustine's answer to Cyprian shows it did not."

### lpc.force.illegal-to-established-shift — `description`

**C-21 · P2 · loose**
- Sentence: "a century and a third later, the magistrate could be asked, and eventually was."
- Problem: Letter 185 §25 says the measure was sought "from the emperors", by envoys sent to the court.
- Evidence: NPNF104:19623-19632.
- Proposed text: "a century and a third later, the emperors could be asked, and eventually were."

### lpc.force.inherited-latin-theological-vocabulary — `description`

**C-22 · P1 · claim contradicted by a vendored text of this world**
- Sentences: "what had to be argued could be argued in the language the people in the assembly already spoke." / "since that depends on a theological language in the people's own tongue, able to carry the content."
- Problem: Augustine himself says that a lack of Punic "greatly hindered" the preaching of the gospel in the Hippo region. He looked for a Punic-speaking presbyter to serve as bishop at Fussala. Latin was not the tongue of every assembly. These lines also clash with the world's own thin_topics on the Punic and Berber substrate.
- Evidence: NPNF101:35996-36000 (Letter LXXXIV); NPNF101:54466-54469 (Letter CCIX §3).
- Proposed text: "The words were already to hand. What had to be argued could be argued in Latin, the church's own language of preaching. Where people spoke only Punic, Augustine says, preaching was greatly hindered." Then: "This made preaching and catechesis possible as the main way of forming people, since that depends on a theological language able to carry the content."

### lpc.force.organized-carthaginian-church — `description`

**C-23 · P2 · no primary locus**
- Sentence: "It could also call councils of dozens of bishops at short notice."
- Problem: "At short notice" restates `Doc_01` line 126 and `Doc_08` line 75, but no primary passage supports it. The 256 council met on a fixed date after an exchange of letters.
- Evidence: `Doc_01_World_Identification_Boundaries_Orientation.md:126`; SENT:107-115.
- Proposed text: "It could also call councils of dozens of bishops."

**C-24 · P2 · loose**
- Sentence: "And it supplied the council setting where both formulas of conciliar authority were eventually spoken."
- Problem: Only "bishop of bishops" was spoken in council, in 256. Augustine's "plenary Councils" formula is written in a treatise.
- Evidence: SENT:138-141; NPNF104:11303.
- Proposed text: "And it supplied the councils that both formulas of conciliar authority are about."

### lpc.force.transmission-institutionally-dominant-side — `description`

**C-25 · P1 · claim wider than source; contradicts this world's own records**
- Sentences: "In his own time or later, each man stood on the institutionally dominant side of every dispute he joined. That side was eventually the canonized one."
- Problem: On rebaptism, his most famous dispute, Cyprian's side did not become the canonized one. Augustine argues that the ruling was wrong and was corrected by a plenary council. This world's own `lpc.force.augustine-engagement-cyprian-conciliar-acts` and `lpc.demo.font-twice-answered` say so. The sentence restates `Doc_02` §6 (quoted at `Doc_08` line 198), and that finding is too broad as well.
- Evidence: NPNF104:11303; ANF05:56866-56873.
- Proposed text: "The writings of both Cyprian and Augustine survive in unusually full form. Both were kept by the church that later became the canonical one. That church kept Cyprian even where it judged him wrong, on rebaptism."

### lpc.force.vandal-invasion-siege-of-hippo — `description`

**C-26 · P2 · missing locus**
- Sentence: "The Vandals crossed from Spain in 429."
- Problem: The only source is Prosper. Prosper's crossing entry ("Gens Wandalorum ab Hispania ad Africam transit") is not tied to 429 in this record, and the vendored file's year mapping was not shown. The 28 August 430 death date is verified ("V. kl. Sept.").
- Evidence: `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt:54126`; file header line 9.
- Proposed fix: cite the year mapping for entry 1295, or a source that gives 429. No text change if one is cited.

---

## gravity

### lpc.gravity.collegial-communion-preserved — `description`

**C-27 · P1 · claim wider than source**
- Sentences: "Neither breaks fellowship over the sharpest doctrinal disputes in the record. Neither bishop's writings hold a single counter-example."
- Problem: The grace dispute is one of this world's sharpest doctrinal disputes. In it, the African council of 418 anathematized the Pelagian positions. Its canons stand in the African Code, which the world_core cites. Julian of Eclanum, a bishop, was deposed over the dispute, and Augustine wrote against him at length. The sentence restates `Doc_04` line 60, but holds only for rebaptism and Cyprian's memory.
- Evidence: `cic/texts/npnf214_seven-ecumenical-councils.xml:36430-36445` (canon CIX, Carthage 418, "let him be anathema"); NPNF105:942, 1530 (Julian deposed; NPNF editor's account).
- Proposed text: "Over rebaptism, the sharpest dispute between them, neither breaks fellowship with a fellow bishop. The grace dispute ran differently: African councils condemned the Pelagian teaching."

### lpc.gravity.confessor-authority-vs-episcopal-peace — `description`

**C-28 · P2 · missing locus**
- Sentence: "Tertullian, in On Modesty, already tells of sinners who ask confessors for peace."
- Problem: As C-19.
- Proposed fix: add the De Pudicitia 22 locus.

### lpc.gravity.grace-and-human-incapacity — `description`

**C-29 · P1 · contested point stated as settled**
- Sentence: "In them Augustine refuses the Pelagian claim that a believer's own moral effort is enough without grace."
- Problem: Whether this was Pelagius's own position is exactly what `lpc.contested.grace-pelagius-characterization` holds open. The sentence gives Augustine's account of it as the Pelagian claim itself.
- Evidence: `records/lpc/contested_claim/lpc.contested.grace-pelagius-characterization.md` (held_against 1, concedes).
- Proposed text: "In them Augustine refuses a claim he sets out as the Pelagian one: that a believer's own moral effort is enough without grace. Whether Pelagius himself held it in that form is disputed."

### lpc.gravity.pastoral-office-flock-keeping — `description`

**C-30 · P2 · stale statement about the build**
- Sentences: "Possidius's Life of Augustine is not counted. It has not been checked on its own, beyond naming the Megalius consecration."
- Problem: Possidius has since been read in full, and other records cite chapters IV, VIII and XXIV verified at source.
- Evidence: world_core sources ("whole work, read in full"); `lpc.force.congregational-acclamation-overriding-preference` locus (ch. VIII, lines 2142-2143); `Doc_01` line 26 (`Possidius_Full_Read_2026-09-16.md`).
- Proposed text: "Possidius's Life of Augustine is not counted in this rating, though it has since been read in full."

**C-31 · P2 · loose**
- Sentence: "It recurs without a break in every primary source, for both bishops and both phases."
- Problem: "Without a break" sits badly with the 258–391 silence that the world's other records name.
- Proposed text: "It recurs in every primary source, for both bishops and both phases."

### lpc.gravity.preaching-and-catechesis — `description`

**C-32 · P2 · loose**
- Sentence: "It depends on a shared vernacular to teach in: the inherited Latin theological vocabulary."
- Problem: As C-22. Latin was not everyone's vernacular (Letter LXXXIV).
- Proposed text: "It depends on a shared language to teach in: the inherited Latin theological vocabulary."

### lpc.gravity.sacramental-ordination-validity — `description`

**C-33 · P2 · loose interval**
- Sentence: "Two separate bishops argue it at length, decades apart."
- Problem: The interval is about 145 years (256 to c. 400).
- Proposed text: "Two separate bishops argue it at length, more than a century apart."

**C-34 · P2 · loose**
- Sentence: "It explains the whole break between Stephen and Cyprian."
- Problem: Whether there was a formal break of communion is not established in the vendored sources, and the world's own collegial-communion record says neither side broke fellowship.
- Proposed text: "It explains the whole dispute between Stephen and Cyprian."

---

## honest_limit

### lpc.limit.apostolic-origin-undefended — `statement`

**C-35 · P1 · contradicts the source it cites**
- Sentence: "We believe each bishop holds the whole office, not a share."
- Problem: De Unitate 5 says the opposite of "not a share": "The episcopate is one, each part of which is held by each one for the whole" (*cuius a singulis in solidum pars tenetur*).
- Evidence: ANF05:42288-42291; `cic/texts/cyprian_de-unitate-ecclesiae-catholicae-lat_hartel1868-csel3-tei.txt:339`.
- Proposed text: "We believe the office of bishop is one. Each bishop holds his part of it for the whole."

### lpc.limit.ordinary-interior-life — `statement`

**C-36 · P1 · unsupported detail**
- Sentence: "... about the single most examined conversion in the ancient world."
- Problem: This is an evaluative superlative from reception history. No cited source supports it. The quotation itself ("how greatly did I weep in Thy hymns and canticles") is word for word (NPNF101:13731-13732).
- Proposed text: "But he wrote that down years afterward, already a bishop, about a conversion he examined at book length."

### lpc.limit.rural-punic-berber-life — `statement`

**C-37 · P2 · loose**
- Sentence: "the language ordinary people spoke there before they ever learned the one we were taught in"
- Problem: "Before they ever learned" implies that rural speakers later learned Latin. That is not in any source. Letter LXXXIV shows Punic-only speakers in the Hippo region itself.
- Evidence: NPNF101:35996-36000.
- Proposed text: "the language many ordinary people spoke there, which was not the one we were taught in"

### lpc.limit.the-silent-century — `statement`

**C-38 · P2 · loose**
- Sentence: "Something like a hundred and thirty years sit between the bishop who opens our own record and the one who closes it."
- Problem: The 130 years run from Cyprian's death to Augustine's ordination, not from one bishop to the other. The qualification ("as far as we have yet weighed") is present and correct.
- Proposed text: "Something like a hundred and thirty years sit between the death of the bishop who opens our record and the ordination of the one who closes it."

### lpc.limit.womens-own-voice — `statement`

**C-39 · P2 · missing loci**
- Sentences: the Numidicus sentence and the Quartillosia sentences.
- Problem: Both are verified, but neither is cited. Numidicus is in ANF05 Ep. XXXIV (32095-32110), not Ep. XX–XXI. Quartillosia is in the *Passio Montani et Lucii* VIII ("cuius mulieris et maritus et filius ante triduum passi erant"), at `cic/texts/acta-martyrum-selecta_gebhardt1902.txt:7094-7104`.
- Proposed fix: add both loci. No text change.

**C-40 · P2 · loose**
- Sentence: "a woman we know as Albina, and a community of nuns at Hippo, are known to us only through one of our own bishop's letters about them."
- Problem: Letters CXXVI and CCXI are addressed *to* Albina and *to* the nuns (NPNF101:44459, 54736).
- Proposed text: "are known to us only through one of our own bishop's letters to them and about them."

---

## Fields checked clean (27)

- contested_claim: `lpc.contested.compel-coercion-development` claim; `lpc.contested.cyprian-death-genre` claim (the CF V7.4 Tier 1 quote is word for word with marked ellipses, scratchpad `CiC_L3B_Formation_World_Construction_Framework_V7.4.txt:253`); `lpc.contested.de-unitate-recensions` claim; `lpc.contested.grace-pelagius-characterization` claim.
- voice_craft: `identity`; `guard`; `characteristic_concerns[0]`; `characteristic_concerns[2]`; `flavor_notes[consistency-pressure].note`; `flavor_notes[imagery].note`; `flavor_notes[grief-and-vigilance].note`.
- demonstration: `lpc.demo.font-twice-answered` text#2; `lpc.demo.road-back-examined` text#2.
- force: `confessors-claim-to-grant-peace` ("thousands of certificates ...", ANF05:30204; the "confessor" count of 20 across npnf101–108 reproduced); `congregational-acclamation-overriding-preference` (ANF05:32372-32373; ANF05:27818-27820; Possidius 2130-2143); `manichaeism-and-pelagian-anthropology`; `plague-of-cyprian`; `recurring-contest-failed-member`; `standing-legal-condition-unlicensed-religion`; `transmission-asymmetric-span-133-year-silence` (silence qualified and marked Contested); `valerianic-persecution`.
- gravity: `conciliar-authority-theory` ("plenary" counted 31 times in On Baptism, NPNF104:10756-15292; quotes match); `penitential-discipline`.
- honest_limit: `411-gesta-unread`; `no-chain-of-witnesses` (City of God XXII.5, "who state and write that they witnessed it", npnf102:45386); `the-lapsed-own-account`; `the-outsiders-own-view` (Ad Demetrianum; Constantine passage at NPNF104:17721, a paraphrase without quote marks, faithful).

Quotations verified word for word within scope, all clean: the "judging no man ..." quote (ANF05:56870-56871); "bishop of bishops ... own proper right of judgment" (ANF05:56872-56876); "[E]ven of the plenary Councils ..." (NPNF104:11303); "the authority of plenary Councils"; "[I]t is the shepherd that is chiefly wounded ..." (ANF05:43727); "your suffrage and God's judgment" and "ancient venom" (ANF05:32372-32373); Pontius's "by the judgment of God and the favour of the people ..." (ANF05:27818-27820); "these thirteen letters ..." (ANF05:30188-30189); "writing and the matter, and even the paper itself ..." (ANF05:28930-28932, Cyprian's own Ep. III); Testimonies III.4 "we must boast in nothing, since nothing is our own" (ANF05:53423; quoted by Augustine at NPNF105:20912); "how greatly did I weep in Thy hymns and canticles" (NPNF101:13731); "thousands of certificates were daily given, contrary to the law of the Gospel" (ANF05:30204). The Retractationes phrases "with a certain judicial severity" and "as with a censor's pen" are the build's own English for Latin at `augustine_retractationes-lat_knoll-csel36.txt:1512-1513`. They are faithful renderings. No English translation is vendored.

## Counts

- Fields in scope: 60. Clean: 27. With at least one finding: 33.
- Findings: 40 in all. **P1: 15**. **P2: 25**.
- P1 list: C-1, C-4, C-5, C-9, C-11, C-12, C-14, C-15, C-17, C-22, C-25, C-27, C-29, C-35, C-36.
- Every site in scope that states the 258–391 silence was checked. Correctly qualified: thinness, the 133-year force, the-silent-century. Unqualified: augustine-engagement force (C-15) and Caution 2 (C-4). Qualified but not labelled Contested and wider than the pastoral-voice finding: horizon (C-6).
