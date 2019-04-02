<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true"/>
    <mq-layout mq="lg+">
      <Hero/>
    </mq-layout>
    <main :class="$style.wrapper">
      <!-- Introduction -->
      <SectionLayout title="A Byte About Us" :contentStyle="{'text-align': 'justify'}">
        <p>
          The Department of Computer Science and Engineering, IIT (BHU) Varanasi
          brings to you yet another edition of its annual coding extravaganza, Codefest!
          Being more diverse than ever, Codefest '19 boasts of a plethora of events,
          ranging from competitive programming, algorithms and application development
          to upcoming trends like cryptography, machine learning, computer vision and cyber security.
          With problems being of varying difficulty levels, Codefest provides the perfect platform
          for fresh enthusiasts, as well as the experienced ones, to code together and compete for ultimate glory.
        </p>
      </SectionLayout>
      <!-- Lookback at CF'18 -->
      <SectionLayout title="Lookback">
        <Lookback/>
      </SectionLayout>
      <!-- Sponsors -->
      <!-- <Sponsors/> -->
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import SectionLayout from "@components/layouts/SectionLayout";
import Hero from "@components/Hero";
import Footer from "@components/Footer";
import Lookback from "@components/Lookback";
import Sponsors from "@components/Sponsors";
export default {
  components: {
    AppBar,
    Hero,
    SectionLayout,
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
@require '~@styles/mixins';

.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font-family: 'Quicksand';
  font-weight: 500;
  font-kerning: auto;
  padding-bottom: 100px;
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
