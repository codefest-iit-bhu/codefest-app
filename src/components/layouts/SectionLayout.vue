<template>
  <div :class="$style.sectionContainer">
    <h1 :class="[$style.sectionTitle, $style[$mq]]">{{ title }}</h1>
    <hr :class="$style.sectionLine">
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
      type: String
    },
    contentStyle: {
      required: false,
      type: Object
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

div.sectionContainer {
  margin: 36px 0;

  h1.sectionTitle {
    font-family: 'Aldo the Apache';
    padding: 12px 0;
    letter-spacing: 2px;
    font-size: 64px;
    margin-top: 144px;

    &.lg, &.xl, &.xxl {
      padding-top: 36px;
    }

    &.xs, &.sm, &.md {
      margin-top: 72px;
    }

    &.xs {
      font-size: 56px;
    }

    ~/:nth-child(even) h1.sectionTitle {
      text-align: start;
    }

    ~/:nth-child(odd) h1.sectionTitle {
      text-align: end;
    }
  }

  hr.sectionLine {
    height: 4px;
    background-color: $chartreuse;
    display: block;
    width: 70%;
    border: none;
    margin: 12px 0 36px;

    ~/:nth-child(even) hr.sectionLine {
      margin-right: 30%;
      background-image: linear-gradient(to left, $black, $chartreuse);
    }

    ~/:nth-child(odd) hr.sectionLine {
      margin-left: 30%;
      background-image: linear-gradient(to right, $black, $chartreuse);
    }
  }
}
</style>
