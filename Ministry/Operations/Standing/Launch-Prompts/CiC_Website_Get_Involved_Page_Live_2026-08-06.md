# Funding Strategy Thread → Website Design Thread — `support.html` rebuilt, needs to go live

**What this is:** a handoff from the Funding Strategy thread to whichever thread owns
`churchinconversation.com`'s actual deployment. The page content is done, committed, and
pushed to `main` — this dispatch is asking that thread to get it live and confirm back.

---

## What changed

`cic-website/support.html` was rebuilt from scratch, live with Mark, replacing the old
"Help us open more seats at the Table" version (single undifferentiated giving pool, no
real cost figures). Full line-by-line derivation of every decision is in
`Ministry/Features/Funding-Strategy/Decision-Log.md`, 2026-08-06 entry — not repeated here,
but the short version:

- **New title/framing:** "Help Us Open the Door a Little Wider" — door imagery chosen
  deliberately (already part of the brand) over an alternative "more chairs at the Table"
  direction, both real options Mark weighed.
- **Real cost figures**, grounded in `CiC_Cost_Study_Per_Transaction_V0_1.md`: ~$2/hour for
  a 1:1 conversation, up to $5/hour for a full three-Representative table.
- **Four-part response** replacing the old copy: cost reduction, "less expensive features"
  (Atlas + Tours, grounded in the Atlas README and Tour Experience Module Strategy doc), an
  Accessibility Fund, and a new Academic Review Fund (external scholarly review — this is a
  new giving option that didn't exist on the old page).
- **A new "Why It's Worth It" section** — an Old Testament/Church parallel, live-verified
  against BibleProject's own published framing (not invented) before being adapted to this
  page's own wording.
- **Nav renamed sitewide**: "Support" → "Get Involved", on all 8 pages that link here
  (`index.html`, `about.html`, `whats-next.html`, `atlas-v3.html`, `tour.html`,
  `privacy.html`, `pilot-feedback.html`, `support.html` itself), plus the page's own
  `<title>` tag. **The URL/filename deliberately did not change** — still `support.html`,
  not `get-involved.html` — because that exact URL was just given to Stripe as part of an
  active compliance review (see below); renaming the file would have broken that link.

**Committed and pushed:** commit `b0e5583` on `main`, verified against `origin/main`
directly. `git diff` on that commit has the full before/after for every file touched.

## What's intentionally not done yet — not a bug, a scope call

- **The interactive Stripe checkout from the old page was removed, not carried over.** The
  old version had real working JS calling `/api/support/checkout` for one undifferentiated
  amount. The new page has a plain "email us" contact prompt instead, per Mark's explicit
  instruction ("for now i just want text, not the stripe yet"). Real checkout wiring for two
  *separately-designated* funds (Accessibility vs. Academic Review) is genuine follow-up
  work — the existing endpoint only supports one amount, not a fund selection, so this isn't
  a quick restore of the old code.
- **The closing "Be Part of It" section is the plain, functional version**, not a more
  narrative "join us" invitation. An earlier attempt at that was explicitly rejected by Mark
  as too abstract; he wants to think through "what are they joining" further before that
  section gets revisited. Don't treat the current closing section as finished/final — it's
  usable as-is, just not the intended end state.

## Why this needs the website-design thread specifically, not just a git push

Per `cic-website/README.md`'s own deployment section, this site deploys via **Cloudflare
Pages, connected to Git, auto-deploying on every push to the connected branch** — this
thread doesn't have visibility into whether that Cloudflare Pages project is actually
connected and live yet, or still a documented-but-unexecuted setup step. If it's already
connected, this change may already be live with no further action. If not, this is the
blocking step.

**Ask: confirm actual live status at `churchinconversation.com/support.html`** (or wherever
it's actually served), and complete the Cloudflare Pages connection/deploy if it isn't done
yet. Report back either way — "already live, confirmed" or "deployed just now" or "blocked
on X" — so this thread and Mark both know where it actually stands, not just where the repo
stands.

## Completion criteria

Same convention as every other cross-thread dispatch in this project: a dated log entry
wherever this lands confirming live status, plus anything found broken or blocking flagged
back rather than silently worked around.
