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
