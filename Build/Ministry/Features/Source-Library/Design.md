# The Source Library — design of record

**Status:** Approved to proceed (Mark, 2026-10-14, seven decisions converged one at a
time in the design thread). Implementation is the first job after the pilot launches,
starting with desert. Docs only until then; no code, records or model calls were part of
this design.

**Decision record:** `Build/Ministry/Technology/CiC_FrontEnd_Decision_Log.md`,
entry of 2026-10-14. Research behind it: `Research.md` in this folder.

---

## 1. What this is for

Every source a participant sees becomes a link into the passage itself: our own
verified copy first, the place we downloaded it from beside it. Nothing in the passage
is generated, so it is faithful by construction.

Mark's framing (14 October): CiC's aim is better conversations about faith among real
people in their churches, and also a robust source useful well beyond a first visit.
Scholars study one of these worlds for years. The depth is in the primary texts, of
which our records are only a thin slice. Linking every answer to its passages turns a
conversation into a doorway into the texts, and lets outside scholarly reviewers check
us directly.

## 2. The seven decisions

| # | Question | Decision (Mark, 2026-10-14) |
|---|---|---|
| 1 | What the Library is and how far it reaches | A **reading room for our worlds**: every vendored text readable whole on our site, the citation as the door in. Built on the field's **record shape from day one** (work, edition, passage address in the edition's own labels, quotation anchor). Delivered first as a **footnote service** for desert. |
| 2 | Where a citation's link lands | **Our reader first**, the host edition second (CCEL section page, archive.org item, Scaife or the Patristic Text Archive where a text also lives there). The **scanned page embedded** beside our text for archive.org texts comes in Stage 2. |
| 3 | CCEL's terms while we wait for an answer | **Passage now, volumes later.** Show the cited passage in its section, credited to CCEL as the source of the file, with the link. At the opening of Stage 1, Mark reads CCEL's copyright page live and sends the letter. Whole volumes from CCEL files open only with permission. Independent archive.org scans are the fallback if CCEL declines. |
| 4 | Where the passage address lives | **Derive at build, write back, gate.** The verbatim gate computes the anchor; a mechanical pass writes it into each citation's `address` field world by world; a gate re-derives on every build and fails on drift. Loci stay free text. New loci carry no file line numbers. Work identifiers come in Stage 2. |
| 5 | Where the reader lives | **The public site**, under its own directory, opened inside the conversation app's existing side panel. |
| 6 | When the section cannot be pinpointed | **Work-level link, labelled "section not pinpointed"**, with the locus shown as "look for" text and a per-world coverage report. Never a guessed section. |
| 7 | Front door or links only | **Links only in Stage 1.** Every passage page carries one line saying what the Library is and that a shelf is coming. The browsable shelf is its own decision when Stage 2 opens and the CCEL answer is in. |

Agreed earlier by Mark and carried here: English first for the pilot; source language and
participant language kept as separate dimensions so no door closes on many languages and
many worlds; nothing hard-codes "English" or the number of worlds.

### The heart of it

The one guarantee this whole effort exists to give, "the words you just heard are these
words, here," is only true on a page we serve. The texts are the proof that nothing is
generated, made visible and made shareable. They are the part of CiC that could outlast
any conversation. Where a file was downloaded from another project's site, that project is
credited on every page that shows its text, and permission is asked before whole volumes
are republished.

## 3. What exists today

Measured on 2026-10-14 by a read-only survey of `records/` and `cic/texts/`.

| Fact | Count | What it means |
|---|---|---|
| Vendored texts in `cic/texts/` | 479 | 435 plain text (mostly archive.org OCR), 38 CCEL ThML XML. 674 MB. |
| Files with a non-English `Language:` header | 285 | Latin 174, French 57, German 20, Greek 19, Czech 5, others. |
| Quote records, fleet-wide | 374 | 366 are `verified-direct`: the gate found the exact wording in the file. |
| Citation entries (`sources[]`) on all records | 4,216 | 382 on quotes. The rest cite stories, terms, figures, witnesses, limits. |
| Loci carrying file line numbers in prose | 359 | Brittle across re-vendoring. |
| Loci still showing apparatus after `display_locus` | 160 | Across 114 records in 9 worlds. Logged as a known gap (see §10). |
| Loci carrying a CCEL section id | 123 | Mostly gallic. Positional ids, useful as a local key and for the CCEL link. |
| Citations using the structured `address` field | 5 | All desert, all Evagrius. Three different meanings of the suffix exist in the repo today. |
| Source records naming their vendored file in `edition` | 342 | The file is already known at the record layer. |

