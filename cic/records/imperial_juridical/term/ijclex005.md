---
id: ijclex005
world_id: imperial-juridical-christianity
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: Imperator intra Ecclesiam, non supra Ecclesiam
aliases:
- the emperor is within the Church, not over it
- Ambrose's formula
- the Auxentius sermon formula
quick_meaning: 'The emperor stands within the Church, not above it. Our bishop said it to an imperial court that was demanding a basilica. He meant that no crown, whatever its power, can command what belongs to the altar.'
world_meaning: 'They asked for a building. We did not give it, and our bishop told them why, standing
  where he could be heard: the emperor is a son of the Church, not her master. He may ask what any believer
  may ask. He may not command what no believer may command. A palace belongs to the emperor; a church
  belongs to God''s priest to guard, and a priest who hands it over because a soldier stands at the door
  has not kept faith, whatever the soldier''s own rank.


  We do not say this because we deny the emperor''s own real power — we know exactly how real it is; soldiers
  were sent, and we sat inside those walls through a night not knowing if they would be sent again with
  orders to take the building by force rather than merely surround it. We say it because power and rightful
  command are not the same thing, and a bishop''s own office carries a claim that does not bend simply
  because the one making the opposing claim commands an army. What we could offer against that army was
  not a weapon. It was the plain refusal to leave, sustained, through that night, by singing together
  the way the Eastern churches had long sung and we had not yet learned — so that fear had something to
  stand inside besides itself.


  This is not, for us, a claim about grand primacy or ancient sees. It is a narrower and, we think, no
  less serious claim: that within the walls where the faith is kept, the final word does not belong to
  whoever holds the greater force outside them.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This formula names the one thing *communio* and *primatus* alone
  cannot fully account for — a limit on imperial command asserted from inside a single bishop''s own sacramental
  office, not from a see''s own accumulated institutional rank; a participant who understands this term
  understands why this world''s own record shows real limits on the alliance between throne and altar
  even at the height of that alliance''s own institutional confidence.'
distortion_risk: This world's own actors are not proposing separate spheres at all. The emperor remains
  fully inside the Church's own life, subject to its discipline as any believer is — the claim is not
  that the two institutions should be kept apart, but that one of them, precisely because he stands *inside*
  the other rather than above it, cannot command what belongs to it.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how a bishop could stand against an emperor
  - conversation touches the 386 Milan basilica standoff or the Thessalonica/Callinicum episodes
  - participant asks whether the church in this world was simply an arm of the state.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the conversation concerns Strand A's or Strand B's own claims specifically, which rest on a
      different ground entirely (retrieve primatus or presbeia instead).
  force_llm_vote: false
sources:
- source_id: srcIJC07
  author_gravity_note: Ambrose's own *Sermo contra Auxentium*, preached during the 386 standoff itself.
- source_id: srcIJC08
  author_gravity_note: Augustine's *Confessions* 9.7, used narrowly here as eyewitness testimony to the
    congregation's own conduct that same crisis (Doc_02 §1) — not as evidence of Augustine's own formation,
    which belongs to a different world. **Author Gravity note:** this formula survives entirely through
    Ambrose's own account of his own confrontation — a real, disclosed limitation (Doc_02 §2) this chunk
    does not resolve by pretending independent corroboration exists for the formula's own precise wording,
    even where the underlying standoff itself is independently corroborated by Augustine.
modern_hearing: A modern participant is likely to hear this as an early instance of "separation of church
  and state" in something like its modern sense — two independent institutional spheres, each staying
  out of the other's proper business.
semantic_domain: church-state boundary formula - sacramental independence
modern_sense: '''Separation of church and state'' - two institutions kept apart; exactly what the formula
  does NOT propose (chunk Modern/World Hearing).'
period_sense: 'The emperor stands WITHIN the Church, not above it - fully inside its life, subject to
  its discipline as any believer; the claim is location, not separation: one of the two, because he stands
  inside the other, answers to the altar.'
prior_sense: 'Ambrose''s own Latin: ''Imperator enim intra Ecclesiam, non supra Ecclesiam est'' (Sermo
  contra Auxentium, 386) - the formula IS the source; wording carried per Registry row 7''s own verification
  note.'
grounding_criterion: standard
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Ambrose''s own sermon
  preached during the standoff + Augustine''s Confessions 9.7 as narrow eyewitness corroboration of the
  event (the RES parking''s own single-author honesty governs confidence). | DISTANCE: Strand C does not
  persist as a claim-stream to 451 (Doc_01 SS4''s own qualification) - bounded, single-crisis evidentiary
  base.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: 'STRAND C''S OWN VOICE (the Plural-Voices device - the third distinct voice): ''our bishop
  said this to an imperial court demanding a basilica, and meant that no crown, however real its power,
  can command what belongs to the altar.'''
field_relations:
- type: associated-with
  target_id: ijclex004
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): This formula names the one thing
    *communio* and *primatus* alone cannot fully account for — a limit on imperial command asserted from
    inside a single bishop''s own sacramental office, not from a see''s own accumulated institutional
    rank; a participant who understands this term understands why this world''s own record shows real
    limits on the alliance between throne and altar even at the height of that alliance''s own institutional
    confidence. Symmetric mirror: the communion lever.'
- type: associated-with
  target_id: ijclex011
  note: 'The formula and its ground: preached in the contested basilica during the vigil itself; symmetric.'
contested_claim_ids:
- ijcclaim003
chunk_slug: imperator_intra_ecclesiam
chunk_related_line: communio, basilica
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex005_imperator_intra_ecclesiam.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Plural-Voices Note - parked at the S2.2-equivalent; typed home per the splitter docstring] This entry is written from Strand C's own voice specifically (Ambrose's own Milan community) — a third distinct voice alongside *primatus*'s (Strand A) and *presbeia*'s (Strand B), per Doc_01's three-strand finding. This strand's own voice does not persist as an independent claim-making stream to this world's 451 close (Doc_01 §4), which this entry's own Distortion Risk and Key Sources sections already reflect in their bounded, single-crisis evidentiary base. **This is a lexicon-organization device only — see the same caution recorded in the *primatus* entry and Doc_06 §5, Open Item 4: it does not pre-decide a Representative voice or identity question.**

[Reported-Experience Status - parked at the S2.2-equivalent; typed home per the splitter docstring] Reported as the world's own self-understanding — not assessed for historical accuracy; confidence calibration applies to the historical-event layer only.

The formula's own precise wording and the congregation's own emotional experience of the standoff (fear sustained by singing, willingness to remain rather than surrender the building) rest on a single author's own account of his own confrontation (Ambrose) corroborated only for the broad event, not for every specific detail, by an independent eyewitness (Augustine) — historically uncertain at the level of precise wording and interiority, but formationally central to Strand C's own self-understanding (Doc_01 §4).

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain. CT tag not applied.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 2 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
