<template>
  <GridLayout :itemWidth="eventCardWidth" :class="$style.eventWrapper">
    <EventTeam
      v-for="event in events"
      :key="event.id"
      :event="event"
      :class="$style.eventCard"
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
      events: []
    };
  },
  computed: {
    eventCardWidth() {
      return isMinimal(this.$mq) ? "280px" : "350px";
    }
  },
  created() {
    API.fetch("events/")
      .then(({ data }) => {
        if (data.length === 0) {
          this.events = [];
        }
        this.events = data
      })
      .catch(err => {
        this.events = []
        console.log(err);
      })
    // this.events=["Try1","Try2","Try3","Try4","Try5"];
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
