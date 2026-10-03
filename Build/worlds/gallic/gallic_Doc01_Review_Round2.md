# Doc_01 — Independent Review, Round 2

**Document reviewed:** `gallic_Doc01_World_Identification.md` (Gallic Monastic-Ascetic Christianity, Atlas I.27, era 2), status REVISED after Round 1.

**Reviewer:** independent adversarial pass, Round 2. No drafting context, no Round 1 context beyond the Round 1 file itself. The revision's own claims about what it fixed were treated as unverified assertions and checked against the files, not accepted.

**Checked against:** `gallic_Doc01_Review_Round1.md` (all 18 substantial + 12 cosmetic findings + the "WHAT HELD UP" list); `gallic_G1_Scope_and_Source_Acquisition_Manifest.md` (as revised, including commit `13d9a64`); `CASE-gallic-monasticism.md`; `cic-website/data/world-census.json` (read directly from JSON, all five neighbour entries); `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (every quoted passage located and read in the file — Institutes Preface, Conferences part-dedication note, Postumianus Dial. I.1/I.3, Commonitory-introduction note, Conference XII/XXII omission markers, Institutes II.11 psalmody note, the Ligugé/Marmoutier/Lérins founding paragraph); `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part I (extracted and read directly, lines 85–135 of the extracted text); `CAPPADOCIAN_BUILD_LEDGER.md` §§5, 7, 11 for the fix-round-introduces-new-errors precedent; and independent live verification of the archive.org CSEL 21 item and the Faustus/Lucidus synod dating.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**But narrowly, and not in Round 1's sense.** This is a genuinely good revision. Round 1's diagnosis was right, the reviser acted on it, and the central failure — reasoning about the vendored file instead of reading it — has been substantially reversed. Every quotation newly introduced from `npnf211` was located in the file and, with one exception noted below, is verbatim and accurately used. **14 of 18 substantial findings are cleanly fixed, 4 partially, 0 unfixed; 11 of 12 cosmetic fixed, 1 unfixed.** Nothing in Round 1's "WHAT HELD UP" list was disturbed or contradicted.

The verdict is nonetheless SUBSTANTIAL, for four reasons that are individually small and collectively exactly the Cappadocian pattern (ledger §§7, 11: "the round that was fixing errors the previous round had found" introduces new ones):

1. **A new factual error about the primary source was introduced inside the flagship fix.** The sentence that carries the S5 correction misattributes to *Conferences* XI–XVII a dating clause the vendored file applies to *Conferences* I–X (N3). The one sentence the revision most wants credit for reading directly is the one that misreads.
2. **The document's own temporal ceiling is now stated three incompatible ways inside one subsection and is never resolved** (N4). Temporal Scope is a Part I core output. The revision loosened the ceiling correctly and then left it loose in three places at once, while G1 still carries the old c. 450.
3. **S12's correction exists nowhere in the document.** The wrong claim was deleted rather than corrected, and two separate sections now point the reader to an Institutes Preface passage "quoted in §2.3" that is not in §2.3 or anywhere else (N1, N2).
4. **The companion G1, revised in the same pass, now contradicts itself and Doc_01 on two points**, one of which is the *very identification* S6 corrected — retained verbatim two hundred words after the correction was applied (N6).

None of this requires a rewrite. It requires one narrow, mechanical fix round of the kind the Cappadocian ledger describes converging: locate, correct, re-check. The substantive historical and methodological work is sound.

---

## PART 1 — SUBSTANTIAL FINDINGS S1–S18

