<template>
  <GridLayout :itemWidth="eventCardWidth" :class="$style.eventWrapper">
    <EventTeam
      v-for="(event, i) in events"
      :key="i"
      :event="event"
      :class="$style.eventCard"
      :slot="i"
    />
  </GridLayout>
</template>

<script>
import eventsStore from "@store/events";
import API from "@js/api";
import { isMinimal } from "@js/utils";

const AppBar = () => import("@components/Menu/AppBar");
const GridLayout = () => import("@components/layouts/GridLayout");
const EventTeam = () => import("@components/dashboard/EventTeam");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    EventTeam,
    GridLayout,
    Footer
  },
  data() {
    return {
      events: eventsStore.events
    };
  },
  computed: {
    eventCardWidth() {
      return isMinimal(this.$mq) ? "280px" : "350px";
    }
  },
  created() {
    this.$store.dispatch("getProfileEvents").then(data => {
      this.events = data;
    });
  }
};
</script>

<style module lang="stylus">
.eventWrapper {
  margin-top: 40px;

  .eventCard {
  }
}
</style>
