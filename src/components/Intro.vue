<template>
  <ResponsiveTwoColumnLayout :isRightAbove="true">
    <div :class="$style.description" slot="left">
      <p>
        The
        <span
          >Department of Computer Science and Engineering, IIT (BHU)
          Varanasi</span
        >
        brings to you yet another edition of its annual coding extravaganza,
        Codefest!
        <br />
        <br />Being more diverse than ever, <span>Codefest '24</span> boasts of
        a plethora of events, ranging from competitive programming, algorithms
        and application development to upcoming trends like cryptography,
        machine learning, computer vision and cyber security.
        <br />
        <br />With problems being of varying difficulty levels, Codefest
        provides the perfect platform for fresh enthusiasts, as well as the
        experienced ones, to code together and compete for ultimate glory.
      </p>
      <div v-if="!isMinimal" :class="$style.buttonContainer">
        <div :class="$style.link">
          <router-link to="/login"
            :class="[$style.linkText]"
          >
            <h4 v-if="!isLoggedIn">Register / Login</h4>
            <h4 v-if="isLoggedIn">Dashboard</h4>
          </router-link>
        </div>
      </div>
    </div>
    
    <div :class="$style.video" slot="right">
      <youtube :video-id="videoId" ref="youtube" @playing="playing"></youtube>
    </div>

  </ResponsiveTwoColumnLayout>
</template>

<script>
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");
  import { isMinimal } from "@js/utils";

export default {
  components: {
    ResponsiveTwoColumnLayout,
  },
  data: () => {
    return {
      videoId: "QOkjxSVr5Wc",
    };
  },
  methods: {
    playing() {
      console.log("Dekho Dekho!!");
    },
  },
  computed: {
    player() {
      return this.$refs.youtube.player;
    },
    isMinimal() {
      return isMinimal(this.$mq);
    },
    isLoggedIn(){
      return this.$store.getters.isLoggedIn;
    }
  },
};
</script>

<style module lang="stylus">
.description {
  text-align: left;
  margin: 30px 30px 0 0;
  $font-size: 18px;

  span {
    font-weight: bold;
  }
}

.video {
  border-radius: 10px;
  padding: 10px;
  width: 100%;
  box-shadow: var(--box-shadow);

  & > iframe {
    border-radius: 10px;
    width: 100%;
  }
}
.buttonContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }
.link {
    margin: 20px 20px 20px 20px;
    width: 340px;
    height: 120px;
    padding: 20px;
    box-shadow: var(--box-shadow);
    border-radius: 50px 0px 50px 0px;
    text-align: center;
    cursor: pointer;

    .linkText {
      display: inline-block;
      text-decoration: none;
      color: $waterloo;

      h4 {
        text-align: center;
        position: relative;
        top: 50%;
        -ms-transform: translateY(-50%);
        -webkit-transform: translateY(-50%);
        transform: translateY(-50%);
        font-family: 'Roboto Slab';
        $font-size: 30px;
      }
    }

  &:hover {
    box-shadow: var(--inset-box-shadow);

    .linkText {
      color: var(--text-color);
    }
  }
}
</style>
