<template>
  <div :class="$style.root">
    <AppBar :doAnimate="true"/>
    <main :class="$style.wrapper">
      <SpecialEvent />
      <StandardEvent v-for="(event, i) in events" :key="i" :event="event" :id="i"/>
      <div :class="$style.space"></div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import SpecialEvent from "@components/SpecialEvent";
import StandardEvent from "@components/StandardEvent";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    SpecialEvent,
    StandardEvent,
    Footer
  },
  data() {
    return {
      events: [
        {
          title: "Appathon",
          summary:
            "A challenge to blend your creativity and programming skills to develop a robust mobile app.",
          image: "../assets/events/appathon.png"
        },
        {
          title: "Capture The Flag",
          summary:
            "A platform for the aspiring and existing hackers to get acquainted with the real world computer security practices.",
          image: "../assets/events/ctf.png"
        },
        {
          title: "Decipher",
          summary:
            "Cryptographic challenges for those having a knack for solving puzzles and cracking codes.",
          image: "../assets/events/decipher.png"
        },
        {
          title: "Enigma",
          summary:
            "Solve real-life problems by letting your machine learn patterns in the data for you.",
          image: "../assets/events/enigma.png"
        },
        {
          title: "Vista",
          summary:
            "Make machines understand how we perceive and hone your skills in Computer Vision.",
          image: "../assets/events/vista.png"
        },
        {
          title: "Manthan",
          summary: "Compete with some of the best competitive programmers of the world as you dive deep in the world of data structures and algorithms.",
          image: "../assets/events/manthan.png"
        },
        {
          title: "Mathamania",
          summary: "Push your limits and gear up your brain by solving some challenging mathematical problems.",
          image: "../assets/events/mathamania.png"
        },
        {
          title: "Linguipedia",
          summary: "Test your understanding of natural language processing by assessing how well your computer understands it.",
          image: "../assets/events/linguipedia.png"
        },
        {
          title: "Perplexed",
          summary:
            "Adapt to challenging situations by trying your hands at constrained programming.",
          image: "../assets/events/perplexed.png"
        }
      ]
    };
  }
};
</script>
<style module lang="stylus">
.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 120px 0;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}

.space {
  padding: 20px;
}
</style>
