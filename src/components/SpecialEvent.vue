<template>
  <div :class="[$style.hero, $style[$mq]]">
    <!-- <div :class="$style.logoContainer">
      <router-link :to="getPath">
        <img :class="$style.logo" src="@assets/codestart/codestart-S.png" />
      </router-link>
    </div> -->
    <div :class="$style.title">
      <router-link :to="getPath">
        <h1>{{ eventName }}</h1>
      </router-link>
      <!-- <p>
          Join the CodeFest '24 team to bring out the absolute best ideas and
          implementations from some of the best minds in the country, while
          they join us for workshops, competitions, hackathons and a lot more.
        </p> -->
    </div>
    <!-- <div :class="$style.note">
      Note: People not registered on CodeFest are not eligible to receive any
      prizes.
    </div>-->
  </div>
</template>

<script>
export default {
  components: {},
  props: {
    eventName: {
      required: true,
      type: String,
    },
    event: {
      required: true,
      type: String,
    },
    id: {
      required: true,
      type: Number,
    }
  },
  computed: {
    getPath() {
      return `/events-timeline/${this.id}`
    }
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

.hero {
  position: relative;
  background-color: var(--background-color-invert);
  width: 100%;
  overflow: hidden;
  padding: 10px 16px;
  text-align: center;
  max-width: 400px;
  margin: 20px 40px;
  border-radius: 30px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 140px;

  .logoContainer {
    width: 100%;
    max-width: 300px;
    border-radius: 100%;
    margin: 20px auto 40px;
    box-shadow: var(--box-shadow), inset 8px 8px 20px $crown-of-thorns;
    background-color: $vermilion;

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
        padding: 45px;
      }
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 80%;
      margin: 20px auto;
    }
  }

  .title {
    width: 100%;
    text-align: center;

    a:hover {
      text-decoration: none;
    }

    h1 {
      font-family: 'Ubuntu';
      letter-spacing: 3px;
      $font-size: 35px;
      padding: 16px 25px;
      color: var(--text-color-inverted);
      width: 100%;
      margin: auto;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 30px;
        padding-top: 12px;
        padding: 10px;
      }
    }

    p {
      margin-top: 72px;
      font-family: 'Quicksand';
      font-weight: 500;
      $font-size: 26px;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      $font-size: 14px;

      p {
        $font-size: 20px;
      }
    }
  }
}

.note {
  font-family: 'Roboto Slab';
  font-weight: 700;
  text-align: center;
  $font-size: 24px;
}
</style>
