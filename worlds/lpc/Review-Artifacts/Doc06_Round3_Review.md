# Doc_06 — Full Interpretive Lexicon Development: Latin Pastoral-Congregational Christianity
## Round 3 Independent Adversarial Review — targeted verification of the Round 2 fix pass

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-15.

**Scope.** Targeted recheck per `CLAUDE.md` ("from round 2 onward, do a targeted recheck — only what changed, against prior findings"). The unit of review is the diff `1516e71b..a35903e3` ("lpc: apply Doc_06 Round 2's four directed findings") — 6 files, 55 insertions, 20 deletions — plus every claim that diff makes about material it did not change, plus the full re-derivation the index's own header invites. I read the diff, not a summary of it. I drafted nothing under review, wrote neither prior round, and treated both prior rounds as claim sets to test rather than as authority.

**Reviewed:**
- `Doc_06_Full_Lexicon_Development.md` (166 lines) — read in full.
- `Lexicon-Chunks/lpclex002`, `lpclex017`, `lpclex019` (changed) — read in full, before and after, at `1516e71b` and `a35903e3`.
- The other sixteen chunks — parsed programmatically for front-matter, Related-Terms, Registry-row citations, `Author Gravity note` and `## CT Contest Type`; every `## World Meaning` section extracted and swept.
- `Lexicon_Deployment_Index.md` — all eight sections; §1 fully regenerated and diffed.
- `Review-Artifacts/Doc06_Round1_Review.md` and `Doc06_Round2_Review.md` — read in full, as claim sets.
- `lpc_Decision_Log.md`, the 2026-09-15 (second) entry.

**Read as governing standard, not reviewed:** `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0 (front-matter and World Meaning sections read directly); `Doc_03_Lexicon_Candidate_List.md`; `/home/user/cic-project/CLAUDE.md`.

**Vendored source opened directly:** `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (5,728,373 characters). `div1 id="iv" title="Cyprian."` runs from offset 2,069,240 to the `</div1>` at relative offset 2,567,567; 2,863 `<note>` elements inside it, well-formed and non-nested (open/close counts equal, maximum depth 1, final depth 0 — checked before relying on the span marking).

---

## What I checked, and how, stated so it can be re-run

**1. Full index re-derivation (the check the index names as its own).** I parsed all nineteen chunk files from disk — Term, Tier, the seven tag columns, Aliases and Related-Terms out of the fenced front-matter; a regex sweep of each whole chunk body for Registry-row citations, handling comma runs, "and"-joined pairs, en-dashes and hyphens; the literal string `Author Gravity note` — and diffed the result cell-by-cell against `Lexicon_Deployment_Index.md` §1. **19 rows × 13 columns = 247 cells: one mismatch.** See **H-R1**. The Registry-row column, which is the column that failed at Round 1's H1, reproduces on all nineteen rows under my parser and independently under Round 2's eye-read of all fifty `\brows?\b` hits — two independent methods agreeing, per `CLAUDE.md`.

**2. Reciprocity, rebuilt from the files.** Directed-edge set built from the nineteen Related-Terms fields against a hand-written handle map, not read off the index. **122 directed edges, 61 reciprocal pairs, zero one-way, zero self-loops, zero unresolvable handles.** §5's arithmetic is right.

**3. Tag, tier and Author-Gravity tallies, recounted from the chunks.** AS 6 · SC 13 · DR 9 · TC 11 · RT 9 · PV 11 · CT 3; tiers 7 / 12 / 0; Author-Gravity notes 8; `## CT Contest Type` headings 3. Every count **and every membership list** in §2, §3, §4 and §6 reproduces exactly (the only diffs my comparator raised were my own asterisk-stripping of the two italicised *libelli* / *libellatici* term names — an artifact of my script, not of the index; confirmed by eye before discarding).

**4. The M-N1 source claims, verified with note spans marked *before* tags were stripped.** I marked all 2,863 `<note>` spans by character offset first, then counted `certificates?` case-insensitively across the Cyprian `div1`, then classified each hit by whether its offset falls inside a marked span. Result: **42 total, 4 inside `<note>`, 38 outside.** I then located every one of the eight quotations in `lpclex019` in the tag-stripped text with an offset map back into the raw markup, and tested each for note-containment.

**5. World Meaning sweep, all nineteen.** Every `## World Meaning` extracted and swept for analytical-distance markers (*scholars believe, this reflects, the sources indicate, evidence suggests, historically, reconstruction, appears to, seems to, the record shows*), for editorial-provenance vocabulary (*vendored, editorial, 19th-century, Confidence-A/B/C*), for raw filenames and Doc references, and for square brackets.

**6. Attribution audit.** Every sentence in `Doc_06` and the index that attributes a verification to Round 1 or Round 2 was located by grep and checked against what that round's text actually says and actually did.

---

## A premise in my own assignment that did not survive checking

