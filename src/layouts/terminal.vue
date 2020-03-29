<template>
  <div :class="$style.app" :style="`padding-bottom: ${appBottomPadding}`">
    <nuxt />
    <Terminal
      ref="terminal"
      v-model="isTerminalExpanded"
      :prop-current="current"
      @onTerminalStateChanged="terminalStateChanged"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Terminal from '@components/Terminal.vue'

export default Vue.extend({
  components: {
    Terminal
  },
  data() {
    return {
      current: null,
      isTerminalExpanded: false,
      isTerminalShown: true
    }
  },
  computed: {
    appBottomPadding() {
      if (this.isTerminalShown)
        return this.isTerminalExpanded ? '200px' : '90px'
      else return '0px'
    }
  },
  watch: {
    $mq(to, from) {
      if (to === from) return
      console.log(`$mq = ${to} <- ${from};`)
      this.$nextTick(() => {
        this.showTerminal()
      })
    }
  },
  methods: {
    showTerminal() {
      const { terminal } = this.$refs
      if (!terminal) return
      if (this.$route.meta.animateTerminal) terminal.animateScrollShow()
      else terminal.noAnimateScrollShow()
    },
    terminalStateChanged(isShown: boolean) {
      this.isTerminalShown = isShown
    }
  }
})
</script>

<style module lang="stylus">
body {
  background: $black;
}

.app {
  height: 100%;
  width: 100%;
}
</style>
