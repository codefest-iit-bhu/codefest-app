<template>
  <div :class="$style.referral">
    <AppBar/>
    <div style="padding:300px;">
      <center>
        <Leaderboard/>
      </center>
    </div>
    <Footer/>
  </div>
</template>
<script>
import Footer from "@components/Footer";
import AppBar from "@components/Menu/AppBar";
import Leaderboard from "@components/Leaderboard";
export default {
  components: {
    AppBar,
    Footer,
    Leaderboard
  }
};
</script>

<style module lang = "stylus">
.referral {
  text-align: center;
}
</style>