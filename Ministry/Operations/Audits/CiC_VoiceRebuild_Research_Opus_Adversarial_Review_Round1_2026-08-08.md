# Adversarial review (round 1): `CiC_VoiceRebuild_Stage1_Research_Findings_2026-08-08.md`

*Opus review, dispatched 2026-08-08. This is the Stage-1 (Research) gate required by the brief's §9 — the pass that decides whether Design is allowed to build on this document. Per the Standard Practice's point 4, the brief (`Ministry/Features/Front-End-Integration-Strategy/CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`) and the eight prior review artifacts (`..._Round1_2026-08-06.md` through `..._Round5_2026-08-07.md`, plus the three targeted re-checks) were read before any new hunting began, so this round is aimed specifically at what has never been checked.*

*Named failure mode hunted, per point 5, in the form this thread's own history has established: **newly-written positive prose reliably contains new errors, at roughly one P0 per 350–500 words, and the errors cluster in the sentences that assert a replacement fact or a new measurement.** This document is 5,604 words and is almost entirely new positive prose. It also introduces a second, sharper risk class the brief never had: **committed instruments whose output does not match what the prose says they produced.***

*Verification method. Every number in §3.1's twelve-file table re-derived by importing `wrs.gates.core.readability_check` and running it against the twelve named files. `leak_audit_instrument.py` executed end to end and its output diffed against `leak_audit_apparatus_hits.json`. `voice_rebuild_research_probe_results.json` parsed directly — every per-turn measure recomputed from `turn_analyses`, every quoted transcript line matched against the stored `transcript`, usage records tallied by label and by model. `voice_rebuild_research_probe.py` read at `analyze_turn`, `RECLARIFY_PATTERNS`, `TECH_TERMS` and `UsageCapture`. All six committed `*probe_parity_result.json` files parsed. `CiC_L1_Constitution_V2_2.docx` extracted fresh from `word/document.xml` and read at Article 30. All six permanent prompts and both `wrs/records` gates read at every cited line. `representative_prompts.py`, `nodes.py`, `repair_classifier.py`, `facilitator_prompts.py`, `sections.py`, `story_indexer.py`, `story_retriever.py`, `retriever.py`, `indexer.py`, `over_settling_logging.py`, `state.py` and `probe_parity.py` read at every cited line number. Docs 07, 09, 10 and 16 read at every quoted phrase. `arxiv.org` reachability tested directly. All 43 internal `§N` pointers extracted programmatically and resolved by hand.*

---

## Bottom line

**Not ready. Design must not build on §4 as written.**

A great deal of this document is genuinely excellent, and I want to say what survived before saying what didn't, because the failures are narrow and the successes are not. **All twelve readability numbers reproduce exactly** — I re-ran the gate against the twelve named files and got 6.16 / 6.81 / 9.26 / 9.74 / 10.01 / 11.56 for the prompts and 7.83 / 7.54 / 9.61 / 11.54 / 12.48 / 13.27 for the capsules, matching every cell. **The Article 30 correction is exactly right** — I extracted the Constitution myself: Article 30 is "Three-Level Transparency," the three levels are "the formation conversation itself, an on-request reference explanation, and the full scholarly apparatus," and the words *inline*, *hover* and *click* appear **nowhere in the document**. **The probe-parity reading is exact** — parsed from the six committed result files, world for world, with the verdict rule confirmed verbatim at `probe_parity.py:18`. **Every per-turn probe number I could recompute is correct**, including the ones easiest to fudge: mean 19.7 w/s (mean of per-turn, 19.738), FK 10.5 and 11.45 on turns 2 and 4, turn 7 at FK 4.76 / 15.8 w/s, Papnoute's 1.38–6.65 FK band and 42–187 word range against Yausep's 158–342, over-settling at 6/8 and 3/8, `fabrication_adjudication` on Papnoute turn 7 and nowhere else. **Every quoted transcript line is verbatim**, including "You will hear me return to it here" and Papnoute's refusal. **The 8 Final-Assembly files and the 6 markerless chunks reproduce** — I re-ran the instrument and got the same six filenames, and confirmed by executing the story path that `ijcstory001`'s serialized body really does end with "No brackets or builder notes remain." Twenty-nine of thirty-one file/line citations are exact. The §6 egress claim is honest: `arxiv.org` returns 403 at the proxy from this environment.

But **three send-blocking defects remain**, and they fall exactly where the standing rule predicts — in the sentences that assert a new measurement or a replacement fact.

- **The committed leak-audit instrument does not produce the committed leak-audit results.** §0 says "Instrument and raw results are committed beside this document"; §4 says "Every count below is from the committed instrument." Neither is true. Running `leak_audit_instrument.py` yields `files_flagged: 172`, a per-pattern hit structure, and a `kind` vocabulary of `lexicon`/`story`. `leak_audit_apparatus_hits.json` contains 104 files, a per-section count structure, no pattern labels, no hit lines, and `kind` values of `lex`/`story`. **Every headline number in §4 — the 104/178, the six section counts, the six per-world counts — comes from a script that is not committed**, and the one script that *is* committed contradicts the headline by 68 files.
- **§2's turn-length correction repeats the error it corrects.** It says deleting the shared ceiling "would leave Papnoute, Theon, and Marius" ceiling-less. Papnoute's permanent prompt carries the **strictest** turn ceiling in the corpus at `:13` — "Hold to this as a hard measure, not a preference: four sentences is already long for you, and most of what you say should be one to three." §8's open decision 2 is built on the false enumeration.
- **§3.1 contradicts its own table two rows above it.** "Marius's prompt is the only failing prompt file" — the table records Yausep at FK 10.0, verdict "fail (FK at line)" (measured 10.01). §9's Bottom Line repeats the claim. Yausep is one of the brief's three named acceptance worlds and the subject of §5.1.

