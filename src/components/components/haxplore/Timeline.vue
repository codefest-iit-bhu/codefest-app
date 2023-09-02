<template>
  <SectionLayout title="Timeline" id="timeline"> <!-- TODO -->
    <div :class="[$style.timelineContainer, $style[$mq]]">
      <Timeline :timeline="timeline" slot="left" />
    </div>
  </SectionLayout>
</template>

<script>
const Timeline = () => import("@components/Timeline");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    Timeline,
    SectionLayout,
    ResponsiveTwoColumnLayout,
  },
  data() {
    return {
      // TODO
      timeline: [
        {
          isMajor: true,
          start: new Date(2021, 2, 27, 12, 0),
          end: null,
          title: "",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2021, 2, 27, 12, 0),
          end: null,
          title: "Coding Phase Starts",
          summary: "",
        },

        {
          isMajor: true,
          start: new Date(2021, 2, 28, 12, 0),
          end: null,
          title: "",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2021, 2, 28, 0, 0),
          end: null,
          title: "Mid Evaluation",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2021, 2, 28, 12, 0),
          end: null,
          title: "Coding Phase Ends",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2021, 2, 28, 16, 0),
          end: null,
          title: "Presentations",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2021, 2, 28, 20, 0),
          end: null,
          title: "Conclusion and Prizes",
          summary: "",
        },
      ],
    };
  },
};
</script>

<style module lang="stylus">

.timelineContainer {
  width: 100%;
  font-family: 'Roboto Slab';
  $font-size: 20px;

  .timelineHeader {
    margin-top: 78px;

    img {
      width: 600px;
      height: 600px;

      ~/.lg ^[1..-1] {
        width: 500px;
        height: 500px;
      }

      ~/.md ^[1..-1] {
        width: 80%;
        margin-left: 10%;
        // height: 400px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 70%;
        height: 300px;
        margin-left: 15%;
      }
    }

    ~/.xs ^[1..-1] {
      margin-top: 0px;
    }
  }
}
</style>
