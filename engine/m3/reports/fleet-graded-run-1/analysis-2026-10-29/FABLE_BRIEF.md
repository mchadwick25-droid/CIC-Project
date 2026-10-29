# Brief for the Fable design pass: record storage, the Library, and how the engine reads them

Prepared 2026-10-29 from fleet graded run 1. For the project lead and the Fable design session.

## 1. What we want back

A **design**, not a set of patches. One document that says how records are stored and scoped, how the Library's sources connect to them, how both reach the voice, and how we will know a change worked. We have tweaked the engine several times and often ended up circling. This pass should break that.

Deliver:
1. A target design for records, honest limits, cautions and demonstrations (what lives where, who may read it).
2. How a newly vendored source becomes answerable coverage, and how an old limit gets retired when a source upgrade makes it false.
3. A change ledger and a test bench (section 7), so every change names the failure it targets and is checked before it ships.
4. A short list of open questions only the project lead can rule on.

Everything must respect CLAUDE.md. Never invent. Rigor and clear conversation outrank cost and speed. No band-aids, no fix on a fix. The frozen Library Access Gate design (D3, frozen 2026-09-15) changes only by named change order in its Decision Log, never by quiet edit.

## 1a. Containment: this pass has a small budget

Weekly credits are low. Treat this as a bounded design job, not an investigation.
- **One session. No subagents, no fan-out, no parallel reviewers, no paid model calls.** Reading and writing only.
- **Do not re-read the raw run.** Everything needed is in section 2 and section 3 of this brief and in the one-page digest `DIGEST.md` (analysis folder). Open only the files this brief names, and only when a design question cannot be answered without them: `D3-Converged-Design.md` sections 1, 4 and 5, one world's `world_core` record as an example, and `FLOW_MAP.md` part (c).
- **Do not run the replay or any test.** The test bench in section 7 is for later, cheaper sessions.
- **Output cap: the design document at most 4 pages, plus a one-page change ledger and a half-page list of questions for the project lead.** No per-world fix lists; those are Sonnet-level record work afterward.
- **Stop rule:** if you reach the page cap, or an answer would need data not in the brief, stop and list what is missing. Do not widen the search.
- **Out of scope:** writing or editing records, engine code, or tests; re-grading any answer; the lpc go-live decision; CI speed.

