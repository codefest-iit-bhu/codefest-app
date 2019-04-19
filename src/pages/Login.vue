<template>
  <div :class="$style.root">
    <AppBar :isSideNavigationShown="false"/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <TabLayout :tabs="tabs">
          <div :class="$style.formContainer" slot="login">
            <BarLoader :loading="loading" color="#86FF00" :height="10" :class="$style.loader"/>
            <form :class="$style.form" @submit.prevent="emailLogin">
              <div :class="$style.fieldContainer">
                <label for="email" :class="$style.label">email</label>
                <input type="email" :class="$style.field" v-model="email" required>
                <br>
                <label for="password" :class="$style.label">password</label>
                <span :class="$style.fieldWrapper">
                  <input
                    type="password"
                    :class="$style.field"
                    v-model="password"
                    id="login__password"
                    pattern=".{6,}"
                    title="Must be greater than 6 letters."
                    required
                  >
                  <i
                    class="fas"
                    :class="isPasswordVisible('login__password') ? 'fa-eye' : 'fa-eye-slash'"
                    @click="togglePasswordVisibility('login__password')"
                  ></i>
                </span>
              </div>
              <div :class="$style.forgotPasswd">
                <router-link to="/password/reset">Forgot Password?</router-link>
              </div>
              <div :class="$style.btnStyle">
                <button value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </form>
            <div :class="$style.social">
              <button @click="googleLogin" :class="$style.socialButton">
                <img src="@assets/social/google.png">
              </button>
              <button @click="fbLogin" :class="$style.socialButton">
                <img src="@assets/social/facebook.png">
              </button>
              <button @click="gitHubLogin" :class="$style.socialButton">
                <img src="@assets/social/github.png">
              </button>
            </div>
          </div>

          <div :class="$style.formContainer" slot="register">
            <BarLoader :loading="loading" color="#86FF00" :height="10" :class="$style.loader"/>
            <form :class="$style.form" @submit.prevent="emailRegister">
              <div :class="$style.fieldContainer">
                <label for="name" :class="$style.label">name</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  :class="$style.field"
                  v-model="name"
                  required
                >
                <br>
                <label for="email" :class="$style.label">email</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  :class="$style.field"
                  v-model="email"
                  required
                >
                <br>
                <label for="password" :class="$style.label">password</label>
                <span :class="$style.fieldWrapper">
                  <input
                    type="password"
                    :class="$style.field"
                    v-model="password"
                    id="register__password"
                    pattern=".{6,}"
                    title="Must be greater than 6 letters."
                    required
                  >
                  <i
                    class="fas"
                    :class="isPasswordVisible('register__password') ? 'fa-eye' : 'fa-eye-slash'"
                    @click="togglePasswordVisibility('register__password')"
                  ></i>
                </span>
              </div>
              <div :class="$style.btnStyle">
                <button value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </form>
            <div :class="$style.social">
              <button @click="googleLogin" :class="$style.socialButton">
                <img src="@assets/social/google.png">
              </button>
              <button @click="fbLogin" :class="$style.socialButton">
                <img src="@assets/social/facebook.png">
              </button>
              <button @click="gitHubLogin" :class="$style.socialButton">
                <img src="@assets/social/github.png">
              </button>
            </div>
          </div>
        </TabLayout>
      </div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import firebase from "firebase";

import AppBar from "@components/Menu/AppBar";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";
import { BarLoader } from "@saeris/vue-spinners";

export default {
  components: {
    AppBar,
    Footer,
    TabLayout,
    BarLoader
  },
  data() {
    return {
      name: "",
      email: "",
      password: "",
      referral: this.$route.query.referral || "",
      tabs: [
        {
          name: "login",
          title: "Login"
        },
        {
          name: "register",
          title: "Register"
        }
      ],
      loading: false,
      __stubbed: 0
    };
  },
  methods: {
    emailLogin() {
      this.loading = true;
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(result => {
          this.successfulAuth(result, true);
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    emailRegister() {
      this.loading = true;
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(result => {
          this.successfulAuth(result, true);
          this.$toasted.global.success({
            message: "Verification Link has been sent."
          });
          result.user.sendEmailVerification().then(() => {});
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    googleLogin() {
      const provider = new firebase.auth.GoogleAuthProvider();
      this.socialLogin(provider);
    },
    fbLogin() {
      const provider = new firebase.auth.FacebookAuthProvider();
      this.socialLogin(provider);
    },
    gitHubLogin() {
      const provider = new firebase.auth.GithubAuthProvider();
      this.socialLogin(provider);
    },
    socialLogin(provider) {
      this.loading = true;
      firebase
        .auth()
        .signInWithRedirect(provider)
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    successfulAuth(result, byEmail) {
      this.loading = true;
      const { isNewUser } = result.additionalUserInfo;

      result.user
        .getIdToken(true)
        .then(idToken => {
          if (isNewUser)
            this.$recaptcha("login").then(token => {
              this._register(
                idToken,
                byEmail ? this.name : result.user.displayName,
                this.referral,
                token
              );
            });
          else this._login(idToken);
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
          result.user.delete();
        });
    },
    _login(idToken) {
      this.$store
        .dispatch("login", { idToken })
        .then(_ => {
          this.loading = false;
          this.onRedirectAuth(false);
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    _register(idToken, name, referralCode, recaptchaToken) {
      this.$store
        .dispatch("register", {
          idToken,
          name,
          referralCode,
          recaptchaToken
        })
        .then(_ => {
          this.loading = false;
          this.onRedirectAuth(true);
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    onRedirectAuth(isRegistered) {
      const path =
        this.$route.query.redirect ||
        (isRegistered ? "/profile/edit" : "/dashboard");
      this.$router.push({ path });
    },
    togglePasswordVisibility(inputId) {
      const inputElem = document.getElementById(inputId);
      inputElem.type = inputElem.type === "password" ? "text" : "password";
      this.$data.__stubbed++;
    }
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
  created() {
    this.loading = true;
    firebase
      .auth()
      .getRedirectResult()
      .then(result => {
        if (!result.user) this.loading = false;
        else if (result.credential) this.successfulAuth(result, false);
      })
      .catch(err => {
        this.loading = false;
        this.$toasted.global.error_post({ message: err.message });
      });
  }
};
</script>
<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.authContainer {
  font-size: 16px;
  font-family: courier, monospace;
  max-width: 600px;
  margin: auto;
  width: 100%;
}

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 200px 0;
  position: relative;
  top: 0;
  z-index: 1;
  font-family: 'Roboto Slab';
  font-size: 18px;
}

.root {
  height: 100%;
}

.formContainer {
  .loader {
    width: 100%;
    position: absolute;
    top: 0;
  }
}

.form {
  margin: 50px;
}

.fieldContainer {
  width: 100%;
  margin-bottom: 20px;
  text-align: right;
}

.field {
  clear: both;
  height: 30px;
  color: white;
  border: 0;
  outline: 0;
  max-width: 400px;
  width: 100%;
  font-size: 16px;
  background-color: #fff2;
  border-radius: 5px;
  padding-left: 5px;
  margin-bottom: 20px;
}

.label {
  float: left;
  color: white;
  text-align: right;
  height: 30px;
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

.forgotPasswd {
  width: 100%;
  text-align: right;
  margin-bottom: 20px;

  a {
    color: $chartreuse;
  }
}

.btnStyle {
  text-align: center;
}

.submit {
  border: 0;
  background: transparent;
  color: $white;
  border-radius: 100%;
  font-size: 40px;
  height: 40px;
  width: 40px;
  cursor: pointer;
  text-align: center;

  &:hover {
    color: $chartreuse;
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

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
