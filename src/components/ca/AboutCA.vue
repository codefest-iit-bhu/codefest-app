<template>
  <div :class="[$style.aboutContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout :isRightAbove="true">
      <div :class="$style.aboutImage" slot="right">
        <img src="@assets/ca/about.svg" />
      </div>
      <div :class="$style.aboutHead" slot="left">
        <p>
          The CA program is our warm invitation to all you dynamic and enthusiastic students who are eager to represent the spirit of CodeFest’24 team in your campus. 
        </p>
        <p>
          Accompanied with the opportunity to foster innovation and build connections, are the exclusive perks, exciting goodies and well-deserved rewards.
        </p>
      </div>
    </ResponsiveTwoColumnLayout>
  </div>
</template>

<script>
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    ResponsiveTwoColumnLayout,
  },
};
</script>

<style module lang="stylus">
.aboutContainer {
  width: 100%;
  $font-size: 20px;
  padding-top: 30px;

  .aboutImage {
    text-align: center;

    img {
      width: 440px;
      margin: auto;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 240px;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        width: 300px;
      }
    }
  }

  .aboutHead {
    p {
      text-align: justify;
      line-height: 32px;
      padding: 25px 50px 0 0;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        text-align: left;
        line-height: auto;
        padding: 15px 0;
        $font-size: 18px;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        text-align: left;
        padding: 15px 0 15px 0;
        margin: 0;
      }
    }
  }
}
</style>
