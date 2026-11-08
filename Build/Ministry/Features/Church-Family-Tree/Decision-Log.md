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
