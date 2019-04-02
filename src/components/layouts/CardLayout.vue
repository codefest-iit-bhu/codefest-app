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
    isPrimary: {
      type: Boolean,
      default: false,
      required: false
    }
  },
  computed: {
    cardClass() {
      return this.isPrimary ? this.$style.cardLarge : this.$style.cardSmall;
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

$card-large-size = 200px;
$card-small-size = 150px;

whiteCard() {
  background: $white;
  box-shadow: 2px 2px 2px $black;
  color: $black;
}

.cardWrapper {
  .cardLarge {
    whiteCard();
    width: $card-large-size;
    height: $card-large-size;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 0.75 * $card-large-size;
      height: 0.75 * $card-large-size;
    }
  }

  .cardSmall {
    whiteCard();
    width: $card-small-size;
    height: $card-small-size;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 0.75 * $card-small-size;
      height: 0.75 * $card-small-size;
    }
  }

  .card {
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
