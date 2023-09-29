<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout :currentPage="currentPage" v-bind="this.$attrs">
      <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/" v-if="currentPage != 'home'">
          Home
          <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
        </router-link>
      </li>
      <!-- <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/haxplore" v-if="currentPage != 'haxplore'">
          HaXplore
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </router-link>
      </li> -->
      <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/codestart" v-if="currentPage != 'codestart'">
          CodeStart
          <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
        </router-link>
      </li>
      <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/events" v-if="currentPage != 'events'">
          Events
          <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
        </router-link>
      </li>
      <!-- <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/ca">
          CA
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </router-link>
      </li>-->
      <!-- <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/team">
          Team
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </router-link>
      </li>-->
      <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <router-link to="/referral"><b>Referrals</b></router-link>
      </li>
      <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)"
        v-show="showDashboardActions">
        <router-link to="/dashboard">
          <i class="fas fa-id-badge" title="Dashboard"></i>
          <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
        </router-link>
      </li>
      <!-- <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)"
        v-show="showDashboardActions">
        <router-link to="/dashboard/events">
          <i class="fas fa-user-plus" title="My Teams"></i>
        </router-link>
      </li> -->
      <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)"
        v-show="showDashboardActions">
        <a @click="authLogout">
          <i class="fas fa-power-off" title="Logout"></i>
          <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
        </a>
      </li>
      <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)"
        v-show="!showDashboardActions">
        <router-link to="/login">Login / Register</router-link>
      </li>

      <li :class="$style.link" @click="toggleTheme" slot="right">
        <a :class="$style.toggleTheme">
          <img v-if="isThemeLight" :id="$style.sun" src="assets/sun-white.svg" />
          <img v-else :id="$style.moon" src="assets/moon-white.svg" />
        </a>
      </li>

      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
      <router-link to="/haxplore" slot="notch" v-if="currentPage == 'haxplore'">
        <img src="@assets/haxplore/hax_white.svg" @click="clickNotch" />
      </router-link>
      <router-link to="/codestart" slot="notch" v-else-if="currentPage == 'codestart'">
        <img src="@assets/codestart/codestart.png" :class="$style.codestartNotch" @click="clickNotch" />
      </router-link>
      <router-link to="/" slot="notch" v-else>
        <img src="@assets/white-cf24-logo.svg" :class="$style.haxploreNotch" @click="clickNotch" />
      </router-link>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <SectionSidebar v-bind="$attrs" v-if="['md', 'lg', 'xl', 'xxl'].includes($mq)">
        <template v-for="slot in Object.keys($slots)">
          <slot :name="slot"></slot>
        </template>
      </SectionSidebar>
      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <ul :class="$style.sidebarList">
            <li :class="$style.link">
              <router-link to="/events" v-if="currentPage != 'events'">Events</router-link>
              <div :class="$style.subList">
                <slot name="events"></slot>
              </div>
            </li>
            <li :class="$style.link">
              <router-link to="/" v-if="currentPage != 'home'">
                <b>Home</b>
                <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
              </router-link>
            </li>
            <!-- <li :class="$style.link">
              <router-link to="/haxplore" v-if="currentPage != 'haxplore'">
                HaXplore
                <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
              </router-link>
            </li> -->
            <li :class="$style.link">
              <router-link to="/codestart" v-if="currentPage != 'codestart'">
                <b>CodeStart</b>
                <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
              </router-link>
            </li>
            <!-- <li :class="$style.link">
              <router-link to="/ca">CA</router-link>
            </li>-->
            <!-- <li :class="$style.link">
              <router-link to="/team">Team</router-link>
            </li>-->
            <li :class="$style.link">
              <router-link to="/referral"><b>Referrals</b></router-link>
            </li>
            <!-- <li :class="$style.link" v-show="showDashboardActions">
              <router-link to="/dashboard">
                Dashboard
                <div :class="$style.subList">
                  <slot name="dashboard"></slot>
                </div>
              </router-link>
            </li> -->
            <li :class="$style.link" v-show="!showDashboardActions">
              <router-link to="/login"><b>Login / Register</b></router-link>
            </li>
            <li :class="$style.link" v-show="showDashboardActions">
              <a @click="authLogout"><b>Logout</b></a>
            </li>
          </ul>
        </Slide>
      </mq-layout>
    </div>
  </div>
