<template>
  <div :class="$style.wrapper">
    <AppbarLayout v-bind="this.$attrs">
      <!-- Show appbar navigations only on lg+ devices. -->
      <li :class="$style.link" slot="left" v-if="['lg', 'xl'].includes(this.$mq)">
        <router-link to="/events">
          Events
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
        </router-link>
      </li>
      <li :class="$style.link" slot="right" v-if="['lg', 'xl'].includes(this.$mq)">
        <a href="https://goo.gl/DrCFHB" target="_blank">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>Brochure
        </a>
      </li>
      <li :class="$style.link" slot="right" v-if="['lg', 'xl'].includes(this.$mq)">
        <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Sponsor Us
        </a>
      </li>
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm', 'md'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
    </AppbarLayout>
    <mq-layout :mq="['xs', 'sm', 'md']">
      <!-- Show sidebar only for smaller devices. -->
      <div :class="$style.sidebar" ref="sidebar">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <li :class="$style.link">
            <router-link to="/events">Events</router-link>
          </li>

          <li :class="$style.link">
            <a href="https://goo.gl/DrCFHB" target="_blank">Brochure</a>
          </li>
          <li :class="$style.link">
            <a href="https://goo.gl/forms/RyjmY7i002oUHivu2" target="_blank">Sponsor Us</a>
          </li>
        </Slide>
      </div>
    </mq-layout>
  </div>
</template>
<script>
import AppbarLayout from "@components/layouts/AppbarLayout";
import Slide from "@components/Menu/Slide";

export default {
  components: {
    AppbarLayout,
    Slide
  },
  data() {
    return {
      isSidebarOpen: false
    };
  },
  computed: {
    sideBarWidth() {
      if (this.$mq === "xs" || this.$mq === "sm") return window.innerWidth;
      else return 300;
    }
  },
  methods: {
    openSidebar() {
      this.isSidebarOpen = true;
    },
    onCloseSideBar() {
      this.isSidebarOpen = false;
    }
  }
};
</script>
<style module lang="stylus">
@require '~@styles/mixins';
@require '~@styles/theme';

.wrapper {
  li {
    display: inline-block;
  }

  .link {
    padding-top: 10px;

    a {
      color: $white;
      padding: 10px 10px;
      margin-left: 5px;
      text-decoration: none;
      transition: 0.5s;
    }

    a span {
      margin-right: 15px;
      color: $white;
      opacity: 0;
      font-size: 16px;
    }

    a:hover {
      color: $chartreuse;
    }

    a:hover span {
      opacity: 1;
      color: $white;
      animation: neon-text 1s ease-in-out infinite alternate;
    }
  }

  #toggleSidebar {
    margin: 5px 10px;

    a {
      text-decoration: none;
      color: $white;
    }
  }
}

.shown {
}

.sidebar {
  margin: 5px;

  .link {
    font: 14px 'Roboto Slab';
    display: block;

    a {
      color: $white;
      padding: 10px 10px;
      margin-left: 5px;
      text-decoration: none;
      transition: 0.5s;
    }

    a:hover {
      color: $chartreuse;
    }
  }

  .link:hover {
    background: rgb(63, 63, 65);
  }
}
</style>
