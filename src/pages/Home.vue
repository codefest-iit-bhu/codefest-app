<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true" @scrollTop="scrollToTop" />
    <!-- <Hero /> -->
    <main :class="$style.wrapper">
      <!-- Introduction -->
      <SectionLayout
        title="A Byte About Us"
        :contentStyle="{ 'text-align': 'justify' }"
      >
        <Intro />
      </SectionLayout>
      <!-- Lookback at CF'18 -->
      <SectionLayout title="Lookback">
        <Lookback :stats="lookbackStats" />
      </SectionLayout>
      <SectionLayout title="Testimonials">
        <Testimonials :testimonials="testimonials" />
      </SectionLayout>
      <Sponsors />
    </main>
    <Footer />
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
    Testimonials,
  },
  data() {
    return {
      lookbackStats: [
        {
          name: "Prize Money",
          value: "650,000",
          image: "assets/Lookback/lb_prize.svg",
        },
        {
          name: "Countries",
          value: "104",
          image: "assets/Lookback/lb_countries.svg",
        },
        {
          name: "Participants",
          value: "29,800",
          image: "assets/Lookback/lb_participant.svg",
        },
        {
          name: "Unique Visitors",
          value: "664,300",
          image: "assets/Lookback/lb_visitor.svg",
        },
        {
          name: "Registrations",
          value: "23,000",
          image: "assets/Lookback/lb_registration.svg",
        },
      ],
      testimonials: [
        {
          name: "Gennady Korotkevich (Tourist)",
          comment:
            "Manthan had some good problems and it was prepared very well. \
                      I loved the idea of hosting Mathmania at Topcoder! The problems were interesting too. \
                      Perplexed had some nice problems as well. Overall I enjoyed all three events -- thanks a lot! ",
          image: "assets/Testimonial/tourist.jpeg",
        },
        {
          name: "Raj Shukla",
          comment:
            "Thanks, thanks for organizing such amazing competitions.\
                    I really enjoy spending time on Codefest hackathons.\
                    This will help in my career growth as well.\
                    I am extremely happy to get rank 1 on enigma, I never thought of this can happen.",
          image: "assets/Testimonial/raj-shukla.jpeg",
        },
        {
          name: "Infosec IIT R",
          comment:
            "I feel that the competition was challenging. \
              Some of the challenges were a bit tough others were easy. \
              I will definitely recommend others to take part in this CTF \
              and also encourage organizers to conduct such events more often.",
          image: "assets/Testimonial/infosec.jpeg",
        },
      ],
    };
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    },
  },
};
</script>

<style module lang="stylus">

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