Six P1s follow, four of which are instrument overclaims in §7 — the 209-word section that carries the entire weight of the brief §8 falsifiability discipline and is the shortest section in the document.

**Cross-reference integrity: 43 internal `§N` pointers. 41 resolve. One does not resolve at all** — P2's "(§7's sustained-disagreement probe)"; §7 contains no such row. Two resolve to the *brief's* section of that number rather than this document's, unlabelled.

**Completeness map, counted both directions.** Brief §9's Research mandates: (a) Yausep first — **delivered**; (b) Papnoute second — **delivered**; (c) `readability_check` — **delivered and sharpened**, honestly partial where the rebuilt prompt does not exist; (d) the Albina `fabrication_adjudication`/Objective-2×4 interaction — **not delivered** (used once as evidence for P3, handed to Design as nothing). Review-round Research assignments: Round 3's code-side-vs-prompt-side leak question — **delivered** (§8.4); Round 3's circularity/callback mechanism — **delivered** (P6); Round 2's 16-trait adaptation — **delivered, honestly partial**; Round 4's "name Papnoute, the world with the highest leak rate" — **not delivered**; Round 4's Objective-3 positive-goal instrument hole — **not delivered**.

**Balance ratio, counted.** 5,604 words. Framing and principles (§0, §1, §9) **2,187 = 39.0%**. New measurement (§2–§6) **2,750 = 49.1%**. Actionable handoff to Design (§7 instruments + §8 open questions) **667 = 11.9%**. The measurement half is healthy and is what makes this document worth the pass. The 11.9% is thin for the thing Design actually consumes, and §1 alone — 1,613 words, 29% of the document, and the newest, least-checked positive prose in it — is nearly two and a half times the size of everything handed forward.

None of the three P0s is a writing problem. The first would send Design to build a filter against numbers nobody can reproduce; the second would let Design delete a live turn ceiling on the belief it is deleting nothing; the third would tell Design that five of six prompt files pass the accessibility gate when four do.

---

## P0 — fix before this document gates Design

### P0-1. `leak_audit_instrument.py` does not produce `leak_audit_apparatus_hits.json`. Re-running the committed instrument flags 172 files, not 104 — and every §4 headline number comes from a script that was never committed.

§0, method bullet 2:

> *"**The chunk leak audit was executed through the app's own serialization path** (`parse_lexicon_file`/`parse_story_file` → `truncate_at` → `excise_section`), not by grepping raw files. Instrument and raw results are committed beside this document (`leak_audit_instrument.py`, `leak_audit_apparatus_hits.json`)."*

§4, method paragraph: *"**Every count below is from the committed instrument**; flagged lines were sampled and classified by hand."*

I ran the committed instrument. Its output:

```
{"lexicon_total": 118, "story_total": 60, "files_flagged": 172,
 "lexicon_no_key_sources_marker": [pahclex012, pahclex013, syrlex005,
                                   syrlex008, ijclex011, ijclex012],
 "hits_by_pattern": {"modern_scholars": 170, "doc_apparatus": 76,
                     "gravity_apparatus": 63, "see_reference": 39,
                     "template_language": 17, "ct_tags": 10, "builder_notes": 8,
                     "tier_meta": 7, "reciprocity_note": 2, "omitted_per": 2,
                     "construction_framework": 1, "candidate_tested": 1}}
```

Its `flagged` array carries per-file records of the shape `{file, kind, world, no_key_sources_marker, serialized_chars, hits:[{pattern, line}]}`, with `kind` ∈ {`lexicon`, `story`}.

The committed JSON carries records of an entirely different shape:

```
"desertstory001_antonys-call-matthew-19-21.md": {
  "world": "desert_world", "kind": "story",
  "sections": {"Formation Ecology Connection": 5, "Usage Guidance": 1}}
```

104 files, `kind` ∈ {`lex`, `story`}, **per-section counts**, and **no pattern labels, no matched lines, no `no_key_sources_marker` field, no `serialized_chars`**. The committed instrument emits none of that and computes no section attribution at all — `scan()` records only `(pattern, line)` pairs.

So: the JSON was produced by a different script, with a different (narrower) pattern set and an added section-attribution pass, and **that script is not in the repository**. Every §4 headline traces to the JSON, not to the instrument:

| §4 claim | Source |
|---|---|
| 104 of 178 (58%) | JSON file count — confirmed 104 |
| FEC 152 / EF 44 / WM 36 / UG 31 / FAI 28 / PVN 14 | JSON section sums — confirmed exactly |
| Alexandria 33 (23 lex + 10 story), PAHC 21, Syriac 14, Desert 17, IJC 12, Hieronymian 7 | JSON world counts — confirmed exactly, and they sum to 104 |
| 8 Final-Assembly files | JSON — and independently reproducible from the instrument |
| 6 markerless lexicon chunks | Instrument — reproducible |

The arithmetic is internally consistent and I could not falsify any individual number *within the JSON*. That is not the problem. The problem is that the audit's central quantitative claim is **unreproducible from anything committed**, and the artifact that *is* committed and named as its source gives a materially different answer (172, or 97% of the corpus) because it also flags any use of "scholar," "academic," "modern reader," and "see … below."

Two consequences compound it:

