<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :shouldShowSideNavigation="false" />
    <main :class="$style.wrapper">
      <SectionLayout title="What is a Referral?" id="about">
	    <p>After successfully registering for Codefest'20, you can also invite interested folks to register for the event. To do so, you have to simply share the referral link that can be found on your dashboard. Each participant has a unique referral link and each successful registration using your referral link will increment your referral count by one, which is also displayed on your dashboard.<br /><br />

	    The top ten participants with the maximum referral count are displayed on the leaderboard below. So spread the word among your peers to claim several goodies and shwags.</p>
	  </SectionLayout>
      <Leaderboard :leaderboard="leaderboard" />
    </main>
    <Footer />
  </div>
</template>

<script>
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const Leaderboard = () => import("@components/Leaderboard");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    SectionLayout,
    Leaderboard,
    Footer,
  },
  data() {
    return {
      leaderboard: [],
    };
  },
  created() {
    API.fetch("leaderboard/")
      .then(({ data }) => {
        this.leaderboard = data;
      })
      .catch((err) => {
        this.$toasted.global.error_post({
          message: err.message,
        });
      });
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

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
