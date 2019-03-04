<template>
  <div :class="[$style.appbar, doAnimate ? $style.animate : '', $mq]">
    <div :class="$style.nav">
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
    </div>
    <div :class="$style.notch">
      <div :class="$style.logo">
        <router-link to="/">
          <img src="assets/logo.png">
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
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
      this.$el.classList.add(this.$style.shown);
    },
    hideAppbar() {
      this.$el.classList.remove(this.$style.shown);
    },
    animateScrollShow() {
      window.addEventListener("scroll", this.handleScroll);
    }
  },
  mounted() {
    if (this.$props.doAnimate) this.animateScrollShow();
  }
};
</script>
<style module lang="stylus">
@import '../styles/mixins.styl';
@import '../styles/colors.styl';
@import '../styles/anims.styl';

$appbar-height = 50px;
$notch-height = 100px;
$notch-width = 320px;
$appbar-color = $black;
$notch-color = #222222;
$appbar-glow-color = $chartreuse;

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
    font-family: 'Aldo the Apache';
    font-size: 25px;

    .rNav {
      float: right;
      margin: 5px 20px 0 0;
    }

    .lNav {
      float: left;
      margin: 5px 20px 0 0;
    }

    .link {
      display: inline-block;
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

    img {
      width: 80%;
      margin-left: 10%;
    }
  }
}

.shown {
}
</style>
