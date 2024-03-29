<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :currentPage="eventFromStore.title" @scrollTop="scrollToTop" />
    <Landing :eventName="eventFromStore.title" :eventDate="eventFromStore.date"
      :eventLastDateRegistration="eventFromStore.last_date_reg" :showRegisterButton="eventDetails.is_registration_on"
      :isRegistered="eventDetails.team !== undefined && eventDetails.team !== null" :form_link="eventDetails.form_link"
      :eventId="eventDetails.id" />
    <main :class="$style.wrapper">
      <div v-scroll-spy="{ data: 'section' }" ref="scroller">
        <div></div>
        <!-- <Section title="About" :html="eventFromStore.description"/> -->
        <Section v-if="eventFromStore.overview" title="Overview" :html="eventFromStore.overview" />
        <Section v-if="eventFromStore.duration" title="Event Duration" :html="eventFromStore.duration" />
        <Section v-if="eventFromStore.description" title="Detailed Description" :html="eventFromStore.description" />
        <Section v-if="eventFromStore.rules" title="Rules and Regulations" :html="eventFromStore.rules" />
        <Section v-if="eventFromStore.scoring" title="Scoring" :html="eventFromStore.scoring" />
        <Section v-if="eventFromStore.howto" title="How do we register as a team?" :html="eventFromStore.howto" />
        <Section v-if="eventFromStore.submission" title="Submission Guidelines" :html="eventFromStore.submission" />
        <Section v-if="eventFromStore.contact" title="Contact" :html="eventFromStore.contact" />
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
const Section = () => import("@components/EventDetails/Section");
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
    Section,
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
      .then(({ data }) => {
        this.eventDetails = data;
        console.log(data.team);
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

  .contact{
    display: flex
    align-items: center
    span{
      margin: 0px auto
    }
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
  