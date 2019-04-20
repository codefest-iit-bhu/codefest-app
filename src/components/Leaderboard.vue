<template>
  <SectionLayout title="Leaderboard" id="container">
    <div :class="[$style.leaderboard, $style[$mq]]" id="leaderboard">
      <table>
        <tr :class="$style.tablerow">
          <th :class="[$style.col1, $style.head]">Rank</th>
          <th :class="[$style.col2, $style.head]">Name</th>
          <th :class="[$style.col3, $style.head]">Referrals</th>
        </tr>
        <tr v-for="(person, i) in leaderboard" :key="i" :class="$style.tablerow">
          <td :class="[$style.col1, ]">{{ i + 1 }}</td>
          <td :class="[$style.col2, ]">{{ person.name }}</td>
          <td :class="[$style.col3, ]">{{ person.referral_count }}</td>
        </tr>
      </table>
    </div>
  </SectionLayout>
</template>
<script>
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout
  },
  props: {
    leaderboard: {
      required: true,
      type: Array
    }
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.leaderboard {
  text-align: center;
  margin: auto;
  width: 600px;
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0 0 20px $chartreuse inset;

  .col1, .col3 {
    width: 100px;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 50px;
    }
  }

  .col2 {
    width: 400px;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 200px;
    }
  }

  ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
    width: 300px;
  }

  .head {
    font-family: 'Roboto Slab';
    color: $chartreuse;
    padding: 15px 0;
    font-size: 20px;
    border-bottom: 1px solid $chartreuse;
  }

  .tablerow {
    td {
      font-family: 'Quicksand';
      font-size: 16px;
      padding: 10px 0 0;
      font-weight: 600;
    }
  }
}
</style>
