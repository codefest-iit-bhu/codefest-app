<template>
  <div :class="$style.container">
    <SectionLayout title="My Profile">
      <div :class="$style.profile">
        <ResponsiveTwoColumnLayout :isRightAbove="true">
          <div :class="$style.about" slot="left">
            <!-- <div :class="$style.card" v-for="(item ,i) in this.items" :key="i">
              <div :class="$style.label">{{item.key}}</div>
              <div :class="$style.value">{{item.value}}</div>
            </div>-->
            <div :class="$style.box">
              <span :class="$style.key">Referral Code</span>
              <span :class="$style.value">
                <router-link :to="routerLocation">{{ profile.referral_code }}</router-link>
              </span>
              <i class="fas fa-clipboard" :class="$style.copyIcon" @click="clickToCopy"></i>
            </div>
          </div>
          <div :class="$style.dp" slot="right">
            <div :class="$style.img">
              <span class="absolute-center">{{retrieveInitials}}</span>
            </div>
            <span :class="$style.name">{{profile.name}}</span>
          </div>
        </ResponsiveTwoColumnLayout>
      </div>

      <div :class="$style.link" @click="$router.push('/profile/edit')">
        <span :class="$style.linkText">
          <h4>Edit Profile</h4>
        </span>
      </div>
    </SectionLayout>
  </div>
</template>

<script>
import { copyToClipboard } from "@js/utils";
import { SITE_URL } from "@js/constants";

import SectionLayout from "@components/layouts/SectionLayout";
import ResponsiveTwoColumnLayout from "@components/layouts/ResponsiveTwoColumnLayout";

export default {
  components: {
    SectionLayout,
    ResponsiveTwoColumnLayout
  },
  computed: {
    retrieveInitials() {
      const { name } = this.profile;
      if (!name) return;
      const newName = name.split(/\s+/);
      return newName[0][0] + newName[1][0];
    },
    routerLocation() {
      return {
        name: "~/login",
        query: {
          referral: this.profile.referral_code
        }
      };
    }
  },
  props: {
    profile: {
      required: true,
      type: Object
    }
  },
  methods: {
    clickToCopy: function() {
      const referral = this.profile.referral_code;
      const referralShareLink = this.$router.resolve(this.routerLocation).href;
      copyToClipboard(`${SITE_URL}${referralShareLink}`);
      this.$toasted.global.success({
        message: `Copied "${referralShareLink}"!`
      });
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';

.container {
  height: 100%;
}

.link {
  margin: 40px auto;
  width: 290px;
  height: auto;
  padding: 24px;
  border-radius: 50px;
  border: 2px solid $chartreuse;
  text-align: center;
  cursor: pointer;

  .linkText {
    color: $chartreuse;
    display: inline;
    text-decoration: none;

    h4 {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin: 0;
    }
  }

  &:hover {
    box-shadow: inset 0px 0px 10px $chartreuse;
  }
}

.profile {
  display: flex;
  flex-direction: row;
  justify-content: space-around;

  .about {
    text-align: center;
    margin: 15px;
    width: inherit;

    .box {
      border: 2px solid $chartreuse;
      border-radius: 20px;
      text-align: center;
      height: 50px;
      width: 100%;

      .copyIcon {
        cursor: pointer;
        margin-right: 10px;
        margin-top: 10px;
        float: right;
      }

      .key {
        display: inline-block;
        float: left;
        font-weight: bold;
        font-size: 24px;
        padding: 15px;
        height: 100%;
        border-radius: inherit;
        border-bottom-right-radius: 0;
        border-top-right-radius: 0;
        border-right: 1px solid $chartreuse;
        background: alpha($chartreuse, 0.7);
      }

      .value {
        display: inline-block;
        font-size: 14px;
        padding: 15px;
        height: 100%;
      }
    }
  }

  .dp {
    text-align: right;
    float: right;

    .img {
      margin: 15px auto;
      position: relative;
      background-image: url('@assets/dp.png');
      background-size: cover;
      width: 150px;
      height: 150px;
      font-size: 30px;
      font-weight: bold;
    }

    .name {
      float: left;
      font-size: 30px;
      font-weight: bold;
      width: 100%;
    }
  }
}
</style>


