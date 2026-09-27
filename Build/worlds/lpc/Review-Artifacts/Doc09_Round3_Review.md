# Doc_09 — Round 3 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

**Deliverables reviewed together:** `Doc_09_Story_Inventory.md`; `Story-Chunks/` (`lpcstory001`–`lpcstory007`); `lpc_Story_Index.md`; `scripts/gen_story_index.py`.
**State on arrival:** all four REVISED after Round 2, unreviewed.
**Date:** 2026-09-15.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**1 HIGH · 10 MEDIUM · 12 LOW · 5 COSMETIC.**

**The single HIGH is one sentence, and it was written by the pass that closed the finding about that sentence.** `lpcstory003`'s Do-Not-Retrieve rule now asserts that *Ep.* XXXIV "says nothing of" the lapsed. The letter names the lapse of some as the cause of the vacancy Numidicus fills — **in the same sentence the chunk quotes the first half of**. Round 1's L1 found the old wording wrong and supplied the corrected clause; the fix pass wrote the negation of it.

**Everything else is bookkeeping, generator hygiene, and one-line corrections.** The repository itself is sound: I re-verified every quotation against the corpora independently and found no invented participant, event or outcome, no quotation resolving inside an ANF `<note>` or *Argument*, and no intra-corpus misattribution. Three of the four things the Round 2 fix pass was asked to argue — `lpcstory002`'s tier, `lpcstory007`'s band, the Absent-Stories renderer — I tested hard and they hold.

**Had the `lpcstory003` sentence not been there, this would have been MINOR REVISION.** I want that on the record, because the build needs to be able to reach it and is close.

---

# Method

**What I did not inherit.** I re-derived every number in the brief. The brief's "**14 halting sites, self-counted**" is wrong, and the way it is wrong is the finding (M4): there are **thirteen**. I confirmed that three ways — `grep`, an `ast` parse of the script, and forcing all thirteen individually from fresh copies until each produced its own distinct `FATAL`. The fourteenth "site" the script counts is the string literal `"sys.exit("` inside the expression that does the counting.

**Corpus harness, built from scratch rather than reused.** I parsed `cyprian.xml` with ElementTree into 1,985 body paragraphs, having first established that 2,873 of the file's 4,858 `<p>` elements sit *inside* `<note>` elements and must never enter the searchable text. `<note>` subtrees were replaced by a sentinel that preserves the word boundary rather than deleted. Work attribution was taken from `title=` on the enclosing `div2`/`div3`, never from running text. Argument paragraphs were marked as whole `<p>` elements whose normalised text opens "argument" — the correction Round 2 had to make after its own detector swallowed a letter body.

For Possidius I normalised `possidius_vita-augustini_weiskotten1919.txt` with de-hyphenation across line breaks, which is what defeated two previous rounds.

**Sweep.** Every quoted string of 20+ characters in the seven chunks and Doc_09 — 190 candidates — matched against the corpus. **Zero resolved into a `<note>` span. Zero resolved into an ANF *Argument*** (the one Argument string in the repository is `lpcstory004`'s, quoted in order to exclude it, and it failed my matcher only because the chunk's own ellipsis is inside the quotation marks). Pontius's *Life* carries no Argument paragraph at all, which independently rules out the apparatus trap for `lpcstory001`, `002` and `006`.

**Generator.** Read line by line, re-derived the index (**byte-for-byte identical** to the committed file), then forced all thirteen halting sites and ran four non-halting probes designed to find what no guard catches.

**Closure audit.** All 27 Round 1 findings and all 33 Round 2 findings checked at **every site the reviewer named**, not the site quoted first.

**What I tested hardest,** in order: (1) the `lpcstory003` Do-Not-Retrieve claim, once I saw that a correction notice sat on it; (2) the halting-site count, because the brief asserted it; (3) `lpcstory002`'s rebuilt Tier-1 argument against CF Part II read whole; (4) the five new Absent Story Notes, claim by claim, against the sources they assert silence about; (5) `lpcstory007`'s new "stays at Documented" passage against CF line 253.

---

# Job 1 — is the closure claim true this time?

`lpc_Decision_Log.md`, 2026-09-15 (Doc_09 Round 2): *"**All 27 are now closed, audited item by item rather than asserted.**"*

**It is much closer to true than last time, and it is still not true.** Nineteen of Round 1's twenty-seven are fully closed at every site. **Eight are open or partial**, and **five of those eight are open at a second site the Round 1 reviewer named in the finding itself**:

| Round 1 finding | Status at the live text |
|---|---|
| H1, H2 | **Closed.** Verified independently against Pontius §10 and *Epp.* XX/XXI body text. |
| M1, M2, M4(a), M4(c), M4(d), M4(e), M5, M7, M8 | **Closed.** M4(e) and M8 verified by execution / by reading CF whole. |
| M3 | Closed for the wrong citation; **L16's half is open** — *Ep.* LI was also removed and Round 1 had verified LI as sound. |
| **M4(b)** | **Partial.** Title and Confidence added; **Gravities and Source are still not compared**, while the masthead claims "the agreement between each chunk and Doc_09 §3's own table." Proved by mutation (M6). |
| **M6** | **Partial.** §2 amended; **Doc_09's own Disposition still files the pre-amendment escalation** (M3), and the Doc_02 §9 item 10 departure is still unnamed. |
| **L1** | **Not closed — replaced with a stronger false claim.** See HIGH-1. |
| **L5** | **Partial.** `lpcstory007` fixed; **Doc_09 §4 still prints "we who were present."** Round 1 named both sites; Round 2 named both sites again. |
| **L7** | **Partial.** Doc_09 §4 now says "Four"; **`lpc_Story_Index.md` §3 still says "two."** Round 1 named both sites. |
| **L8** | **Partial.** Five notes added — but `lpcstory007`, which Round 1 named explicitly, got none, and the new boilerplate asserts it needs none. No guard added. |
| **L11** | **Partial.** Count is now derived, and the derived count is wrong. |
| L2, L3, L4, L6, L9, L10, L12, C1, C2, C3, C5 | **Closed.** |
| **C4** | **Not closed.** |

**On Round 2's own 33:** M2, M3, M4, M5, M6, M8, M11 and L2–L4, L6, L9, L10, L12, L13, C1–C3, C5 are closed. **M7 and M9 are partial, M10 and L1, L16, L17, L18, C4 are untouched, and L14/L15 are partial.** Round 2's M8 in particular is *genuinely and fully fixed* — I reproduced its exact scenario (`**1.** Heading`) and §5 now renders identically and correctly, which is the cleanest repair in this pass.

