# Doc_02 / Source Registry — Independent Adversarial Review, Round 2

**World:** Gallic Monastic-Ascetic Christianity (Atlas I.27, era 2, `gallic-monastic-ascetic-christianity`)

**Documents reviewed (revised):**
- `gallic_Doc02_Source_Ecology.md` (revised after Round 1)
- `gallic_Source_Registry.md` (revised after Round 1)

**Reviewer:** independent adversarial reviewer, cold — no drafting context, no involvement in the Round 1 review either. This is a follow-up check: every Round 1 finding was checked for whether the fix is *correct*, not merely present, and every claim and quotation the revision introduces was re-verified against the primary source, on the same discipline Round 1 applied.

**Also read for this review:** `gallic_Doc02_Review_Round1.md` (in full); `gallic_Doc01_World_Identification.md`; `gallic_G1_Scope_and_Source_Acquisition_Manifest.md`; `L3B-World-Build-Methodology/Source_Registry_Template.md` V1.0; the pre-revision Registry (`git show 458b5d6`); the corpus-map fix commit `188ebba`.

**Primary evidence independently re-consulted (not taken from the revision's own quotations):** `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` (Gennadius chapters XIX, LXII, LXIV, LXV, LXX, LXXXV, LXXXVI, XCV, read in full **with their endnotes**); `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`; `cic/texts/npnf105_augustine-anti-pelagian-writings.xml`; `cic/texts/npnf101_augustine-confessions-letters.xml` (letter sequence **and its own Prefatory Note**); `cic/corpus-map/_staging/npnf105_augustine-anti-pelagian-writings.yaml` and `cic/corpus-map/gallic-monastic-ascetic-christianity.yaml`; `cic/texts/REGISTRY.yaml`, `AUTHORS.md`, `STRUCTURE.md`.

---

## OVERALL VERDICT

# SUBSTANTIAL REVISION REQUIRED

**Round 1 findings: 18 FIXED, 9 PARTIAL, 1 NOT FIXED (of 28 substantial); 8 FIXED, 1 FIXED-by-removal-with-residue, 2 PARTIAL, 1 NOT FIXED (of 12 cosmetic).**
**New findings introduced by this revision: 18 (N1–N18), of which 6 are substantial enough to be load-bearing on downstream steps.**

The revision is real work and much of it is good. S1, S2, S15, S18, S19, S20, S21, S28 are cleanly and correctly fixed; the Gennadius volume was genuinely found, read, and rowed; the corpus-map fix landed properly at the root and I verified it; the Author Gravity Assessment for the editorial apparatus (S10) is substantive across all five dimensions and its Limitations paragraph is the best new writing in either document.

But the pattern the task asked me to test for **continued, and in the sharpest possible form.** Round 1's closing diagnosis was:

> "reading a passage correctly and then reasoning about it too quickly, in the direction the document already wanted to go... The discipline that catches that is not 'read the file' but '**state what the source says before stating what it supports**'... a fourth Doc_02 finding built the same way would not be caught by re-checking quotations."

The revision quotes that diagnosis back in its own preamble and declares it corrected. Then it does it again, five times, in the fix round itself:

1. **Four separate "new data from Gennadius" are not from Gennadius.** Sulpitius's dates ("born after 353, died about 410"), Cassian's death date ("died 450"), Vincent's "ordained presbyter specifically in 434," and Hilary of Arles's "429" are all **Ernest Cushing Richardson's 1892 editorial endnotes**, not the ancient text. Gennadius's own chapters date nothing; they end "in the reign of Theodosius and Valentinianus." This is *precisely* the S3 error — transferring the editorial apparatus's identification into an ancient author's mouth — committed four times in the document that corrects S3, and committed in the one place where the correction was most explicitly promised.

2. **The document's single *Documented* rating rests on one of those four.** §1.3 upgrades the *Commonitory*'s 434 date to Documented — "the one label in this document fully earned on convergent independent evidence" — on the strength of "Gennadius's independent presbyter-ordination date, the same year." There is no such date in Gennadius. The second anchor does not exist, and the endnote that supplies it is almost certainly derived from the *Commonitory*'s own internal Ephesus dating, making the claimed convergence circular as well as misattributed.

3. **§11's new forces-signal is contradicted by the page that governs it.** Doc_02 infers from the `npnf101` letters gap "which side of this controversy's literature that project's own institutional sympathies favored transmitting in full." That volume's **own Prefatory Note** names the omitted letters by number and gives its reasons: 225 and 226 under "*Some of the letters written by others to Augustin*" (they are not Augustine's); 221–224 under "*a large number of miscellaneous smaller letters*"; and the Pelagian letters generally under "*as the series contains three volumes of Augustin's anti-Pelagian writings*" — i.e. a cross-reference policy, the opposite of a suppression. 168 of 269 letters are printed, with 28 separate gaps. The document states in §10(b) that these omissions rest "on grounds this document cannot fully reconstruct from what it has read," in the same file it says it "checked specifically" for this.

4. **§3's corrected Lérins finding replaces one non-sequitur with another.** Having correctly withdrawn "Cassian's own dedication naming Honoratus as its abbot," §3 announces the link is "now doubly evidenced" by Gennadius's Faustus chapter. Gennadius on Faustus's abbacy (433/4, a generation later) says nothing about Cassian, nothing about Honoratus, and nothing about a Marseilles–Lérins link. What is doubled is the *existence of Lérins*, not the link. And the supporting quotation — "first abbot of the monastery at Lerins" — is cut immediately before "**and then made bishop** of Riez," the clause that makes "first" sequential rather than a claim of primacy. That is an ellipsis of the same shape as S1's.

5. **One Round 1 finding is asserted as fixed and is not fixed at all.** The Registry's own schema note states: "Boundary Status is restricted to exactly **Native** or **Excluded** — no other values." Ten rows carry `Native (context)` (14–16), `Native (pending intake)` (24–29), and `Native (pending discovery)` (32). S11 is verbatim un-actioned under a heading claiming it was actioned.

Separately, and independently disqualifying for a clean pass: **the Registry was renumbered wholesale**, in a document whose Template says "Append-only, no renumbering, no deletion" and whose own header claims "rows 30+ are new this revision, not renumbered from anything." Old rows 4–29 became 5–34. Roughly **twenty-five internal cross-references in Doc_02 and the Registry now point at the wrong row** — including every reference to the editorial apparatus (§2 and §3 cite "Registry row 16"; it is row 17), to the letters gap, to Stancliffe, to Mathisen, and to *Contra Collatorem*. The checkpoint rule that Round 1 called "the one rule that actually catches a builder" is now satisfied in substance and broken in navigation.

This is not a document that can be sent forward. Doc_03 and Doc_04 would inherit a fabricated *Documented* rating, a non-sequitur institutional link, an unsupported forces signal, and a Registry whose row numbers do not match its companion's citations.

**What would make this a clean pass is narrower than Round 1's fix list was.** Four claims must be withdrawn or re-grounded (N1–N4), one asserted-but-absent schema fix must actually be made (N6), the renumbering must be reconciled (N5), and about a dozen cross-references corrected. There is no new reading required beyond re-reading four pages the revision has already opened.

---

## ROUND 1 SUBSTANTIAL FINDINGS — FIX STATUS

| # | Round 1 finding (short) | Status | Detail |
|---|---|---|---|
| **S1** | "Massilian = Prosper's coinage" inverts its source | **FIXED** | Withdrawn explicitly as a withdrawal, not silently replaced. The footnote is now quoted in full including the derivation-from-the-city clause (I re-verified it verbatim at `npnf105`). The replacement "three competing labels" framing does **not** overclaim: each of the three is attributed to its actual authority ("geographic, unattributed derivation"; "Prosper's own words, **per this footnote**"; "per Doc_01 §7's Beza/Sanders research"). Doc_01 §7's own position is explicitly *not* claimed as corroborated. Clean. |
| **S2** | "Three-way Hilary tangle" manufactured | **FIXED** | Now stated as a **rival candidate**, not corroboration: "genuinely competing with both Doc_01 §10's preferred Gallic-lay-monk reading and the 'Hilary of Arles' reading Doc_01 §10 rejected — not a corroboration of either." "Hilary of Norbonne" survives only inside the withdrawal paragraph, correctly described as belonging to *Ep.* 178 in 417. I re-verified the endnote, the two "two laymen" passages, and the Index of Subjects (three Hilarys; Hilary of Sicily indexed to 497–498, 525; no Arles, no Norbonne entry). All accurate. §13 item 1 and the escalation note were rewritten to match. |
| **S3** | "Cassian's own dedication naming Honoratus as its abbot" | **PARTIAL** | The correction itself is exactly right and well stated in both §3 and Registry row 9: Cassian's text names two "holy brothers," says "one of you" presides over "a large monastery," names neither Lérins nor an abbot; the identification is the apparatus's. **But** the same bullet then builds a new non-sequitur on Gennadius (see **N4**), and Registry row 9's own note repeats it. |
| **S4** | Gennadius falsely stated to be unvendored | **PARTIAL** | The false statement is corrected head-on; the volume is read, rowed (row 30), and used throughout; the "different Honoratus" trap (ch. XCV, bishop of Constantina in Africa) is correctly identified and flagged — I verified the chapter and it is exactly as described. **But** the revision's own reading of Gennadius introduces four misattributions of editorial endnotes as ancient text (**N1**), miscounts the chapters (**N13**), and leaves the single most useful thing in the chapters — Gennadius's English summary of Faustus's *De gratia* doctrine — rowed but entirely unused (**N17**). |
| **S5** | §1.1's *Documented* unearned and self-contradictory | **FIXED** | Downgraded to **Widely Accepted** for the composite biographical picture, with the restriction stated explicitly ("not earned by this evidence for anything beyond 'a real, respected contemporary... who knew Martin'"). The internal contradiction with the section's own Confidence line is resolved. *(The supporting framing — "two independent ancient authorities" — is wrong; see **N3**.)* |
| **S6** | Conferences chronology rated near-Documented against the build's own Contested | **FIXED** | Downgraded to "Widely Accepted at most," with the Chadwick/Casiday tension named at the point of rating and carried at full Contested strength. The self-contradiction is explicitly acknowledged. |
| **S7** | Sulpitius Pelagianism *Contested* unearned | **PARTIAL** | The re-rating is genuinely better grounded: Gennadius ch. XIX does assert the charge flatly and in his own voice ("In his old age, he was led astray by the Pelagians..." — verified verbatim). **But** the stated basis is wrong: "two ancient sources in actual disagreement, one flatly asserting the charge, one reporting and rejecting it." The party doing the reporting and rejecting is `npnf211`'s Victorian translator (Alexander Roberts), not an ancient source. The rating may survive; the argument for it does not (**N3**). Note also that Roberts's "some ancient writers" is most plausibly Gennadius himself, which would make this one ancient claim and one modern denial rather than an ancient disagreement. |
| **S8** | Only three of five Article 17 levels used; §12 unfalsifiable | **PARTIAL** | Inferential/Thin is now used and correctly applied (§9 items 3–4, §12). Declining to force a Dominant Modern Reconstruction example is a defensible and honestly-stated call. §12 is rewritten as a real propagation statement. **Not fixed:** §1.3's heading still reads "fl. 425–434" with no label, when Doc_01 §2.3 explicitly rates c. 425 **Inferential/Thin** — the specific instance Round 1 named. §12 lists Inferential/Thin material and does not include it. |
| **S9** | Transmission History answers the wrong question | **PARTIAL** | Cassian's and Vincent's legs are now correct and genuinely good: Gibson named, the Conference XII/XXII excision routed in, the *Institutes* I.X Gazæus footnote added, Heurtley named, and the *Commonitory* Book II theft from Gennadius ch. LXV (verified verbatim). **Sulpitius's leg is wrong:** it states the underlying critical text is "not identified by editor or edition," when the same introduction Doc_02 quotes elsewhere names four — "the editions of Sigonius (1609), of Hornius (1664), of Vorstius (1709), and of **Halm (1866)**." The Cassian leg also misses the volume's own extended transmission discussion, which names **Petschenig's Introduction**, Gazet's 1616 Douay standard edition, and Dionysius's recension that "omits all that savours of Semi-Pelagianism" from Conference XIII — a doctrinally-motivated intermediary acting on this world's single most load-bearing text (**N10**). |
| **S10** | No Author Gravity for the editorial apparatus | **FIXED** | Present at §2, all five dimensions, substantive rather than perfunctory. Warfield correctly identified and correctly positioned (Princeton Calvinist, American reviser and Introduction author, *not* editor of record); Schaff, Holmes, Wallis correctly assigned; the Limitations paragraph draws the right methodological conclusion. The best new paragraph in the revision. *(One factual defect inside it: **N9**.)* |
| **S11** | Three non-schema Boundary values | **NOT FIXED** | The Registry's own schema note claims "Boundary Status is restricted to exactly **Native** or **Excluded** — no other values." The table contains `Native (context)` on rows 14, 15, 16; `Native (pending intake)` on rows 24–29; `Native (pending discovery)` on row 32. Ten of forty-one rows. Nothing was changed except the sentence saying it was changed. |
| **S12** | Row 3's mixed boundary buries an exclusion | **FIXED** (as prescribed) | Split executed: row 3 = *Dialogues* II–III (Native), row 4 = *Dialogue I* (Excluded / Named Comparandum) with a populated Comparandum Note that carries the Marseilles-as-port-of-call detail. This is what Round 1 asked for. *(Two residual notes: the split is what triggered the renumbering, **N5**; and formally excluding a text this world's own author wrote for his own community is in tension with the Template's "was this source actually used, inherited, or drawn on as part of this world's own formation" test — a licensing hazard being handled as a boundary determination. Round 1 prescribed it, so I do not relitigate; it is worth one sentence of reasoning in the row.)* |
| **S13** | Rows 22–27 blank Confidence | **FIXED** | All six (now rows 24–29) carry **B**, with the acquisition-status-vs-citation-reliability distinction stated correctly and the Cappadocian precedent cited. Exactly right. |
| **S14** | Rows 28–29 blank Type/Confidence; no Comparandum Note column | **PARTIAL** | Type and Confidence populated (rows 33, 34); a Comparandum Note column added and populated for rows 33–36. **But** the second half of the finding is unfixed and a new defect was added: the Template says "Both Exclusion Reasons still get a Verification Note explaining what was checked," and rows 37 and 38 (Out-of-Boundary) carry `—` in Verification Note with their exclusion reasoning placed in the **Comparandum Note** column, which the Template reserves for Named Comparanda. Rows 33–36's Verification Notes are exclusion rationales, not records of what was checked, when, against what (**N12**). |
| **S15** | Row 29's "thematic, not evidentiary" asserted without support | **FIXED** | Row 34 now states the literary-dependence question as open and two-sided, names the possible Native aspect as an inherited model, and reserves it to Stancliffe. This is exactly the disposition Round 1 asked for, and it is well written. |
| **S16** | Seven un-rowed sources named in support of claims | **FIXED** | All seven rowed: Gennadius (30), Rule of Benedict (36), Jerome *Comm. Ezech.* (37), Augustine *Ep.* 205 (38), Noris (39), Tillemont (40), Farrar (41). The Out-of-Boundary exclusion reason is now used (37, 38), closing the "zero Out-of-Boundary rows" structural gap Round 1 noted. *(Minor residue: §1.4 now cites "Doc_01 §7's Beza/Sanders research" in support of a specific claim about the "Semi-Pelagians" label; neither is rowed. And row 39 licenses Noris for two Doc_02 claims the revision deleted — **N16**.)* |
| **S17** | Affirmative Duty missing element (c); participant sentence undischarged; category slip | **PARTIAL** | (a), (b), (c) are now all present and (c) is well done — "can honestly speak for the formation ecology's own leadership and its own literary self-understanding; it cannot honestly claim, without flagging the gap live, to speak for what this world's own daily life felt like to someone who left no text" is a real, usable sentence. The Massilian-voice category slip is corrected and explained. The enslaved, rural communities, and children/oblates are added. **But** §10 asserts "(§13 below names this explicitly as owed to that document, not merely asserted as an obligation here)" — and §13's eight items contain **no such item**. The ownership hand-off Round 1 specifically asked for is claimed and absent (**N15**). |
| **S18** | Negative bounded-reconstruction finding asserted over unread corpus | **FIXED** | Now restated plainly as a coverage limit, with the unread material enumerated and the stronger claim explicitly withdrawn. Well done. |
| **S19** | Claudia mischaracterized in both directions | **FIXED** | All three corrections made and correct. I verified Letter II ("Concerning Virginity") and its opening passage verbatim, including "those who are virgins possess something above the rest... presented by the bishop... at the altar of God." The elite/ascetic reframing is right and §10 no longer leans on her. |
| **S20** | "Fullest surviving statement" overclaimed; NPNF letters gap unnamed | **FIXED** | The gap is verified (I independently confirmed `npnf101` runs CCXX → CCXXVII), rowed (row 31), and the claim is walked back precisely — "the fullest statement *in this project's current library*, not the fullest surviving statement." Registry row 15 carries the same correction. *(The **inference** built on the gap at §11 is a separate new error — **N2b**/**N11**.)* |
| **S21** | *Institutes* citation off by one; quote outside any row's verification | **FIXED** | Corrected to I.10 / I chapter X in both §1.2 and §9 and in Registry row 7, whose Verification Note now covers the chapter read and the verbatim quote. I verified the passage sits in Chapter X, that the quoted words are exact, and that the "altogether omitted in the edition of Gazæus" footnote is attached to that chapter. |
| **S22** | Material Culture covers two of four required categories | **FIXED** | §9 now addresses all four, with categories 3 and 4 argued from Mathisen plus primary-text incidental detail and the Priscillianist affair, and both correctly labelled Inferential/Thin. The §5/§9 duplication is resolved (§5 now points forward). |
| **S23** | Sweep never searched the project's own library | **FIXED** (as far as feasible) | The library sweep was run and is what produced rows 30 and 31; I confirmed `REGISTRY.yaml`, `AUTHORS.md` and `STRUCTURE.md` all index the Gennadius volume, so the method genuinely works. The unreached dedicated instruments are named individually as a coverage limit in both documents, and the saturation statement is restated at the strength supported. |
| **S24** | Secondary Scholarship half-met; silent re-deferral | **PARTIAL** | Weaver 1996 added (row 23) — the right work, and the largest single recall gap closed. **But** the "relationship between synthesis and specialist scholarship" element is *named as a gap* rather than addressed, which is honest but is not the activity; interpretive commitments, period and reception are still absent for all six works (Chadwick 1950 vs Casiday 2007 as two generations of method is still unremarked). The re-deferral at §13 item 4 is recorded but still does not say it is re-deferring an obligation Doc_01 §11 item 8 assigned to *this* document. |
| **S25** | Corpus map still carries the overturned Hilary identification | **PARTIAL** | **The corpus-map half is properly fixed and I verified it independently.** Commit `188ebba` edits the staging file at the root, re-merges, and the generated `gallic-monastic-ascetic-christianity.yaml` now reads "a correspondent named Hilary" on all three Augustine rows, with a correction note naming the Hilary-of-Sicily rival. No stale "Hilary of Arles" identification survives in either file, and the sibling buckets (`pelagianism`, `latin-pastoral-congregational-christianity`) were re-merged too. This matches what Doc_02 §1.4 and §13 claim. **The other half is untouched:** G1 Part C item 3 still asserts, unqualified, "corrected 2026-09-08, after Doc_01's Round 2 review (finding N6a)... **The distinction is disclosed in each work's own corpus-map note, not smoothed over**" — the sentence Round 1 proved false. G1 was never corrected to record that the claimed correction had not in fact reached the file. Doc_02 §15 escalates the *pattern* while leaving the *instance* standing. |
| **S26** | No per-row discovery metadata | **FIXED in form** | Channel / instrument / date columns added on all 41 rows, and the Priority-flags section can now actually apply the rule. Two residues: the metadata is reconstructed after the fact, which the Framework explicitly forbids ("logged as searches happen — never reconstructed afterward"), and every new row is stamped **2026-09-09**, a date that has not occurred (**N14**). Also, replacing the schema's `Added` field rather than adding to it drops a Template-required column. |
| **S27** | No boundary around the rest of the Augustine corpus | **PARTIAL** | Rows 35 (rest of Augustine) and 36 (Rule of Benedict) added, both well reasoned; row 35 in particular states the risk correctly and licenses only rows 14–16. **Not addressed:** the Egyptian desert *sayings* material (*Apophthegmata*, *Historia Lausiaca*, Palladius — several vendored), which Round 1 named as the second instance. Row 4 covers only Sulpicius's own Dialogue I. |
| **S28** | "Directly verified this session" second-hand | **FIXED** | Restated precisely at editor's-claim strength, with the editor's own hedged formulation quoted and Registry row 13's contradicting note acknowledged in the text. Exactly the right correction. |

**Substantial totals: 18 FIXED · 9 PARTIAL · 1 NOT FIXED.**

---

## ROUND 1 COSMETIC FINDINGS — FIX STATUS

| # | Finding | Status | Detail |
|---|---|---|---|
| **C1** | Mis-pointed Desiderius cross-reference | **FIXED by removal** | The sentence no longer appears. |
| **C2** | Noris/Cassian Latin quoted as English | **FIXED by removal, with residue** | Both quotations are gone from §3. But Registry row 39 still licenses Noris for "the Lérins-as-cells architectural quotation" and for §1.3's "non modo Semipelagianum se prodit" — neither of which the revised Doc_02 contains (**N16**). |
| **C3** | Pauline exposition chapter ranges | **FIXED** | §1.3 now gives Gal. 1:8 = chs. 8–9 and 1 Tim. 6:20 = chs. 21–24, as two distinct expositions. Matches the chapter titles. |
| **C4** | Conferences dedicatees | **FIXED** | Row 8 now "Helladius and Leontius"; row 10 now "Jovinianus, Minervius, Leontius, and Theodore." |
| **C5** | "W." unresolved; Warfield's role misdescribed | **FIXED** | Resolved to Warfield from the title page, role corrected (Schaff editor; Holmes and Wallis translators; Warfield reviser/Introduction), open item deleted. |
| **C6** | search_record row ranges wrong | **PARTIAL** | Ranges are now internally consistent (1–13 `npnf211`, 14–16 `npnf105`, 18–22 WebSearch, 24–29 sibling), and rows 17, 23, 30, 31 have their own lines. **Rows 33–41 — nine rows, including all four comparanda and all five testimonia — appear in no search_record entry at all**, which is the exact defect C6 named for old rows 28–29. |
| **C7** | *Sacred History* cross-assignment drops one world | **FIXED by removal** | The clause is deleted rather than corrected; row 6 no longer states any cross-assignment. Not wrong any more, but the (correct) fact that G1 records it as shared with `imperial-juridical-christianity` **and** `priscillianist-asceticism` is now recorded nowhere in Step 2. |
| **C8** | Date inconsistencies across the four documents | **PARTIAL** | The Sulpitius date discrepancy is now disclosed rather than silently resolved — good — though misattributed (**N1**). **G1 Part A still gives "Vincent d. c. 445"** against Doc_01 §2.4's and Doc_02 §1.3's "d. before 450"; unreconciled, unmentioned. |
| **C9** | Sidonius Apollinaris silently dropped | **NOT FIXED** | I grepped both documents: **"Sidonius" appears zero times** in Doc_02 and zero times in the Registry. Doc_01 §11 item 7 hands Doc_02 three named leads for the 450–480 interval; two are handled and the third is still neither rowed nor excluded. Worth noting that the Gennadius volume the revision has now read contains a chapter on Sidonius (ch. XCII, "Sidonius the bishop") — the lead was one line away from being closed in the same pass. |
| **C10** | §12 unfalsifiable | **FIXED** | Rewritten as an actual tier-by-tier propagation statement. |
| **C11** | Framework/Template flagging-rule divergence undisclosed | **FIXED** | Disclosed explicitly in the Priority flags section, with both rules stated, the Template's applied as primary with a reason, and the divergence named for the coach thread. Well handled. |
| **C12** | Row 16 citation under-specified | **FIXED** | Row 17 now carries the full editorial and translator citation for both volumes from their own title pages. |

**Cosmetic totals: 8 FIXED · 1 FIXED-by-removal-with-residue · 2 PARTIAL · 1 NOT FIXED.**

---

## NEW FINDINGS — errors introduced by this revision

*Numbered N1–N18. N1–N6 are substantial and load-bearing.*

---

### N1 — SUBSTANTIAL. Four "new data from Gennadius" are Richardson's 1892 editorial endnotes, not Gennadius's text. This is the S3 error, committed four times inside the S3 fix round.

Gennadius's chapters date **nothing**. Every one of them closes with a regnal formula ("in the reign of Theodosius and Valentinianus"). The specific years the revision attributes to him are the modern translator-editor's bracketed endnotes, appended to the chapter's opening word:

| Doc_02 claim | Where the revision puts it | What the file actually is |
|---|---|---|
| "**Gennadius's own chapter** (`npnf203`, ch. XIX, read directly this revision) gives '**born after 353, died about 410**'" (§1.1) | Presented as one of "two independent **ancient** authorities" disagreeing on Sulpitius's dates | Endnote on ch. XIX: *"Sulpicius Severus born after 353, died about 410."* — **Ernest Cushing Richardson**, Princeton College librarian, 1892 |
| "**Gennadius also gives a specific death date, 'died 450,'** not previously in hand" (§1.2) | Presented as ancient corroboration for Cassian | Endnote on ch. LXII: *"Johannes Cassianus died 450."* Gennadius's own text says only "in the reign of Theodosius and Valentinianus" |
| "Vincent was ordained **presbyter specifically in 434** — the same year as the *Commonitory* itself, **a precise new datum**" (§1.3) | Load-bearing: it is the second anchor for the document's only **Documented** rating | Endnote on ch. LXV: *"Presbyter 434, died before 450."* Gennadius's own text says only "presbyter in the Monastery on the Island of Lerins" |
| "he succeeded Honoratus at Arles in **429, per Gennadius ch. LXX's own date**" (§1.4) | Used to correct Doc_01's "bishop 430–449" | Endnote on ch. LXX: *"Born about 401, bishop 429, died 449."* Gennadius's own text gives no dates |

This is the identical error Round 1 recorded as S3 and which the revision's own preamble says it has cured: *"'the source says something adjacent to what I need' was allowed to become 'the source confirms what I need.'"* Here it is worse than S3, because S3 at least transferred an identification from the same volume's apparatus; here a nineteenth-century Presbyterian librarian's dating notes are attributed to a fifth-century Massilian presbyter and then used as **independent ancient corroboration** against another nineteenth-century editor.

**Required:** re-attribute all four to Richardson's apparatus, and re-derive whatever survives. Note that this *strengthens* one of the revision's own instincts — the apparatus Author Gravity Assessment at §2 covers `npnf211` and `npnf105` only; `npnf203`'s apparatus is a third editorial layer, currently unassessed, undeclared, and folded silently into Registry row 30 as if it were primary text rated **A**.

---

### N2 — SUBSTANTIAL. The document's only *Documented* rating rests on the fabricated anchor, and the convergence it claims is circular even if the anchor existed.

§1.3: *"the 434 date, **now doubly anchored** (internal Ephesus dating and Gennadius's independent presbyter-ordination date, the same year) — **Documented**, the one label in this document fully earned on convergent independent evidence."* §12 carries it forward as one of exactly two Documented facts in the whole ecology.

Two problems, either of which is fatal to "convergent independent evidence":

1. **Gennadius supplies no 434.** He says Vincentius was a "presbyter in the Monastery on the Island of Lerins," full stop. The year is Richardson's endnote.
2. **Richardson's 434 is not independent of the *Commonitory*.** The *Commonitory*'s own internal dating (three years after Ephesus 431) is the standard basis for placing Vincent's floruit; an editor's one-line note giving "Presbyter 434" is overwhelmingly likely to be derived from that same datum. Presenting it as a second, independent anchor converts a single piece of evidence into a convergence.

The **rating itself may survive** — Doc_01 §2.4 already rates the 434 composition date *Documented* on the internal Ephesus evidence plus its own independent research, and does so carefully. But Doc_02 must not claim a second anchor it does not have, and must not describe this as the one label "fully earned on convergent independent evidence." As written, the single strongest confidence claim in the document is supported by a sentence that does not exist in the source it cites.

---

### N3 — SUBSTANTIAL. "Two independent ancient authorities" / "two ancient sources in actual disagreement": in both cases the second party is a Victorian editor.

§1.1 twice frames a modern editor as an ancient witness:

- *"Who he was — now on **two independent ancient authorities**, not one, and they disagree on his dates."* The two are `npnf211`'s introduction and `npnf203`'s Gennadius chapter. `npnf211`'s introduction is **Alexander Roberts's** (the volume's own title page: "The Works of Sulpitius Severus. Translated, with preface, and notes, by Rev. Alexander Roberts, D.D., Professor of Humanity, University of St. Andrews"). And per N1 the `npnf203` dates are Richardson's. So the "disagreement between two ancient authorities" is a disagreement **between two nineteenth-century editors**, neither of whom is ancient and neither of whom is described as an editor at the point of use.
- *"This now genuinely meets Article 17's *Contested* bar — **two ancient sources in actual disagreement**, one flatly asserting the charge, one reporting and rejecting it."* Gennadius asserts; the party "reporting and rejecting" is Roberts ("it seems to us that there is no ground for any such conclusion"). One ancient source, one Victorian denial.

This is the specific failure the revision's own §2 Author Gravity Assessment says would have prevented S1: *"A reader should weigh every claim this apparatus makes... with this institutional and theological position in view."* The assessment was written; it was not applied to the very next section that needed it.

---

### N4 — SUBSTANTIAL. §3's corrected Lérins finding replaces one non-sequitur with another, and truncates its supporting quotation before the clause that changes its meaning.

§3, immediately after the correct S3 withdrawal:

> "This document now also has **independent ancient corroboration for the Lérins identification specifically**... Gennadius's own chapter on Faustus (ch. LXXXVI) states directly that Faustus was 'first abbot of the monastery at **Lerins**'... **The link between Cassian's Marseilles and the institution at Lérins is therefore real and now doubly evidenced** — by Gennadius directly for Faustus's own abbacy, and by the editorial apparatus's identification of Cassian's own dedicatees."

Gennadius ch. LXXXVI concerns **Faustus**, whose Lérins abbacy is dated 433/4 in the same volume's apparatus — years after Cassian's dedication, and about a different man. It says nothing about Honoratus, nothing about Cassian, and nothing about any Marseilles–Lérins relationship. What is now doubly evidenced is that **Lérins existed and had abbots**, which was never in dispute. The link itself remains exactly where the S3 correction correctly put it: on the editorial apparatus alone. Calling it "doubly evidenced" walks the correction halfway back in the same bullet.

The quotation is also cut in the S1 manner. Gennadius's full clause is: *"Faustus, **first** abbot of the monastery at Lerins, **and then made bishop** of Riez in Gaul..."* — "first... then" is a sequence. Doc_02 stops at "Lerins," leaving a reader with an apparent claim that Faustus was *the first* abbot of Lérins, which contradicts Doc_01 §2.3's Honoratus-as-founder finding.

**Worse, the corroboration the revision wanted was available in a chapter it read.** Gennadius ch. LXV places **Vincentius** as "presbyter in the Monastery on the Island of Lerins" — a genuine, near-contemporary ancient attestation of Lérins as an institution housing one of this world's own three primary voices. That is real independent evidence for the Lérins node; it just is not evidence for the Cassian dedication. The revision quotes ch. LXV for the pseudonym and the Book II theft and never notices the institutional datum in its first line.

---

### N5 — SUBSTANTIAL. The Registry was renumbered wholesale, in violation of the Template's living-document protocol, and about twenty-five cross-references now point at the wrong rows.

The Template, twice: *"Append-only, no renumbering, no deletion"* (Living-document protocol) and *"**#** | Sequential ID, **never reused**"* (Entry schema). The revised Registry's own header says: *"Append-only: no renumbering, no deletion... rows 30+ are new this revision, **not renumbered from anything**."*

Comparing against the pre-revision file (`git show 458b5d6`), old rows 4–29 were shifted to 5–34 to make room for the *Dialogue I* split. Rows 33 and 34 are the old comparanda rows 28 and 29, renumbered — directly contradicting the header's own assurance. The document log compounds this by re-citing Round 1's findings against the *new* numbers ("S14... rows 33–34's blank Type/Confidence"), which makes the finding trail unreadable against the review it answers.

The navigational damage is extensive. Verified misdirected references:

**In Doc_02** — §1.2 "Registry row 10" (Conf. XII/XXII → row **11**); §1.3 "Registry row 12" (*Commonitory* → **13**); §1.4 "Registry row 22" (Faustus → **24**), "Registry row 30" (letters gap → **31**), "Registry row 31" (*Contra Collatorem* → **32**); §2 "Registry row 16" ×2 (apparatus → **17**), "Registry row 29" (Gennadius → **30**); §3 "Registry row 16" (apparatus → **17**); §7 "Registry row 17" (Stancliffe → **18**); §9 "Registry row 19" (Mathisen → **20**); §10 "Registry rows 10 and 30" (→ **11** and **31**); §11 "Registry row 31" (→ **32**); §13 items 2 and 5 (same two errors again).

**Inside the Registry** — row 9 cites "(row 16)" for the apparatus (→ **17**) and "(row 29)" for Gennadius (→ **30**, while 29 is Prosper's *Pro Augustino Responsiones*); row 12 cites "(row 29)" twice for Gennadius; row 15 cites "row 30" for the letters gap (→ **31**); row 18 cites "row 20's own comparandum reasoning" for the *Vita Antonii* (→ row **34**; row 20 is Mathisen).

Every one of these lands on a real but wrong row, so none of them fails loudly. Two of them — row 9's "(row 29)" and row 18's "row 20" — point at rows that could plausibly be mistaken for the intended target by a reader not checking.

**Required:** either restore the original numbering and append *Dialogue I* as row 30 (Template-compliant, and the header already claims this is what happened), or state the renumbering openly as a deliberate one-time exception with a mapping table — and correct all twenty-five references either way.

---

### N6 — SUBSTANTIAL. S11 is declared fixed in a dedicated schema note and is not fixed.

Registry, "Schema note (Round 1 findings S11, S14, S26)": *"Boundary Status is restricted to exactly **Native** or **Excluded** — no other values."*

Registry table, Boundary column: `Native (context)` — rows 14, 15, 16. `Native (pending intake)` — rows 24, 25, 26, 27, 28, 29. `Native (pending discovery)` — row 32.

Ten rows. The document log repeats the claim: "Boundary column restricted to Native/Excluded." The consequence Round 1 named is unchanged: the Template's handoff rule passes only Native entries forward to Doc_03 and Step 10, and six of these ten (24–29) license nothing because they are not vendored, while row 32 records a work with no located edition at all. A downstream filter on the literal string `Native` still picks up none of them; a filter on `startswith("Native")` still picks up all of them. Either way the gate does not do its job.

That a fix round can assert a schema correction in a dedicated note while leaving the field untouched is itself the finding worth escalating: it is the same shape as the G1/corpus-map failure this build has now hit three times (Doc_01 N6, Doc_02 S25, and here).

---

### N7 — SUBSTANTIAL. *Contra Collatorem*'s "discovery via Gennadius" is misattributed: `npnf211`'s own Cassian prolegomena names the title, describes the treatise, and locates its edition. Row 32's Confidence D is wrong on the Template's own tier definitions.

§11 and Registry row 32: *"**Registry row 31 — Prosper's *Contra Collatorem*, a third Prosper work, not previously identified, found via Gennadius rather than via the sibling session's own sweep**."* Row 32's Verification Note: *"Existence and general subject confirmed via Gennadius's own description; **no accessible edition located yet**."*

Gennadius does **not** name the work. He says only "an anonymous book against certain works of Cassianus." The title *Contra Collatorem* is builder-supplied — which, per the Template's step 4, is `discovery_channel: builder-prior-knowledge`, the exact channel the priority-review flag is keyed to, and the row instead records `builder-direct-read`.

And the work was already in the vendored file this build has read from the start. `npnf211`'s Cassian prolegomena:

> "This was the origin of **Prosper's work 'Contra Collatorem,'** against the author of the Conferences, a treatise of considerable power and force, although not scrupulously fair. **The treatise is given in Gazet's edition of Cassian.**"

— with a further note elsewhere that Gazet's text is the basis of Migne's. So: the title is named, the content characterised, the edition located, all in a source Registry row 17 already covers at Confidence A. Row 32's **D** is wrong on the Template's own scale (*D = "Tradition/genre-level attribution, no specific text/author named"*); a named author and a named work with a located edition is at minimum **C** and on this evidence **B**.

This also undercuts §14's headline methodological claim. The revision's lesson from Round 1 was "search the project's own library." The library was searched at the *filename/index* level and it worked. It was not searched at the level of the introductions the build had already been quoting for two drafting passes — which is where *Contra Collatorem*, Petschenig, Gazet, Halm, and Dionysius's Conference XIII recension all are.

---

### N8 — MODERATE. Registry row 12's confidence annotation is internally incoherent and moves the wrong way.

Row 12 (*De Incarnatione*): Confidence field reads *"B → **C, corrected upward this revision on Gennadius's independent corroboration**."*

Three problems in one cell: (a) the pre-revision row (old row 11) was already **C**, not B, so the arrow's origin is wrong; (b) **C is lower than B** on the Template's axis, so "corrected upward" describes a downgrade; (c) the evidence now in hand — Gennadius ch. LXII stating the Leo commission, read directly and verbatim this session — supports **B or A**, not C. The substantive point (Gennadius independently corroborates Doc_01's Leyser-sourced Leo detail) is correct and well found; the grade attached to it is backwards.

---

### N9 — MODERATE. §2's Author Gravity Assessment states that `npnf211`'s introduction is anonymous. Each of its three introductions is signed on its own title page, with institutional position.

§2, Limitations: *"`npnf211`'s own introduction is **anonymous as to its specific author** within the volume's editorial team."*

The volume's own title pages, in the same file, on the same kind of page the revision says it "checked directly this revision" for `npnf105`:

- *"The Works of Sulpitius Severus. Translated, **with preface, and notes**, by Rev. **Alexander Roberts**, D.D., **Professor of Humanity, University of St. Andrews, Scotland**."*
- *"The Commonitory of Vincent of Lérins... Translated by Rev. **C. A. Heurtley**, D.D., **The Lady Margaret's Professor of Divinity in the University of Oxford, and Canon of Christ Church**."*
- *"The Works of John Cassian. Translated, **with prolegomena, prefaces, and notes**, by Rev. **Edgar C. S. Gibson**, M.A., **Principal of the Theological College, Wells, Somerset**."*

So each author's introduction is written by that author's own translator, named, with his institutional and confessional location on the page. This is not a technicality: it is exactly the material the Author Gravity dimension exists to capture, it is what made the Warfield identification productive two sentences earlier in the same paragraph, and the assessment declares it unavailable while sitting on top of it. Two Anglican professors of divinity and a Scottish Professor of Humanity is a materially different apparatus profile from "anonymous editorial team," and it bears directly on how much weight §1.1's Pelagianism rebuttal (Roberts's) and §1.2's chronology (Gibson's) should carry.

---

### N10 — MODERATE. The Transmission History rewrite (S9) reports as unavailable material that is named in the same prolegomena, including the one doctrinally-motivated intermediary that touches this world's most load-bearing text.

§1.1: Roberts's translation is *"itself made from a specific underlying critical text **this document has not identified by editor or edition**."* The same introduction, three paragraphs from the biographical passage §1.1 quotes: *"we have had constantly before us the editions of **Sigonius (1609)**, of **Hornius (1664)**, of **Vorstius (1709)**, and of **Halm (1866)**."*

For Cassian, `npnf211`'s prolegomena carry an extended transmission discussion the revision does not use, including:

- **Gazet's 1616 Douay edition**, "what has remained until the present day the standard edition of Cassian's works," with its "annotations... on a number of passages (some thirty in all) of doubtful orthodoxy, in order to put the reader on his guard against following Cassian in his errors";
- **Petschenig's Introduction to Cassian** (i.e. the CSEL critical text), cited by page;
- **Dionysius's recension**, which "in his endeavour to make Cassian orthodox, **omits all that savours of Semi-Pelagianism**" from the **Thirteenth Conference**, "and from c. viii. onward there are large omissions and various suggestive alterations in the text";
- a recension made "in the interests" of a doctrinal position by Victor of Martyrites.

Dionysius's alteration of Conference XIII is a named intermediary with a named theological agenda acting on the single text this world's grace controversy turns on. It is the textbook answer to the Framework's question. Round 1's S9 asked for exactly this and the revision reached for it in the Gazæus footnote — which is the smaller instance on the same page family — while leaving the larger one unread.

---

### N11 — MODERATE. §11's new forces-signal is refuted by the Prefatory Note of the volume it is drawn from, and §10(b)'s "grounds this document cannot reconstruct" are stated in that same note.

§11: *"whatever historical or editorial process led a nineteenth-century Protestant translation project to include Augustine's replies but not the letters that provoked them is itself informative about **which side of this controversy's literature that project's own institutional sympathies favored transmitting in full**."*
§10(b): the omissions are *"on grounds this document cannot fully reconstruct from what it has read."*

`npnf101`'s own Prefatory Note, in the file Doc_02's header says it "checked specifically for the letter sequence discussed at §1.4 and §10," states the grounds by number:

> "Of the two hundred and seventy-two letters given in the Benedictine edition... **one hundred and sixty are translated in this selection**... the general reasons which have guided us in the selection. We have omitted— ... **II. Almost all the letters relating to Pelagianism, as the series contains three volumes of Augustin's anti-Pelagian writings (vols. iv. xii. xv.)**... **V. Some of the letters written by others to Augustin. This excludes—94, 109, 121, 160, 168, 225, 226, 230, 270. VI. A large number of miscellaneous smaller letters... This excludes—110, 112, ... 221, 222, 223, 224, ...**"

So 225 and 226 are omitted **because they are not Augustine's letters**, and 221–224 as **miscellaneous minor letters** — and the volume's stated policy on Pelagian material is a *cross-reference* to the three anti-Pelagian volumes, i.e. the opposite of a sympathy against transmitting that side. I counted the printed sequence independently: **168 of 269 letters, with 28 separate gaps**, of which 221–226 is one.

Consequences:

1. **§11's inference must be withdrawn.** It is not merely unsupported; the governing page contradicts it.
2. **§10(b) must be corrected.** The grounds are reconstructible and are stated verbatim.
3. **Registry row 31's framing — "on the same pattern as row 11" — is wrong.** Row 11's absences (Conference XII, XXII) carry no stated reason, are content-specific, and are exactly about sexuality and the body. Row 31's are declared, general, and neutral. Equating them dilutes the good finding at row 11.

The *row itself is still right to exist* — the two letters are genuinely unvendored and genuinely the most consequential missing documents for this world. Only the interpretation attached needs to go.

---

### N12 — MODERATE. Rows 37–38 place their exclusion reasoning in the Comparandum Note column and leave the Template-required Verification Note blank.

Template: *"Both Exclusion Reasons still get a **Verification Note** explaining what was checked; only a Named Comparandum **additionally** needs a clear statement of the specific image, claim, or reading it must not be mistaken for."*

Rows 37 (Jerome, *Comm. Ezech.* 36) and 38 (Augustine, *Ep.* 205) are Excluded / **Out-of-Boundary**. Both carry `—` in Verification Note, with their reasoning ("Cited only as third-party testimony... Jerome's own corpus belongs to a different world") sitting in the **Comparandum Note** column — a field the Template scopes to Named Comparanda only. Under the Registry's own schema note, which introduced that column for precisely that purpose, these two rows misuse it and drop the field the Template actually requires of them.

Related, on rows 33–36: their Verification Notes are exclusion *rationales* ("The case document's own G0 ruling deliberately excludes...", "Doc_01 §2.1 draws the analogy...") rather than records of what was checked, when, against what. Round 1's S14 named this defect on old row 29 specifically; it now applies to four rows instead of one.

---

### N13 — COSMETIC-PLUS. Two count errors introduced this revision.

- §2: *"with named chapters on **eight** of this world's own principals — Sulpitius (ch. XIX), Cassian (LXII), Eucherius (LXIV), Vincentius (LXV), Hilary of Arles (LXX), Prosper (LXXXV), and Faustus (LXXXVI)"* — **seven** are listed. The revision correctly removed Honoratus from Round 1's list of eight (Round 1 had wrongly included him) and did not adjust the count. Doc_02's own header, §15, and Registry row 30 all correctly say seven.
- §13 item 8: *"The **five** not-yet-vendored sibling-located leads (Faustus, two Eucherius works, Hilary of Arles's *Vita Honorati*, two Prosper works)"* — **six** are listed, six are rowed (24–29), and G1 logs six.

---

### N14 — COSMETIC-PLUS. Every new row and search_record entry is stamped 2026-09-09, a date that has not occurred.

Today is 2026-09-08. Every commit in this build, including the corpus-map fix the revision cites, is 2026-09-08. Doc_02 and the Registry stamp all revision work, all new discovery dates, and the corpus-map correction note as **2026-09-09**. Since `discovery_date` is one of the three per-row fields the Framework requires (and requires "logged as searches happen — never reconstructed afterward"), forty-one rows now carry a metadata field that is both reconstructed and post-dated.

---

### N15 — MODERATE. §10 states that §13 records the Facilitator-Governance ownership. §13 does not.

§10(c) closes: *"This is the sentence the Facilitator-Governance apparatus should carry forward (**§13 below names this explicitly as owed to that document**, not merely asserted as an obligation here)."*

§13's eight carried-forward items are: the Hilary identification; the two edition-level gaps; critical editions/translations; the six secondary works; *Contra Collatorem*; Van Dam and a synthesis history; the library sweep discipline; the five/six unvendored leads. **None concerns the Facilitator-Governance function, the participant-facing naming language, or Article 20 at all.** The claim that the hand-off is recorded is false, and it is false about the precise element Round 1's S17 said was missing — the difference between describing the obligation and discharging it.

---

### N16 — COSMETIC-PLUS. Registry row 39 licenses Noris for two Doc_02 claims the revision deleted.

Row 39's Licensed For: *"Doc_02 §1.3's Vincent-Massilian-sympathy reading ('non modo Semipelagianum se prodit'); the Lérins-as-cells architectural quotation."* Neither the Latin tag nor the cells quotation survives in the revised Doc_02 (both were removed in the course of fixing C2). The checkpoint rule runs Doc_02 → Registry; this is the reverse mismatch, and it leaves a Native row licensed for nothing the ecology actually says.

---

### N17 — MODERATE. The chapters were read; three substantive findings inside them were not taken.

All three are in text the revision quotes from and states it read in full:

1. **Gennadius's English summary of Faustus's *De gratia* is rowed and never used.** Ch. LXXXVI: *"he teaches that the grace of God always invites, precedes and helps our will, and whatever gain that freedom of will may attain for its pious effect, **is not its own desert, but the gift of grace**."* Registry row 30 lists this among what the row closes; Doc_02 uses it nowhere. It is a near-contemporary characterisation of the leading "Massilian-side" theologian's own doctrine as strongly grace-prevenient — which complicates §1.4's and §11's framing of the controversy and bears directly on Doc_04's gravity work. Round 1's S4 named this as one of four gaps rowing Gennadius would close; rowing it closed the bookkeeping and not the gap.
2. **Gennadius calls the *Dialogues* "a sort of dialogue in two divisions"** against `npnf211`'s three — a genuine ancient transmission datum bearing directly on the *new* rows 3/4 split, which is built on a three-Dialogue structure. Unremarked.
3. **Ch. LXX independently attests Hilary of Arles's *Vita Honorati*** ("that work which is of so great practical value to many, **his Life of Saint Honoratus, his predecessor**") — an ancient witness to the existence and subject of Registry row 27, this world's missing founding narrative, which the row currently records at B on an archive.org location alone. Also unremarked.

The pattern is worth naming because it is the mirror image of N1: where the revision *did* find new data it took an editor's note for the ancient text, and where the ancient text genuinely offered new data it did not take it.

---

### N18 — COSMETIC. "Gallus" is described as the frame narrator.

§1.1: *"describes the *Dialogues* as 'a Conference between Postumianus and Gallus' — Gennadius's own name for the **frame narrator**."* Gennadius's own sentence continues "**in which he himself acted as mediator and judge of the debate**" — the frame narrator is Sulpitius; Postumianus and Gallus are the two disputants. *(The underlying observation is correct and I verified it: "Gallus" appears **zero times** in `npnf211`, whose translation calls the third speaker only "the Gaul" / "this Gallic friend." The hedge attached to it — that whether "Gallus" was ever the man's name is not determinable from what this document has read — is exactly the right register, and is one of the better-disciplined sentences in the revision.)*

---

## WHAT GENUINELY NOW HOLDS UP

Stated before the fix list, because a fair amount of this revision is good and some of it is very good.

**Quotations and locations I re-verified independently and found exact:**

- Gennadius ch. XIX on Sulpitius, verbatim, including *"a man distinguished by his birth, by his excellent literary work, by his devotion to poverty and by his humility, beloved also of the sainted men Martin bishop of Tours and Paulinus Nolanus"*; *"He wrote to his sister many Letters"*; and the Pelagian passage *"In his old age, he was led astray by the Pelagians, and recognizing the guilt of much speaking, kept silent until his death..."* — and §1.1's characterisation of the last as a flat assertion in Gennadius's own voice, not a report of others, is correct and is a real strengthening of the S7 material.
- Gennadius ch. LXII on Cassian: the John-the-Great ordination, the presbyterate at Marseilles, *"two monasteries, that is to say one for men and one for women, **which are still standing**"*, and *"at the request of Leo the archdeacon, afterwards bishop of Rome"*. I also counted the Conference list: **twenty-four**, exactly as §1.2 says, in Gennadius's own order. The independent corroboration of the twin Marseilles houses and of Doc_01's Leyser-sourced Leo detail is real and correctly claimed.
- Gennadius ch. LXV on Vincentius: the Lérins presbyterate, the *Peregrinus* pseudonym, and *"the greater part of the second book of this work having been stolen, he composed a brief reproduction of the substance of the original work"* — verbatim, and correctly deployed as a **transmission** fact rather than a composition fact, which is precisely what S9 asked for.
- **Gennadius ch. XCV, the "Honoratus" trap.** Verified: *"Honoratus, bishop of Constantina in Africa wrote a letter to one Arcadius who on account of his confession of the catholic faith had been exiled to Africa by King Genseric."* Doc_02 §2's flagging of this false match — and Registry row 30's "do not conflate" note — is exactly right, well judged, and the kind of finding that only comes from actually opening the chapter. Round 1 itself had listed Honoratus among Gennadius's chapters on "this world's principals"; the revision caught the reviewer's error, checked it, and said so.
- The `npnf105` material: the "Massilians"/*reliquiæ Pelagianorum* footnote in full; both "two laymen" passages; the endnote *"It is, of course, not certain that this is the same Hilary that wrote to Augustin from Sicily, but it seems probable"*; the Index of Subjects listing exactly three Hilarys with no Arles and no Norbonne entry. All exact.
- The `npnf101` letter sequence: CCXX → CCXXVII, verified. The gap is real and rowing it is right.
- *Institutes* I, Chapter X: the dress-and-climate passage sits there, the quotation *"adapted to the humble character of our profession and the nature of the climate"* is verbatim, and the footnote *"This and the following chapter are altogether omitted in the edition of Gazæus"* is attached to that chapter.
- Sulpitius, *Doubtful Letters* II "Concerning Virginity": the quoted passage on consecrated virgins is verbatim, and §6's genre argument from it is sound.

**Judgments and disciplines that hold:**

- **S1 and S2 are model corrections.** Both are stated as withdrawals rather than quietly replaced; both replacement framings are attributed rather than asserted; the "three competing labels" finding is genuinely more useful to Doc_03 than the claim it replaces; and the Hilary-of-Sicily rival is carried as a rival, with Doc_01's own preference left standing on its own grounds.
- **The corpus-map fix is real and landed at the root.** I checked the staging file, the generated bucket, and the sibling buckets. This is the one place in this build's history where a "correction announced in one file" was actually propagated to the record it was about, and the commit message is honest about why the earlier one was not.
- **The Author Gravity Assessment for the apparatus (§2)** is substantive across all five dimensions and its Limitations paragraph draws the correct methodological moral. Its factual defect (N9) does not undo the assessment.
- **Registry rows 33–36** (Hilary of Poitiers, *Vita Antonii*, the rest of Augustine, the Rule of Benedict) are the right four comparanda, and row 35's reasoning — a Representative for a grace-and-effort world generating from a model saturated in Augustine — is the sharpest boundary thinking in either document.
- **Row 34's S15 correction** is exemplary: it converts an unsupported assertion into a properly two-sided open question, reserves it to the right instrument, and keeps the practical warning intact.
- **§10's element (c)** is genuinely well written and gives the downstream apparatus something usable, even though §13 fails to receive it.
- **The C11 disclosure** — naming a live inconsistency between the Framework's literal text and the Template's rule, applying one with a stated reason, and referring the conflict up rather than resolving it unilaterally — is exactly the right handling.
- **The honest-limitation posture survived the fix round**, which is not a given: §14's coverage limit, §7's "named as a real gap, not filled here," and §10's restated bounded-reconstruction limit are all cases where the revision could have papered over and did not.

---

## RECALL AND PRESS — CARRIED FORWARD FROM ROUND 1

Round 1's ten-item recall test is not re-run (it is a per-review instrument and re-running my own list against a revision I have already read would not be independent). Scored against Round 1's same ten, the revision closes **one** gap:

| Round 1 item | Now |
|---|---|
| Weaver 1996 | **Rowed** — row 23, existence and subject verified |
| Fontaine SC 133–135 | Still absent; named as an open item (§13.3) |
| Pricoco, *L'isola dei santi* | Still absent, unnamed |
| Stewart, *Cassian the Monk* | Still absent, unnamed |
| Rousseau, *Ascetics, Authority, and the Church* | Still absent, unnamed |
| Ramsey ACW *Conferences*/*Institutes* | Still absent; named as an open item |
| Van Dam | Still absent; named as an open item (§13.6) |

**Recall on Round 1's list would now be 4/10.** The three PRESS gaps are all dispositioned: PRESS-1 (Gennadius) rowed at 30 and read, though with the misattribution problems at N1; PRESS-2 (Letters 225/226 and the NPNF gap) rowed at 31 and correctly verified, though with the inference problem at N11; PRESS-3 (Weaver) rowed at 23. **All three PRESS items are genuinely closed as discoveries.** The Registry's Type axis still uses only P and S — **M** and **L** remain unused on all 41 rows, which Round 1 flagged as the shape of the recall miss and which no fix addressed.

---

## RECOMMENDED DISPOSITION

**SUBSTANTIAL REVISION REQUIRED — but a short and bounded one.** Unlike Round 1, this is not a document that needs re-argument. Six things have to happen, and none requires research beyond re-reading pages already open:

1. **Withdraw or re-ground the four Gennadius date claims (N1)** and everything built on them — specifically §1.3's *Documented* rating (N2), §1.1's "two independent ancient authorities" and §1.1's "two ancient sources in actual disagreement" (N3), and §1.4's "per Gennadius ch. LXX's own date." Declare `npnf203`'s Richardson apparatus as a third editorial layer and either fold it into Registry row 17's Author Gravity or give it its own.
2. **Withdraw §11's letters-gap inference and correct §10(b) (N11)** against `npnf101`'s own Prefatory Note, and re-describe Registry row 31 so it is not equated with row 11. Keep the row.
3. **Fix §3's "doubly evidenced" claim (N4)**, restore the truncated Faustus clause, and — if independent ancient attestation of the Lérins node is wanted — use Gennadius ch. LXV on Vincentius, which actually supplies it.
4. **Actually restrict the Boundary column to Native/Excluded (N6)**, moving "context," "pending intake," and "pending discovery" into Licensed For or the Verification Note.
5. **Reconcile the renumbering (N5)** — restore the original numbers and append *Dialogue I*, or declare the exception with a mapping table — and correct all twenty-five cross-references in both files.
6. **Close the small set**: N7 (*Contra Collatorem* attribution and grade), N8 (row 12's confidence arrow), N9 (the "anonymous" claim), N10 (Halm/Petschenig/Dionysius), N12 (rows 37–38 schema), N13–N16, plus the four still-open Round 1 items: **C9 (Sidonius)**, **S8's unlabelled "fl. 425"**, **S17's missing §13 Facilitator item**, and **S25's uncorrected G1 Part C claim**.

**A note on the pattern, offered as diagnosis.** This build's history now shows the same failure three rounds running, and it is not carelessness — the reading is careful and the quotation accuracy is high. It is that in each fix round the document, having correctly established that *a source it has in hand says something*, treats the nearest useful proposition as established. Round 1 named the counter-discipline: "state what the source says before stating what it supports." This revision quotes that sentence and then, four times in one section, states what an *editor's note* says and reports it as what the *source* says.

The concrete version of that discipline for the next pass is narrower and mechanical: **when quoting from a nineteenth-century translated volume, identify for every proposition whether it comes from the ancient text, the translator's introduction, or a bracketed editorial note — and write which, in the sentence.** Every N1–N4 error, and S1 and S3 before them, disappears under that one rule. Both of this build's vendored volumes make the distinction typographically obvious; the revision's own §2 Author Gravity Assessment argues for exactly this discipline in prose, one section before §1.1 fails to apply it.

The second, smaller pattern worth naming: **a fix asserted is not a fix applied** (N6, S25's G1 half, N15). Three of this build's findings across two documents are now of that exact shape. Whatever check catches it — a diff, a grep of the schema note against the column, a reviewer re-reading the claimed fix rather than the claim — should be run before the next disposition, not after it.

---

**Review completed:** 2026-09-08.
**Reviewer:** independent adversarial review, Round 2, cold — no drafting context, no involvement in Round 1.
**Verdict:** SUBSTANTIAL REVISION REQUIRED. Round 1: 18 FIXED / 9 PARTIAL / 1 NOT FIXED substantial; 8 FIXED / 1 FIXED-with-residue / 2 PARTIAL / 1 NOT FIXED cosmetic. New findings: 18 (N1–N18), 6 load-bearing. Recall on Round 1's list: 4/10 (was 3/10). PRESS: all three closed as discoveries.
