# Doc_09 — Round 2 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-15 · **Round:** 2 · **Deliverables under review (four, together):** `Doc_09_Story_Inventory.md`; `Story-Chunks/` (`lpcstory001`–`lpcstory007`); `lpc_Story_Index.md`; `scripts/gen_story_index.py`.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**0 HIGH · 11 MEDIUM · 17 LOW · 5 COSMETIC.**

**Both of Round 1's HIGH findings are genuinely and verifiably closed, and I could not manufacture a third.** I rebuilt the Cyprian corpus from XML with `<note>` spans marked before stripping, re-swept every quoted string in all seven chunks, and re-read Pontius §§9–10, *Ep.* XX/XXI/XXXIII/XXXIV/LIX/LXVII and Possidius *Vita* XXVIII–XXXI at source. `lpcstory002` now reports what Pontius §10 actually says, quoted accurately. `lpcstory005`'s two quotations are restored character-exact, `(spiritual)` parenthesis included. `lpcstory001`'s re-citation to *Ep.* LXVII is correct in locus and wording. **The repository is still not composited**: 56 matched quoted strings, **zero** inside a `<note>`, **zero** inside an ANF *Argument* except the one `lpcstory004` quotes in order to exclude it.

**What holds this at SUBSTANTIAL is not a surviving HIGH. It is that the fix pass closed roughly a fifth of Round 1 and the build's own record says it closed all of it.** `lpc_Decision_Log.md`'s entry for this pass states **"All findings are addressed."** Of Round 1's twenty-seven findings, **five are fully closed, five are partially closed, and seventeen were not touched at all** — one MEDIUM (M8), eleven LOW, and all five COSMETIC. Four further defects were introduced or left behind by the corrective edits themselves, which is the pattern Doc_08's Rounds 2, 3, 4, 7 and 8 established and which I was directed to assume until checked. It is present, but in a milder form than in Doc_08: the new defects are glosses and bookkeeping, not fabrications.

**Adequate to proceed to Doc_10 — yes, and more clearly than at Round 1.** See the dedicated section.

---

# Method

**What I actually did, so the grading can be audited.**

