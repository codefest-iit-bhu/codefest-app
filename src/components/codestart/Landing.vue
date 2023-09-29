<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <ResponsiveTwoColumnLayout :isRightAbove="false" @init="initLanding">
      <div :class="$style.heroImage" slot="left">
        <div :class="$style.logo">
          <div class="absolute-center" :class="$style.preloader">
            <div :class="[$style.circle, $style.circle1]" :style="circleStyle"></div>
            <div :class="[$style.circle, $style.circle2]"></div>
            <div :class="[$style.circle, $style.circle3]"></div>
          </div>
        </div>
      </div>
      <div :class="$style.heroText" class="absolute-center" slot="right">
        <span :class="$style.haxplore">
          <img
            src="@assets/codestart/codestart.png"
            v-if="$store.getters.currentTheme === 'dark'"
          />
          <img src="@assets/codestart/codestart-light.png" v-else />
        </span>
        <span :class="$style.tagline" ref="tagline"></span>
        <br />
        <br />
        <span :class="$style.venue" style="margin-bottom: 40px">
          <span :id="$style.loc">
            <i class="fas fa-university"></i> IIT (BHU), Varanasi <br />
            <!-- <i class="fas fa-calendar" aria-hidden="true"></i> March 27 - 28, 2021 -->
          </span>
        </span>
        <LoginButton v-show="!showLoginStaus" />
        <DiscordButton />
      </div>
    </ResponsiveTwoColumnLayout>
  </div>
</template>

<script>
import { TypingAnim } from "@js/utils";
import LoginButton from "./LoginButton.vue";
const Countdown = () => import("@components/Countdown");
const DiscordButton = () => import("@components/codestart/DiscordButton");

const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    Countdown,
    DiscordButton,
    LoginButton,
    ResponsiveTwoColumnLayout,
    LoginButton,
  },
  data() {
    return {
      hackathonStart: new Date(2019, 8, 23),
      isTyped: false,
    };
  },
  computed: {
    showLoginStaus() {
      return this.$store.getters.isLoggedIn;
    },
    circleStyle() {
      var theme = localStorage.getItem('theme');
      if(theme =='light') {
        return {
          'background-color': '#00a100'
        }
      }
    }
  },
  methods: {
    initTypingAnimation() {
      const elem = this.$refs.tagline;
      this.animTyping = new TypingAnim(elem, "Init. Develop. Deploy.");

      window.setInterval(() => {
        this.isTyped ? this.animTyping.erase() : this.animTyping.type();
        this.isTyped = !this.isTyped;
      }, 2000);
      this.animTyping.type();
      this.isTyped = true;
    },
    initCircleAnimation() {
      var $circles = document.getElementsByClassName(this.$style.circle);
      var tl = new TimelineMax();
      TweenMax.set($circles, { scale: 0 });
      var x = $circles;
      var z = [x[0], x[1]];
      tl.insert(
        TweenMax.staggerTo(
          x,
          1,
          {
            opacity: 1,
            scale: 1,
            ease: Power1.easeIn,
          },
          0.2
        )
      );
      tl.insert(
        TweenMax.staggerTo(
          z,
          0.5,
          {
            scale: 1.2,
            boxShadow: "0 25px 25px rgba(0, 0, 0, 0.4)",
            repeat: -1,
            yoyo: true,
            ease: Power1.easeOut,
          },
          0.2
        ),
        "-=0.4"
      );
    },
    initLanding() {
      this.initTypingAnimation();
      this.initCircleAnimation();
    },
  },
};
</script>

<style module lang="stylus">
$ht = 100vh;
$wd = 100vw;

