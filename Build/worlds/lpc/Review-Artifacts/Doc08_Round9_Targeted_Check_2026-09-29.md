Simulated review — informational only, not an Article 31 substitute.

# Doc_08 — Round 9 targeted independent check of the unreviewed Round 8 revision

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Opus 5.0
- **Drafter model provenance:** the draft commit `9eccc532` carries the trailer "Claude Opus 5", recorded above as Opus 5.0. The Round 8 fix-pass commit lies outside this shallow checkout. Neither Doc_08 nor `lpc_Decision_Log.md` records its drafter model. Later live-surface edits to Doc_08 carry "Claude Sonnet 5" (`b73abfd2`, `28e35b19`) and Opus 5.5 (`45aa2333`).
- **Reviewer agent:** independent review subagent, session 7ead543b (fresh context, no authorship of anything reviewed)
- **Drafter agent:** lpc build thread (draft: session_0154L7Jqjwb9mt9pQGDUs2dv; Round 8 fix-pass session not recorded)
- **Round:** 9 (targeted check, not a new revision cycle)
- **Truncation check, method 1:** byte count on disk compared with the HEAD blob size from `git cat-file -s`, for all four inputs: Doc_08 74717 = 74717 bytes (478 lines); Index 19338 = 19338 (156); generator 49543 = 49543 (841); Round 8 review 63159 = 63159 (475). Doc_08 was read in two pages (lines 1–386 and 386–479), which together cover the whole file.
- **Truncation check, method 2:** structural end markers and element counts. Doc_08 ends in its Disposition "build-cycle position" paragraph, has 9 `## Section` headings and 17 `#### Force` headings. The Index ends in its Disposition line. The generator parses with `ast.parse` and ends in its two `print` calls. The Round 8 review ends with "*End of Round 8 review.*"
- **Date:** 2026-09-29
- **Scope:** `Doc_08_Forces_Document.md`, `scripts/gen_force_index.py`, `lpc_Force_Index.md`, `Doc08_Round1–8_Review.md` (Round 8 read in full), `Open_Gaps_Tracking.md` (Doc_08 status entry and OG-3/OG-4).
- **File name:** this file deliberately does not match `Doc08_Round*_Review.md`. The generator globs that pattern and would halt against Doc_08's "Eight" claims. `engine/m10/rounds.py` does not count this file either. The Doc_08 count is already 8 against a cap of 3, so leaving it out changes no routing. It is named here so that nobody reads it as hidden.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 4 MEDIUM, 6 LOW, 2 COSMETIC.**

Severity mapping to the Standard Practice tiers: HIGH = P0, MEDIUM = P1, LOW/COSMETIC = P2.

**The forces analysis is sound.** Nothing below touches it. **Every value in the committed `lpc_Force_Index.md` is correct today.** Both HIGH findings are false statements the generator *can* emit with exit 0, plus one false closure claim already sitting in Doc_08's Disposition. This is the ninth round on this document and the review cap is three. The residual pattern needs a decision from Mark, not a tenth round (see **For Mark**).

---

## What I confirmed clean

