<template>
  <div :class="$style.link">
    <div :class="$style.discordButton" @click="inviteToDiscord">
      <i class="fab fa-discord" :class="$style.discordLogo"></i>
      Discord Server
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    inviteToDiscord() {
      // TODO
      window.open(
        `https://discord.gg/QZBtntYH`,
        "_blank"
      );
    }
  },
  mounted() {
    this.$emit("mounted");
  }
};
</script>

<style module lang="stylus">
$discord-color = #7289da;

.link {
  margin: auto;
  margin-top: 10px;
  max-width: 312px;
  height: auto;
  padding: 10px;

  border-radius: 5px
  text-align: center;
  cursor: pointer;
  background-color: $discord-color;
}

.discordButton {
  display: flex;
  justify-content: center;
  color: white;
}

.discordLogo {
    font-size: 25px;
    margin-right: 10px;
}
</style>
