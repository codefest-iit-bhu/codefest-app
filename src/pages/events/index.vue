<template>
  <div :class="$style.root">
    <AppBar />
    <main :class="$style.wrapper">
      <SpecialEvent />
      <StandardEvent
        v-for="(event, i) in events"
        :id="i"
        :key="i"
        :event="event"
        :keep-open="isMinimal"
      />
    </main>
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { isMinimal } from '@js/utils'
import events from '~/store/events'
const AppBar = () => import('@components/Menu/AppBar')
const SpecialEvent = () => import('@components/SpecialEvent')
const StandardEvent = () => import('@components/StandardEvent')
const Footer = () => import('@components/Footer')

export default Vue.extend({
  components: {
    AppBar,
    SpecialEvent,
    StandardEvent,
    Footer
  },
  layout: (ctx) => (ctx.isDesktopOrTablet ? 'terminal' : 'mobile'),
  data() {
    return events
  },
  computed: {
    isMinimal() {
      return isMinimal(this.$mq)
    }
  }
})
</script>

<style module lang="stylus">
.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 100px 0;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
