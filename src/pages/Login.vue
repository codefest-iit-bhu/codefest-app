<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <TabLayout :tabs="tabs">
          <div :class="$style.formContainer" slot="login">
            <BarLoader :loading="loading" color="#86FF00" :height="10" :class="$style.loader"/>
            <form :class="$style.form" @submit.prevent="emailLogin">
              <div :class="$style.fieldContainer">
                <label for="email" :class="$style.label">E-mail</label>
                <input type="email" :class="$style.field" v-model="email" required>
                <br>
                <label for="password" :class="$style.label">Password</label>
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
                <label for="name" :class="$style.label">Name</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  :class="$style.field"
                  v-model="name"
                  required
                >
                <br>
                <label for="email" :class="$style.label">E-mail</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  :class="$style.field"
                  v-model="email"
                  required
                >
                <br>
                <label for="password" :class="$style.label">Password</label>
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

const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const TabLayout = () => import("@components/layouts/TabLayout");
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
          result.user
            .sendEmailVerification()
            .then(() =>
              this.$toasted.global.success({
                message: "Verification Link has been sent."
              })
            )
            .catch(err => {
              this.$toasted.global.error_post({
                message: err.message
              });
            });
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
        .signInWithPopup(provider)
        .then(result => this.successfulAuth(result, false))
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    successfulAuth(result, byEmail) {
      this.loading = true;
      // const { isNewUser } = result.additionalUserInfo;

      result.user
        .getIdToken(true)
        .then(idToken => {
          this.tryLoginAndRegister(
            idToken,
            byEmail ? this.name : result.user.displayName
          );
        })
        .catch(err => {
          this.loading = false;
          this.$toasted.global.error_post({ message: err.message });
          result.user.delete();
        });
    },
    tryLoginAndRegister(idToken, name) {
      this._login(idToken)
        .then(_ => {
          this.loading = false;
          this.onRedirectAuth(false);
        })
        .catch(_ => {
          console.log(_);
          this.$recaptcha("login")
            .then(recaptchaToken =>
              this._register(idToken, name, this.referral, recaptchaToken)
            )
            .then(_ => {
              this.loading = false;
              this.onRedirectAuth(true);
            })
            .catch(err => {
              this.loading = false;
              this.$toasted.global.error_post({ message: err.message });
            });
        });
    },
    _login(idToken) {
      return this.$store.dispatch("login", { idToken });
    },
    _register(idToken, name, referralCode, recaptchaToken) {
      return this.$store.dispatch("register", {
        idToken,
        name,
        referralCode,
        recaptchaToken
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
  font-family: 'Quicksand';
  font-weight: 600;
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
    color: $vermilion;
    font-family: 'Roboto Slab';
    font-weight: 600;
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
    color: $vermilion;
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
  border-top: 1px solid $vermilion;

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