- **§4's caveat (1) is false as written.** *"every pattern class was hand-sampled and the per-file JSON is committed for full inspection."* The JSON contains section names and integers. There are no lines in it. A Design reader cannot inspect a single flagged string.
- **§4's caveat (2) promises a separation the committed artifact cannot support.** *"Some flagged material is deliberately serialized and participant-safe in content while apparatus-flavored in register (e.g. 'Contested.' confidence labels); the committed JSON preserves section attribution so Design can separate the two."* Section attribution alone does not separate them — you need the matched text. The JSON has the attribution and not the text.

**Why this blocks.** §4's own conclusion is that the leak has "two structurally different halves," that the 104-file half is "a chunk-authoring / field-form problem," and that a prompt-side filter "cannot fix the first half." §8 decision 4 hands Design the sequencing of that fix, and §9's Bottom Line makes the filter "load-bearing, not hygienic." All of that rests on a number Design cannot re-derive and an instrument that, run as committed, says something else. This is the same class as round 2's finding on the brief — a claimed data pool that did not survive opening the actual files — except here the pool exists and the *instrument attribution* is what fails.

**Fix.** Commit the script that actually produced `leak_audit_apparatus_hits.json`, with its pattern list, and make it the named instrument in §0 and §7. Either extend it to emit the matched line per hit (so caveats (1) and (2) become true), or delete both caveats' claims about inspectability. Then reconcile the two instruments explicitly in §4: state the narrow pattern set's count (104) and the broad set's count (172), say which one the 58% headline is, and say plainly that `modern_scholars` and `see_reference` are the two classes that separate them. If `leak_audit_instrument.py` is superseded, remove it rather than leave a committed script that contradicts the document beside it.

---

### P0-2. §2's turn-length correction is itself an incomplete enumeration asserted as complete. Papnoute carries the strictest turn ceiling in the corpus, and §8's open decision 2 is built on the claim that he carries none.

§2, correction 1:

> *"`_HOW_YOU_ENGAGE`'s 'A Turn Has a Measure' is the only shared ceiling, not the only ceiling. This changes the shape of the open turn-length decision (§8): **deleting the shared ceiling would not leave Albina/Chloe/Yausep ceiling-less, but would leave Papnoute, Theon, and Marius so** — and the per-world ceilings are themselves in the files being rebuilt."*

`data/desert_world/desert_Representative_Permanent_Prompt_Papnoute.txt:13`, verbatim:

> *"The word we gave was short… **Hold to this as a hard measure, not a preference: four sentences is already long for you, and most of what you say should be one to three.** This holds exactly as much when the question is heaviest, the company is hardest, or another elder in the room has spoken at far greater length…"*

That is a hard, explicit, per-world turn-length ceiling — tighter than Albina's "rarely runs past two short paragraphs," tighter than Chloe's "stops at two short paragraphs," tighter than Yausep's "two or three short paragraphs at the very most," and phrased in the *identical* "hard measure, not a preference" formula as Albina's. It is not a sentence-length rule; §5A's Papnoute quote (`:7`, "Your sentences stand next to each other") is the sentence-length rule and sits six lines earlier in the same file. The document quotes `:7` in its own §2.4 list of verified register quotes and did not look six lines down.

Theon and Marius check out — `alex_…Theon.txt:37` and `ijc_…Marius.txt:117` are genuinely sentence-shape rules with no turn ceiling. So the correct statement is "would leave **Theon and Marius** ceiling-less," and the correct count is **four** per-world ceilings, not three.

**A second miscitation inside the same correction.** *"Albina — 'a turn of yours rarely runs past two short paragraphs' (`hal_…Albina.txt:29`)."* That sentence is at **line 27**. Line 29 is the periodic-rhythm paragraph ("Your sentences run the way a trained hand's Latin runs"). The brief's §5A cites `:29` for the *rhythm* claim, correctly; this document reused the brief's line number for a different quote two lines up without re-deriving it — in a correction whose entire premise is that the brief's turn-length account was not checked carefully enough.

**Why this blocks.** §8 decision 2 states the Design question as *"where does the turn-measure live in the rebuilt architecture (shared block, per-world files, or both)"* on the strength of this enumeration. Under the enumeration as written, deleting `_HOW_YOU_ENGAGE`'s ceiling leaves half the fleet with no length discipline at all and Design must invent one. Under the true enumeration, four of six worlds are covered and the real question is narrower and different: whether Theon and Marius should acquire per-world measures, or whether the shared block survives specifically for them. Papnoute is also the world §5.2 uses as the clean-run existence proof — the document argues from his short, paced turns (42–187 words, 8.9–19.7 w/s) without noticing that his file contains the instruction most directly responsible for them.

**Fix.** Correct §2.1 to name four per-world ceilings with Papnoute's `:13` quoted, fix the Albina citation to `:27`, and rewrite §8 decision 2 to the narrower question the true enumeration produces. Then grep the document for its own corrected vocabulary — "ceiling-less," "only shared ceiling," "three per-world" — and confirm zero survivors, per the discipline the targeted re-check established on the brief.

---

### P0-3. §3.1's "Marius's prompt is the only failing prompt file" contradicts §3.1's own table, and §9 repeats it. Yausep's prompt fails the gate.

§3.1's table, as written:

| File | FK | FRE | Verdict |
|---|---|---|---|
| Yausep prompt | 10.0 | 65.0 | **fail (FK at line)** |
| Marius prompt | 11.6 | 59.8 | fail both |

§3.1's second consequence, two paragraphs below the table:

> *"**Marius's prompt is the only failing prompt file** — consistent with finding A's read that his register-and-reasoning-mode entanglement is the deepest per-file rebuild risk."*

§9's Bottom Line, third site:

> *"the accessibility problem in the files is concentrated in **Marius's prompt and three capsules**."*

