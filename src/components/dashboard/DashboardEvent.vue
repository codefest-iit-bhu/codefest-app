<template>
  <GridLayout :itemWidth="eventCardWidth">
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

import AppBar from "@components/Menu/AppBar";
import GridLayout from "@components/layouts/GridLayout";
import EventTeam from "@components/dashboard/EventTeam";
import Footer from "@components/Footer";

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
.eventCard {
}
</style>
