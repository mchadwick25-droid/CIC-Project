# Doc_09 — Round 6 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**1 HIGH · 6 MEDIUM · 12 LOW · 4 COSMETIC.**

**Say the large good part first, because it is large and it is new.** This is the first fix pass in six rounds that did most of what it said it did. Both of Round 5's HIGHs are genuinely closed at the sites Round 5 named. **MEDIUM-9 — build apparatus inside deployable Story Text, open since Round 2 — is closed in all seven chunks with zero prose lost**, which I verified word by word against the pre-pass commit. **Four LOWs that had been open for four consecutive rounds are closed, and I verified all four at source**: *Ep.* LXVII's address does name Cyprian and exactly thirty-six colleagues; Pontius §10 does read *"collected together those who were slain by the king and cast out"*; *Ep.* LI's omission is now reasoned rather than silent; the master table's confidence cell is short. All **sixteen** halting sites in `gen_story_index.py` fire when forced from sixteen fresh copies, the index regenerates **byte-identical**, and `GUARD_LABELS` matches the AST count exactly. `notice_strip.py`'s over-strip — Round 5's HIGH-2 — is gone: on constructed input and on the live deliverables, `live()` no longer deletes prose after an inline notice.

**What holds the verdict at SUBSTANTIAL is one finding, and it is the defect class that has now produced a HIGH in six rounds out of six.**

- **HIGH-1.** `lpcstory007` states **twice**, in live prose, that **"no second account of Augustine's death exists in this corpus."** `Source_Registry.md` **row 203** — Prosper of Aquitaine's *Epitoma Chronicon*, **Native**, grade **A**, **vendored** at `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt` — records the death under a. 430, with the date and the siege. The row's own Notes cell says it was acquired precisely to close *"this world's own end-window (Augustine's death, 430…), now independently attested by a contemporary Latin chronicle where previously this world's construction held none."* **Doc_02 §5 and Doc_08 both say so in as many words.** The claim is load-bearing: it is the reason the Tier Justification gives for the tier resting on the eyewitness claim alone.

The six MEDIUMs are: a second absolute negative whose stated cause its own cited source refutes (§7 item 1); Doc_09's Status header still frozen at Round 4; a standing claim in §8 item 2 that **this fix pass's own edits falsified**; a boundary-guard bypass that the new `AVAIL_CLAUSE` vocabulary widened rather than closed; a stated contract in `notice_strip.py` that is false and a test harness that structurally cannot catch it; and the absence of the *Confessions* from §6's candidate list.

**If HIGH-1 is fixed — two sentences in one chunk — and MEDIUM-1's clause is corrected, I would return MINOR REVISION on this same reading.** Nothing else here blocks Doc_10.

---

# Method — everything below was derived here

**I inherited nothing.** Not from the brief, not from the fix pass, not from Rounds 1–5. Three of the brief's premises turned out to be wrong and are recorded at the end as brief errors.

1. **Cyprian harness, built from scratch.** A character-by-character scan of `anf05_hippolytus-cyprian-caius-novatian.xml` carrying, for every output character, its innermost `<div1–4>` `title=` (work attribution **by title, never by position**), its `<pb n="">` page, and **whether it lies inside a `<note>` span, marked before any tag was stripped**. Two streams: with notes (3,456,476 normalised characters) and note-stripped (3,069,068). 497 titled divisions. A separate **ANF *Argument* index** built from the raw `<p>Argument…</p>` paragraphs (95 of them), so an editorial summary can be told from body text.
2. **Epistle numbers resolved from the printed headings**, not from order: 76 `Epistle N. Title` headings extracted and matched. *Ep.* XX = *Celerinus to Lucian*; XXI = *Lucian Replies*; XXVI = *Cyprian to the Lapsed*; XXXIII = ordination of Celerinus as **reader**; XXXIV = Numidicus; LIX = the Numidian ransom; LXVII = Spain/Basilides.
3. **Pontius sectioned.** The nineteen numbered sections of the *Life* located and every quotation in `lpcstory001`, `002`, `006` and Doc_09 resolved to its section.
4. **Possidius harness, built from scratch.** Weiskotten segmented by running head (`SANCTI AUGUSTINI VITA` = Latin page, `LIFE OF SAINT AUGUSTINE` = English page), English-only stream reconstructed (177,055 chars), **de-hyphenated at line ends**, spaces before punctuation dropped, plus a word-only stream with all punctuation stripped as a second method, and a chapter map.
5. **Four letters read whole** rather than searched: *Ep.* XX, XXI, XXVI and XXXIV.
6. **CF V7.4 extracted from the .docx myself** (722 paragraphs) and every CF quotation in Doc_09, the chunks and the index matched against it.
7. **The generator.** Halting sites counted by my own AST walk (**16**), all sixteen forced from sixteen fresh copies, plus seven further mutation probes hunting for fail-open behaviour, each with a matched positive control.
8. **`notice_strip.py` attacked in both directions** with constructed input, and its whole notice inventory scanned across all nine deliverable files.
9. **Every chunk diffed against the pre-pass commit** (`a6a6be73`) at the level of headings, horizontal rules, front-matter fences, notice inventory, bold balance, and Story-Text word multiset.
10. **Every absolute negative in Doc_09 and all seven chunks**, extracted from *live prose only* (notice spans removed), and tested against source.

---

# Job 1 — auditing the Round 5 fix pass's claims

The Document Log's claim is *"Both HIGH closed; all 10 MEDIUM, all 20 LOW and all 6 COSMETIC addressed."* Checked at **every** site each finding named.

### Closed — verified in the live text

