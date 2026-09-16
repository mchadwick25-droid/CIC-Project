# Step 3a Lexicon - Review Round 2

**Reviewer:** independent, adversarial; no part in the draft or in Round 1. **Under review:** the 18 term records in `records/desert/term/` and `worlds/desert/build/LEXICON-INDEX.md` at commit `184747bc` ("desert step 3a, review round 1: fix build-jargon in senses + quote-mark issues"), branch `world/desert`, against the pre-fix draft `b7d20aa0`. **Ground truth used:** the vendored texts in `cic/texts/` (npnf202, npnf204, npnf211, `palladius_lausiac-history_clarke1918.txt`, `webbe_world-english-bible-british-edition.xml`), `worlds/desert/CiC_W3_Doc06_Full_Lexicon.md`, the step-2 source records in `records/desert/source/`, `records/_fleet/canon_question/`, and `engine/m1/gates.py` / `engine/m2/builders.py`. Method: every one of the 72 sense fields in all 18 records was read in full (not spot-checked), the complete `b7d20aa0→184747bc` diff was read line by line, every quoted string in every participant-facing field was scanned, and every line-pointer in every `sources[].locus` was opened in the vendored file.

---

## A. Per-finding verification

### Finding 1 (SUBSTANTIAL, build-infrastructure vocabulary in `senses`) — **PARTIALLY FIXED; ONE FIX INTRODUCED A NEW INSTANCE OF THE SAME DEFECT**

Seven of the eight flagged instances are genuinely and cleanly fixed, verified by reading the new text, not the claim:

| record | new evidential text | verdict |
|---|---|---|
| antirrhesis | "The work itself survives chiefly in Syriac and Armenian; what can be checked directly in English is Socrates's own description of it." | clean |
| theoria | jargon removed (but see New Finding 2 — the replacement is factually overclaimed) | jargon clean |
| koinonia | "no English of it can be quoted here directly… alongside modern scholarship on the Latin" | clean |
| synaxis | "his own eyewitness account" | clean |
| puritas-cordis | "both checked word for word" | clean |
| apotage | "not the Rule's own words" | clean |
| logismoi | "a one-author elaboration kept distinct here" | clean |

**The eighth is not fixed — and the jargon there is newly introduced by the fix itself.** `records/desert/term/desert.term.apatheia.md:44`:

> evidential: "The systematized sense rests on Evagrius's own writings, which survive but are not translated into any English **this corpus** can quote directly; …"

