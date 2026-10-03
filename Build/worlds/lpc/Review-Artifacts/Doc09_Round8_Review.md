# Doc_09 — Round 8 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`)

*Simulated review — informational only, not an Article 31 substitute.*

---

# VERDICT: **MINOR REVISION**

**0 HIGH · 4 MEDIUM · 5 LOW · 3 COSMETIC.**

**Read this box first, because the deliverables moved while I was reviewing them.** The brief names `c4f7d376` as HEAD. It was, when I started. **Partway through Job 1 the working tree began rewriting itself under me** — `scripts/gen_story_index.py` carried an mtime equal to the second I ran `ls` — and by the time I reached Job 5 a new commit had landed:

```
a416fc6f Extract correction history from the deliverables; delete the stripper
c4f7d376 Doc_09 Round 7 fix pass  <- what this review audits
```

`a416fc6f` **deletes `scripts/notice_strip.py` and `scripts/test_notice_strip.py` outright** and moves every inline `[CORRECTED …]` notice out of the nine deliverables into a new `Review-Artifacts/Doc09_Correction_History.md`. Three of the six deliverables this brief named no longer exist. I did three things about it, and they are the reason this review is trustworthy rather than a casualty of the race:

1. **I pinned everything to a verified clean extraction of `c4f7d376`** in scratch and re-ran every measurement I had already taken. All reported numbers below are from the pin, not from the live tree.
2. **I discarded one finding I had already written** — a crash in `test_notice_strip.py` — after establishing it was an artifact of the concurrent edit and **not** present at `c4f7d376`, where the suite passes 50 checks at exit 0.
3. **I checked which of my findings survive into `a416fc6f`.** Every content finding below does, verbatim. The one tooling finding (LOW-3) is mooted by the deletion.

**The headline is that Job 1 came back clean, and Job 5 came back clean, and neither has happened before in this document's history.**

