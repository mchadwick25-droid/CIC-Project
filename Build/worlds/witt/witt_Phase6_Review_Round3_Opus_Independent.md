# Independent Review — Round 3 (Opus, targeted recheck)
## Target document: `witt_Phase6_Facilitator_Coordination_DRAFT.md`

**Date:** 2026-09-28
**Reviewer:** Claude Opus 5.5, a separate review agent with fresh context. It did not draft or revise this document. It is the same model that wrote Round 2. One Round 2 finding here (P6-S9) turns out to have been wrong on its own evidence, and it is reported as a Round 2 error below.

**What this review is.** A targeted recheck of the revision (commit `d68543fc0`) against the nine Round 2 findings P6-S1 to P6-S9 in `witt_Phase6_Review_Round2_Opus_Independent.md`. It also checks the revision thread's account in `Open_Gaps_Tracking.md` OG-44, and whether this document is consistent with Phase Five as Phase Five now stands. It is not a fresh review.

**Verdict: SUBSTANTIAL, narrowly. Not yet cleared.** Eight of the nine findings are resolved, including the participant-facing Section A: all three of its findings are fixed and the readability claim was verified independently. The one substantive residual is P6-S9. The revision applied it faithfully, but Round 2 had grounded it in the wrong artifact, so B7 now misdescribes what the deployed Representative does. Checking this also surfaced a real divergence between the project-lead-confirmed living-tradition handling and the deployed prompt. It is logged in `Open_Gaps_Tracking.md` OG-45 for the project lead.

---

## Section 1 — What was checked

