<template>
  <div :class="[$style.appbar, doAnimate ? $style.animate : '']">
    <div :class="$style.nav">
      <ul :class="$style.rNav">
        <li :class="$style.link">
          <a href="https://goo.gl/DrCFHB">
            <span class="fa fa-circle fa-xs" aria-hidden="true"></span>Brochure
          </a>
        </li>
        <li :class="$style.link">
          <a href="https://goo.gl/forms/RyjmY7i002oUHivu2">
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

    .rNav {
      float: right;
      font-family: Aldo the Apache;
      font-size: 25px;
      margin: 5px 20px 0 0;

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
          -webkit-animation: neon 1s ease-in-out infinite alternate;
          -moz-animation: neon 1s ease-in-out infinite alternate;
          animation: neon 1s ease-in-out infinite alternate;
        }
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

@keyframes neon {
  from {
    text-shadow: 0 0 2.5px $white, 0 0 5px $white, 0 0 7.5px $white, 0 0 10px $chartreuse, 0 0 12.5px $chartreuse, 0 0 15px $chartreuse, 0 0 25px $chartreuse;
  }

  to {
    text-shadow: 0 0 1px $white, 0 0 2px $white, 0 0 3px $white, 0 0 4px $chartreuse, 0 0 5px $chartreuse, 0 0 6px $chartreuse, 0 0 10px $chartreuse;
  }
}
</style>
