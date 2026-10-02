# Library PR 656: commentary moved out of live surfaces
Text removed or reworded in live and canonical files so that `tools/check_live_commentary.py --enforce` passes on the files this branch edits. Each entry gives the text as it stood and the text that replaced it, verbatim, grouped by file. In `download-queue-seed.yaml` the `verified_by` dates stay in the seed; `gen_download_queue.py` now writes them in words in `DOWNLOAD-QUEUE.md`. `DOWNLOAD-QUEUE.md` was regenerated from the seed, which added the 36 seed rows the committed copy had not yet picked up. `tools/tests/test_check_live_commentary.py` pins a different currently flagged line as its REWRITE sample, because the line it pinned in `DOWNLOAD-QUEUE.md` no longer carries an ISO date. In `cic/engine/corpus_map_merge.py` the variable `todo` became `pending_rows`; no comment text moved.

## Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md

### 1

As it stood:

~~~
 *(Re-keyed 2026-08-05, full-system review Rigor P1-2, off the SS3.0 discovery-channel/verification-state/evidentiary-weight axes — mechanically enforced by `wrs/gates/core.py::gate_priority_review_trigger`. The prior rule, "Flag anything at Confidence C or below," assumed the Confidence letter's B still meant "specific work/locus named"; after the Round-1 recalibration redefined B to mean recall, the legacy letter stopped marking the actual risk boundary.)*
~~~

Now reads:

~~~
 *(Keyed off the SS3.0 discovery-channel/verification-state/evidentiary-weight axes and mechanically enforced by `wrs/gates/core.py::gate_priority_review_trigger`. The Confidence letter alone does not mark the risk boundary, because B means recall.)*
~~~

### 2

As it stood:

~~~
 It does not attempt to check a candidate source against what any other world has already claimed as native — that is a genuinely different, harder problem (a mechanism that has to hold up across dozens of worlds, not protect one), and an earlier attempt to solve both problems in one document at once produced a design that did neither well. Cross-world checking is intentionally left as open, named follow-up work, not folded in here.
~~~

Now reads:

~~~
 It does not check a candidate source against what any other world has already claimed as native. That is a different, harder problem: a mechanism that has to hold up across dozens of worlds, not protect one.
~~~

## Build/worlds/witt/witt_Doc_01_World_Identification_Boundaries_Orientation.md

### 1

As it stood:

~~~
as host-verified by "direct fetch, 2026-09-15," rights basis
~~~

Now reads:

~~~
as host-verified by direct fetch on 15 September 2026, rights basis
~~~

## Build/worlds/lpc/Source_Registry.md

### 1

As it stood:

~~~
 The whole *Vita*, Preface and chapters I–XXXI, has been read (`Review-Artifacts/Possidius_Full_Read_2026-09-16.md`) |
~~~

Now reads:

~~~
 The whole *Vita*, Preface and chapters I–XXXI, has been read |
~~~

## Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md

### 1

As it stood:

~~~
`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, 2026-09-26 entry; that entry
~~~

Now reads:

~~~
`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`; that entry
~~~

## Build/worlds/latap/Step0_Movement_Scope_Confirmation.md

### 1

As it stood:

~~~
the approved slate of 2026-09-29 keeps him on this shelf
~~~

Now reads:

~~~
the approved slate keeps him on this shelf
~~~

### 2

As it stood:

~~~
The only written record of the ruling is the System Hub decision log entry of 2026-09-26, "Two
~~~

Now reads:

~~~
The only written record of the ruling is the System Hub decision log entry "Two
~~~

### 3

As it stood:

~~~
 That entry records it as a ruling dated 2026-09-10, restates this document's own text, and quotes
~~~

Now reads:

~~~
 That entry restates this document's own text and quotes
~~~

### 4

As it stood:

~~~
the Round 1 and Round 3 review artifacts record that wording, and the census no longer carries it.
~~~

Now reads:

~~~
the census no longer carries that wording.
~~~

### 5

As it stood:

~~~
with no XML parser, run on 2026-09-29 over
~~~

Now reads:

~~~
with no XML parser, run over
~~~

### 6

As it stood:

~~~
All but two were vendored on 2026-09-29. The exceptions are Hartel's CSEL 3 (2026-09-05) and Robinson (2026-09-08).
~~~

Now reads:

~~~
All but two were vendored together. The exceptions are Hartel's CSEL 3 and Robinson.
~~~

### 7

As it stood:

~~~
(archive.org title search, 2026-09-21, recorded in the Source Readiness Dossier)
~~~

Now reads:

~~~
(archive.org title search, recorded in the Source Readiness Dossier)
~~~

### 8

As it stood:

~~~
built records on 2026-09-29: both are used
~~~

Now reads:

~~~
built records: both are used
~~~

### 9

As it stood:

~~~
direct check performed 2026-09-29, covering
~~~

Now reads:

~~~
direct check covering
~~~

### 10

As it stood:

~~~
re-checked directly on 2026-09-29. `cic/corpus-map/latin-pastoral
~~~

Now reads:

~~~
checked directly. `cic/corpus-map/latin-pastoral
~~~

### 11

As it stood:

~~~
the Library decision log entry of 2026-09-29, "Cross-world
~~~

Now reads:

~~~
the Library decision log entry "Cross-world
~~~

### 12

As it stood:

~~~
Re-read on 2026-09-29: the census entry for I.33
~~~

Now reads:

~~~
Read directly: the census entry for I.33
~~~

### 13

As it stood:

~~~
A search of `records/` on 2026-09-29 for
~~~

Now reads:

~~~
A search of `records/` for
~~~

### 14

As it stood:

~~~
swept read-only on 2026-09-29 for all six
~~~

Now reads:

~~~
swept read-only for all six
~~~

### 15

As it stood:

~~~
All of them are new since Round 5 and await review.
~~~

Now reads:

~~~
All of them are new material and await review.
~~~

### 16

As it stood:

~~~
the approved slate of 2026-09-29 keeps both on the shelf
~~~

Now reads:

~~~
the approved slate keeps both on the shelf
~~~

### 17

As it stood:

~~~
The Library decision log entry of 2026-09-29, "Window slate
~~~

Now reads:

~~~
The Library decision log entry "Window slate
~~~

### 18

As it stood:

~~~
`cic-website/data/world-census.json` on 2026-09-29:
~~~

Now reads:

~~~
`cic-website/data/world-census.json`:
~~~

### 19

As it stood:

~~~
re-run read-only on 2026-09-29.
~~~

Now reads:

~~~
run read-only.
~~~

## cic/corpus-map/_staging/bell_jews-christians-egypt-meletian-papyri_1924.yaml

### 1

As it stood:

~~~
      open item 1, and this world's own Open_Gaps_Tracking.md). Not yet
      cited by any quote,
~~~

Now reads:

~~~
      item 1, and this world's own Open_Gaps_Tracking.md). Not
      cited by any quote,
~~~

## cic/corpus-map/_staging/calvin_letters-vol1_bonnet1858.yaml

### 1

As it stood:

~~~
Vols. I-II) - a genuinely open gap.
~~~

Now reads:

~~~
Vols. I-II) - Vol. III is absent from the corpus.
~~~

## cic/corpus-map/_staging/gregory-great_dialogues_gardner1911.yaml

### 1

As it stood:

~~~
      own coverage overlaps is not yet resolved
      (roman-church-gregorian_Source_Readiness_Dossier.md §5).
~~~

Now reads:

~~~
      own coverage overlaps is undetermined
      (roman-church-gregorian_Source_Readiness_Dossier.md §5).
~~~

## cic/corpus-map/_staging/luther_works-v3-selected_various1930.yaml

### 1

As it stood:

~~~
Closes the gap witt_Source_Registry.md's
      R18 flagged
~~~

Now reads:

~~~
Closes the gap that row R18 of
      witt_Source_Registry.md flagged
~~~

## cic/corpus-map/_staging/tertullian_quae-supersunt-t2-polemica-lat_oehler1853.yaml

### 1

As it stood:

~~~
the treatise heading itself is not caught by grep)
~~~

Now reads:

~~~
grep does not find the treatise heading itself)
~~~

## Build/worlds/_cross-world/dossiers/latin-apologists_Source_Readiness_Dossier.md

### 1

As it stood:

~~~
**Dossier author / date:** source-acquisition research thread, 2026-09-21;
refreshed 2026-09-29 (see the refresh note below)
**Corpus-map / `cic/texts/` state as of:** the working tree of branch
`claude/busy-pasteur-4sx229` on 2026-09-29 (HEAD `d1140c9f`). The
2026-09-21 pass was made against `main` @ commit `820550b`.

**Refresh, 2026-09-29.** This dossier was brought up to the Library as it
stood on that date. Since the 2026-09-21 pass, the original-language
witnesses for this shelf were vendored (§1), Commodian's *Carmen
apologeticum* joined the shelf in Latin, the approved window slate was
applied to the corpus map, and the Step 0 was revised with the dating
research. Findings of the 2026-09-21 pass that still hold are kept and
dated. Findings that changed are rewritten.

~~~

Now reads:

~~~
**Dossier author:** source-acquisition research thread
**Corpus-map / `cic/texts/` state:** the current working tree

The original-language witnesses for this shelf are vendored (§1). Commodian's
*Carmen apologeticum* is on the shelf in Latin. The approved window slate is
applied to the corpus map, and the Step 0 carries the dating research.

~~~

### 2

As it stood:

~~~
§1 gives the recount of 2026-09-29 and says which works it does not cover. The Step 0 was revised
on 2026-09-29, and that revision has not yet been independently reviewed.

~~~

Now reads:

~~~
§1 gives the recount and says which works it does not cover. The Step 0's
revision with the dating research awaits independent review.

~~~

### 3

As it stood:

~~~
counted
by distinct work on 2026-09-29.
~~~

Now reads:

~~~
counted
by distinct work.
~~~

### 4

As it stood:

~~~
Word counts are Step 0's recount of 2026-09-29 (§3 B1,
~~~

Now reads:

~~~
Word counts are Step 0's recount (§3 B1,
~~~

### 5

As it stood:

~~~
English text of 40 works on 2026-09-29: the original
~~~

Now reads:

~~~
English text of 40 works: the original
~~~

### 6

As it stood:

~~~
CC BY-SA 4.0; vendored 2026-09-29): CSEL 4
~~~

Now reads:

~~~
CC BY-SA 4.0): CSEL 4
~~~

### 7

As it stood:

~~~
apparatus interleaved; vendored 2026-09-29 unless stated):
~~~

Now reads:

~~~
apparatus interleaved):
~~~

### 8

As it stood:

~~~
(vendored 2026-09-05, now also assigned
  here for
~~~

Now reads:

~~~
(now also assigned
  here for
~~~

### 9

As it stood:

~~~
Latin and Greek; vendored 2026-09-08): carried
~~~

Now reads:

~~~
Latin and Greek): carried
~~~

### 10

As it stood:

~~~
own count, verified 2026-09-29).
~~~

Now reads:

~~~
own count).
~~~

### 11

As it stood:

~~~
- **A real defect found and fixed in the 2026-09-21 pass, not merely
  named; re-verified 2026-09-29.**

~~~

Now reads:

~~~
- **A stale slug in a staging file, repointed.**

~~~

### 12

As it stood:

~~~
It was
  repointed to `latin-apologists` and re-merged on 2026-09-21. On
  2026-09-29 the row is on the generated shelf
~~~

Now reads:

~~~
It is
  repointed to `latin-apologists` and merged, and the row is on the generated shelf
~~~

### 13

As it stood:

~~~
None as of 2026-09-29. See §4
~~~

Now reads:

~~~
None. See §4
~~~

### 14

As it stood:

~~~
(title search, 2026-09-21): zero results.
~~~

Now reads:

~~~
(title search): zero results.
~~~

### 15

As it stood:

~~~
it was vendored on 2026-09-29 (CSEL 15 scan and TEI, §1), and
~~~

Now reads:

~~~
it is vendored (CSEL 15 scan and TEI, §1), and
~~~

### 16

As it stood:

~~~
Checked against `archive.org` (2026-09-21): Jerome's
~~~

Now reads:

~~~
Checked against `archive.org`: Jerome's
~~~

### 17

As it stood:

~~~
On 2026-09-29 the research pass found the passage's Latin
~~~

Now reads:

~~~
A later research pass found the passage's Latin
~~~

### 18

As it stood:

~~~
A critical edition is still not on the shelf: the 2026-09-21 pass recorded that Helm's is not public domain, while the 2026-09-29 research says Helm 1913 is public domain by date but was not found on archive.org. That disagreement is unresolved here.
~~~

Now reads:

~~~
A critical edition is not on the shelf. The first pass recorded that Helm's is not public domain; the later research says Helm 1913 is public domain by date but was not found on archive.org. The two records disagree.
~~~

### 19

As it stood:

~~~
Only an 1721 edition was found on archive.org (2026-09-29).
~~~

Now reads:

~~~
Only an 1721 edition was found on archive.org.
~~~

### 20

As it stood:

~~~
not opened in the 2026-09-29 research pass; their
~~~

Now reads:

~~~
not opened in the research pass; their
~~~

### 21

As it stood:

~~~
log entry of 2026-09-29 records the approved
~~~

Now reads:

~~~
log entry records the approved
~~~

### 22

As it stood:

~~~
Checked 2026-09-29: neither
~~~

Now reads:

~~~
Checked directly: neither
~~~

## Build/worlds/_cross-world/dossiers/greek-apologists-second-century_Source_Readiness_Dossier.md

### 1

As it stood:

~~~
**Dossier author / date:** source-acquisition research thread, 2026-09-21.
**Refresh, 2026-09-29:** reviewed with its Step 0 in Rounds 6 and 7. Sections 1 to 5
are restated to the library as it stands: the corpus-map shelf (17 works),
the original-language witnesses added to `cic/texts/`, the Apologists
window slate and the Tatian ruling in
`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (four entries of that
date, one of which corrects a sentence of another), and the revised Step 0. The refresh corrects four statements of the
first version: the Dialogue word count credited to Step 0 (Step 0 states
no word counts), the claim that Step 0 recounted the roster
"independently", the "Revision 7" label (Step 0 carries no revision
number), and Routh's *Reliquiae sacrae* vol. V as a Melito lead (it holds
Archelaus and creeds; Melito is in vol. I, which is vendored).
**Corpus-map / `cic/texts/` state as of:** 2026-09-29, the working tree on
top of commit `9452a7d7`. The first version was checked against `main` @
`820550b`.

