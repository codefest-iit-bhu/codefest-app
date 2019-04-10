<template>
  <div :class="[$style.testimonials, $style[$mq]]">
    <div :class="$style.testimonial" v-for="(item, i) in testimonials" :key="i">
      <div :class="$style.avatar">
        <img :src="item.image">
      </div>
      <div :class="$style.textbox">
        <div :class="$style.corner"></div>
        <div :class="$style.text">
          <h3>{{ item.name }}</h3>
          <p>{{ item.comment }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      testimonials: [
        {
          name: "Gennnady Korotkevich (Tourist)",
          comment:
            "Manthan had some good problems and it was prepared very well. \
                      I loved the idea of hosting Mathmania at Topcoder! The problems were interesting too. \
                      Perplexed had some nice problems as well. Overall I enjoyed all three events -- thanks a lot! ",
          image: "assets/Testimonial/tourist.jpeg"
        },
        {
          name: "Raj Shukla",
          comment:
            "Thanks, thanks for organizing such amazing competitions.\
                    I really enjoy spending time on Codefest hackathons.\
                    This will help in my career growth as well.\
                    I am extremely happy to get rank 1 on enigma, I never thought of this can happen.",
          image: "assets/Testimonial/rupee.png"
        },
        {
          name: "Infosec IIT R",
          comment:
            "I feel that the competition was challenging. \
              Some of the challenges were a bit tough others were easy. \
              I will definitely recommend others to take part in this CTF \
              and also encourage organizers to conduct such events more often.",
          image: "assets/Testimonial/infosec.jpeg"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

$ht = 120px;
$rd = 60px;

.testimonials {
  --item-height: $ht;
  --item-round: $rd;

  &.xs {
    --item-height: 2 * $ht;
    --item-round: $rd * 0.5;
  }

  &.sm {
    --item-height: 1.2 * $ht;
    --item-round: $rd * 0.66;
  }

  &.md, &.lg {
    --item-height: 1.5 * $ht;
  }

  .testimonial {
    width: 80%;
    margin-left: 10%;
    display: flex;
    flex-wrap: no-wrap;
    margin-bottom: 40px;
    margin-top: 40px;

    .avatar {
      order: 0;
      border-radius: var(--item-round);
      height: calc(var(--item-round) * 2);
      width: calc(var(--item-round) * 2);
      background: $white;
      padding: calc((var(--item-round) / 5));

      img {
        height: calc(var(--item-round) * 1.6);
        width: calc(var(--item-round) * 1.6);
        border-radius: 60px;
      }
    }

    .textbox {
      order: 1;
      display: flex;
      flex-flow: row;

      .corner {
        order: 2;
        min-width: var(--item-round);
        height: var(--item-round);
        background-repeat: no-repeat;
      }

      .text {
        order: 3;
        background: $chartreuse;
        padding: 15px calc(var(--item-round) * 0.68);

        h3 {
          color: $black;
          margin: 0;
          font-family: 'Roboto Slab';

          ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
            font-size: 14px;
          }
        }

        p {
          color: $black;
          font-size: 14px;

          ~/.xs ^[1..-1], ~/.sm ^[1..-1], ~/.md ^[1..-1] {
            font-size: 12px;
          }
        }
      }
    }

    ~/.xs ^[1..-1] {
      width: 95%;
      margin-left: 2.5%;
    }
  }

  .testimonial:nth-child(odd) {
    flex-flow: row;

    .textbox {
      flex-flow: row;

      .corner {
        background-image: url('@assets/Testimonial/corner-odd.svg');
      }

      .text {
        border-bottom-left-radius: var(--item-round);
        border-bottom-right-radius: calc(2 * var(--item-round));

        ~/.xs ^[1..-1], ~/.md ^[1..-1] {
          border-bottom-right-radius: var(--item-round);
          border-top-right-radius: var(--item-round);
        }
      }
    }
  }

  .testimonial:nth-child(even) {
    flex-flow: row-reverse;

    .textbox {
      flex-flow: row-reverse;
      text-align: right;

      .corner {
        background-image: url('@assets/Testimonial/corner-even.svg');
      }

      .text {
        border-bottom-right-radius: var(--item-round);
        border-bottom-left-radius: calc(2 * var(--item-round));

        ~/.xs ^[1..-1], ~/.md ^[1..-1] {
          border-bottom-left-radius: var(--item-round);
          border-top-left-radius: var(--item-round);
        }
      }
    }
  }
}
</style>
