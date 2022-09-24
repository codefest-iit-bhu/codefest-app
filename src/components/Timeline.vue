<template>
  <div :class="$style.timeline">
    <TimelineCheckpoint v-for="(checkpoint, i) in timeline" :key="i" :data="checkpoint" />
  </div>
</template>

<script>
const TimelineCheckpoint = () => import("@components/TimelineCheckpoint");

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
  width: 100%;
  margin-bottom: 50px;
  float: left;
}
</style>
