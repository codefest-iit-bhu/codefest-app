<template>
  <div :class="$style.repl">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <router-link
          :to="breadcrumbLinks[i]"
          :class="$style.breadcrumbs__step"
          v-for="(dir, i) in pwd"
          :key="i"
        >{{ dir }}</router-link>
      </div>
      <span v-if="!isActive">{{ input }}</span>
      <input
        :id="$style.input"
        type="text"
        ref="cli"
        @keydown="collectInput"
        v-if="isActive"
        v-model="input"
      >
    </div>
    <div v-if="!!output" :class="$style.output">
      <component :is="outputHtml"></component>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import { navigation, terminal } from "../js/store";
import { CommandNotFoundError, CommandInvalidInput } from "../js/exceptions";

export default {
  props: {
    pwd: {
      type: Array
    },
    propInput: {
      type: String,
      default: ""
    },
    propOutput: {
      type: String,
      default: ""
    },
    isActive: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      output: this.propOutput,
      input: this.propInput
    };
  },
  computed: {
    outputHtml() {
      return Vue.compile(`<div>${this.output}</div>`);
    },
    breadcrumbLinks() {
      return navigation.getLinksFromPwd(this.pwd);
    }
  },
  methods: {
    evalInput(cmdLine) {
      return cmdLine.split(/\s+/);
    },
    runChangePage() {
      if (arguments.length === 0) {
        this.$router.push("/");
        return;
      }
      if (arguments.length > 1)
        throw new CommandInvalidInput(1, "Invalid arguments provided");
      let targetDir = arguments[0];
      let url;
      try {
        url = navigation.getTargetPageUrl(this.pwd, targetDir);
      } catch (error) {
        throw new CommandInvalidInput(2, "Directory not found.");
      }
      this.$router.push(url);
    },
    runListPage() {
      if (this.pwd === null) return;
      let list = navigation.listContents(this.pwd);
      let result = [];
      for (let key in list) {
        let name = key;
        let url = list[key]["/"] || list["/"];
        result.push(`<router-link to="${url}">${name}</router-link>`);
      }
      return this.outputAsColumns(result);
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
    }
  },
  watch: {
    pwd: function(newPwd, oldPwd) {
      this.$emit("pwdChanged");
    }
  },
  mounted() {}
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
$output-link = $dodger-blue;

.repl {
  margin-top: 5px;
}

.breadcrumbs {
  text-align: center;
  display: inline-block;
  overflow: hidden;
  margin-right: 10px;

  a&__step, a&__step:visited {
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

.output {
  margin-top: 5px;

  .column {
    display: grid;
    grid-auto-flow: column;
    grid-template-columns: repeat(5, 150px);
    column-gap: 20px;

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
</style>
