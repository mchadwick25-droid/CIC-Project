# Doc_09 — Round 5 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**2 HIGH · 10 MEDIUM · 20 LOW · 6 COSMETIC.**

**Say the good part first, because it is the larger part and it is now settled.** The three Absent Story Notes rewritten after Round 4 **hold**. I verified every positive and every negative in them at source, twice each. Pontius does point the reader to the *Acta*. Possidius does record the burning of Hippo, in *Vita* XXVIII, inside the span the chunk cites, and the Latin on the facing page confirms it. Cyprian did receive and answer a letter written by lapsed petitioners, at *Epistle* XXVI, in his own voice and in body text. **Round 4's three HIGHs are genuinely closed, and the fix pass did not over-correct into new positive claims that fail.** That was the thing most likely to go wrong this round and it did not go wrong.

**What holds the verdict at SUBSTANTIAL is two findings, and neither is in a Story Text.**

- **HIGH-1** is the defect class this document has produced in four of five rounds, surviving at the one site Round 4 named and the fix pass did not visit: `lpcstory005`'s **Usage Guidance** still tells the Representative that the nearest thing to a named lapsed person in this corpus is Celerinus's unnamed sister — **in a sentence that cites Doc_09 §7 item 3 as its authority, after §7 item 3 was rewritten at Round 4 to say the opposite**, and against the letter the chunk is built on, which names Numeria and asks that "such a great sin" be remitted to her. It is a deployable retrieval instruction resting on a false claim about its own source.
- **HIGH-2** is in the new script. `scripts/notice_strip.py` — written to stop a four-round false positive in closure audits — **deletes every live assertion that follows an inline notice in the same paragraph**. On Doc_09 §7 it discards 48% of the section. On the §2 escalation paragraph it returns a single space. A closure audit run through it reports live, uncorrected prose as "mention only". It manufactures precisely the false conclusion the recurring defect depends on, and it is plausibly why the §2/Disposition contradiction at MEDIUM-2 below was not caught.

**If those two are fixed — one sentence and one regex — I would return MINOR REVISION on this same reading.** Nothing in the MEDIUM band is a blocking defect, nothing requires re-selecting a story, re-reading a source, or rewriting a Story Text, and the LOW/COSMETIC tail is a cleanup pass that has now been deferred four times.

---

# Method

**Everything below was derived here. I inherited no claim from the brief, from the fix pass, or from Rounds 1–4** — including the finding counts, the "roughly 100 findings" figure, and the characterisation of the defect class. Two of the brief's premises turned out to be wrong (COSMETIC-6, and the notice-stripper limitation reported in the check-confirmation section).

1. **Corpus harness, built from scratch.** I parsed `cyprian.xml` character by character, carrying for every character its containing work (`title=` on `<div2>`/`<div3>`), its page, and **whether it lies inside a `<note>` span — marked before any tag was stripped**, as the brief requires. I then built *two* search streams: one with note text in place and one with note text removed. A quotation that matches in the **note-stripped** stream is body text by construction, which is a stronger test than an in-note flag. 1,724,448 characters, 152,353 of them inside notes, 107 works.
2. **Possidius harness, built from scratch.** Weiskotten is bilingual with alternating pages. I segmented the main text (lines 1604–5075) by running head — `SANCTI AUGUSTINI VITA` opens a Latin page, `LIFE OF SAINT AUGUSTINE` an English one — reconstructed the English-only stream, de-hyphenated at line ends, and kept a chapter map. This defeats the failure mode that produced false negatives in four consecutive rounds (a Latin page inserted mid-sentence, and `physi-/cians`). It did not defeat all of them; see the check-confirmation section.
3. **Every quotation in all seven chunks and in Doc_09** re-matched against source. Zero resolve inside a `<note>`. The one that resolves to an ANF *Argument* is the one `lpcstory004` quotes in order to exclude.
4. **The three rewritten Absent Story Notes, assertion by assertion, positives as hard as negatives**, each confirmed a second way (note-stripped stream for Cyprian and Pontius; the facing Latin page for Possidius).
5. **The generator.** Regenerated into a clean copy: **byte-identical** to the committed index. Counted halting sites by AST walk: **13**. Forced all 13 from thirteen fresh copies. Then ran eleven further mutation probes hunting for defects no guard catches.
6. **The index re-derived independently** — my own parser, my own gravity rule (the explicit `**Gravities:**` declaration only), my own §7 item and word counts — and compared field by field against the committed output.
7. **`notice_strip.py`** read, then attacked in both directions with six constructed cases and then against the live deliverables.
8. **Rounds 1–4 read in full** and every finding tested at **every site the finding names**, not the site it quotes.
9. **The withdrawal of CO-022's escalation** checked against CF V7.4 Part II's own text at `cf74.txt` lines 247–271, read whole.
10. **The Decision Log entry and the fix-pass commit** (`a6a6be73`) read against each other and against the live text.

---

# Job 1 — the open-findings register

## 1.1 How many findings there actually are

**Counted raw, across the four rounds: 121** (R1 27, R2 33, R3 28, R4 33). **Counted as distinct findings, collapsing carried repeats: 78.** The brief's "roughly 100" sits between the two and matches neither. Recorded as directed; see COSMETIC-6.

## 1.2 The register

Status key: **CLOSED** · **PARTIAL** (some named sites fixed, others live) · **OPEN**. Every row was checked at the live text, at **every** site the finding names. No `[CORRECTED …]` notice was taken as evidence of anything.

### Closed (verified in the live text) — 44 distinct findings

