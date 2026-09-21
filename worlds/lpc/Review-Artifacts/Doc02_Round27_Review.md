# Doc_02 — Source Ecology: Latin Pastoral-Congregational Christianity
## Round 27 Independent Adversarial Review — scoped to the banner-stripping rewrites of `Source_Acquisition_Manifest.md` and `Source_Registry.md` (commit `7bdb759`) against their own pre-rewrite text, and to the self-reported figures in the new Decision Log entry that records them

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `7bdb759`, "lpc: strip inline correction banners from Manifest and Registry", 2026-09-08 13:23:10 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Acquisition_Manifest.md` at `7bdb759` (81 lines, 5,289 words) read in full, front matter through the "Decision from the project lead" section
- The same file at `9c1cc01` (89 lines, 6,278 words), extracted with `git show 9c1cc01:…` — the pre-rewrite text Round 26's own fix pass left in place — and compared against HEAD hunk by hunk at word level (`git diff --word-diff=plain -U0`, **24 hunks**, every one read)
- `Source_Registry.md` at `7bdb759` (329 lines, 212 rows, 35,404 words) and at `9c1cc01` (329 lines, 212 rows, 37,611 words), compared at word level (`git diff --word-diff=plain -U0`, **43 hunks**, every one read), and independently re-parsed row by row by leading numeric cell
- `lpc_Decision_Log.md` (378 lines) — the new final entry, "2026-09-08 — `Source_Acquisition_Manifest.md` and `Source_Registry.md` rewritten to remove inline correction banners, extending the standing rule the prior entry named but left un-extended," read clause by clause, and **every one of its sixteen numeric/structural self-claims recomputed independently**; the log's own entry headings enumerated and counted by date; line 330 read directly for the Round 19 paragraph's own pointer into the Manifest
- `Doc_02_Source_Ecology.md` (158 lines) at HEAD, §10 read in full for the Registry Status line's inbound cross-reference, and §1/§9 for the network-access and G-item claims
- `Review-Artifacts/Doc02_Round26_Review.md`, read in full for its own eight findings, so each could be checked for an unfixed sibling in these two documents; `Doc02_Round8_Review.md`, `Doc02_Round9_Review.md`, `Doc02_Round10_Review.md`, `Doc02_Round11_Review.md`, `Doc02_Round13_Review.md`, `Doc02_Round14_Review.md` and `Doc02_Round18_Review.md` for the review-history of the Status line's own finding-count sequences
- `git diff --stat 9c1cc01 7bdb759`, to establish which files this commit actually touched (three: the Manifest at ±52 lines, the Registry at ±132, the Decision Log at +14/−0)
- Registry word counts recomputed at `1e01153`, `acb3396`, `9f14783` and `9c1cc01` in turn, to establish which baseline the entry's "before" figure could have come from

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not write either rewrite pass, did not write the Decision Log entry recording them, did not dispatch or brief the subagent that edited the Registry, and did not write Rounds 1–26.

**Scope, stated plainly — this is a Round-26-shaped round, not a Round-25-shaped one.** The sourcing claims underneath these two documents were independently re-verified through Round 25 and no new sourcing work happened in either pass, so this round does not re-run the recall test, the PRESS question, the archive.org identity fetches, or the corpus-map audit. Four briefs instead. First: diff each rewrite against its own prior state and confirm that every substantive claim, figure, Registry-row citation, dated fact, identifier, cross-reference and scope qualifier in the old text survives in the new — looking specifically for the shape Round 26 found on Doc_02, a fact deleted alongside the banner wrapped around it, and for meaning changed by the removal of context a banner was carrying. Second: check each of Round 26's own eight findings for an unfixed *sibling* instance in these two documents. Third: recompute every figure the new Decision Log entry asserts about its own pass, rather than accept the entry's account of itself. Fourth: re-run the structural checks (run-aware bold-nesting, paren/bracket/backtick balance, header/table/list structure, cross-reference resolution) on both rewritten files.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC.**

**The `Source_Registry.md` rewrite is, at the row level, the cleanest pass in this document set's recorded history, and its central claim holds.** All 43 Registry hunks were read at word level. Across the 212-row table, **every** substantive residue survives: an atom-level sweep of the old text against the new — archive.org identifiers, backticked file paths and locus ids, dates, imprint years, CSEL/CCSL volume numbers, row numbers, G-item numbers, section pointers and every bare integer — found **no reduction that is not fully accounted for by pure correction-history narration**, and each of the 64 distinct reductions the sweep flagged was traced individually to the banner it sat inside, with the current fact confirmed still standing in the same cell or at the row the cell points to. Several cells were rewritten *better* than a strip: row 33 gained "four of them reviews and the fifth the publisher page" to carry Round 21's L5 substance forward; row 49 gained an explicit «"Epistolae," not "Epistulae"» to carry Round 4's C1 forward; rows 45, 56 and 196 converted their banners into standing negative warnings ("**not** `histoirelittra00moncuoft`", "`archive.org/details/PossidiusAug` is a 2008 audio recording", "**Letter 185 is NOT in this range**") rather than deleting the disambiguation with the history. Both disclosed "improvements" hold: the fragile "line 295" pointer's descriptive replacement resolves uniquely (the phrase it names occurs in exactly one other paragraph, the intended target), and no "most recently Round 8's own M1" survives anywhere.

**All structural claims reproduce exactly.** 212 rows, numbered 1–212, no gap and no duplicate; 12 pipes on every row; the physical row-number sequence **byte-identical** between the pre-edit and post-edit commits, with the three disclosed-placement rows (48, 52, 60) at identically the same out-of-sequence positions; Registry headers identical line-for-line; table header and separator rows unchanged; list structure unchanged; bold-marker nesting clean. All **46** distinct Manifest→Registry row references, all **211** distinct internal Registry row references, all nine Manifest G-items and both Manifest §-references resolve to targets that exist and say what the citing document claims they say.

**Where the findings are: in what both passes deleted outright rather than trimmed, and — for everything this pass actually introduced — overwhelmingly in the Manifest rather than the Registry.** The Manifest, the half rewritten directly by the build thread rather than by the briefed subagent and the half for which **no word-level diff-read is disclosed anywhere**, contributes **M1**, four of the five LOWs, and the pass's one plainly false self-claim, out of 81 lines. The Registry, across 212 rows and 43 hunks, contributes **M2**, one LOW and one COSMETIC — and all three of those sit outside the table, in the front matter and one Confidence cell. **M3** is not this pass's own breakage at all: it is a cross-reference `acb3396` broke, which Round 26 caught and fixed in the Manifest only, and which this pass then rewrote past without sweeping.

**Two of the three MEDIUMs are the shape Round 26 named**: a paragraph deleted with something outside itself pointing into it. At M1 that happens three-deep — two pointers inside the Manifest and one from `lpc_Decision_Log.md` — and the deleted paragraph was not a banner at all, containing none of the three phrases the pass searched for. At M3 it is the same single pointer Round 26 already found once, left standing in the sibling document.

---

## Decision Log self-claims — every figure recomputed independently

| Claim in the new 2026-09-08 entry | Recomputed | Result |
|---|---|---|
| Manifest word count 6,278 → 5,289 (≈16%) | `wc -w` on `git show 9c1cc01:…` = **6,278**; on HEAD = **5,289**; Δ989 = 15.75% | **Exact** |
| Manifest bold-bearing lines 38 → 33 | `grep -c '\*\*'` = **38** → **33** | **Exact** |
| Manifest: zero bold-nesting mismatches, zero literal survivals, across all 33 lines | markdown-it-py 4.2.0 `commonmark`, `<strong>` spans extracted from rendered HTML of every bold-bearing line vs. run-aware sequential `**` pairing, code spans normalized on both sides: **0 mismatches, 0 odd-count lines, 0 literal survivals** | **Holds** |
| Manifest: case-insensitive residue search returns zero hits | "corrected here" **0**; "independent review round" **0**; "from an earlier draft" **0** | **Holds** |
| Manifest: "No fact, figure, Registry-row reference, archive.org identifier, or acquisition detail was altered" | §1's superseding note deleted outright, taking a dated verification fact (WebFetch + curl → HTTP 200) and the document's current network-access status with it | **FAILS — see M1** |
| Manifest: "Four heading-correction banners were deleted outright" (implying nothing else was) | Four heading banners deleted, **plus** the §1 network-access superseding note — a fifth outright deletion, undisclosed | **Incomplete — see M1** |
| Registry word count 37,577 → 35,404 (≈5.8%) | HEAD = **35,404**, exact. Pre-edit = **37,611**, not 37,577 — and 37,611 at *every* candidate baseline (`1e01153`, `acb3396`, `9f14783`, `9c1cc01`). True Δ = 2,207 = **5.87%**, not 5.78% | **"After" exact; "before" wrong by 34 — see C3** |
| Registry bold-bearing lines held at 200 | **200** → **200** | **Exact** |
| Registry: 212 rows, numbered 1–212, no gap or duplicate | 212 rows by leading numeric cell; sorted set is exactly 1–212 | **Holds** |
| Registry: 12 pipe characters on every row | set of per-row pipe counts = **{12}**, old and new | **Holds** |
| Registry: physical row order byte-identical to the pre-edit commit | row-number sequences identical, old vs. new, element for element | **Holds** |
| Registry: disclosed-placement rows 48, 52, 60 unmoved | out-of-sequence transitions identical old and new: (…48→42…), (…193→60…), (…60→52…) | **Holds** |
| Registry: zero mismatches, zero literal survivals, across all 200 bold-bearing lines | **0 mismatches, 0 odd-count lines, 0 literal survivals** | **Holds** |
| Registry: backtick and parenthesis balance clean on every line | 0 odd-backtick lines, 0 unbalanced-paren lines, 0 unbalanced-bracket lines (inline code stripped) | **Holds** |
| Registry: case-insensitive residue search returns zero hits | "corrected here" **0**; "independent review round" **0**; "from an earlier draft" **0** | **Holds** (but see **C4**) |
| "448 bold-bearing lines" across four core documents, zero mismatches, zero literal survivals (commit message) | Doc_02 **64** + Registry **200** + Manifest **33** + Decision Log **151** = **448**; all four return 0 mismatches, 0 literal survivals | **Exact** |
| "The full word-level diff (43 hunks) was read in full" | Registry alone = **43**. Manifest = **24**. Both together = **67** | **Holds for the Registry only — see C2** |
| Two disclosed "improvements" (the "line 295" pointer; the "most recently Round 8's own M1" generalization) | Both present; the replacement descriptive pointer resolves uniquely; "most recently Round 8" occurs **0** times at HEAD | **Holds** |

**Structural checks beyond the entry's own.** Registry headers byte-identical between old and new, at identical line numbers; Manifest header text identical (line numbers shifted by the 8-line contraction, expected); Registry table header row and separator row each present exactly once, unchanged; top-level list-item counts unchanged in both files (Manifest 1, Registry 0); **all fragile `line N` cross-references are now gone from both files** (old Manifest carried two, at lines 67 and 87; old Registry carried one, at line 325 — none survives), which is a real improvement beyond the stated mandate. **Markdown structure is intact in both documents.**

**Round 26's eight findings, checked for unfixed siblings in these two documents.** L2's sibling — the Donatism build's own five-failed-attempts fact — **survives intact** at Registry row 44 and is correctly stripped of its banner only. L6's sibling class (a Registry-row citation dropped while rephrasing) — **none found**; the atom sweep confirms every row reference in the old Registry and Manifest survives except those inside pure correction-history. C4's sibling class (an arithmetic claim that does not match its own numbers) — **none found**: "reaching zero at Round 5 and holding for ten rounds running" is correct against the HIGH sequence (Rounds 5–14 = ten); "Round 3's rise," "Round 2's dip" and "Round 5's rise" are all correct against the MEDIUM sequence; row 23's "thirteen works" matches a title list of exactly thirteen distinct works; row 11's 17 + 11 + 2 + 138 = 168 holds. **M2's sibling — found and unfixed: see M3.** **L1's sibling class — found: see C4.** **C1's sibling — found, and re-created by this very commit: see C1.**

---

## MEDIUM findings

### M1 — The Manifest's §1 network-access **superseding note** was deleted outright, though it is not a banner; §1 now asserts a network block the same section contradicts seven times, three live pointers into it break, and a dated verification fact is lost

**Where.** `Source_Acquisition_Manifest.md`, old line 61 (`9c1cc01`), deleted entirely. The paragraph immediately above it — old line 59, new line 57 — is untouched.

**Old text, verbatim, deleted in full:**

> **Superseded 2026-09-08: network access confirmed working.** Direct WebFetch and curl tests against `archive.org` both returned HTTP 200 this session, with no proxy relay failures — the infrastructure-level block this paragraph and this Manifest's own G1–G9 acquisition pattern (Mark opening each link and supplying the file himself) both rested on no longer holds. This paragraph is kept as the historical record of a real, previously-confirmed limitation, not rewritten to look retroactively current. Consequence: G1's remaining Pars III, G2, G5, G6, G7, G8, and G9 were all fetched, opened, and independently verified directly by this build thread rather than requiring the project lead's own manual download — see each item's own "Fulfilled 2026-09-08" paragraph above.

**This is not a correction banner.** It contains none of the pass's own three governing phrases — no "corrected here," no "independent review Round N's own X," no "from an earlier draft's own Y." It is a dated supersession note of exactly the kind the Manifest carries at three other sites, all of which the pass left standing (new lines 11, 61, 79). The Decision Log entry's account of the Manifest names only "**four** heading-correction banners deleted outright," and asserts "**No fact, figure, Registry-row reference, archive.org identifier, or acquisition detail was altered**." Both statements are wrong about this deletion.

**Consequence 1 — §1 now states, in the present tense and unqualified, something false.** New line 57 opens: *"**A network-access limitation, disclosed rather than papered over.** This build session's outbound network access **blocks** direct fetch of the specific pages named above — archive.org and general web domains return an egress-blocked error when checked directly from inside this session…"* and closes with live operational instruction: *"Before treating any of G1–G5, G7, or G9 as ready to vendor: (a) open the link and confirm it actually delivers full text under free access…"* **Eight** separate paragraphs above it in the same section already say the opposite — new line 21 ("**Pars III fulfilled 2026-09-08.** Network access to archive.org, confirmed working for the first time this build…"), and seven further "Fulfilled" paragraphs at new lines 25, 35, 39, 43, 47, 51 and 55, each of which opens "With network access confirmed working." The one sentence that reconciled the contradiction is gone, and the instruction block now tells the project lead to go open links for items the same section records as already vendored.

**Consequence 2 — three live cross-references break.** All three pointed at the deleted note and were true before this commit:

1. `Source_Acquisition_Manifest.md` **new line 11** (unchanged by this commit): *"With network access confirmed working the same day **(§1 below)**, G1's remaining Pars III, G2, G5, G6, G7, G8, and G9 were fetched…"* — §1 no longer confirms it; §1 now denies it.
2. `Source_Acquisition_Manifest.md` **new line 81** (unchanged by this commit): *"…rested on a real, then-genuine network-access block that has since been confirmed resolved **(see §1's own superseding note)**."* — §1 has no superseding note. Case-insensitive, the string "supersed" occurs in §1 exactly once at HEAD, at new line 19, and there it is about Hartel's CSEL 3 being superseded by CCSL 3 — an unrelated claim about an edition.
3. `lpc_Decision_Log.md` **line 330**, the Round 19 paragraph: *"…contradicting the Manifest's own later 'Status update, 2026-09-08' section closing eight of them, **with no superseding note of the kind this Manifest's own network-access paragraph already carries for itself** (M2)."* — present tense, and no longer true.

The pass also deleted the one *inbound* pointer it could see: old line 87's "on the same practice this Manifest already follows at line 11, **line 61**, and its own §1 heading" was trimmed to "Superseded 2026-09-08:". Old line 61 *was* the note. Both the pointer and its target went; the two pointers the pass did not have open stayed and now dangle.

**Consequence 3 — a dated, independently-verified fact is lost.** "Direct WebFetch and curl tests against `archive.org` both returned HTTP 200 this session, with no proxy relay failures" is the primary evidence for the single operational change that closed eight of nine G-items. It is the only statement of that test anywhere in the Manifest or the Registry: `` `archive.org` `` in backticks falls 2 → 1 across the rewrite, and the bare integer "200" falls 1 → 0. The underlying fact survives in `lpc_Decision_Log.md`'s own "2026-09-08 — Network access confirmed working" entry, which is why this is MEDIUM and not higher — but §1 is where this Manifest discloses its own operating constraints, and the disclosure no longer appears there.

**Why this is MEDIUM and not LOW.** It is not a dropped ornament. It is (a) a live document now asserting the opposite of its own current state, in a paragraph a reader is directed to twice for the reconciliation that used to be there; (b) three checkably-broken pointers, all of which this commit broke; (c) an outright deletion of non-banner text that the pass's own account does not disclose and expressly denies. This is the Round 26 M2 shape — deleting a paragraph something outside it points into — arriving inside the very file Round 26 identified as the victim last time.

### M2 — The Registry's Status line deleted both fourteen-round finding-count sequences while keeping every claim built on top of them, reversing Round 9's own documented remedy

**Where.** `Source_Registry.md` line 3, the Status line — the first Registry hunk of this commit.

**Old text (the two parentheticals, verbatim):**

> **HIGH findings fell monotonically to zero and have stayed there** (Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0), reaching zero at Round 5 and holding for ten rounds running. **MEDIUM findings did not fall monotonically** (15/6/7/4/9/9/2/2/1/2/1/1/1/0 — added here, Round 6's own L1, since an earlier draft of this line stated no numbers at all, leaving a reader unable to check the companion document's own "fallen each round" claim against anything): Round 3's rise and Round 2's dip both reflect… **This sentence does not otherwise characterize the trend or classify what kind of finding each round made** — each round's own review artifact is the authoritative account of what it found and of what kind; this line states only the raw counts.

*(Quoted verbatim. The three elements this finding is about are the two parenthesised number series and the closing clause "this line states only the raw counts.")*

**New text:**

> **HIGH findings fell monotonically to zero and have stayed there**, reaching zero at Round 5 and holding for ten rounds running. **MEDIUM findings did not fall monotonically**: Round 3's rise and Round 2's dip both reflect… **This line does not otherwise characterize the trend or classify what kind of finding each round made** — each round's own review artifact is the authoritative account of what it found and of what kind.

**What was correction-history and what was not.** Only the clause "— added here, Round 6's own L1, since an earlier draft of this line stated no numbers at all…" is banner. The two number series are data: fourteen review rounds' HIGH counts and fourteen review rounds' MEDIUM counts. Neither survives anywhere in a live document — `grep` for `6/2/1/1/0/0` and `15/6/7/4/9/9` at HEAD returns hits only inside `Review-Artifacts/` (Rounds 8, 10, 11, 13, 14, 17, 18, 19, 20, 23).

**Four claims that survive now have nothing to check them against, in a document whose readers are directed to check.** "Reaching zero at Round 5"; "holding for ten rounds running"; "Round 3's rise and Round 2's dip"; "Round 5's rise." All four are *true* — this round recomputed them from the fourteen review artifacts' own `Findings:` lines and both sequences reproduce exactly — but a reader at the site can no longer verify any of them without opening fourteen files. The deleted banner's own stated reason for adding the numbers was that without them a reader is "unable to check the companion document's own 'fallen each round' claim against anything." The pass deleted the numbers and left the claims, restoring precisely the condition Round 6's L1 was written to end.

**This reverses a remedy the review record shows was deliberate and repeatedly re-verified.** `Doc02_Round9_Review.md` M1 found the trend *narrative* false against the sequence stated in the same sentence; `Doc02_Round10_Review.md` line 27 records the remedy in terms: *"the specific structural remedy Round 9 introduced — dropping the comparative MEDIUM-findings trend claim and **letting the number sequence stand alone rather than narrating it** — holds."* The pass has now done the exact inverse: dropped the sequence and kept the narration. Six separate rounds — 9, 10, 11, 13, 14 and 18 — independently recomputed these sequences against the review artifacts as a standing check; `Doc02_Round18_Review.md` line 206 does it last, calling both "exact." That standing check now has no target in the live text.

**A dangling qualifier follows from the same deletion.** "This line does not **otherwise** characterize the trend" took its force from the sentence the pass also deleted, "this line states only the raw counts." With the counts gone, "otherwise" has no antecedent and the disclaimer disclaims against nothing — the line now characterizes the trend and *only* characterizes it.

**Undisclosed.** The Decision Log's Registry paragraph accounts for outright deletions as "a small number of pure correction-history clauses **with no independent substantive residue** (mostly heading- or label-correction banners, and a few historical drift-narratives in the front matter's own methodology paragraphs)." Two fourteen-element verified data series are not that.

### M3 — Unfixed sibling of Round 26's M2: the Registry Status line still points into `Doc_02_Source_Ecology.md` §10 for a 2026-09-02 disposition entry that §10 no longer contains — on a line this pass rewrote

**Where.** `Source_Registry.md` line 3, first clause — the same line M2 concerns, and the first hunk this pass edited:

> **Status:** **Approved to proceed** (self-disposed by the build thread together with `Doc_02_Source_Ecology.md`, 2026-09-02; **see that document's own §10 for the full disposition entry**).

**What it resolves to now.** `Doc_02_Source_Ecology.md` §10 (line 148 heading, body at lines 154–156) contains **zero** occurrences of the string `2026-09-02`. Its Disposition paragraph states a **2026-09-08** disposition and refers to the 2026-09-02 clearance only as a superseded subordinate clause ("Rounds 1–14 (2026-09-01–09-02) cleared the original text outright at Round 14… and that clearance was superseded…"). The paragraph that *was* the 2026-09-02 entry — old Doc_02 line 162, headed "Disposition (Round 14, superseded above; retained as the historical record it was written as)" — was deleted at `acb3396`.

**This is Round 26's M2, in the other companion document, unfixed.** Round 26 found the identical construction in `Source_Acquisition_Manifest.md` line 11 and graded it MEDIUM; the fix at `9c1cc01` repointed **only the Manifest**, to `lpc_Decision_Log.md`'s 2026-09-02 entry (log line 121, heading verified present and matching the Manifest's quotation verbatim). The Registry's identical pointer was never swept. The Manifest's fix even names the reason in passing — "(`Doc_02_Source_Ecology.md` §10 now states only the current, 2026-09-08 disposition that superseded this one)" — a sentence that is equally true of the Registry's pointer and was not applied to it.

**Why this belongs to this round rather than the last one.** The breakage predates this commit; the *omission* is this commit's. This pass had Registry line 3 open and rewrote it — the two number series at M2 come out of this same sentence — and did not check the cross-reference sitting in its first clause. It is the same scope-propagation shape Round 26 named: declining to edit a file is not a reason to skip checking it, and neither is editing one part of a line a reason to skip the rest of it.

*(Note, so the record is accurate: the Status line's own "**Approved to proceed** … 2026-09-02", stated without a supersession marker while Doc_02 §10 disposes all three documents to 2026-09-08, and its "Fourteen independent adversarial review rounds" over a record now at twenty-six, are both **pre-existing** staleness this commit did not introduce and which Rounds 16 through 23 each reported as observed state. Those are not this finding. The broken pointer is.)*

---

## LOW findings

### L1 — Manifest G7 had "that round" changed to "this round" in the same edit that removed the round identification, inverting the transform correctly applied to G4 four entries earlier

**Old** (`9c1cc01` line 47): "**Added this revision (Round 6's own recall-test item 1 / PRESS answer 1), the sharpest gap *that* round found, with an operational consequence.**"

**New** (line 45): "**Added this revision, the sharpest gap *this* round found, with an operational consequence.**"

With "(Round 6's own …)" gone, "this revision" and "this round" have no antecedent whatsoever, and "this round" now most naturally reads as the current one. The pass did the correct opposite transform at G4, four entries earlier in the same section, on the identical construction:

**G4 old** (line 33): "**Added this revision (Round 4's own M4), the sharpest gap *this* round found.**"
**G4 new** (line 31): "**Added at Round 4, the sharpest gap *that* round found.**"

So the two sentences that were parallel in the old text are now opposed, and the one that lost its anchor is the one that gained "this." This is a substantive alteration riding along with a banner strip — the shape Round 26's L5 named — rather than a deletion. A second casualty: G7's provenance in "Round 6's own **recall-test item 1** / PRESS answer 1" is now absent from the document entirely, since §1's intro (new line 17) records only "G7 from its PRESS answer 1."

### L2 — The "Added at Round N" provenance line is treated four different ways across G4–G9, one of which loses it outright

Old and new, side by side:

| | Old (`9c1cc01`) | New (HEAD) |
|---|---|---|
| G4 | "Added this revision (Round 4's own M4)…" | "**Added at Round 4**…" ✔ anchored |
| G5 | "Added at Round 4 (its own M3): …" | *(no "Added" line at all)* |
| G6 | "Added at Round 5 (its own M6/PRESS #1)." | "**Added at Round 5.**" ✔ anchored |
| G7 | "Added this revision (Round 6's own recall-test item 1 / PRESS answer 1)…" | "**Added this revision**…" ✘ unanchored |
| G8 | "Added this revision (Round 6's own recall-test item 2)." | "**Added this revision.**" ✘ unanchored |
| G9 | "Added at Round 7 (Round 7's own recall-test item 1 / PRESS answer 2)." | "**Added at Round 7.**" ✔ anchored |

G5's disappears because its entire "Added at Round 4 (its own M3)" clause was a banner wrapper around the rights-position correction, and the rewrite kept only the fact ("Public domain by imprint date (1901–05); the author's own death date (1941) has no bearing on that status"). Each G-item's round of origin is still recoverable from §1's intro line 17 — which is why this is LOW — but the section now reads inconsistently, and "Added this revision" at G7 and G8 states nothing at all.

### L3 — Manifest G2's "the same correction" now has no antecedent, and the CO-022 propagation rule it cited is gone

**Old** (line 25), the whole clause bold in the original: "Pellegrino's own year is corrected here (Round 2's own M6): a second WebSearch this revision identified it as 1955, superseding this candidate's own earlier "year not identified" note (Registry row 48 discharges the same correction; propagated here to match, *per CO-022's Naming and term propagation rule*) — a fix that had landed in the Registry but not, until now, in this operational document."

**New** (line 23): "Pellegrino's own year: a second WebSearch identified it as **1955** (Registry row 48 discharges **the same correction**)."

The 1955 date survives and Registry row 48 does carry it (verified: row 48 titles Pellegrino at "Alba: Edizioni Paoline, **1955**" and its Licensed-For reads "year and editor's first name both confirmed by a second search this revision"). But "**the same** correction" is now a bare demonstrative pointing at a correction the sentence no longer states — the banner it referred back to is the thing that was removed. Separately, `CO-022` falls from two mentions to one across the Manifest; the survivor is the Disposition paragraph's escalation clause, so the *Naming and term propagation* rule — the rule under which corrections are propagated between the Registry and this operational document — is now cited nowhere in the Manifest.

### L4 — Manifest G5 lost both markers that supersede its own named archive.org lead, while the request paragraph above still offers that lead; the Registry's parallel site was handled correctly

**Old** (line 41): "**Fulfilled 2026-09-08, *with a correction to this request's own named lead*.** With network access confirmed working, this build thread independently opened `histoirelittra00moncuoft` directly and found it is **not** Tome Premier at all — its own title page reads "TOME CINQUIÈME / SAINT OPTAT ET LES PREMIERS ÉCRIVAINS DONATISTES," 1920, already vendored on the sibling Donatism build's own branch. ***That lead is corrected here rather than used.*** Fresh search located…"

**New** (line 39): "**Fulfilled 2026-09-08.** With network access confirmed working, this build thread independently opened `histoirelittra00moncuoft` directly and found it is **not** Tome Premier at all — its own title page reads "…," 1920, already vendored on the sibling Donatism build's own branch. Fresh search located…"

Meanwhile G5's own request paragraph, new line 37, is untouched and still reads: "Freely hosted at the Internet Archive: **`archive.org/details/histoirelittra00moncuoft`** and `archive.org/details/histoirelitterai03monc_0`." A reader taking the identifiers from the request paragraph — which is what that paragraph is for — is no longer told at the point of the correction that the first one is the wrong volume and superseded.

**The comparison that makes this a finding rather than a preference:** the same fact, in `Source_Registry.md` row 56, was rewritten the *right* way in the same commit — the banner became an explicit standing warning: "(`histoirelittra01moncuoft`, `histoirelittra02moncuoft`, `histoirelitterai03monc_0` — **not** `histoirelittra00moncuoft`, which row 206's own Verification Note discloses is not vol. I at all but Tome Cinquième, 1920…)". Two documents rewritten in one pass gave the same fact opposite treatments, and the weaker one is in the operational document the project lead is meant to act from.

### L5 — Registry row 56 dropped the record that its Confidence was raised, a change this Registry elsewhere treats as CO-022-substantial

**Old** (row 56, Confidence cell): "| S | **B** **(raised from C** — public domain status *now* resolved rather than hedged, see Verification Note) |"
**New:** "| S | **B** (public domain status resolved rather than hedged, see Verification Note) |"

"Raised from C" is not correction-history in the banner sense — no round is attributed, and no earlier draft is described as wrong. It is the record that this row's Confidence rating changed. Row 33's Verification Note, unchanged by this pass, states the standard that makes that record matter: *"a Confidence-rating change is a substantial revision under CO-022 and is not self-applied post-disposition — flagged for that decision rather than for further second-opinion review."* Row 56's own Source-Check column still carries "extent/rights re-verified Round 4 fix pass," so the change is inferable and pre-dates the Round 14 disposition, which is why this is LOW rather than MEDIUM. But the Registry now records a B where it previously recorded a B-that-was-a-C, and it is the only row in the table that had such a record to lose.

---

## COSMETIC findings

### C1 — This commit re-staled the very sentence Round 26's C1 fix was written to cure, by the same mechanism, one commit later

`lpc_Decision_Log.md` line 330 (written at `9c1cc01` as the fix for Round 26's C1) reads: *"…Doc_02 §2's own pointer to "`lpc_Decision_Log.md`'s 2026-09-08 entry" was ambiguous among the four entries this log **then** dated 2026-09-08, **a count since grown to five** (C2)."*

Entry headings recounted at HEAD: `grep -c '^### 2026-09-08'` = **6**. This commit added the sixth. `git diff 9c1cc01 7bdb759 -- lpc_Decision_Log.md` is +14/−0, so line 330 was not touched — it was falsified by the new entry appended below it. Round 26's C1 fix correctly made the historical scope explicit ("then dated"), which is the durable half, but then pinned a live running count that the same fix pass's successor immediately broke. The Registry's three sibling instances ("the four entries this Decision Log dates 2026-09-01") are all gone, removed with their banners; 2026-09-01 is still four, so nothing was lost there.

### C2 — The disclosed 43-hunk diff-read covers the Registry only; the Manifest's own 24 hunks have no disclosed fact-preservation check, and that is where the findings are

The commit message states, unqualified: *"The full word-level diff (43 hunks) was read in full before committing, checking specifically for the Round 26 failure shape."* Recomputed with the exact command the Decision Log names: `git diff --word-diff=plain -U0 9c1cc01 7bdb759 --` gives **43** hunks for `Source_Registry.md`, **24** for `Source_Acquisition_Manifest.md`, **67** for both together.

The Decision Log's own placement is more careful — the sentence sits under the heading "**Independent verification of the subagent's own work**," which scopes it correctly to the Registry. But that leaves the Manifest, rewritten by the build thread itself, with only structural validation disclosed ("the run-aware sequential-pairing-versus-CommonMark bold-nesting test returns zero mismatches and zero literal survivals…; a case-insensitive search… returns zero hits") plus the bare assertion "No fact, figure, Registry-row reference, archive.org identifier, or acquisition detail was altered." Every one of those structural checks passes, and all of them look at what *survived*.

This is recorded as COSMETIC because it is a finding about the account rather than about the documents. It is worth stating plainly anyway: the half of this commit that received the briefed subagent, the worked "do not do this" examples and a 43-hunk diff-read carries **one** MEDIUM, one LOW and one COSMETIC across 212 rows; the half that received neither carries **one** MEDIUM, four LOWs and the pass's one false self-claim across 81 lines. The verification asymmetry and the finding distribution match exactly.

### C3 — The Registry's pre-edit word count is misstated by 34 in both the Decision Log entry and the commit message

Both state "Word count fell from **37,577** to 35,404 (about 5.8%)." Recomputed: `wc -w` on HEAD = **35,404** (exact), and on the pre-edit file = **37,611**. The 37,611 figure is stable across every commit the pre-edit Registry could have been taken from — `1e01153`, `acb3396`, `9f14783` and `9c1cc01` all return 37,611 — so there is no baseline at which 37,577 is correct. The true reduction is 2,207 words, **5.87%**, not the 2,173 / 5.78% the stated pair implies. Nothing downstream depends on the figure; it is recorded because this entry's own governing discipline is that a pass's account of itself is not itself verification, and this is the one arithmetic in it that does not reproduce.

### C4 — Eight Registry sites had the round attribution *trimmed* rather than removed, which is why the residue search returns zero — the same shape as Round 26's L1

The old Registry carried **37** occurrences of the exact phrase "independent review Round," across 21 lines. At HEAD it carries **0**, and the entry reports that as a clean result. But at **eight** of those sites the attribution was not removed, only shortened: the vendoring-provenance form "(2026-09-08, **independent review** Round 15)" became "(2026-09-08, Round 15)", uniformly across rows 40, 41, 56, 61, 78, 89, 90 and 99. The other 29 were genuine banner removals.

Keeping "Round 15" is defensible — it dates a vendoring event rather than narrating a correction, and the treatment is at least consistent. The finding is about the *check*, not the edit: a residue search keyed to "independent review Round" cannot distinguish a site where the banner was removed from a site where the two words were deleted out of the middle of it, so the zero-hit result is weaker evidence than the entry presents it as. This is exactly the mechanism Round 26's L1 named on Doc_02 — a verification search that cannot reach a site whose wording the same pass changed.

---

## Observation, not a finding: one class of correction-history was deliberately kept, and the rule is now applied at two different widths

`Source_Registry.md` new line 283 retains, verbatim and untouched: *"**Two corrections worth keeping as a record rather than as an enumeration:** row 42's Licensed-For was briefly widened to carry a vivid claim at Confidence C without this section being re-run (Round 3), then reverted (Round 4)… and row 65's Licensed-For was narrowed (Round 5)…"* This is round-attributed correction history of exactly the kind the standing rule sends to `lpc_Decision_Log.md`, surviving because it does not use any of the three phrases the pass searched for and because its own text argues for keeping it.

That may well be right — it is a caution about how a row can move across a governing rule without the rule's own text changing, which is a live methodological point rather than a record of a fixed error. It is recorded here only so the width of the rule is on the record: after this pass, `Doc_02_Source_Ecology.md`, `Source_Registry.md` and `Source_Acquisition_Manifest.md` are consistent in having no banners of the stripped form, and inconsistent in whether round-attributed history survives at all. Which width is intended is the project lead's call, not this round's.

---

## CO-022 escalation-category assessment

**1. Representative identity.** Nothing in this round touches Representative identity. Neither rewrite changed a claim about what this world is, whom it speaks for, or what its sources license — this round independently confirmed that every archive.org identifier, vendored file path, Registry row citation, Confidence letter, Boundary Status and Exclusion Reason in the old text survives in the new. M1 concerns a session's own network-access status and three internal pointers; M2 concerns a review-history data series; M3 concerns where a disposition record lives; the LOW and COSMETIC findings concern provenance lines, dangling referents, a Confidence-change record, and the accuracy of the pass's own account of itself. **Not an escalation.**

**2. Portfolio-level or cross-world strategic decisions.** One finding touches cross-world matter and does not decide anything for another world: L4 concerns how this Manifest supersedes its own named archive.org lead for a Monceaux volume already vendored on the sibling Donatism build's branch — a statement lpc makes about its own request, not an action on that branch. Round 26's L2 sibling, the Donatism build's own five-failed-attempts acquisition history at Registry row 44, was checked specifically this round and **survives intact**. Nothing in this round proposes any change to another world's files. **Not an escalation.**

**3. Governance or methodology decisions.** The rewrite is governance-adjacent — a change to how this world's build documents are written — but it is the project lead's own direct instruction, extending a rule the prior entry had already disclosed as standing, and this round does not disturb it. This round proposes no change to CO-022, `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CF V7.4, or any governing document. M3 is a broken pointer, not a proposal about the *Disposition* rule — and this round expressly does not reopen the conjunctive/disjunctive question Round 26 left open at its own M1, which the Round 26 fix pass resolved by grounding the disposition in the project lead's own direct authority rather than in either reading. L5 observes that a Confidence-change record was dropped; it does not propose changing any Confidence letter or the rule governing them, and the row's rating is unchanged. C2 and C4 are findings about a verification method's reach, applied against a standard this document set already holds itself to. The one genuine methodology question this round surfaces — how wide the banner-stripping rule should run, given that one class of round-attributed history was deliberately kept — is recorded above as an observation and expressly left to the project lead rather than answered here. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on a point of fact. Every figure it re-derives agrees with the round or the entry that stated it — the HIGH sequence 6/2/1/1/0/0/0/0/0/0/0/0/0/0 and MEDIUM sequence 15/6/7/4/9/9/2/2/1/2/1/1/1/0 both reproduce exactly against the fourteen artifacts' own `Findings:` lines, matching Rounds 9, 10, 11, 13, 14 and 18; the 212-row structure, the 448 bold-bearing lines, the Manifest's own word and bold counts, and both disclosed "improvements" all reproduce. The single arithmetic disagreement (C3, the Registry's pre-edit word count) is a recomputation against the file itself at four separate commits, not a disagreement with a reviewer. M2 puts this round in agreement with Round 9's remedy and in disagreement with the *pass*, not with a review. M3 agrees with Round 26's M2 and finds it under-applied. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Whether this round's findings change either document's status line, and what disposition follows, is **not assessed here**, per CO-022's rule that the build thread applies its own disposition. Per the project lead's own standing instruction recorded in both 2026-09-08 banner-stripping entries, these findings are shown before any fix is applied; nothing in this artifact has been fixed, and no file other than this one was written.

