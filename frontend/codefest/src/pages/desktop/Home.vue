<template>
  <div :class="$style.root">
    <!-- <AppBar/> -->
    <Hero/>
    <main :class="$style.wrapper">
      <!-- Introduction -->
      <Intro/>
      <!-- Lookback at CF'18 -->
      <Lookback/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Intro from "@components/Intro";
import Hero from "@components/Hero";
import Quote from "@components/Quote";
import Terminal from "@components/Terminal";
import Footer from "@components/Footer";
import Lookback from "@components/Lookback";
export default {
  components: {
    AppBar,
    Hero,
    Intro,
    Lookback,
    Footer
  },
  data: () => {
    return {};
  }
};
</script>
<style module lang="stylus">
.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  min-height: calc(55vh - 16px);
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  margin-bottom: 200px;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
