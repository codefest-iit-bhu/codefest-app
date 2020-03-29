<template>
  <div :class="[$style.wrapper, $style[$mq]]">
    <AppbarLayout v-bind="this.$attrs">
      <mq-layout slot="left" mq="md+">
        <li :class="$style.link">
          <n-link to="/events">
            Events
          </n-link>
        </li>
        <!-- <li :class="$style.link" slot="left" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <n-link to="/ca">
          CA
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </n-link>
      </li> -->
        <!-- <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <n-link to="/team">
          Team
          <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span>
        </n-link>
      </li> -->
        <!-- <li :class="$style.link" slot="right" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
        <n-link to="/referral">
          <span class="fa fa-circle fa-xs" aria-hidden="true"></span>
          Referrals
        </n-link>
      </li> -->
      </mq-layout>
      <mq-layout slot="right" mq="md+">
        <li v-show="showDashboardActions" :class="$style.link">
          <n-link to="/dashboard">
            <i class="fas fa-id-badge" title="Dashboard"></i>
            <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
          </n-link>
        </li>
        <li v-show="showDashboardActions" :class="$style.link">
          <a @click="authLogout">
            <i class="fas fa-power-off" title="Logout"></i>
            <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
          </a>
        </li>
        <li v-show="!showDashboardActions" :class="$style.link">
          <n-link to="/login">
            <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
            Login
          </n-link>
        </li>
      </mq-layout>
      <li
        v-if="['xs', 'sm'].includes(this.$mq)"
        :id="$style.toggleSidebar"
        slot="left"
      >
        <a class="bm-toggle" @click="openSidebar">
          <i class="fa fa-bars"></i>
        </a>
      </li>
      <n-link slot="notch" to="/">
        <img src="~assets/white-cf20-logo.svg" @click="clickNotch" />
      </n-link>
    </AppbarLayout>
    <div ref="sidebar" :class="$style.sidebar">
      <SectionSidebar
        v-if="['md', 'lg', 'xl', 'xxl'].includes($mq)"
        v-bind="$attrs"
      >
        <template v-for="slot in Object.keys($slots)">
          <slot :name="slot"></slot>
        </template>
      </SectionSidebar>
      <mq-layout :mq="['xs', 'sm']">
        <Slide
          :is-open="isSidebarOpen"
          :width="sideBarWidth"
          @closeSideBar="onCloseSideBar"
        >
          <ul :class="$style.sidebarList">
            <li :class="$style.link">
              <n-link to="/events">Events</n-link>
              <div :class="$style.subList">
                <slot name="events"></slot>
              </div>
            </li>
            <li :class="$style.link">
              <n-link to="/haxplore">
                HaXplore
                <!-- <span class="fa fa-circle fa-xs" :class="$style.awesome" aria-hidden="true"></span> -->
              </n-link>
            </li>
            <!-- <li :class="$style.link">
              <n-link to="/ca">CA</n-link>
            </li> -->
            <!-- <li :class="$style.link">
              <n-link to="/team">Team</n-link>
            </li> -->
            <!-- <li :class="$style.link">
              <n-link to="/referral">Referrals</n-link>
            </li> -->
            <li v-show="showDashboardActions" :class="$style.link">
              <n-link to="/dashboard">
                Dashboard
                <div :class="$style.subList">
                  <slot name="dashboard"></slot>
                </div>
              </n-link>
            </li>
            <li v-show="!showDashboardActions" :class="$style.link">
              <n-link to="/login">Login / Register</n-link>
            </li>
            <li v-show="showDashboardActions" :class="$style.link">
              <a @click="authLogout">Logout</a>
            </li>
          </ul>
        </Slide>
      </mq-layout>
    </div>
  </div>
</template>

<script>
import { isMinimal } from '@js/utils'

const AppbarLayout = () => import('@components/layouts/AppbarLayout')
const SectionSidebar = () => import('@components/SectionSidebar')
const Slide = () => import('@components/Menu/Slide')

export default {
  components: {
    AppbarLayout,
    SectionSidebar,
    Slide
  },
  data() {
    return {
      isSidebarOpen: false
    }
  },
  computed: {
    sideBarWidth() {
      if (isMinimal(this.$mq) && process.client) return window.innerWidth
      else return 300
    },
    showDashboardActions() {
      return this.$store.getters.isLoggedIn
    }
  },
  mounted() {
    const { doHideOnIdle } = this.$data
    this.isSideNavigationIdle = false
    if (doHideOnIdle) window.addEventListener('scroll', this.handleScroll)
    else window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    openSidebar() {
      this.isSidebarOpen = true
    },
    onCloseSideBar() {
      this.isSidebarOpen = false
    },
    clickNotch() {
      if (this.$route.name === '~') this.$emit('scrollTop')
    },
    authLogout() {
      this.$store.dispatch('logout')
      if (this.$route.meta.requiresAuth) this.$router.push({ name: '~' })
    }
  }
}
</script>

<style module lang="stylus">
@require '~@styles/anims';

.wrapper {
  li {
    display: inline-block;
  }

  .link {
    margin-top: 10px;

    .awesome {
      border-radius: 10px;
    }

    a {
      cursor: pointer;
      height: inherit;
      color: $white;
      font-weight: 600;
      $font-size: 20px;
      letter-spacing: 0.8px;
      padding: 0 10px;
      text-decoration: none;
      transition: 0.5s;
      vertical-align: middle;
    }

    a span {
      margin-right: 15px;
      color: $white;
      opacity: 0;
      $font-size: 16px;
    }

    ~/.xs ^[1..-1] a, ~/.sm ^[1..-1] a, ~/.md ^[1..-1] a {
      $font-size: 16px;
    }

    a:hover {
      color: $chartreuse;
    }

    a:hover span {
      opacity: 1;
      color: transparent;
      animation: timeline-border-green 1s ease-in-out infinite alternate;
    }
  }

  #toggleSidebar {
    margin: 5px 10px;

    a {
      text-decoration: none;
      color: $white;
      transition: 0.5s;
    }
  }

  .appbarLogo {
    display: inline-block;
    height: 100%;
    padding: 5px;
    margin: 0 10px;

    img {
      height: inherit;
    }

    &#haxploreLogo img {
      padding: 10px 0;
      cursor: pointer;
    }
  }

  .sidebar {
    margin: 0 auto;

    ul {
      list-style: none;

      li {
        margin: 20px auto;
        display: block;

        .subList {
          margin: 10px 0 0 10px;

          li {
            margin: 5px;
          }
        }

        a, .subList a {
          font: 500 15px 'Roboto Slab';
          color: $white;
          text-decoration: none;
          cursor: pointer;
          padding: 10px;
          display: inline-block;
          width: 100%;

          span {
            color: $white;
            $font-size: 14px;
            border-radius: 100%;
          }

          &:hover {
            color: $chartreuse;
            background: rgba(63, 63, 65, 0.7);
          }
        }

        &.active, .subList li.active {
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
      cursor: pointer;
      margin: auto;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      ul {
        padding-top: 10px;
      }
    }
  }
}
</style>
