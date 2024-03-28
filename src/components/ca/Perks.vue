<template>
  <div :class="[$style.workContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout :isRightAbove="true">
      <div :class="$style.workImage" slot="right">
        <img src="@assets/ca/perks.svg" />
      </div>
      <div :class="$style.workHead" slot="left">
        <div :class="$style.taskList">
          <ul :class="$style.list" class="fa-ul">
            <li :class="$style.taskItem" v-for="(task, i) in tasks" :key="i">
              <span class="fa-li">
                <i class="fas fa-caret-right"></i>
              </span>
              <span :class="$style.textStart">{{ task.start }}</span>
              {{ task.rest }}
            </li>
          </ul>
        </div>
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
  data() {
    return {
      tasks: [
        {
          start: "A certificate of recognition, authenticated by the HoD ",
          rest:
            "of the Department of Computer Science and Engineering, IIT(BHU),  that will boost your resume and showcase your leadership skills.",
        },
        {
          start: "Unlock a treasure chest of exciting goodies ",
          rest:
            "– perks you won't find anywhere else!",
        },
        {
          start: "Free access ",
          rest:
            "to exclusive workshops, seminars, and events organized by CodeFest that will enhance your knowledge and skills in various domains of coding.",
        },
        {
          start: "Build lasting connections and professional networks ",
          rest:
            "with like-minded peers within the vibrant CodeFest community.",
        },
        {
          start: "Track your impact ",
          rest:
            "and see your hard work pay off with the dynamic leaderboard on CodeFest's official website. The top-ranked Campus Ambassadors will unlock exclusive rewards and recognition.",
        },
        {
          start: "A lifetime experience ",
          rest:
            "of being part of a dynamic community of coders eager to learn, innovate, and create an impact.",
        },
      ],
    };
  },
};
</script>

<style module lang="stylus">
.workContainer {
  width: 100%;
  padding-top: 30px;

  .workImage {
    text-align: center;

    img {
      width: 400px;
      margin: auto;
      margin-top: 80px;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 200px;
        margin-bottom: 0;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        width: 300px;
        margin-top: 60px;
      }
    }
  }

  .workHead {
    .taskList {
      width: 600px;
      margin: auto;
      font-family: 'Quicksand';
      font-weight: 500;
      border-radius: 10px;
      padding: 30px 10px;

      .list {
        list-style: none;

        .taskItem {
          padding: 20px 0;

          span {
            color: $vermilion;
          }

          .textStart {
            color: $vermilion;
            font-weight: 600;
            letter-spacing: 1px;
            font-family: 'Roboto Slab';
          }

          ~/.md ^[1..-1], ~/.lg ^[1..-1] {
            padding: 0 0 30px 0;
          }
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: auto;
        padding-top: 0;
        $font-size: 16px;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        width: auto;
        padding-top: 0;
        $font-size: 18px;
      }
    }
  }
}
</style>
