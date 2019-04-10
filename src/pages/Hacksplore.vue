<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar
      :shouldShowSideNavigation="isPastLanding"
      :shouldShowHaxploreLogo="isPastLanding"
      @scrollTop="scrollToTop"
    >
      <li :key="i" v-for="(title, i) in titles" v-show="!!title">
        <a>
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          {{ title }}
        </a>
      </li>
    </AppBar>
    <Landing/>
    <main :class="$style.wrapper">
      <div v-scroll-spy="{data: 'section'}" ref="scroller">
        <div></div>
        <About/>
        <FAQ/>
        <Timeline/>
        <Prizes/>
        <Sponsors/>
      </div>
    </main>
    <FooterN/>
  </div>
</template>

<script>
import AppBar from "@components/haxplore/AppBar";
import Timeline from "@components/haxplore/Timeline";
import About from "@components/haxplore/About";
import FAQ from "@components/haxplore/FAQ";
import Landing from "@components/haxplore/Landing";
import Prizes from "@components/haxplore/Prizes";
import Sponsors from "@components/Sponsors";
import FooterN from "@components/haxplore/FooterN";
import SectionLayout from "@components/layouts/SectionLayout";

export default {
  components: {
    AppBar,
    About,
    FAQ,
    Timeline,
    Prizes,
    SectionLayout,
    Landing,
    Sponsors,
    FooterN
  },
  data() {
    return {
      section: 0,
      titles: [null, "About", "FAQ", "Timeline", "Prizes", "Sponsors"]
    };
  },
  computed: {
    isPastLanding() {
      return this.section > 0;
    }
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 50px 0;
  z-index: 1;
  position: relative;
  font: 500 18px 'Quicksand';
  font-kerning: auto;
}

.faqContainer {
  width: 100%;
  font-size: 20px;

  .faqHeader {
    line-height: 30px;
    font-weight: bold;
    text-align: center;

    img {
      width: 300px;
      height: 300px;
    }
  }
}

.root.xs, .root.sm {
  .faqContainer {
    margin-top: 50px;

    .faqHeader {
      display: flex;
      flex-direction: row;
      align-items: flex-end;

      img {
        width: 100px;
        height: 100px;
      }

      .faqMessage {
        font-size: 13px;
        line-height: 20px;
        margin-left: 20px;
      }
    }

    .faqList {
      margin: 20px 0;
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