| First raised | Finding | Verified how |
|---|---|---|
| R1-H1 | `lpcstory002` asserted a silence Pontius §10 refutes | §10 now quoted in Story Text, Tier Justification and Usage Guidance; §10 read whole at source. *But see MEDIUM-6 — a third site in the same chunk.* |
| R1-H2 | `lpcstory005`'s two altered quotations | Both restored and matched verbatim, in body text, in the note-stripped stream |
| R1-M1 | Perpetua sermons "unread" → unavailable | §6 item 1 and §8 item 5 both corrected |
| R1-M2 | header said none of Doc_01–08 self-disposed | Corrected; I checked all eight status lines — three read *Approved to proceed*, five do not |
| R1-M3 | `lpcstory001` mis-cited corroboration | *Ep.* XXXIII removed; *Ep.* LXVII verified at source. *Ep.* LI residue open — see LOW-3 |
| R1-M4(a) | index audit columns were string literals | Now evaluated predicates |
| R1-M4(c) | Registry-row derivation polarity-blind | `NEG_CLAUSE` now shared by both derivations. *Class not fully closed — MEDIUM-4, MEDIUM-5* |
| R1-M4(d) | phase guessed from author keywords | Read from Doc_09 §3. *Whitespace hole open — LOW-10* |
| R1-M4(e) | §5 emitted garbage rows on a legal Markdown variant | One shared `ABSENT_ITEM` pattern; forced, renders correctly |
| R1-M5 | `lpcstory007` cited one chapter, drew on three | Source now XXVIII–XXXI; I verified the psalms, the request, the death, the will and the library instruction are all in XXXI, and the siege in XXVIII–XXX |
| R1-M6 | "a source is not a tier" filed as CF's rule | Disclosed as this build's construction. *Escalation withdrawn — see the CO-022 assessment, and MEDIUM-2* |
| R1-M7 | Tier-2 argument cited Doc_08 §2B-5 for what it does not say | Both sites corrected. I verified Doc_08 §2B-5 does carry *"these thirteen letters sent forth at various times… which I have transmitted to you"*, and traced it to *Ep.* XIV, Cyprian's own |
| R1-M8 / R2-M11 | confidence bands inconsistent between `002` and `007` | `lpcstory007`'s access-based warrant is sound and survives pressure |
| R1-L1 / R2-L1 / R3-HIGH-1 | `lpcstory003`'s Do-Not-Retrieve misstated *Ep.* XXXIV | Now *"names them only as the cause of the vacancy"* — exact against the letter |
| R1-L2 | "heap" / "searching a heap of bodies" | Both gone; *"Where she searched, the letter does not say"* is correct |
| R1-L3 | "than his hearers expected" / "in the streets" | Both gone; *"over the whole city"* verified |
| R1-L4 | "to be" inside `lpcstory004`'s quotation marks | Corrected; source reads *"may now Himself be rescued"* |
| R1-L5 | "we who were present" | Gone from both named sites — the chunk **and** Doc_09 §4. The string occurs zero times in Weiskotten; *"asked of us who were present"* is exact |
| R1-L6 | *Gesta* called "this world's one unread source" | §6 item 4 and §8 item 4 both corrected |
| R1-L7 | "two" candidates vs §6's four | Doc_09 §4 and index §3 both now say four; §6 enumerates four |
| R1-L8 | no chunk carried an Absent Story Note | Six of seven now do; `lpcstory001`'s omission is reasoned |
| R1-L9 | wrong operative ground for Perpetua's exclusion | The 2026-08-26 ruling now named; Registry row 204 confirms *"Out-of-Boundary … by prior ruling"*, Excluded in both portions |
| R1-L10 | "the library… largely survived" | Gone; the chunk now says Possidius records the instruction, not the outcome |
| R1-L11 / R2-L13 | guard count typed / Round 1 credited with forcing later guards | Derived by AST; the masthead now says *"the guards that existed when it ran"* |
| R1-L12 | §7 item 4 argued only from Phase One | Albina and the Nuns of Hippo now named. Doc_02 §6 confirms both are known only through Augustine's framing |
| R1-C1 / R2-C1 | Tier 3 confidence trimmed without ellipsis | Restored; matches CF l. 261 |
| R1-C2 | merged across Pontius's *"said he"* | Restored; verified |
| R1-C3 | "Firmilian" for "Firmilian of Caesarea" | Corrected |
| R1-C5 | "the Perpetua material" for "sermons" | Corrected; Doc_05 §11 item 9 says *sermons* |
| R2-M2 | index said no review round had run | Derived from `Review-Artifacts/` |
| R2-M3 | index carried the retracted Tier-2 claim | Corrected |
| R2-M4 | `lpcstory007`'s Source field mis-glossed the span | Corrected and **true**: XXXI carries psalms/preaching/death/will/library; the siege is in XXVIII–XXX. Verified line by line |
| R2-M5 | `lpcstory002` tested two of CF's three markers | All three now addressed, marker one conceded |
| R2-M6 | §8 items 2 and 5 contradicted each other | Item 2 is now a placeholder |
| R2-M7 | gravity derivation polarity-blind | Shares `NEG_CLAUSE` |
| R2-M8 | §5 garbage rows on the alternative enumeration | Closed |
| R2-M9 | CF Tier 1 confidence clause trimmed | Restored; matches CF l. 253 |
| R2-L15 (main clause) | masthead overclaimed the §3 cross-check | Title, tier, confidence, gravities **and** source rows are now compared. *Gravities fails open — MEDIUM-5* |
| R3-M2 | Doc_09's Status and Document Log frozen at Round 1 | Log runs through the Round 4 fix pass. *Disposition half open — MEDIUM-3* |
| R3-M3 | Disposition filed the escalation in its retracted form | Withdrawn. *§2 not updated — MEDIUM-2* |
| R3-M4 | self-counted guard figure counted its own literal | AST walk; I reproduced both figures (13 vs naive 14) |
| R3-M6 | gravity derivation right only by accident | `.**` boundary added; I re-derived gravities from the declaration alone and got the same seven pairs |
| R3-M7 | Absent Story Note rollout skipped `lpcstory007` | It now has one. *The build-progress boilerplate inside the section remains — COSMETIC-3* |
| R3-M8 | `lpcstory005` and §7 item 3 on the lapsed women | Rewritten at Round 4 and correct. *Third site open — HIGH-1* |
| R3-L1 | Absent Story Notes rendered as setext H2 headings | Fixed — blank line before every `---`; checked all five |
| R3-L4 | index §3 still said "two" candidates | Now four |
| R4-H1 | `lpcstory006` on the *Acta* | Rewritten; Pontius's pointer verified at source. *Residue — MEDIUM-7* |
| R4-H2 | `lpcstory007` on the siege | Rewritten; all three Possidius quotations verified in XXVIII, English and Latin. *Residue — MEDIUM-8* |
| R4-H3 | `lpcstory005` on source loss | Rewritten; *Ep.* XXVI verified. *Third site — HIGH-1* |
| R4-M2 | §7 item 4's "searching the ashes" | Gone; now *"searches for his body and finds him alive"*, which is what the letter says |
| R4-M4 (first half) | §3 source-row test subtracted `rows_excluded` | Fixed and forced: §3 naming row 41 as `lpcstory006`'s source now halts |
| R4-M6 | `lpcstory007` said "the one scriptural phrase" | Corrected; both phrases now inside the argument |

### Partial — 3

| ID | What is closed | What is live |
|---|---|---|
| **R2-M1 / R3-M1 / R4-M1** — the closure record | The fix pass did **not** claim full closure this time, which is a real change and should be credited | The Decision Log says *"the MEDIUM/LOW/COSMETIC findings addressed here are **enumerated in the commit**."* Commit `a6a6be73`'s message enumerates H1, H2, H3, the closure count, the escalation and one generator defect. **It enumerates no MEDIUM below M4, no LOW and no COSMETIC.** M6 was fixed and appears in neither. See **MEDIUM-1** |
| **R4-M4** — §3 cross-check | source-row containment now halts on a disclaimed row (forced) | the **gravities** comparison still fails open: `if cgrav and cgrav != …` skips entirely when §3's Gravities cell carries no G-code. Reproduced. See **MEDIUM-5** |
| **R4-M5** — Document Log and Disposition | Document Log now runs to the Round 4 fix pass | The Disposition still says **"Both HIGH findings are claims this document made about its sources"** and describes Round 1's two. Four rounds have produced **six** HIGHs. See **MEDIUM-3** |

### Open — 31 distinct findings

| First raised | Carried at | Finding | Current site |
|---|---|---|---|
| R2-M10 | R3-M10, R4-M7 | build-process notices inside deployable Story Text | `lpcstory002` ×4, `003` ×2, `004` ×1, `007` ×1 — **four chunks, not five**. MEDIUM-9 |
| R2-L14 | R4-L12 | guard enumeration lists eight conditions under a derived count of 13 | `lpc_Story_Index.md` masthead. LOW-12 |
| R2-L16 | R3-L5, R4-L3 | *Ep.* LI dropped without a reason; `lpcstory001` rests on one locus | chunk 001 Source field notice. LOW-3 |
| R2-L17 | R3-L6, R4-L4 | "Tobias, who **buried** the dead" — Pontius says *"collected together those who were slain by the king and cast out"* | `lpcstory002` Story Text, l. 27. Verified at source. **Fourth round.** LOW-4 |
| R2-L18 | R3-L7, R4-L5 | *Ep.* LXVII called "Cyprian's own letter"; it is synodical | chunk 001 Source field **and** Tier Justification — both named sites live. **Fourth round.** LOW-5 |
| R3-L2 | R4-L1 | Absent Story Note precedes Usage Guidance | all six chunks that carry one; the L4 template orders it last. LOW-1 |
| R3-L3 | R4-L2 | Doc_09 §2's Tier 2 confidence line trims CF without ellipsis | Doc_09 l. 34; CF l. 257 continues *"The tradition is authentic; specific details and attributions carry Contested confidence."* LOW-2 |
| R3-L9 | R4-L6 | the tier reversal against Doc_02 §9 item 10 is unnamed | Doc_09 cites §9 item 10 at l. 13 and §8 item 3, both for the provisional-inventory fact only. LOW-6 |
| R3-L10 | R4-L7 | `lpcstory006` never engages CF's Tier 3 **genus** clause | chunk 006 Tier Justification; the string *"resting on collected tradition"* appears zero times in it. LOW-7 |
| R3-L11 | R4-L8 | review history keyed to artifact existence, not to a fix pass | reproduced: a one-word `Doc09_Round5_Review.md` makes the index say *"REVISED after Round 5 … this file is the Round 5 fix pass."* **It will fire on this review.** LOW-8 |
| R3-L12 | R4-L9 | confidence-band guard is substring-based | reproduced: `Not Documented` passes; index prints *"**Yes** — Not Documented"*. LOW-9 |
| R4-L10 | — | all-whitespace Phase cell passes the missing-phase guard | reproduced: blank Phase cell in the Master Table. LOW-10 |
| R4-L11 | — | the generated index nests a notice inside a notice | reproduced by running the generator's own `assert_coverage` over its own output. LOW-11 |
| R4-L13 | — | §6 item 2 quotes Registry row 41's wording without attributing it | Doc_09 §6 item 2. Verified against row 41. LOW-13 |
| R4-L14 | — | "Two facts close the chapter." They do not | `lpcstory007` l. 29; XXXI continues for ~25 more lines. LOW-14 |
| R4-L15 | — | duplicate story-id chunk files undetected | reproduced: *"Eight stories — Tier 1 (7)"*, two identical rows, no halt. LOW-15 |
| R4-M8 | — | the guard notice describes a method the script no longer uses | index masthead still ends *"Counted here with a grep over the script rather than from memory"*; the script parses the AST, and the notice's own sentence explains why a grep is wrong. MEDIUM-10 |
| R4-M9 | — | §7 item 3's claim carried into `lpcstory005`'s Usage Guidance | **HIGH-1** |
| R1-C4 | R3-C1, R4-C1 | index §1 Confidence cell for `lpcstory006` carries the full two-clause band | `lpc_Story_Index.md` §1. **Fourth round.** COSMETIC-1 |
| R3-C2 | R4-C2 | §8 item 2's placeholder rationale is not a fact | nothing cross-references §8 by item number. COSMETIC-2 |
| R3-C3 | R4-C3 | the `[ADDED … L8]` boilerplate repeated verbatim | now in **six** chunks. COSMETIC-3 |
| R3-C4 | R4-C4 | Tier 4 placement quotation drops CF's governing condition | Doc_09 §3.1; CF l. 267 continues *"when it is explicitly marked as reconstruction in the construction notes."* COSMETIC-4 |
| R3-C5 | R4-C5 | `global BANDS` declared inside the chunk loop | `gen_story_index.py` l. 87. COSMETIC-5 |
| *(new this round)* | — | eight further findings — see the findings section | MEDIUM-2, 4, 5, 6, 7, 8; LOW-16 to LOW-20; HIGH-2 |

