<template>
  <div :class="[$style.lookback, 'sectionContainer']">
    <h1 class="sectionTitle">Lookback</h1>
    <hr class="sectionLine">

    <div :class="$style.container">
      <div :class="$style.stat" v-for="(stat, i) in stats" :key="i">
        <div :class="$style.clip">
          <img :src="stat.image" :class="$style.img">
        </div>
        <div :class="$style.name">{{ stat.name }}</div>
        <div :class="$style.value">{{ stat.value }}</div>
      </div>
    </div>
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
  .container {
    display: grid;
    grid-template-columns: 200px 200px 200px;
    grid-template-rows: 200px;
    grid-column-gap: 30px;
    grid-row-gap: 50px;
    justify-content: space-evenly;
  }

  .stat {
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

    .name, .value {
      font-family: Aldo the Apache;
      margin-left: auto;
      margin-right: auto;
      text-align: center;
      color: $chartreuse;
      line-height: 28px;
      font-size: 25px;
    }
  }
}
</style>
