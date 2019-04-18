import Vue from "vue";
import GAnalytics from "ganalytics";
import vueMq from "vue-mq";
import VueYoutube from "vue-youtube";
import scrollSpy, { Easing } from "vue2-scrollspy";
import firebase from "firebase";
import Toasted from "vue-toasted";
import { VueReCaptcha } from "vue-recaptcha-v3";
import { VueSpinners } from "@saeris/vue-spinners";

import App from "./App";
import router from "./router";
import filters from "./plugins/filters";
import store from "./store";

import "./styles/index.styl";

Vue.config.productionTip = false;
const render = h => h(App);

Vue.use(Toasted, {
  position: "bottom-center",
  duration: 3000,
  iconPack: "fontawesome",
  action: {
    icon: "times",
    onClick: (e, toastObject) => toastObject.goAway(0)
  },
  fitToScreen: true,
  singleton: true
});

Vue.toasted.register(
  "error_post",
  payload => {
    const msg = payload.message || "Something went wrong!";
    return `Oops... ${msg}`;
  },
  { icon: "exclamation-circle", type: "error", duration: 5000 }
);

Vue.toasted.register(
  "success",
  payload => {
    const msg = payload.message || "Success!";
    return `Yay! ${msg}`;
  },
  { icon: "check", type: "success" }
);

Vue.use(VueSpinners);

Vue.use(vueMq, {
  breakpoints: {
    __: 320,
    xs: 575,
    sm: 767,
    md: 991,
    lg: 1367,
    xl: 1920,
    xxl: Infinity
  }
});

Vue.use(scrollSpy, {
  easing: Easing.Cubic.In
});

Vue.use(VueYoutube);

Vue.use(VueReCaptcha, {
  siteKey: "6LepxJ0UAAAAAMGBO1-1PxqQ_Y3TuJGt5DHp5cHk",
  loaderOptions: {
    useRecaptchaNet: true
  }
});

Vue.use(filters);

// Mount w/ Hydration
// ~> because HTML already exists from`pwa export`
// @see https://ssr.vuejs.org/guide/hydration.html
const app = new Vue({
  router,
  store,
  render
}).$mount("#app", true);

if (process.env.NODE_ENV === "production") {
  window.ga = new GAnalytics("UA-72222745-1");

  router.afterEach(nxt => {
    ga.send("pageview", {
      dp: nxt.path
    });
  });
}

// Service Worker registration
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("./sw.js");
}

const config = {
  apiKey: "AIzaSyDgx3hMDrBTQ6ci9hKg0MMmbR36rBaH6Bo",
  authDomain: "codefest19.firebaseapp.com",
  databaseURL: "https://codefest19.firebaseio.com",
  projectId: "codefest19",
  storageBucket: "codefest19.appspot.com",
  messagingSenderId: "800543243585"
};

firebase.initializeApp(config);
