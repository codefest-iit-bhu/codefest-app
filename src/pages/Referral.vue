<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :shouldShowSideNavigation="true"/>
    <main :class="$style.wrapper">
      <Leaderboard :leaderboard="leaderboard"/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const Leaderboard = () => import("@components/Leaderboard");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    Leaderboard,
    Footer
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

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.root {
  height: 100%;

  .wrapper {
    width: 80%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    font: 500 18px 'Quicksand';
    padding: 100px 0;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
