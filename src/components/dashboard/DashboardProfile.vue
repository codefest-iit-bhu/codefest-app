<template>
  <div :class="[$style.container, $style[$mq]]">
    <div :class="$style.profilehead">
      <div :class="$style.userinit">
        <p>{{ retrieveInitials }}</p>
      </div>
      <span :class="$style.username">{{ profile.name }}</span>
    </div>
    <hr :class="$style.rightHr" />
    <div :class="$style.profile">
      <div :class="$style.about">
        <div :class="[$style.countdiv, is_verified]">
          <span :class="$style.reftext">Referral Count</span>
          <span :class="$style.refcount" v-if="profile.is_verified">
            {{
            profile.referral_count
            }}
          </span>
          <span :class="$style.refcount" v-else>
            <i class="far fa-times-circle"></i>
          </span>
        </div>
        <div :class="$style.box" v-if="profile.is_verified">
          <span :class="$style.key">Referral Link</span>
          <span :class="$style.value" v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)">
            <router-link :to="routerLocation">
              {{
              profile.referral_code
              }}
            </router-link>
          </span>
          <span v-else></span>
          <i class="fas fa-clipboard" :class="$style.copyIcon" @click="clickToCopy"></i>
        </div>
        <p :class="$style.helptext" v-if="profile.is_verified">
          Share the above referral link with your contacts to win exciting
          goodies!
        </p>
        <p :class="$style.disabledreferral" v-else>
          Referral link disabled. Please verify your account first and refresh
          the page.
          <br />
          <a href="javascript:void(0)" @click="resendVerification">Click here</a>
          to resend verification email.
        </p>
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
            <span :class="$style.pvalue">{{ profile.phone }}</span>
          </div>
          <div :class="$style.row">
            <span :class="$style.pkey">
              <span>Email</span>
            </span>
            <span :class="$style.pvalue">{{ user_email }}</span>
          </div>
          <div v-if="profile.institute_type == 1" :class="$style.row">
            <span :class="$style.pkey">
              <span>Institute Name</span>
            </span>
            <span :class="$style.pvalue">{{ profile.institute_name }}</span>
          </div>
          <div :class="$style.row">
            <span :class="$style.pkey">
              <span>Resume (*.pdf)</span>
            </span>
            <span :class="$style.pvalue">
              <form enctype="multipart/form-data">
                <input
                  type="file"
                  name="resume"
                  @change="
                    uploadResume($event.target.name, $event.target.files)
                  "
                />
              </form>
            </span>
          </div>
          <p :class="$style.helptext">
            Resume upload is recommended to be considered for hiring
            opportunities!
          </p>
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
      <a v-if="!!certificate" :href="certificate" target="_blank">
        <div :class="$style.link">
          <span :class="$style.linkText">
            <h4>Get Certificate</h4>
          </span>
        </div>
      </a>
      <a v-if="!!resume" :href="resume" target="_blank">
        <div :class="$style.link">
          <span :class="$style.linkText">
            <h4>View Resume</h4>
          </span>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
import { copyToClipboard } from "@js/utils";
import { SITE_URL } from "@js/constants";
import API from "@js/api";
import { auth } from "firebase/app";

