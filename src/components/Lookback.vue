<template>
  <div :class="[$style.lookback, $style[$mq]]">
    <GridLayout :itemWidth="computedWidth">
      <div
        :class="$style.stat"
        v-for="(stat, i) in this.stats"
        :key="i"
        :slot="`item${i}`"
      >
        <div :class="$style.clip">
          <img :src="stat.image" :class="$style.img" />
        </div>
        <div :class="$style.name">{{ stat.name }}</div>
        <div :class="$style.value">{{ stat.value }}</div>
      </div>
    </GridLayout>
  </div>
</template>
<script>
const GridLayout = () => import("./layouts/GridLayout");

export default {
  props: {
    stats: {
      type: Array,
    },
  },
  components: {
    GridLayout,
  },
  computed: {
    computedWidth() {
      if (this.$mq == "lg") return "160px";
      return "220px";
    },
  },
};
</script>

<style module lang="stylus">
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
      box-shadow: var(--icon-shadow);
      background: white;
      width: 160px;
      height: 160px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 25px;
      padding: 10px;
      background-color: $waterloo;
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
      font-weight: 700;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      color: var(--text-color);
      line-height: 28px;
      $font-size: 25px;
    }
  }
}
</style>