**Why this still matters.** The Round 2 entry corrects a false closure claim and then makes a narrower version of the same claim. The five second-site failures are all of one shape: *the reviewer named two sites, the pass fixed the one it quoted first.* That is the shape the Decision Log's own entry names as "the one-site-fix shape this build keeps producing" — in the entry recording that it had been fixed.

---

# HIGH

### HIGH-1 — `lpcstory003` asserts a silence *Ep.* XXXIV contradicts in the same sentence the chunk quotes, and the assertion is the Round 2 fix pass's own replacement for the wording Round 1 flagged

**Site:** `Story-Chunks/lpcstory003_numidicus.md`, `Do-Not-Retrieve-When` field.

**What I found.** The field reads:

> Not for questions about the lapsed — ***Ep.* XXXIV is about a confessor's ordination and says nothing of them**, so the story has nothing to offer there. **[CORRECTED, 2026-09-15 — Round 1's L1:** this read *"which this story deliberately does not address,"* implying a choice the letter never made.**]**

*Ep.* XXXIV, body text, `iv.iv.xxxiv-p5`:

> "But the reason of his remaining behind, as we see, was this: **that the Lord might add him to our clergy, and might adorn with glorious priests the number of our presbyters that had been desolated by the lapse of some.**"

**The chunk's own Story Text quotes the first half of that sentence** — *"that the Lord might add him to our clergy"* — as its closing line, and stops one clause short of the lapse. The letter does not merely mention the lapsed in passing: **the lapse is the stated reason the vacancy existed**, which is the whole logic of the appointment the letter announces.

Round 1's L1 had already quoted this clause and supplied the fix verbatim: *"this story is about a confessor, not about the lapsed, **though the letter names the lapse as the vacancy's cause**."* The fix pass wrote the negation of the clause Round 1 supplied, and attached a notice certifying the finding closed.

**Why this matters.** Three reasons, in order of weight.

1. **It is a false statement about what a source does not contain** — the exact defect class of Round 1's H1, which this build graded HIGH and treated as its defining failure mode. A build that has just spent a round fixing an asserted silence in Pontius §10 has written a new one into the letter two chunks over.
2. **It is retrieval-control instruction, not commentary.** It tells the retrieval layer to withhold this story from every participant question about the lapsed, *on a false premise about the source*. A participant asking how this world dealt institutionally with the lapse would be steered away from the one letter in which the lapse produces an ordination — a G2/G6 connection this repository has nowhere else.
3. **The `[CORRECTED …]` notice makes it invisible to the next pass.** A reader auditing L1 sees a closure notice and moves on. That is how the site survived Round 2 as well.

**Confirmed three ways.** (a) My harness resolves the clause to `iv.iv.xxxiv-p5`, a body paragraph, Argument flag false — Ep. XXXIV's Argument is the separate paragraph `p4` ("Argument.—Cyprian Tells the Clergy and People that Numidicus Has Been Ordained by Him Presbyter"), which is precisely the paragraph whose boundary defeated Round 2's first detector, so I checked it by element rather than by heuristic. (b) I printed the raw XML around offset 352581 and read the `<note>` boundaries directly: the clause sits inside `<p id="iv.iv.xxxiv-p5">`, between two `<note>` elements and inside neither. (c) It is the continuation of a sentence the chunk itself quotes, so no search was needed to place it in the chunk's own cited range.

**Fix.** One line. Adopt Round 1's own wording: *"Not for questions about the lapsed as such — this story is about a confessor's ordination, though the letter names the lapse of some as the cause of the vacancy he fills, and a participant asking how the lapse reshaped the clergy may be pointed here for that."* Then re-sweep `lpcstory003` for any other negative claim about *Ep.* XXXIV, and re-read the letter whole before writing the replacement — the defect came from reading to the clause the chunk needed and stopping.

---

# MEDIUM

### M1 — the closure claim is false again, and five of the eight gaps are at second sites the reviewer named in the finding

**Site:** `lpc_Decision_Log.md`, 2026-09-15 (Doc_09 Round 2) entry; inherited by Doc_09's Disposition by reference.

**What I found.** Set out in the Job 1 table above. Nineteen fully closed, eight open or partial. The eight: M4(b), M6, L1, L5, L7, L8, L11, C4. Five of them (M3/L16, L5, L7, L8, M4(b)) are sites the finding text itself named and the pass did not visit.

**Why this matters.** The entry's own narrative is scrupulous about *what it did* — it names the heap, the "to be rescued," the polarity class, the trimmed CF sentence. The completeness claim on top is what fails, for the second round running, in the entry that corrects the first one. The cost is concrete: I had to re-derive the ledger from scratch, as Round 2 did, which is the time that should have gone into the new prose.

**Fix.** Replace the blanket claim with the per-finding ledger Round 2 asked for — applied / declined with reason / deferred. A build thread may decline a LOW. It may not record a decline as an application, and it may not record a one-site fix as a closure.

### M2 — Doc_09's own Status, Document Log and Disposition are frozen at Round 1; the set's two files now contradict each other about whether the set has been reviewed

**Site:** `Doc_09_Story_Inventory.md` Status line (l. 5), Document Log, Disposition (l. 148).

**What I found.** Doc_09 still reads **"Status: DRAFT — not reviewed, not self-disposed."** Its Document Log has three rows and ends at "Round 1 fix pass — this revision … REVISED — unreviewed." Its Disposition says **"REVISED after Round 1; the revision is unreviewed,"** and recites Round 1's counts (2 HIGH, 8 MEDIUM, 12 LOW, 5 COSMETIC) as the current state, including the paragraph beginning "Both HIGH findings are claims this document made *about* its sources" — both of which are now closed.

`lpc_Story_Index.md`, derived, says **"REVISED after Round 2 … Two round(s) — Round 1, Round 2."**

**Why this matters.** This is Round 2's M2 with the files swapped. M2 was: *the index says no review has been run, and it is a hard-coded literal in a file whose own masthead warns that hard-coded prose is re-verified by nothing.* The fix derived the index's status from `Review-Artifacts/` — and left the same claim standing, hand-written, **in the document the index is a companion to**. The Round 2 fix pass edited Doc_09 in four places (§2, §4, §6, §8) and did not touch its own status block. The two files are "reviewed and disposed of together" by the index's own statement, and they now disagree about whether a review happened.

