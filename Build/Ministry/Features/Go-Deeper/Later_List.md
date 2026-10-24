# Go Deeper — Later list

Append-only. A merged entry's number never changes.

1. 2026-10-24, landing page drawer: the button shows whenever the site's `GoDeeperConfig.enabled` is on, but the panel only draws if the app was built with `VITE_DEEPER_ENABLED=on`. If the two ever differ, the drawer would be empty. A shared switch is not built.
2. 2026-10-24, landing page drawer: the account home and sign-in opened from the panel inside the frame were not tried; accounts are switched off by default. Try them when accounts go on.
3. 2026-10-24, landing page drawer: the drawer does not trap keyboard focus; Tab can reach the page behind it. Escape closes it and focus returns to the button.
4. 2026-10-24, landing page drawer: the frame was tried only on localhost (site on one port, app on another). Try it on the live site and app domains after promotion.
5. 2026-10-24, landing page drawer: `GoDeeperConfig.drawer` in `cic-website/assets/go-deeper-config.js` ships `false`. After the promotion that puts the panel-only app on `live`, set it to `true` in a small pull request, then check the drawer on the live domains (item 4).