| R5 finding | Verified how |
|---|---|
| **HIGH-1** — `lpcstory005` Usage Guidance | Rewritten; it now names Numeria and Candida and says *"The absence is of the lapsed voice, not of lapsed names."* I read *Ep.* XX whole: the rewrite is accurate to it, and to §7 item 3, at every clause |
| **HIGH-2** — `notice_strip.live()` over-stripping | Gone. On Doc_09 §7 the retention is 78% (was 52%); §2's escalation paragraph returns 929 words (was one space). Reproduced on constructed input too. *But the new contract is overstated — MEDIUM-5* |
| M1 — Decision Log enumeration | The Round 5 entry now enumerates H1, H2, M1–M10, L1–L20, C1–C6 by ID |
| M2 — §2 routed a withdrawn escalation | §2 l.41 now reads *"the escalation was WITHDRAWN at Round 4 and the Disposition records the withdrawal"* |
| M3 — Disposition recited two HIGHs | Now *"Eight HIGH findings… across five rounds"*; I recounted 2+0+1+3+2 = 8, and the 6/1/1 breakdown holds |
| M4 — index credited `lpcstory003` with rows 191/194 | §4 now prints `1 · *named, not drawn on: 191, 194*` |
| M5 (parts 1 and 3) — case-sensitive row regex; gravities fail-open | `re.IGNORECASE` added and forced; empty §3 Gravities cell now halts, forced. *Part 2 open — MEDIUM-4* |
| M6 — `lpcstory002` denied what its own §10 quotation says | Rewritten; the new form quotes §10 and confines the denial to the narrow question. Verified §10 at source |
| M7 — `lpcstory006` characterised the *Acta* unopened | Narrowed to *"not one of them left an account of their own"*, which holds. *A new unwarranted claim replaced it — LOW-6* |
| M8 — `lpcstory007` re-asserted an absolute after quoting the answer | The clause is deleted; the note now ends *"The scale is documented… The experience is not."* |
| **M9 — notices inside deployable Story Text (open since Round 2)** | **Closed in all seven chunks: zero notice spans inside `## Story Text`.** I diffed the Story-Text word multiset against `a6a6be73`: **no prose lost in any chunk.** *No guard added — LOW-7* |
| M10 — index masthead named a grep as the remedy | Now *"counted off this script rather than typed"* |
| L1 — Absent Story Note before Usage Guidance | Reordered in all six chunks; matches the L4 template's order. *Rule separators lost — LOW-2* |
| L2 — §2 Tier 2 band trimmed | CF's continuation restored, verified against my own .docx extraction. *Tier 3's continuation still trimmed — COSMETIC-1* |
| L3 — *Ep.* LI dropped without a reason | Now stated in chunk 001's Source field |
| **L4 — Tobias "buried"** | Now *"collected together those who were slain by the king and cast out"* — **exact against Pontius §10, body text, note-stripped stream.** Fourth round, closed |
| **L5 — *Ep.* LXVII called Cyprian's own letter** | Corrected at **both** named sites. **I counted the address: 37 names, i.e. Cyprian + 36 colleagues.** The chunk's *"Cyprian, Cæcilius, Primus, Polycarp and thirty-three more"* is also exactly right. *Grammar broke — LOW-9* |
| L6 — the Doc_02 §9 item 10 reversal unnamed | §2 l.39 names it; Doc_02 §9 item 10 verified to read *"in terms matching the Framework's own Tier 3 definition"* |
| L7 — chunk 006 never engaged CF's genus clause | Now quoted at full strength in the Tier Justification and escalated at §8 item 7. Quotation exact against CF |
| L8 (half) — review history keyed to artifact existence | The fix-pass claim now comes from Doc_09's Document Log. Reproduced: with a stub Round 6 artifact the Disposition correctly says *"no fix pass has been recorded against it."* *The Status line still fires — LOW-5* |
| L9 (half) — substring confidence-band guard | The **guard** now compares whole tokens with a `not `-lookbehind. *The rendered audit column does not — LOW-3* |
| L10 — all-whitespace Phase cell | Forced: halts |
| L11 — index nests a notice in a notice | Ran the generator's own `assert_coverage` over `lpc_Story_Index.md`: passes |
| L12 — eight guards listed under a count of thirteen | `GUARD_LABELS` has 16 entries, my AST walk counts 16, and the mismatch is itself a forced halting site |
| L13 — §6 item 2 quoted row 41 unattributed | Now *"in `Source_Registry.md` row 41's own words"*; row 41's Notes cell verified to carry that exact string |
| L14 — "Two facts close the chapter" | Now *"Two details follow, mid-chapter"* |
| L15 — duplicate story ids | Forced: halts |
| **L16 — the *Acta* pointer's section** | Now cited as **§11**. Verified: *"what God's priest replied to the interrogation of the proconsul, there are Acts which relate"* is in §11, and §11 opens **"Banishment followed these actions"** — exactly as the chunk says |
| L17 — three under-strip cases | All three fixed; italic prefixes, long prefixes and `]` inside the body all handled, reproduced |
| L18 — two strippers, one claim | Explained in the script and asserted by test G1; the two now agree to the word on §2 and §7 |
| **L19 — inner quotation marks** | Restored. Weiskotten reads `"he slept with his fathers," as it is written, "well-nourished in a good old age."`; the chunk now nests them |
| L20 — §3 row comparison one-directional | Both directions compared now. *With a grouping bug — LOW-4* |
| C1 — index §1 confidence cell | Short band in the cell, full band printed below |
| C4 — CF Tier 4 governing condition | Restored, verified at CF |
| C5 — `global BANDS` in the loop | Now module-level |

### Partial or not closed

| R5 finding | What is live |
|---|---|
| **M5 part 2** — incidental negation demoting a used row | Still bypasses the boundary guard, and the new `AVAIL_CLAUSE` **widened** the bypass to the words *"available"* and *"pending"*. Forced with a positive control. **MEDIUM-4** |
| **L9** — substring band test | The §3 audit table still prints `any(b in s["conf"] …)`. Forced: with the guard relaxed the table prints *"**Yes** — Not Documented"*, which is the exact output L9 reported. The script's own comment says this redundancy exists as a backstop; the backstop was not fixed. **LOW-3** |
| **L8** — index Status line | Reproduced: a Round 6 artifact on disk makes the index say *"REVISED after Round 6 — the revision is unreviewed"* four lines above its own Disposition saying no Round 6 fix pass exists. **LOW-5** |
| **C2** — §8 item 2's placeholder rationale | The reason given is now **false, and this pass falsified it**. **MEDIUM-3** |
| **C3** — the L8 boilerplate | De-duplicated to a one-liner, still repeated verbatim in six chunks, and **the one-liner's markdown is broken**. **LOW-1**, COSMETIC-3 |

**Honest summary of the pass: 33 of Round 5's 38 findings are closed at every site the finding named; 5 are partial.** That is a real change from the three-to-six-findings-per-pass pattern the last three rounds diagnosed, and it should be said plainly. The one-line findings at named sites were visited this time. **What the pass did not do is check whether its own new sentences were true** — which is where HIGH-1, MEDIUM-1 and MEDIUM-3 come from.

---

# Findings

## HIGH

### HIGH-1 — `lpcstory007` asserts twice that no second account of Augustine's death exists in this corpus. Registry row 203 is a contemporary chronicle that records it, vendored for that purpose, and Doc_02 and Doc_08 both say so

**Sites.** `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md` **l. 55** (Tier Justification) and **l. 73** (Absent Story Note). Live prose, no notice near either. Neither sentence was written by this fix pass; neither has been tested by any previous round.

**What the chunk says.**

> l. 55: *"One limitation stated rather than absorbed. Possidius is writing in praise… The ordinary corrective — check the detail against another witness — is unavailable: **no second account of Augustine's death exists in this corpus.** The tier rests on the eyewitness claim and the absence of genre machinery, not on corroboration."*

