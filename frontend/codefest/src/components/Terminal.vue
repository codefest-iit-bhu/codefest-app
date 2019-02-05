<template>
  <div :class="$style.terminal" ref="terminal" @click="$refs.cli.focus()">
    <div :class="$style.items">
      <REPL
        v-for="(item, i) in historyItems"
        :key="i"
        :input="item.input"
        :output="item.output"
        :pwd="item.pwd"
      />
      <REPL :pwd="pwd" :isActive="true" />
    </div>
  </div>
</template>
<script>
import { navigation } from "../js/store";
import REPL from "./REPL";

export default {
  props: ["current"],
  components: {
    REPL
  },
  data() {
    return {
      pwd: navigation.getPwdFromCurrent(this.current)
    };
  },
  computed: {
    historyItems: () => {
      return [
        {
          pwd: ["~"],
          input: "as",
          output: "Invalid command."
        }
      ];
    }
  },
  methods: {
    handleScroll(event) {
      if (window.scrollY / window.innerHeight > 0.5) {
        this.$refs.terminal.classList.add(this.$style.shown);
      } else {
        this.$refs.terminal.classList.remove(this.$style.shown);
      }
    },
    evalInput(cmdLine) {
      return cmdLine.split(/\s+/);
    },
    printOutput(content) {},
    runChangePage() {
      return "cd";
    },
    runListPage() {
      let list = navigation.listContents(this.pwd);
      console.log(list);
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
          .then(function(result) {
            console.log(result);
          })
          .catch(function(error) {
            console.error(error);
          });
      }
    },
    completeInput(cmdLine) {},
    collectInput(event) {
      if (event.keyCode == 13) {
        // Enter is presed.
        this.submitInput(event.target.value);
        event.target.value = "";
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
  moveAnimation(startDistance: -200px, targetDistance: 0px);
}

.items {
}

.blink {
  animation: blink 500ms infinite alternate;
}

.shown {
}
</style>
