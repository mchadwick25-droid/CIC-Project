---
id: don.contested.augustine-precipice-charge
world_id: donatism
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells:
- F6-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: don.source.augustine-answer-to-petilian
  locus: 'Answer to the Letters of Petilian, Book II, paras 46, 110, 114, 160, 193, 195, 197 and 204 (npnf104, lines 16209-16210, 16857, 16889-16891, 17232, 17532, 17550, 17575, 17715)'
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: 'Against the Donatists, Book III, chapter 4 (optatus_against-the-donatists.txt, line 2014): the charge that some sought death out of desire for a false martyrdom'
  license: public-domain
- source_id: don.source.augustine-correction-of-the-donatists
  locus: 'Letter 185, chapter 3 (npnf104 line 19454): the charge that they killed themselves as a daily habit'
  license: public-domain
- source_id: don.source.passio-marculi
  locus: 'the Latin account of Marculus''s death, told as an execution (monumenta-vetera-donatistarum_migne-pl8.txt, lines 1232-1235)'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks whether Optatus's and Augustine's charges against the Donatist martyrs are true
  - participant asks how Marculus or Donatus died
  prefer_instead:
  - participant asks whether the martyrs' deaths prove the Donatist claim (don.contested.church-of-the-martyrs)
  - participant asks about the Circumcellions' character generally (don.contested.circumcellion-character)
relations: []
claim: Some Donatists honoured as martyrs took their own lives. Two Catholic bishops say so.
held_against:
- The charge comes only from opponents. Optatus (Against the Donatists III.4) and Augustine (Answer to Petilian II.46, 110, 114, 160, 193, 197, 204; Letter 185.12) both wrote to deny these dead the name of martyr. Two hostile writers agreeing is not independent confirmation.
- Augustine's own case admits doubt. Of Marculus and Donatus, the deaths most often cited, he calls it a great question whether they died by their own act or were put to death by command (II.46).
- The one Donatist account of such a death, the Passio Marculi, tells it as an execution. Marculus was put to death by his enemies.
- Augustine names the Circumcelliones in some of these passages (II.46, 110, 204) and not in others, where he speaks of your martyrs and those confessors of yours (II.114, 160, 193). Beyond Marculus and Donatus he names no one and gives no number or date.
- His harshest verdict on these deaths (II.114) answers a taunt in Petilian's own letter. It is a judgment in a quarrel, not a report of events.
concedes: That both opponents made the charge is not in doubt, and Augustine treats such deaths as common. Whether any Donatist died this way, and how many, cannot be settled from hostile writers and one hagiography. This record does not say it happened or that it did not.
use_note:
  means: "Two Catholic opponents charge that Donatists honoured as martyrs people who took their own lives; this is hostile polemic about a contested group, not an independent report."
  not_for:
    - "a claim about the eternal fate of any person who died by suicide"
    - "a claim that the passage is advice to a person now in distress"
    - "a claim that Donatists did, or did not, die this way, beyond what their opponents allege"
    - "a claim that Augustine's harshest verdict on these deaths applies to anyone outside this dispute"
  years: {from: 366, to: 417}
  status: provisional
---
