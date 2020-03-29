<template>
  <div :class="[$style.cardWrapper, $style[$mq]]">
    <div :class="cardClass">
      <div :class="$style.card__header">
        <slot name="header"></slot>
      </div>
      <div :class="$style.card__content">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    extraCardClass: {
      type: String,
      default: null,
      required: false
    }
  },
  computed: {
    cardClass() {
      return {
        [this.$style.card]: true,
        [this.extraCardClass]: !!this.extraCardClass
      };
    }
  }
};
</script>

<style module lang="stylus">
$card-large-size = 200px;
$card-small-size = 150px;

whiteCard() {
  background: $white;
  box-shadow: 2px 2px 2px $black;
  color: $black;
}

.cardWrapper {
  width: 100%;
  height: 100%;

  .card {
    whiteCard();
    width: 100%;
    height: 100%;
    margin: 0 auto;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 75%;
      height: 75%;
    }

    &__header {
      height: 60%;
      overflow: hidden;
    }

    &__content {
      height: 40%;
      overflow: hidden;
    }
  }
}
</style>