| # | Status | Notes |
|---|---|---|
| **S1** — §2.1/§5 silently resolve the one-world-or-two question | **FIXED** | §2.1 now gives two explicit conditional floors (c. 360 if one world; c. 400–410 for the southern node if a lineage of two) and states plainly why it proceeds on c. 360 (single Atlas entry, no Doc_01 authority to split). §5's entry question is answered in the same conditional form, both readings named. This is Round 1's fix (a), executed properly. |
| **S2** — §1's "people moving between them" at [Documented], contradicted by §2.3 | **FIXED** | The bracket is gone entirely. §1 bullet 1 is retitled "evidenced for one node, hypothesised for the whole," restricts the evidenced claim to Lérins–Marseilles, and explicitly names the Tours link as "this world's own working hypothesis, not yet evidence." Circular sourcing (a G0 record grounding a *Documented* rating) removed. |
| **S3** — §6's word-count figure is arithmetically wrong for its use | **PARTIALLY FIXED** | **Arithmetic independently re-verified and correct.** Case table sums: 364,648 + 228,578 + 109,539 + 28,254 = 731,019 ✓. 731,019 − 228,578 = **502,441** ✓. 731,019 − 364,648 = 366,371 ✓ (Round 1's diagnosis confirmed: case §4 subtracted Cassian, not Hilary). G1's new total: 502,441 + 95,295 = **597,736** ✓, header rounds to ≈597,700 ✓. Three things remain wrong. **(a)** The corrected arithmetic appears *nowhere in Doc_01* — only the bare number "502,441" in §6, pointing to "§12 below," where §12 mentions that the correction was made but never states it. The header sends the reader to §6; §6 sends them to §12; §12 has nothing. **(b)** Round 1's fix said the word-count "is in any case not evidence that two nodes belong to one formation world" and to find a different argument. §6 still lists the corrected figure as one of three items under "For treating this as one world." The figure is now right and the inference is still invalid. **(c)** The census `why` field still reads "roughly 366,000 words" — Round 1 named this explicitly as propagation. Neither Doc_01 nor G1 corrects or discloses it. See N11. |
| **S4** — Postumianus's Dialogues do not attest Lérins/Marseilles | **FIXED** | Verified in the file myself: Dial. I.1 "Landing on the thirtieth day at Marseilles, I came on from that and arrived here" (line 2568); Dial. I.3 "after setting sail from Narbonne, on the fifth day we entered a port of Africa" (line 2655). "Lérins" does not occur in the Dialogues. §2.3 now states the correction openly, names the first draft's error, and draws the right conclusion. Well done; this is the strongest single fix in the revision. |
| **S5** — the Lérins–Marseilles link is never evidenced, and the evidence is in the vendored file | **FIXED (with a new error inside the fix — see N3)** | The Conferences XI–XVII dedication note is quoted in §2.3 and verified verbatim against lines 15545–15552. §1, §4, §6 and §11 all now rest the southern pair on it. The substance is right. The framing sentence around it introduces a new misstatement (N3) and truncates the quotation at a non-sentence-end inside quotation marks (N9). |
| **S6** — "Prosper and Hilary of Arles" contested, contradicted by the vendored source | **PARTIALLY FIXED** | The label is corrected: §10 now carries it as **Contested**, names the Commonitory-introduction contradiction (verified at lines 11784–11795), and notes the lay-monk identification is the weight of opinion. §11 item 2 carries it as a real open item. G1 gal-src-11 corrected. **What was not done is what Round 1 explicitly asked for:** "Re-examine §7's and §8.2's 'two-way argument' framing on that basis." §8.2 is untouched — it still says this world "produced treatises addressed to, and answered by, Augustine of Hippo by name," which is the framing S6 said is materially changed if the correspondents were pro-Augustinian reporters. Worse, **§4 actively re-asserts the corrected error**: "This world's monks were in direct, functioning correspondence with … Augustine; and, per Prosper's and his correspondent's 431 journey, Pope Celestine I." If the correspondent's identity is Contested and Prosper is on the other side, they are not "this world's monks," and §4 says they are. The correction is recorded in §10 and contradicted in §4. |
| **S7** — Cassian/Augustine relative chronology treated as settled | **FIXED** | §7 now carries it as **Contested**, names Chadwick's redating and Casiday against it (bibliographic details — *Tradition and Theology in St John Cassian*, OUP 2007 — correct), uses the vendored file's own "not later than 426" window accurately, and rewrites "what it was refusing" so it no longer depends on Conference XIII answering a text it may predate. §10's bare "which precedes rather than answers" is gone. Clean. |
| **S8** — c. 450 argued without Faustus; Mathisen used backwards | **PARTIALLY FIXED** | Faustus is now engaged at length (§2.4, §2.6, §5, §6, §10, §11) and the counter-argument is *made* rather than skipped — the register-change reasoning (formation-community literature → synodal commission) is genuinely good. The Mathisen inversion is corrected explicitly and correctly. But the fix leaves the boundary unresolved in three incompatible forms (N4), and the synod date is asserted flat, unlabelled, on a date the literature does not settle, and conflicts with G1's own figure (N7). |
| **S9** — the "undocumented thirty-year gap" | **FIXED** | §2.5 restates it as a housekeeping gap between two census entries' proposed date ranges, names Faustus, the 475 synods and Sidonius as its actual contents, and engages both census continuity claims. I verified both quotations against the JSON: "the seedbed of the Merovingian Gallic church that follows it" ✓ and "Receives Martin of Tours's line" ✓. §8.5 updated to match. It is no longer the document's headline open item. |
| **S10** — project coinage attributed to "the secondary literature" | **FIXED** | §1 now says "the case document's own phrase … its own coinage," and names the misattribution as corrected. §4's already-correct attribution is unchanged. The internal contradiction is gone. |
| **S11** — two Institutes "quotations" that are not quotations | **FIXED** | Both bogus strings are gone from the document (grep-confirmed). §1 now quotes "by the customs of the monasteries which are found throughout Pontus and Mesopotamia," verified verbatim at line 16532, and carries the Pontus/Mesopotamia detail Round 1 said was the more interesting fact. The pointer attached to it is broken (N1/N2), but the quotation itself is correct. |
| **S12** — "dedicated broadly to Gallic monasteries" contradicted by the primary text | **PARTIALLY FIXED** | The false claim is removed from §2.3 and §3 (grep-confirmed: "Castor" and "Apta" appear nowhere except in the unrelated §2.3 dedication sentence). But **it was deleted, not corrected**: Castor of Apta Julia is never named, the Preface's "your province, which is at present without monasteries" (verified line 16437) never appears, and the substitution mechanism Round 1 said was worth carrying to Doc_02 is only half-carried. §4 says obliquely "the *Institutes* is addressed to one named bishop" — without naming him. Two sections then point at a Preface passage "quoted in §2.3" that does not exist (N2). Round 1's instruction was "Correct §2.3 and §3"; the revision removed §3's claim without supplying the correction, and the document is now *less* informative about its own principal source than the finding intended. |
| **S13** — five unsupported confidence labels | **FIXED (all five)** | (a) §2.2 Hilary/Ligugé now **Widely Accepted** with the Sulpicius-single-source reasoning stated ✓. (b) §2.1's rating basis is now the vendored NPNF introduction, verified verbatim at line 15446: "Ligugé was founded shortly after 360, and Marmoutier rather later, after 371" ✓ — abbey-website/encyclopedia basis gone. (c) "c. 425" for Vincent's entry now **Inferential/Thin**, with the reasoning given ✓. (d) The §1 [Documented] bracket removed with S2 ✓. (e) Vincent–Lupus now **Inferential/Thin**, not Contested, with the right justification ✓. All five labels are drawn from the fixed Article 17 vocabulary, which I confirmed against V7.4's Confidence Calibration section (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin). |
| **S14** — Strand Determination output not delivered | **FIXED** | §6 records **provisionally strand-singular**, quotes the Framework's own default sentence accurately ("a world without established strands is treated as strand-singular throughout all subsequent steps" — verified against V7.4 Part I), and states the operative status for downstream work. This is exactly Round 1's recommended fix and it satisfies the Framework's Output line. One methodological caveat at N12 — it does not change the status. |
| **S15** — §5 answers two of six World Separation questions | **FIXED** | All six V7.4 Part I questions are now present and answered substantively, in the Framework's own order (new gravity / major gravity disappeared / formation / worship / authority / interpretation) — I checked this against the extracted V7.4 text directly. The worship answer is the strongest addition and is properly grounded: the Institutes II.11 note, verified at lines 17479–17482, reads "the rule that prayers should be intermingled with Psalms which was perhaps introduced into the West by Cassian, was widely adopted both in Gaul and in Spain." (One hedge dropped — see N10.) |
| **S16** — all three Augustine treatises called "Augustine's replies" | **FIXED** | §10 now says explicitly that only *De praedestinatione sanctorum* and *De dono perseverantiae* are addressed to Gaul, that *On Rebuke and Grace* is Hadrumetum-addressed and carried `provisional`, and that "the two-treatise figure, not the three-treatise 95,295-word total, is what should be called 'Augustine's replies to Gaul' downstream." Consistent with G1 Part C and with §3. |
| **S17** — the Conference XII/XXII edition gap | **FIXED** | Verified independently in the file: Conference XII "Not translated" (line 37471) and Conference XXII "This Conference is omitted" (line 46045) — G1's cited line ranges 37466–37475 and 46037–46045 both contain their target ✓. §4 carries it, §10 cross-references it, §11 item 4 keeps it distinct from the women's-presence question, and G1 gal-src-01's "all 24 conferences in scope" is corrected. §4's handling — insisting the evidential-visibility gap and the ecological-visibility gap "should not be allowed to blur into one another" — is better than the finding asked for. |
| **S18** — "Massilian" as self-designation | **FIXED** | §7 now states it is Prosper's label for the group he was reporting on, not a self-designation, and adds the Marseilles-specific-reach limitation Round 1 flagged for §6. Substantively correct. One over-claim about *what the vendored file says* — N10. |

