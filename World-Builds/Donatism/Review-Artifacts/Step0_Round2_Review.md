# Step 0 Movement-Scope Confirmation (Donatism) — Round 2 Independent Adversarial Review

**Reviewed document:** `World-Builds/Donatism/Step0_Movement_Scope_Confirmation.md` (DRAFT v2, revised 2026-09-01)
**Checked against:** `World-Builds/Donatism/Review-Artifacts/Step0_Round1_Review.md` (22 findings — 4 high, 10 medium, 8 low)
**Reviewer:** independent isolated agent, no drafting involvement, dispatched per `cic-build-cycle`
**Review date:** 2026-09-01
**Overall verdict: SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**Sources re-extracted and re-read in full for this round (not carried over from Round 1):** `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx` (`word/document.xml`, tags stripped — full Sections A/B, Procedure, Governance); `CiC_Step0_Conclusion_FINAL_v2.docx` (same method — full text); `CiC_L1_Constitution_V2_2.docx` (version block, Article 4 "On the Scope of 'Movement'", Article 22 Forces Principle); `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` (status block, Record Integrity Principle, freeze gates); `CiC_L3B_Formation_World_Template_V1.5.docx` (Integrated Ecology Analysis — the eight lenses, enumerated directly from the document's own headings); `Syriac-Build/CiC_Coach3_Step0_Critique_2026-07-06.md`; `Imperial-Juridical-Christianity/Doc_01_World_Identification_Boundaries_Orientation.md` §6 and `Step0_Movement_Scope_Confirmation.md` §5–§6; `Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` (grep, Donatism occurrences); `cic/corpus-map/donatism.yaml`; `cic/texts/README.md`; `cic/engine/texts_registry.py`; `cic/texts/` directory listing; `world-build-docs/*/SOURCE-REQUEST-MANIFEST.md` and `records/*/search_record/*` (for the meaning of "G1"); `Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`; the `cic-build-cycle` SKILL text (four escalation categories, substantial-vs-cosmetic definition).

**Summary.** The revision is real work, not a cosmetic pass. Eighteen of the twenty-two Round 1 findings are genuinely fixed on independent re-check, including all three of the sourcing/provenance high findings (H1, H2, H3), and every quotation newly introduced in v2 that I could test against a primary source is character-exact. **But the revision introduced a new high-severity fabrication of exactly the class Round 1 existed to catch:** §3 B2's answer to M9 asserts a pass "across all eight lenses" against a list of eight lenses that is not this project's — it is an external religious-studies taxonomy, uncredited, that omits five of the Template's eight actual Integrated Ecology Analysis lenses. Four further medium findings are new, three of them defects introduced by the fixes themselves, and one of them is a "Corrected in v2" claim in §6 that is not accurate. H4 is partially open: the World #6 route Round 1 offered was taken legitimately, but the second limb of the category-4 analysis (the Step 0 Conclusion's own logged Article 3 interpretive question, which names this world) is still nowhere in the document while §6 asserts nothing unresolved remains.

---

## Part 1 — Round 1 findings, re-verified individually

Legend: **FIXED** = independently confirmed resolved against the actual source. **PARTIAL** = improved, but something is still wrong or the fix introduced a new problem. **NOT FIXED**.

### HIGH

