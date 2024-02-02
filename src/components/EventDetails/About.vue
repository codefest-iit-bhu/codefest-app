<template>
  <SectionLayout title="About" id="about">
    <p v-for="para in sentences">{{ para }}</p>
  </SectionLayout>
</template>

<script>
import events from "@store/events";
const SectionLayout = () => import("@components/layouts/SectionLayout");

export default {
  components: {
    SectionLayout
  },
  props: {
    about: {
      type: String,
      default: ""
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
  }
};
</script>

<style module lang="stylus"></style>
