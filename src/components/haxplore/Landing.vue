<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <ResponsiveTwoColumnLayout :isRightAbove="false" @init="initLanding">
      <div :class="$style.heroImage" slot="left">
        <div :class="$style.logo">
          <div class="absolute-center" :class="$style.preloader">
            <div :class="[$style.circle, $style.circle1]"></div>
            <div :class="[$style.circle, $style.circle2]"></div>
            <div :class="[$style.circle, $style.circle3]"></div>
          </div>
        </div>
      </div>
      <div :class="$style.heroText" class="absolute-center" slot="right">
        <span :class="$style.haxplore">
          <img src="@assets/haxplore/hax_white.svg" v-if="$store.getters.currentTheme === 'dark'" />
          <img src="@assets/haxplore/hax.svg" v-else />
        </span>
        <span :class="$style.tagline" ref="tagline"></span>
        <br />
        <br />
        <span :class="$style.venue">
          <span :id="$style.loc">
            <i class="fas fa-university"></i> IIT (BHU), Varanasi <br>
            <i class="fas fa-calendar" aria-hidden="true"></i> March 27 - 28, 2021
          </span>
        </span>
        <DevfolioButton />
        <DiscordButton />
      </div>
    </ResponsiveTwoColumnLayout>
  </div>
</template>

