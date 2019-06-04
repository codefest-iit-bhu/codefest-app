<template>
  <div :class="[$style.floatBtn, animateClass, $style[$mq]]">
    <button id="devfolio-apply-now" ref="devfolioBtn" @click="registerDefault">
      <svg
        class="logo"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 115.46 123.46"
        style="height:24px;width:24px;margin-right:8px;"
      >
        <path
          d="M115.46 68a55.43 55.43 0 0 1-50.85 55.11S28.12 124 16 123a12.6 12.6 0 0 1-10.09-7.5 15.85 15.85 0 0 0 5.36 1.5c4 .34 10.72.51 20.13.51 13.82 0 28.84-.38 29-.38h.26a60.14 60.14 0 0 0 54.72-52.47c.051.05.08 2.18.08 3.34z"
        ></path>
        <path
          d="M110.93 55.87A55.43 55.43 0 01 60.08 111s-36.48.92-48.58-.12C5 110.29.15 104.22 0 97.52l.2-83.84C.38 7 5.26.94 11.76.41c12.11-1 48.59.12 48.59.12a55.41 55.41 0 0 1 50.58 55.34z"
        ></path>
      </svg>Apply with Devfolio
    </button>
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

.floatBtn {
  /* stickWithSpace(bottom: 30px, right: 30px); */
  width: $btn-width;
  height: $btn-height;
  border-radius: 50px;
  background: $black;
  margin: 10px auto;
  border: 2px solid $chartreuse;
  text-align: center;
  color: $chartreuse;
  font-family: 'Roboto Slab';
  box-shadow: inset 0px 0px 5px $chartreuse;
  text-align: center;
  overflow: hidden;

  &:hover {
    box-shadow: inset 0px 0px 10px $chartreuse;
  }

  :global {
    #devfolio-apply-now {
      -ms-flex-align: center;
      -webkit-box-align: center;
      padding: 10px 20px;
      align-items: center;
      background: none;
      cursor: pointer;
      color: $white;
      border: none;
      display: -ms-flexbox;
      display: -webkit-box;
      display: flex;
      font-size: 18px;
      font-weight: 600;
      text-align: center;
      text-transform: none;

      &:not([disabled]) {
        cursor: pointer;
      }

      .logo {
        fill: $white;
      }
    }
  }
}
</style>