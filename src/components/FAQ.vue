<template>
  <div :class="[$style.faqList, $style[$mq]]">
    <QuesAns
      v-for="(item, i) in faqItems"
      :key="i"
      :item="item"
      ref="faqs"
      :index="i"
      @onToggleQuestion="closeOtherQuestions"
      v-bind:codestart="pcodestart"
    >
      <slot :name="i">
        <p :inner-html.prop="item.answer | anchor"></p>
      </slot>
    </QuesAns>
  </div>
</template>

<script>
const QuesAns = () => import("@components/QuesAns");

export default {
  components: {
    QuesAns
  },
  data() {
    return {
      pcodestart : this.codestart,
    }
  },
  props: {
    faqItems: {
      type: Array,
      required: true
    },
    codestart: {
      required: false,
      type:Boolean,
    }
  },
  methods: {
    closeOtherQuestions(index, isOpen) {
      let { faqs } = this.$refs;
      faqs.forEach((faq, i) => {
        if (i != index) faq.open = false;
      });
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