~~~

Now reads:

~~~
**Dossier author:** source-acquisition research thread.
Sections 1 to 5 describe the library as it stands: the corpus-map shelf (17 works),
the original-language witnesses in `cic/texts/`, the Apologists
window slate and the Tatian ruling in
`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`, and the Step 0. Step 0 states
no word counts and carries no revision number. Routh's *Reliquiae sacrae* vol. V holds
Archelaus and creeds; Melito is in vol. I, which is vendored.
**Corpus-map / `cic/texts/` state:** the current working tree.

~~~

### 2

As it stood:

~~~
(title and creator search, 2026-09-21): no public
~~~

Now reads:

~~~
(title and creator search): no public
~~~

### 3

As it stood:

~~~
(title search, 2026-09-21) for an English
~~~

Now reads:

~~~
(title search) for an English
~~~

## cic/corpus-map/_staging/download-queue-seed.yaml

### 1

As it stood:

~~~
    vendored_note: "vendored 2026-09-13 by the ijc thread from the sibling archive.org item vitasanctiambros0000paul; this seed row's identifier never resolved to the file used"
~~~

Now reads:

~~~
    vendored_note: "vendored by the ijc thread from the sibling archive.org item vitasanctiambros0000paul; this seed row's identifier never resolved to the file used"
~~~

