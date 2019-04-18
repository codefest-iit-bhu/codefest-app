<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true" :isSideNavigationShown="false" @scrollTop="scrollToTop"/>
    <Hero/>
    <main :class="$style.wrapper">
      <!-- Introduction -->
      <SectionLayout title="A Byte About Us" :contentStyle="{'text-align': 'justify'}">
        <Intro/>
      </SectionLayout>
      <!-- Lookback at CF'18 -->
      <SectionLayout title="Lookback">
        <Lookback/>
      </SectionLayout>
      <SectionLayout title="Testimonials">
        <Testimonials/>
      </SectionLayout>
      <Sponsors/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/Menu/AppBar";
import SectionLayout from "@components/layouts/SectionLayout";
import ResponsiveTwoColumnLayout from "@components/layouts/ResponsiveTwoColumnLayout";
import Hero from "@components/Hero";
import Intro from "@components/Intro";
import Footer from "@components/Footer";
import Lookback from "@components/Lookback";
import Sponsors from "@components/Sponsors";
import Testimonials from "@components/Testimonials";

export default {
  components: {
    AppBar,
    Hero,
    Intro,
    SectionLayout,
    ResponsiveTwoColumnLayout,
    Lookback,
    Sponsors,
    Footer,
    Testimonials
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';

.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font: 500 18px 'Quicksand';
  padding: 100px 0;
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
