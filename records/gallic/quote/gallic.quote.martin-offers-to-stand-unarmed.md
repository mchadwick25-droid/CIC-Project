---
id: gallic.quote.martin-offers-to-stand-unarmed
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Widely Accepted as Sulpitius's own text (Vita ch. IV, read at its own locus for
    this record). The providential reading of the enemy's surrender ("who can doubt that this victory
    was due to the saintly man?") is disclosed here as Sulpitius's own framing, carried as his, not
    adopted as this record's independent finding - the same caution the host record's own
    divergence_note states. One named ancient witness, not present at the scene, is Widely Accepted
    strength, not Documented.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. IV (npnf211 div ii.ii.v, file lines 842-863): Julian's charge of cowardice, Martin's offer to stand unarmed, the imprisonment, and the enemy's surrender"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Martin offered to do to prove he was not afraid"
  - "participant asks how the standoff with Julian ended"
  - "Representative needs Sulpitius's own providential reading of the surrender, named as his"
  prefer_instead:
  - "participant wants the whole scene told as a story, with its outcome - retrieve gallic.story.discharge-before-caesar, which this record is drawn from"
  - "participant wants Martin's first speech, refusing the donative - retrieve gallic.quote.martin-refuses-the-donative"
text: >-
  Then truly the tyrant stormed on hearing such words, declaring that, from fear of the battle, which
  was to take place on the morrow, and not from any religious feeling, Martin withdrew from the
  service. But Martin, full of courage, yea all the more resolute from the danger that had been set
  before him, exclaims, "If this conduct of mine is ascribed to cowardice, and not to faith, I will
  take my stand unarmed before the line of battle tomorrow, and in the name of the Lord Jesus,
  protected by the sign of the cross, and not by shield or helmet, I will safely penetrate the ranks
  of the enemy." He is ordered, therefore, to be thrust back into prison, determined on proving his
  words true by exposing himself unarmed to the barbarians. But, on the following day, the enemy sent
  ambassadors to treat about peace and surrendered both themselves and all their possessions. In these
  circumstances who can doubt that this victory was due to the saintly man? It was granted him that he
  should not be sent unarmed to the fight. And although the good Lord could have preserved his own
  soldier, even amid the swords and darts of the enemy, yet that his blessed eyes might not be pained
  by witnessing the death of others, he removed all necessity for fighting. For Christ did not require
  to secure any other victory in behalf of his own soldier, than that, the enemy being subdued without
  bloodshed, no one should suffer death.
speaker_or_author: "Sulpitius Severus, narrating, with Martin's own vow quoted directly"
license: verbatim
modern_lens_note: >-
  A modern reader hears an offer to walk unarmed toward an army as reckless, or as a rhetorical
  flourish never meant to be tested. Sulpitius does not let it stay rhetorical - Martin is imprisoned
  overnight, still "determined on proving his words true." What settles the scene for Sulpitius is not
  that Martin was brave; it is that no battle was needed at all, which he reads as evidence the victory
  was granted rather than won. The passage keeps that reading explicit as the narrator's own, not as a
  claim this record independently verifies.
modern_rendering: >-
  Then the tyrant flew into a rage at these words. He declared that Martin was leaving the army out of
  fear of the battle set for the next day, not out of any religious feeling. But Martin was full of
  courage. The danger put before him made him all the more determined. He cried out: "Is what I am
  doing put down to cowardice and not to faith? If so, I will stand unarmed in front of the battle
  line tomorrow. In the name of the Lord Jesus, I will pass safely through the enemy ranks. I will be
  guarded by the sign of the cross, not by shield or helmet." So he was ordered to be thrown back into
  prison, set on proving his words true by facing the barbarians unarmed. But the next day the enemy
  sent envoys to discuss peace. They surrendered themselves and everything they owned. Given all this,
  who can doubt that this victory was due to the holy man? He was granted this: he would not be sent
  unarmed into the fight. The good Lord could have kept his own soldier safe, even among the swords
  and javelins of the enemy. But he did not want Martin's blessed eyes to suffer the pain of watching
  others die. So he took away any need to fight. Christ needed to win no other victory for his own
  soldier than this one. The enemy was beaten without bloodshed, and no one had to die.
relations:
- type: associated-with
  target: gallic.story.discharge-before-caesar
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.martin-refuses-the-donative
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, same chapter div
`id="ii.ii.v"` (line 819) as gallic.quote.martin-refuses-the-donative. `grep -n "thrust back into
prison"` and `grep -n "who can doubt that this victory"` each return one hit, lines 852 and 855-856.
Read lines 842-863 directly: the quoted span runs from "Then truly the tyrant stormed..." through "...
no one should suffer death," the remainder of the same paragraph and the end of the chapter - one
continuous passage, nothing skipped.

Normalization: line breaks joined with single spaces. Martin's second speech is marked in the source
by a dash before an opening curly quotation mark, closed by a plain curly closing mark; rendered here
as a normal, properly-paired quotation for the same reason given on the companion record. No word was
added, dropped, substituted, or reordered.

speaker_or_author names both the narrator and the quoted speaker, as on the companion record, because
narration and Martin's vow form one continuous sentence in the source.