**Substantial tally: 14 FIXED · 4 PARTIALLY FIXED (S3, S6, S8, S12) · 0 NOT FIXED.**

---

## PART 2 — COSMETIC FINDINGS C1–C12

| # | Status | Notes |
|---|---|---|
| C1 | **FIXED** | "an strong" → "a strong" (grep-confirmed: no occurrence remains). |
| C2 | **FIXED** | §7 now distinguishes Beza's c. 1556 coinage (for contemporary Roman Catholic teaching) from Sanders's 1571 retrospective application, exactly per Backus & Goudriaan. |
| C3 | **FIXED (by deletion)** | The unattributable "inappropriate, ambiguous and unjust" quotation is gone. |
| C4 | **FIXED** | Saint-Sauveur named in §2.3, §3, §4 and §11 item 4; Saint-Victor correctly identified as the men's house. |
| C5 | **FIXED** | §3 now gives ~600 km straight-line, "materially more by any actual route," and names the first draft's error. Direction of the inequality is now right. |
| C6 | **FIXED (moot)** | *Contra Collatorem* no longer appears in the document at all. |
| C7 | **FIXED** | §10 now runs Cassian's Roman connection through Leo, "archdeacon under Pope Celestine I, who commissioned *De Incarnatione* (429/430)," and names the misattribution as corrected. |
| C8 | **FIXED** | §8.3 now quotes the census `why` in full: "…in a Rule that later Western monasticism kept returning to." Verified verbatim against the JSON. |
| C9 | **FIXED** | §10 now reads "*Conferences* I–XXIV" with the three-published-parts explanation, plus the 22-of-24 cross-reference. |
| C10 | **FIXED** | §8.3 now cites RB 73's full "the Conferences of the Fathers, their Institutes and their Lives" and adds RB 42's daily-reading prescription. G1 gal-src-02 carries the same correction. |
| **C11** | **NOT FIXED** | §5 still reads: "a formation practice — replicable ascetic community, **not a bishop's individual household** — distinct from Hilary's own creedal-episcopal world." This is verbatim the construction Round 1 flagged: the referent is undefined, it sits adjacent to Hilary of Poitiers and reads as a contrast against him, there is no evidence Hilary kept such a household, and the case document uses "a bishop's ascetic household at Tours" of **Martin's own foundation** — so as written the sentence contrasts Ligugé against a description of Ligugé. §2.1 independently supplies a better framing ("ascetic withdrawal organized as a replicable community, not removed from episcopal life"), which makes §5's retention of the old phrasing look like an oversight rather than a decision. |
| C12 | **FIXED** | The disclosure is in the header's "Governed by" line, names V7.4's own DRAFT status block accurately, and identifies this as the seventh world freezing against an unratified governing document. Better placed than Round 1 suggested. |

