---
id: lpc.story.the-plague-and-the-enemies
world_id: latin-pastoral-congregational-christianity
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
use_note:
  means: "Pontius says that in the plague Cyprian preached love of enemies, and help reached beyond believers."
  not_for:
    - "a claim that the persecutors themselves were helped"
    - "a claim that any source outside Pontius describes the relief"
    - "a claim that the sermon survives in Cyprian's own hand"
    - "a claim that a pagan Carthaginian's account of being helped survives"
  years: {from: 246, to: 258}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: Widely Accepted rather than Documented because the address's own content reaches us
    only through Pontius reporting the sermon in a work written to praise the man who preached
    it -- a reported speech inside a biography of praise, not a letter in the man's own hand (Story-Chunks/lpcstory002,
    Tier Justification).
sources:
- source_id: lpc.source.pontius-life-and-passion-of-cyprian
  locus: SSSS9-10; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 27920-28000
  license: public-domain
- source_id: lpc.source.cyprian-minor-pastoral-treatises
  locus: De Mortalitate, the corroborating treatise written into the same epidemic
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how we treated outsiders or enemies
  - participant raises suffering, epidemic, or disaster
  - participant asks what we did that was visibly different from those around us
  - participant asks what Cyprian taught his people to do when plague struck the city
  prefer_instead:
  - participant is asking about martyrdom or persecution as such -- the plague was not a persecution,
    and treating it as one misreads this account
  - participant asks about healing or miracle, which this account does not contain
claim_guards: []
relations:
- type: associated-with
  target: lpc.figure.cyprian
- type: associated-with
  target: lpc.figure.pontius
- type: associated-with
  target: lpc.witness.restless-heart-and-the-unrepentant-enemy
- type: associated-with
  target: lpc.quote.a-dreadful-plague-broke-out
- type: associated-with
  target: lpc.quote.it-becomes-us-to-answer-to-our-birth
- type: associated-with
  target: lpc.quote.good-done-to-all-not-only-the-household
narrative_tier: 1
narrative_tier_justification: 'Widely Accepted. Tier 1 at the narrative level, Widely Accepted rather than Documented (Doc_09 SS3). Pontius is a named contemporary within the horizon, and the epidemic itself is independently attested -- Cyprian''s own De mortalitate was written into it. The confidence is stepped down one band because the content of the address reaches us only through Pontius, reporting the sermon in a work written to praise the man who preached it -- a reported speech inside a biography of praise is not the same evidentiary object as a letter in the man''s own hand. Not Tier 3: there is no miracle and no providential intervention, and the death-as-completion pattern is absent because nobody dies here.'
tellable_as: How our bishop met a plague by teaching us to love even our enemies, and to help everyone,
  not only our own
text: "Pontius, writing as a deacon, described the epidemic. A dreadful plague broke out, he wrote, and went from house to house through a frightened city, carrying off countless people every day, each from his own home.\n\nWhat followed was not about the disease. It was about what the city did. People shuddered and fled from the contagion, and wickedly put out their own people -- bodies left where they fell, no longer bodies but the corpses of many.\n\nAgainst that, when we were gathered in one place, our bishop preached. He began with mercy, and then went further. There was nothing remarkable, he told us, in caring for our own. Anyone does that. What would distinguish us was loving our enemies and praying for those persecuting us, in imitation of a God who makes His sun rise and sends rain to feed the seed, and shows these kindnesses to strangers as well as to His own. We ought, he said, to live up to our birth: those who are plainly born of God should not fall short of it.\n\nAnd Pontius records what followed. The poor among us, who had no money to give, gave labour instead. Relief was given to everyone, not only to those of the household of faith. Pontius reaches for a comparison and finds it wanting -- more was done, he writes, than is recorded of Tobias, who gathered up the dead of his own race only."
telling: 'Our deacon Pontius tells of the sermon and the help that followed in his life of our bishop. He wrote it in praise of the man who preached.


  "Afterwards there broke out a dreadful plague," he wrote. It went through the houses of the trembling city one after another, carrying off countless people every day.


  Everyone shuddered and fled, Pontius says, and shunned the contagion. They wickedly put out their own friends. All over the city there lay no longer bodies but the corpses of many.


  When we were gathered in one place, our bishop preached. He began with the good that mercy does, and then went further. There was nothing remarkable, he said, in caring only for our own.


  To be perfect, we must do more than the tax collector or the pagan. We must love even our enemies, and pray for those who persecute us. God makes His sun rise and sends rain to feed the seed. He shows these kindnesses not only to His own people. We ought, Cyprian said, "to answer to our birth."


  Many who were too poor to give money gave their own labour instead. So, Pontius says, good was done to all people, not only to those of the household of faith.


  More was done, Pontius says, than is recorded of Tobias. Tobias gathered the bodies of those the king had killed, but only those of his own race.'
absent_detail: Whether the persecutors themselves were among those helped is not something Pontius says
  one way or the other, and no source outside him describes the relief operation at all. No pagan Carthaginian
  of ours left a word about being helped by us during this epidemic.
