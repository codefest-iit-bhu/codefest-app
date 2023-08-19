<template>
  <SectionLayout title="Previous Sponsors" id="sponsors">
    <div :class="[$style.sponsors, $style[$mq]]">
      <!-- <ResponsiveTwoColumnLayout>
        <div :class="$style.title" slot="left">
          <div :class="$style.cell">
            <div :class="$style.clip">
              <a :href="title.link" target="_blank">
                <img :src="title.image" :class="$style.img" />
              </a>
            </div>
          </div>
        </div>
        <div :class="$style.titleText" slot="right">
          <div :class="$style.txt">Title Sponsor</div>
        </div>
      </ResponsiveTwoColumnLayout>-->
      <div :class="$style.container">
        <GridLayout
          :columns="$mq | mq({ xs: 1, sm: 1, md: 2, lg: 2, xl: 2 })"
          itemWidth="260px"
          itemHeight="260px"
        >
          <div :class="$style.cell" v-for="(stat, i) in stats" :key="i" :slot="`item${i}`">
            <div :class="$style.clip">
              <img :src="stat.image" :class="$style.img" />
            </div>
          </div>
        </GridLayout>
      </div>

      <div :class="$style.buttonContainer">
        <!-- <div :class="$style.link"> -->
          <a
            href="https://drive.google.com/file/d/15BYqDZwShgFFqkgBPKqr0j-AcFF-_Umm"
            :class="$style.linkText"
            target="_blank"
          >
            <!-- <h4>Sponsor Brochure</h4> -->
            <Button text="Sponsor Brochure"/>
          </a>
        <!-- </div> -->
        <!-- <div :class="$style.link"> -->
          <a
            href="https://docs.google.com/forms/d/e/1FAIpQLScinI5YpU61F8Re4wFooBgH18Q8iE1_Du-nW1IIExruqLwRpw/viewform"
            :class="$style.linkText"
            target="_blank"
          >
            <!-- <h4>Sponsor Us</h4> -->
            <Button text="Sponsor Us" />
          </a>
        <!-- </div> -->
      </div>
    </div>
  </SectionLayout>
</template>

<script>
import Button from "./layouts/Button.vue"
const GridLayout = () => import("./layouts/GridLayout");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    Button,
    SectionLayout,
    GridLayout,
    ResponsiveTwoColumnLayout,
  },
  data() {
    return {
      stats: [
        {
          image: "assets/Sponsors/aws.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/cisco.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/mozilla1.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/top-coder.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/eligible.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/uber.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/zebronics.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/grab-on.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/hackerearth.png",
          link: "#",
        },
        {
          image: "assets/Sponsors/hackerrank.png",
          link: "#",
        },
      ],
      buttonHovered: false,
    };
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

$cell-size = 200px;
$box-height = 250px;
$box-width = 250px;

.sponsors {
  .offset {
    ~/.xl ^[1..-1], ~/.xxl ^[1..-1] {
      width: 80%;
      margin: auto;
    }
  }

  .buttonContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      flex-flow: column;
      margin: auto;
    }
  }

  .linkText {
    // display: inline-block;
    // text-decoration: none;
    // color: $waterloo;
    

    // h4 {
    //   text-align: center;
    //   position: relative;
    //   top: 50%;
    //   -ms-transform: translateY(-50%);
    //   -webkit-transform: translateY(-50%);
    //   transform: translateY(-50%);
    //   font-family: 'Roboto Slab';
    //   $font-size: 30px;
    // }
    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      margin: 20px;
      margin-top:30px;
    }

  }

  .txt {
    text-align: center;

    h4 {
      font-family: 'Quicksand';
      font-weight: bold;
      $font-size: 30px;
    }
  }

  .container {
    .cell {
      width: $cell-size;
      height: $cell-size;

      .clip {
        background-color: white;
        width: 85%;
        height: 85%;
        padding: 10px;
        border-radius: 25px;
        box-shadow: var(--box-shadow);
      }

      .img {
        width: 100%;
        height: 100%;
        margin: auto;
      }

      .txt {
        $font-size: 20px;
        font-family: 'Roboto Slab';
        font-weight: 600;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        text-align: center;
        width: 150px;
        height: 150px;

        .clip {
          margin-top: 20px;
          margin-left: 7px;
        }
      }
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      margin: 0 auto 25px;
    }
  }

  .title {
    width: 80%;
    margin: 80px auto;
    height: $box-height;

    .cell {
      width: 300px;
      height: 300px;
      margin: auto;

      .clip {
        background-color: white;
        transform: rotate(45deg);
        width: 70%;
        height: 70%;
        border-radius: 25px;
        margin: 30px 15%;
      }

      .img {
        width: 100%;
        height: 100%;
        margin: auto;
        transform: rotate(-45deg);
      }

      ~/.md ^[1..-1] {
        width: 360px;
        height: 360px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 240px;
        height: 240px;
        margin: 20px auto 0;
      }
    }

    ~/.md ^[1..-1] {
      justify-content: space-between;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      flex-flow: column;
      height: auto;
      text-align: center;
      margin: auto;

      .clip {
        margin-top: 20px;
        margin-left: 30px;
      }
    }
  }

  .titleText {
    .txt {
      margin: 150px auto;
      $font-size: 60px;
      font-family: 'Roboto Slab';
      font-weight: 600;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      .txt {
        margin: 0 auto 50px;
        padding-top: 0;
        $font-size: 30px;
      }
    }
  }
}
</style>
