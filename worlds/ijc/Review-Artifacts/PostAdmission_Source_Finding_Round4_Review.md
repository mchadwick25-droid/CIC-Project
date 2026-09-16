# Post-Admission Source Finding (Philostorgius / *Opus Imperfectum*) — Round 4 Independent Adversarial Review

**Reviewed document:** `Post_Admission_Source_Finding_Philostorgius_OpusImperfectum_2026-09-09.md`
**Also reviewed:** `Open_Gaps_Tracking.md` item 16, for consistency with the above
**Reviewer:** independent isolated agent (Opus), no drafting involvement in the reviewed document, in item 16, or in any prior review
**Branch reviewed:** `claude/ijc-philostorgius-opus-imperfectum-finding`. **The document changed under this review.** I began against `3f6397e2` (the post-Round-3 revision) and finished against `b663348f` ("drop the tooling-defect enumeration, state the defect qualitatively"), committed at 02:21 while this review was running. Findings below are stated against the **current** text at `b663348f`; where a finding applies only to the superseded text it is marked as history.
**Round 4 findings are numbered Q1–Q17.**
**Overall verdict: SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**Bottom line.** I recomputed §5 item 4's enumeration from `engine/m1/cross_world.py` and `cic/texts/` before it was deleted. **Every one of the six figures was correct, and the fourteen-key list was correct member for member.** 14 keys, 18 files, 65 vendored files, 60 distinct keys, 44 `COVERAGE` entries, 2 `BY_DESIGN` — all verified by direct parse. The enumeration was deleted at the exact moment it had finally become right, and the two things in that item that are *still* wrong were kept: the stated cause of the earlier error is false, and the Tier 1 bounding sentence is inoperative for the cohort it bounds. Both survive verbatim into the replacement text, which means the pre-declaration at §7 and item 16 that this review's findings on that item are "overtaken" is itself wrong.

Separately and more seriously: the edit propagated to §5, §7, the headline and item 16 and **did not reach §6**, which now contains two stale claims — one citing a "six worlds" figure the document no longer states, and one that is a full round out of date, saying two reviews have been filed and a Round 3 is required. §6 is the section that gates self-disposition, and this is the second time that same paragraph has gone stale (Round 2 caught the first). That is the same failure class, for the fourth consecutive round, introduced *by the edit that was supposed to end it*.

And the edit rests on a verbatim quotation attributed to the project lead — *"drop the enumeration and state the defect qualitatively"* — for which there is no verifiable record anywhere in this repository, in a document whose own §0 goes to real trouble to paraphrase rather than quote an unverifiable off-repo instruction for exactly this reason.

**The headline verdict survives a fourth attempt.** I re-derived it from `Doc_04_Gravity_Discovery.md`, the vendored Philostorgius file, `Source_Registry.md` and `Doc_08_Forces_Document.md` without reference to any prior round's argument. Neither acquisition is structural for Doc_04. Nothing moves. Said plainly, because it has now been established four independent times: on the substantive historical question, this document is right.

---

## Half A, part 1 — §5 item 4's enumeration, recomputed from scratch

Done by direct parse of the `COVERAGE` and `BY_DESIGN` literals in `engine/m1/cross_world.py` (lines 80–95) and of `cic/texts/`, using the module's own `corpus_key()` rule (`re.split(r"[_.]", filename)[0]`) and `gen_corpus_table.py`'s own file filter (`p.suffix in (".xml", ".txt")`, excluding `README.md`).

| figure the document claimed | my recomputation | status |
|---|---|---|
| 14 `COVERAGE` keys | **14** | ✔ |
| 18 vendored files | **18** | ✔ |
| 65 vendored files | **65** | ✔ |
| 60 distinct keys | **60** | ✔ |
| 44 `COVERAGE` entries | **44** | ✔ |
| 2 `BY_DESIGN` (`anf10`, `webbe`) | **2**, exactly those | ✔ |

Arithmetic closes: 44 + 2 + 14 = 60. The fourteen-key list — `anan-isho`, `basil`, `eunomius`, `evagrius`, `gregory-nazianzen`, `gregory-nyssa`, `julian`, `lucian`, `macarius`, `morison`, `nestle1904`, `pachomius`, `philostorgius`, `tacitus` — matches my computed set member for member, with no additions and no omissions. The 18 files under those keys are the expected ones (`basil`, `gregory-nazianzen`, `gregory-nyssa` and `julian` carry two files each; the other ten carry one). Every `COVERAGE` key has at least one vendored file, so no key is orphaned.

Also verified directly, and holding:

- **`grep -ci cappadocian worlds/_cross-world/CORPUS-USE.md` returns 0.** ✔ Confirmed.
- **CORPUS-USE.md's header counts 64 against 65 on disk.** ✔ Confirmed, and I identified the discrepancy exactly: the report is stale by precisely one file, `nestle1904_greek-new-testament-grc.txt`, which appears nowhere in it.
- **Refinement (i).** `corpus_tier()` returns `"4 - unclassified"` (line 205), distinct from `"4 - outside this window"` (line 213); CORPUS-USE.md line 153's legend documents only the latter sense. ✔ The label-collision diagnosis is right.
- **Lines 140, 142 and 153 of CORPUS-USE.md** carry, respectively, Mark's 2026-08-26 "ranked, but not ignored" standard, the `engine/m4`-never-opens-`cic/texts/` mechanism with the "a source record exists (even a low-ranked one)" clause, and the Tier 4 legend row. ✔ All three verbatim at the cited lines.
- **`cappadocian` is `state: admitted` in `records/worlds.yaml`** (line 200), so the current §5's "the per-world report covers most but not all of the built worlds" is true. ✔

**Two things in that item are wrong, and both survived the deletion.** They are Q3 and Q4 below.

---

## Half A, part 2 — Round 3 findings R1–R21: does each fix hold?

