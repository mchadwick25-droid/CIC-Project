Simulated review — informational only, not an Article 31 substitute.

# The 258 to 391 silence claim: independent verification of the project lead's ruling as applied in commit 3c23d0fba (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-verifier subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** the lpc build-thread worker, commit 3c23d0fba "lpc: apply the silence-claim ruling" (trailer "Claude Sonnet 5.5")
- **Round:** 36 (verification of a directed correction, applying the project lead's 2026-09-30 ruling on OG-27; not a new revision round)
- **Truncation check, method 1:** hash and tail comparison. For all 15 files changed in 3c23d0fba, `git hash-object <path>` equals `git rev-parse 3c23d0fba:<path>` (15 files, 0 mismatches). The later commit 6bdc2ad6f touches none of the 15. Each file's last 50 bytes end on a complete sentence, a table row, or the `if __name__ == "__main__":` block.
- **Truncation check, method 2:** structural parse. `wb_lpc_s21.py`, `wb_lpc_s25.py` and `wb_lpc_s28.py` compile. The force, limit and world core records parse as YAML front matter (15, 13 and 16 keys) and each has a body after the closing `---`. Doc_02 has its ten `## ` headings, ending at `## 10. Disposition`. Doc_05, Doc_08 and Doc_09 each end at `## Disposition`. The Registry parses to 272 numbered rows, 1 to 272, with no gap or duplicate.
- **Date:** 2026-09-30
- **Scope:** `git show 3c23d0fba`; the vendored files by structural marker; a sweep of every live copy of the claim; dry runs of s21, s25, s28 and `gen_story_index.py` into the scratchpad.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but does not disqualify, P2 polish.

## Verdict

**Close, but not yet ready.** The ruling is applied faithfully to rows 231 and 232, in every place the last review named. Every date, line and quotation in Doc_02 §7 checks out at source. Nothing the correction states is refuted, so there is no P0. The claims register passes, and the generators reproduce every edited field.

Three things remain:

- The edge of the gap is still incomplete. Pontius's *Life* and the *Acta Cypriani* belong to the same tail as the two acts. Neither is named. The last review raised this as P1-1, and it was not carried through.
- Doc_05 §7 still has an interval column that reads **None** for sources.
- The limit record calls 256 "the last dated act of this world's first phase".

All three are mechanical once the lead confirms the first.

## Findings

### P0

None.

### P1

**P1-1. The tail of Cyprian's phase names two texts; the Registry holds four.** Doc_02 §7 (line 120) says the acts of rows 231 and 232 "are the last voice of Cyprian's own community". It then says that "From them to Augustine's ordination in 391, no source in the Registry supplies" such a voice. Two more Native texts sit at the same edge, and neither is named:

- ***The Life of Cyprian by Pontius*** (rows 7, 40, 194 and 205). Row 7 is drawn on, and `lpcstory006` is built from it. The vendored Harnack file (row 205) dates it:
  - Lines 380–381: "das Jahr 259 als Jahr der Abfassung … (dies ist auch die herrschende Ansicht)".
  - Lines 4360–4362 call the two passiones "mit der „Vita Pontii" gleichzeitigen" (contemporaneous with the *Life*).
  - Line 2356 says Pontius wrote "bald nach dem Martyrium Cyprians".
  - The live figure record `lpc.figure.pontius` (lines 30–31) itself says: "After his bishop's execution in 258, he wrote The Life and Passion of Cyprian."
- ***The Acta Cypriani*** (row 41; row 194; row 231, no. 13; row 232, no. XI). The Knopf file dates the first hearing by consuls of 257: "Imperatore Valeriano quartum et Gallieno tertium consulibus" (line 4822, under `13. Akten Cyprians.` at 4820). It dates the second hearing "idibus Septembris Tusco et Basso", which is 258 (line 4857). It records the brethren's own words: "turba fratrum dicebat: Et nos cum ipso decollemur" (line 4913). That is a congregation's voice. Harnack (lines 376–379) says Pontius cannot yet have had the Acta "in der Zusammenstellung, in der wir sie lesen". On his reading, the compiled Acta come after the *Life*.

**Why this is P1, not P0.** Nothing the correction states is refuted. Harnack makes the *Life* contemporaneous with the acts, not later, so "from them to 391" still holds. But "the last voice" asserts an order that no vendored file fixes. The claim is rated Documented, so its edge has to be complete.

**The fix, mechanical under the ruling's own logic:**
- Name the *Life* and the *Acta* with rows 231 and 232 as the tail of Cyprian's phase.
- Replace "the last voice" with wording that does not assert an order, such as "the closing voices of Cyprian's own community".

**Where it applies:**
- Doc_02 line 120; Doc_05 line 27; Doc_08 lines 23 and 264; Doc_09 lines 23 and 120; `lpc_Gapped_Formation_Precedent.md` line 21.
- The force record's `divergence_note`, `description` and `manifestations`.
- The limit record's `why_sources_cannot_answer`.
- World core caution 2 and the thin-topics note.
- The generators: s21 (around lines 4392 and 4508), s25 (around lines 1578 and 1591) and s28 (around line 883).

**P1-2. Doc_05 §7 still carries the oldest form of the claim.** Line 287 is the Temporal Configuration table's "Sources in this world's record" row. Its interval column reads **None**. Line 281 calls the span "an unattested interval". Both are false against the Registry:

- rows 27, 64 and 264 (Optatus, Native);
- rows 231 and 232;
- row 7 (see P1-1);
- the licensed exceptions in rows 26, 11, 22, 25, 44 and 88.

They are also false against Doc_05's own §0.3, which names these rows. Doc_01 §5 itself says the interval "is not undocumented history in general". This copy was missed by the correction and by the last review's sweep. A fix could read "none that continues Cyprian's voice (§0.3)" and "an interval silent in this world's own voice".

**P1-3. The limit record's source locus is false.** `lpc.limit.the-silent-century.md` line 18 reads: `locus: 256, the last dated act of this world's first phase`. Its generator carries the same text (`wb_lpc_s28.py` line 866). The *Acta Cypriani* are Native first-phase texts with consular dates of 257 and 258 (P1-1). The Registry's own row 4 title says the vendored heading dates the Seventh Council "a.d. 258". Under the ruling, the acts of rows 231 and 232 now also belong to the first phase. A fix could read "256, the Seventh Council; the first phase closes with Cyprian's martyrdom in 258 and the acts written just after it".

### P2

- **Build vocabulary in the force record's spoken text.** The `description` passes on plainness: 38 sentences, a mean of 12.6 words, a longest of 24. It passes on voice: "we/our" throughout, and no "this world". But it still uses build vocabulary:
  - "phase" (five times);
  - "the only force of ours" and "not itself counted as a force";
  - "Donatism's own territory" (OG-25 flagged this phrase in a spoken field);
  - "confirmed by a positive check, not inferred from silence";
  - "Nothing else found so far does".

  The record's `register` is `etic`, while the text is now first-person. That mismatch should be settled one way or the other.
- **Documented rating.** It remains the right level for a claim about the record. It is fully earned once P1-1 names the whole edge.
- **A dehyphenated quotation in backticks.** Doc_02 quotes `episcopus noster solus passus fuisset` as one string. The file breaks it across the two lines as "epi-" / "scopus", and its OCR reads "adhue" for "adhuc". Say that the line break is joined.
- **"Cyprian's own community" and no. 15.** The *Passio* of Marianus and Jacobus is set in Numidia: "pergebamus in Numidiam" and "Cirtensis coloniae", about lines 5188–5191 of the Knopf file. The phrase is exact for no. 16 ("episcopus noster") and broad for no. 15. It is the ruling's own wording, so it is noted for the lead, not held against the correction.
- **A date source not cited.** "Neither vendored file prints a date for them" is true. I checked Knopf's headings and bibliographic notes for nos. 15 and 16, and Gebhardt's Vorwort and headings for XIII and XIV. But row 205 (Harnack) does place the acts in Valerian's time, contemporaneous with the *Life* of 259 (lines 1901–1902, 4360–4362). Citing it would ground "written in the persecution that followed" in more than the Latin alone.
- **World Profile line 26 says "genuine, undocumented interval".** The same paragraph and Doc_01 §5 say it is not undocumented history. "Undocumented in this world's own voice" would fix it.
- **World core caution 2.** It still forbids filling the silence ("Never fill it … Do not supply one"). It allows what the records document, and every named item checks out:
  - the Manichaean years (row 22's Licensed-For cell);
  - the conversion in 386 and the baptism in 387 (Doc_02 §8's Documented sequence).

  But the list reads as closed. "For example" would stop it from reading as the only exceptions. There may also be a tension with World Profile line 26, "it does not narrate the century between them", for Augustine's own life before ordination. Worth one line of alignment.
- **Undated Native pseudepigrapha.** Row 6 and the *Opera Spuria* in row 194 include homiletic pieces transmitted under Cyprian's name, such as `Incipit epistula Cypriani de aleatoribus` (Hartel file, line 4988). Hartel's praefatio gives them no dates; I searched for "saec. IV", "post Cypriani mortem" and similar. So the Registry cannot place them inside the gap, and the claim holds. A Documented claim could still name them as undated and set aside.
- **Row 37 (CIL VIII, Numidia supplement; Native, vendored)** holds inscriptions from inside the interval. Doc_02's list says "include", so the omission falsifies nothing. It could be named.
- **Rep Phase 5 Round 1, probe 4 (line 33)** says the Council of Cirta is "documented only through the neighboring rival communion's own record". That is false. Row 27, Native, narrates it: `XIV. The acts of the Council of Cirta.` at line 181 of `optatus_against-the-donatists.txt`, and the editor's note at line 565 dates it to 305, not "the 330s". Augustine's *Contra Cresconium* III, row 216, treats it too. This is a completed test record, so fix it at the next Phase 5 round. The probe's pass/fail result does not change, because Optatus is drawn on for no claim.
- **Records that cannot be rebuilt (already known, OG-26).** The generator dry runs match every field this commit edited. But the world core's `horizon`, `formation_logic` and `thinness`, and the force record's `canon_cells` (set later by `wb_lpc_s2y_canon_cells.py`), differ from s21 and s25 output.
- **Outside lpc's documents; flagged, not touched.** `cic-website/tree/latin-pastoral-congregational-christianity.html` says Augustine "preached to the same congregation". Read after the Carthage sentence, that means Cyprian's church, but Augustine preached at Hippo. `world-census.json` has the same wording, as the last review noted. The Library lead from OG-27 is still open: Knopf nos. 19–22 and 29 are African acts from inside the gap with no Registry row, and no. 19 is dated "Tusco et Anulino consulibus" at line 6456.

## What was verified at source (by structural marker)

- **Knopf–Krueger 1929 (row 231)**, `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt`:
  - 5166 `15. Martyrium des Marianus und Jakobus.`
  - 5365 `Cyprianus apparuit`
  - 5629 `16. Martyrium des Montanus und Lucius.`
  - 5632 `Et nobis est apud uos certamen, dilectissimi fratres`
  - 5865 `concordiam, pacem,`
  - 5871 `Haec omnes de carcere simul scripserant`
  - 5918 `quam Cypriano docente didicerant`
  - 6135–6136 `epi-` / `scopus noster solus passus fuisset`
  - 6203 `sacerdotio destinauit`
  - 6248 `17. Martyrium des. Fruktuosus.`

  All are as cited. No year is printed for nos. 15 and 16: the notes after each text are bibliographic only, and the contents list at lines 181–182 gives no dates.
- **Gebhardt 1902 (row 232).** The *Passio SS. Mariani et Iacobi* heading is at line 6920 and the *Passio SS. Montani et Lucii* heading at 7492. Running heads read "XIII. Passio …" and "XIV. Passio …". The Vorwort (lines 259–265) names Franchi de' Cavalieri's recension and gives no date. The agent's claim holds for both files.
- **Optatus.** Line 2 of both TEI headers (rows 264 and 265) reads `Optatus of Milevis (fl. 366-385)`. The row 27 file (line 5) and the Ziwsa scan (line 6) read `c. 366-393 CE`. Doc_02's attribution is now correct.
- **Row 265.** `div n="1"` has the Thamugadi consular formula at lines 129–130. `div n="10"` has `data Non. Februar. Serdica.` at line 1648.
- **Theodosian Code (row 44).** `XVI,  2,  4  (321  lul.  3).` is at line 83906, and Doc_02 now reproduces the doubled spaces byte for byte.
- **Row 26 (`npnf214`).** `xv.iv.ii-p12` has Gratus, 345–348. `xv.iv.ii-p13` has Genethlius, 387 or 390. `xv.iv.iv.iii-p8` names Genethlius again.
- **Row 202 (Bruns).** Lines 7854–7858: `CONCILIUM CARTHAGINENSE PRIMUM` / `TEMPORE JULII L PAPAE ?)` / Gratus.
- **Licensed-For cells.** Row 26: "The institutional skeleton of this world's own conciliar life (Doc_01 §2, on the Apiarius affair)". Row 202: "Latin original standing behind … (row 26)". Row 59: "Licensed for row 26's own Apiarius-affair claim". Doc_02's new glosses match.
- **Rows 11, 22 and 25.** `vii.1.I-p2` reads "a.d. 386". `iv.iv.ii-p3` reads "a.d. 388". `npnf107` `ii-p8` reads "shortly after his conversion (387)".
- **Doc_09's quotation of Doc_02 §7** ("overwhelmingly through sources that are Donatism's own territory (World #4), not this world's.") is verbatim.

## Claims register and generators

- **Claims register.** `python Build/worlds/lpc/scripts/check_claims.py` passes: 142 claims and 142 entries. Rows `db01c6d3`, `cc0fa5c1` and `e27efe3b` match the live Doc_09 text. `6db40b49` (item 1's heading) is unchanged and still true under the ruling.
- **Dry runs.** s21, s25 and s28 were run into a scratchpad mirror (`records/lpc` a fresh directory; the repo checked clean afterwards). Parsed field by field with whitespace normalized, these fields are identical to the committed records:
  - the force record's `description`, `manifestations`, `divergence_note` and `name`;
  - the limit record's `statement`, `why_sources_cannot_answer` and `sources`;
  - the world core's `cautions` and `thin_topics`.

  The committed text differs from the generator output only in YAML line-wrapping. `gen_story_index.py`, run to a scratch base, reproduces `lpc_Story_Index.md` byte for byte, including "1137 words". The old s21 lines ("holds nothing dated inside it"; "only through") are gone.

## Sweep: every live copy of the claim

| Location | Status |
|---|---|
| Doc_02 §7, line 120 | True; the edge needs the *Life* and the *Acta* named (P1-1) |
| Doc_05 line 27 (§0.3) | True; same edge (P1-1) |
| **Doc_05 lines 281, 287 (§7 table, "None"; "unattested interval")** | **False** (P1-2) |
| Doc_05 lines 251, 293 | True |
| Doc_08 lines 23, 264, 279 | True; same edge (P1-1). 279's "overwhelmingly" is restored |
| Doc_08 lines 191, 302, 359 | True |
| Doc_09 lines 23, 120; claims register | True under the ruling; same edge (P1-1) |
| `lpc_Story_Index.md` line 93 | True under the ruling (generated from Doc_09) |
| `lpc_Gapped_Formation_Precedent.md` line 21 | True; same edge (P1-1) |
| World Profile line 26 | True in substance; "undocumented interval" is loose (P2) |
| World Profile lines 184, 238, 366, 424, 428, 650–654, 714, 768 | True under the ruling (428: 133 years, row 27 named) |
| Rep Phase 1 line 82; Phase 2 lines 31, 33, 71; Phase 3 line 55; Phase 4 line 28; Phase 6 line 39 | True under the ruling's convention (258 as the marker); acts not named, which a Representative document need not do |
| **Rep Phase 5 Round 1 line 33** | **False** on "documented only through the rival communion" (P2; test record) |
| Permanent Prompt line 21; Capsule line 79 | True under the ruling: "roughly a hundred and thirty years" matches; "your own congregational voice falls silent" holds with the acts as the tail |
| Doc_07 lines 176, 232, 244; Force Index lines 34, 91 | True |
| Force record (`divergence_note`, `description`, `manifestations`) | True; same edge (P1-1); vocabulary (P2) |
| Limit record `statement`, `why_sources_cannot_answer` | True; same edge (P1-1) |
| **Limit record `sources[0].locus`** | **False** (P1-3) |
| World core `horizon` line 90, `thinness` line 240, caution 2, thin-topics note | True; caution 2 and the note: same edge (P1-1) |
| Force record `lpc.force.augustine-engagement-cyprian-conciliar-acts` line 52 | True |
| `wb_lpc_s21.py`, `wb_lpc_s25.py`, `wb_lpc_s28.py` (edited fields) | Match the records; same edge (P1-1); s28 line 866 **false** (P1-3) |
| `gen_story_index.py` line 509; `wb_lpc_s24.py` line 319; `wb_lpc_s2y_canon_cells.py` | True (no claim of absence) |
| Story and Lexicon chunks | No copy. `lpcstory006` is built from the *Life* (see P1-1) |
| `cic-poc/frontend`, `packages/` | No lpc copy |
| `cic-website` | No copy of the silence claim; "the same congregation" (P2, outside scope) |

## For the project lead

1. **Does the ruling's "tail of Cyprian's phase" also cover Pontius's *Life* and the *Acta Cypriani*?** Harnack (row 205) dates the *Life* to 259 and calls the acts of rows 231 and 232 contemporaneous with it. The compiled *Acta* may be later still. The recommendation is yes: name all four texts as the tail, and drop "the last voice". Once confirmed, this is mechanical and needs no new revision round.
2. **"Cyprian's own community" for the Numidian *Passio* of Marianus and Jacobus.** Keep it as ruled, or say "the African church in Cyprian's communion"?
