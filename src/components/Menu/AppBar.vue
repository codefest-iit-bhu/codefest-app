<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :class="$style.link" slot="left" v-if="['lg', 'xl'].includes(this.$mq)">
        <router-link to="/events">
          Events
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </router-link>
      </li>
      <li :class="$style.link" slot="right" v-if="['lg', 'xl'].includes(this.$mq)">
        <a href="https://goo.gl/DrCFHB" target="_blank">
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>Brochure
        </a>
      </li>
      <li :class="$style.link" slot="right" v-if="['lg', 'xl'].includes(this.$mq)">
        <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
          Sponsor Us
        </a>
      </li>
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <mq-layout mq="md+" v-show="isSideNavigationShown">
        <ul @mouseover="isSideNavigationIdle = false" @mouseleave="isSideNavigationIdle = true">
          <slot></slot>
        </ul>
      </mq-layout>

      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <ul>
            <li :class="$style.link">
              <router-link to="/events">Events</router-link>
              <div :class="$style.eventList">
                <slot></slot>
              </div>
            </li>

            <li :class="$style.link">
              <a href="https://goo.gl/DrCFHB" target="_blank">Brochure</a>
            </li>
            <li :class="$style.link">
              <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">Sponsor Us</a>
            </li>
          </ul>
        </Slide>
      </mq-layout>
    </div>
  </div>
</template>

<script>
import { isMinimal } from "@js/utils";

import AppbarLayout from "@components/layouts/AppbarLayout";
import Slide from "@components/Menu/Slide";

export default {
  components: {
    AppbarLayout,
    Slide
  },
  props: {},
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
        if (this.isSideNavigationIdle) return;
        const now = new Date().getTime();
        if (now - this.lastScrollEventTime >= sideNavigationIdleTimeout) {
          this.isSideNavigationIdle = true;
        }
      }, sideNavigationIdleTimeout);
    }
  },
  mounted() {
    const { doHideOnIdle } = this.$data;
    this.isSideNavigationShown = true;
    this.isSideNavigationIdle = false;
    if (doHideOnIdle) window.addEventListener("scroll", this.handleScroll);
    else window.removeEventListener("scroll", this.handleScroll);
  },
  watch: {
    isSideNavigationIdle: function(to, from) {
      if (to === from) return;
      this.animateSideNav(to ? -130 : 0);
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  li {
    display: inline-block;
  }

  .link {
    height: 100%;

    .awesome {
      border-radius: 10px;
    }

    a {
      height: inherit;
      color: $white;
      padding: 0 15px;
      text-decoration: none;
      transition: 0.5s;
      vertical-align: middle;
    }

    a span {
      margin-right: 15px;
      color: $white;
      opacity: 0;
      font-size: 16px;
    }

    a:hover {
      color: $chartreuse;
    }

    a:hover span {
      opacity: 1;
      color: transparent;
      animation: timeline-border 1s ease-in-out infinite alternate;
    }
  }

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

        .eventList {
          margin: 10px 0 0 10px;

          li {
            margin: 5px;
          }
        }

        a, .eventList a {
          font: 500 14px 'Roboto Slab';
          color: $white;
          text-decoration: none;
          cursor: pointer;
          padding-left: 10px;

          span {
            color: $white;
            font-size: 14px;
            border-radius: 100%;
          }

          &:hover {
            color: $chartreuse;
          }
        }

        &.active, .eventList li.active {
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

    ~/.md ^[1..-1], ~/.lg ^[1..-1], ~/.xl ^[1..-1] {
      position: fixed;
      right: -130px;
      top: 0;
      width: 150px;
      padding: 15px;
      display: flex;
      flex-flow: column;
      justify-content: space-around;
      height: 100%;
      z-index: 9;

      li {
        span {
          position: absolute;
          left: 0;
          margin: 5px auto;
        }
      }
    }

    ~/.md ^[1..-1], ~/.lg ^[1..-1] {
      background: linear-gradient(to right, alpha($mine-shaft, 0.8), alpha($mine-shaft, 0.1));
    }
  }
}
</style>
