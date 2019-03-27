<template>
  <div :class="$style.root">
    <div :class="$style.title">
      <h2>Hacksplore FAQ</h2>
    </div>
    <main :class="$style.wrapper">
      <div :class="[$style.faqList, $style[$mq]]">
      <Q v-for="(event, i) in events" :key="i" :item="event" :id="i"/>
      </div>
    </main>
  </div>
</template>

<script>
import Q from "@components/Q";
export default {
  components: {
    Q,
  },
  data() {
    return {
      events: [
        {
          question: "Aur beta ... papa ko bhule to nhi?",
          answer:
            "Baap se mazak nhi.",
          image: "assets/chevron-down.svg"
        },
        {
          question: "Capture The Flag",
          answer:
            "A platform for the aspiring hackers to get acquainted with the real computer security practices.",
          image: "assets/chevron-down.svg"
        },
      ]
    };
  }
};
</script>

<style module lang="stylus">
.wrapper {
  text-align: right;
  width: 100%;
  padding: 20px 20px 20px 20px;
  position: relative;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
  .title{

    h2{
      font-family: 'Aldo the Apache';
      font-size: 40px;
      text-align: center;
      margin-bottom: 20px;
    }
  }
}

.faqList {
  width: 50%;
  float right;

  &.xs, &.sm {
    width: 100%;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