My assignment stated that the fix pass "used unguarded global string replacements in `Doc_06_Full_Lexicon_Development.md` (e.g. 'eighteen' → 'nineteen')" and directed me to hunt the collateral damage. **That did not happen.** No global replacement was run. `Doc_06` contains "eighteen" six times and "nineteen" five times; the diff shows the word *"eighteen"* being **added**, deliberately and correctly, at two sites (the Status paragraph and the Disposition), in order to scope Round 1's verifications to the eighteen chunks it actually saw — which is the M-N2 fix working as intended. Four of the six surviving "eighteen"s are correct in context (Doc_03's eighteen candidate terms, twelve of eighteen flagged Tier 1, the eighteen-term list, Round 1's eighteen chunks). **The real defect in that neighbourhood is the opposite of the one I was pointed at**: two arithmetic sites Round 2 named were *not* touched at all, while the document and the Decision Log both claim they were. That is **M-R4**, and I would have mis-filed it as collateral damage from a replacement if I had trusted the brief. Recorded per the assignment's own instruction that a failing check gets the same scrutiny as a passing one — here the checker was wrong and the document was right.

---

## VERDICT: REVISION REQUIRED

**New findings: 1 HIGH · 4 MEDIUM · 5 LOW · 2 COSMETIC — 12 in total.**

**The four directed fixes: 1 FIXED · 3 PARTIALLY FIXED.**

**What holds up, and it is the substance.** The thing Round 2 said blocked Doc_07 is genuinely cleared. `lpclex002`'s World Meaning is clean — I swept all nineteen World Meanings and **zero** carry a bracket, an analytical-distance marker, an editorial-provenance term, or a filename. The disclosure now sits in Key Sources, reads coherently, and the World Meaning lost nothing it needed: the sentence the disclosure is about is intact and the paragraph flow is continuous. The M-N1 correction is right at source and I verified it the hard way: the corrected quotation — *"thousands of certificates were daily given, contrary to the law of the Gospel, I wrote letters in which I recalled by my advice, as much as possible, the martyrs and confessors to the Lord's commands"* — occurs **exactly once** in the Cyprian `div1`, at an offset **outside every one of the 2,863 marked `<note>` spans**, inside `div3 id="iv.iv.xiv" n="XIV" shorttitle="Epistle XIV"`. The chunk's new "— Epistle XIV" attribution is correct. The endnote variant the chunk disclaims sits inside `<note class="endnote" id="iv.iv.x-p5">`, as claimed. The **42 / 4 / 38** split reproduces to the number. All eight of `lpclex019`'s quotations are verbatim and all eight sit outside every note span. Reciprocity survives at 122/61/0. Every tag count, tier count, Author-Gravity cell and Registry-row cell reproduces. `lpclex019` is row seven of the Editorial-Apparatus Register. M-N4's cross-reference now runs both ways and both directions are substantively correct. The six carried findings are named in §5 and — with one exception noted below — named honestly; I checked each against Round 2's text and against the current files, and **none of the six touches the five entries `Doc_06` §6 hands to Doc_07** (*confessor*, *the lapsed*, *reconciliation*, *communion*, *heresy*). That claim in §5 holds.

**What does not.** The pass edited `lpclex017`'s Aliases line in a chunk and edited the index by hand in the same commit without regenerating it — leaving exactly one stale master-table cell, which is Round 1's H1 defect class recurring in the deliverable whose central claim is that re-deriving the table is the check. Three of the four directed fixes landed at some of their named sites and not others: index §6 still carries the Round-1 over-attribution that M-N2 named by name; three statements of the flat **42** still stand, one of them two paragraphs from the paragraph that calls 42 "the figure a naive sweep returns"; and the register's own count is now **five** in one place, **six** in another and **seven** in a third, across two co-produced documents. And `Doc_06` and the Decision Log both assert that L-N1 was "corrected in this pass" when two of its three named sites are untouched — a false claim of correction, made by the same pass that was applying M-N2, which is the finding about false claims of verification.

---

## Status of the four directed fixes

| # | Finding | Status |
|---|---|---|
| **H-N1** | Editorial disclosure placed inside `lpclex002`'s Tier 1 World Meaning | **PARTIALLY FIXED** |
| **M-N1** | `lpclex019` quoting the editorial endnote as Cyprian; 42-vs-38 unreconciled | **PARTIALLY FIXED** |
| **M-N2** | Round 1 credited with work it did not do | **PARTIALLY FIXED** |
| **M-N4** | One-way *certificate* disambiguation between `lpclex017` and `lpclex019` | **FIXED** |

### H-N1 — PARTIALLY FIXED

Round 2 gave four explicit instructions. Two landed; two did not.

**Landed.** (a) The bracketed paragraph is gone from World Meaning — verified not by reading the diff but by re-extracting all nineteen World Meanings and sweeping them: **zero hits, all nineteen clean**, on brackets, analytical-distance markers, editorial-provenance vocabulary, filenames and Doc references. Before `4f35c7bc` `lpclex002` was clean, at `4f35c7bc` it was the sole hit, and at `a35903e3` it is clean again. (b) The disclosure sits in Key Sources, which is one of the two sites Round 1 specified. It is coherent, it correctly separates what is the editor's from what is Cyprian's, and the World Meaning did not lose anything: the sentence it qualifies (*"some never went near the altar but bought a paper saying they had"*) is intact and reads continuously into the next paragraph.