| Round 3 | Fix status | Where |
|---|---|---|
| R1 (HIGH) — recount wrong, six keys falsely listed | **HOLDS on the number** (all six figures verified correct before deletion); **DOES NOT HOLD on the cause**, which is false and survives the deletion | Q3 |
| R2 (HIGH) — corrected figures surviving two lines below their own correction | **HOLDS in §5, §7, headline and item 16**; **DOES NOT HOLD in §6**, which the new edit did not reach | Q1 |
| R3 (MEDIUM) — impossible keys-vs-files reconciliation | **HOLDS** — withdrawn and named as a rationalization | clean list |
| R4 (MEDIUM) — false cappadocian rationale | **HOLDS** — corrected, and I re-verified both halves (grep = 0; the record does exist) | clean list |
| R5 (MEDIUM) — unclassified vs rendered Tier 4 conflated | **DOES NOT HOLD** — the distinction is drawn on a mechanism that cannot operate for this cohort, and the mechanism that does operate is unstated | Q4 |
| R6 (MEDIUM) — item 16's Doc_08 §7/§9 locators | **HOLDS** — item 16 now reads "Doc_08 Section 6 and Section 8, Doc_08's Open Items and Process Findings (item 2)"; all three verified against Doc_08 | clean list |
| R7 (MEDIUM) — Dekkers re-misattributed | **UNVERIFIABLE, and unmarked as such** — moved to a third channel this environment cannot reach | Q8 |
| R8 (MEDIUM) — item 16 mis-states Round 2's tally | **HOLDS** — "two new HIGH … plus eight MEDIUM and six LOW" matches the Round 2 file's own headings exactly | clean list |
| R9 (MEDIUM) — "constrains what a Round N should re-examine" | **HOLDS** — replaced in both entries with "not as a licence to skip re-checking" | clean list |
| R10 (MEDIUM) — "in two cases" | **HOLDS** — corrected to one, with the miscount disclosed | clean list |
| R11 (MEDIUM) — Doc_08 Section 6 omitted | **HOLDS** — added at §2.3 and at item 16; I read Section 6 and the "exactly one substantial instance" sentence is verbatim at its "What Selection Effects Shaped What Survives" subsection | clean list |
| R12 (LOW) — §0/§1 "paraphrases" near-verbatim | **DOES NOT HOLD** — §0 line 13 is unchanged, and §7 mislabels a different finding as R12 | Q15, Q7 |
| R13 (LOW) — unmarked "Constantine"→"Constantius" | **HOLDS** — now marked as Walford's slip; I confirmed the file reads "Constantine" at that point and "Constantius" nine lines later in the same chapter | clean list |
| R14 (LOW) — README quotation truncated with no closing ellipsis | **DOES NOT HOLD** — unchanged | Q13 |
| R15 (LOW) — 300–425 asserted without its locator | **DOES NOT HOLD** — unchanged, third consecutive round | Q10 |
| R16 (LOW) — Candidate 6 a bare negative | **DOES NOT HOLD** — unchanged | Q11 |
| R17 (LOW) — "Confidence A" shorthand | **DOES NOT HOLD** — unchanged in §7 and item 16 | Q12 |
| R18 (LOW) — §7's Round 2 entry overstates | **HOLDS in part** — the F5 bullet now discloses that the Round 2 correction was itself wrong; "M9 … Both corrected" still overstates, since the Dekkers half was re-misattributed | Q8 |
| R19 (LOW) — §7 silent on Round 2's LOWs | **DOES NOT HOLD, and recurs a generation later** for Round 3's ten LOWs | Q7 |
| R20 (LOW) — un-indented paragraph breaking out of the list | **DOES NOT HOLD** — and the un-indented block has grown from one paragraph to four | Q14 |
| R21 (LOW) — item 16 names only the Round 1 review file | **DOES NOT HOLD** — now reports three verdicts and still names one path | Q9 |

