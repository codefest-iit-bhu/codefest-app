<template>
  <div :class="$style.link">
    <div :class="$style.registerButton" @click="registerEvent">Register</div>
  </div>
</template>

<script>
export default {
  methods: {
    registerEvent() {
      // Implement the registration logic here
      alert('Registration logic goes here!');
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
    background-color: #FF7F50;
  }

  .registerButton {
  display: flex;
  justify-content: center;
  color: white;
}
</style>
