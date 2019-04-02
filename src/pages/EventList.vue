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
        :keepOpen="$mq === 'xs' || $mq === 'sm'"
      />
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/Menu/AppBar";
import SpecialEvent from "@components/SpecialEvent";
import StandardEvent from "@components/StandardEvent";
import Footer from "@components/Footer";
import events from "@js/store/events";

export default {
  components: {
    AppBar,
    SpecialEvent,
    StandardEvent,
    Footer
  },
  data() {
    return events;
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