**Did not land.** (c) Round 2's fix said, in terms, *"phrase it without a filename."* The new Key Sources paragraph reads *"`lpclex018` carries the disclosure in full"* — the same raw filename, moved rather than removed, in a chunk whose own Related-Terms field already carries the proper handle (*libellatici / sacrificati*). (d) Round 2's fix said *"Do not stack a second bracket on top of the first — remove and redo, per `CLAUDE.md`'s 'no fix on a fix.'"* The pass did the opposite: it edited the existing `**[CORRECTION, 2026-09-15 — Round 1's H3.]**` block **in place**, extending it to `**[CORRECTION, 2026-09-15 — Round 1's H3, corrected again at Round 2's H-N1.]**`. That is a fix stacked on a fix, at the exact site where it was forbidden by name.

**And the sub-claim the assignment asked me to test specifically: the chunk's Final Assembly line is still not true.** `lpclex002` line 69 still reads *"No brackets or builder notes remain."* The file contains a bracket and a builder note, in Key Sources. Round 2 listed that falsity as one of the four rules H-N1 broke; the pass fixed the location of the bracket and left the false statement about it standing. See **L-R1**.

### M-N1 — PARTIALLY FIXED

**Landed, and it verifies at source.** The quotation is replaced with Epistle XIV's own text, correctly attributed, and I confirmed it independently by the method the chunk itself now prescribes — marking note spans before stripping tags. The 42 / 4 / 38 split reproduces exactly. `lpclex019` is the seventh row of index §7, with an accurate description. Index §7's closing paragraph now states the mechanical control correctly.

**Did not land.** Round 2's fix (b) was *"State the count as 38 in Cyprian's own text, 4 in editorial notes, 42 in the `div1` span"* — that is, reconcile the record rather than overwrite one figure with another. It was stated in one paragraph of `lpclex019` and in index §7, and left unreconciled at three other sites, one of which is in the same file:

- `lpclex019`, Key Sources, Discovery note: *"did not sweep the English word the translation actually uses, **which appears 42 times** and carries two distinct referents."* Two paragraphs above, the same section says *"42 is the figure a naive sweep returns."* The chunk now contradicts itself inside one section.
- `Doc_06` §2.4: *"'Certificate' occurs **42 times in Cyprian's own `div1` span**"* — offered as the attestation ground for adding the term. Round 2's whole point was that *"scoped to Cyprian's own `div1` span"* is true and is not the same thing as Cyprian's own words.
- `Doc_06` §5 item 7: *"did not sweep the English word the translation uses **42 times**."*

See **M-R2**. The arithmetic is right everywhere; it is the reconciliation that was applied in one place and not the other three.

### M-N2 — PARTIALLY FIXED

Round 2 named **four** sites. Three are fixed and fixed well; the fourth is untouched.

**Fixed.** `Doc_06` Status (now: *"it reviewed **eighteen** chunks — `lpclex019` did not exist yet — and on those eighteen found no misquotations in its spot-checks, 110 reciprocal links across 55 pairs…, no analytical-distance markers in eighteen World Meanings, and 7 Yes / 11 No Author-Gravity cells"*). `Doc_06` Disposition (Round 1 and Round 2 split out by round). Index §5 (now credits Round 2, with the Round 1 figures stated correctly). I checked every number in all three against Round 1's own text: 110/55, 7 Yes / 11 No, eighteen World Meanings, three CT contest types, and the hedge *"in its spot-checks"* — which is exactly right, because Round 1 said *"a substantial majority, spot-checked."* This is a careful, honest rewrite.

**Not fixed.** `Lexicon_Deployment_Index.md` §6, closing line, unchanged: ***"Round 1 verified every Yes and every No against the chunks."*** It sits directly under a table of **eight** Yes rows spanning **nineteen** entries, one of which is `lpclex019`. Round 1 verified seven Yes and eleven No across eighteen. `lpclex019`'s Author-Gravity cell has still never been independently verified by any round that names itself. Round 2's M-N2 quoted this sentence explicitly as one of its four sites. See **M-R1**.

**And the pattern recurred against Round 2.** `Doc_06`'s Disposition now credits Round 2, on nineteen chunks, with *"every quotation verbatim **but one**."* Round 2's own scope statement is a targeted recheck of the changed material: it verified eight quotations in `lpclex019` and states at its head that it did not re-review the untouched chunks. See **L-R4**.

### M-N4 — FIXED

Both directions are present and both are substantively right. `lpclex017`'s Do-Not-Retrieve-When now names the collision, identifies its own referent as the empire's document, routes the confessors' letter of peace to `lpclex019`, and states that a bare *"what was a certificate?"* should surface both. `lpclex019`'s Do-Not-Retrieve-When states the reciprocity. Index §8 records it accurately and attributes it to Round 2's M-N4 correctly. The ambiguity is marked in `lpclex017`'s alias list.

Two residues, neither of which unmakes the fix: Round 2's fix also asked that the shared bare alias be narrowed on **both** sides, and `lpclex019` still carries a bare `certificate` alias unchanged; and the narrowing that *was* done on `lpclex017` is the change that produced the stale index cell at **H-R1**.

---

## NEW — HIGH

### H-R1 — The index was hand-edited while a chunk's front-matter changed, and one master-table cell is now stale: `lpclex017`'s Aliases

**Site:** `Lexicon_Deployment_Index.md` §1, row 17, Aliases cell.

