<template>
  <div :class="$style.root">
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
                    <input
                      type="password"
                      id="old__password"
                      :class="$style.field"
                      v-model="currentPasswd"
                      required
                    >
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
                    <input
                      type="password"
                      id="new__password"
                      :class="$style.field"
                      v-model="newPasswd"
                      required
                    >
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

import AppBar from "@components/Menu/AppBar";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";

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
      border-radius: 4px 4px 0 0;
      box-shadow: inset 0px 0px 15px $chartreuse;

      .formNav {
        width: 100%;
        position: absolute;
        bottom: 0;
        text-align: center;
        border-top: 1px solid $chartreuse;
        padding: 20px;
        margin: 0;
        border-radius: 0 0 4px 4px;

        i {
          cursor: pointer;

          &.active {
            color: $chartreuse;
          }
        }
      }

      .card {
        padding: 20px;
        margin: 10px;
        width: 100%;
        position: relative;

        h3 {
          color: $chartreuse;
          text-align: center;
          text-transform: uppercase;
        }

        .loader {
          margin: auto;
          position: absolute;
          top: calc(50% - 60px);
          left: calc(50% - 30px);
          border: 5px solid $white;
          border-radius: 50%;
          border-top: 5px solid $chartreuse;
          width: 60px;
          height: 60px;
          -webkit-animation: spin 2s linear infinite; /* Safari */
          animation: spin 2s linear infinite;
        }

        @keyframes spin {
          0% {
            -webkit-transform: rotate(0deg);
          }

          100% {
            -webkit-transform: rotate(360deg);
          }
        }

        @keyframes spin {
          0% {
            transform: rotate(0deg);
          }

          100% {
            transform: rotate(360deg);
          }
        }

        .fieldsContainer {
          width: 100%;
          margin-bottom: 15px;
          text-align: right;
        }

        .field {
          input, select {
            height: 30px;
            color: white;
            border: 0;
            outline: 0;
            max-width: 400px;
            width: 100%;
            font-size: 16px;
            background: #fff2;
            border-radius: 5px;
            padding-left: 5px;
            margin-bottom: 15px;
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
            float: left;
            clear: both;
            color: white;
            text-align: right;
            height: 30px;
            margin-bottom: 15px;
          }
        }

        .btnStyle {
          text-align: center;

          .submit {
            border-radius: 4px;
            background: $chartreuse;
            color: black;
            border: 1px solid $limeade;
            height: 30px;
            width: 70px;
            cursor: pointer;
            text-align: center;

            &:hover {
              background: $limeade;
              color: $white;
            }
          }

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
      }
    }

    @media screen and (max-width: 769px) {
      .wrapper {
        width: 90%;
      }
    }
</style>