I re-ran `readability_check` on all twelve files. Yausep's prompt returns `fk_grade 10.01, fre 65.05, violations: ['FK grade 10.0 > 10.0']` — the gate fails it, and the document's own table records that correctly. Two of six prompt files fail, not one.

**Why this blocks.** Yausep is one of the brief §8's three named live-test acceptance worlds; he is the entire subject of §5.1; and §5.1's own finding is that his measured *output* runs a 19.7 w/s battery mean with two turns above FK 10. §3.1's Albina consequence turns on the distinction between file and output ("her *file* is not her problem; her *output* is"). For Yausep, **both** fail — which is a materially different and more useful finding than the one the document draws, and it is the one that §7 Part A's risk-ordered per-world sequence would want. As written, a Design reader who takes the prose over the table concludes Yausep's prompt is inside the band and that only his output needs work.

The failure shape is the one this thread has caught repeatedly: a claim corrected or established in one place (the table) and left standing in falsified form at two other sites (§3.1's bullet, §9's summary).

**Fix.** Rewrite §3.1's second consequence to "Marius's and Yausep's prompts are the two failing prompt files, Marius on both numbers and Yausep at the FK line," and correct §9 to match. Note the second-order finding while you are there: Yausep is the only world in the corpus failing on *both* file and output, which is a stronger argument for his position in the acceptance set than the one §5.1 currently makes.

---

## P1 — materially improves, not disqualifying

### P1-1. §7's instrument table overclaims on two rows and omits the instrument P2 points at. This is the section carrying the brief §8 falsifiability discipline.

Three separate defects in 209 words.

**(a) The over-settling confirmed rate was not reported, and this probe cannot report it.** §7's row: *"`over_settling_logging` confirmed-rate (`app/over_settling_logging.py`) | Existing | Distinct from firing rate; **both reported** for governance evaluation."* Nothing in §5 reports a confirmed rate. It could not have: `voice_rebuild_research_probe.py`'s `UsageCapture` handler filters on `msg.startswith("[llm_usage]")` and is attached to `logging.getLogger("cic.llm_usage")`, while `log_over_settling_decision` emits `"[over_settling_decision] world_id=%s screened=%s confirmed=%s"` on its own logger. The confirmed rate is structurally outside what this session captured — and §8 decision 3 says so itself: *"10-of-12 firing with confirmed-rate unmeasured in that count."* §7 and §8 disagree.

**(b) The reclarify-opener rate the script measures returned zero, and the 1-of-8 is a hand classification the document does not label as one.** §7's row credits the probe with *"reclarify-opener rate (finding C's tally)."* Recomputing from the committed results: `reclarify_opener_patterns` is `[]` on **all sixteen turns across both worlds**. The six `RECLARIFY_PATTERNS` regexes target the false-referent form ("when I said X," "by X I mean"). Yausep turn 2's actual opener — *"When I speak of the qyama, I mean the vow itself"* — matches none of them, and the document is right that it is a genuinely different class (true-referent). But §5.1 states it as **"Unprompted term-reclarification opener: 1 of 8 turns"**, formatted identically to the automated 3-of-8 and 2-of-8 counts beside it, with no note that the instrument scored 0 and a human scored 1. §5.1's parenthetical about the false-referent class appearing "**0 of 8** times" is the regex result; the 1 is not.

**(c) There is no sustained-disagreement probe, and P2 cites one.** P2: *"what no instrument yet measures is whether the position actually holds by the third or fourth push (**§7's sustained-disagreement probe**)."* §7 has nine rows; none is a sustained-disagreement probe. This is the document's only unresolvable internal pointer, and it lands on P2's central falsifiability claim — the one place where the document promises Objective 6 an instrument.

**Fix.** Change (a) to "confirmed rate: existing mechanism, **not captured by this session's probe** — the probe reads `[llm_usage]` only; capturing it needs one more log handler." Change (b) so §5.1 reads "1 of 8 by hand classification; the committed regex set scores this class 0 of 8 and needs a true-referent pattern added before it is a real tally," and change §7's row to match. For (c), either add a sustained-disagreement probe row marked **Still missing — named Design-stage instrument**, or repoint P2 at §8 decision 7 and say plainly that Objective 6 leaves Research with a licence question and no instrument.

---

### P1-2. "Roughly 10–12 invisible calls per visible reply" overstates both the cited source and this session's own captured data — in the paragraph that arms §8's cost argument for cutting live safety mechanisms.

§5.1: *"Roughly 10–12 invisible calls per visible reply, matching `Decision-Log.md:63`."*

The Decision Log says *"~40 real LLM calls each — roughly **ten** invisible calls for every one visible reply"* — and it says it at **line 65**, not 63; line 63 is the "What ran, for real" paragraph. (The brief carries the same `:63` miscitation; §2.4 lists this material among what was "reproduced exactly at the cited locations this session," so the line number was not re-derived.)

This session's own capture, recomputed from `voice_rebuild_research_probe_results.json`:

| World | usage records | `main_response` | invisible per visible reply |
|---|---|---|---|
| Yausep | 71 | 8 | **7.9** |
| Papnoute | 68 | 8 | **7.5** |

So the document's own instrument measured 7.5–7.9, its cited source says ten, and the prose says "10–12." The direction of the error is the one that matters: **upward, on cost, in the sentence Design will read when deciding whether `over_settling`, `citation_grounding`, `drift_detection` and `confirmed_glosses` earn their keep** (§8 decision 3, which explicitly assembles "the cost facts"). Round 5's P0-4 blocked the brief for a ~20× cost overstatement in exactly this argument.

