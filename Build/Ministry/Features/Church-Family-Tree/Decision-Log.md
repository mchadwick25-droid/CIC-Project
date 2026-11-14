# Church Family Tree — Decision Log

Append-only, workstream-local. Dated entries: what was decided, the reasoning (the
heart as well as the mechanics), and the next action. The map's design history before
this workstream is in `../Atlas-World-Map/Decision-Log.md`; this file does not repeat it.

Scope: the Church Family Tree as Faithways Studio's second product, on its own domain,
standing alone and opening a second door into Church in Conversation.

---

## 2026-11-06 — Converged: the tree moves to its own domain and becomes the lead public product

**How it was reached.** One strategy thread, run as divergent, groan zone and convergent,
one question at a time, with options and a recommendation rendered for Mark on each. Mark
said "Converged, auto mode" on 2026-11-06. The working page used to reach it was a
claude.ai Artifact (not in the repo). This entry is the record.

### The heart of it

Mark: the tree "serves the same audience" as Church in Conversation. "The advantage is I
can make this as public as I want and it costs no API, while the conversation is much
more complex and I'm still not sure we will ever get it to the point of rigor we need. I
can move the tree forward now." The tree is the part of the mission that can go fully
public today. It must not wait on, or borrow credibility from, the conversation. Its own
rigor rests on the census, the lineage links and the narration, and that is where scrutiny
will land.

### Rulings

1. **Old addresses (Q1, option B).** Tree pages on `churchinconversation.com` redirect
   permanently, in one hop, to the same path on the new domain. The data file
   (`/data/world-census.json`) is served byte for byte at both addresses from one build, not
   redirected, because research scripts often do not follow redirects. Link anchors
   (`tree/<id>#<link-id>`) survive because browsers carry the fragment across a redirect,
   so long as the new pages keep the same anchor names.
2. **The address.** `https://www.churchfamilytree.com`. The bare `churchfamilytree.com`
   redirects permanently to `www`. Church in Conversation stays on its bare domain.
   Mark owns `churchfamilytree.com` (Namecheap, registered 2026-09-18, expires 2027-09-18,
   auto-renew on) and `churchinconversation.com`, `churchinconversation.org` and
   `faithwaysstudio.com` (Cloudflare Registrar, expiring July 2027, auto-renew checked).
3. **Three systems (Q2, option C).** The Library (texts, corpus map, census) is the shelf
   behind both products. Its public face, when it comes, is the tree: visitors reach texts
   *through* a movement or world, not through a separate library site. A searchable Library
   may come later; nothing promised now may have to move when it does.
4. **Which movements show their texts (Q2b, option C).** Once the passage reader exists, a
   movement's shelf opens when its text assignments pass their own Library check, whether or
   not a world is built. Built worlds' shelves count as checked. Each shelf says how it was
   checked. This keeps the tree from depending on the conversation.
5. **Audience (Q3).** The same audience as Church in Conversation. The tree is the lead
   public product and moves on its own schedule.
