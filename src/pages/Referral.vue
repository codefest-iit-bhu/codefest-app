<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <Leaderboard :leaderboard="leaderboard"/>
    </main>
    <Footer/>
  </div>
</template>
<script>
import API from "@js/api";

const Footer = () => import("@components/Footer");
const AppBar = () => import("@components/Menu/AppBar");
const Leaderboard = () => import("@components/Leaderboard");
export default {
  components: {
    AppBar,
    Footer,
    Leaderboard
  },
  data() {
    return {
      leaderboard: {}
    };
  },
  created() {
    API.fetch("leaderboard/")
      .then(({ data }) => {
        console.log(data);
        this.leaderboard = data;
      })
      .catch(console.log);
  }
};
</script>

<style module lang = "stylus">
.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  padding: 50px 20px 50px 20px;
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