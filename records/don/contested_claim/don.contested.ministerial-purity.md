---
id: don.contested.ministerial-purity
world_id: donatism
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: seven books written to answer this doctrine - the traditor/ordination/sacrament chain as Augustine
    reconstructs it in order to refute it, and the Bagai reception turned against it
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: Petilian's own quoted rebaptism-theology arguments, the fullest surviving Donatist voice for this
    doctrine - quoted clause by clause inside the work answering them
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acta Purgationis Felicis (314/315), Appendix I - the founding traditio accusation against
    Felix of Aptungi in its own documentary form, and its unfavourable outcome
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: the seven books answering Parmenian - the earliest sustained argument against this doctrine, written
    roughly five decades after the founding events it narrates
  license: public-domain
- source_id: don.source.cyprian-epistles
  locus: the third-century North African purity theology this doctrine reads itself as continuing rather
    than departing from
  license: public-domain
claim: >-
  A sacrament's validity rises and falls on the giver's own unbroken purity. A hand that surrendered the
  scriptures under persecution cannot afterwards give what the church gives, so the ordination of Caecilian
  by Felix of Aptungi conveyed nothing, and everything flowing from that line is void - which is why this
  communion exists at all, and why recognising the rival's sacraments has never been available as a term
  of peace.
held_against:
- The founding accusation's own documentary record tells against it. The Acta Purgationis Felicis (314/315),
  the formal proconsular inquiry Constantine ordered into whether Felix had handed over the scriptures,
  ended with the notary Ingentius confessing under threat of torture that he had forged the letter that
  proved the charge, and that he had forged it working for the accusing side. The confession's own extraction
  under threat is a real reason to hold the finding loosely; it is not a reason to say the inquiry found
  in this communion's favour, which it did not (don.story.acta-purgationis-felicis)
- The doctrine's own councils did not apply it to themselves. At Bagai in 394 the same body that condemned
  the Maximianists in the imagery of shipwrecked corpses received Felicianus of Musti and Praetextatus
  of Assuris back into office without rebaptism and without reordination, and Augustine made exactly that
  the centre of his case - if reordination could be waived there, on the mainstream party's own authority,
  the absolute rule did not hold even for the party that preached it most fiercely
  (don.story.bagai-reconciliation; don.gravity.rigor-against-reception)
- Augustine's counter-ecclesiology is a serious scriptural argument, not a debating move, and it was answered
  as such. At the 411 Conference he argued from the wheat and the tares that the church holds good and
  bad together until the harvest, and Emeritus of Caesarea answered him out of the same books, verse against
  verse - the record preserves a real exchange, not a refutation of a straw position
  (don.story.conference-of-carthage-411; don.figure.augustine)
