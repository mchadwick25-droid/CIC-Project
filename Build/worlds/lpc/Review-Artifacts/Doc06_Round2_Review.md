# Doc_06 — Full Interpretive Lexicon Development: Latin Pastoral-Congregational Christianity
## Round 2 Independent Adversarial Review — targeted recheck of the Round 1 fix pass

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-15.

**Scope.** Targeted recheck per `CLAUDE.md` ("from round 2 onward, do a targeted recheck — only what changed, against prior findings"). The unit of review is the diff `54d024b8..4f35c7bc` ("lpc: apply Doc_06 Round 1 findings; add a nineteenth lexicon term") plus every claim that diff makes about the material it did not change. I did not re-review the eleven chunks the fix pass left untouched, except where a changed document makes a claim about them.

**Reviewed:**
- `Doc_06_Full_Lexicon_Development.md` (163 lines, REVISED after Round 1).
- `Lexicon-Chunks/lpclex001`, `002`, `003`, `004`, `005`, `011`, `017`, `018` (changed) and `lpclex019_certificates-letters-of-peace.md` (new) — all nine read in full; the other ten parsed programmatically for front-matter, Related-Terms, Registry-row citations and Author-Gravity markers.
- `Lexicon_Deployment_Index.md` (all eight sections, regenerated and diffed — see below).
- `lpc_Decision_Log.md`, the 2026-09-15 entry.
- `Review-Artifacts/Doc06_Round1_Review.md` (the findings under recheck; treated as a claim set to test, not as authority).

**Read as governing standard, not reviewed:** `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0 (full); `CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx` Parts I–VI (extracted from `word/document.xml`, markup stripped); `CiC_L1_Constitution_V2_2.docx` (extracted in full; Articles 17, 19, 26, 28, 30 located by heading); `Doc_03_Lexicon_Candidate_List.md`; `Doc_05_Ecological_Reconstruction.md` §1.1; `/home/user/cic-project/CLAUDE.md`.

**Vendored source opened directly:** `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (5,728,373 characters; `div1 id="iv" title="Cyprian."` spans byte offsets 2,069,240–4,637,196).

---

### What I did, stated so it can be re-run

**1. Full index re-derivation.** I parsed all nineteen chunk files from disk — Term, Tier, Tags, Aliases, Related-Terms from the fenced front-matter; a regex sweep of each whole chunk body for Registry-row citations; the literal string `Author Gravity note`; the presence of a `## CT Contest Type` heading — and diffed the result cell-by-cell against `Lexicon_Deployment_Index.md` §1. All **19 rows × 13 columns = 247 cells: zero mismatches.** My row parser deliberately handled the failure modes the assignment named — comma runs, the word "and", en-dashes and hyphens as ranges, and rows cited only in prose — then I separately grepped every `\brows?\b` occurrence across all nineteen chunks and read the 50 hits by eye to confirm no range, no "and"-joined pair and no prose-only citation exists anywhere in the corpus that the pattern could have missed. It does not; the corrected generator is not lossy in any other direction I could construct.

**2. Reciprocity, rebuilt from scratch.** I built the directed-edge set from the nineteen Related-Terms fields with a hand-written handle map (not read off the index) and tested `(a,b) ∈ E ⇒ (b,a) ∈ E`. **122 directed edges, 61 reciprocal pairs, zero one-way, zero self-loops, zero unresolvable handles.** §5's arithmetic is right.

**3. Tag and tier tallies, recounted from the chunks.** AS 6 · SC 13 · DR 9 · TC 11 · RT 9 · PV 11 · CT 3; tiers 7 / 12 / 0; Author-Gravity notes 8; `## CT Contest Type` headings 3. Every one matches §2, §3, §4, §6 and Doc_06 §2's stated distribution.

**4. Source verification of the new chunk.** Eight quoted strings from `lpclex019` were located in the markup-stripped Cyprian `div1` and character-compared; each occurs exactly once. The **42** count was re-run under the chunk's own stated rule (case-insensitive `certificates?`, markup stripped, scoped to `div1 id="iv"`): **42, exactly.** I then classified all 42 occurrences by referent from their surrounding context, and separately mapped each to whether it falls inside a `<note>` element.

**5. World Meaning sweep, all nineteen.** Every `## World Meaning` section extracted and swept for analytical-distance markers and for bracketed builder matter.

---

### A failing check I confirmed before reporting it

My first pass at the "42 occurrences" claim looked like a contradiction of Round 1, which reported **38**. Before treating either as wrong I mapped every occurrence to its enclosing element and found the whole of the difference: **42 total in the `div1`, of which exactly 4 sit inside `<note>` elements** — 19th-century editorial apparatus — leaving **38 in Cyprian's own printed text.** Neither figure is an error. Round 1 applied the scope this build applies everywhere else (the *plebs* finding at `lpclex010` turns on precisely this exclusion); the fix pass applied a looser one and stated it. So my check did not fail, and neither document is wrong about arithmetic — but the divergence itself is unreconciled on the record, and one of those four editorial occurrences is quoted in the new chunk as Cyprian. That is **M-N1** below. Recorded per the assignment's instruction rather than discarded.

