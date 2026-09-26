# 05 — Landing-page structure and choice flow: three ways in, of different cost and depth

**Workstream:** Website V2 · **Kind:** research brief (input to a design pass; decides nothing) · **Date:** 2026-09-08 · **Researched by:** Fable · **Companions:** `01-narrative-invitation-design-patterns.md` (pacing and emotional shape), `02-craft-and-visual-quality-bar.md` (surface), `03-trust-and-honest-sourcing-presentation.md` (honesty in the flow), `04-long-sentence-hero-headline-sizing.md` (the hook)

**Why this brief exists.** The homepage now has copy with heart and a page order it inherited rather than designed: a one-line hook, the ~300-word "Unfolding Story," a boxed "What's new" notice, a grid of tradition chairs (the Interview door, primary and immediately actionable), two picture-led "portal" cards (the Table, then the Atlas), and the support ask. Church in Conversation is unusual in offering three *genuinely different* ways in — **Interview** (one voice, one visitor; the primary path, closest to the project's name, cheapest to run at roughly $0.35 an hour), **Table** (up to three voices with the visitor at once; secondary, roughly $0.75 an hour), and **Atlas** (a free, no-conversation map of 290+ movements across twenty centuries; tertiary, currently the second portal). Mark asked for the *structural* side to be research-backed: the order the three are presented in, the visual hierarchy between them, how the page moves from reading into choosing and launching, and what the choosing surface itself should be. This brief answers those four questions with named, real examples and ends with a concrete page structure.

**How the research was done, honestly.** No external page was fetched live: every direct fetch from this sandbox is blocked at the egress proxy, as in briefs 01–04. Everything below rests on one of five kinds of evidence, tagged inline:

- **[indexed]** — a named site's own indexed page text as returned by web search (titles, copy, structure descriptions), not seen rendered.
- **[maker's account]** — a studio, agency, museum, or product team describing what it built and why, via indexed text or press.
- **[research]** — a peer-reviewed study, or a Nielsen Norman Group / Baymard usability finding, via indexed abstracts and summaries.
- **[industry claim]** — a vendor's own numbers or a marketing blog's figure; reported because it is what the trade repeats, never relied on.
- **[verified: repo]** — the CiC files read directly (`cic-website/index.html`, the Storyboard, the Decision-Log). **[inference]** marks my own reasoning or arithmetic.

Where a claim about a site's layout is my inference from its indexed text rather than something seen rendered, it says so. §8 lists what D-work should open in a real browser before anything is imitated. Roughly sixty searches were run; nothing was written from memory alone.

---

## 1. The short answer

Four things the evidence says, in order of confidence.

1. **One clear start, with the others plainly present.** The homepage-usability canon (Nielsen's 113 guidelines), government design systems, and every component library converge on one high-emphasis action per screen with secondary options visibly *different* rather than smaller. NN/g's finding is the sharp version: "without explicit differences, users are likely to assume all choices are the same or fret over the smallest distinctions." The three CiC doors differ on two honest axes — *how many voices* (one vs. several) and *talk vs. browse* — and the page should say so instead of presenting three look-alike cards.
2. **The museum and documentary world has a settled shape for guided-plus-free: overture → guided path → free exploration as the coda.** The Searchable Museum's intro video → parts; Nicky Case's *Evolution of Trust* ending in an optional sandbox; The Pudding's essays ending in "explore it yourself"; Google Earth's *Voyager* stories beside free-roam; Mitchell Whitelaw's "generous interfaces" argument that a collection should *show* itself before it asks for a query. For CiC this places the chairs (guided, primary) immediately after the story and the Atlas (free, browse) as the closing door — not a fourth thing competing with the chairs.
3. **The reading-to-choosing seam is where attention is lost, and it must be lean.** NN/g's 2018 eyetracking puts 57% of viewing time above the fold and 74% within the first two screenfuls; the CiC chairs currently begin around screenful two on desktop and three or four on a phone, behind a boxed banner and five lines of apparatus. The graceful transitions on record (the NYT's *You Draw It*, *Dimensions in Testimony*'s story-then-questions, Ideum's *Voices from the Front* interface) get the visitor from the last emotional line to the first face in one move, with the only text between them being a contract.
4. **The chooser should be faces, one action each, in a grid on desktop and a list on phones — not a scrolling catalogue.** NN/g: cards are for browsing, lists for scanning, tables for comparing; carousels on touch are "plagued by low discoverability and sequential access." The choosers people call effortless — Netflix profiles, *Finding Freedom*'s five portraits, Spotify's pick-five-artists — are big pictures, a name, one tap. The current chair cards carry a 72px portrait, two competing links, a three-line clamped blurb, and a dates-and-places row in a fixed-width horizontally scrolling strip: a catalogue record, not a person.

The structural recommendation (§7): **overture → one lean seam → the chairs (primary) with the Table as the second, quieter row of the same "sit down" movement → the Atlas full-width as the closing "explore everything else" door → the ask.** Table's higher cost is communicated by *saying so* — as AI "deep research" modes say "5–30 minutes" — not by hiding the card further down the page.

---

## 2. Where the page stands, and what already binds this brief [verified: repo]

**The live order** (`cic-website/index.html`, lines 193–347):

| # | Section | Width | What it is | Lines |
|---|---|---|---|---|
| 1 | `.hero` | 44rem, centred | Arriving mark, the 21-word hook (brief 04), hidden "Welcome back" line for returners | 193–201 |
| 2 | `.story` | 38rem reading column | "The Unfolding Story," four paragraphs, ~300 words; the last paragraph names the atlas, the stories, and the chair, in that order | 203–209 |
| 3 | `.whats-new-banner` | 64rem, boxed, sans | "The Cappadocian tradition has joined the table, and Church in History has been completely rebuilt." | 211–214 |
| 4 | `.who` | 64rem | Eyebrow → H2 "Who would you like to have a conversation with?" → scope line → disclosure paragraph (left rule) → instruction line → two era groups, each a horizontally scrolling row of fixed 232px chair cards → pilot note → cost caveat | 216–309 |
| 5 | `.portals` | 64rem, stacked | **Table** portal (painting, "Set your own table," Arriving mark on the CTA) then **Atlas** portal (river capture, "Church in History") | 311–330 |
| 6 | `.more-link` | — | "What's next →" | 331 |
| 7 | `.support` | 64rem card | "Running these conversations costs real money" + two Stripe buttons | 333–347 |

Each chair card carries: portrait (72px, links to the tradition page), name + role, tradition, dates · places, a three-line clamped tile, and two links — "Start the conversation →" (to `talk.html?worlds=…&mode=interview&from=index.html%23who`) and "More information" (to the tradition page).

**Three things worth recording before any recommendation:**

- **The two design documents and the live file disagree on portal order.** Storyboard §1.6 and the Decision-Log entry of 2026-09-03 both say "full width, stacked (Atlas over Table)"; the shipped `index.html` puts the Table portal first (line 312) and the Atlas second (line 321). This is documentation drift, not a ruling either way — and it is exactly the ordering question this brief is about. Whatever §7 recommends, the three should be reconciled.
- **The desktop chair row is 16px short of holding four chairs.** `--wide` is 64rem = 1024px with 1.25rem padding each side → 984px of content; four 232px chairs plus three 1.5rem gaps = 1000px. So the Imperial era's fourth chair (Albina) is always clipped on desktop, at every viewport, and the row scrolls. The Decision-Log verified the scroll works; the arithmetic says it is always needed. [inference — confirm in a browser]
- **The cost contract sits after the commitment.** The pilot note and the "about five conversations" caveat (lines 307–308) come *below* every "Start the conversation" link, so a visitor reads the terms after being offered the seat.

**Rulings this brief respects rather than reopens:** the chairs are "the one path that matters now" and the typed-question door was cut as a duplicate (Storyboard §1 history, 2026-09-03); portals are full-width because the river image "read as a blurry smudge" at half width (Decision-Log, 2026-09-03); chair cards "shouldn't get smaller" (same entry); the disclosure line keeps its position ahead of any conversation link (brief 03 §0); "no explaining the experience instead of having it" (brief 01 P8); the ask is last and small (brief 01 P6). Where §7 touches one of these it says so and offers a fallback.

---

## 3. Question 1 — Several genuine ways in, without diluting the primary one

### 3.1 How museums and archives pair a guided path with free exploration

**Mitchell Whitelaw, "Generous Interfaces for Digital Cultural Collections" (Digital Humanities Quarterly 9.1, 2015)** · [research]. The founding text for the browse-first side of this question. Its abstract: "Search is ungenerous: it withholds information, and demands a query," and it argues for "rich, browsable interfaces that reveal the scale and complexity of digital heritage collections." Generous interfaces "offer rich, browsable views; provide evocative samples of primary content; and support an understanding of context and relationships." Europeana later devoted an issue of its professional magazine to the idea. **Take:** the Atlas *is* CiC's generous interface — it shows the whole twenty centuries before anyone asks a question. On the homepage, its picture should do that showing (Mark's full-width ruling is already this instinct), and the copy beside it should say plainly what the chairs cannot yet cover.

**Google Arts & Culture** · [indexed]. Its navigation was consolidated to three verbs — **Inspire** (curated feed), **Play** (cultural games), **Explore** (browse the collection) — with institutional "Stories" and 170+ "Themes" as the curated layer. A 2025 Pratt design critique notes the navigation "can be cumbersome" [critique]. **Take:** three doors named as *what you do* (be shown / play / browse) rather than what the institution calls its products; and a caution that a platform of this size cannot keep the three from competing — CiC, with three doors and seven voices, can.

**Google Earth — *Voyager*** · [indexed]. "A showcase of guided tours, intended to curate your experience," partner-authored, launched from a single button beside the free-roam globe; "projects" let people build their own. **Take:** the cleanest large-scale example of *guided beside free* where neither hides the other: the guided stories are one control on top of the free world, and the free world is the default state.

**The Met's *Heilbrunn Timeline of Art History*** (relaunched 2016, interface by CHIPS) · [indexed]. Four named components — Essays, Works of Art, Chronologies, Keywords — over "more than 1,000 essays, 8,000 works of art, 300 chronologies"; "fully optimized to be responsive." **Take:** a historical archive with distinct ways in *names each kind of thing* and lets a keyword system cross-link them, so the visitor is never asked to pick a silo up front. CiC's tradition pages and the Atlas's movement entries are the two "kinds" that should cross-link the same way.

**Anne Frank House** (DOOR / IN10; three internet awards 2019) · [maker's account]. The site was reorganised around "the four most important elements of their story: the hiding place, Anne Frank's diary, the people in hiding and their helpers, and the historical context," with the Secret Annex Online as the free-exploration piece beside them. Communication Arts described the result as a "corporate + storytelling" split. **Take:** name a *small* number of story elements and let the immersive/free surface sit beside them as its own thing — not as a fifth element.

**Smithsonian NMAAHC *Searchable Museum*** (Fearless, 2021) · [maker's account, carried from brief 01]. "Greeted by an introductory video, before entering four discrete parts, each split into chapters." **Take:** overture first, then a small numbered set of guided parts; search is present but not the front door.

**Voices from the Front** (National WWII Museum, Ideum UI, 2024) · [maker's account]. Eighteen interviewees; the Forbes Gallery version "provides visitors a way to filter the different kinds of experiences to choose which they'd like to learn about, in order to narrow their choice from among the 18." **Take:** when the roster grows past a handful, the museum adds a *filter by kind of experience* rather than more cards — the era heads CiC already has are this filter, and they will carry the roster to twenty before anything else is needed.

**Numiko, "Best Museum and Gallery Websites 2026"** · [critique]. The roundup's own criterion: a good museum site "gives visitors all the information they need … in a clear way," a great one does that "in a way that creates a sense of excitement and wonder, taking users on a serendipitous journey of discovery." Examples: Guggenheim Bilbao's full-screen hero video with "a simple tile-based design" beneath; the Van Gogh Museum's sideways-scrolling homepage (noted as unusual, not recommended). **Take:** the professional bar for the category is *clarity first, wonder second* — the two are ordered, not traded.

### 3.2 The "one clear start" rule, from the usability canon and design systems

- **Jakob Nielsen, 113 homepage guidelines (2001; still NN/g's reference)** · [research, via a secondary transcription]. "Emphasize the highest priority tasks so that users have a clear starting point on the homepage"; give them "a prominent location such as the upper-middle of the page" without "a lot of visual competition"; "keep the number of core tasks small (1–4) and the area around them clear." **Take:** one to four *tasks*, not one to four *cards* — CiC's three doors are inside the limit; what the guideline forbids is visual competition around the primary one.
- **NN/g, "'Get Started' Stops Users" (2017)** · [research]. "A generic Get Started call-to-action attracts clicks, but also misleads users and acts as a roadblock for those looking to get information." **Take:** the chairs' "Start the conversation →" is specific; the portals' "Open Church in History →" and "Set your own table →" are specific. Keep every CTA a verb plus the real noun.
- **NN/g, "Explicitly State the Difference Between Options"** (updated from a 2013 Nielsen piece) · [research]. "Without explicit differences, users are likely to assume all choices are the same or fret over the smallest distinctions"; emphasising the attributes that differ "will greatly improve users' confidence." **Take:** the single most useful sentence for CiC's three doors. Interview vs. Table differ on *how many voices*; conversation vs. Atlas differ on *talk vs. browse*. Neither difference is currently stated in one place; each card describes itself in isolation.
- **NN/g, "Audience-Based Navigation: 5 Reasons to Avoid It"** · [research]. Users don't know which group they belong to, content overlaps, "users worry they're missing out," they pick the wrong group, and usability degrades. **Take:** CiC's split is by *mode* (talk to one / talk to several / browse), not by audience (pastor / academic / seeker). That is the right axis — but the same warning applies to any mode-picker placed *before* the overture: a visitor asked "which kind of thing do you want?" on arrival will worry about what the other doors hold. The doors come after the story.
- **GOV.UK publishing components; Scottish Government Design System** · [indexed]. "Use buttons to move through a transaction, aim to use only one button per page"; "Use only one primary button on a page (or section of a page). More than one can confuse users." Component libraries (Carbon and others) say the same: "a layout should contain a single high-emphasis button." **Take:** per *section*, one high-emphasis action — which also licenses the chairs section to have its own primary (the seat) and the Atlas section its own (the map), as long as they are separated by a section boundary and differ in emphasis.
- **NN/g, "Progressive Disclosure"** · [research]. "Defers advanced or rarely used features to a secondary screen"; "initially, users are shown only a few of the most important options." Secondary coverage cites a 2006 study with 30–50% faster initial task completion when advanced features were deferred [industry claim — not verified against the primary]. **Take:** the Table is the advanced mode of the conversation; it belongs one step *after* the simple mode, not beside it as an equal.

### 3.3 The guided → sandbox shape

- **Nicky Case, *The Evolution of Trust* (2017)** · [indexed + critique]. A thirty-minute guided explorable; "at the end of most of Nicky Case's explorables, there is a 'Sandbox Mode'"; it is "totally optional, and players are free to skip it or play around"; "the only time players can dive away from the script and create their own narrative." **Take:** the strongest single precedent for where the Atlas belongs relative to the chairs: free exploration is the *reward at the end of the guided thing*, offered, never required.
- **The Pudding's essay endings** · [indexed]. Essays close with explore-it-yourself tools ("Explore satellite imagery of all of them"; "Explore the Buttolph Collection from the New York Public Library's archive"). **Take:** the same shape in journalism — narrative, then the open dataset.
- **Bret Victor, "Explorable Explanations" (2011)** · [indexed]. "People currently think of text as information to be consumed. I want text to be used as an environment to think in"; explorables "deliberately guide the attention of their audience" as distinct from isolated widgets. **Take:** the reason guided comes first — a bare sandbox does not tell the visitor what to look for.
- **Prison Valley** (Upian / ARTE, 2010; Web Documentary Award) · [maker's account]. The visitor "checks into a room at the Riviera Motel" — a hub — then meets characters; "interactive zones" open along the way, and "when Internet users exit the extras, they can take up the narrative where they left off." **Take:** the return path. CiC's `from=index.html#who` parameter on every seat link already does this; keep it, and give the Atlas the same way back.

### 3.4 What the good ones share

1. **Doors are named by the visitor's act** (Inspire / Play / Explore; Watch / Explore / Listen in brief 01), and the difference between them is said once, plainly.
2. **The guided path is the default and comes first; free exploration is the coda**, present from the start as a picture or a globe but entered last.
3. **Three or four named parts, never a wall** (Anne Frank House's four elements; Searchable Museum's four parts; Heilbrunn's four components).
4. **A filter, not more cards, when the roster grows** (Voices from the Front's kinds of experience; CiC's era heads).
5. **One high-emphasis action per section**, with a section boundary between sections that each need their own.
6. **A way back to the hub** after any door.

---

## 4. Question 2 — From a moving paragraph to "now choose": the seam

### 4.1 Why the seam is where a page is won or lost

**NN/g, "Scrolling and Attention" (2018 study; 130,000 fixations, 120 participants)** · [research]. "Users spent about 57% of their page-viewing time above the fold, and 74% of the viewing time was spent in the first two screenfuls, up to 2160px," with "a sharp decrease in attention following the fold." **Applied to CiC** [inference — line counts modelled, not measured]: at 17px/1.65 in a 38rem column the story runs roughly 20–24 lines (≈650–750px) beneath a ~350px hero, so the chairs begin at about the second screenful on a desktop — right at the 74% boundary — and, at ~40 characters a line on a phone, around the third or fourth screenful. Everything between the story's last sentence and the first face is therefore being paid for with the scarcest attention on the page.

**NN/g, carousels and banners** · [research]. "Banner blindness": boxed, promotional-looking elements are "noticed, but often ignored as advertising or irrelevant content." **Applied:** the "What's new" box — sans, bordered, rounded, full-`--wide` — sits in the seam and has the shape of the one element NN/g says readers have learned to skip. The news it carries is real; its *placement and shape* make it read as an interruption between the invitation and the faces.

### 4.2 Museums and installations: overture, contract, then the chooser

**Dimensions in Testimony** (USC Shoah Foundation; Illinois Holocaust Museum, 2017; thirteen survivors) · [maker's account]. The format "enables survivors to tell their deeply moving personal stories and then respond to questions from the audience." **Take:** the transition from listening to asking is built into the experience: the survivor speaks first, at length; the visitor's question comes *after* they have heard a voice. This is the museum form of brief 01's P8 and brief 03's R3 — the visitor should have heard one real line before being asked to choose whom to ask.

**Voices from the Front** (Ideum) · [maker's account]. The interface "guides visitors through the process, provides enough information and prompting to inspire the visitor to ask questions of their own, and removes any discomfort in interacting with a novel system"; the museum's brief was to help visitors "understand Voices from the Front, differentiate among interviewees, and become comfortable with initiating conversations." **Take:** three jobs for the seam, in the museum's own words — *understand what this is, tell the people apart, feel comfortable starting.* Notice what is absent: instructions. Ideum's answer to discomfort was prompting (suggested questions), not a how-to line.

**Finding Freedom** (Museum of the American Revolution; AREA 17; Webby 2026) · [maker's account]. Five people, first-person narratives with decision points; "no portraits or images exist for Andrew, Deborah, Eve, Jack, or London," so Wood Ronsaville Harlan painted them "with respect and attention to historical records." Teacher guides debrief "the decision-making process, what was persuasive." **Take:** the chooser is five painted faces and five names; the *choice* the visitor is invited to weigh is the person's, inside the story, not the visitor's at the door. Whether the interactive opens with an introduction before the five faces could not be verified from indexed text — D-work should open it (§8).

**Bear 71** (NFB / Jam3, 2012) · [maker's account, carried from brief 01]. The opening "delivers an announcement on the length of the story" before the wordmark and the video; the map is entered after. Jam3's stated design problems: "how Bear 71's narration would exist in a non-linear user experience, when the audience would have control of the visuals versus when the story would take over." **Take:** the contract at the door (how long, what kind of thing) is what makes the later hand-off to control feel fair.

**Museum kiosks generally** · [indexed, weak]. An "attract screen" draws attention in idle mode and, on touch, yields to the menu; guidance stresses "an idle mode that invites interaction without overwhelming the exhibit." **Take:** CiC's hero (mark + hook) is the attract screen; the scroll is the touch. The pattern is fine and needs no further apparatus.

### 4.3 Journalism: the micro-interaction that primes the choice

**NYT, *You Draw It* (Aisch, Cox, Quealy, 2015–17)** · [critique + maker's account]. The series "proposed a model of an article interspersed with visual modules that forced the user to interact in order to access the analytical text," built on "the idea that the surprising nature of the correlation is more compelling after one has been forced to think about it first"; Cox: the design "wasn't ultimately about typography and whitespace, but about empathy." **Take:** the most-studied graceful transition in the genre works by asking for a *tiny, reversible* act before the reveal. For CiC the equivalent is already latent in the two-tier link on each chair — the portrait (light: read about her) before the seat (heavy: start) — and could be strengthened by making the light act the visible one.

**NYT, *How Y'all, Youse and You Guys Talk* (Josh Katz, 2013)** · [indexed]. The most-viewed page in the paper's history; there is no narrative before the quiz — the first screen *is* the first question. **Take:** the opposite pole. When the interaction itself is the hook, no overture is needed. CiC has ruled the story is the overture (brief 01 P2), so this pole is not CiC's — but it shows the chooser can come very early *if it is light*, which argues for a skip-to-the-voices link for the visitor who arrives already knowing.

**The Pudding** (§3.3) · [indexed]. Narrative first, open tool last.

### 4.4 Interactive documentary: the hub after the prologue

- **Prison Valley** (§3.3): a motel room as the hub; objects in the room open the material; the narrative resumes where it was left. [maker's account]
- **Highrise: Out My Window** (NFB, Helios, 2010) · [maker's account]. "The interface evokes a residential apartment building, where each window … leads to an apartment in a different city — 13 in all"; click a window, enter, click people or objects. No longer available (Flash). **Take:** the chooser as a *place* — thirteen lit windows in one façade — rather than a list. A row of portraits under an era heading is the same idea at CiC's scale.
- **Hollow** (Elaine McMillion Sheldon, 2013; Peabody) · [maker's account]. "Thirty video portraits … distributed across five thematic sections"; designed as a "lean forward and lean back" experience. **Take:** thirty faces became navigable by grouping them into five sections — the era-head pattern, proven at four times CiC's roster.
- **Journey to the End of Coal** (Honkytonk, 2008; 1.5 million page views on lemonde.fr) · [indexed]. Choose-your-own-adventure; the visitor is "positioned as an investigative journalist." **Take:** giving the visitor a *role* at the hand-off ("you're one of the four chairs," which the Table copy already does) is a known way to make the choice feel like entering rather than configuring.
- **Sandra Gaudenzi's four i-doc modes** · [research]. Hypertext (branching), conversational (game-like exchange), participatory (co-creation), experiential (embodied space). **Take:** CiC's Atlas is hypertext, its Interview and Table are conversational. The literature treats these as different *relationships with the visitor*, which is the deepest reason not to present them as three equal cards.

### 4.5 Graceful versus jarring, as the examples show it

| Graceful | Jarring | Evidence |
|---|---|---|
| The last sentence of the story hands directly to the question; one contract line between them | A boxed notice, an eyebrow, a scope line, a disclosure block, and an instruction line between the story and the faces | NN/g attention gradient; banner blindness; Ideum's three jobs |
| The visitor has heard a voice before choosing whom to ask | The first voice is heard only after committing to a seat | Dimensions in Testimony; brief 01 P8; brief 03 R3 |
| A tiny reversible act precedes the commitment (draw the line; open a window; read about her) | The first available act is the full commitment ("Start the conversation") | You Draw It; Highrise; Finding Freedom |
| The contract (how long, what it costs, what it won't do) is read before the door | The cost caveat sits below the seats | Bear 71; charity: water's 100%; live `index.html` lines 307–308 |
| A skip for those who already know | Every visitor must scroll the overture | Evolution of Trust's optional sandbox; the live side-door for returners (keep) |
| A way back to the hub after any door | Dead ends | Prison Valley; the live `from=` parameter (keep) |

---

## 5. Question 3 — Order, size, and placement for asymmetric options

### 5.1 What position does to choice (peer-reviewed)

- **Murphy, Hofacker & Mizerski, "Primacy and Recency Effects on Clicking Behavior" (JCMC, 2006)** · [research]. Two field experiments on live sites: "the higher a link's position in a list of links, the greater the probability that visitors will click on that link" (primacy), with a smaller recency bump for the last item. **Applied:** in CiC's vertical stack, the first door after the story will be chosen most, the last a little more than the middle. That is a reason to put the primary first — and a reason the *last* portal position is not the graveyard it looks like.
- **Valenzuela & Raghubir, "Position-based beliefs: The center-stage effect" (J. Consumer Psychology, 2009)** · [research]. Five experiments: people "assume that retailers place the most popular product options in the middle of an array," choose the centre more, and the effect is "driven by inferences of product popularity rather than higher levels of attention." **Rodway, Schepman & Lambert (Applied Cognitive Psychology, 2012)** replicated it with five alternatives "in either a horizontal or a vertical fashion" — physical socks and web images alike. **Applied:** with three chairs in a row, Theon (centre) will be picked more than Chloe or Mar Yausep for no reason of his own; with four, there is no true centre. This is not something to game — chronological order is the honest order — but it is something to *know* when reading pilot usage numbers, and a reason to prefer a wrapping grid (which dilutes any single centre) over a single row.
- **Chernev, Böckenholt & Goodman, "Choice overload: A conceptual review and meta-analysis" (JCP, 2015; 99 observations)** · [research]. Whether more options hurt depends on four moderators: choice-set complexity, decision-task difficulty, **preference uncertainty**, and decision goal. **Applied:** seven chairs is not a large set; the risk is preference uncertainty — a visitor who does not yet know what "Syriac" or "Cappadocian" means. The remedy the meta-analysis implies is not fewer chairs but *less uncertainty per chair*: a face, a place, one line of what she is like, and an era heading that does the grouping.

### 5.2 What size, styling, and layout do (usability studies)

- **NN/g, "Flat UI Elements Attract Less Attention and Cause Uncertainty"** · [research]. Users "spent 22% more time on web pages that had weak signifiers"; ghost buttons — "text with a thin border and no background" — are the named weak signifier. **Applied:** CiC deliberately uses underlined text links rather than buttons (brief 01's anti-funnel register); that is fine for the *primary* action only if it is unmistakably a link (the current madder underline is). A secondary door that is *also* a bordered card with a text link is at risk of reading as inert. The differentiation between primary and secondary has to come from something other than button-versus-ghost.
- **NN/g, "Zigzag Image–Text Layouts Make Scanning Less Efficient" (eyetracking)** · [research]. "Decorative images used in an alternating list layout caused users to stumble," but "when images had informational value and were aligned or alternating, users studied them in detail and referenced them multiple times." **Applied:** the river capture and the Table painting are informational, not decorative, so a stacked or side-by-side treatment is fine either way — the evidence supports Mark's full-width ruling and does not forbid a narrower Table image, as long as the image carries information.
- **NN/g, "Cards: UI-Component Definition"** · [research]. "Cards are for browsing, lists are for scanning, and tables are for comparing"; "card layouts typically deemphasize the ranking of content." **Applied:** exactly the property wanted for the seven chairs (no ranking) and exactly the property *not* wanted for the three doors (which are ranked). Three equal cards for three unequal doors is the wrong component.
- **NN/g, "Carousels on Mobile Devices"** · [research]. Touch carousels "are plagued by low discoverability and sequential access"; swipe "creates the problem of swipe ambiguity on iOS." **Applied:** the chair rows are horizontally scrolling strips of fixed 232px cards; on a 390px phone about a chair and a half is visible and the Imperial era needs three swipes. The Decision-Log's reason for the rows — chairs must not shrink — is honoured equally by a vertical list, where each chair gets *wider*.

### 5.3 The pricing-page pattern — what it teaches and what it must not lend

The three-tier pricing page is the most A/B-tested "three unequal options" layout on the web. The trade repeats large numbers for it — a highlighted middle tier "increases selection of the middle option by 38%," a "Most Popular" badge lifts that tier "30–40%," one case "moved conversion from 1.2% to 3.1%" — all **[industry claim]**, from conversion-marketing blogs, none verifiable here, and all consistent with the peer-reviewed centre-stage mechanism above (people infer popularity from position). **What it teaches:** hierarchy among three options is produced by *one* differentiated cell — border, size, or position — not by three competing treatments. **What it must not lend:** the badge. "Most popular" is manufactured social proof; brief 01 §4.6 already rules urgency and superlatives out of CiC's register, and the centre-stage research shows the badge works precisely by making people "follow the herd." CiC's differentiation must be honest difference (one voice / three voices / the whole map), stated, not popularity, implied.

### 5.4 Real examples of a costlier or slower mode framed honestly beside the primary one

- **"Deep research" modes (ChatGPT, Gemini, Perplexity, 2025–26)** · [indexed + critique]. The costlier mode is a *named option beside the default*, and the interface says what it costs the user: "5 to 30 minutes per query because they optimize for thoroughness"; ChatGPT "displays research steps in an expandable sheet," Gemini uses "a two-panel design that separates the conversation from research details." **Take:** the clearest current precedent for what the Table needs — a plain statement of *slower, deeper, more* in the option itself, so the visitor chooses it knowingly. The Table's copy currently says what it *is* ("bring two or three of them to one table") but not what it *costs in tempo or to run*, and the page communicates its secondary status only by putting it lower.
- **NotebookLM's three panels — Sources / Chat / Studio** · [indexed]. The primary act (chat with citations) has its own panel; the richer generated artefacts (Audio Overview's two hosts, timelines, FAQs) live in Studio beside it, generated on request. **Take:** a multi-voice artefact placed *beside* the single-voice conversation as its elaboration, not as a separate destination.
- **Google Earth *Voyager*** (§3.1): guided stories as one control on top of the free globe. [indexed]
- **charity: water** (brief 01): the ask last, and the cost promise ("100%") stated at the top. [indexed]

### 5.5 The free tertiary path that must not look like an afterthought

Whitelaw's argument (§3.1) is the strongest reason the Atlas cannot be a footnote: it is the only surface that shows the *whole* of what CiC is about, and the chairs cover four centuries of twenty. Histography (Matan Stauber, 2015; Smashing Magazine, Communication Arts) · [indexed] — "every dot … represents a historic event," fourteen billion years, "as a user scrolls, the dots jumble and then reassemble" — is the nearest well-known cousin of the Atlas river and was received, everywhere it was covered, as a *destination*, not a widget. The Heilbrunn Timeline's four cross-linked components show the archive-side structure that lets a browse surface and a story surface refer to each other. **Take:** the Atlas earns full width and the closing position; what it does not need is to compete with the chairs for the first door. Its earlier presence on the page should be a *sentence* — the honest contract that the voices so far are four centuries and the rest is on the map — not a second card.

---

## 6. Question 4 — The choosing and launching surface itself

### 6.1 Component choice: cards, lists, tables, or a guided picker

| Component | Evidence says it suits | Suits CiC when |
|---|---|---|
| **Card grid** | Browsing without a target; heterogeneous items; visually driven items (NN/g cards; Baymard "grid for visually driven products") | Desktop chairs — seven faces, no ranking, the visitor is browsing |
| **Vertical list** | Scanning; space-efficient; spec-driven items (NN/g; Baymard "list view for spec-heavy"); the pattern Duolingo uses for "Choose a Course" [indexed] | Phone chairs — one column, each row full width, portrait left |
| **Table** | Comparing attributes across rows (NN/g; Baymard product tables) | Never on the homepage; the record store and About |
| **Guided picker / wizard** | "Liberating in cases where people don't care about their choices or don't know enough to make a decision"; "processes performed only occasionally" (NN/g Wizards) | An *optional* "not sure who?" beside the grid, once the roster passes what era heads can carry (§6.3) |
| **Free-text prompt** | NN/g chatbot study: "users complained when a bot did not allow them to pick an option and instead required them to type"; both inputs should exist | Not as the door (ruled out 2026-09-03); fine inside the conversation |

### 6.2 Named choosers, and why each feels the way it does

- **Netflix, profile selection / 2025 welcome screen** · [critique — Raw.Studio, UX Planet; not seen rendered]. "A bold, cinematic screen with a full-bleed hero image … paired with subtle profile icons anchored to the bottom"; "one clear, compelling starting point instead of overwhelming the user with too many choices." **Why it feels effortless:** large picture, a name, one tap, no text, no instructions.
- **Finding Freedom** · [maker's account]. Five painted faces, five names, first-person. **Why:** the roster is small enough to see whole; every portrait is *made* (brief 02 §3); the choice is "whose story," not "which product."
- **Voices from the Front** · [maker's account]. Eighteen faces with a filter by kind of experience; prompting instead of instruction. **Why:** at eighteen the museum added a filter and suggested questions — not more text per person.
- **Spotify, "choose five or more artists"** · [indexed + critique]. Pictures of artists; a critique notes "displaying artists' pictures adds extensive stickiness value — the user feels much more connected." **Why:** the face is the whole card.
- **Duolingo, "Choose a Course"** · [indexed]. "A list of languages topped with a header simply reading 'Choose a Course'"; then goal, then motivation, each one screen. **Why:** a list is right when items are near-identical in kind and the visitor scans for a known one; the header is a question, and there is exactly one thing to do per screen.
- **Highrise: Out My Window** · [maker's account]. Thirteen windows in one façade. **Why:** the chooser is a *place*; each option is a lit window, not a record.
- **Game "character select" screens** (Overwatch as the usual reference; Game UI Database catalogue) · [critique, mixed quality]. Characters must be "identifiable by silhouette alone"; one case study replaced "a static grid with a vertical scroll layout to improve scannability." **Why it transfers:** thirty years of a genre whose only job is *pick a person and go* — big portrait, name, role glyph, one confirm. And the same grid-on-wide / list-on-narrow split the web evidence reaches independently.

### 6.3 Guided pickers, and where they earn a place

- **Headspace** · [critique]. "What brings you to Headspace?" — six options including "Just checking it out." **Take:** an intent question with an honest opt-out is the lightest possible guide.
- **charity: water, *Someone Like You*** · [indexed]. "You answer a few questions, then the page reloads and you see the video portrait of the person most like you" — one person, from four hundred stories collected in two weeks. **Take:** the picker's output is an *introduction to a person*, which is exactly what a CiC guide should return: a chair, with a reason.
- **Apple, "Help Me Choose" (June 2024)** · [indexed]. A quiz beside the Mac grid asking what the machine will be used for, where, with what; follow-ups per answer. **Take:** the grid stays the primary surface; the guide is a *link beside it* for the uncertain.
- **NN/g Wizards** (§6.1) and **NN/g chatbots** — quick replies expected; forced typing resented. [research]
- **Typeform**'s one-question-at-a-time format reports 47.3% completion across 568M submissions **[industry claim — vendor]**; secondary coverage adds that "for forms with fewer than 5 fields, traditional formats often perform equally well or better" [industry claim]. **Take:** the conversational-form advantage is for *long* forms. A two-question CiC guide gains nothing from that format; it gains from being optional, short, and ending in a face.

**Where this leaves the guide for CiC:** the typed-question door was cut on 2026-09-03 as a duplicate of the chairs, and that ruling stands. A two-tap *intent* guide ("What brought you here?" → "Then sit with Papnoute; here's why") is a different thing — but with seven chairs under two era heads it is not yet needed (Chernev's moderators; Voices from the Front added its filter at eighteen). Recommend: **defer** until the roster reaches roughly twelve, and design it then as Apple does — a link beside the grid, never in front of it.

### 6.4 What makes a chooser feel like a form (and the live chair does most of these)

| Form tell | Effortless alternative | Evidence |
|---|---|---|
| Two competing links per item ("Start" and "More information") | One action per card; the name/portrait is the "about" link and reads as such | Heydon Pickering, *Inclusive Components: Cards* — put the link on "the main distinctive piece of information (like a heading)" not a generic call; Adrian Roselli on block links [indexed] |
| A spec row (dates · places · role) and a clamped three-line blurb | Face, name, tradition, one short line; the rest on the tradition page | Baymard: spec rows belong to list/table views of spec-driven goods; NN/g explicit-differences: state the *differentiating* attribute, not every attribute |
| A 72px portrait beside ~120 words | The portrait is the card (96–128px on desktop; full row height on phone) | Netflix, Spotify, Finding Freedom, Highrise, character select |
| An instruction line ("Start the conversation directly, or click anyone's picture first…") | None; the two affordances are self-evident | Ideum: prompting, not instruction; Netflix needs no how-to |
| A horizontally scrolling strip with snap points | Wrapping grid (desktop) / vertical list (phone) | NN/g carousels on mobile; the 16px overflow arithmetic in §2 |
| The terms after the commit button | The contract line above the first card | Bear 71; brief 01 P1 |

None of this shrinks a card — it *removes text and enlarges the face* — so it sits inside the 2026-09-03 ruling rather than against it.

---

## 7. Synthesis — the page structure the evidence recommends

**The principle in one line.** *Overture, then one lean seam, then the primary act with its deeper variant beneath it, then the free world as the closing door, then the ask.* Hierarchy comes from order, from stated difference, and from one high-emphasis action per section — never from shrinking or hiding the secondary doors, and never from popularity badges.

### 7.1 The recommended page, top to bottom

| # | Section | Register and width | What changes, and the evidence for it |
|---|---|---|---|
| 1 | **Hero** | 44rem, centred; mark + hook (sizes per brief 04) | *Add* one muted line under the hook that is both contract and skip: the reading length, what follows, and a jump link to the chairs (Mark's words; e.g. "A two-minute story, then seven voices you can sit with. Skip to the voices ↓"). *Keep* the returners' side door. — Bear 71's running-time contract; Evolution of Trust's optional skip; NN/g attention gradient (phone visitors reach the chairs at screen 3–4). |
| 2 | **The Unfolding Story** | 38rem reading column, unchanged copy | Nothing structural. Note that its last paragraph already orders the doors atlas → stories → *chair*, so the last thing read is the first door offered. |
| 3 | **The seam** | 38rem, in the story's own register — no box, no eyebrow, no rule | *Remove* the "What's new" banner from here (one italic line under the hook, or the What's Next line, is where news belongs). *Collapse* scope + disclosure + instruction + pilot caveat to **two sentences in the flow**: (a) the contract — seven voices from the first four centuries, that each conversation costs real money to run, and the "about five" ask — and (b) the constraint-promise disclosure in brief 03's R5 form. *Add* the one-line honest pointer that the other sixteen centuries are on the map (a text link, not a card). *Drop* the instruction line. — NN/g banner blindness; CME "the box nobody saw" (brief 03 F1); Ideum's three jobs; NN/g explicit differences; Whitelaw. |
| 4 | **H2 + the chairs — the primary door** | 64rem | H2 stays the question it is. **Desktop:** a wrapping grid (`auto-fit, minmax(220px, 1fr)` or 3+4 explicit), so all seven are visible at once and no row scrolls. **Phone:** a vertical list, each chair a full-width row, portrait left. **Each chair:** portrait 96–128px (desktop) or row-height (phone); name + tradition; one line of place/date; **one action** — "Start the conversation →" — and the portrait/name as the single "about" link; the three-line tile moves to the tradition page. Era heads stay as the grouping. Chronological order within an era. — NN/g cards for browsing / lists for scanning; NN/g mobile carousels; Chernev (reduce uncertainty per item, not the count); Pickering; the centre-stage effect (dilute it; don't game it); the §2 overflow arithmetic. |
| 5 | **The Table — the second row of the same "sit down" movement** | 64rem section, one visual step below the chairs: image at 44rem (or full width but shorter), eyebrow "The Table," two sentences, CTA with the Arriving mark | *Move* it out of `.portals` into the tail of the chairs section, directly beneath them, so its relation to the chairs (same act, more voices) is spatial. *Say* its difference and its cost honestly in the copy: several voices, slower, costlier for the project to run, worth it once you know who you'd seat. — NN/g progressive disclosure (the advanced mode one step after the simple one); NotebookLM's Studio beside Chat; deep-research modes' "5–30 minutes"; NN/g explicit differences. **Fallback** if Mark keeps the portal card: keep it a portal but *above* the Atlas, with the honest-cost sentence added. |
| 6 | **The Atlas — full-width closing door** | 64rem, the river capture full width (unchanged), eyebrow, H2 "Church in History," two sentences, CTA | *Keep* full width (Mark's ruling; NN/g zigzag supports it because the image is informational). *Reframe* as the coda: everything else — twenty centuries, 290 movements — is here to explore freely, no conversation needed. *Give it a way back* (a `from=` parameter like the seats). — Evolution of Trust's sandbox; The Pudding's endings; Whitelaw; Murphy's recency bump (the last position is not a graveyard). |
| 7 | **What's next →** | one line | Absorbs the "What's new" sentence if it does not go under the hook. |
| 8 | **Support** | 64rem card, unchanged | Last and small, as ruled (brief 01 P6). The cost *contract* has moved up to the seam; this card is the *ask*. |

### 7.2 Why this order and not another

- **Chairs before Table:** progressive disclosure; one-voice is the simple mode of the same act; Table's cost is stated, not hidden by position.
- **Table before Atlas:** because Table is *the same kind of thing* as the chairs and Atlas is not (Gaudenzi's conversational vs. hypertext); the two conversation surfaces form one movement, the browse surface another. This is also the live file's order — and the opposite of the Storyboard's and Decision-Log's stated "Atlas over Table." Reconcile the documents to whichever Mark rules.
- **Atlas last, but present early as a sentence:** the guided → sandbox shape (Case, The Pudding, Voyager) puts free exploration at the end; Whitelaw and the four-centuries gap put an honest pointer to it in the seam. One link early, one full-width door late; never two cards.
- **Ask after all three doors:** unchanged; charity: water, Sacred Space (brief 01).

### 7.3 How the hierarchy is carried, concretely

| | Interview (chairs) | Table | Atlas |
|---|---|---|---|
| Position | First after the seam | Directly beneath the chairs, same section | Own section, last before the ask |
| Size | Seven faces, grid/list, largest total footprint | One image at 44rem or a shorter full-width band | One image, full width |
| Emphasis | The page's one high-emphasis action per chair | One CTA, with the Arriving mark | One CTA |
| Difference stated | "one voice, one of you" | "several voices at once — slower, and costlier to run" | "no conversation — the whole map, free to explore" |
| Contract | above the first card | in its own two sentences | "free" in its own sentence |

### 7.4 Alternatives considered and set aside

1. **Three equal portals (a bento of doors).** Rejected: NN/g cards de-emphasise ranking and the doors *are* ranked; brief 01 §4.3 already rules out the bento register.
2. **A mode switcher at the top ("Interview · Table · Atlas").** Rejected: forces the audience-navigation problem (users "worry they're missing out," pick wrong) before the overture; brief 01 P2 puts every door after the story.
3. **Atlas first, because it is free and "generous."** Seriously considered — Whitelaw is persuasive, and a visitor whose question lives in 1517 has no chair. Set aside for the homepage because the chairs are the mission's primary act and the guided → sandbox evidence is consistent; the seam's one-line pointer gives that visitor a path without a second card. Revisit if pilot data shows arrivals with post-451 questions dominating.
4. **A guided picker now.** Deferred to a roster of ~12 (§6.3); when built, a link beside the grid (Apple), returning a person (charity: water), never the door itself (ruling of 2026-09-03).
5. **Shrinking the story on phones.** Not proposed: the copy is ruled; the skip link under the hook is the structural answer.

---

## 8. What this brief could not verify, and what D-work should do next

- **Nothing external was seen rendered.** Six things should be opened in a real browser and captured into `Sandbox/` before imitation: `amrevmuseum.org/interactives/finding-freedom` (does it open with an introduction before the five faces? how are the faces laid out at 390px?); `ncase.me/trust` (the sandbox hand-off at the end); `artsandculture.google.com` (the Inspire/Play/Explore nav and how Stories sit beside Explore); `metmuseum.org/toah` (four components on one landing); one Pudding essay with an explore-ending; and a NotebookLM notebook (Chat beside Studio).
- **The Finding Freedom opening sequence**, the **Netflix welcome screen** claims (secondary blogs), and the **progressive-disclosure "30–50% faster"** figure are carried from secondary sources and flagged as such.
- **All pricing-page percentages** are marketing claims; only the centre-stage mechanism behind them is peer-reviewed.
- **The line-count and screenful estimates** in §4.1 and the 16px overflow in §2 are arithmetic; screenshot at 360, 390, 768 and 1280px to confirm where the first chair actually lands, and whether Albina's chair is clipped at 1280px.
- **The Table painting at 44rem**: verify in a browser that three figures read at reading-column width before choosing that over a shorter full-width band — the full-width ruling was made for the river's threads, which blur; a portrait may not.
- **The portal-order drift** between `index.html` (Table, Atlas) and the Storyboard/Decision-Log ("Atlas over Table") needs a one-line ruling either way, recorded in `Decision-Log.md`.
- Nothing here changes Design V2's frozen type, colour, motion inventory, or accessibility floor. The chair redesign in §7.1 row 4 keeps every 44px target and the no-JS state (a grid and a list are both pure CSS).

---

## Sources consulted

*Usability research (via indexed abstracts and summaries):* nngroup.com — "113 Design Guidelines for Homepage Usability" and "Top 10 Guidelines for Homepage Usability" (with the liamdelahunty.com transcription of the 113); "'Get Started' Stops Users"; "Explicitly State the Difference Between Options"; "Audience-Based Navigation: 5 Reasons to Avoid It"; "Progressive Disclosure"; "Cards: UI-Component Definition" and "Card View vs. List View"; "Carousels on Mobile Devices"; "Scrolling and Attention" (2018 study); "Flat UI Elements Attract Less Attention and Cause Uncertainty"; "Zigzag Image–Text Layouts Make Scanning Less Efficient" and its gazeplots; "Wizards: Definition and Design Recommendations"; "The User Experience of Chatbots"; "Choice Overload Impedes User Decision-Making" and "Clean the Sludge from Decision-Making Workflows." baymard.com — list view vs. grid view for spec-driven vs. visually driven products; product tables for B2B.

*Peer-reviewed:* Whitelaw, "Generous Interfaces for Digital Cultural Collections," DHQ 9.1 (2015); Chernev, Böckenholt & Goodman, "Choice overload: A conceptual review and meta-analysis," JCP 25 (2015); Valenzuela & Raghubir, "Position-based beliefs: The center-stage effect," JCP 19 (2009); Rodway, Schepman & Lambert, "Preferring the One in the Middle," Applied Cognitive Psychology 26 (2012); Murphy, Hofacker & Mizerski, "Primacy and Recency Effects on Clicking Behavior," JCMC 11 (2006); Gaudenzi, "The Living Documentary" (Goldsmiths thesis) and "Modes of Interactivity: Analysing the Webdoc."

*Museums, archives, installations (makers' accounts and press):* amrevmuseum.org (Finding Freedom interactive, About, primary sources, teacher units, Webby and MUSE releases); fearless.tech and technical.ly (Searchable Museum); artsandculture.google.com and its Play listing; about.artsandculture.google.com; ixd.prattsi.org critique (2025); google.com/earth (Voyager) and ubilabs.com; metmuseum.org/toah/about and enfilade18thc.com (2016 relaunch, CHIPS); annefrank.org colophon and 2019 awards; commarts.com (Anne Frank House, Bear 71, Histography); ideum.com/portfolio/voices-from-the-front; nationalww2museum.org (Voices from the Front page and press release); sfi.usc.edu and ilholocaustmuseum.org (Dimensions in Testimony); numiko.com "Best Museum and Gallery Websites 2026"; histography.io, smashingmagazine.com interview with Matan Stauber; museum-kiosk vendor guidance (halloffame-online.com; blogs.library.duke.edu on attract screens).

*Journalism and explorables:* revue-backoffice.com on *You Draw It*; driven-by-data.net (Aisch); peabodyawards.com and medium.com/data-science on the NYT dialect quiz; ncase.me/trust and blog.ncase.me; css-tricks.com and medium.com coverage of *The Evolution of Trust*; storybench.org and medium.com/@matthew_daniels on The Pudding's structure; maartenlambrechts.com and en.wikipedia.org on Explorable Explanations (Victor).

*Interactive documentary:* upian.com, docubase.mit.edu, opendoclab.mit.edu (Prison Valley); highrise.nfb.ca, heliosdesignlabs.com, docubase.mit.edu (Out My Window); hollowdocumentary.com, storybench.org, docubase.mit.edu (Hollow); sometimes.ca, experiments.withgoogle.com, webgpu.com showcase (Bear 71 / Jam3); honkytonk.fr, doclab.org, en.wikipedia.org (Journey to the End of Coal).

*Products and design systems:* raw.studio and uxplanet.org (Netflix welcome page — critique); userguiding.com, mobbin.com, usabilitygeek.com (Duolingo onboarding); tearthemdown.substack.com and kristenberman.substack.com (Headspace); medium.com/@smarthvasdev and design-bootcamp (Spotify onboarding); charitywater.org/someonelikeyou and medium.com/intently; appleinsider.com (Apple "Help Me Choose," June 2024); help.typeform.com, tinycommand.com, fillout.com (conversational forms — vendor and secondary); parallel.ai, franciscomoretti.com, androidauthority.com (deep-research mode UIs); blog.google, xda-developers.com, support.google.com/notebooklm (NotebookLM panels); components.publishing.service.gov.uk, designsystem.gov.scot, carbondesignsystem.com, cieden.com (button hierarchy); inclusive-components.design/cards and adrianroselli.com (block links); gameuidatabase.com, medium.com/@TheDesignMechanic, nastyrodent.com (character select).

*Pricing-page industry claims (reported, not relied on):* mida.so, designrevision.com, directpaynet.com, broworks.net, 925studios.co.

*Project documents [verified: repo]:* `cic-website/index.html`; `Build/Ministry/Features/Website-V2/CiC_Website_V2_Storyboard.md` (§1, §1.6, §1.8–1.10); `Build/Ministry/Features/Website-V2/Decision-Log.md` (entries of 2026-09-03 on the era rows and the portals); briefs 01–04 in this folder.
