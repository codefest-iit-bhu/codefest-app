import { KEY_THEME } from "@js/constants";

function loadThemePreference() {
  return localStorage.getItem(KEY_THEME);
}

function saveThemePreference(theme) {
  localStorage.setItem(KEY_THEME, theme);
}

function getThemeAccordingToCurrentTime() {
  const today = new Date();
  const currentHour = today.getHours();
  return (currentHour <= 19 && currentHour >= 5) ? "light" : "dark";
}

export default {
  state: {
    theme: loadThemePreference() || getThemeAccordingToCurrentTime(),
    inTransition: false
  },
  getters: {
    currentTheme: state => {
      return state.theme;
    },
    inTransition: state => {
      return state.inTransition;
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
      state.inTransition = true;
      setTimeout(() => {
        state.inTransition = false;
      }, 400);
    }
  }
};
