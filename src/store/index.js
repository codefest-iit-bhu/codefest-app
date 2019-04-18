import Vue from "vue";
import Vuex from "vuex";

import auth from "./auth";
import dashboard from "./dashboard";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    dashboard
  }
});
