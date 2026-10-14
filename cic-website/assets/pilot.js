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

  // One of the join form's role values. The server holds the list and checks it.
  var ROLE = /^[a-z_]{1,32}$/;

  // The app's address for the pack: the link and the chosen role travel in the fragment, which no server is sent.
  function joinUrl(appOrigin, link, role) {
    if (!LINK.test(link || "") || !ROLE.test(role || "")) return null;
    return appOrigin.replace(/\/+$/, "") + "/#cic-pilot=" + link + "&role=" + role;
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
  var form = root.document.getElementById("pilot-form");
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var target = joinUrl(config.app, link, form.elements.role.value);
    if (target) root.location.assign(target);
  });
  root.document.getElementById("pilot-offer").hidden = false;
})(typeof window !== "undefined" ? window : this);
