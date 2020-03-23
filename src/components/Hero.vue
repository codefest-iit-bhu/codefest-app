<template>
  <header ref="header" :class="$style.hero">
    <mq-layout mq="lg+">
      <div class="absolute-center" :class="$style.title">
        <!--<h1 id="heroTitle">
        code
        <span>Fest</span>
        <sup>19</sup>
        </h1>-->
        <div :class="$style.cftitle">
          <span>
            <img src="@assets/cf19-hero-logo.svg">
          </span>
          <span :class="$style.tagline" ref="tagline"></span>
          <span :class="$style.venue">
            <span :id="$style.loc">
              <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
            </span>
            <span :id="$style.date">
              <i class="far fa-calendar-alt"></i> 23 - 25 August, 2019
            </span>
          </span>
        </div>
      </div>
      <canvas ref="rains" :class="$style.rains"></canvas>
    </mq-layout>
    <mq-layout :mq="['sm', 'xs', 'md']">
      <div class="absolute-center" :class="[$style.smallhero, $style[$mq]]">
        <div :class="$style.aws">
          <img src="assets/Sponsors/aws.png">
        </div>
        <div :class="$style.presents">
          <span>presents</span>
        </div>
        <div :class="$style.cflogo">
          <svg viewBox="0 0 335.71 293.38">
            <path
              class="cls-1"
              d="M170.18,293.38V49.4c-1.81-.58-119.63-.82-124.31-.3-.51,1.78-.76,142.54-.23,148.75,5.27.28,10.59.09,15.9.12s10.72,0,16.08,0h65c-7.7,16.54-15.36,32.66-22.92,48.77H0V.44C.08.36.13.3.19.25S.31.12.38.11A6,6,0,0,1,1.32,0Q168.24,0,335.15,0c.13,0,.26.13.56.3a12.17,12.17,0,0,1-1,1.23Q311.86,24.64,289,47.75a4.24,4.24,0,0,1-3.44,1.19H215.78c-.52,1.91-.7,45.89-.23,50.23,2.79.27,5.64.09,8.48.12s5.92,0,8.88,0h52.44c-.8.91-1.23,1.45-1.71,1.94q-21.66,21.94-43.3,43.92a5,5,0,0,1-4,1.62c-6-.09-12,0-18,0h-2.94c0,1.15,0,2.15,0,3.16q0,46.56,0,93.11a15.68,15.68,0,0,0,0,1.68,4.34,4.34,0,0,1-1.49,3.8Q194.9,268,176,287.64C174.23,289.47,172.38,291.21,170.18,293.38Z"
            ></path>
          </svg>
        </div>
        <div :class="$style.cftext">
          <span :class="$style.tagline" ref="tagline"></span>
          <p :class="$style.loc">
            <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
          </p>
          <p :class="$style.date">
            <i class="far fa-calendar-alt"></i> 23 - 25 August, 2019
          </p>
        </div>
        <div :class="$style.registerbtn">
          <router-link to="/login">
            <span :class="$style.register">Register</span>
          </router-link>
        </div>
      </div>
    </mq-layout>
  </header>
</template>

<script>
import { TypingAnim } from "@js/utils";

