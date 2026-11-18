# Church Family Tree — workstream

**What this is:** the Church Family Tree as Faithways Studio's second product, on its own
domain, `https://www.churchfamilytree.com`. It stands alone, and it opens a second door into
Church in Conversation for every world that is open to the public.

**Status (2026-11-15):** live at churchfamilytree.com, which deploys from `main`. Eras 1 to 10
have their traditions and stories. Eras 1 to 4 have Who profiles, and eras 1 to 3 have major
councils. The first milestone is eras 1 to 7 complete for public release (Mark, 2026-11-15). The
work runs in three threads under one coordinator: live fixes, the Library, and writing. The Who
writing standard is being re-set from Mark's rulings of 2026-11-15 (`Decision-Log.md`). No new
Who or council text is written until he approves it.

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