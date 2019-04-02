<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <StandardEventDetails :event="events[currentEventIndex]"/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/Menu/AppBar";
import StandardEventDetails from "@components/StandardEventDetails";
import Footer from "@components/Footer";
import events from "@js/store/events";
export default {
  components: {
    AppBar,
    StandardEventDetails,
    Footer
  },
  data() {
    return events;
  },
  computed: {
    currentEventIndex() {
      const urlName = this.$route.params.name;
      let i = this.events.findIndex(event => event.name === urlName);
      if (i === -1) {
        this.$router.replace("/404");
        return;
      }
      return i;
    }
  }
};
</script>

<style module lang="stylus">
.wrapper {
  width: 80%;
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

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
