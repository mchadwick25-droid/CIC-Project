---
id: gallic.quote.germanus-and-chaeremon-on-the-husbandman
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conferences XIII.2-3, read at its locus for this record). Widely
    Accepted as Cassian's report of Germanus's and Chaeremon's exchange; the doctrinal content of
    Chaeremon's answer is Contested [CT] for its meaning relative to Augustine and for the fairness of
    the label "semi-Pelagian" (gallic.term.grace, gallic.term.free-will) - a dispute this record neither
    depends on nor resolves. The extended speeches are Cassian's literary composition of what he heard,
    decades later, not a transcript.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conferences XIII.2-3 (npnf211 divs iv.v.iv.ii-iii, file lines 37515-37582): Germanus's objection that effort ought to earn its own reward, and Chaeremon's answer using the husbandman and the rains"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what the grace-and-effort argument actually said, or wants the husbandman analogy"
  - "participant uses \"free will,\" \"grace,\" \"effort,\" or \"does it matter what I do\""
  - "conversation reaches whether human striving earns anything, or where a good will comes from"
  prefer_instead:
  - "participant wants the doctrine argued at full theological depth - retrieve gallic.term.grace, gallic.term.free-will, gallic.term.beginning-of-a-good-will (all [CT])"
  - "participant wants the two later summary statements from further on in the same Conference - retrieve gallic.quote.chaeremon-on-grace-and-free-will"
text: >-
  Then Germanus: ... it seems to us absurd for the reward of our efforts, i.e., perfect chastity, which
  is gained by the earnestness of one's own toil, not to be ascribed chiefly to the exertions of the man
  who makes the effort. For it is foolish, if, when for example, we see a husbandman taking the utmost
  pains over the cultivation of the ground, we do not ascribe the fruits to his exertions.

  Chaeremon: ... Neither can the husbandman, when he has spent the utmost pains in cultivating the
  ground, forthwith ascribe the produce of the crops and the rich fruits to his own exertions, as he
  finds that these are often in vain unless opportune rains and a quiet and calm winter aids them ... As
  then the Divine goodness does not grant these rich crops to idle husbandmen who do not till their
  fields by frequent ploughing ... For a man should consider and with a most careful scrutiny weigh the
  fact that he could not by his own strength apply those very efforts which he has earnestly used in his
  desire for wealth, unless the Lord's protection and pity had given him strength for the performance of
  all agricultural labours ... From which we clearly infer that the initiative not only of our actions
  but also of good thoughts comes from God, who inspires us with a good will to begin with, and supplies
  us with the opportunity of carrying out what we rightly desire ... But it is for us, humbly to follow
  day by day the grace of God which is drawing us.
speaker_or_author: "Germanus and Abbot Chaeremon, as Cassian records their exchange (Conference XIII.2-3)"
license: verbatim
modern_lens_note: >-
  Chaeremon does not deny the husbandman's labor; he turns it around. A farmer's effort is real, but it
  cannot alone make the rain fall or the winter mild, and "the Divine goodness does not grant these rich
  crops to idle husbandmen" either - both halves are held at once. The conclusion he draws is not that
  effort is pointless but that its starting point, "the initiative," is not the man's own: he is called
  to "humbly follow day by day," not to originate the grace he follows.
modern_rendering: >-
  Then Germanus: ... The reward of our efforts is perfect chastity, gained by the earnestness of one's
  own toil. It seems absurd to us not to credit it mainly to the labor of the man who makes the effort.
  For it is foolish, when we see a farmer, for example, taking the greatest pains to work the ground, not
  to credit the fruits to his labor.

  Chaeremon: ... Neither can the farmer who has taken the greatest pains to work the ground at once
  credit the yield of his crops and their rich fruits to his own labor. He finds that his efforts often
  come to nothing unless timely rains and a quiet, calm winter help them ... Just as God's goodness, then,
  does not grant these rich crops to lazy farmers who do not work their fields with frequent ploughing
  ... For a man should think this over and weigh it with the greatest care. By his own strength he could
  not have made the very efforts he put in so earnestly out of his desire for wealth. He could have made
  them only if the Lord's protection and mercy had given him strength for all the work of farming ...
  From this we clearly conclude that the beginning, not only of our actions but also of our good
  thoughts, comes from God. He puts a good will in us to begin with. He gives us the chance to carry out
  what we rightly desire ... But our part is to follow humbly, day by day, the grace of God that is
  drawing us.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. Germanus's chapter is `<div4 title="Chapter
II..." ... id="iv.v.iv.ii">` (line 37508); `grep -n "Then Germanus"` returns line 37515. Chaeremon's
chapter is `<div4 title="Chapter III..." ... id="iv.v.iv.iii">` (line 37527); `grep -n "Chæremon:"` returns
line 37534. `grep -n "humbly to follow day by day"` returns line 37582, the close of this record's span.

The `text` field keeps Germanus's objection (lines 37515-37524, opening at "it seems to us absurd," his
own preceding clause about "last night's discussion" left out as connective framing already carried in
gallic.quote.germanus-troubled-after-the-nights-teaching) and four sentences of Chaeremon's answer (lines
37534-37582), joined by ellipses at the points where the source's own material is skipped: a restatement
of the husbandman point (lines 37541-37544, "so that we have often seen fruits..."), a clause on human
pride not claiming credit for grace (lines 37547-37552), the run from "for the performance of all
agricultural labours" through a string of Scripture citations on rain and harvest (lines 37556-37567), and
a Scripture citation on "every good gift" between the initiative clause and the final sentence (lines
37575-37581). None of the skipped material is flagged content; each ellipsis marks a real omission, and
no word was added, changed, or reordered within what is kept. "Neither" (opening Chaeremon's quoted
sentence) is capitalized here as the first word of the extracted quote; the source reads "For neither,"
mid-sentence.

speaker_or_author names both speakers because the record is their exchange, not one man's statement: the
whole point Chaeremon makes only stands as an answer to Germanus's own objection.
