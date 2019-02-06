import Vue from "vue";
import Router from "vue-router";
import { isMobile } from "../js/utils";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      name: "~",
      path: "/",
      component: () =>
        import(`@pages/${isMobile() ? "mobile" : "desktop"}/Home`)
    },
    {
      name: "~/events",
      path: "/events",
      component: () =>
        import(`@pages/${isMobile() ? "mobile" : "desktop"}/EventList`)
    },
    {
      name: "~/about",
      path: "/about",
      component: () => import("@pages/About")
    },
    {
      path: "/blog",
      component: () => import("@pages/Blog")
    },
    {
      path: "/blog/:title",
      component: () => import("@pages/Article")
    }
  ]
});
