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
            <stop offset="0%" :class="$style.grad_start"/>
            <stop offset="100%" :class="$style.grad_end" />
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
        <p>{{event.summary}}</p>
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


/* color scheme */
$backgroungColorLight = $mystic;

$gradStartLight = #ffedba;
$gradEndLight = #eb8c06;

$svgGradStartLight = #945803;
$svgGradEndLight = #ed9f30;

$textColorLight = black;
$titleColorLight = black;

$lineFadeOneLight = #ff0000;
$lineFadeTwoLight = #ff6200;
$lineFadeThreeLight = $mystic;

$boxshadowLight = 0 0.50rem 0.50rem rgba(0, 0, 0, 0.2), 0 0 1rem rgba(0, 0, 0, 0.2);




* {
  box-sizing: border-box;
  line-height: 1.2;
  font-family: 'Open Sans', sans-serif;
}

img {
  max-width: 100%;
  max-height: 100%;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 65vh;
  background: $backgroundColorLight;
  margin-left: 10%;
  margin-right: 10%;
}

.grad_start{
  stop-color: $svgGradStartLight;
  stop-opacity:1;
}

.grad_end {
  stop-color:$svgGradEndLight;
  stop-opacity:0.001;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  position: relative;
  background: $gradStartLight;
  background: -webkit-linear-gradient($gradStartLight, $gradEndLight);
  background:    -moz-linear-gradient($gradStartLight, $gradEndLight);
  background:         linear-gradient($gradStartLight, $gradEndLight);
  width: 500px;
  height: 60vh;
  border-radius: 10px;
  padding: 2rem;
  color: $textColorLight;
  box-shadow: $boxshadowLight;
  overflow: auto;

  &__image-container {
    margin: 0 auto;
  }

  &__line {
    opacity: 0;
    animation: LineFadeIn 0.8s 0.8s forwards ease-in;
  }

  &__image {
    opacity: 0;
    animation: ImageFadeIn 0.7s 1.4s forwards;
  }

  &__grad {
    opacity: 0;
    animation: ImageFadeIn 0.7s 1.4s forwards;
  }

  &__title {
    color: $titleColorLight;
    margin-top: 1;
    font-weight: 800;
    letter-spacing: 0.01em;
  }

  &__content {
    margin-top: 1rem;
    opacity: 0;
    animation: ContentFadeIn 0.8s 1.5s forwards;
  }

  &__svg {
    position: absolute;
    left: 0;
    top: 110px;
  }
}


</style>