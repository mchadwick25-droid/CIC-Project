---
id: gallic.quote.martin-if-christ-bore-with-judas
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
    Widely Accepted and Documented at its locus (Dialogues III.15). Martin's saying is reported as
    something he "often repeated" over a pattern of later accusations against Brictio, by a named
    disciple-narrator speaking of his own household - the wording is well attested at the narrative level;
    what nothing at the locus confirms is anything about Brictio's later career or status, a limit the
    host record's own claim_guards already name.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.15 (npnf211 div ii.iv.iii.xv, file lines 5330-5339): Martin's explanation that he
    had seen Brictio driven by demons and was not moved by his reproaches; Martin's refusal to remove
    Brictio from the presbyterate despite repeated accusations, and his repeated saying, 'If Christ bore
    with Judas, why should not I bear with Brictio?'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Martin kept Brictio in office despite repeated accusations"
  - "participant asks what Martin actually said about bearing with a difficult man, or wants the saying itself"
  - "conversation reaches forgiveness, patience with a wrongdoer, or refusing to use authority to settle a personal injury"
  prefer_instead:
  - "participant wants the whole story first - retrieve gallic.story.brictio-in-the-courtyard"
text: >-
  And then the holy man explained both to him and to us all, how he had seen him driven on by demons, and
  declared that he was not moved by the reproaches which had been heaped upon him; for they had, in fact,
  rather injured the man who uttered them. And subsequently, when this same Brictio was often accused
  before him of many and great crimes, Martin could not be induced to remove him from the presbyterate,
  lest he should be suspected of revenging the injury done to himself, while he often repeated this
  saying: ‘If Christ bore with Judas, why should not I bear with Brictio?’
speaker_or_author: "Gallus, narrating; the closing saying is quoted as Martin's own repeated words"
license: verbatim
modern_lens_note: >-
  Martin gives his own reason for staying his hand, and it is not mercy in the abstract: he will not use
  his office to settle a wrong done to himself personally, "lest he should be suspected of revenging the
  injury." The saying that follows measures Brictio against the worst betrayal the tradition knows -
  Judas - and still chooses to bear with him, not because the charges were false, but because bearing
  with a wrongdoer, not removing him, is what the saying claims Christ himself did first.
relations:
- type: associated-with
  target: gallic.story.brictio-in-the-courtyard
modern_rendering: >-
  Then the holy man explained, both to him and to all of us, how he had seen demons driving him on. He
  declared that the insults heaped on him did not move him. In fact, they had hurt the man who spoke
  them instead. Later, this same Brictio was often accused before Martin of many serious crimes. Yet
  Martin could not be persuaded to remove him from the priesthood. He did not want to be suspected of
  taking revenge for the wrong done to himself. And he often repeated this saying: ‘If Christ bore with
  Judas, why should I not bear with Brictio?’
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "And
then the holy man explained"` returns line 5330; `grep -n "Brictio?"` returns line 5339, the chapter's
closing line (`Brictio?'"</p>`, immediately followed by `</div4>`). Read with `sed -n '5330,5339p'`.

Normalization: line breaks joined with single spaces. The source's outer double curly quotation mark
closing the whole chapter (Gallus's reported speech) is dropped, as at this quote's start; the single
curly quotes around Martin's own saying, ‘If Christ bore with Judas, why should not I bear with
Brictio?’, are kept, since that is direct speech quoted inside Gallus's narration. No word was added,
dropped, substituted, or reordered.

speaker_or_author records both layers: the paragraph is Gallus's own narration, but its closing sentence
attributes the saying itself directly to Martin ("he often repeated this saying"), so the field notes
both rather than collapsing the two into one name.
