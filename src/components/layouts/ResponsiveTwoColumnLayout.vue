<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <div :class="[$style.left, leftClass]">
      <slot name="left"></slot>
    </div>
    <div :class="[$style.right, rightClass]">
      <slot name="right"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isRightAbove: {
      required: false,
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isMinimal() {
      return this.$mq === "xs" || this.$mq === "sm";
    },
    leftClass() {
      return this.isMinimal && !this.isRightAbove ? this.$style.upper : "";
    },
    rightClass() {
      return this.isMinimal && this.isRightAbove ? this.$style.upper : "";
    },
  },
};
</script>

<style module lang="stylus">
.wrapper {
  width: 100%;
  font-family: 'ubuntu';
  $font-size: 20px;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: flex-start;

  .left, .right {
    width: 100%;
  }

  .upper {
    order: -1;
  }

  &.xs, &.sm {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
