# Doc_08 — Forces Document, and `lpc_Force_Index.md`: Latin Pastoral-Congregational Christianity
## Round 3 Independent Adversarial Review — verification of the Round 2 fix pass, plus a cold read of everything it wrote

**Deliverables under review:** `Doc_08_Forces_Document.md` (446 lines) and `lpc_Force_Index.md` (143 lines), as committed at `561c2c35` ("lpc: apply Doc_08 Round 2 — all 11 findings, incl. 3 HIGH the Round 1 fix introduced"). Working tree is clean against that commit; what I reviewed is what is on disk.

**Prior rounds:** `Doc08_Round1_Review.md` — SUBSTANTIAL REVISION REQUIRED (4H 5M 3L 1C). `Doc08_Round2_Review.md` — SUBSTANTIAL REVISION REQUIRED (3H 4M 3L 1C), of which all three HIGH findings were defects the Round 1 fix pass had itself introduced.

**Standing instruction I was given and took seriously:** assume the Round 2 fix pass did the same until checked. It did.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**4 HIGH · 5 MEDIUM · 4 LOW · 2 COSMETIC — 15 in total.**

Ten of Round 2's eleven findings are genuinely closed at the live text, several of them exactly and well: H1's misattribution is corrected at all four sites and the standing method is correctly widened; the four Cyprianic quotations re-verify by containing-work heading as well as by note-span; the Index's derived tables re-derive to zero mismatches against an independent parse; L1, L2 and C1 are closed precisely.

But the pattern that produced Round 2's three HIGH findings has produced four more. The sentence written to close Round 2's H2 asserts, as a fact about §5, something §5 contradicts three sections below — and the new §6 control built to catch exactly that class of defect is blind to it by design. The construction-record block invented to close Round 2's M3 did not remove construction-record voice from Layer 2; a mechanical scan finds it in all three rewritten entries and in none of the other fourteen, including a `Source_Registry.md` row number and the phrase "rendering this build's own" inside the world's-voice layer. The new §7 cross-check prints, in the delivered Index, a disagreement that does not exist — it reports as absent from Doc_08 §7 the very force the last pass added to §7. And both deliverables' review-history statements are one round stale and now false, at the exact line that carries a correction notice about that same defect having occurred one round earlier.

None of these requires new source research. All are correctable inside this build thread's editing authority.

---

## Method — what I actually opened and ran

**Documents read in full:** both deliverables; `Doc08_Round1_Review.md` and `Doc08_Round2_Review.md`; `L4-Templates/[world-code]_Forces_Document.md` (Section 3 preamble, the 1A/2B/3B layer slots); the Forces Framework plain text (`FF.txt` §§1, 2, 3, 5, 6); Constitution Articles 17, 19, 22, 23 (text at `const.txt`); `cic/texts/INTAKE.md`; Doc_02 §1 and §2 on the *Retractationes* and on intra-corpus attribution; Doc_04 §§2, 4, 5, 6 on Candidate 2's Persistence result; `Lexicon_Deployment_Index.md` §6; `lpc_Decision_Log.md`'s 2026-09-15 Doc_08 Round 2 entry; `Source_Registry.md` rows 67, 78, 209.

**Sibling Doc_08 files opened:** Donatism, Imperial-Juridical-Christianity, Syriac-Christianity-Edessa-Nisibis, Alexandria-Catechetical-School, Desert-Monasticism, Hieronymian-Ascetic-Literary, Cappadocian, 01-Post-Apostolic-House-Church — eight in all, grepped for any interposed Layer-2 block and read where a hit or a near-hit appeared.

**Scripts run:**
- The saved generator `gen_force_index.py`, unmodified except for its output path, against the live Doc_08. **Output is byte-identical to the committed `lpc_Force_Index.md`.** The Index is what the script produces; every Index finding below is a finding about the delivered file, not about a stale copy.
- The same generator against `9eccc532:Doc_08_Forces_Document.md` (the pre-fix draft), reproducing the fix pass's own claimed regression result, then instrumented to show *which* defects it caught and which it did not.
- An **independent re-derivation** of the Index's §1 master table (gravity and confidence columns), §2 counts, §3 by-gravity table and §4 row count, written from Doc_08's own §3/§4/§5 without reference to the generator. **Zero mismatches across all 17 rows, all 8 gravity rows, and the 27 force–gravity pairs.** 17 forces; 14 Documented / 3 Widely Accepted; 15 connections; no empty gravity row.
- A **four-case mutation test** of the two new controls (results in the check-confirmation section).
- A **quotation verification pass** over `cyprian.xml` and `npnf104` that marks `<note>` spans *and* preserves `<div1>`–`<div4>` `title=` attributes as sentinels through the tag strip, so that every quotation returns both an `INSIDE-NOTE` verdict and the heading of the work that contains it.
- A **discriminating Layer-2 register scan** across all seventeen Layer 2 blocks.
- Direct byte-level inspection of `cic/texts/augustine_retractationes-lat_knoll-csel36.txt`, Prologus, lines 1507–1520.

---

## Job 1 — Round 2's eleven findings, closure status at the live text

| # | Finding | Status |
|---|---|---|
| **H1** | 2B-5 attributes to Cyprian a directive written by the Roman clergy | **CLOSED, and well.** Doc_08 line 209 now attributes the sentence to Epistle II, "written **by the Roman clergy to the Carthaginian clergy**," notes it is the letter Cyprian later returned for collation, and records it as the network's practice under Doc_01 §5's boundary. Corrected at all four named sites: Doc_08 2B-5, Doc_08 §8 line 393, Index §5 line 109, `lpc_Decision_Log.md` line 1187. The standing method at 2B-5 Layer 3 item 2 is widened to require recovering the containing work's heading alongside the note spans, and says in terms that "editorial interleaving and intra-corpus attribution are two different failure modes and only one of them was being checked." I re-verified all four surviving Cyprianic quotations plus the five others in the matrix by heading recovery — all clean (see below). |
| **H2** | §3/§5 gravity contradiction not reconciled; new architecture makes it undetectable | **CLOSED IN PART, AND A NEW CONTRADICTION INTRODUCED.** 1B-1/G2 and 2A-1/G8 are genuinely reconciled by additions to §5, and both additions are sound (see the note under NEW-H1). 2B-1/G7 is reconciled by narrowing §3 — but the narrowing asserts something false about §5's G6 list. A reconciliation control was added at Index §6, and it cannot see the new contradiction. **See NEW-H1.** |
| **H3** | Layer-2 control certifies the draft it was built to prevent; hard-coded prose presented as derived | **CLOSED IN PART.** The stub test is real: run against `9eccc532` it now flags three entries and prints "3 force(s) MISSING a Layer 2." The Index states honestly that it "still measures presence, not quality." But the accompanying disclosure of which lines are hard-coded is under-inclusive, and it omits the lines that have actually gone stale. **See NEW-M3 and NEW-H3.** |
| **M1** | §7 is a second hand-maintained derivation nothing checks | **CLOSED IN FORM, DEFECTIVE IN FACT.** A §7 cross-check now exists at Index §7 — and prints a disagreement that does not exist. **See NEW-H4.** |
| **M2** | 3B-2 declares an interior experience "attested" on behavioural evidence | **CLOSED.** Line 262 now opens "What is attested is the mode, not the feeling of it," the "what it feels like from inside" sentence is gone, and Reported-Experience Status is applied at line 268. (The marker's referent is loosely expressed — NEW-L4 — and §9's tick was not updated to match — NEW-M4.) |
| **M3** | Build-thread maintenance prose inside Layer 2 | **NOT CLOSED.** The one sentence Round 2 quoted is gone. Construction-record voice is live in all three rewritten Layer 2 entries, and in none of the other fourteen. **See NEW-H2.** |
| **M4** | *Retractationes* uncited, unquoted, Latin-only witness undisclosed | **CLOSED IN SUBSTANCE, with a false claim inside the disclosure.** Row 209 is cited, the second-witness status is named, `INTAKE.md`'s second limb is correctly identified and does exist ("or when no English translation exists at all yet"), the Latin is quoted at its Prologus locus and the English is marked as this build's own. The rendering is accurate. But the disclosure's assertion that "the Latin is quoted with the source file's own OCR retained" is false. **See NEW-M2.** |
| **L1** | "three" truncated connection descriptions should be "four" | **CLOSED.** Measured directly in `9eccc532:lpc_Force_Index.md`: exactly four connection cells at 150 characters, all cut mid-word, and exactly two Force names at 88. The Index now says "two Force names and four connection descriptions." Correct. |
| **L2** | Doc_04's Candidate 5 heading quoted with `[Supporting]` dropped | **CLOSED.** Doc_08 line 27 now quotes `"Candidate 5 [Supporting] — Conciliar Authority Theory (Egalitarian vs. Hierarchical)"`. Verified character-for-character against `Doc_04_Gravity_Discovery.md` line 84. |
| **L3** | §8 asserts the governing set is unanimous when the L4 template carries a carve-out | **CLOSED IN PART.** Doc_08 line 391 now flags the template's Proportionality carve-out, quotes it exactly against template lines 104–106, and explains why it does not reach the transmission entries. The reasoning is right. But the new sentence describes the governing set as having "one scoped exception in it," and it has more than one. **See NEW-L3.** |
| **C1** | "Reported-Experience Status" asserted at three sites, named at none | **CLOSED.** Line 252 names it: "***Reported-Experience Status* (Constitution Article 17; Forces Framework §3)**," with the Framework's own formula following. |

