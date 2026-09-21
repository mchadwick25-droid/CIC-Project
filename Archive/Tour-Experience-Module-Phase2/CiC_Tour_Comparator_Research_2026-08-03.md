# Tours — Comparator Research: What Makes an Honestly-Sourced Experience Impactful
## Research memo, 2026-08-03

**Status:** research memo for the redesign thread to read alongside the six
same-day Front-End Decision Log entries and the PAHC shape-proof, before
drafting the formal Tour Manifest template. Not a design decision on its own
— findings below are cited as validation, contrast, or open questions, marked
as such.

**Prompted by Mark's ask:** research historical and modern online tours/
experiences for what makes them impactful *without recruitment*, rooted in
honest, transparent sourcing, with visuals and voice — what can this project
learn to make Tours give real insight into the lives, theology, and practices
of historical Christian movements, so a participant experiences the
fragmented reality of the record, not a smoothed-over story.

---

## 1. Virtual Paul's Cross Project (NC State, dir. John N. Wall) — closest real analog

A scholarly reconstruction of John Donne's actual 1622 Gunpowder Day sermon
at Paul's Cross, London. Script drawn from a surviving manuscript copy plus
the first printed edition. Visual model built from period engravings, maps,
and drawings. Full acoustic modeling of the pre-Fire cathedral precinct.

**The one idea worth carrying forward, not yet in the shape-proof:** the
project lets a listener hear the same sermon from **8 different physical
positions in the crowd and 4 different crowd sizes** — it doesn't model the
historical experience as singular. Worth a real design conversation later:
whether a tour could honestly represent that where you stood (near the
presider, near the door, near the poor member the tour describes being
served) changed what the gathering actually felt like — without inventing
anything new, just choosing where to place the observer.

