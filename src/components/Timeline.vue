<template>
  <div :class="$style.timeline">
    <TimelineCheckpoint v-for="(checkpoint, i) in timeline" :key="i" :data="checkpoint"/>
  </div>
</template>

<script>
import TimelineCheckpoint from "@components/TimelineCheckpoint";

export default {
  components: {
    TimelineCheckpoint
  },
  props: {
    timeline: {
      type: Array,
      required: true
    }
  }
};
</script>

<style module lang="stylus">
.timeline {
  position: relative;
  height: 100%;
  width: 40%;
  padding: 0 5%;
  margin-bottom: 50px;
  margin-left: 10%;
  float: left;
}
</style>
