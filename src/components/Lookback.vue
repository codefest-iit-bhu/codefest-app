<template>
  <div :class="[$style.lookback, 'sectionContainer']">
    <h1 class="sectionTitle">Lookback</h1>
    <hr class="sectionLine">
    <!-- <div :class="$style.cell" v-for="(stat, i) in stats" :key="i">
      <div :class="$style.clip">
        <img :src="stat.image" :class="$style.img">
      </div>
      <div :class="$style.txt">
        {{ stat.name }}
        <br>
        {{ stat.value }}
      </div>
    </div>-->
    <div :class="$style.table">
      <table>
        <tr :id="$style.imgRow">
          <td :class="$style.imgCell" v-for="(stat, i) in stats" :key="i">
            <div :class="$style.clip">
              <img :src="stat.image" :class="$style.img">
            </div>
          </td>
        </tr>
        <tr :id="$style.nameRow">
          <td :class="$style.dataCell" v-for="(stat, i) in stats" :key="i">
            <div :class="$style.txt">{{ stat.name }}</div>
          </td>
        </tr>
        <tr :id="$style.valRow">
          <td :class="$style.dataCell" v-for="(stat, i) in stats" :key="i">
            <div :class="$style.txt">{{ stat.value }}</div>
          </td>
        </tr>
      </table>
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
  .table {
    table {
      width: 80%;
      margin: auto;

      #imgRow {
        .imgCell {
          width: 200px;
          height: 200px;

          .clip {
            clip-path: polygon(25% 0%, 75% 0%, 100% 43.3%, 75% 86.6%, 25% 86.6%, 0% 43.3%);
            background: white;
            width: 160px;
            height: 160px;
            margin-left: auto;
            margin-right: auto;
            padding: 10px;
            background-color: $chartreuse;
          }

          .img {
            width: 70%;
            position: relative;
            top: 10%;
            left: 15%;
          }
        }
      }

      #nameRow, #valRow {
        .dataCell {
          font-family: Aldo the Apache;
          margin-left: auto;
          margin-right: auto;
          text-align: center;
          margin-top: 300px;

          .txt {
            color: $chartreuse;
            // position: relative;
            // top: -76%;
            line-height: 28px;
            font-size: 25px;
          }
        }
      }
    }
  }
}
</style>
