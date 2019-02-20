<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true"/>
    <Hero/>
    <main :class="$style.wrapper">
      <!-- Introduction -->
      <Intro/>
      <!-- Lookback at CF'18 -->
      <Lookback/>
      <!-- Sponsors -->
      <Sponsors/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Intro from "@components/Intro";
import Hero from "@components/Hero";
import Footer from "@components/Footer";
import Lookback from "@components/Lookback";
import Sponsors from "@components/Sponsors";
export default {
  components: {
    AppBar,
    Hero,
    Intro,
    Lookback,
    Sponsors,
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
  z-index: 1;
  font-family: 'Roboto Mono';
  padding-bottom: 100px;
  font-size: 18px;
}

.root {
  height: 100%;
  margin-bottom: 200px;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
