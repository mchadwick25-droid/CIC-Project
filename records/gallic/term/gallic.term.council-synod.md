---
id: gallic.term.council-synod
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-E
- F3-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice tension, directly opposed [PV]: the same institution is the guarantor of truth in
    Vincent's Lerins (an ancient General Council's decrees preferred to "the rashness and ignorance
    of a few"; Ephesus, which "innovated nothing") and the thing the saint flees in Sulpitius's
    Tours (the assembly of bishops that handed the Priscillianists to the sword; "never again did
    he attend a synod"). The divergence is the finding, not a defect, and the two hearings are
    never reconciled. Cassian has no council in what was read. No Latin lemma sought.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 3 [8] ("prefer the decrees, if such there be, of an ancient General Council to the rashness and ignorance of a few"); ch. 29 [77] ("the holy council which some three years ago was held at Ephesus"); ch. 31 [82] ("innovated nothing, presumed nothing, arrogated to themselves absolutely nothing")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'II.13 ("A synod, composed of bishops, was held at Nemausus"); III.13 ("never again did he attend a synod, and kept carefully aloof from all assemblies of bishops")'
  license: public-domain
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.47 ("a Synod was assembled at Saragossa"); II.50 ("declared heretics by a sentence of the bishops") - II.46-51 only read'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what authority councils had
  - why Vincent appeals to Ephesus
  - why Martin refused to attend synods
  - participant uses "council," "synod," "ecumenical," "bishops meeting," "Ephesus," "Nicaea"
  - Comm. ch. 3 or chs. 29-31; the angel who reported the synod at Nemausus; Saragossa; "never again did he attend a synod"
  prefer_instead:
  - the question is about the bishop's office (retrieve bishop / the monk-bishop)
  - the question is about the rule's three criteria (retrieve the rule)
  - the question is about the elder's after-supper conference (retrieve conference)
  - a specific council's canons - Ephesus is Vincent's example, not our subject
relations:
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.progress-vs-alteration
- type: associated-with
  target: gallic.term.heretic-heresy
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.apostolic-see-pope
- type: associated-with
  target: gallic.term.angels
- type: associated-with
  target: gallic.term.theotocos
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.the-fathers-elders
plain_meaning: >-
  Two things at once. At Lerins, the ancients' decree that guards the faith, legitimate because it
  innovates nothing. At Tours, the assembly of bishops that handed heretics to the sword, and
  that Martin never entered again.
world_word: council / synod
false_friend:
- '"ecumenical council" as a settled constitutional organ with defined authority'
- synods as church bureaucracy
- Martin's refusal as anti-institutionalism
senses:
  informational: >-
    At Lerins the council guards antiquity. When within antiquity itself the ancients disagree,
    the Catholic will "prefer the decrees, if such there be, of an ancient General Council to the
    rashness and ignorance of a few." Vincent's proof is recent: "the holy council which some three
    years ago was held at Ephesus," where the bishops "innovated nothing, presumed nothing,
    arrogated to themselves absolutely nothing, but used all possible care to hand down nothing to
    posterity but what they had themselves received from their Fathers." A council is legitimate
    exactly insofar as it transmits. At Tours the synod is where bishops do harm. Martin refused to
    attend the synod at Nemausus and was told its decrees by an angel on shipboard. At Saragossa the
    Priscillianists were condemned in their absence; the affair ended at Trier with an emperor's
    sword. Forced into one communion with the Ithacian bishops, Martin "never again did he attend a
    synod, and kept carefully aloof from all assemblies of bishops."
  evidential: >-
    Attested in Vincent (Comm. 3, 29, 31) and Sulpitius (Dial. II.13, III.13; Sacred History
    II.47, II.50). Cassian has no council in what was read. The two valences are documented
    separately and never meet in one text.
  personal: >-
    We hold both without reconciling them. Vincent's council may not speak for Martin, nor
    Martin's flight for Vincent. The bishop who was made bishop against bishops kept away from the
    place where bishops gather - and the monk of Lerins looked to that place for the memory of the
    whole Church set in writing.
  translational: >-
    A modern hearer wants a council to be a constitutional organ with defined authority, or wants
    Martin's refusal to be a stand against institutions. Neither fits. For Vincent a council is
    legitimate only because it hands on what it received; for Martin the synod is where bishops
    urged the sword, and he would not sit there again.
quick_meaning: >-
  For Vincent, the ancients' decree preferred to the rashness of a few, valid because it adds
  nothing. For Martin, the assembly that handed heretics to the sword, and which he never
  attended again. Two hearings we never reconciled.
distortion_risk: medium
use_note:
  means: "Council meant two opposed things: for Vincent the ancients' decree that guards the faith by innovating nothing, for Martin the bishops' assembly he never entered again."
  not_for:
    - "an ecumenical council as a settled organ with defined authority"
    - "Martin's refusal as anti-institutionalism"
    - "the bishop's office, which sits in gallic.term.monk-bishop"
    - "the three criteria of Vincent's test, which sit in gallic.term.the-rule"
  years: {from: 397, to: 434}
  status: reviewed
---
Built from Doc_06 entry 059 (`galliclex059_council-synod.md`, Tier 2, tags SC TC PV; Doc_03
7.8). The [PV] is carried as the divergence_note's substance and in every sense: neither valence
is allowed to speak for both. canon_cells: F1-E because Vincent's account of what Ephesus's
bishops did ("innovated nothing") is this world's own answer to how a council relates to the
faith; F3-P because Trier and the sword are the north's own record of bishops using state power
against Christians who disagreed, and Martin's refusal is its judgment on that.

Related-Terms also names bishop / the monk-bishop, the rule, novelty vs. antiquity, and the Fathers
/ elders - cross-batch at authoring time, added as relations (typed associated-with) at the
reconciliation pass once all 81 term records existed.
