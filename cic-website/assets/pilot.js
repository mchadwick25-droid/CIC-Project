(function (root) {
  "use strict";

  var LINK = /^[A-Za-z0-9_-]{1,64}$/;

  function linkOf(search) {
    var params = new URLSearchParams(search || "");
    var name = params.has("for") ? params.get("for") : "general";
    return LINK.test(name) ? name : null;
  }

  var ROLE = /^[a-z_]{1,32}$/;

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
  if (root.location.search && root.history && root.history.replaceState) root.history.replaceState(null, "", root.location.pathname);
  if (!config.pilot || !link) return;
  var form = root.document.getElementById("pilot-form");
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var target = joinUrl(config.app, link, form.elements.role.value);
    if (target) root.location.assign(target);
  });
  root.document.getElementById("pilot-offer").hidden = false;
})(typeof window !== "undefined" ? window : this);
