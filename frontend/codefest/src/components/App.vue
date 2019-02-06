<template>
  <div :class="$style.app">
    <router-view/>
    <Terminal :current="current" :key="current"/>
  </div>
</template>

<script>
import Terminal from "../components/Terminal";

export default {
  components: {
    Terminal
  },
  data() {
    return {
      current: "~"
    };
  },
  watch: {
    $route(to, from) {
      this.current = `~${to.path}`;
    }
  }
};
</script>

<style module lang="styl">
@import "../styles/colors.styl";

.app {
  background: $black;
}
</style>
