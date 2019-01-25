<template>
  <div :class="$style.terminal" ref="terminal" @click="$refs.cli.focus()">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <a :class="$style.breadcrumbs__step" v-for="(dir, i) in pwd" :key="i">{{ dir }}</a>
      </div>
      <input :id="$style.input" type="text" ref="cli" />
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
    handleScroll(event) {
      if (window.scrollY / window.innerHeight > 0.5) {
        this.$refs.terminal.classList.add(this.$style.shown);
      } else {
        this.$refs.terminal.classList.remove(this.$style.shown);
      }
    }
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  dismounted() {}
};
</script>
<style module lang="stylus">
@import '../styles/colors.styl';
@import '../styles/mixins.styl';
@import '../styles/anims.styl';

$breadcrumb-hovered = $deep-fir;
$breadcrumb-unselected = $limeade;
$breadcrumb-arrow = $white;
$breadcrumb-root = $verdun-green;
$breadcrumb-text = $white;
$cli-text = $chartreuse

.terminal {
  background: $black;
  height: 200px;
  width: 100%;
  z-index: 5;
  box-shadow: 1px -2px 2px 5px white;
  stick('bottom');
  font-family: 'Courier New'
  font-size: 20px;
  font-weight: 800;
  color: $cli-text
  moveAnimation(startDistance: -200px, targetDistance: 0px);
}

.breadcrumbs {
  text-align: center;
  display: inline-block;
  overflow: hidden;
  margin-right: 10px;

  &__step {
    text-decoration: none;
    outline: none;
    display: block;
    float: left;
    font-size: 18px;
    line-height: 30px;
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
      width: 30px;
      height: 30px;
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
      cursor: pointer;

      &::after {
        color: $breadcrumb-arrow;
        background: $breadcrumb-hovered;
      }
    }
  }
}

.cli {
  width: 100%;
  height: 30px;
  display: flex;
  flex-flow: row wrap;
  align-items: center;

  div {
    height: 100%;
  }

  #input {
    background: $transparent;
    border: none;
    outline: none;
    color: unset;
    font: unset;
    flex-grow: 1;
  }
}

.blink {
  animation: blink 500ms infinite alternate;
}

.shown {
}
</style>
