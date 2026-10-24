Simulated review — informational only, not an Article 31 substitute.

# `lpc` Phase L0, item A — Doc_04 carried-open findings: does any of them change a downstream record, claim or gravity?

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Drafter model note:** `lpc_Decision_Log.md` and the cost ledger record no drafter model for Doc_04. CLAUDE.md routes Doc_04 drafting to Fable and revision to Sonnet. The text on disk is the product of the revision passes, so the field gives the revision model. That is the routing default, stated and not verified.
- **Reviewer agent:** independent Phase L0 reviewer subagent, fresh context, session_01PdSKYEGnPNVAntVFg5ZReR, high effort
- **Drafter agent:** pre-V2.0 `lpc` build thread (Doc_04 draft of 2026-09-09 and the fix passes of 2026-09-12 to 2026-09-15)
- **Round:** 1 — a single Phase L0 check, not a revision round. The file name matches no `Round_N` pattern, so it consumes no round against Doc_04.
- **Truncation check, method 1:** content identity. For Doc_04 (74954 B), `Doc_04_Superseded_Claims.md` (8339 B), `build/lpc_Rebaseline_Declaration.md` (3697 B) and `Doc04_Round11_Review.md` (59192 B), `wc -c` equals `git cat-file -s HEAD:<path>` and `git hash-object` equals `git rev-parse HEAD:<path>` at HEAD `2f0e42d2`. Doc_04 is byte-identical to the version the 2026-09-29 check read.
- **Truncation check, method 2:** structural completeness. Doc_04's H2 sequence runs §1 to §8 and then `## Disposition` (lines 12, 16, 22, 154, 167, 190, 205, 216, 251). The appendix runs §1 to §5 (lines 11 to 59). Every table row has an even pipe count (§4: 10 rows × 6; §6: 10 × 10; §8: 28 × 5). Both files end on a complete sentence inside their last section.
- **Date:** 2026-10-23
- **Scope:** Doc_04 and its appendix, read in full. Rounds 5 to 11, read by finding heading, plus Round 11's verification table, its "Still live" list and its act-158 adjudication, read in full. `Doc04_Independent_Check_2026-09-29.md` was read, and its findings re-tested on disk rather than carried. Downstream, by targeted grep and line reads: Docs 05 to 09, `lpc_Force_Index.md`, all eight `records/lpc/gravity/` records, and the three `records/lpc` files on the *Gesta* lineage (the Lancel source record, `lpc.limit.411-gesta-unread`, world core caution 9). Also `Source_Registry.md` row 65, `lpc_Gapped_Formation_Precedent.md` §4a and §4b, `Open_Gaps_Tracking.md` OG-22 and OG-27, CF V7.4 ¶304, 305, 309 and 310, and Forces Framework V1.1 ¶175 and ¶199 (from the docx XML).
- **Out of scope, by instruction:** Doc_04 is not re-reviewed, redrafted or reopened. Candidate 5's Supporting classification is the project lead's ruling and is not revisited.
- **Severity vocabulary:** P0 blocks; P1 is materially wrong or misleading and must be fixed before freeze; P2 is polish or record hygiene.
- **Nothing was edited except this file.** No web search and no model call were made.

---

## Verdict

**0 P0 · 1 P1 · 5 P2.**

**No carried-open finding changes a gravity downstream.** That covers every classification, six-test verdict, Interaction Matrix relation and gravity-force link. The eight gravity records match Doc_04 §4: Primary 1, 2, 3, 6; Supporting 4, 5, 7; Tensional 8. `lpc_Force_Index.md` lines 60 to 67 carry the same classes, and Doc_08 line 330 carries the same three G5 forces (1B-1, 2A-3, 2B-4). Candidate 5 reads as Supporting at every site checked.

**One substantial finding goes to the project lead: F1.** Approved downstream documents and two records state that Doc_04 Open Items 6 and 8 are open. Both have been CLOSED since 2026-09-15. One line, Doc_05 line 317, says the *Gesta* could change G5, which the precedent rules out. This is a claim about what is still open, not about a gravity. But it is wrong as written, and it sits in approved documents, so it needs a named change order.

