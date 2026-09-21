# VERDICT: SUBSTANTIAL REVISION REQUIRED

**Counts:** 2 HIGH · 4 MEDIUM · 3 LOW · 1 COSMETIC

This is a single-dimension review (Source and Quotation Fidelity only). Condensation loss and internal consistency are covered by parallel reviewers and are out of scope here except where noted in one line.

---

## What this review actually checked

**Scope.** Every quoted string in `lpc_World_Profile.md` (the live file, 761 lines) was located and checked — not a sample. I identified every span inside quotation marks (both `"..."` and the italicized `*"..."*` markdown form) by exhaustive grep (`grep -no '"[^"]*"'` and the italic variant), then traced each one to the document or vendored text it is attributed to. I also checked every `Doc_0n §x` citation attached to a quotation, plus a targeted (non-exhaustive) set of absence/silence claims and named attributions.

**Counts.** **44 distinct quoted spans** were checked against their cited source (listed individually in the table below; a few are adjacent fragments of one sentence, counted separately because each closes its own quotation mark). **21 distinct `Doc_0n §x` / chapter loci** were opened and read in full to confirm they contain the claimed content, not just that they exist. Two absence claims were independently re-run against the actual vendored corpus (not just against the CiC document that asserted them): the "twenty stem occurrences of *confessor*" sweep across `npnf101`–`npnf108`, and the "*libellus* headword absent from the corpus" claim. Both were reproduced exactly by direct regex sweep of the vendored files. Three named-attribution claims (Datus / "Bishop of the Kept Flock", the Article 29 confirmation, the gapped-formation-precedent ruling) were checked against `lpc_Decision_Log.md` and `lpc_Gapped_Formation_Precedent.md`.

**Method for "character-exact."** For every quotation I opened the cited document (or, for a primary-source quotation, the vendored `.txt`/`.xml` file under `cic/texts/`) and located the actual passage by grep on a distinctive substring, then read the surrounding paragraph and compared it word-for-word, including punctuation immediately inside the closing quotation mark and ellipsis characters. For Possidius (Weiskotten 1919), I built a de-hyphenated copy of the vendored file (joining `word-\nword` line-break hyphenation into `wordword`) before searching it, per the review brief's warning, and searched that copy for every Possidius quotation. Chapter attribution was confirmed by locating the nearest preceding `CHAPTER <roman>` header in the de-hyphenated text and confirming the quoted passage falls before the next one.