### 2

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; the host catalogues this scan [187-?], not 1859"
~~~

Now reads:

~~~
    vendored_note: "vendored; the host catalogues this scan [187-?], not 1859"
~~~

### 3

As it stood:

~~~
    vendored_note: "vendored 2026-09-29 as a second witness; Thomson-Forester 1909 (suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt) had already closed pahc's need"
~~~

Now reads:

~~~
    vendored_note: "vendored as a second witness; Thomson-Forester 1909 (suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt) had already closed pahc's need"
~~~

### 4

As it stood:

~~~
    vendored_note: "vendored 2026-09-29"
~~~

Now reads:

~~~
    vendored_note: "vendored"
~~~

### 5

As it stood:

~~~
    vendored_note: "vendored 2026-09-29"
~~~

Now reads:

~~~
    vendored_note: "vendored"
~~~

### 6

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Easton 1934 is a Cambridge University Press (UK) edition (copyright notice: Copyright 1934, Cambridge University Press; reprinted 1962). Gutenberg lists it as public domain in the US, but that is the host's own clearance, not a licence, and INTAKE.md treats foreign-published 1931+ translations as presumed URAA-restored. Needs a ruling from Mark, or a renewal/URAA check."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Easton 1934 is a Cambridge University Press (UK) edition (copyright notice: Copyright 1934, Cambridge University Press; reprinted 1962). Gutenberg lists it as public domain in the US, but that is the host's own clearance, not a licence, and INTAKE.md treats foreign-published 1931+ translations as presumed URAA-restored. Needs a ruling from Mark, or a renewal/URAA check."
~~~

