---
id: gallic.quote.paphnutius-the-thief-possessed-and-healed
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
    Widely Accepted for the wording, Documented at its locus (Conferences XVIII.15). Contested for the
    narrated event: the accuser's possession and its cure are the tradition's own supernatural claims,
    offered by a narrator (Piamun) reporting events of Paphnutius's youth at second hand, decades before
    the telling. This record carries Piamun's words as the tradition's own account of vindication, not an
    independent assessment that a possession and a reserved cure occurred.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43058-43079): the accuser possessed
    by a demon and confessing his own plot; Isidore's healing gift unable to cure him; the cure reserved
    for Paphnutius's own prayers"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how Paphnutius was vindicated, or why the cure was reserved for him and no one else"
  - "participant asks about possession, exorcism, or a saint's healing gift inside this story specifically"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.paphnutius-and-the-hidden-book"
  - "participant is asking about exorcism as a practice generally - retrieve gallic.term.possessed-exorcism"
text: >-
  He, Who is the witness of all secret things and knows them, suffered him to be no longer tried by
  Himself or defamed by others. For what the author of the crime, the wicked thief of his own property,
  the cunning defamer of another's credit, had done with no man there as a witness, that He made known by
  means of the devil who was himself the instigator of the sin. For possessed by a most fierce demon, he
  made known all the craft of his secret plot, and the same man who had conceived the accusation and the
  cheat betrayed it. But he was so long and grievously vexed by that unclean spirit that he could not
  even be restored by the prayers of the saints living there, who by means of divine gifts can command
  the devils, nor could the special grace of the Presbyter Isidore himself cast out from him his cruel
  tormentor, though by the Lord's bounty such power was given him that no one who was possessed was ever
  brought to his doors without being at once healed; for Christ was reserving this glory for the young
  Paphnutius, that the man should be cleansed only by the prayers of him against whom he had plotted, and
  that the jealous enemy should receive pardon for his offence and an end of his present punishment, only
  by proclaiming his name, from whose credit he had thought that he could detract.
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  The tradition is careful about who cannot cure the accuser: not the saints of the desert generally, not
  even Isidore, whose gift the passage says had never failed before. That failure is the point - the cure
  is "reserved," withheld from every other possible healer so that only Paphnutius's own prayers, prayed
  for the man who wronged him, could free his accuser. Vindication here is not a punishment on the guilty
  man; it is a healing only the wronged man can give.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: PENDING_OPUS_RENDERING
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "He,
Who is the witness"` returns line 43058; `grep -n "from whose credit he had thought"` returns line
43079, ending "...he could detract." immediately before "He then" (also line 43079), which opens the
closing-moral quote (its own record). Read with `sed -n '43058,43079p'`.

Normalization: the source splits the word "no longer" across a page break (`<pb n="487" .../>`) between
"suffered him to be no" and "longer / tried by Himself"; the two halves are joined into "no longer" with
a single space, matching the printed prose, not the page-break artifact. Line breaks elsewhere joined
with single spaces. The source's curly apostrophes ("another's", "Lord's") are kept as in the source. No
word was added, dropped, substituted, or reordered.
