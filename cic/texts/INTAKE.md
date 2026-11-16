# Intake — turning a raw file into a vendored, registered, findable text

**Hand-written, not generated.** Unlike `README.md`/`AUTHORS.md`/`STRUCTURE.md`
in this same directory, nothing regenerates this file — it's the procedure,
not a report on the corpus.

**Trigger — two real paths, both fine.** Mark finds a source
and downloads it to his own machine; from there:
- **Attach it in a live chat message** — one or a few files, no separate
  upload step. Good for a single find mid-conversation.
- **Push it to `cic/texts/_intake/` on GitHub** — better for a batch (a
  whole folder of finds at once), or anything found outside a live
  session. A session picks up whatever's waiting there. See
  `cic/texts/_intake/README.md` for that folder's own discipline: nothing
  in it is vendored yet, and it empties out as each file is processed.

This document is what happens next either way, in whichever session picks
the file up — from a raw attachment or `_intake/` file to a vendored file
every future session can search and cite.

**Two shapes of source, same pipeline, different rights checklist.** Most of
this corpus is an English translation of an ancient work. Mark also sources
**original-language texts** (Greek, Latin, Syriac, ...) directly. Everything below applies to both; where they differ,
both paths are stated.

**A clean public-domain original can be primary evidence.** Language is not what decides whether a source is primary —
credibility and truth are. If a work is a primary source to the world it
belongs to, that holds regardless of what language it survives in. In
practice:

- A quote record holds the original-language text, verified against the
  vendored file, the same verification discipline every English quote
  already gets.
- The modern English a Representative speaks, or a card prints, is our own
  rendering of that original, marked in the record as rendered from the
  original rather than quoted from an existing English edition. A second
  rendering, made independently by an agent that never sees the first,
  checks it. Any difference in meaning is marked uncertain, and both
  readings are kept. The model that renders is the one `CLAUDE.md` names
  for renderings, unless Mark has made an exception for the work in hand.
  An older stage of a language counts as foreign here: Old and Middle
  English (`ang`, `enm`), Middle High German (`gmh`) and the like. A
  quotation from an English text printed before 1931 is given in our modern
  English too, with the second rendering; the printed wording stays on
  record with its file and lines.
- A public-domain English translation, where one exists, is a cross-check
  against our rendering — useful, not required. Its absence is not a
  reason to treat the original as unusable.
- **Scan quality decides quotability, not language.** A garbled OCR
  scan — long ſ, þ, ð and similar systematic encoding failures aside,
  which the quote gate normalizes deterministically — stays second witness
  until a clean witness of the same work is vendored. See `REGISTRY.yaml`
  for `apparatus` mappings recording a specific edition's own OCR
  substitution pattern (e.g. Arnold's and Matthew's Wyclif editions
  rendering þ as `])`/`]?`), each one verified against page images before
  it's trusted. No model ever retypes a source to work around a bad scan.


---

## 1. Read what was actually received

Extract the text, and pull whatever the source itself states: title, author,
translator/editor, publisher, year, and — critically — **where Mark got it
and what that host itself says about rights.** A chat attachment usually has
this in Mark's message alongside it; a file pulled from `_intake/`
should have it in a sidecar note per that folder's own convention. If
neither states the URL and the host's own rights statement, ask before doing
anything else. A rights basis is never guessed; it either comes from the
file's own front matter, from the host page Mark names, or from the
project's own PD-by-date rule applied to a stated publication date. See
`cic/engine/texts_registry.py`'s own module docstring for the full
verified-not-asserted case this whole registry rests on.

## 2. Settle the rights basis

**English translations** — the established two-route rule, restated in
`texts_registry.py`'s own docstring:
- Published > 95 years ago (rolling; 1930 as of 2026) → public domain by
  date.
- Where a title page prints no year, a copyright notice in the volume dated
  1930 or earlier stands for the date; a dated preface stands for it only
  where the library catalogue's date agrees. The header's Rights line says
  which date was used and where it stands in the file.
- A transcriber's explicit PD declaration (Pearse's site-wide notice is the
  precedent) → accepted, recorded as such.
- An explicit open licence (CC BY 4.0 — Dysinger's Evagrius is the one case
  so far) → `open-licence`, with the attribution string recorded and carried
  into every quote that draws on it.
- The date is the imprint on the title page, not the host's record, and the
  line moves each January.
- An institution's report (an annual statement, a proceedings) counts by a
  date printed in its own text, where that date is read on the page image.
  The header's Rights line says where the date stands.
