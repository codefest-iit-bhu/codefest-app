<template>
  <SectionLayout title="FAQ" id="faq">
    <div :class="[$style.faqContainer, $style[$mq]]">
      <ResponsiveTwoColumnLayout>
        <div :class="$style.faqHeader" slot="left">
          <div :class="$style.faqImage">
            <div class="absolute-center" :class="$style.faqImageText">?</div>
          </div>
          <div :class="$style.faqMessage">
            Have any more Questions?
            <br />Reach out to us at any time.
            <br />
            <br />
            <a
              href="mailto:events.codefest@iitbhu.ac.in?subject = Query&body = Message"
              :class="$style.email"
              >events.codefest@iitbhu.ac.in</a
            >
            <br />
            <a href="https://facebook.com/codefest" :class="$style.facebook"
              >facebook.com/codefest</a
            >
            <br />
          </div>
        </div>
        <FAQ :faqItems="faq" slot="right" />
      </ResponsiveTwoColumnLayout>
    </div>
  </SectionLayout>
</template>

<script>
const FAQ = () => import("@components/FAQ");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    FAQ,
    SectionLayout,
    ResponsiveTwoColumnLayout,
  },
  data() {
    return {
      faq: [
        {
          question: "What is the eligibility criteria?",
          answer:
            "Any college student, pursuing undergraduate, post-graduate or PhD, can be a part of HaXplore.",
        },
        {
          question: "How to participate?",
          answer: "Details to be released soon.",
        },
        {
          question: "Is there any registration fee?",
          answer: "No, it’s absolutely free of cost.",
        },
        {
          question: "What is the allowed team size?",
          answer: "Form a team, comprising of minimum 1 and maximum 4 members.",
        },
        {
          question:
            "What will be expected from us to build during the hackathon?",
          answer:
            "Tracks and other details will be released soon! Stay connected to know more.",
        },
        {
          question: "Are there any special prizes for girls?",
          answer:
            "Yes. In order to promote gender equality and diversity, we have a prize money of Rs.5000 for the best All-Girls team.",
        },
      ],
    };
  },
};
</script>

<style module lang="stylus">
.faqContainer {
  width: 100%;
  $font-size: 20px;

  .faqHeader {
    line-height: 30px;
    font-weight: bold;
    text-align: center;
    font-family: 'Quicksand';

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      display: flex;
      flex-direction: column;
      text-align: center;
      margin-bottom: 16px;
    }

    .faqImage {
      width: 350px;
      height: 350px;
      margin: 0 auto;
      padding: 25px;
      position: relative;
      border-radius: 50%;
      box-shadow: var(--box-shadow);
      background: $waterloo;
      position: relative;

      .faqImageText {
        $font-size: 280px;
        font-weight: 700;
        color: $white;
        text-shadow: var(--inset-box-shadow);
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 250px;
        height: 250px;

        .faqImageText {
          $font-size: 200px;
        }
      }
    }
  }

  .faqMessage {
    box-shadow: var(--box-shadow);
    background: var(--background-color);
    width: 370px;
    margin: 30px auto 0;
    padding: 20px 10px;
    border-radius: 45px 0;

    .facebook, .email {
      color: $waterloo;

      &:hover {
        color: var(--text-color);
      }
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      $font-size: 13px;
      line-height: 20px;
      margin-left: 20px;
      width: 280px;
      margin: 30px auto;
    }
  }

  &.xs, &.sm {
    margin-top: 50px;
  }
}
</style>
