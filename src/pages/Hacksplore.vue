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
        <SectionLayout title="Lookback">
          <Lookback :stats="lookbackStats" />
        </SectionLayout>
        <SectionLayout title="Testimonials">
          <Testimonials :testimonials="testimonials" />
        </SectionLayout>
        <!-- <Timeline/> -->
        <!-- <Prizes/> -->
        <!-- <HaxploreSponsors/> -->
        <SectionLayout title="Sponsor Us">
          <div :class="$style.link">
            <a href="https://drive.google.com/file/d/15BYqDZwShgFFqkgBPKqr0j-AcFF-_Umm" :class="$style.linkText" target="_blank">
              <h4> Sponsor Brochure </h4>
            </a>
          </div>
        </SectionLayout>
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
const Lookback = () => import("@components/Lookback");
import Prizes from "@components/haxplore/Prizes";
const HaxploreSponsors = () => import("@components/haxplore/HaxploreSponsors");
const FooterN = () => import("@components/haxplore/FooterN");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const Testimonials = () => import("@components/Testimonials");

export default {
  components: {
    AppBar,
    About,
    FAQ,
    Timeline,
    Prizes,
    SectionLayout,
    Landing,
    Lookback,
    HaxploreSponsors,
    FooterN,
    Testimonials
  },
  data() {
    return {
      section: 0,
      // titles: [null, "About", "FAQ", "Lookback", "Testimonials", "Prizes"],
      devfolioKey: "haxplore",
      lookbackStats: [
        {
          name: "Prizes worth",
          value: "200,000",
          image: "assets/Lookback/lb_prize.svg"
        },
        {
          name: "Time",
          value: "24 Hours",
          image: "assets/Lookback/time.svg"
        },
        {
          name: "Participants",
          value: "100+",
          image: "assets/Lookback/lb_participant.svg"
        },
        {
          name: "Github repos",
          value: "30+",
          image: "assets/Lookback/github-repos.svg"
        },
        {
          name: "Lines of code",
          value: "100,000+",
          image: "assets/Lookback/lines-of-code.svg"
        }
      ],
      testimonials: [
        {
          name: "Shravan",
          comment:
            "Haxplore was a highly challenging and refreshing experience. \
            There was so much energy and enthusiasm in the competition, it was inspiring to discover \
            the different teams, approaches and experiments towards building solutions to a variety of \
            problems within 24hrs. It was perhaps the best hackathon I have participated till date. I would like \
            to express my gratitude to the organizers for wonderfully organizing the event.",
          image: "assets/Testimonial/shravan.jpeg"
        },
        {
          name: "Daksh Miglani",
          comment:
            "HaXplore at IIT BHU is one of the finest hackathons our country has to offer. \
            I had a great time there, the wifi was fast as well, and the mentors were really helpful. \
            All in all a great place to hack.",
          image: "assets/Testimonial/daksh.jpeg"
        },
        {
          name: "Akshay",
          comment:
            "Great team, great jury members. Waiting for Haxplore 2.0",
          image: "assets/Testimonial/akshay.jpeg"
        }
      ]
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

.link {
  margin: auto;
  width: 290px;
  height: auto;
  padding: 24px;
  border-radius: 50px;
  border: 2px solid $chartreuse;
  text-align: center;
  cursor: pointer;

  .linkText {
    color: $chartreuse;
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Viga';
      font-size: 30px;
      margin: 0;
    }
  }

  &:hover {
    box-shadow: inset 0px 0px 10px $chartreuse;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
