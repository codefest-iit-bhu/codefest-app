<template>
  <div :class="$style.faqItem">
    <div :class="[$style.question,$style[$mq]]" @click="toggleQues">
      <p>
        {{item.question}}
        <i class="fa fa-chevron-down" :style="chevronRotateStyle" aria-hidden="true"></i>
      </p>
    </div>
    <div :class="[$style.answer,$style[$mq]]" :style="answerHeightStyle">
      <p>{{item.answer}}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      open: false,
      openProgress: 0,
      maxHeight: 100
    };
  },

  props: {
    item: {
      required: true,
      type: Object
    }
  },

  methods: {
    toggleQues: function() {
      this.open = !this.open;
    }
  },

  computed: {
    height() {
      return this.openProgress * this.maxHeight;
    },
    angle() {
      return this.openProgress * 180;
    },
    answerHeightStyle() {
      return { height: `${this.height}px` };
    },
    chevronRotateStyle() {
      return { transform: `rotate(${this.angle}deg)` };
    }
  },

  watch: {
    open: function(val) {
      TweenLite.to(this.$data, 0.4, { openProgress: val ? 1 : 0 });
    }
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.faqItem {
  position: relative;
  width: 100%;
  text-align: left;
  clear: both;
  border-bottom: 2px solid $chartreuse;

  .question {
    font-size: 20px;
    cursor: pointer;
    font-family: 'ubuntu';
    font-weight: bold;

    i {
      position: absolute;
      right: 0px;
    }

    &.xs, &.sm {
      font-size: 15px;
    }
  }

  .answer {
    font-size: 18px;
    overflow: hidden;
    width: 100%;
    clear: both;
    font-family: 'Roboto mono';

    &.xs, &.sm {
      font-size: 13px;
    }
  }
}
</style>
