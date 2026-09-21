# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 5 Independent Adversarial Review — the 2026-09-14 reconciliation pass, and a first independent audit of the *Gesta* targeted read the ruling rests on

**Documents reviewed (working tree, branch `lpc-doc04-round2`, at `c3b31c8b`, tree clean):**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_04_Gravity_Discovery.md` (235 lines) — read in full; both tables machine-parsed cell-by-cell; all 28 Interaction Matrix pairs checked for symmetry and then against each candidate's own §3 Interaction bullet; bold-marker and backtick parity checked on every line; the pre-pass text at `b2e93cac` word-diffed line by line against HEAD.
- `Review-Artifacts/Doc04_Gesta_Targeted_Read_2026-09-14.md` (56 lines) — **every claim re-derived independently from the primary text.** Never previously reviewed; treated as the highest-risk artifact in the folder.
- `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (144,733 lines) — read directly. Every cited file line opened with surrounding context; every count re-run; the act inventory re-derived with an OCR-tolerant pattern built for this scan's own substitution set (`t`→`l`/`i`/`j`, `u`→`n`, `m`→`ni`), not with the read's pattern; the 118400–123000 span sampled at six points to characterize what is actually in it.
- `Review-Artifacts/Doc04_Round4_Review.md` (372 lines) — read in full; each of the 20 findings (H1–H6, M1–M5, L1–L6, C1–C3) tested individually at its own named site at HEAD, in both directions: the seven claimed resolved, and the thirteen claimed outstanding.
- `Review-Artifacts/Doc02_Round30_Review.md` (40 lines) — read in full for the drift root-cause claim; tested against the file it describes (`Language: lat` confirmed at line 26 of the *Gesta* scan).
- `lpc_Decision_Log.md` (660 lines) — the 2026-09-14 entry read in full and tested against the file it describes; the 2026-09-09 (later still) and 2026-09-10 entries read for the retracted-claim question; the claim's introduction traced through `git log -S` and across all four merge parents.
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines) — §4 (all three authority axes, the Conclusion), §5, §8 items 6, 7 and 10 read verbatim at source, not from any prior review's rendering.
- `Source_Registry.md` row 65 — read in full, by field.
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx` — extracted from `word/document.xml`; Article 21 read in full, all four paragraphs.
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — same extraction; the Gravity Classification block (Primary / Supporting / Tensional) and the Confidence/Gravity Cross-Check read verbatim.
- `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — same extraction; Layer 3 and Section 4's Step 4 entry read verbatim and located by line.
- `L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md` — §4's classification labels read verbatim.

**Review date:** 2026-09-14
**Reviewer:** independent adversarial review thread. Did not draft Doc_04, did not run the reconciliation pass, **did not perform the *Gesta* targeted read**, did not draft any prior review artifact in this world, and ran no prior round in this build's history.

**Method note.** Two things were done that no prior round in this series has done. First, the *Gesta* read was audited **at source**, claim by claim, against the 144,733-line scan — not checked for internal consistency, and not accepted on the read's own account of its method. The read is new primary-source work, never independently reviewed, performed by the same thread that then applied the ruling resting on it; it is therefore treated as the load-bearing artifact and given its own section below. Second, the pass's own central methodological claim — that the reconciliation set was **derived by searching the document** rather than copied — was tested by running that search, at both the pre-pass commit and HEAD, and then by hunting deliberately for sites the four search terms **cannot** reach. Both tests failed.

The governing question throughout was the one Round 4 named and this pass says it adopted: *a check is only as good as the set it runs over*. Round 4 found a copied list was the defect. This round finds that a **derived** list is only as good as its terms, and that the terms chosen are structurally blind to the one subsection that matters most.

Marking per Constitution Article 31: **Simulated review — informational only, not an Article 31 substitute.**

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 7 HIGH · 8 MEDIUM · 8 LOW · 3 COSMETIC — 26 in total.**

**Fix-pass verification tally, against Round 4's 20 findings: 3 genuinely resolved · 4 partially resolved · 13 outstanding as reported · 0 silently fixed.** The pass claims **seven** resolved (H1–H6, M1). Three are (H2, H3, H5). Four are not (H1, H4, H6, M1) — and one of those, M1, survives **byte-identical at its own named site**.

**The thirteen-outstanding claim is accurate.** M2, M3, M4, M5, L1, L2, L3, L4, L5, L6, C1, C2 and C3 were each tested at HEAD and each is genuinely still open. Nothing on that list was silently fixed and reported open, and nothing on it was broken further. This is the first honest half of a certification this document has produced in six passes and it should be said plainly.

**The 24-site set is not complete, and the number is not reproducible.** Running `Tensional|escalat|Candidate 5|Conciliar Authority` over the document returns **37 lines at `b2e93cac`** and **36 at HEAD** — not twenty-four, at either state. More seriously, the four terms **do not match a single line of Candidate 5's own twelve test bullets** (lines 86–97), its Classification paragraph (99), its classification line (101), or its "What the classification does not claim" paragraph (107). The subsection is *headed* "Candidate 5"; its body never names it. Two stale sites survive there (M5 below), exactly the migration this round was asked to predict. And one site the search **did** match — §7 Open Item 3, line 211, which contains both "Candidate 5" and "Tensional" — still states the superseded classification as settled fact (H1).

**The *Gesta* read is OVERSTATED — not fabricated, not unsound in its direction, but not established by the evidence it cites.** Every file line it names exists and carries substantially what it says. Its two "corrections to the record" are real. But the load-bearing inferential step — from *mandatum* to conciliar-authority theory — is not supported by the passages cited; one of its two census claims is drawn from Migne's editorial footnote apparatus rather than from the Conference; its headline term-count undercounts by roughly forty per cent through the precise failure mode the read itself documents and warns about; and the strongest genuinely on-axis sentence in the source was missed. The full audit is at the end of this document.

---

## Twelve things checked hard and found CLEAN, stated before the findings