1. **Built my own marked corpus.** Tokenised `cyprian.xml` element by element, tracking (a) the containing work from the `title=` attribute on `<div2>`/`<div3>`, (b) `<note>` nesting depth, and (c) the `<p>` element stack, producing a 1.58M-character body text in which every `<note>` span is replaced by **a single space** (never deleted — Round 1's D2) and every character carries its work and its paragraph id. I marked ANF *Argument* regions as **whole `<p>` elements whose text opens `Argument`** — 101 of them — after my first, heuristic detector proved wrong (see check-confirmation).

2. **Re-swept every quoted string in all seven chunks** by strict alternating-delimiter split after stripping correction notices, normalising `æ`/`œ`, diacritics, typographic quotes and all non-alphanumerics to single spaces, with an ellipsis-aware second pass. 85 strings extracted; 56 matched to corpus body text; the 15 non-matches triaged individually (below). Each match resolved to its containing work, paragraph id, note flag and Argument flag.

3. **Read the primary passages whole, not only the matched strings** — Pontius §§9, 10, 18; *Ep.* XIV, XX, XXI, XXXIII, XXXIV, LIX, LXVII; Possidius *Vita* XXVIII, XXIX, XXXI and the closing peroration — and read each revised Story Text against them sentence by sentence.

4. **Verified Possidius separately** against `cic/texts/possidius_vita-augustini_weiskotten1919.txt`, binning every hit to its chapter by offset against the 30 English-sequence chapter headings, with a de-hyphenation-tolerant matcher and a by-hand read across the bilingual page break at pp. 142/143.

5. **Read CF V7.4 Part II at source** (`cf74.txt` lines 250–271 and the Cross-Walk at 215–221) and re-checked Doc_09 §2's five block quotations word for word against it — including the clause §2 does **not** quote.

6. **Reproduced the generator independently.** Copied the four deliverables to a scratch tree, ran `gen_story_index.py`, diffed: **the committed `lpc_Story_Index.md` reproduces byte-for-byte.** Counted halting sites by grep (**13**), confirmed against `git show 25edc87d` that the pre-fix script had **12**, and **forced all 13 by mutation**. Then hunted defects the guards do not catch, reproducing each by execution.

7. **Diffed the fix pass** (`git show b43f37d6`) to establish exactly which files and which lines the corrective edits touched — `lpcstory003`, `lpcstory004` and `lpcstory006` were not touched at all — and checked every Round 1 finding at its own site rather than accepting a `[CORRECTED …]` notice as evidence.

8. **Checked the upstream citations** — Registry rows 1, 7, 28, 41, 122, 171, 191, 192, 194, 204; Doc_02 §2; Doc_08 Force 2B-5 and the thirteen-letter dossier quotation traced to its own epistle and author; Doc_01–Doc_08's own Status lines; the L4 chunk template; the `cic-story-repository` skill (the §2 epigraph is verbatim); Constitution V2.3 Articles 19 and 20.

**What I tested hardest:** the restored quotations (character by character), the `lpcstory002` §10 passage and the tier argument built on it, the *Ep.* LXVII re-citation, the Possidius chapter span, and the generator. **What I tested least hard:** the Retrieve-When/Do-Not-Retrieve judgements as pastoral judgements, and Doc_08's forces analysis, taken as given per its own eight rounds.

---

# Job 1 — disposition of Round 1's twenty-seven findings

**Closed — verified at the destination, not at the notice.** Five of Round 1's findings are fully closed (H1, H2, M2, M3, M5); four further sub-findings inside M4 and M7 are closed within partially-closed parents. All nine are tabulated:

| # | Verification |
|---|---|
| **H1** | `lpcstory002` now carries §10. Every sentence of the new passage matched to Pontius §10 body text, in order, with the intervening sentence not falsely elided. The three silence claims are gone from Story Text, Tier Justification and Usage Guidance, and Doc_09 §4's row is corrected. **Closed.** |
| **H2** | *Ep.* XX §2 restored with `(spiritual)` intact and the verb un-recast; *Ep.* XXI §2 reads "were ordered to be put to death by hunger and thirst". Both matched to body text (`Celerinus to Lucian`, `Lucian Replies to Celerinus`). "killed by death" now occurs **zero** times in the chunk's Story Text and zero times in the corpus including notes. **Closed.** |
| **M2** | Header corrected; Doc_01/02/03 Status lines read "Approved to proceed (self-disposed…)" and Doc_04–08 do not. **Closed.** |
| **M3** | *Ep.* XXXIII is "About the Ordination of Celerinus as Reader" (confirmed from the `div3` `title=`); the new citation to *Ep.* LXVII resolves to body text at `iv.iv.lxvii-p27` and both quoted clauses are exact. **Closed** (with L16 below). |
| **M4(a)** | The two audit columns are now evaluated predicates, with the redundancy disclosed in-code. **Closed.** |
| **M4(c)** | Row extraction is polarity-aware; `lpcstory006` is credited with row 7 only and rows 41/194 are shown as named-but-not-used. **Closed** (but see M7 below — the same defect survives one field away). |
| **M4(d)** | Phase is read from Doc_09 §3 and a missing value halts. **Closed** on one of Round 1's two offered limbs. |
| **M5** | *Vita* XXVIII–XXXI does cover both stray sentences. The siege is XXVIII ("almost fourteen months") and XXIX ("the third month of the siege"); the forty-year friendship is in Possidius's peroration, which Weiskotten prints **inside chapter XXXI's run** (no heading intervenes between `CHAPTER XXXI` and `NOTES`). **Closed** — but the Source field's explanation of the span is wrong; see M4 in Findings. |
| **M7** | Doc_09 §3.1 retracts the lifetime-collection assertion and re-grounds the thirteen-letter quotation, which I traced to *Ep.* XIV, Cyprian's own letter to the Roman clergy, body text. **Closed in Doc_09 only** — see M3 in Findings. |

**Partially closed (4):** M1 (§6 rewritten; §8 item 2 left standing and contradicted by a new item 5 — see M6); M4(b) (Confidence now cross-checked and the mutation halts; Title, Gravities and Phase still not, and the `lpcstory001` title divergence is still live — L15); M6 (rule disclosed and routed; CF's own alternative route still unquoted and the Doc_02 §9 item 10 departure still unnamed — see M9); L11 (count corrected to 13; enumeration still lists 8 clauses and the number is hard-coded — L14).

**Open — untouched, verified at the site (17):** **M8** (`lpcstory007` still Documented with no added rationale); **L1** ("desolated by the lapse of some" is in *Ep.* XXXIV **body**, `iv.iv.xxxiv-p5`, not the Argument at p4); **L2**; **L3**; **L4**; **L5** ("we who were present" occurs **zero** times in Weiskotten; the source reads "he asked **of us** who were present"); **L6**; **L7**; **L8** (no chunk carries an Absent Story Note); **L9**; **L10**; **L12**; **C1**–**C5** (all five).

`lpcstory003`, `lpcstory004` and `lpcstory006` were not edited at all in the fix pass, which accounts for most of the open LOW items.

---

# Job 2 — what the fix pass broke, and what no guard catches

**The generator reproduces byte-for-byte, and all thirteen halting sites fire.** Forced by mutation: nested notice openers; an unterminated `[NOTED,`; a removed front-matter fence; a deleted `Confidence:` line; `Tier: 5`; a renamed `## Tier Justification`; a Tier-4 chunk with no Source Identification; Tier 1 + `Inferential/Thin`; an emptied `Story-Chunks/`; a §3 tier flip; **a §3 Confidence flip** (the mutation Round 1 used to demonstrate M4(b) now halts); a chunk missing from §3; a removed §3 Phase cell; a one-item §7; and row 28 in a Source field.

**Defects no guard catches — each reproduced by running the generator:**

- **Gravities are derived polarity-blind.** Adding *"This story bears on neither G5 nor G7"* to `lpcstory004` printed **`G1, G3, G5, G7`** in the Master Story Table. This is M4(c)'s defect, fixed for Registry rows and left standing one field away in the same script, in the same pass that reasoned about it explicitly in a code comment. (M7.)
- **§5's item renderer is still unvalidated.** Rewriting §7's headings in the legal Markdown variant `**1.** There is no story…` emitted five garbage rows each opening with a stray `**`, under an unchanged "**Not a placeholder.**" This is Round 1's M4(e), not fixed. (M8.)
- **Title and Phase are not cross-checked.** Setting Doc_09 §3's title for `lpcstory006` to *"The martyrdom of Saint Cyprian of Antioch"* — the exact conflation Registry row 159 warns about — emitted normally. Flipping `lpcstory007`'s §3 Phase to "One" emitted normally. (L15.)

---

# Findings

## HIGH

**None.** I looked hard for one, in the two places this build's history says it would be: a source claim made about the new §10 passage, and a new quotation introduced by a corrective edit. Neither is there. The new §10 material is accurate to the word; the restored `lpcstory005` quotations are exact; the *Ep.* LXVII re-citation is right. The closest thing to a surviving quotation defect is `lpcstory007`'s "we who were present" (L5), which changes a pronoun and not a meaning.

## MEDIUM

### M1 — Seventeen of Round 1's twenty-seven findings were not touched, and the fix pass's own record says all are addressed

**Site:** `lpc_Decision_Log.md`, 2026-09-15 (Doc_09 Round 1) entry; commit `b43f37d6`; and by consequence Doc_09's Document Log and Disposition, which point to that record.

**What I found.** The Decision Log entry states: *"Round 1 … returned SUBSTANTIAL REVISION REQUIRED — 2 HIGH, 8 MEDIUM, 12 LOW, 5 COSMETIC … **All findings are addressed.**"* The commit touched four chunk files, Doc_09, the index and the script. `lpcstory003`, `lpcstory004` and `lpcstory006` were not touched. Checking each finding at its own site: **five fully closed, five partially closed, seventeen untouched** — one MEDIUM (M8), eleven LOW, and all five COSMETIC. One of the partials, M4(e), I reproduced by execution. The entry's own narrative is honest about what it *did* (it names H1, H2, M1, M2, M3 and the four generator items); the completeness claim on top of it is not.

**Why this matters.** This build's every prior fix pass recorded the finding count it applied and matched it ("all thirteen findings", "all 11 findings", "all 15 findings"). A closure record that overstates is worse than an unfinished fix pass, because the next round has no way to know which findings were considered and declined and which were simply missed — and Doc_09's Disposition and Document Log inherit the claim by reference. Round 1's L1, L2, L4, L10 and C1–C5 are small; the point is that nothing records a decision about them.

**Fix.** Either apply the remaining seventeen, or amend the Decision Log entry to a per-finding ledger — applied / declined with reason / deferred — and say which. A build thread may decline a LOW finding; it may not record a decline as an application.

### M2 — `lpc_Story_Index.md` states that no review round has been run against the set. Round 1 was run

**Site:** `lpc_Story_Index.md` Status line and Disposition; `scripts/gen_story_index.py` lines 176 and 286.

**What I found.** Status: *"**DRAFT — not reviewed, not self-disposed.**"* Disposition: *"**No review round has been run against any of the three.** Not self-certified. Not Frozen."* Round 1 was run against all four deliverables and returned SUBSTANTIAL REVISION REQUIRED; Doc_09's own Status, Document Log and Disposition say so three times over.

Both sentences are hard-coded prose in the generator — in the same file whose masthead declares "**Hard-coded prose, re-verified by nothing:** the explanatory paragraphs." The risk the masthead names materialised in the pass that edited the masthead.

**Why this matters.** These four files are "reviewed and disposed of together" by the index's own statement. A reader who opens the index to learn the set's status is told the set is unreviewed. This is the same class as Round 1's M2 (MEDIUM), and the same shape the brief flagged: **a fix landed in one file of a set that is disposed of as a unit.**

**Fix.** Update both strings in the generator and regenerate. Better: derive the round count by counting `Review-Artifacts/Doc09_Round*_Review.md`, which is what `lpc_Force_Index.md` already does for Doc_08.

### M3 — the index still carries the Tier-2 claim Doc_09 §3.1 retracted at M7, and points the reader at the section that now contradicts it

**Site:** `lpc_Story_Index.md` §2, final paragraph; `scripts/gen_story_index.py` line 212.

**What I found.** Round 1's M7 named two sites: "Doc_09 §3.1, Tier 2 paragraph; **repeated in `lpc_Story_Index.md` §2**." Doc_09 §3.1 was corrected and now reads: *"Whether the corpus as a whole was assembled in his lifetime or after it is not something this build has established, and the earlier wording asserted it."* The index still reads: *"This world transmitted itself by correspondence, and **a dossier assembled by its own author in his own lifetime** is not a community's remembered collection. **See Doc_09 §3.1.**"*

**Why this matters.** The index asserts as fact the claim Doc_09 has just retracted, and cites Doc_09 as its authority for it. Of the two files, the index is the one a reviewer filters by. The Tier-2-is-zero conclusion is sound on CF's own definition either way — that is exactly what the Doc_09 correction says — so the cost is entirely avoidable.

**Fix.** Replace the generator's line 212 with Doc_09 §3.1's corrected wording and regenerate.

### M4 — `lpcstory007`'s corrected Source field makes a new, checkable claim that is false

**Site:** `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md`, Source field.

**What I found.** The corrected field reads: *"**XXVIII–XXXI** — the death and burial sequence, of which XXXI carries the penitential psalms, the will and the library instruction, **while the siege and the last preaching are established in the preceding chapters**."*

The siege is in the preceding chapters — XXVIII ("almost fourteen months") and XXIX ("the third month of the siege"). **The last preaching is not.** "Up to the very moment of his last illness he preached the Word of God in the church incessantly, vigorously and powerfully, with a clear mind and sound judgment" sits in **chapter XXXI**, three sentences after "he had all that time free for prayer" — I located it by offset against the edition's own chapter headings and then printed the surrounding page to be sure. All twelve of the chunk's Possidius quotations are in XXXI.

**Why this matters.** The span itself is now right, so no citation fails and M5 is closed. But the field that was corrected for an inaccurate source claim now carries a different inaccurate source claim, in the same sentence. This is the recurring shape, in its mildest form: the corrective edit added an explanatory gloss that was not checked against the text it glosses.

**Fix.** "…of which XXXI carries the penitential psalms, the last preaching, the death, the will and the library instruction, while the siege is established at XXVIII–XXIX."

### M5 — `lpcstory002`'s rebuilt Tier-1 warrant tests two of CF's three markers and leaves the third unaddressed, though the cited range carries it twice

**Site:** `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md`, Tier Justification, "Not Tier 3" and "Why the tier holds anyway".

**What I found.** The rebuilt argument enumerates CF V7.4's three markers — *"the idealized portrait of a saint's life, the miracle sequence, the death as completion of a formed life"* (verbatim; I checked it at `cf74.txt` line 260) — and concludes: *"**A scriptural comparison inside a moral exhortation is none of the three.**"*

That sentence is true. But the argument disposes of only two markers explicitly ("no miracle and no providential intervention", "nobody dies here") and never addresses the **idealized portrait**, which is present in the cited range and not in the Tobias sentence at all:

> §9: "it would be a wrong to pass over what **the pontiff of Christ** did, **who excelled the pontiffs of the world** as much in kindly affection as he did in truth of religion."
> §10: "And under such a teacher, who would not press forward … to please both God the Father, and Christ the Judge, and **for the present so excellent a priest**?"

Round 1 named the first of these in the same bullet that produced H1. The fix pass removed the falsified "no typological patterning" claim and built a new argument around the Tobias typology, and left the marker Round 1 actually quoted untouched.

**I tested the tier itself, hardest of anything in this review, and Tier 1 holds.** The distinction the chunk draws is real: `lpcstory006`'s Zacchaeus typology is applied to *what physically happened* and the reader cannot separate event from pattern; §10's Tobias comparison is applied to *how much was given*, and the underlying fact — relief extended beyond the congregation — is the kind of claim Cyprian's own treatises independently make. CF's Tier 3 is for material "resting on collected tradition rather than direct documentation"; Pontius is direct documentation. Encomiastic epithets for the subject do not reshape the events. **Tier 1 at Widely Accepted is right.** The warrant printed for it is incomplete.

**Fix.** Add the third marker and answer it: the idealised portrait is present as *encomium of the bishop*, and encomium of the narrator's subject does not reshape the reported events — which is why the confidence is stepped to Widely Accepted rather than the tier to 3. That is the argument the chunk is in fact making; it just does not say so.

### M6 — Doc_09 §8 now contradicts itself: item 2 and item 5 are the same open item with opposite content

**Site:** `Doc_09_Story_Inventory.md` §8, items 2 and 5.

**What I found.** Item 2: *"Augustine's sermons on Perpetua and the Scillitan martyrs are **unread at source** (§6 item 1)."* Item 5: *"Augustine's sermons on Perpetua and the Scillitan martyrs are **unavailable, not unread** (§6 item 1, corrected at Round 1)."* §6 item 1 itself now says they are *"not available to this build at all."*

Round 1's M1 named both §6 item 1 **and §8 item 2** as sites. The fix pass rewrote §6, **appended** a new §8 item 5, and left §8 item 2 standing.

**Why this matters.** §8 is the section a next pass reads to know what work is outstanding. It now instructs that pass to go and read a text the same list says does not exist, two items later. The correction is defeated by the sentence it was appended beneath. This is the fix-pass-introduced class of defect, and it is the clearest instance in this pass.

**Fix.** Delete item 2; keep item 5 and renumber. While there, item 4 and §6 item 4 still say the 411 *Gesta* is "this world's one unread source" while items 1 and 2 name another (L6).

### M7 — the gravity derivation is polarity-blind: M4(c)'s defect, fixed for rows and left standing one field away in the same script

**Site:** `scripts/gen_story_index.py` line 103; `lpc_Story_Index.md` §1, Gravities column.

**What I found.** Rows are now extracted clause by clause with a negation test (lines 95–101), with a code comment explaining exactly why. Gravities are extracted eleven lines further down as `sorted(set(re.findall(r"\b(G[1-8])\b", t)))` over the **whole chunk body** — no clause splitting, no polarity test, and no cross-check against Doc_09 §3's own Gravities column.

**Reproduced.** Adding *"This story bears on neither G5 nor G7."* to `lpcstory004`'s Formation Ecology Connection printed **`G1, G3, G5, G7`** in the Master Story Table, with no guard firing. The index then presents that row as derived.

**Why this matters.** Round 1 routed the polarity defect to portfolio level on the ground that "every sibling build's story index will scrape Source fields the same way." The same pass that fixed it for one field left it in another field of the same table — which strengthens the routing considerably: **the defect is a class, not an instance.** Declining to draw on something is normal prose in these chunks (`lpcstory006` does it for the *Acta*; `lpcstory003`'s Do-Not-Retrieve does it for the lapsed), so this is a live hazard, not a contrived one.

**Fix.** Apply the same clause-split-and-negate to the gravity scan, or read gravities from a dedicated front-matter field, and cross-check the result against Doc_09 §3's Gravities column.

### M8 — Round 1's M4(e) is not fixed; §5 still emits garbage rows on a legal Markdown variant under an unchanged "Not a placeholder"

**Site:** `scripts/gen_story_index.py` lines 146 and 260.

**What I found.** The guard counts items with `^\*\*\d\.` (line 146); the renderer captures with `^\*\*(\d)\.\s*(.+?)\*\*` (line 260). Round 1's recommended fix — `assert len(items) == len(absent_items)` before rendering — was not applied, and the commit message's list of generator fixes names only four of the five.

**Reproduced.** Rewriting §7's headings as `**1.** There is no story…` — a legal Markdown rendering of the same content — produced:

```
| 1 | ** There is no story from inside the 133-year silence, and there cannot be. |
```

five times, under the unchanged sentence "**Doc_09 §7 answers the required question with five enumerated absences, in 564 words.** Not a placeholder."

**Why this matters.** §7 is the Article 20 section. A renderer that silently degrades the one table asserting §7 is substantive, while the assertion stands, is the precise failure the script's own "FAIL LOUDLY" header exists to prevent.

**Fix.** Assert the two counts agree before rendering, and halt on mismatch.

### M9 — Doc_09 §2 trims CF's Tier 1 confidence clause at exactly the sentence that supplies CF's own route, then escalates a new rule on the ground that CF supplies none

**Site:** `Doc_09_Story_Inventory.md` §2, Tier 1 bullet and the `[ADDED — Round 1's M6]` paragraph.

**What I found.** §2 states that its confidence bands are "the Framework's own words." CF V7.4 line 253 reads in full:

> "Confidence level: Documented to Widely Accepted at the narrative level. **May carry Widely Accepted or Contested confidence for specific details within the narrative depending on the author's access and perspective.**"

§2 prints the first sentence and drops the second, unmarked. The `[ADDED]` paragraph then escalates "a source is not a tier" on the ground that **"CF V7.4 … does not state how to tier a source that satisfies one tier's author test and another's genre test simultaneously."** That is literally true of *tiering*, and materially incomplete: CF's dropped sentence is a stated mechanism for genre-affected reliability inside Tier 1, and it is **the mechanism this document actually uses at `lpcstory002`** (Tier 1, stepped to Widely Accepted because the sermon reaches us through a biographer of praise).

Round 1's M6 asked for three things: mark the rule as the build's judgement (**done**), note CF's own alternative route (**not done**), and name the departure from Doc_02 §9 item 10's provisional Tier 3 reading of Pontius (**not done** — Doc_02 §9 item 10 is cited at the head of Doc_09 for a different purpose and the reversal is nowhere named).

**Why this matters.** This is the document's one portfolio-level governance escalation. A project lead ruling on it should see CF's line 253 whole, because on the evidence of `lpcstory002` the build already has a CF-native solution and may not need the new rule at all. As filed, the escalation is raised against a Framework text the document itself has trimmed at the deciding point.

**Fix.** Restore CF line 253's second sentence in §2, state in the `[ADDED]` paragraph that CF offers a confidence-calibration route which `lpcstory002` in fact takes, and name the Doc_02 §9 item 10 departure.

### M10 — a `[CORRECTED …]` notice sits inside `lpcstory002`'s deployable Story Text, with a transition sentence whose referent is a prior draft

**Site:** `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md`, Story Text.

**What I found.** `lpcstory002` is the only chunk in the set with a correction notice inside `## Story Text`; the other six put theirs in the Source field or the Tier Justification. The new §10 material is also introduced by **"And Pontius does say what followed."** — a sentence that answers a reviewer, not a reader, and is unintelligible to anyone who has not read Round 1. The narrative then ends on a 90-word build-process block rather than on Pontius.

The L4 template's Final Assembly Instruction 3 is directly on point: *"does this story announce its epistemic status through the way it is told, or does it require an external disclaimer? The tier register should be built into the telling, not added as a footnote."*

**Why this matters.** Story Text is the deployable layer — the thing a Representative retrieves and speaks from. Every other section of the chunk is builder-facing and is the right home for the record. The material itself is excellent; it is only the seam that shows.

**Fix.** Move the notice to the Tier Justification (which already carries the parallel H1 notice) and rewrite the transition so the paragraph reads forward from the sermon — the Tobias comparison is a natural close.

### M11 — Round 1's M8 is untouched: the confidence bands are still set inconsistently between `lpcstory002` and `lpcstory007`

**Site:** `lpcstory002` and `lpcstory007` Confidence fields and Tier Justifications.

**What I found.** Unchanged from Round 1, and now sharper: `lpcstory002` is stepped to **Widely Accepted** because "a reported speech inside a biography of praise is not the same evidentiary object as a letter in the man's own hand" — while having a corroborating witness in *De mortalitate*. `lpcstory007` remains **Documented** while its own Tier Justification records that "no second account of Augustine's death exists in this corpus" and that "the tier rests on the eyewitness claim and the absence of genre machinery, not on corroboration." `lpcstory007` was edited in this pass (the Source field) without the band being revisited or the asymmetry explained.

Both remain inside CF's Tier 1 band, so this is calibration, not classification — but it is the direction Article 17 warns about.

**Fix.** As Round 1: step `lpcstory007` to Widely Accepted on its own stated ground, or state why eyewitness presence outweighs absent corroboration here while reported speech does not outweigh present corroboration there.

---

## LOW

**Carried from Round 1, verified open at the site (11).**

**L1** — `lpcstory003`'s Do-Not-Retrieve still says the story "deliberately does not address" the lapsed; *Ep.* XXXIV names the lapse as the vacancy's cause in its **body** ("desolated by the lapse of some", `iv.iv.xxxiv-p5`, Argument flag false — I re-checked this after my own detector briefly said otherwise).
**L2** — `lpcstory003`: "He was in the heap" and "a daughter searching a heap of bodies"; the letter says she "sought for the corpse of her father."
**L3** — `lpcstory002`: "went further **than his hearers expected**" (no audience reaction in Pontius) and "Bodies were left **in the streets**" (Pontius: "over the whole city").
**L4** — `lpcstory004`: "**to be** rescued and redeemed…" inside the quotation marks; the source reads "may now Himself **be** rescued and redeemed."
**L5** — `lpcstory007` Tier Justification and Doc_09 §4 both quote **"we who were present."** That string occurs **zero** times in Weiskotten; the source reads "he asked **of us** who were present." "in our presence" is exact. This is the one quotation defect that survives the pass, and it sits in the §4 row whose text is "Every detail is his."
**L6** — §6 item 4 and §8 item 4 still call the 411 *Gesta* "this world's one unread source" while §6 item 2 and §8 item 1 name another.
**L7** — Doc_09 §4 and index §3 both still say **two** candidates were declined; §6 enumerates **four**.
**L8** — No chunk carries the template's **Absent Story Note** section; at least four carry exactly that material inside other sections. No guard for it.
**L9** — §6 item 1 still grounds Perpetua's exclusion on the date "on the same reasoning that excludes the Scillitan martyrs at row 28." Registry row 204 gives a different operative ground: *"Out-of-Boundary for this world by prior ruling — assigned to `tertullian-s-voice` … (Mark's own 2026-08-26 ruling)."* This bears on whether the proposed future story may touch the text at all.
**L10** — `lpcstory007`: "The library, per Possidius's instruction, largely survived." Possidius records the instruction only ("He repeatedly ordered that the library of the church and all the books should be carefully preserved for future generations"); the outcome is not in the chapter.
**L12** — §7 item 4 still argues entirely from Phase One and never names Albina (*Ep.* CXXVI) or the Nuns of Hippo (*Ep.* CCXI), the two strongest counter-cases and the only Phase Two ones. The item is correct; it is weaker than it needs to be.

**New at this round (6).**

**L13 — the masthead notice claims a verification that could not have happened.** *"the script has thirteen halting sites and **Round 1 forced all of them**."* The count is right — I grepped it and forced all thirteen. But `git show 25edc87d` shows the pre-fix script had **twelve** `sys.exit` calls; the thirteenth (Doc_09 §3 stating no transmission phase, line 142) was created by this fix pass. Round 1 forced twelve and reported twelve. A newly written guard is represented as adversarially verified. *Fix:* "…thirteen halting sites; Round 1 forced the twelve that then existed, and the thirteenth was added in this pass and is unreviewed."

**L14 — the guard enumeration still does not match its own count, and the count is hard-coded.** The masthead lists eight clauses and then asserts thirteen sites. Unlisted: no front-matter fence; a notice-like opener surviving stripping; no chunks found; a **Confidence** disagreement with §3 (only "tier" is named, though the pass extended the check); a missing Phase. The notice says the number was "counted here with a grep over the script rather than from memory" — but it is typed into prose the masthead itself declares "re-verified by nothing," so it goes stale on the next guard. Round 1's L11 asked for the count to be derived or the number dropped; neither was done. *Fix:* emit the count from `len(re.findall(r"sys\.exit", open(__file__).read()))`, or list the conditions without a number.

**L15 — the masthead still overclaims the §3 cross-check, and a live divergence remains.** *"the agreement between each chunk and Doc_09 §3's own table"* — Tier and Confidence are compared; **Title, Gravities and Phase are not.** Doc_09 §3 still titles `lpcstory001` "The election of Cyprian, **still a neophyte**" where the chunk's canonical `Story-Title` is "The Election of Cyprian", against the template's "use the same title consistently across all references." I demonstrated that §3 could retitle `lpcstory006` "The martyrdom of Saint Cyprian of Antioch" — the conflation Registry row 159 warns about — with no halt. §3 also still gives `lpcstory006` the bare "Contested" where the chunk and the template's Tier 3 pairing carry the full clause; the new check tolerates this by design (`cconf.split(";")[0]`), which resolves Round 1's M4(b) by widening the check rather than closing the divergence. *Fix:* narrow the masthead to "the tier and confidence agreement", or extend the comparison and reconcile §3.

**L16 — `lpcstory001`'s correction notice describes half of the change it made.** The notice reads: *"this cited *Ep.* XXXIII and LI. **XXXIII is about Celerinus's appointment as a reader**…"* True, and it is Round 1's finding. But *Ep.* **LI** was also removed, and Round 1 verified LI as **correct** corroboration ("by the suffrage of the people who were then present"). Round 1's recommended fix was XXXII **and** LXVII. The chunk now rests on a single letter, and the notice gives no reason for dropping a citation that was sound. *Fix:* restore LI (or XXXII) alongside LXVII, or say why one locus suffices.

**L17 — `lpcstory002`: "Tobias, who buried the dead of 'his own race only.'"** Pontius writes "Tobias **collected together those who were slain by the king and cast out**, of his own race only." "Buried" is the chunk's gloss, outside the quotation marks but attributed to Pontius's sentence. Small, and the same class as L2/L3. *Fix:* "who gathered the dead of 'his own race only.'"

**L18 — *Ep.* LXVII is described as "Cyprian's own letter."** It is a synodical letter: "Cyprian, Cæcilius, Primus, Polycarp, Nicomedes … and Paulus, to Felix the presbyter, and to the peoples abiding at Legio and Asturica." Cyprian is first-named and the letter is his in the ordinary sense, so this is not the intra-corpus misattribution failure mode — but in a build where `lpcstory005` makes attribution discipline a section of its own, a 37-signatory council letter should be named as one, particularly since "by the suffrage of the whole brotherhood" is then the voice of a synod attesting a shared practice, which is *stronger* corroboration, not weaker. *Fix:* "a letter of Cyprian and thirty-six colleagues in council."

---

## COSMETIC

**C1** — Doc_09 §2's Tier 3 confidence line still trims CF at three points without ellipsis; CF reads "Contested for the general portrait **or attribution**; Inferential/Thin for specific details shaped by **hagiographic** convention **or for events whose historical occurrence cannot be verified**." (Verified at `cf74.txt` line 261.)
**C2** — `lpcstory002` still merges across the source's interpolation: Pontius has `"It becomes us," said he, "to answer to our birth…"`. My sweep flagged this string as unmatched for exactly that reason.
**C3** — `lpcstory005` still quotes Doc_02 as "Firmilian"; Doc_02 §2 reads "Firmilian **of Caesarea**".
**C4** — `lpc_Story_Index.md` §1's Confidence cell for `lpcstory006` still carries a full clause.
**C5** — Doc_09's header still paraphrases Doc_05 §11 item 9's "the Perpetua **sermons**" as "the Perpetua **material**".

---

# Is the deliverable adequate to proceed to Doc_10?

**Yes, and more clearly than at Round 1.**

- **The repository is not composited, and I verified that independently rather than inheriting it.** 56 quoted strings matched to body text across two corpora; **zero** inside a `<note>`; **zero** inside an ANF *Argument* except `lpcstory004`'s deliberate exclusion quotation, which my corrected detector confirms is inside `iv.iv.lix-p4`, an Argument paragraph, while the sesterces figure the chunk actually uses is at `iv.iv.lix-p14`, body. Both of the build's own evidentiary claims — the Argument/body distinction at `lpcstory004` and the confessor attributions at `lpcstory005` — survive direct checking a second time.
- **The thing Round 1 said it would not let pass unfixed is fixed.** `lpcstory002`'s Usage Guidance no longer instructs the Representative to say something untrue about a source; it now instructs the Representative to report what Pontius says *with the source's own character named*, which is better than either the original or the minimum fix.
- **The tier work survives its hardest test.** I re-read Pontius §18 and Possidius XXXI whole against CF's three markers and confirm the `lpcstory006`/`lpcstory007` pair is a textual distinction, not a convenient one. `lpcstory002`'s Tier 1 also holds — the argument for it is incomplete (M5), not wrong.
- **The generator reproduces byte-for-byte and all thirteen halting sites fire**, including the three that Round 1's M4 caused to be strengthened.

What holds the verdict at SUBSTANTIAL is bookkeeping and sweep, not substance: **seventeen untouched findings recorded as closed (M1)**, a sibling deliverable that denies the review happened (M2) and still carries a retracted claim (M3), and four small defects introduced or left by the corrective edits (M4, M6, M7, M8). **None of these blocks Doc_10.** A fix pass that actually closes the remaining list should clear at Round 3, and I would expect it to.

**The one thing I would not carry into Doc_10 unfixed** is M2 together with M3 — not because either is dangerous, but because `lpc_Story_Index.md` is the artifact downstream work will consult, and it currently misstates both the set's review status and one of Doc_09's own retracted claims.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** This document makes no identity, title or voice decision. Noted separately and not as an escalation: `lpcstory002`'s deployable Story Text now contains build-process apparatus (M10). That is a content defect inside this document's own gift to fix, not an identity decision.

- **Portfolio-level or cross-world — TWO items, both inherited, and one materially strengthened.**
  1. *The corpus-wide editorial-apparatus item.* Re-verified independently and still the ledger's first **positive** instance: of 56 matched strings, zero resolve inside an *Argument* except the one quoted to be excluded. Carry forward unchanged.
  2. *The index-generator-as-build-artifact item (Doc_08 Round 5; Round 1's M4c).* **Strengthened, and the strengthening is the point.** The fix pass made row extraction polarity-aware with a code comment explaining why, and left the **gravity** extraction polarity-blind eleven lines below (M7). A defect that is fixed in one field and survives in the adjacent field of the same table is not an instance — it is a class, and every sibling world's story index will inherit the class, not the instance. **Route at portfolio level with this second instance attached.**

- **Governance or methodology — open at six, and one filing needs amendment before it is ruled on.** The build routed *"a source is not a tier"* as a new item, which is right and was Round 1's M6. **But the escalation as filed misstates the Framework's silence** (M9): CF V7.4 line 253's second sentence — "May carry Widely Accepted or Contested confidence for specific details within the narrative depending on the author's access and perspective" — is a CF-native route to the same problem, is dropped from §2's quotation of that very line, and is the route this document already takes at `lpcstory002`. **The project lead should be shown CF line 253 whole before ruling**, because the answer may be that no new rule is needed. I add no seventh item; I ask that the sixth be amended before it is ruled on.
  **One further methodology question I raise rather than escalate**, for the project lead's judgement: what "apply the review" means when a fix pass closes nine of twenty-seven findings and the Decision Log records "All findings are addressed" (M1). Doc_08's fix passes recorded matched counts; this one did not. If a build thread may decline LOW findings — and it reasonably may — the convention should be stated, because otherwise every subsequent round has to re-derive the ledger, as I did.

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. Doc_09's substantive statement of it is accurate; only its scope-word is still wrong (L6), and §8 now carries four items about unread or unavailable sources while §6 item 4 says there is one.

---

# Check confirmation — my own harnesses, including the two that were wrong

**Thirty-odd failing checks in this build have turned out to be defects in the check.** Two of mine were, and one of them would have produced a fabricated HIGH against the chunk that quotes Cyprian's own letter most carefully. I record them before the findings that survived.

## Defective checks of my own (both caught before reporting)

**D1 — my ANF *Argument* detector marked an entire letter body as editorial matter.** My first pass located `Argument.—` in the flattened body and ended the region at the next `\n1.`, on the assumption that ANF letter bodies open with a numbered paragraph. *Ep.* XXXIV does not — it opens "Cyprian to the presbyters and deacons, and to the whole people…" — so the region ran on 2,000 characters and swallowed the letter. The detector duly reported that **every one of `lpcstory003`'s quotations was inside the ANF Argument**: the wife "burned (I should rather say, preserved)", the daughter who "sought for the corpse of her father", "remained unwillingly from among the companions". Had I reported that, `lpcstory003` would have taken a fabricated HIGH for reading 19th-century editorial matter as Cyprian's voice — against a chunk that is in fact clean. **Caught by printing Ep. XXXIV's paragraph structure from the raw XML:** the Argument is `iv.iv.xxxiv-p4` alone; the body is `p5`. I rebuilt the detector to mark whole `<p>` elements whose text opens "Argument", yielding 101 Argument paragraphs across the volume. Re-run: **0 of 56 matched strings inside an Argument**, and the one string that *is* inside one is `lpcstory004`'s deliberate exclusion quotation at `iv.iv.lix-p4`.

**D2 — my work-attribution regex matched `shorttitle=` before `title=`.** Every epistle came back labelled "Epistle LXVII" rather than by its actual title, which would have made the intra-corpus misattribution check useless — I could not have told a letter *by* Cyprian from a letter *to* him. Caught on the first query, fixed with a negative lookbehind, and no finding rested on the broken version.

**D3 — the Possidius page-break false negative, reproduced.** My sweep reported `lpcstory007`'s "With all the members of his body intact, with sight and hearing unimpaired, while we stood by and watched and prayed…" as missing. This is exactly Round 1's disclosed D3: the sentence is **split across pages 142 and 143 with the Latin text and the apparatus criticus printed between**. I confirmed by hand that the two halves join exactly as the chunk prints them. Not a finding. My matcher also needed a de-hyphenation-tolerant pattern for "physi-cians" and "re-peatedly"; without it, two more strings read as missing.

## Confirmations of the findings I did report

- **H1's closure confirmed three ways.** (1) Every sentence of the new §10 passage matched to body text and binned to Pontius's §10 by reading the section whole from `\n10.` to `\n11.`. (2) The passage printed directly from the raw XML region, outside any `<note>` and outside any Argument paragraph. (3) A corpus-wide search of every `lpc` file for "household of faith", "Tobias", "overflowing works" and "straitness of poverty" returns **only** `lpcstory002`, the Round 1 review and the Decision Log — confirming the notice's claim that no upstream document had ever cited §10, and that the citation is new here.
- **H2's closure confirmed two ways.** Both restored quotations matched to body text at `Celerinus to Lucian` and `Lucian Replies to Celerinus`, with the containing works recovered from the `div3` `title=` attributes rather than the running text; and "killed by death" searched across the **whole** volume **including notes** — zero occurrences. The phrase now appears in the chunk only inside a sentence describing the error it corrects.
- **M3's closure (the *Ep.* LXVII re-citation) confirmed two ways.** The harness resolved both clauses to `iv.iv.lxvii-p27`; I then printed the letter's opening from the marked corpus, which gave the Argument, the 37 signatories and the body, establishing both that the quotation is body text and that L18's point about the collective authorship is real.
- **M4 confirmed two ways.** "Up to the very moment of his last illness he preached the Word of God" binned to chapter XXXI by offset against the edition's own 30 English chapter headings; then confirmed by printing the surrounding 2,000 characters, which show `CHAPTER XXXI / Death and burial` five sentences earlier.
- **M7, M8 and L15 confirmed by execution**, not by reading the code: each mutation applied to a scratch copy, the generator run, and the emitted index inspected. I checked each mutation actually changed the file (`assert n != t`) before running — Round 1's own Decision Log records a mutation that silently failed to apply and looked exactly like a working guard.
- **M1 confirmed by diff and by site.** `git show b43f37d6 --stat` establishes which files the pass touched; each untouched finding then checked by grep at its own destination rather than inferred from the diff.
- **All thirteen halting sites forced individually**, each from a fresh copy of the deliverables, each producing its own FATAL message; and the committed index re-derived **byte-for-byte** before any mutation.

## The review brief's own premises, reported as directed

1. **"The masthead now claims thirteen halting sites. Reproduce them."** Correct — there are thirteen and I forced all thirteen. What the brief inherits without qualification is the notice's further claim that *Round 1 forced all of them*; Round 1 forced the twelve that existed (L13).
2. **"`lpcstory007`'s source span changed from *Vita* XXXI to XXVIII–XXXI. Check that the span actually covers what the chunk draws on."** It does — including the forty-year friendship, which Round 1 placed in a separate "epilogue" but which Weiskotten prints inside chapter XXXI's own run. **Round 1's M5 is closed.** What is wrong is the Source field's gloss on the span (M4), which is a different defect from the one the brief anticipated.
3. **"Does the Tobias typology plus a reported sermon push it to Tier 3?"** No. I tested this hardest of anything here and Tier 1 at Widely Accepted is right; the chunk's stated warrant is incomplete in a different place than the brief suggests — the **idealized portrait**, not the typology (M5).
4. **"Round 1's own headline was that the repository is not composited."** Independently re-verified and it holds.
5. **The brief's characterisation of the four generator changes is accurate**, with one addition worth stating: the No-Tier-5 audit columns are now evaluated predicates whose "No" branch is unreachable in any file that emits, because both conditions also halt earlier. The script says so itself in a comment and calls the redundancy the point. That is a fair defence and I do not grade it.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**0 HIGH · 11 MEDIUM · 17 LOW · 5 COSMETIC** — of which **seventeen** are Round 1 findings verified untouched at their own sites, and **five** (M2, M4, M6, M7 as a class-instance, and L13) were introduced or left behind by the Round 1 fix pass itself.

**Both HIGH findings are closed and the stories are sound.** The verdict is driven by breadth and by a false closure record, not by anything a participant would be told wrongly. **A fix pass that works through the remaining list should clear this deliverable at Round 3.**

*Simulated review — informational only, not an Article 31 substitute.*
