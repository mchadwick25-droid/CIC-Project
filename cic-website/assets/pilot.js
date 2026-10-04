(function (root) {
  "use strict";

  var AUDIENCE = /^[a-z][a-z0-9-]{0,23}$/;

  // The audience a link names in its query (?for=pastors), or general when it names none.
  // Other parameters a link picks up on the way are ignored.
  function audienceOf(search) {
    var params = new URLSearchParams(search || "");
    var name = params.has("for") ? params.get("for") : "general";
    return AUDIENCE.test(name) ? name : null;
  }

  // The app's address for the pack: the audience travels in the fragment, which no server is sent.
  function joinUrl(appOrigin, audience) {
    return appOrigin.replace(/\/+$/, "") + "/#cic-pilot=" + audience;
  }

  var api = { audienceOf: audienceOf, joinUrl: joinUrl };
  root.CicPilot = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;

  if (!root.document || !root.GoDeeperConfig) return;
  var config = root.GoDeeperConfig;
  // Nothing shows until the pilot is opened in the site's config, so a link found early shows an empty page.
  if (!config.pilot) return;
  var audience = audienceOf(root.location.search);
  if (!audience) return;
  var end = root.document.querySelector('[data-pilot-end="' + audience + '"]');
  if (!end) return;
  end.hidden = false;
  root.document.getElementById("pilot-button").setAttribute("href", joinUrl(config.app, audience));
  root.document.getElementById("pilot-offer").hidden = false;
})(typeof window !== "undefined" ? window : this);
