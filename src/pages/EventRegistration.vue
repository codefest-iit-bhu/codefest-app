<template>
    <div :class="[$style.root, $style[$mq]]">
      <AppBar/>
      <main :class="$style.wrapper">
        <EventTeam :event="eventDetails"/>
      </main>
      <Footer />
    </div>
  </template>
  
  <script>
  import API from "@js/api";
  
  const AppBar = () => import("@components/Menu/AppBar");
  const EventTeam = () => import("@components/dashboard/EventTeam");
  const Footer = () => import("@components/Footer");
  
  export default {
    components: {
      AppBar,
      EventTeam,
      Footer,
    },
    data() {
      return {
        eventDetails: {},
      };
    },
    created() {
      console.log(this.$route.params.id);
      API.fetch(`events/${this.$route.params.id}/`)
        .then(({data}) => {
          this.eventDetails = data;
        })
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
      padding: 200px 0;
      display: flex;
      justify-content: center;
      align-items: center;
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
  