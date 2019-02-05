<template>
  <div :class="$style.app">
    <router-view/>
  </div>
</template>

<script>
export default {};
</script>

<style module lang="styl">
@import "../styles/colors.styl";

.app {
  background: $black;
}
</style>
