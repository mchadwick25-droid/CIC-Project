# Launch prompt — Church Family Tree build thread (2026-11-06)

Paste everything below the line into a fresh Claude Code session on this repository.

---

Build the Church Family Tree's move to its own domain and its standalone release, per the
converged plan. Mark said "Converged, auto mode" on 2026-11-06: carry out the plan without
asking step by step, and stop only for the stop points listed below.

**Read first, in this order:**
1. `CLAUDE.md`, which holds the working rules.
2. `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`. It holds every ruling, and
   it is the plan.
3. `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`.
4. The Atlas Decision Log entry of 2026-11-06 (`Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`).
   It covers the lineage rigor pass, permanent IDs and the permanence promise in
   `meta.identifiers`.
5. `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`, "What does not go
   through this". The public site deploys from `main` through Cloudflare Workers Build,
   so a merge to `main` is a deploy.

**Ground rules for this thread**
- **Plan changes.** A real change to a ruling is a named change order, logged in the
  decision log. Never make a quiet edit.
- **Commentary.** Live and canonical files carry no commentary. Notes go in the
  workstream folder.
- **Pull requests.** One pull request per phase slice. Open it as a draft, push once after
  the local checks pass, then mark it ready. Merge your own pull request when CI is green,
  and check the deploy.
- **Models.** Sonnet drafts, Opus reviews, and Haiku does the mechanical work. The review
  cap is three rounds.
- **Content standard.** Participant-facing text meets the reading bar in `CLAUDE.md`.
  Check it with `engine.m7.turn_readability.score_turn`.
- **Other threads' content.** Don't touch it. Flag it instead: the atlas's 23 drifted
  entries, and the two movement texts in `Open-Gaps.md`.

## Before Phase 1: what the lineage thread has shipped (update of 2026-11-06)

