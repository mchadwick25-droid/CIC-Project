---
id: gallic.quote.paphnutius-accused-and-the-book-found
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
    Widely Accepted as Piamun's own telling (Conferences XVIII.15). The wording is Documented at its
    locus; the accusation, the astonishment of the community, and the search are the tradition's own
    narration of events decades before the telling.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43018-43039): the accuser's complaint
    to S. Isidore; the community's astonishment; the search of the cells by three Elders; the book found
    in Paphnutius's cell among the palm boughs"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks who accused Paphnutius, or how the desert searched and found the hidden book"
  - "participant asks how a false accusation could look convincing to a whole community"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.paphnutius-and-the-hidden-book"
text: >-
  And when the whole service was ended as usual, in the presence of all the brethren he brought his
  complaint to S. Isidore who was Presbyter of this desert before this same Paphnutius, and declared that
  his book had been stolen from his cell. And when his complaint had so disturbed the minds of all the
  brethren, and more especially of the Presbyter, so that they knew not what first to suspect or think,
  as all were overcome with the utmost astonishment at so new and unheard of a crime, such as no one
  remembered ever to have been committed in that desert before that time, and which has never happened
  since, he who had brought forward the matter as the accuser urged that they should all be kept in
  Church and certain selected men be sent to search the cells of the brethren one by one. And when this
  had been entrusted to three of the Elders by the Presbyter, they turned over the bed-chambers of them
  all, and at last found the book hidden in the cell of Paphnutius among the boughs of the palms which
  they call σειρά, just as the plotter had hidden it.
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  The accuser is the one who proposes the search - the tradition lets him engineer his own cover, and the
  community's shock ("so new and unheard of a crime") measures how well the plan worked. Nothing in the
  passage lets Paphnutius speak yet; the book is found, and the story moves straight to what he does next.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: >-
  When the whole service had ended as usual, he made his complaint to Saint Isidore in
  front of all the brothers. Isidore was the priest of this desert before Paphnutius himself. The man declared that his
  book had been stolen from his cell. His complaint deeply troubled all the brothers, and the priest
  most of all. They did not know what to suspect or think first. Everyone was utterly astonished at so
  new and unheard-of a crime. No one remembered such a thing ever happening in that desert before, and
  it has never happened since. Then the man who had raised the matter as accuser made a proposal.
  Everyone should be kept in the church, and chosen men should be sent to search the brothers' cells one
  by one. The priest gave this task to three of the Elders. They turned over everyone's sleeping
  quarters. At last they found the book hidden in Paphnutius's cell, among the palm branches they call
  seira. It was just where the plotter had hidden it.
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "And
when the whole service"` returns line 43018; `grep -n "just as the plotter"` returns line 43038, `grep -n
"And when the inquisitors"` returns line 43039 (the sentence immediately following, outside this quote's
close). Read with `sed -n '43018,43039p'`.

Normalization: line breaks joined with single spaces. The endnote anchor after "S. Isidore" (n="2091",
Gazet's identification note) sits inside the source's own prose and is dropped, exactly like any other
in-line note anchor. The Greek word for the palm boughs, σειρά, is given in the source itself (marked as
Greek text) and is kept verbatim rather than transliterated or paraphrased. No word was added, dropped,
substituted, or reordered.
