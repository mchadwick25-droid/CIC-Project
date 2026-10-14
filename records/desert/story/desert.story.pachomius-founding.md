---
id: desert.story.pachomius-founding
world_id: desert-monasticism
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I, F3-I]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the broad outline (founding, vision, Rule, growth into a federation) - Contested for recension-specific incident detail, matching desert.force.formation-at-scale's own basis. The vision and brass-tablet legend are told here as Palladius reports them (ch. XXXII), a vendored, hagiographic account; the brother-John detail is told as the Lives tradition carries it (desert.source.pachomian-corpus), whose incident-level reliability this build does not independently adjudicate, matching desert.figure.pachomius's own hedge for the identical claim. Palladius's own population figures (seven thousand men, thirteen hundred in the first house) are his own present-tense report, decades after Pachomius's death, and should be read as an order-of-magnitude indicator from an interested witness rather than a precise count, per that source's own AUTHOR GRAVITY caution; the death-time house count (nine for men, two for women) and the 'low thousands' membership estimate are Doc_01 SS2.1's own claims, which state the same order-of-magnitude caution for the membership figure specifically."
sources:
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. XXXII - the vision, the angel's command, and the brass tablet, in Clarke's translation"
  license: public-domain
- source_id: desert.source.pachomian-corpus
  locus: "the founding narrative's own further detail (brother John, further companions), per this source's own standing discipline for incident-level Lives material"
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how a solitary practice became a shared, rule-governed community"
  - "participant asks who held authority and how anyone came to have it"
  - "participant asks how this world's practice worked at scale, for many rather than one"
relations:
- type: illustrates
  target: desert.gravity.koinonia
- type: associated-with
  target: desert.figure.pachomius
- type: associated-with
  target: desert.force.formation-at-scale
- type: associated-with
  target: desert.gravity.authority-tension
- type: associated-with
  target: desert.quote.pachomius-angel-tablet
- type: associated-with
  target: desert.quote.rule-for-the-weak
- type: associated-with
  target: desert.story.angel-hands-the-tablet
narrative_tier: 1
narrative_tier_justification: "Tier 1 (Documented Historical Narrative) for the founding's broad outline and datable range; the vision and brass-tablet legend inside it carry Palladius's own hagiographic frame, which this record's own tellable_as and text mark rather than present as neutral incident report."
tellable_as: 'how a hermit''s life became a rule for many: an angel, a brass tablet, and thousands of monks'
text: >-
  The tradition tells that Pachomius, already far along in the solitary life, sat one day in his
  cave when an angel came to him. The angel said: you have ordered your own life well, so there
  is no need to go on sitting in your cave. Go out now, gather the young monks, and live with
  them. And the angel gave him a tablet of brass with a rule written on it. Each was to eat and
  work according to his own strength. The strong were to be given the harder tasks, and the weak
  what they could manage. The community was to be divided into sections, each marked by a letter
  of the alphabet. The head of the house could then ask after any section by its letter alone.
  It was a private code, and only the spiritual knew its meaning. A stranger from a house with a
  different rule could not eat or drink with them, unless he was truly on a journey. A newcomer
  who meant to stay could not enter the sanctuary for three years. Pachomius, they say,
  protested that the prayers set down were too few. The angel answered that the rule was pitched
  for the weak, so even the little ones could keep it. The perfect, he said, have no need of a
  rule, for in their own cells they have given their whole life to God. The tradition also
  remembers that Pachomius was joined first by his own brother John, and then by others, at
  Tabennesi in the Thebaid. Writing decades after Pachomius's death, Palladius found the
  community numbering some seven thousand men across its houses, thirteen hundred in the first
  and greatest - a witness's own rough count, not a precise census. By another report, the
  community Pachomius left at his death in 346 stood at nine houses for men and two for women,
  with membership in the low thousands - likewise a rough estimate, not a precise count.
telling: "Palladius tells of a man named Pachomius, who lived at Tabennisi in the Thebaid. He says Pachomius was counted worthy of prophecies and of angelic visions. Palladius says an angel appeared to him as he sat in his cave. The angel told him he had ordered his own life well, so it was pointless to stay in the cave any longer. He was to go out, gather all the young monks, and live with them.\n\nThe angel gave him a brass tablet with a rule written on it. Each man was to eat and drink according to his strength, and his work was to match that strength. Pachomius objected that the prayers it set were few. The angel answered that he had given the rule so that even the little ones would keep it. The perfect, he said, need no rule, because alone in their cells they have given their whole lives to the contemplation of God.\n\nIn his own day, Palladius says, the monasteries that kept this rule held seven thousand men. The first and great monastery was the one where Pachomius himself had lived, and he gives it thirteen hundred members."
absent_detail: "No account here claims the vision or the tablet as verified history rather than the tradition's own remembered founding story; Palladius's own text is a hagiographic summary at one remove from the Rule's own text, not the Rule itself, and the multiple, only partially overlapping recensions of the Lives carry a genuinely unresolved version-priority debate this document does not adjudicate."
modern_contrast: "A modern reader may hear a founder receiving a revelation and scaling an organization and reach for the contemporary \"founder origin story\" genre - a visionary's master plan. This world's own record frames the angel and tablet as an answer to a real, specific problem this world faced (desert.force.formation-at-scale: how a formation demanding one extraordinary hermit's own intensity could work for many, not one man's ambition), and the vision itself carries Palladius's own hagiographic frame rather than neutral incident report."
use_note:
  means: "The tradition tells that Pachomius, sent by an angel with a brass tablet to gather young monks, founded a rule-governed community that grew to thousands."
  not_for:
    - "Presenting the vision or the tablet as verified history"
    - "Treating Palladius's population figures as precise counts"
    - "Presenting recension-specific Lives details, such as the brother John, as settled"
    - "Merging it with the iron-tablet account in desert.story.angel-hands-the-tablet"
  years: {from: 318, to: 346}
  status: reviewed
---
The vision/tablet material is verified directly against the vendored
Palladius file (cic/texts/palladius_lausiac-history_clarke1918.txt,
ch. XXXII, line 397 - the same passage desert.force.formation-at-scale
cites). The tablet's own content is paraphrased rather than quoted at
length; desert.quote.pachomius-angel-tablet carries the direct
quotation of its opening clause.

The closing sentence keeps Palladius's own present-tense report (seven
thousand men, thirteen hundred at the first house, written decades after
Pachomius's death) grammatically distinct from the death-time house
count and membership estimate, which are attributed to Doc_01 SS2.1
directly (in divergence_note, matching desert.story.antony-withdrawal's
own convention for citing that document in a story record).
The text uses Palladius's own wording,
"not allowed to enter the sanctuary." Doc_01
SS2.1's own hedge on the membership figure ("should be read as an
order-of-magnitude indicator rather than a precise census") and
Palladius's own AUTHOR GRAVITY caution on his population figures are
both carried in the compiled text.

Formation significance: directly generates desert.gravity.koinonia
(Supporting) and is the founding episode desert.force.formation-at-scale
documents. At the institutional register it shows the Rule's own origin
story: authority here is given by vision and written down, not only
earned through personal relationship, the same contrast
desert.gravity.authority-tension names.