What the cheaper steps do before and after this pass: Sonnet (or the project lead's thread) prepares the digest and checks the section 4D hypotheses against the code and records. After the design, Sonnet implements it in small ledger-sized changes and tests each on the saved drafts.

## 2. What the run found (numbers)

12 worlds, 28 sealed questions each, answers read four ways. $16.55 of $17.00 spent.
- Automatic checks passed 336 of 336. They cannot gate.
- Our reviewers, checking against our records: 206 ship, 97 fix, 33 blocked. 90% scholarly acceptable.
- Outside referees, who saw no records: of 120 answers, 27 rejected after voiding 2 alx rejections (the alx referee was given a wrong time window, 150 to 260 instead of the record's 150 to 400). They rejected 17 of 33 we blocked and 6 of 63 we would have shipped.
- The cut step removed 297 sentences in 11 worlds. About 55 to 60 left a real orphan. 30 removed sentences were word for word in a record the sentence itself cited.
- The test ran the admission harness, not the live answer path. It skipped the live directive, the gate and reader, the recitation retry, self-revision and the length limit.

Full reports, per-answer grades, the code map, the replay and the outside referee outputs are in the analysis folder on branch `claude/fleet-run-1-analysis` (see section 9).

## 3. What the evidence says about storage

Confidence is marked. "Code-read" means a reviewer read the code and did not run it.

| # | Problem | Evidence | Confidence |
|---|---|---|---|
| S1 | A cell counts as covered if any record is tagged to it. Nothing checks that records answer each kind of question the cell holds. | Missing records for original sin, fate of outsiders, being born again, apostolic practice, survival today in rzg, gallic, alx, pahc, cappadocian, ijc. rzg's canon_cells do not match the fleet questions (7 cells). | High |
| S2 | Retrieval matches words, routes to at most 2 cells, and ignores the question's own category. Records depend on hand-written `retrieve_when` hints. | don: the cell's own record was not offered in 16 of 28. pahc: 13 of 28. | High for the symptom, code-read for the cause |
| S3 | Honest limits are stored per cell, and enter only when the right cell matched. The evidence block says "anything beyond these is our honest limit". | False silence in nearly every world: "no such source exists" where the period's sources do exist. The outside referees named the sources (Perpetua; Gregory of Nyssa, De infantibus; Macarius 38; Didache 11 and 15; Serdica 343; Cruciger; Argula von Grumbach). Note: the referees were told a wrong window for alx; no time-window finding stands from them. | High |
| S4 | Cautions, horizon notes, formation logic and demonstrations are stored with ordinary content and compile as citable text in builder wording. | Cautions read aloud (lpc caution 17); "I am a representative of…" recited; post-window names cleared by citing the core record; claim guards misread as denials. | Code-read |
| S5 | Witness and story text carries quote words inline, so the cut step removes them. | witt and don residue. 30 grounded sentences cut. | High (replay) |
| S6 | The build has no status filter for draft records. | One code-read finding. | Low, check first |
| S7 | Quote records are not in the voice's prompt. Only the evidence block offers them, with a speaker name the voice must carry correctly. | 81 cuts for "lead-in does not name its speaker". The test did show the name every time. | High (replay) |
| S8 | The repo is 3 GB, mostly `cic/texts` (about 1.9 GB, 1,528 files), checked out whole by every CI job. Library validators build the index twice. | PRs take about 20 minutes. | High |

## 4. The Library and source upgrades: what changes the picture

What I read in the frozen D3 design and the repo, in brief:
- A world's **shelf is computed, not stored**. At compile time the world's census id joins to `cic/corpus-map/<id>.yaml`, and the result is written into the package as `compiled/shelf.json`.
- `engine/m9` runs confinement checks against the shelf. A verbatim quote must match, byte for byte, inside the world's own shelf files. Source records name their shelf row.
- **Voicing permission** for material on a non-tradition row is decided by a documented tradition-pair relationship plus a per-row `documented_exchange` tag. Corpus-map judgment supplies these inputs.
- About 115 source records are **unvendored** and, by that design, confined to the etic layer. They have no row and never will.
- **Every corpus-map or `cic/texts` merge stales every affected world.** `repin-on-library-change.yml` opens one repin PR per stale world.
- The waiver list on day one was large (398 source-kind, about 283 shelf-row, 296 to 407 voicing-pair, 116 off-shelf citations). The byte check covers about a third of voiced material. Stories, witnesses and terms stay human-verified.
- The wants register tracks sources we want. PR 1241 is open with 15 unclassified rows that need a decision.

What source upgrades mean for this pass:

**A. Test results are tied to library state, and we did not record it.** The 12 worlds ran at 11 different commits, and rebuilt packages had different content hashes from the run's. Because a library merge stales worlds, a result is only meaningful with the library snapshot it ran against. Design a **run manifest**: commit, library file hashes, package hashes, engine version, per world.

**B. A newly vendored source does not become coverage by itself.** Coverage is hand-authored records. Upgrading the library adds shelf rows, but a question the shelf can now answer stays unanswered until someone writes a witness or limit. Design a **shelf-versus-records report**: what each world's shelf holds that no record covers, by question type. (I do not know if one exists.)

**C. Old limits go stale when sources improve.** An honest limit written as "no text of this kind is vendored" becomes false once one is. Design **limit provenance**: each limit declares the shelf evidence it rests on, so a library change flags the limits it may have falsified. Check first whether lpc's women's-voice limit and the Perpetua claim are an instance of this. I have not read that record.

**D. Hypotheses to test, not conclusions.** All unverified.
1. The emic/etic and voicing gate may be producing some false silence: material on non-tradition rows or unvendored sources can be cited but not voiced, so the voice reports silence. don's outside rejection ("almost no Donatist voice survives") fits this, but I have not traced it.
2. The wants-register wording that resolves a basilica-archaeology row as "a recognized field category with nothing to vendor" may feed the voice's claim that "nothing physical survives" in lpc. Trace it before assuming.
3. The 16 shared single-unit files (Optatus, the Collatio acts, the Theodosian Code files) only reach file-grain locus. This affects don and ijc, which had the highest rates of cut and ungrounded sentences in some categories.

**E. Do not let a library upgrade undo a record fix.** Repin builds new packages automatically. Any record fix we make must survive the next repin, and the repin PRs must not hide a regression.

## 5. Questions the design must answer

1. How does a record declare which kinds of question it answers, so S1 can be checked mechanically?
2. Where do builder notes, cautions and horizon text live so the voice never reads them as ground? What is the voice-safe form of each caution?
3. How are honest limits stored per question type, with a flag for "our shelf lacks it" versus "the period's sources lack it"?
4. How do witness and story records hold quoted material so the cut step cannot remove it?
5. What does the voice do when no record covers a question: which words are allowed, which are not?
6. How does a library upgrade propagate to coverage and to limits (sections 4B and 4C)?
7. How are drafts excluded from packages, and the repo and CI size reduced without weakening any gate?
8. What is the minimal change to the cut step so that removing a sentence cannot leave a dangling one or change attribution?

## 6. Constraints

- Quote wording, source fidelity and no-invention rules stand. Do not weaken a gate to reduce a count.
- Cost: per answer $0.018 to $0.040, dominated by prompt size. Output length is the lever. Keep answers short and clear (CEFR B2, grade 8 to 10, FRE 60 or more).
- Any change to D3 goes through its Decision Log as a named change order.
- Promotions to live remain the project lead's decision.

## 7. Change ledger and test bench (the anti-circling rule)

1. Every engine or record-structure change gets a ledger line before it is built: the failure it targets, the exact saved answers that should change, and the expected effect.
2. Test it first on the **308 saved drafts**. Re-running the cut step on them reproduces the shipped answers exactly (308 of 308), at no cost. Scripts: `replay/` in the analysis folder.
3. If a change does not move its named failure, **revert it**. Do not patch on top.
4. Before any live decision: a live-path run (not the admission harness), a second reviewer pass on the rubric, and an **outside referee** pass with no access to our records. Human specialists check the answers the AI referees reject.
5. Record the run manifest (section 4A) with every result.

## 8. What we do not know

- The outside referees are AI models acting as scholars. Most used no web search. Their corrections need a human specialist before we change records on their word.
- The code map was read, not run. The live-path effect of the missing directive is unmeasured and needs paid calls.
- Cappadocian has no automatic result, no per-answer cost and no replay.
- The orphan count is a heuristic, about 60% precise on a sample of 30.
- I read only part of the D3 design and none of the corpus-map classification files. Sections 4D hypotheses are from that partial read.

## 9. Where the material is

Branch `claude/fleet-run-1-analysis`, folder `engine/m3/reports/fleet-graded-run-1/analysis-2026-10-29/`: RUBRIC.md, second-pass reviews (`out/<world>.json`), blind packets and outside referee reports (`blind/`), FLOW_MAP.md, REPLAY_REPORT.md, removals.jsonl, this brief, and the findings page. The first-pass reviews are in `Build/worlds/<code>/Review-Artifacts/Fleet_Run1_Answer_Review_2026-10-28.md`. The Library design is `Build/Ministry/Features/Library-Access-Gate/D3-Converged-Design.md` and its Decision-Log.
