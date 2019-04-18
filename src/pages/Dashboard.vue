<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :isSideNavigationShown="true">
      <li :class="{[$style.active]: isHomeView}" slot="dashboard">
        <router-link to="/dashboard">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Profile
        </router-link>
      </li>
      <li :class="{[$style.active]: isEventsView}" slot="dashboard">
        <router-link to="/dashboard/events">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Events
        </router-link>
      </li>
    </AppBar>
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
    isEventsView: false
  },
  created() {
    API.fetch("profile/")
      .then(({ data }) => {
        if (!data.is_profile_complete) {
          this.$router.replace("/profile/edit");
        }
        console.log(data);
        this.profile = data;
      })
      .catch(console.log);
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

.root {
  height: 100%;

  .wrapper {
    width: 80%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    font: 500 18px 'Quicksand';
    padding: 100px 0;
  }

  .active {
    a {
      color: $chartreuse;
      font-weight: bold;

      span {
        color: $white;
        animation: neon-text 1s ease-in-out infinite alternate;
      }
    }
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
