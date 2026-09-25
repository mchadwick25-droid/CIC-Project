---
id: gallic.quote.cassian-adapts-egypt-to-gaul
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
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes Preface, read at its locus for this record) - his
    own stated method for adapting the Egyptian rule to Gaul, load-bearing for the south's own
    receptive-with-adaptation mode.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Preface (npnf211 div iv.ii, file lines 16515-16534): Cassian's own method - follow the
    ancient Egyptian rule rather than any individual founder's own fancy, adapting only where
    climate or circumstance in Gaul makes the letter of it impossible"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Cassian decided what to keep and what to change from Egyptian practice"
  - "participant asks whether Gallic monasticism was Egypt copied exactly, or Egypt adapted"
  prefer_instead:
  - "participant wants the original request this method answers - retrieve gallic.quote.castor-anxious-for-egyptian-institutions"
text: >-
  In this, too, I will try to satisfy your directions, so that, if I
  happen to find that anything has been either withdrawn or added in
  those countries not in accordance with the example of the elders
  established by ancient custom, but according to the fancy of any one
  who has founded a monastery, I will faithfully add it or omit it, in
  accordance with the rule which I have seen followed in the
  monasteries anciently founded throughout Egypt and Palestine, as I do
  not believe that a new establishment in the West, in the parts of
  Gaul could find anything more reasonable or more perfect than are
  those customs, in the observance of which the monasteries that have
  been founded by holy and spiritually minded fathers since the rise of
  apostolic preaching endure even to our own times. I shall, however,
  venture to exercise this discretion in my work,—that where I find
  anything in the rule of the Egyptians which, either because of the
  severity of the climate, or owing to some difficulty or diversity of
  habits, is impossible in these countries, or hard and difficult, I
  shall to some extent balance it by the customs of the monasteries
  which are found throughout Pontus and Mesopotamia; because, if due
  regard be paid to what things are possible, there is the same
  perfection in the observance although the power may be unequal.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This is a method, not a slogan: Cassian will correct any local practice that departs from the
  ancient Egyptian rule out of one founder's own preference, but he also allows real adaptation
  where Gaul's own climate makes the Egyptian letter genuinely impossible - substituting Pontic and
  Mesopotamian custom in those specific cases, not inventing a Gallic rule of his own.
modern_rendering: >-
  In this, too, I will try to satisfy your directions. To that end, suppose I happen to find that
  something in those countries has been either taken away or added. And suppose the change does
  not follow the example of the elders, set by ancient custom, but the whim of whoever founded a
  monastery. Then I will faithfully add it or leave it out. I will do so by the rule I have seen
  kept in the monasteries founded long ago throughout Egypt and Palestine. For I do not believe a
  new foundation in the West, in Gaul, could find anything more reasonable or more perfect than
  those customs. The monasteries founded by holy and spiritually minded fathers since the
  apostles first preached keep those customs. In keeping them, they have lasted even to our own
  time. In my work, however, I will venture to use my own judgment in this way. I may find
  something in the rule of the Egyptians that is impossible in these countries, or hard and
  difficult. The cause may be the harsh climate, or some difficulty or difference in habits. In
  that case, I will balance it to some extent with the customs of the monasteries found
  throughout Pontus and Mesopotamia. For if we take proper account of what is possible, keeping
  the rule is just as perfect, though strength may be unequal.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"fancy of any one who has founded"` returns line 16519; `grep -n "power may be unequal"` returns a
hit at line 16535. Read with `sed -n '16515,16535p'`, inside the Institutes Preface. The two
sentences quoted here ("In this, too..." through "...even to our own times." and "I shall,
however..." through "...power may be unequal.") are immediately adjacent in the source, with no
intervening text; this record carries them together as the one continuous passage they are, rather
than as two separate records joined by an ellipsis.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.