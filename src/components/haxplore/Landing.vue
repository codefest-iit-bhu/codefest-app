<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <div :class="$style.hero">
      <div :class="$style.logo">
        <img :id="$style.top" src="@assets/haxplore/logo-landing.svg">
        <img :id="$style.base" src="@assets/haxplore/phone-perspective.svg">
      </div>
      <span :class="$style.tagline" ref="tagline"></span>
      <span :class="$style.venue">
        <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
        <b>|</b>
        <i class="far fa-calendar-alt"></i> 23 - 25 August, 2019
      </span>
      <!-- <Countdown :until="hackathonStart" :class="$style.landing__countdown"/> -->
    </div>
    <FloatingButton text="Register"/>
  </div>
</template>

<script>
import { TypingAnim } from "@js/utils";
import Countdown from "@components/Countdown";
import FloatingButton from "@components/FloatingButton";

export default {
  components: {
    Countdown,
    FloatingButton
  },
  data() {
    return {
      hackathonStart: new Date(2019, 8, 23),
      isTyped: false
    };
  },
  mounted() {
    this.animTyping = new TypingAnim(
      this.$refs.tagline,
      "Imagine. Create. Iterate."
    );

    window.setInterval(() => {
      this.isTyped ? this.animTyping.erase() : this.animTyping.type();
      this.isTyped = !this.isTyped;
    }, 2000);
    this.animTyping.type();
    this.isTyped = true;
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.landing {
  position: relative;
  margin-top: 80px;

  .hero {
    display: flex;
    flex-flow: column;
    text-align: center;

    ~/__countdown {
      margin: 30px auto;
    }

    .tagline, .venue {
      margin: 10px auto;
      height: 32px;
      font: 26px 'Ubuntu';
    }

    ~/.xs .tagline, ~/.sm .tagline {
      font-size: 22px;
    }

    .venue {
      font-size: 22px;

      b {
        margin: 7px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 16px;
      }
    }

    .logo {
      width: 900px;
      height: 600px;
      margin: 60px auto 20px;

      ~/.lg ^[1..-1] {
        width: 800px;
        height: 528px;
      }

      ~/.md ^[1..-1] {
        width: 700px;
        height: 462px;

        #base {
          top: -70px;
        }
      }

      ~/.sm ^[1..-1] {
        width: 500px;
        height: 330px;

        #base {
          top: -50px;
        }
      }

      ~/.xs ^[1..-1] {
        width: 320px;
        height: 212px;

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
