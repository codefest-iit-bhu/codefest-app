<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <!-- <div :class="$style.hero">
      <span :class="$style.register">Registrations will be open soon.</span>
      <Countdown :until="hackathonStart" :class="$style.landing__countdown"/>
    </div> -->
    <!-- <ResponsiveTwoColumnLayout>
      <div :class="$style.heroImage" slot="left">
        <div :class="$style.preloader">
            <div :class="$style.circle1" ref="circle1" v-on:click="animatePreloader()"></div>
            <div :class="$style.circle2" ref="circle2"></div>
            <div :class="$style.circle3" ref="circle3"></div>
        </div>
      </div>
      <div :class="$style.heroText" slot="right">
        <span :class="$style.haxplore">
          <img src="@assets/haxplore/logo-text.svg">
        </span>
        <span :class="$style.tagline" ref="tagline"></span>
        <span :class="$style.venue">
          <span :id="$style.loc">
            <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
          </span>
        </span>
      </div>
    </ResponsiveTwoColumnLayout> -->
  </div>
</template>

<script>
import { TypingAnim } from "@js/utils";
const Countdown = () => import("@components/Countdown");
const ResponsiveTwoColumnLayout = () => import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    Countdown,
    ResponsiveTwoColumnLayout,
  },
  // props: {
  //   animateIcon: {
  //     type: Boolean,
  //     default: true,
  //     required: false    }
  // },
  data() {
    return {
      hackathonStart: new Date(2019, 8, 23),
      isTyped: false,
      animateIcon: true,
    };
  },
  mounted() {
    // this.animTyping = new TypingAnim(
    //   this.$refs.tagline,
    //   "Init. Develop. Deploy."
    // );

    // window.setInterval(() => {
    //   this.isTyped ? this.animTyping.erase() : this.animTyping.type();
    //   this.isTyped = !this.isTyped;
    // }, 2000);
    // this.animTyping.type();
    // this.isTyped = true;
  },
  methods: {
    animatePreloader() {
      console.log("Yep!");
      const { circle } = this.$refs["circle"];
      console.log(circle);
      var tl = new TimelineMax();
      var random1 = Math.floor(Math.random() * 10000);

      TweenMax.set(circle, {scale: 0});

      tl.insert(
        TweenMax.staggerTo(circle.toArray(), 1, {
          opacity: 1,
          scale: 1,
          ease: Power1.easeIn
        }, 0.2)
      );

      tl.insert(
        TweenMax.staggerTo(circle.toArray(), 0.5, {
          scale: 1.2,
          boxShadow: '0 25px 25px rgba(0, 0, 0, 0.4)',
          repeat: -1,
          yoyo: true,
          ease: Power1.easeOut
        }, 0.2), '-=0.4'
      );
    },
    animate(){
      const { circle1 } = this.$refs.circle1;
      console.log("OK!");
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.landing {
  position: relative;

  .heroImage {
    width: 100%;
    height: 100%;

    .preloader {
      width: 100%;
      height: 100%;
      padding: 300px 250px;
    
      .circle1, .circle2, .circle3 {
        border-radius: 500px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        margin: 0 auto;
      }

      .circle1 {
        background-color: #7752d5;
        width:500px;
        height: 500px;
        padding: 40px;
      }

      .circle2 {
        background-color: #8362d9;
        width: 420px;
        height: 420px;
        padding: 20px;
      }

      .circle3 {
        background-color: #9f88d6;
        width: 380px;
        height: 380px;
      }
    }
  }

  .heroText {
        .haxplore {
      margin: 10px auto 20px;

      img {
        width: 200px;
      }

      ~/.xs ^[1..-1] img {
        width: 150px;
      }
    }

    .tagline, .venue {
      margin: 10px auto;
      height: 32px;
      font: 24px 'Ubuntu';
      text-align: center;
    }

    ~/.lg .tagline, ~/.md .tagline {
      font-size: 18px;
      margin-bottom: 0;
      margin-top: 6px;
      margin: auto;
    }

    ~/.xs .tagline, ~/.sm .tagline {
      font-size: 14px;
    }
  }
}
</style>
