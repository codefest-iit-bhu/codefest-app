<template>
  <Leaderboard :leaderboard="leaderboard"/>
</template>

<script>
import API from "@js/api";

const Leaderboard = () => import("@components/Leaderboard");
export default {
  components: {
    Leaderboard
  },
  data() {
    return {
      leaderboard: []
    };
  },
  created() {
    API.fetch("leaderboard/")
      .then(({ data }) => {
        this.leaderboard = data;
      })
      .catch(err => {
        this.$toasted.global.error_post({
          message: err.message
        });
      });
  }
};
</script>