**Totals against the four rounds: 44 distinct findings closed, 3 partial, 31 open.**

## 1.3 The honesty test

**The brief's account of the fix pass's claims is close but not exact, and the inexactness runs in the build's favour.**

- **Claimed and delivered:** H1, H2, H3 (all three verified at source), M2 ("the ashes"), M3 (the escalation, withdrawn — and the withdrawal is correct), M4's first half (the `rows_excluded` subtraction, forced).
- **Not claimed anywhere, and delivered:** **M6** — `lpcstory007`'s "one scriptural phrase". The brief says the pass claimed M6. It does not, in the Decision Log or in the commit. It fixed it silently. That is the opposite of the pattern this document has been criticised for, and it should be said.
- **Claimed and not delivered:** the Decision Log's closing sentence — *"the MEDIUM/LOW/COSMETIC findings addressed here are **enumerated in the commit**."* **There is no such enumeration.** The commit message names H1–H3, the closure count, the escalation and the generator regression. It names no LOW and no COSMETIC, and of the MEDIUMs only M1, M3 and M4. **MEDIUM-1.**
- **The refusal to claim full closure is real and is the single most improved thing about this pass.** Three rounds of "all findings addressed" have stopped. What replaced it is a pointer to an enumeration that does not exist — a smaller failure of the same kind, and a fixable one.

**Measured closure against Round 4's 32 actionable findings: 6 fully closed, 3 partial, 23 open.** The diff is 20 changed lines in Doc_09, 4–6 in each of three chunks, 8 in the index, 12 in the generator, plus the new 37-line script. That is the size of a six-finding pass, and six is what it is. **The pattern the last three rounds diagnosed holds exactly: every finding the reviewer argued at length was fixed; almost every one-line finding was not.** Four LOWs are now open for a fourth consecutive round (LOW-3, LOW-4, LOW-5, and R1-C4 at COSMETIC-1).

---

# Findings

## HIGH

### HIGH-1 — `lpcstory005`'s Usage Guidance asserts a silence the letter it is built on refutes, and cites as its authority the Doc_09 item that was rewritten last round to say the opposite

**Site.** `Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md`, **Usage Guidance**, l. 69. Live prose, no notice anywhere near it. Round 4 named this exact site as M9 and the fix pass did not visit it.

**What I found.** The field reads:

> *"Doc_09 §7 item 3 makes this the sharpest absence in the repository: the world's central first-phase crisis is documented entirely from the side of those who did not fail it, and **the nearest thing to a named lapsed person is a woman described in the third person by her brother as a grief he is enduring.**"*

Three things are wrong with that sentence, and they compound.

1. **Doc_09 §7 item 3 no longer says it.** Round 3 wrote *"the closest this corpus comes to a named lapsed person"*; Round 4's H3 struck it; the live §7 item 3 now says, in bold, **"The absence is of the lapsed voice, not of lapsed names."** The Usage Guidance cites §7 item 3 as authority for the proposition §7 item 3 exists to deny.
2. **The chunk's own Absent Story Note, two sections above, contradicts it** — it names Numeria and Candida and says this corpus *"names people whose standing after the persecution was in dispute, records what was argued about them."*
3. **The letter refutes it.** I read *Ep.* XX whole. Celerinus asks Lucian to *"remit **such a great sin** to those our sisters, **Numeria and Candida**"*, cites *"their repentance and the works which they have done towards our banished colleagues"*, and reports that *"their cause having been lately heard, the chief rulers commanded them in the meantime to remain as they are, until a bishop should be appointed."* He then defends **Candida** specifically — *"she gave gifts for herself that she might not sacrifice"*, *"I know, therefore, that she has not sacrificed."* **He offers no such defence of Numeria.** Numeria is a named woman whose sin is conceded, whose repentance and works are recorded, and whose case has been formally heard and adjourned. That is a named lapsed person with a history, four sentences from the passage the chunk quotes.

**Why this matters.** This is the defect class that has produced a HIGH in four of five rounds — a silence asserted about a source that the source refutes, **inside the very letter the chunk cites** — and it is in the field that governs what the Representative is permitted to say. Article 20's secondary duty is explicit that *"absence of evidence is never itself evidence of content"*; here a documented presence is being reported as an absence. A participant who read *Epistle* XX could catch it. And the mechanism is the documented one: Round 4 argued H3 at length and named M9 in four lines; the pass fixed the two sites in the argument and skipped the one in the line.

**Fix.** Replace the clause with the corrected §7 item 3's own form: *"…and the named women whose standing was disputed — Numeria and Candida — are discussed, weighed and dispatched to peace by two men writing to each other. Not one of them speaks."* That is both true and sharper, and it makes the Usage Guidance agree with the Absent Story Note eight lines above it.

### HIGH-2 — `notice_strip.py`'s `live()` deletes every live assertion that follows an inline notice in the same paragraph, and silently discards half of Doc_09 §7 and all of §2's escalation paragraph

**Site.** `scripts/notice_strip.py`, `_HEADING` and `live()`. New this round, never reviewed.

**What I found.** `live()` applies `_HEADING` first. `_HEADING` is

```
\*\*[^*\n]{0,120}\[(TAG)\b[^\]]*?\]\*\*.*?(?=\n\n|\Z)
```

The prefix `[^*\n]{0,120}` matches **zero** characters, so the pattern fires on an **ordinary inline notice** `**[CORRECTED …]**` as readily as on the heading form it was written for — and then `.*?(?=\n\n|\Z)` **consumes everything to the end of the paragraph**. In this build's Markdown, one paragraph is one line, so that is the rest of the item.

Reproduced on constructed input:

```
Alpha asserts something live. **[CORRECTED … :** the old text said X.**]** Beta asserts something live and uncorrected.
→ live() == "Alpha asserts something live."     # "Beta …" is gone
```

Reproduced on the deliverables:

