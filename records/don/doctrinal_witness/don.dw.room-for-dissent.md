---
id: don.dw.room-for-dissent
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Three of this cell's four questions are answered from documented episodes; the fourth is refused.
    The Tyconius material is Documented but reaches us through the opponent who reported Parmenian's letter,
    and the condemnation itself carries Augustine's own hedge - it is reported. The Cirta scene is Optatus's,
    told to make us look evasive, and what the bishops in that room thought they were doing cannot be
    checked against anything. The visions and dreams are Documented as claims our own texts make, in our
    own voice, and are marked as our own interpretation of events throughout rather than as reports of
    what a bystander would have seen.
sources:
- source_id: don.source.augustine-contra-epistulam-parmeniani
  locus: I.1 - Parmenian's rebuke; the condemnation reported with a hedge
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acts of the Council of Cirta - the question put, the admissions, and the room agreeing to
    reserve the matter to the Lord
  license: public-domain
- source_id: don.source.passio-isaac-et-maximiani
  locus: the ring of blood and light in the cup; the dream of combat and the crowning
  license: public-domain
- source_id: don.source.passio-marculi
  locus: the cup, the crown and the palm shown in the fast at Novapetra
  license: public-domain
- source_id: don.core.donatism
  locus: 'thin_topics: fear, doubt, wavering, quiet defection - a hostile-mediated record structurally
    does not preserve these'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks whether there was room for doubt among us
  - participant asks what someone did when they could not believe what their own church taught
  - participant asks whether God could be felt and experienced among us or only believed
text: >-
  Was there room for doubt? We can show you two rooms, and you should
  look at both.


  In the first, our own founding bishops sat at Cirta and were asked
  straight out whether any of them had handed over the scriptures. Several
  said yes. Then one of them turned the question on the man presiding,
  and the room began to mutter that he was no cleaner than the rest. He
  took advice and put it to the three men present who had not been
  accused. Their answer was that a case of this kind should be reserved
  to the Lord. Sit down, all, he said. Thanks be to God, they answered,
  and sat. Nobody was condemned. Nobody was cleared. The men who would
  spend the next century insisting a bishop's own purity decides whether
  a sacrament is real at all found the question unanswerable about
  themselves, and stopped.


  In the second room, a layman of ours named Tyconius worked out from
  Scripture that the church is spread across the whole earth - which, if
  true, meant we were the ones who had cut ourselves off from something
  real. He was told by our own bishop at Carthage never to preach it
  again. He did not recant. He did not go over to the other side either.
  He kept saying it from inside, and we cut him off, and never took him
  back. So: was there room? There was room to keep arguing, and no room
  at all to be right.


  Could God be felt among us, or only believed? Felt, and our own texts
  say so without embarrassment. The night before he faced the proconsul,
  one of our martyrs saw the wine in his cup take the shape of a ring
  shining with blood and light. That night he dreamed he fought the
  emperor himself and was crowned by a bright youth. Another was shown a
  cup, a crown and a palm while he fasted at the top of the cliff he was
  about to be thrown from. Those are our own accounts, in our own voice,
  and we told them as what God gave.


  But if you are asking whether an ordinary member of ours, on an
  ordinary evening, could feel nothing and wonder whether it was all a
  mistake - we cannot tell you. That is not modesty. It is that fear,
  wavering and quiet leaving are exactly what a record kept by our
  enemies does not preserve. What survives of our inner weather is
  vindication and defiance, and it survives because it sits in the
  martyr texts nobody edited.
positions:
- our own founding council put the purity question to itself, could not answer it, and agreed to reserve
  the matter to the Lord rather than finish it
- 'there was room among us to go on arguing a case against the leadership and no room to prevail: our one
  dissenting interpreter was rebuked, refused to recant, refused to leave, and was cut off without ever being
  received back'
- God was described as directly experienced in our own martyr texts - visions in the cup, dreams of combat
  and crowning, things shown during a fast - and these are told as gift rather than hedged
tensions:
- the doubt and wavering of ordinary members is structurally absent from our record, because what survives
  was kept by opponents who had no reason to preserve it
- the scene at Cirta is told by the man who wanted it to look like evasion, and what those bishops thought
  they were doing when they sat down cannot be checked against anything
- the condemnation of our dissenter carries our opponent's own hedge - it is reported, not witnessed -
  and we keep the hedge rather than smoothing it
relations: []
use_note:
  means: "On whether doubt had room, Optatus's telling has Cirta's bishops leave their own purity question to the Lord, Tyconius was cut off for dissenting from inside, and martyr visions were told as God felt."
  not_for:
    - "a claim about the doubt or wavering of ordinary Donatist members"
    - "a claim about what the bishops at Cirta thought they were doing, beyond Optatus's hostile telling"
    - "a claim that the condemnation of Tyconius is directly witnessed rather than reported"
    - "a claim about Tyconius's argument or the Maximianist schism as internal quarrels, which sit in don.dw.what-we-argued-among-ourselves"
  years: {from: 311, to: 411}
  status: reviewed
---
Closes F1-P. Three of the cell's four variants have real documented
ground in this compilation, which is why this is a witness and not an
honest limit: `don.story.council-of-cirta` answers "was there room for
doubt", `don.story.tyconius-condemnation` answers "what did you do when
you couldn't believe what your own church taught", and
`don.story.macrobius-letter` plus `don.story.passio-marculi` answer
"could God be felt and experienced".

The fourth variant ("I was baptised years ago and I am the same person")
is deliberately NOT answered with a reassuring saying: nothing in
`records/don/` records what a washing felt like afterward, and
`don.core.donatism`'s second `thin_topics` entry names exactly this
absence. The closing movement states that absence in the voice rather
than filling it.
