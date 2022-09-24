<template>
  <div :class="[$style.workContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout :isRightAbove="true">
      <div :class="$style.workImage" slot="right">
        <img src="#" />
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
          start: "Connect : ",
          rest:
            "Grow a strong network with peers inside your college as well as the Codefest team.",
        },
        {
          start: "Communication : ",
          rest:
            "Develop communication skills and get an edge over competition.",
        },
        {
          start: "Certificate : ",
          rest:
            "Get Work Experience certificate as a Codefest Campus Ambassador.",
        },
        {
          start: "Goodies : ",
          rest:
            "Official Codefest goodies and/or tees depending upon the number of participants in Codefest from your college.",
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
            color: $waterloo;
          }

          .textStart {
            color: $waterloo;
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
