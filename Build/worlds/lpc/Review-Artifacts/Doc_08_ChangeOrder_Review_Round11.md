Simulated review — informational only, not an Article 31 substitute.

# Doc_08 full review after change order CO-LPC-1

- **Document:** `Build/worlds/lpc/Doc_08_Forces_Document.md` (branch `claude/lpc-augustine-sermons-2026-10-23`; the task named head `a0209b8d`, the checkout's HEAD is `4e7a4bd9`; the file is unchanged since commit `949edbcf`, "lpc change order, part 2"), with `Build/worlds/lpc/lpc_Force_Index.md`, `Build/worlds/lpc/scripts/gen_force_index.py`, `records/lpc/force/lpc.force.illegal-to-established-shift.md` and `records/lpc/force/lpc.force.transmission-institutionally-dominant-side.md`
- **Round:** 11
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent adversarial review subagent, fresh context (drafted none of the text under review)
- **Drafter:** Sonnet 5.5 drafters for CO-LPC-1, checked by the `lpc` build thread; earlier text by the `lpc` build thread (draft and Round 1 to 8 fix passes 2026-09-15; Opus 5.0 per `Review-Artifacts/L0_Doc08_Generator_Check_2026-10-23.md`, which takes it from the Round 9 check)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** CO-LPC-1 drafters and the `lpc` build thread
- **Date:** 2026-10-23
- **Scope:** full review of Doc_08 in its current state, the Force Index, the CO-LPC-1 generator change (diff `949edbcf^..949edbcf`) and the two force records CO-LPC-1 edited. Every substantive claim; every quotation re-verified against the vendored files and the governing documents; every interval and date; consistency with the 2026-10-23 rulings (D1 to D5, Doc_02 §7, Doc_05 crosswalk, Article 20, lexicon discovery method, liturgical candidates), with OG-28 to OG-51 and with Docs 01 to 07; Forces Framework integration; whether each L0 finding CO-LPC-1 claims to fix is fixed, and whether the edits introduced new errors.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6875`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc` gives 478 lines and 74,387 bytes. I read the file in full through line 478, which ends on the Disposition's last sentence ("This document has now been through **eight** review rounds."). All 12 `## ` headings are present in order (lines 2, 18, 31, 39, 284, 318, 363, 377, 391, 419, 444, 468), and there are 17 `#### Force` headings.
- **Truncation check, method 2:** hash comparison against the committed blob. `sha256sum` of the working file and of `git show HEAD:<path>` both give `10b7edc7…2455e8b`. `git hash-object` equals `git rev-parse HEAD:<path>` (`5e40e3e7`). The Index (`971f6cf8`), the generator (`fd044cb4`) and both records (`0281e137`, `ab0a317e`) also match their HEAD blobs.
- **Method limits:** no web search and no model call. Nothing edited except this file. The generator was run only on a scratch copy.

---

## What was verified and holds

- **Force Index regenerates identically.** I copied Doc_08, the generator and the `Doc08_*` review files to a scratch folder and ran `gen_force_index.py <scratch>`. It exited 0 ("17 forces, 15 connections, 8 gravities"). `diff` against the committed `lpc_Force_Index.md` is empty, and both files hash to `1ca2b60f…cdf4cd93b`. `git status` showed no change to tracked files.
- **The generator change is sound.** I re-ran the L0 mutants on scratch copies:
  - **L0 H1.** I removed both `## VERDICT:` headings from the Round 8 artifact and planted "Round 7 was **CLEARED**". The generator now halts ("artifact says (no VERDICT heading) … Refusing to emit"). Before, it printed a false CLEARED. `verdict_counts` reads the verdict only from a `## VERDICT: <word>` heading outside code fences (`gen_force_index.py:217-223`).
  - **L0 H2.** I set the Status line to "not yet Approved to proceed" and the Disposition to "**Not disposed.**". The Index now prints "REVISED after Round 8 — the revision is unreviewed" and "**Not disposed.**". `APP.match` anchors approval to the opening of the line (`gen_force_index.py:121-122`).
  - **L0 M1.** A `[CO-022, 2026-09-15 — also **3A-1**]` notice on the G6 line now halts the run (exit 1). The tag pattern admits digits and hyphens (`gen_force_index.py:32`).
  - **L0 M2, L1, L2 and C1.** The "thirteen controls" paragraph, the A to M lists, "emphasis-dense", "the force-ID pattern" and "five known tags" are all gone. The Index header now lists the Status and Review-history lines as derived (`lpc_Force_Index.md:8`), which matches `Doc_08:12`.
- **CO-LPC-1's text corrections to Doc_08 hold.**
  - **L0 L7.** Line 33 now quotes Doc_01 exactly: "not Layer-1 documentation in the Forces Framework's formal sense" (`Doc_01_World_Identification_Boundaries_Orientation.md`, one hit).
  - **L0 C2.** Line 161 closes "…not 2's own continuation …", and line 334 now carries "— see §3, §5)", which matches `Doc_04_Gravity_Discovery.md:195`.
  - **L0 M3.** Lines 358 and 438 show Doc_04 §7 item 6 closed and the *Gesta* kept for narrow facts, which agrees with Doc_04.
  - **L0 L8.** The workbook rule is now cited to V1.9 (Archive) and V2.0.
  - **L0 M4.** The "[ADDED …] provenance clauses … retained deliberately" text is gone. P2-2 below covers the residue.
- **Quotations re-verified word for word.** I checked each one with whitespace, line-end hyphens and apostrophes normalised, and confirmed each by its containing heading:
  - **`anf05`:** "it is the shepherd that is chiefly wounded in the wound of his flock". "your suffrage and God's judgment" and "ancient venom" are in *To the People, Concerning Five Schismatic Presbyters*. The Pontius "neophyte" sentence. "thousands of certificates were daily given, contrary to the law of the Gospel" and "these thirteen letters … transmitted to you" are in *To the Presbyters and Deacons Assembled at Rome*. "you always read my letters to the very distinguished clergy who preside with you there" is in *To Cornelius*. "matter, and even the paper itself…" and "as it actually came to hand … Crementius the sub-deacon, to carry" are in *To the Presbyters and Deacons Abiding at Rome. A.D. 250*. "to send a copy of this letter … make your own opportunities" is in *From the Roman Clergy to the Carthaginian Clergy*, as Doc_08 says.
  - **`npnf104`:** "even of the plenary Councils, the earlier are often corrected by those which follow them".
  - **CSEL 36:** `augustine_retractationes-lat_knoll-csel36.txt:1509-1511` reads "sine in libris siue in epistulis siue in / 5 tractatibus cum quadam iudiciaria seueritate" and "uelut censorio stilo". The emendation is disclosed. The apparatus for line 4 records only "resecta H" and "epistolis", so it gives no variant against *siue*.
  - **Weiskotten's Possidius:** lines 2133-2143 hold "to all the clergy of Hippo and to all the people", "all who heard rejoiced and clamored", the refusal "since his bishop was still living", and "under com-/pulsion and constraint he yielded". Possidius cites *De Mortalitate* (line 722).
  - **Forces Framework V1.1 (docx):** "This is not optional. All three layers are required for every force.", "…a gravity whose ecology is incomplete.", the "Where direct testimony is absent…" sentence, and "documented as the world's own self-understanding rather than asserted as historically established fact".
  - **L4 template:** "Forces with minimal formative trace may be documented briefly at Layer 1 only with a note explaining why full treatment was not warranted".
  - **Upstream documents:** the Doc_04 §3 and §6 quotations; "this document's own reading" (exactly two cells in Doc_04, as line 334 says); Doc_02 §2 "occasional rather than systematic… documents what crises provoked correspondence"; Doc_02 §6 "on the institutionally dominant and eventually canonized side of every dispute he engaged"; Doc_01 §6 "the foundational inheritance of the subsequent Western theological tradition".
- **Every interval and date checked against the documents' own dates:**
  - **133 years and "a century and a third":** 258 to 391. Lines 23, 179, 191, 264 and 302, and record `illegal-to-established-shift:42`.
  - **"About 170 years" (line 205) and "Some 170 years on" (record `transmission-institutionally-dominant-side:55`):** the compared acts are the Decian-era letters (c. 250 to 252, by their own ANF headings) and the *Retractationes* "near the end of his life" (c. 426 to 427; Augustine died 430). That is about 168 to 177 years, so the wording holds. The Decision Log gives the basis as "258 and 430", which are the two men's deaths, not the dates of the compared acts. The figure stands on the correct endpoints as well.
  - **"A century and a half afterward"** (record line 53, Augustine's recourse to state action): 258 to 401, or to 404 and 405, is about 143 to 147 years. It holds.
  - **Other dates:** Cyprian bishop 248/249 to 258; Augustine presbyter 391, bishop 395/396, died 430. The plague "c. 249–262" matches Doc_01's "Plague of Cyprian (c. 249–262)". Possidius's "two to three years" (from c. 246 to 248/249), "seven years" (250/251 to 258) and "roughly nine years" Manichaean also hold. The Vandal crossing in 429 holds. Death on 28 August 430 matches Prosper, row 203, "V kl. Sept." under 430. Carthage under 439 is "nine years later". Prosper of Aquitaine is fairly called a "Gallic chronicler".
- **Forces Framework integration.** Doc_08 is the Framework's own deliverable. It has all six cells, three layers per force, transmission at 2B-5 and 3B-2, 15 named cross-cell connections, and every gravity linked. The integration is substantive. The 17 force IDs, the 15 connections, the 8 gravity rows and the confidence spread (14 Documented, 3 Widely Accepted, 2B-3's Contested element) agree across §3, §5, §7, §9 and the Index.
- **The two force records.** Their links and confidence match the Index. Their descriptions score FK 8.8 / FRE 60.3 and FK 8.3 / FRE 60.4 on `engine/m7/turn_readability.score_turn`, with no failures. The new "a century and a third" (line 42) agrees with Doc_08 2B-3.
- **The sermon rulings (D1 to D5) need no edit in Doc_08.** 2B-5's description of the working corpus ("ANF/NPNF … critical Latin editions vendored but far less used") is still true today. No title "Bishop of the Kept Flock" appears.

---

## Findings

### P1-1. 3B-2 and §1 still state the gap claim the project lead ruled false, and attribute it to Doc_02 §7, which CO-LPC-1 rewrote to say the opposite

- **Where:** `Build/worlds/lpc/Doc_08_Forces_Document.md:23` and `:264`.
- **What the document says.** Line 23: "No primary source named at Doc_02 §1 and no row in `Source_Registry.md` dates from within that interval." Line 264: "Doc_02 §7 records that **no primary source named at §1 and no Registry row dates from within the roughly 133 years** … **Confidence: Documented** — this is a fact about the record, checkable against the Registry."
- **Evidence.**
  - `Doc_02_Source_Ecology.md:122`, as restated by CO-LPC-1 on the project lead's ruling ("Doc_02 §7 gap claim: restated to Doc_01's narrower test", `lpc_Decision_Log.md:2373-2379`), now reads: "Some rows of `Source_Registry.md` do date from the gap, or record its events, and none of them is that voice". It names Optatus (c. 366 to 393; rows 27, 64, 300, 301), row 223, rows 235, 228 and 59, and rows 44 and 88.
  - `Source_Registry.md:40`, `:87` and `:365` (Optatus, Native) confirm this.
  - The check the entry offers ("checkable against the Registry") therefore fails. Doc_08 also misreports what Doc_02 §7 says.
- **Reach.** The same claim is in `records/lpc/force/lpc.force.transmission-asymmetric-span-133-year-silence.md:16` and `:31` ("no text in our own source catalogue, dates from within that gap"). It is in `lpc_Claims_Register.md:61` (claim `25da1952`). Outside this review's scope, it is also in `Doc_05_Ecological_Reconstruction.md:27` (§0.3).
- **Why P1.** It changes a Documented claim's substance. It is the exact claim the ruling corrected, and the change order did not carry the correction into Doc_08 or its record. A downstream builder reading 3B-2 would receive the overruled version.
- **Fix:**
  - Restate lines 23 and 264 to Doc_01's test as Doc_02 §7 now words it: no surviving voice continuous with Cyprian's ordinary-pastoral mode, from within this world's boundary, dates from within the gap. Rows that date from the gap (Optatus, the councils, the *Codex Theodosianus*) are polemic, canons or law, not that voice.
  - Keep "Documented", tied to that narrower test.
  - Make the same correction in the 3B-2 force record (lines 16 and 31) and in the claims register row.
  - Flag Doc_05 §0.3 to its owner through Open_Gaps.

### P2-1. The review record in Doc_08 and the Index is stale and narrower than it says

- **Where:** `Doc_08:14`, `:434`, `:472`, `:474` and `:478`; `lpc_Force_Index.md:3`, `:4` and `:154`; `gen_force_index.py:196`.
- **Evidence.**
  - `python -m engine.m10.cli roundcount lpc 8` reports 10 review files: Rounds 1 to 8, `Doc08_Round9_Targeted_Check_2026-09-29.md` and `L0_Doc08_Generator_Check_2026-10-23.md`. With this file there are 11.
  - Doc_08 says "eight". It also says "the Round 8 fix pass is itself unreviewed", but two checks have since examined that revision.
  - Doc_08 does not say that it was changed after approval, by CO-LPC-1.
  - The Index says the count is "counted from `Review-Artifacts/` rather than typed". The generator globs only `Doc08_Round*_Review.md`, so it cannot see the Round 9 check, the L0 check or this file. `assert_doc08_round_count` then forces Doc_08's prose to agree with that narrower count.
- **Fix:**
  - Make the Index state the rule it actually counts by, or count by the rule of `engine/m10/rounds.py`.
  - Restate Doc_08's Status line and Disposition to the real record: Approved to proceed, then amended by CO-LPC-1, and reviewed under the Cap ruling. Keep the history itself in the Decision Log, not in the document.

### P2-2. §8's scan figure "six hits at two entries" was not re-run, and the document's own earlier arithmetic gives five

- **Where:** `Doc_08:399`.
- **Evidence.**
  - Before CO-LPC-1, the line said that removing the `[ADDED …]` provenance clauses leaves five hits, with 3B-2 losing one (`git show 949edbcf`). CO-LPC-1 kept "six" and added "No inline provenance clause remains in any entry", so on the document's own account the current figure is five.
  - It locates 3B-1's three hits but not 3B-2's.
  - `Open_Gaps_Tracking.md:1731` (OG-50) already records that this claim was not re-run.
- **Fix:** re-run the seven-marker scan on the current text and state the figure and where each hit sits, or drop the figure.

### P2-3. Process narration remains in the body of a canonical file that CO-LPC-1 edited

- **Where and what:**
  - `Doc_08:177`: "an independent review found §7 reporting a Contested element that no force entry carried".
  - `:403`: "an unqualified 'permits no exceptions' overstated … named here for whoever next relies on this notice".
  - `:405`: "richer than the stubs they replaced".
  - `:407`: the whole paragraph "The defect was worse than a rule breach … none of it was looked for … All three entries are now written".
  - `:434`: "which this line said had not been run for five rounds and five fix passes".
- **Evidence.** CLAUDE.md, "Keep the live/canonical surfaces clean": a PR that edits a canonical file also removes the commentary already in it. `tools/check_live_commentary.py --surface worlds` does not flag these lines (it reports only PROTECTED and KEEP lines for Doc_08), so the gate does not catch them.
- **Fix:** delete the narration and keep each line's substance where it has any. For example, line 407's disclosure of the Latin-only *Retractationes* witness is already at 2B-5.

### P2-4. A run-on sentence introduced by CO-LPC-1

- **Where:** `Doc_08:476`.
- **Evidence.** The line reads "…states that new builds create no `.xlsx` workbooks Markdown is the required form, not a departure from precedent." A full stop is missing after "workbooks". It was introduced by the edit in `949edbcf`.
- **Fix:** "…create no `.xlsx` workbooks. Markdown is the required form…".

### P2-5. The 2B-5 record overstates the *Retractationes* translation gap

- **Where:** `records/lpc/force/lpc.force.transmission-institutionally-dominant-side.md:81-82`.
- **Evidence.**
  - The record says "our own corpus holds no English translation of it".
  - Doc_08 line 213 says "no **complete** English translation is vendored", and line 407 says substantial excerpts survive inside NPNF's editorial apparatus.
  - Doc_02 §1 says "no complete English translation of the Retractationes is vendored, but substantial excerpts are".
- **Fix:** "our own corpus holds no complete English translation of it, and none of this passage".

### P2-6. The count of 2B-5's Layer 2 quotations disagrees with itself

- **Where:** `Doc_08:209` and `:430` against `:407`.
- **Evidence.**
  - Lines 209 and 430 say the Layer 2 "rests on four quotations in the world's own voice".
  - Line 407 speaks of "the four English-attested Cyprianic quotations" plus the Augustinian exhibit.
  - Layer 2 (lines 203 and 205) carries four Cyprianic quoted passages and the *Retractationes* Latin.
- **Fix:** "four Cyprianic quotations and one from the *Retractationes*" at lines 209 and 430.

---

## Counts

P0: 0. P1: 1. P2: 6.

Per the Cap ruling, the substantial finding goes to the project lead. This file does not authorize a further review file.

VERDICT: Substantial revision required
