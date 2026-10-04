---
id: gallic.quote.sulpitius-on-the-secular-judge-in-an-ecclesiastical-cause
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-P
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Sulpitius's own words, in his own voice, in the Sacred History (not reported speech
    attributed to Martin, though it states Martin's position: "He maintained that..."). Widely Accepted
    at the narrative level - a related, distinct telling of a later phase of the same affair, the tribunes
    episode covered in gallic.quote.gallus-on-the-tribunes-for-the-spains, by the same author, not independent
    corroboration of it.
sources:
- source_id: gallic.source.sulpitius-sacred-history
  locus: "Sacred History II.50 (npnf211 div ii.vi.ii.l, file lines 11655-11660): Sulpitius's own statement of Martin's position on the trial of the Priscillianists at Treves"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Martin thought of the state judging a church matter, in Sulpitius's own words rather than the Dialogues' narrated scene"
  - "participant uses \"church and state\" or asks whether excommunication should have been enough"
  - "participant asks what Martin thought about secular rulers judging Church matters"
  - "participant asks why Martin opposed a state-run trial of the Priscillianists"
  prefer_instead:
  - "participant wants the fuller narrated scene at Treves, with the tribunes and the forced communion - retrieve gallic.quote.gallus-on-the-tribunes-for-the-spains or gallic.quote.gallus-on-the-forced-communion-and-the-angel"
text: >-
  He maintained that it was quite sufficient punishment that, having been declared heretics by a sentence
  of the bishops, they should have been expelled from the churches; and that it was, besides, a foul and
  unheard-of indignity, that a secular ruler should be judge in an ecclesiastical cause.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  Sulpitius states this as his own summary of Martin's position, not as a quotation of anything Martin
  said aloud. The claim has two parts, and only one is about mercy: expulsion from the churches is
  "quite sufficient punishment" for the charge of heresy itself, but the deeper objection is
  jurisdictional - it is "unheard-of" for a secular ruler to judge a church cause at all, regardless of
  the verdict. Martin's plea for the Priscillianists' lives and his objection to the emperor as judge are,
  in Sulpitius's telling, the same principle.
modern_rendering: >-
  He said the bishops had already declared them heretics. Being driven out of the churches, he held,
  was punishment enough. Besides, he said, it was a foul and unheard-of disgrace for a secular ruler to
  judge a church case.
relations:
- type: associated-with
  target: gallic.story.trier-and-the-ithacian-communion
- type: associated-with
  target: gallic.gravity.authority-ambivalence
use_note:
  means: "Sulpitius, in his own voice in the Sacred History, states Martin's position that expulsion sufficed for the heretics and that a secular judge in a church cause was unheard of."
  not_for:
    - "independent corroboration of the Dialogues' Treves account, when both come from the same author"
    - "a claim that Martin thought the condemned were not heretics"
    - "Martin's own direct words, when Sulpitius gives them in indirect speech"
    - "Martin's later petition at the palace, which sits in gallic.quote.gallus-on-the-tribunes-for-the-spains"
  years: {from: 397, to: 406}
  status: reviewed
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "quite sufficient punishment"`
returns one hit, line 11656. The chapter div is `<div4 title="Chapter L." ... prev="ii.vi.ii.xlix"
next="ii.vi.ii.li" id="ii.vi.ii.l">` (line 11634). The quoted span is `sed -n '11655,11660p'`, from "He
maintained that it was quite sufficient punishment..." through "...a secular ruler should be judge in an
ecclesiastical cause." Sulpitius's surrounding narration (Ithacius's character, the trial before Evodius,
Priscillian's execution) is left outside the `text` field as narrator's prose describing other matters,
not part of the stated principle.

Normalization: hard-wrapped lines joined with single spaces. No word was added, dropped, substituted, or
reordered.

speaker_or_author is gallic.figure.sulpitius: this is Sulpitius's own authorial statement, in his own
voice, of what Martin held - not reported speech in quotation marks in the source, and not converted to
the we-voice.