- **Faithful generation.** I ran the committed generator on a scratch copy (Doc_08 plus the eight `Doc08_Round*_Review.md` files) with the base path passed as `argv[1]` and the working directory set to `/`. It exits 0 with "17 forces, 15 connections, 8 gravities". The output is **byte-identical** to the committed Index: sha256 `3cdfc0f2…ffeae1c34` on both. No committed file was touched.
- **Cross-cell map.** All 15 §4 rows appear in Index §4 with source, destination and direction intact. That count covers one deliberate non-connection (`2A-2`) and one coincidence (`3A-1` → `3B-1`). The master-table → / ← columns are the correct inversion of those rows. `1B-3` correctly shows no §4 row.
- **Gravity linkages.** Each Index §3 row matches the §5 lists force for force. G4's five forces come from the "every force in Cell 2A" expansion, and that expansion is right. All eight classifications match Doc_04 §4. **Candidate 5 (G5) is Supporting in Doc_08 §1, §5 and Index §3**, matching Doc_04 §4 and §7 items 2 and 7. Its three forces (`1B-1`, `2A-3`, `2B-4`) are carried as indirect, not as organizing. §6 reports no contradictions, §7 agrees at all 17 forces, and the §3-against-§4 check is clean.
- **Doc_04 quotations used for the `2B-1`/G6 relation.** All verified at Doc_04 §3 (Candidate 2's and Candidate 6's Interaction lines) and §6. The claim that the "this document's own reading" hedge sits on exactly two matrix cells is correct: I counted 2.
- **Vendored-source spot check.** Thirteen quotations match verbatim, ignoring whitespace and typographic apostrophes, and none falls inside a `<note>` span. The containing-work headings were recovered from `anf05` `div3` titles. The Cyprianic transmission quotations sit in Cyprian's own letters. The copy instruction sits in "From the Roman Clergy to the Carthaginian Clergy", which is how Doc_08 attributes it. "Chiefly wounded" is from *On the Lapsed*. The plenary-councils line is in `npnf104`. The *Retractationes* Prologus reads "sine in libris siue in epistulis siue in / tractatibus…", exactly the emendation Doc_08 discloses, and "uelut censorio stilo" is present. Possidius ch. VIII: "all who heard rejoiced…", "under com-/pulsion and constraint he yielded" (Latin *compulsus atque coactus*).
- **Round 8 findings now closed**, each tested with a mutation (harness in scratchpad; one fresh copy per mutant):
  - H1's live forms `[FURTHER CORRECTION, Round 9.]` and `[SUPERSEDED, Round 9: …]` now halt. So do colon, semicolon, parenthesis, en-dash, three-word and 16-letter tags. The new `assert_no_notices` rule (no notice in a deliverable at all) is a real structural improvement.
  - M1: a dropped trailing pipe, a deleted row and a `From`-prefixed row all halt against the certified 15. A duplicated row halts.
  - M3: the Status line renders `LATEST_FIX_PASS`, and "REVISED after Round N" is checked against the fix-pass ordinal.
  - M2, in part: per-round counts in Doc_08 are now compared with each artifact.

---

## HIGH

### H1 — Round 8's H2 is still reproducible, and Doc_08's Disposition says it is fixed.

**Mutant.** Round 8's own H2 mutant, applied to the Round 8 artifact. The heading becomes a bare `VERDICT`, then "Round 7 was **CLEARED** on the analysis.", then "This round: **SUBSTANTIAL REVISION REQUIRED**." The generator exits 0 and emits this Index Disposition:

> the most recent `Review-Artifacts/Doc08_Round8_Review.md` (2H 5M 6L 1C, **CLEARED**)

The review-history line also switches to "Round 8: CLEARED". `verdict_counts` now searches `window` rather than `t[i:i+200]`, but it still takes the **first** verdict word in that window, so a recital of an earlier round still wins. The same first-match path on the counts is caught now, and a fenced heading is caught too, but only incidentally: the per-round count comparison with Doc_08 halts both, while nothing compares verdict *words* per round. The one verdict-word check, `all N returning X`, runs only when every artifact carries the same verdict, so it goes silent in exactly this case.

**False claim already in a canonical file.** Doc_08's Disposition, line 474, says: *"the generator could, **on a defect now fixed**, have printed a false clearance in the Index's own Disposition."* Two sentences later it says: *"All findings from all eight rounds are addressed above or in the Index, each correction marked in place."* Both are false:
- Round 8's H2 is reproducible as shown.
- M5, L2, L5 and C1 are untouched (see L1, L2, L5 and C1 below).
- No correction is "marked in place". The inline notices were removed, and the generator now halts if any exists.

**Why HIGH.** The Disposition is the section a disposition is read from. Round 8 graded this output HIGH, and it now comes with a closure claim attached.

**Fix, for whoever is assigned.** Report ambiguity when the verdict window contains more than one verdict word. Compare each `Round N` verdict word in Doc_08 with `_VC[N][1]`. Restate the two Disposition sentences at their true strength.

### H2 — `parent_disposition` counts a bare mention of "approved to proceed" as an approval. A not-disposed Doc_08 is rendered "Approved to proceed" in the Index's Status and Disposition, exit 0.

**Site.** `gen_force_index.py` lines 128–154, which were added in the unreviewed Round 8 revision. `APP = re.compile(r"approved to proceed", re.I)` is searched anywhere in the Status line and anywhere in the Disposition section.