**Fix.** Replace with the measured number: *"7.5–7.9 invisible calls per visible reply in this session's own capture (Yausep 63/8, Papnoute 60/8), against the Decision Log's 'roughly ten' at `Decision-Log.md:65` for a four-turn battery with a different governance mix."* Correct the line number at both sites and, since §2.4 vouches for it, re-check the rest of §2.4's list the same way.

---

### P1-3. The headline "3 of 8" bridge-first violation is measured against a twelve-term list; Yausep's `:45` names three terms. Against the instruction as written the count is 2 of 8.

§5.1: *"**Bridge-first (his own `:45` instruction — 'Let the word follow the story, not stand in front of it'): violated in 3 of 8 turns.** Turns 2, 3, and 4 open with the technical term in the first sentence… **against an explicit, currently-deployed instruction.**"*

`syr_Representative_Permanent_Prompt_Yausep.txt:45`, verbatim:

> *"**Before you reach for raza, qyama, or Iḥidaya as your first word**, ask whether your own record gives you a face, a name, or a scene for this question instead… Let the word follow the story, not stand in front of it."*

The probe's `TECH_TERMS["syriac-edessa-nisibis"]` carries twelve terms: `raza, raze, qyama, ihidaya, iḥidaya, bnay, bnat, madrasha, madrashe, shrara, memra, ewangeliyon`. Turns 2 and 3 trip on `qyama` — named in `:45`, and both openers lead with it flat ("When I speak of the qyama…", "It was about the qyama —"). Those are clean hits. **Turn 4 trips on `madrasha`**, which `:45` does not name, and its opener is *"A teaching-hymn (madrasha) was never one thing only"* — the English gloss first, the Syriac in parentheses, which is arguably the instruction's second clause being obeyed rather than broken.

The document's "3 of 8 violations of the bridge-first instruction" is therefore 2 of 8 against `:45` as written, plus one debatable case against a broader reading of the same principle. Both readings support P3's conclusion; the difference is that 2/8 is a defensible measurement and 3/8 is not, and 3/8 is what §3's P3, §5.1, §5.3 and §9's Bottom Line all carry — the last of them calling it "the stage's sharpest single result."

**Fix.** Report both: *"2 of 8 against `:45`'s own named terms (turns 2 and 3, both `qyama`); a third turn (4, `madrasha`) leads with the term under a broader reading of the same rule but glosses it in English first — counted separately rather than folded in."* Then note in §7 that `TECH_TERMS` is broader than any single world's instruction, so the measure is a bridge-first *proxy*, not instruction-adherence, and Design should not read it as the latter.

---

### P1-4. Round 4 measured this leak by hand and gave Research a named instruction. §4 neither reconciles with that measurement nor applies the instruction, and reports counts where the interesting finding is rates.

Round 4's own leak table (`..._Round4_2026-08-07.md`, lines 200–206): **46 of 118 lexicon chunks** leaking build-process metalanguage — 27 inside `Ecological Function`, 6 markerless tails, **17 covered by neither** — with a per-world distribution and verbatim examples, produced by executing the same serialization path. Its fix instruction, verbatim: *"**Name Papnoute — currently the only world the brief never associates with this leak, and the one with the highest rate**"* (9 of his 18 lexicon chunks).

§4 does not cite Round 4's 46, does not reconcile 58 flagged lexicon files against it, and does not name Papnoute or Desert anywhere. Its per-world bullet reports raw counts and then draws an interpretive conclusion from them:

> *"Per-world (files with ≥1 apparatus hit): Alexandria 33 (23 lex + 10 story), PAHC 21, Syriac 14, Desert 17, IJC 12, Hieronymian 7. No world is clean; **Alexandria's volume is largest in absolute terms (it has 50 of the 118 lexicon chunks), consistent with the brief's Theon-exposure note.**"*

Alexandria holds 60 of the 178 files. Normalising the document's own numbers:

| World | flagged | total files | rate |
|---|---|---|---|
| PAHC | 21 | 26 | **81%** |
| Syriac | 14 | 19 | 74% |
| IJC | 12 | 18 | 67% |
| Desert | 17 | 28 | 61% |
| Alexandria | 33 | 60 | 55% |
| Hieronymian | 7 | 27 | 26% |

Alexandria is fifth of six by rate. The "consistent with the Theon-exposure note" inference is an artifact of corpus size, and the world the audit should be flagging to Design — PAHC, whose capsule is also the worst of the twelve on readability (§3.1) and whose Representative is §7 Part A's *pilot world* — goes unremarked.

**Fix.** Add a rate column to §4's per-world line, cite Round 4's 46/17 measurement and say what the new pattern set adds to it, name Papnoute/Desert per Round 4's instruction, and replace the Alexandria inference with the rate-based one. §9's leak sentence should follow.

---

### P1-5. Brief §9's Research mandate (d) is not delivered. The Albina `fabrication_adjudication` interaction reaches Design as evidence for a different claim and as no open question at all.

Brief §9.1(d), verbatim: *"treat the pilot's Albina `fabrication_adjudication` firing (finding C) as a real open interaction between Objectives 2 and 4, not a one-off."* Brief §5(C) is explicit about why: the Marcella story chunk's own Usage Guidance names an epitaph-genre caveat, the prototype delivered it flat as record, and *"Fable's Research stage should treat this as a real, not hypothetical, interaction between Objective 2 (draw on stories more) and Objective 4 (no fabrication, ever)."*

§0 claims the document covers "the open research tasks the brief and its five adversarial review rounds assigned to this stage." The Marcella finding appears exactly once, as P3's item 3 — used as evidence that the story-context block's genre-caveat instruction "under-held." That is a fair use, but it is a *different* claim from the one the brief assigned. §8's eight open decisions contain nothing about how a lead-with-the-concrete-story instruction is to be paired with carrying a source's own genre caveats; §7's instrument table has no row for it; §8's "Gaps Research names" does not name it.

