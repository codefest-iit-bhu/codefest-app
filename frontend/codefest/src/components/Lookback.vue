<template>
  <div :class="[$style.lookback, 'sectionContainer']">
    <h1 class="sectionTitle">Lookback</h1>
    <div :class="$style.cell" v-for="(stat, i) in stats" :key="i">
      <div :class="$style.clip">
        <img :src="stat.image" :class="$style.img">
      </div>
      <div :class="$style.txt">
        {{ stat.name }}
        <br>
        {{ stat.value }}
      </div>
    </div>
    <br>

    <!-- <svg class="clip-svg">
      <defs>
        <clipPath id="hexagon-clip" clipPathUnits="objectBoundingBox">
          <polygon points="0.25 0.05, 0.75 0.05, 1 0.5, 0.75 0.95, 0.25 0.95, 0 0.5" />
        </clipPath>
      </defs>
    </svg>-->
  </div>
</template>
<script>
export default {
  data() {
    return {
      stats: [
        {
          name: "Prize Money",
          value: "500,000",
          image: "assets/Lookback/rupee.png"
        },
        {
          name: "Countries",
          value: "98",
          image: "assets/Lookback/countries.png"
        },
        {
          name: "Participants",
          value: "24,654",
          image: "assets/Lookback/participants.png"
        },
        {
          name: "Unique Visitors",
          value: "328,902",
          image: "assets/Lookback/visitors.png"
        },
        {
          name: "Registrations",
          value: "16,302",
          image: "assets/Lookback/registrations.png"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@import '../styles/theme.styl';
@import '../styles/colors.styl';

.lookback {
  .cell {
    width: 500px;
    height: 100px;
    margin-left: auto;
    margin-right: auto;
    font-family: Aldo the Apache;

    .txt {
      color: $chartreuse;
      position: relative;
      top: -76%;
      line-height: 28px;
      font-size: 25px;
    }

    .clip {
      clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
      background: white;
      width: 100px;
      height: 100px;
      padding: 10px;
      background-color: $chartreuse;
    }

    .img {
      width: 80%;
      height: 80%;
      position: relative;
      top: -45%;
      left: 10%;
    }

    &:nth-child(2) {
      .img {
        top: 0;
        left: 0;
        margin: 10px;
      }
    }

    &:nth-child(odd) {
      .txt {
        margin-right: 55%;
        text-align: right;
        float: right;
      }

      .clip {
        margin-left: 50%;
      }
    }

    &:nth-child(even) {
      .txt {
        margin-left: 55%;
        text-align: left;
        float: left;
      }

      .clip {
        margin-left: 30%;
      }
    }
  }
}
</style>