- **Doc_09 §7:** 853 words in, **444 out** — 48% deleted. Every one of these live sentences disappears: *"They are discussed, vouched for and dispatched to peace…"*, *"The world's most consequential formation question is documented exclusively from the side of those who did not fail it."*, *"Numeria and Candida are discussed, weighed, and dispatched to peace by two men…"*, *"The absence is not an artefact of Cyprian's corpus. It holds across both phases and 180 years."*, *"no woman in this world's horizon left a narrative of her own."*
- **Doc_09 §2's escalation paragraph** — 460 words, the paragraph that states what is escalated and where it is routed — **`live()` returns a single space.**

**Why this matters.** This script exists for one purpose: to decide, in a closure audit, whether a phrase is *mention* or *use*. Over-stripping makes live prose look like mention. **That is the exact false conclusion that lets an open finding be recorded as closed** — the failure this document has committed three rounds running, now available as a one-line library call. It is worse than the ad-hoc sweeps it replaces, because those erred toward false positives (reporting fixed things as unfixed), which cost a reviewer time; this errs toward false negatives, which cost a reader the truth. And the §2 paragraph it erases whole is the one carrying MEDIUM-2 below — a contradiction the fix pass did not catch.

The docstring's own framing is the trap: it says *"A pattern that only matches `**[TAG …]**` leaves that trailing prose live"* and treats trailing prose as always notice. Trailing prose after a **heading-form** notice is narration of the error; trailing prose after an **inline** notice is the document continuing.

**Fix.** Require the heading form to be distinguishable from the inline form — the heading form has **non-empty, non-bracket** prose before the `[`:

```python
_HEADING = re.compile(r"\*\*[^*\n\[]{1,120}\[(?:" + TAGS + r")\b[^\]]*?\]\*\*.*?(?=\n\n|\Z)", re.S)
```

and run `_INLINE` **first** so inline notices are consumed before `_HEADING` can reach them. Then add the two cases in LOW-17 below. And add a regression test that asserts `live(Doc_09 §7)` retains a known live sentence — the script has no tests at all.

---

## MEDIUM

### MEDIUM-1 — the fix pass points at an enumeration that does not exist

**Site.** `lpc_Decision_Log.md`, Round 4 entry, final sentence; commit `a6a6be73`.

**What I found.** *"The closure count for this pass is stated where it can be checked: 3 HIGH, and the MEDIUM/LOW/COSMETIC findings addressed here are enumerated in the commit; the remainder are carried openly rather than certified closed."* The commit message enumerates H1, H2, H3, the false closure claim, the withdrawn escalation and the row-containment regression. **No LOW is named. No COSMETIC is named. Of nine MEDIUMs, three.** M6 was fixed and is named in neither place.

**Why this matters.** The pass deliberately stopped claiming blanket closure — genuinely the right move, and I want to credit it. It then replaced the false claim with a pointer to a record that is not there, which means the next round still has to re-derive the ledger from scratch, as I did and as Rounds 2, 3 and 4 each did. Four rounds have now spent their first hours on the same bookkeeping.

**Fix.** Either enumerate by ID in the Decision Log entry — six lines — or delete the clause and say *"six findings closed; the rest are carried open and unlisted."* The second is honest and costs nothing.

### MEDIUM-2 — Doc_09 §2 still routes the escalation the Disposition withdrew, eight pages away in the same document

**Site.** Doc_09 §2, the paragraph beginning *"That rule is this build's construction…"*, against the Disposition's escalation block.

**What I found.** §2 says, in live prose: *"it is **escalated** rather than asserted"* … *"That narrower question is **what is escalated**"* … *"**Routed to the project lead** as a governance/methodology item **at the Disposition**."* The Disposition says: *"**WITHDRAWN at Round 4**"* … *"**Nothing is escalated here**, and the pattern is recorded instead."*

**Why this matters.** This is Round 3's M3 with the files swapped — then the Disposition filed what §2 had retracted; now §2 files what the Disposition has withdrawn. §2 explicitly directs the reader to the Disposition for the filing, and the Disposition says there is none. **This is also the paragraph `notice_strip.py` erases entirely (HIGH-2)**, which is the likeliest reason a closure sweep did not see it: the tool built to find exactly this kind of residue deleted the evidence.

**Fix.** Rewrite §2's final three sentences to record the construction and its withdrawal: *"This rule was escalated three times and withdrawn at Round 4, on the ground that CF classifies stories rather than sources; the Disposition records the withdrawal."*

### MEDIUM-3 — the Disposition still recites Round 1's two HIGHs as though they were the document's HIGH record

**Site.** Doc_09, Disposition, second paragraph. Round 4's M5, second half.

**What I found.** *"**Both HIGH findings** are claims this document made *about* its sources: a silence asserted in Pontius that his §10 does not contain, and two quotations altered in transcription."* Those are Round 1's H1 and H2. Since then: Round 3's HIGH-1 (*Ep.* XXXIV), and Round 4's H1, H2 and H3. **Six HIGHs, of which the Disposition describes two**, in the paragraph a reader consults to learn what has gone wrong with this document. The sentence immediately above it correctly lists all four rounds' counts, so the document contradicts itself within four lines.

**Why this matters.** It understates the record by two thirds at the one place the record is summarised, and it does so in the direction that flatters the build.

**Fix.** *"Six HIGH findings across four rounds, and all six are one defect: a silence asserted about a source that the source refutes. Four of the six were in fields that instruct the Representative."*

### MEDIUM-4 — the committed index credits `lpcstory003` with two Latin rows the chunk has not opened, under a paragraph asserting every listed row is one the story "actually draws on"

**Site.** `lpc_Story_Index.md` §4, row `lpcstory003`. **This is a live defect in committed output, not a mutation.** Found by no previous round.

**What I found.** §4 prints:

`| lpcstory003 | 1, 191, 194 | row 1: Native, row 191: Native, row 194: Native |`

under the heading **"Registry row(s) cited"** and the claim **"Every row a story *actually draws on* is Native."** The chunk's Source field reads: *"…(`Source_Registry.md` row 1; vendored in English at `anf05`). **Latin second witness at rows 191/194.**"* That is a statement of what exists, not of what was used — and **Doc_09 §8 item 6 says the Latin check is still pending**: *"pending a check of the ANF parenthesis against the Latin at rows 191/194."* The chunk draws on row 1 only.

Doc_09 §3's own Source cell for `lpcstory003` says *"(row 1)"* — one row where the index says three — and nothing compares in that direction, because the containment test is one-directional (`csrc_rows - _used - _excl`).

**Why this matters.** It is Round 1's M4(c) exactly: **a row named for a reason other than use, credited as use, and then vouched for.** `NEG_CLAUSE` catches *"has not been read"* and misses *"second witness"*, *"pending"*, *"available"*. Fixing an instance and not the class is the shape this build has repeated at M4(c) → M7 → M4 → here.

**Fix.** Either add an explicit availability vocabulary to the polarity split (`second witness`, `pending`, `available`, `where no English`), or — better and structural — require a chunk to state *drawn-on* rows in a dedicated `Rows:` front-matter field and leave prose out of the derivation entirely. And make the §3 row comparison symmetric so a §3 cell that under-names halts too.

### MEDIUM-5 — two bypasses of the boundary guard, and a fail-open in the gravities comparison; none is caught by any of the 13 halting sites

**Site.** `gen_story_index.py` ll. 104–107 (row extraction), ll. 174–178 (gravities comparison). All three reproduced from fresh copies.

**What I found.**

1. **Case-sensitive row extraction.** `re.findall(r"row(?:s)?\s+…", clause)` carries no `IGNORECASE`. A Source field sentence that *begins* with a row citation — *"Row 28 supplies the acclamation formula used above."* — is **invisible to every derivation**. Forced: rc 0, and §4 prints `| lpcstory004 | 1 | row 1: Native |` with no trace of row 28, under *"The check is mechanical: the row number is read from each chunk's own Source field."* The same chunk with a lowercase `row 28` halts correctly: *"FATAL: story source row(s) ['28'] are not Native."* **The only thing standing between a boundary breach and the guard is a capital letter at the start of a sentence.** Round 4's own second defective check was a case-sensitivity miss in its harness; nobody looked for the same class in the committed script.
2. **Incidental negation demotes a used row.** *"row 28 supplies the acclamation formula, which the Registry does not otherwise license."* — one clause, one `does not`, and row 28 is filed as *"named but explicitly not used"* and never boundary-checked. Forced: rc 0, §4 prints `1 · *named but explicitly not used: 28*`.
3. **Gravities comparison fails open.** `if cgrav and cgrav != set(s["gravities"])` — a §3 Gravities cell with no G-code (`—`, `none`, `TBD`) skips the comparison entirely. Forced: rc 0, Master Table prints the chunk's gravities as though §3 had agreed. This is the surviving half of Round 4's M4, *"the §3 cross-check's two new comparisons both fail open"* — the source half was fixed and this one was not.

