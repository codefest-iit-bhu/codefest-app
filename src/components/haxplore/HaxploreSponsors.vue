<template>
  <SectionLayout title="Previous Sponsors" id="sponsors">
    <div :class="[$style.sponsors, $style[$mq]]">
      <!-- <ResponsiveTwoColumnLayout :class="$style.offset">
        <div :class="$style.title" slot="left">
          <div :class="$style.cell">
            <div :class="$style.clip">
              <a :href="title.link" target="_blank">
                <img :src="title.image" :class="$style.img">
              </a>
            </div>
          </div>
        </div>
        <div :class="$style.titleText" slot="right">
            <div :class="$style.txt">Title Sponsor</div>
        </div>
      </ResponsiveTwoColumnLayout> -->
      <div :class="$style.container">
        <GridLayout
          :columns="$mq | mq({xs: 1, sm: 1, md: 2, lg: 2, xl: 2})"
          itemWidth="260px"
          itemHeight="260px"
        >
          <div :class="$style.cell" v-for="(stat, i) in stats" :key="i" :slot="`item${i}`">

                <a target="_blank" :href="stat.link">

                <div :class="$style.clip">
                  <img :src="stat.image" :class="$style.img">
                </div>
                <br>
                <span :class="$style.txt">{{ stat.text }}</span>

                </a>
          </div>
        </GridLayout>
      </div>
      <!-- <div :class="$style.buttonContainer">
      <div :class="$style.link">
          <a
            href="https://drive.google.com/file/d/1ABFiTwX8Eb7w--0DOqpzJOPqjiE-WQ9D/view?usp=sharing"
            :class="[$style.linkText]"
            target="_blank"
          >
            <h4>Sponsor Brochure</h4>
          </a>
        </div>
        <div :class="$style.link">
          <a
            href="https://docs.google.com/forms/d/e/1FAIpQLScinI5YpU61F8Re4wFooBgH18Q8iE1_Du-nW1IIExruqLwRpw/viewform"
            :class="[$style.linkText]"
            target="_blank"
          >
            <h4>Sponsor Us</h4>
          </a>
        </div>
      </div> -->
    </div>
  </SectionLayout>
</template>

<script>
const GridLayout = () => import("../layouts/GridLayout");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    SectionLayout,
    GridLayout,
    ResponsiveTwoColumnLayout,
  },
  data() {
    return {
      stats: [
        {
          image: "assets/Sponsors/Devfolio_Logo-Colored.svg",
          link: "https://devfolio.co/"
        },
        {
          image: "assets/Sponsors/github.png",
          link: "https://github.com/"
        },
        {
          image: "assets/Sponsors/polygon.svg",
          link: "https://polygon.technology/"
        },
        {
          image: "assets/Sponsors/Portis_Logo-Black.svg",
          link: "https://www.portis.io"
        },
        {
          image: "assets/Sponsors/Tezos_Logo-Colored.svg",
          link: "https://tezos.com"
        },
        {
          image: "assets/Sponsors/aws.png",
          link: "https://aws.amazon.com/"
        }


        
      ],
      title: {
        image: "assets/Sponsors/aws.png",
        link: "https://aws.amazon.com/"
      }
    };
  }
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
  }

  .link {
    margin: 20px 20px 20px 20px;
    width: 250px;
    height: 120px;
    padding: 20px;
    box-shadow: var(--box-shadow);
    border-radius: 50px 0px 50px 0px;
    text-align: center;
    cursor: pointer;

    .linkText {
      display: inline-block;
      text-decoration: none;
      color: $waterloo;

      h4 {
        text-align: center;
        position: relative;
        top: 50%;
        -ms-transform: translateY(-50%);
        -webkit-transform: translateY(-50%);
        transform: translateY(-50%);
        font-family: 'Roboto Slab';
        $font-size: 30px;
      }
    }

    &:hover {
      box-shadow: var(--inset-box-shadow);

      .linkText {
        color: var(--text-color);
      }
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

      a{
        text-decoration: none;
        color: var(--text-color);
      }

      .clip {
        background-color: white;
        width: 70%;
        height: 70%;
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
        width: 200px;
        height: 200px;

        .clip {
          margin-top: 20px;
          margin-left: 30px;
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
