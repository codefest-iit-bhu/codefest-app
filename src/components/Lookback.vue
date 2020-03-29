<template>
  <div :class="[$style.lookback, $style[$mq]]">
    <GridLayout :item-width="computedWidth">
      <div
        v-for="(stat, i) in stats"
        :key="i"
        :slot="`item${i}`"
        :class="$style.stat"
      >
        <div :class="$style.clip">
          <img :src="imgSrc(stat.image)" :class="$style.img" />
        </div>
        <div :class="$style.name">{{ stat.name }}</div>
        <div :class="$style.value">{{ stat.value }}</div>
      </div>
    </GridLayout>
  </div>
</template>

<script lang="ts">
import { assetSource } from '@js/utils'
import Vue from 'vue'
import GridLayout from './layouts/GridLayout'

export default Vue.extend({
  components: {
    GridLayout
  },
  props: {
    stats: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    computedWidth() {
      if (this.$mq === 'lg') return '160px'
      return '220px'
    }
  },
  methods: {
    imgSrc(path: string) {
      return assetSource(path)
    }
  }
})
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
      clip-path: polygon(25% 0%, 75% 0%, 100% 43.3%, 75% 86.6%, 25% 86.6%, 0% 43.3%);
      background: white;
      width: 160px;
      height: 160px;
      margin-left: auto;
      margin-right: auto;
      padding: 10px;
      background-color: $chartreuse;
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
      color: $chartreuse;
      line-height: 28px;
      $font-size: 25px;
    }
  }
}
</style>
