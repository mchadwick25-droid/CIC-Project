# Round 3 review of Doc_01 (a combined review of Steps 0 to 2)

# Independent Adversarial Review, Round 2 (targeted recheck): The Methodist Revival (`meth`), Steps 0–2

I worked read-only in `/home/user/CIC-Project/.claude/worktrees/agent-a96deecff567a597c` at HEAD `cd1d06a6`. I wrote nothing. The only tool I ran was `tools/check_live_commentary.py`, which reports without writing, and `git status` stayed clean. I read the brief and the real Round 1 file (the Round 2 review file). Every claim below with a line number was checked against the vendored file, the live census JSON, or the Framework V7.4 docx.

## Verdicts

| Document | Verdict |
|---|---|
| Step 0 | **Cleared on substance.** Leftover problems are one repeated P1 (process narration) and some P2s. A mechanical fix-up is enough; no new review round is needed. |
| Doc_01 | **Still substantial.** §4's conclusion is defensible, but its argument was adopted from Round 1 rather than re-tested. §9 is not yet well-formed. One Round 1 P0 location was never fixed (the Decision Log). One Round 1 P1 is unfixed (the stale census quote in §2). |
| Doc_02, Registry, Manifest, corpus-map, `PAIRS.yaml` | **Still substantial, but narrow.** Most voice and count fixes landed and check out. Three P1s remain: Registry row 13 pre-decides against Option A, the `PAIRS.yaml` relation is wrong, and the fix added new process narration to the live corpus-map. |

## The central question: does Doc_01 §4 hold up on its own merits?

**The conclusion is defensible. The argument was largely laundered from Round 1.** The bullets repeat Round 1's table almost word for word:
- "Two of this world's four named candidate gravities are absent or directly contradicted"
- "Partial, not decisive"
- "Arguably yes — the predestination dispute…"

None of it was independently re-tested. Specific problems:

1. **The gravity question is circular (P1).** §3 (line 51) names the free-grace gravity *as* "directly counterposed to Whitefield's own Calvinism". §4 (line 61) then finds that Whitefield diverges from it. §3 also calls these gravities "preliminary, subject to Doc_04". So the whole separate-world finding depends on Doc_04 upholding two provisional gravities, and that dependency is never disclosed.

2. **One dispute is counted twice (P1).** Predestination drives both "gravity: yes" (line 61) and "interpretation: arguably yes" (line 63). Line 67 then reads the tally as "a real, if not unanimous, case". Remove the double count and the §4-versus-§5 split rests on one doctrinal disagreement.
   - Also, the Framework (V7.4, "World Separation Criteria") frames the six questions as "When does one world become another?" with "Questions include…". That is a heuristic for change over time, not a scored tally for a rival movement of the same period. Neither Round 1 nor the rewrite notices this.
   - Line 61 still folds two Framework questions into one bullet.

3. **The test mixes levels (P1).** Line 59 says the test runs on "his post-1741 organized Calvinistic Methodism… not at the level of his own person". But the two strongest "yes" answers (lines 61 and 63) describe Whitefield's personal theology. That theology was public from 1739 onward, inside the 1738–41 window that Option B keeps in this world. So §4 does not support B's date split, although B claims to "match how… §4 already argues the underlying six-question case, at the level of institutional legacy".

4. **Step 0's binding rule is broken (P1).** Step 0 §4 item 6 (line 99) says any description of Whitefield's theology must be flagged as second-hand. Line 61 ("his own Calvinism holds unconditional election, and his own soteriology has no place for a doctrine of sinless perfection") carries no such flag and no confidence tag. "Sinless perfection" is also the opponents' framing of this world's own gravity, which is a fidelity problem in exactly the sentence doing the work.

