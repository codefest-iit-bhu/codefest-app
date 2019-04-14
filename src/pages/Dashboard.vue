<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :isSideNavigationShown="false"/>
    <main :class="$style.wrapper">
      <DashboardEvent v-if="isEventsView"/>
      <DashboardProfile :profile="profile" v-if="isHomeView"/>
    </main>
    <Footer/>
  </div>
</template>

<script>
import API from "@js/api";

import AppBar from "@components/Menu/AppBar";
import DashboardEvent from "@components/dashboard/DashboardEvent";
import DashboardProfile from "@components/dashboard/DashboardProfile";
import Footer from "@components/Footer";

export default {
  components: {
    AppBar,
    DashboardEvent,
    DashboardProfile,
    Footer
  },
  data() {
    return {
      profile: {}
    };
  },
  props: {
    isHomeView: false,
    isProfileEditView: false,
    isEventsView: false
  },
  created() {
    API.fetch("profile/")
      .then(({ data }) => {
        if (!data.is_profile_complete) {
          console.log("Not Complete!");
        }
        console.log(data);
        this.profile = data;
      })
      .catch(console.log);
  }
};
</script>

<style module lang="stylus">
@require '~@styles/mixins';

.root {
  height: 100%;

  .wrapper {
    width: 80%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    font: 500 18px 'Quicksand';
    padding: 140px 0 100px;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
