<template>
  <SectionLayout title="Leaderboard" id="container">
    <table :class="[$style.leaderboard, $style[$mq]]" id="leaderboard">
      <thead>
        <tr :class="$style.tablerow">
          <th :class="$style.head">Rank</th>
          <th :class="$style.head">Name</th>
          <th :class="$style.head">Referrals</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(person, i) in leaderboard"
          :key="i"
          :class="$style.tablerow"
        >
          <td>{{ i + 1 }}</td>
          <td>{{ person.name }}</td>
          <td>{{ person.referral_count }}</td>
        </tr>
      </tbody>
    </table>
  </SectionLayout>
</template>

<script>
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout,
  },
  props: {
    leaderboard: {
      required: true,
      type: Array,
    },
  },
};
</script>
<style module lang="stylus">

.leaderboard {
  text-align: center;
  margin: auto;
  width: 100%;
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0 0 12px $waterloo inset;
  table-layout: fixed;

  .head {
    font-family: 'Roboto Slab';
    color: $waterloo;
    padding: 12px 0;
    $font-size: 16px;
    border-bottom: 1px solid $waterloo;
  }

  .tablerow {
    td {
      font-family: 'Quicksand';
      $font-size: 16px;
      padding: 12px 0;
      font-weight: 600;
    }
  }
}
</style>