<script>
import { TypingAnim } from "@js/utils";
const Countdown = () => import("@components/Countdown");
const DevfolioButton = () => import("@components/haxplore/DevfolioButton");
const DiscordButton = () => import("@components/haxplore/DiscordButton");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    Countdown,
    DevfolioButton,
    DiscordButton,
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      hackathonStart: new Date(2019, 8, 23),
      isTyped: false
    };
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
            ease: Power1.easeIn
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
            ease: Power1.easeOut
          },
          0.2
        ),
        "-=0.4"
      );
    },
    initLanding() {
      this.initTypingAnimation();
      this.initCircleAnimation();
    }
  }
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
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
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
        background-color: $waterloo;
        width: calc((var(--hero-dia) / 1.3));
        height: calc((var(--hero-dia) / 1.3));
        margin-top: calc((var(--hero-dia) / -2.6));
        margin-left: calc((var(--hero-dia) / -2.6));
      }

      .circle2 {
        background-color: var(--background-color);
        width: calc((var(--hero-dia) / 1.6));
        height: calc((var(--hero-dia) / 1.6));
        margin-top: calc((var(--hero-dia) / -3.2));
        margin-left: calc((var(--hero-dia) / -3.2));
      }

      .circle3 {
        background-color: $waterloo;
        background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0ODUuOTUgNDg1Ljk1Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2U0NzcxODt9LmNscy0ye2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmhheHBsb3JlLWxvZ28tb3JhbmdlLWJnPC90aXRsZT48ZyBpZD0iTGF5ZXJfMiIgZGF0YS1uYW1lPSJMYXllciAyIj48ZyBpZD0iTGF5ZXJfMS0yIiBkYXRhLW5hbWU9IkxheWVyIDEiPjxjaXJjbGUgY2xhc3M9ImNscy0xIiBjeD0iMjQyLjk4IiBjeT0iMjQyLjk4IiByPSIyNDIuOTgiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMzc2LjI5IDM3Mi44OSAzNjcuNDQgMzgwLjY3IDM2Ny40NCAxMDQuNjIgMzc2LjI5IDExMi40MSAzNzYuMjkgMzcyLjg5Ii8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzY2LjA5LDM4My42N3YtMjgybDExLjU1LDEwLjE2VjM3My41Wm0yLjcxLTI3Ni4wNlYzNzcuNjhsNi4xNC01LjRWMTEzWiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMDkuNjYgMzczLjU0IDExOC41MSAzODEuMzMgMTE4LjUxIDEwNS4yOCAxMDkuNjYgMTEzLjA2IDEwOS42NiAzNzMuNTQiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xMTkuODYsMzg0LjMybC0xMS41NS0xMC4xN1YxMTIuNDVsMTEuNTUtMTAuMTdaTTExMSwzNzIuOTNsNi4xNCw1LjQxVjEwOC4yN2wtNi4xNCw1LjRaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMTc3LjM4LDE3OC4yLDExNiwxMTYuNzZsLS43NSwxMS43Nyw1Ni4yNiw1Ni4yNlExNzQuMjcsMTgxLjM2LDE3Ny4zOCwxNzguMloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xNzEuNTEsMTg1Ljc5bC01Ny01NywuODctMTMuNTYsNjMsNjMtLjQ3LjQ4Yy0yLjA2LDIuMDctNCw0LjI3LTUuODksNi41NFptLTU1LjYyLTU3LjUyLDU1LjUyLDU1LjUxYzEuNi0xLjkyLDMuMjgtMy43OSw1LTUuNThsLTU5LjktNTkuOVoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zMTMuNiwxODQuODZsNTYuMzMtNTYuMzMtLjc1LTExLjc3LTYxLjUsNjEuNTFRMzEwLjgsMTgxLjQyLDMxMy42LDE4NC44NloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zMTMuNTUsMTg1Ljg3bC0uNDctLjU4Yy0xLjg1LTIuMjctMy44My00LjQ3LTUuODgtNi41NWwtLjQ3LS40OCw2My02MywuODcsMTMuNTZabS00LjkyLTcuNmMxLjc0LDEuNzksMy40MywzLjY2LDUsNS41OGw1NS41OS01NS41OC0uNjQtMTBaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMTcxLjg4LDMwMS4ybC01Ni41MSw1Ni41MS43NSwxMS43Niw2MS43My02MS43M0MxNzUuNzYsMzA1LjY2LDE3My43NiwzMDMuNDcsMTcxLjg4LDMwMS4yWiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTExNS41NCwzNzFsLS44Ny0xMy41Niw1Ny4yNS01Ny4yNi40OC41OGMxLjg2LDIuMjUsMy44Niw0LjQzLDUuOTMsNi40OWwuNDguNDctLjQ4LjQ5Wm0uNTItMTMsLjY0LDEwLDYwLjE5LTYwLjJjLTEuNzUtMS43Ny0zLjQ1LTMuNjMtNS4wNi01LjU0WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTMwNy4yMiwzMDcuNjdsNjEuOCw2MS44Ljc1LTExLjc2LTU2LjU4LTU2LjU4UTMxMC4zNiwzMDQuNTUsMzA3LjIyLDMwNy42N1oiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zNjkuNiwzNzFsLTYzLjM0LTYzLjM0LjQ4LS40N2MyLjA4LTIuMDgsNC4wNy00LjI2LDUuOTItNi41bC40OC0uNTcsNTcuMzIsNTcuMzJabS02MS40My02My4zNCw2MC4yNyw2MC4yNy42My0xMC01NS44NC01NS44NEMzMTEuNjMsMzA0LDMwOS45NCwzMDUuODksMzA4LjE3LDMwNy42N1oiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yNDIuNSwzMzkuODNhOTcuMSw5Ny4xLDAsMSwxLDk3LjEtOTcuMUE5Ny4yMSw5Ny4yMSwwLDAsMSwyNDIuNSwzMzkuODNabTAtMTgzLjM3YTg2LjI4LDg2LjI4LDAsMSwwLDg2LjI4LDg2LjI3QTg2LjM3LDg2LjM3LDAsMCwwLDI0Mi41LDE1Ni40NloiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjQyLjk3IDE4MC44MSAyNTEuNDMgMTQ3LjUgMjM0LjUyIDE0Ny41IDI0Mi45NyAxODAuODEiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjQyLjk4IDMwMi42MSAyMzQuNTIgMzM1LjkxIDI1MS40MyAzMzUuOTEgMjQyLjk4IDMwMi42MSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIzMDQuNzIgMjQyLjU1IDMzOC4wMyAyNTEuMDEgMzM4LjAzIDIzNC4xIDMwNC43MiAyNDIuNTUiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMTgyLjkyIDI0Mi41NSAxNDkuNjIgMjM0LjEgMTQ5LjYyIDI1MS4wMSAxODIuOTIgMjQyLjU1Ii8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjIyNi43MyAyMTEuNzcgMjA3LjI5IDE4Ny4zMiAxNzMuNzggMTg3LjUxIDE3My43NSAxODMuNDYgMjA5LjI0IDE4My4yNSAyMjkuOTEgMjA5LjI1IDIyNi43MyAyMTEuNzciLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjEzLjczIDIxNC41NSAyMDEuMzMgMTk4LjY0IDE4NS41NiAxOTguNTkgMTg1LjU4IDE5NC41MyAyMDMuMzEgMTk0LjU5IDIxNi45MyAyMTIuMDUgMjEzLjczIDIxNC41NSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIyMDcuOTcgMjI3LjY5IDE4NS42NSAxOTguNTMgMTYwLjAxIDE5OC41MyAxNjAuMDEgMTk0LjQ3IDE4Ny42NiAxOTQuNDcgMjExLjIgMjI1LjIzIDIwNy45NyAyMjcuNjkiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjIwOS4zNiIgY3k9IjIyNi42IiByPSI0LjIzIi8+PGNpcmNsZSBjbGFzcz0iY2xzLTIiIGN4PSIyMTQuNjYiIGN5PSIyMTIuMDMiIHI9IjQuMjMiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjIyOC42NCIgY3k9IjIxMS4xMyIgcj0iNC4yMyIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIyNzEuNTYgMzA1LjkxIDI1MC44OSAyNzkuOTEgMjU0LjA3IDI3Ny4zOCAyNzMuNTEgMzAxLjg0IDMwNy4wMiAzMDEuNjQgMzA3LjA1IDMwNS43IDI3MS41NiAzMDUuOTEiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjk1LjIyIDI5NC42MyAyNzcuNDkgMjk0LjU3IDI2My44NyAyNzcuMSAyNjcuMDcgMjc0LjYxIDI3OS40NyAyOTAuNTIgMjk1LjI0IDI5MC41NyAyOTUuMjIgMjk0LjYzIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjMyMC43OSAyOTQuNjkgMjkzLjE1IDI5NC42OSAyNjkuNiAyNjMuOTMgMjcyLjgzIDI2MS40NiAyOTUuMTUgMjkwLjYzIDMyMC43OSAyOTAuNjMgMzIwLjc5IDI5NC42OSIvPjxjaXJjbGUgY2xhc3M9ImNscy0yIiBjeD0iMjcxLjQ0IiBjeT0iMjYyLjU2IiByPSI0LjIzIi8+PGNpcmNsZSBjbGFzcz0iY2xzLTIiIGN4PSIyNjYuMTQiIGN5PSIyNzcuMTMiIHI9IjQuMjMiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjI1Mi4xNiIgY3k9IjI3OC4wMyIgcj0iNC4yMyIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTI5MS4yNiwxOTUuNjRhMy4yNywzLjI3LDAsMCwwLTQtLjVsLTU2LjEyLDMzLjEzYTMuMDUsMy4wNSwwLDAsMC0uNDkuMzhsNi4yNiw2LjI2YTEwLjYzLDEwLjYzLDAsMCwxLDE1LDE1bDYuMjcsNi4yNmEzLjA1LDMuMDUsMCwwLDAsLjM4LS40OWwzMy4xMy01Ni4xMUEzLjI3LDMuMjcsMCwwLDAsMjkxLjI2LDE5NS42NFoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xOTkuNywyOTIuNDlhNS4zLDUuMywwLDAsMS00LjU2LThsMzMuMTQtNTYuMTJhNS40LDUuNCwwLDAsMSwxLjg3LTEuODdsNTYuMTEtMzMuMTNhNS4zLDUuMywwLDAsMSw3LjI1LDcuMjZsLTMzLjEzLDU2LjFhNS4zMiw1LjMyLDAsMCwxLTEuODcsMS44N0wyMDIuNCwyOTEuNzVBNS4yOSw1LjI5LDAsMCwxLDE5OS43LDI5Mi40OVpNMjg5LDE5Ni43MmExLjIyLDEuMjIsMCwwLDAtLjYzLjE3TDIzMi4yMSwyMzBhMS4xNiwxLjE2LDAsMCwwLS40NC40NGwtMzMuMTMsNTYuMTFhMS4yNCwxLjI0LDAsMCwwLC4xOSwxLjUsMS4yNywxLjI3LDAsMCwwLDEuNS4xOWw1Ni4xMi0zMy4xM2ExLjIxLDEuMjEsMCwwLDAsLjQzLS40NEwyOTAsMTk4LjU4YTEuMjIsMS4yMiwwLDAsMC0xLjA2LTEuODZabS00NC42Miw1OC41M0ExMi42OCwxMi42OCwwLDEsMSwyNTcsMjQyLjU3LDEyLjcsMTIuNywwLDAsMSwyNDQuMzMsMjU1LjI1Wm0wLTIxLjNhOC42Miw4LjYyLDAsMSwwLDguNjIsOC42MkE4LjYzLDguNjMsMCwwLDAsMjQ0LjMzLDIzNFoiLz48L2c+PC9nPjwvc3ZnPg==');
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
