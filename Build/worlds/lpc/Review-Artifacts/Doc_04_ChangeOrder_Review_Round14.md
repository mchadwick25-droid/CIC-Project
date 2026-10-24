Simulated review — informational only, not an Article 31 substitute.

# Doc_04 full review after change order CO-LPC-1

- **Document:** `Build/worlds/lpc/Doc_04_Gravity_Discovery.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `4e7a4bd9`; the file is unchanged since commit `949edbcf`, "lpc change order, part 2"), with the four records CO-LPC-1 changed that rest on it: `records/lpc/gravity/lpc.gravity.pastoral-office-flock-keeping.md`, `records/lpc/gravity/lpc.gravity.conciliar-authority-theory.md`, `records/lpc/honest_limit/lpc.limit.411-gesta-unread.md`, `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md`
- **Round:** 14
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent adversarial review subagent, fresh context (drafted none of the text under review)
- **Drafter:** Sonnet 5.5 drafters for CO-LPC-1, checked by the `lpc` build thread; earlier text by the `lpc` build thread (draft 2026-09-09, fix passes 2026-09-12 to 2026-09-15; drafting model not recorded in the log)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** CO-LPC-1 drafters and the `lpc` build thread
- **Date:** 2026-10-23
- **Scope:** full review of Doc_04 in its current state and of the four records above: every substantive claim; quotations re-verified against the vendored files and the governing documents; consistency with the 2026-10-23 rulings (D1 to D5, Doc_02 §7, Doc_05 crosswalk, Article 20, lexicon discovery method, liturgical candidates), with OG-28 to OG-51, and with Docs 01 to 03; Forces Framework integration; the CO-LPC-1 edits (diff `949edbcf^..949edbcf`) against `Review-Artifacts/L0_Doc04_Carried_Open_Check_2026-10-23.md` F1 to F6. Candidate 5's Supporting classification is the project lead's ruling and is not reopened.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6875`)
- **Truncation check, method 1:** line and byte count with an end-of-file read: `wc` gives 266 lines and 74,863 bytes; the file was read in full through line 266, which ends on the closing sentence of the Disposition ("§7 Open Items 6 and 8 are closed."), with headings §1 to §8 and Disposition present in order (lines 12, 16, 22, 154, 167, 190, 205, 216, 251).
- **Truncation check, method 2:** hash comparison against the committed blob: `sha256sum` of the working file and of `git show HEAD:<path>` both give `0113a357bc30fd754021f5559d78d3890461d0f56fa509465879b2b838492902`; `git hash-object` equals `git rev-parse HEAD:<path>` (`73d77f1e`). The four records also match their HEAD blobs (`git hash-object` = `git rev-parse HEAD:<path>`).
- **Method limits:** no web search and no model call. Nothing edited except this file.

---

## What was verified and holds

