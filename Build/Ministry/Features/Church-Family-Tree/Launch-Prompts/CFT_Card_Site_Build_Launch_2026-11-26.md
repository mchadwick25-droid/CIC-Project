# Church Family Tree: the card site build (2026-11-26)

Paste the part below the line as the first message of a new session.

---

Build the new card layout on churchfamilytree.com for every kind of card: tradition, person, council and era. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Stage-Two-Kit/Kit.md` (sections 1 to 3), which is the specification, and the Decision-Log entries it cites.

**Scope.** `cft-website/index.html` (the map's card panel), `Build/tools/generate_tree_pages.mjs` (the tree pages), `tools/validate-census.mjs` and the census schema in `cic-website/data/world-census.json` (`meta`): a place for each tradition's and council's card sources, open questions, quotation originals and timeline (periods, each with lines of `when`, `text`, reference), and the short description. The layout works with today's recordings and with none. The Family line view opens from the card's direct line; its forest green is replaced by a color that passes the color-vision check against the gold influence and red lines on its own. Keep Read along and search working.

**Order.** First a mock with two real cards for Mark (one tradition, one person), at phone and desktop width, in an Artifact. Build only after he says yes. No content is written here: cards without a timeline yet show their other sections. Tests and the census validator for every new field.

**Release.** One pull request, merged when CI is green; check the live site. Report to the coordinator.
