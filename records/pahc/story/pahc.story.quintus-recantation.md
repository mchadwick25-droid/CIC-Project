---
id: pahc.story.quintus-recantation
world_id: post-apostolic-house-church
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Contested on the same dating grounds as pahc.story.martyrdom-of-polycarp (c. 155-156 traditional vs. Eusebius's Chronicon 167 CE) and shaped by the same hagiographic letter's own conventions - see pahc.contested.martyrdom-polycarp-dating. This specific passage (ch. 4) is widely regarded by scholars as an early, unedited layer of the letter precisely because it is unflattering to the community's own reputation - an argument from embarrassment, not independent attestation, and this record does not upgrade its own narrative_tier on that basis alone."
sources:
- source_id: pahc.source.martyrdom-polycarp
  locus: "4 (Quintus's own recantation); 5-7 (Polycarp's own withdrawal and arrest, by contrast); 6 (the two youths seized, one tortured into confessing)"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether this world ever encouraged seeking out martyrdom"
  - "participant asks what happened when someone's courage failed under threat"
  prefer_instead:
  - "participant needs Polycarp's own death narrated in full - use pahc.story.martyrdom-of-polycarp instead"
relations:
- type: associated-with
  target: pahc.gravity.martyrdom-meaning
- type: associated-with
  target: pahc.story.martyrdom-of-polycarp
narrative_tier: 3
narrative_tier_justification: "Tier 3 (attributed tradition), matching pahc.story.martyrdom-of-polycarp: both come from the same letter, framed as Smyrna's own testimony to Philomelium rather than direct documentation, and shaped by the same hagiographic and martyrological convention throughout. This specific passage carries a real, disclosed nuance (see divergence_note) - its unflattering content is one argument scholars use for treating it as an early, unedited layer - but that argument bears on textual layering, not on the passage's own genre, so this record keeps the same tier its sibling carries rather than treating internal plausibility as a reason to grade it higher."
tellable_as: >-
  Before the letter praises Polycarp's own courage, it names a different man first. He came forward
  for trial on his own. Then he lost his nerve, when he actually saw the beasts.
text: >-
  This is how the community at Smyrna told it, in the same letter that honors Polycarp's own death.
  Before that letter praises him, it names someone else first. A man named Quintus, a Phrygian who
  had lately come to the city, forced himself - and some others with him - to come forward for trial
  of his own will. But when he actually saw the wild beasts, he lost his nerve. After much urging, the
  proconsul persuaded him to swear the oath and offer sacrifice. The community's own letter draws the
  lesson plainly, without softening it: "we do not commend those who give themselves up, since the
  Gospel does not teach so." Polycarp did the opposite. When he first heard that he was being sought,
  he was not troubled at all. At his own community's urging, he agreed to leave the city for a quiet
  house in the country, where he spent his last days praying. He did not go looking for arrest. He was
  found only after two young men in his own household were seized. One of them, tortured, told his
  pursuers where he was. The letter sets these two men side by side on purpose. One went looking for
  the test, and failed it. The other simply kept living faithfully, was found where he was, and held
  firm once he was.
absent_detail: "Quintus's own account of what led him to come forward, or of what he felt when his nerve broke, does not survive. Only the community's judgment of the act is recorded, never his own words."
modern_contrast: >-
  A modern reader often hears a martyr story as a simple call to imitate all-out courage. This
  world's own record complicates that on purpose. The very letter that honors Polycarp's death also
  names a man who sought the danger out and failed. It says plainly that seeking danger out was
  never the example to follow.
use_note:
  means: "Before praising Polycarp's courage, the letter names Quintus, who came forward for trial on his own and lost his nerve at the sight of the beasts."
  not_for:
    - "a call to imitate all-out courage"
    - "seeking danger out as the example to follow"
    - "Quintus's own account of his reasons"
  years: {from: 155, to: 156}
  status: reviewed
---
`atlas-v3.html`'s own `documentedStories` array for
post-apostolic-house-church names
three entries: "Ignatius Asks Rome Not to Save Him" (matches
`pahc.story.ignatius-guarded-journey`), "The Grandsons of Jude Before
Domitian" (matches `pahc.story.grandsons-before-domitian`), and
"Quintus, Who Volunteered and Then Swore" - which matched no existing
story record. `pahc.story.martyrdom-of-polycarp` narrates the same
letter but centers Polycarp's own trial and death (chs. 6, 9, 12,
15-16, 18); the site's own third entry centers a different passage
(ch. 4, plus the withdrawal/arrest material in chs. 5-7) with a
different point - a caution against seeking martyrdom out, not
Polycarp's own martyrdom. This record covers that ground as its own
story rather than folding it into the sibling record, matching this
world's own gravity record's (`pahc.gravity.martyrdom-meaning`) already
established use of the same Quintus material ("the community's own
recorded refusal to commend a volunteer who recanted") and
`pahc.demo.lament-suffering`'s own reliance on it.

Every quotation and detail checked directly against
`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`, div2 iv.iv,
chapters IV-VII: ch. 4 ("Now one named Quintus, a Phrygian, who was
but lately come from Phrygia, when he saw the wild beasts, became
afraid. This was the man who forced himself and some others to come
forward voluntarily [for trial]. Him the proconsul, after many
entreaties, persuaded to swear and to offer sacrifice... we do not
commend those who give themselves up [to suffering], seeing the Gospel
does not teach so to do" - quoted verbatim); ch. 5 ("when he first
heard [that he was sought for], was in no measure disturbed... in
deference to the wish of many, he was persuaded to leave it. He
departed, therefore, to a country house..."); ch. 6 ("they seized upon
two youths [that were there], one of whom, being subjected to torture,
confessed. It was thus impossible that he should continue hid, since
those that betrayed him were of his own household"). No detail is
carried from the site's own prose without this direct re-verification;
the site's own "a servant boy was tortured" is looser than the
vendored text's "two youths," one of whom was tortured and confessed -
this record's own text keeps the vendored text's actual count and
wording rather than the site's paraphrase.

CROSS-RECORD CONSISTENCY CHECKED against `pahc.story.martyrdom-of-
polycarp` (both narrate the same letter, related here by
`associated-with`): no contradiction found. The sibling record's own
"eighty and six years" quotation (ch. 9) is not repeated here; this
record stays inside chs. 4-7, the material its own sibling does not
narrate, and both records' framing of Polycarp's own withdrawal agree
(neither claims he sought arrest).

Reciprocal `associated-with` edges added on this same pass to
`pahc.gravity.martyrdom-meaning` and `pahc.story.martyrdom-of-polycarp`
(gate_reciprocity's own requirement) - see each record's own trailing
note.
