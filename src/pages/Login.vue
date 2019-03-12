<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.tabs">
        <div :class="[$style.tab, isLoginTab ? $style.active : '']">login/register</div>
        <!-- <div
          :class="[$style.tab, !isLoginTab ? $style.active : '']"
          v-on:click="toggleTabs"
        >register</div>-->
      </div>
      <div :class="$style.formContainer">
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
      <!-- <Form :form="registerForm" :id="register" ref="register" :class="$style.register"/> -->
    </main>
    <Footer/>
  </div>
</template>

<script>
import AppBar from "@components/AppBar";
import Form from "@components/Form";
import Footer from "@components/Footer";
export default {
  components: {
    AppBar,
    Form,
    Footer
  },
  methods: {
    toggleTabs(event) {
      console.log(this.$refs.login);
      this.isLoginTab = !this.isLoginTab;
      if (this.isLoginTab) {
        this.$refs.login.$el.style.display = "block";
        this.$refs.register.$el.style.display = "none";
      } else {
        this.$refs.login.$el.style.display = "none";
        this.$refs.register.$el.style.display = "block";
      }
    }
  },
  data() {
    return {
      isLoginTab: true,
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
@import '../styles/theme.styl';
@import '../styles/anims.styl';
@import '../styles/colors.styl';

.formContainer {
  background: #111;
  font-size: 16px;
  font-family: courier, monospace;
  position: relative;
  top: 0;
  left: 0;
  padding: 0;
  border: 1px solid $chartreuse;
  border-radius: 0 0 10px 10px;
  width: 100%;
  max-width: 600px;
  margin: auto;
  box-shadow: inset 0px 0px 20px $chartreuse;
}

.register {
  display: none;
}

.tabs {
  position: relative;
  top: -30px;
  width: 100%;
  margin: auto;
  max-width: 550px;
}

.tab {
  position: relative;
  cursor: pointer;
  float: left;
  background: $chartreuse;
  clip-path: polygon(10% 0%, 90% 0%, 100% 100%, 0% 100%);
  z-index: 11;
  height: 30px;
  line-height: 30px;
  width: 200px;
  text-align: center;
  color: #222;
}

.tab:not(:first-child) {
  left: -30px;
}

.active {
  background: $limeade;
  color: white;
  z-index: 12;
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
