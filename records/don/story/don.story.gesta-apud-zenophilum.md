---
id: don.story.gesta-apud-zenophilum
world_id: donatism
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-P
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Documented, and unusually so for this corpus: a court transcript with named deponents,
    independently corroborated on its central fact by a second primary source written on the opposing side
    decades later with no evident coordination. The one thing that must not be forgotten is where the transcript
    survives - inside Optatus''s own appendix of documents. The proceeding''s record is not his composition,
    but the selection of it for preservation is his act, and it is preserved because its findings tell
    against us.'
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: Gesta apud Zenophilum (320); cic/texts/optatus_against-the-donatists.txt, lines 6194-6880, read
    directly for this record
  license: public-domain
- source_id: don.source.augustine-donatist-correspondence
  locus: Letter XLIII (397); cic/texts/npnf101_augustine-confessions-letters.xml, lines 28040-28069
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks for the most documentary and least narrated evidence we have - an actual transcript
    rather than a later account
  - participant asks whether the traditio-era financial disputes were ever formally investigated
  - participant wants a fact two independent sources agree on rather than one witness's word
  prefer_instead:
  - participant wants the earlier narrative of how the treasury dispute and the rival consecration arose
    - don.story.lucilla-affair is the origin and is best offered alongside this
  - participant is asking about the forgery investigation into Felix of Aptungi - don.story.acta-purgationis-felicis
    is a different proceeding six years earlier
relations:
- type: associated-with
  target: don.figure.silvanus-of-cirta
- type: associated-with
  target: don.figure.lucilla
- type: associated-with
  target: don.figure.purpurius
- type: associated-with
  target: don.figure.majorinus
- type: associated-with
  target: don.figure.optatus-of-milevis
- type: associated-with
  target: don.figure.augustine
narrative_tier: 1
narrative_tier_justification: 'Among the strongest Tier 1 candidates in this corpus, satisfying every element
  of the definition at its fullest: direct textual attestation in the form of a literal court transcript
  rather than a later narrative reconstruction; named participants with identifiable roles - a presiding
  consular official and a series of named deponents, including grave-diggers put on oath; a precise date,
  320; and a historically credible claim whose core fact is independently corroborated by a second primary
  source from the opposing side, decades later. The genre carries less interpretive distance than a narrated
  source does, so the caveats Tier 1 asks for the author''s perspective sit lighter here than on don.story.lucilla-affair,
  which is Optatus''s own narration of the same broader affair. They do not vanish: the transcript reaches
  us inside his appendix, and it is there because it damages us.'
tellable_as: A Roman official puts named witnesses on oath in 320 and asks where four hundred pieces of
  silver went - and the answers name the bishop of Cirta a betrayer and the rival altar at Carthage as
  what the money bought.
text: >-
  In 320, before the consular official Zenophilus, a formal inquiry was
  opened into what had actually happened to the church's own money.

  The complaint had been laid by Nundinarius, a deacon degraded by his
  own bishop, and it named names. Silvanus of Cirta, it charged, was a
  betrayer and a thief of the goods of the poor - and all of them, the
  bishops and priests and deacons and elders, knew it, because of the
  four hundred pieces of silver given by the noble woman Lucilla, for the
  sake of which they had conspired together that Majorinus should be made
  bishop, and out of which the schism came. Victor the fuller, it added,
  had paid twenty pieces to be made a priest.

  Letters were read into the record, and the letters are what a modern
  reader will find hardest. Purpurius, a bishop, had written to Silvanus
  urging him to settle with the deacon quietly, before the flame burst
  out that could not afterward be put out without spiritual bloodshed -
  and adding, in the same letter, that he knew the things written in the
  bill of accusation were true. He wrote to the clergy and elders of
  Cirta in the same terms, and closed by warning them to see that no one
  learned the story of this conspiracy. A bishop named Fortis wrote to
  Silvanus in the same vein: let us not come into a public court and be
  condemned by the gentiles. A bishop named Sabinus wrote twice. Every
  one of the letters ends the same way. Let no one know about it.

  Then the witnesses were questioned directly, under record. Zenophilus
  said that from the acts and letters read aloud it was clear that
  Silvanus was a betrayer, and turned to a deponent named Victor: say
  frankly whether you know he handed anything over. He handed it over,
  Victor said, but not in my presence. What office did he hold at the
  time? Sub-deacon, said Victor; the persecution broke out when Paul was
  bishop. And when he came to be made bishop, Nundinarius said, the
  people answered: let it be another - hear us, God. Did the people cry
  out that Silvanus was a betrayer? I myself fought against his being
  made bishop, Victor said. So you knew he was a betrayer - confess it.
  He was a betrayer, Victor said. We wanted one of our own townsmen, a
  man of integrity; I knew that if the office went to such as he, we
  should end up before the emperor's court.

  Decades afterward Augustine, no friend to our cause, referred back to
  this same episode in a letter of his own, recalling that Nundinarius,
  in the heat of passion, revealed many secrets - among them that the
  founding of a rival altar at Carthage had been made possible by money
  that came from Lucilla. Two witnesses, on opposite sides of the schism
  and decades apart, describe the same underlying fact.
absent_detail: Silvanus himself is questioned nowhere in what survives here; the proceeding is about him
  rather than with him, and no answer of his to any of it is on the record. Nor is there any account from
  our own side of what the money was for, what the seniors thought they were doing with it, or what Lucilla
  believed she was paying for.
modern_contrast: >-
  A modern reader may expect a founding document to be a creed. This one
  is a receipt - or an argument about a receipt. It is also the single
  most checkable thing in our whole record, and it does not flatter us:
  the letters read into it show bishops advising each other, in writing,
  to keep a matter out of court because the accusation was true. Being
  able to say that plainly, from a transcript, is worth more than a
  cleaner story would be.
---
Compiled from World-Builds/Donatism/Story-Chunks/donstory005_gesta-apud-
zenophilum.md (Doc_09 story index row donstory005, Tier 1). UNLIKE the
other eight compiled stories, this record's narrative text is NOT simply
the chunk's own text carried forward. The chunk narrates the proceeding
at one remove ("names given, questions asked, answers recorded") without
reproducing what was actually said. The vendored transcript was
therefore reopened directly at the chunk's own cited locus for this
record, cic/texts/optatus_against-the-donatists.txt lines 6194-6300, and
the accusation, the letters, and the examination of Victor were read and
narrated from the text itself. The specific sum, the named deponents,
and the Augustine corroboration are all as the chunk already had them.

SILVANUS OF CIRTA IS A REAL FIND OF THIS STEP, NOT AN INVENTION. He is
named nowhere in any of this world's nine construction documents, but he
is the central subject of the proceeding at the locus donstory005 itself
cites, and Purpurius's and Fortis's letters name him repeatedly. He gets
a figure record (don.figure.silvanus-of-cirta) on that basis - the
vendored primary text at an already-licensed locus - and the fact that
the construction documents never named him is stated on that record
rather than glossed over. This is the same pattern Doc_09 Section 9
item 1 already named for Axido and Fasir: content already inside the
licensed corpus, simply not yet read for this purpose.

NUNDINARIUS gets no figure record. He is the proceeding's own
complainant and is named here and in Augustine's Letter XLIII, but he is
a deacon appearing in one episode, and a figure record for him would
carry nothing this story does not already carry.

PAIRED WITH don.story.lucilla-affair, whose grievance this proceeding
investigates seven years later. Both retrieval blocks name the pairing.
