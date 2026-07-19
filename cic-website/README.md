# Church in Conversation — public website

A plain static site (no build step, no framework) for churchinconversation.org
and churchinconversation.com. Brand system: `Ministry/Communication/Brand-Assets/`
and `CiC_Messaging_Branding_Kit_QuickRef_V0_1.md`.

## Pages

- `index.html` — Home
- `about.html` — Mission, the Five Convictions, How It Works, Safety & Disclosure, About Us
- `support.html` — Nonprofit status (honest, current) and how to support the work

Copy is pulled directly from `Vision, Mission, Convictions, and Foundational
Commitments V1.1.docx` and the Messaging & Branding Kit — not written fresh.
The Support page deliberately does **not** have a live "Donate" button: the
entity isn't incorporated yet, so a direct public giving flow would either be
non-deductible or misleading. It routes interested supporters to email
instead, and states current status plainly. Update this page as each real
milestone lands (incorporation this week; EIN; 501(c)(3) determination,
expected ~Q1 2027 per the funding plan) — search this file for "In formation"
and "not yet a recognized 501(c)(3)" when that's ready to change.

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
   `churchinconversation.org` (make it primary) and `churchinconversation.com`
   (set to redirect to `.org`, the standard nonprofit convention — avoids
   duplicate-content SEO issues and picks one canonical identity). If your
   domains' DNS isn't already on Cloudflare, it'll walk you through
   nameserver changes; if they are, custom domains attach in a couple of
   clicks with no email downtime.
5. Every subsequent push to the connected branch auto-deploys. No server,
   no ongoing hosting cost.

## Editing

Plain HTML/CSS, no build tooling — edit the `.html` files directly and the
shared look lives in `assets/style.css`. Fonts (Alegreya + Alegreya Sans) load
from Google Fonts via the `<link>` tags already in each page's `<head>` — a
real website isn't subject to the CSP restrictions that block this inside a
Claude Artifact, so no need to self-host or inline the font files.

## Known follow-ups, not yet done

- `hello@churchinconversation.org` needs to actually exist (set up email
  forwarding/hosting on the domain, or point it at a real inbox) before
  publishing — it's referenced on every page.
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