### 7

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 8

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 9

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 10

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 11

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 12

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 13

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

Now reads:

~~~
    vendored_note: "vendored; machine-corrected transcription of the CSEL scan, preferred base for quoting, with the CSEL 41 volume scan (corpusscriptoru18wiengoog) as the print check"
~~~

### 14

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; the only Latin witness of De fide et symbolo, De continentia, De bono viduitatis, De adulterinis coniugiis, De divinatione daemonum, De cura pro mortuis gerenda and De patientia; the print check on the seven csel-dev TEI files"
~~~

Now reads:

~~~
    vendored_note: "vendored; the only Latin witness of De fide et symbolo, De continentia, De bono viduitatis, De adulterinis coniugiis, De divinatione daemonum, De cura pro mortuis gerenda and De patientia; the print check on the seven csel-dev TEI files"
~~~

### 15

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; Latin of the catechetical work of Registry row 15; the German notes are modern scholarship"
~~~

Now reads:

~~~
    vendored_note: "vendored; Latin of the catechetical work of Registry row 15; the German notes are modern scholarship"
~~~

### 16

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; pre-critical Maurist text; high OCR misread rate; a finding aid, not a quotable text"
~~~

Now reads:

~~~
    vendored_note: "vendored; pre-critical Maurist text; high OCR misread rate; a finding aid, not a quotable text"