This matters more than it looks, because the document's own §5.2 supplies live evidence on it that goes unread: Papnoute's turn 7 fired `fabrication_adjudication` on an illustrative scene, and §5.2 reads it as "the system working." That is the Objective-2×4 interaction firing again, in a probe run for a different purpose, and the document treats it as an aside.

**Fix.** Add a ninth §8 open question naming the interaction explicitly — how the §7 Part A lead-with-insight/story instruction is paired with a genre-caveat carry-through requirement, and whether `fabrication_adjudication` firing rate is the right instrument for it or whether it needs a separate genre-caveat check. Cite both the pilot's Albina firing and this session's Papnoute turn 7 as the two live instances.

---

### P1-6. §7 claims to leave behind "what now exists to make every claim falsifiable" and omits the largest known instrument gap in the program.

Round 4 established, and the brief's own §8 still concedes in its `readability_check` bullet, that Objective 3's positive goal has no instrument: *"it tests the accessibility floor, not the objective's actual, positive goal (insight, connection, honesty), which still has no instrument here."* §6 of the brief makes Objective 3 exactly as program-ending as Objective 4.

§7 lists nine instruments and marks three as missing (per-signal drift breakdown, declining-initiative signal, first-sentence uptake tally). Half of the program's stated non-negotiable — insight, connection, depth, honest company — is absent from the table entirely, and §8's "Gaps Research names beyond the brief's reading list" names three gaps, none of them this one. The document's own P1–P7 answer to the governing question is largely *about* this half (P4's insight-organisation, P6's callbacks and candidate understandings, P2's disagreement), so the omission is not that the document ignores the goal — it is that it never says the goal remains unfalsifiable.

**Fix.** Add a row to §7: *"Objective 3's positive goal (insight, connection, honesty) — **no instrument, this stage or any prior one**; the readability gate measures the floor, not the goal (brief §8's own concession). Named as the largest open instrumentation task for Design."* Add it to §8's gap list.

---

## P2 — polish

1. **"reaches the model verbatim in 8 files, not 1."** The brief knew two — `ijclex011` and `ijclex012` — and §4's very next clause says so. Should read "not 2."
2. **The Final Assembly quote is silently truncated.** §4 renders it as *"No brackets or builder notes remain. Tier/Confidence alignment confirmed."* `ijcstory001`'s serialized body continues: *"…confirmed (Tier 1 → Documented at the narrative-existence level)."* Add the ellipsis.
3. **§5.3's "two central voice instructions in 3/8 and 2/8 turns."** The 2/8 is FK > 10 — the project's `wrs/parameters.yaml` reading floor, not an instruction in Yausep's file. His file's instruction is "Each stage is its own short sentence." Call the FK measure a proxy for it, not the instruction itself.
4. **Bare `§N` is used for both this document's sections and the brief's**, 43 times. Two mis-resolve internally: §8 decision 4's *"against §4's content-freeze rule"* (this document's §4 is the leak audit and has no content-freeze rule — the brief's §4 does), and §8 decision 2's *"§7 Part A's rewrite"* (this document's §7 is the instrument table and has no Parts). Prefix every cross-document pointer with "the brief's," as §0, §2 and §7's header already do.
5. **§6's trait table numbers response-length restraint "12"**, in a `#` column otherwise carrying the paper's own indices, while the prose says it is "near-certainly one of the missing five." Mark it `—` or `(unnumbered)`.
6. **P6's callback finding drops its source's confidence label.** `10_…_Realness_Study:47` carries *"(Medium confidence — one strong practitioner account, corroborated by academic literature)"*; P1 and P2 both carry their labels, P6 does not, and P6 calls the mechanism "the cheapest circularity mechanism" and "the concrete mechanism Objective 1's circular half was missing."
7. **"It occurred with all live guard layers present"** (§5.1) is inferred, not logged. The probe does not record whether `retrieved_context` was non-empty, and layer 1 is present only `if retrieved_context:` (`representative_prompts.py:168`). The inference is well-supported — `negative_condition_lexicon` and `citation_grounding` both fired on turn 2 — but turn 2 resolved zero citations, so say "inferred from the retrieval-guard usage labels" rather than asserting presence.
8. **§3.1's "the only real callers"** is now one caller short of its own session: `voice_rebuild_research_probe.py:110` imports `readability_check`. Not a wiring to voice, but the enumeration is stated as current.
9. **"the two worst-contaminated fields in the corpus"** holds on raw hit counts (152 / 44). By files affected it is less clean: `Formation Ecology Connection` 45 of 60 story files, `Ecological Function` 33 of 107 lexicon files, `Usage Guidance` 20 of 60. The story field is decisively the worst; the lexicon field is comparable to `Usage Guidance`. Report both denominators.
10. **§3.2 is a one-line stub pointing at P7.** It is honest about being one, but it means the document's "two load-bearing system facts" section is half a cross-reference. Either fold it into §3.1's heading or give it the two sentences that make it readable standalone.

---

## What verified clean

Everything below I re-derived independently this round, not by trusting the document's own account of it.

**§3.1's twelve-file table — every cell.** Re-ran `wrs.gates.core.readability_check` against the twelve named files: Theon 6.16/78.92, Chloe 6.81/74.89, Albina 9.26/65.42, Papnoute 9.74/62.38, Yausep 10.01/65.05, Marius 11.56/59.84, Alexandria capsule 7.83/74.10, Syriac 7.54/71.81, Desert 9.61/66.35, Hieronymian 11.54/58.96, IJC 12.48/57.22, PAHC 13.27/56.09. Every rounded value matches. Albina is genuinely third-most-accessible of the six; three capsules genuinely fail both numbers; PAHC genuinely is the worst of twelve and Chloe genuinely is the second-plainest prompt.

