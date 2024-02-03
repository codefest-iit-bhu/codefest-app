<template>
  <SectionLayout :title="title">
    <div v-html="html"></div>
  </SectionLayout>
</template>

<script>
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout
  },
  props: {
    html: {
      type: String,
      default: ""
    },
    title:{
      type: String,
      default: "",
    }
  },
  computed: {
    sentences() {
      const sentencesArray = this.about.split('.');
      const result = [];
      for (let i = 0; i < sentencesArray.length; i += 2) {
        const currentSentence = sentencesArray[i] + (sentencesArray[i + 1] ? '. ' + sentencesArray[i + 1] + '.' : '.');
        result.push(currentSentence);
      }
      return result;
    }
  },
};
</script>

<style module lang="stylus"></style>