**Cosmetic tally: 11 FIXED · 1 NOT FIXED (C11).**

---

## PART 3 — NEW FINDINGS (Round 2)

### N1. Six broken §-cross-references, four of them pointing at the very fixes they cite as evidence — SUBSTANTIAL

The revision added §2.6 and rewrote §2.5, shifting the subsection contents. Six pointers were not updated, and four of them are attached to Round 1 fixes, so a reader following the document's own audit trail is sent to the wrong place precisely where the document is asking to be checked:

| Location | Points to | What is actually there |
|---|---|---|
| §1, "quoted exactly, Round 1 finding S11 corrected — **see §2.3** for the fuller passage" | §2.3 | No Institutes Preface material at all. §2.3 is Lérins/Marseilles dates, the Conferences dedication, and Postumianus. |
| §2.1, "**see §9** on why this is not rated *Documented*" | §9 | §9 is "Disclosure obligations carried from G0" — nothing about confidence ratings. The reasoning is in §2.2's own bracket and (partly) §10. |
| §2.4, Faustus named in the Commonitory introduction "(**§2.5, §7** below)" | §2.5, §7 | Neither mentions the Commonitory introduction. The passage is quoted in **§4**. |
| §4, "only the correspondent's identity is in question, **§7**" | §7 | §7 does not discuss the Hilary identification. It is in **§10**. |
| §10, "The identity of Augustine's correspondent 'Hilary' (**§2.3, §6, §7**)" | §2.3, §6, §7 | None of the three mentions the correspondent's identity. |
| §11 item 2, "(**§2.3, §7, §10**)" | §2.3, §7 | Same; only §10 is right. |
| §5, "the *Institutes*, explicitly designed to be portable to 'a new establishment in the West,' **per the Preface quoted in §2.3**" | §2.3 | Again, no Preface quotation there. (The quoted phrase itself is verbatim-correct, line 16522.) |
| §6/§12, the arithmetic correction "(**§12 below**)" / "(§6, **§12**)" | §12 | §12 says the correction was made and propagated; it never states the arithmetic. §12 also cites itself. |

**Why it matters.** Round 1's central complaint was reasoning about sources rather than reading them. This revision reads the sources and then mis-files where it put what it read. A Doc_02 builder following §10's Hilary pointer to "§2.3, §6, §7" will find nothing, conclude the item was dropped, and lose a Contested flag the document worked hard to establish. **Fix:** repoint all eight, mechanically.

