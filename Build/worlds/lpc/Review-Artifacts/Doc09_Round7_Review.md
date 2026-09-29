# Doc_09 — Round 7 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**2 HIGH · 5 MEDIUM · 10 LOW · 4 COSMETIC.**

**The good part is large and it is mechanical, so say it first.** Round 6's fix pass closed almost everything Round 6 named, and I forced rather than read it. **All 17 halting sites in `gen_story_index.py` fire from 17 fresh copies of the world tree** (the pass added one, so the count moved 16 → 17 and `GUARD_LABELS` moved with it — my own AST walk returns 17 and the list has 17 entries). **MEDIUM-4 is closed structurally**, exactly as Round 6 specified: all six demotion forms I could build — `available`, `pending`, `does not`, `unread`, `second witness`, and the plain positive control — now halt at the boundary guard. **LOW-7's Story-Text notice guard is real and survives five mutation probes**, including three that route to a *different* halting site rather than failing open. **LOW-2 is closed: every `##` and `###` heading in all seven chunks is preceded by a `---` rule**, checked mechanically. **LOW-1's unbalanced bold is gone and bold parity is even in all seven files.** LOW-3, LOW-4 and LOW-5 are each closed and I forced each with a matched positive control. The index regenerates **byte-identical**. The test suite passes. **Every quotation still resolves at source**: 18 of 18 CF quotations exact against my own .docx extraction; 72 chunk quotations resolved in ANF05 body text with **zero** resolving to editorial apparatus; 19 of 19 Possidius quotations located, chapter by chapter, in a bilingual-aware English stream I built from scratch.

**What holds the verdict at SUBSTANTIAL is two findings, and both were made by this pass.**

- **HIGH-1 is Round 5's HIGH-2 reintroduced by the fix written for Round 6's LOW-8.** `classify()` now extends every notice span to the **last** `]**` in its paragraph. Where a paragraph contains two sibling notices — which is common in this document — the live prose *between* them is swallowed. Across the nine deliverables this puts **14,337 characters / 2,338 words of live prose inside a "notice" span at 15 sites**, including most of §6 item 1, §6 items 4–5, §8 items 3–8, and §2's Tier 2 and Tier 3 definitions. `mentions_only()` returns **True** for live assertions such as *"The 411 *Gesta* remains unread"* and *"Augustine's *Confessions* (row 9) yields no story."* The committed pre-pass module returns `live` for every one of them. This is a closure-audit tool reporting live, uncorrected text as mention only — the exact operation the module's own docstring says Round 5's HIGH-2 performed, in the function the docstring names as *"the one to call in a closure audit."*

- **HIGH-2 is the signature defect, at a site no round has tested, in the source this document already reads.** Doc_09 §7 item 5: the daily pastoral work *"is the one thing no story records, **because nobody writes it down**."* Possidius wrote nine chapters of it — *Vita Augustini* **XIX–XXVII**, whose own printed headings are *"Augustine as judge," "How he interceded for prisoners," "His frame of mind when attending councils," "Augustine's use of food and clothing," "His use of the church revenues," "Household affairs," "On the companionship of women," "Service to the needy and sick."* That is Registry **row 192, Native, vendored**, the same file `lpcstory007` is built from. Doc_05's own open item 10 says the *Vita* is *"vendored and **unread** beyond one identification."* The true statement is *unread*, and this document has been corrected on the unread/unavailable distinction twice already (§6 item 1, §8 item 1).

The five MEDIUMs: §7 item 1's replacement reason is refuted by the Registry row it cites; `notice_strip._BODY` still lets a notice body cross a paragraph break by three routes, and the new `unterminated()` is blind to all three; the Prosper quotation added to close Round 6's HIGH occurs **zero times** in the vendored file; §4 still says **Four** candidates after this pass made §6 five; and the Disposition lists five rounds' counts under *"Six rounds have been run."*

**If HIGH-1 (two lines of `classify`), HIGH-2 (one sentence in §7), MEDIUM-1 (one clause) and MEDIUM-3 (a disclosure) were fixed, I would return MINOR REVISION on this same reading.** The story content is, for a seventh consecutive round, clean.

---

# Method — everything below was derived here

**I inherited nothing** — not from the brief, not from the fix pass, not from Rounds 1–6. I verified the three commit refs the brief supplies before using them: `7c9b56b4` is HEAD and is *"Doc_09 Round 6 fix pass"*; `44dd6151` is *"Doc_09 Round 5 fix pass"*; `a6a6be73` is the Round 4 pass. All three are correct, which is a change from the last two briefs. Working tree clean.

1. **ANF05 harness, character-level, built from scratch.** A hand-written tag scanner over `anf05_hippolytus-cyprian-caius-novatian.xml` carrying, for every one of 3,475,736 output characters, its innermost `<div1–4>` `title=` (**attribution by title, never by position**), its `<pb n="">` page, and **whether it lies inside a `<note>` span — marked before any tag was stripped** (381,835 note characters, 5,490 note spans). Two normalised streams: with notes, and note-stripped with **one space substituted per note span** so that a quotation the ANF interrupts with an editorial gloss is not fused into a false miss.
2. **Possidius harness, built from scratch.** `possidius_vita-augustini_weiskotten1919.txt` segmented by running head (`LIFE OF SAINT AUGUSTINE` = English page, `SANCTI AUGUSTINI VITA` = Latin page), English-only stream reconstructed (154,792 chars), **de-hyphenated at line ends**, plus a second punctuation-free word stream, plus a chapter map built from the printed `CHAPTER N` headings.
3. **CF V7.4 extracted from the .docx myself** (722 paragraphs, unzip + `<w:t>` walk). **No line numbers are cited anywhere below** — Round 6 established they are extraction-dependent and it is right.
4. **The generator.** Halting sites counted by my own AST walk (17), every one forced from a fresh copy of the world tree, plus separate bypass probes against the boundary guard, the §3 comparison, the confidence-band renderer and the new Story-Text guard.
5. **`notice_strip.py` attacked in both directions** on constructed input and on the live deliverables, with the committed pre-pass module loaded side by side as a control.
6. **Every absolute negative in Doc_09 and all seven chunks** extracted from *live prose only* and tested at source.
7. **Every chunk structurally diffed** against `44dd6151`: heading set, rule-before-heading, bold parity, front-matter fields, notice inventory.

---

# Job 1 — auditing the Round 6 fix pass's claims

The Document Log claims *"HIGH closed; all 6 MEDIUM, all 12 LOW and all 4 COSMETIC addressed."* Checked at **every** site each finding named.

### Closed — verified in the live text, most of them by forcing