---

## VERDICT: REVISION REQUIRED

**New findings: 1 HIGH · 4 MEDIUM · 4 LOW · 1 COSMETIC — 10 in total.** (Two further pre-existing defects are noted separately and excluded from the count, because the fix pass did not cause them.)

**Round 1's eight findings: 7 FIXED · 1 FIXED WRONGLY.** No Round 1 finding was wrong or overstated; all eight verify at source.

**What holds up, and it is most of it.** The index is now genuinely diffable: 247 of 247 cells re-derive exactly, and the H1 root cause was fixed at the generator rather than patched at the cell — the worked proof at row 01 (`Rows 1, 2, 3, 5, 19`) is real. Reciprocity survives the nineteenth term intact at 122/61/0. Every tag count, every tier count and every Author-Gravity cell recomputes. The nineteenth term is tiered defensibly, its eight quotations are verbatim, the 42-count reproduces to the character under its own stated rule, the two-referent claim is true (I classified all 42: roughly 23 Decian sacrifice-certificate, 19 confessors' letter of peace), and the new chunk does **not** conflate them — its `Do-Not-Retrieve-When` names the distinction explicitly and routes the other referent to `libelli`. The scope note is honoured: `Doc_03_Lexicon_Candidate_List.md` is not in the diff. `lpclex018`'s World Meaning is **not** invention and does not smuggle the editor's classification back: graduated treatment of certificate-holders versus sacrificers is Cyprian's own, in his own words (*"Neither must you think… that those who receive certificates are to be put on a par with those who have sacrificed"*; *"it was decided… that the receivers of certificates should in the meantime be admitted, that those who had sacrificed should be assisted at death"*), and the general grant of peace that makes "the road ends inside" true is Epistle LIII's. I checked that expecting to find the defect the assignment pointed me at, and it is not there.

**What does not.** The H3 fix put the disclosure in the one section of the one chunk where it does the most damage — inside a **Tier 1 World Meaning**, in square brackets, in flat etic register, with a raw filename cross-reference — contradicting Round 1's own stated fix site, the L4 template's World Meaning rule, that chunk's own Final Assembly Instruction, and LDF Part VI's self-containment rule. The new chunk's Key Sources quotes a 19th-century editorial endnote and presents it as Cyprian's correspondence, in a deliverable whose central discipline is keeping that apparatus out. And Doc_06 now credits Round 1 with four verifications Round 1 did not and could not have run, on material that did not exist when Round 1 ran — the world's own Decision Log states the same facts correctly, so the deliverable disagrees with its own log.

---

## Status of Round 1's eight findings

| # | Finding | Status | Evidence |
|---|---|---|---|
| **H1** | Lossy index generator — row 01 printed `Rows 1, 19` for a chunk citing 1, 2, 3, 5, 19 | **FIXED** | Row 01 now reads `Rows 1, 2, 3, 5, 19`. Full re-derivation: 247/247 cells match. Fixed at the generator (index header states the pattern change), not hand-patched — and I confirmed no range, "and"-joined or prose-only row citation exists in any of the nineteen chunks that a corrected pattern could still drop. |
| **H2** | Unjustified `[PV]` on *suffrage* | **FIXED** | `lpclex011` Tags now `AS` alone. Index §1 row 11 PV cell is `–`; §3's PV list (11 terms) does not contain suffrage; §8 records the correction. Doc_03's governing sentence re-verified at source (`Doc_03` line 19): *"it does not sit on 'suffrage,' which is a cross-phase pattern rather than a single-phase term."* |
| **H3** | Editorial classification narrated as fact in `lpclex002`'s Tier 1 World Meaning | **FIXED WRONGLY** | Both required components landed — a disclosure in `lpclex002`, and a sixth row in index §7. But the disclosure was placed **inside World Meaning** as a bracketed etic paragraph, not in Key Sources or the Author Gravity note as Round 1 specified. See **H-N1**. |
| **M1** | Tier 3 entries carrying a forbidden Key Sources section | **FIXED** | `lpclex017` and `lpclex018` both `Tier: 2`; index §1, §2 and Doc_06 §2.3 all agree; LDF Part III's remedy sentence is quoted accurately (*"A Tier 3 entry that begins to require these should be reclassified to Tier 2 rather than expanded in place"*) and the reclassification is the textually supported reading of it. World Meaning and Ecological Function supplied per "structure should not fragment." Two consequential defects in the new sections: **M-N3**, **L-N3**. |
| **M2** | Missing *letters of peace* term | **FIXED** | `lpclex019_certificates-letters-of-peace.md`, Tier 2, tagged SC/TC/DR/RT/PV, six reciprocal Related-Terms edges, eight quotations verbatim at source, 42-count reproducible to the character. Doc_03 untouched — scope note honoured, confirmed against the diff's file list. One provenance defect: **M-N1**. |
| **M3** | LDF Part III "Key Texts" vs. L4 template mismatch | **FIXED** | Round 1's fix was "route it, do not act on it." Doc_06 §5 item 8 records it; the Disposition's CO-022 category 2 now names three portfolio items; the Decision Log carries it. LDF Part III's Tier 1 list re-verified at source: *"Key Texts — primary textual evidence, where applicable / Key Sources — primary historical voices or texts substantively informing this entry's reconstruction"* — two sections, and the template has one. |
| **L1** | "already Tier 2 candidates in Doc_03" overstated Doc_03 | **FIXED** | The phrase is gone. §2.3 now reads *"were drafted at Tier 3 on attestation rather than importance."* Doc_03's Disposition claim (*"assigns no final tier classification of its own"*) is no longer contradicted. |
| **L2** | §1's "one disclosed exception" read backwards | **FIXED** | §1 now separates the two cases cleanly: one term added at §2.4, a second flagged-not-added at §5 item 3. |

**Was Round 1 right?** Yes, on all eight. I re-verified H2's Doc_03 sentence, H3's Doc_05 §1.1 disclosure, M1's two governing texts, M2's absence, M3's LDF/template divergence and L1's Doc_03 Disposition directly at source rather than through Round 1's account of them. Every one reproduces. Round 1's one arguable imprecision — reporting 38 where the corpus holds 42 under a looser scope — turns out to be Round 1 applying this build's *own* editorial-exclusion rule correctly; see **M-N1**.

---

## NEW — HIGH

### H-N1 — The H3 fix moved an editorial disclosure *into* a Tier 1 World Meaning, in brackets, with a filename cross-reference — breaking three rules at once and falsifying the chunk's own completion statement

**Site:** `Lexicon-Chunks/lpclex002_the-lapsed.md`, `## World Meaning`, second paragraph, added at `4f35c7bc`:

> `[**Provenance of the two-way distinction, marked here rather than left to the reader:** the clean split between those who sacrificed and those who only bought the paper reaches this record as the vendored edition's own **19th-century editorial endnote**, attached to a different, Confidence-C text, and not as Cyprian's own classification in *De Lapsis*.` `lpclex018` `carries the disclosure in full. What *is* Cyprian's own, and what this passage rests on, is the refusal to let either group's failure be final.]`

**What I found.** I extracted all nineteen `## World Meaning` sections and swept them for analytical-distance markers and bracketed matter. **Eighteen are clean. `lpclex002` is the sole hit**, and every hit in it is inside the paragraph the fix pass added: `reaches this record`, `editorial`, `19th-century`, `Confidence-C`, `vendored`, `lpclex018`, plus the enclosing square brackets. Before `4f35c7bc` this section was clean; the fix pass created the defect.

Four separate rules are broken at this one site:

1. **The L4 template's World Meaning instruction**, verbatim: *"Check before saving: no analytical-distance markers in this section… The World Meaning should read as if it comes from someone who knows this term from the inside, rendered accessible for someone who does not."* Its Final Assembly step 3 lists the markers to remove. "Reaches this record as the vendored edition's own 19th-century editorial endnote" is maximal analytical distance — it is a sentence about the *edition*, inside the section reserved for the world's own voice.
2. **The template's Final Assembly step 1** ("Replace all [BRACKETS] with world-specific content") — and the chunk's own closing line, unchanged, still asserts **"No brackets or builder notes remain."** That statement is now false of the file it appears in.
3. **LDF Part VI**, verbatim: *"Each chunk is self-contained. A reader of any single chunk should have everything they need for that term without consulting other chunks, except through the Related Terms cross-references which name (not embed) the related entries."* The inserted paragraph tells the reader that `lpclex018` "carries the disclosure in full" — a raw filename, in a content section, telling a self-contained runtime unit that it is not self-contained.
4. **Round 1's own stated fix**, which the fix pass records as applied: *"one sentence in `lpclex002`'s Key Sources or Author Gravity note."* Neither site was used.

**Why this matters.** `lpclex002` is Tier 1 and `[RT]`-tagged — LDF Part V's runtime priority set. Under Article 30's Three-Level Transparency, World Meaning *is* Level 2: it is what a participant receives when they ask about the term mid-encounter. A participant asking "what were the lapsed?" would receive a bracketed paragraph about a 19th-century American editor's endnote and a Confidence grade, in the middle of the world's own voice. Against `CLAUDE.md`'s participant-facing bar this is the textbook case of an AI tell and disclaimer-as-crutch. And Doc_06 §6 hands *the lapsed* to Doc_07's affective lens specifically — Round 1 flagged that this one entry's fix should land before Doc_07 draws on it. It has not landed correctly.

**Fix.** Delete the bracketed paragraph from World Meaning. Restore the World Meaning to unbracketed in-world prose; if the sentence *"Some of them went up and burned the incense; some never went near the altar but bought a paper saying they had"* is to keep the editorial caveat, put the caveat where Round 1 said and where `lpclex018` already puts its own — in Key Sources or the Author Gravity note — and phrase it without a filename. Index §7's sixth row and the Doc_06 §5 item 6 register entry stay; only the placement is wrong. Do not stack a second bracket on top of the first — remove and redo, per `CLAUDE.md`'s "no fix on a fix."

---

## NEW — MEDIUM

### M-N1 — `lpclex019` quotes a 19th-century editorial endnote and presents it as Cyprian's own correspondence; four of its 42 counted occurrences are editorial and none of this is disclosed

**Site:** `Lexicon-Chunks/lpclex019_certificates-letters-of-peace.md`, `## Key Sources`, the third quoted string: *"thousands of certificates were given, against the Gospel law, I wrote letters in which I recalled by my advice as much as possible the martyrs and confessors to the Lord's commands"* — attributed to *"Cyprian's own crisis correspondence, Registry row 1 (Confidence A), where the whole argument is conducted"*, with the section closing *"All quoted here are re-verified at source in `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`, scoped to Cyprian's own `div1` span."*

**What I found.** That string occurs exactly once in the volume, and it is inside `<note anchored="yes" id="iv.iv.x-p4.4" n="2219" place="end">` — an editorial endnote hanging off the *Argument* heading prefixed to Epistle X (`div3 id="iv.iv.x"`). It is not Cyprian's printed text. Cyprian's own text of the same sentence is printed later in the volume, in Epistle XIV (`div3 id="iv.iv.xiv"`), and reads differently:

> *"thousands of certificates were **daily** given, **contrary to the law of the Gospel**, I wrote letters in which I recalled by my advice, **as much as possible,** the martyrs and confessors to the Lord's commands."*

So the chunk quotes the apparatus's older rendering in preference to the volume's own translation of the same passage, and labels the result re-verified Cyprian. "Scoped to Cyprian's own `div1` span" is true and is not the same thing as Cyprian's own words — this build established that distinction itself, at `lpclex010`, where the *plebs* finding turns on exactly it.

Separately: of the **42** occurrences the Attestation paragraph counts, **4 fall inside `<note>` elements** — one each in Epistle X (the Argument endnote quoted above), Epistle XII, Epistle XIII (Rigaltius's gloss on *faciunt invidiam*) and Treatise III (*De Lapsis*). **38 sit in Cyprian's own printed text** — which is exactly the figure Round 1 reported. Neither Doc_06 §2.4, nor §5 item 7, nor the chunk, nor the Decision Log notes that Round 1 published 38, or why the figures differ. `Lexicon_Deployment_Index.md` §7's Editorial-Apparatus Register lists six entries and `lpclex019` is not among them, although it is now the only chunk in the lexicon that quotes an endnote as primary text.

**Why this matters.** Constitution Article 28's Anti-Fabrication Prohibition is explicit that the standard is not general accuracy: *"it requires that every source cited be genuine, identifiable, and accurately represented."* An editor's rendering represented as the author's correspondence fails "accurately represented," even where the substance is the author's. This is also the same failure class as H3, one fix pass later, in the chunk added to close M2. And `CLAUDE.md` is direct that two documents disagreeing is a finding to log, not to quietly reconcile — Round 1's 38 was silently superseded by 42 with no note anywhere.

**Fix.** Three things, none large. (a) Replace the quoted string with Epistle XIV's own text, cited as Epistle XIV, and keep the short phrase *"thousands of certificates"* which is genuinely Cyprian's in both. (b) State the count as **38 in Cyprian's own text, 4 in editorial notes, 42 in the `div1` span**, and say which rule Round 1 used — that reconciles the two figures instead of overwriting one. (c) Either add `lpclex019` to index §7 as a seventh register row, or state in its Key Sources that the four note-occurrences are excluded from what the entry rests on.

---

### M-N2 — Doc_06 and the index credit Round 1 with four verifications Round 1 did not run, on material that did not exist when it ran — and the world's own Decision Log states the same facts correctly

**Sites:** `Doc_06_Full_Lexicon_Development.md` **Status** (line 20) and **Disposition** (line 158); `Lexicon_Deployment_Index.md` §5 (line 110) and §6 (line 129).

**What I found.** Doc_06's Status: *"Round 1 also confirmed zero misquotations, full Related-Terms reciprocity, all three CT contest types genuinely completed, **no analytical-distance markers across nineteen World Meanings**, and an Author-Gravity column matching every chunk."* Doc_06's Disposition: *"zero misquotations against the vendored sources; **122 links across nineteen entries** with zero one-way… and **every** Author-Gravity cell matching its chunk."*

Round 1 ran against **eighteen** chunks. It reported **110 directed edges / 55 reciprocal pairs**, not 122/61. It checked eighteen World Meanings, not nineteen — and the nineteenth-era edit to `lpclex002` has since broken that very check (H-N1). It verified **7 "Yes" and 11 "No"** Author-Gravity cells over eighteen rows; there are now 8 and 11 over nineteen, and `lpclex019`'s cell has never been independently checked. And Round 1 did not claim zero misquotations outright — its own words are *"a substantial majority, spot-checked across all seven Tier 1 entries and four of nine Tier 2 entries."* The index repeats two of these: §5 says the 122-link figure was *"independently re-verified by Round 1"*, §6 says *"Round 1 verified every Yes and every No."*

The `lpc_Decision_Log.md` entry for this same fix pass gets it right: *"No analytical-distance markers across **eighteen** World Meanings."* So the deliverable contradicts its own log, in the same commit.

**Why this matters.** `CLAUDE.md`: *"A blocking review finding can't be dismissed by self-certification — it needs independent re-confirmation."* Dressing new, unreviewed material in a prior review's verification is self-certification with a citation attached, which is worse than none — a Round 3 reader, or a Doc_07 thread, would reasonably skip re-checking the new chunk on the strength of it. The figures themselves are all correct on my own re-derivation (122/61/0, 8 Author-Gravity notes); it is the attribution that is false.

**Fix.** Rewrite both passages to say what Round 1 actually verified, over eighteen chunks, and state separately and in its own voice what the fix pass re-derived over nineteen. The Decision Log's wording is the model.

---

### M-N3 — `lpclex017` and `lpclex018`'s new World Meaning and Ecological Function sections rest on Cyprian's Epistles and cite nothing; and `lpclex017`'s standing evidentiary claim is contradicted by this very fix pass

**Sites:** `Lexicon-Chunks/lpclex017_libelli.md` (`## World Meaning`, `## Ecological Function`, `## Key Sources`) and `lpclex018_libellatici-sacrificati.md` (same three sections).

**What I found.** Both new World Meanings make specific, substantive historical claims, and both are **true** — I traced every one:

- `lpclex017`: *"A demand you could satisfy with money rather than incense"* — attested in Cyprian's own words, Epistle LI, in the certificate-holder's reported defence: *"I pay a price for this purpose, that I may not do what is not lawful for me to do"*, and *"although his hand is pure, and no contact of deadly food has polluted his lips, yet his conscience is nevertheless polluted."*
- `lpclex018`: *"the road back is longer for one than the other"* — Epistle LI again: *"Neither must you think… that those who receive certificates are to be put on a par with those who have sacrificed"*, and *"the receivers of certificates should in the meantime be admitted, that those who had sacrificed should be assisted at death."* *"What does not change is where the road ends"* — Epistle LIII, the synod's general grant of peace to the lapsed.

So this is **not invention**, and `lpclex018` has not smuggled the editorial classification back in: it says so itself (*"the World Meaning above is written to the substance of graduated penance, which Cyprian's own correspondence does attest, rather than to the editor's labels"*), and that statement checks out. The defect is that **neither chunk cites any of it.** `lpclex018`'s Key Sources still names only Registry row 8 — the Confidence-C anonymous treatise whose endnote the entry disclaims — and `lpclex017`'s names row 8 plus Doc_01's gloss. Neither names row 1. The index's Source Registry Cross-Reference cells therefore read `Rows 8` for both, correctly derived and now materially under-reporting each entry's real evidentiary base. That is the same shape of defect as H1, with the chunk rather than the index as the under-reporter.

Worse, `lpclex017`'s Key Sources still closes: *"The term is carried here as supporting reference vocabulary for the lapsed, **on Doc_01's gloss rather than on attestation in this world's own primary text.**"* The Latin headword's absence is true and I re-verified it. But this same fix pass established, at `lpclex019`, that the translation names this exact referent roughly **23 times** using the word "certificate" — which is in `lpclex017`'s own Aliases list. The entry now denies an attestation the deliverable proves two files away. Doc_06 §5 item 7 draws the general lesson (*"a headword sweep in the original language cannot find a term the surviving corpus only ever names in translation"*) and then does not apply it to the entry the lesson came from.

**Why this matters.** Article 28 requires that where a claim is the builder's own inference or synthesis it be marked as such; here the claims are neither marked nor sourced, which leaves a reader unable to tell inference from evidence. And a deployment chunk whose Ecological Function now asserts that this term *"is the reason reconciliation is a process with stages rather than a single yes or no"* is load-bearing, while its Key Sources still calls it *"the lowest-attested item in this lexicon… carried for recognizability."* Those two sentences, in the same file, are not compatible.

**Fix.** Add Registry row 1 to both entries' Key Sources with the specific Epistles (LI for the graduated treatment and the price-paying defence; LIII for the final grant of peace), quoted or cited, and re-run the index generator so the cross-reference cells read `Rows 1, 8`. In `lpclex017`, replace *"rather than on attestation in this world's own primary text"* with the accurate statement: the **Latin headword** is absent; the referent is attested in the translation's own word, which `lpclex019` counts. In `lpclex018`, reconcile "lowest-attested item, carried for recognizability" with an Ecological Function that makes it structural — one of the two has to give.

---

### M-N4 — Adding `lpclex019` created a retrieval collision with `lpclex017` that only one of the two chunks defends against

**Sites:** `lpclex017_libelli.md` and `lpclex019_certificates-letters-of-peace.md`, Aliases / Retrieve-When / Do-Not-Retrieve-When.

**What I found.** Both chunks list the bare alias **`certificate`**. Both claim the same trigger: `lpclex017` — *"participant asks what a certificate was, or how someone could lapse without sacrificing"*; `lpclex019` — *"participant asks what a certificate was in this world."* `lpclex019` defends the boundary properly: *"Do-Not-Retrieve-When: the participant is asking about the Decian sacrifice-certificate that made someone lapsed in the first place — that is a different document travelling in the opposite direction; see libelli."* `lpclex017`'s Do-Not-Retrieve-When was **not** updated and still reads only *"the participant is asking about the category of persons rather than the document — that is the lapsed."* It says nothing about the letters of peace.

So the disambiguation runs one way. On the plain question *"what was a certificate?"* the retrieval layer has two chunks claiming the trigger, one of which will answer with the Decian sacrifice-certificate as though it were the only referent — which is precisely the confusion Doc_06 §2.4 identifies as the whole reason the term was added (*"the two documents travel in opposite directions"*).

**Why this matters.** LDF Part VI defines Do-Not-Retrieve-When as *"conditions under which surfacing this chunk would be inappropriate or confusing"*, and this is the clearest such condition in the lexicon. The new term closes a vocabulary gap and opens a retrieval one.

**Fix.** Add the reciprocal exclusion to `lpclex017`'s Do-Not-Retrieve-When (pointing to `certificates` for the confessors' letters of peace), and narrow the shared bare alias — `lpclex017` should carry `sacrifice-certificate` / `certificate of compliance`, `lpclex019` should carry `letter of peace` / `libellus pacis`, with the unqualified word either dropped from one or explicitly shared and disambiguated in both Retrieve-When lines.

---

## NEW — LOW

### L-N1 — Doc_06's own arithmetic and cross-references were not carried through the edit

Three places in `Doc_06_Full_Lexicon_Development.md` still describe the pre-fix deliverable:

- **§1, "Does" paragraph (line 26):** *"**eighteen** self-contained deployment chunks written to the L4 template"* — there are nineteen. The adjacent "Does not" paragraph was rewritten; this one was not.
- **Disposition (line 160):** *"Doc_05 §11 item 11's corpus-wide editorial-apparatus question, of which **§5 item 6 above registers five local instances**"* — §5 item 6 (line 123), rewritten in the same commit, says **six**, twice. The document contradicts itself two sections apart.
- **§5 item 6 (line 123):** *"this document registers the six local instances and **excludes all six**."* The sixth is not excluded: `lpclex002` narrates the distinction and then marks it, which the index §7 row and the chunk's own correction note both say explicitly (*"Marked in place above rather than rewritten away"*).

**Fix.** "nineteen"; "six"; and "excludes five and marks the sixth in place."

### L-N2 — Review-round process narration is now embedded in five deployment chunks and the index header

`lpclex002` (`**[CORRECTION, 2026-09-15 — Round 1's H3.]**`), `lpclex011` (`**Tag correction, 2026-09-15 — Round 1's H2.**`), `lpclex017` and `lpclex018` (`**Tier corrected 2026-09-15 — Round 1's M1…**`), `lpclex019` (a Discovery note citing `Doc06_Round1_Review.md` by filename), and `Lexicon_Deployment_Index.md`'s header (`**[CORRECTION, 2026-09-15 — Round 1's H1.]**`) all now carry round-by-round change history inside the build output. Every one of these facts is already recorded, at greater length and more accurately, in `lpc_Decision_Log.md`'s 2026-09-15 entry and Doc_06's Document Log — which is where `CLAUDE.md` places them: *"Notes, decision logs, audit trails, adversarial-review rounds… belong in `Ministry/` … never inline."* Deployment chunks are runtime retrieval units under LDF Part VI, not a changelog surface; a participant reaching Level 3 on *suffrage* should not be reading about a tag that was removed at a review round.

This world's own standing rule, stated in `Doc_03`'s Status line, already says the same thing: *"this world's own standing rule that a build document states the current, corrected text and lets the Decision Log and Review-Artifacts carry the record of what it once said and who fixed it."* The fix pass departed from it in six files without saying so.

**Fix.** Strip the correction notes from the five chunks and the index header; the Decision Log entry already carries all of it. Retain the substantive content in `lpclex017`/`lpclex018`'s Final Assembly Instructions (the LDF Part III reasoning for Tier 2) but as a statement of what the entry *is*, not of what it was corrected from.

### L-N3 — "A lexicon with no Tier 3 entries is a result, not a gap" is asserted rather than tested, on a premise Doc_03 does not support

**Sites:** `Doc_06` §2.3 (line 65); `Lexicon_Deployment_Index.md` §2 (line 72); the Decision Log's M1 paragraph — the same sentence in all three.

The claim's stated ground is: *"Doc_03's candidates were generated from gravity-bearing vocabulary, and nothing on that list turned out to be peripheral enough to sit at reference depth."* Doc_03 does not describe itself that way. Its own account is *"every term below is drawn from the Registry's own **Native** entries specifically, per Step 3's own instruction to work from the Registry rather than from Doc_02's raw ecology narrative directly."* It organises its sections against Doc_01 §3's *candidate* gravities, which is not the same thing — and LDF Part I places Doc_03 at Step 3, **before** Gravity Discovery at Step 4, so candidates could not have been generated from confirmed gravity-bearing vocabulary. The premise is loose in the same way Round 1's L1 was loose.

More substantially, the conclusion is stated, not derived. LDF Part III defines Tier 3 as *"low distortion risk, limited technical weight, and minimal ecological centrality"*; no section of Doc_06 or the index tests the twelve Tier 2 entries against that definition. I ran the test myself and the claim survives it — the one entry whose tag profile superficially matches (`lpclex011` *suffrage*, tagged `AS` alone: no DR, no TC, no RT) turns out to be mis-tagged rather than peripheral, per the pre-existing note below. So I am **not** finding that an entry belongs at Tier 3. I am finding that the deliverable asserts a conclusion it did not test, in three places, on a premise its own upstream document contradicts.

**Fix.** Replace the premise with what Doc_03 actually says, and either show the test (one sentence against Part III's three-part Tier 3 definition) or soften the claim to what is defensible: no candidate on the list carries low distortion risk *and* limited technical weight *and* minimal ecological centrality together.

### L-N4 — Doc_06's CO-022 assessment files the discovery-method finding nowhere, while its own Decision Log half-recognises it

`Doc_06`'s Disposition states *"Governance or methodology: **open, unchanged** — Doc_04's three items; this document adds none."* But §5 item 7, added by this pass, records that Doc_03's headword-sweep discovery method cannot find a term the corpus names only in translation — and then says *"every other frequency-based discovery judgement in Doc_03 rests on the same method."* This world's corpus is a 19th-century English translation throughout, and so are several others in the portfolio. That is a methodology finding about LDF Part I's candidate-discovery adequacy, not a note. The Decision Log gets closer, calling it *"A fourth… flagged as a method question rather than an item"*, but Doc_06's Disposition drops even that qualification.

**Fix.** File §5 item 7 under CO-022 category 3 (governance or methodology), alongside Doc_04's three, or under category 2 as a fourth portfolio item. It should not sit outside the four categories while being described as affecting every frequency-based judgement in an upstream Approved-to-proceed document.

---

## NEW — COSMETIC

### C-N1 — Two quotations in `lpclex019`'s World Meaning are silently recapitalised

*"Designate by name in the certificate those whom you yourselves see…"* — the source reads *"I beg you that you will designate by name in the certificate…"*. *"Certificates are so given to some as that it is said…"* — the source reads *"For I hear that certificates are so given to some…"*. Both are set in italic as quotations, with no ellipsis or bracket marking the truncation and the changed initial capital. The remaining text of both is verbatim, and both are quoted correctly, lowercase and with an ellipsis, in the same chunk's Key Sources and in Doc_06 §2.4 — so the chunk contradicts itself on its own quotation convention. Given this build's demonstrated care elsewhere (Round 1 confirmed it reproduces an awkward half-bracketed editorial insertion exactly rather than smoothing it), the inconsistency is worth one minute to fix: lowercase the initial letters and mark the truncation.

---

## Noted, pre-existing — not caused by this fix pass, excluded from the counts

These two are real and I record them rather than let them go quiet, but the fix pass did not introduce either and neither should weigh on this gate.

- **`lpclex011` *suffrage* carries no `[DR]` tag** although Doc_06 §4 names it as one of the two sharpest instances of distortion shape 2 (*"Suffrage does the same — a franchise, where this world has acclamation without procedure"*) and the chunk's own Distortion Risk pairing is a textbook DR case (*"A modern participant will hear 'suffrage' as the right to vote, and expect a franchise, a ballot and a procedure"*). Round 1's By-Tag check verified that the index matches the chunks, which it does; it did not test whether the tags are right. The fix pass edited this Tags line (removing `[PV]`) without noticing. This is also what makes the zero-Tier-3 claim in L-N3 look untested when it is in fact sound.
- **This world has no `Open_Gaps_Tracking.md`**, although `CLAUDE.md` requires that *"every known gap, open question, or review outcome belongs in that world's `Open_Gaps_Tracking.md` — never left to live only in a conversation thread."* This pass created two new open items (§5 items 7 and 8) with nowhere numbered to put them. The file exists in only 3 of the 12 worlds under `World-Builds/`, so this is a fleet-level gap rather than this deliverable's, and belongs to the project lead rather than to a build thread.

---

## Article 19 / Article 28 invention check on the changed material

Every substantive historical claim in the ~230 added lines traces to a source I located and read. `lpclex019`'s eight quotations are verbatim and its 42-count reproduces exactly. `lpclex017`'s and `lpclex018`'s new World Meanings and Ecological Functions are traceable to Cyprian's Epistles LI and LIII, which I read at source — **nothing is invented**, including the claim the assignment pointed me at as the likely invention (`lpclex018`'s graduated penance), which is Cyprian's own and not the editor's. The two failures are of *representation*, not of fabrication: an editorial endnote presented as Cyprian's correspondence (M-N1), and true claims presented without the citation that would let a reader distinguish evidence from inference (M-N3). Both are Article 28 "accurately represented" failures rather than Article 19 invention. The one genuinely new fabrication-adjacent risk is H-N1, and it is a placement error, not a content error: the disclosure is correct, it is simply in the section reserved for the world's own voice.

---

## Is the deliverable adequate to proceed to Doc_07?

**Not as it stands — and the gap is two sites wide, not a round of rework.** I am stating this as a settled condition rather than deferring it, per the assignment.

**What blocks Doc_07 specifically.** One thing, and it is H-N1. Doc_06 §6 hands *confessor*, *the lapsed* and *reconciliation* to Doc_07's affective lens by name. *The lapsed* is the chunk whose World Meaning now carries a bracketed paragraph about a 19th-century editor. A Doc_07 thread reading that section for affective content reads editorial apparatus in the middle of it. Round 1 anticipated exactly this and said the `lpclex002` fix "should land before Doc_07 draws on it." It has not.

**What must land with it but does not block Doc_07.** M-N1, because a quotation attributed to Cyprian is the editor's, and the deliverable's own register does not know about it; and M-N2, because the record currently claims a verification that was not performed, which would let the next gate skip a check it should run.

**What does not need to wait.** M-N3, M-N4 and all four LOWs are real and should be fixed, but none of them touches the seven Tier 1 entries, the gravity spine, the tier distribution, the CT tagging or the conceptual pairing Doc_07 is told to use. Doc_06 §6's two handoffs are sound advice and I found nothing wrong with the reasoning behind either.

**So:** fix H-N1, M-N1 and M-N2 at their three named sites; verify those three sites and nothing else; then proceed to Doc_07 and carry M-N3, M-N4 and the LOWs into the same pass or the next. A third full review round is not warranted and would not be a good use of the budget — the index derivation, the reciprocity, the tag and tier arithmetic and every quotation but one are independently confirmed clean, and the remaining work is checkable by inspection at named line numbers.

---

## Escalation assessment (CO-022)

**1. Representative identity, title, or voice — does not apply.** Confirmed independently against all changed material. Nothing in the new chunk, the two rewritten chunks, the regenerated index or the rewritten Doc_06 sections makes or implies an identity, title or voice decision. §6's handoff to Doc_07 names lenses and entries.

**2. Portfolio-level or cross-world — three items carried, correctly, plus one fresh instance.** Doc_05 §11 item 11's corpus-wide editorial-apparatus question; Doc_05 §11 item 15's *Boundary Structures* / *Boundary Ecology* inconsistency; and Round 1's M3 (LDF Part III's "Key Texts" versus the L4 template), newly and correctly added by this pass and traced by me to both governing texts. **M-N1 is a fresh local instance of the first**, and I note it rather than adding a fourth item — the corpus-wide question is already routed and the register is already known to be incomplete.

**3. Governance or methodology — Doc_06 says it adds none, and that is wrong.** §5 item 7's discovery-method finding — that a Latin-headword sweep cannot find a term a translated corpus names only in English, and that *"every other frequency-based discovery judgement in Doc_03 rests on the same method"* — is a methodology item bearing on LDF Part I across every world whose corpus is a translation. It is currently filed nowhere. See **L-N4**. This review routes it to the project lead in this category.

**4. Unresolved tensions — one open, correctly carried.** Doc_04 §7 Open Item 6 (the 411 *Gesta*). I confirmed nothing in the nineteenth chunk or the two rewritten chunks relies on it. No new unresolved tension: every finding in this review has a named site and a concrete fix, none is a standoff.

**Departure from the build cycle.** Not re-litigated, per instruction. Judged only on whether the record is honest and complete: Doc_06's Disposition names the departure plainly, names the two Doc_05 items it waits on, names which thread cannot dispose of what and why, and the Decision Log carries the same account at greater length. **The record of the departure is honest and complete.** The nineteenth term's addition is likewise recorded plainly, attributed to the project lead's direction of 2026-09-15, with the reason stated and the Doc_03 scope note honoured in fact as well as in text.

---

*End of Round 2 review. Simulated review — informational only, not an Article 31 substitute.*