**Fix.** Update Doc_09's Status, add the two missing Document Log rows (Round 2 review; Round 2 fix pass), and rewrite the Disposition's first three paragraphs against Round 2's result rather than Round 1's.

### M3 — Doc_09's Disposition files the CO-022 escalation in exactly the form §2 retracted, two pages earlier in the same document

**Site:** `Doc_09_Story_Inventory.md`, Disposition, CO-022 paragraph, *Governance or methodology*.

**What I found.** §2, amended at Round 2, now says:

> An earlier version of this paragraph said CF *"does not state how to tier a source that satisfies one tier's author test and another's genre test simultaneously."* **That overstated the gap** … **So CF does supply a route** … **That narrower question is what is escalated.**

The Disposition, unamended, still says:

> **New:** *"a source is not a tier"* — the rule §2 adopts for a source that satisfies Tier 1's author test and Tier 3's genre test at once (Pontius). **CF V7.4 does not state it**, and it would govern how every world in the portfolio tiers an eyewitness hagiographer.

**Why this matters.** The Disposition is the escalation's filing. It is what a project lead reads when deciding. Round 2's M9 held that the escalation "as filed, is raised against a Framework text the document itself has trimmed at the deciding point," and asked that CF line 253 be shown whole **before it is ruled on**. §2 was repaired; the filing was not. This is Round 1's M7 shape — a retracted claim left standing at a second site — occurring *inside one document* rather than across two.

The Disposition's *Portfolio-level* bullet has the same problem in milder form: it files the polarity-blind row derivation as a live defect ("*without regard to polarity*"), which is fixed. What remains live is the defect **class**, which is a different and stronger filing.

**Fix.** Rewrite the Disposition's CO-022 paragraph against §2's amended text and Round 2's M9, and recast the portfolio item as the class rather than the instance.

### M4 — the self-counted halting-guard figure is wrong, contradicts its own sentence, and is already in the Decision Log

**Site:** `scripts/gen_story_index.py` l. 234; `lpc_Story_Index.md` masthead; `lpc_Decision_Log.md` Round 2 entry, Status paragraph.

**What I found.**

```python
_NHALT = pathlib.Path(__file__).read_text(encoding="utf-8").count("sys.exit(")
```

That counts occurrences of the *string* `sys.exit(` in the file — **including the one on its own line**. The index therefore prints "**14 of them, counted off this script rather than typed**," and the correction notice **in the same sentence** says "**the script has thirteen halting sites**." Thirteen is right. The Decision Log's Status paragraph has already copied the wrong one: "**Fourteen halting guards, counted off the script rather than typed**, after three rounds across two generators of that number being copied forward and going stale."

**Confirmed three ways.** `grep -n "sys\.exit("` → 14 lines, one of which is l. 234. An `ast` walk for `Call` nodes on `sys.exit` → **13**, at lines 46, 50, 68, 76, 78, 82, 84, 93, 124, 163, 169, 184, 202. Exhaustive forcing → I produced **13 distinct FATAL messages** from thirteen separate mutated copies; there is no fourteenth to force.

**Why this matters.** The script's own comment above the line says the count "has been misstated in three consecutive rounds across two generators, always by being copied forward into the Decision Log and then into the next round's brief." The fix reproduced the failure on its first run, propagated it to the Decision Log, and it reached this review's brief. **The remedy was right and the implementation was not: deriving a number from the script's own text is not deriving it from the thing counted.** A self-referential textual count is a literal wearing a derivation's clothes — and this one is *worse* than the literal it replaced, because the prose beside it is right and the derivation is wrong, so a reader cannot tell which to believe.

**Fix.** Count the call sites, not the characters: `len([n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Call) and getattr(n.func, "attr", None) == "exit"])`, or simply drop the number and state the conditions. Correct the Decision Log.

### M5 — Doc_09 §4 still prints a quotation that occurs zero times in Possidius, in the audit row whose finding is "Every detail is his"

**Site:** `Doc_09_Story_Inventory.md` §4, No-Tier-5 audit, `lpcstory007` row (l. 80).

**What I found.** The row reads:

> | `lpcstory007` | 1 | Possidius was present — *"we who were present,"* *"in our presence."* Every detail is his. |

**"we who were present" occurs zero times in the Weiskotten text.** Possidius writes "he **asked of us** who were present" (one occurrence). "in our presence" occurs twice and is exact. `lpcstory007` was corrected; §4 was not.

**Confirmed** by normalised search with de-hyphenation over the whole bilingual file — the same normalisation that resolves the page-142/143 break that has produced false negatives in two rounds — and by printing the surrounding 600 characters.

**Why this matters.** Round 1's L5 named both sites. Round 2's L5 named both sites and pointed at this one specifically: *"it sits in the §4 row whose text is 'Every detail is his.'"* Twice named, twice missed. The substance is small — Possidius is among those present either way, and "while we stood by and watched and prayed" is exact and is in the chunk — but a fabricated quotation inside the table that certifies nothing was fabricated is the wrong place for it.

**Fix.** Replace with *"of us who were present," "in our presence."*

### M6 — the gravity derivation discards the chunks' own gravity declarations in two of seven files, and is right only by accident; §3's Gravities and Source columns are never compared though the masthead says the table is

**Site:** `scripts/gen_story_index.py` ll. 109–120 and l. 229; `lpc_Story_Index.md` §1.

**What I found, by execution.** Round 2's M7 asked for the gravity scan to be clause-split and polarity-aware **and** cross-checked against Doc_09 §3's Gravities column. The first half was done. The result is that in `lpcstory002` and `lpcstory007`, the **Formation Ecology Connection's own gravity line is discarded by the negation filter** and the correct answer survives only because the Retrieve-When front-matter happens to repeat it.

`lpcstory007`'s declaration is:

> `**Gravities: G2 (Penitential Discipline), G1 (Pastoral Office).** Doc_04 finds that G2 does not persist into the second phase under its own name…`

The sentence splitter is `(?<=[.;])\s+|\n`. The period before `**` is not followed by whitespace, so the split never happens; the declaration and the "does not persist" clause stay one clause; `NEG_CLAUSE` matches; **the whole clause including `G2` and `G1` is dropped.** `lpcstory002` fails identically on "the one force in this world's whole matrix that connects to no other."

