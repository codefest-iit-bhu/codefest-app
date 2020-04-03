<template>
  <div
    v-show="isSideNavigationShown"
    :class="[$style.wrapper, $style[$mq]]"
    @mouseover="isSideNavigationIdle = false"
    @mouseleave="isSideNavigationIdle = true"
    ref="sidebar"
  >
    <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
      <slot></slot>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    shouldShowSideNavigation: {
      type: Boolean,
      default: false,
      required: false
    },
    doHideOnIdle: {
      type: Boolean,
      default: true,
      required: false
    }
  },
  data() {
    return {
      isSideNavigationShown: true,
      sideNavigationIdleTimeout: 1000,
      lastScrollEventTime: 0,
      isSideNavigationIdle: false
    };
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
  },
  methods: {
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
    const { doHideOnIdle, shouldShowSideNavigation } = this.$props;
    this.isSideNavigationShown = shouldShowSideNavigation;
    this.isSideNavigationIdle = false;
    if (doHideOnIdle) window.addEventListener("scroll", this.handleScroll);
    else window.removeEventListener("scroll", this.handleScroll);
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  position: fixed;
  right: -140px;
  top: 0;
  width: 150px;
  padding: 15px;
  display: flex;
  flex-flow: column;
  justify-content: space-around;
  height: 100%;
  z-index: 9;

  ul {
    list-style: none;

    li {
      margin: 20px auto;
      display: block;

      a {
        padding: unset;
        font: 600 16px 'Roboto Slab';
        color: $white;
        text-decoration: none;
        cursor: pointer;

        span {
          color: $white;
          font-size: 14px;
          margin-right: 5px;
        }

        &:hover {
          background: unset;
          color: $vermilion;
        }
      }

      &.active {
        a {
          color: $vermilion;
          font-weight: bold;

          span {
            color: $white;
            animation: neon-text 1s ease-in-out infinite alternate;
          }
        }
      }
    }
  }

  &.md, &.lg {
    background: linear-gradient(to right, alpha($mine-shaft, 0.8), alpha($mine-shaft, 0.1));
  }
}
</style>
