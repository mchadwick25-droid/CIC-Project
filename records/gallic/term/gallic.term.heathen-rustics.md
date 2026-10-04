---
id: gallic.term.heathen-rustics
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Sulpitius, Tours) for the Gallic-mission sense - a real node marker: nothing in
    Cassian, Vincent, or Salvian as read addresses a pagan countryside. Cassian's "heathen" are the
    philosophers whose chastity was counterfeit (Conf. XIII.4-5) and the "ingrained heathen habits"
    of Gentile converts (XVIII.5) - a different referent, held apart. Under Article 20 the rustics
    are visible only as the ministry's object; none of them speaks. The historicity of the northern
    events falls under virtus / power's Reported-Experience Status. No Latin lemma sought.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. II (parents "heathens"); ch. VI (his mother freed "from the errors of heathenism"); ch. XII ("the Gallic rustics in their wretched folly"; "images of demons veiled with a white covering"); ch. XIII ("very few, nay, almost none ... had received the name of Christ"; churches or monasteries where temples fell; the sacred pine); ch. XIV (the temple burned); ch. XV (the assassin); ch. XVII ("an unconverted heathen")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.4 ("he made them all catechumens, by placing his hand upon the whole of them")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'XIII.4-5 (heathen philosophers) - the other referent'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'XVIII.5 ("their ingrained heathen habits") - the other referent'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether Gaul was Christian in Martin's day
  - what Martin did to temples
  - who the "rustics" were, or how the countryside was converted
  - participant uses "pagan," "heathen," "peasants," "temple," "idol," "mission," "evangelize"
  - the veiled images; the burned temple; the sacred pine; the assassin; "very few, nay, almost none ... had received the name of Christ"
  prefer_instead:
  - the participant means Cassian's "heathen" philosophers or "ingrained heathen habits" - a different referent
  - the question is about the Roman province politically (retrieve Gaul)
  - the south, where no pagan countryside appears at all
relations:
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.possessed-exorcism
- type: associated-with
  target: gallic.term.gaul
- type: associated-with
  target: gallic.term.catechumen
- type: associated-with
  target: gallic.term.conversion
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.sign-of-the-cross
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.monastery-coenobium
- type: associated-with
  target: gallic.term.the-world-secular
plain_meaning: >-
  At Tours, the unconverted countryside of Gaul. It was Martin's mission field. There he halted the
  veiled idols, burned temples, felled a sacred pine, and built churches where they fell.
world_word: heathen / rustics ("the Gallic rustics in their wretched folly")
false_friend:
- '"pagan" as a neutral religious identity to be respected'
- temple-burning as intolerance to be judged
- Gaul as already Christian by the fourth century
- '"rustics" as a social class rather than a religious condition'
senses:
  informational: >-
    Martin's Gaul was mostly not yet Christian, and the Life says so plainly of the country around
    Tours: "before the times of Martin, very few, nay, almost none, in those regions had received
    the name of Christ." The rustics are met on the road with their rites - "the images of demons
    veiled with a white covering" carried through the fields - and Martin halts them with the cross.
    He burns "a very ancient and celebrated temple" and thrusts the flames back from a neighbouring
    house; he fells a sacred pine while "the chief priest of that place, and a crowd of other
    heathens" oppose him; a heathen draws a sword and Martin offers his neck. "Wherever he destroyed
    heathen temples, there he used immediately to build either churches or monasteries." His own
    father "continued to cleave" to heathenism. In the south the word has no countryside behind it;
    Cassian's heathen are philosophers.
  evidential: >-
    Directly attested in Sulpitius alone (Vita II, VI, XII-XV, XVII; Dial. II.4). Cassian's two
    uses name a different referent. The rustics themselves never speak; they are converted in
    crowds, made catechumens by one hand, exorcised, catechized - always the ministry's object.
  personal: >-
    Where the temples fell we built churches and monasteries, and the name of Christ prevailed
    where almost none had received it. That is the north's field, and our saint's power was shown
    there in public. At Marseilles we have no word for what he broke.
  translational: >-
    A modern hearer may see either a neutral "pagan" identity to be respected, or intolerance to be
    judged, and may assume Gaul was already Christian. For us the unconverted countryside was the
    field where the saint's power was shown and the name of Christ made to prevail - and the south
    has no such field at all.
quick_meaning: >-
  At Tours, the unconverted countryside - the mission field where Martin halted idols, burned
  temples, and built churches in their place. Where almost none had the name of Christ.
distortion_risk: medium
use_note:
  means: "Heathen rustics meant, at Tours, the unconverted Gallic countryside where Martin halted idols, burned temples and built churches where they fell."
  not_for:
    - "pagan as a neutral identity, or temple burning as intolerance to be judged"
    - "Gaul as already Christian by the fourth century"
    - "Cassian's heathen philosophers, a different referent"
    - "the Roman province politically, which sits in gallic.term.gaul"
  years: {from: 397, to: 435}
  status: provisional
---
Built from Doc_06 entry 053 (`galliclex053_heathen-rustics.md`, Tier 2, tags SC DR RT; Doc_03
6.8). Single-voice by node, stated in divergence_note; the south's silence is stated, as the
chunk's voice note requires. canon_cells: F3-I because the spread of the name of Christ through
the countryside around Tours is this term's own subject.

Related-Terms also names virtus / power, sign of the cross, bishop / the monk-bishop, conversion,
monastery / coenobium, and the world / secular - cross-batch at authoring time, added as relations
(typed associated-with) at the reconciliation pass once all 81 term records existed. The chunk also
names blessing (in-batch); not made a relation, since no dependency is stated.
