<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <TabLayout :tabs="tabs">
          <div :class="$style.formContainer" slot="basic">
            <form :class="$style.form" @submit.prevent>
              <div :class="$style.fieldContainer">
                <div :class="$style.field">
                  <label for="gender" :class="$style.label">gender</label>
                  <select :class="$style.field" v-model="gender">
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                    <option value="2">Others</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="phone" :class="$style.label">phone</label>
                  <input type="phone" :class="$style.field" v-model="phone">
                </div>
                <div :class="$style.field">
                  <label for="instituteType" :class="$style.label">institute type</label>
                  <select :class="$style.field" v-model="instituteType">
                    <option value="0">School</option>
                    <option value="1">College</option>
                    <option value="2">Proffesional</option>
                  </select>
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button value="<" :class="$style.submit">
                  <i class="fas fa-arrow-circle-left"></i>
                </button>
                <button value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </form>
          </div>

          <div :class="$style.formContainer" slot="academic">
            <form :class="$style.form" @submit.prevent>
              <div :class="$style.fieldContainer">
                <div :class="$style.field">
                  <label for="institute" :class="$style.label">institute</label>
                  <input type="institute" v-model="institute">
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
              <div :class="$style.btnStyle">
                <button value="<" :class="$style.submit">
                  <i class="fas fa-arrow-circle-left"></i>
                </button>
                <button value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </form>
          </div>

          <div :class="$style.formContainer" slot="handles">
            <form :class="$style.form" @submit.prevent>
              <div :class="$style.fieldContainer">
                <div :class="$style.field">
                  <label for="codeforce" :class="$style.label">codeforces</label>
                  <input type="text" v-model="codeforces">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button value="<" :class="$style.submit">
                  <i class="fas fa-arrow-circle-left"></i>
                </button>
                <button value=">" :class="$style.submit">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </form>
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
      tabs: [
        {
          name: "basic",
          title: "Basic"
        },
        {
          name: "academic",
          title: "Academic"
        },
        {
          name: "handles",
          title: "Handles"
        }
      ]
    };
  },
  methods: {}
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