**Sources:** [EDUCAUSE Review](https://er.educause.edu/articles/2014/10/the-virtual-pauls-cross-project-digital-modelings-uneasy-approximations) · [Acentech project profile](https://www.acentech.com/project/virtual-pauls-cross/) · [project site](https://vpcross.chass.ncsu.edu)

## 2. Rome Reborn (Bernard Frischer / UCLA) — validates the tiered-sourcing approach independently

A fully interactive digital model of ancient Rome, in continuous development
since 1996. **The sourcing discipline is differentiated by evidence
availability, not applied uniformly:** major monumental buildings (the
Colosseum, the Forum) are built from ancient plans, texts, and archaeological
studies. The "filler" vernacular buildings between them — where almost
nothing survives — are built from the best available secondary source: a
1:250 physical scale model held in a Roman museum, digitized and used
honestly as the best-we-have, not disguised as an attested building.

**Why this matters for the redesign thread:** this is independent field
validation that the primary-vs-trusted-secondary distinction already decided
today (2026-08-03 entries #4–#5) isn't a compromise invented under budget
pressure — it's how serious digital heritage scholarship already handles
exactly this problem.

**Sources:** [Rome Reborn — Wikipedia](https://en.wikipedia.org/wiki/Rome_Reborn) · [Learning Sites / UCLA CVRLab](https://www.learningsites.com/VWinAI/VWinAI_UCLA_CVRLab-home.php)

## 3. Google Arts & Culture "Talking Tours" — the live-generation model this project already rejected, named plainly

Gemini narrates 360° Street View locations live, generated fresh per user
interaction, with a follow-up "ask a question" feature. Deployed at 200+
sites (Gyeongju, historic Jeddah, more).

**Read as contrast, not as a model to follow.** This is exactly the
per-participant live-generation cost structure Tours was redesigned away
from today — and it carries a trust cost worth naming alongside the token
cost: nothing in that pipeline is reviewed before a specific participant
hears it. Google's tours can cover far more locations, far more cheaply, than
this project ever will. The trade this project is making is real: slower,
narrower coverage, in exchange for content a human actually reviewed before
anyone heard it. Worth being able to say that trade-off out loud, not just
assume it.

**Sources:** [Google Arts & Culture blog](https://blog.google/company-news/outreach-and-initiatives/arts-culture/4-experimentations-with-voice-ai-models-to-help-you-explore-culture/) · [Talking Tours](https://artsandculture.google.com/experiment/talking-tours/8AGlfzgsYmBeIA?hl=en)

## 4. Museum audio tour design — soundscape, personalization, and one open question

Current best practice (MuseumNext, museum audio-guide literature, 2025):
professionally scripted narration paced for spoken word; **layered ambient
soundscape** to build a sense of place (the Cutty Sark uses creaking wood,
gulls, and port chatter rather than narrated dialogue to create presence);
and **personalized depth** — a visitor hears an initial narrative, then can
choose to go deeper into a first-person account, historical context, or
expert analysis.

**The personalization pattern is already yours.** This is the same shape as
the Level 1/2/3 + citation-chip pattern already built into this project — a
visitor chooses how deep to go, the base experience never requires it. Good
field validation that this is a proven UX pattern, not invented complexity.

**Open question flagged, not decided:** does ambient soundscape (city noise,
a lamp being lit, a quiet murmur before the reading starts) sit at a
different risk level than narrated dialogue, since it's not making a
specific evidentiary claim the way spoken words are? Worth a real design
conversation for the redesign thread — not assumed safe just because it
sounds like scene-setting texture rather than a claim.

**Sources:** [MuseumNext, 2025 trends](https://www.museumnext.com/article/new-ideas-for-museum-audio-tours-trends-shaping-2025/) · [Guide-ID / blooloop](https://blooloop.com/museum/news/guide-id-immersive-audio-storytelling/)

## 5. Drive Thru History (Dave Stotts) — a real precedent for "impactful without recruitment"

An on-location documentary series filming at the actual historical sites,
treating the Gospels and church history "as historical canons as opposed to
faith-based books," explicitly non-denominational, and reviewed as appealing
to believers and secular audiences alike without pushing an agenda.

**Proof this is achievable, and the exact gap this project closes.** Drive
Thru History earns trust through tone and on-location presence, but it has
no citation apparatus, no tiering, no disclosed sourcing at all — a viewer
takes it on the host's word. This project can match its warmth and beat it
decisively on rigor: the same non-preachy tone, backed by actual, checkable
sources.

**Sources:** [Plugged In review](https://www.pluggedin.com/youtube-reviews/drive-thru-history-with-dave-stotts/) · [Family Theater Productions](https://www.familytheater.org/blog/drive-thru-history-dave-stotts-bible-gospels)

## 6. *The Chosen* — the cautionary case, named plainly

A single opening disclaimer ("biblical events are condensed"), followed by
extensive invented characters and scenes woven into the Gospel narrative
with no scene-by-scene marking of what's attested versus invented. The
documented, legitimate criticism: viewers can't reliably tell where the
Gospels end and the writers' creative choices begin.

**This is the concrete version of the failure mode this project's whole
per-beat, per-element disclosure discipline already exists to refuse** — not
an abstract principle, a real, well-known, criticized example of what
happens without it. Worth keeping as the reference case when anyone
(including future construction threads) is tempted to fold a disclaimer into
one threshold sentence instead of marking each claim where it actually
occurs.

**Sources:** [ScreenRant, theology experts](https://screenrant.com/is-the-chosen-accurate-bible-experts-explain/) · [Compelling Truth](https://www.compellingtruth.org/review-of-the-Chosen.html)

## 7. Museum best practice on uncertainty — independent field validation of the honest-silence beats

Current museum-labeling best practice: *"acknowledging uncertainty invites
curiosity rather than simulating certainty."* Recommended technique for
contested or thin evidence: state each source's actual claim plainly
("documents indicate X; oral histories suggest Y; investigation continues")
rather than picking one version and presenting it as settled.

**Direct validation of the Desert-synaxis and unrecorded-prayer honest-
silence beats already in tonight's design** — the field has independently
reached the same conclusion this project reached from its own convictions:
saying "we don't know" builds more trust than smoothing over the gap, not
less.

**Sources:** [UCL, Dr Eva Miller](https://www.ucl.ac.uk/history/news/2025/jul/could-museums-be-more-transparent-dr-eva-miller) · [Sacred Skulls](https://www.sacredskulls.co.uk/what-museum-labels-should-actually-tell-visitors-about-provenance-and-human-cost)

## 8. Documentary technique — the "reflexive mode" as craft, not just ethics

Documentary scholarship names a "reflexive mode" — where a film draws
attention to its own limits and the maker's own choices — as a legitimate,
established technique for handling gaps in the historical record honestly,
distinct from simply omitting what can't be shown.

**Reframes the Facilitator's honest-silence beats as good craft, not just an
obligation layered on top of the design.** A documentarian naming what a film
can't show you is a recognized storytelling move, not a disclaimer breaking
the fourth wall — worth carrying that framing into how the redesign thread
talks about these beats.

**Sources:** [Fiveable, documentary techniques](https://fiveable.me/lists/essential-documentary-film-techniques) · [HistoryNewsNetwork](https://www.historynewsnetwork.org/article/filmmaking-reality-and-fact-how-documentaries-shap)

---

## Summary — what to carry into the redesign thread

1. Tiered sourcing (primary vs. trusted secondary, disclosed) is field-
   standard practice in serious digital heritage work, not a compromise —
   cite Rome Reborn if this ever needs defending to a skeptical reviewer.
2. Live AI-generated narration (Google's model) is a real, working
   alternative this project deliberately didn't choose, for named reasons
   (cost *and* trust) — worth being able to state that trade-off plainly.
3. Honest-silence beats and per-element disclosure aren't just this
   project's own conviction — they're independently validated by both
   museum practice and documentary theory as what actually builds trust.
4. *The Chosen* is the concrete cautionary case for what happens without
   per-beat disclosure; Drive Thru History is the concrete positive case for
   tone without recruitment. Both are worth keeping as reference points, not
   just abstractions.
5. Two open ideas, neither decided here: multiple observer positions for the
   same attested event (Paul's Cross model), and whether ambient soundscape
   sits at a different risk tier than narrated dialogue.
