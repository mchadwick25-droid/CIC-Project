# Church in Conversation — public website

A plain static site (no build step, no framework) for churchinconversation.com
(primary) and churchinconversation.org (kept registered, redirects to .com).
Brand system: `Ministry/Communication/Brand-Assets/`
and `CiC_Messaging_Branding_Kit_QuickRef_V0_1.md`.

## Pages

- `index.html` — Home
- `about.html` — Mission, the Five Convictions, How It Works, Safety & Disclosure, About Us
- `support.html` — **Pulled from nav 2026-07-22, no page currently links here.** Funding
  strategy and support gifts are held for Phase 1 of the launch, per Mark's direct
  decision — the first priority after go-live is participant feedback, not a giving ask.
  File kept on disk as a status record, not deleted; see its own header comment and
  `Ministry/Features/Funding-Strategy/` (a converged five-phase roadmap already exists
  there) for what happens when this picks back up.

Copy is pulled directly from `Vision, Mission, Convictions, and Foundational
Commitments V1.1.docx` and the Messaging & Branding Kit — not written fresh.
**Entity status (updated 2026-07-21): Faithways Studio, Inc. is incorporated**
(Colorado Public Benefit Corporation, Entity ID 20261874960; not a nonprofit,
no 501(c)(3), contributions are not tax-deductible). The Support page's giving
mechanics, when it goes live, are built around the monetization ladder in
`Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md`, not charitable-deductibility
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

- **Resolved, 2026-07-21:** every page's contact link now points to
  `info@churchinconversation.com` — Mark confirmed this is the real mailbox
  he set up for the general website link (matching the product-identity Zoho
  mailbox from the entity-formation update). The earlier `hello@` address
  this site briefly used is retired.
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
