<template>
  <div :class="[$style.floatBtn, animateClass]" @click="openLink">
    <i class="fas fa-user-plus" :class="$style.btn"></i>
    <span :class="$style.txt">{{ text }}</span>
  </div>
</template>

<script>
import { isMinimal } from "@js/utils";

export default {
  props: {
    text: {
      required: true,
      type: String,
    },
    link: {
      required: false,
      type: String,
      default: null,
    },
  },
  computed: {
    animateClass() {
      return isMinimal(this.$mq) ? "" : this.$style.animate;
    },
  },
  methods: {
    openLink() {
      if (this.link != null) this.$router.push({ name: this.link });
    },
  },
};
</script>

<style module lang="stylus">
$btn-height = 60px;
$btn-width = 60px;
$btn-radius = 30px;
$btn-expand-width = 150px;
$image-expand-width = 18px;

.floatBtn {
  stickWithSpace(bottom: 40px, right: 40px);
  width: $btn-width;
  height: $btn-height;
  background-color: $waterloo;
  color: $waterloo;
  border-radius: $btn-radius;
  text-align: center;
  z-index: 999;
  overflow: hidden;
  transition: width 0.3s;
  cursor: pointer;

  .btn {
    color: black;
    height: 100%;
    width: 100%;
  }

  .txt {
    color: black;
    font-family: 'Aldo the Apache';
    $font-size: 18px;
    margin-left: 5px;
  }

  &.animate:hover {
    width: $btn-expand-width;

    .btn {
      width: auto;
    }
  }

  i {
    margin-top: (($btn-height - 18px) / 2);
  }
}
</style>
