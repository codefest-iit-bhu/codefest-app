<template>
  <div :class="$style.root">
    <Events/>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Events from "@components/Events";
import Terminal from "@components/Terminal";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    Events,
    Terminal,
    Footer
  }
};
</script>
<style module lang="stylus">
.wrapper {
  width: 100%;
  margin: 0 auto;
  position: relative;
  min-height: calc(55vh - 16px);
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
