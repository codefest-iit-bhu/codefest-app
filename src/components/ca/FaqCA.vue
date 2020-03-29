<template>
  <div :class="[$style.faqContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout>
      <div :class="$style.faqHeader" slot="left">
        <img src="assets/ca/faq.svg">
      </div>
      <FAQ :faqItems="faq" slot="right"/>
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
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      faq: [
        {
          question: "Who is eligible for being a campus ambassador?",
          answer:
            "Anyone currently enrolled in any technical institute, who is \
            connected to people who might be interested in coding competitions and hackathons can be a Campus ambassador."
        },
        {
          question: "What is the responsibility of a CA",
          answer:
            "A CA's responsibility is to publicize Codefest among the students of\
             their college and act as a representative of the fest in their college."
        },
        {
          question: "How to apply for the CA programme?",
          answer:
            "Visit our facebook page/website and register as a CA by filling up the Google form available."
        },
        {
          question: "Can a CA register as a participant too?",
          answer:
            "Ofcourse! Any CA can participate in whatever event he/she wishes to, there is no such restriction."
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

