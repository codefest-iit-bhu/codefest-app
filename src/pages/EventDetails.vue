<template>
  <div :class="$style.root">
    <AppBar @scrollTop="scrollToTop" :shouldShowSideNavigation="true">
      <li
        v-for="(event, i) in events"
        :key="i"
        :class="{ [$style.active]: i === currentEventIndex }"
        slot="events"
      >
        <router-link :to="'/events/' + event.name">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          {{ event.title }}
        </router-link>
      </li>
    </AppBar>
    <main :class="$style.wrapper">
      <StandardEventDetails :event="events[currentEventIndex]" />
    </main>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const StandardEventDetails = () => import("@components/StandardEventDetails");
const Footer = () => import("@components/Footer");
import events from "@store/events";
export default {
  components: {
    AppBar,
    StandardEventDetails,
    Footer,
  },
  data() {
    return events;
  },
  computed: {
    currentEventIndex() {
      const urlName = this.$route.params.name;
      let i = this.events.findIndex((event) => event.name === urlName);
      if (i === -1) {
        this.$router.replace("/404");
        return;
      }
      return i;
    },
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    },
  },
};
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
  $font-size: 18px;
}

.root {
  height: 100%;
}

.active {
  a {
    color: $waterloo;
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
