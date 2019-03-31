<template>
  <div :class="[$style.root, $style[$mq]]">
    <main :class="$style.wrapper">
      <SectionLayout title="FAQ" id="faq">
        <div :class="$style.faqContainer">
          <div :class="$style.faqHeader">
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
          <FAQ :class="$style.faqList" :faqItems="faq"/>
        </div>
      </SectionLayout>
    </main>
  </div>
</template>

<script>
import FAQ from "@components/FAQ";
import Footer from "@components/Footer";
import SectionLayout from "@components/layouts/SectionLayout";
export default {
  components: {
    FAQ,
    SectionLayout
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
.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 20px 20px 50px 20px;
  position: relative;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.faqContainer {
  width: 100%;
  font-family: 'ubuntu';
  font-size: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;

  .faqHeader {
    line-height: 30px;
    font-weight: bold;
    text-align: center;

    img {
      width: 300px;
      height: 300px;
    }
  }

  .faqList {
    width: 50%;
  }
}

.root.xs, .root.sm {
  .faqContainer {
    margin-top: 50px;
    width: 100%;
    flex-direction: column;
    align-items: flex-start;

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
      width: 100%;
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
