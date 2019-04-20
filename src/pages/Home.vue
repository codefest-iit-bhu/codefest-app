<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true" @scrollTop="scrollToTop"/>
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
const AppBar = () => import("@components/Menu/AppBar");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");
const Hero = () => import("@components/Hero");
const Intro = () => import("@components/Intro");
const Footer = () => import("@components/Footer");
const Lookback = () => import("@components/Lookback");
const Sponsors = () => import("@components/Sponsors");
const Testimonials = () => import("@components/Testimonials");

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