| | |
|---|---|
| **Index prints** | `libellus, libelli, certificate, sacrifice-certificate, certificate of compliance` |
| **Chunk holds** | `libellus, libelli, sacrifice-certificate, certificate of compliance, certificate (ambiguous — see Do-Not-Retrieve-When)` |

**What I found.** The diff changes `lpclex017`'s `Aliases:` line and changes `Lexicon_Deployment_Index.md` at five places — the Status line, the Revised line, §5, §7 and §8 — and does not touch the master table. I re-derived all 247 cells from the nineteen chunks and diffed: **246 match exactly, this one does not.** It is the only stale cell in the table, and it is precisely the cell the fix pass changed upstream.

**Why this matters.** Three reasons, and the third is the operational one.

First, the index's own header states its central claim: *"Every row is parsed directly out of `Lexicon-Chunks/lpclex*.md`… **Re-deriving it is the check:** regenerate and diff."* That claim is false again, for the second time in three rounds, and it is false in the same column-adjacent way — a cell that does not reproduce from the chunk it claims to be derived from. Round 1's H1 said an index advertised as safe to diff *"is worth nothing if the derivation is lossy."* This time the derivation is not lossy; the index simply was not re-derived. The header still says *"Generated from the chunk files, not maintained alongside them"* — and this commit maintained it alongside them, by hand.

Second, the header's Round-1 correction note says the generator was fixed at the pattern rather than at the cell. The evidence of this commit is that the generator was not run at all: five prose sections were edited by hand and the table was left alone.

Third, and worst: **this stale cell defeats the fix it was produced by.** M-N4 exists because a retrieval layer resolving the bare word *certificate* must not answer with `lpclex017` as if it were the only referent. The chunk now qualifies that alias. The index — the artifact whose whole stated purpose is to let a builder answer retrieval questions *"without opening a single chunk"* — still lists the bare, unqualified `certificate` under `lpclex017`. Anything built from the index rather than from the chunks inherits exactly the collision M-N4 was raised to close.

**Fix.** Re-run the generator over all nineteen chunks and commit the regenerated table, rather than hand-patching row 17. Then state in the header, honestly, that §§5–8's prose is hand-maintained and only §1 is generated — because the header currently claims generation for a file five of whose eight sections are written by hand, which is what let this happen.

---

## NEW — MEDIUM

### M-R1 — Index §6 still credits Round 1 with verifying every Author-Gravity cell, including one it never saw — a site M-N2 named explicitly

**Site:** `Lexicon_Deployment_Index.md` §6, closing paragraph: *"**8 of 19 entries carry an Author Gravity note.** The column is derived from the presence of that note in each chunk, so it cannot disagree with the chunk. **Round 1 verified every Yes and every No against the chunks.**"*

**What I found.** Round 1's own answer to its fifth review question reads: *"All **seven** 'Yes' cells (the flock, the lapsed, reconciliation/penitential discipline, confessor, grace, plenary Council, compel them to come in)… all **eleven** 'No' cells."* Seven and eleven is eighteen. The table above this sentence has eight Yes cells across nineteen entries; the eighth is `lpclex019`, which did not exist when Round 1 ran. I re-derived the column myself and it is correct — eight chunks carry an `Author Gravity note` and they are exactly the eight the table marks Yes — so the **column** is sound and the **attribution** is not.

**Why this matters.** This is the identical sentence-shape that M-N2 was raised about, at one of the four sites M-N2 named, left standing while the other three were rewritten well. `CLAUDE.md`: *"A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation."* A Doc_07 thread reading §6 would reasonably treat `lpclex019`'s Author-Gravity cell as independently confirmed. It has been confirmed — by Round 2 and now by me — but not by Round 1, and the sentence says Round 1.

**Fix.** Replace with the Round 1 / Round 2 split already used at §5: *"Round 1 verified seven Yes and eleven No across eighteen entries; Round 2 re-derived the column across all nineteen."*

### M-R2 — The 42-vs-38 reconciliation landed in one paragraph and not in the three other places the figure is stated, including the same section of the same chunk

**Sites:** `lpclex019_certificates-letters-of-peace.md`, Key Sources, Discovery note; `Doc_06_Full_Lexicon_Development.md` §2.4 and §5 item 7.

**What I found.** The Attestation paragraph now says, correctly and verifiably, *"**38 is the figure that attests the term; 42 is the figure a naive sweep returns**, and the gap between them is this corpus's standing hazard."* Two paragraphs later, in the same Key Sources section, the Discovery note says the translation's own word *"appears 42 times and carries two distinct referents"* — the naive figure, unqualified, presented as the discovery evidence. `Doc_06` §2.4 does the same (*"occurs **42 times in Cyprian's own `div1` span**"*), and it is doing load-bearing work there: it is the stated ground on which the nineteenth term was added. §5 item 7 does the same again.

I verified the arithmetic rather than assuming it: 42 occurrences of `certificates?` in the Cyprian `div1`, of which 4 fall inside marked `<note>` spans, leaving 38. Both figures are true of different things. That is exactly why the record needs to say which is which everywhere it says either — which is what Round 2's fix (b) asked for and what the entry's own new paragraph argues for.

