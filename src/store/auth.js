import { KEY_AUTH_TOKEN } from "@js/constants";
import API, { Response, STATUS } from "@js/api";

import firebase from "firebase/app";

function getTokenFromStorage() {
  return localStorage.getItem(KEY_AUTH_TOKEN);
}

function putTokenToStorage(token) {
  if (!token) localStorage.removeItem(KEY_AUTH_TOKEN);
  else localStorage.setItem(KEY_AUTH_TOKEN, token);
}

function saveCampusAmbassadorStatus(status) {
  localStorage.setItem("is_campus_ambassador", status);
}

function getCampusAmbassadorStatus() {
  if(localStorage.getItem("is_campus_ambassador")) return localStorage.getItem("is_campus_ambassador");
  return false;
}

export default {
  state: {
    token: getTokenFromStorage() || "",
    userId: -1,
    isCampusAmbassador: getCampusAmbassadorStatus(),
  },
  getters: {
    isLoggedIn: (state) => {
      return !!state.token;
    },
    authToken: (state) => state.token,
    isCampusAmbassador: (state) => state.isCampusAmbassador,
  },
  mutations: {
    AUTH_SUCCESS(state, data) {
      const { token, user_id, is_campus_ambassador } = data;
      state.token = token;
      state.userId = user_id;
      state.isCampusAmbassador = is_campus_ambassador;
      saveCampusAmbassadorStatus(is_campus_ambassador);
      putTokenToStorage(token);
    },
    AUTH_LOGOUT(state) {
      state.token = "";
      putTokenToStorage(null);
    },
    CA_STATUS_UPDATE(state, is_campus_ambassador) {
      state.isCampusAmbassador = is_campus_ambassador
      saveCampusAmbassadorStatus(is_campus_ambassador)
    }
  },
  actions: {
    login({ state, commit }, { idToken }) {
      const body = {
        id_token: idToken,
      };
      return API.post("login/", { body }).then((response) => {
        commit("AUTH_SUCCESS", response.data);
        return response;
      });
    },
    register(
      { state, commit },
      { idToken, name, referralCode, recaptchaToken }
    ) {
      const names = (name || "Anonymous").split(/\s+/);
      const body = {
        id_token: idToken,
        first_name: names[0],
        last_name: names.length > 0 ? names[1] : "",
        applied_referral_code: referralCode,
        g_recaptcha_response: recaptchaToken,
      };
      return API.post("register/", { body }).then((response) => {
        commit("AUTH_SUCCESS", response.data);
        return response;
      });
    },
    logout({ state, commit }) {
      firebase.auth().signOut();
      commit("AUTH_LOGOUT");
    },
    update_ca_status(
      {state, commit},
      {new_status}
    ) {
      commit("CA_STATUS_UPDATE", new_status)
    }
  },
};