**Mutant.** Status set to "REVISED after Round 8 — the revision is unreviewed; not yet Approved to proceed." Disposition set to "**Not disposed.** This document has not been Approved to proceed; …". The generator exits 0 and the Index prints `**Status:** **Approved to proceed**, inherited from …` and `**Approved to proceed, 2026-09-15**, together with …`. That is a false disposition, printed in the two places a disposition is read from.

**The mirror case is already live.** Run on the pre-fix draft at `9eccc532`, which I recovered by fetching the full SHA, the generator halts with "Status line says NOT approved while its Disposition section says Approved to proceed". That draft's Disposition says "Not disposed" and only *mentions* the phrase ("requires a document to reach at least *Approved to proceed*"). This same false positive is what stops control (A) from running (see M2).

**Why HIGH.** It produces a false approval with no guard firing: the self-certification-by-accident outcome Round 8 warned about. The committed Index is correct only because Doc_08 really is approved.

---

## MEDIUM

### M1 — The notice channel is narrower but still open. Five forms still put a false force–gravity connection into the Index, exit 0. Control (F), "a build-process notice anywhere in Doc_08 halts the run", is stated more broadly than it is implemented.

The mutant plants each form on §5's G6 line with `**3A-1**` inside the bracket. Each one emits G6 as `2A-3, 2B-1, 2B-4, 3A-1` (4 forces), exit 0:
- `[CO-022, 2026-09-15 — …]`
- `[CORRECTED at R7 — …]`
- `[R8-FIX, 2026 — …]`
- `[Doc08-R8 — …]`
- `[CORRECTED.2026 …]` and `[CORRECTED/2026 …]`

The first two are Round 8's own listed mutants. `_TAG` admits no digits or hyphens, and `_SEP` has no "word, then dash" form. `DETECT` shares both limits, so it is not wider on the axis these forms exploit. The class risk is lower now that deliverables carry no notices by rule, and `CO-022` is a live token in this document.

### M2 — The Index's controls paragraph makes claims the committed code cannot back.

- *"There are **thirteen** … The count is re-derived by exit code each run, not copied."* This is a hard-coded literal at generator line 775. No control harness is committed anywhere in the repo, so nothing re-derives anything.
- **(A)** cannot run against the committed generator. It halts on H2's false positive, and with no review artifacts present it crashes (`KeyError: 0` at line 835, `_VC[LATEST]`). To check the claim itself, I bypassed both in a scratch copy. The detection logic does then reproduce the advertised result: contradictions `1B-1`/G2, `2A-1`/G8 and `2B-1`/G7, and three missing Layer 2 entries. The finding is that (A) is not reproducible as the Index describes it, not that it is wrong.
- **(F)** is described twice, and the two descriptions contradict each other: "halts the run", then "is stripped and its planted ID does not reach the tables". A heading-form `[ADDED, …]` notice halts, so the second description is false.
- The second enumeration of the controls still stops at (I). This is Round 8's L1, unaddressed.

### M3 — Doc_08 presents the 411 *Gesta* as unread and open, and as a possible support for G5. Doc_04 and OG-4 record that question as closed.

**Sites.** §5 "Where Forces Analysis Surfaced Gaps" item 3: *"remains unread (Doc_04 §7 Open Item 6), and it is the one unexploited source that could bear on G5's force-connection"*. §9 outstanding item 2: *"is unread"*. The Disposition: *"Unresolved tensions: one open — the 411 Gesta"*.

**What the record says.** Doc_04 §7 item 6 now reads **"CLOSED AS A PERSISTENCE QUESTION, 2026-09-15"**, and says that reading the *Gesta* to support Candidate 5 *"is the precedent's named failure mode"*. Two reads were made and both were withdrawn (`Doc04_Gesta_Targeted_Read_2026-09-14.md`). OG-4 calls this "a closed decision, not an open question". So "unread" is inaccurate, and "could bear on G5" points readers toward the path the governing precedent forbids. G5's Supporting classification is not affected.

### M4 — §8 describes provenance clauses that no longer exist.

Doc_08 line 399 says the `[ADDED …]` provenance clauses *"are retained deliberately, so the marker's own history is auditable at its site"*, and computes a five-hit versus six-hit residue that includes them. No such clause exists in Doc_08, and `assert_no_notices` would halt if one did. The paragraph is headed "Checked rather than asserted", but its figures describe an earlier text.

---

## LOW

