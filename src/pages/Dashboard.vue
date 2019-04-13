<template>
  <div :class="$style.root">Dashboard</div>
</template>

<script>
import API from "@js/api";

export default {
  created() {
    API.fetch("profile/", { token: this.$store.getters.authToken })
      .then(({ data }) => {
        if (!data.is_profile_complete) {
          alert("Not Complete!");
        }
        console.log(data);
      })
      .catch(console.log);
  }
};
</script>

<style module lang="stylus"></style>
