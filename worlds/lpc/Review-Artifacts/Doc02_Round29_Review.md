# Doc_02 — Source Ecology and Source Registry: Latin Pastoral-Congregational Christianity
## Round 29 Independent Adversarial Review — scoped to the Round 28 fix pass (`9c3ebb3` + `bc0183d`), verifying each of Round 28's eighteen findings against the files rather than against the fix pass's own account, hunting for defects the fix pass itself introduced, re-deriving the new *CTh* XVI.5.21 identification and the fourteen-acts count from the primary texts, and auditing the corpus-map edit through its generated output

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `bc0183d`, "lpc: Round 28 fix pass -- all 18 findings addressed; donatism.yaml corrected", 2026-09-09 02:52:17 UTC, on branch `lpc-round26-rows-65-44`; parent `9c3ebb3`, "lpc: fix Round 28 HIGH finding -- withdraw mislabeled Letter 185 fine claim", 02:44:50 UTC; grandparent `0842ae2`, the commit that added `Doc02_Round28_Review.md`, 02:44:21 UTC; and `0124a9f`, the pre-fix state every claim below is diffed against):**
- `Review-Artifacts/Doc02_Round28_Review.md` (380 lines) — read in full before anything else, finding by finding, and used only as the list of eighteen claims to test, never as evidence for any of them. Its own H1, L2, L5 and C3 were re-derived from primary sources and one of them is corrected below
- `worlds/lpc/Source_Registry.md` (329 lines, 37,285 words, 212 rows) — line 3 (Status) read clause by clause against its own text at `0124a9f`; rows 44 (line 58) and 65 (line 83) read cell by cell against `0124a9f` and `9c3ebb3`; all 214 table lines re-parsed by column position for pipe count, column count, row-number sequence and physical order; every row carrying "not a vendoring candidate" enumerated by Type and Confidence for the L5 sweep audit; rows 39, 51, 58, 59, 64, 67, 88, 191, 194 read in full
- `Doc_02_Source_Ecology.md` (160 lines, 13,148 words) — line 3 (Status), line 97 (§5), and all of §10 (lines 148–160) read in full against `0124a9f`
- `Source_Acquisition_Manifest.md` (81 lines, 5,577 words) — line 11 (Disposition), line 59 (the sourcelibrary.org caution), line 69 (§3's membership rule and the new row-65 paragraph) read in full
- `lpc_Decision_Log.md` (406 lines, 25,950 words) — the new 2026-09-09 entry (lines 379–406) read clause by clause; lines 93–111, 121, 189–193 and 318–378 read for what it does and does not supersede
- **Primary texts, read directly rather than through either the fix pass's or Round 28's account of them:** `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` (27,049 lines) on this branch — Letter 185 §25 located at its own `div3 n="7"` inside `div2 id="v.vi"` and read in full, and every occurrence of the fine language in the whole volume enumerated and attributed to its own `div`. `cic/texts/theodosianus-16_mommsen-meyer1905.txt` at `don-lpc` (94,020 lines) — both title pages, *CTh* XVI.5.21 and XVI.5.52 read in the body, and every "ten pounds of gold" formula in Book 16 Title 5 enumerated with its own constitution heading and date. `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` at `don-lpc` (144,732 lines) — the `ACTORES VII` roster read at its own heading, and an independent OCR-tolerant scan of the *Gesta* span for numbered acts naming Augustine, run without reference to the fourteen numbers claimed
- `worlds/don/don_Decision_Log.md` at `don-lpc` (590 lines) — the "2026-09-01 — G3 acquisition attempts, five tried, none vendored" entry and the Boyd substitute entry read attempt by attempt; `worlds/don/Source_Registry.md` at `don-lpc` (79 lines) — rows 14 and 16 read in full
- `cic/corpus-map/_staging/codex-theodosianus_latinlibrary.yaml` (101 lines), `cic/corpus-map/donatism.yaml` (219 lines), `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (1,176 lines) — the diff `9c3ebb3..bc0183d` read hunk by hunk, and the generated output independently reproduced: the whole `cic/corpus-map/` tree copied to a scratch directory and `corpus_map_merge.py` re-run there with no flags, then diffed against the committed tree
- `cic/engine/corpus_map_merge.py` (`--check` run, and `--help` read for what `--write-only` does and does not do); `cic/texts/REGISTRY.yaml`, `cic/texts/README.md`, and all of `worlds/_cross-world/` swept for live statements the corrections falsify, with `gen_needs_ruling.py` re-run in the same scratch copy to test whether its output still matches the map

**Review date:** 2026-09-09
**Reviewer:** independent adversarial review thread. Did not draft the Round 28 revision, did not write either fix commit, did not write `Doc02_Round28_Review.md` or Rounds 1–27, and did not perform any vendoring on either branch.

**What this round does and does not re-run.** It does not re-run the recall test, the PRESS question, the corpus-map census, or a whole-document sweep of Doc_02. It runs four briefs. **First:** for each of the eighteen findings, decide independently whether it is fixed, partly fixed, unfixed, or mis-fixed — from the files, not from the commit messages and not from the Decision Log's own account, both of which claim all eighteen are addressed. **Second, and given the highest weight:** hunt for defects the fix pass introduced, because Round 28's own HIGH was a correction pass introducing a false claim, and a second fix pass at the same site is where that shape recurs. **Third:** re-derive the two new positive claims — the *CTh* XVI.5.21 identification and the fourteen-acts count — from the primary texts alone. **Fourth:** audit the corpus-map edit end to end, including whether the generated files actually regenerated and whether anything downstream of them still lags.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 6 MEDIUM · 7 LOW · 4 COSMETIC.**

**The fix pass is substantially better work than the revision it repairs, and its two hardest new claims survive independent re-derivation.** *CTh* XVI.5.21 really is the law Augustine's Letter 185 §25 describes, and the identification is not merely plausible but the only candidate the vendored file supports: `denis libris auri` occurs in exactly two lines of the whole 94,020-line volume, both inside XVI.5.21, and every other "ten pounds of gold" clause in Title 5 *De haereticis* belongs to a constitution of 428 — long after the "Theodosius, of pious memory" §25 names. The law's own scope, `quoscumque constiterit vel ordinasse clericos vel suscepisse officium clericorum … denis libris auri viritim`, maps clause for clause onto §25's "any heretical bishop or clergyman … should be fined ten pounds of gold": the bishop who ordains, the clergyman who accepts office, ten pounds each. The 392/401/412 chronology as row 44 now states it is right, and NPNF's own endnote 2521 dates the council 401 exactly as the row says. **Fourteen is right.** An independent line-initial scan of the *Gesta* span, run without reference to the fix pass's list, returns exactly the same fourteen act numbers — 50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, 267, 272 — every one a genuine numbered act, every one Augustine, none an index or contents entry. **The M1 correction is accurate to both limbs of the sibling build's own record**, and the sourcelibrary.org caution it erased is restored at both sites. **And the corpus-map fix was done correctly at the mechanical level**, which is the level where this project's generated files usually go wrong: the edit was made in `_staging/`, `--check` exits 0, and a full independent re-merge into a scratch tree reproduces both generated files byte-identically, with no collateral change anywhere else in the 788-assignment output.

**Where the HIGH is: in the one sentence the fix pass wrote to prove it had read the primary text.** Row 44's withdrawal narrative says Letter 185 §25 was "read directly this round in `npnf104_augustine-anti-manichaean-anti-donatist.xml` **already vendored on this branch**," and then quotes it: "the law … which imposes a fine of ten pounds of gold, which none of you have ever paid to this very day." **That sentence is not in §25.** It is not in Letter 185 at all. It is from *Answer to the Letters of Petilian the Donatist*, Book II — a different work, 2,186 lines earlier in the same NPNF volume, in a different `div2`. The phrase "which none of you have ever paid to this very day" occurs exactly once in the entire file, at line 17438, and §25's actual wording is different. Round 28's HIGH was a correction pass attaching a real fact to the wrong statute; this fix pass's HIGH is a correction pass attaching a real fact to the wrong work — the same failure, one layer down, inside the sentence written to demonstrate the failure had been cured (H1).

**Where the MEDIUMs are: in the count repair, and in everything the fix pass edited around rather than in.** The repair of the review-round count states "twenty-seven" three times in one Status line and twice in the other, at a commit where `Review-Artifacts/` demonstrably holds **twenty-eight** — Round 28's own artifact, committed eight minutes before the first fix commit, and reported by name in the same sentence (M1). Deleting the count from the Registry Status line left two sentences that the count had bounded now unbounded and false, and the new opening clause "1 HIGH" now sits in a line that also asserts HIGH findings "have stayed" at zero (M2). Three sites written in `bc0183d` say Round 27's twelve findings are "unrecorded in `lpc_Decision_Log.md`" and that "its commissioning entry is the log's last word on it" — in the same commit that writes the log entry recording them (M3). `Source_Acquisition_Manifest.md` gained a live project-lead acquisition decision at §3 and lost nothing from its own Disposition paragraph, which still says the review cycle "has now concluded for these three documents" and still points at a Doc_02 §10 sentence this same commit deleted (M4). Doc_02 §10's escalation-category paragraph and its project-lead-direction paragraph were left unmarked and in the present tense, asserting that no CO-022 category applies and that editing a generated corpus-map entry is outside this build thread's authority — in the commit that raises a category-4 escalation and edits another world's generated corpus-map bucket (M5). And the L5 sweep, presented as covering "all eight rows carrying 'not a vendoring candidate'," names five and misses **row 58**, Cyprian's CCSL 3 — the strongest instance of the shape in the table, whose public-domain alternative is not merely identifiable but already vendored on this branch and already rowed three times (M6).

**The propagation shape recurs for an eighth consecutive round.** Round 28 called it "the recurring failure of this document set." M4, M5 and M6 are all the same shape, and L4 extends it into the fleet-wide generated layer: `worlds/_cross-world/NEEDS-RULING.md` is generated from `cic/corpus-map/`, publishes the very note fields this pass rewrote, and was not regenerated — it still reports "2 works, 2 assignments" where the map now yields five and six.

---

## HIGH

### H1 — Row 44 quotes Letter 185 §25 for a sentence that is not in Letter 185. The quotation is from *Answer to the Letters of Petilian* Book II, a different work in the same volume. The misquotation sits inside the clause asserting that §25 was "read directly this round."

**Where.** `Source_Registry.md` line 58 (row 44), the withdrawal narrative introduced at `9c3ebb3` and carried unchanged through `bc0183d`:

> Letter 185 §25, read directly this round in `npnf104_augustine-anti-manichaean-anti-donatist.xml` **already vendored on this branch**, cites a fine of **ten pounds of gold**, not silver: "the law … which imposes a fine of ten pounds of gold, which none of you have ever paid to this very day."

**What §25 actually says**, read this round at its own `div3 type="Chapter" n="7"` inside `div2 id="v.vi"` ("The Correction of the Donatists" = Letter 185), file lines 19624–19632:

> … if they would take the law which Theodosius, of pious memory, enacted generally against heretics of all kinds, to the effect that any heretical bishop or clergyman, being found in any place, should be fined ten pounds of gold, and confirm it in more express terms against the Donatists, who denied that they were heretics …

**Where the quoted sentence actually comes from.** File line 17438, inside `div3 type="Book" n="II" id="v.v.iv"` — *Answer to the Letters of Petilian the Donatist*, Book II, at paragraph anchor `v.v.iv.lxxxiv`:

> … it was this that first made it necessary to urge before the vicar Seranus that the law should be put in force against you **which imposes a fine of ten pounds of gold, which none of you have ever paid to this very day**, and yet you charge us with cruelty.

**Re-derived by count, not by impression.** The string "which none of you have ever paid to this very day" occurs **exactly once** in the 27,049-line file — at 17438, not in §25. The string "which imposes a fine of ten pounds" likewise occurs **once**, at 17438. Neither occurs anywhere in Letter 185. §25's own words are "should be fined ten pounds of gold," which is not what the row quotes.

**Why this is HIGH and not LOW.**

(a) **It is new, and it is at the site of the previous HIGH.** Round 28's H1 was a correction pass mis-attributing a real fact to the wrong statute. This is a correction pass mis-attributing a real quotation to the wrong work, in the sentence written to close that finding. The row's own Decision Log entry calls the previous error "recorded rather than quietly repaired"; the repair introduced its own.

(b) **The misquotation is load-bearing for the row's own evidentiary claim.** The row is not merely wrong about a citation. It says the passage was "read directly this round" and offers the quotation as the proof. A verbatim string that is not in the cited passage is the one thing that cannot be true if the passage was read. The row cannot be both accurate about its method and accurate about its quotation, and it is the method claim that the rest of the row rests on.

(c) **It is refutable in one command against a file already vendored on this branch** — the identical objection Round 28 raised against the claim this sentence replaced, and the identical remedy: `grep` for the quoted string.

(d) **The two passages say materially different things.** §25 describes a law of Theodosius I *sought* by the council of 401 and describes the fine prospectively; the Petilian passage describes a fine *already in force* and unpaid, urged before the vicar Seranus. A reader who follows the row to §25 for the words the row quotes will not find them, and a reader who takes the quoted words as §25's will have Augustine saying something in 417 about non-payment that he says in a different work about a different proceeding.

**What is not wrong, and must not be lost in the fix.** The substantive identification is sound and was independently confirmed this round. §25 does describe a ten-pounds-of-gold law of Theodosius I against heretical clergy; XVI.5.21 (392 Iun. 15) is that law; and it is the only candidate the vendored file offers. `denis libris auri` occurs at exactly two lines in the whole volume, 86855 and 86862, both inside XVI.5.21; every other `decem librarum auri` clause in Title 5 sits under `XVI, 5, 65 (428 Mai. 30)`. The fix is to the quotation, not to the conclusion.

**Fix shape.** Replace the quoted string with §25's own words — "any heretical bishop or clergyman, being found in any place, should be fined ten pounds of gold" — or drop the quotation and cite the paragraph. If the Petilian passage is wanted (it is genuinely useful: it is Augustine on the same fine's non-enforcement), cite it as *Contra litteras Petiliani* II, in its own right, and say so.

---

## MEDIUM

### M1 — Both repaired Status lines state that `Review-Artifacts/` holds **twenty-seven** review artifacts and adjudicate **twenty-seven** rounds, at a commit where it holds twenty-eight and where the same sentence reports Round 28's own verdict. The repair of the stale-count defect restates it, one commit after it was adjudicated.

**Where.** `Source_Registry.md` line 3 (three occurrences of "twenty-seven") and `Doc_02_Source_Ecology.md` line 3 (two), both written at `bc0183d`:

> `Review-Artifacts/` holds twenty-seven `Doc02_Round*_Review.md` files. … **twenty-seven rounds, disposition 2026-09-08.**

> Three numbers were in play for one joint disposition: twenty-five here, fourteen at the Registry, twenty-seven `Doc02_Round*_Review.md` files in `Review-Artifacts/`. **Adjudicated: twenty-seven rounds, disposition 2026-09-08.**

**Re-derived by count.**

| commit | `Doc02_Round*_Review.md` tracked |
|---|---|
| `0124a9f` (the state Round 28 adjudicated) | **27** |
| `0842ae2` (Round 28's artifact committed) | **28** |
| `9c3ebb3` | **28** |
| `bc0183d` (where both Status lines are written) | **28** |

`git ls-tree -r --name-only bc0183d …/Review-Artifacts/` returns twenty-eight, numbered 1–28 with no gap.

**Why this is not pedantry about an off-by-one.** Three things stack.

(a) **The same sentence contradicts the number.** Both lines open "**Round 28 returned SUBSTANTIAL REVISION REQUIRED (1 HIGH, 6 MEDIUM, 7 LOW, 4 COSMETIC)**" and then adjudicate that twenty-seven rounds have run. A round that returned a graded verdict has run. The line asserts twenty-eight rounds and twenty-seven rounds in one breath.

(b) **Twenty-seven was correct only for the state Round 28 read.** Round 28's adjudication section says so explicitly and shows its work at HEAD = `0124a9f`. Transcribing an adjudication across three commits without re-running its one countable input is precisely the "unre-derived claim reaching a live document" pattern that the same Status line says is "tracked in `lpc_Decision_Log.md`."

(c) **It is the tenth recurrence of the defect the sentence claims to end.** The line itself says "this is the ninth recurrence, not a first sighting," and Round 27's C1 is headed "*This commit re-staled the very sentence Round 26's C1 fix was written to cure, by the same mechanism, one commit later.*" This is that, again, one commit later.

**Fix shape.** The Registry line's own remedy is already written and already correct — stop stating a count, point at the directory. Apply it to the adjudication clause too, or state the count as of a named commit rather than as of nothing.

### M2 — Deleting "Fourteen independent adversarial review rounds" from the Registry Status line left two sentences that the count had bounded, now unbounded and false — and the new "1 HIGH" clause contradicts the line's own surviving claim that HIGH findings "have stayed" at zero.

**Where.** `Source_Registry.md` line 3. Three sentences, all live, all in one line.

**Limb one — the unbounded sweep claim.** At `0124a9f` and at `1b91ef2` the line read:

> **Fourteen independent adversarial review rounds; each round's findings were worked through in a following fix pass**, documented in `Review-Artifacts/` and, where a finding was itself wrong or two reviews disagreed with each other, in `lpc_Decision_Log.md`.

The fix pass deleted the leading clause and left the rest, now standing alone as a general present-tense claim:

> Each round's findings were worked through in a following fix pass, documented in `Review-Artifacts/` …

Seventy words earlier, the same line says: "**Round 27's twelve findings are at this writing unfixed**." The line asserts that every round's findings were worked through and that one round's were not.

**Limb two — the trend claim.** Also surviving unedited on the same line:

> **HIGH findings fell monotonically to zero and have stayed there**, reaching zero at Round 5 and holding for ten rounds running.

The line now opens by reporting that Round 28 returned **1 HIGH**. "Have stayed there" is false as of the line's own first sentence, and "ten rounds running" (Rounds 5–14) is a window the line no longer sits inside.

**Why MEDIUM.** This is not inherited staleness. The first limb was *created* by this pass's own deletion: a bounded historical statement became an unbounded false one because the bound was removed and the predicate was not. The second is a collision the pass created by inserting a contradicting fact into the same line and not reading down. Both are in the Registry's Status line, which is the first thing a Doc_03 or Doc_04 builder reads, and both are exactly Round 27's M2 ("*deleted both fourteen-round finding-count sequences while keeping every claim built on top of them*") recurring at the same site by the same mechanism.

### M3 — Three sites written in `bc0183d` state that Round 27's twelve findings are "unrecorded in `lpc_Decision_Log.md`," in the same commit that writes the `lpc_Decision_Log.md` entry recording them.

**Where, all three at `bc0183d`:**
- `Source_Registry.md` line 3: "Round 27's twelve findings are at this writing unfixed **and unrecorded in `lpc_Decision_Log.md`**."
- `Doc_02_Source_Ecology.md` line 3: identical clause.
- `Doc_02_Source_Ecology.md` line 156 (§10): "**Round 27's twelve findings are unfixed and unrecorded in `lpc_Decision_Log.md`** — **its commissioning entry is the log's last word on it.**"

**What the same commit put in the log.** `lpc_Decision_Log.md` lines 379–406, the new 2026-09-09 entry, twice:

> **Round 27's twelve findings remain unfixed and, until this entry, unrecorded** — the log's last word on Round 27 was its commissioning.

> M2 (no sweep) — see the escalation below; the two `lpc_Decision_Log.md` sites the review names are dated historical entries, superseded by this entry …

The log knows it now records them and says so with the correct tense. The three documents that point at the log do not, and §10's "its commissioning entry is the log's last word on it" is flatly false as of the same commit: the log's last word on Round 27 is 27 lines further down.

**Why MEDIUM rather than COSMETIC.** Round 28's M6 was that no log entry existed. The fix pass wrote one — the right fix — and then left three documents telling the reader it did not. A reader who follows the disclosure to the log to confirm the gap will find the gap closed and the disclosure wrong, which is worse for the record than either state alone, and it is the same class of defect as Round 28's M4 (an edit misdescribing its own scope) reappearing at three sites instead of one.

### M4 — `Source_Acquisition_Manifest.md` was substantively edited — a live project-lead acquisition decision added at §3 — with no change to its own Disposition paragraph, which still asserts the review cycle has concluded for all three documents and still points at a Doc_02 §10 sentence this same commit deleted.

**What the pass added**, `Source_Acquisition_Manifest.md` line 69: a new paragraph moving row 65 "**out of §3 and into §1's territory**," naming "**a real, public-domain acquisition candidate whose rights position has been resolved rather than assumed**," and stating a decision for the project lead — "**whether to vendor the Migne file onto this world's branch, or to merge the sibling branch, or to leave it where it sits.**" That is the M3 fix and it is a good one.

**What the pass did not touch**, `Source_Acquisition_Manifest.md` line 11:

> **Disposition.** This document, `Doc_02_Source_Ecology.md`, and `Source_Registry.md` were self-disposed together by the build thread to **Approved to proceed** on 2026-09-02 … (**`Doc_02_Source_Ecology.md` §10 now states only the current, 2026-09-08 disposition that superseded this one**). … distinct from **the self-disposable review cycle that has now concluded for these three documents**.

**Both parenthetical claims are now false, and this commit falsified them.** Doc_02 §10 no longer "states only the current, 2026-09-08 disposition": as of `bc0183d` its first paragraph is headed "**Disposition — SUPERSEDED**" and its second is headed "**Superseded disposition, retained as history**." And "the self-disposable review cycle that has now concluded for these three documents" is contradicted by both companions' Status lines, by §10, and by the Manifest's own new paragraph, which routes a decision to the project lead.

**And the reopening does not name the Manifest.** Doc_02 §10's new paragraph reads "This document and **`Source_Registry.md`** are REOPENED and carry no disposition." The superseded paragraph one line below disposes **three** documents. So after this commit the Manifest is the one document of the three that was materially edited in this pass and carries no statement of its own disposition status at all — while its own Disposition paragraph claims it was disposed in a set of three, two of which have since been reopened without it.

**Why MEDIUM.** This is the propagation shape at its plainest: the fix pass opened the Manifest, changed what it routes, and left the paragraph that describes the Manifest's own standing asserting the opposite. Round 28's M3 said the two documents "give opposite answers to 'does the project lead need to decide anything about the 411 Conference acts?'" That question is now answered consistently; "is this document disposed?" is not.

### M5 — Doc_02 §10's escalation-category assessment and its project-lead-direction paragraph were left unmarked and in the present tense. They assert that no CO-022 category applies and that editing a generated corpus-map entry is outside this build thread's authority — in the commit that raises a category-4 escalation and edits another world's generated corpus-map bucket.

**Where.** `Doc_02_Source_Ecology.md` lines 150 and 160, both inside §10, both untouched by `bc0183d`, both sitting above and below the two paragraphs the pass did rewrite.

**Line 150, live and unqualified:**

> On that test, **none of the three documents decides a portfolio-level question.** … both are corpus-map census questions **this build thread cannot resolve (re-homing or merging a generated-file entry is outside this build thread's own editing authority)**, and this document does not resolve either — **it discloses both and leaves the corpus map's own current state standing** … If a future census-level correction re-homes Optatus's own *tradition* placement or merges the council rows, **that correction happens at the corpus-map/System Hub level, not here; no escalation follows from naming the question.**

**Line 160, live and in the present tense:**

> The escalation-category assessment above was independently re-run by Round 25 against its own findings and **found none of CO-022's four categories applies** to what Round 25 found; that finding is adopted here as confirmation that **no escalation category stands in the way** of the project lead's own direction …

**What the same commit actually did.** `lpc_Decision_Log.md`, new entry: "**CO-022 escalation category 4 — raised, and resolved by project-lead direction.** … The file is another world's corpus-map bucket, outside this build thread's editing authority … **Corrected under that direction — in `cic/corpus-map/_staging/codex-theodosianus_latinlibrary.yaml` …** This edit was made on another world's bucket under explicit project-lead direction." And `git diff 9c3ebb3..bc0183d -- cic/corpus-map/` confirms `donatism.yaml` changed.

**Why MEDIUM.** §10 is the section a reader consults for this document set's escalation position, and it now says three things the same commit disproves: that no category applies, that this thread does not touch generated corpus-map entries, and that no escalation follows from naming such a question. The pass marked the *disposition* paragraph as superseded and left the two paragraphs that reason toward it live and unmarked — a half-fix of exactly the M5 Round 28 raised, which was that §10 asserts what the Status line denies.

### M6 — The L5 sweep is presented as covering "all eight rows carrying 'not a vendoring candidate'" and names five. It misses **row 58** — Cyprian's CCSL 3, the strongest instance of the shape in the table, whose public-domain alternative is already vendored on this branch and already rowed three times.

**Where.** `Source_Registry.md` line 83 (row 65):

> **Sweep for this same defect shape, run at Round 28's own L5** … The shape is: a modern in-copyright critical edition marked "not a vendoring candidate," where an earlier printing of the same underlying ancient text carries a different rights position that was never checked. **Eight Type-P rows carry that phrase.** Rows 64 (Labrousse) and 67 (Mutzenbecher) already name their public-domain alternatives … Rows 49 and 50 (Divjak, Dolbeau) are genuinely clean … **One residual, named rather than left for a later round to rediscover: row 59** (Munier, *Concilia Africae*, CCSL 149) …

**Re-derived this round across all 212 rows by column position.** Nineteen rows carry "not a vendoring candidate." Restricted to Type **P**, there are **seven**, not eight: rows **49, 50, 58, 59, 64, 65, 67**. (Row 51 is Type P/S; if it is the eighth, the accounting is short by two rather than one.) The row names 49, 50, 59, 64, 67 and itself — six. **Row 58 is named nowhere.**

**What row 58 is.** *Sancti Cypriani episcopi opera*, CCSL 3 (Weber and Bévenot, 1972), 3A (1976), 3B–3D *Epistulae* (Diercks, 1994–1999), Turnhout — Type P, Confidence C, Native:

> **Not currently vendored** — in copyright (1972–1999+), consultation-only, **not a vendoring candidate**; naming it does not itself close row 3's own open question, which requires reading this edition's own apparatus.

That is row 65's shape exactly: a modern in-copyright critical edition of an ancient text, marked not-a-candidate, with no earlier printing of the same text named in the cell.

**And unlike row 59, the earlier printing is not hypothetical.** Hartel's public-domain *S. Thasci Caecili Cypriani opera omnia*, CSEL 3.1–3.3 (Vienna, 1868–1871), is rowed **three times** in this same Registry — rows 39, 191 and 194 — and is **already vendored on this branch**, as `cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt` and `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`. Row 58 may still be the right call (its own note gives a real reason the earlier edition does not substitute — the apparatus), but that is a reason to *state*, in the form rows 64 and 67 already model, not a reason to omit the row from a sweep the same sentence says covered eight of eight.

**Why MEDIUM rather than LOW.** Round 28 rated the *absence* of a sweep at LOW because nothing turned on it. This is different: a sweep was commissioned, was run, is disclosed as complete, states a count it does not account for, and misses the one row in the set whose alternative is sitting in `cic/texts/` on this branch. A disclosed-complete sweep that is incomplete is worse than a disclosed-absent one, because the next round has been told not to look.

---

## LOW

### L1 — The L4 fix replaced the 1954 photostat reprint with the 1905 original and left "2nd ed." standing. The vendored file's own two title pages, which the row cites as its authority, carry no edition statement at all.

**Where.** `Source_Registry.md` line 58, row 44's Source cell, as rewritten at `bc0183d`:

> *Theodosiani libri XVI cum Constitutionibus Sirmondianis*, **2nd ed.** (Berlin: Weidmann, **1905**; this row's Source description formerly named the 1954 photostat reprint, corrected at Round 28's own L4 — the vendored file's own two title pages read `BEROLINI APVD WEIDMANNOS MDCCCCV`, so **the object this row is now about is the 1905 original** …)

**Read directly this round**, `theodosianus-16_mommsen-meyer1905.txt` lines 138–192. Title page one: `THEODOSIANI / LIBRl XVI / CVM CONSTITVTIONIBVS SIRMONDIANIS / ET / LEGES NOVELLAE … EDroERVNT / TH. MOMMSEN et PAVLVS M. MEYER / ACCEDVNT TABVLAE 8EX / VOLVMINIS I PARS POSTB^RIOIl / BEROLINI / APVD weidmannos / MDCCCCV`. Title page two: `… EDIDIT / ADSVMPTO APPARATV P. KRVEGERI / TH. MOMMSEN / VOLVMINIS I PARS rOSTERIOR / TEXTVS CVM APPARATV / BEROLINI / APVD WEIDMANNOS / MDCCCCV`. **Neither carries an edition statement** — no *editio secunda*, no *ed. 2*, nothing.

"2nd ed." is the descriptor of the object the L4 fix removed: the 1954 Weidmann *lucis ope expressa* reprint is the second edition; the 1905 Mommsen–Meyer is the first. The cell now attaches the reprint's edition number to the original's date and place, inside a parenthesis explaining that the reprint has been removed.

**Why LOW.** The rights argument — public domain by the 1905 date, plus Google's retained disclaimer — is unaffected and correct. What is defective is the bibliographic identity of the row's own named object, in a row whose whole correction was that the named object and the argued-about object were different.

### L2 — Two locators introduced this pass to close Round 28's C3 and to ground the XVI.5.21 identification both point at the wrong line, and both were carried over from Round 28's account rather than re-derived.

**(a) Row 65**, `Source_Registry.md` line 83: "the `ACTORES VII. / EX PARTE CATHOLICORUM` table **at file line 113083**."

Read directly: `ACTORES VII.` is at `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` line **113067** and `EX PARTE CATHOLICORUM. EX PARTE DO.NATl.` at line **113069**. Line **113083** is `Possidius Calamensis. 7- Adeodatus Milevitanus.` — the roster's last entry, not the heading the row quotes. (Augustine's own line, `Augustinus Uipporegiensis. 5. Emeritls Ca^sareensis.`, is at 113075.) The locator is inside the table, which is why it is LOW and not worse — but Round 28's C3 was specifically that the row gave no locator, and the locator supplied does not point at what the sentence names.

**(b) Row 44**, same line: "*CTh* XVI.5.21, headed `XVI, 5, 21 (392 lun. 15)` in the vendored file **at line 86855**, reads `denis libris auri viritim`."

Read directly: the heading `XVI, 5, 21 (392 lun. 15).` is at `theodosianus-16_mommsen-meyer1905.txt` line **86852**; the constitution opens at 86854; line **86855** is the line containing `denis libris auri viritim`. As written, "at line 86855" attaches to the heading, which is three lines earlier.

**Why this is a finding and not nitpicking.** Both numbers are transcribed from `Doc02_Round28_Review.md` (which states 113083 for the table and cites 86855 for XVI.5.21) rather than re-derived. The whole discipline this round is run under is that a claim in a review artifact is a claim to re-check, not a fact to inherit — and these are the two locators a future reader would use to verify the two corrections that matter most.

### L3 — `Doc_02_Source_Ecology.md`'s Status line claims the count disclosure is "stated identically here and in `Source_Registry.md`." It is not: the Registry states "no count is stated here" and points at the directory; Doc_02 states counts and a range stale by three.

**The claim**, `Doc_02_Source_Ecology.md` line 3:

> **A count discrepancy … now adjudicated and repaired — stated identically here and in `Source_Registry.md`, per the cross-document fact-consistency rule that an earlier draft of these two disclosures broke by describing the same problem at two different sizes (Round 28's own L7).**

**What the two lines actually do.** `Source_Registry.md` line 3: "**Applying this line's own remedy rather than restating a number that has gone stale nine times:** no count is stated here. **The authoritative record is the `Review-Artifacts/` directory itself.** … Full findings and fixes for each round are in `Review-Artifacts/`, `Doc02_Round1_Review.md` onward — **read the directory, not a range stated here**, for the same reason no count is stated."

`Doc_02_Source_Ecology.md` line 3, closing sentence, unedited by this pass: "Full round-by-round findings and disposition history are in `lpc_Decision_Log.md` and `Review-Artifacts/Doc02_Round1_Review.md` **through `Doc02_Round25_Review.md`**, not restated here."

So the Registry says do not state a range and states none; Doc_02 states a range, and the range ends three artifacts short of the twenty-eight on disk — the same stale-pointer defect the adjudication above it was written to close. The adjudicated facts do match across the two lines; the remedy does not, and the sentence claiming identity is stronger than what the pass delivered.

**Why LOW.** The substantive adjudication is genuinely harmonized, which was L7's actual complaint. What fails is the self-description and the one pointer the harmonization did not reach.

### L4 — `worlds/_cross-world/NEEDS-RULING.md` is generated from `cic/corpus-map/`, publishes the note fields this pass rewrote, and was not regenerated. It reports "2 works, 2 assignments" where the map now yields five and six, and carries none of the correction.

**Verified by re-running the generator.** The whole `cic/corpus-map/` tree and `worlds/_cross-world/` were copied to a scratch directory and `gen_needs_ruling.py` re-run there against the committed map. Output: `5 works, 6 assignments, 3 groups`. The committed file says `**2 works, 2 assignments.**`, and its narrative says "87 became 2" and "**87 to 2** — a 98% reduction." Regenerated, those read "87 became 5" and "**87 to 5** — a 94% reduction."

The regenerated file also gains a `## donatism — 3 work(s)` section quoting, verbatim, the corrected *Codex Theodosianus* note this pass wrote. The committed file has no `donatism` section at all.

**Why LOW rather than MEDIUM.** The staleness pre-dates this pass — the corpus-map entry was added 2026-09-03 and `NEEDS-RULING.md` was never regenerated then either — so the committed file does **not** carry the false row-44 clause the pass withdrew; it carries nothing about the work at all. Nothing live is falsified about rows 44 or 65. What is defective is the sweep's own boundary: the pass corrected a machine-readable note precisely because a generated artifact was reading it as state, and stopped one generator short of the fleet-wide artifact whose entire job is to publish those notes. `corpus_map_merge.py` was re-run; `gen_needs_ruling.py` was not, and nothing discloses the gap. Regenerating it touches other worlds' rows, which is why this is also named under CO-022 category 4 below rather than simply as a fix.

### L5 — The Registry Status line says "no count is stated here" and then states a count three times in the same line.

**Where.** `Source_Registry.md` line 3, in sequence within one line:

> `Review-Artifacts/` holds **twenty-seven** `Doc02_Round*_Review.md` files. … **twenty-seven rounds**, disposition 2026-09-08. … **Applying this line's own remedy rather than restating a number that has gone stale nine times: no count is stated here.** … raising "fourteen" to "**twenty-seven**" would otherwise imply a clean record that does not exist.

The remedy sentence is true only of the sentence it replaced. The line states a round count twice and an artifact count once, and then says it does not. Round 28's M4 was that a Status line described its own edit's scope falsely; this is the same shape at a different clause. (The numbers themselves are also wrong — M1.)

**Fix shape.** Either drop the standing counts and let the adjudication live in `lpc_Decision_Log.md` and `Doc02_Round28_Review.md`, or keep them and delete the claim not to be stating any. The current text asserts both.

### L6 — The fourteen act numbers are cited bare, and the *Gesta*'s act numbering is not unique across the file: act 158 sits roughly 5,000 lines *before* act 50, so the fourteen span at least two separately-numbered sequences and a bare number does not locate an act.

**Verified this round by line position**, `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`:

| act | line | act | line |
|---|---|---|---|
| 158 | 121763 | 189 | 128730 |
| 50 | 126795 | 201 | 129008 |
| 53 | 126873 | 206 | 129059 |
| 98 | 127457 | 257 | 129392 |
| 160 | 128392 | 265 | 130239 |
| 162 | 128449 | 272 | 130297 |
| 187 | 128715 | 267 | 130312 |

Act 158's context confirms the reason: at 121763 Augustine is subscribing his mandate before Marcellinus (`… Carlbagiui consliuilus, prtesente viro clarissimo tribuno et notario Marcellino mandatum suscepi et subscripsi`), bracketed by `l.")7. PtUUamt tpiucpit dixii` and `139. PeiHktnat epitcopuÂ» dixit` — a different, earlier sequence from the one containing acts 50–272, which run in order from 126795 onward.

Row 65, the Manifest §3 paragraph and the Decision Log all present the fourteen as one flat list. A reader given "act 158" and "act 50" has no way to know they belong to different sequences, and the file offers no unambiguous way to find 158 from its number alone.

**Why LOW.** The substance is untouched: all fourteen are genuine, all fourteen are Augustine, and the count is right. What is missing is the one clause distinguishing the sequences, and Round 28's C3 established that this row's evidence-kind distinctions are worth stating.

### L7 — Row 65 correctly keeps "Still a floor"; the Manifest and the Decision Log state fourteen flat. The floor is real, and the flat statements overclaim.

**The three sites.**
- `Source_Registry.md` line 83: "an OCR-tolerant line-initial scan across the *Gesta* span returns **fourteen** … **Still a floor: mid-line instances and heavier garblings are not counted.**"
- `Source_Acquisition_Manifest.md` line 69: "it opens a live primary route to Augustine's own recorded voice at the Conference — **he speaks in fourteen numbered acts.**"
- `lpc_Decision_Log.md`, new entry: "Augustine is among the seven Catholic *actores* and **speaks in fourteen numbered acts.**"

**The floor is not rhetorical.** Re-derived this round: a scan tolerant of the ordinary `u`/`v`, `s`/`l`, `i`/`l` substitutions finds thirteen of the fourteen and **misses act 265**, whose formula reads `265. Augutlimu episcoput Eccletim catholkw dixtt.` — the surname garbled past that tolerance. A scan that missed one at that tolerance can miss others. Fourteen is a well-founded floor and is not a count.

This is `co024b`'s cross-document fact-consistency rule — the rule this pass invokes by name for the count disclosures — applied to the claim the pass corrected: the hedge survives in one document and is dropped in the two that restate it.

---

## COSMETIC

### C1 — `Doc_02_Source_Ecology.md` line 160 now trails two paragraphs that supersede it and still says "the disposition **below**."

The paragraph beginning "By the project lead's own direction, 2026-09-08 …" is the last in the file and refers twice to "**the disposition below**" and "**this disposition**." The pointer was already backwards at `0124a9f`; the pass's reordering — inserting a "SUPERSEDED" paragraph above it and a "retained as history" paragraph between — makes it point past the end of the document at a disposition that no longer stands. See also M5, which is the substantive half of the same paragraph.

### C2 — The corrected note asserts, inside `donatism.yaml`, that "Donatism's own corpus-map bucket did not list this work."

`cic/corpus-map/donatism.yaml` line ~209 and its staging source: "**Donatism's own corpus-map bucket did not list this work when this entry was first written; that state has not been re-checked as of this correction.**" This sentence is the note field of the entry for that work, in that bucket. The past-tense reframing the pass added is an improvement on the prior "does not yet list this work," but the sentence still reads, in the file that lists it, as a statement about whether the file lists it. One clause — "the entry you are reading is that listing" — would close it.

### C3 — The count adjudication's "state no count" remedy was applied to the two Status lines and not to `Doc_02_Source_Ecology.md` line 154, which still says "fourteen rounds."

> "… not cured by **fourteen rounds** of recall-test-and-PRESS checking, which is a start on that sweep rather than a substitute for it."

Line 154 sits in §10, outside the "retained as history" framing the pass applied to lines 158–160, and states a round count in the present tense in the same section whose Status line now says no count is stated. Minor, and the sentence's substantive point (the sweep is unrun) is correct and unaffected.

### C4 — The Decision Log records the corpus-map regeneration as `--check` then `--write-only`, which the tool's own help says is the non-authoritative mode.

> "regenerated with `corpus_map_merge.py --check` then `--write-only`."

`corpus_map_merge.py --help`: `--write-only` "**skips pruning entirely** … Use this from inside one build thread's own intake work so it can never touch or prune another world's still-in-progress staging file; **run a plain, full merge (no flags) periodically for the complete, authoritative pass**." A full merge was independently run this round in a scratch copy and reproduces both generated files byte-identically, so **no harm resulted** — but the log records the narrow mode as the whole of the regeneration check, on an edit that deliberately reached into another world's bucket, which is where the pruning question actually bites.

---

## What was checked and found clean

**The XVI.5.21 identification — re-derived from the vendored text alone, not from Round 28's account of it or the fix pass's.**
- **`denis libris auri` occurs at exactly two lines in the whole 94,020-line volume** — 86855 and 86862 — **both inside XVI.5.21**. There is no competing occurrence anywhere.
- **XVI.5.21 is where and as claimed.** Heading at line 86852: `XVI, 5, 21 (392 lun. 15).` Body from 86854: `IDBM AAA. tatiano p(babfecto)f(raetori)o. Id haereticis erroribus quoscumque constiterit vel ordinasse clericos vel suscepisse officium clericorum, denis libris auri viritim multandos esse censemua, locum sane, in quo vetita temptantur, si coniventia domini patuerit, fisci nostri viribus adgregari.` Theodosius I with his co-Augusti; heretical clergy generally; ten pounds of gold each.
- **The scope genuinely matches §25's description, clause for clause.** "any heretical bishop" ↔ `ordinasse clericos`; "or clergyman" ↔ `suscepisse officium clericorum`; "ten pounds of gold" ↔ `denis libris auri`; "each" ↔ `viritim`; "being found in any place" ↔ the law's own `locum sane, in quo vetita temptantur` and its later `si quos talibus repertos`. This is not a loose fit.
- **No rival candidate survives.** Every other "ten pounds of gold" clause in Title 5 *De haereticis* — lines 88517, 88628, 88648 — falls under `XVI, 5, 65 (428 Mai. 30)`, thirty-three years after Theodosius I's death. §25's "Theodosius, of pious memory" rules them all out.
- **The chronology row 44 now states is right.** XVI.5.21 = 392 (heading, read directly). The council = 401 (NPNF endnote 2521, read directly: "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401"). XVI.5.52 = 412 (heading at line 87862, read directly: `XVI, 5, 52 (412 lan. 30>.`). Eleven years, and different Augusti in the inscriptions (`IDBM AAA. tatiano` versus `iDBM AA. sELBvco`).
- **XVI.5.52's own text is exactly as both rounds report it.** Line 87881: `que, circumcelliones argenti pondo decem.`, inside the graduated schedule running `auri pondo quinquaginta … quadraginta … triginta … viginti … quinque`. The silver/gold distinction the withdrawal turns on is real and visible in one line.

**The fourteen-acts count — re-derived without reference to the list.**
- A line-initial numbered-act scan over `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, written before the row's list was read, returns **exactly fourteen** hits and **exactly the fourteen numbers the row names**: 50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, 267, 272. No fifteenth, no number in the row's list that the scan does not return.
- **Every one was checked at its own line.** All fourteen are genuine numbered acts inside the *Gesta*; all fourteen are Augustine; **none is an index, contents or apparatus entry**, and **none is a different speaker**. The surrounding acts at each site are other named disputants (Marcellinus, Emeritus, Alypius, Adeodatus, Petilianus, Montanus), which is what a real act sequence looks like.
- **The apparent out-of-order pair 272 (130297) / 267 (130312) was checked and is not a fabrication.** The local sequence reads 265, 266, 271, 272, 267, 268, 269, 270 — a two-column OCR interleave in the Migne scan, not an invented number. Both acts are real and both are Augustine.
- **Round 28's L2 finding is confirmed exactly**, and the fix pass's adoption of it is faithful, including the retained "Still a floor" hedge and the correct note that act 158 truncates at `158. Augustinus episcop` and carries none of the speech formula.

**The L1 quotation-discipline fix — every string checked against the file.**
- The roster prints `Augustinus  Uipporegiensis.` at line 113075 — exactly the reading the row gives, correctly marked as a normalization rather than a quotation.
- All three garbled speech formulas the row quotes occur verbatim: `50. Augustinus episcopus Eccleshv catholicai dixil.` (126795), `53. Augustinus episcopus Ecclesia; catholicm dixit.` (126873), `160. Augustinus episcopus Ecclesios caUiolicai dixit.` (128392).
- The row no longer presents a normalized string inside quotation marks anywhere. **L1 is properly fixed**, and it is the cleanest of the eighteen fixes.

**The M1 five-attempts correction — checked against `don_Decision_Log.md` attempt by attempt.**
- Attempt 1: `theodosianilibri02code`, the *Prolegomena* (Vol. I Pars Prior). Attempt 2: the sourcelibrary.org DOCX, "rejected on source-integrity grounds," an English paraphrase with inline glosses, CC BY-SA 4.0, with a run of invisible zero-width Unicode characters. Attempts 3–5: "same wrong volume repeated." **Four of five, and the second is the sourcelibrary one — exactly as row 44 and Doc_02 §5 now state, at both sites.**
- **The security caution is restored and intact.** `Source_Acquisition_Manifest.md` line 59 still carries it by name and grounds it in this attempt; row 44 now names it as "the ground of the standing cross-world caution"; Doc_02 §5 names it too. The limb Round 28 said had been erased is back in all three places.
- The don Registry row 16 two-limb formula the fix pass says it now matches ("all resolved to the same wrong volume … or were rejected on source-integrity grounds") was read directly and does say that.

**The corpus-map fix — audited through the generator, not through the diff.**
- **The edit was made in the staging source**, `cic/corpus-map/_staging/codex-theodosianus_latinlibrary.yaml`, exactly as the Decision Log states, and not directly in either generated file.
- **The generated files really did regenerate consistently.** The whole `cic/corpus-map/` tree was copied to a scratch directory and `corpus_map_merge.py` re-run there with **no flags** (the full authoritative pass, not `--write-only`). `diff -r` against the committed tree returns **identical** — every one of the 528 works and 788 assignments, not just the two entries touched.
- **`python3 cic/engine/corpus_map_merge.py --check` exits 0** and reports 528 works → 788 assignments across 56 Atlas entries with no error.
- **Nothing was collaterally changed.** `git diff 9c3ebb3..bc0183d -- cic/corpus-map/` touches three files and exactly two entries — the `latin-pastoral-congregational-christianity` and `donatism` assignment blocks of one staging file, and their two generated reflections. No other work, role, confidence, locus or source_file value moved.
- **The withdrawal is done in place, not by deletion**, in both the staging source and both generated files, with the superseded clause quoted so the record survives — the handling the Decision Log describes.
- **The substance of the new lpc note is correct.** "Letter 185 §25 describes a law of Theodosius I fining heretical clergy ten pounds of GOLD; that is CTh XVI.5.21 (392 Iun. 15)" is accurate, and the note correctly flags that this Latin Library file's own text of XVI.5.21 has not been checked, so the entry stays provisional. It does not repeat H1's misquotation.

**Structural and table integrity — independently re-derived, all clean.**
- **214 table lines, exactly 12 pipe characters on every one**, no exceptions, no stray `|` in the three rewritten cells (which are among the largest in the table). **212 data rows, numbered 1–212, no gap, no duplicate.**
- **Physical-order breaks are exactly the three the front matter discloses** — 48→42, 193→60, 60→52 — unchanged by this pass.
- **Bold-marker nesting, backtick balance, parenthesis balance and bracket balance all clean** on every edited line of all four documents, once code spans are excluded. Registry line 58 returns a +1 parenthesis delta on a naïve count; this was traced to character 7016 and is the **deliberate verbatim reproduction of the scan's own malformed heading** `(412 lan. 30>`, which was verified against the file at line 87862 and is correct as printed. Not a defect.
- Both edited rows keep their eleven columns; rows 44 and 65 retain their `#`, Type, Confidence, Boundary Status, Exclusion Reason, Comparandum, Added and Discovery cells unchanged.

**Findings verified as genuinely fixed, beyond those above.**
- **C1 (the renumbering residue):** `Source_Registry.md` line 3 now reads "stood on the **pre-Round-28** text." Fixed; zero remaining "pre-Round-26" occurrences.
- **C2 (the heading normalization):** row 44 now says the sibling build's records normalize XVI.5.52's heading to "412 Ian. 30" where the scan reads `(412 lan. 30>`, and attributes the normalization to them. Verified against the file; accurate.
- **C4 ("closing" row 14):** row 65 now reads "**correcting — not closing —** that build's own Registry row 14 (which withdrew its erroneous rights finding but deliberately held Confidence at B)." Verified: don Registry row 14 at `don-lpc` is Type P, **Confidence B**, with the note "Confidence held at B rather than raised to A: the file's own text has not yet been read in full."
- **L3 (the "shared corpus" claim):** now reads "in this project's vendored corpus on the sibling Donatism branch — **not on `main`, and not on this branch**." Verified: the file is on neither.
- **L6 (Round 27's M3 uncited):** both Status lines now cite `Doc02_Round27_Review.md`'s M3 by name and carry the Rounds 16–23 history. Round 27's finding counts were re-derived from the artifact itself (0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC = twelve; Round 26: 0 HIGH · 2 MEDIUM · 6 LOW · 4 COSMETIC), and "Rounds 26, 27 and 28 each returned SUBSTANTIAL REVISION REQUIRED" is confirmed true against all three artifacts' own verdict lines.
- **M4 (the misdescribed edit):** the Registry Status line now states the discrepancy in the past tense and repairs it rather than claiming an unrepaired flag. The specific defect Round 28 named is gone.
- **M5's §10 half:** §10's first paragraph is now headed "Disposition — SUPERSEDED," names the reopening, corrects "Round 25, the most recent" to "the most recent **at the time this paragraph was written**," and discloses Round 27's twelve findings. The pointer from the Status line to §10 now resolves to a consistent claim.
- **M6 (no log entry):** written, 28 lines, dated, and substantive.

**A Round 28 claim that does not survive re-derivation, corrected here so it does not propagate.** Round 28's H1 is headed "**Row 44 and Doc_02 §5** identify *CTh* XVI.5.52 as the statute behind the fine …" and its opening summary repeats it. **Doc_02 §5 never carried that claim.** `git show 0124a9f:…/Doc_02_Source_Ecology.md | grep -c "5\.52"` returns **0**, and `grep -c "circumcellion"` returns **0**. The equation existed at one site, `Source_Registry.md` row 44, and nowhere else. The fix pass correctly did not "repair" a site that had no defect and did not repeat the review's error — which is the right handling and is recorded here as clean, not as a finding against the pass.

**Considered and declined as findings.**
- *`cic/texts/REGISTRY.yaml` line 962 still says the OTA copy "left this world without a vendored copy of the text at all."* Read in full. It is a dated provenance note about why the Latin Library file was supplied on 2026-09-02, and the statement remains true of **this branch**, where `theodosianus-16_mommsen-meyer1905.txt` still does not exist. Not falsified by row 44's correction. No finding.
- *`worlds/_cross-world/` beyond `NEEDS-RULING.md`.* `CONSISTENCY-MATRIX.md`, `WANTS-REGISTER.md`, `DOWNLOAD-QUEUE.md`, `CORPUS-USE.md` and `download-queue-seed.yaml` were all swept for row 44, row 65, *Codex Theodosianus*, Mommsen, *Gesta* and the 411 Conference. Nothing in any of them states what either correction withdraws. (Their generators require an `engine` module not importable from a scratch copy, so their currency against the map was not independently re-derived; only `NEEDS-RULING.md` could be and is reported at L4.)
- *The Manifest §3 rule itself was not amended, only carved out by name for row 65.* The rule still says "checking that rule against the table … is authoritative," and mechanically applied it still routes row 65 into §3. But §3 already carries two named transitions out of the category (Monceaux, Goldbacher) on exactly this footing, and the new paragraph applies that precedent explicitly and reasons it. That is the fix Round 28's M3 asked for. No finding.
- *Row 44 retains its Confidence B and row 65 its Confidence C.* Both correct and correctly reasoned against the Registry's own calibration rule; neither row's Licensed-For content has been read against a file on this branch. No finding.
- *Round 28's own count of "eight Type-P rows."* Strictly seven carry the phrase (row 51 is P/S). The miscount is inherited, and it is not what M6 turns on — M6 is that row 58 is unnamed under either count.

---

## CO-022 escalation-category assessment

Run against all four categories, against what the fix pass actually did and the state it leaves, not against its own account of itself.

**1. Representative identity, name, or title decisions — does not apply.** Nothing in the fix pass touches Representative identity, naming or titling. No Representative exists for this world.

**2. Portfolio-level or cross-world strategic decisions — does not apply, and the handling here is an improvement worth recording.** Round 28 noted that the cross-world question raised by both rows — whether to vendor the two sibling-branch files onto this branch or merge `donatism-lpc-integration` — was "one clause from becoming" an escalation and was left unnamed as such. The fix pass names it explicitly in two places: `Source_Acquisition_Manifest.md` line 69 ("**That is a cross-world resource question, not an lpc-ecology one, and it is recorded in `lpc_Decision_Log.md` for the project lead rather than answered here**") and the Decision Log's own "**A cross-world resource question, named as portfolio-level**." Neither decides it. That is the disciplined handling Round 28 asked for and it was delivered.

**3. Governance or methodology decisions — does not apply to the pass, and the live governance question is correctly named and correctly left open.** Doc_02 §10's new paragraph and the Decision Log both state it in the same terms: the 2026-09-08 disposition rests on the project lead's direct instruction to close the cycle after Round 25; Rounds 26, 27 and 28 have each since returned SUBSTANTIAL REVISION REQUIRED; whether a disposition issued that way survives three adverse rounds "is neither a build thread's nor a reviewer's to settle." Verified true on all three counts and correctly not decided. **One thing to add for the project lead, which this round makes visible and the pass does not name:** the count is now **four** consecutive adverse rounds, this one included, and the disposition question compounds with M5 — §10 still contains two live paragraphs reasoning *toward* that disposition and asserting no escalation category applies, in a commit that raised one.

**4. Unresolved tensions the pipeline cannot close on its own — APPLIES, on one ground, and one prior ground is now closed.**

- **Closed, correctly: the `donatism.yaml` contradiction.** Round 28's category-4 escalation was that another world's corpus-map bucket asserted, machine-readably and on row 44's named authority, what row 44 had just withdrawn — and that this build thread could not correct it from where it stood. The pass escalated it, obtained an explicit project-lead direction, corrected it **through the staging source rather than the generated file**, and disclosed the whole chain in `lpc_Decision_Log.md` with the direction quoted. The mechanical execution was independently verified this round and is correct. **This is the right shape and should be treated as the precedent.**
- **Open, and new: the cross-world generated layer below the corpus map.** `worlds/_cross-world/NEEDS-RULING.md` (L4) is generated fleet-wide from `cic/corpus-map/` and lags it by five works and six assignments; regenerating it would rewrite rows belonging to worlds this build thread has no authority over, and it would also publish, fleet-wide, the note this pass just wrote. This build thread cannot close that from where it stands: it can neither leave a stale fleet artifact nor regenerate other worlds' rows on its own authority. **Named here for the project lead or a coach pass**, on exactly the footing the `donatism.yaml` question was named at Round 28.

**On the two project-lead attributions, checked directly as the brief directs.** Both are real chat instructions from this session and both are quoted in `lpc_Decision_Log.md` with dates. **"use lpc-own and open Round 26 for rows 65 and 44"** is represented accurately, including the honest disclosure that the "Round 26" half was renumbered in flight to avoid destroying an existing artifact — a deviation from the literal instruction, disclosed rather than silently taken. **"fix the donatism.yaml note and work the remaining findings"** is quoted exactly and the edit made under it stays within it: correcting the note through `_staging/` is the only mechanism by which `donatism.yaml` *can* be fixed, and the pass says so. The parallel lpc-bucket edit made in the same staging file is a small extension beyond the literal words, but it is in this world's own bucket, is squarely within ordinary authority, and is disclosed by name in the log ("and the parallel lpc entry updated with the XVI.5.21 identification"). **No attribution to the project lead anywhere in the pass lacks a verifiable record, and no new attribution was invented** — the recurring CO-022 failure mode is again absent, as it was at Round 28.

**On Round 27's twelve findings being deferred rather than absorbed — adjudicated, since the brief asks directly.** **The deferral is defensible as a scoping decision and is now properly disclosed, but the stated reason is weaker than the pass presents it.**

*What is defensible.* Round 27's findings were raised against a different object — the 2026-09-08 banner-strip rewrites of the Manifest and Registry — and folding twelve unrelated findings into a two-row sourcing correction genuinely would bury them; the deferral is stated in three places (`Doc_02_Source_Ecology.md` §10, both Status lines, the Decision Log) rather than left for a reviewer to discover from the artifact folder, which is exactly what Round 28's M5 asked for. That is a real improvement and it is not scope evasion: nothing is hidden, and the twelve are now named, counted and recorded in the log for the first time.

*Where the stated reason weakens.* Two of the twelve — Round 27's **M2** and **M3** — attach to `Source_Registry.md` **line 3**, the Status line this pass rewrote for the third time. They are therefore not severable from this pass's scope in the way the disclosure implies. And the consequence is visible in this round's own findings: Round 27's M2 is headed "*deleted both fourteen-round finding-count sequences while keeping every claim built on top of them*," and **M2 above is that same defect, recreated by this pass at the same line by the same mechanism**; Round 27's C1 is headed "*re-staled the very sentence Round 26's C1 fix was written to cure, by the same mechanism, one commit later*," and **M1 above is that, again, one commit later**. A finding you defer against a line you keep rewriting does not stay deferred; it recurs.

*Recommendation, not a decision.* The two Round 27 findings that live on the line this pass edits should be absorbed rather than deferred, and the remaining ten held as declared. That is a scoping call for the project lead, not a reviewer's to make, and it is named here rather than assumed.

---

## Restated verdict

**SUBSTANTIAL REVISION REQUIRED — 1 HIGH · 6 MEDIUM · 7 LOW · 4 COSMETIC.**

This is a better fix pass than the revision it repairs, and its two hardest new claims hold under independent re-derivation from the primary texts: *CTh* XVI.5.21 really is the law Augustine's Letter 185 §25 describes, and it is the only law in the vendored volume that can be; Augustine really does speak in exactly the fourteen numbered acts the row lists, every one checked at its own line; the sibling build's five acquisition attempts really do break four-and-one as row 44 now says; and the corpus-map correction was executed correctly through the staging source, with the generated output independently reproduced byte-identically by a full re-merge. Of the eighteen findings, thirteen are genuinely and cleanly fixed.

What fails is, once again, the layer above the verified fact. **H1** puts a quotation into the Registry of record attributed to a paragraph it is not in — it is from a different work in the same volume — inside the very sentence asserting that the paragraph was read directly this round. That is Round 28's HIGH recurring one layer down, in the sentence written to cure it. **M1** restates the stale review-round count the same line adjudicates, at a commit where the number is demonstrably one higher and where the same sentence reports the round that makes it so. **M2** and **M3** are self-contradictions the pass created: a deleted count that unbounded two surviving claims, a "1 HIGH" inserted into a line asserting HIGH has stayed at zero, and three sites declaring a log entry absent in the commit that writes it. **M4**, **M5** and **M6** are the propagation shape for an eighth consecutive round — a Manifest edited but not re-stated, a §10 half-marked, and a sweep disclosed as complete that misses the row whose public-domain alternative is already sitting in `cic/texts/`.

One escalation category applies. **CO-022 category 4** is triggered afresh by the fleet-wide generated layer below the corpus map (`NEEDS-RULING.md`, L4), which this build thread can neither leave stale nor regenerate on its own authority — and the `donatism.yaml` category-4 escalation Round 28 raised is, by contrast, **properly closed**: escalated, directed, executed through the staging source, and disclosed. The governance question — whether the 2026-09-08 disposition survives what are now four consecutive adverse rounds — remains live, is correctly named by the pass, and is named again here for the project lead rather than decided.

Neither `Doc_02_Source_Ecology.md` nor `Source_Registry.md` is eligible for any disposition on this text, and `Source_Acquisition_Manifest.md`, materially edited in this pass, should be brought explicitly into the same state rather than left carrying a Disposition paragraph that says the cycle has concluded (M4). All three should stay REOPENED.

*This artifact is `Doc02_Round29_Review.md`. `Doc02_Round29_Review.md` did not exist before this round; no existing review artifact was read to, written to, or modified, and no file in the repository was changed by this review other than the creation of this one.*