**Summary: 11 of 21 hold; 10 do not** (R5, R7, R12, R14, R15, R16, R17, R19, R20, R21 in full, plus R1's causal half, R2 in §6 and R18 in part).

---

## HIGH

**Q1. The mid-review edit propagated to four places and missed §6, which now contradicts the rest of the document twice — the same failure class, fourth consecutive round, in the section that gates self-disposition.**

Commit `b663348f` changed the headline, §5 item 4, §7 and `Open_Gaps_Tracking.md` item 16. It did not touch §6. Two consequences:

- **§6 line 217** reads: *"(b) The `engine/m1/cross_world.py` ranking defect at §5 item 4, **which this document itself describes as reaching six worlds** — it is portfolio-level by its own account."* §5 item 4 no longer describes it as reaching six worlds. It now says *"the per-world report covers most but not all of the built worlds"* and gives no count at all, deliberately. §6 cites the document for a claim the document has stopped making — which is the R2 pattern (a corrected figure surviving elsewhere) inverted: the correction landed everywhere except the one section that quotes it.
- **§6 line 221** reads: *"**Disposition: none, and none is claimed.** **Two** independent adversarial review rounds have been filed as files in `Review-Artifacts/` (Round 1 … Round 2 …). … Because Round 2 called for substantial revision and this document has since been revised again, `cic-build-cycle` requires it to go back through review: **a Round 3 is required before any disposition is considered.**"* Three rounds have been filed. The status line at line 3 says "Awaiting Round 4"; §7 line 271 says a **Round 4** is required; item 16 says a Round 4 is required. §6 alone still says two and Round 3.

The aggravating fact is four lines below it: §6 carries a parenthetical disclosing that *this same paragraph* went stale once before and was caught at Round 2 (F11). It has now gone stale again, in the same way, in the same paragraph, one round later — and neither §6 nor the Round 3 file names where the Round 3 review artifact lives, which `cic-build-cycle` requires of the log.

Severity HIGH because §6 is the escalation self-assessment that gates whether this thread may self-dispose, and because a reader who opens §6 alone is told the document needs a review round it has already had.

**Q2. A verbatim quotation is attributed to the project lead, in three places, with no verifiable record — the exact failure mode `cic-build-cycle` (CO-022) names.**

- §5 line 198: *"**Scope, stated qualitatively — on the project lead's own instruction, 2026-09-09.**"*
- §5 line 200: *"On the fourth pass the project lead directed that the enumeration be dropped and the defect stated qualitatively."*
- §7 line 273: *"**Resolved by the project lead, 2026-09-09: "drop the enumeration and state the defect qualitatively."**"*
- `Open_Gaps_Tracking.md` item 16: *"Mark's resolution, 2026-09-09: drop the enumeration and state the defect qualitatively. Applied."*
- The commit message itself: *"Project lead's instruction, 2026-09-09: 'drop the enumeration and state the defect qualitatively.'"*

`cic-build-cycle`, Disposition: *"**Nothing is attributed to 'the project lead' anywhere in any document — a quote, a decision, an instruction — without a verifiable record that the project lead actually said or wrote it.** Hold this to the same bar as Frozen: a real, checkable record, not a claim."* CO-022's preamble names *"content fabricated-attributed to 'the project lead'"* as one of four specific failure modes this version of the skill exists to close.

A repo-wide grep for the quoted instruction returns only this document, item 16 and the commit message. There is no session artifact, no decision file, no Decision Log entry. I am not alleging fabrication — I have no way to know — and the instruction may well be exactly what Mark said. That is precisely the point of the rule: *unverifiable is not good enough*, and the bar is a checkable record, not the plausibility of the claim.

Three things make this worse than a bare rule breach:

1. **The document already knows better.** §0 contains a whole disclosed paragraph explaining that the commissioning brief is an off-repository session instruction, that no later reader can open it, that a repo-wide grep for its phrases returns nothing, and that therefore *"the brief is paraphrased rather than quoted throughout and its unverifiability is disclosed rather than left for a reader to discover."* Two sections later the same document quotes the project lead verbatim on an equally unverifiable off-repo instruction, with no such disclosure. The discipline is applied to the party whose words weakened the document and not to the party whose words authorised deleting content.
2. **The quoted words are near-verbatim the document's own prior proposal.** The superseded §7 read: *"the right response is probably to **delete the enumeration and state the defect qualitatively** rather than to correct the number a fourth time."* The instruction quoted back is *"drop the enumeration and state the defect qualitatively."* A recommendation the document wrote for itself now returns as a project-lead quotation authorising exactly that action. That may be simple concurrence; it is also indistinguishable, on the record as it stands, from the document approving its own proposal in the lead's voice.
3. **§7 asserts the opposite three lines above.** The "Round 3 verified clean" paragraph at line 269 ends: *"no unsupported project-lead attribution … across all three rounds."* That sentence is now four lines above an unsupported project-lead attribution.

**Q3. The stated cause of the "22" error is false, and it is falsified by the very list Round 3 quoted. It survives the deletion in two places.**

Current §5 line 200: *"then a recomputed key count that was itself wrong (**a regex matched only the first key on each line of the `COVERAGE` literal, so keys sitting mid-line read as absent**)."* Current §7, R1 bullet: *"Cause found and recorded at §5 — **a regex matching only the first key on each line of the literal**."* The commit message repeats it a third time.

I simulated it. `re.findall(r'^\s+"([\w-]+)":', <the COVERAGE literal>, re.M)` — a regex that matches only the first key on each line — returns **13** keys: `addai`, `anf04`, `anf08`, `chronicle-of-edessa`, `npnf101`, `npnf105`, `npnf109`, `npnf113`, `npnf201`, `npnf205`, `npnf209`, `npnf213`, `origen`. Under that hypothesis the missing cohort would be **47 of 60 keys**, not 22.

The falsification is sharper than the arithmetic. Round 3's R1 quotes the Round 2 list in full: the twenty-two were `anan-isho`, `anf10`, `basil`, `eunomius`, `evagrius`, `gregory-nazianzen`, `gregory-nyssa`, `julian`, `lucian`, `macarius`, `morison`, `nestle1904`, **`npnf102`, `npnf103`, `npnf106`, `npnf108`, `npnf110`, `npnf114`**, `pachomius`, `philostorgius`, `tacitus`, `webbe`. Set against my recomputation, exactly six entries are false — the six `npnf1xx` — and the other sixteen are the true fourteen plus the two `BY_DESIGN` keys. So Round 2's parse correctly identified **38** of the 44 `COVERAGE` keys as present, including twenty-five that sit **mid-line**: `anf01`, `anf02`, `anf03`, `anf05`, `anf06`, `anf07`, `anf09`, `aphrahat`, `ephraim`, `npnf104`, `npnf107`, `npnf111`, `npnf112`, `npnf202`, `npnf203`, `npnf204`, `npnf206`, `npnf207`, `npnf208`, `npnf210`, `npnf211`, `npnf212`, `npnf214`, `optatus`, `palladius`. A regex that saw only the first key on each line could not have found any of them. It would also have had to miss `npnf104`, `npnf107`, `npnf111` and `npnf112` — four mid-line `npnf1xx` keys sitting on the same lines 85–88 — which it did not.

Asked directly whether this is a plausible and honestly-stated diagnosis: **it is neither.** It is not plausible, because it is off by a factor of more than two and contradicted by twenty-five entries of the list it purports to explain. And it is not honestly stated, because it is presented as a found cause (*"Cause found and recorded at §5"*) in a document whose whole disciplinary theme is not asserting more than has been checked. The honest statement available on the evidence is narrower and would have cost nothing: *six keys on lines 85–88 were listed as absent when they are present; the mechanism that produced that specific six has not been established.*

This finding is **not** overtaken by the deletion. Both statements are in the current text.

---

## MEDIUM

**Q4. The Tier 1 bounding sentence names a mechanism that cannot operate for this cohort, and omits the one that does. R5's fix does not hold.**

Current §5 line 204: *"a volume with no `COVERAGE` entry is *unclassifiable by date*, which is not the same set as what renders under Tier 4 — `corpus_tier()` returns `"1 - named, never opened"` before it ever reaches the `COVERAGE` lookup for any volume a world names."* §7's R5 bullet: *"Tier 1 pre-empts the lookup. Distinguished at §5."*

The code path is described correctly in the abstract — line 202 does return Tier 1 before line 204's `COVERAGE.get`. But `named` is not "any volume a world names." In `gen_corpus_table.py` it comes from `observe_second_hand_sources()`, which iterates `_AUTHORS_BY_FILE`, which is built only from files whose `corpus_key` is in the `AUTHORS` table. **None of the fourteen unclassified keys is in `AUTHORS`** — I checked all fourteen; `AUTHORS`' 41 keys are a strict subset of `COVERAGE`'s 44. So Tier 1 can never pre-empt any member of this cohort, in any world, ever. The qualifier bounds nothing.

The mechanism that actually operates is a different one, and Round 3's R5 named it in the sentence the repair did not adopt: `gen_corpus_table.py` skips any file the world already sources (`counts.get(filename, {}).get(w)`). Confirmed empirically against the current report: `alx` and `syr` each render **17** of the cohort's 18 files under Tier 4 — all of them except `nestle1904`; `desert` renders 13, omitting exactly the four it sources (`anan-isho`, `evagrius`, `macarius`, `pachomius`); and `nestle1904` is missing from every world not because it is sourced anywhere (it is sourced nowhere) but because the report predates it. So the cohort is *more* uniformly rendered under Tier 4 than the document's hedge implies, for reasons the document does not give.

One review disagreement to log, per `cic-build-cycle`: Round 3's R5 offered `nestle1904` as its example of a sourced volume dropping off the worklist. That is wrong on the same file — `nestle1904` has no source record in any world; it is absent because CORPUS-USE.md was generated when 64 files were on disk. Round 3's underlying mechanism is right; its illustration is not.

**Q5. "Got them wrong three times" across "three revisions" misdescribes the history: the third revision's figures were correct, and the enumeration was deleted at the moment it had become right.**

Current §5 line 200: *"This item carried a scale figure and a world count through three revisions, and **got them wrong three times**."* The three wrong statements it then lists — "roughly a dozen … all seven worlds", the recomputed key count, the keys-versus-files reconciliation — come from **two** revisions, not three: the reconciliation and the key count were both in the post-Round-2 text. The post-Round-3 text, the one deleted, was **right on every figure I could test**, as recorded above.

The sentence therefore reads as though the count was still failing at the moment it was removed. It was not. That matters for two reasons: it misstates the document's own error history in the paragraph whose stated purpose is to disclose that history accurately, and it supplies a stronger warrant for the deletion than the facts support. (Note that the paired claim "twice the error ran in the direction of overstating the defect" *is* now accurate, because the current text says "a scale figure **and a world count**" — "seven" overstated the world count and "22" overstated the key count. The superseded text's "this one ancillary figure … twice in the direction of overstatement" was not accurate, since "roughly a dozen" understated an 18-file cohort. The rewrite fixed that half.)