**What this did *not* cover, and why.** (1) The "Grounding:" citation lists at the end of each gravity entry (e.g. "Doc_01 §1, §3; Doc_02 §1, §2, §4, §5…") were not individually opened — these are broad section-range pointers attached to no specific quoted claim, and checking dozens of them against Doc_01–Doc_08 in full was outside what this pass could complete; I focused on loci that anchor an actual quotation or a specific, falsifiable factual assertion. (2) The G7/"grace" raw-frequency count (1,798) was cross-checked for internal consistency across Doc_01→Doc_03→Doc_04→Doc_05→Profile (all four agree) and a rough sanity sweep of the raw file returned a plausible superset count (2,072 over the whole `npnf105` file before excluding front/back matter), but I did not reproduce the exact div1-scoped sweep Doc_03 describes — this is a plausibility check, not a proof, and I say so rather than letting it stand as one. (3) Most of Section 8's and Doc_09-sourced absence claims (the lapsed's missing voice, the missing woman's voice, no founding narrative) were spot-checked on one thread each (the Numidicus passage, for instance) rather than swept exhaustively against the full Doc_09 Story Inventory and its own eight prior review rounds; I relied in part on the fact that Doc_09's absence-claim defect (the project's own signature failure mode) has already been through eight adversarial rounds, and I did not re-run that document's own check_claims-style sweep myself. (4) Archaeological/material-absence claims ("no site report... independently verified") are negative claims about material outside the vendored text corpus and cannot be tested from here; I note them as undischarged rather than either confirming or refuting them. (5) I did not check every internal cross-reference for consistency (word counts, section numbering, gravity counts) — that is the other reviewers' lane.

---

## Table of every quotation checked

Legend: **V** = vendored primary source (`cic/texts/`); **D** = CiC construction document; loc = the locus the Profile itself cites.

| # | Profile line | Quoted text (as it appears in the Profile) | Cited source | Result |
|---|---|---|---|---|
| 1 | 30 | "pastoral and sacramental before it is juridical" | Doc_01 §1 | PASS — exact, correct locus |
| 2 | 54 | "the ecological hub" | Doc_05 §9.1 | **FAIL (LOW)** — Doc_05 §9.1's own heading reads "an ecological hub"; "the ecological hub" is Doc_08's paraphrase, not Doc_05's wording |
| 3 | 82 | "neither does any of us set himself up as a bishop of bishops... every bishop... has his own proper right of judgment" | Cyprian, 256 preface (ANF05) | PASS — ellipses correctly mark elisions; all retained text exact |
| 4 | 94 | "the question persists as its own answer reverses" | cited: Doc_04 §3 Candidate 6 | **FAIL (MEDIUM)** — this exact wording is at Doc_04 §4 (Classification Summary); §3 Candidate 6 itself reads "the question persists even as the answer changes" |
| 5 | 96 | "the ecology's recurring stress test" | Doc_05 §9.2 | PASS — exact |
| 6 | 80 | "the clearest candidate for a genuinely cross-phase term" | Doc_03, quoted at Doc_04 §3 | PASS — exact, correct locus (Candidate 3) |
| 7 | 114 | "the channel through which external pressure reaches an ordinary believer" | Doc_08 §5 | PASS — exact, correct section |
| 8 | 128 | "Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding." | "the gapped-formation precedent from the project lead" | **FAIL (HIGH)** — see Finding 1: not a verbatim quotation of the project lead or of the precedent document; it is Doc_04's own *unquoted*, bolded editorial sentence |
| 9 | 142 | "structurally freestanding rather than load-bearing" | Doc_04 (Candidate 7, Dependency test) | PASS — exact |
| 10 | 160 | "thousands of certificates were daily given, contrary to the law of the Gospel" | Cyprian, at Doc_08 Force 2B-2 | PASS — verified against ANF05 |
| 11 | 184 | "the holy martyr Cyprian… in his letter which he wrote on Mortality" | Possidius | PASS content (ch. XXVII); ellipsis-character choice (`…`) inconsistent with row 3's `...` — see Cosmetic finding |
| 12 | 200 | (disclosure, no quote marks) — *libellus* absent from corpus, one occurrence in Introductory Notice to the Novatian treatise | Doc_01/Doc_03 | PASS — independently reproduced: exactly one `libell-` hit in all of `anf05`, at the cited location |
| 13 | 204 | "it is the shepherd that is chiefly wounded in the wound of his flock" | *De Lapsis* 4 | PASS — exact, correct paragraph number |
| 14 | 204 | "I wail with the wailing, I weep with the weeping." | *De Lapsis* 4 | PASS — exact |
| 15 | 204 | "ancient venom" | Cyprian's letters | PASS — exact |
| 16 | 206 | "No claim is made about what an individual catechumen at Carthage or Hippo experienced interiorly" | Doc_05 §5.1 | PASS — exact, correct subsection |
| 17 | 216 | "an ordinary believer at Hippo in the 420s is being formed by this material; an ordinary believer at Carthage in the 250s is not" | Doc_05 §5.3 | PASS — exact, correct subsection |
| 18 | 220 | "episodic" | Doc_01 §1 | PASS — exact |
| 19 | 220 | "one recurring pressure among several on this world's own ordinary pastoral office" | Doc_01 §1 | **FAIL (MEDIUM)** — see Finding 3: source reads "...several on **the** ordinary pastoral office"; "this world's own" is inserted |
| 20 | 224 | "your suffrage and God's judgment" | Cyprian's episcopate (letters) | PASS — exact, verified in Ep. XXXIX |
| 21 | 224 | "and to all the people" | Possidius ch. VIII | PASS — exact |
| 22 | 224 | "rejoiced and clamored most [eagerly] that this should be done" | Possidius ch. VIII | PASS — `[eagerly]` is a disclosed bracketed correction of the source's own OCR garble ("elageriy"); rest exact |
| 23 | 224 | "refused to accept the episcopate" | Possidius ch. VIII | PASS — exact |
| 24 | 224 | "under compulsion and constraint he yielded." | Possidius ch. VIII | PASS content; quote truncated (source continues "...and accepted the ordination to the higher office") without an ellipsis mark — see Low finding |
| 25 | 224 | "gave his presbyter the right of preaching the Gospel...contrary to the practice and custom of the African churches," | Possidius ch. V | **FAIL (LOW)** — source ends this clause with a period, not a comma; see Finding 5 |
| 26 | 224 | "some other presbyters by permission of their bishops began to preach to the people in their presence." | Possidius ch. V | PASS — exact |
| 27 | 226 | "bishop of bishops" | Cyprian, 256 preface | PASS — exact |
| 28 | 234 | "judging no man, nor rejecting any one from the right of communion, if he should think differently from us," | Cyprian, 256 preface | PASS — exact |
| 29 | 240 | "are often corrected by those which follow them, when, by some actual experiment, things are brought to light which were before concealed" | Augustine, *De Baptismo* II (via Doc_07 §3B) | PASS — exact, verified in `npnf104` |
| 30 | 378 | "Cyprian never asked the magistrate for anything; a century and a third later the magistrate could be asked, and eventually was" | Doc_08, Layer 2 | PASS content; Doc_08 itself does not present this as a quotation (no quote marks in Doc_08) — see Finding 4 (pattern note) |
| 31 | 586 | "I am placed in the midst of a great tribulation" | Cyprian, *Ep.* XX | PASS — exact |
| 32 | 586 | "the (spiritual) death of my sister, who in this time of devastation has fallen from Christ" | Cyprian, *Ep.* XX | PASS — exact, including parenthetical |
| 33 | 636 | "from which were supplied the things necessary for the altar," | Possidius chs. XXII **and XXIV** | **FAIL (HIGH)** — see Finding 2: content is entirely in ch. XXIV; ch. XXII contains none of it |
| 34 | 636 | "never had any desire" | Possidius chs. XXII **and XXIV** | **FAIL (HIGH)** — same as above |
| 35 | 660 | "Numeria and Candida" | Cyprian, *Ep.* XX | PASS — named exactly, correct letter |
| 36 | 668 | "mostly through what preaching and catechesis presuppose about it," | Doc_01 §3 (via Doc_05) | **FAIL (MEDIUM)** — see Finding 6: comma inserted, parenthetical dropped with no ellipsis mark |
| 37 | 668 | "not through separate liturgical treatises." | Doc_01 §3 | PASS content; quote closed early (source continues "...the way, for instance, World #9's...") without ellipsis — folded into Finding 6 |
| 38 | 678 | "if anything, more diffusely and more widely continuous into the present than any single-see primacy claim" | Doc_01 §1 | PASS — exact |
| 39 | 685 | "a bishop of bishops" | Cyprian, 256 preface | PASS — exact |
| 40 | 687 | "compel them to come in," | Augustine (Luke 14:23 warrant) | PASS — verified verbatim in `npnf101` (multiple letters) |
| 41 | 731 | "the highest-value unblocked task in the build" | Doc_07 §8 item 8 | PASS content; not a quotation in Doc_07 itself (bolded plain prose) — see Finding 4 (pattern note) |
| 42 | 703 (Section 10) | Full "Integrative Observation" paragraph | Doc_07 §6, "copied verbatim" | PASS — diffed programmatically, byte-identical |
| 43 | 40 / 715 | "Pastoral Office as Flock-Keeping" (disclosed divergence from G1's own name) | Doc_04 §4 | PASS — Doc_04 §4's table does read exactly this, confirming the Profile's own disclosure is accurate |
| 44 | 158 | "twenty stem occurrences of confessor... against roughly 150 in Cyprian's one volume" | Doc_05 §2.3 | PASS — independently reproduced by direct regex sweep of `npnf101`–`npnf108` (total 20, matching the claimed per-volume breakdown exactly) and `anf05` (158, "roughly 150" is a fair rounding) |

**Tally: 34 PASS, 10 FAIL** (2 HIGH, 4 MEDIUM, 4 LOW/COSMETIC as detailed in Findings below; two of the ten FAIL rows, #33/#34, are one finding).

---

## Findings, most severe first

### Finding 1 (HIGH) — A quotation attributed to "the project lead" is not the project lead's words, and does not appear in the document it is sourced to

**Profile text (line 128):** *"Doc_04 §7 Open Item 8 is CLOSED (2026-09-15), on the gapped-formation precedent from the project lead: "Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding.""*

The sentence is set in italics and quotation marks — the Profile's own formatting convention for a direct quotation — and is attributed to "the gapped-formation precedent from the project lead," i.e., presented as the project lead's own words, transmitted through `lpc_Gapped_Formation_Precedent.md`.

**What the actual sources say:**
- `lpc_Decision_Log.md` line 642 ("Provenance, stated exactly"), the document's own record of what the project lead actually said: *"the ruling itself — Candidate 5 is Supporting, with the reconciliation pass to follow."* That is the entire verbatim ruling on record. No mention of "honestly thin" or "a puzzle with a cleaner solution outstanding."
- `lpc_Gapped_Formation_Precedent.md` §4b, the document actually cited as the source: its own quoted precedent sentence is different — *"Treat five consecutive re-classifications of the same candidate as itself the signal to stop and accept the narrower finding."* The phrase "honestly thin" / "cleaner solution outstanding" does not appear anywhere in this file.
- `Doc_04_Gravity_Discovery.md` line 214, the only place the exact wording quoted by the Profile actually exists: **"Candidate 5 is Supporting, and honestly thin, and that is the answer rather than a puzzle with a cleaner solution outstanding."** — but there it is Doc_04's *own* bolded editorial sentence, written by the Doc_04 build thread, with no quotation marks at all. It is presented in Doc_04 as that document's conclusion, not as anyone else's words.

So the Profile has taken a build thread's own unquoted synthesis sentence and re-presented it, verbatim, dressed in quotation marks and italics and attributed to "the project lead," as though the project lead spoke or wrote those words. This is exactly the category CO-022 exists to prevent ("nothing is attributed to the project lead without a verifiable record") and matches this project's own definition of a misattributed/fabricated quotation.

**Fix:** Either drop the quotation marks and attribute the sentence to Doc_04 as Doc_04's own synthesis (not to the project lead), or replace it with the actual verifiable project-lead language ("Candidate 5 is Supporting") plus, if the elaboration is wanted, an unquoted paraphrase clearly marked as this build's own gloss.

---

### Finding 2 (HIGH) — Citation locus cites two Possidius chapters; the content is entirely in one, and the other contains nothing related

**Profile text (line 636):** *"Possidius chs. XXII and XXIV name the church's treasury and consistory "from which were supplied the things necessary for the altar," the holy vessels, the annual audit, and Augustine's having "never had any desire" for new buildings."*

I read Possidius chs. XXII, XXIII and XXIV in full in the de-hyphenated Weiskotten text (`cic/texts/possidius_vita-augustini_weiskotten1919.txt`, lines 2798–3026).

- **Chapter XXII** ("Augustine's use of food and clothing") is entirely about his diet, wine, clothing, bedding, table manners, and his rule about gossip at meals. It contains **no reference at all** to treasury, consistory, the altar, church vessels, the annual accounting, or new buildings.
- **Chapter XXIII** ("His use of the church revenues") discusses possessions and clerical jealousy over them — closer to the topic, but still not the specific claims quoted.
- **Chapter XXIV** ("Household affairs") is where every one of the claimed facts actually sits: the annual accounting of receipts and expenditures ("At the end of the year the accounts were recited to him..."), the melting-down of the holy vessels for the poor, "For new buildings he **never had any desire**...", and the treasury/consistory sentence ending "...**from which were supplied the things necessary for the altar**, had been neglected by the faithful..." — all within lines 2901–3026, i.e., wholly inside Chapter XXIV.

Citing "chs. XXII and XXIV" for content that is entirely in XXIV, with XXII containing none of it, is a locus that exists but says something else — the more serious kind of citation error the review brief specifically calls out. This looks like an off-by-two chapter slip (XXII for XXIV, or possibly meaning to span XXII–XXIV and overstating the range).

**Fix:** Cite Possidius ch. XXIV alone (or "chs. XXIII–XXIV" if the revenue-jealousy material in XXIII is meant to be included), not "chs. XXII and XXIV."

---

### Finding 3 (MEDIUM) — Altered quotation: words inserted into a quoted phrase that are not in the source

**Profile text (line 220):** *"Against World #6 (Imperial-Juridical Christianity), the primacy question is "episodic" here — "one recurring pressure among several on this world's own ordinary pastoral office" — where it is constitutive there."*

**Doc_01 §1 (the cited source), verbatim:** *"...this document's evidence finds it episodic in this world's own corpus — one recurring pressure among several on **the** ordinary pastoral office — where it is constitutive of two of IJC's own three strands' own stated grounds..."*

The source reads "on **the** ordinary pastoral office." The Profile's quotation reads "on **this world's own** ordinary pastoral office" — three words inserted inside the quotation marks that do not appear in Doc_01 at all. The insertion doesn't reverse the sentence's meaning, but it is presented as an exact quotation and is not one.

**Fix:** Either quote the source exactly ("...on the ordinary pastoral office") or drop the quotation marks around that clause and paraphrase.

---

### Finding 4 (MEDIUM) — Pattern: plain, unquoted prose from a source document is re-presented as an italicized direct quotation

Two further instances (beyond Finding 1, which is the same pattern compounded by misattribution):

- Line 378: *"Cyprian never asked the magistrate for anything; a century and a third later the magistrate could be asked, and eventually was"* (Doc_08, Layer 2) — in `Doc_08_Forces_Document.md` line 179, this sentence is Doc_08's own plain narrative prose, with no quotation marks of any kind.
- Line 731: *"the highest-value unblocked task in the build"* — in `Doc_07_Integrated_Ecology_Analysis.md` line 252, this phrase is bolded but not quoted; it is Doc_07's own unmarked assertion.

In both cases the words themselves are accurate (character-exact), so these do not misstate content. But rendering a source's own unflagged analytical prose as an italicized, quotation-marked "quotation" manufactures the appearance that the source itself singled the phrase out as noteworthy or citable language — which it did not. This is the same mechanism (not the same instance) as the "italics added around a quotation the source gives plain" defect named in this build's history, generalized here to whole sentences rather than a formatting-only slip. Given that at least one instance of this pattern (Finding 1) concealed an actual fabrication, the pattern itself is worth flagging as a MEDIUM risk factor independent of the two clean instances found here.

**Fix:** Reserve italicized quotation-mark formatting for spans the cited document itself marks or clearly intends as quotable language; render paraphrase of a document's own unquoted analytical prose as paraphrase.

---

### Finding 5 (LOW) — Punctuation altered inside a closing quotation mark

**Profile text (line 224):** *"gave his presbyter the right of preaching the Gospel in his presence in the church and very frequently of holding public discussions — contrary to the practice and custom of the African churches,"*

**Possidius, ch. V, verbatim:** "Therefore he gave his presbyter the right of preaching the Gospel in his presence in the church and very frequently of holding public discussions — contrary to the practice and custom of the African churches." (period)

The Profile's quotation substitutes a comma for the source's own period so the quotation can run into the Profile's own following clause ("...and afterwards..."). The content is unchanged, but this is exactly the "punctuation pulled inside a closing quotation mark" defect type named in this build's history.

**Fix:** Close the quotation at "African churches." and start a new sentence, or move the comma outside the quotation marks.

---

### Finding 6 (MEDIUM) — Elision without an ellipsis mark, plus an inserted comma

**Profile text (line 668):** *"its rite is recovered "mostly through what preaching and catechesis presuppose about it," "not through separate liturgical treatises.""*

**Doc_01 §3, verbatim (via Doc_05 §10's own quotation of it):** "Worship is present but recovered mostly through what preaching and catechesis presuppose about it **(baptismal practice, the Eucharist, the Creed taught to catechumens), not** through separate liturgical treatises..."

The Profile splits one continuous sentence into two separately-closed quotations, silently dropping the parenthetical ("(baptismal practice, the Eucharist, the Creed taught to catechumens)") with no ellipsis mark, and inserting a comma after "about it" that the source does not have there (the source's comma sits later, after the parenthetical). The resulting two fragments read naturally but are not what the source's punctuation actually does.

**Fix:** Either quote the full sentence with an ellipsis marking the drop, or quote only "not through separate liturgical treatises" and paraphrase the rest.

---

## Lower-severity / cosmetic notes (not scored above the LOW/COSMETIC tally)

- **Ecological-hub misattribution (LOW, table row 2):** "the ecological hub," attributed to Doc_05 §9.1, is Doc_05's own heading's indefinite-article form ("an ecological hub"); the definite-article phrasing quoted by the Profile actually originates in Doc_08 line 322's paraphrase of Doc_05's finding, not in Doc_05 itself.
- **Citation-locus mismatch (MEDIUM, table row 4):** "the question persists as its own answer reverses," cited to "Doc_04 §3 Candidate 6," is the exact wording only of Doc_04 §4's classification-summary table; §3 Candidate 6's own Persistence bullet uses different wording ("the question persists even as the answer changes"). Both convey the same idea, but the citation points to the wrong section for the exact string quoted.
- **Ellipsis character inconsistency (COSMETIC):** the Cyprian 256-preface quotation (line 82) uses ASCII "..." for its two elisions; the Possidius quotation (line 184) uses the Unicode "…" character for its one elision. No stated convention favors one over the other, and the document uses both.
- **Untruncated-without-marker quotations (LOW, folds into table rows 24 and 37):** two Possidius/Doc_01 quotations end mid-sentence at a natural clause boundary without an ellipsis mark, though the retained text is accurate as far as it runs.

---

## What I did not find

I did not find a repeat of Round 1's specific defects (no new fabricated quotation matching that pattern beyond Finding 1's new instance; no altered primary-source quotation changing meaning; no misattributed Doc_01 string beyond the ones already disclosed and corrected in Section 4F). The two absence claims I independently re-ran against the vendored corpus (the *confessor* sweep and the *libellus* headword) both held up exactly as claimed — these are the strongest-evidenced claims in the document precisely because their own sources show the sweep methodology and I could rerun it. The G1 name-divergence disclosure (line 40/715, "Pastoral Office as Flock-Keeping" vs. "...as Territorial Flock-Keeping") is accurate: Doc_04 itself is internally inconsistent between its own §3 candidate header and its own §4 table, and the Profile discloses this correctly rather than papering over it.

Given the fabricated/misattributed quotation in Finding 1 strikes directly at CO-022's governance rule, and Finding 2 is a citation locus that actively points at the wrong chapter for the exact content claimed (the more serious of the two citation-error types per this review's own instructions), this document has not cleared the bar this dimension sets, notwithstanding a large majority of quotations (34 of 44 checked) passing cleanly.
