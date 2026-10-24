Simulated review — informational only, not an Article 31 substitute.

# Doc_08: Phase L0 item A, check of the generator findings and the unreviewed Round 8 revision

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Opus 5.0
- **Drafter model provenance:** `lpc_Decision_Log.md` (entry "2026-09-15 (seventh)") records the drafting but names no model, and `build/lpc_Build_State.yaml` leaves `drafter_model` blank for Doc_08. The model is taken from `Doc08_Round9_Targeted_Check_2026-09-29.md`, which read the "Claude Opus 5" trailer on draft commit `9eccc532`. That commit is not in this shallow checkout, so I could not re-read the trailer myself.
- **Reviewer agent:** independent review subagent, session_01PdSKYEGnPNVAntVFg5ZReR (fresh context; I wrote nothing under review)
- **Drafter agent:** lpc build thread (draft: session_0154L7Jqjwb9mt9pQGDUs2dv, per the Round 9 check; the Round 8 fix-pass session is not recorded)
- **Round:** 10 (the tenth Doc_08 review-type file on disk; a Phase L0 check, not a revision round)
- **Truncation check, method 1:** I compared each file's byte count on disk with its HEAD blob size (`git cat-file -s`). Doc_08: 74717 = 74717 bytes, 478 lines. Index: 19338 = 19338, 156 lines. Generator: 49543 = 49543, 841 lines. Round 8 review: 63159 = 63159, 475 lines. These match the sizes the Round 9 check recorded, so none of the four files has changed since 2026-09-29.
- **Truncation check, method 2:** I checked each file's end marker and counted its structural elements. Doc_08 ends in the "build-cycle position" paragraph of its Disposition and has 9 `## Section` headings and 17 `#### Force` headings. I read it in two pages (lines 1–386 and 387–479), which cover the whole file. The Index ends in its Disposition line. The generator parses with `ast.parse` and ends in its two `print` calls. The Round 8 review ends "*End of Round 8 review.*"
- **Date:** 2026-10-23
- **Scope:** `scripts/gen_force_index.py`, `lpc_Force_Index.md`, `Doc_08_Forces_Document.md` (read in full), `Doc08_Round8_Review.md` (verdict and findings), `Doc08_Round9_Targeted_Check_2026-09-29.md`, `Open_Gaps_Tracking.md` (Doc_08 entry, OG-3, OG-22), `build/lpc_Rebaseline_Declaration.md`, the 17 `records/lpc/force/` records, the 8 `records/lpc/gravity/` records, `lpc.limit.411-gesta-unread`, and Doc_09's references to Doc_08. I re-verified the quotations against `cic/texts/` and against the governing documents.
- **Counting note:** the caller set this file's name. It carries "Doc08" and "Check", so `engine/m10/rounds.py` counts it as a Doc_08 review file. The re-baseline declaration recorded 8 review files. With the Round 9 check and this file there are now 10. The generator globs only `Doc08_Round*_Review.md`, so this file does not change its output.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 9 LOW, 2 COSMETIC.** All of these are for the project lead. Severity maps to the Standard Practice tiers as HIGH = P0, MEDIUM = P1, LOW and COSMETIC = P2.

**The answers in short.**

1. **Does the Index match Doc_08?** Yes, exactly: 17 forces, every ID, every cell, every confidence level, all 15 §4 connections and all 8 gravity rows.
2. **Is the unreviewed Round 8 revision sound?** Its forces content is sound and sourced. The generator and the certification text are not. Both HIGH findings from the Round 9 check still reproduce, and both can print a false disposition with exit 0.
3. **Does any open finding change a downstream record?** No open finding changes a force record's gravity links, its force links or its confidence. Two findings do reach downstream text: the 411 *Gesta* framing (M3) and the transmission interval at 2B-5 (M5).

---

## Question 1: does the Force Index match Doc_08?

**Yes, byte for byte.** I copied Doc_08, the generator and the `Doc08_*` review files into the scratchpad. I then ran the generator there, passing the scratch folder as `argv[1]`. It exited 0 and reported "17 forces, 15 connections, 8 gravities". `diff` against the committed `lpc_Force_Index.md` showed no differences, and the sha256 begins `3cdfc0f2` on both. `git status` stayed clean. I did not run the generator in the repo, because it writes `lpc_Force_Index.md`.

