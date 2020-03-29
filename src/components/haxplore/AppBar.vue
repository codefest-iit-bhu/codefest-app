<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
      <li :class="$style.appbarLogo" slot="left" v-if="shouldShowCollegeLogo">
        <img src="assets/logo-dcse.png">
      </li>
      <li :class="$style.appbarLogo" slot="right" v-if="shouldShowCollegeLogo">
        <img src="assets/logo-iitbhu.png">
      </li>
      <li
        :class="$style.appbarLogo"
        :id="$style.haxploreLogo"
        slot="left"
        v-if="shouldShowEventLogo"
        @click="$emit('scrollTop')"
      >
        <img src="assets/haxplore/logo-text.svg">
      </li>
      <n-link to="/" slot="notch" v-if="!isMinimal">
        <img src="assets/white-cf20-logo.svg">
      </n-link>
      <n-link to="/haxplore" slot="notch" v-else>
        <img src="assets/haxplore/logo-text.svg" @click="$emit('scrollTop')">
      </n-link>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <SectionSidebar v-bind="$attrs" v-if="['md', 'lg', 'xl', 'xxl'].includes($mq)">
        <slot></slot>
      </SectionSidebar>
      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <n-link to="/">
            <img src="assets/white-cf20-logo.svg" :class="$style.sidebarLogo">
          </n-link>
          <!-- <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
            <slot></slot>
          </ul>-->
          <ul :class="$style.sidebarList">
            <li :class="$style.link">
              <n-link to="/events">Events</n-link>
              <div :class="$style.subList">
                <slot name="events"></slot>
              </div>
            </li>
            <li :class="$style.link">
              <n-link to="/haxplore">
                HaXplore
                <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
              </n-link>
            </li>
            <!-- <li :class="$style.link">
              <n-link to="/ca">CA</n-link>
            </li> -->
            <!-- <li :class="$style.link">
              <n-link to="/team">Team</n-link>
            </li> -->
            <!-- <li :class="$style.link">
              <n-link to="/referral">Referrals</n-link>
            </li> -->
            <li :class="$style.link" v-show="showDashboardActions">
              <n-link to="/dashboard">
                Dashboard
                <div :class="$style.subList">
                  <slot name="dashboard"></slot>
                </div>
              </n-link>
            </li>
            <li :class="$style.link" v-show="!showDashboardActions">
              <n-link to="/login">Login / Register</n-link>
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
    Slide
  },
  props: {
    shouldShowHaxploreLogo: {
      type: Boolean,
      default: false,
      required: false
    }
  },
  data() {
    return {
      isSidebarOpen: false
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
    }
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
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  #toggleSidebar {
    margin: 5px 10px;

    a {
      text-decoration: none;
      color: $white;
      transition: 0.5s;
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
            color: $white;
            $font-size: 14px;
            margin-right: 5px;
          }

          &:hover {
            color: $chartreuse;
          }
        }

        &.active {
          a {
            color: $chartreuse;
            font-weight: bold;

            span {
              color: $white;
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