**Fixed since the 2026-09-29 check, verified on disk:**
- Its N2 and N3 (the Lancel source record's act count and `rights_status`) are corrected, per OG-27.
- Registry row 65 now carries the act-158 explanation, which closes R6 M9, R9 M11 and R10 M11 on the Registry side.

---

## Source check of the one fact Doc_04 relies on

Doc_04 §7 Open Item 6 and appendix §2 rely on one fact: act 158 is Augustine's subscription to the mandate, not a speech. The check below opened `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (144733 lines):

- line 121764 is `158.  Augustinus  episcop`, with no *dixit*;
- lines 121765 and 121767 carry the Carthage / tribune-and-notary Marcellinus clause chain;
- line 121768 begins `mendalum`, then `usccpi  fll  nibacripsj` (*mandatum suscepi et subscripsi*);
- line 121756 (act 157) and line 121790 (act 159) are both Petilianus *dixit*;
- the same formula occurs at 121736–40 (Adeodatus, *ejendevi el sui-scrlpsi*, that is *mandavi et subscripsi*) and at 121772–75 (Vincentius, *boc mendetum*).

**The fact holds.** Its downstream statements are accurate: Lancel source record lines 19 and 51, row 65, Doc_05 line 215, and world core caution 9.

---

## Each carried-open finding and its disposition

The carried-open set is Round 11's own findings plus its "Still live" list for Rounds 5 to 10 (`Doc04_Round11_Review.md`, verification table). Earlier findings that Round 11 maps onto one of its own are listed under the Round 11 finding. **Closed** means gone on disk. **Harmless** means the finding is live, but nothing downstream repeats it or rests on it. **Changes downstream** gives the file and line.

| Carried-open finding | Disposition |
|---|---|
| R11 H1 to H4 | **Closed.** Status line 3 reads "1–11" and "5–11", and Disposition line 259 records all four as closed. |
| R11 M1 (with R9 L8, R10 H3-half, R10 M8-half, R10 L7). Appendix §1.2 (line 15) says "nothing depends on it", while Doc_04 line 91 says Dependency "passes narrowly", and the Tensional exclusion lives only in the appendix. | **Harmless.** The G5 record follows Doc_04 line 91 ("Only one finding depends on it", record line 67), not the appendix. No downstream file restates the Tensional exclusion. Doc_07 line 94 describes the premise accurately. |
| R11 M2 (with R9 M12, R10 M9). The Disposition (line 266) and the Decision Log give different escalation positions. Line 266 still counts Open Item 6 as an open tension. | **Changes downstream**, through the Open Item 6 pointer. See F1. The escalation count itself is governance-only. |
| R11 M3. Inline correction narration at Doc_04 line 34 ("a citation correction, not a classification change") and line 207 ("restored"). | **Changes downstream** at `records/lpc/gravity/lpc.gravity.pastoral-office-flock-keeping.md` lines 15–19, where the line-34 phrase is copied into `divergence_note`. See F2. Line 207 is not propagated. |
| R11 M4 (with R10 M3). Appendix line 5 contradicts the §4 preamble at line 47. | **Harmless.** Appendix only. |
| R11 M5 (the pass's self-report) | **Harmless.** It is about a past Decision Log entry. |
| R11 M6. Line 188 drops the search-bound qualifier. | **Harmless.** §3 lines 90 and 94 keep the bound. The G5 record lines 75–76 keep it too ("a limit of the search so far, not a proven absence"). |
| R11 M7. Open Item 6 has no owner and no acceptance criterion. | **Mooted in Doc_04.** Open Item 6 closed on precedent §4a. **But it changes downstream:** Doc_05 line 354 still repeats "no owner and no acceptance criterion" and says commissioning the read needs the project lead. See F1. |
| R11 L1 / R10 L1. Appendix line 35 cites 121764 for a phrase at 121768. | **Harmless.** Act 158's header is at 121764 and the formula at 121768. Row 65 now cites both lines correctly. |
| R11 L2 (with R9 L1-residue, R10 L5). Doc_04 line 99 quotes 3 of the 4 sentences of the Primary definition, with no ellipsis. | **Harmless.** Checked against CF ¶304. No downstream file quotes the definition. |
| R11 L3 (with R9 C2, R10 L6). Doc_04 line 7 changes Doc_01's verbs to "generate … state". | **Harmless.** Doc_01 lines 118 and 177 read "generates … states". No downstream file repeats the altered form. |
| R11 L4 (with R9 L6, R10 L8). "Has not been validly read" understates against row 65. | **Harmless.** It is repeated at Doc_05 line 215, Doc_07 line 234 and `lpc.limit.411-gesta-unread` (`why_sources_cannot_answer`). It errs in the cautious direction, and no claim rests on it. |
| R11 L5 / R10 L4. Appendix §5 gives paragraph 200 with no counting convention. | **Harmless.** The rule sits at docx paragraph index 199 (0-based) under "Step 4 — Gravity Discovery", and also at 175 (Layer 3). Doc_04's attribution is correct. Doc_08 line 330 quotes the rule accurately. |
| R11 L6 (with R10 L2, L3). Appendix §2.1's "~45%" and "two missed acts" are the withdrawn read's own figures. | **Harmless** to gravities. "~45% low" is repeated in `lpc_Gapped_Formation_Precedent.md` §4a (line 35), which is guidance, not a gravity claim. |
| R11 L7 (with R9 L3 to L5). The *Gesta* read artifact was not touched. | **Harmless.** It is a withdrawn artifact. |
| R11 L8, L10, C1, C2, C3 (with R10 C1 to C3). Appendix heading, §4 cell form, asterisk count, live attribution in appendix §4, and the §8 "Mechanical pass" row. | **Harmless.** Form only. |
| R11 L9. Decision Log line 777 points at the wrong entry. | **Harmless.** Decision Log only. |
| R8 H1(d). Doc_04 line 96 extends CF ¶309's no-upgrade rule to every divergence. | **Harmless.** ¶309 bars upgrading a candidate whose tests are strong and whose evidence is thin. Neither divergence (G3, G5) was upgraded. The G5 record rates `Inferential-Thin`, a tier ¶309 holds below Primary, which is consistent with Supporting. No classification moves. |
| R9 H4, and Open Item 8 (a determinate classification is reachable) | **Closed in Doc_04** (line 214, precedent §4b). **But it changes downstream:** Doc_05 line 355 and Doc_07 lines 94 and 250 say Open Item 8 is "unaddressed". See F1. The outcome is not affected, because Doc_07 line 94 notes that the argument reaches Supporting. |
| R9 M1-residue. The Status line does not name the withdrawal artifact. | **Harmless.** |
| R9 M8; R10 L10, L11. Decision Log record items. | **Harmless.** Decision Log only, not re-checked line by line. |
| R10 H5. Appendix completeness claim. | **Closed** as R11 H2. |
| R10 L12. Candidate 2's Dependency bullet lost the explicit "not Doc_01 §5's" negation. | **Harmless.** The G2 record (lines 72–74) states the mirroring of collegial communion without attributing it to Doc_01. |
| R6 M9 / R9 M11 / R10 M11. Row 65 against act 158. | **Closed on both sides.** Row 65 (Registry line 88) now gives thirteen speech acts, with act 158 as a subscription, and asks that restatements keep the floor. **The Doc_04 side is now stale.** See F3. |
| The governance and methodology escalation, items (a) to (d) | **Harmless** to records. Only the project lead can close it. It is not decided here. |
| Candidate 5's Supporting ruling | **Not reopened.** Applied consistently at every site checked. |

---

## Findings

### F1 — P1. Approved Docs 05, 07 and 08, and two records, say Doc_04 Open Items 6 and 8 are open. Both closed on 2026-09-15.

**Root (Doc_04, upstream):** four pointers were not updated when Open Items 6 and 8 closed (lines 212 and 214):
- line 97 routes the forces residue "to §7 Open Item 6";
- line 105 says Round 9's finding "is unaddressed and is carried at §7 Open Item 8";
- line 208 says "Open Items 6 and 8 may both bear on the classification";
- line 266 lists Open Item 6 as an open "Unresolved tension".

**Downstream text that is now wrong:**
- `Doc_05_Ecological_Reconstruction.md`:
  - line 25 says §11 carries Open Items 6 and 8 "forward unresolved";
  - line 173 says the two items "may both bear on it";
  - line 317 says the 411 material "is the one place that could change" G5's relation to formation. Precedent §4a rules out asking the *Gesta* to "retroactively prove a thin candidate's persistence";
  - line 354 says the read has "no owner and no acceptance criterion" and needs the project lead to commission it;
  - line 355 says Open Item 8 is "unaddressed".
- `Doc_07_Integrated_Ecology_Analysis.md`: line 94 ("Open Item 8 must not be quietly dropped"), line 234 ("One evidentiary question remains open") and line 250 ("Doc_04 §7 Open Item 8 remains unaddressed").
- `Doc_08_Forces_Document.md` line 358 calls the *Gesta* "the one unexploited source that could bear on G5's force-connection".
- `records/lpc/gravity/lpc.gravity.conciliar-authority-theory.md` lines 85–86: "have not reopened the question. It remains open."
- `records/lpc/honest_limit/lpc.limit.411-gesta-unread.md`, `why_sources_cannot_answer`: "bears specifically on G5's own Repetition and Persistence tests". This is inherited from Doc_07 line 234.

**What does not change:** G5's class, tests, relations and forces. All of these sites state, correctly, that nothing is drawn from the *Gesta*. Only the claim about what is open is wrong.

**Fix route:** one named change order covering Doc_04's four pointers and the downstream lines above. It edits approved documents and records, so it needs the project lead to rule on it. It should not be made as a quiet edit. The 2026-09-29 check raised this as its N1, and it is unchanged since then.

### F2 — P2. Correction narration from Doc_04 line 34 is copied into a canonical record.

`records/lpc/gravity/lpc.gravity.pastoral-office-flock-keeping.md` lines 15–19 end `divergence_note` with "a citation correction, not a classification change". That is process narration on a live or canonical surface, and it carries R11 M3 into `records/`. Fixing it changes no gravity.

### F3 — P2. Doc_04 is now out of date against the amended row 65.

- Doc_04 line 7 says row 65 records the *Gesta* as "available to Doc_04, and not yet drawn on by it". Row 65 now reads "available to Doc_04, which relies on one narrow fact from it".
- Doc_04 line 212 says the row 65 amendment is "flagged, not applied". It has been applied.

This is within Doc_04 and changes nothing downstream. Fold it into F1's change order.

### F4 — P2. World core caution 9 drops the floor that row 65 asks for.

`records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` lines 326–327 say "In thirteen numbered acts … each act has been counted and quoted". Row 65 calls thirteen "a floor, not a count" and asks that restatements carry the floor. "Quoted" also claims more than any record shows. This is the 2026-09-29 check's N4, and it is still live after OG-27's correction. It changes no gravity.

### F5 — P2. The OCR string quoted for act 158 is not byte-exact.

Doc_04 line 212 and row 65 give `mendalum ·usccpi fll nibacripsj`. The file holds two spaces, then the bytes `c3 a2 c2 80 c2 a2` (a mojibake bullet, not a middle dot), then `usccpi  fll  nibacripsj`, with double spaces throughout. The normalized reading and the finding are unaffected. A verbatim quotation should either match the bytes or say it has been normalized.

### F6 — P2. Process narration is still present in two `records/lpc` bodies.

- The G5 record body (line 106) says "See this script's own docstring…".
- The body of `lpc.limit.411-gesta-unread` says "read in full this session … named in this script's own docstring".

This is the 2026-09-29 check's N6, and it is unchanged. It belongs to the records owner's scope and is flagged here, not touched.

---

## Substantial findings for the project lead

1. **F1:** stale Open Item 6 and 8 status in approved Docs 05, 07 and 08, in the G5 record and in the 411 limit record. It needs one named change order. F2, F3 and F6 can ride on the same order.

Nothing else here is substantial. No carried-open finding moves a gravity, a classification, a test verdict, a matrix relation or a force link.
