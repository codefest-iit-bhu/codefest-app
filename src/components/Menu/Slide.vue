<template>
  <div>
    <SideBar v-bind="this.$attrs" @openSideBar="openSideBar" @closeSideBar="closeSideBar">
      <slot></slot>
    </SideBar>
  </div>
</template>

<script>
import SideBar from "../SideBar";
export default {
  name: "slide",
  components: {
    SideBar: SideBar
  },
  methods: {
    openSideBar() {
      this.$emit("openSideBar");
    },
    closeSideBar() {
      this.$emit("closeSideBar");
    }
  }
};
</script>
