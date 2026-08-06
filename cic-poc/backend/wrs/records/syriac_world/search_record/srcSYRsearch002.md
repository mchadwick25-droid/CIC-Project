---
id: srcSYRsearch002
world_id: syriac-edessa-nisibis
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: 'Purposive (Booth''s standard) - the FIELD-BIBLIOGRAPHY SWEEP (2026-08-06), run against
  the Academic Rigor Review''s finding #10 recommendation verbatim: Syriac against Brock''s Syriac Studies:
  A Classified Bibliography and its Parole de l''Orient/Hugoye continuations, via syri.ac (free). This is
  the FIRST session in this world''s history in which that specific instrument was actually opened - srcSYRsearch001
  logged it, and its own pre-freeze re-sweep, as a standing coverage limit, never accessed. Documents this
  sweep only.'
types_sought:
- works held by syri.ac''s hosted Brock bibliography (and syri.ac''s own annotated author/topic pages) touching
  this world''s actual deployed subject matter - Ephrem, Aphrahat, Bardaisan, the Doctrina Addai, the Odes
  of Solomon, the Diatessaron, bnay qyama/ihidaya asceticism, Jacob of Serugh (as Ephrem-memory source only)
- edition/translation detail for rowed works still carrying edition_status none-consulted, specifically
  srcSYR020 (Doctrina Addai) - the one item srcSYRsearch001 named by row number and deferred twice (migration
  sweep, then pre-freeze re-sweep) to "the pre-freeze re-sweep" that never actually ran this instrument
approaches:
  syriac-org-indexed-page-search: 1
  row-cross-check: 1
years_searched:
  from: 1876
  to: 2026
languages_searched:
- en
- fr
inclusion_exclusions: 'Included: syri.ac-hosted or syri.ac-indexed bibliography entries and author pages
  bearing on this world''s Native-boundary subject matter, cross-checked against the existing 64-row registry.
  Excluded: syri.ac material for authors/works outside this world''s window or licensing (Jacob of Serugh''s
  broader ~400-homily corpus - only his single Ephrem memra is licensed here, per srcSYR045 and Doc_04''s
  own exclusion of his wider corpus from C2; the Peshitta as a developed topic - Doc_03 Sec. 3.2 and syrlex006
  explicitly decline to develop it as a lexicon entry, and syrgrav009 records it as a deliberately not-advanced
  gravity, so new Peshitta bibliography is a confirmed-correct absence, not a gap); bnay qyama/ihidaya material
  generally, because that topic was already this world''s single most productive search area at S6.2/SYR
  S2.1a (12 existing rows: 006, 010, 013, 026, 027, 032, 033, 045, 056, 057, 058, 062) and the syri.ac results
  returned for it (Aphrahat, Sahdona, Babai, Joseph Hazzaya, Philoxenus, John of Dalyatha author pages) name
  authors/works outside this world''s 200-410 CE boundary rather than a rowed-work gap.'
terms_tried:
- term: 'syri.ac direct fetch (https://syri.ac, https://syri.ac/bibliography/... )'
  productive: false
- term: 'WebSearch site:syri.ac Ephrem bibliography'
  productive: true
- term: 'WebSearch site:syri.ac bibliography Aphrahat'
  productive: true
- term: 'WebSearch site:syri.ac bibliography "Jacob of Serugh"'
  productive: true
- term: 'WebSearch site:syri.ac bibliography "Doctrina Addai" OR "Teaching of Addai"'
  productive: true
- term: 'WebSearch site:syri.ac bibliography "bnay qyama" OR "ihidaya" OR Syriac asceticism monasticism'
  productive: true
- term: 'WebSearch site:syri.ac bibliography Peshitta'
  productive: true
- term: 'WebSearch Howard 1981 "Teaching of Addai" Scholars Press edition'
  productive: true
- term: 'WebSearch Lollar 2023 Doctrina Addai Teaching of Addai edition translation'
  productive: true
