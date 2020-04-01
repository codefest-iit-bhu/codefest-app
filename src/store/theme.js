import { KEY_THEME } from "@js/constants";

function loadThemePreference() {
  return localStorage.getItem(KEY_THEME);
}

function saveThemePreference(theme) {
  localStorage.setItem(KEY_THEME, theme);
}

export default {
  state: {
    theme: loadThemePreference() || "light"
  },
  getters: {
    currentTheme: state => {
      return state.theme;
    }
  },
  mutations: {
    TOGGLE_THEME(state) {
      state.theme = state.theme === "dark" ? "light" : "dark";
      saveThemePreference(state.theme);
    }
  },
  actions: {
    toggle_theme({ state, commit }) {
      commit("TOGGLE_THEME");
    }
  }
};