**Ten closed, one closed-in-part-and-regressed (H2), and three closures (H3, M1, M4) that carry a new defect inside the fix.**

---

## HIGH

### NEW-H1 — The sentence written to close Round 2's H2 asserts a fact about §5 that §5 contradicts; the Index prints the contradiction; and the control built to catch this class of defect cannot see it

**Site:** `Doc_08_Forces_Document.md` line 161 (Force 2B-1, Layer 3) against line 326 (§5, G6). `lpc_Force_Index.md` line 31 (the `2B-1` master row) and §3's G6 row. `gen_force_index.py` lines 118–150 (the `CONNECT`/`DISCLAIM` pass) and Index §6.

**What I found.** Round 2's H2 required the 2B-1/G7 divergence to be reconciled. The fix pass reconciled it by narrowing §3. Line 161 now reads:

> **This force therefore connects to G2, and to G2 only.** Its phase-two afterlife is a *family resemblance* to G6 and G7 in Doc_04's own sense — those gravities were tested and classified separately — **not a force-connection this document asserts**, **which is why §5's G6 and G7 lists do not carry it** and why G7's single-force origin there stands.

§5's G6 list, line 326, unchanged from the original draft and untouched by either fix pass:

> **G6 — Sacramental and Ordination Validity (Primary).** Connected forces: **2A-3** …, **2B-4** …, **2B-1** *(its phase-two inheritance of the failed-member question)*.

§5's G6 list does carry it. The Index's master row for `2B-1` reads **G2, G6**, and its by-gravity G6 row reads `2A-3`, `2B-1`, `2B-4` — both correctly derived from §5. So the delivered pair contradicts itself on its face: Doc_08 §3 says the force connects to G2 and to G2 only and states why §5's G6 list omits it; §5 lists it; the Index prints it.

I confirmed this three ways: a literal grep for the §5 G6 line; an independent parse of §5 that extracts every bolded force ID per gravity entry (G6 → `2A-3`, `2B-1`, `2B-4`); and the Index's own two tables, which agree with the parse.

**Why the reconciliation went one-sided.** Doc_04 is unambiguous, and Doc_08's reading of it is faithful: Candidate 2's concern "does not persist into Augustine's phase under its own name; **what survives is a family resemblance to Candidates 6 and 7**, tested and classified as their own distinct gravities" (Doc_04 lines 47, 175, 182). The family resemblance runs to **both**. The fix pass applied that reasoning to G7's list and not to G6's, and then wrote a sentence asserting it had been applied to both.

**Why this matters, and what else rests on it.** Three things.

1. It is the same defect Round 2's H2 named — §3 and §5 disagreeing about the gravity relation — recurring inside the sentence that closes H2, and now worse in kind: the old §3 sentence was a loose "connects to"; the new one makes a positive, checkable, false claim about what another section of the same document says.
2. **§6's Author-Gravity convergence claim now rests on an undefended asymmetry.** §5's G7 entry calls G7 "Single-force-origin," and §6 line 358 builds on it: "The forces analysis independently reproduces the pattern at **G7**, whose single-force origin at 2A-4 mirrors its single-voice evidentiary base. **Where forces analysis and Author Gravity analysis agree from opposite directions, the finding is firmer than either alone.**" The single-force origin holds only because §5 excludes 2B-1 from G7 on the family-resemblance ground — while including it in G6 on the same ground. The convergence is not independent of a choice the document makes inconsistently and does not defend. Round 2 raised this exact structure against the pre-fix text; it survives in a different shape.
3. **The new §6 control is blind to it by construction.** Index §6 tests one direction only — "§3 asserts a connection §5's list omits" — and declares the reverse "not a defect." This is the reverse: §3 asserts a *dis*connection §5's list contradicts. I ran the generator against the live document: §6 prints "**No disagreements**." It is a control that returns clean on a live contradiction of precisely the kind it was installed to notice.

**Fix.** Decide the G6 question on Doc_04's own terms and make §3, §5 and §6 say the same thing. Either (a) §5's G6 entry drops `2B-1`, matching G7 and matching Doc_04's symmetric family-resemblance finding — in which case the Index's `2B-1` row becomes `G2` alone and §6's convergence claim is strengthened; or (b) §5 keeps `2B-1` under G6 *and* adds it to G7, and line 161 is rewritten to say what is actually true, with §5's "single-force-origin" wording and §6's convergence claim restated at the strength that survives. Do not close this by editing line 161 alone: the whole finding is that a claim about §5 was written without opening §5. Then widen §6's control to report both directions, with the reverse direction printed as an observation rather than a defect if that distinction is worth keeping.

---

### NEW-H2 — Construction-record voice is live inside Layer 2 at all three rewritten entries, and §8 certifies that it is not; the block invented to prevent this did not

**Site:** `Doc_08_Forces_Document.md` line 207 (2B-5 Layer 2), line 250 (3B-1 Layer 2), lines 262 and 264 (3B-2 Layer 2), against line 387 (§8's certification) and line 385 (§8's From-Within CONFIRMED).

**What I found.** Round 2's M3 found one build-thread sentence inside 2B-5's Layer 2. The fix pass removed that sentence and built a new structural device — a "**Layer 2 — construction-record notes (this build's voice, not the world's)**" block — and then certified at line 387:

> Three entries (2B-5, 3B-1, 3B-2) need source status, Reported-Experience marking or a correction recorded against them. **None of that is the world's voice**, so **none of it sits in Layer 2**: each is carried in a **Layer 2 — construction-record notes** block placed after the prose and labelled as this build's voice.

I extracted all seventeen Layer 2 blocks using the generator's own extraction rule (world-voice portion only, construction-record blocks split off) and scanned them for seven markers of construction-record register: this document's own force IDs, upstream `Doc_0n` citations, build-file references (`Source_Registry`, `lpc_`, `Lexicon_Deployment`, `INTAKE`), `§` references, self-reference to the layer scheme, "this build / this document / this entry," and evidentiary meta-statements ("is attested," "is documented").

