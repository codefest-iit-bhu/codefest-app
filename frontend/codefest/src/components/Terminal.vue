<template>
  <div :class="$style.terminal" @click="focusTerminalInput">
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
      />
    </div>
  </div>
</template>
<script>
import { navigation, terminal } from "../js/store";
import REPL from "./REPL";
import { CommandList } from "../js/commands.js";
import { CommandNotFoundError } from "../js/exceptions";

export default {
  props: ["propCurrent"],
  components: {
    REPL
  },
  data() {
    return {
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
    }
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
    focusTerminalInput() {
      this.$refs.cli.focusInput();
    },
    initCommandsOnPageChange() {
      this.$refs.cli.submitInput("ls");
    },
    showTerminal() {
      this.$el.classList.add(this.$style.shown);
      this.$el.scrollIntoView();
    },
    hideTerminal() {
      this.$el.classList.remove(this.$style.shown);
    },
    animateScrollShow() {
      window.addEventListener("scroll", this.handleScroll);
    },
    noAnimateScrollShow() {
      window.removeEventListener("scroll", this.handleScroll);
      this.showTerminal();
    },

    submitResult(status, output) {
      terminal.addToHistory(this.pwd, status, this.input, output);
      this.$refs.cli.clearInput();
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
  },
  mounted() {},
  dismounted() {}
};
</script>
<style module lang="stylus">
@import '../styles/colors.styl';
@import '../styles/mixins.styl';
@import '../styles/anims.styl';

$cli-text = $chartreuse;

.terminal {
  background: $black;
  height: 200px;
  width: 100%;
  z-index: 5;
  box-shadow: 1px -2px 2px 5px white;
  stick('bottom');
  font-family: 'Courier New';
  font-size: 20px;
  font-weight: 800;
  color: $cli-text;
  overflow-y: auto;
  moveAnimation(startDistance: -200px, targetDistance: 0px);
}

.items {
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
</style>