- **CO-LPC-1's OG-38 corrections in Doc_04.** Lines 97, 105, 208 and 266 now show Open Items 6 and 8 as closed. Line 7 now quotes row 65 exactly ("available to Doc_04, which relies on one narrow fact from it", `Source_Registry.md:88`). Line 7 now quotes Doc_01 §8 item 7's verbs exactly ("generates ... states", `Doc_01_World_Identification_Boundaries_Orientation.md:179`). Line 34's correction narration is gone (L0 F2). Line 212 now says the act-158 OCR string is normalised (L0 F5).
- **Act 158.** `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` line 121764 reads `158.  Augustinus  episcop` with no *dixit*. Line 121768 reads `mendalum`, a mojibake mark, then `usccpi  fll  nibacripsj`. Act 157 (line 121756) and act 159 (line 121790) are Petilianus *dixit*. Adeodatus is at 121736–40 and Vincentius's *boc mendetum* at 121775. The finding holds as stated.
- **Primary quotations, re-verified word for word at the structural marker.** The 256 preface, "neither does any of us set himself up as a bishop of bishops ... has his own proper right of judgment" (`anf05`, div3 `iv.vi.i`, lines 56871–56878). *On Baptism* II.3, "the authority of plenary Councils" (`npnf104`, div4 `v.iv.iv.iii`, line 11303). Letters XXXI §4 and CCXIII §4 (`npnf101`, lines 25856 and 55368). *De Lapsis*, "the shepherd that is chiefly wounded in the wound of his flock" (`anf05`, line 43727; G1 record manifestation).
- **Governing-text quotations.** CF V7.4 Primary and Supporting definitions (¶305, ¶306), the "noted explicitly rather than resolved by upgrading" clause (¶310) and the cross-check sentence (¶311); Forces Framework V1.1 "a gravity that cannot be connected ... is incomplete" (Step 4 entry); Constitution Article 21, "once made, governs all subsequent strand attribution; where strands exist, convergence across them is a test of a gravity's centrality". All from the docx XML.
- **Project-document quotations.** All Doc_01 quotations checked except the two at P2-2; all Doc_02 quotations except P2-1; all Doc_03 quotations and tags (`[SC], [RT]`; `[SC], [TC], [RT]`; `[AS], [TC], [PV]`; `[SC], [TC], [PV]`; `[SC], [TC], [DR]`); Registry rows 1, 22, 23, 65 Licensed-For and Verification phrases; the three `lpc_Gapped_Formation_Precedent.md` quotations.
- **Registry row identities.** Rows 1, 2, 4, 5, 7, 12, 13, 15, 18, 19, 21, 22, 23, 65 and 192 name the works Doc_04 says they name.
- **Stage job and Forces integration.** Present and substantive: candidates are generated from Doc_02 streams, Author Gravity risks are flagged at generation (Candidates 2, 5, 7, 8), all six tests and the Confidence/Gravity Cross-Check run per candidate, each candidate carries a forces-connection notation, and Candidate 5's incomplete-ecology residue is named against Forces Framework V1.1 Step 4 rather than hidden. The §4 index table and §6 matrix agree with §3.
- **World core caution 9** now carries the row 65 floor ("at least thirteen ... a floor, not a count") (L0 F4).

---

## Findings

### P1-1. The sermon scope (D1) changed the evidence base under Doc_04's negative Persistence findings, and Doc_04 neither tests nor bounds them

