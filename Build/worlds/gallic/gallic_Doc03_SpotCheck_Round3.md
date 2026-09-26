# Doc_03 Spot-Check — Round 3 (bounded)

**Document checked:** `gallic_Doc03_Lexicon_Candidates.md`, status REVISED (Round 2 revision, 2026-09-09), 929 lines.
**Checker:** independent, fresh context; no part in drafting, in Round 1, in Round 2, or in the Round 2 fix pass.
**Date:** 2026-09-09.
**Scope:** bounded verification that the specific Round 2 fix list (N1–N12 plus residual C7) actually landed in the live file, plus one independent mechanical count and a disturbance sweep. **Not** a re-run of Round 1's or Round 2's substantive research.
**Read in full:** `gallic_Doc03_Review_Round1.md`; `gallic_Doc03_Review_Round2.md`; the whole live Doc_03.
**Primary source opened directly this pass:** `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (raw XML, `<div id>` boundaries preserved), for the eleven N1 lemma loci and the two *regula* witnesses. Every claim below marked ✔ was checked in the live file or the vendored XML, not taken from the §11 log.

---

## VERDICT

**DOES NOT CLEAR — three specific remaining defects, all narrow.**

**All thirteen assigned fix items landed.** N1–N12 and the residual C7 are physically present in the live file, in the right place, with the Appendix synchronised. The independent mechanical `[AS]` count **agrees exactly with the document's own claim**. Entry↔Appendix agreement is exact across all 81 rows on Origin, Risk/Function and Tier; the four N5 Voices cells and the N11 cell are correct and 1.10's entry-vs-Appendix contradiction is resolved. Nothing outside the declared ~20-entry-plus-§0/§9/§10/§11 footprint was disturbed: no broken cross-reference, no malformed table, all 81 entries structurally complete, every arithmetic claim (81 rows, 16 Tier-1, 16/81 ≈ 20%, 14/4/3/2 single-voice, Appendix AS/SC 5/76) independently recomputed and correct.

**What is wrong is small but is the build's own two named failure modes, recurring one level down** — one fix claimed in the log that did not land, and one unchecked reviewer assertion copied verbatim into the document. Both are inside the same two headings (3.6 and 7.2). The third defect is two stale §11 lines. All three are single-line edits.

**Recommendation:** a micro-fix pass on R1–R3, then **self-dispose to Approved to Proceed without a further review round** — nothing found here touches the classification layer Doc_04 or Doc_06 consumes.

---

## Part A — the assigned fix list, item by item

### 1. N1 — false "unverified" heading claims

I checked **all eleven** named entries plus 3.5, not the six requested. Every one no longer asserts the false negative; each names a real witness, and **I confirmed each Latin form is actually present in the vendored XML** rather than trusting the correction.

| Entry | Heading now says | Verified in `npnf211` |
|---|---|---|
| 1.1 *monachus* | "not unverified" · Heurtley's Introduction `iii.i`, "*Monasterium potest unius monachi habitaculum nominari*" | ✔ at `iii.i`; "Monachos" also at `iv.iii.iv.xvii` |
| 1.5 *cella* | "not unverified" · same locus `iii.i`, "*exstructis cellulis*" | ✔ `cellulis` ×1 at `iii.i` |
| 1.10 *conversio* | "not unverified" · Gibson's textual fn. at *Conf.* XXIV.1 (`iv.vi.viii.i`) | ✔ "Petschenig's text reads *conversione*, others *conversatione*" at `iv.vi.viii.i` |
| 1.11 *renuntiatio* | "not unverified" · Gibson's Prolegomena `iv.i.ii`, "*de institutis renuntiantium Libri XII*" | ✔ ×1 at `iv.i.ii` |
| 3.1 *magister* (clause only) | "not unverified" · four occurrences in Roberts's/Gibson's footnotes | ✔ 4 occurrences — but see R5 |
| 3.2 *exemplum* | "not unverified" · Gibson's fn. at *Inst.* III.4 (`iv.iii.iii.iv`), "*Trinæ confessionis exemplo*" | ✔ exactly there |
| 3.6 *instituta* | "not unverified" · Prolegomena `iv.i.ii`, "*De Institutis*" / "*de institutis renuntiantium*"; also *institutionum* | ✔ all three at `iv.i.ii` |
| 5.7 *meritum* | "not unverified" · Heurtley's Appendix II (`iii.xxxvi`), "*quod gratia præceditur merito nostro*" | ✔ exactly there |
| 6.3 *benedictio* | "not unverified" · Gibson's fn., "*collecta oratione ad vesperam ab Episcopo cum benedictione*" | ✔ at `iv.iii.ii.vii` = *Inst.* II.7 (no locus given — see R4) |
| 7.6 *tentatio* | "not unverified" · "*tentationis periculum*" | ✔ ×1 at `iv.iii.iii.x` = *Inst.* III.10 (no locus given — see R4) |
| 7.11 *communio* | "not unverified" · "*in Ecclesia sua, id est, in communionis suæ conventiculo*" | ✔ ×1 at `iii.xxxvi` (no locus given — see R4) |

**3.1 handled correctly in structure:** *discipulus* still reads "unverified"; only the *magister* clause is corrected — as the log claims.

**3.5 (*collatio*) states the trap in both directions.** ✔ The heading gives the exact-form hits (three, all Vincent's *Symbolum* etymology at *Comm.* ch. 29–30, "a creed-etymology with no relation to Cassian's genre") **and** the inflected Cassianic-genre hits in the editorial apparatus, and says explicitly that the lemma is attested "only in the editorial layer, not in Cassian's own ancient text, and never in the etymological sense Vincent gives the same three letters." I verified the five inflected hits exist (`Collationes` ×2, `collationibus`, `Collationi` at `iv.i.ii`; `Collat.` at `iii.i`).

**Heading-count sanity:** 27 headings contain the string "unverified"; 10 of those are corrections reading "**not** unverified," 1 (3.1) is mixed. Headings still asserting an unverified lemma = **17**, matching §0 Discipline 2's "the remaining ~17." ✔

**§0 Discipline 2 and §10 item 1** both rewritten to the corrected practice; neither repeats the retired generic false list. ✔

### 2. N2 — 1.9 *professio* ✔ PASS
Heading now cites `iv.vii.i`, "the Preface to Cassian's *De Incarnatione*" — not *Conf.* Pref. I — and states plainly that this is "Registry row 12, which §10 item 3 and §11 state was **not read this pass** — this lemma witness sits in unread territory, disclosed rather than filled in silently." Registry row 12 named as unread. ✔

### 3. N3 — 3.6 *regula* locus ✔ PASS (the locus itself)
Heading now reads "Gibson's footnote at ***Inst.* I.11**" with the bracketed note that I.10 is the climate-modification chapter and "the two loci were conflated." I confirmed `Regula S. Bened. c. lv` sits at `iv.iii.i.xi` = *Inst.* I ch. XI. ✔ **But the second half of the N3 fix is defective — see R1 and R2 below.**

### 4. N4 — 5.3 and 5.6 ✔ PASS, including the self-caught detail
- 5.3 Tags line (L393): `[SC] [TC] [DR] [CT]` — no `[AS]`. ✔
- 5.6 Tags line (L419): `[SC] [TC] [DR]` — no `[AS]`. ✔
- Appendix rows 5.3 and 5.6 both read **SC**. ✔
- **The self-caught N10-class error is genuinely fixed, not merely claimed fixed.** I ran a token-level scan of both Tags lines: the only bracketed tokens present are the applied tags. Both notes read "retagged from **Signature Vocabulary**," spelled out, with no bracket. ✔

### 5. N5 — Appendix Voices cells ✔ PASS
- 1.1 → `S C (G, Sv)` · entry names Salvian (*Gov.* VIII.4). ✔
- 1.10 → `C, Sv (S other sense)` · entry AG reads "the monastic sense is Cassian's and Salvian's." **The direct contradiction is resolved.** ✔
- 1.11 → `S C, Sv` · entry names Salvian (*Gov.* VI.6, III.3). ✔
- 8.8 → `C S (G, Sv)` · entry names Salvian (*Gov.* VII.12). ✔
- Mechanical check across all 81 rows: the set of Appendix rows carrying `Sv` (1.1, 1.2, 1.10, 1.11, 1.13, 3.11, 6.10, 8.8) is **identical** to the set of entries whose Voices/AG text names Salvian. No over- or under-marking. ✔

### 6. N6 — 6.10 Registry line ✔ PASS
Now reads: "43; 30 and 42 (the title witness); 13 (Vincent's contrast term) and **9** (*Conf.* XI.6, Cassian's contrast term — corrected … row 9 covers Conferences XI–XVII, not row 8 …); **1–3** (Sulpitius's imminent-Antichrist contrast term, omitted at Round 1, added Round 2 N6)." Row 8 is gone; rows 1–3 present. ✔

### 7. N7 — 1.9 and 5.4 Registry lines ✔ PASS
- 1.9: `1, 3, 7, 8, 10, 12, 17` — rows 12 and 17 present, with the reason stated inline. ✔
- 5.4: `1, 5, 7, 8, 9, 14, 16, 17` — rows 17 **and 5** present, 5 identified as the *Doubtful Letters*, the actual source of the *perseverantia* footnote. ✔

### 8. N8 — Salvian's dates ✔ PASS
6.10 carries a **Temporal note** naming Gennadius ch. LXVIII ("he is still living at a good old age"), Richardson's endnote ("died about 484"), and dating *De Gubernatione Dei* itself to 439–450 "inside the window" while Salvian's lifespan runs past this world's c. 450 window — explicitly matched to the C6 disclosure required for Faustus, and correctly saying this is not a licensing problem because the Boundary Check is subject-based. ✔

### 9. N9 — §10 ✔ PASS
- **§10 item 8 is new** and proposes "a row for Sanford's own apparatus … parallel to row 42," for the Registry owner, explicitly not created here. ✔
- **§10 item 6** now carries: "**Added, Round 2 N9: row 30 (Gennadius) — this revision read ch. LXVIII (Salvian) beyond the seven chapters row 30's own Verification Note records.**" ✔

### 10. N10 — 1.3 ✔ PASS
1.3's Tags line reads `[SC] [TC]. **Corrected, Round 2 N10:** not tagged runtime-likely as a self-description…`. No literal `[RT]` token remains. ✔

### 11. N11 — 1.2 ✔ PASS
Voices line now carries the Salvian attestation with the exact wording and locus: "'monasteries' occurs twice at *Gov.* VIII.4–5 ('they in evil dens, these in monasteries'; 'any servant of God from the monasteries of Egypt…')." Registry line reads `1, 3, 7, 10, 30, 43` — row 43 present. Appendix 1.2 Voices reads `S C (G, Sv)`. ✔

### 12. N12 — §0 ✔ PASS
- **Discipline 3** retitled "three voices, not one (**now four, per the Round 1 revision's own Salvian sweep, S6 — reconciled here, Round 2 N12**)" and states that row 43 "is a fourth Native voice, distinct from the original three in that it was not part of Doc_02's own founding Author Gravity Assessment and reaches this document through a bounded later sweep." ✔
- **Entry format** line now reads "*Voices* (which of the primary voices attest it — the original three, **plus Salvian where he does, named explicitly per Discipline 3**; node)." ✔

### 13. Independent `[AS]` count — **CONFIRMS the document's claim**

Scan of every line beginning `- **Tags.**` (excludes §0's legend and all §11 log entries), token-matched on `[AS]`:

**Exactly 5 entries: 7.2 (L548), 7.4 (L564), 7.5 (L572), 7.13 (L636), 8.8 (L714).** This reproduces the log's claim precisely. Appendix Origin column returns the **identical five rows**, split 5 AS / 76 SC = 81. ✔

*One note, not a defect:* the **occurrence** count is 6, not 5, because 8.8's own Tags line repeats the token in its explanatory prose ("kept **[AS]** after Round 1 (S1)"). 3.11's line does the same with `[SC]`. In both cases the repeated token is the *applied* tag, so no per-entry mechanical scan can be misled and the §11 log's Round 1 claim ("no **retired** tag appears as a literal bracketed token") remains true. Flagged only because the log records finding a first-pass "overcount of 7" — anyone re-running an occurrence-based grep will get 6 and should not read that as a regression.

### 14. Disturbance sweep — clean
- 81 entries; section counts 13+4+11+12+9+10+14+8 = 81, matching the Appendix row count exactly, no duplicate, gap or ordering error. ✔
- Every one of the 81 entries carries all six required lines (definition, Evidence, Voices, Tags, Tier, AG, Registry). ✔
- **Entry↔Appendix mechanical comparison across all 81 rows:** Origin agrees on all 81; Risk/Function agrees on all 81 (the only two divergences are 1.7 and 4.11, where the Appendix correctly records a sub-term tag — 4.11 is the C2 fix working as intended); Tier agrees on all 81. **No new entry-vs-Appendix contradiction was introduced.** ✔
- Every `N.N` reference anywhere in the document resolves to a real entry. No stale cross-reference. ✔
- No malformed table row anywhere, including the §11 discovery table and the 81-row Appendix. ✔
- Arithmetic re-derived independently: Tier-1 = 16 (1.1, 1.11, 2.1, 3.2, 3.3, 3.7, 4.1, 5.1, 5.2, 5.3, 6.1, 6.4, 7.1, 7.2, 7.3, 8.1), matching §9.2's enumeration and the Appendix; 16/81 = 19.75% ≈ 20% ✔; single-voice AG tallies = Cassian 14, Vincent 4, Sulpitius 3, Salvian 2, matching §9.1's four parentheticals exactly ✔ (5.6 correctly still counted in the Cassian-only block after its Origin retag — Origin and AG are independent classifications and the pass kept them so).
- Residual C7: §11's *Institutes*, *Conferences* and *Commonitory* discovery rows all now carry completed outputs columns naming the loci Round 2 listed. ✔

---

## Part B — remaining defects

### R1 (MODERATE — a fix claimed in the log that did not land). 7.2's heading was never corrected.

§11's N3 entry states: "**7.2's 'only *regula* witness' phrasing corrected** to acknowledge a second RB witness in the Prolegomena, without weakening 7.2's substantive point."

7.2's heading (L544) still reads, unchanged:

> "the volume's **only** *regula* witness is the RB footnote noted at 3.6, which is monastic and editorial, not Vincent's"

The acknowledgement landed **only inside 3.6's heading**, which says "so 7.2's 'the volume's only *regula* witness' undercounts by one." 7.2 itself was not touched. A reader arriving at 7.2 — which is the entry that actually makes the claim, and one of the sixteen Tier-1 entries — still meets the uncorrected assertion. This is precisely this build's documented failure mode (fix logged before the edit landed), recurring at exactly one item in a pass whose §11 log otherwise reports its mechanical re-greps honestly.

**Fix:** one clause in 7.2's heading. Note that once R2 is applied the correct wording is not "a second RB witness" (see below).

### R2 (MODERATE — an unchecked reviewer assertion copied verbatim, one level down). The Prolegomena's second *regula* witness is **Pachomius**, not Benedict.

3.6's new clause reads: "A second **RB** witness exists in the Prolegomena's own edition description ('*Accedit* **Regula** *S.* …')". This is inherited verbatim from Round 2's N3, which asserted "both are RB."

The vendored text at `iv.i.ii` reads:

> "Accedit **Regula S. Pachomii**, quæ a S. Hieronymo in Latinum sermonem conversa est"

It is the **Rule of Pachomius, in Jerome's Latin translation** — not the Rule of Benedict. The document's own ellipsis ("*Accedit* **Regula** *S.* …") elides exactly the word that disproves the claim.

This matters slightly beyond pedantry, and in the direction that makes the correction *more* useful, as N1's did: a Pachomian *regula* witness is not Registry-row-36 (Named Comparandum, Benedict) territory at all — it is Egyptian-monastic, i.e. the `desert-monasticism` neighbour whose relation to this world's vocabulary is the whole subject of the S1/N4 Origin-tag test. Calling it "RB" mis-files it under an Excluded row and loses the only *regula* witness in the volume that is neither Benedictine nor editorial-cross-reference-to-Benedict.

It is also, exactly, the error class this pass exists to eliminate: Round 2's own factual assertion adopted into the document without opening the file. The pass re-verified Round 2's N1 lemma claims (correctly — I confirmed all eleven) but not its N3 second-witness claim.

**Fix:** correct 3.6's clause to name Pachomius and drop the "RB" attribution; carry the same correction into 7.2's heading per R1.

### R3 (MINOR — stale §11 bookkeeping, contradicting the header). Two document-level log lines were not updated for Round 2.

§11's closing lines still read:

- "**Disagreement log:** none (one review round; no second review exists to disagree with the first)." — Two review rounds now exist, and the same §11 records Round 2 overturning Round 1 on three assertions (the exact-form lemma search, the *professio* locus, the *regula* locus) plus the 5.3/5.6 `[AS]` retention. The line is false on its own document's face.
- "**Disposition:** REVISED (**Round 1 revision**, 2026-09-09) — pending Round 2 review. … a fresh review round is required before disposition."

The Disposition line **directly contradicts the header status block** (L5), which reads "REVISED (**Round 2 revision**, 2026-09-09) … Awaiting a further bounded check or self-disposition." A reader landing on §11 is told a Round 2 review is still pending.

**Fix:** two lines.

### R4 (COSMETIC). Four N1 corrections name the layer but not a locus, against the document's own "exact locus" claim.

§0 Discipline 2 says the eleven lemmas were "each now corrected to its **exact locus** in its own entry," and §10 item 1 repeats "each now corrected in its own heading with the exact locus." Seven headings do give a `<div>` id or chapter (1.1, 1.5, 1.10, 1.11, 3.2, 3.6, 5.7). Four give only the layer:

| Entry | Heading says | Actual locus (located this pass) |
|---|---|---|
| 3.1 *magister* | "in Roberts's and Gibson's footnotes" | `ii.vi.ii.xli`, `ii.vi.ii.xlviii`, `iv.i.ii` |
| 6.3 *benedictio* | "Gibson's footnote" | `iv.iii.ii.vii` = *Inst.* II.7 (a section §11 declares unread) |
| 7.6 *tentatio* | "the editorial apparatus" | `iv.iii.iii.x` = *Inst.* III.10 (likewise unread) |
| 7.11 *communio* | "the editorial apparatus" | `iii.xxxvi` = Heurtley's Appendix II |

No false claim — all four witnesses are real, and Round 2's own N1 table supplied no locus for these four either, so the pass could not have copied one. Only the "exact locus" boast overstates. The loci above are supplied so a fix pass can close it in four edits.

### R5 (COSMETIC). 3.1's *magister* witnesses are all in senses unrelated to the entry.

The count and layer are right (4 occurrences, all editorial). But every one is a different word-sense from 3.1's spiritual master/teacher: "*magistro officiorum*" and "*magistris officialibus*: Halm reads '*magistri*'" are Roberts's endnotes on the imperial **master of offices** (`ii.vi.ii.xli`, `ii.vi.ii.xlviii`), and "*magistro* Johane Nide" is a personal title in a manuscript colophon in Gibson's Prolegomena (`iv.i.ii`). None is 3.1's sense.

The heading removes the false negative, which was the point of N1 — but it leaves a reader to infer that the lemma is attested *for this term*, which is the same shape as the *collatio* trap that 3.5 is (rightly) commended for disclosing in both directions. A one-clause sense-caveat would close it. (Related and trivial: 3.5's "'Cassian, *Collat.* xvii.18' (×2)" is one occurrence in Heurtley's Introduction, not two — inherited from Round 2's table; the total of five inflected hits is nonetheless correct, since `Collationes` is the form that occurs twice.)

---

## Checks that passed, recorded so a fix pass need not redo them

1. All thirteen assigned fix items (N1–N12, residual C7) are physically present in the live file, verified in the file rather than from the log.
2. The independent `[AS]` Tags-line count reproduces the document's claim exactly: 5 entries, 7.2/7.4/7.5/7.13/8.8, with matching Appendix rows and a 5/76 = 81 Origin split.
3. Entry↔Appendix agreement is exact across all 81 rows on Origin, Risk/Function and Tier; the Salvian marking is exactly congruent between entries and Appendix on all 8 rows that carry it.
4. All arithmetic recomputed: 81 entries, 81 Appendix rows, section counts, 16 Tier-1, 16/81 ≈ 20%, single-voice 14/4/3/2.
5. Structural integrity: every entry carries all seven required fields; no broken `N.N` cross-reference; no malformed table; no numbering or ordering error; nothing outside the declared footprint disturbed.
6. Every one of the eleven N1 lemma corrections was checked against the vendored XML and is factually sound — this pass did **not** repeat the Round 1 revision's mistake of adopting a reviewer's search result unverified. The single exception is the *regula* second-witness claim at R2, which came from Round 2's N3 rather than its N1 table.
7. The N4 self-caught bracketed-token error is genuinely fixed at both 5.3 and 5.6, not merely claimed fixed.

## Disposition

**Not yet Approved to Proceed — bounded to three one-line edits (R1, R2, R3), with two optional cosmetics (R4, R5).**

None of the three touches the Origin tags, the voice classification, the §9.1 routing, or the Tier flags — i.e. nothing Doc_04 or Doc_06 consumes changes. R1 and R2 are confined to two headings (3.6, 7.2) and R3 to two §11 lines. **After those edits the document should self-dispose to Approved to Proceed; a fourth review round would not be a good use of the build's attention.**

**Disagreement log (Round 3 vs. Round 2):** one. Round 2's N3 stated that a second *regula* witness exists in the Prolegomena and that "both are RB." **I disagree:** the Prolegomena witness is "*Accedit Regula S. Pachomii, quæ a S. Hieronymo in Latinum sermonem conversa est*" — the Rule of Pachomius, not Benedict (R2). On everything else in Round 2's finding list, and on every Round 2 fix I re-tested, I agree with Round 2 and confirm the fix landed.
