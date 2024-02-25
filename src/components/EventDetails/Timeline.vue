<template>
  <div>
    <h1 :class="[$style.sectionTitle, $style[$mq], tooLong]">Timeline</h1>
    <div :class="[$style.timelineContainer, $style[$mq]]">
      <Timeline :timeline="timeline" slot="left" />
    </div>
  </div>
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
          start: new Date(2024, 1, 16, 12, 0),
          end: null,
          title: "Last Date of Registration - CTF",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 1, 17, 12, 0),
          end: null,
          title: "Event Starts - CTF",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 20, 12, 0),
          end: null,
          title: "Last Date of Registration - Vista",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 24, 12, 0),
          end: null,
          title: "Event Starts - Vista",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 25, 12, 0),
          end: null,
          title: "Last Date of Registration - HaXplore",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 25, 12, 0),
          end: null,
          title: "Last Date of Registration - Enigma",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 25, 12, 0),
          end: null,
          title: "Last Date of Registration - Manthan",
          summary: "",
        },
        // {
        //   isMajor: true,
        //   start: new Date(2024, 2, 27, 12, 0),
        //   end: null,
        //   title: "Event Starts - TBD",
        //   summary: "",
        // },
        {
          isMajor: true,
          start: new Date(2024, 2, 29, 12, 0),
          end: null,
          title: "Event Starts - HaXplore",
          summary: "",
        },
        {
          isMajor: true,
          start: new Date(2024, 2, 29, 12, 0),
          end: null,
          title: "Event Starts - Enigma",
          summary: "",
        }
      ],
    };
  },
};
</script>

<style module lang="stylus">

.timelineContainer {
  font-family: 'Roboto Slab';
  $font-size: 20px;

  .timelineHeader {

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

h1.sectionTitle {
  font-family: 'Baloo Bhaina 2';
  color: var(--heading-color);
  letter-spacing: 2px;
  $font-size: 64px;
  margin-bottom: 0px;

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

</style>
