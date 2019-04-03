<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar>
      <ul v-scroll-spy-active="{class: $style.active}" v-scroll-spy-link>
        <li :key="item" v-for="item in titles">
          <a>
            <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
            {{item}}
          </a>
        </li>
      </ul>
    </AppBar>
    <main :class="$style.wrapper">
      <div v-scroll-spy>
        <FAQ/>
        <Timeline/>
        <Prizes/>
      </div>
    </main>
  </div>
</template>

<script>
import AppBar from "@components/haxplore/AppBar";
import Timeline from "@components/haxplore/Timeline";
import FAQ from "@components/haxplore/FAQ";
import Prizes from "@components/haxplore/Prizes";
import Footer from "@components/Footer";
import SectionLayout from "@components/layouts/SectionLayout";

export default {
  components: {
    AppBar,
    FAQ,
    Timeline,
    Prizes,
    SectionLayout
  },
  data() {
    return {
      section: 0,
      titles: ["FAQ", "Timeline", "Prizes"]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 20px 20px 50px 20px;
  position: relative;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.faqContainer {
  width: 100%;
  font-family: 'ubuntu';
  font-size: 20px;

  .faqHeader {
    line-height: 30px;
    font-weight: bold;
    text-align: center;

    img {
      width: 300px;
      height: 300px;
    }
  }
}

.root.xs, .root.sm {
  .faqContainer {
    margin-top: 50px;

    .faqHeader {
      display: flex;
      flex-direction: row;
      align-items: flex-end;

      img {
        width: 100px;
        height: 100px;
      }

      .faqMessage {
        font-size: 13px;
        line-height: 20px;
        margin-left: 20px;
      }
    }

    .faqList {
      margin: 20px 0;
    }
  }
}

.active {
  a {
    color: $chartreuse !important;
    font-weight: bold;

    span {
      color: $white;
      animation: neon-text 1s ease-in-out infinite alternate;
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
