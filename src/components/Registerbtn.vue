<template>
  <div :class="$style.floatBtn" @click="$emit('onClick')">
    <i class="fas fa-user-plus" :class="$style.btn"></i>
    <span :class="$style.txt">{{ text }}</span>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      required: true,
      type: String
    }
  }
};
</script>

<style module lang = "stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

$btn-height = 60px;
$btn-width = 60px;
$btn-radius = 30px;
$btn-expand-width = 150px;
$image-expand-width = 18px;

.floatBtn {
  stickWithSpace(bottom: 40px, right: 40px);
  width: $btn-width;
  height: $btn-height;
  background-color: $chartreuse;
  color: $chartreuse;
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
    font-size: 18px;
    margin-left: 5px;
  }

  &:hover {
    width: $btn-expand-width;

    .btn {
      width: auto;
    }
  }
}

i {
  margin-top: (($btn-height - 18px) / 2);
}
</style>