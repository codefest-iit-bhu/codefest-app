<template>
    <table :class="[$style.points, $style[$mq]]" id="points">
      <thead>
        <tr :class="$style.tablerow">
          <th :class="$style.head">Rank</th>
          <th :class="$style.head">Name</th>
          <th :class="$style.head">Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(person, i) in cas" :key="i" :class="$style.tablerow">
          <td>{{ i + 1 }}</td>
          <td>{{ person.name }}</td>
          <td>{{ person.points }}</td>
        </tr>
      </tbody>
    </table>
</template>

<script>
import API from "@js/api";

export default {
  data() {
    return {
      cas: []
    };
  },
  created() {
    API.fetch("cas/")
      .then(({ data }) => {
        this.cas = data;
      })
      .catch(err => {
        this.$toasted.global.error_post({
          message: err.message
        });
      });
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.points{
  text-align: center;
  margin: auto;
  width: 100%;
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0 0 12px $chartreuse inset;
  table-layout: fixed;

  .head {
    font-family: 'Roboto Slab';
    color: $chartreuse;
    padding: 12px 0;
    font-size: 16px;
    border-bottom: 1px solid $chartreuse;
  }

  .tablerow {
    td {
      font-family: 'Quicksand';
      font-size: 16px;
      padding: 12px 0;
      font-weight: 600;
    }
  }
}
</style>