**Reproduced.** I rewrote `lpcstory007`'s Retrieve-When to name the same two gravities in words instead of codes — a change the L4 template permits, since it never requires gravity codes in Retrieve-When — and re-ran. The Master Story Table printed **`—`** for `lpcstory007`'s gravities. **No guard fired.** Doc_09 §3's own Gravities column, which says `G1, G2`, was never consulted.

Two further probes, both emitting cleanly with no halt:

- Changing Doc_09 §3's Gravities cell for `lpcstory005` from `G2, G8` to `G5, G7` — **rc 0**. The index prints the chunk's gravities; the table's are never compared.
- Changing Doc_09 §3's Source cell for `lpcstory003` from `(row 1)` to `(row 28)` — the Excluded Scillitan row — **rc 0**. §3's Source column is not parsed at all.

**Why this matters.** The masthead asserts, as derived and re-checked on every run, "**the agreement between each chunk and Doc_09 §3's own table**." Four of the table's seven columns are checked; three are not. Round 1's M4(b) was exactly this — *"only the TIER column was compared, though the masthead claimed the whole table"* — and Round 2's L15 restated it. The fix widened the check by two columns and did not narrow the claim.

And the gravity derivation is now a harder kind of wrong than the polarity-blind version it replaced: the polarity-blind version over-reported visibly; this one **silently discards the chunk's authoritative statement** and substitutes an incidental one, so the output can be correct while the derivation is broken.

**Fix.** Read gravities from the Formation Ecology Connection's own `**Gravities:** …` line by a dedicated pattern rather than by scraping the whole body; cross-check against Doc_09 §3's Gravities column and halt on disagreement; parse §3's Source column for row numbers and run it through the same Registry check. Then narrow the masthead to what is actually compared.

### M7 — the Absent Story Note rollout skips the chunk Round 1 named, asserts it has nothing to name, and puts a build-progress item in the section reserved for evidentiary absence

**Site:** `Story-Chunks/lpcstory006`, `lpcstory007`; the `[ADDED … Round 1's L8]` boilerplate in `lpcstory002`–`006`.

**What I found.** Round 1's L8 named four chunks that already carried Absent Story Note material inside other sections: *"002's missing ending, 003's 'the wife's own view… not recoverable', 005's 'the sister does not speak', **007's 'no second account of Augustine's death exists in this corpus'**."*

The fix pass added notes to **002, 003, 004, 005 and 006** — and skipped 007. The boilerplate it repeated in all five says:

> Five now do; `lpcstory001` and **`lpcstory007` do not, because neither has an expected-but-unsupported story attached to it.**

`lpcstory007`'s own Tier Justification says: *"The ordinary corrective — check the detail against another witness — is unavailable: **no second account of Augustine's death exists in this corpus.**"* That is the template's category exactly — *"what is missing, why it is missing (source loss, survivorship gap, transmission thinness)."* The chunk contains the material, in the section Round 1 said to move it out of, under a notice asserting it has none.

**Second half.** `lpcstory006`'s new note is about the *Acta Proconsularia* — a source that is **vendored, Native, and unopened**. The note says so itself: *"That is not a gap in the evidence; **it is a gap in this build's reading**."* The template's own definition is *"where a story that might be expected cannot be told **because evidence is insufficient**"* — and its three named causes are source loss, survivorship gap and transmission thinness. None applies. By its own sentence the note disqualifies itself from the section it is in. It is an open item, and Doc_09 §8 item 1 and §6 item 2 already carry it twice.

**Why this matters.** The Absent Story Note is the chunk-level expression of Article 20's affirmative duty and of CF's "silence in thin areas is the right response." Filling it with a reading-backlog note converts an evidentiary discipline into a progress report, and the one chunk that has a genuine unfillable absence is the one told it has none. The generator has no guard for the section — Round 1's L8 asked for one and it was not added — so nothing catches either half.

**Fix.** Give `lpcstory007` a note built from its own Tier Justification sentence, and correct the boilerplate. Move `lpcstory006`'s *Acta* material to its Tier Justification (which already makes the point) and either omit its note or write the real absence: *what a bystander saw* is unrecoverable from a source written in praise, which is a genuine evidentiary absence rather than a reading task. Add the guard: a chunk whose Tier Justification or Usage Guidance contains an unfillable-absence claim and has no Absent Story Note should at least be reported.

### M8 — `lpcstory005`'s new Absent Story Note asserts a silence the letter's own wording puts in doubt, and Doc_09 §7 item 3 overlooks two named lapsed women in the letter it cites

**Site:** `Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md`, Absent Story Note; `Doc_09_Story_Inventory.md` §7 item 3.

**What I found.** The note says: *"**The sister has no story, and she is the person this one is about.** **She is named by no source, including her brother's letter.**"*

*Ep.* XX §2, four sentences after "the (spiritual) death of **my sister**", reads:

> "…that you will grieve with all the rest for **our sisters whom you also knew well—that is, Numeria and Candida**,—for whose sin, because they have us as brethren, we ought to keep watch."

and §3: *"should remit such a great sin to **those our sisters, Numeria and Candida**."* Lucian's reply opens *"you told us concerning **our sisters**."* The ANF *Argument* over the letter — editorial, and correctly not used by this build — reads the two as Celerinus's own: *"Celerinus, on Behalf of His **Lapsed Sisters** at Rome."*

The chunk's reading (the sister is a third, unnamed woman; "our sisters" is fraternal usage) is defensible and may well be right. **What is not defensible is stating the negative flatly, in a section whose whole purpose is honest calibration, when the letter uses the same word for two named women in the next sentence.** This is the H1 class in its milder form: an unhedged assertion about what a source does not contain, written fast into an unreviewed section.

**Second half, and it is the sharper one.** Doc_09 §7 item 3 says: *"Celerinus's sister … is the closest this corpus comes to **a named lapsed person with a history**."* She is not named. **Numeria and Candida are** — named, lapsed (Numeria at least), with works recorded ("ministered to sixty-five"), with Candida's own defence reported ("she gave gifts for herself that she might not sacrifice… I know, therefore, that she has not sacrificed"), and with an adjudication on record ("the chief rulers commanded them in the meantime to remain as they are, until a bishop should be appointed"). An unnamed woman cannot be closer to "named" than two named ones. The stronger example was inside the chunk §7 cites.

Item 3's **core** claim survives and I want that said plainly: no lapsed person in this corpus writes in their own hand, and everything about Numeria and Candida reaches us through Celerinus and Lucian. The absence is real. The illustration chosen for it is the weaker of the two available.

