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
              href="mailto:codefest@iitbhu.ac.in?subject = Query&body = Message"
              :class="$style.email"
            >codefest@iitbhu.ac.in</a>
            <br>
            <a href="https://facebook.com/codefest" :class="$style.facebook">facebook.com/codefest</a>
            <br>
          </div>
        </div>
        <FAQ :faqItems="faq" slot="right">
          <p
            slot="0"
          >Any college student, pursuing undergraduate, post-graduate or PhD, can be a part of HaXplore.</p>
          <p slot="1">Details to be released soon.</p>
          <p slot="2">No, it’s absolutely free of cost.</p>
          <p slot="3">Form a team, comprising of minimum 2 and maximum 3 members.</p>
          <p slot="4">
            Individual participants will not be shortlisted. Only complete teams will be considered for shortlisting.
            Further details to be released soon!
          </p>
          <!-- <div slot="5"> -->
          <p slot="5">Yes, the travel reimbursement will be provided to everyone.</p>
          <!-- <table :class="$style.travel">
              <tr>
                <td>0-200 km</td>
                <td>Rs. 500/person</td>
              </tr>
              <tr>
                <td>200-500 km</td>
                <td>Rs. 750/person</td>
              </tr>
              <tr>
                <td>500-1000 km</td>
                <td>Rs. 1000/person</td>
              </tr>
              <tr>
                <td>More than 1000 km</td>
                <td>Rs. 1500/person</td>
              </tr>
          </table>-->
          <!-- </div> -->
          <p slot="6">
            Full 3 meals would be provided for 2 days, Saturday and Sunday. Snacks would be provided regularly
            during the entire course of the hackathon. Accommodation will be provided from Friday evening to Monday morning.
          </p>
          <p slot="7">
            There are three stations available in, and near Varanasi; Varanasi Junction(BSB), Manduadih Station(MUV)
            and Pt. Deen Dayal Upadhyaya Junction(DDU), Manduadih being the nearest. Flight and bus options are also available.
          </p>
          <p slot="8">Tracks and other details will be released soon! Stay connected to know more.</p>
          <p slot="9">
            Yes. In order to promote gender equality and diversity,
            we have a prize money of Rs.5000 for the best All-Girls team.
          </p>
        </FAQ>
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
          question: "What is the eligibility criteria?",
          answer: ""
        },
        {
          question: "How to participate?",
          answer: ""
        },
        {
          question: "Is there any registration fee?",
          answer: ""
        },
        {
          question: "What is the allowed team size?",
          answer: ""
        },
        {
          question: "What will be the criteria for shortlisting?",
          answer: ""
        },
        {
          question: "Will travel reimbursement be provided?",
          answer: ""
        },
        {
          question: "Will food and accommodation be provided?",
          answer: ""
        },
        {
          question: "How to reach IIT BHU?",
          answer: ""
        },
        {
          question:
            "What will be expected from us to build during the hackathon?",
          answer: ""
        },
        {
          question: "Are there any special prizes for girls?",
          answer: ""
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

  // .travel {
  // width: 100%;

  // tr, td {
  // height: 50px;
  // text-align: center;
  // border: 1px solid $chartreuse;
  // }
  // }
  .faqMessage {
    a {
      color: $dodger-blue;
    }

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

