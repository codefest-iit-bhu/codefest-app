<template>
  <SectionLayout title="Prizes" id="prizes">
    <GridLayout columns="3">
      <CardLayout>
        <img src="@assets/faq.svg" slot="header">
        <h3 slot="content">2nd position - $30K</h3>
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
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';
</style>
