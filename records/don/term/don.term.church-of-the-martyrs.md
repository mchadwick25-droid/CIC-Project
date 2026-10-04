---
id: don.term.church-of-the-martyrs
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
- F6-E
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: 'The self-understanding is Documented -- it is what the three Donatist-voiced martyr texts
    and the annual commemoration are for. What is thinner is the phrase itself: no vendored passage in this build
    quotes a fixed Latin title, and ''the Church of the Martyrs'' is the field literature''s standing summary
    of the self-description rather than a checked quotation from a Donatist text. Doc_06 SS1 also records that
    this term''s full depth is deliberately carried inside the Martyr/Martyrdom Tier-1 entry rather than developed
    separately, so this record is a pointer to that depth as much as an entry in its own right.'
sources:
- source_id: don.source.passio-marculi
  locus: the community narrating its own persecution as vindication
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: the commemorative occasion this self-description is preached at
  license: public-domain
- source_id: don.source.passio-isaac-et-maximiani
  locus: Macrobius's letter to the Carthage congregation
  license: public-domain
- source_id: don.source.frend-the-donatist-church
  locus: the standard modern account of the self-description
  license: in-copyright-consultation
retrieval:
  tier: 2
  retrieve_when:
  - a participant asks what this communion called itself, in positive rather than oppositional terms
  - a participant asks why suffering counted as proof of being the true church
  prefer_instead:
  - the question is about a specific martyr or a specific persecution episode rather than the self-description
relations:
- type: associated-with
  target: don.term.martyr-martyrdom
- type: associated-with
  target: don.term.deo-laudes
plain_meaning: This is what we call ourselves, and not for effect. We are not a group defined by what we left.
  We are the one communion that has actually suffered, and gone on suffering, for the truth.
world_word: the Church of the Martyrs
false_friend:
- a boast about spiritual superiority, rather than a claim about what actually happened
- a title claimed by any persecuted church, when the point here is who did the persecuting
- a fixed formal Latin title -- what survives is the self-understanding, not a quoted slogan
senses:
  informational: 'The positive counterpart to every refusal. Where ''Caecilianist'' and the rejection of ''catholic''
    say what this communion will not concede, this says what it claims to be: the body proved true by having paid.
    It ties the martyr cult, the annual commemoration and the purity doctrine into one self-description -- suffering
    as the visible evidence that the doctrine is held rather than merely stated.'
  evidential: The underlying self-understanding is about as well attested as anything in this world, because it
    survives in texts this communion wrote itself. The phrase used to name it is a modern scholarly summary, and
    this record does not present it as a quotation.
  personal: 'Held against the rival''s position this is not a boast but an argument: one side has the emperor''s
    favour, the other has its dead. Doc_05 SS2 places this at the centre of what belonging felt like.'
  translational: '''Every church honours its martyrs'' -- but few define themselves by the claim that the other
    church''s favour with the ruling power is exactly what disqualifies it. That inversion is what this name is
    doing.'
quick_meaning: The Church of the Martyrs -- what we are, not merely what we left.
distortion_risk: medium
use_note:
  means: "This is the Donatist self-understanding as the one communion that has truly suffered for the truth, rather than a group defined by what it left."
  not_for:
    - "a claim that it is a boast of spiritual superiority rather than a claim about what happened"
    - "a claim that any persecuted church could take the title regardless of who did the persecuting"
    - "a claim that it was a fixed formal Latin title or quoted slogan"
    - "a claim about the commemorations and texts that carry it as a pattern, which sit in don.gravity.church-of-the-martyrs"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 012 (Tier 2; full depth deliberately carried inside the Martyr/Martyrdom Tier-1 entry rather than promoted). Slug uses the Latin form for id stability; world_word keeps the English, since no fixed Latin title is quoted anywhere in the build.
