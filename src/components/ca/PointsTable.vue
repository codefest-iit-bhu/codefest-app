<template>
  <SectionLayout v-show="isLoggedIn && isCampusAmbassador" title="CA Leaderboard" id="container">
    <table :class="[$style.leaderboard, $style[$mq]]" id="leaderboard">
      <thead>
        <tr :class="$style.tablerow">
          <th :class="$style.head">Rank</th>
          <th :class="$style.head">Name</th>
          <th :class="$style.head">CA Score</th>
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
          <td>{{ person.ca_score }}</td>
        </tr>
      </tbody>
    </table>
  </SectionLayout>
</template>

<script>
import API from "@js/api";
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout,
  },
  data() {
    return {
      leaderboard: [],
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    isCampusAmbassador() {
      return this.$store.getters.isCampusAmbassador;
    }
  },
  created() {
    API.fetch("leaderboard/")
      .then(({ data }) => {
        this.leaderboard = data;
      })
      .catch((err) => {
        this.$toasted.global.error_post({
          message: err.message,
        });
      });
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
  box-shadow: 0 0 12px $vermilion inset;
  table-layout: fixed;

  .head {
    font-family: 'Roboto Slab';
    color: $vermilion;
    padding: 12px 0;
    $font-size: 16px;
    border-bottom: 1px solid $vermilion;
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
