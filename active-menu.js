(function () {
  function normalizePath(value) {
    var raw = String(value || "");

    if (raw === "") return "/";
    if (/^(mailto:|tel:|javascript:|#)/i.test(raw)) return "";

    raw = raw.replace(/\\/g, "/");

    try {
      var url = new URL(raw, window.location.origin);
      if (url.origin === window.location.origin) {
        raw = url.pathname;
      } else if (/^https?:\/\//i.test(raw)) {
        return "";
      }
    } catch (e) {
      raw = raw.split("#")[0].split("?")[0];
    }

    raw = raw.split("#")[0].split("?")[0];
    raw = raw.replace(/\/+/g, "/");

    if (raw === "") return "/";
    if (raw.charAt(0) !== "/") raw = "/" + raw;

    raw = raw.replace(/\/+/g, "/");

    if (raw === "/index.html") return "/";
    if (raw.length > 1 && raw.endsWith("/")) raw = raw.slice(0, -1);
    if (raw === "/index.html") return "/";

    return raw || "/";
  }

  function fallbackTarget(normalizedCurrentPath) {
    var current = normalizePath(normalizedCurrentPath).replace(/^\//, "");
    var target = "";

    if (current === "") target = "/";
    else if (current === "kontakty.html") target = "/";
    else if (current === "dokumenty.html" || current.indexOf("dokumenty-") === 0) target = "/dokumenty.html";
    else if (current === "zbir.html" || current.indexOf("zbir-") === 0) target = "/zbir.html";
    else if (current === "vidhody.html" || current.indexOf("vidhody-") === 0 || current.indexOf("promyslovi-vidhody") === 0 || current === "kabelni-vidhody.html") target = "/vidhody.html";
    else if (current === "kudy-zdaty.html" || current.indexOf("kudy-zdaty-") === 0) target = "/kudy-zdaty.html";
    else if (current.indexOf("sortuvannya/") === 0 || current.indexOf("sortuvannya-") === 0 || current === "sortuvannya.html") target = "/sortuvannya.html";
    else if (current.indexOf("logistyka/") === 0 || current.indexOf("logistyka-") === 0 || current === "logistyka.html") target = "/logistyka.html";
    else if (current.indexOf("pererobka/") === 0 || current.indexOf("pererobka-") === 0 || current === "pererobka.html" || current === "chy-potribno-pererobyty-chy-utylizuvaty.html") target = "/pererobka.html";
    else if (current.indexOf("yak-") === 0 || current.indexOf("spysannya-") === 0 || current.indexOf("likvidaciya-") === 0 || current.indexOf("povernennya-") === 0 || current.indexOf("akt-") === 0 || current.indexOf("fotozvit-") === 0) target = "/utylizaciya.html";
    else if (current.indexOf("utylizaciya/") === 0 || current.indexOf("utylizaciya-") === 0 || current.indexOf("utilizaciya-") === 0 || current === "utylizaciya.html") target = "/utylizaciya.html";

    return target ? normalizePath(target) : "";
  }

  var currentPath = normalizePath(window.location.pathname);
  var links = document.querySelectorAll("nav a[href], .sidebar a[href]");
  var allSidebarLinks = [];
  var matches = [];

  links.forEach(function (a) {
    a.classList.remove("active", "current");
    a.removeAttribute("aria-current");

    var normalizedHref = normalizePath(a.getAttribute("href"));
    allSidebarLinks.push({ node: a, path: normalizedHref });

    if (normalizedHref && normalizedHref === currentPath) {
      matches.push(a);
    }
  });

  if (matches.length === 0) {
    var fallbackPath = fallbackTarget(currentPath);
    if (fallbackPath) {
      allSidebarLinks.forEach(function (item) {
        if (!matches.length && item.path === fallbackPath) {
          matches.push(item.node);
        }
      });
    }
  }

  if (matches.length > 0) {
    matches[0].classList.add("active");
    matches[0].setAttribute("aria-current", "page");
  }
})();
