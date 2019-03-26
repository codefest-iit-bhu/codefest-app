<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.timeline">
        <div :class="[$style.eventContainer, $style.done]"></div>
        <div
          v-for="(event,i) in timeline"
          :class="[$style.eventContainer, isDone(i)?$style.done:'']"
          :key="i"
        >
          <div :class="$style.date">
            <span>
              <i class="fa fa-calendar-alt" aria-hidden="true"></i>
              {{event.date}}
            </span>
          </div>
          <div :class="$style.event">
            <span style="display:inline">{{event.title}}</span>
            <span style="display:inline">
              <img :src="event.image">
            </span>
          </div>
        </div>
      </div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    Footer
  },
  data() {
    return {
      timeline: [
        {
          date: "20 March",
          title: "Appathon",
          summary:
            "A challenge to blend your creativity and programming skills to develop a robust mobile app.",
          image: "../assets/events/appathon.png"
        },
        {
          date: "25 March",
          title: "Capture The Flag",
          summary:
            "A platform for the aspiring hackers to get acquainted with the real computer security practices.",
          image: "../assets/events/ctf.png"
        },
        {
          date: "26 March",
          title: "Decipher",
          summary:
            "Cryptographic challenges for those having a knack for solving puzzles and cracking codes.",
          image: "../assets/events/decipher.png"
        },
        {
          date: "27 March",
          title: "Enigma",
          summary:
            "Solve real-life problems by letting your machine learn patterns in the data for you.",
          image: "../assets/events/enigma.png"
        },
        {
          date: "28 March",
          title: "Vista",
          summary:
            "Make machines understand how we perceive and hone your skills in Computer Vision.",
          image: "../assets/events/vista.png"
        },
        {
          date: "29 March",
          title: "Manthan",
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms.",
          image: "../assets/events/manthan.png"
        },
        {
          date: "30 March",
          title: "Mathmania",
          summary:
            "Push your limits and gear up your brain by solving some challenging mathematical problems.",
          image: "../assets/events/mathamania.png"
        },
        {
          date: "2 August",
          title: "Linguipedia",
          summary:
            "Solve challenging problems in the field of Natural Language Processing.",
          image: "../assets/events/linguipedia.png"
        },
        {
          date: "2 August",
          title: "Perplexed",
          summary:
            "Adapt to challenging situations by trying your hands at constrained programming.",
          image: "../assets/events/perplexed.png"
        }
      ]
    };
  },
  methods: {
    isDone(i) {
      var eventDate = new Date(this.timeline[i].date + " 2019");
      var today = new Date();
      return eventDate <= today;
    }
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 100px 20px 50px 20px;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

.timeline {
  height: 100%;
  width: 100%;
  margin: auto;

  &:after {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    left: calc(50% - 7px);
    background-color: white;
    border: 1px solid $chartreuse;
    bottom: 30px;
    border-radius: 50%;
    z-index: -1;
  }

  .eventContainer {
    align-items: center;
    margin: 0 auto;
    padding: 0;
    position: relative;
    height: 100px;

    &:first-child {
      height: 50px;
    }

    &:before {
      content: '';
      position: absolute;
      width: 20px;
      height: 20px;
      left: calc(50% - 8px);
      background-color: white;
      border: 1px solid $chartreuse;
      top: calc(50% - 10px);
      border-radius: 50%;
      z-index: 1;
    }

    &:after {
      content: '';
      position: absolute;
      margin: auto;
      z-index: -2;
      border-right: 5px solid white;
      top: 0;
      bottom: 0;
      left: 50%;
    }

    &.done {
      &:after {
        border-color: $chartreuse;
      }

      &:before {
        background: $chartreuse;
      }
    }

    .date, .event {
      position: absolute;
      display: flex;
      flex-direction: column;
      // margin: 15px auto;
      color: black;
    }

    .date {
      left: calc(50% - 150px);
      width: 150px;
      height: 50px;
      padding: 0;
      line-height: 50px;
      background: white;
      text-align: center;
      border-radius: 5px 0 0 5px;
    }

    .event {
      border-radius: 5px;
      left: calc(50% + 20px);
      top: 25px;
      padding: 5px;
      background: $chartreuse;
      height: 80px;
      width: 200px;
      min-width: 100px;
      justify-content: right;
      font-family: 'Roboto Mono';

      img {
        width: 50px;
        height: 50px;
      }

      &:before {
        content: ' ';
        height: 0;
        position: absolute;
        top: 18px;
        width: 0;
        z-index: 1;
        left: -10px;
        border: medium solid white;
        border-width: 10px 10px 10px 0;
        border-color: transparent $chartreuse transparent transparent;
      }
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