- **L1 — Round 8's M5 is untouched.** Index §6 and generator line 801 still say (G) halts on an *"emphasis-dense"* span. The comment at lines 95–97 still says `STRUCTURAL` carries *"the force-ID pattern"*. Neither test exists.
- **L2 — Round 8's L2 is untouched, and the two deliverables now disagree.** Index line 8 lists the Status line, Review-history line and Disposition as "hard-coded prose, re-verified by nothing". Index line 4 and Doc_08 line 12 both say the review-history line is derived.
- **L3 — §9 is still read by nothing.** The certification regex matches only number-before-"connections", so it reads §8's "Fifteen connections" and never §9's "— fifteen". Mutant: delete one §4 row and change §8 to "Fourteen". The Index prints "**14 connections**" against §9's *fifteen*, exit 0. §9's cell distribution also stays unread (mutated to a wrong distribution: exit 0, no output).
- **L4 — The review-history guard is still narrower than "every claim form is matched".** These pass with exit 0: "Three rounds of independent adversarial review"; a Document Log row's verdict changed to **CLEARED**; the Round 3 and Round 4 Log rows deleted; "run **twice**".
- **L5 — Robustness.** `--help` dies in a raw `FileNotFoundError`, and no review artifacts means a `KeyError`. A legitimate bracketed citation (`[CSEL 1868]`) halts with a message calling it a "build-process notice". That fails safe, but the diagnosis is wrong.
- **L6 — Commentary on a live surface** (CLAUDE.md, "Keep the live/canonical surfaces clean"). `tools/check_live_commentary.py --surface worlds` reports:
  - Doc_08: REWRITE ×3 and ROUTE ×2, at lines 217, 334, 358, 399 and 405.
  - Index: REWRITE ×1, at line 4.
  - Generator: REWRITE ×75, mostly the change-history comment blocks at lines 21–65 and 172–205.
  
  Line 334 narrates Round 3's error and cites "the same pass whose notice certified…", a notice that no longer exists. Flagged, not touched.

## COSMETIC

- **C1.** The comment at generator line 31 says "The five known tags". `KNOWN_TAGS` has seven.
- **C2.** Doc_04 §6's 2×7 cell ends "…not 2's own continuation — see §3, §5)". Doc_08 lines 161 and 334 quote it closed at "continuation" with no ellipsis.

---

## For Mark — what a single round cannot close

1. **The cap is long past.** This is round 9 against a cap of 3, and `rounds.py` already reports `roundcount-cap` for Doc_08 at 8. Every round since Round 5 has cleared the analysis and found new defects in the generator's *self-description*. Both HIGHs above are the same failure shape: a control, or a closure claim, stated more broadly than the code behind it. A tenth fix-and-review cycle is the pattern the cap exists to stop. The options:
   - **(a)** Another fix pass on the generator, plus a targeted recheck.
   - **(b)** Fix the two HIGHs as one-line code changes. Strip the Index's control narrative and Doc_08's closure sentences down to what the code derives. Register M1–M4 and L1–L6 as `ACCEPTED_OPEN` against OG-3.
   - **(c)** Retire the self-certifying prose entirely. The Index would carry only derived tables, and the generator would be treated as build tooling rather than a deliverable. This also answers the portfolio question Round 8 raised about where generators live.
   
   **Recommendation: (b).** It closes the only two false-output paths and stops paying for prose audits. The choice is yours.
2. **M3 (the *Gesta* framing)** conflicts with a closed project-lead ruling. Correcting it is a text change, but it touches how G5's gap is presented, so it should follow your ruling rather than a build-thread judgement.
3. **OG-3's status line** ("Round 8's own HIGH findings stand unfixed") is now partly stale. Round 8's H1 live forms and M1 are closed; its H2 is not. This review does not edit `Open_Gaps_Tracking.md`; that update is for the build thread.
4. **Where this file goes in the count.** Decide whether this check should count as a Doc_08 round. If it should, renaming it to `Doc08_Round9_Review.md` will make the generator halt until Doc_08's "Eight" claims are updated.

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 4 MEDIUM, 6 LOW, 2 COSMETIC.** The forces analysis is sound and the committed Index is correct. The generator and the certification prose are not yet safe to trust unread. Routed to the project lead under the review cap.

*Simulated review — informational only, not an Article 31 substitute.*