### N2. The S12 correction exists nowhere in the document, and two sections cite it as if it does — SUBSTANTIAL

Combining the §1 and §5 pointers above: the document twice tells the reader that the Institutes Preface is quoted in §2.3, and §12 states as part of its evidence of diligence that "the relevant passages (**Institutes Preface**, Conferences XI–XVII dedication note, Postumianus's itinerary, the Commonitory introduction's Honoratus/Hilary/Faustus sentence, the Conference XII/XXII omission notes) were located and read in the source file." Four of those five are demonstrably in the document and verbatim. The Institutes Preface is represented by exactly one clause in §1 and one four-word phrase in §5, and the correction S12 called for — Castor, Apta Julia, "your province, which is at present without monasteries" — is not in the document at all.

This matters beyond housekeeping because S12's whole point was that the corrected fact is *more* useful than the error: one named bishop, one province in the far Mediterranean south, expressly monastery-less, saying nothing about the Loire. That is direct support for §2.3's honest finding about the missing Tours link, and the revision deleted rather than deployed it. **Fix:** state the corrected dedication in §2.3 (or §3) with the Preface's own words, and repoint §1 and §5 to it.

**Worth recording as a partial defence of the first draft, and a caution for Doc_02:** the Preface *does* contain "I do not believe that a new establishment in the West, **in the parts of Gaul** could find anything more reasonable or more perfect than are those customs" (line 16522). Round 1's S12 is still right that "dedicated broadly to Gallic monasteries" misstates the dedication — the addressee is one bishop — but the Preface's own horizon is not purely Apta Julia either. The revision, having excised the passage entirely, has left the document with no way to see this nuance. It should be carried, at the right strength, rather than swung from one flat claim to the opposite silence.

### N3. A new factual error about the vendored source, inside the sentence carrying the flagship S5 fix — SUBSTANTIAL

§2.3: "Cassian's second set of *Conferences* (XI–XVII) — **completed shortly after Castor's death in 426** — 'is dedicated to Honoratus and Eucherius…'"

The vendored file (lines 15540–15552) says the opposite of what that clause implies. Reading it in order:

> "He therefore dedicated Conferences I.–X. (the first portion of the work) to Leontius … **This portion** of Cassian's work must have been completed shortly after the death of Castor in 426. It was speedily followed by Part II., containing Conferences XI. to XVII. This is dedicated to Honoratus and Eucherius…"

"Completed shortly after Castor's death in 426" is the file's statement about **Conferences I–X**, not XI–XVII. The file's own dating of XI–XVII is the *opposite* direction — "must have been published **not later than** that year," i.e. on or before 426 — which is precisely the fact §7 relies on for the Contested Conference XIII chronology. So the revision states, in the same document, that XI–XVII was completed after 426 (§2.3) and not later than 426 (§7). §7 has it right.

This is exactly the Cappadocian pattern (ledger §7: "the rewrite itself had introduced new errors"), and it is in the one sentence the revision most prominently offers as proof that it read the file. **Fix:** delete the clause, or reassign it to Conferences I–X.

### N4. The temporal ceiling is now stated three incompatible ways, and Doc_01 no longer states a working window — SUBSTANTIAL

Round 1's S8 asked the document to argue the boundary rather than skip it. It now argues it — and arrives at three different answers, two of them in the same subsection:

- §2.4 heading: "**Ending point: c. 450** argued against its strongest counter-evidence"
- §2.4 body: "the c. 450 date is itself approximate and the real marker is closer to the **mid-450s to 460s**, when Faustus's own role shifts from monk-abbot to bishop"
- §2.4 closing: "What actually changes in kind, per the Faustus reasoning above, is closer to the **460s–470s**"
- and the register-change argument the section actually makes locates the change at the **475** synodal commission, later still

Meanwhile §2.5 computes its interval from a c. 450 close ("the 450–480 interval"), §2.6 and §8.5 assume the same, §5's exit reasoning is gone entirely, and **G1 still states the window as c. 360–450** in its title line and Part A. So the two documents revised in the same pass now disagree about the world's own dates, and Doc_01 disagrees with itself.

The §2.1 floor was handled correctly — two conditional floors, an explicit statement of which one the document proceeds on, and why. The ceiling got the loosening without the resolution. Temporal Scope is a named Part I output; a document may honestly say a boundary is imprecise, but it has to say which figure downstream work uses. **Fix:** state one working ceiling with its imprecision named (the natural candidate is "c. 450, with the real change in kind falling in the 460s–470s"), make §2.4's three formulations agree, and update G1 or state explicitly that G1's c. 360–450 stands as the working window.

### N5. The archive.org title is misquoted — SUBSTANTIAL (source-attribution discipline)

