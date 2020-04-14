<template>
  <SectionLayout title="Timeline" id="timeline">
    <div :class="[$style.timelineContainer, $style[$mq]]">
      <ResponsiveTwoColumnLayout :isRightAbove="true">
        <div :class="$style.timelineHeader" slot="right">
          <img src="@assets/haxplore/timeline.svg" />
        </div>
        <Timeline :timeline="timeline" slot="left" />
      </ResponsiveTwoColumnLayout>
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
      timeline: [
        {
          isMajor: true,
          start: new Date(2019, 7, 23, 12, 0),
          end: null,
          title: "",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 23, 20, 0),
          end: null,
          title: "Reporting @ Visvesvaraya Hostel",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2019, 7, 24, 12, 0),
          end: null,
          title: "",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 9, 0),
          end: null,
          title: "Breakfast @ CSE Department",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 10, 0),
          end: null,
          title: "Theme Announcement & Opening Ceremony @ LT 21",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 12, 0),
          end: null,
          title: "Lunch @ CSE Department",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 12, 45),
          end: null,
          title: "Venue Reporting @ UG Lab-I, CSE Department",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 13, 0),
          end: null,
          title: "EVENT START",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 17, 30),
          end: null,
          title: "Snacks/Supper",
          summary: "",
        },

        {
          isMajor: false,
          start: new Date(2019, 7, 24, 21, 0),
          end: null,
          title: "Dinner",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 24, 22, 0),
          end: null,
          title: "Mid-Review",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2019, 7, 25, 12, 0),
          title: "",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 2, 0),
          title: "Snacks",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 9, 0),
          title: "Breakfast",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 12, 0),
          title: "Submission Deadline",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 12, 0),
          title: "Lunch",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 17, 0),
          title: "Presentation",
          summary: "",
        },
        {
          isMajor: false,
          start: new Date(2019, 7, 25, 19, 30),
          title: "Closing Ceremony",
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
