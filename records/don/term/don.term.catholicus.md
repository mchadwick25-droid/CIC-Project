---
id: don.term.catholicus
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: 'The sharpest piece of content here -- the Donatist preacher''s sarcastic pun, ''catholic''
    not as universal but as the place where wrongdoing is committed with impunity -- reaches this record through
    Jean Mabillon''s seventeenth-century annotation on the commemorative sermon as reported in Doc_02 SS4 and
    Doc_03 Cluster 2, not from the sermon''s own Latin read directly: Doc_02 SS9 item 12 records that the sermon''s
    full text beyond the passages checked has not been read. Doc_03 SS6 also flags modern editorial mediation
    of this kind as a distinct risk from ancient Author Gravity and asks Doc_06 to give it its own label; Doc_06
    did not, so the distinction is carried here in the record instead.'
sources:
- source_id: don.source.passio-donati-sermon
  locus: the preacher's wordplay on 'catholic', via Mabillon's annotation
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: the rival's own claim to the unqualified title
  license: public-domain
- source_id: don.source.monceaux-histoire-litteraire-tome5
  locus: the fuller modern analysis of the sermon
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - a participant asks who the 'Catholics' were in this dispute, or whether that word settles anything
  - a participant asks how the word 'catholic' was used or contested here
  prefer_instead:
  - '''Catholic'' is being used for the later Roman Catholic Church as a modern institution'
relations:
- type: associated-with
  target: don.term.ecclesia
- type: associated-with
  target: don.term.caecilianist
plain_meaning: Both sides read 'catholic' -- universal -- as their own rightful title. The state grants it to
  our rival; we do not. One of our own preachers turned the word back on them. He said it names the place where
  wrong is done and no one is punished for it.
world_word: catholicus
false_friend:
- the Roman Catholic Church as a later, settled denominational body
- '''catholic'' as an agreed and uncontested title in the fourth-century West'
- a purely doctrinal word, when the fight over it here is about legitimacy and law
senses:
  informational: 'Both hierarchies claimed universality, and the imperial administration consistently attached
    the word to the rival. The counter-move preserved in the record is a pun rather than an argument: a Donatist
    preacher, on Mabillon''s reading of the commemorative sermon, twisted ''catholic'' from universal into the
    place where wrongdoing goes unpunished.'
  evidential: Widely Accepted rather than Documented at citation level. The pun is reported by a modern editor
    annotating a sermon whose own full Latin this build has not read, and Doc_02 SS9 item 12 names that gap explicitly.
    The contest over the word itself is not in doubt; this particular witticism rests on editorial mediation and
    should be attributed that way if it is used.
  personal: Losing a word to one's opponents is a real loss when the state enforces the usage. The pun is what
    refusal sounds like when the legal fact cannot be changed.
  translational: '''Catholic just means the Roman Catholic Church, doesn''t it?'' -- not here, and not yet. In
    fourth-century Africa it is a contested adjective meaning universal, claimed by two rival bodies, with the
    law backing one of them.'
quick_meaning: Universal -- the title our rival claims, the state grants, and we refuse to concede.
distortion_risk: high
use_note:
  means: "Both sides claimed 'catholic', meaning universal; the state granted it to the rival, and a Donatist preacher reportedly turned the word back on them."
  not_for:
    - "a claim that catholic was an agreed and uncontested title in the fourth-century West"
    - "a claim that it refers to the later, settled Roman Catholic Church"
    - "a claim that the fight over the word was purely doctrinal rather than about legitimacy and law"
    - "a claim about the 411 judge's ruling on the name, which sits in don.dw.the-word-catholic-and-no-door-today"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 007 (Tier 2, no promotion forwarded). No deployment chunk built this cycle. Doc_03 SS6 names modern editorial mediation (Mabillon/Monceaux as a different kind of risk from ancient Author Gravity), and Doc_06 did not act on it; divergence_note holds that risk.
