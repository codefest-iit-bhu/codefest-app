import Vue from "vue";
import GAnalytics from "ganalytics";
import App from "./App";
import vueMq from "vue-mq";
import VueYoutube from "vue-youtube";
import router from "./router";
import "./styles/index.styl";
import scrollSpy, {
  Easing
} from "vue2-scrollspy";
import firebase from 'firebase';

Vue.config.productionTip = false;
const render = h => h(App);

Vue.use(vueMq, {
  breakpoints: {
    xs: 575,
    sm: 767,
    md: 991,
    lg: 1200,
    xl: 1920,
    xxl: Infinity
  }
});

Vue.use(scrollSpy, {
  easing: Easing.Cubic.In
});

Vue.use(VueYoutube);

// Mount w/ Hydration
// ~> because HTML already exists from`pwa export`
// @see https://ssr.vuejs.org/guide/hydration.html
let app = new Vue({
  router,
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
  apiKey: 'AIzaSyDgx3hMDrBTQ6ci9hKg0MMmbR36rBaH6Bo',
  authDomain: 'codefest19.firebaseapp.com',
  databaseURL: 'https://codefest19.firebaseio.com',
  projectId: 'codefest19',
  storageBucket: 'codefest19.appspot.com',
  messagingSenderId: '800543243585'
};

firebase.initializeApp(config);

firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    /* eslint-disable no-new */
    app = new Vue({
      router,
      render: h => h(App)
    }).$mount('#app');
  }
});