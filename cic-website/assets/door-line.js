(function (root) {
  "use strict";

  // Shows the one line about the free conversations this week, when the server
  // has one. With nothing to say, or any failure, the page stays as it was.
  function show(target, body) {
    if (!target || !body || typeof body.line !== "string" || !body.line) return false;
    target.textContent = body.line;
    target.hidden = false;
    return true;
  }

  function load(target, env) {
    return env
      .fetch(env.apiBase + "/api/deeper/door", { credentials: "omit", referrerPolicy: "no-referrer" })
      .then(function (response) {
        return response.ok ? response.json() : null;
      })
      .then(function (body) {
        return show(target, body);
      })
      .catch(function () {
        return false;
      });
  }

  var api = { show: show, load: load };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.DoorLine = api;
    var target = root.document && root.document.getElementById("door-line");
    if (target && root.GoDeeperConfig && root.GoDeeperConfig.enabled) load(target, { fetch: root.fetch.bind(root), apiBase: root.GoDeeperConfig.api });
  }
})(typeof window !== "undefined" ? window : this);