**Q6. §7 and item 16 pre-declare the disposition of a review that had not been filed, and the pre-declaration is wrong.**

§7 line 275: *"Its findings on that now-deleted enumeration are **overtaken** by the decision above and should be read as history; its findings on everything else stand and are to be applied normally."* Item 16: *"its findings on the now-deleted enumeration are overtaken and its findings on everything else still apply."*

Disclosing the sequencing is right and I credit it. Sorting the unread review's findings into "overtaken" and "still apply" is not. It is a build thread deciding in advance which parts of an independent review it will act on, in the same document that says four lines earlier *"This thread does not self-score."*

It is also factually wrong here. Two of my three findings on that item — Q3 (the false regex diagnosis) and Q4 (the inoperative Tier 1 bound) — are about text that **survived the deletion verbatim** and is in the current §5 and §7. A third, Q5, is about the replacement text itself. Nothing about the enumeration's removal overtakes any of them.

**Q7. §7's Round 3 entry misrepresents what was changed on the LOW findings, and mislabels one — word for word the defect Round 2's F13 and Round 3's R19 raised.**

The Round 3 entry's last bullet reads, in full: *"**R12 (LOW) and nine further LOWs.** The unmarked "Constantine"→"Constantius" emendation in the Candidate 5 row is now marked as Walford's slip rather than silently corrected."*

- **Mislabelled.** The Constantine/Constantius emendation is Round 3's **R13**, not R12. R12 is the near-verbatim-"paraphrase" finding, which is untouched (Q15).
- **Seven of the ten are untouched**, while the bullet's shape — a heading naming all ten, sitting in a list of fixes — reads as a disposition of all ten. Unaddressed: R12, R14, R15, R16, R17, R20, R21. Addressed: R13 only, plus R18 in part and R19 not at all.

Round 2's F13 said this about Round 1's four LOWs: it *"leaves a reader unable to tell declined from missed."* Round 3's R19 said it again about Round 2's six. The document fixed it for Round 1's four and has now reproduced it for Round 3's ten. Declining a LOW is a perfectly good answer; not saying which were declined is not.

**Q8. The Dekkers dating is now credited to a third channel, which this environment cannot reach and which §3.1 does not mark as unreached — and §3.1's own promise to mark such cases is not honoured for it or for Brepols.**

§3.1 now says the Dekkers dating came *"not"* from Wikipedia (*"wrong, caught at Round 2"*) and *"then to the Brepols listing (also wrong, caught at Round 3 — Brepols does not appear to carry it); the channel that does carry the van Banning/Dekkers dispute is Papahagi's *Mediaeval Studies* article named next."*

