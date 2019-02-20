<template>
  <div :class="$style.app">
    <router-view/>
    <Terminal :propCurrent="current" ref="terminal"/>
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
      current: null
    };
  },
  watch: {
    $route(to, from) {
      let terminal = this.$refs.terminal;
      terminal.animateScrollShow();
      this.current = to.name;
    }
  }
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';

.app {
  background: $black;
  height: 100%;
}
</style>