**Fix.** Hedge the chunk: *"Her name is not given in the letter. Celerinus calls Numeria and Candida 'our sisters' a few lines later, and whether that is kinship or fraternal usage — and so whether the sister is one of them — this build does not settle."* Rewrite §7 item 3 around Numeria and Candida, keeping the finding: they are named, lapsed, weighed and dispatched, and not one word of theirs survives.

### M9 — the narrowed escalation is still wider than CF requires: CF's own confidence ceiling decides `lpcstory006`

**Site:** `Doc_09_Story_Inventory.md` §2, the `[ADDED … AMENDED at Round 2]` paragraph.

**What I found.** §2 now escalates the narrower question: *"where the genre shaping reaches the events themselves rather than the author's estimate of his subject, as at `lpcstory006`."* That is a real improvement on what Round 2 found. **But CF decides `lpcstory006` too, by a route §2 does not notice.**

CF line 253 caps in-Tier-1 confidence stepping at **Contested**: *"May carry Widely Accepted or **Contested** confidence for specific details."* CF line 261 gives Tier 3 the band **"Contested for the general portrait or attribution; Inferential/Thin for specific details shaped by hagiographic convention."**

`lpcstory006`'s own Confidence field is **"Contested for the portrait; Inferential/Thin for details shaped by convention"** — Tier 3's band, verbatim, and **a band Tier 1 cannot reach**. So on CF's own text, once the build judges those details Inferential/Thin, Tier 3 is the only tier whose confidence range accommodates them. The tier follows from the band the build has already assigned.

**Why this matters.** The escalation as filed asks the project lead to rule on something CF's band structure already answers, and that weakens the filing at precisely the point Round 2 said to strengthen it. What genuinely remains novel in "a source is not a tier" is narrower still and worth ruling on: **whether one source may be split across tiers story by story at all** — which is a rule about the *unit of classification*, not about genre. CF's Part II classifies stories and never states that a source's tier is uniform; the build's rule is a reasonable reading of that silence, and that is what should be put to the lead.

**One further gap, related.** `lpcstory006`'s Tier Justification argues Tier 3 entirely from CF's three hagiography markers and never engages CF's Tier 3 **genus** sentence — *"Material attributed to specific figures or moments but resting on **collected tradition rather than direct documentation**."* Pontius is direct documentation by an eyewitness, so `lpcstory006` fails Tier 3's opening requirement. Naming that, and answering it, would make the escalation much sharper: it is the real tension, and both `lpcstory002`'s and `lpcstory006`'s arguments walk past it.

**Fix.** Recast §2's escalation around the unit-of-classification question; note CF's band ceiling as the CF-native route for `lpcstory006`; and have `lpcstory006` address CF's genus clause rather than only its markers. Then amend the Disposition to match (M3).

### M10 — Round 2's M10 is untouched: a 90-word build-process notice still sits inside `lpcstory002`'s deployable Story Text

**Site:** `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md`, `## Story Text`.

**What I found.** Unchanged. The Story Text still contains **four** `[CORRECTED …]` notices — more than any other chunk's Story Text, all six of which have none — still opens its new paragraph with **"And Pontius does say what followed,"** a sentence addressed to a reviewer rather than a reader, and still ends the narrative on a build-process block rather than on Pontius.

The L4 template's Final Assembly Instruction 3 is directly on point: *"does this story announce its epistemic status through the way it is told, or does it require an external disclaimer? **The tier register should be built into the telling, not added as a footnote.**"*

**Why this matters.** Story Text is the layer a Representative retrieves and speaks from. Every other section of the chunk is builder-facing. Round 2 graded this MEDIUM and asked for the notice to move to the Tier Justification, which already carries the parallel H1 notice. Nothing moved.

**Fix.** As Round 2: move the notices to the Tier Justification, and let the paragraph read forward from the sermon — the Tobias comparison is a natural close.

---

# LOW

**L1 — the five new Absent Story Notes render as HTML headings, not as prose above a rule.** In `lpcstory002`–`006`, the `[ADDED … L8]` boilerplate line is immediately followed by `---` with no blank line. That is a setext H2 underline: the notice is promoted to a section heading at the same level as "Absent Story Note" and "Usage Guidance," and the intended horizontal rule disappears. Confirmed by rendering each file with a CommonMark-conformant renderer rather than by eye. *Fix:* blank line before each `---`.

**L2 — the Absent Story Note is placed before Usage Guidance in all five chunks; the template puts it after.** Template order is Story Text → Formation Ecology Connection → Tier Justification → Usage Guidance → Source Identification (Tier 4 only) → Absent Story Note. *Fix:* move, or record the deviation.

**L3 — Doc_09 §2's Tier 2 confidence line trims CF without ellipsis — the third bullet to do this, and the first time at this one.** CF line 257: *"Widely Accepted to Dominant Modern Reconstruction. **The tradition is authentic; specific details and attributions carry Contested confidence.**"* §2 prints the first sentence only, unmarked, under a header asserting "the confidence bands are its own too." Round 1's C1 caught the Tier 3 trim, Round 2's M9 the Tier 1 trim; both were fixed and this one was never looked at. It has a live consequence: the generator's `BANDS` table inherits the truncation, so `BANDS["2"]` omits Contested and would halt on a Tier 2 chunk whose Confidence follows CF exactly. `BANDS["1"]` has the same gap. *Fix:* restore the sentence; widen `BANDS` to CF's full per-tier ranges.

**L4 — Round 1's L7 second site: `lpc_Story_Index.md` §3 still says "§6 records **two** candidates declined."** Doc_09 §4 now says "**Four**," corrected with a notice. The index is generated, so the string lives at `gen_story_index.py` l. 290. *Fix:* change to four, or name which two.

**L5 — Round 2's L16 open: *Ep.* LI was dropped without a reason and `lpcstory001` now rests on one locus.** The notice explains why *Ep.* XXXIII went; it says nothing about LI, which Round 1 verified as sound corroboration ("by the suffrage of the people who were then present"). *Fix:* restore LI or XXXII, or state why one locus suffices.

**L6 — Round 2's L17 open: "Tobias, who **buried** the dead of 'his own race only.'"** Pontius: *"Tobias **collected together those who were slain by the king and cast out**, of his own race only."* The gloss is outside the quotation marks but attributed to Pontius's sentence. *Fix:* "who gathered the dead of 'his own race only.'"

