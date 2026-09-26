# Targeted re-check (post-`598f69c` fix commit): `CiC_VoiceRebuild_Stage1_Research_Findings_2026-08-08.md`

*Opus targeted re-check, dispatched 2026-08-08. Not a second full round — scoped to the single commit that has landed since the Research Round 1 adversarial review and has never been reviewed: `598f69c` ("Apply Research Round 1 adversarial findings"), on branch `claude/cic-voice-rebuild-postmortem-fr4859`. Round 1 (`..._Research_Opus_Adversarial_Review_Round1_2026-08-08.md`) read in full first, per the Standard Practice's point 4, so each fix could be judged against what it was supposed to do rather than against the commit message's account of itself. Brief §§4/7/8/9 and Round 4 re-read at every hunk the commit cites. The rest of the document was deliberately not re-reviewed.*

*Verification method, per points 1 and 3. Every replacement fact re-derived from primary source, never from the fix commit's wording. The four per-world turn-ceiling quotes opened at their stated line numbers in `cic-poc/backend/data/*/…Permanent_Prompt_*.txt` and matched character-for-character; Theon's (61 lines) and Marius's (160 lines) prompts read whole and grepped for every length/measure/paragraph/turn token. `leak_audit_instrument.py` executed end to end and its output `git diff`ed against the committed `leak_audit_apparatus_hits.json`; every §4 figure independently recomputed from the regenerated JSON; the pre-commit instrument recovered from `598f69c^` and run, to establish whether 172 is real and whether it is still reproducible. Section denominators (107 / 60 / 60) recounted from the raw corpus. The apparatus regex decomposed into its eight pattern classes and re-run per file to test §4's causal reconciliation. Round 4's leak table (lines 200–210) re-read and its three-world distribution matched file-by-file against the new JSON. `voice_rebuild_research_probe_results.json` parsed directly: usage records tallied by label, `turn_analyses` read per turn, transcripts read whole. `Decision-Log.md:65`, `wrs/parameters.yaml:103-104`, `app/prompts/representative_prompts.py:162-199`, `app/rag/pipeline.py:135-170`, `scripts/voice_rebuild_research_probe.py:110,130-137` read at every cited location. All 43 `§N` pointers re-extracted and resolved by hand. Diff sized: 258 changed lines in the findings document, 237 in the instrument, 1,609 in the results JSON.*

---

## Bottom line

**Not clean.** The three P0s are genuinely and completely fixed — I verified all three from source and could not falsify any part of them. But the commit also wrote a substantial block of *new positive prose* into §4 (the instrument-provenance method paragraph and the Round-4 reconciliation), and that block is where three new defects sit. Two Round-1 fix items were applied at the quoted site and left unapplied elsewhere.

**0 P0. 3 P1. 9 P2.** Design is not blocked, but §4's method paragraph and its Round-4 reconciliation paragraph both need a rewrite before this document gates Design, because a Design reader who takes them at face value will believe things about the committed instrument that are not true.

**What is clean, verified independently:**

