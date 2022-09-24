<template>
  <div :class="$style.container">
    <div :class="$style.card" @click="navigateToDetails">
      <div :class="$style.card_top">
        <div :class="$style.card__image - container">
          <img :class="$style.card__image" :src="event.icon" />
        </div>
      </div>

      <div :class="$style.card_bottom">
        <div :class="$style.card__content">
          <h1 :class="$style.card__title">{{ event.title }}</h1>
          <p>{{ event.summary }}</p>
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
      type: Object,
    },
    id: {
      require: true,
      type: Number,
    },
  },
  methods: {
    navigateToDetails() {
      this.$router.push(`/events/${this.event.name}`);
    },
  },
};
</script>

<style lang="stylus" module>
@require '~@styles/anims';

* {
  box-sizing: border-box;
  line-height: 1.2;
}


.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 64vh;
  max-width: 300px;
  background: var(--background-color);
  margin-left: 10%;
  margin-right: 10%;
}

.card_top{
  height: 50%;
  background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
  padding: 1rem 1rem 1rem 1rem;
}

.card_bottom {
  flex-grow: 1;
  background: var(--background-color);
  border-radius: 15px 15px 0px 0px;
  padding: 0.25rem 1.5rem 1rem 2rem;
  box-shadow:  0 0 2rem rgba(0,0,0,0.5);

}

.card {
  display: flex;
  flex-flow: column;
  position: relative;
  background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
  height: 60vh;
  border-radius: 10px;
  color: var(--text-color);
  box-shadow: var(--box-shadow);
  overflow: auto;

  &__image {
    margin-left: auto;
    margin-right: auto;
    display: block;
    max-height: 24vh;
    width: auto;
    opacity: 0;
    animation: ImageFadeIn 0.8s 0.3s forwards;
  }

  &__title {
    font-family: 'roboto slab';
    font-weight: 700;
    text-align: center;
    letter-spacing: 0.05em;
  }

  &__content {
    font-family: 'Quicksand';
    font-weight: 500;
    opacity: 0;
    animation: ContentFadeIn 0.8s 0.3s forwards;
  }

}
</style>