**I also checked the Index by hand against Doc_08 itself**, so that the match does not rest on the generator alone:

- **Forces and IDs.** The 17 `#### Force` headings give 1A (2), 1B (3), 2A (4), 2B (5), 3A (1) and 3B (2). The Index master table, Doc_08 §9 and §7 all give the same IDs and the same distribution.
- **Gravity links.** Each Index §3 row equals the §5 list for that gravity. G4's five forces come from expanding "every force in Cell 2A", which is right. Each force's own Layer 3 names the gravities §5 assigns it. The only gaps are the five forces carried in §5 alone (2A-1, 2A-2, 2A-3 and 2A-4 for G4, and 2A-2 for G1), and the Index lists all five as observations. 2B-3, 2B-5 and 3B-2 carry no gravity, as in §5.
- **Classes.** G1, G2, G3 and G6 are Primary. G4, G5 and G7 are Supporting. G8 is Tensional. These agree with Doc_08 §1 and with the eight gravity records.
- **Confidence.** 14 forces are Documented and 3 are Widely Accepted (1A-2, 1B-3, 3B-1). 2B-3 also carries a Contested secondary element. §3, §7 and the Index all agree on this.

---

## Question 2: is each unreviewed Round 8 change sound and sourced?

### What is sound

- **The forces content.** I verified every quotation that Doc_08 attributes to a vendored source, comparing the text with whitespace, line-end hyphens and apostrophe forms normalised:
  - In `anf05`: "chiefly wounded", "your suffrage and God's judgment", "ancient venom", the Pontius "neophyte" sentence, "thousands of certificates were daily given", "these thirteen letters", "you always read my letters", "matter, and even the paper itself…", "as it actually came to hand… Crementius the sub-deacon, to carry", and the Roman clergy's "send a copy of this letter".
  - In `npnf104`: "even of the plenary Councils…".
  - In CSEL 36: the *Retractationes* Prologus reads "sine in libris siue in epistulis siue in / 5 tractatibus cum quadam iudiciaria seueritate…" and "uelut censorio stilo". This is the emendation Doc_08 discloses, plus a margin line number.
  - In Weiskotten's Possidius, ch. VIII: "all who heard rejoiced and clamored…" and "under com-/pulsion and constraint he yielded".
  - From the governing documents: the Forces Framework V1.1 lines ("This is not optional…", "Where even inferential reconstruction is unsupported…", "A gravity that cannot be connected…"), the carve-out in the L4 template, and the Doc_02 and Doc_04 lines on Candidate 2, Candidate 5 and Candidate 6.
  
  The exceptions are listed at L7 and C2.
- **Generator changes that hold.** I tested these with fresh mutants in the scratchpad:
  - `[FURTHER CORRECTION, Round 9. …]` on the G6 line now halts, through `assert_no_notices`. Round 8's H1 live form is closed.
  - The §4 duplicate-row and certified-count guards hold.
  - The Status line renders `LATEST_FIX_PASS`.

### HIGH

**H1. Round 8's H2 is still open, and Doc_08's Disposition says it is fixed (Round 9 H1, confirmed again).**
- **What I ran.** In the Round 8 artifact I replaced `## VERDICT: SUBSTANTIAL REVISION REQUIRED` with a bare `## VERDICT`. I then added "Round 7 was **CLEARED** on the analysis." before the real verdict. The generator exited 0. The Index Disposition printed `Doc08_Round8_Review.md` (2H 5M 6L 1C, **CLEARED**), and the review-history line printed "Round 8: CLEARED".
- **Cause.** `verdict_counts` still takes the first verdict word in its window.
- **The false claims.** Doc_08 Disposition line 474 says this was "a defect now fixed". It also says "each correction marked in place", but the inline notices were removed and the generator now halts if any exists. Both statements are false in a canonical file.

