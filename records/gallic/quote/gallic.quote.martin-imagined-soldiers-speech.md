---
id: gallic.quote.martin-imagined-soldiers-speech
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own composition, not as Martin's verbatim words: Sulpitius introduces it
    himself as his own rhetorical expansion of the one sentence Martin actually said ("Do you not think
    you hear him speaking in the following few words which I repeat?"). It is carried here as the
    author's own soldier's-speech idiom for what he believed Martin's one recorded prayer meant, not as
    an independent report of anything Martin said aloud.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2438-2453): Sulpitius''s own rhetorical expansion of Martin''s prayer, cast in a soldier''s idiom'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what "soldier of Christ" meant in practice, or wants the fullest statement of it in this letter
  - participant asks why Martin's death scene sounds like a veteran's speech about serving until discharged
  prefer_instead:
  - participant wants Martin's own one recorded sentence, not Sulpitius's expansion of it - retrieve
    gallic.quote.martin-disciples-plea-and-his-reply, which carries "O Lord, if I am still necessary..."
  - participant is asking whether Martin literally said these words - he did not; Sulpitius says so himself
text: >-
  Terrible, indeed, Lord, is the struggle of bodily warfare, and surely it is now enough that I have
  continued the fight till now; but, if thou dost command me still to persevere in the same toil for
  the defense of thy flock, I do not refuse, nor do I plead against such an appointment my declining
  years. Wholly given to thee, I will fulfill whatever duties thou dost assign me, and I will serve
  under thy standard as long as thou shalt prescribe. Yea, although release is sweet to an old man
  after lengthened toil, yet my mind is a conqueror over my years, and I have no desire to yield to old
  age. But if now thou art merciful to my many years, good, O Lord, is thy will to me; and thou thyself
  wilt guard over those for whose safety I fear.
speaker_or_author: Sulpitius Severus, speaking in Martin's voice
license: verbatim
modern_lens_note: >-
  Sulpitius is explicit that this is his own gloss, not a transcript - he asks Bassula to hear it as
  what Martin's silence "sounded like," not as a quotation. The idiom he reaches for is military
  service: continuing the fight, serving under a standard, being released from duty rather than simply
  dying. It is the clearest statement in the letter of Martin's death as a soldier's discharge, not a
  patient's release.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.sulpitius
modern_rendering: >-
  Lord, the struggle of bodily warfare is fearsome indeed. Surely it is enough by now that I have
  kept up the fight this long. But if you command me to go on in the same labor to defend your
  flock, I do not refuse. Nor do I plead my failing years against such a post. I am wholly given to
  you. I will carry out whatever duties you assign me. I will serve under your banner for as long as
  you direct. Yes, release is sweet to an old man after long labor. Yet my mind has conquered my
  years, and I have no wish to give in to old age. But if you now take pity on my many years, your
  will for me is good, O Lord. You yourself will guard those whose safety I fear for.
use_note:
  means: "Sulpitius, in Letter III, composes a soldier's prayer in Martin's voice to express what Martin's dying words meant, and presents it as his own expansion."
  not_for:
    - "Martin's own recorded words, when Sulpitius frames the speech as his own composition"
    - "the disciples' plea and Martin's actual reply at his death, which sit in gallic.quote.martin-disciples-plea-and-his-reply"
    - "evidence that Martin called himself a soldier on his deathbed"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"Terrible, indeed, Lord, is the struggle"` returns line 2438; `grep -n "guard over those for whose
safety I fear"` returns line 2453. Read in full at lines 2437-2453: one continuous speech, immediately
following Sulpitius's own framing sentence, "Do you not think you hear him speaking in the following
few words which I repeat?" (line 2437-2438), which is left outside the `text` field as the narrator's
own introduction, not part of the spoken content itself.

The host record's own current wording opens mid-sentence ("surely it is now enough...") and elides
"nor do I plead against such an appointment my declining years. Wholly given to thee, I will fulfill
whatever duties thou dost assign me, and" with an ellipsis; this record carries the complete speech
verbatim from its actual opening clause through its close, per the source. No word was added, dropped,
substituted, or reordered; hard line wraps were joined with single spaces, and the edition's own curly
quotation marks are dropped as its own punctuation.

speaker_or_author is given as "Sulpitius Severus, speaking in Martin's voice," not gallic.figure.martin:
the source itself distinguishes this passage from Martin's own attested words, so attributing it to
Martin directly would misstate what the letter claims.
