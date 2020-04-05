import Vue from "vue";
import Router from "vue-router";
import store from "@store";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      name: "~",
      path: "/",
      component: () => import(`@pages/Home`),
      meta: {
        title: "CodeFest '20 | IIT (BHU) Varanasi",
        metaTags: [],
        noTerminal: false,
        animateTerminal: true
      }
    },
    {
      name: "~/events",
      path: "/events",
      component: () => import(`@pages/EventList`),
      meta: {
        title: "CodeFest '20 | Events",
        metaTags: [],
        noTerminal: false,
        animateTerminal: true
      }
    },
    {
      name: "~/events/name",
      path: "/events/:name",
      component: () => import("@pages/EventDetails"),
      meta: {
        title: "CodeFest '20 | Event",
        metaTags: [],
        noTerminal: false
      }
    },
    {
      name: "~/ca",
      path: "/ca",
      component: () => import("@pages/CampusAmbassador"),
      meta: {
        title: "CodeFest '20 | Campus Ambassdor",
        metaTags: [],
        noTerminal: true
      }
    },
    {
      name: "~/team",
      path: "/team",
      component: () => import(`@pages/Team`),
      meta: {
        title: "CodeFest '20 | Team",
        metaTags: [],
        noTerminal: true,
        animateTerminal: true
      }
    },
    {
      name: "~/login",
      path: "/login",
      component: () => import(`@pages/Login`),
      meta: {
        title: "CodeFest '20 | Login",
        metaTags: [],
        noTerminal: true
      }
    },
    {
      name: "~/password/change",
      path: "/password/change",
      component: () => import(`@pages/ChangePassword`),
      meta: {
        title: "CodeFest '20 | Change Password",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/dashboard",
      path: "/dashboard",
      component: () => import(`@pages/Dashboard`),
      props: {
        isHomeView: true
      },
      meta: {
        title: "CodeFest '20 | Dashboard",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/dashboard/events",
      path: "/dashboard/events",
      component: () => import(`@pages/Dashboard`),
      props: {
        isEventsView: true
      },
      meta: {
        title: "CodeFest '20 | Event Registration",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/profile/edit",
      path: "/profile/edit",
      component: () => import(`@pages/ProfileEdit`),
      meta: {
        title: "CodeFest '20 | Profile Edit",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/haxplore",
      path: "/haxplore",
      component: () => import(`@pages/Hacksplore`),
      meta: {
        title: "CodeFest '20 | HaXplore",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/password/reset",
      path: "/password/reset",
      component: () => import(`@components/ForgotPassword`),
      meta: {
        title: "Forgot Password",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/referral",
      path: "/referral",
      component: () => import(`@pages/Referral`),
      meta: {
        title: "Referral Leaderboard",
        metaTags: [],
        noTerminal: true,
        requiresAuth: false
      }
    },
    {
      name: "~/test",
      path: "/dummy",
      component: () => import("@pages/Test")
    },
    {
      name: "404",
      path: "/*",
      component: () => import(`@pages/404`),
      meta: {
        title: "CodeFest '20 | 404",
        noTerminal: true
      }
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    else
      return {
        x: 0,
        y: 0
      };
  }
});

// Credits to: https://alligator.io/vuejs/vue-router-modify-head
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.metaTags);
  const previousNearestWithMeta = from.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if (nearestWithTitle) document.title = nearestWithTitle.meta.title;

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll("[data-vue-router-controlled]")).map(
    el => el.parentNode.removeChild(el)
  );

  // Skip rendering meta tags if there are none.
  if (!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags
    .map(tagDef => {
      const tag = document.createElement("meta");

      Object.keys(tagDef).forEach(key => {
        tag.setAttribute(key, tagDef[key]);
      });

      // We use this to track which meta tags we create, so we don't interfere with other ones.
      tag.setAttribute("data-vue-router-controlled", "");

      return tag;
    })
    // Add the meta tags to the document head.
    .forEach(tag => document.head.appendChild(tag));

  // Handle secure routes
  const { isLoggedIn } = store.getters;
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isLoggedIn) return next();

    return next({
      name: "~/login",
      query: {
        redirect: to.fullPath
      }
    });
  }
  if (isLoggedIn && to.name === "~/login")
    return next({
      name: "~/dashboard"
    });

  next();
});

export default router;