**H2. `parent_disposition` treats any mention of "approved to proceed" as an approval (Round 9 H2, confirmed again).**
- **What I ran.** I set the Status line to "REVISED after Round 8 … not yet Approved to proceed." I set the Disposition to "**Not disposed.** This document has not been Approved to proceed." The generator exited 0. The Index printed `**Status:** **Approved to proceed**, inherited from…` and `**Approved to proceed, 2026-09-15**, together with…`.
- **Why it matters.** This is a false disposition, printed in the two places a disposition is read from. The committed Index is correct only because Doc_08 really is approved.

### MEDIUM

**M1. The correction-notice channel is narrower but still open (Round 9 M1, confirmed again).**
- **What I ran.** I put `[CO-022, 2026-09-15 — also **3A-1**]` on §5's G6 line. The generator exited 0, and the Index G6 row printed `2A-3`, `2B-1`, `2B-4`, `3A-1` (4 forces). That is a false force–gravity link.
- **Cause.** `_TAG` and `DETECT` admit no digits or hyphens. CO-022 is a live token in Doc_08.
- **Effect on the Index text.** Control (F), "a build-process notice anywhere in Doc_08 halts the run", is stated more broadly than the code implements it.

**M2. The Index's controls paragraph claims what the committed code cannot back (Round 9 M2, confirmed by reading the code).**
- "Thirteen … re-derived by exit code each run" is a literal at generator line 775. No control harness is committed.
- Control (F) is described twice, and the two descriptions contradict each other: "halts the run", then "is stripped".
- The second list of controls stops at (I).

**M3. The 411 *Gesta* is presented as unread, open, and a possible support for G5 (Round 9 M3, confirmed again).**
- **What the record says.** Doc_04 line 212 reads "CLOSED AS A PERSISTENCE QUESTION, 2026-09-15". Doc_08 §5 gap 3, §9 item 2 and the Disposition still frame the *Gesta* as unread and open.
- **Downstream reach.** The framing has spread:
  - `records/lpc/gravity/lpc.gravity.conciliar-authority-theory.md` says the *Gesta* "remain unread … It remains open". The Doc_04 independent check already flags this record (its N1).
  - Doc_09 lines 110 and 137 cite Doc_08 §9 for "unread".
  - `lpc.limit.411-gesta-unread` ("has not been validly read") is accurate as written, but its id carries the same framing.
- **Who decides.** G5's Supporting class is not affected. The correction should follow the project lead's ruling, as Round 9 advised.

**M4. §8 describes "[ADDED …] provenance clauses" as "retained deliberately", but none exists (Round 9 M4, confirmed again).** The generator's `assert_no_notices` passes on the live Doc_08, which it could not do if any such clause were present. The five-hit and six-hit figures in line 399 therefore describe an earlier text.

**M5. New. Wrong interval in 2B-5's Layer 2, carried into the force record with a different wrong figure.**
- **The error.** Doc_08 line 205 says "A century and a third later" for the step from Cyprian's dossier to Augustine's *Retractationes*. The dossier letters date from 250 to 258. The *Retractationes* date from "near the end of his life", c. 426–427 (Augustine died in 430). The interval is about 170 years. The 133 years in the text is this world's 258–391 silence, applied to the wrong pair of dates.
- **Downstream.** `records/lpc/force/lpc.force.transmission-institutionally-dominant-side.md` re-renders the phrase as "A century and a half later". That is also short, and it differs from its own source document.
- **Why MEDIUM.** It is a factual error in world-voice text that has reached a record. The fix is a wording change at both sites, not a redraft.

### LOW

