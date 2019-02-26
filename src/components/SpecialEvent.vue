<template>
  <header :class="$style.hero">
    <div>
      <div :class="$style.logoContainer">
        <img :class="$style.logo" src="@assets/events/hackathon-special.png">
      </div>
      <br>
      <div :class="$style.title">
        <h1>Onsite Hackathon</h1>
        <br>
        <div>
          <p>
            Join the Codefest '19 team to bring out the absolute best ideas and implementations from some of the best developers in the country,
            while they join us for a 24 hours long hackathon under a single roof.
          </p>
        </div>
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
  text-align: center;
}

.logoContainer {
  width: 20%;
  border: 2px solid $chartreuse;
  min-width: 100px;
  border-radius: 100%;
  margin: 20px auto 40px;
  animation: neon-box 1.5s ease-in-out infinite alternate;
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
