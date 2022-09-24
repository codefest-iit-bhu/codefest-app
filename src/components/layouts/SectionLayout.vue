<template>
  <div :class="$style.sectionContainer">
    <h1 :class="[$style.sectionTitle, $style[$mq], tooLong]">{{ title }}</h1>
    <hr :class="$style.sectionLine" />
    <div :style="contentStyle">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      required: true,
      type: String,
    },
    contentStyle: {
      required: false,
      type: Object,
    },
  },
  computed: {
    tooLong() {
      const title = this.$props.title;
      if (title.length > 10) {
        return this.$style.tooLong;
      }
    },
  },
};
</script>

<style module lang="stylus">
div.sectionContainer {
  margin: 36px 0;

  h1.sectionTitle {
    font-family: 'Baloo Bhaina 2';
    color: var(--heading-color);
    letter-spacing: 2px;
    $font-size: 64px;
    margin-top: 144px;
    margin-bottom: 0px;

    &.lg, &.xl, &.xxl {
      padding-top: 36px;
    }

    &.xs, &.sm, &.md {
      margin-top: 72px;
    }

    &.xs {
      $font-size: 52px;
    }

    ~/:nth-child(even) h1.sectionTitle {
      text-align: start;
    }

    ~/:nth-child(odd) h1.sectionTitle {
      text-align: end;
    }
  }

  h1.tooLong {
    &.xs {
      $font-size: 36px;
    }
  }

  hr.sectionLine {
    height: 8px;
    background-color: $waterloo;
    display: block;
    width: 70%;
    border: none;
    margin: 0px 0 48px;

    ~/:nth-child(even) hr.sectionLine {
      margin-right: 30%;
      border-radius: 10px;
      background-image: linear-gradient(to left, var(--background-color), $waterloo);
    }

    ~/:nth-child(odd) hr.sectionLine {
      margin-left: 30%;
      border-radius: 10px;
      background-image: linear-gradient(to right, var(--background-color), $waterloo);
    }
  }
}
</style>
