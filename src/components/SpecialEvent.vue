<template>
  <div :class="$style.hero">
    <div>
      <div :class="$style.logoContainer">
        <img :class="$style.logo" src="@assets/events/hackathon-special.png">
      </div>
      <div :class="[$style.title, $style[$mq]]">
        <h1>Onsite Hackathon</h1>
        <p>
          Join the Codefest '19 team to bring out the absolute best ideas and implementations from some of the best developers in the country,
          while they join us for a 24 hours long hackathon under a single roof.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  mounted() {}
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.hero {
  position: relative;
  background-color: $black;
  min-height: 300px;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  padding: 10vh 16px;
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
  width: 100%;
  margin: 30px auto 0;
  text-align: center;

  h1 {
    font-family: 'Aldo the Apache';
  }

  &.xs, &.sm {
    font-size: 14px;
  }
}
</style>