- **`notice_strip.py` is correct. I could not break it.** I wrote a second implementation sharing no code with it, ran the two against each other on **200,000 fuzzed inputs (zero disagreements, zero exceptions)**, on 20 hand-built adversarial cases covering every shape the brief named, and on all nine deliverables. **`live()` deletes no live prose anywhere.** **`classify()` returns `notice-only` for zero of 479 live-prose sentences** — against a positive control where the pre-pass module returns `notice-only` for **52** of them. Round 7's HIGH-1 and MEDIUM-2 are closed as a class, exactly as the rewrite claims. **The module was right when it was deleted**, and that should be on the record so the deletion is never retrospectively justified by a defect that was not there.
- **The signature defect did not produce a HIGH.** I extracted **111 absolute and exclusivity claims from live prose, 103 of which have never been quoted in any Doc_09 review artifact**, and tested every testable one at source. They hold. That is the first round of eight in which this document's central recurring defect produced nothing.
- **Every quotation resolves.** 140 of 157 quoted strings resolved automatically; I ran the remaining 17 down by hand and **all 17 are accounted for** (the document's own words, scare quotes, self-corrections, and one string the build itself declares occurs zero times — it does). **Zero quotations resolve to editorial apparatus** — eighth consecutive verification, with the note mask laid down before a single tag was stripped.
- **Round 7's two HIGHs are closed at source**, and closed *well*. The Possidius chapter range, every printed heading quoted, and row 192's status are exact. The Prosper OCR is now quoted verbatim and I confirmed each token — `cxcellentissimus`, `Y. kl. Sept.`, `luliani`, `NVandalorum` — **once in the body, zero in the header**, with the corrected form **once in the header, zero in the body**, precisely as the chunk now says.

**What holds the verdict at MINOR is four MEDIUMs, and all four are the same failure the last two rounds named: a number or a neighbour that one of this pass's own edits falsified.** The worst is the Disposition's HIGH ledger, which no longer adds up — **8 + 1 + 1 = 10, under a heading that says eleven** — and which the pass's *own Decision Log entry*, written in the same commit, states **correctly**. The right number was written; it was written in the wrong file. That is verbatim the diagnosis Round 7 delivered about Round 6.

**If MEDIUM-1 through MEDIUM-4 were fixed — four sentences — I would clear this document.**

---

# Method — everything below was derived here

**I inherited nothing.** Not the brief's numbers, not the fix pass's claims, not Rounds 1–7. Two of the brief's own premises turn out to be wrong and are reported at the end.

1. **Commit refs verified before use.** `c4f7d376` = *"Doc_09 Round 7 fix pass"*; `7c9b56b4` = *"Doc_09 Round 6 fix pass"*; `6c16e5f9` = the Round 7 review artifact and **nothing else** (`git diff 7c9b56b4 6c16e5f9` touches one file); `25edc87d` = the original draft. All four correct. Branch `lpc-doc04-round2` correct.
2. **Pinned tree.** `git archive c4f7d376 | tar -x` into scratch, then md5-verified file-by-file against `git show c4f7d376:…`. Every measurement re-run against the pin after the concurrent commit appeared.
3. **A second notice scanner, written from scratch** — an explicit character-walk state machine with a depth stack and its own tag matcher — with no line of code taken from `notice_strip.py`. Used as the differential oracle throughout.
4. **ANF05 harness, character-level, built for this round.** Hand-written tag scanner over `anf05_hippolytus-cyprian-caius-novatian.xml` carrying, for each of **3,475,736** output characters, its innermost `<div1–4>` `title=` (**attribution by title, never by position**), its `<pb n="">` page, and **whether it lies inside a `<note>` span, marked before any tag was stripped** (**381,835** note characters). Two streams: with notes, and note-stripped with one space substituted per note span. **I found and fixed two defects in my own harness before trusting it** (see Check confirmation).
5. **Possidius harness, built for this round, then rebuilt** after its first version silently dropped an English page at the bilingual seam. Final version searches the whole de-hyphenated body with a chapter map read off the printed `CHAPTER N` headings — **all 31 chapters I–XXXI, no gaps**.
6. **CF V7.4 extracted from the .docx myself** (unzip + `<w:t>` walk, 722 paragraphs). **No line numbers are cited anywhere below.**
7. **The generator** re-run from the pin (index **byte-identical**), 17 halting sites counted off my own AST walk, and four guards forced from fresh copies of the world tree.

---

# Job 1 — attacking `notice_strip.py`

The brief instructed me to assume the module is wrong again and find how. **It is not wrong.** Here is what I did to establish that, because a negative result of this size needs its working shown.

### The differential oracle

I implemented the stated contract independently: openers are `0–2 asterisks + [ + a tag word + word boundary`; a nested opener increments depth; `]**` decrements; depth zero ends the span; spans never cross `\n`; an opener that never reaches depth zero is reported and not acted on. Mine walks characters with a stack; theirs alternates `re.search` and `str.find`. Different shapes, same contract.

| test | result |
|---|---|
| **nine deliverables** — spans, unterminated offsets, and full `live()` output | **identical, file for file. 83 spans, 0 unterminated, `live()` byte-equal in all nine** |
| **20 hand-built adversarial cases** | **identical in all 20** |
| **200,000 fuzzed strings** built from notice atoms, stray `]**`, backticks, CRLF, blank lines, bracket types, unbalanced `**` | **0 disagreements, 0 exceptions, 0 `classify()` crashes** |

### The cases the brief asked for, and what each does

| construction | outcome | safe? |
|---|---|---|
| two sibling notices with live prose between (Round 7's HIGH-1 shape) | **two spans**; the middle sentence survives `live()` and classifies **`live`** | ✔ |
| **three** notices on one line | **three separate spans**; both live segments survive | ✔ |
| genuinely nested notice (Round 6's LOW-8 shape) | **one span**, correctly spanning the container | ✔ |
| opener inside a code span / backticks | reported by `unterminated()`, **not acted on**; the live sentence survives | ✔ |
| backticked opener **plus** a real notice later on the same line | real notice spanned, backticked one reported, live prose between them kept | ✔ |
| `]**` inside a quoted string in the body | span **ends early** — under-strip, the documented safe direction; no live prose lost | ✔ |
| partial tag (`[CORRECTIONS`) | no match, no span, no deletion | ✔ |
| unbalanced `**` before an opener (`**bold**[CORRECTED`) | span starts two characters early; cosmetic only | ✔ |
| body containing `(`, `{`, `[` of other bracket types | ignored; span correct | ✔ |
| **CRLF line endings** | spans and offsets correct; `\r` is carried inside the line so `off += len(line)+1` stays exact | ✔ |
| a line that is only a notice | whole line replaced by one space | ✔ |
| notice split over a newline | **no span; opener reported** — the line-scope contract holding | ✔ |
| quoted opener with no inner closer inside a real notice | outer reported unterminated, inner spanned; **live tail survives** | ✔ |
| two openers, one closer, live prose between | outer reported, **`LIVE-SWALLOWED-A` survives `live()`** | ✔ |
| table row / list item context | spans confined to the row; the next row untouched | ✔ |
| lower-case tag | no match — which is what the generator's separate shape guard is for | ✔ |

### On the live deliverables

I split every deliverable into live-prose sentences (≥45 chars, outside every span my own scanner finds) and ran the committed `classify()` over each.

```
live = 479      ambiguous = 22      NOTICE-ONLY = 0
```

**Positive control, required because this is a zero.** The same sweep, run with the pre-pass module (`7c9b56b4`) against the pre-pass files, returns **52 `notice-only` verdicts on live prose**, including *"No motive is attributed to either man beyond what they write"* and *"The provisional Step-2 inventory was never made."* **The check can see the defect. The defect is gone.**

The 22 `ambiguous` verdicts are all Form-B trailing prose, which the docstring says is undecidable and which `mentions_only()` deliberately returns `False` for. That is the contract, not a defect. I also verified the Form A/B discriminator by hand on all 83 spans: **69 Form A, 14 Form B, and all 14 are genuine bare provenance stamps.** The docstring's claim that trailing prose exists in **11** cases is exactly right — I count **11 Form-B stamps with trailing prose and 3 without**.

### The two strippers agree

The generator keeps its own regex stripper. Round 7's LOW-18 test compares them on §7 and §2 only. **I compared them on all nine deliverables, whole:**

```
Doc_09  5939 vs 5939      index  1734 vs 1734      001  969 vs 969
002 1813 vs 1813   003 1039 vs 1039   004 1026 vs 1026
005 1598 vs 1598   006 1417 vs 1417   007 1782 vs 1782
```

**Word-for-word identical in all nine.** No drift.

**Verdict on Job 1: the module is sound, and the rewrite was the right call.** The only thing I have against it is a stale number in the comment that justifies its design — LOW-3 below.

---

# Job 2 — auditing the Round 7 fix pass's claims

The Document Log claims *"Both HIGH closed; all 5 MEDIUM, all 10 LOW and all 4 COSMETIC addressed."* Checked at **every** site each finding names. No `[CORRECTED …]` notice accepted as evidence.

| R7 finding | Verified how |
|---|---|
| **HIGH-1** — `classify()` swallows live prose between sibling notices | **Closed as a class, and forced.** See Job 1. Regex replaced by a depth scanner; 0 of 479 live sentences classify `notice-only` against a 52-hit positive control |
| **HIGH-2** — §7 item 5 said the ordinary pastorate is unrecorded | **Closed, and the correction is exact.** Chapters XIX–XXVII verified present; **every one of the seven headings quoted is verbatim in the printed text** at the right chapter; row 192 read in full (**Native**, **Vendored**, grade A); Doc_05 open item 10 quoted exactly. **The heading list stops at XXV without an ellipsis — LOW-2** |
| M1 — §7 item 1's ownership claim refuted by row 27 | **Closed.** Row 27 read: Boundary Status **Native**, corpus map `role: tradition`. Doc_02 §1 read whole — *"native to one, etic evidence for the other"* is **verbatim**, and row 27's *"not drawn on for a specific claim in this world's own Doc_01 or Doc_02"* is **verbatim** |
| **M2** — notice body crossing a paragraph break by three routes | **Closed structurally.** Line scoping removes the paragraph bound entirely. All three of Round 7's constructions now keep their live sentence *and* report the opener; forced |
| **M3** — the Prosper quotation not at source | **Closed, precisely.** Counted over header and body separately: the chunk's OCR string **1 in body, 0 in header**; the corrected form **0 in body, 1 in header** at offset **3485**, which the Decision Log names correctly. Each of the four tokens confirmed body-only |
| M4 — §4 said *"Four"* candidates | **Closed.** §4 now says *"Five"*; §6 enumerates five |
| M5 — Disposition listed five rounds under *"Six rounds"* | **Closed.** Seven rounds enumerated under *"Seven rounds have been run,"* and **all seven per-round counts match each review artifact's own verdict line**, checked mechanically. **The HIGH tally in the same paragraph is now broken a different way — MEDIUM-1** |
| L1 — *"has not been reviewed at all"* | **Closed**, and **better than Round 7 asked.** Round 7 wanted *both* clauses rewritten, on the ground that *"eight are complete, not five."* The pass rewrote only the second. **It was right to:** the first clause says *complete, reviewed **and awaiting a project-lead disposition***, and by this document's own Input-documents paragraph that is exactly Doc_04–Doc_08 — **five**. Round 7 misread the conjunction |
| L2 — §2's transcription disclosure undercounted | **Closed, and the new count is exactly right.** Found mechanically with a **case-sensitive** matcher over note-stripped ANF and de-hyphenated Possidius: **6 sites across 5 chunks** — `002` l.15, `003` l.21, `005` l.21, `006` l.17, `006` l.21, `007` l.23 |
| L3 — Decision Log's stale notice count | **Closed.** The number is gone, replaced by a statement that both prior figures were stale literals. No new number to go stale |
| L4 — *"check count is derived rather than typed"* | **Closed.** The clause is gone |
| L5 — §6 item 3 lifting row 9's words unattributed | **Closed.** Now *"in `Source_Registry.md` row 9's own words"*; the quoted phrase is verbatim in row 9's Notes |
| L6 — test suite blind spots | **Closed.** Nine new checks (J1–J5) plus a nine-file invariant (J6). Suite passes 50 checks, exit 0, **at the pin** |
| **L7** — `lpcstory004`'s undisclosed ANF dollar note | **Closed, and I verified the note is apparatus:** *"at $3,757"*, *"For the Augustan age it would be"*, *"The text (sestertia) dubious"* each return **1 hit with notes, 0 note-stripped**. The chunk now names it and still excludes it. **A lowercase sentence opener came with the edit — COSMETIC-1** |
| L8 — boundary-guard message asserting sourcing | **Closed, and forced.** New message: *"row(s) ['204'] named in a story's Source field are not Native … Since Round 6 this checks disclaimed rows too, so the breach is naming a non-Native row at all, whichever polarity the chunk claims"* |
| L9 — §8 item 2's *"Three"* cross-references | **Not closed.** *"Three"* became *"Four"*; there are **at least seven at six sites** — LOW-1 |
| L10 — `lpcstory007`'s Latin-only witness | **Closed.** Now *"vendored in Latin only, so row 203's own second-witness caveat under `cic/texts/INTAKE.md` applies"* |
| C1 — stray leading space | **Closed.** `grep -c "^ [A-Z]"` returns **0** in all seven chunks |
| C2 — *"two words after the sum"* | Adopted from Round 7's own wording. The note is **adjacent** to the sum — COSMETIC-2 |
| C3 — guard message vs. where the blocks live | **Closed.** Message now says *"the chunk's '### Transcription corrections' block"*, and that heading exists in all four chunks that carry one |
| C4 — §8 item 8's *"one chapter of Possidius"* | **Closed.** Now *"one story from a four-chapter span of Possidius"*, agreeing with §3 and the chunk |
| COSMETIC-2 (R7) — number-word map stopping at six | **Closed**, and reproduced: the index prints *"**Seven** round(s)"*. **The comment describing the fix is false — LOW-4** |

**Honest summary: 19 of Round 7's 21 findings are closed at every site the finding named, and two of the closures are better than Round 7 asked for.** L9 is not closed. HIGH-2's closure carries a new small defect (LOW-2). **This is the third consecutive pass that did most of what it said, and the first whose tooling work I could not break.**

**The failure mode is unchanged and is now the only thing wrong with this document.** Every MEDIUM below is a number or a neighbouring sentence that one of this pass's own edits falsified. Round 6 named it; Round 7 named it again and prescribed the convention (*"when an edit adds or removes an enumerated item, grep the document for every number that could be counting it"*). **The convention was not adopted.**

---

# Findings

## HIGH

**None.**

I looked hard and in the places the brief pointed me. The tool is sound; the quotations are sound; the absolutes are sound. I am not going to manufacture one. What follows is real but none of it reaches HIGH.

---

## MEDIUM

### MEDIUM-1 — the Disposition's HIGH ledger does not add up: eight plus one plus one, under a heading that says eleven — and the same paragraph names the missing one two sentences later

**Site.** `Doc_09_Story_Inventory.md`, Disposition, second paragraph. Live prose.

> *"**Eleven HIGH findings have been raised across seven rounds. Eight are one defect — a silence asserted about a source that the source refutes. One was a transcription failure, and one was a tool that manufactures the same false silence mechanically.**"*

**8 + 1 + 1 = 10.** One of the eleven has no home in the partition.

**The missing one is named in the same paragraph.** The enumeration that follows lists *both* stripper findings — *"Round 5: … and `notice_strip.py`, written to prevent false closures, deleting 48% of §7's live prose"* and *"Round 7: … and the stripper reintroducing its own over-consumption, this time between sibling notices."* And three sentences on, the paragraph states the correct number outright:

> *"**Two of the eleven were introduced by a fix pass answering the previous round** — both in `notice_strip.py`, the tool written to prevent false closures."*

**So the paragraph says "one was a tool" and "two … both in `notice_strip.py`" within three sentences of each other.**

**I enumerated all eleven from the review artifacts themselves**, by heading, not from the document:

| # | Round | Site | class |
|---|---|---|---|
| 1 | R1 H1 | `lpcstory002` Story Text / Tier Justification / Usage Guidance | signature |
| 2 | R1 H2 | `lpcstory005` — two altered quotations | **transcription** |
| 3 | R3 H1 | `lpcstory003` `Do-Not-Retrieve-When` | signature |
| 4–6 | R4 H1–H3 | three Absent Story Notes | signature |
| 7 | R5 H1 | `lpcstory005` Usage Guidance | signature |
| 8 | R5 H2 | `notice_strip.py` `live()` | **tool** |
| 9 | R6 H1 | `lpcstory007` Tier Justification + Absent Story Note | signature |
| 10 | R7 H1 | `notice_strip.py` `classify()` | **tool** |
| 11 | R7 H2 | `Doc_09` §7 item 5 | signature |

**8 signature, 1 transcription, 2 tool.** Eleven.

**Why this is MEDIUM and not LOW.** Three reasons.

1. **It is the exact operation the pass was correcting.** The pre-pass sentence read *"Eight HIGH findings … across five rounds. Six are one defect …"* — and **6 + 1 + 1 = 8 was arithmetically correct.** The pass updated *"Eight"*→*"Eleven"* and *"Six"*→*"Eight"* and left the *"one … and one"* tail alone, in the same edit that added the Round 7 sentence naming the second tool finding. The edit broke a sentence that was previously sound.
2. **The correct figure was written the same day, in the same commit, in a different file.** `lpc_Decision_Log.md`'s Round 7 entry: *"**The HIGH ledger, now stated exactly.** Eleven HIGH findings across seven rounds. **Eight are the signature defect.** One was transcription, **two were the stripper.**"* That is right. Round 7's own Job 5 ended on precisely this observation about Round 6 — *"The right number was written; it was written in the wrong file."*
3. **It is the one place the record is summarised**, and the `[CORRECTED — Round 5's M3]` notice attached to this very paragraph says it *"understated the record by three quarters **at the one place the record is summarised**."*

**Fix.** *"…One was a transcription failure, and **two were the tool** written to prevent false closures, which manufactured the same false silence mechanically."* Or delete the *"Two of the eleven…"* sentence as redundant once the partition is right.

---

### MEDIUM-2 — "Five of the eight were in fields that instruct the Representative." Seven of the eight were

**Site.** `Doc_09_Story_Inventory.md`, Disposition, same paragraph, immediately after MEDIUM-1's site. Live prose.

> *"**Five of the eight were in fields that instruct the Representative.**"*

**The referent of "the eight" changed under this sentence and the number did not move with it.** Before the pass, *"the eight"* meant **all eight HIGH findings across five rounds**. After the pass, the only *"eight"* in the paragraph is **the eight signature-defect findings**. The sentence was not touched.

**Taking it at its post-pass referent and checking every one at its site**, from the review artifacts' own headings:

| signature HIGH | field |
|---|---|
| R1 H1 | Story Text, Tier Justification, Usage Guidance — *"and writes it into the Representative's mouth"* ✔ |
| R3 H1 | `Do-Not-Retrieve-When` ✔ |
| R4 H1 | Absent Story Note ✔ |
| R4 H2 | Absent Story Note ✔ |
| R4 H3 | Absent Story Note + Doc_09 §7 ✔ |
| R5 H1 | Usage Guidance ✔ |
| R6 H1 | Tier Justification + Absent Story Note ✔ |
| R7 H2 | Doc_09 §7 item 5 — the absence register, not a chunk field ✘ |

**Seven of the eight**, on the strictest reading that excludes §7 item 5. Round 7's MEDIUM-5 already told this document the figure was too low and asked for six; the pass rewrote the two sentences above it and left this one.

**Why it matters.** This is the sentence that tells a reader how dangerous the defect class is. Understating it by two — in the paragraph whose own attached notice records that it once understated the record *"by three quarters"* — is the same error the notice commemorates.

**Fix.** *"**Seven of the eight** were in fields that instruct the Representative; the eighth was in §7, which Doc_10 inherits as this document's absence register."*

---

### MEDIUM-3 — two items in the same numbered list each claim to be *the* largest available improvement to this document, and this pass wrote the second one

**Sites.** `Doc_09_Story_Inventory.md` §8 item 1 and §8 item 9; reinforced at §6 item 2 and §7 item 5. **All four are live prose** — I confirmed each with `classify()`, which returns `live` for all four and `notice-only` only for the one occurrence that genuinely sits inside a notice.

> **§8 item 1:** *"**The *Acta Proconsularia* is unread** (§6 item 2). Reading it would move `lpcstory006` from Tier 3 to Tier 1, which is **the single largest available improvement to this document**."*

> **§8 item 9:** *"**Possidius, *Vita Augustini* XIX–XXVII … is vendored, Native (row 192), and unread** … **Reading it is the largest available improvement to this document**."*

Eight lines apart, in the same numbered list, about two different sources. They cannot both be true.

The same contradiction runs in §6/§7:

> **§6 item 2** (*Acta*): *"**This is the highest-value unexploited source for this document.**"*
> **§7 item 5** (Possidius): *"**This is the strongest single improvement available to this document**."*

**This pass created it.** `git show 7c9b56b4` confirms §8 item 1's and §6 item 2's superlatives **predate** the pass and §7 item 5's and §8 item 9's are **new this pass** — written in the fix for Round 7's HIGH-2, without checking the standing claim four items above.

**Why it matters, and it is not merely stylistic.** §8 is the document's instruction to whoever runs the next pass. It now issues two mutually exclusive instructions about what to read first. §6 item 2 additionally calls the *Acta* *"the strongest single candidate for the next pass"* while §6 item 3 calls the *Confessions* *"the strongest Phase Two candidate"* — that one is properly qualified and is fine. The two unqualified superlatives are not.

Round 4's HIGH-1 was graded on the shape *"self-refuting in one sentence."* This is self-refuting across one list.

**Fix.** Rank them once, in one place. Something like: *"§8 item 9 (Possidius XIX–XXVII) is the largest available improvement; §8 item 1 (the* Acta *) is the largest available **tier** improvement, since it alone can move a story from Tier 3 to Tier 1."* Both facts survive and the contradiction does not.

---

### MEDIUM-4 — "Seventh consecutive round of this document's signature defect" is refuted by this document's own round table: Round 2 produced no HIGH at all

**Sites.** `Doc_09_Story_Inventory.md` §7 item 5's correction notice; `Story-Chunks/lpcstory007_the-psalms-on-the-wall.md` (*"Sixth consecutive round"*); `lpc_Decision_Log.md` Round 6 and Round 7 entries. At `a416fc6f` these have moved to `Review-Artifacts/Doc09_Correction_History.md` unchanged.

> §7 item 5: *"**Seventh consecutive round of this document's signature defect** — a silence asserted about a source, which the source refutes."*

**The document's own Disposition, ten lines below, prints the counts:**

> *"Round 1 (2H 8M 12L 5C), **Round 2 (0H 11M 17L 5C)**, Round 3 (1H 10M 12L 5C), Round 4 (3H 9M 16L 5C), Round 5 (2H 10M 20L 6C), Round 6 (1H 6M 12L 4C), Round 7 (2H 5M 10L 4C)."*

**I verified all seven against each review artifact's own verdict line. Round 2 is 0 HIGH**, and the Document Log says so in words: *"**No HIGH; reviewer states it could not manufacture one.**"*

**So the run is not consecutive, and it is not seven rounds.** The Disposition's own enumeration of the defect names Rounds **1, 3, 4 (×3), 5, 6, 7** — **eight instances across six rounds**, with Round 2 skipped. I read Round 2's eleven MEDIUM headings to be sure nothing of this class hides there: its M4 (*"`lpcstory007`'s corrected Source field makes a new, checkable claim that is false"*) is a misplacement claim about which chapter carries the last preaching, not a silence refuted by its own source, and Round 2 graded it MEDIUM.

**Why it matters.** This is the phrase in which the document characterises its own central recurring defect, and it is the phrase a reader of `Doc09_Correction_History.md` will take away. It is wrong by one on the count and wrong on the word *consecutive*, and it is refuted by a table in the same file. The error was introduced at Round 6 (*"Sixth consecutive"*, when the true figure was five rounds) and incremented rather than checked at Round 7.

**Fix.** *"The eighth instance of this document's signature defect, across six of the seven rounds run — Round 2 found none."*

---

## LOW

**LOW-1 — §8 item 2 says "Four cross-references now exist." There are at least seven, at six sites; this is the second consecutive round the sentence has been corrected to a wrong number, and this pass added one of the falsifying references itself.** `Doc_09_Story_Inventory.md` §8 item 2: *"**Four** cross-references now exist, so the placeholder is load-bearing after all."* Enumerated across the whole world build, references to **Doc_09's** §8 by item number: `Doc_09` Document Log (*"one new escalation raised (§8 item 7)"*); `Doc_09` Disposition (*"Doc_09 §8 item 7 carries it"*); `lpcstory006` (*"Doc_09 §8 item 1"*); `lpc_Decision_Log.md` l. 1453 (*"Doc_09 §8 item 7"*); `lpc_Decision_Log.md` l. 1524 — **two**, *"§8 item 2"* and *"§8 item 8"*, in the Round 6 entry; `lpc_Decision_Log.md` l. 1544 (*"§8 item 9"*), **added by this pass**. **I verified against `7c9b56b4` that l. 1524's two were already present when Round 7 counted four** — so the number was wrong when written and the same commit made it worse. *Fix:* say *"several"*, or derive it.

**LOW-2 — §7 item 5 presents an incomplete list as "the printed headings" of a nine-chapter range, with no ellipsis, in the document that discloses a convention against exactly this.** *"**Possidius, *Vita Augustini* XIX–XXVII, is nine chapters of exactly that** — the printed headings run *"Augustine as judge," … "Household discipline."*"* **All seven quoted headings are verbatim and in the right chapters — I verified each against the printed text (XIX, XX, XXI, XXII, XXIII, XXIV, XXV).** But the list stops at **XXV** and silently drops **XXVI *"On the companionship of women"*** and **XXVII *"Service to the needy and sick"*** — both of which exist, both of which are ordinary episcopal practice, and both of which Round 7's own review quoted. §2 of this document carries a whole disclosed convention about not trimming quotations silently, and §2's Tier definitions have been corrected three times (Round 1's C1, Round 5's L2, Round 6's C1) for *"trimmed at the sentence boundary without an ellipsis."* The Decision Log's version of the same list drops **XXII** instead, so the two lists do not even agree with each other. *Fix:* an ellipsis, or all nine.

**LOW-3 — `notice_strip.py`'s design-justifying comment states a span count its own commit falsified; the Decision Log entry for the same commit states it correctly.** `scripts/notice_strip.py`: *"Measured across the nine deliverables: of **75** notice spans, ZERO cross a newline."* **75 is the pre-pass figure.** I counted with three independent implementations — the committed module, the pre-pass module, and my own scanner — and all three agree: **75 at `7c9b56b4`, 83 at `c4f7d376`.** The Decision Log's Round 7 entry says *"of **83** notice spans, zero cross a newline."* The empirical claim itself holds — 0 unterminated openers and 0 orphan `]**` across all nine files — so only the number is stale, in the comment that is the entire evidentiary basis for the line-scoping design. **Mooted at `a416fc6f`, which deletes the module.**

**LOW-4 — the generator's comment says the number-word map is "Derived rather than extended by hand." It was extended by hand.** `scripts/gen_story_index.py`: the comment *"Round 7's COSMETIC-2: this map stopped at six … **Derived rather than extended by hand.**"* sits directly above `_NW = {…, 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve"}` — **six new typed literals**, which is extension by hand and nothing else. This is the same shape as Round 7's LOW-4 (*"the check count is derived rather than typed"* — the suite emitted no count), one round later, in the file whose own doctrine is *"DERIVE, never type. A number typed here is a number that goes stale."* **It goes stale at Round 13.** The fix works and the index correctly prints *"Seven round(s)"* — I reproduced it. Only the description is wrong. *Fix:* either derive it, or say *"extended by hand; a `num2words` fallback would end this."* **This survives at `a416fc6f`.**

**LOW-5 — the Decision Log's Round 7 entry is accurate on everything it states and silent on two things the pass did.** I checked it claim by claim and it is the most honest artifact in this set — *"of 83 notice spans"* (right, where the module says 75); *"Eleven … Eight … One … two were the stripper"* (right, where the Disposition says one); *"at offset 3485, inside the vendoring header this build itself wrote"* (**verified: offset 3485, header, once in the whole file**); *"Traced by `git log -S`: the claim entered at the original draft `25edc87d`"* (**verified by my own `git log -S`**); *"Nine new tests"* (J1–J3 plus J4/J5 × three routes = nine). **What it does not record:** that the §7 item 5 and §8 item 9 rewrites created a superlative that contradicts §8 item 1 (MEDIUM-3), and that *"Five of the eight"* was left standing when its referent changed (MEDIUM-2). Round 7 raised exactly this as its Problem 4 — *"omission rather than misstatement, but material"* — and set the standard itself: *"a fix pass that damages a deliverable and repairs it silently is the pattern this log exists to prevent."* *Fix:* one clause per omission.

---

## COSMETIC

**COSMETIC-1 — a lowercase sentence opener in a deployable field, introduced by this pass.** `lpcstory004` Usage Guidance: *"The Representative should resist converting the sum into modern currency. **the** vendored ANF05 does print a conversion…"* The Round 7 fix for LOW-7 spliced a clause in and left the capital off. Usage Guidance is a field that instructs the Representative. **Survives at `a416fc6f`.**

**COSMETIC-2 — "two words after the sum" overstates the distance; the note is adjacent.** `lpcstory004`: *"an **editorial note**, two words after the sum."* The ANF prints *"…a sum of one hundred thousand sesterces, [An immense contribution, for the times…]"* — the note opens immediately after the sum, with nothing between. The phrasing is inherited verbatim from Round 7's own LOW-7, so this is a shared slip rather than a new one. *Fix:* *"immediately after the sum."*

**COSMETIC-3 — the boundary guard prints `'status not parsed'` where it means a non-Native row.** Forced from a fresh copy with row 204 named in a Source field and added to §3, the guard halts with *"row(s) ['204'] … are not Native in Source_Registry.md (**{'204': 'status not parsed'}**)."* It **fails closed**, which is the right direction and the reason this is cosmetic — but the parenthesis is supposed to tell the operator what the row's status *is*, and for row 204 it cannot read it. All seven live stories' rows (1, 7, 192) parse cleanly, so nothing is affected today. *Fix:* distinguish *"Excluded"* from *"unparseable"* in the message.

---

# Is the deliverable adequate to proceed to Doc_10?

**Yes, once four sentences are fixed — and on the story content, unreservedly yes.**

**What is ready, verified independently for an eighth time with instruments built for this round.** Seven stories, seven real texts. **140 of 157 quoted strings resolved automatically and the remaining 17 run down by hand to zero unexplained** — twelve are the document's own words or scare quotes, one is a string the build itself declares occurs zero times *(and it does: "to be killed by death by hunger and thirst" returns 0)*, one is a Possidius quotation that is continuous in the printed English but interrupted in the file by an intervening Latin page *(I located both halves at XXXI and confirmed the chunk reconstructs it correctly)*, and three are quotations of the document's own superseded text. **Zero quotations resolve to editorial apparatus** — the note mask was laid down before a single tag was stripped and confirmed in both directions on twelve randomly sampled note spans from twelve different works. **Every Possidius heading exact.** **Every Prosper OCR token exact, body-confirmed, header-excluded.** **Every absolute in live prose tested at source and holding.** The generator's 17 guards match its 17 `GUARD_LABELS`, the mismatch is itself a guard, four guards forced from fresh copies, and **the index regenerates byte-identical.** The test suite passes 50 checks at exit 0.

**What is not ready.** Four sentences in the Disposition and §8, none of which is a claim about a source. The ledger does not add up (MEDIUM-1); the danger figure is two too low (MEDIUM-2); the next pass is given two incompatible instructions (MEDIUM-3); the defect's own tally contradicts the table beneath it (MEDIUM-4).

**One thing I want on the record, because the tree moved.** `a416fc6f` deleted `notice_strip.py` and `test_notice_strip.py` while I was reviewing them. **At the commit this review audits, that module was correct** — 200,000 differential trials, 20 adversarial constructions, a full-corpus sweep against a 52-hit positive control, and word-for-word agreement with the generator's independent stripper on all nine deliverables. If the deletion is the right architectural call — and removing inline notices from canonical surfaces may well be — it should be recorded as an architectural simplification, **not** as the removal of a broken tool. It was not broken.

---

# CO-022 escalation assessment

- **Representative identity, title, or voice — does not apply.** No identity, title or voice decision is made in this document. **Noted and not escalated:** COSMETIC-1 sits in a Usage Guidance field, and MEDIUM-3's competing superlatives sit in §8, which instructs the next pass rather than the Representative. All are within this document's own gift.

- **Portfolio-level or cross-world — two inherited.**
 1. *The corpus-wide editorial-apparatus item.* **Eighth consecutive independent verification, still zero positive instances.** And this round it can be **narrowed**: Round 7's LOW-7 near-miss is now closed — `lpcstory004` names the ANF dollar note, confirms it is apparatus, and still excludes it, which is the class handled correctly in prose rather than merely avoided. **I recommend this comes back as a narrowing, with the `lpcstory004` disclosure attached as the worked example.**
 2. *The index-generator-as-build-artifact item.* Round 7 recommended routing this as a **CLOSE**. I concur and would add evidence: the guard count is now derived from the syntax tree, the guard *prose* is rendered from the same list the count is checked against, and **a mismatch between list and count is itself the seventeenth halting site** — which I forced. The remaining typed literal in the file is `_NW` (LOW-4), which is a different and much smaller thing.

- **Governance or methodology — one open, checked rather than accepted.** Doc_09 §8 item 7 escalates which half of CF's Tier 3 definition governs at `lpcstory006`. I read CF V7.4's Tier 3 paragraph whole from my own .docx extraction. The genus clause is verbatim as quoted; the hagiographic sentence is explicitly *"a specific type **within** this tier"*; **CF does not say which governs when they conflict.** The escalation is well-formed and correctly separated from the withdrawn *"a source is not a tier"* question. **I would sustain it.** The standing advice holds: the *Acta* is Latin in the Hartel volume, `INTAKE.md` licenses it, and reading it would likely moot the question — but see MEDIUM-3 before deciding whether it or Possidius XIX–XXVII goes first, because this document currently says both.
 **The methodology item Round 7 raised from its HIGH-2 is answered.** Doc_05's open item 10 and Doc_09 §7 item 5 no longer disagree: §7 item 5 now quotes Doc_05's *"vendored and unread beyond one identification"* and draws the unread/unwritten distinction explicitly. **The convention Round 7 proposed — re-read the routed-to document's open items before routing an absence to it — was followed.**

- **Unresolved tensions — one open, unchanged.** The 411 *Gesta*, relied on for nothing here. §6 item 5 and §8 item 4 state it accurately.

- **A process observation that is not an escalation but should be read by whoever sequences this work.** **A fix pass committed to these deliverables while an independent review of them was running**, and deleted two of the six artifacts the review was commissioned to attack. Nothing was lost here because I pinned the commit and re-ran everything, and I checked that every content finding survives into the new HEAD. But a review whose object changes mid-flight is a review that can report defects that no longer exist and miss defects that now do. **The build cycle's one-document-at-a-time discipline should extend to one-state-at-a-time: no fix pass on deliverables with a review in flight.**

---

# Check confirmation — including three defective checks of my own

**Three of my own checks failed before reporting, and I record them first**, because trusting a check that returns something adjacent to a claim is this build's documented meta-defect and I am not exempt from it.

**Defective check 1 — an ANF harness that disagreed with itself about apostrophes.** My first note-mask control returned 0 hits in *both* streams for two of five sampled note fragments. Cause: the query normaliser mapped `’`→`'` while the stream builder discarded it as punctuation. Had I trusted it, every quotation containing a possessive would have read as a miss.

**Defective check 2 — the same harness disagreeing about ligatures and non-ASCII letters.** After fixing check 1, one control still failed on a fragment containing `cœnæque`: the stream kept `œ` (it is `isalnum()`), the query normaliser deleted it. Both normalisers now fold `œ/æ/ß/ﬁ/ﬂ` and restrict to ASCII. **After the fix, 12 of 12 note-mask controls pass** — each fragment found in the with-notes stream and returning **zero** hits note-stripped.

**Defective check 3 — a Possidius harness that silently dropped an English page.** My first version reconstructed an English-only stream by running head, and returned **0 hits for "Household discipline"** — the printed heading of chapter XXV. **Had I trusted it I would have filed a HIGH accusing §7 item 5 of quoting a heading that does not exist.** It does exist; my language splitter had mis-assigned the page because the Latin running head follows rather than precedes it. I rebuilt on the whole de-hyphenated body — an English query cannot match Latin, so searching everything is strictly safer — and the chapter map now returns **all 31 chapters I–XXXI with no gaps.**

## Confirmations, one for every finding resting on a negative or a forced result

**C1 — for the Job 1 zero.** Old and new modules and my own scanner loaded side by side. **Positive control first:** the pre-pass module returns `notice-only` for **52** live-prose sentences on the pre-pass files. The same sweep on the committed module and files returns **0 of 479**. 200,000 fuzz trials, 0 disagreements. 20 adversarial cases, 0 disagreements, 0 live-prose deletions. Nine deliverables, `live()` byte-equal, 83 spans, 0 unterminated, **0 orphan `]**` outside any span** — which is what makes *"zero cross a newline"* provable rather than asserted.

**C2 — the ANF harness, both directions.** 3,475,736 characters, 381,835 note characters. Body control (*"the judgment of God and the favour of the people"*, Pontius, p. 269, title *The Life and Passion of Cyprian…*) found and marked **not** in note; nonsense returns MISS; **12 note fragments from 12 different works found with notes and returning zero note-stripped.** Every *Epistle* resolved by `title=`, never by position.

**C3 — the Possidius harness.** All 31 printed chapter headings located; the nine headings of XIX–XXVII each found once, in the correct chapter; *"we who were present"* returns **MISS**, which is the string the build itself records as occurring zero times — a positive control the build supplied; nonsense returns MISS; the bilingual page break at the death quotation located in both halves.

**C4 — for LOW-2 (the heading list).** Chapters XXVI and XXVII read whole from the printed text, not from a table of contents, and their headings quoted above are exact. Row 192 read in full: **Native**, **Vendored**, grade **A**, *"a genuinely bilingual edition"*. Doc_05 open item 10 read in full and the quoted clause is verbatim.

**C5 — for the Prosper verification.** Header and body separated at the file's own delimiter and counted independently, whitespace-normalised. Chunk's OCR string: **1 body, 0 header.** Corrected form: **0 body, 1 header, at offset 3485.** Each of `cxcellentissimus`, `Y. kl. Sept.`, `luliani`, `NVandalorum`: body only. Positive control: `excellentissimus` returns 1 in the header and 0 in the body, which is the mirror image and confirms the two streams are actually separated.

**C6 — for MEDIUM-1, MEDIUM-2 and MEDIUM-4.** All eleven HIGH findings enumerated from the **review artifacts' own headings**, not from the document, with each site read. All seven per-round counts read from each artifact's own verdict line and compared to the Disposition — **all seven match**. Round 2's eleven MEDIUM headings read in full to confirm the signature defect is genuinely absent there, and its M4 read whole to confirm it is a different class.

**C7 — for MEDIUM-3.** All four superlatives located by regex over live prose and each independently classified `live` by the committed `classify()`. `git show 7c9b56b4` used to establish which two predate the pass (§6 item 2, §8 item 1) and which two are new (§7 item 5, §8 item 9).

**C8 — for LOW-1 and the §6/§8 cross-reference audit.** Every `§N item M` reference in the world build enumerated with a pattern that does **not** require the `Doc_09` prefix, then filtered by reading each site to see which document's §8 it means. Counted against `7c9b56b4` as well, to establish the number was already wrong when written. **Separately: every §6 and §8 item-number reference resolves** — §6 has 5 items and every reference points at 1, 2 or 3; §8 has 9 and every reference points at 1, 2, 7, 8 or 9. §8 gaining item 9 renumbered nothing. **That is clean and worth crediting.**

**C9 — for the §2 count (which I confirm rather than fault).** Capitalisation sites found with a **case-sensitive** matcher built specially, after my case-insensitive one returned a meaningless zero. Controls: an exact body phrase returns True; the same phrase title-cased returns False; a Possidius heading returns True and its lower-case form False; nonsense False. Result: **7 sites, 6 of them in chunks, across 5 chunks** — exactly the *"Six … across five chunks"* the document claims, with the seventh being §2's own quotation of its example.

**C10 — for the generator credits.** 17 `sys.exit` sites from my own AST walk; `GUARD_LABELS` read from source at 17 entries; index regenerated **byte-identical** to the committed file; four guards forced from four fresh copies of the world tree (Story-Text notice, §3 row disagreement, boundary/non-Native, GUARD_LABELS mismatch), each returning rc 1 with its own message, against a clean control run at rc 0.

**C11 — absolute negatives that held, tested and recorded because they could have been findings.** *"not one of them speaks"* / *"preserves nothing any of them wrote or said"* (the lapsed) — *Ep.* XXVI read whole in body text: Cyprian reports that the lapsed wrote twice and quotes **no** words of theirs; *De Lapsis* read whole and **every** quoted first-person utterance in it is scripture; ANF's own Argument to *Ep.* XXVI states *"the Letter of the Lapsed to Which He Replies is **Wanting**."* **Held.** *"No source says whether the captives were recovered… Cyprian never writes again about the outcome"* — `sesterces` occurs in body text in **one work only**, *To the Numidian Bishops*; `captivity` across eleven works, none of them a follow-up. **Held.** *"Doc_08's Force 2A-2 … is the one force in this world's whole matrix that connects to no other"* — `lpc_Force_Index.md` gives 2A-2 Cross-Cell *"none — see §4"*, §4 records *"Deliberately isolated"*, and the tally line says *"15 connections, including **1** deliberate non-connection (`2A-2`)"*. **Held, and it is exactly one.** *"This world produced no apophthegmata-style collection, no sayings anthology, no* Vitae Patrum*"* — the only sayings collections vendored are Syriac/Egyptian (`palladius_paradise-v1-syriac`, `anan-isho_paradise-v2-sayings`). **Held.** *"No story in this repository draws on an Excluded row"* — proved by the generator's own boundary check passing at rc 0 over rows 1, 7 and 192, all Native.

**What I tested hardest.** In order: `notice_strip.py`, by an independent reimplementation, 200,000 differential trials, 20 constructions and a full-corpus sweep against a 52-hit positive control — **and it held**. Then every absolute in live prose, one by one at source, **103 of them never quoted in any prior review** — and they held. Then every quotation, through three purpose-built harnesses, two of which I had to repair before trusting — and they resolved. Then every count the pass's own edits could have staled — **which is where all four MEDIUMs were, and every one of them is arithmetic, not evidence.**

**What would change the verdict.** Fixing MEDIUM-1 (one clause), MEDIUM-2 (one word), MEDIUM-3 (rank the two candidates once) and MEDIUM-4 (one phrase). With those, **I would clear this document.** On the story content alone, considered apart from the summary layer, **I clear it now** — eight rounds have verified every quotation independently, found no composite, no invention, and no editorial apparatus in the world's voice, and that is what Doc_10 consumes.

---

# Errors in this round's brief

**Two, both in the framing that told me where to look. Neither changed where I looked, but both are wrong and the record should say so.**

**Brief error 1 — *"This module has now produced a HIGH in three of the last four rounds."* It is two of the last four.** `notice_strip.py` was created by the Round 4 fix pass (`a6a6be73`, verified with `git log --diff-filter=A`). It has been reviewable in Rounds 5, 6 and 7 and produced a HIGH in **Round 5 (HIGH-2)** and **Round 7 (HIGH-1)** — not in Round 6, whose single HIGH was `lpcstory007`'s denial of a second account of Augustine's death, and not in Round 4, whose three HIGHs were all in Absent Story Notes. The brief's rider — *"each time in the fix for the previous round's finding"* — is right for both of the two.

**Brief error 2 — *"The signature defect has produced a HIGH in seven of seven rounds."* It is six of seven.** **Round 2 returned 0 HIGH**, which I confirmed from Round 2's own verdict line, from the Disposition's round table, and from the Document Log's *"No HIGH; reviewer states it could not manufacture one."* The defect appears at Rounds 1, 3, 4, 5, 6 and 7 — **eight instances across six rounds**. This is the same error the deliverable makes at MEDIUM-4, so the brief and the document are wrong together, which is worth noting: the brief did not inherit it from me and I did not inherit it from the brief.

**Everything else in the brief checks out.** All four commit refs are correct and I verified each. The known-false premises are correctly flagged: **editorial apparatus read as the world's voice is zero in this deliverable**, verified for an eighth time with the mask built before tag stripping and with three of my own defective checks caught and discarded; and **CF line numbers are extraction-dependent**, which is why none appears above. The brief's warning about positional attribution in ANF05 is well founded and load-bearing — the corpus prints Celerinus's and Lucian's letters under Cyprian's name, so a positional check would misattribute `lpcstory005`'s two central quotations; my harness resolves every quotation by `title=`. The brief's instruction to mark `<note>` spans **before** stripping tags is the single most important line in it. And the brief's warning to verify the refs myself proved more necessary than it can have known — **the tree they point at changed underneath this review**, which is reported in the box at the top.

---

# VERDICT: **MINOR REVISION**

**0 HIGH · 4 MEDIUM · 5 LOW · 3 COSMETIC.**

**Two things happened this round that have not happened before in this document's history, and they are the finding.** **First, the tool held.** I attacked `notice_strip.py` with an independent reimplementation, 200,000 differential trials, twenty constructed adversarial shapes and a sweep of every live sentence in the corpus against a positive control that fires 52 times on the old module — and it returned zero. The rewrite from regex to a line-scoped depth scanner closed Round 7's HIGH-1 and MEDIUM-2 **as a class**, and the module was correct at the moment a concurrent pass deleted it. **Second, the signature defect produced nothing.** I extracted 111 absolute and exclusivity claims from live prose, 103 of them never quoted in any review artifact, and every testable one held at source — the lapsed silence, the Numidian ransom, the isolated plague force, the Possidius chapters, the Prosper OCR. Eight rounds in, every quotation in this repository still resolves, nothing is composited, nothing is invented, and no editorial apparatus is read as the world's voice.

**What is left is arithmetic.** All four MEDIUMs are numbers or neighbouring sentences that this pass's own edits falsified — a ledger that sums to ten under a heading of eleven, a danger figure two too low, two items in one list each claiming to be the single largest improvement, and a *"seventh consecutive round"* refuted by a table ten lines below it. Round 6 named this mechanism, Round 7 named it again and wrote the convention that prevents it, and the convention was not adopted. **It is now the only thing wrong with this document, and it is four sentences.**

*Simulated review — informational only, not an Article 31 substitute.*