§2.4 and §10 present, in italics as an edition title: "*Fausti Reiensis et Ruricii Opera*, ed. August Engelbrecht, CSEL vol. 21, Vienna: F. Tempsky, 1891; confirmed `NOT_IN_COPYRIGHT (US)`."

Verified independently against `archive.org/metadata/corpusscriptorum21fausuoft`:

- Title: **"Fausti Reiensis Praeter sermones pseudo-eusebianos opera : accedunt Rurieii epistulae"** — not "Fausti Reiensis et Ruricii Opera"
- Creator/editor: Faustus, Bishop of Riez, 5th cent; **Engelbrecht, August, 1861–1925**; Ruricius I ✓
- Date **1891** ✓ · Publisher **Vindobonae: F. Tempsky** ✓ · Volume **21** ✓ · Copyright status **NOT_IN_COPYRIGHT** ✓
- Contents independently confirmed to include **De gratia libri duo** (with De spiritu sancto libri duo, Epistulae, Sermones; Ruricius: Epistularum libri duo) ✓

So the *substance* of the claim is verified and the lead is real and usable — this is a genuine, well-executed piece of new work, and I want to credit it. But the title as rendered is wrong on two counts: it drops "Praeter sermones pseudo-eusebianos" (which defines what the volume *excludes*, and so what a vendoring pass would and would not get), and "et Ruricii Opera" misstates the Ruricius content, which is *epistulae* only. Doc_01 also reports the ToC string as "FAVSTI DE GRATIA LIBRI II"; the catalogued form is "De gratia libri duo," and archive.org's full-text search endpoint did not return the claimed string on my check — the content is confirmed by other means, the exact string is not. In a document whose two most serious Round 1 findings (S11, S12) were both quotation-accuracy failures, an invented edition title inside italics is not a nit. **Fix:** use the item's actual title, or drop the italic title and cite the item id plus editor/series/year, which are all correct.

### N6. G1, revised in the same pass, now contradicts itself and Doc_01 — SUBSTANTIAL

Three defects in the companion document, all introduced or left by this revision pass:

**(a) G1 Part C item 3 still carries the exact identification S6 corrected.** Line 132: "only the latter two are actually addressed to **Prosper and Hilary of Arles** (`assigned`)." Two hundred words earlier, the same file's gal-src-11 row records the correction: "**corrected 2026-09-08 (Doc_01 review finding S6): this Hilary's identity is Contested, not Hilary of Arles.**" The file both applies and contradicts the same finding. This is the single clearest instance in this pass of a fix landing in one place and being missed in another.

**(b) Three incompatible dispositions of Faustus across the two files.** G1's "Honest gaps, not pursued now" paragraph (lines 79–87) says *De Gratia* is "a genuine double reason not to chase it now" and worth "a PRESS-style discovery check at B-1b." G1's newly added leads table (lines 92–109, commit `13d9a64`) lists it as "ready for Doc_02's own intake pass." Doc_01 §2.4, §10 and §11 item 3 call it "the immediate next G1 action rather than a someday item" and "the concrete next G1 action." The reader cannot tell what the build actually intends to do, or when.

**(c) Two dates for the same text.** G1 twice says *De Gratia* was written **474**; Doc_01 says **c. 475**. See N7.

**Fix:** correct Part C item 3; reconcile the Faustus disposition to one statement; align the date.

### N7. The 475 synod date is asserted flat, unlabelled, on a date the literature does not settle — SUBSTANTIAL

§2.4: "He wrote ***De Gratia*** (two books) **c. 475**, at the express request of the synods of **Arles and Lyons (475)**, against the predestinarian presbyter Lucidus."

Independent checking finds the dating genuinely unsettled: the Catholic Encyclopedia gives Arles and Lyons **475**; other accounts give **Arles 473, Lyons 474**; scholarly summaries give the councils an uncertain range of **c. 470–474**. This world's own G1 says **474**. The revision presents a bare parenthetical "(475)" with no confidence label, on a date that is Contested-to-Widely-Accepted at best — in a document that has just spent §2.3 and §10 correcting five confidence labels for exactly this failure.

**The mechanism is worth naming, because it is the one this review round exists to catch:** "c. 475 … synods of Arles and Lyons (475)" is Round 1's own phrasing, reproduced. The revision's §12 claims every checkable fact was "independently re-verified … not merely corrected on the reviewer's word." For this fact, it was corrected on the reviewer's word, and the reviewer's date is the one the reviser's own G1 disagrees with. **Fix:** carry the synod dating as "c. 473–475" with an appropriate label, or state the range and the disagreement.

### N8. Over-claims about what the vendored source says — MODERATE

Two places where the file supports less than the document says it does. Both are mild in substance and both are the same species of error Round 1 found in the first draft, which is why they are worth recording rather than waving through.

