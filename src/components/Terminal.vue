<template>
  <div
    :class="[$style.terminal, terminalStateStyle, terminalShownStyle]"
    ref="terminal"
  >
    <button :class="$style.togglebtn" @click="toggleShowTerminal">
      <div>
        <span class="absolute-center">
          <i class="fas fa-chevron-down" :style="chevronRotateStyle"></i>
        </span>
      </div>
    </button>
    <div :class="$style.items" @click="focusTerminalInput" ref="history">
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
        @onBlurInput="blurTerminalInput"
      />
    </div>
  </div>
</template>

<script>
import { navigation, terminal } from "@store/navigation";
import { CommandList } from "@js/commands";
import { CommandNotFoundError } from "@js/exceptions";

const REPL = () => import("./REPL");

export default {
  props: {
    propCurrent: {
      type: String,
    },
    isExpanded: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    REPL,
  },
  model: {
    prop: "isExpanded",
    event: "onTerminalExpand",
  },
  data() {
    return {
      shouldShow: false,
      isShown: false,
      isHelpShown: false,
      angle: 0,
      historyItems: terminal.getHistory(),
      pwd: [],
    };
  },
  computed: {
    current() {
      return this.propCurrent;
    },
    environmentVars() {
      return {
        pwd: this.pwd,
        vue: this.$refs.cli,
      };
    },
    terminalStateStyle() {
      return this.isExpanded ? this.$style.expanded : this.$style.collapsed;
    },
    terminalShownStyle() {
      return this.isShown ? this.$style.shown : "";
    },
    chevronRotateStyle() {
      return { transform: `rotate(${this.angle}deg)` };
    },
  },
  mounted() {
    this.pwd = navigation.getPwdFromCurrent(this.current);
    this.$nextTick(() => this.$emit("init"));
  },
  watch: {
    current: function(newValue, oldValue) {
      if (!newValue) return;
      this.pwd = navigation.getPwdFromCurrent(newValue);
    },
  },
  methods: {
    handleScroll(event) {
      if (window.scrollY / window.innerHeight > 0.5) this.showTerminal();
      else this.hideTerminal();
    },
    focusTerminalInput(event) {
      if (event.target.tagName !== "A") {
        this.$refs.cli.focusInput();
        this.now = new Date();
        if (!this.isExpanded && !this.isHelpShown) {
          this.$refs.cli.submitInput("help");
          this.isHelpShown = true;
        }
        this.$emit("onTerminalExpand", true);
      }
    },
    initCommandsOnPageChange() {
      this.$refs.cli.submitInput("ls");
    },
    showTerminal() {
      if (this.shouldShow) this.isShown = true;
    },
    hideTerminal() {
      this.isShown = false;
    },
    collapseTerminal() {
      this.scrollToBottom();
      this.$emit("onTerminalExpand", false);
    },
    changeTerminalState(state) {
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
    toggleShowTerminal() {
      this.shouldShow = !this.shouldShow;
      if (this.shouldShow) {
        TweenLite.to(this.$data, 0.35, { angle: 0 });
        this.showTerminal();
        this.changeTerminalState(true);
      } else if (!this.isShown) {
        this.shouldShow = true;
        this.showTerminal();
        this.changeTerminalState(true);
      } else {
        TweenLite.to(this.$data, 0.35, { angle: 180 });
        this.hideTerminal();
        this.changeTerminalState(false);
      }
    },
    blurTerminalInput(e) {
      setTimeout(() => {
        if (new Date() - this.now > 300) this.collapseTerminal();
      }, 300);
    },

    submitResult(status, output) {
      const { cli } = this.$refs;
      if (!cli) return;
      const input = cli.input;
      if(output !== null)terminal.addToHistory(this.pwd, status, input, output);
      this.$refs.cli.clearInput();
      this.scrollToBottom();
    },
    scrollToBottom() {
      const { history } = this.$refs;
      this.$nextTick(() => {
        if (!!history) history.scrollTop = history.scrollHeight;
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
      let cmd = words.splice(0, 1)[0].trim();
      this.getCommandPromise(cmd, words)
        .then((result) => {
          this.submitResult(0, result);
        })
        .catch((error) => {
          console.error(error);
          this.submitResult(error.code, error.message);
        });
    },
  },
};
</script>
<style module lang="stylus">
@require '~@styles/anims';

$cli-text = $white;
$expanded-height = 200px;
$collapsed-height = 90px;

.togglebtn {
  position: absolute;
  height: 30px;
  width: 30px;
  clip-path: polygon(20% 0, 80% 0, 100% 100%, 0 100%);
  background: $waterloo;
  color: $waterloo;
  right: 5px;
  top: -30px;
  z-index: 26;
  cursor: pointer;
  padding: 0.5px;

  div {
    width: 100%;
    height: 100%;
    clip-path: polygon(20% 0, 80% 0, 100% 100%, 0 100%);
    background: $cod-gray;
  }
}

.terminal {
  background: $mine-shaft;
  width: 100%;
  z-index: 25;
  box-shadow: rgb(7 249 250) 0 0px 10px 0px;
  stick('bottom');
  font: 400 18px 'Roboto Slab';
  color: $cli-text;

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
  overflow-y: auto;

  &::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    background-color: #F5F5F5;
  }

  &::-webkit-scrollbar {
    width: 10px;
    background-color: #F5F5F5;
  }

  &::-webkit-scrollbar-thumb {
    background-color: #000000;
    border: 2px solid #555555;
  }
}

.blink {
  animation: blink 500ms infinite alternate;
}

.shown {
}
</style>
