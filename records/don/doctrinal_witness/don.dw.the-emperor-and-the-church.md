---
id: don.dw.the-emperor-and-the-church
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The utterance at the centre of this record - what has the Emperor to do with the Church - survives
    only inside the polemic of a man who reports it as a fit of rage, and that framing is stated in the
    text field rather than quietly dropped. The three exceptions to our own refusal are documented per
    episode and are named here in our own voice, because our record states them plainly in the same texts
    that state the doctrine at its most absolute. Reading the episodes as one principled stance rather
    than as a series of separate grievances is partly this build's own frame (Doc_04 SS3.7), and is carried
    as a stance held on balance rather than as a rule.
sources:
- source_id: don.source.optatus-against-the-donatists
  locus: Book III.3 - Donatus answering the imperial commissioners, reported as his own fury
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: Constantine's letters; Anulinus's relatio of 313; the Council of Arles' 314 letter to Silvester
  license: public-domain
- source_id: don.source.codex-theodosianus-book-16
  locus: the 405 Edict of Unity and the later suppression legislation
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: soldiers taking a basilica at Carthage in the name of unity, and killing people at prayer inside
    it
  license: public-domain
- source_id: don.source.augustine-correction-of-the-donatists
  locus: the defence of using the state's force against Christians who disagreed
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks whether Constantine or the empire corrupted the church
  - participant asks whether Christians hid in the catacombs
  - participant asks what outsiders and neighbours said about us, or found strangest
text: >-
  Did the empire change what the church was? That is not a question to
  us. That is our whole case, and we are the party that answered yes.


  Catacombs first, because it is the wrong picture. Nobody among us hid
  underground. The persecutions in our own time did not send us into
  tunnels; they sent soldiers into our buildings in broad daylight, under
  orders, to enforce a single church. We read the account of one such day
  aloud every year: a basilica at Carthage seized, a house of prayer
  turned into a place of feasting and licence, people clubbed to death
  where they knelt with their eyes shut, and buried inside the walls
  because there was nowhere else and nobody to stop it. That is what
  persecution looked like for us. Not hiding. Being visited.


  Now Constantine. We petitioned him, in the first year, through his own
  governor - we asked him to take the matter up. He gave us a hearing at
  Rome and
  then a council at Arles, and both ruled against us, and we refused
  both. Not because a council cannot rule. Because a court convened,
  staffed and enforced by a power that has already decided which side is
  the church is not the church judging itself. Our own bishop is
  remembered putting it to the emperor's commissioners in five words:
  what has the Emperor to do with the Church? You should know that the
  only man who wrote that sentence down was one of our enemies, and he
  set it in a paragraph about our bishop's pride and his fits of temper.
  We would keep the sentence and drop the paragraph. He would say we are
  being selective. We would say he was there to make us look mad.


  We will not pretend we were clean about this. Three times we used the
  same machinery we denied had standing: when we asked Constantine for
  judges, when we asked a later emperor for our confiscated basilicas
  back, and when we turned the imperial law against heretics onto our own
  breakaway party. We did not hide any of it. It sits in the same texts
  that state the doctrine at its hardest.


  What did our neighbours say about us? That we washed people twice. That
  our country members were violent wanderers. That we were the party of a
  man rather than the church of Christ - and one of our own petitions,
  signed by our own bishops, gave them that phrase to use. And to
  outsiders, the strangest thing of all: two of every office in every
  town, two bishops, two altars, two names for the same God, and not one
  point of doctrine between them.
positions:
- the claim that the empire's arrival changed what the church was is not a charge we answer but the case
  we were founded to make
- persecution in our own time meant troops entering our buildings under orders to enforce unity, not concealment
  or hiding
- we rejected the Rome and Arles rulings on the ground that a court convened and enforced by a state that
  has already named the other side the church is not the church judging itself
- we used imperial machinery three times ourselves - in 313, again for our confiscated basilicas, and
  against our own breakaway party - and our record states this openly alongside the doctrine at its most
  absolute
- 'what struck outsiders was the completeness of the duplication: two bishops and two altars per town with no
  doctrinal difference between them'
tensions:
- the utterance our refusal is remembered by survives only inside an opponent's polemic, framed as a fit
  of rage, and we cannot produce it in any other form
- reading three separate appeals to imperial power as exceptions inside one principled stance, rather
  than as a series of grievances, is partly a modern frame and not a rule any text of ours sets out
- the charge that our country members were violent is attested as a charge, and its truth is not settled
  by anything independent of the polemic that makes it
relations:
- type: associated-with
  target: don.quote.donatus-quid-est-imperatori
use_note:
  means: "Donatists held that empire changed the church, met persecution as daylight seizures rather than catacombs, refused the Rome and Arles rulings, and owned three recourses to imperial power."
  not_for:
    - "a claim that Donatus's retort survives other than in Optatus's hostile framing"
    - "a claim that the charges of Circumcellion violence are settled fact"
    - "a claim that the Donatists never used imperial machinery"
    - "a claim about how Donatist councils governed and judged their own cases, which sits in don.dw.who-decides-a-disputed-case"
  years: {from: 313, to: 412}
  status: reviewed
---
Closes F3-E, the cell where this world is strongest, because the cell's
central variant ("did Constantine corrupt the church - did the empire
change what you were?") is the question this communion existed to answer
in the affirmative.

All four variants are engaged. Catacombs are answered by replacing the
picture with the documented one (`don.story.passio-donati-sermon`).
Constantine is answered from `don.term.refusal-of-imperial-legitimacy`,
including its three named exceptions, which the world's own `cautions`
item 8 insists must be stated rather than managed. The neighbours'
accusations are drawn from `don.term.rebaptism`, `don.term.agonistici`
and `don.term.pars-donati`, and the Circumcellion charge is carried as a
charge whose character is contested (`cautions` item 4).

Paired with `don.quote.donatus-quid-est-imperatori`;
reciprocal relation declared there. The text field names the quote's
hostile framing in the voice rather than leaving it to the quote record's
own `modern_lens_note`, because a reader who hears only the sentence
would otherwise be misled about how it reaches us.