| R6 finding | Verified how |
|---|---|
| **HIGH-1** — `lpcstory007` denied a second account of Augustine's death | Both sites rewritten. Row 203 read in full (**Native, grade A, Vendored**); the a. 430 entry read in the file at l. 54206–54212. The substance is right and the correction *strengthens* the chunk. **The quotation itself does not match the file — MEDIUM-3** |
| M1 — §7 item 1 / §1 on the 133-year gap | §1 now quotes Doc_02 §7 exactly; I read Doc_02 §7 whole and the clause *"richly attested — through sources that are Donatism's own territory (World #4), not this world's"* is verbatim. **§7 item 1's replacement reason is a new error — MEDIUM-1** |
| M2 — Status header frozen at Round 4 | Now *"REVISED after Round 6 … Six independent adversarial review rounds"*, agreeing with the Document Log, the Disposition and the index. **The same defect survives 168 lines later — LOW-1** |
| M3 — §8 item 2's false claim about cross-references | Corrected, with the falsification attributed to the Round 5 pass. **The count it states is one short — LOW-9** |
| **M4 — `AVAIL_CLAUSE` widened the boundary bypass** | **Closed structurally.** `allrows` is built from `rows` **and** `rows_excluded`. Forced from six fresh copies: the plain form, `available`, `pending`, an incidental `does not`, `unread` and `second witness` **all** now halt with *"row(s) ['204'] are not Native … A story sourced to an Excluded row is a boundary breach."* Round 6's own two positive controls are among them |
| M5 — `notice_strip`'s false contract | **Partly.** A truly empty line now bounds a notice body and `unterminated()` reports the opener. **Three other paragraph breaks do not — MEDIUM-2** |
| M6 — the *Confessions* absent from §6 | Added as §6 item 3 and §8 item 8. Row 9 verified **Native**; row 197 confirms the NPNF English is vendored and the Latin (`augustine_confessiones-lat_knoll-csel33.txt`) too, so *"row 9, Native, vendored"* holds. **§6's count was not updated — MEDIUM-4; the wording is lifted from row 9 unattributed — LOW-5** |
| **L1 — unbalanced bold in five chunks** | Gone. `**` parity is even in all seven files and the malformed form returns zero hits |
| **L2 — ten deleted section-separator rules** | **Closed, and I checked it mechanically rather than by eye.** Every `##` *and* `###` heading in all seven chunks is preceded by a `---`. Ten rules restored, matching the ten deleted |
| L3 — substring band test in the audit renderer | **Forced.** With the halting guard neutralised and the chunk declaring `Not Documented`, the §4 table now prints `| lpcstory003 | 1 | **Yes** | **NO** — Not Documented |`. Round 5's L9 output is gone from the backstop as well as the guard |
| L4 — `_missing` compared unsplit groups | **Forced, both directions.** A chunk drawing on `rows 1/191` against a §3 cell naming `rows 1, 191` now emits rc 0; the same chunk with 191 removed from §3 halts with *"the chunk draws on row(s) ['191'] that Doc_09 §3's Source column does not name."* Fails closed, satisfiable by correct input |
| **L5 — index Status line** | **Forced.** I dropped a stub `Doc09_Round7_Review.md` into a copy and regenerated: Status stays *"REVISED after Round 6"* while the review count goes to seven and the Disposition correctly says no fix pass is recorded. Keyed to `FIXED`, as asked |
| **L7 — no guard on notices in Story Text** | **Closed and hard.** Five probes, all halt: a well-formed notice (the new guard), a mistyped terminator (the swallowed-opener guard), a bare Form B stamp (the new guard), a notice split over a blank line and a lower-case tag (the surviving-opener guard) |
| L6 — the *Acta* characterised unopened | Now *"generally printed as covering both proceedings … this build has not opened it"* |
| L9 — `lpcstory001` grammar | *"and **point** to a case they can check"* |
| L11 — `lpcstory003`'s future tense | *"no source in this corpus **supplies** them"* |
| L12 — *"is seen"* → *"is *watched*"* | Done, with the *Confessions* named as the reason |
| C1 — CF's Tier 3 continuation | Restored. **Exact against my own extraction**: *"The formation ideal communicated is credible evidence; the specific events claimed are not."* |
| C2 — untitled transcription block | Given a `### ` heading in all four chunks. **A stray leading space came with it — COSMETIC-1** |
| C3 — the L8 one-liner | Removed from all five chunks that carried it (Round 6's COSMETIC-3 said *six*; the pre-pass files carry it in **five** — `001` and `007` never had it, and LOW-1's own site list was the correct one) |
| C4 — silent initial capitalisation | Disclosed at §2. **The count in the disclosure is wrong — LOW-2** |
| L8 — `classify` on a nested notice | Addressed, and **the fix is HIGH-1** |
| L10 — two stale figures in the Decision Log | One removed, one replaced with **a new wrong figure — LOW-3, LOW-4** |

**Honest summary: 21 of Round 6's 23 findings are closed at every site the finding named; M5 is partial; L8's fix is a regression.** That is the second consecutive pass that did most of what it said. **The failure mode has changed and is worth naming exactly: this pass verified the sentences it *changed* and did not check the *counts and neighbours* those changes invalidated.** Every one of MEDIUM-4, MEDIUM-5, LOW-1, LOW-2, LOW-3 and LOW-9 below is a number or a neighbouring sentence that one of this pass's own edits falsified — which is precisely the operation Round 6 caught at MEDIUM-3 and named as *"the document's signature defect in miniature."*

---

# Findings

## HIGH

### HIGH-1 — the fix for LOW-8 reintroduces Round 5's HIGH-2: `classify()` swallows live prose between two notices in one paragraph and reports it as mention, at 15 sites in the live deliverables

**Site.** `scripts/notice_strip.py` ll. 132–141.

```python
notices = []
for a, b in notice_spans(text):
    stop = text.find("\n\n", a)
    stop = len(text) if stop == -1 else stop
    last = text.rfind("]**", b, stop)
    notices.append((a, last + 3 if last != -1 else b))
```

**What it does.** For each notice span it extends the end to the **last** `]**` still inside the paragraph. The comment says this is so *"a nested quotation cannot truncate its container."* But the search is not restricted to the container — it runs to the paragraph end. Where a paragraph holds **two sibling notices**, span one is extended over span two, and everything between them, which is live prose, is absorbed.

**Constructed, with a matched control:**

```
Item one. **[CORRECTED … Round 1:** the earlier text was wrong.**]**
THE SERMON TEXTS ARE NOT AVAILABLE TO THIS BUILD AT ALL.
**[CORRECTED … Round 2:** another note.**]** Tail.
```
`classify(t, "THE SERMON TEXTS ARE NOT AVAILABLE TO THIS BUILD AT ALL")` → **`notice-only`**.
Delete the second notice and the identical sentence returns **`live`**. That is the control.

**On the committed deliverables.** I measured, for every notice span in the nine files, how much text the extension newly covers that no other span covers:

**15 sites, 14,337 characters, 2,338 words of live prose now inside a "notice" span.**

Sites include `Doc_09 §6 item 1` (2,719 + 2,200 chars), `§6 item 4` (509), `§8 items 3–8` (1,904 + 431), `§2`'s Tier 2 and Tier 3 definitions (1,145 + 706), `§3`'s table (976), `§4`'s escalation paragraph (1,630), and `lpcstory002`'s Usage Guidance (577).

Run against the committed pre-pass module (`44dd6151`) as a control:

| phrase in live prose | `classify` NEW | `classify` pre-pass | `mentions_only` NEW |
|---|---|---|---|
| *"The healing miracles at Hippo"* | **notice-only** | live | **True** |
| *"Augustine's *Confessions* (row 9) yields no story"* | **notice-only** | live | **True** |
| *"The provisional Step-2 inventory was never made"* | **notice-only** | live | **True** |
| *"The 411 *Gesta* remains unread"* | **notice-only** | live | **True** |
| *"Unavailable is a different problem from unread"* | **notice-only** | live | **True** |
| *"this story is easily flattened into a modern account of Christian charity during epidemics"* | **notice-only** | live | **True** |
| *"The wider question is answered; the narrow one is not"* | **notice-only** | live | **True** |

**Why this is HIGH.**