What I could establish:

- **Wikipedia does not carry it.** ✔ I fetched the *Opus Imperfectum* article: it gives Erasmus 1530, the Timothy/Maximinus/Anianus candidates, and *"sometime in the 5th century"*. No Dekkers, no sixth century, no Schlatter, no Cooper. Round 2 and Round 3 were both right.
- **brepols.net and pims.ca are both egress-blocked from this environment.** I could not retrieve either. The Papahagi attribution is therefore neither confirmed nor refuted here.
- The exact dispute sentence — *"Dekkers (CPL 707) captures a dominant trend in the scholarship in advocating a date of composition in the mid-sixth century; however, Joop van Banning, the senior editor of a new edition in progress, believes the Opus was composed in the second or third quarter of the fifth century"* — is retrievable through the search index, and the listing it is most strongly associated with is **not** Papahagi's article but Brent Landau's *Revelation of the Magi* chapter (the *Revelation* survives in summary inside the *Opus imperfectum*, so its dating is discussed there). That is a search-index association, not a retrieved page, and I state it as such. It does not prove Papahagi lacks the sentence. It does mean there is at least one demonstrable channel for the claim and it is not the one now named.

The finding is the pattern, not the fact: **one dating has now been attributed to three different channels in three consecutive rounds**, the first two demonstrably wrong, the third unreachable — and §3.1 states it flatly. §3.1 opens by promising that *"where a host was unreachable, the fact rests on search listings rather than on a retrieved copy, **and is marked as such**."* That promise is honoured in §3.2 (for PG 56 on archive.org) and honoured nowhere in §3.1 — neither brepols.net nor pims.ca is marked as unreached, and both are.

**Q9. Item 16 still names one review artifact path while reporting three verdicts; §6 names none for Round 3. R21 does not hold.**

`cic-build-cycle`'s Disposition section requires the log to record *"where each review artifact file lives."* Item 16 links only `Review-Artifacts/PostAdmission_Source_Finding_Round1_Review.md` and then reports Round 2's and Round 3's outcomes with no paths. Round 3 filed this at LOW when it was one missing path; it is now two. §7 does name all three files, so the paths exist and the omission is purely in the log entry the skill actually specifies.

---

## LOW

**Q10.** *(R15, third consecutive round.)* §5 item 4 still asserts *"Philostorgius's *History* covers 300–425; this world's window is 312–451"* with no locator, at the one place the figure does load-bearing work. Both halves are real and in the repository: the vendored file's own Pearse/Quasten note at **line 50** reads *"a Church History in twelve books covering the period 300-425"* ✔, and `records/worlds.yaml` **line 152** carries `time_window: {start: 312, end: 451}` ✔. Round 1 cited the note; three revisions have not.

**Q11.** *(R16.)* Candidate 6's row in the §2.3 table is still *"No demonstrated relationship."* — the only row with a bare negative. The adjacent passage Round 3 identified is real: Book **II.13** (file line 136) has the martyr Lucian *"debarred from the church and the altar by the hand of tyranny"* offering the eucharist on his own breast. It does not move the classification (312, Nicomedia, outside all three strands, third-hand through a hostile epitomizer, and Doc_04 grounds Candidate 6 in this world's Native record), but that is the argument the row should make.

**Q12.** *(R17.)* "Confidence A" shorthand retained in §7's H2 bullet and in item 16, collapsing `citation_specificity: A`, the Registry's A–E Confidence tiers and Doc_04's five-level formation vocabulary. §2.3's body quotes the actual field names and is fine — I verified `citation_specificity: A`, `verification_state: verified-direct` and `formation_confidence: Documented` at lines 10, 11 and 13 of the Hilary record.

**Q13.** *(R14.)* §2.3 still quotes `cic/texts/README.md` line 168 as *"srcIJC24 excludes the Athanasius corpus… Hilary is an independent Latin transmitter of the same texts, so the exclusion does not apply."* The line continues *"and no owner decision is needed to use them."* Nothing is distorted — the omitted clause strengthens the point — but the quotation is presented as complete.

**Q14.** *(R20.)* The un-indented block that breaks out of §5's numbered list has grown from one paragraph to **four** (current lines 198, 200, 202, 204), all at column 0 while items 4's other sub-paragraphs sit at four spaces. As rendered, the entire qualitative scope statement falls outside the numbered item it belongs to, and item 5's numbering is disturbed.

**Q15.** *(R12.)* §0 line 13 is unchanged: *"this world's build was phase-1 complete and merged, with the M3 live admission step blocked awaiting a go-ahead."* Round 1's M10 quoted the brief as "phase 1 complete and merged" and "the M3 live admission step blocked awaiting a go-ahead." The substantive concern is discharged (nothing is presented as the brief's own words, and I confirmed no brief quotation survives anywhere in the repository), but "paraphrased" still overstates what was done to the wording, and R12 is not acknowledged.

**Q16.** §1(1)'s repo-root figure has gone stale by one: `untranslated` now appears in **39** files case-sensitively and **40** case-insensitively, not 38/39. The cause is benign and structural — the metric counts this document's own review artifacts, so it increments by one every round; Round 3 measured 38/39 before its own file existed. The **load-bearing** claim is the scoped one and it is exactly right: `grep -rIil untranslated worlds/ijc/ records/ijc/` returns exactly four files, all of them this finding and its three review artifacts ✔. Recorded because the document presents the repo-root figure as a checked number.

**Q17.** §7 line 269's clean-list sentence — *"no unsupported project-lead attribution … across all three rounds"* — is true of the first three rounds and sits four lines above the attribution at Q2. Presentational, but it is the sentence a reader will use to conclude the opposite.

---

## What checked out clean

Verified from primary sources this round, not accepted from any prior review's account.

