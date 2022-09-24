<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>

      <li :class="$style.link" @click="toggleTheme" slot="right">
        <a :class="$style.toggleTheme">
          <img v-if="isThemeLight" :id="$style.sun" src="assets/sun-white.svg" />
          <img v-else :id="$style.moon" src="assets/moon-white.svg" />
        </a>
      </li>

      <li :class="$style.appbarLogo" slot="left" v-if="shouldShowCollegeLogo">
        <img src="@assets/logo-dcse.png" />
      </li>
      <li
        :class="$style.appbarLogo"
        :id="$style.haxploreLogo"
        slot="left"
        v-if="shouldShowEventLogo"
        @click="$emit('scrollTop')"
      >
        <img src="@assets/haxplore/logo-text.svg" />
      </li>
      <router-link to="/" slot="notch" v-if="!isMinimal">
        <img src="@assets/white-cf20-logo.svg" />
      </router-link>
      <router-link to="/haxplore" slot="notch" v-else>
        <img src="@assets/haxplore/logo-text.svg" @click="$emit('scrollTop')" />
      </router-link>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <SectionSidebar v-bind="$attrs" v-if="['md', 'lg', 'xl', 'xxl'].includes($mq)">
        <slot></slot>
      </SectionSidebar>
      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <router-link to="/">
            <img src="@assets/white-cf20-logo.svg" :class="$style.sidebarLogo" />
          </router-link>
          <!-- <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
            <slot></slot>
          </ul>-->
          <ul :class="$style.sidebarList">
            <li :class="$style.link">
              <router-link to="/events">Events</router-link>
              <div :class="$style.subList">
                <slot name="events"></slot>
              </div>
            </li>
            <li :class="$style.link">
              <router-link to="/haxplore">
                HaXplore
                <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
              </router-link>
            </li>
            <!-- <li :class="$style.link">
              <router-link to="/ca">CA</router-link>
            </li>-->
            <!-- <li :class="$style.link">
              <router-link to="/team">Team</router-link>
            </li>-->
            <!-- <li :class="$style.link">
              <router-link to="/referral">Referrals</router-link>
            </li>-->
            <li :class="$style.link" v-show="showDashboardActions">
              <router-link to="/dashboard">
                Dashboard
                <div :class="$style.subList">
                  <slot name="dashboard"></slot>
                </div>
              </router-link>
            </li>
            <li :class="$style.link" v-show="!showDashboardActions">
              <router-link to="/login">Login / Register</router-link>
            </li>
            <li :class="$style.link" v-show="showDashboardActions">
              <a @click="authLogout">Logout</a>
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
    Slide,
  },
  props: {
    shouldShowHaxploreLogo: {
      type: Boolean,
      default: false,
      required: false,
    },
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
    isMinimal() {
      return isMinimal(this.$mq);
    },
    shouldShowCollegeLogo() {
      return !this.isMinimal && !this.shouldShowHaxploreLogo;
    },
    shouldShowEventLogo() {
      return !this.isMinimal && this.shouldShowHaxploreLogo;
    },
    showDashboardActions() {
      return this.$store.getters.isLoggedIn;
    },
    isThemeLight() {
      return this.$store.getters.currentTheme === "light";
    },
  },
  methods: {
    openSidebar() {
      this.isSidebarOpen = true;
    },
    onCloseSideBar() {
      this.isSidebarOpen = false;
    },
    authLogout() {
      this.$store.dispatch("logout");
      if (this.$route.meta.requiresAuth) this.$router.push({ name: "~" });
    },
    toggleTheme() {
      this.$store.dispatch("toggle_theme");
    },
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

.wrapper {
  .link {
    margin-top: 5px;

    a {
      color: $waterloo;
      font-weight: 600;
      $font-size: 20px;
      padding: 0 10px;
      transition: 0.5s;
      vertical-align: middle;
    }

    a:hover {
      color: var(--text-color);
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

        a {
          font: 500 20px 'Roboto Slab';
          color: $white;
          text-decoration: none;
          cursor: pointer;

          span {
            color: $waterloo;
            $font-size: 14px;
            margin-right: 5px;
          }

          &:hover {
            color: $waterloo;
          }
        }

        &.active {
          a {
            color: $waterloo;
            font-weight: bold;

            span {
              color: $waterloo;
              animation: neon-text 1s ease-in-out infinite alternate;
            }
          }
        }
      }
    }

    .sidebarLogo {
      width: 200px;
      cursor: pointer;
      margin: auto;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      ul {
        padding-top: 10px;
      }
    }
  }
}
</style>
