---
id: gallic.quote.paphnutius-asks-for-a-plan-of-repentance
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Piamun's own telling (Conferences XVIII.15). The wording is Documented at its
    locus; Paphnutius's stated reason for staying silent is the tradition's own account of his interior
    motive, offered by a narrator who was not present to it.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43040-43058): Paphnutius's own
    silence though innocent, his stated fear of being called a liar, and his fortnight of penance at the
    threshold of the Church"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why Paphnutius did not defend himself, or what the tradition gives as his own reason"
  - "participant asks what penance looked like for a monk of Scete, or what 'not cast down in mind' means in this passage"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.paphnutius-and-the-hidden-book"
text: >-
  Paphnutius, although he was perfectly clear in the sincerity of his conscience, yet like one who
  acknowledged the guilt of thieving, gave himself up entirely to make amends and humbly asked for a plan
  of repentance, as he was so careful of his shame and modesty (and feared) lest if he tried to remove
  the stain of the theft by words, he might further be branded as a liar, as no one would believe
  anything but what had been found out. And when he had immediately left the Church not cast down in
  mind but rather trusting to the judgment of God, he continually shed tears at his prayers, and fasted
  thrice as often as before, and prostrated himself in the sight of men with all humility of mind. But
  when he had thus submitted himself with all contrition of flesh and spirit for almost a fortnight, so
  that he came early on the morning of Saturday and Sunday not to receive the Holy Communion but to
  prostrate himself on the threshold of the Church and humbly ask for pardon, ...
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  The passage gives the reason for the silence in Paphnutius's own logic, not the narrator's guess:
  clearing himself in words risked a second charge, "liar," on top of the first, since the found book
  would outweigh anything he said. His response is not passivity - fasting three times as often, tears,
  a fortnight prostrate at the threshold - it is penance for a crime he did not commit, chosen because he
  judged it safer to trust God's judgment than his own defense.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: >-
  Paphnutius knew his conscience was completely clear. Yet he acted like a man who admitted he was
  guilty of theft. He gave himself up wholly to making amends, and humbly asked to be given a course of
  penance. He cared deeply about his modesty and his sense of shame. He feared that if he tried to wipe
  away the stain of the theft with words, he would also be branded a liar. No one would believe anything
  except what had been found. He left the church at once, not downcast but trusting in the judgment of
  God. He wept constantly at his prayers, and fasted three times as often as before. In front of others
  he lay face down, with complete humility of mind. For almost two weeks he humbled himself like this,
  in deep sorrow of body and spirit. Early on Saturday and Sunday mornings he came to church, but not to
  receive Holy Communion. He came to lie face down on its threshold and humbly ask for pardon.
use_note:
  means: "Piamun, in Cassian's Conferences, tells how the innocent Paphnutius accepted penance for the theft rather than defend himself, fearing to be called a liar."
  not_for:
    - "a rule that the falsely accused should always accept guilt, rather than one monk's choice"
    - "the accuser's possession and Paphnutius's vindication, which sit in gallic.quote.paphnutius-the-thief-possessed-and-healed"
    - "Gallic communion practice, when the Saturday and Sunday detail is Egyptian"
  years: {from: 426, to: 435}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "And
when the inquisitors"` returns line 43039 (this quote's opening sentence begins there); `grep -n "humbly
ask for"` returns line 43057, continuing to "pardon," on line 43058. Read with `sed -n '43039,43058p'`.

Normalization: line breaks joined with single spaces. The endnote anchor after "Holy Communion" (n="2092",
a note on Saturday/Sunday communion practice in Egypt versus Gaul) sits inside the source's own prose and
is dropped. No word was added, dropped, substituted, or reordered. The quote ends mid-sentence, at the
comma after "pardon,", because the next clause ("He, Who is the witness of all secret things...") opens a
new narrative movement, carried in its own quote record.
