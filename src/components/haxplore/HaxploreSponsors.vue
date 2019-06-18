<template>
  <SectionLayout title="Sponsors" id="sponsors">
    <div :class="[$style.sponsors, 'sectionContainer', $style[$mq]]">
      <div :class="$style.titleContainer">
        <div :class="$style.cell">
          <div :class="$style.clip">
            <a :href="title.link" target="_blank">
              <img :src="title.image" :class="$style.img">
            </a>
          </div>
        </div>
        <div :class="$style.type">
          <p :class="$style.txt">Title Sponsor</p>
        </div>
      </div>
      <div :class="$style.associateContainer">
        <div :class="$style.cell">
          <div :class="$style.clip">
            <a :href="associate.link" target="_blank">
              <img :src="associate.image" :class="$style.img">
            </a>
          </div>
        </div>
        <div :class="$style.type">
          <p :class="$style.txt">Associate Sponsor</p>
        </div>
      </div>
      <div :class="$style.associate2Container">
        <div :class="$style.cell">
          <div :class="$style.clip">
            <a :href="associate2.link" target="_blank">
              <img :src="associate2.image" :class="$style.img">
            </a>
          </div>
        </div>
        <div :class="$style.type">
          <p :class="$style.txt">Associate Sponsor</p>
        </div>
      </div>
      <div :class="$style.container">
        <GridLayout
          :columns="$mq | mq({xs: 1, sm: 2, md: 3, lg: 4, xl: 5})"
          itemWidth="200px"
          itemHeight="200px"
        >
          <div :class="$style.cell" v-for="(stat, i) in stats" :key="i" :slot="`item${i}`">
            <center>
              <div :class="$style.clip">
                <img :src="stat.image" :class="$style.img">
              </div>
              <br>
              <span :class="$style.txt">{{ stat.text }}</span>
            </center>
          </div>
        </GridLayout>
      </div>
      <div :class="$style.txt"></div>
      <div :class="$style.link">
        <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" :class="$style.linkText" target="_blank">
          <h4>Sponsor Us</h4>
        </a>
      </div>
    </div>
  </SectionLayout>
</template>

<script>
import GridLayout from "../layouts/GridLayout";
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout,
    GridLayout
  },
  data() {
    return {
      stats: [],
      title: {
        image: "assets/Sponsors/aws.png",
        link: "https://aws.amazon.com/"
      },
      associate: {
        image: "assets/Sponsors/devfolio_logo.svg",
        link: "https://devfolio.co/"
      },
      associate2: {
        image: "assets/Sponsors/github.png",
        link: "https://github.com/"
      }
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';
@require '~@styles/anims';

$cell-size = 200px;
$box-height = 200px;
$box-width = 300px;

.sponsors {
  .link {
    margin: auto;
    width: 290px;
    height: auto;
    padding: 24px;
    border-radius: 50px;
    border: 2px solid $chartreuse;
    text-align: center;
    cursor: pointer;

    .linkText {
      color: $chartreuse;
      display: inline;
      text-decoration: none;

      h4 {
        font-family: 'Aldo the Apache';
        font-size: 30px;
        margin: 0;
      }
    }

    &:hover {
      box-shadow: inset 0px 0px 10px $chartreuse;
    }
  }

  .txt {
    text-align: center;

    h4 {
      font-family: 'Quicksand';
      font-weight: bold;
      font-size: 30px;
    }
  }

  .cell {
    width: $cell-size;
    height: $cell-size;

    .clip {
      background-color: white;
      transform: rotate(45deg);
      width: 70%;
      height: 70%;
      border-radius: 25px;
    }

    .img {
      width: 100%;
      height: 100%;
      margin: auto;
      transform: rotate(-45deg);
    }
  }

  .container {
  }

  .titleContainer, .associateContainer, .associate2Container {
    width: 80%;
    margin: 80px auto 25px;
    height: $box-height;
    display: flex;
    justify-content: space-around;

    .cell {
      order: 1;
      width: 250px;
      height: 250px;
      margin: 0 0 0 20px;

      .clip {
        background-color: white;
        transform: rotate(45deg);
        width: 70%;
        height: 70%;
        border-radius: 25px;
      }

      .img {
        width: 100%;
        height: 100%;
        margin: auto;
        transform: rotate(-45deg);
      }

      ~/.md ^[1..-1] {
        width: 200px;
        height: 200px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 200px;
        height: 200px;
        margin: auto;
      }
    }

    ~/.md ^[1..-1] {
      justify-content: space-between;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      flex-flow: column;
      height: auto;
      text-align: center;

      .clip {
        margin-top: 20px;
        margin-left: 30px;
      }
    }

    .type {
      order: 2;
      width: 400px;

      .txt {
        font-family: 'Roboto Slab';
        font-weight: 600;
        font-size: 40px;
        border-top: 3px solid white;
        border-bottom: 3px solid white;
        border-left: 1px solid white;
        border-right: 1px solid white;
        border-radius: 70px 0;
        animation: timeline-border-white 1.5s ease-in-out infinite alternate;
        padding: 20px 0;
        height: 100px;
      }

      ~/.md ^[1..-1] {
        width: 300px;

        .txt {
          height: auto;
          font-size: 25px;
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 250px;
        margin: auto;

        .txt {
          font-size: 20px;
          height: auto;
        }
      }
    }
  }

  .associateContainer, .associate2Container {
    .cell {
      order: 2;
    }

    .type {
      order: 3;

      .txt {
        font-size: 35px;
      }
    }
  }
}
</style>