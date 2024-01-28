<template>
  <div :class="$style.link">
    <div :class="$style.googleFormButton" @click="openGoogleForm">Google Form</div>
  </div>
</template>

<script>
export default {
  methods: {
    openGoogleForm() {
      // Implement logic to open the Google Form link
      window.open('https://your-google-form-link', '_blank');
    },
  },
};
</script>

<style module lang="stylus">

  .link {
    margin: auto;
    margin-top: 10px;
    max-width: 312px;
    height: auto;
    padding: 10px;

    border-radius: 5px
    text-align: center;
    cursor: pointer;
    background-color: #1CAC78;
  }

  .googleFormButton {
    display: flex;
    justify-content: center;
    color: white;
}
</style>