1. **It is the same operation as Round 5's HIGH-2 and the same direction.** Round 5's HIGH-2 was *"a closure audit run through it reported live, uncorrected text as 'mention only' — manufacturing exactly the false conclusion the recurring defect depends on."* That sentence is in this file's own docstring, twelve lines above the code that now does it again.
2. **It targets the audit interface, not the stripper.** The docstring says `live()` under-strips by design and *"`classify()` is the one to call in a closure audit."* `live()` is fine. The function the build is told to trust is the broken one, and `mentions_only()` — documented as *"conservative"* — returns True on live text.
3. **Three of the seven demonstrated phrases are sentences this very pass wrote** (§6 item 3/4, §8 item 8). A Round 8 audit asking *"did the Confessions actually get added as a live candidate?"* would be told **no, it is only mentioned in a notice.**
4. **The test suite cannot catch it.** H4 constructs a genuinely *nested* notice and asserts `notice-only`, which is correct for that shape. There is no sibling-notice case anywhere in the suite, and the fix's own justification never distinguishes the two shapes.

**Fix.** Bound the extension by the container, not the paragraph: search only within the text the *outer opener* governs — e.g. stop at the first position where a following `\*{0,2}\[(TAGS)` opener begins, or accept the inner truncation and solve LOW-8 by matching nested brackets rather than by reaching forward. LOW-8's error direction was the safe one; this one is not, and reverting is strictly better than what is committed.

---

### HIGH-2 — Doc_09 §7 item 5 says the ordinary pastorate is "the one thing no story records, because nobody writes it down." Possidius wrote nine chapters of it, in the Native vendored source this document's only Phase Two story is built from

**Site.** `Doc_09_Story_Inventory.md` **l. 126**. Live prose, no notice in the item.

> *"**5. There is no story of an ordinary, uneventful pastorate.** Every story here is a crisis… **The daily work that Doc_04 makes this world's Primary gravity — a bishop keeping a flock, week after week, when nothing is happening — is the one thing no story records**, because nobody writes it down. This is the gap Tier 4 reconstruction exists for, and it is why this world's Tier 4 material sits in Doc_05 rather than here."*

**What the corpus contains.** `possidius_vita-augustini_weiskotten1919.txt` — `Source_Registry.md` **row 192**, **Native**, **Vendored**, *"a genuinely bilingual edition with a complete English translation"* — carries, between the Donatist chapters and the death, a continuous block of chapters whose own printed headings are:

| | |
|---|---|
| **XIX** | *Augustine as judge* |
| **XX** | *How he interceded for prisoners* |
| **XXI** | *His frame of mind when attending councils* |
| **XXII** | *Augustine's use of food and clothing* |
| **XXIII** | *His use of the church revenues* |
| **XXIV** | *Household affairs* |
| **XXVI** | *On the companionship of women* |
| **XXVII** | *Service to the needy and sick* |

Read whole, chapter XXII is week-after-week pastoral life in the exact sense §7 item 5 says is unrecorded:

> *"His garments and foot-wear and even his bedclothing were modest yet sufficient… His table was frugal and sparing, though indeed with the herbs and lentils he also had meats at times for the sake of his guests… His spoons only were silver, but the vessels in which food was served were earthen, wooden or marble… At the table he loved reading and discussion rather than eating and drinking, and against that pest of human custom he had this inscription on his table: **Who injures the name of an absent friend / May not at this table as guest attend.**"*

And chapter XX records Augustine's standing rule about intercession, with a reply from the Vicar of Africa Macedonius quoted in full; chapter XXVI records his refusal to have even his sister and nieces live with him *"because of the possible stumbling-block."*

**Why this is HIGH, and each reason is sufficient.**

1. **The stated cause is flatly refuted.** *"Because nobody writes it down"* is the operative clause. Somebody did, at length, in a Native vendored source. The honest statement is available and this document has already been made to write it twice: **`Doc_05_Ecological_Reconstruction.md`'s own open item 10** says *"Possidius's *Vita Augustini* (row 192) is vendored and **unread beyond one identification**."* Unread is not unwritten. §6 item 1 of this same document states the distinction as a rule — *"Unavailable is a different problem from unread"* — and §8 item 1 applies it to the *Acta*.
2. **It is load-bearing on two structural claims.** It is the stated reason this document has **zero Tier 4 stories**, and it is the stated reason Tier 4 material *"sits in Doc_05 rather than here."* Doc_05 has not read it either. So the document routes an absence to a sibling document that its own open-items list says has not opened the source.
3. **It is the source `lpcstory007` already cites.** The chunk's Source field declares *Vita* **XXVIII–XXXI**. The chapters above are immediately before the declared span, in the same file, in English. This is the Round 1 H1 shape — *"reading to a chosen boundary, then asserting a negative about what lies past it"* — which the document itself names at `lpcstory002` l. 71 as *"the shape this build keeps producing."*
4. **It is the seventh consecutive round's instance of the same defect class**, and this time the refuting source is not merely in the corpus but is the one source this document's whole second phase rests on.
5. **§6 does not list it.** The section that exists to record what was weighed and set aside contains five items and none of them is *Vita* XIX–XXVII — the single densest block of ordinary-pastorate evidence this world has.

**Fix.** Replace the causal clause and add a §6 item:

> *"…is the one thing no **story** in this inventory records. It is not unrecorded: Possidius devotes* Vita *XIX–XXVII to exactly this — Augustine as judge, his intercessions, his table and its rule against slander, the church revenues, the household, the sick. Those chapters are outside the span this build has read (Doc_05 open item 10 records the* Vita *as unread beyond one identification), and reading them is a reading task, not an absence."*

---

## MEDIUM

### MEDIUM-1 — §7 item 1's replacement reason is refuted by the only row it cites: row 27 is **Native** to this world and is the corpus map's own **home** for that tradition

