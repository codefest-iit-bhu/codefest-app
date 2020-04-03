<template>
  <div :class="$style.container">
    <div :class="$style.card" @click="navigateToDetails">
      <div :class="$style.card__image-container">
        <img
          :class="$style.card__image"
          :src="event.icon"
          alt
        />
      </div>

      <svg :class="$style.card__svg" viewBox="0 0 800 500">
        
        <defs>
          <linearGradient id="grad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#080717;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#316048;stop-opacity:0.001" />
          </linearGradient>
        </defs>
        
        <path
          :class="$style.card__grad"
          d="M 0 100 Q 50 200 100 250 Q 250 400 350 300 C 400 250 550 150 650 300 Q 750 450 800 400 L 800 500 L 0 500"
          stroke="transparent"
          fill="url(#grad)"
        />
        <path
          :class="$style.card__line"
          d="M 0 100 Q 50 200 100 250 Q 250 400 350 300 C 400 250 550 150 650 300 Q 750 450 800 400"
          stroke="pink"
          stroke-width="3"
          fill="transparent"
        />
      </svg>

      <div :class="$style.card__content">
        <h1 :class="$style.card__title">{{event.title}}</h1>
        <p>{{event.description}}</p>
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
  font-family: 'Open Sans', sans-serif;
}

img {
  max-width: 100%;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 70vh;
  background: black;
  margin-left: -25%;
  margin-right: -25%;
}

.card {
  position: relative;
  background: #316048;
  background: -webkit-linear-gradient(#316048, #0f0e2b);
  background:    -moz-linear-gradient(#316048, #0f0e2b);
  background:         linear-gradient(#316048, #0f0e2b);
  width: 500px;
  height: 65vh;
  border-radius: 10px;
  padding: 2rem;
  color: #aaa;
  box-shadow: 0 0.25rem 0.25rem rgba(0, 0, 0, 0.2), 0 0 1rem rgba(0, 0, 0, 0.2);
  overflow: auto;

  &__image-container {
    background-color: white;
    margin: -2rem -2rem 1rem -2rem;
  }

  &__line {
    opacity: 0;
    animation: LineFadeIn 0.8s 1s forwards ease-in;
  }

  &__image {
    opacity: 0;
    animation: ImageFadeIn 0.8s 1.6s forwards;
  }

  &__grad {
    opacity: 0;
    animation: ImageFadeIn 0.8s 1.6s forwards;
  }

  &__title {
    color: white;
    margin-top: 0;
    font-weight: 800;
    letter-spacing: 0.01em;
  }

  &__content {
    margin-top: -1rem;
    opacity: 0;
    animation: ContentFadeIn 0.8s 1.8s forwards;
  }

  &__svg {
    position: absolute;
    left: 0;
    top: 110px;
  }
}


</style>