<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <div :class="$style.formContainer" slot="basic">
          <form :class="$style.form">
            <div :class="$style.card" v-show="navIndex==0">
              <h3>basic</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="name" :class="$style.label">name</label>
                  <input type="test" :class="$style.field" value v-model="name" required>
                </div>
                <div :class="$style.field">
                  <label for="gender" :class="$style.label">gender</label>
                  <select :class="$style.field" v-model="gender" required>
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                    <option value="2">Others</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="phone" :class="$style.label">phone</label>
                  <input type="phone" :class="$style.field" v-model="phone" required>
                </div>
                <div :class="$style.field">
                  <label for="country" :class="$style.label">country</label>
                  <input type="country" :class="$style.field" v-model="country" required>
                </div>
                <div :class="$style.field">
                  <label for="instituteType" :class="$style.label">institute type</label>
                  <select :class="$style.field" v-model="instituteType" required>
                    <option value="0">School</option>
                    <option value="1">College</option>
                    <option value="2">Proffesional</option>
                  </select>
                </div>
              </div>
            </div>
            <div :class="$style.card" v-show="navIndex==1">
              <h3>academic</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="institute" :class="$style.label">institute</label>
                  <input type="text" v-model="institute">
                </div>
                <div :class="$style.field">
                  <label for="year" :class="$style.label">year</label>
                  <input type="number" name="year" :class="$style.field" v-model="year">
                </div>
                <div :class="$style.field">
                  <label for="branch" :class="$style.label">branch</label>
                  <select type="text" name="branch" :class="$style.field" v-model="branch">
                    <option value="cse">CSE</option>
                    <option value="noncse">Non-CSE</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="degree" :class="$style.label">degree</label>
                  <input type="degree" :class="$style.field" v-model="degree">
                </div>
              </div>
            </div>
            <div :class="$style.card" v-show="navIndex==2">
              <h3>handles</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="codeforce" :class="$style.label">codeforces</label>
                  <input type="text" v-model="codeforces">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button type="submit" value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </div>

            <div :class="$style.formNav">
              <i class="fas fa-circle" @click="nav(0)" :class="navIndex==0?$style.active:''"></i>
              <i class="fas fa-circle" @click="nav(1)" :class="navIndex==1?$style.active:''"></i>
              <i class="fas fa-circle" @click="nav(2)" :class="navIndex==2?$style.active:''"></i>
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

export default {
  components: {
    AppBar,
    Footer,
    TabLayout
  },
  data() {
    return {
      profile: null,
      navIndex: 0
    };
  },
  methods: {
    nav(index) {
      var form = document.querySelectorAll("form")[0];
      if (form.checkValidity()) {
        this.navIndex = index;
      } else form.querySelectorAll("button")[0].click();
    }
  },
  created() {
    API.fetch("profile/", { token: this.$store.getters.authToken })
      .then(({ data }) => {
        this.profile = data;
        if (!data.is_profile_complete) this.navIndex = 0;
        else this.navIndex = 2;
        console.log(data);
      })
      .catch(console.log);
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
      margin: auto;
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

      .formNav {
        width: 100%;
        text-align: center;
        border: 1px solid $chartreuse;
        border-top: 0;
        padding: 20px;
        margin: 0 10px;
        border-radius: 0 0 4px 4px;

        i {
          cursor: pointer;

          &.active {
            color: $chartreuse;
          }
        }
      }

      .card {
        border: 1px solid $chartreuse;
        border-radius: 4px 4px 0 0;
        box-shadow: inset 0px -2px 5px $chartreuse;
        padding: 20px;
        margin: 10px 10px 0;
        width: 100%;
        min-height: 400px;

        h3 {
          color: $chartreuse;
          text-align: center;
          text-transform: uppercase;
        }

        .fieldsContainer {
          width: 100%;
          margin-bottom: 20px;
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
            margin-bottom: 20px;
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
            margin-bottom: 20px;
          }
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
          font-size: 30px;
          height: 30px;
          width: 30px;
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
      }
    }

    @media screen and (max-width: 769px) {
      .wrapper {
        width: 90%;
      }
    }
</style>
