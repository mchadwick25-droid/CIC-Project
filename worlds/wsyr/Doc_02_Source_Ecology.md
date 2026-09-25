# World (proposed code `wsyr`): Syriac Orthodox (West Syriac) Christianity — Source Ecology

**Status:** DRAFT, Revision 1. Follows Doc_01 (this session, not yet
independently reviewed). Not yet independently reviewed itself.

---

## 0. Purpose and Scope

This document performs Step 2 (Source Ecology) per
`reference/method/CiC_Record_Native_World_Build_Process_V1.8.md` §2: an
exact locus for every quotable passage this session actually checked; a
quotability flag for every vendored file; own-voice/opponent-voice flags
wherever one work mixes them; corpus-map rows with corrected role and
confidence; a holdings disposition for every item; a thin-evidence map;
editions/languages, with primary vs. cross-check marked; and cross-world
overlaps. Seven primary-source files were newly vendored this session
(§1); all corpus-map assignment and REGISTRY.yaml work referenced below was
done directly against the actual files, not from summary (see
`cic/corpus-map/_staging/*.yaml` and `cic/texts/REGISTRY.yaml` for the full
provenance record each vendored file carries).

## 1. Source Ecology Overview

This world's evidentiary base has an unusual shape for this project: one
insider historian (John of Ephesus) supplies genuinely rich, personally-
witnessed narrative material across two separate works; one theologian-
patriarch (Severus of Antioch) supplies real administrative correspondence
in his own hand (via early translation); and the movement's single most
consequential institutional actor (Jacob Baradaeus) is known to us
**only** through John of Ephesus's own portrait of him — he left no
surviving writing of his own. This is the opposite asymmetry from `syr`,
where the world's own foremost voices (Ephrem, Aphrahat) are extremely
well-attested in their own written corpus but institutional actors are
comparatively thin. Six sources are newly vendored and directly
spot-verified this session; four sources already sat in this world's own
corpus-map bucket before this session began (inherited, not created by
this build) — see §2 Table B for what those four are and their own
pre-existing dispositions, which this document reviews but does not
silently alter.

## 2. Source Registry

### Table A — Newly vendored this session, directly spot-verified