~~~

### 17

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; pre-critical Maurist text; OCR misreads about one word in ten; a finding aid, not a quotable text"
~~~

Now reads:

~~~
    vendored_note: "vendored; pre-critical Maurist text; OCR misreads about one word in ten; a finding aid, not a quotable text"
~~~

### 18

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; first edition of the 33 Guelferbytanus sermons; ascription of individual sermons not decided by the file"
~~~

Now reads:

~~~
    vendored_note: "vendored; first edition of the 33 Guelferbytanus sermons; ascription of individual sermons not decided by the file"
~~~

### 19

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; OCR misreads about one word in five or six; several sermons not Augustine's per later scholarship"
~~~

Now reads:

~~~
    vendored_note: "vendored; OCR misreads about one word in five or six; several sermons not Augustine's per later scholarship"
~~~

### 20

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; holds the Acta Cypriani (no. 13) and the Passiones of Marianus and Jacobus (no. 15) and of Montanus and Lucius (no. 16) in Latin"
~~~

Now reads:

~~~
    vendored_note: "vendored; holds the Acta Cypriani (no. 13) and the Passiones of Marianus and Jacobus (no. 15) and of Montanus and Lucius (no. 16) in Latin"
~~~

### 21

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; holds the Acta S. Cypriani (no. XI) and the Passiones of Marianus and Jacobus (no. XIII) and of Montanus and Lucius (no. XIV) in Latin"
~~~

Now reads:

~~~
    vendored_note: "vendored; holds the Acta S. Cypriani (no. XI) and the Passiones of Marianus and Jacobus (no. XIII) and of Montanus and Lucius (no. XIV) in Latin"
~~~

### 22

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; German scholarship on Cyprian's treatises and penance; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; German scholarship on Cyprian's treatises and penance; consultation-only"
~~~

### 23

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; German scholarship on Cyprian and the Roman see; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; German scholarship on Cyprian and the Roman see; consultation-only"
~~~

### 24

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; German scholarship; 1930 imprint at the edge of the Library's 1930-or-earlier rule; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; German scholarship; 1930 imprint at the edge of the Library's 1930-or-earlier rule; consultation-only"
~~~

### 25

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; German scholarship on Western penance; the continuation the preface announces is not in the file; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; German scholarship on Western penance; the continuation the preface announces is not in the file; consultation-only"
~~~

### 26

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; French scholarship on Cyprian's theology; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; French scholarship on Cyprian's theology; consultation-only"
~~~

### 27

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; French reference work on the African sees and their bishops; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; French reference work on the African sees and their bishops; consultation-only"
~~~