6. **The first standalone release (Q4a, option B, plus Mark's addition).** The map and all
   300 movement pages, the narration, a method page, confidence on every link at a glance, a
   data and citation page, and find-your-church search, **and** the connections and tensions
   fully built and documented.
7. **What "fully built" means (Q4a-ii, option B, then more).** For launch: every relationship
   a movement's own relations summary and description name becomes a link with a type,
   confidence grade, note and source, and a relationship that cannot be sourced comes out of
   the prose or is marked uncertain. Two independent checks: prose to links and links to
   prose. Then a full review of the whole link set. After launch, keep building toward the
   full scholarship era by era, each era a numbered, dated release.
8. **The door into a conversation (Q4b, option B).** A world's door shows on the tree only
   when Church in Conversation marks that world open to the public (one field, carried into
   the census by the existing sync). It lands on the world's own page on
   `churchinconversation.com`, which frames the conversation first. Mark, "add the worlds":
   all 11 Built & Live worlds start switched on, so today's doors stay open through the move.
9. **Brand (Q5, option A).** Sister brands, each "A Faithways Studio project", sharing one
   visual family, each with its own mark and each naming the other.
10. **Code and deployment (Q6, option B).** Two Cloudflare Workers from one repository, both
    fed by one Library. The tree gets its own live folder and Worker config and reuses the
    audio range script. The census is authored once and copied byte for byte into both sites
    by a build step, with a CI check that the copies match. The old Worker keeps the
    redirects. The census moves into the Library as its own named step later.
11. **Analytics and privacy (Q7, option B).** Cookie-free counts only: Cloudflare's traffic
    numbers and its cookie-free Web Analytics. The tree gets its own short privacy page. The
    door passes only a page reference.
12. **Order (Q8, option A).** Move the address first, with the tree as it is plus its own
    about, privacy and support pages, the redirects and the checks. Then build the standalone
    release in place. Neither the tree's launch nor Church in Conversation's waits on the other.
13. **Every tradition on the tree (Q9, option B).** One read-only sweep of the Library's own
    files (dossiers, NEEDS-RULING, staging notes) for every tradition or person with no census
    home, plus the Cyrilline duplicate. Mark rules on the list in one sitting. The agreed
    entries ship together as one numbered release before the standalone launch.
14. **Person profiles (Q9b, option A).** A movement-or-person kind field, kept separate from
    status (the same orthogonality as the founder-prophet marks). A person entry keeps the
    same record, page, links, grades and permanent ID. Tertullian (`tertullian-s-voice`,
    I.17) becomes person + A5, told within the Latin Apologists (I.43), per the 2026-09-10
    latap ruling. Who qualifies: someone the corpus treats as a party in their own right, with
    writing of their own or a recorded position, who founded no lasting movement.
15. **The living mark (Q9c, option A, with the leaf).** Three shapes: an ended movement keeps
    the dot, a living tradition gets a leaf, a person gets a portrait-style mark. Shape carries
    the meaning, never colour alone, and a legend explains all three. Before the leaf appears:
    a written definition of "living" and a check of all 169 living flags against it, with
    disputed descent carrying a confidence grade. Mark picks the drawn marks from 2 to 4 options.
16. **Mark size and tap targets (Q9d, option C).** Marks grow with zoom but never fall below
    a visible floor on screen. Each movement gets one tap area covering its mark, its name and
    the space between: at least 24 px, 44 px on touch. In a crowded era the nearer mark wins.
    Tested at phone size before it ships.
17. **Contributions (Q10, option A).** The tree's own support page saying what a gift pays for
    on the tree, the same not-a-nonprofit, not-tax-deductible line as Church in Conversation's
    word for word, two new Stripe links in the existing Faithways account, and one quiet
    "Support the tree" link in the header and footer. Banners only later, once usage is known.
18. **Review status in the data.** A field that tells AI-checked, partner-contributed and
    scholar-reviewed apart, shown on each movement page. Academic review is the biggest need
    (see the license policy, `cic-website/license.html`, and the System Hub Decision Log entry
    of 2026-11-06).

### Change orders this makes

- **Permanence promise:** `meta.identifiers` gains the domain rule, shipped as data release 2
  with the move. Logged in `../Atlas-World-Map/Decision-Log.md`, 2026-11-06.
- **Source Library reader:** it lives on the tree's domain, not on Church in Conversation's.
  Logged in `../Source-Library/Decision-Log.md`, 2026-11-06.

### Related, decided the same day elsewhere

The Faithways license policy (live at `churchinconversation.com/license`), the permission
request form and the homepage footer links: System Hub Decision Log, 2026-11-06,
mchadwick25-droid/CIC-Project#1518 and #1519.

### Next action

A fresh build thread starts from `Launch-Prompts/CFT_Build_Launch_2026-11-06.md` and runs
Phase 1 in auto mode. Mark supervises it directly (his choice, over this thread acting as a
manager, to keep context cost down). Open items are in `Open-Gaps.md`.

---

## 2026-11-06 — The move's order: a build step assembles the tree site (Mark: "a")

**Why it came up.** The build thread's step-zero reading (`Build-Plan.md`) found that a
pure `git mv` takes the tree off `churchinconversation.com` in the same merge that puts it in
the new folder, before the new domain serves it. That breaks the launch prompt's hard rule. The
map also uses files the rest of the site shares (world recordings, world data, the narration
player, the feedback script, the icon).

**Options shown.** A: a build step assembles the tree site at deploy time; nothing moves until
the domain is attached and verified, then one merge does the pure rename and the redirects.
B: commit a full second copy, then delete the originals (about 650 MB of duplicate audio kept in
the public history for good). C: rename and redirect in one merge, then attach the domain
(both addresses fail in between; ruled out).

**Decided (Mark, 2026-11-06): A.** One new script in `tools/`, `build_tree_site.mjs`, gathers the tree's
files and copies the census and the shared files into the tree Worker's build folder. A CI step
runs it and checks each copy is byte for byte identical to its source. This is ruling 10's
mechanism, applied to every shared file. No file is committed twice. Ruling 10 itself is
unchanged.

**Next action.** The rivers first (one pull request), then P1a per `Build-Plan.md`.

---

## 2026-11-07 — Places and modern countries on the map (new chunks PL1–PL3)

**Decided (Mark, 2026-11-07).** The map's names say when but not where. Each movement gains a
short place line drawn only from its own region text, and the country or countries those
places lie in today, each checked against a gazetteer (Wikidata or Pleiades) with its ID
stored. Display: names only at full-map zoom; a second line under the name once zoomed in;
the full line in the panel and on the tree page, with "today" stated. One legend line says
places are given with today's countries. Disputed or politically sensitive borders go to Mark
as one list for one ruling; none is decided case by case.

**Where it goes.** After the rivers and before the rename (P1c). P1a merged first but moved
nothing, so the map file is still in place. One pull request for the data and the display,
because the census is public the moment it merges.

**Change order: release numbering.** The place fields ship as data release 2. The domain rule
planned for release 2 with P1c becomes release 3. Releases stay in the order they ship; folding
both into one would hold the places back until the domain is attached.

**Sources reachable.** From the build sandbox on 2026-11-07, Pleiades answered, and so did
Wikidata's query service. Wikidata's entity API refused one unnamed request (HTTP 429); lookups
go through the query service with a named client.

**Next action.** Mark sees the revised chunk list once, then PL1 starts.

**Added the same day (Mark: "do the same for the stories that are on the main page").** The 62
gap stories, the map's book icons, get the same place line and modern countries, from their own
`region` text and the same gazetteers, and their disputed borders join the same one-sitting list.
Their only copy is the data embedded in the map file, not the census, so their fields change no
census release. They have no name on the map, so the place line goes in the hover tip and the
panel, not beside the icon.

**Ruled the same day (Mark: "use the familiar names").** Where an entry's region text gives two
names for one place, the place line shows the one a general reader knows. Applied to seven
labels (Lyon, Whitby, Bratislava, Beijing, Sivas, Massawa, Genadendal); the record is
`Build/Ministry/Operations/Audits/2026-11-07_place-labels/README.md`.

**Ruled the same day (Mark: "make sure the spacing still works … you can adjust their place a
little to make space, they don't have to be exactly in the year on the map or in the river, just
make it easy to navigate").** The map may draw a movement's dot and name a little away from its
exact year and its river's center line, so names, place lines and dots do not overlap and each
stays easy to tap. Only where things are drawn moves: dates, links and every panel keep the real
values, and links attach to the moved dots. Built into PL3, with the overlap measured before and
after.

**Ruled the same day (Mark: "A for both").**
1. *Disputed places* name the place in plain geographic words and no state: "Bethlehem, West
   Bank", "Cyprus (the island)", "Palestine (the historical region)"; Jerusalem, Gaza, the
   Judean Desert and China show as the place alone. The words are stored in the census as
   `placeQualifiers`, so the data says what the map says. Rejected: naming every state Wikidata
   lists (it can read as taking a side), and the place alone everywhere (says less).
2. *Historical regions* (27 places, 45 entries, such as Persia, Roman Africa, Prussia and
   historical Armenia) show the place alone. Their present-day countries come in a later,
   checked pass as their own release. Rejected: doing that pass before this ships, and naming
   only the country of a region's core (it understates regions that spanned several).

The place fields ship as data release 2, dated 2026-11-07.

---

## 2026-11-07 — The map's place line leaves out places the name already says

**Decided (Mark: "many of the names have the place in them, if they do maybe we dont need it
duplicated").** On the map, a place already in the movement's shown name drops out of its second
line; its country stays. "Alexandria" shows "Egypt", "Third-Century Rome" shows "Italy", "Syriac
Edessa" shows "Nisibis, Turkey". Where nothing is left to add, there is no second line. The
panel and the tree page keep the full line, since their headings use the long name. 49 of 292
names contained a place.

**Also decided the same day (Mark, of the book icons: "not all of them have names").** Each of
the 62 gap stories shows its title beside its icon from the second zoom step (0.7), the same
step as place lines. The titles join the no-overlap layout and hide with the stories switch.
Measured at reading zoom: no overlaps, 223 place lines shown.

---

## 2026-11-07 — P1c built: the tree moves to its own folder; old addresses redirect

Mark: "go ahead with P1c full auto", after `www.churchfamilytree.com` was attached and checked.

- **The move.** A pure rename (its own commit, 1,163 files, all 100 % renames) puts the map, the
  movement pages and their recordings in `cft-website/`.
- **The redirects.** On `churchinconversation.com` the Worker answers every old tree address,
  the three old map addresses and the moved recordings with a permanent, one-hop redirect to the
  same path on the tree's domain, query kept. A movement listed as retired with `redirectTo`
  goes straight to its new page in the same hop. The census is served, never redirected. The
  switch is a single setting in `wrangler.jsonc` (`TREE_ORIGIN`); the tree's own Worker has none.
- **Data release 3.** `meta.identifiers` gains the domain rule; `meta.license` names the license
  policy. Release 2 was the place labels.
- **Checks.** `tools/validate-census.mjs --tree` fails any movement without a page, any retired
  redirect without a page to land on, and any link whose anchor is missing from either of its
  two pages. `tools/check_tree_domains.mjs` checks the live addresses after a deploy.
- **Scripts no longer go stale.** `assets/` revalidates on every visit on both sites (Open-Gaps 16).
- **Feedback on the map.** The page-feedback bar recognises the map on the tree's home page and
  keeps its old page name, so feedback before and after the move stays together.

---

## 2026-11-07 — The tree's own header and a switch bar in place of the legend

**Decided (Mark: "this program is church family tree so it should be in the upper left corner …
then to the right we have a button to church in conversation. we can replace the three buttons
below with on off switches/legend"; then "Grouped chips").** On `www.churchfamilytree.com`:
- The header leads with "Church Family Tree"; one "Church in Conversation" button sits to the
  right.
- Church in Conversation's three feature buttons give way to one row of chips: Rivers, Links and
  Evidence each open their own switches; Stories is one on/off switch; Key holds the status
  colors and the notes on width, threads, lean and places. One panel opens at a time; Escape
  or a click elsewhere closes it. The old legend box at the bottom left goes.
- The switches work as before and keep each visitor's choices.
- The intro line now points to the switches under the title (Reading Ease 72).

Rejected: every switch in one long scrolling strip (hard to scan on a phone), and one button that
opens the whole legend (hides more than today's legend does).

**Refined the same day (Mark: connections should be one chip with an explanation, off by default;
rivers and stories on by default).** The bar is Rivers, Connections, Stories and Key. Connections
holds a short explanation, an "All connections" switch, the four kinds of link and the four
levels of certainty. A first visit shows rivers, names and stories with no lines; a visitor turns
on all connections or only the kinds they want, and the choice is kept. Checked: 0 of 86 lines on
a first visit, 86 with all on, 34 with only "argued against, broke with", kept after a reload.
The intro now says where to find them (Reading Ease 70).

**Also the same day (Mark: "if someone clicks off a river, the worlds connected to that river
should also hide").** A river's switch now also hides the story icons on that river and the
"continues as" lines that touch it, as it already hid its dots, names, place lines, portraits
and connections. Checked: Africa off hides its 3 stories and leaves nothing on that river
showing; All rivers off clears the map.


## 2026-11-07 — P1d built: door switch and the tree's own pages

Built to the plan (P1d in `Build-Plan.md`):
- Each world record has a `public_open` switch. It is on for the 11 Built & Live worlds. The
  census sync carries it into the census and the map as `publicOpen`.
- An open world's panel and tree page offer "Meet <Representative> on Church in Conversation",
  linked to that world's page there. With no world open, built worlds show only the quiet line
  "Church in Conversation, from the same team." A test generates the pages both ways.
- The tree pages share one header and footer with the new about, privacy and support pages.
  Their text lives in `Build/tools/tree_site_pages.json`. Reading Ease: about 61, privacy 85,
  support 66. The one paragraph under 60 is the not-a-nonprofit sentence (30). It must match
  `cic-website/support.html` word for word, and a test checks that it does.
- The support page shows its give buttons only once both Stripe links are in the content file.
  Until Mark makes them, the page explains support without buttons.

**Trimmed the same day (Mark: "on the world card, we dont need the four boxes … on the page we
dont need the blue box … also the not yet built section should be removed").**
- Tree pages lose the four fact boxes (era, dates, region, status) and the status block. The
  line above the title already gives era, dates and region. A visitor can tell from the door
  whether a Representative exists.
- The present-day country line, the only fact the boxes added, now sits under that line. It
  shows only when it names a country.
- The map loses its intro box. Training and About buttons will replace it later, as their own
  piece of work.

## 2026-11-07 — P1c and P1d merged and live; P1e built

**Merged (#1531).** Mark chose to carry the header, switches and P1d in the same pull request as
P1c (option A), so one new build would pick up the corrected Cloudflare preview settings. The
tree's preview builds kept running with settings other than the ones saved under Previews Base,
so Mark turned tree previews off and approved merging with that one check red. Every GitHub check
passed. After the deploy, `tools/check_tree_domains.mjs` found 0 problems across 300 movements,
and the census was identical at both addresses.

**P1e.** Church in Conversation's tree links now point at `https://www.churchfamilytree.com`:
the "Church Family Tree" button on 17 site pages and 12 tradition pages, the homepage showcase
and fallback lines, and the 12 "See it on the Church Family Tree" links. All 13 distinct targets
answer 200 live. The feedback bar's page name `atlas-v3` stays, so feedback keeps one name. The
note for the outside researcher was drafted for Mark to send (Reading Ease 66).

## 2026-11-07 — P1e merged; P1a2 built

**P1e merged (#1532).** Live: Church in Conversation's homepage and tradition pages link straight
to `www.churchfamilytree.com`.

**P1a2.** The feedback API reads a comma-separated list of site origins, so the feedback bar works
from both domains:
- `CIC_API_SITE_ORIGIN` (falling back to `CIC_DEEPER_SITE_ORIGIN`) becomes a list.
- The Go Deeper claim routes read their own variable the same way. Its value stays the one Church
  in Conversation origin, because the app build's `VITE_DEEPER_SITE_ORIGIN` must match it and
  the tree has no Go Deeper.
- `render.yaml` declares `CIC_API_SITE_ORIGIN` on the production service with both origins.
- Tests cover each allowed origin, refused look-alikes, and the list parsing.

Before promotion, the live API answers Church in Conversation's origin and gives the tree's
origin no permission header (checked 2026-11-07). Nothing changes until Mark promotes `main` to
`live` and the variable reaches Render.

## 2026-11-07 — Phase 2 links: Opus drafts, a second Opus 5.5 reviews

**Decided (Mark: "this time we will do opus drafts and then a second opus 5.5 review. we get
higher quality that way and the new opus 5.5 is not as expensive as the old and better").**
For the per-era link sessions (P2-L1 to P2-L10), Opus drafts the links and prose changes. A
separate Opus 5.5 agent reviews them, briefed with the data and sources, not the drafters'
conclusions. Haiku still does the inventory and the mechanical work. The three-round review
cap is unchanged. The launch prompt carries the change.

Scope: this link work. The general split in `CLAUDE.md` (Sonnet drafts, Opus reviews) is not
changed by this entry.

## 2026-11-07 — The Philocalia's compilers

**Decided (Mark: "go with the reliable credits and forget the cappadocian record on this", and
"make sure its an accurate coming from the sources").** The tree credits Basil of Caesarea and
Gregory of Nazianzus with compiling the Philocalia of Origen, without "tradition says". The
credit is stated as the editors' credit, because that is where it comes from: the editors of the
vendored editions of both men's letters say it (Browne and Swallow, NPNF 7, 1894: "From his
exegetical writings they compiled a book of Extracts"; Blomfield Jackson, NPNF 8, 1895: "in
conjunction with his friend Gregory, Basil compiled the collection"). Gregory's own Letter 115
only sends the book, and no ancient text in the Library names its compilers. The Cappadocian
records, which hold the compilers contested, are left as they are; this is a ruling for the
tree's text, not a records change. Applied in data release 5 to `alexandria-catechetical`'s
legacy and the `alexandria-catechetical--cappadocian-nicene-pastoral-monastic-tradition` link
note.

## 2026-11-08 — Major links: a switch, and what makes a link major

**Decided (Mark: "we need a way to prioritize and scale"; "prioritize the top few that click on
and off (things with historical implementations, not just a squabble)"; "still off, but yes a
major links"; test M2; "converged, auto mode").** The map still opens with no lines. Connections
gains a "Major links" switch, off by default, that draws only major links. Picking a movement
still lights all of its own links, and every link stays on its card and tree page.

A link is major when:
- its type is "gave rise to", "continued as" or "broke with"; or
- its type is "influenced", "argued against" or "in contact with", and one of its own listed
  sources shows a lasting outcome beyond the quarrel: a council, canon or law condemning a
  group; a split into a separate church; a teaching, text or practice taken up by the other
  side; or a rule or practice changed. Such a link carries `outcome`, one plain sentence naming
  that result from its own sources.

**Options shown** (artifact "Taming the tree's lines"): A lines on demand; B lineage spine plus
lines on demand; C key links per era; D detail by zoom. Then, for the test: M1 type only; M2
type plus a sourced outcome; M3 a ranked top ten per era. Recommended B, then M2. Mark took a
switch (from C) with the M2 test.

**Why M2.** It catches consequential arguments and influence (a council condemning a group, the
Reformers reading Augustine), while every major mark stays tied to a source the review checks.
A ranked top ten would have made comparative claims no source can carry.

**Scope.** Eras 6 to 10 mark outcomes while drafting (launch prompt step 4b). Eras 1 to 5 get
one pass (P2-ML), with the map switch, after eras 4 and 5 merge.

**Change order (2026-11-08, Mark: "Drop 'taken up'").** After review, the M2 test made 151 of
the 302 links in eras 1-5 major (74 by type, 77 by outcome), about 30 per era, far more than
"the top few". The test is narrowed. A link of the three judged types is major only when its own
sources show an institutional act: a council, canon, synod or law condemning, deposing or
excluding a group or its teaching; a split into a separate church or body; or a rule, practice
or settlement changed by an authority. A teaching, text or practice merely taken up by the
other side no longer counts; those links stay on the cards, minor. Options shown with it: keep
M2 (151 lines), type only (74), and two levels of line weight.

**Cap ruling (2026-11-08, Mark: "Use the reviewer's fix").** The major-links pass reached its
three-round review cap with one substantial finding open (round 3, R3-01): the Carmelite 1247
outcome sentence had the friars ask for confirmation of a rule already corrected, where the
source has them ask for the correction itself. The reviewer's own replacement sentence is applied
word for word; no fourth round. File:
`Build/Ministry/Operations/Audits/2026-11-08_major-links/Opus_Review_Round3_TargetedRecheck.json`.

## 2026-11-08 — The link work covers eras 1 to 9

**Decided (Mark: "we have not build out era 10 traditions, so lets consider the tree to be eras 1 - 9 completed").**
Phase 2's per-era link passes cover eras 1 to 9. Era 10's traditions are not yet built, so
P2-L10 waits until they are. Era 10's movements stay on the map as they are. P2-L11, the
whole-set review, covers the links of eras 1 to 9.

## 2026-11-08 — Major links: a church body adopting another's text by vote is minor

**Decided (Mark: "Adoption by vote is minor; keep the four outcomes dropped").** Under the
"Drop 'taken up'" change order, a council, synod or assembly adopting another side's confession,
catechism, worship order or set text by its own vote is a text taken up, not a rule changed by an
authority. Such a link stays minor and carries no `outcome`.

**Applied (P2-L7, data release 12).** The four era-7 outcomes stay dropped (Uppsala 1593, the
Scottish General Assembly 1562, the Paris synod 1559, Emden 1571). The outcome P2-ML had put on
`hieronymian-ascetic-literary--the-tridentine-church` (Trent's Vulgate decree) is removed, so all
six links of the class are treated alike. Later link passes and P2-L11 apply the same reading.

## 2026-11-08 — An Armenian Apostolic movement for era 8

**Decided (Mark: "add an era-8 Armenian Apostolic movement").** The era 8 links pass escalated that
the Armenian lane had no Apostolic Church between 1650 and 1815. Options shown: add an era-8
Apostolic movement (recommended), widen the Mekhitarist movement, or accept the lane as it stood.
Mark took the first. Built as P2-L8a; the census change order is recorded in the map's own
Decision-Log (2026-11-08, "Era 8 change order: census 300→301").

## 2026-11-08 — Rulings on the era 6 open questions

Mark ruled on the seven questions the era 6 links pass logged in Open-Gaps (2026-11-08), one at
a time, each shown with three options and a recommendation. He took the recommendation each time
("a").

1. **The Church of the East's "Hakkari" name.** Rename the display name to "The Church of the
   East — Timur's Catastrophe and the Northern Remnant", with the place label and the era 7
   schism summary to match. The ID and page address stay. Why: the patriarchs of the late
   fifteenth century sat at Gazarta and Mosul on the upper Tigris; only the survivors were in the
   Hakkari mountains. "Northern" covers both; "Hakkari" outran the sources. Shown with: keep the
   name; "the Mountain Remnant".
2. **An authority's acts on another body's own order, and church jurisdiction.** Drawn as
   "in contact with", with an `outcome` naming the act where the link's own sources show it. The
   jurisdiction links now drawn as "influenced" (a patriarch appointing another church's head
   bishop) are re-typed. Leo X's division of the Franciscan order (1517) is drawn this way. Why:
   "influenced" claims ideas passed where the sources show an appointment; the outcome field
   already counts a rule or settlement changed by an authority. Shown with: a seventh type, "had
   authority over"; leave as is. Settles "No link type for church jurisdiction" (2026-11-08) too.
3. **The councils of Constance and Basel.** They stay inside the papal church's movement
   (`latin-papal-church-avignon-to-lateran-v`), whose own text tells them as part of its story;
   every note names the council that acted. Shown with: a movement for the councils; renaming the
   movement "The Latin Church".
4. **The Carthusians after 1300.** A later Carthusian movement goes on the list for the gap
   sweep and the agreed-entries release (P2-G1, P2-G3), split by era as the Waldensians were.
   Until then the era 6 text states the copying of The Cloud and the Scale with no link. Shown
   with: stretching `carthusian-life` past 1300; leaving it.
5. **The inquisition-record sects and the Free Spirit.** Split by evidence. The era 6 movement
   keeps the Adamites and other groups known only from hostile records, and points to the Free
   Spirit instead of retelling it. The 1367 case moves onto the existing link from the papal
   church to the Free Spirit; the link it came from is retired. Why: the Free Spirit was mostly
   a charge, the Adamites a real band; the 1367 suspect belongs to the Free Spirit story. Shown
   with: merging the two movements; leaving both.
6. **Well-known facts with no vendored source.** A standard, undisputed fact that is not a
   relationship may stand without a source in the Library, with its wanted text listed. The
   guard: a fact that charges someone with violence or persecution, gives a number, or is
   disputed needs a source, or is stated as what is reported. Settles "Well-known facts with no
   vendored source" (2026-11-07). Shown with: every fact needs a source; all stand until P2-L11.
7. **Page recordings that read old text.** Each recording stores a fingerprint of the text it
   was made from; a page whose text has changed hides its Listen button until it is re-voiced.
   One paid re-voicing batch runs after the era 9 links pass, sample first and approved by ear,
   settings passed and printed. Why: no page plays corrected errors, and re-voicing is paid for
   once. Shown with: re-voice eras 5 and 6 now; leave the recordings until the end.

**Cap ruling (2026-11-08, Mark: "a").** The era 6 rulings work reached its three-round review cap
with one substantial finding open (round 3, R3-01): era 7's rewrite of the 1552 schism's summary,
merged during review, said the story "grows out of the Church of the East of Timur's age and the
Hakkari mountains", the reading ruling 1 set aside. The reviewer's own replacement sentence ("The
story grows out of the Church of the East after Timur.") is applied word for word; no fourth round.
File: `Build/Ministry/Operations/Audits/2026-11-08_era-6-rulings/Opus_Review_Round3_TargetedRecheck.json`.

## 2026-11-08 — Tree pages re-voiced after era 9 (ruling 7 carried out)

**Done (Mark: "run the sample, same voice and settings", then "run the rest").** Every tree
recording whose fingerprint no longer matched its page's text was re-voiced, as ruling 7 of the
era 6 rulings set out.

**Settings, as printed by every request.** Voice `onwK4e9ZLuTAKqWW03F9` (Daniel), model
`eleven_multilingual_v2`, output `mp3_44100_64`, stability 0.95, similarity 0.68, style 0, speaker
boost on: the settings of the last tree run (front-end decision log, 2026-09-29, "Daniel
re-narration redone with the right voice"). Voice and model were passed on the command; none was
read from the environment.

**Sample.** Three pages (the Church of the East after Timur, the Franciscan order of era 6,
Lollardy), 3,057 characters, 1,345 credits. Mark approved by ear.

**Run.** 152 pages, 151,529 characters, under the approved cap of 152,000; 66,671 credits by the
API's `character-cost` headers. All 152 request lines carry the same voice, model and settings; no
failures. Sizes sit at 563-650 bytes per character across the 155 new files, so none is truncated.
Every manifest entry for them records the voice, model, format and text fingerprint.

**Result.** No tree recording is stale. 280 of 301 tree pages show a Listen player; the rest are
built worlds, which play their own story, or pages with no recording.

**Limits.** The voice cannot be confirmed from ElevenLabs' side with this key; it rests on the
voice id in each request, the sizes, and Mark's ear on the sample.

## 2026-11-08 — Whole-set rulings

**Decided (Mark, one question at a time, after the whole-set review of eras 1 to 9, P2-L11).**
Each was shown with options and a recommendation as an artifact.

1. **One old account (Mark: "c for ruling 1").** A link whose only support is one 19th- or
   early-20th-century account that states the tie is Dominant Modern Reconstruction only where a
   modern study already cited in the repo supports the same reading; otherwise it is
   Inferential-Thin. Options shown: Thin for all (recommended), Dominant for all, this one.
2. **What `verified-direct` means (Mark: "a").** The quoted lines were read and match. Whether
   they show the relationship is what the grade says. Options shown: this (recommended); the
   Drafting Brief's old meaning, "the quote shows the relationship"; a fifth status.
3. **A secondary work held in the Library (Mark: "a").** It may carry `file`, `lines` and a
   verbatim `quote`, all three together, and the validator checks the quote like a primary's.
   Options shown: this (recommended); title only, as the Drafting Brief had it; leave the mix.
4. **Deposed by a ruler (Mark: "b").** Under the narrowed major-links test, a church head or
   prelate deposed by any authority, church or state, counts as an institutional act, not only by
   a council, canon, synod or law. Options shown: council or law only (recommended), this, keep
   the split between eras 3 and 8.
5. **The Bogomil-to-Cathar link (Mark: "a").** Keep one: Balkan Bogomilism to the Cathars.
   `bogomils--cathars-albigensians` is retired, pointing to it. The wider overlap of the two
   Bogomil entries stays open (Open-Gaps, "The Bogomil entries overlap", 2026-11-08).

**Change order.** Rulings 1 to 3 amend the Drafting Brief
(`Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`) and
`tools/validate-census.mjs`. Ruling 4 widens the 2026-11-08 major-links test by one act.
Applied as P2-L11b, data release 19.

## 2026-11-08 — Era 10 becomes history, 1906–2010 (change order)

**Decided (Mark: "lets make era 10 historical and go from 1905 to 2000"; "Living as of 2000";
"we are using the standard we used to identify and source the 300 worlds in the family tree";
"converged, auto mode").** Later in the same sitting Mark moved the end to 2010, relayed to this
thread from the era 1 thread: era 10 becomes a century of global Christianity, from Azusa Street
(1906) and Edinburgh 1910 to the 2010 centenary meetings, Edinburgh 2010 and Lausanne's Cape Town
congress.

1. Era 10 runs 1906 to about 2010, written "c. 2010" in the era band and dates. Mark: "yes era 10
   ends in 2010 (about) living traditions are alive today. the other eras do not need the 2010
   perspective, its there era and today (2026)" (relayed). The boundary with era 9 stays at 1906
   (Azusa Street), so era 9's frozen
   end does not move.
2. Era 10's history runs to about 2010, and nothing after it is mapped. Eras 1 to 9 are not tied to
   2010: each covers its own span. In every era the living-tradition marker means alive today
   (2026), the tree's one statement about the present. Mark set "as of 2000", then "as
   of 2010", then corrected it in the same sitting (relayed): "no i think alive today means now, not
   16 years ago".
3. Era 10 is identified and sourced by the same Step 0 standard as eras 1 to 9. The per-world
   construction standard does not apply.
4. The Living-Era Protocol Addendum V1.0 governs the living marker, and only it: dated own-voice
   evidence (R2), the Contemporary-Documented / Contemporary-Reported grades (R3) and present-tense
   humility (R4). No other present-tense claim enters an entry.

The survey also widens to Christian movements and trends outside formal church bodies (Bible
translation, campus ministries, church planting, world missions and the like). The unit is the
movement, never the organization; how such entries are marked is a gate question. Mark tightened it: "it needs to be a defined movement, not just a trend". A candidate needs a
recognizable beginning, identifiable carriers, a name its participants or contemporaries used, and
recognition as a movement in a cited source; a diffuse trend becomes a named line or is left out.

After 2010 (Mark, "yes, pass that to era 10", relayed): the tree says nothing past 2010 and says
so plainly. The living mark, as finally ruled, means alive today (rule 2). A
later decade joins once it is about fifteen years in the past (2010–2020 around 2035), under the
same standard, as a numbered data release. A "since 2010" note and a rolling cut-off were
declined. The reader-facing line, for the method page and the era 10 band once the gate rules:
"The tree's history runs to 2010. Movements since then will be added as they become history."

Mark's own wording of the rule (relayed from the era 1 thread): "anything after is a living
tradition or new, but not mapped. 2010 back is historical and treated that way except with a
living tradition marker".

**Change order.** This amends the era 10 freeze of 2026-08-14 (Atlas World Map Decision-Log, "ERA
10 FROZEN by Mark", and `CiC_Step0_Era10_V1_0.md`): the span, the dated-reading clause on living
rows, the "present" end dates, and the retention of the most recent rows. The full list is in the
Atlas World Map Decision-Log entry of the same date ("Change order: era 10 becomes history").

It also amends this log's entry "The link work covers eras 1 to 9" (2026-11-08) in one respect:
era 10's traditions are now re-surveyed as history first, and P2-L10 waits for Mark's gate ruling
on that re-survey. The census is unchanged until then.

## 2026-11-08 — Dominant links on two or three old accounts

**Decided (Mark: "add the modern studies for the eight links", then "a").** Eight links graded
Dominant Modern Reconstruction rested on two or three accounts written before 1930, which ruling 1
of "Whole-set rulings" (one account) did not reach. Two have a modern study already cited in the
repo for the same events, and it is added: Skinner (2009) on the 1794 Ruthenian reunion campaign,
Frazee (1983) on the Avedik affair. The other six have none anywhere in the repo, so they become
Inferential-Thin and their wanted studies are listed. Options shown: Thin and list the wanted
studies (recommended); cite modern studies from outside the repo, unread; leave them Dominant.
Applied as P2-L11c, data release 20. Review added one more link of the same kind (Coptic Egypt to Makuria, on Griffith 1913 alone), also made Inferential-Thin.

## 2026-11-08 — The whole-set review is approved to proceed

**Decided (Mark: "approve the full review").** P2-L11, the whole-set review of the links for eras
1 to 9, is approved to proceed, together with its two follow-ups: the five whole-set rulings
(P2-L11b, data release 19) and the Dominant links on old accounts (P2-L11c, data release 20). This
is the work's own approval, not a closure: nothing closes before Phase Five boundary testing and
the full-system review. Era 10's links wait for Mark's era 10 gate (P2-E10, then P2-L10).
## 2026-11-08 — Evidence for recent movements (change order)

**Decided (Mark: "yes as the writings are current or recent history so its more reliable than 2000
years ago yes on 3"; "we have to be able to tell an accurate story, but use different criteria").**
A movement after about 1930 shows the four marks of a defined movement by two kinds of evidence
together: its own dated founding texts (beginning, carriers, name) and a standard scholarly
reference work that recognizes it as a movement. Neither needs to be vendored in the Library. Each
is cited in full with its verification state, and [S] never counts as verified. This amends the era
10 re-run brief, which allowed only vendored texts and works the repo already cited. Full entry:
Atlas World Map Decision-Log, same date.

## 2026-11-08 — The two Bogomil entries are split by date

**Decided (Mark: "a").** `bogomils` (era 4) covers the movement from about 950 to 1054: its
Bulgarian founder, Cosmas's sermon, the spread into Byzantium. It hands its later story to
`balkan-bogomil-continuation` (era 5, 1054-1300): Basil's burning, Zigabenos, Tarnovo 1211 and
the Cathar claim. Its date label becomes "c. 950–1054", and its summary, description, why, legacy
and voices are trimmed to match. No ID, page or link changes. Options shown: split by date
(recommended), merge into one entry for 950-1300, leave both. Settles "The Bogomil entries
overlap" (Open-Gaps, 2026-11-08). Data release 21. The page's recording no longer matches its
description, so its Listen button is hidden until the next re-voicing batch, which needs its own
sample approval.
## 2026-11-08 — Era 10 gate: every recommendation taken

**Decided (Mark: "take every recommendation").** All 79 gate questions are ruled by their stated
recommendations. The one exception is G-15: IX.50 (the Christian Right) has no recommendation and
stays held for Mark's direct answer. G-49 was withdrawn. Full entry, with what the ruling does:
Atlas World Map Decision-Log, "ERA 10 GATE", same date. The work runs as P2-E10a (the census pass
on the existing rows), P2-E10b (new rows and named lines) and P2-E10c (the `kind` field and its
drawing, the method-page line, the era band). Then P2-L10 and P2-V.

## 2026-11-09 — The gap sweep ruled (P2-G1)

**How it was reached.** Mark ruled on the P2-G1 sweep
(`Build/Ministry/Operations/Audits/2026-11-08_tree-gap-sweep/`) in chat, one question at a time, each
with options and a recommendation, on 8 and 9 November. After item 16 he asked for principles
instead of one answer per item ("is there a principle we can use"), and adopted six drawn from his
own rulings ("a"). The working page was the artifact "Tree Gap Sweep Ruling". The sitting record,
with each item's outcome and the principle that settled it, is `Rulings_2026-11-09.md` and
`Outcomes.json` in the audit folder.

### Rulings on the candidates

1. **The Cyrilline duplicate (D).** `cyrilline-miaphysite-egyptian-tradition` (I.14) is retired
   into `cyrilline-miaphysite-egyptian-christianity` (II.1) with a redirect. II.1 becomes the
   entry for the church of Alexandria, running across the era 2/3 line (Mark: "the era lines are
   for reference not definition"). Its claim to the inheritance of Athanasius and Cyril is graded
   Contested, since the Chalcedonian line claims it too. Shown with: retire only; re-scope I.14
   (breaks the permanence promise); retire and add a separate entry to 451 (recommended).
2. **Where II.1 starts (A).** With Athanasius, 328. That settles "No entry for the church of
   Alexandria, 4th-5th century" (Open-Gaps, 2026-11-07) and gives Aksum's conversion-era entry
   its parent. The Library shelf of I.14 (Cyril, Ephesus 431 and 449) moves to II.1.
3. **New movements (each A, as recommended):** the Melitian schism; the Luciferians; the New
   France Jesuit mission (end date set by the vendored Relations, the converts heard through the
   missionaries, as its sourcing note will say); the Swedish Lutherans of New Sweden (flagged
   thin: one source, Acrelius 1759); English Unitarianism (Biddle, Nye and Toulmin named inside it);
   the Melkite Greek Catholic Church after 1815; the Hutterites (span from their own chronicles).
4. **Mennonites and Amish after 1650 (A, a new successor entry).** Recommended was extending the
   Anabaptist entry. Its shelf starts as later printings of the older texts, and a source pass is
   wanted. This sets the pattern for item 9 and principle 3.
5. **People.** Augustine, told within `latin-pastoral-congregational-christianity`, whose census
   text is corrected to match its own Doc_01 (it takes in the controversies); the lpc world is
   not touched. Irenaeus, within `post-apostolic-house-church`. Nestorius, within the Antiochene
   exegetes, with a custody link to the Church of the East. Simeon of Beth Arsham, within the
   Syriac Orthodox church. William Tyndale, within the English Reformation, as its forerunner.
   Jovinian and Peter the Iberian, within no tradition. John Chrysostom (new), within
   `antiochene-exegetical-christianity-chrysostom-ce`, which stays a movement.
6. **Windesheim (C).** Stays inside the Devotio Moderna entry, whose text gains a line that its
   houses kept their own chronicle; Busch's chronicle joins that shelf.
7. **The Nonjurors (B).** Stay inside the Restoration and Georgian Church of England entry.

### People on the map (change order to rulings 14 and 15)

- **Who gets a person mark.** Anyone who passes ruling 14's test; or has 10 or more works of
  their own on a tradition's shelf, founders included (about 23 people); or is named repeatedly in
  the own-voice texts of later traditions (in at least two later traditions, about five mentions
  each), counted by a script with an alias list. Mark sees the list before it ships.
- **Every tradition shows its named people.** Drawn from its `voices`: named individuals whose
  words the Library holds or the entry quotes from a source. None is invented. A tradition with no
  named individual shows none, and its card says why.
- **Where they sit.** One switch, Traditions | People, turns the same map from one layer to the
  other; it opens on Traditions. Each tradition's people sit in a horizontal row at its place,
  ordered by date, up to three on the map, all of them on the card. A person told within no
  tradition sits in the gap, placed as gap stories without a world are.
- **Doors.** A person told within a world carries that world's door, on the person's page and the
  tradition's, shown when the world is open.
- **Links.** A link stays one record on the tradition, with one ID, grade and sources, and names
  the person it concerns where its own sources do. The Traditions view draws it from the
  tradition, the People view from the person.
- **Pictures.** A mark shows a real likeness only where one was made in the person's lifetime or
  near it, public domain, credited and date-checked. Otherwise it shows a drawn silhouette of the
  period and tradition family, in male and female forms, labeled "silhouette, not a likeness". A
  person's page may also show later traditional depictions, captioned with date and artist. No
  paid image generation.

### Principles for the rest (Mark: "a")

1. Evidence sets an entry's span, not the era lines.
2. A distinct body with its own period and its own voice in the Library gets its own entry.
3. A living tradition past its entry's end gets a successor entry, not a stretched one. Where the
   Library has no voice for the later period, the gap is held as a named gap, shown by the dashed
   thread, and its wanted texts go to the source-research thread; it is built when they arrive.
4. A person gets a mark by the tests above, told within the tradition the Library shelves them in.
5. A branch, order, wing or colonial arm an existing entry already tells stays inside it, unless it
   passes principle 2 on its own evidence.
6. A thin lead (a category, a stale note, no Library evidence) is left out.

Held as named gaps by principle 3: the medieval English church after 1066, the medieval
Scandinavian church after 1104, the Melkites from 1009 to 1724, the Syriac Orthodox church after
1300, the Scottish church after 1650, the Swedenborgian successor after 1815, and the Old Believers
after 1815. Stay inside by principle 5: the Second Bulgarian Empire's church and the councils.
Ambrose, Jerome and Gregory the Great get person marks inside their entries, which stay movements.

### The link passes' open questions (principle M, Mark: "a")

**M. Before launch, the method holds still.** The six link types and five grades stay; conventions
go on the method page; sourced text stands with its wanted texts queued; one entry's fixes go to
its owner or P2-L11; paid runs wait for their text to settle. Under it: each emperor's act stays on
its own sources; the first Persian entry ends at the synod of 424 (principle 1); Ambrose's Milan
stays beside the imperial church; Caucasian Albania's span follows the vendored histories, and the
Bagratid "absorbs after 705" goes; the two "continues as" fields that only influenced are cleared;
the Alcuin link is drawn and the other two wait; long-gap links to modern churches are not drawn.

**Earlier rulings stand.** Several of these questions were ruled on 2026-11-08 in "Rulings on the
era 6 open questions", "Whole-set rulings", "Dominant links on two or three old accounts" and "The
two Bogomil entries are split by date", and are applied in data releases 19 to 21. The sitting's
table did not show those rulings. Where it differs, the earlier ruling stands and the sitting's
line is superseded: the Bogomil split at 1054, the narrowed grade for links on old accounts, the
"Northern Remnant" name, the Free Spirit split, and a later Carthusian movement made in P2-G3. On
well-known facts, jurisdiction and page recordings the two agree.

### What this sends where

- **P2-G2 (schema)** carries the person kind beside the era 10 `kind` field (`cross-church
  movement`), the retired-ID redirect for I.14, the `concerns` field on links, and the people row.
- **P2-G3 (agreed entries)** builds the new entries and person entries, runs the person count and
  the later-worlds count, and shows Mark the people list before it ships.
- **New chunks:** the People layer on the map (switch, rows, gap placement, links by view); the
  silhouette set, drawn with P2-K1; and the likeness check (rights and date per image).
- **The source-research thread** gets the wanted texts for the held gaps.
## 2026-11-09 — Era 10 follow-up rulings

**Decided (Mark: "take every recommendation").**
- IX.50, the Christian Right, enters as a thin Tier 3 cross-church movement, 1979 to c. 2010
  (G-15 (i)).
- IX.53, faith missions, stays held until its statement of faith is found.
- IX.31's old page shows a "retired" notice. This follows G-8(a): the row is retired with no
  redirect.
- Re-voicing starts with a small paid sample that Mark approves by ear.

Full entry: Atlas World Map Decision-Log, same date.

## 2026-11-09 — Cross-church movements get their own column (P2-E10d)

**Decided (Mark, relayed from the era 1 thread).** Looking at the live map, Mark said the striped
movement band "looks like it encompasses the entire river and they didn't". His choice: "A with a
toggle on and off, starting off like connections".

1. **The striped bands go.** Cross-church movements (census rows with `kind: "cross-church
   movement"`) no longer draw over any river.
2. **Their own column.** Each era band gets a narrow movements column at its edge. A movement is a
   thin line there that runs only for its own dates, start to end, with its name at its start.
3. **Ties on pick.** Hovering over or picking a movement draws faint ties to the churches its own
   census links connect it to, from the existing edges data. The ties stay while its card is open,
   the way links light up now. Nothing new is claimed: a tie appears only where a sourced link
   exists, and a movement with no links shows none.
4. **A Movements switch, off by default, like Connections.** It shows or hides the column, opens
   off, is remembered on reload like the other switches, and the Key explains it in one plain
   sentence.
5. **Unchanged.** Cards and tree pages keep the "A movement across churches" label, and the census
   `kind` data is not touched. Any Key row or code that only served the old band is removed.

**How it was carried out.** The column sits to the right of the rivers in each era that holds a
cross-church movement; an era with none shows no empty column, so the map does not suggest that
era had none. A movement is now drawn only in its column: it no longer counts toward its river's
width, sits on no river as a mark, and does not pull rivers together or apart. The switch is its
own chip beside Stories and is remembered in the browser under `tree-movements`, the same way the
Major links choice is kept. On 2026-11-09 none of the six cross-church movements has a census
link, so no ties show yet; IX.50 names IX.33 and IX.24 in its text only. Screenshots:
`Build/Ministry/Features/Church-Family-Tree/Screenshots/2026-11-09_P2-E10d/`. Stop point: Mark sees
the screenshots.

**Moved to the left (Mark, on the screenshots).** "lets put them on the left side as this is on the
other side of the out of the niceen movements": the right edge holds the lane outside the Nicene
floor, so the column now sits left of each era's first river, below the era's text, with names
reading leftward. It fits in the space already there, so the rivers do not move.

## 2026-11-09 — Era 10 global completeness sweep, by region and by river

**Decided (Mark: "1 and across the rivers too").** Era 10's roster leans American (29 of 56 entries
are tagged North America). The Catholic and Orthodox rivers barely reach the Global South. Step 0's
completeness sweep runs again for era 10, by region and by river, under the same standard and
evidence rule, and returns to Mark's gate. Full entry: Atlas World Map Decision-Log, same date.

## 2026-11-09 — Era 10 global sweep gate ruled

**Decided (Mark, by number, G-80 to G-150).** Every answer matches its recommendation. The 14 ready
rows and 23 named lines are drafted, reviewed and applied as P2-E10h. IX.11 is narrowed by change
order (G-132 b). The 15 "enter once" candidates wait for their named sources, and the 22 holds wait
too. Full entry: Atlas World Map Decision-Log, "ERA 10 GLOBAL SWEEP GATE".

---

## 2026-11-09 — P2-E10h applied: data release 25

The global sweep's 15 ruled rows (IX.59 to IX.73) and 61 register edits are drafted. They were
reviewed in three rounds and approved to proceed in Round 3. They are applied as data release 25:
322 movements, 578 links. The atlas gains the 4<->5 bridge lane (G-80 c). Held lines and open
points are in Open-Gaps 139 and 140. Full entry: Atlas World Map Decision-Log, "P2-E10h carried
out".

---

## 2026-11-10 — P2-E10d approved; four open calls answered

**Decided (Mark: "take every recommendation").**
- **The left-side movements column is approved as built.** Movements are drawn only in their own
  column: no river width, no mark on a river and no river card. An era with no cross-church
  movement shows no column. It ships after a merge with data release 25, whose new cross-church row
  (IX.60, the church struggle against apartheid) appears in the column.
- **IX.44 and the United States: not carried out, and returned to Mark.** On a closer reading, every
  row whose place label says "N. America" lists no modern country (for example VIII.10, VIII.14 to
  VIII.16 and IX.15). Adding the United States to IX.44 alone would break that pattern for one row.
  What "N. America" should map to is a cross-row question for Mark.
- **A lane's first dot sitting above its river, and "this map…" in participant copy.** No
  recommendation had been given on either, so neither is treated as ruled. The recommendation now
  put to Mark is to leave both as they are. That changes nothing, and both stay open in
  Open-Gaps 140.

---

## 2026-11-10 — P2-L10 starts; evidence for era 10 links

Mark: "yes, start P2-L10". The era 10 gate has ruled, so the 2026-11-08 deferral ("The link work
covers eras 1 to 9") ends. On the evidence question Mark chose (b). A church body's own dated text,
read online, and a study confirmed in the run may support a link. Such a link reaches Widely
Accepted at most, and Documented stays reserved for a quote held in the Library. Full entry: Atlas
World Map Decision-Log, "Change order: evidence for era 10 links".

Era 10 runs in two parts by lane, as era 9 did:
- part 1: the Protestant, Pentecostal, Cross-Family and Protestant-bridge lanes, 38 movements;
- part 2: the rest, 33 movements.

---

## 2026-11-10 — A seventh link type, "member of"; Q2 and Q3 as recommended

Mark: "do the right thing not the easy, so b", then "Q1 b only". Membership of a council or
fellowship of churches is its own link type, "member of", and never major. A movement writer's own
dated text counts like a church body's own text, capped at Widely Accepted. Each denomination's own
statement in *Religious Bodies 1906* counts as its own text. Full entry: Atlas World Map
Decision-Log, "Change order: a seventh link type".

## 2026-11-10 — Rows labeled "N. America" get countries from their own text

Mark chose option (c). A row whose place label includes "N. America" lists a modern country only
where its own text names that country or a place in it. Full entry: Atlas World Map Decision-Log,
"Change order: modern countries for rows labeled 'N. America'". The work ships as data release 26
after review.

---

## 2026-11-10 — Data release 26: "N. America" rows gain their countries

30 rows gain the United States, Canada or Mexico, each from a sentence in the row's own text. It
was reviewed in two rounds and approved to proceed. Full entry: Atlas World Map Decision-Log, "Data
release 26".

---

## 2026-11-10 — A "member of" link may be Widely Accepted on the membership record alone

Mark chose Widely Accepted. A council's or member church's own dated membership record carries a
"member of" link to Widely Accepted with no study beside it. This settles Open-Gaps 143. Full entry:
Atlas World Map Decision-Log, same date.

---

## 2026-11-10 — P2-L10 done: era 10 is linked

The era 10 links were drafted, reviewed and applied in two parts.
- Part 1: data release 27, 33 links added.
- Part 2: data release 28, 33 links added.

Each part passed independent review in its second round. The census now holds 644 links. Three
are "member of" links, from the Disciples of Christ, the Church of Greece and the Kimbanguist
church to the World Council of Churches. 28 of the 71 era 10 movements still have no "gave rise
to" or "continued as" link coming in, down from 48. 9 have no link at all. Open-Gaps 149 lists
them. Records are in `Build/Ministry/Operations/Audits/2026-11-10_links-era-10-part-1/` and
`-part-2/`.

---

## 2026-11-10 — P2-G89 starts: the eras 8 and 9 global sweep

Mark: "start the eras 8-9 sweep". This carries out his scope of 2026-11-09 ("eras 8 - 10 for
now"). Eras 8 and 9 lean on Europe and North America:
- Era 8 (1650-1815) has 30 entries. 18 are tagged North Europe, and Africa, Latin America and
  Greater Asia have one each.
- Era 9 (1815-1906) has 51 entries. 45 region tags are North Europe or North America.

The method is that of the era 10 sweep, with four regional passes: Africa; Latin America and the
Caribbean; Asia and the Pacific; and the Middle East, Caucasus, Russia and Eastern Europe. Each
pass covers every river, uses non-English sources, and must answer the timeline breaks of
Open-Gaps 135 and 142 that fall in its region. That includes Mark's test that a break tied to
another movement, such as the Jesuits' worldwide missions, is not split off. Eras 8 and 9 are
frozen, so the results come to Mark's gate as change orders.

---

## 2026-11-10 — The people list ruled; P2-G3 applied as data release 29

**How it was reached.** P2-G3 published the people list for Mark (https://claude.ai/artifact/BDrnfEJ6WH5rn4tizoGxeE):
the 22 person entries, every tradition's people row, and five questions, each with options and a
recommendation. Mark answered "A a, B a, C a, D a, E a" (2026-11-10).

**Decided (Mark).**
- **A.** Athanasius is told within the catechetical school, where the Library shelves his works
  (principle 4). II.1's text names him as its first bishop and links to his page.
- **B.** A person told within no tradition (Jovinian, Peter the Iberian) is a Pre-Survey Candidate
  with the status word "Told within no tradition". No new status.
- **C.** A named voice counts on words of their own: their own writing, a document issued or signed
  in their name, or verbatim minutes. Speech that others report for them, and works of disputed
  authorship, do not count, for quotes and Library rows alike.
- **D.** The people the later-worlds count found are held for a follow-up: the count is re-run with
  each alias checked for namesakes and the editions' own notes left out, and the clean list goes to
  Mark. The 22 ship now.
- **E.** The later Carthusian movement runs 1300 to 1534. 1534 onward is held as a named gap until
  the Library holds a voice of its own (principle 3; Chauncy's Historia is wanted).

**Decided (Mark, 2026-11-10, asked after the release was built).** Until the map has its people view
(P2-P), it leaves person entries, Tertullian included, and the links whose end is a person out of the
map. Shown with: show them as tradition dots for now, as Tertullian was.

**Decided in the build, under the rulings.**
- A movement whose people row is empty carries `peopleNote`, one plain sentence saying why. This
  carries principle P4b's "its card says why" into the census; the validator requires it and the tree
  page shows it.
- Where a link names two person entries, `concerns` names the person whose words its sources quote
  (the two links to the Reformed cities go to Calvin).

**Applied.** Data release 29: 353 movements, 689 links. Audit:
`Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/`. Open items: Open-Gaps 150 to 156.

---

## 2026-11-10 — P2-G89 at Mark's gate: the eras 8 and 9 global sweep

**Done.** Four regional passes (Africa; Latin America and the Caribbean; Asia and the Pacific; the
Middle East, Caucasus, Russia and Eastern Europe) and a river-by-river cross-check. They are merged
into one record:
`Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`.
An independent reviewer read it in three rounds (Round 1 full, Rounds 2 and 3 targeted). Round 3
passed with no findings, and the cap is reached. The pass files are in
`Build/Ministry/Operations/Audits/2026-11-10_g89-sweep/passes/`.

**Found.** 68 rows, 62 counted (6 sit inside another candidate): enter 22, enter once 2, named
line 18, hold 19, already carried 1. Every Open-Gaps 135 and 142 break in 1650-1906 is answered
under Mark's uniqueness test, except two in North Europe (the Scottish church after 1650 and the
Swedenborgian New Church after 1815), which no pass covered. New breaks found: Kongo after 1650,
the Copts c. 1300-1517, the Moravians after 1815, Southern Africa, and China to 1906 (not 1793).
Data release 29 landed during the sweep; Round 2 checked its new rows against the candidates.

**At the gate.** https://claude.ai/artifact/34vANZonmFxqr9KXUUUdr4 — questions G89-1 to G89-55,
each with options and a recommendation. The cross-cutting ones come first: a Society of Jesus row
for 1650-1814, Propaganda Fide and the MEP as carrier lines, VIII.7's four wings, a Moravian row
after 1815, the home of Southern Africa, and how the frozen-era change orders are handled.

**Not changed.** The census. Eras 8 and 9 are frozen, so every addition Mark admits is a change
order, drafted and reviewed after his ruling.

## 2026-11-10 — What 'living' means: P2-V applied as data release 30

**Ruled before this chunk.** Ruling 15 (2026-11-06) asked for a written definition of "living"
and a check of every living flag before the leaf appears. The era 10 change order (2026-11-08,
rules 2 and 4) set what the mark means: alive today, in every era, governed only by the frozen
Living-Era Protocol Addendum V1.0 (R2 to R4). Principle 3 of the gap sweep (2026-11-09) set that a
living tradition past its entry's end gets a successor entry, not a stretched one. The era 10 gate
(G-5, option a) kept the mark on episodes of living traditions and on bodies with no dated source
yet, with the source wanted. This entry carries those rulings out; it decides nothing new.

**The definition (carried-out text, on the method page under "What the living mark means").**

> A living mark means one thing: the tradition is alive today, in 2026. It is the only statement the tree makes about the present. Everything else on an entry is history.

> The mark belongs to the tradition, not to the entry's dates. An entry that ends in 1300 still carries it when the church, religious order or community it describes survives today. Its later history belongs to a later entry. Where the tree has no later entry yet, the gap is named, and the dates are never stretched to cover it.

> An episode counts. A revival, a reform or a single period in a church's history is marked living when the wider tradition it belongs to is still alive.

> Surviving ideas are not enough. A school, a party or a sect whose own community ended is not marked living, even when its writings are still widely read. A modern group that adopts an ancient name is not counted as its heir unless a record shows an unbroken community.

> Decline is not an ending. A tradition is marked ended only when the record shows a clear end: it dissolved, it merged into another body, or its last member died.

> Each mark rests on dated evidence, beginning with the body's own recent words: a dated statement, report or rule. A mark is "documented" when an independent source confirms it and we have checked that source. It is "reported" when it rests on the body's own word, or on an outside source we have not yet checked. Where we hold no dated source yet, the record says so, and the missing source is listed as wanted.

> We describe what a body's dated documents say, never what its members believe. A living church can change its teaching, so each mark is a dated reading of the record, not a permanent verdict.

> Sometimes two churches claim the same ancestors, or the record breaks off for centuries. Then the claim of descent gets its own confidence grade, on the same five levels the tree uses for links.

**How the rule reads each kind of entry** (the working rule the check applied; audit
`Review_Brief.md`). A church or one period of a church in a place is living when that local
church continues to today, through later entries or a present-day body; it is ended when that
local community ended, even if the wider communion lives on. An order is living while it exists.
A movement or revival inside a church is living as an episode of it. A school, circle of writers
or party in a controversy is not living unless its own community continued. A separate body is
living while it exists. An entry on a "continued as" line reaching a living era 10 entry is the
same tradition, by the tree's identity rule.

**The check.** All 330 movements (persons are not movements). On main before this release, 192
flags were true, not the plan's 169. Era 10's 65 flags stand as the era 10 gate set them; 12 of
them now cite dated evidence they lacked. Every flag in eras 1 to 9 was checked both ways: forward,
from each flag to its evidence; backward, from 58 present-day families to the entries that carry
them. Drafted by Sonnet researchers, reviewed by Opus in three rounds (approved in round 3).

- Of the 127 true flags in eras 1 to 9: 117 kept, 9 kept with a new descent grade, 1 dropped (Latin
  Pastoral-Congregational Christianity, the North African church, whose end its own text records).
  The Alexandrian catechetical school stays living: its world's own record (Article 29, confirmed
  by Mark 2026-07-17) names the Coptic Orthodox Church as its primary living heir, and a built
  world's confirmed status governs its census flag.
- 73 flags move from false to true: mostly middle periods of living churches on their own
  "continued as" lines (the Armenian, Byzantine, Church of the East, Latin, Russian lines), and
  orders the flag had missed (the Carmelites, the later Carthusians). 59 stay false.
- After: 264 living (era 10: 65). Every living flag now carries `livingEvidence.basis`, and either
  `carrier` (the entries that carry the same tradition today) or its own dated evidence and grade:
  in eras 1 to 9, 6 CD, 62 CR and 4 none. 23 carry a descent grade.
- Every quote was found verbatim by two methods: in the page saved when it was taken, and in a
  fresh fetch (88 in the research batches, 23 for era 10, and each quote added in revision). Five
  home-page items whose text had rotated count as unverified.

**Decided in the build, under the rulings.**
- The census gains `livingEvidence.carrier`, and the validator requires every living tradition
  to say what its mark rests on (a carrier, or a grade of CD, CR or none). A carrier must be
  living and must hold its own evidence.
- A descent grade judges descent itself. It does not copy a "continued as" link's grade when that
  grade reflects the tree's sources rather than a break in the church (round 1, CO-2).
- A living flag with no recorded end and no dated source stays living, graded none, with the
  source wanted, as the era 10 gate ruled for the same case (round 1, CO-3).
- Citation dates in the public file are written out ("8 September 2026").

**Applied.** Data release 30: 353 movements, 689 links. Audit:
`Build/Ministry/Operations/Audits/2026-11-10_living/`. Open items: Open-Gaps 157 to 163. The leaf
itself waits for P2-K1 (Mark's pick).

---

## 2026-11-10 — P2-G89 gate ruled: all recommendations

**How it was reached.** The gate page (https://claude.ai/artifact/34vANZonmFxqr9KXUUUdr4) put
G89-1 to G89-55 to Mark, each with options and a recommendation. Mark: "all recommended"
(2026-11-10).

**Decided (Mark).** Every question takes its recommended option, sub-questions included, as stated
in §8 of `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Eras8-9_GlobalSweep_V1_0.md`.
Where a recommendation has two steps ("hold, then a line"), the first step applies now and the
second when its condition is met. G89-9 takes (a), the Kongo row with its thin middle stated
plainly.

**Decided (Mark, asked after).** G89-8 takes (a): the Coptic row starts at 1517, by Mark's leave
for this one row to begin in era 7 (G89-6, sub-question 2). Shown with: start at 1650 and log
1517-1650 for the era 7 owner. 1300-1517 is logged for the era 6 owner.

**Next.** Carry out the rulings as named change orders to the frozen eras 8 and 9 (G89-6 a: one
register, drafted and reviewed together, one data release).

---

## 2026-11-10 — The later-worlds people ruled (P2-G3b)

**How it was reached.** P2-G3b re-ran the later-worlds count that Mark held back in answer D a,
with namesakes checked, editorial matter masked and every counted passage read in context and
reviewed (audit: `Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/`). The clean
list went to Mark as the artifact "Later-Worlds People"
(https://claude.ai/artifact/AGVVFoi57c6gNtDtVoyADC): 32 people passing, 14 recommended, 18 held,
and three questions, each with options and a recommendation. Mark answered "take every
recommendation" (2026-11-10).

**Decided (Mark).**
- **A. Founders who pass by this route are held.** Ruling 14's test stands as worded ("founded no
  lasting movement"); change order 10c's exception for founders stays tied to the own-works count.
  Held: Priscillian, Valentinus, Mani, Novatian, Hilarion of Gaza, Apollinaris of Laodicea, Valdes,
  Francis of Assisi, Zwingli. Each is told within their movement's entry. Shown with: take the
  founders whose own words the Library holds; take all nine.
- **B. Answer C applies as written.** A letter issued in a person's name and a jointly written work
  count as their own words; sermons taken down by hearers do not. Paula and Pamphilus get entries;
  Tauler is held. Pamphilus is told within the catechetical school, where the Library shelves his
  work. Shown with: hold all three; take all three.
- **C. Two later traditions need two different witnesses.** One author's book shelved twice does
  not make two traditions. Constantius II and Basilides are held. Shown with: count shelves as
  written.
- **The 14 entries:** Polycarp of Smyrna, Methodius of Olympus, Pamphilus, Lactantius,
  Constantine, Paula, Basil of Caesarea, Gregory of Nazianzus, Patrick, Justinian, Bede, Gregory
  VII, Innocent III, Hugo Grotius. Built as person entries in the shape of release 29's, hidden
  from the map until P2-P like the others.

**Also held, under the rules as written (no question):** Paul of Samosata, Mesrop Mashtots,
Maximilla, Kaleb, Heraclius and Bonaventure: the Library holds no words of their own and no
recorded position that answer C counts. Reasons, one per person: Open-Gaps, "The later-worlds
people held, with their reasons" (2026-11-10).

**Correction to ruling B's premise (decided by the coordinator under Mark's "take every
recommendation", 2026-11-10; Mark free to override).** The build's review found that the Library
does not hold the text of Pamphilus's Apology for Origen: `npnf203` has only Rufinus's preface and
epilogue to his Latin version, and the only other words of Pamphilus held, the fragments on Acts in
`anf06`, are of disputed authorship. Ruling B was put as "Pamphilus wrote the Apology with
Eusebius". Pamphilus is held by the standard every other held person met (no undisputed words of
his own in the Library), and the Apology is wanted. The release carries 13 entries.

**Cap ruling (data release 31, round 3).** The build's third Opus round (`Build/Ministry/Operations/Audits/2026-11-10_later-worlds-people/build/reviews/Review_Round3.json`)
left one substantial finding: two swapped sentence fields in Basil of Caesarea's fact table, the
drafting record. The coordinator closed it under Mark's standing instruction (2026-11-10) not to
bring him every decision. The reviewer's exact text was applied (`build/p2/Draft_r3.json`) and
checked against the source lines, and no census field depended on it.

## 2026-11-10 — Three held people come in once the Library holds their words (P2-G3b, second release)

**How it was reached.** The Library thread filled three of the held people's wants (PR #1577,
`Build/Ministry/Features/Source-Library/CFT-Wants.md`). The coordinator ruled, under Mark's
"take every recommendation" (2026-11-10), that each now passes the test the hold rested on; Mark is
free to override.
- **Pamphilus of Caesarea.** The Apology for Origen, Book I, in Rufinus's Latin, is now vendored
  (`pamphilus_apologia-pro-origene-rufinus-lat_lommatzsch1846.txt`; PG 17 as a second witness).
  The correction to ruling B's premise held him only for the missing text; ruling B counts the
  jointly written Apology as his own words. He gets an entry, told within the catechetical school.
- **Bonaventure.** His own works are now vendored: the Legenda maior in Salter's English (1904)
  and the Tria opuscula (Quaracchi 1911). He was held only for having no words of his own held.
- **Heraclius.** The Ecthesis (638), a document issued and signed in his name, is in Mansi X and
  now shelved on his home tradition. The review judged it still counts under answer C, though a
  later letter has him say Sergius wrote it; the entry names both.
- **Nikodemos the Hagiorite** (1782) leaves the people row of the 1453-1650 Ottoman tradition, out
  of its window; he stays in the Kollyvades row. The Pedalion shelf row moves under the Library's
  fix.

Francis of Assisi and Priscillian, whose own words the Library now also holds, stay held as
founders (question A).

## 2026-11-10 — Where each river leaves its parent

**The defect (Mark, 2026-11-10).** "why does the reformation and protestent river come out of greek
east, thats wrong". The map drew each river out of the river of whichever link into its first
movement came first in the data, with "influenced" counted as descent. Wittenberg's first such link
was an influence from Chrysostom's Antiochene tradition, so the Protestant river rose from Greek
East. The parent had moved by accident as the Phase 2 link work added links. A second fault: two
Protestant movements start in 1517, and data order chose which one was first. A fallback table
covered only five lanes.

**Ruled (coordinator, under Mark's standing instruction to decide routine calls).** A river's
origin is a claim about descent, so neither an influence nor data order may decide it.
- A river's first movements are all its church bodies tied at its earliest start.
- Its parent is the river of the strongest descent link into them. The order is: "gave rise to"
  or "continued as" (lineage) before "broke with" (a break, counted only from a movement that
  started earlier); then major before minor; then confidence; then the parent's earlier start;
  then its ID.
- With no such link, the page's record declares the parent, with a reason, a confidence on the
  five-level scale and a source. Lane 0 is the origin trunk.

**Built.**
- `cft-website/index.html`: `RIVER_ORIGINS`, one entry per river, from which the map draws. The
  inference code and the old fallback table are gone.
- `tools/validate-census.mjs` holds the rule and fails when the record and the census disagree, in
  these cases: a river with no entry; a lineage entry that is not the rule's pick; a declared entry
  where a descent link exists; a missing reason, confidence or source; a quote not found verbatim
  in its Library lines; a chain of parents that never reaches the trunk; or a parent that starts
  later than its child. A new census link that would move a river now fails CI until the record is
  changed on purpose.
- `tools/tests/validate_census_river_origins.test.mjs`: nine cases.

**Each river, before and after.**

| River | Before | After | Basis |
|---|---|---|---|
| Syriac East | Non-Nicene (Bardaisanite influence) | origin trunk | declared, Contested: Eusebius, *Church History* 1.13 (the Thaddeus story, a legend) |
| Syriac/Prot. bridge | Syriac East | Syriac East | lineage: St Thomas Christians gave rise to the Mar Thoma reform |
| Caucasus | Syriac East (influence listed first) | Greek East | declared, Contested: Gregory consecrated at Caesarea; Ormanian (1912) gives the dispute |
| Greek East | Africa (Alexandria influence) | origin trunk | declared, Widely Accepted: Eusebius, *Church History* 4.5 (Jerusalem's bishops from James) |
| Greek/Latin bridge | Greek East (influence) | Greek East | declared, Inferential-Thin: its first voice Eusebius of Caesarea; Nicaea (*Life of Constantine* 3.6) |
| Africa | origin trunk (Greek-apologist influence) | origin trunk | declared, Widely Accepted: Eusebius, *Church History* 2.16 (the Mark tradition, as reported) |
| Africa/Latin bridge | Africa | Africa | lineage: Uganda martyrs continued as |
| Latin West | origin trunk (influence) | origin trunk | declared, Widely Accepted: Tertullian, *Prescription* 36 |
| Latin/Prot. bridge | Latin West | Latin West | lineage: Philippine Catholicism gave rise to the Philippine Independent Church |
| Protestant & Evangelical | Greek East (Chrysostom influence) | Latin West | lineage: the Hussites "continued as" the Czech churches (Documented), one of the river's two 1517 first movements |
| Global Revival & Pentecostal | none | Protestant & Evangelical | declared, Widely Accepted: the census record's own works (Tudur Jones, Oak, CHC 9) |
| Cross-Family | Protestant & Evangelical | Protestant & Evangelical | lineage: the mainline gave rise to progressive Christianity |
| Non-Nicene | none | origin trunk | declared, Widely Accepted: Tertullian, *Against the Valentinians* 4 |

The plain parents were built directly. Five went to the coordinator as options with
recommendations: Syriac East, Caucasus, Greek East, Africa and the Greek/Latin bridge. The
coordinator took every recommendation. Shown with them: Syriac East from Greek East (via the Antioch
tradition) or unattached; Caucasus from Syriac East or the trunk; Greek East from Africa; Africa from
Greek East; the bridge from Latin West or the trunk.

**Wanted, not added.** A sourced break link from the late-medieval Latin church to Wittenberg, and
a "gave rise to" link from Caesarea to Armenia. Both are census changes under the link evidence
standard (Open-Gaps 173).

**Checked.** `validate-census.mjs` with `--atlas` and `--tree` gives 0 errors. All 53 census tests
pass. `atlas-check --edges-only` passes. The commentary and spelling checks are clean. The gap
between neighboring rivers is at least 18 px at both zooms, the same before and after. The switch
check is unchanged: with Africa hidden, 13 of 14 rivers and 297 of 323 dots stay on, and all of
them come back when Africa is restored. No page errors. Screenshots before and after (full map,
the early centuries, close on 1517; dark and light; desktop and phone):
`Screenshots/2026-11-10_river-origins/`.

**Approved (Mark, 2026-11-10, on the artifact "River Origins Review",
https://claude.ai/artifact/NNXYt18C89c21cMqTa56k3).** "rivers look good, merge it".

---

## 2026-11-10 — P2-G89b carried out: data release 33 adds the eras 8 and 9 sweep's 26 rows

**Done under the gate ruling ("all recommended", with G89-8 a and G89-9 a), in auto mode.** Each
admitted item is a named change order to the frozen eras 8 and 9, recorded in one register (G89-6
a): the slice drafts, `Build/Ministry/Operations/Audits/2026-11-10_eras8-9-rulings/drafts/`. Data
release 33: 395 movements (369 before), 733 links (689 before), 289 living (264 before).

- **26 new rows,** VII.34 to VII.49 and VIII.53 to VIII.62, in eight slices (Africa, Latin America,
  Asia in two parts, the Middle East in two parts, the rivers in two parts). The Coptic row starts
  in 1517 by Mark's leave. Canudos is the only new row not marked living.
- **34 row changes** carry the ruled named lines and the living pass. Where a new row became the
  latest entry of a living line, the older row's dated evidence moved to it and the older row names
  it as carrier (the Jesuits, the Moravians, the Old Believers, the Maronites, Kongo). Five rows
  outside the slices' lists changed only so that no carrier is itself carried, as P2-V's rule
  requires: VI.13, IV.10, V.22, the Hussite row and the Czech churches row.
- **48 links; 4 retired and replaced** where a new row sits between two rows the tree already
  joined: IV.26 to VIII.13 (through the Coptic row), VI.30 to VIII.40 (through the Church of the
  East's three patriarchates), VII.19 to VI.11 (through the Jesuits 1650-1814, G89-1 b), VIII.31
  to VII.7 (through the Old Believers after 1815, G89-38 a).
- **Rules the coordinator set for every slice:** a row the sweep record calls living today, with no
  living carrier, stays living with its own grade "none" and the dated source wanted (P2-V's
  practice); modern-country IDs come only from census rows; every new row lists its sources; a
  rendering of a non-English quote shows its original beside it.
- **Reviews.** Each slice was reviewed by Opus from its sources, with every quote re-fetched. AF
  and RV-A reached the cap over the sources lists added after their approval; Mark ruled twice
  ("take the recommendation"): one ordered check, then its fixes applied as written (System Hub
  Decision Log, both 2026-11-10).
- **Evidence.** A raw online text carries a link at Widely Accepted at most; Documented needs a
  Library quote. This is the conservative reading of the sweep's rule.
- **River 4.5 now leaves Latin West.** Kongo after 1650 (VII.42) is now the first movement of the
  Africa/Latin bridge, so by the rule in "Where each river leaves its parent" (2026-11-10) the
  river's origin is its "continued as" link from the Kongo entry to 1650, parent river 5. It was
  river 4, through the Uganda martyrs. This is the parent G-80 (c) named for the bridge.

**Held and open.** Every hold, want and open point is in Open-Gaps, from "Eras 8 and 9 rulings,
Africa holds" to "Small questions the eras 8 and 9 rulings leave open" (2026-11-10), including
VIII.52's 1911 end and the two North Europe breaks, which stay open.

**Next action.** A follow-up chunk enters the held items whose sources the Library's batch 2 now
holds. Full entry: Atlas World Map Decision-Log, "P2-G89b carried out".

## 2026-11-10 — P2-G89c carried out: data release 34 enters the held eras 8 and 9 items the Library now sources

**Done under the same gate ruling ("take every recommendation"), in auto mode.** The ruling held
some items only for want of a source. Entering one once the Library holds it carries out the same
change order (G89-6 a). Each item was tested against its vendored source first. Data release 34:
396 movements (395 before), 736 links (733 before). Audit:
`Build/Ministry/Operations/Audits/2026-11-10_eras8-9-sourced/`.

- **One new row:** the Transylvanian Unitarian Church, 1660-1906 (VII.50), lane 8, continuing the
  anti-Trinitarian entry, which now names it as the carrier of its living mark.
- **Seven named lines** in existing rows: the Peking mission to 1808 (the Russian church to the Holy
  Synod); the Cofradia de San Jose (Philippine Catholicism); Korea's Protestant beginnings (the
  Missionary Movement's Native Churches); Marsden's chaplaincy and New Zealand mission (the
  Victorian Church of England); Saint-Domingue and the Bethlemites (Colonial Latin American
  Devotional Catholicism); Holly's Haitian Episcopal church (the Black Church in America).
- **Links:** VOC world "continued as" Indonesian Christianity (Widely Accepted, the 1815-1861 gap
  named); the Unitarian row's two links; two links regraded from Inferential-Thin to Widely
  Accepted on their candidate study quotes (China and the Jesuits; southern Africa and Herrnhut).
- **Held, with reasons:** AP7, LA8-8 and the parts no source carries. Open-Gaps, "The held eras 8
  and 9 items the Library's sources now carry" (2026-11-10).
- **Coordinator calls** (session 01JMNsSDbFsmawtDvuAiukNQ, under Mark's standing instruction to
  decide routine calls, 2026-11-10):
  - Open-Gaps 191 (the VOC lineage question): yes, the VOC world's churches "continued as"
    Indonesian Christianity, at most Widely Accepted on Aritonang ch. 9 (Joseph Kam's work from
    1815 as a rehabilitation of the same church), the 1815-1861 gap named in the link and kept in
    Open-Gaps.
  - LA8-6's homes: Holly as a line in the Black Church in America, not the Haitian church row (no
    frozen date change; a Protestant lane); Saint-Domingue in Colonial Latin American Devotional
    Catholicism. The concordat church after 1860 stays held.
  - AP12: only the Anglican line enters, on Marsden; the Catholic and Methodist lines stay held.
  - RV-7: a lane 8 row, not a line closing the anti-Trinitarian entry, which would stretch a
    frozen era 7 row across the era line.
  - AP11: a line in the era 8 Russian church row only, since the source ends in 1808.
- **Worker calls under the same rule:** LA8-8 held (Claret's Apuntes do not carry the line the
  gate names); AP7 held (no Catholic document printed word for word); the Korean Catholic line
  after 1886 held for a later entry, as the Korean Catholic row's own status text keeps that gap;
  the Society of Jesus link to the Unitarian row dropped (only the Unitarians' later account blames
  the Jesuits; the army and a Catholic bishop did the seizing).
- **Reviews.** Each slice was drafted by Sonnet and reviewed by Opus from its sources, two rounds at
  most; every slice approved. The Library shelf rows for Holly, the Korean Repository, Marsden and
  Ferencz (1875) moved onto the entries that now carry them.

**For Mark, through the coordinator:** two Section A questions, the Tolstoyans and the Dukhobors
(Open-Gaps, "Two Section A questions for Mark", 2026-11-10).

## 2026-11-11 — Person briefs: 60 to 120 seconds, personal and theological (Mark, 2026-11-11)

**Decided (Mark, relayed by the coordinator).** Mark first chose "go with option 1, flexible 60–90
seconds". The same day he revised it: "i want the brief to be both perosonal (their story) and
theological (major stanses, "they fought for, they developed, they defended ....)it ok if they run
long, we can also redo them if they don't meet the standard. lets say 60 - 120 minutes depending
on their size of scope and influence". He meant seconds.

The standard is:
- A brief runs 60 to 120 seconds when read aloud, about 150 to 300 words. The person's scope and
  influence set the length.
- Every brief is both personal (their story) and theological (what they fought for, developed
  and defended).
- An existing brief that misses the standard is rewritten.

Options shown before the revision: (1) a flexible 60–90 seconds, 150–220 words, set by what the
sources carry, never padded (chosen, then revised as above); (2) a fixed one minute; (3) 90 seconds
to 2 minutes for every person.

**The brief's shape.**
1. Who they were, in one line, with time and place.
2. Their story, and what they did or wrote that mattered.
3. The positions they fought for, developed or defended, and why these mattered to their own
   tradition and to its opponents.
4. One line in their own words, where the Library holds them.

Facts the person's card already shows (dates, place, role, works) are not repeated.

**How it reads aloud (Mark, after the 2026-11-11 recording sample).** Mark's words: "so these
are a little flat and ai ish, i want it a little more story telling, not fact giving. the years
read as natural not just reading numbers, the sentences flowing together not all short simple
sentances for an elementary student". He placed the flatness in one brief: "the flatness was in
the origin, person". He found that "the bogomils listens better". These notes are part of the
standard for the person rewrites:
- A brief tells a story. It does not list facts.
- Years are written to be spoken naturally, not read out as bare numbers.
- Sentences flow and connect. They are not all short and simple. Grade 8 is a floor for the
  reading level, not a target.
- A brief names its real witnesses. Mark's words: "we need to not say his editor, it should be
  accounts tell of 5 times he...", and then: "i like eusebius says thats great it was the abstract
  reference to "his editor" that didn". So a brief names the person behind an account ("Eusebius
  says…", "Palladius tells…", "his own letters say…"). It never refers to whoever produced the text
  by role alone: "his editor", "the editor", "the translator", "a modern scholar", "the compiler".
  If the source matters to the story, the brief names the person. If it does not, the brief tells
  the event with "accounts tell…".
- The exception keeps the brief true to its sources. When the only account is partisan or hostile,
  or the accounts disagree, the brief says so plainly in story terms ("his enemies claimed…", "one
  account says…, another…"). A contested claim is never told as settled.

**Where it applies.** All 39 existing person briefs and next week's briefs for the 340 named
people. The 39 person briefs in the census on 2026-11-11 run 58 to 246 words (median 178). None
is over 300 words. 10 are under 150:
- Ephrem the Syrian 58, Origen 99, Hugo Grotius 104, Athanasius of Alexandria 107, John Chrysostom
  112, Bede of Jarrow 114, Gregory of Nyssa 117, Gregory of Nazianzus 121, Constantine the Great
  123, Methodius of Olympus 141.

All 39 are checked against the whole standard, not only its length, and rewritten where they fall
short.

**Recording.** No person brief is recorded in the 2026-11-11 batch (the coordinator's decision).
The 39 are recorded together in the chosen people voice once they meet the standard. The tree
narration planner leaves out every person row until then. Mark is choosing that voice from three
candidates (George, Bill, Brian), each heard reading the Athanasius brief.

## 2026-11-11 — Tradition briefs and documented stories recorded (data release 34)

**Done (Mark: "yes, record the sample and leave the built worlds out"; then "do the stories that
need updating or are done, then hold for the councils and new stories"; caps chosen on a question
card, "Caps as suggested").** Every tradition brief and every documented story whose text had
changed or had no recording is recorded, from `main` at f80e551c.

**Order of work (Mark, 2026-11-11).** Mark's words: "order of work, finish tradition briefs,
finish stories including counsels and new stores, then the who briefs, then the rivers and
connections that we will work on next week and maybe next month".
1. Tradition briefs (this batch).
2. The stories that are ready (this batch). Stories still being written, the councils and the
   like are held until their text exists, then get their own run.
3. The "who" briefs: the person briefs, after their rewrite to the standard set in "Person briefs:
   60 to 120 seconds, personal and theological" (2026-11-11).
4. Streams and connections, next week or next month.

**The three tree voices.** Mark's words for the people voice: "this of them all need a mature voice,
we take people seriousl[y]". Every tree voice sounds mature (40s to 60s), measured and warm,
serious without being solemn or preachy, and never casual, young or dramatic.

| Voice | Use | Id | Accent |
|---|---|---|---|
| Daniel, "Steady Broadcaster" | Tradition briefs | `onwK4e9ZLuTAKqWW03F9` | British |
| Neo, "Calm and Controlled" | Stories | `onegjDE2z0mQtp1g0HK7` | South African (Voice Library) |
| David Baker | People | `fxnZk29PIJ3WKEC9MDEo` | Canadian (Voice Library) |

Mark's words for the story voice: "keep neo for stories". For people he asked for "a warm mature
canadian voice", and he chose "david baker" by ear.

**How the people voice was chosen.** All four comparisons used `eleven_multilingual_v2`,
`mp3_44100_64` and the Daniel settings.
- Run "CFT people-voice comparison 2026-11-11": the Athanasius brief (597 characters) read by
  George (`JBFqnCBsd6RMkjVDRZzb`), Bill (`pqHfZKP75CvOlQylNhV4`) and Brian (`nPczCjzI2devNBz1zQrb`).
  867 credits. The Origen brief read by Daniel served as a fourth comparison.
- Brian and Charlie (Australian) were ruled out.
- Then the coordinator's run "Mark 2026-11-11 'give me a reading of 20 seconds of the origin from
  each'": 276 characters each, read by David Baker, Jeff (`bE3COCGjWQ0g9MBhv2cf`), Jason Worobec
  (`3RY5h7DeqeGY5EV6NrAl`) and Charles (`JsrIJzhkegmrtozsL1wV`). 536 credits.

When the person briefs are recorded, David Baker's id is passed on the command, never read from the
environment. The Athanasius text used in the comparison is real census text that fails the new
person standard: it opens on who claims him, mentions the Library shelf, says "his editor" and has
no theology. It is on the rewrite list.

**Settings, as printed by every request.** Model `eleven_multilingual_v2` for the briefs and
`eleven_v4` for the stories, both at output `mp3_44100_64`. Stability 0.95, similarity 0.68,
style 0, speaker boost on. Voice and model were passed on each command; none was read from the
environment.

**Sample (run "CFT sample 2026-11-11").** Three items, 1,996 characters, 968 credits:
- the stale Bogomils brief (800 characters, 388 credits);
- the stale story `cyrilline-miaphysite-egyptian-christianity-0` (610 characters, 296 credits);
- a new person brief, Origen in Daniel (586 characters, 284 credits).

Mark found the Bogomils brief "listens better" and the Origen brief flat. Origen was kept off the
site when person rows were held.

**Run (run "CFT full batch 2026-11-11 (Mark approved sample and caps)").**
- **Tradition briefs:** 121 (60 new, 61 stale), 179,236 characters, under the cap of 180,000.
  86,904 credits by the API's `character-cost` headers. One brief,
  `the-anglican-communion-twentieth-century`, failed on a 503 connection reset and was re-run. The
  account was charged for the failed request too, 400 credits with no audio returned.
- **Stories:** 181 (178 stale, 3 new), 255,204 characters, under the cap of 256,000. 123,731
  credits, no failures.
- **Rate:** 0.485 credits per character on both models, against 0.44 on the 2026-11-08 and
  2026-11-09 runs.

**Credits, reconciled.** This session's runs total 212,870 credits by their own headers:
- sample, 968;
- voice comparison, 867;
- tradition briefs, 86,904;
- the charged 503 failure, 400;
- stories, 123,731.

Two approved runs in other sessions used the same account on the same day, and their figures
come from their own reports:
- the coordinator's people-voice comparison, 536 credits;
- the person-brief pilot, run "CFT person pilot 2026-11-11", in David Baker's voice, cap 5,500
  characters (session_01JMNsSDwnAiKRGQ5GRsfSad). Its first report was Origen, 1,734 characters,
  841 credits; its final figure is in its own record.

The account read 1,835 used before the batch and 216,355 at the end of the stories.

**ElevenLabs' own history** (`GET /v1/history`, from 23:00 UTC on 2026-11-10) agrees with the
counter: 317 requests, 216,355 credits, all from these runs.

| Voice | Requests | Credits | What |
|---|---|---|---|
| Daniel | 124 | 87,976 | 121 briefs, the Bogomils and Origen samples, the charged 503 failure |
| Neo | 183 | 124,715 | 181 stories, the story sample, and one duplicate request |
| David Baker | 4 | 2,395 | the coordinator's comparison (134) and the pilot (2,261) |
| Six comparison voices | 6 | 1,269 | the people-voice comparisons |

The duplicate is the story `the-missionary-movement-s-native-churches-seramp-0`. It was charged
twice, 688 credits each, under two request ids 17 seconds apart (02:03:10 and 02:03:27 UTC). The
run sent one request for it and logged one success. The second request most likely came from a
retry in the network layer between this session and ElevenLabs. The 503 on the Anglican brief came
from that same layer. The cause cannot be confirmed from here. Together the two cost 1,088 credits
with no extra audio. A later paid run should compare the run log with this history afterward.

**Checks.**
- Every manifest entry records its voice, model, format and text fingerprint.
- Brief sizes run 568-681 bytes per character and 11.7-14.1 characters per second. Story sizes run
  491-598 bytes per character and 13.4-16.3 characters per second. None is truncated.
- Dry runs now plan nothing: 337 tradition briefs and all 503 documented stories match their text.
- The tree pages were rebuilt, and only Listen players were added, on 122 pages. 338 tree pages
  now play a recording. The map shows story players from the manifest when a page opens.

**What the batch left out, as ruled.**
- The 12 built worlds. Their tree pages show no tree recording, and their story plays in the
  Representative's voice.
- The 39 person rows.
- The 8 movements with no `longDescription`.

The tree planner now carries the built-world and person exclusions. It also treats a recording
whose text fingerprint no longer matches as stale (it used to count any recording as current).

**Limits.** The voices cannot be confirmed from ElevenLabs' side with this key. They rest on the
voice id in each request, the sizes, and Mark's ear on the sample.

## 2026-11-11 — Person-voice delivery: setting C (Mark: "c is best")

**Superseded** by "Person voice: Jon on Eleven v4, replacing David Baker" (2026-11-11).

**Decided (Mark, relayed by the coordinator, 2026-11-11).** Mark heard the Origen pilot clip and
found it "not warm and personal enough". He approved a three-way test ("yes, run the three-way
test") and, after listening, ruled "c is best". Person briefs are recorded with:
- voice David Baker, `fxnZk29PIJ3WKEC9MDEo`;
- model `eleven_multilingual_v2`, output `mp3_44100_64`;
- settings `{"stability":0.45,"similarity_boost":0.75,"style":0.3,"use_speaker_boost":true}`.

Tradition briefs and stories keep their own delivery (stability 0.95, similarity 0.68, style 0,
speaker boost on). A person run of `Build/tools/generate_tree_narration.mjs` (`--people`) takes the
voice and the settings on the command, `--person-voice-id` and `--voice-settings`. Both are
required, printed and never read from the environment.

**The test.** The restored Origen brief (2,148 characters) was read three times in David Baker's
voice, one clip per setting:

| Clip | Settings | Length |
|---|---|---|
| A, as before | stability 0.95, similarity 0.68, style 0, speaker boost on | 2:26 |
| B | stability 0.6, similarity 0.75, style 0.15, speaker boost on | 2:27 |
| C, chosen | stability 0.45, similarity 0.75, style 0.3, speaker boost on | 2:27 |

The clips are on the review page https://claude.ai/artifact/FtrkKBz8BHU9WMmDQLVu8v only. The run log
is `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/recording/warmth-test.log`.

## 2026-11-11 — Spend note: the Origen warmth test ran at full length

**What happened.** Run "CFT Origen warmth test 2026-11-11" was approved with a cap of 6,600
characters and recorded the full Origen brief three times. That came to 6,444 characters and 3,123
credits, 1,041 a request by the `character-cost` headers. The account went from 216,355 to 219,478
used. ElevenLabs' history (`GET /v1/history`) shows exactly those three requests, with the settings
as sent, and no duplicate.

Mark then revised the run: "just do 30 seconds of each", with a cap of 1,400 characters. That
message was queued at 03:24:24Z, after all three requests had finished (about 03:24 UTC by the
history). Recording 30 seconds of each, as Mark wanted, would have cost about 650 credits; the run
spent about 2,470 more.

**Cause.** Two coordinator sessions were relaying to the same worker at once: the outgoing one and
its successor. The approval came from the outgoing coordinator, a minute after the incoming one had
said to make no paid calls, and its revision then arrived too late.

**Fix.** One line of command. A worker takes paid instructions only from the current coordinator.
When coordination moves to a new session, the old one stops relaying paid approvals and passes them
through the new one.

## 2026-11-11 — Cap ruling: one recheck of the six restored person briefs

**Cap ruling (2026-11-11, Mark: "a, run the Opus recheck on the six").** Six early-church
person briefs had material cut only to fit the old 300-word ceiling. That material was restored
after Mark ruled that length follows scope ("we are fine going over a little, infact i want to make
sure we are not cutting off to get a perfect number"). The six are Origen, Athanasius of
Alexandria, John Chrysostom, Gregory of Nyssa, Gregory of Nazianzus and Constantine the Great. Each
had already used its three review rounds in the person-brief pilot. Mark ordered one targeted Opus
recheck of the restored text, which does not count toward the cap:
`Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/reviews/R4_cap-ruling_recheck.md`.
The restored drafts are in that pilot's `recheck-2026-11-11/` folder. Ephrem and Methodius lost
nothing substantive and keep their round-3 text.

## 2026-11-11 — Data release 35: the eight early-church person briefs, recorded

**Done (Mark: "2", "yes, go ahead and record the 8").** The eight early-church person briefs from
the pilot now meet the standard. They are the census `longDescription` for Origen, Methodius of
Olympus, Constantine the Great, Athanasius of Alexandria, Ephrem the Syrian, Gregory of Nazianzus,
Gregory of Nyssa and John Chrysostom, in data release 35. Each person's page plays the brief in
David Baker's voice.

**Length.** Text cut only to fit 300 words was restored, and six briefs gained material. The
recheck is in "Cap ruling: one recheck of the six restored person briefs" (2026-11-11), and the
texts and cards are in `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/final/`.
Each person card is saved there as JSON, ready for the people-layer build. No census field was
added for the cards.

| Person | Words | Recorded |
|---|---|---|
| Origen | 374 | 2:30 |
| John Chrysostom | 360 | 2:26 |
| Gregory of Nyssa | 346 | 2:12 |
| Athanasius of Alexandria | 325 | 2:14 |
| Constantine the Great | 312 | 1:58 |
| Gregory of Nazianzus | 307 | 2:06 |
| Ephrem the Syrian | 269 | 1:49 |
| Methodius of Olympus | 222 | 1:28 |

**Run "CFT early-church people 8, 2026-11-11".**
- Voice and model: David Baker (`fxnZk29PIJ3WKEC9MDEo`), `eleven_multilingual_v2`,
  `mp3_44100_64`.
- Settings: `{"stability":0.45,"similarity_boost":0.75,"style":0.3,"use_speaker_boost":true}`
  (delivery C). They were passed on the command with `--people`, `--person-voice-id` and
  `--voice-settings`, and printed on every request.
- Characters: 14,313, under the cap of 15,000.
- Credits: 6,939 by the `character-cost` headers. The account went from 219,478 used to 226,417.
  ElevenLabs' history shows the same 8 requests and 6,939 credits, with the settings as sent and
  no duplicate.
- Log: `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/recording/early-people-8.log`.

The pilot clips were never on the site, and these recordings replace them. Tertullian was not in
this run. The map still leaves person rows out until the people layer is built, so the recordings
play on each person's own page.

---

## 2026-11-11 — The people layer: Who beside every tradition and river (P2-P)

**How it was reached.** Mark looked at the first People view (draft PR #1585, a global Traditions |
People switch) and called the all-names view "a little chaotic". He asked for a Who control beside
the clicks he already has. Four takes were drawn on the real data
(https://claude.ai/artifact/Cu4jx1Zx1WVoJZJ386vMfZ, version 4). Mark converged on 2026-11-11.
His words are quoted where they settle a point.

**Decided (Mark, 2026-11-11).**
- **The traditions map stays primary.** There is no global People switch. It replaces the switch
  in the P2-P row of the Build-Plan.
- **A Who button on every tradition card.** It is full width and carries a count ("Who · 10
  people"). Mark: "the who needs to be prominate on the card too".
- **A Who pill on each river in each era.** Mark: "a river who click at the top of each era, so it
  would only open that river and era, if a stream starts in the era it would be in the beggining
  of the thick part".
- **A profile pill beside each tradition label.** Mark: "we need a profile pill next to each
  tradition also that opens that traditions who".
- **Names show on the map at once.** Mark: "the profile pills on the main page instantly show the
  names in the river or next to the tradition as designed". There is no card in between. Tapping
  the pill again, or the "Who: <scope> ×" chip, clears them.
- **Vertical stacks that stay with their river.** Mark: "for the world lets to them verticly, not
  accross other rivers. so if there is three names it would be three rows first one level with the
  world to the right and other names below it so it looks like they are attatched to the river and
  not crossing over to other worlds". A name is cut short with "…" where the next river begins, and
  the card has it in full. Where the right side is too tight, the stack uses the river's left side.
  A second stack on the same river starts below the first, with a dotted line to its own
  tradition. A stack shows up to 6 names for one tradition and 4 for a river in an era, then
  "+N more". Other traditions' labels under an open stack are hidden while it is open.
- **One profile icon.** Mark: "we are only using a profile icon not real pictures at this point.
  simple". Everyone gets the same icon, in the river's color. Likenesses (P2-PL) are deferred.
- **Option C is the base.** Plain stacks, no plates, and a chip in the switch bar.
- **Every name opens a person card.** Mark: "for each name we can click on and get their card with
  the voiced intro, standardized template of information and sources", and "the brief then the
  card context continues the story". The brief plays on open, as a tradition card's does. The card
  order is: name and other forms; Known for; dates (with "about"); place; tradition; role; the brief
  and its length; key works (3 at most); Legacy in two parts, "What traces to them" and "How
  they're remembered" (honoured, disputed or condemned, and by whom; Mark merged "named by other
  traditions" into it); What is uncertain (the brief's caveat, then more); links on the map;
  Sources last, in two groups, "Their own words" and "Written about them".
- **Missing fields are absent, never filled.** A named voice with no brief and no card data shows
  what exists: name, dates, tradition, and words of theirs the record quotes.
- **A person shows once.** Within one Who view, each person shows in one stack. The card shows the
  other traditions that name them, in the words of those traditions' own records ("wrote against
  him within Marcion's own lifetime"), never as membership.

**Decided in the build, under the rulings.**
- **Where a name goes when neither side has room.** Where both sides of a tradition are too tight
  (under 70 map units), the stack starts on the line below the label, beside the dot. This keeps
  the rule that a stack never crosses another river.
- **Which stack a repeated person joins.** A person entry joins the stack of the tradition that
  tells them, if that tradition is in view. Anyone else joins the earliest stack that names them.
- **A stack pushed below another one is headed by its tradition's name.** The tradition's own
  label may be hidden under the stack above, so the header and the dotted line both say whose
  people these are.
- **A voice is joined to a person entry by name and date.** A row's name joins an entry when it
  matches the entry's name, short name or informal name and the row's year falls within 30 years
  of the entry's dates. The date test keeps Ignatius of Antioch (107) apart from Ignatius of Loyola.
- **People told within no tradition** (Jovinian, Peter the Iberian) show in their river's Who for
  their era, at their own year.
- **Links that end at a person** are drawn from that person's home tradition, as #1585 drew them
  in its Traditions view. A link is not drawn where both ends fall in one tradition. It also is not
  drawn where the person has no tradition. The person's card lists every link that names them.
- **Pills show at reading zoom only.** On the whole-map view they would shrink to specks, so the
  river and profile pills appear with the tradition labels. The card's Who button works at any
  zoom. It brings the map in close enough to read the names.
- **A tradition that names no one has no profile pill.** Its card's Who button reads "Who · no one
  named" and is not active, and its Who section gives the plain reason (`peopleNote`).
- **Card data has a home.** Person entries take an optional `card` (knownFor, role, keyWorks,
  legacy {traces, remembered}, uncertain, sources {ownWords, about}). The census validator checks
  it. It is filled for the 10 pilot people, and nowhere else yet: for eight, from the final cards
  of data release 35 (`Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/final/`); for
  Bede and Grotius, from the reviewed pilot drafts (`drafts/`).
  `ownWords` is read from the Library's shelves by author. A work is marked disputed only where its
  Library row says so.

**Deferred (Mark, 2026-11-11).** P2-PL, likenesses: one profile icon until then. P2-S, search:
deferred for its own design pass.

**Applied.** Data release 36: the `card` field on the 10 pilot people, described in the census's
own notes. The map mirrors `people`, `peopleNote`, `toldWithin` and `card`.

**Supersedes.** "The people layer: what the rulings left open (P2-P)", the coordinator's calls on
#1585 (2026-11-10), were never merged. This entry replaces them. #1585 is closed in favor of the
new pull request.

---

## 2026-11-11 — Who and the connection lines are never shown together (P2-P)

**Decided (Mark, 2026-11-11, on his first look at the P2-P screenshots, relayed by the
coordinator).** Mark's words: "so when who is on then connections should be off".

- **Turning Who on hides the connection lines.** This applies to the card's Who button, a river's
  Who pill and a tradition's profile pill. A link that an open card would light stays hidden too,
  and so do the dotted "continued as" lines between rivers.
- **Clearing Who puts the lines back as they were.** If connections were off before, they stay
  off. The connection switches show the lines as off while Who is showing. The choice saved for
  the next visit is the one made before Who opened.
- **Turning a connection on while Who is showing clears Who.** This covers "All connections",
  "Major links" and any kind of link. The two are never shown together.

**Mark's look (2026-11-11), relayed by the coordinator.** Mark's words: "those are fine, merge it".
He also accepted the five build calls listed on the review page
(https://claude.ai/artifact/5uvUNq4maMRVJ8bQjPUT1D): a stack starts below the label when neither
side has room; a tradition that names no one has no profile pill; pills show at reading zoom only;
links that end at a person are drawn from the person's home tradition; people told within no
tradition appear in their river's Who.

---

## 2026-11-11 — Who a Who is: the record stands on its own (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words in the order he gave them).**
- "the record has to stand on their own, if not it can become a story, but not a who"
- "a who is someone who has a source of material they developed or was developed with them,
  origin, augustine, luther etc. a story might be somone like joan of arc, who followed, but never
  really entered into the shaping of the church"
- On "developed with them": "a, both count". A body of work counts when the person wrote it, and
  also when hearers or disciples recorded it, or a circle produced it jointly, where it carries the
  person's thought and is attributed to them.
- "lets add or a following to the body of work". A community or movement that formed around the
  person and carried what they shaped also counts.
- "a great starting point and we can look at exeptions or if we are leaving a catagory out"

So a Who is a person with a body of work: their own, recorded by their hearers or disciples,
produced with their circle, or carried by a following that formed around them. Someone who took
part in the church's story but did not shape it, as Joan of Arc did not, can be told as a story.
They are not a Who.

**What this replaces and reverses.**
- **Replaced:** the counting routes for a person mark in "People on the map (change order to
  rulings 14 and 15)" (2026-11-09). These were ruling 14's test, 10 or more works of one's own on a
  tradition's shelf, and repeated mentions in later traditions' own-voice texts. The standard above
  is now the test for a Who.
- **Reversed:** answer C of "The people list ruled" (2026-11-10), as it applies to hearers'
  records. Speech that hearers or disciples recorded and attributed to a person now counts.
- **Reversed:** the hold on founders in "The later-worlds people ruled (P2-G3b)" (2026-11-10),
  item A. A following that formed around a founder now counts toward their body of work.

**The interim (Mark: "a, merge with the 39").** Until every person has been sorted against the
standard, Who shows only the 39 person entries. This covers the map's stacks, its pills, the
person cards and "+N more", and the tree pages' People section.
- Named voices are not shown as people, but they stay in the census, because the sweep needs
  them.
- A tradition whose people include no person entry shows no Who pill, no Who button and no Who
  section. A tradition that names no one still shows its `peopleNote`, which stays true.
- The census notes say what Who shows.
- One switch lifts the display rule: `WHO_ENTRIES_ONLY`, in `cft-website/index.html` and
  `Build/tools/generate_tree_pages.mjs`.

**Next.** A read-only sweep, after Friday 2026-11-13, sorts every person into Who, story or
wanted. Mark sees the result (Open-Gaps, "The Who sweep", 2026-11-11). Until then, the named-voice
items in "What the people layer leaves open" (2026-11-11) wait on the sweep.

## 2026-11-11 — Person voice: Jon on Eleven v4, replacing David Baker

**Decided (Mark, relayed by the coordinator, 2026-11-11).** Mark's words: "yes this voice will
work for all people/who texts. lets rerun the 8 and replace the old voice with this and these
settings. use the earl church people first 8". On the settings: "defaults, nothing changed". On
the tone: "calm, wise, inviting, documentary biography tone. Not dramatic and not pushy."

Every person brief and every other "who" text is now recorded with:
- voice: Jon, "Warm, Grounded Storyteller", `MFZUKuGQUsGJPQjTS4wC`;
- model: `eleven_v4`, output `mp3_44100_128`;
- settings: `{"stability":0.85,"similarity_boost":0.88,"style":0.05,"use_speaker_boost":true,"speed":0.95}`,
  which are Jon's defaults;
- audio tags: `[calmly]` at the start and `[warmly]` before the last sentence. The tags go only
  into the text sent to ElevenLabs, never into the census text or a page.

The approved sample (206 credits, request `qXoJKGCES7Ib2BN0l5UC`) is at
https://claude.ai/artifact/EuNdBRSiL8sBwmxfTzHDFn. A person run of
`Build/tools/generate_tree_narration.mjs` (`--people`) takes these on the command:
- the voice: `--person-voice-id`;
- the model: `--model`;
- the output format: `--output-format`;
- the settings: `--voice-settings`;
- the tags: `--open-tag` and `--closing-tag`.

Each is printed before the first request, and none is read from the environment.

## 2026-11-11 — A common name is placed at its first mention

**Decided (Mark, 2026-11-11).** Mark's words: "if a name is common we need to clarify from where".
At its first mention in a text, a name that could mean more than one person gets a role, a place or
a time. Examples are "the church historian Socrates", "Theophilus of Alexandria" and "Palladius of
Helenopolis". The brief and the person card are separate texts, and each gets its own first
mention. The identifier must come from the vendored sources, and no new claim may come with it.

## 2026-11-11 — A short intro for each person, beside the full brief (Mark: "a")

**Decided (Mark, 2026-11-11).** Each person gets a new intro of about 25 seconds, beside the full
brief. The full brief stays as it is. The intros come later, and none was made in the Jon run below.

## 2026-11-11 — Cap ruling: the common-name edits to the eight early-church briefs

**Cap ruling (2026-11-11).** The common-name standard is a change Mark ordered to reviewed text,
not a fourth revision round. Its edits to the eight briefs and their cards had one targeted Opus
recheck, covering the changed sentences only:
`Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/reviews/R5_common-names_recheck.md`.
It found nothing blocking. Its eight standard fixes were applied as written. The drafter's change
list is in that pilot's `names-2026-11-11/CHANGES.md`.

## 2026-11-11 — Data release 37: the eight early-church people in Jon's voice

**Done.** The eight early-church briefs and person cards now place every common name at its first
mention, in data release 37. All eight are recorded again in Jon's voice, and those recordings
replace the David Baker clips and their manifest entries.

| Person | Words | Recorded |
|---|---|---|
| Origen | 382 | 2:21 |
| John Chrysostom | 373 | 2:23 |
| Gregory of Nyssa | 348 | 2:03 |
| Athanasius of Alexandria | 332 | 2:08 |
| Constantine the Great | 318 | 1:55 |
| Gregory of Nazianzus | 311 | 1:53 |
| Ephrem the Syrian | 274 | 1:38 |
| Methodius of Olympus | 224 | 1:26 |

**Run "CFT early-church people 8, Jon v4, 2026-11-11".**
- Characters: 14,629 of brief text, 14,773 sent with the tags, under the 15,000 cap.
- Credits: 7,162 by the `character-cost` headers.
- Reconciled by request id against `GET /v1/history`: all 8 ids appear once each (source TTS,
  `eleven_v4`, `mp3_44100_128`), for 7,162 credits, with no duplicate. For `eleven_v4` the history
  records only stability and leaves the voice and text empty, as it did for the approved sample.
  The full settings sent are in the run's printed log.
- Balance: 230,027 used before and 237,189 after. No other request was billed in the run window.
- Log: `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/recording/jon-v4-early-people-8.log`.

**Other use of the key the same afternoon (for Mark).** Four `eleven_v4` history items came from
ElevenLabs' web app, source "Flows":
- 15:49 UTC, 416 credits;
- 15:55, 435;
- 15:55, 435;
- 15:56, 390.

Another 1,728 credits were charged between 226,417 and 229,821 with no history item at all. None
of these came from this build.

## 2026-11-11 — The era 1 Who scan: four categories, the story test, two witnesses (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The read-only
scan of era 1 sorted every candidate under "Who a Who is: the record stands on its own"
(2026-11-11). It was tuned in five steps:
- The story test: "there still has to be enough to tell the story, not just theological argument".
  A writer whose record is only doctrine is not a Who.
- A fourth category: "not everyone has to be a story, only those that are compelling testemonies.
  they can just be listed in the source conversation". So there are four categories:
  - **WHO:** shaped the church, left a body of work or a following, and the record carries enough
    life to tell a story.
  - **STORY:** only a compelling testimony, a life or witness worth telling in its own right.
  - **LISTED:** named in their tradition's sources conversation, with no profile and no story.
  - **WANTED:** would be a Who if the Library held one named source. The source is named.
- Founders known only through enemies: "Two witnesses". Such a founder is a Who only when at least
  two independent opponents agree on the outline of their life, and the brief marks polemic as
  polemic and names whose it is. Otherwise WANTED, naming the own-tradition source, or LISTED.
  Epiphanius drawing on Irenaeus is one witness, not two.
- Perpetua: "Story". A first-person testimony is a STORY; WHO is for those who shaped the church.
- Methodius of Olympus: first "Keep for now", then "Keep as Who", as a named exception. His live
  brief tells a story, and he shaped the debate over Origen. It is not a rule change.

**The calls on the judgment cases (Mark).**
- Valentinus: "Who".
- Paul of Samosata: "Wanted". The council's letter and Epiphanius are not independent; Loofs 1924
  is wanted.
- Alexander of Jerusalem, Cornelius of Rome, Lucian of Antioch and Gregory Thaumaturgus become
  STORY. Lucian's details are tagged Contested. Gregory's story names Gregory of Nyssa's Life as a
  later, legendary source.
- The coordinator's routine call, which Mark can overrule: a WANTED source must be able to carry a
  life, not only writing.

**Outcome of the era 1 sweep.** 76 people: WHO 25, STORY 8, LISTED 39, WANTED 4. The WANTED rows
are Melito of Sardis, Ptolemy the Valentinian, Paul of Samosata and Mani. Marcion and Valentinus
pass the two-witness test; Mani fails it and Callistus is LISTED. An Opus check read the cited
passages for every WHO, STORY and WANTED row: 14 rows were corrected and none was unsupported.
The coordinator's expected figure of LISTED 40 did not add up (25 + 8 + 40 + 4 = 77); the rows give
39. The full table and the check's notes: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era1/`.

**What this does not change.** No census, record or site change is made by this sweep. The display
rule (Who shows only the 39 person entries) lifts on Mark's call after the other eras are sorted.
Approved to proceed (Mark, 2026-11-11).

## 2026-11-11 — The era 2 Who scan, and the standing OUTSIDE WITNESS label (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The read-only
scan of era 2 (312–451 CE) used the era 1 standard. Mark ruled on the cases it raised:
- **Recorders are Whos.** On Palladius of Helenopolis: "he needs to be a who"; then "we need
  Palladius as a who as a biographer and other things, we need to include people like him as
  who's". A biographer, church historian or recorder whose work became a main source for how the
  church knows its people and past is WHO on that body of work. Where the recorder's own life is
  too thin to tell, the row stays WHO as a judgment call. So Palladius, Possidius, Sulpicius
  Severus, Paulinus of Milan, Epiphanius, Socrates, Sozomen, Philostorgius, Koriun, Eghishe,
  Auxentius of Durostorum, Theodoret and Rufinus are WHO, and Pontius the Deacon (era 1) is
  rescored WHO.
- **Women.** "women who have 1 source and that source is a who, then that qualifies". Of the
  readings offered, Mark chose "Who if she shaped": WHO if she founded, taught or led; STORY
  otherwise. Macrina, Paula, Marcella, Fabiola, Olympias and Melania the Elder are WHO; Monica is
  STORY; Amma Sarah is LISTED (her sayings come from anonymous collections).
- **Emperors:** "By the standard". Constantine is WHO as a named exception, Theodosius I is
  STORY, and the rest are sorted by the standard (Constantius II, Julian, Pulcheria, Justina:
  LISTED).
- **Founders known through a disciple's or biographer's record:** "Who". The record counts as
  developed with them, and the brief marks it as hagiography.
- **Founders with their own words and a following:** "Own words + following". The two-witness test
  stays for founders with no words of their own (Melitius, Donatus).
- **Jovinian:** "Take it down". He is LISTED; his live profile comes down in a later release.
- **Councils:** "counsels are treated like a tradition with a different icon and title. but
  people who are a part of it should be on the who click". Councils are not people and carry no
  verdict; the scan lists each council with its participants.

**The standing OUTSIDE WITNESS label (all eras).** Mark's lines, in order:
1. "they are who but clearly mentioned as outside witnesses" (Josephus and Tacitus).
2. "this should be all that are significant witnesses outside the church through the eras".
3. "these are historians, not doctrine or athiests or others fighting the church, just objective
   historians".
OUTSIDE WITNESS is a standing WHO label for historians outside the church who report on it. Its
profile says who the writer was, exactly what they say, and how far it can be trusted (for
Josephus, which lines of the Testimonium scholars think were added). Josephus and Tacitus are
WHO. Suetonius and Ammianus Marcellinus are WHO under it (the coordinator's reading of the second
and third lines). Polemicists do not qualify; Celsus, Porphyry, Lucian of Samosata, Julian and
Libanius are LISTED by the standard. Pliny the Younger, a governor's report and not a historian's
work, is an open judgment call. Future era scans apply the label. The three era 1 rows
(Josephus, Tacitus, Suetonius), Pliny, the three LISTED polemicists and Pontius the Deacon are
added to the era 1 record as an addendum; the era 1 counts are unchanged.

**Outcome of the era 2 sweep.** 107 people: WHO 57, STORY 8, LISTED 48, WANTED 2. Judgment-call
rows: 54. The WANTED rows are Gregory the Illuminator (Agathangelos) and Ezana of Aksum (his
inscriptions). Four Opus checks read the cited passages: 51 first-pass rows (35 confirmed, 15
corrected, 1 not supported: Mesrop, whose source, Koriun's Life, is held), 21 new or changed rows
(9 corrected), the outside-witness rows and the 12 councils (8 corrected). The full table and the
checks: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/`.

**What this does not change.** No census, record or site change is made by this scan. Jovinian's
profile comes down in a later release. Councils stay out of the census until a change order on
frozen eras makes them an entry kind. The display rule (Who shows only the person entries) lifts
on Mark's call after the other eras are sorted. Approved to proceed (Mark, 2026-11-11).
## 2026-11-11 — The Who profile pattern (Mark, 2026-11-11)

**Decided (Mark, relayed by the coordinator; his words as given).** One pattern governs every Who
profile, story and listed line: `Who_Profile_Pattern.md` in this folder. Approved to proceed (Mark,
2026-11-11).
- **Writing standard, by reference.** "we use the same principles we used to develop the tradition
  cards, simple modern english with the accessability and no ai tells etc. it is a full design i
  dont want to repeat, no tails, no statements that have no context or meaning no xy no wise saying
  etc. find the quality and follow it". The pattern cites `CLAUDE.md`, the Writing Standard, the
  NorthStar target and the Voice and Style Guide (1.1 to 1.12) and does not restate them.
- **No intro.** "why are we bringing an introduction in we have the brief defined and a story goes
  into the story". This reverses "A short intro for each person, beside the full brief (Mark: 'a')"
  (2026-11-11). The earlier entry came from a misreading of a pasted voice spec. Person audio is the
  brief only. The Jon tags, `[calmly]` at the start and `[warmly]` before the closing line, apply to
  the brief and stay in the audio script.
- **Length.** "we moved the who to 1 to 2 minutes with streatch for major people". This replaces
  the 60 to 120 seconds of "Person briefs" (2026-11-11). No bands and no numeric ceiling beyond it.
- **Opening and disputes.** Scene first. A contested point is told where it arises ("Dispute in
  place"), not at the close.
- **Hostile-witness founders.** "teaching two, life one": two independent witnesses for the teaching,
  and the life outline may rest on one if the brief says so. This refines the era 1 scan ruling
  ("at least two independent opponents agree on the outline of their life").
- **The categories stack.** "for whos, they are still in the record or lists." Every named person
  keeps their list line; a Who or a story is added on top.
- **Outside witness.** A label on a Who profile for a historian outside the church (Josephus,
  Tacitus): "these are historians, not doctrine or athiests or others fighting the church, just
  objective historians".
- **Councils.** "counsels are treated like a tradition with a different icon and title. but people
  who are a part of it should be on the who click", and "it is one who listed in two places (counsil
  and the tradition)". One profile, never a second copy.
- **Common names.** "dont forget the newer ones like name full or place of common names like we did
  for socratise", refined to "socrates from constantinopel". The form is name of place ("Socrates of
  Constantinople"), with a role or time only where a place does not identify the person. This
  refines "A common name is placed at its first mention" (2026-11-11), whose example "the church
  historian Socrates" it replaces.

**Resolved by the standard (the coordinator, 2026-11-11).** Old quotes: short plain ones only,
otherwise told in modern words naming the source. Confidence on the card: plain sentences, no
labels. Other name forms: the census `informalName`, and an original-language form only where a
vendored source spells it. Namesake ids: add the place when names collide; an existing id is never
renamed, because ids name the tree pages and the audio files.

**Opus check (2026-11-11).** One Opus read checked the pattern against the standard and the eight
live briefs and cards. Its fixes to the pattern are applied. Its findings in the eight are
registered in Open-Gaps ("Pattern findings in the eight live person texts", 2026-11-11). Nothing
live was changed: that is a change order.


## 2026-11-11 — The era 3 Who scan: rulers, carry to era 4, recorders without the label (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The read-only scan
of era 3 (451–622 CE) used the era 1 and 2 standard. Mark ruled on the cases it raised:
- **Rulers:** "Story unless own voice". Official texts alone (edicts, chancery letters) make a
  STORY; an own corpus or a personal confession makes a WHO. Justinian (his Novels) and Reccared
  (his own confession at Toledo III) are WHO. Anastasius I, Heraclius, Theodoric, Huneric, Clovis
  and Geiseric are STORY.
- **People named in era 3 entries who fall after 622:** "Carry to era 4". Thirteen provisional
  rows (Muirchu, Adomnán, Jonas of Bobbio, Aidan, Colmán, Cogitosus, Braulio, Ildefonsus, John of
  Nikiu, Maximus the Confessor, Sophronius of Jerusalem, Antony of Choziba, al-Baladhuri) are
  scored in the era 4 scan and are not counted in era 3.
- **Marcellinus Comes:** "Recorder, no label". WHO as a recorder. The OUTSIDE WITNESS label stays
  on Procopius and Agathias (and al-Baladhuri, carried to era 4).
- **Theodora:** "Who".

**Coordinator's calls under settled rules (not Mark's words; Mark may overrule).** Barsanuphius and
John of Gaza are two WHO rows, as the census draws them; the brief notes that the held answers are
not labelled by speaker. Moses of Khoren is WHO as a recorder, with his date tagged Contested.

**Outcome of the era 3 sweep.** 104 people: WHO 65, STORY 19, LISTED 12, WANTED 8, plus 13 rows
carried to era 4. Judgment-call rows: 67. Justinian is WHO: his Novels are held (Novel 131
included); the 553 acts are held only as extracts in `npnf214`; his edicts against the Three
Chapters are not held as text; Procopius's Buildings, Secret History and Wars are held. All five
live person entries (Simeon of Beth Arsham, Peter the Iberian, Gregory the Great, Patrick,
Justinian) are WHO, so no live profile is at risk. The WANTED rows are Iakob Tsurtaveli, Vachagan
III, Movses Daskhurantsi, Sabas, John Malalas, Theophylact Simocatta, al-Tabari and Ibn Ishaq.
Opus checks read the cited passages: 116 first-pass rows (98 confirmed, 18 corrected, none not
supported; George of Choziba, Theodoric and Huneric moved to STORY), the 33 draft councils (4
corrected), and the one row changed by Mark's answers. Thirty-one councils are listed with their
participants. The full table and the checks:
`Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay
out of the census until the change order named in the era 2 entry.

## 2026-11-11 — Map Who: how many names, which names, and where they sit (Mark, 2026-11-11)

**Decided (Mark, relayed by the coordinator; his words as given).** A design ruling on the map's
Who view, which changes the caps in "The people layer: Who beside every tradition and river (P2-P)"
(2026-11-11).
- **Names shown.** "i think 1 - 4 names on the voice click per tradition, 1 to 5 names on a river
  per era. then click for more for each (more click)", and "pick by major name, order by date".
  The map's Who shows up to 4 names per tradition and up to 5 per river per era. They are chosen
  from that place's major Whos and shown in date order. A "more" click shows everyone, in date
  order.
- **A major mark.** Each Who carries a "major" mark, proposed at writing time and confirmed by Mark
  in each batch. The era scans propose it in a "Major?" column.
- **Where "more" sits and where names sit.** "the more should appear under the names for a
  tradition and next to the who button on the river, the names show up around the dates they were a
  part on the river". For a tradition, "more" sits under its names. For a river, "more" sits next
  to the river's Who button. On a river each name sits at the point matching the dates the person
  was active.
- **Which side of the river.** "to the right of the river". River names sit to the right of the
  river, at their dates.
- **Fading.** "and everything else fades so it is clear if it runs over". While a Who is open,
  everything else on the map fades back, so the names stay readable where they run over other
  rivers or labels.

**What this changes.** The build caps of 6 names for a tradition and 4 for a river in an era become
4 and 5. The live build moves a stack to the river's left when the right side is tight; the build
slice resolves that against this ruling, with the fade as the likely answer, and brings Mark any
case where the right side has no room. This is map and data work for a later build slice (Open-Gaps
217). No map or data change is made here.

## 2026-11-11 — Recordings held back by the name-clarity pass stay as they are for about two months (Mark, 2026-11-11)

**Decided (Mark, relayed by the coordinator; his words as given).** "ok put these on hold for a
couple of months until we have more credits, this is not a major concern".
- Every recorded text held back by the name-clarity pass (PR #1597, release 38) stays as it is,
  text and audio, for about two months. The list is
  `Build/Ministry/Operations/Audits/Name_Clarity_Pass_Held_Back_2026-11-11.md`. It covers the 8
  Jon person briefs and the 69 tradition and story recordings.
- The text of those fields is not edited until then.
- They are re-recorded together in one approved, capped run when credits allow (Open-Gaps 218).

## 2026-11-11 — The era 4 Who scan: Wanted, Story, Listed for now (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The read-only scan
of era 4 (622–1054 CE) used the standard of eras 1 to 3, with Mark's pairing ruling ("if two people
are tied together in their sources with similar identity its ok to make that a single who") and
the "Major?" proposal column. Mark ruled on the cases it raised:
- **John of Damascus:** "Wanted". The Library holds his Exposition but no life; the Life by John of
  Jerusalem is wanted. The row moves from WHO to WANTED.
- **Charlemagne:** "Story". His held texts are capitularies and official letters.
- **Vladimir and Olga of Kyiv:** "Listed for now". Both rest on Mouravieff's retelling and the Kyiv
  Synopsis; rescore both when the Primary Chronicle is held (Open-Gaps 216).
- **Heraclius (live person entry):** "Story, keep live". He is recorded STORY; his live profile
  stays until stories are built, then moves over (Open-Gaps 216).

**Coordinator's calls under settled rules (not Mark's words; Mark may overrule).**
- Pairs: seven paired rows (Cyril and Methodius, Antony and Theodosius of the Caves, Boris and
  Gleb, Flora and Maria, Benedict Biscop and Ceolfrid, John the Iberian and John Tornike, Mar Sapir
  Iso and Mar Proth); Karbeas and Chrysocheir, Muirchu and Tirechan, Eulogius and Alvarus, Berno and
  Odo, Grigol Khandzteli and Giorgi Merchule stay two rows each.
- The Coptic patriarchs found in the History of the Patriarchs (Agatho, John III, Simon I,
  Alexander II, Michael I, Isaac, Yusab) are all WHO, Major "no".
- Dhuoda is WHO under the women's rule (she taught). Alopen is WHO, with the thin life flagged.
- One supplement scan after all eras covers shapers the Library holds that no census text names.
- Adam of Bremen and Nestor the chronicler go to the era 5 scan.

**Era 3 addendum.** Mark's pairing ruling arrived after the era 3 scan merged. Barsanuphius and John
of Gaza are now one paired WHO row, and Mennas (Benjamin I's brother), al-Tabari and Ibn Ishaq moved
to era 4 by date. Era 3 is now 100 people: WHO 64, STORY 18, LISTED 12, WANTED 6; judgment-call
rows 64 (Open-Gaps 215).

**Outcome of the era 4 sweep.** 157 rows (a paired row counts once): WHO 46, STORY 9, LISTED 59,
WANTED 43. Judgment-call rows: 86. Bede is WHO; Heraclius is STORY. Two rows (Adam of Bremen,
Nestor) are carried to era 5. Thirty-five councils are listed with their participants. An Opus
check read the cited passages for 105 WHO, STORY and WANTED rows (75 confirmed, 30 corrected, none
not supported; one row, Braulio, carried another bishop's life from two OCR columns run together),
21 LISTED rows (15 right), and the 35 councils (7 corrected). A targeted recheck read the rows
changed by Mark's answers. The full table and the checks:
`Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay
out of the census until the change order named in the era 2 entry. Approved to proceed (Mark,
2026-11-11).

## 2026-11-11 — The era 5 Who scan: Innocent III Wanted, Henry IV Who, three Georgian stories (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The read-only
scan of era 5 (1054–1300 CE) used the standard of eras 1 to 4, with Mark's pairing ruling and the
"Major?" proposal column. Mark ruled on the cases it raised:
- **Innocent III (live person entry):** "Wanted, keep live". The Library holds his letters and
  Lateran IV extracts but no life of him. His live profile stays until the Gesta Innocentii III is
  held, then he is rescored (Open-Gaps 219).
- **Henry IV:** "Who". His own first-person letters tell his fall, which is the personal-confession
  branch of the ruler rule.
- **David IV, Tamar and Rusudan of Georgia:** "All three stories". All three rows are STORY.
- **Library timing:** "After all scans". The Library thread gets one combined WANTED list after
  eras 6 to 10 are scanned, ordered by era with major figures first (Open-Gaps 220).

**Coordinator's calls under settled rules (not Mark's words; Mark may overrule).**
- Sava of Serbia is WANTED (Domentijan's Life). Brother Leo is WANTED (Scripta Leonis; the
  Library's own header calls the Speculum Perfectionis attribution contested).
- Dionysius bar Salibi, Mari ibn Sulayman and Abu Salih are all WHO, flagged.
- The Muslim and Jewish historians that would fit as OUTSIDE WITNESS (Ibn al-Athir, Usama ibn
  Munqidh, Ibn Jubayr, Rashid al-Din, Benjamin of Tudela) are named in no era 5 census text and none
  is held. They go in Open-Gaps as wanted sources, with no rows. Anna Komnene is WANTED (OUTSIDE
  WITNESS) on the Procopius precedent.
- Pairs: Yahballaha III and Rabban Sauma, Rufino and Angelo, Domentijan and Teodosije, and the
  awlad al-Assal are one row each. Alberic and Stephen Harding are split into two rows.
- Humbert of Romans is WANTED as a recorder, to match Gerard de Frachet. Recorders whose named
  source carries the order's own story stay WANTED (Rimbert and Anskar precedent).
- By date of work, Symeon the New Theologian, Yahya ibn Said and John of Rila go to an era 4
  supplement. Bernard Gui, Eckhart, Tauler, Suso, Angelo Clareno, Belibaste, Jacques de Molay, John
  of Brunn and Guiard of Cressonessart go to the era 6 scan. Marguerite Porete stays in era 5.

**Outcome of the era 5 sweep.** 101 rows (a paired row counts once): WHO 14, STORY 9, LISTED 35,
WANTED 43. Judgment-call rows: 62. Gregory VII and Bonaventure are WHO; Innocent III is WANTED and
flagged. Fourteen councils are listed with their participants. An Opus check read the cited passages
for 67 WHO, STORY and WANTED rows (49 confirmed, 18 corrected, none not supported, no invented
person-detail), 18 LISTED rows (13 right) and the draft councils (6 confirmed, 9 corrected). A
targeted recheck read the 12 rows changed afterwards (3 confirmed, 9 corrected, none not supported).
The Library holds no work by a Muslim, Jewish or Western secular chronicler of 1054–1300. The full
table and the checks: `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era5/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay
out of the census until the change order named in the era 2 entry. Approved to proceed (Mark,
2026-11-11).

## 2026-11-11 — Events get their own entry when their impact reaches the river level (Mark, 2026-11-11)

**Decided (Mark, 2026-11-11, relayed by the coordinator; his words as given).** The test for an
event's own entry, with its own icon and title as councils have, is reach:
- **The test:** "i think the test is it impacts beyond a tradition, it impacts at a river level".
- **What counts:** "so what are we talking about, counsils obviosly, but even the westminister
  confession impacted multiple denominations in a river".
- **The event is the process:** "its not the actual confession but the process/meetings that
  developed it im talking about".
- **Failure still counts:** "yes, even if there was no resolution like the great schism".

**What this means (the coordinator's reading).**
- An event gets its own entry when its impact reaches the river level, beyond any one tradition.
  Councils are one kind of event. Others: schisms, unions, edicts, persecutions across churches,
  conquests and falls, meetings between traditions, Bible translations, revivals and ecumenical
  events. This replaces the earlier plan to show councils as stories under Shared Events.
- For confessions and creeds, the event is the gathering or process that produced the document,
  not the document: the Westminster Assembly (1643–1653), the Diet of Augsburg (1530), the Synod of
  Dort (1618–19), the drafting of the Heidelberg Catechism (1563). The document is told on the
  event's card and listed among its sources, and the participants go on the event's Who click, as
  with a council.
- An event qualifies when the process ended without a resolution (the break of 1054, the Great
  Western Schism, failed reunion talks). The test is impact at the river level, not how the event
  ended.
- Building events on the map is the same later slice as councils (Open-Gaps 217 and the councils
  entry).
- The events themselves are being found by a separate scan of major events across all ten eras,
  which Mark asked for on 2026-11-11. That scan does not write this entry.

## 2026-11-12 — The era 6 Who scan: friars under the Latin papal church, two Greek chroniclers labelled (Mark, 2026-11-12)

**Decided (Mark, 2026-11-12, picked from options, relayed by the coordinator).** The read-only scan
of era 6 (1300–1517 CE) used the standard of eras 1 to 5, with Mark's pairing ruling and the
"Major?" proposal column. Mark ruled on the cases it raised:
- **Friars in Asia:** Montecorvino, Jordanus and Marignolli go under the Latin papal church,
  cross-linked from the Church of the East and St Thomas entries.
- **Outside-witness label:** Sphrantzes and Chalkokondyles are labelled. Doukas is a plain
  recorder, because he is partisan.
- **Hostile writers:** Gui is WHO as a recorder, with his polemic marked as polemic. Walsingham and
  Knighton are LISTED until their introductions are read for a life.
- **Jakoubek of Stříbro:** WANTED, naming his tracts.
- **Gost Radin:** WHO, flagged, with the old Patarene frame marked as the old reading.

**Coordinator's calls under settled rules (not Mark's words; Mark may overrule).**
- Hilton, Love, Merswin, the Cloud author, the Theologia Deutsch author and Mirk are LISTED, on the
  story test.
- Margery Kempe is WANTED, naming the Book. Savonarola and Colette are WHO (Colette under the
  women rule); Capistrano is WANTED. Kantakouzenos is WHO. Barlaam and Akindynos get two rows.
  Ruusbroec gets one shared row, home in Devotio Moderna. Gerson and Marsilius are WHO, noted so
  the supplement scan skips them. Zara Yaqob is WANTED, for the Mashafa Berhan. Tekle Haymanot
  stays in era 6, flagged.
- Made by the scan: Richental is a recorder with no outside-witness label; Olivi and Ban Kulin go
  to the era 5 supplement by date of work; Rashid al-Din, Ibn Battuta, Ibn Khaldun, Abu'l-Fida and
  al-Qalqashandi get no rows and go in Open-Gaps as wanted sources (the era 5 call); al-Umari and
  al-Maqrizi, held in their own text, are WHO (OUTSIDE WITNESS); Doukas, Sphrantzes and
  Chalkokondyles are era 6 by date of work, and the era 5 file's line sending them to era 7 is
  corrected.

**Outcome of the era 6 sweep.** 162 rows (a paired row counts once): WHO 69, STORY 21, LISTED 58,
WANTED 14. Judgment-call rows: 43. Both live person entries, Wyclif and Kempis, are WHO, so none is
flagged. Thirty-three councils are listed. An Opus check read the cited passages for 103 WHO, STORY
and WANTED rows (74 confirmed, 29 corrected, none not supported, no invented person-detail) and 36
LISTED rows (23 confirmed, 8 corrected, 5 not supported as LISTED, all five rescored). The Library
holds no Jewish chronicler of 1300–1517. The full table and the checks:
`Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay
out of the census until the change order named in the era 2 entry. Approved to proceed (Mark,
2026-11-12).

## 2026-11-12 — Councils: one word for every gathering, and the major councils (Mark, 2026-11-12)

**Decided (Mark, 2026-11-12, in the scan thread; his words as given).** The scan of major events
across the ten eras was narrowed to gatherings, and the full list of councils and synods was added:
- **All councils and synods:** "i do want all the councils and synods".
- **The test:** "they need to be river level, mutliple traditions comming together or impacting
  multiple traditions".
- **What counts:** "if there was a gathering or attempt to come together to make a decision, seeking
  god together that is what im talking about". Some items "are or should be in the story catagory,
  and maybe we will do a historical events that shaped christianity".
- **Summits count:** "so we need to include major summits as part of the event catagory".
- **Sources, not rulings:** "dont use my rulings use the sources and reliable history to determine".
- **The Great Schism of 1054:** "keep it in the stories". The legates' own account (Mirbt nos.
  227-228) says the patriarch refused to meet them or to hold a council, so it was not a gathering.
- **Review:** "yes do a review and a duplication check on everything" (relayed by the coordinator).

**Decided (Mark, 2026-11-12, picked from options, relayed by the coordinator).**
- **One word, councils:** "Use one word for all 182 gatherings. The about 46 that reached a whole
  river are "major councils", with their own map entry and icon. The rest show on their tradition.
  Summits like Lausanne count as councils in this sense." Events and councils are the same thing
  under two names once events are narrowed to gatherings. This renames the "events" category of the
  2026-11-11 entry "Events get their own entry when their impact reaches the river level" and
  replaces it. The river-level test of that entry stands. Persecutions, conquests, edicts, revivals,
  Bible translations, conversions and schisms that were not meetings are stories, not councils.
- **Quinisext and Dvin:** the Quinisext Council (691/692) and the Council of Dvin (c. 607-609) are
  major councils. Both pass the test: Rome refused to sign the Quinisext canons, and Dvin split the
  Armenian and Georgian churches.

**Outcome.** 46 major councils (per era 1 to 10: 1, 8, 3, 6, 3, 2, 12, 2, 3, 6); a list of 182
councils (HELD 72, PARTLY 64, WANTED 46); 49 items held for the story and historical-events
categories. Four Opus checks and a script reviewed every row, and Opus checked the two promoted rows.
Keswick (a devotional convention that decided nothing) and Westphalia (a congress of states) are on
the story list. Full table: `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/`.

**Coordinator's calls under Mark's full-auto instruction of 2026-11-12 (not Mark's words; Mark may
overrule).** Poissy 1561, the Conference of Carthage 411, Chanforan 1532 and Polotsk 1839 are major
councils, each a gathering that tried to decide something across several traditions with a held
record. Cross-church links for Lausanne, the World Council of Churches, Barmen and the 1872 Bulgarian
council, and map entries for the Councils of Rome and Carthage 251, Arles 314, Clermont, Marburg and
the 1555 Diet, are map-build work (Open-Gaps 217 and 222), not census changes now.

**What this does not change.** No census, record or site change is made by this scan. Approved to
proceed (Mark's rulings of 2026-11-12, relayed by the coordinator, under his full-auto instruction).

## 2026-11-12 — The era 7 Who scan: Melanchthon Who, the WANTED rows re-sorted (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).** The read-only scan of era 7 (1517–1650 CE) used the standard of eras 1 to 6. Four questions went to the coordinator, none a major decision:
- **Melanchthon:** WHO, flagged thin life, Major yes, not WANTED. The Library holds his own Augsburg Confession and Apology and about 80 texts that name him. The coordinator then ordered the other "doctrine only" WANTED rows re-sorted by the same standard: where a person's own held work, plus a following or held witnesses, carries a tellable life, the row is WHO; for women, one held source that shows her shaping the church makes her WHO. Camerarius's Life stays a wanted source.
- **Philip Neri:** WHO, with the hagiography marked as hagiography (Bacci's Life of 1622).
- **Ivan IV and John Winthrop:** WHO under the own-voice rule; Ivan's polemic marked as polemic.
- **Ferenc Dávid:** the two-witness rule for the teaching. WHO: the Torda 1568 diet record, and his opponent Socinus's disputation with him.
- **Jean Ingoro and Jean Tingoro:** the check could not settle it; two rows, cross-referenced, identity Inferential-Thin.

**Calls made by the scan under settled rules.** Pairs as one row (Grebel and Manz, Ursinus and Olevianus, Melville and Melvill, Field and Wilcox, the Mornays, Ricci and Trigault, Lopes and Pigafetta, Naito and Oumemidono, Houghton with the Carthusians of 1535 as one STORY group); Western envoys and travellers carry no OUTSIDE WITNESS label (Herberstein is a Catholic imperial envoy, inside Christianity); hostile inside writers are tradition-relative (Recusant founders WHO as their tradition's voices; Sarpi WHO as a hostile inside recorder); popes STORY; works after 1650 go to era 8 by date of work; Dutch Further Reformation has no WHO yet. On re-sorting, Robert de Nobili became WHO flagged witness-only (two independent held witnesses, no text of his own), which extends the two-witness rule to a founder with no held text; the coordinator may overrule it.

**Outcome of the era 7 sweep.** 259 rows (a paired row counts once): WHO 115, STORY 48, LISTED 87, WANTED 9. All five live person entries (Luther, Calvin, Tyndale, Ignatius, Grotius) are WHO, so none is flagged. The Library holds no Ottoman, Jewish or humanist historian of 1517–1650, so no row carries the OUTSIDE WITNESS label. An Opus check read the cited passages for 182 WHO, STORY and WANTED rows (144 confirmed, 35 corrected, 3 not supported, no invented person-detail) and 39 LISTED rows (33 stand, 6 corrected); a second Opus recheck covered the rows the answers changed. Twenty-one first-pass rows were moved to era 8 by date of work and handed to the era 8 scan. The full table and the checks: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era7/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay out of the census until the change order named in the era 2 entry; gatherings found are listed as leads for the councils list. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12).

## 2026-11-12 — The era 9 Who scan: Laestadius and Rosenius Who, Spiritualism held for Mark (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).** The read-only scan of era 9 (1815–1906 CE) used the standard of eras 1 to 7. Five questions went to the coordinator:
- **Laestadius and Rosenius:** WHO, thin life flagged. An in-era life told from inside their own church (Cornelius, 1886) meets the Dallet standard. Waldenström stays WANTED.
- **Montero y Vidal and Pelesz:** LISTED (the Gui and Walsingham precedent): hostile recorders with no life to tell.
- **Pobedonostsev STORY, Ryaboshapka and Ratushny LISTED** on the same book (Conybeare): kept as they are.
- **Spiritualism / New Thought:** the 6 rows (10 people) stay WANTED and provisional. Whether a movement listed as "Outside Article 4 Scope" belongs on the tree at all is held for Mark.
- **Source pass:** all WANTED sources are registered in Open-Gaps only, major first, and nothing is queued. The Library gets one combined WANTED list after all scans (Open-Gaps 220).
- **Boundary people:** Carey, Allen (1816), Hormizd, Marsden, Sheptytsky, Hoyek and Underwood stay in era 9. The era 8 worker has the list of names sent to its desk and the list kept here.

**Calls made by the scan under settled rules.** The Melanchthon rule (era 7) moved Carey, Channing, Filaret (Drozdov) and Holly from WANTED to WHO, thin life flagged. The Opus check found a full life of Leonid of Optina held (OPT1 285-372): WHO. The era 2 recorder ruling moved Dallet, Marnas, Badger, Whitehouse and Edavalikel Philipos to WHO. Pobedonostsev and Nikolai Kasatkin had two worker rows each; one is kept. Popes are STORY. Kolodziejczyk is era 10. Mackenzie carries no OUTSIDE WITNESS label.

**Outcome of the era 9 sweep.** 255 rows (a paired row counts once): WHO 34, STORY 11, LISTED 49, WANTED 161. Judgment-call rows: 128. Era 9 has no live person entries. No row carries the OUTSIDE WITNESS label: no secular, Jewish, Muslim, Asian or African historian of these churches is held for the period. The Library holds almost nothing of 1815–1906, so most named shapers are WANTED. An Opus check read the cited passages for 33 WHO and STORY rows (21 confirmed, 12 corrected, none not supported, no invented person-detail), absence for 168 WANTED rows (157 confirmed, 7 corrected, 1 not supported) and 24 LISTED rows (16 stand). The full table and the checks: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era9/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay out of the census until the change order named in the era 2 entry; gatherings found are listed as leads. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12).

## 2026-11-12 — The era 10 Who scan: deaths in 1990 or later held, Surma Khanim WANTED (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).** The read-only scan of era 10 (1906 to c. 2010) used the standard of eras 1 to 9. Mark has not ruled on living people, so the hold was set by the coordinator in two steps:
- **Reading of the living-people hold.** The hold is for people who are alive or whose status is unknown. Anyone whose death the census states is scored, flagged in the Dates cell. Anyone certainly dead by common knowledge who died before 1990 is scored and tagged "death not in a held source (Widely Accepted)". Anyone alive, of unknown status, or dead in 1990 or later is held for Mark.
- **Deaths in 1990 or later are held whatever the source:** Ford (2019), Lefebvre (1991), Schutz (2005) and Antonios of Eritrea (2022) moved from WANTED to the held list. Recent deaths sit too close to Mark's coming rule.
- **Wigram's 1953 death** is accepted from the Library header.
- **The Birmingham girls and William Jennings Bryan** stay WANTED.
- **Surma Khanim:** the women rule applied exactly. The held line (WIGA 10058-10060) names her the best head of the patriarchal house but shows no leading or representing; she is WANTED (not LISTED), her own 1920 book the wanted source.
- **Four entries with no named person** (Anglican Communion, Church Struggle against Apartheid, Protestantism in Latin America, Ecumenical Movement and WCC) show an empty Who view for now.
- **Kostelnyk** stays WANTED, the collaboration marked and his motives Contested.
- **Modern scholars** who write about the churches are not scored; **the 1904–05 Welsh and Korean figures** (Roberts, "Awstin", Stead, Sŏ Sang-yun) stay in era 9; **Tyrrell and Loisy** stay in era 10; **Sheptytsky** stays in era 9.

**Calls made by the scan under settled rules.** Recorders are WHO with a thin life flagged (Malech, Wigram, Ormanian, Scher). Moffett and Gale are WHO on held lines in Underwood's Call of Korea and the Korean Repository. Pius X is STORY on two held encyclicals; Mar Shimun Benyamin is STORY on one witness (the Opus check corrected the draft's "Mar Shimun XXI", a later patriarch). Other popes are WANTED because no text of theirs is held. No row carries the OUTSIDE WITNESS label.

**Outcome of the era 10 sweep.** 134 rows (a paired row counts once): WHO 6, STORY 2, LISTED 6, WANTED 120. A further 124 rows of people are held for Mark and carry no verdict. Judgment-call rows: 55. Era 10 has no live person entries (all 71 entries are movements with empty `people` lists). The Library holds almost nothing of 1906 to c. 2010. An Opus check read 142 rows (124 confirmed, 12 corrected, 6 not supported) and every death tag. The full table and the checks: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era10/`.

**What this does not change.** No census, record or site change is made by this scan. The held list waits for Mark's rule on living people. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12).

## 2026-11-12 — Living people Listed only, recent deaths scored, Spiritualism removed, Syriac page faults to the clean-up (Mark, 2026-11-12)

**Mark's rulings (2026-11-12, picked from options; relayed by the coordinator).**
- **Living people, "Listed only":** "Living people appear in their tradition's lists but get no Who profile or story until after they die." Every held person who is alive is LISTED, tagged "living: Listed only until death". Where a death cannot be confirmed, the person is treated as living and LISTED, tagged "status unknown: treated as living". No status is invented either way.
- **Recent deaths, "Score normally":** "Score them like anyone else, as long as a held source or the census states the death. Only the living wait for the rule above." Ford, Lefebvre, Schutz, Antonios and every other person whose death in 1990 or later is stated in a held source or the census are scored as usual. A recent death known only from common knowledge stays "status unknown".
- **Spiritualism and New Thought, "Remove them":** "Follow the target list: these movements are outside the scope, so their 10 rows come off. They can be added back if you widen the scope later."
- **Syriac page, "In the clean-up":** "Fix them with the other 11 built worlds, as one change order, alongside the about 560 bare names."

**What was done.** The era 10 audit and page were rebuilt under rulings 1 and 2. The 124 rows of the first version's held list became Listed-only rows or scored rows; a second Opus check confirmed the census statements of death for Ford, Lefebvre, Schutz, Antonios and Gatu, moved Moon, Abiodun and Ilia II to scored rows, and re-tagged twelve "living" rows to "status unknown". Fourteen held names that are not persons who shaped a tradition (modern scholars and sources, an unidentified pair, a line of office holders, a name already in another era) are listed under "Not scored". The six Spiritualism and New Thought rows (10 people) were removed from the era 9 audit, and the era 9 page was republished. The Syriac page faults are in Open-Gaps. Era 10 now stands at 244 rows: WHO 6, STORY 2, LISTED 108, WANTED 128 (101 of the LISTED rows are Listed-only). Era 9 stands at 249 rows: WHO 34, STORY 11, LISTED 49, WANTED 155.

**Coordinator calls (not Mark's words; Mark may overrule).** Ilia II is scored on a death stated in an era 5 census entry (the census as a whole counts). Gatu is scored WANTED on the census citation of his obituary. People who died before 1990 by common knowledge stay scored under the earlier coordinator call; twelve more possible pre-1990 deaths known only from a model's memory stay "status unknown" until a source confirms them.

**What this does not change.** No census, record or site change. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12), with Mark's four rulings as stated.

## 2026-11-12 — The era 8 Who scan: church heads by the two-witness rule, Quesnel LISTED, one outside witness (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).** The read-only scan of era 8 (1650–1815 CE) used the standard of eras 1 to 7. Five questions went to the coordinator, none a major decision, each answered by a settled precedent:
- **Heads of churches or parties with no text of their own held:** the two-witness precedent (Ferenc Dávid, de Nobili). WHO, flagged "no own text held", where two independent held witnesses carry the person; STORY where only one does. Hacob IV, Simeon of Erevan, Mar Thoma I, Mar Dionysius I and De Cock all went under the two-witness rule and are WHO.
- **Compilers:** Freylinghausen stays WHO; Reitz is LISTED.
- **Arnauld and Quesnel:** Arnauld is WHO, flagged. Quesnel goes by the Melanchthon rule exactly. The bull Unigenitus of 1713 is held but prints only the 101 condemned propositions, not the Réflexions morales, and his life rests on Neale 1858 alone, so he is LISTED under the later-retelling rule.
- **Outside witness:** the era 7 Herberstein precedent (a Christian writer is inside Christianity, whatever the church). Rycaut, Tournefort and Ludolf are plain WHO recorders. Volney is the only label kept, with his skepticism marked as his standpoint. Moreau de Saint-Méry is plain, as a partisan.
- **People with no era 8 census entry:** scored here by date of work; the census gaps are in Open-Gaps 225.

**Calls made by the scan under settled rules.** Doctrine-only classics (Barclay, Chauncy, Tennent) LISTED; modern historians who are the sole source of an entry not scored and flagged for era 9; Aquino de Belén and the VOC translators LISTED; Kimpa Vita, da Gallo and Pedro IV WANTED, because the two Capuchin relations are not held; Archdeacon Thomas and Mar Thoma I are one man, one WHO row; Carey, Richard Allen, Yohannan Hormizd and Gregory V left to era 9, by the era 9 scan's own list. Boundary names from the era 7 and era 9 scans are scored once here.

**Outcome of the era 8 sweep.** 411 rows (a paired row counts once): WHO 137, STORY 51, LISTED 179, WANTED 44. Judgment-call rows: 232. The live person entry, John Wesley, is WHO, so none is flagged. An Opus check read the cited passages for 223 WHO, STORY and WANTED rows (211 confirmed, 12 corrected, none unsupported, no invented person-detail), 46 LISTED rows, and 23 later rows (21 confirmed, 2 corrected), and re-tested every WANTED row against the era 7 precedents (eight moved up). The full table and the checks: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era8/`.

**What this does not change.** No census, record or site change is made by this scan. Councils stay out of the census until the change order named in the era 2 entry; gatherings found are listed as leads for the councils list. Approved to proceed (coordinator, under Mark's full-auto instruction of 2026-11-12).

## 2026-11-12 — Who profiles, era 1 batch 1: Opus drafts the rest, majors capped at 2:30, Marcion of Pontus (Mark, 2026-11-12)

**The test.** Mark's earlier ruling (2026-11-12, picked from options): "Opus drafts the first era 1 batch of 8–10, and a separate fresh Opus agent reviews it. I measure the allowance cost and show you the drafts. Then you decide whether Opus drafts the rest." The batch was Josephus, Ignatius of Antioch, Marcion, Justin Martyr, Clement of Alexandria, Eusebius of Caesarea, Hermas and Valentinus, drafted to `Who_Profile_Pattern.md`. An independent Opus agent reviewed it: round 1 found 16 blocking and 46 minor findings, and round 2 found all 16 resolved. Mark saw the result at https://claude.ai/artifact/L6WmFpm7yFx9YyaJCmwiA3.

**Cost.** The batch came to 22.40 on the session record's `cost_usd` measure, about 2.8 per profile: drafting at most 13.75, review round 1 about 4.84, and fixes with round 2 3.81. The measure is telemetry at API rates, not a bill. On the same measure, each whole Sonnet era scan came to between 15.9 (era 9) and 47.6 (era 8). No paid API calls were made.

**Decided (Mark, 2026-11-12, picked from options, relayed by the coordinator).**
1. **Drafter, "Opus for all".** Opus drafts every remaining Who profile, and an independent Opus agent reviews each batch. This is a change order against `CLAUDE.md`'s "Sonnet drafts and revises", and that line now names the exception.
2. **Major marks, "Confirm all".** Josephus, Ignatius of Antioch, Marcion, Justin Martyr, Clement of Alexandria and Eusebius of Caesarea are major. Hermas and Valentinus are not.
3. **Length, "Cap majors at 2:30".** "Trim each major brief to 2:30 at most." The six majors now run 392 to 404 words, about 2:25 to 2:30 at Jon's pace. Hermas and Valentinus run about 1:55.
4. **Name, "Marcion of Pontus".** "This follows the two early witnesses. The brief can mention that Epiphanius later names Sinope, marking that as his claim." The id is `marcion-of-pontus`, and every first mention matches.

A targeted Opus recheck of the trimmed text and the renaming was the third and last review round. The approved files are in `Who-Profiles/era1/batch1/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-12_who-profiles-era1-batch1/`. No census, record or site change is made. The profiles go onto the site with the map Who build (Open-Gaps, "Placing the approved Who profiles", 2026-11-12). Approved to proceed (Mark, 2026-11-12).

## 2026-11-12 — The supplement Who scan: later retelling decides the early-saint Lives, the follow-up pass kept to its named leads (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).** The read-only scan covered people the Library holds but no census text names, so the ten era scans did not reach them (leads from the era audits and Open-Gaps 219 to 227, plus a script over the corpus-map). Ten questions went to the coordinator, none a major decision:
- **Follow-up pass:** one short pass on the named leads only (Niketas Stethatos, Ruricius, Marcus Cassinensis, the Collectio Avellana popes, John Fletcher of Madeley, the Young volume), with the same check. It was not widened.
- **People named by a census text who fell between eras:** the 15 WANTED rows (eras 9 and 10) stay in the supplement.
- **Early saints' Lives:** the later-retelling rule of the era 4 scan applies. A long Life written centuries later is still a later retelling, so length is not the test. Senan, Findian, Cadoc, Paternus, Findchua, Carantoc, Tatheus and Bernacus are LISTED. Brendan stays WHO on Adomnán's Life of Columba and Ciarán on Adomnán and Tirechan, which carry them from near their own time.
- **Kept as scored:** Sempad WHO and Hayton LISTED (does the book record the church's own events); the Paris Mission of Korea (Imbert, Berneux and Daveluy WHO, the other four one STORY group row); Arnaud WHO flagged and Boyer LISTED; Harasiewicz WHO, McKenzie STORY, Harnack WANTED.
- **Elipandus and Felix:** WHO (pair, Contested). The condition set was met: Elipandus's letters, Beatus and Heterius, the Frankish annals of 792 and 794 and the Frankfurt capitulary of 794 are held.
- **Corrections to earlier audits:** four change-order items are logged in Open-Gaps 229 and no earlier audit is edited.
- **Whitespace-tolerant absence check:** step one of the combined WANTED list (phase 2). Any era-audit WANTED row found to be held is logged by era and dropped from the list.

**Mark confirms the coordinator calls (2026-11-12).** Mark reviewed the full list of coordinator calls from the era 6 to 10 scans, the era 10 follow-up and the councils scan, and said, verbatim: "i think these all work". Those calls now stand as confirmed by Mark. They are the era 6, era 7, era 8, era 9 and era 10 Who-scan entries, the councils scan entry and the living-people follow-up entry, all 2026-11-12. Those entries are not edited.

**Calls made by the scan under settled rules.** Wilfrid, Cuthbert, Cedd and Chad WHO on Bede; recorders WHO with a thin life flagged; Olivi and Payne WHO by the Melanchthon rule; Elizabeth of Thuringia, Eadburga and Bugga WHO by the women rule; Berengar LISTED; popes and rulers STORY on official texts; Abelard WANTED because the census names him; no row carries the OUTSIDE WITNESS label.

**Outcome.** 253 rows (a paired or group row counts once): WHO 108, STORY 36, LISTED 92, WANTED 17. An Opus check opened the cited passages for 158 WHO, STORY and WANTED rows (127 confirmed, 27 corrected, 2 not supported, no invented person-detail), 32 LISTED rows, the ten founders, and 15 follow-up rows (8 confirmed, 7 corrected, none unsupported). The full table and the checks: `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/`.

**What this does not change.** No census, record or site change is made by this scan, so there is no data release number. Approved to proceed (coordinator, 2026-11-12; Mark may overrule).

## 2026-11-12 — The combined wanted list, eras 1 to 10: the re-run first, Yared and Pantalewon LISTED (coordinator, under Mark's full-auto instruction of 2026-11-12)

**Mark's instruction (2026-11-12, verbatim, relayed by the coordinator).** "you can continue with era 7 - 10 full auto, im stepping our for a few hours, only hold if there is a major decision needed, otherwise use our principles and past decisions to guide you".

**Coordinator calls under that instruction (not Mark's words; Mark may overrule).**
- **One combined list.** Following Mark's ruling of 2026-11-11 ("After all scans", Open-Gaps 220), the Library thread gets one list, ordered by era with major figures first: every WANTED row of the ten era audits and the supplement, the outside-witness sources and council records named in Open-Gaps 219 to 227, and the Library-label corrections. The Spiritualism and New Thought sources stay out (Mark, 2026-11-12).
- **Re-run first.** Every WANTED row was searched again with whitespace-tolerant patterns before the list was built, because the OCR files double-space names. Any row found held is logged as a change-order item by era and dropped from the list.
- **Later retelling is a general rule.** The ruling that named ten early saints did not limit the rule. Yared and Pantalewon are LISTED too, unless a held source from near their own time carries them. None is held; Yared's Life survives in one undated manuscript and Pantalewon's is by Metropolitan Yeshaq, about 1480. Roger Clap moved from LISTED to STORY (a first-person testimony needs no church office, the Hopper precedent). Vinnian, author of the held Penitential, has his own LISTED row beside Findian of Clonard because their identity is Contested.
- **Major marks.** The audits of eras 1 to 5 marked only WHO rows. A Sonnet pass proposed yes or no for the 175 wanted rows with no clean mark, by the audits' own test; the list labels them "(proposed here)". They are not Mark's.

**Outcome.** 461 person sources after merging 2 rows that want the same source and dropping 1 found held (Charles Simeon, era 9): 150 marked major. Plus 27 outside-witness sources with no person row and 46 council records. The supplement audit now reads 254 rows: WHO 106, STORY 37, LISTED 94, WANTED 17. A script check passed on all 552 rows of the list. The list and the checks: `Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/`.

**What this does not change.** No census, record or site change is made, so there is no data release number. Nothing is acquired or queued; the coordinator decides how the list is handed to the Library thread. Approved to proceed (coordinator, 2026-11-12; Mark may overrule).

## 2026-11-12 — Who profiles, era 1 batch 2: the major marks confirmed (Mark, 2026-11-12)

**The batch.** The eight era 1 WHO rows from the first era 1 scan that were neither live nor in batch 1, taken in date order: Tacitus and Suetonius (both labelled outside witness), Tatian, Bardaisan of Edessa, Hippolytus of Rome, Novatian, Pontius the Deacon and Dionysius of Alexandria. Ephrem, Augustine, Athanasius, Jerome and Didymus, marked "era 2 by date" in that scan, are left for era 2. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all".

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review, found 6 blocking and 47 minor points. The blocking ones were a contested birth date told as settled (Suetonius), a reconstruction told as fact (Tatian), a dispute stopped before its witness's verdict and one altered quote (Bardaisan), a partisan source presented as neutral (Novatian's Auxanon), and a role standing in for a named witness (Pontius). Round 2 found all 6 resolved and 3 new one-sentence points, all fixed. Round 3, the last, found no blocking point. Every quotation was re-checked word for word against its vendored file. No paid calls were made. Mark saw the result at https://claude.ai/artifact/CA5h2Zg38UinqEWFr1V4Lm.

**Decided (Mark, 2026-11-12, picked from options, relayed by the coordinator).** Major marks, "Confirm all". Tatian, Hippolytus of Rome, Novatian and Dionysius of Alexandria are major, at 400 to 403 words, about 2:28. Tacitus, Suetonius, Bardaisan of Edessa and Pontius the Deacon are not, at 302 to 323 words, about 1:51 to 1:59.

**Coordinator calls.** The batch membership and date order, and leaving the "era 2 by date" rows to era 2.

**What is still open.** The supplement Who scan (Open-Gaps 229) adds three era 1 WHO rows that are in neither batch: Peter of Alexandria, Anatolius of Alexandria and Laodicea, and Polycrates of Ephesus. The site-work items and name gaps are in Open-Gaps, "Era 1 Who batch 2: site list lines and name gaps" (2026-11-12).

The approved files are in `Who-Profiles/era1/batch2/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-12_who-profiles-era1-batch2/`. No census, record or site change is made, so there is no data release number. Approved to proceed (Mark, 2026-11-12).

## 2026-11-12 — Pronunciation list for the audio script: Standard English, Mark's seven names, a pause between paragraphs (Mark, 2026-11-12)

**Mark's rule, verbatim ("Standard English").** "Use the usual English way of saying these names, as an English-language documentary narrator would: roo-FY-nus, DEE-shus, sess-uh-REE-uh." It governs every name with more than one accepted way to say it.

**Mark's seven fixes, from listening to the live Origen brief.** Origen → OR-ih-jen; Eusebius → yoo-SEE-bee-us; Hexapla → HEK-suh-pluh; Rufinus → roo-FY-nus; Caesarea → sess-uh-REE-uh; Decius → DEE-shus; Nazianzus → naz-ee-AN-zus.

**Mark's pacing note.** In the Origen brief, after "in a book called the True Discourse", the move to "But on a journey through Palestine..." has almost no pause. He suggested a paragraph break such as `<break time="0.5s" />` between paragraphs.

**Built.** `Build/tools/tree-narration-pronunciations.json` holds the seven, each a respelling, and the pause tag. `requestTextFor` in `Build/tools/generate_tree_narration.mjs` applies them in person runs only, to the request and nowhere else. Matching is by whole word in the case written, so possessives and "X of Y" forms are caught. The census text, the recording fingerprint and the page text do not change. Tests are in `generate_tree_narration.test.mjs`.

**Coordinator calls (not Mark's words; Mark may overrule).**
- **The pause uses `[pause]`, not `<break>`.** ElevenLabs' current docs say "Eleven v4 and Eleven v3 do not support SSML break tags" and point to audio tags, ellipses and text structure. They show `[pause]` in an example but list no pause tags for v4. Whether `[pause]` gives the half second Mark wants is unconfirmed until a paid test is heard.
- **Respellings, not a pronunciation dictionary.** The docs do not say whether dictionaries work on v4, and the dictionary page could not be read.
- **Person runs only.** The other tree narration runs are unchanged.
- **Proposals not applied.** 97 more names are proposed on the "Pronunciation List" page, with an Opus check. Only the seven are live.

**What this does not change.** No census, record or site change is made and no recording is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-12; Mark may overrule).

## 2026-11-12 — Who scan records cleaned: each person once, five change-order items applied, Pliny the Younger Who (coordinator; Pliny ruling by Mark)

These are change orders to merged audit records. The census, `records/`, `packages/`, `cic-website/` and `cft-website/` are not touched.

**Decided (Mark, 2026-11-12, picked from options, relayed by the coordinator).** Pliny the Younger, the one undecided era 1 row, becomes "Who, outside witness", not major, alongside Tacitus and Suetonius. His profile goes in era 1 batch 3. Reason: Mark's ruling.

**Duplicates merged (24 rows removed), reason: the same person stood in two places.** The rule is the settled date-of-work rule: keep each person once, in the era of their main work, and where the rows differ keep the better-evidenced row and merge in any held source the other cites. Every removed row is kept word for word in `Build/Ministry/Operations/Audits/2026-11-12_who-scan-dedupe/Removed_Rows.md`, with where it went.
- Pontius the Deacon (era 1): the stale LISTED row from the first table goes; the WHO row of the addendum stays.
- Era 1 rows tagged "era 2 by date", which era 2 had already re-scored: Eusebius of Caesarea, Ephrem the Syrian, Augustine of Hippo, Athanasius of Alexandria, Jerome, Didymus the Blind, Aphrahat, Possidius of Calama (LISTED, now WHO in era 2), Faustus of Milevis, Valens of Mursa with Ursacius of Singidunum, Palladius of Ratiaria. The era 2 rows stay; they already cite every source of the era 1 rows.
- Era 2 to era 3 (Avarayr 451 and later): Vardan Mamikonian (STORY in era 2, WHO in era 3; the better-evidenced WHO row stays), Eghishe/Elishe (era 3 stays; the era 2 tags Contested and Inferential-Thin are merged in), Euthymius the Great and Reccared (era 2 itself sent both to the era 3 scan).
- Era 3 to era 4: Elfoddw/Elbodug (era 4 stays) and Heraclius (era 4 stays, the live person entry; the era 3 sources are merged in).
- Era 7 to era 8: Richard Baxter, Sir John Chardin, Marie de l'Incarnation and Mar Atalla/Ahatallah (LISTED in era 7, STORY in era 8; the era 8 STORY row stays). The era 7 sources are merged into the era 8 rows.
- Era 8 to era 9: Herman of Alaska and Philiphê Bỉnh (both WANTED; the wanted sources of both rows are merged into the era 9 rows). Herman's work on Spruce Island and Bỉnh's writings are after 1815.
- The script ran over all ten audits and the supplement with spelling, diacritic, "and"/"/" and bracketed-name tolerance. The other repeated names are different people and stay: Callistus (bishop of Rome, and the Melitian monk), Julian (the Apostate, the Nubian missionary, the patriarch of Antioch, Julian of Eclanum), Symmachus (the prefect, and the pope), the two Thomas Joneses, and the two John Thomases.
- The provisional "Carried to era 4" (era 3) and "Carried to era 5" (era 4) tables repeated 18 people already scored in the next era. They are removed too; each section keeps the list of names. `Era8_Carry_Rows.md` in the era 7 folder is a separate hand-off file and was not changed.

**Small fixes.** Era 9, James Thomson (supplement table): "died before 1990 (common knowledge)" is replaced by "death not in a held line", since no held file gives his death. Era 10: "101 of the LISTED rows" now reads 102, as the table does. Era 9: "157 of the 249 rows are WANTED" now reads 154, as the table does after the Simeon rescore below. The count lines of eras 1, 2, 3, 6, 7, 8 and 9 follow their tables.

**Change-order items of Open-Gaps 229 and 230, applied under the settled rules.**
- Isidore of Kyiv (era 6): LISTED to STORY. His letter on the fall of Constantinople is held in full (PG159 55969 on, listed at 337-339), a first-person eyewitness testimony. Not WHO: one letter, no body of work, no following held.
- Josaphat Kuntsevych (era 7): WANTED to LISTED. Susza's Life is held, but it is a later retelling and an advocacy text (1665), so the later-retelling rule applies. The Polotsk process acts are not held; the row is no longer WANTED and leaves the combined wanted list.
- Charles Simeon (era 9): WANTED to LISTED. Held: Wesley's entry of 20 December 1784, Curnock's life note, and Marsden's life with one quoted letter. That is a meeting and a few facts told by later hands, with no work of his own. WHO flagged "no own text held" was the other option.
- The Zoilus note (era 3): he is the Alexandrian patriarch (MOMM2 18879-18881), not one of the African Three Chapters bishops.
- Anna Komnene (era 5): the Verdict cell no longer says "(OUTSIDE WITNESS)", to match the text ("WANTED without the label").
- One Opus subagent confirmed the cited lines of the three rescored rows. Its findings are in the audits' rows.

**Combined wanted list.** Josaphat Kuntsevych leaves it, and the era 8 row of Philiphê Bỉnh merges into his era 9 row. It now holds 459 person sources (150 major): era 7 has 8 and era 8 has 42. Audit-row references were re-pointed and `trace_check.py` passes. The Major proposals file drops the era 8 Bỉnh row (174 rows, 35 yes).

**New counts.** Era 1: 72 people (64 in the first table plus 8 addendum rows); WHO 24, STORY 8, LISTED 36, WANTED 4. Era 2: 111. Era 3: 98. Era 6: STORY 22, LISTED 57. Era 7: 255. Era 8: 409. Era 9: WHO 34, STORY 11, LISTED 50, WANTED 154. Total 2,112 people, 254 of them supplement rows. The Who Scan Register page was rebuilt from the corrected audits.

No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-12; Mark may overrule).

## 2026-11-13 — Data release 40: the Lactantius quotes on the Tertullian link cite the public-domain English (Mark, 2026-11-13)

**The ruling it carries out.** On 2026-11-12, through the operations thread (ops open item 6), Mark ruled that the two CC BY-SA quotes on the link `tertullian-s-voice--latin-apologists` be replaced with the public-domain 1890 Brandt print, re-verified word for word.

**What was found.** The Library's public-domain scan of the 1890 print (`cic/texts/lactantius_divinae-institutiones-epitome-lat_brandt-csel19.txt`, Internet Archive operaomniaacced00laubgoog) has no page 411. The OCR runs from page 410 straight to page 412, and Div. inst. V.4.3 is on page 411. So the ruled swap could not be made from a held file.

**Decided (Mark, 2026-11-13, picked from options, relayed by the coordinator).** "English now, Latin later." The link now cites William Fletcher's translation in Ante-Nicene Fathers vol. 7 (1886, public domain, `cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`): the chapter heading at line 4565, "Chap. IV.—Why This Work Was Published, and Again of Tertullian and Cyprian.", and at line 4569, "fully pleaded the same cause in that treatise which is entitled the". The ANF text puts markup between "Although", "Tertullian" and "Apology", so the verbatim quote is the run of plain words between them. The link's note, grade and verification state are unchanged. A public-domain scan of the 1890 print that holds page 411 goes on the Library list, so the Latin can be added back (Open-Gaps 234).

**Checked.** Both quotes were checked by two methods: the census validator's verbatim span check, and a separate exact-substring count over the file (each occurs once, on its cited line).

Data release 40 (2026-11-13). The data page's release number follows. Approved to proceed (Mark, 2026-11-13).

## 2026-11-13 — Conversations not yet live: the tree names each Representative but does not link to the conversation (Mark, 2026-11-13)

**The question.** On 2026-11-12 Mark told the operations thread that the tree stands alone and that "we will not have the conversation live as it will take more time to get to the context accuracy we need". The tree still carried "Meet [Representative] on Church in Conversation" on 25 tree pages and on the map card. Each link led to a Church in Conversation tradition page whose "Begin a conversation" button starts the engine.

**Decided (Mark, 2026-11-13, picked from options, relayed by the coordinator).** "Keep, say 'coming soon'." The Representatives' names stay. Each link becomes a plain line with no link: "Conversations with [Representative] are coming soon to Church in Conversation." The map's "representative voice" lines and the footer link to the Church in Conversation home stay.

**How.** One setting, `conversationsLive` in `Build/tools/tree_site_pages.json`, set to false. The tree page generator and the map (`CONVERSATIONS_LIVE` in `cft-website/index.html`) both follow it, and a test checks that they agree. Setting it to true restores the links in one change. No census change, so there is no data release number.

Approved to proceed (Mark, 2026-11-13).

## 2026-11-13 — Church in Conversation keeps its conversations on for the pilot; the tree's privacy page names no system (Mark, 2026-11-13)

**Decided (Mark, 2026-11-13).** "keep it on for church in conversation for the pilot, fix the feedback bar keeping it simple doesnt have to tell our system info."

- The "Begin a conversation" buttons on the Church in Conversation site stay on for the pilot. The tree keeps its "coming soon" lines (Decision-Log, "Conversations not yet live", 2026-11-13).
- The tree's privacy page, section "The feedback bar", no longer says feedback goes to Church in Conversation's server. It now says: "Feedback comes straight to our team. It carries no visitor ID and no cookie. We use it to fix and improve the tree." What each button sends is unchanged, and so is the feedback bar itself.

No census change, so there is no data release number. Approved to proceed (Mark, 2026-11-13).

## 2026-11-13 — Who profiles, era 1 batch 3: Peter of Alexandria major, Pliny the Younger an outside witness (Mark, 2026-11-13)

**The batch.** The three era 1 WHO rows from the supplement Who scan that were in neither earlier batch, Peter of Alexandria, Anatolius of Alexandria and Laodicea and Polycrates of Ephesus, and Pliny the Younger, ruled a Who as an outside witness, not major (Mark, 2026-11-12). Opus drafted each profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all". Pliny follows the outside-witness form of Tacitus and Suetonius in batch 2.

**Decided (Mark, 2026-11-13, picked from options, relayed by the coordinator).** Major marks, "As proposed". Peter of Alexandria is major, at 402 words, about 2:29. Anatolius of Alexandria and Laodicea and Polycrates of Ephesus are not, at 323 words each, about 2:00. Pliny the Younger is not major, as an outside witness, at 310 words, about 1:55.

**Review.** Two rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review, found no blocking point and 7 minor ones. Six were fixed: one dispute-announcing opener, three sentences over 25 words, two men named Eusebius in one scene, and a records.json tag. The seventh, where the outside-witness label renders, belongs to the page. Round 2, a targeted recheck, found all six resolved and nothing new. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**What is still open.** The Library holds no edition of Pliny's Letters. Open-Gaps 235, "Era 1 Who batch 3" (2026-11-13), logs that need and closes the batch 2 and Pliny items.

The approved files are in `Who-Profiles/era1/batch3/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era1-batch3/`. No census, record or site change is made, so there is no data release number. Mark ruled on the major marks; the review outcome and merge are the coordinator's call under Mark's full-auto instruction of 2026-11-13. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 1: nine profiles, five majors (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The first nine era 2 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/Who_Scan_Era2.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, that are neither live on the site nor already written, taken in order of death or last attested year, as era 1 batch 2 was: Melitius of Lycopolis, Arius, Pachomius, Antony the Great, Frumentius, Aetius of Antioch, Hilary of Poitiers, Lucifer of Cagliari and Hilarion of Gaza. Eusebius of Caesarea is skipped, since era 1 batch 1 wrote him. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all". The supplement scan's twelve era 2 WHO rows are not in this sequence (Open-Gaps 236).

**Coordinator calls (not Mark's words; Mark may overrule).** The batch and its date order. Major marks: Arius, Antony the Great, Pachomius, Hilary of Poitiers and Frumentius are major, at 401 to 404 words, about 2:29 to 2:30. Frumentius is major because he founded the line of the Ethiopian church, a river on the map. Major sets the 2:30 cap, not a target, so Pachomius and Frumentius are written only as far as the held material carries. Melitius of Lycopolis, Aetius of Antioch, Lucifer of Cagliari and Hilarion of Gaza are not major, at 320 to 323 words, about 2:00.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review, found 9 blocking and 59 minor points. Its new pattern was the witness swap: a modern editor's words given to an ancient writer, or a writer's own phrase given to the document he quotes (Robertson's summary quoted as Athanasius on Arius; the "Bishop of Auxumis" of Athanasius given to the emperor's letter on Frumentius; a nickname given to Aetius's own party with no witness). The others were a Socrates account of the Arian quarrel's start told as settled, an interval no source gives (Pachomius), a dropped manuscript note (Antony), a shipwreck no held account has (Frumentius), and a role in place of a named witness (Hilarion). Round 2 found all 9 resolved, 7 minor points, and one new blocking point that a round 1 suggestion had caused: Blomfield Jackson's own sentence on Theophilus given to the Dictionary of Christian Biography he had just quoted (Frumentius). All were fixed. Round 3, the last, found no blocking point and one comma, which was fixed. Card sentences over 25 words stay as card text, as in era 1 batch 2. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**What is still open.** Open-Gaps 236, "Era 2 Who batch 1" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch1/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch1/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 2: nine profiles, six majors (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next nine era 2 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/Who_Scan_Era2.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after era 2 batch 1, in order of death or last attested year: Macrina the Younger, Auxentius of Durostorum, Ulfila, Damasus of Rome, Priscillian, Cyril of Jerusalem, Apollinaris of Laodicea, Tyconius and Eunomius of Cyzicus. Athanasius, Ephrem, Basil and Gregory of Nazianzus fall in the same years and are skipped as live person entries. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** The batch and its date order. Major marks, as proposed by the drafter: Ulfila, Damasus of Rome, Priscillian, Cyril of Jerusalem, Apollinaris of Laodicea and Eunomius of Cyzicus are major, at 402 to 406 words, about 2:28 to 2:30. This follows batch 1, where Aetius was not major because Eunomius is the larger Anomoean figure. Macrina the Younger, Tyconius and Auxentius of Durostorum are not major, at 317 to 324 words, about 1:57 to 2:00. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in two parts, found 7 blocking and 40 minor points. The blocking ones were a modern editor's reconciling reading told as following one witness (Macrina), a contested year and a contested condemnation told as settled on the card (Damasus, Priscillian), hostile witnesses left unmarked (Orosius and the Council of Braga for Priscillian; Augustine for Tyconius), a card quotation not word for word from a work the card did not list, and a family the card said no source gives (both Cyril). Round 2 found all resolved and one new blocking point: the Ulfila card said no held source names his consecrator's see, but Duchesne names Eusebius of Nicomedia, and Kauffmann's synod of 341 agrees. That and 5 minor points were fixed. Round 3, the last, found nothing open. Card sentences over 25 words stay as card text, as in era 1 batch 2. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** The Council of Braga that names Priscillian is dated era 599 in its held acts, which is 561, not 563. The scan's birth years for Cyril, Apollinaris, Macrina and Eunomius rest on no held line, so the cards give the years the sources give. Auxentius of Durostorum is in the people list of one movement only, the era 3 "Gothic, Vandal & Lombard Homoian Christianity", and his card names it.

**What is still open.** Open-Gaps 237, "Era 2 Who batch 2" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch2/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch2/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 3: nine profiles, three majors (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next nine era 2 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/Who_Scan_Era2.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batches 1 and 2, taken in order of death or last attested year: Ammianus Marcellinus, Martin of Tours, Didymus the Blind, Evagrius Ponticus, Fabiola of Rome, Epiphanius of Salamis, Olympias of Constantinople, Melania the Elder and Marcella of Rome. Paula of Rome is skipped, since she is live. None of the nine is live or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all". Ammianus Marcellinus carries the outside witness label, in the form of Tacitus in era 1 batch 2.

**Coordinator calls (not Mark's words; Mark may overrule).** The batch and its date order. Major marks, as the drafter proposed: Martin of Tours, Evagrius Ponticus and Epiphanius of Salamis are major, at 405 words each, about 2:30. Martin is major because Gallic monasticism grew from his houses and Sulpicius's Life made him a model saint of the Latin West; Evagrius because he set down the desert's teaching on the eight thoughts, and his Origenism was condemned after his death; Epiphanius because his Panarion is the era's great catalogue of heresies and he opened the Origenist quarrel in Palestine. Didymus the Blind, Ammianus Marcellinus (an outside witness), Fabiola of Rome, Olympias of Constantinople, Melania the Elder and Marcella of Rome are not major, at 322 to 324 words, about 2:00. Two ids carry a place: `fabiola-of-rome`, since Jerome's Letter 126 has a second Fabiola, and `olympias-of-constantinople`, from Palladius's "the deaconess of Constantinople".

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review, found 1 blocking and 34 minor points, and no witness swap of the era 2 batch 1 kind. The blocking point was Evagrius Scholasticus's report of Justinian's condemnation: "the Blind" was added to his words, and his "Evagrius" was told as this Evagrius, which he does not say. The sentence left the brief; the card keeps his words and the caveat, and the record tags the identification Inferential-Thin. The minors were mostly dropped hedges (Ammianus's "as I believe", Ramsay's "not entirely", Gennadius's "first to mention"), a card caveat missing from its brief, and first mentions without a place on the cards. Round 2 found all resolved but one partly, no new blocking point, and three new minors, all fixed. Round 3, the last, found no blocking point and one long sentence, which was split. Card sentences over 25 words stay as card text, as in the earlier batches. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**What is still open.** Open-Gaps 238, "Era 2 Who batch 3" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch3/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch3/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 4: nine profiles, three majors (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next nine era 2 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/Who_Scan_Era2.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after era 2 batch 3, in order of death or last attested year as the scan gives it: Rufinus of Aquileia, Pelagius, Paulinus of Milan, Sulpicius Severus, Honoratus of Arles, Palladius of Helenopolis, John Cassian, Possidius of Calama and Philostorgius. Augustine of Hippo falls in the same years and is skipped as a live person entry. The supplement scan's twelve era 2 rows stay for their own batch (Open-Gaps 236). Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** The batch and its date order. Major marks, as the drafter proposed: Pelagius, Rufinus of Aquileia and John Cassian are major, at 404 to 405 words, about 2:30. Pelagius is major because he gave his name to a movement with its own river and his own letter and answers are held; Rufinus because his translations and Church History shaped what the Latin church knew of Origen and Eusebius; Cassian because his Institutes and Conferences carried Egyptian desert monasticism to the West. Paulinus of Milan, Sulpicius Severus, Honoratus of Arles, Palladius of Helenopolis, Possidius of Calama and Philostorgius are not major, at 324 to 327 words, about 2:00. Palladius stays a recorder, as Auxentius of Durostorum did in batch 2. Paulinus's card names the movement whose voices line holds him, "Ambrosian Milan (standalone)", by its census name.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in two parts, found 2 blocking and 23 minor points, and no witness swap. The blocking ones were a translator's dates told as resting on Cassian's prefaces when he uses them to date the prefaces (Honoratus), and Jerome's attack on "a Palladius" told as settled to be this man, against Tillemont's doubt reported in the notes to Fremantle's edition of Jerome (Palladius). The minors were mostly contested dates told plainly, an unsourced life story told as report (Sulpicius), and first mentions without a place. Round 2 found all resolved, no new blocking point and six new minors, all fixed. Round 3, the last, found nothing open. Card sentences over 25 words stay as card text, as in the earlier batches. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** The Paulinus of Milan row says Marius Mercator makes the accuser of Caelestius the author of the Life. The held Latin of Mercator calls him only a deacon of Ambrose; the identification is Kaniecka's and a note in the Migne edition, so the record tags it Dominant Modern Reconstruction. The scan's years for Rufinus (411), Sulpicius (about 425), Pelagius (about 420), Philostorgius (about 439) and Honoratus (born about 350) rest on no held line; the cards give the years the sources give.

**What is still open.** Open-Gaps 239, "Era 2 Who batch 4" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch4/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch4/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 5: ten profiles, five majors (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The last seven era 2 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era2/Who_Scan_Era2.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after era 2 batch 4, in order of death or last attested year as the scan gives it: Socrates of Constantinople, Mesrop Mashtots, Cyril of Alexandria, Sozomen, Theodoret of Cyrrhus, Leo of Rome and Koriun. Augustine of Hippo and Nestorius fall in the same years and are skipped as live person entries. Then the first three, by death or last attested year, of the supplement scan's twelve era 2 WHO rows (Open-Gaps 236): Alexander of Alexandria, Eusebius of Nicomedia and Ossius of Cordoba. The other nine go to batch 6: Liberius of Rome, Marcellus of Ancyra, Moses the Black, Germanus of Auxerre, Hilary of Arles, Marius Mercator, Eutyches, Prosper of Aquitaine and Eznik of Kolb; several of their years rest on no held line, so that order is the scan's. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** The batch and its date order. Major marks, as the drafter proposed: Cyril of Alexandria, Leo of Rome, Theodoret of Cyrrhus, Mesrop Mashtots and Eusebius of Nicomedia are major, at 395 to 406 words, about 2:26 to 2:30. Cyril is major because he drove the Council of Ephesus of 431 against Nestorius and set the Christology both Chalcedonians and Miaphysites claim; Leo because his Tome was read at Chalcedon as a standard of the faith; Theodoret as the leading Antiochene theologian of his day, deposed in 449 and restored at Chalcedon; Mesrop because he made the Armenian letters and began the Armenian Bible; Eusebius as Arius's patron and head of the party that led the Eastern church after Nicaea, following Arius major in batch 1. Alexander of Alexandria and Ossius of Cordoba are not major, at 326 and 329 words, about 2:00: their held words are two letters and one letter, and Athanasius carries the river. Socrates of Constantinople, Sozomen and Koriun are Whos as recorders and not major, at 321 to 328 words, about 2:00, in the form of Auxentius of Durostorum in batch 2 and Palladius of Helenopolis in batch 4. Mesrop is a founder known through a disciple's record, and his brief marks Koriun's Life as hagiography. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in two parts, found 1 blocking and 22 minor points, and no witness swap. The blocking point was an absence claim a held file contradicts: the Ossius card said no source gave his death, but Henry Percival's council volume reports the views of Hefele, Cave and Pagi. The minors were mostly a bracket or a modern year given to the ancient author (Koriun's French; Prosper's consular dating of Leo's election), dropped hedges (Hartranft's "probably", Sozomen's "as it is reported"), one side of a dispute left out of a brief (Mesrop's letters), and first mentions without a place. Round 2 found all resolved but one partly, no new blocking point and three new minors: a pronoun left loose by a trim, a closed list of Arius-side sources that held files contradict, and a dropped honest limit. All were fixed. Round 3, the last, found all three resolved and nothing new. Card sentences over 25 words stay as card text, as in the earlier batches. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scans found in drafting.** No held line gives "about 405" for the Armenian alphabet or the scan's years for Mesrop; Koriun's patron is told two ways; Sozomen's years and spelling, and Eusebius of Nicomedia's death year and baptism of Constantine, rest on modern notes. Details are in Open-Gaps 240.

**What is still open.** Open-Gaps 240, "Era 2 Who batch 5" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch5/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch5/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-13 — Who profiles, era 2 batch 6: nine profiles, one major, era 2 complete (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The last nine of the supplement scan's twelve era 2 WHO rows (Open-Gaps 236), after the three in era 2 batch 5, in the order the batch 5 entry lists them: Liberius of Rome, Marcellus of Ancyra, Moses the Black, Germanus of Auxerre, Hilary of Arles, Marius Mercator, Eutyches, Prosper of Aquitaine and Eznik of Kolb. None is a live person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's batch 1 ruling, "Opus for all". This batch completes era 2: every era 2 WHO row of the era 2 scan and of the supplement scan is now written or skipped as live.

**Coordinator calls (not Mark's words; Mark may overrule).** Major marks, as the drafter proposed: Eutyches is major, at 400 words, about 2:28, because the archimandrite whose name the controversy took was condemned in 448, restored at Ephesus in 449 and condemned at Chalcedon, the council that divided the Chalcedonian and Miaphysite rivers. The other eight are not major, at 319 to 330 words, about 2:00. Moses the Black is not major, against the scan's proposal, since he founded no tradition, the call made for Hilarion of Gaza in batch 1. The coordinator's care point: the recorder label is used only where recording others is the main held role. Marius Mercator is a recorder and translator; Prosper of Aquitaine is described as a theologian and chronicler, and Hilary of Arles as a monk and bishop.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in two parts, found 2 blocking and 40 minor points. Both blocking points were the batch's recurring faults: an absence claim two held editors contradict (Prosper's brief said no source gave his birth or death, where Richardson's note to Gennadius and Freese's note to Photius give 403 to 463), and a witness swap (Eznik's brief gave Artashat and Mihr-Nerseh to Lazar of Pharp, who names no place and makes King Yazdegerd the edict's author). The minors were mostly facts placed under the wrong witness (Felix under Ammianus; "refuted the Arians", which is Blomfield Jackson's note, given to Marcellus's letter; the veil, which is a translator's note, given to Ambrose), a doubt overstated (the Mansi editors leave the author of the Life of Hilary open), first mentions without a place, missing source entries, and non-major briefs a little over 2 minutes. Round 2, a targeted recheck, found all resolved but two partly, both carried by round 1's own suggested wording, and 5 new minor points, all fixed. Round 3, the last, found all five resolved and nothing new. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Several of the supplement scan's years rest on no held line (Moses, Germanus, Liberius, Hilary, Prosper), and its "contested" date for Eznik's work has no held sides. Four card traditions are the scan's and name a record the person appears in, not his party. Details are in Open-Gaps 241.

**What is still open.** Open-Gaps 241, "Era 2 Who batch 6" (2026-11-13).

The approved files are in `Who-Profiles/era2/batch6/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-13_who-profiles-era2-batch6/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-13; Mark may overrule).

## 2026-11-14 — Who profiles, era 3 batch 1: ten profiles, five majors, Vakhtang I Gorgasali to STORY (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The first ten era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, in order of death or last attested year as the scan gives it: Vardan Mamikonian, Dioscorus of Alexandria, Euthymius the Great, Timothy Aelurus, Elishe, Victor of Vita, Moses of Khoren (by the traditional date), Barsauma of Nisibis and Narsai, then Lazar Parpetsi, whose row gives no year. Patrick and Peter the Iberian fall in the same years and are skipped as live person entries. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** Major marks, as the drafter proposed: Dioscorus of Alexandria, who presided at Ephesus in 449 and was deposed at Chalcedon, and whose name the churches that rejected Chalcedon kept; Timothy Aelurus, who led the anti-Chalcedonian church of Egypt through his exile; Barsauma of Nisibis, who held the synod of Beth Lapat in 484; Narsai, head of the school at Nisibis, whose homilies are held in English; and Vardan Mamikonian, the commander at Avarayr in 451, told by two near-contemporary histories. They run 391 to 404 words, about 2:25 to 2:30. Euthymius the Great, Elishe, Victor of Vita, Moses of Khoren and Lazar Parpetsi are not major, at 320 to 324 words, about 2:00. Elishe, Victor, Moses and Lazar are Whos as recorders. Euthymius is known through Cyril of Scythopolis's Life, which the brief marks as hagiography. Moses of Khoren's date and authorship stay Contested; the brief says the Library holds only the fifth-century side. Vakhtang I Gorgasali, WHO in the scan, is rescored STORY under Mark's era 3 ruling "Story unless own voice": no words of his own are held, since his speeches are the chronicler's and his one letter survives inside Lazar's History. Lazar Parpetsi took his place. Narsai keeps the id `narsai` with the card name "Narsai of Nisibis"; Lazar keeps the census name and id. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in three parts, found 6 blocking and 43 minor points. The blocking points were a witness swap (the dating of Lazar, from an introduction signed by Victor Langlois, given to the translator Samuel Ghesarian in the Vardan profile), a modern year told as Lazar's (he gives Avarayr a place and the feast of Pentecost, not 451), a contested claim told as settled (who baptized Aspebetus: Cyril of Scythopolis says Euthymius, Duchesne says Juvenal of Jerusalem), two absence claims held files contradict (Victor of Vita's see told as resting on unanimous manuscripts, where Halm's apparatus and Mesnage give the Utica variant; Lazar's census year 485, which matches Neumann's end date for the History), an identification told as settled where its editor leaves it open (the two Barhadbeshabbas, of the History and of the Cause of the Schools),. The minors were mostly editors' dates told as the ancient text's, dropped hedges, first mentions without a place, and the Library's word "held" on a card. Round 2, a targeted recheck, found all resolved but five partly, no new blocking point and five new minors; all were fixed. Round 3, the last, found the profiles clear and five minor points in the Open-Gaps entry, all fixed as worded. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Several of the scan's years rest on no held line (Timothy Aelurus, Euthymius, Narsai), Dioscorus's death year and both days for Avarayr are editors' dates, several Langlois line citations are wrong, Barhadbeshabba is held twice where the scan cites him only through Connolly, and no held work argues Moses of Khoren's later date. Details are in Open-Gaps 242.

**What is still open.** Open-Gaps 242, "Era 3 Who batch 1" (2026-11-14). The remaining era 3 WHO rows: 48 from the era 3 scan (59 not live, less these ten and Vakhtang I Gorgasali, now STORY) and 21 from the supplement scan, 69 in all.

The approved files are in `Who-Profiles/era3/batch1/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch1/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Who profiles, era 3 batch 2: ten profiles, four majors, Vahan Mamikonian and Kaleb of Aksum to STORY (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 1, in order of death or last attested year as the scan gives it: Joshua the Stylite, John Rufus, Brigid of Kildare, Zachariah Rhetor, Severus of Antioch, Caesaria of Arles the Elder, Caesarius of Arles, Julian, missionary to the Nobadae, Ferrandus of Carthage and Benedict of Nursia. Simeon of Beth Arsham falls in the same years and is skipped as a live person entry. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** Vahan Mamikonian and Kaleb of Aksum, WHO in the scan, are rescored STORY under Mark's era 3 ruling "Story unless own voice": no words of their own are held. Vahan's speeches and letters survive only inside Lazar of Pharp's History, and Kaleb's prayer only in the Book of the Himyarites and the Synaxarium. Ferrandus of Carthage and Benedict of Nursia took their places. Major marks, as the drafter proposed: Severus of Antioch, the leading theologian and patriarch of the anti-Chalcedonian church of Syria, whose letters are held in English; Caesarius of Arles, bishop for forty years, who signed first at Orange, whose chapters on grace and free will came from Rome, and wrote rules for monks and nuns; Julian, missionary to the Nobadae, who began the church at the head of the Nubian Christianity river, on the Frumentius precedent; and Benedict of Nursia, whose Rule founds the Benedictine river. They run 378 to 405 words, about 2:20 to 2:30. Julian's brief follows John of Ephesus, his one witness, and is not stretched to the cap. Joshua the Stylite, John Rufus, Brigid of Kildare, Zachariah Rhetor, Caesaria of Arles the Elder and Ferrandus of Carthage are not major, at 316 to 325 words, about 2:00. Joshua and Zachariah are Whos as recorders. Brigid's brief says plainly that Cogitosus wrote her Life long after her death and that it is a book of miracles, tagged Widely Accepted (the coordinator's care point); Benedict's marks Gregory the Great's Dialogues the same way. Julian's card name gives his role and John's own name for the people, since no held source gives him a place and "Nobadia" is in no held file. Zachariah keeps "Zachariah Rhetor", since "of Mitylene" rests on Brooks's identification. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in three parts, found 5 blocking and 36 minor points. The blocking points were the batch's recurring faults: an attribution told as settled (Joshua's Chronicle preserved by Dionysius of Tell-Mahre, which is Wright's view; Nau calls the compiler the Pseudo-Dionysius, writing in 775); a disputed authorship told as settled (the notice of Ferrandus called anonymous, where Arevalo prints it as Isidore's own chapter and Baronius gives it to Isidore); a false absence (all of Caesaria known from her brother's Life, where Krusch reports Venantius Fortunatus's poems on her); the coordinator's care point unmet (Brigid's brief framed the date of Cogitosus as open, where every held witness puts him long after her); and an ambiguous pronoun in the one sentence marking John of Ephesus as partisan. The minors were mostly a modern scholar's date or view given one side only, place names a source does not give, pronouns that can mislead, and first mentions without a place. Round 2, a targeted recheck, found all 41 resolved and 7 new minor points, all fixed. Round 3, the last, found the batch clear and one minor point in the records, fixed as worded. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Many of the scan's years rest on no held line or only on a Library file header (Severus, Zachariah, Benedict, Ferrandus, Julian); Brigid's years are Basnage's notice reprinted in Migne; several leads point to an editor's introduction or a commentary instead of the Life. Details are in Open-Gaps 244.

**What is still open.** Open-Gaps 244, "Era 3 Who batch 2" (2026-11-14). The remaining era 3 WHO rows: 36 from the era 3 scan (48 after batch 1, less these ten and Vahan Mamikonian and Kaleb of Aksum, now STORY) and 21 from the supplement scan, 57 in all.

The approved files are in `Who-Profiles/era3/batch2/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch2/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Who profiles, era 3 batch 3: ten profiles, three majors, Theodora a Who on Mark's named ruling (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 2, in order of death or last attested year as the scan gives it: Theodora, wife of Justinian, Marcellinus Comes, Cosmas Indicopleustes, Barsanuphius and John of Gaza (one paired profile, on Mark's pairing ruling), Mar Aba I, Vigilius of Rome, Romanos the Melodist, Cyril of Scythopolis, Procopius of Caesarea and Samson of Dol. Justinian I falls in the same years and is skipped as a live person entry. Dorotheus of Gaza, "mid-6th c." in the scan, falls after this batch: Migne heads Gallandi's notice on him "ANNO DOMINI DXCVI", and the Bollandists it reports place him at the end of the sixth century. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** Theodora stays WHO on Mark's own named ruling in the era 3 scan, "Theodora: Who" (2026-11-11), which sits beside his rule for rulers, "Story unless own voice"; no words of her own are held, and the speech in the Nika revolt is tagged as Procopius's composition in brief, card and records. Her card name gives her role, "wife of Justinian", since no held source gives a place that identifies her. Major marks, as the drafter proposed: Theodora, whose protection, by John of Ephesus's account, kept the anti-Chalcedonian refugees and set up the bishops of the separate Syriac Orthodox hierarchy; Vigilius of Rome, the pope at the centre of the Three Chapters quarrel and the council of 553, with his Constitutum and letters held; and Mar Aba I, the catholicos who reunited and reformed the Church of the East, whose synod of 544 is held. They run 402 to 405 words, about 2:30. The other seven are not major, at 320 to 325 words, about 2:00. Marcellinus Comes, Cosmas Indicopleustes and Cyril of Scythopolis are Whos as recorders; Marcellinus carries no label, by Mark's ruling. Procopius carries the Outside witness label, with his card's Tradition line "Outside the church". Cosmas's card tradition follows the census row, Aksumite Christianity, beside McCrindle's view that he most probably belonged to the Church of the East. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in three parts, found 11 blocking and 57 minor points. The blocking points were the recurring faults: false absences (Liberatus's chapter 22 said not to be in the held PL 68 file; the Synaxaristes life of Romanos and the German Life of Mar Aba said not held); a disputed attribution told as settled (the Menologion that holds Romanos's notice given to Constantine Porphyrogenitus, which is Pitra's view, where PG 99 gives the same Vatican manuscript to the emperor Basil); a source called hostile where no held scholar says so (the Book of the Popes on Vigilius); a false "only" on what the Book of the Popes says of Silverius; a second false absence for Barsanuphius (Evagrius Scholasticus, held, calls him an Egyptian enclosed near Gaza); two places told one way for Mar Aba (his baptism and burial, where the Life and Mari ibn Sulayman differ); Cosmas's church placed as settled; a witness swap (Andrea Gallandi's notice on Dorotheus credited to Migne, who reprints it); and the Life of Euthymius said to survive whole, where Cotelier's note says otherwise. The minors were mostly an editor's year told as the ancient source's, a judgment given to the wrong witness, witnesses not placed, and process words on a card. Round 2, a targeted recheck, found all 11 blocking and 56 minor points resolved and one partly, and 5 new minor points on cards and records, all fixed. Round 3, the last, found the batch clear, with two minor points on sentence length in three cards, fixed as worded. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Several of the scan's years rest on no held line or only on a Library file header (Theodora, Romanos, Cyril, Samson, Barsanuphius and John); Marcellinus's own chronicle ends at 534; Mar Aba's 540 is Chabot's reckoning; Vigilius's recantation is dated December 553; Theodora's Zachariah leads are a footnote quoting Michael the Syrian and Book IX, the later compiler's. Details are in Open-Gaps 245.

**What is still open.** Open-Gaps 245, "Era 3 Who batch 3" (2026-11-14). The remaining era 3 WHO rows: 26 from the era 3 scan (36 after batch 2, less these ten) and 21 from the supplement scan, 47 in all.

The approved files are in `Who-Profiles/era3/batch3/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch3/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Major councils, eras 1 and 2: the council pattern and nine profiles (Mark, 2026-11-14)

**Decided (Mark, 2026-11-14, in the council thread; his words as given).** The scope: "lets write the counsils for era 1 and 2 only for now". The pattern and its worked example, the Councils of Carthage and Rome on the lapsed (251), were shown to him in an Artifact. He added one field: "for the card, we need to know the issues/contriversy that caused to meet". He then approved: "approved, go ahead with era 2".

**The pattern.** `Council_Profile_Pattern.md`, adapted from `Who_Profile_Pattern.md`. A major council is an entry in the tradition-entry form, with `kind` `major-council`, its own icon and the title "Major council", under Mark's era 2 ruling, "counsels are treated like a tradition with a different icon and title. but people who are a part of it should be on the who click" ("The era 2 Who scan", 2026-11-11). Its people show under Who with their verdicts. What it adds to the Who pattern:
- each witness is tagged with its kind: acts, participant, later narrative or modern reconstruction;
- lost acts are said once, early;
- the condemned party's view is given in its own words where held;
- every count, and every date no ancient writer gives, names the historian it comes from;
- the issue that brought the bishops together, the decision and the outcome are three separate fields;
- sources fall into three groups.

The spoken brief has a ceiling of 2:30, never a target.

**Worker's calls under the pattern (not Mark's words; Mark may overrule).** A person in a council record whom no Who scan has scored shows as NOT SCORED, with no id, so the council profile makes no verdict. An id appears only where a Who profile or census entry already has one. Opus drafted every profile, as for Who profiles.

**The nine councils.** Era 1: the Councils of Carthage and Rome on the lapsed (251). Era 2: Arles (314), Nicaea (325), Sardica (343), Ariminum and Seleucia (359), Constantinople (381), the Conference of Carthage (411), Ephesus (431) and Chalcedon (451). Every brief runs 393 to 400 words, about 2:30. FK runs 7.4 to 8.5 and reading ease 60.1 to 63.8.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting.
- Round 1, the full review, found no blocking points, 6 substantial and 25 minor. The substantial points:
  - Arius's teaching was told only through the council, although his own letter is held.
  - Philostorgius was placed on the Homoian side; he was a Eunomian.
  - Gregory of Nazianzus's farewell was told as coming before the council met.
  - Timothy of Alexandria was marked NOT SCORED, although the supplement scan has him LISTED.
  - The Carthage record was called full in one sentence and broken off in the next.
  - The Zachariah chronicle was not dated as a later compilation.
- Round 2, a targeted recheck, cleared eight councils. It found one new substantial point, Hefele named at Chalcedon without being introduced, and seven minors.
- Round 3 cleared all nine, with four optional minors; three were fixed as wording.

Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**What is still open.** Open-Gaps 246, "Major councils, eras 1 and 2" (2026-11-14). The councils of eras 3 to 10 are not started.

The files are in `Council-Profiles/era1/` and `era2/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era1-2/`. No census, record or site change is made, so there is no data release number. Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Who profiles, era 3 batch 4: ten profiles, four majors, Theodosius I's own letters found (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 3, in order of death or last attested year as the scan gives it: Victor of Tunnuna, Theodosius I of Alexandria, Gildas, Jacob Baradaeus, Agathias of Myrina, Cassiodorus, Longinus, bishop of the Nobadae, Radegund, John of Ephesus and David of Wales. None is a live person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** Major marks, from the drafter's proposal: Theodosius I of Alexandria, the anti-Chalcedonian patriarch of Egypt through his long exile, after whom the Theodosians were named; Jacob Baradaeus, who ordained the separate Syriac Orthodox hierarchy, and after whom the Jacobites were named; Cassiodorus, whose Vivarium and Institutions set a pattern for monastic copying and study; and Gildas, whose own work is the one British church voice of the century, with his late Lives flagged as late. They run 401 to 405 words, about 2:30. John of Ephesus is not major. He stays a recorder at standard length, to match the Palladius ruling, and his work as bishop and missionary is in the brief. Victor of Tunnuna, Agathias, Longinus, Radegund and David of Wales are not major either. The non-majors run 320 to 326 words, about 2:00. Victor of Tunnuna is a Who as a recorder. Agathias carries the Outside witness label, with his card's Tradition line "Outside the church"; his faith is told as disputed between G. J. Vossius and B. G. Niebuhr. Radegund is judged by what is held in her own words. Her letter to the bishops in Gregory of Tours's History is given as hers. The three poems in her voice are Fortunatus's by every held edition, and the brief says so. Longinus's card name gives his role and the people John of Ephesus names, since no held source gives him a place, as with Julian in batch 2. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting. Round 1, the full checklist review in three parts, found 6 blocking and 63 minor points. Three blocking points were false absences: the year in prison at Chalcedon for John of Ephesus, which Michael the Syrian tells; a birth reckoning for David of Wales, which the Bollandists give in the Acta Sanctorum; and writings of Jacob Baradaeus, whose reply to the Alexandrians Michael gives. The others were Ussher's reading of Gildas's forty-four years told as Gildas's own words; the partisan witnesses for Theodosius left unmarked, and the order of his ordination told as settled; and the History of the Patriarchs misreported on his years in Upper Egypt. The minors were mostly an editor's view or year told as settled, disputes given one side, common names without a place, English words in quotation marks for a Latin or French source, and process words on cards. Round 2, a targeted recheck, found 66 of the 69 resolved and 3 partly, 1 new blocking point and 8 new minors, all fixed. The blocking point was a false absence for a year of the synod of Brefi, which the Bollandists report as Spelman's and Ussher's 519. Round 3, the last, found the batch clear, with two minor points on sentence length in two cards, fixed as worded. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Most of the scan's years for these ten rest on no held line or only on a Library file header. The scan's "no work of his own is held" for Theodosius I is wrong: two of his letters are held in English. Agathias's "Vita" is Niebuhr's of 1828. Victor of Tunnuna's Balearic Islands are Mommsen's correction. Several leads point to footnotes, editors' bridges or contents pages. Details are in Open-Gaps 247.

**What is still open.** Open-Gaps 247, "Era 3 Who batch 4" (2026-11-14). The remaining era 3 WHO rows: 16 from the era 3 scan (26 after batch 3, less these ten) and 21 from the supplement scan, 37 in all.

The approved files are in `Who-Profiles/era3/batch4/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch4/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of the Venantius Fortunatus card, era 3 Who batch 5

**Cap ruling (2026-11-14, Mark: "One targeted check", picked from options, relayed by the coordinator).** The third and last review round of era 3 Who batch 5 found one blocking point, on the Venantius Fortunatus card: it said Gregory of Tours calls him a priest each time he names him, where Gregory's prologue to the first book of the Virtues of Martin names him with no title. The reviewer's fix was applied: "Gregory of Tours calls him a priest and never bishop." Mark ordered one targeted Opus check of that card sentence and its two records strings, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch5/R4_cap-check.md`. Its verdict was NOT CLEAR, with no blocking point. The card sentence passed: in both of Gregory's held texts he calls Fortunatus a priest wherever he gives a title, and never bishop. The contested-claim side passed. The records claim failed on two minor citation points, with its substance right: it named the Virtues of Martin I.13 without a line and cited a line from the Glory of the Martyrs, a work it did not name; and it cited the prologue quotation to one line where it runs over two. Both were fixed as worded, and the participant text did not change. The coordinator treated the cap ruling as met (2026-11-14), since a minor finding needs no further round. Then, on Mark's question "Do we need the never a bishop? Is that relevant to the perspective or an ai tell", the coordinator dropped "and never bishop" from the card and the records: the card now reads "Gregory of Tours calls him a priest", the part the cap check confirmed.

## 2026-11-14 — Who profiles, era 3 batch 5: ten profiles, four majors, Evagrius Scholasticus placed with the imperial church (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The next era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, after batch 4, in order of death or last attested year as the scan gives it: Evagrius Scholasticus, Gregory of Tours, Dorotheus of Gaza, Columba, Leander of Seville, Venantius Fortunatus, Reccared, Henana of Adiabene, Augustine of Canterbury and Baudonivia. Gregory the Great falls in the same years and is skipped as a live person entry. Dorotheus of Gaza is placed at 596, by Migne's heading on Andrea Gallandi's notice. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).** Major marks: Columba, who founded Iona, from which Bede says many houses in Britain and Ireland grew; Augustine of Canterbury, who led Gregory's mission to Kent and was first archbishop of Canterbury; Leander of Seville, who with Reccared brought the Visigothic kingdom to the Nicene faith at the Third Council of Toledo; and Reccared, whose own confession there is held. They run 396 to 404 words, about 2:27 to 2:30. Gregory of Tours stays at standard length as a recorder, to match the Palladius and John of Ephesus rulings, and his bishopric is in the brief. Evagrius Scholasticus, Dorotheus of Gaza, Venantius Fortunatus, Henana of Adiabene and Baudonivia are not major. The non-majors run 324 to 325 words, about 2:00. Evagrius Scholasticus, Gregory of Tours and Baudonivia are Whos as recorders. Reccared stays a Who on Mark's named ruling for rulers, "Story unless own voice": the acts present the tomus as the king's, and O. M. Dalton's note that Leander composed the speech is given as Dalton's. Evagrius Scholasticus's card tradition reads "The Byzantine Imperial Church (Justinianic)", correcting the scan's "Syriac Orthodox", since he writes for the side that held to Chalcedon as adviser to Gregory of Antioch. Henana of Adiabene's brief says the teaching he was condemned for is known only through his opponents, and that a pupil's praise of the man survives: Barhadbeshabba wrote under him, and Addai Scher reports treatises of his own surviving outside the Library. His specific charges rest on Babai the Great alone, and the synods' references to him are inferred by their editors. The 2:30 is a cap, not a target.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in three parts, found 11 blocking and 46 minor points. The blocking points were false absences (the Annales Cambriae, held, for Columba; Venantius Fortunatus's poem for the council that tried Gregory of Tours; Scher's report of Henana's own treatises); Huyshe made a doubter of a link his own note asserts (Columba); two of Bede's meetings merged into one (Augustine); a misread year (Evagrius's losses in the plague; Turchi's 584, which dates Leander's bishopric, not his exile); a disputed point told one way (Sabrisho's part, for Henana; the relic of the Cross at Poitiers, for Baudonivia); the editors of Gregory's Register put among the doubters of the letter in Reccared's name, which they answer; and an identification Dorotheus states himself tagged as an inference. Round 2 found all 11 resolved, 2 new blocking points and 15 minors. The blocking points were Arndt's reckoning of Gregory of Tours's consecration year told backwards on the card, and a judgment credited to Paul Ewald and Ludwig Hartmann together, where the held volumes say Hartmann edited them after Ewald's death. Round 3, the last, found nine profiles clear, 9 minor points, and 1 blocking point on the Venantius Fortunatus card, all fixed as worded; Mark's cap ruling above settles the last. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Most of the scan's years for these ten rest on no held line or only on an editor's reckoning, and Evagrius Scholasticus's church is misplaced. Details are in Open-Gaps 248.

**What is still open.** Open-Gaps 248, "Era 3 Who batch 5" (2026-11-14). The remaining era 3 WHO rows: 6 from the era 3 scan (16 after batch 4, less these ten) and 21 from the supplement scan, 27 in all.

The approved files are in `Who-Profiles/era3/batch5/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch5/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).


## 2026-11-14 — Eras 1 and 2 on the live tree: 75 Who profiles and 9 major councils (Mark, 2026-11-14; data release 41)

**Decided (Mark, 2026-11-14, his words as given or relayed).** The job: eras 1 and 2 "fully built" with "every feature working" on the live tree. Councils: "counsels are treated like a tradition with a different icon and title. but people who are a part of it should be on the who click". He saw a local-build preview (https://claude.ai/artifact/SS4Aq6bVYsZXvrqMY6ys9T) and approved it: "Aprove". The worker's recommendation on each of the preview's ten questions stands as approved. On the profile control, relayed by the coordinator: "as i look at it we dont need both the who and the profile on the page, it is double points for the same action, lets remove the profiles and just leave the who, one for a river that opens all the who on the river in that era, and one near the tradition".

**What went in.** 75 person entries (20 era 1, 55 era 2) from `Who-Profiles/era1/batch1-3` and `era2/batch1-6`, and 9 major-council entries from `Council-Profiles/era1` and `era2`. Each person has the brief as its text, the card, a tree page and a place in its tradition's Who and its river's Who; 68 are told within a tradition and 7 within none. The 31 voice rows in the traditions that named these people became links to the entries. There is no audio player on any of them; a player shows only when a recording of the current text exists, so recordings added later need no layout change (recording stays on hold, Open-Gaps 218).

**Schema (backward compatible; documented in the census notes field).** New `kind` "major-council", with a new status "Major council"; a `council` object (rivers, knownFor, datesNote, calledBy, issue, attended, decided, outcome, record with each witness's kind, traditions in four groups, uncertain, sources in three groups); a council's `people` list is its Who, with items {person, part} or {name, verdict, part}; new optional card keys otherNames, label ("Outside witness"), datesNote and placeNote, and author and date on "their own words" sources. The validator checks all of it. It also now checks that every quotation in a person's or council's text stands word for word in a file the entry cites under `cic/texts/`. The check reads each file once. It tolerates footnotes the brief quotes, page-anchor and page-number breaks in a scan, and hyphen line-breaks; the schema tests run it with `--skip-quotes`, and CI runs the full check. The CI step that fetches the vendored texts now also fetches the files the cards and councils cite.

**Calls settled by the approved recommendations.** Card traditions that are other forms of a site tradition use that tradition. Arius is told within Homoian ('Arian') Christianity, Epiphanius of Salamis within Early Palestinian Ascetic Monasticism, Socrates of Constantinople within Novatianism. Sozomen and Olympias are told within none, in the Greek East river. Josephus, Tacitus, Suetonius and Pliny the Younger sit in the Origin river, and Ammianus Marcellinus in Latin West. The four "record, not party" cards (Marcellus, Marius Mercator, Prosper, Eutyches) stay as the profiles have them. On a council's Who, a person with no verdict shows in plain words: "Profile to come", "Told in a story", "Listed", "Not yet assessed". Councils sit in a "Major councils" column left of the rivers, with ties to the traditions they touched drawn on open. The 217 caps, major mark and "more" click are carried, not built here. Places with no census row show their name with no "today in" country, and no id is invented.

**The map's Who controls.** The person-icon profile pill beside each tradition is replaced by a "Who" pill, so Who is the one control: one per river per era and one beside each tradition. Person cards show the careful dates and place of the profile and the "Outside witness" label, and list the councils the person attended.

**Quotation check, what it found.** Of 26 quotations that first failed, 22 were faults in the check (markup stripped from plain-text scans, footnotes the briefs quote, page anchors inside words, scan page numbers, hyphen breaks). Three needed a source added to a card, in the sources list only: Alexander of Alexandria (Philostorgius, Walford) and Eznik of Kolb (Burkitt's introduction in Mitchell's Ephraim, for both quotes). One was a suspected wording error on the Athanasius card. The coordinator relayed Mark's pick, "Fix now, audio returns later", then a fresh Opus recheck found the original wording word for word at lines 5392-5394 of Pusey's English, broken across a line by a hyphen ("all-cele-/brated"). The brief and the voices line stay as they were, and his recording is untouched. No quotation was changed or had its marks dropped.

**Wording changed (listed for the Opus recheck).** The project's spelling check (Decision-Log 77) flagged 76 words in the new entries' own prose, and the profile files were mirrored (51 words in 35 files, 21 briefs; two titles the Opus recheck caught, "On the Advent of Our Saviour" and "the Liberian Catalogue", were put back and added to the checker's list of names). All are British to American spellings (defence, honoured, summarises, rumours and the like); no quoted span and no title of a work was changed. "Defence against the Arians", "Defence of Dionysius" and "Refutation and Defence" now sit in the checker's list of names with a British spelling. A fresh Opus agent rechecked every changed line: no quoted span changed, no meaning changed, and its two title findings are fixed as above.

**Also changed.** `engine.m6` atlas sync now takes a field out of the map's copy when the census no longer holds it (a tradition that gained people loses its `peopleNote`), with tests. The data page and its citation examples show release 41 (14 November 2026). Release 41 follows release 40 (PR #1621).

**What is still open.** Open-Gaps 249. Open-Gaps 217 (caps, major mark, placement) is carried. The 17 council people with no Who scan verdict stay "Not yet assessed" (246).

Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Major councils, era 3: three profiles (Mark's instruction, through the coordinator)

**Decided (Mark, 2026-11-14; his words as given).** The scope: "do the major counsils for era 3 also". The three are the era 3 rows of the councils scan (`Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/Councils_Scan.md`): the Second Council of Constantinople (553), the Third Council of Toledo (589) and the Council of Dvin of the Armenian–Georgian break. Each is written to `Council_Profile_Pattern.md`, in the form of the era 1 and 2 councils.

**The three councils.**
- Constantinople 553: 400 words, FK 8.1, reading ease 60.2. The Library holds only English extracts of the acts; the losing side speaks in Vigilius's Constitutum and Facundus, both in Latin, and in Victor of Tunnuna.
- Toledo 589: 400 words, FK 7.0, reading ease 68.7. The acts are held in Latin with the signatures; every witness is Catholic, and the Homoian view reaches us through the acts' anathemas, John of Biclaro and Gregory of Tours's report of the envoy Agilan.
- Dvin: 371 words, FK 7.7, reading ease 61.8. No record of the council or letter of its two church heads is held; among the held writers only modern ones tell of a synod at Dvin, and the year is told as between 596 and 609, with Brosset's 596 and Ormanian's 609 named.

**Worker's calls under the pattern (not Mark's words; Mark may overrule).** The Who click lists those who took part, those condemned, and those who acted on the council's decisions; writers who only report a council are in its record and sources. The Dvin id keeps 609, the year of the census and the scan, with the dispute told in the entry. American spelling in the profiles' own prose, as Decision-Log 77 and the eras 1 and 2 live release require; quotations keep their own spelling. Opus drafted every profile.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting.
- Round 1, the full review, found no blocking points, 5 substantial and 21 minor. The substantial points: the Church of the East's synod of 585 was told as an answer to the council, a link that is only Jérôme Labourt's reading; Michael the Syrian's account was missed and an absence claimed; Kyrion's side was said to reach us only through foes, though his one witness, Issaverdens, favors him; the Dvin brief opened on Stephen of Taron's anathema as if it were the council's scene, without saying that only modern writers tell of a synod; and the editors of Gregory's letter to Quiricus were misread.
- Round 2, a targeted recheck, cleared Constantinople and Toledo and found one new substantial point on Dvin, a second false absence (Brosset cites the medieval historians Kirakos and Ukhtanes for the council), with four minors.
- Round 3 cleared all three, with three optional minors, taken as wording.

Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**What is still open.** Open-Gaps 250, "Major councils, era 3" (2026-11-14). The councils of eras 4 to 10 are not started.

The files are in `Council-Profiles/era3/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_council-profiles-era3/`. No census, record or site change is made, so there is no data release number; councils reach the site through the map build.

## 2026-11-14 — Cap ruling: one check of three round 3 fixes, era 3 Who batch 6

**Cap ruling (2026-11-14, Mark: "One targeted check", picked from options, relayed by the coordinator).** The third and last review round of era 3 Who batch 6 found three blocking points. None was in a brief or an audio script. The first was in the Babai the Great records, the batch 5 Henana of Adiabene note and Open-Gaps: round 2's fix counted Oskar Braun's omissions from his German Life of George as three passages, where his footnotes show the introduction shortened, four passages passed over and two more given only as notes. The second was in the Ruricius of Limoges records: an era variant for the council of Agde was cited from Bruns's apparatus to the second council of Vaison. The third was in Open-Gaps: Constantius of Lyon was said to be named nowhere in the census, where the Germanus of Auxerre and Hilary of Arles entries name him. The fixes were applied as worded, with one Babai card sentence that went with the first. Mark ordered one targeted Opus check of those fixes and that sentence, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch6/R4_cap-check.md`. Its verdict was NOT CLEAR, with one blocking point. The Agde fix and the census list-line fix passed, and so did the card sentence. The new count of Braun's omissions was still wrong: Braun gives three passages only as notes, not two, and the one missed is his note on three longer prayers before the crucifixion (braun1915 l.14995-14996). Four minor points were found: Chabot gives three passages of the Life in French, not two; a comma was missing; two OCR readings in the Agde quotation were unflagged; and one census clause named era 1 for era 2.


## 2026-11-14 — Second cap ruling: Braun's omissions listed by line, one last check, era 3 Who batch 6

**Cap ruling (2026-11-14, Mark: "List the lines, one last check", picked from options, relayed by the coordinator).** The count of Braun's omissions had been wrong twice, so a third count would have been a fix on a fix. The count was dropped everywhere it appeared: in the Babai the Great records claim and absent detail, the batch 5 Henana of Adiabene note and Open-Gaps 251. Each now says Braun "shortens the introduction and leaves out or sums up several passages" and gives his eight notes by line (braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947, 14995-14996). The card sentence already said this and had passed. The four minor points were applied as worded. One more Opus check of only those changed strings, by an agent that had not seen the drafting or the earlier rounds, does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch6/R5_cap-check.md`. Its verdict was NOT CLEAR on one minor point only, with no blocking point: every changed string states what its source lines hold, all eight ranges are Braun's own notes, and none is missing. Three of the changed sentences ran past 25 words, and one clause read ambiguously. All three were fixed as worded, and the cap ruling is met.

## 2026-11-14 — Who profiles, era 3 batch 6: ten profiles, three majors, Benjamin I to era 4, Ruricius of Limoges in his place (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The last five era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era3/Who_Scan_Era3.md`, as cleaned in `2026-11-12_who-scan-dedupe/`, in order of death or last attested year as the scan gives it: Columbanus, John Moschus, John of Biclaro, Babai the Great and Isidore of Seville. Then the first era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/` by best held date: Constantius of Lyon, Severinus of Noricum, Faustus of Riez, Gennadius of Marseilles and Ruricius of Limoges. None is a live person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Benjamin I of Alexandria goes to era 4.** The History of the Patriarchs heads his entry 622 to 661, and his patriarchate, his flight from Cyrus and his return under 'Amr all fall after 622, so the dedupe's date-of-work rule puts him in era 4. Ruricius of Limoges, the next supplement row by best held date, took his place. Theopistus, whose row is earlier but rests on no held date and holds nothing about the man, goes to the end of the era 3 list for a check on whether he can be written at all.
- **Major marks, as the worker proposed.** Columbanus, who founded Luxeuil and Bobbio, and whose Rule, Penitential, sermons and letters are held. Isidore of Seville, Leander's successor at Seville and author of the Etymologies, who signs first at the Fourth Council of Toledo. Babai the Great, abbot of Izla, who helped govern the Church of the East while it had no head and whose teaching on the union in Christ it kept. They run 403 to 405 words, about 2:30. The other seven are not major and run 323 to 325 words, about 2:00. John Moschus, John of Biclaro, Constantius of Lyon and Gennadius of Marseilles are Whos as recorders at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours. The 2:30 is a cap, not a target.
- **Severinus of Noricum's card tradition** reads "Early Benedictine / Italian Monasticism" only. The supplement scan also places him in Gothic, Vandal and Lombard Homoian Christianity, but he was Catholic, and that placing comes only from the Rugians he lived among. Logged in Open-Gaps.
- **A correction to batch 5.** One records note on Henana of Adiabene said Babai's Book of the Union was "not held". It is held in part, as J. Labourt quotes it in French, and Babai's Life of George is held in J.-B. Chabot's French passages and Braun's German. That note was corrected in this batch's pull request and checked in every review round. Batch 5's brief and card are unchanged, and the point that the charges rest on Babai alone still holds.
- **Empty `date` keys.** Round 2 asked for one ruling on `"date": null` in card sources. The worker ruled for the batch README, "A field with no content is left out", and removed all 31.
- **American spelling.** The new prose follows the project's spelling rule (Decision-Log 77), as main's era 3 council profiles do.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in three parts, found 14 blocking and 54 minor points. The blocking points included false absences (the PL 80 works of Columbanus; Redemptus's account of Isidore's death, retold by Poschmann; Mari and 'Amr on Babai; Braun's German Life of George), a Toledo IV canon on Jews turned into a general rule against forced belief, Seville II's 619 told as settled where Pagi's held note argues 618, the end of John of Biclaro's Chronicle misplaced, a rendered quotation from Columbanus that dropped a condition, Babai made abbot before any source has him so, two namesakes split where a held chronicle makes them one, Scher's year given to the Chronicle of Seert, Krusch made to disagree with Levison where his own Addenda reverse him, Sidonius's reading of Faustus's books placed at Clermont, and Ruricius's "harsher food" told as real food. Round 2 found all resolved but two partly, 1 new blocking point (Braun's Life of George called "whole") and 14 minors, all fixed. Round 3, the last, found 3 blocking and 8 minor points, all fixed as worded. Mark's two cap rulings above settle the blocking ones. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Most of the scan's years for these ten rest on a Library file header or an editor's note; several leads point to the wrong man or say "not held" where the Library holds the text. Details are in Open-Gaps 251.

**What is still open.** Open-Gaps 251, "Era 3 Who batch 6" (2026-11-14). The era 3 scan rows are now all written or moved, Benjamin I to era 4. The supplement scan's era 3 WHO rows not yet written: 16, in order of best held date to be set by the coordinator: Fulgentius of Ruspe, Boethius, Philoxenus of Mabbug, John Climacus, Primasius of Hadrumetum, Eugippius, Marius of Avenches, Barhadbeshabba 'Arbaya, Brendan of Clonfert, Ciaran of Clonmacnois, Dionysius Exiguus, Avitus of Vienne, Martin of Braga, Liberatus of Carthage and John of Beth Aphthonia, with Theopistus last.

The approved files are in `Who-Profiles/era3/batch6/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch6/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of the post-round-3 correction, era 3 Who batch 7

**Cap ruling (2026-11-14, Mark: "One check each (Recommended)", picked from options, relayed by the coordinator).** A round 3 fix to the John of Beth Aphthonia brief added "John of Ephesus names another monastery of Aphthonia, at Charrhae." The worker applying the card fixes flagged it, and the drafter confirmed against the file: in John of Ephesus's list of consecrations each city is the man's see, so Charrhae is where Sergius, "from the monastery of Aphthonia", was made bishop. The drafter removed the sentence, rewrote the card's "Beth Aphthonia and Kenneshre" item and the records to match, and restored the brief's sentence on John bar Aphthonia's record of the debates ("which the chronicles mention but do not give"). Mark ordered one targeted Opus check of those changes, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch7/R4_cap-check.md`. Its verdict was NOT CLEAR, with no blocking point. The brief paragraph, the removal, the audio and the readability passed; John of Ephesus's parallel list says it outright ("Sergius in the city of Charrhae, from the monastery of the house of Aphthonia"). Three minor points were fixed as worded: a card spelling ("the monastery of Bar Aphthonia, called of Kenneshre"), a records quotation given in the scan's OCR form, and a line number. The participant text of the brief did not change.

## 2026-11-14 — Who profiles, era 3 batch 7: eight profiles, three majors, John of Beth Aphthonia as the Life's author (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The first eight of the fifteen remaining era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`, by best held date of death or last mention: Avitus of Vienne, Philoxenus of Mabbug, Boethius, Fulgentius of Ruspe, Eugippius, John of Beth Aphthonia, Ciaran of Clonmacnois and Primasius of Hadrumetum. Primasius, last seen at his signature in May 553, comes before Dionysius Exiguus, whom William Cave's notice has dead before 556. None is a live person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Major marks.** Boethius, whose treatises gave Latin theology its terms on the Trinity and on person, and whose Consolation of Philosophy is his own voice from prison; Philoxenus of Mabbug, the leading Syriac writer of the church that refused Chalcedon, bishop of Mabbug from 485 by Budge's date and exiled under Justin, whose Discourses are held; Fulgentius of Ruspe, the leading Catholic voice in Vandal Africa, exiled to Sardinia, who answered King Thrasamund. They run 400 to 405 words, about 2:30. Avitus of Vienne is not major: an important bishop, but he shapes no river of his own, and keeping the mark scarce keeps it meaningful; his letter to Clovis and his dispute with Gundobad are in the brief. Eugippius, John of Beth Aphthonia, Ciaran of Clonmacnois and Primasius of Hadrumetum are not major either. The non-majors run 323 to 325 words, about 2:00. The 2:30 is a cap, not a target.
- **John of Beth Aphthonia** is one Who, as the author of the second Life of Severus of Antioch, under the recorder rule. Whether he is the archimandrite John bar Aphthonia of Kenneshre is stated plainly and kept as a contested claim: M.-A. Kugener calls the attribution false, and J.-B. Chabot, Rubens Duval and E. W. Brooks write of the Life as bar Aphthonia's. Bar Aphthonia's facts are kept apart and given as his.
- Eugippius is a Who as a recorder. Ciaran of Clonmacnois is a founder known through a late Life, which the brief marks as a saint's Life and the house's own telling. Primasius's surrender and death are known only from Victor of Tunnuna, who wrote against him; Heinrich Kihn's warning that Victor wrote as a party man is in the brief.
- **Card traditions.** Fulgentius of Ruspe is told within Gothic, Vandal & Lombard Homoian Christianity, as the Victor of Vita card is, since the census has no movement for the Catholic church of Vandal Africa. Boethius keeps the scan's first placing, The Byzantine Imperial Church (Justinianic), though he died before Justinian's reign; that goes to the placing (Open-Gaps 252).
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Before review, a card-drafting pass checked every brief sentence against its source and found and fixed 21 slips. Round 1, the full checklist review in three parts, found 7 blocking and 49 minor points. The blocking points: a catalog of saints not in the Roman Martyrology read as the Roman Martyrology (Boethius); Michael the Syrian's "first" version of the New Testament heard as the first ever made (Philoxenus); years of the Greeks given with no era, and a catalog heading told as the text of a pottery fragment (John); Kihn given a reading of Victor's monastery he does not hold (Primasius); and, for Ciaran, the Lismore Life misreported on his teachers and his first house, and a false absence (Tirechan also tells his baptism by Justus). The minors were mostly common names without a place, an editor's year or view told as settled, and dropped hedges. Round 2, a targeted recheck, found all 7 resolved, 0 new blocking points and 15 minors. Round 3, the last, found 0 blocking and 11 minors, all applied. One round 3 fix carried a misreading (a second monastery of Aphthonia at Charrhae, where John of Ephesus names Charrhae as a bishop's see); the fix worker caught it, the drafter confirmed it against the file and corrected brief, card and records. Mark's cap ruling below settles the correction. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Most of the scan's years for these eight rest on a Library file header; one header merges two men. Details are in Open-Gaps 252.

**What is still open.** Open-Gaps 252, "Era 3 Who batch 7" (2026-11-14). The supplement scan's era 3 WHO rows not yet written, for batch 8: Dionysius Exiguus, Liberatus of Carthage, Brendan of Clonfert, Martin of Braga, Marius of Avenches, Barhadbeshabba 'Arbaya and John Climacus, with Theopistus set aside for a separate check.

The approved files are in `Who-Profiles/era3/batch7/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch7/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of the round 3 fixes, era 3 Who batch 8

**Cap ruling (2026-11-14, Mark: "One check each (Recommended)", picked from options, relayed by the coordinator).** The third and last review round of era 3 Who batch 8 found one blocking point. The Brendan of Clonfert card said the Annales Cambriae's "editor takes" their Brendan "Byror" for Brendan of Birr, a role where the pattern needs a named witness. The reviewer's fix named John Williams ab Ithel, who edited them, and it was applied as worded with the round's 14 minor fixes. Three of those changed briefs: "Gregory's English translator" and the punctuation of the Thomas à Kempis quotation in John Climacus, and "which Liberatus shared" in Liberatus of Carthage. Mark ordered one targeted Opus check of the round 3 fixes, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch8/R4_cap-check.md`. Its verdict was CLEAR, with no blocking or minor point: John Williams ab Ithel is the editor on the Annales Cambriae's title page and gives Byror as Birr in his preface; each minor fix says what its source lines say, with its witness attached; the Thomas à Kempis source has no comma after "John Climacus", so the comma now sits outside the marks; and nothing outside the listed fixes changed. The cap ruling is met.

## 2026-11-14 — Who profiles, era 3 batch 8: eight profiles, two majors, Theopistus written, era 3's Who list complete (coordinator, under Mark's full-auto instruction of 2026-11-13)

**The batch.** The last era 3 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`: Dionysius Exiguus, Liberatus of Carthage, Brendan of Clonfert, Martin of Braga, Marius of Avenches, Barhadbeshabba 'Arbaia of Halwan and John Climacus, with Theopistus checked last. Batch 7 takes the other eight supplement rows. None is a live person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Major marks, as the worker proposed.** John Climacus, whose Ladder, held in PG 88 with Daniel of Raithu's Life, carried Sinai's teaching on the monk's life into Greek, Latin and the New Devotion. Dionysius Exiguus, whose Easter tables counted the years from the Incarnation and whose Latin canons the Roman church used, by Cassiodorus. They run 402 and 405 words, about 2:30. The other six are not major and run 304 to 336 words. Liberatus of Carthage, Marius of Avenches, Barhadbeshabba and Theopistus are Whos as recorders, by the rulings for Palladius, John of Ephesus and Gregory of Tours. The 2:30 is a cap, not a target.
- **Theopistus is written.** The scan said nothing about the man is held. In fact, the History of Dioscorus is told in his own voice and calls him the deacon of Dioscorus. François Nau argues that the text we have was reworked after 512 by a writer of Peter the Iberian's school. The profile puts that view at its center, tells the narrator's account as the book's, and runs to the length his one held source carries, about 1:50.
- **Two Barhadbeshabbas kept apart.** The profile is the bishop of Halwan who signs the synod J.-B. Chabot dates to 605 and who wrote the Cause of the Foundation of the Schools. The Ecclesiastical History is credited to Barhadbeshabba 'Arbaia of the school of Nisibis, as batch 1's Narsai and Barsauma cards have it, and Nau's view that the two may be one man is given as his. The display name is "Barhadbeshabba 'Arbaia of Halwan", so the two do not collide on the tree; the id is `barhadbeshabba-arbaya`.
- **Card traditions, the worker's calls, accepted.** Dionysius Exiguus in Early Benedictine / Italian Monasticism; Liberatus of Carthage in Latin African Christianity under Byzantium; Martin of Braga in Nicene Visigothic Iberia, since the census has no Suevic movement; Brendan of Clonfert in Insular / Irish Monastic Christianity only. Brendan stays a Who on Adomnan's Life of Columba, by the supplement scan's ruling, and his brief says his Lives are centuries later.
- **American spelling.** The new prose follows the project's spelling rule (Decision-Log 77).

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in five parts, found 14 blocking and 65 minor points. The blocking points:
- **False absences.** Louis Duchesne's charge that Dionysius drew his Nicene Easter rule from a later Alexandrian letter was left out. A Theopistus card line said only two sources name him.
- **Witnesses wrong or missing.** A note signed R. in Arndt's Gregory was given to Krusch. The Chronicle of Seert's "Hadbeshabba 'Arbaya" was made the bishop of Halwan without saying the identification is Addai Scher's.
- **Barhadbeshabba's card.** The History was filed under the bishop's own works. His place came from an Assemani volume the card did not cite. His display name matched batch 1's other man.
- **Sources misread.** John Climacus's brother George was said to die within ten months, where the Bollandists' Latin reads ten years. Garnier's five bishops were all called deposed.
- **Context missing in the briefs.** Martin of Braga had no time anchor. Theopistus had no word of Chalcedon or of Dioscorus's exile.
- **Other blocking points.** A Library header was cited as a source on the Climacus card. The book's account was told as fact for Theopistus. One Dionysius sentence did not parse.

Round 2, a targeted recheck, found all of them resolved, with 3 new blocking points and 17 minors, all fixed. The blocking points were a Dumio dispute that a round 1 fix had created, Hugh Williams counted as a second witness for Adomnan's Brendan, and a false absence of Jean Garnier's first name. After round 2, every card sentence over 25 words was split. Round 3, the last, found seven profiles clear and 1 blocking point on the Brendan card, with 14 minors, all fixed as worded; Mark's cap ruling above settles it. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Most of the years for these eight rest on a Library file header or an editor's reckoning, and two "not held" lines are wrong: Theopistus's own voice, and Barhadbeshabba's life beyond the 605 signature. Details are in Open-Gaps 253.

**Era 3's Who list is complete.** With this batch and batch 7, every era 3 WHO row of the era 3 scan and of the supplement scan is written or moved: Benjamin I of Alexandria to era 4, and Vakhtang I Gorgasali, Vahan Mamikonian and Kaleb of Aksum to STORY.

**What is still open.** Open-Gaps 253, "Era 3 Who batch 8" (2026-11-14).

The approved files are in `Who-Profiles/era3/batch8/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era3-batch8/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Eras 4 to 7 built in full: every Who row whose sources are held (Mark, 2026-11-14)

**Decided (Mark, 2026-11-14, picked from options, relayed by the coordinator).** Eras 4 to 7 of the Church Family Tree are built in full. Every WHO row whose sources are held gets a Who profile, not only the majors. Mark's choice: "Full builds, 4-7 (Recommended)". The era scans for eras 4 to 7 are the lists the batches are drawn from, and a WANTED row waits until its named source is held. The first batch under this ruling is era 4 batch 1. Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Cap ruling: one check of three card fixes, era 4 Who batch 1

**Cap ruling (2026-11-14, Mark: "Apply + one check (Recommended)", picked from options, relayed by the coordinator).** The third and last review round of era 4 Who batch 1 found all eight profiles clear, with no blocking point. Three of its minor fixes were in participant text, all on cards, with no brief or audio change: the Boniface of Mainz card's first key work split a 28-word sentence, keeping Kylie's quotation "We are of one blood and one bone." as it stands; the Nennius card's dates now say that Louis Duchesne calls the writer pseudo-Nennius before placing him in the ninth century; and the Adomnán of Iona card's Easter item puts back "Bede adds" on the "lover of peace" sentence, which a split had cut loose from its witness. Mark ordered the three applied as worded and one targeted Opus check of only those strings, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch1/R4_cap-check.md`. Its verdict was CLEAR, with no blocking or minor point: Kylie's letter has the Saxons themselves say the words, and the quotation is word for word; Duchesne calls the writer "pseudo-Nennius" and dates him to the ninth century; and "Bede adds" ties the sentence to Bede V.15. Each string runs 21 words or fewer. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 1: eight profiles, eight majors, Cuthbert's letter on Bede's death found (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** The first eight WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md` whose Major column proposes yes: Bede, Boniface of Mainz, Aidan of Lindisfarne, Hild of Whitby, Adomnán of Iona, Alcuin of York, Dhuoda and Nennius. None was written before. Bede is a live census person entry; his profile keeps the census id `bede-of-jarrow`, and the census is not changed. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Major marks.** All eight are major, as the scan proposed: these are river-level figures. Seven run 402 to 405 words, about 2:30. Nennius keeps the mark but is a recorder with a thin held life, so his brief runs near standard length, 340 words, about 2:06. Bede is also a recorder, but his own closing statement, his list of works and Cuthbert's letter on his death carry the full length. The 2:30 is a cap, not a target.
- **Bede and the live entry.** The profile agrees with the live entry except where the held lines differ, and those points go to Open-Gaps for a census fix: the Gospel of John at the deathbed and the age at death are L. Cecil Jane's, the year 735 is disputed, the Biographical Notice is Jane's, and the "sell Christ" line comes from Arnold's Select English Works volume 3.
- **Nennius.** His authorship of the Historia Brittonum is attributed, and the brief says so plainly in its second paragraph, with the witnesses on each side: the book's own prologue, Hugh Williams and W. H. Stevenson for him; Louis Duchesne and James Raine, who call the writer pseudo-Nennius, the heading that gives the book to Mark the anchorite, and copies that give it to Gildas. The card name is plain "Nennius"; the work's author line reads "Nennius (attributed)". The doubt is over who wrote the book, not over his name.
- **Names and ids.** "Boniface of Mainz", `boniface-of-mainz`, since popes of the name are in the census; "Adomnán of Iona", as the census and the era 3 Columba card spell it.
- **Card traditions, the worker's calls.** Aidan of Lindisfarne in "Anglo-Saxon Christianity; Insular / Irish Monastic Christianity", since both movements cover his years and name him. Adomnán of Iona in "Medieval Irish Christianity; Insular / Irish Monastic Christianity", Medieval Irish first by his years as abbot. Boniface of Mainz in "Anglo-Saxon Christianity", which lists him and covers his life.
- **Dhuoda** stays a Who under the women ruling: she taught, in writing, through a handbook for her sons. The brief says plainly what she did.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in four parts, found 11 blocking and 68 minor points. The blocking points:
- **False absences.** The census Lollard line on selling Christ was marked not held; it is in Arnold's Select English Works volume 3.
- **Sources misread or softened.** Plummer's "sad" was tied to the wrong sentence of Bede (Aidan). Carloman's promise to correct "something" was told as a promise to set right the church's order (Boniface). Dhuoda's "if God wills" was dropped from her prayer.
- **Contested claims told as settled.** The timing of Cuthbert's vision of Aidan's soul was told from one Life only.
- **Witnesses wrong or missing.** Alcuin's "master" read as Charlemagne, where Mabillon names his teacher Ælberht. The Nennius card cited an edition no held line supports.
- **Counts.** The Hild card miscounted Bede's chapters on her.
- **Writing and form.** A Dhuoda sentence stated her classification and told nothing. The Nennius card carried process narration, and listed "pseudo-Nennius" as another form of his name.

Round 2, a targeted recheck in two parts, found Boniface and Alcuin clean and the rest resolved but two partly, with 1 new blocking point (a Dhuoda sentence split so that her conditional prayer read as fact) and 13 minors, all fixed. Round 3, the last, found all eight clear, with no blocking point and seven minors. Four were in the README and notes and were applied; three were card strings, and Mark's cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Cuthbert's letter on Bede's death is held in Plummer 1896, against the scan's "not held". Adomnán's On the Holy Places is held in PL 88. Hild has a second witness in Stephen's Life of Wilfrid. The Alcuin file holds PL 101 only, without the letters. Several of the scan's years rest on Library file headers. Details are in Open-Gaps 254.

**What is still open.** Open-Gaps 254, "Era 4 Who batch 1" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch1/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch1/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Era 3 on the live tree: 76 Who profiles and 3 major councils (Mark, 2026-11-14; data release 42)

**Decided (Mark, 2026-11-14, through the coordinator).** He saw a local-build preview (https://claude.ai/artifact/A1K3p6vHGqX4om7mwrAXk4, version 2) and approved it: "Approve". The worker's recommendation on each of the preview's four questions stands as approved; the coordinator had accepted each one before Mark's approval. The job, as the coordinator gave it: era 3 on the live tree as data release 42, the same way as release 41, with Open-Gaps 247, 249, 251, 252 and 253 folded in.

**What went in.** 76 person entries from `Who-Profiles/era3/batch1-8` and 3 major-council entries from `Council-Profiles/era3`. Each person has the brief as its text, the card, a tree page and a place in its tradition's Who and its river's Who; 71 are told within a tradition and 5 within none. 31 voice rows in the traditions that tell these people became links to the entries (Barsanuphius and John, two rows, became their one paired entry). Dioscorus of Alexandria now links from the Chalcedon council's Who, and Primasius of Hadrumetum from Constantinople 553's. There is no audio player on any of them (recording stays on hold, Open-Gaps 218). Every rule of release 41 carries over: the schema, the controls, the validator, the quotation check and the spelling method.

**Placings.** Approved on the preview's question 2, settling Open-Gaps 242 and 252. Boethius is told within no tradition, in the Latin West river: he died in 524, before Justinian's reign, which the scan's placing assumed, and no census tradition is the Catholic church of Ostrogothic Italy. Victor of Vita and Fulgentius of Ruspe are told within no tradition, in the Africa river: the Homoian entry of the Vandal kingdom, which their cards named, would set two Nicene bishops in the river labeled "Non-Nicene Traditions", which review round 1 found misleading. Procopius of Caesarea and Agathias, the two outside witnesses, are told within none in the Greek East river, as Ammianus Marcellinus is in the Latin West. Columbanus is told within Insular / Irish Monastic Christianity (Bangor, and the scan's first placing), Faustus of Riez within Gallic Monastic-Ascetic Christianity (abbot of Lérins), and Samson of Dol within British and Welsh Christianity (the census has no Breton movement). The worker's calls that follow the batch cards, which Mark may overrule: Constantius of Lyon in British and Welsh Christianity, as the writer of Germanus's British mission; Gennadius of Marseilles in Gallic Monastic-Ascetic Christianity, the Lérins and Marseilles line, though its census span ends at 450.

**Short dates, map years and places.** The build wrote each person's short dates line from the card's own dates note, and the review checked each against it. Where the sources give no year, the map year is the Who scan's or the Library file's, as in release 41 (Open-Gaps 255). A place label names at most two places; ids are copied only from census rows, so many towns show their name with no "today in" country.

**Quotations.** Of 36 quotation failures in the first run, none was a misquotation. Many were faults in old scans: misread letters, a dropped space, a word broken across lines without a hyphen, and running heads or footnotes inside a sentence. They are now written down as 13 readings, by file and line, in `tools/quote_scan_readings.json`, with what the printed page reads; a dropped range must hold exactly the lines it declares. One needed two held sources on the Victor of Tunnuna card, the notes in the Ante-Nicene and Nicene Fathers that call him "Victor of Tunis". Fourteen are the profiles' own English of a Latin or French line. Approved on the preview's question 1: they keep their quotation marks, with "in modern words" beside them. They are listed by entry, span and original in `tools/quote_renderings.json`; the check skips exactly those spans and fails when one no longer stands in its entry. Review round 1 checked each against its original, clause by clause. Six profiles had renderings with no such mark, or quotation marks on words that were not quotations. Babai's and John Moschus's renderings are now marked and listed. Victor of Vita's and Moses of Khoren's now quote the original ("nostrae civitatis", "nouveau Platon"); Zachariah's name form lost its quotation marks; and the Caesaria card now says plainly which letter greets her as a holy sister.

**Fixes folded in (old and new text in the audit's `Census_Text_Changes.md`).**
- Open-Gaps 247: the David line of British and Welsh Christianity no longer gives a death "around 589" or the patron-saint title, which no held line carries; the annals give 588 or 601. The Gildas line no longer calls him "the only substantial contemporary British voice". The Julian and Benedict voices lines now agree with their new cards.
- Open-Gaps 249: Dioscorus is a person entry, linked from Chalcedon.
- Open-Gaps 251: John of Biclaro's "Maccurritae" are no longer read as the Makurians without question; Theodor Mommsen, his editor, thought them a people of Mauretania. Isidore no longer "presides" at Toledo IV; his name stands first among its signatures. Faustus is no longer "the first abbot of Lérins".
- Open-Gaps 252: Boethius and Fulgentius, as above.
- Open-Gaps 253: the Ladder is no longer said to be read every Lent; Liberatus is no longer cited for Reparatus's deposition; the Nisibis story of the Church of the East now gives each event to the witness that holds it, and drops a governor's protection no held line gives. The Dioscorus records note now names the Arabic and Ethiopic synaxaries.

**Wording changed (listed for the Opus recheck).** American spelling in the profiles' own prose, about 40 words; no quotation and no title of a work changed. "Catalogue of the Saints of Ireland", "Catalogue of writers" and "Catalogue of Abdisho" are now in the spelling check's list of names. The rendering marks and the card sentences above.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round. Round 1, the full review, found 2 blocking points (Victor of Vita and Fulgentius in the Non-Nicene river; a governor's protection in the Nisibis story that no held line gives), 8 substantial and 10 minor. Round 2, a targeted recheck, found no blocking point, 4 substantial (a verb, Philoxenus's dates line, the Ladder's "him", and Labourt's reading set against the Chronicle) and 6 minor. Round 3 approved it to proceed, with 3 minor points taken as wording. Every changed line of participant text was checked, including for AI tells and generic voice. Every quotation was checked against its vendored file. No paid calls were made.

**Also changed.** The data page and its citation examples show release 42 (14 November 2026). Release 42 follows release 41 (PR #1647).

**What is still open.** Open-Gaps 255. Open-Gaps 217 (caps, major mark, placement) is carried.

Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Minor round 3 fixes to reader-facing text get one targeted check without asking Mark (Mark, 2026-11-14)

**Decided (Mark, 2026-11-14, picked from options, relayed by the coordinator).** Mark chose "Check, and make it standing (Recommended)". The option read: "Apply the four as worded, plus one targeted Opus check of only those strings. From now on, minor round 3 fixes to reader-facing text get the same treatment without asking you. A blocking point open after round 3 still comes to you." From now on, a Who batch whose third and last review round finds only minor points in reader-facing text applies them as worded. One targeted Opus check of only those strings follows, by an agent that has not seen the drafting or the earlier rounds. That check does not count toward the cap. A blocking point open after round 3 still goes to Mark for a cap ruling. Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Cap ruling: one check of four round 3 fixes, era 4 Who batch 2

**Cap ruling (2026-11-14, Mark: "Check, and make it standing (Recommended)", picked from options, relayed by the coordinator).** Round 3, the last review round of era 4 Who batch 2, found no blocking point in any of the eight profiles. Four of its seven minor points were in participant text:
- **Benjamin I of Alexandria, brief and audio.** "its translator" became "the History's translator", since a sentence had come between the History and "its".
- **Gregory of Narek, brief and audio.** "of the same century" became "of Gregory's own century", since it could be heard as Serpos's eighteenth century.
- **Martin I of Rome, card.** The decree item now places Theodore Calliopas as the governor who arrested Martin, and says Martin reports the decree rather than quotes it.
- **Timothy I of Baghdad, card.** An item headed "His name." now opens 'Why he is called "of Baghdad".'

Mark ordered the four applied as worded, and one targeted Opus check of only those strings by an agent that had not seen the drafting or the earlier rounds. The check does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch2/R4_cap-check.md`. Its verdict was CLEAR, with no blocking point. Evetts is the translator on the History's title page, and the life is headed 622 to 661. Macler dates Stepanos of Taron to the late tenth and early eleventh century, and the Anania sentence is still his. Mansi has Calliopas as exarch, rendered governor, and Martin's letter reports the decree's "irregulariter & sine lege". The four witnesses on Timothy's name hold. One minor point was found and applied as worded: in the Benjamin brief, the Evetts sentence moved up one place, so that "He came from a rich family" points to Benjamin. No word changed, and the brief is still 405 words, FK 8.23, Flesch 60.07. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 2: eight profiles, eight majors, the Photian councils found in Mansi (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** The eastern majors of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: Maximus the Confessor, Martin I of Rome, Photius of Constantinople, Timothy I of Baghdad, Dionysius of Tel Mahre, Jacob of Edessa and Gregory of Narek. Benjamin I of Alexandria is added, moved to era 4 by the date of his work (era 3 batch 6). His brother Mennas is a separate STORY row and is not written here. None of the eight is a census person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Major marks.** All eight are major, matching the scan's marks; Benjamin I is major because he led the Coptic church through the Arab conquest. Each brief runs 404 or 405 words, about 2:30. Dionysius of Tel Mahre is a recorder, but his held life carries the full length, as Bede's did in batch 1. In Bar Hebraeus he gives his election in his own words, two journeys to Egypt, a hearing before al-Ma'mun, and his death. The 2:30 is a cap, not a target.
- **Martin I** is written from what the held lines say of his stand over the teaching of one will: the Lateran synod, his seizure, trial and exile, and his own letters from Cherson. The trial and stripping are told from the account by one of his clergy, and the seizure, the voyage and Cherson from his own letters.
- **Ids, the worker's calls, accepted.** `martin-i-of-rome`, in the form of the era 3 bishops of Rome; `timothy-i-of-baghdad`, since "Timothy I" alone collides with Timothy I of Alexandria, Timothy II and Timothy Aelurus; `photius-of-constantinople`, since the census and the Library hold other men named Photius.
- **Card traditions, the worker's calls, accepted.** Maximus in the Heraclian entry and Latin African Christianity under Byzantium, which lists him and covers the dispute with Pyrrhus in Africa. Martin in the Heraclian entry only, since no era 4 census movement is Roman. Benjamin in Coptic Christianity under Early Islam first and The Church of Alexandria and Miaphysite Egypt second, since his return under 'Amr and most of his patriarchate fall after 642.
- **Own words in other languages.** Where a man's own words are held only in Latin, French or Italian, the brief tells them in modern words with the source named. It keeps quotation marks for held English.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in four parts, found 12 blocking and 69 minor points. The blocking points:
- **False absences.** Benjamin's homily on the wedding at Cana is listed in Assemani's catalogue. Gregory of Narek is quoted twice in Parisot's Aphrahat. Jacob of Edessa's Chronicle is held in Brooks's Latin, and his canons in part in Bar Hebraeus's Nomocanon. The acts of Photius's council of 879 are in Mansi 17, and Cornelius Will gives his death year, 891.
- **Witnesses wrong or missing.** Bar Hebraeus's editors were put on the wrong side of the question over the shorter chronicle credited to Dionysius. Elias of Nisibis was given Timothy's place of enthronement and the eight months of dispute, which are Chabot's, Bar Hebraeus's, Amr's and Mari's. Joseph Assemani's reading on the caliph al-Hadi was told as Amr's own.
- **Unsupported.** Peter of Yaman was placed among the bishops made in Timothy's time.
- **Context dropped.** The Maximus card said Macarius of Antioch's profession cursed Maximus at the council of 680-681, without saying the council anathematized and deposed Macarius.
- **Contested told as settled.** The 105 bishops of Martin's synod, where Theophanes gives 150.

Round 2, a targeted recheck in two parts, found 3 blocking and 19 minor points, all fixed. Two blocking points came from round 1 fixes: the Cana homily was given the date of the codex before it, and a Martin card item said "that council" before any council was named. The third was a false absence: Tel Mahre's place is held, in W. Wright citing Yaqut. Round 3, the last, found no blocking point and seven minor points. Three were in the records and notes and were applied. Four were in participant text, and Mark's cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Mansi 15, 16 and 17-18 are held, against the council row's "not held", so both Photian councils are in the Library. Photius's life is held, against "no life held". For every profile, the held witnesses go well past those the scan lists. Details are in Open-Gaps 256.

**What is still open.** Open-Gaps 256, "Era 4 Who batch 2" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch2/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch2/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of two round 3 fixes, era 4 Who batch 3

**Cap ruling (Mark's standing ruling of 2026-11-14, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark").** Round 3, the last review round of era 4 Who batch 3, found no blocking point in any of the eight profiles. Two of its four minor points were in participant text:
- **Cuthbert of Lindisfarne, card.** The Ripon item now says Bede's prose Life has Eata and Cuthbert "driven home" for the Life's "domum repulsus est", and names "Bede's History", since "His History" could be heard as Cuthbert's.
- **Cogitosus, brief and audio.** "Painted boards adorned it" became "Painted boards adorned the church", since "it" could be heard as the altar or a tomb.

Both were applied as worded, with one targeted Opus check of only the changed strings, by an agent that had not seen the drafting or the earlier rounds. The check does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch3/R4_cap-check.md`. Its verdict was CLEAR, with no blocking or minor point. The Life reads "repulsus", the Cogitosus sentence matches PL 72, and the brief runs 327 words, FK 7.85, Flesch 64.90. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 3: eight Insular profiles, no majors, Wilfrid of Ripon, Stephen's Life of Wilfrid found (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** Eight Insular WHO rows. Six come from `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: Theodore of Tarsus, Willibrord, Leoba, Muirchu maccu Machtheni, Tirechan and Cogitosus. Two come from `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`: Wilfrid and Cuthbert of Lindisfarne. None is a census person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **No majors.** Anglo-Saxon Christianity already has four majors in Bede, Boniface, Aidan and Hild, and Medieval Irish Christianity has Adomnán of Iona. All eight run 327 to 346 words, about 2:01 to 2:08. Tirechan, Cogitosus and Muirchu are recorders and stay at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours.
- **Leoba**, whose record is thin, is written from her one letter, three letters to her and Edward Kylie's introduction. The brief says which part is Kylie's.
- **Wilfrid of Ripon**, id `wilfrid-of-ripon`, against the supplement scan's "Wilfrid of York". The approved Hild of Whitby texts already call him so, and keep "Wilfrid of York" for Hild's pupil, Wilfrid II.
- **Card traditions, the worker's calls, accepted.** Muirchu and Tirechan in Medieval Irish Christianity. Cogitosus in Medieval Irish Christianity and Insular / Irish Monastic Christianity, since his date is disputed. The five English figures are in Anglo-Saxon Christianity only.
- **Two era 3 card readings** are logged for the era 4 map build and not changed here: the Brigid of Kildare card on Basnage's placing, and the Ciaran of Clonmacnois card on Tirechan's date.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in two parts, found 7 blocking and 56 minor points. The blocking points:
- **False absences.** Stephen was said to be alone in telling Theodore's confession and Wilfrid's prison and Austerfield, where Fridegod's and Eadmer's Lives, in the same volume, tell them too. Bede's own year for Cuthbert's consecration, the year King Egfrid was killed, was missed.
- **Witnesses on the wrong side.** Charles Plummer was counted against Theodore's authorship of the penitential, though he calls it Theodore's work. Stokes's index was read as listing Muirchu's father separately from Brigid's biographer.
- **A namesake collision.** "Wilfrid of York" against the approved Hild texts.
- **A contested point told one way.** Cuthbert's vision of Aidan was told only in Bede's timing, against the approved Aidan profile.

Round 2, a targeted recheck, found 1 blocking and 14 minor points, all fixed. The blocking point came from a round 1 fix: the Cuthbert card said Bede does not put Cuthbert among the monks who left Ripon, where his prose Life does. Round 3, the last, found no blocking point and four minor points. Two were in the records and README and were applied. Two were in participant text, and the cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Stephen's Life of Wilfrid is held in Raine 1879, with Fridegod's and Eadmer's Lives, against the scan's "not held". Bede's prose Life of Cuthbert and the Lindisfarne monk's Life are held in Latin. Alcuin's Life of Willibrord is held, and so is Theodore's Penitential. Muirchu's preface is held only in White's English, since Stokes's pages are missing from the file. Details are in Open-Gaps 257.

**What is still open.** Open-Gaps 257, "Era 4 Who batch 3" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch3/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch3/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of nine round 3 fixes, era 4 Who batch 4

**Cap ruling (Mark's standing ruling of 2026-11-14, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark").** Round 3, the last review round of era 4 Who batch 4, found no blocking point in any of the eight profiles. It found nine minor points, all in participant text or the README:
- **Hincmar of Reims, brief and audio.** "In his own letter, Hincmar wished…" became "the uncle wished…", since his nephew shares the name.
- **Who wrote the 861 notice of Prudentius.** G. H. Pertz gives it to Hincmar and Nicolás Antonio to an unnamed annalist. The Prudentius brief and four Prudentius card strings, and one Hincmar card string, no longer give it to Hincmar without naming Pertz. Taken as minor, as the reviewer rated it.
- **Cards.** Georg Waitz's role at first mention on both Carolingian cards; "Some comes through defenders" for "The rest" on the Prudentius card; Mayansius placed as Antonio's biographer (Braulio); Cixila placed at first mention (Ildefonsus); Felix, Cardinal Lorenzana, Antonio, Mommsen and the deacon Gudila placed (Julian); "W. J. Rees" for the bare "Rees" (Beuno). The README's audio line now says `[warmly]` goes at the start of the last paragraph.

All were applied as worded, with one targeted Opus check of only the changed strings, by an agent that had not seen the drafting or the earlier rounds. The check does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch4/R4_cap-check.md`. Its verdict was CLEAR, with no blocking point. It found four minor clarity points and two observations, and all were applied without changing a claim (listed in `R3_changes.md`): Pertz placed as "an earlier editor" on two cards; "the annals he had kept" in the Prudentius brief, now 345 words, FK 7.81, Flesch 64.48; "Julian signed the councils"; and Gottschalk and Antonio placed in a Prudentius card item. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 4: eight Latin West profiles, two majors, Hincmar major on his held church-law writings, Will's 1054 texts found (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** Eight Latin West WHO rows. Seven come from `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: Hincmar of Reims, Prudentius of Troyes, Jonas of Bobbio, Braulio of Zaragoza, Ildefonsus of Toledo, Beuno and Humbert of Silva Candida. Julian of Toledo comes from `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`. None is a census person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **Majors.** Humbert of Silva Candida is major, as the Roman face of the 1054 break. Hincmar was first marked standard, because the scan held only his annals. Drafting found his church-law and church-political writings held (Mansi 15 to 17, Krusch, Mommsen), and the coordinator then marked him major. Both briefs run about 400 words, about 2:30; the 2:30 is a cap, not a target. The other six run 327 to 346 words, about 2:01 to 2:08. Prudentius and Jonas are recorders and stay at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours.
- **Humbert and 1054** are told from both sides' held lines: the envoys' account and sentence, and the edict of Keroularios's synod with his letters to Peter of Antioch. Cornelius Will, who edited both, is marked as taking the Roman side. The disputed readings are tagged: the day of the sentence, who wrote the account and the reply to Nicetas, who forged what, why they never met, and where the Dialogue was written.
- **Hincmar** is told from his annals, the Douzy bishops' letter to Pope Hadrian II, his own letter to Hadrian and his nephew's own complaint to Pope John VIII. Bruno Krusch's hostile verdict is given only as Krusch's.
- **Beuno's** record is late, and his brief says so early, under the later-retelling rule.
- **Card traditions, the worker's calls, accepted.** Humbert in the Latin Papal entry and the Macedonian entry. Beuno in British and Welsh Christianity, against the scan's Medieval Welsh, which begins in 768. Jonas in Insular / Irish Monastic Christianity, since Merovingian Gallic Christianity ends in 620.
- **The laws and writings against Jews** in the Visigothic profiles are told in the sources' own terms. Braulio's letter for the council of 638 and its canon are told with the king's policy, and Julian's dedication to King Ervig is told as his own words.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in four parts, found 26 blocking and 75 minor points. The blocking points:
- **False absences.** Hincmar's ordination in 845, his death in 882 and his nephew's own complaint. Felix's notice of Julian's death. Ildefonsus's reported birth and the place of Agali. Jonas's birth at Susa. The dispute over Braulio's authorship of the notice of Isidore's works.
- **The wrong man.** The Annals of Saint-Bertin's introduction is G. H. Pertz's, not Georg Waitz's, and the note on Lebeuf's reading of 849 is Bouquet's. Antonio blames an unnamed annalist, not Hincmar.
- **Dates on the wrong event, or told as settled.** Humbert's 24 June belongs to Nicetas's recantation. The 16 July of the sentence is Will's reading, against Mirbt's 13 July. Pope Benedict was already dead when the bishops of 688 answered him.
- **One side only.** The Greek answer on the creed and on the failed meeting was missing. "Royal annals" was told as settled.
- **Sources misread.** Braulio's answer to the pope's "dumb dogs" line. Julian's dedication to Ervig. Lebeuf's signs read as a Spaniard's hand. A curse that lost "unless they repent". Beuno's centuries came only at the close. Mirk's date rested only on the Library header.

Round 2, a targeted recheck in two parts, found 4 blocking and 21 minor points, all fixed. All four blocking points came from round 1 fixes made on one card and not carried to its sister card, or from the narrator's voice. "Royal annals" was left on the Hincmar card. The slander charge was left on the Prudentius card. Braulio's archdeacon was told as Eugenius II. The Jews' argument in Julian's book was told in the narrator's voice. Round 3, the last, found no blocking point and nine minor points, and the cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Cornelius Will's Acta et scripta (1861) is held, with both sides of 1054. Hincmar's canon-law work is held, against the scan's "not held". Prudentius's own works are held in Patrologia Latina 115, and Jonas's Latin preface and his Life of John of Réomé in Barralis and Krusch. For every profile the held witnesses go well past those the scans list. Details are in Open-Gaps 258.

**What is still open.** Open-Gaps 258, "Era 4 Who batch 4" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch4/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch4/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of one round 3 card fix, era 4 Who batch 5

**Cap ruling (Mark's standing ruling of 2026-11-14, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark").** Round 3, the last review round of era 4 Who batch 5, found no blocking point in any of the eight profiles and one minor point, in participant text:
- **Sophronius of Jerusalem, card.** In the first `uncertain` item, "His Greek can be read as saying it of the temple or of Umar" became "Theophanes's Greek can be read ...", since "His" could be heard as Sophronius's.

It was applied as worded, with one targeted Opus check of only that string, by an agent that had not seen the drafting or the earlier rounds. The check does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch5/R4_cap-check.md`. Its verdict was CLEAR, with no finding: Theophanes's "Τοῦτον" (PG108 l.61789) can take "ναόν" (l.61787) or Umar, and the Latin "Hunc" (l.61824) takes Umar. The check noted that the item's unchanged last sentence says "No text" where the records say "No held text"; that is logged in Open-Gaps 259 and not changed. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 5: eight eastern profiles, two majors, Moses bar Kepha's On Paradise found in Migne 111 (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** Eight eastern WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: Sophronius of Jerusalem, Athanasios the Athonite, Sebeos, Antony of Choziba, Moses bar Kepha, Alopen, Thomas of Marga and John of Nikiu. None is a census person entry or was written before. Adam (Jingjing), the stele's author and a separate scan row, is named only as the stele's author, King-Tsing. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator and worker calls (not Mark's words; Mark may overrule).**
- **Majors.** Athanasios the Athonite, who founded the first great house on Mount Athos, and Alopen, who brought the Church of the East to China. Athanasios's brief runs 405 words, about 2:30. Alopen's runs 362 words, about 2:14: everything the held sources say of him goes back to the one Xi'an stele, and the brief says so early. The worker raised this before writing it short, and the coordinator agreed (2026-11-14): the 2:30 is a cap, not a target, as with Nennius.
- **The other six** run 348 to 356 words, about 2:09 to 2:12. Sebeos, Thomas of Marga and John of Nikiu are recorders and stay at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours; Antony of Choziba is a recorder known only from his own writings.
- **Sebeos's authorship** is tagged contested. Frédéric Macler, his French translator, rejects the first two books printed under his name and takes the third alone as his; Stephen of Taron names the History as his. No held source argues against book III, and a modern study is wanted.
- **Sophronius** is written as his own man: Stephen of Dor's oath at Calvary, his poem on his own life, Sergius's account of the dispute at Alexandria, his synodal letter and Christmas sermon, Theophanes's account of Umar, and the council of 680-681. Maximus is not in his brief.
- **Card traditions, the worker's calls, reported to the coordinator.** Sophronius in the Heraclian entry and Chalcedonian Monasticism - Judean Desert & Gaza; Athanasios in the Macedonian entry and Athonite & Comnenian Byzantine Monasticism; Sebeos in Armenian Christianity before the Bagratids, since the scan's "Armenian Apostolic" is no census name; Antony of Choziba in Chalcedonian Monasticism - Judean Desert & Gaza, though its window ends at 614, since no era 4 entry covers the desert houses; Thomas of Marga in the Silk Road and Abbasid entries of the Church of the East.
- **Words held only in Greek, Latin or French** are told in modern words with the source named. Quotation marks are kept for held English. The Greek of Meyer's Athos edition and of the Choziba volume is badly garbled and is quoted in no participant text.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in two parts, found 10 blocking and 60 minor points. The blocking points:
- **A pronoun or a sentence changing what the source says.** Sophronius's words on the abomination of desolation were turned onto the temple; Basil was made to add Moses bar Kepha's point on church builders; the History of the Patriarchs' writer, not John of Nikiu, was the spiritual son of John III.
- **A hedge dropped and a note moved.** Macler's reading of Sebeos on the invasion as punishment lost its "he does not say it outright" and was set beside a passage it does not gloss.
- **False absences.** Alopen's "all that is known" (the census cites the Tang huiyao, not held); George of Choziba's "only held account" (Nikodemos the Hagiorite gives a notice); the Chronicle as "the source" for Benjamin's return (the History of the Patriarchs tells it too).
- **The wrong work or the wrong owner.** Moses's baptism line credited to his liturgy commentary; B. Evetts's A.D. heading told as the History's; a Seleucia placing credited to Budge.

Round 2, a targeted recheck, found 2 blocking and 20 minor points, all fixed. Both blocking points came from round 1 fixes: Theophanes's Greek leaves open whether Sophronius spoke of the temple or of Umar, where the fix had chosen Umar from the Latin; and the 903 passage credited to C. W. Mitchell is F. C. Burkitt's introductory essay. Round 3, the last, found no blocking point and one minor point, in participant text, and the cap ruling above settles it. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Moses bar Kepha's On Paradise is held in Masius's Latin inside the Migne 111 file named for Nicholas Mystikos, against "none of his works is held". The name Antony is in the Greek of the Choziba Life. Mari ibn Sulayman has Thomas of Marga as metropolitan caring for his imprisoned brother, the patriarch Theodosius. The census's story of Athanasios found alive under the dome rests on no held line. Open-Gaps 50's "636, not 635" for Alopen does not hold as a reading of the held stele translation. Details are in Open-Gaps 259.

**What is still open.** Open-Gaps 259, "Era 4 Who batch 5" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch5/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch5/`. No census, record or site change is made, so there is no data release number. Approved to proceed (the batch worker, under the coordinator's brief of 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of the round 3 fixes, era 4 Who batch 6

**Cap ruling (Mark, 2026-11-14: "Fix + one check (Recommended)", picked from options, relayed by the coordinator).** Round 3, the last review round of era 4 Who batch 6, found one blocking point. The Simon I card said Eusèbe Renaudot reads the archdeacon George's history as ending with Simon, against John the deacon's Alexander II. Renaudot's own sentence (REN l.13765-13772) gives George John's end point, the time of the caliph Sulaiman, so the two do not disagree, and the card contradicted the Alexander II card. Round 3 also found seventeen minor points: records line numbers, pronoun and antecedent fixes, Severus's "Muslims do not fast today" for Renaudot's "hodie", and Michael I's and Alexander II's card items on Evetts's heading and on who wrote Alexander's last years. The fixes were applied as worded, with the reviewer's identifier for Severus's first mention in the brief. Mark ordered one targeted Opus check of only those strings, by an agent that had not seen the drafting or the earlier rounds, which does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch6/R4_cap-check.md`. Its verdict was NOT CLEAR, with no blocking point: the fix for the blocking point was found correct, 16 strings clear, and 5 minor points, all applied as worded without changing a claim (listed in `R3_changes.md`): a three days' count in the Simon brief, now 381 words, FK 5.80, Flesch 76.97; Budge introduced at first mention and the Dabra Zegag reading stated in the Simon card and records; one "bishop of al-Ushmunain" in the Severus brief, FK 6.58, Flesch 71.90; and a correction to the change logs' account of Evetts's name forms. The check says the batch is clear once these are applied, as in era 4 batch 4. The cap ruling is met.

## 2026-11-14 — Who profiles, era 4 batch 6: eight Coptic profiles, no majors, the History's writers kept apart from Severus (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** The eight Coptic WHO rows of `Build/Ministry/Operations/Audits/2026-11-11_who-scan-era4/Who_Scan_Era4.md`: the patriarchs Agathon, John III of Samannud, Isaac, Simon I, Alexander II, Michael I and Joseph I (Yusab) of Alexandria, and Severus ibn al-Muqaffa. None is a census person entry or was written before. Benjamin I (era 4 batch 2) and his brother Mennas, a STORY row, are not in this batch. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator calls (not Mark's words; Mark may overrule).**
- **No majors.** Coptic Christianity under Early Islam has Benjamin I as its major, and these patriarchs are told mostly through one History. The briefs run 344 to 381 words, about 2:08 to 2:21. Severus is a recorder and stays at standard length, by the rulings for Palladius, John of Ephesus and Gregory of Tours; his own life is thin, and his card says so.
- **Whose account.** Every brief says what its life rests on. The History of the Patriarchs is told as a later Arabic history of the Coptic church and its lives are not called Severus's. John III's writer is his unnamed spiritual son; Michael I's is John the deacon, who names himself and calls Moses of Wasim his spiritual father; John says the archdeacon George wrote the history to the time of the caliph Sulaiman, and that he wrote the rest of Alexander II's chapter. Isaac is told from the History and from Mina's Coptic Life, which its editor E. Porcher says was written to edify. Joseph I's History life is not held; he is told from Renaudot's Latin retelling, the two synaxaria and Bar Hebraeus's quotation of Dionysius of Tel Mahre.
- **Severus and the History's authorship.** The held lines show a dispute over how much of the History is his (Evetts: it cannot be known; Renaudot names later continuers and doubts his Greek) and over his century (Evetts placed him in the ninth century in 1895 and near the end of the tenth in 1904). Both are tagged contested and told in place. No held line says in those words that his authorship is disputed, as the census's peopleNote does; that is in Open-Gaps.
- **Ids and names.** `agathon-of-alexandria`, as Evetts and the approved Benjamin I card spell him ("Agatho" is an other name); `john-iii-of-samannud`; `joseph-i-of-alexandria`, an English id, with Yusab, the census's name, as an other name; `severus-ibn-al-muqaffa`.
- **Card traditions.** All eight read "Coptic Christianity under Early Islam", as the scan places them; all their dates fall within it.
- **Renaudot** is marked in every text as a Catholic writing in 1713, who calls these patriarchs heretics.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in two parts, found 9 blocking and 54 minor points. The blocking points:
- **Sources misread.** Porcher's "not a historical work as conceived today" was shortened to "not as history". Nau's reckoning of Isaac's years was given to the wrong sources. Renaudot's iron ring worn on the right hand was told as a brand. Shamul was made the only person with the dying Alexander, where he was the only bishop. Kurrah was said to send Alexander to beg, where Alexander asked to go.
- **A witness on the wrong man.** John the deacon was made Michael I's spiritual son; he is Moses of Wasim's.
- **False absences.** No held line was said to name the writer of Alexander's last years, where John the deacon says he wrote them; Severus's other works were said to be named only in publisher lists.

Round 2, a targeted recheck in two parts, found 2 blocking and 21 minor points, all fixed. The blocking points: "Agathon writes" settled who wrote the Macarius account, which Renaudot disputes; and the Alexander card ended George's history at Usamah's removal, where John ends it at the time of Sulaiman. Round 3, the last, found one blocking and seventeen minor points, and the cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Found in drafting.** The research notes' "I the sinner Agathon" is "And as for me, the sinner Agathon", across a page break (SEV l.45965, 46143). Simon I's Arabic Synaxarium notice, 24 Abib, is held, bound into the PO 17 John of Ephesus file. Samad ordered the coals for John III's feet but did not use them. Details and the scan corrections are in Open-Gaps 260.

**What is still open.** Open-Gaps 260, "Era 4 Who batch 6" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch6/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch6/`. No census, record or site change is made, so there is no data release number. Approved to proceed (coordinator, 2026-11-14; Mark may overrule).

## 2026-11-14 — Cap ruling: one check of two round 3 card fixes, era 4 Who batch 7

**Cap ruling (Mark's standing ruling of 2026-11-14, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark").** Round 3, the last review round of era 4 Who batch 7, found no blocking point in any of the seven profiles and four minor points. Two were in participant text, both on cards:
- **Symeon the New Theologian, card.** `legacy.remembered` 2 now reads "Manuel Calecas, a Dominican, wrote against the Palamites. In a note, Combefis reads the deluded monks that Calecas attacks as Symeon and his disciples.", so no clause sits between Calecas and his verb.
- **Niketas Stethatos, card.** `legacy.traces` 2 is split at "Greek.", from 29 words into two sentences.

The other two, a records witness and the README's word counts, were applied as worded. All four were applied as worded, with one targeted Opus check of only those strings, by an agent that had not seen the drafting or the earlier rounds. The check does not count toward the cap: `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch7/R4_cap-check.md`. Both card strings and the README counts passed. The check found one minor point in the records only: two of the Niketas skete claim's line ranges were off by a line or two, and Athos and the monk were not cited. It was applied as worded and confirmed by reading the six ranges in the file, as the check allowed. No participant text changed. The cap ruling is met.

## 2026-11-14 — Who profile length: non-majors to 2:00 from the next batch, and era 4 batch 7 kept as written (Mark, 2026-11-14)

**Decided (Mark, 2026-11-14, relayed by the coordinator, then in his own words to the batch 7 worker).** Mark first chose, from options, "Hold to 2:00 from now on (Recommended)". The option read: "From the next batch on, non-majors stop at 2:00 (about 325 words), as the pattern says. Profiles already written stay as they are." He then added: "hold to two without cutting off", so that a brief fits 2:00 by being written tighter, never by stopping a story halfway or dropping one of a pair. When the batch 7 worker had drafted 2:00 versions of its six non-major briefs, Mark said: "no stop, how much of the story will we loose, i would rather have a 2;15 good story than a 2;00 cramped but flat card". He was shown, for each brief, its length and what a 2:00 version would drop, and answered: "keep".

**What follows.** Era 4 batch 7 keeps its lengths: the single non-majors at 348 to 365 words, about 2:09 to 2:15, and the three paired profiles at 392 to 400 words, about 2:25 to 2:28, under the 2:30 cap the coordinator allowed for pairs, since each tells two lives. The tightened drafts were never written into the profiles. For later batches, the coordinator reads Mark's words together: non-majors aim at 2:00, and a good story at about 2:15 is preferred to a cramped one at 2:00. Approved to proceed (Mark, 2026-11-14).

## 2026-11-14 — Who profiles, era 4 batch 7: seven profiles, one major, three pairs, the summary of Niketas's Life of Symeon found in Migne 152 (coordinator, under Mark's ruling of 2026-11-14 that eras 4 to 7 are built in full)

**The batch.** Seven era 4 WHO rows of `Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md`: Symeon the New Theologian; Niketas Stethatos; Cedd and Chad; Elipandus of Toledo and Felix of Urgell; Paul the Deacon; Paulus Emeritanus; and Pisentius of Coptos and John the Elder. Three are paired profiles under Mark's pairing rule of 2026-11-11, "if two people are tied together in their sources with similar identity its ok to make that a single who", and each says why the two share it. None is a census person entry or was written before. Opus drafted every profile to `Who_Profile_Pattern.md`, per Mark's era 1 batch 1 ruling, "Opus for all".

**Coordinator and worker calls (not Mark's words; Mark may overrule).**
- **Major.** Symeon the New Theologian, as the scan proposes: the Philokalia's teachers of stillness read him. His brief runs 404 words, about 2:30. The other six are not major.
- **Lengths.** The pairs run to the 2:30 cap, the coordinator's call, which Mark then kept ("keep", in the entry above). Paul the Deacon and Paulus Emeritanus are recorders; Paulus's own life is thin, held only in the first chapter and the close of his book, and his card says so.
- **Symeon's life** is told from François Combefis's summary of Niketas's Life, with Combefis's own judgments kept apart, beside Symeon's own chapters and the Philokalia's notice. The coordinator agreed to this use (2026-11-14). Where Symeon's own telling and the Life differ on his ordination, both are given.
- **Elipandus and Felix.** Their view is told from Elipandus's letters and Felix's confession; Alcuin, Pope Hadrian I, the council of Frankfurt and the Frankish annals are given as the opponents they are, and the brief says early that much comes through them.
- **Card traditions, the worker's calls, confirmed by the coordinator.** Symeon and Niketas in "The Byzantine Imperial Church (Macedonian Era); Athonite & Comnenian Byzantine Monasticism", since the scan's "Byzantine monastic and hesychast tradition" is no census name; Elipandus and Felix in "Mozarabic Christianity; Carolingian Reform Christianity", since the scan's Nicene Visigothic Iberia ends in 711; Paul the Deacon in "Carolingian Reform Christianity", since the scan's two entries end in 604 and 680; Pisentius and John in "The Church of Alexandria and Miaphysite Egypt". Cedd and Chad and Paulus Emeritanus stand as the scan places them.
- **Words held only in Greek, Latin or Slavonic** are told in modern words with the source named. Quotation marks are kept for held English.
- **American spelling** in the new prose (Decision-Log 77); quotations keep their own spelling.

**Review.** Three rounds by fresh Opus agents that had not seen the drafting, at full effort in every round (Mark, relayed by the coordinator: "dont sacrafice quality, expecially the quality of writing"). Round 1, the full checklist review in two parts, found 14 blocking and 59 minor points. The blocking points:
- **A held own-voice witness missed.** Symeon's own telling of his ordination vision, in the Philokalia, differs from the Life on who said the prayer, and his closing words had lost "of those who take up the cross".
- **False absences.** Symeon's discourses "known only from Combefis", where Nil Sorsky quotes him; Agobard's book on Felix "known only from Froben"; "John gives no year", where he gives "this fifth year"; the README's Life as "the one source" for Pisentius.
- **Sources misread or hedges dropped.** Le Quien's dating of Niketas's later treatise is his inference; the twenty-two chapters Paisius heard of were Greek, in a skete on Athos; Agobard's "nonnullos" is people, not "some of it"; Elipandus's Toledo prayers were told as settled against Férotin's manuscript.
- **Wrong work or OCR told as fact.** The letter to the bishops of Gaul is in PL 101, not PL 96; Froben's "prope 50" and the Migne notice's "1658" are scan misreadings, not editors' slips; Felix was not heard at Frankfurt; "Paul Warnefried" is not Foulke's form.

Round 2, a targeted recheck, found 1 blocking and 8 minor points, all fixed. The blocking point came from a round 1 fix: the Cedd and Chad card said Cynebil built Lastingham, where Bede's preface has it built by the two brothers and the Latin keeps Cedd as builder. Round 3, the last, found all seven clear, with four minor points, and the cap ruling above settles them. Every quotation was re-checked word for word against its vendored file. No paid calls were made.

**Corrections to the scan found in drafting.** Niketas's Life of Symeon is not held as a text, but Combefis's long summary of it with Greek extracts is (PG 152). Pisentius's "d. c. 632" rests on no held line. Paul the Deacon's "died after 791" misreads Foulke. Paulus Emeritanus's "Levita Christi" is held. Details are in Open-Gaps 261.

**What is still open.** Open-Gaps 261, "Era 4 Who batch 7" (2026-11-14).

The approved files are in `Who-Profiles/era4/batch7/` in this folder, and the reviews are in `Build/Ministry/Operations/Audits/2026-11-14_who-profiles-era4-batch7/`. No census, record or site change is made, so there is no data release number. Approved to proceed (the batch worker, under the coordinator's brief of 2026-11-14; Mark kept the lengths).
