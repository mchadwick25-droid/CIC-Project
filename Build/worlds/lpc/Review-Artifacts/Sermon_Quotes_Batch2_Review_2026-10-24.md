# lpc sermon batch 2 and Vandal-date correction: independent review

- Branch: `claude/lpc-sermon-batch2-2026-10-24` at `667ee9c7` (commits `0796212a`, `667ee9c7`), diffed against `origin/main`.
- Reviewer model: Opus 5.5 (`claude-opus-5-5`).
- No repo file was modified. The gates ran in a detached scratch worktree, which was removed afterwards.

## Gates and mechanical checks

- `python -m engine.m10.cli records lpc`: **PASS**.
- `python -m engine.m10.cli regate lpc`: **PASS**. 9 record files changed, 180 fields checked, 7 new or edited. It reports 6 edited fields below FK 8 but does not fail them; the batch 1 grade-8-floor question still stands. Every other note is a base failure this branch did not change.
- `engine/m4/tests/test_quote_speaker_offered.py`: 17 passed. The assertion is now `392`, and the worktree holds 392 quote files.
- **Verbatim, two independent methods.** Method A: Python strips notes and tags and folds whitespace, then searches for the substring. Method B: `sed` strips tags, `tr` folds whitespace, then `grep -cF` searches for a fixed string. Both methods ran against the `text:` field of each record on the branch. All 6 match exactly once at the stated lines. For P1 and G2, which cross two lines, neither line alone holds the passage, so the ranges are no wider than needed. No `<note>` falls inside any passage. Only `<pb n="502">` falls inside G1, and it is stripped.
- **PL 38 ranges.** I read every range in the OCR file. Each one starts on the line holding the first Latin word and ends on the line holding the last: P1 26187 *Quia* to 26199 *invocaus*; P2 27719 *Commemora* to 27724 *tux.*; P3 27006 *Et* to 27028 *tioni nostra*; G1 51152 *Mirum* to 51156 *meo*; G2 26351 *Quare* to 26356 *in te.*; G3 50082 *Denique* to 50088 *excitet te.* The sermon start lines match the inventory.
- **NPNF lines resolve.** Each record's own context claims hold: the Rom. x. 13 note at 10641; Paul named at 10639; Eucharist bread at 10891-10894; the times of day at 11170; the "unclothed" sentence at 11172-11177; the 2 Cor. iv. 7 note at 19485; the Cyprian heading at 19865/19867; the God's-will-in-saved-and-lost lead-in at 10693-10700.
- **Headings.** NPNF 6, 7 and 8 are each headed "On the Lord's Prayer ... to the Competentes", so the guard "Competentes, not a Creed sermon" holds for P1, P2, P3 and G2. NPNF 81 carries "Against the Pelagians" in NPNF's title, so the G1 guard holds. NPNF 78 is headed John v. 31 **and** Gal. v. 16 (see G3-2).
- **Cells and relations.** The three preaching quotes are F2-I, matching the gravity's F2-I. The three grace quotes are F1-T, matching the gravity's F1-T. Each quote carries one `associated-with` edge to its gravity. Each gravity gains the three inverse edges, emitted from `wb_lpc_s25.py` G4 and G7. They are reciprocal. Nothing else changed in either gravity record. `wb_lpc_s2y_canon_cells.py` adds exactly the six assignments. The `cic/texts/README.md` back-references were added to the PL 38, NPNF 106, Prosper and Possidius rows.
- `prefer_instead` targets all exist: `the-creed-first-then-the-prayer`, `let-your-creed-be-a-mirror`, `two-hear-one-scorns-one-rises`, `what-is-done-by-you-he-does-in-you`, and `stewards-and-future-bishops`, whose `retrieve_when` matches the P3 pointer.

## A. Six sermon quote records

### P1 `lpc.quote.the-creed-first-then-the-prayer` (NPNF 6 §1)

The quote is verbatim, the range is right, and the rendering holds the bar. *ergo* is absorbed into "That is why", which also carries *ideo*. The Paul-unnamed guard is correct: the passage does not name him, and he is named at 10639.