### 28

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; the Numidia volume only; the other provinces are separate volumes, not vendored"
~~~

Now reads:

~~~
    vendored_note: "vendored; the Numidia volume only; the other provinces are separate volumes, not vendored"
~~~

### 29

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; French scholarly history of the city; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; French scholarly history of the city; consultation-only"
~~~

### 30

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; German scholarship on the Stephen-Cyprian baptism dispute; the first part of the work whose appendix is already vendored"
~~~

Now reads:

~~~
    vendored_note: "vendored; German scholarship on the Stephen-Cyprian baptism dispute; the first part of the work whose appendix is already vendored"
~~~

### 31

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Low priority: Augustine's anti-Manichaean works; the English of the Reply to Faustus is vendored in npnf104 (Registry row 22), and the Latin of Contra Adimantum is on csel-dev."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Low priority: Augustine's anti-Manichaean works; the English of the Reply to Faustus is vendored in npnf104 (Registry row 22), and the Latin of Contra Adimantum is on csel-dev."
~~~

### 32

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Low priority, outside the window: the history concerns the persecution under the Vandal kings Geiseric and Hunneric (the edition's preface cites the work as 'Victoris Vitensis historia persecutionis Africanae prouinciae sub Geiserico et Hunirico regibus Wandalorum'), after c. 430."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Low priority, outside the window: the history concerns the persecution under the Vandal kings Geiseric and Hunneric (the edition's preface cites the work as 'Victoris Vitensis historia persecutionis Africanae prouinciae sub Geiserico et Hunirico regibus Wandalorum'), after c. 430."
~~~

### 33

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Low priority: a fragment of the corpus (the Mauretanian provinces), not the Proconsularis or Numidia inscriptions; the CIL VIII Supplement for Numidia is already vendored."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Low priority: a fragment of the corpus (the Mauretanian provinces), not the Proconsularis or Numidia inscriptions; the CIL VIII Supplement for Numidia is already vendored."
~~~

### 34

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Optatus and Tyconius passages."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Optatus and Tyconius passages."
~~~

### 35

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Cyprian passages."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Cyprian passages."
~~~

### 36

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Augustine, Donatist and Petilian passages."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The sweep counted its Augustine, Donatist and Petilian passages."
~~~

### 37

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 38

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 39

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. Not on the list this row's batch was given; recorded because the sweep opened it and its metadata verifies. Its title page was not read, so its volume statement rests on the host record."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. Not on the list this row's batch was given; recorded because the sweep opened it and its metadata verifies. Its title page was not read, so its volume statement rests on the host record."
~~~

### 40

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The scan is the Republican Period volume; the volumes on the imperial period, where the Christian Latin authors stand, were not opened."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The scan is the Republican Period volume; the volumes on the imperial period, where the Christian Latin authors stand, were not opened."
~~~

### 41

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 42

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 43

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 44

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The scan is Volume II, not Volume I, and a mid-century reprint printing; the rights basis for that printing is not settled here, on the ground the Library applies to reprint facsimiles, and Volume I was not opened."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library. The scan is Volume II, not Volume I, and a mid-century reprint printing; the rights basis for that printing is not settled here, on the ground the Library applies to reprint facsimiles, and Volume I was not opened."
~~~

### 45

As it stood:

~~~
    hold_note: "Held 2026-09-29, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. Reference tier: a field bibliography opened for the sweep, not vendored. It names works and scholarship for lpc and is consulted, not quoted; low priority for the Library."
~~~

### 46

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: outside the world's window and about 22 MB. Use the Toronto scans of the original Burrows printing; the Pageant Book Company scans (for example jesuitrelationsa0011reub) are modern facsimile reprints and are excluded."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: outside the world's window and about 22 MB. Use the Toronto scans of the original Burrows printing; the Pageant Book Company scans (for example jesuitrelationsa0011reub) are modern facsimile reprints and are excluded."
~~~

### 47

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: before Borgia's generalate, about 4 MB."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: before Borgia's generalate, about 4 MB."
~~~

### 48

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored, to stay inside the size budget: about 10 MB for five volumes. Fetch and register the same way as the vendored MHSI volumes."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored, to stay inside the size budget: about 10 MB for five volumes. Fetch and register the same way as the vendored MHSI volumes."
~~~

