<template>
  <div :class="$style.event">
    <div :class="$style.whiteHead">
      <div :class="$style.eventLogo">
        <img :src="event.icon">
      </div>
      <div :class="$style.eventTitle">
        <p>{{event.title}}</p>
      </div>
    </div>
    <hr :class="$style.rightHr">

    <div :class="$style.eventDesc">
      <TabLayout :tabs="tabs">
        <div :class="$style.descContainer" slot="summary">
          <h4 :class="$style.tabTitle">Summary</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text">{{event.summary}}</p>
        </div>

        <div :class="$style.descContainer" slot="rules">
          <h4 :class="$style.tabTitle">Rules</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text"></p>
          <ul>
            <li :class="$style.ruleText" v-for="(rule, i) in event.rules" :key="i">{{ rule }}</li>
          </ul>
        </div>

        <div :class="$style.descContainer" slot="contact">
          <h4 :class="$style.tabTitle">Co-ordinators</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text"></p>
          <div :class="$style.stat" v-for="(stat, i) in event.coordinators" :key="i">
            <div :class="$style.name">{{ stat.name }}</div>
            <div :class="$style.email">{{ stat.email }}</div>
          </div>
        </div>

        <div :class="$style.descContainer" slot="faq">
          <h4 :class="$style.tabTitle">FAQ</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text"></p>
          <div :class="$style.stat" v-for="(stat, i) in event.faq" :key="i">
            <div :class="$style.question">{{ stat.question }}</div>
            <div :class="$style.answer">{{ stat.answer }}</div>
          </div>
        </div>
      </TabLayout>
    </div>

    <div :class="$style.ps">
      <div :class="$style.link">
        <a href="#">
          <h4 :class="$style.linkText">Problem Statement</h4>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import TabLayout from "@components/layouts/TabLayout";

export default {
  components: {
    TabLayout
  },
  props: {
    event: {
      required: true
    }
  },
  data() {
    return {
      tabs: [
        {
          name: "summary",
          title: "Summary"
        },
        {
          name: "rules",
          title: "Rules"
        },
        {
          name: "contact",
          title: "Contact"
        },
        {
          name: "faq",
          title: "FAQ"
        }
      ]
    };
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.event {
  .whiteHead {
    margin-top: 64px;
    height: 108px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;

    .eventLogo {
      order: -2;
      background: $chartreuse;
      border-radius: 50%;
      width: 108px;
      height: 108px;
      padding: 18px;

      img {
        height: 72px;
        margin: 0;
      }
    }

    .eventTitle {
      order: -1;

      p {
        color: $white;
        font-family: 'Aldo the Apache';
        text-align: right;
        font-size: 50px;
        margin: 0;
        float: right;
        padding-top: 30px;
      }
    }
  }

  hr {
    height: 4px;
    background-color: $chartreuse;
    display: block;
    width: 70%;
    border: none;
  }

  .rightHr {
    margin-top: 5px;
    margin-bottom: 72px;
    margin-left: 30%;
    background-image: linear-gradient(to right, $black, $chartreuse);
  }

  .leftHr {
    margin-top: 0;
    margin-right: 30%;
    background-image: linear-gradient(to left, $black, $chartreuse);
  }

  .eventDesc {
    margin-bottom: 100px;

    .descContainer {
      padding: 36px;

      .tabTitle {
        font-size: 48px;
        font-family: 'Aldo the Apache';
        margin-top: 12px;
        margin-bottom: 18px;
      }

      .text {
        font-size: 20px;
        margin-top: 36px;
        margin-bottom: 10px;
        font-family: 'Quicksand';
        font-weight: 500;
      }

      ul {
        padding-left: 25px;

        .ruleText {
          font-family: 'Quicksand';
          font-weight: 500;
          margin-bottom: 10px;
        }
      }

      .stat {
        .name, .question {
          font-family: 'Aldo the Apache';
          font-size: 28px;
          margin-bottom: 12px;
        }

        .email, .answer {
          margin-bottom: 20px;
          font-family: 'Quicksand';
          font-weight: 500;
        }
      }
    }
  }

  .ps {
    .link {
      margin: 0 auto 60px;
      width: 290px;
      height: auto;
      padding: 24px;
      border-radius: 50px;
      box-shadow: inset 0px 0px 20px $chartreuse;
      animation: neon-box 1.5s ease-in-out infinite alternate;
      border: 2px solid $chartreuse;

      a {
        text-decoration: none;
      }

      .linkText {
        font-family: 'Aldo the Apache';
        font-size: 30px;
        color: $chartreuse;
        margin-top: 20px;
        text-align: center;
        display: inline;
      }
    }
  }

  .contacts {
    .container {
      display: grid;
      grid-template-columns: 50% 50%;
      grid-template-rows: 100px;
      grid-column-gap: 30px;
      grid-row-gap: 50px;
      justify-content: space-evenly;
    }

    .stat {
      .name, .email {
        font-family: 'ubuntu';
        font-weight: bold;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        font-size: 20px;
      }
    }
  }
}
</style>
