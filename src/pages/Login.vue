<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <TabLayout :tabs="tabs">
          <div :class="$style.formContainer" slot="login">
            <Form :form="loginForm" :id="login" ref="login" :class="$style.login"/>
            <div :class="$style.social">
              <a href="#">
                <img src="assets/social/google.png" :class="$style.socialButton">
              </a>
              <a href="#">
                <img src="assets/social/facebook.png" :class="$style.socialButton">
              </a>
              <a href="#">
                <img src="assets/social/github.png" :class="$style.socialButton">
              </a>
            </div>
          </div>

          <div :class="$style.formContainer" slot="register">
            <Form :form="registerForm" :id="register" ref="register" :class="$style.register"/>
            <div :class="$style.social">
              <a href="#">
                <img src="assets/social/google.png" :class="$style.socialButton">
              </a>
              <a href="#">
                <img src="assets/social/facebook.png" :class="$style.socialButton">
              </a>
              <a href="#">
                <img src="assets/social/github.png" :class="$style.socialButton">
              </a>
            </div>
          </div>
        </TabLayout>
      </div>
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Form from "@components/Form";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";
export default {
  components: {
    AppBar,
    Form,
    Footer,
    TabLayout
  },
  methods: {},
  data() {
    return {
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
      loginForm: {
        fields: [
          {
            label: "email",
            name: "email",
            type: "text"
          },
          {
            label: "password",
            name: "password",
            type: "password"
          }
        ],
        submitText: "login"
      },
      registerForm: {
        fields: [
          {
            label: "name",
            name: "name",
            type: "text"
          },
          {
            label: "email",
            name: "email",
            type: "text"
          },
          {
            label: "password",
            name: "password",
            type: "password"
          },
          {
            label: "confirm password",
            name: "confirm-password",
            type: "password"
          }
        ],
        submitText: "register"
      }
    };
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
    margin: 10px;
    width: 40px;
    height: 40px;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
