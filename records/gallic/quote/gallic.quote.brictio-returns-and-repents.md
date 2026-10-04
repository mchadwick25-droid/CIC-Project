---
id: gallic.quote.brictio-returns-and-repents
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
    Widely Accepted and Documented at its locus (Dialogues III.15). The demonic explanation for Brictio's
    change of heart ("I believe") is Gallus's own interpretation, carried at Contested strength for the
    demon's role specifically; the repentance and forgiveness themselves are the narrative's plain claim.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.15 (npnf211 div ii.iv.iii.xv, file lines 5323-5330): Brictio's sudden return,
    his plea for pardon at Martin's feet, and Martin's ready forgiveness"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how the quarrel ended, or how quickly Brictio repented"
  - "participant asks how readily Martin forgave, or what forgiveness looked like in practice"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.brictio-in-the-courtyard"
text: >-
  But with rapid steps he rushed back by the way he had gone out, the demons having, I believe, been, in
  the meantime, driven from his heart by the prayers of Martin, and he was now brought back to
  repentance. Speedily, then, he returns, and throws himself at the feet of Martin, begging for pardon
  and confessing his error, while, at length restored to a better mind, he acknowledges that he had been
  under the influence of a demon. It was no difficult business for Martin to forgive the suppliant.
speaker_or_author: "Gallus, as Sulpitius Severus records his account in the Dialogues"
license: verbatim
modern_lens_note: >-
  The turn is immediate - "rapid steps," "speedily" - and it is Brictio himself, in Gallus's report, who
  names a demon as the cause of his own outburst; Gallus does not put the words in his mouth. Martin's
  forgiveness is reported in a single short sentence, with none of the ceremony given to the accusation
  itself - the story spends far more words on the rage than on the pardon.
relations:
- type: associated-with
  target: gallic.story.brictio-in-the-courtyard
modern_rendering: >-
  But he rushed back quickly the way he had gone out. In the meantime, I believe, Martin's prayers had
  driven the demons from his heart. Now he had been brought back to repentance. So he quickly returns
  and throws himself at Martin's feet. He begs for pardon and confesses his error. At last restored to a
  better mind, he admits that a demon had been driving him. It was no hard thing for Martin to forgive
  the man who begged him.
use_note:
  means: "Gallus relates that Brictio rushed back, confessed at Martin's feet that a demon had driven him, and Martin readily forgave him."
  not_for:
    - "the demon's role as established fact, when Gallus offers it as his belief"
    - "the tirade itself, which sits in gallic.quote.brictio-tirade-and-martins-restraint"
  years: {from: 404, to: 406}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "But
with rapid steps"` returns line 5323; `grep -n "forgive the suppliant"` returns line 5330. Read with `sed
-n '5323,5330p'`.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
