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
tellable_as: "how one man's own solitary path became a rule for many - a vision, a tablet, and a community that grew to thousands"
text: >-
  The tradition tells that Pachomius, already far along in the solitary life,
  sat one day in his cave when an angel came to him. The angel said: your own
  life is in order; it is enough. Go out now, gather the young monks who need
  what you have already learned, and live with them. And the angel gave him a
  tablet of brass with a rule written on it. Each was to eat and work
  according to his own strength. No one was to be forced past what he could
  bear, or excused from all discipline either. The community was to be divided
  into sections, each marked by a letter of the alphabet, so the head of the
  house could ask after any section by its letter alone - a private code whose
  meaning only the spiritual knew. A stranger from another house could not eat
  or drink among them without leave. A newcomer could not enter the sanctuary
  for three years, until his steadiness had been tested. Pachomius, they say,
  protested that the prayers set down were too few. The angel answered that
  the rule was pitched for the weak, so even the little ones could keep it -
  the perfect need no rule at all, having already given their whole life to
  God in their own cells. The tradition also remembers that Pachomius was
  joined first by his own brother John, and then by others, at Tabennesi in
  the Thebaid. Writing decades after Pachomius's death, Palladius found the
  community numbering some seven thousand men across its houses, thirteen
  hundred in the first and greatest - a witness's own rough count, not a
  precise census. By another report, the community Pachomius left at his death
  in 346 stood at nine houses for men and two for women, with membership in
  the low thousands - likewise a rough estimate, not a precise count.
absent_detail: "No account here claims the vision or the tablet as verified history rather than the tradition's own remembered founding story; Palladius's own text is a hagiographic summary at one remove from the Rule's own text, not the Rule itself, and the multiple, only partially overlapping recensions of the Lives carry a genuinely unresolved version-priority debate this document does not adjudicate."
modern_contrast: "A modern reader may hear a founder receiving a revelation and scaling an organization and reach for the contemporary \"founder origin story\" genre - a visionary's master plan. This world's own record frames the angel and tablet as an answer to a real, specific problem this world faced (desert.force.formation-at-scale: how a formation demanding one extraordinary hermit's own intensity could work for many, not one man's ambition), and the vision itself carries Palladius's own hagiographic frame rather than neutral incident report, as this record's own tellable_as and text already mark."
---
Re-derived from the prior build's cleared Doc_09a Story 1.3. The
vision/tablet material is newly and directly verified against the
vendored Palladius file this session (cic/texts/palladius_lausiac-
history_clarke1918.txt, ch. XXXII, line 397 - the same passage
desert.force.formation-at-scale now cites), a genuine improvement on
Doc_09a's own unattributed telling. The tablet's own content is
paraphrased rather than quoted at length; desert.quote.pachomius-angel-
tablet now carries the direct quotation of its opening clause.

Step4, Round 1 review Finding S6: this body previously cited
desert.quote.pachomius-angel-tablet before that record existed - built
above rather than the reference removed, since the material genuinely
supports a verbatim quote. Finding M4: the closing sentence had
attached Palladius's own present-tense report (seven thousand men,
thirteen hundred at the first house, written decades after Pachomius's
death) to a "by the time of his death" framing Palladius does not give
- corrected to separate the two claims. Finding C6: "not admitted to
full communion" corrected to "not allowed to enter the sanctuary,"
Palladius's own wording. Finding C9: this body already invoked
desert.gravity.authority-tension in prose without declaring a relation
to it - added above.

Step4, Round 2 review Finding S9: the Round 1 fix above moved the
death-time house-and-membership figure onto desert.source.rousseau-
pachomius, which does not register a membership count (its own
sources[] entry on desert.gravity.koinonia covers the house count
only, explicitly excluding population), and the compiled sentence's
"by his own account" still grammatically reattached the death-time
figure to Palladius, the nearest antecedent - reasserting exactly the
claim M4 required be detached from him. Corrected: the
rousseau-pachomius citation is removed from sources[] (koinonia's own
citation is not duplicated here), the death-time house count and
membership estimate are now attributed to Doc_01 SS2.1 directly (in
divergence_note, matching this build's own convention for citing that
document in a story record - see desert.story.antony-withdrawal), and
the compiled text is restructured so the two claims read as
grammatically distinct sentences. Doc_01 SS2.1's own hedge on the
membership figure ("should be read as an order-of-magnitude indicator
rather than a precise census") and Palladius's own AUTHOR GRAVITY
caution on his population figures are both now carried in the compiled
text, closing Finding M9's separate note that the M4 fix had dropped
Palladius's own never-precise-counts caution when it sharpened "by
report, to thousands" into an exact "seven thousand... thirteen
hundred."

Formation significance: directly generates desert.gravity.koinonia
(Supporting) and is the founding episode desert.force.formation-at-
scale documents. Answers F4-I ("How did a person actually become one of
you?") at the institutional register, and F3-I ("Who held authority
among you, and how did anyone come to have it?") with the Rule's own
origin story - authority here is given by vision and written down, not
only earned through personal relationship, the same contrast
desert.gravity.authority-tension names.

BAR SWEEP (2026-08-29, Mark: "much better thats the bar"): text rewritten to the approved sample's level - short sentences, everyday words; every claim, name, quote, hedge, and reviewed constraint kept.
