# Go Deeper — Later list

Append-only. A merged entry's number never changes.

1. 2026-10-24, landing page drawer: the button shows whenever the site's `GoDeeperConfig.enabled` is on, but the panel only draws if the app was built with `VITE_DEEPER_ENABLED=on`. If the two ever differ, the drawer would be empty. A shared switch is not built.
2. 2026-10-24, landing page drawer: the account home and sign-in opened from the panel inside the frame were not tried; accounts are switched off by default. Try them when accounts go on.
3. 2026-10-24, landing page drawer: the drawer does not trap keyboard focus; Tab can reach the page behind it. Escape closes it and focus returns to the button.
4. 2026-10-24, landing page drawer: the frame was tried only on localhost (site on one port, app on another). Try it on the live site and app domains after promotion.
5. 2026-10-24, landing page drawer: `GoDeeperConfig.drawer` in `cic-website/assets/go-deeper-config.js` ships `false`. After the promotion that puts the panel-only app on `live`, set it to `true` in a small pull request, then check the drawer on the live domains (item 4).
6. 2026-10-26, landing page drawer: `GoDeeperConfig.drawer` is now `true` (resolves item 5). Item 4, trying the drawer on the live domains, is done by the pull request that turned it on.
7. 2026-10-26, Render: auto-deploy for cic-engine was left off by the manual rollback. Turning it back on is Mark's call in the dashboard (Settings, Deploy).
8. 2026-10-26, the 404 that followed promotion 1131 (the accounts fixes, the LPC records and the ledger work, with this thread's panel) has no known cause. The pieces other than this thread's are still to be promoted one at a time.
9. 2026-10-26, from Mark's live screenshot: the conversation's top-bar "Get more conversations" button shows a tight yellow box with the text touching its edges (possibly the focus outline); the panel's text runs close to its right edge; the message box shows a scrollbar with almost no text. None looked at yet.
10. 2026-10-26, the panel's "Get more conversations" link opens a popup of `go-deeper.html`, which reads "Codes are not on sale yet" while buying is suspended (ruling 80). Whether the link should show, or go elsewhere, is Mark's call.
