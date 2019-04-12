<template>
  <div>
    <div :class="[$style.closeBtn,hideEvent,expandEvent]" @click="isShown = false">
      <i class="fas fa-chevron-down"></i>
    </div>
    <div :class="[$style.openBtn,showEvent]" @click="isShown = true">
      <i class="fas fa-chevron-up"></i>
    </div>
    <div
      :class="[$style.terminal, terminalStateStyle, terminalShownStyle]"
      @click="focusTerminalInput"
    >
      <div :class="$style.items">
        <REPL
          v-for="(item, i) in historyItems"
          :key="i"
          :propInput="item.input"
          :propOutput="item.output"
          :pwd="item.pwd"
        />
        <REPL
          ref="cli"
          :pwd="pwd"
          :isActive="true"
          @pwdChanged="initCommandsOnPageChange"
          @onSubmitInput="onSubmitInput"
          @onBlurInput="collapseTerminal"
        />
      </div>
    </div>
  </div>
</template>
<script>
import { navigation, terminal } from "@store/navigation";
import { CommandList } from "@js/commands";
import { CommandNotFoundError } from "@js/exceptions";
import REPL from "./REPL";

export default {
  props: {
    propCurrent: {
      type: String
    },
    isExpanded: {
      type: Boolean,
      default: false
    }
  },
  components: {
    REPL
  },
  model: {
    prop: "isExpanded",
    event: "onTerminalStateChanged"
  },
  data() {
    return {
      isShown: false,
      isHelpShown: false,
      historyItems: terminal.getHistory(),
      pwd: []
    };
  },
  computed: {
    current() {
      return this.propCurrent;
    },
    environmentVars() {
      return {
        pwd: this.pwd,
        vue: this.$refs.cli
      };
    },
    terminalStateStyle() {
      return this.isExpanded ? this.$style.expanded : this.$style.collapsed;
    },
    terminalShownStyle() {
      return this.isShown ? this.$style.shown : "";
    },
    hideEvent() {
      return this.isShown ? "" : this.$style.hideBtn;
    },
    showEvent() {
      return this.isShown ? this.$style.hideBtn : "";
    },
    expandEvent() {
      return this.isExpanded ? this.$style.moveUp : "";
    }
  },
  mounted() {
    this.pwd = navigation.getPwdFromCurrent(this.current);
  },
  watch: {
    current: function(newValue, oldValue) {
      if (!newValue) return;
      this.pwd = navigation.getPwdFromCurrent(newValue);
    }
  },
  methods: {
    handleScroll(event) {
      if (window.scrollY / window.innerHeight > 0.5) this.showTerminal();
      else this.hideTerminal();
    },
    focusTerminalInput(event) {
      if (event.target.tagName !== "A") {
        this.$refs.cli.focusInput();
        this.changeTerminalState(true);
      }
    },
    initCommandsOnPageChange() {
      this.$refs.cli.submitInput("ls");
    },
    showTerminal() {
      this.isShown = true;
    },
    hideTerminal() {
      this.isShown = false;
    },
    collapseTerminal() {
      this.changeTerminalState(false);
      this.scrollToBottom();
    },
    changeTerminalState(state) {
      if (state && !this.isExpanded && !this.isHelpShown) {
        this.$refs.cli.submitInput("help");
        this.isHelpShown = true;
      }
      this.$emit("onTerminalStateChanged", state);
    },
    animateScrollShow() {
      this.hideTerminal();
      window.addEventListener("scroll", this.handleScroll);
    },
    noAnimateScrollShow() {
      window.removeEventListener("scroll", this.handleScroll);
      this.showTerminal();
    },

    submitResult(status, output) {
      const { cli } = this.$refs;
      if (!cli) return;
      const input = cli.input;
      terminal.addToHistory(this.pwd, status, input, output);
      this.$refs.cli.clearInput();
      this.scrollToBottom();
    },
    scrollToBottom() {
      this.$nextTick(() => {
        this.$el.scrollTop = this.$el.scrollHeight;
      });
    },
    getCommandPromise(cmd, args) {
      var envs = this.environmentVars;
      return new Promise(function(resolve, reject) {
        let result = null;
        for (let i = 0; i < CommandList.length; i++) {
          if (CommandList[i].isValid(cmd)) {
            result = new CommandList[i](args, envs);
            break;
          }
        }
        if (!!result)
          result
            .execute()
            .then(resolve)
            .catch(reject);
        else reject(new CommandNotFoundError());
      });
    },
    onSubmitInput(words) {
      let cmd = words.splice(0, 1)[0];
      this.getCommandPromise(cmd, words)
        .then(result => {
          this.submitResult(0, result);
        })
        .catch(error => {
          console.error(error);
          this.submitResult(error.code, error.message);
        });
    }
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';
@require '~@styles/anims';

$cli-text = $chartreuse;
$expanded-height = 200px;
$collapsed-height = 90px;

.terminal {
  background: $black;
  width: 100%;
  z-index: 25;
  box-shadow: 1px -2px 2px 5px white;
  stick('bottom');
  font: 800 18px 'Courier New';
  color: $cli-text;
  overflow-y: auto;

  &.expanded {
    height: $expanded-height;
    moveAnimation(startDistance: (-($expanded-height)), targetDistance: 0px);
  }

  &.collapsed {
    height: $collapsed-height;
    moveAnimation(startDistance: (-($collapsed-height)), targetDistance: 0px);
  }
}

.items {
  height: 100%;
  width: 100%;
}

.blink {
  animation: blink 500ms infinite alternate;
}

.shown {
}

.terminal::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #F5F5F5;
}

.terminal::-webkit-scrollbar {
  width: 10px;
  background-color: #F5F5F5;
}

.terminal::-webkit-scrollbar-thumb {
  background-color: #000000;
  border: 2px solid #555555;
}

.closeBtn {
  position: fixed;
  right: 3px;
  z-index: 999;
  bottom: 100px;
  color: $chartreuse;

  &:hover {
    cursor: pointer;
  }

  &.hideBtn {
    display: none;
  }

  &.moveUp {
    bottom: 210px;
  }
}

.openBtn {
  position: fixed;
  right: 3px;
  z-index: 999;
  bottom: 10px;
  color: $chartreuse;

  &:hover {
    cursor: pointer;
  }

  &.hideBtn {
    display: none;
  }
}
</style>
