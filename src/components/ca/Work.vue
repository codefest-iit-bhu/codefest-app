<template>
  <div :class="[$style.workContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout>
      <div :class="$style.workImage" slot="left">
        <img src="@assets/haxplore/faq.svg">
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
        <div
          :class="$style.para"
        >The number of participants from your college will determine the number of goodies you get as a Campus Ambassador of Codefest.</div>
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
          start: "Connect ",
          rest:
            "Codefest with the student community inside your campus and circle."
        },
        {
          start: "Publicize",
          rest:
            "Codefest by sharing the posts and updates on social media, through word-of-mouth, posters and e-mails."
        },
        {
          start: "Encourage",
          rest:
            "the students of your campus for active participation in Codefest."
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
      margin-left: 0;
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