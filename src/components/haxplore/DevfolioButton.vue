<template>
  <div :class="$style.link">
    <div
      class="apply-button"
      :data-hackathon-slug="devfolioKey"
      :data-button-theme="$store.getters.currentTheme"
      style="height: 44px; width: 312px"
    ></div>
  </div>
</template>

<script>
export default {
  props: {
    devfolioKey: {
      type: String,
      default: "haxplore-v2"
    }
  },
  methods: {
    injectDevfolioScript() {
      const script = document.createElement('script');
      script.src = 'https://apply.devfolio.co/v2/sdk.js';
      script.async = true;
      script.defer = true;
      document.body.appendChild(script);
    }
  },
  mounted() {
    this.$emit("mounted");
    this.injectDevfolioScript();
  }
};
</script>

<style module lang="stylus">
.link {
  margin-top: 30px;
  justify-content: center;
  text-align: center;
}
</style>