- **§7 (Massilian).** "**This document's own vendored source supplies the period-contemporary alternative, and states plainly whose word it is** … 'Massilian' (*Massilienses*) is **Prosper of Aquitaine's own label**." The file (lines 14780–14830) does not state this. Its editor narrates Prosper's letter using his own phrase "the Massilian clergy," and elsewhere (line 14901) writes "the Massilians, **as Prosper represents them**." *Massilienses* does not occur in the file at all. The conclusion is historically correct — Prosper does use the term — but the file is a nineteenth-century editor's narration, not the source "stating plainly whose word it is." Restate as independently established and corroborated by the file's usage, not as the file's own testimony.
- **§5 (worship).** The document says the apparatus "traces the practice of interspersing psalms with set prayers **as a specific Egyptian-to-Gallic (and Spanish) transmission**." The note (line 17479) reads: "the rule that prayers should be intermingled with Psalms **which was perhaps introduced into the West by Cassian**, was widely adopted both in Gaul and in Spain." The hedge is the editor's and should survive into a document that is otherwise scrupulous about hedges.

### N9. C8's defect re-introduced in a new quotation — COSMETIC

§2.3's Conferences dedication quotation ends "…the volume must have been published not later than that year." with a closing period inside the quotation marks. The source sentence continues: "…not later than that year, **or he would have been termed 'Episcopus,' as he is in the Preface to Conference XVIII., instead of 'frater.'**" This is precisely C8 (truncation inside quotation marks at a point that reads as a sentence end), which the revision fixed for the census `why` field and re-committed in the same pass. The omitted clause is also the *reasoning* for the dating, so it is worth keeping. Add an ellipsis or the full sentence.

### N10. The census `why` field's inherited error is left uncorrected and undisclosed — MODERATE

Round 1's S3 listed the propagation explicitly: "The census entry's own `why` field also says 'roughly 366,000 words.'" I confirmed it is still there verbatim in `cic-website/data/world-census.json`. Under the corrected arithmetic, 366,371 is the with-Cassian-removed figure, so the census is describing this world's material with a number that excludes its largest author. G1 discloses the case-document error and Doc_01 references it; neither mentions the census. Given the project's provenance discipline (Doc_01 §12 correctly declines to edit the G0 record and discloses instead), the right move is the same one: disclose it. It is currently the only unflagged live instance of the error.

### N11. "Provisionally strand-singular" satisfies the Framework's output but strains its authority model — MINOR / METHODOLOGICAL

§6's finding is the right one and matches Round 1's recommended fix. Two frictions with V7.4 Part I as actually written, worth a sentence rather than a rewrite:

- The Framework says the strand determination "**is made at Step 1 and governs all subsequent work**" and that "strand attribution applies only where Step 1 established strands." §6 says the default is "a placeholder for a genuinely live question, **not a finding this document has actually made**," and assigns revision authority to Doc_04. The Framework gives Step 4 cross-strand *gravity testing*, not the power to revise a Step 1 strand finding. The practical outcome is the same and the honesty is better than silence; the sentence disclaiming the finding should be softened so it does not read as declining the output it just delivered.
- §6 and §2.1 route the one-world-or-two question to **Doc_04**. The case document calls it "a **Step 0** question this document cannot settle" (case §5), and V7.4 places world separation at Step 1. Neither Doc_01 nor Doc_04 is Step 0. Doc_01 is right that it lacks authority to split a single Atlas entry; it should say the question needs a Step 0/Atlas act rather than implying Doc_04 will settle it.

### N12. §10's "eleven of eighteen" over-reads Round 1's own note — MINOR

§10's standing confidence note asserts: "**Eleven** of this document's first draft's eighteen substantial errors were resolvable directly from `npnf211…xml`." Round 1's closing note says eleven findings "share one cause" (reasoning about sources rather than reading them) and then names **eight** as resolvable from the XML (S12, S11, S4, S5, S6, S7, S8, S17), with S3 resolvable from the case document. The revision converts "share one cause" into "resolvable directly from the XML" and keeps the number. It is a self-critical over-claim rather than a self-flattering one, but it is still a claim accepted from the reviewer without checking — the exact discipline §12 says was applied.

---

## PART 4 — WHAT HELD UP, AND WHAT IS NOW GENUINELY SOLID

**Round 1's "WHAT HELD UP UNDER SCRUTINY" list: nothing was disturbed, weakened or contradicted.** I checked each item against the revision:

