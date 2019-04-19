<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
      <li :class="$style.appbarLogo" slot="left" v-if="shouldShowCollegeLogo">
        <img src="@assets/logo-dcse.png">
      </li>
      <li :class="$style.appbarLogo" slot="right" v-if="shouldShowCollegeLogo">
        <img src="@assets/logo-iitbhu.png">
      </li>
      <li
        :class="$style.appbarLogo"
        :id="$style.haxploreLogo"
        slot="left"
        v-if="shouldShowEventLogo"
        @click="$emit('scrollTop')"
      >
        <img src="@assets/haxplore/logo-text.svg">
      </li>
      <router-link to="/" slot="notch" v-if="!isMinimal">
        <img src="assets/cf19-white-logo.svg">
      </router-link>
      <router-link to="/haxplore" slot="notch" v-else>
        <img src="assets/haxplore/logo-text.svg" @click="$emit('scrollTop')">
      </router-link>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <mq-layout mq="md+" v-show="isSideNavigationShown"></mq-layout>

      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <img
            src="@assets/haxplore/logo-text.svg"
            :class="$style.sidebarLogo"
            @click="$emit('scrollTop')"
          >
          <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
            <slot></slot>
          </ul>
        </Slide>
      </mq-layout>
    </div>
  </div>
</template>

<script>
import { isMinimal } from "@js/utils";

import AppbarLayout from "@components/layouts/AppbarLayout";
import SectionSidebar from "@components/SectionSidebar";
import Slide from "@components/Menu/Slide";

export default {
  components: {
    AppbarLayout,
    SectionSidebar,
    Slide
  },
  props: {
    shouldShowSideNavigation: {
      type: Boolean,
      default: true,
      required: false
    },
    shouldShowHaxploreLogo: {
      type: Boolean,
      default: false,
      required: false
    }
  },
  data() {
    return {
      isSidebarOpen: false,
      isSideNavigationShown: true,
      sideNavigationIdleTimeout: 1000,
      doHideOnIdle: true,
      lastScrollEventTime: 0,
      isSideNavigationIdle: false
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
    }
  },
  methods: {
    openSidebar() {
      this.isSidebarOpen = true;
    },
    onCloseSideBar() {
      this.isSidebarOpen = false;
    },
    animateSideNav(val) {
      const { sidebar } = this.$refs;

      TweenLite.to(sidebar, 0.8, {
        right: val
      });
    },
    handleScroll(event) {
      const { sideNavigationIdleTimeout } = this.$data;
      this.lastScrollEventTime = new Date().getTime();
      this.isSideNavigationIdle = false;
      setTimeout(() => {
        if (this.isSideNavigationIdle) return;
        const now = new Date().getTime();
        if (now - this.lastScrollEventTime >= sideNavigationIdleTimeout) {
          this.isSideNavigationIdle = true;
        }
      }, sideNavigationIdleTimeout);
    }
  },
  mounted() {
    const { doHideOnIdle, shouldShowSideNavigation } = this.$data;
    this.isSideNavigationShown = shouldShowSideNavigation;
    this.isSideNavigationIdle = false;
    if (doHideOnIdle) window.addEventListener("scroll", this.handleScroll);
    else window.removeEventListener("scroll", this.handleScroll);
  },
  watch: {
    shouldShowSideNavigation: function(to, from) {
      if (to === from) return;
      const { sidebar } = this.$refs;
      const finalRight = to ? 0 : -140;
      const onStart = () => {
        if (to) this.isSideNavigationShown = true;
      };
      const onComplete = () => {
        if (!to) this.isSideNavigationShown = false;
      };
      TweenLite.to(sidebar, 0.8, {
        right: finalRight,
        onStart,
        onComplete
      });
    },
    isSideNavigationIdle: function(to, from) {
      if (to === from) return;
      if (to && !this.shouldShowSideNavigation) return;
      this.animateSideNav(to ? -120 : 0);
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
            font-size: 14px;
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
}
</style>
