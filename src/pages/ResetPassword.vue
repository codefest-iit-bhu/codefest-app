<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <div :class="$style.formContainer" slot="basic">
          <form :class="$style.form" @submit.prevent="submitForm">
            <div :class="$style.card">
              <h3>Reset Password</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="currentPasswd" :class="$style.label">current password</label>
                  <input
                    type="password"
                    id="currentPasswd"
                    :class="$style.field"
                    v-model="currentPasswd"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="newPasswd" :class="$style.label">new password</label>
                  <input
                    type="password"
                    id="newPasswd"
                    :class="$style.field"
                    v-model="newPasswd"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="confirmPasswd" :class="$style.label">retype new password</label>
                  <input
                    type="password"
                    id="confirmPasswd"
                    :class="$style.field"
                    v-model="confirmPasswd"
                    required
                  >
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
import AppBar from "@components/Menu/AppBar";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";
import firebase from "firebase";
import API from "@js/api";

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
      confirmPasswd: ""
    };
  },
  methods: {
    submitForm() {
      var user = firebase.auth().currentUser;
      if (this.newPasswd == this.confirmPasswd)
        user
          .reauthenticateAndRetrieveDataWithCredential(this.currentPasswd)
          .then(_ => {
            user
              .updatePassword(this.newPassword)
              .then(_ => {})
              .catch(console.log);
          })
          .catch(console.log);
      else alert("Passwords do not match.");
    }
  },
  created() {},
  mounted() {}
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

    @media screen and (max-width: 769px) {
      .wrapper {
        width: 90%;
      }
    }
</style>