The draft at `b7d20aa0` read "(consult-only; the vendored Socrates excerpts…)". The revision removed "consult-only" and "vendored" and wrote in **"this corpus"** — the exact string Round 1 named as an exemplar of the defect (it quoted koinonia's "what **this corpus** holds directly" as the model instance). This is the illusory-fix pattern the Doc_04/Doc_06/Doc_08 history warns about: the flagged tokens were removed and a synonym from the same banned family substituted, in the same field, in the same revision.

**My exhaustive re-scan of all 72 sense fields found two further pre-existing instances Round 1 missed** (both untouched by the fix, so the pattern was never exhaustively swept even at draft-review time):

- `desert.term.koinonia.md:42` **informational**: "It is the clearest strand-bound term **in this lexicon** — the solitary and semi-solitary strands have no equivalent." The lexicon is a build artifact; in-world there is no lexicon. Same class as "this record."
- `desert.term.kellion.md:39` **evidential**: "No specific structure can be tied to a specific named figure, and **no record here** tries." Record self-reference — the precise thing the logismoi fix was made to remove ("this record keeps distinct" → "kept distinct here").

Borderline, listed for completeness but not requiring change on my judgment: `desert.term.theoria.md:35` "Its strand-bound status is a **tested finding**, not an impression" (review-process vocabulary); koinonia's "quoted **here**" and logismoi's "kept distinct **here**" (bare "here" reads as the speaking situation, not the corpus — acceptable).

Confirmed independently, and it bears on severity: the defect remains latent, not live. `engine/m1/gates.py:247` scopes `_ATTRIBUTION_FIELDS["term"]` to `plain_meaning`/`quick_meaning`/`world_word` only, and `engine/m2/builders.py:_chunk_text` compiles exactly those three fields for terms — `grep -rn "senses" engine/ --include=*.py` returns only the schema and the completion-gate field list. Nothing mechanical will ever catch this, and nothing currently ships it; it becomes retrieval content later, which is why it has to be right now.

**Verdict: NOT FIXED for apatheia (fix introduced the new instance); FIXED for the other seven; two additional pre-existing instances found on exhaustive re-scan.**

### Finding 2 (SUBSTANTIAL, paraphrases inside quotation marks) — **GENUINELY FIXED** (one further instance found on re-scan, below)

- `desert.term.kellion.md:40`: now "the tradition's own remembered counsel holds that a cell, sat in, will teach a person everything." No quotation marks. The body's self-contradicting clause ("it is deliberately not marked as a quotation here") was also corrected to "paraphrase-only until Budge lands," so the body and the field now agree — the fix went to the contradiction, not just the symptom.
- `desert.term.apophthegma.md:40`: "'Give me a word'" → "Asking an elder for a word was a real request…" No quotation marks.

I re-scanned every quoted string in every participant-facing field across all 18 records (`plain_meaning`, `quick_meaning`, `false_friend`, `retrieve_when`/`do_not_retrieve_when`, and all four senses). All remaining quotation marks are word-mentions or scare quotes ('flight to the desert', 'Withdrawal'/'retreat', 'stillness', 'Theory', 'really', 'going to church', 'Communal rule', 'Freedom from compulsion', 'purity of heart') except three attributed strings, which I checked against the vendored files:

- antirrhesis evidential, "selections from the Holy Scriptures against tempting spirits, distributed into eight parts" — **verbatim confirmed** in `npnf202_socrates-sozomen-ecclesiastical-histories.xml` at lines 13541–13542 (Socrates IV.23; the phrase is hard-wrapped, so a naive line-grep misses it — it must be checked against whitespace-flattened text). Real quote, correctly placed.
- puritas-cordis informational, 'Blessed are the pure in heart' — **verbatim confirmed** in the vendored `webbe_world-english-bible-british-edition.xml` (Matt 5:8: "Blessed are the pure in heart, for they shall see God"). Real quote.
- nepsis informational, 'be sober, be watchful' — **not verbatim in any vendored text.** See New Finding 3.

**Verdict: GENUINELY FIXED as to the two flagged records; the rescan Round 1 claimed to have done missed one instance.**

### Finding 3 (COSMETIC, Conference I line pointer) — **GENUINELY FIXED, verified at the file, not at the diff**

`desert.term.puritas-cordis.md:17` now reads `~line 26109`. I opened `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` at 26100–26120. The quoted sentence begins at **line 26109** ("gaping at this remark, the old man proceeded: The end of our profession") and runs through 26112 ("the immediate aim or goal, is purity of heart, without which no one can / gain that end"). Verbatim as quoted, with the record's ellipses honestly placed. The old pointer 26147 sits in Chapter V's restatement ("the immediate goal is purity of heart, which he not unfairly terms 'sanctification'") — Round 1's diagnosis was exactly right and the correction lands on the right line. I.4 chapter attribution correct.

Applying the exhaustive-rescan rule to this pattern too, I opened **every** remaining line-pointer in the 18 records: antirrhesis `~13540` ✓ (npnf202); cheironaxia `~31290–31300` ✓ (npnf204 §3, "He worked, however, with his hands… and part he spent on bread and part he gave to the needy" at 31289–31292); cheironaxia and synaxis `file line 225` ✓ (both Palladius quotes sit on that single wrapped line — "All these men work with their hands at linen-manufacture, so that all are self-supporting" and "They occupy the church only on Saturday and Sunday," with the eight priests immediately following); puritas-cordis `~20072` ✓ (npnf211 Institutes IV.43: ladder from "the fear of the Lord" at 20066 to "By purity of heart the perfection of apostolic love is acquired" at 20073). **No second instance of the finding-3 pattern exists.**

### Finding 4 (COSMETIC, index dropped a false friend) — **GENUINELY FIXED**

`LEXICON-INDEX.md` row 17 now reads `affirmation technique; arguing with yourself`, matching `desert.term.antirrhesis.md:35-36`. I re-walked all 18 rows' alias cells against their records' `false_friend` lists in the same pass: no other omission, and no alias invented that isn't in a record.

### Finding 5 (COSMETIC, dropped `Ergocheiron`) — **GENUINELY FIXED, and the pattern is exhaustively clear**

`desert.term.cheironaxia.md:36` is now `world_word: cheironaxia / ergocheiron`, with a body note recording why. I then checked the pattern rather than the instance: `grep -E "^#{2,4} "` over Doc_06 shows exactly two entry titles carrying an alternate/compound form — 1.6 "Gerōn / Abba / Amma" and 1.7 "Cheirōnaxia / Ergocheiron." Both are now carried in `world_word` (`geron / abba / amma` was already correct). Every other Doc_06 title's parenthetical is an English gloss, not an alternate form, and correctly lives in `plain_meaning`. **No further drops.** The slash form is compiled into chunk text via `_chunk_text`, and the precedent (`geron / abba / amma`) already existed; alias-safety and no-build-attribution gates still pass with it (see §C).

### Finding 6 (PLAUSIBLE, uncited interpretive claim on antirrhesis) — **GENUINELY FIXED**

`desert.term.antirrhesis.md:41` was "the tradition held that arguing with a thought feeds it; this answers it from outside itself, with a word that is not yours" → now "this answers a thought from outside itself, with a word that is not yours, rather than debating it on its own ground." The unanchored attributed-to-the-tradition rule is gone; what remains is a description of the technique's own shape, which the informational sense and the Socrates description both support. The body records the reasoning. Correct disposition of a finding Round 1 could only mark plausible.

### Finding 7 (COSMETIC, Gould unregistered) — **GENUINELY FIXED**

`desert.term.apatheia.md` now carries `- source_id: desert.source.gould-desert-fathers` with locus "the named counter-position to Rubenson's Origenist-influence reading (consult-only)." I read `records/desert/source/desert.source.gould-desert-fathers.md`: it is the registration anchor for exactly this ("his published criticism holds that Rubenson's Origenist/Alexandrian-influence reading of the Letters of Antony overreaches the texts"), rights `copyrighted-consult-only`, weight `contested`. The referential gate resolves it. The sense's wording ("Gould's published counter-position holds that reading overreaches") stays inside the bound the source record itself sets ("the specific review/article venue is not pinned by this corpus — pin it before quoting Gould directly"): the record describes, never quotes. Clean, and consistent with `desert.source.rubenson-letters` carrying the other pole.

---

## B. New findings from the fresh adversarial pass

**N1. SUBSTANTIAL — `desert.term.theoria` evidential sense: the Round-1 rewrite replaced corpus jargon with an evidential overclaim.** `desert.term.theoria.md:35`:

> "Rests on Evagrius's own corpus; the historian Socrates names his works and quotes some of his sentences, **which is the one place this stage's teaching can be checked in English directly.**"

The draft said "the vendored Socrates excerpts as the one directly checkable witness **to his works**" — true. The rewrite narrows the claim from *his works* to *this stage's teaching* (contemplation), and that claim is false against the vendored text. I read the whole Socrates IV.23 extract in `npnf202`: after naming the three books, Socrates writes "These are his words:" and subjoins ascetic maxims and anecdotes — a drier diet and love conducting a monk to tranquillity, the brother freed from night apparitions by ministering to the sick, Antony's "my book… is the nature of things that are made," Macarius on memory of injuries, the sold gospel-book, the five reasons monks act. **There is no contemplation doctrine in the excerpt at all.** The record contradicts its own source row, which honestly says "the scheme's contemplative stage (consult-only; vendored excerpt witness via Socrates IV.23)," and its own `verification_state: verified-via-authority`. Compare antirrhesis, whose parallel rewrite got this exactly right ("what can be checked directly in English is Socrates's own description **of it**"). Fix is one clause — say that what is checkable in English is Socrates's naming of the works and a handful of his practical sayings, not this stage's teaching.

**N2. SUBSTANTIAL — Finding 1's pattern is not exhaustively cleared: three live instances remain** (detailed in §A/Finding 1, restated here so the revision has a checklist): `desert.term.apatheia.md:44` "any English **this corpus** can quote directly" (introduced by the Round-1 fix); `desert.term.koinonia.md:42` "the clearest strand-bound term **in this lexicon**"; `desert.term.kellion.md:39` "and **no record here** tries." All three need in-world rewording on the model of the seven that were done correctly.

**N3. SUBSTANTIAL — `desert.term.nepsis` informational sense quotes scripture that is not verbatim in any vendored text and registers no source for it.** `desert.term.nepsis.md:38`: "Rooted in shared Christian vocabulary (**'be sober, be watchful'**)…". This is 1 Peter 5:8, but the vendored `webbe_world-english-bible-british-edition.xml` reads "**Be sober and self-controlled. Be watchful.**" — the record's rendering matches no vendored English (it is closest to ESV/RSV wording, which this corpus does not hold), and `nepsis`'s `sources[]` carries only the apophthegmata and Evagrius records, no scripture source at all. This is precisely Finding 2's class — paraphrased material inside quotation marks presented as an attested wording — in a record Round 1's rescan passed over. It is the easiest of all to fix, because a real verbatim is available in the vendored Bible; the choice is to quote WEB accurately (and register it) or drop the quotation marks and name the source of the phrase in prose.

**N4. COSMETIC — the index's own "Review Round 1 note (applied)" is inaccurate as written.** `LEXICON-INDEX.md` states the fix removed build vocabulary "('vendored,' 'consult-only,' '**this corpus**') inside seven records' evidential senses." "this corpus" survives in apatheia's evidential sense, which is one of those seven. A revision note that overstates its own completeness is exactly what this project's review discipline exists to prevent; it must be corrected together with N2, not left standing.

**N5. COSMETIC — quote hygiene, `desert.term.antirrhesis.md:39`.** The Round-1 rewrite moved the terminal period **inside** the closing quotation mark: "…distributed into eight parts.**'**" The source sentence does not end there — it continues "…, according to the number of the arguments." The record's own `sources[].locus` renders the same span correctly with no interior period. Use an ellipsis or place the period outside.

**N6. COSMETIC — `desert.term.cheironaxia.md:17` locus silently elides a word from a verbatim claim.** The locus quotes "'he worked with his hands... part he spent on bread and part he gave to the needy'"; npnf204 §3 reads "**He worked, however, with his hands**, having heard, 'he who is idle let him not eat,' and part he spent…". The interior ellipsis is honest; the dropped "however," is not marked. The claim is labelled a verbatim locus, so it should be exact or marked.

**N7. COSMETIC — program vocabulary and a term collision in two sense fields.** `desert.term.geron-abba-amma.md:46` (translational): "If a modern **participant** asks about women's authority…" — "participant" is CiC program vocabulary for the app user, and it is inconsistent with the register's own convention elsewhere ("a modern hearer" in puritas-cordis, "a modern reader" in logismoi, "the modern picture" in apotage). Relatedly `desert.term.koinonia.md:44` (personal): "**Participants** felt it as a different kind of authority" — here the word means the monks, colliding head-on with the program's reserved sense of the same word inside retrieval content. Both are one-word fixes ("a modern hearer"; "those who joined").

**N8. COSMETIC — record-body note ordering is inconsistent across the revision.** Five records (apotage, koinonia, logismoi, synaxis, theoria) place the new "Step3a Review Round 1…" note *before* the "Re-derived from Doc_06…" provenance paragraph; six others (antirrhesis, apatheia, apophthegma, cheironaxia, kellion, puritas-cordis) place it *after*. The after-form is right — provenance first, revision history second. Purely presentational.

**Checked and clean (no finding).** Nothing else surfaced, including on the axes Round 1 might plausibly have flattered: all four senses of all 18 records read in full; every canon question I spot-verified exists and fits at close range (`f4-p-01` "I can't quiet my own head" for hesychia/logismoi/nepsis/apatheia; `f2-i-01` "How did you read your scriptures?" for antirrhesis; `f2-e-02` "Isn't most of what's said about you legend, collected centuries later?" for apophthegma; `f5-e-01` "If archaeologists dug up the place you met, what would they find?" for kellion; `f4-i-02` "Why and how did you pray?" for theoria) — no canon-cell overreach introduced by the fix, and penthos's deliberate empty set still stands with its stated reason; the reciprocity graph is untouched by the diff and the gate confirms it; confidence blocks are unchanged and still earned (antirrhesis `verified-direct` rests on the Socrates description I verified verbatim; puritas-cordis `A`/`verified-direct`/`Documented` rests on two loci I verified verbatim; apatheia `Contested`/`verified-via-authority` with both poles now registered); Doc_06 fidelity on every field the diff touched; step-2 source-record consistency (Gould, apophthegmata paraphrase discipline, Evagrius `work` coverage); no encoding damage — the only non-ASCII character in all 18 records is the macron in the quoted Doc_06 title "Cheirōnaxia" in cheironaxia's body, which is correct.

---

## C. Gate battery (run by this reviewer)

```
python3 -c "sys.path.insert(0,'.'); load_world_records('desert') + load_fleet_records() + load_registry(); gates.run_all(...)"
records: 52
PASS schema-validation · referential · reciprocity · completion-per-type · narratability
PASS quote-recording · alias-safety · distribution-health · confidence-crosscheck
PASS rights · readability · no-build-attribution
FAIL canon-coverage — 18 blank cells (C-E/I/P/T, F1-E/I/P/T, F2-P, F2-T,
     F3-E/P/T, F4-E, F4-T, F6-E/I/T)
```

12 of 13 pass. The canon-coverage state is **identical** to Round 1's (same 18 cells), i.e. the revision caused no coverage regression, and it remains the expected mid-build condition — only term/source/search_record types exist at step 3a and the blank cells belong to later steps' record types. `run_all` takes three arguments (`records, fleet, registry`); the registry comes from `engine.m1.registry.load_registry()`. Worth confirming explicitly: the new slash-form `world_word` did **not** break `alias-safety`, `readability` (FK ceiling), or `no-build-attribution`, and none of the eleven body notes added by the revision trip any gate, because bodies are outside `_ATTRIBUTION_FIELDS` and outside `_chunk_text`.

---

## D. Assessment

Five of the seven Round 1 findings are genuinely fixed, and three of them are fixed better than the minimum: the kellion fix corrected the body's self-contradiction rather than only the quotation marks, the cheironaxia fix restored the alternate form *and* I confirmed no sibling instance exists, and the puritas-cordis line pointer lands on the right line in the real file. The line-pointer pattern and the alternate-form pattern are both now exhaustively clear, checked instance by instance against the vendored texts rather than accepted on the revision's word.

But the two substantial pattern findings — the ones this round exists to re-test — are not clear. Finding 1's fix removed the flagged tokens from apatheia and wrote a fresh instance of the same banned family into the same field, which is the illusory-fix signature this project learned to look for in Doc_04/Doc_06/Doc_08; the exhaustive sweep Round 1 called for turns up two more instances it did not reach; the index's applied-note now asserts a completeness the files do not have; and Finding 2's rescan missed a quoted scripture phrase that matches no vendored English. On top of that, one rewrite traded a jargon problem for an accuracy problem: theoria now claims the contemplation teaching is directly checkable in English, and the vendored Socrates extract — which I read end to end — contains no contemplation teaching at all.

None of this is deep. Every item is a clause-level edit in a field that ships nothing yet. But four substantial items across five records, two of them created by the Round 1 revision itself, is not a cleared step.

VERDICT: SUBSTANTIAL REVISION REQUIRED
