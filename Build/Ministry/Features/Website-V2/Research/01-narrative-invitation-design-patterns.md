# 01 — Narrative and invitation design patterns: what real sites do to draw a visitor in

**Workstream:** Website V2 · **Kind:** research brief (input to a design pass; decides nothing) · **Date:** 2026-09-08 · **Researched by:** Fable, per the model-routing ruling (deep research)

**Why this brief exists.** Mark's pivot, in his words: "it's not about getting more users, but connecting with the right ones and drawing people in to open a door to deepening their faith and the story of Jesus." The engine now works (real pilot feedback). The need has changed from *get a tester into a conversation fast* to *engage a visitor's heart*. A pilot tester put the diagnosis sharply: the conversation did not feel AI-lazy or hollow, but the site's own marketing copy did. Mark has since written homepage copy everyone agrees has heart — concrete historical imagery (modest homes, mountain monasteries, Reformation squares, colonial fields), honest about the church's failures, ending in an invitation to explore rather than a pitch. This brief researches how real, currently-live sites achieve that same pull *structurally* — pacing, opening, whitespace, emotional shape — so the surrounding website can be redesigned to a craft level worthy of the copy, the Atlas, and the conversation UI. The site's posture must be invitation, never a funnel; that is the project's own principle, "revealing is witness, never recruitment" (Constitution; carried on the live Arrival screen and in the frozen Design V2).

**How the research was done, honestly.** Every direct page fetch from this sandbox was blocked at the network egress proxy (hallow.com, bible.com, charitywater.org, nytimes.com, pudding.cool, emergencemagazine.org, amrevmuseum.org, nga.gov, awwwards.com, nngroup.com, web.archive.org and roughly twenty others). Web search worked and returns indexed page text, so every observation below comes from one of: (a) **page text** — a site's own indexed copy, titles, or headings, quoted verbatim; (b) **maker's account** — the studio, agency, award, or press release describing what was built; (c) **critique** — a published analysis or usability study. Each example is tagged with which. Where a claim is my inference from those sources rather than something I saw rendered, it says so. D-work should open the six URLs listed in §6 in a real browser and capture screenshots into `Sandbox/` before anything is imitated.

---

## 1. The short answer

The sites that draw people in through story do four things the SaaS pattern (hero → features → social proof → CTA) never does. They **open with a contract, not a claim** — a plain statement of what this is, what it costs, how long it takes, or what it will not do. They **put an overture before any choice** — a video, a voice, a first chapter — so the visitor is already inside something before being asked to pick. They **let the reader set the tempo** — the piece reads as a documentary if you scroll slowly and as an article if you scroll fast, and nothing hijacks the scroll. And they **keep the chrome tiny so the artifact can be huge** — enormous images, generous margins, three colours, a serif with a lineage — because whitespace is how a page says it is not in a hurry to get something from you.

The strongest single analogue for Church in Conversation is not a faith app at all. It is the Museum of the American Revolution's *Finding Freedom*: five real people from 1781, speaking in dramatized first person built from pension records and court papers, the primary sources exposed beside the voice, the visitor asked to weigh choices "when there was no clear route to freedom." That is CiC's premise — a voice from the record, honest about the record — done as a Webby-winning web experience.

The faith-app category, meanwhile, is the clearest picture of what *not* to do. Hallow's homepage is a textbook growth funnel (celebrity hero, "#1" superlative, free-trial CTA, exit-intent popups, streaks, leaderboards) and it has drawn exactly the critique — "the commodification of Christianity," "the gamification of connecting with God" — that CiC's charter is built to avoid. The quiet outliers (Sacred Space, Lectio 365, Emergence Magazine) show the alternative: the practice *is* the page.

---

## 2. Examples, by category

### 2.1 Faith and contemplative sites

#### Hallow — hallow.com · *the cautionary contrast* · [page text + maker's account + critique]

