<template>
  <div :class="[$style.appbar, doAnimate ? $style.animate : '']">
    <div :class="$style.nav"></div>
    <div :class="$style.notch">
      <div :class="$style.logo">
        <a href="/">
          <img src="assets/logo.png">
        </a>
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

$appbar-height = 40px;
$notch-height = 75px;
$notch-width = 200px;
$appbar-color = #242424;
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
    box-shadow: $appbar-glow-color 0 1px 4px 1px;
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
      left: 1px;
      padding: 20px 20px 0 25px;
      clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
      background: $notch-color;
      height: 100%;
      width: $notch-width - 2 * @left;
    }

    img {
      width: 100%;
    }
  }
}

.shown {
}
</style>
