<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <div :class="$style.hero">
      <div :class="$style.logo">
        <img :id="$style.top" src="assets/haxplore/logo-landing.svg">
        <img :id="$style.base" src="assets/haxplore/phone-perspective.svg">
      </div>
      <span :class="$style.haxplore">
        <img src="assets/haxplore/logo-text.svg">
      </span>
      <span :class="$style.tagline" ref="tagline"></span>
      <span :class="$style.venue">
        <span :id="$style.loc">
          <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
        </span>
      </span>
      <DevfolioButton/>
      <!-- <span :class="$style.register">Registrations will be open soon.</span> -->
      <!-- <Countdown :until="hackathonStart" :class="$style.landing__countdown"/> -->
    </div>
  </div>
</template>

<script>
import { TypingAnim } from "@js/utils";
const Countdown = () => import("@components/Countdown");
const DevfolioButton = () => import("@components/haxplore/DevfolioButton");

export default {
  components: {
    Countdown,
    DevfolioButton
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
      "Init. Develop. Deploy."
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
      $font-size: 18px;
      margin-bottom: 0;
      margin-top: 6px;
      margin: auto;
    }

    ~/.xs .tagline, ~/.sm .tagline {
      $font-size: 14px;
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

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        $font-size: 16px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 14px;
      }
    }

    .logo {
      width: 800px;
      height: 500px;
      margin: 60px auto 0;

      ~/.lg ^[1..-1] {
        width: 500px;
        height: 312.5px;
        margin: 30px auto 0;

        #base {
          top: -60px;
        }
      }

      ~/.md ^[1..-1] {
        width: 480px;
        height: 300px;
        margin: 30px auto 0;

        #base {
          top: -60px;
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
