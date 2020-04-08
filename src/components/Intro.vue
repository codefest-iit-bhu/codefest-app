<template>
  <ResponsiveTwoColumnLayout :isRightAbove="true">
    <div :class="$style.description" slot="left">
      <p>
        The
        <span
          >Department of Computer Science and Engineering, IIT (BHU)
          Varanasi</span
        >
        brings to you yet another edition of its annual coding extravaganza,
        Codefest!
        <br />
        <br />Being more diverse than ever, <span>Codefest '20</span> boasts of
        a plethora of events, ranging from competitive programming, algorithms
        and application development to upcoming trends like cryptography,
        machine learning, computer vision and cyber security.
        <br />
        <br />With problems being of varying difficulty levels, Codefest
        provides the perfect platform for fresh enthusiasts, as well as the
        experienced ones, to code together and compete for ultimate glory.
      </p>
    </div>
    <div :class="$style.video" slot="right">
      <youtube :video-id="videoId" ref="youtube" @playing="playing"></youtube>
    </div>
  </ResponsiveTwoColumnLayout>
</template>

<script>
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");
export default {
  components: {
    ResponsiveTwoColumnLayout,
  },
  data: () => {
    return {
      videoId: "QOkjxSVr5Wc",
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
  $font-size: 18px;

  span {
    font-weight: bold;
  }
}

.video {
  border-radius: 10px;
  padding: 10px;
  width: 100%;
  box-shadow: var(--box-shadow);

  & > iframe {
    border-radius: 10px;
    width: 100%;
  }
}
</style>
