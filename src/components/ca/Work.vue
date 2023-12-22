<template>
  <div :class="[$style.workContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout>
      <div :class="$style.workImage" slot="left">
        <img src="@assets/ca/work.svg" />
      </div>
      <div :class="$style.workHead" slot="right">
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
    <!-- <div :class="$style.para">
      The number of participants from your college will determine the number of
      goodies you get as a Campus Ambassador of CodeFest.
    </div> -->
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
          start: "Coordinating ",
          rest:
            "with our organizing team to facilitate the participation process for students from your college",
        },
        {
          start: "Creating awareness ",
          rest:
            "about CodeFest in your respective colleges by circulating posters, mails or messages in the official college groups",
        },
        {
          start: "Promoting CodeFest ",
          rest:
            "in your college campus and through various social media platforms, including but not limited to Facebook, Instagram, and LinkedIn",
        },
        {
          start: "Encouraging students ",
          rest:
            "from your college to participate in the event and engage in the various activities and competitions",
        },
        {
          start: "Providing feedback and suggestions ",
          rest:
            "to enhance the overall experience of participants",
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
      margin: 40px 0;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 200px;
      }

      ~/.md ^[1..-1] {
        width: 260px;
        margin-top: 100px;
      }

      ~/.lg ^[1..-1] {
        width: 300px;
        margin-top: 40px;
        margin-bottom: 40px;
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
      padding: 20px 10px;

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
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        padding: 0 10px;
        width: auto;
        $font-size: 16px;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        padding: 0 10px;
        $font-size: 18px;
      }

      ~/.md ^[1..-1] {
        width: 360px;
      }

      ~/.lg ^[1..-1] {
        width: 440px;
      }
    }
  }

  .para {
    box-shadow: inset 0 0 20px $vermilion;
    border-radius: 20px 0 20px 0;
    padding: 30px;
    text-align: center;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      padding: 20px;
      border-radius: 15px 0 15px 0;
      $font-size: 16px;
      width: auto;
      text-align: center;
    }

    ~/.md ^[1..-1], ~/.lg ^[1..-1] {
      padding: 20px 20px;
      width: 600px;
      margin-top: 30px;
      margin: auto;
    }
  }
}
</style>