**Three observations, stated without weighing them.**

First: **the Registry rewrite's core claim is true, and it is the strongest result of its kind in this document set's record.** Of the 43 Registry hunks, only two carry a substantive finding — hunk 1 (the Status line, M2 and M3) and the row 56 hunk (L5); the eight hunks behind C4 carry a finding about the pass's own verification search rather than about the text they produced, and the remaining 33 carry nothing at all. The atom-level sweep found not one identifier, date, row number, locus, imprint year, file path or figure lost outside a banner; and every one of the twelve structural self-claims about the table reproduces exactly, including the byte-identical physical row order. Against Round 26's finding that six of eight Doc_02 defects were facts deleted with their banners, a briefed subagent working cell by cell from worked examples produced, at 212 rows and 2,207 words removed, **zero** instances of that failure mode. The method worked.

Second: **the findings cluster precisely where the verification did not reach.** Both of this round's document-level MEDIUMs, four of five LOWs, and the pass's one false self-claim are in `Source_Acquisition_Manifest.md` — the file that got no disclosed diff-read — or on the one Registry line whose non-table content the subagent's row-by-row brief did not cover. The Registry's 43 hunks were read; the Manifest's 24 were not; the findings follow that line almost exactly.

Third: **every substantive finding is again a deletion, not an alteration — with one exception.** No fact in either new document was found to be *wrong* against a source. M1, M2, M3, L2, L3, L4 and L5 are all of the form "something true was removed, or something pointing at it was left behind." The exception is **L1**, where "that round" became "this round" while the round was being deleted — the only place in 67 hunks where the rewrite changed a claim's meaning rather than dropping it. As Round 26 observed of its own pass, a deletion pass cannot verify itself by looking at its own output; both this round's MEDIUMs in the Manifest were reachable only by diffing against the prior text, and M3 only by following a pointer out of the file.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC.**
