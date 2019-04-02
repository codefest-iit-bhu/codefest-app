<template>
  <SectionLayout title="FAQ" id="faq">
    <div :class="[$style.faqContainer, $style[$mq]]">
      <ResponsiveTwoColumnLayout>
        <div :class="$style.faqHeader" slot="left">
          <img src="assets/faq.svg">
          <div :class="$style.faqMessage">
            Have any more Questions?
            <br>Reach out to us at any time.
            <br>
            <br>codefest@iitbhu.ac.in
            <br>facebook.com/codefest
            <br>
          </div>
        </div>
        <FAQ :faqItems="faq" slot="right"/>
      </ResponsiveTwoColumnLayout>
    </div>
  </SectionLayout>
</template>

<script>
import FAQ from "@components/FAQ";
import SectionLayout from "@components/layouts/SectionLayout";
import ResponsiveTwoColumnLayout from "@components/layouts/ResponsiveTwoColumnLayout";

export default {
  components: {
    FAQ,
    SectionLayout,
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      faq: [
        {
          question: "How to reach Varanasi/IIT(BHU)?",
          answer: "Google Lanka BHU.."
        },
        {
          question: "Capture The Flag",
          answer:
            "A platform for the aspiring hackers to get acquainted with  dsfjks kx ksjn nksn ksnf so n snno real computer security practices."
        },
        {
          question: "Capture The Flag",
          answer:
            "A platform for the aspiring hackers to get acquainted with the real computer security practices."
        },
        {
          question: "How to reach Varanasi/IIT(BHU)?",
          answer: "Google Lanka BHU.."
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.faqContainer {
  width: 100%;
  font-family: 'ubuntu';
  font-size: 20px;

  .faqHeader {
    line-height: 30px;
    font-weight: bold;
    text-align: center;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      display: flex;
      flex-direction: row;
      align-items: flex-end;
    }

    img {
      width: 300px;
      height: 300px;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 100px;
        height: 100px;
      }
    }
  }

  .faqMessage {
    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      font-size: 13px;
      line-height: 20px;
      margin-left: 20px;
    }
  }

  &.xs, &.sm {
    margin-top: 50px;
  }
}
</style>

