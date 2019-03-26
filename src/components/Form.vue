<template>
  <form :class="$style.form">
    <div v-for="(i, field) in form.fields" :key="i" :class="$style.fieldContainer">
      <label v-bind:for="field.name" :class="$style.label">{{field.label}}</label>
      <input
        v-bind:type="field.type"
        v-bind:name="field.name"
        :class="$style.field"
        :id="field.name"
      >
    </div>
    <div>
      <button type="submit" value=">" :class="$style.submit">
        <i class="fas fa-arrow-circle-right"></i>
      </button>
    </div>
  </form>
</template>

<script>
export default {
  props: ["form", "id"],
  methtods: {},
  mounted() {
    document.getElementsByTagName("input")[0].focus();
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';

$cell-collapsed-size = 150px;

.form {
  margin: 50px;
}

.fieldContainer {
  width: 100%;
  margin-bottom: 20px;
  text-align: right;
}

.field {
  clear: both;
  height: 30px;
  color: white;
  border: 0;
  outline: 0;
  max-width: 400px;
  width: 100%;
  font-size: 16px;
  background: #fff2;
  border-radius: 5px;
  padding-left: 5px;
}

.label {
  float: left;
  color: white;
  text-align: right;
  height: 30px;
}

.submit {
  border: 0;
  background: transparent;
  color: $white;
  border-radius: 100%;
  font-size: 40px;
  height: 40px;
  width: 40px;
  cursor: pointer;

  &:hover {
    color: $chartreuse;
  }
}
</style>
