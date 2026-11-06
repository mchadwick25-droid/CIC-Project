(function (root) {
  "use strict";
  var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;
  root.GoDeeperConfig = {
    enabled: true,
    accounts: true,
    pilot: true,
    drawer: true,
    app: isLocal ? "http://localhost:5173" : "https://app.churchinconversation.com",
    api: isLocal ? "http://localhost:8000" : "https://app.churchinconversation.com",
  };
})(window);
