<template>
  <div :class="[$style.points , $style[$mq]]">
    <div :class="$style.link">
      <h4>Coming Soon</h4>
    </div>
  </div>
</template>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.points {
  margin: 50px auto;

  .link {
    margin: 0 auto 60px;
    width: 290px;
    height: auto;
    padding: 25px;
    border-radius: 50px;
    box-shadow: inset 0px 0px 20px $chartreuse;
    animation: neon-box 1.5s ease-in-out infinite alternate;
    border: 2px solid $chartreuse;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 220px;

      h4 {
        margin: 0;
        font-size: 21px;
      }
    }

    h4 {
      margin: 0;
      font-size: 30px;
      font-family: 'Aldo the Apache';
      color: $chartreuse;
      text-align: center;
    }
  }
}
</style>