- **P0-1 (instrument provenance) — fixed, exactly.** I ran `leak_audit_instrument.py`; it regenerated `leak_audit_apparatus_hits.json` **byte-identical** to the committed file (`git diff` empty). Every §4 headline reproduces from it: `apparatus_files` 104, `apparatus_files_lex` 58, `apparatus_files_story` 46, `hits_by_section` 152 / 44 / 36 / 31 / 28 / 14, `files_by_section` 45 / 33 / 20 / 17 / 8, `per_world` rates 0.81 / 0.74 / 0.67 / 0.61 / 0.55 / 0.26, the six markerless files, the eight Final-Assembly files. Independently: 107 lexicon files really do carry an `Ecological Function` field (89 as `## heading`, 18 as `**bold label**`); 60 story files carry `Formation Ecology Connection` and 60 carry `Usage Guidance`; Alexandria really holds 50 of the 118 lexicon chunks. Round 1's central P0 is closed.
- **P0-2 (turn ceilings) — fixed, all four quotes verbatim at the stated lines.** `desert_…Papnoute.txt:13` — *"Hold to this as a hard measure, not a preference: four sentences is already long for you, and most of what you say should be one to three"* ✓. `hal_…Albina.txt:27` — *"a turn of yours rarely runs past two short paragraphs"* ✓ (line 29 is the periodic-rhythm paragraph, as Round 1 said). `pahc_…Chloe.txt:31` — *"Even your fullest answer stops at two short paragraphs"* ✓. `syr_…Yausep.txt:43` — *"two or three short paragraphs at the very most"* ✓. Theon and Marius carry **no** turn or answer-length ceiling: I read both files whole; Theon's `:37` is sentence shape and Marius's `:117` is court vocabulary, and neither file contains the word "paragraph" or any stated turn measure. §8 decision 2 was rewritten to match. Zero survivors of the falsified enumeration anywhere in the document.
- **P0-3 (two failing prompts) — fixed at all three sites.** §3.1's table unchanged and still correct; §3.1's consequence now reads "Two prompt files fail: Marius (both numbers) and Yausep (FK 10.0, at the ceiling)"; §9's Bottom Line now reads "concentrated in two prompts (Marius failing both numbers, Yausep at the FK line)". Whole-document grep for *"only failing prompt"*: zero hits.
- **P1-2 (invisible calls) — fixed and correct.** Recomputed from `voice_rebuild_research_probe_results.json`: Yausep 71 usage records − 8 `main_response` = 63 invisible over 8 turns = **7.875 → 7.9**; Papnoute 68 − 8 = 60 over 8 = **7.50**. Both match the document. `Decision-Log.md:65` is the right line and carries *"roughly ten invisible calls for every one visible reply"* verbatim. The explanatory parenthetical ("single-world Interview turns skip the table-mode checks") checks out structurally — `turn_type_router`, `turn_selector`, `convergence_check`, `misattribution_check`, `manufactured_resolution_check` are table-mode labels absent from both single-world batteries. Whole-document grep for `10–12`, `10-12`, `:63`: zero hits.
- **P1-3 (bridge-first) — fixed and correct.** `Yausep:45` names exactly three terms (`raza`, `qyama`, `Iḥidaya`). From `turn_analyses`: turns 2 and 3 lead on `qyama` (named), turn 4 on `madrasha` (not named, English gloss first), turns 1/5/6/7/8 false. **2 of 8 as written, 3 of 8 broad** — exactly as reported, at all four sites (§1 P3, §5.1, §5.3, §9). Whole-document grep for `3/8` and for `3 of 8` as a bridge-first count: zero surviving pre-fix hits (the two remaining `3 of 8` strings are the broad measure, correctly labelled, and Papnoute's over-settling rate).
- **P2-7 (guard-layer inference) — fixed and correct.** Yausep turn 2's `usage_labels` in the results JSON do contain both `negative_condition_lexicon` and `citation_grounding`. The inference chain is sound: `app/rag/pipeline.py:152-162` only reaches `evaluate_negative_conditions` when a relevance-kept candidate carries an evaluable guard, so the label implies non-empty retrieval, and `representative_prompts.py:163` gates layer 1 on `if retrieved_context:`. The document now says "inferred" and names what the probe does not log. Correct.
- **The Round-4 reconciliation's *file-level* claim holds.** All five of Round 4's named verbatim examples re-flag in the new JSON: `ijclex001_primatus`, `ijclex002_presbeia`, `ijclex005_imperator_intra_ecclesiam`, `desertlex011_apatheia`, `hal_lex11_exegesis-practiced-authority`. Better than that — Round 4's whole "17 covered by neither" distribution reproduces almost exactly: Desert 9 lexicon files split `World Meaning` 7 / `Distortion Risk` 2 (Round 4's exact breakdown, same 9 files), IJC 3 in `Plural-Voices Note` (Round 4's exact 3), Alexandria 6 in `World Meaning` against Round 4's 5. **Desert lexicon is 9 of 18 = 50%**, the document's number, and it is the same 9 files Round 4 found by hand. That sub-claim is not just numerically right, it is the same set.
- **Every other P2 from Round 1 landed:** "not 1" → "not 2" ✓; Final Assembly quote now carries `[...]` ✓; §5.3's FK-as-proxy ✓; trait-table `12` → `—` ✓; P6 carries its source's medium-confidence label ✓; "only *pre-existing* real callers" ✓ (`voice_rebuild_research_probe.py:110` does import `readability_check`); both denominators reported in §4 ✓; §3.2 expanded from a stub ✓; §8 decisions 2 and 4 now say "the brief's §7 Part A" and "the brief's §4" ✓. §8 question 9 and the two new §7 rows deliver P1-5 and P1-6 with their evidence verified (brief finding C's Albina firing is quoted accurately; Papnoute turn 7's participant question — *"Tell it to me plain, the way you'd tell a boy who walked out to your cell and asked"* — really is the participant-supplied hypothetical the document says it is).

**The pattern, stated for the record.** Round 1 predicted it in its own closing: *"because fixes (1), (2) and (4) all require asserting replacement facts, this document should get a targeted re-check of exactly those hunks."* That is what happened, with one refinement worth carrying forward. Fix 2 (the ceilings) required replacement facts that were **quotations** — and every one of them is right, because a quotation can be checked at the moment of writing. Fix 1's replacement facts were **descriptions of an instrument's behaviour and causal explanations of a discrepancy** — and all three defects below are of that kind. The distinction is not "new prose is unsafe"; it is that *new prose describing what a script does is unsafe unless you re-read the script after rewriting it*, and nobody re-read `leak_audit_instrument.py` against §4's paragraph after the rewrite. Both the paragraph and the script's own docstring now describe a two-stage instrument that the script is not.

---

## P1 — materially improves, not disqualifying

### P1-1. §4's method paragraph and the instrument's own docstring both describe a two-stage instrument. The committed instrument has one stage, cannot produce 172, and does not implement one of the pattern classes both texts attribute to it.

§4, method paragraph (new in this commit):

> *"…in two stages: **a deliberately over-matching broad screen (172 files flagged** — that number includes by-design material like Distortion Risk's "modern hearing" language and is NOT a leak count; **used only for the no-Key-Sources-marker detection and as a candidate pool**), then a refined apparatus classification (gravity codes/numbering, Doc_/Force references, template/assembly language, CT tags, **tier meta-language**, builder notes, strand codes) with per-section attribution. **Every count below reproduces from the single committed instrument**."*

`leak_audit_instrument.py`'s own docstring, also new in this commit, says the same thing in more detail — *"Stage 1 (broad screen): wide pattern classes over serialized bodies… Its file count (172) is NOT a leak count"* — and then *"Stage 2 (refined classification)."*

Three things are wrong, all verified by reading and running the committed file:

1. **There is no Stage 1.** The script has exactly one pattern object, `APPARATUS` (lines 114–118), and one scan loop (lines 133–156). No broad screen exists anywhere in it. Running it produces no `172` and no `files_flagged` key at all.
2. **172 is real but is no longer reproducible from anything in the repository.** I recovered the pre-commit instrument from `598f69c^` and ran it: `files_flagged: 172`, confirmed. That script was *overwritten* by this commit. So the fix traded one provenance defect for a smaller one: Round 1's complaint was that the committed script contradicted the document by 68 files; the position now is that the document cites a number no committed artifact can produce. Round 1's fix instruction was *"state the narrow pattern set's count (104) and the broad set's count (172)"* — which the document does — but it presumed both counts would remain derivable.
3. **The no-marker detection does not come from any broad screen.** The committed instrument computes it inline at line 101 (`sections.find_section(body, KEY_SOURCES_MARKERS) is None`) inside the refined pass. The paragraph's account of the division of labour between the two stages describes neither the old script nor the new one.
4. **"Tier meta-language" is not a pattern class of the refined classification.** The `APPARATUS` regex is, in full: gravity codes and named gravities, `G0\d`, `C\d (`, `Doc_0\d`, `Force \d[A-C]`, `Tensional`, `Primary/Supporting grav`, `Strand [A-C]`, `Final Assembly Instruction`, `L4-Templates`, `per Template`, `CT tag`, `Contest Type`, `Reciprocity Note`, `builder notes?`, `No brackets`. **No tier pattern.** The *old* broad instrument did have one (`tier_meta`, `\bTier[- ][123]\b|\btier justification\b`); the phrase survived the rewrite of the sentence and now misdescribes the instrument it names.

**Why this matters.** §4 is the section Round 1 blocked on, and the whole point of the fix was to make its provenance claim true. It is now true of the 104 and false of everything else in the same paragraph. A Design reader auditing the filter will run the committed script, get no 172 and no tier-language class, and be back where Round 1 started — with a document whose account of its instrument does not match the instrument.

**Fix.** Two options, both cheap. (a) Restore the broad screen as a `--broad` mode in the same file so 172 is reproducible, and delete `tier meta-language` from both pattern lists (or add the pattern). (b) Delete the two-stage framing entirely: say that an earlier over-matching screen (172, superseded and not committed) established the candidate pool, that the committed instrument is the refined classification only, and list its pattern classes from the regex itself. Correct the script's docstring in the same edit — right now the docstring is a committed artifact making a false claim about its own code, which is the exact artifact class Round 1 named as this stage's new risk.

---

### P1-2. §4's Round-4 reconciliation asserts three things about the 58-vs-46 difference. The file-level claim holds; the superset claim is false for two files, and the causal explanation accounts for 6 of the 12, not 12.

§4, headline bullet 1 (new in this commit):

> *"Reconciliation with Round 4's hand-verified measurement (46 of 118 lexicon chunks): **this instrument's lexicon count (58) is a superset of that verified floor** — **the added pattern classes (strand codes, tier meta-language, Reciprocity/template references) account for the difference**, and every Round-4 example re-flags here."*

**"Every Round-4 example re-flags here" is true** — I checked all five named files and the full three-world distribution behind Round 4's 17 (see the clean list above). That part is solid and is the strongest thing in the paragraph.

**The superset claim is false for at least two files.** Round 4's table (`..._Round4_2026-08-07.md:200-206`) partitions its 46 leaking lexicon chunks by which of the brief's two filter patterns would catch them: 27 by pattern 1 (`Ecological Function`), **6 by pattern 2 (no `Key Sources` marker, whole tail passes)**, 17 by neither. The six markerless chunks are therefore inside Round 4's 46. Checked against the new JSON: `syrlex005` and `syrlex008` appear (on `Reciprocity Note`), `ijclex011` and `ijclex012` appear (on `Final Assembly Instruction`), but **`pahclex012_hetaeria.md` and `pahclex013_pertinacia.md` do not appear in `apparatus_hits` at all.** I executed the serialization path on both: their entire model-facing body is `## Distortion Risk` / `**Modern Hearing:**` / `**World Hearing:**` / `**Confidence:**` — 548 and 651 characters, no apparatus pattern anywhere in them. They are real fail-open leaks and they are not in the 58. 58 ⊉ 46.

This is not a rounding quibble. §4's own "What this hands Design" paragraph correctly separates the leak into *two structurally different halves* — 104 apparatus-authored files and 6 code-side fail-opens — while the reconciliation paragraph, five bullets earlier, compares the first half against a Round-4 measurement that spans both. The document contradicts its own taxonomy across §4.

**The causal explanation is wrong by half.** I decomposed `APPARATUS` into its eight classes and re-ran it per lexicon file. Per-class file counts: `Doc_/Force` 34, gravity 24, strand 12, CT 8, Reciprocity 2, template 2, builder 2, `C\d (` 1. **Files hitting *only* the classes the document names as "added" — strand codes, CT tags, Reciprocity/template — number 6, not 12:** `pahclex005_diakonos`, `pahclex010_agape-label`, `syrlex005_memra`, `syrlex008_mar`, `alexlex011_nous`, `ijclex010_nea_rhome`. And two of those six (`syrlex005`, `syrlex008`) are markerless chunks Round 4 already counted, so they cannot be part of the difference at all. The named classes explain at most 4 of the 12-file gap. ("Tier meta-language," the third class named, does not exist in the instrument — see P1-1.)

**Fix.** Rewrite the sentence to what is actually true and verifiable: *"Round 4's hand check found 46 of 118 lexicon chunks leaking, partitioned as 27 inside `Ecological Function`, 6 markerless fail-opens and 17 covered by neither. This instrument's apparatus pass re-flags all of Round 4's named examples and reproduces its whole 17-chunk distribution file-for-file (Desert 9 — the same 9, `World Meaning` 7 / `Distortion Risk` 2; IJC 3 in `Plural-Voices Note`; Alexandria 6 against Round 4's 5). It is not a superset: `pahclex012` and `pahclex013` leak structurally (no `Key Sources` marker) but carry no apparatus vocabulary, so they sit in §4's second half, not this count."* That is longer, true, and re-derivable from the two committed artifacts.

---

### P1-3. Round 1's P0-1 fix asked for §4's two classification caveats to be corrected or deleted. Neither was touched. Caveat (1) still promises Design an inspectability the committed JSON does not provide.

§4, caveats paragraph — **unchanged by this commit**:

> *"(1) pattern-matching over-flags; every pattern class was hand-sampled and **the per-file JSON is committed for full inspection**, but per-line true/false classification across all 104 files was not done exhaustively…"*

Round 1's finding was specific: *"The JSON contains section names and integers. There are no lines in it. A Design reader cannot inspect a single flagged string."* Its fix was equally specific: *"Either extend it to emit the matched line per hit (so caveats (1) and (2) become true), or delete both caveats' claims about inspectability."*

The regenerated JSON's per-file record shape is unchanged: `{"world": …, "kind": …, "sections": {name: count}}`. No `line`, no matched text, no pattern label. The instrument's `scan` loop discards the match object after computing `section_of(body, m.start())` (lines 142–143). Caveat (1) is still false as written, and the fix commit's message claims the P2 sweep and all six P1s landed.

This is the half-application failure in its cleanest form — the fix was applied at the site Round 1 quoted longest (the §4 method paragraph) and not at the site three paragraphs below that the same finding named.

**Fix.** One line in the instrument: change the `sections` value from a count to a list of `(section, line)` pairs, or add a parallel `"lines"` array capped at 220 chars per hit. Then caveat (1) and caveat (2) both become true and the audit becomes genuinely re-auditable. Failing that, delete "for full inspection" and say what the JSON actually supports: *"the per-file JSON is committed with per-section hit counts, which locates every flag to a field but does not reproduce the matched text."*

---

## P2 — polish

1. **Round 1's P2-4 (bare `§N` disambiguation) is half-applied.** The two pointers Round 1 named by hand were both fixed (§8 decision 4 → "the brief's §4"; §8 decision 2 → "the brief's §7 Part A"), but the general instruction — *"Prefix every cross-document pointer"* — was not swept. Four bare cross-document pointers remain: §0 line 18 (*"where the brief requires falsifiability (§8)"* — this document also has an §8, and it is the open-questions section, so it reads either way), §0 line 40 (*"the four §3 studies"* — the brief's §3; this document's §3 is the load-bearing system facts), §3.1 line 333 (*"(§6 Objective 3)"* — the brief's §6; this document's §6 is the 16-trait rubric), §8 line 692 (*"per §9's mandate to say so plainly"* — the brief's §9; this document's §9 is the Bottom Line and carries no mandate). All four resolve correctly *to the brief*; none is prefixed.

2. **The sustained-disagreement repoint introduced a new dangling pointer.** P2 now reads *"the sustained-disagreement probe the brief's §8 specifies — an instrument that does not exist yet; **see this document's §7 table**."* The brief's §8 attribution is correct (line 1139: *"A sustained-disagreement probe, run across multiple turns per world"*). But §7's table has eleven rows and **none of them is a sustained-disagreement probe** — the reader is sent to a table to find an acknowledgement of a gap the table does not contain. Round 1 offered two fix options; the commit took neither cleanly, repointing the attribution but then pointing forward at a row that was never added. Either add the row (marked *Still missing — named Design-stage instrument*, alongside the three other "still missing" rows) or end the sentence at "does not exist yet."

3. **§9 still says "instructions," plural, where §5.3 was corrected to one instruction plus one proxy.** §9: *"a currently-deployed world violating its own file's central voice **instructions** under measurement."* §5.3, rewritten in this same commit, now says exactly the opposite — bridge-first is his file's instruction, and the FK-10 exceedance is *"the project's FK-10 reading floor — a proxy for his file's 'each stage is its own short sentence' instruction, **not the instruction itself**."* Only one of the two measured failures is a violation of an instruction in his file. Same defect shape as P0-3: corrected at the site the review quoted, left standing in the summary. Fix: *"violating its own file's bridge-first instruction and running above the project's reading floor."*

4. **P3's instance count is off by one, in a sentence this commit rewrote.** §1 P3 introduces *"the system's own further instances"* and lists **five** (numbered 1–5), then says *"This session's live probes added **the fifth** and sharpest instance"* — it is the sixth. §5.3, whose sentence was rewritten in this commit, preserved *"on top of **the four prior instances** P3 lists."* Both should be one higher. Round 1 did not catch this; it is being reported now because the §5.3 sentence was edited without re-checking the count it carries.

5. **§3.1's new Yausep bullet attributes a *file* failure to a finding about *output*.** The new text: *"Yausep's at-the-line failure matches finding D's correction that he was never demonstrably plain."* Brief finding D (line 587ff) is a measurement of his *baseline transcripts* — *"Yausep 23.0 [words/sentence]… he does not read as short"* — i.e. output. §3.1's own first bullet makes the file-vs-output distinction the crux of the whole section ("Her *file* is not her problem; her *output* is"). The sentence is not false — Yausep is weak on both — but it blurs the distinction the section is built on, in the bullet immediately below the one that establishes it. Round 1's suggested note is sharper and does not blur anything: *"Yausep is the only world in the corpus failing on both file and output."*

6. **§5.1 gives the wrong reason the reclarify regex missed the opener.** New text: *"the opener's present-tense 'When I speak of the qyama, I mean…' is not among the regex's **past-tense patterns**."* Read at `voice_rebuild_research_probe.py:130-137`: five of the six patterns are past-tense, but the sixth — `by [\w'-]+ (?:I|we) (?:mean|meant)` — accepts the present tense. The discriminator is the **form** (false-referent: "when I said X", "by X I mean"), exactly as Round 1 described it, not the tense. Minor, but it is a claim about a committed instrument's behaviour, in a sentence written to correct a claim about a committed instrument's behaviour.

7. **§7's two new rows put the instrument description in the Status column.** The table's columns are `Instrument | Status | What it measures`. The Objective 2×4 row's Status cell reads *"`fabrication_adjudication` firing rate on story-led turns, plus manual read…"* (a measurement description) and its "What it measures" cell reads *"Named for Design — see §8 question 9"* (a status). The Objective 3 row has the same inversion in milder form. Both rows are substantively right and deliver P1-5 and P1-6; they just read as swapped against nine correctly-filled rows above them.

8. **§2.1's parenthetical understates Theon.** *"A scan of Theon's and Marius's files found no per-turn ceiling (both instruct short *sentences*, not short turns)."* The headline claim is correct — I read both files whole and neither carries any stated turn or answer-length measure. But Theon's `:45` does carry an unmeasured length discipline of turn scope: *"if the engagement has become a lecture, with the participant a spectator, it has departed from the way this world formed anyone. When you find yourself explaining at length, turn back into a question"* — plus `:47`'s *"You do not deliver everything at once."* Since §8 decision 2's whole question is what Theon and Marius should acquire if the shared ceiling goes, Design should know Theon has an anti-lecture rule with no measure attached rather than nothing at all. Add six words.

9. **§4's paired denominators switch corpus mid-sentence without saying so.** *"Ecological Function 33 of 107 **lexicon** files, comparable to Usage Guidance's 20 of 60."* The 60 is *story* files — `Usage Guidance` appears in 60 of 60 story chunks and in **zero** lexicon chunks (verified by grep across all six worlds). Both numbers are right and the comparison is fair on rate (31% vs 33%), but "comparable to Usage Guidance's 20 of 60" immediately after "lexicon files" invites the wrong denominator. Write "20 of 60 story files."

---

## What verified clean (re-derived this pass, not trusted)

**The regenerated instrument output, in full.** `python3 leak_audit_instrument.py` → `git diff` on `leak_audit_apparatus_hits.json` returns empty. `lexicon_total` 118, `story_total` 60, all six worlds migrated, `apparatus_files` 104 (58 lex / 46 story), `no_key_sources_marker` = the six named files in the document's order, `final_assembly_reaches_model` = `ijclex011`, `ijclex012` and `ijcstory001`–`006` (8, and all six of Marius's story chunks — the document's "most exposed world" claim holds).

**Every §4 figure, against the JSON.** 104/178 = 58.4%. Section hits 152 / 44 / 36 / 31 / 28 / 14 exact. Files-by-section 45 / 33 / 20 / 17 / 8 exact. Per-world 21/26 = 80.8→81%, 14/19 = 73.7→74%, 12/18 = 66.7→67%, 17/28 = 60.7→61%, 33/60 = 55%, 7/27 = 25.9→26%. PAHC genuinely is the highest rate in the corpus, and the brief genuinely does pilot the `_HOW_YOU_ENGAGE` rewrite against Chloe alone (`brief:892`, *"Pilot it against Chloe alone, verify in isolation"*), so the "the pilot will run on the most contaminated corpus" observation is real and is the finding Round 4 asked for.

**Corpus denominators, recounted from the raw files.** 118 lexicon (Alexandria 50, Desert 18, Hieronymian 15, PAHC 13, IJC 12, Syriac 10) and 60 story (10/10/12/13/6/9). 107 lexicon files carry an `Ecological Function` field; the 9 that do not are `pahclex012`, `pahclex013`, `syrlex005`, `syrlex008`, `alexlex051`, `alexlex059`, `alexlex074`, `alexlex081`, `alexlex090`.

**All four ceiling quotes and line numbers**, opened directly and matched character-for-character, plus the negative scan of Theon (61 lines) and Marius (160 lines) for `paragraph|sentence|turn|length|measure|at most|brief|short` — no ceiling in either.

**Every probe number the fix touched.** Yausep `words_per_sentence` per turn 17.9 / 24.4 / 20.9 / 28.3 / 19.9 / 12.6 / 15.8 / 18.1 → mean 19.7375 ✓. FK > 10 on turns 2 (10.5) and 4 (11.45) only ✓. `technical_term_in_first_sentence` true on 2, 3, 4 ✓ with `first_technical_term` `qyama` / `qyama` / `madrasha` ✓. Turn 5 first sentence *"Mar Simeon."* ✓. Turn 7 FK 4.76, 15.8 w/s ✓. `reclarify_opener_patterns` empty on all 16 turns across both worlds ✓. Papnoute FK 1.38–6.65, 8.9–19.7 w/s, 42–187 words vs Yausep's 158–342 ✓. `over_settling_adjudication` 6 of 8 and 3 of 8 ✓. `fabrication_adjudication` once, Papnoute only ✓. Usage totals 71 and 68, `main_response` 8 each ✓.

**`wrs/parameters.yaml:103-104`** carries `flesch_kincaid_grade_band: [8, 10]` and `flesch_reading_ease_min: 60` — §5.1's and §5.3's "the project's own reading floor" attribution is right.

**Brief citations behind the new §8 question 9.** Finding C's Albina passage (`brief:543-560`) says exactly what the document says it says, including *"on the exact turn where the prototype told the Marcella story concretely"* and the epitaph-genre Usage Guidance. `representative_prompts.py:186-199` is the story-context block carrying the Tier/Confidence and Usage-Guidance-source instruction. Papnoute's turn 7 participant question is the hypothetical the document describes.

**Whole-document sweep for pre-fix survivors** — `only failing prompt`, `3/8` as a bridge-first count, `10–12`/`10-12`, `:63`, `Albina.txt:29`, `three per-world`, `ceiling-less`, `only shared ceiling`, `not 1`, `| 12 |`: **zero hits on every one.** Where the fixes were applied, they were applied completely. The three half-applications found this pass (P1-3, P2-1, P2-3) are all cases where Round 1 named a *class* of site rather than quoting the specific string.

---

## Recommended fix list, in order

1. Rewrite §4's method paragraph and `leak_audit_instrument.py`'s docstring so both describe the single-stage instrument that exists; drop or implement "tier meta-language"; either restore the broad screen as a mode or say plainly that 172 came from a superseded, uncommitted screen. **(P1-1)**
2. Rewrite the Round-4 reconciliation sentence: keep "every Round-4 example re-flags" and add the distribution match that supports it; drop "superset" and the added-classes explanation, and name `pahclex012`/`pahclex013` as the two Round-4 chunks that sit in §4's *other* half. **(P1-2)**
3. Emit matched lines from the instrument, or delete "for full inspection" from caveat (1). **(P1-3)**
4. Sweep the P2 list — items 2 (dangling §7 pointer), 3 (§9's plural "instructions") and 4 (the instance miscount) are the three that a Design reader would actually trip on.

After (1)–(3), §4 is sound and the document is ready to gate Design. Nothing here needs a third pass: (1) and (2) are two paragraphs, (3) is one line of Python, and all three are verifiable by re-running the committed script and diffing the JSON — which is now, to the fix commit's real credit, a thing that works.

---

*Simulated review — informational only, not an Article 31 substitute.*

---

# Addendum — follow-up verification, 2026-08-08 (commits `503f74d` and `2c41473`)

*Opus follow-up, same discipline, same document, dispatched after the two commits that landed on top of `598f69c`. Scope: (1) `503f74d`, a brand-new §8 question 9 (record-sourced assembly as the default architecture, per Mark's 2026-08-08 direction) plus a §0 purpose note plus the renumbering of the old question 9 → 10 — new positive prose that has never been checked; (2) `2c41473`, the fix pass applying this re-check's own 3 P1s and 9 P2s. Nothing else in the document was re-reviewed.*

*Verification method. Every factual claim in the new §8 question 9 taken to source: `wrs/records/*/source/` counted per world with `find`; all twelve record subdirectories enumerated and counted per world; `wrs/views/permanent_prompt.py` and `wrs/views/chunk_views.py` read for the Desert-hardcoding and staging claims; brief §6's priority paragraph and Objective 5 read verbatim; the `wrs/` lockstep requirement located at `brief:297`; the rigor/bibliography sweep confirmed in `git log` on `cic-poc/backend/wrs/records`; `git diff --stat f4c15c8~2..HEAD -- cic-poc/` run to test §0's "nothing was changed this stage." For the fix pass: `leak_audit_instrument.py` executed and `git status` checked for a byte-identical regeneration; the pre-`598f69c` broad instrument re-run and its flagged set compared element-wise against the restored Stage 1; the `APPARATUS` regex re-decomposed per class; `Usage Guidance` occurrences counted across all 118 lexicon and 60 story chunks; the instrument grepped for any line-emitting code; all `§N` pointers re-extracted; every one of this re-check's twelve findings grepped at its site.*

## Addendum bottom line

**Not clean.** **0 P0, 4 P1, 7 P2.**

**The instrument work is now genuinely and completely right, and it is worth saying so first.** `leak_audit_instrument.py` runs two real stages: `broad_screen_files: 172` and `apparatus_files: 104` both emit from the same execution, and re-running it leaves `git status` clean — the committed JSON is byte-identical to what the committed code produces, both numbers included. I also confirmed the restoration is *faithful* rather than coincidental: I re-ran the pre-`598f69c` broad instrument and compared sets, and the old "hits **or** markerless" definition and the new "hits only" definition flag exactly the same 172 files (every markerless file also carries a broad hit), so the restored Stage 1 is the same screen that historically produced the number, not a new screen tuned to hit it. All four of P1-1's specific complaints are closed: 172 is reproducible, `tier meta-language` has moved from the Stage 2 list to the Stage 1 list in both the docstring and §4 (matching the code, where it is a `BROAD_PATTERNS` entry and absent from `APPARATUS`), the Stage 2 prose list now matches the regex class-for-class, and both texts now say the no-Key-Sources-marker detection comes from the serialization step rather than from either pattern stage — which is where the code does it. P1-2's reconciliation is also correctly rewritten: "neither contains the other" is right, `pahclex012`/`pahclex013` are named and correctly reassigned to the fail-open class, and `tier meta-language` is gone from the added-classes list.

**But the fix pass repeated this thread's signature failure twice, in the two places where it chose to write a new explanatory clause instead of deleting a false one** (P1-A-2 and P1-A-3 below) — and the new §8 question 9, being 400 words of brand-new positive prose, carries the round's only wrong number and a direct verbal contradiction with the section header it sits under.

**The new §8 question 9 is substantively well-sourced.** Everything in it that I could take to source held except the record count: the Desert-only staging assembler is real (`STAGING = HERE/"staging"/"desert_world"`, hardcoded `desertcore001` / `desertvoice001` / `world_id: "desert-monasticism"`, writes to staging only, docstring's *"Deterministic: same records -> byte-identical outputs"* supporting the "deterministic assembly" framing); `probe_parity`'s 4-of-6 failure and its record-layer-fidelity reading are exactly as P7 and §3.2 already established, and the "records-vs-deployed drift this architecture ends structurally" inference follows from them; the `wrs/` lockstep requirement is real at `brief:297`; Objective 5 is genuinely *"The Construction Framework itself changes so that world #7 doesn't reintroduce this exact gap"*; and the quality-governance constraint's load-bearing citation is verbatim — brief §6 says *"Objective 3 carries exactly as much weight as Objective 4, not less."* The "recent rigor and bibliography sweeps" are real (`06a9561`, "Rigor: real field-bibliography sweep, Syriac (syri.ac) + Desert (BIBP)"). **The renumbering is clean**: whole-document grep returns exactly two `question N` pointers — §0's new note pointing at question 9 (the new item, correct) and §7's Objective-2×4 row pointing at question 10 (the renumbered item, correct). No dangling pointer to the old numbering anywhere. **§0's new purpose note is verifiably true**: `git diff --stat f4c15c8~2..HEAD -- cic-poc/` shows the entire Research stage added exactly two files, `voice_rebuild_research_probe.py` and its results JSON. No voice file, capsule, or pipeline was touched.

---

## P1 (addendum)

### P1-A-1. §8 question 9's one quantitative claim is wrong. "26–41 source records per world" understates the largest world by 35 records.

> *"the `wrs/records/<world>/` layer: **26–41 source records per world** plus term/story/gravity/contested_claim/figure/demonstration/voice_profile/world_core records…"*

Counted directly (`find wrs/records/<world>/source -type f`, all `.md`):

| World | source records |
|---|---|
| PAHC | **76** |
| Syriac | **64** |
| Imperial-Juridical | 41 |
| Alexandria | 37 |
| Desert | 26 |
| Hieronymian | 26 |

The true range is **26–76**. The stated ceiling of 41 excludes the two largest worlds, and PAHC — the world §4 has just identified as carrying the corpus's highest apparatus-leak rate (81%) and the world whose Representative is the brief's pilot — is nearly double the stated maximum. This is the only number in the new section, it is the section's evidence that the record layer is substantial enough to build on, and it is the classic shape: a replacement fact asserted in new prose without being counted.

**Fix.** *"26–76 source records per world (Desert and Hieronymian 26, Alexandria 37, IJC 41, Syriac 64, PAHC 76)."* The corrected number strengthens the argument rather than weakening it.

### P1-A-2. §4's caveat (1) was rewritten into a new false claim. Running the committed instrument does not produce the matched lines; it produces no lines at all.

The previous caveat said the JSON was committed *"for full inspection"* — this re-check's P1-3 called that false because the JSON carries no matched text. The replacement:

> *"the committed JSON carries per-file, per-section hit counts (**the matched lines themselves are reproducible by running the committed instrument**, not stored in the JSON)…"*

Grepped the instrument for every output path: `write_text` at line 221 (summary + per-file section counts) and `print` at line 223 (summary). `scan_body` computes `section_of(body, m.start())` and **discards the match object**; no `m.group()`, no line slicing, no text capture anywhere in the file. Running the committed instrument emits exactly zero matched lines. A Design reader following the caveat's instruction will run the script and get the same JSON back.

P1-3 offered two fixes: emit the lines, or say what the JSON actually supports. The commit took a third path that asserts a capability the code does not have — replacing a false claim about the JSON with a false claim about the script. The honest version is one clause shorter: *"(the matched lines are not stored; re-deriving them means re-running the `APPARATUS` regex against the serialized bodies yourself)."*

### P1-A-3. §4's Usage Guidance denominator was replaced with a false statement about the corpus. `Usage Guidance` appears in zero lexicon chunks.

Previous text (correct, merely ambiguously placed): *"comparable to Usage Guidance's 20 of 60."* This re-check's P2-9 asked for four words — "20 of 60 **story** files." The replacement:

> *"comparable to Usage Guidance (20 files — **a section that appears in both chunk types, so it takes no single denominator**)."*

Counted across the whole corpus: `Usage Guidance` appears in **60 of 60 story chunks and 0 of 118 lexicon chunks**. And all 20 flagged files carry it as a story section (`Counter({'story': 20})` from the committed JSON). The section does *not* appear in both chunk types; it takes a perfectly good single denominator, which is the one the document just deleted.

This is strictly worse than the defect it fixed: a correctly-stated rate (20/60 = 33%, genuinely comparable to Ecological Function's 33/107 = 31%) was replaced by no rate at all plus a false premise. Restore the number and add the missing word.

### P1-A-4. §8's own preamble says these are decisions that must not happen "by default." New question 9 installs a default architecture. The contradiction is verbal and sits four lines apart.

§8's heading paragraph, **unchanged**:

> *"Decisions this Research stage deliberately does NOT make, **listed so none happens by default**:"*

New question 9:

> *"Design evaluates **making the records the authored artifact and the deployed prompt a deterministic assembly from them** as **the default architecture, not one option among several**."*

Item 9 is not an open question and does not pretend to be — it is Mark's 2026-08-08 direction, correctly labelled as such in its own first line, and it belongs in the document. But it is filed inside a numbered list whose header promises the opposite, and it is the only item in the list that fixes a starting position rather than leaving one open. Items 1–8 all read *"Design decides X"*; item 9 reads *"X is the default; Design evaluates it."* A Design reader scanning §8's header and then item 9 gets two opposite signals about whether the architecture is settled, in the one place where the answer has real consequences for what Design builds first.

Round 3 and Round 5 on the brief both rated this same shape — a directive filed under a header that disclaims directives — as blocking. It is milder here because item 9 self-labels its provenance. **Fix**, one of three, all cheap: retitle §8 (*"Open questions and standing directions handed to Design"*), or move item 9 above the numbered list as a framed direction with the list renumbered back, or add one clause to §8's preamble: *"…listed so none happens by default — with the exception of item 9, which records a direction already given rather than a question left open."*

---

## P2 (addendum)

1. **The instance miscount was suppressed at one site and left at the other.** §5.3 now reads *"on top of the prior instances P3 lists"* (the count simply deleted), but §1 P3 still reads *"This session's live probes added **the fifth** and sharpest instance"* against a list that enumerates **five** numbered items — it is the sixth. Same half-application shape the original finding described; the fix took the site the finding quoted and not the site it named.

2. **The bare cross-document pointer this re-check named explicitly was not fixed, and a redundant duplicate was added beside it.** §3.1 line 347 still reads *"The Albina decision the brief reserves for Design **(§6 Objective 3)**"* — the exact bare pointer P2-1 flagged. Three lines below, the commit inserted a *second* reference to the same objective, this one prefixed: *"the unresolved values decision (**brief §6 Objective 3** — shorten her sentences…)."* So the document now names the same brief objective twice in one bullet, once bare and once prefixed. The other three named pointers were fixed correctly (§0's `the brief's §8`, `the four studies the brief's §3 names`, §8's `per the brief §9's mandate`). At least three further bare pointers to the *brief's* §5 remain unswept (lines 33, 63, 266 — *"Every §5 code/prompt claim,"* *"with §5's bug-level findings,"* *"none reverses a §5 finding"*), each of which resolves to a different section in this document. Neither this re-check nor the fix caught those; noting them so the next sweep is complete rather than a fourth partial one.

3. **"Matches file-for-file" overstates the Round-4 distribution match by one world.** New §4 text: *"Round 4's 17-chunk uncovered-set distribution **matches file-for-file**."* Round 4's table is Desert 9 / Alexandria 5 / IJC 3 = 17; the instrument gives Desert 9 (the same 9, `World Meaning` 7 + `Distortion Risk` 2), IJC 3 (the same 3), Alexandria **6** in `World Meaning` = 18. Round 4 never lists the Alexandria filenames, so a file-for-file claim is not checkable for that row and is numerically off by one. This re-check's own wording was *"reproduces almost exactly… Alexandria 6 against Round 4's 5"*; the restatement dropped the qualifier. Write *"reproduces exactly for Desert and IJC and to within one file for Alexandria (6 here against Round 4's 5)."*

4. **"The Research evidence assembled above already argues each piece" is true for three of the five pieces and false for two.** `probe_parity`'s 4-of-6, the enforcement-at-assembly-time argument (P3 + §3.1 + §4), and Objective 5's world-#7 point are all genuinely assembled above. But **the assembler's existence and its Desert-only staging scope appear nowhere above** — §4's only mention of `permanent_prompt.py` is its docstring's exclusion set — and **the `wrs/` lockstep requirement is never stated in this document at all** (it lives at `brief:297`). Both claims are true; I verified the assembler by reading the file. They are new facts presented as a recap, which is the framing that stops a reader from checking them. Say "verified this session" for the assembler and prefix the lockstep requirement to the brief.

5. **The record-type enumeration omits `force`, the third-largest record class.** *"plus term/story/gravity/contested_claim/figure/demonstration/voice_profile/world_core records."* All eight named types exist and are populated in all six worlds. So do three unnamed ones: **`force` (10–18 records per world**, larger than `gravity`, `contested_claim`, `demonstration`, `figure`, `voice_profile` or `world_core` in every world), `quote` and `search_record`. Since the point of the sentence is that the record layer is rich enough to assemble from, understating it is self-defeating; add `force` at minimum.

6. **§8 question 9 sends Design to §7 for an instrument §7 says does not exist.** *"the assembled output must pass the same instruments this stage built (§7 — the probe battery, output readability, **the naturalness rubric traits**, the sustained-disagreement probe when built)."* §7's own Objective-3 row says the naturalness-rubric checklist is a **candidate** for an instrument that does not exist, and the sustained-disagreement row (added by this same commit) says the same. The parenthetical's "when built" covers the second; the first is stated as though §7 already carries it. Extend the qualifier: *"…the naturalness rubric traits and the sustained-disagreement probe, both when built."*

7. **§4's added-pattern-classes list is now accurate but incomplete.** *"this instrument's added pattern classes (strand codes, Reciprocity/template references) account for part of the remaining difference."* Decomposed per class, the files flagged **only** by classes absent from Round 4's tighter definition are six: `pahclex005` (strand), `ijclex010` (strand), `syrlex005` (Reciprocity), `syrlex008` (Reciprocity), and `pahclex010` and `alexlex011` — both on **CT tags**, a class the sentence does not name. Hedging to "part of" makes the statement true; adding "CT tags" makes it complete, and costs two words.

---

## What verified clean this addendum (re-derived, not trusted)

**The two-stage instrument, end to end.** `python3 leak_audit_instrument.py` → `broad_screen_files: 172`, `apparatus_files: 104`, `apparatus_files_lex: 58`, `apparatus_files_story: 46`, section hits 152 / 44 / 36 / 31 / 28 / 14, files-by-section 45 / 33 / 20 / 17 / 8, per-world rates 0.81 / 0.74 / 0.67 / 0.61 / 0.55 / 0.26 — and `git status` clean afterward. Set-level check against the pre-`598f69c` broad instrument: the two definitions of "flagged" (hits-or-markerless vs hits-only) select **the same 172 files**, so Stage 1 is a faithful restoration, not a number reverse-engineered to match prose.

**Docstring and §4 against the code, class by class.** `BROAD_PATTERNS` (15 regexes) contains `tier meta-language`, `scholar`/`historian`/`academic`/`modern hearing`, `see … below/above`, `Confidence: Inferential|Attested|…`, `FLAG-\d+`, `front-matter`, `Construction Framework` — matching the docstring's and §4's new Stage 1 description. `APPARATUS` contains gravity codes and named gravities (Tensional / Primary / Supporting), `Doc_0\d`, `Force \d[A-C]`, `Strand [A-C]`, `Final Assembly Instruction`, `L4-Templates`, `per Template`, `CT tag`, `Contest Type`, `Reciprocity Note`, `builder notes?`, `No brackets` — matching the new Stage 2 description, with no tier pattern. The no-marker list is computed in `serialized_lexicon` at line 101, outside both pattern stages, as both texts now say.

**The remaining ten of this re-check's twelve findings landed correctly**: the Round-4 reconciliation rewrite (P1-2), the §1 P2 → §7 pointer, now resolving to a real **Sustained-disagreement probe** row (P2-2); §9's *"violating its own file's bridge-first instruction… with the reading floor exceeded as a proxy"* (P2-3); §3.1's Yausep bullet, now correctly scoping finding D to output and naming the artifact difference (P2-5); §5.1's regex-miss diagnosis, now *"a present-tense, true-referent sense-clarification… not among the committed patterns, which target other constructions"* (P2-6); §7's three new rows with Status and What-it-measures un-swapped (P2-7); §2.1's Theon note, quoting `alex_…Theon.txt:45` accurately (*"read with, not to lecture… two travellers over one text"* — verbatim against the file, with an honest elision) (P2-8).

**§8 question 9's sourcing**, item by item: `wrs/views/permanent_prompt.py` hardcodes `desertcore001`, `desertvoice001`, `world_id: "desert-monasticism"` and writes only into `wrs/views/staging/desert_world/`; its docstring carries both the exclusion set and *"Deterministic: same records -> byte-identical outputs."* `brief:297` carries the lockstep requirement verbatim. `brief:611-637` carries *"Objective 3 carries exactly as much weight as Objective 4, not less"* and the "two parallel, non-negotiable priorities" framing. `brief:645` carries Objective 5's world-#7 clause. Twelve record subdirectories exist per world, all eight named ones populated in all six.

**Renumbering and stage-scope claims.** Two `question N` references in the whole document, both correct after renumbering. `git diff --stat f4c15c8~2..HEAD -- cic-poc/`: two files, both new probe artifacts — §0's "nothing in any voice file, capsule, or pipeline was changed this stage" is exactly true.

## Addendum fix list

1. `26–41` → `26–76`, with the per-world list. **(P1-A-1)**
2. Rewrite caveat (1)'s parenthetical to stop claiming the instrument emits lines. **(P1-A-2)**
3. Restore "20 of 60 story files" and delete "appears in both chunk types." **(P1-A-3)**
4. Reconcile §8's preamble with item 9 — one clause, three equally good options above. **(P1-A-4)**
5. Sweep the seven P2s; items 1 and 2 are one-word edits at sites already named twice.

Three of the four P1s are single-sentence repairs to sentences written in the last two commits, and none of them touches a measurement — the measurements, including the two that this thread spent two rounds on, are now correct and reproducible. **The document is one short editing pass from ready. A fourth adversarial pass is not warranted; whoever makes these edits should re-read §4's caveat and §8's preamble once against the code and the header respectively before committing.**

---

*Simulated review — informational only, not an Article 31 substitute.*

---

# Addendum 2 — final verification and stage verdict, 2026-08-08 (commit `2734c0a`)

*Narrow scope: the commit applying this addendum's 4 P1s and 7 P2s. Every replacement fact re-checked against the source I derived it from, not against the addendum's own wording; every fix grepped at every site it was supposed to reach; the whole document re-swept for pointer resolution and for contradictions with unchanged text; the instrument re-run; §3.1's six prompt-file readability numbers re-derived from scratch this pass rather than carried on Round 1's authority.*

## Did every finding land?

**Yes — eleven of eleven, at every site, with one wording residue.**

| Finding | Landed | Verified against |
|---|---|---|
| P1-A-1 record counts | ✓ | *"26–76 source records per world — PAHC 76, Syriac 64, IJC 41, Alexandria 37, Desert 26, Hieronymian 26"* — matches my `find` counts world-for-world, no transcription drift |
| P1-A-2 matched lines | ✓ | *"matched line text is not stored anywhere (the committed regex and corpus make the matches recomputable, but the instrument as committed does not emit them)"* — true of the code; the false capability claim is gone |
| P1-A-3 Usage Guidance | ✓ | *"20 of 60 story files (the section appears only in story chunks; all 20 flagged files are story files)"* — matches the corpus count (0 of 118 lexicon, 60 of 60 story) and the committed JSON's `Counter({'story': 20})` |
| P1-A-4 preamble conflict | ✓ (body) | *"as the first candidate architecture — a direction set by Mark, with the adopt/adapt/reject decision still Design's to make and record explicitly, consistent with this section's rule that no decision happens by default."* "Not one option among several" is gone; §8's header and the item now agree |
| P2-1 instance count | ✓ | §1 P3 now reads *"the sharpest instance yet"* — the count dropped rather than corrected, which is the right call for a list that may grow |
| P2-2 bare pointers | ✓ | Complete sweep this time: `brief-§5` at lines 33/63/266, `(brief §6 Objective 3)` at 347 with the redundant duplicate removed. **Whole-document re-extraction: every remaining bare `§N` resolves inside this document.** The cross-reference defect that ran through four passes is closed |
| P2-3 Alexandria one-file | ✓ | *"the per-world distribution matches within one file (Alexandria counts 6 here against Round 4's 5, whose filenames Round 4 did not list)"* — exactly the qualification I derived |
| P2-4 "assembled above" | ✓ | Now *"most in this document's own findings, two directly against the brief and its review rounds"*, with the assembler sourced to *"the brief's §7 Part A correction, re-verified this stage"* and the lockstep to *"(brief §4.2)"* |
| P2-5 record types | ✓ | `term/story/gravity/force/contested_claim/figure/demonstration/quote/search_record/voice_profile/world_core` — all eleven non-`source` subdirectories, matching the twelve I counted on disk |
| P2-6 §7 instruments | ✓ | *"the §6 rubric traits once built into an instrument per §7's named Objective-3 gap, the sustained-disagreement probe when built"* — no longer claims §7 carries an instrument it says is missing |
| P2-7 CT tags | ✓ | *"(strand codes, CT tags, Reciprocity/template references)"* — CT is the class behind 2 of the 6 only-added-class files |

**Two new citations introduced by this commit, both checked, both correct.** *"the brief's §7 Part A correction"* for the Desert-only assembler: brief §7 Part A runs from line 760, and line 794 opens *"**One real correction about the source records above, not a restatement: `wrs/views/permanent_prompt.py` does not currently assemble the deployed prompt**"* — it is a correction, it is in §7 Part A, and it carries the staging file, the Desert hardcoding and the `DELIBERATELY TEMPORARY` markers verbatim. *"(brief §4.2)"* for the lockstep requirement: §4.2 spans lines 207–358 and the requirement is at line 297. Both resolve exactly.

**No misquoted counts. No new contradiction with unchanged text.** I re-resolved every `§N` pointer in the document and re-read every site the commit touched against its neighbours. The one thing this commit could have broken — §8's preamble — is now the thing it explicitly reconciles.

**One residue, P2-grade, named for honesty rather than for action.** §8 item 9's **bold title still reads "Record-sourced assembly as the *default* architecture to evaluate"** while its body now says "the first candidate architecture." The body carries the reconciliation and the title carries "to evaluate," so nothing false is asserted and the preamble conflict is genuinely resolved — but a reader skimming titles gets the older word. Two other editorial residues in the same class: §4's reconciliation says *"What does reproduce exactly:"* and then lists something that *"matches within one file"*, and states the Round-4-examples claim twice in one sentence. All three are copy-edits, not corrections. None changes a fact, a number, or an instruction to Design.

## Independent re-derivation this pass

`leak_audit_instrument.py` re-run: `git status` clean, `broad_screen_files: 172` and `apparatus_files: 104` both emitting from one execution. §3.1's six prompt-file numbers re-derived from scratch by importing `wrs.gates.core.readability_check` — Theon 6.16/78.92, Chloe 6.81/74.89, Albina 9.26/65.42, Papnoute 9.74/62.38, **Yausep 10.01/65.05 with `['FK grade 10.0 > 10.0']`**, **Marius 11.56/59.84 with both violations**. Every cell matches the table, and the "two failing prompt files" finding — the third P0 of Round 1 — is confirmed by the gate itself rather than by any prior pass's report of it.

---

## Bottom line for the whole document, per the Standard Practice's point 6

**Ready for Mark's stage sign-off.**

Stated as plainly as point 6 requires, and not softened because this is the fourth pass on the same artifact: **there is no P0 anywhere in this document, no P1 anywhere in this document, and every claim that four passes have put in question has been taken to primary source and reproduced.** Every finding raised across Research Round 1 (3 P0, 6 P1, 10 P2), this targeted re-check (3 P1, 9 P2) and its addendum (4 P1, 7 P2) — **42 findings** — is closed. What remains is three copy-edits.

The specific things a Design reader can now rely on, each re-derived by this reviewer rather than accepted:

- **The leak audit is fully reproducible.** One committed script, two real stages, `172` and `104` from the same run, a byte-identical JSON on regeneration, and a prose description that matches the code class-for-class. This was the defect that blocked the document at Round 1; it is not merely patched, it is the strongest instrument-provenance position anything in this thread has held.
- **Every measurement reproduces**: the twelve-file readability table (re-derived this pass), the per-turn probe measures, the invisible-call rates, the bridge-first counts, the section and per-world leak figures, the corpus denominators, and the record-layer counts behind the new architecture direction.
- **Every correction to the brief holds at source**, including the four per-world turn ceilings that the first two passes got wrong in two different ways.
- **Cross-reference integrity is clean** for the first time in this thread's history: every bare `§N` resolves inside this document, every cross-document pointer is prefixed, and the two renumbered pointers both land.

**What Mark should know is still open — not defects, but things the document itself names as unclosed**, and which sign-off endorses rather than resolves: Objective 3's positive goal still has no instrument (§7, §8(d)); the sustained-disagreement probe does not exist (§7); four rubric traits remain egress-blocked (§8(a)); `mark_voice_simulation_results.json` is still uncommitted, so brief finding C's four claims rest on the Decision Log and brief alone (§8(c)); and §8 item 9 records a direction from Mark whose adopt/adapt/reject decision is Design's. Each is disclosed in the document in the right place, which is the condition that makes sign-off honest rather than optimistic.

**A further adversarial pass is not warranted and would not be a good use of the tier.** The pattern across four passes is now unambiguous and worth recording for the Design gate's dispatch: **quotations and deletions held on first application every time; new prose asserting a replacement fact, a causal explanation, or a description of what a script does failed on first application every time, and roughly half the time on second application too.** Design's dispatch should aim its skepticism at exactly that class — and at nothing else, because everything else in this thread's history has held.

---

*Simulated review — informational only, not an Article 31 substitute.*
