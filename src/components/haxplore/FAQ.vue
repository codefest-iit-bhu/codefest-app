<template>
  <SectionLayout title="FAQ" id="faq">
    <div :class="[$style.faqContainer, $style[$mq]]">
      <ResponsiveTwoColumnLayout>
        <div :class="$style.faqHeader" slot="left">
          <img src="@assets/haxplore/faq.svg">
          <div :class="$style.faqMessage">
            Have any more Questions?
            <br>Reach out to us at any time.
            <br>
            <br>
            <a
              href="mailto:events.codefest@iitbhu.ac.in?subject = Query&body = Message"
              :class="$style.email"
            >events.codefest@iitbhu.ac.in</a>
            <br>
            <a href="https://facebook.com/codefest" :class="$style.facebook">facebook.com/codefest</a>
            <br>
          </div>
        </div>
        <FAQ :faqItems="faq" slot="right"/>
      </ResponsiveTwoColumnLayout>
    </div>
  </SectionLayout>
</template>

<script>
const FAQ = () => import("@components/FAQ");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () => import("@components/layouts/ResponsiveTwoColumnLayout");

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
          question: "What is the eligibility criteria?",
          answer:
            "Any college student, pursuing undergraduate, post-graduate or PhD, can be a part of HaXplore."
        },
        {
          question: "How to participate?",
          answer: "Details to be released soon."
        },
        {
          question: "Is there any registration fee?",
          answer: "No, it’s absolutely free of cost."
        },
        {
          question: "What is the allowed team size?",
          answer: "Form a team, comprising of minimum 2 and maximum 3 members."
        },
        {
          question: "What will be the criteria for shortlisting?",
          answer:
            "Individual participants will not be shortlisted. Only complete teams will be considered for shortlisting. Further details to be released soon!"
        },
        {
          question: "Will travel reimbursement be provided?",
          answer: "Yes, the travel reimbursement will be provided to everyone."
        },
        {
          question: "Will food and accommodation be provided?",
          answer:
            "Full 3 meals would be provided for 2 days, Saturday and Sunday. Snacks would be provided regularly during the entire course of the hackathon. Accommodation will be provided from Friday evening to Monday morning."
        },
        {
          question: "How to reach IIT BHU?",
          answer:
            "There are three stations available in, and near Varanasi; Varanasi Junction(BSB), Manduadih Station(MUV) and Pt. Deen Dayal Upadhyaya Junction(DDU), Manduadih being the nearest. Flight and bus options are also available."
        },
        {
          question:
            "What will be expected from us to build during the hackathon?",
          answer:
            "Tracks and other details will be released soon! Stay connected to know more."
        },
        {
          question: "Are there any special prizes for girls?",
          answer:
            "Yes. In order to promote gender equality and diversity, we have a prize money of Rs.5000 for the best All-Girls team."
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
  font-size: 20px;

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
      width: 300px;
      height: 300px;

      ~/.xs ^[1..-1] {
        width: 70%;
        margin: 0 auto;
      }

      ~/.sm ^[1..-1] {
        width: 50%;
        margin: 0 auto;
        margin-bottom: 16px;
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

