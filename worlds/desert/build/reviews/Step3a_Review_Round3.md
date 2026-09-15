# Step 3a Lexicon — Review Round 3

**Reviewer:** independent, adversarial; no part in the draft, Round 1, or Round 2. **Under review:** the 18 term records in `records/desert/term/` and `worlds/desert/build/LEXICON-INDEX.md` at commit `9cbd26e6` ("desert step 3a, review round 2: fix illusory-fix instance + factual overclaim + unverified quote"), branch `world/desert`. **Ground truth used:** the vendored texts in `cic/texts/` (`npnf202`, `npnf204`, `npnf211`, `palladius_lausiac-history_clarke1918.txt`, `webbe_world-english-bible-british-edition.xml`), `worlds/desert/CiC_W3_Doc06_Full_Lexicon.md`, the step-2 source records in `records/desert/source/`, `records/_fleet/canon_question/`, and `engine/m1/gates.py`.

**Method, stated so it can be audited:** all 72 sense fields (18 records × 4 registers) were extracted programmatically, counted (exactly 72, exactly 4 per record — no field silently absent), read in full by hand, and then swept a second time against six explicit jargon families (corpus/build self-reference; vendor/licensing; verification-process; record-schema; risk-marker; CiC-reserved vocabulary) rather than against the specific strings Rounds 1 and 2 had named. Both full diffs (`b7d20aa0→184747bc` and `184747bc→9cbd26e6`) were read line by line. Every quoted string in every field was extracted and checked. Every `sources[].locus` line-pointer was opened in the vendored file and the passage compared **against what the record says the passage shows**, not merely against the quoted words. The reciprocity graph and the index table were re-derived from the records mechanically. The gate battery was run.

---

## A. The jargon pattern — the question this round exists to answer

**Is the build-infrastructure/corpus-management vocabulary pattern in the `senses` fields NOW exhaustively clear? NO.**

**Five instances remain, in four records.** Three are pre-existing and were missed by *both* prior rounds' claimed exhaustive sweeps. One was **introduced by Round 2's own fix** — meaning the illusory-fix signature has now recurred in three consecutive rounds, on the same field of the record set, each time caught only by the next round.

### J1 — SUBSTANTIAL. `desert.term.nepsis.md:39` (evidential): "one-author concentration **flag**."

"Flag" is this build's own risk-marker vocabulary (Doc_06 §1.9's "[PV] flag:"; the index's own Author-gravity column literally reads "flagged"). In-world there is no flag; there is a fact.

### J2 — SUBSTANTIAL. `desert.term.xeniteia.md:34` (evidential): "the compiler screen on the sayings collections applies here as everywhere."

### J3 — SUBSTANTIAL. `desert.term.penthos.md:34` (evidential): "(compiler screen applies)."

"Compiler screen" is this build's own source-criticism apparatus label (from the step-2 source records), not carried from Doc_06. `desert.term.apophthegma.md`'s evidential sense states the identical caution entirely in-world and is the model to match.

### J4 — SUBSTANTIAL, illusory-fix signature recurring a third time. `desert.term.theoria.md:35` (evidential): "it is checked directly against what the wider movement's own sources do and do not say."

Round 2 itself flagged the prior wording ("a tested finding, not an impression") as borderline review-process vocabulary and left it; its own rewrite then made the review-process framing *explicit* — a stronger member of the same family, in the same field, in the same revision.

### J5 — weakest, listed for completeness. `desert.term.koinonia.md:43` (evidential): "Every rule-content claim names which of these it rests on."

Near-verbatim restatement of a build rule from the Pachomian source record's body. Borderline; fix while touching the record anyway.

## B. Other SUBSTANTIAL findings

**S1 — `desert.term.theoria` evidential: Round 2's fix of one factual overclaim introduced a different one.** "…this contemplative stage's own teaching, **which stays untranslated**" is false and contradicted by the record's own registered source: `desert.source.evagrius-praktikos.md` names Bamberger's 1970 translation of exactly this material as existing — **copyrighted and unquotable here**, not untranslated. Three consecutive states of defect on one clause: jargon (draft) → factual overclaim (R1 fix) → opposite factual overclaim + fresh jargon (R2 fix).

**S2 — `desert.term.puritas-cordis` mis-describes Cassian's Institutes IV.43, under the lexicon's only citation_specificity A / "verified verbatim" label.** Both the locus ("the fear-of-the-Lord ladder ending in purity of heart") and the evidential sense ("climbs from the fear of the Lord to the same summit") say the ladder *ends* at purity of heart. Reading the whole chapter: the ladder's actual final rung is "the perfection of apostolic love," with purity of heart the *penultimate* rung. Both prior rounds verified the quoted words sat at the line without checking the words against the claim. This flattens exactly the teleological distinction (purity of heart as immediate goal, not final end) the term exists to carry, and Conference I's own quote on the same record makes that distinction explicitly.

## C. COSMETIC findings

- **C1** — theoria: "Socrates … quotes some of his practical sayings **in English**" attributes the English to Socrates rather than to Zenos's translation; the source record requires the double caveat (excerpting + translation).
- **C2** — apatheia: "have no English rendering to quote directly here" is ambiguous against its own source record (Bamberger, Sinkewicz exist, copyrighted); match koinonia's cleaner model ("no English of it can be quoted here directly").
- **C3** — the index's "Review rounds note" undercounts the Finding-1 record set ("seven" should be "eight," matching Round 1's own list) and, in its closing line, repeats the exact over-claim-of-completeness pattern (asserting the sweep is now accurate rather than describing what was actually swept).
- **C4** — antirrhesis body note ordering: Round 2's note landed *above* Round 1's, reversing the chronological convention Round 2 itself established everywhere else.

## D. Verified clean (no finding)

Reciprocity (24 edges, re-derived from scratch, matches Doc_06 and the index exactly). Index-to-record fidelity (18/18 rows, no drift). Canon-cell resolution (zero orphans; penthos's empty set still correctly reasoned). Quotation-mark hygiene — **this pattern (Round 1 Finding 2) is now exhaustively clear**, confirmed by extracting every quoted string in all 72 sense fields plus the other participant-facing fields: no unattested string sits inside quotation marks anywhere. Confidence blocks other than puritas-cordis's (S2). Doc_06 fidelity elsewhere. No encoding damage. Zero "participant" collisions remain in any sense field (Round 2's N7 fix scoped correctly and holds). All of Round 2's other fixes (apatheia, koinonia's other two edits, kellion, nepsis's scripture fix, antirrhesis's punctuation, cheironaxia's locus, geron-abba-amma) independently re-verified genuine against the vendored files.

## E. Gate battery

12 of 13 pass (schema-validation, referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, no-build-attribution); canon-coverage fails on the same 18 blank cells as Rounds 1–2 (expected, unchanged, no regression). No gate can or will catch section A — `_ATTRIBUTION_FIELDS` doesn't scope `senses`, and nothing compiles it yet. This is a human-read-only defect class.

## F. Assessment

Nine of Round 2's eleven fixes are clean. But three consecutive rounds have now each swept for the specific strings the prior round named rather than for the pattern by family, and each has therefore left survivors for the next round to find — including one written in by the "fix" meant to remove it. Plus one real, previously unexamined factual defect (S2) sitting under the lexicon's strongest confidence label. Nothing here ships yet (senses are not compiled), but this is not a cleared step.

VERDICT: SUBSTANTIAL REVISION REQUIRED
