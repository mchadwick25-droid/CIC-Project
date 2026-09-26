# Doc_02 (Source Ecology) + Source Registry + Source Acquisition Manifest — Round 2 Independent Adversarial Review

**World:** Donatism (`don`)
**Documents reviewed:** `Doc_02_Source_Ecology.md` (revised), `Source_Registry.md` (revised), and `Source_Acquisition_Manifest.md` (new this revision) — all three read in full, together.
**Reviewer:** independent adversarial review thread (Opus), 2026-09-01. No part of this review was drafted by the build thread. This reviewer did not draft, and has no memory of drafting, any of the documents under review, and did not draft Round 1.
**Method:** every Round 1 finding was re-verified against the primary or governing source directly, not against the revised documents' own account of them. Every quotation newly introduced this revision was traced to its named source and checked character-by-character. New defects were hunted independently, including in sections Round 1 never touched.
**Checked against:** `cic/texts/optatus_against-the-donatists.txt` (read at Book I chs. XI–XIX, the apparatus at notes 42/49/150, the Book VII opening, and the Appendix testimony); `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` (Prolegomena Chapter II in full, plus *On Baptism* I.1.2 and VII.5–6 and *Contra litteras Petiliani* III); `cic/texts/npnf101_augustine-confessions-letters.xml` (Letter LXXXVII in full; the div3 letter index); `cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml`; `cic/texts/npnf214_seven-ecumenical-councils.xml` (the Carthage-under-Cyprian title page); `cic/texts/README.md`; `cic/corpus-map/donatism.yaml` (all twelve entries, line by line); `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md` V1.0; `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part II and Step 2 (extracted from `word/document.xml`); `CiC_L1_Constitution_V2_2.docx` Articles 20, 23, 26 (extracted); `Build/reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` (extracted); `Doc_01_World_Identification_Boundaries_Orientation.md` and `Step0_Movement_Scope_Confirmation.md` (both Approved to proceed); `don_Decision_Log.md`; `Review-Artifacts/Doc02_Round1_Review.md` and `Doc01_Round2_Review.md`; the `cic-build-cycle` skill text; `Build/worlds/ijc/Doc_02_Source_Ecology.md` and its `Source_Registry.md`; `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md` and its five siblings; `records/ijc/search_record/` and `records/desert/search_record/`; `Build/worlds/_cross-world/README.md` and `WANTS-REGISTER.md`; and the git history of this world's build folder.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 high, 16 medium, 15 low.**

The revision is a genuine and substantial improvement. Round 1's header reports "5 high, 15 medium, 13 low," but its body actually carries M1 through M16, so the real total is thirty-four findings, not thirty-three. Of those thirty-four I confirm **twenty-six fully fixed, seven partially fixed, and one not fixed at all** — and the four highest-value fixes (the Homoian import deleted, the Lucilla material recovered and quoted accurately, the manifest actually written, the corpus-map role contradiction disclosed and logged) are real, checkable, and mostly well done. The Lucilla quotations are character-exact against the vendored Optatus. The two NPNF104 Prolegomena quotations are character-exact against the vendored file. Nothing in the "checks out clean" section of Round 1 was disturbed, and one item on it — Registry row 6's Ep. 87 licensing constraint — I independently re-verified against Letter LXXXVII itself and found correct in every particular, including the negative claim about §8.

The verdict is nonetheless SUBSTANTIAL because two findings change a sourcing conclusion or a factual claim, and because the failure pattern this build's Decision Log already names as recurring has recurred, in three distinguishable forms:

1. **Reviewer fix-text adopted into the document's own voice without independent verification.** Round 1 supplied replacement wording for H1 ("carries Book VII") and a replacement date for M12 ("c. 398–400"). Both were adopted verbatim. Neither is supported by the vendored file that settles it. This is the exact failure mode `don_Decision_Log.md` records under "Standing process notes for this world," and Doc_01's own Round 2 found three instances of it.
2. **A fix reaching for the nearest available source rather than the best one.** Doc_01 §4's binding is now discharged — but through a nineteenth-century editorial summary (Type S) of two unvendored works, when Augustine's own *On Baptism*, vendored and already Registry row 3, makes the same point directly and more fully, including the half of the claim the summary does not support.
3. **A new artifact built without checking whether the project already has that artifact.** The Source Acquisition Manifest was written from scratch. The project already carries `SOURCE-REQUEST-MANIFEST.md` in six worlds, with a settled schema, a settled location, and a settled rights posture — and the new Manifest offers the project lead an acquisition path that the vendored corpus's own README rules out in one sentence.

Round 1 predicted Round 2 would be "materially shorter." It is not, but the reason is instructive: most of what follows is in material Round 1 never reached — the new §5 categories, the new Manifest, the new Registry rows, and the revision's own procedural claims about itself.

---

## What checks out clean

Stated at length, because a great deal of this is right and a further revision must not disturb it.

**Round 1's clean list survives intact.** I re-checked each of the four items Round 1 named as not-to-be-touched:

- **The 256-council double entry.** Row 10 (`anf05`, `role: antecedent`, confidence `assigned`, Registry Confidence B) and row 11 (`npnf214`, `role: tradition`, confidence `provisional`, Registry Confidence C, "not to be cited at row 10's confidence"), with the §9 item 6 forward watch, are all present and unchanged. Row 11 has additionally *gained* the L8 fix and gained it correctly (below). Untouched otherwise.
- **The Augustine letters split.** All eleven numerals, the 168-letter volume, the div3 derivation, the eight-or-more cut, Letter LXXVI by its title's address, and the 2026-08-26 attribution are all still exact against `donatism.yaml`. Unchanged.
- **Registry row 6's Ep. 87 licensing constraint.** I did not take this from Round 1. I read Letter LXXXVII in `npnf101` in full. §6 is precisely the conciliar-authority reproach and it names the Maximianists explicitly ("the council of the followers of Maximianus who were cut off from you… was of no authority against you, because their number was small compared with yours; and yet claim for your council an authority against the nations"). §7 and §8 concern the civil powers, Romans 13, and the emperors, and neither mentions the Maximianists. The row's positive license and its negative constraint are both exactly right. **This is the single best piece of discipline in either document and must survive any further revision untouched.**
- **The four five-dimension Author Gravity entries.** Optatus, Augustine, Petilian, Cyprian, each with all five dimensions, all still present. Petilian's Transmission History paragraph is unchanged and is still the sharpest paragraph in the document.

**The corpus map is still represented accurately.** All twelve entries still have a corresponding row; every `role:` and `confidence:` string quoted in a Verification Note still matches `donatism.yaml` character-for-character. Row 1's `role: context`, rows 3/4/5's `role: tradition`, row 6's newly-added `role: context`, rows 7–10's `role: antecedent`, row 11's `tradition`/`provisional`, row 13's `provisional` — all verified against the file this session.

**H5 (Lucilla) is fixed, and the quotations are exact.** I grepped `optatus_against-the-donatists.txt` myself: thirteen occurrences. The chapter heading is "XVI. The quarrel of Lucilla against Caecilian" and Book I runs from line 25 to line 761, so **§6's "I.16" citation is correct**. "the Schism, after the consecration of Caecilian, was effected at Carthage through a certain mischief-making woman named Lucilla" is verbatim. "Majorinus, a member of the household of Lucilla — at her instigation, and through her bribes — was consecrated Bishop by Betrayers" is verbatim (em-dashes normalised from the file's `----`). Nothing is paraphrased-as-quoted. The characterisation "a wealthy Carthaginian laywoman" is supported by the text and its Appendix, not asserted: I.18 has "that influential, mischief-making woman… together with all her retainers"; the *Gesta apud Zenophilum* material in the Appendix has "the four hundred pieces of money, that were given by the noble woman Lucilla" and the Zenophilus interrogatories about that money. The reading that Optatus needs her real standing in order to blame her is fair against I.16–I.19 and against the translator's own note at line 617, which reads the schism through "the anger of… a shameless woman" as one of three causes. **This bullet is a better discharge of Article 20 than the blank it replaced, and its core should not be softened.**

**H4's two quotations are real and correctly located.** "The Synod had granted a season of delay during which all who returned should be held innocent. Of this very many availed themselves; the baptism of these was valid; those who remained outside lost both baptism and the church" is verbatim in `npnf104` at the Prolegomena Chapter II summary of *Contra Cresconium* Book III (the sentence spans the volume's page break at p. 387). "Why rebaptize us… when you do not repeat the rite upon your once expelled but now restored Maximianists?" is verbatim in the same chapter's account of the *Psalmus contra Partem Donati*, and Doc_02's attribution of it to the *Psalmus* is correct. The heading "Chapter II.—An Analysis of Augustin's Writings Against the Donatists" is exact. "(four books, c. 406, 'some say as late as 409')" is exact — the file reads "wrote (406 A.D., some say as late as 409) *Contra Cresconium Grammaticum Partis Donati, libri IV*." "*Contra epistulam Parmeniani* (three books, c. 400)" is exact — "Augustin replies (c. 400 A.D.) in three books: *Contra Epistolam Parmeniani*." **No fabricated quotation was found in Doc_02.** (One is in the Registry — see M9.)

**H1's factual error is gone and its replacement is half-right.** There is no eighth book. The revised text correctly grounds the second edition in the added name of Pope Siricius, which is exactly what the vendored apparatus supports at note 42.1 ("In the first edition of St. Optatus written about 370 a.d. the list of Popes ended with Damasus. The name of Siricius who became Pope in 383 was added in the second edition") and note 49.1 (the Lucian/Claudian additions to the anti-pope list). The false motive-claim about a Parmenian reply is gone. See M5 for the one clause that outran the evidence.

**H2 is fully fixed.** The Homoian/"Arianism" bullet is gone from §8. A word-boundary search for `Arian` and `Homoian` across Doc_02 and the Registry returns only §6's IJC comparison, which is accurate, attributed, and about IJC rather than about Donatism. §8's Dominant Modern Reconstruction now carries only the Circumcellion reading, which is correctly placed, and doctrinal orthodoxy stays where Round 1 said it belonged, under Documented / Widely Accepted at Step0 §2 A1. Exactly the right fix.

**H3 is fixed in the sense that matters most: the manifest exists.** Five Registry rows no longer point at a file nobody can open. Its cross-references to the Registry are internally consistent — item 1 → row 14, item 2 → row 15, item 3 → row 16, item 4 → rows 19/20, item 5 → rows 35/36, all correct — and Doc_02 §9 item 1's list of its four subjects matches. That consistency check passes cleanly.

**The Manifest's network disclosure is accurate, and I independently corroborated it three ways.** It says archive.org, Gallica and general web domains returned `EGRESS_BLOCKED`. (a) My own session returns `curl: (56) CONNECT tunnel failed, response 403` for `archive.org/metadata/...`. (b) `cic/texts/README.md` states as a standing fact that "the sandbox this project's agents run in blocks every patristic text host (ccel.org, newadvent.org, wikisource, archive.org, gutenberg, tertullian.org)." (c) `records/desert/search_record/desert.search.apophthegmata-pd-english.md` records the same block, dated and verified, in an unrelated build. The disclosure is neither overstated nor understated, and the instruction to open each link before treating rights status as final is the right posture. **Credit where due: this is honest, and it is the kind of limitation that is usually papered over.**

**Article 26 and Article 23 are now quoted correctly.** §2's attribution of the five dimensions to the Framework, with Article 26 as the delegating authority, matches Article 26 Section A verbatim ("The dimensions of source assessment, including transmission history, and the construction stages at which the discipline is enforced are governed by the Construction Framework"). §6's Article 23 restatement now correctly makes it govern *the Representative's speech* — "The Representative speaks about the world's opponents as the world understood them — honestly, without rehabilitating them into modern equals and without modern editorializing" — and the ellipsis is honest. M14's scope-shift is fixed, and the IJC inversion (an absent opponent there, an over-present one here) is now named in one clean sentence. **This is one of the best-executed fixes in the revision.**

**L8 is fixed and the fix is correct.** I verified the `npnf214` title page directly: "The Council of Carthage held under Cyprian." followed by "a.d. 257." Row 11 records the discrepancy, keeps the corpus map's September-256 dating, and explains why. Exactly right.

**M10 and M11 are fully and substantively fixed.** §4 now performs all five Framework evaluations — authorship and date, proximity, genre conventions, formation ecology revealed, Author Gravity risk — for each of the three Passiones, individually, and the *Acta Saturnini* entry correctly doubles its Author Gravity risk for the contested chain of custody. §5 now carries all four Framework categories, and the "Martyrology assessment category" gloss in §4 is verbatim faithful to Part II ("what the community believed a faithfully formed life looks like under ultimate pressure").

**M16 is fixed well.** The forces-lens paragraph in §6 answers all three of Step 2's questions — which sources speak to external forces, what silences reveal, what survivorship patterns indicate — and answers the third with a genuinely good observation ("the forces that ended this world's own institutional continuity are also, structurally, the forces that determined what evidence about this world would survive at all"). It gathers rather than pads.

**M15 is fixed, and fixed better than Round 1 asked.** Doc_02 §1 states the corpus map's internal inconsistency plainly, in the document's own analytical voice, without editorialising; row 6 now carries `role: context` and the observed discrepancy; §9 item 7 and §10 both route it for census-level correction. The refusal to "correct" a generated file outside the build thread's authority is right.

**M4, M6, M7, M8, M9(b)(c)(d), M12(part), M13(part), L1, L3, L4, L5, L6, L7, L11, L13 are fixed.** Row 12 has its "in the vendored corpus" qualifier back. Row 21 no longer fills the Licensed-For field with its own negation. Rows 19–21 moved off D. Row 29 has a Confidence value and a real Verification Note, and its comparandum reasoning now carries the two things that actually make the case — the shared `anf05` volume and the corpus map's own *De Unitate* note. §3's Shaw pointer goes to §6. §6 bullet 1 cites B2/B5. §1 no longer labels a paraphrase "verbatim." §7 says "a further century and a half." §4 restores Doc_01's hedge and the Parmenian/council distinction. Row 1 names its edition. Rows 14/15/16 say their Author Gravity assessment is deferred rather than leaving the omission silent. All confirmed against the current text.

**M1 is fixed at all five sites.** Every "Doc_01 §2, A5" is now `Step0_Movement_Scope_Confirmation.md` §2, A5 — Doc_02 §3, §6 (twice), Registry rows 16 and 24. Row 5's remaining "confirmed against Doc_01 §2" is legitimate: Doc_01 §2 does carry Letter 185, c. 417, tribune Boniface.

**M2 is fixed at both sites.** §7 now says Doc_01 §7 item 8 "binds Doc_08's own ending-forces cell… It does not bind this document," and §10 repeats the correction rather than the error.

**M3 is fixed and the target verifies.** Row 13 now cites `Step0_Movement_Scope_Confirmation.md` §3, B1, which does contain "mostly compiling African conciliar canons originating c. 397–407 rather than legislating them fresh."

**M5 is fixed.** Rows 32 (Gregory's Register), 33 (*De doctrina christiana* III) and 34 (Ebbeler) exist, with narrow licences. Row 33's vendoring claim verifies: `npnf102` contains all four books of *On Christian Doctrine* and 27 occurrences of "Tichonius" — the NPNF spelling — so Book III's Tyconian material is genuinely there.

**The Registry's checkpoint-compliance statement was added, and it is very nearly true.** Of every source Doc_02 names in support of a specific claim, I found exactly one without a row (M16 below). That is a real improvement on Round 1's three.

**The Step 0 Conclusion quotations in row 29 are verbatim.** "one man's rigorist stance and irregular consecration as a rival bishop, rather than a broader community's own interpretive tradition" and "Real redundancy risk against Donatism" are both exact. (Their *locations* are not — see M10.)

---

## HIGH

### H1. The Source Acquisition Manifest offers the project lead an acquisition path the vendored corpus's own README rules out in one sentence — and does so as the *only* path for this world's most load-bearing unvendored source.

`cic/texts/README.md`, lines 16–21, is unambiguous:

> "**PUBLIC DOMAIN ONLY.** Every file here must be out of copyright, and its own provenance header must say so… **In-copyright editions (Holmes 2007, Ward 1975) are referenced by `source` record and never vendored — committing them would be redistribution.**"

The Manifest's own framing is "the project lead's decision on **which editions enter `cic/texts/`**," and each item ends with a **Destination** filename. Against that rule:

- **Item 1 (*Gesta Collationis Carthaginiensis*).** Rights status stated as "Not public domain" (Sources Chrétiennes / Cerf; CCSL / Brepols). A Destination filename is nonetheless given (`gesta-collationis-carthaginiensis_actes-conference-carthage_lancel1972.pdf`, or four per-volume variants). The "Where" is an archive.org item the Manifest itself says is probably controlled-lending. And the item explicitly says "No public-domain full edition (Latin or English) was identified this session." So the single acquisition route offered for the *Gesta* — the source Doc_02 §1 calls load-bearing and Registry row 14 licenses for "Donatist bishops' own recorded words at length" — is a route the corpus rules bar outright.
- **Item 2 option B** (Babcock, SBL 1989), **item 3 option B** (Pharr, Princeton 1952 / Lawbook Exchange reprints), and **item 4's alternative** (Tilley, Liverpool 1996) are all in-copyright and all presented as things to "acquire… on which option (A/B where offered)."

The decision block then reads: "For each of items 1–4: acquire, decline, or defer, and on which option (A/B where offered)." For item 1 there is no A/B — there is one option, and it is barred.

This is not a technicality about a rule the project keeps loosely. The project has a settled, written *category* for exactly this case, and uses it: `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md` §3 records "**Theodosian Code in English** — Pharr (1952) treated as in copyright, fails closed," and §4 records "Consultation-only secondary scholarship (never vendored)… All in copyright; named in record trailing bodies as references, never quoted as licensed material, **per the corpus README's own rule**." The fleet-level `Build/worlds/_cross-world/WANTS-REGISTER.md` states the same posture in its own words: in-copyright works are "in copyright, so they can never be vendored (redistribution), but they can be bought and consulted."

The Donatism Manifest never names that category once, in any of its five items, and the word "consult" appears nowhere in it.

Why this is high and not medium: this is the one artifact in Step 2 whose entire purpose is to produce a decision by a person. It puts an unavailable option in front of that person, as the recommended and in one case sole path, for the source the rest of the document set says it most needs — and it does so against a rule that is written down, one directory away from the destination it names. A project lead acting on item 1 as written would either place an in-copyright PDF in a public-domain-only library, or discover after the fact that the decision he was asked for was never available. The rights disclosure in the "Rights status" line does not cure this, because the Manifest never draws the conclusion the disclosure requires.

**Fix.** Restructure the Manifest on the project's own existing three-way split, which already exists and already works: (1) acquirable, public domain — Burkitt 1894, Mommsen/Meyer 1905, Migne PL 8, and (add) Ziwsa's CSEL 26 Optatus and Monceaux; (2) confirmed unavailable in the public domain, recorded not requested — Lancel, Babcock, Pharr, Tilley, Maier, with each one's fallback path named (for the *Gesta*, that fallback is: no vendored text, Emeritus's recorded words unavailable for quotation, and Doc_02 §1's claim about them stands at referenced-only until that changes); (3) consultation-only secondary scholarship, never vendored — which is also where Registry rows 23–26 (Frend, Shaw, Tilley, Brown) belong and are currently not placed. Do not offer a Destination filename for anything in category (2) or (3).

---

### H2. Doc_02 §1's Maximianist reconstruction inverts the polarity of the passage it quotes, drops the refutation clause that immediately follows it, and rests the whole discharge on a Type-S nineteenth-century summary while the vendored primary that states the point better — including the half the summary does not support — sits unused at Registry row 3.

Doc_02 §1 reads:

> "That summary reports the decisive fact Doc_01 §4 identifies: when the mainstream (Primianist) Donatist party suppressed the Maximianist schism with state assistance (the Bagai sentences, 394–398) and its bishops and clergy sought return, '[the Synod had granted a season of delay… lost both baptism and the church]' — **a decision Augustine's Donatist interlocutor Cresconius does not deny but engages with directly**, professing (per the same summary) to 'have made special inquiry into the whole history.' **Returning Maximianist clergy and their baptisms were received without reordination or rebaptism.** … the underlying practice is reported as a fact about the Donatist party's own conduct, **contested by a Donatist interlocutor on its interpretation rather than on its occurrence.**"

**(a) The polarity is inverted.** In the source, the quoted sentences are not the summary's own report of a decision that Cresconius then declines to deny. They *are* Cresconius's report. The full passage in `npnf104`, Prolegomena Chapter II, summary of *Contra Cresconium* Book III:

> "Cresconius says he will neither absolve nor condemn Optatus, and **as to the Maximianists, he professes to have made special inquiry into the whole history. The Synod had granted a season of delay during which all who returned should be held innocent. Of this very many availed themselves; the baptism of these was valid; those who remained outside lost both baptism and the church. Augustin refutes the statement** from its inherent contradictions and from the language of the Synod against the Maximianists."

The Donatist asserts; the Catholic refutes. Doc_02 has it the other way round: it makes the account neutral, has the Donatist merely not-denying it, and then says it is "contested by a Donatist interlocutor." No Donatist contests it in this passage. Augustine does.

**(b) The refutation clause is dropped.** "Augustin refutes the statement from its inherent contradictions and from the language of the Synod against the Maximianists" is the next eight words after the closing quotation mark, and it is not in Doc_02 at any confidence. That clause materially changes the evidentiary character of what is quoted: the summary does not present the season-of-delay decision as an agreed fact about Donatist conduct. It presents it as a contested Donatist apologetic account that Augustine rejected as self-contradictory. A downstream builder who follows the citation will find the source saying something Doc_02 says it does not.

**(c) The "without reordination" half is not in the cited source at all.** Nothing in the Prolegomena's *Contra Cresconium* summary mentions reordination. That half of the sentence is carried across from Doc_01 §4, uncited, and lands in the same breath as a quotation that does not support it.

**(d) And the vendored primary that does support all of it is Registry row 3.** `npnf104` contains Augustine's *On Baptism, Against the Donatists* — vendored, Native, Type P, Registry row 3, Doc_02's own §1 headline source. Book I, ch. 1 §2 makes the exact argument, with the reordination point stated outright:

> "For as those who return to the Church, if they had been baptized before their secession, are not rebaptized, so those who return, having been ordained before their secession, are certainly not ordained again; but either they again exercise their former ministry… **they are not ranked with the laity. For Felicianus, when he separated himself from them with Maximianus, was not held by the Donatists themselves to have lost either the sacrament of baptism or the sacrament of conferring baptism. For now he is a recognized member of their own body, in company with those very men whom he baptized while he was separated from them in the schism of Maximianus.**"

And Book VII: "the Donatists… have consented to acknowledge the baptism which was conferred among the followers of Maximianus, whom they had condemned… whom they received with Felicianus and Prætextatus." The same volume also carries the point in *Contra litteras Petiliani* (Registry row 4) — "If they say that Felicianus of Musti, and Prætextatus of Assavæ, whom they afterwards received, were not of the party of Maximianus…" — and in the Prolegomena's own summary of Letter 70: "**If he was welcomed without rebaptism, why not treat the Church diffused through the whole world with the same consideration?**"

So the position is this. Doc_02 §1 says "neither survives in a vendored full text" of *Contra Cresconium* and *Contra epistulam Parmeniani* — true — and then treats that as meaning the reconstruction must run through a nineteenth-century editorial précis, rowed at Type S. It does not. The *works* are unvendored; the *evidence* is vendored, in primary form, in two sources this Registry already rows as Native P, in the very file the summary sits in. The discharge of Doc_01 §4's binding is therefore made at a materially weaker evidentiary grade than the corpus actually permits, on a passage the document misreads, while asserting a clause that passage does not carry.

Why this is high: it changes a sourcing conclusion (which source discharges a binding obligation, and at what weight), it misstates a factual claim about the source (who asserts, who refutes), and it does both in the single most consequential new paragraph in the revision. Row 31's own honest caveat — "not a substitute for acquiring the primary texts themselves" — is correct as far as it goes and does not reach this, because the substitute that was needed was not the unvendored primary but the vendored one.

**Fix.** Rebuild the paragraph on *On Baptism* I.1.2 and VII.5–6 (row 3) and *Contra litteras Petiliani* (row 4) as the primary evidence, quoting Augustine directly; keep row 31 for what it is uniquely good for — the dating of *Contra Cresconium* and *Contra epistulam Parmeniani*, and the *Psalmus* parallel. State plainly that the season-of-delay account is Cresconius's own explanation and that Augustine rejects it, which is a *sharper* Author Gravity point than the one currently made: the reception itself is common ground between the two parties, and only its justification is in dispute. That is the version the sources actually support, and it survives the objection that the whole thing is a debating point scored by a hostile source — which the current version asserts and does not earn.

---

## MEDIUM

### M1. The Registry states that the priority-review trigger "has been re-run **mechanically** against the Discovery column… rather than by narrative judgment." It has not been. Eleven builder-prior-knowledge rows are unflagged, two of them contradicting their own Verification Notes.

I tabulated all 36 rows against the Discovery column. Twenty carry `builder-prior-knowledge`. Nine are flagged (19, 20, 21, 22, 25, 26, 27, 28, 29). **Eleven are not: 14, 15, 16, 17, 18, 23, 24, 32, 33, 35, 36.**

Some of those are defensible on the trigger's third conjunct (not currently licensing a load-bearing vivid claim): rows 14–16, 35, 36 are unvendored acquisition targets. Others are not:

- **Row 23 (Frend)** is builder-prior-knowledge, not re-read this session, and licenses §5's rural/urban and cultural-environment claims and §3's terminal-record licence. That is load-bearing and specific by any reading. Unflagged.
- **Row 24 (Shaw)** is builder-prior-knowledge, not re-read, and licenses §6's reading of the Circumcellion category — a specific interpretive claim the Confidence Map elevates to Dominant Modern Reconstruction. Unflagged. Meanwhile **row 26 (Brown) *is* flagged**, though its licence is expressly "general historical framing only — not licensed for vivid, specific claims." The trigger is firing on the row that cannot trip it and not firing on the two that can.
- **Row 32 (Gregory's Register)** carries, in its own Verification Note, the words "**flagged for priority review** before it supports any claim beyond the terminus-of-attestation point." It is not in the flag list.
- **Row 33 (*De doctrina christiana* III)** likewise says "**flagged for verification** before supporting any claim more specific than the influence relationship itself." It is not in the flag list.

A Registry whose flag list contradicts two of its own rows has not been re-run mechanically against anything. The claim that it was is the defect: Round 1's M13 asked for the columns *and* a mechanical re-run, and the revision delivered the columns and an assertion about the re-run.

**Fix.** Either actually run it and let the list grow, or delete the word "mechanically" and say that the trigger was applied by judgment against the stated conjuncts, naming which rows were considered and released and why. Add rows 23, 24, 32 and 33 at minimum.

### M2. Rows 30 and 31 are set at Confidence B while their own Verification Notes describe Confidence A. They are the only two rows in this Registry that meet the Template's definition of A, and neither is set there.

The Template: "**A** — Verified this session against an accessible primary source, translation, or authoritative reference. **B** — Specific work/locus named, not independently re-checked this session."

Row 30: "**Directly verified this session** against `cic/texts/optatus_against-the-donatists.txt` (13 occurrences, including the chapter heading… and the account of Majorinus's consecration…)" — Confidence B.
Row 31: "**Directly read this session** in the vendored file… quoted directly from this text" — Confidence B.

Both are textbook A. Not one of the thirty-six rows sits at A. The sibling world's Registry has a whole disclosed note on getting this calibration right in the other direction ("A is reserved for cases where an accessible primary source, translation, or authoritative reference was actually consulted and checked this session; everything resting on trained historical knowledge alone, however confident, is B or lower"). Donatism has over-corrected past it, with the result that the Confidence letter no longer distinguishes the two rows where real verification happened from the twenty where it did not. Round 1's M7 was the same axis-reliability complaint pointing the other way; the revision fixed one end and broke the other.

**Fix.** Move rows 30 and 31 to A. If the build thread's reasoning is that A requires re-collating a whole work rather than a specific locus, say so once in a note rather than encoding it silently in every row — but that reading is not the Template's.

### M3. §6's Gender bullet attributes a 1917 translator's footnote to Optatus himself, and re-renders its content from "amongst the Donatists" to "among the Maximianists."

Doc_02 §6: "**Optatus's own apparatus** also records a second lead: Augustine's Letter 162 reports 'that a woman like Lucilla was subsequently the cause of a schism within a schism' — **a later split among the Maximianists themselves** — naming a second, currently unidentified female actor…"

Two problems.

**(a) It is not Optatus's apparatus.** Optatus has no apparatus. The note is O.R. Vassall-Phillips's, from the 1917 Longmans edition — a nineteenth-/twentieth-century editorial remark, roughly fifteen centuries after the text it annotates. Registry row 30 gets this right ("reported only in **Optatus's own translator's apparatus**"). Doc_02 does not, and Doc_02 is the document a reader meets first. In a document whose central discipline is Author Gravity, attributing a modern editor's aside to the ancient author is precisely the wrong direction of error, and it silently upgrades the lead's evidentiary weight from "a modern editor's cross-reference" to "the world's earliest narrative source."

**(b) The content is changed.** The note reads: "St. Augustine tells us (Ep. clxii) that a woman like Lucilla was subsequently the cause of a schism within a schism — of a later schism **amongst the Donatists themselves**." "A schism within a schism amongst the Donatists" is, on the obvious reading, the Maximianist schism. Doc_02 relocates it *inside* the Maximianist party — a third-order split the note does not describe — and Registry row 30 repeats the relocation ("a schism within the Maximianist schism"), and §9 item 5 carries it forward as an open item for Doc_09. One reviewer-era misreading is now in three places and pointed at a future document.

**(c) A checkable fact that would have caught it was not checked.** Letter CLXII is **not in the vendored `npnf101` volume** — its div3 index runs …CLIX, CLXIII…, so the NPNF selection omits it. Row 30 honestly says the lead "has not been independently checked against Letter 162 itself," which is right, but does not say that it *cannot* be, from the current corpus. That is a one-command finding and it sharpens the note considerably.

**Fix.** In §6, say "the vendored edition's own translator's apparatus records…"; render the note's content as it stands ("a later schism among the Donatists themselves — on the obvious reading, the Maximianist schism"); and add to row 30 that Letter 162 is absent from the vendored NPNF101 selection, so the lead cannot be closed without acquisition.

### M4. §6 claims to have exercised Article 20's secondary (reconstruction) duty for Lucilla, but the Confidence Map carries no tier marking for that material — which Article 20 requires for all reconstruction produced under the permission, and which the IJC precedent supplies for its own equivalent case.

Constitution Article 20: "**All reconstruction produced under this permission carries the confidence calibration and tier marking Article 17 requires. It is presented at inferential confidence and never as equivalent to documented material.**"

Doc_02 §6 and §9 item 5 both state that the secondary duty is "exercised once this pass, for Lucilla." Doc_02 §8's Confidence Map does not mention Lucilla in any of its four bands. The Inferential/Thin band lists three items and none of them is this. The Registry's row 30 Confidence B is a citation-reliability tier, not an Article 17 confidence level, and the two are explicitly different axes.

The sibling world got this right on the parallel case. `Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` §8 lists, under Inferential/Thin: "any claim about **Justina's own theological commitments beyond what hostile sources report of her actions**." That is exactly the marking Donatism's Lucilla material needs and does not have.

There is a second, cleaner reading available and the document should choose between them: what §6 actually does for Lucilla is report what a hostile source attests and name what it cannot support — which is the **primary** duty (naming structural absence and its shape), performed very well, not the secondary one. Nothing in the bullet reconstructs Lucilla's own perspective, voice, or formation. If that is the honest description, §6 and §9 item 5 are overclaiming, and the correct fix is to say the secondary duty was *considered* against condition (c) and found not to be needed, because the trace supports naming rather than reconstruction.

**Fix.** Pick one. Either (a) add an Inferential/Thin line to §8 on the Lucilla material's limits, modelled on IJC's Justina line, and keep the "exercised once" claim; or (b) reclassify the bullet as a primary-duty discharge and correct §6 and §9 item 5. Do not leave a claimed Article 20 reconstruction with no Article 17 marking anywhere in the document.

### M5. "carries Book VII" — Round 1's own suggested fix wording, adopted verbatim, and not supported by the vendored file.

Doc_02 §2, Optatus, Limitations: "the work's second edition (after 383, on the evidence of the added name of Pope Siricius) updates the papal and Donatist episcopal lists and **carries Book VII**, showing Optatus's own argument extended after the fact rather than fixed at the first edition."

In context this asserts that Book VII is part of what the second edition added. The vendored file does not support it. What it supports is: the papal list was extended from Damasus to Siricius (note 42.1), and the anti-pope list gained Lucian and Claudian (note 49.1). Both notes then point outward — "(cf. Preface to Book VII)", "(See Preface, p. xxii.)" — to the translator's Preface, **which is not in the vendored file**: `optatus_against-the-donatists.txt` begins directly at "BOOK THE FIRST" and contains no front matter. The one other Book VII remark in the file (note 309.4) is about a transposition of two chapters to Book III, not about the second edition. The file's own provenance header, meanwhile, dates the Latin original "c. 366-393 CE," which is a third dating alongside the corpus map's "c. 366–367, rev. c. 385" and the apparatus's "about 370."

Round 1's proposed replacement sentence read, word for word: "…updates the papal and Donatist episcopal lists and carries Book VII, showing Optatus's own argument extended after the fact rather than fixed at the first edition." It was adopted without the check Round 1 itself demanded three paragraphs later ("H1, H5, and M12 all require checking a claim against a file, not re-reasoning it"). The check was run for H5 and not for H1.

**Fix.** Drop "and carries Book VII," or, if the build thread wants the claim, source it to the translator's Preface and say the Preface is not in the vendored file. Note the three-way dating divergence in row 1's Verification Note rather than leaving it silent.

### M6. "specifically dated to c. 398–400" — Round 1's own suggested date, adopted verbatim, unsupported by the vendored source, contradicted by the same sentence, and carried by no Registry row.

Doc_02 §2, Petilian, Representativeness: "at a moment **specifically dated to c. 398–400** — contemporaneous with Augustine's *Answer* (Book I c. 400, Book III c. 401–402)…"

The half that verifies: `npnf104`'s Prolegomena states "He replied with one book to so much as he had received, c. 400 A.D.… he composed the second book, c. 401 A.D.… **Meanwhile Petilian responded to the first issue**, and this necessitated a third book, c. 401 or 402 A.D." Doc_02's parenthetical dating of Augustine's books is exact.

The half that does not: the source dates *Augustine's* books, not Petilian's letters, anywhere. And it records that Petilian wrote again *after* Augustine's Book I — that is, after c. 400 — which the "c. 398–400" bracket excludes, in a sentence that cites the very evidence excluding it. The word "specifically" makes an inference into an attested date.

No Registry row carries this dating. Row 4's Verification Note does not mention it; row 12's does not; row 31 is licensed narrowly for "Maximianist rebaptism-theology reconstruction," not for Petilian chronology. So the sharpest date in the Author Gravity section rests on nothing rowed.

Round 1's M12 fix text read: "so Petilian's letters date to c. 398–400." It was adopted with "specifically" added.

**Fix.** "his surviving letters belong to the years around 400 — the first before Augustine's *Answer* Book I (c. 400), a second answering it, prompting Book III (c. 401–402)," sourced to row 31 and with row 4's Verification Note extended to carry the chronology. The substantive point — that the grievance is contemporary pressure, not personal memory of 347–348 — is right and should stay; it does not need a false precision to stand.

### M7. §5's two new categories rest on the most contested element of Frend's thesis without naming the contest, while the Registry's own rows 24 and 26 hold the standard rebuttal, and §8 marks none of it Contested.

The two bullets added this revision:

> "**Social-historical background:** Donatism's own regional and social distribution — heavily rural and Numidian relative to the more urban, Proconsular-Africa-centered Caecilianist strength, **a pattern named substantially in Frend (row 23)**…"
> "**Surrounding cultural and religious environment:** the Punic- and Libyan-speaking substrate of rural Numidia, and the region's own pre-Christian religious practice, are named in the field literature (**again substantially in Frend**) as part of the standard context both for the Circumcellion question (§6 below) and for Donatism's own rural strength more generally."

The bare distributional claim is uncontroversial. The frame these two bullets place it in — a Punic/Libyan substrate as the standing explanation of Donatism's rural strength and of the Circumcellions — is Frend's 1952 social-and-native-protest thesis, and it is the most contested single argument in the modern literature on this movement. This Registry rows two of its principal critics:

- **Row 24, Shaw, *Sacred Violence* (2011)** — the book Doc_02 §3 licenses precisely because it treats the Circumcellion category as substantially a hostile construction. That argument is, among other things, a sustained refusal of Frend's sociological reading of the same group.
- **Row 26, Brown, *Religion and Society in the Age of Saint Augustine* (1972)** — a collection that includes Brown's direct critiques of the native-resistance reading of African religious dissent. *(Stated at Confidence B on my own field knowledge; I did not re-read the volume this session, and I hold myself to the same standard I am applying.)*

So §5 imports, as neutral background context, a reading that §6 spends its longest bullet dismantling on the authority of a source this same Registry rows — and §8's Confidence Map places none of it under Contested. §5's own hedging ("a context this document names rather than exploits," Confidence C, not independently verified) mitigates but does not cure: the problem is not the confidence level, it is that a live scholarly dispute is presented as settled background, in the two sections added specifically to bring evidence from *outside* the Optatus/Augustine concentration.

**Fix.** Name the dispute in one sentence in each bullet — that Frend's social-and-substrate reading is the classic account and that Shaw (row 24) and Brown (row 26) are the standard correctives — and add a Contested line to §8 for the substrate reading. Both bullets get *better*, not weaker: a named live dispute is more useful to Doc_04 and Doc_05 than an unmarked consensus that is not one.

### M8. §10 labels the corpus-map inconsistency a "Category 4 item" and in the same sentence declines to escalate it. The governing skill does not permit that combination — and on my own assessment it is not a Category 4 item.

Doc_02 §10: "…it is **logged as a Category 4 item** for census-level/System Hub correction, **not escalated to the project lead** as a decision only he can make…"

`cic-build-cycle`, Escalation categories: "Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back.**" And: "A document only becomes eligible for disposition when it has cleared an independent review without that review calling for substantial revision, **and none of the four escalation categories applies.**"

So the label and the disposition are mutually exclusive as written. If §10's characterisation is right, this document cannot be self-disposed at all; if the disposition is right, the label is wrong.

On the substance, I think the label is wrong, and I reach that independently rather than by accepting either the document's or Round 1's framing. Category 4 is "**Unresolved tensions the pipeline can't close on its own** — two reviews disagreeing with each other, a contradiction between two already-cleared master documents, or a finding that cuts against an earlier decision." The corpus-map item is none of these: it is an infelicitous *rationale* inside a generated census file, whose actual role assignments are correct and were ruled on 2026-08-26; it contradicts no cleared master document; it cuts against no decision; and the pipeline *can* close it — the same skill assigns editing authority over non-world-build files to a coach thread, and Step0 §5 ("Process findings for System Hub") plus Step0 §3 B1's handling of the `texts_registry.py` claim are this world's own worked precedent for that route. Doc_02 §9 item 7 already routes it correctly. It is §10's label that is the error.

Round 1 recommended the Category 4 label. This is a review-to-review disagreement; on the skill's own text I supersede it, and record the disagreement here rather than quietly reversing it, following the precedent `don_Decision_Log.md` records for Doc_01 Round 2.

**Fix.** Delete "Category 4" from §10 and describe the item as it is: a process finding surfaced for census-level correction through the System Hub channel, alongside §9 item 8, with no escalation category triggered. See the escalation section below for the two genuine escalation-adjacent items §10 does not currently name.

### M9. Registry row 31 presents "held valid" as a direct quotation from `npnf104` and it is not there.

Row 31: "…including the specific finding used in Doc_02 §1 (the Synod's grant of a '**season of delay during which all who returned should be held innocent**,' with the baptism of returning Maximianists '**held valid**,' **quoted directly from this text**)."

The source reads "**the baptism of these was valid**." The phrase "held valid" occurs twice in `npnf104` — once in *On Baptism* IV ch. 53 on baptism from an unbaptised minister, once in a Petilian-facing passage — and in neither case about the Maximianists. The first quotation in the row is exact; the second is a conflation of "held innocent" and "was valid," presented inside a clause that asserts direct quotation.

The substance is correct and the correct wording is shorter. But this is the first fabricated quotation found anywhere in this document pair across two rounds, and it sits in a Verification Note — the field whose entire job is to say what was checked. This project runs a standing fabrication check; a quotation-hygiene failure inside the checking apparatus is worth grading as more than cosmetic.

**Fix.** "with the baptism of returning Maximianists reported as valid ('the baptism of these was valid')."

### M10. Row 29's fix text introduces two new mis-attributions where Round 1 found one.

Round 1's M9(b) found "World #9 entry area" wrong. That is fixed. Two new ones took its place.

**(a) The two Step 0 Conclusion quotations are in different sections, and the row assigns both to one.** Row 29's Comparandum Note reads: "The Step 0 Conclusion (**Possible Future Worlds, 'From this review cycle' subheading**) names an explicit 'real redundancy risk against Donatism'… excluding Novatianism from the portfolio on person-defined-movement grounds ('one man's rigorist stance and irregular consecration as a rival bishop, rather than a broader community's own interpretive tradition')…" I extracted the document. "Real redundancy risk against Donatism" is indeed under Possible future worlds → From this review cycle. "one man's rigorist stance…" is not: it is roughly forty paragraphs earlier, under "**Excluded on the person-defined-movement ground (the new second criterion)**." Both quotations are verbatim; one is in the wrong place.

**(b) *De Trinitate*'s doctrinal assessment is attributed to the corpus map, which has no Novatian entry.** Row 29's closing clause: "…excluded here for the shape of the temptation it creates via shared transmission, not for its own doctrinal content, **which the corpus map already treats as unproblematic pre-Nicene orthodoxy.**" `cic/corpus-map/donatism.yaml` contains twelve entries and none of them is Novatian; the file never mentions him. The judgment is the Step 0 Conclusion's — "Novatian's own *De Trinitate* is a solid, broadly orthodox pre-Nicene treatise" — and the row cites the Step 0 Conclusion two sentences earlier for something else.

Right substance, wrong document, twice — the exact error class Round 1 named as the one that "survives a fix pass, because the fixer recognizes the substance as correct and moves on."

**Fix.** Split the section citation; point the orthodoxy judgment at the Step 0 Conclusion.

### M11. Doc_01 §7 item 6's binding on *Contra Cresconium* and *Contra epistulam Parmeniani* is not discharged, and the stated reason is inconsistent with how the Manifest treats the Passiones.

Doc_01 §7 item 6 (binding): "Augustine's *Contra Cresconium* and *Contra epistulam Parmeniani* are likewise unvendored and are this document's own load-bearing sources for the Maximianist episode… **Doc_02 should add them to the same acquisition tracking.**"

Registry rows 17 and 18: "Acquisition of the full text remains an open item, **not currently in `Source_Acquisition_Manifest.md` for lack of a verified public-domain or open-access English edition this pass.**" The Manifest itself does not mention either work anywhere — not as an item, not as a deferred item, not in the decision block.

Three problems. First, the binding said "add them to the same acquisition tracking," not "add them if an English edition exists," and it is not discharged. Second, the stated reason is inconsistent with the Manifest's own practice one item away: Manifest item 4 handles the *Passio Marculi* and *Passio Isaac et Maximiani* precisely by offering a public-domain **Latin-only** edition (Migne PL 8) with the English translation recorded as the copyrighted alternative. Applied consistently, that treatment would put Migne PL 43 and/or the CSEL Petschenig volumes for both Augustine works in front of the project lead as a public-domain Latin option. Third, Doc_02 §9 item 1 says only that the two works "remain unvendored in full" and does not disclose that they were left out of the Manifest, so the omission is discoverable only from two Registry rows.

**Fix.** Add both to the Manifest on item 4's own Latin-only pattern, or state in §9 item 1, in the document's own voice, that Doc_01 §7 item 6 is discharged only in part and why.

### M12. The Registry and the Manifest state contradictory verification statuses for the same Gallica finding — and describe it as two different kinds of object.

Registry rows 19 and 20, Verification Note: "**Confirmed extant** in Patrologia Latina vol. 8 and in a **Gallica (BnF) manuscript listing** (Latin)"; Discovery column: "cross-checked via WebSearch this pass (Patrologia Latina vol. 8; **Gallica BnF manuscript listing**)."

Manifest item 4: "A **Gallica (Bibliothèque nationale de France) digitization of the same Migne volume** was also identified in earlier research this pass but **its exact ark identifier was not re-confirmed** in this session's searches and **should be treated as unverified until re-found**."

Two co-equal Step 2 outputs, produced in the same pass, one calling a finding confirmed and the other calling it unverified. They also disagree about what it is: a *manuscript listing* (a catalogue entry for a medieval codex) and a *digitization of the Migne volume* (a scan of an 1844 printed book) are different objects with different evidentiary value, and only the second would bear on acquisition.

**Fix.** Decide which it is, state it once, and make the Registry follow the Manifest's honesty rather than the other way round.

### M13. The clean-documents discipline is breached in all three files.

`don_Decision_Log.md` states the requirement in the project's own words: "This log holds the review-round history, revision rationale, and escalation checks for each document in this world's build, **so the construction documents themselves stay clean, substantive content — no inline revision annotations, no 'corrected in vN' markers, no review-round commentary woven into the analysis.**"

Five instances:

1. **Doc_02 §10:** "The relative-recall and PRESS exercises conducted at this document's own **Round 1 review** are a start on that sweep…"
2. **Doc_02 §10:** "…and the **rows added this revision** (Gregory's Register, *De doctrina christiana* III, Ebbeler, the NPNF104 Prolegomena summary, Lucilla, Tilley's…) close part of the gap **the recall test found**…"
3. **Doc_02 §9 item 2:** "…the social-historical and cultural-environment categories **added this pass**…"
4. **Source_Registry.md, saturation statement:** "…the ten-item relative-recall and PRESS exercises **run at this document's own Round 1 review**… **This Registry closes this revision pass**…"
5. **Source_Acquisition_Manifest.md:** the §5 heading — "Supporting works named at **Doc_02's Round 1 review**" — and its closing sentence, "the relative-recall gap **Doc_02's own Round 1 review** found."

This is a standing project requirement, restated in this world's own Decision Log, and it was the subject of its own commit (`cb178333`, "move revision/review history out of build documents into Decision Log") immediately before the revision commit that reintroduced it.

There is a real substantive point buried in instances 1 and 4 — that the recall and PRESS exercises are a partial start on the V7.4 sweep — and it can be made without naming a review round: "A ten-item relative-recall check and the PRESS instrument have been run against this Registry; both are a start on the field-bibliography sweep V7.4 requires, not a substitute for it."

**Fix.** Rewrite all five in the documents' own voice; move the round-attribution to `don_Decision_Log.md`, where the Doc_02 entry is still marked "to be completed when review concludes."

### M14. The Registry dropped the Template-schema **Added** field when it added the Discovery column, degrading the append-only audit trail at exactly the moment seven rows were appended.

The Template's entry schema lists ten fields, the last being "**Added** | Date and who/what added it." The original Registry (commit `58ee86a5`) had it, populated as "2026-09-01, `don` build thread." The revision replaced it with "Discovery (channel / instrument / date)" rather than adding alongside it. `Imperial-Juridical-Christianity/Source_Registry.md` retains **Added**.

The cost is concrete. This Registry is an append-only living document; seven rows (30–36) were appended this revision; and there is now nothing in the table that distinguishes them from the twenty-nine drafted in the original pass, because every Discovery date is the same day. Row 32's Discovery value even carries a fragment of revision history ("carried from Doc_02 §3/§7 citation gap") in a field that is not for that.

**Fix.** Restore **Added** as its own column and keep Discovery. Populate **Added** for rows 30–36 distinctly from rows 1–29 so the append is visible.

### M15. No `search_record` exists, and the project has a live per-world mechanism for one that this world is not using — while the Discovery column is presented as though drawn from a record that was never kept.

V7.4 Step 2: "**Keep a search_record as the discovery work proceeds:** every discovery channel used… with instrument and date per search, **logged as searches happen — never reconstructed afterward.** Every source row carries its own `discovery_channel`, `discovery_instrument`, and `discovery_date` **from this record**."

The project implements this. `records/<world>/search_record/` exists for seven worlds — `pahc`, `hal`, `ijc`, `desert`, `syr`, `alx`, `fix` — as per-search YAML-fronted markdown files with `query`, `channel`, `result`, `found_sources`, `note`, and a confidence block carrying `citation_specificity` / `verification_state` / `evidentiary_weight`, which are the three axes the Source Registry Template's re-keyed priority trigger is defined on. It includes negative sweeps (`ijc.search.c-p-negative-sweep.md`, `f1-t-negative-sweep`, and five more), which are precisely what V7.4's saturation statement requires. **There is no `records/don/`.**

So Round 1's M13 is fixed in form and not in substance: the three per-row fields exist, but the record they are specified to come "from this record" does not, the values are demonstrably reconstructed at revision time, and the Registry does not disclose either fact. A reader takes "builder-prior-knowledge, cross-checked via WebSearch this pass / WebSearch / 2026-09-01" as a log entry; it is a recollection.

**Fix.** Either open `records/don/search_record/` on the existing schema and back-fill honestly with a note that entries were reconstructed on 2026-09-01, or state in the Registry that no search_record was kept this pass and that the Discovery column is a post-hoc reconstruction. The second is a one-sentence fix and is preferable to leaving the impression of the first.

### M16. Checkpoint: the *Psalmus contra Partem Donati* is named in support of a specific claim in §1 and has no Registry row.

Doc_02 §1: "a use already visible in his earlier rhetorical question, **from the same Prolegomena's account of his *Psalmus contra Partem Donati***: 'Why rebaptize us…'"

A specific named work of Augustine's, doing evidentiary work — it establishes that Augustine deployed the Maximianist argument well before *Contra Cresconium*, which is the "already visible" claim's whole content. No row. The Registry rows *De doctrina christiana* III (row 33) for a weaker relationship — a single influence claim about Tyconius — so consistency demands this one too. The Template's checkpoint is stated as the one hard rule: "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row."

The Registry's own new compliance statement — "Every source named in `Doc_02_Source_Ecology.md` in support of a specific claim has a corresponding row below" — is therefore not quite true, by one row. Round 1 correctly advised adding it "only once it is true."

**Fix.** Add a row for the *Psalmus contra Partem Donati* (P, C, Native, licensed narrowly for the pre-406 Maximianist-argument datum, Verification Note recording that only the Prolegomena's summary of it is vendored, not the poem).

---

## LOW

**L1. Round 1's L2 is not fixed.** Doc_02 §5 still reads "(**Doc_01 §3, B2 discussion** — this document does not repeat that reasoning, only its evidentiary basis)" and Registry row 28 still reads "(Doc_01 §3 B2 discussion)". I re-read Doc_01 §3: it is "Distinct World Criteria," four bulleted questions, **no B-numbered items anywhere**. The content is `Step0_Movement_Scope_Confirmation.md` §3 B2, whose closing sentence is the exact warrant being reached for: "the material/epigraphic evidence logged as support for Authority Structures, Boundary Structures, and Memory Structures specifically rather than a lens of its own." This is the one member of Round 1's "right substance, wrong section" cluster that survived the sweep — and Round 1 named it as the error type most likely to survive one.

**L2. §7's new cross-reference is wrong.** "the same distinction is restated here because **§1 and §5 above rely on it**." Neither does: §1 stops at 439 and §5 never touches the terminal period. **§3** relies on it — it licenses Frend for "the terminal-record material (Gregory the Great's Register, §7 below)." This clause is new with the M2 fix; the original §7 had no such sentence.

**L3. Row 13 is now the only corpus-map-derived row that omits its `role:` value.** The M15 fix added `role: context` to row 6, correctly. Rows 1, 2, 3, 4, 5, 7, 8, 9, 10, 11 all state theirs. Row 13 (Code of Canons 419) states only `confidence: provisional`; the corpus map gives it `role: context`. A one-word completion of a sweep that stopped one row short.

**L4. Row 1 asserts a translator attribution the vendored file itself flags as unconfirmed.** The row names "English translation by O.R. Vassall-Phillips (Longmans, Green & Co., 1917)". The file's provenance header reads: "London: Longmans, Green & Co., 1917 (O.R. Vassall-Phillips, trans./ed.) — **translator attributed on external bibliographic grounds; not confirmed from this file's own text, which does not name a translator**." The attribution is almost certainly right; the Registry should carry the file's own caveat, particularly since §2 and §6 now both lean on that translator's apparatus.

**L5. Manifest bibliographic slips.** Item 3's scope note calls Mommsen/Meyer 1905 "the full **six-volume** Mommsen edition." *Theodosiani libri XVI cum Constitutionibus Sirmondianis et Leges novellae ad Theodosianum pertinentes* (Berlin: Weidmann, 1905) is two volumes, the first in two parts — three physical books at most. The same item calls it a single edition two paragraphs earlier. Item 4 dates Migne's *Patrologia Latina* "compiled 1841–1855"; the Latin series ran from 1844. *(Both stated at Confidence B on my own field knowledge, not re-checked against a catalogue this session.)*

**L6. The Manifest omits the two mechanical steps the corpus README requires on vendoring.** "Once a decision is made, the chosen files are placed by the project lead at the destinations named above" — but `cic/texts/README.md` requires that each file's "own provenance header must say so" on rights, and that `python cic/engine/texts_registry.py --write-readme` be run "after vendoring a new file or adding an ENTRIES row in that module." For a document whose stated purpose is to make an acquisition actionable, leaving both out is a real gap.

**L7. "G1" is used three times across Doc_02 and the Manifest with no definition and no cross-reference.** I verified it is a real project convention rather than an invention: `records/desert/search_record/desert.search.apophthegmata-pd-english.md` records "the acquisition is an OPEN request to Mark — **manifest G1, priority P1**," and a sibling record uses the same label. But nothing in the Donatism build defines or points at it, and `Step0_Round1_Review.md` already flagged an undefined "G1" in this same world. Give it a one-clause gloss and a pointer.

**L8. The saturation statement no longer names any unproductive search, and the previous draft at least conceded that none had been run.** V7.4: "Close the Registry with a saturation statement naming **the last unproductive searches — which queries, against which instruments, returned nothing new.** A Registry without a saturation statement is not complete." Round 1's L10 flagged the broken sentence "The last unproductive search this pass: none run yet: this is a first-pass Registry…" — the fix deleted the sentence rather than repairing it, and with it the only acknowledgement of that specific requirement. The current statement says the *sweep* was not run, which is a different (also required) thing.

**L9. The Registry still has no Status line.** Round 1's L10 second half. `Imperial-Juridical-Christianity/Source_Registry.md` opens with one ("**Status:** Cleared review (Round 2, CLEARED)…"). A Registry that is a co-equal Step 2 output and is disposed of jointly with Doc_02 should say so on its own face.

**L10. An unflagged homonym that will bite Doc_03 and Doc_09.** "Maximian" the deposed deacon and rival primate of Carthage (Doc_02 §1, Registry rows 17–18) and "Maximian" of the *Passio Isaac et Maximiani* (Doc_02 §4, Registry row 20) are different people, both prominent in this document, and nothing anywhere distinguishes them. The Registry's Comparandum-Note apparatus exists for exactly this kind of easy-to-conflate hazard.

**L11. Rows 35 and 36 use the hybrid Type "P/S," which the sibling world's Registry explicitly corrected away from.** IJC's own closing notes: "Rows 18–21 use Type **P** (Primary), not a hybrid 'P/S' code as this build's first-drafted pass used — the Template defines S strictly as modern scholarship." The Template does say "may combine," so this is defensible and I record it as an inconsistency with sibling practice rather than an error — but a translated primary corpus with a scholarly introduction is precisely the case IJC ruled on, and one of the two worlds should follow the other.

**L12. Row 35 quotes a chapter title while stating that contents were not checked, and the two documents capitalise it differently.** Row 35: "contains '**The martyrdom of Marculus**'" / "contents not independently checked against the volume itself this session." Manifest item 4: "including '**The Martyrdom of Marculus**'." Either is a plausible rendering; presenting one in quotation marks in a row that disclaims having opened the book is the issue.

**L13. Row 30 should record that Letter 162 is not in the vendored corpus.** `npnf101`'s div3 letter index runs …CLIX, CLXIII…; the NPNF selection omits CLXII. That is a one-command check that turns "not independently checked" into "not checkable from the current corpus," which is the more useful statement for acquisition planning.

**L14. §4's *Passio Marculi* dating rests on unattributed "the scholarship."** "composed close to the martyrdom it narrates… **on the scholarship's own dating**." Frend (row 23) is the natural anchor and is licensed for exactly this; naming him costs nothing and puts the claim inside the Registry.

**L15. Manifest item 3 does not cite the project's own existing determination on Pharr.** "no free English alternative was identified this session" — `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md` §3 already records "Theodosian Code in English — Pharr (1952) treated as in copyright, fails closed." Reaching the same conclusion independently is fine; not knowing the project had already reached it is the pattern H1 describes.

---

## Round 1 disposition table

| Round 1 | Status | Note |
|---|---|---|
| H1 (eighth book) | **Partial** | Error removed; replacement clause "carries Book VII" unsupported — M5 |
| H2 (Homoian import) | **Fixed** | Bullet deleted; no residue anywhere |
| H3 (missing manifest) | **Partial** | Manifest exists and cross-references cleanly; rights posture defective — H1 |
| H4 (Maximianist binding) | **Partial** | Discharged, but on the wrong source and with the passage misread — H2 |
| H5 (Lucilla) | **Fixed** | Quotations exact, I.16 correct, no overstatement of the core; two errors in the second lead — M3 |
| M1 (Doc_01 §2 A5 ×5) | **Fixed** | All five |
| M2 (Doc_01 §7 item 8) | **Fixed** | §7 and §10 both |
| M3 (row 13 citation) | **Fixed** | Step0 §3 B1 verified |
| M4 (row 12 qualifier) | **Fixed** | |
| M5 (three missing rows) | **Fixed** | Rows 32, 33, 34 added; one new gap — M16 |
| M6 (row 21 licence) | **Fixed** | Now "Not yet licensed"; provenance cited |
| M7 (rows 19–21 at D) | **Fixed** | Moved to B; new error at the other end — M2 |
| M8 (row 29 confidence/note) | **Fixed** | Confidence B, real Verification Note |
| M9 (row 29 reasoning) | **Partial** | (b)(c)(d) fixed well; (a) still unsourced but now flagged; two new mis-citations — M10 |
| M10 (§4 per-source evaluation) | **Fixed** | All five items, all three texts |
| M11 (§5 four categories) | **Fixed** | Both added; new substantive problem — M7 |
| M12 (Petilian dating) | **Partial** | Made precise and thereby wrong at the edge — M6 |
| M13 (discovery fields) | **Partial** | Columns added; no search_record, re-run not mechanical — M1, M15 |
| M14 (Article 23 scope) | **Fixed** | Verbatim correct; inversion named |
| M15 (corpus-map role) | **Fixed** | Disclosed in §1, row 6, §9 item 7, §10 |
| M16 (forces lens) | **Fixed** | Substantive, gathers rather than pads |
| L1 (Shaw pointer) | **Fixed** | |
| L2 (Doc_01 §3 B2) | **NOT FIXED** | Both sites — L1 |
| L3 (Step0 B2/B5) | **Fixed** | |
| L4 ("verbatim" label) | **Fixed** | |
| L5 ("two centuries") | **Fixed** | |
| L6 (Article 26) | **Fixed** | Verbatim verified |
| L7 (Tyconius hedge) | **Fixed** | Hedge and distinction both restored |
| L8 (a.d. 257) | **Fixed** | Verified against `npnf214` |
| L9 (IJC reuse) | **Fixed** | §9 item and §6 paragraph both rewritten with world-specific content; §1 points at Step0 |
| L10 (broken sentence / status) | **Partial** | Sentence gone, checkpoint statement added; no Status line — L9; requirement lost — L8 |
| L11 (edition on row 1) | **Fixed** | With one caveat — L4 |
| L12 (row 6 pointer) | **Fixed** | Reworded so Doc_01 §4 attaches to "the Maximianist affair," which it does discuss |
| L13 (Author Gravity deferral) | **Fixed** | Rows 14, 15, 16 |

**26 fully fixed, 7 partial, 1 not fixed at all (L2, at both of its sites).** Within the seven partials, the specific residues are: H1 → M5; H3 → H1(new); H4 → H2(new); M9(a) still unsourced though now flagged; M12 → M6; M13's substance (no search_record, trigger not actually re-run) → M1 and M15; L10's Status line → L9 and its saturation-search requirement → L8.

*(Round 1's own header reports 15 mediums; its body carries M1–M16. This table follows the body.)*

---

## Mandated reviewer coverage checks (Framework V7.4, Step 2, "Doc_02 review requirement")

Run fresh this round, against a partly different instrument set from Round 1's, since re-running Round 1's exact list against a revision tuned to it would not be a test.

### Ten-item relative-recall test

Ten works a specialist would expect in a Donatism bibliography, drawn from the standard critical-edition series (CSEL, CCSL, SC, TU), the Liverpool *Translated Texts for Historians* series, and the standard monograph and *histoire littéraire* literature — instruments independent of this build.

| # | Work | In Registry? |
|---|---|---|
| 1 | Ziwsa (ed.), *S. Optati Milevitani libri VII* (CSEL 26, Vienna 1893) — the critical Latin text underlying row 1's translation | **No** |
| 2 | Edwards (trans.), *Optatus: Against the Donatists* (TTH 27, Liverpool 1997) | **No** |
| 3 | Tilley (trans.), *Donatist Martyr Stories* (TTH 24, Liverpool 1996) | **Yes** — row 35 |
| 4 | Maier, *Le Dossier du Donatisme*, 2 vols. (TU 134/135, 1987/1989) | **Yes** — row 36 |
| 5 | Lancel (ed.), *Actes de la Conférence de Carthage en 411* (SC 194/195/224/373; CCSL 149A) | **Yes** — named on row 14 |
| 6 | Petschenig (ed.), Augustine's anti-Donatist works, CSEL 51–53 — the critical text of *Contra Cresconium* and *Contra epistulam Parmeniani* | **No** |
| 7 | Frend, *The Donatist Church* (Oxford 1952) | **Yes** — row 23 |
| 8 | Shaw, *Sacred Violence* (Cambridge 2011) | **Yes** — row 24 |
| 9 | Tilley, *The Bible in Christian North Africa* (Fortress 1997) | **Yes** — row 25 |
| 10 | Monceaux, *Histoire littéraire de l'Afrique chrétienne*, vols. IV–VI (Paris 1912–1922) — the standard older literary history, which prints the Donatist documentary and hagiographic corpus | **No** |

**Relative recall = 5/10**, up from Round 1's 4/10 on a different list.

The pattern has shifted but not resolved. The Registry now holds the interpretive monographs *and* two of the three documentary/translation instruments Round 1 named. What it still holds none of is **a critical edition of any of its own primary texts**. Row 1 names a 1917 English translation and no Latin text; rows 3–6 name NPNF volumes and no CSEL; rows 17–18 name works and no editions at all; rows 15, 16, 19 and 20 name works whose editions the Manifest identifies but the Registry does not carry. That is the specific gap items 1, 2 and 6 measure, and it has a practical consequence already visible in this review: §2's Optatus Limitations claim (M5) turns on what the second edition changed, which is a question the critical edition's apparatus settles and the 1917 translator's footnote only gestures at.

Item 10 is worth singling out. Monceaux vols. IV–VI are pre-1929 and public domain, and they print both Macarian-repression *Passiones* with commentary. That is a free answer to Manifest item 4's stated problem ("the only edition of either text identified this session in any form, free or commercial") and a second witness against the un-critically-edited Migne text the Manifest currently offers alone.

### PRESS question, asked verbatim

> "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."

**Answer — three, all dispositioned "should be rowed":**

1. **Paul Monceaux, *Histoire littéraire de l'Afrique chrétienne*, vols. IV–VI (Paris: Leroux, 1912–1922).** The standard older literary history of Donatism; prints the Donatist documentary and hagiographic corpus with commentary. Pre-1929, public domain. **Disposition: row it (P/S, B, Native) and add it to the Manifest as a public-domain acquisition candidate — it is the single most efficient free answer to both the Passio problem (Manifest item 4) and the edition-level gap the recall test measures.**
2. **Karl Ziwsa (ed.), *S. Optati Milevitani libri VII* (CSEL 26, Vienna: Tempsky, 1893).** The critical Latin edition of this world's earliest narrative source. Public domain. **Disposition: attach to row 1 as its named critical edition alongside the 1917 translation, and use its apparatus to settle the second-edition question at M5 rather than the translator's footnote.**
3. **Michael Petschenig (ed.), *Sancti Aureli Augustini Scripta contra Donatistas*, CSEL 51–53 (Vienna, 1908–1910).** The critical text of *Contra Cresconium* and *Contra epistulam Parmeniani* — Registry rows 17 and 18, which currently name no edition at all. Public domain. **Disposition: attach to rows 17 and 18 and add to the Manifest, which discharges Doc_01 §7 item 6 (M11) on the Latin-only basis the Manifest already uses for item 4.**

I can name more than three; the instrument caps the answer at three. Round 1's own PRESS answer was dispositioned two-of-three (Tilley and Maier rowed, Lancel attached); its recall-table misses at items 8, 9 and 10 (Edwards, Babcock, Tengström) were not dispositioned at all, and V7.4 requires that "every named work is dispositioned — rowed, or excluded with a reason." Babcock is now named in the Manifest but not rowed; Edwards and Tengström appear nowhere.

---

## Escalation-category assessment (run independently, not accepted from §10)

Against `cic-build-cycle`'s four standing categories, on the current content of all three documents.

- **Representative identity, name, or title decisions** — not touched by any of the three. §10 is correct.

- **Portfolio-level or cross-world strategic decisions** — §10 says neither document decides one, and confines its assessment to Doc_02 and the Registry. **That assessment is incomplete, because it omits the third document.** The Source Acquisition Manifest asks the project lead to decide whether to spend money on, or seek institutional access to, four in-copyright scholarly editions (Lancel, Babcock, Pharr, Tilley), and — as H1 sets out — asks it in terms that would place at least one of them inside a library the project's own README restricts to public-domain material. Acquisition posture and rights policy are decided for reasons external to this world's ecology; that is the category's own definition. This is not a reason to *withhold* the Manifest — putting acquisition decisions to the project lead is exactly right, and G1 is the correct route. It is a reason for §10 to say so, and to say it after H1 is fixed, so that what reaches the project lead is a choice among options that are actually available.

- **Governance or methodology decisions** — §10 says the document creates none. On the Article 20/23 routing and the corpus-map ruling, that is correct: both apply existing authority rather than making it. But **§9 item 8 is not accounted for anywhere in §10.** It states that the Step 2 forces-lens requirement is a "structural gap in how the Step 2 template is currently applied" and names `Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` — a document already **cleared at Round 2 and disposed of** — as sharing the gap. That is a finding about the build process, asserted against an already-cleared document in another world. It does not decide governance and I do not think it triggers Category 3 on its own; it is a System Hub process finding of the same kind as the two already standing in `don_Decision_Log.md`. But §10's escalation paragraph should name it and route it, rather than leaving it to sit unremarked in §9.

- **Unresolved tensions the pipeline can't close on its own** — §10 names one item here and mislabels it (M8). Running the category myself:
  - **The corpus-map `context`/`tradition` inconsistency is not a Category 4 item.** Reasoning at M8. It is a process finding for the census owner, routed correctly by §9 item 7 through the channel Step0 §3 B1 and §5 already established. §10 should drop the label.
  - **There is one genuine Category 4 item, and it is this round's own.** Two of this revision's fixes (M5, M6) were adopted verbatim from Round 1's suggested wording, and Round 2 finds both unsupported against the vendored files; and Round 2 supersedes Round 1 on the Category 4 label itself (M8). That is "two reviews disagreeing with each other" in the category's own words. This world already has the precedent for handling it without escalation: `don_Decision_Log.md` records, for Doc_01 Round 2, "logged as a review-to-review disagreement, with Round 2 superseding Round 1 on direct source verification." **Disposition: log it that way in the Decision Log, not escalate it.** The disagreement is settled by opening a file, which is what a Category 4 escalation is for when it *cannot* be.
  - **Registry rows 19/20 versus the Manifest on the Gallica finding (M12)** is a contradiction between two co-equal outputs of one pass. It is closable by the build thread in a sentence, so it is a defect and not a Category 4 item — but it must actually be closed, not carried.

**Assessment: no escalation category applies once M8's label is corrected and H1 is fixed — but §10's assessment as written is not sustainable.** It must be re-run after revision; it must cover all three documents rather than two; it must drop the Category 4 label; and it must route §9 item 8 and the acquisition-rights question explicitly rather than by silence. Until H1 is fixed, the Manifest should not go to the project lead in its current form, because the decision it asks for is partly not available.

**On disposition eligibility and completeness (V7.4: "A Registry without a saturation statement is not complete"):** the Registry's own saturation statement is honest in the direction that matters — it says the field-bibliography sweep was not run and does not claim closure — and Doc_02 §10 mirrors that honestly. **This is genuinely creditable and should be preserved.** Two qualifications. First, the statement opens "This Registry **closes** this revision pass…" and then says it is "not yet closed… in the full Construction Framework V7.4 sense," which is a small internal contradiction worth removing. Second, V7.4's requirement is not only that a sweep be acknowledged but that the statement "name the last unproductive searches — which queries, against which instruments, returned nothing new," and the current statement names none (L8) — where the sibling world has literal negative-sweep records for exactly this. The honest disclosure is a floor, not the requirement.

---

## Guidance for the revision pass

1. **H2 is a research task, not a writing task, and it is done in one file you already have open.** *On Baptism* I.1.2 and VII.5–6 are in `npnf104`, the same file as the Prolegomena. Read them, quote Augustine, and let row 31 do the narrower job it is actually good for. The corrected reading — reception common ground, justification in dispute — is the stronger argument, so this is an upgrade and not a retreat.
2. **H1 is a restructuring task with an existing template.** `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md` is four sections long and already solves every problem the Donatism Manifest has: supplied / open public-domain requests with priorities / confirmed-unavailable-in-public-domain, recorded not requested / consultation-only, never vendored. Adopt that shape. Do not invent a fifth one.
3. **Do not adopt this review's suggested wording without opening the file.** That is not a formality. It is the failure mode this world's Decision Log records six times across five review rounds, and it is how M5 and M6 got into the current draft — from Round 1's fix text, verbatim, unchecked. Where I have proposed replacement wording above, treat it as a description of what needs to be true, not as text to paste.
4. **Fix the citation cluster by opening every cited section, not by recognising the substance.** L1 survived Round 1's sweep for exactly the reason Round 1 predicted. There are now four in the cluster: L1 (two sites), L2, L3, and M10 (two sites).
5. **Nothing in "What checks out clean" above may be disturbed.** Specifically and above all: Registry row 6's Ep. 87 licensing constraint, which I re-verified against the letter itself and which is the best single piece of discipline in this document pair; the 256-council double entry in both rows and §9 item 6; the Augustine letters split; the four five-dimension Author Gravity entries; the Lucilla quotations and the I.16 citation; the two NPNF104 Prolegomena quotations as quotations; the §6 Article 23 restatement and the IJC inversion sentence; the §4 five-item evaluations; the forces-lens paragraph; and the Manifest's network-limitation disclosure, which I could not falsify and could corroborate three ways.
6. **Expect Round 3 to be short.** Two of the three highs-and-near-highs are localized to single paragraphs, the citation cluster is mechanical, and the escalation and clean-documents items are wording. What is not short is H1, which needs the Manifest rebuilt on the project's own existing shape — and that is worth doing properly, because it is the artifact that leaves this build and reaches a person.

---

*Review artifact filed per `cic-build-cycle`: review rounds exist as files, not claims. This review was conducted independently of the build thread that drafted the documents, and independently of Round 1, against primary and governing sources directly rather than against any document's own account of them. Where this review disagrees with Round 1 (M5, M6, M8), the disagreement is recorded as such rather than resolved silently, and rests on direct verification against the vendored files and the governing skill text.*
