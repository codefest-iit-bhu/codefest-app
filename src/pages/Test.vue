<template>
  <div>
    <FloatingButton text="Coming soon" @click="runTest"/>
  </div>
</template>

<script>
import FloatingButton from "@components/FloatingButton";
import API from "@js/api";

export default {
  components: {
    FloatingButton
  },
  methods: {
    runTest() {
      console.log("fetching...");
      this.$store.dispatch("login", {});
    }
  }
};
</script>

<style module lang="stylus"></style>
