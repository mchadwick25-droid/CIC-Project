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
  locus: De Mortalitate 1-2; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 46695-46728
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
telling: 'A dreadful plague broke out in our city and went from house to house, killing countless people every day.


  Everyone shuddered and fled the infection, and they even put their own dying friends out of their homes. Soon the bodies of many were left lying all over the city as mere corpses.


  Then we gathered in one place, where our bishop spoke to us first about mercy and then went further. There was nothing special, he said, about caring only for our own people. To be perfect, we had to love even our enemies and pray for those who persecute us. God makes His sun rise and sends rain to feed the seed, for strangers as well as for His own people. If we call ourselves His children, we should show it by being good the way He is good.


  So many who were too poor to give money gave their labour instead, and good was done to everyone, not only to our own people.


  Our deacon Pontius judged that more was done here than in the story of Tobias, who gathered up only the dead of his own people.'
absent_detail: Whether the persecutors themselves were among those helped is not something Pontius says
  one way or the other, and no source outside him describes the relief operation at all. No pagan Carthaginian
  of ours left a word about being helped by us during this epidemic.
modern_contrast: 'A modern listener may hear ''love your enemies'' as a maxim available anywhere. What
  is not available everywhere is the specific setting: said to a frightened congregation, in a city where
  the dead were left where they fell, by a bishop who would himself be executed a few years later.'
heart: Pontius says that when plague struck and people put out their own, Cyprian taught us to love even our enemies. Then good was done to all people, not only to our own.
events:
- line: A dreadful plague broke out and carried off countless people every day.
  rests_on: A dreadful plague broke out
  essential: true
- line: People fled the contagion and put out their own; corpses lay all over the city.
  rests_on: wickedly put out their own people
  essential: true
- line: 'When we were gathered, our bishop preached: caring only for our own is nothing remarkable.'
  rests_on: There was nothing remarkable, he told us, in caring for our own.
  essential: true
- line: We must love even our enemies and pray for our persecutors, as God gives sun and rain beyond His own people.
  rests_on: loving our enemies and praying for those persecuting us
  essential: true
- line: Cyprian said we ought to answer to our birth.
  rests_on: We ought, he said, to live up to our birth
  essential: false
- line: The poor gave their labour; good was done to all people, not only to the household of faith.
  rests_on: Relief was given to everyone
  essential: true
- line: Pontius says more was done here than is recorded of Tobias, who gathered the dead of his own race only.
  rests_on: more was done, he writes, than is recorded of Tobias
  essential: false
telling_short: 'A dreadful plague broke out and killed countless people every day. Everyone fled the infection, and they even put their own dying friends out of their homes.


  When we gathered, our bishop told us that there was nothing special about caring only for our own people. We had to love even our enemies and pray for those who persecute us.


  So good was done to everyone, not only to our own people. Our deacon Pontius judged that more was done here than in the story of Tobias, who had gathered the dead of his own people only.'
telling_medium: 'A dreadful plague broke out in our city and went from house to house, killing countless people every day. Everyone shuddered and fled the infection, and they even put their own dying friends out of their homes. Soon the bodies of many lay all over the city, left as mere corpses.


  When we gathered, our bishop told us that there was nothing special about caring only for our own people. We had to love even our enemies and pray for those who persecute us. God makes His sun rise and sends rain for strangers as well as for His own people. If we call ourselves His children, we should show it by being good the way He is good.


  So many who were too poor to give money gave their labour instead, and good was done to everyone, not only to our own people.


  Our deacon Pontius judged that more was done here than in the story of Tobias. Tobias had gathered up the dead whom the king had killed, but only those of his own people.'
telling_long: 'A dreadful plague broke out in our city and went through the houses one after another. Every day it struck without warning and killed countless people, each one in his own home.


  The whole city was afraid, and people shuddered and fled the infection. They even put their own dying friends out of their homes, as if putting out the dying could keep death out as well.


  Soon the bodies of many lay all over the city, left as mere corpses. Anyone who walked past could see that the same death would come to him in his turn, and the sight called for pity. But no one cared for anything except his own gain, however cruel. No one did for another what he would want done for himself.


  In those days our bishop also wrote to us about all these deaths. Many of us kept a steady mind and a firm faith, but some were shaken because their minds were weak or their faith was failing. So he reminded us that the Lord had warned of wars, famines, earthquakes and plagues, so that they would not take us by surprise.


  When we gathered, our bishop first spoke about mercy, using examples from the holy readings to show how much kind deeds count with God.


  After that he went further, and told us that there was nothing special about caring only for our own people. To be perfect, we had to do more than any tax collector or pagan does, and overcome evil with good. We had to show mercy the way God shows it, and love even our enemies and pray for those who persecute us.


  God makes His sun rise and sends rain to feed the seed, for strangers as well as for His own people. If we call ourselves His children, why do we not follow the example of our Father? We were born of God, he said, so we ought to act like it. When the Father is good, His children should show they are His by being good the way He is good.


  So the work began, and the tasks were shared out to suit each person and his place among us. Many who were too poor to give money gave their own labour instead, and that work was worth more than any money. Good was done to everyone, not only to our own people.


  Our deacon Pontius set this beside the story of Tobias, a man known for his great kindness. He judged that more was done in our city, and he asked Tobias to forgive him again and again for saying so. Tobias must admit, Pontius wrote, that much was possible before Christ came but more after, since all is made complete in the time of Christ. When the king killed people and threw out their bodies, Tobias gathered up the dead, but he gathered only those of his own people.'
---
Derived from Story-Chunks/lpcstory002_the-plague-and-the-enemies.md, recast into first-person register. The epidemic description and Cyprian's reported address are in the Life and Passion of Cyprian by Pontius, in cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, several thousand lines after the passage lpcstory001 uses.
