<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <div :class="$style.formContainer" slot="basic">
          <form :class="$style.form" @submit.prevent="submitForm">
            <div :class="$style.card">
              <h3>Change Password</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="old__password" :class="$style.label">current password</label>
                  <span :class="$style.fieldWrapper">
                    <input type="password" id="old__password" v-model="currentPasswd" required>
                    <i
                      class="fas"
                      :class="isPasswordVisible('old__password') ? 'fa-eye' : 'fa-eye-slash'"
                      @click="togglePasswordVisibility('old__password')"
                    ></i>
                  </span>
                </div>
                <div :class="$style.field">
                  <label for="new__password" :class="$style.label">new password</label>
                  <span :class="$style.fieldWrapper">
                    <input type="password" id="new__password" v-model="newPasswd" required>
                    <i
                      class="fas"
                      :class="isPasswordVisible('new__password') ? 'fa-eye' : 'fa-eye-slash'"
                      @click="togglePasswordVisibility('new__password')"
                    ></i>
                  </span>
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button type="submit" value=">" :class="$style.next">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import firebase from "firebase";
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const TabLayout = () => import("@components/layouts/TabLayout");

export default {
  components: {
    AppBar,
    Footer,
    TabLayout
  },
  data() {
    return {
      currentPasswd: "",
      newPasswd: "",
      __stubbed: 0
    };
  },
  computed: {
    isPasswordVisible() {
      this.$data.__stubbed; // To make this computed data reactive.
      return inputId => {
        const inputElem = document.getElementById(inputId);
        if (inputElem) return inputElem.type !== "password";
      };
    }
  },
  methods: {
    submitForm() {
      var user = firebase.auth().currentUser;
      user
        .reauthenticateAndRetrieveDataWithCredential(this.currentPasswd)
        .then(_ => {
          user
            .updatePassword(this.newPassword)
            .then(_ => {
              this.$toasted.global.success({
                message: `Successfully updated password!`
              });
            })
            .catch(err => {
              this.$toasted.global.error_post({ message: err.message });
            });
        })
        .catch(err => {
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    togglePasswordVisibility(inputId) {
      const inputElem = document.getElementById(inputId);
      inputElem.type = inputElem.type === "password" ? "text" : "password";
      this.$data.__stubbed++;
    }
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.authContainer {
  font-size: 16px;
  font-family: courier, monospace;
  max-width: 700px;
  margin: 50px auto;
  width: 100%;
}

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 100px 0;
  position: relative;
  top: 0;
  z-index: 1;
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
}

.form {
  margin: 20px;
  position: relative;
  border: 1px solid $chartreuse;
  border-radius: 5px;
  box-shadow: inset 0px 0px 15px $chartreuse;
  background: #111;

  .formNav {
    width: 100%;
    text-align: center;
    border-top: 1px solid $chartreuse;
    padding: 20px;
    margin: 0;

    i {
      cursor: pointer;

      &.active {
        color: $chartreuse;
      }
    }
  }

  .card {
    padding: 10px 20px;
    min-height: 300px;
    margin: 5px;
    width: 100%;
    position: relative;

    h3 {
      color: $chartreuse;
      text-align: center;
      text-transform: uppercase;
    }

    .fieldsContainer {
      width: 100%;
      padding: 5px;
      margin: 5px auto;
      text-align: right;
    }

    .field {
      margin: 10px auto;
      margin-top: 20px;
      text-align: center;

      input, select {
        text-align: left;
        display: inline-block;
        height: 30px;
        width: calc(100% - 120px);
        color: white;
        border: 0;
        outline: 0;
        margin: auto;
        font-size: 16px;
        border-radius: 5px;
        padding-left: 5px;
        background: #fff2;
      }

      .fieldWrapper {
        width: 100%;
        position: relative;

        i {
          top: 0;
          right: 7px;
          position: absolute;
          cursor: pointer;
        }
      }

      option {
        color: black;
      }

      .label {
        display: inline-block;
        text-align: left;
        width: 100px;
        color: white;
        height: 30px;
      }
    }

    .btnStyle {
      text-align: center;

      .next {
        border: 0;
        background: transparent;
        color: $white;
        border-radius: 100%;
        font-size: 30px;
        height: 30px;
        width: 30px;
        cursor: pointer;
        text-align: center;

        &:hover {
          color: $chartreuse;
        }
      }
    }

    .social {
      width: 100%;
      max-width: 600px;
      margin: auto;
      text-align: center;
      padding: 5px;
      margin-top: 20px;
      border: 0;
      border-top: 1px solid $chartreuse;

      .socialButton {
        background-color: Transparent;
        background-repeat: no-repeat;
        border: none;
        cursor: pointer;
        overflow: hidden;
        outline: none;

        img {
          margin: 10px;
          width: 40px;
          height: 40px;
        }
      }
    }
  }
}

.xs, .sm {
  .form {
    .field {
      input, select, .label {
        font-size: 16px;
        width: 100%;
      }
    }
  }
}
</style>