- **P1-1 (P2).** The claim guard says "The passage uses 'received'". The passage, the `text` field, says "learnt"; only the rendering says "received". Proposed: `The modern rendering uses 'received' (accepistis) for the Creed and the Prayer; it does not describe a formal handing-over ceremony, and none may be supplied unless the sermon itself gives it.`
- **P1-2 (P2).** The lens note says "He answers a question about order". No question is put in the passage. Proposed: `He explains the order: they received the Creed first, so that they would know what to believe, and the Lord's Prayer after it, so that they would know whom to call on.`
- **P1-3 (P2).** The body calls *accepistis* "the rite's own word, paired with 'give back'" but gives no source for the pairing. Proposed: add `(the pair is used openly in Sermon 58, PL 38 line 27711, reddituri estis, non Orationem, sed Symbolum)`.

### P2 `lpc.quote.let-your-creed-be-a-mirror` (NPNF 8 §13)

The quote is verbatim, the range is right, and the rendering holds. *mens* is rendered "mind" on the Latin's authority. Note: "Let it be your wealth" follows NPNF's singular, where the Latin has a plural *Sint ... ista*. That is acceptable, and not a finding.

- **P2-1 (P2).** One `retrieve_when` reads "how daily faith was kept up outside church". "Outside church" comes from the omitted sentence at 11170. Proposed: `participant asks how a believer was told to keep up faith day by day`.
- **P2-2 (P2).** The lens note says "A modern listener may hear 'professest' as a claim of skill". That is not a plausible misreading. Proposed: `A modern listener may not know 'professest'. The Latin, confiteris, is to declare openly; here what the hearer declares is the Creed.` Keep the rest as it is.

### P3 `lpc.quote.the-sermon-and-the-readings-are-daily-bread` (NPNF 7 §7)

The quote is verbatim, and the range is right, crossing the page break. The rendering holds. "Now" is NPNF's word, not the Latin's, but the present *tracto* carries it. Not a finding.

- **P3-1 (P2).** The third claim guard says the passage "does not say how often ... readings [were] read". The passage says "the daily lessons which ye hear in church" (*lectiones quotidie auditis*), and the rendering says "every day". The guard contradicts the passage. Proposed: `The sermon is to the Competentes on the Lord's Prayer, not a sermon on the Creed, and the passage does not say how often hymns were sung.`

### G1 `lpc.quote.two-hear-one-scorns-one-rises` (NPNF 81 §3)

The quote is verbatim, the range is right, and the rendering holds. "Strange", "claim", "truthful Teacher" and "rises" are all supported. The NPNF-title guard is correct.

- **G1-1 (P2).** The lens note ends "since belief is given by the Father". The verse says coming to Christ is given, and the guard bars extending it into a doctrine. Proposed: `The one who rises is not to claim it, since no one comes to Christ unless it is given him by the Father.`

### G2 `lpc.quote.what-is-done-by-you-he-does-in-you` (NPNF 6 §7)

The quote is verbatim, the range is right, and the rendering holds; the opening question is 24 words. The lead-in guard is present and correctly placed at PL 38 26340-26351. The Competentes and not-Pelagian guards hold.

- **G2-1 (P1, blocking).** The lens note glosses the passage's key term wrongly: "'by you' is what you will yourself, and 'in you' is God's will done in a person." Set against "God's will", "what you will yourself" reads as the person's own will as opposed to God's. Augustine's "by you" is God's will done by you as well (*Aliud est, ut fiat a te ... sed fiat et a te*, PL 38 26348-26351; NPNF 10700 "That His will may be done by thee is another thing ... O that it may be done by thee also"). A participant would take the opposite of the lead-in the guard exists to supply. Proposed lens note: `A modern listener may hear 'He doeth in thee what is not done by thee' as God forcing a person. Augustine is explaining the petition 'Thy will be done in heaven and in earth'. God's will is done 'in you' whether you will it or not; it is done 'by you' when you do it as well. Nothing is done by the one who prays that God does not also do in him.` Make the same change in the claim guard: replace `'by you' is willing it yourself` with `'by you' is God's will done by you as well`.
- **G2-2 (P2).** The claim guard quotes the Latin lead-in as "fit enim voluntas Dei in te". PL 38 line 26340 reads *Fiet enim*, the future tense. Proposed: `from Fiet enim voluntas Dei in te, etsi non fit a te`.

