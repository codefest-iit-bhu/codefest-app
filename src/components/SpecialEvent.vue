<template>
  <div :class="[$style.hero, $style[$mq]]">
    <div>
      <router-link to="haxplore">
        <div :class="$style.logoContainer">
          <img :class="$style.logo" src="@assets/haxplore/logo-landing.svg">
        </div>
      </router-link>
      <div :class="$style.title">
        <a>
          <router-link to="haxplore">
            <h1>HAXPLORE</h1>
          </router-link>
        </a>
        <p>
          Join the Codefest '19 team to bring out the absolute best ideas and implementations from some of the best developers in the country,
          while they join us for a 24 hours long hackathon under a single roof.
        </p>
      </div>
    </div>
    <div
      :class="$style.note"
    >Note: People not registered on CodeFest are not eligible to recieve any prizes.</div>
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

  .logoContainer {
    width: 20%;
    border: 2px solid $chartreuse;
    min-width: 100px;
    border-radius: 100%;
    margin: 20px auto 40px;
    animation: neon-box 1.5s ease-in-out infinite alternate;

    .logo {
      width: 90%;
      height: 90%;

      ~/.xxl ^[1..-1] {
        padding: 80px;
      }

      ~/.xl ^[1..-1] {
        padding: 35px;
      }

      ~/.lg ^[1..-1] {
        padding: 30px;
      }

      ~/.md ^[1..-1] {
        padding: 20px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        padding: 15px;
      }
    }
  }

  .title {
    width: 100%;
    margin: 30px auto 0;
    text-align: center;

    a:hover {
      text-decoration: none;
    }

    h1 {
      font-family: 'Aldo the Apache';
      letter-spacing: 3px;
      font-size: 54px;
      padding-top: 16px;
    }

    p {
      font-family: 'Quicksand';
      font-weight: 500;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      font-size: 14px;
    }
  }
}

.note {
  font-family: 'Quicksand';
  font-weight: 500;
  text-align: center;
  padding-bottom: 10px;
}
</style>