</template>

<script>
import { isMinimal } from "@js/utils";

const AppbarLayout = () => import("@components/layouts/AppbarLayout");
const SectionSidebar = () => import("@components/SectionSidebar");
const Slide = () => import("@components/Menu/Slide");

export default {
  components: {
    AppbarLayout,
    SectionSidebar,
    Slide
  },
  props: {
    currentPage: {
      type: String
    }
  },
  data() {
    return {
      isSidebarOpen: false,
    };
  },
  computed: {
    sideBarWidth() {
      if (isMinimal(this.$mq)) return window.innerWidth;
      else return 300;
    },
    showDashboardActions() {
      return this.$store.getters.isLoggedIn;
    },
    isThemeLight() {
      return this.$store.getters.currentTheme === "light";
    }
  },
  methods: {
    openSidebar() {
      this.isSidebarOpen = true;
    },
    onCloseSideBar() {
      this.isSidebarOpen = false;
    },
    clickNotch() {
      if (this.currentPage === "haxplore") {
        this.$emit("scrollTop");
      } else {
        if (this.$route.name === "~") this.$emit("scrollTop");
      }
    },
    authLogout() {
      this.$store.dispatch("logout");
      if (this.$route.meta.requiresAuth) this.$router.push({ name: "~" });
    },
    toggleTheme() {
      this.$store.dispatch("toggle_theme");
    }
  },
  mounted() {
    const { doHideOnIdle } = this.$data;
    this.isSideNavigationIdle = false;
    if (doHideOnIdle) window.addEventListener("scroll", this.handleScroll);
    else window.removeEventListener("scroll", this.handleScroll);
  }
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

.wrapper {
  li {
    display: inline-block;
  }

  .link {
    margin-top: 5px;

    .awesome {
      border-radius: 10px;
    }

    a {
      color: $waterloo;
      cursor: pointer;
      height: inherit;
      font-weight: 600;
      $font-size: 20px;
      letter-spacing: 0.8px;
      padding: 0 10px;
      text-decoration: none;
      transition: 0.5s;
      vertical-align: middle;
    }

    a span {
      margin-right: 15px;
      color: $white;
      opacity: 0;
      $font-size: 16px;
    }

    ~/.xs ^[1..-1] a, ~/.sm ^[1..-1] a, ~/.md ^[1..-1] a {
      $font-size: 16px;
    }

    a:hover {
      color: var(--text-color);
    }

    a:hover span {
      opacity: 1;
      color: transparent;
      animation: timeline-border-green 1s ease-in-out infinite alternate;
    }
  }

  #toggleSidebar {
    margin: 5px 10px;

    a {
      text-decoration: none;
      color: $waterloo;
      transition: 0.5s;
    }
  }

  .toggleTheme {
    margin: -5px;

    #sun {
      height: 1.2em;
      position: relative;
      top: 3px;
      fill: blue !important;
    }

    #moon {
      height: 1em;
      position: relative;
      top: 3px;
    }

    ~/.xs #sun, ~/.sm #sun {
      height: 1.5em;
    }

    ~/.xs #moon, ~/.sm #moon {
      height: 1.3em;
      top: 2px;
    }
  }

  .appbarLogo {
    display: inline-block;
    height: 100%;
    padding: 5px;
    margin: 0 10px;

    img {
      height: inherit;
    }

    &#haxploreLogo img {
      padding: 10px 0;
      cursor: pointer;
    }
  }

  .sidebar {
    margin: 0 auto;

    ul {
      list-style: none;

      li {
        margin: 20px auto;
        display: block;

        .subList {
          margin: 10px 0 0 10px;

          li {
            margin: 5px;
          }
        }

        a, .subList a {
          font: 500 15px 'Roboto Slab';
          text-decoration: none;
          cursor: pointer;
          padding: 10px;
          display: inline-block;
          width: 100%;

          span {
            color: $waterloo;
            $font-size: 14px;
            border-radius: 100%;
          }
        }
      }
    }

    .sidebarLogo {
      width: 250px;
      cursor: pointer;
      margin: auto;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      ul {
        padding-top: 10px;
      }
    }
  }

  .haxploreNotch {
    margin-top: 5% !important;
  }

  .codestartNotch {
    margin-top: 2% !important;
  }
}
</style>
