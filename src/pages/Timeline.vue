<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.timeline">
          <Checkpoint v-for="(checkpointData,i) in timeline" :key="i" :checkpointData="checkpointData" />
      </div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Checkpoint from "@components/Checkpoint";
import Footer from "@components/Footer";

export default {
  components: {
    AppBar,
    Checkpoint,
    Footer
  },
  data() {
    return {
      timeline: [
        {
          major: true,
          start: new Date(2019, 2, 28, 12, 0),
          end: new Date(2019, 2, 28, 15, 0),
          title: "Start",
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms.",
          image: ""
        },
        {
          major: false,
          start: new Date(2019, 2, 29, 12, 0),
          end: new Date(2019, 2, 29, 15, 0),
          title: "Decipher",
          summary:
            "Cryptographic challenges for those having a knack for solving puzzles and cracking codes.",
          image: "../assets/events/decipher.png"
        },
        {
          major: false,
          start: new Date(2019, 2, 30, 12, 0),
          end: new Date(2019, 2, 30, 15, 0),
          title: "Enigma",
          summary:
            "Solve real-life problems by letting your machine learn patterns in the data for you.",
          image: "../assets/events/enigma.png"
        },
        {
          major: false,
          start: new Date(2019, 2, 31, 12, 0),
          end: new Date(2019, 2, 31, 15, 0),
          title: "Vista",
          summary:
            "Make machines understand how we perceive and hone your skills in Computer Vision.",
          image: "../assets/events/vista.png"
        },
        {
          major: true,
          start: new Date(2019, 3, 1, 12, 0),
          end: new Date(2019, 3, 1, 15, 0),
          title: "Submission",
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms.",
          image: "../assets/events/manthan.png"
        },
        {
          major: false,
          start: new Date(2019, 3, 2, 12, 0),
          end: null,
          title: "Results",
          summary:
            "Push your limits and gear up your brain by solving some challenging mathematical problems.",
          image: "../assets/events/mathamania.png"
        }
      ]
    };
  },
  computed: {
    
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
  position: relative;
  height: 100%;
  width: 35%;
  padding: 0 5%;
  margin-bottom: 50px;
  float: left;

}

</style>
