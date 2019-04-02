<template>
  <div :class="[$style.faqList, $style[$mq]]">
    <QuesAns v-for="(item, i) in faqItems" :key="i" :item="item" ref="faqs" :index="i" @onToggleQuestion="closeOtherQuestions"/>
  </div>
</template>

<script>
import QuesAns from "@components/QuesAns";
export default {
  components: {
    QuesAns
  },
  props: {
    faqItems: {
      type: Array,
      required: true
    }
  },
  methods: {
    closeOtherQuestions(index, isOpen) {
      let { faqs } = this.$refs;
      faqs.forEach((faq, i) => {
        if (i != index)
          faq.open = false
      })
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
