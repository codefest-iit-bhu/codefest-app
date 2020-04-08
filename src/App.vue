<template>
  <div
    :class="$style.app"
    :data-theme="currentTheme"
    :style="`padding-bottom: ${this.appBottomPadding}`"
  >
    <router-view />
    <Terminal
      :propCurrent="current"
      v-model="terminalExpanded"
      ref="terminal"
      v-if="shouldShowTerminal"
      @onTerminalStateChanged="terminalStateChanged"
    />
  </div>
</template>

<script>
const Terminal = () => import("@components/Terminal");

export default {
  components: {
    Terminal,
  },
  data() {
    return {
      current: null,
      terminalExpanded: false,
      isTerminalShown: true,
    };
  },
  computed: {
    shouldShowTerminal: function() {
      let { noTerminal } = this.$route.meta;
      noTerminal = Object.is(noTerminal, undefined) ? true : noTerminal;
      return !(this.$mq === "sm" || this.$mq === "xs" || noTerminal);
    },
    appBottomPadding: function() {
      if (this.shouldShowTerminal && this.isTerminalShown)
        return this.terminalExpanded ? "200px" : "90px";
      else return "0px";
    },
    currentTheme: function() {
      return this.$store.getters.currentTheme;
    },
  },
  methods: {
    showTerminal() {
      const { terminal } = this.$refs;
      if (!terminal) return;
      if (this.$route.meta.animateTerminal) terminal.animateScrollShow();
      else terminal.noAnimateScrollShow();
    },
    terminalStateChanged(isShown) {
      this.isTerminalShown = isShown;
    },
  },
  watch: {
    $route(to, from) {
      if (to === from) return;
      this.current = to.path;
      this.$nextTick(() => {
        this.showTerminal();
      });
    },
    $mq(to, from) {
      if (to === from) return;
      console.log(`$mq = ${to} <- ${from};`);
      this.$nextTick(() => {
        this.showTerminal();
      });
    },
  },
  created() {
    if (this.$workbox) {
      this.$workbox.addEventListener("waiting", () => {
        console.log("WORKBOX ---- Waiting to update UI!");
        this.$workbox.messageSW({ type: "SKIP_WAITING" });
      });
    }
  },
};
</script>

<style module lang="stylus">
.app {
  color: var(--text-color);
  background: var(--background-color);
  height: 100%;
  width: 100%;
}
</style>
