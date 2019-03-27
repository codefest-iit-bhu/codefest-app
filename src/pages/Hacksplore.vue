<template>
  <div :class="$style.root">
    <div :class="$style.title">
      <h2>Hacksplore</h2>
    </div>
    <main :class="$style.wrapper">
      <FAQ/>
    </main>
  </div>
</template>

<script>
import FAQ from "@components/FAQ";
import Footer from "@components/Footer";
export default {
  components: {
    FAQ,
  },
  data() {
    return {
      events: [

      ]
    };
  }
};
</script>

<style module lang="stylus">
.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 20px 20px 50px 20px;
  position: relative;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
  .title{

    h2{
      font-family: 'Aldo the Apache';
      font-size: 50px;
      text-align: center;
      margin-bottom: 20px;
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
