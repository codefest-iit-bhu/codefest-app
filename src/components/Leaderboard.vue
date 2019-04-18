<template>
  <div :class="$style.leaderboard">
    <div :class="[$style.headings,$style.tablerow]">
      <div :class="$style.tablecell">Rank</div>
      <div :class="$style.tablecell">Name</div>
      <div :class="$style.tablecell">Referals</div>
    </div>
    <div :class="[$style.tablerow,$style.positions]" v-for="person in people">
      <div :class="$style.tablecell">{{ person.rank }}</div>
      <div :class="$style.tablecell">{{ person.name }}</div>
      <div :class="$style.tablecell">{{ person.referrals }}</div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      people: [
        {
          name: "Nishant Mittal",
          referrals: 256,
          rank: 1
        },
        {
          name: "ABC",
          referrals: 150,
          rank: 2
        }
      ]
    };
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.leaderboard {
  text-align: center;
  display: grid;
  grid-gap: 20px;
  grid-auto-rows: 40px;
  width: 700px;

  .tablerow {
    display: grid;
    grid-template-columns: 1fr 4fr 4fr;

    .tablecell {
      overflow: hidden;
    }
  }

  .headings {
    font-family: 'Aldo the Apache';
    font-size: 20px;
    color: $chartreuse;
    border-bottom: 1px solid $chartreuse;
  }

  .positions {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: $chartreuse;
    font-size: 18px;
    // border-bottom: 1px solid $chartreuse;
  }
}
</style>
