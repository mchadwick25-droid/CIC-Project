---
id: gallic.quote.brictio-tirade-and-martins-restraint
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted and Documented at its locus (Dialogues III.15). Sulpitius's and Gallus's hostility to
    Brictio is their own perspective - his tirade is reported by men against him, and his own side is not
    heard, per the host record's own narrative-tier finding.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.15 (npnf211 div ii.iv.iii.xv, file lines 5305-5319): Brictio's onset on Martin,
    Martin's placid restraint, and Brictio's tirade calling Martin's visions 'ridiculous fancies'"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what Brictio actually said against Martin, or wants his own words as Gallus reports them"
  - "participant asks how Martin responded in the moment, before the demon was named as the cause"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.brictio-in-the-courtyard"
text: >-
  The miserable man, moved with bitter rage on account of these things, and, as I believe, chiefly
  instigated by the impulse received from those demons, made such an onset upon Martin as scarcely to
  refrain from laying hands upon him. The holy man, on his part, with a placid countenance and a
  tranquil mind, endeavored by gentle words to restrain the madness of the unhappy wretch. But the spirit
  of wickedness so prevailed within him, that not even his own mind, at best a very vain one, was under
  his control. With trembling lips, and a changing countenance, pale with rage, he rolled forth the words
  of sin, asserting that he was a holier man than Martin who had brought him up, inasmuch as from his
  earliest years he had grown up in the monastery amid the sacred institutions of the Church, while
  Martin had at first, as he could not deny, been tarnished with the life of a soldier, and had now
  entirely sunk into dotage by means of his baseless superstitions, and ridiculous fancies about visions.
speaker_or_author: "Gallus, as Sulpitius Severus records his account in the Dialogues"
license: verbatim
modern_lens_note: >-
  Gallus gives Brictio's own reasoning for calling himself the holier man - raised inside the Church from
  boyhood, against Martin's years as a soldier before he converted. It is a real argument, not mere abuse,
  and Gallus reports it before he reports Martin's silence in response: the holy man answers rage with
  gentleness, not with a counter-argument.
relations:
- type: associated-with
  target: gallic.story.brictio-in-the-courtyard
modern_rendering: >-
  These things filled the wretched man with bitter rage. And, I believe, the urging of those demons
  drove him most of all. He attacked Martin so fiercely that he barely held back from striking him. The
  holy man, for his part, kept a calm face and a peaceful mind. With gentle words he tried to hold back
  the unhappy man's madness. But the spirit of evil had such a grip on him that he could not control
  even his own mind. That mind was a very foolish one even at the best of times. His lips trembled, and
  his face changed, pale with rage. He poured out sinful words. He claimed he was a holier man than
  Martin, who had raised him. From his earliest years, he said, he had grown up in the monastery,
  trained in the Church's holy ways. Martin, he said, had first been stained by a soldier's life, as
  Martin could not deny. And now, he said, Martin had sunk completely into old age's foolishness. His
  groundless superstitions and ridiculous fancies about visions had brought him to it.
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "The
miserable man, moved with bitter rage"` returns line 5305; `grep -n "ridiculous fancies about visions"`
returns line 5319. Read with `sed -n '5305,5319p'`.

Normalization: line breaks joined with single spaces. Source order preserved exactly: the "placid
countenance" restraint (Martin's response to the near-laying-on-of-hands) precedes the "trembling
lips"/"rolled forth the words of sin" tirade in the source itself, and that order is kept here even
though the host record's own paraphrase currently presents them in the reverse sequence - the quote
record uses the source's actual order. No word was added, dropped, substituted, or reordered.
