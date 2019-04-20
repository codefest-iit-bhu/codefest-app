<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <SpecialEvent/>
      <StandardEvent
        v-for="(event, i) in events"
        :key="i"
        :event="event"
        :id="i"
        :keepOpen="isMinimal"
      />
    </main>
    <Footer/>
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const SpecialEvent = () => import("@components/SpecialEvent");
const StandardEvent = () => import("@components/StandardEvent");
const Footer = () => import("@components/Footer");
import events from "@store/events";
import { isMinimal } from "@js/utils";

export default {
  components: {
    AppBar,
    SpecialEvent,
    StandardEvent,
    Footer
  },
  data() {
    return events;
  },
  computed: {
    isMinimal() {
      return isMinimal(this.$mq);
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';

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
