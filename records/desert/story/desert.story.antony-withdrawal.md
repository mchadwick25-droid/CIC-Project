---
id: desert.story.antony-withdrawal
world_id: desert-monasticism
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I, F5-P]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the staged chronology as a general pattern, matching Doc_01 SS2.1's own treatment of it as well-established; Contested for incident-level detail, on the same basis as desert.story.antony-call. The specific dates below (c. 286 for the fort; c. 305 emerging; c. 311-313 to the inner mountain) and the inner mountain's own location (between the Nile and the Red Sea) are Doc_01 SS2.1's own claims, not independently re-derived from the Vita's own text, which does not itself supply calendar years or that geographic description - the Vita's own SS49-50 gives only a three-day journey, a lofty mountain, a spring, a plain and palm trees."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS3-4 - the older ascetic near his own village; SS12-13 - crossing to the abandoned fort across the river and dwelling there, acquaintances who came and waited outside, and the noises they heard within; SS49-50 - the later withdrawal to the inner mountain, seeking greater solitude from the many who beset him"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how someone actually became part of this life, step by step"
  - "participant asks whether belonging here cost something - family, community, standing"
  - "participant asks why someone who sought solitude kept moving further away from people"
relations:
- type: illustrates
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.figure.antony
- type: associated-with
  target: desert.force.village-ascetic-culture
- type: associated-with
  target: desert.dw.strangest
narrative_tier: 1
narrative_tier_justification: "Tier 1 (Documented Historical Narrative), same basis as desert.story.antony-call: named author, contemporary-generation text. The staged pattern (village edge, then a place of greater withdrawal, then greater withdrawal again once the first place stopped being solitary) is the narrative's own repeated structure, not a single incident."
tellable_as: 'Antony withdrew in stages: a hermit near his village, a ruined fort, then a far mountain'
text: >-
  Withdrawal was not one act for us. It was repeated. Antony began close to home, seeing and
  copying an old man already living a solitary life near his village. From there he moved
  further, until he found an abandoned fort across the river, long deserted and overrun. He
  crossed over and shut himself inside it, seeing almost no one for years and receiving bread,
  let down from above, twice a year. People still came and spent days and nights outside.
  Eventually he came out, and disciples gathered near him. Years later, wanting more solitude
  than that gathering allowed, he withdrew again, further still, into the desert. Later report
  places it between the river and the sea; what he himself found was a high mountain, a spring,
  and palms, reached after three days' journey. He stayed there for most of the rest of his
  life. Each move left people behind. The Vita gives a reason only for the last one: crowds
  beset him, and he wanted quiet.
telling: "Athanasius tells us that Antony left the world in stages. First he lived near his own village, as all did who wished to train in those days. He had seen an old hermit in the next village and copied his devotion.\n\nLater he found a fort on the far side of the river. It had stood empty so long that it was full of creeping things. Antony crossed over and lived there, and the creatures, Athanasius wrote, fled at once as if someone were chasing them. He built up the entrance completely and stored six months of loaves. He found water inside. He stayed alone, never going out and never looking at anyone who came, and loaves were let down to him from above twice a year.\n\nFriends who came were not let in. They often spent days and nights outside, and they heard what sounded like crowds clamouring within.\n\nAthanasius says that Antony was beset by many people and could not be still. Then a voice came to him from above and told him that, if he truly wanted quiet, he should go into the inner desert. He journeyed three days and three nights with Saracens, desert nomads, who were going that way. He came to a very lofty mountain, with a clear spring at its foot, a plain, and a few uncared-for palm trees. He recognised the place as his own home and stayed."
absent_detail: "The Vita gives a reason only for the last move: at SS49 he is beset by many, not allowed to be still, and afraid the signs worked through him may puff him up. It states no reason for the earlier moves, and it gives no account of what changed for him at each remove. This world's evidence gives the pattern, not the felt reasoning behind each specific move."
modern_contrast: "A modern reader may hear a lifelong pattern of moving further from people as social avoidance, or read the crowds that kept finding him as ironic proof the withdrawal 'failed.' This world's own record frames the two as compatible rather than contradictory: withdrawal was the whole work of formation (desert.gravity.withdrawal), and being sought out anyway was never the point being defeated - elder-mediated authority (desert.gravity.elder-authority) depended on exactly this kind of asymmetric access, a formed person others could reach even in retreat."
use_note:
  means: "Antony withdrew repeatedly, from an older ascetic near his village to an abandoned fort to the inner mountain, evidencing withdrawal as a lifelong deepening."
  not_for:
    - "Presenting the calendar years or the mountain's location as coming from the Vita, which gives neither"
    - "Supplying reasons for the first two moves, which the Vita does not give; SS49 gives one only for the last"
    - "Presenting incident-level detail as settled"
  years: {from: 270, to: 313}
  status: reviewed
---
Re-derived from the prior build's cleared Doc_09a Story 1.2. SS3-4 and
SS12-13 verified directly against the vendored file this session
(matching desert.force.village-ascetic-culture's own SS3-4 locus and
the general topography narrated at SS12-13 - the abandoned fort, the
acquaintances outside, the noises heard within). SS49-50 (the inner mountain) was also opened directly
this pass: it gives a three-day journey, a lofty mountain, a spring, a
plain and palm trees, but no coastal or riverine placement and no
calendar year - the "between the Nile and the Red Sea" description and
the specific dates are Doc_01 SS2.1's own claims, now cited as such in
divergence_note rather than left implied to come from the Vita itself.

The confidence block attributes "between the river and the sea" and
the specific dates to Doc_01 SS2.1, not to Vita SS49-50, which does not
carry them. The text matches both the Vita ("imitated him in piety,"
Vita SS3) and desert.force.village-ascetic-culture's own wording
("sought out and modeled himself on"). The compiled `text` field marks
the placement as report rather than firsthand narration, and gives what
the Vita itself actually supplies (the three-day journey, the mountain,
the spring, the palms) alongside it, matching the standing rule that a
source's or attribution's own caveat travels with the compiled field
carrying the claim, not only with an uncompiled note. The F5-P-01 cost
reading is stated in the compiled text field itself.

Formation significance: the paradigm instance of
desert.gravity.withdrawal as an intensifying practice rather than a
single decisive break - directly answering F4-I ("How did a person
actually become one of you? Walk me through it.") with the process
itself, and F5-P-01 ("Did belonging cost you anything - family,
friends, standing?"), now answered in the compiled text directly.

The text follows the desert register: short sentences, everyday words; every claim, name, quote, hedge, and reviewed constraint is kept.
