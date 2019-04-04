<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <mq-layout mq="md+" v-show="isSideNavigationShown">
        <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
          <slot></slot>
        </ul>
      </mq-layout>

      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <img src="@assets/haxplore/logo-text.svg" :class="$style.sidebarLogo">
          <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
            <slot></slot>
          </ul>
        </Slide>
      </mq-layout>
    </div>
  </div>
</template>

<script>
import { TweenLite } from "gsap";
import { isMinimal } from "@js/utils";

import AppbarLayout from "@components/layouts/AppbarLayout";
import Slide from "@components/Menu/Slide";

export default {
  components: {
    AppbarLayout,
    Slide
  },
  props: {
    shouldShowSideNavigation: {
      type: Boolean,
      default: true,
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
      const finalRight = to ? 20 : -140;
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
      this.animateSideNav(to ? -100 : 20);
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

  .sidebar {
    margin: 0 auto;

    ul {
      list-style: none;

      li {
        margin: 20px auto;
        display: block;

        a {
          font: 500 18px 'Roboto Slab';
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
      margin: auto;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      ul {
        padding-top: 10px;
      }
    }

    ~/.md ^[1..-1], ~/.lg ^[1..-1], ~/.xl ^[1..-1] {
      position: fixed;
      right: -140px;
      top: 0;
      width: 150px;
      padding: 20px;
      display: flex;
      flex-flow: column;
      justify-content: space-around;
      height: 100%;
    }
  }
}
</style>
