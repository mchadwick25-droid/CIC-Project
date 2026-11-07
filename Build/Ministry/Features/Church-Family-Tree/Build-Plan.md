# Church Family Tree — Build Plan

The chunked plan for the converged build (Decision-Log.md, 2026-11-06). One chunk is one
pull request unless it says otherwise. This file is the workstream's progress record: each
chunk's status line changes as it finishes.

Status key: **todo**, **building**, **in review** (PR open), **merged**, **waiting on Mark**.

## What reading the code found (2026-11-06)

These shaped the cut. None of them changes a ruling.

1. **The map is not self-contained.** `atlas-v3.html` (44,411 lines) and the 300 tree pages
   use files the rest of Church in Conversation also uses:
   - used by the map or tree only, so they move: `audio/tree/` (156 MB),
     `audio/docstories/` (370 MB), `audio/stories/` (38 MB);
   - shared, so they stay in `cic-website/`: `audio/worlds/` (78 MB, also on the tradition
     pages), `data/worlds/` (written by `engine/m2/site_compiler.py`),
     `assets/narration-player.js`, `assets/feedback.js`, `assets/feedback.css`,
     `assets/favicon.svg`, and the census.
2. **A pure rename removes the tree from the old site in the same merge.** `git mv` takes the
   files out of `cic-website/` at once, before the new domain serves them. That breaks the hard
   rule. The proposed order (below, "The move, step by step") avoids it with a build step, and
   it commits no second copy of the audio.
3. **The map and tree pages link into the old site by relative address.** `index.html`,
   `index.html#who`, `table.html`, `../talk.html?worlds=…`, `../traditions/<id>.html`. On the
   new domain these would break. They become full `https://churchinconversation.com/…`
   addresses before the rename, so the rename itself stays pure.
4. **Feedback cannot post from the new domain yet.** `feedback.js` posts to
   `app.churchinconversation.com/api/feedback`, which allows one site origin
   (`CIC_API_SITE_ORIGIN`, `engine/api/config.py`). Allowing a second origin is an API change.
   It reaches Render only through a promotion to `live`, which is Mark's call.
5. **CI checks out without `cic-website/audio/`** in about ten jobs (sparse checkout). Each of
   those jobs needs the tree's audio folder excluded too after the move.
6. **The generator also writes `cic-website/sitemap.xml` and `robots.txt`.** These split: the
   tree's pages go in the tree's own sitemap.
7. **The door field has a home.** World records are `records/worlds/<code>.yaml`, read by
   `engine/m1/registry.py`, with the schema in `engine/m1/schemas.py`; `engine/m6/census_sync.py`
   carries named fields into the census.

## The move, step by step (the hard rule)

`main` deploys on merge, so the order is:

1. **P1a.** Add the tree's Worker config and one build script that assembles the tree site
   into a build folder at deploy time. At this stage the script reads the tree's files where
   they are now, in `cic-website/`. Nothing moves and the old site is untouched. The new Worker
   serves on its `workers.dev` address only.
2. **P1b.** Mark attaches `www.churchfamilytree.com`. Verify that it serves the tree.
3. **P1c.** Only then, in one merge: the pure rename into the tree's own folder (its own
   commit, 100 % similarity), the script reads the new paths, and the old Worker gets its
   redirects. Both Workers rebuild from the same merge, so the new site keeps serving and the
   redirects land on it.

The same build script copies the shared files (finding 1) into the tree's build folder from
`cic-website/`. One copy lives in git; the build makes the second, so the audio is never
committed twice. The CI check runs the script and compares the two copies of each shared file,
byte for byte. This is ruling 10's "copied by a build step, with a CI check that they match",
applied to every shared file, not only the census.

## Chunks

