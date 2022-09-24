<template>
  <div :class="$style.container">
    <table :class="[$style.points, $style[$mq]]" id="points">
      <thead>
        <tr :class="$style.tablerow">
          <th :class="$style.head">Rank</th>
          <th :class="$style.head">ID</th>
          <th :class="$style.head">Name</th>
          <th :class="$style.head">Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(person, i) in cas" :key="i" :class="$style.tablerow">
          <td>{{ i + 1 }}</td>
          <td>{{ person.caid }}</td>
          <td>{{ person.name }}</td>
          <td>{{ person.points }}</td>
        </tr>
      </tbody>
    </table>
    <br />
    <span :class="$style.lastUpdated"> Last Updated : {{ last_updated }}</span>
  </div>
</template>

<script>
import API from "@js/api";

export default {
  data() {
    return {
      cas: [],
      last_updated: "",
    };
  },
  created() {
    API.fetch("cas/")
      .then(({ data }) => {
        this.cas = data;
        this.last_updated = this.cas[0].last_updated;
        console.log(this.last_updated);
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
.points{
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

.container{
  text-align: center;

  .lastUpdated {
    display: inline-block;
    box-shadow: 0 0 12px $waterloo inset;
    padding: 15px 25px;
    font-weight: 600;
    border-radius: 10px;
    margin: auto;
    font-family: 'QuickSand';
    color: white;
  }
}
</style>
