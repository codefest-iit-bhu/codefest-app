<template>
  <div :class="[$style.faqContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout>
      <div :class="$style.faqHeader" slot="left">
        <img src="@assets/ca/faq.svg" />
      </div>
      <FAQ :faqItems="faq" slot="right" />
    </ResponsiveTwoColumnLayout>
  </div>
</template>

<script>
const FAQ = () => import("@components/FAQ");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    FAQ,
    ResponsiveTwoColumnLayout,
  },
  data() {
    return {
      faq: [
        {
          question: "What is the role of a Campus Ambassador?",
          answer:
            "Campus Ambassadors are passionate student representatives who spark excitement for CodeFest within their colleges. They act as a bridge between the organizers and their peers, ensuring smooth participation and offering valuable insights into the event.",
        },
        {
          question: "Am I suitable to become a Campus Ambassador?",
          answer:
            "Any passionate and motivated college student from any academic background or technical skill level is eligible to apply.",
        },
        {
          question: "Can there be multiple Campus Ambassadors from a particular college?",
          answer:
            "The number of Campus Ambassadors chosen from each college may vary depending on the college size and number of applications.",
        },
        {
          question: "How much time do I need to invest once selected as a Campus Ambassador?",
          answer:
            "The time commitment will vary depending on the tasks allotted and the stage of the CodeFest cycle.",
        },
        {
          question: "Will my progress be monitored?",
          answer:
            "Yes, your dedication will shine on our leaderboard. We will track your progress based on the number of referrals you bring to CodeFest and reward the top scorers with exciting prizes, so stay motivated and keep the CodeFest spirit alive!",
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
  padding-top: 30px;

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

    img {
      width: 320px;

      ~/.xs ^[1..-1] {
        width: 200px;
        margin: 0 auto;
        margin-bottom: 16px;
      }

      ~/.sm ^[1..-1] {
        width: 260px;
        margin: 0 auto;
        margin-bottom: 16px;
      }

      ~/.md ^[1..-1] {
        width: 260px;
        margin: 20px auto;
      }

      ~/.lg ^[1..-1] {
        width: 300px;
        margin: 30px auto;
      }
    }
  }

  .faqMessage {
    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      $font-size: 13px;
      line-height: 20px;
      margin-left: 20px;
    }
  }

  &.xs, &.sm {
    margin-top: 50px;
  }
}
</style>