- **Opening.** Indexed homepage copy: **"Join Mark Wahlberg and Jonathan Roumie on Hallow, the #1 prayer app"** with the CTA **"Try Hallow for Free."** Seasonal landing pages carry the line **"Find God's Peace"** ("…in 2026," "…this Lent," "…this Easter") and "Download for free today."
- **Structure (inferred from page text and the features page).** Celebrity/superlative hero → free-trial CTA → feature inventory ("10,000+ sessions," Rosary, Sleep Bible Stories, Bible in a Year) → testimonials ("This app has gotten me to pray every day") → app-store badges. Story appears nowhere before a functional choice; the first thing offered is a trial.
- **Growth machinery (maker's own account).** Wisepops case study: a Lent-timed 90-day free trial promoted in an **exit-intent popup featuring the influencers** drove 32,533 visitors to the signup window; Hallow's Director of Organic Marketing credits popups "optimized separately for mobile and for desktop" with "thousands of incremental purchases." The 2024 Super Bowl spot produced "the most downloads in a single minute we'd ever seen"; the Pray40 Lent challenge reached 5 million concurrent participants in 2025 and a 300% rise in new subscriptions in Q1. The app tracks a **Prayer Streak and a Game Streak**, a Trivia Leaderboard, and lets users compare prayer minutes with friends.
- **Emotional shape.** Reassurance (peace) + authority (#1, celebrities) + urgency (liturgically timed trials). It is a conversion arc with a religious vocabulary.
- **Critique on record.** Slate and Salon reviews (2025) and Freya India's essay "The Commodification of Christianity" name the discomfort directly: being "congratulated for maintaining a streak," "the gamification of connecting with God," apps that "have to be so engaging we can't stay away." A reviewer's line — these companies "need users to keep coming back" — is the opposite of Mark's "not more users, the right ones."
- **Take:** nothing structural. **Leave:** all of it. This is the register the pilot tester heard in CiC's old copy.

#### YouVersion / The Bible App — bible.com · *utility, not story* · [page text]

- **Opening.** Indexed title: **"Read the Bible online. A free Bible on your phone, tablet, or computer."** App page: **"Download The Bible App Now — 100% Free, No ads or purchases."** Trust is carried by scale ("used on more than 500 million devices"; "2,500+ versions in 2,100+ languages") and by a **Verse of the Day** that is itself content.
- **Structure.** The tool is offered immediately; there is no narrative before the functional choice. The honest, plain promise (free, no ads) is the only warmth.
- **Take:** a promise stated flatly, without adjectives, reads as trustworthy. **Leave:** a stat-wall as the trust device. Mark has already ruled "no stale numbers" on the CiC homepage (Decision-Log, 2026-09-03), and CiC's numbers are small; borrowed scale-signalling would ring false.

#### Pray.com — pray.com · [page text]

- Indexed title: **"Pray: The World's #1 App for Daily Prayer and Biblical Audio Content."** Superlative-led like Hallow; "5,000+ daily prayers, meditations, bedtime stories, and cinematic stories." Noted only as a second data point that "#1" is the category's default hero — which is exactly why CiC should not sound like it.

#### Lectio 365 — lectio365.com · *the quiet alternative* · [page text]

- **Opening.** "A daily devotional resource to help you pray through the Bible every day, written by 24-7 Prayer leaders and delivered through a free app." The page explains a **practice** (the P.R.A.Y. rhythm: Pause, Rejoice/Reflect, Ask, Yield; morning, midday, night), not a product. It is "donation-supported… kept free so more people can pray the Bible every day."
- **Shape.** Practice → who writes it → how to get it. No superlative, no trial, no streak. It passed 2 million downloads in March 2026 without any of the machinery above.
- **Take:** describe the practice, name who stands behind it, offer it. That is an invitation's whole grammar.

#### Sacred Space — sacredspace.com · *the experience is the homepage* · [page text]

- Founded 1999 by two Irish Jesuits; "over five million visits annually." Indexed homepage title: **"Your daily prayer online."** The homepage *is* a ten-minute guided prayer in six stages — **The Presence of God, Freedom, Consciousness, The Word, Conversation, Conclusion** — moved through "slowly and attentively."
- **Structure.** There is no pitch layer at all. The first screen is the first stage. The site has survived 27 years on this.
- **Take:** this is the strongest structural precedent for Mark's own ruling of 2026-09-03 — *"no explaining the experience instead of having it."* A short, real exchange with a Representative belongs *inside* the homepage's arc, not described beside it.

#### BibleProject — bibleproject.com · [page text + maker's account]

- **Opening.** Indexed title: **"Study the Story of the Bible With Free Tools."** The thesis line — the Bible as "a unified story that leads to Jesus" — is the hero idea; the sections are verbs of exploration: **Watch, Explore, Listen, Study** ("meditate on scripture in your own way and at your own pace").
- **Craft note.** Underbelly's case study of BibleProject's announcement sites: "features that allow users to hear the founders' impassioned voices while accompanying text appears in sync with the audio," with the visual theme carried "through page loading, transitions, and hover states."
- **Take:** section labels as verbs of exploration, not acquisition; a founder's actual voice as the warmth source. **Leave:** the resource-hub density (CiC is one door, not a library).

#### Emergence Magazine — emergencemagazine.org · *the gold standard for slow, contemplative long-form* · [maker's account + critique]

- Ecology, culture, spirituality; designed by Studio Airport (NL). Studio Airport's stated rule: **"everything that you see on the site is there for a reason."** Communication Arts and the Webby "Crafted with Code" citation describe a **"slow consumption approach" with balanced typography, use of whitespace and minimal navigation.** Essays ship with a narrated "listen" version and ambient audio; photo stories use scroll-triggered reveals. Awwwards SOTD (2018) logs a **three-colour palette** (black, pink, white). Webby and National Magazine Award nominations, Peabody and Emmy nominations, European Design Awards gold.
- **Emotional shape of an essay page (from the makers' descriptions).** Title and a single image; a choice to read or listen; then uninterrupted prose with images arriving at the pace of the text. Nothing asks for anything until the end.
- **Take:** three colours, one serif, big margins, a listen option, minimal nav. This is the reading register CiC's tradition pages and About should inherit.

#### Plough — plough.com · [page text + maker's account]

- Faith, culture and society, since 1920. Plough's own account of its redesign ("Retooling the Plough"): the logo adapted from **Rudolf Koch's Fette Deutsche Schrift** found in their archive; the wordmark set in a contemporary condensed serif; "rigorous attention to editing and design." The site's framing question is a human one — "How can we live well together, and what gives life purpose?" — not a product claim.
- **Take:** typographic authority drawn from a real tradition, not from a trend. CiC's palette and type are locked by the Brand Guidelines; the lesson is about *where authority comes from*, not about changing the type.

#### Alabaster — alabasterco.com · [page text]

- "Beautiful Bibles and Books on Creativity and Faith"; vision "to see all of humanity experience God as good and beautiful." Commerce, but beauty-led and image-first. Noted as evidence that a faith brand can lead with beauty rather than features and still be taken seriously.

### 2.2 Scrollytelling, documentary, and long-form interactive journalism

#### *Snow Fall: The Avalanche at Tunnel Creek* — The New York Times, 2012 (still live at its original URL) · [page text + critique]

- **Opening.** The first words are the story, already moving: **"The snow burst through the trees with no warning but a last-second whoosh of sound, a two-story wall of white and Chris Rudolph's piercing cry: 'Avalanche! Elyse!'"** Behind it, an ambient looping video of blowing snow.
- **Pacing.** A student rhetorical analysis (2025) notes the text "is formatted to not fill the page but to stay on the left, which gives the feeling of being on a white, empty mountain." Six chapters. Multimedia appears only where it is organic — an interview video where a survivor speaks, a clickable name that opens a small bio card, a terrain fly-through where the reader needs geography.
- **The backlash is instructive.** "Snow Fall" became a newsroom verb; the critique "Snowfallen" lamented pieces that "go to extreme lengths to add design elements… that do little more than distract from the story itself." It took sixteen people six months; it did not work on mobile, where half of traffic already was. The NYT's own retrospective standard: multimedia "absolutely organic to the storytelling itself."
- **Take:** text left, white space as landscape; media only where the story needs it. **Leave:** any effect that exists to impress.

#### *Firestorm* — The Guardian, 2013 · [maker's account]

- Tasmanian bushfires. journalism.co.uk on how it was built: writer Jon Henley "interjected chapters of contextual information at key points of the narrative." Each chapter "opens on full-width footage with ambient sound; scroll moves you between filmed testimony, stills and reported text, so **a reader who scrolls slowly gets a documentary and one who scrolls fast gets an article.**"
- **Take:** that sentence is the pacing principle this brief recommends adopting whole (§5, P3).

#### *The Boat* — SBS Australia, 2015 · [maker's account + critique]

- Nam Le's story of Vietnamese refugees after 1975. "Invites users to scroll its title page to open the first of six ink panel chapters"; "over 300 separate illustrations… 59 of which include custom animation"; the reader can "set the auto scroll story-by-story, or interact with each story" themselves. Public Media Alliance's "Best of PSM."
- **Take:** a title page that opens into chapters; hand-made ink rather than photography or stock; tempo control offered, never imposed.

#### *Welcome to Pine Point* — NFB, 2011 · [maker's account + critique]

- A mining town erased from the map; "a piece about memory, and how memory is utilized, filtered and activated." A "digital scrapbook": chapters (Intro, Town, Pine Pointers, Ends and Odds, … One for the Road), yearbook photos, hand-drawn animation, a score by the Besnard Lakes. The makers said they were "toying with the idea of the death of the photo album."
- **Take:** the *form* was chosen to match the *subject* (memory → scrapbook). CiC's subject is a church that met in modest homes and mountain monasteries; the form should look like it came from those places.

#### *Bear 71* — NFB, 2012 · [critique]

- A grizzly's life told from her perspective through the park's surveillance cameras. The analysis on record notes the opening "delivers an announcement on the length of the story" (20 minutes) before anything else, then the wordmark, then a video introducing the protagonist.
- **Take:** the honest contract at the door — tell the visitor how long and what kind of thing this is before asking for their attention.

#### *In pursuit of democracy* — The Pudding, November 2025 · [critique + page text]

- Alvin Chang analysed every mention of "democracy" in the Congressional Record since 1880. FlowingData's description: "each dot represents five speeches or remarks, with bright dots being ones that argue American democracy is under threat"; early on the word meant the Democratic party and the shift in meaning is *revealed* by scrolling. The Pudding's house style is "sparse on words" — data and design carry the narrative. (The Pudding's developer Russell Samora wrote Scrollama, the IntersectionObserver library most newsroom scrollytelling still uses.)
- **Take:** one honest artifact revealed gradually beats ten claims stated at once. CiC's Atlas river is that artifact.

#### *A visual journey through the life of Ozzy Osbourne* — South China Morning Post, July 2025 · [critique]

- Maglr's 2026 roundup: "moves chronologically… using scroll-triggered illustrations, archival imagery, and carefully paced text." A recent, currently-live proof that chaptered biographical procession still works in 2025–26 without 3D or WebGL.

#### Nielsen Norman Group, "Scrolljacking 101" · [critique — usability study]

- NN/g tested sites across industries using scrolljacking: "the majority of study participants were at least mildly disoriented"; participants "did not hesitate to click away from the page or refresh it"; it "leads to more user pain than benefits." The one exception they allow: a scroll effect "is beneficial when it gradually adds supporting information to lessen cognitive load and support storytelling. When it does not serve this function, it is not worth it."
- **Take:** that exception is the entire licence for motion on the CiC site. Design V2 §6.3 already binds a full motion inventory; this is the external evidence for it.

### 2.3 Museum and historical-archive digital exhibits

#### *Finding Freedom* — Museum of the American Revolution (online 2020; Webby People's Voice, 30th Annual Webbys 2026; AAM MUSE bronze 2021; Anthem silver 2022) · [maker's account]

- Five real people of African descent in Virginia, 1781 — **Andrew, Deborah, Eve, Jack, London** — "as they contemplated their best opportunities for freedom, liberty, and self-determination." "Dramatized first-person narratives" built "using primary sources ranging from pension records to newspaper ads, period maps and broadsides, surviving objects, works of art, court records, and correspondence." "Historically accurate watercolor illustrations" by Wood Ronsaville Harlan. The visitor is asked "to consider the difficult choices… when there was no clear route to freedom, safety, or equal rights." Adapted from a gallery touchscreen with the agency AREA 17. Short contextual essays, a primary-sources page, and a glossary sit beside the narrative. ~1.5 million pageviews.
- **Why this is CiC's nearest kin.** A voice from the record, in first person, with its sources shown, asking the visitor to weigh a real historical choice — and honest that the record is partial (the museum publishes the sources so the reconstruction can be checked). This is "a voice of its tradition, in real conversation" with the seams visible.
- **Take:** person first, then sources; painted imagery; choices framed as the person's, not the visitor's conversion. **Leave:** the classroom scaffolding (units, teacher resources) — right for schools, wrong for a seeker.

#### The Searchable Museum — Smithsonian NMAAHC (2021; built by Fearless; CIO 100; Webby nominee 2022) · [maker's account + press]

- "Visitors to the exhibition are greeted by an **introductory video**, before entering **four discrete parts, each split into chapters** containing artworks, artifacts, multimedia, and historical material." "Through first-person accounts and artifacts…" Museumgoers "take it in at their own pace." The first exhibition, *Slavery and Freedom*, begins in the 14th century and ends with Reconstruction.
- **Take:** overture → parts → chapters, with first-person accounts as the through-line and pace left to the reader. This is the macro-structure to test for CiC's "Church in History" arc.

#### Rijksmuseum website and Collection Online — Fabrique + Q42 (Webby 2025, two wins, Best User Interface; Dutch Design Award) · [maker's account]

- "Extremely large images… a special 'image first' design"; a dedicated **Stories** platform with "'scroll counting' style articles, tours, 'zoomers', live events and podcasts"; a customer journey per audience; described as "the Netflix for art."
- **Take:** let the artifact be enormous and give story its own first-class section, not a blog tab.

#### Anne Frank House — the Secret Annex online / 3D tour (relaunched Nov 2024) · [maker's account]

- The rooms are shown "furnished according to how it was when occupied… between 1942 and 1944," modelled by Vertigo Games — while the real Annex "remains empty today, following the wish of Otto Frank." A cloned voice guides the tour in four languages.
- **Take:** a *declared* reconstruction, honest that it is one, is the museum world's precedent for what CiC does with a Representative: the reconstruction is offered as such, and the visitor is told.

#### National Gallery of Art — nga.gov (Webby People's Voice 2026, Cultural Institutions; 12 Webbys since 2022) · [press]

- Recognised for "engaging new audiences through compelling digital content across its social media and website." Noted for currency; the press material does not describe the page structure, so no structural claims are made here.

### 2.4 Mission-driven brand storytelling

#### charity: water — charitywater.org · [page text + critique]

- **Opening.** Indexed title: **"charity: water | Help Bring Clean and Safe Water to Communities."** The spine of the whole site is one plain promise, repeated everywhere: **"100% of all public donations bring clean water to people in need"** (operations funded by a separate private group of donors).
- **Structure (critique).** Morweb's analysis: "a pyramid structure… the top pages of the site light on text and the subpages more dense, allowing visitors to go deeper as needed." The Storytelling Non-Profit: visiting the site "doesn't feel like a blatant ask for money — it's an educational resource." Fast Company: content "champions hope and dignity over guilt."
- **Story before ask.** *The Spring* — a short film narrated by the founder, tagline "Until nobody on earth dies from dirty water…" — anchors the giving page. *Someone Like You* (World Water Day): "answer questions about their values to connect with one of 400 people living in Adi Etot" — personalisation used to produce an *encounter*, not a segment.
- **Take:** the promise is the hero; story precedes the ask; hope over guilt; personalisation only if it introduces you to a person. **Leave:** the donation-page machinery.

#### Patagonia — patagonia.com · [page text + maker's account]

- **The line.** "We're in business to save our home planet." Homepage statements (indexed): "We support grassroots activism," "We keep your gear in play," "We give our profits to the planet" — declarative, first-person plural, no plea.
- **Honesty as the brand.** The Footprint Chronicles (2007) directive: "Be completely honest about where our products came from and the resources required to create them," including "the challenges Patagonia is still working to solve." Its framing to visitors: "this is your conversation." Worn Wear invites customers' own repair stories. A brand analysis notes the imagery is "breathtaking nature shots… paired with carefully selected but provocative words… **without putting itself at the centre**."
- **Take:** a company confessing its own footprint is the commercial cousin of Mark's copy being honest about the church's failures. The site says "we," names what it has not solved, and decentres itself. That is the register.

#### Reading-first editorial references (brief) · [critique]

- **Aeon** (aeon.co): long-form essays in three columns; "a hover-triggered animation that shifts the colors of the cover photos" — the only motion on the page, and it exists to help the reader keep place in a long scroll.
- **The Marginalian**: "large margins, well-placed pull quotes, and a distraction-free environment… without feeling heavy," on a pastel ground.
- Both are evidence that a text-heavy page can be warm if the margins are generous and the chrome is quiet.

---

## 3. What the good ones share

Read across the twenty-odd examples above, the emotional pull is produced by the same handful of structural moves, regardless of category:

1. **A contract at the door.** Bear 71 states the running time; charity: water states 100%; Anne Frank House states the rooms are a reconstruction; Lectio 365 states free and donation-supported. The first screen tells the truth about what this is before it asks for anything.
2. **Overture, then chapters.** Searchable Museum's intro video → four parts; The Boat's title page → six chapters; Firestorm's full-bleed chapter openings; Snow Fall's moving first sentence. Something *happens* before the visitor is asked to choose.
3. **The reader owns the tempo.** Firestorm's slow/fast rule; The Boat's optional auto-scroll; NN/g's finding that hijacked scroll makes people leave.
4. **One voice, first person, from the record — with the seams showing.** Finding Freedom's dramatized narratives with sources published beside them; Patagonia's confessed footprint; Snow Fall's bio cards.
5. **The artifact is huge; the chrome is tiny.** Rijksmuseum's "image first"; Emergence's three colours and minimal nav; Snow Fall's text kept left on an "empty mountain"; Aeon's and The Marginalian's margins.
6. **Hope and dignity over guilt; the ask is last and small.** charity: water explicitly; Patagonia's "we give our profits" as a statement not a plea; Sacred Space and Lectio 365 with no ask at all on the first screen.
7. **Form matches subject; imagery is made, not generated.** Pine Point's scrapbook, The Boat's ink, Finding Freedom's watercolour, Plough's Koch-derived letterform.
8. **The experience is on the page.** Sacred Space's prayer *is* the homepage; BibleProject's founders' voices with synced text; Emergence's listen option.

---

## 4. Current trends (2025–26) that would work against the mission if adopted uncritically

Each entry names the trend, the evidence that it is contested even on its own terms, and why it specifically clashes with "invitation, never recruitment."

1. **Glassmorphism / "Liquid Glass."** Apple's June 2025 material drew an accessibility backlash (developer forums, Infinum, Access Advisors: "foreground text blends into background elements"; "fatiguing under real-world light"); Apple added a "Tinted" control in iOS 26.1 and reduced default transparency again for iOS 27. Creative Boom lists it among the trends creatives are "so over" in 2026. **Clash:** frosted panels read as a tech product's control surface, and they cost contrast — Design V2 holds four WCAG criteria *above* AA. A hearth is not made of glass.
2. **Gradient-mesh, purple-glow, "abstract orb" AI-startup aesthetic.** The critiques are unusually specific: AI-default design is "Inter font, purple gradient, three cards, rounded corners"; sites with "the same dark gradient, same faint glow behind the hero… same abstract orb where the product should be"; visitors conclude "they probably just used AI… are they vibe-coding the actual product too?" Gradients have "lost any sense of intentionality" because image generators default to them. **Clash:** this is the pilot tester's diagnosis rendered in pixels. A page that looks AI-generated tells the visitor the voice inside is too — the one thing the engine has just proven it is not.
3. **Bento grids.** 2026 practitioner critique: most are "decorative, with cells that are the same size and content retrofitted to fit them, reading as a card wall"; explicitly wrong "when they need linear progression or deep content." **Clash:** a bento is a feature inventory. CiC's homepage is a procession with an arc; a grid of equal cells says "pick a feature," not "come in."
4. **Scrolljacking, heavy parallax, 3D/WebGL immersive heroes.** NN/g: "more user pain than benefits"; participants clicked away. Awwwards data: 3D sites took 61% of Site of the Day in Q1 2026 (from 23% in 2024); the 2025 Site of the Year is a Formula 1 driver's site with a rotating WebGL helmet and cinematic scroll sequences. Snow Fall's own backlash: cost, and mobile. **Clash:** spectacle asks to be admired; invitation asks to be entered. The Atlas is already the project's one earned "game-grade" surface — the marketing site should frame it, not compete with it.
5. **Kinetic typography, custom cursors, preloaders.** 2026 guides concede the failure mode: "motion becomes necessary to understand what is being said," "text animations delay access to meaning or force users to wait," and vestibular harm means `prefers-reduced-motion` is "non-negotiable." **Clash:** a headline that assembles itself is performing. Mark's copy should simply be *there* when the page opens.
6. **Urgency, scarcity, countdowns, "#1," celebrity social proof.** Dark-pattern literature is unambiguous ("Only 1 left," fake timers "nudge users to act impulsively"); the EU's Digital Fairness Act draft is expected Q3 2026 to bundle "dark patterns, manipulative personalisation and opaque contract design." In the faith category specifically: Hallow's Lent-timed 90-day trial, Pray.com's "#1 in the world." **Clash:** Mark's brief is "not more users, the right ones." Urgency selects for the impulsive, not the seeking.
7. **Exit-intent and newsletter popups; confirmshaming.** Hallow's own vendor boasts of influencer exit-intent popups. Harry Brignull's term for the guilt-worded decline ("No thanks, I hate saving money"; a medical-kit site's "No, I'd rather bleed to death"); popup vendors' own 2025 data admit nonprofit visitors "rely on storytelling and trust, not urgency" and "read before they act," and that "guilt-trip buttons backfire… they'll remember that feeling." **Clash:** an interruption is the opposite of hospitality; a guilt-worded decline is recruitment in its purest form.
8. **Gamification — streaks, leaderboards, prayer minutes.** Hallow's Prayer Streak, Game Streak and Trivia Leaderboard have drawn on-record critique: "the gamification of connecting with God"; apps that must be "so engaging we can't stay away." **Clash:** streaks manufacture return through loss-aversion. CiC's return should be because a door was worth walking back through.
9. **Chat-box-as-hero and chatbot chrome.** UX Collective (Aug 2026): "AI chat is the loudest pattern of 2026 and the most over-applied"; practitioners call it "a pendulum swing that will correct itself." **Clash, with a nuance:** CiC's conversation is real and is the product — but a homepage whose hero is a text field with a blinking cursor reads as "another AI chatbot," exactly the framing Mark dropped fleet-wide on 2026-09-03 ("drop the 'AI system' framing"). Show a *person speaking from a place*, not an input box.
10. **AI-generated imagery.** The 2026 tells are named in the trade: "golden-hued," over-polished, and a documented pushback toward "hand-drawn illustrations, scribble accents… imperfect by design." **Clash:** CiC's subject is real places and real sources. A generated "monk in a monastery" would undercut the honesty of copy that is honest about where the record runs out.
11. **Stat-walls and vanity counts as trust.** Fine for YouVersion's 500 million devices. **Clash:** Mark has already cut stale numbers from the homepage; the trust device for CiC is *sources named*, not users counted.
12. **Feature-first information architecture in general** (hero → features → proof → CTA). **Clash:** it front-loads the functional choice that every good example above defers. It is the SaaS pattern the whole brief is arguing against.

---

## 5. Synthesis — eight principles for the CiC homepage and site-wide pacing

Opinionated, each tied to something researched above. These are recommendations for the design pass, not rulings; Mark decides.

**P1. Open with the contract, not a claim.** *(Bear 71's running-time announcement; charity: water's 100%; Anne Frank House's declared reconstruction; Lectio 365's "free, donation-supported.")* The first screen says plainly what this is, what it is built from, and what it will never do — "witness, never recruitment" belongs *in the opening*, as the site's honest sentence, not buried in a disclosure grid. No superlative, no number, no adjective doing the work a fact should do.

**P2. Overture before any door.** *(Searchable Museum's intro video → four parts; The Boat's title page → chapters; Firestorm's chapter openings.)* Mark's historical-imagery copy *is* the overture. It runs first and alone; the tradition doors, the Atlas portal and the Table portal come after it, never beside it in the hero. A visitor should be somewhere — a modest home, a mountain monastery — before being asked where to go.

**P3. Scroll slowly, get a documentary; scroll fast, get an article.** *(Firestorm's build note; NN/g's scrolljacking study; Snow Fall's mobile failure.)* Every section carries a plain-text spine that reads complete at speed, with imagery and any motion adding depth only for those who linger. No scrolljacking; no effect the reader cannot skip; `prefers-reduced-motion` honoured; every arc readable at 320px. Motion only where it "gradually adds supporting information."

**P4. One voice, first person, from the record — and show the seams.** *(Finding Freedom's dramatized first-person with sources published beside it; Patagonia's confessed footprint; Snow Fall's bio cards.)* A real Representative excerpt on the page is worth more than any description of the engine — and it sits next to its named source. "Where the record runs out" is a *visible design element* (a marked gap, a stated uncertainty), not a footnote; that honesty is the site's distinctive beauty, the way Patagonia's confessed footprint is its brand.

**P5. Huge artifact, tiny chrome.** *(Rijksmuseum's "image first"; Emergence's three colours and minimal nav; Snow Fall's text on an "empty mountain"; Aeon's and The Marginalian's margins.)* The Atlas river, the painted Table, and the era imagery get full width — Mark's 2026-09-03 ruling for full-width stacked portals is already this instinct. Navigation stays minimal; body measure stays short; the page breathes. Whitespace is how a page tells a person thinking about their life that it is not in a hurry.

**P6. Hope and dignity over guilt; the ask comes last and is small.** *(charity: water's stated ethic; Patagonia's declaratives; Sacred Space with no ask on the first screen.)* No popups, no countdowns, no streaks, no "#1," no guilt-worded decline anywhere on the site. Honesty about the church's failures is delivered in Mark's copy with dignity, not accusation. The close is an open door — "explore" — and the get-involved ask lives on its own page, said once, plainly.

**P7. Form matches subject: made imagery, period-true, never generated-looking.** *(Pine Point's scrapbook for memory; The Boat's ink; Finding Freedom's watercolour; Plough's Koch-derived letterform; the 2026 "imperfect by design" turn.)* Modest homes, monasteries, squares, fields — drawn, painted, or actually photographed, with texture and restraint. Nothing on the page should be mistakable for an AI startup: no gradient mesh, no orb, no glass, no bento, no Inter-and-purple. Authority comes from the tradition the type and images belong to.

**P8. The experience is on the page.** *(Sacred Space's prayer as homepage; BibleProject's founders' voices with synced text; Emergence's "listen"; Mark's own ruling "no explaining the experience instead of having it.")* Somewhere inside the homepage's arc — after the overture, before the doors — the visitor hears a Representative actually speak: a short real exchange, or a first exchange they can have there. Not a screenshot of a chat UI, not a text field as hero: a voice, from a place, with its source named.

---

## 6. What this brief could not verify, and what D-work should do next

- **Direct rendering was blocked.** Six URLs should be opened in a real browser and captured (full-page, desktop and 390px mobile) into `Sandbox/` before any structural imitation: `emergencemagazine.org` (home + one essay), `amrevmuseum.org/interactives/finding-freedom`, `searchablemuseum.com` (Slavery and Freedom entry), `sacredspace.com`, `charitywater.org`, and `hallow.com` (as the contrast).
- **Hallow's exact section order** is inferred from page text and its features page, not seen rendered; the hero copy and CTA are verified verbatim.
- **The Pudding's 2026 homepage** could not be indexed via search at all; its 2025 *democracy* piece is described from FlowingData's account.
- **Numiko's "Best Museum and Gallery Websites 2026"** (V&A, Nottingham Contemporary and ten more) was only partially visible; worth a full read in a browser.
- Nothing here changes Design V2's frozen type, colour, motion inventory or accessibility floor; where a principle above touches a frozen item, it goes through a change order in `Decision-Log.md`, not this file.

---

## Sources consulted

*Indexed page text and makers' accounts:* hallow.com (index snapshots, `/try-hallow/`, `/features/`, `/about/`); wisepops.com/customers/hallow; bible.com (`/`, `/app`); pray.com; lectio365.com; sacredspace.com (`/`, `/about/`); bibleproject.com (`/`, `/about/`); underbelly.is (BibleProject case study); emergencemagazine.org (`/about/`, essay index, "Behind the Scenes of Our Design Process"); webbyawards.com "Crafted with Code: Emergence Magazine"; commarts.com webpick; awwwards.com/sites/emergence-magazine; plough.com ("Retooling the Plough"); alabasterco.com; charitywater.org (`/`, `/about`, `/our-approach/100-percent-model`, `/stories/videos/the-spring`); patagonia.com (`/activism/`, `/stories/`, Footprint Chronicles stories, `/ownership/`); amrevmuseum.org (Finding Freedom interactive, about, primary sources, Webby and MUSE press releases); nmaahc.si.edu and si.edu Searchable Museum releases; technical.ly and jingdailyculture.com on the Searchable Museum; q42.nl and fabrique.com Rijksmuseum cases; winners.webbyawards.com (Rijksmuseum 2025; NGA 2026); nga.gov/press/webby-award-wins; annefrank.org (3D tour, VR publication); journalism.co.uk ("How the Guardian built Firestorm"); designrush.com and publicmediaalliance.org on *The Boat*; blog.nfb.ca and niemanstoryboard.org on *Welcome to Pine Point*; documentary.org and shortoftheweek.com on *Bear 71*; flowingdata.com (Pudding democracy piece, Nov 2025); maglr.com (SCMP Ozzy Osbourne, 2026 roundup); realclearpolitics.com and niemanstoryboard.org (*Snow Fall* opening).

*Critique and studies:* nngroup.com "Scrolljacking 101"; sites.gsu.edu rhetoric analysis of *Snow Fall* (2025); simonowens.net and Fast Company on the *Snow Fall* backlash; Slate (Feb 2024, Apr 2025), Salon (Apr 2025), freyaindia.co.uk "The Commodification of Christianity," thebereancall.org on Hallow; creativeboom.com "10 trends creatives are so over in 2026"; smoothui.dev "AI Design Slop"; studiomaydit.com and 925studios.co on AI-startup aesthetics; saasframe.io and studiomeyer.io on bento grids; digitalsilk.com and studiomeyer.io on kinetic typography; infinum.com, accessadvisors.nz, developer.apple.com forums, gulfnews.com on Liquid Glass; digitalstrategyforce.com on 2026 Awwwards 3D share; awwwards.com (Lando Norris, Site of the Year 2025); uxdesign.cc "Chat is the wrong interface for AI" (Aug 2026); xictron.com, prosemedia.com, eleken.co on dark patterns and the Digital Fairness Act; deceptive.design and builtin.com on confirmshaming; popupsmart.com 2025 benchmark and divimode.com on popups; morweb.org, thestorytellingnonprofit.com, fastcompany.com, upleaf.com on charity: water; siiimple.com, framerbite.com on Aeon and The Marginalian.

*Project documents:* `Build/Ministry/Features/Website-V2/CiC_Website_Design_V2.md` (frozen), `Decision-Log.md` (rulings of 2026-09-03 cited by heading), `cic-poc/frontend/src/components/Arrival.tsx` ("Revealing is witness, never recruitment").
