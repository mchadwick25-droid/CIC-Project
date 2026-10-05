(function (root) {
  "use strict";
  // The two addresses the Go Deeper pages talk to, in one place. The app's own
  // VITE_DEEPER_SITE_ORIGIN and the server's CIC_DEEPER_SITE_ORIGIN must name
  // this site's exact origin.
  var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;
  // Off until Go Deeper is turned on, so the home and Get Involved pages make no
  // request to a route that does not exist yet.
  root.GoDeeperConfig = {
    enabled: true,
    // On when a pilot audience is open; off, the pilot page shows nothing.
    pilot: false,
    app: isLocal ? "http://localhost:5173" : "https://cic-engine-staging.onrender.com",
    api: isLocal ? "http://localhost:8000" : "https://cic-engine-staging.onrender.com",
  };
})(window);
