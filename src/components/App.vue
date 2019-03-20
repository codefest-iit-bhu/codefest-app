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
      return !(this.$mq === "sm" || this.$mq === "xs");
    },
    appBottomPadding: function() {
      if (this.shouldShowTerminal)
        return this.terminalExpanded ? "200px" : "90px";
      else return "0px";
    }
  },
  watch: {
    $route(to, from) {
      const { terminal } = this.$refs;
      if (!terminal) return;
      this.current = to.name;
      this.$nextTick(() => {
        if (document.body.clientHeight > window.innerHeight)
          terminal.animateScrollShow();
        else terminal.noAnimateScrollShow();
      });
    },
    $mq(to, from) {
      console.log(`$mq = ${to} <- ${from};`);
    }
  }
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';

:root {
  --base-font: 12px;
}

@media (max-width: 767px) {
  :root {
    --base-font: 8px;
  }
}

body {
  background: $black;
}

.app {
  font-size: var(--base-font);
  height: 100%;
  width: 100%;
}
</style>