**Fourteen of the seventeen Layer 2 blocks return zero on every marker. The three rewritten ones return hits, and they are the only ones that do.** The scan discriminates; it does not fire on everything.

The live sentences:

- **3B-1, line 250** — inside Layer 2: *"Augustine, at the end, goes back through everything he has written and corrects it — "cum quadam iudiciaria seueritate," with a certain judicial severity (Retractationes, Prologus; **Latin-only witness, `Source_Registry.md` row 209, rendering this build's own** — see 2B-5)."* A Registry row number, a second-witness disclosure, this build's own authorship of a translation, and a cross-reference to another force's ID — all inside the world's-voice layer, in the very entry for which a construction-record block was created to hold exactly this material. The block sits four lines below and holds only the Reported-Experience marker.
- **2B-5, line 207** — inside Layer 2: *"**Those are named at Layer 3** as effects on the reconstruction, **which is where they belong**."* A sentence about this document's own layer scheme, addressed to a reader of the document.
- **3B-2, lines 262 and 264** — inside Layer 2: *"**What is attested is the mode, not the feeling of it**"* and *"**That much is documented**, and it is why **the engagement at 2B-4** takes the form of exegesis rather than appeal to received practice."* Two evidentiary meta-statements and a force ID.

**Why this matters.** The Forces Framework's governing test for Layer 2, at FF line 170, is: *"could someone formed within this world recognize this as an honest account of how they understood what was happening to them?"* No one formed in this world can recognise a CSEL vendoring status, a `Source_Registry.md` row, a statement that a translation is "this build's own," a claim about which of this document's layers a topic belongs in, or a cross-reference to force 2B-4. FF line 168 is explicit that this is *"the error the Forces Framework was created to prevent,"* and FF line 255 that a Layer 2 failing it violates Articles 22 and 23 simultaneously. Doc_08's own header, line 8, sets the same rule for itself: Layer 2 "is the exception, and is written in this world's own vocabulary as the template requires."

So §8's "none of it sits in Layer 2" is false, and §8's "From-Within Principle — **CONFIRMED.** Every one of the seventeen forces carries a Layer 2 written in this world's own vocabulary" is false at three of seventeen — the same three, one round after the same certification was found false at one of seventeen. Round 2's M3 said of the sentence it found: "leaving it would mean the document's own From-Within certification is false on a sentence the document wrote to explain its From-Within correction." That is now true of the mechanism the document built to answer that finding.

This is the most consequential finding in the review, because Layer 2 is what a Representative is eventually built to inhabit, and because the defect survived a fix pass that was specifically about it.

**Fix.** Move each of the four sentences into the construction-record block that already exists at each of the three entries. At 3B-1 in particular, the parenthesis belongs in the block below it verbatim; the Layer 2 sentence needs nothing but "Augustine, at the end, goes back through everything he has written and corrects it." At 2B-5, delete the Layer-3 pointer sentence or move it to Layer 3. At 3B-2, recast "What is attested is the mode, not the feeling of it" and "That much is documented" as the block's business — the block already says both things, in better words, two paragraphs later. Then re-run the register scan across all seventeen entries before re-certifying §8, and say in §8 that the certification was checked rather than asserted.

---

### NEW-H3 — Both deliverables state a review history that is one round out of date and now false, at the exact line that carries a correction notice about that defect having happened one round earlier

**Site:** `Doc_08_Forces_Document.md` lines 430–437 (Document Log) and line 442 (Disposition). `lpc_Force_Index.md` lines 3–4 (Status and Revised) and line 143 (Disposition). Propagated from `gen_force_index.py`, where the Index's three lines are hard-coded string literals.

**What I found.** This deliverable pair has been reviewed twice. `Review-Artifacts/Doc08_Round2_Review.md` exists, is dated 2026-09-15, returned SUBSTANTIAL REVISION REQUIRED (3H 4M 3L 1C), and was committed in `561c2c35` — the same commit that produced the text under review. Neither deliverable says so.

Doc_08's Document Log ends at "Round 1 fix pass." There is no row for the Round 2 review and none for the Round 2 fix pass. Doc_08's Disposition, line 442, reads:

> **Not disposed. REVISED after Round 1; the revision is unreviewed.** `Review-Artifacts/Doc08_Round1_Review.md` returned **SUBSTANTIAL REVISION REQUIRED (4 HIGH, 5 MEDIUM, 3 LOW, 1 COSMETIC)** … every finding is addressed above or in the Index … **[CORRECTED, 2026-09-15:** this line previously read *"No review round has been run against this document,"* in the same commit range as its own review artifact — the identical defect Doc_07's Round 2 raised as NEW-H1 one document earlier.**]** … **The three rewritten Layer 2 entries and the regenerated Index are first-draft material that no reviewer has yet seen.**

Every substantive clause there is now wrong. The revision is not unreviewed; the review that matters is Round 2's, not Round 1's; the counts cited are Round 1's; the three rewritten Layer 2 entries are precisely the material Round 2 read and raised H1, M2, M3 and M4 against. And the correction notice embedded in that same sentence describes the identical defect, at the identical line, one round earlier — the document names the failure mode and then commits it again in the paragraph that names it.

The Index is stale in the same way and in three places: "**REVISED after Round 1 — not reviewed**," "**Revised:** 2026-09-15 (Round 1 fix pass)," and a Disposition citing Round 1's verdict and calling itself "the fix pass."

**Why this matters.** These are the lines a project lead reads to decide whether a document can be disposed. A reader of either file today is told the deliverable stands one round behind where it stands, with one review's findings outstanding rather than two rounds of history. Constitution Article 30 and CO-022 make disposition turn on review status; a false review-status line is not cosmetic in a governance sense. It also makes the pair's own audit trail unusable: fifteen of the twenty-four correction notices in Doc_08 cite "Round 2's" findings, against a Disposition that says no Round 2 exists.

**Compounding, and this is the part that is a defect in the Round 2 H3 fix rather than an omission.** The Index's three stale lines are hard-coded literals in `gen_force_index.py`, so re-running the generator reprints them. The new disclosure paragraph added for Round 2's H3 (Index line 7) enumerates what is hard-coded: *"the explanatory paragraphs under §§2, 3, 4 and 5, including this one."* The Status line, the Revised date and the Disposition are not in that list — and they are the hard-coded lines that have actually gone wrong. See also NEW-M3.

**Fix.** Add the two missing Document Log rows. Rewrite Doc_08's Disposition to state the true position: two independent review rounds run, Round 2 returned 3H 4M 3L 1C, this is the Round 2 fix pass, unreviewed. Update the Index's Status, Revised and Disposition strings **in the generator**, not in the file, and extend the hard-coded-prose list to name them. Then add a standing discipline: the review-history lines are the ones this build has now got wrong twice, so they should be the first thing a fix pass touches, not the last.

---

### NEW-H4 — The Index's new §7 cross-check prints, in the delivered file, a disagreement that does not exist: it reports as absent from Doc_08 §7 the one force the last fix pass added to §7

**Site:** `lpc_Force_Index.md` line 133; `gen_force_index.py` line 231 (`s7 = dict(re.findall(r"(\d[AB]-\d) \((Documented|Widely Accepted)\)", sec7))`); against `Doc_08_Forces_Document.md` §7's first list paragraph.

**What I found.** Index §7, the control added to close Round 2's M1, prints:

> - **`2B-3` is absent from §7's list** but carries `Documented` at §3.
>
> **Each line above is a disagreement between two hand-and-script derivations of the same relation. It is reported, not resolved.**

Doc_08 §7 lists `2B-3`. It reads: *"… 2B-2 (Documented), **2B-3 (Documented, with a contested secondary element — see below)**, 2B-4 (Documented) …"* and closes *"**All seventeen appear here**"* — with a correction notice stating that this list "previously named sixteen, silently omitting `2B-3`," which the last fix pass corrected.

The generator's regex requires the closing parenthesis immediately after the label. `(Documented, with a contested secondary element — see below)` does not match it, so `2B-3` falls out of `s7` and is reported missing. I confirmed this three ways: by tracing the regex against the live §7 (16 captures); by an exhaustive extraction of every force ID appearing anywhere in §7 (17, including `2B-3`); and by reading §7's paragraph, where `2B-3` is visibly present and bolded.

**Why this matters.** Three reasons, in ascending order.

1. A delivered artifact prints a false finding about its companion document. A reader who acts on it will "fix" §7 by re-listing a force already listed, or will conclude the pair has drifted when it has not.
2. The false positive is on **the exact entry the previous fix pass corrected**. §7 was hand-patched to add `2B-3`; the control written in the same pass reports that patch as missing. The control was evidently never run against the post-fix document — or, if it was, its one printed line was not read against §7.
3. `lpc_Decision_Log.md`'s Round 2 entry states that "**both new controls were regression-tested against that same pre-fix document before being trusted**." A regression test against the pre-fix draft is not a test of a control that reads a section the fix pass was simultaneously editing. This is the build's signature shape exactly: a check that proves something adjacent to the claim, then is trusted because it returned something.

**A second, latent defect in the same five lines.** `s7` recognises only `Documented` and `Widely Accepted`. Any force §7 labelled `Contested`, `Dominant Modern Reconstruction` or `Inferential/Thin` would fall out of the dictionary entirely and be reported as *absent* rather than as a *conflict*, so the `s7_conflict` branch is effectively dead code for three of the Constitution's five confidence levels. I demonstrated this by mutation (see the check-confirmation section): relabelling `1A-1` as `(Contested)` in §7 produces "`1A-1` is absent from §7's list," not "§7 says Contested, §3 says Documented."

**Fix.** Make the pattern tolerant of a parenthetical elaboration and of all five labels — capture the first label word inside the parentheses, whatever follows it — and re-run against the live document until §7 prints agreement. Then state in §7's prose that the control has been run against the current text, not only against a superseded one.

---

## MEDIUM

### NEW-M1 — The regression test the fix pass cites as validating the two new controls does not show what it is reported to show

**Site:** `lpc_Decision_Log.md` line 1191; `lpc_Force_Index.md` §6's closing paragraph ("**It catches the class of defect Round 1 caught by accident**").

**What I found.** The Decision Log records: *"both new controls were regression-tested against that same pre-fix document before being trusted: **three stubs flagged, one gravity disagreement flagged — exactly what Round 1 found by hand**."*

I reproduced the run rather than accepting it. Against `9eccc532`, the current generator prints exactly three `**STUB**` rows (2B-5, 3B-1, 3B-2), "3 force(s) MISSING a Layer 2," and one §6 disagreement. The numbers are right. The gloss is not.

**On the gravity disagreement.** The one it flags is **`1B-1`/G2**. It does **not** flag `2B-1`/G7 — the divergence Round 1 found by hand and named in its H1 fix instruction ("reconcile the 2B-1/G7 contradiction between Doc_08 §3 and §5 before regenerating anything"), and the one Round 2 built the whole of H2 around. I instrumented the control to show why: the pre-fix sentence is *"This force therefore connects to G2 in phase one and to G6/G7 in phase two"* — `CONNECT` matches, nothing disclaims it, but the gravity tokens are unbolded, and the control only counts `**G*n***`. It does not flag `2A-1`/G8 either: *"Confirms rather than reshapes **G1** and **G8**"* never reaches the bold test, because `CONNECT` has no verb for "confirms." Round 1's H1 table (lines 121 and 123) identified both `1B-1`/G2 and `2B-1`/G7 by hand. The control catches one of two, and the one it misses is the flagship.

Measured across the whole live document: of the **19** Layer-3 sentences that name a gravity, the control examines **7**. Ten are discarded because `CONNECT` does not recognise their verb ("is why," "gives," "enables," "terminates," "outlives," "confirms," "intensifies"); one is discarded by `DISCLAIM`, whose pattern includes the bare phrase `rather than` — a construction this document's house style uses constantly; one (pre-fix) by the bold requirement. The Index's §6 does state the bold-token weakness in general terms. It does not state that the control misses the specific defect it cites as its reason for existing.

**On the three stubs.** Round 1 found **two** genuinely blank Layer 2 entries. Doc_08 §9's own correction notice says so: *"Two (2B-5, 3B-2) were genuinely blank … **the third (3B-1) was never blank at all**, so the line misdescribed its own document in both directions."* The control flags three, because the pre-fix 3B-1 contains the words "left unfilled." By the document's own considered account of its own history, that is a false positive, recorded as confirmation.

**Why this matters.** The regression test is the evidence offered that the two controls are real and not another H3. It is the right instinct and the right method, and it was read the way the build keeps reading its checks: the numbers came back, so the controls were trusted. Reproducing it takes four minutes and shows the §6 control catching one of two known instances and missing the named one.

**Fix.** Restate the regression result at both sites in the terms it actually supports: the stub control flags all three entries Round 1's H4 covered, one of which Doc_08 §9 holds was not blank; the §6 control reproduces one of the two §3/§5 divergences Round 1 found by hand and misses `2B-1`/G7 because the tokens there are unbolded. Then broaden `CONNECT` (or invert it: flag every gravity-naming Layer-3 sentence and let a reader dismiss the attestation claims) and narrow `DISCLAIM`, which currently suppresses on the phrase "rather than."

### NEW-M2 — The *Retractationes* quotation silently normalises the source file's OCR, in the same clause that certifies the OCR was retained

**Site:** `Doc_08_Forces_Document.md` line 205 (2B-5, Layer 2) and line 213 (2B-5, construction-record note). Source: `cic/texts/augustine_retractationes-lat_knoll-csel36.txt` line 1511.

**What I found.** Doc_08 quotes, as the Augustinian pillar of its transmission-consciousness argument:

> *"siue in libris siue in epistulis siue in tractatibus cum quadam iudiciaria seueritate"*

and discloses at line 213: *"the Latin is quoted with **the source file's own OCR retained**."*

The vendored file's Prologus reads:

> tror, ut opuscula mea **sine** in libris siue in epistulis siue in
> 5 tractatibus cum quadam iudiciaria seueritate recenseam et,

The first `siue` is OCR'd `sine` — the u/n confusion the file's own provenance header names as one of its expected noise classes. The string `siue in libris` occurs **zero** times in the file; `sine in libris` occurs **once**. I confirmed this three ways: a grep for each form, a whole-file count, and a raw byte-span dump around `iudiciaria seueritate`.

So the one OCR defect inside the quoted span was silently corrected, in the clause that says it was not.

**What is sound here, stated so the fix is scoped.** The emendation restores the true CSEL reading: Knöll's apparatus at the same locus records no `sine`/`siue` variant, and the sense requires the tricolon. The English rendering is accurate — *"whether in books or in letters or in treatises, with a certain judicial severity"* for the quoted span, and *"as with a censor's pen"* for `uelut censorio stilo`, which the file carries cleanly at line 1513. The shorter quotation at 3B-1, *"cum quadam iudiciaria seueritate,"* reproduces the file exactly. The Registry row (209), the second-witness caveat, and `INTAKE.md`'s second limb are all correctly identified. Doc_02 §1's claim that no complete English translation is vendored is verbatim accurate, and no English *Retractationes* file exists in `cic/texts/`.

**Why this matters.** The disclosure exists because the quotation is unverifiable by the ordinary route — there is no English witness to check it against — so the reader's only recourse is to open the Latin file. A reader who does that, searching the string the document prints, gets no hits and has to guess whether the quotation is wrong, the file is wrong, or the document has emended silently. The document told them which, and told them wrong. This is the one entry in the matrix whose subject is what happens to a text in transmission, in a build with eight documented instances of reading apparatus as text and one round-old finding about quotation provenance.

**Fix.** One clause. Either print the file's reading with the emendation marked — `s[i]ue in libris` or `sine [sc. siue] in libris` — or keep the corrected text and change line 213 to say that the file's OCR reads `sine` at the first limb and that this build has emended it to the reading Knöll prints. Either is honest; the present combination is not.

### NEW-M3 — The Index's hard-coded-prose disclosure, added to close Round 2's H3, is under-inclusive in exactly the places where the hard-coded prose is wrong

**Site:** `lpc_Force_Index.md` line 7; `gen_force_index.py` lines 244–252 (header literals), 318–336 (§6 literals), 340–352 (§7 literals).

**What I found.** The disclosure reads:

> **Derived from the source document, and therefore re-checked on every run:** every table in §§1–4, all counts and totals, **the §6 reconciliation report and the §7 cross-check**. **Hard-coded prose, re-verified by nothing:** the explanatory paragraphs under §§2, 3, 4 and 5, including this one.

Three problems, each checkable against the generator.

1. **§6's no-disagreement paragraph is a hard-coded literal, not a report.** It is the `else` branch's string, and it names three specific forces: *"The three Round 2 found — `2B-1`/G7, `1B-1`/G2, `2A-1`/G8 — were reconciled in the source document."* That sentence prints unchanged whatever the document says, on any run where `mismatch` is empty. It is presented under a heading the disclosure classifies as derived.
2. **§6's and §7's explanatory paragraphs are likewise literals** ("What this tests, narrowly…", "This is a weaker test than it looks…", "Why this section exists…", "The honest statement of the design rule…"), and the disclosure's hard-coded list stops at §5.
3. **The Status line, the Revised date and the Disposition are literals and are not named at all** — and they are currently false (NEW-H3).

**Why this matters.** The disclosure exists because Round 2 proved a blanket "re-running the generator is the check" claim covered less than it sounded like. The replacement is a narrower claim that still covers less than it sounds like, in the same direction, and the lines it wrongly implies are re-verified are the ones that have drifted.

**Fix.** List the hard-coded prose exhaustively — the header block including Status/Revised/Disposition, and the explanatory paragraphs under §§2–7 including both branches of §6 and §7. Say that in §§6 and 7 only the *findings* (the mismatch table, the disagreement lines, the agreement sentence) are derived, and that everything around them is commentary.

### NEW-M4 — §9's Reported-Experience tick says "at `3B-1` and there only"; the same fix pass applied the status at `3B-2`

**Site:** `Doc_08_Forces_Document.md` line 416, against line 268. Related understatements at line 351 (§5 item 4) and line 377 (§7).

**What I found.** Round 2's M2 required Reported-Experience Status at 3B-2. The fix pass added it, at line 268: *"***Reported-Experience Status* (Constitution Article 17; Forces Framework §3) applies to the first sentence above**…"*. §9's completion tick, line 416, was not updated:

> - [x] Reported-Experience Status applied where self-understanding is historically uncertain but formationally central — **at `3B-1` and there only** …

That is now false, and emphatically so. §5 item 4 and §7 are not false, but both name only 3B-1 and so understate compliance.

This tick already carries a Round 1 correction notice for "pointing at nothing." It now points at the wrong scope — a fix applied at one site and missed at the sites that describe it. That §9's tick is the certification line makes it worse than an ordinary stale cross-reference: §9 is what a reader checks instead of re-reading the matrix.

**Fix.** "at `3B-1` and `3B-2`." Update §5 item 4 and §7's sentence to match. The L4 template's Cell-2B transmission instruction also names the status ("apply Reported-Experience Status where appropriate"); 2B-5 carries none, which is defensible — its Layer 2 rests on four verified quotations — but worth one clause saying so, since the template names the slot.

### NEW-M5 — The "Layer 2 — construction-record notes" block is a self-invented convention: no template defines it, no sibling build uses it, its label contradicts §8's account of it, and it moves the Reported-Experience marker out of the layer the template places it in

**Site:** `Doc_08_Forces_Document.md` lines 209, 252, 266 (the three blocks); line 387 (§8's account). Against `L4-Templates/[world-code]_Forces_Document.md` lines 95–106, 127–136, 296–311, 437–443; FF §3.

**What I found.** The L4 Forces template defines exactly three headed layers per force and nothing between them. Its Section 3 preamble is categorical — "**No force should appear in a cell without Layer 1, Layer 2, and Layer 3 documentation**" — and its Layer 2 bracket text places the Reported-Experience marker **inside Layer 2**: *"Where this self-understanding is historically uncertain but formationally central, mark as: 'Reported as the world's own self-understanding — not assessed for historical accuracy; confidence calibration applies to the historical-event layer only.'"* FF §3's table says the same: "Reported-Experience Status applied where self-understanding is historically uncertain but formationally central" is a property *of Layer 2*.

I grepped all eight sibling Doc_08 files for any interposed block. **None uses one.** Two take a different route with the same problem: Alexandria writes "*Layer 2 — not applicable:*" at 3A-2 as "a deliberate proportionality exception"; Donatism writes the absence *inside* Layer 2 at four forces and then, at its §8, records having *moved* inline document citations out of four "not recoverable" Layer 2 entries into Layer 1 and Layer 3 — the same problem solved without inventing a fourth block.

Two things are right about the lpc convention and should be said. It answers a real finding; and keeping build-voice material out of the world's voice is the correct instinct, better than Donatism's "move it to Layer 1 or 3" where the material is genuinely about neither. But:

- **The label reuses a governed term for something the document says is not that thing.** §8 line 387 says the content does "not sit in Layer 2," while the block is headed "**Layer 2 — construction-record notes**." A reader scanning for the layer headings now finds two "Layer 2 —" headers at three forces, and the generator has to special-case the string to tell them apart (`re.split(r"\*\*Layer 2 — construction-record note", raw)[0]`). If a later pass renames the block, the split silently fails and the stub test starts counting note text as world-voice prose.
- **It relocates the template's own instrument.** The Reported-Experience marker at 3B-1 now sits outside the layer it qualifies and reaches back into it ("applies to the whole Layer 2 above"), which is not how either governing document frames it.
- **Round 1's M3 condemned a self-invented "Reported-Experience-*adjacent*" label.** This is not that — it is a structural container, not a confidence status, and it is honestly labelled as this build's voice. I do not grade it as the same defect. But it is undefined by any governing document, unprecedented across twelve worlds, and it did not in fact do the job it was built for (NEW-H2).

**Fix.** Keep the device — it is better than the alternatives — and fix three things. Rename it so it does not claim to be a layer: "**Construction-record notes on this entry (this build's voice, not the world's)**." State in §8 that this is a convention this document introduces, that no template defines it, that no sibling uses it, and why it is preferable to writing the same material into Layer 1 or Layer 3 as Donatism did — flagged for the project lead rather than adopted silently, in the same spirit as the L3 disclosure at line 391. And keep the Reported-Experience marker inside Layer 2 where the template puts it, with only the source-status and correction material in the block.

---

## LOW

### NEW-L1 — §8 says three Layer 2 entries were unwritten; §9 says one of the three "was never blank at all"

**Site:** `Doc_08_Forces_Document.md` line 389 against line 408, and against line 377.

Line 389: *"An earlier version of this document left **three** Layer 2 entries unwritten — 2B-5, 3B-2 and 3B-1."* Line 408: *"Two (2B-5, 3B-2) were genuinely blank … **the third (3B-1) was never blank at all**, so the line misdescribed its own document in both directions."* Line 377's correction notice takes §9's side: *"this previously reported two entries left unfilled and one marked as not experienced from within."*

Two live correction notices in the same document give incompatible accounts of the same defect. I confirmed the underlying fact at `9eccc532`: 3B-1's pre-fix Layer 2 is 313 characters of prose that declares itself *"left unfilled"* — so "unwritten" is arguable and "never blank at all" is also arguable, but they cannot both be the document's position. This is the class of defect the build has been grading since Round 2's L1: a correction notice that misdescribes the defect it corrects.

**Fix.** Make line 389 match §9's line 408: two blank, one written-but-self-declared-unfilled.

### NEW-L2 — §8 drops "complete" from Doc_02's finding about the *Retractationes*

**Site:** `Doc_08_Forces_Document.md` line 393.

§8 writes: *"no English translation vendored anywhere in this corpus, `Doc_02` §1."* Doc_02 §1 says: *"**no complete English translation** of the Retractationes is vendored, but substantial excerpts are, quoted inside NPNF's own editorial apparatus"* — and names the specific excerpt (Retractationes II.18, at `npnf104`'s preface) that Registry row 209 was acquired to close at first hand. 2B-5's own note at line 211 gets this right ("no complete English translation is vendored anywhere in this corpus"); §8 does not. Minor, but §8 is the paragraph arguing that the Augustinian exhibit is disclosed rather than passed off, and it overstates the disclosure's premise in a build where the same word was corrected one document earlier.

**Fix.** Insert "complete."

### NEW-L3 — The L3 fix says the governing set has "one scoped exception in it"; it has more than one, and two sibling builds have relied on the others

**Site:** `Doc_08_Forces_Document.md` line 391.

The new paragraph is right about the L4 template's Proportionality carve-out, quotes it exactly, and reaches the right outcome. But it concludes: *"an unqualified 'permits no exceptions' overstated a governing set with **one scoped exception** in it."*

The Forces Framework's own Governing Principle, FF line 34, closes: *"Where direct testimony is absent, the Reported-Experience Status applies. **Where even inferential reconstruction is unsupported, the builder names the absence and documents the limit** rather than supplying modern interpretation as substitute."* Constitution Article 19's reconstruction clause runs the same way — reconstruction is *"rare, secondary to naming absence."* Whether "names the absence" can be satisfied *inside* a written Layer 2 (as Donatism's 2B-2 does, at length and specifically) or licenses a terse absence statement is exactly the question Round 1's H4 turned on, and FF §3's "not optional" does not settle it by itself. Two sibling builds read it the other way: Donatism marks four Layer 2 entries "not recoverable from surviving sources," and Alexandria writes "*Layer 2 — not applicable*" at 3A-2 as "a deliberate proportionality exception, not an omission." Both are disposed documents in this portfolio.

I am not asking the outcome to change — lpc's transmission entries are richer than the stubs they replaced and the research that produced them was the right work. But the count is wrong and the portfolio position is more interesting than the sentence allows, and FF §6's instruction in the analogous case is to flag rather than resolve.

**Fix.** "a governing set with more than one scoped allowance in it," and one clause noting FF's own name-the-absence limb and the two sibling builds that read it as permitting a stated absence — flagged for the project lead, not resolved here. See the CO-022 section.

### NEW-L4 — 3B-2's construction-record bullets point at "the first sentence above" and "the second sentence" across two paragraphs

**Site:** `Doc_08_Forces_Document.md` lines 268 and 269.

3B-2's Layer 2 is two paragraphs of two and three sentences. The first bullet applies Reported-Experience Status to "**the first sentence above**"; the second says "**The second sentence** is a bound, not a reconstruction." Read against the second paragraph the referents work ("The inheritance was therefore received as text…" and "And the gap itself was not experienced as a gap…") and the bullets' own content confirms that reading. Read against the whole of Layer 2 they point at "What is attested is the mode…" — an evidentiary statement Reported-Experience Status makes no sense applied to. Given that the marker's scope is what Round 2's M2 was about, an ambiguous referent is worth removing.

**Fix.** Quote the opening words of each sentence, as the 3B-1 marker does with "the whole Layer 2 above."

---

## COSMETIC

### NEW-C1 — The M4 notice's count of prior sites is ambiguous and probably one short

`Doc_08_Forces_Document.md` line 213: *"this claim previously stood **twice**, unquoted and uncited."* Round 2's M4 named three sites (2B-5 line 205, 3B-1 line 244, §8 line 378). The word *Retractationes* appears twice in the pre-fix document (2B-5 and §8); the *claim* stands at three, since 3B-1 makes it without naming the work. Scoped to the two rewritten Layer 2 entries, "twice" is correct; scoped to Round 2's own site list it is short by one. Given that this build now grades miscounted correction notices, one word of scope would close it.

**Fix.** "previously stood at both of these entries" or "previously stood three times."

### NEW-C2 — The M3 notice describes the removed clause as what 2B-5's Layer 2 "opened with"

`Doc_08_Forces_Document.md` §8 line 387: *"2B-5's Layer 2 opened with *'which an earlier version of this entry wrongly denied'*."* The clause was the tail of the opening sentence, not its opening. Trivial, and reported only because the surrounding notice is otherwise exact.

---

## Additional checks that returned clean, stated plainly — and which of them I tested hardest

**Quotation fidelity, re-verified by the widened method (tested hardest).** I rebuilt the verification pass Round 2's H1 called for: mark `<note>` spans, then preserve `<div1>`–`<div4>` `title=` attributes as sentinels *through* the tag strip, so each hit returns both a note verdict and its containing work. Run over every quotation in the matrix:

| Quotation | Site | Note? | Containing work |
|---|---|---|---|
| "these thirteen letters sent forth at various times…" | 2B-5 | outside | To the Presbyters and Deacons Assembled at Rome (Ep. XIV) — Cyprian |
| "you always read my letters to the very distinguished clergy…" | 2B-5 | outside | To Cornelius, Concerning Fortunatus and Felicissimus (Ep. LIV) — Cyprian |
| "matter, and even the paper itself, gave me the idea…" | 2B-5 | outside | To the Presbyters and Deacons Abiding at Rome, A.D. 250 (Ep. III) — Cyprian |
| "as it actually came to hand, that you may examine…" | 2B-5 | outside | same — Cyprian |
| "to send a copy of this letter to whomsoever you are able" | now attributed correctly in 2B-5's note | outside | **From the Roman Clergy to the Carthaginian Clergy** (Ep. II) — confirming Round 2's H1 and Doc_08's corrected attribution |
| "it is the shepherd that is chiefly wounded…" | 1A-1 | outside | On the Lapsed — Cyprian |
| "your suffrage and God's judgment" / "ancient venom" | 1B-2 | outside | To the People, Concerning Five Schismatic Presbyters (Ep. XXXIX) — Cyprian |
| "by the judgment of God and the favour of the people…" | 1B-2 | outside | The Life and Passion of Cyprian… By Pontius the Deacon |
| "thousands of certificates were daily given…" | 2B-2 | outside | To the Presbyters and Deacons Assembled at Rome (Ep. XIV) — Cyprian |
| "even of the plenary Councils, the earlier are often corrected…" | 2B-4 | outside | *On Baptism, Against the Donatists* (`npnf104`), Bk. II ch. 3 — Augustine |

Every one is outside editorial apparatus and by the figure Doc_08 says wrote it. Each phrase occurs exactly once in its volume. This is the check Round 2 asked to have widened, and the widening holds.

**The Index's derived content (tested hardest, second).** An independent parse of Doc_08 §3, §4 and §5 — written without reading the generator's derivation code — reproduces the Index's master-table gravity column and confidence column for all seventeen rows, the by-gravity table for all eight gravities including the G4 set-reference expansion to five, the 14/3/0/0/0 confidence distribution, and the 15-row connection table. **Zero mismatches.** The `2A-2` non-connection is the one `(none)` row; the cross-cell inversions are consistent in both directions; `1B-3` is correctly shown as the one force §4 neither connects nor deliberately isolates, and correctly carried as an open observation rather than given a manufactured link. The Index's substance is sound; every Index finding above concerns what it *says about itself* or what its two new controls report.

**Doc_04 fidelity.** Doc_08's family-resemblance reading is faithful to Doc_04, at three loci (lines 47, 175, 182): Candidate 2's concern does not persist under its own name and survives as a family resemblance to Candidates 6 and 7. The 1B-1→G2 and 2A-1→G8 additions to §5 are both correct and neither strains a phase-bound claim — 1B-1, 2A-1, 1A-1 and 2B-2 are all phase-one forces, so §5's "all three connected forces are phase-one forces" for G8 and the Cross-Strand note's phase-bound claims survive the additions intact. All eight Candidate→G mappings and classifications re-verify against Doc_04 §4.

**Governing-document quotations.** FF §3's "This is not optional. All three layers are required for every force" — exact at FF line 141. FF §5's incomplete-ecology sentence, quoted at §5's G5 entry with the `[A]` bracket marking the recapitalization — exact. The L4 template's Proportionality carve-out, quoted at §8 line 391 — exact against template lines 104–106. Doc_04's Candidate 5 heading — now exact. Doc_02 §1's Retractationes sentence — accurate at 2B-5 (see NEW-L2 for §8). `INTAKE.md`'s second limb — exists, at lines 23–28, in the words Doc_08 relies on. Constitution Article 17 is the confidence/reported-experience article, as cited.

**Counts and upstream pointers.** "8 of 19 entries carry an Author Gravity note" — `Lexicon_Deployment_Index.md` §6 line 129 says exactly that; Round 1's H3 is closed correctly. Doc_07 §3A's textual-not-successive finding is at Doc_07 line 243, and 3B-2's citation of it (corrected from "Doc_05 §3A") is right. Doc_06 §5 item 7's headword-sweep finding is at Doc_06 line 129, as cited. `Lexicon_Deployment_Index.md` §7's seven local instances and the eighth recorded only in the Decision Log — Doc_08's account of all three destinations is still exact.

**Article 19 / invention.** No Layer 1 claim is asserted without a traceable source. The 133-year silence is held as a silence; no Donatism-territory material fills it. NEW-H2 is a register violation, not an invention; NEW-M2 is a provenance misstatement, not a fabricated quotation.

---

## Job 2's harder question — what these controls would still miss

I ran four mutations against the live Doc_08 and regenerated the Index each time. A positive control is included so the reader can see the instruments are not simply inert.

| Mutation | §5 stub | §6 | §7 |
|---|---|---|---|
| **Baseline (live document, unmutated)** | clean | **CLEAN** — and NEW-H1's contradiction is live | **false positive on `2B-3`** |
| §3 asserts "**G6** is strengthened by this force," a connection §5 omits, using a verb `CONNECT` does not know | clean | **CLEAN — missed** | unchanged |
| §7 relabels `1A-1` `(Contested)` against §3's `Documented` | clean | clean | **"`1A-1` is absent from §7's list" — the wrong diagnosis** |
| A Layer 2 replaced with fluent modern-analytic prose ("a coercive administrative instrument whose sociological function…") | **clean — missed** | clean | unchanged |
| *(positive control)* §5 drops `2A-4` from G7 | clean | **1 flagged — caught** | unchanged |

So, stated plainly: the two new controls will still miss **(a)** a §3 claim that a force *does not* connect where §5 says it does — the live NEW-H1; **(b)** any §3 connection claim whose verb is outside a nine-item list, or whose gravity token is unbolded, or whose sentence contains "rather than" — roughly twelve of the nineteen gravity-naming Layer-3 sentences in this document; **(c)** a §7 label *conflict* in three of the Constitution's five confidence levels, which is reported as an absence instead; **(d)** a Layer 2 that is long, fluent and entirely in the analyst's register — which the Index says honestly, and which is the live NEW-H2; and **(e)** every hand-carried count in Doc_08 §§8 and 9 ("seventeen," "fifteen," "all eight," the ten checklist ticks), none of which any control reads, and one of which is currently false (NEW-M4).

The structural point is the one the Index itself half-states at §6: a control written by reading the defect that was found describes that defect rather than its class. `CONNECT` is a list of the verbs that happened to appear in the sentences someone looked at. `DISCLAIM` is a list of the phrases that happened to produce false positives on the first run. Both are fitted to a sample of one document at one moment, and both will drift out of coverage the moment the prose is edited — which is what happened between the pre-fix draft and the live one.

---

## A check that failed and was confirmed before being trusted — and four of my own that were defective

**The one I confirmed before reporting.** Index §7's printed line, "`2B-3` is absent from §7's list," is a failing check. Before reporting that §7 was *not* missing `2B-3` I confirmed it three ways on three code paths: (1) traced the generator's own regex over the live §7 and got 16 captures, with `2B-3` the one absent; (2) extracted every force ID appearing anywhere in §7 by a different pattern and got 17, `2B-3` included; (3) read §7's list paragraph directly, where `2B-3` is present, bolded, and carries a correction notice about having been added. Had I stopped at (1) I would have reported §7 as genuinely missing an entry — the failing check proving something adjacent to the claim, and being trusted because it returned something. The same discipline applied to NEW-M2: `grep "siue in libris"` returning zero hits proves nothing on its own, so I also grepped the alternative form (one hit) and dumped the raw byte span around `iudiciaria seueritate`.

**My four defective checks, reported because a reviewer who reports only the checks that survived has concealed the base rate of their own instrument.**

1. **A column-count filter that returned a clean zero for the wrong reason.** Measuring truncated Force names in the pre-fix Index, I filtered table rows with `len(columns) >= 8` and got **0 names at or above 86 characters** — which would have made Round 2's L1 wrong about "two Force names." The pre-fix master table has **seven** columns, not eight; the filter matched nothing and reported zero. Re-running with an exhaustive listing of all seventeen rows returned two names at exactly 88, confirming L1. This is precisely the shape the brief warned about, committed by me, and caught only because the answer contradicted a finding I had independent reason to believe.
2. **A fixed-width context window that suppressed a real hit.** Counting pre-fix mentions of the *Retractationes* I used `grep -o ".\{80\}Retractationes.\{120\}"`, which requires 120 characters of trailing context; the 2B-5 mention at line 205 has about sixty, so it was silently dropped and I read "one mention" where there are two. Caught by re-running a plain `grep -c`.
3. **A Layer-3 extractor that ran past the end of the force.** My first register scan split the document on `#### Force ` rather than terminating each force at `## Section 4`, so force 3B-2's "Layer 3" segment swallowed Sections 4, 5, 6 and 7 — and my instrumentation duly attributed §5's gravity lists to 3B-2's Layer 3. The output looked substantive, which is exactly why it was dangerous. Re-run with the generator's own boundary rule, and the results reported above are from the corrected version.
4. **A mutation harness whose result parser could not see the result.** My first mutation run reported "§7 clean" for every case, including the baseline — because my regex for §7's finding lines required `**` immediately after `- `, and the real line is ``- **`2B-3` is absent…``. The harness was reporting the absence of its own match as the absence of a finding. Caught by re-running against a baseline whose correct answer I already knew, which is the only reason a baseline case was in the table.

Three of these four returned a *clean* result. That is the failure mode this build keeps producing, and it is not confined to the documents under review.

---

## Is the deliverable adequate to proceed to Doc_09?

**No — but the distance is short, and shorter than four HIGH findings suggests.**

The substance of the forces analysis is sound and has now survived three rounds: seventeen forces correctly distributed across six populated cells; both transmission entries present as named forces of their own; fifteen cross-cell connections with correct direction, including one recorded non-connection and one explicitly non-causal coincidence; all eight confirmed gravities connected; confidence calibration correct force by force on independent re-derivation; every quotation verified to its containing work. The Index's derived tables are correct. That is a real Step 8 deliverable underneath the defects.

Doc_09 will draw two things from here: the gravity–force connections, through the Index, and the transmission entries, which are where a story repository's tier justifications and its Absent Stories answer have to be grounded. Both are where the remaining defects sit.

- **NEW-H1 is blocking.** Doc_09 will cite gravity–force connections. `2B-1`'s connections are currently stated two different ways in the same deliverable pair, and the resolution bears on whether G7's single-force origin — and §6's convergence finding — hold at the strength claimed. Whichever way it goes, it must be settled before anything cites it.
- **NEW-H2 is blocking.** Doc_09's governing discipline is that nothing is invented and every story's standing is visible. Layer 2 is the register a story repository inherits its voice from. Three of seventeen Layer 2 entries currently contain build-thread apparatus — a Registry row number, a translation-provenance disclosure, this document's own layer names and force IDs — and both transmission entries are among them. That material propagates.
- **NEW-H3 is blocking for disposition rather than for Doc_09's content**, but it is the cheapest of the four to fix and the one a project lead is most likely to act on wrongly.
- **NEW-H4 and NEW-M1 are not blocking for Doc_09.** They are defects in what the Index says about its own checks. They should be fixed because the next reviewer will otherwise be invited to trust a control that reports a disagreement which does not exist, and a regression result that does not show what it is said to show.

**No new source research is required.** Everything above is settled inside files already open in this build.

---

## CO-022 escalation assessment

Checked against Doc_04–Doc_07's disposition records, `lpc_Decision_Log.md`'s 2026-09-15 entries, and Doc_08's own Section 1 and Disposition.

**Representative identity, title, or voice — does not apply.** Confirmed; Doc_08 makes no identity, title or voice decision.

**Portfolio-level or cross-world — four items, none decided here, all accurately restated.** The eighth editorial-apparatus instance is correctly attributed, with both destinations correctly described as showing seven and none. The standing-method widening Round 2 recommended (recover the containing work's heading alongside the note spans) is applied at 2B-5 Layer 3 item 2 and is the right form of words; I used exactly that method and it works.

**One observation for the project lead, which I put as a widening of the fourth item rather than a fifth.** NEW-L3 surfaces a genuine portfolio-level inconsistency about what the Forces Framework's three-layer requirement permits. lpc's Doc_08 §8 states the requirement admits no exception; Donatism's Doc_08 marks four Layer 2 entries "not recoverable from surviving sources" and states the absence inside the layer; Alexandria's Doc_08 writes "*Layer 2 — not applicable*" at 3A-2 as "a deliberate proportionality exception"; and the Framework's own Governing Principle (FF line 34) contains a name-the-absence limb that the L4 template's Proportionality carve-out is not the only source of. Three worlds have read one rule three ways. That is the lead's question, not this thread's, and lpc's own resolution — write the entries — is the safest of the three regardless of how it is settled. I do not think it opens a new category; it belongs with the existing governance/methodology item about template-versus-framework conflicts.

**A second observation, on the same item.** NEW-M5's construction-record block is a structural convention introduced by one world and used by none of the other eleven. If it is the right answer to the Layer-2-versus-build-voice problem — and I think it is closer to right than either sibling alternative — it belongs in the L4 template rather than in one world's Doc_08. If it is not, it should be named as a local departure. Either way it should not stay undeclared.

**Governance or methodology — open, unchanged, four items.** Confirmed. All fifteen findings above are correctable inside this build thread's own editing authority; none is a governance question.

**Unresolved tensions — one open**, the 411 *Gesta*, confirmed relied on for nothing in this document.

**This review adds no escalation item.**

---

## On the brief that commissioned this review

Checked rather than accepted, per its own instruction. Everything material in it held: the generator is where the brief says, and reproduces the committed Index byte-for-byte; the three construction-record blocks are at 2B-5, 3B-1 and 3B-2 and no template defines them; §5's G2 and G8 lists did gain `1B-1` and `2A-1`; 2B-1's Layer 3 was rewritten to a family-resemblance reading; the Retractationes file is at the path given, is Registry row 209, carries OCR noise, and has no vendored English counterpart; the "3 stubs, 1 disagreement" regression claim reproduces exactly; Round 1's and Round 2's counts are correct; the note-marking and heading-recovery methods work as described, and `cyprian.xml` does carry work names on `<div2>`/`<div3>` `title=` attributes rather than `<head>` elements.

Two small corrections, neither affecting a finding:

1. The brief says the Latin quotation and English rendering were "newly added at 2B-5 **and 3B-1**." The 3B-1 addition is a short Latin tag (*"cum quadam iudiciaria seueritate"*) with a rendering and a provenance parenthesis, not the full quotation; the full Prologus quotation and the `uelut censorio stilo` tag are at 2B-5 only. This matters for NEW-M2's scope: the OCR normalisation affects the 2B-5 quotation alone, and 3B-1's shorter tag reproduces the file exactly.
2. The brief says the last pass "claims it regression-tested both new controls against the pre-fix document … and got '3 stubs, 1 disagreement.'" It does, at `lpc_Decision_Log.md` line 1191 — but the claim as written is "**exactly what Round 1 found by hand**," and that gloss, not the numbers, is what fails (NEW-M1). The numbers reproduce.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**4 HIGH · 5 MEDIUM · 4 LOW · 2 COSMETIC — 15 in total.**

The substance of this forces analysis is good and is now well tested: the matrix, the connections, the gravity synthesis, the confidence calibration and the Index's derived tables all re-derive correctly and independently, and the ten quotations in the matrix verify to their containing works under the widened method Round 2 called for. Ten of Round 2's eleven findings are genuinely closed, several of them exactly.

But for the second consecutive round, the fix pass's own new material is where the serious defects are. The sentence that closes Round 2's H2 makes a false claim about §5 that §5 contradicts three sections below, and the control built to catch that class of defect is blind to it by design. The block invented to close Round 2's M3 did not clear construction-record voice out of Layer 2; a discriminating scan finds it in all three rewritten entries and in none of the other fourteen, while §8 certifies the opposite. The control built to close Round 2's M1 prints a disagreement that does not exist, about the very entry the same pass added. And both files now state a review history that stopped being true when the review artifact next to them was written — at the exact line that carries a correction notice about that having happened one round earlier.

**What I tested hardest, and what held:** the quotation pass (ten quotations, note-span plus containing-work heading, on two files and two code paths), the independent re-derivation of every Index table (zero mismatches across 17 rows, 8 gravity rows and 27 force–gravity pairs), and the Doc_04 family-resemblance reading, which Doc_08 renders faithfully. **What I tested hardest and which failed:** the two new controls, under a reproduced regression run and a four-case mutation test, and the Layer-2 register, under a scan that returns zero on fourteen of seventeen entries and fires on exactly the three the last pass rewrote.

Four focused corrections — settle `2B-1`'s gravity relation in §3, §5 and §6 together; move four sentences out of three Layer 2 entries; make both files' review-history lines true and fix them in the generator; and widen two regexes so the §7 cross-check stops printing a false finding — would put this deliverable within reach of clearance. No new source research is required.

*End of Round 3 review. Simulated review — informational only, not an Article 31 substitute.*
