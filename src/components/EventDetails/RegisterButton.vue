<template>
  <div :class="$style.link">
    <div :class="$style.registerButton" @click="registerEvent">Register</div>
  </div>
</template>

<script>
export default {
  props: {
    eventId: {
      type: Number,
    },
    username: {
      type: String,
    }
  },
  methods: {
    registerEvent() {
      // Implement the registration logic here
      if (this.eventId == 4) {
        this.$store
        .dispatch("createEventTeam", {
          eventId: this.eventId,
          teamName: this.username,
        })
        .then(({ data }) => {
          this.$router.push(`/dashboard/events/${this.eventId}`);
        })
        .catch((err) => {
          this.$toasted.global.error_post({ message: err.message });
        });
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
