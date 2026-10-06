(function (root) {
  "use strict";

  // A public audience's name or a private audience's secret key. The page cannot tell which, and does not need to.
  var LINK = /^[A-Za-z0-9_-]{1,64}$/;

  // The link a page address names (?for=...), or general when it names none. Other parameters are ignored.
  function linkOf(search) {
    var params = new URLSearchParams(search || "");
    var name = params.has("for") ? params.get("for") : "general";
    return LINK.test(name) ? name : null;
  }

  // The app's address for the pack: the link travels in the fragment, which no server is sent.
  function joinUrl(appOrigin, link) {
    return appOrigin.replace(/\/+$/, "") + "/#cic-pilot=" + link;
  }

  var api = { linkOf: linkOf, joinUrl: joinUrl };
  root.CicPilot = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;

  if (!root.document || !root.GoDeeperConfig) return;
  var config = root.GoDeeperConfig;
  var link = linkOf(root.location.search);
  // A private audience's key is a password: it leaves the address bar and the history at once, before anything else can return.
  if (root.location.search && root.history && root.history.replaceState) root.history.replaceState(null, "", root.location.pathname);
  // Nothing shows until the pilot is opened in the site's config, so a link found early shows an empty page.
  if (!config.pilot || !link) return;
  root.document.getElementById("pilot-button").setAttribute("href", joinUrl(config.app, link));
  root.document.getElementById("pilot-offer").hidden = false;
})(typeof window !== "undefined" ? window : this);