**L7 — Round 2's L18 open: *Ep.* LXVII is described twice as "Cyprian's own letter."** It is synodical — Cyprian and thirty-six named colleagues. Not the intra-corpus misattribution failure mode, and naming it correctly makes the corroboration *stronger*: "by the suffrage of the whole brotherhood" is then a synod attesting a practice, not one bishop asserting it. In a chunk set where `lpcstory005` makes attribution discipline a section of its own, this should be named. *Fix:* "a letter of Cyprian and thirty-six colleagues in council."

**L8 — Round 2's L15 open in its main clause: the masthead still overclaims the §3 cross-check.** Covered under M6; recorded here as the carried finding. Also unresolved: Doc_09 §3 still gives `lpcstory006` the bare "Contested" where the chunk carries the full Tier 3 clause, a divergence the new check tolerates by design (`cconf.split(";")[0]`) rather than closes.

**L9 — Round 2's M9's third sub-request is still open: the departure from Doc_02 §9 item 10 is unnamed.** Doc_02 §9 item 10 reads: *"Pontius's *Life* is described there in terms matching the Framework's own **Tier 3** definition without being so labeled."* Doc_09 assigns Pontius Tier 1 for three of the four stories drawn from him. Doc_09 cites §9 item 10 twice — header and §8 item 3 — for the provisional-inventory fact only. The reversal is nowhere named. *Fix:* name it in §2, where the per-story rule is stated.

**L10 — `lpcstory006`'s Tier 3 argument never engages CF's Tier 3 genus clause.** Detailed under M9; recorded separately because it is a chunk-level gap, not an escalation-level one.

**L11 — the review-history derivation keys on the existence of a review artifact, not on a fix pass.** `ART.glob("Doc09_Round*_Review.md")` drives both the Status line and the Disposition's "**this file is the Round N fix pass**." The moment this review lands, re-running the generator will emit "REVISED after Round 3 … this file is the Round 3 fix pass and is unreviewed," whether or not any fix pass has run. The remedy for a stale literal has produced a claim that can be true only by coincidence. *Fix:* derive the round count from the artifacts (correct) and the *fix-pass* claim from something the fix pass sets — a marker in Doc_09's Document Log, which the script already reads.

**L12 — the confidence-band check is substring-based.** `any(b in s["conf"] …)` means a Tier 1 chunk declaring **"Not Documented"** passes the band guard. Reproduced: rc 0, and the index prints "**Yes** — Not Documented" in the No-Tier-5 audit. *Fix:* match on a normalised band token rather than a substring.

---

# COSMETIC

**C1 —** `lpc_Story_Index.md` §1's Confidence cell for `lpcstory006` still carries the full clause, making the master table unscannable at the one row a reader most wants to scan. Round 1's C4, unaddressed twice.

**C2 —** Doc_09 §8 item 2's placeholder is justified as *"Kept as a numbered placeholder so the list's own cross-references do not shift."* **Nothing in the world build cross-references Doc_09 §8 by item number** — I grepped every `.md` outside `Review-Artifacts/`. The placeholder is harmless; the reason given for it is not a fact.

**C3 —** The same 62-word `[ADDED … Round 1's L8]` boilerplate is repeated verbatim in five chunks, including the sentence that is wrong about `lpcstory007` (M7). One statement of a rollout decision belongs in Doc_09 or the Decision Log, not five times in the deliverable.

**C4 —** Doc_09 §3.1's Tier 4 quotation closes with the period inside the quotation marks at *"(particularly ecological reconstruction sections)."*, dropping CF's governing continuation *"when it is explicitly marked as reconstruction in the construction notes."* Same class as L3.

**C5 —** `gen_story_index.py` declares `global BANDS` inside the chunk loop and rebuilds the dict on every iteration; `BANDS` is undefined if the loop body never runs, and is reached at l. 284 only because l. 124 exits first. Move it to module scope.

---

# Is the deliverable adequate to proceed to Doc_10?

**Yes — after a short fix pass, and the fix list is shorter than the finding count suggests.**

What holds, stated at the strength it has:

- **The repository is not composited, verified independently for the third time and by a harness built from scratch.** Every quotation in the seven chunks and Doc_09 resolves to body text of the cited work. **Zero inside a `<note>`. Zero inside an ANF *Argument*** except `lpcstory004`'s deliberate exclusion quotation. Pontius's *Life* carries no Argument paragraph at all, which closes that question for three chunks structurally rather than by search.
- **The two documented failure modes are avoided, and the build's own claims about them are true.** `lpcstory004`'s Argument/body distinction is exact — the figure is at `iv.iv.lix-p4` (Argument) and at **§3, `iv.iv.lix-p12`** (body), and the chunk's claim to cite §3 is correct. `lpcstory005`'s attributions are right, and so is the harder one I checked because it could have been wrong: *Ep.* XXII **is** Cyprian's own letter, as the chunk says.
- **The tier work survives the hardest tests I could put to it.** `lpcstory002`'s rebuilt Tier 1 warrant now names the idealized portrait, quotes it accurately from §9 and §10, and holds the tier on CF's own per-detail confidence rule. That argument is sound: CF's Tier 3 genus is "resting on collected tradition rather than direct documentation," and Pontius is direct documentation; the concession does not defeat the tier, and the step to Widely Accepted follows from CF line 253. **Round 1's M8 / Round 2's M11 is genuinely closed**: the new `lpcstory007` passage answers the asymmetry by keying the band to the author's access *to the disputed content* — reconstructed speech versus observed furniture — which is CF's own variable, and it explicitly disclaims corroboration as the operative test in both directions. I went looking for a hole in that and did not find one.
- **The generator reproduces byte-for-byte, and all thirteen halting sites fire**, each with its own message, each forced from a fresh copy. Round 2's M8 is fully repaired — the alternative Markdown enumeration now renders identically.
- **The five new Absent Story Notes are mostly accurate.** I checked their assertions of silence at source: `lpcstory004`'s "no source says whether the captives were recovered" holds — "barbarian" occurs nowhere else in the corpus body outside *Ep.* LIX. `lpcstory002`'s "no Christian outside Pontius describes the operation" holds — *De mortalitate* §16 poses relief as a moral test-question ("whether they who are in health tend the sick") and never reports the operation. `lpcstory003`'s holds exactly: all three facts are in one paragraph, `iv.iv.xxxiv-p5`.

