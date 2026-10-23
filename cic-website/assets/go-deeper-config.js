(function (root) {
  "use strict";
  // The two addresses the Go Deeper pages talk to, in one place. The app's own
  // VITE_DEEPER_SITE_ORIGIN and the server's CIC_DEEPER_SITE_ORIGIN must name
  // this site's exact origin.
  var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;
  // Off, the privacy page keeps its Go Deeper section hidden.
  root.GoDeeperConfig = {
    enabled: true,
    // On when a pilot audience is open; off, the pilot page shows nothing.
    pilot: true,
    app: isLocal ? "http://localhost:5173" : "https://app.churchinconversation.com",
    api: isLocal ? "http://localhost:8000" : "https://app.churchinconversation.com",
  };
})(window);