**The Article 30 correction, in full.** Extracted `CiC_L1_Constitution_V2_2.docx` from `word/document.xml`. Article 30 is titled "Three-Level Transparency." Its text: *"The architecture presents its reconstruction at three levels — the formation conversation itself, an on-request reference explanation, and the full scholarly apparatus."* A case-insensitive search for `hover`, `click` and `inline` across the whole extracted document returns **zero hits**. The correction is exactly right, including its scoping note that the point is immaterial to this thread's scope.

**Probe-parity, world for world.** Parsed all six committed `*probe_parity_result.json`: Desert `parity: PASS, failing_both: 0`; PAHC `PASS, 0`; Alexandria `FAIL, 2`; Hieronymian `FAIL, 1`; IJC `FAIL, 1`; Syriac `FAIL, 2`. Exactly as §P7 states, counts included. `probe_parity.py:16-18` confirms the four graded dimensions (register, measure, refusal behavior, vocabulary), the two trials, and the verdict rule verbatim: *"parity holds if no probe gets DIFFERENT-VOICE on both trials."* Albina, Marius and Yausep are indeed the three failing acceptance worlds.

**Every recomputable probe number.** From `turn_analyses`: tech-term-in-first-sentence true on turns 2, 3, 4 only (3 of 8); FK > 10 on turns 2 (10.5) and 4 (11.45); per-turn w/s mean 19.738; turn 7 at FK 4.76, 15.8 w/s; Papnoute all-false on every failure measure, FK 1.38–6.65, 8.9–19.7 w/s, 42–187 words against Yausep's 158–342; `over_settling_adjudication` on Yausep turns 1,2,3,4,5,8 (6 of 8) and Papnoute turns 2,3,5 (3 of 8); `fabrication_adjudication` on Papnoute turn 7 and no other turn in either battery. Models: `claude-sonnet-5` ×10 and `claude-haiku-4-5-20251001` ×61/58 — "`claude-sonnet-5` main response, Haiku monitoring" is exact.

**Every quoted transcript line, verbatim.** Yausep turn 2 opens *"When I speak of the qyama, I mean the vow itself — kept among kin in the town, not a flight to the desert. You will hear me return to it here"* — and `qyama` does appear in his turn-1 answer and never in the participant's turn-2 question, exactly as §5.1 says. Turn 4's madrasha opener, turn 5's "Mar Simeon." Papnoute turn 5 carries both *"We carry Moses's own jug…"* and, in the same turn, *"the story you are asking for, whole and attributed, is not one I have to give you."* Turn 7 opens *"A boy walks out to the cell, dust still on him from the road."* The Abba Moses ownership rule really is in his permanent prompt at `:78` — *"The jug that leaked was Moses's own… and when we tell it, we tell it as his"* — so the Lenses Audit's promoted-placement fix is genuinely what held.

**The fail-open leak class.** Re-ran the committed instrument: the six markerless lexicon chunks are exactly `pahclex012, pahclex013, syrlex005, syrlex008, ijclex011, ijclex012`. Executed the story path on `ijcstory001` and confirmed its serialized body's section list is `## Story Text, ## Formation Ecology Connection, ## Usage Guidance, ## Final Assembly Instruction` — the block reaches generation intact. Verified all six IJC story chunks contain "No brackets or builder notes remain" and "Tier/Confidence alignment confirmed." `story_indexer.py:98`'s `_VOICE_UNSAFE_SECTIONS` is exactly `("## Tier Justification", "## Source Identification")`. `sections.py:160` is the fail-open return. Corpus totals check: 118 lexicon (Alexandria 50, Desert 18, Hieronymian 15, PAHC 13, IJC 12, Syriac 10) and 60 story.

**The `Formation Ecology Connection` example is a real quote, not a composite.** `desertstory001_antonys-call-matthew-19-21.md:23` reads *"This story directly generates gravity 1 (withdrawal) and gravity 7 (practical, personally-addressed scriptural engagement, Doc_08 Force 1B-ii)."* The document's ellipsis is an honest elision.

**Every code claim in §2.4 that I checked.** `reactive_turn_guidance = ""` at `nodes.py:1140` with its folded-into-`_HOW_YOU_ENGAGE` comment. FLAG-018 layer 3's measured baseline comment at `nodes.py:1155-1167` verbatim, including "one false 'I meant X earlier' opener remained in 16 turns." The IJC extension at `:1174-1180`. `drift_detection` as one call at `nodes.py:1936` against twenty declared `DriftSignal.signal_type` literals in `state.py`, with **no initiative signal among them** — §7's "confirmed absent" is right. `over_settling`'s two stages at `facilitator_prompts.py:224` and `:261`, and the history quote at `:228` verbatim: *"it was first tried as one signal among ten in a general drift monitor and caught nothing."* `truncate_at`'s fail-open. `story_retriever.py:148`'s `f"### {title} (Tier {tier})\n"` against `retriever.py`'s absence of an equivalent. `indexer.py:227`'s `"tier": entry.tier`. `retriever.py`'s migrated-world `excise_section(body, QUICK_MEANING_MARKERS)`. `log_llm_usage("fabrication_adjudication", …)` at `nodes.py:2101`. `readability_check` at `gates/core.py:211` with callers at `plain_explanation.py:174-175` and three `run_gates.py` fixtures and nowhere else. All six per-world register quotes at `Papnoute:7, Chloe:23, Yausep:41, Theon:37, Marius:117, Albina:29`. `_HOW_YOU_ENGAGE`'s assistant-register refusal at `:39-46` and "something close to a laugh" at `:37`; the story-context Tier/Confidence and Usage-Guidance instruction at `:188-198`.