**Why this matters.** `Doc_06` §2.4's 42 is not a passing number; it is the evidentiary justification for breaking Doc_03's eighteen-term list. Stating it as *"in Cyprian's own `div1` span"* reproduces, word for word, the ambiguity Round 2 identified as the root of M-N1 (*"'scoped to Cyprian's own `div1` span' is true and is not the same thing as Cyprian's own words"*). And a chunk that says 42 is a naive sweep in one paragraph and states a flat 42 as evidence two paragraphs later is not a record a later pass can rely on.

**Fix.** At all three sites, state it as the chunk's Attestation paragraph now does: 38 in Cyprian's own text, 4 in editorial notes, 42 in the `div1` span. The referent-split figure in the Discovery note (two distinct referents) should be stated against 38, not 42, since the four note-occurrences are not part of what attests the term.

### M-R3 — The Editorial-Apparatus Register now has three different counts in two co-produced documents

**Sites:** `Lexicon_Deployment_Index.md` §7; `Doc_06_Full_Lexicon_Development.md` §5 item 6 and Disposition.

| Where | What it says |
|---|---|
| Index §7 heading and table | **Seven** entries (seven rows; `lpclex019` added this pass) |
| `Doc_06` §5 item 6 | ***"registers **six** entries"***; ***"registers the six local instances; **five are excluded** from the entries outright and **the sixth is marked in place**"*** |
| `Doc_06` Disposition, CO-022 category 2 | ***"of which §5 item 6 above registers **five** local instances"*** |

**What I found.** The pass raised the register from six rows to seven and rewrote §5 item 6's exclusion clause **in the same commit**, without changing either count. The "five" in the Disposition is the site Round 2's L-N1 named as a contradiction when the register held six; it now disagrees with two numbers instead of one. And the rewritten clause in §5 item 6 — *"five are excluded from the entries outright and the sixth is marked in place"* — no longer describes the register at all: there are seven entries, and the seventh is neither excluded nor marked in place. It is a quotation that was replaced, with the error recorded.

**Why this matters.** The editorial-apparatus register is the single most safety-adjacent control in this deliverable — it exists to keep a 19th-century Protestant editor's theological verdicts from reaching a participant as this world's own voice. Index §7's own closing paragraph says *"a register listing the instances its author remembered is not a control."* A register whose count is stated three different ways in the two documents that point at it is, in the same sense, not a control: a reader cannot tell from `Doc_06` how many instances there are, and `Doc_06` is where the escalation is filed.

**Fix.** Set all three to seven. Rewrite the exclusion clause to describe what actually happened to each of the seven — five excluded from the entries, one (`lpclex002`) marked in place, one (`lpclex019`) a misquotation replaced and recorded.

### M-R4 — `Doc_06` and the Decision Log both state that L-N1 was corrected; two of its three named sites are untouched

**Sites:** `Doc_06_Full_Lexicon_Development.md` §1 (line 28) and Disposition (lines 162, 164); `lpc_Decision_Log.md`, 2026-09-15 (second) entry.

**What I found.** `Doc_06`'s Disposition lists L-N1 among the six carried findings as *"**L-N1** (arithmetic not carried through — §1 said eighteen chunks; **corrected here**)"*, and the Decision Log records *"L-N1 (arithmetic — **corrected in this pass**)."* Round 2's L-N1 named three sites. Checking each:

1. **§1, "Does" paragraph** — *"and **eighteen** self-contained deployment chunks written to the L4 template."* **Unchanged.** There are nineteen. This is the one site `Doc_06`'s own text names as corrected, and it is the one site most visibly not corrected.
2. **Disposition, CO-022** — *"§5 item 6 above registers **five** local instances."* **Unchanged.** (Also **M-R3**.)
3. **§5 item 6, "excludes all six"** — **changed**, and the change is now stale per **M-R3**.

A fourth instance of the same arithmetic, which Round 2 did not name, also stands: §4's heading, *"the pattern named once here rather than **eighteen** times."*

**Why this matters.** This is not the arithmetic; L-N1 is a LOW and the project lead directed it carried, so an uncorrected L-N1 is not a defect I am reporting. **What I am reporting is the claim of correction.** A document asserting it has fixed something it has not is the same failure class as M-N2 — a record claiming a verification that was not performed — committed by the pass whose job that commit was. `CLAUDE.md`'s "fix it right" section exists for precisely this: *"No band-aids… no 'good enough for now.'"* The honest options were to correct the three sites or to carry L-N1 plainly. The pass did neither.

**Fix.** Either make the two remaining edits ("nineteen"; "seven") and keep the claim, or delete *"corrected here"* and *"corrected in this pass"* from both records. Not both.

---

## NEW — LOW

### L-R1 — `lpclex002`'s Final Assembly line is still false, and the pass stacked a correction onto the correction it was sent to undo

`lpclex002` line 69: *"No brackets or builder notes remain."* The file's Key Sources carries `**[CORRECTION, 2026-09-15 — Round 1's H3, corrected again at Round 2's H-N1.]**`. Round 2 listed this exact falsity as one of the four rules H-N1 broke and instructed *"remove and redo"* rather than stacking. The pass edited the existing bracket in place to append *"corrected again at Round 2's H-N1"* — a second correction note inside the first, which is what both Round 2 and `CLAUDE.md`'s "no fix on a fix" rule forbid by name. The substance of the correction note is accurate and well written; its placement and its stacking are not, and the completion statement above it is untrue of the file it appears in.

