---
id: witt.search.unopened-volume-sweep
world_id: lutheran-wittenberg-and-its-congregations
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources: []
query: "Every vendored file this world's own build actually touches -- the ten
  file-codes Doc_03 SS0/Doc_08 SS0 define (v1, v2, v3, LC, SC, Hy, TT, Co, AC,
  Ap) -- cross-checked in both directions against the 95-row
  witt_Source_Registry.md and the 89 records/witt/source/*.md records: (a)
  does every vendored file cic/texts/REGISTRY.yaml lists as supplied for this
  world's build have a Registry row and a source record; (b) does every
  Native Registry row have exactly one source record, and every Excluded row
  correctly none; (c) does any other cic/texts/ entry, or any
  cic/corpus-map/_staging/ file, name Luther/Melanchthon/Wittenberg/
  Karlstadt/Zwingli/Erasmus material this world's own documents (Doc_01,
  Doc_02, Doc_04-Doc_10, the Source Registry) actually rely on without a row
  -- the same shape as the Cappadocian and Gallic worlds' own unopened-volume
  sweeps, run for this world instead."
channel: "direct grep of cic/texts/REGISTRY.yaml for every Luther/Melanchthon/
  Wittenberg/Karlstadt/Zwingli/Erasmus-adjacent filename entry, cross-checked
  against cic/corpus-map/lutheran-wittenberg-and-its-congregations.yaml and
  its cic/corpus-map/_staging/ source files; a field-level cross-check of
  every records/witt/source/*.md record's own external_ids.witt_source_registry_row
  against the live Registry table (94 live rows: 89 Native, 5 Excluded, plus
  one superseded-Excluded row R95), run by script (grep + sort, not tallied
  by hand) rather than trusted from either side's own summary statistics;
  followed by reading each near-miss in its own surrounding document context
  before deciding, 2026-09-19."
result: not_found
found_sources: []
note: "NOTHING NEW FOUND SITTING UNOPENED OR UNROWED. cic/texts/REGISTRY.yaml
  carries exactly ten Luther/Melanchthon-adjacent filename entries for this
  world -- luther_works-v1-selected_jacobs-spaeth1915.txt,
  luther_works-v2-selected_jacobs-spaeth1916.txt,
  luther_works-v3-selected_various1930.txt,
  luther_large-catechism_bente-dau1921.txt,
  luther_small-catechism_smith1994.txt, luther_hymns_bacon-allen.txt,
  luther_table-talk_bell1886.txt, luther_bondage-of-the-will_cole1823.txt,
  melanchthon_augsburg-confession_anon-pg275.txt, and
  melanchthon_apology-augsburg-confession_bente-dau1921.txt -- exactly the
  ten file-codes (v1, v2, v3, LC, SC, Hy, TT, Co, AC, Ap) Doc_03 SS0 and
  Doc_08 SS0 both key against, and exactly the ten files
  cic/corpus-map/_staging/ holds staging entries for. A grep of REGISTRY.yaml
  for Zwingli, Karlstadt, or any other Reformed/Anabaptist-side name returned
  no further filename this world's own build could have drawn on and did
  not: this world's library is genuinely bounded to these ten files, and the
  Registry's own SS13 finding ('Marburg' and 'Zwingli' return zero hits in
  all ten files, independently reproduced this pass) is not an artifact of
  an unsearched corpus -- there is no eleventh file to search.
  ROW-TO-RECORD CROSS-CHECK, run by script rather than trusted from either
  side's own tally: every records/witt/source/*.md record carries an
  external_ids.witt_source_registry_row field; the 89 values recovered are
  1-32, 34-54, 56, 59-93 -- exactly the Registry's 89 live Native rows, with
  no duplicate and no row skipped inside that set. The six absent numbers
  (33, 55, 57, 58, 94, 95) are exactly the Registry's own six Excluded rows
  (R33 Out-of-Boundary; R55, R57, R58, R94 Named Comparandum; R95
  superseded-Excluded, correctly carrying no live record of its own since
  R55 now covers its material directly). No Native row lacks a record; no
  Excluded row has one it should not. This is a clean, exhaustive 1:1
  mapping, not a sampled check.
  CANDIDATES CHECKED AND CLEARED, not waved through on a keyword match
  alone: (1) Melanchthon's Loci Communes (1521) is quoted only as an
  incidental phrase inside R32's own Verification Note ('Lauterbach's notes
  collected into sure and certain Loci Communes,' the Table Talk's own
  collection method as Aurifaber describes it) -- not Melanchthon's 1521
  systematic theology itself, which is not vendored and has no row. This is
  a real absence, but it is a wider-literature gap (Step 3 below), not an
  unopened file sitting in cic/texts/: no vendored Loci Communes text
  exists in this project's library for a sweep to find. (2) The Weimarer
  Ausgabe (WA) -- named only inside R63's own Verification Note as
  editorial background ('Weimar/Erlangen/Berlin/Walch/Clemen,' the German
  critical-edition lineage the Philadelphia editors describe themselves
  working from) -- not a text this world's own documents draw claims from,
  correctly unrowed. (3) The four corpus-map gaps Doc_02 SS0 and SS16 item 1
  already name (v1 Prefaces 1539/1545 = R1; v2 Doctrines of Men = R16; v3
  Magnificat = R18; v3's three Emser writings = R21-R23) -- checked against
  cic/corpus-map/lutheran-wittenberg-and-its-congregations.yaml directly:
  all four are genuinely absent from the corpus-map's own work list even
  though the underlying vendored files hold them and the Registry rows them
  correctly. This is not a discovery-sweep finding (the texts are vendored
  and rowed) but a corpus-map indexing gap Doc_02 already disclosed and
  explicitly assigned to the coach thread, not this build thread, to fix
  (SS16 item 1) -- named here only so a reader of this sweep does not
  mistake its absence from this note for an unchecked area.
  NO ADJACENT FINDING of the shape the Cappadocian and Gallic sweeps
  defined (a source cited load-bearing by a sibling document but never
  given a Registry row) turned up here: every filename candidate this pass
  checked was either already rowed, an incidental phrase inside an
  already-rowed row's own apparatus, or a named, already-disclosed absence
  outside this project's vendored library entirely. This is consistent
  with, not surprising given, witt_Source_Registry.md's own five-revision
  review history (Round 1 through the Round 5 ZellFinalCheck) plus an
  independent post-approval script re-verification of all 95 rows at 11
  columns -- a Registry put through more successive independent rounds than
  either the Cappadocian or Gallic precedent before this sweep began, so a
  sweep run after that scrutiny should expect at most a small residue, and
  found none."
---
THE SHAPE THIS WORLD'S OWN SWEEP TOOK, run the same way Cappadocian's and
Gallic's were and landing at the same "nothing new" result both of theirs
did.

Five successive review rounds already ran against witt_Source_Registry.md
before this sweep began (witt_Doc02_Review_Round1.md,
witt_Doc02_Review_Round2.md, witt_Doc02_SpotCheck_Round3.md,
witt_Doc02_Round4_ZellCheck.md, witt_Doc02_Round5_ZellFinalCheck.md), each
one hunting specifically for missing, mistiered, or mishandled sources
across five successive revisions, plus a script-run independent
re-verification of the finished table's own schema and statistics. By the
time this sweep started, the obvious misses -- and several non-obvious ones,
including a undisclosed evidentiary-basis upgrade caught only at Round 5 --
were already found and fixed by that process, not by this one. What a
discovery sweep run after that kind of scrutiny should expect to find is
not a pile of overlooked volumes but, at most, a small residue. This pass
found none: every filename candidate checked either resolved to an
already-rowed source, an incidental phrase inside an already-rowed row's
own apparatus, or a named, already-disclosed absence entirely outside this
project's vendored library.

WHY THE ROW-TO-RECORD CROSS-CHECK MATTERED TO RUN ANYWAY, even though the
file-discovery half cleared instantly. B-1's own construction script parsed
the Registry's full 95-row table already, so the more realistic place for a
genuine miss to hide was not in cic/texts/ itself but in the row-to-record
step -- a row correctly identified by the Registry but somehow dropped,
duplicated, or mis-numbered on the way into records/witt/source/. Running
that cross-check by script against each record's own
external_ids.witt_source_registry_row field, rather than trusting either
side's own summary count, is the check that actually tests B-1's
construction step, not merely re-confirms the Registry's own arithmetic.
It reproduced a clean 1:1 mapping with no gap on either side.

WHAT THIS RESULT MEANS FOR B-1. This world's Source Registry's own
completeness claim -- every vendored file this build's documents cite has a
checkpoint row, and every Native row has a source record -- is not merely
asserted here but independently tested against the vendored-text library,
the corpus-map, and the record set itself, and found to hold, with zero
residue on the file-discovery side and a clean, script-verified 1:1
mapping on the row-to-record side. B-1's 89 source records and its one
world_core record rest on a Registry this sweep did not find any gap in.

SATURATION STATEMENT AND COVERAGE LIMITS -- stated plainly rather than
implied by a clean sweep result, since B-1a's own instruction is that a
zero-miss discovery sweep is not the same claim as "this world's evidence
base is complete." This world's own Doc_02 SS11-SS13 (the Source Asymmetry
Assessment, the Missing Voices Assessment, and the Forces Lens) already
name this world's real coverage limits in detail, and this sweep adopts
them rather than re-deriving a separate list:

- The asymmetry is inverted, not merely thin (Doc_02 SS11): the
  congregational register with the largest ecological role in this world
  (the catechism learned at home, the hymn sung weekly, the visitation
  examination) has the smallest evidential footprint in the library, which
  is overwhelmingly the founder's own argued doctrine (~90% of the words
  across the ten files).
- No woman's own text is vendored (Doc_02 SS12.1): the library holds no
  primary source written by a woman. Grumbach's 1523 letter (R54) is Native
  by a session-verified naming claim but the primary edition (Matheson
  1995) is itself unread; Zell's corpus (R55) is Excluded by a disclosed
  conservative default, not a demonstrated finding, and remains real,
  named, and unvendored.
- No ordinary parish record is vendored (Doc_02 SS12.2, SS7): the 1527-28
  Saxon visitation protocols exist and were written by this world's own
  movement, but sit untranslated and unvendored (R51, R52) -- this world's
  Representative has not read them, and this build cannot construct the
  parish's own experience of being inspected from anything currently in
  hand.
- The two texts most consequential to this world's ethical record -- *On
  the Jews and Their Lies* (1543, R49) and *Against the Murderous, Thieving
  Hordes of Peasants* (1525, R48) -- are both genuinely unvendored (rights
  and hosting barriers, G1 Part B, not neglect), characterized in this
  build only from tertiary description (R83), and explicitly barred by R94
  from ever being reached for as if in hand.
- The Reformed and Roman Catholic contemporaries appear only as this
  world's own texts represent them (the "(context)" rows, R36, R39-R43),
  never in their own voice; the Marburg Articles (R56), signed by this
  world's own leaders, remain a located but unread lead.
- A period-specific German/Latin lexicon is not vendored (R87); Doc_03's
  term work draws only on the translators' own glossing footnotes, not a
  period reference work.

None of these limits is new: this sweep's contribution is confirming, by
independent file-level and row-level checking rather than by restating
Doc_02's own prose, that the coverage gaps this world's build already
disclosed are the real and complete set -- not a partial list sitting
alongside an undisclosed further gap this sweep would have caught.
