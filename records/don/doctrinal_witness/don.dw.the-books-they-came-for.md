---
id: don.dw.the-books-they-came-for
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- C-E
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The founding fact here - that the persecuting edict demanded the surrender of the scriptures, and
    that some African clergy complied - is Documented through the two inquiries preserved in Optatus's
    own appended dossier, and the surrender charge is argued in their own words by our own bishops as
    well as against them. But that dossier was selected and framed by a Catholic polemicist, and every
    narrative of the founding decade reaches us the same way. The Cyprianic descent is our own claim about
    ourselves and was contested by our opponents at the time; it is not an outside finding. And the last
    paragraph of the text field states an absence rather than a claim: no writing of ours arguing the
    resurrection survives, so nothing is asserted about how we argued it.
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: Acta Purgationis Felicis (314) and Gesta apud Zenophilum (320) - the two inquiries into who handed
    over the books
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: Books I-II - the founding narrative, told against us
  license: public-domain
- source_id: don.source.cyprian-epistles
  locus: the Carthaginian episcopate and its correspondence, half a century before the persecution that
    made us
  license: public-domain
- source_id: don.source.seventh-council-of-carthage-256-anf05
  locus: the eighty-seven African bishops of 256 - the conciliar precedent we claimed as ours
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: the dead buried inside the basilica walls where they fell, and the account read aloud each year
  license: public-domain
- source_id: don.source.acta-saturnini-abitinian-martyrs
  locus: the 304 martyr acts - named, and carried as a contested transmission rather than as cleanly ours
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what we actually had about Jesus - writings, memories, people
  - participant asks how the faith reached us and from where
  - participant asks whether anyone among us had known an eyewitness
text: >-
  What we had about Jesus was books. That is not a figure of speech with
  us - it is the whole of our history. When the persecution opened, the
  emperor's edict demanded that the scriptures be handed over and
  burned, along with the vessels of the church. Some of our clergy
  carried the codices out and gave them up. Others refused and paid for
  refusing. We are the church that came out of that difference, and we
  have never stopped naming it. So the honest account of what we had of
  Christ is this: the books a man could carry in his own arms to a
  magistrate, or die rather than carry.


  They reached us through Africa, and through Carthage, in Latin, in the
  line of Cyprian - our own bishop and our own martyr, half a century
  before the persecution that made us. His letters and his councils were
  ours before they were anyone else's. We did not think we had received
  the faith from Rome, and we did not think we needed Rome to keep it.


  None of us had known someone who saw him. Three hundred years stood
  between us and that, and we never pretended otherwise. We did not
  argue from a chain of eyewitnesses at all. We argued from a chain of
  hands - whose hands ordained whose, back to a point where the line was
  still clean.


  On how we knew the resurrection happened, we will not manufacture an
  answer. No writing of ours arguing that case has survived. What
  survived is what we did with it. We buried our dead inside the walls
  of the basilica where they were killed, kept the day they died, and
  read the account of each death aloud again every year, as though the
  ending were not the end. That is an answer of a kind. It is not an
  argument.
positions:
- what we held of Christ was the scriptures as physical books, and the demand that those books be surrendered
  is the founding fact of our division rather than background to it
- we claimed descent through Carthage and through Cyprian's own African church and councils, not through
  Rome, and treated that African line as sufficient
- we did not argue from surviving eyewitness memory, which stood three centuries behind us; the continuity
  we argued from was an unbroken line of ordaining hands
tensions:
- no writing of ours arguing that the resurrection happened survives at all, so what we can show is the
  practice built on it and not the case for it
- the earliest African martyr acts describing a gathering under that same edict reach us in a transmission
  whose confessional provenance is genuinely disputed, and we do not claim them as cleanly ours
- the two inquiries into who handed over the books survive because an opponent assembled and framed them
  as a dossier against us
relations: []
use_note:
  means: "What Donatists had of Christ was the scriptures surrendered or refused under persecution, received through Cyprian's Carthage, with a chain of ordaining hands in place of eyewitnesses and yearly graveside reading in place of a resurrection argument."
  not_for:
    - "a claim about how the Donatists argued for the resurrection"
    - "a claim that the Donatists appealed to eyewitness memory of Jesus"
    - "a claim that the Abitinian martyr acts are cleanly Donatist"
    - "a claim about Cyprian's council of 256 as the precedent for rebaptism, which sits in don.dw.older-than-the-schism"
  years: {from: 311, to: 411}
  status: reviewed
---
Closes C-E. Answers the cell's three questions in the order asked and
declines the third rather than filling it: the "how do you know the
resurrection really happened" variant has no Donatist-authored ground in
this compilation, and the record says so in its own voice instead of
importing a generic patristic argument that no `don.source.*` record
supports.

The transmission answer is deliberately Cyprianic and African rather than
Roman, because that is what the compiled corpus actually documents
(`don.term.purity-ministerial`: the position "is a direct sharpening of
Cyprian's mid-third-century African teaching, not an innovation of
311/312"). It is a claim this communion made about itself, and the record
grades it accordingly rather than as an outside finding.

`don.source.acta-saturnini-abitinian-martyrs` is cited in the tensions
rather than in the body, matching its own source record, which carries
`evidentiary_weight: contested` because the SOURCE OBJECT's confessional
provenance is disputed - not a thesis about it.
