(function (root) {
  "use strict";

  // Shows the Go Deeper parts of the privacy page only when Go Deeper is on,
  // and swaps the one-job cookie paragraph for the two-job one.
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

  var api = { apply: apply };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.PrivacyGoDeeper = api;
    if (root.document) apply(root.document, root.GoDeeperConfig);
  }
})(typeof window !== "undefined" ? window : this);