**Fix.** Per Round 2, and per this world's own standing rule quoted at Round 2's L-N2 — the chunk states the current corrected text, the Decision Log and Review-Artifacts carry the history. Then the Final Assembly line is true without editing it.

### L-R2 — The pass introduced a bracketed builder note into `lpclex019`, which had none, under a Final Assembly line asserting that none remain

At `1516e71b`, `lpclex019` contained no bracketed builder note — I checked the file at that commit. At `a35903e3` it carries `**[CORRECTION, 2026-09-15 — Round 2's M-N1.]**`, while line 73 still reads *"No brackets or builder notes remain."* This is the H-N1 falsity, newly created in a second chunk by the pass that was applying H-N1. It is the same family as carried L-N2 and I am not re-reporting L-N2 — L-N2's own description ("five chunks and the index header") is still exactly accurate, since `lpclex019` was already one of the five. What is new is that the pass **deepened** a live carried finding in two files rather than leaving it where Round 2 found it, and falsified a completion statement that had been true.

**Fix.** Move both correction blocks to the Decision Log, which already carries them at greater length, or amend the two Final Assembly lines to say what is true.

### L-R3 — `Doc_06`'s own status apparatus was not carried through the pass

Three sites, all in the document the pass rewrote:

- **Status line 20:** *"**REVISED after Round 1** — not self-disposed."* The index's Status line was updated in this same commit to *"REVISED after Rounds 1 and 2"*, and so was the Decision Log. `Doc_06`'s own Status line — the first thing a Doc_07 thread reads — was not.
- **Document Log (line 150–152):** three rows, ending at *"2026-09-15 | Round 1 fix pass."* There is **no row** for the Round 2 review and **no row** for the Round 2 fix pass. The Document Log is the document's own audit surface and this commit added nothing to it.
- **Disposition line 158:** *"…adequate to proceed to Doc_07 after one narrow fix pass; **that pass is this one**, and all findings are applied."* There have now been two passes, and six findings are deliberately not applied. The next sentence, correctly updated, says *"Whether **either** fix pass succeeded is not this thread's to declare"* — so the paragraph contradicts itself one sentence apart.

**Fix.** Update the Status line; add two Document Log rows (Round 2 review — REVISION REQUIRED 1H 4M 4L 1C; Round 2 fix pass — four applied, six carried); rewrite the first Disposition sentence to describe both passes.

### L-R4 — `Doc_06` credits Round 2 with a quotation check wider than Round 2's stated scope

`Doc_06` Disposition: *"Round 2, on **nineteen** — all 247 index cells re-derived with zero mismatches, 122 links across 61 pairs with zero one-way, **every quotation verbatim but one**, and nothing invented in the two reclassified entries."* Round 2 states its scope at its head: *"I did not re-review the eleven chunks the fix pass left untouched, except where a changed document makes a claim about them."* What it verified was eight quotations in `lpclex019` plus the changed material in `lpclex017`/`lpclex018`. It did not check every quotation in the lexicon, and nobody has: Round 1 checked *"a substantial majority, spot-checked."*

The phrase is also imprecise about the one exception — the endnote quotation *was* verbatim; what was wrong was its attribution. This is the M-N2 pattern surviving one round later with Round 2 as its subject, in the paragraph written to fix M-N2. Grading it LOW rather than MEDIUM because the claim is a modest overreach rather than a wholesale transfer of verification, and because the underlying fact (no misquotation has been found) is true so far as either round looked.

**Fix.** *"Round 2, on the changed material — eight quotations in `lpclex019` verbatim at source, one of them from the editorial apparatus rather than Cyprian's text."*

### L-R5 — Round 2's two "noted, pre-existing" items are recorded nowhere and have gone quiet

Round 2 recorded two defects outside its counts, *"rather than let them go quiet"*: that `lpclex011` *suffrage* carries no `[DR]` tag although `Doc_06` §4 names it as one of the two sharpest instances of distortion shape 2 and the chunk's own Distortion Risk pairing is a textbook DR case; and that this world has no `Open_Gaps_Tracking.md`. I grepped `Doc_06`, the index and `lpc_Decision_Log.md`: **neither appears anywhere.** They are not among the six carried findings at §5, and `Open_Gaps_Tracking.md` still does not exist (3 of 12 worlds under `World-Builds/` have one).

`CLAUDE.md` is direct: *"Every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread."* Both items are now known review outcomes living only in a review artifact nobody is required to re-open. The `[DR]` item is also the one Round 2 says makes the zero-Tier-3 claim (carried L-N3) *"look untested when it is in fact sound"* — so it is load-bearing for a carried finding's disposition.

**Fix.** Record both in the Decision Log entry for this pass, and open this world's `Open_Gaps_Tracking.md` — or, if the file's absence is a fleet-level matter for the project lead as Round 2 judged, say so in the record instead of saying nothing.

---

## NEW — COSMETIC

### C-R1 — The two edited chunks' front-matter now carries markdown and a raw filename that no other chunk's does

