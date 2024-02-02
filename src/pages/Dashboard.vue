<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :shouldShowSideNavigation="true">
      <li slot="dashboard">
        <router-link to="/">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Home
        </router-link>
      </li>
      <li :class="{ [$style.active]: isHomeView }" slot="dashboard">
        <router-link to="/dashboard">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Profile
        </router-link>
      </li>
      <li :class="{ [$style.active]: isEventsView }" slot="dashboard">
        <router-link to="/dashboard/events">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          My Teams
        </router-link>
      </li>
    </AppBar>
    <main :class="$style.wrapper">
      <DashboardEvent v-if="isEventsView" />
      <DashboardProfile :profile="profile" v-if="isHomeView" />
      <Referral v-if="isLeaderboardView" />
    </main>
    <Footer />
  </div>
</template>

<script>
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const DashboardEvent = () => import("@components/dashboard/DashboardEvent");
const DashboardProfile = () => import("@components/dashboard/DashboardProfile");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    DashboardEvent,
    DashboardProfile,
    Footer,
  },
  data() {
    return {
      profile: {},
    };
  },
  props: {
    isHomeView: false,
    isEventsView: false,
    isLeaderboardView: false,
  },
  created() {
    API.fetch("profile/")
      .then(({ data }) => {
        if (!data.is_profile_complete) {
          this.$router.replace("/profile/edit");
        }
        this.profile = data;
      })
      .catch((err) => {
        this.$toasted.global.error_post({
          message: err.message,
        });
      });
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

.root {
  height: 100vh;

  .wrapper {
    width: 80%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    font: 500 18px 'Quicksand';
    padding: 100px 0;
  }

  li {
    &.active {
      a {
        span {
          color: var(--text-color) !important;
        }
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
