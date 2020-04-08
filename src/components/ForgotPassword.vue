<template>
  <div :class="$style.root">
    <AppBar />
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <form :class="$style.form" @submit.prevent="forgot_password">
          <h3>RESET PASSWORD</h3>
          <div :class="$style.fieldContainer">
            <label for="email" :class="$style.label">email</label>
            <input
              type="email"
              :class="$style.field"
              v-model="email"
              required
            />
          </div>
          <div :class="$style.btnStyle">
            <button value=">" :class="$style.submit">
              <i class="fas fa-arrow-circle-right"></i>
            </button>
          </div>
        </form>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const TabLayout = () => import("@components/layouts/TabLayout");

import { auth } from "firebase/app";

export default {
  components: {
    AppBar,
    Footer,
    TabLayout,
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    forgot_password() {
      auth()
        .sendPasswordResetEmail(this.email)
        .then((user) => {
          const msg =
            "The reset password link has been sent to your email. Please check the inbox!!.";
          this.$toasted.global.success({ message: msg });
        })
        .catch((err) => {
          this.$toasted.global.error_post({ message: err.message });
        });
    },
  },
};
</script>
<style module lang="stylus">
@require '~@styles/anims';

.authContainer {
  $font-size: 16px;
  font-family: courier, monospace;
  max-width: 800px;
  margin: auto;
  width: 100%;
  border: 2px solid $vermilion;
  border-radius: 10px;
  box-shadow: inset 0px 0px 10px $vermilion;

  h3 {
    text-align: center;
    color: $vermilion;
  }
}

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 200px 0;
  position: relative;
  top: 0;
  z-index: 1;
  font-family: 'Roboto Mono';
  $font-size: 18px;
}

.root {
  height: 100vh;
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
  max-width: 600px;
  width: 100%;
  $font-size: 16px;
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
    color: $vermilion;
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
  $font-size: 40px;
  height: 40px;
  width: 40px;
  justify-content: space-between;
  cursor: pointer;
  text-align: right;

  &:hover {
    color: $vermilion;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
