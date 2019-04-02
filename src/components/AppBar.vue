<template>
  <div :class="$style.root">
    <div :class="[$style.appbar, doAnimate ? $style.animate : '']" ref="appbar">
      <div :class="$style.nav">
        <mq-layout mq="lg+">
          <!-- Show appbar navigations only on lg+ devices. -->
          <ul :class="$style.lNav">
            <li :class="$style.link">
              <router-link to="/events">
                Events
                <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
              </router-link>
            </li>
          </ul>
          <ul :class="$style.rNav">
            <li :class="$style.link">
              <a href="https://goo.gl/DrCFHB" target="_blank">
                <span class="fa fa-circle fa-xs" aria-hidden="true"></span>Brochure
              </a>
            </li>
            <li :class="$style.link">
              <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">
                <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
                Sponsor Us
              </a>
            </li>
          </ul>
        </mq-layout>
        <mq-layout :mq="['xs', 'sm', 'md']">
          <ul :class="$style.lNav">
            <li :id="$style.toggleSidebar">
              <a href="#" class="bm-toggle" @click="openSidebar">
                <i class="fa fa-bars"></i>
              </a>
            </li>
          </ul>
        </mq-layout>
      </div>
      <div :class="[$style.notch, $style[$mq]]">
        <div :class="$style.logo">
          <router-link to="/">
            <img src="assets/logo.png">
          </router-link>
        </div>
      </div>
    </div>
    <mq-layout :mq="['xs', 'sm', 'md']">
      <!-- Show sidebar only for smaller devices. -->
      <div :class="$style.sidebar" ref="sidebar">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <li :class="$style.link">
            <router-link to="/events">Events</router-link>
          </li>

          <li :class="$style.link">
            <a href="https://goo.gl/DrCFHB" target="_blank">Brochure</a>
          </li>
          <li :class="$style.link">
            <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">Sponsor Us</a>
          </li>
        </Slide>
      </div>
    </mq-layout>
  </div>
</template>
<script>
import Slide from "./Menu/Slide";

export default {
  components: {
    Slide
  },
  data() {
    return {
      isSidebarOpen: false
    };
  },
  computed: {
    sideBarWidth() {
      if (this.$mq === "xs" || this.$mq === "sm") return window.innerWidth;
      else return 300;
    }
  },
  props: {
    doAnimate: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleScroll(event) {
      if (window.scrollY / window.innerHeight > 0.5) this.showAppbar();
      else this.hideAppbar();
    },
    showAppbar() {
      let el = this.$refs.appbar;
      if (el) el.classList.add(this.$style.shown);
    },
    hideAppbar() {
      let el = this.$refs.appbar;
      if (el) el.classList.remove(this.$style.shown);
    },
    animateScrollShow() {
      window.addEventListener("scroll", this.handleScroll);
    },
    noAnimateScrollShow() {
      window.removeEventListener("scroll", this.handleScroll);
    },
    handleAnimation(mq) {
      if (!this.$props.doAnimate) return;
      if (mq === "lg" || mq === "xl") this.animateScrollShow();
      else {
        this.noAnimateScrollShow();
        this.showAppbar();
      }
    },
    openSidebar() {
      this.isSidebarOpen = true;
    },
    onCloseSideBar() {
      this.isSidebarOpen = false;
    }
  },
  watch: {
    $mq(to, from) {
      this.handleAnimation(to);
    }
  },
  mounted() {
    this.handleAnimation(this.$mq);
  }
};
</script>
<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';
@require '~@styles/anims';

$appbar-height = 50px;
$notch-height = 100px;
$notch-width = 320px;
$appbar-color = $black;
$notch-color = $mine-shaft;
$appbar-glow-color = $chartreuse;
$sidebar-width = 250px;

.root {
}

.appbar {
  height: $notch-height;
  width: 100%;
  z-index: 10;
  stick('top');

  &.animate {
    moveAnimation(side: 'top', startDistance: (-($notch-height)), targetDistance: 0px);
  }

  .nav {
    height: $appbar-height;
    background: $appbar-color;
    box-shadow: $appbar-glow-color 0 2px 10px 3px;
    font-family: 'Roboto Slab';
    font-weight: 700;
    font-size: 25px;

    .rNav {
      float: right;
      margin: 5px 20px 0 0;
    }

    .lNav {
      float: left;
      margin: 5px 20px 0 0;
    }

    li {
      display: inline-block;
    }

    .link {
      padding-top: 10px;

      a {
        color: $white;
        padding: 10px 10px;
        margin-left: 5px;
        text-decoration: none;
        transition: 0.5s;
      }

      a span {
        margin-right: 15px;
        color: $white;
        opacity: 0;
        font-size: 16px;
        margin-top: 0;
      }

      a:hover {
        color: $chartreuse;
      }

      a:hover span {
        opacity: 1;
        color: $white;
        animation: neon-text 1s ease-in-out infinite alternate;
      }
    }

    #toggleSidebar {
      margin: 5px 10px;

      a {
        text-decoration: none;
        color: $white;
      }
    }
  }

  .notch {
    position: relative;
    top: -($appbar-height);
    clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
    margin-left: auto;
    margin-right: auto;
    width: $notch-width;
    height: 100%;
    z-index: 11;
    background: $appbar-glow-color;

    .logo {
      position: absolute;
      bottom: 1px;
      left: 2px;
      padding: 20px 20px 0 25px;
      clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
      background: $notch-color;
      height: 100%;
      width: $notch-width - 2 * @left;
    }

    &.sm, &.xs {
      height: 80%;
      width: 0.75 * $notch-width;

      .logo {
        left: 2px;
        width: 0.75 * $notch-width - 2 * @left;
      }
    }

    img {
      width: 80%;
      margin-left: 10%;
    }
  }
}

.shown {
}

.sidebar {
  margin: 5px;

  .link {
    font-family: 'Roboto Slab';
    font-size: 14px;

    a {
      color: $white;
      padding: 10px 10px;
      margin-left: 5px;
      text-decoration: none;
      transition: 0.5s;
    }

    a:hover {
      color: $chartreuse;
    }
  }

  .link:hover {
    background: rgb(63, 63, 65);
  }
}
</style>
