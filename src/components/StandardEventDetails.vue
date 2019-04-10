<template>
  <div :class="[$style.event, $style[$mq]]">
    <div :class="$style.whiteHead">
      <div :class="$style.eventLogo">
        <img :src="event.icon">
      </div>
      <span :class="$style.eventTitle">{{event.title}}</span>
    </div>
    <hr :class="$style.rightHr">

    <div :class="$style.eventDesc">
      <TabLayout :tabs="tabs">
        <div :class="$style.tabContainer" slot="description">
          <h4 :class="$style.tabTitle">Description</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text">{{ event.description }}</p>
        </div>

        <div :class="$style.tabContainer" slot="rules">
          <h4 :class="$style.tabTitle">Rules</h4>
          <hr :class="$style.leftHr">
          <ul>
            <li
              :class="$style.ruleText"
              v-for="(rule, i) in event.rules"
              :key="i"
              :inner-html.prop="rule | anchor"
            ></li>
          </ul>
        </div>

        <div :class="$style.tabContainer" slot="contact">
          <h4 :class="$style.tabTitle">Co-ordinators</h4>
          <hr :class="$style.leftHr">
          <ul>
            <li
              :class="$style.ruleText"
              v-for="(coordinator, i) in event.coordinators"
              :key="i"
              :inner-html.prop="coordinator | anchor"
            ></li>
          </ul>
        </div>

        <div :class="$style.tabContainer" slot="faq">
          <h4 :class="$style.tabTitle">FAQ</h4>
          <hr :class="$style.leftHr">
          <p :class="$style.text" :inner-html.prop="event.faqIntro | anchor">}</p>
          <FAQ :faqItems="event.faq"/>
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
import FAQ from "@components/FAQ";

export default {
  components: {
    TabLayout,
    FAQ
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
          name: "description",
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
  padding-top: 16px;

  .whiteHead {
    height: 108px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;

    .eventLogo {
      order: -2;
      background: $chartreuse;
      border-radius: 50%;
      width: 108px;
      height: 108px;
      padding: 18px;

      img {
        height: 100%;
        margin: 0;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 72px;
        height: 72px;
      }
    }

    .eventTitle {
      order: -1;
      color: $white;
      font-family: 'Aldo the Apache';
      text-align: right;
      font-size: 50px;
      margin: 0;
      float: right;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 36px;
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

    .tabContainer {
      padding: 36px;

      .tabTitle {
        font-size: 36px;
        font-family: 'Aldo the Apache';
        margin-top: 12px;
        margin-bottom: 18px;
      }

      .text {
        font-size: 20px;
        margin-top: 36px;
        margin-bottom: 20px;
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

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 220px;

        .linkText {
          font-size: 21px;
        }
      }

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
  }
}
</style>