- **Where:** Doc_04 line 47 (Candidate 2 Persistence), line 175 (§5: the lapsed-crisis concern "has genuinely lapsed under its own name", closing Doc_01 §4's deferred question "by name"), line 182 (§5 bullet), line 150 (Candidate 8: "no Augustine-phase confessor-authority material is identified").
- **Evidence:** CO-LPC-1 wrote D1 into Doc_01 §2 (`Doc_01_World_Identification_Boundaries_Orientation.md:26`) and Doc_02 (`Doc_02_Source_Ecology.md:13`): the world now includes the Maurist *Sermones* 1 to 396 (PL 38, PL 39) and the post-Maurist finds. Doc_04 generates its candidates from Doc_02's evidence streams (line 7) and was not touched for D1. The newly in-scope PL 39 holds Sermo 352, *De utilitate agendae poenitentiae* II (heading `cic/texts/augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt:4166–4168`). At lines 4796–4802 Augustine preaches: *tenuit Ecclesia catholica istam veritatem de poenitentia agenda. Fuerant enim qui dicerent, quibusdam peccatis non esse dandam poenitentiam; et exclusi sunt de Ecclesia, et haeretici facti sunt.* In plain terms: the Catholic Church held to this truth about doing penance against certain heresies, for some said that penance must not be granted for certain sins, and they were cut off from the Church. That is the rigorist position Doc_04 line 46 names as the Novatianist schism, answered in Augustine's own preaching. Sermo 393 (heading line 15917) speaks of one "remotus ... ab altari" who must "reconcilietur" while still healthy (lines 15938–15941), and of "Agens poenitentiam, et reconciliatus" (line 15999).
- **Why it matters:** Doc_04 is the world's gravity spine, and §5 uses Candidate 2's Persistence result to correct a Doc_01 bullet and to close a deferred World Separation question. The result now stands on an evidence base the change order widened, with a counter-instance inside the new scope. Candidate 2's Primary classification does not depend on it (it rests on the Cyprian phase), and nothing here bears on Candidate 5.
- **Fix:** state at lines 47, 150, 175 and 182 that the Persistence findings were reached on the pre-D1 corpus (row 19's 97 sermons only). Withdraw "closed: it has genuinely lapsed" at line 175 and carry it as an open item: test Candidate 2's Persistence, and Candidate 8's, against the in-scope sermons, on the sermons that pass OG-28's per-sermon authenticity tag. Log the item in `Open_Gaps_Tracking.md`. The classifications in §4 need not move.

### P1-2. Candidate 5's disclosed search bound names only the *Gesta*, but Augustine restates the plenary-council formula in two letters of a Registry row Doc_04 already draws on; the G5 record states the opposite as fact

- **Where:** Doc_04 line 90 (Repetition: "not independently restated in a second Augustine-authored work this document has drawn on"; "**Search bound:**" names only the *Gesta*), line 94 (Persistence), line 162 and line 169 ("at one locus each"). G5 record line 62: "Each theory is attested at only one place in each bishop's writings."
- **Evidence:** Letter LIV to Januarius, §1: customs "held as approved and instituted either by the apostles themselves, or by plenary Councils, whose authority in the Church is most useful" (`cic/texts/npnf101_augustine-confessions-letters.xml`, div3 `vii.1.LIV`, line 29896; Latin *uel plenariis conciliis, quorum est in ecclesia saluberrima auctoritas*, `cic/texts/augustine_epistulae-1-123-lat_goldbacher-csel34.txt:15466`, under the address at line 15401). Letter XLIII §19: "there still remained a plenary Council of the universal Church" (`npnf101`, div3 `vii.1.XLIII`, line 28126; CSEL 34 line 12350). Both letters belong to Registry row 11 (Augustine's general correspondence, `Source_Registry.md`), the row that holds Letters XXXI and CCXIII, which Doc_04 relies on for Candidate 1 (line 34). Letter LIV is a pastoral letter on liturgical custom.
- **Why it matters:** the record states an unbounded absence that the vendored, in-world corpus contradicts. CLAUDE.md requires an absence to be stated at the scope actually searched. In Doc_04, the bound is literally true ("drawn on"), but presenting the *Gesta* as the only unread place misdescribes the search.
- **Fix (no reclassification; Candidate 5 stays Supporting on the ruling):** at Doc_04 line 90, add Letters XLIII §19 and LIV §1 to the search bound by locus, as restatements found and not weighed in the six tests. At lines 162 and 169, say "at one locus each among the texts weighed". In the G5 record, replace line 62's sentence with a bounded one that names the two letters. Log in `Open_Gaps_Tracking.md` that Letter LIV is pastoral and bears on Candidate 5's Formation test, for the project lead. Under precedent §4b this is not a ground for a further classification attempt.

### P1-3. The world core record, which CO-LPC-1 edited, still presents closed Open Items 6 and 8 as live, and misattributes Round 9's argument to Doc_04

- **Where:** `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` line 309 (caution 6: "A firm answer looks reachable from our own premises, but it has not been settled"); line 425 (keyword note: "Doc_04 finds reachable-but-unrun on its own premises"); lines 257–260 (the *Gesta* "remain largely untapped" and "bear on the question of what councils can decide").
- **Evidence:** Doc_04 line 214 closes Open Item 8: Candidate 5 "is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding"; Round 9's argument "is recorded, not pursued ... Whether the argument holds is not assessed here." Doc_04 line 212 closes Open Item 6: the *Gesta* is not asked to bear on Candidate 5. OG-38 (`Open_Gaps_Tracking.md:1630`) closes only "when every site is corrected and an independent check sweeps outward from each". CO-LPC-1 edited this record at caution 9 only (diff `949edbcf`).
- **Why it matters:** this is the same stale-status defect class the L0 check rated P1 (F1), in the record the Representative's world framing draws on. Line 425 also puts in Doc_04's mouth a finding Doc_04 explicitly declines to make.
- **Fix:** caution 6: drop the "firm answer looks reachable" sentence and keep the Doc_01 caveat. Line 425: "...Doc_01 does not consider fully settled; Doc_04 classifies it Supporting on the project lead's ruling." Lines 257–260: say the *Gesta* is kept for narrow, checkable facts and is not asked to settle the conciliar question. Then sweep the other `records/lpc` files for "reachable" and "untapped".

### P1-4. §7 Open Item 6 mixes superseded and current text, and the change order edited words inside the passage it labels as the original

- **Where:** Doc_04 line 212.
- **Evidence:** the item opens "CLOSED", then says "The original item read:" and runs on without a closing marker through "The question is open and unprejudiced. **The read should be commissioned from a thread that wrote neither withdrawn version...**", then into the current act-158 finding ("One narrow finding survives and is relied on here"). It ends with "`Source_Registry.md` row 65 now carries the same explanation", which CO-LPC-1 wrote in place of the original's "flagged, not applied" (diff `949edbcf`). So the passage labelled "original" is no longer the original, and a reader cannot tell where the superseded text ends and the live finding begins.
- **Why it matters:** this is the root site of OG-38. It still contains, in the document's own words, an instruction to commission the read and a statement that the question is open. That wording produced the downstream errors the change order was written to fix. Change history also does not belong inline in a canonical file (CLAUDE.md, "Keep the live/canonical surfaces clean").
- **Fix:** delete the "original item read" narrative; it is already held in `Doc_04_Superseded_Claims.md` §2 and the Decision Log. Keep three things: the closure on precedent §4a, the narrow act-158 finding with its line-by-line grounds, and the row 65 concordance.

### P2-1. A Doc_02 quotation that CO-LPC-1 corrected in Doc_02 was left uncorrected in Doc_04

- **Where:** Doc_04 line 56.
- **Evidence:** Doc_04 quotes Doc_02 §2 as "Augustine arguing *with* Cyprian, disputing his ruling while claiming his communion". CO-LPC-1 changed Doc_02 line 40 to "that \"Augustine argues *with* Cyprian ...\"", matching Doc_01 lines 102 and 106. The Doc_04 wording now matches no file.
- **Fix:** "Augustine argues *with* Cyprian, disputing his ruling while claiming his communion" (Doc_01 §5, as quoted at Doc_02 §2).

### P2-2. Two Doc_01 quotations carry an inserted "own"

- **Where:** Doc_04 line 65 and line 175.
- **Evidence:** line 65 quotes "tested against this document's own hardest instance"; Doc_01 line 110 reads "Tested against this document's hardest instance". Line 175 quotes "is Doc_04's own to confirm, not asserted as settled here"; Doc_01 line 95 reads "is Doc_04's to confirm". (The second error is copied from Doc_03 line 36.) This is the same defect OG-40 fixed in Doc_08.
- **Fix:** quote both exactly.

### P2-3. Doc_03's counts are restated without the matching rule the project lead ruled on

- **Where:** Doc_04 lines 26 (113), 41 (96, 114, 31, 20, ~150, 128), 56 (~120), 141 (~150, 128).
- **Evidence:** the lexicon-method ruling (`lpc_Decision_Log.md`, 2026-10-23, OG-36) requires every count to give its rule and its note-free number "by change order, to Doc_03's counts". OG-36 gives the note-free figures: flock/shepherd/pastor 113 → 106, confessor(s) 150 → 139, "the lapsed" 96 → 91. Doc_03 was not edited by CO-LPC-1 and is not listed as outstanding in OG-50. No tier or test result moves.
- **Fix:** when Doc_03's counts are restated, carry the note-free figures and the rule into Doc_04, or cite the counts as "Doc_03's figures, apparatus included". Add the Doc_03 recount to OG-50.

### P2-4. Two record sentences say more about the *Gesta* than is known or ruled

- **Where:** G5 record lines 85–86 ("The 411 Gesta ... do not settle it. We have not read them in full."); 411 limit record lines 27–28 ("is not something we can tell you yet").
- **Evidence:** "do not settle it" is a claim about the content of a text the same sentence says has not been read. "Yet" implies a pending read, which precedent §4a and Doc_04 line 212 close.
- **Fix:** G5: "We do not ask the 411 *Gesta* to settle it; they have not been read in full." Limit record: drop "yet".

### P2-5. The Status line, the Disposition and §8 no longer describe the document's state, and process narration survives

- **Where:** Doc_04 line 3; lines 207, 213, 214; lines 253–261; §8 (lines 216–249).
- **Evidence:** line 3 calls the document Approved to proceed 2026-09-15 with "Rounds 5–11 findings outstanding". It does not say the text was amended by CO-LPC-1 on 2026-10-23 and is under this Cap-ruled review. The L0 check found most carried findings closed or harmless, and CO-LPC-1 closed R11 L3, L0 F2 and F3, and part of R11 M2 and M3. Line 259 still lists them as outstanding. §8 records no post-approval event: not the 2026-09-29 check, not the L0 check, not the change order. Narration remains at line 207 ("§3's own restored Cross-Check note"), line 213 ("Round 2's own escalation assessment held..."), line 214 ("a sixth attempt ... after five supersessions across nine rounds"), and lines 259–261 (quotations of Round 11 and "not being held for a twelfth round"). CLAUDE.md: "Any PR that edits a live or canonical file also removes the commentary already in that file." `tools/check_live_commentary.py --surface worlds` marks these lines PROTECTED, so the tool does not catch them.
- **Fix:** rewrite line 3 as a short, true status line: Approved to proceed 2026-09-15; amended by CO-LPC-1 2026-10-23; under `Review-Artifacts/Doc_04_ChangeOrder_Review_Round14.md`; history in `lpc_Decision_Log.md`. Reduce the Disposition to the disposition and the open escalation. Add the post-approval review files to §8, as Template §9 requires. Remove the narration at lines 207, 213, 214 and 259–261.

### P2-6. G1 record claims sermon collections for both bishops

- **Where:** G1 record lines 62–63 ("It appears ... in both collections of sermons").
- **Evidence:** Doc_04 Candidate 1 (lines 26–35) cites Cyprian's letters, the 256 preface, *De Lapsis* and Pontius, not a Cyprianic sermon collection. No Registry row lists one.
- **Fix:** "in Cyprian's letters and treatises and in Augustine's sermons".

### P2-7. Residual narration and stale facts in the records CO-LPC-1 touched

- **Where:** world core line 339 (caution 11: the review "has not yet returned"), line 428 (body: "This world has no entry in records/worlds.yaml at all"; `records/worlds/lpc.yaml` now exists); G5 record `divergence_note` lines 15–23 ("the sharpest such divergence in this document", "re-verified across Doc_01's nine rounds", the phrase CO-LPC-1 removed from G1 and Doc_04 line 34) and description lines 62 and 89–90 ("it should be said plainly", "stated plainly rather than padded"), which read as assistant voice; G1 body line 101 ("Re-derived from the approved Doc_04 ..."), against G5's rewritten "Taken from".
- **Fix:** remove the narration and the voice tells, and update the registry sentence. Then make the two gravity records' provenance lines match.

---

Counts: 0 P0, 4 P1, 7 P2.

## VERDICT: Substantial revision required

VERDICT: Substantial revision required