instruments:
- 'syri.ac (https://syri.ac) - the Brock Syriac Studies: A Classified Bibliography (1960-1990) host, with
  Parole de l''Orient/Hugoye continuations, per the review''s finding #10. Direct WebFetch to syri.ac and
  its bibliography/* pages returned HTTP 403 every time (consistent with WebFetch 403ing on every host tried
  this session, including en.wikipedia.org - a general tool-level block, not a syri.ac-specific one). Google-indexed
  syri.ac pages WERE reachable via WebSearch (title+URL+snippet), and this is the instrument actually used:
  individual bibliography-entry pages, author pages, and Brock''s own bibliographical-handout pages (syri.ac/brock/*)
  surfaced by name for every subject-matter query run. This converts syri.ac from "not accessed" to "accessed,
  indirectly, via search-engine index" - a real but partial access mode, weaker than a live query interface,
  logged honestly as such rather than claimed as a full database search.'
- 'L''Annee philologique; Oxford Bibliographies; the Hugoye cumulative index; a systematic GEDSH pass - NOT
  ACCESSED this session either (out of this sweep''s scope, which the review''s finding #10 named as syri.ac
  specifically for this world); these four remain standing coverage limits, unchanged from srcSYRsearch001.'
---
Saturation statement (field-bibliography sweep scope, 2026-08-06): syri.ac was reached, indirectly, through search-engine-indexed pages rather than a live query against the site itself (which 403'd on every direct attempt). Six subject-matter queries against syri.ac's indexed content (Ephrem, Aphrahat, Jacob of Serugh, Doctrina Addai, bnay qyama/ihidaya, Peshitta) each returned real, named bibliography and author pages. Cross-checked against the existing 64-row Syriac registry, none surfaced a work-level gap: the Ephrem results matched the registry's own CSCO/Beck edition pattern; the Aphrahat, Jacob of Serugh, and bnay qyama/ihidaya results named authors and works this world's own boundary or licensing already excludes (Jacob's wider corpus outside C2's evidentiary basis; bnay qyama already this world's most-rowed topic at 12 rows); the Peshitta results confirmed rather than contradicted this world's own deliberate non-development of that topic (syrlex006, syrgrav009). One genuine, specifically-named gap WAS closed: srcSYR020 (Doctrina Addai) carried edition_status none-consulted with no edition/translation fields since 2026-07-06; srcSYRsearch001 named the two missing editions by author and year ("Howard 1981 / Lollar 2023 -> row 20") and deferred them twice without ever running this instrument. Both editions were independently confirmed this session - Howard's Syriac/English Teaching of Addai (Scholars Press, 1981, SBL Texts and Translations 16, reprinting Phillips's 1876 Syriac text) via syriaca.org/bibl/2105.html and Princeton/Penn/Missouri library catalogue records; Lollar's Doctrine of Addai and the Letters of Jesus and Abgar (Cascade Books, Early Christian Apocrypha 10, 2023) via the Wipf and Stock/Cascade catalogue page and its NASSCAL preview PDF - and srcSYR020 was updated accordingly (edition_status: none-consulted -> critical; edition and translation fields added). Neither edition was independently re-read this session; the row's verification_note says so plainly. The four instruments srcSYRsearch001 named beyond syri.ac (BIBP, L'Annee philologique, Oxford Bibliographies, the Hugoye cumulative index, a systematic GEDSH pass) were outside this sweep's scope (the review's finding #10 specified syri.ac for Syriac) and remain standing coverage limits, unchanged.

Provenance: this file is the field-bibliography sweep log, run against the Academic Rigor Review's finding #10 (Ministry/Operations/Audits/CiC_FullSystem_Review_2026-08-05/02_Academic_Rigor_Review.md, ~line 670). srcSYR020's edit is the sweep's one direct, low-risk, fully-cited correction; no new source rows were added, and no other existing row was found to need correction or contradiction on the evidence surfaced this session.
