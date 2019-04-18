<template>
  <div :class="[$style.container, $style[$mq]]">
    <div :class="$style.profilehead">
      <div :class="$style.userinit">
        <p>{{retrieveInitials}}</p>
      </div>
      <span :class="$style.username">{{profile.name}}</span>
    </div>
    <hr :class="$style.rightHr">
    <div :class="$style.profile">
      <div :class="$style.about">
        <div :class="$style.box">
          <span :class="$style.key">Referral Link</span>
          <span :class="$style.value">
            <router-link :to="routerLocation">{{ profile.referral_code }}</router-link>
          </span>
          <i class="fas fa-clipboard" :class="$style.copyIcon" @click="clickToCopy"></i>
        </div>
        <p
          :class="$style.helptext"
        >Share the above referral link with your contacts to win exciting goodies!</p>
        <div :class="$style.profileinfo">
          <div :class="$style.row">
            <span :class="$style.pkey">
              <span>Name</span>
            </span>
            <span :class="$style.pvalue">{{ profile.name }}</span>
          </div>
          <div :class="$style.row">
            <span :class="$style.pkey">
              <span>Country</span>
            </span>
            <span :class="$style.pvalue">{{ profile.country }}</span>
          </div>
          <div :class="$style.row">
            <span :class="$style.pkey">
              <span>Phone</span>
            </span>
            <span :class="$style.pvalue">{{ profile.phone}}</span>
          </div>
          <div v-if="profile.institute_type == 1" :class="$style.row">
            <span :class="$style.pkey">
              <span>Institute Name</span>
            </span>
            <span :class="$style.pvalue">{{ profile.institute_name }}</span>
          </div>
        </div>
      </div>
    </div>

    <div :class="$style.actionButtons">
      <div :class="$style.link" @click="$router.push('/profile/edit')">
        <span :class="$style.linkText">
          <h4>Edit Profile</h4>
        </span>
      </div>
      <div
        :class="$style.link"
        @click="$router.push('/password/change')"
        v-if="profile.provider === 'password'"
      >
        <span :class="$style.linkText">
          <h4>Change Password</h4>
        </span>
      </div>
    </div>
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
      console.log(this.profile);
      if (!name) return;
      const newName = name.split(/\s+/);
      if (typeof newName[1][0] !== "undefined")
        return newName[0][0] + newName[1][0];
      return newName[0][0];
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
  padding-top: 50px;

  .profilehead {
    height: 108px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;

    .userinit {
      order: -2;
      background: $chartreuse;
      border-radius: 50%;
      width: 108px;
      height: 108px;
      padding: 18px;
      font: 72px 'Aldo the Apache';
      color: $black;

      p {
        text-align: center;
        width: 100%;
        margin-top: 5px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 72px;
        height: 72px;
      }
    }

    .username {
      order: -1;
      color: $white;
      font-family: 'Aldo the Apache';
      text-align: right;
      font-size: 50px;
      margin: 0;
      float: right;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 36px;
      }
    }
  }

  hr {
    height: 4px;
    background-color: $chartreuse;
    display: block;
    width: 70%;
    border: none;
  }

  .rightHr {
    margin-top: 5px;
    margin-bottom: 72px;
    margin-left: 30%;
    background-image: linear-gradient(to right, $black, $chartreuse);
  }

  .actionButtons {
    margin: 40px auto;
    text-align: center;
  }

  .link {
    margin: 0 10px;
    width: 220px;
    padding: 18px;
    border-radius: 50px;
    border: 2px solid $chartreuse;
    text-align: center;
    cursor: pointer;
    display: inline-block;

    .linkText {
      color: $chartreuse;
      display: inline;
      text-decoration: none;

      h4 {
        font-family: 'Aldo the Apache';
        font-size: 22px;
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
      width: 100%;

      .box {
        border: 2px solid $limeade;
        border-radius: 100px;
        text-align: center;
        height: 50px;
        width: 60%;
        margin-left: 20%;

        .copyIcon {
          cursor: pointer;
          margin-right: 20px;
          margin-top: 10px;
          float: right;
        }

        .key {
          display: inline-block;
          float: left;
          font-weight: bold;
          font-family: 'Roboto Slab';
          font-size: 24px;
          padding: 8px 15px;
          height: 100%;
          color: $black;
          border-radius: inherit;
          border-bottom-right-radius: 0;
          border-top-right-radius: 0;
          border-right: 1px solid $chartreuse;
          background: alpha($chartreuse, 0.7);
        }

        .value {
          display: inline-block;
          font-size: 18px;
          font-family: 'Quicksand';
          padding: 12px;
          height: 100%;
        }

        ~/.md ^[1..-1] {
          width: 100%;
          margin-left: 0%;
        }
      }
    }

    .helptext {
      font-size: 14px;
    }

    .profileinfo {
      width: 60%;
      margin-left: 20%;

      .row {
        // clip-path: polygon(4% 0, 100% 0, 96% 100%, 0 100%);
        transform: skew(30deg);
        border: solid 2px $limeade;
        margin-top: 10px;
        margin-bottom: 10px;

        .pkey {
          width: 30%;
          background: $limeade;
          display: inline-block;
          float: left;
          font-weight: bold;
          font-family: 'Roboto Slab';
          font-size: 16px;
          padding: 8px 15px;
          height: 100%;
          color: $black;
          background: alpha($chartreuse, 0.7);

          span {
            display: inline-block;
            transform: skew(-30deg);
          }
        }

        .pvalue {
          width: 70%;
          transform: skew(-30deg);
          display: inline-block;
          font-size: 16px;
          font-family: 'Quicksand';
          padding: 8px;
          height: 100%;
        }
      }
    }
  }
}
</style>
