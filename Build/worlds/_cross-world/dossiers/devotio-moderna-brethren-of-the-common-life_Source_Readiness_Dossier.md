# Source Readiness Dossier — Devotio Moderna / Brethren of the Common Life

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.3
**Corpus-map slug:** `devotio-moderna-brethren-of-the-common-life`
**Time window:** c. 1380–1517
**Region(s):** Low Countries
**Dossier author / date:** source-research thread, 2026-09-25
**Corpus-map / `cic/texts/` state as of:** 2026-09-25 — the three §3 leads
below have been vendored, headered, registered, and assigned this same
pass. See §1 below for current state.

## 1. Already assigned

**A fresh candidate, no longer cold-start as of this pass.** Three works
vendored and assigned to `cic/corpus-map/devotio-moderna-brethren-of-the-common-life.yaml`:

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Imitation of Christ | kempis | tradition | assigned | ~446K chars (unextracted word count) | `kempis_imitation-of-christ_benham1886.txt` |
| The Founders of the New Devotion (Lives of Gerard Groote and Florentius Radewin) | kempis | tradition | assigned | ~567K chars (unextracted word count) | `kempis_founders-of-the-new-devotion_arthur1905.txt` |
| Gerardi Magni Epistolae XIV (Groote's own letters, Latin) | groote | tradition | assigned | ~262K chars (unextracted word count) | `groote_epistolae-xiv-lat_acquoy1857.txt` |

A real three-pillar base, the same shape this project's other multi-source
worlds already take: Thomas a Kempis's own devotional writing (the
Imitation), Kempis's own telling of the movement's founding story (the
Lives), and the founder Gerard Groote's own surviving voice (the Letters,
Latin original, no PD English translation found - see §4). Together these
give both directions this movement is known for: the interior devotional
practice it's famous for (the Imitation) and its own account of where that
practice came from (the Lives, the Letters).

## 2. Cross-link opportunities

None found or expected — every other vendored corpus text is either
patristic-era (pre-451 CE) or from other Era 6/7 candidates researched this
same batch (Lollardy, Hussites) with no figure or text overlap.

## 3. Verified acquisition leads

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Imitation of Christ: Four Books | Thomas a Kempis | William Benham | 1886 | archive.org `imitationofchris00benhrich` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch, 2026-09-25, metadata and body text checked |
| The Founders of the New Devotion (Lives of Gerard Groote, Florentius Radewin and their followers) | Thomas a Kempis | J. P. Arthur | 1905 | archive.org `foundersofnewdev00thom` | pd-us-by-date | direct fetch, 2026-09-25, metadata and body text checked |
| Gerardi Magni Epistolae XIV | Gerard Groote | ed. J. G. R. Acquoy | 1857 | archive.org `gerardimagniepi00acqugoog` | pd-us-by-date, `NOT_IN_COPYRIGHT` confirmed | direct fetch, 2026-09-25, metadata checked and the opening of Epistola I read directly to confirm genuine legible Latin text, not a garbled scan |

**Scale (rough):** three solid volumes, over a million characters combined
(unextracted word count) — comparable to a mid-size patristic corpus, with
real range across genres: devotional treatise, hagiographic/biographical
narrative, and personal correspondence.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Early printed English translations of the Imitation of Christ (1580, 1582, 1602, 1609, 1636 editions, all on archive.org's Early English Books collections) | Older, potentially more period-flavored English renderings than Benham's 1886 translation | Not pursued once Benham's clean, confirmed-legible 1886 edition was in hand — archaic black-letter OCR quality on these earlier printings would need individual verification and offers no clear advantage over an already-solid PD translation. Not closed as unavailable, just not needed; a future pass could still check them if a period-English register is wanted for this specific text. |
| English translation of Gerard Groote's letters | Would give the founder's own voice without the Latin barrier | Searched directly (title-based archive.org query); no results. Not conclusively exhausted - a name-variant search (Geert Groote, Gerardus Magnus) or a check of Hyma's scholarship for embedded translated excerpts could still turn something up, but nothing surfaced this pass. |

## 5. Open cross-world questions

**Vs. the Anabaptist Movements (VI.3) and the Society of Jesus (VI.11),
both vendored earlier this same batch:** the census's own `relationsSummary`
for this world names it a "parent-influence on both Luther's schooling and
Jesuit pedagogy - a rare both-directions ancestor." Neither of those two
worlds' corpus-map entries currently cross-reference this one, and no
shared vendored text exists to link them directly (this is an influence
relationship, not a text-sharing one) - worth naming explicitly in whichever
Doc_02 runs for any of the three, but not something a corpus-map row can
represent on its own.

## 6. Step 0 scope notes (for whoever drafts Doc_01/the Step 0 confirmation)

**Doctrinal floor:** not assessed in depth this pass. Nothing in the
material fetched raised a visible complication - the Imitation is
squarely orthodox devotional literature - but a real Step 0 pass should
still check directly rather than assume.

**Scale and shape honestly stated:** unlike Lollardy (one prolific author)
or the Hussites (one central figure), this candidate already has a
genuine three-voice structure spanning devotional, biographical, and
epistolary genres. The real open question flagged in the census's own
`legacy` field - "the houses themselves did not survive the century they
helped bring about; most dissolved during the Reformation" - is an
institutional-decline note, not a sourcing gap; nothing in the vendored
corpus currently documents that decline directly, which is worth noting
for whoever builds this world's Doc_02, not a defect in what's vendored
here.
