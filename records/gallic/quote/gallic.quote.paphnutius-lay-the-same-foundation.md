---
id: gallic.quote.paphnutius-lay-the-same-foundation
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted and Documented at its locus (Conferences XVIII.15) as Piamun's own closing exhortation
    to Cassian and Germanus - the stated moral the whole story is told to teach, not a narrated event.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43079-43084): Piamun's closing
    statement that Paphnutius's boyhood already showed his future character, and his exhortation to lay
    the same foundation"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what the Paphnutius story is finally for, or what virtue it teaches"
  - "conversation reaches humility or patience as a foundation to be laid, not a height reached at once"
  prefer_instead:
  - "participant wants the whole story first - retrieve gallic.story.paphnutius-and-the-hidden-book"
text: >-
  He then in his early youth already gave these signs of his future character, and even in his boyish
  years sketched the lines of that perfection which was to grow up in mature age. If then we want to
  attain to his height of virtue, we must lay the same foundation to begin with.
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  Piamun does not end by praising Paphnutius; he ends by turning the whole story into an instruction to
  his own listeners - "we must lay the same foundation." The point of the story is not what happened to
  one young monk decades earlier but what any monk hearing it is now asked to build.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: >-
  So even in his early youth he already showed signs of the man he would become. Even as a boy, he drew
  the outline of the perfection that would grow in his adult years. If we want to reach his height of
  virtue, then we must lay the same foundation from the start.
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "He
then$"` returns line 43079 (among other unrelated hits elsewhere in the file); `grep -n "lay the same
foundation"` returns line 43083. Read with `sed -n '43079,43084p'`, from "He then in his early youth..."
through "...begin with." (the closing `</p></div4>` follows immediately).

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
