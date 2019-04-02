<template>
  <div :class="$style.wrapper">
    <AppbarLayout v-bind="this.$attrs"></AppbarLayout>
  </div>
</template>

<script>
import AppbarLayout from "@components/layouts/AppbarLayout";

export default {
  components: {
    AppbarLayout
  }
};
</script>

<style module lang="stylus">
.wrapper {
}
</style>
