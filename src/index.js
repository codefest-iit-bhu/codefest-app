import Vue from "vue";
import GAnalytics from "ganalytics";
import vueMq from "vue-mq";
import VueYoutube from "vue-youtube";
import scrollSpy, { Easing } from "vue2-scrollspy";
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/analytics";
import Toasted from "vue-toasted";
import { VueReCaptcha } from "vue-recaptcha-v3";
import { VueSpinners } from "@saeris/vue-spinners";

import App from "./App";
import router from "./router";
import filters from "./plugins/filters";
import store from "./store";
import wb from "./registerServiceWorker";

import "./styles/index.styl";

Vue.config.productionTip = false;
const render = (h) => h(App);

Vue.use(Toasted, {
  position: "bottom-center",
  duration: 3000,
  iconPack: "fontawesome",
  action: {
    icon: "times",
    onClick: (e, toastObject) => toastObject.goAway(0),
  },
  fitToScreen: true,
  singleton: true,
});

Vue.toasted.register(
  "error_post",
  (payload) => {
    const msg = payload.message || "Something went wrong!";
    return `Oops... ${msg}`;
  },
  { icon: "exclamation-circle", type: "error", duration: 5000 }
);

Vue.toasted.register(
  "success",
  (payload) => {
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
    xxl: Infinity,
  },
});

Vue.use(scrollSpy, {
  easing: Easing.Cubic.In,
});

Vue.use(VueYoutube);

Vue.use(VueReCaptcha, {
  siteKey: "6LepxJ0UAAAAAMGBO1-1PxqQ_Y3TuJGt5DHp5cHk",
  loaderOptions: {
    useRecaptchaNet: true,
  },
});

Vue.use(filters);

if (process.env.NODE_ENV === "production") {
  window.ga = new GAnalytics("UA-72222745-1");

  router.afterEach((nxt) => {
    ga.send("pageview", {
      dp: nxt.path,
    });
  });
}

// Service Worker registration
Vue.prototype.$workbox = wb;

const firebaseConfig = {
  apiKey: "AIzaSyBfkhzmR8nf1vwTLj9upIVo3QoOTDte6zU",
  authDomain: "codefest-iit-bhu.firebaseapp.com",
  projectId: "codefest-iit-bhu",
  storageBucket: "codefest-iit-bhu.appspot.com",
  messagingSenderId: "934000349180",
  appId: "1:934000349180:web:abd404ec2aa2ee8b5f2c79",
  measurementId: "G-CMRT89PN1N"
};

firebase.initializeApp(firebaseConfig);

// Mount w/ Hydration
// ~> because HTML already exists from`pwa export`
// @see https://ssr.vuejs.org/guide/hydration.html
const app = new Vue({
  router,
  store,
  render,
}).$mount("#app", true);
