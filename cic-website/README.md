# Church in Conversation — public website

A plain static site (no build step, no framework) for churchinconversation.com
(primary) and churchinconversation.org (kept registered, redirects to .com).
Brand system: `Build/Ministry/Communication/Brand-Assets/`
and `CiC_Messaging_Branding_Kit_QuickRef_V0_1.md`.

## Pages

- `index.html` — Home
- `about.html` — Mission, the Five Convictions, How It Works, Safety & Disclosure, About Us
- `support.html` — "Get Involved," rewritten with real cost figures; see its own
  header comment and the funding-strategy decision record under
  the project's private funding-strategy material for the full derivation. Currently
  unlinked from the site nav — needs a content refresh; the homepage's own
  "Keep the Door Open" section carries the real Stripe give links directly,
  so giving still works with this page unlinked. Names one fund,
  Accessibility, with real checkout live — two Stripe Payment Links
  (one-time and monthly), both feeding that one fund, no server involved;
  see the page's own header comment for which link is which.

- `pilot.html` — the pilot's offer and its "Get my free pack" link into the app. Unlisted, noindex, empty until `pilot: true` in `assets/go-deeper-config.js`; the audience comes from `?for=`. Script: `assets/pilot.js`.
- `go-deeper.html` and `go-deeper-return.html` — Go Deeper: how a code lets a
  conversation carry on, and the page Stripe sends a buyer back to, which shows
  the code. Switched off: nothing links to them, they are marked noindex, and
  the buy button stays hidden until a Payment Link is set in the page. The
  shared script is `assets/go-deeper.js`. Decision record under
  the project's private funding-strategy material.

Copy is pulled directly from `Vision, Mission, Convictions, and Foundational
Commitments V1.1.docx` and the Messaging & Branding Kit — not written fresh.
**Faithways Studio, Inc. is incorporated** (Colorado Public Benefit
Corporation, Entity ID 20261918758; not a nonprofit, no 501(c)(3),
contributions are not tax-deductible). The Support page's giving mechanics
(see the Pages section above) are built around the monetization ladder in
the project's private go-live cost model, not charitable-deductibility
framing — see that file before changing the ask copy or amounts.

## Deploying (Cloudflare Pages — free tier, recommended)

1. Push this `cic-website/` folder to its own GitHub repo (a subfolder of the
   main CiC-Project monorepo also works if you set the Pages build's "root
   directory" to `cic-website`).
2. In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect
   to Git**, pick the repo, leave build command blank and output directory as
   `/` (or `cic-website` if deploying from the monorepo root).
3. Cloudflare gives you a `*.pages.dev` URL immediately — check it renders
   before touching DNS.
4. **Custom domains:** in the Pages project → Custom domains → add
   `churchinconversation.com` (make it primary — the entity is now a for-profit
   PBC, and .org read as nonprofit-coded) and `churchinconversation.org` (set
   to redirect to `.com` — keep it registered, don't let it lapse, so old
   links still resolve). If your domains' DNS isn't already on Cloudflare,
   it'll walk you through nameserver changes; if they are, custom domains
   attach in a couple of clicks with no email downtime.
5. Every subsequent push to the connected branch auto-deploys. No server,
   no ongoing hosting cost.

## Editing

Plain HTML/CSS, no build tooling — edit the `.html` files directly and the
shared look lives in `assets/style.css`. Fonts (Alegreya + Alegreya Sans) load
from Google Fonts via the `<link>` tags already in each page's `<head>` — a
real website isn't subject to the CSP restrictions that block this inside a
Claude Artifact, so no need to self-host or inline the font files.

## Known follow-ups, not yet done

- The "How It Works" and "Safety & Disclosure" sections on the About page
  were written directly from the Vision doc and Constitution's own
  commitments (Article 17/Article 6-adjacent language) — worth a brand-kit
  compliance pass before this goes fully public, same as any other CiC
  public copy.
- No favicon raster exports yet (BR-17 in the System Hub tracker covers
  this) — the SVG favicon works in modern browsers but a proper `.ico`/PNG
  set would cover older clients and app icons.
- Consider adding the Article 31 external-review disclosure once that
  process is further along — the positioning brief's own overclaim register
  says not to claim "scholarly validated" before that's true, and this site
  currently doesn't make that claim, which is correct for now.