**Why this matters.** §4's standing claim is *"No story draws on an Excluded row… The check is mechanical."* Two of the three ways that claim can be false are in the committed script, and the third leaves a masthead claim of full-table agreement untrue.

**Fix.** `re.IGNORECASE` on the row pattern; split the Source field into clauses at sentence boundaries **and** require the negation to govern the row's own clause rather than the sentence; and make an empty §3 Gravities cell a halt rather than a skip.

### MEDIUM-6 — `lpcstory002`'s Usage Guidance closes by denying what the chunk's own §10 quotation says

**Site.** `lpcstory002`, Usage Guidance, final sentence. Round 1's H1 at a third site in the same chunk.

**What I found.** The field ends: *"The specific thing Cyprian is reported to have asked for is narrower and harder: not care for the sick generally, but care for **the people persecuting them**. If a participant asks whether that happened, the answer is that **this world's own record does not say.**"*

Pontius §10 — which the same chunk quotes twice, once calling it *"the clause that answers the sermon directly"* — reads: *"Thus what is good was done in the liberality of overflowing works **to all men, not to those only who are of the household of faith**."* I read §§9–11 whole. §9's address is explicitly about *"those that persecute him"*; §10's result clause is Pontius's answer to it.

**Why this matters.** The chunk says three times that Pontius *does* answer, in the Story Text, the Tier Justification and the first half of this very field, and then closes by telling the Representative the record is silent. Whichever reading is right, the chunk cannot hold both, and the one a Representative will act on is the last sentence of the Usage Guidance.

**I am not grading this HIGH**, and the reason is worth stating: Pontius says *"to all men"*, not *"to their persecutors"*. The narrow question is genuinely unanswered. What is defective is the flat form of the denial and its collision with the chunk's own finding.

**Fix.** *"If a participant asks whether that happened, the answer is what Pontius records — that relief went 'to all men, not to those only who are of the household of faith' — and that he does not say whether any of those men were the persecutors the address named."*

### MEDIUM-7 — `lpcstory006`'s Absent Story Note characterises the *Acta* again, in the opposite direction, and the *Acta* is on this build's own disk

**Site.** `lpcstory006`, Absent Story Note, first paragraph — the paragraph Round 4's H1 did **not** rewrite.

**What I found.** *"not one of them left a word — **no bystander account, hostile or sympathetic, survives from anyone in that clearing who was not writing as a member of Cyprian's own church.**"*

Two paragraphs later the note says the *Acta Proconsularia* exists, is vendored at rows 41 and 194, and is unread. The chunk's **Source field** calls it *"the strictly documentary witness"* to Cyprian's death; Doc_09 §6 item 2 calls it *"the one strictly documentary (as opposed to hagiographic)"* record. **Those statements and the sentence above cannot both be true**: a strictly documentary court record of the death is, by the chunk's own description, not a document written from inside Cyprian's church.

**I opened it.** Row 194's file — `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` — is vendored, and the *Acta* begins at l. 41413. It records the clearing in detail: *"multa turba conuenit ad Sexti"*; *"turba fratrum dicebat: et nos cum ipso decollemur"*; *"multa turba eum prosecuta est"*; *"in agrum Sexti productus est et ibi se bicerna byrro expoliauit et genu in terra flexit"*; the twenty-five gold pieces paid to the executioner; the two Juliani who tied the blindfold when Cyprian could not; and *"eiusque corpus propter **gentilium curiositatem** in proximo positum est"* — the body placed nearby because of the **pagans'** curiosity. It carries details Pontius does not, and it names a pagan audience.

**Why this matters.** For the fourth consecutive round, `lpcstory006`'s Absent Story Note makes a claim about what the *Acta* does or does not contain **without opening it**, while the file sits in the corpus. The direction changes; the operation does not.

**I am not grading this HIGH**, and the reason is worth stating: the transmitted *Acta* is a composite whose narrative frame is Christian (*"turba fratrum"*), so *"no bystander account from anyone not writing as a member of Cyprian's own church"* may survive scrutiny on its merits. **But this build cannot know that**, because it has not read the text, and the sentence asserts it as settled.

**Fix.** Two lines. Either narrow to what is certain — *"no one in that crowd left an account of their own"* — or, better, spend an hour on ll. 41413–41629 and close Doc_09 §8 item 1, which the document itself calls *"the single largest available improvement to this document."* It is 200 lines of Latin, and `INTAKE.md` already licenses it.

### MEDIUM-8 — `lpcstory007`'s rewritten Absent Story Note re-asserts an absolute negative one sentence after quoting the source that answers it

**Site.** `lpcstory007`, Absent Story Note, third paragraph.

**What I found.** *"…no one who fled Hippo wrote down what leaving was like, and **no source in this corpus records what became of the people Augustine had served for thirty-five years.**"* The paragraph immediately above quotes Possidius saying congregations were *"despoiled and stripped of all their goods and begging in abject poverty"* and that Hippo was *"**abandoned by its inhabitants**, was burned by the enemy."*

**Why this matters.** The first clause — nobody wrote down what leaving was like — is true and is the right finding. The second is the Round 4 H2 operation at reduced amplitude: an absolute *"no source records"* placed one sentence after the quotation that partly records it. The note's own closing line, *"The scale is documented. The experience is not,"* is the correct statement and makes the middle clause unnecessary.

**Fix.** Delete the clause. The paragraph reads better and truer without it.

### MEDIUM-9 — build-process notices inside deployable Story Text, open for a fourth round

**Site.** `lpcstory002` (four), `lpcstory003` (two), `lpcstory004` (one), `lpcstory007` (one). Round 2's M10, Round 3's M10, Round 4's M7.

**What I found.** `lpcstory002`'s Story Text carries roughly 190 words of correction apparatus, including a 90-word block about which section of Pontius an earlier draft had not read. **Round 4 said "five chunks"; it is four** — `lpcstory005` and `lpcstory006` carry none.

**Why this matters.** Story Text is the field Doc_10 consumes as deployable narrative. A chunk whose narrative is 30% build history is not deployable without an editorial pass nobody has scheduled. Three rounds have asked; the generator has no guard, and it is the one place a guard would pay for itself.

**Fix.** Move every notice out of `## Story Text` into `## Tier Justification`, and add a fourteenth halting site: a notice inside Story Text is FATAL.

### MEDIUM-10 — the index's guard notice describes a method the script abandoned, in the sentence that explains why the method was wrong

**Site.** `lpc_Story_Index.md` masthead, final clause. Round 4's M8.

**What I found.** The notice ends *"Counted here with a grep over the script rather than from memory."* The script counts by AST walk. The same notice, four clauses earlier, explains that *"a count derived from a script's own source text is a literal in disguise"* — which is exactly what a grep is.

**Why this matters.** The masthead's own declared standing is *"Hard-coded prose, re-verified by nothing."* This is that class, and it now describes the defect as the remedy.

**Fix.** *"Counted off this script's syntax tree, which cannot see its own counting expression."*

---

## LOW

**LOW-1** *(R3-L2, R4-L1)* — **The Absent Story Note precedes Usage Guidance in all six chunks that carry one.** `L4-Templates/Story_Repository_Chunk_Template.md` orders it last, after Source Identification. *Fix:* move it, or record the deviation once in Doc_09.

**LOW-2** *(R3-L3, R4-L2)* — **Doc_09 §2's Tier 2 confidence line trims CF without ellipsis**, in the section whose masthead says *"the confidence bands are its own too."* CF l. 257 continues *"The tradition is authentic; specific details and attributions carry Contested confidence."* Consequence: `BANDS["2"]` inherits the truncation and would halt on a Tier 2 chunk following CF exactly.