1. **Both tables are structurally clean.** Machine-parsed at HEAD: pipe counts uniform (6 across all ten Classification Summary rows; 10 across all ten Interaction Matrix rows). Bold-marker parity and backtick parity are balanced on **every line of the document**, table lines included. The pass broke neither table.
2. **All 28 Interaction Matrix pairs are symmetric**, machine-checked, with the single deliberate asymmetry (2↔7 "Reshaped by" / 7↔2 "Reshapes") correctly directional. All eight §3 Interaction bullets were then checked cell-by-cell against their own matrix rows: **all eight agree**, with no cell claimed in a bullet that the matrix does not carry and none carried in the matrix that its bullet contradicts.
3. **Candidate 5's matrix row is unchanged and is consistent with Supporting.** Three reinforcing (1, 3, 6), four none (2, 4, 7, 8), zero competing — **identical in shape to Candidate 4's row**, which is also classified Supporting (3 reinforcing / 4 none), and stronger than Candidate 7's (1 reinforcing, 1 reshape, 5 none), also Supporting. CF V7.4's Supporting definition's own second clause — *"function within the context established by primary gravities"* — is what three reinforcing relations with three Primaries (1, 3, 6) and no competing relation with anything actually describes. The row is not evidence against the classification. It is not evidence *for* it either, and the document never claims it is; it rests Supporting entirely on the 411 material.
4. **Every file line the *Gesta* read cites exists and carries substantially what is claimed of it.** 126796, 126791, 126798–126799, 126804, 114365, 114369, 113800, 114810, 118124, 122189, 117505, 125505, 118422, and all fourteen act lines — each opened with context. Not one is a fabrication or a misnumber.
5. **The roster-drift correction is exactly right.** `ACTORES VII.` sits at **113068** and `Augustinus Uipporegiensis` at **113076**; Registry row 65 cites 113067 and 113075. `Language: lat` is at **line 26** of the file. `Doc02_Round30_Review.md` does say what is claimed of it, including the deliberate decision not to hand-patch pending the fleet-wide fix. The read's decision to cite current lines, name the drift, and leave row 65 alone is correct and correctly reasoned.
6. **All fourteen acts on Registry row 65's list are genuinely present at the fourteen named lines**, verified one at a time. Act 14 at 125505 genuinely prints `Angustinus episcopus` and is genuinely a fifteenth instance not on that list.
7. **Constitution Article 21 is verbatim as quoted.** *"Whether a world contains distinct internal strands is a construction finding that, once made, governs all subsequent strand attribution; where strands exist, convergence across them is a test of a gravity's centrality."* Strand is defined as *"a meaningfully distinct pattern of formation emphasis, practice, authority structure, or ecological orientation within a single world, not merely a variation in detail."* Article 21 contains **no** reopening trigger, exactly as §5 states.
8. **§5's substantive Article 21 argument is sound on its own terms.** "A single episcopate disputing the scope of its own collective mandate, before a judge, is one authority structure in operation, not two" is a correct application of the Article 21 definition — the 411 record does show two *parties*, but Doc_01 §5 places the Donatist hierarchy outside this world's boundary, so no second in-world pattern of authority structure is evidenced. The argument is fit for purpose; the problem is what sits four hundred words above it (H2).
9. **Doc_01 §8 item 10 is quoted verbatim, bracket and all**, and its heading really does end *"not yet closed."* `with particular weight` really is Doc_01 §4's own phrase (line 79) as well as §8 item 7's; `the closest call`, `closer to this world's own ordinary exercise of office than the other two axes are`, and *"The conciliar-authority axis is different in kind, and this document does not fold it into that same account"* are all verbatim at Doc_01 §4 line 77.
10. **CF V7.4's Primary and Tensional definitions are verbatim as quoted**, and the gravity definition (*"A gravity is a force around which multiple dimensions organize. A topic recurs. A gravity organizes."*) is verbatim at Part III's Core Historical Gravity Discovery. The Template's `did-not-reach-gravity-status` label is genuinely at Template §4 and genuinely absent from CF V7.4 Part III.
11. **Round 4's H3 is genuinely and correctly fixed, and the fix was re-derived rather than copied.** `right of communion` occurs **0 times** in `Source_Registry.md` and **1 time** in `Doc_03_Lexicon_Candidate_List.md`, at row 54's "communion (preserved despite disagreement)" entry — which is where Doc_04 now points it. This is the first time in this series that a repointing fix has been verified at its new target before being written.
12. **The thirteen findings reported outstanding are genuinely outstanding, individually tested.** L1's severed `§2` still sits at line 56 (a line this pass *did* edit); L4's subjectless *"Supporting rather than load-bearing:"* is still at line 173; C2's lowercase *"reconstructed). the conciliar-authority disagreement"* is still at line 173; M2's spliced 113 figure, M3's "genuinely lapsed" closure, M4's revisitation reading and M5's ambiguous-results gap are all untouched. The pass did not quietly fix anything it reported open.

---

## HIGH

### H1 — §7 Open Item 3 still states the superseded classification as settled fact; the search the pass says it ran matched that line; and the Decision Log certifies, in terms, that no such residue exists

**Sites:** `Doc_04_Gravity_Discovery.md` line 211 (§7 Open Item 3 — **byte-identical to `ccb25f37`**, and to `b2e93cac`); `lpc_Decision_Log.md` line 652; Doc_04 line 3 (Status); Doc_04 line 229 (§8).

Open Item 3 reads, at HEAD:

> *"This candidate did not, in the end, need that label: **Candidate 5 is classified Tensional, a real Framework category, once the Supporting and Tensional definitions are actually run against it (§3 above) rather than reached past.**"*

Three separate certifications are false because of this one line.

- **The Status line** says the pass *"reconciles every site in this document that carried the superseded classification."* It does not.
- **The Decision Log**, line 652, says: *"a residue sweep confirmed the only remaining Tensional references are Candidate 8's own (genuinely Tensional, untouched) and the historical record in Open Item 6 and §8."* I enumerated all sixteen lines containing "Tensional" at HEAD and classified each. Fifteen are accounted for by that description. **Line 211 is not**, and it is the only live one. The residue sweep either was not run or did not return what the entry says it returned.
- **Round 4's H1 is reported resolved.** Round 4 named three sites: line 99, line 175, line 211. Lines 99 and 175 were rewritten. **Line 211 was not touched at all** — Round 4 had already flagged it as byte-identical to `ccb25f37`, and it is still byte-identical now, one round later.

This is worse than Round 4's H1, not better. Round 4's diagnosis was that the destination *list* was copied and therefore incomplete. The pass adopted the remedy — derive the list by searching — and line 211 **contains both `Candidate 5` and `Tensional`**. The search matched it. The failure has moved from *not finding the site* to *finding it and not acting on it*, which the adopted remedy cannot catch and the pass's own certification does not admit.

Open Item 3 is a carried-forward item addressed to whoever picks this document up next. It tells that reader the classification is Tensional, settled, on a test that §3 now says was never run and a label §3 now says nothing rests on.

**Fix:** rewrite Open Item 3's middle sentence to state the actual history and outcome — *"This candidate did not, in the end, need that label: it is classified **Supporting** (project lead's ruling, 2026-09-14), reached by running the Framework's own Supporting definition against it rather than reaching past the three real categories."* Then re-run the residue sweep and correct the Decision Log sentence to say what the sweep actually returns.

### H2 — §5 certifies the item-10 trigger "not met" and certifies the *Gesta* unread, four hundred words above the Finding that says the trigger is met and the Decision Log entry that says the same

