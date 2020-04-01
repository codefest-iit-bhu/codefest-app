<template>
  <div :class="[$style.lookback, $style[$mq]]">
    <GridLayout :itemWidth="computedWidth">
      <div :class="$style.stat" v-for="(stat, i) in this.stats" :key="i" :slot="`item${i}`">
        <div :class="$style.clip">
          <img :src="stat.image" :class="$style.img">
        </div>
        <div :class="$style.name">{{ stat.name }}</div>
        <div :class="$style.value">{{ stat.value }}</div>
      </div>
    </GridLayout>
  </div>
</template>
<script>
import GridLayout from "./layouts/GridLayout";

export default {
  props: {
    stats: {
      type: Object
    }
  },
  components: {
    GridLayout
  },
  computed: {
    computedWidth() {
      if (this.$mq == "lg") return "160px";
      return "220px";
    }
  },
  data() {
    return {
      stats: [
        {
          name: "Prize Money",
          value: "650,000",
          image: "assets/Lookback/lb_prize.svg"
        },
        {
          name: "Countries",
          value: "104",
          image: "assets/Lookback/lb_countries.svg"
        },
        {
          name: "Participants",
          value: "29,800",
          image: "assets/Lookback/lb_participant.svg"
        },
        {
          name: "Unique Visitors",
          value: "664,300",
          image: "assets/Lookback/lb_visitor.svg"
        },
        {
          name: "Registrations",
          value: "23,000",
          image: "assets/Lookback/lb_registration.svg"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';

.lookback {
  .stat {
    width: 200px;
    height: 200px;

    &:nth-child(odd) {
      &::before {
        content: '';
        width: 100px;
      }
    }

    .clip {
      border-radius: 30px;
      box-shadow: var(--box-shadow);
      background: white;
      width: 160px;
      height: 160px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 5px;
      padding: 10px;
      background-color: $vermilion;
    }

    .img {
      width: 70%;
      height: 70%;
      position: relative;
      top: 10%;
      left: 15%;
    }

    .name, .value {
      font-family: 'Quicksand';
      font-weight: 500;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      color: $vermilion;
      line-height: 28px;
      font-size: 25px;
    }
  }
}
</style>
