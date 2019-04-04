<template>
  <div :class="[$style.sponsors, 'sectionContainer']">
    <center>
      <div :class="$style.titleContainer">
        <div :class="$style.titleImg">
          <!-- Image Here -->
        </div>
        <div :class="$style.titleTxt">Title Sponsor</div>
      </div>
    </center>
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
  </div>
</template>

<script>
import GridLayout from "./layouts/GridLayout";
export default {
  data() {
    return {
      stats: [
        {
          image: "assets/Sponsors/aws.png",
          text: "Assoicate Sponsor"
        },
        {
          image: "assets/Sponsors/eligible.png",
          text: "ABC Sponsor"
        },
        {
          image: "assets/Sponsors/uber.png",
          text: "XYZ Sponsor"
        },
        {
          image: "assets/Sponsors/top-coder.png",
          text: "Platform Sponsor"
        },
        {
          image: "assets/Sponsors/uber.png",
          text: "AB Sponsor"
        },
        {
          image: "assets/Sponsors/uber.png",
          text: "AB Sponsor"
        }
      ]
    };
  },
  components: {
    GridLayout
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

$cell-size = 200px;
$box-height = 200px;
$box-width = 300px;

.sponsors {
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

  .titleContainer {
    width: $box-width;
    height: $box-height;
    margin-bottom: 50px;
    display: grid;
    grid-template-rows: 1fr 50px;
    grid-row-gap: 10px;

    .titleImg {
      border: 1px solid $chartreuse;
      box-shadow: inset 0px 0px 10px #86ff00;
    }

    .titleTxt {
      text-align: center;
      font-family: Aldo the Apache;
      font-size: 25px;
    }
  }
}
</style>