### G3 `lpc.quote.no-one-has-the-love-of-god-from-himself` (NPNF 78 §4)

The quote is verbatim, the range is right, and the rendering holds. *Denique* is rendered "Indeed", *de te* "through you", and *accendat, illuminet, excitet* "kindle, give light, stir up", verb for verb. The Paul-unnamed guard is correct: the passage calls him only "he". He is "the Apostle" at 19483 and is named in §3 at 19470.

- **G3-1 (P2).** `divergence_note`: "since de te makes the believer the source through which God's love returns to Him". Calling the believer "the source" of love says the opposite of the passage. Proposed: `'love Himself in thee' renders amet se de te, literally 'love Himself from you', rendered 'through you';`
- **G3-2 (P2).** The claim guard says "the sermon is on Galatians v. 16-17". The NPNF title is "On the words of the Gospel, John v. 31 ... and on the words of the apostle, Galatians v. 16". Proposed: `the sermon is on John v. 31 and Galatians v. 16-17 (the flesh against the Spirit).`

## B. The Vandal-date correction (commit 0796212a, OG-66)

**What holds at source.**
- Prosper enters entry 1295, *Gens Wandalorum ab Hispania ad Africam transit*, under *Hierio et Ardabure a. 427* (line 54069; entry at 54126; the next year's heading, 428, is at 54130). True.
- The siege began in 430. Possidius XXIX, lines 4146-4148, says "in the third month of the siege he succumbed to fever". The editor's note at 5873-5874 reads "On August 28, 430, in the third month of the siege, Augustine died". Prosper's a. 430 entry places the death *inter impetus obsidentium*. "In 430 they besieged Hippo" and "fell ill in the third month" are both true and no wider than the evidence.
- No "429" is left as a stated date in the record, `wb_lpc_s25.py`, Doc_08 3A-1, the World Profile or the Force Index.

### B-1 (P0, blocking): "the one chronicle we hold enters the crossing under 427" is false at source, and so is OG-66's premise

The vendored corpus holds at least three other witnesses to the crossing:
- **Hydatius**, a Spanish bishop and contemporary, gives **429, in May**: *Gaisericus rex de Baeticae provinciae litore cum Vandalis omnibus eorumque familiis mense Maio ad Mauritaniam et Africam relictis transit Hispaniis*. This is entry 90, year V of Theodosius, with Mommsen's margin 429, at `cic/texts/chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt` lines 1641-1645. Isidore's parallel on the same lines also gives 429.
- **The Gallic Chronicle of 452**, inside the very file the record cites (`prosper_chronica-minora-1-lat_mommsen1892.txt` lines 71067-71071, entry 108), enters *Vandali in Africam transfretantes* under Theodosius year VIII. On Mommsen's margins that is later than 429.
- **The Possidius editor**, in the other file the record cites, dates the invasion to 428 (lines 465, 5364, 5845).

Modern secondary works in `cic/texts/` also give 429: Duchesne 1910 at line 21523, and Dalton's Gregory of Tours note at line 23325.

So "the one chronicle we hold" is untrue. Both of OG-66's statements are also untrue: "No vendored source gives 429 for the crossing" and "The modern date 429 rests on evidence this build has not vendored". The correction removed a date that a contemporary chronicle in the Library directly supports. The new wording also misdescribes the held evidence in a canonical record, in a sentence the voice can speak.

**Proposed fix (root cause: the evidence was not searched beyond the one cited file).**
1. Add Hydatius as a source:
   - Add a Source Registry row and an `lpc.source` record for Mommsen, *Chronica Minora* II (MGH AA XI), Hydatius's *Continuatio*. If Doc_02's approved state requires it, add the row by change order.
   - Cite it in the force record. Locus: `Hydatius, Continuatio Chronicorum Hieronymianorum, entry 90 (year V of Theodosius; Mommsen's margin 429), 'Gaisericus rex ... cum Vandalis omnibus eorumque familiis mense Maio ad Mauritaniam et Africam relictis transit Hispaniis' -- cic/texts/chronica-minora-2_marcellinus-victor-tunnunensis-biclaro-isidore-mgh-aa-11-lat_mommsen1894.txt, lines 1641-1645`.
2. Record description and `wb_lpc_s25.py`, first sentence: `The Vandals crossed from Spain into Africa in May 429, by the count of Hydatius, a Spanish bishop writing at the time; Prosper's chronicle enters the crossing under 427. In 430 they besieged Hippo. Augustine fell ill in the third month of the siege, and he died on 28 August 430 -- ...` (the rest unchanged).
3. Doc_08 Force 3A-1 Layer 1: `The Vandals crossed from Spain into Africa in May 429 (Hydatius, a contemporary Spanish chronicler, Registry row [new]); Prosper's chronicle enters the crossing under 427 (Registry row 203). In 430 they besieged Hippo, and Augustine fell ill in the third month of the siege (Possidius, Vita XXIX); he died on 28 August 430. ...`
4. Doc_01 lines 46 and 140: `(from 429)` may then stand again. The World Profile and Force Index titles, "The Vandal invasion and the siege of Hippo (430)", are accurate and can stay.
5. OG-66: replace "What was wrong" and "Correction" with an accurate account. The records gave 429 without a cited source; Prosper enters the crossing under 427; Hydatius (vendored, lines 1641-1645) gives May 429; the Gallic Chronicle of 452 and the Possidius editor (428) differ. The record now cites Hydatius for 429 and Prosper for the difference, and dates the siege to 430 on Possidius. Delete the sentence "The modern date 429 rests on evidence this build has not vendored".

**Fallback, if a new Registry row cannot be added now.** Record, s25 and Doc_08: `The Vandals crossed from Spain into Africa in the late 420s; the chronicles disagree on the year, and Prosper's enters the crossing under 427.` Remove "the one chronicle we hold" everywhere, correct OG-66 as in item 5, and register Hydatius as a known open item. "Late 420s" is no wider than the evidence: 427, 428 and 429 sit inside it, and the Gallic 452 date is the outlier.

### B-2 (P1, blocking): Doc_01 still states 429

`Doc_01_World_Identification_Boundaries_Orientation.md` line 27, Ending point (430), reads "the Vandal invasion (crossing from Spain in 429, besieging Hippo as Augustine lay dying)". The commit changed lines 46 and 140 but missed this one. The six sites are therefore inconsistent, and OG-66's claim that "every site now says" is untrue.
- Under the B-1 fix: `(crossing from Spain in 429, by Hydatius's count, besieging Hippo in 430 as Augustine lay dying)`.
- Under the fallback: `(crossing from Spain in the late 420s, besieging Hippo in 430 as Augustine lay dying)`.

### B-3 (note, not a finding)

The `packages/lpc` build output is not in this diff. A package rebuild after the `records/` edits is a default "just do it" action.

## Counts

- Records reviewed: 6 quote records, plus 2 gravity records (relation edges only) and 1 force record.
- Verbatim: 6 of 6 under both methods. PL 38 ranges: 6 of 6 correct. NPNF context lines: all resolve.
- Renderings: 6 of 6 meet the bar. None needs re-rendering.
- Findings, A: 0 P0, 1 P1 (G2-1), 10 P2 (P1-1, P1-2, P1-3, P2-1, P2-2, P3-1, G1-1, G2-2, G3-1, G3-2).
- Findings, B: 1 P0 (B-1), 1 P1 (B-2).
- Totals: 1 P0, 2 P1, 10 P2.
- Gates: records PASS; regate PASS; quote-count test PASS (392).

VERDICT: Substantial revision required