> l. 73: *"Possidius is the only witness to Augustine's last weeks; **no second account of his death exists anywhere in this corpus**, so the ordinary corrective of checking a detail against another witness is unavailable here and nowhere else in this repository is a Tier 1 story so wholly dependent on one man."*

**What the corpus contains.** `Source_Registry.md` **row 203**:

> *"Prosper of Aquitaine, Epitoma Chronicon, with its African continuations — Theodor Mommsen (ed.), Chronica Minora Saec. IV–VII, Vol. I … | P | **A** | **Native** | — | **This world's own end-window (Augustine's death, 430; the Vandal capture of Carthage, 439), now independently attested by a contemporary Latin chronicle where previously this world's construction held none** | **Vendored** at `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`."*

I opened the file. At the printed year 430 (file l. 54201–54204):

> *"Aurelius Augustinus episcopus per omnia excellentissimus **moritur** V. kl. Sept., libris Iuliani **inter impetus obsidentium Vandalorum** in ipso dierum suorum fine respondens et gloriose in defensione Christianae gratiae perseverans."*

Augustine dies on 28 August, answering Julian's books **amid the assaults of the besieging Vandals**, at the very end of his days. That is a second witness to the death, its date, and the siege — the three things the chunk draws from Possidius and says cannot be checked.

**And this build already knows.** `Doc_08_Forces_Document.md` l. 230: *"**A near-contemporary Gallic chronicler independently records the death under that year (Registry row 203).** Confidence: Documented."* `Doc_02_Source_Ecology.md` §5: *"A contemporary witness is now vendored: Prosper of Aquitaine's Epitoma Chronicon (Registry row 203) … **independently locating and quoting Augustine's own death under the year 430**."* Doc_09's own header declares Doc_01–Doc_08 as its input documents.

**Why this is HIGH and not MEDIUM.** Three reasons, and each is sufficient on its own.

1. **It is not a shading, it is a flat false negative, stated twice, in two different fields.**
2. **It is load-bearing on a tier.** The Tier Justification uses it as the premise of its closing sentence — *"The tier rests on the eyewitness claim… not on corroboration."* Corroboration exists. And `lpcstory001`'s Tier Justification says, in this same repository, that what settles a tier is *"corroboration outside [the author's] own frame."* By that rule `lpcstory007` has what `lpcstory001` says a Tier 1 needs and reports that it does not.
3. **It is the sixth consecutive round's instance of this document's defining defect** — a silence asserted about a source that the source refutes — and this time the refuting source is a **Native, grade-A, vendored row of this world's own Registry**, acquired and logged for exactly this gap.

**Fix.** Two sentences.
- l. 55: *"The ordinary corrective is thin rather than absent: Prosper of Aquitaine's chronicle (Registry row 203) independently records the death, its date and the siege, but nothing corroborates the interior of the room. The tier rests on the eyewitness claim and the absence of genre machinery."*
- l. 73: *"Possidius is the only witness to Augustine's last weeks — Prosper records the death and the year and nothing of the fortnight before it — so the ordinary corrective of checking a detail against another witness is unavailable for everything this story is actually made of."*

Both are truer and both are sharper.

---

## MEDIUM

### MEDIUM-1 — §7 item 1 says nothing survives from the 133-year silence; §1 relays a claim about the Registry that row 27 of the Registry refutes, and the Doc_02 section cited as authority says the opposite in its own preceding clause

**Sites.** `Doc_09_Story_Inventory.md` **l. 115** (§7 item 1) and **l. 23** (§1). The index's §5 singles out §7 item 1 as *"the one to test hardest."*

**What the document says.**

> l. 115: *"Between Cyprian's martyrdom in 258 and Augustine's ordination in 391, **this world tells itself no stories at all** — not because nothing happened, but **because nothing survives.**"*

> l. 23: *"Doc_02 §7 records that **no primary source named at §1 and no row in `Source_Registry.md` dates from within it.**"*

**What the Registry contains.** **Row 27: Optatus of Milevis, *Against the Donatists* (Books I–VII), Boundary Status **Native**, vendored** at `cic/texts/optatus_against-the-donatists.txt` — and a second Latin witness at row 64's note, `optatus_libri-vii-critical_ziwsa1893.txt`. Both files' own headers date the original **c. 366–393 CE**: squarely inside the 258–391 interval. Optatus is an African bishop writing African church narrative from inside the gap, and an **English translation is vendored** (Vassall-Phillips 1917). Rows 44 and 88 (the *Codex Theodosianus*) carry constitutions from inside the interval too.

**And Doc_02 §7 says so itself, in the sentence before the one Doc_09 quotes:** *"…since the interval is in fact **richly attested** — through sources that are Donatism's own territory (World #4), not this world's. This document discharges that binding directly: no primary source named at §1 above, and no row in `Source_Registry.md`, dates from within this 133-year gap."* The second sentence contradicts the first, and Doc_09 relayed the wrong half.

**Why this matters.** The chunk `lpcstory005`'s own Absent Story Note states the governing principle: *"Article 20 requires the reason for an absence to be named correctly, not merely dramatically."* The absence here is real — this world tells no stories from the interval — but the reason is **boundary assignment**, not survival. Saying *"nothing survives"* tells a Representative that the period is dark. It is not dark; it is somebody else's. That is precisely the Round 4 H3 operation (source loss vs. never-asked) at a new site, and it is the second absolute negative in this document that its own cited source refutes.

**Fix.** *"…not because nothing happened, and not because nothing survives — the interval is richly attested — but because what survives from it is Donatism's territory rather than this world's. Registry row 27 (Optatus of Milevis, c. 366–393) is Native to this world and narrates from inside the gap; no story is built from it because the corpus map homes that material elsewhere."* And strike the Registry half of §1 l. 23, or attribute it as Doc_02's claim rather than restating it.

### MEDIUM-2 — Doc_09's Status header is still frozen at Round 4, four lines from a `[CORRECTED]` notice about that exact failure, and three other places in the same build say Five

**Site.** `Doc_09_Story_Inventory.md` **l. 5**.

> *"**Status:** **REVISED after Round 4 — the revision is unreviewed, and not self-disposed.** **Four independent adversarial review rounds have been run**; `lpc_Story_Index.md` derives its own copy of that count by reading `Review-Artifacts/`."*

Against, in the same file: the **Document Log** (l. 152–153) records the Round 5 review *and* the Round 5 fix pass; the **Disposition** (l. 159) says *"**REVISED after Round 5**… **Five rounds have been run**"*; and the generated **index** l. 3–4 says *"REVISED after Round 5 … Five round(s)."*