| # | Goal | Stop point | Status |
|---|---|---|---|
| R1–R3 | The rivers, one PR | Mark judges by eye on the preview | merged (#1526) |
| P1a | Tree Worker and build script; full addresses for cross-site links | none | merged (#1527) |
| C1 | Public site carries code only; notes moved to `Build/Ministry` | none | merged (#1528) |
| PL1 | Place labels from each movement's and gap story's own region text | none | merged (#1529) |
| PL2 | Modern countries, each with a gazetteer ID | Mark rules on disputed borders, one sitting | merged (#1529) |
| PL3 | Place line on the map, panel and tree pages; data release 2 | Mark sees screenshots on the preview | merged (#1529) |
| P1a2 | Feedback API allows the tree's origin | Mark: promotion and Render variable | todo |
| P1b | Attach the domain; verify | Mark: dashboard steps | done (2026-11-07) |
| P1c | Rename, data release 3, redirects | none (after P1b is verified) | merged (#1531) |
| P1d | Door switch; about, privacy and support pages | Mark: Stripe links | merged (#1531); give buttons wait on the Stripe links |
| P1e | Repoint Church in Conversation's links; verify; note for the researcher | none | in review |
| P2-L1…L10 | Links, one era per chunk | none | todo |
| P2-L11 | Full review of the whole link set | none (3-round cap) | todo |
| P2-M | Method page, confidence at a glance | none | todo |
| P2-D | Data and citation page | none | todo |
| P2-S | Find-your-church search | none | todo |
| P2-G1 | Gap sweep (read only) | Mark's ruling sitting | todo |
| P2-G2 | Schema additions | none | todo |
| P2-G3 | The agreed entries | narration sample, by ear | todo |
| P2-V | "Living" definition and the 169 flags | none | todo |
| P2-K1 | Drawn marks, 2 to 4 options | Mark's pick | todo |
| P2-K2 | Marks, floor, tap areas; phone, light and color-vision test | none | todo |
| P2-Z | Launch gates, numbered release, announcement draft | gates 5 and 6 belong to other threads | todo |

### R1–R3 — the rivers (one pull request, three commits)

The rivers brief asks for one pull request, and Mark judges the feel once. The three chunks
are three commits on one branch, each checked before the next.

- **R1, width.** `widthAt()` range and exponent tuned by eye; `laneSamples` smoothed with a
  moving average over a few decades; zero width stays zero.
- **R2, drift and gap.** Pull types and push types per the brief; confidence weights;
  `DRIFT_MAX` raised with `tanh` kept; a longer smoothstep fade in `driftInfluence`; a hard
  minimum gap from both widths; no double pull at a lane's genesis; links still attach to dots.
- **R3, legend and switches.** The two plain notes under Tradition families; drift recomputed
  without hidden lanes, so a hidden river leaves no pull.
- **Files:** `cic-website/atlas-v3.html`; `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`
  (the new entry first, the final weights after).
- **Inputs:** current `main` (#1517, #1521, #1524 merged).
- **Done means:** `check_live_commentary.py --base origin/main --enforce` and `check_spelling.py`
  clean; `validate-census.mjs` and `atlas-check --edges-only` green without edits; Chromium
  screenshots before and after at full-map and close zoom, dark and light, plus a phone width;
  no page errors; a scripted check that no two neighboring rivers' edges come closer than the
  gap at any sampled year; the switch check still passes (Africa hidden: 12 of 13 rivers).
- **Stop:** Mark judges the feel on the branch preview before merge.

### P1a — tree Worker and build script; old site untouched

- **Goal:** the tree's own Worker builds and serves the tree on its `workers.dev` address,
  with nothing moved.
- **Files:** `wrangler.cft.jsonc` (new); `tools/build_tree_site.mjs` (new: assembles
  `.build/tree/` from a declared list of tree files and shared files); `cft-website/_headers`
  and `cft-website/robots.txt` (new folder, with only the tree's own new files at this stage);
  `cic-worker/worker.test.mjs` (the baseline-header check covers both sites' `_headers`);
  `.gitignore`; `cic-website/atlas-v3.html` and `Build/tools/generate_tree_pages.mjs` (relative
  cross-site links become full addresses; tree pages regenerated); `wrangler.jsonc` (its
  commentary removed, by the standing rule); `README.md` map and
  `CiC_Repo_Structure_Tracking.md` (the new top-level folder and config first).
- **Folder name:** `cft-website/`, beside `cic-website/`.
- **Done means:** the build script runs clean; a CI step runs it and checks every shared copy
  is byte for byte identical to its source; `node --test cic-worker/worker.test.mjs` passes;
  a local `wrangler dev --config wrangler.cft.jsonc` serves the map, a tree page, a narration
  file with a `206` range answer, and the census; churchinconversation.com is unchanged.
- **Stop:** none.

### PL1–PL3 — places and modern countries (one pull request, three commits)

Added 2026-11-07 (Mark). The names on the map say when, not where. These chunks add the place
and the country it lies in today. They edit the map and the census, so they come before the
rename in P1c. P1a has already merged, but it moved nothing, so the order still holds. One pull
request, because the census is served publicly the moment it merges: the data and the display
ship together, after Mark's ruling.

- **PL1, place labels.** A `placeLabel` on each of the 300 movements, shortened from its own
  `region` text only, and on each of the 62 gap stories (the map's book icons), from the
  story's own `region` text: at most two places, then "and beyond". Never a place the entry doesn't
  name. Sonnet drafts; a second, independent pass (a separate agent, given only the region
  text and the label) checks each label back against its region text.
- **PL2, modern countries.** `modernCountries` on each movement and each gap story: every country its places lie
  in today, each with the gazetteer ID used (a Wikidata ID from its "country" property, and a
  Pleiades ID where the place is ancient). Looked up, never filled from memory. Every place
  under a disputed or politically sensitive border (Jerusalem and the Holy Land, parts of the
  Caucasus, Kosovo, Cyprus, Western Sahara and similar) goes on one list, each with a proposed
  neutral wording. **Stop: Mark rules on the whole list in one sitting** before anything merges.
- **PL3, display and release.** At full-map zoom, names only. Zoomed in, a small second line
  under each name ("Scetis · Egypt"). In the panel and on the tree page, the full place line
  with "today" explicit ("Carthage, today in Tunisia"). One legend line: "Places are given with
  the country they lie in today." A hidden river hides its place lines. The place line sits
  inside the movement's own group, so P2-K2's tap area takes it in. Where labels would collide,
  the place line hides first. Dots and names may move a little off their exact year and
  river line so nothing overlaps (Mark, 2026-11-07); dates and links stay true. Gap stories have no name on the map, only an icon, so their
  place line goes in the hover tip and the panel, with "today" stated; no text is added beside
  the icons. Data release 2.
- **Files:** `cic-website/data/world-census.json`, `tools/validate-census.mjs` (every movement
  has a `placeLabel`; every modern country has a source ID; given the map file too, the same
  for every gap story, whose only copy is the map's embedded data), `cic-website/atlas-v3.html`,
  `Build/tools/generate_tree_pages.mjs` and the regenerated pages, an audit folder under
  `Build/Ministry/Operations/Audits/`, the decision log and Open-Gaps.
- **Done means:** the validator passes; the independent check finds every label faithful to
  its region text; Chromium at phone width, light and dark, full and close zoom, the busiest
  eras without collisions; the switch check unchanged; readability scored on the new lines.
- **Stops:** Mark's disputed-border ruling (PL2), then Mark sees the screenshots on the branch
  preview before merge (PL3).

### P1a2 — feedback from the tree's domain

- **Goal:** the feedback API accepts posts from the tree's origin as well as the old one.
- **Files:** `engine/api/config.py`, `engine/api/feedback_routes.py`, `engine/api/deeper_routes.py`
  (one origin becomes a list), their tests.
- **Done means:** API tests pass, with a test for each origin and one for a refused origin.
- **Stop:** merging deploys nothing. Mark's call: promote to `live` through the runbook, then
  set `CIC_API_SITE_ORIGIN` on Render to both origins (exact steps given). Until then a visitor
  on the new domain who sends feedback sees the widget's existing error text.

### P1b — Mark's dashboard steps (no pull request)

Exact steps, given in chat when P1a has merged:

1. Create the second Workers Build: the same repository, deploy command
   `npx wrangler deploy --config wrangler.cft.jsonc`, build command
   `node tools/build_tree_site.mjs`.
2. Attach `www.churchfamilytree.com` as a custom domain; add a redirect rule from
   `churchfamilytree.com` to `https://www.churchfamilytree.com`, permanent, path and query kept.
3. Turn on Web Analytics for the new domain (cookie-free; no script tag needed when the proxy
   injects it, or the snippet goes into P1d).

- **Done means:** the new domain answers `200` for `/`, `/tree/<id>`, a narration file with a
  `206` range answer, and `/data/world-census.json` with the same SHA-256 as the old address;
  the bare domain answers one `301` to `www`.

### P1c — the move, data release 3, redirects

- **Goal:** the tree's files live in `cft-website/`; old addresses redirect in one hop.
- **Files:** `git mv` (its own commit): `cic-website/atlas-v3.html` becomes `index.html` in
  `cft-website/`, and `cic-website/tree/` and `cic-website/audio/{tree,docstories,stories}/` move
  under the same names into `cft-website/`. Then: `tools/build_tree_site.mjs` reads the new paths;
  `engine/m6/cli.py` (`ATLAS_PATH`), `engine/m6/census_atlas_sync.py`, `cic/engine/corpus_coverage.py`,
  `tools/check_no_embedded_world_data.py` and its baseline, `Build/tools/generate_tree_pages.mjs`
  and `generate_tree_narration.mjs` (paths, canonical links, the tree's own sitemap),
  `cic-website/sitemap.xml`; `.github/workflows/ci.yml` (paths filters; the sparse checkouts
  exclude the tree's audio folder too); the redirect rules on the old Worker (a `_redirects` file in `cic-website/`
  if Cloudflare's asset redirects allow a full address in one hop, otherwise `cic-worker/worker.mjs`
  with tests); `cic-website/atlas.html` and `world-atlas.html` become redirect rules, and their
  files go to `Archive/`. Census: `meta.identifiers` gains the domain rule, `meta.license` is
  added, `meta.release` becomes 3 (release 2 is the place labels, PL3). `tools/validate-census.mjs --base` gains a check that every
  promised ID (retired and renamed included) has a redirect rule and a page, and every link ID
  has its anchor on its page.
- **Done means:** all census and engine tests pass; a redirect test covers `/tree/<id>`,
  `/tree/<id>.html`, a renamed movement, the three atlas addresses and the census (served, not
  redirected); `wrangler dev` for both configs; `Open-Gaps.md` item 4 closed.
- **After merge:** curl every old address: one `301` hop each, fragment kept; census hash equal
  at both domains, headers identical.
- **Stop:** none, but it waits until P1b is verified.

### P1d — door switch and the tree's own pages

- **Goal:** doors show only for worlds marked open; the tree carries its own about, privacy
  and support pages and its footer.
- **Files:** `engine/m1/schemas.py` and `records/worlds/<code>.yaml` (a `public_open` field, on
  for the 11 Built & Live worlds); `engine/m6/census_sync.py` and its README and tests (the field
  carried into the census as `publicOpen`); the map (`index.html` in `cft-website/`) and `generate_tree_pages.mjs`
  (the door lands on `churchinconversation.com/traditions/<id>.html`; with no world open, the one
  line "Church in Conversation, from the same team."; header and footer); new
  `about.html`, `privacy.html` and `support.html` in `cft-website/`; Web Analytics if a snippet is needed.
- **Done means:** sync check green; a test with every world switched off shows the quiet line;
  readability scored with `engine.m7.turn_readability.score_turn` on every new paragraph, results
  in the PR; the not-a-nonprofit line matches `cic-website/support.html` word for word, by a check.
- **Stop:** Mark makes the two Stripe links (steps given); the support page ships with them.

### P1e — repoint Church in Conversation; verify; researcher note

- **Files:** `cic-website/index.html` (four tree links), the tradition pages and
  `cic-website/templates/tradition.html`, `about.html`, `license.html`, `privacy.html`,
  `support.html`, `whats-next.html`, `story.html`, `table.html`, `go-deeper*.html`, `pilot*.html`,
  `assets/chooser.js`, `assets/orientation-render.mjs` (every tree link to the new domain).
- **Done means:** a link check finds no tree link left on the old domain; the post-deploy curl
  sweep passes; a short note for the outside researcher drafted in an Artifact.
- **Stop:** none (Mark sends the note).

### Phase 2

- **P2-L1 … L10, links by era (one fresh session per era).** For each movement in the era: every
  relationship its relations summary and description name becomes a link (type, grade, note,
  sources with a verbatim quote), or the prose loses or qualifies it. Two checks: prose to links,
  links to prose. Files: `cic-website/data/world-census.json`, regenerated tree pages and atlas
  edges, an audit folder under `Build/Ministry/Operations/Audits/`. Done: `validate-census.mjs
  --base` green, every quote verified against `cic/texts`, the two-way check listed in the audit.
  Sonnet drafts, Opus reviews.
- **P2-L11, whole-set review.** Opus, three-round cap, across all eras.
- **P2-M, method page.** The plain statement that every claim is AI-checked and none is yet
  reviewed by an independent scholar; confidence shown at a glance on every link.
- **P2-D, data and citation page.** The release, the permanence promise, how to cite, the
  license link, the request form (`https://tally.so/r/kb97Br`) and the invitation to review.
- **P2-S, search.** A new list of everyday names (the census's informal names are titles),
  sourced, and the search box on the map.
- **P2-G1, gap sweep.** Read only, by Haiku and Sonnet, of the Library's dossiers, NEEDS-RULING
  and staging notes. Output: one list for Mark's ruling sitting. **Stop.**
- **P2-G2, schema.** The movement-or-person kind; a confidence grade on living descent; the
  review-status field shown on each page; Tertullian as person + A5; the Cyrilline duplicate
  retired with a redirect.
- **P2-G3, agreed entries.** One numbered release. Narration for new pages (Open-Gaps item 10):
  sample first, Mark's approval by ear, every setting passed and printed. **Stop for the sample.**
- **P2-V, living.** The written definition; all 169 flags checked against it.
- **P2-K1, drawn marks.** Leaf, person and dot, 2 to 4 options rendered for Mark. **Stop.**
- **P2-K2, marks and tap areas.** Bigger marks with an on-screen floor; one tap area per
  movement, 24 px, 44 px on touch, nearer mark wins; new legend rows that obey the switches (a
  hidden lane hides its marks and tap areas). Test at phone size, on the light theme, and with a
  color-vision simulation of the link colors beside the new marks (Open-Gaps item 11).
- **P2-Z, launch.** Confirm the gates (Open-Gaps items 5 and 6, other threads' work; the license
  is live), ship the numbered release, draft the announcement.

## Not in scope

Preset views (declined). Carrying saved legend choices across domains (they reset, as
expected). Promotion to `live` (Mark's call).
