# Doc_03 Review — Round 2 (independent adversarial)

**Document under review:** `gallic_Doc03_Lexicon_Candidates.md`, status REVISED (Round 1 revision, 2026-09-09) — Lexicon Candidate List, Gallic Monastic-Ascetic Christianity (Atlas I.27, era 2).
**Reviewer:** independent, fresh context; no part in drafting, in Round 1, or in the revision pass.
**Date:** 2026-09-09.
**Read in full for this review:** `gallic_Doc03_Review_Round1.md`; the whole live `gallic_Doc03_Lexicon_Candidates.md` (913 lines); `gallic_Source_Registry.md` rows 1–17 and 24–44; `gallic_Doc01_World_Identification.md` §8 and §10–11; `gallic_Doc02_Source_Ecology.md` §13A.
**Primary sources consulted directly this round:** `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (raw XML, so that `<note>`/`<div>` boundaries are visible and the ancient/editorial split is decidable); `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` (raw XML); `cic/texts/salvian_on-the-government-of-god_sanford1930.txt` (read at every cited locus, plus Book I in full).

---

## VERDICT

**BOUNDED REVISION REQUIRED — four items.**

**Answer to the question this round exists to settle, stated first:** **no Round 1 fix turned out to be a false claim.** Every one of S1–S9 and C1–C7 that the §11 log says was applied is physically present in the live file, in the right place, and the Appendix was synchronised with it. I re-ran every mechanical count the log reports (AS 7, SC 74, PV 5, CT 7, Tier-1 16, Appendix rows 81, headings marked "unverified" 28, 16/81) and reproduced all of them exactly, and I checked Origin/Risk-Function tag agreement between every entry and its Appendix row mechanically across all 81 rows — agreement is perfect. The repeated failure mode of this build (fix claimed in the log, edit never landed or landed in the wrong place) **did not recur here.**

**What is wrong instead is a different and subtler thing:** the revision fixed the *bookkeeping* correctly while accepting the *reviewer's factual assertions* without re-running them. The S5 fix converted Round 1's word-boundary search result into ~28 bold, load-bearing negative claims in entry headings ("unverified — no lemma in the vendored translation"), and at least ten of those claims are false against the vendored file — the lemma is present, in inflected form, in the volume's own editorial apparatus. One of them (1.9 *professio*) carries a locus that is not merely imprecise but points into a work the document itself declares unread. And the S1 retag, though executed exactly as claimed, applies its own stated criterion inconsistently to the two entries that keep `[AS]` on Cassianic evidence.

**Bounded to:** N1 (the false "no lemma" claims), N2 (1.9's locus), N4 (the `[AS]` criterion at 5.3/5.6), N5–N7 (three small bookkeeping omissions created by the Salvian addition and the S5 fix). Everything else in the revision is sound, and the Salvian sweep — the most consequential new content and the thing I was asked to test hardest — **checks out completely against the source**.

---

## What I verified against source text, vs. structure only

**Verified against primary source text this round (I opened the file and read the passage):**
- All 15 Salvian loci cited at 1.13, 6.10, 1.1, 1.10, 1.11, 3.11, 8.8 — book, chapter, page, and wording (details in S6 below).
- Gennadius ch. LXVIII on Salvian in the raw `npnf203` XML, including whether the *De gubernatione Dei* gloss is ancient text or Richardson's `<note place="end">`.
- Gennadius ch. XIX (`v.iv.xx`) in raw XML, re-confirming the ancient/editorial split Round 1 passed.
- *Conf.* XIII.18's "first stage in the Divine gift" / "second stage in Divine grace" / "persistence of the goodness already acquired" (C1, and 5.4's third stage).
- The Conference authorship map (`iv.iv.*`, `iv.v.*`, `iv.vi.*` div titles): Conf. I–II Moses, III Paphnutius, XI–XIII Chæremon, XIV–XV Nesteros, XVIII Piamun, XXIV Abraham. This is what decides N4.
- Word-boundary and inflected-form searches over the whole `npnf211` file for 23 Latin lemmas asserted in headings, with the enclosing `<div>` located for every hit (this is what decides N1, N2, N3).
- Named spot-checks of Round 1's own passed list: the Sarabaite Egyptian-language phrase, "of which they reckon eight," "which we have seen observed throughout Egypt," "Institutes which are not mine but the fathers'," "discretion is the mother of all virtues," "the blessed Antony," the sackcloth disapproval, the "midday demon," "By purity of heart…," "expelled from the monastic system as unworthy," "this province that is frozen as it were with the cold of Gaul." All present. (I ran a deliberate negative control through the same method to confirm the method reports misses.)
- Heurtley's Appendix III (`iii.xxxvii`), which Round 1 explicitly did not open — it is indeed the note on Celestine's letter, so 7.2's CT-type claim is accurate at the level of subject.

**Checked structurally only, not re-verified against source:** the ~50 quotations Round 1 verified and did not change (I re-checked ten of them, listed above, and re-checked that the revision did not alter the surrounding Evidence lines); the tier estimates; the substantive accuracy of the Distortion-Risk one-liners; Doc_01's and Doc_02's own findings where Doc_03 relies on them; the unvendored/Latin-only rows 24–29, 32 (I confirmed the files exist and read the Registry's own text about them).

---

## Round 1 findings, verified item by item

| # | Verdict | Note |
|---|---|---|
| **S1** | **PARTIAL** | Retag executed exactly as claimed; criterion applied inconsistently at 5.3 and 5.6 (→ N4) |
| **S2** | **PASS** | |
| **S3** | **PASS** | All four counts independently recomputed |
| **S4** | **PASS** | |
| **S5** | **PARTIAL** | Marking landed on 28 headings; ~10 of the marks assert a falsehood (→ N1, N2, N3) |
| **S6** | **PASS (evidence) / PARTIAL (bookkeeping)** | Every Salvian locus verified; three small errors created (→ N5, N6, N8) |
| **S7** | **PASS** | All 15 rows added + row 3 removed from 1.1; new omissions created elsewhere (→ N7) |
| **S8** | **PASS** | |
| **S9** | **PASS** | |
| **C1–C6** | **PASS** | |
| **C7** | **PARTIAL** | The two rows Round 1 itemised are fixed; the same under-reporting survives in three other rows |

### S1 — retag `[AS]`→`[SC]` on 13 Egyptian-derived entries. **PARTIAL.**

**What actually landed (verified).** `[AS]` now appears in exactly seven Tags lines in the whole file — 5.3 (L393), 5.6 (L419), 7.2 (L548), 7.4 (L564), 7.5 (L572), 7.13 (L636), 8.8 (L714) — and nowhere else outside §0's tag key. All thirteen named entries (1.4, 3.5, 3.6, 3.7, 3.8, 4.1, 4.2, 4.4, 4.5, 4.6, 4.9, 4.10, 8.6) now read `[SC]`, each with a one-clause "received" note, and 3.11 was additionally retagged with its reasoning stated. The Appendix Origin column names exactly the same seven AS rows. `[AS]` survives on none of the thirteen. **This fix is real and complete.**

I also independently confirmed the "received" justifications: Conf. I–II are Abbot Moses's, Conf. III Paphnutius's, Conf. XI Chæremon's, Conf. XIV Nesteros's, Conf. XVIII Piamun's — so 4.1, 4.2, 4.4, 4.9, 4.10, 3.7's Egyptian-council framing, and 1.4's "in the Egyptian language" are each correctly grounded.

**Where it fails.** Of the seven `[AS]` retentions, the four Vincentine ones (7.2, 7.4, 7.5, 7.13) and 8.8 pass the Framework's comparative test cleanly against Doc_01 §8's neighbour list. **5.3 and 5.6 do not** — see **N4**. The revision moved the problem rather than solving it for those two.

### S2 — §9.1's "all three voices" list. **PASS.**

L734 now lists nine terms (3.2, 3.3, 3.4, 7.3, 6.4, 7.1, 7.11, 1.12, 3.10); I checked each against its own Voices line and Appendix Voices cell — all nine read "All three" / "S C V" consistently. 1.1 and 2.1 are moved to a new two-voice line (L736). 1.6 is removed (L738) and its Voices line now states the Vincent evidence honestly as "the same English word, a different referent," on 1.10's pattern. §9.2 item 1's stated ground is corrected. 2.1's AG line is corrected. Appendix 1.6 reads "S C (V other referent)".

### S3 — arithmetic. **PASS on all four counts, recomputed independently.**

- "Cassian only (14)": I extracted every AG line reading "single-voice (Cassian)" — 1.4, 1.8, 3.7, 3.8, 3.11, 4.1, 4.2, 4.4, 4.5, 4.6, 4.9, 4.10, 4.12, 5.6 = **14**, and §9.1's enumeration names exactly those fourteen. (1.2's qualified "Cassian-only (single-voice)" on a *distinction* is correctly excluded, as it was at Round 1.)
- Appendix rows: **81**, no duplicates, no gaps, in order; section counts 13+4+11+12+9+10+14+8 = 81.
- Tier-1 flags: **16** entries carry "Tier (est.) 1" (1.1, 1.11, 2.1, 3.2, 3.3, 3.7, 4.1, 5.1, 5.2, 5.3, 6.1, 6.4, 7.1, 7.2, 7.3, 8.1), and the Appendix Tier column returns the identical set.
- 16/81 = 19.75%, "≈ 20%" ✔.
- The subsidiary counts are right too: Vincent only (4), Sulpitius only (3), Salvian only (2).

### S4 — *virtus* double-filing. **PASS.**

6.1 is routed only under "Cross-voice tension" (L732). Its appearance in the Sulpitius-only paragraph (L730) is an explicit removal note, not a filing.

*(Residual, not new and not introduced by this revision: **3.3** is still filed in both "Cross-voice tension" and "Genuinely shared across all three voices." Unlike 6.1's case this is defensible — 3.3's own AG line reads "none as a term; cross-voice tension in referent," which is genuinely both — but a Doc_04 reader following §9.1 as a routing instruction will meet it twice. Round 1 did not flag it; I record it so it is a decision rather than an oversight.)*

### S5 — unverified Latin lemmas. **PARTIAL — the marking landed, the claims it makes are often false.**

**What landed (verified).** Exactly **28** entry headings contain "unverified." The remaining lemma-bearing headings are all footnote- or apparatus-attested (*monasterium*, *acedia*, *gratia*, *virtus*, *cilicium*, *papa*, *summus sacerdos*, *Tractatores*, and the four editorial-layer lemmas). §0's "Built from" paragraph and Discipline 2 now describe the practice as it actually is. §10 item 1 is updated. **3.5's heading does disclose the collatio trap** rather than relocating it.

**Independent lemma spot-checks I ran that Round 1 did not (word-boundary, whole file, exact form):** *traditio* 2, *communio* 0, *religiosi* 0, *theoria* 0, *initium* 0, *regula* 2, *collatio* 3, *discretio* 0, *puritas* 0, *gubernatio* 0, *signum* 0, *novitas* 0, *permutatio* 0, *perfectio* 0, *compunctio* 0, *cogitationes* 0. The document's zero-claims for *theoria* (4.10), *initium fidei* (5.3), *puritas* (4.1), *discretio* (3.7), *novitas* (7.3), *permutatio* (7.5), *perfectio* (4.3), *compunctio* (4.8), *cogitationes* (4.4), *signum crucis* (2.3), *religiosi* (1.13) and *gubernatio Dei* (6.10) are **correct**. The *militia* (2.1), *fratres* (1.6), *perseverantia* (5.4) and *regula* (3.6/7.2) claims are substantially correct; I located each witness and confirmed the layer.

**Where it fails: N1, N2, N3 below.** Ten-odd headings assert a negative that the file contradicts, and one of them (1.9) is a wrong locus into an unread work.

### S6 — Salvian disposition. **PASS on the evidence. PARTIAL on the bookkeeping.**

This is the strongest part of the revision and I tested it hardest. **Every single Salvian claim checks out.** I located each quotation in `salvian_on-the-government-of-god_sanford1930.txt`, resolved its Book from the file's own book headers, its chapter from the file's own bare-numeral chapter markers, and its page from the running heads:

| Doc_03 claim | Verified |
|---|---|
| 1.13 "Religious men are lowly … they rejoice in weakness" — *Gov.* I.2, pp. 42–43 | ✔ Book I, ch. 2, p. 42 (verbatim; OCR reads "fiee" for "flee") |
| 1.13 "the religious are happier than all others in this, that they have what they wish" | ✔ Book I, ch. 2, p. 43 |
| 1.13 "toil, fasting, poverty, humility and weakness are not burdensome" | ✔ Book I, ch. 2, p. 43 |
| 1.13 "the religious who have gained some reputation by a general repentance and now seek after new honors" — V.10, pp. 153–4 | ✔ Book V, ch. 10, p. 153 |
| 1.13 / 1.1 "the monks — that is, for the servants of God" — VIII.4, p. 229 | ✔ Book VIII, ch. 4, p. 229 |
| 1.13 / 1.11 "make a show of renouncing their wealth … make their renunciation complete" — III.3, p. 83 | ✔ Book III, ch. 3, p. 83 |
| 1.10 "repent of their conversion"; "professing physical continence" run "riot in incontinence of spirit"; "this is not conversion to God but aversion from him" — V.10 | ✔ Book V, ch. 10, pp. 153–154 |
| 1.10 "the conversion of one man does not atone for the sins of the many" — III.11 | ✔ Book III, ch. 11, p. 96 |
| 1.11 "I renounce the devil, his pomps and spectacles and his works" — VI.6 | ✔ Book VI, ch. 6, p. 168, and it *is* the baptismal renunciation, as the entry says |
| 3.11 "a lukewarm Christian and hateful to the Lord"; "cast out because of lukewarmness"; Rev. 3:15–16; "do not justify their profession of faith" — IV.19, pp. 130–131 | ✔ Book IV, ch. 19, pp. 130–131, and the referent **is** ordinary Christians, not monks |
| 8.8 "the country of the Belgae burst into flames … the whole body of the Gallic provinces" — VII.12 | ✔ Book VII, ch. 12, p. 204 |
| 8.8 "'we Gauls' is not his phrase in what was read" | ✔ zero occurrences in the file |
| 6.10 helmsman "never takes his hand from the tiller"; "never turns his most gracious eyes from the whole extent of the world"; "careless and neglectful of human actions" — I.1, pp. 39–40 | ✔ Book I, ch. 1, pp. 39–40 |
| 6.10 "the present judgment of God was clearly shown" — VII.10, p. 201 | ✔ Book VII, ch. 10, p. 201 |
| 6.10 "We are judged by the ever-present judgment of God, and thus a most slothful race has been aroused…" — VII.12, p. 203 | ✔ Book VII, ch. 12, p. 203 |
| 1.1 "his one use of the word" (monks) | ✔ "monk/monks" occurs once in Salvian's own text (VIII.4); the other hits are Sanford's Introduction, two footnotes, and the index |
| 1.13 Sanford's Seneca footnote at I.2 | ✔ there is a Seneca *De remediis fortuitorum* note at exactly that point — evidence the sweep was real, not reconstructed |

**Gennadius corroboration for 6.10 — verified in the raw XML, including the layer split.** Gennadius **ch. LXVIII** (div `v.iv.lxix`) reads, in the ancient text, "five books *On the present judgment*"; the gloss "*present judgment* more generally known as *Divine Providence* (De gubernatione Dei.)" is a `<note place="end">`, i.e. Richardson's. Doc_03 attributes it to Richardson and rows it to 42. **Correct.** The ancient-vs-editorial discipline held on the one genuinely new Gennadius chapter this revision read.

**Does Salvian support "a fourth Native voice inside the southern node"?** Yes, on this build's own rules. Registry row 43 is Native/Confidence A with a Boundary Check (Doc_02 §13A) resting on three independent ancient lines, two of them already vendored — Hilary of Arles's funeral sermon naming Salvian "*charorum suorum unus*", Eucherius's letter, Gennadius. Licensed For expressly includes "Doc_06 lexicon" and expressly excludes the grace/free-will controversy, and Doc_03 honours that exclusion exactly (nothing added to §5; 6.10 says so in its own Tier line). The document also declines to make Salvian a fourth *node*, correctly, and §10 item 5 states the node placement (a second Marseilles voice inside the southern node) consistently with Doc_01 §6. **This did not need a boundary/scope escalation.** It does need the small repairs at N5, N6 and N8.

### S7 — missing Registry rows. **PASS.**

I printed all 81 Registry lines and checked each of the 15 named additions against the entry's own Evidence line and the Registry's row definitions (row 7 = *Institutes*, 8 = Conf. I–X, 9 = Conf. XI–XVII, 10 = Conf. XVIII–XXIV, 13 = *Commonitory*, 1/2/3/5/6 = the Sulpitian works). **All 15 present and correct**: 1.6→7, 1.10→7, 2.1→13, 2.4→3, 3.4→10, 3.7→7, 5.8→9+13, 6.3→10, 6.8→9+10, 7.1→10, 7.3→10, 7.6→1, 7.12→6, 8.4→13, 8.7→8. Row 3 is removed from 1.1 with a stated reason (also closing C3). No Excluded row (4, 33–38, 44) is used as evidence anywhere; row 36 still appears exactly once, explicitly as an excluded comparandum. New omissions were nevertheless created at 1.9 and 5.4 — see N7.

### S8 — CT on 7.1 and 5.4. **PASS.**

`[CT]` now appears in exactly seven Tags lines: 5.1, 5.2, 5.3, 5.5, 5.8, 7.2, 7.5. Neither 7.1 nor 5.4 carries it; both retain `[DR]`, with the modern-hearing gap restated as a Distortion note. Appendix CT cells match the same seven. 5.2's CT type is now stated in full rather than by cross-reference.

### S9 — PV on 1.4 and 8.4. **PASS.**

`[PV]` now appears in exactly five Tags lines: 6.1, 7.8, 7.10, 8.1, 8.5 — Round 1's own list of the five good applications. Neither 1.4 nor 8.4 carries it; each states why in its own Tags line. Appendix PV cells match.

### C1–C7

- **C1 PASS.** Neither 5.1 nor 5.4 quotes the composite. 5.1 gives the text's own two phrasings; I confirmed both against *Conf.* XIII.18 in the XML ("the first stage in the Divine gift" … "the second stage in Divine grace" … "held by the persistence of the goodness already acquired"). The three residual occurrences of the retired string in the file are the corrective notes themselves and the revision log.
- **C2 PASS.** Appendix 4.11 now reads `TC RT (DR on sub-term "canonical")`. My mechanical entry-vs-Appendix tag comparison across all 81 rows found no other divergence.
- **C3 PASS** (folded into S7).
- **C4 PASS.** The *Conf.* Pref. II climate sentence is out of 3.11's Evidence and is marked in its definition as an authorial pun, not an attestation; it still does its honest work at 8.8.
- **C5 PASS.** 5.3 now reads `32 (via npnf211 prolegomena — row 32's own text is unvendored and unread…)`.
- **C6 PASS.** 5.1's AG line carries the Faustus post-window clause (episcopate into the 490s, Doc_01 §6).
- **C7 PARTIAL.** §11's *Letters* and *Dialogues* rows now have complete outputs columns. But Round 1's C7 also said "Same pattern in one or two other rows," and it survives: the *Institutes* row still reports outputs as "§§1, 3, 4, 8" although Institutes loci are cited at 2.1, 2.2, 2.3, 5.4, 6.2, 6.4, 7.3 and 8.5–8.6; the *Conferences* row reports "§§3–5, 1.3–1.4, 4.10–4.12" although Conferences are cited throughout §§2, 6, 7 and 8; the *Commonitory* row reports "§7 throughout; 5.8, 5.9" although the *Commonitory* is cited at 1.12, 2.4, 3.1–3.4 and 3.10. Cosmetic, as before.

---

## New findings

### N1 (SUBSTANTIAL). At least ten of the 28 "unverified — no lemma in the vendored translation" heading claims are false against the vendored file — and they were introduced by this revision.

Round 1's word-boundary search was for **exact nominative forms only**. The revision adopted its result as a verified negative and hardened it into bold, load-bearing heading claims, without re-running the search for anything except *militia*, *initium* and *theoria*. Searching the same file for **inflected forms** shows the lemma is present, in the volume's own editorial apparatus, for at least the following — in most cases in the very sense the entry defines:

| Entry | Heading asserts | Actually in `npnf211` |
|---|---|---|
| **1.1** *monachus* | "no lemma in the vendored translation" | `iii.i` (Heurtley's Introduction): "**Monasterium potest unius monachi habitaculum** nominari."—Cassian. *Collat.* xvii. 18. Also "Monachos" in a title citation |
| **1.5** *cella* | same | same locus: "Tota ubique insula, exstructis **cellulis**, unum velut monasterium evasit" (of Lérins) |
| **1.10** *conversio* | same | `iv.vi.viii.i` (*Conf.* XXIV.1, Gibson's textual fn.): "Petschenig's text reads ***conversione***, others *conversatione*" — the monastic *conversio/conversatio* crux, exactly this entry's sense |
| **1.11** *renuntiatio* | same | `iv.i.ii` (Gibson's Prolegomena, MS/edition history): "*Ioannis Cassiani* … de institutis **renuntiantium** Libri XII" — the Latin title of the very book whose chapter-title 1.11's Evidence quotes |
| **3.1** *magister* | same | four occurrences (*magistro* ×2, *magistri*, *magistris*) in Roberts's/Gibson's notes |
| **3.2** *exemplum* | same | `iv.iii.iii.iv` (*Inst.* III.4, Gibson's fn.): "Trinæ confessionis **exemplo**"; also *exempla*, *exemplar*, *exemplaribus* |
| **3.6** *instituta* | same | `iv.i.ii`: "*De* **Institutis**" / "de **institutis** renuntiantium"; also *institutionum* |
| **5.7** *meritum* | same | `iii.xxxvi` (Heurtley's Appendix II), quoting Augustine's *De dono persev.* in Latin: "quod gratia præceditur **merito** nostro" — precisely 5.7's grace-and-merit sense |
| **6.3** *benedictio* | same | Gibson's fn.: "*collecta oratione* ad vesperam ab Episcopo cum **benedictione**"; also *benedictionis*, *benedictis* |
| **7.6** *tentatio* | same | "**tentationis** periculum" in a note |
| **7.11** *communio* | same | "in Ecclesia sua, id est, in **communionis** suæ conventiculo" |
| **3.5** *collatio* | "the word does occur … three times, but all three are in Vincent's etymology"; as the genre name the lemma is "unverified in this corpus" | The three exact-form hits are indeed Vincent's. But **five further inflected occurrences** are the Cassianic genre: `iv.i.ii` "**Collationes** SS. Patrum XXIIII", "in singulis **collationibus**", "precedenti **Collationi** ab ipso substituta"; `iii.i` "Cassian. **Collat.** xvii. 18" |

§0 Discipline 2 repeats the same false negatives generically ("zero occurrences of, among others, *puritas*, *discretio*, *depositum*, *renuntiatio*, *compunctio*, *monachus*, *cella*, *magister*, *cogitationes*"): of that list, *renuntiatio*, *monachus*, *cella* and *magister* are wrong.

**Why this matters, and why it is not merely pedantic.** (a) These are the only sentences in the document that make a *verified* factual claim about the Latin, and Doc_06 is instructed to build a lemma-verification pass on them; a false negative tells Doc_06 to stop looking exactly where the witness is. (b) The corrected version is *better* for the build, not worse — several of these witnesses (the *Institutes*' own Latin title, the *conversio/conversatio* variant, "gratia præceditur merito") are genuinely useful. (c) Most of these loci sit in sections §11 declares unread (Prolegomena, Heurtley's Introduction and Appendices, *Inst.* III, *Conf.* XXIV), so this is a coverage consequence, not carelessness — but it must be stated as one. (d) It is the *collatio* trap in reverse, in the same document that congratulates itself on disclosing the collatio trap.

**Suggested fix.** Re-run the lemma search on inflected forms; change the false headings to "attested in the volume only in the editorial apparatus at *[locus]*"; correct §0 Discipline 2's list; and add one clause to §10 item 1 noting that the volume's Prolegomena and the translators' Latin apparatus are themselves an unswept lemma source.

### N2 (SUBSTANTIAL). 1.9's *professio* witness is at the wrong locus, and the true locus is in a work the document declares unread.

1.9's heading reads: "*professio* — corpus-supported only in **Gibson's textual footnote at *Conf.* Pref. I**, Petschenig's reading against Gazæus's, editorial layer, Registry row 17." §10 item 1 repeats "exact loci at 1.6, **1.9**, 3.6, 5.4."

There is exactly one occurrence of *Professio* in the whole volume. It is at **`iv.vii.i` = the Preface to Cassian's *On the Incarnation of the Lord, Against Nestorius*** — `<note>` reading "*Professio* (Petschenig): *Progressio* (Gazæus)", attached to the words "Great is the honour but most perilous the undertaking." That work is **Registry row 12**, which §10 item 3, §11's coverage table and entry 7.14 all state was **not read this pass**.

Round 1 made this locus error first; the revision copied it verbatim without opening the file. The claim "exact locus" is therefore not true of 1.9, and the entry's one "corpus-supported" citation reaches into unread territory that the document's own Discipline 1 forbids filling in silently. Round 1's check #79 — that every Cassian locus falls inside a declared-read section — no longer holds for this one citation as a matter of fact, though it still holds as written.

**Fix:** correct the locus to the *De Incarnatione* Preface, add row 12 alongside row 17, and note that the witness sits in an unread work (which is a legitimate disclosure, not a defect, once stated).

### N3 (MINOR). 3.6's *Regula S. Bened.* footnote is at *Inst.* I.11, not I.10.

3.6's heading and §10 item 1 place Gibson's RB c. lv footnote "at *Inst.* I.10." It is at `iv.iii.i.xi` = **Book I ch. XI, "Of the Spiritual Girdle and its Mystical Meaning."** (Inst. I.10 is the climate-modification chapter, which 3.6 and 8.6 cite correctly for the climate clause — the two are being conflated.) A second RB witness exists in the Prolegomena's edition description ("Accedit **Regula** S. …"), so 7.2's "the volume's only *regula* witness" is also one witness short, though both are RB and 7.2's substantive point survives. Again inherited verbatim from Round 1 without checking.

### N4 (SUBSTANTIAL). The S1 retag criterion is applied inconsistently: 5.3 and 5.6 keep `[AS]` on evidence that is entirely reported Egyptian teaching.

§0's revised tag key states the criterion the retag used: "vocabulary Cassian himself frames as received Egyptian teaching is tagged `[SC]` with a 'received' note." Applied to 4.9, the note reads "received (Abbot Chaeremon, *Conf.* XI)"; to 4.2 and 4.4, "received (Abbot Moses, *Conf.* I)".

**5.6 co-operation** keeps `[AS]`. Its entire Evidence line is *Conf.* III.12 and *Conf.* XIII.13, XIII.17. I confirmed from the XML's own division titles that **Conference III is the Conference of Abbot Paphnutius** and **Conference XIII is the Third Conference of Abbot Chæremon** — the same abbot whose Conf. XI material was retagged `[SC]` two sections earlier, and the same reported-conference frame. The chapter closes "Strengthened by this food the blessed Chæremon prevented us from feeling the toil of so difficult a journey."

**5.3 the beginning of a good will** keeps `[AS]` on the identical basis: *Conf.* XIII.3, 7, 11, 12 (Chæremon) and *Conf.* III.19 (Paphnutius). Its own heading additionally concedes that the English headword "beginning of faith" is *Augustine's translators' phrase*, and Doc_01 §8.4 names `pelagianism` as a neighbouring world — the one world where this exact question carries equivalent weight.

The document's actual defence for these two is a *different* criterion — that they are "this world's own formulation of its own argument," i.e. what the world made of received material — which is a real and arguable position, but it is not the criterion §0 states, and it is precisely the argument that would also rescue *purity of heart* and *discretion*. Right now the same evidence shape gets two different Origin tags in the same document. Round 1 endorsed keeping `[AS]` here, so this is inherited rather than invented; but I was asked to test it independently, and it does not pass.

**Fix (either direction is defensible, but one must be chosen and stated):** either retag 5.3 and 5.6 `[SC]` with a "received, then made this world's own" note, or restate §0's criterion so that it is about *what a world argues with a received vocabulary*, not about whether the vocabulary was received — and then re-test the thirteen retagged entries against the restated criterion.

### N5 (MODERATE). The Appendix Voices column was not updated for four of the five Salvian attestation notes — and now contradicts an entry.

The Appendix legend was correctly extended ("Sv=Salvian, row 43, fourth Native voice"), and 3.11's row uses it ("C (Sv non-monastic)"). But the four other entries that gained Salvian attestations did not:

| Entry | Entry's Voices/AG line now says | Appendix Voices cell still says |
|---|---|---|
| 1.1 | Sulpitius, Cassian; Gennadius; **Salvian** | `S C` |
| 1.10 | AG: "the monastic sense is **Cassian's and Salvian's**" | `C (S other sense)` |
| 1.11 | Cassian; Sulpitius; **Salvian** | `S C` |
| 8.8 | Sulpitius, Cassian; Gennadius; **Salvian** | `C S (G)` |

1.10 is a direct contradiction: the entry now claims two voices for the monastic sense, the Appendix one. §0 Discipline 3 calls the per-term voice attestation "the single most important classification in the document for Doc_04's purposes," and the Appendix is the filtering surface Doc_04 will actually use. This is the same defect class as S2, newly created by the S6 fix.

### N6 (MODERATE). 6.10's Registry line cites the wrong row.

6.10's Registry reads "43; 30 and 42 (the title witness); **13 and 8** for the contrast terms." The contrast terms named in its Voices line are Vincent's *Comm.* ch. 1 [2] (row 13 ✔) and **Cassian's *Conf.* XI.6** — which is Registry **row 9** (Conferences XI–XVII), not row 8 (Conferences I–X). The document maps Conf. XI to row 9 correctly everywhere else (4.3, 4.9). Additionally, Sulpitius's imminent-Antichrist material, also named as a contrast term, draws on rows 1–3, none of which is listed. This is an S7-class defect in one of the two brand-new entries.

### N7 (MINOR). Two of the four new editorial-lemma citations name Registry row 17 in the heading but omit it from the Registry line.

- **1.9** heading: "editorial layer, **Registry row 17**." Registry line: `1, 3, 7, 8, 10.` — no 17.
- **5.4** heading: "Roberts's footnote on Halm's reading **in the *Doubtful Letters***, editorial layer, **Registry row 17**." Registry line: `1, 7, 8, 9, 14, 16.` — no 17, **and no row 5**, which is the *Doubtful Letters*, the work the new citation comes from. (I confirmed the *perseverantia* note is at `ii.v.i.i`, Doubtful Letters, Letter I ch. I.)

1.6 does list row 17; 3.6 correctly lists row 36. So the omission is inconsistent, not systematic — the S5 fix created two new instances of exactly the S7 defect the same pass was closing.

### N8 (MINOR). Salvian carries no temporal note, though C6 required one for Faustus.

C6 obliged 5.1 to disclose that Faustus's episcopate runs past this world's c. 450 window. Salvian gets no equivalent clause anywhere: the document never dates *De gubernatione Dei*, and the very Gennadius chapter this revision read (ch. LXVIII) says of Salvian "He is still living at a good old age," with Richardson's endnote giving "died about 484." The build's own Boundary Check rule is subject-based, not date-based, so this is not a licensing problem — but the asymmetry with C6's own precedent is visible, and 6.10's evidence (the Gothic/Vandal ruin of the Gallic provinces) is precisely the material a reader will want dated relative to the window.

### N9 (MINOR). Two traceability gaps opened by the Salvian pass.

- 6.10's Evidence cites "**Sanford's Introduction** (editorial) discusses the same discrepancy" and 1.13's Evidence discusses Sanford's footnotes. Sanford's 1930 apparatus is a distinct modern editorial layer with **no Registry row** — the exact gap Registry row 42 was created to close for Richardson and row 17 for the NPNF translators. Either propose a row or restrict the citations to the ancient text.
- §10 item 6's Registry-maintenance proposals (rows 2, 3, 6, 8/9/10, 13, 14–16) do **not** include row 30, although this revision read a new Gennadius chapter (LXVIII) beyond the seven row 30's Verification Note records.

### N10 (COSMETIC). A bracketed tag token still sits inside an explanatory note.

§11's mechanical-check paragraph claims "no retired tag appears as a literal bracketed token inside a Tags line, so a mechanical scan cannot mistake a note for a tag." **1.3**'s Tags line reads `[SC] [TC]. Not [RT] as a self-description…`. The token is a never-applied tag rather than a retired one, so the log's claim is literally true — but the stated purpose is defeated, and my own automated entry-vs-Appendix comparison flagged 1.3 as the sole false positive in 81 rows because of it.

### N11 (OBSERVATION, no action required). Salvian's "monasteries" was swept for and not recorded.

§11's sweep lists "monastery" among its search terms. Salvian's own text uses it twice at *Gov.* VIII.4–5 ("they in evil dens, these in monasteries"; "any servant of God from the monasteries of Egypt or the sacred places of Jerusalem"), which would be a genuine fourth-voice attestation for **1.2**. Not recorded there. Recording the negative ("swept, judged not to add") or the attestation would close the loop.

### N12 (OBSERVATION). §0 was not fully reconciled with the fourth voice.

The "Built from" paragraph, §9.1 and §10 item 5 all name Salvian. **Discipline 3** ("three voices, not one") and the **Entry format** line ("*Voices* (which of the three primary voices attest it; node)") were not touched. The two new entries handle this by disclaiming ("outside the three of §0 Discipline 3"), which is honest; but §0 remains the place a reader learns the scheme, and it still describes a three-voice document.

---

## Checks that passed this round, recorded so Round 3 (if any) need not redo them

1. **No false fix claims.** Every S1–S9 and C1–C7 edit the §11 log claims is present in the live file. I reproduced independently: `[AS]` = 7 entries and the same 7 Appendix rows; `[SC]` = 74 Tags lines (74+7 = 81); `[PV]` = 5; `[CT]` = 7; Tier-1 = 16 in both entry text and Appendix; Appendix rows = 81 with no duplicate, gap or ordering error; headings containing "unverified" = 28. The residual hits for the strings the log says it grepped to zero ("Cassian only (11)", "not yet in the library", "Pref. II (the Gallic cold)") occur **only inside the revision log's own text**, i.e. the greps were run before the log was written, as the log states.
2. **Entry↔Appendix tag agreement is exact across all 81 rows** (mechanically compared; the only flag was N10's false positive at 1.3).
3. **The ancient-vs-editorial discipline held on the new material.** Gennadius ch. LXVIII's *De gubernatione Dei* gloss is correctly identified as Richardson's endnote and rowed to 42; Gennadius ch. XIX's "Virtues or miracles." is still correctly identified as a footnote; the ancient text at ch. XIX still carries everything Doc_03 attributes to it.
4. **Boundary discipline holds.** No candidate draws on an Excluded row (4, 33–38, 44) as evidence. Row 36 appears once, explicitly as an excluded comparandum. No *Dialogue I* citation exists anywhere. Row 43's Licensed-For exclusion of the grace controversy is honoured — nothing from Salvian appears in §5.
5. **Coverage discipline holds for Cassian.** Every *Institutes* and *Conferences* locus cited anywhere in the document (Inst. Preface, I, IV, V.1–4, X.1–5; Conf. Prefs I–III, I, II, III, IX.1–3, XI.2–8, XIII, XIV.1–8, XVIII) falls inside a section §11 declares read. The one exception is N2's underlying fact, not the citation as written.
6. **Numbering and cross-reference integrity survived the two insertions.** 1.13 and 6.10 are appended at the end of their sections; nothing was renumbered; no cross-reference to another entry number is stale; the Appendix legend, §9.1's new Salvian line, §9.2's count and §10 item 5 all agree.
7. **No Doc_06 drift.** No entry carries a World Meaning, Ecological Function, paired hearings, Related Terms, or a deployment chunk. 1.13 and 6.10 are quote-dense but stay within the "one to three sentences" definition band as the existing outliers (5.1, 6.1, 8.6) do.
8. **The §9.1 "all three voices" list is now internally true**: all nine remaining terms read "All three" in their entries and "S C V" in the Appendix.

---

## Disposition

**Not Approved to Proceed — bounded.** Four items should be closed before Doc_04 begins, because Doc_04 consumes §9.1's routing and Doc_06 consumes the tags and the lemma line:

1. **N1** — correct the false "no lemma" claims (and correct §0 Discipline 2's list). This is mechanical and the corrected version is more useful than the current one.
2. **N2 / N3** — correct 1.9's and 3.6's loci; add row 12 at 1.9 with the unread-work disclosure.
3. **N4** — decide, and state, which `[AS]` criterion governs, and apply it consistently to 5.3 and 5.6.
4. **N5 / N6 / N7** — four Appendix Voices cells, one Registry row, three Registry-line omissions.

N8–N12 are one-clause additions that can ride along in the same pass.

**Explicit note for the build thread on this world's documented failure mode.** The failure this round is *not* the one the brief expected. Nothing was claimed and not done. What happened instead is that the revision treated the Round 1 reviewer's factual assertions — a word-boundary search result, two footnote loci — as verified findings and built bold claims on top of them without opening the file. Every one of those inherited assertions that I checked (three of three: the lemma search, the *professio* locus, the *regula* locus) turned out to be wrong in detail. **The lesson that generalises: an adversarial review's own factual claims are not a verified source, and a revision that copies them into the document converts a reviewer's shortcut into the document's own assertion.** Where the revision did its own work — the Salvian sweep, every locus of which I checked and every one of which is right down to the page — it is the best evidentiary work in this world's build so far.

**Disagreement log (Round 2 vs. Round 1):**
- Round 1 S5 stated that the corpus-supported lemmas are four (*fratres*, *professio*, *regula*, *perseverantia*) and that ~21 named lemmas have zero occurrences. **I disagree in part**: the search was exact-form only; on inflected forms the volume supports at least *monachus*, *cella*, *conversio*, *renuntiatio*, *instituta*, *magister*, *exemplum*, *meritum*, *benedictio*, *tentatio*, *communio*, *traditio*, and *collatio* in the Cassianic genre sense (N1).
- Round 1 placed the *professio* footnote at *Conf.* Pref. I and the *Regula S. Bened.* footnote at *Inst.* I.10. **I disagree**: they are at the *De Incarnatione* Preface and *Inst.* I.11 respectively (N2, N3).
- Round 1 listed 5.3 and 5.6 among the terms that "survive the `[AS]` test unchanged." **I disagree**: both rest wholly on reported conferences of Egyptian abbots (Paphnutius, Chæremon), which is the frame that triggered the retag elsewhere (N4).
- On everything else — S1's core diagnosis, S2, S3, S4, S6, S7, S8, S9, C1–C7, and the whole of Round 1's "Checks that passed" list as re-tested — **I agree with Round 1**, and I confirm those checks still hold after the revision.