**Sites:** Doc_04 line 173 (§5 — the pass edited the first third of this line and left the rest); line 175 (§5's Finding); `lpc_Decision_Log.md` line 650.

Line 173, at HEAD, still contains all of this:

> *"**This document re-weighed Doc_01 §4's own two quotations — the 256 preface and *On Baptism*'s "authority of plenary Councils" — and surfaced no evidence Doc_01 had not already weighed. The trigger is therefore not met**..."*
>
> *"...That second limb is the **escalated** question (§3), and nothing here rests on it. **Bound stated with the finding...** Candidate 5's Repetition and Persistence tests above disclose that this document has **not** read the *Gesta Collationis Carthaginiensis*... **If a targeted read surfaced such material it would be evidence Doc_01 has not weighed, and item 10's trigger would be met.** Carried as §7 Open Item 6."*

Line 175, the next paragraph:

> *"The trigger turns on Doc_04's own formal six-test assessment surfacing evidence Doc_01 has not weighed. **It now has: the 411 Conference material is evidence Doc_01 never weighed.**"*

And the Decision Log, line 650: *"the 411 material **is** evidence Doc_01 never weighed, so Doc_01 §8 item 10's reopening trigger is now met on its own terms."*

So the document asserts, in §5, both limbs of a contradiction; the escalation is described as live in a paragraph that §3 says is closed; and the *Gesta* is described as unread in the same section whose Finding rests on having read it. This is not ambiguity — line 173's sentences are bolded certifications.

**And the contradiction has a governance consequence the pass does not engage.** Doc_01 §8 item 10's full sentence, verified verbatim, is: *"...until and unless Doc_04's own formal six-test assessment, weighing this axis directly, surfaces evidence this document has not weighed — **in which case the finding is reopened rather than defended past the evidence**."* Doc_04 quotes the antecedent and drops the consequent at every site. Having now conceded the antecedent is satisfied, §5 declines the consequent and substitutes a fresh substantive argument on Article 21's strand definition. That argument may well be right (clean-check 8 above). But item 10 does not authorize substituting it: on item 10's own terms the finding is reopened, and the reopened finding then stands or falls on the Article 21 argument. The difference is not cosmetic — "reopened and re-affirmed" and "never reopened" are different records for Doc_05 and Doc_07 to inherit.

**Fix:** delete the "trigger is therefore not met" certification and the entire "Bound stated with the finding" passage from line 173, both now false. Then state the item-10 consequent explicitly: the trigger is met, the finding is therefore reopened per item 10, it is re-run against Article 21's strand definition on the 411 evidence, and it is re-affirmed — with the reason. Route the reopening through CO-022 category 3 or 4 rather than absorbing it, since it changes a determination Doc_01 already cleared.

### H3 — §7 Open Item 2, the instruction carried forward to Doc_05, Doc_07 and Doc_08, now contradicts itself in a single sentence — a defect this pass created

**Site:** Doc_04 line 210 (§7 Open Item 2 — new text in this pass).

> *"Carried forward to Doc_05/Doc_07/Doc_08: those later steps **should not treat the conciliar-authority disagreement as a Primary or Supporting, world-organizing gravity, but should treat it as a Supporting gravity organizing a significant portion of the ecology**..."*

The pre-pass sentence read *"should not treat it as a Primary or Supporting, world-organizing gravity, but..."* and continued with the bounded-residue characterization. The pass rewrote the clause after "but" and left the clause before it standing. The result instructs three downstream documents both to refuse and to adopt the same classification.

**Why HIGH.** Open Item 2 is the single highest-consequence sentence in §7 — it is the instruction three later steps will read instead of re-deriving the classification. It is new text, written by the pass whose entire purpose was reconciling this proposition, and it is self-nullifying. A downstream builder who follows it cannot proceed; one who resolves it by picking a half will pick without knowing they chose.

**Fix:** *"those later steps should not treat the conciliar-authority disagreement as a Primary, pervasively formation-shaping gravity, and should not treat it as a merely theoretical difference between the two anchor figures; they should treat it as a Supporting gravity..."*

### H4 — Supporting is certified against a one-clause quotation of a three-clause definition, with a distinguishing gloss that is not in the Framework — the identical defect Round 2's H5 raised against Tensional, now repeated for the label that replaced it

**Sites:** Doc_04 line 99 (§3's Classification paragraph — new text in this pass); line 164 (§4's Classification cell — new); line 210 (§7 Open Item 2 — new); `lpc_Decision_Log.md` line 648.

CF V7.4 Part III, Gravity Classification, verbatim and in full:

> *"Supporting Gravities organize significant portions of the ecology but function within the context established by primary gravities. They pass multiple gravity tests but may not demonstrate the same breadth of dependency or persistence."*

What Doc_04 line 99 says:

> *"It does meet **Supporting**, whose Framework definition is that a gravity 'organize[s] significant portions of the ecology' **without the pervasive formation reach Primary requires**."*

Two defects, both of the shape this document has now been found to have four times.

- **The definition is quoted to its first clause and stopped.** The two clauses that actually distinguish Supporting from Primary — *"function within the context established by primary gravities"* and *"may not demonstrate the same breadth of dependency or persistence"* — are never quoted and never run, at any of the four sites. Round 2's H5 found Tensional *"quoted but never argued"* because *"the operative limb… was never run."* §3's own escalation paragraph (line 103) recites that history as corrected. It is not corrected; it has been transferred.
- **The distinguishing gloss is invented.** *"without the pervasive formation reach Primary requires"* appears nowhere in CF V7.4. It is a negation of the *Primary* paragraph, imported to stand in for the Supporting paragraph's actual distinguishing clauses. That is precisely the *"importing a later paragraph's own stricter test"* move that §5 line 173 congratulates itself for avoiding on the gravity definition.

The second omission is not neutral. The Framework says Supporting gravities *"may not demonstrate the same breadth of dependency or **persistence**"* — and Persistence is the single test the entire reclassification turns on. Running the actual definition would require saying what Candidate 5's Dependency breadth is (line 91: passes *narrowly*, on one construction finding, with *"no candidate below depend[ing] on this axis"*) and what its Persistence breadth is (one preface in 256, one treatise c. 400, one conference in 411). Neither is engaged anywhere.

**Why HIGH.** The classification is the project lead's ruling and this review does not reopen it. But Doc_04 is the document of record for *why* the label fits, and it certifies the fit against a truncated quotation plus a fabricated clause — in bold, as "the Framework's own definition," at four sites, in a pass whose stated subject is correcting exactly this.

**Fix:** quote the Supporting paragraph in full at §3 and run all three clauses. If Dependency breadth and Persistence breadth are the narrow limbs, say so — the Framework's own definition anticipates that, and a candidate that fits Supporting *because* of the "may not demonstrate the same breadth" clause is better supported than one that fits a phrase.

### H5 — The *Gesta* read's load-bearing inference is not supported by the passages it cites: the *mandatum* at 411 is a procuratorial litigation instrument, and one of the two principal disputants expressly distinguishes the mandate formalities from the cause of the faith

**Sites:** `Doc04_Gesta_Targeted_Read_2026-09-14.md` Findings 1 and 2, and the "What this does to the test" section; Doc_04 line 94 (Persistence — new text in this pass); `lpc_Decision_Log.md` line 646.

The read's heading for Finding 1 is: *"the *mandatum* is an **inter-episcopal authority instrument**, operative and contested."* Doc_04 now carries that into the live document as the falsification of the Persistence absence claim. I read the surrounding context at every cited line and at the mandate's own recitation.

**What the mandate actually is, from the text itself.** At the recitation beginning line 122190ff the scan carries the instrument's own opening: *"Januarianus, Primianus, Felix, Donatus, Candorius, Optatus, Donatianus, Antonianus, Victorianus, Fortis et ceteri — Primiano, Petiliano, Emerito, Protasio, Montano, Gaudentio, Adeodato coepiscopis nostris… salutem. Mandamus vobis…"*, and a few lines on, *"…causam, defensoresque vos facimus adversus traditores persecutoresque nostros, qui nos in judicio…"* — normalized: *we make you our defenders in the cause, against our persecutors, who [bring] us into court*. That is a **procuratorial mandate**: a party's principals authorizing seven named advocates to conduct its case before a state-appointed judge. It is signed by each principal with the formula *mandavi et subscripsi* (~130 instances of `Mandavi`/`mandavi` and variants in the acts span — none of which the read found, see M3).

**What the dispute over it actually is.** At line 117505, which the read cites and paraphrases neutrally as *"a legal argument… about whether the mandate of the remainder is superfluous where one holds it,"* the speaker is **Emeritus**, in act 41, and his argument runs the opposite way to the read's framing:

> *"Fidei causa est, quae et sine mandato ipso iure agi potest… Quid est quod de mandato, vel de obligatione mandati, de subscriptione, de modo, de formulis, quaeritur?… cum singuli quique propriam causam et salutis suae negotium gerant, superfluumque sit ceterorum mandatum, cum in uno consistat Ecclesiae tota persona?"*

Emeritus is arguing that the mandate formalities are **beside the point** — this is a cause of faith, pursuable without a mandate by law itself — and he goes on in the same speech to set *forensis altercatio iurisque conflictus* and *merita iuris praescriptionemque causarum* against *"simplex illa veritas qua datur vita."* The participants themselves characterize the mandate wrangle as forensic procedure distinguishable from the substantive cause. That is direct source evidence **against** reading the mandate dispute as evidence of conciliar-authority theory in contest.

**And the axis is not this axis.** Doc_01 §4, verbatim at line 77, defines the conciliar-authority axis precisely: *"What changes on this axis is not a bishop's relation to a rival hierarchy but the appellate structure above the individual bishop within his own communion — whether a plenary council can overrule a provincial one, or an individual bishop's own judgment, in a way the 256 preface's own ecclesiology refuses."* Whether seven delegates hold valid standing to represent a litigating party is not that question. The read never states the axis it is testing against, never quotes Doc_01 §4's definition of it, and never asks whether its evidence reaches it.

**Why HIGH.** This is the single inferential step between the source and the classification. The read asserts it in a heading and never argues it. Doc_04 line 94 now states it as established in the live document: *"Inter-episcopal authority structure is **operative**… It is **contested** as a question of authority structure, not merely invoked."* The source shows a procedural standing dispute that one disputant explicitly frames as *not* the cause of faith.

**This is not a finding that no such evidence exists in the source.** It does — see L6, which names the sentence the read should have cited and did not. The finding is that the read did not establish its conclusion from the passages it chose, and the document now asserts the conclusion on their strength.

**Fix:** state the axis being tested, from Doc_01 §4's own definition, before drawing an inference. Then argue, explicitly, whether a procuratorial mandate contested on standing reaches it — including Emeritus's own contrary framing at 117505, which must be quoted rather than neutralized. Where it does reach it (Aurelius at act 40), cite that instead.

### H6 — The read's episcopal census is drawn from a span that is substantially Migne's editorial footnote apparatus, and one of its two named subscribers is a seventh-century bishop from a note on the Lateran Council of 649

**Sites:** `Doc04_Gesta_Targeted_Read_2026-09-14.md` Finding 3; Doc_04 line 94 (*"the subscription region alone (118400–123000) carries 250 `episcop-` tokens across dozens of named bishops"* — new text in this pass); `lpc_Decision_Log.md` line 646.

The read calls lines 118400–123000 *"the subscription region"* and counts within it. That span is **not** a clean subscription region. It interleaves the day-one *recognitio* and subscription text with Migne's own dense editorial apparatus: **117 lines in the span begin with a footnote marker** of the form `(NN)`, and the apparatus repeatedly identifies African sees by reference to the **Lateran Council under Pope Martin I (649)** — at lines 119181, 119445, 119834, 119842, 119871, 120285, 121452, 121468, 121505, 121860, 121881, 121902, among others.

The read's second named example is from exactly that apparatus. Line 119042 reads:

> *"Synodicae episcoporum Byzacenorum ad Constantinum in concilio Lateranensi sub Martino subscribit **Constantinus episcopus sanctae Ecclesiae Heliensis**"*

— immediately followed by footnote *"(75) Cellensis. Duae fuere huius nominis Ecclesiae in Africa…"*. The read presents this as *"Named bishops subscribing include Assellicus of Tusuros (line 118422) and **Constantinus (line 119042)**, among many others."* Assellicus is genuine — at 118422 he answers the roll-call *Praesto sum*. **Constantinus at 119042 is not a subscriber at the 411 Conference at all.** He is a bishop of Helia named in a nineteenth-century editorial note about a council held 238 years after the Conference.

The `250 episcop-` count is contaminated by the same apparatus. (It is also not reproducible: case-insensitive `episcop` over 118400–123000 returns **253**; case-sensitive lowercase returns **248**. Neither is 250, and the count excludes 35 instances of the OCR variant `cpiscop` plus `episeop`, `opiscop`, `episcnp` — see M3.)

**Why HIGH.** Finding 3 is the limb that carries *"contested among clergy far beyond the two anchor figures,"* which is half of what the read claims falsifies the absence claim, and Doc_04 line 94 now cites the 250 figure in the live document. A census run over a span whose composition was never characterized, producing one example from the wrong century, does not establish it. The underlying proposition is almost certainly true — real subscription formulae in quantity are visible at e.g. 121001–121012 — but it is not established by what was counted.

**Fix:** bound the census to the actual subscription/recognitio passages, exclude the apparatus, withdraw the Constantinus example, and re-derive the token count OCR-tolerantly.

### H7 — The pass's central methodological claim is unreproducible, and the four search terms are structurally blind to the one subsection that matters

**Sites:** Doc_04 line 3 (Status); line 229 (§8); `lpc_Decision_Log.md` line 652.

Three statements, all certified:

> *"Every site carrying the superseded classification was located **by searching the whole document** for `Tensional|escalat|Candidate 5|Conciliar Authority` — **twenty-four lines** — rather than by copying any enumeration."*
> *"**Twenty-four destinations were re-read at HEAD after the edits; all carry the change.**"*
> *"A check can only be as complete as the set it runs over, so the set is now derived rather than inherited."*

I ran the search. It returns **37 matching lines at `b2e93cac`** and **36 at HEAD**. Twenty-four is not the result at either state, and the pass's actual diff touches **26** lines. Whatever "twenty-four" counts, it is not what the sentence says it counts, and the reader cannot reconstruct it. This matters more than an arithmetic slip because it is the certification of the remedy Round 4 asked for: a derived set whose size cannot be reproduced from the derivation is not auditable, which is the entire property the remedy was supposed to add.

**And the derivation is structurally incomplete.** I tested which lines of Candidate 5's own subsection the four terms reach. The answer is: the heading (84) and the classification-history paragraphs (103, 105) — and **nothing else**. Lines 86, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101 and 107 — the generation note, all six test bullets, the Cross-Check, the Forces notation, the Classification paragraph, the classification line and the "does not claim" paragraph — match none of the four terms. The subsection is headed by the candidate's name and its body refers to it as *"this candidate."* Two stale sites survive there (M5). The remedy Round 4 recommended has the same shape of hole as the defect it replaced; it is simply a different hole.

**Fix:** state the reproducible number, or drop it. Then add to the derivation the one term that would have closed it: the section-scope itself — every line between a `### Candidate N` heading and the next one belongs to the destination set for a change to Candidate N's classification, regardless of whether the line names it. And retain a pronoun sweep (`this candidate`, `this axis`, `the axis`) for prose outside the subsection.

---

## MEDIUM

### M1 — Round 4's M1 is reported resolved; the defect survives at Round 4's own named site, unedited

Round 4's M1 names **line 173** and the Decision Log. The emphasized quotation is still there, byte-identical, presented as what a governing framework *reads*:

> *"CF V7.4 reads "They *may* not organize as broadly as primary gravities **but they prevent the ecology from being reducible to its primary forces**""*

Verified against `word/document.xml`: the Tensional paragraph is a single run with no `<w:b/>` and no `<w:i/>`. The emphasis is not in the source and no "emphasis added" is stated. What the pass *did* was add a parenthetical at line 106 — *"(quoted here without added emphasis; the `.docx` carries none, Round 4's M1)"* — attached to a **different, shorter quotation** at a **different site**. Fixing a finding at a site it does not name, while leaving its named site untouched, and then reporting the finding resolved, is the destination-check failure mode in a new direction.

### M2 — Round 4's H6 is reported resolved; its own (b) limb is not fixed, and H1 and H4 are not fixed either, so "seven resolved" is at best three

Round 4's H6(b) asked the Status line to carry Round 3's verified tally into its Round 2 sentence. The Status line still reads *"The preceding Round 2 fix pass addressed **26 of Round 2's 27 findings**"* — the Round 2 pass's own headline — with no 22/4 tally anywhere; `22 genuinely fixed` returns 0 hits in the document. H6(a) and (c) were addressed; (b) was not.

Combined with H1 (line 211 untouched) and H4 (the "trigger not met" certification untouched) and M1 above, the pass's claim of **"H1, H2, H3, H4, H5, H6 and M1 — seven of twenty"** resolves to: **genuinely resolved 3** (H2, H3, H5), **partially resolved 4** (H1, H4, H6, M1). This is the **sixth consecutive overstated certification**, in the pass whose §8 line says *"five consecutive passes overstated what they had closed"* and whose Decision Log says *"the sixth should not."*

### M3 — The read's headline count of 58 undercounts by roughly forty per cent, through the exact failure mode the read documents and warns about in its own correction 3

The read states: *"The term appears **58 times** across the acts span (lines 113000–131000)."* Case-insensitive `mandat` over that span returns exactly 58, so the number is honestly derived from the pattern used. The pattern is the problem.

Enumerating every `manda`-initial token in the span shows the *mandatum*-family forms the pattern **cannot** match, because this scan routinely prints `t` as `l` or `i`: `mandalo` (8), `mandalum` (7), `mandali` (4), `mandaium` (3), `mandaio` (3), `mandaii` (3), `mandala` (2), `Mandalum` (2), plus singletons `mandalorcs`, `mandalnn`, `mandaliim`, `mandaiii`, `mandaiee`, `mandaiam`, `mandaia`, `Mandaluni`, `Mandalo` — roughly **40 further tokens**, putting the true figure near 95–100. Three of the read's own cited lines print excluded forms: 114366 (`mandali`), 126791 (`mandaii`), 122189 (`mandatnm` — matched) and 117487–117491 (`nandaiun`, `nandaii`, `mandarunt` — none matched).

The read's own correction 3 says: *"This is the same mechanism this build has recorded across five review rounds: a search too strict for the text it was run against, then trusted because it returned something."* It then ran exactly that search for its headline count and did not re-test it. The figure is now in the live document at Doc_04 line 94 (*"the term recurring 58 times across the acts span"*). The error runs *toward* the read's conclusion being understated, not overstated — which is why it is MEDIUM — but a count offered as evidence of density cannot be forty per cent low and still be the count.

### M4 — The read certifies act 14 as "a fifteenth"; there is at least a sixteenth, and it is precisely the kind row 65 warned the floor was hiding

Running an OCR-tolerant line-initial scan built for this scan's substitution set across lines 110000–135000 returns **sixteen** numbered acts in which Augustine speaks: the fourteen on row 65's list, act 14 at 125505, and **act 230 at line 129294**, printing `Autjuslinus` (`t`→`tj`):

> *"230. Autjuslinus episcopus Ecclesiae catholicae dixit. In Ecclesia sumus, in qua Caecilianus episcopatum gessit et diem obiit…"*

A genuine speech act, with the full formula, in an undamaged stretch. The read's third pass — *"checking each named act number directly rather than trusting the scan"* — could not find it by construction: it checked the fourteen named numbers. Registry row 65 already says *"Still a floor: mid-line instances and **heavier garblings** are not counted"*; `Autjuslinus` is a heavier garbling, which is to say row 65 predicted this instance and the read did not look for it. The Decision Log now records act 14 as "a fifteenth" as a closed correction to the record.

### M5 — Two stale sites survive inside Candidate 5's own subsection, both invisible to the four search terms, both contradicting text the same pass wrote

**Line 96, the Confidence/Gravity Cross-Check**, unedited: *"…their organizing breadth is not supported at the same level, **this candidate's own six-test profile above being narrow at best**. The classification is set by that profile and is **not** upgraded…"* The profile above is no longer narrow at best — it now carries two clean passes (Repetition, Persistence), per line 99 and §4's row; and the classification *was* upgraded, from Tensional to Supporting, by this pass.

**Line 97, the Forces-connection notation**, unedited: *"better described as **a live, unresolved theoretical residue of the century-gap itself**… the residue is recorded at **§7 Open Item 6 rather than treated as discharged**."* Line 99, two lines below, says the candidate is *"not a theoretical residue visible only between two bishops a century apart, which is what the earlier profile described and **what the evidence no longer supports**."* And §7 Open Item 6 is now headed *"**Discharged** 2026-09-14."*

Neither line contains `Tensional`, `escalat`, `Candidate 5` or `Conciliar Authority`. These are the sites H7 predicts.

### M6 — The read's OCR-hazard disclosure names one range for "two regions" and excludes from its scope the regions it actually draws from

The read states: *"**Two regions** (roughly 128470–128500) carry two-column bleed severe enough that nothing is drawn from them."* One range is named. And the disclosure is not accurate as a characterization of the scan around the read's own load-bearing citations:

- **126781–126783**, four lines above act 50, is fully bled: *"SC scqiii liOC ipsuni | jaclurain aulciil f;iccrc ini|.c- forial , suidoi iiiii am…"*
- **126758–126795**, the act 49 context the read cites for Emeritus, is severely garbled and carries an unattributed embedded `\iujuiiliiiin tpiteoput ttixil.` (Augustinus episcopus dixit) at ~126764 that the read's line-initial method cannot see and does not mention.
- **130290–130315**, from which the read draws acts 265, 272 and 267, is column-interleaved — which is why **act 272 sits at 130298 and act 267 at 130313**, out of order, a fact the read's own "confirmed at named file lines" list reproduces without remark.

128470–128500 is genuinely bad; it is not the only such region, and it is not where the load-bearing material is.

### M7 — The Decision Log does not now read coherently: the merge re-inserted a claim the next entry retracts as false, with no in-place correction

At `b2e93cac` and `b419357b`, `lpc_Decision_Log.md` contained one instance of the Round 27 claim. The merge at `c3b31c8b` brought in a second, from `5aa68053`, at **line 510**, inside the 2026-09-09 (later still) entry:

> *"**What remains open, and is not closed by this disposition.** Round 27's twelve findings, deferred on scope grounds and unfixed."*

Four lines below it, the 2026-09-10 entry: *"…both lines of work merged, **the false 'Round 27 unfixed' claim retracted**"* and *"The 'Round 27 unfixed' claim is false and **is retracted in place** in the three documents above, per this document set's own established convention of correcting a sourcing or factual conclusion **in place with the correction disclosed**, not by deleting the record of the error."*

Line 510 carries no in-place correction — no marker, no pointer forward, nothing (`retract`, `corrected`, `false` all return 0 in lines 506–512). The log therefore asserts as an open item, in one entry, exactly the claim the next entry certifies as retracted in place. A reader working forward inherits the false belief and only loses it four paragraphs later, by accident. The reconciliation pass rewrote this file and did not check what the merge had put back into it.

### M8 — "Persistence passes at the world level" is stated flat; the absence claim's second limb is not falsified, and the document concedes as much two lines later

The absence claim under test, quoted by the read itself, has a second limb: *"or that it was operative or contested **among ordinary clergy** — only between two specific bishops at two specific moments separated by over a century."* The read reports *"Both are falsified,"* and Doc_04 line 94 now reads *"**Passes at the world level**"* with no qualification.

The 411 evidence falsifies *"only between two specific bishops at two specific moments"* — that limb is genuinely dead, and this review does not dispute it. It does not establish the other half: the participants are **bishops**, an episcopal college convened as a college. Doc_04 itself says so, at line 107: *"the *Gesta*… shows the question operative among **bishops**, not among catechumens or ordinary believers."* Ordinary clergy — presbyters, deacons, readers — are not evidenced. The sub-limb the absence claim actually asserted is unrefuted, and the document both concedes it and certifies the whole claim falsified, eight lines apart.

Separately, on "world level": this world spans c. 246–430 and the evidence is one preface (256), one treatise (c. 400), and one conference (411). That is three loci across 185 years, two of them within a decade in one phase. That may still be a pass; it is not the same as the flat, unqualified *"Passes at the world level"* the bullet now asserts in bold, with nothing carried from the Repetition bullet's own admission that Cyprian's pole still has no second locus.

---

## LOW

### L1 — The read presents four *capitula* citations "in sequence"; they come from at least two distinct capitula series, in neither file order nor number order
114365 is capitulum 49, 114369 is 50, **113800 is 151**, and 114810 is 164. The read lists them 114365 → 114369 → 113800 → 114810, so item three sits 565 lines *before* items one and two in the file. The read's own quotation-discipline paragraph warns that act numbers *"recur in the *capitula*… and again in the acts proper"*; it then presents a cross-series list as a sequence without saying so.

### L2 — The 58-count span mixes *capitula* with acts and is labelled "the acts span"
Lines 113000–131000 include the *capitula* (113800, 114365, 114369, 114810 are all in it) as well as the acts proper. Each mandate reference summarized in a capitulum is therefore counted twice — once in the table of contents, once in the body — inside a figure presented as recurrence across the acts.

### L3 — "47 distinct `Name episcopus` forms" is not reproducible
A straightforward `[A-Z][a-z]+ +episcopus` over 118400–123000 returns **72** distinct forms — including place-adjectives read as names (`Vinensis`, `Telensis`, `Igilgitanus`, `Membressilanus`, `Numidia`, `Ulunnensis`) and OCR junk (`Ux episcopus`, `Hs episcopus`, `Hujus episcopus`, `Hanui episcopus`). The read hedges the *interpretation* well (*"no precise figure is asserted here"*) but the number 47 is stated as a count and cannot be reconstructed.

### L4 — The act-50 normalization is assigned to one line, spans three, and silently adjusts a spelling
The read says *"At **line 126796**, normalized: *Augustinus episcopus Ecclesiae catholicae dixit. Legatur mandatum nostrum, et intellegent quam cuncta contineat.*"* Line 126796 carries only the speaker formula; the sentence runs to 126797 and ends on **126798**, which is the same line the read separately assigns to Petilianus. Separately, the scan prints `inlclligcut` — normalizing to *intelligent*, not *intellegent*. The substitution is defensible as orthography but is not disclosed, and the read's stated rule is normalizations of what the scan prints.

### L5 — Act 158 is presented as one of "fourteen acts… confirmed present" without the caution Registry row 65 already carries
Line 121764 reads, in full, *"158. Augustinus episcop"* and is followed by a heavily damaged passage carrying the subscription formula *"…Carthagini constituto, praesente viro clarissimo tribuno et notario Marcellino, [hoc] mandatum suscepi et subscripsi."* Row 65 already records that act 158 *"truncates at `158. Augustinus episcop` and carries none of the formula the others share, so it does not support a claim about the recorded form."* The read drops that caution and lists 158 with the other thirteen as flatly confirmed — and, in the same document, treats 121764 as falling inside its own "subscription region" (118400–123000). It is both an act number and a subscription entry; the read never reconciles that.

### L6 — The strongest genuinely on-axis sentence in the source was missed, and `concili-` was never searched at all
At act 40, beginning line 117487, **Aurelius of Carthage** says (normalized):

> *"Nec enim egredi possumus limitem istius mandati, quod nobis patres vel fratres nostri **universalis concilii Ecclesiae catholicae**, hic apud Carthaginem constituti, mandarunt."* — *We cannot go beyond the limit of that mandate which our fathers and brothers of the universal council of the catholic Church, assembled here at Carthage, mandated to us.*

A council issuing a mandate whose limits bind its own delegates, said on the record by the primate of Carthage, is on Doc_01 §4's axis in a way the standing dispute is not. The read's `mandat` pattern cannot reach it (the scan prints `nandaiun`, `nandaii`, `mandarunt`), and the read never ran `concili-` at all — which returns roughly **100 occurrences** in its own 113000–131000 span, `concilio` alone 78 times. A read commissioned to test a *conciliar-authority* question searched one term and it was not that one.

### L7 — Round 4's L1 sits on a line this pass edited, and is reported outstanding without noting that
The pass rewrote line 56 to fix Round 4's H3 (the "right of communion" attribution). L1's defect — *"…where disagreement does not sever fellowship). §2 (Cyprian's Influence…"*, a `§2` severed from its `Doc_02` head by a full stop — is in the same sentence and was left. Reporting it outstanding is accurate; not disclosing that the pass had the line open and did not take it is not.

### L8 — The Forces Framework rule is attributed to §4 (Step 4); it is in the Layer 3 section
Doc_04 cites it twice — line 97 (*"Forces Framework V1.1 §4 (Step 4) states that…"*) and line 214 (*"Forces Framework V1.1 §4's rule…"*). Verbatim, *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete"* sits in the **Layer 3 — Formation Impact** block, which precedes *"Section 4 — Integration with the Construction Process"*; §4's own Step 4 entry is a different paragraph (*"Each confirmed gravity is assessed against the forces analysis…"*). The quotation is exact; the location is not. Round 4's clean-list item 10 certified *"Section 4's Step 4 entry read verbatim,"* so this has now survived two rounds.

---

## COSMETIC

### C1 — A new sentence-case defect, introduced by this pass, of the same shape as Round 4's C1
The Disposition previously read *"…answers **Round 3's** findings; per CO-022, a substantial revision returns…"* — a semicolon, so lowercase was correct. The pass rewrote the clause to end in a full stop and left the following word lowercase: *"…the remainder are outstanding and listed in §8. **per** CO-022, a substantial revision returns…"* Round 4's C1 was *"the C2 fix introduces a new sentence-case defect at the same sentence"*; this is the same move.

### C2 — §5's Finding renders its emphasis inverted
Line 175 opens a bold marker immediately before "Finding:" and closes one at the paragraph's end, with two further bold pairs nested between them. Markdown pairs them greedily, so the sentence the author bolded (*"An earlier version rested it on exactly such a claim…"*) renders plain and the sentence they left plain (*"The trigger turns on Doc_04's own formal six-test assessment…"*) renders bold. Parity is even, so no parity check catches it.

### C3 — §2 carries a lowercase sentence start
Line 20 ends a bolded sentence with "…it is not one candidate." and begins the next with a lowercase "what recurs across the two bishops is not one evidentiary base…". Pre-existing, not on Round 4's list, not introduced here.

---

## Fix-pass verification table

| Round 4 finding | Status at `c3b31c8b` | Note |
|---|---|---|
| H1 — escalation carried to §3's four listed sites and no others; lines 99, 175, 211 | **PARTIALLY RESOLVED** | Lines 99 and 175 rewritten and correct. **Line 211 (§7 Open Item 3) untouched — byte-identical to `ccb25f37` and to `b2e93cac` — and still states "Candidate 5 is classified Tensional."** The pass's own search matches that line. Reported resolved (R5 H1) |
| H2 — §5's Finding restates the struck Tensional misstatement and re-rests the non-reopening on the escalated label | **GENUINELY RESOLVED** | `by definition does not organize broadly` returns **0** hits. Line 175 rewritten; the classification-dependent premise removed. Correct |
| H3 — the "right of communion" clause repointed to Registry row 4, where it occurs 0 times | **GENUINELY RESOLVED** | Now points to Doc_01 §4/§5 and Doc_03's "communion" entry, with the false attribution disclosed. Re-verified at source: 0 in `Source_Registry.md`, 1 in `Doc_03` row 54. Correct, and correctly re-derived |
| H4 — §5 certifies item 10's trigger "not met" on a narrower test | **NOT RESOLVED** | The certification is **still at line 173, unedited**, alongside the claim the *Gesta* is unread. Line 175 now says the trigger **is** met. The finding was not fixed; it was contradicted (R5 H2) |
| H5 — "stands either way" contradicts the Dependency bullet | **GENUINELY RESOLVED** | Line 91 rewritten: the contingency is now scoped to *evidence* rather than *label*, and the distinction named. Coherent with lines 105 and 173 |
| H6 — certification overstated; (a) counts, (b) Round 2 headline, (c) Decision Log | **PARTIALLY RESOLVED** | (a) and (c) addressed. **(b) not:** the Status line still reads "26 of Round 2's 27 findings"; `22 genuinely fixed` returns 0 hits (R5 M2) |
| M1 — the §5 Tensional quotation carries emphasis CF V7.4 does not have | **NOT RESOLVED** | The quotation is **still at line 173, byte-identical**, with emphasis, presented as what "CF V7.4 reads." A parenthetical was added at line 106, at a different quotation at a different site (R5 M1) |
| M2 — Candidate 1's 113 figure splices a row-scope | **OUTSTANDING — as reported** | Untouched. Correctly named |
| M3 — §5 closes the "disappeared gravity" question as "genuinely lapsed" against Doc_04's own Persistence finding | **OUTSTANDING — as reported** | Untouched. Correctly named |
| M4 — §5's revisitation reading stretches Article 21 | **OUTSTANDING — as reported** | The clause is inside line 173, which the pass edited; the clause itself is unchanged. Correctly named |
| M5 — CF V7.4's provision for ambiguous test results never engaged | **OUTSTANDING — as reported** | Untouched. Arguably narrowed in relevance by the ruling, but not addressed |
| L1 — Candidate 3's citation list severs "§2" from its head | **OUTSTANDING — as reported** | Still at line 56, a line this pass edited (R5 L7) |
| L2 — verbless fragments at two Cross-Checks | **OUTSTANDING — as reported** | Untouched |
| L3 — Candidates 4 and 7 certify a flat "Documented" from a two-name band | **OUTSTANDING — as reported** | Untouched |
| L4 — "Supporting rather than load-bearing:" subjectless fragment | **OUTSTANDING — as reported** | Still at line 173, 1 hit |
| L5 — Doc_01 §8 item 7 quoted with altered verbs | **OUTSTANDING — as reported** | Untouched |
| L6 — Open Item 4 attributes the purity/sufficiency candidate to Doc_03 | **OUTSTANDING — as reported** | Untouched |
| C1 — sentence-case defect at the C2 fix's sentence | **OUTSTANDING — as reported** | Untouched; and a new one of the same shape introduced at the Disposition (R5 C1) |
| C2 — lowercase sentence start in §5 | **OUTSTANDING — as reported** | `reconstructed). the conciliar-authority` still 1 hit |
| C3 — the escalation stated in four different forms | **OUTSTANDING / partly moot** | The escalation is closed; the closure is now stated in four forms instead |

**Totals, counted from the table and checked to sum: 3 genuinely resolved · 4 partially resolved · 13 outstanding · 0 silently fixed = 20.**

- **Genuinely resolved (3):** H2, H3, H5.
- **Partially resolved (4):** H1, H4, H6, M1 — of which **H4 and M1 are byte-identical at their own named sites.**
- **Outstanding as reported (13):** M2, M3, M4, M5, L1, L2, L3, L4, L5, L6, C1, C2, C3. **The pass's thirteen-outstanding claim is accurate in full.**
- **Silently fixed and misreported open (0).** **Broken further (0).**

**Against the pass's claim of "H1, H2, H3, H4, H5, H6 and M1 — seven of twenty":** four of the seven are not resolved, and two of those four were not edited at all. This is the **sixth consecutive overstated certification**, in the pass whose §8 line names the previous five and says the sixth should not repeat them. The honest half of the certification — the thirteen — is fully accurate, and that is a real improvement worth recording alongside the failure.

---

## Audit of the *Gesta* targeted read

**Verdict: OVERSTATED.** Not unsound in direction, not fabricated, and materially better sourced than anything else in this build's Candidate 5 history. But it does not establish its conclusion from the evidence it cites, and the document now asserts the conclusion on that evidence's strength.

**What survives audit, and it is substantial.** Every one of the fourteen named act lines, and every one of the eleven other cited file lines, was opened and checked. **Not one is fabricated, misnumbered, or misquoted in substance.** The Latin normalizations at 114369 (*quod mandatum suum universa contineat*), 114810 (*mandatum Catholicorum non debere disquiri*), 126796–126798 and 126804 (*ex mandati serie et ex praesenti professione*) are all defensible against what the scan prints, and the read's declared rule — normalizations, not quotations, cited by file line — is followed in substance throughout. The roster-drift correction is exactly right, correctly root-caused to `Language: lat` at line 26, correctly checked against `Doc02_Round30_Review.md`, and correctly declines to patch row 65. Act 14 at 125505 is genuinely a fifteenth instance. The read's disclosure of its own three-pass search failure is candid and is the most useful paragraph in the artifact. **The Persistence bullet's first limb — that Augustine's position is attested in a second, independent, non-treatise locus in his own recorded voice decades after *On Baptism* — is established.** Act 50 is real, Augustine speaks, and the subject is the scope of a collective episcopal authorization.

**Where it overstates, in descending order of consequence.**

1. **The inference from *mandatum* to conciliar-authority theory is asserted in a heading and never argued** (H5). The 411 *mandatum* is, on the text's own showing, a procuratorial instrument by which a party's bishops appoint seven *defensores* for a lawsuit (*"defensores vos facimus adversus traditores persecutoresque nostros, qui nos in judicio…"*). The dispute over it is a standing challenge. And **Emeritus, at the read's own line 117505, expressly separates the mandate formalities from the substantive cause**: *"Fidei causa est, quae et sine mandato ipso iure agi potest… Quid est quod de mandato, vel de obligatione mandati, de subscriptione, de modo, de formulis, quaeritur?"* The read paraphrases this line neutrally and loses the speaker, the polarity and the argument. Doc_01 §4 defines the axis as *"the appellate structure above the individual bishop within his own communion — whether a plenary council can overrule a provincial one, or an individual bishop's own judgment."* The read never quotes that definition and never tests its evidence against it.
2. **The census limb is built on a contaminated span with one example from the wrong century** (H6). 118400–123000 is not "the subscription region"; it is subscription text interleaved with Migne's footnote apparatus (117 marker lines; repeated citation of the Lateran Council of 649). "Constantinus (line 119042)" is a bishop of Helia named in one of those notes, not a 411 subscriber.
3. **The headline count of 58 is ~40% low**, excluded by the `t`→`l`/`i` substitution the read's own correction 3 documents as this scan's signature failure (M3).
4. **The act inventory stops one short.** Act 230 at 129294 (`Autjuslinus`) is a sixteenth instance, of exactly the "heavier garbling" class row 65 said the floor was hiding (M4).
5. **"Both limbs falsified" is half true.** The "only between two specific bishops" limb is dead. The "operative or contested among *ordinary clergy*" limb is not established — the 411 record is an episcopal college, which Doc_04 itself concedes at line 107 (M8).
6. **The OCR-hazard scoping is inaccurate** — "two regions," one named, and neither of the two regions the read actually draws its most load-bearing material from (M6).
7. **It searched one term, and not the obvious one.** `concili-` returns ~100 hits in the read's own span and was never run. The single strongest on-axis sentence in the source — Aurelius at act 40, *"nec enim egredi possumus limitem istius mandati, quod nobis patres vel fratres nostri universalis concilii Ecclesiae catholicae… mandarunt"* — was missed, and it is the sentence that would have carried the inference the read asserts without it (L6).

**What this means for "Persistence passes at world level."** The honest statement the evidence supports is narrower than what Doc_04 line 94 now asserts: *a second, independent, non-treatise Augustine locus exists; the 411 record shows a mandate issued by a council of the African episcopate, binding its delegates, its scope litigated among named bishops on both sides and ruled on by the imperial cognitor; that falsifies "only between two specific bishops at two specific moments"; it does not reach ordinary clergy, and the evidence that reaches conciliar authority as an appellate question (rather than as procuratorial standing) is one sentence at act 40 that this read did not cite.* That is still a pass, and probably still enough to move the candidate off a bounded residue. It is not *"Passes at the world level"* flat, and it is not two limbs falsified.

**On the process question.** The read was performed by the thread that then applied the ruling resting on it, and reached the build's live document through a Decision Log entry written by the same thread. That is not itself a defect — the artifact is explicit about its own commission and explicit that it "reaches no classification." But it is the first time in this build's history that a **primary-source read** has passed into a live classification without any independent re-derivation, and six of the eight defects above are the kind that a second reader opening the file would catch in an hour. The build's own repeatedly-recorded failure mode is *"a search too strict for the text it was run against, then trusted because it returned something."* This read names that mechanism, discloses having hit it twice, and then hits it three more times undisclosed — on the term count, on the act inventory, and on the term it never searched.

---

## Escalation-category assessment (CO-022)

Run against all four categories, with near-misses checked rather than assumed away.

**1. Representative-identity decisions — does not apply.** Nothing in Doc_04, the *Gesta* read or the 2026-09-14 Decision Log entry names, titles, characterizes or constrains this world's Representative. Doc_03's `[CT]`-withholding cells are untouched.

**2. Portfolio-level / cross-world decisions — does not apply, narrowly.** The IJC precedent claims at Open Item 3 and Candidates 4, 6 and 7 were not edited. The *Gesta* corpus-map assignment is applied, not made. The `Language: lat` drift is correctly left to the fleet-wide task and correctly not hand-patched, per Round 30's own reasoning. **Near-miss checked:** the read corrects the record on Registry row 65's act count (fifteen, now sixteen — M4) without editing row 65, which is the right call; the correction is recorded in this world's artifacts only, and row 65 is a shared-corpus row also relied on by the sibling Donatism build. Recording it in this world's Decision Log rather than proposing a Registry edit keeps it inside this world. That is a defensible boundary, and this review does not trip the category on it — but it should be noted that the sibling build's row 65 now carries a figure two worlds' evidence contradicts.

**3. Governance / methodology decisions — TRIPPED, at moderate intensity, and for the third consecutive round on the same limb.** Round 3 recommended the destination check; Round 4 found the destination *list* was the defect and recommended deriving it by search; this pass adopted that and the derived set is structurally blind to the subsection the change lives in (H7), while the one matched site it missed (H1) shows a derived set does not by itself close the gap either.

The discipline these three rounds keep circling is one sentence, and it is not "search harder": **the unit of reconciliation is the section, not the line.** A change to Candidate N's classification makes every line between `### Candidate N` and the next heading a destination, regardless of whether that line names the candidate — because a subsection's body refers to its subject by pronoun. Every failure in H1, H7 and M5 is closed by that rule and by nothing narrower. This is offered as a condition of this document's own remaining passes, not as a portfolio rule, per Round 4's own recommendation against escalating it.

**4. Unresolved tensions the pipeline can't close — RE-OPENED, on a limb the pass did not notice it had touched.** The Candidate 5 classification escalation is genuinely closed by the project lead's ruling, and this review takes no position on the label. But §5 now concedes that Doc_01 §8 item 10's reopening trigger **is met** (line 175; Decision Log line 650) while the same section certifies it **not met** (line 173) and neither site engages item 10's own consequent — *"in which case the finding is reopened rather than defended past the evidence."* Whether a Doc_01-level determination that Doc_01 itself made reopenable is reopened, re-affirmed, or simply held is not a question Doc_04 can settle by writing a better paragraph; Doc_01 §5 is a cleared, disposed document. **Recommend escalating the narrow question:** *the item-10 trigger is now met on its own terms; does the strand-singular determination reopen and re-affirm on the Article 21 argument at §5, or is it held unreopened?* Doc_04's own answer to that question is currently both.

**Result: two categories tripped — category 3 (governance/methodology), for the third consecutive round on the same migrating limb; and category 4, re-opened on the item-10 trigger question, which is narrow, answerable, and currently answered twice in opposite directions inside one section.**

---

## Note on disposition — deliberately not assessed

Consistent with this folder's practice across the Doc01, Doc02, Doc03 and Doc04 Round 1–4 series, this review does not recommend a disposition. Doc_04's Status line and Disposition both state that a substantial revision returns to independent review before disposition, and the Decision Log's 2026-09-14 entry self-applies none. That is correct on its own terms and is left alone.

Four observations offered without recommendations attached.

**First, the honest half should be credited.** The thirteen-outstanding enumeration is accurate in full, item by item, at HEAD. Nothing on it was silently fixed and nothing was broken further. After five rounds of overstated closure lists, a pass that names thirteen open findings and is right about all thirteen has changed something real, and the finding that it is still wrong about four of the seven it claimed should not erase that.

**Second, the *Gesta* read is the most valuable artifact this build has produced on Candidate 5, and it needed one more reader.** Six of its eight defects are visible to anyone who opens the file with a second search term. The lesson is not that the read was careless — it is more careful than most of the fix passes it feeds — but that a primary-source read that will carry a classification needs the same independent re-derivation that a *citation* gets, and it did not receive one before the ruling was applied.

**Third, the destination-check family has now failed three times in three different ways** — copied list (R3), matched-but-unactioned site (R5 H1), and derived-set blind spot (R5 H7). Each remedy addressed the previous failure and left a new surface. The section-scope rule at category 3 above closes all three; nothing narrower does.

**Fourth, §5 is now the least coherent section of the document**, and it is the section carrying an Article 21 determination forward to every subsequent step. Lines 173 and 175 assert opposite things about the same trigger, two paragraphs apart, both in bold, and the Decision Log sides with 175 while the document's own §7 Open Item 6 header sides with neither. Whatever else this document's next pass does, §5 should be rewritten whole rather than edited clause by clause — it has now been patched at the clause level in four consecutive passes and the incoherence has increased each time.
