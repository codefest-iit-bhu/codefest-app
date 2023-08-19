<template>
  <div :class="$style.tabbedWindow">
    <div :class="$style.tabsContainer" >
      <div ref="tabWrapper">
        <div
          :class="[$style.tabWrapper,$style.border, isActiveTab(i)]"
          :id="`${idPrefix}_${i}`"
          v-for="(tab, i) in tabs"
          :key="i"
          :style="tabStyle(i)"
        >
          <div :class="$style.tabTitle" @click="toggleTab(i)" :id="tab.title">
            {{ tab.title }}
          </div>
          <div :class=" $style.back" @click="toggleTab(i)" >
          </div>
        </div>
      </div>
    </div>

    <div :class="$style.panelsContainer">
      <div
        :class="[$style.panelWrapper, isActiveTab(i)]"
        v-for="(tab, i) in tabs"
        :key="i"
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
      type: Array,
    },
    idPrefix: {
      required: false,
      type: String,
      default: "tab",
    },
  },
  data() {
    return {
      currentTab: 0,
    };
  },
  computed: {
    isActiveTab() {
      return (index) => (index === this.currentTab ? this.$style.active : "");
    },
  },
  methods: {
    toggleTab: function(index) {
      if (this.tabs.length * 130 > window.innerWidth) this.alignTab(index);
      this.currentTab = index;
      this.$emit('onToggleTab', this.currentTab); 
    },
    tabStyle: function(index) {
      return {
        left: `${index * 100}px`,
      };
    },
    alignTab: function(index) {
      const tab = document.getElementById(`${this.idPrefix}_${index}`);
      const tabWidth = tab.offsetWidth;
      let xDiff = (index - this.currentTab) * (window.innerWidth * 0.2);
      if (xDiff < 0) xDiff = 0;
      this.$refs.tabWrapper.style.transform = `translateX(${-xDiff}px)`;
    },
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

$tab-width = 130px;
$tab-height = 30px;
$margin= 2px;
.tabbedWindow {
  width: 100%;
  height: 100%;

  .tabsContainer {
    // border-radius: 0 20px 0px 0;
    // clip-path:polygon(14px 0,320px 0,334px 100%,0 100%);
    position: relative;
    overflow-x: hidden;
    overflow-y: hidden;
    width: 100%;
    height: $tab-height+2*$margin;
    float: left;
    bottom: 2.5px;
    z-index :1;

    .tabWrapper {
      width: $tab-width+2*$margin;
      height: $tab-height+2*$margin;
      position: absolute;
      top: 0;
      margin:0px;
      background: rgb(7,249,250);
      clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);

      .tabTitle {
        z-index: 20;
        cursor: pointer;
        background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
        font: 12pt 'Roboto Slab';
        font-weight: 600;
        clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);
        height: $tab-height;
        line-height: 30px;
        width: $tab-width;
        text-align: center;
        color: var(--text-color);
        margin: $margin;
      }
      
    }
    .back{
      cursor: pointer;
      // background: var(--dark-shadow-color);
      font: 12pt 'Roboto Slab';
      font-weight: 600;
      clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);
      // clip-path:polygon(10px 0,$tab-width 0,100% 100%,0 100%);
      height: $tab-height;
      line-height: 30px;
      width: $tab-width;
      text-align: center;
      color: var(--text-color);
      margin: $margin;
      background: rgba(0,0,0,0.85);
      bottom:$tab-height+$margin;
      position:relative;
      z-index: -1;
    }

    .active {
      .tabTitle {
        background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
        color: $white;
        z-index: 25;
      }
      .back{
        height:$tab-height+$margin;
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
      border-radius: 0 0 10px 10px;
      background: var(--text-color-inverted);
    }

    .active .tabContent {
      display: block;
    }
  }
}
</style>
