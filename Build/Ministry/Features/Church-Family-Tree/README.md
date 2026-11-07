# Church Family Tree — workstream

**What this is:** the Church Family Tree as Faithways Studio's second product, on its own
domain, `https://www.churchfamilytree.com`. It stands alone, and it opens a second door into
Church in Conversation for every world that is open to the public.

**Status:** converged 2026-11-06 ("Converged, auto mode"). Phase 1, the move, is ready to
start in a fresh build thread. Nothing is built yet.

## What is in this folder

- **`Decision-Log.md`** — every ruling, with its reasoning. Start here.
- **`Open-Gaps.md`** — known gaps and open items, numbered and append-only.
- **`Launch-Prompts/CFT_Build_Launch_2026-11-06.md`** — the prompt that starts the build
  thread, with the build steps in order.

## Where the tree's parts live

| what | where |
|---|---|
| The map | `cft-website/index.html` |
| Movement pages (generated) | `cft-website/tree/<id>.html`, from `Build/tools/generate_tree_pages.mjs` |
| The census (hand-edited) | `cic-website/data/world-census.json`, validated by `tools/validate-census.mjs` |
| Narration | `cft-website/audio/tree/` |
| Design history | `../Atlas-World-Map/` |
| License policy | `cic-website/license.html` (live) |

The census stays in `cic-website/data/` and is copied, byte for byte, into the tree's site at deploy time. The old addresses on `churchinconversation.com` redirect to the tree's domain (P1c, 2026-11-07).