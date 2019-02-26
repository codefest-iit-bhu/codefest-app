<template>
  <div :class="$style.app" :style="`padding-bottom: ${this.terminalExpanded ? '200px' : '90px'}`">
    <router-view/>
    <Terminal :propCurrent="current" v-model="terminalExpanded" ref="terminal"/>
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
  watch: {
    $route(to, from) {
      let terminal = this.$refs.terminal;
      this.current = to.name;
      this.$nextTick(() => {
        if (document.body.clientHeight > window.innerHeight)
          terminal.animateScrollShow();
        else terminal.noAnimateScrollShow();
      });
    }
  }
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';

body {
  background: $black;
}

.app {
  height: 100%;
  width: 100%;
}
</style>
