<template>
  <div :class="$style.link">
    <div :class="$style.linkText">
      <h4>Applications Closed</h4>
    </div>
  </div>
</template>

<script>
import { isMinimal } from "@js/utils";

export default {
  props: {
    devfolioKey: {
      type: String,
      default: "haxplore"
    }
  },
  computed: {
    animateClass() {
      return isMinimal(this.$mq) ? "" : this.$style.animate;
    }
  },
  methods: {
    registerDefault() {
      window.open(
        `https://devfolio.co/external-apply/${this.devfolioKey}`,
        "_blank"
      );
    }
  },
  mounted() {
    this.$emit("mounted");
  }
};
</script>

<style module lang = "stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

$btn-height = 65px;
$btn-width = 250px;

.link {
  margin: auto;
  width: 290px;
  height: auto;
  padding: 24px;
  border-radius: 50px;
  border: 2px solid $chartreuse;
  text-align: center;
  cursor: pointer;

  .linkText {
    color: $black;
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Viga';
      font-size: 20px;
      margin: 0;
    }
  }

  &:hover {
    box-shadow: inset 0px 0px 10px $chartreuse;
  }
}

.floatBtn {
  /* stickWithSpace(bottom: 30px, right: 30px); */
  width: $btn-width;
  height: $btn-height;
  border-radius: 50px;
  background: $white;
  margin: 10px auto;
  border: 2px solid $chartreuse;
  padding-top: 8px;
  text-align: center;
  color: $chartreuse;
  font-family: 'Roboto Slab';
  box-shadow: inset 0px 0px 5px $chartreuse;
  overflow: hidden;

  &:hover {
    box-shadow: inset 0px 0px 10px $chartreuse;
  }

  :global {
    #devfolio-apply-now {
      -ms-flex-align: center;
      -webkit-box-align: center;
      padding: 10px 20px;
      /* align-items: center; */
      background: none;
      /* cursor: pointer; */
      color: $black;
      border: none;
      display: -ms-flexbox;
      display: -webkit-box;
      /* display: flex; */
      font-size: 18px;
      font-weight: 600;
      text-align: center;
      text-transform: none;

      &:not([disabled]) {
        /* cursor: pointer; */
      }

      .logo {
        fill: $black;
      }
    }
  }
}
</style>