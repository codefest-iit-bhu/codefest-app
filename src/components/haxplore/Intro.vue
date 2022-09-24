<template>
  <SectionLayout title="Intro" id="intro">
    <ResponsiveTwoColumnLayout :isRightAbove="true">
      <div :class="$style.description" slot="left">
        <p>
          <span>HaXplore</span> is going to be the ultimate pit-stop for
          developers. From taking care of your accomodation to providing you
          with savoury treats; food facilities and refreshments throughout the
          competition. Don't worry about your travel costs as well, we'll have
          them covered for you!
          <br />
          <br />And even if you don't win anything, fret not my friend! You'll
          go home with loads of goodies, a lot of experience and memories for a
          lifetime.
        </p>
      </div>
      <div :class="$style.video" slot="right">
        <youtube :video-id="videoId" ref="youtube" @playing="playing"></youtube>
      </div>
    </ResponsiveTwoColumnLayout>
  </SectionLayout>
</template>

<script>
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    ResponsiveTwoColumnLayout,
    SectionLayout,
  },

  data() {
    return {
      videoId: "4I0AUhHTR-g",
    };
  },
  methods: {
    playing() {
      console.log("Dekho Dekho!!");
    },
  },
  computed: {
    player() {
      return this.$refs.youtube.player;
    },
  },
};
</script>

<style module lang="stylus">
.description {
  text-align: left;
  margin: 30px 30px 0 0;

  span {
    font-weight: bold;
  }
}

.video {
  box-shadow: 0 0 10px $waterloo;
  width: 100%;

  & > iframe {
    width: 100%;
  }
}
</style>
