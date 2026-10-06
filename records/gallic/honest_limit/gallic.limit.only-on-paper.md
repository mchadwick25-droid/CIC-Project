---
id: gallic.limit.only-on-paper
world_id: gallic-monastic-ascetic-christianity
record_type: honest_limit
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-E
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted that this build's evidentiary base for the world is text-only: the source
    ecology survey found no archaeological report, papyrological find, or material-culture study
    specific to any of this world's four sites in this project's library, and named that as a real
    gap rather than as proof that none exists (gallic_Doc02_Source_Ecology.md §5 and §9, items
    1-2: 'none vendored'). This record therefore states what this world's own record can hand a
    participant - words, not stones - and does not claim that nothing has ever been dug up at any
    of these places, which would be a claim about a literature this build has not searched.
sources:
- source_id: gallic.core.gallic
  locus: "thinness: what the island kept day by day 'our record does not hold at all'; cautions: the four editorial place-names that 'occur nowhere in the ancient texts'"
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: "ch. X: the wooden cell, the caves hollowed in the rock, one meal, the copying - the whole of what Tours gives of its own material life"
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: "I-IV: dress, hours, the entrance sequence - Egypt's customs as written for a bishop's new house; IV.2: no one in our monasteries kept it 'even for a year'"
  license: public-domain
- source_id: gallic.search.unopened-volume-sweep
  locus: "nothing new sitting unopened in this project's library for this world"
  license: public-domain
statement: >-
  If you dug up the places we lived, we could not tell you what you would
  find. Not the caves and the wooden cell across the river from Tours. Not
  the island in its harbour. Not the two houses at Marseilles. Nothing we
  can hand you comes out of the ground. All of it comes from books: one
  man's Life of the saint, with his letters and his dialogues; Cassian's
  two books written for a bishop's new house; Vincent's remembrancer; a
  funeral sermon for the island's founder; and a list of authors written
  down a generation after us. Even the names you may know for our places
  are not in our own books, so we do not use them. How do historians know
  about daily life like ours? From what Cassian said Egypt did, and from
  his complaint that no one in Gaul kept it for a year. From what
  Sulpitius said the saint did in his cell. Of the island's own day, not a
  line. What we ate, where we slept, what the rooms looked like - only as
  far as those pages say, and no further.
why_sources_cannot_answer: >-
  No archaeological, papyrological, or material-culture source for any of
  this world's four sites - the two houses near Tours, the island, the
  two houses at Marseilles - is vendored in this project's library, and
  the source ecology survey named that as a real evidentiary gap rather
  than smoothing it over or treating it as proof that no such literature
  exists (gallic_Doc02_Source_Ecology.md §5 'Material Evidence: none
  independently vendored' and §9 items 1-2 'none vendored'; a future
  field-bibliography sweep is flagged there as the remedy). Everything
  this world's own records say about rooms, dress, food, and hours rests
  on textual description alone: Sulpitius's one chapter on the community
  across the river (gallic.source.sulpitius-vita-martini ch. X), Cassian's
  program written as Egypt's customs for a Gallic house
  (gallic.source.cassian-institutes I-IV), and nothing at all from inside
  the island (gallic.core.gallic thinness). The four editorial place-names
  a participant is most likely to bring (gallic.core.gallic cautions) are
  themselves absent from the ancient texts as read. The unopened-volume
  sweep (gallic.search.unopened-volume-sweep) confirms nothing already in
  the library closes this. This is a gap in the evidentiary base this
  build inherited, revisited by re-entering the build if such material is
  later acquired - never by silent edit.
nearest_material:
- gallic.core.gallic
- gallic.term.cell
- gallic.term.the-monks-dress
- gallic.story.honoratus-and-the-island
- gallic.term.gaul
- gallic.demo.record-thinnest
relations: []
use_note:
  means: "The record attests that all it holds of this world's places and daily life comes from a few books, with no excavation and nothing on the island's day."
  not_for:
    - "a claim that nothing has ever been dug up, when the build has not searched that literature"
    - "the island's founder, his arrival and his going to a see, which sit in gallic.story.honoratus-and-the-island"
    - "what the brethren at Tours sang and at what hours, which sits in gallic.term.unceasing-prayer"
    - "the unheard women of the houses, whose one trace, a choir of virgins, sits in gallic.story.death-of-martin-at-condate"
  years: {from: 397, to: 426}
  status: reviewed
---
Closes F5-E at the Answer-the-Canon step (inserted between B-7 and B-8)
as a genuine, declared absence, on the shape of
cappadocian.limit.no-stones-to-show and alx.limit.material-remains -
verified against this world's own Doc_02 rather than assumed to transfer.
The check changed one thing: Cappadocian's record can say its two named
institutions have never been securely identified by excavation, because
its own core record states that as a finding; this world's Doc_02 says
only that nothing material is VENDORED and explicitly warns against
inferring that none exists ("not assume none exists simply because none
is yet vendored," §5). The statement is written to that narrower truth -
what our record can hand you, and where it stops - and the
why_sources_cannot_answer field carries the library-gap framing alx's
record models, with the re-entry rule.

Answers both live variants of the cell in one voice (what digging would
find: we cannot say; how historians know: from the books, and which
books). The list of books in the statement is this world's own Native
corpus as its source records name it: Sulpitius (rows 1-3, 6), Cassian
(rows 7, 9-10), Vincent (row 13), Hilary of Arles's sermon (row 27),
Gennadius (row 30). The "names you may know for our places" sentence
carries gallic.core.gallic's third caution (Ligugé, Marmoutier,
Saint-Victor, Saint-Sauveur) without voicing any of the four names.
Statement register measured with engine/m1/fk.py before commit (see gate
battery).