`git diff a6a6be73 HEAD -- Doc_09_Story_Inventory.md` returns **no change to the Status line at all** — the fix pass never touched it.

**Why this matters.** The sentence that is stale carries, inline, the notice recording that it was stale before: *"[CORRECTED, 2026-09-15 — Round 3: this read 'DRAFT — not reviewed' through two review rounds… **The Round 2 remedy landed in the generated sibling and not in the hand-maintained document**]."* The remedy has now failed to land in the hand-maintained document for the **third** time, in the line that documents the previous two failures. It is also the one line a reader checks first.

**Fix.** One line, and add a Document-Log convention that the Status line is rewritten in the same edit as the Log row.

### MEDIUM-3 — §8 item 2's stated reason for keeping a placeholder is false, and this fix pass is what made it false

**Site.** `Doc_09_Story_Inventory.md` **l. 130**.

> *"Kept as a numbered placeholder so the numbering in this document's own review history stays readable; **nothing in the world build cross-references §8 by item number.**"*

Grepping `Doc_09 §8 item N` across the world build, excluding `Review-Artifacts/`:

- `Story-Chunks/lpcstory006_the-death-of-cyprian.md` l. 59 — *"Doc_09 **§8 item 1** carries it open"*
- `Doc_09_Story_Inventory.md` l. 165 (the Disposition) — *"**Doc_09 §8 item 7** carries it"*
- `lpc_Decision_Log.md` l. 1453 — *"Doc_09 §8 item 7"*

**All three were written by this fix pass.** At `a6a6be73` the same grep over both files returns nothing, so Round 5's COSMETIC-2 was right when it was made and the sentence was true. The pass added two cross-references to §8 by item number and left standing the sentence saying there are none.

**Why this matters.** This is the document's signature defect in miniature and in the cheapest possible form: an absolute negative about the build's own text, refuted by the same commit that left it standing. It also means a future editor renumbering §8 will break two live pointers while reading a sentence that tells them nobody points at §8.

**Fix.** *"Kept as a numbered placeholder because §8 items 1 and 7 are cross-referenced by number from `lpcstory006` and from this document's own Disposition."*

### MEDIUM-4 — the `AVAIL_CLAUSE` fix widened the boundary-guard bypass instead of closing it: the words "available" and "pending" now take a row out of the Excluded-row check with no halt

**Site.** `scripts/gen_story_index.py` ll. 39–48 and 151–167. Forced from fresh copies, with a matched positive control.

**What I found.** Round 5's MEDIUM-5 had three parts. Two are fixed. The third — *"incidental negation demotes a used row"* — was answered by adding `USE_VERB` and halting only when a clause carries **both** a demoting phrase **and** one of eight verbs (`supplies|supply|provides|provide|gives|give|carries|carry|is drawn on|are drawn on|draws on`). Any other verb, and the demotion is silent.

The same edit added `AVAIL_CLAUSE`, which matches `\bavailable\b`, `\bpending\b`, `\bnot yet\b`, `\bwould let\b`, `\bsecond witness\b` and three more, and routes the row into `rows_excluded` — **which is never boundary-checked**. `allrows` is built from `s["rows"]` only.

**Forced, from fresh copies of the world tree:**

| `lpcstory003` Source field tail | result |
|---|---|
| `Row 28 supplies the acclamation wording above.` (§3 names row 28) | **rc 1** — *"FATAL: story source row(s) ['28'] are not Native in Source_Registry.md ({'28': 'Excluded'}). A story sourced to an Excluded row is a boundary breach."* |
| `Row 28, the only comparandum **available** here, underlies the acclamation wording above.` | **rc 0** — §4 prints `` | `lpcstory003` | 1 · *named, not drawn on: 28* | row 1: **Native** | `` |
| `Row 28 underlies the wording above, **pending** a fuller check.` | **rc 0**, same |
| `Row 28 underlies the wording above, though it **does not** settle the date.` | **rc 0**, same |

The positive control halts; adding one ordinary English word makes an Excluded row invisible to the guard whose output is printed under *"**Every row a story actually draws on is Native**… The check is mechanical."*

**Why this matters.** Round 5 named this defect *"a guard defeated by orthography"* and routed it portfolio-wide with the remedy attached: *"a derivation that reads prose inherits prose's variability, and the remedy is a declared field, not a better regex."* The pass wrote a better regex, and the new vocabulary is **more** collidable than the old — `available` and `pending` are among the commonest words a Source field would use. Fixing an instance and enlarging the class is the fifth appearance of this shape.

**Fix.** Boundary-check `rows_excluded` as well as `rows` — a row this world may not use is a breach whether or not the chunk says it used it. That is two lines and it closes the class without a vocabulary at all.

### MEDIUM-5 — `notice_strip.py` states a contract it does not implement, and the test suite's "independent" checker shares the defect

**Site.** `scripts/notice_strip.py` docstring ll. 38–41 and 70–75; `scripts/test_notice_strip.py` ll. 80–103.

**The stated contract.**

> *"`live()` removes Form A spans ONLY. **It NEVER deletes prose outside a bracket, so it cannot hide a live assertion.**"*

**It can.** `_NOTICE` is `\*{0,2}\[(TAGS)\b(?:[^\]]|\](?!\*\*))*?\]\*\*` compiled with `re.S`. The body can cross blank lines, so the span is bounded not by the notice's own end but by **the next `]**` anywhere later in the file**. A notice whose terminator is mistyped `.]` instead of `.**]**` swallows everything up to the next well-formed notice. Constructed and run:

```
**[MOVED, 2026-09-15 — Round 6:** moved from Story Text.]

Numeria and Candida are discussed, weighed, and dispatched to peace.

**[ADDED — Round 5:** narration.**]**
```
`live()` returns `' \n'`. The live sentence is gone. A second case with a bare `[CORRECTED]` in ordinary prose swallows an intervening paragraph the same way.

**The test cannot catch it.** `independent_live_words()` is offered as *"a second, independent implementation… Shares no regex with the module under test."* It shares no regex and **the whole algorithm**: `j = txt.find("]**", i)` — skip from `[TAG` to the next `]**`. It reproduces the failure exactly, so F1 agrees with `live()` while both are wrong. F2 is weaker still: `removed = [w for w in sec.split() if w not in live(sec).split()]` is word-**membership**, so any deleted word that occurs elsewhere in the section is invisible, and the containment test uses `sec_.find(w)` — the *first* occurrence of the word, not the one that was removed.

**What saves the build today, and it is luck rather than design.** I scanned all nine deliverables: **71 notice openers, 71 matched spans, 0 uncovered, 0 spans crossing a blank line.** The defect is latent. Its trigger is a one-character typo in a notice terminator, in a build that writes notices by hand and has already shipped one malformed notice this pass (LOW-1).

