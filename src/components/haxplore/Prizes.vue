<template>
  <SectionLayout title="Prizes" id="prizes">
    <GridLayout
      :columns="$mq | mq({xs: 1, sm: 2, md: 3, lg: 3, xl: 3})"
      itemWidth="300px"
      itemHeight="300px"
    >
      <CardLayout v-for="(stat,i) in this.stats" :key="i" :slot="`item${i}`" isRounded="True">
        <img src="stat.image" slot="header">
        <h3 slot="content">{{ stat.text }}</h3>
      </CardLayout>
    </GridLayout>
  </SectionLayout>
</template>

<script>
import SectionLayout from "@components/layouts/SectionLayout";
import GridLayout from "@components/layouts/GridLayout";
import CardLayout from "@components/layouts/CardLayout";

export default {
  components: {
    SectionLayout,
    GridLayout,
    CardLayout
  },
  data() {
    return {
      stats: [
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "1st Prize"
        },
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "2nd Prize"
        },
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "3rd Prize"
        },
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "4th Prize"
        },
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "5th Prize"
        },
        {
          name: "Prize Money",
          image: "@assets/Lookback/rupee.png",
          text: "6th, 7th, 8th Prize"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';
</style>
