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
          isMajor: true,
          start: new Date(2019, 2, 28, 12, 0),
          end: new Date(2019, 2, 28, 15, 0),
          title: "Start",
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms."
        },
        {
          isMajor: false,
          start: new Date(2019, 2, 29, 12, 0),
          end: new Date(2019, 2, 29, 15, 0),
          title: "Decipher",
          summary:
            "Cryptographic challenges for those having a knack for solving puzzles and cracking codes."
        },
        {
          isMajor: false,
          start: new Date(2019, 2, 30, 12, 0),
          title: "Enigma",
          summary:
            "Solve real-life problems by letting your machine learn patterns in the data for you."
        },
        {
          isMajor: false,
          start: new Date(2019, 3, 31, 12, 0),
          end: new Date(2019, 3, 31, 15, 0),
          title: "Vista",
          summary:
            "Make machines understand how we perceive and hone your skills in Computer Vision."
        },
        {
          isMajor: true,
          start: new Date(2019, 3, 1, 12, 0),
          end: new Date(2019, 3, 1, 15, 0),
          title: "Submission",
          summary:
            "Compete with the best competitive programmers of the world in the world of data structures and algorithms."
        },
        {
          isMajor: false,
          start: new Date(2019, 3, 2, 12, 0),
          title: "Results",
          summary:
            "Push your limits and gear up your brain by solving some challenging mathematical problems."
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
  font-family: 'ubuntu';
  font-size: 20px;

  .timelineHeader {
    img {
      width: 500px;
      height: 500px;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 300px;
        height: 300px;
      }
    }
  }
}
</style>
