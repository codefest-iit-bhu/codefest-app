<template>
  <div :class="$style.root">
    <AppBar :currentPage="'events'" />
    <div :class="$style.wrapper2">
      <div :class="$style.wrapper">
        <Timeline></Timeline>
      </div>
      <div :class="$style.wrapper">
        <SpecialEvent v-for="event in events" :eventName="event.name" :key="event.id" :id="event.id" />

        <!-- <mq-layout :mq="['md', 'lg', 'xl', 'xxl']">
        <StandardEvent
          v-for="(event, i) in events"
          :key="i"
          :event="event"
          :id="i"
          :keepOpen="isMinimal"
        />
      </mq-layout>
      <mq-layout :mq="['sm', 'xs']">
        <StandardEventMobile
          v-for="(event, i) in events"
          :key="i"
          :event="event"
          :id="i"
        />
      </mq-layout> -->
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import API from "@js/api";
const AppBar = () => import("@components/Menu/AppBar");
const SpecialEvent = () => import("@components/SpecialEvent");
const StandardEvent = () => import("@components/StandardEvent");
const StandardEventMobile = () => import("@components/StandardEventMobile");
const Timeline = () => import("@components/EventDetails/Timeline");
const Footer = () => import("@components/Footer");
import events from "@store/events";
import { isMinimal } from "@js/utils";

export default {
  components: {
    AppBar,
    StandardEventMobile,
    StandardEvent,
    Footer,
    SpecialEvent,
    Timeline,
  },
  data() {
    return {
      events: []
    }
    // return events;
  },
  computed: {
    isMinimal() {
      return isMinimal(this.$mq);
    },
  },
  created() {
    API.fetch("events/")
      .then(({ data }) => {
        if (data.length === 0) {
          this.events = [];
        }
        this.events = data.map(event => {
          return {
            id: event.id,
            name: event.name
          }
        })
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

.wrapper {
  width: 40%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  $font-size: 18px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.wrapper2 {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  $font-size: 18px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  padding-top: 80px;
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
