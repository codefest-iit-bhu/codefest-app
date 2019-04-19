<template>
  <div
    :class="$style.wrapper"
    @mouseover="isSideNavigationIdle = false"
    @mouseleave="isSideNavigationIdle = true"
  >
    <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
      <slot></slot>
    </ul>
  </div>
</template>

<script>
export default {};
</script>

<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';

.wrapper {
  position: fixed;
  right: -140px;
  top: 0;
  width: 150px;
  padding: 15px;
  display: flex;
  flex-flow: column;
  justify-content: space-around;
  height: 100%;
  z-index: 9;

  ~/.md ^[1..-1], ~/.lg ^[1..-1] {
    background: linear-gradient(to right, alpha($mine-shaft, 0.8), alpha($mine-shaft, 0.1));
  }
}
</style>