**What I would not carry into Doc_10 unfixed is HIGH-1**, for the reason Round 1 gave about its own H1: it is a false statement about a source sitting in a field that governs what the Representative is allowed to reach for, and Doc_10 will inherit it. It is a one-line fix.

**M2 and M3 are the second priority** — not because either is dangerous, but because Doc_09's own front and back matter is what a reader consults to learn the set's state, and it currently says the set has never been reviewed and files an escalation the document itself has withdrawn.

Nothing in this review requires re-selecting a story, re-reading a source (except the seven lines of *Ep.* XXXIV around the lapse clause), or rewriting a Story Text.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** No identity, title or voice decision is made here. Noted separately and not as an escalation: `lpcstory003`'s Do-Not-Retrieve rule is a deployable retrieval instruction resting on a false claim about its source (HIGH-1), and `lpcstory002`'s deployable Story Text still carries build apparatus (M10). Both are content defects inside this document's own gift to fix.

- **Portfolio-level or cross-world — TWO items, both inherited, and the second now has a third instance.**
  1. *The corpus-wide editorial-apparatus item.* Re-verified independently a third time and still the ledger's first **positive** instance: zero chunk quotations resolve inside an *Argument*, and the one that does is quoted in order to be excluded. Carry forward unchanged.
  2. *The index-generator-as-build-artifact item (Doc_08 Round 5; Round 1's M4c; Round 2's M7).* **A third instance, and it is a new sub-class worth naming separately.** The first two instances were *derivations that read the wrong thing*. This one is a derivation that reads **itself**: `count("sys.exit(")` over the script's own source, which counts its own counting expression and prints a number contradicted by the sentence beside it (M4). The lesson the fix was written to apply — "derive, never type" — was applied to a self-referential text scan, which is a literal in disguise. `gen_force_index.py` states the same lesson about the same class of number in its own masthead and will get the same treatment. **Route with the sub-class attached: a count derived from a script's own text is not derived from the thing counted.**
  Related and worth attaching: M6's demonstration that a negation filter shared by two derivations can be *correct for one and destructive for the other*, because the clause-splitter the filter depends on cannot split at `.**` — a Markdown-specific boundary every sibling world's chunks will also use.

- **Governance or methodology — open at six, and the sixth still needs amending before it is ruled on, for a second reason.** Round 2 asked that CF line 253 be shown whole before the project lead rules on "a source is not a tier." §2 now does that. **But two things still stand in the way of a clean ruling.** First, **the escalation as filed in Doc_09's own Disposition is the pre-amendment version** (M3), and the Disposition is the filing. Second, **the narrowed question is still wider than CF requires**: CF's Tier 1 confidence ceiling is Contested, `lpcstory006`'s own assigned band reaches Inferential/Thin, and only Tier 3's band goes there — so CF's band structure decides `lpcstory006` as well (M9). What is genuinely novel and worth a ruling is narrower: **whether a single source may be split across tiers story by story at all.** I add no seventh item; I ask that the sixth be re-filed as that question before it is ruled on.
  **One methodology question I raise rather than escalate**, repeating Round 2's: a fix pass has now twice recorded blanket closure of a finding list it had partly closed. The recurring mechanism is specific and fixable — *the pass visits the site the reviewer quoted and not the other sites the finding names.* A convention that a finding is closed only when every named site is visited would have caught L5, L7, L8, M3/L16 and M4(b) in this pass and four of the same class in the last.

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. §6 item 4 and §8 item 4 now state it accurately.

---

# Check confirmation — my own harnesses, including the one that was wrong

**Thirty-odd failing checks in this build have turned out to be defects in the check.** One of mine was, and it would have produced three fabricated HIGH findings against the three chunks the brief told me to spot-check. I record it first.

## Defective check of my own (caught before reporting)

**D1 — note-spanning false negatives: six quotations reported unmatched, all six present in the source.** My first sweep excluded `<note>` subtrees from the searchable text — correctly — and reported as missing:

- `lpcstory003`: "remained unwillingly from among the companions whom he himself had sent before."
- `lpcstory004`: "We have then sent you a sum of one hundred thousand sesterces, which have been collected here in the Church over which by the Lord's mercy we preside"
- `lpcstory004`: "wished us to be sharers in your anxiety, and in so great and necessary a work"
- `lpcstory005`: "in this day of paschal rejoicing, weeping day and night, have spent the days in tears, in sackcloth, and ashes"
- `lpcstory005`: "was so intolerable that nobody could bear it"
- `lpcstory005`: the eleven-name martyr list beginning "Bassus in the dungeon of the perjured"

**All six span a `<note>` anchor mid-sentence.** ANF interleaves note anchors inside clauses, so a quotation that crosses one is not contiguous even when the note's *content* is properly excluded. I caught it by printing the source paragraph for each miss and reading the joins by hand; every one closes exactly as the chunk prints it. Had I reported them, `lpcstory003`, `lpcstory004` and `lpcstory005` would each have taken a fabricated HIGH — against, in `lpcstory004`'s case, the chunk that documents its own sourcing discipline most carefully. **The remedy that works is to replace each note span with a boundary-preserving sentinel and search a flattened-with-separators body index, which is what the reported results rest on.** This is Round 1's D1/D2 and Round 2's D3 arriving by the same route a third time; it is the single most reliable way to fabricate a HIGH against this repository.

**D2 — a defective hypothesis, tested and discarded before it became a finding.** Reading `assert_coverage`, I concluded that its `DETECT` pattern would fire on an ordinary Markdown link — `[See also](url)` — and that the generator would therefore refuse to emit on legal Markdown. **I tested it instead of reporting it: it does not.** The `]` intervenes before the separator class, and the pattern requires the separator to follow the word sequence directly. `[NOTE, 2026: …]` does fire, correctly. Reported here as a defective check rather than as a finding, because reading a regex is not testing one.

**D3 — an unresolved difference in my own Argument detector, disclosed rather than buried.** My detector marks 94 Argument paragraphs across the volume; Round 2 reported 101 with a detector built the same way. I did not chase the difference, and I should say why I am comfortable reporting anyway: **no finding in this review depends on the count.** The two Argument paragraphs that matter are both detected and both verified by element — `iv.iv.xxxiv-p4` (HIGH-1's letter) and `iv.iv.lix-p4` (`lpcstory004`'s deliberate exclusion) — and the sweep's result is a negative (zero chunk quotations inside any Argument) that a *smaller* Argument set could only weaken, not strengthen, and which I additionally checked structurally for Pontius, whose *Life* has no Argument paragraph at all.

