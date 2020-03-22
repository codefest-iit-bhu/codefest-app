<template>
  <div :class="[$style.event, $style[$mq]]">
    <div :class="$style.whiteHead">
      <div :class="$style.eventLogo">
        <img :src="event.icon" />
      </div>
      <span :class="$style.eventTitle">{{event.title}}</span>
    </div>
    <hr :class="$style.rightHr" />

    <div :class="$style.eventDesc">
      <TabLayout :tabs="tabs">
        <div :class="$style.tabContainer" slot="description">
          <h4 :class="$style.tabTitle">Description</h4>
          <hr :class="$style.leftHr" />
          <p :class="$style.text">{{ event.description }}</p>
        </div>

        <div :class="$style.tabContainer" slot="contact">
          <h4 :class="$style.tabTitle">Co-ordinators</h4>
          <hr :class="$style.leftHr" />
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
          <hr :class="$style.leftHr" />
          <!-- <p :class="$style.text" :inner-html.prop="event.faqIntro | anchor">}</p> -->
          <FAQ :faqItems="event.faq" />
        </div>
      </TabLayout>
    </div>
    <div
      :class="$style.note"
    >Note: People not registered for this event on CodeFest are not eligible to recieve any prizes.</div>

    <div :class="$style.link">
      <router-link to="/dashboard/events/" v-if="!event.url" :class="$style.linkText">
        <h4>Register</h4>
      </router-link>
      <a v-else :href="event.url" target="_blank"  :class="$style.linkText">
        <h4>Problem Statement</h4>
      </a>
    </div>
  </div>
</template>

<script>
const TabLayout = () => import("@components/layouts/TabLayout");
const FAQ = () => import("@components/FAQ");

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

.link {
  margin: auto;
  width: 290px;
  height: auto;
  padding: 24px;
  border-radius: 20px 2px;
  box-shadow: 8px 8px 20px $botticelli, -12px -12px 20px $white;
  text-align: center;
  cursor: pointer;
  transition: all 2s ease;

  .linkText {
    color: $waterloo;
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin: 0;
    }
  }

  &:hover {
    box-shadow: inset 8px 8px 20px $botticelli, inset -12px -12px 20px $white;

    .linkText{
      color: $mine-shaft;
    }
  }
}

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
      background: $mystic;
      box-shadow: 8px 8px 20px $botticelli, -12px -12px 20px $white;
      border-radius: 50%;
      width: 108px;
      height: 108px;
      padding: 24px;

      img {
        height: 100%;
        margin: 0;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 72px;
        height: 72px;
      }

      &:hover {
        background: $lonestar;
      }
    }

    .eventTitle {
      order: -1;
      color: $cod-gray;
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
    background-color: $waterloo;
    display: block;
    width: 70%;
    border: none;
  }

  .rightHr {
    margin-top: 5px;
    margin-bottom: 72px;
    margin-left: 30%;
    background-image: linear-gradient(to right, $mystic, $waterloo);
  }

  .leftHr {
    margin-top: 0;
    margin-right: 30%;
    background-image: linear-gradient(to left, $mystic, $waterloo);
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

      .text, .ruleText {
        a {
          word-break: break-all;
          color: $waterloo;
          font-size: 14px;
          font-weight: 600;

          &:before {
            content: ' ';
          }
        }

        a:hover{
          color: $black;
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
      border-radius: 20px 2px 20px 2px;
      box-shadow: inset 0px 0px 20px $tulip-tree;
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

.note {
  font-family: 'Quicksand';
  font-weight: 600;
  text-align: center;
  padding-bottom: 20px;
}
</style>
