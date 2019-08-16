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
    <Landing :devfolioKey="devfolioKey" @mounted="landingMounted"/>
    <main :class="$style.wrapper">
      <div v-scroll-spy="{data: 'section'}" ref="scroller">
        <div></div>
        <About/>
        <FAQ/>
        <Timeline/>
        <Prizes/>
        <HaxploreSponsors/>
      </div>
    </main>
    <FooterN/>
  </div>
</template>

<script>
const AppBar = () => import("@components/haxplore/AppBar");
const Timeline = () => import("@components/haxplore/Timeline");
const About = () => import("@components/haxplore/About");
const FAQ = () => import("@components/haxplore/FAQ");
const Landing = () => import("@components/haxplore/Landing");
import Prizes from "@components/haxplore/Prizes";
const HaxploreSponsors = () => import("@components/haxplore/HaxploreSponsors");
const FooterN = () => import("@components/haxplore/FooterN");
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    AppBar,
    About,
    FAQ,
    Timeline,
    Prizes,
    SectionLayout,
    Landing,
    HaxploreSponsors,
    FooterN
  },
  data() {
    return {
      section: 0,
      titles: [null, "About", "FAQ", "Timeline", "Prizes", "Sponsors"],
      devfolioKey: "haxplore"
    };
  },
  computed: {
    isPastLanding() {
      return this.section > 0;
    },
    devfolioRegisterLink() {
      return `https://devfolio.co/external-apply/${this.devfolioKey}`;
    }
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    },
    landingMounted() {
      let devfolioOptions = {
        buttonSelector: `#devfolio-apply-now`,
        key: this.devfolioKey
      };
      let script = document.createElement("script");
      script.src = "https://apply.devfolio.co";
      document.body.append(script);
      script.onload = function() {
        new Devfolio(devfolioOptions);
      };
    }
  },
  mounted() {}
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
