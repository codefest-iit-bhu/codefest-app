<template>
  <div
    :class="[$style.appbar, $style[$mq], { [$style.animate]: doAnimate }]"
    ref="appbar"
  >
    <div :class="$style.nav">
      <ul :class="$style.lNav">
        <slot name="left"></slot>
      </ul>
      <ul :class="$style.rNav">
        <slot name="right"></slot>
      </ul>
    </div>
    <div :class="$style.notch">
      <div :class="$style.back"></div>
      <div :class="[$style.logo, !haxplorePage ? $style.codefestLogo : ' ']">
        <slot name="notch" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    doAnimate: {
      type: Boolean,
      default: false,
    },
    haxplorePage: {
      type: Boolean,
      default: false,
    },
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
      if (["lg", "xl", "xxl"].includes(this.$mq)) this.animateScrollShow();
      else {
        this.noAnimateScrollShow();
        this.showAppbar();
      }
    },
  },
  watch: {
    $mq(to, from) {
      this.handleAnimation(to);
    },
  },
  mounted() {
    this.handleAnimation(this.$mq);
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

$appbar-height = 50px;
$notch-height = 100px;
$notch-width = 320px;
$notch-color = $mine-shaft;

.appbar {
  height: $notch-height;
  width: 100%;
  z-index: 10;
  stick('top');
  user-select: none;

  &.animate {
    moveAnimation(side: 'top', startDistance: (-($notch-height + 20)), targetDistance: 0px);
  }

  .nav {
    // background: var(--background-color);
    background: radial-gradient(circle, rgba(7,249,254,0.1), rgba(7,249,254,0.2));
    backdrop-filter: blur(10px);
    height: $appbar-height;
    // box-shadow: var(--appbar-shadow-color) 0 1px 10px 3px;
    box-shadow: rgb(7 249 254) 0 0px 0px 2px;
    font-family: 'Roboto Slab';
    $font-size: 25px;

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

    ul {
      list-style: none;
    }
  }

  .notch {
    position: relative;
    top: -($appbar-height);
    clip-path: polygon(0 0,100% 0,90% 100%,10% 100%);
    // border-radius: 0 0 20px 20px;
    margin: -2px auto;
    width: $notch-width;
    height: 70%;
    z-index: 11;
    // background: var(--appbar-shadow-color);
    // background: #60d7d2;
    background: rgb(7,249,254);
  

    .logo {
      position: absolute;
      bottom: 1px;
      left: 2px;
      padding: 0;
      clip-path: polygon(0 0,100% 0,90% 100%,10% 100%);
      // border-radius: 0 0 20px 20px;
      // background: $notch-color;
      // background: #234845;
      background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
      height: 100%;
      width: $notch-width - 2 * @left;
      box-shadow: 0 4px 30px var(--appbar-shadow-color);
    }

    .codefestLogo {
      padding: 20px 20px 0 25px;
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
      margin-top: -3%;

      // ~/.xs ^[1..-1] {
      //   margin-top: -3%;
      // }
    }
  }
  .back{
    background: rgba(0,0,0,0.85);
    height: 98%;
    width: 99%;
    margin: 1.5px;
    clip-path: polygon(0 0, 100% 0, 90% 100%, 10% 100%);
  }
}
</style>