- **The whole §5 item 4 enumeration, before it was deleted** — all six figures and the fourteen-key list, recomputed independently. Recorded above in full because it bears directly on Half B.
- **CORPUS-USE.md's staleness, pinned exactly.** Header says 64 vendored files against 65 on disk ✔; the single absent file is `nestle1904_greek-new-testament-grc.txt` ✔; `grep -ci cappadocian` returns 0 ✔; cappadocian is `state: admitted` and genuinely missing from the report ✔; `records/cappadocian/source/cappadocian.source.photius-epitome-philostorgius.md` exists ✔.
- **The Doc_08 locators, in both files.** "**Status:** CONFIRMED. Doc_04's own Candidate 3 Confidence/Gravity Cross-Check divergence (Section 7) is carried at full strength, not resolved" is verbatim at Doc_08 line 279, under **Section 8 — Governing Principles Applied**, *Named-Tension Principle* ✔. The Doc_09 routing is **item 2** of Doc_08's "Open Items and Process Findings" ✔. **Section 9 is "Doc_08 Completion Certification"** ✔, so the parenthetical explaining the old §9 citation is right. **Section 6 — Transmission as a Force Dimension** carries the *"Homoian Christianity's own self-testimony survives in exactly one substantial instance"* sentence at its "What Selection Effects Shaped What Survives" subsection ✔, and R11's addition is accurate. `Doc_05_Ecological_Reconstruction.md` §5 is "Boundary Structures — policed doctrinally and juridically at once" ✔.
- **The F2 repair, re-verified independently for a second time.** `Source_Registry.md` **row 24** marks the Athanasius corpus **Excluded**, Named Comparandum, *"do not use beyond the single Julius I quotation already licensed at row 4"* ✔; **row 4** carries *"do not extend Native status to the surrounding Athanasian material"* ✔; `cic/texts/README.md` **line 168** carries *"srcIJC24 excludes the Athanasius corpus beyond the single Julius quotation. Hilary is an independent Latin transmitter of the same texts, so the exclusion does not apply"* ✔; the Hilary record's `citation_specificity: A`, `verification_state: verified-direct`, `formation_confidence: Documented` and the *"'like the Father' formula discussed from line 8067 and repeatedly after"* body note are all verbatim ✔.
- **Every Philostorgius quotation and chapter attribution I tested.** IV.10's *"confirmed that belief with the signatures of the bishops present"* (file line 226, Book IV ch. 10) ✔; IV.11's *"having subscribed their names to the doctrine of unlikeness, sent their letters about in every direction"* (line 230) ✔; IV.12's *"one thing hidden in his bosom and another ready upon his tongue"*, *"not even enduring to learn in what sense Aetius used that term"*, *"That the Son is like to the Father according to the Scriptures"*, *"by the artifice of this same Acacius"* and *"under the name of economy"* (line 230) ✔; V.1's *"playing the part of mere time-servers, and reverencing the will of the emperor as paramount to the truth"* (line 234, Book V ch. 1) ✔; Photius *Bibl.* cod. 40's *"severely attacks Acacius … for his extreme severity and invincible craftiness"* (line 50) ✔; the Quasten note's *"a late apology for the extreme Arianism of Eunomius"* (line 50) ✔; IV.3's Liberius recall (line 212) ✔. File is **1,007 lines** with **241** numbered footnotes and all twelve books ✔, supplied by **Mark, 2026-08-31**, per `cic/texts/REGISTRY.yaml` line 760 ff. ✔.
- **§2.2(b), completely.** *"The Anomoeans/Eunomians are not strictly Homoians"* is verbatim on the Chrysostom *Homily on the Paralytic* row of `anomoean-eunomian-christianity.yaml` (line 14) ✔; its next clause is *"Needs Mark's ruling on whether that entry covers anti-Anomoean material or the second id should be dropped"* ✔; the dated addendum *"Re-pointed 2026-08-26 … rather than the Homoian wing it split from in 360"* is on the same row ✔; the "canon 1 names Eunomians and Arians as separate parties" rationale is on the **Constantinople 381** row (line 33), a different row ✔. The document's weakened restatement is correct against the file.
- **§2.4.** Philostorgius rows exist only in `anomoean-eunomian-christianity.yaml` (`role: tradition`) and `cappadocian-nicene-pastoral-monastic-tradition.yaml` (`role: context`) ✔; no `imperial-juridical-christianity` row ✔; `grep -rIiE 'philostorg|eunomi|anomoean' records/ijc/` returns **zero** ✔. The *Historia Arianorum* ijc row carries **`role: tradition`** ✔ and the "Assigned three ways … the ijc world's own problem stated by its sharpest opponent" note is verbatim ✔.
- **Both Doc_02 §7 quotations, character-for-character** (lines 117 and 111) ✔, including the *homoousios*/*heteroousios*/*homoios* boundary the argument turns on.
- **All three Auxentius disclosure layers.** The search record's `query` scoped to one text and `result: not_found` ✔; the source record's `rights_status: "referenced-only; no vendorable public-domain English edition (fails closed for quotation)"` ✔; the participant-facing `thinness_statement` ending *"and the defeated Homoian side's own voice"* ✔. **24** search records ✔.
- **§0's admission facts and §4's CI constraint.** `state: admitted`, `time_window: {start: 312, end: 451}`, pinned at `packages/ijc/2026-09-04T18-49-02Z` with a `manifest_hash` ✔; `WORLDS_REGISTRY_LOG.md` "yes i admit all six worlds", 28/28 sealed probes, the named report file ✔; `render.yaml` line 89 `CIC_ENFORCE_ADMISSION` ✔; BUILD-LOG's header *"Compile (6), admission (7), open (8): intentionally NOT started"* ✔ and §1's "154 records" ✔ against `find records/ijc -type f` = **182**, all `.md` ✔; `.github/workflows/ci.yml` line 236 `m2-staleness-check` with the quoted comment ✔.
- **The Round 1 and Round 2 tallies in item 16.** Round 1: four HIGH (H1–H4), eight MEDIUM (M5–M12), four LOW (L13–L16) ✔. Round 2: two HIGH (F2, F5), eight MEDIUM (F1, F3, F6–F11), six LOW (F12–F17) ✔ — counted from the review files' own severity headings.
- **Standing checks.** No fabricated quotation anywhere: every quotation I sampled — from the vendored Philostorgius file, Doc_02, Doc_04, Doc_05, Doc_08, `Source_Registry.md`, `cic/texts/README.md`, `ci.yml`, CORPUS-USE.md, `worlds.yaml`, the corpus maps and the records — is verbatim at the location given. No wrong chapter attribution. No uncredited cross-world reuse: the cappadocian record is named and credited throughout. No claimed verification that I could show was not performed, with the single exception of Q3's causal claim. The document does not self-score and claims no disposition. Its two other Mark attributions (`CORPUS-USE.md` line 140, `WORLDS_REGISTRY_LOG.md`) are both cited to checkable records and both verbatim — which is what makes Q2 the outlier rather than the pattern.

