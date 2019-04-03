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

      <mq-layout :mq="['xs', 'sm',]">
        <Slide :isOpen="isSidebarOpen" @closeSideBar="onCloseSideBar" :width="sideBarWidth">
          <img src="@assets/haxplore/text-based-green.svg" :class="$style.sidebarLogo">
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
    }
  }

  .sidebar {
    margin: auto;

    a {
      font: 16px 'Roboto Slab';
    }
  }

  &.xs, &.sm {
    .sidebar {
      .sidebarLogo {
        width: 250px;
        margin: auto;
      }

      ul {
        padding-top: 10px;

        li {
          margin: 5px auto;
          display: block !important;

          a {
            color: $white;
            margin: auto;
            text-decoration: none;
            transition: 0.5s;
          }

          a span {
            display: none;
          }

          a:hover {
            color: $chartreuse;
          }
        }
      }
    }
  }

  &.md, &.lg, &.xl {
    .sidebar {
      position: fixed;
      top: calc(50% - 75px);
      right: 20px;
      max-width: 230px;
      font-size: 18px;

      ul {
        padding: 0;
        list-style: none;

        li {
          margin-bottom: 20px;
          padding-right: 5px;

          a {
            font: 14px 'Roboto Slab';
            color: $white;
            text-decoration: none;
            cursor: pointer;
            transition: 0.5s;

            span {
              margin-right: 5px;
              color: $white;
              font-size: 14px;
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
    }
  }
}
</style>
