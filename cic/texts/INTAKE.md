# Intake — turning a raw file into a vendored, registered, findable text

**Hand-written, not generated.** Unlike `README.md`/`AUTHORS.md`/`STRUCTURE.md`
in this same directory, nothing regenerates this file — it's the procedure,
not a report on the corpus.

**Trigger — two real paths, both fine (2026-09-03).** Mark finds a source
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
this corpus so far is an English translation of an ancient work. Starting
2026-09-02, Mark is also sourcing **original-language texts** (Greek, Latin,
Syriac, ...) as second witnesses — never primary evidence for a
Representative (this project's evidence language is English), but legitimate,
rights-clean material for when two English translations disagree, or when no
English translation exists at all yet. Everything below applies to both;
where they differ, both paths are stated.

---

## 1. Read what was actually received

Extract the text, and pull whatever the source itself states: title, author,
translator/editor, publisher, year, and — critically — **where Mark got it
and what that host itself says about rights.** A chat attachment usually has
this in Mark's own message alongside it; a file pulled from `_intake/`
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
- A transcriber's explicit PD declaration (Pearse's site-wide notice is the
  precedent) → accepted, recorded as such.
- An explicit open licence (CC BY 4.0 — Dysinger's Evagrius is the one case
  so far) → `open-licence`, with the attribution string recorded and carried
  into every quote that draws on it.
- 1931–1963 US publications need an actual renewal check (Stanford Copyright
  Renewal Database / NYPL `cce-renewals`), not a guess — flag for that
  research rather than assuming clear.
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

**Original-language files carry the second-witness caveat into this step
too.** Its `note` field should say plainly that this is a witness for
cross-checking an English rendering, not itself citable as a Representative's
evidence — the same caveat that will need to travel again into any world's
own `source` record that eventually cites it (its `USE DISCIPLINE` prose).

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

Derived, gitignored, ~10 seconds for the whole corpus as of 2026-09-02 (64
files). Skipping this just means the new file is invisible to
`corpus_index.py`'s search until someone rebuilds it — not a correctness
risk, just a wasted trip for whoever searches next.

## 9. Report back

State plainly: what was vendored, its rights basis, which Atlas entries it
was assigned to and why (flag `confidence: needs-ruling` rather than guess a
world it doesn't clearly belong to), and — for an original-language file —
restate the second-witness caveat explicitly, so it's never later cited as
if it were English evidence.

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
