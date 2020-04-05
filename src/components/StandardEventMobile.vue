<template>
  <div :class="$style.container">
    <div :class="$style.card" @click="navigateToDetails">

      <div :class="$style.card_top">

        <div :class="$style.card__image-container">
          <img :class="$style.card__image" :src="event.icon" />
        </div>

      </div>

      <div :class="$style.card_bottom">

        <div :class="$style.card__content">
          <h1 :class="$style.card__title">{{event.title}}</h1>
          <p>{{event.summary}}</p>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
export default {
  props: {
    event: {
      require: true,
      type: Object
    },
    id: {
      require: true,
      type: Number
    }
  },
  methods: {
    navigateToDetails() {
      this.$router.push(`/events/${this.event.name}`);
    }
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';


* {
  box-sizing: border-box;
  line-height: 1.2;
}


.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 65vh;
  max-width: 300px;
  background: $backgroundColorLight;
  margin-left: 10%;
  margin-right: 10%;
}

.card_top{
  height: 55%;
  background: $vermilion;
  padding: 1rem 1rem 1rem 1rem;
}

.card_bottom {
  height: 40%;
  background: var(--background-color);
  padding: 0rem 1.5rem 1rem 2rem;
}

.card {
  position: relative;
  background: var(--background-color);
  height: 60vh;
  border-radius: 10px;
  color: var(--text-color);
  box-shadow: var(--box-shadow);
  overflow: auto;

  &__image {
    margin-left: auto;
    margin-right: auto;
    display: block;
    max-height: 28vh;
    width: auto;
    opacity: 0;
    animation: ImageFadeIn 0.8s 0.3s forwards;
  }

  &__title {
    font-family: 'Baloo Bhaina 2';
    font-weight: 500;
    letter-spacing: 0.01em;
  }

  &__content {
    font-family: 'Quicksand';
    opacity: 0;
    animation: ContentFadeIn 0.8s 0.3s forwards;
  }

}
</style>