`lpclex017` and `lpclex019` are the only two of nineteen whose fenced Retrieval Front-Matter block contains `**bold**` markers and a backticked filename. The block is a code fence, so the asterisks and backticks are literal characters to anything parsing it, and the L4 template's own front-matter specimen is plain text throughout. `lpclex017`'s new text also points to *"`lpclex019`"* by filename, where its sibling `lpclex019` points to *"libelli"* by the Related-Terms handle — two conventions for the same cross-reference, introduced in one commit.

**Fix.** Strip the emphasis markers; use the handle (*certificates*) rather than the filename, matching `lpclex019`'s own line and the Related-Terms convention.

### C-R2 — "which is where Round 1 specified it" narrows what Round 1 actually said

`lpclex002`, index §7's neighbourhood and the Decision Log all now say the disclosure sits in Key Sources *"where Round 1 specified it."* Round 1's fix reads: *"one sentence in `lpclex002`'s **Key Sources or Author Gravity note**."* Two sites were offered; the pass chose one, correctly, and then reported Round 1 as having named only that one. Trivial in effect — the chosen site is compliant either way — but it is a small instance of the same habit the two Medium attribution findings above are about.

---

## Were Rounds 1 and 2 right?

**Round 2's grading of Round 1's H3 as FIXED WRONGLY: upheld, on independent evidence.** Round 1's H3 fix instruction named Key Sources or the Author Gravity note. The Round 1 fix pass put a square-bracketed paragraph — naming a filename, a Confidence rating, and the vendored edition's editorial apparatus — inside a Tier 1, `[RT]`-tagged World Meaning. I confirmed the shape of that independently rather than through Round 2's account: sweeping all nineteen World Meanings at `1516e71b` returns `lpclex002` and nothing else; sweeping the same nineteen at `a35903e3` returns nothing at all. The section was clean before that fix and is clean after its reversal. Round 2's judgement was correct and its remedy was the right one.

**Round 2's M-N1 arithmetic and source work: reproduces exactly.** 42 / 4 / 38, the endnote's `<note class="endnote" id="iv.iv.x-p5">` location, the Epistle XIV text and its `div3 n="XIV"` container all check out under my own independent run with note spans marked before stripping. Round 2's index re-derivation (247/247) and reciprocity (122/61/0) also reproduce — the 247th cell has since been staled by the fix pass, not by Round 2.

**One correction to Round 2's root-cause account of M-N1.** Round 2 wrote that *"the drafting pass took the wrong one."* The endnote's wording — *"thousands of certificates were given, against the Gospel law"* — appears verbatim in **Round 1's own M2 finding text**, presented there as Cyprian. The drafting pass did not pick the wrong variant out of the corpus; it copied its reviewer. Round 1 also published 38, which is the note-excluded figure, without stating the rule that produced it, so the chunk had a correct number and an incorrect quotation from the same paragraph of the same review. This sharpens rather than softens the finding: index §7's remedy (*"check every quotation against the marked-up source"*) has to apply to quotations arriving from review artifacts too, which is the one path by which this one entered. Neither round is wrong; the causal chain is one link longer than Round 2 drew it.

**Round 1: no finding of it has turned out wrong.** Round 2 re-verified all eight at source and I spot-re-verified H1's premise (the flock's five Registry rows), H2's Doc_03 sentence, H3's fix wording and M2's count. All hold.

**Round 2: no finding of it has turned out wrong.** Its one arguable imprecision is the M-N1 root-cause attribution above, and its scope claim about quotations is being over-read by `Doc_06` rather than overstated by Round 2 itself (**L-R4**).

**On the six carried findings.** Checked only for honest naming, per instruction, not re-litigated. Five of the six are named accurately in `Doc_06` §5 and in the Decision Log — including L-N2, whose "five chunks and the index header" is still exactly right, and L-N3, which correctly records that Round 2 ran the test and the conclusion survived. The sixth, **L-N1, is named dishonestly** — reported as corrected when it is not (**M-R4**). And **none of the six touches what Doc_07 draws on**: I checked each against the five entries `Doc_06` §6 names (*confessor*, *the lapsed*, *reconciliation*, *communion*, *heresy*). M-N3 touches `lpclex017`/`lpclex018`; L-N2 touches `lpclex002`'s Key Sources but not its World Meaning or Ecological Function, which are the sections the affective lens reads; C-N1 touches `lpclex019`. That claim in §5 holds.

---

## Article 19 / Article 28 invention check on the changed material

Every substantive claim in the fifty-five added lines traces to something I located and read. The one new primary-source assertion — the Epistle XIV reading — is verbatim at source, outside every note span, correctly attributed. The 42 / 4 / 38 figures are reproducible to the number. The new cross-reference prose in `lpclex017` and `lpclex019` asserts only what the two entries already establish. The rewritten Round-1 attribution paragraphs in `Doc_06` and index §5 understate rather than overstate what Round 1 did, which is the right direction to err. **Nothing is invented.** The residual defects are all defects of *record* — a stale derived cell, an unreconciled figure, a count stated three ways, and a correction claimed but not made. `lpclex002`'s World Meaning, which is the only participant-facing text this pass touched, is now clean and is the pass's best work.

---

## Is the deliverable adequate to proceed to Doc_07?