- A scan that carries a microfilm maker's notice against reproduction is not
  taken, whatever the date of the print. Another scan of the same print with
  no such notice may be.
- A host's own additions (page-foot stamps, watermark text, host banners) may
  be removed at intake; nothing of the printed work is. The header's
  Provenance note gives the exact text removed, the number of lines, the host
  URL and the original byte count, so the original can be fetched again and
  checked against the file.
- 1931–1963 US publications whose copyright was not renewed → free, for any
  such book. The renewal search (Stanford Copyright Renewal Database / NYPL
  `cce-renewals`, or the catalogue transcriptions) is run, never guessed, and
  recorded in the file header: what was searched, the names searched, the
  date, the result. A renewal found means in copyright, not held.
- An owner's own statement that the text is free (CC BY 4.0, "not
  copyrighted", "may be reproduced without permission") → `owner-declared
  free`, a class beside public domain, with the owner's own words copied into
  the file header. Entries the owner marks as reprinted "with permission" are
  skipped. Where the statement says the text must stay unchanged, the text is
  quoted word for word only and gets no modern rendering.
- A "non-commercial use only" permission → not held. Cite and link, and write
  for permission where the text matters.
- Foreign-published 1931+ translations: assume URAA-restored (in copyright in
  the US) unless a licence says otherwise — see
  `world-build-docs/_cross-world/PLAN-texts-store-scaling.md`'s sibling
  planning doc and the source-infrastructure blueprint's §3.2 for the full
  decision tree.

**Original-language texts** — a different reservoir, so a different check.
Real hosts this project's own research has already verified, in descending
order of how often they'll actually come up:
- **First1KGreek / Patristic Text Archive** — CC BY / CC BY-SA. Vendorable;
  record the licence and attribution string exactly as `open-licence` sources
  already do.
- **Perseus/Scaife, TCP (EEBO/ECCO/Evans)** — CC BY-SA or released free of
  restriction; same treatment.
- **MDZ (Munich), e-rara.ch** — public domain as prints, but check that
  specific library's own reuse statement before vendoring a scan; record
  which statement was checked.
- **Documenta Catholica Omnia** — **POINTER ONLY, NEVER VENDOR.** The site
  itself asserts copyright on its "electronic edition." If this is Mark's
  source, cite it bibliographically in the eventual source record; do not
  save its text into `cic/texts/`.
- **Vatican texts** — the Latin of the *Acta* printed by 1930 is held under
  the date rule and rendered by us. Everything later is cite and link only.
- **Court and government records** — a printed record counts by its imprint
  date, like a book. Unprinted archive records are cite only. US federal
  government works are free.
- **Church statements with no stated terms** (confessions, conference
  resolutions, bishops' documents) — cite and link, and write to the body for
  permission.
- **Old works whose only scan is locked** (lending-only) — record as "located,
  not obtainable here"; do not take them.
- **Martin Luther King Jr.** — cite and link only. No quotation, no rendering.
- **A work we do not hold** is never quoted. A profile gives facts and a
  citation.
- **Our own rendering from an old original** — a second independent
  rendering checks the first, whether or not an old English translation
  exists, and differences in meaning are marked uncertain on the card.
- Anything else: treat like an English translation from an unfamiliar host —
  find the host's own explicit rights statement before proceeding, never
  infer one from silence.

## 3. Name the file

Existing convention (`cic/texts/README.md`'s own header, `corpus_map.py`'s
docstring): `<series><vol>_<slug>.<ext>` for a series volume (NPNF/ANF-style),
`<author>_<work-slug>_<translator><year>.<ext>` for a standalone English
translation. No world prefix — files serve every world that cites them, not
one.

**Original-language extension:** no translator exists, so the suffix names
the language and the edition instead —
`<author>_<work-slug>-<lang>_<editor><year>.<ext>`, where `<lang>` is an ISO
639-3 code (`grc` Ancient Greek, `lat` Latin, `syr` Classical Syriac, ...) —
a real, checkable code, the same "no invented labels" discipline
`rights_basis` and `AUTHOR-IDS.yaml`'s own identifiers already follow.
Example: `evagrius_praktikos-grc_muyldermans1932.txt`.

## 4. Write the intake header

Every vendored file opens with the same block, prepended if the source
didn't carry one of its own (real example: `basil_ascetic-works-longer-
shorter-rules_clarke1925.txt`'s own header):

```
Title: <the work's own title>
Creator: <author (translator/editor credited here, not as a separate line)>
Publisher: <publisher, place, series if any>
Publication Date: <year>
Rights: <the declared basis - see §2; "Public Domain" or the open-licence name>
Language: <ISO 639-3 code - ONLY if not English; omit the line entirely for
  an English translation, since absence already means English (texts_
  registry.py's own language_declared() default)>
Source: <exactly where this came from and how, incl. who supplied it and when>
Provenance note: <how this header was assembled, what was mechanically
  stripped (OCR artifacts, apparatus), and the rights basis restated in one
  sentence a reader could check independently>
Content note: <only if the file is a partial extract, a multi-work
  compilation, or otherwise needs a caveat a later session would want up front>
```

Never touch a file's wording while writing this header — mechanical
extraction only (OCR/DOCX-conversion artifacts stripped, apparatus markers
noted, nothing paraphrased or "cleaned up" beyond that). Real precedent
throughout this directory: every existing intake header states exactly what
was normalized and why.

## 5. Register it

Add an entry to `cic/texts/REGISTRY.yaml` (`filename`, `supplied_by`,
`date_added`, optional `notes`) and run the full sweep:

```
python cic/engine/texts_registry.py            # confirms rights clears, no orphans
python cic/engine/texts_registry.py --write-readme   # regenerates README.md
```

A non-English file shows up automatically in `report()`'s own "non-English
source(s)" flag and `README.md`'s `lang` column — nothing extra to remember
there.

## 6. Assign it — check every world it could serve, not just the one asked for

Corpus-map assignment is **non-exclusive by design**: a source found for one
world's request often belongs in others too (Athanasius' Vita Antonii is the
standing example — Alexandria's own author, desert's evidential base).
Before writing a `_staging/` entry, check `cic/engine/corpus_map.py
--coverage` and skim `cic-website/data/world-census.json` for every Atlas
entry this work could plausibly serve, not only the world Mark was thinking
of when he found it. Write one `cic/corpus-map/_staging/<volume>.yaml` file
per source volume (the writer's-view shape that file's own header
documents), then:

```
python cic/engine/corpus_map_merge.py --check    # validate staging, write nothing
python cic/engine/corpus_map_merge.py            # merge into the real buckets
```

**Original-language files get the same assignment treatment as an English
translation — primary where the work itself is primary to the world.** Its
`note` field should say what kind of witness this is: a primary
original-language voice, ready to quote once verified against the scan; or
a second witness for cross-checking an English rendering because the scan
itself is too garbled to quote from directly yet (§2's scan-quality rule).
Whichever it is, state it plainly — this is what any world's own `source`
record that eventually cites it (its `USE DISCIPLINE` prose) will need to
carry forward.

## 7. If it's a new Expression of a known Work, say so in WORKS.yaml

Only when it actually joins something already there or worth tracking as a
Work/Expression pair — `cic/corpus-map/WORKS.yaml` is seeded, not
comprehensive; don't force an entry a real need hasn't asked for yet. When it
does apply, an original-language file is exactly the `recension`/`language`
distinction that schema already carries (see `palladius-lausiac-history`'s
own two-expression entry for the shape: same Work, two independent
Expressions, one Greek-based, one Syriac).

## 8. Make it findable now, not next session

```
python cic/engine/corpus_index.py --build
```

Derived, gitignored, about 10 seconds for the whole corpus. Skipping this just means the new file is invisible to
`corpus_index.py`'s search until someone rebuilds it — not a correctness
risk, just a wasted trip for whoever searches next.

## 9. Report back

State plainly: what was vendored, its rights basis, which Atlas entries it
was assigned to and why (flag `confidence: needs-ruling` rather than guess a
world it doesn't clearly belong to), and — for an original-language file —
state which it is: primary evidence, ready to quote once verified against
the scan, or second witness because the scan itself isn't clean enough to
quote from yet (§2's scan-quality rule) — never leave that ambiguous.

---

## What this replaces, and what it doesn't

This is the mechanical half of intake — file, header, registry, assignment,
index. It does not decide what a world's own `source` record says about a
text, doesn't write that record, and doesn't decide tier, quote-worthiness,
or interpretive weight — those stay a build thread's own judgment, per
`corpus_map.py`'s own standing rule (assignment ≠ interpretation). See
`cic/corpus-map/README.md` for the map's own discipline and
`Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_3.md`'s
"Cross-world source layer" section for how a world's own Doc_02/G1 work
draws on everything this produces.