const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    SectionLayout,
    ResponsiveTwoColumnLayout
  },
  data() {
    return {
      certificate: null,
      resume: null,
      user_email: null
    };
  },
  computed: {
    retrieveInitials() {
      const { name } = this.profile;
      if (!name) return;
      const newName = name.split(/\s+/);
      if (newName.length > 1) return newName[0][0] + newName[1][0];
      return newName[0][0];
    },

    is_verified() {
      if (this.profile.is_verified == true) {
        return this.$style.verified;
      } else {
        return this.$style.notverified;
      }
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
  created() {
    API.fetch("certificate/")
      .then(({ data }) => {
        this.$data.certificate = data.url;
      })
      .catch(e => {
        this.$data.certificate = null;
      });
    API.fetch("resume/")
      .then(({ data }) => {
        this.resume = data.resume;
      })
      .catch(e => {
        this.resume = null;
      });
    auth().onAuthStateChanged(user => {
      if (user) {
        this.user_email = user.email;
      }
    });
  },
  methods: {
    clickToCopy() {
      const referral = this.profile.referral_code;
      const referralShareLink = this.$router.resolve(this.routerLocation).href;
      copyToClipboard(`${SITE_URL}${referralShareLink}`);
      this.$toasted.global.success({
        message: `Copied "${referralShareLink}"!`
      });
    },
    resendVerification() {
      auth()
        .currentUser.sendEmailVerification()
        .then(() => {
          this.$toasted.global.success({
            message: "Verification Link has been sent."
          });
        })
        .catch(err => {
          this.$toasted.global.error_post({
            message: err.message
          });
        });
    },
    uploadResume(fieldName, fileList) {
      var resumeFile = new FormData();
      if (!fileList.length) return;
      resumeFile.append(fieldName, fileList[0], fileList[0].name);
      API.put("resume/", {
        body: resumeFile,
        headers: {
          "Content-Type": undefined
        }
      })
        .then(({ data }) => {
          const msg = "Your resume has been uploaded successfully!";
          this.$toasted.global.success({ message: msg });
          this.resume = data.resume;
        })
        .catch(err => {
          this.$toasted.global.error_post({ message: err.message });
        });
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

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
      background: $waterloo;
      border-radius: 50%;
      box-shadow: var(--icon-shadow);
      width: 108px;
      height: 108px;
      padding: 18px;
      font: 48px 'Roboto Slab';
      font-weight: 700;
      color: $black;

      p {
        text-align: center;
        width: 100%;
        margin-top: 5px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 72px;
        height: 72px;
        $font-size: 30px;
        padding: 12px;
      }
    }

    .username {
      order: -1;
      color: $white;
      font-family: 'Baloo Bhaina 2';
      font-weight: 700;
      color: var(--text-color);
      text-align: right;
      $font-size: 50px;
      margin: 0;
      float: right;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 36px;
      }
    }
  }

  hr {
    height: 8px;
    background-color: $waterloo;
    display: block;
    width: 70%;
    border: none;
  }

  .rightHr {
    margin-top: 5px;
    margin-bottom: 72px;
    margin-left: 30%;
    background-image: linear-gradient(to right, var(--background-color), $waterloo);
    border-radius: 10px;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      margin-bottom: 16px;
    }
  }

  .actionButtons {
    margin: 40px auto;
    text-align: center;
  }

  .link {
    margin: 0 10px;
    width: 260px;
    padding: 18px;
    border-radius: 50px;
    background-color: var(--background-color);
    box-shadow: var(--small-icon-shadow);
    text-align: center;
    cursor: pointer;
    display: inline-block;

    .linkText {
      color: $waterloo;
      display: inline;
      text-decoration: none;

      h4 {
        font-family: 'Roboto Slab';
        $font-size: 22px;
        margin: 0;
      }
    }

    &:hover {
      box-shadow: var(--inset-small-icon-shadow);

      .linkText {
        color: var(--text-color);
      }
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      margin-bottom: 30px;
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
        border-radius: 100px;
        box-shadow: var(--small-icon-shadow);
        color: var(--text-color);
        background-color: var(--background-color);
        text-align: center;
        height: 50px;
        width: 60%;
        margin-left: 20%;
        position: relative;

        .copyIcon {
          padding: 12px;
          cursor: pointer;
          margin-right: 15px;
          float: right;
        }

        ~/.lg ^[1..-1], ~/.xxl ^[1..-1], ~/.xl ^[1..-1], ~/.md ^[1..-1] {
          .key {
            display: inline-block;
            float: left;
            font-weight: 700;
            font-family: 'Roboto Slab';
            $font-size: 24px;
            padding: 10px 15px 10px;
            height: 100%;
            color: $white;
            border-radius: inherit;
            border-bottom-right-radius: 0;
            border-top-right-radius: 0;
            border-right: 1px solid $waterloo;
            background: alpha($waterloo, 0.7);
          }

          .value {
            display: inline-block;
            $font-size: 18px;
            font-family: 'Quicksand';
            font-weight: 600;
            padding: 12px;
            height: 100%;
          }
        }

        ~/.md ^[1..-1] {
          width: 100%;
          margin-left: 0%;
        }

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          display: flex;
          flex-flow: column;
          width: 200px;
          height: 200px;
          border-radius: 30px;
          border: 3px solid $waterloo;
          animation: timeline-border-green 1s ease-in-out infinite alternate;
          margin: auto;

          .key {
            display: inline-block;
            width: 100%;
            font-weight: bold;
            font-family: 'Roboto Slab';
            $font-size: 24px;
            padding: 8px 15px;
            color: var(--text-color);
          }

          .copyIcon {
            width: 100%;
            $font-size: 60px;
            padding: 24px 0;
            color: $waterloo;
          }
        }
      }
    }

    .helptext {
      $font-size: 14px;
      display: inline-block;
      border: 3px solid $waterloo;
      border-radius: 10px;
      padding: 8px 16px;
      margin-top: 40px;
      box-shadow: var(--small-icon-shadow);
    }

    .disabledreferral {
      display: inline-block;
      $font-size: 14px;
      box-shadow: 0 0 20px red inset;
      border: 1px solid red;
      border-radius: 10px;
      padding: 8px 16px;
    }

    .countdiv {
      width: 200px;
      height: 200px;
      border-radius: 30px;
      margin: auto;
      margin-top: 50px;
      margin-bottom: 50px;
      display: flex;
      flex-flow: column;
      transition-property: width, height;
      transition: all 2s ease-in-out;

      .reftext {
        order: 0;
        height: 50px;
        color: var(--text-color);
        padding: 15px 0;
        font: 600 20px 'Roboto Slab';
      }

      .refcount {
        height: 150px;
        order: 1;
        padding: 30px 0;
        font: 600 60px 'Roboto Slab';
        color: $waterloo;
      }
    }

    .verified {
      border: 5px solid $waterloo;
      animation: timeline-border-green 1s ease-in-out infinite alternate;
    }

    .notverified {
      border: 5px solid red;
      animation: timeline-border-white 1s ease-in-out infinite alternate;

      i {
        color: red;
      }
    }

    .profileinfo {
      width: 800px;
      margin: auto;

      .row {
        transform: skew(30deg);
        border-radius: 0 15px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: var(--small-icon-shadow);
        $font-size: 16px;
        display: flex;
        flex-flow: row;

        .pkey {
          width: 30%;
          background: $limeade;
          display: inline-block;
          border-radius: 0 15px;
          order: 1;
          font-weight: bold;
          font-family: 'Roboto Slab';
          padding: 6px 15px;
          height: 100%;
          color: $white;
          background: alpha($waterloo, 0.8);

          span {
            display: inline-block;
            transform: skew(-30deg);
          }
        }

        .pvalue {
          width: 70%;
          order: 2;
          transform: skew(-30deg);
          display: inline-block;
          font-family: 'Quicksand';
          font-weight: 700;
          padding: 6px;
          height: 100%;
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        .row {
          width: 100%;
          flex-flow: column;
          $font-size: 12px;

          .pkey {
            order: 1;
            width: 100%;
          }

          .pvalue {
            order: 2;
            width: 100%;
          }
        }
      }

      ~/.xs ^[1..-1] {
        width: 240px;
      }

      ~/.sm ^[1..-1] {
        width: 300px;
      }

      ~/.md ^[1..-1] {
        width: 550px;
      }
    }
  }
}
</style>