- **L1. (Round 9 L1, confirmed by reading.)** The Index and generator line 801 still say "emphasis-dense". The comment at lines 95–97 still says "the force-ID pattern". Neither test exists.
- **L2. (Round 9 L2, confirmed by reading.)** Index line 8 calls the review-history line "re-verified by nothing". Index line 4 and Doc_08 line 12 call it derived.
- **L3. (Round 9 L3, confirmed again.)** I deleted the 2B-5→3B-2 row and changed §8 to "Fourteen". The generator exited 0 and printed "**14 connections**" against §9's "fifteen". Nothing reads §9.
- **L4. (Round 9 L4, carried; not re-run.)** The review-history guard misses some claim forms.
- **L5. (Round 9 L5, partly confirmed.)** With no review artifacts present, the generator now exits 1 on the history guard before it reaches the `KeyError`. That fails safe, but the message names the wrong cause. `--help` and the `[CSEL 1868]` misdiagnosis are carried, not re-run.
- **L6. (Round 9 L6, confirmed again.)** `tools/check_live_commentary.py --surface worlds` gives the same results as before: Doc_08 REWRITE ×3 and ROUTE ×2, Index REWRITE ×1, generator REWRITE ×75. These are live and canonical surfaces under CLAUDE.md. I flagged them and did not touch them.
- **L7. New. One quotation has a word added.** Doc_08 §2 quotes Doc_01 §6 as *"not Layer-1 documentation in the Forces Framework's **own** formal sense."* Doc_01 line 132 reads "in the Forces Framework's formal sense". The word "own" is not in the source.
- **L8. New. Stale citation.** The Disposition cites `CiC_Record_Native_World_Build_Process_V1_3.md` for "Do not create new workbooks." No V1.3 exists on disk. The words are in `Archive/Superseded-Method/CiC_Record_Native_World_Build_Process_V1.9.md` line 283, and V2.0 line 768 holds the same rule. The substance is unaffected.
- **L9. New. A downstream claim about review.** Doc_09 line 11 says Doc_01 to Doc_08 are "all complete and independently reviewed". Doc_08's Round 8 revision has never been reviewed, as Doc_08 itself says.

### COSMETIC

- **C1. (Round 9, confirmed again.)** The comment says "The five known tags", but `KNOWN_TAGS` has seven.
- **C2. (Round 9, confirmed again.)** Doc_04 line 195 ends "…not 2's own continuation — see §3, §5)". Doc_08 lines 161 and 334 close the quotation at "continuation)" with no ellipsis.

---

## Question 3: does any open finding change a downstream record?

- **Force records (17).** I extracted each record's `formation_confidence` and its `relations` to gravities and forces. All 17 match the Index exactly: gravity sets, cross-cell partners in both directions, and confidence, including the Contested placement note in 2B-3's `divergence_note`. **No open finding changes any of them.** The one text defect is M5, the interval in the 2B-5 record.
- **Gravity records (8).** The force lists and classes match Index §3 exactly. The one text defect is M3, the *Gesta* framing in the G5 record.
- **Doc_09.** Its two Doc_08 citations on 2B-5 and 3B-2 match Doc_08. It inherits M3 at lines 110 and 137, and L9 at line 11. No story, tier or index row depends on a generator finding.
- **The generator findings (H1, H2, M1, M2, L1–L5, C1)** change no record. They are risks of false output, not errors in what is committed.

---

## For the project lead

1. **The review cap.** Doc_08 now has 10 review-type files against a cap of 3. The Round 9 check offered three ways to close, (a), (b) and (c), and recommended (b): fix H1 and H2 as one-line code changes, cut the control and closure text down to what the code derives, and register the rest as `ACCEPTED_OPEN` against OG-3. I agree, because nothing found since 2026-09-29 changes that picture. The choice is yours.
2. **M3 and M5 are text corrections that reach records.** M3 is the *Gesta* framing in Doc_08, Doc_09 and the G5 record. M5 is the 2B-5 interval in Doc_08 and in its record. Each would be one named change order. M3 should follow your *Gesta* ruling.
3. **OG-3 remains partly stale.** Round 8's H1 live forms are closed, and its H2 is open. The Round 9 check first reported this. I did not edit `Open_Gaps_Tracking.md`.

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 9 LOW, 2 COSMETIC.**
- The Index matches Doc_08 exactly.
- The forces analysis and its sources hold, apart from M5, L7 and C2.
- No open finding changes a force record's links or confidence.
- Both HIGH findings are reproducible paths to a false disposition, and both are routed to you under the review cap.

*Simulated review — informational only, not an Article 31 substitute.*
