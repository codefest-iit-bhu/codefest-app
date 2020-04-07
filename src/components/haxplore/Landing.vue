<template>
  <div :class="[$style.landing, $style[$mq]]" id="landing">
    <!-- <div :class="$style.hero">
      <span :class="$style.register">Registrations will be open soon.</span>
      <Countdown :until="hackathonStart" :class="$style.landing__countdown"/>
    </div> -->
    <div :class="$style.hero">
      <div :class="$style.logo">
        <div :class="$style.preloader">
          <div :class="[$style.circle, $style.circle1]">
          </div>
          <div :class="[$style.circle, $style.circle2]">
          </div>
          <div :class="[$style.circle, $style.circle3]">
          </div>
        </div>
      </div>
      <!-- <span :class="$style.haxplore">
        <img src="@assets/haxplore/logo-text.svg">
      </span>
      <span :class="$style.tagline" ref="tagline"></span>
      <span :class="$style.venue">
        <span :id="$style.loc">
          <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
        </span>
      </span> -->
    </div>
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

    var $circles = document.getElementsByClassName(this.$style.circle);
    var tl = new TimelineMax();
    TweenMax.set($circles, {scale: 0});
    var x = $circles;
    var z= [x[0],x[1]]
    tl.insert(
      TweenMax.staggerTo(x, 1, {
        opacity: 1,
        scale: 1,
        ease: Power1.easeIn
      }, 0.2)
    );
    tl.insert(
    TweenMax.staggerTo(z, 0.5, {
      scale: 1.2,
      boxShadow: '0 25px 25px rgba(0, 0, 0, 0.4)',
      repeat: -1,
      yoyo: true,
      ease: Power1.easeOut
    }, 0.2), '-=0.4');
  },
  methods: {
    loaderOut() {
      console.log('Image is done loading.');
    },
    getRandomNumber() {
      return Math.floor(Math.random() * 10000);
    },
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.landing {
  position: relative;
  padding-top: 200px;

  .preloader {
    width: 100%;
    height: 100%;
    z-index: 10;
    position: absolute;

    .circle {
      border-radius: 190px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
      position: absolute;
      top: 50%;
      left: 50%;
      opacity: 0;
    }

    .circle1 {
      background-color:  	#e47718;
      width: 240px;
      height: 240px;
      margin-top: -120px;
      margin-left: -120px;
    }

    .circle2 {
      background-color: #ffffff;
      width: 170px;
      height: 170px;
      margin-top: -85px;
      margin-left: -85px;
    }

    .circle3 {
      background-color: #e47718;
      background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0ODUuOTUgNDg1Ljk1Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2U0NzcxODt9LmNscy0ye2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmhheHBsb3JlLWxvZ28tb3JhbmdlLWJnPC90aXRsZT48ZyBpZD0iTGF5ZXJfMiIgZGF0YS1uYW1lPSJMYXllciAyIj48ZyBpZD0iTGF5ZXJfMS0yIiBkYXRhLW5hbWU9IkxheWVyIDEiPjxjaXJjbGUgY2xhc3M9ImNscy0xIiBjeD0iMjQyLjk4IiBjeT0iMjQyLjk4IiByPSIyNDIuOTgiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMzc2LjI5IDM3Mi44OSAzNjcuNDQgMzgwLjY3IDM2Ny40NCAxMDQuNjIgMzc2LjI5IDExMi40MSAzNzYuMjkgMzcyLjg5Ii8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMzY2LjA5LDM4My42N3YtMjgybDExLjU1LDEwLjE2VjM3My41Wm0yLjcxLTI3Ni4wNlYzNzcuNjhsNi4xNC01LjRWMTEzWiIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxMDkuNjYgMzczLjU0IDExOC41MSAzODEuMzMgMTE4LjUxIDEwNS4yOCAxMDkuNjYgMTEzLjA2IDEwOS42NiAzNzMuNTQiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xMTkuODYsMzg0LjMybC0xMS41NS0xMC4xN1YxMTIuNDVsMTEuNTUtMTAuMTdaTTExMSwzNzIuOTNsNi4xNCw1LjQxVjEwOC4yN2wtNi4xNCw1LjRaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMTc3LjM4LDE3OC4yLDExNiwxMTYuNzZsLS43NSwxMS43Nyw1Ni4yNiw1Ni4yNlExNzQuMjcsMTgxLjM2LDE3Ny4zOCwxNzguMloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xNzEuNTEsMTg1Ljc5bC01Ny01NywuODctMTMuNTYsNjMsNjMtLjQ3LjQ4Yy0yLjA2LDIuMDctNCw0LjI3LTUuODksNi41NFptLTU1LjYyLTU3LjUyLDU1LjUyLDU1LjUxYzEuNi0xLjkyLDMuMjgtMy43OSw1LTUuNThsLTU5LjktNTkuOVoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zMTMuNiwxODQuODZsNTYuMzMtNTYuMzMtLjc1LTExLjc3LTYxLjUsNjEuNTFRMzEwLjgsMTgxLjQyLDMxMy42LDE4NC44NloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zMTMuNTUsMTg1Ljg3bC0uNDctLjU4Yy0xLjg1LTIuMjctMy44My00LjQ3LTUuODgtNi41NWwtLjQ3LS40OCw2My02MywuODcsMTMuNTZabS00LjkyLTcuNmMxLjc0LDEuNzksMy40MywzLjY2LDUsNS41OGw1NS41OS01NS41OC0uNjQtMTBaIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNMTcxLjg4LDMwMS4ybC01Ni41MSw1Ni41MS43NSwxMS43Niw2MS43My02MS43M0MxNzUuNzYsMzA1LjY2LDE3My43NiwzMDMuNDcsMTcxLjg4LDMwMS4yWiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTExNS41NCwzNzFsLS44Ny0xMy41Niw1Ny4yNS01Ny4yNi40OC41OGMxLjg2LDIuMjUsMy44Niw0LjQzLDUuOTMsNi40OWwuNDguNDctLjQ4LjQ5Wm0uNTItMTMsLjY0LDEwLDYwLjE5LTYwLjJjLTEuNzUtMS43Ny0zLjQ1LTMuNjMtNS4wNi01LjU0WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTMwNy4yMiwzMDcuNjdsNjEuOCw2MS44Ljc1LTExLjc2LTU2LjU4LTU2LjU4UTMxMC4zNiwzMDQuNTUsMzA3LjIyLDMwNy42N1oiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zNjkuNiwzNzFsLTYzLjM0LTYzLjM0LjQ4LS40N2MyLjA4LTIuMDgsNC4wNy00LjI2LDUuOTItNi41bC40OC0uNTcsNTcuMzIsNTcuMzJabS02MS40My02My4zNCw2MC4yNyw2MC4yNy42My0xMC01NS44NC01NS44NEMzMTEuNjMsMzA0LDMwOS45NCwzMDUuODksMzA4LjE3LDMwNy42N1oiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yNDIuNSwzMzkuODNhOTcuMSw5Ny4xLDAsMSwxLDk3LjEtOTcuMUE5Ny4yMSw5Ny4yMSwwLDAsMSwyNDIuNSwzMzkuODNabTAtMTgzLjM3YTg2LjI4LDg2LjI4LDAsMSwwLDg2LjI4LDg2LjI3QTg2LjM3LDg2LjM3LDAsMCwwLDI0Mi41LDE1Ni40NloiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjQyLjk3IDE4MC44MSAyNTEuNDMgMTQ3LjUgMjM0LjUyIDE0Ny41IDI0Mi45NyAxODAuODEiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjQyLjk4IDMwMi42MSAyMzQuNTIgMzM1LjkxIDI1MS40MyAzMzUuOTEgMjQyLjk4IDMwMi42MSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIzMDQuNzIgMjQyLjU1IDMzOC4wMyAyNTEuMDEgMzM4LjAzIDIzNC4xIDMwNC43MiAyNDIuNTUiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMTgyLjkyIDI0Mi41NSAxNDkuNjIgMjM0LjEgMTQ5LjYyIDI1MS4wMSAxODIuOTIgMjQyLjU1Ii8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjIyNi43MyAyMTEuNzcgMjA3LjI5IDE4Ny4zMiAxNzMuNzggMTg3LjUxIDE3My43NSAxODMuNDYgMjA5LjI0IDE4My4yNSAyMjkuOTEgMjA5LjI1IDIyNi43MyAyMTEuNzciLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjEzLjczIDIxNC41NSAyMDEuMzMgMTk4LjY0IDE4NS41NiAxOTguNTkgMTg1LjU4IDE5NC41MyAyMDMuMzEgMTk0LjU5IDIxNi45MyAyMTIuMDUgMjEzLjczIDIxNC41NSIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIyMDcuOTcgMjI3LjY5IDE4NS42NSAxOTguNTMgMTYwLjAxIDE5OC41MyAxNjAuMDEgMTk0LjQ3IDE4Ny42NiAxOTQuNDcgMjExLjIgMjI1LjIzIDIwNy45NyAyMjcuNjkiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjIwOS4zNiIgY3k9IjIyNi42IiByPSI0LjIzIi8+PGNpcmNsZSBjbGFzcz0iY2xzLTIiIGN4PSIyMTQuNjYiIGN5PSIyMTIuMDMiIHI9IjQuMjMiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjIyOC42NCIgY3k9IjIxMS4xMyIgcj0iNC4yMyIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIyNzEuNTYgMzA1LjkxIDI1MC44OSAyNzkuOTEgMjU0LjA3IDI3Ny4zOCAyNzMuNTEgMzAxLjg0IDMwNy4wMiAzMDEuNjQgMzA3LjA1IDMwNS43IDI3MS41NiAzMDUuOTEiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMjk1LjIyIDI5NC42MyAyNzcuNDkgMjk0LjU3IDI2My44NyAyNzcuMSAyNjcuMDcgMjc0LjYxIDI3OS40NyAyOTAuNTIgMjk1LjI0IDI5MC41NyAyOTUuMjIgMjk0LjYzIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9IjMyMC43OSAyOTQuNjkgMjkzLjE1IDI5NC42OSAyNjkuNiAyNjMuOTMgMjcyLjgzIDI2MS40NiAyOTUuMTUgMjkwLjYzIDMyMC43OSAyOTAuNjMgMzIwLjc5IDI5NC42OSIvPjxjaXJjbGUgY2xhc3M9ImNscy0yIiBjeD0iMjcxLjQ0IiBjeT0iMjYyLjU2IiByPSI0LjIzIi8+PGNpcmNsZSBjbGFzcz0iY2xzLTIiIGN4PSIyNjYuMTQiIGN5PSIyNzcuMTMiIHI9IjQuMjMiLz48Y2lyY2xlIGNsYXNzPSJjbHMtMiIgY3g9IjI1Mi4xNiIgY3k9IjI3OC4wMyIgcj0iNC4yMyIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTI5MS4yNiwxOTUuNjRhMy4yNywzLjI3LDAsMCwwLTQtLjVsLTU2LjEyLDMzLjEzYTMuMDUsMy4wNSwwLDAsMC0uNDkuMzhsNi4yNiw2LjI2YTEwLjYzLDEwLjYzLDAsMCwxLDE1LDE1bDYuMjcsNi4yNmEzLjA1LDMuMDUsMCwwLDAsLjM4LS40OWwzMy4xMy01Ni4xMUEzLjI3LDMuMjcsMCwwLDAsMjkxLjI2LDE5NS42NFoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0xOTkuNywyOTIuNDlhNS4zLDUuMywwLDAsMS00LjU2LThsMzMuMTQtNTYuMTJhNS40LDUuNCwwLDAsMSwxLjg3LTEuODdsNTYuMTEtMzMuMTNhNS4zLDUuMywwLDAsMSw3LjI1LDcuMjZsLTMzLjEzLDU2LjFhNS4zMiw1LjMyLDAsMCwxLTEuODcsMS44N0wyMDIuNCwyOTEuNzVBNS4yOSw1LjI5LDAsMCwxLDE5OS43LDI5Mi40OVpNMjg5LDE5Ni43MmExLjIyLDEuMjIsMCwwLDAtLjYzLjE3TDIzMi4yMSwyMzBhMS4xNiwxLjE2LDAsMCwwLS40NC40NGwtMzMuMTMsNTYuMTFhMS4yNCwxLjI0LDAsMCwwLC4xOSwxLjUsMS4yNywxLjI3LDAsMCwwLDEuNS4xOWw1Ni4xMi0zMy4xM2ExLjIxLDEuMjEsMCwwLDAsLjQzLS40NEwyOTAsMTk4LjU4YTEuMjIsMS4yMiwwLDAsMC0xLjA2LTEuODZabS00NC42Miw1OC41M0ExMi42OCwxMi42OCwwLDEsMSwyNTcsMjQyLjU3LDEyLjcsMTIuNywwLDAsMSwyNDQuMzMsMjU1LjI1Wm0wLTIxLjNhOC42Miw4LjYyLDAsMSwwLDguNjIsOC42MkE4LjYzLDguNjMsMCwwLDAsMjQ0LjMzLDIzNFoiLz48L2c+PC9nPjwvc3ZnPg==");
      width: 140px;
      height: 140px;
      // border-radius: 8px;
      margin-top: -70px;
      margin-left: -70px;
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