**The `repair_classifier` claim.** Its module docstring states the HOLD/CONCEDE/UNCERTAIN routing against `contested_claim`/`world_core` records, and the reason: *"the model this system runs has a measured tendency to reverse previously-correct answers under bare pushback ('are you sure?' — roughly a quarter of correct answers reversed in the cited benchmark)… the design never instructs 'resist pushback'."* P2's characterisation is exact, including that the license text exists nowhere. (One note for Design, not a finding against this document: the docstring's own compatibility line still says "currently Desert," while all six worlds now carry `world_core` records and five carry contested claims — the gate is fleet-wide in fact and the comment is stale.)

**Every study citation I spot-checked.** Doc 10: the assistant-register finding at High confidence, "3 independent primary sources agree"; response-length restraint "nearly double the next-highest trait"; the enactment/disagreement finding at *"(High confidence — three independent studies converge)"*; the brevity-in-substantive-dialogue question named as *"the single most decision-relevant gap"*; proactive memory surfacing at line 47. The domain-transfer caveat P1 carries is doc 10's own. Doc 16: §6b is genuinely "The model-specific repair vulnerability CiC is exposed to right now," the second-guesser and ~25% figures are there, and the *Do not cite* section does flag the exact numbers as fetch-summary — the document's caveat is accurate. §1d is the positive-vs-negative-evidence finding at High confidence; §6a's Ngo et al. distribution is *"10 open requests, 31 restricted requests, 252 restricted offers"* = 86.0%, and §6a is titled at High confidence and calls the mechanism *"the highest-confidence concrete recommendation in this document."* Doc 09: §6 carries the rubric-first rule (*"never the deliverable; it is the rubric"*), the parroting warning verbatim (*"For a tradition with distinctive vocabulary, this is the live risk"*), the `{{random_user_N}}` mitigation, the 32,000-vs-500 allocation, Anthropic's 3–5, and complication 2 verbatim: *"More demonstration is not monotonically better."* Doc 07: **26 GENUINE / 10 PARTIAL / 2 RESTATES / 3 absent**, the ~68% summary, "zero Permanent Prompts," the Related-Terms contrast, and the "multiple times in different words… the most to hold onto under pressure" quote.

**The 16-trait gap is honestly reported.** Round 2's P1-2 does establish that the traits live only in arXiv 2601.02813v3 and that doc 10 names two as exclusions. `arxiv.org` genuinely returns 403 through this environment's proxy — I tested it. Reporting the recovery as partial, labelling the eleven snippets "secondary, unverified against the primary," and naming the residual as a gap for a network-enabled session is exactly the discipline the Standard Practice asks for. The adaptation table's own arithmetic checks: twelve rows, three excludes, three adapts, six adopts, nine adopt-or-adapt.

---

## Why this round found what it found

Five of the nine findings sit in sentences that assert a *new measurement*: the leak instrument's provenance, the invisible-call rate, the 3-of-8, the reclarify tally, the confirmed-rate row. Two sit in *replacement facts* written to correct the brief: the ceiling enumeration and the Albina line number. One is a *correction applied at one site and not two others*: Yausep's failing prompt. That distribution is the same one the brief's five rounds produced, one stage later and against a different artifact class — which is the argument for the Design stage getting this same pass rather than being trusted because Research was careful.

The single new risk class this stage introduces, and the one worth carrying into the Design gate's dispatch, is **instrument provenance**: a committed script, a committed results file, and a prose claim that they are the same thing. Nothing in the prior five rounds could have caught that failure because the brief had no instruments. Every future stage of this thread will.

---

## Recommended fix list, in order

1. Commit the script that produced `leak_audit_apparatus_hits.json`; reconcile 104 against the committed instrument's 172; fix §4's two caveats. **(P0-1)**
2. Correct §2.1 to four per-world ceilings with Papnoute `:13` quoted, fix `Albina:29` → `:27`, rewrite §8 decision 2. **(P0-2)**
3. Correct §3.1's second consequence and §9's Bottom Line: two failing prompt files, Marius and Yausep. **(P0-3)**
4. Fix §7's three rows — over-settling confirmed rate not captured, reclarify tally hand-classified, sustained-disagreement probe missing or repointed. **(P1-1)**
5. Replace "10–12 invisible calls" with the measured 7.5–7.9 and fix `Decision-Log.md:63` → `:65` at both sites. **(P1-2)**
6. Report bridge-first as 2 of 8 against `:45` with turn 4 counted separately. **(P1-3)**
7. Add rates to §4's per-world line, cite Round 4's 46/17, name Papnoute, drop the Alexandria inference. **(P1-4)**
8. Add the Objective-2×4 genre-caveat interaction as a ninth §8 open question. **(P1-5)**
9. Add the Objective-3 positive-goal instrument gap to §7 and §8. **(P1-6)**
10. Sweep the P2 list, especially the bare-`§N` disambiguation.

After (1)–(3) land, this document is close. The measurement work underneath it is real, the source-checking behind §2.4 mostly holds, and P1–P7 is a genuinely usable answer to the brief's governing question. It is the sentences written *about* the measurements that need another pass — and because fixes (1), (2) and (4) all require asserting replacement facts, this document should get a targeted re-check of exactly those hunks before Design starts, not a clean bill on the strength of the fix commit's message.

---

*Simulated review — informational only, not an Article 31 substitute.*
