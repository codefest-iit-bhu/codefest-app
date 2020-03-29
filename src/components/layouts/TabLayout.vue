<template>
  <div :class="$style.tabbedWindow">
    <div :class="$style.tabsContainer">
      <div ref="tabWrapper">
        <div
          v-for="(tab, i) in tabs"
          :id="`${idPrefix}_${i}`"
          :key="i"
          :class="[$style.tabWrapper, isActiveTab(i)]"
          :style="tabStyle(i)"
        >
          <div :id="tab.title" :class="$style.tabTitle" @click="toggleTab(i)">
            {{ tab.title }}
          </div>
        </div>
      </div>
    </div>

    <div :class="$style.panelsContainer">
      <div
        v-for="(tab, i) in tabs"
        :key="i"
        :class="[$style.panelWrapper, isActiveTab(i)]"
      >
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
      default: 'tab'
    }
  },
  data() {
    return {
      currentTab: 0
    }
  },
  computed: {
    isActiveTab() {
      return (index) => (index === this.currentTab ? this.$style.active : '')
    }
  },
  methods: {
    toggleTab(index) {
      if (this.tabs.length * 130 > window.innerWidth) this.alignTab(index)
      this.currentTab = index
    },
    tabStyle(index) {
      return {
        left: `${index * 100}px`
      }
    },
    alignTab(index) {
      const tab = document.getElementById(`${this.idPrefix}_${index}`)
      const tabWidth = tab.offsetWidth
      let xDiff = (index - this.currentTab) * (window.innerWidth * 0.2)
      if (xDiff < 0) xDiff = 0
      this.$refs.tabWrapper.style.transform = `translateX(${-xDiff}px)`
    }
  }
}
</script>

<style module lang="stylus">
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
        background: $limeade;
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
        background: $chartreuse;
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
