<template>
  <div :class="$style.root">
    <h1>Dashboard</h1>
    <DashboardProfile :profile="profile"></DashboardProfile>
  </div>
</template>

<script>
import API from "@js/api";
import DashboardProfile from "@components/DashboardProfile";
export default {
  components: {
    DashboardProfile
  },
  data() {
    return {
      profile: {}
    };
  },

  created() {
    API.fetch("profile/", { token: this.$store.getters.authToken })
      .then(({ data }) => {
        if (!data.is_profile_complete) {
          console.log("Not Complete!");
        }
        console.log(data);
        this.profile = data;
      })
      .catch(console.log);
  }
};
</script>

<style module lang="stylus">
.root {
  height: 100%;

  h1 {
    color: white;
  }
}
</style>
