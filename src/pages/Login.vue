<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <TabLayout :tabs="tabs">
          <div :class="$style.formContainer" slot="login">
            <form :class="$style.form" @submit.prevent="emailLogin">
              <div :class="$style.fieldContainer">
                <label for="email" :class="$style.label">email</label>
                <input type="email" :class="$style.field" v-model="email" required>
                <br>
                <label for="password" :class="$style.label">password</label>
                <input type="password" :class="$style.field" v-model="password" required>
              </div>
              <div :class="$style.forgotPasswd">
                <a href="#">Forgot Password</a>
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
            <form :class="$style.form" @submit.prevent="emailRegister">
              <div :class="$style.fieldContainer">
                <label for="name" :class="$style.label">name *</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  :class="$style.field"
                  v-model="name"
                  required
                >
                <br>
                <label for="email" :class="$style.label">email *</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  :class="$style.field"
                  v-model="email"
                  required
                >
                <br>
                <label for="password" :class="$style.label">password *</label>
                <input type="password" :class="$style.field" v-model="password" required>
                <br>
                <label for="referral" :class="$style.label">referral code</label>
                <input
                  type="text"
                  id="referral"
                  name="referral"
                  :class="$style.field"
                  v-model="referral"
                >
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
import AppBar from "@components/Menu/AppBar";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";
import firebase from "firebase";

export default {
  components: {
    AppBar,
    Footer,
    TabLayout
  },
  data() {
    return {
      name: "",
      email: "",
      password: "",
      referral: "",
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
      loading: false
    };
  },
  methods: {
    emailLogin() {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(result => {
          this.successfulAuth(result, true);
        })
        .catch(err => {
          alert(err.message);
        });
    },
    emailRegister() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(result => {
          this.successfulAuth(result, true);
        })
        .catch(err => {
          alert(err.message);
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
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(result => {
          this.successfulAuth(result, false);
        })
        .catch(err => {
          alert(err.message);
        });
    },
    successfulAuth(result, byEmail) {
      const { isNewUser } = result.additionalUserInfo;
      result.user
        .getIdToken(true)
        .then(idToken => {
          if (isNewUser)
            this._register(
              idToken,
              byEmail ? this.name : result.user.displayName,
              this.referral
            );
          else this._login(idToken);
        })
        .catch(err => {
          alert(err.message);
          result.user.delete();
        });
    },
    _login(idToken) {
      this.loading = true;
      this.$store
        .dispatch("login", { idToken })
        .then(_ => {
          this.loading = false;
          this.onRedirectAuth(_);
        })
        .catch(_ => (this.loading = false));
    },
    _register(idToken, name, referralCode) {
      this.loading = true;
      this.$store
        .dispatch("register", {
          idToken,
          name,
          referralCode
        })
        .then(_ => {
          this.loading = false;
          this.onRedirectAuth(_);
        })
        .catch(_ => (this.loading = false));
    },
    onRedirectAuth() {
      console.log(arguments[0]);
      const path = this.$route.query.redirect || "/";
      this.$router.push({ path });
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
  font-family: 'Roboto Mono';
  font-size: 18px;
}

.root {
  height: 100%;
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
  background: #fff2;
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

.forgotPasswd {
  width: 100%;
  text-align: right;

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
