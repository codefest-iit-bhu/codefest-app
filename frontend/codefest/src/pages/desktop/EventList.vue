<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <StandardEvent v-for="(event, i) in events" :key="i" :event="event" :id="i"/>
      <div :class="$style.space"></div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import StandardEvent from "@components/StandardEvent";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    StandardEvent,
    Footer
  },
  data() {
    return {
      events: [
        {
          title: "Appathon",
          summary:
            "A challenge to blend your creativity to develop a robust mobile app.",
          image: "../assets/events/appathon.png"
        },
        {
          title: "Enigma",
          summary:
            "Solve real-life problems by letting your machine learn patterns.",
          image: "../assets/events/enigma.png"
        },
        {
          title: "Manthan",
          summary: "Dive deep in the world of data structures and algorithms.",
          image: "../assets/events/manthan.png"
        },
        {
          title: "Vista",
          summary:
            "Make machines perceive and hone your skills in Computer Vision.",
          image: "../assets/events/vista.png"
        },
        {
          title: "Perplexed",
          summary:
            "Adapt to challenging situations by delving in constrained programming.",
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
  padding: 100px 0;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
  margin-bottom: 200px;
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