modern_contrast: 'A modern listener may hear ''love your enemies'' as a maxim available anywhere. What
  is not available everywhere is the specific setting: said to a frightened congregation, in a city where
  the dead were left where they fell, by a bishop who would himself be executed a few years later.'
heart: Pontius says that when plague struck and people put out their own, Cyprian taught us to love even our enemies. Then good was done to all people, not only to our own.
events:
- line: A dreadful plague broke out and carried off countless people every day.
  rests_on: Afterwards there broke out a dreadful plague,
  essential: true
- line: People fled the contagion and put out their own; corpses lay all over the city.
  rests_on: They wickedly put out their own friends.
  essential: true
- line: 'When we were gathered, our bishop preached: caring only for our own is nothing remarkable.'
  rests_on: There was nothing remarkable, he said, in caring only for our own.
  essential: true
- line: We must love even our enemies and pray for our persecutors, as God gives sun and rain beyond His own people.
  rests_on: We must love even our enemies, and pray for those who persecute us.
  essential: true
- line: Cyprian said we ought to answer to our birth.
  rests_on: to answer to our birth.
  essential: false
- line: The poor gave their labour; good was done to all people, not only to the household of faith.
  rests_on: good was done to all people, not only to those of the household of faith.
  essential: true
- line: Pontius says more was done here than is recorded of Tobias, who buried only his own race.
  rests_on: More was done, Pontius says, than is recorded of Tobias.
  essential: false
telling_short: 'Our deacon Pontius tells this in his life of our bishop, written in praise of the man who preached.


  "Afterwards there broke out a dreadful plague," he wrote. Everyone shuddered and fled from the contagion, he says, and wickedly put out their own friends.


  When we were gathered in one place, our bishop Cyprian preached. There was nothing remarkable, he said, in caring only for our own. We must love even our enemies, and pray for those who persecute us.


  Then, Pontius says, good was done to all people, not only to those of the household of faith.'
telling_medium: 'Our deacon Pontius tells this in his life of our bishop, written in praise of the man who preached.


  "Afterwards there broke out a dreadful plague," he wrote. It carried off countless people every day. Everyone shuddered and fled from the contagion, he says, and wickedly put out their own friends. Over the whole city lay no longer bodies but the corpses of many.


  When we were gathered in one place, our bishop preached. There was nothing remarkable, he said, in caring only for our own. We must love even our enemies, and pray for those who persecute us. God makes His sun rise and sends rain to feed the seed, and not only for His own people. We ought, Cyprian said, "to answer to our birth."


  Many who were too poor to give money gave their own labour instead. So, Pontius says, good was done to all people, not only to those of the household of faith. More was done, he says, than is recorded of Tobias. Tobias gathered the dead of his own race only.'
telling_long: 'Our deacon Pontius describes these events in his life of our bishop Cyprian. He wrote it in praise of the man who preached, so we hear the sermon as Pontius reports it.


  "Afterwards there broke out a dreadful plague," he wrote. It invaded every house of the trembling people, one after another. Day by day, with sudden attack, it carried off countless people, each from his own house.


  Everyone shuddered and fled, Pontius says, and shunned the contagion. They wickedly put out their own friends, as if shutting out the dying could shut out death itself.


  Over the whole city lay no longer bodies but the corpses of many. The sight of them asked passers-by for pity, since the same lot would in turn be theirs. No one cared for anything but cruel gain, Pontius says. No one did to another what he wished done to himself.


  When the people were gathered together in one place, our bishop preached. First he urged the benefits of mercy. He used examples from divine lessons to show how much kindness counts with God.


  Then he added that there was nothing remarkable in caring only for our own. Anyone who wanted to be perfect had to do more than the tax collector or the pagan. He had to overcome evil with good, and show a mercy like the mercy of God.


  So, he said, we must love even our enemies, and pray for those who persecute us, as the Lord teaches. God makes His sun rise and sends showers to feed the seed. He shows these kindnesses not only to His own people, but to strangers too.


  If a man claims to be a son of God, Cyprian asked, why does he not follow the example of his Father? We ought, he said, "to answer to our birth." Those clearly born of God should not fall short of it. The good Father should be seen in His children, when they copy His goodness.


  Pontius thinks that if the pagans had heard these words, they would probably have believed at once. Then he asks what a Christian people should do, whose very name comes from faith.


  So the work was shared out according to each person''s character and rank. Many who were too poor to give money gave their own labour instead. Pontius counts that service dearer than all riches.


  So, Pontius says, good was done to all people, not only to those of the household of faith. More was done, he says, than is recorded of the matchless kindness of Tobias.


  Tobias must forgive this, Pontius says, again and again. Much could be done before Christ, but more could be done after Christ, since all fullness belongs to His times. Tobias gathered those the king had killed and thrown out, but only those of his own race.'
---
Derived from Story-Chunks/lpcstory002_the-plague-and-the-enemies.md, recast into first-person register. The epidemic description and Cyprian's reported address are in the Life and Passion of Cyprian by Pontius, in cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, several thousand lines after the passage lpcstory001 uses.
