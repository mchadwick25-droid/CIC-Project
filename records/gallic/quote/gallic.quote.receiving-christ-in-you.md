---
id: gallic.quote.receiving-christ-in-you
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- C-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes V.24, read at its locus for this record). The
    speaker is an unnamed elder of Egypt, and the setting is Egypt - Cassian and Germanus arriving
    from Palestine; this is Egypt's teaching received in Gaul, carried into a Gallic monk's cell by
    Cassian's book, and must always be named as the fathers' own (gallic.core.gallic caution 1).
    Whether any house in Gaul kept the fast broken for a guest, Cassian does not say.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes V.24 (npnf211 div iv.iii.v.xxiv, file lines 21017-21027): the elder's reply when asked why the daily fast was broken without scruple for the arriving guests"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Jesus would have wanted anything to do with someone like them, or how a stranger was received"
  - "participant asks about hospitality, guests, or when a fast could be broken"
  - "participant asks how this world saw Christ in other people"
  prefer_instead:
  - "participant is asking what a house in Gaul did with a guest - the setting here is Egypt, and Cassian records no Gallic instance"
text: >-
  The opportunity for fasting is always with me. But as I am going to
  conduct you on your way, I cannot always keep you with me. And a fast,
  although it is useful and advisable, is yet a free-will offering. But
  the exigencies of a command require the fulfilment of a work of
  charity. And so receiving Christ in you I ought to refresh Him but when
  I have sent you on your way I shall be able to balance the hospitality
  offered for His sake by a stricter fast on my own account. For 'the
  children of the bridegroom cannot fast while the bridegroom is with
  them:' but when he has departed, then they will rightly fast.
speaker_or_author: "one of the elders of Egypt, unnamed, as Cassian reports him (Institutes V.24)"
license: verbatim
modern_lens_note: >-
  A modern reader may take this as a rule about table manners: guests
  outrank diets. The elder is saying something harder. A fast is a gift a
  man chooses to give; charity is a command he is not free to skip. And
  the reason charity outranks the fast is not politeness - it is that the
  stranger at the door is Christ, so feeding him is feeding Christ. The
  elder does not ask who the traveller is or what he has done; "receiving
  Christ in you" is said of two men he has never met. The fast is not
  cancelled, only moved: he will make it up alone, afterwards, so that
  the guest never carries the cost of his host's devotion.
modern_rendering: >-
  I can fast any day. But I am about to walk you on your way, and I will
  not have you with me for long. A fast is good and worth doing, but it is
  a gift I choose to give. Charity is a command, and a command has to be
  carried out. So since I receive Christ in you, I ought to feed him. Once
  I have sent you on, I can make up for the welcome I gave for his sake by
  fasting more strictly on my own. As the Lord said, the bridegroom's
  friends cannot fast while the bridegroom is with them. Once he has gone,
  then they will rightly fast.
relations:
- type: associated-with
  target: gallic.dw.christ-in-the-beggar-and-the-guest
- type: associated-with
  target: gallic.dw.the-christ-who-bears-the-wounds
use_note:
  means: "An unnamed Egyptian elder, in Cassian's Institutes, explains breaking his fast for guests because receiving Christ in them commands charity, and he will fast afterwards."
  not_for:
    - "evidence that Gallic houses broke fasts for guests, which Cassian does not say"
    - "a Gallic teaching rather than Egypt's, received through Cassian's book"
    - "Christ shown in the beggar at Amiens, which sits in gallic.quote.the-cloak-divided-and-the-vision-of-christ"
  years: {from: 415, to: 426}
  status: reviewed
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between
B-7 and B-8) directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
-i "receiving Christ"` returns one hit, line 21021 ("charity. And so
receiving Christ in you I ought to refresh Him but when"). The chapter div
is `<div4 title="Chapter XXIV. How in Egypt we saw that the daily fast was
broken without scruple on our arrival." ... id="iv.iii.v.xxiv">` (line
20980). The quoted span is the elder's whole reply, `sed -n '21017,21027p'`,
opening after Cassian's frame ("one of the elders replied:", line 21016)
at "The opportunity for fasting is always with me." (line 21017) and
closing at "then they will rightly fast." (line 21027); "on my own
account." falls at line 21023. Cassian's own frame - the arrival from Syria into Egypt,
the astonishment at the fast broken, the question put to the elder - is
left outside the `text` field as narrator's prose and is summarized in
the locus above.

Normalization: hard-wrapped lines joined with single spaces; the source's
double space after "account." normalized to one. The edition wraps the
whole reply in curly double quotation marks (dropped, as the edition's
speech-marking) and sets the scripture clause in curly single quotation
marks (kept, as plain single quotation marks, because they mark the
elder's own citation inside his speech). Endnote 866 (S. Matt. ix. 15;
"The Latin has sponsus in each clause"), attached after the scripture
clause, is publisher's apparatus and is dropped; endnotes 864 and 865
belong to Cassian's frame, not to the quoted span. No word was added,
dropped, substituted, or reordered.

This is the passage gallic.voice.craft's own gap note named as "the
natural ground for any future C-cell answer this world can honestly give"
and recorded as having no term, story, or doctrinal_witness record behind
it anywhere in this world's store; it is also already compiled as
standing instruction in the approved Doc_10 prompt ("the fast broken for
a guest, because receiving Christ in the guest we ought to refresh Him")
and named at Doc_09 Section 6 item 5 as ecology rather than story. This
record gives it its first record of its own. Ground for
gallic.dw.christ-in-the-beggar-and-the-guest (the guest received as
Christ, without being asked who he is) and for
gallic.dw.the-christ-who-bears-the-wounds (Christ met in the poor and the
guest); reciprocal associated-with declared on both.

speaker_or_author is a plain string, not a figure id: the speaker is an
unnamed Egyptian elder, and no figure record exists or should exist for
him. The attribution is kept exactly as Cassian gives it - "one of the
elders" - so that the voice names whose story this is, per the reception
discipline.