export default {
  methods: {
    initMatrixRain() {
      const c = this.$refs.rains;
      var ctx = c.getContext("2d");
      c.height = window.innerHeight;
      c.width = window.innerWidth;
      var code = "01{}-+=xyz*&%$<>?/\\89".split("");
      var font_size = 25;
      var columns = (2 * c.width) / font_size;
      var drops = [];
      for (var x = 0; x < columns; x++) drops[x] = 1;
      function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.03)";
        ctx.fillRect(0, 0, c.width, c.height);
        ctx.fillStyle = "#86ff00";
        ctx.font = font_size + "px Roboto Slab";
        for (var i = 0; i < drops.length; i++) {
          var text = code[Math.floor(Math.random() * code.length)];
          ctx.fillText(text, i * font_size, drops[i] * font_size);

          if (drops[i] * font_size > c.height && Math.random() > 0.975)
            drops[i] = 0;

          drops[i]++;
        }
        requestAnimationFrame(draw);
      }
      draw();
    },
    tryMatrixRain() {
      if (["lg", "xl", "xxl"].includes(this.$mq)) {
        this.initMatrixRain();
      }
    }
  },
  mounted() {
    this.tryMatrixRain();

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
  },
  watch: {
    $mq: function() {
      setTimeout(this.tryMatrixRain.bind(this), 500);
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.hero {
  position: relative;
  background-color: $white;
  min-height: 300px;
  height: 100vh;
  max-width: 100%;
  overflow: hidden;
  padding: 10px 16px;
  color: #f1f1f1;
}

.rains {
  height: 100%;
  width: 100%;
  position: absolute;
  overflow: hidden;
  bottom: 0;
  top: 0;
}

.title {
  height: 30%;
  width: 100%;
  z-index: 2;
  margin: auto;
  text-align: center;

  .cftitle {
    background: rgba($white, 0.7);
    width: 60%;
    margin-left: 20%;
    padding-right: 5%;
    padding-left: 5%;
    padding-top: 50px;
    padding-bottom: 50px;
    border-radius: 300px;
    box-shadow: 0 0 200px 100px rgba($white, 0.6);

    .tagline {
      display: block;
      margin: 10px auto;
      height: 32px;
      font: 30px 'Ubuntu';
      font-weight: 600;
      text-align: center;
    }

    ~/.xs .tagline, ~/.sm .tagline {
      font-size: 20px;
    }

    .venue {
      font-size: 22px;

      #loc, #date {
        display: inline-block;
        padding: 4px;
      }

      #loc::after {
        content: '|';
        margin-left: 2px;

        ~/.xs ^[1..-1] {
          content: '';
          margin: unset;
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 16px;
      }
    }
  }
}

.smallhero {
  .aws {
    margin: auto;
    height: 100px;
    width: 100px;
    border-radius: 50px;
    padding: 10px;
    background: $black;

    img {
      width: 100%;
    }
  }

  .presents {
    margin: 15px auto;
    font-family: 'Ubuntu';
    font-weight: 600;
    color: $black;
    text-align: center;
  }

  .cflogo {
    width: 100%;
    margin: auto;

    svg {
      width: 350px;
      height: 300px;
      display: inline-block;

      path {
        fill: $waterloo;
        animation: svg-transform 2.5s ease-in-out infinite alternate;
      }

      ~/.sm ^[1..-1] {
        width: 280px;
        height: 240px;
      }

      ~/.xs ^[1..-1] {
        width: 210px;
        height: 180px;
      }
    }
  }

  .cftext {
    width: 100%;
    display: block;
    padding-top: 50px;

    .tagline {
      display: block;
      margin: 10px auto;
      height: 32px;
      font: 26px 'Ubuntu';
      text-align: center;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 16px;
      }
    }

    ~/.sm ^[1..-1] {
      font-size: 16px;
    }

    ~/.xs ^[1..-1] {
      font-size: 16px;
    }

    p {
      margin-bottom: 10px;
      font-family: 'Roboto Slab';
      font-weight: 600;
      text-align: center;

      ~/.md ^[1..-1] {
        margin: 0;
        display: inline-block;
      }
    }
  }

  ./md ^[1..-1] {
    padding-top: 150px;
  }
}

.registerbtn {
  text-align: center;
  padding-top: 20px;

  .register {
    margin: auto;
    margin-top: 10px;
    margin-bottom: 10px;
    height: auto;
    padding: 10px 20px;
    border-radius: 50px;
    border: 2px solid $waterloo;
    text-align: center;
    cursor: pointer;
    color: $waterloo;
    font-family: 'Roboto Slab';
    font-weight: 600;
    box-shadow: inset 0px 0px 10px $waterloo;
  }
}
</style>
