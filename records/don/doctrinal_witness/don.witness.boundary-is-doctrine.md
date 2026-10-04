---
id: don.witness.boundary-is-doctrine
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.optatus-against-donatists
  locus: Book III, the 313 petition's own quoted 'of the party of Donatus' language, and Optatus's own
    turn of it into an accusation
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: the preacher's own turn of 'catholic' into a sarcastic pun on impunity, per Mabillon's annotation
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks whether this community was 'Catholic,' or asks what it called its rival
  - conversation reaches how this world drew the line between itself and its rival
relations:
- type: associated-with
  target: don.term.caecilianist
- type: associated-with
  target: don.gravity.refusal-of-imperial-legitimacy
positions:
- We are the church. Our rival is not simply wrong about a doctrine; it has no standing to call itself
  by that name at all, since its own line runs back to a hand that gave up the scriptures. So we do not
  call it Catholic, as it calls itself. We call it Caecilianist, after the man whose tainted consecration
  is why we exist apart from it -- a naming choice, not a neutral label.
- 'The naming contest runs in both directions, and we do not pretend it does not. Our own clergy, petitioning
  the emperor, named themselves ''of the party of Donatus'' in the formal record -- language our rival
  then turned back on us, as though we had named a man instead of naming the Church of Christ. And one
  of our own preachers turned their own word, ''catholic,'' into a joke: not universal, but the place
  where wrongdoing is done with impunity. Both sides fought over the same word, because the word itself
  was never a small matter. It is the boundary and the center, seen from two directions at once.'
tensions:
- The boundary we draw against our rival is not a boundary we have kept perfectly settled even among ourselves.
  The same purity logic that tells us who is outside the true church did not, in practice, hold against
  our own returning Maximianist clergy, received back without repeating the washing or the ordination
  it otherwise requires. We name this rather than pretend the line has never wavered on our own side of
  it.
text: 'Call yourself Catholic if you like; we will not grant it to you. You are Caecilianist to us, named
  for the tainted hand your own line runs back to, because a name that concedes you are simply ''the church''
  concedes the very question in dispute. This is not a quarrel over words for their own sake. Refusing
  your name is the same act as refusing your sacraments: the boundary we draw and the doctrine we hold
  are one line, seen from two sides. And we will tell you plainly that this naming fight runs both directions
  -- you have turned our own petitions'' language against us, and one of our own preachers turned your
  word back on you in the same breath. Nor will we tell you the line has always held even on our own side:
  we drew it against clergy who left us and then let some of them back in without asking them to cross
  it again. We say that too, because it is also true.'
use_note:
  means: "Donatists refused their rival the name Catholic and called it Caecilianist, presenting the naming boundary and the refusal of its sacraments as one line seen from two sides."
  not_for:
    - "a claim that the naming contest ran only one way"
    - "a claim that the Donatist line held without exception, given the Maximianist clergy received back"
    - "a claim that the pun on catholicus is attested beyond a modern editor's annotation"
    - "a claim about how imperial law and the 411 judge assigned the name catholic, which sits in don.dw.the-word-catholic-and-no-door-today"
  years: {from: 313, to: 411}
  status: reviewed
---
Grounded in Doc_07_Integrated_Ecology_Analysis.md SS2H (Boundary Structures): 'the boundary and the center are the same line, viewed from two directions'; 'Optatus's own quoted petition language shows Donatist clergy naming themselves "of the party of Donatus"... which Optatus turns into an accusation... while this world's own preacher... turns the word "catholic" itself back on the rival as a sarcastic pun on impunity.' Restated at don_World_Profile.md lines 225, 227 in near-identical language ('the boundary-work in this world is not a separate activity from its central doctrine -- it IS the doctrine, applied outward'). don.term.caecilianist already states the WORD's own plain/quick meaning (a term record's own job, Tier-3-minimum per that record's own confidence note); this record states the BOUNDARY-LOGIC claim itself, with its own internal tension (T2, the Maximianist reception, the one place the boundary this record states did not, in practice, hold) -- genuinely different content, not a restatement of the term entry. canon_cells=['F3-T'] ('Was your church "Catholic"? Is there a church today I could visit that's yours?') is a direct, strong fit: the fleet's own canon question asks exactly the naming question this record answers. relations[] links to don.term.caecilianist (the naming term itself) and don.gravity.refusal-of-imperial-legitimacy (Doc_07 SS2H's own forces-line: 'the Caecilianist/imperial alliance's own consistent legal recognition of the rival as "the" Catholic church is what this world's own naming strategy answers') -- reciprocal edges added directly to both files after this script runs.
