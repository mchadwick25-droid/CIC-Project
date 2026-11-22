# Church Family Tree, phone loading, step 3: launch

Paste this as the first message of a new session.

---

Run step 3 of the Church Family Tree phone loading project (Open-Gaps 352): change the map so it starts from the slim page and loads each card's text when the card opens, then switch the deploy to the slim page. Steps 1 and 2 are done and merged. Mark, 2026-11-22: "yes, check how it loads on phones", then "go ahead with the build step". Phones are two thirds of visits; on an emulated mid-range phone the map shows its names after about 5.1 s on Wi-Fi, 6.7 s on 4G and 16.7 s on slow 4G, because the page is 9.6 MB (2.6 MB compressed) of embedded data.

**Read first, in this order.** `CLAUDE.md`. Open-Gaps 352 and the Decision-Log entries "Phone loading: the audit is done" and "Phone loading, step 2" (both 2026-11-22). `Build/Ministry/Operations/Audits/2026-11-22_cft-phone-loading-audit/README.md` and its `startup_fields.json` and `scripts/`. `tools/slim_map_data.mjs`, `tools/slim_map_fields.json` and `tools/tests/slim_map_data.test.mjs`. Mark's plan page (private, an Artifact): https://claude.ai/artifact/Y5wc4XWqaxg6o5XjHY4fQt.

**What exists.** The full data stays in `cft-website/index.html` in git, so `atlas-sync`, the validators, the tests and the story kit keep working. `node tools/slim_map_data.mjs` makes the slim copy in `.build/tree-slim/`: a page of 1.28 MB (0.35 MB compressed) with only the start-up fields and a SHA-256 of each long description (`descHash`), 629 files `data/entries/<id>.json` (median 9.9 KB, largest 34 KB) and one `data/edges-detail.json` (1.08 MB, link sources and the rest of each link). The stories (0.21 MB) and the link tooltip text (`note`, 0.20 MB) stay in the page. Nothing reads or deploys the slim copy yet.

**The job.**
1. **A loader** in the map's script, `ensureEntry(m)`: fetch `data/entries/<id>.json` once, cache the promise, merge it into the entry object (arrays merge by index, as `merge` in `tools/slim_map_data.mjs` does). On the full page, where the fields are already there, it does nothing, so the committed page, the tests and local work behave as today. `ensureEdgesDetail()` does the same for the link card.
2. **Call it where the audit says card-only fields are first read:** `openPanel` for a tradition, a built world, a person and a council, `openPersonCard` (people list rows and names), a deep link `?world=<id>` (fetch before opening), and `openPanelEdge`. Load ahead on hover and keyboard focus. A phone has no hover, so decide and measure what to do about the first tap (for example the start of a press, or idle loading of the cards in view) and say what you chose.
3. **An error and retry state** in the card. A card must never show half filled.
4. **The audio check** (`treeAudioCurrent`, near the `sha256Hex` calls) uses `m.descHash` when it is there and hashes `m.longDescription` when that is.
5. **The deploy.** `tools/build_tree_site.mjs` writes the slim page and data files into `.build/tree` in place of the full `index.html`; the committed page stays the source. Check `wrangler.cft.jsonc`, the CI job "Tree site build" and the Worker: `cic-worker/worker.mjs` builds the link-preview page for LinkedIn and other crawlers from the head of `index.html`, so test that it still works on the slim page.

**Proof, all before Mark sees anything.**
- **Same cards.** Open all 629 entries on the full page and on the slim page served from the build output, and compare each panel's HTML (and the people list and person card where they apply). Zero differences, with the fetch path exercised.
- **No hidden early read.** At 1440 px and at 390 px, nothing at start-up reads a field the slim page lacks. The audit ran only at 1440 px, so this is new work (`Build/Ministry/Operations/Audits/2026-11-22_cft-phone-loading-audit/scripts/build_tracer.py` is the tool).
- **Paths.** A deep link, the keyboard (Enter on a mark, focus handling as today), the error path (block the fetch: the card shows the error, the retry works), recordings still show their players, and a link card.
- **Timings.** An emulated Pixel 5, processor slowed four times, a fresh cache, at Wi-Fi, 4G (9 Mbps, 150 ms) and slow 4G (1.6 Mbps, 150 ms), before and after, with bytes. The estimate to beat or explain: names after about 3 s on Wi-Fi and about 5 s on slow 4G.
- The census validator, census tests, tree page tests, worker tests, `tools/tests/slim_map_data.test.mjs`, live commentary, American spelling and the Open-Gaps number check.

**Lessons from this thread.**
- The map needs `cic-website/assets` and `cic-website/data` beside it, so a local copy needs symlinks to them. The legend choices (People on, and so on) persist in `localStorage` across reloads in one browser context.
- `window.innerWidth` forces a layout when the page is dirty; `narrowScreen()` now reads a cached value. Do not reintroduce live reads in start-up paths.
- Placement code (`placeCompactPeople`, `labelFitRun`) builds a fresh collision grid on each run; calling a piece of it twice on one grid makes things collide with themselves.
- The tracer proxies replace objects with proxies; code that compares objects by identity still works because the proxies are cached per object.
- Cloudflare builds can take 9 minutes or more when queued; wait for the new code to appear on the live page before checking it.

**Stops for Mark:** the draft pull request with before and after screenshots at several zooms, the timings, and the render-equality result. Merging deploys churchfamilytree.com at once, so Mark's look comes first. Choices he may change: the link tooltip text and the stories staying in the page.

**Release.** One pull request, a draft first; push once after the local checks pass, merging the latest `main` in as the last step. After the merge, wait for the deploy, then fetch the live page, open a card, and re-run the timings against the live site. Log it in the Decision-Log and Open-Gaps 352, append only.
