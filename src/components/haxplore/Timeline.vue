<template>
  <SectionLayout title="Timeline" id="timeline">
    <div :class="[$style.timelineContainer, $style[$mq]]">
      <ResponsiveTwoColumnLayout :isRightAbove="true">
        <div :class="$style.timelineHeader" slot="right">
          <img src="@assets/haxplore/timeline.svg">
        </div>
        <Timeline :timeline="timeline" slot="left"/>
      </ResponsiveTwoColumnLayout>
    </div>
  </SectionLayout>
</template>

<script>
import Timeline from "@components/Timeline";
import SectionLayout from "@components/layouts/SectionLayout";
import ResponsiveTwoColumnLayout from "@components/layouts/ResponsiveTwoColumnLayout";

export default {
  components: {
    Timeline,
    SectionLayout,
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      timeline: [
        {
          isMajor: false,
          start: new Date(2019, 7, 23, 12, 0),
          end: null,
          title: "TBA",
          summary: ""
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 24, 12, 0),
          end: null,
          title: "TBA",
          summary: ""
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 12, 0),
          title: "TBA",
          summary: ""
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';

.timelineContainer {
  width: 100%;
  font-family: 'Roboto Slab';
  font-size: 20px;

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