Two facts carry the design. The CCEL XML files carry stable ids on every section and
paragraph (`id="v.ii.iii-p1"`), and the edition's own labels sit beside them
(`type="Book" n="I"`). And the verbatim gate in `engine/m1/quote_verbatim.py` locates
every verified quote inside its file on every build and keeps only a pass or fail. The
position is computed and thrown away. Keeping it is the hinge.

## 4. The citation record

The field's answer, consistent across the Perseus URN scheme, the Distributed Text
Services standard (1.0, February 2026), the TEI header, Sefaria and the Bible APIs, is a
record with four separable parts. CiC adopts that shape.

1. **Work.** The abstract text, independent of any edition. Identifier from a free
   authority file where one exists: Clavis Clavium numbers (CPG, CPL) for the Greek and
   Latin fathers, Syriaca work URIs for Syriac, OSIS book codes for scripture. Carried on
   the source record (`work_id` / `external_ids`). **Stage 2.**
2. **Edition.** The vendored file. Its filename is already unique, immutable after
   registration, and carries the language infix. A superseding file is a new edition id,
   never an overwrite.
3. **Passage address.** Where in the edition, in the edition's own labels.
4. **Quotation anchor.** The exact words, with a short run of text before and after
   them, the W3C `TextQuoteSelector` shape Hypothesis uses in production. Lets the
   passage be re-found and lets drift be detected.

Everything the app renders is a view computed from that record: the CCEL deep link, a
Text Fragment URL, a Scaife or PTA link, an archive.org page link, the cite-this box.

## 5. The anchor grammar

One grammar replaces the three meanings the `cic:` address has today (a chapter number
in five desert records, a ThML div id in the corpus map, a line number in the corpus
index).

```
cic:<file>#<section-path>[/p<n>]

cic:npnf204_athanasius-select-works-letters.xml#vita-antonii.3/p1
cic:anan-isho_paradise-v2-sayings_budge1907.txt#s12/p3
```

- `file` is the vendored filename.
- `section-path` uses the edition's own labels, walked from the file's own structure:
  for ThML, the `@type` and `@n` attributes (Book I, Chapter 3, §46), normalised to a
  dotted path; for a plain-text file, a section ordinal from a one-time segmentation of
  that file by its own headings, stored beside the file as a small index and never
  written into the file.
- `p<n>` is the paragraph ordinal within the section.
- The positional ThML `id` is kept as the snapshot-local resolver and as the generator
  of the CCEL link (`ccel.org/ccel/<author>/<book>.<divid>.html#<divid>-p<n>`, a
  pattern confirmed from live pages but not from CCEL documentation; one browser check
  settles it).
- Line numbers never appear in an anchor.

**Why anchors survive re-vendoring.** Vendored files are never edited after
registration, only superseded under a new name. When a file is superseded, the source
record's `edition` changes, the next rebuild re-verifies every quote against it, and the
anchors are recomputed and written back. Nobody retypes anything.

## 6. Derivation, write-back and the gate

```
records/<world>/quote/        1. Record: quote text and free-text locus, as today
engine/m1/quote_verbatim.py   2. Verify: the gate finds the exact match in the file
      (new, same module)      3. Anchor: keep the match position; translate it to the
                                 enclosing section path and paragraph ordinal; store the
                                 quotation anchor (exact, prefix, suffix)
      (new, mechanical pass)  4. Write back: fill sources[].address on the record,
                                 world by world, after the derivation has been read
                                 against a few dozen real quotes
engine/m1/gates.py            5. Gate: re-derive on every build; fail if the stored
                                 address no longer resolves to the same section and the
                                 same words (the drift check no standard provides)
engine/m4/citation_cards.py   6. Package: ship the anchor on the citation card
cic-website/ (new section)    7. Reader: open the section, highlight the passage
```

