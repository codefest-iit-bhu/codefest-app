<template>
  <div :class="$style.app" :style="`padding-bottom: ${this.appBottomPadding}`">
    <router-view/>
    <Terminal
      :propCurrent="current"
      v-model="terminalExpanded"
      ref="terminal"
      v-if="shouldShowTerminal"
    />
  </div>
</template>

<script>
import Terminal from "../components/Terminal";

export default {
  components: {
    Terminal
  },
  data() {
    return {
      current: null,
      terminalExpanded: false
    };
  },
  computed: {
    shouldShowTerminal: function() {
      let { noTerminal } = this.$route.meta;
      noTerminal = Object.is(noTerminal, undefined) ? true : noTerminal;
      return !(this.$mq === "sm" || this.$mq === "xs" || noTerminal);
    },
    appBottomPadding: function() {
      if (this.shouldShowTerminal)
        return this.terminalExpanded ? "200px" : "90px";
      else return "0px";
    }
  },
  methods: {
    showTerminal() {
      const { terminal } = this.$refs;
      if (!terminal) return;
      if (document.body.clientHeight > window.innerHeight)
        terminal.animateScrollShow();
      else terminal.noAnimateScrollShow();
    }
  },
  watch: {
    $route(to, from) {
      this.current = to.name;
      this.$nextTick(() => {
        this.showTerminal();
      });
    },
    $mq(to, from) {
      console.log(`$mq = ${to} <- ${from};`);
      this.$nextTick(() => {
        this.showTerminal();
      });
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';

body {
  background: $black;
}

.app {
  height: 100%;
  width: 100%;
}
</style>
