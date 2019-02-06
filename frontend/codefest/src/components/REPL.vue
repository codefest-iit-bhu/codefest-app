<template>
  <div :class="$style.repl">
    <div :class="$style.cli">
      <div :class="$style.breadcrumbs">
        <a :class="$style.breadcrumbs__step" v-for="(dir, i) in pwd" :key="i">{{ dir }}</a>
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
    <div v-if="!!output">
      <p :class="$style.output">{{ output }}</p>
    </div>
  </div>
</template>

<script>
import { navigation, terminal } from "../js/store";
import { CommandNotFoundError } from "../js/exceptions";

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
  methods: {
    evalInput(cmdLine) {
      return cmdLine.split(/\s+/);
    },
    submitResult(status, output) {
      terminal.addToHistory(this.pwd, status, this.input, output);
    },
    runChangePage() {
      return "cd";
    },
    runListPage() {
      let list = navigation.listContents(this.pwd);
      for (let key in list) {
      }
      list.forEach(elem => {
        let item = elem[0] || elem;
        console.log(item);
      });
    },
    getCommandPromise(cmd, args) {
      var that = this;
      return new Promise(function(resolve, reject) {
        try {
          let result;
          if (cmd === "cd") {
            result = that.runChangePage(args);
          } else if (cmd === "ls") {
            result = that.runListPage(args);
          } else {
            reject(new CommandNotFoundError());
          }
          resolve(result);
        } catch (error) {
          reject(error);
        }
      });
    },
    submitInput(cmdLine) {
      let words = this.evalInput(cmdLine);
      if (words.length > 0) {
        let cmd = words.pop(0);
        this.getCommandPromise(cmd, words)
          .then(result => {
            this.submitResult(0, result);
          })
          .catch(error => {
            this.submitResult(error.code, error.message);
          });
      }
    },
    completeInput(cmdLine) {},
    collectInput(event) {
      if (!this.isActive) return false;
      if (event.keyCode == 13) {
        // Enter is presed.
        this.submitInput(event.target.value);
        event.target.value = "";
      }
    },
    focusInput() {
      if (this.isActive) this.$refs.cli.focus();
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
  margin-top: 5px;
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

.output {
  margin-top: 5px;
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
