<template>
  <div :class="$style.container" :style="gridStyle">
    <div :class="$style.itemWrapper" v-for="(slot, i) in Object.keys($slots)" :key="i">
      <slot :name="slot"></slot>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    columns: {
      type: Number,
      default: 3
    },
    itemWidth: {
      type: String,
      default: "200px"
    },
    itemHeight: {
      type: String,
      default: "200px"
    }
  },
  computed: {
    gridStyle() {
      return {
        "grid-template-columns": `repeat(auto-fit, minmax(${
          this.itemWidth
        }, 1fr))`
      };
    }
  }
};
</script>
<style module lang="stylus">
.container {
  display: grid;
  grid-column-gap: 30px;
  grid-row-gap: 50px;
  justify-content: space-evenly;

  .itemWrapper {
    margin: 0 auto;
  }
}
</style>