**LOW-3** *(R2-L16, R3-L5, R4-L3)* — ***Ep.* LI was dropped from `lpcstory001` without a reason.** The notice explains why XXXIII went and is silent on LI, which Round 1 verified as sound. Fourth round. *Fix:* restore LI or XXXII, or say why one locus suffices.

**LOW-4** *(R2-L17, R3-L6, R4-L4)* — **"Tobias, who *buried* the dead of 'his own race only.'"** Pontius §10: *"Tobias **collected together those who were slain by the king and cast out**, of his own race only."* Verified at source; live text, not in a notice. Fourth round.

**LOW-5** *(R2-L18, R3-L7, R4-L5)* — ***Ep.* LXVII described as "Cyprian's own letter" at both sites** — the Source field (*"Cyprian's own letter on episcopal election"*) and the Tier Justification (*"In *Ep.* LXVII **Cyprian argues**"*). It is synodical: Cyprian and thirty-six named colleagues. Naming it correctly makes the corroboration **stronger** — *"by the suffrage of the whole brotherhood"* then reports a synod attesting a shared practice. Fourth round, in the chunk set where `lpcstory005` gives attribution discipline a section of its own.

**LOW-6** *(R3-L9, R4-L6)* — **The tier reversal against Doc_02 §9 item 10 is still unnamed.** Doc_02 describes Pontius *"in terms matching the Framework's own **Tier 3** definition"*; Doc_09 assigns him Tier 1 for two of three stories and cites §9 item 10 twice, both times for the provisional-inventory fact only. *Fix:* name it in §2, where the per-story rule is stated.

**LOW-7** *(R3-L10, R4-L7)* — **`lpcstory006`'s Tier 3 argument never engages CF's genus clause.** CF l. 260 opens Tier 3 with *"resting on collected tradition rather than direct documentation."* Pontius is direct documentation by a named eyewitness. The string appears zero times in the chunk. This is the strongest available argument *against* the tier the chunk assigns, and the template asks for tier disagreement at full strength.

**LOW-8** *(R3-L11, R4-L8)* — **The review-history derivation keys on artifact existence, not on a fix pass.** Reproduced: a one-word `Doc09_Round5_Review.md` in a scratch copy makes the generator emit *"REVISED after Round 5 … this file is the Round 5 fix pass and is unreviewed."* **It will fire the moment this file lands.** *Fix:* derive the round count from the artifacts and the fix-pass claim from a marker the fix pass writes into Doc_09's Document Log, which the script already reads.

**LOW-9** *(R3-L12, R4-L9)* — **The confidence-band guard is substring-based.** Reproduced: a Tier 1 chunk declaring **"Not Documented"** passes, and the No-Tier-5 audit prints *"**Yes** — Not Documented."*

**LOW-10** *(R4-L10)* — **An all-whitespace Phase cell passes the missing-phase guard.** Reproduced: `| G1, G3 |   |` yields `phase_of["lpcstory001"] == ""` and a blank Phase cell in the Master Table, under a comment claiming *"a missing value is reported rather than inferred."*

**LOW-11** *(R4-L11)* — **The generated index nests a notice inside a notice.** Reproduced by running the generator's own `assert_coverage` over `lpc_Story_Index.md`: one swallowing notice at the masthead — the condition that makes the script exit FATAL on a chunk, in the file that exemplifies the discipline.

**LOW-12** *(R2-L14, R4-L12)* — **The guard enumeration lists eight conditions under a derived count of 13.** Unlisted: no front-matter fence; a surviving notice-like opener; no chunk files; no transmission phase in §3. Third round.

**LOW-13** *(R4-L13)* — **Doc_09 §6 item 2 quotes *"the one strictly documentary (as opposed to hagiographic)"* without saying who said it.** It is `Source_Registry.md` row 41's own wording; as printed it reads as scholarship about the *Acta*.

**LOW-14** *(R4-L14)* — **"Two facts close the chapter." They do not.** The will and the library instruction sit mid-chapter; XXXI continues with the church's possessions, Augustine's relatives, the clergy and monasteries, the secular poet's epitaph and Possidius's closing prayer. Third correction to this chunk's placement of material within XXXI, unfixed.

**LOW-15** *(R4-L15)* — **Duplicate story-id chunk files are not detected.** Reproduced: copying `lpcstory001_election-of-cyprian.md` to `lpcstory001_dup.md` yields *"Eight stories — Tier 1 (7)"* with two identical rows and no halt.

**LOW-16** *(new)* — **`lpcstory006`'s Absent Story Note quotes Pontius §11 without saying so, and §11 is outside the span the chunk declares.** The Source field says §§15–19; *"what God's priest replied to the interrogation of the proconsul, there are Acts which relate"* is at **§11**, where Pontius is describing the **banishment** hearing of 257, not the capital trial of 258. The quotation is exact and the pointer is real — the *Acta* covers both proceedings — but a reader told only *"Pontius himself points the reader to it"* cannot check it, and the chunk has now been corrected twice for placing material outside its cited span. *Fix:* cite §11 and say which proceeding it describes.

**LOW-17** *(new)* — **`notice_strip.py` under-strips in three ways, each leaving correction prose standing as a live assertion.** All reproduced:
 - an **italic in the heading prefix** (`**First, the *ANF* reading. [CORRECTED …]**`) defeats `_HEADING` (`[^*\n]` cannot cross `*`); `_INLINE` removes the bracket and leaves the error-quoting prose live;
 - a **prefix longer than 120 characters** does the same;
 - a **`]` anywhere inside the notice prose** — a `[sic]`, a Markdown link, a bracketed gloss — defeats **both** patterns (`[^\]]*?`), leaving the entire notice standing as live text.
 The build's notices already contain italics routinely; the first case is a live hazard, not a hypothetical one. *Fix:* allow `*` in the prefix but exclude `[`; drop the length cap or raise it; and match the notice body with a `(?:[^\]]|\](?!\*\*))*?` form that stops only at a closing `]**`.

**LOW-18** *(new)* — **"One stripper, shared" is not shared, and the two disagree.** `gen_story_index.py` keeps its own line-scoped `NOTICE`/`strip_notices` and does not import `notice_strip`. On Doc_09 §7 the generator's stripper yields **672** words and `notice_strip.live()` yields **444** — a 34% divergence; on the §2 escalation paragraph the generator keeps every sentence and `live()` keeps none. Two strippers with different answers is the condition the new file was written to end. *Fix:* after HIGH-2 is fixed, have the generator import `live()` and delete its local copy, or state plainly that the two have different jobs and why.

**LOW-19** *(new)* — **`lpcstory007`'s Story Text drops the quotation marks its own Tier Justification depends on.** Weiskotten prints *"he slept with his fathers," as it is written, "well-nourished in a good old age."* — the scriptural phrases marked as quotations. The Story Text renders the sentence as one continuous quotation with the inner marks removed; the Tier Justification then argues that these phrases *"are flagged in his own text as quotations"* and that this is what keeps them epitaph rather than pattern. The argument is right and the evidence for it has been silently deleted from the passage above it. *Fix:* restore the inner marks.

**LOW-20** *(new)* — **The §3 source-row comparison is one-directional.** Doc_09 §3 may name **fewer** rows than the chunk with no halt, which is how MEDIUM-4's divergence (§3: row 1; index: rows 1, 191, 194) sits in committed output uncaught. *Fix:* compare the sets both ways, or state in the masthead that §3's Source column is checked for containment only.

---

## COSMETIC

**COSMETIC-1** *(R1-C4, R3-C1, R4-C1)* — `lpc_Story_Index.md` §1's Confidence cell for `lpcstory006` still carries the full two-clause band, making the master table unscannable at the one row a reader most wants to scan. **Fourth round.**

**COSMETIC-2** *(R3-C2, R4-C2)* — Doc_09 §8 item 2's placeholder is justified *"so the list's own cross-references do not shift."* I grepped the world build: nothing cross-references §8 by item number. The placeholder is harmless; the reason given for it is not a fact.

**COSMETIC-3** *(R3-C3, R4-C3)* — The `[ADDED … Round 1's L8]` boilerplate is now repeated verbatim in **six** chunks, inside the Absent Story Note — the section the template reserves for evidentiary absence, carrying a build-progress statement instead. One statement of a rollout decision belongs in Doc_09.