Steps 1 and 2 exist and do not change. The existing `address` schema field and its
format gate (`gate_canonical_address`) are reused; the gate's meaning tightens from
"well-formed and file exists" to "resolves to the same passage".

**What changes in how loci are recorded.** Nothing mandatory. Loci stay human-readable
free text, the place a reader looks up in any edition. Going forward, no file line
numbers in a locus (a gate warns); the verification note belongs in the record body,
which is the audit trail and never ships. The `address` field becomes derived and
checked, with a hand-written value only as an override where derivation fails (a quote
verified in a translator's footnote, a non-quote citation the parser cannot place).

**Coverage, honestly.**

| Citation kind | Entries | Anchor the build can derive |
|---|---|---|
| Verified quotes | 366 | Exact passage, every time, from the verifier's match. |
| Quotes verified via authority or not rechecked | 8 | Work level. The reader opens the work and shows the locus as the place to look. |
| Non-quote citations | 3,834 | Section level where the locus names a division the parser can match to the file's own labels. Otherwise work level, labelled "section not pinpointed". Never a guess. |

A per-world coverage report turns the unresolved loci into a visible queue for
overrides rather than a silent gap.

## 7. The reader

Lives on the public site under its own directory, opened from the app in the existing
Level 3 side panel. One page serves study groups, scholars, reviewers and search
engines, with no session.

**What the passage page holds.**

- The section, whole, with the cited passage highlighted and the page scrolled to it;
  the rest of the work one click away, section by section.
- The edition's own notes as footnotes (the ThML files keep them as `<note>` elements;
  a quote verified in a note opens on the note).
- The record's modern rendering, labelled as ours, beside the original wording when a
  Representative quoted the passage. A rendering is a separate version of the passage,
  its own class, with its author and date.
