<template>
  <div>
    <div :class="$style.container">
      <div :class="$style.itemWrapper" v-for="(slot, i) in Object.keys($slots)" :key="i">
        <slot :name="slot"></slot>
      </div>
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
      type: Number,
      default: 200
    },
    itemHeight: {
      type: Number,
      default: 200
    }
  }
};
</script>
<style module lang="stylus">
.container {
  display: grid;
  grid-template-columns: 300px; // 200px 200px;
  grid-template-rows: 200px;
  grid-column-gap: 30px;
  grid-row-gap: 50px;
  justify-content: space-evenly;

  .itemWrapper {
  }
}
</style>
