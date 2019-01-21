<template>
  <div :class="$style.terminal">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <a :class="$style.breadcrumbs__step" v-for="(dir, i) in pwd" :key="i">{{ dir }}</a>
      </div>
      <span :id="$style.input" ref="cliInput"></span>
      <span :id="$style.cursor" :class="$style.blink">_</span>
    </div>
  </div>
</template>
<script>
import { navigation } from "../js/store";

export default {
  data() {
    return {
      pwd: navigation.pwd
    };
  },
  computed: {},
  methods: {
    inputCliText(character) {
      let elem = this.$refs.cliInput;
      elem.innerHTML += character;
    }
  },
  mounted() {
    window.addEventListener("keypress", event => {
      let code = event.keyCode;
      this.inputCliText(String.fromCharCode(code));
    });
  }
};
</script>
<style module lang="stylus">
@import '../styles/colors.styl';
@import '../styles/mixins.styl';
@import '../styles/anims.styl';

$breadcrumb-unselected = $chartreuse;
$breadcrumb-hovered = $limeade;
$breadcrumb-arrow = $white;
$breadcrumb-root = $verdun-green;
$breadcrumb-text = $white;

.terminal {
  background: $black;
  height: 200px;
  width: 100%;
  z-index: 5;
  box-shadow: 1px -1px 2px 5px white;
  stick('bottom');
  font-family: 'Roboto Mono';
}

.breadcrumbs {
  text-align: center;
  display: inline-block;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25);
  overflow: hidden;

  &__step {
    text-decoration: none;
    outline: none;
    display: block;
    float: left;
    font-size: 12px;
    line-height: 36px;
    padding: 0 10px 0 40px;
    position: relative;
    background: $breadcrumb-unselected;
    color: $breadcrumb-text;
    transition: background 0.5s;

    &:first-child {
      padding-left: 25px;

      &::before {
        left: 14px;
      }
    }

    &:last-child {
      border-radius: 0 5px 5px 0;
      padding-right: 20px;

      &::after {
        content: none;
      }
    }

    // arrow
    &::after {
      content: '';
      position: absolute;
      top: 0;
      right: -18px;
      width: 36px;
      height: 36px;
      transform: scale(0.707) rotate(45deg);
      z-index: 1;
      border-radius: 0 5px 0 50px;
      background: $breadcrumb-unselected;
      transition: background 0.5s;
      box-shadow: 2px -2px 0 2px $breadcrumb-arrow;
    }

    &:hover {
      color: $breadcrumb-text;
      background: $breadcrumb-hovered;

      &::after {
        color: $breadcrumb-arrow;
        background: $breadcrumb-hovered;
      }
    }
  }
}

.cli {
  width: 100%;
}

.blink {
  animation: blink 500ms infinite alternate;
}
</style>
