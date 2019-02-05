<template>
  <div :class="$style.repl">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <a :class="$style.breadcrumbs__step" v-for="(dir, i) in pwd" :key="i">{{ dir }}</a>
      </div>
      <span v-if="!isActive">{{input}}</span>
      <input :id="$style.input" type="text" ref="cli" @keydown="collectInput" v-if="isActive">
    </div>
  </div>
</template>
<script>
export default {
  props: {
    pwd: {
      type: Array
    },
    input: {
      type: String,
      default: ""
    },
    output: {
      type: String,
      default: ""
    },
    isActive: {
      type: Boolean,
      default: false
    }
  }
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
$cli-text = $chartreuse;

.repl {
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
</style>