---

## The headline verdict, attacked a fourth time from scratch

I read `Doc_04_Gravity_Discovery.md` and the vendored file without reference to any prior round's argument, and asked what would have to be true for something to move.

- **The six candidates.** Candidate 3's Confidence/Gravity Cross-Check reads, verbatim, *"full confidence in reconstructing **what, precisely,** was being enforced **or resisted** at any given moment inside the Homoian-establishment decades is lower than the mechanism's own attestation"*, with the preceding clause grounding that in *"directly-surviving Homoian self-testimony (Confidence C, Registry row 23)"* ✔. The divergence is about *Homoian self-testimony*. Philostorgius is not Homoian — Doc_02 §7 defines Homoian identity partly by its rejection of the Anomoian *heteroousios*, the corpus map separates the parties on a dated record, and the file's own Quasten note calls the work an apology for Eunomius's extreme Arianism. The formula he transmits is already held at `citation_specificity: A`, `verification_state: verified-direct`, `formation_confidence: Documented` through Hilary. He adds a second opponent-transmitter of an already-Documented formula. The divergence does not narrow. Candidate 2's Forces-connection notation (*"which theological content it favors shifts with the reigning emperor"* ✔ verbatim) is corroborated from outside by IV.10–V.1 and stays Primary. Candidate 5's narrow Formation pass (*"shapes which theological vocabulary this world's own actors could safely use"* ✔) is strengthened by IV.12 and stays Supporting. Candidates 1, 4 and 6 are untouched.
- **The Interaction Matrix.** A cell records a demonstrated relationship between two candidates. Corroborating an existing cell does not create one. No cell changes.
- **Article 21.** Candidate 3 is *"Confirmed cross-strand to Strands A and B only"* ✔; Philostorgius touches neither strand boundary. Doc_04 Open Item 2 (Candidate 6 in Strand B) is not closed by anything in the file.
- **Doc_08.** Section 6's "exactly one substantial instance" claim is about Homoian self-testimony and is untouched; a losing-side history surviving inside a hostile epitome corroborates that section's mechanism rather than complicating it. Section 8's Named-Tension status is unchanged.
- **Finding #2.** The rights test is decisive and correctly applied: PG 56:611–946 public domain, Kellerman/Oden (IVP 2010) the only complete English translation and in copyright, same posture as Auxentius. The *Catena Aurea* rejection is the strongest single paragraph in the document and I would not change a word of it.

**Neither acquisition is structural for Doc_04. Nothing in `Doc_04_Gravity_Discovery.md`, its Interaction Matrix, its Article 21 findings, or `Doc_08_Forces_Document.md` should move. I could not overturn it, and this is the fourth round that could not.**

---

## HALF B — a recommendation to the project lead

**The question put to me:** the document's own §7 proposed that a fourth error in §5 item 4's enumeration should be answered by deleting the enumeration and stating the defect qualitatively. That has now happened. My view is asked on whether it was right, on whether the precision was load-bearing, on whether a fifth round would add value, and — if the document is now correct — to say so without hedging.

**1. Was the precision load-bearing? No. The document is right about that, and it is the strongest part of its case.**

I tested it directly rather than accepting it. Take every number out of §5 item 4 and ask what changes in the finding's conclusions. Nothing does. The headline verdict rests on Doc_02 §7's Homoian/Anomoian boundary, Registry row 23, and the Hilary holding — none of which touches the cohort size. §2.4's corpus-map escalation rests on the *Historia Arianorum* precedent. §4's no-record constraint rests on the CI pin. §6's escalation count rests on the defect being cross-world, which requires only "more than one world", not "six". The one thing item 4 has to establish is the *causal* claim — that a volume mislabelled as out-of-window is a volume no builder has reason to open, which is how Philostorgius went unconsidered here — and that argument runs on CORPUS-USE.md lines 140 and 142 and needs no count at all. Whether the cohort is 14 keys or 40 changes nothing a reader would act on differently, except the priority of an engine ticket that is not this thread's to write.

**2. Was the repeated failure evidence that the enumeration should go, or that it should stay and be right? Neither, quite — and the timing makes this the wrong answer to the right question.**

The honest sequence is this. Three rounds failed on hand-maintained counts. The post-Round-3 revision replaced hand-counting with a script. **And it worked.** I recomputed all six figures and the fourteen-member list from the source files and every one was correct. The method had been fixed and the output was right on the first attempt after fixing it. The enumeration was then deleted — one revision after it stopped being wrong, and on a rule ("if a fourth round finds a fourth error") whose antecedent this round does not satisfy, because I found no fourth error *in the enumeration*.