- The doctrine's specific argumentative shape - precisely how the reasoning runs from traditio to invalid
  ordination to invalid sacrament - reaches this record substantially through Augustine's own refutation
  of it. Its existence and centrality are Documented independently, corroborated by the Maximianist affair's
  own presupposing logic and by Petilian's quoted words; its texture is not
  (don.gravity.ministerial-purity's own divergence_note)
- Even Petilian's arguments, this communion's fullest surviving voice on the doctrine, survive because
  Augustine quoted them clause by clause in order to answer them - clauses selected for answerability,
  not a Donatist statement of the doctrine made for its own sake (don.figure.augustine;
  don.source.augustine-answer-to-petilian)
concedes: >-
  Two things, and neither is softened here. First, the founding case is lost on its own documents: the
  one formal inquiry into the traditio charge against Felix returned a forged letter and a confessed forger
  working for the accusers, and this communion's own eventual answer to that was not that the inquiry had
  been won but that the wider traditio dispute involved far more people and incidents across that founding
  decade than one proceeding settles, and that the principle at stake did not stand or fall on one man's
  case. Second, the doctrine's own institutional practice contains a named exception it never denied -
  the Maximianist clergy taken back unrepeated - stated plainly in the same body of texts that state the
  doctrine at its most absolute. What this record cannot supply is any reasoning of this communion's own
  for holding the two together, because none survives; what it can say is that the gap was not hidden,
  and that naming it was never thought to require closing it.
divergence_partners:
- ijc.gravity.sacramental-institutional-tension (world imperial-juridical) - the closest comparable position
  in the fleet, and a genuine divergence rather than a thematic echo. That world holds two grounds of authority
  apart and never merges them, authority from sanctity and sacrament against authority from office and
  position, and its own record states that a reconstruction which resolves the tension has failed the world.
  This claim resolves the identical tension absolutely in favour of the first ground and makes the resolution
  the reason a whole parallel church exists. The Imperial and Juridical world carries no contested_claim
  on the question - its divergent position sits in that Tensional gravity record - and this entry names
  the gravity rather than manufacturing a contested_claim pairing that does not exist.
- ijc.contested.office-holder-scope (world imperial-juridical) - a real, narrower divergence about what
  an office is. That claim holds that a juridical, office-centred Christianity was what ordinary Christians
  of Rome, Milan and Constantinople actually lived, and concedes only that the record's silence about ordinary
  believers is a fact about transmission. This claim holds that office without personal purity is not office
  at all - the same question about what qualifies a man to act for the church, answered from the opposite
  end.
relations:
- type: associated-with
  target: don.gravity.ministerial-purity
use_note:
  means: "On the Donatist claim, a sacrament depends on the giver's purity, so Felix's ordination of Caecilian conveyed nothing and the rival's sacraments are void."
  not_for:
    - "a claim that the Acta Purgationis Felicis proved Felix guilty of handing over the scriptures"
    - "a claim that the doctrine was applied without exception, since Bagai received Maximianist clergy back without rebaptism"
    - "a claim that Augustine's counter-ecclesiology was only a debating move"
  years: {from: 311, to: 439}
  status: provisional
---
Built for the Table Readiness Round from the cleared Doc_04 SS3.1 (candidate G1, six of six PASS,
classified Primary at SS4, with the core-doctrine/argumentative-texture divergence flagged rather
than smoothed) and Doc_07 SS6's own Integrative Observation, which states the concession above in
this world's own construction record before any opponent states it: an absolute conviction and a
named, undenied exception held in the same breath, without experiencing that as contradiction. Held
for don.gravity.ministerial-purity per this step's Primary-gravity minimum; associated-with recorded
reciprocally on that gravity record in the same pass.

WHY THE FELIX INQUIRY LEADS held_against RATHER THAN THE AUGUSTINIAN ARGUMENT. The strongest thing
held against this doctrine is not a theological counter-position but a document from this world's own
founding decade, and don.story.acta-purgationis-felicis already carries it at full strength with its
own reason for keeping it: the unfavourable finding is the point. Placing it first here follows that
record rather than reversing its emphasis for the sake of a tidier claim. The torture caveat is
carried with it, in the same sentence, exactly as that story record carries it - a reason to hold the
finding loosely, never a reason to reframe it as a win.

WHAT THIS RECORD DELIBERATELY DOES NOT ASSERT. Optatus's own positive counter-doctrine of sacramental
validity - that the sacraments are Christ's and the minister only a worker - is not stated in
held_against above, because no compiled record in this world's corpus carries that argument at a
verified locus, and this step did not reopen the Optatus text to check it. What IS carried is what
this world's own records attest Optatus and Augustine actually arguing: Optatus as the earliest
sustained answer to Parmenian written five decades after the founding events, Augustine as the
wheat-and-tares argument answered on the record at 411, and the Bagai reception which Augustine
turned into his central case. A future pass that reads Optatus Book V directly could strengthen this
record's held_against; until then the absence is named rather than filled by a plausible-sounding
generic opposition.

CONFIDENCE. formation_confidence Contested, matching every other contested_claim in this fleet: the
doctrine's existence is Documented and is not what is contested here - what is contested is whether
the doctrine holds, and this world's own record supplies the strongest material against it.
citation_specificity B, verification_state verified-via-authority: the sources cited are read through
this world's already-compiled story, figure and gravity records rather than reopened at their own
loci in this pass. canon_cells left empty, matching this world's records generally.
