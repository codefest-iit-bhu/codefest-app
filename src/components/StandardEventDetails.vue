<template>
  <div :class="[$style.event, $style[$mq]]">
    <div :class="$style.whiteHead">
      <div :class="$style.eventLogo">
        <img :src="event.icon" />
      </div>
      <span :class="$style.eventTitle">{{ event.title }}</span>
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
    <div :class="$style.note">
      Note: People not registered for this event on CodeFest are not eligible to
      receive any prizes.
    </div>

    <!-- <div :class="$style.register">
      <h2>Registrations will be live soon.</h2>
    </div> -->

    <div :class="$style.link">
      <router-link to="/dashboard/events/" :class="$style.linkText">
        <h4>Register</h4>
      </router-link>
      <!-- <a v-else :href="event.url" target="_blank"  :class="$style.linkText">
        <h4>Problem Statement</h4>
      </a> -->
    </div>
  </div>
</template>

<script>
const TabLayout = () => import("@components/layouts/TabLayout");
const FAQ = () => import("@components/FAQ");

export default {
  components: {
    TabLayout,
    FAQ,
  },
  props: {
    event: {
      required: true,
    },
  },
  data() {
    return {
      tabs: [
        {
          name: "description",
          title: "Summary",
        },
        {
          name: "contact",
          title: "Contact",
        },
        {
          name: "faq",
          title: "FAQ",
        },
      ],
    };
  },
  mounted() {
    console.log(this.event);
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/anims';

.link {
  margin: auto;
  margin-top: 30px;
  width: 290px;
  height: auto;
  box-shadow: var(--box-shadow);
  padding: 15px;
  border-radius: 0px 30px 0px 30px;
  text-align: center;
  cursor: pointer;

  .linkText {
    color: $waterloo;
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Baloo Bhaina 2';
      $font-size: 30px;
      margin: 0;
    }
  }

  &:hover {
    box-shadow: var(--inset-box-shadow);

    .linkText {
      color: var(--text-color);
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
      background: $vermilion;
      box-shadow: var(--box-shadow);
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
      color: var(--heading-color);
      font-family: 'Baloo Bhaina 2';
      font-weight: 700;
      text-align: right;
      $font-size: 50px;
      margin: 0;
      float: right;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 36px;
      }
    }
  }

  hr {
    height: 8px;
    background-color: $vermilion;
    border-radius: 10px;
    display: block;
    width: 70%;
    border: none;
  }

  .rightHr {
    margin-top: 5px;
    margin-bottom: 72px;
    margin-left: 30%;
    background-image: linear-gradient(to right, var(--background-color), $vermilion);
  }

  .leftHr {
    margin-top: 0;
    margin-right: 30%;
    background-image: linear-gradient(to left, var(--background-color), $vermilion);
  }

  .eventDesc {
    margin-bottom: 100px;

    .tabContainer {
      padding: 36px;
      background-color: var(--background-color);
      box-shadow: var(--inset-box-shadow);

      .tabTitle {
        $font-size: 36px;
        font-family: 'Baloo Bhaina 2';
        font-wright: 600;
        margin-top: 12px;
        margin-bottom: 4px;
      }

      .text {
        margin-top: 36px;
        margin-bottom: 20px;
        font-family: 'Quicksand';
        font-weight: 500;

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          $font-size: 15px;
        }
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
          $font-size: 14px;

          &:before {
            content: ' ';
          }
        }
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

.register {
  text-align: center;
  font-family: 'Roboto Slab';
  font-weight: 700;
}

.note {
  font-family: 'Quicksand';
  font-weight: 700;
  box-shadow: var(--box-shadow);
  padding: 20px;
  text-align: center;
  width: 70%
  margin: 0 auto;
  border-radius: 25px 0;
}
</style>