**Yes.** Stated plainly, and more plainly than Round 2 could state it, because the thing Round 2 named as the single blocker is verifiably gone.

**What Round 2 said blocked Doc_07 is cleared.** Round 2's block was one site: `lpclex002`'s World Meaning, which `Doc_06` §6 hands to Doc_07's affective lens by name, carrying a bracketed paragraph about a 19th-century editor. A Doc_07 thread reading that section now reads unbroken in-world prose. I verified this across all nineteen World Meanings, not just the one, and all nineteen are clean.

**Nothing in this round's twelve findings touches the five entries Doc_07 is told to use.** H-R1 is a cell in the index's row 17 (*libelli*, Tier 2). M-R1 and M-R4 are attribution and arithmetic in the index's §6 and `Doc_06`'s §1 and Disposition. M-R2 touches `lpclex019` and two `Doc_06` sections. M-R3 is a count. The LOWs are status apparatus, completion lines and gap tracking. `Doc_06` §6's two handoffs — *confessor* / *the lapsed* / *reconciliation* for the affective lens, *communion* / *heresy* for the conceptual lens — rest on entries this round found nothing wrong with, on top of two prior rounds that found nothing wrong with them either.

**What must still land, and how it should be verified.** The HIGH and the four MEDIUMs are documentation-integrity defects and every one is fixable by inspection at a named line. They should be applied before or alongside Doc_07, not after it, for one specific reason: three successive fix passes have now each introduced a fresh defect of their own, and two of the three introduced it *in the act of applying a finding about exactly that failure mode* — Round 1's H3 fix broke the World Meaning rule while fixing an editorial-provenance finding, and this pass staled an index cell while fixing a retrieval-alias finding and claimed a correction it had not made while fixing a finding about claimed verifications. **The next pass should therefore not be self-certified.** The check is mechanical and cheap: regenerate §1 from the nineteen chunks and diff it, and grep `Doc_06` and the index for every remaining "Round 1", "Round 2", "five", "six", "seven", "eighteen" and "42". Both take minutes and both would have caught everything in this review.

**A fourth full round is not warranted.** The content is verified three times over — the tier spine, the tag and tier arithmetic, the reciprocity, the Author-Gravity column, every quotation in the changed material, and the register's mechanical control are all independently confirmed. What remains is a short list of named lines and a re-run of a script.

---

## Escalation assessment (CO-022)

**1. Representative identity, title, or voice — does not apply.** Confirmed independently against all changed material. Nothing in the three rewritten chunks, the index's edited sections or the rewritten `Doc_06` passages makes or implies an identity, title or voice decision. §6's handoff to Doc_07 names lenses and entries.

**2. Portfolio-level or cross-world — three items, unchanged, all correctly carried.** Doc_05 §11 item 11's corpus-wide editorial-apparatus question; Doc_05 §11 item 15's *Boundary Structures* / *Boundary Ecology* inconsistency; and Round 1's M3 (LDF Part III's *Key Texts* versus the L4 template, which I confirmed carries only Key Sources). **This round adds none.** H-R1 is a local derivation failure, not a portfolio question. The register-count confusion at M-R3 is a local instance of item 1, already routed, and I note it rather than adding a fourth — the same call Round 2 made about M-N1.

**3. Governance or methodology — Doc_04's three items, plus the translated-corpus discovery-method item, now correctly filed.** I verified the L-N4 fix landed: `Doc_06`'s Disposition now reads *"open — Doc_04's three items, plus one this document adds and previously failed to file"* and names §5 item 7's finding explicitly. The Decision Log carries it under category 3. That is the fix Round 2 asked for and it is complete. **This round adds no new item.** The pattern noted above — three fix passes, three fresh defects — is a build-thread discipline observation, not a governance or methodology change, and I record it in the adequacy section rather than inflating it into an escalation.

**4. Unresolved tensions — one open, correctly carried.** Doc_04 §7 Open Item 6 (the 411 *Gesta*). Nothing in the changed material relies on it; I checked the three edited chunks and the edited `Doc_06` sections directly. No new unresolved tension: every finding in this review has a named site and a concrete fix, none is a standoff.

**Departure from the build cycle.** Not re-litigated, per instruction. Judged only on whether the record stays honest: `Doc_06`'s Disposition still names the departure plainly, still names the two Doc_05 items it waits on, and the Decision Log's new entry restates it. That record remains honest and complete. **The Status line's failure to move from "REVISED after Round 1" to "REVISED after Rounds 1 and 2" (L-R3) is the only place the record has slipped behind the facts**, and it is a one-line fix.

---

## VERDICT

**REVISION REQUIRED — 1 HIGH · 4 MEDIUM · 5 LOW · 2 COSMETIC (12 new findings).**
**Directed fixes: H-N1 PARTIALLY FIXED · M-N1 PARTIALLY FIXED · M-N2 PARTIALLY FIXED · M-N4 FIXED.**
**Adequate to proceed to Doc_07: yes — Round 2's single named blocker is verifiably cleared, and none of this round's findings touches the five entries Doc_07 is handed. The fix pass should run alongside Doc_07 and must be verified by re-derivation rather than self-certified.**

---

*End of Round 3 review. Simulated review — informational only, not an Article 31 substitute.*
