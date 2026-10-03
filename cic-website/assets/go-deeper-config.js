(function (root) {
  "use strict";
  // The two addresses the Go Deeper pages talk to, in one place. The app's own
  // VITE_DEEPER_SITE_ORIGIN and the server's CIC_DEEPER_SITE_ORIGIN must name
  // this site's exact origin.
  var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;
  root.GoDeeperConfig = {
    app: isLocal ? "http://localhost:5173" : "https://cic-engine.onrender.com",
    api: isLocal ? "http://localhost:8000" : "https://cic-engine.onrender.com",
  };
})(window);
