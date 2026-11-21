// Color theme (system / light / dark), the mobile menu, and the table of contents.
// Loaded in <head> without defer so the theme is applied before first paint.
(function () {
  "use strict";

  var root = document.documentElement;
  var STORAGE_KEY = "theme";
  var SETTINGS = ["system", "light", "dark"];
  var prefersDark = window.matchMedia("(prefers-color-scheme: dark)");

  root.classList.add("js");

  function savedSetting() {
    try {
      var value = localStorage.getItem(STORAGE_KEY);
      return SETTINGS.indexOf(value) === -1 ? "system" : value;
    } catch (e) {
      return "system"; // storage blocked (e.g. private mode)
    }
  }

  function applySetting(setting) {
    var theme = setting === "system" ? (prefersDark.matches ? "dark" : "light") : setting;
    root.setAttribute("data-theme-setting", setting);
    root.setAttribute("data-theme", theme);

    var toggle = document.getElementById("light-toggle");
    if (toggle) {
      toggle.title = "Color theme: " + setting;
    }
  }

  function saveSetting(setting) {
    try {
      localStorage.setItem(STORAGE_KEY, setting);
    } catch (e) {
      // The choice still applies to this page view.
    }
  }

  applySetting(savedSetting());

  // Follow the OS when it changes and the setting is "system".
  var onSystemChange = function () {
    var setting = root.getAttribute("data-theme-setting");
    if (setting === "system") {
      applySetting(setting);
    }
  };
  if (prefersDark.addEventListener) {
    prefersDark.addEventListener("change", onSystemChange);
  } else if (prefersDark.addListener) {
    prefersDark.addListener(onSystemChange);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("light-toggle");
    if (toggle) {
      applySetting(root.getAttribute("data-theme-setting"));
      toggle.addEventListener("click", function () {
        var current = root.getAttribute("data-theme-setting");
        var next = SETTINGS[(SETTINGS.indexOf(current) + 1) % SETTINGS.length];
        saveSetting(next);
        applySetting(next);
      });
    }

    var toggler = document.querySelector(".navbar-toggler");
    var menu = document.getElementById("navbarNav");
    if (toggler && menu) {
      toggler.addEventListener("click", function () {
        var open = menu.classList.toggle("show");
        toggler.classList.toggle("collapsed", !open);
        toggler.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    // Table of contents: mark the section being read.
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-sidebar a"));
    if (tocLinks.length) {
      var NAVBAR_CLEARANCE = 90; // px: a heading above this line counts as reached
      var heldUntil = 0;

      var markActive = function (active) {
        tocLinks.forEach(function (link) {
          link.classList.toggle("active", link === active);
        });
      };

      var onScroll = function () {
        if (Date.now() < heldUntil) {
          return;
        }
        // Near the end of the page the line slides down to the bottom of the
        // window, so the last, short sections get their turn too.
        var page = document.documentElement;
        var remaining = page.scrollHeight - window.innerHeight - window.scrollY;
        var line = Math.max(NAVBAR_CLEARANCE, window.innerHeight - remaining);
        var active = tocLinks[0];
        tocLinks.forEach(function (link) {
          var heading = document.getElementById(link.hash.slice(1));
          if (heading && heading.getBoundingClientRect().top <= line) {
            active = link;
          }
        });
        markActive(active);
      };

      tocLinks.forEach(function (link) {
        link.addEventListener("click", function () {
          // The jump itself scrolls the page; keep the clicked entry marked through it.
          markActive(link);
          heldUntil = Date.now() + 500;
        });
      });

      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }
  });
})();
