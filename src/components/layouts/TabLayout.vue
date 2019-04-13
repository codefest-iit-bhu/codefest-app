<template>
  <div :class="$style.tabbedWindow">
    <div :class="$style.tabsContainer">
      <div
        :class="  [$style.tabWrapper, isActiveTab(i)]"
        :id="`${idPrefix}_${i}`"
        v-for="(tab, i) in tabs"
        :key="i"
        :style="tabStyle(i)"
      >
        <div :class="$style.tabTitle" @click="toggleTab(i)">{{ tab.title }}</div>
      </div>
    </div>

    <div :class="$style.panelsContainer">
      <div :class="[$style.panelWrapper, isActiveTab(i)]" v-for="(tab, i) in tabs" :key="i">
        <div :class="$style.tabContent">
          <slot :name="tab.name"></slot>
        </div>
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

.tabbedWindow {
  width: 100%;
  height: 100%;

  .tabsContainer {
    border-radius: 0 20px 0px 0;
    position: relative;
    overflow-x: scroll;
    width: 100%;
    height: $tab-height;
    float: left;
    -ms-overflow-style: none;
    scrollbar-width: none;

    &::-webkit-scrollbar {
      display: none;
    }

    .tabWrapper {
      width: 100%;
      height: $tab-height;
      position: absolute;
      top: 0;

      .tabTitle {
        z-index: 20;
        cursor: pointer;
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
    }

    .active {
      .tabTitle {
        background: $limeade;
        color: white;
        z-index: 25;
      }
    }
  }

  .panelsContainer {
    margin: 0;
    padding: 0;

    .tabContent {
      display: none;
      position: relative;
      top: $tab-height;
      border: 1px solid $limeade;
      border-radius: 0 0 10px 10px;
      box-shadow: inset 0px -2px 15px $chartreuse;
      background: $cod-gray;
    }

    .active .tabContent {
      display: block;
    }
  }
}
</style>
