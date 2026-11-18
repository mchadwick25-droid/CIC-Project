(function (root) {
  "use strict";

  function apply(doc, config) {
    if (!config || config.enabled !== true) return false;
    var section = doc.getElementById("go-deeper");
    var oneJob = doc.getElementById("cookie-one-job");
    var twoJobs = doc.getElementById("cookie-two-jobs");
    if (!section || !oneJob || !twoJobs) return false;
    section.hidden = false;
    twoJobs.hidden = false;
    oneJob.hidden = true;
    return true;
  }

  var ACCOUNT_PARTS = [
    "accounts-optional", "accounts-holds", "accounts-signin", "accounts-back", "accounts-delete",
    "accounts-review", "accounts-services", "accounts-retention",
  ];

  function applyAccounts(doc, config) {
    if (!config || config.accounts !== true) return false;
    var parts = ACCOUNT_PARTS.map(function (id) { return doc.getElementById(id); });
    if (parts.some(function (part) { return !part; })) return false;
    parts.forEach(function (part) { part.hidden = false; });
    return true;
  }

  var api = { apply: apply, applyAccounts: applyAccounts };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.PrivacyGoDeeper = api;
    if (root.document) {
      apply(root.document, root.GoDeeperConfig);
      applyAccounts(root.document, root.GoDeeperConfig);
    }
  }
})(typeof window !== "undefined" ? window : this);
