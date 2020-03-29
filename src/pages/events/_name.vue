<template>
  <div :class="$style.root">
    <AppBar :should-show-side-navigation="true" @scrollTop="scrollToTop">
      <li
        v-for="(event, i) in events"
        :key="i"
        slot="events"
        :class="{ [$style.active]: i === currentEventIndex }"
      >
        <n-link :to="'/events/' + event.name">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          {{ event.title }}
        </n-link>
      </li>
    </AppBar>
    <main :class="$style.wrapper">
      <StandardEventDetails :event="events[currentEventIndex]" />
    </main>
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import events from '~/store/events'
const AppBar = () => import('@components/Menu/AppBar')
const StandardEventDetails = () => import('@components/StandardEventDetails')
const Footer = () => import('@components/Footer')

export default Vue.extend({
  components: {
    AppBar,
    StandardEventDetails,
    Footer
  },
  layout: (ctx) => (ctx.isDesktopOrTablet ? 'terminal' : 'mobile'),
  data() {
    return events
  },
  computed: {
    currentEventIndex() {
      const urlName = this.$route.params.name
      return this.events.findIndex((event) => event.name === urlName)
    }
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut })
    }
  },
  validate({ params }) {
    return events.events.findIndex((event) => event.name === params.name) !== -1
  }
})
</script>

<style module lang="stylus">
@require '~@styles/anims';

.wrapper {
  width: 75%;
  margin: 0 auto;
  padding: 100px 20px 50px 20px;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

.active {
  a {
    color: $chartreuse;
    font-weight: bold;

    span {
      color: $white;
      animation: neon-text 1s ease-in-out infinite alternate;
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