- Beza c. 1556 ✓ retained and now correctly distinguished from Sanders 1571.
- *Commonitory* 434 at **Documented**, internally dated three years after Ephesus ✓ retained, and §2.3 now says explicitly why this is the one place the label is fully earned.
- Vincent's death "before 450" ✓ retained with the Gennadius reasoning.
- Ligugé c. 360, Marmoutier after 371, Martin d. 397 ✓ retained; the vendored-source corroboration is now quoted rather than paraphrased.
- Martin's ordination as exorcist under Hilary ✓ retained; only the rating changed, as S13a asked.
- Honoratus/Lérins 410, and the refusal to narrow the c. 400–410 range ✓ retained and now doing more work (it supplies the conditional southern floor).
- Cassian at Marseilles c. 415, two houses ✓ retained, now with both names.
- Prosper's and his correspondent's 431 journey to Celestine ✓ retained; the journey is kept, only the identity flagged — the precise distinction Round 1 asked for.
- *De correptione et gratia* → Hadrumetum ✓ retained in §3 and §10, and now strengthened by S16's correction.
- Stancliffe / Leyser / Mathisen / Chadwick bibliographic details ✓ all retained accurately; Casiday added and correct.
- Mathisen's thesis ✓ retained and now used in the right direction.
- Atlas identifiers and all census quotations ✓ re-verified by me against the JSON; all verbatim.
- Priscillianism §8.4 ✓ retained intact.
- §4 Missing Voices ✓ retained and materially strengthened by S17.
- §7 Forces ✓ retained; the "geographically modest withdrawal" observation Round 1 called load-bearing is intact and unweakened.
- §9 Disclosure obligations ✓ retained verbatim in substance.
- World Separation Criteria present ✓ — and now complete.
- The Hilary of Poitiers exclusion ✓ handled as well as before.

**What is now genuinely solid, beyond Round 1's list:**

- **The Lérins–Marseilles evidentiary base.** §2.3 is now the document's best section: a documented positive link (the XI–XVII dedication), a stress-tested negative (no Tours link), and a correction of the first draft's misused Postumianus evidence, all resting on passages I located and read myself. The asymmetry Round 1 objected to — one link tested, the other assumed — is gone.
- **The conditional-floor construction (§2.1 + §5).** This is a better answer than either of Round 1's two suggested fixes. It keeps the scope question genuinely open, records which figure downstream work uses and why, and makes §5's entry answer honest without pretending the world has two floors in operation.
- **The complete §5.** All six questions, none perfunctory, and the worship answer in particular is grounded in a specific note in the vendored file rather than asserted. It is now materially stronger than the comparison world's own §5.
- **The Faustus engagement.** The register-change argument (formation-community literature → synodal commission) is a real argument, honestly held apart from the argument's *content*, and it gives Doc_02 and Doc_08 something usable. The dating slippage (N4, N7) is a defect in its bookkeeping, not in its reasoning.
- **§4's two-kinds-of-absence distinction.** Separating the edition-level suppression of Conferences XII and XXII from the ecological question about women's presence — and refusing to let them blur — is better work than S17 asked for and is the right implementation of Article 20's evidential-vs-ecological-visibility distinction.
- **The disclosure posture throughout.** C12's unratified-Framework disclosure, the refusal to edit the G0 record while flagging its error, and §12's escalation check are all handled well and in the project's own idiom.

---

## Reviewer's note on the shape of this round

Round 1 found a document that reasoned about its sources. Round 2 finds a document that read them and then mis-shelved what it read. Of the seven substantial new findings, **five are bookkeeping failures attached to correct substance** (N1, N2, N4, N6, N9) and **two are accuracy failures inside newly added material** (N3, N5, with N7 a third if the synod date is counted as new). Not one is a reasoning error, and not one requires reopening a judgment the revision made.

That is the convergence shape the Cappadocian ledger describes (§11: "each round's findings were smaller and more mechanical than the last"), and it should be read as such — but the ledger's other lesson applies with equal force: this is the third document in this fleet's recorded history where a correction pass aimed at citation accuracy has itself introduced citation-accuracy errors (an invented edition title, a misattributed dating clause, a truncated quotation, and eight pointers to material that isn't where they say it is). The discipline that catches it is the one being applied here: check the file, not the claim that the file was fixed.

**Recommended disposition:** one narrow, targeted fix round addressing N1–N7 and C11, plus the four partial items (S3's argument and census disclosure, S6's §4/§8.2 downstream re-examination, S8/N4's ceiling, S12's missing correction), followed by a bounded spot-check of only that round's changes. A full third adversarial pass is not warranted; the substantive ground is settled.

---

**Review complete. Verdict: SUBSTANTIAL REVISION REQUIRED (narrow scope). Substantial: 14 FIXED, 4 PARTIAL, 0 NOT FIXED. Cosmetic: 11 FIXED, 1 NOT FIXED. New findings: 12 (N1–N7 substantial, N8/N10 moderate, N9/N11/N12 minor).**