5. **Vendored evidence that bears directly on §4 and §9 was never consulted (P1).** Round 1 missed it too. Asbury's own vendored voice says:
   - `asbury_journal-v2_1821.txt` lines 17961–17963 (1798), at "dear Whitefield's tomb": "His sermons established me in the doctrines of the Gospel more than any thing I ever heard or had read at that time". The founder of this world's American strand credits Whitefield with forming him.
   - `asbury_journal-v3_1821.txt` lines 19339–19341 (1815): "the Whitefield Methodists, called New Lights, laboured with success: the Wesleyan Methodists are heirs to these".
   - Against that: v1 lines 17714–17718 ("first awakened by Mr. Whitefield, afterward convinced by reading Mr. Wesley's sermon on Falling from Grace; and now a fast friend, and member of our society"), and v1 line 15477 ("they may follow Mr. Whitefield in Calvinism"). These show the doctrinal boundary working at the level of ordinary members.
   - v2 line 8618 (1793): Asbury visits "Mr. Whitefield's Orphan-House", which is Whitefield's post-1741 Bethesda.

   So the world's own texts both confirm the doctrinal line and claim Whitefield as a forebear. Doc_02 §6 (line 84) and Registry row 13 say every Whitefield characterization comes from "Wesley's/Asbury's own references", yet Asbury's references were never actually used.

6. **The "independent re-confirmation" is circular (P1).** §9 (line 142) says §4's finding "stands, independently re-confirmed at this review". The table is Round 1's own, and it is certified by citing Round 1's own approval. That is not independent re-confirmation under CLAUDE.md.

**What is fixed:** the scoring is no longer inverted, the false census-corroboration claim is withdrawn (line 69), and §4 and §5 are now consistent with each other.

## Is §9's escalation now well-formed enough for Mark to rule on it as presented?

**Not yet.** The three options are distinct, and the recommendation language is legitimate under CLAUDE.md. But:

- **B has no stated cost, while A and C each get one. B's one stated advantage is false (P1).** Line 144 says B "keeps every currently-accurate census field intact".
  - The census story "Whitefield Asks for Slaves" is dated "1740 – 1770". Nearly all of it is post-1741: the 1747 plantation, the December 1748 letter, legal slavery from 1751. It ends with Whitefield leaving Bethesda and "the roughly fifty people it owned to the Countess of Huntingdon" — the very Huntingdon line that B moves out of this world.
  - B's split is also contradicted by the Asbury passages above.
- **B's destinations are not described accurately (P1).**
  - VII.6 is New England, 1734–c.1760, and cannot hold English Calvinistic Methodism.
  - For VII.10, the census says "The Welsh revival began independently of England" and does not list Whitefield among its voices. Doc_01 line 142 and OGT item 21 ("VII.10 itself constituted as his own Calvinistic-Methodist line", "his own preaching helped set going") and Doc_02 §7 line 99 ("the census's own home for Whitefield's… line") all overstate this.
  - In practice, B requires a new census entry. That is a portfolio cost, and it is never stated as one.
