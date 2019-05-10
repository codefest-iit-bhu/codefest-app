<template>
  <div :class="[$style.workContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout>
      <div :class="$style.workImage" slot="right">
        <img src="@assets/haxplore/faq.svg">
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
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      tasks: [
        {
          start: "Connect : ",
          rest:
            "Grow a strong network with peers inside your college as well as the Codefest team."
        },
        {
          start: "Communication : ",
          rest: "Develop communication skills and get an edge over competition."
        },
        {
          start: "Certificate : ",
          rest:
            "Get Work Experience certificate as a Codefest Campus Ambassador."
        },
        {
          start: "Goodies : ",
          rest:
            "Official Codefest goodies and/or tees depending upon the number of participants in Codefest from your college."
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.workContainer {
  width: 100%;
  padding-top: 30px;

  .workImage {
    img {
      width: 80%;
      margin-left: 20%;
      margin-bottom: 50px;
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
            color: $chartreuse;
          }

          .textStart {
            color: $chartreuse;
            font-weight: 600;
            letter-spacing: 1px;
            font-family: 'Roboto Slab';
          }
        }
      }
    }

    .para {
      box-shadow: inset 0 0 20px $chartreuse;
      border-radius: 20px 0 20px 0;
      padding: 30px;
    }
  }
}
</style>