**COSMETIC-4** *(R3-C4, R4-C4)* — Doc_09 §3.1 quotes CF's Tier 4 placement rule as *"is appropriate in world documents (particularly ecological reconstruction sections)."* with the period inside, dropping CF l. 267's governing continuation *"**when it is explicitly marked as reconstruction in the construction notes**."* The condition is the operative half, and it is the half that licenses this document's placement decision.

**COSMETIC-5** *(R3-C5, R4-C5)* — `gen_story_index.py` l. 87 declares `global BANDS` inside the chunk loop and rebuilds the dict each iteration; `BANDS` is undefined if the loop body never runs and is read again at l. 315.

**COSMETIC-6** *(new — a premise of this round's brief, recorded as directed)* — **"Roughly 100 findings" matches neither count.** Raw across the four rounds: **121** (27 + 33 + 28 + 33). Distinct, collapsing carried repeats: **78**. The brief's second checkable premise about the fix pass's claims is also slightly wrong in the build's favour — see §1.3; **M6 was fixed without being claimed.** The brief's third premise, about `notice_strip.py`'s "one known limitation", is wrong and is recorded in the check-confirmation section below.

---

# Is the deliverable adequate to proceed to Doc_10?

**Not quite as it stands. Yes after a fix pass of about twenty lines — and the fix list is now genuinely short.**

**What is ready, stated at the strength it has, and verified independently for a fifth time.** Seven stories, seven real texts, every one opened. Every quotation in every chunk and in Doc_09 resolves to **body text of the cited work** — zero inside a `<note>`, zero inside an ANF *Argument* except `lpcstory004`'s deliberate exclusion quotation. **No invented participant, event or outcome anywhere in any Story Text.** Both of the build's own evidentiary claims survive direct checking again: the Argument/body distinction at `lpcstory004`, and the attribution of *Epp.* XX–XXI away from Cyprian. The tier work is textual rather than convenient, and the `lpcstory006`/`lpcstory007` pair remains the best-made thing in the repository. The index regenerates **byte-identical** from its committed script, and my own independent derivation of every number in it — seven stories, 6/0/1/0, seven gravity pairs, five absences, 672 words — agrees at every field. All thirteen halting sites fire.

**And the thing this round was called to test has passed.** The three rewritten Absent Story Notes carry four positive source claims between them, and **all four are true**, verified twice each. No over-correction. That was the predicted next failure and it did not happen.

**What is not ready is what was not ready last round: the instruction layer.** Step 10 is Representative Emergence, and Usage Guidance and Absent Story Notes are where this document tells a Representative what it may not say. **Three of those fields still assert absences the sources do not support** — `lpcstory005`'s Usage Guidance (HIGH-1, refuted by the letter the chunk is built on), `lpcstory002`'s (MEDIUM-6, contradicted by the chunk's own quotation), `lpcstory006`'s (MEDIUM-7, a claim about a source on this build's own disk). Article 20 makes an absence's stated cause a participant-facing obligation, and provides that *"absence of evidence is never itself evidence of content."* Doc_10 will inherit these fields verbatim.

**The one thing I would not carry into Doc_10 unfixed is HIGH-1**, for the same reason Rounds 1, 3 and 4 each gave about their own: it is a false statement about a source sitting in the field that governs what the Representative reaches for, and it is one sentence.

**HIGH-2 does not block Doc_10** — it is a build tool — but it should be fixed **before the next fix pass runs**, because the next fix pass will use it to decide what is closed.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** No identity, title or voice decision is made here. Noted separately and not as an escalation: three deployable retrieval fields rest on false or self-contradicting claims about their sources (HIGH-1, MEDIUM-6, MEDIUM-7), and build apparatus still sits inside four chunks' deployable Story Text (MEDIUM-9). All are content defects within this document's own gift to fix.

- **Portfolio-level or cross-world — two items, both inherited, and the second has a fourth and fifth instance.**
 1. *The corpus-wide editorial-apparatus item.* Re-verified independently for the fifth time and still the ledger's first **positive** instance: of every quotation in seven chunks and Doc_09, zero resolve inside a `<note>` and zero inside an ANF *Argument* except the one quoted in order to exclude it. Pontius's *Life* carries no *Argument* paragraph at all. Carry forward unchanged.
 2. *The index-generator-as-build-artifact item (Doc_08 R5; Doc_09 R1-M4c, R2-M7, R3-M4, R4-M4).* **Two new instances, and the second names a sub-class the previous four did not.** MEDIUM-4 is a derivation that reads the right field and cannot tell *availability* from *use* — the fifth appearance of polarity-blindness, and the first that is **live in committed output** rather than latent. MEDIUM-5 is new in kind: **a guard defeated by orthography.** A capital letter at the start of a sentence makes a Registry row invisible to every derivation in the script, including the boundary guard whose output is printed as *"the check is mechanical."* Every sibling world's story index will scrape Source prose the same way. **Route with the sub-class attached: a derivation that reads prose inherits prose's variability, and the remedy is a declared field, not a better regex.**
 **Worth attaching as a third:** HIGH-2. This build has now written *four* notice-strippers across two documents — three ad hoc, one shared — and the shared one is the first to produce **false negatives**. A notice grammar that must be recognised by regex at all is the portfolio-level problem; a delimiter the tooling can rely on (a fenced block, an HTML comment, a footnote reference) would end the class.

- **Governance or methodology — the withdrawal is CORRECT, and I checked it rather than accepting it. But the Disposition overstates what the withdrawal disposes of, and the document contradicts itself about whether anything is filed.**

 **The withdrawal is right.** I read CF V7.4 ll. 247–271 whole. l. 249: *"transparent classification of where on that spectrum **each story** sits."* l. 250: *"The four-tier **story** classification framework."* l. 271: *"a working catalog of **stories** available within the world, classified by tier."* Step 9, l. 699: *"a complete catalog of all formation **stories** with final tier classifications."* **CF classifies stories.** Splitting Pontius across tiers story by story is what the framework prescribes, not a departure from it. **The escalation as filed at Round 3 was correctly withdrawn, and a build thread that withdraws its own escalation after checking the governing text is doing the right thing in the right order.** I looked for a reason to reinstate it and did not find one.

 **Two qualifications, and the second is a finding.**

 1. **A distinct question survives, and it is not the one that was withdrawn.** CF's Tier 3 opens with a **genus**: *"Material attributed to specific figures or moments but **resting on collected tradition rather than direct documentation**."* Hagiographic narrative is *"a specific type within this tier."* Pontius is direct documentation by a named eyewitness deacon — so `lpcstory006` is placed in a tier whose genus clause excludes it, on the strength of a sub-clause inside that genus. **That is a real ambiguity in CF and it decides this document's only Tier 3 assignment.** It is not answered by "CF classifies stories, not sources," because it is not a question about sources. It has never been filed in this form; LOW-7 records that the chunk does not engage it. **I am not filing it as a seventh escalation** — the honest first step is the one Doc_09 §8 item 1 already names: **read the *Acta*.** It is vendored, it is 200 lines of Latin at `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` l. 41413, `INTAKE.md` licenses it, and reading it would very likely move `lpcstory006` to Tier 1 and make the question moot. If after reading it the tier stays at 3, **then** file the genus question, in those words.
 2. **The document does not agree with itself about the withdrawal.** §2 says in live prose that the question *"is escalated"* and is *"routed to the project lead… at the Disposition"*; the Disposition says *"WITHDRAWN"* and *"Nothing is escalated here."* **MEDIUM-2.** This is Round 3's M3 with the files swapped, and the paragraph carrying it is the one the build's own new stripper deletes entirely — which is a fair summary of how these two findings are connected.

 **A methodology observation I raise rather than escalate**, repeating Rounds 2, 3 and 4 because the mechanism has now been identified three times and not acted on: *a finding is closed only when every site it names has been visited.* Applying that convention alone would have closed LOW-3, LOW-4, LOW-5, COSMETIC-1 and HIGH-1 in this pass. **HIGH-1 is the cost of not applying it**, and it is the fifth round in which the same mechanism has produced the round's worst finding.

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. §6 item 4 and §8 item 4 state it accurately.

---

# Check confirmation — my own harnesses, including the two that were wrong

**Thirty-odd failing checks in this build have turned out to be defects in the check, and every reviewer in this sequence has had at least one.** I had two. I record them before the findings that survived.

## Defective checks of my own (both caught before reporting)

**Defective check 1 — the Weiskotten trap, fifth round running, in a new form.** My first Possidius sweep reported `"as they hung upon the wall and read them; and he wept freely and constantly"` **absent**. It is present, at XXXI. My harness already handled the two failure modes Round 4 documented — page-break insertion and end-of-line hyphenation — and was defeated by a **third**: Weiskotten prints `read them ; and he wept`, with a space before the semicolon, a 1919 typesetting convention my whitespace normaliser collapsed into a mismatch. Had I reported it, it would have been a fabricated quotation finding against the chunk whose quotations are the cleanest in the set. Fixed by dropping spaces before punctuation in both harnesses, and re-confirmed at word level with all punctuation stripped.

**Defective check 2 — raw-XML search against a hard-wrapped file.** When confirming the three rewritten notes a second way, I searched `cyprian.xml` directly for `"there are Acts which relate"` and `"I know, therefore, that she has not sacrificed"` and got **-1 for both**, then compounded it: `x[max(0,-3000):-1]` silently returns the whole document, so my paragraph-id probe reported both strings as living in `iv.vii.vi-p19`, a section neither is in. Both strings are present; the XML wraps them across source lines, which a raw `find` cannot cross. **A miss and a spurious location from the same bug** — and the spurious location, had I trusted it, would have supported a fabricated "quotation taken from the wrong work" finding against both rewritten notes. Confirmed properly through the marked stream, which whitespace-normalises.

## Confirmations, one for every finding that rests on a failing check

**Confirmation 1 — the index is genuinely derived and genuinely current.** Copied the world tree to a clean directory, ran the committed `gen_story_index.py`, diffed against the committed `lpc_Story_Index.md`: **byte-identical**.

**Confirmation 2 — the index is right, checked against a derivation that shares no code with it.** My own parser, my own gravity rule (the explicit `**Gravities:**` declaration only, ignoring `Retrieve-When`), my own §7 parser: seven stories; tiers 6/0/1/0; `001` G1,G3 · `002` G1,G4 · `003` G1,G6 · `004` G1,G3 · `005` G2,G8 · `006` G1,G8 · `007` G1,G2; five enumerated absences; **672 words**. Every value matches the committed index.

**Confirmation 3 — thirteen halting sites, all forced.** AST walk: 13 (naive string count: 14 — both reproduced outside the script). All thirteen forced from thirteen fresh copies, each returning rc 1 with its own message.

**Confirmation 4 — for HIGH-1.** *Ep.* XX read whole. Numeria: *"remit **such a great sin** to those our sisters, Numeria and Candida"*, *"their repentance and the works which they have done towards our banished colleagues"*, *"their cause having been lately heard, the chief rulers commanded them… to remain as they are."* Candida is defended; Numeria is not. Both strings matched in the **note-stripped** stream, so both are body text by construction, and both also match with notes present.

**Confirmation 5 — for HIGH-2.** Six constructed cases plus two live files. The over-strip reproduced on synthetic input, on Doc_09 §7 (853 → 444 words, with five named live sentences deleted), and on the §2 escalation paragraph (460 words → one space). The generator's independent stripper keeps all of it, which confirms the defect is `notice_strip`'s and not the text's.

**Confirmation 6 — for MEDIUM-4 and MEDIUM-5.** All three behaviours forced from fresh copies, with the matched control in each case: a lowercase `row 28` halts, a capitalised `Row 28` does not; a clean clause halts, the same clause with an incidental `does not` does not; a §3 Gravities cell with codes is compared, one without is skipped. The live `lpcstory003` divergence confirmed twice — once from the committed index, once from my independent derivation, which flagged the same row-set mismatch without being told to look.

**Confirmation 7 — for MEDIUM-7.** The *Acta* located in the vendored Hartel volume at l. 41413 and read: the crowd at Sextus's, the brethren's cry, the disrobing, the twenty-five aurei, the two Juliani, *"propter gentilium curiositatem."* Independently, no English *Acta* exists in the Cyprian division of `anf05` — `Galerius Maximus`, `Thascius Cyprianus` and `Sextus` all return zero — which confirms Doc_09 §6 item 2's Latin-only claim at the same time.

**Confirmation 8 — for every positive in the three rewritten notes, twice each.**
- *Pontius points to the Acta:* `"what God's priest replied to the interrogation of the proconsul, there are Acts which relate"` — Pontius §11, p. 271, body text, matched in both the with-notes and note-stripped streams.
- *Cyprian answered the lapsed:* `"whoever you are who have sent this letter, add your names to the certificate…"` — *Ep.* XXVI, p. 305, `iv.iv.xxvi-p11`, a `<p>` not a `<note>`; the div3 title is **"Cyprian to the Lapsed"**; §2 of the same letter independently confirms *"some who are of the lapsed have lately written to me."*
- *Possidius records the burning:* all three quotations in **CHAPTER XXVIII**, English lines 4065–4073 — and confirmed a second way on the **facing Latin page**, which also defeats the hyphenation trap: *"post eius obitum urbs Hipponensis incolis destituta ab hosti-/bus incensa est."*
- *Candida:* both clauses in *Ep.* XX, p. 298, body text, both streams.

**Confirmation 9 — a finding I dropped.** I flagged `lpcstory005`'s claim that its Absent Story Note quotes *"the L4 template's own first category"* for source loss. The template lists *"source loss, survivorship gap, transmission thinness"* — source loss is first. The citation is exact. No finding.

**Confirmation 10 — a brief premise I tested and found wrong.** The brief states `notice_strip.py` has *"one known limitation — a notice whose tag sits at the **end** of a paragraph rather than the start."* **I constructed that case and it works correctly**: live prose before the notice is preserved and the error phrase is stripped. The real limitations are the four in HIGH-2 and LOW-17, none of which is about position in the paragraph. **The stated known limitation is not the one the script has**, which matters because a documented-but-wrong limitation directs attention away from the real ones.

**What I tested hardest.** In order: the three rewritten Absent Story Notes, positives and negatives, sentence by sentence, at source, twice each — that is where the brief pointed and that is where the fix pass succeeded. Then `notice_strip.py`, in both directions, which is where it failed. Then the generator, by thirteen forced halts and eleven mutation probes. Then the closure ledger, finding by finding, at every site each finding names — which is where HIGH-1 was.

**What would change the verdict.** Fixing **HIGH-1** (one sentence in `lpcstory005`'s Usage Guidance) and **HIGH-2** (two regex changes and a first test in `notice_strip.py`). With those two, I would return **MINOR REVISION** on this same reading: nothing in the MEDIUM band is blocking, and the LOW/COSMETIC tail — much of it now four rounds old — is a cleanup pass. **On the story content alone, considered apart from the instruction layer and the tooling, I would clear this document.** Five rounds have now verified every quotation independently and found no composite and no invention, and that is the part Doc_10 consumes as content.

**If a fix pass disagrees with either HIGH, the thing to produce is not an argument but the text.** For HIGH-1: a reading of *Epistle* XX in which Numeria is not a named woman whose sin is conceded and whose case was heard. For HIGH-2: a run of `live()` over Doc_09 §7 that retains *"The world's most consequential formation question is documented exclusively from the side of those who did not fail it."*

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**2 HIGH · 10 MEDIUM · 20 LOW · 6 COSMETIC.**

**The three rewritten Absent Story Notes hold, at source, positives and negatives alike — the thing this round existed to test has passed.** Round 4's three HIGHs are closed and the fix pass did not over-correct. Against the four rounds' 78 distinct findings: **44 closed, 3 partial, 31 open.** What keeps the verdict at SUBSTANTIAL is one sentence in a deployable retrieval field that asserts a silence its own letter refutes — the fifth round in which this document's worst finding is that defect, and the second in which it survived at a site a previous round named and the fix pass did not visit — together with a brand-new closure-audit tool that deletes live prose and would certify that sentence closed.

*Simulated review — informational only, not an Article 31 substitute.*
