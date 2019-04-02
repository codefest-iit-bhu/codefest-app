<template>
  <div>
    <SectionLayout title="Sponsors">
      <Sponsors/>
    </SectionLayout>
    <FloatingButton text="Coming soon"/>
  </div>
</template>

<script>
import FloatingButton from "@components/FloatingButton";
import Sponsors from "@components/Sponsors";
import SectionLayout from "@components/layouts/SectionLayout";
export default {
  components: {
    FloatingButton,
    Sponsors,
    SectionLayout
  }
};
</script>

<style module lang="stylus">
</style>
