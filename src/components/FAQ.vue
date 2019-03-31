<template>
  <div :class="[$style.faqList, $style[$mq]]">
    <Q v-for="(item, i) in faqItems" :key="i" :item="item"/>
  </div>
</template>

<script>
import Q from "@components/Q";
export default {
  components: {
    Q
  },
  props: {
    faqItems: {
      type: Array,
      required: true
    }
  }
};
</script>

<style module lang="stylus">
.faqList {
  width: 100%;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