- **The seven items the specialist corpora agree on**, written at the B2 bar: the print
  citation beside the permalink; who made the digital text and how ("CCEL's proofed
  markup", "archive.org scan text"); a status word ("checked against the file on
  <date>", "uncorrected scan text"); the licence; the identifier with version and date;
  a cite-this box; a way to report an error.
- **Plain labels no surveyed project yet uses:** "an 1892 translation"; "Latin; the
  English beside it is our rendering"; "abridged recension", where the file's content
  note says so.
- "This edition at its source": the host link.
- One line saying what the Library is and that a shelf is coming (Stage 1 orientation).
- Stage 2, archive.org texts: the scanned page itself, through the Internet Archive's
  IIIF image service, with the quotation's leaf highlighted.

The reading-level bar applies to everything we write on the page. It does not apply to
the source text, which is shown as the edition printed it.

## 8. Non-English and OCR texts

- **Two language dimensions, kept apart.** Source language from the file header's ISO
  639-3 code, on the passage. Participant language a property of the interface and of
  any translation layer, never of the file.
- **Non-English passage.** Original shown as the primary text, labelled by language and
  edition. The record's English rendering beside it, labelled as ours. A vendored
  public-domain translation of the same work offered as a second column where it exists.
- **OCR state.** The file's provenance note already says whether it is raw OCR and what
  was normalised. The reader shows a short caveat drawn from it and never alters the text.
  Stage 2 can surface the Internet Archive's own per-page confidence where a text was
  rebuilt from its hOCR.
- **Later translations** are a layer keyed by anchor: one translation of one passage into
  one language, with its own author and rights. Never an edit to a vendored file.
- **Pointer-only sources** (Documenta Catholica Omnia, New Advent, in-copyright
  translations) get a card that says so and a host link where one exists. No reader page.

## 9. Rights

- Public-domain translations and editions: shown with the file's own rights line.
- CCEL files: decision 3 above. Passage with credit now; volumes after permission;
  archive.org scans as fallback. CCEL's copyright page is read live by Mark at the opening
  of Stage 1, before any CCEL-derived passage is displayed, because the project's wording
  of it is second-hand.
- Open-licence files (one CC BY, several CC BY-SA TEI editions): attribution shown on
  every page; any corrected text CiC publishes from a ShareAlike source carries the same
  licence.
- Internet Archive page images are embedded through its IIIF service, not copied; a
  descriptive User-Agent and back-off on 429 for any server-side fetch, per its bots page.

## 10. Hosting, pipeline and risks

**Hosting.** Rendered section files and one small index per text go to Cloudflare R2,
served by the existing Worker pattern used for packages and audio, read by a static
reader page on the public site. Raw texts are 674 MB; rendered output perhaps double;
R2's free tier holds 10 GB. Nothing is added to the Render image. Cloudflare Pages was
set aside: its 20,000-file cap is close to the section count of the 38 ThML volumes alone.

**Build pipeline.** A Library build in `cic/engine/` beside the corpus tools (segment,
emit sections and index, upload with size and hash verification); anchor derivation and
write-back in `engine/m1/`; the gate in `engine/m1/gates.py`; the card field in
`engine/m4/`; the reader page in `cic-website/`; a one-line change to the card component.

**Risks to live and canonical surfaces.**

- `cic/texts/` is never edited. Segmentation indexes live beside the files or in build
  output.
- `records/` changes are the mechanical write-back of a derived field, gated, plus hand
  overrides. The leaking-loci cleanup is a separate PR owned by the worlds.
- The package gains additive fields. Old packages still restore.
- A new public directory on the site requires the root README map and
  `CiC_Repo_Structure_Tracking.md` to change first, by the standing rule.
- The CCEL section-URL pattern and the archive.org Terms of Use must each be read once
  in a browser; the sandbox blocks both hosts.

**Known gap, logged, not fixed here.** 160 citation entries across 114 records in 9
worlds still show machine apparatus (file names, "line N", CCEL volume tags, build-doc
references) to participants after `display_locus`. Logged in
`Build/Ministry/Operations/Standing/CiC_Cross_System_Analysis_Tracking.md`, 2026-10-14,
with the record ids per world. Each world's own thread resolves its share.

## 11. The phased plan

| Stage | Work | Stopping point |
|---|---|---|
| **Before pilot launch** | Design only (this document). A read-only dry run of anchor derivation on desert reports coverage; no model calls, no writes. No action for Mark. | Nothing participant-facing changes. The pilot ships as it is. |
| **Stage 1** (first job after launch) | Opening step, Mark's own: read CCEL's copyright page live and send the letter asking permission to republish the volumes. Passage display with credit does not wait on the answer. Then: anchor derivation for verified quotes, shipped in the package; derivation read against real desert quotes, then written back with the gate. Library build for the texts desert cites; upload to R2. Reader v1: section, highlight, notes, provenance panel, the seven items, host link, language and OCR labels, orientation line. Card gains "Read the passage" and "This edition at its source". Work-level fallback with "section not pinpointed". Per-world coverage report. | Mark reads three desert conversations with live links. External reviewers of the desert pilot can follow every quote. |
| **Stage 2** (fleet) | Every vendored text, including non-English with rendering beside original. Section-level resolution for non-quote citations. Archive.org texts rebuilt from hOCR and page-number files so each quotation carries a leaf index; the page image embedded through IIIF. Work identifiers from Clavis Clavium, Syriaca and OSIS on source records. CCEL volumes opened if permission is in hand, else the scan fallback begins. Leaking-loci cleanup as its own PR. The shelf decision. | Every card in every built world links somewhere real. Coverage report per world. |
| **Stage 3** (later, by need) | Translation layer keyed by anchor for participant languages. The browsable shelf, if decided. Open publication of citation records; a Distributed Text Services endpoint so other projects can cite us. Recension comparison where two witnesses of one work are vendored. | Each item is its own decision when the need is real. |

## 12. Not verified in this design

- The exact URL pattern of CCEL section pages (ids are in our files; the live site is
  blocked from the sandbox).
- CCEL's copyright page wording, held only from search extracts.
- The Internet Archive Terms of Use page (its developer and bots pages were read).
- The rendered size of the Library on R2 (the "roughly double" figure is a plan, not a
  measurement).
- Whether the Patristic Text Archive serves a DTS endpoint today.
