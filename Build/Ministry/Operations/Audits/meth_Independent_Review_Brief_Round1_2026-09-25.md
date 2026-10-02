# Independent Adversarial Review Brief — The Methodist Revival, Steps 0–2

**For:** whoever runs the genuinely independent (cross-model) review this world's build thread could not itself perform this pass — see `Open_Gaps_Tracking.md` item 3 and every review-round file in `Review-Artifacts/` for why. This brief is written so that reviewer needs nothing from this build thread except the pointers below; it should read the actual files itself, not this brief's own summary of them.

**Standard to apply:** `reference/method/CiC_Adversarial_Review_Standard_Practice.md` in full — source-level verification (open the actual vendored file, not this document's paraphrase of it), a P0/P1/P2 severity vocabulary, counted structural checks rather than an impression, and a genuine bottom-line verdict. Model tier per that same document: Opus.

**What this pass is reviewing:** three documents, treated as one unit because they were built together and reference each other constantly:
- `worlds/meth/Step0_Movement_Scope_Confirmation.md`
- `worlds/meth/Doc_01_World_Identification_Boundaries_Orientation.md`
- `worlds/meth/Doc_02_Source_Ecology.md`, plus its two co-equal companions `worlds/meth/Source_Registry.md` and `worlds/meth/Source_Acquisition_Manifest.md`

**What already happened, so this pass doesn't re-litigate settled ground.** Each document cleared one same-thread adversarial pass (`Review-Artifacts/Step0_Review_Round1.md`, `Doc01_Review_Round1.md`, `Doc02_Review_Round1.md`), each verdict COSMETIC ONLY, each catching and fixing one real error (an arithmetic slip; a leftover process-narration artifact; a row-count error). Read those three files first — not to trust their own account, but so this pass calibrates on what has already been checked once and aims fresh skepticism at what hasn't. **This pass is the first review that is actually independent** in the sense `cic-build-cycle` requires; treat everything in the three target documents as unverified until you yourself have checked it, regardless of what the same-thread rounds claim to have confirmed.

**Read this world's own `Open_Gaps_Tracking.md` and `meth_Decision_Log.md` before starting** — both name real, disclosed limitations (a stale-checkout version mismatch since corrected; a pre-existing engine tool gap; a genuinely incomplete corpus) this pass should treat as background, not as new findings to rediscover — but should independently spot-check at least once (per the adversarial standard's own rule: re-verify the most severe claims yourself rather than trusting a prior summary, including this build thread's own).

## The specific failure modes to hunt for, named directly rather than left implicit

This project's own real history (per `CiC_Adversarial_Review_Standard_Practice.md` and the review-round history visible in `worlds/rzg/rzg_Decision_Log.md`) has produced, more than once: a fabricated or inverted quotation; a citation to a source that doesn't say what it's cited for; a claim asserted as the census's or a prior document's own wording when it isn't verbatim; two documents in the same world silently contradicting each other on the same underlying fact; a scope or strand decision reached by weighing evidence selectively rather than running the actual named test; and — this world's own most likely failure mode, given its own disclosed corpus gaps — a claim about the movement's own working ministry (1739–1790) resting on evidence this pass's own corpus doesn't actually cover (only Journal Vol. I, 1738, and Sermons Vol. I are vendored). Assume the same risk classes are present in this world's own documents until checked, the same way the standard practice's own dispatch language does for its own precedent case.

## Per-document checklist

### Step 0

- Re-verify the Aldersgate quotation directly against `cic/texts/wesley-j_journal-v1_curnock1909.txt` (lines cited in Doc_01 §2, not Step 0 itself, but Step 0 references it) — character for character, including the disclosed day-heading digit discrepancy.
- Re-verify the Article 4 quotation against `reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` directly (it is a `.docx`; extract via `python -m zipfile` or equivalent, do not trust a copy from another world's document).
- Check the §2 A3 contemporary-movements claims (the Whitefield "Free Grace" breach, the Moravian relationship, the Fetter Lane/Countess of Huntingdon material) against Widely Accepted historiography — flag anything stated with more confidence than the document's own hedge admits, or anything actually wrong.
- Check the Tier/disposition reasoning in §3–4 actually follows from the evidence named, not from a foregone conclusion.
- Confirm the version-discrepancy disclosure (§0) is now accurate against the real, current `reference/method/CiC_Record_Native_World_Build_Process_V1.8.md` — this was corrected once already post-merge; verify the correction itself is accurate, not merely present.

### Doc_01

- **The Whitefield world-separation argument (§4) and the British/American Strand Determination (§5) are this document's own two real, load-bearing judgment calls — give these the most scrutiny, not the least.** Independently re-run the Framework's own six-question test on both relationships yourself, from the evidence named, rather than checking only whether the document's own application of the test is internally consistent. Would a fair-minded historian reach the same conclusion from the same facts?
- Check every specific date and event (Aldersgate 24 May 1738; the Wesley/Whitefield breach 1739–41; the Fetter Lane breach 1740; the 1743 General Rules; the 1744 first Conference; the 1784 Christmas Conference; Wesley's 1791 death; the 1795 Plan of Pacification) against standard historiography — this build thread flagged most of these "Widely Accepted, not independently vendor-verified," which is an honest hedge, not a substitute for actually being right.
- Check §7's Moravian account (the 1735–36 Georgia-voyage first contact, predating Aldersgate) — this is the single most complex, multi-part historical claim in the document; verify it is not overstated or under-hedged.
- Check that §4 and §5 do not silently contradict each other or double-count the same evidence for two different conclusions (the same six-question method, applied to two different relationships, reaching opposite answers) — Doc_01's own Round 1 review claims to have checked this; re-check it yourself.
- Confirm every internal cross-reference (Doc_01 → Step 0 §4 items; Doc_01 → Open_Gaps_Tracking.md item numbers) actually resolves to what it claims.

### Doc_02, Source_Registry, Source_Acquisition_Manifest

- **Recount every count claim.** This build thread's own Round 1 review caught one wrong count ("eight" vs. the actual eleven corpus-map rows); do not assume that was the only one. Recount the Source Registry's own 22 rows; recount the Manifest's own G-item numbering; recount Open_Gaps_Tracking.md's own 16 entries (note: this brief itself was written after a 16th entry was added post-merge — confirm the number in the live file, not this brief).
- Re-verify both directly-quoted passages (the Aldersgate quotation, the Large Minutes "rise of Methodism" quotation) against the actual vendored files yourself, at the cited line numbers, independent of this build thread's own claim to have done so.
- Check the Author Gravity Assessment (§2) for the specific failure mode named in this project's own history: does it let a source's own visibility (word count, how much survives) stand in for a claim about the movement's own actual historical balance, anywhere it isn't explicitly flagged as doing so?
- Check the Voice column in `Source_Registry.md` — does anything cited as "own" voice actually contain editorial or opponent material not flagged as such?
- Independently re-run `python -m engine.m9.cli holdings meth` (after `mkdir -p records/meth` if needed) and `grep -n "methodist" engine/m1/cross_world.py` yourself — this build thread's own account of the holdings-tool finding (Open_Gaps_Tracking.md items 15–16) should be independently reproduced, not trusted, per the adversarial standard's own rule against accepting a dismissal without re-verification.
- Check the Doc_02 header's own disclosure paragraph (the corrected holdings-tool account) for internal accuracy against what you find.

## Cross-document consistency

- Every dated fact that appears in more than one of the three documents (Aldersgate's date; the 1784 Christmas Conference; the Moravian breach) should read identically or explain a stated, deliberate difference — flag any silent drift.
- Every escalation-category self-assessment (each document's own §on Disposition) should hold up under your own fresh run of all four categories, not merely be internally consistent with the document's own argument.

## What "done" looks like

A P0/P1/P2-tiered finding list, per document or combined; a genuine bottom-line verdict for each of the three documents (cleared / substantial revision required, with the specific finding(s) that require it); and, separately, an explicit answer to the one question this brief cares about most: **do the two real judgment calls in Doc_01 (§4 Whitefield-as-separate-movement; §5 British/American-as-two-strands) actually hold up against the Framework's own test, run fresh, or were they reached by a build thread that wanted a clean answer?** Save the result as `worlds/meth/Review-Artifacts/Independent_Review_Round1.md` (or split per document if that reads better) so it becomes this world's own first genuinely independent review round, per `cic-build-cycle`'s own definition — and so a future reader never has to wonder whether "independent review" here means what it means everywhere else in this project.