- The diff `7b37c68b6..c5685e29d` for this file, and the current file in full.
- **Section A readability, recomputed** with `engine.m1.fk` (`fk_grade`, `fre_score`) directly against the current line-34 text.
- `records/witt/contested_claim/witt.contested.theses-door-posting.md` (for P6-S1).
- `engine/m4/reports/live-table-report-witt-rzg-2026-09-19.json` (for P6-S4): quote, `dominance_word_share`, `isolation_violations`.
- `engine/m4/facilitator_turns.py` (for P6-S5/S6: turn list, `SYSTEM_NATURE` text).
- FG V3.6 §12, read from the `.docx` (for P6-S6).
- The deployed `packages/witt/2026-09-26T20-13-54Z/compiled/prompt.txt` and `capsule.md`, plus `records/witt/world_core/witt.core.witt.md` (for P6-S8, P6-S9).
- `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and `World_Facilitation_Brief_Template.md` v1.2 (readability floor wording).
- Cross-document: Phase Five's current Summary Table and Sections 3.2, 3.4, 3.7, 3.8.

---

## Section 2 — Round 2 findings, one by one

| Finding | Status | Basis |
|---|---|---|
| **P6-S1** contested posting as fact | **Resolved** | The card now says the professor "sent theses … to his archbishop." The contested-claim record's `held_against` concedes that the letter to Albrecht, "enclosing the Theses," is "directly attested, signed, and complete." "His archbishop" is defensible: Albrecht was metropolitan over Wittenberg's diocese. The door/hammer detail is gone. |
| **P6-S2** readability | **Resolved; figures verified** | `engine.m1.fk` on the current card: **FK 6.2723, FRE 73.2477**. That matches the claimed 6.27 / 73.25. 130 words, 10 sentences, sentence lengths 5, 14, 16, 4, 16, 10, 12, 11, 18, 24 (longest 24, as claimed). FK falls below the template's 8–10 band. The document flags this rather than hiding it. The NorthStar decision does say the band floor of 8 is "**reported, not failed**" ("too-simple is not the risk the floor guards"), so the flag is honest and not a defect. Minor, not a finding: the card still opens on a verbless fragment ("Wittenberg, in the German lands."). |
| **P6-S3** felt-experience promise | **Resolved** | "what a household was asked to carry, morning, table, and night" matches B3 and the deployed [reception] rule. |
| **P6-S4** rzg "never tested" | **Resolved; verified** | The quote "their names barely appear in what we hold", `dominance_word_share {rzg: 0.65, witt: 0.35}` and `isolation_violations: []` all match the report. See the note on the "VI-4 family" label in Section 3. |
| **P6-S5** undeliverable disclosure | **Resolved** | B3 and B7 both disclose that `facilitator_turns.py` has no boundary-disclosure turn (OG-24). Confirmed against the file's turn list. Nothing is designed. |
| **P6-S6** self-narration caution | **Resolved** | "Fires on the first direct question" is corrected. §12's rule is quoted exactly against the `.docx`. The second, distinct caution on boundary-content narrated refusal is added. One carried-over wording issue is noted in Section 3. |
| **P6-S7** SE-2 as finding | **Resolved** | Recast as a hypothesized risk and stated as not observed, consistent with Phase Five. |
| **P6-S8** named comparanda | **Resolved** (+ cosmetic C-4) | Prompt line 29 does name the Tetrapolitan Confession. B7's statement is now accurate. |
| **P6-S9** living-tradition caution | **Applied as asked, but Round 2 was wrong: new residual R3-P6-1** | See below. |

---

## Section 3 — Substantive residual, and non-blocking notes

### R3-P6-1 (Round 2 error in P6-S9). B7 attributes text to "the deployed prompt" that the deployed prompt does not contain.

**Found.** B7 now says: "The deployed prompt's own closing paragraph does distinguish itself, generically: 'What you speak from is your own formation... not a claim about what those communities believe or practice now. They have their own voice.'" That paragraph is line 37 of `witt_Representative_Permanent_Prompt_Nikolaus.txt`, the design artifact. **It is not in the deployed `compiled/prompt.txt` or `capsule.md`.** A search for "their own voice", "believe or practice now", "account of themselves" and "living tradition" finds nothing in either. Round 2's P6-S9 cited "the Permanent Prompt's closing paragraph", which is the `.txt`. That contradicted Round 2's own S-1 finding that the `.txt` is not what participants meet. The revision faithfully carried Round 2's error into the text and relabelled it "deployed".

What the deployed prompt actually does is in `witt.dw.one-holy-church-forever` (compiled prompt, ~line 561): "A church today you could visit that's ours -- we cannot answer that from our own record, which does not reach past our own founder's lifetime and the confessional book gathered by 1580." So, measured against the deployed artifact, the **original** B7 wording ("does not comment on, defer to, or distinguish itself from any modern Lutheran body") was closer to correct than the revision's.

**Required.** B7's living-tradition caution should describe the deployed behaviour. The deployed prompt characterizes no modern body and draws no explicit distinction from one. Asked about a church today, the voice answers that its record does not reach that far. The Doc_10 §6 "Version A" paragraph exists only in the `.txt` (see the next item). This changes what the Facilitator is told the Representative does. That is the same test Round 2 applied, so it is substantive, though narrow.

**Related, and outside this document to fix. Logged as OG-45 for the project lead.** Doc_10 §6 records "Version A runtime handling" (the "they have their own voice and their own account of themselves" paragraph) as part of the Living Tradition Status Confirmation, which the project lead confirmed ("Confirm as drafted"). The deployed compiled prompt does not carry that paragraph. And `records/witt/world_core/witt.core.witt.md`'s LIVING_TRADITIONS note still reads "Article 29 confirmation is a project-lead decision and is PENDING", which is stale against Doc_10 §6's CONFIRMED. A project-lead-confirmed Article 29 runtime handling appears not to have reached runtime. That is a real gap and it goes to the project lead. It is not something a Phase Six revision can close.

### Non-blocking notes (not findings; for the next revising thread)

- **B7's self-narration caution still says Phase Five "found that Nikolaus's constructed voice twice produced" the failure.** Phase Five's SR turns are drafting-thread compositions (Phase Five Round 3, R3-2). The caution itself stands on independent evidence: Doc_10 §7's real first-turn failure, FG V3.6 §10/§15, and GoLive H-1. So this is an attribution fix that should follow Phase Five's own R3-2 fix, not a separate substantive finding here.
- **B5's "VI-4 family" label on "their names barely appear in what we hold."** Round 2 introduced this label. But the phrase is not model drift. It appears verbatim in three deployed records (`witt.dw.one-holy-church-forever`, `witt.limit.record-thinnest`, `witt.demo.record-thinnest`). And under the standard Phase Five's revised AN-2 now applies (Part Eight licenses "naming honestly what its own record holds and where it stops"), it may well be licensed idiom. Part Eight's Anachronism test separately says "never names its own limits as documentation or preservation." The build should state one criterion for which "what we hold" phrasings pass and which fail, and apply it to B5, AN-2 and the records alike, rather than call this one a defect by label. If it is a defect, it is a within-world record fix (see Phase Five Round 3, R3-3).
- **B4's "Nikolaus never discusses 'sources'…"** is contradicted by the live 1543 turn, which B7 itself cites ("not among the sources we hold in hand"). "Is built never to" would be accurate.
- **If Phase Five's CL-1 is rescored FAIL** (Phase Five Round 3, R3-4), B7's 1543 caution ("now scores this probe AMBIGUOUS") must follow.

---

## Section 4 — Cosmetic and propagation fixes applied directly (2026-09-28)

These change no finding. They correct status and cross-document statements to match the record. They are recorded here, not inline.

- **C-1.** Status paragraph: "Phase Five first, now settled" → "Phase Five first (itself revised and awaiting Round 3 independent review)". Phase Five is not settled.
- **C-2.** "What this document adds": "the two genuine FAILs (SR-2/SR-3, self-narration under sustained pressure; SE-2, institutional-reach confidence creep)" still described SE-2 as a FAIL and still said "under sustained pressure". Both contradict Phase Five's revision and this document's own B7. It now reads: the SR-2/SR-3 FAILs (firing on the first direct question), plus SE-2 as a hypothesized risk only.
- **C-3.** "Source documents read": Phase Five "(Approved to proceed)" → "(revised 2026-09-28, awaiting Round 3 independent review)". The "World build status" line said "Doc_01–Doc_10 and Phase Five all Approved to proceed". It now states that Doc_01–Doc_10 are Approved to proceed and that Phases Five to Seven are revised, awaiting Round 3, with no current Approved to proceed (OG-43, OG-44).
- **C-4.** B7 named comparanda: "now scored FAIL as originally written, PASS at SECOND LOOK once corrected" gave a score Phase Five never assigns (Phase Five scores AN-3 FAIL and offers a corrected version without scoring it). It now reads "scored FAIL as written, with a corrected version that recognizes the name plainly."
- **C-5.** B7 `SYSTEM_NATURE` quotation: em dash → " - ", to match the source.
- **C-6.** B4: "(Constitution Article 23; Permanent Prompt, museum-guide discipline)" → "(Constitution Article 23; RCF V3.2 Part Eight, Violation Indicator VI-1)". The deployed prompt has no museum-guide framing (Phase Five S-1). This is propagation only.

---

## Section 5 — Boundaries and cross-document consistency

- **No new live probes; no Facilitator turn type designed or implied. Confirmed.** B3 and B7 state that the boundary-disclosure turn is absent and do not sketch one.
- **Consistency with Phase Five as it now stands** (after C-2 to C-4): B7 matches on SR-2/SR-3 (FAIL, §12 routing), SE-2 (hypothesized), AN-3 (FAIL, name recognized), CL-1 (AMBIGUOUS, live output, no Facilitator path), RS-2 (AMBIGUOUS). B3 matches on the six thin domains and OG-24. The one pending dependency is CL-1: if Phase Five moves it to FAIL, B7 follows.

---

## Section 6 — Verdict and disposition

**Verdict: SUBSTANTIAL, narrowly. Not yet cleared; not yet eligible for "Approved to proceed."**

- Resolved: P6-S1 to P6-S8.
- Open: **R3-P6-1** (P6-S9 re-correction against the deployed artifact). It is one paragraph, and it arises from a Round 2 reviewer error, which is disclosed here.

The remaining changes are small and mechanical once Phase Five's own residuals are settled. The sequencing the project lead set (Five, then Six, then Seven) should hold, because B7 depends on Phase Five's CL-1 score and on its evidentiary-status wording. A next revision would be **round 2 of the three-round cap**. No escalation category is triggered by this document's own residual. The **OG-45 living-tradition divergence** is a separate item for the project lead, because it touches a project-lead-confirmed Article 29 determination. This review does not change the document's status line.