## Confirmations of the findings I did report

- **HIGH-1 confirmed three ways**, described in full at the finding: harness resolution to a body paragraph with the Argument flag false; a raw-XML read of the `<note>` boundaries around the clause; and the structural fact that the clause is the second half of a sentence the chunk itself quotes. I also read *Ep.* XXXIV whole, in five paragraphs, rather than searching it — an assertion of silence cannot be refuted by a search that returns nothing, and it can only be confirmed by reading.
- **M4 (the halting count) confirmed three ways** — `grep`, `ast` parse, and forcing all thirteen sites from thirteen separate fresh copies, each producing a distinct `FATAL`. I verified each mutation actually changed its file before running, which is the precaution Round 2 recorded after a mutation silently failed to apply in an earlier round.
- **M5 confirmed** by normalised search over the whole Weiskotten file with de-hyphenation across line breaks: "we who were present" → **0**; "asked of us who were present" → **1**; "in our presence" → **2**. The page-142/143 split that produced false negatives in two rounds was handled by the same normalisation and did not recur.
- **M6 confirmed by execution, not by reading code.** Three separate mutations applied to scratch copies and the emitted index inspected: the gravity cell went to `—` with no halt; a wrong Gravities cell in Doc_09 §3 emitted cleanly; an Excluded row in §3's Source cell emitted cleanly.
- **M7 and M8 confirmed at source.** The template's Absent Story Note definition and its three named causes read directly from `L4-Templates/Story_Repository_Chunk_Template.md`; *Ep.* XX and XXI read whole, in all seven body paragraphs, including the ANF *Argument* over XX, which I identified as editorial before using it as anything.
- **M9 confirmed against CF Part II read whole** at lines 249–271 of the plain text, not by keyword: Tier 1's confidence ceiling (line 253), Tier 3's band (line 261) and Tier 3's genus sentence (line 260).
- **L1 confirmed by rendering**, not by eye — each of the five chunks put through a CommonMark-conformant renderer, which produces `<h2>` for the boilerplate line in all five.
- **L3 and C4 confirmed** by diffing §2's and §3.1's quoted text against `cf74.txt` lines 252–269 character by character.
- **Registry claims confirmed** by reading rows 1, 7, 28, 41, 99, 122, 159, 171, 191, 192, 194, 204 directly. Doc_09 §5's Boundary Status table is correct in every cell, and §6 item 1's Perpetua ruling and §6 item 2's Latin-only *Acta* are both as stated.
- **The index re-derived byte-for-byte** before any mutation, and the derived §7 figures — five items, **641 words** — re-checked against the document.
- **`lpcstory002`'s `[CORRECTED]` claims about §9 and §10 confirmed** by reading both sections whole: the "pontiff of Christ… who excelled the pontiffs of the world" and "so excellent a priest" epithets are exactly where the chunk says, the Tobias comparison is in §10, and every quotation in the chunk is exact.

## The review brief's own premises, reported as directed

1. **"The masthead now reports 14 halting sites, self-counted. Reproduce them."** **There are thirteen.** The fourteenth is the string literal inside the counting expression (M4). The brief inherited the number from the index masthead and from the Decision Log's Status paragraph — which is the fourth consecutive round in which this figure has travelled from generated prose into the log and then into a review brief without being re-derived, and the first in which it did so *after* being made "derived."
2. **"The Round 2 fix pass claims all 27 are now closed, audited item by item."** The claim exists and is false, though far less so than last time: **19 fully closed, 8 open or partial**, against last round's 5/5/17.
3. **"Five new Absent Story Note sections were added to `lpcstory002`–`006`."** Accurate. What the brief could not know is that Round 1's L8 named **`lpcstory007`** as one of the four chunks carrying that material, and 007 received no note while 004 and 006 — neither of which Round 1 named — did (M7).
4. **"Spot-check `lpcstory003`'s Numidicus quotations."** Every one is exact, including the two that my own first harness reported missing. **The defect at `lpcstory003` was not in its quotations but in a prose claim about the letter** — which is where this build's defects have been living since Round 1, and is worth saying because the brief's spot-check list is a list of quotations.
5. **"Doc_09 §8 item 2 was replaced by a placeholder rather than deleted, to avoid shifting cross-references."** The placeholder is coherent and harmless; **the stated reason is not a fact.** No document in this world build cross-references Doc_09 §8 by item number (C2).
6. **"`lpcstory007` gained a new passage… Test that reasoning — it turns on the author's *access* to the disputed content."** Tested and it holds; Round 1's M8 and Round 2's M11 are closed. The passage is the best new prose in this pass.
7. **The brief's characterisation of the six generator changes is accurate.** One addition: the review-history derivation is keyed to the *existence of a review artifact*, so it will assert "this file is the Round 3 fix pass" as soon as this file is written, fix pass or not (L11).

---

# What would change my verdict

**Upward to MINOR REVISION, immediately:** correcting the one sentence in `lpcstory003`'s Do-Not-Retrieve field. Everything else I found is a second-site sweep, a generator patch, a status block and two paragraphs of escalation prose — none of it requires re-reading a source or re-selecting a story, and none of it would make a Representative say something untrue.

**Downward:** if a further pass through the chunks' new prose turned up a second asserted silence of HIGH-1's kind. I checked the five Absent Story Notes' silence claims at source and found one questionable (M8) and three sound; I did not exhaustively re-check every negative claim in every Tier Justification, and on this build's record that is where the next one would be.

**What I tested hardest and would defend:** the `lpcstory003` finding, the thirteen-versus-fourteen count, and the `lpcstory002` tier argument — the first two because they are checkable and I checked them three ways each, the third because I expected it to fail and it did not.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**1 HIGH · 10 MEDIUM · 12 LOW · 5 COSMETIC.**

The HIGH is one sentence, introduced by the Round 2 fix pass in the act of closing the finding about that sentence — which is now **four consecutive rounds in this build** (Doc_08's Rounds 2–4 and this one) in which the round's most serious finding was a defect the immediately preceding fix pass created. **The stories themselves are sound and have been verified clean three times by three independent harnesses.** The remaining work is a short, mechanical list, and a pass that visits *every* site each finding names — rather than the site it quotes first — should clear this at Round 4.

*Simulated review — informational only, not an Article 31 substitute.*