- **C cites the wrong precedent (P2).** It says the "corpus-map already uses" multi-home assignment for Asbury and Allen. The multi-home assignment is in the census `voices` field; the only Asbury corpus-map rows are this world's own. C is also close to the current census state: Whitefield is already a voice of both VII.5 and VII.6. So "leaves the underlying allocation question formally undecided" understates it, and C never says whether Whitefield's Calvinistic organization sits inside VII.5's story.
- **All three options presuppose §4.** None lets Mark reject §4's separation premise. That premise is itself the cross-world decision, and it rests on provisional gravities (see point 1 above).
- **A quiet pre-decision sits in the sibling documents.**
  - Doc_02 line 84 says: "Source Registry (row 13) accordingly marks him Boundary Status 'Native' — his own person and 1738–41 presence are squarely part of this world's story, whatever the eventual ruling". That is only true under B or C, so it rules out A.
  - That contradicts Doc_02 §10 (line 136, content "correct regardless") and Doc_01 line 153.
  - Registry row 13's "own (Whitefield's — a different own-voice)" also conflicts with the Registry's own definition of "opponent (a rival or contemporary movement's own voice)".
- **The disposition is inconsistent across documents (P0, the unfixed location of Round 1 P0-2/P0-3).** `meth_Decision_Log.md` was changed only by a row count.
  - Line 26 still says the census "corroborated" the Whitefield finding ("no Whitefield source named, no descendant tradition traced through his line").
  - Line 28 still reads "Disposition: Approved to proceed, self-applied" for Doc_01.
  - Line 42 lists Whitefield under "Decided… no escalation required".
  - No round-2 entry was appended, yet Doc_01 §9 and OGT item 20 send readers there for "the complete, itemized account".
  - Doc_02 line 6 also calls Doc_01 "(Approved to proceed)".
  - Doc_01's own header (line 3) says "those parts of this document are self-disposed 'Approved to proceed'", while §9 (line 151) uses the conditional "would self-dispose".

**What Mark needs before ruling:**
- B's real costs: the Slaves story and the Huntingdon bequest, and the need for a new census entry.
- The Asbury evidence.
- The fact that §4 depends on Doc_04.
- Row 13 made neutral.
- The Decision Log corrected by an appended entry.

## Other checklist items

**Step 0**
- **Confirmed correct:**
  - The Zinzendorf sequence matches Widely Accepted historiography: banished 1736, met at Marienborn in July 1738, Herrnhut in August.
  - `statusWord` "Researched — strong candidate" matches the live census.
  - Sermon III: the heading is at line 1204 and footnote 6 at lines 8298–8299 ("by the Rev. Mr. Charles Wesley").
  - Item 7 (Article 20) and item 3 (review independence) now point to the right OGT entries.
- **Process narration (P1, repeat).** The "B1 correction narrative" still exists word for word (line 70). The fix added about six new "corrected at independent review" asides (lines 5, 11, 37, 38, 40, 63).
- **Cross-reference and small errors (P2):**
  - Line 5 cites OGT item 1 for the statusWord change; item 1 is the version-discrepancy entry.
  - "Items 1 and 16" (line 7, and Doc_01/Doc_02 line 6) should be items 1 and 17. Item 17 is the V1.8 closure; item 16 is about the holdings tool.
  - Line 38's "per Doc_01 §2" should be §7.
  - `dateRationale` (line 19) is not a field in the census.
  - Line 62 says "birth through… 24 May 1738", which is inconsistent with the June end of the volume.
- **A3.4 neighbour list (P2).** It omits VIII.4, the Holiness movement, which has a census edge `the-methodist-revival → the-holiness-movement`, type `formed`, `Documented`. It also omits VI.26, the Remonstrants, which the census names as the source of Wesley's "Arminian" label. The six one-line characterizations it does give are accurate.

**Doc_01, §§5 and 7**
- **§5 Whatcoat 1787.** This is accurate as Widely Accepted historiography. A better, vendored source exists in `asbury_journal-v2_1821.txt` lines 8606–8609 (1793): "Because I did not establish Mr. Wesley's absolute authority over the American connexion: — for myself, this I had submitted to; but the Americans were too jealous to bind themselves to yield to him in all things relative to church-government." §5's statement "not independently vendor-verified" can be upgraded.
- **§7 Böhler.** §12 is at line 26881; §11 actually starts at 26858, where OCR reads "ii.". Böhler also appears in the dated entries from 7 February 1738 (line 24493). The storm passage (around 6983) and Nitschmann (line 5224) are confirmed.
- **§7 Fetter Lane (P2).** Wesley's own dated entry for 1 May 1738 (lines 26031–26037, "This evening our little society began, which afterwards met in Fetter Lane") is primary evidence. It is stronger than the Curnock footnote cited "near 27040", which is actually at line 27056.
- **§7 "ends 8 June 1738" (P2).** Only half right. The Germany resolution is the **Wed. 7** entry (line 27667), not 8 June. The Thur. 8 entry runs on to the embarkation on "Tuesday the 13th… Gravesend" before "END OF VOL. I." The core claim, that Herrnhut is not in Vol. I, holds. The same "8 June" wording appears in Registry row 1, the corpus-map, and OGT items 6 and 18.
- **§2, unfixed Round 1 findings:**
  - (P1) Line 22 still quotes as verbatim a census `statusDescription` ("Its end moved to 1815 under the continues-cap convention… the discarded round-1800…") that no longer exists. The live text is "Tiered Strong (Tier 1)… Its window ends in 1815. Wesley's death…"; the old wording last appears in commit d1abf887.
  - (P2) Line 33 still cites Large Minutes lines 379–381. The quotation actually ends at line **387** ("others to do the same."), so Round 1's "386" was itself one line off. The fix copied 386 into Registry row 3 and the corpus-map without re-checking the file.
  - (P2) Also unfixed from Round 1: Asbury's death as "one year" after 7 Dec 1815, the anti-slavery rule "within a few years", and the "directly attested" Wesley recoil, which rests on a census story marked "primary text not yet read".
- **`records/worlds/meth.yaml`.** All three Round 1 doorway errors are fixed. Two new P2s: "bishop-led church in 1784" is anachronistic (the title was superintendent until 1787), and one participant-facing sentence runs about 65 words, far over the roughly 25-word ceiling.

**Doc_02 set**
- **Confirmed correct:**
  - The corpus-map has 12 rows, with Sermon III as `wesley-charles`, the Large Minutes as `wesleyan-conference` (institutional voice), and the Curnock introduction as `curnock-nehemiah` (the lines ~1745–1770 locus is right).
  - Asbury's word count: 197,367 + 184,476 + 187,327 = 569,170 of 1,005,750, which is 56.6%. I re-ran `wc -w`.
  - Registry row 4: the Preface ends at lines 257–258. The sermon headings at 490 and 7595 are correct.
  - The Manifest's false queue claim is withdrawn, and only G1 is in the queue.
- **New counting errors (P2):**
  - "~299,000" for Wesley is the total *before* removing Sermon III. Journal 208,889 + Sermons 89,972 − Sermon III 4,936 = 293,925.
  - "~29 remaining" sermons should be 28 (44 − 16). This appears in Doc_02 line 29, Registry row 10, Manifest G2, the corpus-map, and Step 0. OGT item 10 still says "~32".
- **`PAIRS.yaml` (P1):**
  - "One-way" is ruled on what happens to be vendored, and the entry admits the historical relationship "was not" one-way. The pair semantics in `Build/Ministry/Features/Library-Access-Gate/D3-Converged-Design.md` (CM-3/Q2) classify documented exchange between traditions, and the stillness controversy is exactly that kind of exchange.
  - The `direction: a->b|b->a` field that CM-3 requires for one-way pairs is missing.
  - The file's own header says it "carries only the fixture pair" and that real fleet pairs are "corpus-map's own thread's judgment call". The header is now wrong, and the ruling was made outside its stated owner.
  - The evidence cites lines 27070–27074, which do not mention the Moravians.
- **New commentary in the live canonical corpus-map (P1).** The fix itself added narration such as "corrected at independent review", "Corrects a round-1 misattribution… (Doc_02 Independent Review Round 1, P1)" and "Translation note, added at independent review" to `the-methodist-revival.yaml` (lines 46–48, 65–69, 81–83, 129–130, 149–150) and to its `_staging/` files. `check_live_commentary.py` flags them.
- **Smaller issues (P2):**
  - §7 omits VIII.4, even though OGT item 20 calls the list "complete".
  - VII.6 is described as the "clearest direct figure-overlap this world's own corpus-map carries", but the corpus-map carries no Whitefield row.
  - Manifest G1 still says "All 8 volumes are hosted" when only four were checked.
  - Asbury is still described as "complete across the full window" (Round 1 P2, unfixed).
  - "Bishop-elect" should be "bishop".

**Open_Gaps_Tracking.md**
- The OGT numbers cited in the documents match the live file, except the "items 1 and 16" and Step 0 line 5 errors above.
- **Append-only rule broken (P1).** Items 6, 14 and 16 were edited in place (item 6 was fully rewritten; see `git diff 9f2aa29e HEAD`).
- Items 12 (the invented OCR defect) and 10 ("~32") still state false claims, with no pointer to their corrections.
- Documents still cite gaps by bare number instead of subject and date.

## Bottom line

- The build thread fixed the factual errors well.
- It did **not** re-test the §4 argument independently.
- The escalation cannot be ruled on as presented yet: B's costs are hidden and its one stated advantage is false; Doc_02/Registry row 13 already act as if A is ruled out; and the Decision Log still records Doc_01 as "Approved to proceed" with the Whitefield question decided.
- Every item above is fixable in one targeted round without re-arguing the conclusion.

## Disposition

Disposition: Not approved to proceed.

The text finds Doc_01 still substantial; Section 9 escalates the Whitefield allocation question to the project lead, and no ruling is recorded. The text describes itself as an independent cross-model review. PR #616 records every review round as a same-thread self-review, and no reviewer agent, session or model identifier accompanies the file. This filing does not treat it as an independent review, and the verdict below is not a clearance. A later recheck that the branch's commit message 8e187eaa9 describes has no review file in the repository, so no clearance of any kind is on record.
