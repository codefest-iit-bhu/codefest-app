import { KEY_AUTH_TOKEN } from "@js/constants";
import API, { Response } from "@js/api";

function getTokenFromStorage() {
  return localStorage.getItem(KEY_AUTH_TOKEN);
}

function putTokenToStorage() {}

export default {
  state: {
    token: getTokenFromStorage() || "",
    user: {},
    authResponse: null
  },
  mutations: {
    AUTH_REQUEST() {
      state.authResponse = Response.loading();
    },
    AUTH_SUCCESS(response) {
      state.authResponse = response;
      const { data } = response;
      state.token = data.token;
    },
    AUTH_ERROR(response) {
      state.authResponse = response;
    },
    AUTH_LOGOUT() {
      state.token = "";
      state.authResponse = Response.success(null);
    }
  },
  actions: {
    login({ state, commit, rootState }, data) {
      API.fetch("events/", state.token)
        .then(console.log)
        .catch(console.log);
    }
  }
};
