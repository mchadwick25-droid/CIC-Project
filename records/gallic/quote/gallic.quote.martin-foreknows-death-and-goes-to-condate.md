---
id: gallic.quote.martin-foreknows-death-and-goes-to-condate
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own narration in Letter III. The claim it carries - that
    Martin foreknew the timing of his own death, and chose the Condate journey with that knowledge -
    rests on Sulpitius's own authority alone; the letter's own opening tells Bassula to ask "those who
    were present" for anything beyond what Sulpitius personally knows. Carried as Widely Accepted: a
    named author's contemporary claim, not independently corroborated, but not the letter's more
    fantastical register either.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2379-2392): Martin''s foreknowledge of his death and his decision to travel to the quarrelling church at Condate'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks whether Martin knew he was dying, or why he took on the Condate journey so near the end
  - conversation reaches choosing costly duty with the cost already known, rather than duty that overtakes someone by surprise
  prefer_instead:
  - participant wants the deathbed scene itself, not the journey that preceded it - retrieve gallic.quote.martin-disciples-plea-and-his-reply
  - participant is asking about Condate's own later history, not this one visit - outside our window and evidence
text: >-
  I have to state, then, that Martin was aware of the period of his own death long before it occurred,
  and told the brethren that his departure from the body was at hand. In the meantime, a reason sprang
  up which led him to visit the church at Condate. For, as the clerics of that church were at variance
  among themselves, Martin, wishing to restore peace, although he well knew that the end of his own
  days was at hand, yet he did not shrink from undertaking the journey, with such an object in view.
  He did, in fact, think that this would be an excellent crown to set upon his virtues, if he should
  leave behind him peace restored to a church.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  Sulpitius frames the Condate journey as a choice, not an accident: Martin goes toward more work,
  not away from it, with the end already in view. The letter reads foreknowledge of death not as a
  burden but as a final chance at virtue - restoring one quarrelling church counted, for Sulpitius, as
  a fitting close to a life already full of them.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.figure.martin
modern_rendering: >-
  I must say, then, that Martin knew the time of his own death long before it came. He told the
  brothers that he would soon leave his body. Meanwhile, a reason arose that led him to visit the
  church at Condate. The clergy of that church were quarrelling among themselves. Martin wanted to
  restore peace there. He knew well that the end of his days was near. Yet he did not shrink from
  making the journey for such a purpose. In fact, he thought that leaving behind him a church at
  peace again would be a fine crown to set on his virtues.
use_note:
  means: "Sulpitius writes that Martin foreknew his death yet travelled to Condate to reconcile its quarrelling clergy, counting restored peace a crown for his virtues."
  not_for:
    - "corroborated fact about the foreknowledge, which rests on Sulpitius alone"
    - "the deathbed scene, which sits in gallic.quote.martin-disciples-plea-and-his-reply"
  years: {from: 397, to: 397}
  status: provisional
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"was aware of the period of his own death"` returns line 2380, opening the paragraph at
`<p id="ii.iii.iii-p12">` (line 2379). `grep -n "excellent crown to set upon his virtues"` returns line
2392, the sentence's close. Read in full at lines 2379-2392: the passage is one continuous, unbroken
run of prose in the source, so the whole run is carried as a single quotation rather than cut at the
two originally flagged fragments within it.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single
spaces. No word was added, dropped, substituted, or reordered.

speaker_or_author is given as "Sulpitius Severus, narrating," not a figure id: this is the letter's
own authorial narration about Martin, not words spoken by Martin or attributed to him directly.