| Work | Author | Date/context | Extent vendored | Vendored file | Own-voice / opponent-voice | Quotability | Confidence |
|---|---|---|---|---|---|---|---|
| *Lives of the Eastern Saints* | John of Ephesus (c. 507-588) | c. 566-568 | 58 chapters (Syriac + English, PO 17-19) | `john-of-ephesus_lives-of-the-eastern-saints_brooks1923.txt` | Own-voice throughout (miaphysite insider, personal acquaintance of many subjects) | **Verify locus-by-locus** — mixed Syriac-script/English OCR; ch. 49 confirmed clean and quotable (see §2 note below); rest of file not yet individually checked | Documented (ch. 49 content); file-wide quotability Inferential-Thin pending further locus checks |
| *Ecclesiastical History*, Part III | John of Ephesus | events to c. 585 | Book III (and index fragments of IV-VI) | `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` | Own-voice | **Verbatim-ready** for Book III.36-38 (directly verified clean English, lines 11905-12080); rest of Book III not yet individually checked | Documented (III.36-38); Widely Accepted for the rest, pending individual verification |
| *The Sixth Book of the Select Letters* | Severus of Antioch (c. 459-538) | letters written 512-538 | 123 letters (Parts I-II, complete English translation) | `severus-of-antioch_select-letters-book6-part1_brooks1903.txt`, `...part2_brooks1904.txt` | Own-voice (Severus's own Greek, via early Syriac translation — see Doc_01 §4) | Second witness only, pending individual locus checks — sampled for authenticity (clearly genuine patriarchal correspondence, not yet checked letter-by-letter) | Documented that the work is genuine; Inferential-Thin per-letter until checked |
| *The Discourses of Philoxenus* | Philoxenus of Mabbug (c. 440-523) | ascetic homilies, undated within his episcopate (485-519) | 13 discourses (Vol. II translation) | `philoxenus-of-mabbug_discourses_budge1894.txt` | Own-voice | Second witness only — not yet individually locus-checked this session | Documented that the work is genuine and correctly attributed; Inferential-Thin per-passage |
| *The Chronicle of Joshua the Stylite* | Traditional attribution, uncertain (see Doc_01 §5) | composed 507, covers 494/5-506 | Whole work | `joshua-the-stylite_chronicle_wright1882.txt` | **Undetermined** — see Doc_01 §5, corpus-map staging note; not established as this world's own voice or as context | Verbatim-ready in the clean English narrative body; footnote apparatus (Syriac/Arabic transliteration) is not quotable | Widely Accepted for the events narrated; role classification Contested/open |
| *The Syriac Chronicle known as that of Zachariah of Mitylene* | Composite: Zacharias Scholasticus (Chalcedonian) + anonymous continuator, c. 569 | events to c. 569 | Whole compilation | `zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` | **Mixed, book-by-book** — see Doc_01 §5 and corpus-map `authors_ruled` entry; not yet resolved book-by-book this session | Second witness only, pending the book-by-book pass | Widely Accepted that the compilation is genuine and roughly as described; own-voice/opponent-voice per book Inferential-Thin |

**Locus verification actually performed this session** (the specific loci a
future quote record can cite as already checked, not merely claimed):

- `john-of-ephesus_lives-of-the-eastern-saints_brooks1923.txt`, line 26185
  onward: ch. 49, "The Forty-Ninth History, of the Blessed James the Bishop
  and Brave and Valiant Combatant" — the Jacob Baradaeus portrait. Confirms
  his origin at Thella, training at the monastery of "Psiltha"/"Fsiltha,"
  c. 15 years at Constantinople under Theodora's protection, joint
  consecration with a second bishop (Theodore, for the Ghassanid capital),
  and — at line 26301, in a footnote — the direct etymological source of
  his nickname ("Burd'ava"/"Burd'ana," "the man of the patchwork garment"),
  from a cloak he cut in two for clothing and covering. See
  `cic/corpus-map/_staging/john-of-ephesus_lives-of-the-eastern-saints_brooks1923.yaml`
  for the full verification note.
- `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`, lines
  11905-12080: Book III.36-38, the Asia Minor pagan mission (Tralles, the
  Derira temple-to-monastery conversion, 24 new churches, imperial funding,
  the jurisdiction dispute with the bishop of Tralles). The Preface (lines
  210-224) separately states the mission's "seventy thousand" baptism
  figure; this build did **not** locate that exact number restated within
  III.36-38 itself — flagged as editorially-attested, not yet pinned to
  John's own sentence (see REGISTRY.yaml entry and Open_Gaps_Tracking.md).

**Corpus-map cross-check performed:** `python cic/engine/corpus_map_merge.py --check`
passes clean; `python cic/engine/corpus_index.py --build` indexes all seven
new files (227 files, 68,842 passage units fleet-wide after this session's
additions). `python cic/engine/texts_registry.py` confirms all seven as
Public Domain with no orphan/rights-basis problems.

### Table B — Already in this world's corpus-map bucket before this session (inherited, reviewed not recreated)

| Work | Author | Role | Confidence | Source file | This document's own review |
|---|---|---|---|---|---|
| The Arabic Gospel of the Infancy of the Saviour | arabic-gospel-of-the-infancy | transmission | assigned | `anf08_...` | Unreviewed this session; existing note is self-explanatory (custody, not composition) and not revisited |
| The Chronicle of Edessa | chronicle-of-edessa | context | provisional | `chronicle-of-edessa_cowper.txt` | Reviewed. Placement question inherited unresolved from `NEEDS-RULING.md` (a Chalcedonian composition-era chronicle documenting this world's ground "from the rival side of 451") — **not decided by this document**, carried to `Open_Gaps_Tracking.md` |
| A Canticle of Mar Jacob the Teacher on Edessa | jacob-of-sarug | tradition | assigned | `anf08_...` | Unreviewed this session; note explicitly "non-exclusive on purpose," not revisited |
| The Divine Liturgy of James | liturgy-of-st-james | tradition | provisional | `anf07_...` | Reviewed; see Doc_01 §4 — text postdates its own apostolic attribution and predates this world's window by composition; provisional status affirmed, not overturned |

## 3. Author Gravity Assessment (Constitution Article 16; preliminary — full classification is Doc_04's own job)

**Severus of Antioch.** Representativeness: high for elite theological
argument and patriarchal administration; low for lay or ordinary clerical
experience. Authenticity: high (genuine early translation of a real
working patriarch's correspondence, per Brooks's own scholarly edition).
Boundary status: squarely native — the movement's own foremost self-
articulated voice. Institutional position: the highest office this world's
own hierarchy held before it was driven underground. Continuity: his
doctrinal self-definition is the thread Doc_01 §6 finds continuous into
Jacob Baradaeus's own later institutional-survival phase.

**John of Ephesus.** Representativeness: unusually high for lived,
personally-witnessed community experience across the movement's whole
social range (ascetics, bishops, laypeople he baptized); genuinely rare for
this period. Authenticity: high. Boundary status: native, and also, per
Doc_01 §3 and §7, a figure whose own career complicates any simple
"persecuted-church-outside-the-system" framing — worth Doc_04's direct
attention as a potential gravity-defining tension (a persecuted bishop who
was also an instrument of the same empire's own coercive missionary
policy), not smoothed into a single clean role.

**Jacob Baradaeus.** No surviving writing of his own — known entirely
through John of Ephesus's portrait (and secondary/later tradition, e.g.
Michael the Syrian, not vendored). Representativeness/Authenticity
questions therefore properly attach to John's own reliability as a witness
(addressed above), not to Jacob as an independent source. Institutional
position: the central figure of this world's own second, itinerant phase
(Doc_01 §6) — a Doc_09/figure-record subject, not a Doc_02 "author."

**Philoxenus of Mabbug.** Representativeness: a second major theological
voice, useful as a cross-check against treating Severus as this world's
only doctrinal register — but the vendored *Discourses* are ascetic-
spiritual, not Christological-polemical (Doc_01 §5); his fit for this
world's own doctrinal center of gravity specifically is not yet
demonstrated by the source actually in hand. Authenticity: high
(established critical edition). Boundary status: boundary-adjacent by
birth date, native by career (Doc_01 §2).

## 4. Secondary Scholarship Assessment

Three secondary/reference works are named in the census's own pre-existing
source list; none is vendored (all are in-copyright, in-print modern
scholarship — correctly not vendored under this project's own PD-only
intake rule):

- **Volker L. Menze, *Justinian and the Making of the Syrian Orthodox
  Church*** (Oxford Early Christian Studies, 2008). The standard modern
  monograph specifically on how this world's own separated hierarchy
  actually formed (518-553) — the single most directly on-topic secondary
  work named for this world. Not independently verified this session
  (no access to the text); its center-of-gravity fit (a specialist in
  exactly this world's own formation, not an adjacent topic) is stated by
  the census and not independently re-checked here — flagged, not
  asserted as verified.
- **W. H. C. Frend, *The Rise of the Monophysite Movement*** (1972). Broad
  standard narrative connecting the Syrian and Egyptian anti-Chalcedonian
  movements; dated (over 50 years old) but still commonly cited as the
  foundational English-language survey. Same not-independently-verified
  caveat applies.
- ***Cambridge History of Christianity*, vol. 2, ch. 3** (F. W. Norris,
  "Greek Christianities"). Reference anchor, not a monograph on this world
  specifically.

A fourth work is directly relevant but was not in the census's own list,
found instead during this session's own acquisition research: **Greatrex,
Phenix & Horn, *The Chronicle of Pseudo-Zachariah Rhetor*** (Translated
Texts for Historians 55, Liverpool University Press, 2011) — the modern
critical edition and the source of the authorship analysis this document's
own `pseudo-zachariah-rhetor` corpus-map ruling relies on (§2 Table A). Not
vendored (in copyright); its own scholarly apparatus was not directly
consulted this session — the authorship analysis is accepted on the
strength of its being the modern standard treatment named in the corpus-map
ruling's own evidence, not independently re-derived here.

None of these four works is vendored. All four are named in
`Open_Gaps_Tracking.md` as real acquisition targets for Mark, not silently
treated as consulted.

## 5. Formation Narrative Sources

Genuinely thin, on the evidence actually in hand this session. No
foundation-legend or origin-narrative text comparable to `syr`'s own
Doctrina Addai was located for this world specifically — this world's own
"formation narrative," such as it is, is Chalcedon itself (Doc_01 §7), an
external ecclesiastical-political event rather than an internal foundation
story. This is named as a real content gap, not filled by invention.

## 6. Material Culture and Daily Life Sources

Thin. The census's own `experienceToday` field names Mor Gabriel Monastery
(Tur Abdin, founded 397, still functioning) as a living continuity point,
but 397 predates this world's own 451 opening by over half a century — its
relevance is to this tradition's own longer continuity, not to lived
material practice *within* 451-636 specifically. No archaeological or
material-culture source specific to this world's own window was
independently located or verified this session — a real gap, not filled.

## 7. Source Asymmetry and Missing Voices

Per Article 20's own naming discipline, stated directly rather than merely
gestured at: every source in Table A is an elite, literate, male, urban (or
monastic) voice. No source vendored this session directly attests an
ordinary lay believer's own words, a village congregation's own experience,
or a woman's own first-person voice — Theodora and the Ghassanid royal
women appear only as reported patrons in others' narration (John of
Ephesus's own narration, specifically), never as directly attested
speakers in their own right in anything vendored this session. This
mirrors, and does not improve on, the asymmetry Doc_01 §1 already names.
This is disclosed as a limitation this world's own later steps must
reckon with (per this world's own `thinness_statement`,
`records/worlds/wsyr.yaml`), not resolved here.

## 8. Boundary Cases — Narrative Summary

See Doc_01 §5 for the full argument. In summary: Philoxenus of Mabbug
(born before 451, career entirely inside the window — treated as native,
not excluded); the Chronicle of Joshua the Stylite (in-window and
in-territory, but confessional allegiance undetermined — role left open);
the Zachariah Rhetor compilation (mixed authorship requiring book-by-book,
not whole-work, own-voice/opponent-voice tagging — not yet done). None of
these is a Bardaisan-style Section-A floor question (Doc_01 already cleared
the floor cleanly at the movement level, Step 0 §1); all three are
source-attribution and role-classification questions specific to Doc_02's
own job.

## 9. Forces Lens Applied to Source Ecology (Forces Framework Step 2)

Doc_01 §7's preliminary forces identification frames what this session's
own source-gathering actually found: real, direct textual evidence for the
doctrinal force (Severus's own letters), for the institutional-survival
force (John of Ephesus's direct portrait of Jacob Baradaeus), and for the
political-patronage force (the Ghassanid/Theodora material within that same
portrait). Thinner: direct textual evidence of the *missionary* force
Doc_01 §7 also names (John's Asia Minor mission is well-attested, per §2,
but its relationship to this world's own internal formation — rather than
to the empire's own separate missionary ambitions — is a live
characterization question, not a sourcing gap).

## 10. Confidence Map

This world's own core historical facts — Chalcedon's 451 date and content,
Severus's patriarchate and exile, Jacob Baradaeus's consecration and
itinerant ordination program, John of Ephesus's authorship of both vendored
works, the Yarmouk 636 date — are **Documented**. The precise mechanics and
dating of Ghassanid patronage (Doc_01 §2 flag) and the "seventy thousand"
baptism figure's exact locus (§2 above) are **Widely Accepted** as
editorially/traditionally reported but not yet independently pinned by
this build to a single verified primary-text sentence. This tradition's own
self-designation (Doc_01 §1, Step 0 §1) is **Inferential-Thin** — not yet
located in any vendored source. The Chronicle of Edessa's and the Chronicle
of Joshua the Stylite's own role classifications are **Contested**, in the
project's own internal sense (an open methodological/attribution
disagreement this build has not resolved), not in the sense of disputed
historical fact. The Zachariah Rhetor compilation's own book-by-book
own-voice/opponent-voice split is **Inferential-Thin** pending the pass
Doc_01 §5 calls for.

## 11. Resolution of Doc_01's Carried-Forward Items

Of Doc_01 §10's eight open items, this document makes partial progress on
four and leaves four genuinely open, named plainly rather than forced:

- **Item 1 (self-designation):** still open. Not located in any source
  checked this session.
- **Item 2 (strand-singular test against Jacob's own ordination theory):**
  still open — Jacob left no writing of his own to test against (§3
  above), so this question may need to be answered from Severus's own
  writing on ordination theory (not yet checked) or from later tradition,
  not from a source Jacob himself authored. Named as a real methodological
  constraint on how this question can ever be resolved, not only as
  unresolved.
- **Item 3 (Chronicle of Edessa placement):** not decided, per this
  document's own §2 Table B and Doc_01 §5 — carried to
  `Open_Gaps_Tracking.md` unchanged.
- **Item 4 (Joshua Stylite's role):** not decided — genuinely open, named
  in the Source Registry (§2) rather than forced to a default.
- **Item 5 (Zachariah Rhetor book-by-book tagging):** not done this
  session — the compilation's whole-work `provisional` status (§2)
  reflects this, rather than a book-by-book table this document does not
  yet have the grounds to produce responsibly.
- **Item 6 (Ghassanid/Theodora chronology):** partially developed — line
  26025's footnote (in the vendored Lives file) states "Theodora lived 12
  years after [Jacob's consecration]," consistent with her 548 death date;
  not independently cross-checked against a second source this session.
- **Item 7 (absent Phase Two portfolio survey):** unchanged, named for the
  project lead, not something Doc_02 can resolve.
- **Item 8 (Severus's own doctrinal corpus):** unchanged — a real
  acquisition gap. The Select Letters (vendored) are administrative
  correspondence; Severus's own Christological argument in his own words
  (his Homilies, his anti-Julianist and anti-Chalcedonian treatises) is not
  yet vendored. Named directly in `Open_Gaps_Tracking.md` as the single
  most consequential acquisition gap this session leaves open.

## 12. Open Items Carried Forward to Later Steps

Superset of Doc_01 §10's own list, updated:

1. Self-designation (unresolved).
2. Strand-singular test against Jacob's own ordination theory — may
   require Severus's own writing, not Jacob's (none survives).
3. Chronicle of Edessa placement (unresolved, inherited from
   `NEEDS-RULING.md`).
4. Joshua Stylite's role, `context` vs. `tradition` (unresolved).
5. Zachariah Rhetor book-by-book own-voice/opponent-voice tagging (not
   done).
6. Ghassanid/Theodora chronology — partially confirmed (Theodora's 548
   death, per the vendored file's own footnote), not independently
   cross-checked.
7. Absence of a completed Phase Two portfolio survey (named for the
   project lead).
8. Severus's own doctrinal corpus not yet vendored — the single largest
   named acquisition gap.
9. **New, this document:** the "seventy thousand" baptism figure's exact
   locus within John's own narrative voice (as opposed to the 1860
   editor's Preface) not yet found — see §2.
10. **New, this document:** four secondary/reference works named for this
    world (Menze 2008, Frend 1972, Greatrex/Phenix/Horn 2011, Cambridge
    History vol. 2 ch. 3) are not vendored and not independently
    consulted this session — real acquisition and verification targets,
    not treated as read.
11. **New, this document:** the remaining Severus Select Letters material
    beyond Book VI (other letter collections; the separate Syriac-text-
    only volumes of Book VI itself) is not vendored — see
    `cic/texts/REGISTRY.yaml`.
12. **New, this document:** John of Ephesus, *Lives of the Eastern Saints*,
    ch. 47 (the Tralles mission, per the census's own second documented
    story) is not yet independently located and verified in this file —
    the Ecclesiastical History's own parallel account was verified
    instead; ch. 47 itself remains an open task.
