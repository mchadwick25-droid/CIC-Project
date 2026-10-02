# Adversarial Review — `records/ijc/` verbatim and source fidelity
**Branch:** `world/ijc` · **Reviewed:** 2026-08-21 · **Reviewer:** isolated Opus dispatch · **Method:** every claim re-derived from the vendored files in `/home/user/CIC-Project/cic/texts/`, `<note>` elements stripped before comparison; nothing accepted from memory.

## Summary verdict: SUBSTANTIAL REVISION REQUIRED

Scoped precisely, because the headline is better than the verdict sounds:

**No quote record's `text` field is corrupt.** All 20 verbatim quotes were matched character-by-character against their editions. There is no fabricated wording, no altered word, no silent paraphrase, and — importantly — **no editor-note text anywhere inside a quote's `text` field**, in a corpus where the ThML interleaves notes mid-sentence and several of these quotes are cut apart by note elements (Julius, Leo *Tome*, Leo Sermon 82, Jerome, Sozomen, Socrates, Eusebius *VC*). The note-stripping discipline held on all 20.

The verdict is driven by defects in the *apparatus*: one source record quotes words that are not in the file it names; three records cite the wrong chapter for a load-bearing narrative; the world's central creed quote applies two opposite bracket conventions and misdescribes both; and seven locus line-ranges do not contain the text they cite. In a record set whose entire warrant is the phrase "Text verified verbatim against the vendored file 2026-08-21," those are the errors this review exists to catch, and they should be fixed before finalization.

### Counts actually checked
| Scope | Checked |
|---|---|
| Quote records | 20/20 (all `license: verbatim`), each located and diffed against its vendored file |
| Source records | 19/19; **45** file-line claims verified individually; **10** `DC.Rights` headers read; **9** translator/editor attributions verified against the volumes' own front matter |
| Search records | 16/16, including the two named spot-checks (De obitu Theodosii; Rufinus HE) |
| Non-quote loci carrying line numbers | **21/21** cross-checked (task asked for ≥10) |
| Referential integrity | 125 records; 0 dangling `source_id` / `relation.target` / `found_sources` / figure-id references |
| Referenced-only sources | 2/2 confirmed to license no quotation; all 5 citations of them carry `license: referenced-only`; 0 verbatim licenses outside `quote/` |

---

## HIGH

### H1 — `ijc.source.lactantius-de-mortibus`: quotation attributed to a file that does not contain it

The trailing body states:

> Ch. 48 preserves the actual text of the 313 Milan agreement (**"when I, Constantine Augustus, and I, Licinius Augustus..."**), making this the world's most direct witness to its own legal beginning.

That wording is **not in `anf07`**. Fletcher's ANF translation of *De mortibus* ch. XLVIII (file line 10684) reads:

> "When we, Constantine and Licinius, emperors, had an interview at Milan, and conferred together with respect to the good and security of the commonweal…"

`grep` over the whole of `cic/texts/` finds `"I, Constantine Augustus"` in exactly one place — a **different work in a different volume**: Eusebius, *HE* X.5, McGiffert's translation, `npnf201_eusebius-church-history-life-of-constantine.xml:50280`:

> "4. When I, Constantine Augustus, and I, Licinius Augustus, came under favorable auspices to Milan…"

So the source record puts McGiffert's Eusebius wording inside quotation marks and attributes it to Fletcher's Lactantius. This is the precise failure mode the build's own discipline forbids, and it is doubly awkward because `ijc.source.eusebius-historia-ecclesiastica` separately registers *HE* X.5 at line 50202 — the record set contains both texts and conflated them.

Mitigating: `ijc.quote.milan-edict` itself quotes the **correct** ANF7 wording. The corruption is confined to the source record's prose.

**Fix:** replace the parenthetical with the ANF7 wording, or drop the quotation marks and describe rather than quote. Consider adding a line distinguishing the two surviving transmissions of the Milan document, since the build holds both.

---

## MEDIUM

### M2 — Theodoret's penance scene cited as **V.18** in three records; it is **V.17** in the vendored edition

`ijc.source.theodoret-he` verifies the chapter correctly and then contradicts itself four lines later. Propagates to `ijc.source.ambrose-epistles` and `ijc.search.npnf210-ambrose`. `ijc.story.emperor-penance` hedges correctly (V.17-18). **Fix:** change all three bare citations to V.17.

### M3 — `ijc.quote.nicene-creed`: bracket convention applied two different ways inside one record, misdescribed in the note

"[from heaven]" dropped entirely, "[we believe]" kept with brackets stripped, parenthetical Latin/Greek "(consubstantialem)" dropped — all under one note claiming a single consistent "omitted" convention.

### M4 — `ijc.quote.chalcedon-definition`: opposite convention to M3, under an identically-worded declaration; names a bracket outside the quoted span

### M5 — `ijc.search.ammianus-english`: `result: found` with `found_sources: []` and no source record — inconsistent with the identically-situated Paulinus search's resolution

### M6 — `ijc.quote.lactantius-dream`: note falsely claims the transcription "carries" a Latin X; the file has Greek Χ (chi), substitution undisclosed as such

---

## LOW

- **L7** — Seven locus line-ranges too narrow for their quotes (nicene-creed, vc-conquer-by-this, canon28-equal-privileges, constantine-bishop-outside, augustine-vigil-hymns, julius-custom, leo-tome-each-form)
- **L8** — Undisclosed terminal-punctuation substitution (milan-edict, chalcedon-definition) vs. disclosed elsewhere (julius-custom)
- **L9** — canon28-equal-privileges note transliterates a Greek gloss into Latin letters
- **L10** — milan-edict attributes a jointly-issued document to Constantine alone (disclosed in body, so a judgment call not a concealment)

---

## Verified clean — worth recording

All 20 quote texts exact matches modulo the enumerated items. Note-stripping held in every hard case (Julius, Leo Tome, Jerome, Sozomen, Socrates all interrupted by footnotes mid-sentence, correctly rejoined). Marked ellipsis in augustine-vigil-hymns is honest. Both named search spot-checks (De obitu Theodosii absent from npnf210; Rufinus continuation absent from npnf203) confirmed genuinely absent. All 10 DC.Rights headers read Public Domain; all 9 translator attributions verified at the exact lines claimed. Boundary discipline held — no license:verbatim outside quote/, both referenced-only sources license nothing quotable.

## Recommended fix set (12 records)
HIGH: lactantius-de-mortibus (false quote). MEDIUM: theodoret-he/ambrose-epistles/npnf210-ambrose (V.17 not V.18); nicene-creed/chalcedon-definition (bracket convention); ammianus-english (found/[] mismatch); lactantius-dream (chi rationale). LOW: 7 locus widenings; 2 punctuation disclosures; 1 transliteration fix.
