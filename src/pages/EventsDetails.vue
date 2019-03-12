<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <!-- <EventDetails v-for="(event, i) in events" :key="i" :event="event" :id="i"/> -->
      <EventDetails/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import EventDetails from "@components/EventDetails";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    EventDetails,
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
            "A platform for the aspiring hackers to get acquainted with the real computer security practices.",
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
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms.",
          image: "../assets/events/manthan.png"
        },
        {
          title: "Mathmania",
          summary:
            "Push your limits and gear up your brain by solving some challenging mathematical problems.",
          image: "../assets/events/mathamania.png"
        },
        {
          title: "Linguipedia",
          summary:
            "Solve challenging problems in the field of Natural Language Processing.",
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
  padding: 100px 20px 50px 20px;
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
</style>
