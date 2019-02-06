<template>
  <div :class="[$style.sponsors, 'sectionContainer']">
    <h1 class="sectionTitle">Sponsors</h1>
    <div :class="$style.container">
      <div :class="$style.cell" v-for="(stat, i) in stats" :key="i">
        <div :class="$style.clip">
          <img :src="stat.image" :class="$style.img">
        </div>
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
          image: "../assets/Sponsors/aws.png"
        },
        {
          image: "../assets/Sponsors/av.png"
        },
        {
          image: "../assets/Sponsors/top-coder.png"
        },
        {
          image: "../assets/Sponsors/eligible.png"
        },
        {
          image: "../assets/Sponsors/grab-on.png"
        },
        {
          image: "../assets/Sponsors/hackerrank.png"
        },
        {
          image: "../assets/Sponsors/hackerearth.png"
        },
        {
          image: "../assets/Sponsors/ntd-india.png"
        },
        {
          image: "../assets/Sponsors/uber.png"
        },
        {
          image: "../assets/Sponsors/zebronics.png"
        },
        {
          image: "../assets/Sponsors/oh-campus.png"
        },
      ]
    };
  }
};
</script>

<style module lang="styl">
@import '../styles/theme.styl';
@import '../styles/colors.styl';

$cell-size = 200px

.sponsors
  .cell
    width $cell-size
    height $cell-size

    .clip 
      clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
      background-color white
      width 100%
      height 100%

    .img
      width 75%
      height 75%
      margin: ($cell-size / 8)
      
    &:nth-child(odd)      
      .clip
        float right

    &:nth-child(even)
      .clip
        float left 


  .container
    display grid
    grid-template-columns 200px 200px 200px
    grid-template-rows 200px 
    grid-column-gap 50px
    grid-row-gap 30px
    justify-content space-evenly
</style>