**Sites.** `Doc_09_Story_Inventory.md` **l. 118** (§7 item 1) and **l. 23** (§1's notice).

> l. 118: *"…this world tells itself no stories at all — not because nothing happened, and not because the century is undocumented, but because **what documents it belongs to the neighbouring world's record rather than this one's.** Row 27's Optatus writes inside the gap, and writes about the Donatist schism."*

**What the Registry and Doc_02 record.** `Source_Registry.md` **row 27**: Boundary Status **Native**; corpus map `role: **tradition**`, `confidence: provisional`. `Doc_02_Source_Ecology.md` **§1**, read whole, quotes the corpus map's own note that *"**this entry**"* — this world's own — *"**is the census's home for that tradition**"*, and states the placement in as many words:

> *"…Optatus is `tradition` **here** and `context` on the Donatism side (**native to one, etic evidence for the other**)…"*

So the one in-gap document the sentence names **belongs to this world's record**, on the build's own census, and is carried by the neighbouring world as *context*. The sentence asserts the reverse.

**And §1 refutes it in a single line.** l. 23's live prose says the interval is attested *"through sources that are Donatism's own territory (World #4), not this world's"*; the `[CORRECTED — Round 6's M1]` notice attached to that same sentence says row 27 is *"**Native and vendored**."* Native means in-boundary **for this world**. That is the Round 4 H1 shape — *"self-refuting in one sentence"* — at a new site.

**What is actually true, and Doc_02 §1 supplies it.** The reason no story is built from Optatus is **subject matter**, not ownership: *"Optatus's *Against the Donatists* is Catholic-side anti-Donatist polemic, not evidence of this world's own ordinary pastoral-congregational life the way Cyprian's and Augustine's own corpora are."* The sentence's own next clause — *"and writes about the Donatist schism"* — already carries that reason. The ownership clause adds nothing true.

**Why it matters.** `lpcstory005`'s Absent Story Note states the governing rule: *"Article 20 requires the reason for an absence to be named correctly, not merely dramatically."* Round 6 corrected *"nothing survives"* on exactly that ground. The replacement tells a Representative that a third of this world's span is documented in somebody else's archive, when the build's census homes the principal in-gap text **here**. And Doc_02 §9 item 11 records the Optatus placement as an open census-level question, which this sentence closes by assertion.

**Fix.** *"…but because what documents it is anti-Donatist polemic rather than this world's own pastoral record. Registry row 27 (Optatus of Milevis, c. 366–393) is **Native** to this world and writes from inside the gap — Doc_02 §1 homes him here as `tradition` and the Donatism build carries him as `context` — but he writes the schism, not a congregation, and no story is built from him for that reason."*

---

### MEDIUM-2 — MEDIUM-5 is not closed: a notice body still crosses a paragraph break by three routes, `live()` still deletes live assertions, and `unterminated()` is blind to all three

**Site.** `scripts/notice_strip.py` l. 66 and ll. 79–89.

```python
_BODY = r"(?:[^\]\n]|\n(?!\n)|\](?!\*\*))*?"
```

The body is bounded by `\n\n` — a **literally empty** line. Markdown paragraph breaks are not all literally empty, and markdown list items and table rows are not separated by blank lines at all. Three constructions, each run through the committed `live()`:

| construction | `live()` keeps the live sentence? | `unterminated()` reports the malformed opener? |
|---|---|---|
| paragraphs separated by a **whitespace-only** line (`"\n   \n"`) | **No** — returns `' '` | **No** — returns `[]` |
| a **bullet list** under a mistyped terminator | **No** — returns `' '` | **No** — returns `[]` |
| a **table**, rows separated by single newlines | **No** — the intervening row is deleted | **No** |

**Positive control.** The truly-empty-line case — the one Round 6 constructed and the one the pass's own test H1 uses — is genuinely fixed: `live()` keeps *"Numeria and Candida are discussed…"* and `unterminated()` returns one offset. **The fix closed the case that was demonstrated and not the class.**

**It is live-relevant, not theoretical.** I scanned the nine deliverables: **14 notice openers sit on a line that is not followed by a literally empty line** — 10 in numbered or bulleted lists (`Doc_09` §2's tier bullets at ll. 35–37, §5 at l. 64, §6 items at ll. 104, 106, §8 items at ll. 133, 138) and 1 inside a `§3` table row (l. 77).

**Forced on the committed Doc_09.** I changed the final `**]**` of §6 item 1's notice (l. 104) to `]` — **one character** — and re-ran:

```
live() words, committed : 5462
live() words, one-char typo : 5181
WORDS OF LIVE PROSE DELETED : 281
unterminated() on the mutated file : []
```

*"Unavailable is a different problem from unread"* and *"the strongest single candidate for the next pass"* both vanish from `live()` output, and the detector written to flag exactly this reports the markup as well-formed.

**Why this matters.** The docstring still says *"It **NEVER** deletes prose outside a bracket, so it cannot hide a live assertion."* That sentence is still false. The file's own closing line — *"A control stated more broadly than it is implemented is worse than no control, because the next round will trust it"* — still describes its own docstring, one round after Round 6 quoted it.

**Fix.** Treat a paragraph break as `\n[ \t]*\n`, and bound the body by the **line** for list and table contexts (a notice in this build never spans a rendered block). Then make `unterminated()` a genuinely independent scanner — a per-line pass that finds openers and their terminators without using `_NOTICE` at all. As written it derives its answer from the same regex whose failures it is supposed to expose, which is the defect Round 6 named at the test harness.

---

### MEDIUM-3 — the Prosper quotation written to close Round 6's HIGH occurs **zero times** in the vendored file, is silently normalised, and is reproduced from the file's own header, which the header says is not authoritative

**Site.** `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md` **l. 55**, deployable Tier Justification.

> *"**Prosper of Aquitaine's *Epitoma Chronicon* (`Source_Registry.md` row 203, Native, vendored) independently attests the death at a. 430**: *"Aurelius Augustinus episcopus per omnia **excellentissimus** **moritur** V. kl. Sept., libris Iuliani **inter impetus obsidentium Vandalorum**"*"*

**What the file says.** `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`, body, ll. 54206–54212:

```
UWA Aurelius Augustinus episcopus per omnia cxcellentissimus
moritur Y. kl. Sept., libris luliani inter impetus obsidentium
"NVandalorum in ipso dierimi suorum tine respondens et glo-
riose in defensione Cliristianae gratiae perseverans.
```

**Counted, whitespace-normalised, over the whole file:**

| string | occurrences in the body | occurrences in the file incl. header |
|---|---|---|
| the chunk's full quoted string | **0** | **0** |
| `Aurelius Augustinus episcopus per omnia excellentissimus` | **0** | **1** (the header only) |
| `inter impetus obsidentium Vandalorum` | **0** | **0** |
| `Aurelius Augustinus episcopus per omnia cxcellentissimus` | **1** | 1 |

So the chunk's string matches the **vendored file's own header note**, not its body — and the header itself says, in its Provenance line: *"quotations in this header … are given in standard/readable spelling for legibility … **the file's own body text, not this header's quotation of it, is authoritative for exact wording.**"* The chunk also reaches past the header's ellipsis to supply *"Vandalorum"*, which the body prints as `NVandalorum`.

**Why this is MEDIUM and not COSMETIC.**

1. **This build discloses OCR normalisation as a matter of course, and did not here.** `Source_Registry.md` rows 194 and 204 both say, in the same sentence as their quotations, *"**quoted here in normalized form, disclosed rather than left silent**"* and enumerate the letter confusions. Row 203 itself, which the chunk cites, carries the same practice.
2. **The same pass added a whole paragraph disclosing a much smaller change.** Doc_09 §2's new masthead (l. 31) discloses that five quotations silently capitalise an initial letter, on the stated ground that *"a reader running a literal string search against the vendored text will miss them."* A reader running a literal search for the Prosper quotation gets **zero hits**. The disclosure written this pass does not cover the only quotation this pass added.
3. **The Decision Log calls it verified.** The Round 6 entry says *"**Verified at source**: 'Aurelius Augustinus episcopus per omnia excellentissimus moritur V. kl. Sept., libris Iuliani inter impetus obsidentium Vandalorum'"* — of a string that is not at source. That is a Decision Log honesty item (see Job 5).
4. **Round 1's HIGH in this document was a transcription failure of this exact shape** — *"two quotations altered in transcription, one printing a phrase that occurs nowhere in the corpus"* — and the Disposition recites it as such.

**The substance is right.** Augustine does die on `V kal. Sept.` amid the Vandal siege, and the correction to HIGH-1 is sound. Only the transcription is undisclosed.

**Fix.** Print the body's own reading with the normalisation disclosed, as rows 194 and 203 do — *"quoted in normalised form; the file's OCR reads `cxcellentissimus`, `Y. kl.`, `luliani`, `NVandalorum`"* — and add the INTAKE.md Latin-only second-witness caveat that row 203 carries and that §6 item 2 invokes for the *Acta*.

---

### MEDIUM-4 — §4 still says **Four** candidates were considered and not built; this pass made §6 five

**Sites.** `Doc_09_Story_Inventory.md` **l. 84** against **§6** (ll. 104–108).

> l. 84: *"**No story required inventing a participant, a detail, or an outcome…** **Four** candidates were considered and not built; see §6, where each is recorded with the reason. **[CORRECTED, 2026-09-15 — Round 1's L7:** this said *"Two."***]**"*

§6 now enumerates **five**: 1 Perpetua sermons, 2 the *Acta*, **3 the *Confessions* (added this pass)**, 4 *City of God* XXII.8, 5 the 411 *Gesta*. `git diff 44dd6151 HEAD` shows the insertion and the renumbering of the old items 3 and 4; l. 84 is not in the diff.

**Why it matters.** It is the same shape as MEDIUM-3 of Round 6 — an edit falsifying a standing sentence the same commit leaves alone — and it is a **typed count**, in a document whose generator's own header doctrine is *"DERIVE, never type. A number typed here is a number that goes stale."* The sentence already carries the notice recording that it was wrong once before. This is its second failure by the same mechanism.

**I checked for stale §6 item numbers as the brief asked.** The renumbering of old items 3 and 4 into 4 and 5 broke **nothing**: every live reference to §6 by item number (`Doc_09` §8 items 1, 5 and 8; `lpcstory006` ll. 6 and 63) points at items 1, 2 or 3, none of which moved. That is clean and worth crediting.

**Fix.** *"**Five** candidates…"*, or derive it in the generator, which already parses §6.

---

### MEDIUM-5 — the Disposition lists five rounds' counts under "Six rounds have been run," and still says "Eight HIGH findings across five rounds," in the paragraph corrected for that exact understatement

**Site.** `Doc_09_Story_Inventory.md` **ll. 165 and 167**.

> l. 165: *"**Not disposed. REVISED after Round 6…** **Six rounds have been run**, all returning **SUBSTANTIAL REVISION REQUIRED**: Round 1 (2H 8M 12L 5C), Round 2 (0H 11M 17L 5C), Round 3 (1H 10M 12L 5C), Round 4 (3H 9M 16L 5C), Round 5 (2H 10M 20L 6C)."*

Six rounds are claimed; **five** are enumerated. Round 6 (1H 6M 12L 4C) is missing. The pass edited this sentence — the diff shows *"Five rounds"* → *"Six rounds"* and *"after Round 5"* → *"after Round 6"* — and did not extend the list it introduces.

> l. 167: *"**Eight HIGH findings have been raised across five rounds. Six are one defect — a silence asserted about a source that the source refutes.**"*

It is now **nine across six**, and **seven** are that one defect. Round 6's HIGH-1 is missing from the enumeration that follows, which stops at Round 5. So is the derived tally *"Five of the eight were in fields that instruct the Representative"* — Round 6's HIGH-1 was in a Tier Justification **and** an Absent Story Note, so it is six of nine.

**Why it matters.** The `[CORRECTED — Round 5's M3]` notice attached to this very paragraph says it *"understated the record by three quarters **at the one place the record is summarised**."* It understates it again, at the same place, in the pass that edited the sentence two lines above. And the pass's own Decision Log entry says *"Sixth consecutive round of this document's signature defect"* — the correct figure was written the same day, in the same commit, in a different file.

**Fix.** Add Round 6's counts to the list and make the HIGH tally nine across six, seven of them the one defect.

---

## LOW

**LOW-1 — the Disposition's closing line says this document "has not been reviewed at all," twelve lines below "Six rounds have been run," and has said so since the original draft.** `Doc_09_Story_Inventory.md` l. 173: *"**Build-cycle position.** Five documents in this world are complete, independently reviewed, and awaiting a disposition only the project lead can give. **This is the sixth, and it has not been reviewed at all.**"* I traced the string across all seven Doc_09 commits (`25edc87d`, `b43f37d6`, `f447e7ae`, `abff3618`, `a6a6be73`, `44dd6151`, `7c9b56b4`): present in every one. Six review rounds and six fix passes have not touched it, including the pass that fixed MEDIUM-2 — the identical staleness, 168 lines earlier in the same file. **Also wrong on its own terms:** `Review-Artifacts/` carries completed round sets for Doc01–Doc08 plus Step0, so this is the **ninth** document, not the sixth, and eight are complete, not five. *Fix:* rewrite both clauses, and put the Status line, the Disposition's first sentence and this line under one convention so they move together.

**LOW-2 — §2's new transcription disclosure undercounts its own sites: six across five chunks, not five across four.** l. 31: *"Five such sites exist across four chunks."* I found them mechanically — every quotation whose opening word is capitalised in the chunk, whose lower-case form is present in the source and whose capitalised form is not — with the note-stripped ANF stream and the de-hyphenated Possidius stream. **Six sites in five chunks:** `002` l. 15 (*"There broke out a dreadful plague"*), `003` l. 21 (*"Was found half dead…"*), **`005` l. 21 — *"Because they have us as brethren, we ought to keep watch,"* against *Ep.* XX's *"…for whose sin, because they have us as brethren, we ought to keep watch"***, `006` l. 17 and l. 21, `007` l. 23. Round 6's COSMETIC-4 listed five and the pass typed the five without recounting. The `005` site is in the chunk whose Usage Guidance was itself Round 5's HIGH. *Fix:* six and five, and name `lpcstory005`.

**LOW-3 — the Decision Log replaces one stale notice count with another.** The Round 6 entry rewrites Round 5's *"all 53 notices"* to *"every notice in this world build (**79** spans as of Round 6)"*. Counted with the committed stripper across the nine deliverables: **75**. Counted with the pre-pass stripper on the pre-pass files: **71** — which is exactly Round 6's figure, so 71→75 is the real movement and 79 matches neither end. Across every `.md` in the world build outside `Review-Artifacts/` it is 154. *Fix:* 75, or drop the figure as the check count was dropped.

**LOW-4 — the Decision Log says the test suite's check count is "derived rather than typed." The suite emits no count at all.** `scripts/test_notice_strip.py` prints per-check lines and then *"All checks passed."* — nothing derived and nothing typed. Removing a stale literal is the right fix; describing the removal as a derivation is not what happened, in an entry whose stated purpose is to record what was actually done.

**LOW-5 — §6 item 3 reproduces row 9's Notes verbatim without marks or attribution, which is the defect Round 6's L13 corrected at §6 item 2 in the same pass.** New l. 106: *"the founding first-person document of this world's Augustine half."* `Source_Registry.md` row 9's Notes: *"the founding first-person document of this world's own Augustine half (Doc_01 §2)."* Item 2, eleven words earlier in the same section, now reads *"in `Source_Registry.md` row 41's own words"* — the fix for exactly this shape. *Fix:* the same construction.

**LOW-6 — the test suite's new cases lock in the safe half of the stripper and cannot reach either live defect.** H1, H3 and H6 all use literally empty lines, so they pass while MEDIUM-2's three paragraph-break routes remain open; H6 in particular asserts *"no malformed notice markup"* across all nine files using the detector that cannot see them. H4 asserts `notice-only` for a genuinely nested notice — correct — and there is no sibling-notice case, which is HIGH-1. The suite has grown by eight checks and its blind spots are unchanged.

**LOW-7 — `lpcstory004` tells the Representative that "Doc_02 vendors no source that would license a conversion" of the sesterces; the vendored ANF05 prints a dollar conversion two words after the sum the chunk quotes.** l. 55. In `anf05` at p. 355 the letter reads: *"We have then sent you a sum of one hundred thousand sesterces, **[An immense contribution, for the times. In our money reckoned (for temp. Decii) at $3,757. For the Augustan age it would be $4,294. The text (sestertia) dubious. Ed. Paris.]** which have been collected here in the Church…"* **The chunk's disposition is right** — that is 19th-century editorial apparatus, not a licensed source, and the note calls its own text *"dubious."* But this chunk already discloses the *other* editorial locus at the same sum (*"The identical figure also appears in the ANF Argument, which is editorial — the chunk cites the body, and says so"*), and it is the one chunk in the set whose evidentiary discipline is cited as exemplary. Naming the note and excluding it would make the absolute true rather than merely defensible. *Fix:* one clause.

**LOW-8 — the widened boundary check will now halt on a chunk that names an Excluded row in order to disclaim it, with a message that will be false.** The message is *"A story **sourced to** an Excluded row is a boundary breach"* but the check now fires on `rows_excluded` too, i.e. on rows the chunk states it does **not** draw on. This is Round 6's own prescribed remedy and I think it is the right trade, but the message must stop asserting sourcing. *Fix:* two message variants, one per set.

**LOW-9 — §8 item 2's correction states a count that is one short.** l. 133: *"Three cross-references now exist, so the placeholder is load-bearing after all."* There are **four** live references to Doc_09 §8 by item number: `Doc_09` l. 157 (the Document Log row, *"one new escalation raised (§8 item 7)"*), `Doc_09` l. 171 (the Disposition), `lpcstory006` l. 61, and `lpc_Decision_Log.md` l. 1453. The missing one is inside Doc_09 itself and is invisible to the `Doc_09 §8 item [0-9]` grep Round 6 used, which the pass adopted without re-running in-document. The correction's point stands; the number does not.

**LOW-10 — `lpcstory007` cites a Latin-only witness in a deployable field without the rule this document applies to its other Latin-only witness.** Row 203's own Vendoring cell ends *"Original-language witness (Latin) — second-witness caveat applies per `cic/texts/INTAKE.md`."* Doc_09 §6 item 2 invokes that rule explicitly for the *Acta* (*"Under `cic/texts/INTAKE.md` a Latin witness is citable where no English rendering exists"*). `lpcstory007` l. 55 and the Absent Story Note at l. 79 tell the Representative that Prosper corroborates the death, with no such note, and no statement of whether an English Prosper exists in this corpus. *Fix:* one clause in the Source or Tier Justification.

---

## COSMETIC

**COSMETIC-1 — four chunks carry a stray leading space introduced with the new `###` heading.** `002` l. 63, `003` l. 49, `004` l. 45, `007` l. 61 all begin *" These were recorded inline in the Story Text…"*. One space is below the four-space code-block threshold so nothing renders wrong; it is an artifact of the heading insertion and should be trimmed.

**COSMETIC-2 — the index's number-word map stops at six, so the moment this artifact lands the index will print a digit mid-sentence.** `gen_story_index.py` l. 363: `_NW = {0: "No", …, 6: "Six"}`. Reproduced by dropping a stub Round 7 artifact into a copy and regenerating: *"**7 round(s)** — Round 1, … Round 7"* and *"**7 independent review round(s) have been run**"*, where the previous six printed words. A typed literal in the file whose doctrine is that typed numbers go stale. *Fix:* `num2words`-style fallback or extend the map with a derivation.

**COSMETIC-3 — the transcription blocks are now a section of their own, while the generator's own remedy text and the Decision Log still say they belong inside Tier Justification.** The block sits between two `---` rules under a `### ` heading; the new halting message at `gen_story_index.py` l. 139 says *"Move them to **Tier Justification**."* Both readings are defensible; they should agree.

**COSMETIC-4 — §8 item 8 calls Phase Two "one story from one chapter of Possidius"; §3 and the chunk declare XXVIII–XXXI.** Inherited verbatim from Round 6's MEDIUM-6 wording. Four chapters, of which XXXI carries the story.

---

# Is the deliverable adequate to proceed to Doc_10?

**Not on the content — which is ready — but on two instruction-layer sentences and one tool.**

**What is ready, verified independently for a seventh time and by instruments built for this round.** Seven stories, seven real texts. **72 chunk quotations resolve to ANF05 body text and zero resolve to editorial apparatus** — I built the note mask before stripping a single tag and confirmed it in both directions (body text found and marked not-in-note; five randomly sampled note fragments found in the with-notes stream and **absent** from the note-stripped stream; nonsense returns MISS). Eight quotations that at first looked note-resident turned out to be body text that the ANF interrupts with an editorial gloss, which the chunks correctly step over — that is the build's discipline working, not failing. **19 of 19 Possidius quotations located** with chapter, including the nested inner quotation Round 5 restored. **18 of 18 CF quotations exact.** Every *Epistle* resolved to its work by `title=`, never by position: *Ep.* XX is `Celerinus to Lucian`, XXI `Lucian Replies to Celerinus`, XXXIV `To the Same, About the Ordination of Numidicus as Presbyter`, LIX `To the Numidian Bishops, on the Redemption of Their Brethren`, LXVII `To the Clergy and People Abiding in Spain, Concerning Basilides` — no misattribution anywhere. **No invented participant, event or outcome.** The generator's 17 guards all fire; the index is byte-identical.

**What is not ready.** `classify()` will tell the next fix pass that live text is mention (HIGH-1), and §7 item 5 will tell a Representative that nobody recorded the ordinary pastoral work this world's Primary gravity is built on (HIGH-2). Doc_10 inherits §7 verbatim as the document's absence register.

**HIGH-1 should be fixed before the next fix pass runs**, for the reason Round 5 gave about its own HIGH-2 and Round 6 repeated: the next pass will use this tool to decide what is closed, and today it would close §6 and §8 wrongly.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** No identity, title or voice decision is made in this document. Noted separately and not as an escalation: `Doc_09` §7 item 5 and `lpcstory004` l. 55 assert absences the corpus does not support, and §7 item 1 names a reason the Registry refutes. All are within this document's own gift to fix. **The M1 identity decision recorded in the Decision Log on 2026-09-15 is outside this deliverable and I did not review it**, except to note that its own open item 5 correctly routes a real portfolio constraint.

- **Portfolio-level or cross-world — two inherited, both with new instances.**
 1. *The corpus-wide editorial-apparatus item.* **Seventh consecutive independent verification and still zero positive instances in this deliverable.** Built afresh with the note mask laid down before tag stripping. Carry forward unchanged. **I record the one new wrinkle, because it is the class's near-miss:** `lpcstory004` correctly excludes the ANF *Argument* at the sesterces and does not mention the ANF *footnote* at the same sum, which supplies a dollar conversion the chunk's Usage Guidance says no vendored source supplies (LOW-7). The disposition is right and the disclosure is incomplete.
 2. *The index-generator-as-build-artifact item (Doc_08 R5; Doc_09 R1-M4c, R2-M7, R3-M4, R4-M4, R5-M4/M5, R6-M4).* **Seventh instance, and this one should be routed as a CLOSE rather than a recurrence.** Round 6 attached the remedy — *"boundary-check `rows_excluded` as well as `rows`; that is two lines and it closes the class without a vocabulary at all"* — and the pass implemented it exactly. I forced six demotion forms, including both of Round 6's own bypasses, and all six halt. **When a portfolio item names a structural remedy and a pass implements it, the item should come back as closed with the forcing attached as evidence.** The vocabulary regexes (`NEG_CLAUSE`, `AVAIL_CLAUSE`, `USE_VERB`) are still load-bearing for the §4 *"named, not drawn on"* column, so the class is narrowed rather than eliminated — but the boundary breach it kept producing is gone.

- **Governance or methodology — one open, and I checked it rather than accepting it.** Doc_09 §8 item 7 escalates which half of CF's Tier 3 definition governs at `lpcstory006`. I read CF V7.4's Tier 3 paragraph whole from my own extraction. The genus clause is exactly as quoted — *"Material attributed to specific figures or moments but resting on collected tradition rather than direct documentation"* — the hagiographic sentence is explicitly *"a specific type **within** this tier,"* and **CF does not say which governs when they conflict**. Pontius is direct documentation by a named eyewitness deacon. The escalation is well-formed, correctly separated from the withdrawn *"a source is not a tier"* question, and stated at full strength in the chunk. **I would sustain it.** I repeat the standing advice: the *Acta* is Latin at `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` from l. 41413, `INTAKE.md` licenses it, and reading it would likely move `lpcstory006` to Tier 1 and moot the question.
 **A second methodology item, new and arising from HIGH-2.** Doc_05's open item 10 and Doc_09 §7 item 5 disagree about the same source: Doc_05 says the *Vita* is **unread**, Doc_09 says the material in it is **unwritten**. A world build that routes an absence from one document to another should re-read the routed-to document's own open items. That is a convention, not a ruling, and I raise it as one.

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. §6 item 5 and §8 item 4 state it accurately.

- **A methodology observation about the pass itself.** Round 6 named the mechanism as *"the pass verified the sentences it changed and did not verify the sentences it left."* **That has been half-fixed and half-inverted.** This pass did re-test sentences it left — `lpcstory007`'s absolutes, `lpcstory003`'s future tense, the *Acta* characterisation — and closed them. What it did not do is re-check the **counts and neighbours its own edits invalidated**: §4's *"Four"* (MEDIUM-4), the Disposition's round list and HIGH tally (MEDIUM-5), §2's *"five sites across four chunks"* (LOW-2), §8 item 2's *"Three"* (LOW-9), the Decision Log's *"79"* (LOW-3). The convention that would catch all five: **when an edit adds or removes an enumerated item, grep the document for every number that could be counting it — and prefer to derive the number in the generator, which already parses the sections these counts describe.**

---

# Check confirmation — including two defective checks of my own

**Two of my own checks failed before reporting.** I record them first, because trusting a check that returns something adjacent to a claim is this build's documented meta-defect and I am not exempt from it.

**Defective check 1 — quotation matching that broke on terminal punctuation.** My first quotation run reported 73 misses across the chunks, including *"still in the early days of his faith, and in the untaught season of his spiritual life."* and *"Persons who favoured him had climbed up into the branches of the trees."* Every one was an artifact of including the closing period inside the search string where the ANF prints a comma or a dash. Caught by progressive prefix truncation against the stream and printing the source context. Had I trusted it, it would have produced a fabricated mass-transcription HIGH against the cleanest chunks in the set.

**Defective check 2 — a note mask that produced eight false "editorial apparatus" hits.** After fixing check 1, eight quotations resolved with `all(in_note)` True — including `lpcstory004`'s hundred thousand sesterces and `lpcstory001`'s *Ep.* LXXVI ordination clause. **That would have been a fabricated HIGH of the exact class the portfolio ledger tracks.** Caught by printing each hit's own source context: in every case the chunk quotes a continuous span of **body text** that the ANF interrupts with a bracketed editorial note, and my note-stripped stream substitutes a space at that point, so the match spans the note's original character range without any of its words. The chunks step over the apparatus correctly. The finding is **zero**, and it took the second method to see it.

## Confirmations, one for every finding resting on a negative or a forced result

**C1 — the ANF harness, both directions.** Body text found and marked not-in-note (*"the judgment of God and the favour of the people"*, Pontius, p. 269, title `The Life and Passion of Cyprian…`); five randomly sampled note fragments from five different works found in the with-notes stream and returning **zero** hits in the note-stripped stream; a nonsense string returns MISS in both. All controls pass.

**C2 — the Possidius harness.** Exact hits with file line for 19 quotations across two separated regions of the English stream (the siege chapters and the death chapters); *"we who were present"* correctly returns **MISS**, which is the string the chunk itself records as occurring zero times — a positive control the build supplied; nonsense returns MISS; a punctuation-free second stream agrees on the two hyphenation-sensitive cases.

**C3 — for HIGH-1.** Old and new modules loaded side by side. Constructed case with a matched single-notice control (`notice-only` → `live` when the second notice is deleted); the absent-phrase control returns `absent`; a phrase far from any notice returns `live` under both. On the live files, the 15 sites are computed by subtracting characters already covered by some other span, so the 14,337 figure is *newly* swallowed text only.

**C4 — for HIGH-2.** Chapter headings XIX–XXVII extracted from the printed `CHAPTER N` lines of my own English stream, not from a table of contents; chapter XXII read whole; row 192 read in full (**Native**, **Vendored**, bilingual with a complete English translation); `Doc_05_Ecological_Reconstruction.md` open item 10 read in full; `Doc_09` and all seven chunks grepped for *"XIX"*, *"XXII"* and *"ordinary pastorate"* — the chapters are cited **nowhere**, so the omission is total rather than a citation I missed.

**C5 — for MEDIUM-1.** Row 27 read in full (**Native**; `role: tradition`; `confidence: provisional`; double-placed with `donatism.yaml` as `role: context`); `Doc_02_Source_Ecology.md` §1 read whole for the placement, and §7 read whole for the *"richly attested"* clause, which is verbatim in Doc_09 §1 — so §1's quotation is exact and only §7 item 1's paraphrase is at fault.

**C6 — for MEDIUM-2.** Three constructed inputs run through the committed `live()`, each deleting a live sentence with `unterminated()` returning `[]`; the truly-empty-line case run as the positive control and passing; a one-character mutation of the committed `Doc_09` §6 item 1 losing 281 words of live prose with `unterminated()` still returning `[]`; and a scan of the nine deliverables locating the 14 notices that sit in list or table context.

**C7 — for MEDIUM-3.** Whitespace-normalised occurrence counts over the whole file and over the body separately, with the OCR form as the positive control (1 hit in the body) and the normalised form as the negative (0 in the body, 1 in the header); the file's own Provenance note read for its statement that the header's quotations are not authoritative; rows 194 and 204 read for the build's own disclosure convention.

**C8 — for MEDIUM-4, MEDIUM-5, LOW-2, LOW-3 and LOW-9.** Each count recomputed from the artifact it describes: §6 items enumerated (5); the Disposition's round list enumerated (5 under a claim of 6) and the HIGH tally recomputed from the round counts (9 across 6); the capitalisation sites found mechanically with both a positive control (it recovers all five Round 6 named) and a negative control (it does not fire on *"No one regarded anything besides his cruel gains"*, which is sentence-initial in the source); notice spans counted with both modules on both the pre-pass and post-pass files (71 → 75, not 79); §8-by-item-number references enumerated by a pattern that does **not** require the `Doc_09` prefix, which is how the fourth was found.

**C9 — for the generator credits.** 17 halting sites from my own AST walk; `GUARD_LABELS` length 17 read from the syntax tree; **all 17 forced from 17 fresh copies of the world tree**, each returning rc 1 with its own distinct message, plus a clean control run at rc 0 on an unmodified copy. MEDIUM-4's bypass retested in six forms with the plain positive control. LOW-3 forced by neutralising the guard so the renderer alone decides. LOW-4 forced in both directions. LOW-5 forced with a stub Round 7 artifact. LOW-7 forced with five distinct malformed and well-formed notices.

**C10 — negatives that held, tested and passed.** Recorded because they could have been findings and are not. *"No one who fled Hippo wrote down what leaving was like"* — `salvian_on-the-government-of-god_sanford1930.txt` searched for *refugee*, *fled*, *exile*, *Hippo*, *Carthage*: the search is live (60 hits for *Vandal*, 13 for *Carthage*, 12 for *exile*) and finds **zero** for *Hippo* and no first-person African refugee voice; Salvian writes Carthage 439 from Marseilles. *"No English translation of [the* Acta *] exists anywhere in this corpus"* — held. *"The lapsed have no story of their own"* — *Ep.* XX read whole; Numeria and Candida are named and discussed and neither speaks. *"Where she searched, the letter does not say"* — *Ep.* XXXIV read whole; no locative. *"Not one of them left an account of their own"* of Cyprian's execution crowd — held. *"No story survives in the voice of an ordinary believer"* — held; Possidius is a bishop, which is why §7 item 2 survives where §7 item 5 does not. **Row 9 is `Native` and the *Confessions* is vendored** in NPNF and in Latin at row 197, so §6 item 3's *"row 9, Native, vendored"* is sound even though row 9's own Vendoring cell does not carry the stamp.

**What I tested hardest.** In order: the two scripts, by 17 forced halts, six bypass probes, five guard probes and a bidirectional attack on the stripper — which is where HIGH-1 and MEDIUM-2 were. Then every absolute negative in live prose, one by one at source — which is where HIGH-2 was, and where six others held. Then every count the pass's own edits could have staled — which is where MEDIUM-4, MEDIUM-5, LOW-2, LOW-3 and LOW-9 were. Then every quotation, through three purpose-built harnesses — which found one transcription problem (MEDIUM-3) in 109 quotations, and that is the finding.

**What would change the verdict.** Fixing **HIGH-1** (bound `classify`'s span extension by the container, or revert it), **HIGH-2** (one sentence in §7 item 5 plus a §6 item), **MEDIUM-1** (one clause) and **MEDIUM-3** (disclose the normalisation). With those, **MINOR REVISION** on this same reading. **On the story content alone, considered apart from the instruction layer and the tooling, I would clear this document** — seven rounds have now verified every quotation independently and found no composite and no invention, and that is what Doc_10 consumes as narrative.

**If a fix pass disagrees with HIGH-2, the thing to produce is not an argument but the text:** a reading of `possidius_vita-augustini_weiskotten1919.txt` chapters XIX through XXVII, and of `Doc_05`'s open item 10, on which *"the daily work … is the one thing no story records, because nobody writes it down"* is true.

---

# Job 5 — the Decision Log's Round 6 entry, checked for honesty

**Mostly honest, and better than the deliverable it describes. Four problems.**

**What checks out.** *"33 of Round 5's 38 findings were verified closed"* — Round 6's own figure, correctly attributed. *"All 16 halting sites forced"* — Round 6's count, correct for Round 6. *"Closed structurally rather than by vocabulary — `rows_excluded` is now boundary-checked too"* and *"both of Round 6's own positive controls (`available`, `pending`) now halt"* — **true, and I forced both plus four more.** *"L2 (ten section-separator rules deleted by the notice mover, restored; every `##` heading in all seven chunks now has one, verified)"* — **true, and my own mechanical check agrees at every heading including the four new `###` ones.** *"L7 … now a halting site, forced"* — true, and it survives five probes. *"L5 … keyed to `FIXED` … forced"* — true, reproduced. The three brief errors are reported accurately and the *"eight instances of editorial apparatus"* correction is restated correctly as **zero**, which my independent check confirms for a seventh time.

**Problem 1 — "Verified at source" is claimed for a string that is not at source.** The entry prints the Prosper quotation and says *"Verified at source."* That exact string occurs **zero times** in `prosper_chronica-minora-1-lat_mommsen1892.txt`; it occurs once in the file's **header**, which says it is not authoritative. See MEDIUM-3. The *fact* was verified; the *string* was not, and the entry does not distinguish them.

**Problem 2 — a new stale literal replaces the old one.** *"(**79** spans as of Round 6)"* — the figure is 71 before the pass and 75 after. See LOW-3.

**Problem 3 — a claim about the test suite that does not describe it.** *"its check count is derived rather than typed"*; the suite emits no count. See LOW-4.

**Problem 4 — omission rather than misstatement, but material.** The entry records M6 as *"added as a candidate and carried at §8 item 8"* and does not record that the addition **renumbered §6 items 3 and 4** — so nothing in the log prompts the count check that would have caught MEDIUM-4. The pass's own Round 5 entry set the standard here: *"One defect this pass introduced and corrected rather than carried… Recorded because a fix pass that damages a deliverable and repairs it silently is the pattern this log exists to prevent."* The renumbering is a structural edit and belongs in the entry.

**What the entry gets right that the deliverable does not.** It says *"**Sixth consecutive round** of this document's signature defect"* — the correct running tally — on the same day the Disposition in `Doc_09` still says eight HIGHs across five rounds. The right number was written; it was written in the wrong file.

---

# Errors in this round's brief

**None found.** All three commit refs are correct and I verified each against `git log`. The premises the brief flags as known-false are correctly flagged: **editorial apparatus read as the world's voice is zero in this deliverable**, verified independently for a seventh time with a mask built before tag stripping and with two of my own false positives caught and discarded; and **CF line numbers are extraction-dependent**, which is why none appears above. The brief's warning about positional attribution in ANF05 is well founded and load-bearing — my harness resolves every quotation by `title=`, and the corpus does print Celerinus's, Lucian's and the Roman clergy's letters under Cyprian's name, so a positional check would misattribute at least `lpcstory005`'s two central quotations.

The brief's one prediction that did not hold: it directs attention to stale cross-references from the §6 renumbering. **There are none** — every live §6-by-item-number reference points at items 1, 2 or 3, which did not move. The count in §4 is what the renumbering broke, and the brief did not name it.

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**2 HIGH · 5 MEDIUM · 10 LOW · 4 COSMETIC.**

**This pass closed 21 of Round 6's 23 findings at every site each finding named, and I forced rather than read the tooling half of that — 17 halting sites from 17 fresh copies, six bypass forms all halting, five guard probes all halting, and a byte-identical index.** The story content is clean for the seventh consecutive round: every quotation at source, zero editorial apparatus, no invention. What holds the verdict at SUBSTANTIAL is that the two worst findings were both **made by this pass or left standing in the section it rewrote**: the fix for a LOW whose error direction was explicitly the safe one reintroduced Round 5's HIGH-2, and now reports 2,338 words of this document's own live prose as mention; and §7 item 5 tells a Representative that nobody wrote down the ordinary pastoral work this world's Primary gravity is built on, while nine chapters of it sit unread in the one source the document's second phase already depends on. That is the seventh round in a row in which this document's worst content finding is a silence asserted about a source the source refutes — and the second in which the refuting source is one the build itself vendored and then did not open.

*Simulated review — informational only, not an Article 31 substitute.*