**Why this matters.** The file's own closing line is *"A control stated more broadly than it is implemented is worse than no control, because the next round will trust it."* That sentence is presently describing its own docstring.

**Fix.** Forbid the body from crossing a blank line (`(?:[^\]\n]|\n(?!\n)|\](?!\*\*))*?`), and make one test genuinely independent — e.g. assert that every removed character index lies within a span found by a *paragraph-scoped* scanner.

### MEDIUM-6 — §6's "candidates considered and not built" omits the *Confessions*, which this world's Registry calls the founding first-person document of its own second half

**Site.** `Doc_09_Story_Inventory.md` §6, and the document as a whole: the string *"Confessions"* occurs **zero** times in Doc_09 and zero times in any of the seven chunks.

**What I found.** `Source_Registry.md` row 9: *"Augustine, *Confessions* | P | B | **Native** | — | Augustine's own conversion narrative (386–387); **the founding first-person document of this world's own Augustine half** (Doc_01 §2)."* It is vendored in Latin (row 197) and in English in the NPNF corpus. Doc_02 §1 lists it first among Augustine's vendored works.

Phase Two of this world is represented in Doc_09 by **one story, from one source, one chapter long**. The single most narrative-dense Native source in the world's second half is not built, not excluded, and not mentioned. §6 records four candidates — the Perpetua sermons, the *Acta*, *City of God* XXII.8, and the 411 *Gesta* — and the *Confessions* is not among them.

**Why this matters.** CF requires Doc_09 to be *"a complete catalog of stories available within the world"* (Step 9, my extraction l. 700), and §6 exists to record what was weighed and set aside. An omission this large makes §6's list unreliable as a record of what was considered, and it leaves the document's own §7 item 5 — *"There is no story of an ordinary, uneventful pastorate"* — untested against the one Native source most likely to contain one.

**I am not saying a story must be built from it.** There are respectable reasons not to: the *Confessions* narrates Augustine's pre-episcopal life, much of it in Italy, outside the Africa-centred horizon §1 declares. That reasoning is exactly what §6 is for, and it is absent.

**Fix.** A fifth §6 item, three sentences, saying which of the *Confessions*' episodes are in-horizon and why none is built this pass.

---

## LOW

**LOW-1 — five chunks now carry a notice with unbalanced bold, introduced by this pass.** `lpcstory002` l. 81, `003` l. 63, `004` l. 57, `005` l. 67, `006` l. 63 all read:
`**[ADDED — Round 1's L8; the rollout decision and its exceptions are stated once in Doc_09 §7.**]**`
Three `**` runs, not four. Rendered: `<strong>[ADDED — … §7.</strong>]**` — a literal `**` on the page. The form it replaced was balanced; I rendered both to confirm. *Fix:* `…Doc_09 §7.]**`.

**LOW-2 — the notice mover deleted ten section-separator rules across six chunks, and the set is now inconsistent.** Before the pass, **every** `## ` heading in **all seven** chunks was preceded by a `---` rule. Now: `## Absent Story Note` has no preceding rule in any of the six chunks that carry one, and `## Usage Guidance` has none in `002`, `003`, `004` and `007` but does in `005` and `006`. `lpcstory001` is untouched and still consistent. Mechanically confirmed against `a6a6be73`, which returns an empty list for every file.

**LOW-3 — the No-Tier-5 audit column still uses the substring band test that Round 5's L9 reported.** `gen_story_index.py` l. 457: `in_band = any(b in s["conf"] for b in BANDS[s["tier"]])`. The *guard* at l. 135–136 was rewritten to compare whole tokens with a `not `-lookbehind; the renderer was not. Forced — with the guard neutralised, a chunk declaring **"Not Documented"** makes the table print `| lpcstory001 | 1 | **Yes** | **Yes** — Not Documented |`, which is L9's reported output verbatim. The script's own comment at that line says the duplication exists precisely *"so that the table cannot go stale if a guard is ever relaxed, and the redundancy is the point."* The redundancy is now asymmetric: the backstop is the weaker of the two.

**LOW-4 — the new §3 `_missing` comparison compares unsplit row groups against split rows, producing a false FATAL.** `gen_story_index.py` l. 245: `_missing = set(s["rows"]) - csrc_rows`, where `s["rows"]` holds raw capture groups such as `"191/194"` while `csrc_rows` is split on `[/,]`. Forced: a chunk drawing on `rows 191/194` and a §3 cell naming `rows 191, 194` halts with *"the chunk draws on row(s) ['191/194'] that Doc_09 §3's Source column does not name."* Fails closed, so it is not dangerous — but it is a guard that cannot be satisfied by correct input, introduced in the fix for L20. *Fix:* split both sides before differencing, as the three neighbouring comparisons already do.

**LOW-5 — the index's Status line will assert a Round 6 revision that has not happened, the moment this file lands.** Reproduced by dropping a stub `Doc09_Round6_Review.md` into a copy and regenerating: l. 3 reads *"**REVISED after Round 6 — the revision is unreviewed**"* while l. 122 correctly reads *"no fix pass has been recorded against it in Doc_09's Document Log, so this file still reflects the Round 5 pass."* L8's remedy was applied to the sentence L8 quoted and not to the clause L8 named first. *Fix:* key the Status line to `FIXED`, not `LATEST`.

**LOW-6 — `lpcstory006` makes a new positive claim about the contents of a text it says nobody here has opened.** l. 61: *"**The *Acta* covers both proceedings, so the pointer holds.**"* The Source field two sections above says the *Acta* *"**has not been read in this build**"*, and the same paragraph says *"Whether the *Acta*'s frame is a bystander's is a question about a text nobody here has opened."* **I opened it.** `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` from l. 41413 carries the 257 hearing before **Paternus** (*"exsul ad urbem Curubitanam proficisci"*) and the 258 trial before **Galerius Maximus** — so the claim is **true**. The defect is warrant, not accuracy: the fix for M7 replaced one uncited characterisation of an unread source with another. *Fix:* cite it, or write *"the transmitted *Acta* is generally printed as covering both proceedings; this build has not opened it."*

**LOW-7 — M9 was closed by hand and the guard the review asked for was not added.** Round 5's M9 fix said *"add a fourteenth halting site: a notice inside Story Text is FATAL."* `GUARD_LABELS` has sixteen entries and none of them is that. The seven chunks are clean today; nothing stops the next pass from writing a notice back into a Story Text, in a script whose own doctrine is *"FAIL LOUDLY"* and which now halts on fifteen lesser conditions. *Fix:* four lines, and it is the one guard that protects the field Doc_10 consumes.

