<template>
  <div :class="$style.tabsContainer">
    <div
      :class="[$style.tabWrapper, isActiveTab(i)]"
      :id="`${idPrefix}_${i}`"
      v-for="(tab, i) in tabs"
      :key="i"
    >
      <div :class="$style.tabTitle" @click="toggleTab(i)" :style="tabStyle(i)">{{ tab.title }}</div>
      <div :class="$style.tabContent">
        <slot :name="tab.name"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tabs: {
      required: true,
      type: Array
    },
    idPrefix: {
      required: false,
      type: String,
      default: "tab"
    }
  },
  data() {
    return {
      currentTab: 0
    };
  },
  computed: {
    isActiveTab() {
      return index => (index === this.currentTab ? this.$style.active : "");
    }
  },
  methods: {
    toggleTab: function(index) {
      this.currentTab = index;
    },
    tabStyle: function(index) {
      return {
        left: `${index * 120}px`
      };
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

$tab-width = 150px;
$tab-height = 30px;

.tabsContainer {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

  .tabWrapper {
    width: 100%;
    height: 100%;
    display: inline;

    .tabTitle {
      z-index: 20;
      cursor: pointer;
      position: absolute;
      top: 0;
      background: $chartreuse;
      font-family: 'Roboto Slab';
      font-weight: 500;
      clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);
      height: $tab-height;
      line-height: 30px;
      width: $tab-width;
      text-align: center;
      color: $black;
    }

    .tabContent {
      display: none;
      position: relative;
      top: $tab-height;
      border: 1px solid $chartreuse;
      border-radius: 0 0 10px 10px;
      box-shadow: inset 0px 0px 20px $chartreuse;
      background: $cod-gray;
    }

    &.active {
      .tabTitle {
        background: $limeade;
        color: white;
        z-index: 25;
      }

      .tabContent {
        display: block;
      }
    }
  }
}
</style>
