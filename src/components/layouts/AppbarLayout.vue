<template>
  <div :class="[$style.appbar, $style[$mq], {[$style.animate]: doAnimate}]" ref="appbar">
    <div :class="$style.nav">
      <ul :class="$style.lNav">
        <slot name="left"></slot>
      </ul>
      <ul :class="$style.rNav">
        <slot name="right"></slot>
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
      const { appbar } = this.$refs;
      if (appbar) appbar.classList.add(this.$style.shown);
    },
    hideAppbar() {
      const { appbar } = this.$refs;
      if (appbar) appbar.classList.remove(this.$style.shown);
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

.appbar {
  height: $notch-height;
  width: 100%;
  z-index: 10;
  stick('top');
  user-select: none;

  &.animate {
    moveAnimation(side: 'top', startDistance: (-($notch-height)), targetDistance: 0px);
  }

  .nav {
    height: $appbar-height;
    background: $appbar-color;
    box-shadow: $appbar-glow-color 0 2px 10px 3px;
    font-family: 'Roboto Slab';
    font-size: 25px;

    .rNav {
      float: right;
      padding-right: 10px;
    }

    .lNav {
      float: left;
      padding-left: 10px;
    }

    .lNav, .rNav {
      height: 100%;
      margin: 0;
      margin-bottom: 20px;
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

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
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
</style>