**LOW-8 — `classify()` returns `'live'` for text that is pure mention when one notice quotes another.** Constructed:
```
Live intro. **[CORRECTED, 2026-09-15 — Round 6:** the earlier note read *"**[ADDED, 2026-09-15 — Round 1's L8.**]**"* and asserted that the library largely survived.**]** Live tail.
```
`notice_spans` returns one span ending at the **inner** `]**`, so `classify(t, "the library largely survived")` returns **`'live'`** although the phrase sits inside the outer notice's narration. The error direction is the safe one — a reviewer is sent to look at something already fixed — and the generator halts on this shape inside a chunk. Recorded because the module's docstring presents `classify` as the function *"to call in a closure audit"* and does not name this case.

**LOW-9 — the L5 fix broke the sentence it fixed.** `lpcstory001` l. 37: *"In *Ep.* LXVII **Cyprian and his thirty-six co-signatories argue** that a bishop should be 'chosen in the presence of the people…' **and points to** a case they can check."* The subject was made plural and the second verb was left singular. The diff against `a6a6be73` shows exactly this edit.

**LOW-10 — two derived figures in the Decision Log's Round 5 entry do not check.** *"Surveyed across all **53 notices** in this world build"* — I count **71** notice spans across Doc_09, the index and the seven chunks (the entry's other figure, 11 Form B stamps split 5/6, is **exactly right**, which is what makes 53 look like a stale literal). *"`scripts/test_notice_strip.py` is new — **21 checks**"* — the suite emits **19**. Both are the *"a number typed here is a number that goes stale"* defect the generator's own header warns about, in the entry written to demonstrate honesty.

**LOW-11 — `lpcstory003` l. 61 states a prediction as a finding.** *"…are all unrecoverable, and **no source in this corpus will ever supply them**."* The present tense is verifiable and true; the future tense is not a claim this build can make about a corpus that gained row 203 and row 194 within the last fortnight. *Fix:* *"no source in this corpus supplies them."*

**LOW-12 — `lpcstory007` l. 39's "only place in this world's record" is refuted on the natural reading.** *"**This is the only place in this world's record where a man who spent his life adjudicating other people's penitence is seen performing his own.**"* Augustine's *Confessions* — Native, row 9, vendored, written after his ordination, and Book X in particular — is a bishop's book-length examination of his own continuing sin. The claim survives only on the reading where *"is seen"* strictly requires an external observer. Given that the sentence sits in a chunk whose neighbouring absolute is HIGH-1, it should be narrowed. *Fix:* *"This is the only place in this world's record where a man who spent his life adjudicating other people's penitence is **watched** performing his own."*

---

## COSMETIC

