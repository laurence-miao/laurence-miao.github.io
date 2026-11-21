// Color theme (system / light / dark) and the mobile menu.
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
  });
})();