### 49

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored, to stay inside the size budget. The series ran to 1932, so check each volume's own title-page year, and vendor only volumes printed 1930 or earlier."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored, to stay inside the size budget. The series ran to 1932, so check each volume's own title-page year, and vendor only volumes printed 1930 or earlier."
~~~

### 50

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored, to stay inside the size budget: about 16 to 20 MB. Volume 8 was printed in 1923, inside the date rule."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored, to stay inside the size budget: about 16 to 20 MB. Volume 8 was printed in 1923, inside the date rule."
~~~

### 51

As it stood:

~~~
    why: "The request's R11 names the Madrid printing of 1597-1602. Only the Cologne printing of 1612-1615 (16 volumes, Latin) was found on the reachable hosts."
~~~

Now reads:

~~~
    why: "The request names the Madrid printing of 1597-1602. Only the Cologne printing of 1612-1615 (16 volumes, Latin) was found on the reachable hosts."
~~~

### 52

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: sixteen large volumes, probably over 30 MB, and a seventeenth-century printing whose OCR was not sampled. Needs a ruling on whether the Cologne printing stands in for the Madrid one."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: sixteen large volumes, probably over 30 MB, and a seventeenth-century printing whose OCR was not sampled. Needs a ruling on whether the Cologne printing stands in for the Madrid one."
~~~

### 53

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: the Ratio is covered by the Institutum; about 5.5 MB for the four volumes."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: the Ratio is covered by the Institutum; about 5.5 MB for the four volumes."
~~~

### 54

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: it is a secondary French narrative and not de Nobili's own text. De Nobili's Latin and Portuguese originals and the documents of the rites controversy were not found on the reachable hosts."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: it is a secondary French narrative and not de Nobili's own text. De Nobili's Latin and Portuguese originals and the documents of the rites controversy were not found on the reachable hosts."
~~~

### 55

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: a lead, not a request. Ribadeneira's Latin Life of Ignatius (1572) is already vendored."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: a lead, not a request. Ribadeneira's Latin Life of Ignatius (1572) is already vendored."
~~~

### 56

As it stood:

~~~
    hold_note: "Blocked 2026-09-30, not vendored: the file server returned 500. Retry the raw *_djvu.txt download; vendor only the raw file. Volume 2 (1882) was not located."
~~~

Now reads:

~~~
    hold_note: "Blocked, not vendored: the file server returned 500. Retry the raw *_djvu.txt download; vendor only the raw file. Volume 2 (1882) was not located."
~~~

### 57

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: mostly after the window, 1.07 MB. The appendix on the Brethren's confessions from the founding to the 1570s could carry the 1504 and 1508 texts and was not read."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: mostly after the window, 1.07 MB. The appendix on the Brethren's confessions from the founding to the 1570s could carry the 1504 and 1508 texts and was not read."
~~~

### 58

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored, to stay inside the size budget (4.9 MB). Palacky's Documenta and Goll's edition of Brezova are vendored and cover the Relatio and Brezova."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored, to stay inside the size budget (4.9 MB). Palacky's Documenta and Goll's edition of Brezova are vendored and cover the Relatio and Brezova."
~~~

### 59

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: later editions of works Erben and Novotny already give. Check each volume's printed year, since the series ran into the 1900s."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: later editions of works Erben and Novotny already give. Check each volume's printed year, since the series ran into the 1900s."
~~~

### 60

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored. The 1535 printing is the better witness of the Confession if its OCR is cleaner than Brown's; read the host library's rights statement first."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored. The 1535 printing is the better witness of the Confession if its OCR is cleaner than Brown's; read the host library's rights statement first."
~~~

### 61

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: German hymns of the sixteenth century, mostly after the window."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: German hymns of the sixteenth century, mostly after the window."
~~~

### 62

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: scholarship and not a source; a reference-tier lead."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: scholarship and not a source; a reference-tier lead."
~~~

### 63

As it stood:

~~~
    hold_note: "Held 2026-09-30, not vendored: not cleaner than the vendored 1592 and 1524 printings."
~~~

Now reads:

~~~
    hold_note: "Held, not vendored: not cleaner than the vendored 1592 and 1524 printings."
~~~

### 64

As it stood:

~~~
    vendored_note: "vendored 2026-09-29; English biography; consultation-only"
~~~

Now reads:

~~~
    vendored_note: "vendored; English biography; consultation-only"
~~~
