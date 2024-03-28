<template>
  <div :class="$style.root">
    <AppBar />
    <main :class="$style.wrapper">
      <CAHero />
      <SectionLayout title="What is the Campus Ambassador Program?">
        <AboutCA />
      </SectionLayout>
      <SectionLayout title="What is a Campus Ambassador’s job?">
        <Work />
      </SectionLayout>
      <SectionLayout title="Why should you become a Campus Ambassador?">
        <Perks />
      </SectionLayout>
      <SectionLayout title="FAQ">
        <FaqCA />
      </SectionLayout>
     
        <PointsTable />
    </main>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const CAHero = () => import("@components/ca/CAHero");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const Work = () => import("@components/ca/Work");
const AboutCA = () => import("@components/ca/AboutCA");
const Perks = () => import("@components/ca/Perks");
const FaqCA = () => import("@components/ca/FaqCA");
const ContactCA = () => import("@components/ca/ContactCA");
const PointsTable = () => import("@components/ca/PointsTable");
export default {
  components: {
    AppBar,
    CAHero,
    Footer,
    Work,
    AboutCA,
    Perks,
    ContactCA,
    FaqCA,
    PointsTable,
    SectionLayout,
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: auto;
  position: relative;
  z-index: 1;
  padding: 200px 20px 50px 20px;
  $font-size: 18px;
}

.root {
  height: 100%;
}

@media screen and (max-width: 996px) {
  .wrapper {
    width: 95%;
    margin: 0 auto;
    padding-top: 120px;
  }
}
</style>
