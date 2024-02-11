<template>
  <div :class="$style.link">
    <div :class="$style.registerButton" @click="registerEvent">{{ text }}</div>
  </div>
</template>

<script>
export default {
  props: {
    eventId: {
      type: Number,
    },
    text: {
      required: true,
      type: String,
    },
    redirectLink: {
      required: false,
      type: String,
    }
  },
  methods: {
    registerEvent() {
      if(this.redirectLink){
        this.$router.push(`${this.redirectLink}`)
      }
      else{
        // Implement the registration logic here
        this.$router.push(`/dashboard/events/${this.eventId}`)
      }
    },
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
    background-color: #FF7F50;
  }

  .registerButton {
    display: flex;
    justify-content: center;
    color: white;
    font-size: 25px;
  }
</style>
