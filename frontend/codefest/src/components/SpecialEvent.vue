<template>
  <header ref="header" :class="$style.hero">
    <div id="hero">
      <div :class="$style.logoContainer">
        <img :class="$style.logo" src="../assets/events/hackathon.png">
      </div>
      <br>
      <div :class="$style.title">
        <h1>Onsite Hackathon</h1>
        <br>
        <div>This a very special event of codefest 19 exclusively for vella people.</div>
      </div>
    </div>
  </header>
</template>

<script>
import Nav from "@components/Nav";

export default {
  components: {
    Nav
  },
  mounted() {}
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';
@import '../styles/anims.styl';

.hero {
  position: relative;
  background-color: $black;
  min-height: 300px;
  height: 100vh;
  max-width: 100%;
  overflow: hidden;
  padding: 10px 16px;
  color: #f1f1f1;
  text-align: center;
}

.logoContainer {
  background: $white;
  width: 20%;
  min-width: 100px;
  border-radius: 100%;
  margin: 20px auto 40px;
  animation: neon2 1.5s ease-in-out infinite alternate;
}

.logo {
  width: 100%;
}

.title {
  height: 30%;
  width: 100%;
  margin: auto;
  text-align: center;

  h1 {
    font-size: 50px;
    font-family: 'Aldo the Apache';
    font-weight: 300;
  }
}
</style>
