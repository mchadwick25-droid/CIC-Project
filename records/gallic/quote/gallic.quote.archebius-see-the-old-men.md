---
id: gallic.quote.archebius-see-the-old-men
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted at the narrative level: Cassian reports these as Archebius's own spoken words to
    him and Germanus, in a Conference composed in Gaul decades after the journey, in a literary dialogue
    form whose speeches are reconstructions. Archebius's words are Cassian's rendering of what he
    remembered, not a transcript; no independent witness to Archebius survives.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conferences XI.2 (npnf211 div iv.v.ii.ii, file lines 36825-36839): Archebius's reply when he heard the travelers wished to seek out the fathers in still remoter parts of Egypt"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what an old monk-bishop told visiting travelers about what he had lost by taking office"
  - "conversation reaches formation by named example, or the finding that mere sight of the old is itself a lesson"
  prefer_instead:
  - "participant wants Cassian's own description of Archebius rather than his speech - retrieve gallic.quote.archebius-carried-off-to-panephysis instead, or alongside"
text: >-
  "Come," said he, "see in the meanwhile the old men who live not far from our monastery, the length of whose service is
  shown by their bent bodies, as their holiness shines forth in their appearance, so that even the mere
  sight of them will give a great lesson to those who see them: and from them you can learn not so much
  by their words as by the actual example of their holy life, what I grieve that I have lost, and
  having lost cannot give to you. But I think that my poverty will be somewhat lessened by this zeal of
  mine, if when you are seeking that pearl of the Gospel which I have not, I at least provide where you
  can conveniently procure it.
speaker_or_author: "Bishop Archebius, as Cassian reports him (Conferences XI.2)"
license: verbatim
modern_lens_note: >-
  Archebius does not offer himself as the lesson; he points past himself. He calls what he has lost -
  the old men's kind of holiness - "that pearl of the Gospel which I have not," and offers, instead of
  his own teaching, only the sight of men who still have it. The office is framed here as a poverty he
  cannot undo, not a platform he uses.
modern_rendering: >-
  "Come," he said, "see, meanwhile, the old men who live not far from our monastery. Their bent bodies show how
  long they have served. Their holiness shines out in how they look. Even the mere sight of them will
  teach a great lesson to those who see them. From them you can learn what I grieve that I have lost.
  You will learn it less from their words than from the real example of their holy life. Having lost
  it, I cannot give it to you. But I think this eagerness of mine will ease my poverty a little. It
  will, if I at least show you where you can easily get that pearl of the Gospel. You are seeking it,
  and I do not have it.
relations:
- type: associated-with
  target: gallic.story.bishop-archebius
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml,
same paragraph as gallic.quote.archebius-carried-off-to-panephysis (`iv.v.ii.ii-p2`, lines 36825-36839).
Cassian's frame - "he then when he had received us kindly and most graciously in the aforesaid
Thennesus whither the business of electing a Bishop there had brought him, as soon as he heard of our
wish and desire to inquire of the holy fathers even in still more remote parts of Egypt: 'Come,' said
he," - falls between the two records and is left out here as narrator's prose and speech-tag, not
Archebius's own words. The quoted span is Archebius's reply verbatim and unbroken, "see in the meanwhile
the old men..." through "...conveniently procure it." (lines 36829-36839); the excerpt capitalizes
"See" at its own opening in place of the source's lower-case "see", which follows the dropped speech-tag
"said he,".

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
The source wraps the whole reply in curly double quotation marks (the edition's own speech-marking,
dropped, exactly as a quotation is lifted from a printed page). No word was added, dropped, substituted,
or reordered.

speaker_or_author is a plain string, not a figure id: no gallic.figure record exists for Archebius, and
none should be created for a figure fully carried by the one story he appears in.