**COSMETIC-1** — Doc_09 §2's **Tier 3** confidence line still stops before CF's continuation *"The formation ideal communicated is credible evidence; the specific events claimed are not"*, with no ellipsis, after the identical remedy was applied to Tier 1 (Round 2) and Tier 2 (Round 5's L2) in the same bulleted list. The fix landed on the two bullets a finding quoted and not on the third.

**COSMETIC-2** — the "Transcription corrections" blocks in `002`, `003`, `004` and `007` sit **after** a horizontal rule with no heading of their own, so they render as an untitled section between Tier Justification and Usage Guidance. The Decision Log describes them as *"moved… into Tier Justification."* Give the block a `### ` heading or move it above the rule.

**COSMETIC-3** — the L8 one-liner is still repeated verbatim in six chunks. C3 asked for *one* statement of a rollout decision, in Doc_09. Doc_09 §7 now has it; the six pointers are new duplication of the thing that was de-duplicated.

**COSMETIC-4** — four chunks silently capitalise the first letter inside a quotation (`"Was found half dead…"` for the source's `…—was found half dead…`; `"There broke out a dreadful plague,"`; `"Persons who favoured him…"`; `"Having with his own hands…"`; `"He had all that time free for prayer."`). Conventional, and no meaning is changed. Noted only because this repository corrects quotations at finer granularity than this elsewhere, and a reader running a literal search will miss them.

---

# Is the deliverable adequate to proceed to Doc_10?

**Yes, after one two-sentence fix. This is the closest this document has been in six rounds.**

**What is ready, verified independently for a sixth time, and this time at more sites.** Seven stories, seven real texts. **Every quotation in all seven chunks and in Doc_09 resolves to body text of the work the chunk names** — zero inside a `<note>`, and the only hit inside an ANF *Argument* is the one `lpcstory004` quotes in order to exclude it, which means the build's own evidentiary discipline at that chunk survives a check built to break it. Every *Epistle* number is right against the printed headings. Every Pontius section is right. Every Possidius quotation is in the chapter the chunk claims, in the span the Source field declares. **No invented participant, event or outcome anywhere in any Story Text**, and the notice move that rewrote four chunks lost **not one word** of Story-Text prose. The generator regenerates byte-identical, all sixteen halting sites fire, and the guard enumeration is derived rather than typed.

**What is not ready is one sentence in one field, and it is the same field class as the last five rounds.** `lpcstory007`'s Tier Justification and Absent Story Note tell a Representative that Augustine's death has one witness. It has two, and the second is in this world's own Registry as a grade-A Native row, cited by Doc_02 and Doc_08. Doc_10 will inherit those fields verbatim. Under Article 20 the Representative would be stating an absence that is not there, about the single most consequential event in this world's second phase.

**MEDIUM-1 should go with it** — it is one clause, it is in §7, and the correct version is available in the same Doc_02 sentence the document already cites.

**Nothing in the tooling blocks Doc_10.** MEDIUM-4 and MEDIUM-5 should be fixed **before the next fix pass runs**, for the reason Round 5 gave about its own HIGH-2: the next pass will use these to decide what is closed.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** No identity, title or voice decision is made here. Noted separately and not as an escalation: two deployable fields assert absences their sources refute (HIGH-1, LOW-12), and one section of Doc_09 does (MEDIUM-1). All are within this document's own gift to fix.

- **Portfolio-level or cross-world — two inherited, one of them with a new and instructive instance.**
 1. *The corpus-wide editorial-apparatus item.* Re-verified independently for the sixth time and still the ledger's first **positive** instance. I built the note mask before stripping tags and a separate *Argument* index from the raw `<p>` elements, and ran both over every quotation in nine files: **zero in notes, one in an *Argument*, and that one is quoted in order to be excluded.** Carry forward unchanged. **The brief's claim of "eight instances" of editorial apparatus read as the world's voice does not describe this deliverable** — see brief error 3.
 2. *The index-generator-as-build-artifact item (Doc_08 R5; Doc_09 R1-M4c, R2-M7, R3-M4, R4-M4, R5-M4/M5).* **Sixth instance, and it is the most useful one yet, because this time the fix made the class worse.** Round 5 routed it with the remedy attached — *"the remedy is a declared field, not a better regex"* — and the pass wrote a better regex whose new vocabulary (`available`, `pending`, `not yet`) collides with ordinary English far more often than the old one did. **Route with that attached: when a portfolio item names a remedy and a pass implements the thing the remedy was meant to replace, the item should come back with the implementation attached as evidence.** The two-line structural fix — boundary-check the excluded rows too — is available and closes the class without any vocabulary.

- **Governance or methodology — one open, correctly raised, and I checked it rather than accepting it.** Doc_09 §8 item 7 escalates **which half of CF's Tier 3 definition governs when the genus clause and the hagiographic-convention clause conflict**. I read CF V7.4's Tier 3 paragraph whole from my own .docx extraction. The genus clause is exactly as quoted — *"Material attributed to specific figures or moments but resting on collected tradition rather than direct documentation"* — and the hagiographic sentence is explicitly *"a specific type **within** this tier."* **Pontius is direct documentation by a named eyewitness deacon, and CF genuinely does not say which clause wins.** The escalation is well-formed, correctly separated from the *"a source is not a tier"* question withdrawn at Round 4 (which I re-checked and agree was correctly withdrawn), and stated at full strength in the chunk. **I would sustain it.** I repeat Round 5's advice about the order of operations: the *Acta* is 216 lines of Latin at `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` l. 41413, `INTAKE.md` licenses it, I read enough of it this round to confirm it covers both proceedings and carries the clearing, the twenty-five *aurei*, the two Juliani and *"propter gentilium curiositatem"* — and reading it would very likely move `lpcstory006` to Tier 1 and moot the question.

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. §6 item 4 and §8 item 4 state it accurately.

- **A methodology observation, and this time it is a credit rather than a complaint.** Five rounds reported the same mechanism: *findings argued at length get fixed; one-line findings at named sites do not.* **This pass broke the pattern** — 33 of 38 closed, including four LOWs that had survived four rounds. The mechanism that produced this round's HIGH is a different one and worth naming for the next pass: **the pass verified the sentences it changed and did not verify the sentences it left.** HIGH-1, MEDIUM-1 and LOW-12 are all sentences no round has ever tested, sitting in fields that three rounds have rewritten around them. The convention that would catch them is: *when a fix pass touches a field, it re-tests every absolute negative in that field, not only the one the finding named.*

---

# Check confirmation — including three defective checks of my own

**Three of my own checks failed before reporting. I record them first, because a check that returns something adjacent to a claim and is then trusted is this build's documented meta-defect and I am not exempt from it.**

**Defective check 1 — an *Argument* mask that swallowed a whole letter.** My first ANF *Argument* detector ran from `Argument.-` to the next `" 1. "`. *Epistle* XXXIV has no numbered sections, so the span ran to a 4,000-character default and **flagged all ten of `lpcstory003`'s quotations as 19th-century editorial matter** — which would have been a fabricated HIGH against the chunk with the cleanest provenance in the set. Caught by reading *Ep.* XXXIV whole (2,040 characters; the Argument is one sentence). Rebuilt from the raw `<p>Argument…</p>` elements, 95 of them, with two-way controls.

**Defective check 2 — a global substring test for *Argument* membership.** The rebuilt mask was still queried as *"is this string anywhere in the Argument corpus?"*, so *"contrary to the law of the Gospel"* — which `lpcstory005` quotes from *Ep.* XIV's body — was flagged as editorial because the identical phrase happens to appear in *De lapsis*'s Argument. Caught by printing the hit's own context, which is Cyprian in the first person: *"…thousands of certificates were daily given, contrary to the law of the Gospel, **I wrote letters in which I recalled by my advice**…"*. Had I trusted it, it would have been a fabricated misattribution finding.

**Defective check 3 — note removal that fused words.** My note-stripped stream deleted `<note>` characters without leaving a separator, so the ANF's inline gloss in *Ep.* XXXIV turned *"remained unwillingly Otherwise, 'unconquered.' from among"* into *"unwillinglyfrom"*, producing a false MISS on a real quotation. Fixed by substituting one space per note span and re-confirming on three controls.

## Confirmations, one for every finding that rests on a negative or a forced result

**C1 — the Cyprian harness, both directions.** Body text found and marked not-in-note (*"the judgment of God and the favour of the people"*, Pontius, p. 269); note text found in the with-notes stream and **absent** from the note-stripped stream (four ASCII probes drawn from four different works); a nonsense string returns MISS. All three controls pass.

**C2 — the *Argument* index, both directions.** `lpcstory004`'s exclusion quotation (*"Cyprian Begins by Deploring the Captivity…"*) resolves **IN** the Argument corpus; the sum the chunk actually cites (*"We have then sent you a sum of one hundred thousand sesterces"*) resolves **OUT** of it, in the letter body. That is the build's own evidentiary claim at that chunk, tested by an instrument built to break it.

**C3 — the Possidius harness.** Exact hits with chapter and line for six quotations; MISS on a nonsense string; the three near-misses resolved by printing 600 characters of source around each and confirming the only differences are an initial capital and a substituted period. The hyphenation and page-break traps that produced false negatives in four consecutive rounds are handled, and a second, punctuation-free word stream agrees.

**C4 — for HIGH-1.** Four independent confirmations. (i) `Source_Registry.md` row 203 read in full: **Native**, grade **A**, **Vendored**, and its Notes cell names Augustine's death as the thing it attests. (ii) The file opened and the a. 430 entry read in Latin. (iii) `Doc_08_Forces_Document.md` l. 230 and `Doc_02_Source_Ecology.md` §5 both say a chronicler independently records the death, naming row 203. (iv) Doc_09 and all seven chunks grepped for *"Prosper"* and *"row 203"*: **zero occurrences**, so the omission is total rather than a citation I missed.

**C5 — for MEDIUM-1.** Registry row 27 read in full (**Native**, vendored, double-placed with `donatism`); both vendored Optatus files' own headers read, giving *"Optatus of Milevis (Latin original, **c. 366-393 CE**)"*; Doc_02 §7 read whole, containing both the true clause (*"the interval is in fact richly attested"*) and the false one Doc_09 relays.

**C6 — for MEDIUM-3.** Positive control across time: the grep `Doc_09 §8 item [0-9]` returns **nothing** at `a6a6be73` and **three hits** at `HEAD`, two of them in files this pass edited. The claim was true when Round 5 made it and the pass falsified it.

**C7 — for MEDIUM-4.** Four forced runs from four fresh copies of the world tree, each with the matched control in the same shape: the plain positive form halts at the boundary guard with the Excluded-row message; the same sentence with *"available"*, with *"pending"*, or with an incidental *"does not"* emits rc 0 and prints the row as *"named, not drawn on."*

**C8 — for MEDIUM-5.** Three constructed inputs run through the committed `live()`, each deleting a live sentence; plus a scan of all nine deliverables showing 71 openers, 71 matched spans, 0 uncovered and 0 spans crossing a blank line — which is what makes it latent rather than live, and is the reason this is MEDIUM and not HIGH.

**C9 — for LOW-1 and LOW-2.** Markdown rendered through a CommonMark implementation: the new boilerplate emits `<strong>…</strong>]**`, the pre-pass form emits clean nested bold. Rule-before-heading checked mechanically with `a6a6be73` as the positive control, returning an empty defect list for all seven files before the pass.

**C10 — for the generator credits.** Sixteen halting sites counted by AST walk, sixteen forced from sixteen fresh copies, each returning rc 1 with its own distinct message; `GUARD_LABELS` length 16; regeneration into a clean copy **byte-identical** to both the committed and the working-tree index.

**C11 — negatives that held, tested and passed.** Recorded because they are the ones that could have been findings and are not. *"Where she searched, the letter does not say"* — *Ep.* XXXIV read whole, no locative. *"Cyprian never writes again about the outcome"* of the ransom — every occurrence of *captivity*, *captive brethren*, *redemption*, *barbarians* across 497 titled divisions; *Ep.* LIX is the only Cyprianic locus. *"No Christian outside Pontius describes the operation"* — *On the Mortality* and *An Address to Demetrianus* both searched for relief language; the search finds *plague* and *pestilence* in both, so it is live, and finds no relief operation. *"Not one of them left an account of their own"* of Cyprian's execution crowd — holds, including against the *Acta*, whose *"turba fratrum"* is reported, not authored. *"No English translation of it exists anywhere in this corpus"* — `Galerius Maximus`, `Thascius Cyprianus`, `Paternus the proconsul`, `I am a Christian and a bishop` across all 117 vendored texts; every hit is Latin, French or German scholarship. *"They wrote; he read it; it does not survive"* — *Ep.* XXVI read whole, and the ANF Argument itself says *"**But the Letter of the Lapsed to Which He Replies is Wanting.**"*

**What I tested hardest.** In order: the absolute negatives, one by one, at source — which is where HIGH-1 and MEDIUM-1 were, and where six others held. Then the notice move, word by word against the pre-pass commit — which is where LOW-1 and LOW-2 were, and where the prose was clean. Then the generator, by sixteen forced halts and seven bypass probes — which is where MEDIUM-4 was. Then `notice_strip.py` in both directions — which is where MEDIUM-5 was. Then every quotation, twice, through two streams — which found nothing, and that is the finding.

**What would change the verdict.** Fixing **HIGH-1** (two sentences in `lpcstory007`) and **MEDIUM-1** (one clause in Doc_09 §7 item 1 and one in §1). With those, I would return **MINOR REVISION** on this same reading. **On the story content alone, considered apart from the two absences and the tooling, I would clear this document** — six rounds have now verified every quotation independently and found no composite and no invention, and that is what Doc_10 consumes as content.

**If a fix pass disagrees with HIGH-1, the thing to produce is not an argument but the text:** a reading of `Source_Registry.md` row 203, of `prosper_chronica-minora-1-lat_mommsen1892.txt` at the year 430, and of `Doc_08` l. 230, on which *"no second account of Augustine's death exists in this corpus"* is true.

---

# Errors in this round's brief

Recorded as directed. Two are checkable facts and one is a characterisation that does not describe the deliverable.

**Brief error 1 — `HEAD~2` is the Round 5 fix-pass commit itself.** The brief says the notice mover deleted front-matter from four chunks and directs me to *"verify all seven chunks are intact and correct against `git show HEAD~2:<path>`."* `HEAD~2` is `44dd6151`, *"Doc_09 Round 5 fix pass"* — the commit that contains the repair. Diffing against it is a tautology; it returns empty for every deliverable. The pre-pass state is **`HEAD~3` = `a6a6be73`**, and that is what I used. **The substance of the brief's claim checks out**: all seven chunks have exactly two fence markers, seven front-matter fields each, `## Story Text` at line 13, and no field lost against `a6a6be73`.

**Brief error 2 — the CF line numbers are off by one against my own extraction, and are not a stable citation.** The brief says §2's Tier 2 band quotes **CF l. 257** and §3.1 quotes **CF l. 267**. In my own paragraph-level extraction of `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` (722 paragraphs), the Tier 2 confidence line is **l. 258** and the Tier 4 placement rule is **l. 268**; Tier 1's band is 254, Tier 3's genus 261, Step 9's catalog requirement 700. Round 5's numbers (253/257/260/261/267/699) are consistently one lower. **Line numbers in a .docx-to-text conversion depend on how empty paragraphs and table cells are handled and should not be carried between rounds as if they were citations.** Doc_09 never cites CF by line number, which is correct. **The substance holds at every site**: both quotations are exact against CF's own text, including the restored continuations.

**Brief error 3 — "eight instances" of editorial apparatus read as the world's voice does not describe this deliverable.** The brief calls it *"a documented failure here (eight instances)."* Whatever that count refers to upstream, in the six deliverables under review it is **zero**: of every quotation in Doc_09 and all seven chunks, none resolves inside a `<note>`, and exactly one resolves inside an ANF *Argument* — `lpcstory004`'s, which is quoted in order to exclude it and is disclosed as such in the chunk, in Doc_09 §4 and in the Disposition. I built the check to find eight and it found none. Stated because a brief that names a live hazard where the build has a clean record directs attention away from the hazards it does have, which this round were two absolute negatives nobody had tested.

---

# VERDICT: **SUBSTANTIAL REVISION REQUIRED**

**1 HIGH · 6 MEDIUM · 12 LOW · 4 COSMETIC.**

**This is the best fix pass this document has had: 33 of Round 5's 38 findings closed at every site each finding named, four four-round-old LOWs among them, the Story Text cleaned of build apparatus without losing a word, and a rewritten stripper that no longer manufactures false closures.** What keeps the verdict at SUBSTANTIAL is that the pass verified the sentences it changed and not the sentences it left: `lpcstory007` still tells a Representative, twice, that Augustine's death has one witness, while a contemporary chronicle recording it sits in this world's own Registry as a Native grade-A vendored row that Doc_02 and Doc_08 both cite by number. That is the sixth round in a row in which this document's worst finding is a silence asserted about a source the source refutes — and the first in which the refuting source is one the build itself went out and acquired to close exactly that gap.

*Simulated review — informational only, not an Article 31 substitute.*
