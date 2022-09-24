<template>
  <div :class="[$style.repl, $style[$mq]]">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <router-link
          :to="breadcrumbLinks[i]"
          :class="$style.breadcrumbs__step"
          v-for="(dir, i) in pwd"
          :key="i"
          >{{ dir }}</router-link
        >
      </div>
      <span v-if="!isActive">{{ input }}</span>
      <input
        :id="$style.input"
        type="text"
        ref="cli"
        @keydown="collectInput"
        @blur="onUnfocusInput"
        v-if="isActive"
        v-model="input"
      />
    </div>
    <div v-if="!!output" :class="$style.output">
      <component :is="outputHtml"></component>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { navigation, terminal } from "@store/navigation";
import { CommandNotFoundError, CommandInvalidInput } from "@js/exceptions";

export default {
  props: {
    pwd: {
      type: Array,
    },
    propInput: {
      type: String,
      default: "",
    },
    propOutput: {
      type: String,
      default: "",
    },
    isActive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      output: this.propOutput,
      input: this.propInput,
    };
  },
  computed: {
    outputHtml() {
      return Vue.compile(`<div>${this.output}</div>`);
    },
    breadcrumbLinks() {
      return navigation.getLinksFromPwd(this.pwd);
    },
  },
  methods: {
    evalInput(cmdLine) {
      return cmdLine.trim().split(/\s+/);
    },
    submitInput(cmdLine) {
      this.input = this.input || cmdLine;

      let words = this.evalInput(this.input);
      if (words.length > 0) {
        this.$emit("onSubmitInput", words);
      }
    },
    completeInput(cmdLine) {},
    collectInput(event) {
      if (!this.isActive) return false;
      if (event.keyCode == 13) {
        // Enter is presed.
        this.submitInput(event.target.value);
      }
    },
    focusInput() {
      if (this.isActive) this.$refs.cli.focus();
    },
    clearInput() {
      this.input = "";
    },
    onUnfocusInput(e) {
      this.$emit("onBlurInput", e);
    },
  },
  watch: {
    pwd: function(newPwd, oldPwd) {
      this.$emit("pwdChanged");
    },
  },
  mounted() {},
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

$breadcrumb-hovered = $crown-of-thorns;
$breadcrumb-unselected = $waterloo;
$breadcrumb-arrow = $white;
$breadcrumb-text = $white;
$cli-text = $white;
$output-link = $dodger-blue;

.repl {
  margin-top: 5px;

  ~/.xs, ~/.sm, ~/.md {
    $font-size: 16px;
  }

  .breadcrumbs {
    text-align: center;
    display: inline-block;
    overflow: hidden;
    margin-right: 10px;

    a^[1..-1]__step, a^[1..-1]__step:visited {
      text-decoration: none;
      outline: none;
      display: block;
      float: left;
      $font-size: 18px;
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

  .output {
    margin-top: 5px;

    .column {
      display: grid;
      grid-template-columns: repeat(4, minmax(150px, 1fr));
      grid-row-gap: 10px;
      grid-column-gap: 20px;

      ../ {
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }

    a, a:visited {
      color: $output-link;
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
}
</style>
