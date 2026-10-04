# Syriac (Edessa/Nisibis) — Source Request Manifest

**World:** `syr` / `syriac-edessa-nisibis` (identity settled through Step 1; Representative identity remains Mark's step-5a touchpoint)
**Produced at:** per-world build step 2, Source ecology (spec §4.3.2), 2026-08-21
**For:** Mark, in his operational source-acquisition role (Build-Blueprint §7)
**Search basis:** every entry is grounded in a search recorded in `Build/worlds/syr/build/records/search_record/` — including the searches that came back empty. The vendored corpus (`cic/texts/`) already covers the load-bearing base: Mark supplied the Syriac-specific files 2026-08-15..18 (Doctrine of Addai, Chronicle of Edessa, Hallock's Aphrahat, Mitchell's Prose Refutations) alongside the ANF/NPNF volumes. Rights on every SUPPLIED entry were read from each file's own provenance header, never from this request.

---

## 1. Already supplied and verified (no action needed)

| source record | vendored file | note |
|---|---|---|
| `syr.source.ephrem-nisibene-hymns` · `-nativity-hymns` · `-epiphany-hymns` · `-hymns-on-faith-pearl` · `-three-homilies` · `syr.source.aphrahat-select-demonstrations` | `npnf213_…xml` | DC.Rights Public Domain; translator split (Stopford/Morris/Johnston, ed. Gwynn) read from the volume's own preface |
| `syr.source.aphrahat-demonstrations-hallock` | `aphrahat_demonstrations-2-7_hallock1932.txt` | rights rest on the transcriber's declaration (1932 translation) — accepted by Mark 2026-08-18, noted in the record |
| `syr.source.ephrem-prose-refutations` | `ephraim_prose-refutations_mitchell1912-1921.txt` | |
| `syr.source.diatessaron-arabic-harmony` | `anf09_…xml` | Hogg's Arabic-recension rendering; harmony-tradition witness only |
| `syr.source.bardaisan-book-of-laws` · `syr.source.ancient-syriac-documents` | `anf08_…xml` | Named-Comparandum / hagiographic-tier disciplines in the records |
| `syr.source.doctrine-of-addai` | `addai_doctrine-of-addai.txt` | legend-framing license |
| `syr.source.chronicle-of-edessa` | `chronicle-of-edessa_cowper.txt` | |
| `syr.source.eusebius-…` · `theodoret-…` · `sozomen-…` · `socrates-…` · `jerome-de-viris` | `npnf201/202/203_…xml` | Syriac-relevant loci verified by direct grep 2026-08-21 |

## 2. Deferred — future work (not blocking; Mark could not locate as of 2026-08-22)

### 2.1 Odes of Solomon — **CLOSED 2026-09-09, by direct acquisition**
- **Wanted:** J. Rendel Harris, *The Odes and Psalms of Solomon* — the 1909 editio princeps or the 1911 second edition (an archive.org scan of the printed volume preferred, so the file carries its own title page and date).
- **Status (2026-08-22):** Mark could not locate a copy on hand. Logged as future work — pick up whenever a copy surfaces; not required for this world to proceed through step 6/7/8 later, since nothing here is load-bearing on the Odes.
- **Status (2026-09-09): CLOSED, not by Mark.** A build session with unusual live WebSearch/WebFetch access found and vendored the exact named edition directly (Harris, 2nd ed. 1911, Cornell University Library scan, archive.org `cu31924029308677`, "no known copyright restrictions") — see `cic/texts/harris_odes-and-psalms-of-solomon_harris1911.txt`, `cic/texts/REGISTRY.yaml`, and `Build/worlds/syr/build/records/search_record/syr.search.odes-of-solomon-pd.md` (result: found). `syr.source.odes-of-solomon` now stands at rights `public-domain`, not `pending-verification`; verbatim quoting is licensed subject to that record's own OCR-quality caveat (the English translation-with-commentary section needs verse-by-verse reconstruction before any specific wording is certified `verified-direct` at the quote level — real follow-up work, not yet done).

### 2.2 Synodicon Orientale (the 410 Synod acts) — **P3 · DEFERRED, bounded**
- **Wanted:** J.-B. Chabot, *Synodicon Orientale* (Paris, 1902) — public-domain in principle, but **French**; no PD English exists (search: `syr.search.synod-410-acts-english`).
- **Why bounded:** the 410 Synod is this world's closing boundary, and its substance is already carried at reviewed confidence via Doc_01/Doc_02 and the vendored historians. A vendored Chabot would allow direct verification of specific canons if a later step needs them; it would not add licensed-quote material for the English-speaking voice.
- **Status (2026-08-22):** Mark could not locate a copy on hand. Logged as future work — lowest priority of the two; the world's own closing-boundary claims already rest on other reviewed sources and do not depend on this text.

## 3. Named gaps with no acquirable PD remedy (for the record, not requests)

- **Aphrahat complete:** 13 of 23 Demonstrations (including most of the anti-Jewish set) have no PD English — Lehto 2010 / Valavanolickal 2005 are consultation-only (`syr.search.aphrahat-complete-english-pd`).
- **Ephrem's major cycles:** Hymns on Faith complete (Wickes 2015), Hymns on Paradise (Brock 1990), Hymns on Virginity (McVey 1989), Commentary on the Diatessaron (McCarthy 1993) — all in copyright; **Contra Haereses has no complete English translation at all** (`syr.search.ephrem-corpus-gaps`).
- **Persian martyr acts:** no PD English; Sozomen II.9–14 (vendored) is the narrative witness instead (`syr.search.persian-martyr-acts-english`).
- **Liber Graduum:** no PD English, and partly post-410 in final form — named for completeness per Doc_02 §1, not a founding source (`syr.search.liber-graduum-english`).

## 4. Consultation-only secondary anchors (never vendored)

Registered as `source` records with rights `in-copyright (consultation-only)`, carried from the approved Doc_02 §4 expertise-verification pass: Murray 1975 and Griffith (2002; 1991/1993; 1986) — the two Step 0 anchor additions — plus Brock, Drijvers, Possekel, Ramelli (calibrated: one contested position), Petersen, Harvey, Koltun-Fromm, Malki Malki 2024, Segal, Kayaalp 2013, GEDSH, Millar. **De-anchored per Step 0: Adam Schor** (center of gravity is 5th-century Theodoret's Syria, outside this window) — recorded in `syr.search.secondary-anchors-verification`.

## 5. Decisions for Mark

§2.2 remains logged as **future work**, not an open decision — Mark confirmed (2026-08-22) it is not on hand right now, and it does not block this world's progress. §2.1 (Odes of Solomon) is no longer future work: it closed 2026-09-09 by direct acquisition (see §2.1 above), not by Mark supplying a copy. Revisit §2.2 opportunistically; nothing else in this world's record set is blocked on acquisition.
