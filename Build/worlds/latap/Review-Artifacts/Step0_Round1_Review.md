# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 1 Independent Adversarial Review

**Reviewed documents:**
- `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (Atlas I.35, drafted 2026-09-10, commit `98ec3d32`)
- `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` (Atlas I.43, drafted 2026-09-10, commit `98ec3d32`)

**Reviewer:** independent isolated agent, no drafting involvement. Scope extended beyond ordinary review by the commissioning instruction to run a full Era 1 sweep (§C below), which neither document performed.

**Overall verdicts:**
- **I.35 (Second-Century Greek Apologists): SUBSTANTIAL REVISION REQUIRED**
- **I.43 (Latin Apologists): SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**A note on method, since both drafts assert checks they did not run.** Every factual claim below was re-derived directly against the repository — `records/<world>/` read file-by-file, `cic/corpus-map/*.yaml` read in full for every entry named, `cic-website/data/world-census.json` filtered and string-tested for the passages presented as quotation, and the vendored XML in `cic/texts/` parsed and word-counted with `lxml`. Where a draft says "directly verified" or "independently verified," this review states what the underlying artifact actually contains. Nothing here is accepted from either draft's own summary of what it found.

**Working-tree note.** The commissioning brief located both drafts in this worktree; they were not present at `HEAD` (`5eb39472`). They were found on `_review/apologists` / `candidate-worlds-step0-apologists` at `98ec3d32` and fast-forwarded into this worktree before review. No content was altered.

---

## Part A — Findings against I.35, The Second-Century Greek Apologists

### A1. [HIGH] B3's built-world sweep claims no overlap where the largest one in the repository sits: Tatian is a built figure in the Syriac world, and the *Address to the Greeks* is one of that world's own load-bearing source records

**Claimed** (§3 B3, third bullet): *"Versus the other six built worlds (Desert, PAHC as above, Hieronymian, Syriac, Imperial-Juridical, Cappadocian): no figure or source overlap found in this pass."* B1 lists *Tatian's Address* among this candidate's vendored core, and the Section B conclusion falls back on "Athenagoras, Theophilus, Tatian (with his own caveat), and Aristides alone" should the Justin ruling go against the candidate.

**Found.** `records/syr/` carries:
- `syr.figure.tatian.md` — a full figure record, `evidentiary_weight: corroborating`, `formation_confidence: Widely Accepted`, `bridge_line: "the man who wove the four Gospels into the one story these churches read for two hundred years"`;
- `syr.source.tatian-address-to-greeks.md` — a source record for **the exact work I.35 names**, `evidentiary_weight: load-bearing`, `verification_state: verified-direct`, with two passages verified to file line (ch. XLII at 7460, ch. XXIX at 6972);
- two quote records built on it (`syr.quote.tatian-born-assyrian`, `syr.quote.tatian-barbaric-writings`), plus `syr.gravity.diatessaron-normative`, `syr.force.diatessaron-adoption`, `syr.term.ewangeliyon-da-mhallete`, and a naming in `syr.core.syriac.md`.

The source record's own text states the world's claim on him in terms that leave no room for "no overlap found": *"AND IT SETTLES THE CLAIM THIS WORLD MAKES ON HIM. Every argument for Tatian belonging to the Syriac East runs through the statement that he was an Assyrian."*

This is not a subtle find. `cic/corpus-map/greek-apologists-second-century.yaml` — the candidate's own corpus map — carries the adjacency in the *Address*'s own note: *"Tatian sits awkwardly across two entries... later returned east and claimed as a forefather by the Syriac tradition, which the syr world already reaches through his Diatessaron in anf09... Mark may want a ruling on where his voice sits."* The *Address* is triple-assigned in the corpus map — `post-apostolic-house-church`, `greek-apologists-second-century`, `syriac-edessa-nisibis` — a fact readable in one grep.

**Consequence.** The draft names one binding pre-Doc_01 ruling (Justin) and builds its Tier-1 conditional on a fallback roster that includes Tatian. A second figure-boundary of the same kind, against a *built and live* world, sits inside that fallback. B3 does not survive as written, and the §3 conclusion ("this candidate's B1/B2 case weakens somewhat... but very likely still clears Tier 1 on Athenagoras, Theophilus, Tatian... and Aristides alone") is unsupported until the Tatian boundary is disposed of.

**Severity: HIGH.** Drives the verdict.

### A2. [HIGH] The load-bearing premise of the Justin case — that PAHC uses him narrowly and leaves the apologetic argument, the address to power, and the Trypho debate unclaimed — is contradicted by PAHC's own records

**Claimed** (§3 B3, first bullet): *"Direct inspection of what PAHC actually draws from him — the conversion narrative (Dialogue 2–8), the worship/baptism description (1 Apol. 61, 65–67), and one theological aside flagged in-record as 'his own, not necessarily the whole world's' (1 Apol. 46) — shows PAHC using him narrowly, as a community witness, and never engaging his actual philosophical argument, his address to Roman power, or the Dialogue's extended debate with Trypho. That gives this candidate real, unclaimed territory in the same man's corpus."*

**Found.** Each of the three "never" claims fails against the records the draft says it inspected.

*"Never engaging his actual philosophical argument."* `records/pahc/quote/pahc.quote.moses-is-more-ancient.md` is 1 Apol. 44, `evidentiary_weight: load-bearing`, canon cell F2-T, retrieval tier 1, with the trigger *"participant asks how this world argued with outsiders about its scriptures"* and a `divergence_note` reading *"It is an apologetic claim about chronology made to a pagan audience."* That is the antiquity-of-Moses argument — a core apologetic move — already built out. Separately, 1 Apol. 46 is carried by **two** quote records, not the one the draft names: `pahc.quote.justin-reasonable-livers` (tier 2) and `pahc.quote.those-who-lived-reasonably-are-christians` (`load-bearing`, tier 1), the second opened specifically to serve `pahc.witness.god-and-argument`, *"which cites this exact chapter for 'the Logos present in every race of men'."* The Logos-spermatikos doctrine — the philosophical argument the draft's own A2 calls "one of [Nicene vocabulary's] direct historical sources" — is already a load-bearing tier-1 PAHC claim.

*"Never engaging... his address to Roman power."* `pahc.quote.the-memoirs-of-the-apostles-are-read.md` carries the `divergence_note`: *"Justin is describing the practice of his own community to an outside audience, in an apology addressed to the emperor, so the account is shaped to look orderly and unthreatening to a Roman reader."* `pahc.source.justin-first-apology.md`'s binding caveat says the same. `pahc.figure.justin.md`'s `bridge_line` is *"He described our Sunday worship in an open letter to the emperor, and died for the name he defended."*

*"Never engaging... the Dialogue's extended debate with Trypho."* `pahc.source.justin-dialogue.md`'s WEIGHT note: *"this world's fullest display of how its scriptures were actually read — proof-from-prophecy, the memoirs of the apostles read alongside the prophets — and of the porous, argued Jewish-Christian boundary (Doc_01 §2.1's Ways-That-Never-Parted caution applies: the Dialogue is an argument in progress, not a report of a settled separation). Also a witness to inner-Christian plurality: Dialogue 80's acknowledgment..."* Proof-from-prophecy *is* the Dialogue's argument, and PAHC has a named Doc_01 caution governing how it is used.

**Also missing from the draft's own inventory.** `pahc.figure.justin.md` lists a fourth item the draft omits: *"His writing against Marcion 'among every nation' (1 Apol 26, 58) is inside testimony that the rivals were live and undefeated,"* and `pahc.source.justin-first-apology.md` calls chs. 26 and 58 *"this world's clearest inside evidence that the rival movements were live, contemporary, and undefeated."* Those are the exact two citations §2's A5 offers as this candidate's distinctive rival-engagement territory. They are already claimed.

**Severity: HIGH.** The revision must re-derive what is genuinely unclaimed in Justin from the records themselves. The honest residue is narrower than the draft states — plausibly the *Second Apology*, the philosophical-school framing of Justin's own vocation, and the sustained Trypho argument *as argument* rather than as scripture-reading evidence — but that case has to be made, not assumed.

### A3. [HIGH] The Augustine precedent, on which the whole "shared figure" option rests, is misdescribed; the project's actual on-record precedent points a different way

**Claimed** (§3 B3, first bullet): *"the precedent for this (a single figure serving two Representatives through two different projects) is Augustine, already split cleanly across HAL's Hebrew-vs-Septuagint correspondent and Donatism's anti-Donatist controversialist."*

**Found.** `records/hal/figure/hal.figure.augustine.md` closes with: *"STRICTLY AN OUTSIDE VOICE: Augustine belongs to his own (not-yet-built) world; this record draws on him ONLY as the other side of the correspondence, per the cleared Doc_02 boundary."* Donatism's Step 0 §2 A5 places Augustine among *"the Caecilianist party (Caecilian, Optatus, Augustine, the imperial state as adjudicator) inside this world's own Doc_02, as Donatism's own opponents, reconstructed from inside Donatism's own perspective"* — an Article 23 opponent, not a co-owned voice. Augustine's own native home is LPC (World #8), where he is an anchor figure.

So the pattern is not "one figure serving two Representatives." It is: **native to one world; declared outside voice or declared opponent everywhere else.** Applied to Justin, that precedent does not license option (a) as drafted; it points to a third option the document does not consider — Justin native to PAHC, held here as a declared outside/boundary voice with a written bounding rule.

**The genuinely on-point precedents exist and are uncited.** Two:
1. `records/alx/source/alx.source.athanasius-vita-antonii.md` carries a cross-build flag inside the `work` field itself — *"desert-content world-attribution is CROSS-BUILD, held open with the Desert world"* — plus an explicit bounding rule: *"no Alexandrian record may treat desert formation logic as constitutively Alexandrian on this text's authority."* `records/desert/source/desert.source.athanasius-vita-antonii.md` holds the same work from the other side. This is a worked, live model of exactly the mechanism the Justin question needs.
2. Mark's own ruling of 2026-08-27 in `cic/corpus-map/latin-apologists.yaml`: *"THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS... That is the Athanasius case the schema names — the Vita Antonii is desert's and Against the Arians is Alexandria's, one author, two entries, split by work."*

**And the draft understates its own problem.** Split-by-work is the project's named remedy, and it is *unavailable* for Justin: `pahc.figure.justin.md` claims `locus: whole work` on **both** the *First Apology* and the *Dialogue*. The Justin question is therefore harder than the Augustine framing suggests, not softer — while being simultaneously *less* undecided than the draft implies, since `cic/corpus-map/greek-apologists-second-century.yaml` already records a 2026-08-26 corpus-level dual assignment for all three genuine Justin works (*"greek-apologists-second-century added alongside... pahc is kept: the era and church-world really are its"*). Neither the ruling nor its limits are cited.

**Severity: HIGH.** §4 item 1 must be rewritten around the actual precedent set, and should present three options, not two.

### A4. [HIGH] §2 A5's Article-21 finding and §4 item 3's binding obligation are premised on a bundling that does not exist in the corpus map

**Claimed** (§2 A5): *"Several of the fragmentary voices currently bundled with them in `pahc.source.second-third-century-remains.md` (Hegesippus, Dionysius of Corinth, Rhodon, Polycrates, Serapion, Apollonius) are, on inspection, internal church correspondence... even though the census currently files them under the same candidate. **This is a real, unresolved boundary question for Doc_01, not a cosmetic one**."* §4 item 3 makes it binding.

**Found.** `cic/corpus-map/greek-apologists-second-century.yaml` holds sixteen works: the Ambrose *hypomnemata*, Aristides' *Apology*, Aristo of Pella's fragments, Athenagoras ×2, Justin ×6 (three genuine, three pseudonymous), the *Epistle to Diognetus*, Melito's fragments, Quadratus' fragments, Tatian's *Address*, Theophilus' *To Autolycus*. **None of the six names the draft lists is on it.** Grepping `cic/corpus-map/` for each: Hegesippus → `post-apostolic-house-church`, `alexandria-catechetical`, `montanism-the-new-prophecy`, `novatianism`, `UNATTRIBUTED`; Dionysius of Corinth → `post-apostolic-house-church` only; Rhodon → `post-apostolic-house-church`, `marcion-marcionism`; Polycrates, Serapion, Apollonius → `post-apostolic-house-church` (Apollonius also `montanism-the-new-prophecy`, Serapion also `apocryphal-and-pseudepigraphal-literature`, `syriac-edessa-nisibis`). The census's own I.35 entry names none of them either; its `voices` list runs Quadratus, Aristides, Justin, Athenagoras, Theophilus, Melito, the writer to Diognetus.

The genre question the draft raises is a fair one *in principle* — but as stated it describes work already done. `pahc.source.second-third-century-remains.md` is a single load-bearing PAHC source record covering ten fragmentary authors, and its own body text already runs the disentanglement the draft calls for (*"THIS WAS FOUND INSIDE A PILE LABELLED AS SOMETHING ELSE... The volume splits by its own div1 sections"*), including per-author dispositions for Maximus of Jerusalem, Pantaenus, and Pseud-Irenaeus.

**Severity: HIGH.** §4 item 3 as written directs Doc_01 to unbundle something that is not bundled. What is actually open — whether Quadratus, Melito, Aristo of Pella and the Ambrose *hypomnemata* (which *are* on this candidate's map, dual-assigned) should stay dual-assigned with PAHC — is a different and much narrower question the draft never states.

### A5. [MODERATE] The candidate's own roster, as actually assigned, contains four works the document never names — including three pseudo-Justin works flagged `provisional`

**Found.** Beyond the sixteen-work map above: the three works transmitted under Justin's name that the corpus map carries at `confidence: provisional` with the note *"transmitted under Justin, widely doubted"* (the *Discourse to the Greeks*, the *Hortatory Address to the Greeks*, *On the Sole Government of God*), plus Aristo of Pella's *Dialogue of Jason and Papiscus* fragments and the Ambrose *hypomnemata* (itself `provisional` on a date question). §2's A5 spends a paragraph on genre uncertainty among voices that are not on the roster, and none on the three pseudonymous attributions and two `provisional` date flags that are.

**Severity: MODERATE.** B1's "strong pass, independently verified against the actual text library" cannot stand as an unqualified statement while the roster's own attribution flags go unmentioned.

### A6. [MODERATE] A5's Marcion handling misstates both the rule and the IJC precedent it cites

**Claimed** (§2 A5): *"Per A5, Marcion is not separately screened here; he appears, correctly, as this candidate's own named opponent, the way Homoian Christianity appears inside IJC's own build rather than as an independent candidate."*

**Found.** A5's actual text (`CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`): *"A movement's historical rivals — movements it anathematized or was anathematized by — are not separately assessed for inclusion as their own worlds **under this section**."* The scope limiter is "under this section" — A5 governs what an *including* world's own Section A pass must do, and says nothing against a rival being screened in its own right elsewhere. Marcion demonstrably *was* screened in his own right: census I.20, status `Excluded - Doctrinal Floor (C1)`, whose own `statusMeta` reads *"Excluded on a stated creedal ground you can read in full. Exclusion is not a judgment of unimportance."*

IJC's confirmation states this correctly and the draft inverts it. IJC §2 A5: Homoian Christianity *"was already tested and excluded at the portfolio level, on the doctrinal floor, **as its own candidate world** — a floor effect, not a judgment of unimportance."* The draft's "rather than as an independent candidate" says the opposite of the document it cites.

**Severity: MODERATE.** Outcome unaffected (Marcion belongs inside this candidate's reconstruction either way); the rule statement and the precedent citation are both wrong, and the same sentence rests on 1 Apol. 26/58, already claimed by PAHC (A2 above).

### A7. [MODERATE] §4 item 6 routes the Trypho obligation away from the Article that actually governs it

**Claimed** (§4 item 6): the *Dialogue*'s engagement with Judaism is *"not a Christian-heresy rival in the Article 20/23 sense, and should not be handled as if it were."*

**Found.** Article 23 (Constitution, "Governing external opponents") reads: *"How the world understood those it anathematized or combated belongs within this principle. The Representative speaks about the world's opponents as the world understood them — honestly, without rehabilitating them into modern equals and without modern editorializing. This is categorically distinct from the Marginalized-Voices duty in Article 20, which concerns the suppressed within the community."* Article 20's own text confirms the division: its scope *"does not extend to the community's external opponents, those it anathematized or combated. That is governed by the Writing-From-Inside Principle in Article 23."*

Nothing in Article 23 limits "opponents" to Christian heresies. Rabbinic Judaism as Justin's interlocutor falls squarely inside it. The draft is right that Article 20 does not apply and right that this is not a heresy case — but by packaging 20 and 23 together and excluding both, it leaves the obligation floating on "needs deliberate, careful framing" when Article 23 supplies a specific and demanding standard. PAHC has already gone further: `pahc.source.justin-dialogue.md` carries a named Doc_01 §2.1 "Ways-That-Never-Parted caution."

**Severity: MODERATE.**

### A8. [MODERATE] §4 item 2's Tatian/Encratite obligation is already discharged, in a built world, on the same text — and the "Bardaisan discipline" the draft invokes names a record type it does not use

**Claimed** (§2 A2, §4 item 2): Tatian's later turn *"must be named plainly in Doc_02 rather than left for a participant or reviewer to discover unflagged. This is the same discipline the project already applies to Bardaisan and Modalism elsewhere in the census."*

**Found.** `syr.source.tatian-address-to-greeks.md` already carries a section headed **"THE ENCRATITE CHARGE, HANDLED HONESTLY"**: *"Eusebius accuses him of it and this world's figure record carries the charge. The Address is not a confession of it and must not be read as one: it is an apology addressed to Greeks, written before the events Eusebius describes, and its asceticism is of a piece with the whole second-century apologetic register. What the Address supplies is the material for a reader to weigh the charge rather than only receive it."* `syr.figure.tatian.md` carries it too, with `narratable: false` and a stated reason.

As for "the discipline the project applies to Bardaisan": it is not a census status word, it is a **record type**. `records/syr/contested_claim/syr.contested.bardaisan-nicene-floor.md` states the claim, lists it `held_against` two specific named divergences, and cites three modern monographs (Possekel, Ramelli, Drijvers) with license status per source. §4 item 2 asks Doc_02 for a source-record note; the precedent it invokes calls for a `contested_claim` record.

**A second, internal problem in the same passage.** §2 A2 clears Tatian on the ground that the *Address* is *"generally read by the field as predating or independent of that later turn"* — an uncited appeal to consensus on a genuinely disputed dating. §4 item 1 of the *sibling* document demands, for Commodian, *"a cited scholarly judgment."* The same standard is not applied to Tatian, where the dating question bears directly on an A2 clearance.

**Severity: MODERATE.**

### A9. [MODERATE] The A1/A2 routing cites IJC's "as applicable" reasoning for the opposite of what IJC used it for, and the closest precedent goes uncited

**Claimed** (§2 A1): *"A1 is not the operative test in the primary sense (per the same 'as applicable' Procedure text IJC's own confirmation relied on for its 312–325 sliver); A2 is the real gate here."*

**Found.** The Procedure's actual text: *"Test each candidate against A1 (and A2 or A3 as applicable)."* On its plain terms A1 is unconditional and A2/A3 are the conditional additions. IJC used that sentence to reach *"both A1 and A2 apply, to different phases of the same continuous movement,"* explicitly rejecting a forced either/or — and IJC's own Round 1 review recorded, as its first HIGH finding, that reading the Procedure as making A2 exclusive was an invented rationale. The draft cites the fixed document as authority for the position the fix removed.

The outcome is defensible — a window wholly closed at 200 CE has no post-Creed phase to test — but the warrant is misattributed, and the genuinely on-point precedent is uncited: LPC's cleared Step 0 §2 runs A2 as the governing test for Cyprian's wholly pre-Nicene phase, quotes the Procedure sentence directly, and says of it *"nothing else."*

**Severity: MODERATE.**

### A10. [MODERATE] The Article 4 provenance line is inaccurate, and the document restates the floor in a way Article 4 forbids Step 0 from doing

**Claimed** (header): *"Constitution V2.3 Article 4 (Movement-Scope scoping section, as quoted directly in `Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md` §2, reused here verbatim rather than re-extracted independently)."*

**Found.** IJC §2 A1 contains no quotation of Article 4 — no quotation marks, no block quote. It paraphrases: *"tests whether a movement's own confession affirms, in its plain historical sense, the content drawn from the Nicene-Constantinopolitan Creed (381) — full divinity and consubstantiality of Christ, true humanity, the Passion/resurrection/ascension/return, and the Spirit as Lord and giver of life."* The draft reproduces that paraphrase and calls it verbatim reuse of a direct quotation.

This matters because Article 4 itself closes with: *"This is the authoritative statement of the floor's content; the Construction Framework's Step 0 operationalizes it procedurally and **must not restate it independently** — where the two differ, this Article governs."* LPC's Step 0 handles this correctly and says so: *"This document does not restate the floor's content on its own authority; it applies it,"* then quotes all five commitments exactly. The apologist drafts restate a paraphrase of a paraphrase.

**Severity: MODERATE.** (Version handling — "V2.3" against the filename `CiC_L1_Constitution_V2_2.docx` — is correct, per IJC's own Round 1 verification, and is not a finding.)

### A11. [MODERATE] A Tier is assigned without addressing the Methodology's own prohibition on per-world scoring, and without the warrant IJC and LPC each established

**Found.** Section B's scope paragraph: *"this is a phase-level process, run once when the project opens a new release phase, **never a per-world process**."* IJC and LPC both confront that sentence and answer it — their warrant is that they are already-selected portfolio worlds being re-tested against text that postdated their selection. Neither apologist draft contains the phrase "per-world process" at all (`grep -c` → 0 in both), and neither has that warrant: these are not selected worlds. They are `Possible Future World (on record)` entries, a status whose own `statusMeta` reads *"not yet chosen, not forgotten."*

The drafts nonetheless render Section A clearances and assign Tier 1. That is a disposition, and the framework under which "on record" entries live says dispositions are not theirs to make (see A12).

**Severity: MODERATE.** Not necessarily fatal — a candidate case *can* usefully pre-figure a Tier — but it must be framed as a signal, with the prohibition quoted and answered, as both sibling documents do.

### A12. [MODERATE] §5's process finding was made without checking the one existing document nearest this mode, and mischaracterizes the document it does cite

**Claimed** (§0, §5): this is *"closer in kind to the era-10 Step 0 methodology's individual candidate write-ups (`CiC_Step0_Era10_V1_0.md`)"*; and *"no template exists for this specific situation... System Hub may want to name this as a recognized third mode."*

**Found, on the Era 10 document.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_V1_0.md` is titled *"Step 0 — Era 10: The Global Church Era (1906–present) · A1.E10 · V1.0"* and is structured as a five-step **era-wide run**: §1 "Survey update + completeness sweep (step 1)", §2 "Section A (step 2)", §3 "Section B (step 3) — [E]", §4 "Source bases (step 4)", §5 "Gravity-bounded dates (step 5)", §6 "Tiered output, status proposals, questions for Mark." It is the phase-level survey mode the Methodology already describes, not "individual candidate write-ups." The analogy runs backwards.

**Found, on the uncited document.** `Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md` is exactly the instrument for pre-Step-0 candidate assessment of on-record entries. Its own scope text: *"It renders no floor verdicts of its own. Where an entry carries a floor note, it uses the Methodology's own vocabulary — 'plain-reading' observations (A1), continuity questions (A2)... — as questions the era's Step 0 will have to answer."* Its entries carry a *"Sourcing signal — ...A signal, not a B1 score"* and *"Ecology signal — ...A signal, not a B2 score."* Neither draft cites it.

This is the failure mode IJC's own Round 1 review caught as its finding #4 — a claim of methodological novelty made without finding the prior treatment that already exists.

**Severity: MODERATE.** §5 is not necessarily wrong that a third mode should be named; it is wrong to say no framework exists, and its supporting analogy is inverted.

### A13. [LOW] §1's block quotation is not a quotation

**Found.** No string from §1's block-quoted paragraph occurs in `world-census.json`. Tested directly: *"A body of individuals defending Christianity's reasonableness"* → 0 occurrences; *"fragmentary sub-apostolic voices"* → 0. IJC and LPC both head §1 *"(as already confirmed, quoted verbatim from the Step 0 Conclusion)"* and their block quotes match their sources exactly. Using the same visual form for composed text, in a document explicitly following that template, invites a reader to treat it as sourced. The composition also imports Hegesippus and Dionysius of Corinth into the candidate's roster (see A4); each name occurs exactly once in the census, in PAHC's entry.

**Severity: LOW**, but it is a quote-accuracy defect of the class IJC's Round 1 review recorded twice.

### A14. [LOW] Small unchecked items that were checkable

- §2 A5: *"it is not yet confirmed here which specific fragments of Melito's are vendored under his name."* They are: `anf08` div2 x.v, 11,288 words, section locus verified in `pahc.source.second-third-century-remains.md` at line 70117. One grep. (Separately worth knowing for Doc_02: the ANF Melito predates the twentieth-century recovery of the Paschal homily the census's own `voices` entry names, so that text is *not* in the vendored corpus.)
- B1 lists the *Epistle to Diognetus* without the date caveat this candidate's own corpus map attaches to it (*"Doubt is the date — some put it after the entry's 200 CE close"*).
- §2 A2's Irenaeus citation is sound (AH I.28.1 does report Tatian's post-martyrdom separation and his link to the Encratites), and "found or lead" is appropriately hedged — Irenaeus derives the Encratites from Saturninus and Marcion and credits Tatian with a specific doctrine, not with founding them.

---

## Part B — Findings against I.43, The Latin Apologists

### B1. [HIGH] Tertullian is absent from the entire document — including from a B3 whose own census entry names him first

**Found.** The census entry for I.43 lists Tertullian in its own `voices` array: *"Tertullian — whose Apology of 197 begins the whole enterprise, and who has an entry of his own rather than a place in this one."* Its `relationsSummary` states the separation and its reason: *"It touches tertullian-s-voice, which begins the enterprise and is kept separate because a voice that distinct is its own entry."* Its `legacy` field opens: *"The Latin vocabulary of Christian argument was largely made here, and in Tertullian's hands at the same time."*

`cic/corpus-map/tertullian-s-voice.yaml` holds **33 works**, including the *Apology (Apologeticus)*, *Ad Nationes*, *To Scapula*, *The Soul's Testimony*, and *An Answer to the Jews* — i.e. the Latin apologetic corpus proper, all of it, assigned to I.17.

The draft mentions Tertullian **zero times**. Its B3 checks I.35, LPC and IJC; §4 item 7 admits *"Only LPC and IJC were checked directly in this pass."*

**Why this is substantive rather than a citation gap.** §2's A5 argues the candidate is *"one coherent tradition developing in stages"* — Minucius Felix → Arnobius → Lactantius — and §4 item 6 makes that the binding Article 21 question for Doc_01. Whether a "developing tradition" argument survives the removal of the man whose 197 *Apology* the candidate's own census entry calls the beginning of the enterprise is precisely the Article 21 question, and the draft does not pose it. B5 leans on geographic span (Rome/Ostia, Numidia, Nicomedia, Trier) without noting that Carthage — the province's own apologetic centre, and Arnobius' own province — is excluded by a boundary the document never states.

**And an on-record treatment already exists, uncited.** LPC's `Source_Registry.md` row 29 runs this exact boundary formally: Tertullian's corpus classified **Excluded / Named Comparandum**, with a stated rationale (*"he predates Cyprian's own episcopate by decades, wrote as a lay apologist rather than this world's own bishop-centered pastoral office"*) and a pointer to `cic/corpus-map/tertullian-s-voice.yaml`. That is a cleared, five-round-reviewed treatment of the same problem in an adjacent world, and it says something I.43 has to answer: the reason LPC gives for excluding Tertullian is that he *"wrote as a lay apologist"* — the very thing I.43 is about.

**Severity: HIGH.** Drives the verdict. §3 B3 must add a Tertullian bullet, and §2 A5 must fold I.17 into the Article 21 discussion.

### B2. [HIGH] Minucius Felix's Christological content is not "thin" in the vendored text — it is absent; and §4 item 3 instructs Doc_02 to pre-decide a live scholarly dispute

**Claimed** (§2 A2): *"Minucius Felix clears, with a disclosure, not a caveat of divergence: the *Octavius*... is genuinely thin on distinctively Trinitarian or Christological content — this is a feature of the dialogue's own persuasive strategy... rather than evidence of divergence from proto-orthodoxy."* §4 item 3 makes that reading binding on Doc_02: *"Name the *Octavius*'s own persuasive strategy... as the reason for its thin Trinitarian content, **rather than treating the thinness as evidence of anything else**."*

**Found**, by parsing `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, div2 `iv.iii` (22,305 words excluding editorial notes; note-tails preserved):

| token | occurrences |
|---|---|
| `\bJesus\b` | **0** |
| `\bChrist\b` | **1** — and it is inside an ANF editor's chapter *Argument* heading ("...for the Confession of Christ's Name..."), not in Minucius' text |
| `\bSon of God\b` | 0 |
| `\bincarnat\w*` | 0 |
| `\bcrucifi\w*` | 1 — likewise inside an editor's Argument heading (ch. IX) |

The one place Minucius' own prose meets the charge, ch. XXIX, reads in full: *"For in that you attribute to our religion the worship of a criminal and his cross, you wander far from the neighbourhood of the truth, in thinking either that a criminal deserved, or that an earthly being was able, to be believed God."* He then turns immediately to Egyptian god-kings and imperial flattery. There is no positive Christological statement anywhere in the work.

A2's test is whether a movement's *"own surviving confession affirm[s], in the less technical language available to it, the substance Article 4 states."* For one of this candidate's four figures, the vendored corpus supplies no affirmation of Article 4's second, third or fourth commitments at all. The clearance therefore rests entirely on argument-from-silence plus external inference — which may well be right, and is a genuinely long-running scholarly debate, but is not what "clears, with a disclosure, not a caveat of divergence" describes.

**§4 item 3 is the more serious half.** It directs Doc_02 to name one reading as *the* reason and to refuse to treat the evidence "as evidence of anything else." That is an instruction to close a contested question in the candidate's favour before Doc_02 opens — the opposite of the discipline `syr.contested.bardaisan-nicene-floor.md` models, and of Conviction 4's own *"Participants deserve access to... tensions, disagreements, uncertainties."*

**Severity: HIGH.** Drives the verdict.

### B3. [HIGH] Lactantius clears A2 "without qualification" as "the strongest possible A2 case," when he carries the best-attested ancient criticism on Article 4's fifth commitment

**Claimed** (§2 A2): *"**Lactantius clears without qualification** — he is, if anything, the strongest possible A2 case in this candidate: a proto-Nicene establishment theologian, tutor to Constantine's own son at Trier, whose *Divine Institutes* argues the same substantive content the Creed would later formalize."*

**Found.** The biography is right (rhetor at Nicomedia; tutor to Crispus at Trier, c. 317). The theological claim is not. Lactantius' pneumatology is the standard difficulty with him: Jerome, *Ep.* 84.7, states that Lactantius *"in his letters, and especially in those to Demetrianus, denies the substance of the Holy Spirit, and by a Jewish error says that it is referred either to the Father or to the Son."* Article 4's fifth commitment is *"The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son."* Alongside this sit *Div. Inst.* VII's chiliasm and *Div. Inst.* II.8–9's two-spirits cosmology, both routinely named as rough edges against later orthodoxy.

Note the shape of the error: the draft correctly flags Minucius' Christological thinness and Arnobius' anthropology as disclosable, then hands the anchor figure — the one whose 2026-08-27 addition *"quadrupled the entry's corpus,"* per the census — a clean pass, on the very commitment where the ancient criticism is sharpest and best-sourced. A2 disclosures are being applied to the figures the draft already thought were awkward, not derived from the texts.

**Severity: HIGH.** Drives the verdict. Lactantius' pneumatology needs a disclosed A2 item in §2 and a §4 entry, at minimum on Jerome's charge.

### B4. [HIGH] The Lactantius/IJC "live boundary" was ruled on by Mark, by name, on 2026-08-27, in this candidate's own corpus map — and the ruling is uncited

**Claimed** (§3 B3, third bullet, and §4 item 4): the overlap is *"closer to IJC's own 'World #5 vigilance' pattern than to a hard boundary requiring a project-lead ruling before drafting... Doc_01 should log this as a live boundary rather than an assumed-obvious one."* §4 item 4 makes it *"binding on Doc_01."*

**Found**, in `cic/corpus-map/latin-apologists.yaml`, on the *Divine Institutes* entry:

> *"RULED BY MARK 2026-08-27: Lactantius lives in `latin-apologists` (I.43)... **THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS.** Lactantius' apologetic corpus moves; *Of the Manner in Which the Persecutors Died* does NOT. That is the Athanasius case the schema names — the Vita Antonii is desert's and Against the Arians is Alexandria's, one author, two entries, split by work."*

The three companion works carry the same ruling's dependency resolution, each noting the confidence rise from `provisional` to `assigned`. This is precisely the project-lead ruling the draft says has not happened, made in the file that defines the candidate's own roster, dated eleven days before the draft.

**Severity: HIGH.** §4 item 4 presents settled, cited governance as open work; the effect is to route a resolved question back through Doc_01 while leaving Mark's actual ruling — and the split-by-work precedent it names — off the record of this document entirely.

### B5. [MODERATE] IJC's claim on *De Mortibus Persecutorum* is materially understated

**Claimed** (§3 B3): *"Lactantius appears in IJC today exactly once, cited only for *De Mortibus Persecutorum* and only for one story — Constantine's pre-battle vision (`ijc.source.lactantius-de-mortibus.md`, `ijc.story.dream-before-battle.md`)."*

**Found.** `ijc.source.lactantius-de-mortibus` is `evidentiary_weight: load-bearing` and is cited by **nine** IJC records: `ijc.gravity.church-state-alliance`, `ijc.figure.constantine`, `ijc.story.dream-before-battle`, `ijc.contested.constantine-conversion`, `ijc.quote.milan-edict`, `ijc.quote.lactantius-dream`, `ijc.force.constantine-alliance`, plus two search records. The source record's own note: ch. 48 *"preserves the actual text of the 313 Milan agreement... making this the world's most direct witness to its own legal beginning,"* verified against the file and corrected once at review.

So the second-largest thing IJC draws from Lactantius is not a story at all — it is the Edict of Milan text, and IJC carries two independent transmissions of it (Lactantius' and Eusebius') expressly *"never conflated."*

**What checks out:** the draft's core claim — that the *Divine Institutes* and companions are untouched by IJC — is correct. `grep -rn "Divine Institutes" records/` returns nothing.

**Severity: MODERATE.** The conclusion survives; the characterisation does not, and understating a neighbour's claim is exactly what a boundary note exists to prevent.

### B6. [MODERATE] Arnobius' conversion account is attributed to Arnobius, and the hedge the census itself carries is dropped

**Claimed** (§2 A2, heading and body): *"**Arnobius' theology carries real, disclosed idiosyncrasy, by his own admission.** Jerome reports Arnobius wrote *Against the Heathen* at his bishop's insistence, as proof of a conversion the church did not yet trust — he was, **on his own text's own evidence**, a rhetoric teacher freshly converted and not yet formed by sustained catechesis."*

**Found.** Three distinct slips in three sentences.
1. *"by his own admission"* — the conversion story is Jerome's report (*De viris illustribus* 79; *Chronicle* ad ann. 327), not Arnobius' admission. The draft says so correctly in its next clause, then re-attributes it to the author.
2. *"at his bishop's insistence"* — Jerome's account is that the bishop **would not admit him**, and that Arnobius wrote the books as a pledge to obtain baptism. "At his insistence" reverses the direction.
3. *"on his own text's own evidence"* — the *Adversus Nationes* does not describe its author as a rhetoric teacher, a recent convert, or uncatechized. That is all Jerome.

The census entry for I.43 carries the hedge the draft drops: *"to persuade his own bishop that his conversion was genuine, **if Jerome is to be believed**."* Jerome's account is itself disputed in modern Arnobius scholarship.

**The Book II claim checks out.** *Adversus Nationes* II does argue that souls are of a *media qualitas*, not immortal by nature, receiving immortality as a gift through Christ. The draft's description of the position is accurate; only the provenance framing is wrong.

**Severity: MODERATE.**

### B7. [MODERATE] Commodian's dating is made binding pre-Doc_01 work; Minucius Felix's — flagged by the census in the same sentence — is not mentioned as an issue at all

**Found.** The census's own sourcing note for I.43 ends: *"Two of the four authors are barely datable: Minucius Felix within a century, Commodian within three."* The draft carries the Commodian half into §2, §3 B3 and §4 item 1 (with the correct corpus-map grounding: `confidence: provisional`, *"the reason is the date rather than the shelf"*). The Minucius half appears nowhere.

This matters for B3 specifically. A mid-third-century *Octavius* — a live option across the disputed range — would place Minucius Felix inside census I.33, *The Roman Church in the Third Century* (c. 200–268, Rome), a separate on-record candidate the draft does not check. The draft's own logic for Commodian (*"if the later dating is judged more likely, he may need to be reassigned rather than retained"*) applies to Minucius against I.33 with equal force.

**Severity: MODERATE.**

### B8. [MODERATE] The structural findings from Part A apply here in identical form

Carried over without re-argument, since I.43 reproduces I.35's framing verbatim in each case:
- §1's block quotation is not a quotation (tested: *"Latin-language philosophical and polemical defenses"* → 0 occurrences in the census; *"brought the empire's troubles"* → 0). See A13.
- The Article 4 provenance line ("quoted verbatim in IJC §2, reused here") is inaccurate, and the floor is restated in a way Article 4 forbids. See A10.
- The A1/A2 routing cites IJC's "as applicable" reasoning for the opposite of what IJC used it for; LPC's on-point pre-Nicene precedent is uncited. See A9. (The arithmetic is right: 325 − 320 = five years.)
- Tier 1 is assigned without quoting or answering Section B's *"never a per-world process."* See A11.
- §5's process finding is made without checking `CiC_World_Atlas_PreStep0_Survey_V0_1.md`. See A12. (§5 here simply adopts I.35's finding, so it inherits the defect wholesale.)

**Severity: MODERATE** each.

### B9. [LOW] Roster and scale details

- **"Vendored whole" covers about half of Commodian.** The *Instructiones* is vendored (15,008 words); the *Carmen apologeticum* is not in ANF and is not in `cic/texts/`. The draft's phrasing is defensible per-work but leaves the impression of a complete corpus.
- **The *Epitome of the Divine Institutes* is vendored** (`anf07`, div3 `iii.ii.viii`) and is omitted from B1's list of Lactantius' works.
- **"the Great Persecution (303–311)"** takes Galerius' edict as the terminus; persecution continued in the East under Maximinus Daia to 313. Cosmetic.

---

## Part C — The full Era 1 sweep (commissioned; performed by neither draft)

Twenty-one entries carry `era == 1` in `cic-website/data/world-census.json`. Both drafts disclose partial sweeps (I.35 §4 item 5: PAHC only; I.43 §4 item 7: LPC and IJC only). This section closes the gap. Method: for every entry, the census record was read in full, the entry's `cic/corpus-map/*.yaml` bucket was read work-by-work where one exists, and `records/<world_key>/` was grepped for every author name on both candidates' rosters. Findings are stated only where something real was found.

### C1. I.7 — Syriac Christianity (Edessa/Nisibis), Built & Live. **MATERIAL. Changes I.35's B3 and its §4 item 5.**

Fully argued at **A1** above. In short: Tatian is a built `figure` record with a `load-bearing` source record on the *Address to the Greeks*, plus two quotes, a gravity, a force and a term; the *Address* is triple-assigned in the corpus map (`pahc`, `greek-apologists-second-century`, `syriac-edessa-nisibis`); and the corpus map's own note says *"Mark may want a ruling on where his voice sits."* A second shared work exists too — the Ambrose *hypomnemata* is dual-assigned to `greek-apologists-second-century` and `syriac-edessa-nisibis`, on a ruling of 2026-08-26 recorded in the map (*"greek-apologists-second-century is added, which is where the argument belongs, and syriac-edessa-nisibis is kept, which is how it reached us"*).

**Disposition: must be added to §3 B3 as its own bullet and to §4 as a second binding pre-Doc_01 ruling, alongside Justin.** The Tier-1 conditional cannot stand on a fallback roster containing Tatian until it is disposed of.

**Bardaisan (also census I.32) — no roster contact with either candidate**, and no reason to expect any; his Era-1 relevance to this review is as **precedent, not adjacency**. See **A8**: `syr.contested.bardaisan-nicene-floor.md` is the record type the "Bardaisan discipline" I.35 invokes actually denotes, and it is the correct home for both the Tatian/Encratite item and (per **B3**) the Lactantius/pneumatology item.

**Bearing on Ephrem and Aphrahat: none.** Neither appears in either candidate's corpus map; both post-date I.35 entirely and sit outside I.43's language and province.

### C2. I.17 — Tertullian's Voice, Possible Future World. **MATERIAL. Changes I.43's B3 and its §2 A5.**

Fully argued at **B1**. 33 works on `tertullian-s-voice.yaml` including the whole Latin apologetic corpus; named in I.43's own census `voices` and `relationsSummary`; absent from the draft entirely; and already given a formal Named-Comparandum treatment in LPC's `Source_Registry.md` row 29.

**Disposition: must be added to §3 B3, and the Article 21 discussion in §2 A5 must state whether a "developing tradition" claim survives the exclusion of its own opening act.** The census supplies a reason for the separation ("a voice that distinct is its own entry"); the draft must either adopt that reason and say so, or contest it — not omit it.

**Bearing on I.35: none.** Tertullian post-dates the window and writes in the wrong language.

### C3. I.33 — The Roman Church in the Third Century, Possible Future World. **MATERIAL (moderate). Bears on I.43's B3 and §4.**

The corpus map holds eight works, seven of them Hippolytus. No work overlap with either candidate. The real adjacency is the one at **B7**: Minucius Felix is a Roman advocate whose dialogue is set at Ostia and whose date the census says cannot be fixed within a century. I.33's window is c. 200–268, Rome. A mid-third-century *Octavius* — inside the live range — lands in I.33's window and city.

**Disposition: add to §4 item 1, reframed as a dating obligation covering both barely-datable authors rather than Commodian alone.** Not a tier-changing finding.

### C4. I.24 — Ebionite / Nazoraean Current, Contested — Evidentiary. **MATERIAL (low). Bears on I.35's B3 and §2 A5.**

Two real contacts, both already recorded in I.35's own corpus map and neither mentioned in the draft:
1. **Aristo of Pella's fragments are dual-assigned** to `greek-apologists-second-century` and `ebionite-nazoraean-current` (and `post-apostolic-house-church`). The map's own note: *"a Hebrew-Christian apologetic dialogue from Pella. The Jewish-Christian current and pahc are both defensible; neither is demonstrated by the fragments."*
2. The *Dialogue with Trypho*'s own entry on I.35's map records: *"Ch. 47's discussion of Torah-observant Christians is also one of the era's few direct witnesses to the ebionite-nazoraean-current material — noted here rather than assigned, since it is a few chapters of a 75,000-word work."*

This is directly germane to §4 item 6, which treats the Dialogue's Jewish material as purely a modern-framing problem; it is also an evidentiary-boundary problem against a Contested entry.

**Disposition: add one bullet to B3 and one clause to §4 item 6.** Does not change the tier.

### C5. I.20 — Marcion / Marcionism, Excluded — Doctrinal Floor (C1). **MATERIAL (moderate), but as a rule-and-precedent error, not an overlap.**

Fully argued at **A6**: the A5 rule text is misquoted in effect ("under this section" dropped), and the IJC precedent is cited for the reverse of what IJC says. Two further checks: Rhodon's fragments — one of the names I.35 wrongly places on its own roster — are assigned to `marcion-marcionism`, not to this candidate; and the two Marcion passages I.35's A5 relies on (1 Apol. 26, 58) are already named in PAHC's own figure and source records.

**Disposition: rewrite the A5 paragraph.** No tier effect.

### C6. I.8 — Latin Pastoral-Congregational Christianity, Selected — Not Yet Built. **I.43's check is sound; I.35 had no obligation.**

Verified independently rather than accepted: `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` contains **no** work by Arnobius, Lactantius, Minucius Felix or Commodian — Arnobius having been moved out on 2026-08-27, as the `latin-apologists.yaml` entry records (*"MOVED 2026-08-27 from latin-pastoral-congregational-christianity, where the worker had parked it as provisional"*). The only apologist name surviving anywhere in LPC's build documents is Minucius Felix, and only inside a corpus-map note quoted about a *Cyprianic* treatise (*Quod Idola Dii Non Sint* *"compiles Tertullian and Minucius Felix"*), which is a dependency observation, not a roster claim. **I.43's B3 finding of no figure overlap is correct**, and its hedge ("not exhaustively re-checked here") was more cautious than it needed to be.

**On the I.35 question raised in the brief — was I.35 obligated to check LPC? No.** Grepping LPC's and Donatism's complete build directories for Justin, Athenagoras, Theophilus, Tatian and Aristides returns zero hits. LPC opens in the 240s in Carthage; I.35 closes in 200 in the Greek East. The Judaism/heresy content of Justin's *Dialogue* has no contact with LPC's congregational subject matter — and where such content does have a live claimant, it is Donatism's Article 23 material and PAHC's existing Ways-That-Never-Parted caution, both already on record. **Immaterial for I.35.**

**Note, correcting the commissioning brief's premise:** LPC is not "mid-build" in the record sense in this tree. There is no `records/lpc/`. It has Doc_01, Doc_02, a Source Registry, and a five-round-cleared Step 0. That is enough for a real cross-check, which is what was run.

### C7. Entries checked and found immaterial

Each of the following was checked the same way — census record read, corpus map read where one exists, both candidates' rosters grepped — and found to have no bearing:

- **I.1 Post-Apostolic House-Church (Built & Live).** Checked by both drafts, but the check itself is defective for I.35 — see **A2**, **A4**.
- **I.2 Alexandrian Catechetical (Built & Live).** I.35's finding of no figure overlap is **verified correct**: `records/alx/` contains no record for any I.35 or I.43 figure. The apparent name hits in `alx.source.clement-*` are Clement's own citations of Tatian/Athenagoras/Theophilus inside the *Stromateis*, not roster claims. The "historical bridge" framing in B3 is fair.
- **I.21 Valentinian & other Gnostic Christianities (Excluded, C1).** Shares the volume `anf02` with I.35 (Clement's *Stromateis*), no shared work. Immaterial.
- **I.22 Manichaeism (Excluded, C1).** Shares the volume `anf06` with I.43 (Alexander of Lycopolis, Archelaus), no shared work, no shared figure, no period contact with I.35. Immaterial in one sentence, as the brief anticipated.
- **I.25 Montanism (Contested).** No corpus contact with either candidate; its Tertullian works are I.17's, its Apollonius and Claudius Apollinaris fragments are PAHC's. **On the Tatian/Encratism–Montanism question specifically:** the two are distinct second-century currents, no ancient source makes Tatian a Montanist, Irenaeus derives the Encratites from Saturninus and Marcion rather than from Phrygia, and there is no corpus-map or records-level adjacency. The historiographical habit of discussing them together does not create a Step 0 boundary. **Immaterial** — though note that two of the six names I.35 wrongly places on its own roster (**A4**) are in fact Montanism's, which is a symptom of the same unchecked bundling.
- **I.26 Novatianism (Contested).** Cyprianic/Roman material, `anf05`; no contact with either candidate. Immaterial.
- **I.31 Modalist Monarchianism (Floor Question).** One work, Tertullian's *Against Praxeas* — I.17's, not I.43's. Immaterial as adjacency. As precedent, I.35 §2 A2 invokes "the discipline the project applies to... Modalism"; that discipline is the census `Floor Question (register)` status, whose own `statusMeta` reads *"Carries a named creedal question for a future Step 0 to answer — stated as a question, not a verdict."* Fairly invoked, though see **A8** on the record-type point.
- **I.36 Apocryphal and Pseudepigraphal Literature.** 44 works, sharing volume `anf08` with I.35's Quadratus, Melito and Aristo fragments. No shared work. Worth one flag forward, not a B3 bullet: `pahc.source.second-third-century-remains.md` records that `anf08`'s two div1 sections were once confused for one another (*"THIS WAS FOUND INSIDE A PILE LABELLED AS SOMETHING ELSE"*), so any I.35 build drawing on `anf08` should cite by div1 section, not by volume.
- **I.38 The Anatolian Church in the Third Century.** Gregory Thaumaturgus and Methodius, `anf06`. Shares the volume with Arnobius; no shared work, no shared figure. Immaterial.
- **I.39 The Church of Roman Palestine before Constantine.** Julius Africanus, Eusebius' *Martyrs of Palestine*, `anf06`/Eusebian. No contact. Immaterial.
- **I.40 Latin Christianity in the Danubian Provinces.** Victorinus of Pettau's two works, in `anf07` — the same volume as Lactantius, and already drawn on by a built world (`hal.source.victorinus-apocalypse-jerome-recension.md`). Different author, different works; no bearing on I.43. Immaterial, but it is a second demonstration that `anf07` is not I.43's uncontested territory, which strengthens the case that **B4**'s already-ruled per-work split should be cited rather than reopened.
- **I.42 The Church of Antioch in the Third Century.** One work, Malchion's synodal letter, `anf06`. No contact. Immaterial.

### C8. Sweep summary

Of the nineteen Era 1 entries not already checked by the drafts, **five carry real bearing**: I.7 (Syriac) and I.17 (Tertullian's Voice) at a level that changes the documents; I.33, I.24 and I.20 at a level that adds disclosure items. Fourteen are immaterial. Both drafts' §4 "full sweep is binding on Doc_01" items should be marked partially discharged by this review, with the five live items named — a deferral to Doc_01 is not the right home for a finding that a *built* world already owns one of the candidate's own core texts.

---

## What checked out clean (verified directly, not assumed)

Verified against the actual artifacts, and worth recording so the revision does not re-open settled ground:

**Scale and sourcing claims — every number checks.** Parsed from the vendored XML (raw section counts, matching the convention the census's own figures were evidently taken at):

| Work | Draft/census claim | Counted |
|---|---|---|
| Minucius Felix, *Octavius* | ~24,000 | 23,819 (22,305 excluding editorial notes) |
| Commodian, *Instructiones* | ~15,000 | 15,008 |
| Arnobius, *Adversus Gentes* | ~140,000 | 140,826 |
| Lactantius, *Divine Institutes* | ~240,000 (census) | 241,990 |
| Lactantius, *Anger of God* / *Workmanship* / Fragments | (unquantified) | 20,382 / 18,840 / 3,932 |
| **I.43 total** | *"just under half a million"* | **464,797** |

**I.35's B1 "vendored whole" claims — all verified present, in the files named**, with word counts: Justin *First Apology* 24,990 (`anf01` viii.ii), *Second Apology* 5,055 (viii.iii), *Dialogue* 75,254 (viii.iv); Athenagoras *Plea* 18,582 and *On the Resurrection* 13,334 (`anf02` v.ii, v.iii); Theophilus *To Autolycus* 30,702 (`anf02` iv.ii); Tatian's div1 19,029 (`anf02` iii); *Epistle to Diognetus* 5,067 (`anf01` iii.ii); Aristides 14,910 across Greek and Syriac recensions (`anf09` xiii); the "Remains of the Second and Third Centuries" 33,223 across ten authors (`anf08` x). "Roughly ten fragmentary sub-apostolic voices" — exactly ten are named in `pahc.source.second-third-century-remains.md`.

**"Justin Martyr is one of only eleven named figures in PAHC's own roster"** — exactly eleven files in `records/pahc/figure/`. Counted.

**I.43's core B1 file attributions** — Minucius Felix and Commodian in `anf04`, Arnobius in `anf06`, Lactantius in `anf07`: all correct.

**"The *Divine Institutes* and its companion works... completely untouched by IJC"** — correct. `grep -rn "Divine Institutes" records/` returns zero hits across all eight built worlds.

**No built world holds a Minucius Felix, Commodian or Arnobius figure or source record** — the apparent grep hits are all ANF volume-title strings inside `edition:` fields (`anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`; "Ante-Nicene Fathers, vol. 6 (Gregory Thaumaturgus, Dionysius, Julius Africanus, Methodius, Arnobius)"). Checked individually.

**Census quotations that ARE verbatim** (unlike the §1 block quotes): I.35's naming-note quote — *"apologetic is a genre rather than a community... this is a body of people doing one thing in one direction for eighty years, not a settlement with a bishop"* — matches the census exactly, with the elision of *"and a survey may well decide it:"* correctly marked. I.43's *"the least thin of the five gaps he ruled on"*, the 2026-08-27 Lactantius ruling and its "quadrupled the entry's corpus," the Arnobius provenance (*"the wrong genre and the wrong province"*), and the teacher-pupil line resting *"on a line in Jerome"* — all match.

**I.35 §0's account of the corpus-assignment origin** — verified against the census `why` field, including the Athens-not-among-PAHC's-regions detail. Accurate.

**Historical claims that hold:** Irenaeus *AH* I.28.1 on Tatian's post-martyrdom separation (and the "found or lead" hedge is appropriate — Irenaeus derives the Encratites from Saturninus and Marcion); Justin against Marcion at 1 Apol. 26 and 58; Justin's death c. 165; Athenagoras addressing Marcus Aurelius; Arnobius' *media qualitas* soul argument in Book II; Lactantius at Nicomedia and then tutoring Constantine's son at Trier; Commodian's dating range spanning roughly three centuries; 325 − 320 = five years.

**I.35's Alexandria bullet** — no figure overlap, verified directly against `records/alx/`. The sequential-bridge framing is fair.

**I.43's LPC bullet** — verified independently and correct (C6).

**Both drafts' status discipline** — "DRAFT, unreviewed. Not self-disposed. Not Approved to proceed," with no build thread opened — is exactly right for what these are, and is the single thing about the pair that most closely matches the project's own discipline. The findings above are about what the documents assert inside that frame, not about the frame.

---

## Verdicts

### I.35 — The Second-Century Greek Apologists: **SUBSTANTIAL REVISION REQUIRED**

Four HIGH findings, any one of which would be sufficient. **A1**: B3 declares no overlap against six built worlds when a built, live world holds Tatian as a figure and his *Address* as a load-bearing source, and the candidate's own corpus map flags the conflict in the work's own note. **A2**: the premise that PAHC leaves Justin's philosophical argument, his address to power, and the Trypho debate unclaimed fails against PAHC's own quote, source and witness records — including two tier-1 records on 1 Apol. 46 and a load-bearing record on 1 Apol. 44. **A3**: the Augustine precedent on which the shared-figure option rests is misdescribed; HAL declares Augustine "STRICTLY AN OUTSIDE VOICE" and Donatism holds him as an Article 23 opponent, while the genuinely on-point precedents (the Athanasius cross-build flag, Mark's `per work` ruling) go uncited — and split-by-work is unavailable for Justin because PAHC claims `locus: whole work` on both texts. **A4**: §4 item 3's binding Article 21 obligation is premised on a bundling that does not exist in the corpus map.

The candidate itself looks genuinely strong on the evidence — B1's sourcing claims all verified, the Alexandria bridge is real, B4's audience case is honestly scoped. What fails is the document's own verification: it repeatedly says "direct inspection," "independently verified," "no overlap found" for checks that a grep would have overturned. That is the specific failure this project's review culture exists to catch.

### I.43 — The Latin Apologists: **SUBSTANTIAL REVISION REQUIRED**

Four HIGH findings. **B1**: Tertullian — named first in the candidate's own census `voices` list, holder of 33 works including the entire Latin apologetic corpus, and already given a formal Named-Comparandum treatment in LPC's cleared Source Registry — is absent from the document entirely, including from the Article 21 "developing tradition" argument he most directly bears on. **B2**: Minucius Felix's Christological content is not thin but absent from the vendored text (Jesus: 0; Christ: 1, in an editor's heading), and §4 item 3 instructs Doc_02 to close a live scholarly dispute in the candidate's favour. **B3**: Lactantius clears A2 "without qualification" as "the strongest possible A2 case" on the very commitment where Jerome's own charge sits. **B4**: the Lactantius/IJC boundary was ruled by Mark on 2026-08-27 in the candidate's own corpus map, naming the `per work` split precedent — and the ruling is uncited, with §4 item 4 reopening it as Doc_01 work.

I.43 is the better-sourced candidate of the two and its scale claims are the most thoroughly verified thing in either document — every word count checks. But its Section A rests on an unexamined clearance for its anchor figure and an argument-from-silence for another, and its B3 omits its own most obvious neighbour. The Section B conclusion's comparative claim — *"Cleaner than I.35 on B3 specifically: no shared, fully-claimed figure comparable to Justin was found in any built or building world"* — is true as far as it goes and, after **B1** and **C2**, no longer establishes what it is offered to establish.

### Round 2 status

Not run. Both documents should be revised against the findings above and re-reviewed before any build thread opens, per `cic-build-cycle`'s review-gated discipline and both documents' own §6.
