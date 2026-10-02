# Doc_02 (Source Ecology) / Source Registry / Source Acquisition Manifest — Round 2 Adversarial Review (Targeted Recheck)

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Reviewed at commit:** `4fd3579b` ("Revise Doc_02 per Round 1 review: fix fabricated citation, more"), branch `reformed-cities-doc01` (checked out elsewhere; reviewed from a content-identical local branch `review-doc02-round2` at the same commit, confirmed via `git rev-parse`)
**Documents reviewed:**
- `World-Builds/Reformed-Zurich-and-Geneva/Doc_02_Source_Ecology.md` (DRAFT, Revision 2)
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Registry.md`
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Acquisition_Manifest.md`
**Prior round:** `Review-Artifacts/Doc02_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED (4 high, 4 medium, 3 low), reviewed at `3d624182`.
**Reviewer stance:** cold adversarial review, no drafting context. Per `cic-build-cycle` and this project's cost discipline, this is a **targeted recheck** of Round 1's findings and a hunt for fix-introduced defects — not a full re-review from scratch. Every claim below was independently re-verified against primary material (the actual census JSON, the actual vendored text files, the actual Doc_01 text, the actual Template and Framework/Constitution documents) rather than trusted from Revision 2's own masthead account of what it fixed.

---

## Verdict: SUBSTANTIAL REVISION REQUIRED (narrow scope)

Three of Round 1's four High findings, and all of its Medium/Low findings, are genuinely and independently confirmed fixed. The fourth (H4, "documented" misuse) is also fixed, cleanly and consistently. **But this revision's own fix for Round 1's Low finding L2 (the "Dort" keyword false-positive) introduces a new, verifiable High finding**: Doc_02 §7 now asserts, confidently and specifically, that no vendored source touches the 1618–19 Synod of Dort directly — a claim that is factually wrong, checkable against the very file the document already cites, and wrong in a way that recreates this exact project's most-repeated failure pattern (asserting in the builder's own voice that a source does or doesn't say something it does or doesn't actually say). One further Medium finding is a small residual inconsistency left over from the H3 fix. This is a substantially smaller defect set than Round 1 — the underlying primary-source handling remains excellent — but it is not yet clean enough to clear.

---

## Confirmed FIXED (independently re-verified, not taken on the document's own word)

### Round 1 H1 — Fabricated "Swiss Reformation" / Manchester citation: gone

Grepped all three documents for "Swiss Reformation" and "Manchester." The only hit across the whole document set is in Doc_02's own masthead status line, which *describes* the Round 1 finding retrospectively (naming the defect that was fixed) — it does not assert the fabricated attribution as a live claim anywhere. I independently re-pulled `cic-website/data/world-census.json`'s `sources` field for `the-reformed-cities-zurich-and-geneva`: it contains exactly one secondary-scholarship entry, "Scott Manetsch, Calvin's Company of Pastors (OUP, 2013), with Bruce Gordon, Calvin (Yale, 2009)" — no Gordon *Swiss Reformation* title anywhere. Doc_02 §3, Source_Registry.md row 11, and Source_Acquisition_Manifest.md §3 now all correctly name only Gordon's *Calvin* and Manetsch, and Registry row 11 is now split correctly (one book per prior fabricated pairing is gone). **Genuinely fixed.**

### Round 1 H2 — Anabaptist-origin correction: now stated in full, and consistent with Doc_01 §7

Doc_02 §2 (Zwingli's Author Gravity, *Influence*) now states, under an explicit "Discharging Doc_01 §8 item 4's own binding instruction directly here" heading: Grebel baptized Blaurock at Manz's house (21 January 1525), Blaurock then baptized the others including Manz; Grebel and Manz were formerly in Zwingli's circle; Blaurock (a former priest from Chur) is not established as having belonged to that circle, and the document does not extend the claim to him. I compared this directly against Doc_01's own text (line 139, its §8 item 4 source): the wording is near-verbatim and factually identical — same names, same event, same careful non-extension of circle-membership to Blaurock. Doc_02 also names the two governing documents Doc_01 required be corrected (Source Readiness Dossier §5, Step 0 §3 B3) and states plainly that both are inaccurate at this level of detail. Doc_02 §9 item 2 now explicitly logs this as "DISCHARGED this pass." **Genuinely fixed and cross-document consistent.**

### Round 1 H3 — Registry rows 13–17 schema conflation: the schema fields themselves are now fixed (see also new Medium finding below)

Read `Source_Registry_Template.md` directly. Its schema requires: Exclusion Reason blank if Native, populated only with "Out-of-Boundary" or "Named Comparandum" if Excluded; Licensed For blank if Excluded, and if Native, naming "the specific gravity, force, lexicon term, or Representative trait this source justifies."

Checked rows 13–17 directly: **Exclusion Reason is now blank ("—") on all five rows**, and Boundary Status remains correctly Native (these sources' subject matter is squarely this world's own). Licensed For now names an actual target for each (e.g., row 14: "Consistory authority-structure claims (Doc_01 §5 Strand Determination limb 2), once acquired..."; row 16: "Direct Beza-strand and Dort-throughline claims (Doc_01 §7), once acquired..."). The "not currently usable" caveat that trails each Licensed For entry is additional disclosure, not a schema violation — the acquisition-status narrative that used to live (wrongly) in Exclusion Reason has moved into the Verification Note, exactly as Round 1's suggested fix (a) specified. **The core schema violation is genuinely fixed.**

### Round 1 H4 — "documented" reintroduced on the Dort-delegate claim: fixed, and no other misuse found

Doc_02 §7 no longer applies "documented" to the Dort-delegate claim; it now reads "attested in standard Reformation historiography, not yet verified against a vendored primary source, the same calibrated formulation Doc_01 itself uses throughout rather than the reserved term 'documented.'" I compared this against Doc_01's own current phrasing for the identical claim (§8 item 3 / the Live evidence passage): "attested in standard historiography, not yet checked against a vendored primary source" — same substance, consistent.

I then extracted Constitution Article 17 / Construction Framework V7.4's own five-level definitions directly from the .docx files (via zipfile+regex) to check every other use of "documented" in the document set against the actual bar ("Multiple independent sources with no serious scholarly dispute. Permitted language: 'documented,' 'securely attested.'"):
- Doc_02 §2, "The documented mediating figure of the entire Zurich/Geneva bridge" (Bullinger) — checked against Doc_01 line 90, which independently and already treats the identical claim as Documented-tier, "stated here without qualification." Consistent, not a fresh overclaim.
- Doc_02 §2, "documented far less in this vendored corpus" and §8, "not itself a documented fact" — both ordinary-English uses (describing corpus density, or explicitly denying Documented status), not confidence-tier assertions.
- Doc_02 §6, "a documented woman's voice" (Dentière) — a bare, undisputed biographical fact (she existed and published).
- Registry row 5 Licensed For, "The documented Zurich/Geneva doctrinal bridge" — describes what the directly-vendored, Confidence-A Consensus Tigurinus text itself demonstrates, consistent with Doc_01 §5.

**No misuse of the reserved term found anywhere in the current document set.**

### Round 1 Medium/Low findings — also confirmed fixed

- **M1 (Heidelberg Catechism overclaim):** Doc_02 §1 now quotes Doc_01 §2 verbatim ("a distinct pastoral/catechetical voice alongside Calvin's Geneva Catechism, from the Reformed tradition's German wing") rather than paraphrasing it into "doctrinally continuous with both." I checked Doc_01 §2's actual text directly — the quotation is exact. The predestination-restraint nuance is now flagged Contested in §8 rather than asserted. **Fixed.**
- **M2 (Registry rows 11–12 Licensed For):** now name specific targets (Calvin's biography/Geneva ministry for Author Gravity §2; Geneva's pastoral/consistorial structure for Doc_01 §5) instead of generic "background only" boilerplate. **Fixed.**
- **M3 (thin §10 escalation self-assessment):** §10 now runs all four escalation categories individually, each with document-specific reasoning (not just headers) — a real improvement matching the bar Doc_01 was eventually held to. **Fixed.**
- **M4 ("G1" label collision):** Doc_02 §9 item 3 now adds an explicit disambiguating note ("'Doc_02/G1' there is that document's own generic shorthand for the acquisition stage, not a pointer to this Manifest's specific item G1"). I checked this against Doc_01 §8 items 7 and 8 directly: both do in fact use "Doc_02/G1" generically for what the Manifest separately labels G3 and G1 respectively — the disambiguation is accurate, not invented. **Fixed.**
- **L1 (Consensus Tigurinus page range):** Registry row 5 now says "pp. 195–244" (was 195–247). I read the vendored file's own intake header directly — it has been corrected to "pp. 195-244... per the last page-header numeral visible" — and I independently confirmed by reading the end of the file that the last visible printed-page marker is indeed "244," with no further page numbers before the file ends. **Fixed and independently re-verified against the actual file, not just the Registry's claim.**
- **L3 (Registry vocabulary-ownership overstatement):** unchanged, correctly left alone per Round 1's own instruction that this was pre-existing project-level versioning drift outside this build thread's scope to fix.

### Spot-checks of Round 1 "checked out cleanly" items — still clean

- **Corpus-map count:** re-verified directly by parsing `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml` — 10 works across exactly 8 unique files. Matches Doc_02 §1 exactly.
- **§9 renumbering:** the new item 2 (Anabaptist discharge) was inserted cleanly; the diff shows a straightforward, correctly-renumbered 1–8 sequence with no item lost, duplicated, or skipped.
- **Translator/date attributions** (Beveridge 1845, Waterman 1815, Jackson 1901/1912, Schaff 1919): untouched by this revision's diff; no reason found to doubt Round 1's direct verification.

---

## High findings (new this round)

### H1 (Round 2) — The revised "Dort" disambiguation note is itself false: the vendored Schaff file *does* touch the 1618–19 Synod of Dort directly, repeatedly, within the very section Doc_02 already cites as verified

Doc_02 §7 now states: *"No vendored source in this corpus currently touches the 1618–19 Synod of Dort directly in any case (the Schaff volume's own text contains the word 'Dort' once, referring to an unrelated 1574 synod, not this one — a keyword search alone would mislead)."* This sentence was added this revision, in direct response to Round 1's L2 finding (which had only established that one "Dort" hit refers to an unrelated 1574 synod, and asked for a one-sentence disambiguating note — not for a sweeping claim that no other reference exists).

I grepped `cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` for "dort" directly: **it contains the word four times, not once.** The first (line 2724, "the synods of Wesel, 1568, of Emden, 1571, and of Dort, 1574") is indeed the unrelated 1574 synod Doc_02 correctly identifies. The other three are not:

- Line 2751: *"the famous General Synod of Dort, after a careful examination, opposed any change, and, in its 148th Session, May 1, 1619, it unanimously delivered the judgment that the Heidelberg Catechism 'formed altogether a most accurate compend of the orthodox Christian faith...'"* — this is the actual 1618–19 Synod of Dort, named by session number and exact date, quoting its own verdict on the Heidelberg Catechism.
- Line 2869: *"The English delegates to the Synod of Dort, George Carleton (Bishop of Llandaff), John Davenant (afterwards Bishop of Salisbury), Archdeacon Samuel Ward, Dr. Thomas Goade, and Walter Balcanqual, said..."* — five named, real historical delegates who attended the actual 1618–19 Synod.
- Line 2878: *"The favorable judgment of the Synod of Dort itself has already been quoted"* — a direct back-reference to the same 1619 session.

This is not a marginal or hard-to-find passage: it sits inside **§ 69, "The Heidelberg Catechism, 1568"** (pp. 548–551 of the printed volume) — the exact section Source_Registry.md row 10 already cites as its own Verification Note ("Sec. 69, original pp. 529–554") and marks Confidence A, "Verified directly." The drafter had already opened and cited this section for an unrelated purpose and still missed, or mischaracterized, its own direct discussion of the real Synod of Dort three paragraphs later.

**Why this matters, and why it is High rather than Low:** this recreates, in a new location, the exact failure category this world's own build history has already named twice as its most serious defect type — asserting in the builder's own voice, without checking, that a specific document does or does not say something. Round 1's H1 was a false positive (claiming a source says something it doesn't); this is a false negative stated just as confidently ("in any case"), about the same kind of question (what does this specific vendored file actually contain), inside a sentence whose entire purpose was to correct an earlier, smaller version of exactly this problem. It also has real downstream consequence: this document's own Confidence Map and §9 open-items list treat the Dort question as entirely unaddressed by any vendored source, when in fact a vendored file already contains a genuine (if English-delegation-only, not Zurich/Geneva-delegation) primary-adjacent account of the actual Synod's proceedings and judgment — material a later document (Doc_04, or a future VI.9/VI.26 build) would want to know exists.

**Fix required:** correct Doc_02 §7 to state accurately that the Schaff volume's discussion of the Heidelberg Catechism (§69) *does* independently attest the real 1618–19 Synod of Dort's own proceedings, its 148th Session (1 May 1619) verdict on the Catechism, and the names of its English delegates — while still correctly noting this does **not** verify the Zurich/Geneva delegate-participation claim specifically (Diodati, Tronchin, Breitinger are not named anywhere in this file). Consider whether this newly-identified passage is worth a Registry Verification Note addition on row 10, and whether it belongs in Doc_02 §9 as a small new open item (a genuine, vendored, English-side primary-adjacent Dort source exists in this corpus, distinct from and short of the still-unverified Zurich/Geneva delegation claim).

---

## Medium findings (new this round)

### M1 (Round 2) — Registry's own "Priority second-opinion review trigger" summary line was not updated to match the H3 fix, and now contradicts the corrected schema fields

`Source_Registry.md`'s closing line (unchanged by this revision — confirmed via diff) still reads: *"Rows 11–17 are consultation-only, excluded, or explicitly flagged as unverified..."* But rows 13–17's Boundary Status is now explicitly Native (per the H3 fix above), and their Exclusion Reason is now correctly blank. Describing these same rows as "excluded" in this summary sentence directly contradicts the schema fields two lines above it, and reintroduces — in prose, in the one paragraph a reader is likeliest to skim for a bottom-line — the identical Native/Excluded conflation the H3 fix was supposed to eliminate throughout the document. This is exactly the kind of fix-round leftover `cic-build-cycle`'s own history warns about: the schema cells were fixed carefully; the summary sentence describing them was not checked against the fix.

**Fix required:** rewrite the sentence to reflect the corrected schema — e.g., "Rows 11–12 are consultation-only Native background sources; rows 13–17 are Native but not yet acquired (Confidence D/E)" — rather than reusing "excluded" for rows that are no longer, and per the Template should never have been, marked Excluded.

---

## Low findings

None beyond what Round 1 already found and this revision correctly left alone (L3, the pre-existing Article 17/Framework versioning gap, correctly flagged rather than touched, per `CLAUDE.md`'s doc-hygiene default).

---

## Escalation-category check (run fresh)

- **Representative identity, title, or voice decision:** does not apply.
- **Portfolio-level or cross-world strategic decision:** does not apply. The two findings above are ordinary content-accuracy defects, fixable within this build thread's own authority.
- **Governance or methodology decision:** does not apply. Neither finding touches the Template or Framework; H1(R2) is a factual-accuracy correction to Doc_02's own prose, and M1(R2) is a self-consistency fix within the Registry.
- **Unresolved tension the pipeline can't close on its own:** does not apply. Nothing here contradicts an already-cleared document or reopens a settled decision.

No escalation category is live. Both findings are addressable by ordinary revision.

---

## Recommendation

Revise Doc_02 §7 (correct the Dort/Schaff false claim) and the Source_Registry.md closing summary line (correct the stale "excluded" reference), then send the revised set through one more focused review round — specifically re-checking the corrected Dort passage against the vendored file, and re-checking the Registry's summary line for internal consistency with its own schema fields. Given how narrow the remaining gap is (one factual correction, one internal-consistency correction), this should be resolvable in a single further pass without touching anything else in the document set — the underlying primary-source citation discipline elsewhere in Doc_02, the Registry, and the Manifest remains sound.
