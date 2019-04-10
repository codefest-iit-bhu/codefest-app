<template>
  <div :class="$style.testimonial">
    <div :class="$style.avatar">
      <img src="@assets/haxplore/prize-second.svg">
    </div>
    <div :class="$style.textbox">
      <div :class="$style.corner">
        <svg :class="$style.svgcorner">
          <path></path>
        </svg>
      </div>
      <div :class="$style.text">
        <h3>Gennady Korotokevich ( Tourist )</h3>
        <p>
          Manthan had some good problems and it was prepared very well.
          I loved the idea of hosting Mathmania at Topcoder!
          The problems were interesting too.
          Perplexed had some nice problems as well.
          Overall I enjoyed all three events -- thanks a lot!
        </p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      stats: [
        {
          name: "Gennnady Korotkevich (Tourist)",
          comment:
            "Manthan had some good problems and it was prepared very well. \
                      I loved the idea of hosting Mathmania at Topcoder! The problems were interesting too. \
                      Perplexed had some nice problems as well. Overall I enjoyed all three events -- thanks a lot! ",
          image: "assets/Lookback/rupee.png"
        },
        {
          name: "Raj Shukla",
          comment:
            "Thanks, thanks for organizing such amazing competitions.\
                    I really enjoy spending time on Codefest hackathons.\
                    This will help in my career growth as well.\
                    I am extremely happy to get rank 1 on enigma, I never thought of this can happen.",
          image: "assets/Lookback/rupee.png"
        },
        {
          name: "Infosec IIT R",
          comment:
            "I feel that the competition was challenging. \
              Some of the challenges were a bit tough others were easy. \
              I will definitely recommend others to take part in this CTF \
              and also encourage organizers to conduct such events more often.",
          image: "assets/Lookback/rupee.png"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';

$t-ht = 120px;

.testimonial {
  height: $t-ht;
  width: 100%;
  display: flex;
  flex-flow: row;
  flex-wrap: no-wrap;

  .avatar {
    order: 0;
    border-radius: ($t-ht / 2);
    height: $t-ht;
    width: $t-ht;
    flex-basis: $t-ht;
    margin-left: 20px;
    background: $white;
    padding: 5px;

    img {
      height: $t-ht-10px;
      width: $t-ht-10px;
    }
  }

  .textbox {
    order: 1;
    height: $t-ht;
    display: flex;
    flex-flow: row;

    .corner {
      order: 2;
      background: transparent;

      .svgcorner {
        viewBox: 0 0 ($t-ht / 2) $t-ht;
        width: ($t-ht / 2);
        height: $t-ht;

        // background: transparent;
        path {
          fill: $white;
          stroke: none;
          d: path('M 60, 60 A 60, 60, 0, 0, 1, 0, 120 L 60, 120 L 60, 60');
        }
      }
    }

    .text {
      order: 3;
      border-top-left-radius: ($t-ht / 2);
      border-bottom-right-radius: $t-ht;
      background: $white;
      padding: 15px ($t-ht / 2);

      h3 {
        color: $black;
        margin: 0;
        font-family: 'Roboto Slab';
      }

      p {
        color: $black;
        font-size: 14px;
      }
    }
  }
}
</style>