Worse, the deletion removed the half of item 4 that was verifiable and kept the half that is still wrong. The two live defects in that item today — the false regex diagnosis (Q3) and the inoperative Tier 1 bound (Q4) — are both *prose*, both survived the cut verbatim, and both are exactly the kind of confident causal assertion that has been this document's recurring weakness. A rule that deletes the numbers because the numbers kept failing, while preserving the unchecked explanations of why they failed, has the diagnosis backwards. The failure was never arithmetic as such; it was **asserting a mechanism that had not been verified** — which is Round 1's H1, Round 2's F2 and F5, and Round 3's R4 and R7, all of them, and Q3 today.

So my recommendation is not "put the numbers back." It is:

- **Keep the qualitative scope statement.** The precision genuinely is not load-bearing, and a document that has to be re-reviewed every time a corpus file is added is carrying a maintenance liability for no analytical return. The current phrasing — a number of volumes, more than one world, recompute from the module — is the right shape.
- **But delete the two surviving causal claims, not the numbers.** Strike the regex diagnosis wherever it appears (§5, §7's R1 bullet, and it should not have gone into the commit message either) and replace it with what is actually known: six keys were listed as absent that are present; the mechanism has not been established. Strike or correct the Tier 1 sentence: for this cohort Tier 1 cannot apply, and if a bound is wanted, the true one is that a world already sourcing a volume drops it from the worklist.
- **Put the recomputation where it will be re-derived, not transcribed.** The scope figure is genuinely useful to whoever fixes `engine/m1/cross_world.py`. It belongs in that engine ticket as a two-line script, not in a prose document that cannot recompute itself. That gives the lead both things: a finding that states the defect qualitatively and never goes stale, and an actionable number that is always current.

**3. Is the document now correct? No — not yet, and I will not hedge that either.**

On the substantive question it was commissioned to answer, it is right, and that is now established four independent times from the primary documents. But "the document" is not just its conclusion. As it stands at `b663348f`:

- §6 contradicts the rest of the document in two places, one of them a full review round out of date, in the section that gates self-disposition (Q1);
- a verbatim project-lead quotation with no verifiable record now authorises a content deletion, in breach of the one rule `cic-build-cycle` holds to the same bar as Frozen (Q2);
- the stated cause of the error that drove three rounds is false and demonstrably so (Q3);
- the sentence that bounds the defect's scope names a mechanism that cannot operate (Q4).

Q1 and Q3 are the same class the last three rounds found. Q1 and Q2 were *introduced by the edit that was supposed to end the pattern*. That is the single most important sentence in this review.

**4. Would a fifth round add value? Yes — one, and narrow. Not an open-ended round.**

I want to separate two things the "three rounds is a lot" framing runs together.

Reviewing the **argument** hit diminishing returns after Round 1. Four rounds have now re-derived the same verdict from the same primary documents and none could move it. Doc_04's classification, the Interaction Matrix, Article 21 and Doc_08's forces have been independently re-tested four times. Another round spent re-litigating that would be pure waste, and I would say so plainly to anyone proposing it.

Reviewing the **housekeeping** has not hit diminishing returns, because every round including this one has found real defects there, and this round found two that a reader acting on §6 alone would be misled by. But the remedy is not a fifth adversarial round of the same kind. It is three specific, checkable things:

1. Fix §6 — both stale claims — and add the Round 2/Round 3 review paths to item 16 and to §6.
2. Produce a verifiable record for the project-lead instruction, or restate the deletion in the document's own voice as a build-thread decision (which it is entitled to make; the enumeration is not a claim, a confidence rating, a sourcing conclusion or a scope boundary). Either is fine. Quoting an unverifiable instruction is not.
3. Strike the regex diagnosis and correct the Tier 1 sentence.

A **Round 5 scoped to exactly those three items plus a mechanical propagation diff** — every changed string grepped across both files, and every sentence of the form "this document says X elsewhere" checked against where it says it — is worth running and should take a fraction of the effort of this round. If it comes back clean, dispose. If the lead would rather not spend another round: items 1 and 3 are objectively checkable in ten minutes by anyone, and item 2 is the lead's own to answer, so a lead-side confirmation plus a coach-thread propagation pass would be a defensible substitute. What is not defensible is disposing of the document with §6 as it stands.

**5. One process observation, offered because the skill asks for tensions to be named rather than absorbed.**

The document was edited while an independent review of it was running, and the edit pre-sorted that review's unread findings into "overtaken" and "still applies". Both halves of that are worth a rule. A document under review should not move; if it must, the review should be told and restarted, not have its conclusions anticipated. And the shape of what happened here — a document proposes a course of action in its own §7; an unverifiable project-lead instruction arrives quoting that proposal almost verbatim; the document then records the instruction as resolution and pre-dismisses the review that was examining the thing removed — is precisely the shape the attribution rule exists to make impossible to construct by accident. I want to be clear that I am not alleging the instruction is invented. I am saying that on the record as it stands there is no way for a later reader to tell, and that the rule's whole point is that "no way to tell" is the failure, not the fabrication.

---

## Overall verdict

**SUBSTANTIAL REVISION REQUIRED.**

Not on the answer. The answer is right, was right at Round 1, and has now survived four independent attempts to break it; §2.2, §2.4, §3.2's *Catena Aurea* rejection and §1's disclosure-limits correction remain careful, self-disadvantaging work, and the F2 repair is a model of how to withdraw an error.

The revision is required because the edit that was meant to close this pattern reopened it. §6 now carries two claims the rest of the document contradicts, one of them a full round stale, in the section that gates self-disposition — the fourth consecutive round of propagation failure, and the second failure of that same paragraph. A verbatim project-lead quotation with no verifiable record now authorises a content deletion, in breach of the one rule this skill holds to the same bar as Frozen. And the deletion removed an enumeration that I verified to be entirely correct while keeping, verbatim, the two claims in that item that are false: the regex diagnosis and the Tier 1 bound.

Nothing found here is a fabricated quotation, a wrong chapter attribution, an uncredited cross-world borrowing, a self-scored result or a pre-declared disposition of the document itself. The document remains DRAFT and claims nothing.