.landing {
  position: relative;
  height: 100vh;
  padding-bottom: 50px;

  .heroImage {
    --hero-ht: $ht;
    --hero-wd: $wd;
    --hero-dia: $wd * 0.3;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      --hero-dia: $wd * 0.8;
    }

    ~/.md ^[1..-1] {
      --hero-dia: $wd * 0.6;
    }

    ~/.lg ^[1..-1], ~/.xl ^[1..-1] {
      --hero-dia: $wd * 0.4;
    }
  }

  .heroImage {
    .preloader {
      .circle {
        border-radius: var(--hero-dia);
        position: absolute;
        left: calc(var(--hero-wd) * -0.25);
        opacity: 0;

        ~/.sm ^[1..-1], ~/.xs ^[1..-1] {
          left: 0;
          top: calc(var(--hero-ht) * -0.15);
        }

        ~/.md ^[1..-1] {
          left: 0;
          top: calc(var(--hero-wd) * -0.2);
        }
      }

      .circle1 {
        background-color: #66ff66;
        filter: blur(50px);
        width: calc((var(--hero-dia) / 1.3));
        height: calc((var(--hero-dia) / 1.3));
        margin-top: calc((var(--hero-dia) / -2.6));
        margin-left: calc((var(--hero-dia) / -2.6));
      }

      .circle2 {
        background-color: #222;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        width: calc((var(--hero-dia) / 1.6));
        height: calc((var(--hero-dia) / 1.6));
        margin-top: calc((var(--hero-dia) / -3.2));
        margin-left: calc((var(--hero-dia) / -3.2));
      }

      .circle3 > svg {
        -webkit-filter: invert(.75); /* safari 6.0 - 9.0 */
                  filter: invert(.75);
      }
      .circle3 {
        background-color: #222;
        background-image: url('../../assets/codestart/codestart-S.png');
        background-size: calc((var(--hero-dia) / 2.5)) calc((var(--hero-dia) / 2.5));
        background-position: center;
        background-repeat: no-repeat;
        width: calc((var(--hero-dia) / 2));
        height: calc((var(--hero-dia) / 2));
        margin-top: calc((var(--hero-dia) / -4));
        margin-left: calc((var(--hero-dia) / -4));
      }
    }

    ~/__countdown {
      margin: 30px auto;
    }
  }

  .heroText {
    --hero-ht: $ht;
    --hero-wd: $wd;
    --hero-dia: $wd * 0.3;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      --hero-dia: $wd * 0.8;
    }

    ~/.md ^[1..-1] {
      --hero-dia: $wd * 0.6;
    }

    ~/.lg ^[1..-1], ~/.xl ^[1..-1] {
      --hero-dia: $wd * 0.4;
    }
  }

  .heroText {
    left: calc(var(--hero-wd) * 0.7);

    ~/.sm ^[1..-1], ~/.xs ^[1..-1] {
      left: calc(var(--hero-wd) * 0.5);
      top: calc(var(--hero-ht) * 0.75);
    }

    ~/.md ^[1..-1] {
      left: calc(var(--hero-wd) * 0.5);
      top: calc(var(--hero-ht) * 0.75);
    }

    justify-content: center;
    text-align: center;
  }

  .heroText {
    .haxplore {
      display: inline-block;

      img {
        width: calc(var(--hero-wd) * 0.3);

      }

      ~/.xs ^[1..-1] img {
        width: calc(var(--hero-wd) * 0.7);
      }

      ~/.sm ^[1..-1] img {
        width: calc(var(--hero-wd) * 0.7);
      }

      ~/.md ^[1..-1] img {
        width: calc(var(--hero-wd) * 0.5);
      }
    }

    .tagline, .venue {
      display: inline-block;
      width: calc(var(--hero-wd) * 0.3);
      margin: 0 auto;
      height: 32px;
      font: 32px 'Quicksand';
      font-weight: 700;
      text-align: center;
    }

    ~/.lg .tagline {
      $font-size: 18px;
      margin-bottom: 0;
      margin-top: 6px;
      margin: auto;
      width: calc(var(--hero-wd) * 0.3);
    }

    ~/.md .tagline {
      $font-size: 18px;
      margin-bottom: 0;
      margin-top: 6px;
      margin: auto;
      width: calc(var(--hero-wd) * 0.5);
    }

    ~/.xs .tagline, ~/.sm .tagline {
      $font-size: 14px;
      width: calc(var(--hero-wd) * 0.7);
    }

    .register {
      margin: auto;
      margin-top: 10px;
      margin-bottom: 10px;
      height: auto;
      padding: 10px 20px;
      border-radius: 50px;
      border: 2px solid $chartreuse;
      text-align: center;
      cursor: pointer;
      color: $chartreuse;
      font-family: 'Roboto Slab';
      font-weight: 600;
      box-shadow: inset 0px 0px 10px $chartreuse;
    }

    .venue {
      $font-size: 22px;

      #loc, #date {
        display: inline-block;
        padding: 4px;
      }

      #loc::after {
        // content: '|';
        // margin-left: 2px;
        ~/.xs ^[1..-1] {
          content: '';
          margin: unset;
        }
      }

      ~/.md ^[1..-1] {
        $font-size: 16px;
        width: calc(var(--hero-wd) * 0.5);
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 14px;
        width: calc(var(--hero-wd) * 0.7);
      }
    }

    .logo {
      width: 800px;
      height: 500px;
      margin: 150px auto 0;
      position: relative;

      ~/.lg ^[1..-1] {
        width: 500px;
        height: 400px;
        margin: 100px auto 0;

        #base {
          top: -60px;
        }
      }

      ~/.md ^[1..-1] {
        width: 480px;
        height: 350px;
        margin: 100px auto 0;

        #base {
          top: -60px;
        }
      }

      ~/.sm ^[1..-1] {
        width: 500px;
        height: 350px;

        #base {
          top: -50px;
        }
      }

      ~/.xs ^[1..-1] {
        width: 320px;
        height: 350px;

        #base {
          top: -20px;
        }
      }

      #top {
        width: 60%;
        height: 60%;
        z-index: 3;
      }

      #base {
        width: 100%;
        position: relative;
        z-index: 1;
        top: -100px;
      }
    }
  }
}
</style>