**Already on `main`** (mchadwick25-droid/CIC-Project#1517):
- **The census.** Release 1 has 300 movements and 86 links. Each link has an ID
  (`from--to`, and `--2` for a second link on the same pair), one of six types, one of
  five grades, and sources (file, lines, locus and verbatim quote).
- **Permanence.** `meta.release` and `meta.identifiers` are set, and `retiredLinks` and
  `retiredMovements` start empty.
- **Atlas links.** `atlas-v3.html` takes its links from the census through
  `engine/m6/atlas_html.write_edges`. CI runs
  `python -m engine.m6.cli atlas-check --edges-only`.
- **Validation.** `tools/validate-census.mjs --base` enforces the types, the grades, the
  quotes against `cic/texts`, and permanence.
- **Tree pages.** These group links by type, show confidence, and give every link an
  anchor: `tree/<id>#<link-id>`.

**In review: mchadwick25-droid/CIC-Project#1521.** It adds link colors in four families,
arrowheads, and legend rows that work as on/off switches. Details:
- **Color tokens:** `--link-grow`, `--link-influence`, `--link-conflict` and
  `--link-contact`.
- **Tree pages:** each lineage section gets the class `link-<family>`.
- **Switches:** they write the class `is-off` and keep choices in `localStorage` under
  the key `tree-hidden`.
- **Data attributes:** `data-lane` on `.river-group` and `.node`; `data-family`,
  `data-conf` and `data-lanes` on `.edge-line` and `.edge-hit`.

**What this means for the build:**
- **Do not start Phase 1 until #1521 has merged.** Step 2 moves `atlas-v3.html` and the
  tree pages by pure rename, and #1521 rewrites both. Branch from `main` after it merges.
  The same goes for any edit to `atlas-v3.html` or `generate_tree_pages.mjs`.
- **Saved legend choices reset on the move.** `localStorage` is kept per site, so
  visitors' choices under `tree-hidden` start fresh on the new domain. That is expected.
  Don't try to carry them across.
- **Phase 2's marks and tap areas build on the legend.** The leaf and person marks, and
  the tap areas from rulings 15 and 16, must work with the switches: a hidden lane hides
  its marks and tap areas too. Add the new marks to the legend as rows, in the same style.
- **Checks #1521 did not cover.** It wasn't checked on the light theme, on phones, or
  with a color-vision simulation. Phase 2's phone test (ruling 16) covers phones. Add a
  light-theme check and a color-vision check of the link colors to that same test,
  because the leaf, person and dot marks have to read alongside them.
- **Preset views are not wanted.** Mark declined preset views for now, so don't build
  them.

## Phase 1: the move (one pull request, after #1521 merges and after `Open-Gaps.md` item 7's nameserver step)

1. **Repo map first.** Update the root `README.md` map and `CiC_Repo_Structure_Tracking.md`
   for the tree's new top-level live folder and its Worker config.
2. **Move the tree, by pure rename.** Use `git mv` with no content edits. The map
   (`atlas-v3.html`) becomes the folder's home page. Move the movement pages
   (`tree/`) and the narration (`audio/tree/`) into the new folder. Point the generators,
   the atlas sync check and CI at the new paths.
3. **Second Worker config.** Add one for the tree, reusing `cic-worker/worker.mjs` for
   audio range requests. When you edit `wrangler.jsonc`, remove its existing commentary,
   by the standing rule.
4. **Redirects on the old Worker.** Make them permanent and one hop each.
   - `/tree/<id>` and `/tree/<id>.html` go straight to
     `https://www.churchfamilytree.com/tree/<id>`.
   - Renamed movements go to their new ID in the same hop.
   - `atlas-v3.html`, `atlas.html` and `world-atlas.html` also redirect.
   - `/data/world-census.json` is not redirected. It is served directly at both addresses,
     with identical headers.
5. **Census copy step and checks.**
   - Add a build step that copies the census into both sites, with a CI check that the
     two copies are byte for byte identical.
   - Extend `tools/validate-census.mjs --base` so that every promised ID, retired and
     renamed ones included, resolves on both domains, and every link ID has its anchor on
     its page.
6. **Permanence promise.** Add the domain rule to `meta.identifiers`, the license field to
   `meta`, and ship it as data release 2.
7. **Door switch.**
   - Add a public-open field on each world record, carried into the census by
     `engine/m6/census_sync.py`.
   - A world's door shows only when the field is on, and it lands on the world's own page
     on `churchinconversation.com`.
   - All 11 Built & Live worlds start on.
   - Until any world is open, the tree shows one quiet line instead: "Church in
     Conversation, from the same team."
8. **The tree's own pages.**
   - About and privacy pages: no cookies, no accounts, cookie-free counts.
   - Footer: "A Faithways Studio project", naming Church in Conversation, and linking to
     the license.
   - Cloudflare Web Analytics.
   - A support page saying what a gift pays for on the tree, with Church in Conversation's
     not-a-nonprofit line word for word. Mark makes the two Stripe links; give him the
     steps.
   - One quiet "Support the tree" link in the header and the footer.
9. **Repoint Church in Conversation's links.** The homepage "Church Family Tree" button
   and every tree link go to the new domain.
10. **Mark's dashboard steps.** Give them as exact steps:
    - Create the second Worker build.
    - Attach `www.churchfamilytree.com`, with the bare domain redirecting to `www`.
    - Turn on Web Analytics.
    - Create the Stripe links.
11. **After the deploy, verify.** Every old address redirects in one hop, and the data
    answers on both domains with the same hash. Then draft a short note for Mark to send
    the outside researcher with the new home address.

## Phase 2: the standalone release (built in place on the new domain)

1. **Links, era by era.** Build them in a fresh session per era. Every relationship a
   movement's own text names becomes a sourced link, with a type, confidence, note and
   source. Run two checks: prose to links, and links to prose. Then a full review of the
   whole link set. The sources schema already exists from #1517.
2. **Method page.** It says plainly that every claim is AI-checked and that none is yet
   reviewed by an independent scholar. Also add confidence on every link at a glance.
3. **Data and citation page.** It carries the release, the permanence promise, how to cite,
   the license link, the request form (https://tally.so/r/kb97Br) and the invitation to
   academic review.
4. **Find-your-church search.** It needs a new list of everyday names, because the census's
   informal names are titles.
5. **Gap sweep.** Read only; Haiku and Sonnet do the reading. Then **stop for Mark's ruling
   sitting**. Then the schema additions:
   - the movement-or-person kind
   - a confidence grade on living descent
   - the review-status field
   - Tertullian set to person + A5
   - the Cyrilline duplicate retired with a redirect.

   Then write the agreed entries.
6. **Living definition and flag check.** Write the "living" definition, and check all 169
   flags against it.
7. **Marks and tap areas.**
   - Leaf, person and dot marks: **stop for Mark's pick** among 2 to 4 drawn options.
   - Bigger marks with an on-screen floor.
   - One tap area per movement: 24 px, or 44 px on touch.
   - Test it at phone size.
8. **Gates before launch.** All three come from `Open-Gaps.md`, items 5 and 6:
   - the atlas drift is synced
   - the two movement texts are fixed
   - the public license is live, which it already is.

   Then ship a numbered release, and announce.

## Stop points (everything else, just do)

- **Mark's ruling sitting** on the gap sweep.
- **Mark's pick** of the drawn marks.
- **Paid narration:** sample first, and Mark's approval by ear before the full run. Pass
  every setting explicitly, and print it.
- **Any metered model call.** None is planned. If a gate needs one, stop and ask.
- **Dashboard-only steps.** Give Mark the exact steps.
- **Escalation categories:** a portfolio, governance or method change, or a tension the
  pipeline can't close.
- **Promotion to `live`.** Never do it. It is Mark's call, and it is not needed for the
  site anyway.
