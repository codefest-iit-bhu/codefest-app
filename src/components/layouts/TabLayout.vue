<template>
  <div :class="$style.tabbedWindow">
    <div :class="$style.tabsContainer">
      <div ref="tabWrapper">
        <div
          :class="  [$style.tabWrapper, isActiveTab(i)]"
          :id="`${idPrefix}_${i}`"
          v-for="(tab, i) in tabs"
          :key="i"
          :style="tabStyle(i)"
        >
          <div :class="$style.tabTitle" @click="toggleTab(i);" :id="tab.title">{{ tab.title }}</div>
        </div>
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
      if (this.tabs.length * 130 > window.innerWidth) this.alignTab(index);
      this.currentTab = index;
    },
    tabStyle: function(index) {
      return {
        left: `${index * 100}px`
      };
    },
    alignTab: function(index) {
      const tab = document.getElementById(`${this.idPrefix}_${index}`);
      const tabWidth = tab.offsetWidth;
      let xDiff = (index - this.currentTab) * (window.innerWidth * 0.2);
      if (xDiff < 0) xDiff = 0;
      this.$refs.tabWrapper.style.transform = `translateX(${-xDiff}px)`;
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

$tab-width = 130px;
$tab-height = 30px;

.tabbedWindow {
  width: 100%;
  height: 100%;

  .tabsContainer {
    border-radius: 0 20px 0px 0;
    position: relative;
    overflow-x: hidden;
    overflow-y: hidden;
    width: 100%;
    height: $tab-height;
    float: left;

    .tabWrapper {
      width: 100%;
      height: $tab-height;
      position: absolute;
      top: 0;

      .tabTitle {
        z-index: 20;
        cursor: pointer;
        background: $crown-of-thorns;
        font: 12pt 'Roboto Slab';
        font-weight: 600;
        clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);
        height: $tab-height;
        line-height: 30px;
        width: $tab-width;
        text-align: center;
        color: $white;
      }
    }

    .active {
      .tabTitle {
        background: $vermilion;
        color: $black;
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
      border: 1px solid $vermilion;
      border-radius: 0 0 10px 10px;
      box-shadow: inset 0px -2px 15px $vermilion;
      background: var(--text-color-inverted);
    }

    .active .tabContent {
      display: block;
    }
  }
}
</style>