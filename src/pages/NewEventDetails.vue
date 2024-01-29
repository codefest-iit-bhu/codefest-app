<template>
    <div :class="[$style.root, $style[$mq]]">
      <AppBar :currentPage="eventDetails.name" @scrollTop="scrollToTop" />
      <Landing :eventName="eventFromStore.title" :showRegisterButton="eventDetails.is_registration_on" :tagline="eventFromStore.tagline" :form_link="eventDetails.form_link"/>
      <main :class="$style.wrapper">
        <div v-scroll-spy="{ data: 'section' }" ref="scroller">
          <div></div>
          <About :about="eventFromStore.description"/>
          <!-- <FAQ />
          <SectionLayout title="Lookback">
            <Lookback :stats="lookbackStats" />
          </SectionLayout>
          <SectionLayout title="Testimonials">
            <Testimonials :testimonials="testimonials" />
          </SectionLayout>
          <Timeline/>
          <Prizes/>
          <HaxploreSponsors /> -->
        </div>
      </main>
      <Footer />
    </div>
  </template>
  
  <script>
  import API from "@js/api";
  import events from "@store/events";

  const AppBar = () => import("@components/Menu/AppBar");
  const Timeline = () => import("@components/EventDetails/Timeline");
  const About = () => import("@components/EventDetails/About");
  const FAQ = () => import("@components/EventDetails/FAQ");
  const Landing = () => import("@components/EventDetails/Landing");
  const Lookback = () => import("@components/Lookback");
  const Prizes = () => import("@components/EventDetails/Prizes");
  const HaxploreSponsors = () => import("@components/EventDetails/HaxploreSponsors");
  const Footer = () => import("@components/Footer");
  const SectionLayout = () => import("@components/layouts/SectionLayout");
  const Testimonials = () => import("@components/Testimonials");
  
  export default {
    components: {
      AppBar,
      About,
      FAQ,
      Timeline,
      SectionLayout,
      Landing,
      Lookback,
      Prizes,
      HaxploreSponsors,
      Footer,
      Testimonials
    },
    data() {
      return {
        eventDetails: {},
        eventFromStore: {}
      };
    },
    computed: {
      isPastLanding() {
        return this.section > 0;
      },
      // devfolioRegisterLink() {
      //   return `https://devfolio.co/external-apply/${this.devfolioKey}`;
      // },
      linkColorStyle() {
        if (this.buttonHovered) return this.$style.hoverColor;
      }
    },
    methods: {
      scrollToTop() {
        TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
      }
      // landingMounted() {
      //   let devfolioOptions = {
      //     buttonSelector: `#devfolio-apply-now`,
      //     key: this.devfolioKey,
      //   };
      //   let script = document.createElement("script");
      //   script.src = "https://apply.devfolio.co";
      //   document.body.append(script);
      //   script.onload = function() {
      //     new Devfolio(devfolioOptions);
      //   };
      // },
    },
    created() {
      API.fetch(`events/${this.$route.params.id}/`)
        .then(({data}) => {
          this.eventDetails = data;
          this.eventFromStore = events.events.filter(event => event.name === data.name)[0]
        })
        .catch(console.log)
      // this.eventName= this.$route.params.name;
      // this.showRegisterButton=true;
    }
  };
  </script>
  
  <style module lang="stylus">
  @require '~@styles/anims';
  
  .wrapper {
    width: 80%;
    margin: 0 auto;
    padding: 0px;
    padding-bottom: 50px;
    z-index: 1;
    position: relative;
    font: 500 18px 'Quicksand';
    font-kerning: auto;
  }
  
  .faqContainer {
    width: 100%;
    $font-size: 20px;
  
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
          $font-size: 13px;
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
    box-shadow: var(--box-shadow);
    border-radius: 50px 0px 50px 0px;
    text-align: center;
    cursor: pointer;
  
    .hoverColor {
      color: var(--text-color) !important;
    }
  
    .linkText {
      color: $waterloo;
      display: inline;
      text-decoration: none;
  
      h4 {
        font-family: 'Roboto Slab';
        $font-size: 30px;
        margin: 0;
      }
    }
  
    &:hover {
      box-shadow: var(--inset-box-shadow);
    }
  }
  
  @media screen and (max-width: 769px) {
    .wrapper {
      width: 90%;
    }
  }
  </style>
  