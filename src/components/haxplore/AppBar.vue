<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <li :id="$style.toggleSidebar" slot="left" v-if="['xs', 'sm'].includes(this.$mq)">
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
    </AppbarLayout>
    <div :class="$style.sidebar" ref="sidebar">
      <mq-layout mq="md+">
        <slot></slot>
      </mq-layout>

      <mq-layout :mq="['xs', 'sm']">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <img src="@assets/haxplore/logo-text.svg" :class="$style.sidebarLogo">
          <slot></slot>
        </Slide>
      </mq-layout>
    </div>
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
  #toggleSidebar {
    margin: 5px 10px;

    a {
      text-decoration: none;
      color: $white;
      text-decoration: none;
      color: $white;
      transition: 0.5s;
    }
  }

  .sidebar {
    margin: 0 auto;

    ul {
      list-style: none;

      li {
        margin: 20px auto;
        display: block !important;

        a {
          font: 500 18px 'Roboto Slab';
          color: $white;
          text-decoration: none;
          cursor: pointer;

          span {
            color: $white;
            font-size: 14px;
            margin-right: 5px;
          }

          &:hover {
            color: $chartreuse;
          }
        }

        &.active {
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
    }

    .sidebarLogo {
      width: 250px;
      margin: auto;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      ul {
        padding-top: 10px;
      }
    }

    ~/.md ^[1..-1], ~/.lg ^[1..-1], ~/.xl ^[1..-1] {
      position: fixed;
      right: 20px;
      width: 150px;
      padding: 20px;
      display: flex;
      flex-flow: column;
      justify-content: space-around;
      height: 100%;
    }
  }
}
</style>
