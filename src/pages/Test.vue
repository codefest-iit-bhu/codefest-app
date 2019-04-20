<template>
  <div>
    <Leaderboard></Leaderboard>
    <FloatingButton text="Coming soon" @click="runTest"/>
  </div>
</template>

<script>
const FloatingButton = () => import("@components/FloatingButton");
import API from "@js/api";
const Leaderboard = () => import("@components/Leaderboard");
export default {
  components: {
    FloatingButton,
    Leaderboard
  },
  data() {
    return {
      loading: false
    };
  },
  methods: {
    runTest() {
      console.log("fetching...");
      this.$store.dispatch("login", this.$data, {}).then(console.log);
      console.log(this.$data);
    }
  }
};
</script>

<style module lang="stylus"></style>
