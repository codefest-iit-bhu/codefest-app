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
      window.open(this.form_link, '_blank');
    },
  },
  props: {
    form_link: {
      type: String
    }
  },
};
</script>

<style module lang="stylus">

  .link {
    margin: 15px auto;
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
    font-size: 25px;
}
</style>
