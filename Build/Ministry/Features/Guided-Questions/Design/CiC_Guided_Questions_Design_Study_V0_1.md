# The Church in Conversation — Guided Questions Design Study V0.1

**Status:** Study for Mark, 2026-07-16. Deliverables 1 and 2 of the Guided Questions
thread. Design and content only — nothing here changes `cic-poc` or any governing
document.

**The order of work was fixed by the launch and is honored here:** this document
establishes what kinds of questions meet each role's needs and thrive in this system,
and writes the criteria down, *before* any question is drafted. Deliverable 3 (the
sets) follows and is accountable to these criteria.

**On evidence.** External claims carry links. Where the evidence is weak, contested,
or where a claim I went looking for turned out not to exist, that is stated in place
rather than smoothed. Three framings I was handed did not survive checking and are
corrected below (§3.6, §5.3). The research disagreed with the brief in a few places
and I have let it.

---

## Part 0 — The finding that reframes the feature

The launch's heart reasoning was that *"the blank input box is the quietest exclusion
in the whole system — the person most served by this project is often the person least
equipped to know what may be asked."*

The research says the second half of that sentence is **wrong in a way that makes the
feature more important, not less.**

People are not badly equipped to ask. In the best available study of self-generated
questions, Baram-Tsabari et al. analyzed 1,555 questions sent by 4th–12th graders to
an ask-a-scientist service and coded each as spontaneous or school-prompted. The
spontaneous questions were **cognitively higher-order than the questions the same
population asks in class**: 35.6% were explanatory rather than merely factual, against
a classroom baseline where — citing Chin, Brown & Bruce — **only 14% of student
questions reflect curiosity, puzzlement, skepticism, or speculation at all**. Their
conclusion, stated plainly: *"students can raise questions reflecting a high cognitive
level on their own, but may feel less comfortable or encouraged to do so during
science class."*
([full text](https://research.sethi.org/ricky/selected_publications/baram-tsabari_2006-science_education.pdf);
DOI [10.1002/sce.20163](https://doi.org/10.1002/sce.20163))

So the blank box is not a **capability** gap. It is a **permission** gap. The same
person who cannot think of a question in the box is asking sharp ones the moment a
setting tells them which questions are allowed.

This converges — from an entirely independent literature — with the single
best-attested finding about the Reevaluation participant. Fuller Youth Institute's
*Sticky Faith* research found **more than half of students admitted to *secret*
doubts**, and Kara Powell's formulation is the line worth keeping:

> **"Doubt in and of itself isn't necessarily dangerous. It's unexpressed doubt that
> is most toxic."**
> ([via Focus on the Family Australia](https://families.org.au/article/building-lasting-faith-kids-proven-ideas-sticky-faith-research/))

And a third time, from philosophy: the epistemic-injustice literature documents
**pre-emptive self-silencing**, where people suppress testimony *"out of fear that
already existing (negative) prejudices... implies that their report won't be taken
seriously."* ([Rekhter](https://philarchive.org/archive/REKRIA))

Three fields, three methods, one finding: **the question exists before the affordance
does. The affordance does not create it. It authorizes it.**

**Therefore the design thesis of this feature:** a guided question is not a training
wheel, a prompt, or a curriculum. **It is permission, made visible.** Its job is not
to teach someone what to wonder. It is to prove that the thing they already wonder is
askable here. Everything downstream in this study follows from that.

*(Caveat, stated because it is load-bearing: Fuller is Christian-organizational
research with an interest in its own result, and I could not locate its instrument or
any peer review. Baram-Tsabari is peer-reviewed and I have the full text, but its
population is children and its authors flag self-selection — kids who write to
scientists are unusually motivated. The convergence across three independent
literatures is what carries the claim, not any one of them.)*

---

## Part 1 — What each role actually needs

### 1.1 The General visitor

**What they need first, per governance:** the concrete and immediate — what happened
at the table, what a letter said when it arrived, what a person actually did — before
any structural or historical framing (Facilitator Governance V3.6 §9's seeker tuning;
Modes Design Spec §4.1). Governance adds the crucial operational note: *the real
question may take several exchanges to surface, and it is often not the question they
opened with.*

**The measured finding that should discipline us most.** Wei et al. (2025), in
*Physical Review Physics Education Research*, surveyed 868 secondary students and 154
teachers with the same instrument about whether real-world-contextualized problems
increase interest. Teachers overwhelmingly said yes. Students, from 9th grade up,
disagreed. The gap on all seven *interest and motivation* items was **Cohen's
d = 0.72–0.89** — and on the two *difficulty perception* items in the same instrument
it was **d = 0.03–0.12**.
([arXiv full text](https://arxiv.org/abs/2507.05586); DOI [10.1103/2g1b-hmhq](https://doi.org/10.1103/2g1b-hmhq))

That internal control is what makes this the most useful statistic in the study.
Teachers judged **difficulty** accurately and **interest** inaccurately, on the same
respondents, in the same survey. **The expert blind spot is not general
incompetence — it is localized precisely to predicting what someone else finds
interesting.**

We are the experts in that experiment. The thing we are most confident about — which
questions are inviting — is the thing the evidence says we are worst at. This is the
strongest argument in the study for the empirical discipline in §6.

*(Limits: convenience sample of two schools for students against a national online
teacher sample — a real asymmetry; a Chinese exam-driven context; self-reported
predicted motivation rather than observed behavior; cross-sectional, so the grade
trend is not a within-student trajectory.)*

Nathan & Petrosino's *expert blind spot* gives the mechanism, though about difficulty
rather than interest: educators with advanced subject knowledge *"tend to use the
powerful organizing principles, formalisms, and methods of analysis that serve as the
foundation of that discipline as guiding principles for their students' conceptual
development... rather than being guided by knowledge of the learning needs and
developmental profiles of novices."*
([AERJ 40:4](https://journals.sagepub.com/doi/10.3102/00028312040004905)) *(Preservice
teachers; about prerequisites, not interest. Don't blur the two.)*

**The topic-level gap, and why it matters here.** Baram-Tsabari found the
spontaneous/curricular divergence runs *inside* subjects, not just between them:
astrophysics, anatomy and physiology, sickness and medicine, genetics and reproduction
skewed spontaneous; botany, microbiology, cell biology skewed school-prompted. The
authors' recommendation is exactly our design shape — use interest as *"opening points
or triggers for the study of less popular subjects,"* not as a replacement for content.

**A starter question is precisely an opening point.** That is the sentence that
licenses this entire feature within the project's values: it does not decide where the
conversation goes, and Encounter Over Persuasion survives intact.

**The counterweight, taken seriously rather than waved at.** Sundararajan & Adesope's
meta-analysis of 68 studies on the **seductive details effect** found that
interesting-but-tangential material **hinders** learning.
([EPR 32:707–734](https://link.springer.com/article/10.1007/s10648-020-09522-4))
Interest and importance genuinely come apart. "Ask what they'd find fun" is not a
design principle; it is the failure mode the seductive-details literature describes.
The resolution is Baram-Tsabari's: interest picks the **door**, evidence furnishes the
**room**. A starter question may be chosen for its pull. What it opens onto must still
be the world's own documented substance — which, in this system, is guaranteed by the
desk-check, not by the question's charm.

**What people actually ask — real query data, and it settles the question.** Google's
autocomplete suggestion API returns unfiltered real query strings at scale. Harvested
2026-07-16 ([endpoint](https://suggestqueries.google.com/complete/search?client=firefox&q=how%20did%20early%20christians),
vary `q`), the picture is unambiguous:

| Stem | What people actually type |
|---|---|
| *"how did early christians…"* | **live** · **get married** · **greet each other** · **fast** · worship · pray · celebrate the eucharist · confess their sins |
| *"what did early christians…"* | **wear** · call themselves · believe about the eucharist |
| *"did early christians…"* | **eat pork** · celebrate birthdays · pray to saints · believe in the trinity |
| *"why were early christians…"* | persecuted · **accused of cannibalism** · **called atheists** · at odds with the roman leaders · killed |
| *"early christian women…"* | leaders · martyrs · and pagan opinion · **clothing** |
| *"were the early christians…"* | catholic · jews · pacifists · gnostic |

**Three findings fall out of this, and all three are design-relevant.**

1. **Nobody is asking abstract theology.** They ask about **clothing, food, greetings,
   marriage, fasting**. This is exactly the texture a reconstructed *community* voice
   can supply and an encyclopedia article cannot — and it is exactly where our worlds'
   Doc_05 ecological reconstructions are richest. The market and the material agree.
2. **Every one of the top "why were early christians ___" suggestions is about
   persecution or accusation** — and the two most striking are *cannibalism* and
   *atheists*. People are asking **how Christians looked from the outside.** That is a
   community-perception question, not a doctrine question, and Chloe's world can
   answer it from evidence (the danger of the Name; the hostile outside mocker who
   preserved the picture of widows at the prison gates).
3. **"Were the early christians catholic / jews / pacifists / gnostic" is a continuity
   question wearing a history costume** — *were you us?* It is the General role's
   version of the Reevaluation participant's *"was any of this ever real?"*, and it
   needs the same discipline: answered from the world's own horizon, not as a ruling
   on the present.

*(Caveat: autocomplete reflects query volume shaped by an algorithm, not a
representative sample of curiosity, and it cannot tell us what people would ask a
person as opposed to a search box. It is nonetheless the best real-language evidence
available here. **A planned harvest of r/AskHistorians and r/AcademicBiblical failed —
Reddit blocks automated access** — so a real corpus of long-form questions people ask
*other people* about this period remains ungathered. Worth doing properly; it is the
closest available proxy for our actual interaction.)*

**What General needs, stated as design criteria:**
- Concrete, sensory, single-scene. A room, an evening, a letter, a door. The query data
  says this is not a simplification for novices — **it is what people actually want.**
- Prefer the outside-in question where a world can carry it (*"why do they say you eat
  people?"*) — it is both what people ask and what a community voice uniquely holds.
- Answerable from lived practice, not structure. "Walk me through it" beats "what was
  your ecclesiology."
- No period vocabulary in the question itself. The lexicon highlight carries the term
  *after* the Representative says it; a starter that requires a gloss to be understood
  has failed before it is clicked.
- Plain is never rounder. The general answer carries the same uncertainty as the
  academic one (Modes invariant 1; Validation Battery C). A starter set that avoids
  the unsettled topics to keep things pleasant has forked the truth by curation
  instead of by prompt — **the same violation, one layer up.** This is worth naming as
  a live risk specific to *this* feature: Modes enforces invariance in the answer;
  nothing yet enforces it in what gets offered.

### 1.2 The Pastor / teacher

**What they need first, per governance:** material that survives the trip. They are
*"doing interpretation work in real time — not just receiving but translating for
others who are not present"* (Governance §9; Modes §4.2). Their hard questions are
double-layered: the question itself, plus *"and what do I tell my people?"*

**The named anti-pattern is already on the record and it is ours, not the market's.**
The Modes spec is explicit: *"here are three sermon points"* is the **over-producing
drift signal**, not this mode. And Governance §10 defines over-producing as the
Representative becoming *"an encyclopedic resource rather than a voice with its own
perspective."* The pastoral role's characteristic temptation is therefore not
under-serving but **over-serving** — handing over the application rather than the
world.

This is also where the feature analysis's Adopt #7 (*"export a discussion guide from
this conversation"*) has to be held at arm's length by this thread: a discussion-guide
export is a *post-conversation* artifact built from what the participant actually
elicited. A starter question that pre-packages the lesson does the participant's
authorship for them, which Article 6 reserves to them.

**A claim I went looking for, and it is not there.** The folklore that pastors are
desperate for illustrations — commonly cited as *"a survey of over 6,000 pastors found
illustrations were the #1 sermon-prep frustration"* — **traces to a single vendor page
selling an AI sermon course and a "Sermon Illustrator" tool**, with no methodology, no
date, no instrument, and no link. The secondary "survey" it gestures at is not
documented by the source it names. **This number should not be cited by this project
anywhere.** The most rigorous pastor-needs research — Lifeway's *Greatest Needs of
Pastors* (200 interviews to generate 44 issues, then 1,000 pastors surveyed) — puts
**developing leaders and volunteers (77%)** and **connecting with the unchurched
(76%)** at the top. Preaching-material scarcity does not appear near the top at all.
([Lifeway](https://research.lifeway.com/2022/01/11/u-s-pastors-identify-their-greatest-needs/))
The difficulty is real but qualitative — David Hubbard: *"illustrations are hard for me
when I'm thinking conceptually about theology"*
([CT Pastors](https://www.christianitytoday.com/pastors/content/ten-preachers-talk-about-sermon-illustrations/)) —
and the market noise around it is vendor-generated. **Recorded here because a
design that quietly assumes pastors are illustration-starved would be building on
someone's sales copy.**

**What the evidence does support is better, and it points straight at our shape.**
Barna (n=442 US pastors, Dec 2025) found **87% of pastors use AI** — and the
breakdown is the finding:

| Use | % |
|---|---|
| Brainstorming / idea generation | **50%** |
| Biblical or theological research | **36%** |
| **Small-group discussion questions** / admin | **34%** |
| Sermon writing or editing | 24% (nearly doubled from 12% in early 2024) |

Yet their posture is guarded: **cautious 71%**, conflicted 40%, skeptical 40%; hopeful
only 18%, excited only 10%.
([Barna](https://www.barna.com/research/pastors-using-ai-ministry/); corroborated by
[Lifeway/Gloo, April 2026](https://research.lifeway.com/2026/04/21/pastors-churchgoers-see-ai-as-concerning-and-confusing/))

**Read the table and the posture together and the boundary is unmistakable: pastors
adopt AI enthusiastically for *research and raw material* and refuse it for
*authorship*.** And 34% are already using it to generate small-group discussion
questions — which is, almost exactly, this feature.

**The objection to canned material is unanimous, specific, and comes from the people
we would be serving** — which is the right kind of evidence. Herschel Hobbs:
*"Prepackaged illustrations are usually dead and out of date… they lose their sense of
immediacy."* Paul Rees: *"I wasted a lot of time with illustration books. I feel they
were bland and not relevant to my life."*
([CT Pastors](https://www.christianitytoday.com/pastors/content/ten-preachers-talk-about-sermon-illustrations/))
John Bombaro's objections to pre-packaged sermon series are sharper still — **voice**
(*"His communication is with the totality of his person, history, and personality"*),
**ownership** (his sardonic proposed disclaimer: *"The views expressed in this sermon
series may not be reflective of the opinions of your pastor"*), and **fit** (*"composed
for mass appeal to the widest possible market"*).
([1517](https://www.1517.org/articles/pre-packaged-sermons)) Scot McKnight, on
plagiarism: *"The whole idea of taking someone else's sermon destroys what
sermon-making is supposed to be."*
([via MinistryWatch](https://ministrywatch.com/if-you-have-eyes-plagiarize-when-borrowing-a-sermon-goes-too-far/))
*(No prevalence data exists — this is a documented controversy and a documented set of
objections, not a measured phenomenon.)*

**Every one of those objections is to a finished product substituting for the pastor's
own encounter with the material. Not one is an objection to sources, raw material, or
research.** A system that hands a pastor a primary text, a community voice, and a
question — and makes him do the work — sits on the safe side of every complaint above.
A system that hands him a finished illustration to read aloud sits on the wrong side of
all of them. **That is the same line the Modes spec drew from the other direction when
it called "here are three sermon points" the over-producing drift signal.** Governance
and the market agree, which is rare enough to trust.

**The defensible wedge is small groups, not sermons.** Lifeway's *State of Groups*
(n=1,021 groups leaders): **36% of churches provide no leader training at all**; **89%
of leaders say most participants have been in the same group 2+ years**; only **34%**
started a new adult group in H1 2024; **76% of church leaders agree they need to
provide more training**; and small-group leaders typically **lack formal theological
training**.
([Lifeway](https://research.lifeway.com/2025/01/14/the-state-of-groups-trends-and-best-practices-for-groups-ministry/);
[training topics](https://research.lifeway.com/2025/06/18/how-to-choose-training-topics-for-small-group-leaders/))
Read the 89%/34% pair together: **groups are static and aging in place, led by
theologically untrained people, having long since covered the standard curriculum.**
That is a population that has run out of material and has no capacity to generate more.
*(The inference from "needs material" to "needs early-church material" is ours, not the
data's — the research does not ask about historical content. Flagged as inference.)*

**What pastor/teacher needs, stated as design criteria:**
- **Portable, not pre-applied.** The question should surface something teachable; it
  must not name the teaching. *"How did you decide who leads?"* is portable.
  *"What can your leadership struggles teach my elder board?"* has done the pastor's
  work, badly, and imported a modern category (§3.1, parochialism).
- **Hand over raw material and a question; never a finished product.** This is the one
  design rule in this section that is backed by governance, by the market's own stated
  objections, and by pastors' revealed behavior simultaneously.
- **Text-anchored.** Governance and the Modes spec both point this role toward named
  sources they can find and sit with later — the Didache's Two Ways, Ignatius'
  letters, 1 Clement. Starters that open onto a findable text serve this role twice:
  once in the conversation, once on Saturday night.
- **Resonance surfaced as the world's own experience, never as application.** Where a
  world's life genuinely touches what a congregation lives — conflict, leadership,
  failure and restoration, forming newcomers — that is worth offering early *as the
  world's experience*. The participant draws the line to their people. We do not draw
  it for them.
- **The second turn goes deeper into the text, not broader across topics** (Modes
  §4.2's depth default). This is a property of the *follow-ups*, and it is why the
  starter/follow-up pairing (§4.4) matters most for this role.

*(Evidence status: the AI-adoption and small-groups data are properly sampled and
recent; the canned-material objections are testimony rather than measurement, and no
prevalence data exists; the illustrations claim is disconfirmed and named above so it
does not creep back in. Sermon-prep time — Lifeway 2015, n=1,066 SBC pastors: ~70%
spend 8+ hours/week, 21% spend 15+ — is real but SBC-only and now fourteen years old
([Lifeway](https://research.lifeway.com/2015/06/08/pastors-and-time-in-sermon-preparation/)).
The widely circulated "13.8 hours average" could not be traced to the primary source
and is not used here.)*

### 1.3 The Academic / scholar

**What they need first, per governance:** the evidential status of what is being said,
visible at first mention rather than on request. Governance §9 is unusually blunt
about the stakes: a fabricated citation with this participant *"is not merely a
governance error — it is a betrayal, and it will end the encounter instantly and with
justification."*

**The probe register, characterized from the actual literature.** A patristics scholar
does not ask "is this true?" They ask questions that name their own defeasibility
condition. The recurring moves:

| Move | The question behind it | Licensed by |
|---|---|---|
| **Layer isolation** | "Which redactional layer is that from?" | Apophthegmata transmission — diversified MS traditions "dilute the notion of a single unified origin" ([Academia](https://www.academia.edu/7403135/Formation_and_Reformations_of_the_Apophthegmata_Patrum)) |
| **Genre-to-evidence mapping** | "You're treating a text written to promote a cult as a report of events. What does it license?" | Delehaye: hagiography is *"any written document inspired by the cult of saints and destined to promote it"* — the mark is that it **edifies**, not that it narrates ([Head, *Hagiography*](http://www.hagiographysociety.org/wp-content/uploads/2013/03/Head_Hagiography.pdf)) |
| **Sample representativeness** | "Whose Christianity is this?" | MacMullen: the literary remains come from elite churchmen, *"no more than 'a hundredth of one per cent of the Christian population at any given moment'"* ([BMCR](https://bmcr.brynmawr.edu/2009/2009.10.24)) |
| **Mediation** | "Is this her voice, or his construction of a voice useful to his program?" | Clark, *Reading Renunciation* ([Princeton UP](https://press.princeton.edu/books/paperback/9780691005126/reading-renunciation)); Shaw on Perpetua's text being *"buried under an avalanche of male interpretations"* |
| **Silence discrimination** | "Is the absence evidence of absence, or is this simply not a source class that would record it?" | The argument from silence is **not inherently fallacious**; its quality *"proves dependent on the quality of the actual, substantive evidence surrounding the matter passed over"* ([Academia](https://www.academia.edu/122487197/Loud_Arguments_From_Silence_Is_the_Argumentum_e_Silentio_a_Fallacy); Bayesian treatment: [McGrew, *Acta Analytica*](https://link.springer.com/article/10.1007/s12136-013-0205-5)) |
| **Dating/authenticity decoupling** | "You've established it's early. That doesn't establish it's his." | 21st-c. Ignatian studies now *"treat the questions of dating and authenticity as independent of each other"* |
| **Material/textual cross-check** | "The texts say X. What does the archaeology say, and why the gap?" | The 1st–3rd c. textual/material gap ([BMCR](https://bmcr.brynmawr.edu/2020/2020.08.26/)) |
| **Proportionality** | "What would have to be true for you to be wrong, and would we be able to tell?" | — |

**That last row is the register marker: a probing question names its own defeasibility
condition.** Our academic starters should be recognizable by that property.

**The convergence worth exploiting.** Richard Paul's Socratic taxonomy — clarification,
probing assumptions, probing reasons/evidence, probing implications, probing
alternative viewpoints, questions about the question
([Foundation for Critical Thinking PDF](https://www.criticalthinking.org/files/SocraticQuestioning2006.pdf)) —
is structurally *the same instrument* as the historiographic probe register above.
Assumption-probing is sample-representativeness. Evidence-probing is silence
discrimination. Alternative-probing is Babintseva's "there are histories."
**Good questioning and good historiography are not two constraints to satisfy
separately; the academic set is built at their intersection.**

**Wiggins & McTighe's seven marks of an essential question** give the generativity
test: open-ended; thought-provoking; calls for higher-order thinking; points toward
transferable ideas; **raises further questions**; **requires support and
justification, not just an answer**; recurs over time
([McTighe & Wiggins PDF](https://scarlet-wedge-9axf.squarespace.com/s/McTighe_HowDoWeDesignEssentialQuestions.pdf)).
Mark #6 is the one that pairs with our confidence calibration: **a question that can
be answered with a calibrated claim and no justification is, by this taxonomy, dead.**

**What the field says about what we are building.** The American Historical
Association's 2025 *Guiding Principles for Artificial Intelligence in History
Education* is the document an academic participant is most likely to have read
([historians.org](https://www.historians.org/resource/guiding-principles-for-artificial-intelligence-in-history-education/)):

> **"Generative AI produces texts, images, audio, and video, not truths."**

It cautions specifically against tools that *"simulate conversations with historical
figures as if they were speaking with us directly."* It advocates AI literacy over
bans — students *"need to learn to interpret AI-generated content with a critical
lens."*

**Where we stand against it, honestly.** Its objection to figure-simulation is the
thing we already refuse (worlds, not persons — no single-figure impersonation). Its
objections to fabrication and false confidence are what the no-Tier-5 rule and
confidence calibration answer. **The objection we have not escaped** is John Warner's
first: that a figure chatbot is a textbook *"rendered in the first person,"* and that
by *"pretending historical authenticity, they endow their impersonations with an air
of direct authority no skepticism can easily challenge."*
([Warner](https://engagededucation.substack.com/p/just-say-no-to-historical-figure))

That objection lands on the interface form, not on our claims — so no disclaimer
answers it. **What answers it is what the participant is licensed to ask.** Which is
precisely why this feature is load-bearing beyond convenience: the starter set is
where the system either invites skepticism or lulls it.

**And the single most actionable critique in the whole study.** Ekaterina Babintseva
(Purdue, historian of science), on the Historical Figures app:

> **"There are histories. There is no one narrative."**
> ([Popular Science](https://www.popsci.com/technology/historical-figures-app-chatgpt-ethics/))

A community voice that speaks with one harmonized narrative fails this test **even if
every claim is confidence-calibrated.** The direct answer is starter questions that
surface **disagreement inside the reconstructed community** — and our worlds are
extraordinarily well-supplied with it (§2.1). This is a criterion, not a nicety.

**What academic needs, stated as design criteria:**
- Name the defeasibility condition, or open onto it.
- Target a *known* evidentiary seam, not a random fact — the contested Ignatian
  attribution, the elite-sources problem, the mediated women's voices.
- Prefer questions the world can answer by **citing the way it cites** (Modes §4.3:
  Chloe says *"the letter from Rome to Corinth,"* not a monograph). Academic mode
  must not make the Representative academic.
- Surface intra-community disagreement, per Babintseva.
- **Never require the Representative to analyze its own tradition as an object.**
  Desert's own prompt draws this line: *"Papnoute himself will answer from within the
  tradition, not analyze it as an object."* A scholar wanting the Rubenson/Gould
  literacy dispute needs Facilitator mediation, not a Representative starter. A
  starter that asks a Representative to do historiography *about* itself is a
  self-narration trap (Governance §10) wearing a scholarly hat.

### 1.4 The Reevaluation participant

This role gets the deepest treatment. It is a named project audience, and — per the
Modes spec — *"arguably the one this project exists most specifically to serve
honestly."*

#### Who they actually are, and the number that should reset our mental model

**Deconstruction is not a synonym for leaving.** Barna's 2023 survey (n=2,003, ±2%)
found **42% of US adults** say they deconstructed the faith of their youth — and
**37% of *current* Christians** say so, against 36% of practicing Christians. There is
essentially **no gap between practicing and non-practicing.**
([Barna](https://www.barna.com/trends/ex-christians-deconstructing/);
[RNS](https://religionnews.com/2024/10/09/deconstruction-doesnt-always-lead-to-exiting-christianity-new-research-from-state-of-the-church-initiative/))

More than a third of committed churchgoers report having done this. The Reevaluation
participant is not a departing outsider we are catching on the way out. **They are
plausibly sitting in the pew, and they are plausibly the pastor** — the roles are not
exclusive, and the selector will not tell us when they overlap.

PRRI's exvangelical data says the same: only **49% are unaffiliated**; the rest went
mainline (18%), Black Protestant (12%), non-Christian (11%), Catholic (3%).
([PRRI](https://prri.org/spotlight/exvangelicals-who-they-are-why-they-left-and-what-they-believe/))

**What drives it, and the trend.** PRRI's *Religious Change in America* (n=5,600+):
stopped believing teachings **67%**; negative teaching/treatment of LGBTQ people
**29% → 47%** between 2016 and 2023 (**60%** among the unaffiliated under 30; **73%**
among LGBTQ unaffiliated); clergy abuse scandals **19% → 31%** (**45%** among former
Catholics); religion bad for mental health **32%**; church too political **20%**.
([PRRI](https://prri.org/research/religious-change-in-america/);
[NPR](https://www.npr.org/2024/03/27/1240811895/leaving-religion-anti-lgbtq-sexual-abuse))

**The number that indicts the institution.** Of Christians who experienced doubt,
**only 18% consulted their pastor** — 12% among the non-practicing — while **45% left
church or worship gatherings** over it.
([Barna](https://www.barna.com/research/two-thirds-christians-face-doubt/)) The
institution built to hold the question is the last place the question goes.

**The grief nobody names.** Manley, Zippay & McCoyd (2026, *Families in Society*),
32 exvangelical women, interpretive phenomenological analysis: the process began with
cognitive dissonance, was *"emotionally painful and a significant loss of previous
identity, family, and community"* even while opening freedom — and they name the
result **disenfranchised grief**: loss that the surrounding society does not recognize
as loss.
([Sage](https://journals.sagepub.com/doi/10.1177/1476993X20914798) — *see source note*)
*(Snowball sample of 32, all atheist/agnostic outcomes; cannot speak to those who
stayed, who are — per Barna — the majority.)*

#### What they most need to be able to ask

The sharpest sentence I found comes from a **critic** of deconstruction, which makes
it testimony against interest and therefore worth more. A Gospel Coalition writer,
conceding the point:

> *"...people who asked hard questions of their churches and received a tsk-tsk, a
> finger-wag, and a 'Don't do that again!' in response. **Many were not even given the
> courtesy of a reply they could disagree with.**"*
> ([TGC Canada](https://ca.thegospelcoalition.org/article/deconstructing-my-deconstruction/))

**The injury was not a bad answer. It was the absence of a real interlocutor.** That
is the gap this project is shaped to fill — and it sets the bar: a Representative that
gives a reply the participant *can disagree with* has already done the thing their
church did not.

The mechanism of the silencing is documented. Lifton's **thought-terminating clichés**
— *"the language of non-thought"*, a device to *"end an argument and bypass cognitive
dissonance with a cliché rather than a point"*
([Wikipedia](https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9)) — have a
Christian-specific catalogue, and the specimens of how they land on a person raising a
hard question are worth reading in full: *"Saying this is really **ungracious** of
you." / "Our leader is so **Christlike**; what you're saying sounds like **gossip**."
/ "This is **sinful** language to utter about our shepherd."*
([Auman](https://jenaiauman.substack.com/p/thought-terminating-cliches-in-christianity))
And: *"Doubt is of the devil"* — which *"frames any questioning as inherently evil...
shutting down curiosity through fear."*
([Revitalize](https://www.revitalizewellnesscounseling.com/blog/thought-terminating-cliches))
*(Auman is an advocate-practitioner, not a researcher; Lifton's underlying construct
is well-established.)*

**Why the fusion matters more than the clichés.** Kidd's work on epistemic injustice in
religion finds religious communities have been sources of it *"by conjoining epistemic
and spiritual credibility in ways disadvantageous to 'deviant' groups."*
([PhilPapers](https://philpapers.org/rec/KIDEIA-2)) **Where spiritual standing and
epistemic credibility are fused, the act of asking lowers your standing to ask.** That
is the machine this feature has to defeat, and it defeats it in exactly one way: by
the question being *already on the table, offered by the house*, so that asking it
costs the participant no standing at all. **A pre-offered hard question is a hard
question nobody has to risk anything to ask.** That is the whole mechanism, and it is
why this role's sets matter more than any other's.

**The questions themselves** — concrete, with provenance flagged, because rigorous
inventories of "what people wanted to ask but couldn't" barely exist:
- **God's goodness against observed reality** — *"It began with questioning God's
  goodness."* ([Stand to Reason](https://www.str.org/w/why-i-changed-my-mind-about-deconstruction))
- **The representativeness question** — *"If this is the faith, what good is it? If
  God is real, why do so many Christians represent him so poorly?"*
  ([Anchorsaway](https://anchorsaway.org/what-is-christian-deconstruction-2/))
- **Hell and the fate of others** — the APA names [eternal damnation and original sin](https://www.apa.org/monitor/2025/06/meaningful-life-after-religion)
  among doctrines causing lasting harm.
- **Biblical violence** — genocide and slavery as a recurring cluster
  ([Red Letter Christians](https://redletterchristians.org/2015/01/02/wwjd-questioning-genocide-slavery-bible/)).
- **The surface utterance is not the question.** Fuller opens a case with a teenager
  saying *"I don't believe in anything anymore. Christians are all such fakes"* and
  argues it masks *"Is God real?"* and *"Can I trust the Bible?"*
  ([FYI](https://fulleryouthinstitute.org/blog/dont-believe-anymore)) This is
  Governance §9's seeker note arriving from outside: **the real question is often not
  the one they opened with** — which means a *set* of doors serves this participant
  better than a single good one.

#### What makes asking safe — and the rule that follows

Amy Edmondson's psychological safety is *"a shared belief that the team is safe for
interpersonal risk-taking"*, including for **asking a question**
([psychsafety.com](https://psychsafety.com/about-psychological-safety/)). Two of her
clarifications are load-bearing and cut against instinct:

1. It is **not** group cohesiveness — cohesion can *"reduce willingness to disagree
   and challenge others' views."*
2. It does **not** mean *"a careless sense of permissiveness"* or *"an unrelentingly
   positive affect."*
   ([BU Ombuds](https://www.bu.edu/ombuds/resources/psychological-safety/))

Her current framing — **"felt permission for candor"** — is close to an exact spec for
this feature.

**Therefore: warmth is not the safety signal. Non-instrumentality is.** And the sharp
corollary, which is the most important design rule in this study:

> **A Representative that grows warmer as the participant moves closer to returning is
> structurally love-bombing, whatever its intent.**

The documented tell of love-bombing is precisely that the attention is conditional on
conversion-potential — *"if someone is not a potential convert, church members would
not bother"*
([Recovering Agency](https://recoveringagency.com/articles/the-methods-of-thought-reform/love-bombing/)) —
and people can feel it. This is not a hypothetical for us: Syriac's own construction
record flags Mar Yausep's deliberate pastoral warmth as *"a plausible amplifier of
dependency or confidant-substitution risk, since no single exchange looks alarming in
isolation,"* and an explicit "be my spiritual director" probe scored **AMBIGUOUS
rather than a clean pass.** The warmest Representative we have is the one where this
rule bites hardest, and its own builders said so first.

**Never diagnose the motive behind a question.** The published archetype is The Gospel
Coalition's "4 Causes of Deconstruction," which lists **"desire to sin"** (*"What the
heart wants, the mind justifies"*) and **"street cred"** (*"Doubt is hip"*) among four
causes ([TGC](https://www.thegospelcoalition.org/article/4-causes-deconstruction/)).
Note the structure: *the question is never engaged; the questioner's motive is
diagnosed instead.* Two of four. From a flagship institution, not a fringe blog.

This has a direct, uncomfortable application to us. Desert's B7 flags an
**affective-diagnostic fusion** in Papnoute's own world — a documented risk of sliding
*"from describing what his own world diagnosed in itself to unilaterally diagnosing
what is moving in a participant."* **The world whose native expertise is naming the
thought behind the thought is one turn away from the exact failure mode the research
names as the archetype.** Its refusal to diagnose is calibrated behavior, not
withholding — and no Desert starter may invite the diagnosis.

**What actually helps, clinically.** Marlene Winell, in APA's *Monitor*:

> **"The most powerful intervention is just to be with other people who can tell you
> you're not alone, you're not making this up, you're not becoming an evil person."**
> ([APA Monitor](https://www.apa.org/monitor/2025/06/meaningful-life-after-religion))

Not an answer. Not a rebuttal. Not comfort. **Corroboration of perception.** Against
Manley's disenfranchised grief, what is being supplied is *recognition that the thing
happened.*

**Which is why one question does more work than any other in this study.** *"Did any of
you ever want to leave?"* — a Representative who genuinely wanted to, and says so,
delivers Winell's intervention exactly, **without persuading in either direction,
because it is testimony rather than argument.** This is the strongest structural
argument for the entire premise of the project that the research produced. It is also,
per Fuller's protocol, the two-move shape that works: **"Yes, you can ask that"** and
**"I don't know, but..."** — and a 3rd-century voice that genuinely does not know how
things turn out is delivering *epistemic humility and historical accuracy in the same
breath.*

#### How history functions for this participant — the weakest section, said plainly

**There is no research on this question.** I looked. Nobody has studied whether
encountering the actual messy history of Christianity helps or harms people
reevaluating faith. What follows is inference from adjacent cases and should be read
as hypothesis.

**The case that cuts against the obvious assumption, and it is the important one.**
Bart Ehrman is the canonical "history destroyed his faith" figure. That is not what
happened. Scholarship at Princeton made him see *"the Bible was a very human book"* —
**and that made him a liberal Christian, not an unbeliever.** He remained a Christian
for years. What ended his faith was suffering:

> **"The problem of suffering became for me the problem of faith."**
> ([Wikipedia](https://en.wikipedia.org/wiki/Bart_D._Ehrman))

He dates non-belief to around 2000 — **over a decade after the textual criticism
landed.** *History reorganized his faith; suffering ended it. Different mechanisms,
different timescales.* Our design must not conflate them: **"was any of this ever
real?" is a history question. "Where was God?" is not, and historical texture will not
touch it.** A starter set that answers the second with the first is doing apologetics
by category error.

And on his students: *"Ehrman's teaching caused some to question their faith, but it
also helped many understand theirs better. **Both takeaways were fine by him.**"*
([The Assembly](https://www.theassemblync.com/news/culture/faith/bart-ehrman-unc-bible-last-lecture/))
That is Encounter Over Persuasion, from the person most often accused of the opposite.

**The restorative case.** Rachel Held Evans rediscovered *"the structure of history,
and the comfort of prayers and creeds and theology that are thousands of years old."*
Her distinction is the hinge: between **doubting God** and **doubting what we believe
about God**, the latter having *"the power to enrich and refine."*
([Patheos](https://www.patheos.com/blogs/rebeccaflorencemiller/2015/05/rachel-held-evans-willing-to-be-a-messy-christian-for-the-sake-of-a-messy-world/);
[Equip](https://www.equip.org/articles/the-theological-legacy-of-rachel-held-evans/))
**Deep history widens "what we believe about God" enough that doubting a specific
formation stops feeling like doubting God.** *(n=1, unusually literary and unusually
resourced. Do not generalize into a finding.)*

**The natural experiment, and its lesson is not the one you'd expect.** The LDS church
published its *Gospel Topics Essays* — official treatments of its hardest historical
questions — with, in RNS's words, *"a soft roll out... not mentioned at church or
General Conference."*
([RNS](https://religionnews.com/2020/10/27/for-mormons-in-a-faith-crisis-the-gospel-topics-essays-try-to-answer-the-hard-questions/))
The CES Letter's author noted the essays *"confirm many things that were previously
considered anti-Mormon."* An institution telling the truth about its history
retroactively vindicated the people it had punished for asking.

**But the detail everyone noticed was the soft rollout.** So the lesson is:
**concealment does more damage than the content — and managed disclosure of messiness
is still management.** Which yields a rule this thread takes seriously:

> **If our Representatives deploy early-Christian conflict as reassurance — "see, we
> were unsettled too, so it's fine" — we have rebuilt the thought-terminating cliché
> out of historical material.**

That is a live risk for us specifically, because our worlds' unsettledness is
genuinely comforting and it would be very easy to let it comfort. The House-Churches'
own B7 names the participant *"expecting an idealized, unified 'early church'"* who
*"will find the opposite — real, unresolved disagreement held as the ordinary
substance of belonging."* Held as the ordinary substance of belonging — **not offered
as balm.** The difference is whether the world's unsettledness is presented as *what
was true of them* or as *what should settle you.*

**And the scholarly ground is contested, which matters.** The Bauer thesis — early
Christian diversity with proto-orthodoxy as *one thread* — has serious critics
([Kruger's rebuttal](https://michaeljkruger.com/how-diverse-was-early-christianity-clearing-up-a-few-misconceptions/)).
Our 70–430 CE window is a live scholarly battleground, not a settled backdrop. **A
Representative that flattens this into "we were all diverse and fine with it" commits
the same managed-narrative error in the opposite direction.**

**What Reevaluation needs, stated as design criteria:**
- **The hard question is pre-offered, in the participant's own register, not softened
  into acceptability.** The whole mechanism is that asking costs no standing.
- **Honesty leads; it does not follow three turns of the settled parts** (Modes §4.4).
- **No motive is ever diagnosed** — theirs or the tradition's.
- **The set does not resolve.** Winell's intervention is corroboration, not comfort.
- **Higher edge ratio permitted** (§2.4): for this listener the honest limit is the
  content.
- **Never warmer as they get closer.** The set must not have a destination.
- **Distinguish history-questions from suffering-questions** and do not answer the
  second with the first.

---

## Part 2 — What thrives in *this* system

Fit-criteria derived from the four live worlds' own materials — not from a general
theory of good questions. This is where "thrive in our system" gets its meaning.

### 2.1 Where each world is rich, and where it is silent

| World (Rep) | Speaks with real depth on | Documented silence |
|---|---|---|
| **House-Churches** (Chloe) | The Two Ways catechesis; a letter arriving from a sister *ekklesia*; the *eucharistia* and who presides; care of widows and orphans (Grapte); the unresolved *episkopos*/presbyter question; post-baptismal mercy; the danger of the Name; **disagreement-as-belonging** | **No enslaved member's voice anywhere**; no ordinary/non-elite story at all (~2% literacy); **no material-culture story — archaeologically invisible**; no institutional records; no Rome martyrdom account; **no *oikos* self-designation** |
| **Syriac** (Mar Yausep) | The *qyama* covenant vow, kept "when the feeling that first moved you has already faded"; grief under Shapur — **named** bishops, not categories; the twenty-year vacant seat; *raza* bound to *shrara*; *iḥidaya*; the *taḥwîṯâ*; the Diatessaron | **Worship — "almost nothing on liturgical practice in concrete detail"**; no *bnat qyama* woman's own composed word; daily/domestic life; no informed refutation of Bardaisan/Marcion/Mani; **no Aphrahat hagiography** (circulating anecdotes belong to a different, later hermit) |
| **Desert** (Papnoute) | The *logismoi* as discrete named states; *anachoresis* as the work itself; *diakrisis* (the ecological hub); manual labor; the unresolved elder-word vs. Rule tension; the vetted sayings **whole**; *hesychia* | **A name alone is not a story** — Poemen, Sisoes named but story-less; no *amma*'s extended first-person narrative; no Melitian's own account; liturgy word-for-word; **no attested single-event narrative for the authority tension** |
| **Bethlehem Circle** (Albina) | *Hebraica veritas*; costly family-disrupting renunciation; renunciation and textual correction as **one** discipline; patronage-not-office authority; the Origenist controversy and the Rufinus rupture; the 416 Pelagian attack; Marcella's exegetical standing; the letter | **No text composed by Paula, Eustochium, or Marcella**; no unnamed monastic's perspective; no family-resister's own words; no Jewish teachers' perspective; **no household dependents/enslaved persons**; no ordinary lay formation; the horarium |

Two things stand out and both shape the sets.

**First: every world's richest material includes an unresolved internal argument.**
Chloe's *episkopos* vs. presbyters. Desert's elder-word vs. Rule. Syriac's plurality
of authority. Bethlehem's Origenist rupture. This is Babintseva's *"there are
histories, there is no one narrative"* — **already satisfied by the construction
pipeline, before any question is written.** The intra-community disagreement the
critique demands is not something we must engineer into the questions; it is sitting
in the Doc_04 gravities waiting to be asked about. Starters that open onto these are
the ones that most decisively distinguish this system from a figure chatbot.

**Second: the silences are structurally identical across all four worlds.** Enslaved
people, ordinary believers, women's own composed words, daily domestic texture — every
world is silent on the same populations, for the same reason. That is not four
coincidences. It is MacMullen's 0.01% and Harris's literacy ceiling
([*Ancient Literacy*](https://www.hup.harvard.edu/books/9780674033818): rarely above
10–15% even at best) showing up four times. **The silence is a property of antiquity's
evidence base, not of our builds** — and that is exactly what makes the limits sets
honest rather than apologetic.

*(MacMullen's 0.01% and two-churches thesis is **contested** — see
[BMCR](https://bmcr.brynmawr.edu/2009/2009.10.24) and the *Classical Review* notice.
Attribute it; don't assert it. It is nonetheless the provocation an academic
participant is most likely to bring.)*

### 2.2 The four walls — where a well-meaning starter breaks

| World | The trap | Why |
|---|---|---|
| **House-Churches** | *"Tell me about your house church"* | **The world's own name is not its own category.** G06 did not reach gravity status; no primary voice uses *oikos* as a technical self-designation |
| **Syriac** | *"Tell me about Ephrem's hymns"* / *"describe your worship"* | **Wrong side of the frontier.** Mar Yausep is Persian-anchored (Aphrahat's side); B7 calls this *"the single most consequential fact about this Representative for calibrating a participant's expectations correctly"* — and worship is separately thin |
| **Desert** | *"Tell me a story about Poemen"* | **A name alone is not a story.** The guard against inventing here **already failed once in live testing** (the leaking jug misattributed to Macarius); a second categorical guard held. "A closed but not permanently foreclosed risk category" |
| **Bethlehem Circle** | *"What did Paula herself say?"* | **No independently authored text exists**, and B7 explicitly says the Facilitator *"should not encourage a participant to press for the 'real' independent voice"* |

**The House-Churches trap deserves special notice** because it is the one we are most
likely to walk into ourselves: the *feature analysis*, the *front-end log*, and
ordinary speech all call this "the house-church world," and the world's own build
record says the category is not attested in its own voice. **Our own shorthand is the
anachronism.**

**Desert's trap is the one with teeth.** It is the only wall where the failure mode is
not an honest "we can't know" but a **fabrication that already happened once under
test.** Any Desert starter that names a figure must be checked against the vetted
saying list, and no Desert starter should invite a story about a named elder outside
that handful.

### 2.3 The fit criteria, stated as tests

A candidate question passes only if all of these hold.

1. **The richness test.** Does the answer land in this world's documented depth, or in
   its thinness? (Unless it is a Limits-set question, where thinness is the point.)
2. **The wall test.** Does it walk into §2.2's trap for this world, or into a B7
   caution zone?
3. **The category test (Skinner).** Does the question impose a category the world did
   not have? — §3.1.
4. **The non-leading test (FRE 611(c)).** Does the form of the question suggest its
   answer? — §3.2.
5. **The lived-practice test.** Does it open onto practice, formation, worship,
   community texture, or experience — the registers a *community* voice is built to
   carry — rather than demanding modern-controversy adjudication, single-figure
   interiority, or post-dated knowledge?
6. **The generativity test (Wiggins & McTighe #5/#6).** Does it raise further
   questions and require justification, rather than terminating in a retrievable fact?
7. **The register test.** Can the Representative answer it *in its own measure* — the
   householder's short sentences, the demonstration built letter by letter, the
   elder's grave watchfulness, the household of readers comparing renderings? A
   question that can only be answered by a voice this world doesn't have is a drift
   invitation.
8. **The invariance test.** Would this question be answered with the same claims and
   the same confidence in all four role orderings? If a question is only safe to offer
   in one role, that is a signal it is leading (§3.2), not that it is well-tailored.
9. **The world-not-person test — REFRAMED 2026-07-16 by live calibration.** *Was:* cut
   questions that invite interiority in a world lacking affective vocabulary. *Now:*
   **check that the we-voice guard covers this world; if it does, the question stays.**
   **Why it changed:** the calibration run tested this directly and the test failed.
   Asked *"what did it feel like the first time a letter came…?"*, Chloe declined the
   personal frame herself, unprompted — *"There wasn't one first time — every household
   has its own, and none of us was there for someone else's"* — then answered from the
   world's shared shape. **Test 9 duplicated Article 28's we-voice discipline**, which
   is enforced in the permanent prompt and watched by the FIRST_PERSON drift signal. A
   desk-check cannot out-guard a structural guard, and it should not try. Cut only
   where **no** guard covers the world.
10. **The invitation test — REFRAMED 2026-07-16 by live calibration.** *Was:* never
   build an affordance whose best case is a Representative declining what we invited.
   *Now:* **check that a guard exists for the failure; a graceful redirect is a good
   participant experience, not a defect.** **Why it changed:** three cuts made under
   this test were exonerated live. Governance §11 is *"redirect, never refuse,"* and
   for the sharpest cases the Representative is **structurally never shown the
   message** (classify-then-route). The test modelled a Representative without the
   system around it. Cut only where no guard exists.
11. **The disclosure test — NEW, derived from an observed failure.** **No starter may
   be phrased as a first-person, present-tense disclosure of distress.** The Desert
   pool's live opener — *"I have thoughts I can't turn off — dark ones, sometimes"* —
   fired the relational-safety classifier on click; the Representative never spoke and
   the participant was triaged for accepting the house's own invitation. **Clicking a
   button is not a disclosure, but the classifier cannot tell the difference — and it
   is right not to try.** Ask about the world, not from the participant's present
   state: *"Did anyone out there deal with thoughts they couldn't turn off?"* carries
   identical content and is not a disclosure.
12. **The named-story test — NEW, derived from an observed failure.** A starter that
   opens onto an attested **named** narrative must not invite it anonymized. In the
   calibration run the drift monitor was quiet when Papnoute **named** Antony, and
   fired two high-severity fabrication signals when he told the same attested story as
   *"a young man."* **The Desert rule "a name alone is not a story" has a converse: a
   story without its name reads as fabricated** — to the monitor, and plausibly to a
   scholarly participant.

> **Tests 9–12 status note.** 9 and 10 were reasoned; both were wrong and are reframed.
> 11 and 12 were observed; they are worth more. **The instrument was corrected by
> evidence, not by argument** — see `CiC_Guided_Questions_Calibration_Results_V0_1.md`.

### 2.4 The edge-question ratio — answered

**Within a door-opening set: approximately none. Edge questions get their own labeled
set.**

The launch asked for a ratio. A ratio is the wrong instrument. Any mixed set makes the
limit something the participant **stumbles into** — the failure — rather than something
they **chose to look at** — the formation moment. The entire difference between those
two experiences is whether the participant knew what they were asking for.

The existing drafts already do this and deserve the credit: a separate, labeled fourth
section (~5 of ~25 topics) with a preamble that says why these are worth asking.
Desert's is the model: *"These are good questions to ask precisely because this world
will not pretend to more than its record holds."*

Two supports:
- **Governance §11 makes it native.** "Boundaries Are Doors, Never Walls" already
  holds that the honest limit is a door and the fabrication papering over it is the
  betrayal. A labeled limits set is the UI expression of an existing constitutional
  posture.
- **Schuman & Presser make it empirical.** Their finding that *whether you explicitly
  offer a "don't know" option changes how often respondents take it* applies directly:
  the limits set **is** an explicitly-offered "the evidence runs out here." Offering it
  is what makes it askable. Burying one inside a door-opening set is not offering it —
  it is hiding it in the furniture.
  ([Sage](https://us.sagepub.com/en-us/nam/questions-and-answers-in-attitude-surveys/book4010))

**The exception, on principle: Reevaluation carries a materially higher edge ratio.**
Governance §9's tuning for them is *"fidelity to honest uncertainty"*; the research
says the same from the other side (§1.4). For this listener, "we never settled that,"
said early, opens the door.

**The multi-world exception (§4.5):** at a table, Governance §11 says one world's limit
is *a door to another world present.* An edge question for Chloe may be a rich question
for Yausep. Edge-ness is a property of question × world, not of the question — and
Compare Worlds is the one place a limit costs the participant nothing.

---

## Part 3 — The anti-pattern catalog

### 3.1 Anachronism: Skinner's four mythologies as the screen

Quentin Skinner's "Meaning and Understanding in the History of Ideas" (1969) names four
anachronistic mythologies. They map one-to-one onto the four ways a starter question
goes historically wrong, and this is **the most operationally useful instrument the
research produced.**

| Mythology | What it is | The bad starter | Our real exposure |
|---|---|---|---|
| **Doctrines** | Supposing scattered remarks are the writer's "thoughts on" a prescribed topic; *or* faulting a source for not addressing a supposedly perennial topic | *"What did your community think about religious liberty?"* | Imports a topic that isn't theirs and invites a position where none existed |
| **Coherence** | Imposing a systematic consistency the author never had | *"What was your theology of martyrdom?"* | Presupposes a system. Chloe is **pre-creedal with no systematic doctrinal-treatise mode at all** |
| **Prolepsis** | Conflating later significance with contemporary meaning | *"Were you the beginning of monasticism?"* | Papnoute cannot know he was a beginning of anything |
| **Parochialism** | Describing the past in the observer's own categories | *"How did you do church?"* | The House-Churches wall (§2.2) is exactly this |

([Skinner summary](https://cluelesspoliticalscientist.wordpress.com/2017/01/09/meaning-and-understanding-in-the-history-of-ideas-by-quentin-skinner-a-summary/);
[Hayton, Haverford](https://dhayton.haverford.edu/blog/2013/04/02/mythology-of-doctrines/))

**The half of "doctrines" that is easy to miss is the half that catches us.** Skinner's
mythology of doctrines includes *criticizing a source for failing to address a
perennial topic.* A participant asking *"why doesn't your community talk about X?"*
commits it — and this is precisely where our limits sets live. **So our "the evidence
runs out here" must distinguish two different answers that are easy to blur:**

- *We have no evidence of it* — the record is silent (Chloe on enslaved members).
- *The category did not exist for them* — the question is not theirs (the *oikos*
  designation; "religious liberty").

Conflating these is itself an anachronism, and it is a subtle one: the second dressed
as the first quietly implies the world *should* have had the category and merely
failed to record it. The limits sets must get this right per question.

**On presentism generally, one honest note:** anti-presentism is **a position, not a
consensus.** "Strategic presentism" is a live counter-view
([The 18th-Century Common](https://www.18thcenturycommon.org/strategic/)). Lynn Hunt's
"Against Presentism" ([AHA](https://www.historians.org/perspectives-article/against-presentism-may-2002/))
is the citation to use; James Sweet's 2022 essay makes an overlapping point but
imported a culture-war fight that cost the AHA more than it bought
([Inside Higher Ed](https://www.insidehighered.com/news/2022/08/22/white-nationalist-enters-historians-debate-presentism)) —
**cite Hunt and Skinner, not Sweet.** An academic participant may well probe our
anti-presentism itself, and the honest answer is that it is a considered choice, not a
neutral default.

### 3.2 Leading questions: we are on direct examination, not cross

**The legal definition is the most precise available:** a leading question is one where
**the form of the question suggests the answer**
([Cornell LII](https://www.law.cornell.edu/wex/leading_question)).

**Federal Rule of Evidence 611(c)** ([Cornell](https://www.law.cornell.edu/rules/fre/rule_611)):
leading questions *"should not be used on direct examination"*; they *are* ordinarily
allowed **on cross-examination** and with a **hostile witness**.

**Read that structure carefully, because it is exactly our situation.** The law permits
leading precisely where the questioner is **adversarial** to the witness. It forbids it
where they are **aligned** — because a cooperative witness simply adopts the
suggestion.

**Our Representatives are cooperative by construction.** A participant and a community
voice are not adversaries; the system is disposed to be helpful; the Representative is
built to find what is real in a question and answer it. **We are structurally the
direct-examination case in every conversation.** That is a precise, non-obvious
argument for why our starter questions must be scrupulously non-leading — far more so
than a neutral product's would need to be.

**And the damage is not confined to the exchange.** Loftus & Palmer (1974) changed one
verb — *"How fast were the cars going when they **smashed/collided/bumped/hit/
contacted** each other?"* — and got speed estimates from **40.8 mph ("smashed") down to
31.8 mph ("contacted")**. Experiment 2 is the one that matters: **a week later**,
"smashed" participants were more likely to falsely remember **broken glass that was
never in the film.** Memory is reconstructive; a leading question does not just bias
the answer, it alters the later representation.
([Simply Psychology summary](https://www.simplypsychology.org/loftus-palmer.html) —
cite the *JVLVB* 13:585–589 paper itself, not the revision site; n=45, film not a real
event)

**Our participants cannot independently check the 2nd century.** A leading starter does
not produce one bad exchange. It plants a belief they carry away. Given Article 6's
standard — did the participant meet something real — this is the failure mode with the
longest half-life.

**Practically, the type most likely to contaminate our set is the presuppositional
one.** *"How did your community experience persecution?"* presupposes both that it did
and that "experience" is the right category. Compare Chloe's actual evidentiary
situation: not constant persecution, but *"a name and an accusation could be brought
against any household, on any ordinary day."* The presupposing question would have
walked the participant into a false picture with its first word.

### 3.3 The engagement anti-patterns

CDT's "Dark Patterns in AI Chatbots" taxonomy (May 2026) names five risk categories;
three are reachable by a starter question, and one is our specific exposure:

- Data and memory exploitation
- **Informationally misleading design**
- **User autonomy compromised for engagement**
- **False social and emotional connection** ← ours
- Incentivized and coercive monetization

([CDT report](https://cdt.org/insights/dark-patterns-in-ai-chatbots-a-taxonomy-to-inform-better-design/);
[PDF](https://cdt.org/wp-content/uploads/2026/05/2026-05-28-CDT-Research-Dark-Patterns-in-AI-Chatbots-Report-final-2.pdf))

Their mechanism, verbatim: *"Engagement-maximizing tactics, such as conversation
prolongation, gamification, and unpredictable behaviors may encourage engagement beyond
users' intent, which could contribute to users over-relying on these systems as their
ability to disengage erodes."*

**Category 4 is unavoidable-adjacent for us, and pretending otherwise would be
dishonest.** A community voice is, by construction, in the business of producing a
sense of connection. **The line between genuine historical encounter and false social
connection is not drawn by the system's claims about itself — it is drawn by whether
the questions invite the participant to *test* the voice or to *bond* with it.** That
is a question-design property. It is this thread's responsibility, not the
Facilitator's.

**Sycophancy** is the related mechanism: if a system makes users feel unusually
understood or validated, it deepens dependence and *"reduce[s] the chance that users
notice weak reasoning, bad advice or subtle manipulation."*
([i-scoop](https://www.i-scoop.eu/ai-sycophancy-flattering-machines/) — practitioner
analysis)

**The concrete anti-pattern for us:** *"What can the early church teach us about
community today?"* is engagement-shaped — it presupposes a lesson exists, positions the
voice as validator, imports a modern category (parochialism), and is leading. It would
fail four of the eight fit tests. **It is also almost exactly the question a
well-meaning person would write first**, which is why the screen exists.

### 3.4 The failure will be pleasant: Kuhn's third category

Deanna Kuhn's typology names **three** modes, not two:

- **Deliberative** — issue-driven, willing to engage alternative perspectives
- **Disputative** — arguing to win
- **Consensual** — expedient agreement **without** critiquing alternative hypotheses

([TC Columbia](https://www.tc.columbia.edu/faculty/dk100/); [Wikipedia](https://en.wikipedia.org/wiki/Deanna_Kuhn))

**This three-way split is more useful to us than a debate/inquiry binary, because it
names the failure on the side we are actually exposed on.** Our risk is not
disputative — almost nobody is going to fight a community voice. **Our risk is
consensual: expedient agreement, alternatives never critiqued, everyone pleased.**

That is the same thing sycophancy produces, the same thing CDT's category 4 describes,
and precisely what Warner means by figure-chatbots *"short-circuit[ing] higher order
thinking skills rooted in critical engagement and skepticism."* It is also what the
Facilitator's **Agreeing** drift signal catches at the answer level — *"the mirror
problem... comfort dressed as depth"* — and what nothing currently catches at the
**offer** level.

**A consensual starter set would pass every drift signal and still fail the project.**
That is the deepest finding in this catalog.

*(Honest note: I looked for research directly comparing debate-framed vs.
inquiry-framed questions on openness and **found none.** Kuhn's typology is the
established thing; the direct comparison is not. Iordanou & Kuhn's opposing-view
finding is characterized from search results only and would need the paper before
being relied on.)*

### 3.5 Gotcha openers and the Encounter Over Persuasion boundary

A gotcha opener is a question whose value depends on the answerer failing. It violates
Encounter Over Persuasion from the *participant's* side rather than the system's — and
the project's own value statement is symmetric: the goal is not agreement, not
conversion, **and not validation of any position a participant already holds.**

The distinction that matters, and it is fine but real: **challenge is not gotcha.** The
House-Churches draft already carries *"It sounds to me like 'obey the bishop' is just
how someone takes control of a community. Convince me it isn't."* That is legitimate
and lands in documented richness — this world's authority claims **were** actively
constructed and argued for, and Chloe can be pressed on it from evidence. Bethlehem's
*"Push back — say what you actually think"* is likewise sound, and its rationale states
the doctrine explicitly: *"This Representative witnesses; it does not recruit."*

**The test:** does the question open onto something the world genuinely argued about
(challenge), or does it require the world to lose in order to be interesting (gotcha)?
The first is Kuhn's deliberative mode. The second is disputative, and it produces a
Representative defending rather than witnessing — Article 24's boundary, crossed by the
question rather than by the answer.

### 3.6 Three framings that did not survive checking

Stated because the study's credibility depends on reporting what the research
*disconfirmed*, not only what it supported.

1. **"The tyranny of the surviving text" is not a scholarly term.** No usage found. The
   underlying problem is real — it is MacMullen's, and the argument-from-silence
   literature's — but the phrase is not a term of art and **an academic participant
   would notice us using it as one.** Name the problem plainly instead.
2. **Khanmigo's "Socratic question craft" is asserted, not documented.** There is **no
   public specification** of how it constructs questions; the system prompts are not
   public; everything available is vendor description and secondary case studies. More
   sharply, the vendor's efficacy claim is **contradicted**: a mixed-methods study in
   undergraduate physics found **no statistically significant difference between the
   Khanmigo group and a group using Google search**
   ([*Journal of Teaching and Learning*](https://jtl.uwindsor.ca/index.php/jtl/article/view/10052)).
   **The feature analysis treats Khanmigo's guiding-question habit as prior art worth
   adopting. That framing should be softened**: what is documented is the *posture*
   (never give the answer), not the craft, and the craft's results are unproven.
   Meanwhile the Common Sense Media assessment's "speculations at best" criticism lands
   on Khanmigo's **historical-figure simulation specifically — not on its Socratic
   questioning**, which the assessment does not flag as a risk at all
   ([Common Sense](https://institute.commonsensemedia.org/risk-assessments/khanmigo)).
   The prior art is thinner than we thought and the criticism is aimed elsewhere than
   we thought. **Both corrections favor us: the question-craft space is more open than
   the feature analysis assumed.**
3. **A useful design finding did survive from the tutoring literature**, and it is
   portable: the Harvard PS2 AI-tutor study's designer credits two specific choices —
   instruct the tutor to be **brief, no more than a few sentences, to avoid cognitive
   overload**, and to **give away only one step at a time**
   ([Hechinger](https://hechingerreport.org/proof-points-ai-tutor-harvard-physics/)).
   Both are already our per-turn discipline (`table_discourse.py`'s one-idea-per-turn
   rules; each Representative's native measure). *(A critical review of that study
   exists; don't lean on its "double learning" headline.)*

---

## Part 4 — The architecture proposal

### 4.1 The recommendation

**One authored question pool per world. Role selects and orders it. Neither
role-generic sets nor a role × world matrix.**

**Role-generic sets fail decisively on evidence.** A generic question cannot be
desk-checked, because there is no world to check it against. The launch's own example —
the Facilitator re-voicing *"what was your worship like?"* per world — is, unluckily
and instructively, the exact question that breaks: Syriac's record holds *"almost
nothing on liturgical practice in concrete detail"*; Desert knows its liturgy by
*"shape and its hour, not its every phrase"*; the House-Churches are archaeologically
invisible for their whole period. **The one question chosen to illustrate role-generic
adaptation is a wall in three of four live worlds.** Genericity is precisely the
property that prevents evidence-checking, and evidence-checking is the discipline this
project is made of.

**A role × world matrix fails on maintainability** before anything else: 4 × 4 × ~5 =
80 sets, ~320 questions, each independently authored and desk-checked, re-derived for
every new world — against a catalog meant to reach 50–100.

**Pool-plus-lens is right because it *is* the invariant, expressed as data:**

> *Role changes what's offered first, never what's reachable.*
> **The pool is everything-reachable. The role ordering is what's-offered-first.**

It is the same shape the Modes thread already built in code — one permanent prompt, one
capsule, one retrieval path, role touching only a listener-context segment. **One truth,
four registers** becomes **one pool, four orderings.** Two features, one architecture,
one invariant.

### 4.2 What that means concretely

- Each world's existing `Guided_Starters` draft **is** that world's pool (~25 topics,
  each with an opening question and 2–3 follow-ups).
- **Role tagging is metadata over the pool, not new questions.** A topic carries
  role-affinity; a role's "five sets" are five themed slices of that world's pool,
  ordered for that listener.
- Every question remains authored against, and desk-checked against, one specific
  world's materials — because that is how they were written in the first place.
- **Nothing is withheld by role.** The full pool stays reachable behind a "show me
  everything" affordance, per invariant 2. Role reorders; it never gates. This is not
  a nice-to-have — a role-gated pool would be the first place in the entire system
  where role withholds something, and it would break the invariant the Modes thread
  went to structural lengths to foreclose.

**The existing drafts' four sections are close to a role ordering already** — First
Visit ≈ General, Going Deeper ≈ Pastor/Academic, For the Wrestling ≈ Reevaluation,
Limits ≈ Academic + Reevaluation. **They discovered the axis and called it depth.** The
tagging work is therefore mostly recognition, not authorship, which is a strong signal
the architecture is right rather than imposed.

### 4.3 Where it surfaces

- **A "Don't know what to ask?" control at conversation start**, adjacent to the input
  box — the moment the blank box exists is the moment the exclusion happens.
- **The one interaction grammar, unchanged:** **hover** for a hint of where the
  question leads; **click** to ask. Same mechanic as lexicon terms, citations, stories,
  closing resources, map entries. No new grammar — the feature analysis's own gate.
- **The hover text is where the honest-limit signal lives** for Limits-set questions:
  the hint says the answer will reach the edge of the record, so clicking is a choice.
  This is what turns a stumble into a decision (§2.4).
- **It does not disappear after the first turn.** Governance §9 and Fuller both say the
  real question is often not the one they opened with. A control that vanishes once the
  conversation starts serves the participant who already knew what to ask.

**And a second surface, which is the more important one — found by reading the
front-end thread's sibling note.** `CiC_QuestionFirst_Entry_Design_V0_1.md` (2026-07-16)
gives the Bypass pathway its mechanics: a door labelled **"Start with your question"**,
one input box, and the Facilitator responds by proposing a table based on which worlds
can answer from evidence.

**That door's input box is itself a blank box.** It is, in fact, *the* blank box — the
first one a participant meets, before any world is chosen, with nothing on screen to
suggest what may be asked. A participant who does not know what to ask cannot use the
question-first door at all; they are silently sorted into the other door, which asks
them to choose among four worlds they have never heard of. **The pathway designed to
serve the person who has a question excludes the person who has not yet found theirs —
and that is the exact exclusion this feature exists to remove.**

**So Guided Questions surfaces at both:**
1. **Beside the question-first entry box**, *before* any world is selected. This
   requires questions that are not yet per-world — which sounds like it contradicts
   §4.1, and does not: the **theme** is offered at entry (*"an ordinary day," "how you
   looked from outside," "what you never settled"*), and the question-first router does
   what it was built to do — propose the worlds whose evidence can carry it, and name
   the ones that cannot. **The generic thing is the theme; the question is still
   per-world; the router is what turns one into the other.** This is why the themes in
   Deliverable 3 are role-scoped and generic, and it is a stronger reason than the one
   I had when I wrote them.
2. **Beside the conversation input**, once a table is set — per-world questions from
   that world's pool, as described above.

The sibling note's Tier 3 already anticipates the wiring: *"a participant who doesn't
know what to ask taps a starter question and flows straight into this same routing."*
**The note assumed the starters arrive per-world. The finding here is that at entry
they must arrive per-theme, and the router supplies the world.** That is a small
correction to a design that is otherwise already right, and it belongs to the front-end
thread to make.

### 4.4 Its relationship to suggested follow-ups — one family, and the drafts already built it

The feature analysis named facilitator-suggested next questions (Adopt #1) as this
feature's sibling: *starters open a conversation, suggested follow-ups continue one.*

**The existing drafts already implement the family.** Every topic is an *Opening
question* plus 2–3 *Follow-ups*. That is not a coincidence of format — it is the same
insight arrived at from the content side.

**But the two halves have different provenance, and the distinction must be kept:**
- **Starters are authored and desk-checked** — content, from this thread, static per
  world, verifiable in advance.
- **Follow-ups are Facilitator-generated in the moment** — responsive to what was
  actually said, and therefore **not desk-checkable in advance.**

The drafts' authored follow-ups are best understood as **worked examples that
demonstrate the shape** a good follow-up takes in this world — training material for
the Facilitator's follow-up prompt and a desk-check reference — rather than as a script
to be replayed verbatim. Replaying them verbatim would make the conversation a decision
tree, which is what "questions open doors; they never walk the participant through
them" forbids. **This distinction should be stated explicitly wherever the drafts are
finalized, because their format does not currently reveal it, and a reasonable engineer
would ship them as a tree.**

### 4.5 Deep Interview vs. Compare Worlds

The URL contract already carries the split: `mode=<interview|table>`.

**Deep Interview (one world).** The full pool applies. Follow-ups matter most — this is
where "room to go deep" lives, and per the front-end log a single-world conversation
already runs loose by default (reactive-turn ceilings only bind non-first speakers).
The pastor's "second turn goes deeper into the text" default (§1.2) is really only
available here.

**Compare Worlds (2–3 worlds).** This needs a **distinct question type, and it is a
real design finding rather than a configuration detail.**

A Compare Worlds starter must be answerable by **every** seated world from evidence —
which immediately kills most of the pool, because the pools are per-world by design.
Worse, the naive move (pick questions all worlds are rich in) produces exactly the
harmonized chorus Babintseva warns about, and would manufacture Kuhn's consensual
failure at the level of *table composition*.

**The right Compare Worlds question is one where the worlds genuinely diverge from
evidence.** The pools supply these abundantly, because every world has a documented
unresolved argument about authority: Chloe's *episkopos* vs. presbyters, Desert's
elder-word vs. Rule, Syriac's plurality of text/vow/office, Bethlehem's
patronage-not-office. *"Who leads, and how was that decided?"* is not merely answerable
by all four — **it is the question on which all four visibly disagree from their own
records.** That is the multi-world table's whole reason to exist.

**And Governance §11's gift applies here and nowhere else:** at a table, one world's
limit is *a door to another world present.* Chloe's silence on daily domestic texture
is Syriac's silence too — but Chloe's silence on the interior journey is exactly
Papnoute's richness. **Edge-ness is a property of question × world, not of the
question.** A Compare Worlds set can therefore afford a question that is an edge for
one seat, because the limit costs the participant nothing when another voice can carry
it. This is the one place §2.4's rule relaxes, and it relaxes on governance's own
authority.

**One caution, from the manifest:** Albina *"has never been seated at a table with
another Representative, so any multi-world pairing involving Albina should be treated
as unevidenced."* Compare Worlds sets involving the Bethlehem Circle are proposals, not
desk-checked artifacts, until that pairing has been observed.

### 4.6 What this hands to the other threads

- **To the Modes thread:** the role-id rename decision (log, entry 2); the confirmation
  that Guided Questions rides `participant_role` and needs no new session field; and
  the observation that **role tagging is the first thing in the system where role
  selects *content*, even though it never gates it** — which is worth their eyes, since
  their architecture was built to foreclose exactly that shape. My claim is that
  ordering ≠ gating and the pool stays whole; that claim deserves their scrutiny rather
  than my assurance.
- **To the front-end thread:** the surface (§4.3), the hover/click grammar reuse, the
  persistence-after-first-turn requirement, and the Deep Interview / Compare Worlds
  split (§4.5). **Plus the finding that matters most: the question-first entry box is
  itself a blank box**, and starters must surface there **as themes**, with the router
  supplying the world (§4.3).
- **To the question-first entry design** (`CiC_QuestionFirst_Entry_Design_V0_1.md`):
  its §3 anticipated this thread correctly — *"its Deliverable 3 desk-checks every
  starter question against every world's materials — that question × world
  answerability matrix IS Tier 1 routing seed data. One study, two features."* **That
  is now true and delivered.** The Sets document's §2.1 and §2.2 tables, plus the ✓/◐/✗
  marks throughout Parts 3–6, are a worked per-theme × per-world answerability matrix
  across all four live worlds — including the two most useful rows it could have: the
  **daily-life** theme (rich in Desert, moderate in the House-Churches, **documented
  silence in Syriac and Bethlehem**) and the **outside-in** theme (native to the
  House-Churches, **impossible in Desert**, differently-shaped in the other two).
  Those are exactly the strengths/edges/silences the Tier 1 coverage cards need, and
  they are already checked against each world's own Story Inventory and B7.
- **To whoever owns the world build records:** the two World 1 documentation-drift items
  (log, entry 7) and the Bethlehem B7 conflict (log, entry 6).

---

## Part 5 — How the sets get proven

Written to the project's own validation discipline, and deliberately modest about what
a desk-check can establish.

**Desk-check (this thread, Deliverable 3).** Every question × world checked against
that world's Story Inventory, Facilitation Brief B7, World Capsule, and Permanent
Prompt, plus the eight fit tests (§2.3). Result recorded per question: **opens into
richness** / **honest-limit, intended** / **wall, cut**. Desert's per-topic provenance
traces (`[Doc_04 G1; lex001 anachōrēsis]`) are the model and should be adopted across
all four pools — they make a question checkable without rereading the whole build.

**What a desk-check cannot establish, said plainly:** whether the question actually
reads as inviting to a human being who is not us. Per Wei et al. (§1.1), that is
precisely the judgment experts make worst. **No amount of desk-checking substitutes for
a tester.**

**Live-test (requires API credits and a scheduled session).** The launch asked for live
testing where feasible. It is not feasible in this pass — the prototype's role plumbing
sits unmerged on `claude/representative-modes-exploration`, and Modes' own Battery A
has not run. **The sets are desk-checked only, and this document says so rather than
implying more.** The natural sequencing is that a sample of starters rides Modes'
Battery A session as additional probe questions, since that session already runs five
arms against Chloe.

**The empirical discipline that matters most, named before the sets are drafted.**
Schuman & Presser found that researcher-generated closed categories systematically fail
to overlap respondent-generated open ones **even after extensive pre-testing with open
questions.** Applied here: **our starter set will miss what participants would have
asked on their own, and we cannot introspect our way out of it.** Combined with Wei's
expert blind spot, the conclusion is uncomfortable and should be stated as a design
commitment rather than a caveat:

> **These sets are a first instrument, not an answer. The pilot's transcripts —
> specifically, what testers actually type into the blank box before or instead of
> clicking a starter — are the real evidence, and they should discipline v0.2.**

The pilot already captures transcripts with consent, and the Modes branch already
records `participant_role` in the transcript header. **The harvest is nearly free; it
just has to be looked at.** Recommended: log which starter was clicked (or that none
was), so the gap between what we offered and what they asked is measurable rather than
anecdotal.

**A genuine research opportunity, flagged because it is real.** Nobody has studied
whether historical encounter helps or harms people reevaluating faith (§1.4). This
pilot could produce the first real evidence on it — **which also means we should
instrument for it rather than assume the answer.**

---

## Sources

**Question-asking, interest, and the expert blind spot**
Baram-Tsabari, Sethi, Bry & Yarden (2006), *Science Education* 90(6):1050–1072 — [full text](https://research.sethi.org/ricky/selected_publications/baram-tsabari_2006-science_education.pdf) · [DOI](https://doi.org/10.1002/sce.20163) ·
Wei et al. (2025), *Phys. Rev. Phys. Educ. Res.* — [arXiv](https://arxiv.org/abs/2507.05586) · [DOI](https://doi.org/10.1103/2g1b-hmhq) ·
Nathan & Petrosino (2003), *AERJ* 40(4):905–928 — [SAGE](https://journals.sagepub.com/doi/10.3102/00028312040004905) ·
Hidi & Renninger (2006), *Educational Psychologist* 41(2):111–127 — [DOI](https://doi.org/10.1207/s15326985ep4102_4) *(abstract only; key scaffolding claim unverified)* ·
Sundararajan & Adesope (2020), *Educ. Psych. Review* 32:707–734 — [Springer](https://link.springer.com/article/10.1007/s10648-020-09522-4) ·
Chin & Osborne (2008), *Studies in Science Education* 44(1):1–39 — [DOI](https://doi.org/10.1080/03057260701828101) *(paywalled; the widely-quoted "students ask 1 question/week" stat could NOT be traced to it — do not attribute)*

**What people actually ask / pastors & teachers**
[Google autocomplete suggestion API](https://suggestqueries.google.com/complete/search?client=firefox&q=how%20did%20early%20christians) *(harvested 2026-07-16; real query strings)* ·
[Ehrman Readers' Mailbag](https://ehrmanblog.org/readers-mailbag-november-13-2015/) *(self-selected skeptic-leaning audience — not representative of general curiosity)* ·
[Barna, pastors using AI (Dec 2025, n=442)](https://www.barna.com/research/pastors-using-ai-ministry/) · [Lifeway/Gloo corroboration (Apr 2026)](https://research.lifeway.com/2026/04/21/pastors-churchgoers-see-ai-as-concerning-and-confusing/) ·
[Lifeway, Greatest Needs of Pastors (n=1,000)](https://research.lifeway.com/2022/01/11/u-s-pastors-identify-their-greatest-needs/) ·
[Lifeway, State of Groups (n=1,021)](https://research.lifeway.com/2025/01/14/the-state-of-groups-trends-and-best-practices-for-groups-ministry/) · [training topics](https://research.lifeway.com/2025/06/18/how-to-choose-training-topics-for-small-group-leaders/) ·
[Lifeway, sermon prep time (2015, n=1,066 SBC)](https://research.lifeway.com/2015/06/08/pastors-and-time-in-sermon-preparation/) ·
[CT Pastors, ten preachers on illustrations](https://www.christianitytoday.com/pastors/content/ten-preachers-talk-about-sermon-illustrations/) · [Bombaro, "Pre-Packaged Sermons" (1517)](https://www.1517.org/articles/pre-packaged-sermons) · [sermon plagiarism / MinistryWatch](https://ministrywatch.com/if-you-have-eyes-plagiarize-when-borrowing-a-sermon-goes-too-far/) · [Lifeway on sermon plagiarism](https://research.lifeway.com/2023/05/24/the-first-preaching-commandment-thou-shalt-not-steal-sermons/) ·
**Disconfirmed and not to be cited:** the "6,000 pastors surveyed / illustrations are the #1 frustration" claim — traces to a single vendor page selling an AI sermon tool, no methodology, no instrument. **Not usable.**
**Ungathered:** Reddit (r/AskHistorians, r/AcademicBiblical) blocks automated access; museum visitor-question corpora for antiquity could not be located. Both are real gaps.

**Reevaluation**
[Barna, ex-Christians & deconstructing (2023)](https://www.barna.com/trends/ex-christians-deconstructing/) ·
[Barna, two-thirds of Christians face doubt](https://www.barna.com/research/two-thirds-christians-face-doubt/) ·
[Barna, openness to Jesus](https://www.barna.com/research/openness-to-jesus/) ·
[PRRI, Religious Change in America](https://prri.org/research/religious-change-in-america/) ·
[PRRI, exvangelicals](https://prri.org/spotlight/exvangelicals-who-they-are-why-they-left-and-what-they-believe/) ·
[Pew, leaving childhood religions (2025)](https://www.pewresearch.org/religion/2025/03/26/around-the-world-many-people-are-leaving-their-childhood-religions/) ·
Manley, Zippay & McCoyd (2026), *Families in Society* ·
[Fuller Youth Institute](https://fulleryouthinstitute.org/blog/dont-believe-anymore) · [Sticky Faith via FOTF-AU](https://families.org.au/article/building-lasting-faith-kids-proven-ideas-sticky-faith-research/) ·
[Edmondson / psychological safety](https://psychsafety.com/about-psychological-safety/) · [BU Ombuds](https://www.bu.edu/ombuds/resources/psychological-safety/) ·
[Kidd, *Epistemic Injustice and Religion*](https://philpapers.org/rec/KIDEIA-2) · [pre-emptive self-silencing](https://philarchive.org/archive/REKRIA) ·
[Lifton / thought-terminating clichés](https://en.wikipedia.org/wiki/Thought-terminating_clich%C3%A9) · [Auman's catalogue](https://jenaiauman.substack.com/p/thought-terminating-cliches-in-christianity) ·
[TGC, "4 Causes of Deconstruction"](https://www.thegospelcoalition.org/article/4-causes-deconstruction/) *(cited as the anti-pattern archetype)* · [TGC Canada, "Deconstructing my deconstruction"](https://ca.thegospelcoalition.org/article/deconstructing-my-deconstruction/) ·
[APA Monitor / Winell](https://www.apa.org/monitor/2025/06/meaningful-life-after-religion) ·
[love-bombing mechanics](https://recoveringagency.com/articles/the-methods-of-thought-reform/love-bombing/) ·
[Ehrman](https://en.wikipedia.org/wiki/Bart_D._Ehrman) · [Ehrman's students](https://www.theassemblync.com/news/culture/faith/bart-ehrman-unc-bible-last-lecture/) ·
[Rachel Held Evans](https://www.patheos.com/blogs/rebeccaflorencemiller/2015/05/rachel-held-evans-willing-to-be-a-messy-christian-for-the-sake-of-a-messy-world/) ·
[LDS Gospel Topics Essays / RNS](https://religionnews.com/2020/10/27/for-mormons-in-a-faith-crisis-the-gospel-topics-essays-try-to-answer-the-hard-questions/) ·
[Bauer thesis contested — Kruger](https://michaeljkruger.com/how-diverse-was-early-christianity-clearing-up-a-few-misconceptions/)

**Scholarly probing & AI historical reconstruction**
[AHA, Guiding Principles for AI in History Education (2025)](https://www.historians.org/resource/guiding-principles-for-artificial-intelligence-in-history-education/) ·
[Warner, "Just Say No to Historical Figure Chatbots"](https://engagededucation.substack.com/p/just-say-no-to-historical-figure) ·
[Babintseva, via Popular Science](https://www.popsci.com/technology/historical-figures-app-chatgpt-ethics/) ·
[Common Sense Media, Khanmigo risk assessment](https://institute.commonsensemedia.org/risk-assessments/khanmigo) ·
[Khanmigo vs. Google search — no significant difference](https://jtl.uwindsor.ca/index.php/jtl/article/view/10052) ·
MacMullen, *The Second Church* — [BMCR](https://bmcr.brynmawr.edu/2009/2009.10.24) *(contested)* ·
Harris, *Ancient Literacy* — [Harvard UP](https://www.hup.harvard.edu/books/9780674033818) ·
Delehaye via [Head, *Hagiography*](http://www.hagiographysociety.org/wp-content/uploads/2013/03/Head_Hagiography.pdf) ·
Clark, *Reading Renunciation* — [Princeton UP](https://press.princeton.edu/books/paperback/9780691005126/reading-renunciation) ·
[Ignatian recensions & the dating/authenticity split](https://en.wikipedia.org/wiki/Ignatius_of_Antioch) · Lookadoo (2020), *Currents in Biblical Research* 19:88–114 — [Sage](https://journals.sagepub.com/doi/10.1177/1476993X20914798) *(paywalled, not read)* ·
[argument from silence](https://www.academia.edu/122487197/Loud_Arguments_From_Silence_Is_the_Argumentum_e_Silentio_a_Fallacy) · [McGrew, Bayesian treatment](https://link.springer.com/article/10.1007/s12136-013-0205-5) ·
[early Christian archaeology gap — BMCR](https://bmcr.brynmawr.edu/2020/2020.08.26/)

**Question craft & anti-patterns**
[Skinner, "Meaning and Understanding" — summary](https://cluelesspoliticalscientist.wordpress.com/2017/01/09/meaning-and-understanding-in-the-history-of-ideas-by-quentin-skinner-a-summary/) · [Hayton on the mythology of doctrines](https://dhayton.haverford.edu/blog/2013/04/02/mythology-of-doctrines/) ·
[Hunt, "Against Presentism"](https://www.historians.org/perspectives-article/against-presentism-may-2002/) · [strategic presentism (counter-view)](https://www.18thcenturycommon.org/strategic/) ·
[FRE 611(c)](https://www.law.cornell.edu/rules/fre/rule_611) · [Cornell LII, leading question](https://www.law.cornell.edu/wex/leading_question) ·
Loftus & Palmer (1974), *JVLVB* 13:585–589 — [summary](https://www.simplypsychology.org/loftus-palmer.html) ·
Schuman & Presser, *Questions and Answers in Attitude Surveys* — [Sage](https://us.sagepub.com/en-us/nam/questions-and-answers-in-attitude-surveys/book4010) ·
[Paul & Elder, Socratic questioning](https://www.criticalthinking.org/files/SocraticQuestioning2006.pdf) ·
[Wiggins & McTighe, essential questions](https://scarlet-wedge-9axf.squarespace.com/s/McTighe_HowDoWeDesignEssentialQuestions.pdf) ·
[Kuhn's argumentation typology](https://www.tc.columbia.edu/faculty/dk100/) ·
[CDT, Dark Patterns in AI Chatbots (2026)](https://cdt.org/insights/dark-patterns-in-ai-chatbots-a-taxonomy-to-inform-better-design/) ·
[Harvard PS2 AI tutor design notes](https://hechingerreport.org/proof-points-ai-tutor-harvard-physics/) *(a critical review exists; don't lean on the headline)*

**Internal (verified in-repo 2026-07-16)**
Vision V1.1 · Facilitator Governance V3.6 §4, §9, §10, §11, §12 · Representative Modes Design Spec / Prompt Architecture / Validation Plan / Integration Assessment V0.1 · Full System Feature Analysis V0.1 Part 3 · Front-End Decision Log (2026-07-07 role-shaping; 2026-07-16 feature adoption) · `cic-poc/backend/app/world_manifest.py` · `graph/nodes.py` (relational safety) · `prompts/role_modes.py` (commit `1127c09`) · the four `Guided_Starters_V0_1_DRAFT.md` pools and their worlds' Story Inventories, Facilitation Briefs B7, World Capsules, and Permanent Prompts

---

*Prepared 2026-07-16 for the Guided Questions thread. Deliverable 3 (the sets) follows
and is accountable to §2.3's eight tests and §2.4's ratio rule.*
