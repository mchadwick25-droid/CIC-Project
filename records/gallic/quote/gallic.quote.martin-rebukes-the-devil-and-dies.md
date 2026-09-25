---
id: gallic.quote.martin-rebukes-the-devil-and-dies
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
  formation_confidence: Contested
  divergence_note: >-
    The wording is Documented as Sulpitius's own text. The event itself - the devil standing at the
    bedside, Martin's face afterward "as if it had been the face of an angel," his limbs "white as
    snow" - is carried by Sulpitius as report: "those who were there present have testified to us."
    Contested at the level of the narrated event, since Sulpitius discloses he was not present and
    relies entirely on others' testimony for it; the words themselves are Documented as what the letter
    claims those witnesses reported.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2474-2484): Martin''s rebuke of the devil at his bedside, his death, and the witnesses'' report of his face and limbs'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how Martin died, or what happened at the very end
  - participant asks about the devil, temptation at death, or how this world understood a contested death
  - conversation reaches what witnesses claimed to see, versus what is reported as plain fact
  prefer_instead:
  - participant wants the community's response before this final moment - retrieve
    gallic.quote.martin-disciples-plea-and-his-reply
  - participant is asking whether the devil "really" appeared - this record carries the words the letter
    reports, not an assessment of the event
text: >-
  Why do you stand here, thou bloody monster? Thou shalt find nothing in me, thou deadly one: Abraham's
  bosom is about to receive me.” As he uttered these words, his spirit fled; and those who were there
  present have testified to us that they saw his face as if it had been the face of an angel. His
  limbs too appeared white as snow, so that people exclaimed, "Who would ever believe that man to be
  clothed in sackcloth, or who would imagine that he was enveloped with ashes?"
speaker_or_author: "Martin, with the witnesses' report as Sulpitius carries it"
license: verbatim
modern_lens_note: >-
  Martin's last words are not fear but defiance - he names the devil plainly and states his own
  confidence flatly, "thou shalt find nothing in me." What follows is not Martin's claim but the
  onlookers': a transformed face and skin. Sulpitius keeps the two distinct - Martin's own words, then
  what others say they saw - even while presenting both as part of one continuous scene.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
modern_rendering: >-
  Why are you standing here, you bloodthirsty monster? You will find nothing in me, deadly one.
  Abraham's bosom is about to receive me. As he spoke these words, his spirit left him. Those who
  were there have told us that they saw his face as if it were the face of an angel. His limbs, too,
  looked as white as snow. So people cried out, "Who would ever believe this man had been dressed in
  sackcloth? Who would imagine he had been wrapped in ashes?"
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"Abraham's bosom is about to receive me"` returns line 2476; `grep -n "enveloped with ashes"` returns
line 2484. Read in full at lines 2473-2484: Martin's rebuke closes one paragraph (`<p
id="ii.iii.iii-p20">` … ending line 2476) and the report of his death and appearance opens the next
(`<p id="ii.iii.iii-p21">`, line 2478) with no material omitted between them - "As he uttered these
words, his spirit fled" follows the rebuke directly - so the two are carried as one continuous
quotation across the paragraph break, not as separate fragments.

The host record's own current wording of the devil rebuke and the witnesses' testimony matches the
source exactly; verified independently rather than trusted on that basis. No word was added, dropped,
substituted, or reordered; hard line wraps were joined with single spaces, and the edition's own curly
quotation marks are dropped as the edition's own punctuation, except where they mark the onlookers'
own exclamation ("Who would ever believe...") which is retained as reported speech within the passage,
matching how the source itself nests it.

speaker_or_author names both Martin and the witnesses' report since the excerpt carries Martin's own
attributed words followed immediately by testimony Sulpitius attributes to unnamed others present at
the death.
