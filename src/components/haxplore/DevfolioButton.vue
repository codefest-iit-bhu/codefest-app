<template>
  <div :class="$style.link">
    <div :class="$style.linkText">
      <h4>Registrations will be live soon</h4>
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

<style module lang="stylus">
$btn-height = 65px;
$btn-width = 250px;

.link {
  margin: auto;
  margin-top: 30px;
  max-width: 350px;
  height: auto;
  padding: 24px;
  border-radius: 50px 0px 50px 0px;
  box-shadow: var(--box-shadow);
  text-align: center;
  cursor: pointer;

  .linkText {
    color: var(--text-color);
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Roboto Slab';
      $font-size: 20px;
      margin: 0;
    }
  }
}

.floatBtn {
  /* stickWithSpace(bottom: 30px, right: 30px); */
  width: $btn-width;
  height: $btn-height;
  border-radius: 50px;
  background: $black;
  margin: 10px auto;
  border: 2px solid $vermilion;
  padding-top: 8px;
  text-align: center;
  color: $vermilion;
  font-family: 'Roboto Slab';
  box-shadow: inset 0px 0px 5px $vermilion;
  overflow: hidden;

  &:hover {
    box-shadow: inset 0px 0px 10px $vermilion;
  }

  :global {
    #devfolio-apply-now {
      -ms-flex-align: center;
      -webkit-box-align: center;
      padding: 10px 20px;
      /* align-items: center; */
      background: none;
      /* cursor: pointer; */
      color: $white;
      border: none;
      display: -ms-flexbox;
      display: -webkit-box;
      /* display: flex; */
      $font-size: 18px;
      font-weight: 600;
      text-align: center;
      text-transform: none;

      &:not([disabled]) {
        /* cursor: pointer; */
      }

      .logo {
        fill: $white;
      }
    }
  }
}
</style>