| ID | Status | Evidence from independent re-check |
|---|---|---|
| **H1** — B5 quotation attributed to the Methodology that isn't in it | **FIXED** | "non-decisive" now appears exactly once in v2, inside the §3 B5 correction note that identifies it as the Round 1 error and attributes it correctly to IJC's own prose. The two strings v2 now quotes as the Methodology's B5 — *"a modest tiebreak, not a filter"* and *"where two candidates are otherwise comparable, the larger/more prominent movement gets modest priority as a tiebreak only; a small, thinly-known movement with genuinely strong evidence still screens in."* — are both character-exact against the extracted `word/document.xml` (B5 heading and body respectively). No content is carried across from the IJC document. |
| **H2** — Primary-gravity-first rule's origin misstated (#8/#9 → #4/#8), load-bearing in three places | **FIXED** | §1 now states the split is #8/#9 and quotes the Step 0 Conclusion's sentence in full — verified character-exact, including the previously-dropped qualifier *"— though partly mitigated there, since Cyprian's ecclesiology and pastoral crisis-management are historically fused rather than cleanly separable."* Donatism's role is restated as the third party whose distinctiveness was improperly shielded, which matches Decisions items 3–4 as re-read. Both propagations are corrected: §3 B3 no longer claims authorship and instead uses the qualifier where it bears (the shared Cyprianic root); §4 item 4 now says explicitly *"not as a rule this world's own history produced."* |
| **H3** — Both §3 boundary findings re-derived on-record work uncited; #6 inverted the prior disposition | **FIXED** | **#6 limb:** v2 now cites and adopts both prior treatments. The Coach3 quotation and the IJC Doc_01 §6 quotation (*"No overlap risk — a point of productive contrast, not a boundary question requiring vigilance the way World #5 does."*) are both character-exact against the sources; IJC Doc_01's status line does read "Cleared review (Round 2, COSMETIC ONLY) — Approved to proceed", so v2's characterization of it is accurate. The "vigilance required" assertion is withdrawn. **#8 limb:** Coach3 is now cited with an exact quotation and correctly marked ellipsis, and the shared-Cyprianic-root risk is added with the corpus map's `role: antecedent` ruling and its *"the authority both sides argued FROM"* note — both verified verbatim in `donatism.yaml`. (See new finding **N6** for an attribution overreach in B3's own concluding sentence.) |
| **H4** — §6's "no escalation category applies" not sustained by §3 and §5 | **PARTIAL** | **Category 2 — mostly fixed, one residue.** The forward-binding requirement on World #6's build and the "symmetrically… once World #8 is built" instruction are both gone ("symmetric" now appears only in §6's own description of what was removed). But §3 B3 still says the imperial-coercion material *"belongs… to World #6's eventual Doc_02"* — see **N2**: IJC's `Doc_02_Source_Ecology.md` already exists and contains zero occurrences of "Donatis*" (re-grepped), so this is both factually wrong about a completed build and a residual soft cross-world assignment that §6 claims was removed. **Category 3 — fixed.** "Established" is withdrawn; §5 now reports IJC's own *"this build's own reading, not a rule the text states directly"* (exact), and the two-case pattern is framed as disclosure. The case-application argument tracks IJC's own cleared reasoning. **Category 4 — the World #6 limb closes legitimately; the second limb does not.** Round 1's fix expressly offered "adopt the existing finding" as one of two permitted routes, and v2 took it; adopting a cleared neighbour document's finding genuinely dissolves the contradiction rather than dodging it, and I do not read that as an escalation-avoiding manoeuvre. But Round 1's category-4 analysis had a second, independent limb: the Step 0 Conclusion's *"Constitutional ambiguity flagged, not resolved"* entry — Article 3's undefined treatment of a formation-type recurring across a temporal gap *"(Cyprian/Augustine, with Donatism in between)… Logged as a standing interpretive question, likely to recur."* Re-verified present in the source. It is still not mentioned anywhere in v2 (grep: no "Article 3"), and §3 B3 — which now turns explicitly on the shared Cyprianic root and quotes *"occupying and contesting the interval"* — is precisely where it recurs. §6 nonetheless asserts *"No unresolved cross-document contradiction remains as of this revision."* |

### MEDIUM

| ID | Status | Evidence from independent re-check |
|---|---|---|
| **M1** — Criterion 2 never applied | **FIXED** | New §2 A2.5 applies the test. The Criterion 2 statement and the Novatianism redundancy line are both character-exact against `CiC_Step0_Conclusion_FINAL_v2.docx`. The clearing argument rests on the communal-tradition ground and the corpus map's `antecedent` ruling — the evidentiary basis Round 1 named — plus the opponents'-label point. (Minor residues at **N8**, **N9**.) |
| **M2** — §5 misdescribes IJC's process findings, dropping Finding 2 | **FIXED** | v2 corrects the count to three, names Finding 2, and quotes it exactly (*"has no home in the formally codified Section A"*), and states its liveness for this world. IJC §5 re-read directly: three findings, Finding 2 as described, recommendation to add as A6 or scope portfolio-level-only — v2's restatement of that recommendation is accurate. (New overstatement introduced in the same paragraph: **N4**.) |
| **M3** — B1 omits the Cyprianic antecedent corpus and imperial legal record | **FIXED** | Both bodies added. The Cyprianic bullet correctly names *Epistles*, *De Lapsis*, *De Unitate* and the 256 council as `role: antecedent` — verified in `donatism.yaml`, all four carry that role — and quotes the 256-council note verbatim. The imperial-legislation bullet is added with CTh 16 and CTh 16.5.52 (412), and the incorrect "closest analogue to World #6's imperial legal material" claim is gone (grep: absent). The Carthage 419 `confidence: provisional` flag is carried into B1 and matches the yaml. (Residual: **N5**.) |
| **M4** — Tyconius load-bearing but unvendored, census-note conflict unsurfaced | **FIXED** | Verified independently: no Tyconius entry exists in `donatism.yaml`, and no Tyconius text exists in `cic/texts/` (directory listing checked; the only repo hits are inside other volumes' text and the census note itself). v2 states this plainly, marks the mitigation prospective, adds the *Liber Regularum* to the acquisition note, and surfaces the census conflict — its rendering of the README/registry note (*"survive at all… 'known only through Augustine's quotations'"*) matches both files' actual wording. |
| **M5** — "fullest surviving Donatist voice" asserted of two texts | **FIXED** | Petilian now carries the corpus map's own qualifier in both places ("in the vendored corpus"; "in the vendored corpus specifically") — matches `donatism.yaml`'s *"the most extensive surviving Donatist voice in the vendored corpus."* The *Gesta* claim is now narrowed to a different, compatible predicate (bishops speaking at length on their own side of an exchange), and the Tyconius claim is a survival claim, not a superlative. No two-text conflict remains. |
| **M6** — "persecuted into near-extinction" historically wrong | **FIXED** | Replaced with legal proscription and progressive suppression after 411–412, survival through the Vandal period (429–439, persecution directed at Catholics), the Byzantine reconquest, and Gregory the Great's Register in Numidia in the 590s. All four are accurate on the standard account (Frend, *The Donatist Church*, closing chapters). "the side that eventually suppressed it" no longer appears in B1 (grep). |
| **M7** — end date is a phase-scope artifact, undisclosed | **FIXED** | New §1 disclosure paragraph, plus §4 item 6 as a binding obligation on Doc_01/Doc_08. The phase scope is correctly stated (70–451 CE, Chalcedon — verified in the Step 0 Conclusion). The A1 language is re-scoped throughout to "within this phase's window" rather than "for the entire life of the movement." Article 22's requirement is paraphrased, not quoted, and the paraphrase is faithful to the Article's actual text. |
| **M8** — A5 assigns the Caecilianists to World #8's territory | **FIXED** | The territorial assignment is withdrawn and named as the error. A5's actual sentence is quoted exactly, and the requirement kept is the A5-grounded one (reconstruct from inside this world's own Doc_02). v2 additionally shows why the old claim cut against the Step 0 Conclusion's own #8 boundary text — which is the reasoning Round 1 asked for. |
| **M9** — B2 asserts an eight-lens pass while addressing two; omits the material record | **PARTIAL — the fix introduced a worse problem** | The material/epigraphic/hagiographic half is genuinely fixed: basilica archaeology, *Deo laudes*, *Passio Marculi*, *Passio Isaac et Maximiani*, *Liber genealogus* are added to B1 and B2, correctly flagged as not yet inventoried. **The eight-lens half is not fixed and is now a fabrication** — see **N1**. |
| **M10** — Tyconius's standing stated as fact in the sentence calling it contested | **FIXED** | Both occurrences corrected. B1 now states the c. 380 condemnation by Parmenian and a Donatist council, the non-conversion, and leaves formal standing open; §2 A5's "which stayed formally Donatist" is gone, replaced by "Tyconius's own contested position." "Donatist exegete" is softened to "Donatist-affiliated exegete." Historically accurate on the standard account. |

### LOW

| ID | Status | Evidence from independent re-check |
|---|---|---|
| **L1** — A1 restates four of five commitments while A4 says "five" | **FIXED** | §2 A1 now cites Article 4 by reference and quotes the Methodology's own non-restatement instruction with correctly marked ellipsis (*"The floor is stated in Article 4 of the Constitution… and is not restated here"* — exact against source). Article 4's section title is verified as "On the Scope of 'Movement'" and it does carry exactly five commitments, so v2's "complete five-commitment text" pointer is accurate and A4's "five" is now consistent. |
| **L2** — Optatus appendix list is the corpus map's, uncited | **FIXED** | Now reads "list per `cic/corpus-map/donatism.yaml`". Order and content re-checked against the yaml `locus` field: identical. |
| **L3** — Optatus dossier over-credited as independent | **FIXED** | Corpus map framing adopted verbatim (`role: context`, *"officials and emperors describing and adjudicating the parties, not either side's own voice"* — exact), plus the explicit statement that it does not recover the Donatist voice and so does not mitigate the Author Gravity problem. |
| **L4** — Circumcellions: §4 stronger than §2; sourcing claim overstated | **FIXED** | §4 item 2 is aligned to §2's weaker framing (characterization shaped by polemic, existence independently attested). CTh 16.5.52 (412) and *agonistici* are both added in both places, and both are historically correct (16.5.52 names *circumcelliones* in its penalty schedule; Augustine reports *agonistici* as the group's own name). "almost entirely" is softened to "substantially." |
| **L5** — Carthage 419 described as legislating what it compiles | **FIXED** | Reworded to "the canons… collected in the 419 African register," with the c. 397–407 origin noted. The Cirta hedge is added: "305 — a date genuinely disputed in the scholarship, with 307 and later argued by some." |
| **L6** — "object of juridical action, not a wielder of it" is one-sided | **PARTIAL** | The offending sentence is deleted (grep: "wielder" absent). But the counter-cases Round 1 named were not carried anywhere — "361" appears nowhere in v2, and Anulinus's *relatio* survives only as an item in B1's appendix list, with no mention that it forwards the Donatists' own petition to Constantine. Meanwhile v2 now adopts Coach3's *"#4 is the church that permanently splits from the mainstream specifically in refusal of that same power"* as the load-bearing basis for the entire World #6 boundary resolution, unqualified. Net effect: the imbalance is no longer stated in this document's own voice, but it is now inherited without examination at a *more* load-bearing point than before. |
| **L7** — version/status citations regress from the IJC precedent | **FIXED** | Header now reads "Constitution V2.3 (file `CiC_L1_Constitution_V2_2.docx`)" and "Construction Framework V7.4 DRAFT's Step 0 stub". Both verified: the Constitution's internal version block reads "Version 2.3"; V7.4's status block still opens "DRAFT — pending Opus deep review and project-lead review; not yet ratified." |
| **L8** — citation-hygiene items (7 sub-items) | **PARTIAL** | *Fixed:* "System Hub's prior finding" removed (grep: absent); "Every major scholarly treatment" removed and replaced with a consensus claim anchored to Frend; the "no complicating theological current" overstatement corrected with a substantive, accurate rebaptism paragraph in A2; the martyr-cult obligation now explicitly labelled "an extension rather than the disclosure itself"; §4 item 7 relabelled "Acquisition note, not a disclosure obligation." *G1 is now defined — but the definition is fabricated* (**N3**). *Not fixed:* the *"not the schism-crisis angle, which belongs to world #4"* quotation is still applied beyond its scope. In the source it is a parenthesis attached specifically to Cyprian's Decian-persecution material; §3 B3 appends it after both the Cyprian and Augustine clauses, and §2 A5 goes further, presenting it as qualifying the world-level summary phrase "ordinary lay formation, preaching, and sacramental life" — two quotations from different parts of the entry joined so the second reads as governing the first. Slightly worse than in v1. |

**Tally:** 18 FIXED, 4 PARTIAL (H4, M9, L6, L8), 0 NOT FIXED.

---

## Part 2 — New findings introduced by the revision

Graded on the same scale Round 1 used.

### HIGH

#### N1. §3 B2's "all eight lenses" pass is asserted against a lens set that is not this project's — five of the Template's actual eight are missing, and the substitute list is an uncredited external taxonomy

**Draft text (§3 B2):** *"**Corrected in v2 (Round 1 M9):** the Round 1 draft addressed two lenses and asserted a pass; all eight are named here."* … *"**Passes B2 across all eight lenses**"*, and §3's Tier conclusion: *"clears Ecology across all eight lenses."*

The eight lenses v2 names are: Worship/liturgical; Narrative/mythic (memory); Doctrinal/philosophical; Ethical/legal; Social/institutional; Material; Ritual/practical; and a bullet on Formation Ecology.

**Why it's wrong.** The Methodology's B2 cites *"the Formation Ecology and Integrated Ecology Analysis dimensions (eight co-equal analytical lenses)."* Extracted directly from `CiC_L3B_Formation_World_Template_V1.5.docx`, the Integrated Ecology Analysis dimension contains exactly eight lenses, in this order:

1. Emotional Ecology
2. Philosophical Ecology
3. Interpretive Ecology
4. Authority Structures
5. Boundary Structures
6. Formation Logic
7. Memory Structures
8. Representative Theological Patterns

Formation Ecology is a **separate Template dimension** (its own top-level heading, several sections earlier), not one of the eight — so v2's eighth bullet is not a lens at all, and the count only reaches eight by including it.

Of the eight actual lenses, v2 names **none** by its own name. Five have no counterpart in v2's list at all: **Emotional Ecology, Interpretive Ecology, Authority Structures, Boundary Structures, Representative Theological Patterns**. This is not a naming quibble — Authority Structures and Boundary Structures are on any reading Donatism's two strongest lenses (a full parallel episcopate; rebaptism as the mechanism of belonging and exclusion), and Emotional Ecology is where the martyr-cult material the Step 0 Conclusion singles out for this world actually lives. A B2 pass that never names them has not run the test.

The substitute list is recognisably Ninian Smart's dimensions-of-religion schema (doctrinal/philosophical, mythic/narrative, ethical/legal, ritual/practical, social/institutional, material — with the experiential/emotional dimension, the seventh, dropped), presented without attribution as though it were the project's own framework. That the project's own practice uses the Template vocabulary is independently confirmable: `Imperial-Juridical-Christianity/Doc_07_Integrated_Ecology_Analysis.md` is structured as Authority Ecology, Boundary Ecology, Formation Logic, Memory-and-Interpretive Ecology, Worship-and-Affective Ecology.

This is the same failure mode as H1 — an external or neighbouring frame promoted into a governing document's voice — and it now sits under a "Corrected in v2" label, which is the specific thing this round was asked to distrust. It changes a criterion's disposition basis, so it is substantial by the skill's own definition.

**Fix:** run B2 against the Template's actual eight lenses by name, with a one-line disposition each. The content v2 has written is largely reusable — it maps onto Memory Structures, Philosophical Ecology, Authority Structures, Boundary Structures and Formation Logic with little loss — but Emotional Ecology, Interpretive Ecology and Representative Theological Patterns need dispositions written, and the material/epigraphic strength should be carried as evidence *for* those lenses rather than as a lens of its own. Keep the Formation Ecology observation, correctly labelled as the separate dimension it is.

### MEDIUM

#### N2. §3 B3 still places material in "World #6's eventual Doc_02" — a document that already exists — and §6 claims that residue was removed

**Draft text (§3 B3):** *"…belongs to Donatism's own Doc_02 as the force pressing on it, and to **World #6's eventual Doc_02** as an instance of the juridical consolidation it documents."*
**Draft text (§6, category 2):** *"Both are removed in v2: the World #6 relationship is resolved by adopting the existing cleared finding… which **requires nothing further of World #6's build**."*

`World-Builds/Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` exists and is a disposed document in a build carried through Step 10. Re-grepped for this round: it contains **zero** occurrences of "Donatis*". So (a) "eventual" is factually false about a completed neighbour build — a Cross-document fact-consistency defect of the same class as M4; and (b) saying the material "belongs to" that document is still an assignment into another world's finished work, which is precisely what §6 asserts was removed. Round 1's category-2 objection is therefore only partly discharged, and §6's own "Corrected in v2" accounting overstates the correction.

**Fix:** either delete the clause, or state it accurately — IJC's Doc_02 is complete and does not treat Donatism; if this build believes that is a gap, it is a portfolio-level observation to be labelled as such and routed, not a tense change.

#### N3. The new definition of "G1" is invented and attributed to "the launch process"

**Draft text (§4):** *"two texts are strong candidates for the Source Acquisition Manifest at G1 **(the gate, per the launch process, at which the build presents this world's scope and source-acquisition choices for the project lead's decision)**."*

Round 1's L8 asked only that "G1" be defined. What v2 supplies is not this project's meaning of the term. Checked across the repository: the artifact is `world-build-docs/<world>/SOURCE-REQUEST-MANIFEST.md`, produced — per its own header — *"at per-world build step 2, Source ecology (spec §4.3.2)… For: Mark, in his operational source-acquisition role."* "G1" is a **gap/item identifier inside that manifest**, not a gate: `records/alx/search_record/alx.search.stromateis-iii-english.md` reads *"SOURCE-REQUEST-MANIFEST.md (gap G1): acquire a copyrighted modern translation…"*, and `records/desert/source/desert.source.apophthegmata-patrum.md` records *"Manifest request G1 is FULFILLED."* There is no gate called G1 anywhere in the repository, and the IJC launch document — the only launch document on disk for a comparable build — defines no such gate.

This is a provenance-accuracy failure of the same species as H1: an unverifiable definition asserted with a source attribution ("per the launch process") that does not support it. That it appears inside a fix labelled as correcting a citation-hygiene finding makes it worse, not lighter.

**Fix:** describe the artifact as it actually is — a Source Request Manifest produced at Step 2 for the project lead's acquisition role, with G1 as an item identifier within it — or drop the gloss and simply name the manifest.

#### N4. §5's warrant for the A6 recommendation misreports IJC's own Finding 2

**Draft text (§5):** *"**Two independent worlds' Step 0 confirmations have now needed this test** and found it un-homed in Section A; recommend System Hub either formally add it as an A6 or scope it explicitly as portfolio-level-only."*

IJC's Finding 2 says the opposite about its own world, in terms: *"This does not affect World #6 (Criterion 2 was applied only to Montanism and Novatianism, and would not exclude a multi-figure, century-spanning institutional world like this one even if applied) — flagged here purely as a standing methodology gap."* IJC did not need the test; it observed the gap while stating that the test was not live for it. Only one world's confirmation has actually had to apply it. The distinction is load-bearing, because the strength of a recommendation to codify a new Section A subtest depends on how many cases have genuinely required it — and this is the same class of error (overstating what a cited neighbour document found) that H3 was raised for.

**Fix:** "IJC flagged the gap without needing the test; this world is the first to have to apply it" — which is still a sufficient basis for the recommendation, and is what the sources support.

#### N5. The imperial legal material's vendoring status is stated three different ways, and it is never flagged for acquisition

Verified: there is no Theodosian Code text in `cic/texts/` and no CTh entry in `donatism.yaml`. Within v2:

- **§3 B1** presents CTh 16 as a present evidentiary body — *"This is a second body of imperial-institutional evidence alongside Optatus's appendix, and — unlike the appendix — it is genuinely independent"* — with no vendoring disclosure, unlike the Tyconius bullet ("not currently vendored") and the material/epigraphic bullet ("None of this is yet inventoried").
- **§3 B1's Author Gravity paragraph** brackets only the other two as prospective — *"The imperial legal material and (once acquired) Tyconius and the material/epigraphic record meaningfully mitigate this"* — which reads as placing CTh on the available side of the line.
- **§4 item 1** says the opposite: *"should be weighted accordingly **once vendored**."*
- **§4's acquisition note** flags only the *Gesta* and the *Liber Regularum*. The one body the document calls a "genuinely independent counterweight" to the world's central evidentiary problem is not on the acquisition list at all.

B1's own test is confidence-sensitive and the document is careful about this everywhere else, which is why the inconsistency stands out.

**Fix:** state CTh 16's unvendored status in B1 alongside the other two, make the Author Gravity sentence consistent with §4 item 1, and add it to the acquisition note.

### LOW

#### N6. B3's concluding sentence attributes to Coach3 a disposition Coach3 did not reach

**Draft text (§3 B3):** *"The genuine adjacency requiring active vigilance during construction is World #8 (on the shared-Cyprianic-root axis, **per Coach3's own finding, adopted here**)."*

Coach3's words are *"Real risk… **Holds anyway**"*, and its overall verdict is *"the nine-world set's pairwise distinctiveness holds up."* "Real risk" is Coach3's; "adjacency requiring active vigilance during construction" is this document's own extension. The extension is defensible on the merits — it is close to what Round 1's H3 fix asked for — but it should be marked as this build's own, not folded into "Coach3's own finding, adopted here." Note also that "genuine adjacency requiring active vigilance" is verbatim the phrase Round 1 struck from the World #6 bullet as an uncited fresh assertion; it has been moved rather than retired.

#### N7. Numbering the uncodified Criterion 2 as "A2.5" cuts against the document's own statement that it has no home in Section A

§2 A2.5 says plainly that the test *"has no home in the formally codified Section A (A1–A5) text — it exists only in the Step 0 Conclusion's own prose"* — and then gives it an A-series section number inside a Section A walkthrough, after which §2's "Section A conclusion" enumerates it in sequence with the real subtests (*"A2's continuity test… clears… the person-defined-movement test (A2.5) clears… A3 is inapplicable; A4 is not needed; A5…"*). That is the precedent-hardening IJC's own §6 warned about ("making it the field's only documented precedent… until that happens"), arriving through formatting rather than through a claim. The disclaimer paragraph mitigates it but does not undo the impression a later builder scanning the headings will take.

**Fix:** retitle it as a non-A-series heading (e.g. "Criterion 2 — the person-defined-movement test (adopted portfolio-level, not codified in Section A)") and adjust the Section A conclusion to list it separately from A1–A5.

#### N8. "logged here rather than only in §3 B3" — B3 does not log it

§2 A2.5 introduces the Novatianism redundancy flag with *"logged here rather than only in §3 B3."* B3 contains no Novatianism reference at all (its bullets cover Worlds #8, #6, #1 and #3). Round 1's M1 fix asked for it in B3. The flag is present in the document, which is what matters, but the cross-reference describes a state of affairs that does not exist.

#### N9. A2.5's closing analogy is garbled and mis-assigns Cyprian

**Draft text (§2 A2.5):** *"…this world clears the person-defined-movement test on communal-tradition grounds, in the same way **Cyprian's or Novatian's own doctrinal soundness** was never the issue for the movements that failed it."*

The movements that failed Criterion 2 are Montanism and Novatianism. Cyprian founded no such movement and is not among them; the Step 0 Conclusion's own statement of the point concerns Novatian's *De Trinitate* and Montanism's Trinitarian/Christological soundness. The sentence also draws an equivalence that does not hold (clearing on communal-tradition grounds is not "the same way" doctrinal soundness was irrelevant elsewhere). Both are drafting-level, but the Cyprian insertion is a factual mis-assignment in a section otherwise carefully sourced.

#### N10. §0's revision note mischaracterises the Round 1 findings it is responding to

**Draft text (§0):** *"Round 1 found four high-severity findings, **all sourcing/provenance defects rather than historical errors**."*

True of H1–H3. H4 is not a sourcing or provenance defect — it is an escalation-category assessment failure, and Round 1's own disposition guidance singles it out as *"not fully closable by revision."* The framing reads as narrowing the review's own result at the top of the document responding to it.

#### N11. The Record Integrity Principle is invoked for something it does not govern

**Draft text (§5):** the H1-class error is described as *"the same class of error the **Record Integrity Principle** and the Step 0 Conclusion's own Provenance-accuracy discipline exist to prevent."*

The Provenance-accuracy discipline is exactly on point. The Record Integrity Principle, read directly in Framework V7.4, is not: it governs document *currency* — *"A finding, fix, or open question is not resolved merely because a later document says it was addressed"* — with its two founding failure cases being stale Construction Notes and a fix described as applied but absent from the deployed file. Neither concerns quotation provenance. Invoking a named governing principle for a case outside its stated scope is a small instance of the same discipline the paragraph is about.

---

## Part 3 — What checked out clean on re-verification (stated because it is a result, not a courtesy)

- **Every quotation newly introduced in v2 that has a testable source is character-exact.** Re-verified individually against freshly extracted text, not against Round 1's findings: the Methodology's B5 heading and body; the Section B "never a per-world process" framing (the truncation Round 1 noted is repaired); A1's non-restatement sentence with correct ellipsis; A5's two passages; the Procedure's "as applicable" line; the Step 0 Conclusion's Primary-gravity-first sentence including the restored qualifier; the Criterion 2 statement; the Novatianism redundancy line; the World #4 entry, martyr-cult disclosure and Ebbeler correction; the World #8 boundary phrases; Coach3's #4/#8 and #4/#6 passages with correct ellipsis; IJC Doc_01 §6's "No overlap risk" sentence; IJC §5 Finding 2's "no home in the formally codified Section A"; the corpus map's `antecedent` note, "authority both sides argued FROM", `role: context` framing, and Petilian "in the vendored corpus" qualifier; the System Hub Decision Log's "recurrence of an already-once-corrected sourcing gap."
- **The v2 corrections to H1, H2 and H3 are genuine, not label-deep.** In each case I checked the corrected claim against the source rather than the correction note against the finding.
- **The corpus-map-derived content is accurate throughout**: the four Cyprianic `antecedent` entries, the 419 register's `provisional` confidence, the appendix list's content and order, Optatus's `role: context`.
- **The new historical content is accurate**: CTh 16.5.52 (412) naming the *circumcelliones*; *agonistici* as the group's own self-designation reported by Augustine; the 419 register as a compilation of c. 397–407 African canons; the Cirta 305/307 date dispute; Parmenian's council condemning Tyconius c. 380 and his non-conversion; the *Liber Regularum*'s independent survival and its relation to *De doctrina christiana* III; the Vandal, Byzantine and Gregorian survival sequence in M6 and §1.
- **§4's obligations remain fully traceable** — item 1←B1, 2←§2 A5, 3←§1/B2, 4←B3, 5←§1, 6←§1 — with no invented obligation, and the mislabelled item 7 correctly demoted to an acquisition note. Internal cross-references (§6 → §4 item 4; §3 → §4) resolve correctly after the renumbering.
- **The category-4 resolution route is legitimate.** Adopting IJC Doc_01 §6's cleared finding genuinely dissolves the contradiction rather than routing around it; Round 1 offered exactly this as one of two permitted paths, and v2 took it with both prior treatments cited. I record this explicitly because the review was asked whether this was a dodge. It is not.

---

## Disposition guidance

**SUBSTANTIAL REVISION REQUIRED.** Not because the revision failed — eighteen of twenty-two findings are genuinely fixed, and the three provenance high findings are fixed properly, with the primary sources re-checked rather than the notes re-read. The verdict turns on **N1**, which independently meets the `cic-build-cycle` definition of substantial: B2's pass — one of the two near-threshold Section B checks, and a component of the Tier 1 determination in §3's conclusion — is asserted against a lens set that is not the Template's, omitting five of the eight actual lenses including the two most favourable to this world. That is a changed claim's substance and a changed sourcing conclusion, not wording. **N2**, **N3**, **N4** and **N5** are each independently more than cosmetic, and **H4**, **M9**, **L6** and **L8** remain partly open.

Three observations for the revision, offered as pattern rather than instance:

1. **The fixes themselves are now the highest-risk surface.** Three of the five most serious new findings (N1, N3, N5) were introduced by Round 1 fixes, and one (N2) is a "Corrected in v2" note that overstates its own correction. A document under adversarial revision accumulates assertions written under pressure to close findings; those assertions need the same sourcing discipline as the original draft, and in v2 they did not get it. N1 and N3 in particular are the same failure mode as H1 — reaching for a plausible external or remembered frame and presenting it in a governing document's voice — recurring inside the fix for a different finding.
2. **H4's second limb should be closed on its merits, not by omission.** The Step 0 Conclusion's logged Article 3 question names this world by name as the rival claimant contesting the Cyprian/Augustine interval, and B3 is where it recurs. Whether or not it rises to a category-4 escalation, §6 cannot assert that nothing unresolved remains while the standing question the portfolio-level document flagged as "likely to recur" goes unmentioned in the section where it recurs.
3. **L6's counter-cases matter more now than they did in Round 1.** With the World #6 boundary resolved by adopting the alignment-versus-refusal contrast, the 313 appeal to Constantine (via Anulinus's *relatio*, which this document lists in B1) and the 361 Julian rescript restoring Donatist basilicas are the two facts most in tension with the axis the document now rests on. Naming them as bounded counter-cases strengthens the adopted finding; leaving them out leaves the document's most load-bearing boundary claim carrying an unstated qualification.

This document returns to *Revision decision* → revise → *Review* Round 3. It is not eligible for cosmetic application, and not eligible for self-disposition.
